<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn5.telesco.pe/file/ltCLOSapohYYquOOO_HoIOPwWLYhGDPIJkU9KVOJ_nUgbkvypsXTMXAVTcDBm_4eIBoPQ9xvEHtuXAeAfqDsy2399ELCkVOD1KfKa1ZnpV0BEj_DlMugJ-MNHKfiVFK6OqtFb5ppDge7h0QM3KT6s7HjopPZe_-AVHszvD5sOfqwxU7VglJmnoYZOwxmyvrH_uKW5n5K-YyJVpHuQUyUlzea-x-vdh9MA9LJCzAyzDqDJvzFm319tp6qSN5CiOtDffwlwm0356ILyjmvzNGvCBKBaWSQvvaQZ0NsXVOQwUkEv24_OVmsV3Saa6NY9GssSZyNzvQAP1ajPrBKq7ac5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 404K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 22:30:47</div>
<hr>

<div class="tg-post" id="msg-107088">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53976f40f7.mp4?token=F8FmfRg7U6E20BO-MYrupZwOVD8QN4LFWy43FXWUB60oB-1V1R2QNsoc3VKdYt4TEU-TvopO-eJv5UWu1-aDyP7uUYsMngDx1v_fxm74gLZIbucx8Fp7gE1QVv8X2lClGi508ev0WJemfFzU-UZ2IAMLx27A8e2EMETelY3yJzAOYhc2b7ubanpk4lSHYJYWNAEACyrN7GpbagH8fYmoVUAAvDzpLB_SJxVLDmNmv85ucZNjE9zekDWe7keXVvIkVkdQcUT856cMKZrjRPoZFwAJPCCbgxYP6nwo4KowYZ9MYCu-r6Ym3zVJniRnCcHkOqaCINCP_J99QTr6gdB59TuDJKnQ_DhFHVvohmIgOcbXKLb3NTCxjR0VD7ZlaB2TP7l5yxb9fxox6FiZB1DM-kMCf2npf4pmAZuABSGcov2KNuad1iGaiUaNRdu28-s6Z1rCqS8mm7nbpmG4ERfmII7Y-dhOOJlXO4PGmVgn5lNg28Jd3pW7A1jW7vxJUTtkYh-SEUPuTfWKqEuZGRYtJvREHL97Hi9hswLh9tO5BaGa7Ad3WGGh2nnDf-L-y-5jx_xzVx1OGinjTDtWLEhSAubzaknmndJ0o49_lHfE2_dNb-GP8cn2giUZh-HAdI9sexzmrGUSIdS_tzkBOq-t56Ja_yxert2jUkjfKG8QSa0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53976f40f7.mp4?token=F8FmfRg7U6E20BO-MYrupZwOVD8QN4LFWy43FXWUB60oB-1V1R2QNsoc3VKdYt4TEU-TvopO-eJv5UWu1-aDyP7uUYsMngDx1v_fxm74gLZIbucx8Fp7gE1QVv8X2lClGi508ev0WJemfFzU-UZ2IAMLx27A8e2EMETelY3yJzAOYhc2b7ubanpk4lSHYJYWNAEACyrN7GpbagH8fYmoVUAAvDzpLB_SJxVLDmNmv85ucZNjE9zekDWe7keXVvIkVkdQcUT856cMKZrjRPoZFwAJPCCbgxYP6nwo4KowYZ9MYCu-r6Ym3zVJniRnCcHkOqaCINCP_J99QTr6gdB59TuDJKnQ_DhFHVvohmIgOcbXKLb3NTCxjR0VD7ZlaB2TP7l5yxb9fxox6FiZB1DM-kMCf2npf4pmAZuABSGcov2KNuad1iGaiUaNRdu28-s6Z1rCqS8mm7nbpmG4ERfmII7Y-dhOOJlXO4PGmVgn5lNg28Jd3pW7A1jW7vxJUTtkYh-SEUPuTfWKqEuZGRYtJvREHL97Hi9hswLh9tO5BaGa7Ad3WGGh2nnDf-L-y-5jx_xzVx1OGinjTDtWLEhSAubzaknmndJ0o49_lHfE2_dNb-GP8cn2giUZh-HAdI9sexzmrGUSIdS_tzkBOq-t56Ja_yxert2jUkjfKG8QSa0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
توضیحات بازگشا سخنگوی پرسپولیس درباره شکایت از آسانی به کمیته استیناف
🔻
فردا به آقای تاج و فدراسیون فوتبال نامه می‌زنیم و سه درخواست داریم. حضور وکلای پرسپولیس، ضبط جلسه و پخش آنلاین جلسه رسیدگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/Futball180TV/107088" target="_blank">📅 22:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107087">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvrJb56T6Q2UV67fYclxjWB1qHfL_jZ9A6MP5pglerxx7wjvvlIfsJoGVB6eZjtF15h5owESIFaHGjLWcAYSyNj4xX79qRWq7JTmUQQNsHZnC8974dJYm2BGqSmb9PboeOljix5QeqEq0SdLpnnxAgekY6LPidYWnKN7uJ5T9CqHDkUH8ib2DdnqYJ-nWd_utSoi1zOZxVak4H87cVef-Zzt_nix6QPrf6k9JaFPXp8JMfKeKRNF2WFAbaX66DCn4UhLmXriDkb2poyJRNsV690U6e3NB2V_Ezz0joKyrc0_vwTsYb4e92ducN9CIXZo1TyoQYxWmcHMwrhd2ZoBJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
جمهوری آذربایجان رسماً پروازها به ایران را تا اطلاع ثانوی متوقف کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/Futball180TV/107087" target="_blank">📅 21:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107086">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91400e175a.mp4?token=GPgHgjjEi_3QrZWZdF96eKuBDL2bdqY2dWJmLK0IKbyj88qRWSrKoEnzcLknDfggnj2PYnrMVew6Czh6XDKUCDWwIcnegh8jQpTqyH0XghxsVGEuJArz1aj3SE91nrz6vs3AcvqqpMEqrlIzWjJCQ5RmU8-ZQ2OYdtzRW0xrRut-sLKdPQlDZmgZU-tET84MD7glIlBr9AZFxpEUinFM-DH5jNKVoRRRwVyqZGAcqjlTFyoVBEfwyV5Ho4HpM0zbunpUaqNQ6jY5BLIjEWihcTKKjwOmQIR272nON6wY1YvBKogTC_ghHS2HrZh5mmvGhXnoVZIiVbyyp09De9uwVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91400e175a.mp4?token=GPgHgjjEi_3QrZWZdF96eKuBDL2bdqY2dWJmLK0IKbyj88qRWSrKoEnzcLknDfggnj2PYnrMVew6Czh6XDKUCDWwIcnegh8jQpTqyH0XghxsVGEuJArz1aj3SE91nrz6vs3AcvqqpMEqrlIzWjJCQ5RmU8-ZQ2OYdtzRW0xrRut-sLKdPQlDZmgZU-tET84MD7glIlBr9AZFxpEUinFM-DH5jNKVoRRRwVyqZGAcqjlTFyoVBEfwyV5Ho4HpM0zbunpUaqNQ6jY5BLIjEWihcTKKjwOmQIR272nON6wY1YvBKogTC_ghHS2HrZh5mmvGhXnoVZIiVbyyp09De9uwVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد چلغوز گودرزی رو داشته باشید که دوباره تصمیم گرفته بره مقبره کوروش
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/107086" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107085">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
تمرین تیم‌ملی فرانسه
✔️
کلاس آموزشی تیپ زدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/Futball180TV/107085" target="_blank">📅 21:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107084">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🙂
💥
مسکات حلال‌خور اتلتیکو مینیرو برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/107084" target="_blank">📅 20:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107083">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8c040c455.mp4?token=CCnwhkUubhuErj1LyQqqfSZfNzghWDsYj4_aUv4QzwqNYdg6UCYqH7pUR5UZKnZzfRkhyunXOuaz3khAgf68VM2bHLi4HMbE-tTreALdARNKURLONFMqR6QmRCUUebxwySIApPrvIABEwzuHp_pW_bpytSUec420NqF18YtXI89mrNsVz6rT0ZKn97T3OR2SRxo8qmI1DfvkbdOshE_qH6VD3HogVo9j3ugvVzxs7I66ygumCd8hMYYwSMCt1ygXeK77Wd6e08e5jmpPLqzI3IfZ8K1JZRC8g2teqCJZ5YCHKnewcso5SptxqrtUT7N1jNHu8_2ZWRSbNmmyzkhbpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8c040c455.mp4?token=CCnwhkUubhuErj1LyQqqfSZfNzghWDsYj4_aUv4QzwqNYdg6UCYqH7pUR5UZKnZzfRkhyunXOuaz3khAgf68VM2bHLi4HMbE-tTreALdARNKURLONFMqR6QmRCUUebxwySIApPrvIABEwzuHp_pW_bpytSUec420NqF18YtXI89mrNsVz6rT0ZKn97T3OR2SRxo8qmI1DfvkbdOshE_qH6VD3HogVo9j3ugvVzxs7I66ygumCd8hMYYwSMCt1ygXeK77Wd6e08e5jmpPLqzI3IfZ8K1JZRC8g2teqCJZ5YCHKnewcso5SptxqrtUT7N1jNHu8_2ZWRSbNmmyzkhbpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
🇮🇷
پیش بینی چند هوش مصنوعی مختلف از قهرمان فصل گذشته لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/107083" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107082">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=fDbswZjmKyf0a6c4ngKyYoQFm-38xtRH_8fMAyElQxdKk3isO_BJkcsYSibQhIo5rXM1M4QqNgjf-fd3j2wT6u3h9eS8RpZ4Po_J2PQZfFnq7zQ0Bk2GivnO2-8ENvX-avW25oWdrJW6yME9Abhzx17X4ctbp4IiVhGg37FvrEOXGBhjSkkDqLoZBOTys4sibPpho3K94ngeRDAWL06vfOA7fAGo0E4zN3W-b6u5K500jCnm9dfDQ8YjcHIWlnrKZakVIIBrPIpDUviAs1Bjr8b6gB4iRemt4tfqpwXoVkt7gi0xuTUfYZbCHB4ruhz3uGWzKZisFGFfki7GxycT5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=fDbswZjmKyf0a6c4ngKyYoQFm-38xtRH_8fMAyElQxdKk3isO_BJkcsYSibQhIo5rXM1M4QqNgjf-fd3j2wT6u3h9eS8RpZ4Po_J2PQZfFnq7zQ0Bk2GivnO2-8ENvX-avW25oWdrJW6yME9Abhzx17X4ctbp4IiVhGg37FvrEOXGBhjSkkDqLoZBOTys4sibPpho3K94ngeRDAWL06vfOA7fAGo0E4zN3W-b6u5K500jCnm9dfDQ8YjcHIWlnrKZakVIIBrPIpDUviAs1Bjr8b6gB4iRemt4tfqpwXoVkt7gi0xuTUfYZbCHB4ruhz3uGWzKZisFGFfki7GxycT5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
ترامپ: آمریکا و ایران قطعاً به نتیجه خواهند رسید؛ به هر طریقی که باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107082" target="_blank">📅 18:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107081">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=INNuUvfiafSKiWbIw0vngbqI_K5XbQDC-Sq6PuWbKODhUipACbdkXor0K-EBsmOpXYZDlRozfUQzp9mt6GDtDX9weMegBwK205SGEHIJSOEulATvPqQWuP-Kb20rDMVjZqtFoveq550WHc9kUE0GFUp_ET86Ngzhyj7l14z5gp86fYyEh1RCbQcOjFWxDHdlFkHdmVmEJ7P4gpmeCvyGgOTu11fXMferCasJUVnKfWQc_ff1yQi68zpdrlIazlPnWtv0UNOuj5R7fcJnyS98I1jmj8HCJI1UDvgCdEX9AL6546g_nAcbIHidVJ1VKW-Mm255q7TNx3SZrOt6hEkf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=INNuUvfiafSKiWbIw0vngbqI_K5XbQDC-Sq6PuWbKODhUipACbdkXor0K-EBsmOpXYZDlRozfUQzp9mt6GDtDX9weMegBwK205SGEHIJSOEulATvPqQWuP-Kb20rDMVjZqtFoveq550WHc9kUE0GFUp_ET86Ngzhyj7l14z5gp86fYyEh1RCbQcOjFWxDHdlFkHdmVmEJ7P4gpmeCvyGgOTu11fXMferCasJUVnKfWQc_ff1yQi68zpdrlIazlPnWtv0UNOuj5R7fcJnyS98I1jmj8HCJI1UDvgCdEX9AL6546g_nAcbIHidVJ1VKW-Mm255q7TNx3SZrOt6hEkf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
ترامپ: انتخابات هیچ تأثیری بر تصمیم من درباره ایران ندارد و تنها تمرکز من بر عدم دستیابی این کشور به سلاح هسته‌ای است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107081" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107080">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
⭕️
⭕️
ترامپ: باید تصمیم بزرگی بگیرم درباره اینکه آیا می‌خواهم ایران را نابود کنم یا اجازه دهم به حیات و شکوفایی خود ادامه دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107080" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107079">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e271237b80.mp4?token=DmCkZtTyAdTRuQT--ms66eXgWooxIRg4MivA4olEXN_MFywlrofUbFkgxolW8LXdn2TG5tJquLslCR3e7SXzkeFfFQoq2eARJ-or61bL5RNVmNJQ-HYg7_mOBWLQbBaS2JtTPsV5VdTJb5wnYpbNKXTMtl15itjjLyU5EpOwybFkBb8DDc1woLPKYbtgvtL_tidlkhTC9CgsfuxpPnxjYliaNEyxmzFgjCdlUzWVTXvOrOfZPRuB68EWuAEeAWUQJmIdL640a1x7F6lP3ZXtkfQUSVk6O3BneAEEFdBZfJcRUS5qPh9NrIo6fjCfijIhmoK6KQK14SGWypsVpZlrNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e271237b80.mp4?token=DmCkZtTyAdTRuQT--ms66eXgWooxIRg4MivA4olEXN_MFywlrofUbFkgxolW8LXdn2TG5tJquLslCR3e7SXzkeFfFQoq2eARJ-or61bL5RNVmNJQ-HYg7_mOBWLQbBaS2JtTPsV5VdTJb5wnYpbNKXTMtl15itjjLyU5EpOwybFkBb8DDc1woLPKYbtgvtL_tidlkhTC9CgsfuxpPnxjYliaNEyxmzFgjCdlUzWVTXvOrOfZPRuB68EWuAEeAWUQJmIdL640a1x7F6lP3ZXtkfQUSVk6O3BneAEEFdBZfJcRUS5qPh9NrIo6fjCfijIhmoK6KQK14SGWypsVpZlrNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
ترامپ: ایران موشکی با قابلیت هدف قرار دادن اروپا ساخته بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107079" target="_blank">📅 18:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107078">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=SCXsAgoaDI2e3qdcUkT4zANZxMPlkwCFtzS_QLqnAeqmLyZpX38e8SQVMYAsoch6fsQwZk5AIF3roUvl5nEEw2Osn9kLMqq48B42F9THLjGeHqKvuEM5HsFZNmBC62WFsZCYrgULyvFgpK-I98YNxiH6sGN43RlmdWMuy9UVK0FsMA8Hu-Cd9rxZvWq04lKSORp4ZowSD3LJpCgDTdhm4-E4bXNAYDMKcgM9ZctBxo0uu3tH1QzKbE_PXM4sFKDRZU_QdgwhC6rbHCDQ2_Y7KTwxz_FKH7vr9XgLHjb1pE4ny3-Y8rzFKKsVKf3nlASyFDkO-p6fqchVBJndpOiwWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=SCXsAgoaDI2e3qdcUkT4zANZxMPlkwCFtzS_QLqnAeqmLyZpX38e8SQVMYAsoch6fsQwZk5AIF3roUvl5nEEw2Osn9kLMqq48B42F9THLjGeHqKvuEM5HsFZNmBC62WFsZCYrgULyvFgpK-I98YNxiH6sGN43RlmdWMuy9UVK0FsMA8Hu-Cd9rxZvWq04lKSORp4ZowSD3LJpCgDTdhm4-E4bXNAYDMKcgM9ZctBxo0uu3tH1QzKbE_PXM4sFKDRZU_QdgwhC6rbHCDQ2_Y7KTwxz_FKH7vr9XgLHjb1pE4ny3-Y8rzFKKsVKf3nlASyFDkO-p6fqchVBJndpOiwWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
ترامپ در سازمان ملل: به ایران در ازای پایان برنامه هسته‌ای و حمایت از تروریسم، همکاری کامل اقتصادی پیشنهاد دادم؛ اما نپذیرفتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107078" target="_blank">📅 18:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107077">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4439db1dc.mp4?token=BK0fSH-g1Jt-Pw40hy3XKsYiguYgTzbdPBdL_jyn3SN_tHUentSTkju_lsJdpf26bITqzY3E5UMyrvjDU-AWrUuRjZzObJxjEMQIqeU3hJadwTxikFY4oIiF9l0XP64c34mI8Ih6JMI0SXZlrJdKj5WES7n6VXrE_QFlD7UoyJfaXL1BAsDPLxil8QFqkeRIdv1aPGDCXFC2m1VKBJOngrE1KiWaHnygU6IJLqNACKWtdxl8nJOMEKWIBKuBKLw7KkAVOmOaa6ZqHbBwB-hdA71YWXcPacx1f_g3fqr3iv4VGd719eWM1EbhpWd0zyHPcfgYiq9zKQFDJ8aguh_vqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4439db1dc.mp4?token=BK0fSH-g1Jt-Pw40hy3XKsYiguYgTzbdPBdL_jyn3SN_tHUentSTkju_lsJdpf26bITqzY3E5UMyrvjDU-AWrUuRjZzObJxjEMQIqeU3hJadwTxikFY4oIiF9l0XP64c34mI8Ih6JMI0SXZlrJdKj5WES7n6VXrE_QFlD7UoyJfaXL1BAsDPLxil8QFqkeRIdv1aPGDCXFC2m1VKBJOngrE1KiWaHnygU6IJLqNACKWtdxl8nJOMEKWIBKuBKLw7KkAVOmOaa6ZqHbBwB-hdA71YWXcPacx1f_g3fqr3iv4VGd719eWM1EbhpWd0zyHPcfgYiq9zKQFDJ8aguh_vqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
تعریف عجیب علیرضا علیزاده از نوید عاشوری که موجب پاره شدن دوباره عادل شد: گفتم ازدواج نکرده بودی، با هم زندگی می‌کردیم!
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107077" target="_blank">📅 18:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107076">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e179f3429.mp4?token=FsPVF0DODLQhfUuUk3SWSyLyYnips3_X-Hr1QKk3vD3XmOe9K8BBHp2YPG9XpVheGRODUquH3mGjabYHfzL-zl_9ZsbMxbyMkXLOmtNCfZNV6kSrvhdfzs7dQv_c4P1JNE30coHLzJ6khhlQJlH7PWFOYDGqhMt9_wxuNmdDw1Ccetc4nCxM76jq_Ejtz-gxDbtjHLyHBW0SzG24mKpr96V3G4WbV-nO1XCCT0iDYHaahKbxx5JJ4uShS72q79gDpLJBOlIlIBQyFLNKIS--oUVXnSji6RwY0b7dF9O_uZqTNGTsrfy2Z3PQTiHaioRIO41Oq-htuVpPXSoNsagT-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e179f3429.mp4?token=FsPVF0DODLQhfUuUk3SWSyLyYnips3_X-Hr1QKk3vD3XmOe9K8BBHp2YPG9XpVheGRODUquH3mGjabYHfzL-zl_9ZsbMxbyMkXLOmtNCfZNV6kSrvhdfzs7dQv_c4P1JNE30coHLzJ6khhlQJlH7PWFOYDGqhMt9_wxuNmdDw1Ccetc4nCxM76jq_Ejtz-gxDbtjHLyHBW0SzG24mKpr96V3G4WbV-nO1XCCT0iDYHaahKbxx5JJ4uShS72q79gDpLJBOlIlIBQyFLNKIS--oUVXnSji6RwY0b7dF9O_uZqTNGTsrfy2Z3PQTiHaioRIO41Oq-htuVpPXSoNsagT-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعضی‌وقتا آدم فکر میکنه لیونل‌مسی تو زمین فوتبال بیشتر از دوتا چشم داره
😐
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107076" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107075">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107075" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/107075" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107074">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbXdsNWAYzs41p9iduL7ZmBlkLm4UGFx2s8VK0AYO0gqNJ-n67jfEXn34NeU6aumiqwRBb5D_-TOtBQcQ2MzixV7D0lfGZOkHxQiOff1mOkadmFGl_mgn_2k5k2m82eL834Fs6ZmMUbriqbNhItSG3ymxWswey-XPRszcaSHzD9qygsjSBgMNnHYUA-ngajxm9aJ8bdrJMR8FYiKS9s1eBICCH904FX9Vo3lo1iatqD54iavgKUFtucTgNYsGMnnwFhhDC30SvOW2fd-OBVTTJsfQAh8AWB9rp9vHHrEMpBueeBr4eQNnbZPnDz9xo8vZeeAj3PFES5hdz0vbl2Uqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107074" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107073">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvQTvCy-UGXTdYtVYWQCeh6EnyZOr7KUtYTZ2ntth0nSXh9Ktwi5ajMMiqMndLAS_bqzgt7wR4X_eDcS6uBUk8s_uAgnqzZcjGJhB4P1yDPtpiUzStMJEEqbCfpt6Y2cjdD0vKW-1A0GyyeRjfPk1QXfdcknf8AlKTGrQM2K2tNZdmZoW-rRIJcBJOwk3FL3qsTyuyfNP6ujV5KbGd3wr4KeHYW_i4veVbJOVromlBD-TdOKViGFms5lUPDGYAZal8IgXfaZU_KWpGnxypaon7T1viVa8tE3OaboDQZGVN7-Sei9PLTx-pM1k92aHNRtkUXTl9B7pnAFfRPhHUPCtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇪🇸
لامین یامال :
🔻
به نظرم همون‌طور که می‌گن، توپ طلا جایزه بهترین بازیکن ساله؛ برای بازیکنی که متفاوته، از تماشای بازی کردنش لذت می‌بری و حتی فقط برای دیدن اون بازیکن حاضر می‌شی بری استادیوم. فکر می‌کنم توپ طلا برای همون بازیکن متفاوته؛ ربطی به تعداد گل‌هایی که می‌زنه یا چیزای دیگه نداره.
🔻
وقتی به توپ طلا فکر می‌کنم، یاد مسی، رونالدینیو و بازیکنایی از این دست می‌افتم. اونا متفاوتن و وقتی بازیشون رو می‌بینی، باعث می‌شن لبخند بزنی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/107073" target="_blank">📅 17:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107072">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjjS0dshSJIOo3ewQoIK3lTSm0k9dvoKWFPbuIkj5m5HOjqywqTlOu0ZxnaxlFz6nS2g9TICRJmVucgJ6Fh6WDClm5Rx49HPD_T-IDH_fnaIbWvB4dG0_e4u84Mn4o9TAh514NwONk30N_Mo3cuypOJYEAePeIemkO_iTT6hiBJhMCBlcpUJnOQPEDpoXD__sUZ4Gt9laZ4oETcaS8WI6gKrFUJ4zh0_TmpOkRRFlNNnSXPmWgJ3wQvIWcD8bxhTyH3eUb1phV_igbD0VsY4B08gvXl0THt8nvCsG1N2CZRXbk9ln2y1a5KgCG_gJunqOohAyScIBYWJDFETMSsPog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
قرارداد جدید آرسنال با آرتتا بزودی امضا میشه و این سرمربی به مدت طولانی قراردادش رو تمدید میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/107072" target="_blank">📅 17:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107071">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ec90abeb5.mp4?token=GZ58PbUlv6UOPBqhEPuUd9msx_MLIdG7vRnD057r_1Tr0gdsfwsd0v02bmJ-Ou-Bf1xdgXR9Do88LW6OahqU05d9Q83PnlOpd1yuy64u3WQc9L5IiifVTmGXDFlWbsIkuoTKz_YU8RODoICGrv_luYRUcCpFIWRv6WI24F0oJ--RHnBZzixIlS2mHsK7HP0bIs7YWb79LbtRu_PJmd7_bdAbXIILklsRtwKcS8spr93Zbg-d41kKVpE3xKjF992Dg9tO0VYsZ5O9HyP6-K4oVzIugwDptYoTrLGqSgVIhsmDyBgX6XBIaDlwDlQSoZTt77HlVFSlX7zIPlOMQyFPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ec90abeb5.mp4?token=GZ58PbUlv6UOPBqhEPuUd9msx_MLIdG7vRnD057r_1Tr0gdsfwsd0v02bmJ-Ou-Bf1xdgXR9Do88LW6OahqU05d9Q83PnlOpd1yuy64u3WQc9L5IiifVTmGXDFlWbsIkuoTKz_YU8RODoICGrv_luYRUcCpFIWRv6WI24F0oJ--RHnBZzixIlS2mHsK7HP0bIs7YWb79LbtRu_PJmd7_bdAbXIILklsRtwKcS8spr93Zbg-d41kKVpE3xKjF992Dg9tO0VYsZ5O9HyP6-K4oVzIugwDptYoTrLGqSgVIhsmDyBgX6XBIaDlwDlQSoZTt77HlVFSlX7zIPlOMQyFPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارلتو، نشون بده یه مادریدیستای واقعی هستی.
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107071" target="_blank">📅 16:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107070">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9DIUVW5ZAcJe4nctCdvkT2ikBH20rz0WkkTbmi37YDi_ESPpl5kbAP1DuHsJlDYm6Jy7bsI2h5hJazrjdx01SO0xMhdAmGq6YzPNDz7XRFng-WY0UBXPQpkhmoSI571vIhCJ4IUTtcCh5SBGfXEwYdEdaoBt3Vu_wjMeqfhO2wU2bPqqstcOmzYY4t7cyWfMmd5Z397-YNZKeWKAUQ7a8ZejiObUCAUm1gNYiLkO6yrcLTK8W3CH5nQ8SwnjnNyM76-io90k-W1g-YSXQw_wdqSgt6WTHzTiP_lCjHob--qjnd4eAH2H3UK40l-cl0KSbW3VT6dFPWo9lCmKIfI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
سهراب بختیاری‌زاده برای نیم‌فصل خواهان جذب یک‌مهاجم خارجی، یک وینگر چپ خارجی و تلاش برای جذب محمد جواد حسین‌نژاد شده است. از سویی بازگشت خلیفه و گودرزی نیز جزو برنامه‌های بختیاری‌زاده در اعلام به تاجرنیا بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107070" target="_blank">📅 16:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107068">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsRslc9RyYkUCsyVjAGgRXDeTIYNqIcrEUA_O4s_geJLX2DFga3oucjt70xJgDbbkqNukWzr7xW42eZVXj_TW0F8AjD3QJQI81-IQ8yfSVFVSnvvpFuS-HiRbFh9L0tZO1eUNXlTcQGLr7gkNk-d9kHMGLbaNtzO8ZfihDZHA4H1trFFsHn_6rdGq79inC5rYKOouxvF6tEFH14dWHV2S9skiNOBm2LcV9tSSMjXyzh1x9TIJGBCU8VwGQX1hjZCrz5pTrhEcyUwEH1_pl_Cf0vVbv1rk2m75RWvj5RT6v9KGCTIB3Y72XOoO33JeAwxwmQFdABJrc-DOvMSa3J4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
اوج تلاش خداداد عزیزی برای درخواست بخشش از مردم بابت وویس زشتش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107068" target="_blank">📅 16:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107067">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpQN2oX7RexmtbYgSpvpznSfddddxJY4meBUMFz9jobwewiJDlP5PZwpFMjHPa6j0zoyv56nYfhGcqz93UK0To2_tQgKqRP3fGsGEbYr92yfAB9-a2l2Ze4D-O6oQceiCiKNjcWduZD26Ri6y7sN7oOssiIBCt0cw7-fiqd89gnzlQd7hm4q7VytyrqRWuBikfcGvKmtYYWiakhGn5YnGPn-XiVTaJfIIboLb1n7SCr3nj-Y-6GvCg2WEhUiMEGKw_wVu2wgL7vfBsa68ZmY507e9AkRSqcu2XlwOdaD9rAuGujAF3RtHyVyOap9wtORQHZ7Vkqx3QLBIklwmwVetA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عملکرد فوق‌العاده موناکو زیر دست فلیپه‌لوئیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107067" target="_blank">📅 16:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107066">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejWLkTb-fSAaBlH-QCuB9CVrIdKlJSZSlYLl7xF7qAiz51YfXL4iCnyDSThT4VWz0ujofc0hRbPo-Pj3ATJsXC4lFa1sPAsyl_QL0mpf3JPaWVm3yxREH33bryE5O6i6uelWGPyxhFw-YGfUePFsnU9-fLHN-4-Rx8_Ue1SyqoBsoMGCi9bxSWh6dwrJXkWd-Bq8_pVlFgKpnfA6IadVrGs7rhYv067vCgKERzHyKgjiZg1H_17Ng_2sPkbXMG8w3-ZgKprfbpG3WhIINZZRhXW72QnH_c8K_bo_JbCuorv_G1DoVCNf4emuuufF21sMXPwMaO1PKeYwjQ6Qkk5zKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهار
تیم با ۱۰۰ درصد برد اروپا تا پیش‌از فیفادی جاری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107066" target="_blank">📅 15:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107065">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_xtuGzSphCfLRbP4QuyWRhjObdm43cMVPcG7zk2pDbARgDySrf-I7m6D1vGHkKTw7KkrHgshCbB04pzPkFfMPD9m5_J-3BuWMELNsDLZj_QAyHOxNSqfmPfUr_ew_9vwqgKOGUEjabIMekRfoMZihnXsKbzOX9PmSaoKt5S5rQO9hz9ylzseYvk74n0-6PLv62RSIB7kAMGFh79cYTZ17gYhL6KsgjqWdLD8AC0otyLxHZwR9UNazMH49q5r9APl2_89rDwjx-N2ny335HO9zJEiz3PTd0m_SZkl13SBuhZX_GgZJGsQeOHKhb9DABDgKYQI_2BmZ8w6PizuWNWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⭕️
عربستان و چند کشور خاورمیانه در آستانه جام ملتهای آسیا با فشار به فیفا به دنبال تعلیق فوتبال ایران هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107065" target="_blank">📅 15:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107064">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74cce70e5a.mp4?token=itsRfMWXP9X8O8HnDzXobvtWUdlKSTgS6LErx1XigfU0TBH6-uyo_90kTnSJDw8GPfJL_nB3p4yUJqkILgUBUwd4Ge_iZqs8CAFtK0BPVkEx4c09F9qO9CiptgIaavNDMZHBTXbDPydsWGwZHRD5ZGrKQPraBuX44BEu5k2Nl4a-1Rk3oEQ9FxkxHhqbOIzviwbxxFXWEMnMXz7M84NGdBxacrDlUZRqxFZgEXxMSY9RDTs-6sL1D9_l6xs9FNSDwKnCFHM_-thk5Akr4VmU2h-7XElaFarFzcHmiNX3Kn3yjVP0P1SqRpeb8KpG8hjY15AsJw4MZfPbJiky0343Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74cce70e5a.mp4?token=itsRfMWXP9X8O8HnDzXobvtWUdlKSTgS6LErx1XigfU0TBH6-uyo_90kTnSJDw8GPfJL_nB3p4yUJqkILgUBUwd4Ge_iZqs8CAFtK0BPVkEx4c09F9qO9CiptgIaavNDMZHBTXbDPydsWGwZHRD5ZGrKQPraBuX44BEu5k2Nl4a-1Rk3oEQ9FxkxHhqbOIzviwbxxFXWEMnMXz7M84NGdBxacrDlUZRqxFZgEXxMSY9RDTs-6sL1D9_l6xs9FNSDwKnCFHM_-thk5Akr4VmU2h-7XElaFarFzcHmiNX3Kn3yjVP0P1SqRpeb8KpG8hjY15AsJw4MZfPbJiky0343Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
مرور هفته‌عجیب فوتبال در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107064" target="_blank">📅 14:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107063">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1af88a540.mp4?token=TTph6eWjpYjAT43dPx04vTfHA0hIYEi4w0eUU3qKsRjxdiDGyBFI6djDYUUleEFtsozt3cXdZChhS1YgGZqoxNpoeiuD-bUoC2_ud1oOIjeAi9VKGfYIQ1dZe9qzD124X40mybIl0wT1_PaaxKRLwyleQ0WcXNma9_4UjOtstYHAbXRicPWTfIR5RNn4FJ-82-pV1cabX2hNJTEhGbFP4oRBGl2KcNcFKrIW-oeTsTwaT-gTMux-pCfpCZPaAN_XNq9nDUWZiVkJ-VyJT55WGtLFNi37nTrZ2pVgsT41nYla3dbYYPHbAQD-T3FpsFdJFSt9_8BSDzGXRY7ELVVbTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1af88a540.mp4?token=TTph6eWjpYjAT43dPx04vTfHA0hIYEi4w0eUU3qKsRjxdiDGyBFI6djDYUUleEFtsozt3cXdZChhS1YgGZqoxNpoeiuD-bUoC2_ud1oOIjeAi9VKGfYIQ1dZe9qzD124X40mybIl0wT1_PaaxKRLwyleQ0WcXNma9_4UjOtstYHAbXRicPWTfIR5RNn4FJ-82-pV1cabX2hNJTEhGbFP4oRBGl2KcNcFKrIW-oeTsTwaT-gTMux-pCfpCZPaAN_XNq9nDUWZiVkJ-VyJT55WGtLFNi37nTrZ2pVgsT41nYla3dbYYPHbAQD-T3FpsFdJFSt9_8BSDzGXRY7ELVVbTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😏
🇪🇸
پست‌سمی تیم رئال‌بتیس از جدول لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107063" target="_blank">📅 14:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107062">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/068efa824d.mp4?token=GwPuKiL2pwf0EcasZo-5GxNGfJTLwZv-ehXnCrx28czI8AFpq4och-NXbMcTRQ2KW0fc3BM7Lp37h4u5P7rc6CKT9J7jhvsbXbx8lwtqlbVvwXXuEFlZ4LLGRAfR4SRxjjVPa2K_MHhs9cQy81nHE3xxbgJqG_7CfYOEu4sPekD-N7F9wpDqFYwfTPluvHL5CbW-5JxJEblYHwKWca0fB_D4C1NDWurXX1YqrDM6AeWovHklcZV1icPh5KPKMRd0QekSzw9a3jJAVXP5RAZW1LbQ1VWbnL7kwrAxIY-eZf72hnr82nh7GGXW3mgw1kHk88Bggwb-gfn5qwVGF-Yn1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/068efa824d.mp4?token=GwPuKiL2pwf0EcasZo-5GxNGfJTLwZv-ehXnCrx28czI8AFpq4och-NXbMcTRQ2KW0fc3BM7Lp37h4u5P7rc6CKT9J7jhvsbXbx8lwtqlbVvwXXuEFlZ4LLGRAfR4SRxjjVPa2K_MHhs9cQy81nHE3xxbgJqG_7CfYOEu4sPekD-N7F9wpDqFYwfTPluvHL5CbW-5JxJEblYHwKWca0fB_D4C1NDWurXX1YqrDM6AeWovHklcZV1icPh5KPKMRd0QekSzw9a3jJAVXP5RAZW1LbQ1VWbnL7kwrAxIY-eZf72hnr82nh7GGXW3mgw1kHk88Bggwb-gfn5qwVGF-Yn1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇮🇷
🇮🇷
شوخی ابوطالب‌حسینی با عدم قهرمانی پرسپولیس در آسیا و ناکامی‌های استقلال در دربی به سبک هوادار مشهور منچستریونایتد
😆
😆
😆
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107062" target="_blank">📅 14:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107061">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/709cbff54e.mp4?token=pQUJGSWD5tAVWNqLeE7GVWQFNlHMUyXuZBT635_gs7OR16EVhi-AmdTzYkweVGY3s23Gr6Ld3hHjPw215BuJW9Vh2eZ9Czfkdsixi-FW_eyP0CII6iP3FkxCJNaDcxm6eokWsbg_mmzGttLvna-jwdoUdB44j3OZzb7JiL5gfCSUEUwPVAbTeE_ws3CF3yBzq79cXPeJQj0E0TUmIANZcBEbj6l12O3n2NNpL72KGxIec7sl7MgKPCqonF4owbBrp6AhTJOyozXEFGjPo9vpU4QupQIZLFi6nVJQOCWzWmh3OrHeFwYgDQGDbMy_lGZo8UEr4tasbWouDSP1PE778w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/709cbff54e.mp4?token=pQUJGSWD5tAVWNqLeE7GVWQFNlHMUyXuZBT635_gs7OR16EVhi-AmdTzYkweVGY3s23Gr6Ld3hHjPw215BuJW9Vh2eZ9Czfkdsixi-FW_eyP0CII6iP3FkxCJNaDcxm6eokWsbg_mmzGttLvna-jwdoUdB44j3OZzb7JiL5gfCSUEUwPVAbTeE_ws3CF3yBzq79cXPeJQj0E0TUmIANZcBEbj6l12O3n2NNpL72KGxIec7sl7MgKPCqonF4owbBrp6AhTJOyozXEFGjPo9vpU4QupQIZLFi6nVJQOCWzWmh3OrHeFwYgDQGDbMy_lGZo8UEr4tasbWouDSP1PE778w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇳
🇸🇳
سادیو مانه با حضور در زادگاهش در کشور سنگال، مبلغ ۲۰ میلیون دلار را برای احداث یک پروژه با اشتغال‌زایی بیش از هزار نفر، سرمایه‌گذاری خواهد کرد. مانه اعلام کرده که بیشتر دستمزدش در دوران فوتبال را صرف رشد منطقه محروم خودش در سنگال خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107061" target="_blank">📅 13:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107060">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548065ddaf.mp4?token=uhlI1_lKCjwriiVu4VDdjkVZz2LHSLABGN7l6vJWeo_wxssD-XSeKGsbB419yxNAjDkQW1fD2ghpRFFvena4ranGrsLQXeipv20hvJrRr91QUWn-YZPSUKU7kAbOUPIgU087m0bdxMAXv5ZiI-FErwpd6BQkgDDsBFzTG4w6TbKWXeNWOaGHgGGyhVA430TpXP0ab8uSAiDbXVjJFgXtjTiuxP1vkO-78yvFNJMJIL57aqo5x1oXe74Lp4bt1gc7OJl8OSAeAXDQgcjMCD-IoLCFMPqDrfpjTJDo9A3B46at7NbXk0ggxeMH2jjAr7rSN0wb5mnJrMH25ysXhACP0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548065ddaf.mp4?token=uhlI1_lKCjwriiVu4VDdjkVZz2LHSLABGN7l6vJWeo_wxssD-XSeKGsbB419yxNAjDkQW1fD2ghpRFFvena4ranGrsLQXeipv20hvJrRr91QUWn-YZPSUKU7kAbOUPIgU087m0bdxMAXv5ZiI-FErwpd6BQkgDDsBFzTG4w6TbKWXeNWOaGHgGGyhVA430TpXP0ab8uSAiDbXVjJFgXtjTiuxP1vkO-78yvFNJMJIL57aqo5x1oXe74Lp4bt1gc7OJl8OSAeAXDQgcjMCD-IoLCFMPqDrfpjTJDo9A3B46at7NbXk0ggxeMH2jjAr7rSN0wb5mnJrMH25ysXhACP0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
علت جدایی ابوطالب از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107060" target="_blank">📅 13:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107059">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38289f78f.mp4?token=s0QGHYJcWSWaRk4KJg8BQ8DjdjFA-RLGvaHAzGpj8LCdVRpO_ZZs6c8O9ClK7E27KV0opBv6fTys1cvWl9YEd_z0GiWxu_4ZVn5yNibebqdDuJxvLB-MgsrVBF5LVj2QNnMU0TawSZAK64SeIjCixqHDE_0zd1axiSvS9hTId_q55uZ0BaRDJ6vPpsNOadW4n0pyTgaotHWZgWCgq5XJE5goxjZha4XKGS4jn7004tCTIwA7CgXYJFhOigHZKvknybERaDhwsBfCjNtPXBW4FM2aHF8WCcFM7wIAkJX4d7jm03nda2V4ssRDzsrcaENkjrJZaBZtLl-SAQTyxzs_6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38289f78f.mp4?token=s0QGHYJcWSWaRk4KJg8BQ8DjdjFA-RLGvaHAzGpj8LCdVRpO_ZZs6c8O9ClK7E27KV0opBv6fTys1cvWl9YEd_z0GiWxu_4ZVn5yNibebqdDuJxvLB-MgsrVBF5LVj2QNnMU0TawSZAK64SeIjCixqHDE_0zd1axiSvS9hTId_q55uZ0BaRDJ6vPpsNOadW4n0pyTgaotHWZgWCgq5XJE5goxjZha4XKGS4jn7004tCTIwA7CgXYJFhOigHZKvknybERaDhwsBfCjNtPXBW4FM2aHF8WCcFM7wIAkJX4d7jm03nda2V4ssRDzsrcaENkjrJZaBZtLl-SAQTyxzs_6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
‼️
دیس سنگین ابوطالب به خداداد عزیزی: قلب آدم صاف باشه نه پاهاش، شما قلبت پرانتزیه آقای خداداد عزیزی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107059" target="_blank">📅 13:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107058">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19fc9edd61.mp4?token=T4pWRefd2-auLeYzncGuQuGkTJoBLXoE5QdQv2KAhw_Nob8_wGKvMqn1SfETLMRTjcnUMrmJQgak5w0NVLl--0pFhQWfHqO-52ZAS7Hntb0LPipNjk0g5_PU7qqFb70jMqPblK1BDOADjL3VlgLLc0kWu1iwj652L1MBRVHUqjG1yr66x_1RnaZnQeBPvyXZ8NDWy5wd-wr20vsVyJGhrz2l9baK4X6OMYyWQw2YL0X6IQLwIov6U77HUIXAIJZZPSPoyY9bdClK_alFZKFYcck78BoUx8-o15CVHu0cjQzA_v1473kRmolXvzyzg-2YQV6ZHD7AUKey5dvqvPmgHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19fc9edd61.mp4?token=T4pWRefd2-auLeYzncGuQuGkTJoBLXoE5QdQv2KAhw_Nob8_wGKvMqn1SfETLMRTjcnUMrmJQgak5w0NVLl--0pFhQWfHqO-52ZAS7Hntb0LPipNjk0g5_PU7qqFb70jMqPblK1BDOADjL3VlgLLc0kWu1iwj652L1MBRVHUqjG1yr66x_1RnaZnQeBPvyXZ8NDWy5wd-wr20vsVyJGhrz2l9baK4X6OMYyWQw2YL0X6IQLwIov6U77HUIXAIJZZPSPoyY9bdClK_alFZKFYcck78BoUx8-o15CVHu0cjQzA_v1473kRmolXvzyzg-2YQV6ZHD7AUKey5dvqvPmgHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
‼️
ابوطالب حسینی ویس لو رفته خداداد عزیزی رو مودبانه ترجمه کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107058" target="_blank">📅 12:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107057">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nxu1REMRxhqvMrVb4RafdpYlqSIjNtBkfU2o4cTAZALYlmZSnCuoG_dT6Mu7Eeo2jmWbF1JpZQgE0yCy-I5ebfYPA_3ty2myRc3fci4xkURdgdozyshiDMM7ROh5G82_MmuIzCMslfXfWP2G_y-gM6hoJEzozFgkmXk6mupXtrGF-RJyJ49EEH7MUT6YDkwN6htQVV2bMt0_L3gNpqAVy29jQjzR4ssduo4joPKEaRO6pKMzbKE52T3xSwqGQt64FBtw23Ije4bMDz5Y1so5zxMNMJ_2IGkoP5nRSM6-Lb69EW8Gvdk3JLoxQva-DXPKllx-5ECub_saIV9bOJ4Jcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای ابوالفضل جلالی فکر کرده در عصر قاجاریه داریم زندگی می‌کنیم. چطور اینقدر راحت دروغ میگن
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107057" target="_blank">📅 12:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107056">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_Se-SuPYTTCVElS_1Re-ngyhptFqgaMkqUtBbkkjO28pxnA7TMXtjFyMvuxZfAczfMd5TrEs_i3KgL-Fft5lnir1Pil6YllufS5ziTAkQswyoyaf0zpepVQ1HxMxoBiCbADQnI_lPJ-b_6wZlxGt_AjVT-6gUpXJE6PmxyvGeXvSMi4GJGoQtgjJhQyflXCWaiUG9CF2VhtpJu6NxVtPNgb0dXmw93_FLKWmHTRQYKftuPgklDhWtTZzfDo-LPSK7dchW7dzcPdlju8VPeIeTOLx0vS0IIdjyXA1jmAF4Dw_wE5xlhrxv3I-0dfV2TJBMUZRrcUB-SXDqHk21yudw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جمع سن سه نفر جلو: 110 سال
احتمال فیکس شدن هر سه بازیکن تو جام ملتهای آسیا هم زیاده. جوان‌گرایی بی‌نظیر امیر قلعه نویی بعد از سال چهارم مربیگریش در تیم ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107056" target="_blank">📅 12:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107055">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa420985a.mp4?token=h5QHsx2ApRpJMVR4BV5dM39c4Oju8AolqNLq7zqOPkBESCDWCheJ2BzVT_PKxR91H9qHy1033IZ7tEs7-n59j1OcL11RThkhHSJUBuldJ6er-6bkQd9ANDAfzL3dT0cs8Qwwxb5y1iX14XMuNQWn7MJxRwFM0u1EXU4H74h28bb_YhC5Amw1SgsVPOJTB7Dz4jZSTsLjj4qrn8XfwC8wNN9tu00KlaaWNg2NW_7GtANCjp7IoKAcMdEjIb7BcjIx_S8OQRvQCcAq4Yz55hvckxuVM8OpJTAkicjegCeSbXmNxLDcvlJNBwFvrthSg6FjSS_-qoCo17xkUKse_4DPUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa420985a.mp4?token=h5QHsx2ApRpJMVR4BV5dM39c4Oju8AolqNLq7zqOPkBESCDWCheJ2BzVT_PKxR91H9qHy1033IZ7tEs7-n59j1OcL11RThkhHSJUBuldJ6er-6bkQd9ANDAfzL3dT0cs8Qwwxb5y1iX14XMuNQWn7MJxRwFM0u1EXU4H74h28bb_YhC5Amw1SgsVPOJTB7Dz4jZSTsLjj4qrn8XfwC8wNN9tu00KlaaWNg2NW_7GtANCjp7IoKAcMdEjIb7BcjIx_S8OQRvQCcAq4Yz55hvckxuVM8OpJTAkicjegCeSbXmNxLDcvlJNBwFvrthSg6FjSS_-qoCo17xkUKse_4DPUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما هم از فیفادی بدتون میاد
🙄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107055" target="_blank">📅 11:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107054">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c092ad06d.mp4?token=SIXfExxcTp2Hs4NaJw8RHAY8suqzhj89IMgxlqkuovHmBQfr1mcDC1TOVVDBLjQpvTuVFJsN5TUDDUnNmOIhlIhEje0WbKEH_EP1PzbMRxzx_PhRJ2s2UmB1tzQb6Co-JJycIWIb30D4SYYpr3bnMXO0ls_WjfB52QAH-07XhES2HRusYywgeluKsbqBDDlo-_XW1QbG1141-Se5RwIB94hOak9ug9TNjTU23xCYnDkperogIuTePZ5iZde5XYx9rHh2-XUOCnxmc8f-jcUtH7eiLstgIodvwN39INBAHtK6WpJKoOK6JMQTxCdDPOIV6-lYYnhcK3kYl1QWuQdVxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c092ad06d.mp4?token=SIXfExxcTp2Hs4NaJw8RHAY8suqzhj89IMgxlqkuovHmBQfr1mcDC1TOVVDBLjQpvTuVFJsN5TUDDUnNmOIhlIhEje0WbKEH_EP1PzbMRxzx_PhRJ2s2UmB1tzQb6Co-JJycIWIb30D4SYYpr3bnMXO0ls_WjfB52QAH-07XhES2HRusYywgeluKsbqBDDlo-_XW1QbG1141-Se5RwIB94hOak9ug9TNjTU23xCYnDkperogIuTePZ5iZde5XYx9rHh2-XUOCnxmc8f-jcUtH7eiLstgIodvwN39INBAHtK6WpJKoOK6JMQTxCdDPOIV6-lYYnhcK3kYl1QWuQdVxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇳🇱
اولین تمرین لاله‌های نارنجی زیر نظر ژاوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107054" target="_blank">📅 11:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107053">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107053" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107053" target="_blank">📅 11:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107052">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvs4FKoB-KAIoZCyB70qNE1-x6W1ImzMd05VYSNAKh5CCkqrdJ-AW_QkbtnLWerWZI0aWbPX25sr4QM31bkmPYN9vxdoufoLCSlX15W4frcT0pqZssXfkZ3npelpBgP8XbUI9Ayg18h3Pd2I7YhKBCSJhPgkVdAw10C0IdGecCG1mBGDw4UhNeP5G72m85I3A5j9Yxp1aCglZxB7ICj531BozJWoe075E3PVEvCZNcpKhihAnWTY6fjBevXgx54xiLVvopGpcwnJoIJR6_hHPktpNtDDgI7whZFKmOcK_ysWgFXJUfdqpCLKgiMNjXE5xbMMV_ejrlZrhI0xrMg80Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107052" target="_blank">📅 11:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107051">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5JSOOLoajzxOpFU5rKmpViaKxE5gTd6UlD9HbdlUiBNsuYWajI9ihENo3f9sDQUmMHbS-MXRlUF_89gVjYxRpcfIZi1nYxc1jpWDsd8FuBnVndsRB-arpqtw6sWqZ1cx7WDMJc-PlQBZnp7xknQUhg5JbGHbrSzcO6FMM4mlbGfPr2jOnrZRcBDUuc-VCyvljfuZQrTtpMPWtbaKnr3Wi45beelz2K3fIHGl387x7Ug-XLiTHu3DOs-ikw1caM6APtFrzdSqbssXMgZ3U9tX7OGsp1wH63VZLPP52JaE-J5LILRQ-z18X4kwKCdCx1GfVa0HDcoRn4nX0J7av9yXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
لیونل مسی ۲.۶ میلیون یورو برای کمک به ساخت مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
✅
این مرکز تخصصی سرطان کودکان در بیمارستان سنت خوآن دِ دئو بارسلونا قرار دارد و ظرفیت رسیدگی به حدود ۴۰۰ بیمار در سال را دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107051" target="_blank">📅 11:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107050">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26eae7147.mp4?token=qRHopVpmjKRcGewJxQsDN-xPkczp8FmLeD0vgpaKM0wvMNF9Mu2mMgO3lh8qrVa3ETyjp82MJ90jksdwuchGyBdmcRpfWEY9iPHSqPh8sj54M5-3Emj1B9Rw6h_3783aeb3_S2evcblGY-fn5i0xQD97JvkH_cHq2vIPcFRpGle2MGkg3TEWiFGurMkycxc-1NYVtEnQsfmaDPKNqtwPEwhyeEU7Hmb-SvlV7tNMHg1maJq15sTh5s_N16ozbj3xgaWh8YgGfBVWcohpChS5UBt-TL6yY3IrEiwnQ2Xy193Usp7i117zTaI9iI6-yme-KNC7IEDi8uxkXo8SLztACA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26eae7147.mp4?token=qRHopVpmjKRcGewJxQsDN-xPkczp8FmLeD0vgpaKM0wvMNF9Mu2mMgO3lh8qrVa3ETyjp82MJ90jksdwuchGyBdmcRpfWEY9iPHSqPh8sj54M5-3Emj1B9Rw6h_3783aeb3_S2evcblGY-fn5i0xQD97JvkH_cHq2vIPcFRpGle2MGkg3TEWiFGurMkycxc-1NYVtEnQsfmaDPKNqtwPEwhyeEU7Hmb-SvlV7tNMHg1maJq15sTh5s_N16ozbj3xgaWh8YgGfBVWcohpChS5UBt-TL6yY3IrEiwnQ2Xy193Usp7i117zTaI9iI6-yme-KNC7IEDi8uxkXo8SLztACA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
در این ویدیو پیرترین موجود زنده دنیا را مشاهده ‌می‌کنید، کوسه گرینلند که بیش از 390 ساله که در اعماق اقیانوس زندگی میکنه؛ این کوسه زمانی متولد شد که آیزاک نیوتون، موتسارت و چارلز داروین هنوز متولد نشده بودن؛ البته که گالیله 70 ساله و شکسپیر چندین سال قبل از دنیا رفته بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107050" target="_blank">📅 11:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107049">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b6b29a98b.mp4?token=pzo8_zY93H1vfF6hR7zCf068LMYJyyiSveYKA_cxB2BSNSVG6htfrAwiCq1UZACYfEQ6wr_5YcV5628ILwd2JDKyarNb8AU0_oo86i1uqQqrU0qtXynK_MpIZ1gHwhgALl873pM6uYOlDqaPKui-a0RgesLFQtMaXZ5JSj6IP2I8s-NWVJojZezDmKThrW-YJLXws4ewXrNEIeX9z6JYY9KpdbUZPSeSn91HOVYRNcePugK5bZrP2wtosizkbdMMqcpsh8QyE-EjrsHdtPu-qAAGFVjWwGEYaMS8yKCGm7dbjEJsthi5WIC-i16jbLGwup5NkSpjn2u4ZV5XSHusKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b6b29a98b.mp4?token=pzo8_zY93H1vfF6hR7zCf068LMYJyyiSveYKA_cxB2BSNSVG6htfrAwiCq1UZACYfEQ6wr_5YcV5628ILwd2JDKyarNb8AU0_oo86i1uqQqrU0qtXynK_MpIZ1gHwhgALl873pM6uYOlDqaPKui-a0RgesLFQtMaXZ5JSj6IP2I8s-NWVJojZezDmKThrW-YJLXws4ewXrNEIeX9z6JYY9KpdbUZPSeSn91HOVYRNcePugK5bZrP2wtosizkbdMMqcpsh8QyE-EjrsHdtPu-qAAGFVjWwGEYaMS8yKCGm7dbjEJsthi5WIC-i16jbLGwup5NkSpjn2u4ZV5XSHusKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاییز با بوی نو کتاب فارسی شروع می‌شه
🍁
✏️
حتی زمان ما، شروع مدرسه ها صفای دیگه ای داشت ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107049" target="_blank">📅 10:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107048">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6ef37fb80.mp4?token=gTAcPOsRnvuvX5d1ByEPo2UjkrDyyaLO4iYKdVjuv_nckHLUAKoXoEZVqwf7T7n-SN0MXqo3ySucQvz38N9gvmHyokEY-HuhNCh6iRvrqEvzCHc7924386dgFDLPwOL2RpQlHKeK9L_65xph4_PQcNM2FHctIAMz2JXyjr_OdS9gAh_z9rrgUmgOnx1brOlIGUxVh2obIAJEbb5IC8X2f1T-yHssYqYPri5f59RPNAHDmkLMTShfBEl-nvffLs7mFap3IsTAJYhC7Q4A1B12j2ZsbghLQ7neP4JYGmT0ZoGeWMc7P1FgYtcx9ULDP4gTBGEnabbh6g8P8KkeUbIEdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6ef37fb80.mp4?token=gTAcPOsRnvuvX5d1ByEPo2UjkrDyyaLO4iYKdVjuv_nckHLUAKoXoEZVqwf7T7n-SN0MXqo3ySucQvz38N9gvmHyokEY-HuhNCh6iRvrqEvzCHc7924386dgFDLPwOL2RpQlHKeK9L_65xph4_PQcNM2FHctIAMz2JXyjr_OdS9gAh_z9rrgUmgOnx1brOlIGUxVh2obIAJEbb5IC8X2f1T-yHssYqYPri5f59RPNAHDmkLMTShfBEl-nvffLs7mFap3IsTAJYhC7Q4A1B12j2ZsbghLQ7neP4JYGmT0ZoGeWMc7P1FgYtcx9ULDP4gTBGEnabbh6g8P8KkeUbIEdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای ابوالفضل جلالی فکر کرده در عصر قاجاریه داریم زندگی می‌کنیم. چطور اینقدر راحت دروغ میگن
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107048" target="_blank">📅 10:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107047">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/090ef42156.mp4?token=mAydgFE1JTizWLCkyLKxzhF8IYegg7hkUZqXh7QVraci0TtA2G9Z56IerZiq_mMPeG6LKqLAld3sZFthcCw-4WPvLhZkyWnkJ3SzoJGr-YoL1fruGuQ09D_EPM05lUJH_z-QsmWGymNEYiiiFaXWZR6gsSFLBGGVCKSpO_68VEnqhVXiSuvOp5BwSmddmUgu3gtDGSE3g1jdOkMhleR864EhbcI0XZyL2a0YsjahYCe8Y_ei3uV4UT_7vJ__YHmqq40ZPBPSmA91OoZSeCjKZIioSu3Wt1zrdOMANXM9BShO6ED_3rWMYs1xHRKwQMc5Y5GdZILc0IEhe5KyFKbb5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/090ef42156.mp4?token=mAydgFE1JTizWLCkyLKxzhF8IYegg7hkUZqXh7QVraci0TtA2G9Z56IerZiq_mMPeG6LKqLAld3sZFthcCw-4WPvLhZkyWnkJ3SzoJGr-YoL1fruGuQ09D_EPM05lUJH_z-QsmWGymNEYiiiFaXWZR6gsSFLBGGVCKSpO_68VEnqhVXiSuvOp5BwSmddmUgu3gtDGSE3g1jdOkMhleR864EhbcI0XZyL2a0YsjahYCe8Y_ei3uV4UT_7vJ__YHmqq40ZPBPSmA91OoZSeCjKZIioSu3Wt1zrdOMANXM9BShO6ED_3rWMYs1xHRKwQMc5Y5GdZILc0IEhe5KyFKbb5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
بابک مرادی: مربی داشتیم (کمک فرهاد مجیدی) که آدم بسیار فاسدی بود. همه فوتبالی‌ها میدونن فاسده اما هنوز داره مربیگری می‌کنه
+احتمالا این شخص فراز کمالوند هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107047" target="_blank">📅 09:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107046">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d781ba027e.mp4?token=R-zp3Vz_eeiZp99CCHJpI8wOiSPDe33b9ABQQEW-VOrI6lpImNKAR8b_OGt_RA1APmwE3bMWf-IHUUeq0MkclLLT0yKcs2966PJ_sDcyg-SU9QTsJOr7ZERaxKWalG7awR_RdAn7R2A0ebKVWHBQ1PpGFWcYUwXjt1EXL9u-ns1VmNABOFctJROvY4pqpeVz_ZrOxxH0upuMthy1lSoAha3i9LLbjQEN0EVuOGmJxCJkeEZbNymqDaS5jME9ywJ2t0byoPzkmAR9QCR-6rvRtJZax0S_R1hbc3SlEpEnzadDHVoCe49UuTe2V7p73tuVNaDoAqh2xSzz8XWRb4u1qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d781ba027e.mp4?token=R-zp3Vz_eeiZp99CCHJpI8wOiSPDe33b9ABQQEW-VOrI6lpImNKAR8b_OGt_RA1APmwE3bMWf-IHUUeq0MkclLLT0yKcs2966PJ_sDcyg-SU9QTsJOr7ZERaxKWalG7awR_RdAn7R2A0ebKVWHBQ1PpGFWcYUwXjt1EXL9u-ns1VmNABOFctJROvY4pqpeVz_ZrOxxH0upuMthy1lSoAha3i9LLbjQEN0EVuOGmJxCJkeEZbNymqDaS5jME9ywJ2t0byoPzkmAR9QCR-6rvRtJZax0S_R1hbc3SlEpEnzadDHVoCe49UuTe2V7p73tuVNaDoAqh2xSzz8XWRb4u1qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
🇮🇷
تعریف و تمجید حمید مطهری سرمربی فولاد خوزستان از سهراب بختیاری زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107046" target="_blank">📅 09:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107045">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed15f390e.mp4?token=TksvfNhaY6BqMBRtkEMl_0SVkOt2V_myxI9DiTNoOArQhyCPbrslsiFXHnofQFx8Qha7FBuAtnMHaH_SJa4lnnZc41BMscvVD2Y0Nv7hgy--Djy4A56dbjARUO5hPdM6W5eEXPDGl5qaKu0cnUMdKxutqNEi70dqL-nRJVgV2sJnus8FW-oXnskX3zkx0d-pmrA1-OWWATvxvDHJftOlvz0SsxjL6ZIDsiqFVtiOTCSytXu2_WU-SkJsMMRgXMMn_Z7RFnsSG6fA8jrEjH1zlEguxoh8s_Vhn5Xh2ntnIFuidOWhdYLfaECNS30ehnKGrqE-Alve5M4WxjPBdFCBnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed15f390e.mp4?token=TksvfNhaY6BqMBRtkEMl_0SVkOt2V_myxI9DiTNoOArQhyCPbrslsiFXHnofQFx8Qha7FBuAtnMHaH_SJa4lnnZc41BMscvVD2Y0Nv7hgy--Djy4A56dbjARUO5hPdM6W5eEXPDGl5qaKu0cnUMdKxutqNEi70dqL-nRJVgV2sJnus8FW-oXnskX3zkx0d-pmrA1-OWWATvxvDHJftOlvz0SsxjL6ZIDsiqFVtiOTCSytXu2_WU-SkJsMMRgXMMn_Z7RFnsSG6fA8jrEjH1zlEguxoh8s_Vhn5Xh2ntnIFuidOWhdYLfaECNS30ehnKGrqE-Alve5M4WxjPBdFCBnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
فوش ناموسی بلینگهام به مادر داور بازی با اتلتیکو که شکار رسانه‌ها شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107045" target="_blank">📅 09:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107044">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a69b72fb04.mp4?token=AqyI9jhV_bwvvhaxmlVfrIYt_SUPLgZrt_jO-EcPQ0KyslMzNoPldr0NR4dxVeTpvvLkN06WIh9IngphUnSsbXOlzGL-jYSAoczZpRrZOLeCI68RsYzovsbT5TFWiKsRmaeK0FOLTLBMoe-dM-2ehsPZrLLAHQFjhHTcGxKLFTkqP3XOdQ6eLmnC7Lw43EJpKflFUDtKejLxFprJp6P17YZ-DHx1jBLYxSUYvmVor9lq09z5JZj-tv2UiZq56lArjwZj4xA9KYzZKHLk0IRtDxNx4dzv1xJ-cGWszABCmXY6ilhdEg-tu7wtnpPtysTgPMySP1tyBx97paMQ-X1znQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a69b72fb04.mp4?token=AqyI9jhV_bwvvhaxmlVfrIYt_SUPLgZrt_jO-EcPQ0KyslMzNoPldr0NR4dxVeTpvvLkN06WIh9IngphUnSsbXOlzGL-jYSAoczZpRrZOLeCI68RsYzovsbT5TFWiKsRmaeK0FOLTLBMoe-dM-2ehsPZrLLAHQFjhHTcGxKLFTkqP3XOdQ6eLmnC7Lw43EJpKflFUDtKejLxFprJp6P17YZ-DHx1jBLYxSUYvmVor9lq09z5JZj-tv2UiZq56lArjwZj4xA9KYzZKHLk0IRtDxNx4dzv1xJ-cGWszABCmXY6ilhdEg-tu7wtnpPtysTgPMySP1tyBx97paMQ-X1znQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
شعر خوانی جالب قیاسی:
«مثل رابطه سهراب بختیاری‌زاده و صالح حردانی
مثل حال دروازه‌بان بعد از تک به تک شدن با یاسر آسانی
یا مثل حال اتوبوس تیم ملی بعد از جریان کنعانی»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107044" target="_blank">📅 08:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107043">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107043" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107043" target="_blank">📅 01:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107042">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTbcKOx7ddKx1QvSwZ650zk7oDj-spa_UjYeiPsQnKvVL9yeqrYrtJyZWdbxIE1kOfozBhQ6zXLocQpsH0-XdYJ5TTu3xTiyHDfIKSoTBigO1dOnukyEDrESSfHtN2lR3o0mJ8DQf-BUZfW1e4Bkt2pn2V9jG_b_1lP2t0O000K_Lg19UBufk3YnW1hLcZ1_rVamq--V8-RXhlznrFHpnBs3cu7aqy_AVSmSRvlZUj3b8jvohSp9ZLL31QWSKRQP1_NbkIW7-HVTRwoMR5oBch_98um1eFpc0s__8X1EJ4fFD3GTDZlgE8QqqUxk0CEygc1vo1xwfUGAWqMG5q0_cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107042" target="_blank">📅 01:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107041">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32c5c8c60.mp4?token=NSiH4bEIsHcuK98OjwmlbbgEF_WDpB1doPz3NJTQ-JhbHkqHqNd_RkmT-4bAHMZRgYxHDJWuR_zlAsdmZtG5Ek7p1h28iX5IUTzlyZ2V-KqIGH5Hl1hhBbwQ_RI2JYOQcbPODjx5fVBbM6DbA18U36Ei-bWJveTzZ9A6PccEwsaK7fONxDp9aahoTwSiuJKJ4tfvfMZZBl4GBjwXJFaybNEx84znUMX14I_IYIpjkfP5e7qK9FQVcO3s6KbrmowMlCjUNGyQ4UoCeurbzoqioPrXqsoGYnAMFdtih5n-i4R9cYD-fAX3c4uOQf_LdpjkIqc3TbtMi3fXYnJcAu0_4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32c5c8c60.mp4?token=NSiH4bEIsHcuK98OjwmlbbgEF_WDpB1doPz3NJTQ-JhbHkqHqNd_RkmT-4bAHMZRgYxHDJWuR_zlAsdmZtG5Ek7p1h28iX5IUTzlyZ2V-KqIGH5Hl1hhBbwQ_RI2JYOQcbPODjx5fVBbM6DbA18U36Ei-bWJveTzZ9A6PccEwsaK7fONxDp9aahoTwSiuJKJ4tfvfMZZBl4GBjwXJFaybNEx84znUMX14I_IYIpjkfP5e7qK9FQVcO3s6KbrmowMlCjUNGyQ4UoCeurbzoqioPrXqsoGYnAMFdtih5n-i4R9cYD-fAX3c4uOQf_LdpjkIqc3TbtMi3fXYnJcAu0_4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🐐
🇦🇷
رونمایی‌رسمی لیونل‌مسی از پیراهن ویژه خودش در آخرین بازی ملی با آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107041" target="_blank">📅 00:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107040">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b37185041.mp4?token=ZR6T5feNYyvKysqDa4XkVfKd1Z-UsX4HIbx927fKut_5UVuFDXFt8VXJ5kEZDuMSygZ42i03_8_CZjb9WOBvs2PmGecF4lkUWYSRL2PGNZYQWUnQ-i-eRCZhpacF-E4qD6Ff2fkM-KF7LUDzT2AOwYmfMLWFsTydOV8gjr5ZGcsFFEYi9wRUESc8sarDe2YksXH33O4oIZhUpf7HEQvO1WEO9V_Wo9SaD8eGwBPAEeYX_k0Nvt3l8dZnvct0dVO4lhmMgQHTJHZb_HRC9npixME4tDLZj_ta2XOvGDTt5ymKfKRxpTJBf8BT16ffIWCa7jvdGz9PARCl0F7GdyC-ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b37185041.mp4?token=ZR6T5feNYyvKysqDa4XkVfKd1Z-UsX4HIbx927fKut_5UVuFDXFt8VXJ5kEZDuMSygZ42i03_8_CZjb9WOBvs2PmGecF4lkUWYSRL2PGNZYQWUnQ-i-eRCZhpacF-E4qD6Ff2fkM-KF7LUDzT2AOwYmfMLWFsTydOV8gjr5ZGcsFFEYi9wRUESc8sarDe2YksXH33O4oIZhUpf7HEQvO1WEO9V_Wo9SaD8eGwBPAEeYX_k0Nvt3l8dZnvct0dVO4lhmMgQHTJHZb_HRC9npixME4tDLZj_ta2XOvGDTt5ymKfKRxpTJBf8BT16ffIWCa7jvdGz9PARCl0F7GdyC-ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام علیرضا بیرانوند به میثاقی روی آنتن زنده: اگر نظام وظیفه اعلام کند من چه زمانی باید به سربازی بروم به جان 2 تا بچه ام فردا می روم سربازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107040" target="_blank">📅 00:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107038">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EXWENM7ZhtgeuMXpyV0qF5xaJU8hRPZ6aonO4nxtd-dtlzMS9rAwtW-GxRyv13kaRfOuglTvtVs7-7wcWMdLNDUPN0XCY6-_VlqVPi4x5fsp5UXOg1J-N3AANlkHWEQwKKoUSW9o3HZYA8S4m_3J3L4wXpngQyIoFxNQespvJxMBxj8QlWmBMrXVCRP-EXU1hoaWDi4KT6QwnCFP-E_NxMQVKeg8RFFz0RYCLo3YQXO7i-1KEZNtM4Ab-9XyQrDV7jnF6AN6I4FgTdBv70yifOYUzn4HH0Quiw9nqkh9ZKbC6YCkao9jFMSh2NwAIfXlIv-wH9uPEXIciSeyNS9GCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mguu5bDM_Clt2qEo8wybgE5GhJ4pxyR8dOuIh75Uek5blAZdlMLhRn3WJSMpOGNX7tksS_5RV3FxmDVlSAbs4widkR_szbMD93rIo4mCveaLqMABfQD8FHEdXpAeo-t8qWa6hJac7vh_fa9QDMHvIjKsRRladBcfBAjJQNk_fT3g5IlvetnwlVKkgfxA6fjRNhm1ZmgxaXQBPqVbl6z6u9JT5LSNEaQM01xKLhdW9gCsjYpN8apHUx50Og4mGHwQSz8Fb-WcPrRHF1DYrIle-gvzeoLqS-tXys37lYNd9EUirpECqc6kN6Q_JKL315unGwduHQijkt9_j-N_W-fpDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
❌
دلیل عدم دعوت اللهیار صیادمنش انتشار این استوری در ایام اعتراضات سراسری دی‌ماه ۱۴۰۴ است که باعث شده حداقل تا چند سال قید حضور در تیم‌ملی را بزند مگر اینکه به مانند سردار آزمون دست به پاچه‌خواری بزند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107038" target="_blank">📅 00:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107037">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
⭕️
‼️
اللهیار صیادمنش: در اردوها به بازیکن احترام نمی‌گذاشتند. حرف‌هایی که جوان‌ها نمی‌توانند بزنند را می‌گویم. در این چهار سال ۱۰ بازی دوستانه روی نیمکت بودم، ۲۰ دقیقه هم بازی نکردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107037" target="_blank">📅 00:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107036">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
⭕️
🎙
اللهیار صیادمنش: تا این افراد در تیم‌ملی باشند حتی اگر بخواهند هم دیگر برایشان بازی نمی‌کنم. در اردوهایی که زیر دست این آقا(قلعه‌نویی) دعوت شدم هم چیزی به من اضافه نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107036" target="_blank">📅 00:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107035">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
⭕️
‼️
🎙
گلایه تند اللهیار صیادمنش بابت ربط‌دادن عدم دعوت به تیم ملی، به مسائل اخلاقی: می‌دانستم قلعه‌نویی هیچ اعتقادی به من ندارد چون اصلا هیچ مسابقه‌ای را از لژیونرها نمی‌بیند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107035" target="_blank">📅 00:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107034">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itflYGJs7DLoqXiWgId_bbjlKb5LKpsESj1YLIMryz5a-en8PhcIUsp86cSUNC5JOzsLVBDolasHUGiC8YEvjuPe0gs-sFO2zelH77w25cfZp785KyNyBzeRquuk7P92JHxvH3rJHIYSZYytIgdtaU14zhjX0QvuxPvruGcKTJKduc1zcbtswjudrB_bZaGn9OYk9WlxwWa-Oa8pbTHUPCnEiQh5B-x9_kvG8w_4P7hRMb0wgxL5e5_uQuYnNk05mjUvheGL2ZyOyKpC482WLzJ5VxMIftyOJl1xvvLyqMneiutlMXP1Q69Kdap_suEHsVtgOZr4G12NrZhDDKBPEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
خاویر‌تباس رئیس لالیگا:
🔹
باخت دیروز رئال مقابل اتلتیکو صرفا جنبه فنی داشت. درست است که اخراج یک بازیکن حریف نادیده گرفته شد اما اینها بهانه خوبی برای باختن نیست. امیدواریم رئال‌مادرید واقعیت تیمش را ببیند و دست از جنجال بردارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107034" target="_blank">📅 00:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107033">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8238d2e025.mp4?token=bplxFrT_8EUgT8HE8KuY0pHK9PtoAJqNDn9HBU1FH7F-AG3VmwH1HoXD4KowBpIn3dmUReaW_hAkZGgeFoVjFauqsvQiWfgDGEMwl7ZCj6xHK-qJ4DHmXFjNyF4MZ0YufOnCo2kyARjEdZ14eILFME8n8wp0oMLOYhuClqY9plga8lWJE2G4ZHldbBHBF1uAHM-QDHzbecsudsXMEGTtPbGuV7ykqcT06eyVyUd8GGRBB6PF4rk8hXPiiaMwpnHCp-tbGPu_QD3vZZdEvd07_v1A6jjZ0WbBAY6kh7DGcgm8kL4SWEBYWxeHcIe9hxdQvUexwBBCp6_7leMijP6Oqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8238d2e025.mp4?token=bplxFrT_8EUgT8HE8KuY0pHK9PtoAJqNDn9HBU1FH7F-AG3VmwH1HoXD4KowBpIn3dmUReaW_hAkZGgeFoVjFauqsvQiWfgDGEMwl7ZCj6xHK-qJ4DHmXFjNyF4MZ0YufOnCo2kyARjEdZ14eILFME8n8wp0oMLOYhuClqY9plga8lWJE2G4ZHldbBHBF1uAHM-QDHzbecsudsXMEGTtPbGuV7ykqcT06eyVyUd8GGRBB6PF4rk8hXPiiaMwpnHCp-tbGPu_QD3vZZdEvd07_v1A6jjZ0WbBAY6kh7DGcgm8kL4SWEBYWxeHcIe9hxdQvUexwBBCp6_7leMijP6Oqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
میثاقی: اردوی تیم ملی تمام شود سربازی علیرضا بیرانوند تعین تکلیف می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107033" target="_blank">📅 23:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107032">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e4355f95.mp4?token=WLzDifixhaU59MWeca6OIr1wSfC_Bd6SjRu2YdCHkbk0pF8hqiUs4jSWU4BxwjtRX88uwD_F--HNmHnVkN_ZWm7wCnw5ZCiRIDB_wTeQjGasvTt9tr3HrmFkUMlLl5qtSyNUH4EXprYUAYCJxP5RCl2wAWGRnPw9NXtMq-XO3SKTlwSkuToq_5mnLbqa3yjByj8LPURXS71K31ZHJpElXh9BSK3DisRoiSKEtDV9EFkBGG1UudURBLUurUkKxKJ25vcqmQk4An6BUSkUhJg72uJiv6kfFqajSdnZaExLG6D-YSiFN2psQhSP6ddS8Rq2xXzg7ngIsz4rgYz4U_8vWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e4355f95.mp4?token=WLzDifixhaU59MWeca6OIr1wSfC_Bd6SjRu2YdCHkbk0pF8hqiUs4jSWU4BxwjtRX88uwD_F--HNmHnVkN_ZWm7wCnw5ZCiRIDB_wTeQjGasvTt9tr3HrmFkUMlLl5qtSyNUH4EXprYUAYCJxP5RCl2wAWGRnPw9NXtMq-XO3SKTlwSkuToq_5mnLbqa3yjByj8LPURXS71K31ZHJpElXh9BSK3DisRoiSKEtDV9EFkBGG1UudURBLUurUkKxKJ25vcqmQk4An6BUSkUhJg72uJiv6kfFqajSdnZaExLG6D-YSiFN2psQhSP6ddS8Rq2xXzg7ngIsz4rgYz4U_8vWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ابوالفضل جلالی بازیکن پرسپولیس: برای هواداران استقلال احترام قائل هستم. آنها زمانی که در تیمشان بودم به من انرژی دادند. در استقلال بهترین عملکرد را داشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107032" target="_blank">📅 23:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107031">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19a96e43d.mp4?token=lnWZdK0yHZlry4aLx_w-TcCTAOawH6y_icc126Vty9q447nzN3w7_xjlFLMjG-sbeb8pMw1mkUc3HT-AdcSbwTWz9arur7ipb3hRQqkKnqzXHj23xk0IWdcZk1lS0XLUaIibgaFzvC5r9mFYGXyo9yng19UW4i3p8r0Ftfd_p3GnfnDFoCCSQrlsu25VNw_DzvqYdW3IQjiEWyNAqiHKC9j9Z9o6p5zcfJVeAnoXwZxHl1AGjLWPRhyGKNHx8U6xEXJd07JTF1Ybv8SQUpPR3FC5OqRD9UPpKCw_-1mE79sQrmOYEe2y57Gb0ZRw5EHJcUPpKfxsmPk-iDY7C5n9Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19a96e43d.mp4?token=lnWZdK0yHZlry4aLx_w-TcCTAOawH6y_icc126Vty9q447nzN3w7_xjlFLMjG-sbeb8pMw1mkUc3HT-AdcSbwTWz9arur7ipb3hRQqkKnqzXHj23xk0IWdcZk1lS0XLUaIibgaFzvC5r9mFYGXyo9yng19UW4i3p8r0Ftfd_p3GnfnDFoCCSQrlsu25VNw_DzvqYdW3IQjiEWyNAqiHKC9j9Z9o6p5zcfJVeAnoXwZxHl1AGjLWPRhyGKNHx8U6xEXJd07JTF1Ybv8SQUpPR3FC5OqRD9UPpKCw_-1mE79sQrmOYEe2y57Gb0ZRw5EHJcUPpKfxsmPk-iDY7C5n9Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
ابوالفضل جلالی مدافع پرسپولیس: الان طرفدار پرسپولیس هستم، عاشق پرسپولیس هستم و سرباز این تیم هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107031" target="_blank">📅 23:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107030">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6fa04dad9.mp4?token=FRVfxMyy9MLyM_-KkalUBsmsrvliLZrgsNw4QJ3CU9wLqtuNHki5gqLLuIZe3b6_kH_5izIbqb8H9j6oUxuClK_ybb4GosjOt5PusY3WhiNwW8ZCBk3EqmK6mb2Ptkt_A1RKnrBRAkKQT0byeG5BH8Q2uke5X-VGmJR1s4s0EE8gipKKNo-7XTpxdJxnDO0K11ZA4BS24IAwBK_AqQw9ZVVWdSjg7B19UuzpM9qtasMBt7_ZXUOZPYDHWYJ8JSAF0CeqOjY6gYvxejaPVxjJvS-OGitZ7QpFBBcaPmECUHfP_djRozfXhbRmqpdYTKMEZDPLGFmzcs3pmrTbFEtO6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6fa04dad9.mp4?token=FRVfxMyy9MLyM_-KkalUBsmsrvliLZrgsNw4QJ3CU9wLqtuNHki5gqLLuIZe3b6_kH_5izIbqb8H9j6oUxuClK_ybb4GosjOt5PusY3WhiNwW8ZCBk3EqmK6mb2Ptkt_A1RKnrBRAkKQT0byeG5BH8Q2uke5X-VGmJR1s4s0EE8gipKKNo-7XTpxdJxnDO0K11ZA4BS24IAwBK_AqQw9ZVVWdSjg7B19UuzpM9qtasMBt7_ZXUOZPYDHWYJ8JSAF0CeqOjY6gYvxejaPVxjJvS-OGitZ7QpFBBcaPmECUHfP_djRozfXhbRmqpdYTKMEZDPLGFmzcs3pmrTbFEtO6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
💙
ابوالفضل جلالی: ساپینتو شاید از قیافه من خوشش نمی آمد که به من بازی نمی داد چون از نظر فنی مورد تایید او بودم/ جالب است رامین رضاییان هم همین مشکل را با ساپینتو داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107030" target="_blank">📅 23:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107029">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11cbab4a72.mp4?token=LAxW1u6N5g4r_8vyiHCs8z6fRBCVNUqGB16omAOuC8nOfKrcZi9H-cj4L6dCJo_YEXAhkb--90yq58uWM3nNzo9S8hbIblQdCW-rMorDvD6K9Chtb-Q6LMrziihEf26jGE4s1378Xz6IlK6FPWket3zc8-IIj5g2LmmKOJkAS--9L7MiaVvU6kgQ-MCw4CQNzt5iYqySwZpW2tSW0f5zzB1n2BbE4ImYiaZAs-0FOZlWQdxwgGVtfZhd0b1TarHvwK44XYAceb4Kq75HE00aGy8S8y_o0b-ef-bd8beeh60EzHf4yR5fPnlSQQS4dvgh7Q7f8iWwr9GyiU0e7KdL-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11cbab4a72.mp4?token=LAxW1u6N5g4r_8vyiHCs8z6fRBCVNUqGB16omAOuC8nOfKrcZi9H-cj4L6dCJo_YEXAhkb--90yq58uWM3nNzo9S8hbIblQdCW-rMorDvD6K9Chtb-Q6LMrziihEf26jGE4s1378Xz6IlK6FPWket3zc8-IIj5g2LmmKOJkAS--9L7MiaVvU6kgQ-MCw4CQNzt5iYqySwZpW2tSW0f5zzB1n2BbE4ImYiaZAs-0FOZlWQdxwgGVtfZhd0b1TarHvwK44XYAceb4Kq75HE00aGy8S8y_o0b-ef-bd8beeh60EzHf4yR5fPnlSQQS4dvgh7Q7f8iWwr9GyiU0e7KdL-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید الهویی مربی تیم ملی: درخواست کرده ایم که از اول دی ماه اردوی آماده سازی تیم ملی جهت حضور در جام ملتهای آسیا را برگزار کنیم
🔴
میثاقی: با این وضعیت بعید می دانم تیم های لیگ برتری بازیکن به تیم ملی بدهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107029" target="_blank">📅 23:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107028">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12081ba765.mp4?token=lHIniZn7gClTqTECut58JBQYIdpeyzah4cHXNHTpRLkvDXtQEJohGhucXY9tYaFyK1RKXYrH9rm_9fdI-teJEXLHeF8Bd3vPUXuE5BSaNhG_M6oyYRuyJyfhpPBnWqUrJzhCZaL-FU0gh_Fb7y4NKlWD0AViEAI-FNmnAK3-Xw37nBYKFaOGVR3F_thDyqZIVMzENwrPAnKmdw5u1lGtiK9ZoIOEHNz_4z3YotchmE2NoguojfA5oeXtYk4vRfL17IGI9M8IC0IwWNIEIMtVLYq2eNLadDLOAgiGGVxeanAtedNa-_G6I2KB5UjIm6fMMnPlY7Sdrzu3kqfAW_XQaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12081ba765.mp4?token=lHIniZn7gClTqTECut58JBQYIdpeyzah4cHXNHTpRLkvDXtQEJohGhucXY9tYaFyK1RKXYrH9rm_9fdI-teJEXLHeF8Bd3vPUXuE5BSaNhG_M6oyYRuyJyfhpPBnWqUrJzhCZaL-FU0gh_Fb7y4NKlWD0AViEAI-FNmnAK3-Xw37nBYKFaOGVR3F_thDyqZIVMzENwrPAnKmdw5u1lGtiK9ZoIOEHNz_4z3YotchmE2NoguojfA5oeXtYk4vRfL17IGI9M8IC0IwWNIEIMtVLYq2eNLadDLOAgiGGVxeanAtedNa-_G6I2KB5UjIm6fMMnPlY7Sdrzu3kqfAW_XQaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
سعید الهویی: پرونده حضور احمد نوراللهی در تیم ملی کلا بسته شده است و این بازیکن خواب و خیال تیم‌ملی با حضور قلعه‌نویی را از سر خود بیرون کند
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/107028" target="_blank">📅 23:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107027">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTenoPNwhZJmJUh4kplZkZrIqXog0jhV3LqR-ZwVPVOdNrhaBRNpVSF8JQ_xZ-umNXxbzqkz3gKxoy0Maol71xQPWloM5XSD7ewEUYHgEitlxNH8J49XM-ahZGh0dMDwIeYznNEbrXFOgfAZVdd1NyubtYX2PaZ3qe_XvRGomQu23AFRmIKlgGNozYYLFulUlHvDJHAo0OOZ2hy4UHDynoswn7cFUBpekSXFio_WWaV4YH5P7z-aZwnP3BWt4htCy1t-Ug0mbdKT8MDVMMrcSjEXc3v_eU_2j-JnhNmtybmy6sUZ0mFrfH5THC6AdMM1L_avHfFgdoNr6B-4qAQIgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
سعید الهویی: الهیار صیادمنش به دلیل یک سری رفتارهایش به تیم ملی فوتبال ایران دعوت نشده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/107027" target="_blank">📅 23:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107026">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c45095faec.mp4?token=batwvvCxGMuaeMtDIUjqhAQ6pwgZnSbgGBb-P1Uh7xMPhwLHGIrAXO5AjfsD8jl8Jr9U1ICLr_WZjKn8-fQ0Koed81adfoAWh_BJA-t7V2ThKC1u5U-OlRWOtCzDR-Dqk0O4R15BW55pYnlP-Bku0xNsUiD0FHXa_ejA4WtOWxbF5jG369UKvl5OEd2Ul3j0c_Nk2iGUy9dH9iG8xv2yZHEg9dII2C5waNCwWTQKVofNROzK9oIEZhE5_XmyQXUCQhsJ-hz2A6Af5CuzZKlwPy_f7TkX3_d2zlF-l2V-_ZektVK_TnFtgGaSXlJGOdD3IE1E3tvFy1J0BN7Ultn8-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c45095faec.mp4?token=batwvvCxGMuaeMtDIUjqhAQ6pwgZnSbgGBb-P1Uh7xMPhwLHGIrAXO5AjfsD8jl8Jr9U1ICLr_WZjKn8-fQ0Koed81adfoAWh_BJA-t7V2ThKC1u5U-OlRWOtCzDR-Dqk0O4R15BW55pYnlP-Bku0xNsUiD0FHXa_ejA4WtOWxbF5jG369UKvl5OEd2Ul3j0c_Nk2iGUy9dH9iG8xv2yZHEg9dII2C5waNCwWTQKVofNROzK9oIEZhE5_XmyQXUCQhsJ-hz2A6Af5CuzZKlwPy_f7TkX3_d2zlF-l2V-_ZektVK_TnFtgGaSXlJGOdD3IE1E3tvFy1J0BN7Ultn8-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
سعید الهویی: الهیار صیادمنش به دلیل یک سری رفتارهایش به تیم ملی فوتبال ایران دعوت نشده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/107026" target="_blank">📅 22:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107025">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
🙂
🎙
به مالکوم گفتم Bro, Easy Football!
کلماتی که از درگیری شدید علیرضا علیزاده با بازیکن سابق بارسا جلوگیری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/107025" target="_blank">📅 22:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107024">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
‼️
انتقاد تند عادل فردوسی‌پور: پدرمون در اومد این‌قدر با ازبکستان بازی کردیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/107024" target="_blank">📅 22:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107023">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee3019bfd.mp4?token=ODC_cnQblIHdTOH0Qg3ACcZVDi8A9FtUuHo2FaPi349gXJf_X8HMfYoSx51txuabh6v5KHvsSzyw_oRNXsxGyUMkLhoWWfDCGkANo57e4KwLPEA8NeCD71J3M07vD7e941CqoQ0NwhU2JA2_uRonLc4Z-sB8ldtCXXIqPrQf3lJX2KIxx3Vd3oKenE5KfPdna5EFMMPRZ3QO4VRI_CxHaK8VWp4x2aHvdjDJrZH3bddHijThNMSmcucaWCQHYWB1bWjPd_nvU5bLfjDmBvj20qy0PuW0CQlRFKPiEYN11DpTlv0GY9gNzqtJKYHibrDskyLZOKUYJsovr0sR1ym8PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee3019bfd.mp4?token=ODC_cnQblIHdTOH0Qg3ACcZVDi8A9FtUuHo2FaPi349gXJf_X8HMfYoSx51txuabh6v5KHvsSzyw_oRNXsxGyUMkLhoWWfDCGkANo57e4KwLPEA8NeCD71J3M07vD7e941CqoQ0NwhU2JA2_uRonLc4Z-sB8ldtCXXIqPrQf3lJX2KIxx3Vd3oKenE5KfPdna5EFMMPRZ3QO4VRI_CxHaK8VWp4x2aHvdjDJrZH3bddHijThNMSmcucaWCQHYWB1bWjPd_nvU5bLfjDmBvj20qy0PuW0CQlRFKPiEYN11DpTlv0GY9gNzqtJKYHibrDskyLZOKUYJsovr0sR1ym8PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ادامه شاهکارهای داورای لالیگا این صحنه رو هم دیروز داور بازی دپورتیوو و بتیس کارت قرمز تشخیص نداد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/107023" target="_blank">📅 21:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107022">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه تراکتور با تهیه مستنداتی درحال رایزنی با نظام‌وظیفه برای کسری یا معافیت علیرضا بیرانوند است. تبریزی‌ها مدعی شدند که بیرانوند دچار مشکلات روانی است و به همین دلیل خالکوبی کرده و باید از ادامه خدمت معاف شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/107022" target="_blank">📅 20:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107021">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrNYs2Wb9J3S3_qkqooIFlnz64TeZ-vOoDctRHd_w7ft5pBXzEJNIL9Fq9omWbBXaqayT--kojqNfMCHm1C3rfw9zmG7xYeV7Om7USfRzgijAcls7P4iISV33Nxvtx5NQ8RpQ1uDVUxX3HnPTs-1X6nzF5EV94XuOE3--v1PRqa4PkORGtJQ5vCJ03Q5nAv3ZY0SLtp_wD5H8WepDBXbJZ6z9gghMksAkyCvM0Gi_VYDzaJQ_6h_9hwKiNlbwz6tEISObP2bNezQ11hovUbVp6VopdC59IAwg46wiz8hY6OpBZotsTp1RSuM8Y2cPEbBCVLD61_agiz_pDDKTg4N4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
مقایسه آمار نیمار و رافینیا در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/107021" target="_blank">📅 20:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107020">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/690c7befaf.mp4?token=GCUQXbKdJ4MWG3C4yPnBXLuNp8k7NJ0VxQz9nIRDUK4ciAJaTf1FThQk1Dqca-v0-nP4qyBLO48vwvn4iYh6l3iDXIQ7cl7TvGbroa-4AayDJGldQbKWUeKiI_HZXG-iJFOiiP_QwUDdErA6BJooWQHme-1FMJxrirxExzKfHrVVZyNBL2CRgugeea4vFTQN4tWcC9BojtYmDI_YeWIRARqazSQo7lbVj7GRHohiaFNEZRkStd4UgdNTLHB77Gc9YWGC5J5ynbOFrvvaJLdVq2O8w07lsev1SDfAbr5yX97bNw9nM1DiY3UGEc0h-QfjPXEzPn00VWSKBh2XYW3kyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/690c7befaf.mp4?token=GCUQXbKdJ4MWG3C4yPnBXLuNp8k7NJ0VxQz9nIRDUK4ciAJaTf1FThQk1Dqca-v0-nP4qyBLO48vwvn4iYh6l3iDXIQ7cl7TvGbroa-4AayDJGldQbKWUeKiI_HZXG-iJFOiiP_QwUDdErA6BJooWQHme-1FMJxrirxExzKfHrVVZyNBL2CRgugeea4vFTQN4tWcC9BojtYmDI_YeWIRARqazSQo7lbVj7GRHohiaFNEZRkStd4UgdNTLHB77Gc9YWGC5J5ynbOFrvvaJLdVq2O8w07lsev1SDfAbr5yX97bNw9nM1DiY3UGEc0h-QfjPXEzPn00VWSKBh2XYW3kyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
واکنش اتلتیکو مادرید به عکس‌های پرینت شده مورینیو در کنفرانس خبری
: «همین حالا به آزار و اذیت داوران پایان دهید!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/107020" target="_blank">📅 20:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107019">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0863a4f870.mp4?token=kGfrjDcXnybIXgy32_Ycs9LAH87Syj2QVJso9EOwX8EpwETW1N66NnjsU-7leS6FYhtNT3U1U6V2GHLDbowtCE_hb7HQ7X71Jxl02vEtWvhYTIzE4-K2e4O_URhwQ1wE_AAnKtamAHlvw0qss5IY3Bo5IreJnATRb5Abw0k7krhiHR4afHXIJJdGjLlXsCOZcBxOf1lOr-hW5vqAgc2EO3p65gFzUSKOd9DiUbh6mYdjpTjZdMQmIf8bsmIE0oo9937uSx46i-RRPbkIW8deJ2n38Zxl_huasswkosxzDR6HGfOw4YU5hV6fvaxq5ftc_14kSP94vEOJIweV1Sz0Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0863a4f870.mp4?token=kGfrjDcXnybIXgy32_Ycs9LAH87Syj2QVJso9EOwX8EpwETW1N66NnjsU-7leS6FYhtNT3U1U6V2GHLDbowtCE_hb7HQ7X71Jxl02vEtWvhYTIzE4-K2e4O_URhwQ1wE_AAnKtamAHlvw0qss5IY3Bo5IreJnATRb5Abw0k7krhiHR4afHXIJJdGjLlXsCOZcBxOf1lOr-hW5vqAgc2EO3p65gFzUSKOd9DiUbh6mYdjpTjZdMQmIf8bsmIE0oo9937uSx46i-RRPbkIW8deJ2n38Zxl_huasswkosxzDR6HGfOw4YU5hV6fvaxq5ftc_14kSP94vEOJIweV1Sz0Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
وضعیت رختکن تیم‌فوتبال رئال‌مادرید بعد از شکست دیشب جلو اتلتیکو!
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/107019" target="_blank">📅 19:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107018">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beecf6e577.mp4?token=dnxKft5ApqBuqHglWhlL_9ujdb3n3f-OHxdMz1yix6ZRk6CjhKjZ29aZ40ExBbBbPT6QvmsfxLBRZn5x7YDMfAW4PyrUbt0wzMiSJiU9xNApj_g2xQWV4yLPto4mb0IbQ005oKOM5m4YNfNpOrUyFlXiUF9qb6b6nVQahoYe9dSiUG5iTw7scc5n9bLEvmT_OpbnfrdQEFdw5D-6eDEGVZP4RYWwrSkGQhoNAfkJ-8GrwyzgXdTfAfqEyjgz59UksQaurkGSpq-0VUDvXGJWcNLjOidgbW3G1BPavjHBvTTOTXJjNCnGoTIYYb_sqkF7DyZp3TKvYSw4gDENj4nf9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beecf6e577.mp4?token=dnxKft5ApqBuqHglWhlL_9ujdb3n3f-OHxdMz1yix6ZRk6CjhKjZ29aZ40ExBbBbPT6QvmsfxLBRZn5x7YDMfAW4PyrUbt0wzMiSJiU9xNApj_g2xQWV4yLPto4mb0IbQ005oKOM5m4YNfNpOrUyFlXiUF9qb6b6nVQahoYe9dSiUG5iTw7scc5n9bLEvmT_OpbnfrdQEFdw5D-6eDEGVZP4RYWwrSkGQhoNAfkJ-8GrwyzgXdTfAfqEyjgz59UksQaurkGSpq-0VUDvXGJWcNLjOidgbW3G1BPavjHBvTTOTXJjNCnGoTIYYb_sqkF7DyZp3TKvYSw4gDENj4nf9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
دیشب «محسن نامجو» که به تازگی برگشته ایران، شروع کرد وسط خیابون با صدای بلند آواز خوندن که یه هموطن با دو کلمه «ک…، خفه‌شو» دهنشو بست و این شاهکار رو خلق کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/107018" target="_blank">📅 19:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107017">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34f1b0314.mp4?token=V3-HWrX4nyFMirbXbPP4-bC5qsCyMq1YDjjqq8j3VEM7IjjWclCy8HGkYLNFvHdvSAhqYTIQPu2cDXJ3s97hGhjhJ3L3VGjZ2MnKTye0noNNFLaOat4R35hJMg5finfy9Nw4Mo9L9y2vsWRje6E8hDgAsal5w0QiN4-x5-xu3E-foUZyMDnZwyX0OE7ristMK9dSb4_KgbuZyQx41lBj9hfDUfhWCfaLRboVNfBSJcV5fbbqOqgjovb1hNtp_dn4ARlaC3Yf_iEhUR3goD1LyHZoamXwCQMoKhkPQFHRhmfN1ZNUSK2EsPv9apw247zwjVdKq3el-ygrjqCIRZ-Aeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34f1b0314.mp4?token=V3-HWrX4nyFMirbXbPP4-bC5qsCyMq1YDjjqq8j3VEM7IjjWclCy8HGkYLNFvHdvSAhqYTIQPu2cDXJ3s97hGhjhJ3L3VGjZ2MnKTye0noNNFLaOat4R35hJMg5finfy9Nw4Mo9L9y2vsWRje6E8hDgAsal5w0QiN4-x5-xu3E-foUZyMDnZwyX0OE7ristMK9dSb4_KgbuZyQx41lBj9hfDUfhWCfaLRboVNfBSJcV5fbbqOqgjovb1hNtp_dn4ARlaC3Yf_iEhUR3goD1LyHZoamXwCQMoKhkPQFHRhmfN1ZNUSK2EsPv9apw247zwjVdKq3el-ygrjqCIRZ-Aeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت هاشم‌بیک‌زاده از استخدام مربی خصوصی رونالدو برای رساندن مدافع تیم‌ملی به جام‌جهانی ۲۰۱۴ برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107017" target="_blank">📅 18:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107016">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beeb6137f6.mp4?token=LniWlpoy_oCMIs1_EVMGjAFr1puN3XWevqBMXqCJAZvN0IAcJMwlh6764OYHCnjA0ebJk7lMK59VAHx6yKkmRuEKQNF9rcPGQVG4TFu9GlfEZQ5izmcCcQDs98rAcM-AW8VcyH2xHYXTx9a2W_CFPVBVP4_wKHOUEsdJfWw_uqaSKeJ3s4ARG8utURyJMhp2LgDndS6QkZZ2XnTpcVubQgk7sziZGbmJJUf3rSi8x9jiHZza4jWS-EhC3HNbtOjpOO6rDGOEx58DguQHjOi6R5oDDBLXRvgecLeEZ__Hc5q-XWu4O6l7UAI2xK32yGyGW57nXAVG_Sq9VpOxqUX5MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beeb6137f6.mp4?token=LniWlpoy_oCMIs1_EVMGjAFr1puN3XWevqBMXqCJAZvN0IAcJMwlh6764OYHCnjA0ebJk7lMK59VAHx6yKkmRuEKQNF9rcPGQVG4TFu9GlfEZQ5izmcCcQDs98rAcM-AW8VcyH2xHYXTx9a2W_CFPVBVP4_wKHOUEsdJfWw_uqaSKeJ3s4ARG8utURyJMhp2LgDndS6QkZZ2XnTpcVubQgk7sziZGbmJJUf3rSi8x9jiHZza4jWS-EhC3HNbtOjpOO6rDGOEx58DguQHjOi6R5oDDBLXRvgecLeEZ__Hc5q-XWu4O6l7UAI2xK32yGyGW57nXAVG_Sq9VpOxqUX5MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرحسین قیاسی: مهران مدیری برای حضور در برنامه من اصلا هیچ پول نگرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107016" target="_blank">📅 18:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107015">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107015" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107015" target="_blank">📅 18:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107014">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELfc-gjaffT_TZVjryUk2vFRgFiG5c_9YlkSOPxvBqadbz0n5mmpWjkhlkijlfs5aqcrnCh6rytN9mhFHqq2uXNOAOVCFETIXpHFBv6tuXeOY27G1fOAypyMCwsSaPAC3qDOF0X-31gIySY0UkiEYzmvDkqqoZTLnxZgO-wZ3AeQ2X3IDCxKsSRUeqRlxslUasqtm_xvxLnGyimL296ZXbkvIThh1qKVZoqqiUX0BXoQ3HwLgbiD0r1WvfUPuPG3agjOUAyGSrcIEtc-lCtTG4zRnKbnp8LQrJ5jA2ZaYVAJ0APwXd9yAV0d34Sm008lZdXygwQFcDQWWxVnhnUB6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107014" target="_blank">📅 18:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107013">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/037abe05f9.mp4?token=shKgKgzvHiani0PkSBUMtpFbdALE_ICO2jltAhn5tpT7rLiH6T5vbY8Chp3tRO--Z8xhB6o40TO29cIeDTnWZiW-dJgUfcn65l1ZnBds0oxdAITx9ULK2YcSFxlNQnNT1xKg2CuJ4fdl9si1psVYxD7QKIuiXABsq2p70U4hO2nzSQCtQVbmDD_DR9wLtLYxQJrmFKDK_HiPtRvva3HU6F834oFfZosgFGtVqpK61iXSQ0FuAzHbhUzUfjO7s3x02VRTZLtb0TBrjWioPPH9A2j50HHBp0Cuga4aAZ2VfZQjtLBUVhvZJy-uw6DarFlNTxSeEOa4foNxTMMxOQB68w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/037abe05f9.mp4?token=shKgKgzvHiani0PkSBUMtpFbdALE_ICO2jltAhn5tpT7rLiH6T5vbY8Chp3tRO--Z8xhB6o40TO29cIeDTnWZiW-dJgUfcn65l1ZnBds0oxdAITx9ULK2YcSFxlNQnNT1xKg2CuJ4fdl9si1psVYxD7QKIuiXABsq2p70U4hO2nzSQCtQVbmDD_DR9wLtLYxQJrmFKDK_HiPtRvva3HU6F834oFfZosgFGtVqpK61iXSQ0FuAzHbhUzUfjO7s3x02VRTZLtb0TBrjWioPPH9A2j50HHBp0Cuga4aAZ2VfZQjtLBUVhvZJy-uw6DarFlNTxSeEOa4foNxTMMxOQB68w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🎙
بهترین گل‌ دوران فرشید اسماعیلی کدام است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107013" target="_blank">📅 17:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107012">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BM_yFaKtlCPzcnfzNrwSPWsKNl2aRg78j1J7jmLQVHBc6pbrKPIt5wcoqdQP5Q2V58ckNstHEWgw3P1OHSkakvi_zEpLlhYaZRiY3xXeS_vOCEQmVLWfr-ICEhhqCph5hMViMBe6ub53rKie6DtddpH2oDkBtI19qE4pDaRTOTjDGWoEU01DqR5BXFgE9CzMCjyO7qSbhCzre-hWKmOWHlXcI3KddYPi1Ua9E-I2tFFdvDpozti3zwDpXu7DtN7_uZcv9c3MHJMJVM6W_Ki7GergeTn7BkwBflEllYyyzQDvqCvWQFrZdqWkiBYGXv0W67XcQwkTG_gmQUle9ZVf4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سه سرمربی آخر منچسترسیتی همشون پنج بازی اولشون تو PL رو بردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107012" target="_blank">📅 17:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107011">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226cc241a7.mp4?token=R1Fww4LtZsDP0qJPj5235294WdLwjMF-1MVnpxv5q6PK097vdDP5D93DHF3Th5Q87EKzQj7YgUbyMC2FEvU7Nv1vClwId34uYfCVXeDGiKF7yPIEQp56HFKgVICVaYZLt-fZ7QQ-ucwTUkvyAJf8giQGXbTnnnBTQhcyyF3UqHFsiuAuMfExGq0xhG4UttCy1Y44gYIZGlv9npS-0CSY-ph_ER0Yb04Mdqgm3bzCugdooAKXxbtDUhpXaGEAoEXj_F36sAflbMqsDR92ADrDmIeasRh0I-ETz6B1u5Zh5g2cLzilmcSvQrt_xHSF0G5BxpWMm_0_xZM41URTWprPsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226cc241a7.mp4?token=R1Fww4LtZsDP0qJPj5235294WdLwjMF-1MVnpxv5q6PK097vdDP5D93DHF3Th5Q87EKzQj7YgUbyMC2FEvU7Nv1vClwId34uYfCVXeDGiKF7yPIEQp56HFKgVICVaYZLt-fZ7QQ-ucwTUkvyAJf8giQGXbTnnnBTQhcyyF3UqHFsiuAuMfExGq0xhG4UttCy1Y44gYIZGlv9npS-0CSY-ph_ER0Yb04Mdqgm3bzCugdooAKXxbtDUhpXaGEAoEXj_F36sAflbMqsDR92ADrDmIeasRh0I-ETz6B1u5Zh5g2cLzilmcSvQrt_xHSF0G5BxpWMm_0_xZM41URTWprPsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
چند شروع جذاب و یک خداحافظی تلخ. این فیفا دی رو از دست ندین.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107011" target="_blank">📅 16:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107010">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
⭕️
⭕️
⭕️
🇺🇸
وزیر خزانه‌داری آمریکا: تمام شرکت‌های هواپیمایی ایرانی از ۲۳ سپتامبر فعالیت خود را در سراسر جهان متوقف خواهند کرد و از پرواز به تمامی مقاصد بین‌المللی منع خواهند شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107010" target="_blank">📅 16:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107009">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfIv4bnIIkff6EKKHwUSHF2GzFq-WgfIAHD2-p1S8SzVAbAIRbj0r0tMhg1vgkRsQtfqhR4bJ6NFAD1DpCLe3v5Qv-hFIgurKVgkTp5E4Jgrm2mSWcbdgvGAdk_kVUjcNwrZGnNAfmPD-81IMdEz3T7jeynn9ggFE96hoFbblv-Ie5OPJRQz-MMMvZuiW79IvOO5k7m_cWnemi-5AtsyDAbjEdJF0oCz4VjVPpXcx_o03fZP8_E1eVT6kgEdff6QvlW7zvFc2F9P4lqAyxS30t9X-YnBPYXb_RqKJoEoFF49JnrunkZwJeD-4rR_MGAnONV_q1t1S8iFp7mRpIWwAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
آمار درخشان اللهیار صیادمنش در لخ‌پوزنان لهستان که نتیجه آن عدم دعوت به تیم‌ملی بود:
🔴
۱۵ بازی؛ ۷ گل؛ ۲ پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107009" target="_blank">📅 16:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107008">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d7084572.mp4?token=vI3djHIFXIh2TMMA3QCTme-BQDfQ0RQbuc__xr-z5HeuhwSsj82EIwelcYJOvIWdV9QvalXBR2HDv59lLESJtkOJHWKQvJFBDHicgfh5sd0NrHenTy_38HB9ex1yvh6f24_npnelQmUHf3SS9OaPspUdEoAcoiXWW7V2DPVN1Yz2Bztu8sCM2JoC-uuZs_Us6T5iVeZI-H4liTATDbe6PkNjfVEancO6EmXrOIIJFYuIfK7TbjEFiF5ohtQjQOb0sL-nJXdHSFIZxfFwAZZHsCkVJsHeY9Ll2ayNVW595PYHRPhohEzte1cvIJzrRGoImC92LS07JXzz1H2eExRX2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d7084572.mp4?token=vI3djHIFXIh2TMMA3QCTme-BQDfQ0RQbuc__xr-z5HeuhwSsj82EIwelcYJOvIWdV9QvalXBR2HDv59lLESJtkOJHWKQvJFBDHicgfh5sd0NrHenTy_38HB9ex1yvh6f24_npnelQmUHf3SS9OaPspUdEoAcoiXWW7V2DPVN1Yz2Bztu8sCM2JoC-uuZs_Us6T5iVeZI-H4liTATDbe6PkNjfVEancO6EmXrOIIJFYuIfK7TbjEFiF5ohtQjQOb0sL-nJXdHSFIZxfFwAZZHsCkVJsHeY9Ll2ayNVW595PYHRPhohEzte1cvIJzrRGoImC92LS07JXzz1H2eExRX2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
افشاگری یاشار سلطانی خبرنگار: روح‌الله رضوی کشمیری، مجری جنجالی شبکه خبر ۱۷ میلیارد نفت از ایران فروخته!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107008" target="_blank">📅 16:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107007">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISWnoGUjeTdgvJu2OVETNm3e4Xa6_rFz-S_Fz8EbDNjoAs41Dj_kS8oRfQSFUQphXUI8zzV3bxQp_h1tXEaD6dlKftq7Ii_GAa0IfCq4S_fL_TVxKWYrvlIWtL_HOIat9YyhmZQDinZ9zSofhtI5tzqTUcMLKk9_em8HZqBtmAiVm9ImIzgUPt1ZF5eowRh1vrQ4fHulLpBsp0QX5kFHB_hHu-hLJIk5ydPqXewwWUwJPQrdk22VVLsu8Fc5Owiq_FRlme7j3zYjOSTzvvnA8xseUVI-aiJLnyvna5RshGKQi7lCUJENVF9ot6VX3urDO6qzWFfwR7zoWqWwJ_GYVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🙂
دیدار دو اسطوره محبوب و مردمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107007" target="_blank">📅 16:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107006">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e35b261cd.mp4?token=FaG4F6_3M2t_xXb47CNY8JdfeAK2U7bsC-pyLAHrURt_WPus8yZmyQ38hbq948_iSIbQvOJ0t3HsKBh6bqVdT2t7ffq79CCSYxCWGnj1HLNEU2r4QeiP7SDh9yp8X0Rt3E0xddxgoc9FNyQXXerI9seTUXI-sBndiwVskaTiojPWACz3fUb2D1qtcZ9Jo6fXxd_Lj0cP6Nu9EknHjTInbDv8gbJhgaF5Akuvg610r8Mc6T30wl1qS6Aua9xQzzI_Bsnh-_lm2zSTZhGe6d_zk7zXBP9tg-ghB3QncrLX1tH3voNIMevGXP_gK5-MD-SflRI26-5tReqwQUOaJws_xzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e35b261cd.mp4?token=FaG4F6_3M2t_xXb47CNY8JdfeAK2U7bsC-pyLAHrURt_WPus8yZmyQ38hbq948_iSIbQvOJ0t3HsKBh6bqVdT2t7ffq79CCSYxCWGnj1HLNEU2r4QeiP7SDh9yp8X0Rt3E0xddxgoc9FNyQXXerI9seTUXI-sBndiwVskaTiojPWACz3fUb2D1qtcZ9Jo6fXxd_Lj0cP6Nu9EknHjTInbDv8gbJhgaF5Akuvg610r8Mc6T30wl1qS6Aua9xQzzI_Bsnh-_lm2zSTZhGe6d_zk7zXBP9tg-ghB3QncrLX1tH3voNIMevGXP_gK5-MD-SflRI26-5tReqwQUOaJws_xzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مانوئل نویر در بازی بایرن جلو یونیون که انگار خودش رو دروازه‌بان نمیدونه
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107006" target="_blank">📅 15:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107005">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4379faf506.mp4?token=to4miK3hUntXckMKZXF5lVTh5rz77oB3mmn3_RIEpT2IHbGBRnKgNZ9WMUFceVMYisGEH6mBSEhjAFzpC6we5bK38IVM8Nclaoc5iuPnGR8ng5_JrrdPGodPk-EkUFnFtM5Z5jqci3NMkNELnxaVhuL-St7A-fKjz-qGGUFHAqTmLaY1aJjgL6ubsIFBL3Gn_xT8N3saeDWEEjC5r6sPCiEmJIAwwO2-SIfR95iI8FqE2CWvrzwouXNOcBQ3iavgRH-2AShc4EzRSC0i_2Pw3oXHVgQ-QYkRY6Y3zPEFYjFOwDLJY7mkwiaSiyDCD_VjmN9McT54BVjJUxuh34FExw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4379faf506.mp4?token=to4miK3hUntXckMKZXF5lVTh5rz77oB3mmn3_RIEpT2IHbGBRnKgNZ9WMUFceVMYisGEH6mBSEhjAFzpC6we5bK38IVM8Nclaoc5iuPnGR8ng5_JrrdPGodPk-EkUFnFtM5Z5jqci3NMkNELnxaVhuL-St7A-fKjz-qGGUFHAqTmLaY1aJjgL6ubsIFBL3Gn_xT8N3saeDWEEjC5r6sPCiEmJIAwwO2-SIfR95iI8FqE2CWvrzwouXNOcBQ3iavgRH-2AShc4EzRSC0i_2Pw3oXHVgQ-QYkRY6Y3zPEFYjFOwDLJY7mkwiaSiyDCD_VjmN9McT54BVjJUxuh34FExw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تمسخر امید عالیشاه توسط مجری صداوسیما پس از فحاشی زشت خداداد عزیزی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107005" target="_blank">📅 15:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107004">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKqiptpJUzbmd98titHrbFvSt9eSAFnTR95baCfP6HzaLgN344-kbQLe8jgRhlfiVonI99ReyhEHmbTxX5VuF9FhTvL-764YQhFvHyfRYd-ZsGQAtumFF1X9RupumABnt9b62VebHXpnERPGFv6Lv5TWjEHdpnLl8-KDv-1CeM09FSrKQg_pA17ARkelKWDyt2rBplkt8gQiWXL5Z7O1YGFS_zDgQhUBQmMGl6OPIqwGDMW0KXujq4lu1sCQXQweJHQ2rxEB5rfJDTJWXNYNbXCbq6qpKk1PKnGkMzhdZOzG4NS2cw0nrvZwUh1zPmLI0JM_WVv2QRCw4yyNLyboFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
پست جدید سردار آزمون بعد از دعوت مجدد به تیم‌ملی: دلم برای شنیدن دوباره سرود کشورم و پوشیدن پیراهن تیم‌ملی تنگ شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/107004" target="_blank">📅 14:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107003">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpOWs953a_DP7hn8S_IgSH095uIy5r7t9GIZhU0Wn9AEdc5RiOjMAQ8TMFV_ojaPONU6Pj4s_Xg9eV9lfbCevFDQSo5lafyGIbG0lh0a_D5doJ-oBk-kbYDrje4TqVAXsGjP8xHcE34TsJ_hwSzg2WW9JHbf_d__7w-R7gSA8oLnlOKcV1407u18aXESGeyStbnlNphrYNS_e25-oaXkwLhgoTwuqiZRRj9CGm_1iwz2RdeZKWuv6QD92bG7xz7JnwqlDfN3s_-tXPAyumGulJ0Tz0f9eymapLpS8sP1QRn2KnhuG8citT1NPxxta3YbwXUf1J4rcx8F33fAR-kERA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد تیم‌ملی اسپانیا با دلافوئنته تا سال ۲۰۳۲ میلادی تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107003" target="_blank">📅 14:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107002">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0213635d.mp4?token=NpJQoaGr7zsjr4pvukMlAZGLg0OqzGaFGVjM_DeKwY6xvpeidY8ctu4q4JhihvTt4hBruB5FzJ81JT4VL74AjfaSPuKFiXhIq9cIOHIHReB8KLABTpQVB0th0EDq8xh4UXh8VM8y47izWQz2NVMpWkPZUZV0_UaE9WsCo24KXMunKLGPeNVV0fkr0aKC3Ttj6qGQuKx3xTi_XsS4fyZL4aTvJDl3U5mIPeGiyCFYy_n6dQ5rtYZq61IpMhCrgAbvfvIR9tk0HMnjuC2JClO1zyBcC2-YleoBOtfNirw2pXhik4rtg-5KLMu76hs4RPuHqovI-9f3T-Z5YrmmL59k2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0213635d.mp4?token=NpJQoaGr7zsjr4pvukMlAZGLg0OqzGaFGVjM_DeKwY6xvpeidY8ctu4q4JhihvTt4hBruB5FzJ81JT4VL74AjfaSPuKFiXhIq9cIOHIHReB8KLABTpQVB0th0EDq8xh4UXh8VM8y47izWQz2NVMpWkPZUZV0_UaE9WsCo24KXMunKLGPeNVV0fkr0aKC3Ttj6qGQuKx3xTi_XsS4fyZL4aTvJDl3U5mIPeGiyCFYy_n6dQ5rtYZq61IpMhCrgAbvfvIR9tk0HMnjuC2JClO1zyBcC2-YleoBOtfNirw2pXhik4rtg-5KLMu76hs4RPuHqovI-9f3T-Z5YrmmL59k2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
🇪🇸
بازیکنان رئال‌مادرید و زیدی‌هاشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107002" target="_blank">📅 14:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107001">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nG4r8o6u6kOGsGczt2ucklbqDfP6k8ha6QyEPuPPNRKIjqy_6t6s2k0BpF3Z81gIKuEke80dqdQm7_uufBUd90TULO8gtEj740DFeoz3kjf3ddJFXKAoQl6C7bSirwIx5SvwfbsLH7KXFnx_2abfp5ikey3561mVK0JW90Z0zYzLHJUhJsUrMhOIFROKTe9wsSD8E4csoYixKG5dX8DMRyjc52rHypBTuES4Z48jeBuURGja1EizWVwDWVQRd5M_TUl-hO7fuW2aJZWHiZqU-AJwG_h434GbR5gMBy1TXw9zWCbezIS-ziDSdAFBdfrMEkkMLr49f8UgJh_YK9P1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین تعداد گل رافینیا، مسی و کریستیانو پس از گذشت ۷ هفته نخست لیگ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107001" target="_blank">📅 14:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107000">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6_iS0Q298zSQPolB9Dh2dQiRGpqh5o8h27qgWH2PupQVxraE90FvbPXddbf0-gmdzlarvdbSBKU436X1RhF5Y2deNeJBTAcFlOqze_HKGW3Be1X5fhffZoU_lT2OEYoF7ZQGhUPedaZuswo7VIi5-3yPRRiqcTaejwvK11bhtbVYef2Ya54ilXQeJ20sj6Oqf1no4Mx8zMoEgF91iWoOHwgwFB1uW2_uD90bdjnVvemfFdpQqpXeDgiApKvkSVStHeVbZlRr8LN2ToT8_FH6bd7drGRt6mssVrHg2wYndNxqJg7Wud-XJWZIUR6-MW8nsVp-hEBf23ZiLyNRHoIFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
پست جدید سردار آزمون بعد از دعوت مجدد به تیم‌ملی: دلم برای شنیدن دوباره سرود کشورم و پوشیدن پیراهن تیم‌ملی تنگ شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107000" target="_blank">📅 13:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106999">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf7b6d21da.mp4?token=AyredPZsALvav7XrVRIzyP2OY5vumPup0-CSfC1qtngMAOVAKfQD8TgGACjEnytuiPE6w3iK7BozL2S7XLcQBFX2hGnIpq2VIURA0Q2lo5U0MGonq5PBvv6nqIo7WUR_pX4Roc0yGS0wpEihdDBGPAbkCYrI6dB4FH9MYBWrPDqURQxJPrlW9nW-55_Nr5LjUz_mpnUGgUDpN5Yzn_hm0Y82XwBOmaP8C0FBovTjLPwtw21oPBk-oJLtMK42_IxsNuEu5YfdBBuTVDXbQgIwv2j-MD4IlrR2JoY5TaVUl5OK9UPkjXaC9a5iLrdqCOvtid-xwPPg3Phan-76K9xobIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf7b6d21da.mp4?token=AyredPZsALvav7XrVRIzyP2OY5vumPup0-CSfC1qtngMAOVAKfQD8TgGACjEnytuiPE6w3iK7BozL2S7XLcQBFX2hGnIpq2VIURA0Q2lo5U0MGonq5PBvv6nqIo7WUR_pX4Roc0yGS0wpEihdDBGPAbkCYrI6dB4FH9MYBWrPDqURQxJPrlW9nW-55_Nr5LjUz_mpnUGgUDpN5Yzn_hm0Y82XwBOmaP8C0FBovTjLPwtw21oPBk-oJLtMK42_IxsNuEu5YfdBBuTVDXbQgIwv2j-MD4IlrR2JoY5TaVUl5OK9UPkjXaC9a5iLrdqCOvtid-xwPPg3Phan-76K9xobIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
اولین گزارش سعید زلفی در پلتفرم اینترنتی پس از جدایی از صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106999" target="_blank">📅 13:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106998">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oqstx8qxBCRl3CeMYrvua7jHx8I7jy74xqr4WKjLMliaPZzexfFT3Pmg-xYx27F-DmsD1xXdYRl-tfbSVhUliXl5XVT5j5M9FOKcU0Rk_a7frqt1p4yqx47Wz3V8U_FtOnoZOCwETqJ1Snl_sdPlElLI95d-3a0O-vMTao7s5_bkA89SIk1Hlp-EblDTFllifizoO4bbsNvcmDQ0kYsPpKmG8vZnitbAL5gMSZa7yDzw-RetnMyValH3tBE7ZhppXzebYWbLKjOVrlbXV3MzKcDST-99CS4_jzuXQB4Mvt5dzli1WIw3dmSx1nbBepr8B2fPgW0ihQ0UBAqmX2nBNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🔴
اینو حتماً تو اینستاگرامتون فعال کنید!
برید:
Settings → Data usage and media quality → Data Saver
با فعال کردنش، اینستاگرام مصرف اینترنت کمتری برای لود عکس و ویدیو داره یه تنظیم کوچیکه، ولی اگه زیاد اینستا می‌رید، تو مصرف حجمتون حسابی اثر می‌ذاره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106998" target="_blank">📅 13:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106997">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Usdmww6NAhTYDe7LmZBYEjPTuwdRyMP2BeBrOjVQghlyyECFEa2FIaR1sxx1sywVGrTk8lxsDcbgAfEi2oRw26GaTu2wnpGMwT8XRYR-0DpVOk36RwRJaesrqxDUyvbZMsTm6b3_B2zDKUL_9cFlKVDPMXzcSpHa7NfgvHjJ5NSYuCT9f_XOYtkb5d2BTzyLHC0qXL2LGukIQMeTksK-__VuFBxXA_ug1hkf37zVil0BvwNCza3AKWSHVMD3jJSC-iT44alYBKEkdI3MS-RGntzWlzkouGOYeTSpdZ1YsbksBgIb7oj5RBJTwgxSyeV2OKZQW8jMI1nMGSvjwFuv3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🙂
استاد گودرزی
: متاسفانه پارسال نزاشتن پیاده تا آرامگاه کوروش بزرگ برم؛ اما امسال دیگه میرم
هموطن راه در جهان یکیست و آن راه راستیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106997" target="_blank">📅 13:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106996">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35dfd98213.mp4?token=X3zDfCcmxH6ZOnNNU9sx65116wjyPA7_zy5hl6ThGDWXVDqf_g57p_R5uAQ686ZVMDpzTmFfPMiY14EzC0L_DGKjQs-Vrc7mlxJz-idXfNrne99RTOfUFzdDb85YvPvW9lEhWLTT9HZyyKQjGehoU95vOWyh-zaxdJKll6aMVZ-awt60WtQe5XwrtOecZTwZZWvOD35fmojyLWyEMxhW6YT5tbX6aDtqylX3FOcbfoeKAY_722PXg-YquYFIERlVxx2Z-CfwKedZ6wt0sbsc1FQL8r60p9ebIH1Xv9h1jn5XkKnAmdUCuvGw9XradTolMok_aa4DhnirAHPyY5GmCYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35dfd98213.mp4?token=X3zDfCcmxH6ZOnNNU9sx65116wjyPA7_zy5hl6ThGDWXVDqf_g57p_R5uAQ686ZVMDpzTmFfPMiY14EzC0L_DGKjQs-Vrc7mlxJz-idXfNrne99RTOfUFzdDb85YvPvW9lEhWLTT9HZyyKQjGehoU95vOWyh-zaxdJKll6aMVZ-awt60WtQe5XwrtOecZTwZZWvOD35fmojyLWyEMxhW6YT5tbX6aDtqylX3FOcbfoeKAY_722PXg-YquYFIERlVxx2Z-CfwKedZ6wt0sbsc1FQL8r60p9ebIH1Xv9h1jn5XkKnAmdUCuvGw9XradTolMok_aa4DhnirAHPyY5GmCYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
لامین‌یامال از مدعیان اصلی توپ‌طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106996" target="_blank">📅 12:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106995">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNo-0jDY0dn0vTIvdaZQnVxzoPZ85CYzBcsc7NMcxY0Qw0oDsRP2QhGQHSVTCeQXgVMf4rmyAgU5w-9xzqMBSYLRPfe7YWC4yZQTRQ5fjZLZYUTCItN68RNUHvDBxlcyvt_4Va9lA_zDh0ZUksGyB1XPh7huKr27JMmW8lD4I8TSR1YPJ1nrdcYG1Yc5_gCBMx_IK540BBqwRkORkaHQ0rvEe0PvB4ZhmN2H4dGKiRn_d7Fyvic38ZgKGmyBKebv8TFIbzGcTc5J3_WjgLaHSlPI5DS8MLLUdIs_ONQeL6_Enohe7WolVaul42N-NaIIfH5Y_iwxrXodaHPrBm4ylg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه تراکتور با تهیه مستنداتی درحال رایزنی با نظام‌وظیفه برای کسری یا معافیت علیرضا بیرانوند است. تبریزی‌ها مدعی شدند که بیرانوند دچار مشکلات روانی است و به همین دلیل خالکوبی کرده و باید از ادامه خدمت معاف شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106995" target="_blank">📅 12:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106994">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8lioxkwM01QXWJRDoC8PShdwwGm7I-c5fp1uukygsOfWRw2MAx0EEzdMeXn4y0AKadd6TvI2hqg10IuOmc9dzcbwx7_aLgcTDMN3Jzy1gNfzrfHTT7my7DI79n8LcOmVoWeYFng_SDiRv3-e-Hjt5Z4gw1FiTGdN4p30RV93CKZKu0M1ALuLCVdos-zd7IFDCQzFbqpi_Uv4LD1b1excy6jvOsKaUDbaIv9GhV2F-dxlfDz43bBYHYKYl0e5lSflzDQNqxGfKX2GhjhoHDtqLAKKNqLiOQf1DFat3tZou38Gga4xpkBXSPuAEtEkdmmEFY1R2MYKyVAReLycRCxIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🫡
🔥
بهترین بازیکن فعلی فوتبال اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106994" target="_blank">📅 12:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106993">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1dd2f2cd.mp4?token=J2_OG40ctWTYlX56XQwInKOczLzf5shV56QEd6Yw4KBkdS_1y-tD6HuU4SDKrEAx6Dlt0ckIkz8PdHXsk03XzunMj1LhNl3nALyGuO4oI38jIodrFDJeOdITx_ourt_2poraV47vkk4rm3JPl9f9LFu8O0-nIoOO7eA59cS8p5XtYG0-KB1US_TUvozyV1QfIfKlJK462Ty-1g8-4OgqMWGb8grb4PPv0izSMyTo9b95LoXsqQvg2L7X2uMiysXZqA0Tl65ENZkToDQR_mEtJFLC-yiC1vT2jrhpesp81jeymaYBW-4mZdKIsKiuya_5Z_SfhToWg-ToTOJktqQzBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1dd2f2cd.mp4?token=J2_OG40ctWTYlX56XQwInKOczLzf5shV56QEd6Yw4KBkdS_1y-tD6HuU4SDKrEAx6Dlt0ckIkz8PdHXsk03XzunMj1LhNl3nALyGuO4oI38jIodrFDJeOdITx_ourt_2poraV47vkk4rm3JPl9f9LFu8O0-nIoOO7eA59cS8p5XtYG0-KB1US_TUvozyV1QfIfKlJK462Ty-1g8-4OgqMWGb8grb4PPv0izSMyTo9b95LoXsqQvg2L7X2uMiysXZqA0Tl65ENZkToDQR_mEtJFLC-yiC1vT2jrhpesp81jeymaYBW-4mZdKIsKiuya_5Z_SfhToWg-ToTOJktqQzBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هالند ویدیو معروفش که با هوش مصنوعی درست شده بود را بازسازی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106993" target="_blank">📅 11:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106992">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omhjXNqAsStsbQd0j3z8YCmVrK1oPwRZXuUjmp2y9E9EA56eaKaJtlwNFM2o7BEs1dKZKN4oLMYQiM5uEVxVLAldFohKhtaKUHY_Y1PlNaI_sBauL7TrsrlWO93vDi1aouyJkmIUfoQhkIJlCmTjPFXO43MExse-bU66BMZQ40GesHE6e5wxtu8U-AYYlYVNAphdlLBlqM49YETuXe326sC9NGFiMwfV1vpSTHN15jrvRMf8zjisuRpj3PGuae4vsjfzOTe4Affupf0tQJUlj-_lzL9ifqsxz9xdzUrd7FnmFDNRZL3_fE5vJSf4jNKRurU_yCnQFQYcc5UuqybebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
‼️
اعلام رأی کمیته استیناف:‌ اعتراض تراکتور رد و محرومیت 4 ماهه خداداد عزیزی تأیید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106992" target="_blank">📅 11:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106991">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0476c7864.mp4?token=prM0x9YyfvoteAO4fKpRcnhFYeQvSQltYgwFh741eehkXhN5xBHQf-eaD2zPCcIHPU_bzkc7iHRSVe5eEPUBJ1ZWEnOl789pjXq92aqnQyRuhzpkBd_xJjUVInVLG_aySy4pXY54wHkl8Zdjw3CMFPwATFhFAO9U7vfzyq4WajE-slcynidMYI9gm_Q7WoM67uwR0iE3juGRFoq5z3RF8KEz-vrYguYO7hN3SG-fi28XBDnXE4iZNl7LOd0iZnWfMTVuTP5XSapRzxOZXMuzhnhVSqSjHfMh23H3Ki4qAlmH4iHElsYvJly-LDzrtPDEZKfam9WOsDV7XMaBTGZfQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0476c7864.mp4?token=prM0x9YyfvoteAO4fKpRcnhFYeQvSQltYgwFh741eehkXhN5xBHQf-eaD2zPCcIHPU_bzkc7iHRSVe5eEPUBJ1ZWEnOl789pjXq92aqnQyRuhzpkBd_xJjUVInVLG_aySy4pXY54wHkl8Zdjw3CMFPwATFhFAO9U7vfzyq4WajE-slcynidMYI9gm_Q7WoM67uwR0iE3juGRFoq5z3RF8KEz-vrYguYO7hN3SG-fi28XBDnXE4iZNl7LOd0iZnWfMTVuTP5XSapRzxOZXMuzhnhVSqSjHfMh23H3Ki4qAlmH4iHElsYvJly-LDzrtPDEZKfam9WOsDV7XMaBTGZfQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
‼️
🇪🇸
ویدیو سال ۲۰۲۳ بارسلونا وقتی که یامال ۱۵ سالش بود و شماره ۱۰ بارسلونا به آنسو فاتی رسید و براش جشن گرفتن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106991" target="_blank">📅 11:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106990">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106990" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106990" target="_blank">📅 11:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106989">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgVqmZ4XJoTUcL1FyFz-KKveUNGJXGHh3T9qdJEEaovUG-ANO_Nb3TwmW3yPwkWZQpBu4YdQXeMHeXfYxM9ndMy8LMk--nCzAsOTWoUpWfLI7T6Ny5PTBhciU7OaR_1bFfdc_Omq5mJoAYHcFq_Dw92jvBPiNCtChfNuAE5HG2_Avui2Avu9NZakNM2UV1N7rtFTrF-6HIjuFP-FqytDgFL1mEAeNlIw0Dk8ZOe9zcU5ZJBO5gWxKb1VmPYSDypd2SR_9zIYV8Bu1RtjnOar7oz6AnEI-h29G5lzWRq1LBaodcMkHLuhu8CsCjKB-uL5_Ca_vzqn4MZkvWv-cNukgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106989" target="_blank">📅 11:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106988">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60ee4811fc.mp4?token=cap0_qq-FO-ihe__UALeYWiRLyl4zom4bxrodmsBU-T5S1f214ytOqd1IsWv6hOnzBU_V6IwGMRbZ9SjXthQmXlI1VqvvrOjIlIaRPg5LI11TVo-qGH3Kvr57_kpTZCVprWGfrePm264hssyG7B25o23Njtdi9DHrljSHvMrA6-434Jv9ccgwhqia_xFVcFoMuONR3ebwvO_QkVbpzPrHDI6JjAKDkSiO3EZeKuSZ8fmDRSbVU89ATwD7Yg2kscj1iVkeYBD-SkZp3xOsKl7R95tqThG_RGiil97wDMmsYOV1qDcv1-UZ1xfxuTUiFgFEcZWHFsKeLREZccJt0zZzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60ee4811fc.mp4?token=cap0_qq-FO-ihe__UALeYWiRLyl4zom4bxrodmsBU-T5S1f214ytOqd1IsWv6hOnzBU_V6IwGMRbZ9SjXthQmXlI1VqvvrOjIlIaRPg5LI11TVo-qGH3Kvr57_kpTZCVprWGfrePm264hssyG7B25o23Njtdi9DHrljSHvMrA6-434Jv9ccgwhqia_xFVcFoMuONR3ebwvO_QkVbpzPrHDI6JjAKDkSiO3EZeKuSZ8fmDRSbVU89ATwD7Yg2kscj1iVkeYBD-SkZp3xOsKl7R95tqThG_RGiil97wDMmsYOV1qDcv1-UZ1xfxuTUiFgFEcZWHFsKeLREZccJt0zZzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با صدای کم‌گوش بدید
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106988" target="_blank">📅 11:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106987">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9186ccb478.mp4?token=ETMWnPeVlJffWicwBkoLIDARx1A4lgsR_BZ17jrZhcvytaXFx5uS6qaolSpkApv3lv2PM1TIM3gPRXhTFeKCNEM8bA9RGCXRsBs9ltedFApeB0VL03ixg3G-bnL5evtdSOvOz-890rOBEUrotp639RBpwu_-P5BRE173glwk9BcdHrzIIz5sePWnZypSAT_g34I3Z4R05z3V9FzwOUh8ck9xGKYaizylJUsUl56COuun_VDdwgrc8Hc-M6ci3LmxirJZWkL7lhkzjjX0x8D7P0mLOxLgTrXlTyN6tuEu4BVwG6ZsEvu-Bw1_zfbm3SAQO3I_rEKfTIWdbHpwiUBYAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9186ccb478.mp4?token=ETMWnPeVlJffWicwBkoLIDARx1A4lgsR_BZ17jrZhcvytaXFx5uS6qaolSpkApv3lv2PM1TIM3gPRXhTFeKCNEM8bA9RGCXRsBs9ltedFApeB0VL03ixg3G-bnL5evtdSOvOz-890rOBEUrotp639RBpwu_-P5BRE173glwk9BcdHrzIIz5sePWnZypSAT_g34I3Z4R05z3V9FzwOUh8ck9xGKYaizylJUsUl56COuun_VDdwgrc8Hc-M6ci3LmxirJZWkL7lhkzjjX0x8D7P0mLOxLgTrXlTyN6tuEu4BVwG6ZsEvu-Bw1_zfbm3SAQO3I_rEKfTIWdbHpwiUBYAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
تعداد‌گل‌های این فصل رافینیا در مقایسه با چند تیم مطرح اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106987" target="_blank">📅 10:40 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
