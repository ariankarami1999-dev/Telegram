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
<img src="https://cdn5.telesco.pe/file/m51dmwXhcIGukHD-4zyFjn-wfXOEgzVfysImEuOILdut0QuXa4tM5z1LfdT1v4XlNcOIATxOGAucvYdSEVqF5OHxhmQVX0NHF0rh05D0ifeACeNS2qjr7ECe33wRTwW7HiA8TXgKLSeTwWPRJThLbyCD_AppRQXdnEFU_8RUyCuNv0yzBTftOX4nf4VHVCvC0YPK-YCNiv1rB639nXlMse9hV2bhdNp42ZbazJUWzOPdNxq4LetAP7NdAvBR5eNi3OWMZQ5M79GqWPWbeN4Pq3Im5qXhmyDKqQhUSxnjIUT2xsEbgjoXBvImPmO_2_hL3mPfCkmZovyDx28uVuEfFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 400K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 16:46:03</div>
<hr>

<div class="tg-post" id="msg-107307">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275c393efd.mp4?token=o6F9DlsBSN1KPSFO1gH3T4d71ChCEE9QyNCxOrADRW-LNCN3uXNg8dKk1f0YPLO9gvFzpqw_dc462ECyZf5xwpoHp8tCQJaKFzYssp0BIfs9Gur1IpBSGaQy2fH2_Yn3DcTRkzZJExi34AIlOlMLz_aDFtD2H4zbQm7VIGTK3bwfQfH4fE7dxNkYfgvGzyMVxGXDor0O-cF9-TLNZm95fAmfg6r3k3q2buDroBZ1z0zJYRh-RWtbrueE8Ph6I712GokErj-Bkivze_w-q0a1gONn9kCUfsrgsACb5prC5Bj_kf-mvAb_LAr5vpkJmR_wijDS2-2hh42P6TeUaz4rkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275c393efd.mp4?token=o6F9DlsBSN1KPSFO1gH3T4d71ChCEE9QyNCxOrADRW-LNCN3uXNg8dKk1f0YPLO9gvFzpqw_dc462ECyZf5xwpoHp8tCQJaKFzYssp0BIfs9Gur1IpBSGaQy2fH2_Yn3DcTRkzZJExi34AIlOlMLz_aDFtD2H4zbQm7VIGTK3bwfQfH4fE7dxNkYfgvGzyMVxGXDor0O-cF9-TLNZm95fAmfg6r3k3q2buDroBZ1z0zJYRh-RWtbrueE8Ph6I712GokErj-Bkivze_w-q0a1gONn9kCUfsrgsACb5prC5Bj_kf-mvAb_LAr5vpkJmR_wijDS2-2hh42P6TeUaz4rkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❌
آنجلوتی بازهم به رافینیا استراحت نداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/Futball180TV/107307" target="_blank">📅 16:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107306">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eR60vB_q1Oi8GWRdBeFdA1yvU8raLOKjrUx_Cc-HRmAAcoXdZ96K_g_Rf8UkfU6PL2UuME2PLBN0npCcc9LW1iFmcwjZY9kXVWiIPtenIPC9B5aDKqbqvz9pwz_GiiGQtFGADI6EkK87WZOksYUnmUnSfpoLacmPJHW7ovlYkp3BWYgx7YR1I1-kpmEczDZycCjSmXkVW9GkQCGLoIkeUI1_CvrlC5zvZcov4Hr450AjqSpI9vwAITavTX_0NUeg2jXzHASC0fov5FOdw-4fxqCDBQnMiWWpbNkX7S9c8ttt45X1auiyVJ1k_LhJnZAboh-Ggt1JuFLXJJUmjVPAuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
🇮🇪
چند بازیکن تیم‌ملی ایرلند از بازی مقابل اسرائیل انصراف دادن و گفتن که مقابل این کشور بازی نمیکنن. در صورتی که این اعتصاب گسترده‌تر بشه و ایرلند وارد زمین نشه، اسرائیل برنده بازی معرفی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/Futball180TV/107306" target="_blank">📅 16:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107305">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=nVYjrJwh-JVke7eeBSDGpQen_AVaiVFvOkcgkTptgBsMQdvt_UPw8uv5IeSn-otxSnu9Yk4xIQpgRGt8L9MEeEcHGX7DKnj3SdbuFCuab4ZLbQmUPC4rH2CNMndlI1vJZGFcR6AVtCAOqpbyVcJOjCwFOz_ZJ4osdFNY51OpB_ZerI30kWOzz74VBQ6sKuP-cMX6x8QvIGDy4YA2lgkva4qW8zJNTNrEcnuaf8glghMnjlKnFlqgk6UmMXKwcVRe8soyokcjPVw8mgd5FoJvjtcJuKpDIaN3etgWxLCVCoguC2a0r6KXohW_BKXm0aIaJBDEkW1fOgR9FTsAOuXiJGCYQZ-jE1TeOkq4K-bKS8RV-i2qSaRff3TQuXZ6FE0lI14MO9SB5M7okTXqsLjmfOVUd3uso7Qaf5uow7wsjytMNZyEdi8xg2AlHIruisfSHkuX-NumImuGr2AUh8s-nmBuuAGKDMrKyBLcxvcOiKYzvI6Fqx1FmPcRFl8--RiEeY0RtcsyC-a12ogvVVubIj8KHggiO8lr7QtX3az4QAmvT4-4V2vVOKsbG0AlH-XbamJuWoqJXaotkt9ekz1ojpXNUk9pJqU4ZxZjVuyusyMNi6JTxFFblQL8nWSiSaCocvzHqfoEj0miDi6dLPzU_39A7NNK1cB6SFMD3MBM8pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=nVYjrJwh-JVke7eeBSDGpQen_AVaiVFvOkcgkTptgBsMQdvt_UPw8uv5IeSn-otxSnu9Yk4xIQpgRGt8L9MEeEcHGX7DKnj3SdbuFCuab4ZLbQmUPC4rH2CNMndlI1vJZGFcR6AVtCAOqpbyVcJOjCwFOz_ZJ4osdFNY51OpB_ZerI30kWOzz74VBQ6sKuP-cMX6x8QvIGDy4YA2lgkva4qW8zJNTNrEcnuaf8glghMnjlKnFlqgk6UmMXKwcVRe8soyokcjPVw8mgd5FoJvjtcJuKpDIaN3etgWxLCVCoguC2a0r6KXohW_BKXm0aIaJBDEkW1fOgR9FTsAOuXiJGCYQZ-jE1TeOkq4K-bKS8RV-i2qSaRff3TQuXZ6FE0lI14MO9SB5M7okTXqsLjmfOVUd3uso7Qaf5uow7wsjytMNZyEdi8xg2AlHIruisfSHkuX-NumImuGr2AUh8s-nmBuuAGKDMrKyBLcxvcOiKYzvI6Fqx1FmPcRFl8--RiEeY0RtcsyC-a12ogvVVubIj8KHggiO8lr7QtX3az4QAmvT4-4V2vVOKsbG0AlH-XbamJuWoqJXaotkt9ekz1ojpXNUk9pJqU4ZxZjVuyusyMNi6JTxFFblQL8nWSiSaCocvzHqfoEj0miDi6dLPzU_39A7NNK1cB6SFMD3MBM8pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
ادعای جنجالی کریمی: خودسرانه برای بیرانوند دفترچه پست کردند؛ در تلاش‌ برای معافیت پزشکی او هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/Futball180TV/107305" target="_blank">📅 15:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107304">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc52d28f2d.mp4?token=gskElv-1WtQzq7itsurCtEGDvTjh9WUoojMqxyCEPDgwJaH1Z2PgBOXwDmIz66sCTiQQ-hlF4zMyWRD1kYBL49ET_IIj_c21XXEH_imiaUmdztIB_F1GTu9rfrzkHE2ntKHRKvazPHQPmq_sJrwAKH9y2LiG5I_I-CKcl3pJQBRwZ12xYoCrUiWqZvdYzHRb6Fzp5YyTSmTonO3aKoRungS-4AH5lhs9tkd3ps65Ma7kMSoA5UPzc9R2UF_RnzfapH1BQpTGjK481DAByIX-iDnRkRE9FZht6aTsdwaI2vVO0pVhNrSuStXifGJQSU1-D2wDTGqruzc0uAsQB1Nz-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc52d28f2d.mp4?token=gskElv-1WtQzq7itsurCtEGDvTjh9WUoojMqxyCEPDgwJaH1Z2PgBOXwDmIz66sCTiQQ-hlF4zMyWRD1kYBL49ET_IIj_c21XXEH_imiaUmdztIB_F1GTu9rfrzkHE2ntKHRKvazPHQPmq_sJrwAKH9y2LiG5I_I-CKcl3pJQBRwZ12xYoCrUiWqZvdYzHRb6Fzp5YyTSmTonO3aKoRungS-4AH5lhs9tkd3ps65Ma7kMSoA5UPzc9R2UF_RnzfapH1BQpTGjK481DAByIX-iDnRkRE9FZht6aTsdwaI2vVO0pVhNrSuStXifGJQSU1-D2wDTGqruzc0uAsQB1Nz-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
حسن پاجانی، قهرمان مسابقات ورزش‌های الکترونیک (بازی efootball) بازی‌های آسیایی ۲۰۲۶ ناگویا: دلیل قهرمان شدنم اینه که یه سال و نیمه ایران نیستم و اینترنت بهتری دارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/Futball180TV/107304" target="_blank">📅 15:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107303">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2e1cd171.mp4?token=Pmra6-CfstpqxvG1DQFkFEoZyIv8tKeKDUzoV_F34PSr4FXw5DZY2uYsddXeh7QnaLaikfIYstB8ucwVbGRpzWY4vBxhyS1UkXyVJI0CHLkOwqlaWu1colsW6LaEIRB_z99nLalL_KpWE6PsXevyOSJcgcTDmMLkxkGz5_CNXeWCVBwr1j-pao2b4fipw6PmrF4MngfjDwgRyW1b8EvA30qW5lrRnbSHhYDJuGQB92BFYdG0ILTTG-vvZW98hB75xWQbMRtwPsYdGLFifMr4yok3LIIvSgAPkBZX2kYSX79UPQH0z1XPbkEkpxW3JNSRRYMg6Zwp6Kk28tIUZFRglA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2e1cd171.mp4?token=Pmra6-CfstpqxvG1DQFkFEoZyIv8tKeKDUzoV_F34PSr4FXw5DZY2uYsddXeh7QnaLaikfIYstB8ucwVbGRpzWY4vBxhyS1UkXyVJI0CHLkOwqlaWu1colsW6LaEIRB_z99nLalL_KpWE6PsXevyOSJcgcTDmMLkxkGz5_CNXeWCVBwr1j-pao2b4fipw6PmrF4MngfjDwgRyW1b8EvA30qW5lrRnbSHhYDJuGQB92BFYdG0ILTTG-vvZW98hB75xWQbMRtwPsYdGLFifMr4yok3LIIvSgAPkBZX2kYSX79UPQH0z1XPbkEkpxW3JNSRRYMg6Zwp6Kk28tIUZFRglA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
هانی رامبد: امسال سال‌بسیار سختی بود اما برای آینده تمام تلاشم را برای گرفتن ویزا ورزشکاران ایرانی برای حضور در مسترالمپیا انجام می‌دهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/Futball180TV/107303" target="_blank">📅 14:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107302">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90efab6fe.mp4?token=WHjT_NmbVz-fCKo6YWdd4Pym5lQD7wOTXYLI8vTvhmyB1DpYr4ihK9A5UJredYkgpT9fzyoranv3batGIEwiLbfKtaHjH2XPk7iVun6Oxlfdi-6UpzBEf1nNRvpMe69cnoFh4zAXJvDZIMOf8EosZREYJ5--KCrHKSgEv3d3mfZfXdvHcmsPnuv0t86dyKgud7f0bHFtBEqyksZDXCJ51fmDr6U9eXQFaNk8v16Mj77EWkUzYxd_VL05wRomCZF0cU1ky3b66dki_mWvjslDqHCS1qId9BfAMAgu5_kaausZiq7aLaIT2lZS_w5Z0hTfg-s4aGdsJv8uI0PqjsGTWDF70e0dLr6pccw7Otq3fA5haopuUWlh65vPhbLNaqwvj9geJ-pZcCgA_ncMrgT4mlwo3dOE7bnRoaMZHzFOfjMFl7klwLIGRWyj47CABaPazL7roe7Rys2wUOjVEVeDS0h3LlRgcSN50FbSZWrPFJ08flNPDetXk-d8mkD-yNe3CIbOfW1wtVc-T7WM16zlklxMhdEOmwUsrwnCAAQSdFJROs_rZGVMla3YcBqilpy7u4dzoCM6ri8YYotu7Q1Vm9jq91OlkrZ1c4HoWmOc07UCm1ggGOwwRPfAVJNq34vzaItpfVErBT7QIhXnFeMYp_O9iH3PFqZyOAAxP7YoAAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90efab6fe.mp4?token=WHjT_NmbVz-fCKo6YWdd4Pym5lQD7wOTXYLI8vTvhmyB1DpYr4ihK9A5UJredYkgpT9fzyoranv3batGIEwiLbfKtaHjH2XPk7iVun6Oxlfdi-6UpzBEf1nNRvpMe69cnoFh4zAXJvDZIMOf8EosZREYJ5--KCrHKSgEv3d3mfZfXdvHcmsPnuv0t86dyKgud7f0bHFtBEqyksZDXCJ51fmDr6U9eXQFaNk8v16Mj77EWkUzYxd_VL05wRomCZF0cU1ky3b66dki_mWvjslDqHCS1qId9BfAMAgu5_kaausZiq7aLaIT2lZS_w5Z0hTfg-s4aGdsJv8uI0PqjsGTWDF70e0dLr6pccw7Otq3fA5haopuUWlh65vPhbLNaqwvj9geJ-pZcCgA_ncMrgT4mlwo3dOE7bnRoaMZHzFOfjMFl7klwLIGRWyj47CABaPazL7roe7Rys2wUOjVEVeDS0h3LlRgcSN50FbSZWrPFJ08flNPDetXk-d8mkD-yNe3CIbOfW1wtVc-T7WM16zlklxMhdEOmwUsrwnCAAQSdFJROs_rZGVMla3YcBqilpy7u4dzoCM6ri8YYotu7Q1Vm9jq91OlkrZ1c4HoWmOc07UCm1ggGOwwRPfAVJNq34vzaItpfVErBT7QIhXnFeMYp_O9iH3PFqZyOAAxP7YoAAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
هری کین یا لامین یامال؟ تفاوت فوتبال انگلیس و اسپانیا؟ وضعیت جود بلینگام؟ مقایسه توخل و فلیک؟⁣
✔️
جواب همه سوالات با آنتونی گوردون در مصاحبه پیش از بازی انگلیس و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/Futball180TV/107302" target="_blank">📅 14:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107301">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e44add616.mp4?token=gibOLSKfBglfRBPcPs4QqLNfgxY9iMPgg6oDUGq1hhNJgPc_yavv5371NAQwyY2cZu06rQFlUAJaE46341BdyR96yOXNLWkPQIFI2_MNHigoba_dkaF0cLf2SJBaSS0t1QeuBkI_RDTSksudxmTLV1w7UNt955T1009sXLxR4aZiYiPS5cPYxuH4ytMp1VG8vifgyJSh2bJHdbs897ywfgIN1AlXc6WW7Qedw2zm_Ibomo5qh4w9Smyl-deQcrsvwPTCqItbX3rz9Ltm6MdQhWpiHPpsAEGpeizg3smp9-gyPcOepnGOed0ZBjar7yZ3DeWePxQUh5KDwBn-0T31JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e44add616.mp4?token=gibOLSKfBglfRBPcPs4QqLNfgxY9iMPgg6oDUGq1hhNJgPc_yavv5371NAQwyY2cZu06rQFlUAJaE46341BdyR96yOXNLWkPQIFI2_MNHigoba_dkaF0cLf2SJBaSS0t1QeuBkI_RDTSksudxmTLV1w7UNt955T1009sXLxR4aZiYiPS5cPYxuH4ytMp1VG8vifgyJSh2bJHdbs897ywfgIN1AlXc6WW7Qedw2zm_Ibomo5qh4w9Smyl-deQcrsvwPTCqItbX3rz9Ltm6MdQhWpiHPpsAEGpeizg3smp9-gyPcOepnGOed0ZBjar7yZ3DeWePxQUh5KDwBn-0T31JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بیرانوند سر صحنه پنالتی بازی با ازبکستان به چه چیزی داشت فکر میکرد؟
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/107301" target="_blank">📅 14:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107300">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d96c298a1.mp4?token=kcPeswaOXgp6xUh9foAt9I7JOEt9Vmp8IotahWcQSrPt5pFAtk7W8gxldon2Ig2ni7aXaaqgDLAWcC1zijmbLQK-j8YsbOqIGYx_0amCAjkoVZrsGEalfUbTTOM4HimfVOVLz29oEQ1rltq_d1-ioZ8YJlocFIrUo1F6YG6CbmWphQ3mVzpvetzD3hdLoJewFAkflCPGP-ALL6CcNjfcYSeVqQl3MRWN_vf938E_GQ24tjJVcBS0D_Z0iCQHe5xHKVsA-nbMUcefR75sNr3wEae6QjjoAuWhogkUHXgvBbSiit1ghWY1NU5kF2OY-rdUnUnXX0Hswaiywma1BTJujA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d96c298a1.mp4?token=kcPeswaOXgp6xUh9foAt9I7JOEt9Vmp8IotahWcQSrPt5pFAtk7W8gxldon2Ig2ni7aXaaqgDLAWcC1zijmbLQK-j8YsbOqIGYx_0amCAjkoVZrsGEalfUbTTOM4HimfVOVLz29oEQ1rltq_d1-ioZ8YJlocFIrUo1F6YG6CbmWphQ3mVzpvetzD3hdLoJewFAkflCPGP-ALL6CcNjfcYSeVqQl3MRWN_vf938E_GQ24tjJVcBS0D_Z0iCQHe5xHKVsA-nbMUcefR75sNr3wEae6QjjoAuWhogkUHXgvBbSiit1ghWY1NU5kF2OY-rdUnUnXX0Hswaiywma1BTJujA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کری خوانی های عجیب هندی‌ها برای ایران؛ لحظات پایانی فینال کبدی مسابقات ناگویا و قهرمانی هند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/107300" target="_blank">📅 13:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107299">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0woe22zJH8J78Fh-mt01wktPL9201vXDU_69hHXHMEP_JYuesMEszkWnb2qfCtuEaTNkdW7IlMsqXATeaMZZxUpyo7pVXrC5at0l9wkNyffJfJNZtQKQeGhwLNqmvVR_3EE7jxRTCeZaIdXOCilwsl-6y830eIpANGtjYqPTiIdAm26VGEHw2A92a0Ahy9-IM84y7JQO1BZi3EDCs6-w5ciMbjKvEtQk6uiDpcNfMGyBu4wiyi7gjiciVM4Zp0IEQxIQ3iI04NDDOZM4-B-k0TV8r8f8Y-oMQGYTQY8JWv872NZnUcOmRvaDV9bpy-ne3Xvl90WcpC5HEnIwYQDPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😳
تو حرم مشهد این آقا صد میلیون چک نذر کرد و انداخته تو ضریح واسه شفای زنش؛ حالا بعد یه مدت اومده رفته بالای ضریح میگه زنم مرده تا پولم رو پس ندید پایین نمیام.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107299" target="_blank">📅 13:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107298">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4221e00ddf.mp4?token=UuhBzoqR_B9BNqGav-cv42VStsbNmPcyD-Ih4PAPqShIsGVWYsW5dnb044cVJ1moyGIGO0x-4pevW3o9DEepFU80v2yxb47b3dHR4rVExAe97-hQb8M19JZA7creVwUZ91LaNNhfLyFH5AUpi8F4TYVaOcwLr6vAcROkcohNc8wpRHwqAdskN1VybjQfgoRB6CfwbT8nfsitCVvl3VYn-y8fO0Sie_qyNLL3pT0WNB5EX-SmSyrLCcV23oINRcc05DA42dxdVBVS00-H0dSki4y-cJszkMyZe_c9sedtbUr0l_l3XNBtBwNXRyYR3NHft6ZiRJRy3vEDEpT9UmtxNxYmBkHhtCAEa3Wit0LPbZ4_uUme80xahiMUyiYs7ww5R7QxyggIXMXDdEWWXRLWU57_r3V7afqDia6KhKM72SpoyMq3XaZNU-GqIY6ZnhrvKS_TV801Q7vPsKLefZRJokl4wOUB8xKaXJzyarMKiP3ay8F-SqAZzeRbp1yuF5HvHWjN2rvWk66m4N4YM5V0oGCgUen6D_t0eDI26ADpjdud2LGzqCk6XX0w7bTugsIFoej7oQlPcLHvxzgQgNeWFn7LL5riyjdOnoq6AcIid0ZzEwpzwmX66G9EIC1namPvSDPC3M-zsrlS05gF5GIoAtJ5p-xRIQMK6Ed3PWhMBF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4221e00ddf.mp4?token=UuhBzoqR_B9BNqGav-cv42VStsbNmPcyD-Ih4PAPqShIsGVWYsW5dnb044cVJ1moyGIGO0x-4pevW3o9DEepFU80v2yxb47b3dHR4rVExAe97-hQb8M19JZA7creVwUZ91LaNNhfLyFH5AUpi8F4TYVaOcwLr6vAcROkcohNc8wpRHwqAdskN1VybjQfgoRB6CfwbT8nfsitCVvl3VYn-y8fO0Sie_qyNLL3pT0WNB5EX-SmSyrLCcV23oINRcc05DA42dxdVBVS00-H0dSki4y-cJszkMyZe_c9sedtbUr0l_l3XNBtBwNXRyYR3NHft6ZiRJRy3vEDEpT9UmtxNxYmBkHhtCAEa3Wit0LPbZ4_uUme80xahiMUyiYs7ww5R7QxyggIXMXDdEWWXRLWU57_r3V7afqDia6KhKM72SpoyMq3XaZNU-GqIY6ZnhrvKS_TV801Q7vPsKLefZRJokl4wOUB8xKaXJzyarMKiP3ay8F-SqAZzeRbp1yuF5HvHWjN2rvWk66m4N4YM5V0oGCgUen6D_t0eDI26ADpjdud2LGzqCk6XX0w7bTugsIFoej7oQlPcLHvxzgQgNeWFn7LL5riyjdOnoq6AcIid0ZzEwpzwmX66G9EIC1namPvSDPC3M-zsrlS05gF5GIoAtJ5p-xRIQMK6Ed3PWhMBF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آنالیز دربی مادرید: چرا رئال به گل نرسید؟
🧐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/107298" target="_blank">📅 13:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107297">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d0bcba0b.mp4?token=A3l5yp16JnCU6TDGOKBs0R4nd_hI-iaFSDXs6mm2jGcEA_QsjHTOnYV7Df-Drf_xyvceOSWy9y4pBkS1iqNOucX5ZNBPrjxpeUiDeIfqW3MB0LgvjIDv8ZAsEg7DwoMMcnXFcS0-_71KlKO_ZGexngtiNSGw-1AyaoZcOyaFz0JOUXR8VIGbY-Zd4GPWFQpfQ5dtAzThai7LhMLIohvonp_Rpg-ft2Zyy70jvjZy13cehiMXHstF_cdnWlzEwykQOpLR3LjD6zcxszP86k7SFoGmtj_yT8sttA9NDWXzATUnAj1f9T1k7oCcDOA6QI3mIbTxeUBXuL76UdW2oPMKOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d0bcba0b.mp4?token=A3l5yp16JnCU6TDGOKBs0R4nd_hI-iaFSDXs6mm2jGcEA_QsjHTOnYV7Df-Drf_xyvceOSWy9y4pBkS1iqNOucX5ZNBPrjxpeUiDeIfqW3MB0LgvjIDv8ZAsEg7DwoMMcnXFcS0-_71KlKO_ZGexngtiNSGw-1AyaoZcOyaFz0JOUXR8VIGbY-Zd4GPWFQpfQ5dtAzThai7LhMLIohvonp_Rpg-ft2Zyy70jvjZy13cehiMXHstF_cdnWlzEwykQOpLR3LjD6zcxszP86k7SFoGmtj_yT8sttA9NDWXzATUnAj1f9T1k7oCcDOA6QI3mIbTxeUBXuL76UdW2oPMKOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
دبیر: تراکتور برای من هیچ فرقی با استقلال و پرسپولیس ندارد
مراسم امضای تفاهم‌نامه همکاری باشگاه تراکتور و فدراسیون کشتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/107297" target="_blank">📅 13:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107296">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nd-x0bsZXLZ70sZtjn8wAPZLNNCiZRgiaCorme2LfM0AqTTDuvaCkXlvHSvLIyDQkKDv-C6c_WHbxYJuDNkN04F4YqvkAlHLP8vh8S5BgeuL_DiLUeC1z9u72iIGQKlcLgYUYhFFzFstXHygwXPb2r5GYCvYjkhQCSM55AUsg2LyKvkiswvnHKsqZ_vr1p0sTTsrImvNRRC31MlqqxttoUttXcPQZiQ99dBpZjmuQswcAlgGFKdHDQDb4aqxe29Btzi-IW5RR_fPLMzbW27kFeiJCP7oFduzGGX8IXhoUkzbcjV0Vx2pApRqoVpUidbUCc4HdpTEXXZbmO6lNMBlQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
👀
همسر سابق سپهر حیدری درباره رامین رضاییان: ایشون بااختلاف چه از نظر فنی چه ازنظر اخلاقی‌بهترین‌بازیکن حال حاضر فوتبال ایرانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/107296" target="_blank">📅 13:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107295">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJBUz01LVO8Q9kuFB7U74LKgO21HhQC5oynMOUgojdUnypOy8cK8EiDj1aJfUuxWs9FFPujRZOrnvOe0YTwt_vt6cU1B-t8oyuTgm2oSj4anSE3gMIRP91kktSImKb8BtVQELesLpNE1yxFKAzJl3j_Gj1QlhpK3B0qdHgC9R5xpEA-w50kboEqbqMD9CcbqUgO6L3isvd-fPcAHWYfEE3OQjXz-x0KFjneUxQfA_daINn8g3pUVIUITBuzjA13fo6FUAFTJ6_EdB_UTXvuU_Nb2JMIO8rD-mSBxcJU7ICTn38w_Ai2KdMDx3uudjdtMU474ERVB9CnQjqL_2svXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگر قهرمانی‌های‌سیتی گرفته بشه نتیجش میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/107295" target="_blank">📅 13:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107294">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107294" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/107294" target="_blank">📅 13:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107293">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLZo_hgBxoD2_quLX9o2zRGMHRLOFUertLAxyHeIVpomnqcxNulgse4HgbavfzzcoDplCsbKnQn1-mIAKsEznRvmZvVw4obzHPM0vjuA3QBdeoA6kh0-fkHjliLdlmsCYzXv4KJY7hyRS4T8azoTYKA1qE96uKftkYphWcV2skkRzY9wmuGyOp8FSuIT--ruzSDt7m-x_mINm4DovJLLhaCXTiHBl8pJIYDYH2pHFNJ4fAAUAGTlTmwOjISiLd67_X5oUjk1rmMh1t9BO8TfHLlRCgqlcoZZ3GtLVeWiINorHOYLTE6JtiCbP9HGMyZKhConba5tmJunHEUCL0oZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز اسپانیا
🆚
انگلیس را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
اسپانیا: ۵ برد و ۹ گل زده
انگلیس: ۴ برد، ۱ شکست و ۱۴ گل زده
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/107293" target="_blank">📅 13:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107292">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa254372b.mp4?token=olwWVNX50upcFlkBjGYV1fYRuG8N2l3cu87bRqBepE2khqdpFu1ky53nP2ZZya4RfZrYxlaLwptmnL7LHc8iZwgEs3HtBj5FX3FwetoPZbcU0lgDORTtuM4jX2qG_-NLRXvkyyD6E6aixrcUiuGBw-_a8lOz56IKZ8G8wN6LjMHBvGaBqucG46qz4JHpSQnEKsZbjTXDqzPY0F19B5WXxI3LHzef4Z3j7zcG9vZr5MJeCNKZw2J2R56VF20Dwuij9LEiMmX5Wkfe3h1B_d1P3tA_CdxmWFqxL0_SbQZDRKcN2ktMq0zpuQ2VwN8vcIUjtV7gdNN4s7amE0B21CljrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa254372b.mp4?token=olwWVNX50upcFlkBjGYV1fYRuG8N2l3cu87bRqBepE2khqdpFu1ky53nP2ZZya4RfZrYxlaLwptmnL7LHc8iZwgEs3HtBj5FX3FwetoPZbcU0lgDORTtuM4jX2qG_-NLRXvkyyD6E6aixrcUiuGBw-_a8lOz56IKZ8G8wN6LjMHBvGaBqucG46qz4JHpSQnEKsZbjTXDqzPY0F19B5WXxI3LHzef4Z3j7zcG9vZr5MJeCNKZw2J2R56VF20Dwuij9LEiMmX5Wkfe3h1B_d1P3tA_CdxmWFqxL0_SbQZDRKcN2ktMq0zpuQ2VwN8vcIUjtV7gdNN4s7amE0B21CljrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
👀
بهزاد داداش‌زاده بازهم یک ادعای جنجالی داشته و گفته که مجید جلالی جادوگر است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/107292" target="_blank">📅 12:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107291">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf4bbaac4.mp4?token=RIsdBalpPWFkFRQinAzbA0LpfIcL57i4zb5VDEoacPpIlKqVaK_-pRQ4sJElC13iVRFPCV6Gd8mgHxYiU2xtUkUV160J3bYI7eczmWGmfC_uy1rO0Lrxrg2hxY0pczH_r213HtQXeQePB2Yt4H9pcfsPVp1yFevzsjvmcNnnEeycARCaLLIByCj5Y8N2h0C3nFlNSZ_vfi5NsKWi-X9dXuDIt9msURICOtDWRHPDZrR3I7hpB5n-vURwLR-fE6taBxLZJLiJznae4kC_ZRAJ_AUPwGKAJYnMhTm6NQ9DD6sPxlKMbKe7UO_p54YEhEX1tlh3XGcWTLVRlipFHgh6bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf4bbaac4.mp4?token=RIsdBalpPWFkFRQinAzbA0LpfIcL57i4zb5VDEoacPpIlKqVaK_-pRQ4sJElC13iVRFPCV6Gd8mgHxYiU2xtUkUV160J3bYI7eczmWGmfC_uy1rO0Lrxrg2hxY0pczH_r213HtQXeQePB2Yt4H9pcfsPVp1yFevzsjvmcNnnEeycARCaLLIByCj5Y8N2h0C3nFlNSZ_vfi5NsKWi-X9dXuDIt9msURICOtDWRHPDZrR3I7hpB5n-vURwLR-fE6taBxLZJLiJznae4kC_ZRAJ_AUPwGKAJYnMhTm6NQ9DD6sPxlKMbKe7UO_p54YEhEX1tlh3XGcWTLVRlipFHgh6bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
گوشه‌ای از نمایش‌جذاب هلند زیر نظر ژاوی در اولین مسابقه رسمی مقابل آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/107291" target="_blank">📅 12:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107290">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b671734a24.mp4?token=EGdjExZBX4mIThLdLpImX-iBCeHllc2ec9RULskratgNqwKRh3_mmLEiTpsxYEYEH5rnGed2znz3ody1FN-xXHvV-4Vm2ZR6r2wXwyAJD-m6_RdyxkknSBQNHCKFsDPm-cXhvYVO7a9QIYeYn0upWNh3YMH1mYfOCwmE3rl8pEHJ7IhWRkWgaTpkMBuiVJYbN-UKZ_vZXC9Kv5YSTjpidPthLpt0OStrgiQCqqE5ofm033HSJvvbHxddVsjd02IzHZ4wq_nWIrTx_ZSbNjLjgGvnIDLIjqAivNk79uSFbiDM1DKK8g_vVCSrjal8vbiN5O55Lz-vJQ1to3gvf4IV5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b671734a24.mp4?token=EGdjExZBX4mIThLdLpImX-iBCeHllc2ec9RULskratgNqwKRh3_mmLEiTpsxYEYEH5rnGed2znz3ody1FN-xXHvV-4Vm2ZR6r2wXwyAJD-m6_RdyxkknSBQNHCKFsDPm-cXhvYVO7a9QIYeYn0upWNh3YMH1mYfOCwmE3rl8pEHJ7IhWRkWgaTpkMBuiVJYbN-UKZ_vZXC9Kv5YSTjpidPthLpt0OStrgiQCqqE5ofm033HSJvvbHxddVsjd02IzHZ4wq_nWIrTx_ZSbNjLjgGvnIDLIjqAivNk79uSFbiDM1DKK8g_vVCSrjal8vbiN5O55Lz-vJQ1to3gvf4IV5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت ریدمان کریم‌آدیمی در بازی مقابل هلند که حسابی اعصاب کلوپ بهم ریخت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107290" target="_blank">📅 11:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107289">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
❌
⭕️
#اختصاصی_فوتبال‌180
🔹
با تصمیم اعضای فدراسیون فوتبال، حسین‌عبدی پس از رقم زدن فاجعه در ناگویا، طی روزهای آینده از هدایت تیم‌ملی امید برکنار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/107289" target="_blank">📅 11:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107288">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dcbb333fe.mp4?token=UUBAKbRxsX0Yj1IsTutlqA4PbdWvO79LkwFQPJnXnvlOk9Clsxv6hk8BOr2N29ySksdftv4FQwHQOZ2_IzalW9lQxvJbl5QDMOL8cocbBxx_x7xBopp7yEaYgzx76GRu3wTfXS28w1CsDIyR71_Sf0S0cO0yyvA1Ojr9a10DNYAzO-fFK2PiG0Qfl-kp-Ci5QFub9sfMxljytldAegUuDxcN_Z6o4AAlhcC3hRRL8FCTtDmpUT3uxO4JGi5GzNx-DoWEs2xjntZ5a65iAmMsWIqi_4HJQ8t1zSMbO2bQPaGkw7szR4PpAiYBTjqSgwPkT5T8nwrIy0nQiwMPvzx5yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dcbb333fe.mp4?token=UUBAKbRxsX0Yj1IsTutlqA4PbdWvO79LkwFQPJnXnvlOk9Clsxv6hk8BOr2N29ySksdftv4FQwHQOZ2_IzalW9lQxvJbl5QDMOL8cocbBxx_x7xBopp7yEaYgzx76GRu3wTfXS28w1CsDIyR71_Sf0S0cO0yyvA1Ojr9a10DNYAzO-fFK2PiG0Qfl-kp-Ci5QFub9sfMxljytldAegUuDxcN_Z6o4AAlhcC3hRRL8FCTtDmpUT3uxO4JGi5GzNx-DoWEs2xjntZ5a65iAmMsWIqi_4HJQ8t1zSMbO2bQPaGkw7szR4PpAiYBTjqSgwPkT5T8nwrIy0nQiwMPvzx5yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
👀
کنایه حسین‌گودرزی بازیکن استقلال به ماجرای سربازی نرفتن علیرضا بیرانوند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107288" target="_blank">📅 11:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107287">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06c8b89d1e.mp4?token=KD6J2RYW3B_J-kE40cmdiadBPgO3vPpNL9hO2gFj0516lAodiPQ9bYD48PM0rSii2vQ3fCCC82PYQgpfoWpZNzyoEDtSbA5Mt9_u-car4uYYHqvCUvljNgutCKkfq_GDNC1hYWg0TAXzGej8ZSOZeQM0GklJlf6pswA4j25nXnrdyyj07awBIpMxQX9yNWZR275CliPC1WLOtz10Fxs_1tvFY-Hhf48fs0vGar-PkVznXJZ2UVBlAm9Mvc67jgOou7QMpg-wnnWkNA3eSYh5oJ30AoV9baFTD1bEK4Xle9DhfehZkRNObg9H50_bb37emu3-aLn-t1vS1fva8vVL1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06c8b89d1e.mp4?token=KD6J2RYW3B_J-kE40cmdiadBPgO3vPpNL9hO2gFj0516lAodiPQ9bYD48PM0rSii2vQ3fCCC82PYQgpfoWpZNzyoEDtSbA5Mt9_u-car4uYYHqvCUvljNgutCKkfq_GDNC1hYWg0TAXzGej8ZSOZeQM0GklJlf6pswA4j25nXnrdyyj07awBIpMxQX9yNWZR275CliPC1WLOtz10Fxs_1tvFY-Hhf48fs0vGar-PkVznXJZ2UVBlAm9Mvc67jgOou7QMpg-wnnWkNA3eSYh5oJ30AoV9baFTD1bEK4Xle9DhfehZkRNObg9H50_bb37emu3-aLn-t1vS1fva8vVL1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
تعجب کریستیانو از تاریخ تولد هم‌تیمییش در تیم ملی پرتغال
😄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/107287" target="_blank">📅 11:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107286">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd536968a.mp4?token=OYziJtLtHdnNfJ8sFSKQo4KyVopnKB6dtaVhicZCi9cIdUcLebVFtS9jDf1NdMtEuM8ZNQ3aV7os5d5kxorl3PWUPQkdj4eapssZDcgY4OA3XB9JKUshXs2H81W_VV3wveEjAsg_b2Jfree_RIX592ZCPKOCUGOv91LGiw_oy6e0qfIK5yK_eM9Qa7AExQQCG6JG1kMTSgeqzE66oZxKyixReguYKYO2Vr_HZdSnkhUY3iyvS1wIDqziESsy_zKXMiApZ-roJqWwZA_8Pye38I0mXTx6A47FmnvHQjIpZeoEq6WKwxBTJHMbTpxRsTqbomOCi-QeCOresoh8WkDyuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd536968a.mp4?token=OYziJtLtHdnNfJ8sFSKQo4KyVopnKB6dtaVhicZCi9cIdUcLebVFtS9jDf1NdMtEuM8ZNQ3aV7os5d5kxorl3PWUPQkdj4eapssZDcgY4OA3XB9JKUshXs2H81W_VV3wveEjAsg_b2Jfree_RIX592ZCPKOCUGOv91LGiw_oy6e0qfIK5yK_eM9Qa7AExQQCG6JG1kMTSgeqzE66oZxKyixReguYKYO2Vr_HZdSnkhUY3iyvS1wIDqziESsy_zKXMiApZ-roJqWwZA_8Pye38I0mXTx6A47FmnvHQjIpZeoEq6WKwxBTJHMbTpxRsTqbomOCi-QeCOresoh8WkDyuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
محمدصلاح رفته تو کوه‌های ترابوزان رو یه سنگ نشسته و حالا شهردار اون منطقه اومده سنگ مورد نظر رو جاذبه گردشگری کرده‌ تا مردم از نشیمنگاه صلاح دیدن کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107286" target="_blank">📅 10:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107285">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c6cfb864.mp4?token=RFnVpdsMHcz4qQr2zqlVMTrtQ8d8x_Zw7UtuY63PA32oGis6YVFqB9lY52YWoq5pJllYTWWZByuU9E_T1YxV2ZWBLvcb0UnHLrPxSYB1oUnt3FYp5ymZRpvFLhWV2jMZUFkauJM7555myV_uds96pBrSv9ZnQh_DIg8q2Gqj6Nd95Wv6Hj4bDKVtkUEfz-y-wM74l_0EYrPR9H_n0n-D-5-wd510MXjmOlXfCeakH4IeE6KwCXiCTIcuqV7kwUzsSdTxjbV8ldZcSZW1OA7IFJ594UJgRkXGCE_vR1iL2BjCP0Ukmn9dUd6qzN6q4MzWrpdh2FeUGO2DB667us8KsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c6cfb864.mp4?token=RFnVpdsMHcz4qQr2zqlVMTrtQ8d8x_Zw7UtuY63PA32oGis6YVFqB9lY52YWoq5pJllYTWWZByuU9E_T1YxV2ZWBLvcb0UnHLrPxSYB1oUnt3FYp5ymZRpvFLhWV2jMZUFkauJM7555myV_uds96pBrSv9ZnQh_DIg8q2Gqj6Nd95Wv6Hj4bDKVtkUEfz-y-wM74l_0EYrPR9H_n0n-D-5-wd510MXjmOlXfCeakH4IeE6KwCXiCTIcuqV7kwUzsSdTxjbV8ldZcSZW1OA7IFJ594UJgRkXGCE_vR1iL2BjCP0Ukmn9dUd6qzN6q4MzWrpdh2FeUGO2DB667us8KsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
کنایه گودرزی به ابوالفضل‌جلالی مدافع فعلی پرسپولیس: زمان مشخص میکنه کی استقلالیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107285" target="_blank">📅 10:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107284">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4908c84c8.mp4?token=NDkL9XIgqBOLs9MtWdyzDtaKtULjRI-e5L83fXxkC9VqsIIlbB4C8857ECS-0aa4A4haTnO9eERKd3XquIwhRyDJ5IdAJXPABu2UPgFag_tOyts5rt8Jaz6B2o0eEDgLqOabI7QFL1MRQcR-0qRoM0-qXMydm3JERoAgTaDjvrIXpLp5Om23N_cHpdH09wyeqRTgVhU49-ngYYhHbsiYCwXS5bquT1UUFLpXumkGP5LbQdHXjzt0OIRcL7-fAbSsta-n5fJFOUjn_7MMuYLxN78_fur_KXX8S8bVjnmj5Tko84d_VgHRx_yRMENi-s5VWGfCoRF9j0S0JuMYvIJo1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4908c84c8.mp4?token=NDkL9XIgqBOLs9MtWdyzDtaKtULjRI-e5L83fXxkC9VqsIIlbB4C8857ECS-0aa4A4haTnO9eERKd3XquIwhRyDJ5IdAJXPABu2UPgFag_tOyts5rt8Jaz6B2o0eEDgLqOabI7QFL1MRQcR-0qRoM0-qXMydm3JERoAgTaDjvrIXpLp5Om23N_cHpdH09wyeqRTgVhU49-ngYYhHbsiYCwXS5bquT1UUFLpXumkGP5LbQdHXjzt0OIRcL7-fAbSsta-n5fJFOUjn_7MMuYLxN78_fur_KXX8S8bVjnmj5Tko84d_VgHRx_yRMENi-s5VWGfCoRF9j0S0JuMYvIJo1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
وضعیت روحی مورینیو، هم اکنون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107284" target="_blank">📅 09:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107283">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c02c187832.mp4?token=i62g5bYnBbWUDEriKLRjzDKEmlvUmA5UH_7T43mmGOPjnaYgvGPMImQ6vM1McIRq2TiXOVa0ZRA3zz3yZAMfmwLKOwV2a-8wFjU1vemA2oiO0t3G4NKMUcJu2rIqW_spMx6T9gK4aqTXiH6g7nMFnZIIDLgVGjF2FebWO8j3VR7fTVqXAXct3Rx7QxBBACTU0u0s09KZK9rdz-apQJqNOFYhOz_xVzdtJEps3zfXKmEBn4nyAYcmrORlT38UICvtnOuOtZvg8uZSPXfXj9ldulQVOp6QB2Q08wk17GsId8wGxTsM287cTPZ5aX3Fe4ic9SYnDR4uhOYd8vxyEl5OYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c02c187832.mp4?token=i62g5bYnBbWUDEriKLRjzDKEmlvUmA5UH_7T43mmGOPjnaYgvGPMImQ6vM1McIRq2TiXOVa0ZRA3zz3yZAMfmwLKOwV2a-8wFjU1vemA2oiO0t3G4NKMUcJu2rIqW_spMx6T9gK4aqTXiH6g7nMFnZIIDLgVGjF2FebWO8j3VR7fTVqXAXct3Rx7QxBBACTU0u0s09KZK9rdz-apQJqNOFYhOz_xVzdtJEps3zfXKmEBn4nyAYcmrORlT38UICvtnOuOtZvg8uZSPXfXj9ldulQVOp6QB2Q08wk17GsId8wGxTsM287cTPZ5aX3Fe4ic9SYnDR4uhOYd8vxyEl5OYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
کنایه توتونچی به ابوالفضل جلالی: یادش رفته بود، که گفته استقلالیه!
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107283" target="_blank">📅 09:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107282">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGf-xqvpSMbbhqNZWR1yRLi9s-cMed6nko_thHteXW0XcAqejsNQqzs_9lU0V24yihQ7VG37lwAKBUdI_Wa80HP4MK3YSvlNQaGK-Lpyhi2VAZCyyNY_ieti032LANrVO11uJleiwQ9VZU_GKrVOnhhDUbhjAXQxXJFnWMKuRw6yhcOqRwmaILwKww58vkRB-828Pnyw_SyGrjAcyjE2SDrSKWoskvN1XGZ1rlmjlLP4l53as20gr_YGg245uX-YZFJ_kRlvi_YOdGILrPZMyby5Dp0jYVSWwQeUbKtHH9wvhW6xegNFZjLSE57D67KNV9YPdiHH4xPl1JXsx5EJjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚑
🇪🇸
آخرین آپدیت از بیمارستان شلوغ رئال که کیلیان امباپه هم به این لیست اضافه شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107282" target="_blank">📅 09:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107281">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEnJThVaxbOkDPDNl_8lPFXnxUjrrOhtOlotfZnZ4ao9AmHNN1gADi-Xliqjcz1D4ESM9JNf9aZPhdeuEVEw2IpRYo5jmo0fIazJR3k3-_VKkFtPFBtsXlRBH9ADje7SbrzeWWQbWLCZ5t3Ui4i9jKlAcknLGMF4oOWJNuQ6gh-UIU3Jlp7NgHrshJgu_UrVZS7Wx3bvI4vyQAKvLs-Q0XG5oBCGURMMAvHrNv-XN_AI1vHDBbiApnqJrjqyuzS6SLnTa4le-eGISrsD_xaAHjX82GAMiOYEjXSdCcLrWHPFWSRMaSr4zCJUXU_HgWdirryoT7UoL-xU9d3fvLe18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥈
تیم‌ملی کبدی بانوان ایران با شکست مقابل هند به نایب‌قهرمانی مسابقات ناگویا دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107281" target="_blank">📅 08:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107280">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d41de8e91.mp4?token=GQuHLJjbQiLozuAyUji57mWJENcCS84SDSL6bPIqO33976po5hX3CjKSE9rxYXo8glRAJ-gDKH0nXVrScxYdCMGmhgMjvca-yVOlV76cfUCMs0DL6v17tdbFCWdEtqu7a5vcM6wh4i9f2G1kmC4C5x_OUwPz8HgnRJccQiavZJyTRzsG3oXnSu2HmnjeP5MHCwFtiXWsJ6ms2suFvcjvkoxsEah2t3y2Vq7u28jiVi2DAHgUtdMqYgk1qi1cT1juIR5nod_mG0NOdtJJIT1mWu0a0v83s2onIWLLmvtDo-455XvIRamHcqAOO6y5yxzmZIbAPtb3QNOxrioWD4Xb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d41de8e91.mp4?token=GQuHLJjbQiLozuAyUji57mWJENcCS84SDSL6bPIqO33976po5hX3CjKSE9rxYXo8glRAJ-gDKH0nXVrScxYdCMGmhgMjvca-yVOlV76cfUCMs0DL6v17tdbFCWdEtqu7a5vcM6wh4i9f2G1kmC4C5x_OUwPz8HgnRJccQiavZJyTRzsG3oXnSu2HmnjeP5MHCwFtiXWsJ6ms2suFvcjvkoxsEah2t3y2Vq7u28jiVi2DAHgUtdMqYgk1qi1cT1juIR5nod_mG0NOdtJJIT1mWu0a0v83s2onIWLLmvtDo-455XvIRamHcqAOO6y5yxzmZIbAPtb3QNOxrioWD4Xb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وضعیت دیشب امباپه که شرایط نهایی این بازیکن تا ساعاتی‌دیگه مشخص میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107280" target="_blank">📅 08:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107279">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107279" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107279" target="_blank">📅 01:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107278">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvIP3aT1E0QarzO9XZZqIYvHywEoo17N59Ot7Z69xa7tjpukpdmGvz94RJiGEjOHurI1ckqi4pG6oZbev6SaM9ms7xbwPpt3B298hRwfFYWYCURJMcXcVjd02FWCCK2ixrlk7zfSNPRbGeMfF5lqG1Ig1V1AF4d2PZuP33KlfTuGMla49YNQTpswh3iZyThJFbhUvlnOpA2DF3NHlx5552VFw57zzdbwYtbLFzLVZdh00H9lkagIJ0Q4Z_-aIRb9tdBhHdrEVqU9MlfGm2fe8Ptfxzacp8SfXYpKEv1yJdpKShAyqtw6r4h7BIbWG_I3l10hNNYRfDZtsQ1WIU9Xdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107278" target="_blank">📅 01:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107277">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfo2YaF_d-5bAeHuUHZxHb5xDHDkE3it8DNxNWdVCEJ8fJEiIyRTmoe7ypFMWK8gGHap6SyMpnCdUCaxwphVudXqRKmgfcZve0P7fUleLLzE4p1ZnMaKoWPWXCmPfAc7K-eKE9whxyRAN51CMC9yxTHQt-EbBteHDSEmGczgHeu_UNOhWqKSMvQh4ImgGgfJh2OPtb_N-PFyIlVwGOpjPfOoDnT8sCj2VhaUAUtCnj-YQ9LhAJQCRpDhensTUx1dJM06qiPpeVUx9il06wsMJQX4BacqxcYS3VRHDf2ZkuoGqZ578UXVAshzA3BY6SkKJBM9MPI5KYgZ5xNG-gL_8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
©️
با اعلام سرمربی تیم‌ملی آرژانتین، کوتی رومرو کاپیتان اول تیم‌ملی آرژانتین پس از خداحافظی لیونل‌مسی افسانه‌ای شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107277" target="_blank">📅 01:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107276">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkXB5jWpxmOfXTho4MrvGhnrxU7kFmQXbBM-kOBnlWpBM6MliZS7Oh_rFOo-_qwsxsOV3rKcQ0ezYwvflKeAKnG0kPYysj6Hz8hvw6dw3vX2k3LaQnLUrssD491o2qTPagsbxbgIEI_bzuT2IHiz7v7_IWrPuyvd4bMdCdX-JMNGwRGcSojCbLMxiLvrY4Nvcf-rPA2bxEKaQ_XR8JHyja9F07_Ijw1cN8Zhz6eQmVapbRJdbrO6-XX6C_eSfe-9mTOrwnpC1lt72MDdTQrnsYmgpZKwCdcBMCUNtRB8ISk90M4vFP958rxn7h7zj-gJiLhi3wJTbAkBw5Vusmpe2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
رومانو: امباپه بدلیل مصدومیت زانو از اردوی تیم‌ملی فرانسه جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107276" target="_blank">📅 01:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107275">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9kx-GOS-qjS5KQ8O_Ab-8PDt5MxRJ11gtPKI8-_FRKAnAaAQS02QQK7bpwsDuwqhqrpjj4lHrJKnPqf3CH4UbhAvkyod-1e4DHKyARwmNjAJx1hOGPhOVT4NBTvGRYqOZLT-tvocIyESFoTQtma6LgQIvUy964jWcbzgHlH3wr_Iez165rdu30wDfWph7iRPDeWo5le0QcRQlG7eYYHTWff4hig9raL1d32HAeHpCgMcixyqd8bzslPe4YEHUOrRFa5hGuq0crtzzyvk4h3gSnjv-yX5jCrO0lv1tnI8jC06Mb1jGIo_te_sTCftmHwmStr6gxeX93P2Q40qHJYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
رومانو: امباپه بدلیل مصدومیت زانو از اردوی تیم‌ملی فرانسه جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107275" target="_blank">📅 01:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107274">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcF-SXIRt72KGiXP7Vw9RB3x7A4HAuywURx54B7fQlZaAjI6GBioCuw_PIo_DS8WFfkm3WbtdDjhv64ihods4Ty6-HPN9Rb9D_yFGTUGcL6B5SaTVdszU51TlBgGuCbNFnJMdjEMEKaHGaSpwezRo6zE7N_mvG8yUM9ERxzwC6ceyhu0DE132pTMVG_Fk3x1ZgRrbAPgFYx-ZccTDdJSGsY_yJUsRBvpJJOWCiOESGdsuMCF8Rppmv2QdsB8ezL5HarJmcDzJ3J0PUQ71NZCzjQF-rs3nCzf3GS8YVWj31107Kp6EuXKGlOHQ_92B2xy-5ws1hagJeEeTkBXJbFeaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
• امباپه به 107 بازی ملی رسید و رکوردی را که قبلاً باتریک ویرا ثبت کرده بود، شکست.
• او هشتمین بازیکنی در تاریخ تیم ملی فرانسه است که بیشترین تعداد بازی را در این تیم داشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107274" target="_blank">📅 00:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107273">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdlAXmAfLMlEYgRFgZ0FeA4h41b90kw7Qb3kQaUXGRhV-eq2yu7FF7Cj9tgY9mjcajMFp4t4qbNCSmuryUBrnu2kC1nI17hF1_IIgEBqbW6PcVxOGsUWzv_vphTnw9db4HUXZ88EZp3MJTU1sJVu1oAPO18TLf286f2oSOrRFoQcG3NarAzysaaCH-UWdeKQFTfYPALrWfzrv-RhxLMorCMg9xyEgVcr3oWRukjXMjDUbKl7IysE_7EGWjXB81cnLuul2aWp3PfILkDCPri9yUtabaq--m6kQadU_T4FplnzKJ-1JEYHwsnxtDU0z6cexoi0J-ZkBThqMmoZ2yIVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گل‌اول فرانسه به ترکیه توسط کیلیان‌امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107273" target="_blank">📅 00:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107272">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWAOGM4cKCN2omM6T4KKiola1lHdxLNmk-GciK-8ji-33-bf5shqGGjc2d67QN6hVRUa-gcGFLpDO1gTWm44-paru5M4qcs03PAgwh7Cd6pAF_HKrVEIE5mB2eCs0SoKhSEArV8CdLBFy0IOVrKGa5BzGKk0I9xIN3Ex75yyojX7arr3Xb8bF9loyRSG2ctfm-LzSGa66bE-DZSEo8zzWt3s6DegIA0rFTJnmnFr6LGrPFsyD6rcH1JQdP579d0IKfGV_m64x1vpmR4Aihi2UMDrKOeDXtCfUHOGTrBR3lh_SVDatR-ORbibzjjN7OLRkV3_B-_2p259dM93wdtnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
گل‌دوم بلژیک به ایتالیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107272" target="_blank">📅 00:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107271">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6892ba52e.mp4?token=RmpR44f-Sn77ITwfE8oAOAs1kKkZd46BvRdcM_mo0_lK6Vp5jYXPDDyNExO8lCy5pCGNMt-8JrRl24m6bxTdFrgddyIHASVPBypkwqZ142BmROG4WaC2F6OBl-vK6WpExEVmo7Iyhu6TX9QzalD6e-kAJY-TxukS4VwsxfUfBT99jyzY7ldJsk6mf48tONreKpBzbl2egzzPBgKSOKQpCuBYBB3m2rSuNh2uYIiivqAAZtJJP4s-EuprhGtSsolAik4aT6Mz8fCXU9nKiLQESCw3chrxmMv13j8PVJO7HVIl1vh6TxlS2PN4GnSPyhoR6Dv-gO5A40CuMd9vstkfzUWtOILfF2VqE9QUD56Pego-C5g6hIgDMQ0isi9x1IvUQDEt1McQ7OA_6Fh_130gSXujiWjtnSYACALpneLgWJ0lmGj9h_iOBTr8SIeYq50F-Q7iaTC4aYmdzz4qBbgRChDrZbTZr56pUzYM0AudzHpbj2_3-5ZfA3TlG5VPB0XYVNe3e6sq7Ip9u0TAQ_fJqLGnrBG9lkQCFDSsYeYri_CyNA5vFwAt8oVBlppPZ92m8exPEG5vWbOVPTw9azQEbPP6Y99M4VntpMpDcN1WpIaM-dDi4A-Zqf9oFa381qjrmUIbg3DDSIQpB7qNrHAYsRSWkZ6JHwz1IEFeP_7we6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6892ba52e.mp4?token=RmpR44f-Sn77ITwfE8oAOAs1kKkZd46BvRdcM_mo0_lK6Vp5jYXPDDyNExO8lCy5pCGNMt-8JrRl24m6bxTdFrgddyIHASVPBypkwqZ142BmROG4WaC2F6OBl-vK6WpExEVmo7Iyhu6TX9QzalD6e-kAJY-TxukS4VwsxfUfBT99jyzY7ldJsk6mf48tONreKpBzbl2egzzPBgKSOKQpCuBYBB3m2rSuNh2uYIiivqAAZtJJP4s-EuprhGtSsolAik4aT6Mz8fCXU9nKiLQESCw3chrxmMv13j8PVJO7HVIl1vh6TxlS2PN4GnSPyhoR6Dv-gO5A40CuMd9vstkfzUWtOILfF2VqE9QUD56Pego-C5g6hIgDMQ0isi9x1IvUQDEt1McQ7OA_6Fh_130gSXujiWjtnSYACALpneLgWJ0lmGj9h_iOBTr8SIeYq50F-Q7iaTC4aYmdzz4qBbgRChDrZbTZr56pUzYM0AudzHpbj2_3-5ZfA3TlG5VPB0XYVNe3e6sq7Ip9u0TAQ_fJqLGnrBG9lkQCFDSsYeYri_CyNA5vFwAt8oVBlppPZ92m8exPEG5vWbOVPTw9azQEbPP6Y99M4VntpMpDcN1WpIaM-dDi4A-Zqf9oFa381qjrmUIbg3DDSIQpB7qNrHAYsRSWkZ6JHwz1IEFeP_7we6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
گل‌دوم بلژیک به ایتالیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107271" target="_blank">📅 00:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107270">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fcef0287f9.mp4?token=IOtG0BAdQbjpwkRE9XckNpR5-f-or2GL-T88hApyEU-iGj24w_G08TD5fgvvE8yBaXzGvGC1UnzW5125Pt-4cvpQf9yQGIXI0swO0B9ZaxgRpy6uFAq-I4ld9Lu1oOuGI0qe3H9YhT67onLNkeXBTHpIGAH25mI59GjmZmFYh00r06Be0I8Dp3UAy6MBJeyU0riDSi0fkjgDlSRyO4qDuKBGZcFKmjNK_TOW2t8yF2N_7qx5nLPiz3prQdyZ7XOkqP0y-f2qHIU60s5Mo8cAH0LZ_79xjnatlIeiuEaQMuvyMqp9V4tWTYuzWLSniIqE9FkR43HrNIMq_TD7flM7yYGUvsinEnTbv5nCkUDYQdo_wB_OM8p33JGq3IRnf2rQmi98BL07vZpa-Wt6rMHA7ZQ6iXwDN5sdvJetQa68m2u5mRT-FlBLILY1i0dNVuknsYUhzaQ_yOBQUeKYAs-KJwKKdPWmdh8Yi9eINXeOzIHyneWZ1iqjCdSNxnNxJwPMiHXhW4cvpLPpEWBeL4sSwxVG6UnKBo0C8-lyeOnlNu-M9dsYNak_oIAYs7bat5dC9uwslkDzLXdEX2Xa6PjWk1C2wNJ0ts_K1Znvk4pBV1XNLXj1fIYfNFrhhFH3dnUJ6H6PsMwhc3_e_TDuDdm35y1iXAtegQBwmtYwkS13zJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fcef0287f9.mp4?token=IOtG0BAdQbjpwkRE9XckNpR5-f-or2GL-T88hApyEU-iGj24w_G08TD5fgvvE8yBaXzGvGC1UnzW5125Pt-4cvpQf9yQGIXI0swO0B9ZaxgRpy6uFAq-I4ld9Lu1oOuGI0qe3H9YhT67onLNkeXBTHpIGAH25mI59GjmZmFYh00r06Be0I8Dp3UAy6MBJeyU0riDSi0fkjgDlSRyO4qDuKBGZcFKmjNK_TOW2t8yF2N_7qx5nLPiz3prQdyZ7XOkqP0y-f2qHIU60s5Mo8cAH0LZ_79xjnatlIeiuEaQMuvyMqp9V4tWTYuzWLSniIqE9FkR43HrNIMq_TD7flM7yYGUvsinEnTbv5nCkUDYQdo_wB_OM8p33JGq3IRnf2rQmi98BL07vZpa-Wt6rMHA7ZQ6iXwDN5sdvJetQa68m2u5mRT-FlBLILY1i0dNVuknsYUhzaQ_yOBQUeKYAs-KJwKKdPWmdh8Yi9eINXeOzIHyneWZ1iqjCdSNxnNxJwPMiHXhW4cvpLPpEWBeL4sSwxVG6UnKBo0C8-lyeOnlNu-M9dsYNak_oIAYs7bat5dC9uwslkDzLXdEX2Xa6PjWk1C2wNJ0ts_K1Znvk4pBV1XNLXj1fIYfNFrhhFH3dnUJ6H6PsMwhc3_e_TDuDdm35y1iXAtegQBwmtYwkS13zJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل‌اول فرانسه به ترکیه توسط کیلیان‌امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107270" target="_blank">📅 23:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107269">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتین: درحال حاضر جریمه کسر امتیاز محتمل‌ترین سناریو است. در صورت شدت این موضوع، ممکن است حکم سقوط سیتیزن‌ها نیز صادر شود!
⛔
🔺
سناریوهای احتمالی برای سیتیزن‌ها:
🔺
❌
توبیخ و جریمه مالی.
🔺
❌
کسر امتیاز از منچسترسیتی.
🔺
❌
کسر امتیاز + سلب جام‌های…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107269" target="_blank">📅 22:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107268">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a64700b02a.mp4?token=CT_Ce2yZzce5tDRv06ds7sg-eVN0V7zZlgniXU_A4gA7lKEicAACE14jBjNljU3cwQt5p0qTGgCzTOw2iv1mp7bhuxMRe_Qc9xTpEuQE1umFBzNJxha_KgibtSTJc5MhEGRx38yTbqaCPDh231tLrH5G96slbT4YouQAIbN7KGOcoV6vim90Yox8pEESewavy7OaUHmi9nvc20uiNHYpjex5LIpne06uCBI5pP83i6XtVRdXGmdrydYh-4Rz7tF1l3p2FQT5kgSBOH1hfJGhOtIuE_3bfA3uMIDl-7JDd4fw_13bRh_0kZsYnTs9kUdsPwMTLfbXCN_KjRNdD0vIATzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a64700b02a.mp4?token=CT_Ce2yZzce5tDRv06ds7sg-eVN0V7zZlgniXU_A4gA7lKEicAACE14jBjNljU3cwQt5p0qTGgCzTOw2iv1mp7bhuxMRe_Qc9xTpEuQE1umFBzNJxha_KgibtSTJc5MhEGRx38yTbqaCPDh231tLrH5G96slbT4YouQAIbN7KGOcoV6vim90Yox8pEESewavy7OaUHmi9nvc20uiNHYpjex5LIpne06uCBI5pP83i6XtVRdXGmdrydYh-4Rz7tF1l3p2FQT5kgSBOH1hfJGhOtIuE_3bfA3uMIDl-7JDd4fw_13bRh_0kZsYnTs9kUdsPwMTLfbXCN_KjRNdD0vIATzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول بلژیک به ایتالیا توسط میکا گودتس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107268" target="_blank">📅 22:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107267">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ایتالیا یکی از بلژیک خورد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107267" target="_blank">📅 22:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107266">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvDSJ_e9jW9VQ3cMg3skn5jhropYC1P_5TN_vOKkxycREOlo16k2mH-7d17y1_3lZ_LAV93_oAWAHLy1E6MTaLhNkFtcjTzZ-kZapg32_x7uoJGK5GXiMQMJqE-SJwSNsdtsG6IFDbnCUpAbNfdVRPwVPIuEshebfEXFRucofFAZPZmy4SwEN0OPpI5VTmtLJUrm-pj_sAyYhImJ2CNypjHeX0ptDqZj3VaydPgIb1PNymfDvNbA9KsdS4fAJ9kaVq1do1UsI6BGBlT2jyq_fOypZwXzwlJFQTTkFRiJItSw75O2AqvvSWFxkduLD87WaGDosZ9Irlc_yk4Y9k5MxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتین: درحال حاضر جریمه کسر امتیاز محتمل‌ترین سناریو است. در صورت شدت این موضوع، ممکن است حکم سقوط سیتیزن‌ها نیز صادر شود!
⛔
🔺
سناریوهای احتمالی برای سیتیزن‌ها:
🔺
❌
توبیخ و جریمه مالی.
🔺
❌
کسر امتیاز از منچسترسیتی.
🔺
❌
کسر امتیاز + سلب جام‌های…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107266" target="_blank">📅 21:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107265">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qD0w1ifRdebib4ynvTsT1QkFMtlN1TJ5ebyrPx2LnRsN6XrQSCosaB6alIfa6-5_10WvZ4Wq0SzS69aadapn9wQisgwgPP4qnLlRcQaK_40KutG7pP2gPziv6h4pwSaKKP13oDX05Q9-0gmiDTEGtupcOqnACEi87jEFhsDGgL9TOmtwasfdgzIJpRRZy0e5kXeKykralKoYq4xeXFIvwFTRbACsmg3X6DA2mUB15feYt4NuMDM25fZcSPypcCH-fQFWkOaTEeL00DEU_6l3L20tBi66RFMEFxn2QzGisXGFhKV9XZchZV4DSIEApaekbTomiXGDzy5DdfEd4vSBEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب ایتالیا و بلژیک | لیگ ملت‌های اروپا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107265" target="_blank">📅 21:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107264">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfCbnESiW9MClZqOA4L-n8i8qPk15KNgUFZ3lq6TjrwPw8amcophgLOH-MgyOUiXBwGq1QtJN050bgwvxWJaAaLP11JaAB4ojOTeDrDlpPWrSltoJUitS3FYo4dz1HYLn5qr3TzW1kcPmjqslBTnu-8ZVxIyCShrg08Pm2X9BMNABaY_dHyRhAg_asWnD4WIfVMKZAKWz_q_Slub9wYbhKOmiOLsUa0jVoPvXG2sgOsB6347BymFbc6Q0rvGEM7dQ5xCt_CmsExA4YMUAi0TdrdCxdJrOeoUDDyuBhr4Gd9bbgg_FJp0tT9VDdqyU1xLp-SBfug9mUu51_4LCEQv0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب فرانسه و ترکیه؛ لیگ ملت‌های اروپا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107264" target="_blank">📅 21:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107263">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c2608c24.mp4?token=vYkI3zClznaXD9P4r3bPgqsdTSl5Mmbwp8TAEfAvO8iZ0uzOqu9oeUvZ0mhqwMgD3GF14TIYmsnnIWvnR8qE55B3V_gG_jYBJou3AnQAAhMnQ-Tr5ay3s9TBqdM_cvHQ3SQ4pvgBtIcfepbvOu6dZHxKphBn5KkvX0SZ6uFBMzMhllV9Dt6FQEJa1hWg4IjJqVmEKcvmn2Ci_vJ92ryW6riIV9TjIB3N----vD0FXoFESeITsM1FiuiM3qb8jpDQAMMvNQMwh2Ern9tRlMsjFzq2E33i4gf7wqcf5aXpUejJMxzeoJ1dLivycxNXRa-Udp52AK4mhdhf7rK86M680g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c2608c24.mp4?token=vYkI3zClznaXD9P4r3bPgqsdTSl5Mmbwp8TAEfAvO8iZ0uzOqu9oeUvZ0mhqwMgD3GF14TIYmsnnIWvnR8qE55B3V_gG_jYBJou3AnQAAhMnQ-Tr5ay3s9TBqdM_cvHQ3SQ4pvgBtIcfepbvOu6dZHxKphBn5KkvX0SZ6uFBMzMhllV9Dt6FQEJa1hWg4IjJqVmEKcvmn2Ci_vJ92ryW6riIV9TjIB3N----vD0FXoFESeITsM1FiuiM3qb8jpDQAMMvNQMwh2Ern9tRlMsjFzq2E33i4gf7wqcf5aXpUejJMxzeoJ1dLivycxNXRa-Udp52AK4mhdhf7rK86M680g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تقلید صدای جالب یاسر آسانی توسط حسین گودرزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107263" target="_blank">📅 20:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107262">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔺
✅
🇬🇷
روایت شنیدنی نوید استادرحیمی از تیم‌رویایی یونان که در سال ۲۰۰۴ قهرمان یورو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107262" target="_blank">📅 20:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107261">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19b5e1f435.mp4?token=G4ftMtzovNLuoRqwuWInXzAQJaGxbumeTJEuvZqTtW4fTWIVikUIrdyof-kOG_4SA6SA-51eKX1AC1QKY93sIxAdeQlCoNlcJNMb9xT3_aUZx_oT5zbWBRhQGE526Ef-CXGqJW7bTRJu2ZCPcJuOycjZBXHSQuZBR6hNOuif5YXqO9gxnX_pPaMVKa33mjCnjKsnqWXm1nWh-LllN2OFoBKZF944d1BhT7IdWJlwOblexDDhvLppVscuCFONWYRNXo1AcEpDqno78aA-66X33naAn84g0GdYrHaMPw_QTaNBXb_jwg2D-JEQY2SCBscHQk5FSl5YtRLaVH9WTVu1mVxIAUOUT6OZuE_3q0o0Rh0A5gzY-UYkU3gf45MEKFEsAcrOp0M6GxIF6wO3g9yRG7CFSqSvEd2QV0jh7DxH7kfIE8DEJGPtRa6PlQkQkXGRchT1JvH5JbrvG36TJ9T2spJbkHRyW2rVowGEO9WkYg02n4RyPYw6ap1-7VJr7PcaTKvkXtCnDH_TJUCu6GSjpR7fFzf1azdjDybTSUfAhNlAWW2LWoA8Kc2K955nLzbqIR03iweyMzOJekM_uwwdaqrOqUjeiJ3ENI3azIIJlrRRSl1Lvc4n0TtGUkiiCxSTh-aZDDtOeV4OjmJkw0IoTqWpYVN3ERkmonPykS8G_p0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19b5e1f435.mp4?token=G4ftMtzovNLuoRqwuWInXzAQJaGxbumeTJEuvZqTtW4fTWIVikUIrdyof-kOG_4SA6SA-51eKX1AC1QKY93sIxAdeQlCoNlcJNMb9xT3_aUZx_oT5zbWBRhQGE526Ef-CXGqJW7bTRJu2ZCPcJuOycjZBXHSQuZBR6hNOuif5YXqO9gxnX_pPaMVKa33mjCnjKsnqWXm1nWh-LllN2OFoBKZF944d1BhT7IdWJlwOblexDDhvLppVscuCFONWYRNXo1AcEpDqno78aA-66X33naAn84g0GdYrHaMPw_QTaNBXb_jwg2D-JEQY2SCBscHQk5FSl5YtRLaVH9WTVu1mVxIAUOUT6OZuE_3q0o0Rh0A5gzY-UYkU3gf45MEKFEsAcrOp0M6GxIF6wO3g9yRG7CFSqSvEd2QV0jh7DxH7kfIE8DEJGPtRa6PlQkQkXGRchT1JvH5JbrvG36TJ9T2spJbkHRyW2rVowGEO9WkYg02n4RyPYw6ap1-7VJr7PcaTKvkXtCnDH_TJUCu6GSjpR7fFzf1azdjDybTSUfAhNlAWW2LWoA8Kc2K955nLzbqIR03iweyMzOJekM_uwwdaqrOqUjeiJ3ENI3azIIJlrRRSl1Lvc4n0TtGUkiiCxSTh-aZDDtOeV4OjmJkw0IoTqWpYVN3ERkmonPykS8G_p0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
بابک مرادی بازیکن سابق استقلال:
🔺
به ولله برای خودم اشک نمی‌ریزم. مگه میشه ایرانی باشی و با این همه ثروت کشور از گرسنگی بمیری؟ وطن مثل ناموسه، برایش جان هم میدهم اما الان شرایط اصلا خوب نیست
🔺
در مراسم عروسی‌ام چهار هزار تا مهمان داشتم و پول یک خانه را خرج کردم اما فدای سر همسرم چون به عشق اون عروسی گرفتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107261" target="_blank">📅 20:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107260">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a1de71c42.mp4?token=Iqp9NSmnW_RKmSXfvPB2wPUzEiUWaOJQUQU5Uv4nF3vA9ie_woyeBd2MRVzxyuGR1HB1V6OatfhmRQgzbm423piSvUHhGqgGFxewlZI2piBctD7bYBa8zS8ApctB0mOxIGsx0lCYo5SSqID1nuQCWGeNJlEyDRk_agvHZso_dxg0M0KIqqHAALueyAbz_7kn1y-wGrKin3SmliZitjqF7A2V8s1uUpMeLygC2cJWE0dY8KvNXlc1Wr8BxFCc8cie67JO1RKptuoecgxIbmB4MVz7e8qtjquUC_Cq3_7hiSUfn4X2E66_XkSDMX-_IBLKAq9LR8Gek3Tr2MdOVrNZ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a1de71c42.mp4?token=Iqp9NSmnW_RKmSXfvPB2wPUzEiUWaOJQUQU5Uv4nF3vA9ie_woyeBd2MRVzxyuGR1HB1V6OatfhmRQgzbm423piSvUHhGqgGFxewlZI2piBctD7bYBa8zS8ApctB0mOxIGsx0lCYo5SSqID1nuQCWGeNJlEyDRk_agvHZso_dxg0M0KIqqHAALueyAbz_7kn1y-wGrKin3SmliZitjqF7A2V8s1uUpMeLygC2cJWE0dY8KvNXlc1Wr8BxFCc8cie67JO1RKptuoecgxIbmB4MVz7e8qtjquUC_Cq3_7hiSUfn4X2E66_XkSDMX-_IBLKAq9LR8Gek3Tr2MdOVrNZ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🐐
👀
مورگان راجرز: رونالدو بازیکن مورد علاقه منه اما من در نیمه‌نهایی جام‌مهانی در برابر مسی ۳۹ ساله بازی کردم و باورنکردنی بود، تصور کن در دوران اوجش چی بوده، نمیشد در برابرش کاری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107260" target="_blank">📅 19:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107259">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/203f6a5b45.mp4?token=H7kqEu8h5gNaaLmy_Q-IL_axznIWVBC3rRysBqOAtGZasNkIN9G2vwjZ4Ic-SjYAUwHrCTzF0b7rHdnlXGTMHBgc3LRfNivAzBcsSWqHnlktKX9xNSZb9hluVmXBFNbggI294xeZaHgeDjF8fTHFhMB-p4F2mEj4uq4NkqwsoUXv3-Y9dcI2WAfKKtdDDy9JdMkv3rVHgSCzhmR3iTeh2evUY91HlWW_vaNRNvH2wtBxlL5PEqj7gF8vAvEkQPbBHbhlWVaakBZ-mReAvkGTclpCMCYiw3ZeRXNLutLQocw-Voc6H8YndAF-pcCqvwtotwJGu0TahLSIMhubExiyvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/203f6a5b45.mp4?token=H7kqEu8h5gNaaLmy_Q-IL_axznIWVBC3rRysBqOAtGZasNkIN9G2vwjZ4Ic-SjYAUwHrCTzF0b7rHdnlXGTMHBgc3LRfNivAzBcsSWqHnlktKX9xNSZb9hluVmXBFNbggI294xeZaHgeDjF8fTHFhMB-p4F2mEj4uq4NkqwsoUXv3-Y9dcI2WAfKKtdDDy9JdMkv3rVHgSCzhmR3iTeh2evUY91HlWW_vaNRNvH2wtBxlL5PEqj7gF8vAvEkQPbBHbhlWVaakBZ-mReAvkGTclpCMCYiw3ZeRXNLutLQocw-Voc6H8YndAF-pcCqvwtotwJGu0TahLSIMhubExiyvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خایه‌کردن ترامپ از پرواز جنگنده‌های آمریکا در مراسم استقبال از رییس‌جمهور چین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107259" target="_blank">📅 19:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107258">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c567de51.mp4?token=YmOosK11KyD5VfecYZGDAKkpSFTkEh_6fzNiWMm-POTsfo-Aet2eJcq8AgVLbT0A835G_IbNEG8Tpml9I4s1bj26A5MCzTji79Y-vp52cSlIpwCHQE4Uxvs_Ytj3YotD8L_UhMZHhCj3d-AS5HuIhYLACEM13xFOiGrVlSplbwMVL_0W_9bEkfprS3MweHr9Xebub9LQpmEHG1XWpAWOAcwIXaF2kZJtmq5i_ap6D8GC-MywDbLhqKEEOa7kt2mm51Z3KEIuklQEea0cUyGDCsWuPdr6aAPXztXVYrSQdzqQZam3hDY_nssyt2wY96lLN7yBnaY-Q2U7k9qXWj4mTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c567de51.mp4?token=YmOosK11KyD5VfecYZGDAKkpSFTkEh_6fzNiWMm-POTsfo-Aet2eJcq8AgVLbT0A835G_IbNEG8Tpml9I4s1bj26A5MCzTji79Y-vp52cSlIpwCHQE4Uxvs_Ytj3YotD8L_UhMZHhCj3d-AS5HuIhYLACEM13xFOiGrVlSplbwMVL_0W_9bEkfprS3MweHr9Xebub9LQpmEHG1XWpAWOAcwIXaF2kZJtmq5i_ap6D8GC-MywDbLhqKEEOa7kt2mm51Z3KEIuklQEea0cUyGDCsWuPdr6aAPXztXVYrSQdzqQZam3hDY_nssyt2wY96lLN7yBnaY-Q2U7k9qXWj4mTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇳🇱
در بازی هلند-آلمان چه گذشت؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107258" target="_blank">📅 18:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107257">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eD8-Fq5E38O4d2Bv3r3ThQQQW0sfGPON_57ltvCTISQck5eqP6HXQy1jdU4C1CZUQuqRnVjdzNv8Uw4NrgvbL6ant-dXtWaJjUr6P8RErF16OYnUBiT9JDTXdxI7BtLrOhdzwmwHvnqX7FrqIVRfyEZKexion7UnywMoKEai3nDXavt1mcLALfk0DDoS26vRtTeFpdz1B3XzDA2rlRVWZTdguYyFwasNC-AkLGYb4360S5urFQKzkZbA2eJaExIUxo8rWxrUnu1Ro60kXNT22ObxEYrkft8qI4vmTn5fFMPPeq1K8mpt_Yw6ypq3C0NNclwMz3c77Cu7VOR0vNcV3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
پرسپولیس در دیداری تدارکاتی مقابل چادرملو با یک گل شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107257" target="_blank">📅 18:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107256">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68163d1ee3.mp4?token=XxHWjZO-g3WstJahD-gqnKdrDciJCIwTi2sgZVboP-yr3H5hzjX7ZPnfYIInkbx3lAcPEufcPXcIzE2iRG_I9ZGbhRsAEbHuaybTKxww8wazLYln20cXMUlFa53HWycCFxhzkma4idCA-XSTHyLvbLKwQ5tsdeUq1cQqKD2urfCxdqDICi8i5VBBvG2sS02sc7sJJA5GEI-NNI8jidKcElnF9tgKNb-OS9ROidOfEbZdYgnlXw1d4sycBHOEZSt-VggwMG328EfDPAzKgKVLK9ATkQXBU3qiSZEMlSVc5t_0RhPqsxhZZr-xkP9xjmwS-J7JUHIItleaEHaFqh2jkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68163d1ee3.mp4?token=XxHWjZO-g3WstJahD-gqnKdrDciJCIwTi2sgZVboP-yr3H5hzjX7ZPnfYIInkbx3lAcPEufcPXcIzE2iRG_I9ZGbhRsAEbHuaybTKxww8wazLYln20cXMUlFa53HWycCFxhzkma4idCA-XSTHyLvbLKwQ5tsdeUq1cQqKD2urfCxdqDICi8i5VBBvG2sS02sc7sJJA5GEI-NNI8jidKcElnF9tgKNb-OS9ROidOfEbZdYgnlXw1d4sycBHOEZSt-VggwMG328EfDPAzKgKVLK9ATkQXBU3qiSZEMlSVc5t_0RhPqsxhZZr-xkP9xjmwS-J7JUHIItleaEHaFqh2jkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
👀
واکنش رسول‌مجیدی به شکست عجیب روز گذشته تیم‌ملی ایران در مقابل ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107256" target="_blank">📅 17:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107255">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107255" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107255" target="_blank">📅 17:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107254">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RF6wYIESPVtlfao3lQDb5uzuMWU14rAxLscTWao6ffhUAAClm2IpqyxNSMr7PoyHq9Sxg3f87rsMp_ae0fKxF8sxUaVRy46iWGZy6hADj8XLi031UFjm5VL0X9gWxXQ8CCov06yMUa1k_WIGcJ6CXkDzqBwsbkXKVKS2No2zT4FKTPZYT9tA9yVSjQBbU5vNTafxM-PwyXhczVYHNmJtlRB3PkEPlhpCVNmUFVye0YPQcI-RbIwbYfUOJNDxZ0zuF8cyRO2JQxDTP7fRvFJ8q4p5PE5zf7fvTKzaB4VcRY9-UEOOyyZgzttPZWPtYybLJb39oM1voSXcumEUfEzYrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز فرانسه
🆚
ترکیه
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ شکست و ۱۲ گل زده
ترکیه: ۳ برد، ۲ شکست و ۹ کل زده
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107254" target="_blank">📅 17:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107253">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
🇮🇷
اشتباه عجیب مریم‌یکتایی گلر بانوان استقلال در بازی مقابل خاتون‌بم که‌دروازه‌اش باز شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107253" target="_blank">📅 17:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107252">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-WnjwF2_ZNs3LGFdVeJYwkGgMa9r9dLXrON9UoVQont1ohISmmcfhvW3O21sKujwe01Mc60LnDGCY4Cp6nGXMOoQQE3JVk9nJxq1LnvqyQbzmUlBiJT7KVEenkDqfNKYIni7nr7gN1NKLJT_wFNhAri3_XibrX7dqsXojeGAOk1f65EvNstzeXSfDx71hiQ0P4nh0RMdUyJD7CoTnieq-U6JV8iam5yHZvnR8YkI4Q4FkjNJjUar93Os0gUopDyH4072l_vxKxqUGYRn8HVYCSc2uY_L2Yz2VNMHIZCBzjwG4Kh7ns4tZXCJNqJydvaigHKcY37oTmGQrQEBxP5Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتین: درحال حاضر جریمه کسر امتیاز محتمل‌ترین سناریو است. در صورت شدت این موضوع، ممکن است حکم سقوط سیتیزن‌ها نیز صادر شود!
⛔
🔺
سناریوهای احتمالی برای سیتیزن‌ها:
🔺
❌
توبیخ و جریمه مالی.
🔺
❌
کسر امتیاز از منچسترسیتی.
🔺
❌
کسر امتیاز + سلب جام‌های…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107252" target="_blank">📅 17:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107251">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gfi_Ldo4AOWVgyXZc1S8zPH422R6pQrMpw2U2KON2jnBoVhv-ALG-BgLAQ2lgekqFaJ17NR4VpNT2jBpIcM3Q9K2CsW9PptIox-DrPl0LECn6mdMu8GkUx5WmLEWHNGvknlxYfKbUH7qcbn1nDtaHBrbHeFY9Fb1XiBeulr-Xc9hNGOP-fql2YYAk1d3SClVlelPPvjsZKKPZOnXu_NHmVtGYSKnGQtrCnNBRoZTdypzaLVnSeF2SOT0muTmcu3VvP0wEtK3C2rYoaY2q6rISU2E4z-MqW5Rr0gpXsLcvGnZ3YPdWKxdiqE9f0dGK4ui6QK0aQJSHqdawld0kfLwUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
منچسترسیتی در پرونده ۱۱۵ اتهام مالی مقصر شناخته شد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از اورنشتین، منچستر سیتی تقریباً در تمامی موارد اتهامی مربوط به نقض مقررات مالی لیگ برتر انگلیس مقصر شناخته شد. انتظار می‌رود این باشگاه به حکم صادره از سوی کمیسیون مستقل اعتراض کند. هنوز…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107251" target="_blank">📅 17:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107250">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYVhT39qLyP235PyVxX5owI2pgeqteMqfmHbh-XdemZvYO_bMDFMSoZ-tKiwAmD7j1eoN58zCDuiFVSGKv4O38NUPJZmFLsBE_fe3L85hLH5pWlPil3ZVL3sTVeJr20ezoTfmcqTdgv3sXbCeV9PuQVvjWXEaW-kpwoKtI6UmnhGj9hr9kiTG_yJFLB6lsGjRnS3P9W_61wPpigSfXgme0hDvIERdLCjbpB6z4DRjliro_rWIQ8YcwWWCujQRPoNeDTJb8Yi5YywtsPKwb4LAdHqaJZ0kMcVpVQlu1-kFmlvviUP45C5HMufS-uRMURF8gcAX0hSgJXUxzpkhV4vdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
منچسترسیتی در پرونده ۱۱۵ اتهام مالی مقصر شناخته شد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از اورنشتین، منچستر سیتی تقریباً در تمامی موارد اتهامی مربوط به نقض مقررات مالی لیگ برتر انگلیس مقصر شناخته شد. انتظار می‌رود این باشگاه به حکم صادره از سوی کمیسیون مستقل اعتراض کند. هنوز در مورد تحریم‌ها تصمیمی گرفته نشده و روند رسیدگی ادامه دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107250" target="_blank">📅 17:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107249">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638e170672.mp4?token=RHZqRQ1TvguqrwThT7H0Qf3AU3nDG7fRi8_1Dl3iKrUS2ubb4nq5Q2UV0CRisCRbfWxfRTc1p4OSQvP6z_Cjo5Kdlu1ZnRtSfsbraM6PhML6gzBCzG8QWOp9RLGV47UnsYXWecwM2vm5zVHGvq-VKlp5CF-gCwJPmpcl4L52AKbs5ZPcCODuydBm4ann6qTvEfBNxqH-vXBiP8odroP8ePTaOpja5lAn2dqpaQk1UbpGUPfALfodaDpb3lpX0R19hhorP0B6poVk4-cWCOBxAO2YqEMkMfo-evvZ7T84pMADdBdnfZaDI9aMBFTp6eTkZ2350A0F5-pq-O9lYpSl-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638e170672.mp4?token=RHZqRQ1TvguqrwThT7H0Qf3AU3nDG7fRi8_1Dl3iKrUS2ubb4nq5Q2UV0CRisCRbfWxfRTc1p4OSQvP6z_Cjo5Kdlu1ZnRtSfsbraM6PhML6gzBCzG8QWOp9RLGV47UnsYXWecwM2vm5zVHGvq-VKlp5CF-gCwJPmpcl4L52AKbs5ZPcCODuydBm4ann6qTvEfBNxqH-vXBiP8odroP8ePTaOpja5lAn2dqpaQk1UbpGUPfALfodaDpb3lpX0R19hhorP0B6poVk4-cWCOBxAO2YqEMkMfo-evvZ7T84pMADdBdnfZaDI9aMBFTp6eTkZ2350A0F5-pq-O9lYpSl-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
هادی چوپان: من حکومتی نیستم هنوز فکر میکنم دارم خواب می‌بینم؛ وطن‌پرستی دلیل حکومتی بودن نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107249" target="_blank">📅 16:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107248">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e4e43dca.mp4?token=dn1Qn1oSNc2RcjL1rHTN_2ncFywQhRtO23Ml2f-Q88FIDyXvPwzxzMi57wnteS8OiErnJLisHBAilEwkxmG8GUhJ3Bj5zIKNQAqgrXdZBRM3Zp6vnHrCknmIAUVBWplSTS1DTc_BRnfxIYjDpZWsDlj61Mm2adqUTpGM-nHoOHyJt4oPDDTyZwmPwFRmS2nNpmFWV7LKicBVrIgwFoEAAPUNTWSOgNAYr3Ft9mtbXy7vjXtYjj3OnK6eX_204b6v_0mXTcDGOfR2O1A2tsr5ZobJs1cTbiCK05SC-8QY_W7Ji-U626Hfun2P2aWyvK8V5EseURobsBLm0OL6BgUZGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e4e43dca.mp4?token=dn1Qn1oSNc2RcjL1rHTN_2ncFywQhRtO23Ml2f-Q88FIDyXvPwzxzMi57wnteS8OiErnJLisHBAilEwkxmG8GUhJ3Bj5zIKNQAqgrXdZBRM3Zp6vnHrCknmIAUVBWplSTS1DTc_BRnfxIYjDpZWsDlj61Mm2adqUTpGM-nHoOHyJt4oPDDTyZwmPwFRmS2nNpmFWV7LKicBVrIgwFoEAAPUNTWSOgNAYr3Ft9mtbXy7vjXtYjj3OnK6eX_204b6v_0mXTcDGOfR2O1A2tsr5ZobJs1cTbiCK05SC-8QY_W7Ji-U626Hfun2P2aWyvK8V5EseURobsBLm0OL6BgUZGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇪🇸
عادل فردوسی‌پور: کاش زلاتان ابراهیموویچ یه روزی برای تیم دیگو سیمئونه فوتبال بازی می‌کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107248" target="_blank">📅 16:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107247">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c917893c10.mp4?token=dty5e1tlcJU_bX1udsagGTOoGWS6Apb5q7ofBq75erx9kmCsVk_xBWWeGpZtCT8qu_KdfagPozx94JoXuDVcnf2ZQsAHzGk9pHz35RUIR5h3OevymGu97NBcCQKanGmwsi_bS0msCzW2YXvzu8Iv7RifMcQ2QbGE5H8J4UCbfuQ0nSKZ8ffPOqL5ykvUffrigSAKVXbiay6VgZ0w7xh0AV3SVIogbXGUo4tYhkggYv5KWfJ1SRStDhiydDaJ2ydlHpqTcjllEQ3PL6EdlpX_NE6auZdq9LRW9WEEbJqHiOPDKPM0r3cBte6QkGjz8dQ-rpAcOZCwvO-uUnZG0fPZLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c917893c10.mp4?token=dty5e1tlcJU_bX1udsagGTOoGWS6Apb5q7ofBq75erx9kmCsVk_xBWWeGpZtCT8qu_KdfagPozx94JoXuDVcnf2ZQsAHzGk9pHz35RUIR5h3OevymGu97NBcCQKanGmwsi_bS0msCzW2YXvzu8Iv7RifMcQ2QbGE5H8J4UCbfuQ0nSKZ8ffPOqL5ykvUffrigSAKVXbiay6VgZ0w7xh0AV3SVIogbXGUo4tYhkggYv5KWfJ1SRStDhiydDaJ2ydlHpqTcjllEQ3PL6EdlpX_NE6auZdq9LRW9WEEbJqHiOPDKPM0r3cBte6QkGjz8dQ-rpAcOZCwvO-uUnZG0fPZLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
🇪🇸
صحبت‌های شنیدنی رودری درباره تفاوت‌های اساسی فلیک‌ و پپ‌گواردیولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107247" target="_blank">📅 16:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107246">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6854f7f8.mp4?token=jFoDWJXL0FM-XVEvuOq4BJl2391lJdKZtCzuaOH5_pSl7AUepZ8xf1KKqFfNABk3NiYgyqQjkNPfg_pz2koJHWLCHFn8Cw9IQZ-4fiR0Tc_hrdIEXoB5UubEkYwJwGeyHPtzCMTXm5_WFJGW5BjxXsicynWmy0ZizndsFyO2h_yBs14K2N_DDedCtCkbKbotwcamodlmFjZX5qE-WbzWqvwai0Uzs9GXZrf8RMfh7tP-0QLNSUMB110LbEexV9V0Wc4rPVp1gmSfmt-tJz8J8U7VDz2Y2xWfnqvlRUBk1mXJBshAq6gaZNkud48SpKqzuOskW6TqNYSNVb1w87IqMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6854f7f8.mp4?token=jFoDWJXL0FM-XVEvuOq4BJl2391lJdKZtCzuaOH5_pSl7AUepZ8xf1KKqFfNABk3NiYgyqQjkNPfg_pz2koJHWLCHFn8Cw9IQZ-4fiR0Tc_hrdIEXoB5UubEkYwJwGeyHPtzCMTXm5_WFJGW5BjxXsicynWmy0ZizndsFyO2h_yBs14K2N_DDedCtCkbKbotwcamodlmFjZX5qE-WbzWqvwai0Uzs9GXZrf8RMfh7tP-0QLNSUMB110LbEexV9V0Wc4rPVp1gmSfmt-tJz8J8U7VDz2Y2xWfnqvlRUBk1mXJBshAq6gaZNkud48SpKqzuOskW6TqNYSNVb1w87IqMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو آندره‌اونانا گلر ترابوزان‌اسپور از روزهای خودش در فیفادی؛ معلوم نیست چه غلطی‌میکنه
🥸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107246" target="_blank">📅 15:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107245">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d52babf07.mp4?token=PehI9nBshgpeVLBGdZDbCSL3cBxhNfudZwS-wHYYKdS5kRK0Jyl6KTy9CMNk_CddE8LwPZk2fxoZwDUgva819Xr0XHJv_rJ5DeeOyh7V2_Pw_BlvyrIteHFiB0AcaIIoJBfeDfRsQTaeyDRHDQZegY8lvC7qivsywbQzWZMgIy_QwNOukmoaH48vsUp1ZO0txJJbfT6wsJM7kHFggeYEsK8_SXnUkT3EHeyvKH2VhSMNH0T1zrTmX5TD_b-OuxgpYcI-wHOdXxV3_dtrSaNz4R-9UM5140ghEqZQPQmcPPRl8JiZ3HiGikvakoKHWFqRUXQB49EQJVREe-elAH12Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d52babf07.mp4?token=PehI9nBshgpeVLBGdZDbCSL3cBxhNfudZwS-wHYYKdS5kRK0Jyl6KTy9CMNk_CddE8LwPZk2fxoZwDUgva819Xr0XHJv_rJ5DeeOyh7V2_Pw_BlvyrIteHFiB0AcaIIoJBfeDfRsQTaeyDRHDQZegY8lvC7qivsywbQzWZMgIy_QwNOukmoaH48vsUp1ZO0txJJbfT6wsJM7kHFggeYEsK8_SXnUkT3EHeyvKH2VhSMNH0T1zrTmX5TD_b-OuxgpYcI-wHOdXxV3_dtrSaNz4R-9UM5140ghEqZQPQmcPPRl8JiZ3HiGikvakoKHWFqRUXQB49EQJVREe-elAH12Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
گل‌خوشکل سون‌هیونگ‌مین مقابل اکوادور که تنها با یک‌گل دیگر به بهترین گلزن تاریخ کره تبدیل میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107245" target="_blank">📅 15:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107244">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22947aa27d.mp4?token=quu8Ugats36v_iWWVrXwVsfeVLB8DoyS7o6a4555q-UGpFm8nwt3Yb5FECEQMdYyVdcfLFlqDhwuks603aXcpCOHOm6eBAboMr95bGkLpcuZMTg78QZpYHKFew7QeOcF8zY-Ggz2K6avOh89W-b1uh2DlJ3dJqloyE4whObjPvfwJsdue3WN-49wS1SWhf6C9cu0i97p0o_m6La3oBvGCum-jbmcdrRtAvj1j57BOzlz7beM7rkgpnqbSXIgMCu7u2bI5qjXyXUDy5TIaAA3oDS5VUMLvauq3JrCL7SMQ2pjmWjkwAWsNC-VcGPsGe2Fj3dgL50OVNdjpLimz69QPx2uWIih0wApmriaylEOAiMH0h1NgV1b-fMJQWas-aVq0xKYbOyIYTqbHjA7OjPi9Rfp6t04iwY7JNLJOatmjVzSUIqI820OP47axt2r8MhsOK3g8uzsy0_BUNXtDu6UDQo7FQakn-_KbQ34aCE8Z_e_6m2R7rZ4qiae22oQoMQqbKq8wMNm3ujfc_gl48WADK1nYu1dzr8eX9hTDaWkv75jmp3vrm35Pdxx5A1NJvhciVhkNObZnCp8Pks84TsbldPLF8g7VdqCf878vorE73peNsXX-HQafleX-O17YEv_e4kfdRtcnJNwXA-WfnCfA4mVSbdUUnhQ8QSmGsidVhE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22947aa27d.mp4?token=quu8Ugats36v_iWWVrXwVsfeVLB8DoyS7o6a4555q-UGpFm8nwt3Yb5FECEQMdYyVdcfLFlqDhwuks603aXcpCOHOm6eBAboMr95bGkLpcuZMTg78QZpYHKFew7QeOcF8zY-Ggz2K6avOh89W-b1uh2DlJ3dJqloyE4whObjPvfwJsdue3WN-49wS1SWhf6C9cu0i97p0o_m6La3oBvGCum-jbmcdrRtAvj1j57BOzlz7beM7rkgpnqbSXIgMCu7u2bI5qjXyXUDy5TIaAA3oDS5VUMLvauq3JrCL7SMQ2pjmWjkwAWsNC-VcGPsGe2Fj3dgL50OVNdjpLimz69QPx2uWIih0wApmriaylEOAiMH0h1NgV1b-fMJQWas-aVq0xKYbOyIYTqbHjA7OjPi9Rfp6t04iwY7JNLJOatmjVzSUIqI820OP47axt2r8MhsOK3g8uzsy0_BUNXtDu6UDQo7FQakn-_KbQ34aCE8Z_e_6m2R7rZ4qiae22oQoMQqbKq8wMNm3ujfc_gl48WADK1nYu1dzr8eX9hTDaWkv75jmp3vrm35Pdxx5A1NJvhciVhkNObZnCp8Pks84TsbldPLF8g7VdqCf878vorE73peNsXX-HQafleX-O17YEv_e4kfdRtcnJNwXA-WfnCfA4mVSbdUUnhQ8QSmGsidVhE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
صحبت‌های جنجالی هادی‌چوپان درباره جاویدنام مسعود ذات پرور: منو شیر شاه، سلطان و شاه خطاب میکرد! عکس منو از باشگاه ها پایین میکشن؛ ولی من بخیل نیستم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107244" target="_blank">📅 14:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107243">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e55638e04.mp4?token=vFdDOMgXbaZOlkKUB8k8oXb4dG6iD2S16CmWZY-aO3UzxpQYuvtQXuejgaMT8kumnzw7iLg_VOj4Ii3GvuHCyiaYkBxhw2zwJjryaXnTdQmYdoRHG3xyXygsOHrHlDliI4uVFSKG-D-6OWxS8bcdTNQ0VD1tzg52Q_8hMwNTUgDkMFcjVYvZ14NnUZfrqJtDZp3NczZqq-itRo2JldsqycVfeDZxeww340S4T88LEr6k5ChL6obgbgbsJHN_6ktGO8MXrhjKHDDAt4JD3t1eSsAC4iABOIjQ5vcDDj8nIxxWydmOorNwnWvDjooKFWb_r8IRbLhFd3c21YKVjWl94yC0zs4hhNYHIjUcTIAafhn-e-fLKQFhawUCyJW-SKz6cRaqvmV2F1NnniiogjDiHBRmuBzosld-a8ohyR_xzBXjx7jPSGJeKAU7viWGcvh-zeAyAfcPoZ0a--ccaMGQL-A27VlZI9X_GDqKK_uK8CSWskCWOT0-ihUkHhUh4kqv0c7uEMm_VJX6Wb9YP-794SsDSjgTfXNPgwZerpUBZ2hs8RLTdoG6h8X7pzwtYWM4cR-YnDVLTkPml4Fs8NZlVBNInLm52TugnXQvJRLnW13KhcyAwxbRH3dhHnu2RTLti9MabRNSoLUufE5IjJNRvXvnwM8qCSXLkPRshO1mpN4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e55638e04.mp4?token=vFdDOMgXbaZOlkKUB8k8oXb4dG6iD2S16CmWZY-aO3UzxpQYuvtQXuejgaMT8kumnzw7iLg_VOj4Ii3GvuHCyiaYkBxhw2zwJjryaXnTdQmYdoRHG3xyXygsOHrHlDliI4uVFSKG-D-6OWxS8bcdTNQ0VD1tzg52Q_8hMwNTUgDkMFcjVYvZ14NnUZfrqJtDZp3NczZqq-itRo2JldsqycVfeDZxeww340S4T88LEr6k5ChL6obgbgbsJHN_6ktGO8MXrhjKHDDAt4JD3t1eSsAC4iABOIjQ5vcDDj8nIxxWydmOorNwnWvDjooKFWb_r8IRbLhFd3c21YKVjWl94yC0zs4hhNYHIjUcTIAafhn-e-fLKQFhawUCyJW-SKz6cRaqvmV2F1NnniiogjDiHBRmuBzosld-a8ohyR_xzBXjx7jPSGJeKAU7viWGcvh-zeAyAfcPoZ0a--ccaMGQL-A27VlZI9X_GDqKK_uK8CSWskCWOT0-ihUkHhUh4kqv0c7uEMm_VJX6Wb9YP-794SsDSjgTfXNPgwZerpUBZ2hs8RLTdoG6h8X7pzwtYWM4cR-YnDVLTkPml4Fs8NZlVBNInLm52TugnXQvJRLnW13KhcyAwxbRH3dhHnu2RTLti9MabRNSoLUufE5IjJNRvXvnwM8qCSXLkPRshO1mpN4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
به‌مناسبت بازگشت زیدان به فرانسه یادی‌کنیم از این عملکرد تاریخی اسطوره مقابل برزیل در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107243" target="_blank">📅 14:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107242">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🎙
👍
احمدزاده سرمربی سابق ملوان از کمک‌های اسطوره احمدرضا عابدزاده می‌گوید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107242" target="_blank">📅 14:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107241">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f13d64d651.mp4?token=fTCJCXw0uNBpLpLnxbLLbHwPTUPOvLKIE_-yCV_R7xiTXxvfHSwHyslserux_k68Vae_LCqlSaX30mpbu1gnbSEL4oAWINpuepn2z9fuuNFMPk6iYub7kA6iwvvb2PY9oU-konMBSORH1zcgKFwqXY1IDO04k2nsY0g_lHiPTDhUZbpI7b7kGuqNhNXy0wswh34HZx5oWkupyX6Ho8Fxu1YMdeRb60FapSmgVeBz8iypNiZq-43XMFVsk62pcqmArMPR5zH1YcW01XQqRaAKCe0cFtfH3u4FNwg7BlQ1orHMT5-drcxmUpT48_uPElEunLF9HXCgu98FwXU2rFhnxml613aw4wyKWXmI0iJ8tQOIjm4dFeNGGNCi7QrQRKwLbKWleXhoIl9HYItVQCEOgMoREkvKJM-a6bE5rIUms-oEw51B7n9clXGgi9IBjMtyl4EgMPsPdsdjmVZaz74GUvgkDXZchBSygHT5XtR-2QExAgfO6SyXsiuQQUGVB5SL3Z_fjYYSjKadEA-p8Q0a-lmwtIowE_hiUn37Uwp4FfgZ7zUS5gCddXFr3MvpMlDACjOxZMvM4j2OF9CFQfboYnKxKWeMCRzzbKh2TuIKywKhi_hTe8Ta-ra8sHVqNdOPne2N20X1N_t9NMVIr5ficrK5YTi1Dn0VGGEOINpKwFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f13d64d651.mp4?token=fTCJCXw0uNBpLpLnxbLLbHwPTUPOvLKIE_-yCV_R7xiTXxvfHSwHyslserux_k68Vae_LCqlSaX30mpbu1gnbSEL4oAWINpuepn2z9fuuNFMPk6iYub7kA6iwvvb2PY9oU-konMBSORH1zcgKFwqXY1IDO04k2nsY0g_lHiPTDhUZbpI7b7kGuqNhNXy0wswh34HZx5oWkupyX6Ho8Fxu1YMdeRb60FapSmgVeBz8iypNiZq-43XMFVsk62pcqmArMPR5zH1YcW01XQqRaAKCe0cFtfH3u4FNwg7BlQ1orHMT5-drcxmUpT48_uPElEunLF9HXCgu98FwXU2rFhnxml613aw4wyKWXmI0iJ8tQOIjm4dFeNGGNCi7QrQRKwLbKWleXhoIl9HYItVQCEOgMoREkvKJM-a6bE5rIUms-oEw51B7n9clXGgi9IBjMtyl4EgMPsPdsdjmVZaz74GUvgkDXZchBSygHT5XtR-2QExAgfO6SyXsiuQQUGVB5SL3Z_fjYYSjKadEA-p8Q0a-lmwtIowE_hiUn37Uwp4FfgZ7zUS5gCddXFr3MvpMlDACjOxZMvM4j2OF9CFQfboYnKxKWeMCRzzbKh2TuIKywKhi_hTe8Ta-ra8sHVqNdOPne2N20X1N_t9NMVIr5ficrK5YTi1Dn0VGGEOINpKwFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اولین‌گزارش نیما‌تاجیک پس از ترک صداوسیما و پیوستن به پلتفرم اینترنتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107241" target="_blank">📅 13:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107240">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e9fe0aa9.mp4?token=pYPaFElIUCv02PA2q4gfGsEpxeWTKtZIFVAFTxIv-D8KczUZulIKG-krgyelL-CKrmE4CJw820y-SXmO3t8puny7CIyCzEfalMtuMulEj5XRfz0pDq0nxWsjELRjeWkVV-w5vBUWRyBbweLSIlvHTNy6mSMHjwRoqLDY_Gf7zOrVMIR2QVNKGpXaimxTpumY7Tyurgxwyz6t6ql2AbcLx_a-nbAdOBQeNWXh9IY9Z8fjrFZ1RB-gvcnie9PuxFXEQogwUJaLot8IfLJuRm22x7HjKzzQ_1BBEM0As2kLY7UNbR3lWBiqoM2-oUoenbWuGHatPmzHVP3adrVf2w7WCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e9fe0aa9.mp4?token=pYPaFElIUCv02PA2q4gfGsEpxeWTKtZIFVAFTxIv-D8KczUZulIKG-krgyelL-CKrmE4CJw820y-SXmO3t8puny7CIyCzEfalMtuMulEj5XRfz0pDq0nxWsjELRjeWkVV-w5vBUWRyBbweLSIlvHTNy6mSMHjwRoqLDY_Gf7zOrVMIR2QVNKGpXaimxTpumY7Tyurgxwyz6t6ql2AbcLx_a-nbAdOBQeNWXh9IY9Z8fjrFZ1RB-gvcnie9PuxFXEQogwUJaLot8IfLJuRm22x7HjKzzQ_1BBEM0As2kLY7UNbR3lWBiqoM2-oUoenbWuGHatPmzHVP3adrVf2w7WCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
رد رشوه میلیونی برای امتیاز دادن به استقلال
🔻
اتفاقات هفته آخر فصل ۸۱-۸۰ لیگ برتر؛ قهرمانی پرسپولیس بعد از شکست باورنکردنی استقلال به ملوانِ محمد احمدزاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107240" target="_blank">📅 13:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107237">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/czdKoh4iO_hWcMEPRPb_Pd7VM2K58Q8ItTjwVk_Zi9seIHcO8bjBIDWVZYJb7zLm-i6UplrtIoUTKFBzkEa8M2FEBU5kAFX1xMrkpH8Nlx1U6GVWy8XBRay9GiXK9atd8bt1N4P9Vkei9XdjYbvb2iHO2wEGR-lBkoSDzBURfJ1QxhMZ6d5RaAphzLqerBR_NH85bS8MWoo8pxAwT1uIuGZyS-1UJtGqwhVw93uqOduhdGHzriUiIgWGZUviFgYsPtfr6p9xTAJxPqAABpNl4ZyXXS6Fjo6gxr7mCHkzNscO0LRXqhDqasECa8Et1MIsW120PhU0ojOWTqDUpvrvlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/asRs9rtoR-B6m47poPp51J3Pw3-LxmAgWlWALy_EqKAG_JV07bRLuACfMnQWGNG4A9-RBaMbXFcaM5jqnqsWWkkYH-wkNaUnYkgczEAdcFvwK4IR48Ck5mDiFP7uOhuDDLO_fUbRYXrHcMbuYwnSrcJjs5hy7X1KBRm_OWzAYkMkOSMglmYs6odc8_cFj5yxI0Q5AH9b5b2hbGpBsqOWEk1QTCgadKIB5G8qse40woW5RNwiQufncRD5FtTza5I79rYWY1HHPlNJiJVLioOjAj94L1U8Rf0vYByCQXI1yN6urXrF7t457HuU7laTdpngOyqKd1J91NZ9AVQ-kG2nJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tucv7ujiQeEafrVQeLUOrmJp3RTkhH8G4EGEh64acRxfN8DN5IdKTDGoklVuXwZT9ik3OdZiSYMzdxv7Wg6tSJRPlW3YFt_t9JYnJSFyvDXgPQaiRXE-RzABOW5Owca1jWqpsv-kXTfqKE2U0sqf6R8j2_ZzKJtbAYyU1Ho5n2ko18CJu-vAx5PO_Kt4Je5JTKjnGxd_JDQTGpXXwPB-lEgnDRjvk6_XbptcCqfZFB8wPoTwOSUxHvRFWhh4Ho_FT-VKky5ovx8LSdVbcVFSpwdtM6kBr1KP7WgrQsA_wj4gF8zlHBiPQS6tXsICr8ulqOkc4JrgW65hQ-Pz2713Xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🐐
🇦🇷
تصاویر اسطوره لیونل‌مسی در آخرین جلسه عکاسی با تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107237" target="_blank">📅 12:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107236">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-GfXvOmnzvEaGUzcUn5bsF1FJZbc4Gv6qC5Z2Ye5YdG34xd8hCI1BDXKN48RZEmfwUDUashyBiIsWnhSpTK48ZCM3eQtMKcS7I8tYN_PCVSRmHFtBbl19_YLLnu2LWw7EpkTqNp_TQoNojZUhL4P0aALk6QG5Eelx-SNYqO40K5qHBCTmHlaTMZ30i0-hm_K0EBzfU3WboSfGglimQEIXwMU4wjtcUINc7qgqG-MO0aPAbXg3F_MvM7N-jglxyquJAW7Wpnj-Ud7eOeQmuWXNY1zaA_ZCIpbsNV51uVkbIJVGn3HNHNVivBTiN0sNPcc2SodwMwjTsGiqVacuJt_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
ترکیب‌رسمی برزیل مقابل استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107236" target="_blank">📅 12:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107235">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d91b2fef.mp4?token=P-3pviqWVGsGpmeYdAwsz-hunAXBwzR_lG0q0SZfCm6Il7tGUkhTcHriPT9x-iACP_WwXgiuA9dq_hqQCh8l_Z2U4mJin8lYhFPsfZLLzA-eePUSS_XdARgxsHTfdBFS5pxHFp7fvXaJO3dw6Mn1k3HVPfiWALJnDdQAkFRgbkjhMyjLA3_Qq_tA-nDdXcbz1ozMfEGMDmwoE_TL9JIpMisygAuHlmON0XDL63i0JCqPP7J1Qm_XK4wVejmBiK_Xfe0tQAcQPPk3eMMyNRPN5LsjaKYxJH8thBA8kE9hs0CXh_hFnoYCYlxJnDVYCbxvgzEVw6ARh6KApikX4BdPScABjcvBA8PEDpbsnwSH3M_Qa14NQut4JJcx3MOyfOZ-YiUFJFtQmzou-TnQbQAW0snZ6DLdYSV5gAZCq8qyp6eUBmiyiyXSWOqKwCWyFk76VDyUHCESx0hnnhNdWdcMqbnwnfoZ63yILtfWBcft2cqpqizrj8YTcEEM-x3j8Zzkni-i9SjIy4iSE4s2xSUm_K1-iLg7JNJuewoVZzWFrKnP1BzJi9suEYs_PXuVASsKaHecV2g_cQL8yGBd9IioUGUd92E_QwDw0Bn8b3CDb_0TOP9ZHD0l_R7UHDOvwkfHxbOxa9BR7V2kUpLLPjmL8tfZfGGhQ5uEoUPr3frPcLE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d91b2fef.mp4?token=P-3pviqWVGsGpmeYdAwsz-hunAXBwzR_lG0q0SZfCm6Il7tGUkhTcHriPT9x-iACP_WwXgiuA9dq_hqQCh8l_Z2U4mJin8lYhFPsfZLLzA-eePUSS_XdARgxsHTfdBFS5pxHFp7fvXaJO3dw6Mn1k3HVPfiWALJnDdQAkFRgbkjhMyjLA3_Qq_tA-nDdXcbz1ozMfEGMDmwoE_TL9JIpMisygAuHlmON0XDL63i0JCqPP7J1Qm_XK4wVejmBiK_Xfe0tQAcQPPk3eMMyNRPN5LsjaKYxJH8thBA8kE9hs0CXh_hFnoYCYlxJnDVYCbxvgzEVw6ARh6KApikX4BdPScABjcvBA8PEDpbsnwSH3M_Qa14NQut4JJcx3MOyfOZ-YiUFJFtQmzou-TnQbQAW0snZ6DLdYSV5gAZCq8qyp6eUBmiyiyXSWOqKwCWyFk76VDyUHCESx0hnnhNdWdcMqbnwnfoZ63yILtfWBcft2cqpqizrj8YTcEEM-x3j8Zzkni-i9SjIy4iSE4s2xSUm_K1-iLg7JNJuewoVZzWFrKnP1BzJi9suEYs_PXuVASsKaHecV2g_cQL8yGBd9IioUGUd92E_QwDw0Bn8b3CDb_0TOP9ZHD0l_R7UHDOvwkfHxbOxa9BR7V2kUpLLPjmL8tfZfGGhQ5uEoUPr3frPcLE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دلیل عدم دعوت مهدی قایدی به تیم ملی؛ ناراحتی قلعه نویی از عدم واکنش قایدی به صحبت‌های یک مجری در یک گفت و گوی تلویزیونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107235" target="_blank">📅 12:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107234">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f256fb52d3.mp4?token=o8avFQGYConjEYwL8zFhQPV7E9LLG1JLpJpg7h84k035B_0IQ_Nr4kOUTvW-_HhiZ-PzMOfm66182Pb0HYUcs5lCWNtkgn41TTUSkujq_TJjKs8xEgjEIMsqi1jhrDPo9YK6UzNFHtOyDM-fqGIuE-8Y_UZ5BZecNIyfMADaydkcYncAq_SeVjLcDZDzGKS6wj-xrMEbqPHmtU8tir18QFzyEs_TQXPlyyqn20EgCvaLoZeTVRgcTFGb9jyw9wfB_LL35f_BR5Nx6VqoiE-KSyNa63OWnE_NB0vARUpRZdqJM_8Eu-8khhWwz1XU6BDGwXAVyI7nTr3DOBGu-ivBLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f256fb52d3.mp4?token=o8avFQGYConjEYwL8zFhQPV7E9LLG1JLpJpg7h84k035B_0IQ_Nr4kOUTvW-_HhiZ-PzMOfm66182Pb0HYUcs5lCWNtkgn41TTUSkujq_TJjKs8xEgjEIMsqi1jhrDPo9YK6UzNFHtOyDM-fqGIuE-8Y_UZ5BZecNIyfMADaydkcYncAq_SeVjLcDZDzGKS6wj-xrMEbqPHmtU8tir18QFzyEs_TQXPlyyqn20EgCvaLoZeTVRgcTFGb9jyw9wfB_LL35f_BR5Nx6VqoiE-KSyNa63OWnE_NB0vARUpRZdqJM_8Eu-8khhWwz1XU6BDGwXAVyI7nTr3DOBGu-ivBLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
درگیری با عارف آقاسی و تهدید سامان فلاح؛ دلیل دعوت نشدن کنعانی‌زادگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107234" target="_blank">📅 12:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107233">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107233" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107233" target="_blank">📅 12:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107232">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0S-iVjcLp3Lc2sBB2p4BVfETT-dxJS9wPGetUkbT2DWVqnDzMZR82hUIpUQN_9L0A3FemT2dLhUT1QgsCIeZd0rBeg3gqA3YTnkA_Kr9x4fZo37AY_b0BV33MnPDwxPoTF-J1_QORCKZBcJq_w5zkNKa4-SZvbysoTW9D2Nq4_pEmW1xtRVkr-TYf_OCGcEtqK1vESZSl_5L0MhIRQA91rQJfSGvG-o6x0PyIn3POhzkyMjyDhSwMkaR_DSSSxsfNn1LJQIRqqpf2pcwpfNuM_B8kdteW9vrGo-vO7cGkA0zwOtVM6u78dDLWzyVh7MsYOXPBY9CR3_uodYGNkJ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
ایتالیا
فرانسه
🆚
ترکیه
برزیل
🆚
استرالیا
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107232" target="_blank">📅 12:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107231">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=OUq0fzezo1U-aPr4gfiim5DkbyyEfFQFj_-2ApDBGd_ySTCpzGnRZ0enI1jDSgWh0WTz1obon7oF9V4cRUpdrEQupBFhLYAt60q-RNsbol0hLKMC6AwIf-zbo73hDI_xFUykMbr1lD-eWsCNT_-F0CkWx9ozySYvTrlrNPolRBASItbdI7ykQKB3Qibbt3FRh5yA6Zk4FeG7mzfiVrMRdMYz26TsM7dprHyaviT7qx8GYVJ3g1iItBWG6mqWLA3zP-36rvUp_8xKQArmr2kwOxe599ycUI5sirbZfYHQb0KD0R9wkkVMyGOa0ErlaOHNbpsChYLwV8BtFpNvpZertQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=OUq0fzezo1U-aPr4gfiim5DkbyyEfFQFj_-2ApDBGd_ySTCpzGnRZ0enI1jDSgWh0WTz1obon7oF9V4cRUpdrEQupBFhLYAt60q-RNsbol0hLKMC6AwIf-zbo73hDI_xFUykMbr1lD-eWsCNT_-F0CkWx9ozySYvTrlrNPolRBASItbdI7ykQKB3Qibbt3FRh5yA6Zk4FeG7mzfiVrMRdMYz26TsM7dprHyaviT7qx8GYVJ3g1iItBWG6mqWLA3zP-36rvUp_8xKQArmr2kwOxe599ycUI5sirbZfYHQb0KD0R9wkkVMyGOa0ErlaOHNbpsChYLwV8BtFpNvpZertQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🟥
بازیکن تیم‌ملی اسرائیل دیشب بخاطر این شادی بعد گل مقابل اتریش با کارت قرمز اخراج شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107231" target="_blank">📅 12:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107230">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
بهانه‌‌های عجیب حسین‌عبدی در بدو ورود به تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107230" target="_blank">📅 11:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107229">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e764af88a2.mp4?token=Pi588B9euAOmqP8wkQ5_XHGZive9YSIOnH6XmBrW7XOaNEDekDSWqjxL0-bdyIlAng-tJFzT9q8jzO6hllQHMkglXt3M_aDOVAmj0M8l-XaH4Nex9Cm27YQhQGaKSAK_w6kAoAoIk277tlbsbFCVUxqRYWeov9uRarH5jxWEb6GhuWpnTnaFukPhckGZthqrwH5y96G2SRYitMGkt2cHykPnfag_AMcxGbLCp9mZ6OgwK9aA-geRb0IKTOsV-oMIETrwUQidJLZvsLscgCLyHqszpO1Hb9kF-Nd2dnBAFn01Ujh4kHZY4L7cOuLhBUA0WAr8S1xXalDIOUGGsboBhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e764af88a2.mp4?token=Pi588B9euAOmqP8wkQ5_XHGZive9YSIOnH6XmBrW7XOaNEDekDSWqjxL0-bdyIlAng-tJFzT9q8jzO6hllQHMkglXt3M_aDOVAmj0M8l-XaH4Nex9Cm27YQhQGaKSAK_w6kAoAoIk277tlbsbFCVUxqRYWeov9uRarH5jxWEb6GhuWpnTnaFukPhckGZthqrwH5y96G2SRYitMGkt2cHykPnfag_AMcxGbLCp9mZ6OgwK9aA-geRb0IKTOsV-oMIETrwUQidJLZvsLscgCLyHqszpO1Hb9kF-Nd2dnBAFn01Ujh4kHZY4L7cOuLhBUA0WAr8S1xXalDIOUGGsboBhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
دیدار هانی رامبد پرافتخار ترین مربی بدنسازی دنیا با بهروز تابانی قهرمان سنگین وزن ایران حاضر در مسترالمپیا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107229" target="_blank">📅 11:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107228">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🎙
صحبت‌های شنیدنی محمد احمدزاده سرمربی سابق ملوان که این‌سال‌ها به شغل دیگری مشغول شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107228" target="_blank">📅 11:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107227">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOWe7yTsAWPhotUShsJISrEP3Zgk7OdSA0hAjb97ECEjdsRsFy2mYFedjySE4VXgEKmJvSnRZ5nj17FuX0Wsvt5CZh72d-ic5LDnB6ZYzjHU1OwYSqCm1MMctd5S1qSE5_vEsw8X-4ZJngUspdncUo5ExzZcBi5sm8Ek5Nz4XpOsIJmR8vTMSF3ZbnZ1OvQgMJ1TTtvy3k7LZqBiJ_vBwUUCXBFkB9PxvjMr_NSh0fPIgfKPHvOd92KvDrXp9jhpeY1fNLByVVoOepeYRM1A2I6c6BTB9jZR4GKUbsWzISs3DzL6FIlOdNdwg82dk0mABxc2E0eYrSr2Jbgz0ZzjEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عذرخواهی اسماعیل قلی‌زاده بازیکن تیم‌ملی امید و استقلال: از همه مردم عذرخواهی میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107227" target="_blank">📅 10:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107226">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHcCooES0obyG3d7aArcr-djlw6PWDatQEeNsoun3OaNZiilPeE7cwJvNsq-LAXHMUsTVtBiqh8aZHxFAXzzTcxQB_YOJ3E4R15CvFn8gNi-ATqIrMK_qk3wMGtRJL06-ZfL2w5Byl_ao0htu4q5FIHfoJ6UF3fRmSSyjprhvZaSHiOP-CRsX13DItdnaBYrxaFn6raUix8LZoSuxUVZNfTC9Oe3sesn34TcLAWYnj8DHGb0j9fYZab6g4EvQdCGsamPc9a8xEjRmA6o-QHOB9_Qw4FeBw8LOU154rqrJPxsvHJ91KBOIFsHzSCfJHVHmB_9s3YLq6QUXcC2v3gzPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
تیبو کورتوا: بدون شک من عملکرد بسیار بهتری از کاسیاس، نویر، بوفون و ... داشتم و خودم را از آنها بهتر و برتر میبینم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107226" target="_blank">📅 10:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107225">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bp9lhoY2bhH1QoFxVnhIUXDcWRLduLycrs0v9MY1FJnPkLncBV1fAjvGIioAafoMiAWRER2XsAftADR7AWxITxxFTDOagUvrDW6M2bY8rzrB_NY-wz1nKcmDn0nI-M_Lob-ZHGIz_6Sso6Lj89OaXVC8BbCZy2M12Iz7xr8yfKfhgVHB1xT_PDNqZmNGXLQrqpIRYUZhlEhc525Yh5NMMrxrWW78MIcnDhU88zj2IE2G9Z6s-Rykwn-Wf1xGEJeYcV6fNV9t0W1zb4HHLddd75OBjXaBMkrXtUx8_GeeP_H3CvEhew2_O1X4YwLrVVB3O3B3P2qBZQb1QFPVy4-fLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
رودری ستاره بارسلونا:
🔻
"من در حال کشف چیزهای جدید هستم. بازی با پاریس در ماه آینده، به همراه رئال مادرید در ال‌کلاسیکو، تجربیات جدیدی خواهند بود. احساساتی که قبلاً نداشته‌ام و مشتاقم به عنوان بازیکن بارسلونا آن‌ها را تجربه کنم. و اگر مجبور باشم یک بازی را انتخاب کنم که بیشترین اشتیاق را برای آن دارم، پاریس سان ژرمن را انتخاب می‌کنم، زیرا آن‌ها در حال حاضر بهترین تیم هستند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107225" target="_blank">📅 10:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107224">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19143fc835.mp4?token=D9jeSmEnRAwFRrbaSEUpRgyvuzCY8vhbUG9L-Hn-4OniDIli5S8dM402FABO4484YdiW4Ke6P-CO7FY1EBjDjc0RvgJqfYFT8ykJTe2YlBWtfo3UK6BYBVl28ZtTbrEUSW-RPmBDrwWeO5268LctOKDMfDL21jwPdGlEdL9iOULtv9E2lXKOpIP-BuIl-agINWST9pQAu291F9WxXCEsoeRCvRV3g-c9DQ0jxJJbvsmd1w0ZRrPDo-QWTa_RDhHVvByT4dgmJjbI2-C_pMtYty3pDgkqgRW5jWg2SR42feqKnZgidCjSEubuNgmi36dxBxPN7loEgW4wwELjtSqXoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19143fc835.mp4?token=D9jeSmEnRAwFRrbaSEUpRgyvuzCY8vhbUG9L-Hn-4OniDIli5S8dM402FABO4484YdiW4Ke6P-CO7FY1EBjDjc0RvgJqfYFT8ykJTe2YlBWtfo3UK6BYBVl28ZtTbrEUSW-RPmBDrwWeO5268LctOKDMfDL21jwPdGlEdL9iOULtv9E2lXKOpIP-BuIl-agINWST9pQAu291F9WxXCEsoeRCvRV3g-c9DQ0jxJJbvsmd1w0ZRrPDo-QWTa_RDhHVvByT4dgmJjbI2-C_pMtYty3pDgkqgRW5jWg2SR42feqKnZgidCjSEubuNgmi36dxBxPN7loEgW4wwELjtSqXoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این‌صحبت‌های بامزه ابوطالب‌حسینی رو برای دوستان خرج‌نکنتون بفرستید
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107224" target="_blank">📅 09:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107223">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/444d39e31d.mp4?token=LKVMWOvKz1dJ3qfVIwNeMhhS515K-WPTLZuaX5vSHvlpynqmaF-KfIIfDgvKrw4aWjs9Anul6aaxWPZm-yEw_vI54zYSDFWmMs_99Np3Km-ZZ-c-0D-r0UuA4JMklpfahdenKleK7KTJF9XtrKhjZLepRO-3UZJuhzIv779cDBh5uOdBk5Z9ieVO4iPOf7uOcoQYLfXWltErmyXK_U4wFlIef31q3OvxE0Er7c_IopnB1g1U9X6aVuHrBKNC7k1Xbb74AQgQfNdTG2Vg3GLiQVA9DZWZLdBkuoClb489CZJY3BaXlsEs5QB47wi_PuOTMe5Jm6NTT7er7atXI_qTMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/444d39e31d.mp4?token=LKVMWOvKz1dJ3qfVIwNeMhhS515K-WPTLZuaX5vSHvlpynqmaF-KfIIfDgvKrw4aWjs9Anul6aaxWPZm-yEw_vI54zYSDFWmMs_99Np3Km-ZZ-c-0D-r0UuA4JMklpfahdenKleK7KTJF9XtrKhjZLepRO-3UZJuhzIv779cDBh5uOdBk5Z9ieVO4iPOf7uOcoQYLfXWltErmyXK_U4wFlIef31q3OvxE0Er7c_IopnB1g1U9X6aVuHrBKNC7k1Xbb74AQgQfNdTG2Vg3GLiQVA9DZWZLdBkuoClb489CZJY3BaXlsEs5QB47wi_PuOTMe5Jm6NTT7er7atXI_qTMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
و بشنوید از زندگی سخت دیومانده
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107223" target="_blank">📅 09:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107222">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d0f84bdc.mp4?token=sifkuNB8OQT5uvsLmniBGJHIzM8Efbzu2KFaw5IN4bl4qT3nfSBrB1Th-UPni0ifdN5WXEhTkKZJSofygTi0uKukO5oMRZQe3xIjrI-q6byWZJvkYwZc1--8csiIfj6vhZt5NYtWiPaBR2kORC6zT1kOhMTs80CJjlrE7_M4wyXXu3F9mnjXYpaPzshhK5WpMH-bNW6zZz-ofxbiGLHOEyCtqSaXzB-OM6SlCjllUedYXtKXXAawI8U1NVi9Z9UgiTeNG-v-pTwsKD6Msafpm8ES7TwBb5ephSJOyIVsHyI8zQMjaJMzGdZWgOXWyc_YUad93M-yQTzqDGtwJTuVxzYplxPRIlDgM-6En9UU0zaiathq0T0iO6kyKQcx5uNZcAWO5lI_teGaFuq0XM0WkLj3L6GE9icdL8PgP_WiAaJsmujJJNiuII9T-fEg14efVp-GnkXR_MqAMd0UihpEffPNu7lswZmck8DptqZI-nqvYkK777x5d-M7lGa5qmpiMYLf0b390f-laFbqRvHNLdovf9DOzEySbPIQV99JOQ0eDWSsEOrSMxFv9wC92jZZ2z-PVUeEECPGhQ6kYHwDBVZqvlqputWnQrvenXNLowowof65tTZy9yU3iQc9x2VZO7l9GjG0S5rj1p3ym0sUbTxVp3ZcOWSkqkcfrnvJ22I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d0f84bdc.mp4?token=sifkuNB8OQT5uvsLmniBGJHIzM8Efbzu2KFaw5IN4bl4qT3nfSBrB1Th-UPni0ifdN5WXEhTkKZJSofygTi0uKukO5oMRZQe3xIjrI-q6byWZJvkYwZc1--8csiIfj6vhZt5NYtWiPaBR2kORC6zT1kOhMTs80CJjlrE7_M4wyXXu3F9mnjXYpaPzshhK5WpMH-bNW6zZz-ofxbiGLHOEyCtqSaXzB-OM6SlCjllUedYXtKXXAawI8U1NVi9Z9UgiTeNG-v-pTwsKD6Msafpm8ES7TwBb5ephSJOyIVsHyI8zQMjaJMzGdZWgOXWyc_YUad93M-yQTzqDGtwJTuVxzYplxPRIlDgM-6En9UU0zaiathq0T0iO6kyKQcx5uNZcAWO5lI_teGaFuq0XM0WkLj3L6GE9icdL8PgP_WiAaJsmujJJNiuII9T-fEg14efVp-GnkXR_MqAMd0UihpEffPNu7lswZmck8DptqZI-nqvYkK777x5d-M7lGa5qmpiMYLf0b390f-laFbqRvHNLdovf9DOzEySbPIQV99JOQ0eDWSsEOrSMxFv9wC92jZZ2z-PVUeEECPGhQ6kYHwDBVZqvlqputWnQrvenXNLowowof65tTZy9yU3iQc9x2VZO7l9GjG0S5rj1p3ym0sUbTxVp3ZcOWSkqkcfrnvJ22I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
❌
زیباترین ورزشگاه ایران، درست در کنار یک آرامستان؛ بررسی شرایط عجیب ورزشگاه تیم نیکاپارس چالوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107222" target="_blank">📅 09:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107219">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZqM6A-XTX8_jvPnv7-1eC2WGe7eA-LNQick_cRcbjpVhLpm6hI8k_l1ZemBLD2zA4ysiZiNymFTI2-hkSC2_gizr0IF4iZg66KlG1rRztV1MtLMy04asU9jmlRvguAswcG2Z_VOowyXHg6wtkNGcqnEsx29cAaQVqfHOv3AIqizMPrBT68WKcvYouFP0HLxd3PZsqdFMpNXiy-GunRBYF-_dNR-Nq5llcN4m0tsoG5ie85Oy7ni2IcBsqWapToQiieBtN7k5wmKyKgGJzbvg3uXJ_3KIqZP3kPoEr-upZvMd8cPftnH_vWtHONUXHGwefRec7mYvQAFiSL1olZ63g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
دین‌هویسن مدافع رئال‌مادرید: شکست مقابل اتلتیکو تقصیر من بود و بابت این موضوع متاسفم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107219" target="_blank">📅 01:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107218">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eq1WThYMXuDO4-arZ2xBpt2M_eQk0QyBXT9P5NbeHxPCbcOF3A6fl3LfNEEn-Zyf8U_fMEe3bmD8lxWdgR_QDYrfFtTHg_fKHEBuYfxRdF5ic1NiTp2R-Rg1uvF19XTtoGRnU2zeWWhTIP5rHZXFV_TVCxmxGVOt6g8JZKaFpPIxESRKzNW6Ep-qLeDhyzB8OpwKN7SI59xI7jtIo7T8U_LTWsogvGhwqxGVDg9N2lwp0wHM88v-Aobo6TM6pQ6xxNJfBQVPfgXzOT6h1naSwX1EXZr0cHZQD2AzV6eon8jAcGYGKwtKkGS5jHrNtTtWlK0YhYyPXANLKx81D8DwgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
مبین‌دهقان بازیکن تیم‌ملی امید و الوحده امارات مورد توجه سهراب بختیاری‌زاده قرار دارد و در نیم‌فصل قرار است مذاکراتی برای جذب این بازیکن از سوی استقلال آغاز شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107218" target="_blank">📅 00:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107217">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c410e310.mp4?token=GQol01VS5LYYn7g9Top6HZU2YMtZDXX1GLjdllD0LasMBLIjVyqMZnI07nwu9NBoLA2_lI0O_kNQPvxjEBSJwEix35uHR1mdgneayTGq9wPhhGaKz_N7RKK3uP-0VB_XxaFAtZUQgN2UNEsbfyh2TC48caWseB36uKw5knv8x9XKWSyioD1xUxwyM48KlAHBjphioIJGq1EokUrzILO2Eo6ruisXV02xHKRdrfuwaCvLVYFW2jyzN6P7V-U14ZMbZSZivTWQgYFcC6ZOhu87GbIr9Bd6odxfNF4JW96hO99VuIEpJzuqdeIJm5weGeYCzCsmJGSXqva4QKTdBuNRT6-plqNqb06CBFRwY50c7N8CW5msVCPAF4h5RvaxTQX4ypywfRGwmi6vj-q4JUdYZslBn3Kzy4qOd4n3chDWPTK-Q9PmCTopo4NC_Nn2XV393bJpRwX_Uv5m0HS9KdbIV88Aa1aCnXSv7qEKrQpsyTGn099LH4T9lzu94s9Yw0mdkPb9p0KU_2khzZeFKUDW6zui2NJhJnlV2IFLmIze1To3TWDwrqh1naXJ1xHAjLLyqnYVqYyeb__kDUlgn2ttYjMnDMZGcdNIxhn3XeH749z1Pa6_-UrGvRc66i_45rHSxSCxvQW9S_ZdoPUUifBpUEX7_gBkZyo9ehPMD6Y3CYo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c410e310.mp4?token=GQol01VS5LYYn7g9Top6HZU2YMtZDXX1GLjdllD0LasMBLIjVyqMZnI07nwu9NBoLA2_lI0O_kNQPvxjEBSJwEix35uHR1mdgneayTGq9wPhhGaKz_N7RKK3uP-0VB_XxaFAtZUQgN2UNEsbfyh2TC48caWseB36uKw5knv8x9XKWSyioD1xUxwyM48KlAHBjphioIJGq1EokUrzILO2Eo6ruisXV02xHKRdrfuwaCvLVYFW2jyzN6P7V-U14ZMbZSZivTWQgYFcC6ZOhu87GbIr9Bd6odxfNF4JW96hO99VuIEpJzuqdeIJm5weGeYCzCsmJGSXqva4QKTdBuNRT6-plqNqb06CBFRwY50c7N8CW5msVCPAF4h5RvaxTQX4ypywfRGwmi6vj-q4JUdYZslBn3Kzy4qOd4n3chDWPTK-Q9PmCTopo4NC_Nn2XV393bJpRwX_Uv5m0HS9KdbIV88Aa1aCnXSv7qEKrQpsyTGn099LH4T9lzu94s9Yw0mdkPb9p0KU_2khzZeFKUDW6zui2NJhJnlV2IFLmIze1To3TWDwrqh1naXJ1xHAjLLyqnYVqYyeb__kDUlgn2ttYjMnDMZGcdNIxhn3XeH749z1Pa6_-UrGvRc66i_45rHSxSCxvQW9S_ZdoPUUifBpUEX7_gBkZyo9ehPMD6Y3CYo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بومیان استرالیایی این‌شکلی از بازیکنان برزیل استقبال کردن
👀
💥
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107217" target="_blank">📅 00:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107216">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBzhLM6kr_Ldkuc9ZbV8yqvZwbx6uH7Z3o7RGx3lHefwhKxPfrc-pbJ-18nuqehnwr5heOAlUpoVB0gxmVzCTrAdYRgntIca0FtE75fmIZsnAyrIvGCSYSEPn_-57RDvM4V9ctorrpnS9PZVrFzLXAzB02J1Cs_XURj1ft9Ziv2rzg_yQKJyEUMCPvYr63xVPqSMiDmvWCGSkRk649PROJhiHnpikc1m0ZOGUEuc39Pgd4urfQF2vT15QJA0ucua2SfzpPOJ1Fq1bxgRxLVoKWImBMotAwujiq9FQrWkeHJE7OSQZA90h9xO-lSQxs5Ub7u6DdGB_zVcbwlfOBqvPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
نتایج‌بازی‌های امشب لیگ‌ملت‌های اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107216" target="_blank">📅 00:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107215">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5xQBrR9cqYtFeePq43gWLv8yCEjG5zC18PW1ElGXr_8TLu0KrFFte-u4VQv4vSWvoGyD3P2wNTfZt2HKbNlbDP4BJrMDifCSZycJdEBheUFkgcfAi_HYz5kJl0E5T8i2KIImyQkXUo0ZjqnZhkYoh_saPUy0LyAEHfv19hKGlv97jcyh0990OGmpZhRveWSX0kjnkiFCxG_kDAsh5UW6XGUdk91lPSewN1roUJTzc4gCm_NqSiD_LPdAhE53pAN1oGWdXZuHR5eamnkqfAKUTYWmY49SunVCqwn8bydgR3KAa4I9IruMibzgffHxOfs1U-WchIdtUNcZVw87m_-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
🇳🇴
هالند اولین بازیکن تاریخ لیگ‌ملت‌های اروپا شد که به رکورد ۲۰ گل زده می‌رسد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107215" target="_blank">📅 00:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107214">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‼️
⚠️
خداداد عزیزی: چرا همش با ازبکستان بازی میکنیم و میبازیم؟ با این تیم در جام ملت‌ها هیچی نمیشیم. بازیکن جوون هم که نداریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107214" target="_blank">📅 23:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107213">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdkXaWbhRaOLkd6MPj_vs5TADyJ_xNw9orVt5e8VHAZ1M8rw6g2Nw43x7mRPJ1AbWY3gKlmqJ_dfaZ08xLprxk8wuT2mQUNyjyYea1y0vk9PLxMcH4uTw-inP0-eQ4JD8asyteoFZn77RJvzYZo5VA7o9q1fF1sma5h-aG-UQiv3KTOcMZ3UvEZUbnoIWib3sbldhIhV15Hu89UjiBv6QoLobf8I8kUEOJnA0tCgETxl5FFr04pGypkUq-v9qmShBNLKU06WSkwBM50jo1GLkQwhIU-Ag95W_svRln38qkqWS8WHYkfmCvli56jA_xP3X6qtutvauCumKle9OQYaRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدووووو زدددددد</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107213" target="_blank">📅 23:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107212">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🐐
🤕
اسطوره رونالدو امروز اینو گل نزد تا به روند درخشان‌ خودش ادامه بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107212" target="_blank">📅 23:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107211">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOaCgJmbpB63ryHWMITZoqmooJ-Yu8Itye9kkLhklwi93JdZbFrtzsTw7SRqwtbQt_Xc6AlPkHydNQP1ME9uY3CSTJTI5CDYmdLEN19xLBz_snnmLjuTsp8T8-Xn9S2FJDH7X_pSKWGGaSFQsoBOkJisUs1JQKEnK57jcW3FXx-UDVeDPOxcbzEOfPPcy5NZZwbSJc2Dvueysux5m594ISZt5Wd1xXKFBsytAwKE-8uYsDIjA82CXw16uAOa_lpwb81k6toUdkf59mMqdiYJgaMef4P4UYtgc7IBPRdSG0rQ0n6KLdGCw7v5iDUIOPlxFDtnsL_u2KppMfBQ3ScxyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐐
🤕
اسطوره رونالدو امروز اینو گل نزد تا به روند درخشان‌ خودش ادامه بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/107211" target="_blank">📅 23:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107210">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmsHerrgVoKjCZi34Ugv90ED78Yz7qzGQiugsltTHtfbkysMdhAMVTOB7p7on3NkNfNvP6HF43T4G3cI_le-G_foXo0z-ajJnV0L3ukcba5j1FG_Fif2L9ZQCKUZv03FGRXNwcNt0INaSTBRbxBj53tBCHLGbZsEAIXoO5e9qMziIz9NphZqiVU6XhJh683I33BLtESbG5yIB6wigcBkwSYEqjg4ldTMwRUmpnABzwDcllRyHtUlAvMxDXaQV8z3fG9UbVw2IzQ05Zcwt0x7X4sd-XVLjv0iWkboVSRcHmSy6CCFKKAPRIPQrLAY5Ys2Vg-bqp5G9cXzPVEPhoj-ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
🇳🇴
هالند اولین بازیکن تاریخ لیگ‌ملت‌های اروپا شد که به رکورد ۲۰ گل زده می‌رسد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/107210" target="_blank">📅 23:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107209">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a0f7b1f262.mp4?token=jeuU9xi-aiRBYN4LAmdb4ezxAQapCuraervTQC5EIduGT5OTsOsda7zWf1UQEzGlODuQ0K_hUlXKTQe6wpSr6Y0IqyCWTidWMn9FXOpKkBmwwpuPvX99C3_BwDblguDkB9eF6JqO9GfeK9ti6wiKflE5_kMbVe9ICfscdSMqSXWOOAvAskVtORpwhjb2BMu9o8PBmaKN67q3nr4h8eDZgw_OnHW0HCYd_VJsqDZlYp6mqw7AzbhWQ3oAJnWF91YIVrkGk0o1acQhaJpKEjVXyrz-mTT2b2-RsT0vpKpj59oGVR0O-_Qe0YUGRggzAn6Pqy9HDGLBoAc9QKncP-WiT6kCztMMKgsQYsFChVB4XD8ebKXqEu2SEj3I9y_we4CCdIOJ0ARDrumbFGpIQl7YsmS_Vg4RMYjGpcooU10EUhl-a4YafD_kQApfTwTqlQT290wxRU9IPg7PE-K85iK1RUsApj8_KvRI8tdAVBFP14lcCtaoLLyS1Au02VDZNX3rTGXFL4YKXNnZm0TNc08KJdaSEtwNOs35PU6fe5w-2WcfgW6GoG7goRzCcHrDwFrPrl9fb8oeVjeX95yfSv0otNatSi2K1_sAZK6cHrFO_IfbmVvYXzWLMunQNtfCpRXGoeuLdsfT6SV8Gwi0fKPU-SmTxZvBickv0jKUC8h2F9U" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a0f7b1f262.mp4?token=jeuU9xi-aiRBYN4LAmdb4ezxAQapCuraervTQC5EIduGT5OTsOsda7zWf1UQEzGlODuQ0K_hUlXKTQe6wpSr6Y0IqyCWTidWMn9FXOpKkBmwwpuPvX99C3_BwDblguDkB9eF6JqO9GfeK9ti6wiKflE5_kMbVe9ICfscdSMqSXWOOAvAskVtORpwhjb2BMu9o8PBmaKN67q3nr4h8eDZgw_OnHW0HCYd_VJsqDZlYp6mqw7AzbhWQ3oAJnWF91YIVrkGk0o1acQhaJpKEjVXyrz-mTT2b2-RsT0vpKpj59oGVR0O-_Qe0YUGRggzAn6Pqy9HDGLBoAc9QKncP-WiT6kCztMMKgsQYsFChVB4XD8ebKXqEu2SEj3I9y_we4CCdIOJ0ARDrumbFGpIQl7YsmS_Vg4RMYjGpcooU10EUhl-a4YafD_kQApfTwTqlQT290wxRU9IPg7PE-K85iK1RUsApj8_KvRI8tdAVBFP14lcCtaoLLyS1Au02VDZNX3rTGXFL4YKXNnZm0TNc08KJdaSEtwNOs35PU6fe5w-2WcfgW6GoG7goRzCcHrDwFrPrl9fb8oeVjeX95yfSv0otNatSi2K1_sAZK6cHrFO_IfbmVvYXzWLMunQNtfCpRXGoeuLdsfT6SV8Gwi0fKPU-SmTxZvBickv0jKUC8h2F9U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول آلمان به هلند توسط انمچا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107209" target="_blank">📅 22:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107208">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1a30387c.mp4?token=pk-3G0jTo_b31dKSokSlzaDP5kbkSjZMaTu0qBOoO3GGpsx5Y7eXViedAdKWHIerj01O0bEQfPtONoWbBQN9lMWYCQXIuEXPTfckApp7w7i1yrRd8cgDtT_q1JOPDWENqhodo1OpFQCtSMfg4zRymAUUHnB18qMxWjAH4DXUfApdhqBC3DWJdrJ9o6E0qUpC-Hgacec9ucXrizy0feFvfumXHIXOTr7teBweI3EkcYTjb38JLx-JmWn74wiOGewFOov6K4VIvq9CvJ7BST3goks_N8lSliuLXR8aP7nX85OFjIZaYLQp_uQnae3E6y8til36kCvBnHhsjXvuDB4Cgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1a30387c.mp4?token=pk-3G0jTo_b31dKSokSlzaDP5kbkSjZMaTu0qBOoO3GGpsx5Y7eXViedAdKWHIerj01O0bEQfPtONoWbBQN9lMWYCQXIuEXPTfckApp7w7i1yrRd8cgDtT_q1JOPDWENqhodo1OpFQCtSMfg4zRymAUUHnB18qMxWjAH4DXUfApdhqBC3DWJdrJ9o6E0qUpC-Hgacec9ucXrizy0feFvfumXHIXOTr7teBweI3EkcYTjb38JLx-JmWn74wiOGewFOov6K4VIvq9CvJ7BST3goks_N8lSliuLXR8aP7nX85OFjIZaYLQp_uQnae3E6y8til36kCvBnHhsjXvuDB4Cgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتانیاهو وسط سخنرانیش یه دفعه پیجر درآورد و گفت اینارو یادتونه؟
اگه یادتون نیست، حزب‌الله خوب یادشه، چون ما با اینا، منفجرشون کردیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/107208" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107207">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305c017139.mp4?token=e0PA1PsZpGIJF6NDOX410lm7sB5DSc-1Qhg66o29c5rXlz7EcnKlQA4bf9cvbV1bBTQr_HfQW0Em5W52yR7OurG2OucaZVdceUD_b3h6GpblPnIp9ce-TdHd9jZTFdRVmUAHfWJR60doguECT3-j2AswjPnmsmZvJgGiHhWlhHAYNvLAuogvbyf9TtEf3fOsQ7blis1NBg0rgJtVLof15jovYaVVsYSf-QKFkBgD3srvMmmfefAkmr_psteq2Ec40RXNTxHi7f7-WmRWXOB9BtqAFrwfSydIomoxaDeRI0tpo8gzIZtsOxS3Mw-Wr5qdulpDTx1x_sswwR0TMBAMuzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305c017139.mp4?token=e0PA1PsZpGIJF6NDOX410lm7sB5DSc-1Qhg66o29c5rXlz7EcnKlQA4bf9cvbV1bBTQr_HfQW0Em5W52yR7OurG2OucaZVdceUD_b3h6GpblPnIp9ce-TdHd9jZTFdRVmUAHfWJR60doguECT3-j2AswjPnmsmZvJgGiHhWlhHAYNvLAuogvbyf9TtEf3fOsQ7blis1NBg0rgJtVLof15jovYaVVsYSf-QKFkBgD3srvMmmfefAkmr_psteq2Ec40RXNTxHi7f7-WmRWXOB9BtqAFrwfSydIomoxaDeRI0tpo8gzIZtsOxS3Mw-Wr5qdulpDTx1x_sswwR0TMBAMuzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«
نابود کردن تأسیسات هسته‌ای ایران
کار دشواری بود؛ واقعاً بسیار دشوار بود.
اما برای من، این یکی از
آسان‌ترین تصمیم‌هایی بود که در دوران نخست‌وزیری‌ام
گرفتم؛ چون اگر این کار را انجام نمی‌دادیم،
همه ما کشته می‌شدیم!
»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/107207" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107206">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22263541ab.mp4?token=Q4BDAE7FcwGpwFA_b_vTInLc7zi2WDO7Oyvy5zpP5KZ1WOKOqbzmjRNydKWN3_84mxQpIAgM-QFrqVsIpzqVT7tr_VPPFQd7T5M61S9oQPP1jYaqzbG_lkM7SqVF7i6OTZzg6PW0AZbSw77-jVpkeC4XSRULzmawaqDdxRI7drXjVOoOI8MgniGSzBdZZ7xK99rXmooN_d24tjaYolxl0lnZKe9dYJivbA61lnuyfRbCLLbrhpXtgGwseSYGL41xOol2arFqCx1LJbHxihQ0bKFqgfYTJ89mNySoyC9v9baUC21jmpenPyiehC_rU25Siy8b0lIfgWeo5lkGi89j2GON-RJ3t0kC0wBLMnI4z0rwAM6MF9NB1_oYAyKtdQPLNlD8ZK-Qwt8ivd0u1bXOJDiKbrY4-qeGN5yz_1Au9KOBtWLqk_eypOmD6xDwBur4v8wuBx_0oXFkJDSlIc1VX5qcGbWhPkrFYQr2VQW_YweWLH3XOhy2UBpvrkoDar4RNLnQEhoMiRQTwIpchc7I-olCIxqUUG6FJBhrOfNxW_Hum_iy956xBeL-2tuYPNTpWXLTfOj2xWvJujbzYwoSuwTyrE9p9mK1zxCo9DJOdD5pyVeGNBT3fazzLts-hSkLzinSN9FGe9ujzHqfPUocQEMpYUQ0ja5OpR2kEa5nqeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22263541ab.mp4?token=Q4BDAE7FcwGpwFA_b_vTInLc7zi2WDO7Oyvy5zpP5KZ1WOKOqbzmjRNydKWN3_84mxQpIAgM-QFrqVsIpzqVT7tr_VPPFQd7T5M61S9oQPP1jYaqzbG_lkM7SqVF7i6OTZzg6PW0AZbSw77-jVpkeC4XSRULzmawaqDdxRI7drXjVOoOI8MgniGSzBdZZ7xK99rXmooN_d24tjaYolxl0lnZKe9dYJivbA61lnuyfRbCLLbrhpXtgGwseSYGL41xOol2arFqCx1LJbHxihQ0bKFqgfYTJ89mNySoyC9v9baUC21jmpenPyiehC_rU25Siy8b0lIfgWeo5lkGi89j2GON-RJ3t0kC0wBLMnI4z0rwAM6MF9NB1_oYAyKtdQPLNlD8ZK-Qwt8ivd0u1bXOJDiKbrY4-qeGN5yz_1Au9KOBtWLqk_eypOmD6xDwBur4v8wuBx_0oXFkJDSlIc1VX5qcGbWhPkrFYQr2VQW_YweWLH3XOhy2UBpvrkoDar4RNLnQEhoMiRQTwIpchc7I-olCIxqUUG6FJBhrOfNxW_Hum_iy956xBeL-2tuYPNTpWXLTfOj2xWvJujbzYwoSuwTyrE9p9mK1zxCo9DJOdD5pyVeGNBT3fazzLts-hSkLzinSN9FGe9ujzHqfPUocQEMpYUQ0ja5OpR2kEa5nqeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«
۱۴ سال پیش
، روی همین تریبون ایستادم و یک
خط قرمز
ترسیم کردم. قول دادم مانع از دستیابی
حکومت ایران
به بمب‌های اتمی شوم؛ سلاح‌های هسته‌ای که برای نابودی اسرائیل هدف‌گذاری شده بودند و می‌توانستند
تمام جهان را تهدید کنند
.
ما دقیقاً همین کار را انجام دادیم.
این کار
بسیار دشوار بود.
»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107206" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107205">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca9f3311b.mp4?token=hgX_miOZDz6Z1bLk1WBVX77dYfShyzkzz7HqnG-6F1PoK-c8bGNZtZY9L5_-38x0gFSLrPP1lwS2ByWW22bmWpsJ6JnJVUGsqRhXuHqtsLKlI4lvPF9H2Lh49T81mS6lRROqefBytBlkeENJKfltUYDJ99wKGwRl-8-n4HOK6vrVYio4VQT3MQLKUfgBovf3rzkePSuBNkivLLtQ30FVlqB6zzUcur0cD3L-zi_MMyUSVJr51404_rMdtP5gVogLP-u_h327uk0tVGoenkgX2aFlJ989pxmqckA56UC7Cuyh9ktxtxlVvdArly3DvjD_UfCt7GK1hN9FY3CYjFFQ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca9f3311b.mp4?token=hgX_miOZDz6Z1bLk1WBVX77dYfShyzkzz7HqnG-6F1PoK-c8bGNZtZY9L5_-38x0gFSLrPP1lwS2ByWW22bmWpsJ6JnJVUGsqRhXuHqtsLKlI4lvPF9H2Lh49T81mS6lRROqefBytBlkeENJKfltUYDJ99wKGwRl-8-n4HOK6vrVYio4VQT3MQLKUfgBovf3rzkePSuBNkivLLtQ30FVlqB6zzUcur0cD3L-zi_MMyUSVJr51404_rMdtP5gVogLP-u_h327uk0tVGoenkgX2aFlJ989pxmqckA56UC7Cuyh9ktxtxlVvdArly3DvjD_UfCt7GK1hN9FY3CYjFFQ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
سانسورهای تلویزیون که مغز رامبد جوان سوت کشید موقع گفتنش!
🎙
افشاگری باور نکردنی رامبد از سانسورهای صداوسیما: بعضی از افراد آنجا مریض جنسی هستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107205" target="_blank">📅 21:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107204">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJ_5gH5l9_GOw-f0fv4Ttrh2P04GjEUEwWtcuX1_pcbJXqH-PgcNvc1zOrVycGs5p-y-ONn9T9M1ZKjuvBpbgd3m5omuBbdzWd53Zml4uqZzj8O7SwDQ_qxpDIwEBGckZnj_PVBmmt0-vCVseGGMYYBQcEwgiR0up_8Svx_pRntri7393HrCf8h8Bc91WfqW8g-bo_eDsYutSlZXDU2PRum5A6vTAWj-SS53GA2ew9ZMdE0Onzy0s99KpOfR4jHIB-KeQSWi9GThVZVZS-Qhl-KIqqFEWILnDAZpNVQyflPlGz7XxIZUDyceNm7JgNgz4mX0_BOBzir4FFydvlmINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
ترکیب هلند و آلمان/ ساعت 22:15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107204" target="_blank">📅 21:13 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
