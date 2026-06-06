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
<img src="https://cdn5.telesco.pe/file/PoUlvBa05GRbPf5Elr3w4_gx1mIswz2U2oMjBLqwSX7n47LgWccWx6r_p3nH2NNjsaBWI_fCpUK4_SQJVV6gvJQ4rE961xHTnl8vk0WLGAfD087BAcY9Bvdiwvcn9G-dTDCSfX4PN4WPyTAiM6KeYZsD5QZn9pi-9DfB0v5qGKHdxw7rqgUioL_SFSuza9GM37h3h2DbhRMg-ZQGzaSb-muhGiLxhuQpkfywUK7jbSWE2GC5rMbLZTv9B9YBjHf3sPtWCFTAwaBwoecJbnHTrlhZSxVJGQlxC_3_WdG8WGnzlPRIRs-HOvZ2SlJz5lcpGATYh4Ki62JDTaUNgOV7xQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 206K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 12:35:58</div>
<hr>

<div class="tg-post" id="msg-91143">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bR2tknDsG5e1AaAzAIgbWU6h2-qthOrZwb3aloJvtcu_sq2J7CDJSYp2G5skk2b72K-xn9kZtawoAk9n8wNVXhhY0i5rjMfbsOW4Hp90ZafCbifzkHNUw35YsBUs565YqUoTCdDssW4_y6YqIvPq9fVxcfMvd2X4RWfA1D6bEtKiY-CEYsFf-oNnvZKG810dcB_5I2FUtL4WoutyfDorZ33jdbr_DNAPmiUWW-OBycOnQQlQxMdEItgEBPMul07DLHjMNZERraJ4_ibxG71Um8QHOhHcFmthB-KF2jLDZy6jT3PN4-zc3WUZ1aKBeJAib8j5NETnOI6Z0YHLBYCfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
#فوووووووری
؛ بردلی بارکولا برای تمدید قرارداد با پاری‌سن‌ژرمن به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 919 · <a href="https://t.me/Futball180TV/91143" target="_blank">📅 12:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91142">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c06a46347a.mp4?token=esVn-radDNKIbMFVBaCAoSLBi5_cEWgSrIdb3hDrSJQnaHsUknJ3UOE0aRboPCT9d0qVyaoFFSX1JocZGaV7sz964nynBvg-k0PujLt5VjF2GZ55wXr4T-nYdL38srA9jM18lafgwfMSt5n0CmZUrx5wHsoC7g-9ASxmmymOxlLl3puGAxwZ0CLTjH5wRPkq-mFHTidnyD_aogrtCvhJNF8yQTcrM4_2WltrO2RVWhEDgCXQki7aDvhsoR2Apq2-o4TozzRBQVjwOdabruv07aKab1jQMWpOzBHQGKfOK6jV9jL_7U0osGfeQRK6f3vT6mAKq44upfHt6MabDrFiqzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c06a46347a.mp4?token=esVn-radDNKIbMFVBaCAoSLBi5_cEWgSrIdb3hDrSJQnaHsUknJ3UOE0aRboPCT9d0qVyaoFFSX1JocZGaV7sz964nynBvg-k0PujLt5VjF2GZ55wXr4T-nYdL38srA9jM18lafgwfMSt5n0CmZUrx5wHsoC7g-9ASxmmymOxlLl3puGAxwZ0CLTjH5wRPkq-mFHTidnyD_aogrtCvhJNF8yQTcrM4_2WltrO2RVWhEDgCXQki7aDvhsoR2Apq2-o4TozzRBQVjwOdabruv07aKab1jQMWpOzBHQGKfOK6jV9jL_7U0osGfeQRK6f3vT6mAKq44upfHt6MabDrFiqzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرژانتینی ها از الان تو آمریکا کولاک به پا کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/Futball180TV/91142" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91139">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d49e89d4ab.mp4?token=asyisFJpU0uS49VgtxBNAjiGwAvvZ7K7kasvNUfIsg3CKtxcriN9Jam-doM4bRZDlRwrIcMuuNsad5Pl47A-fk8OE4Yo39AuVnRFsQP-EXHovcTztBZ9cm5U3aFgLwmL2ul4TkDSXgQh-C7iRxZn-8zNcS8TfJynjxIPLEmI2RbEO4yuqYc238s3hhVSQhXfXRaWx0zk_W41aCX78i7LXP7ijxjTRvoEdqWjPMr0YvX1FiZUc4BX736cRu81YEYSlfSreSv3nP_YrzggVdqfWrcnT-q1lEbCC2-W2luEHfnwryoSRwReuIGL3do4JamxDbA4r0FeOAJe18oMHlnBNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d49e89d4ab.mp4?token=asyisFJpU0uS49VgtxBNAjiGwAvvZ7K7kasvNUfIsg3CKtxcriN9Jam-doM4bRZDlRwrIcMuuNsad5Pl47A-fk8OE4Yo39AuVnRFsQP-EXHovcTztBZ9cm5U3aFgLwmL2ul4TkDSXgQh-C7iRxZn-8zNcS8TfJynjxIPLEmI2RbEO4yuqYc238s3hhVSQhXfXRaWx0zk_W41aCX78i7LXP7ijxjTRvoEdqWjPMr0YvX1FiZUc4BX736cRu81YEYSlfSreSv3nP_YrzggVdqfWrcnT-q1lEbCC2-W2luEHfnwryoSRwReuIGL3do4JamxDbA4r0FeOAJe18oMHlnBNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امروز در کشور، دانش آموزا به تأثیر قطعی معدل یازدهم توی کنکور، دست به اعتراض زدن
«خسرو پناه حیا کن، کنکوریو رها کن»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/91139" target="_blank">📅 12:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91138">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2773ec48db.mp4?token=A0Gtr-__nuWUzUw_oVdWKDWDWrZhp1hwkD3rOrqOLeg00ft-zigMyIN29_uY4fMvLOHKM9cp1B9aTiH09vJZfOltNE0AOFfsfMqLrcR56iIOT94C0BnbB7U63s-I0HpE0khbr-ZlO7tgfeqTkoSZeIUTIkg1gptNCQ98T3vT5j0MY6jl0e_dqwhwLW9cWBlKOKzHU6rw9w6IXqVx3IBdUpj9es8uVNA_2ZPig0jyupuJXzHZnqwA1B9LNKVO-EhoklxQyuPFRV9O2jFBX81FfluTLy0JOkM1nSz-tAIlCM_CQAVPRA5zPQqabGp58rlrmUQHesmH7Lo6i-V6hPy6FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2773ec48db.mp4?token=A0Gtr-__nuWUzUw_oVdWKDWDWrZhp1hwkD3rOrqOLeg00ft-zigMyIN29_uY4fMvLOHKM9cp1B9aTiH09vJZfOltNE0AOFfsfMqLrcR56iIOT94C0BnbB7U63s-I0HpE0khbr-ZlO7tgfeqTkoSZeIUTIkg1gptNCQ98T3vT5j0MY6jl0e_dqwhwLW9cWBlKOKzHU6rw9w6IXqVx3IBdUpj9es8uVNA_2ZPig0jyupuJXzHZnqwA1B9LNKVO-EhoklxQyuPFRV9O2jFBX81FfluTLy0JOkM1nSz-tAIlCM_CQAVPRA5zPQqabGp58rlrmUQHesmH7Lo6i-V6hPy6FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه قهرمانی تیم ام سی الجزایر تو لیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/91138" target="_blank">📅 12:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91137">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-e4yDA_cPSsig_65DdXqlTpHsZQgFnWBTWRwn-Fdl1Z6gxnXWhdGOS9MloSUwbqMOo2EBt_X9qVE2LNPLK1776xWGA4fHaFTwmyfNdIRfI41UE9K21UpTcgg41M5qWYhT_3NnPv8dJucTHXWMVUGUzbDROSh8t9-JA_f1rWIjRyWN7UVPxZMMBFVPZYcOMzjNol8FKbd2TQkCWRhopd6EeoXm7KAab8srpxJpKZarPKJc9dCiNcxsIyte-i_W_ndXmq7POQj1i6nracO--vfxIX59IK9HaaRafhskO4r07WbYgTc6lcKGWOKuDabnSLtG-5iga5RISrE_gQzq-LVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
لیگ‌هایی که بیشترین نماینده رو تو جام‌جهانی دارن؛
انگلیس با 165 بازیکن با اختلاف در صدر.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/91137" target="_blank">📅 12:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91136">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be064ede1a.mp4?token=s5SPjNgcgngpQk6RTnqB-n6Z3G6Ze2rm8hxt8P_uCRVY-TUlMlb9IB5cZirqoF8II4AuVAlgk2A9zuyQ2d0kh7h4Gs9TD89H8IgQYsLyY62f08LiQkyziXEPt_JK5sWVAMOmLKDFExHid0H7JazXGceaU05sDs-Tv6lU84-yZiPhojPvDaZLNumJ6BhYKL7LycbWr8ZivIEVTNmqYNO_PwxCysFf0cZ_4iX5VdzoTeN0TjQr7RqFGqcasAjd-C2AtohMMW8Xv76WGbNV0-mepvXZ8wxnFsPwrQgrCsG4UB64v-sdxNxcad3hlLf7-XgDAT15IUxj0E0-4gztji5r0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be064ede1a.mp4?token=s5SPjNgcgngpQk6RTnqB-n6Z3G6Ze2rm8hxt8P_uCRVY-TUlMlb9IB5cZirqoF8II4AuVAlgk2A9zuyQ2d0kh7h4Gs9TD89H8IgQYsLyY62f08LiQkyziXEPt_JK5sWVAMOmLKDFExHid0H7JazXGceaU05sDs-Tv6lU84-yZiPhojPvDaZLNumJ6BhYKL7LycbWr8ZivIEVTNmqYNO_PwxCysFf0cZ_4iX5VdzoTeN0TjQr7RqFGqcasAjd-C2AtohMMW8Xv76WGbNV0-mepvXZ8wxnFsPwrQgrCsG4UB64v-sdxNxcad3hlLf7-XgDAT15IUxj0E0-4gztji5r0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرکی به ایشون گل بزنه با من طرفه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/Futball180TV/91136" target="_blank">📅 11:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91134">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7pDwI8WWoPYCEEQIBGE3Iq2haXU_JHWMCWHkDh2MbY8I2n08al61wVmOfhSPVtWiTtHCyAxWUpgxBvw7-dIt74k8hjzydW1g_vE2KmIlK-6QYDQySIV7XpNyCDE3uVrF49prlWP96VnP5rC_oc5vxLgJH43ONv2aeLKZiAY2UR4PlSd8IwYMkcJ-yXtjvTquCDow600X32WuFScwVfixwaBt2bQ_VYFmXy-MYwyudHYAJFZTQo2UH4AkM9Jm4JOsrJJMO7JHuPotwT8Qn3HZ2TsvmdsPz5FxZAC5BL9cjGXdXwpQUWhrS6XMldu5vumVw9hlRMZCNtVdPSHqNuPZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7UJLu7vL_BVfqH5u3qACaIFrA6czAH4glnu1bj9QJUZ0YS3cnFy99ZzqTZnBjxb8ps5qhFNWy-1bt_pO8H4ne8-ZypxjCH2yw1KKWSL8okhuYS71LzMB-bsC1yZWHRXz7mbbClH2u9XG734eJPPNvM3GlKm6_yfh8DswPcu9yP0qVXVGcthGhfTZZB_Ip1W5K_U9-iUZLOZj2KDCJ61uHeD9IV2WBQxuJNkYkvB4fVPnIhRcKPh80KYqujgZ7z84H12BeNvZzvOcivAnBlTAiYxkZP7BpUx8yaspCsk-jcZX0s8uZGwjPfOdsE2fYw3q-wJQAWf-MYWEllEw_Shpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
این‌چهره که مشاهده می‌کنید صدف طاهریان بازیگر اسبق تلویزیون و‌ سینما چند سال پس از مهاجرت و کشف حجاب، روز گذشته با انتشار استوری اعلام کرد که به ایران برگشته و خبرگزاری‌های داخلی هم تایید کردن
🙂
🙂
🚬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/Futball180TV/91134" target="_blank">📅 11:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91133">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc3fc13c7.mp4?token=shP2sMX1vx4EQYXltmiaMhbfIi0VlhLQLdnyUB-slReG7PztT9oXdYwu2IhM_9gyqNzcN4Z3zStBdXz-lp13OX1pv-rvW7TC54RKWQM1r3I-TGM4-oFMvyU-jsH4Pclar0VJ8X0XJnzdTw-9RONz_dm9lq1UjI1IhHq50yUy8uM5NKckBMk229ymro--pD09D4wiIjQSrj_DVUAklzt_e0Xy8EKw6Rhbklj00fflXo94ZncPpIXo2l0eFpX2L50C9iRkAeWhm2uGBNx7hpAEuqL_yaDhMw7Hw9IPxKVDWBFlcHB3RRi-xpOuatAkwjjXrs_95yp2VILfJIrwxHX_tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc3fc13c7.mp4?token=shP2sMX1vx4EQYXltmiaMhbfIi0VlhLQLdnyUB-slReG7PztT9oXdYwu2IhM_9gyqNzcN4Z3zStBdXz-lp13OX1pv-rvW7TC54RKWQM1r3I-TGM4-oFMvyU-jsH4Pclar0VJ8X0XJnzdTw-9RONz_dm9lq1UjI1IhHq50yUy8uM5NKckBMk229ymro--pD09D4wiIjQSrj_DVUAklzt_e0Xy8EKw6Rhbklj00fflXo94ZncPpIXo2l0eFpX2L50C9iRkAeWhm2uGBNx7hpAEuqL_yaDhMw7Hw9IPxKVDWBFlcHB3RRi-xpOuatAkwjjXrs_95yp2VILfJIrwxHX_tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوستان حکومت اومدن یه سری تینیجر رو دورهم جمع کردن تا با بساز و برقص از تیم قلعه‌نویی در آستانه جام‌جهانی حمایت کنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/Futball180TV/91133" target="_blank">📅 11:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91132">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/112d86fcd1.mp4?token=sDqKHFjruIogVTTeb2YYcy4yMiB5g3ZaiqlmkkoUrCok48DmtFGZ-ehkKIKrMTJ_rJEJAMa5fmsrL7ZkML_Zy1STuLVpn8yijS2ZgI63RqrpSKZukvgICkPM_NSaIzOtBL-y3xqpgUWJKL7O9Svpc53uQaAUkGl1EfjxkO6KKg72Yff4BZds65Y9ICs3P2_tM-yHaJ7ZUf2CxMkTaFqn26--Ey43Y-Zg9gNgu1qEesAzO4hScvpkibJRsq-iPCoKd8zAwLge-U5o9zAEP7kgiSRLEOrIlGVapVje7_QPXZIwsRXMzdJEsp9Vrzdr2GFFaqmKbNQsjlOvTa5GYAqb1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/112d86fcd1.mp4?token=sDqKHFjruIogVTTeb2YYcy4yMiB5g3ZaiqlmkkoUrCok48DmtFGZ-ehkKIKrMTJ_rJEJAMa5fmsrL7ZkML_Zy1STuLVpn8yijS2ZgI63RqrpSKZukvgICkPM_NSaIzOtBL-y3xqpgUWJKL7O9Svpc53uQaAUkGl1EfjxkO6KKg72Yff4BZds65Y9ICs3P2_tM-yHaJ7ZUf2CxMkTaFqn26--Ey43Y-Zg9gNgu1qEesAzO4hScvpkibJRsq-iPCoKd8zAwLge-U5o9zAEP7kgiSRLEOrIlGVapVje7_QPXZIwsRXMzdJEsp9Vrzdr2GFFaqmKbNQsjlOvTa5GYAqb1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
وضعیت لیگ پایه استان اصفهان: پیشنهاد میشه اگر افسردگی شدید دارید و مدتیه نخدیدید این ویدیو رو تماشا کنین
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/Futball180TV/91132" target="_blank">📅 11:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91131">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=IDMO0JY3nx_i_W8vM3_Cdxy5hSG7RemxlESZ8T7d0cLfqQCfO7pOj1bbCdVh3441GQS6wTtOehzsu0IkcfvrmTKujlQ8mJAVfSTVbHiNo0Wo2h5HUgjfwghJo_VWFl5A0JGWBX4eD5b0oeo2CXY0sjp2GPDJHqPmZ9Wn_6XgU-YaPt2ektirSuVbZQFNb6X4CRDJNGErMvvm7vk61tiYn6G0pgnQ1u4O-BQmQXH8Wtt1bgr_Cgo6mBs-QKh6BroSxnyfPzUQr1kJffWB7zPQd96GYCV_pBCiJhk-Y3nrkj5QTfBxAvi7TEnrGxJJv4Cuxz3cr6USUdsFdPbntl0xhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=IDMO0JY3nx_i_W8vM3_Cdxy5hSG7RemxlESZ8T7d0cLfqQCfO7pOj1bbCdVh3441GQS6wTtOehzsu0IkcfvrmTKujlQ8mJAVfSTVbHiNo0Wo2h5HUgjfwghJo_VWFl5A0JGWBX4eD5b0oeo2CXY0sjp2GPDJHqPmZ9Wn_6XgU-YaPt2ektirSuVbZQFNb6X4CRDJNGErMvvm7vk61tiYn6G0pgnQ1u4O-BQmQXH8Wtt1bgr_Cgo6mBs-QKh6BroSxnyfPzUQr1kJffWB7zPQd96GYCV_pBCiJhk-Y3nrkj5QTfBxAvi7TEnrGxJJv4Cuxz3cr6USUdsFdPbntl0xhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمعی از هوادارای پرسپولیس صبح شنبه رفتن جلو فدراسیون و از مهدی‌تاج میخوان این تیم رو به آسیا بفرسته
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/Futball180TV/91131" target="_blank">📅 10:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91130">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nn0BXD-xp1B-n3TAnhWVwp5eE0zUZMnRXz_HF5YLUEYOOpiTqMcRRKJd25ebxBd2rTjUQI_LD5yYjxxJ7W5GxW17_9IkFMnV4rNXOFNVGq33LvO6rpGyWymREeWm8ZlPTyFBRO-xnMSoC9oen41ao8Gg9YNmXem0OmBQDIH_kfpw1i7lkqMk81mEuAYw0M5q22LGS0Jbm9PUHc-hKZcsB8hUfKwtuAqcPMQFXhzwK59H5kfzzGzO6BblwqA_DdDEUzZwt-kro8fWbkZQqvZq1E2D0FZku9y3-SqBrA5MggzIj0UsxbjbT2xCRnvuMkiQMVUGaqTUFUgIrVllqBhRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇦🇷
❌
#فوووووری
؛ لئوناردو بالردی مدافع آرژانتین روز گذشته در تمرینات دچار مصدومیت شدید شده و نمیتونه در جام‌جهانی حضور پیدا کنه. بزودی آرژانتین نفر دیگه‌ای رو جایگزین این بازیکن میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/91130" target="_blank">📅 10:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91129">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🇺🇸
مهدی‌تاج: آمریکا شیطان صفت درخواست ویزای منو رد کرده. از این موضوع بسیار عصبی و ناراحتم اما کاری از دستم برنمیاد
🐸
🐸
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/Futball180TV/91129" target="_blank">📅 10:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91128">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ss6T0DR7HiJ8fWqTqeqdvlWXnwzZlf5oAsPlgYMOFHtylEYStfYwD_dduJgY0SgIM5ruustZkQkUG5_ogICLtNy1QP2vCFyRkBUGB4SSSyWwogayPrTgqRn7HmryBbSsemN3rSN2ZF2TkgKAakoZolI_1a5PcaRnAGuCvz74L9NqbpkocLnfAe0ahwEn_cs64W0CPXi6W9MOe14iyOq7M5BGtU19bM44kxH4hIdf0FG_GVu7bZ6qzg8-7vwwU7ASfoKlrIEOIYLZvd65MPHIJgJ_5CJLHEZp_0ITEoyGUmEH5Y-jdgZGPMqgQk_8MuUaMt7G4QQsVc5PMI6H6K-gTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
🇮🇶
🇺🇸
#فوووری
؛ آیمن‌حسین ستاره عراق دیشب در بدو ورود به آمریکا حدود ۷ ساعت در بازداشت اداره تحقیقات و مهاجرت این کشور بوده. اتهامات این بازیکن ارتباطاتی با گروه حشدالشعبی بوده و مورد بازجویی قرار گرفته و سپس پس از ۷ ساعت آزاد شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/91128" target="_blank">📅 10:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91127">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🇺🇸
مهدی‌تاج: آمریکا شیطان صفت درخواست ویزای منو رد کرده. از این موضوع بسیار عصبی و ناراحتم اما کاری از دستم برنمیاد
🐸
🐸
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/91127" target="_blank">📅 10:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91126">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/728bdf34c7.mp4?token=jjBO5X6oo1Z6i5pfmkPGhySMofQxSetL6UkI4-DAMPUXAW4hpcJl_GpQfxTX0244DxgfirvGpHpdWZ5fMAQFF7FZqX6vVeQOAti71r-rE9TmgsS-XtRb98SMRNT3cQL8PaLv8ulGDhuOkEIHSeNRn_1uO9Foz1TN_kXSoIs79aC32FwzUw_n6qDVKw7L2N47TMVU8zAVlsiyN9tePO6gLBHIKFzchEKfvOlXSwfRycvPSTdVXy_vpQ1m6Naiak4hBC41YUE4MoekUwpK3LH4h0D2afRzYcNtqE_PhcCGVHK-O8RC7YCkx--By1JEfjrymtj52f3r_rfzva5d6jxZmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/728bdf34c7.mp4?token=jjBO5X6oo1Z6i5pfmkPGhySMofQxSetL6UkI4-DAMPUXAW4hpcJl_GpQfxTX0244DxgfirvGpHpdWZ5fMAQFF7FZqX6vVeQOAti71r-rE9TmgsS-XtRb98SMRNT3cQL8PaLv8ulGDhuOkEIHSeNRn_1uO9Foz1TN_kXSoIs79aC32FwzUw_n6qDVKw7L2N47TMVU8zAVlsiyN9tePO6gLBHIKFzchEKfvOlXSwfRycvPSTdVXy_vpQ1m6Naiak4hBC41YUE4MoekUwpK3LH4h0D2afRzYcNtqE_PhcCGVHK-O8RC7YCkx--By1JEfjrymtj52f3r_rfzva5d6jxZmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زور این دوست عزیزمون از هالک ایرانی بیشتره
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/91126" target="_blank">📅 10:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91125">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
‼️
پشت پرده اخراج شبانه و غیرقانونی علی دایی و دادکان توسط محمود احمدی‌نژاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/91125" target="_blank">📅 09:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91124">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06eeae197.mp4?token=dMu1OamEKfTNa5E29ZfRsY2iqfE3o46rPQVVaRI5vt3lBAwcuWSMIrKhC8VTlgtsb_BYrI5ISEzZ9DBlVmo8sy2nE45nn8sIScZD6v-V5vBJTUkKXHkY0ib_MGSEPWf2AMhC7ZOHvi2q0hOjidyGDisEYljYKNexBMhV3932Ekwp1yEMtdQCsWLDaVHm3AoLwzsq_8byl4oauJiNqXUWWKoTqQft796V5AiOqPJ55IuJU9hknUYv0yJsVEhrOE2YDGVwSVfPo91NY6_KmkIOl6oGrnCNApzSB8bLju4VlvlsKWmKdlLQhgsi1I8qOpDCu3BoiDUEn3OmRClIndSvjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06eeae197.mp4?token=dMu1OamEKfTNa5E29ZfRsY2iqfE3o46rPQVVaRI5vt3lBAwcuWSMIrKhC8VTlgtsb_BYrI5ISEzZ9DBlVmo8sy2nE45nn8sIScZD6v-V5vBJTUkKXHkY0ib_MGSEPWf2AMhC7ZOHvi2q0hOjidyGDisEYljYKNexBMhV3932Ekwp1yEMtdQCsWLDaVHm3AoLwzsq_8byl4oauJiNqXUWWKoTqQft796V5AiOqPJ55IuJU9hknUYv0yJsVEhrOE2YDGVwSVfPo91NY6_KmkIOl6oGrnCNApzSB8bLju4VlvlsKWmKdlLQhgsi1I8qOpDCu3BoiDUEn3OmRClIndSvjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
👀
خنده‌های نیکی‌نیکول زید سابق یامال به رابطه جدید ستاره بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/91124" target="_blank">📅 09:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91123">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/806ce63d62.mp4?token=OmdJLl82YZub6ek8gkx22PHRwexpBtQRUl2sT5NlW0xeJW7IJrnyGbHCahpr9vkVBcwT9qirBb5XGK-0CCSM5dHH6Z41xk7yEaQPN10Pit8Eb3hWZta7oypfnuvKzA2Nsy3IPZC_1rP5_i9NuIJYFcowCm3_7IURUfRBwgPoCXcLpCc0qqPPKSWtCoyF3MV2vlsUiezpyelkvKZsmvB9E46zmiLYYiwW1F3rA03whiFCk1uKADyZhhDkaQk0x9T19orWtXkv4e3r3B7gbzHodUJt9VJr-mQBVT-VrUi42H56430_X66gbde7BVkLZvfH-f_n5Wtwg0-AC2UnA6q-Lxi4A6QEfsGWPnIPm4m6J6b-STQlyWOkP9mCBXbXeu9fZT8npt-0B79azw1BkZnDANmoXHpsX5C9hn1NJVzTaIr8hr6qpThZ-IWB4Jt9I7xtecNqWTLf4LllO_rMA6wdxRHDzEFhs0ha9Hx6FLiYnHfkUEjT_azn8loqBo0_XBtao96sVtup2vx35TpjoLCkLPZQqGtELKL2ukHxUUnoX-ftizWwCT2_PTr8qH4eEMNiIZGB_05XlIl9IHXcYPfvdqlVNMKHqWpgmjCiQxR70xLW-vxlSrYlVv1pslngxpKeoh9BqAVssmMyHvBoybDjYeHcbm9l5yRnEWbioZiHpCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/806ce63d62.mp4?token=OmdJLl82YZub6ek8gkx22PHRwexpBtQRUl2sT5NlW0xeJW7IJrnyGbHCahpr9vkVBcwT9qirBb5XGK-0CCSM5dHH6Z41xk7yEaQPN10Pit8Eb3hWZta7oypfnuvKzA2Nsy3IPZC_1rP5_i9NuIJYFcowCm3_7IURUfRBwgPoCXcLpCc0qqPPKSWtCoyF3MV2vlsUiezpyelkvKZsmvB9E46zmiLYYiwW1F3rA03whiFCk1uKADyZhhDkaQk0x9T19orWtXkv4e3r3B7gbzHodUJt9VJr-mQBVT-VrUi42H56430_X66gbde7BVkLZvfH-f_n5Wtwg0-AC2UnA6q-Lxi4A6QEfsGWPnIPm4m6J6b-STQlyWOkP9mCBXbXeu9fZT8npt-0B79azw1BkZnDANmoXHpsX5C9hn1NJVzTaIr8hr6qpThZ-IWB4Jt9I7xtecNqWTLf4LllO_rMA6wdxRHDzEFhs0ha9Hx6FLiYnHfkUEjT_azn8loqBo0_XBtao96sVtup2vx35TpjoLCkLPZQqGtELKL2ukHxUUnoX-ftizWwCT2_PTr8qH4eEMNiIZGB_05XlIl9IHXcYPfvdqlVNMKHqWpgmjCiQxR70xLW-vxlSrYlVv1pslngxpKeoh9BqAVssmMyHvBoybDjYeHcbm9l5yRnEWbioZiHpCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇲🇽
هنرمند مکزیکی با آهنگ جام‌جهانی این ویدیو تماشایی رو ساخته
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/91123" target="_blank">📅 09:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91121">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1Fj-KR3eOvkO-X11__cNhS4rzG0d7VATK6SCJV0AjCKQMvWzy3vn7a8nmiGIBO1lGBG4xrMwwiSlsNHs1-mWcWgHfZre42BZKkL5KOnvfgoMCzcXpDTwVkvUP5SZ4e1cxXNb7VUimjP6dIAokKAj7qA4GpV813vpT7GJDzYrmn_GHRXi-nAo4wR4jejkwXmHQF-iZl-pZY0aJ4a669vqJ29_CS6-ncWe-xHsNv43-iM_0gFC0n6vCOKsPDIr6QtYBYliJdVc31vJ0Ny4S5rv4t-fxUIh_o3b7ZbY1AOk7hxdDHaZ9BB93Vcx5KZog-idtOTjx-O5g72102v9jQVnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfsMXgnJWi7nGlYMQP-nGNtR9qBh6xLBFnYYI1KpVs3gwD3nW_eQGWErzFkKkfLLHl7T0aysCFo-Em_LC-NDFhuT0pwBas0-FEQHWBbOUIbiE4Z4YI3qI7S_6oJCmImPCcYE8h7EtRuT7SoDNelveProXCKLDi8TweUFGQJp45fc00kqGWJ_Xd1FdFQhHHCtd-iy6Bem_jbW8_1oQKWoX8i-SZEXZOt1x4jOdQqpUKEpyR_2tgYcTYgmATomseLQgzeyG3mOuU-CcjOZrZEn1SmAhekkqlS2CHqKBjm0YADog-gTSAbhdzZV3E_4PvoX60wC-ih2nC5H7E3IB0WP8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
امباپه: به جز هواداران بارسلونا، همه قبول دارند که رئال مادرید بزرگ‌ترین باشگاه جهان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91121" target="_blank">📅 02:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91118">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇪🇸
ورود کاروان اسپانیا به خاک آمریکا برای WC
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91118" target="_blank">📅 02:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91117">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: پرز عاشق و دیوانه اولیسه هست و برای جذبش هرکاری میکنه. پرز گفته این بازیکن منو یاد اوزیل میندازه و شدیدا میخوامش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/91117" target="_blank">📅 02:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91116">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3j5TMGdgCAhV2Pv5o7GDLoVu_gB8cxON0Nya6yURXDi3kCx0arzpAN_mSvrAedHmTHifmVSjXmNEDKkfc45479lIukioekiW-j8ZGwoqmIqa9do_nGgLWnh8bGpJ1XUzeuizmAL8htx_g2k8emeWGJMQrIdzhCX2GsJyfodLuUvZM2H6YHg-cGdoKkCRf8jjxl8ZvePp17Rweh_2NTUK8fWk7G9be5lYGpv1NT4UgCu9NCiSxplf2q9suY9vosLxMksmtC9MuT8-GVHYgAqNSA1xqP7iAsQkldKlP8N2D4qfLMeLGtxOoWhw07YOeBIGYjlk87tsdp5DnCB142jZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇩🇪
#فوووووری
؛ فلورین پلتنبرگ خبرنگار آلمانی از علاقه بایرن‌مونیخ برای جذب مارتینلی ستاره آرسنال خبر داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91116" target="_blank">📅 02:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91115">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: پرز عاشق و دیوانه اولیسه هست و برای جذبش هرکاری میکنه. پرز گفته این بازیکن منو یاد اوزیل میندازه و شدیدا میخوامش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/91115" target="_blank">📅 02:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91114">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🇦🇷
❌
#فووووووووری؛ رسانه‌های ارژانتینی مدعی پارگی رباط صلیبی خولیان آلوارز در آستانه جام‌جهانی شدن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/91114" target="_blank">📅 01:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91113">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🇦🇷
❌
#فووووووووری؛ رسانه‌های ارژانتینی مدعی پارگی رباط صلیبی خولیان آلوارز در آستانه جام‌جهانی شدن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/91113" target="_blank">📅 01:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91112">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKempgzb4IDdo-lCOAhO0-JMj8DOsbKlTs3_Rx1R0uotfaTASr_Zond7_aHkptTkIuEOygx3stIIubNgOoPs6NXy0jYMvz8EzF9wu3Jvaf987sEm0AV-VLDikcig7JUm614cm__CRrJO-w-FPld7BR0rCnM3VqjVc_OpblYxwhfsKPog8JNN8zz4u-HFQkscq1vvOeJ6imFAs3nVoEqFDbbqehIXcZelZtDAM9A2PboQTwE2iTrqqN_T2Rr5S-8mKl6D-Y9UBS4LV4J-D7HGjH4p7sj7YVLCN7JMNZckgjCgj8F18Md9_U1Wu9cP6tp06V3i3TfZPhlkEHlptzsZ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
❌
#فووووووووری
؛ رسانه‌های ارژانتینی مدعی پارگی رباط صلیبی خولیان آلوارز در آستانه جام‌جهانی شدن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/91112" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91111">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MktG8yM56tM07r-KrhT0mvzu1K2zogyYISs829eHMKG57zvUZledcWcs0Y_JhOfY7P7xQz5vI09K5w4AAvsMLC2N7mBXDs66RppN9hVr4tk-TjK8RPl6xx5NKsMv2j3c6jznY7nBv_n-VyB3Nw9MLNAsCgDj6Nx-HMy0VEXmIvLtIh7czBz7XjPw9nW_fX7ZWKn2dC5M38zPF465Umt-JhuLzyyvbP2VS2dRK37JFKdWGiI1BkVbKPAjhyoS7_ColyYJ4ccaKnP9h6CvQxSEaF7__QWQo0eQ_LkSaYE_QZKIlE4FyV-f0OzgJKug0PgogyFgwtWTptfjPM9rx5zdGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت
؛
✔️
تیم ملی والیبال تحت هدایت پیاتزا دومین تیم جوان لیگ ملت‌ها
❌
تیم ملی فوتبال تحت هدایت قلعه نویی دومین تیم پیر جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91111" target="_blank">📅 01:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91110">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_2P8bSu1dgqGwGJBYUZiCLRR3bktI4wGbIUmdA_lFTj3Gg7AEa8RUQozy0N4UcQk_GgioR1e3nQeOD4joczZqNiLbROyCNKnmcunTaaFPmHt9qH_fdLMuxi9QtBde-rPTo3tIFGpcHIeMUZPbjQekZAnNzAIln7ocw9M6DtTbUEdgFLk8-22wghDaAKDWpbh7nqQcq3amB8TPFDf29zAJc5uUvPq0kYReSqqxtzccpFStlDCcxruNiVX9NBIT82PO7kFJ0xSbaf1Yn8o5mnQLUg4LRvlOrC2g0OX7v937MGgvR_d0iVHPnq7sUnB_7PCt6DBxjM6UT0PRFVVNuzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🙂
🏆
هر سری جام جهانی میشه یادم میوفته تتلو میخواست جام جهانی ۲۰۱۸ کاپیتان ایران باشه با شماره هشت و ایران رو قهرمان کنه. بعد پاشد رفت تمرین استقلال که منصوریان راهش نداد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91110" target="_blank">📅 01:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91109">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🚨
موزیک ویدئو کامل شیدا همسر ایرانی مورایس برای جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/91109" target="_blank">📅 01:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91108">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjCLtEjhx9MES5c_jSZ-DspolCpiUQ98xoSqWZvsEmbBAkYHDWwjjNzhT5JiznB_iDVuqcJSR2taqRWkYphHlO-pe0nsImXgqPehTazCnyFaeu-aofyNeuGo8BH8-fxdhvIg4r3nCC7yOgLZJyzK21o3HDJhvX_MQs52zmJ6yocwhQ2mzDgy1tEgqFkQuO7CHvmjDc_t2sGWgERUR0aFaZ0g3ShPHdHxVn9T5oucwa1VsAxY4VXS-_JtO_BaUGbzqbJzuPHrF-ECphP0NNFA8cB5pfxoid01IzgbSsJ4gs43j6gM0mI0vdTUqa80wzxxrKgbPIJ1ML2ftXaTwuBNYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری
؛ یورگن کلوپ اعلام کرده که در سیرک انتخاباتی ریکلمه هیچ نقشی نداره و الکی اسمش آورده شده
❌
هرچند رائول به عنوان نماینده ریکلمه مدعی شده که اگر دوشنبه رای بیارن، مذاکرات جدی با این سرمربی آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/91108" target="_blank">📅 01:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91107">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
#فووووووری
؛ شنیده شده بخاطر توافق خرکی و خیالی، پدافند خارگ فعال شده و سپاه داره موشک میزنه سمت تنگه هرمز
🚬
🚬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91107" target="_blank">📅 01:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91106">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpIL_1pEqEhyp084TeXTYSC98kwhvEDzruKmqlonaKbbLaGbMAWyoimqyjyVRtVy6VCRUeTcDPDt1qejOkQEQMHFjE7S7OCdkmskb43OLTy4fqsA1aIOShSMJ_7e874fitTTYHvmI-XALCT_PPt9NBfWIocHcAEemliIUaTV-3ioGlDZZFcq0zB2F1rP5WJLfRxwoT7lfXazYu8rbHhSUrMLCBfR1KkjytfCtBsyvAq63MKlC9dRJ1t1e8VPfb_ptYHapgcpgH-EPI_nfh5LSNhTOAskuOSk2tVMrJM6LV4u49gkkXvklbAqO8ZKSenFwPypDHNxbrSAQ55rlQsW9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارل 18 ساله به دلیل پارگی عضلانی جام جهانی رو از دست داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/91106" target="_blank">📅 01:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91105">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/KnvF7uEZORIc5CHKe8ywUJ8skTEeHyWkbn7ZnU80WujqYI6wHROu2otj60Dtz3OzmwZyQ9LmYA_yEvAkHMaBWbRYn5zVNwncQtBhYyR08YZAMvMrQDVptxZ7OFE6IgROBCUQdRMwWa0j2emNT88kY68hXjIariglvd_h10B25owj1sCqcpcjVH8UGY2zSx-wXVNKQSmkO05vUTPtXeNE_mfM0hnt_LcjERj-_8A0CjLgRhCNZZEcFf9MluJXEAqJSDmf1-8BQVRV9yFxJPGJicSv8HGPXb_KOYVKM4iALCe8S0aWa5qGAqDbntiFkGDJDdxzkA05VLat0itLrORCXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووووری از رومانو: لنارت کارل جام جهانی رو از دست داد!
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91105" target="_blank">📅 01:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91104">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
فوووووووری از رومانو:
لنارت کارل جام جهانی رو از دست داد!
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/91104" target="_blank">📅 00:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91103">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMqhqjn4wId8418VU6GousgiGEp2zuleRRmp4pWFkUqUcMQ6mhQIxNgUV4RNzycXTbTNi1goUjOO5hS8oqgBiKTdyPXw3ffLvdHvQncM_KLELPC_OIfIbTJW5OOL1L5gKjetS0CD7hkR8oCn_URwn2Kjxfq1o6eoCQbl0-qoBXsAdB1HQPCjey_Z_kUAqvDCT8PeT2mirQOZf57Q52fmHPCQmL_0u01KDU4cQZcla0K96WBF2BgemHBHARB3vlTLIlzSgLzXYFI4iCgJSBmgXo4GWpK6_5A7gYJgaaYDA2nZaGAQcd2agZ0v2YJ6upL08r3oT515QWTJErhlTZqCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب مایکل اولیسه به یک هوادار رئال که ازش خواسته به رئال بیاد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/91103" target="_blank">📅 00:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91102">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f8ee5741.mp4?token=halSPKyIRrEGuPQYf6JcwjDUR_3ulQvN4NlZEZK1C8qijyMH5NXCz3UG1t2Uq4VeyVh70ulIsiZeLmws1BG550Wrs2i11Nsnz2Aw6HPzhQB7YHlr386mUrFXBVChVxPlWriCmbxqnhsC-OtQZbdBrcDNhwLKcRMQJYVhZFh5jRhPxjIqJju4c_ziArNFTeun-LGJBmCaqVLtFmW7RHKnZupRNEcuyXVtOlJiB4hpsZ6gFgt5yDBFMKTdqZY-04D0J8qztC-2YI1b56cicNkOoKvpVSEZt1kDHnErBkcxcpVed9PwZG3Bw7sEQ8uUwufu3roAFsiea4thS9QK5HwtC41jnELI2SGJrf8v8B4ErARTYBzGkRQjaUptATvw0QBkoBIytV1kXZH0jBKEtfYvSPZboV7pJu1HXEfzyO-sh8YccIJJxHLd8tWGzijpet_VFYinak-cjPJ17ls4QlOL3P02O1dUHaDN_-_AblUcojU29XN-X-ZknMTTF_fE153uy3E-FX41GISOfT0bmyjcLih4aXvveiDc5UG0r85YFhM4AJdBRpLH1j9OrILU0IlvkzneVn4TXzCi1uSppuuuhb2ybdyyNgz_f7oaabhok_t_VyvAeWXbZRRE7r-shCQeYxaqQCJp362xOhdafVsua54DZBQxtzwp9i9dUvFU5pY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f8ee5741.mp4?token=halSPKyIRrEGuPQYf6JcwjDUR_3ulQvN4NlZEZK1C8qijyMH5NXCz3UG1t2Uq4VeyVh70ulIsiZeLmws1BG550Wrs2i11Nsnz2Aw6HPzhQB7YHlr386mUrFXBVChVxPlWriCmbxqnhsC-OtQZbdBrcDNhwLKcRMQJYVhZFh5jRhPxjIqJju4c_ziArNFTeun-LGJBmCaqVLtFmW7RHKnZupRNEcuyXVtOlJiB4hpsZ6gFgt5yDBFMKTdqZY-04D0J8qztC-2YI1b56cicNkOoKvpVSEZt1kDHnErBkcxcpVed9PwZG3Bw7sEQ8uUwufu3roAFsiea4thS9QK5HwtC41jnELI2SGJrf8v8B4ErARTYBzGkRQjaUptATvw0QBkoBIytV1kXZH0jBKEtfYvSPZboV7pJu1HXEfzyO-sh8YccIJJxHLd8tWGzijpet_VFYinak-cjPJ17ls4QlOL3P02O1dUHaDN_-_AblUcojU29XN-X-ZknMTTF_fE153uy3E-FX41GISOfT0bmyjcLih4aXvveiDc5UG0r85YFhM4AJdBRpLH1j9OrILU0IlvkzneVn4TXzCi1uSppuuuhb2ybdyyNgz_f7oaabhok_t_VyvAeWXbZRRE7r-shCQeYxaqQCJp362xOhdafVsua54DZBQxtzwp9i9dUvFU5pY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">First dance
❤️
Last dance
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/91102" target="_blank">📅 00:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91099">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e5rluRmqOEQyXoyurpaFvOK9ZImLrh9BfsaE0acYpwEmXh_4VqRD7jLrESNEUsAG19MMoEebzllLConGAXdMajli0sHFl0NLJgmfot_38iQiFxRQk3vTd4ykF7ozm3jH-dr5LWxvq4m3s0RPphROiK_VXwjsogmSDvQYldoGR-1faM5iFbbidB-av7CKUTJZfiaLbhsQ4-trPtwU3WkxJ0rc49J_GfUkHWz_pTQHUzaANE-j8kfGc7cadNw3621NAI0yg-DGLBrihaFXceBth54h3WFaQiPHtulw4Sdyt1rvuxdnfAElWqw9pqSSeNcmgrGJedDLWmT2hsSjShJs8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CneoCr4oz0gBih6dXfr6dHxbrH0ym0_Ltr0EA_vqZLH9KIFUNXjHXucCHH5hpHWvnTKNmY2kK6l3BovYdtVh3DN75sIzX82CmUaRxlViqEO0pKA66x55S9pYDPlT5Kh4y7uVtHu7OIgyImzSBSlUCAYCLBVwcZH6ji-e49oxWaIdZ6UvHbQG2m0yIa-ZdOnkDEhk8aTK0Xq2asp8GgvkGbW3VWyo3h0JMC78kSz5FZzZWIZ0kx8-bnMH83_xsImLx2pxQWo0Zw4QLETLQ1xRLg3-x39E7ffNrsJxtcF04RrSGM4H9l_DMO-lkOeTCYDd8f1Vac_bKsjPEVaGw5Cfbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V_cocnUdCQhxyTZTRd1wYRJCTvq0KLzdl4Pll1rXHmkk8toPNp6Ba1igWs3oeXKq3hDkmFybmYzhZXsmPsu1JSL0AhxA-mWGn6Aa01n84QyP0slfmeAnik6714kZ3AgOYrMLU544MaPpAaAMFdI1n8M5IfIpoVp7XdUZSwrqjJiUqFxlOliMZmqJ3RwQYBgjZmAuyxfQD1m7Zl3FGQxTlF-lwQ2wQN2XuGjpD3aqqN66evh9GxRqWVU9F0dZ6jiBCgZlbjz25tMn2sesB0H6OK37hqhN-b7j2IISoSO0dqhVrqTwfuOguNaIJ4Oo9Mf9A0bS6e4HuwKxXBTfQ1M9AA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زید سابق و با کمالات وینیسیوس
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91099" target="_blank">📅 00:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91098">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0bxqaoPsQUPyNLANGprHjzsfqd0pynZkuCvngPeG8JzTC7A06m5MmPOdCYzz0esjQXXTMRpRR2kcI9_WX2JbaK9nPl8VIvexB53azNB4n5utaBJ7sogpCUrb2QWcxCmgfkM4gt8NUt00y-zi2hOPDRpB8viQF49MhXGKo-p7oym95X93U793H2d-PhuISBXOd1uwGqorlJ0xQBFBHkg9ZnhTRDs6N9IwC_TtmXjQg_6irMnfldtG07aL2o56YZFlX16KrioCNnv3CloCdoYZcEGtUdlACSv38mkLuDFTje0XCoPYohbqNSnA9b-6Ar6J270Hzb5AUEbO_93K18TfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوتبال همینقدر میتونه بی رحم باشه
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91098" target="_blank">📅 00:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91097">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvWWNsosJ8NpKzMF9rySwkw-GxBRGMdz4_xZap3kotaVEPY1IBEmxmpRgBG3oK1TO8lJfv7-6Mkct2xs0nga2kokChMlGxEGGSQ_rRCN_9XpYcZuDAbqJkt2VHiewp7poMYKZYwRCGE6PmAy64643lWicL-1xzELq_RIrnIr318lvfEAcKZexnK3Y_G264SniJiP888QcnhHtPACpapJ9ggajqbEu0kwceVQ1REYQdxiOnUEKUrHjl0q_oO4i1zIn0zRyWfDrVwa3YbzLS8MpSq_Zl4K2Fr1bMLG1nHJwTIRbj4IGehRqhzbj6_D3eLOzIY5MhtSmKwbAb9pptJW4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ بازیکن تیم ملی کلمبیا در عکسی که مجبور شدند قبل از رفتن به جام جهانی با رئیس‌جمهور بگیرند، لبخند نمی‌زند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91097" target="_blank">📅 00:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91096">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
پلی مارکت: صادرات نفت ایران به کمترین حد خودش در ۶ سال اخیر رسید.  @News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91096" target="_blank">📅 00:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91094">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KNj1jpq7KBLdfItDmhBzwo1WlxaBqk5_oxuetzPAP_kh4mJW7xJpzTvMYPhNQ-2KQe8b9mff6V6_HW23p9diX3SZcEEj1yQWVKmLMnOubtLlIhyKoGOWI2O_XY1rhkdaE_hzHR2Ze4VGK0fkdnjbVlTI8iNojyVnt8Kby7KfTjl7kdpKEgJcz7YodDlHrEFxuo_4l6HOQM_Y1v3T_DjswkaPBaXa_uhqA5bWBxTCaJVZyb9G1s3FtcCHwsBAA2jVMcPP1zUMgoN6e77MCrTpPix3hTtVB9hFP0zebNHmwgO653Qktm2qCfl3NZtsJMXZz5-th_3DUP1SLdg6MZyebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iIpvEj4WtYTtOstiBW7v7IMec8IV_36_QmRhnoRozE8NsH5sShwfhu2HrFnykxyLbwOixlVsh9kklkEz_-hY72QUeP_efenlYS1bWFkYPCeDZ1r7eJF23JJ7ZUT_L_36q55VFikntcJ_UKm1FEDLa3MwK8KQarYIa76zkF41vPfudD9ngqKXKkpRoa2NxbYdzayQQnxWHYAnznm_2NwTix7zEH6fYSnmmGVkVopvf3t2NerbJSViCJijpWO9vST0Ys-TBX79BNPDY2OOshWwI7dKsHRQ48W9aLdsF5hGIEenvGT528-D7loWjVwtSd40Z8e6nv3_SeVM6B6bHOopdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
انریکه ریکلمه یورگن کلوپ را به عنوان مربی مدنظر خود معرفی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/91094" target="_blank">📅 00:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91093">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🔵
باشگاه‌استقلال با محمد خلیفه به توافق اولیه و شفاهی رسیده است اما این گلر جوان اعلام کرده که پس از جام‌جهانی و برحسب پیشنهادات دریافتی دیگر خود، تصمیم نهایی را خواهد گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/91093" target="_blank">📅 23:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91091">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZOnDKfIvzhtN5kYUPXKSNx_KDfatM5D3h9g4SNosXl4GfshLkuFkKuQ2xE1woFGDe3n98wYD4JI-KbA6z5z71fdT7OhrgPuKSIuJGB_0AO36jjqPrdm1Z2AdMh15eZ4fLH16ELmkh8IERjqtWIreMUTuYhCivwtsiQC3bISoBUlnhAy1ide986ZJ_7RvUITPovbMAqLlxrO8TOXHpPEjjccSvuw89FLWzdfWrvXQBOgD3DBrp3eWfVwbJWMBuGSq2bFVsw7Y62BxXfRBsqxp3X7VwHoC7jSPsK_jtO0AhERjaH45wa8bt2GVkBIpkOK-WW6EdrTWM_HLq-2SmN_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار بهترین بازیکنای این فصل پنج لیگ معتبر اروپایی در این فصل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91091" target="_blank">📅 23:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91090">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qP6WRaUrEuj6NPp-6o6cexq-UIrwY_LvPsLRzQ_rhVF2joBxdmVpqlqhfPzo0BiO1QswcCJPjEic5gaxkoQIQSZuvKfpUDZGp_ON7eKFZX_T1QV8dZ2_qr3dtVnYZL5acKJ_xOUoDTygjafBroy89bjUVlRfd5SJMsiDokYkZ1bbDEAExgYhMJWcVxyiTE9Sf_sGYl7WuOop3Y83f0KV3Ek1M9yCfiuefIXlssmOqYR__j9JFTB4ferKAg5it8YyWudTHeJYuHmvpkLWm5bvIkZDpMqS-cnoHcfs25WZSZNvbj24uwT4xwMMHcnzdwpWQgKQnZxwmFJfot3vYaJkug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
انریکه ریکلمه یورگن کلوپ را به عنوان مربی مدنظر خود معرفی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91090" target="_blank">📅 23:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91089">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎙
تاجرنیا:
آمادگی هر تصمیمی در خصوص لیگ برتر را داریم اما اینکه لیگ را نیمه کاره بگذاریم و قهرمان مشخص نشود این خلاف عدالت است!
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91089" target="_blank">📅 23:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91088">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696197860e.mp4?token=MzVbWu48lYZgimpLEBr4nBOaNsKETUSbF_OGgD0Wxazzw3RHQKAejvdEpfGPuTQjFPF4ONo2UyEjxE9T9uLlNakLxcuYxLJTJUA5ShYmrD9fEBEql7IOKOtC0UP6XYuYaZen_EEESHfr1KXnbHzup_af2ZrlZXfpNCwohbsG52qlDqe6iwuvNt67P5t6JULFiovoHtK1hmJLZUp5-XI5JetSidWDA7s06dzlhv_2c1aqZW-ruwwTzYGbedkV4-SW19Xh8h_liWM4LxRf42ORgb3CodyT_beHMmFAnmZfu3NOPkJXeQoCq1BmqdlPJuSxmfJZQDgKPICJHFuVLlYzAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696197860e.mp4?token=MzVbWu48lYZgimpLEBr4nBOaNsKETUSbF_OGgD0Wxazzw3RHQKAejvdEpfGPuTQjFPF4ONo2UyEjxE9T9uLlNakLxcuYxLJTJUA5ShYmrD9fEBEql7IOKOtC0UP6XYuYaZen_EEESHfr1KXnbHzup_af2ZrlZXfpNCwohbsG52qlDqe6iwuvNt67P5t6JULFiovoHtK1hmJLZUp5-XI5JetSidWDA7s06dzlhv_2c1aqZW-ruwwTzYGbedkV4-SW19Xh8h_liWM4LxRf42ORgb3CodyT_beHMmFAnmZfu3NOPkJXeQoCq1BmqdlPJuSxmfJZQDgKPICJHFuVLlYzAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل‌زاده:
امیدوارم فدراسیون پاداش بهتری از دوره قبلی (حواله ۱۰۰ میلیاردی ماشین) برامون درنظر گرفته باشه. ما همین حالا هم کار بزرگی انجام داده‌ایم
😂
😐
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/91088" target="_blank">📅 23:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91086">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fb5b6817b.mp4?token=D_EBgmbyOljthJR6ZFOCR6IOO3rdjwmbhRL6s_HtX0_WPMy5BHG29ijg8jtcuOpoESfDCergpqsew2mr9UvqOckREH7pepII75FTzG7EOnNS6xJFAe2IfWCt3LBzJOVnxHSQEd3yQeQ_yHG9328mufGBF6ypjYeP2vbf1EFixzX-cNgAozPX3DKJAGMZ_MEyUugbXQ5twKZIE_HeD1xtvPwIhDk6QHVJAPjDs7Yqk2TDW_wcoGuzKRC4ZG8VGZSxi9P29t0keNoBzV0fAE3S1AzGKjf7rI8hJQwMkBIVtr7-999sP_QTtyyYk52h_MyY-5YiZYOjvMQvxMLa96lC5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fb5b6817b.mp4?token=D_EBgmbyOljthJR6ZFOCR6IOO3rdjwmbhRL6s_HtX0_WPMy5BHG29ijg8jtcuOpoESfDCergpqsew2mr9UvqOckREH7pepII75FTzG7EOnNS6xJFAe2IfWCt3LBzJOVnxHSQEd3yQeQ_yHG9328mufGBF6ypjYeP2vbf1EFixzX-cNgAozPX3DKJAGMZ_MEyUugbXQ5twKZIE_HeD1xtvPwIhDk6QHVJAPjDs7Yqk2TDW_wcoGuzKRC4ZG8VGZSxi9P29t0keNoBzV0fAE3S1AzGKjf7rI8hJQwMkBIVtr7-999sP_QTtyyYk52h_MyY-5YiZYOjvMQvxMLa96lC5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی در تهران بعد از جنگ خرداد 405:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/91086" target="_blank">📅 23:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91085">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNtgjoI5_hRyepjUn1stFLkpWQhCSjbzWZRgDVIbXG6DvgwWL_iDmjFltCTQfN5C0EmbPo2KoqYvThq4Wp9xCNZZZKCjucB51fjWTEHwNcOfsNvVjLVWE6y6wMY6tp088QByGU3KNR-yFviuugulbeINKpJ4iQhaPKMJ1qdKzpmwCs-qN1AKIkyNIBRFkDTBoVNzXULqmjmfPFpGNAcghP-a2FDWXwCNT6rSE__Gx1f5SC3gWl-DZTxOJiYj-M134WVy4bkv4ooYvpgjCDcJzj1tTbUKHGb-okeVpeL1utizSO9p6u0tPXaufMn24NqipstWC8CMlYeiB4-8ruOetw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
موزیک ویدئو کامل شیدا همسر ایرانی مورایس برای جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/91085" target="_blank">📅 23:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91084">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🚨
موزیک ویدئو کامل شیدا همسر ایرانی مورایس برای جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/91084" target="_blank">📅 23:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91083">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGBtkdv-VlQLCqo42BKCARb4vKt-4gzJ-_GgGbaWCm2Y4UTUkhYkZ6CuFYGwWc2T7XYAV1X_jupDLdm8F-vUrsKbUoOYzb-e1-KcERMfr-6LfySkmHezZD6eV6pOfzcHuGMZLDygcINp_4DfASkzatpqHYshzsxv5H5IjH9jv9wBGwPyNZlsEI-8da9_k-mRBY_wYmBhjU3YLRd9lQAo-TcnYPMa4V_QHm8vRN4sgiFrsspipXsnOWHhSsBPTeMs6RkqF6MxpvCK7bDEouFjIdUn_j42o4EeKELuQYh6d9fyLd6OnBUQw2Pc8nRMOpmUEXwe2s3YpsZpKbYQVeRQrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم منتخب بازیکنایی که اصلیت فرانسوی دارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/91083" target="_blank">📅 22:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91082">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9xZOkFeVfj8hA53P3A_aVd6xWJK72tKUgE59M3DYc8q9ToyuY_R4DRSphejHRy3NkhLrqFTrUYhGvPzXUAwWZrYn_66S01h8WvzVhL3OOE3J9fJkEJjPH7ZpGK2cRWbts1Rg_iWq7Zq7NOLkiARb09P_YKijKjO5WGY9kJtN3iY5j-GGyAYFwFmJAHvZz4KLVCb7x5rfRfVKPEmNhinVbhlZCXt48lMC8ltQKO2T7RQDYE1g9O4mmxpTsTkjccueG6CbDD2BO4f-_txAgbU8meunJecm2hBf205Ig8cP9XXrTwWOXJdQ3NH3JG32-cM1eMd867-N95uDu7wesht4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه تماشاگران فینال چمپیونزلیگ 2026 با یه بازی رندوم از ریورپلاته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/91082" target="_blank">📅 22:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91081">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-QQduZvDZjLtAPJZ2tBVez2rERTqi2ZHrmhKdl1h_1G8hbzLwfBVOAvfmBdk7EJFwJQRia9jROrAiaesPHpFlFZH5f_A4UWFIwbGrWuSuE_FSOK0yCOmTmhrC5BKl7uRxxyetw_C7dK_CrYFeoKlAsbbKz8flvThSMIOQRnVL1gvOkMgurZIkJvRiZywXgAmmO5DAQoWvD5FFwafCFFGAgmC28Lq1e52wFOtbYFnSmoZsUfQlkCmnWbXZm0LH2hMdI3SjdRcVeT9HFW4hjowx1AXmJEtrWnvztMF4LlHzF6FE_I1nQQV1mGO1j0nSg1YnoYRGIPUmU_hVFA1JEYMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برزیل
🇧🇷
-
🇪🇬
مصر
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه کلیولند براونز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
برزیل در ۱۰ دیدار اخیر خود، شش برد و یک تساوی کسب کرده و در سه بازی شکست خورده است.
✅
مصر در ۱۰ دیدار اخیر خود، پنج برد و چهار تساوی کسب کرده و در یک بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر برزیل  ۳.۴ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر مصر  ۱.۹ گل در هر بازی بوده
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از ۱.۵ - ضریب : ۱.۱۹
🧠
اگر مجبور به پنهان‌کاری شدید، مسیر اشتباه است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91081" target="_blank">📅 22:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91080">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRIHy6PoessbGiraM5lXtErrjovImjbgcB3GhjJ2Y6ARU4CXNCJzoJ_D1Ow4HAy_p4ilTowMc_hyF1gaPI8-Suof3X05Y1U0YHx-d72L5XCSitlQUjZvlPPFks2cCgkFuS1Swn6w3z2-G3PNuh647aKk7Oe5G2lgw9vf3H932OYtfGQJ5svz1YssDsjuvsaGob87E6cNO_w0jaarnt9atULS5Ggp1EWPsF438cqdhM2HeU0yRNGC42pnUa0w7Sx4aM1F7xvuAuMH-uHsGJZs2DTLDHgBoSYw4naM0zqaiBqNrBhsYvttVLL2hdE9b6d_Oj0vhrRo8azhPwOM3zDIWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکالونی: اصلا منطقی نیست که بگویم من اینجا رئیس هستم و دستور می‌دهم چون همیشه درباره تمام تصمیماتی که می‌گیرم با مسی صحبت می‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91080" target="_blank">📅 22:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91079">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3J3NMcq43ShpfjvzvJtmbDtOAkb1QbFj-FM1GgEnz5uAMw1yhKvaohAG9dbbh4XuAzer3iREJ66IdJjWd7QuSqLZfi1SCmJiMr_eudw9yITn2beiqE-EREivkzKwcmAULg6J_B9UxqthPf85RUewwYEs4E-43wJuyMSd3rtNFPfSSqsxMHoc9JDT6LwiN5w1yn_OE4Bvp6Z0PzIxmOfsg5UGMueJxBKqu46rfOGzDiFTiAoa0wCN0abv9U1XQGBnofSTyYTOndk2t0VzlGOUMPf4SFLBjIjrXHJ-JBPGAISCB79EqCg5cdd4AyG9RQiOnREWOErC9TnN6yuku0G_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین گلزنان فعال در جام جهانی پیش‌رو:
◉ 13 گل — لیونل مسی
◉ 12 گل — کیلیان امباپه
◉ 8 گل — هری کین
◉ 8 گل — نیمار
◉ 8 گل — کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91079" target="_blank">📅 22:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91078">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f50084c22.mp4?token=PZGUo2RJHH6wdFUAd_6h2LcqXt92hX2OfLW2Ne2agIL7_gtwyABOtCVCYKzjwD-Rsx9Q5DcnAQNMksRxF2euHA4va_kgtKeXP6jhFqyzV2LYL5w3bRszVxZHrj5q3TaqWtmWMfM80OO1oeNGoggr8KuHODa4E7Nt9RiKDlILWdYbuGv_tlkymgENwHqdsySCMrDvPw8EeXP7lWjDxUqjw20pM4BeXC6KwPvQJHplF-rqICIKdz2e2R7NqANY0Lbjr8dKQQJ_sHW6hnnM4t50ibOtSlbo7RehEZcQj5xSpGaPB5H35-F_Od91S6nbGy0bFTO9rM87rim4hOBZJqlR8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f50084c22.mp4?token=PZGUo2RJHH6wdFUAd_6h2LcqXt92hX2OfLW2Ne2agIL7_gtwyABOtCVCYKzjwD-Rsx9Q5DcnAQNMksRxF2euHA4va_kgtKeXP6jhFqyzV2LYL5w3bRszVxZHrj5q3TaqWtmWMfM80OO1oeNGoggr8KuHODa4E7Nt9RiKDlILWdYbuGv_tlkymgENwHqdsySCMrDvPw8EeXP7lWjDxUqjw20pM4BeXC6KwPvQJHplF-rqICIKdz2e2R7NqANY0Lbjr8dKQQJ_sHW6hnnM4t50ibOtSlbo7RehEZcQj5xSpGaPB5H35-F_Od91S6nbGy0bFTO9rM87rim4hOBZJqlR8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگر: بازی فینال NBA که شما می‌روید، ارزان‌ترین قیمت بلیت ۸۰۰۰ دلار است. مردم عادی آمریکا نمی‌توانند این رویدادهای ورزشی را بخرند.
ترامپ: می‌توانید آن را از تلویزیون تماشا کنید. تماشای آن از تلویزیون تا حدی رایگان است:)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91078" target="_blank">📅 21:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91077">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
رویترز : ویزای آمریکا برای ملی پوشان فوتبال ایران صادر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91077" target="_blank">📅 21:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91076">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqCYfxe6OcADKNaK1p0QYi2pFvNhLvCIK6-Bl0zWvdXKLunvL41vsA6mw2u_PAjZ0VHDwv_6oi1DtMfEShNVundkxEKBbtis7dY8fTJzW1Kdea6DDYkaHnj1Lxd_f4ukbouhEH4X02iR6G0Ntvyh_9yBk2VWaJaTVJRUZ_MKe-KCj7FyweUuPhKKYBSrjE6b5epXhrGFEoSRxmoctHe4fO5MM9mYlWLfh9EduqGda3DXvLlzvMNVrlTbYxEv0awE0l0It2OvJB_C2XGNieF1bZI8u6wCMRrCBjSA2FP6N04r-saZFltCqPYihOXPTDwldRwD_9HOEFE2Whqox_rAGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نزدیک جام جهانی هستیم و این پرامپت جذاب مخصوص کساییه که میخوان همچین عکسایی با کیت تیم مورد علاقشون داشته باشن..
Ultra-realistic TV broadcast screenshot, identity preserved exactlyfrom reference image. Young woman sitting in the crowd ata(اسم تیم) home soccer match, filmed by a live broadcast camera.She is seated in stadium chairs, leaned back, looking off to the side with a surprised caught-on-camera expression. She wears a (اسم تیم) home jersey with jeans, casual match-day styling, relaxed pose one arm resting on the chair. The jersey should look like a normal full jersey, not a crop top, not rolled up, not tied. Around her are other fans in stadium seats, blurred. Keep the crowd mixed and natural. Add a scoreboard graphic in the top corner subtle broadcast compression, digital noise, bright stadium lighting, and imperfect live-TV framing Telephoto sports camera look, authentic televised soccer crowd shot, natural skin texture, no smoothing.4K.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/91076" target="_blank">📅 21:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91075">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
انریکه ریکلمه: بند فسخ قرارداد ارلینگ هالند کمتر از 180 میلیون یورو است ، اگر به عنوان رئیس رئال انتخاب شوم او به رئال مادرید خواهد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91075" target="_blank">📅 20:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91074">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e998ac734c.mp4?token=T2U7JqPac_qGQKgC91zEymf3AW2mmL8_qhKR7wv1-TW3Y6Rg1EWEW4DMXDSNhrDbrtGi0G57xyoDToHeTA2aaAw7h9y6jDTjpkU4fRDTRSCnKnLNO7ITJPgxXxUnPBcbbQ4mYX3RTn26Mzdlie1gavdRYaqy3hWk4mtI40tvdDtgzIPGFOL7enhwhipLIQNTGCENXeV3UYS0hbu_2oPX09QKuwx-O9HENQMnEOEZf-XkmZHB32OWzJgvViqC8mFx5NmUXj_wCgNcUAyVOC07x-vvD9cA1gnduzw6T47ysIMRwYbcMuodNUkO_S2pf9s0bFmQ7gsv_84Pw2COiEASBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e998ac734c.mp4?token=T2U7JqPac_qGQKgC91zEymf3AW2mmL8_qhKR7wv1-TW3Y6Rg1EWEW4DMXDSNhrDbrtGi0G57xyoDToHeTA2aaAw7h9y6jDTjpkU4fRDTRSCnKnLNO7ITJPgxXxUnPBcbbQ4mYX3RTn26Mzdlie1gavdRYaqy3hWk4mtI40tvdDtgzIPGFOL7enhwhipLIQNTGCENXeV3UYS0hbu_2oPX09QKuwx-O9HENQMnEOEZf-XkmZHB32OWzJgvViqC8mFx5NmUXj_wCgNcUAyVOC07x-vvD9cA1gnduzw6T47ysIMRwYbcMuodNUkO_S2pf9s0bFmQ7gsv_84Pw2COiEASBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
وضعیتم اگه یه سال دیگه ایران بمونم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/91074" target="_blank">📅 20:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91070">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL43-Qin0uaccOAnrg8ljb7nwt9q9u-6cDT10wl9p-_0lEnthV3Ll4B22DO5jO93Rhw29mIp_wnROaQ4eTyBy2oyT4OvbFlRT_P-i-ImfSqQVO_xU6nDL4pbNhfWxEsFJanC8aI9UV7CzkzHuS42QoNLfH_WkWFJARKYBrijbEkw2Wc4alLzifayk4BT_hVClUhhm4yUAjX_fvQ29FRGu07y5MuQRc3oloEH7xtuT9OS3Zs8ntwrCkorRoF-pIUfME5iF3bBSm6O9svQ-bnuGo_upfz82TR2mxipWewTI2FePfEpgtC71vdRu72gsxhsnXElCDQLuM75CYiZbAtp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال یا وینی؟ مسئله این است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/91070" target="_blank">📅 20:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91068">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNKUYynMF0C7swtmNo-tsGu38Ww7HID47W-sPvVu75f2nNfedjoFJw3QjlMAphOuyZni-ENvAN4qQN71LbBilwp_CCNPWAwqSckExl1POP5qaSS7kbV1VU1u1GB6hwGVsXWmpb2OhxluSRHom2qWK2-8VkYrj09zJkSDVTLgaCzNTLWw8FWfik8iiA63rYfpiKNlUQZlHavhzjW13pjrpUwzD1MZ9QYXQ9XNtPrCHozE05HGUJtT_08VjfDywB7yRpKqbUuBqL7sRHZPA7CcNbsow2QbjNQGKNcLJngDGon96B-QeCWA2oCqsD6Wula5Qgn8DdlxBD1XJLM25XgM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iAKW9DWAMkaRIJoNzbsDlQcMu1iT9oOvfh3DDkGeaH4Q9MaJzNGdh6xtEX96ErJ4i5tDjYuteU1sE3dxooQfoJx7s0igZqEqTesW3BpsFYvFuwKtjrHwbqk5XKoDTGcwy-a6ho7BGMs5tgzeX3ellventb2EJ0iZUrTTFcZnmbiSRGQWPdCK1iID9kbqXmt8UwK9p7g3DHxm8lf1fyMsEUV4-YQPpR27DNoUGHRxrP4qaZuXlapmvdPGktiyQLXF0mBCN1Cb8nNjW14_U5Ffdt72KupJtIT3Uvgk5fk8j2ybm6I3utn1e7vSJbc_CMSQroWXvnI6oCrEMRTzcxOaWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز همسر فرانسوی انگولو کانته اعلام کرد که توی دادگاه درخواست طلاق داده چون فک میکرده طبق قانون فرانسه دارایی‌های اونا به طور مساوی باید تقسیم بشه. ولی مشخص شد که کانته هیچ دارایی‌ای در فرانسه نداره و املاک و ثروتش در کشور محل تولدش به نام فرزندان دو قلویش ثبت شده.
حالا کانته کسیه که حق دریافت سهمی از دارایی‌های همسرش رو داره. وقتی همسرش اینو فهمید سریع سعی کرد تا درخواست طلاقش رو کنسل کنه ولی دیگه دیر شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91068" target="_blank">📅 20:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91067">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzJ1ga53H389lH47OYbi1459jJoLFxDK0Vo7mOSNqLQgfRo0ijduG5Fe27sqQ4BJELr0J5f6diaxylrdI_mushFAI7rPMfY82YMuWqlCJBR2mz7zkj0LS1AgjnnNG9tQSoyu5LOmXJf5tUo5vKhOdpaP0yXigKaGwRRoV7JLzbEjKf9uYlCjjKgx4whV3MDfRmeG5X2nFr3tHPt7xSRE3_CNWCGNV5DsSgH5zEhmqfKZMmIzNWJ3JrDRn1bT0jt9x4JZS3SrFKSIFv3aWJlHun-VKnmiRVp0UUEYOQkzamje0r8jxIy8xGb5wShaGWLPpM9bf4w8vCrn4rXWIbSlXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خیلی هاتون پرسید بودید به چ فیلتر شکنی وصل میشیم !!
🛜
دوستان تمام ادمین های چنل ما از اینجا  فیلتر شکن. تهیه میکنن
🤩
🔋
حتی تو زمانی که اینترنت ها قطع. میشه  فیلتر شکن های شما کار میکنه
🚀
تنها جایی که مورد تایید ما هست و  پایدار هست اینجاست
👇
💎
سرعت و پایداری. عالی
💎
بدون  قطعی وکندی سرعت
💎
قیمت عالی و بصرفه
💎
پشتیبانی ۲۴ ساعت
💎
حتی میتونید. تست رایگان قبل خرید بگیرید
حتما یکبار خرید کنید. پشیمون نمیشد
😇
🔋
برای خرید از ربات زیر استفاده  کنید
👇
🤩
@irans_vpn_bot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91067" target="_blank">📅 20:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91066">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXRFjJatW8fq-A9QLKoh1tRs0-LEryA4W-TorPpw8H-rm8Nco1dDaQKuAChwm1_o_dA66Uny7fTkHMk9b12wGdyn-g8XHz95KsQtlYCbr4uGeIgNKq_c4AXBssKkOjD2qAnLXnPIYC1buL9Ic8cB9AT8h-NZH1RBEeuSgIxDQQ1DQ9fpZ58QXu39n2bUxHfyl4iIqa7aNTJRcHt2fby_jF4xtWq_akAjn8_fDDDNmb1KIlInux7dPna4LnpNmE9yfa7oyrJI7i9rpxnFSTVYOmTAWvkF2fRMiFKQ_8WzSZUu7xeMMWH7dzLZGhG774kUToDml_0s_-trqXSYynO-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
یواخیم کلمنت، ریاضی‌دانی که سه قهرمان آخر جام جهانی رو درست پیش‌بینی کرده بود، معتقده که هلند قهرمان جام جهانی ۲۰۲۶ می‌شه
⁉️
⏮️
مدل پیش‌بینی اون همه‌چیز رو در نظر می‌گیره؛ از جمعیت و تولید ناخالص داخلی (GDP) گرفته تا رنکینگ فیفا و فرهنگ فوتبالی کشورها. طبق این مدل، هر چهار تیم مرحله نیمه‌نهایی از اروپا خواهند بود؛ پرتغال انگلیس رو می‌بره و هلند هم اسپانیا رو شکست می‌ده، تا فینال بین هلند و پرتغال برگزار بشه
🤯
🤯
این پیش‌بینی چند شگفتی بزرگ هم داره؛ از جمله اینکه ژاپن تو مرحله یک‌هشتم نهایی برزیل رو حذف می‌کنه و پرتغال هم در مسیر رسیدن به فینال، آرژانتین رو کنار می‌زنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91066" target="_blank">📅 20:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91061">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egiucDCTQwvpFtUFEIETbJ-WCJ4NrB_vWHhe2XDO2Va7sMOu6Q91mzaaTT5-k5zZn9bwBtyJJt0MWij_U4zvJBPZyxhV88DHXTmJrDpaZYtaZ024d5W4UxhJAzbnMRcixW5yIbeEv2WIN_hqoB-5ZeBUNtYXQHGGDaWarNYlqt5VErEFSth-2M7x2V1LESvjmwid-Ei03FXgYSRsOehUT3XFRJw-qa2EH9VyZCXsGpPh3kpL1NaUQz3S_JTIUWY8Yf08FjV3DQ-aBgf3o1FxsKxZvcYsERM2gPK9Sjwy36ucxSmALMBkjTs-zGvGXUA9R7zIphMtwl_LpARfLF33oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pzeNLiY8l1m1WOw9akbaOrIsdpa8uwWPLxCwbyr23X8CXhPORGQ00ZDfUxE2NSHeCeKCeVyi74zhQqeq8bz5qGv-YeO9LzOFzphCUSlJzEPcYbETYP0cm0ryoUVHD-EFxLHEEKasCvv6KpefvTEuTGl45nPRxIsiKCqND-jNKz5DEoi8HcWj2hYkMLwbEg0lN69dt0ObBf3ZQr9ttE-IqGEUhwX2UUvs9X7ezZaLLQXKOrW7WHQxjyF8flI-AKgQ6nbKhPlEC78POLgmWyxbixrhCoCvAGZEiJtLIX6YeVU4PsDFzJL0QdUUWlW6VBYFWCrohvcgDh5yyN4smrNZVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k3LzQu2BoxYdXdhw2OJ5aAqkTrseaP1ZYKvEOTK8QQtbridcFnj5pgW5neOYX7HpKn6RoQeTKdw1rUb6w77QdgJeoCU0wzy_mhSDmmve_xEyCIi35mZecHGaYGZh6-wil9upYXrH49Op3jRrF68V9ykluFIQVcpvGGSoSSWOZjOOPqwt1pk2RZ0RROqaVLGjEuigxnuLrAKz9xhJ4azFfdi_xiw1ib52shvr5dXz0Tk9JyKq3HaxYVtTisidZGhhRqmYm997VhuHVHMU7funQn7kdQWwNiBGNkgyxJf_dI622lAG4UgCUPLUWoPycf_QLc2W3jxnG5jtobOSdr3PYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O_WA_GoDUVgHMPvrAI9quxItxLZ4e4RpdYMX-7Acqf2qwF-Vq59ksq-UX7Yx-z4pbba21LIHJMWGAa_EVLLwtobZJIKtAcnxrspCnU0OhXYRJ3MRfK91P9KUsj7op4ASnQlhYHVeEXhSXAZSsxUx7CjVJztfDtumuGSlQE8iJcSjiw2CHT9O-Pq5NaVZ2W2B7ygFdEgMtAr3wBlq9Xy04j64Einn3zEP7MzeMg6700gUSucPkjEW3o0-NSHU1wu1RlHUgFfrHewrRiWmRzNWs2k1YuByaIi8tieWwS4opuQH2-oFno8zxdXkOIyEPCW7erakYKFWg2ulNHk1Qobjmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
#دانستی‌های_جام‌جهانی
💥
با کلوویس آکوستا فرناندس، «گائوشو دا کوپا» آشنا شوید، کسی که در سال ۱۹۹۰ شغلش را رها کرد تا برزیل را در ۷ جام جهانی و سایر رقابت‌ها در بیش از ۶۰ کشور دنبال کند.
🇧🇷
🏆
وقتی برزیل در خانه با نتیجه تحقیرآمیز ۷ بر ۱ به آلمان باخت، یک عکس نمادین غم عمیق او را ثبت کرد. اما به جای تلخی، کلوویس کاری غیرمنتظره انجام داد: نسخه محبوب جام را به یک هوادار آلمانی داد و گفت که آنها شایسته آن هستند و باید آن را به فینال ببرند.
🕊️
🥲
کلوویس در سال ۲۰۱۵ درگذشت، اما میراث او زنده مانده است. امروز، پسرش هنوز در سراسر جهان سفر می‌کند و کلاه و جام او را که نشان تجاری‌اش هستند، به همراه دارد. عشق واقعی به سرزمین هرگز نمی‌میرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/91061" target="_blank">📅 19:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91060">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👀
#فکت
؛ چوآنگ تنها بازیکن تو لیست 26 نفره تیم کوراسائو هست که در کوراسائو متولد شده و بقیه بازیکنای این تیم توی هلند متولد شدند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/91060" target="_blank">📅 19:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91059">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1s9a26vfUtwb3muVVhqz-6PlIFtzAzGJJntSY7ToViLnINqMo2vJvpVvGfdZwN6vqoQAWTZPW_zVfH5_r4vnIsP862jwHOHhxrvdoKkrVOMAw-lawhc2_7AnY7C7yBBPQ8-H09XKuhBsSvkvhDVCkHU22x2-MFjbfEV4stwBgMz4xmI_OFoFkt8nzSdalHaFT7jTMkS9BgAXmt8WKwL_3tez-wg9lC2ilQXAshNPdyC5AHmOtgv7sA3Kve7B-J0nvefitPqrjOJeJvVdun-qLRrbz3pCNtGzzPqipDxuia2djcU_DeVkM8T7FMpCm9iPqW0WwTB1FvaQYlLTaDS-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارتین بریتویت (مریخی) 35 ساله شد
🟠
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/91059" target="_blank">📅 19:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91058">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLL_EM12dLWzuOHtUB1iU5Ll4sjEgFqxtfGLoeX5X0YrjzLwHHOaGSlYni2RDHkjTny_sTnxigB7PHcGRzlSN3xOQen-H-QMy5IrBl9qpCludkoKXr3YwwdQwetaTKZnib7jreALs1Rby3qMYLnsa-q_fjFtwgc2g6LgVZSO85kgJPlSqDBZshGPeTLUv-Bf-qOyyOU_QjLpPXMWFnBaGSqDLLuvU9iJiFVL7Abi0ZD052CYyLJIy0QxRwxIg2u-hc67Fqw08lBEpWjHAdKMuvnAsm1IH4Z0V6O91U5xoG0SSGEyV8J9FTfBJDkQsHfb1DyHc0mb5WytQFt37ozmAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
🏆
تمام فینال‌های تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91058" target="_blank">📅 18:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91057">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VShIh9DJBTRtHyofl4z-uEhnLCT3aLtndBvkT3DXRcP9tNOjAdKA-Z2WxBE6r-J3EjCE6r3gF2H8ukefMGptA8-WNmhL6aXLM7GH0ZV47Q7NXW_bo_XSNViEjVqfhVN8kwR3FkpRWCK9cfyx4KGxv9ceOldHLtZWV2BVjyKKrPByh4xab_T5lAs7Axar1KxAK4cSEc3TxGnH8X90iCarVfvtZtUZGtAZ_gbgybla1O455ov_N4HMWb4gke_pneO8SjEr9KZGhyU4KtN_jdK0ABBxFtljedDmHDHVZMPSFQopt5N_nnbQZBtsZA5ue7QNtrjPH_y3dIati4b5gYtTyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بمب پرز
گفت بازیکنیه که تو یکی از باشگاه های لیگ قهرمانان بازی میکنه
#بتیس
گفت بازیکنیه که هافبک هجومی بازی میکنه
گفت خریدی مثل رونالدوعه
#گاته
دادم هوش مصنوعی اینو بهم تحویل داد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91057" target="_blank">📅 18:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91055">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HmE5AmUjU_ye64y2zcP1BfowTP54NKd-9LV0cvPtsoRtNshw8XSMBeh340W8y8Ymg0MIN91SXCMlXMU-HoFQcgYOA5ccSedyd0AbFTZKtfjMREhn9BkOr9H_xSbqKGMikLZ5FSJv0UJu6W-Bt7CM4ln9t3wjnqMMdS0Ib1IFiktHs1dJwbUkx5cb9ZzpBTBBNlNmAww50WAB8Pn35Lw6CpA-U1yKucFcxveniGhB7Lxs3SzgrhMR0L0f8lKOEC6jM2IWsVaeLaK3lQpq-B90S9nclk2fUGfLHCaWa01O5QMLGtkvuIOuFCC9M5LUkuWPDlYVLY6xyJDuM0RIUZqVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULD00RV87RqpHt0-hyTnC2APBAOe2DDdW0xhpIWJrKWO1KEvWVM_mhcPwrBcjWZ61WKPHcQGtMJpfkDK541qgdcVqvTYroG6lioMUWScoaiZzcggu5uqPznTC4kplNIxQjMCEdB-i5L9VnpYfluwR5ve1yd0buN1mX5QY4KZzpfY0FqfiQ3sHnwJY0VQuRLynKS8OMxztehmuMB7DhsoVCdo4-dNvC6-PImdqnmNtNIQw2Ak3cPgKnEWSKnpX-C1ZZ8l10dmL-_qLnMBnljArrwrmS0uIBQdr0qydmoG1QG3fkMmoItJjWVL1UWyyd54o0vyBuV61bs-dGBYX7tQPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ژائو نوسی که هم لیگ قهرمانان رو برد و هم زندگیو..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91055" target="_blank">📅 18:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91054">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6ca25791.mp4?token=Yff-FVkMP-eZ5q_s1vaJL9-6SnVLzIjos_qSnxAQ_01Ksxr6OCQCbovBM59Rzbk7pPz184QxpdilWCYnL_xs5yB-sIbSMoa7EibT7_AWvOWMXDdVsD1Io4ZbKLT72eCDCAFJNMqA5t6ZPO3tYDPOoDx5m1ALSUEgoiSDn1_BAQY3pYuczaWn_2uATr-x7uyVWp7WMlC6E_BZGtXmGndkVGWMyfe36jkfu80txTz8ru2qk2IgCZQ91O_MFhGEiliKvbYKAx-VRnY9nIEQIJJoH7yObnZBehQKy4mMQGTzHKV3dSBwC7ihSyn2Jn4UAtJyMBtRRoaABIolDfHEdplJIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6ca25791.mp4?token=Yff-FVkMP-eZ5q_s1vaJL9-6SnVLzIjos_qSnxAQ_01Ksxr6OCQCbovBM59Rzbk7pPz184QxpdilWCYnL_xs5yB-sIbSMoa7EibT7_AWvOWMXDdVsD1Io4ZbKLT72eCDCAFJNMqA5t6ZPO3tYDPOoDx5m1ALSUEgoiSDn1_BAQY3pYuczaWn_2uATr-x7uyVWp7WMlC6E_BZGtXmGndkVGWMyfe36jkfu80txTz8ru2qk2IgCZQ91O_MFhGEiliKvbYKAx-VRnY9nIEQIJJoH7yObnZBehQKy4mMQGTzHKV3dSBwC7ihSyn2Jn4UAtJyMBtRRoaABIolDfHEdplJIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
على فتح الله زاده درباره حركت جنجالى با محمد حسين ميثاقى: چاره‌ای جز این نداشتم که بگویم آبش را بدهید آقای میثاقی بخورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/91054" target="_blank">📅 18:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91053">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gt4RW7olhqfVD_mVNUe01ya8Y6d7SW6VtsVSyswS1KRDKpJYqU0nz5D2f7B5XMr_yQedomd1zhVcRnS7ir3S1y_7kUXMTBwktkgLCYpvHAd8X7gNXCu9yFXPpSHuH3lopEJcQ-L611JCUqAQgLkQOJsmT0m4649BzeqkdjO9meoB4M5o_aEDGOigogUq9g9K18K78PgtO96MDceKUNCVy-Z8j2lh8NGrYXbXNamvZqlj1p9x9I4cbQ5y5ZxhIyRCzSw3Ga17qAL317niQYVP3-0x_Fm5obkVMeAtJTJI5ck8XaY7J5C_zA0i7xuHywc33Hcz5Gazko-kRFiaPZcKbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
کارلو آنچلوتی انتظار داره نیمار این هفته به تمرینات گروهی برزیل اضافه بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/91053" target="_blank">📅 17:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91052">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEaye0KnzEWVHmfc1S5055vVlw6iHTultptwEZbxyenmMnfXSyjybKugfql6_KGNR5hvcVXEOcpntlx9XT2XE2stTl5fwU4mJWegsNymhmJEpFMFVA60z8hjyvZg1270jnN0cwvzEv4n8LDB_2hxgmI9xsudVcvaQCyJl3wj0y8zzSFofs6uAZgTOSwHOZHfrFsjdKC34rTFQZhVEhKmJZvBnJ8SkG8Uj7EaFwvJ32MC_Kt3_f4jZSYfVfqsYJ5ITFtY8DpITfX_jWtd5uVSRqiv2OO68S5C-zGoiY6JkktvBBJdXptx12g1OeF5uXf0ugEGY0P2pjehrfzFfSjyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی قراره با این استوکا تو جام‌جهانی دلبری کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91052" target="_blank">📅 17:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91051">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
رومانو هم تایید کرد بازیکن مدنظر پرز اولیسه است.‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91051" target="_blank">📅 17:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91050">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fb7e52e0a.mp4?token=CX76g_PaqvQPYhXosK3mvU_5aZHKpgqn6cilYre3EPzoHzRfr57XaUgeW8l3u7wlsyBBJKFpLrAmk8j6tJeOTHVHq0-H7TAJmimzIxGdy_iD0dFbPbrqrFRHa8uZyiu6X7TdpTx4h9-YqfDvjVm9NSR-AfnrtdfdYBqrFVThzMt-Z5h0ct57HMN172vNEVOHXWBmYkbzxM0bM0jYetAyL5oH1ldnAJ5vW7iYtzuTMDSdXUdHS8PyUg5C8dI6j0uEysWuyU5Uj82OzJiGvpooQIonTukIr0PMlqYD8PrzjA4oVTBLhBXoPpY2B7vqt9cJn2MGE1Kkc_0EnzxmQbSUzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fb7e52e0a.mp4?token=CX76g_PaqvQPYhXosK3mvU_5aZHKpgqn6cilYre3EPzoHzRfr57XaUgeW8l3u7wlsyBBJKFpLrAmk8j6tJeOTHVHq0-H7TAJmimzIxGdy_iD0dFbPbrqrFRHa8uZyiu6X7TdpTx4h9-YqfDvjVm9NSR-AfnrtdfdYBqrFVThzMt-Z5h0ct57HMN172vNEVOHXWBmYkbzxM0bM0jYetAyL5oH1ldnAJ5vW7iYtzuTMDSdXUdHS8PyUg5C8dI6j0uEysWuyU5Uj82OzJiGvpooQIonTukIr0PMlqYD8PrzjA4oVTBLhBXoPpY2B7vqt9cJn2MGE1Kkc_0EnzxmQbSUzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
▶️
🇦🇷
فینال افسانه‌ای جام جهانی ۱۹۸۶؛ جایی که جادوی دیگو مارادونا و هیجان بازی در ورزشگاه آزتکا یکی از دراماتیک‌ترین فینال‌های تاریخ فوتبال را رقم زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91050" target="_blank">📅 17:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91049">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUm9h5Ds6ruhpzNTEhL3F9le8bgA1Qy6kOZm6kSB83jKDRSC-xR0QzLRw809IzlV5l1XGKEVk6SqHwDkntUcCoTwld2eNKWgfrWoGrraZDqYkxI112D_otR9ku4NxKnIFPy-46Tp6Vzs_o8HZGrq8adGENrFfVcl0J4wmYYolLbf2ElmDMJnMgFy1qSrRqOWeEO8zfocUtIdQmESukzYSM_zorTP98nOGwZLJDoITTrGdtmB8ZgGDno-X1D84tTMrhAkhkVxoYihp40_zFLG7g-YNd9PXjJxrAWgXPhRGbR7DDGggJzDNWPuiV4fYJwYEgS98mYfe5QkbfnUCfcOEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با تمام قوا برای جذب اولیسه وارد عمل خواهد شد. پیشنهاد اولیه پرز 150 میلیون یورو خواهد بود و اولیسه مطلع شده است که بازیکن مورد نظر رئال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/91049" target="_blank">📅 17:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91048">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b36cf84c.mp4?token=PFLMMpFQyr-r1O6-3lZ5wQX1Afe0j97ahZVUk0NN5obl_uf7g9vVwwpTTuic9DOD05kEt8rinfvDXcvg9xyCkKBdVRGLuSlhpbpi6Hz5EGJZ7Y8BcLUIHs9Udf7pePQ9IOch9qIj4vtKi2n8QSwwxedvzOjAB5M6onMaQ3BzXHZUQHak68N50tQ3UoMZIpJd5ToCiA6vpiUNWKWBP9Ir9yjnSWx7H70p-6bw6Y0G32Ooji-ARQqMKyKBX9civ4PL4Wol3GljUnXs6xSAPaXZP8gtLQiLARa9gVVck95rQl1SjZNe5q1je8TCu_JxVhXVHxhOWEZwXGVpkAd_I0c7yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b36cf84c.mp4?token=PFLMMpFQyr-r1O6-3lZ5wQX1Afe0j97ahZVUk0NN5obl_uf7g9vVwwpTTuic9DOD05kEt8rinfvDXcvg9xyCkKBdVRGLuSlhpbpi6Hz5EGJZ7Y8BcLUIHs9Udf7pePQ9IOch9qIj4vtKi2n8QSwwxedvzOjAB5M6onMaQ3BzXHZUQHak68N50tQ3UoMZIpJd5ToCiA6vpiUNWKWBP9Ir9yjnSWx7H70p-6bw6Y0G32Ooji-ARQqMKyKBX9civ4PL4Wol3GljUnXs6xSAPaXZP8gtLQiLARa9gVVck95rQl1SjZNe5q1je8TCu_JxVhXVHxhOWEZwXGVpkAd_I0c7yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با تمام قوا برای جذب اولیسه وارد عمل خواهد شد. پیشنهاد اولیه پرز 150 میلیون یورو خواهد بود و اولیسه مطلع شده است که بازیکن مورد نظر رئال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/91048" target="_blank">📅 17:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91047">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با تمام قوا برای جذب اولیسه وارد عمل خواهد شد. پیشنهاد اولیه پرز 150 میلیون یورو خواهد بود و اولیسه مطلع شده است که بازیکن مورد نظر رئال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/91047" target="_blank">📅 16:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91043">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDcB0Tc0dEUErN0rCCO6c46VC2zAMK_XYiZ-H8J62Utfehmf7Ak4pVUf2OF9RJ7FzOgdQLmM_z3tgpT85z7tOp6QpRqA1YM75xXmoQ2zkVueXn9oBh7RZjeQWPXdQl9azpUK6ysaO1I8djhMmmkGEpQKBlo7UxYtd0KLXC3aqRRx1E3s1hfuvEH1-zV9N4DlExInN84iiIcpQp-_htlg2eN5FTpRlDvhgIIfXCoYpVAdYjwFsRltSx23lJdWOUhpC7rR0YKnOfKRAQTokCMPgvDJVAct_QZ3GTtoJ7nv18S5bKf6fqWxij-FpVN4yR60bdes_HbqaYHk8aTjd6y4Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tnV1iwopy6JjSM-oNvJUk5jM06qLK0FLQG4zY5KsNq4DEt32tYcn6z_i2SHn--zE1ty8v2KUww82uiau4pWDM6XKSr4CXmTXL2FYXRMlX2090iGxm3hns9Zwp454Qz-rGPxdmA24IsOk6wds-zPogd0QO2VwKLmjIKPzKUQsjRHm740IoPm5HGpaC7wmTfBOKSf4YMNFvvaBEuDegcp0z36EJtLKfaKjNMC2gQJ5nPbke7ZzoMfp-PuqRp3SfUOFlQeixn8N_0KT6ItfNJAjpknehUtY4daPqno_kF0kr7I1X9qaEPOJEi3q4sEinLOkcRGML0Bf2w7LpcGTCUFnZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XUWZNFU8VdTJBC9uwUhMBbk7W8Qmef4wKIVT6ld_CFs9hYfsj2HuqBrwXWsUg18dotL4qJ0SDTFAlwx-hkNQOkd_3aI6fdmNq52Etk9KchRJDbDqfyaeEPUmv1m9bDFwoLre-Pj2uUzMWqhYwVJUeZvAfpFczb68wpn8UspREZ17-1tWNjInHT76q7Yq17w778oU3TF3IY6hOsbsaQdFs1u5jYBuYTgvCWKkglkKUEGEcA1iB50wG8yacuTYrN_kebIfjznsRoIJOB6MjQVEvAp6AG5JtNB61hyI1c_yvwEnOwVkXDAi2dzJ7ULiQD56SIhDUVs3tFiSt2g_0OpLlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CBIuQ6wedEmm8q5nt0GVA3gNlzGX_Sc1MXVbaUqyoqh-QhI8amG70N_BrUfgJTsQfine_bHzmE7oYnBFc-hCA9GvKxI3Ce96W_2NL342t80l66uxv5N9RJINQW0v3qgbeoBVIm-lRjKPwjHdYE_Mluq_5j5A9INZe35LRGzSQMXm7d6M0DKg1xpw6GpUvzx4j_betPlTSQdC46hp5ET5CEfXVrQy2-tmVqmlwuOOUjm3SXt9K-dmAchLMKjVApjkq5FPBrA3eIKYiWquXrd4vGF1jlqd88OcPHJA4JcIDYq03nJxEdK5YT4DLWYpQsAvzreIZlnxt6mUUdDNpD5wrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت بازیکنای تیم ملی نروژ در آفتابِ آمریکا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/91043" target="_blank">📅 16:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91042">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d407456a0.mp4?token=eHc3e92Cdk-kTVkGiODr3U6zMro1nPrISsaHHzF4PywED5bwxVjVKu-MwBPRJ8tJSftITm3Kk8yhSnsTJup72j3MXh8wbF-PxhKrcAhPXy-C7e-VjVGwMi0yMSAkd5k9I-uOa-t-rkt7J21Faaw4RJGx6tmRpAHl7wysfzOycXNVgCCEBOqeKiUaThLe2GRJfbSGjqH-czAnKTVjxWGBY-tY4MeG8kgQcOIBloYaDsH5vswpU9_3HdMfz4GEv7rZOSLDOvRAX7YwnGZqeL_jL-G8eT7O80gUJy46_VbScCLCHMn8P7bN8oDN6GmA7eyVswwpfVSkekr9D0cLKQKmmhZ0AaFEUubU19hfNCfjGGYvXZdFuGdlVts8KpBiSjknQ7ljvCmGR4Z-B5z20cS71Qisz4rMM3_WRTYeo8PTjDN_enrFyDcQYXvpEYaTeyHcebu1CvtXDZQoWJ2NG5pZRDjAIS7mpJ9SZC_jI6VUNodytDCAzJ9HZDoNfg2hR97WjCHcKDHzdGcjEnFToWn8n0aMXEPBdT9FZWiTbOxJBtgXBHc-55oCVCqXfVX1_8UNjxgj_VZASFWaforHJdNDaQwuZ2Xn-9Kgpm2LdVtTmPKtimYIRPBROc87ntsGzaCrLeaY46aRvHhExbsy1am2qwPlkIvApbqitXCBVt6dH8o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d407456a0.mp4?token=eHc3e92Cdk-kTVkGiODr3U6zMro1nPrISsaHHzF4PywED5bwxVjVKu-MwBPRJ8tJSftITm3Kk8yhSnsTJup72j3MXh8wbF-PxhKrcAhPXy-C7e-VjVGwMi0yMSAkd5k9I-uOa-t-rkt7J21Faaw4RJGx6tmRpAHl7wysfzOycXNVgCCEBOqeKiUaThLe2GRJfbSGjqH-czAnKTVjxWGBY-tY4MeG8kgQcOIBloYaDsH5vswpU9_3HdMfz4GEv7rZOSLDOvRAX7YwnGZqeL_jL-G8eT7O80gUJy46_VbScCLCHMn8P7bN8oDN6GmA7eyVswwpfVSkekr9D0cLKQKmmhZ0AaFEUubU19hfNCfjGGYvXZdFuGdlVts8KpBiSjknQ7ljvCmGR4Z-B5z20cS71Qisz4rMM3_WRTYeo8PTjDN_enrFyDcQYXvpEYaTeyHcebu1CvtXDZQoWJ2NG5pZRDjAIS7mpJ9SZC_jI6VUNodytDCAzJ9HZDoNfg2hR97WjCHcKDHzdGcjEnFToWn8n0aMXEPBdT9FZWiTbOxJBtgXBHc-55oCVCqXfVX1_8UNjxgj_VZASFWaforHJdNDaQwuZ2Xn-9Kgpm2LdVtTmPKtimYIRPBROc87ntsGzaCrLeaY46aRvHhExbsy1am2qwPlkIvApbqitXCBVt6dH8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هازارد، استعداد سوخته
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/91042" target="_blank">📅 16:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91040">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/QfCa1LIhpUACFU1BE_SjBvM8RFnsBVfIKrgSTBz-r6yGQzdKqU4HxqZWqsSaurd7sY3aC_aLsqPVtqrphdrctCoO8avVvqfKK2t5HBLR25f-ae0N5v4S8u2G8LMWcjR0T-1QqsehQFc5JORz5XIxQPu1tUCsE3o8S6Crtlf4B_NAyFkt_eAnGK3uEAQmno8NMRYNWnfIuGAUvCe_1DRvgnr-U_J8l-xGKLeNGbgfbIxdXNDu2k4f2iE8s3dYeMsWq_pKeIGaah561k9c2_rK_1vQIlqJRwfVra_gh1_yLrxeRZT_kLJaAWv_57jo4iw7m5GXFRqw_ZMKXH2awDmo5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
یامال به عنوان بهترین بازیکن فصل لالیگا انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91040" target="_blank">📅 16:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91038">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMEkYPKon8omn4-NS0j0zxEw6dqeXWdSciHyPNGey_ZJg0lwl_SLtoAc7gvVZNnX5JRHIsYOXWf1hr-2stE6ntNHZYdNQxdKn8zylfPA7VlyKGipJeWSsu7WjsPQ_SyDzCbwoQGPmkjYXMg-TpDNs87rb9L-A4r4Nh-pLQFijny3ouGE_8ghmMC6l4iha1FSl6ULKMVi8D4-IU-WIzxgIm6gh2hrxb-0vS6PTCCjMan7DnGauCWEbce_vu6EedLMUr_RVlL3iPrf0pCvIZCboAGBtV5VJnRkc3CVtDNXsnWhCE1TUH9UddawcMZcO2KXebCgSEXyu2TRgQXPFUocsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#
فووری
از اسپورت:
اوسیمن به بارسلونا پیشنهاد شده است با این حال فعلا جایی در برنامه‌های بارسلونا ندارد و اولویت آلوارز است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/91038" target="_blank">📅 16:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91037">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rl2nr1GYC8ZmVzUWXBl8e3A7H8Fbwd7jRH6_6toQWcZtj5kfn1kh4yExJEMD5v3XJsgk0Di17UdTi-YRQCRXnhOx5OQoBkX4dPLEDEgQxOW6x50Mqt4rfwQesnqau-lmB7PjdCLOigLhjq5_zSO_uhIqKf6lC6VV3vTctDziwtIHOhSREMFN4R5Z4LUqgRBXCYSDW-qOOqUAsU_8dg4hiagV2Idrwez3Tv0AvhXC-NJChgB_3JwYtyJxjh2Lc-bD9QAfOa_Rza24dgM6d5fs7wmlSivFPq365hzkMgeBDY-Pm2sfhsD8YB49pM5_K-1N3Rkv6VWOJmYKkl9QCzR_9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه یه زمانی حس ناکافی بودن داشتی به این فکر کن که برای سقف برنابئو 600 میلیون یورو هزینه شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91037" target="_blank">📅 16:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91035">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXalLQYQZ3ulSMMzpjvXoQSUrwH5nSNvCEUZw6hwXE5nHyOVTOZWMVvtN3iayRXohXo2ZE4-Ch-fuu-QJ83kTwfw9Zxy6O9vfcCZIVPr8srL_IWqRrLvfRuj12znTOHMoguI2HqOpItyMWJKkGWESHow-nn-eqlkGZa0N3Ox1qk7rLn-wuoVl77fkCROYFF6fJ0BpCL1n31cxFehtV2S9Ed6u3y_eCXIwtT1ey8PQKtbCpO_gPaY5mj51-dOCBEJtLbUWMPCBELmrUbr_Lfr4FjEDFwnukvtjff1OLc8pVAxynLxmNhVtk_KYsFxBQScy8Ebjc9C0BWpfUcJiyyPPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل لیائو: من یک چالش جدید خارج از سری‌آ می‌خواهم. لیگ جزیره را با دقت زیادی دنبال می‌کنم. اگر فرصت بازی در آنجا یا لالیگا را داشته باشم، واقعاً خوشحال می‌شوم چون استعداد من در آنجا شکوفا خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91035" target="_blank">📅 16:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91034">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e01837206.mp4?token=V6FeDhBieJrtjp3k1hnVsjW5JW_CMXWSj5HtjbEF3Et0oXxph-D7lLu7sEJmOyDsDoHgGau12NL_SfWzltoLKx_ag-ZaeHMv9KqtFCzck5YM2BuhbvEEjs-M3GxQIRp6OVuLXbfJDYMHYDTn-_IsVkdAAtioOWKVSjUuJtb6Bn_SDhBpQYa2xnPO_bvda25Ig11szyL25bixCpmSZPL7KT9AzielxzsTQMyOSGi99IdjJe8n4k2eusr-SoPNnYKaIc4pj5wY1QMH4sfqtkpzR5CwZq5q-t5Z2BDGLUJDXubKWCNkXxANKy8O-HVFt6t5RBkQVEQVK6ibhLHZpJR92w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e01837206.mp4?token=V6FeDhBieJrtjp3k1hnVsjW5JW_CMXWSj5HtjbEF3Et0oXxph-D7lLu7sEJmOyDsDoHgGau12NL_SfWzltoLKx_ag-ZaeHMv9KqtFCzck5YM2BuhbvEEjs-M3GxQIRp6OVuLXbfJDYMHYDTn-_IsVkdAAtioOWKVSjUuJtb6Bn_SDhBpQYa2xnPO_bvda25Ig11szyL25bixCpmSZPL7KT9AzielxzsTQMyOSGi99IdjJe8n4k2eusr-SoPNnYKaIc4pj5wY1QMH4sfqtkpzR5CwZq5q-t5Z2BDGLUJDXubKWCNkXxANKy8O-HVFt6t5RBkQVEQVK6ibhLHZpJR92w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
🇮🇷
یه هوادار مصری اومده به سمی‌ترین شکل ممکن ترکیب تیم‌ قلعه‌نویی رو برای جام‌جهانی گفته
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91034" target="_blank">📅 16:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91033">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ir9an82rg9JLqbw7I96fIiaHM_lWmqsUZ4l93owNbT9ALjLhN5iFqV2Upjv2AfJ43pCoDP3_zyoGoz7FoCL1eJ-nBMhOhceNA-6SKNpNqifq0xyWYASdcWoyj14C8S2O9ar1rYsaQA5qc9HJTHDOKPn7AwRP1DZn0NdQz9Ik8BZVRZtcJ9Obkio0H3-nZc1SL3YhdY4rzYIvcnatpotiESTFj8RfG25OZ9yYk5kRKiKNFrfmIPap6Zw-FGBdN7YKK8x_g2X2uYp37JGyVwSFkvpq_cjOFUxiqjCNY4qbYmn_OODIk49B-nfvNAixuxeWbWoX0Ys_yrqhtBbNisltyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اگه لیونل مسی در جام جهانی 2026 پاس گل بده، به اولین و تنها بازیکنی تبدیل میشه که در 6 تورنمنت جام جهانی پاس گل داده
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91033" target="_blank">📅 15:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91032">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-iUHRheJ5N5AYULZWhMsYt8FOhANMDkkP7Q5p8DSo81weip7KsguP4WFv1Rh1vzgW2pOWWgAiE_d00n9hVXJNN8lGh7IrGR6o_leuYrmj-i3M_Y6goqR2GiLx09ZTADnmIKelUMyR94b26bSiWwf6VzdDshpX5RjknvpQDJCzINwCXu_MSCcTAu4RNrGsEKCP_LyyByIAyWqRfEbre2TqX_p8zhziNHYsag8FOTrny0RalZI3idseQ1fz8pzZfBpkykxCZEqxk7NybQTYtkHNmMRxoDNyWiiXsqBFSOEf90E5Ssxqby7uk1tS2kvZ3Jwg0ez24oBQNrc4ohrCPftA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری و رسمی: اندی رابرتسون رسما از لیورپول به تاتنهام پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91032" target="_blank">📅 15:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91031">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niqd7cb2I_wkduGuTiZ4cxCu8vyRb4plBQXxVChou8XWmXi0tz_jqOJHezYBPCgA9aKWxmueyRDM0rO9VCN-God1ubIrd8lSN83FfqbTNotSAvhW7sRJ4vKYK2camrOYU2LHWE9035mw6jnFzdNuGDqNY_eBvofLK-F-f9-qo1jmLVJH0np2Z4rEAtHJZqnhKcj3TAHL2Z4X7WB6-7J7zvQS3cWTjQezeC--5DdU-SrwNS3OuxgAlI2PgB6YxVgEClXf0w3KCsIg1KLFqW18fxKC3X9vXT0Y0P_T6cMnpawVWEexAgvF4zlW0FX0Dlpr3UZhSXlOrUoKvv5aGIUB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏆
🇫🇷
#فکت
؛ در جام‌جهانی فعلی، ۹۸ بازیکن متولد کشور فرانسه حضور دارند که فقط ۲۳ نفر ملیت این کشور رو دارن و برای خروس‌ها بازی می‌کنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91031" target="_blank">📅 15:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91030">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40fb78b5f3.mp4?token=YYB8lAlNMjqaSkB-ZtqCIF16Sql1w3DRGOlXb5iEjNDTVQbZW0tLKm4aDtgOPnueyQc-L3Az_FkL6C3jmUHAY93fGOignwxqSh7meFvMp_2n9DegY9i-tA_3clkzetcLKc-ddvJOwNd7Ak1zsaZqXhUyuwH7BYwm0lCMW9aG8MdUm9rPFwFqURC-4I3vn0DRazgDkK2b-ihtc0Sc3lNlQ9b66dpHn725DonwNPFhYfA-hypOXQxV3DRHTGCL1tpuQfswvo4gr_zlH9sNUGxlZPzm1Yx1s1XGbMg_5dM0j_7NpTdZ7Zd6GDi-TikgSfIEDzDg1a4VWeJfiuPSzoJn5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40fb78b5f3.mp4?token=YYB8lAlNMjqaSkB-ZtqCIF16Sql1w3DRGOlXb5iEjNDTVQbZW0tLKm4aDtgOPnueyQc-L3Az_FkL6C3jmUHAY93fGOignwxqSh7meFvMp_2n9DegY9i-tA_3clkzetcLKc-ddvJOwNd7Ak1zsaZqXhUyuwH7BYwm0lCMW9aG8MdUm9rPFwFqURC-4I3vn0DRazgDkK2b-ihtc0Sc3lNlQ9b66dpHn725DonwNPFhYfA-hypOXQxV3DRHTGCL1tpuQfswvo4gr_zlH9sNUGxlZPzm1Yx1s1XGbMg_5dM0j_7NpTdZ7Zd6GDi-TikgSfIEDzDg1a4VWeJfiuPSzoJn5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کلیپ از یه عروسی توی کرمان وایرال شده، مثکه رسمه فامیلای عروس اینجوری فامیلای داماد رو میارن وسط و با چوب میوفتن به جونشون
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/91030" target="_blank">📅 15:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91028">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qYdpOD_AAYGNCrJ0tUeJUf2PzFVxk84TK4fifeMbgbAmJNIpERtftHGihlgdxBjPJ_vCjHXDk66xdlNw8GPRr0-vIOI0HEoODYxQnCT5MdPeTaj0UZVVGh2x0iO2mTU3FIOIcYThCa6RbS_7_L1BoEmWIdB9SfGdu18qC54RwGcIvI0KyS5WcXY8_-9OL1jmGOUsOG_ts38uLFIvo4R5wqXO7YdEI09QbFjsE9Q8PaF03gMvrp0nFWDjLefEeYKVDmRRa2z7HzvHy8crsUiW-yAtu1lSFzmiuWlxy5wysGLJcVGh-nqCLFWZNS4dsTNCcJ4GWMsWU_Qz_HH66vHtYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YFzYxDcgEqWoCBua4so8griv8Dj_W0XtrGrCujSrJnbeLWRM5I0AlkiT9SCrqFsKttLIm_icFGWJSFXxZwVee3_ClAPkpENdtj1R3RB90q46LwQUDlXloWgQYZhShkv8bmgunePxuUZHMT9PZhYz3ne4zfJxd46SlB4drz6McEy_85HQJ5TJ0idu1r0OgvaPv3DNKDhaJY7GboZjZZyacLiOjxdBb1hbNDIGm5UNOwVj6EcujuA4z44u5vAa8c0ZjjEDSYtBahb08KufNM1i0PKB2FbC0-fh_xUHE87oDpnQDxCFiLfUj2pwxtTalEiQ-T1ktUVt6eUQzwYFRgNdoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🎙
🇧🇷
جسیکا توگا، دوست‌دختر سابق وینیسیوس جونیور: «بازیکنان سیاه‌پوست همیشه از نژادپرستی شکایت می‌کنند؛ اما همیشه زنان سفیدپوست و بلوند را ترجیح می‌دهند. هرگز با زنان سیاه‌پوست رابطه ندارند. چرا اینطور است؟»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/91028" target="_blank">📅 14:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91027">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c893a4439a.mp4?token=PQbzhCYbc9uSUlIvnSinKjIstDKnpBJ5fgJN2vD5oKk7rhroTJVBS4W690D6zkSJjuxxxec1qgA3uPiM0wTudc4PH2Ro4zXBpSiq3CCQEs9QmU_YxJbSEY0VVBlaLCZs9b4buXW6ZIjqIktQKeR2IVWIcRoEgq7BUTdamxPA4PXEmdeOC6FzRY-sdfvxcjH-q7LICBRE0eN2gEl1niaD9M94YlUoHlXSaP5n9Fs-mfZeqD3tL3oV7iQIOqjGwigBzhbnOpQNlrS9gCW08cPS5PdS1RksXN0JTATxwMZ83MC7sXMJ-8j_vAs-rWgzrPTPSMW-NDmSFsNY5ZOv5IHkEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c893a4439a.mp4?token=PQbzhCYbc9uSUlIvnSinKjIstDKnpBJ5fgJN2vD5oKk7rhroTJVBS4W690D6zkSJjuxxxec1qgA3uPiM0wTudc4PH2Ro4zXBpSiq3CCQEs9QmU_YxJbSEY0VVBlaLCZs9b4buXW6ZIjqIktQKeR2IVWIcRoEgq7BUTdamxPA4PXEmdeOC6FzRY-sdfvxcjH-q7LICBRE0eN2gEl1niaD9M94YlUoHlXSaP5n9Fs-mfZeqD3tL3oV7iQIOqjGwigBzhbnOpQNlrS9gCW08cPS5PdS1RksXN0JTATxwMZ83MC7sXMJ-8j_vAs-rWgzrPTPSMW-NDmSFsNY5ZOv5IHkEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
امیرحسین ثابتی نماینده مجلس: آمریکا بعد از جام جهانی سنگین‌تر به ایران حمله خواهد کرد و ایران را تبدیل به غزه دوم می‌کنند.
❗️
اگر دوباره سایه جنگ بصورت جدی روی کشور آمد باید پیش‌دستانه پتروشیمی‌ها و زیرساخت‌های منطقه را بزنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/91027" target="_blank">📅 14:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91026">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7143a2f59a.mp4?token=DIVnNfYojzCn6D8xU_EpZmGZUgDRZCsE9k41UHu9jeI9A_ovj8KgNPPEdvjozSezc1jbMpb_poQRMxpMTRUWtYHpjYxqqFE3okQ4Qw0c-quGCIWR1YLZwntGJYaABb6l0rt0oPGsn-LwuzEeHo7TwkgH8Eovh-EDd0fKAg3ep0wNnKcLPKkYwliy_sQRqloGsVGAqRWpDP3PzgSiTGkJ8L5OJhN75_u4farY3bhJMTplDpIqJgx4gOxMrSSCGiG2FRZGPx8vP7IxVsDCFLqCoxxKdveVnWCcmo2BA5PI8NirjTaFlZNJx2k5kvXl03R6ZRRFioFf1q0tKLpona2Btw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7143a2f59a.mp4?token=DIVnNfYojzCn6D8xU_EpZmGZUgDRZCsE9k41UHu9jeI9A_ovj8KgNPPEdvjozSezc1jbMpb_poQRMxpMTRUWtYHpjYxqqFE3okQ4Qw0c-quGCIWR1YLZwntGJYaABb6l0rt0oPGsn-LwuzEeHo7TwkgH8Eovh-EDd0fKAg3ep0wNnKcLPKkYwliy_sQRqloGsVGAqRWpDP3PzgSiTGkJ8L5OJhN75_u4farY3bhJMTplDpIqJgx4gOxMrSSCGiG2FRZGPx8vP7IxVsDCFLqCoxxKdveVnWCcmo2BA5PI8NirjTaFlZNJx2k5kvXl03R6ZRRFioFf1q0tKLpona2Btw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت امباپه در ترکیب فصل‌بعدی رئال
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91026" target="_blank">📅 14:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91025">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z992-0VOGWG9mP5Aie9uQmOZnXn_B0IjbCZ6NnD1AuDWTgRMiOzYEPb0s0dhi78ks6jAz_68hLbp9PWWZ62g_S6gj9EPRSqCa1aCzi-aVpjpU0fLVFJCGZx6lVpDqUiUog3q_xTEbLRuhkNp6XqdHmM2LO4zrQLjKalIgTpoYtBg-fn7CuIH7JU0KpLYsuYc2QMa8gR8vn0pJ9Sk8GxZLu2mi3gDvXQm14KQXWKErs1_uecJrbhVWdqajIYCXCPh4qvxAv1II-CjS07ldcmqYeIEOr-Mu9ARkIO8JU76lLnNf0AoxGDBCMyTYv587DhJnZmpmX4-G_L0O-bfAd_uFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تلگراف: با وجود تکذیب‌ها، فلورنتینو پرز برای جذب ستاره بایرن‌مونیخ رقمی بیش از ۱۵۰ میلیون یورو پرداخت میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91025" target="_blank">📅 14:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91024">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری؛ روزنامه تلگراف: هدف فلورنتینو پرز جذب مایکل اولیسه هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91024" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91023">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qn2fvOAAl7DEw40SC9vsccPVVudUOU8W41UtTMuMP8JqnMhwWBfITGKDjKE2Cj5cgxwTPq6R6LgEkv7cszqpFCw166s9_iSZgJ9tewla65-XntVWBMVPZOJSfPJDGSfbRn7mS6DBbw8dt_lUizarglbqyazUSyIqKmRno7K-IVHEOWBtz9d_7kgBVliiiF70Jjrtn6xDklatyumdJbm6bqYUJW5wQ0on_4SCGl-FLhw25H-dUzQF5Dh35KNtzLdmOsYrrsBMELlbQ1_uo56nXOiEEKi96VvM1t2TPY3ugIYOAf6CspvrKExT98GGr6y6hNtXnTHA2Pj__P5R3j2LIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری
؛ روزنامه تلگراف: هدف فلورنتینو پرز جذب مایکل اولیسه هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91023" target="_blank">📅 14:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91022">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EASHcfGGZPLc9MVXhHN1szuSBXMus6X2tY0u9uoF3whovlZdS83nPCAkEu21hvoGSYdsAFSmwgIh3G7a1aY5q9vTX3QKPoFXjO3RUGk7KKDuEsDnA27u6MCtjR0orpGEe61UAryTii-9V5kzpLm-5w8VhKlHoPR_AzjL5JS-qfvPuCYBOEqZoNuP9slUrUoOQ7dILfM1zwMYArTaFgv-CFwJOubehN52db04MiWH6qLHgJqivmpf-71qzr_erMdUKWz3zsDEYclzPBi_fEBDdFWs2dLqV8yg9yfCCYjWe4HL-FvEyWOBC77vySOICIcPXPTnIFQCR4IybHzJr0gVgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی چوپان هر چند وقت یه بار هوس فحش میکنه یه استوری میزاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/91022" target="_blank">📅 14:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91021">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e1282030.mp4?token=Ec_c6CEo444LpW_-pWiW4nejgdUmaLVcj9iGplwiTDWOr56Yl2NC78wvH-tRlqx3ornT_cW-LLrbSQpDnlkrlUnxEsVGbuDsMUfcWLIfuRd3lPx8PsCWMdyFLFg51KwydXByy7IOPWSeBRi-gFBuX8wSASKPDmrqWN5w2y7SPQlGYZx2UIeL9QmpDkwRCag0C8XE7VABe-QRH6Pum3jhHwse2g5SCOxYDi5BfZhKIcmZkLoIbBHMuDbHejs2SAbxz3y1nB3TpvKBDaU8-44Mm8SNnCLvTNOT0MEV2XpD3XQzIG5m5RxBS-_kbZl_bQkJCgEcOOJ_O0huAkTBgDstzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e1282030.mp4?token=Ec_c6CEo444LpW_-pWiW4nejgdUmaLVcj9iGplwiTDWOr56Yl2NC78wvH-tRlqx3ornT_cW-LLrbSQpDnlkrlUnxEsVGbuDsMUfcWLIfuRd3lPx8PsCWMdyFLFg51KwydXByy7IOPWSeBRi-gFBuX8wSASKPDmrqWN5w2y7SPQlGYZx2UIeL9QmpDkwRCag0C8XE7VABe-QRH6Pum3jhHwse2g5SCOxYDi5BfZhKIcmZkLoIbBHMuDbHejs2SAbxz3y1nB3TpvKBDaU8-44Mm8SNnCLvTNOT0MEV2XpD3XQzIG5m5RxBS-_kbZl_bQkJCgEcOOJ_O0huAkTBgDstzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شهریار مغانلو:
میخوایم با ۳ برد به عنوان صدرنشین صعود کنیم!🫪🫪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91021" target="_blank">📅 14:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91020">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cf842d659.mp4?token=dnHXSj64uy_ie778e6EMLbnXImDcfy_zKKvQ6bJ5vLjQKQvW73U1PGyBa3TaSRhNr-G6prK3avZH8XGlLybaItj610vr8bFjo8nF0pyli14ujy7Aj6em6K8bdL1EpBE4Q5kNgUsyTaaShybBagMQqR9s6p2QrZ7eRqjx-eeovcbBgpVRwZY-SiUSWsuF_d_-U6sirhvrK30m7mYGOe7XkXtzn2fr-3T9YkFlYctSsJezdFy5FyjPIaqtztE5J_yX504BimSmDF4-eLY7pCCaNhrrS2wWE1djq1q6uxSY2cBcRtSKvVO4zNuZre2fEacZBJ2qEnKoSEHNPKiX4hbJkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cf842d659.mp4?token=dnHXSj64uy_ie778e6EMLbnXImDcfy_zKKvQ6bJ5vLjQKQvW73U1PGyBa3TaSRhNr-G6prK3avZH8XGlLybaItj610vr8bFjo8nF0pyli14ujy7Aj6em6K8bdL1EpBE4Q5kNgUsyTaaShybBagMQqR9s6p2QrZ7eRqjx-eeovcbBgpVRwZY-SiUSWsuF_d_-U6sirhvrK30m7mYGOe7XkXtzn2fr-3T9YkFlYctSsJezdFy5FyjPIaqtztE5J_yX504BimSmDF4-eLY7pCCaNhrrS2wWE1djq1q6uxSY2cBcRtSKvVO4zNuZre2fEacZBJ2qEnKoSEHNPKiX4hbJkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇯🇵
ویدیو منتشر شده از زمین تمرین کمپ تیم‌ ژاپن در مکزیک که کیفیت خوبی نداره و باعث‌اعتراض شده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91020" target="_blank">📅 14:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91015">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rl1eULK9HSYLlsz68yn9LVCFTbX3RU9JLbFiJKfqqQpxaD3hIsffP-ZM-QnnsDS-hmL0QhDzBDXpBaYrKCRX_kyHGr_66J5XCA6u729sPcGp3-xrEqBUpdxF7z2o9ntpfl1iM5JXpx9_CqiRovByXDqLv9cnRCw25jR0n9vK48Dzia5K7JaH199gCq7RKOTXl7mgyR1ME1eo7SNOPNAv05oJXTUOmE0IWHWXOMj_KtshEbG9YLqwPqzY1PtTZQYY1lXUCm0U7pObolzDIoWa_2cbQIgNO-Wc3PsUR4E_FLv2yJKNxzXLSdUtgryGySbh4UXmnGQ99VfZ-ByS8S_Gsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UP6U7cH06I70sHgFOXD6OUJR_RCui8WLpGdXhRzukNRdGSavNaozbx0QRsGBVtpBWKU3kSezP4MITmQoHgfq5wvVkc831TRfAsAgq9gFkrGhfwWWVxG5p17j5aUeLPex31G_uJz3o5sk-KdHQdzmDiygNT3xFSwiXVnlvrTGocZSQYU9gl5Ks-W1BwJoWKEnKFWr9B2eJYXQiUYnkdxO0OsLa_tKkLTAvTQdb0ALBXD95q6WfYBXRgmV-pBChICHksEFWcQhdl8QZpwB6U-wQyZxlMj7SFyg419cGp59vaxXe9GpxSMEwbqqy2Oy8MvFBGDDwHXhzjIrS3uytgvTug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ay0G38H0PpoXUNfxsbRn3ohuweB4A-Vzp0viTbrAd2GzXh_1BEZNNHiK0ySBj9X2vyjbBuuWAIIYYPt7gdgxemaiLrnLN2G1HUOaFCPOEIxIfSRq141r7UqSzDSZ2FKgaxKxyRcPtUb1ZmoGtuCuwe5m70pRDACZX1mKUboTA9ahhBopJIKeeOb1fmUqYCCH8l-dm2P5nJfsgFROaiCY1-ooI-Y5RyabhNXCwVz283a7xSSKe17yfWuo45d8LJ2TwCisNTamIQYYlZWjlNVUZlXQ3p0rCTyThJCE_1D2itOGWtQVmKNF13O05WRT5e5A-e5ESQpVcWobcJeFodcAaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B6nwdLiBqUolOUH8RR_0p7OWEVLJygn7BiVUzswqfGvp9ffMbUKc-owVHa85UpPh1qAg6GVZpyyAB6ouKVjZi_y9Cg6S95CGXEm65hDVWTlSRnDQQT9zWLZf4FkEjRJfAMnPMSmgQfIRtoJl_3p1s5Wpxz5Aj_SkAkadG11VXXhgiqRKM3CHT9tAx8iG9FUcFme8FvK6BmiJFLBjQVNCwZ3E9B-iTiHZ3QwlZaVeu07y4LHyy4hE4Mwio4-p7Gu14SbbVwqvAzH2bvwK5hqKniOHa7VlLPwJxrjBokxZ2x3zuuZyaTiT_YPmimFzsVU74DE5VPavEw0KVdijtWbgIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIpsnoS1DM9MUZ-A8KQw8HOarA-37w5OjvZPYKqolZjKtz_3-qes_T16e_rT_Z1PUxAmF2NxKY3WIGMr29Z1je2w__pNaaVTDs3qhiXpCTtIE-rzTClklIoXadK767xTIrWYQNFWxfbWtVSVf-fnG0_2cPmwGtMimxaffq8nvk5qYRhtanzevOj_cldxquWCcPo3GY42-gR70V-cbM6zLSUHPrmqrcrutso9lthKNsUFxuFFdqeXODnZ2LbQ6wBgeJ7JRPgd76nJOQHH1SQInUTWYHOt-2zJK5_WvWoZOO_H8Oc7nEyk5wbNcd0luq5ENAKfO3TyXkWn73OpMHItaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
هوادار روسیه‌ای در انتظار آغاز جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91015" target="_blank">📅 13:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91014">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8abc04017.mp4?token=SfQeAsnnDDLi3qU8km2HqpKY-NP4elm6Z7smI5Pqi1zhJFRaWr5CTcLiaBIqg9Dpuoj23Plt3TOSDzrZjSvqoTuK1-KuiS8ZYyA_RplCRTh84X1_Gmgu4xuGFsv1ac83Lxr56TxnWinIpO0GEaCRu97jaBe6n3nBYQoCE35TCB-NMPiH8i-Xpb6Be6NxnY9eJRiQzcMhM7jKDzD14f6AZZnux50QdE3Ou73jdOGPUQqGiPXM3hD0CZ2cfUYv7DCc3QgcSD0XXIASzdy_bRFEJ9WfSOBwSX0CYUdMU8O--6cPCjpHGLrN_i8HyXK-ZVCLeUVw-8PNvdN-BOShHLlKQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8abc04017.mp4?token=SfQeAsnnDDLi3qU8km2HqpKY-NP4elm6Z7smI5Pqi1zhJFRaWr5CTcLiaBIqg9Dpuoj23Plt3TOSDzrZjSvqoTuK1-KuiS8ZYyA_RplCRTh84X1_Gmgu4xuGFsv1ac83Lxr56TxnWinIpO0GEaCRu97jaBe6n3nBYQoCE35TCB-NMPiH8i-Xpb6Be6NxnY9eJRiQzcMhM7jKDzD14f6AZZnux50QdE3Ou73jdOGPUQqGiPXM3hD0CZ2cfUYv7DCc3QgcSD0XXIASzdy_bRFEJ9WfSOBwSX0CYUdMU8O--6cPCjpHGLrN_i8HyXK-ZVCLeUVw-8PNvdN-BOShHLlKQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
بانوان جذاب اونور آبی موقع استادیوم رفتن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/91014" target="_blank">📅 13:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91013">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b018b6c88.mp4?token=poniH51gJSmvTOC0tTqQ8BWLs3A6HuzdFy1u44JiQpmOJcTz4TqrIb03kaoRMmrfUkH1QJloe5neNorPkANr9skxN8b1ZC27yLNX06G5vv0ZJWpZltACj1ttYTOZ4-mk6sRQpqqzT2GXm2iOztoCoftHVssgw0Mc7GhA9R0LkOlzwrLKXpwTLQaN_MKqFnIensKBmFAIxxnmD3PiADXdYplnEu6zSspqhalB85g5ebKwNh_8f1-EtoihEb-l3eYVYCprvPjWlYk15rZd94r-eHgCXsbZm-jZ5Twlkn5vMWaphocMRj2BoxZFwXGbGbQPfA4y1hXp47pjbFu0zckjYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b018b6c88.mp4?token=poniH51gJSmvTOC0tTqQ8BWLs3A6HuzdFy1u44JiQpmOJcTz4TqrIb03kaoRMmrfUkH1QJloe5neNorPkANr9skxN8b1ZC27yLNX06G5vv0ZJWpZltACj1ttYTOZ4-mk6sRQpqqzT2GXm2iOztoCoftHVssgw0Mc7GhA9R0LkOlzwrLKXpwTLQaN_MKqFnIensKBmFAIxxnmD3PiADXdYplnEu6zSspqhalB85g5ebKwNh_8f1-EtoihEb-l3eYVYCprvPjWlYk15rZd94r-eHgCXsbZm-jZ5Twlkn5vMWaphocMRj2BoxZFwXGbGbQPfA4y1hXp47pjbFu0zckjYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای‌کاش اینترنت وصل نمیشد اینارو نمیدیدیم
🙁
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91013" target="_blank">📅 13:00 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
