print("hello git")

git config --global user.name "username"
git config --global user.email "email@email.com"

#git init
git init

#git status
    # 1. working directory (dossya dizine eklendiğindeki hali)
    # 2. staging area (add)
    # 3. git repo (commit)

#git add


#git commit

#git log

#git log --pretty=oneline


#git commit
# git commit -am "comment"

#git reset --soft commit_id



# soft : belirtilen committen sonraki commitleri siler. Dosyalardaki değişiklikler bozulmaz. Düzenlenmiş dosyalar git'e eklenir.
# git reset --soft HEAD~1



#mixed: belirtilen committen sonraki commitleri siler. Dosyalardaki değişiklikler bozulmaz. Dosyalar git'e eklenmeyecek(untracked hale gelecek)

#hard: belirtilen committen sonraki commitleri siler. Dosyalarda yapılan değişiklikler geri alınır. Yapılan her şey uçar.



# git branch -d new_feature2
# git checkout -b new_feature
