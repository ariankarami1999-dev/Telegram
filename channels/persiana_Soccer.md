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
<img src="https://cdn4.telesco.pe/file/HlVACjRpQNce5LZrKAbtuhmVlQr4bU5kL1_u3beGGr8dZK_WLfQh8bfr75flo-aofB5fWvDj_jAIyGUC4OHjWh1namIO6kbbOOmmNe8G3aa9Qtr2CyLoUbBu5zb26o47QIw6zeIgyiZfw_M9Y0aeiVmBMGFc7U71_jTIxI59FDqdlaNOwx0v_ZrzH-C6j_aU2jOTwLlZGQ2QTJb3W9zFm2fehpsyDwSDrr_0XPOQqwOsZTSr2QYoIPp3xBlW9buD8lbMV99jF1XEUABndeBLdrwlpXPQIMJaAvViZbrNy3os4xcofH6o-rrNJfvmyGyMLgksK08n9rRzZAto8aHuuQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 613K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 01:12:39</div>
<hr>

<div class="tg-post" id="msg-28357">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyANJEs2Q1dGHOKYz9vB_1w7LMB3AOo6oPYDBq1ljnPrUAQurRh49Tgh65n4SpxgKbtVVLGoMX3J1PH2agX66qRq8NI0GKpan5YzRCGKuWXNMkOACyOW7UHsqtnxqu9-REmOkDAO0HMFY833qYf7s8z9flVmM4kA8FJy6kzRVd7FYWM4AFrI0kRGwddilm1LrzhFrm9-0IGPnUkExjo4oyiU_YmeuvmfwioU50HjvuF9fkvFGkAEzs4obkVcg8V8kGN1XxcCFIl87VsY7uBivSFravOijMR79xxVbGjcYcAk1dtT8RTWOch_7ClBdo-zx4R7z8wQaBlNxerplROH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لالیگا|شماتیک‌ترکیب‌بارسلونابرای دیدار امشب با الچه؛ ساعت 23:00 از پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/persiana_Soccer/28357" target="_blank">📅 01:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28356">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da75343e43.mp4?token=CpxrhV4jJm1Klhta9XwukPo2cxq1LKix-avlfI79mMhhso3CsF356SFQNuaTmstqSgregxID29mLxlcijANJ76I4dG6-BobFAKkDsgP3-UtnSxWT5KLokEJR1jGTzyEF9qdCIhu8l3JK0Pj7k3VUCLwBP_0WqQ3biWZHfJATVrVaKYUfzf0ui87EBatOCpB3ZLyemjub4fkOSuapvrJSq81uClVkviYXPYW3eC58x98PKb61oE55lSswfNR218JfTg5ER5ipbP0En4WQwZopRM2PoGDyuAhuSL-EZCnLr_77AyWIqtczznmwexm5pKeE4P4ddUw52SUhbHP58p-TEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da75343e43.mp4?token=CpxrhV4jJm1Klhta9XwukPo2cxq1LKix-avlfI79mMhhso3CsF356SFQNuaTmstqSgregxID29mLxlcijANJ76I4dG6-BobFAKkDsgP3-UtnSxWT5KLokEJR1jGTzyEF9qdCIhu8l3JK0Pj7k3VUCLwBP_0WqQ3biWZHfJATVrVaKYUfzf0ui87EBatOCpB3ZLyemjub4fkOSuapvrJSq81uClVkviYXPYW3eC58x98PKb61oE55lSswfNR218JfTg5ER5ipbP0En4WQwZopRM2PoGDyuAhuSL-EZCnLr_77AyWIqtczznmwexm5pKeE4P4ddUw52SUhbHP58p-TEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ عملکرد حسین‌ حسینی دروازه‌بان سپاهان در تقابل‌های‌ خود با استقلال: چهار بازی، سه شکست، یک‌ مساوی، 5 گل خورده. 0 پیروزی و 0 کلین شیت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/28356" target="_blank">📅 00:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28355">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHt4lENyG0BIowtgrgfUtnQJbKm9mwB7RY02gbzHDLRGLndMU7w3Wct7MT8gngoFDWxPSN8d5BTwZkqKA-8CZrdjYHUhj3mQEXMnUiUZPG8qJp2U6Xbs-uDKhSQMSyDs9mUA14EmtXSBVusL6J6VLyQRnTqTwxE7u6hsOS4q0kbakKO2BZ3Klov2ITm2Kmqpcqs1H_miDwT8y5KL8-x965o22wi-HrBD73S43bLXHbsGsf0c32Lz56yzAWtlLfTkEN5IqknCDeu0jD8tE812Em4iXIajgEkrxqX52yahi_FB7O3W9zNZ2it9dvzB6g8BBnP9YZ-SH5l-kobJLgD_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌رقابت‌های‌باشگاهی؛مدافع‌ عنوان قهرمانی سری‌آ فصل جدید رو با پیروزی پر گل شروع کرد؛ تاتنهام همچون یونایتد شروعی نا امید کننده داشت و 3-0 بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/persiana_Soccer/28355" target="_blank">📅 00:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28354">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMu0eEq93h01KOgT5kOEjknXLTQogqVHfUbwqD7TI7dvPfWtoowLdBj6Kumwd5uAd2eEcPHOYyC-aKNL0V04508R1lWSL88lx92R_nYDHDB7pVqtaJ41iO-ccQrjD_kGVB41GBSUZoYsPmUkABtV_1fd--IoalaObsWyf5LgjYofUnnYNqSH8UL9YNLa7-IHY4KNlqAI_j2SBeLAG2CuiPySata5d8JnqZrwllNR-kzv0z-pj2K_YlgTrA6Td7yD6CLNdDIjYaI8P_ITZ8JUxqd4VWb3_kVWUTJJTJ44MsvfoamlrQ2fHeqeFmXlDBFIfIJqB-r4eSxtx3t66pFXog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
پاریسن ژرمن با درخشش و دبل فران تورس ستاره جدید خود مقابل رنی‌ها از شکست فرار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/28354" target="_blank">📅 00:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28353">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkHpdaLRiwKZAiydvOLFKVM7ugoM7DicuS_YZmi9GBP-dlbzFEuYC8Trqcj1MRVYsnwDw4u1i1o9OOvFEVPh2yckwfRjMIsquQZShborgP5B_dQKIgzDHQY1qhSQnnBCpJHrLR6DKBGv02bW_7ZhtGqn0t8PbkqEcIwGIjpsRIOYt2kNKCmZHRziR4Z9-BIhnUFdsSG_gOSUIHVSGK5t6Gf6vLzJzhdVVnKtPoDDP2ic1uljIuwp3i1CvsIvjguO9txu4LnGoJf-kExTaJ-2b4j3dQX5PgHg9-EIASPI8vGFqvy072E0y7ljanTMcek4KEFDLnwzz9HnqsyTGGLaCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفاصله‌چندساعت‌تابازی‌تراکتور و پرسپولیس؛ هواداران تیم تراکتور مقابل‌هتل بازیکنان پرسپولیس تجمع کرده اند و شعارهایی سر داده اند تا به نوعی شاگردان مهدی تارتار نتونن به راحتی بخوابند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/28353" target="_blank">📅 00:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28352">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e759f195.mp4?token=P49wdk6FEywADJnJguhH151jok1fUbuzSCkQiu9DhbRxHQoWy6Yu-odJHSCSDvMYDBYuPpniWbtgAINbAZOAdMJrz5WyaxmscjtqTLO2HUI3Ca9ibKpq_TAbWog0oj1VRf5QefflTP6z6Urns14X3VLemTxMeIVCVo8iirzyOURkMCFyd7hzdrETzEGEZR3CPtHUmt2r7BPenA-rnfeieG014lq4en2TMuLdu5S53Q2MbxTC6f_ZnH3MXPxrSyIEWXs2h4r_csVGI8H_wzIwM6KzZzA3D2v9gmlIVv4Hp2rG1ol1rBQB2Tp8oS52jEWmon-1yTMRvYPcqk8bsi90vWPtAA02ihP-Ao5Z3aM9GZuG_LQN9h3cDdHvxH0RSpMVlxSOmp8_jXXhr1093Z-2FWTRcEoC0PPjhGTde10X_wa9F_tUB9fVl-DAz3xVqsVZ0-EJWGdAkRQJhD4z_Y4pNFyuxSvvQEYM-1Juoo0itQBRYz128lzIxyJ3MWx5-GF7zUYXNgaQZthKlknA2TltuG5dWsSNZaK4kJJEjtqH_B2IirFPZTTmiH1FnQe90GcCw-xUZqnsytFOO46Ro-tmrWaYHNS3NJ4y6PWcbSa5XCk4b9wbOHZafvFVB-gwb37oTPYrTfoj3NQeow5yJbi9zclum4JFD4cPyZKbctXI1XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e759f195.mp4?token=P49wdk6FEywADJnJguhH151jok1fUbuzSCkQiu9DhbRxHQoWy6Yu-odJHSCSDvMYDBYuPpniWbtgAINbAZOAdMJrz5WyaxmscjtqTLO2HUI3Ca9ibKpq_TAbWog0oj1VRf5QefflTP6z6Urns14X3VLemTxMeIVCVo8iirzyOURkMCFyd7hzdrETzEGEZR3CPtHUmt2r7BPenA-rnfeieG014lq4en2TMuLdu5S53Q2MbxTC6f_ZnH3MXPxrSyIEWXs2h4r_csVGI8H_wzIwM6KzZzA3D2v9gmlIVv4Hp2rG1ol1rBQB2Tp8oS52jEWmon-1yTMRvYPcqk8bsi90vWPtAA02ihP-Ao5Z3aM9GZuG_LQN9h3cDdHvxH0RSpMVlxSOmp8_jXXhr1093Z-2FWTRcEoC0PPjhGTde10X_wa9F_tUB9fVl-DAz3xVqsVZ0-EJWGdAkRQJhD4z_Y4pNFyuxSvvQEYM-1Juoo0itQBRYz128lzIxyJ3MWx5-GF7zUYXNgaQZthKlknA2TltuG5dWsSNZaK4kJJEjtqH_B2IirFPZTTmiH1FnQe90GcCw-xUZqnsytFOO46Ro-tmrWaYHNS3NJ4y6PWcbSa5XCk4b9wbOHZafvFVB-gwb37oTPYrTfoj3NQeow5yJbi9zclum4JFD4cPyZKbctXI1XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه دیدارهای فردا ادامه هفته‌سوم لیگ که در حساس ترین دیدار تراکتور باپرسپولیس بازی میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/28352" target="_blank">📅 23:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28351">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ay9qXdFC-u2wRdABsvYWCMJkZjODX6kz2G6C2nPsaKukj-Bddrw71XTZmUSv5lvPB89wyCC4R5fSmvS_azzFKRx_MwmmaAx5HmjPqNGP41TI9x8ItHSp66VrnZgF8s56woxcw99pciFqUL5ktY_TFw3XbtPilzuRwvOHR-gup_tPB2OBplE9rITBZgGJ3UPd9tcZ4qZUqspD5mHAK6btpfmvyUx4yZ5tUH8SyEXOoxSTgMn-H80ot3zbWKt6JEEujSGTZ2VROTpvj0fPZbj_0p6nNJbr-pKVrbZNi7_48IXTEtr9td0N6F5LeVOBcQ2OJPWOhv9rqIHK0adQ94eRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برنامه کامل دیدارهای هفته چهارم لیگ برتر که قراره روزهای جمعه و شنبه پیش رو برگزار بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/28351" target="_blank">📅 23:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28350">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8101aef2d7.mp4?token=QNkuHht2flHFt9yOeCyHhClVenDCmN_bskb5AIKTAxzFdiWNNzxBkeahT4U-CjecFj8byKdS5vHnHds6DT7dlnKkS4lqtx1AAXl7tIPSgYewYKYVsk3logkxhCCu_macm2T7bFPZlgBeOx1lLt71ecYres1hmq5wYGSSKNxKfp-UkzmnHqCkqwLIhpL3zbG_Y6IWd-Zpan7pLiLLlJoRuwapNcOq5q_Wg74BeFHk0UzTibl7tXkT2KrC1R0OXq8d8hUhMRNRki9LWOTurb7yimYsjMyTx2rFK_cP-ffWlqvzkKTr9nWtFCBfc00evVNaDaWd40qG277UeMRtPOiNg4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8101aef2d7.mp4?token=QNkuHht2flHFt9yOeCyHhClVenDCmN_bskb5AIKTAxzFdiWNNzxBkeahT4U-CjecFj8byKdS5vHnHds6DT7dlnKkS4lqtx1AAXl7tIPSgYewYKYVsk3logkxhCCu_macm2T7bFPZlgBeOx1lLt71ecYres1hmq5wYGSSKNxKfp-UkzmnHqCkqwLIhpL3zbG_Y6IWd-Zpan7pLiLLlJoRuwapNcOq5q_Wg74BeFHk0UzTibl7tXkT2KrC1R0OXq8d8hUhMRNRki9LWOTurb7yimYsjMyTx2rFK_cP-ffWlqvzkKTr9nWtFCBfc00evVNaDaWd40qG277UeMRtPOiNg4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
بانوان‌هوادار استقلال در ورزشگاه شهر قدس در بازی امشب آبی‌ها مقابل سپاهان در هفته سوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/28350" target="_blank">📅 23:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28348">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvFmhJWt5Qb1E4f-xgg3_9p-CyQqyhIlYxtG1l41l0Nty7k6lTMOQlG6m2BTCSdc-Nx9zX0IIO462Aft7ch4sVoCCzjBcRcj8luSDsyY4qkOwFT47n-ca2BH3-0CgRPL7iFiEpqoLGeAiEzIwU-x4nGjaY2ElaK4Ku3VPQJyuH9RBQ7G4MmlYgmGOnVLmSfI4LZeNR-6ldVQBAhe9fciYIfmtgGuh39PbXj5Zq1Q1WFCvvXeYYwjBYZsy8rQx4ASDou4xAQVZhHyQeirgxdo3RRfOltXbePlhzjh81LFk-jTyU1tf8QGTP4Rl0XRauBwbiUG3Vw4ch-v7G3cEX635g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfpTpO4oTAWrpPnBhwwaXH53y6xZIAasKvrdmjSBlchlqFnX9GQ4LdJIVuyNvUKIn5hq8E2Omf4VTUnR--ROEFVs3EkKPvPx-TSBnqzp0P3t6rRmcFXt5cFiQG2WUD47NBEfsglLiCGIJLCmnwottfb5fTrVzAiWPPjqE2DpuuFypKZNf5U24mWc1h4tOS2ym-OJPyyDcr02HWEjy-9hK_jM9oSPsTk16B5b9gc_Xj82TpeX3MPplsFPq5DcbfxOnDc8pJXSi-iA6eGwGlPVPspjpKcSR8hc7hPuuBzUONd0udw-hFxrDHoCNpoqpL4QV2fAeDVuZDIDPTGkceunRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
👤
بااعلام ایجنت مهدی طارمی؛ باشگاه الوصل برای‌خرید مهدی طارمی تنها 400 هزار دلار به باشگاه المپیاکوس پرداخت‌کرده درحالیکه این باشگاه یونانی برای جذب طارمی 2 میلیون یورو هزینه کرده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/28348" target="_blank">📅 22:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28347">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5NA8QmTWfv_BQSnmwNSc8ZUXd8baPiyYiMED5qWBiEaqKo8Y0aI7hVBX9KgTQwt2HX13u3Da0KYEfimXTkQdbVxSqABoo5jVhaCjfmhA8BKpz0fB2h-erJTLQujtBFwqiaNfqjhoAYgFOKUQbR6derVTuHB-Vb2wr58fTV35YvcVKKvnEEKpmN_W081VEmvZ18pwumlK5IOhkc0AA_u0A0gBXwgTj0fTgNioQPX5D6xW-PTD6j1GylY4WuDY8Ig0n3X8cNsDncI6CUtu2wAUw8FGCSuTt0GxIOD2S14OcpYJ8pg4ZZfedcK2AwFqHdHK5KUtskKg6l3iIPl5BN1Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
باشگاه خیبر خرم‌آباد پیشنهاد معاوضه ابوذر صفر زاده مدافع‌چپ‌جدید این تیم با حسین ابرقویی مدافع میانی پرسپولیس رو به مدیریت سرخ‌ها ارائه کرده است. صفرزاده فصل گذشته درملوان بود و در مقطعی شاگرد مهدی تارتار دراین تیم نیز بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/28347" target="_blank">📅 22:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28346">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulAgyuE3BZ-oxH80iv_ryGrZoZ_iSdRfG97kiX8pZxAzr47LB-GsntOeyzSi_ajASyfoLsl5WtlbIRUAU8Dwih_Si0WVEaucPL1kko6hHFpZbC90puxUwxTQbkrfZ56YwFXceHVBMEF_dhabOiRDYW5-SMtucUiKezl7Dw0vibtkHvIJERFMYoiNfj3RO5uZyW6Pi2vU6FELI1Odhft21aqLYzVbFeBGRdq5G8tHrnpy_sSSabjuSBSumcTXJKgGl5a943OjYZr8d9Q7IJxPpIOB78uBPu8uT5yTgoalpwkhcFxPW5nQvMkNSCrE_2QQ2SzyVgKyEK2EAeKV0CsYAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بدون کلین‌شیت بدون پیروزی؛ حسینی به‌دنبال اولین برد مقابل‌استقلال؛ سیدحسین حسینی تاکنون ۲ بار با لباس ملوان و یک‌بار به همراه سپاهان مقابل تیم استقلال قرار گرفته و حاصل آن یک تساوی و ۲ شکست برای او بوده. او در این ۳ بازی گل خورده و اصلا نتوانسته مقابل تیم…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/28346" target="_blank">📅 22:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28344">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/djOiflUtgY359mZRZogfv_6rGevLwAZyj-wT5y_vgwxbBZuhYQyrvu4zkVL-TlXm0T7swsLVzBCkYixlkW3iKAdfw_KDpMFRc_TOKrJYe0gPljtPtZySgAl-5diXl1VCRi6QKSbe_TD1eQE41FOgngseAop4Ho0EnOQ0a-43aJcTNW-zVoLPIMGx0py0I8mQ1od5ZLPMHgeYRQLh7aiaPyZRDNBW7SR7H4zhrRpqCfYmJ47VFgPmaQrP_fUFA_kWf-P2JHUtwU2f-8ACl6v31ybTpuICDAXY7PcSgvaX3x62vg-cTnC47eg-s8ZM0CoTNoiyG9ETBCs6jSTCRqfghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TezgxwTB_I4JOABEWv_3eXz0MOflU26HKkOWdAwUM0sakJWLTC_3R9KqXdU2eWXOzlm4gVV7GeTVSNRUhh1Y4SMtikPost81-ByI1Z4nINxwcrrL2bldfqRmcKZ5g4a5EqX_fxR1fdnc94H_q6U443OG9MQFEbNIkuJ6MZwQsT7V5CSb3MVWFfh2EPFJmFrUwe82tviSCukyt8v6g-eDIakFhkXHl8mfIv6lsWRWe_46dELeEP9Vl1Sd3d4fBWSs3bvrneMdATvQNznYw_leFUumQ5xLz8mixqxTZ_dH5g06LayJOQxA7dgAfbAVwk3tQ9Xq_aOO-P0o2sc81EOgCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
جواد کاظمیان:
اگه ازم بپرسن بهشت چه شکلیه، میگم این شکلی: با جام قهرمانی و توپ طلا، کنار سرخانمم مونیکا بلوچی عزیز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/28344" target="_blank">📅 22:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28343">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVapUqfVjFVfeDXd6jer0ybQ9gPX-JErckBEDX5ZCVz1nfe4j667nBm_2Zj1ZYIVZE1Oqe4Q0-gLEHsOKbxSozcg_C4oNeSpfsDm7LqgpYP7iz84TYH4nPKnwerR7hLnelYydGExdXD7dhR7eYtsMF0sPsVoBWQmICChG80j_Ul5G-Byhz2UfoEMKm5-SFHk-0WzOdmGW0ds8io7ShxSwe_5gpjFMBsowWdbYrGk4f_YcU5BrjX9qbyLBDRBadrAahsRwKAzt68NHdOAj2V_MHIc58V_dfZbXiRO2HgZLoCkC8x3TXIBlhZuvgp4Ss6b7ik8v87W6xQZPtfzqWCSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی پرسپولیس در استانه دیدار با تراکتور: به جز تایم فیفادی به هیییچ عنوان بازیکنی به تیم ملی بزرگسالان و تیم امید نمیدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/28343" target="_blank">📅 21:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28342">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vD3sKnt1LjDy8ENt5WTpcm-xFH95yHZosaP3WTpl9ymlV43AKDKWOAxPnim0cnaJr8IWrqjybnxYSBkhBNlSm44eLrzAJZJ99-eLpfmkZURfDg1vAi9hdvX_OMn3ss-M_PfdBpj_cg-ySIuim8tPu-AYphLdeoTch_vsSB78KJLaW4VB5lTBZgc1wJwMpYjkC4SHY1jDi4_rh25gLxg9nc2-5kEnwhjhMFskHGCAMzxMmgeVtl2D7kgQrBipLSwOIP3aRmi5hgwJmhlRk9H3ddnMacg8WtC72VkZkBZiHWJWWWJEcpvnZGhr8CcQ9JJ6UCFxkZcr9WApSeLHwsvk3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
به مناسبت بازی امشب بارسا مقابل الچه در هفته اول لالیگا؛ نگاهی‌بندازیم به اسکواد نهایی تیم هانسی فلیک درفصل‌جدید رقابت‌ها باجذب رودری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/28342" target="_blank">📅 21:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28341">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
خلاصه‌دیدار تماشایی امشب‌ استقلال
🆚
سپاهان در هفته سوم رقابت های لیگ برتر جام خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/28341" target="_blank">📅 21:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28340">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeQDzBL1wwWCR-Rpb0zqLua_E2x_Sv2VxWZlQgssPBQTvyfQuzEyxuKaqWOPPSMXZCRTQGlNLMtib3fC2Qfx5lAGPd3p__eiDcIKHod8E-0K6uE1OjdeCnrwh6hbfAyinY0S8PdFpZWMjGCJubD6IeHxokc6G05yVCatDGDoe5j2oGxI6mkISJUHkIOVOmsI-_uLe7x6SKUNbhGuUHukxaAcenD4HnfwApyxn_NZarD0jCYGXOh8WTtRLseK_WBWYh9YhITnD3eyYqsj7BDUDJGjL56HBgxwMYJTEHQVU3BPw_thjdJl9U8kofkHHH6PJm7gBqCzUISyukVA6JKDPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم ملی امید برای مسابقات آسیایی ناگویا اعلام شد که امیرحسین حسین زاده ستاره تراکتور تنها بازیکن بزرگسال این لیست است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/28340" target="_blank">📅 21:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28339">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aO0moOmX0NFRuqPGjtJJkHVmvJMj6onHDOc3bxIQSlWffv1RcuojUMknTmFXB0xuTbH1CXo3MLJRVQhfEtKpXTZOxus5HnF5PLAsyOqvgXaIjEmvMKvJt8-7KzGVlC5UoOEoZMuMYLqcZkNeuWcLrTuEf1DYiFhp0uYe52MxP6N1u9dkxvCzuxcW9TguWlm_VTILPfBiCLWoymM856f5w9G_3Oem4MjruzOhW_8vGcqtURG9meEedoHX10JUH8BXCbFM1D5KIVD7GJYu1IbI93k-fjRImrYBUmepYl12HQ27Wq_F60zqz_uhxr-0saaUIXph7-GrG_OjN1PyaKGDyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی ارزشمند و حیاتی آبی ها در تقابل با طلایی پوشان زاینده رود با طعم کلین شیت؛ محرم نویدکیا باز هم به استقلال باخت.
🔵
استقلال
2️⃣
-
0️⃣
سپاهان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/28339" target="_blank">📅 21:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28338">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYmsXiYeOqivvq4qyXCyJ6oZGChpUn8_lw0Dr5HG9sLlBHugLedXWOU-KrD5Zn--QD0LIMiCwHVqJbjIYxYGOwQEnHj6p4xEUCJzKTl761L06CTKs0QIBWJBnEG9Vjmxv_jYu6sPBOTbia5TaMUnLMzo3yTgDCIG4MbJiPi_C0Vch9xSQB86naO3KF9Ulnf1Jk1BQofmj8NPebY0jrSzdnDXI1cQ12DusNLM4nQj-dr0GaVziKJfABSeZuPSjd5ULyP9DQP8_cCf7XYDtw8LWcCEm-4ZAxcj3NsTRUzl26iSUSH9yDqVCMZIJ9_tEXaPwxsHoWLZGLFM7eYW9jFI8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی ارزشمند و حیاتی آبی ها در تقابل با طلایی پوشان زاینده رود با طعم کلین شیت؛ محرم نویدکیا باز هم به استقلال باخت.
🔵
استقلال
2️⃣
-
0️⃣
سپاهان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/28338" target="_blank">📅 21:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28337">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAjCdbtFkXx4mYlX3R1-lW9pStwwF9fKRiEsJOeLxNfqyA9Nq_SkYwzHbzfjGDNKKMvJqF849i25DXPQqzbAflyLcrzLVS1T0urtgxYi_ZNmsw72kjNUQS9N6nvOX2PGOWHb3SwDIgoM5-Dpz7pRv-_ro1CghVL9qPeRRPTg0FqhIJCUsufH2YGDD4OmJwo9X0zge4ip16DPU2myQ1pyesZwRHPvhbp5iG5IUWZxLN9ycW8aXMmtiNxvVcA0I_K0yCZ9-dMd9Lwd7nXOTjL0nv4VYARN2gyOT6r_Sg1DTf-KQTlIeVfIeTzc6vuxWWfF_yUGOZwBipsFBRmeKyxmIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
حسینی دومی هم از آبی‌ها خورد؛ گل دوم استقلال به سپاهان اسماعیل قلی‌زاده در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/28337" target="_blank">📅 21:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28335">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDHAl9uMk-4D-DwV5k9GboQ7nwnm4cZNrQVks4P2c6YEtsXPvITBFpbhRNnwEoMUYSEDlv0PwXQ8CZp3fxKB-o7aKiXX0B0Gy_Jlmm5JCtIBktfTgEf0YrJQeUQ3KnqBoyd2pRNLaZ4UDJZre7E_6Cc7kzI_DA_id8erqqpqswwnWipeX8tRAIVdtjNnu2EahwtMmvcUTlJpuPptd0s_IlaUVE7AHyz1QGVpZgkoa6dq5ubUYOq2j2cY3xLmyEMcd6bGM78-l1TU5JFUPd3DJdAcPk6rEoyA_hDlqAzl8aBFhqwpeMEbLUmQGTk4iV26ZmHBff8rH8wrmUMROQoKww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XZiCTQ210nxxcu3kYXcHVHr5QPGCe3q5MeLZ-c4a_pEpcJ6RqC55w_1FgS7z-s6BMuRAVzH8fGi5C2Kz6VWjbwBIFi7NE88wN1bDl93h8iX5ROZQsCK09LVdgqVcrH9mH3-_nP0ZvGb_TImUTWRGs2e0TaWwHFa228y-_00dRN5Y9b0SGn2PKxE_oekQdQu-aVFvEfPx5ZwfxKBEgad3_6a3vErn48SvPx8YjOgBxsmxVG8U1mPuN9RjkqsmsRelgakmLIUo9_DdbrmkALmCaDcYXQd6gB8SbetW5YFjMSQ6xO774av6AyexIJ6mU7RmTe0gxM-ECss2R1fBxzzb_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نتیجه دو دیدار مهم امشب
؛ فرار سیمئونه از شکست در گام اول لالیگا با گلزنی پسرش و تساوی پرگل و دیدنی لک‌لک‌ها و کلاغ‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/28335" target="_blank">📅 21:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28334">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d47b1892e.mp4?token=d0e21s-TxypGj8Fm5yzyiCuS4_jeY7vBq6avhKfvAYOGM-fLN-osEfkNDRi9q-3W37R8aAp3AFIsbFKbh55JnT8bFlfdJlszoPCMALTOJ-QQzzeyTL5UXeDZjhZ4_oxHdeKpmWbkEvYWlj4v_T4n0B89UsZ4hgwZsfksnZw9UAO6Eh_xVThrnHJyNxr16chEotpGJ5fioh1_20b_Mk0cID3h5-qRdtPgc1rbFsjE-toNT2qYPY5le3Bw8E7JyP9ViecLRxqRoyc_kJZf49fLv9SVdybRuvH3-jjbheIX3QWJVLRiL7t8Juwo3zHgrSidVHcFeQornkWuXyOTcvuzDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d47b1892e.mp4?token=d0e21s-TxypGj8Fm5yzyiCuS4_jeY7vBq6avhKfvAYOGM-fLN-osEfkNDRi9q-3W37R8aAp3AFIsbFKbh55JnT8bFlfdJlszoPCMALTOJ-QQzzeyTL5UXeDZjhZ4_oxHdeKpmWbkEvYWlj4v_T4n0B89UsZ4hgwZsfksnZw9UAO6Eh_xVThrnHJyNxr16chEotpGJ5fioh1_20b_Mk0cID3h5-qRdtPgc1rbFsjE-toNT2qYPY5le3Bw8E7JyP9ViecLRxqRoyc_kJZf49fLv9SVdybRuvH3-jjbheIX3QWJVLRiL7t8Juwo3zHgrSidVHcFeQornkWuXyOTcvuzDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔵
گل تماشایی ابوالفضل کوهی در بازی امشب نساجی مقابل استقلال خوزستان روی حرکت انفرادی خود؛ کوهی درآستانه پیوستن به سپاهان قرار داشت اما در نهایت شاگرد مجتبی حسینی در نساجی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/28334" target="_blank">📅 20:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28333">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_QboGA2u7_K_ObHFdRekO6cLT2YdQ0fonAws0Df48_uo6sZNmcwsBd4jzdCT5tBdvJJk_IM03kdBywMfHEBTViYGtD-oeJy17HjvsGiPf7AnIr-dCG32hMeALtjAcJozzg1sc0PwVBj9M0YAD_lQWMAPbj_xnRtf2QiIBmwtmYbeCIO5qQm8rnKdkl2PuINeBHGAtjb5Bvoh_fDDPdqiEMso6m_2zCpdEOJValE5pDnGM5aalt-OJL1TUO4P74qJYkoQbYwUtdIf3HvD9T9xeRYzzeH6U41J2cFjF0RYdiZpObApagurmc_4_xb8soszrFRklq1XYjpVeWvlHKLRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
دروازه تیم محرم خیلی زود باز شد؛ گل اول استقلال‌به‌سپاهان توسط یاسر آسانی در دقیقه چهار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28333" target="_blank">📅 20:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28332">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQCYm7DwznJrHE7AV4ZkNUYitXF8nePDr9GU4trgJaDeNc2wJF_C59-S7Lz_7L2dOi-UpKqVPsmYaDp4WhfeukkwUZX0VjjLCuUT_fKX4uU_shWnfdiOZ4VEhn3ubYFYCBOmgpzlgu8_WACP3A8167nYlslbfD77GN5qTTlW_x60IfGeM5H6e0jo2lzIWIVhSzwKyjlbr4yK5L1EeHCs39-PHl2MUX8mzMJh9tJXftW9jiJr8tkJ6E6b9JEzfO64sDyXaxHxpcE64kurcSCUuaa_YF1NckB9vqOdh4wQI1r8_2irvZLprhkIhkWsd_rrLfEaADO_8NPtAnwTlN7i9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
حسینی دومی هم از آبی‌ها خورد؛ گل دوم استقلال به سپاهان اسماعیل قلی‌زاده در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/28332" target="_blank">📅 20:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28331">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3797b4f0c.mp4?token=jvo-HYwGRp3VLFze9rb4dS-z5SVeoOB3Vc2-eN35tztz5mepD9IRNvdqc2kdTN0FkoLtKLzcYWV_k5DM62tLV247ynD6-61nFRCzAU5vBjSJ9uBDVmvyyMmxiNrrULTTbznckhRakyRSyqF8CV8y476jl2SQunhQIDHMCGUFH_RaRNMiiZ7hiO1kQFhl7UgrNA0BToJBzovfpVPxwEkShcBes4ibqLbjADmdyjQAIZ8zUXjg2Avwo1HtZk6YTCOZ_QcJix97ju-eQIk3zY4mONLaiyG-KIPuW0WXY5pP1h_xOnXdYf7_6h4OWXaiLdC5f6cGh8p_-HN4_hHYjzhpuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3797b4f0c.mp4?token=jvo-HYwGRp3VLFze9rb4dS-z5SVeoOB3Vc2-eN35tztz5mepD9IRNvdqc2kdTN0FkoLtKLzcYWV_k5DM62tLV247ynD6-61nFRCzAU5vBjSJ9uBDVmvyyMmxiNrrULTTbznckhRakyRSyqF8CV8y476jl2SQunhQIDHMCGUFH_RaRNMiiZ7hiO1kQFhl7UgrNA0BToJBzovfpVPxwEkShcBes4ibqLbjADmdyjQAIZ8zUXjg2Avwo1HtZk6YTCOZ_QcJix97ju-eQIk3zY4mONLaiyG-KIPuW0WXY5pP1h_xOnXdYf7_6h4OWXaiLdC5f6cGh8p_-HN4_hHYjzhpuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
حسینی دومی هم از آبی‌ها خورد؛ گل دوم استقلال به سپاهان اسماعیل قلی‌زاده در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/28331" target="_blank">📅 20:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28330">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/620ce5c574.mp4?token=FvsvnJ2Uu7LIPqGwgLc0BQzIY0Ua7mRt6n5kiFWg-1NDo3SG9F97sJ4AVxrjHeUjBIb4_KUyGPCobsAcrDQmaLyoQmrCOupSXokZ1uN8wfLxTgu7oSTXkpO9Fe_sPgd8u0lNGF5J1RbLu6jhEndvf8Rm4K1fWg8z-0pilaXlif0laXUWvh_BA-9G7ybd6WkFVrU3scaWQ3801t7wxCzKuDw5Pw0g894wafob0z82Vlwgx7WD7MXwEj5v_GxCXmfJT-Ldn6w0BTq5FQXoZ2NM3Eg-w-wslNDK1-XTHWIS51c9SJVdY6GcUSO6sUKNOedfZn6Fk-zfwGGnjrqe9fr9eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/620ce5c574.mp4?token=FvsvnJ2Uu7LIPqGwgLc0BQzIY0Ua7mRt6n5kiFWg-1NDo3SG9F97sJ4AVxrjHeUjBIb4_KUyGPCobsAcrDQmaLyoQmrCOupSXokZ1uN8wfLxTgu7oSTXkpO9Fe_sPgd8u0lNGF5J1RbLu6jhEndvf8Rm4K1fWg8z-0pilaXlif0laXUWvh_BA-9G7ybd6WkFVrU3scaWQ3801t7wxCzKuDw5Pw0g894wafob0z82Vlwgx7WD7MXwEj5v_GxCXmfJT-Ldn6w0BTq5FQXoZ2NM3Eg-w-wslNDK1-XTHWIS51c9SJVdY6GcUSO6sUKNOedfZn6Fk-zfwGGnjrqe9fr9eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🤩
پس از کش و قوس‌های فراوان خولیان آلوارز رضایتش رو برای موندن در اتلتیکو مادرید اعلام کرد و این بازیکن درجمع‌شاگردان سیمئونه موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/28330" target="_blank">📅 20:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28329">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8acaeec43c.mp4?token=XmHIxwUkVXLnvY5wxjw3jarBGKRKXFXWiHcAzH6uFbnIDf8tz9intGxdUQx6amDxjDtTBIqR84mHyY1RnmVpMWkb8zJvLMwt2IN2mAIVj7837S21FNRhUuVZtd8fa6AWMlcmr_QJFTVS9jlbheX42UCQ1SG0B16JmLA2rwuthUcig_v49lGO3dxYsDjgM8bp_QmiTvC2CUm3A700G8pPiMBaad0_QVxQesEplvr5Z16vjq0ZI4TnTXmo8kedRF6R9ese6xyOOUlwKJAgigxuZNfysEVBQPXRSsph9KS8Cy8PioRooh69DrAVoZMzkXj1rjRXxloHoHrDdoIWDixhOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8acaeec43c.mp4?token=XmHIxwUkVXLnvY5wxjw3jarBGKRKXFXWiHcAzH6uFbnIDf8tz9intGxdUQx6amDxjDtTBIqR84mHyY1RnmVpMWkb8zJvLMwt2IN2mAIVj7837S21FNRhUuVZtd8fa6AWMlcmr_QJFTVS9jlbheX42UCQ1SG0B16JmLA2rwuthUcig_v49lGO3dxYsDjgM8bp_QmiTvC2CUm3A700G8pPiMBaad0_QVxQesEplvr5Z16vjq0ZI4TnTXmo8kedRF6R9ese6xyOOUlwKJAgigxuZNfysEVBQPXRSsph9KS8Cy8PioRooh69DrAVoZMzkXj1rjRXxloHoHrDdoIWDixhOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
دروازه تیم محرم خیلی زود باز شد؛ گل اول استقلال‌به‌سپاهان توسط یاسر آسانی در دقیقه چهار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/28329" target="_blank">📅 19:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28328">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f358d6852.mp4?token=LX6sTBXcAgzpEm-Pe8AI4L3i9AhxaSPEwv55SWuznulRVDU1W6sRAOh1Ln1S45usIDDqz_Twl7VTVRzq5A0olmV1XJUURlBbeJmq2tqNJ4NQqwuTVRk147oUAxL-s4MgwF2feWwqWMWmsGrOpTfCYHxKIsoseP4DvOcaq-X2p4b6VMQH5tIAQteuu3rNPdqxYIPcD83wxQBs9Hgq1gx5qOFURhIi_r7LUpYrdx9aqYv2eoxXr03uek1pljungZUnfyySEU2HOJvdkN5tzxV6FjgVn18JRzZrDjrqObJDeG_GbKMSQhLxaruyUXMCGCH3R1RKXdsQ-cFYvUk_c12hag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f358d6852.mp4?token=LX6sTBXcAgzpEm-Pe8AI4L3i9AhxaSPEwv55SWuznulRVDU1W6sRAOh1Ln1S45usIDDqz_Twl7VTVRzq5A0olmV1XJUURlBbeJmq2tqNJ4NQqwuTVRk147oUAxL-s4MgwF2feWwqWMWmsGrOpTfCYHxKIsoseP4DvOcaq-X2p4b6VMQH5tIAQteuu3rNPdqxYIPcD83wxQBs9Hgq1gx5qOFURhIi_r7LUpYrdx9aqYv2eoxXr03uek1pljungZUnfyySEU2HOJvdkN5tzxV6FjgVn18JRzZrDjrqObJDeG_GbKMSQhLxaruyUXMCGCH3R1RKXdsQ-cFYvUk_c12hag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
🔵
شعاراحساسی هواداران تیم استقلال پیش از دیدار با شاگردان محرم نوید: سپاهان دوست داریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/28328" target="_blank">📅 19:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28327">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ae17874e.mp4?token=DSCG3INgyWQzLoySpSX59t9a83iC3CqBzbtfPn8h3eB4Nro0kWBAQ6qlOJNj9lXDrkwvK3WBBs4rhMQaSra8w_y9Scck47pro7yN1CZvEptZBUxUm1QvkT_COzoY91bmidQSr9Fcb3KT_H4lcPmtJhXpPj2m11-IIPfuSD-PXjCotdkiOy3hQfBZ2mYtioIyNcK9FOqNsye0YvWZ5L1fjmP4J4He7Pz579jqY_mlanChofFxfhEYrtiyk9dWKHndjis28_5S2YBVuxJH4hKo0dJBS1DGYXWeBa0zoTAHVZbTQsXGoF2ZfB5zan1J8mTRCf7i-AamxMQOZO6l_8M4sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ae17874e.mp4?token=DSCG3INgyWQzLoySpSX59t9a83iC3CqBzbtfPn8h3eB4Nro0kWBAQ6qlOJNj9lXDrkwvK3WBBs4rhMQaSra8w_y9Scck47pro7yN1CZvEptZBUxUm1QvkT_COzoY91bmidQSr9Fcb3KT_H4lcPmtJhXpPj2m11-IIPfuSD-PXjCotdkiOy3hQfBZ2mYtioIyNcK9FOqNsye0YvWZ5L1fjmP4J4He7Pz579jqY_mlanChofFxfhEYrtiyk9dWKHndjis28_5S2YBVuxJH4hKo0dJBS1DGYXWeBa0zoTAHVZbTQsXGoF2ZfB5zan1J8mTRCf7i-AamxMQOZO6l_8M4sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
شماتیک ترکیب رسمی استقلال برای دیدار امشب مقابل تیم سپاهان اصفهان در هفته سوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/28327" target="_blank">📅 19:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28326">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8b132a0ac.mp4?token=IhDG-xgwDMOPcj2lIZ_fSQb0PKq_ZsFH6HgzUofFaGGanKfk2fg59xxdmpK-EJ0cWrHoquVN-uzoWTaFq3rz0cor8G493yR2bqGv0r84nAFE8yD7O3OMM9ZJJEVHNqtzPuU7XuiBK3o1As-u5JrVgBJSHZzXN6d4gkluVkd1v_pHMKEw13i17YIQWjngD3mWvH_DStgrvAfsvenLPe7urmR_V-qFN0TUaoqZt8NtPUQLReqZg48ZXE5_6WhF_nXaC7kH0QoPZQtiPxfRnMZXGxhrlmuaSkli8gR8a-OxzTeo4uEGT4UxsFFFZdqXAwjBUmqT8vFQGH1VbEZ0B2eFRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8b132a0ac.mp4?token=IhDG-xgwDMOPcj2lIZ_fSQb0PKq_ZsFH6HgzUofFaGGanKfk2fg59xxdmpK-EJ0cWrHoquVN-uzoWTaFq3rz0cor8G493yR2bqGv0r84nAFE8yD7O3OMM9ZJJEVHNqtzPuU7XuiBK3o1As-u5JrVgBJSHZzXN6d4gkluVkd1v_pHMKEw13i17YIQWjngD3mWvH_DStgrvAfsvenLPe7urmR_V-qFN0TUaoqZt8NtPUQLReqZg48ZXE5_6WhF_nXaC7kH0QoPZQtiPxfRnMZXGxhrlmuaSkli8gR8a-OxzTeo4uEGT4UxsFFFZdqXAwjBUmqT8vFQGH1VbEZ0B2eFRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترلان پروانه بعدِکات‌کردن باشروین حاجی‌پور:
بزرگ ترین اشتباهم وارد رابطه شدن با این آقا بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/28326" target="_blank">📅 19:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28325">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAMy3lz4zCPFoeYheIibYrHx6DNcrE_dVeX29qq4YEKVu-FTItUTz3grw7dAVECUHWwRY3bGeD0n729HZfEY4yo2MHCi76xjmNF3Xy9g4J9Zihtp9QcOqHe-hlR3f66NoxG7Vj2IU0JGkoKkDMOwdEf9tm90-wJLirOEoYQkz2xOVRUAr2JLO8_kZQSmAVA4Dsi4LDVI6TcegU61pRJqfFze8Ub2A2A1l1GZaxcDuQdioilctBZhiSFhVC3Tr-x6bzTMzcT07DuCnWy87CwZ5t0DNH-GB2c4qbt7a0H8R37iRhdT-KiO61hI2ApT4OhYZ55PZNu9_i3nExdCucqbtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
امار فوق العاده ی کانال ، کافیه هر روز با یک میلیون شروع کنی و اخر شب +15 میلیون بشی
💵
اگه‌نمیدونی تواین روزها چطور بازی‌های فوتبال جام جهانی و والییال و تنیس رو پیش‌بینی کنی با مستر تیپستر همراه شو
😍
‼️
میتونی راحت حداقل 10 تا 50 میلیون تومان در روز سود کنی
💎
کسب درامد انلاین ینی زندگی راحت پس این کانال از دست نده
✅
لینک ورود به کانال :
👇
sg1
https://t.me/+q-sIylsuFEtlNGI0</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/28325" target="_blank">📅 19:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28324">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTjgP0nXbefQNWmaNXyX_g53OHPjbGf4Z2XAuw31zAVtDZXFMUyAL8qWKllPTlvq8Xs1-6izpYuW2b6MwwwGKXDmVx1sbzeyxtCFoh_qbSkNokPwFrtrEZtHg6uWx_nujkecvEf4q-CRUjD_2xOL7Rcde1_GiONNfJqfQCsPDt8W0Qk928fppvu8VxNH4d3aL7XkR72MtYvMPwXJ-t5YTNsgagFB5mxACaa8TJOPmCsjrNeHDRQPPbuNbaSL2msmzPaHe4OVTu4bABEta7-sb_E2o7qvH1OPuqJirnl7Iug5e2HPovukMI7qK9BUt7JSZvxXtzMiGrXLWoZcQKcsyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
10ستاره‌تیم‌منچسترسیتی که همگی بعد از جدایی پپ گواردیولا از جمع سیتیزن‌ها جدا شدند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/28324" target="_blank">📅 19:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28323">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgVls_xQsRgQS5GeHRNhL9fN9aMTBaIpzHwko-4xtZNDkQ_FnlwW3idMLaSxtya-uFnhs3ULaJmzkYCMWw3wqvgaI0_dvtrwVh5ytVLe1-gWh8jI5hGnsDI6SUdGzAFslqzftAbrvroFaQRX4WA0hWDeyADcCOjRPxIXXEN4ODXNf5euF2_3MVfQqqzoBvdGEBP60g1Gf20LdsirSIVMzqYXgvsO1NnMp58UsaJRk7QfUtfh8PGB5rZUD3RHvFd2QT6N1O-BiE5kcanUBDOmg41P3RC97YyWuMCnLOVB-_YuDx0WxCQ-_B-ewB_ZRpauTa-KoO-N90ereK_IhT023Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی هاشم نژاد دیگر ستاره پرشورها نیز به دلیل مصدومیت دیدار با سپاهان در هفته دوم و دیدار با پرسپولیس در هفته‌سوم رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/28323" target="_blank">📅 18:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28322">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U299K_PZBSWCNCVbd69isOnXFBmGWzuHanCU0OMiQc_ZhpLRn1Izk6pBuJd1W_thH2uDwL_qLM9JlfSUWeEF6A3MC50tcp9_yjyKDT_TbuL7yx5Q0lGmALgiuC4CudZd0nlg7VwLDDCFRexSVCN7wNHtCmPINrgpDhYbKfzZUsKEm8soHHXUJya7ksnTl55fJGWJGQxIdSky_lWwctmOHVp6gUUEI9JmX5Acl9TR4v3G5H_NY5YozgEbZIToO_85v4x3Ceq6Ks_rqCnklybChVXKegEeEReRXGs6vVWtXl7odl9f81-1Ic0nIS4A4LkgGi5pHwCmTG7dQ3a9TlG8uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شماتیک ترکیب رسمی استقلال برای دیدار امشب مقابل تیم سپاهان اصفهان در هفته سوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/28322" target="_blank">📅 18:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28321">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qppc-m5_1VBjMpJK2P0rrvnqd816xROAJ6Z7r8ckFvEPfbSdxV3JusIX9efIJQvKmssN7iWZhxqfsbxqYPuTWpCrBUNmTJZlutavPmCJn7kqm5fp845LIN8VmWONY1gsvLQ4_7d0-LLyAi_4shp3CMnCGouGJ00z3RN7zxFmjrLQRFvkEcszhuAEhTdjhqmiNYq7JqQjBkd4m25oPoZaFkxAJmMfvmPpwtwwkmmeRqlHlFJHoi8Y5636hgatgvAW1DcUTZ3UFeb6gaTfSgFdzCFedcgqPD_6N08VIkUXibTOvbiH0jyNvhbJIYXoVhr16Q9-U451JZyVOaMEe6JOvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته سوم لیگ برتر؛ ترکیب استقلال برای دیدار مقابل سپاهان اصفهان؛ ساعت 19:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/28321" target="_blank">📅 18:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28320">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdVAuig3X--6KeFBKdnIiZg2cqPJRwt8OSfkNFvh6BTs50rOLYcKGP_v6qwkZDRpazsCiKw-5MJagoAk6GelAop6xZJ7zopDDmwAAm6_hvCx9-O6TZM59iBMnyf5hA4QuQn2_BGuiw2lo6D_BecnOJmrjLxuqeY7BVuRnkgG6kyn5mIm4-4QN7H0O_ZPZutTyOyY0WVoIj3SxXA7JB6LG-mWH02o5ogv7NFYaRQxFPdbZ-dEM0L6iDe9WTBC6qM2vSgog42ZhFiI3uSWZdEnZZ_6PfTubGUthKlclc9Fmxu9JNN_3jL7APgnUCkWzSA3hGUFjjgW7PyCqF3tITc68A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
ترکیب احتمالی استقلال
🆚
سپاهان برای دیدار حساس امشب؛ ساعت 19:30 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/28320" target="_blank">📅 18:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28319">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1FyfxfX2MsqNKXTHFmAJYY1B4R9sTjakbNfeR_q0Q8LLdF5XU3dLEwAOJhCFiRJMOczD62rx-Eo8gY_WsNK7vf3Yq75uaIoJCLIU0ztySoqMrNH_dPQRKugWyVrxSpFSrMaM5g_UrRM4wcHVzAz3Ai4hBRZIbwfCN0xuGfOXG5N4RvVD9lFQec-HfA3ItSJtJgL_lks2NG_ZQ_7Zn7uJaCXcwpKs6zv0ef1HjwB5nGKCmJtxKCFHDhu7brKt4nbwhyv3faXd-5KcMDyyDD-ZBtcKSirSJ2aWQqzVWRQXJO3iSBOLh824AF_UA4Oqn_-t97YkC7rfGLhs3bj-piHoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌‌ها؛ مجید حسینی مدافع تیم ملی آمادگی‌اش را برای بازگشت به استقلال اعلام کرده و درصورت موافق بختیاری زاده با او قرارداد میبندند. حسینی از نیم فصل میتونه برای آبی‌ها بازی کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28319" target="_blank">📅 18:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28318">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOdrXF9wqEAtx6YljMaaWK0sGJkoxGKHm-Ava_M7J8REdUZF05idBES1uLtieIFdratJf0jtyfJevXOHNYpUvSRfMALs2t5Kz-1W48U5l4MqRBktVgH09LvnLEpRLC1iZejgIRmpKgTz95Zg2RLt7UAqDdridhOUvGU3DlKV4mfiaK8iBwcc7dNcqvQuln8Hu8tPsL4VWapEsqYskinz3NGNL2vJgjWBwAB5xbSbKRqlqJibeTbp-7mPb2WXu5A8bXLqRnNsrR5xpRqAG5-DtyLYkwTihxUAUtHowCIen6mro-rbaMphnhjiI0XLf3yi7Y45M0aHdEW51zhGjFj7kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
باشگاه خیبر خرم‌آباد پیشنهاد معاوضه ابوذر صفر زاده مدافع‌چپ‌جدید این تیم با حسین ابرقویی مدافع میانی پرسپولیس رو به مدیریت سرخ‌ها ارائه کرده است. صفرزاده فصل گذشته درملوان بود و در مقطعی شاگرد مهدی تارتار دراین تیم نیز بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/28318" target="_blank">📅 17:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28317">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3040660e7.mp4?token=edF_EFbF-dcp2cHplY-pABHFhjXPh_vdUiF4IfXfWTdeqXy5SPqif1KKVLZhFB5GoLKTOywIkzVAejIJ3fD3z5A9n1nEpLok8IFkC4XJIZJigW0cRD3G8I3D8UxIuzsxOUjnA17qmkmJWOspT-4EZHR5FQ8mYkK79mb3sA-ycu7Uyh3Q49WfMcdtx8tHt0rPH77oZR3cqXkcOoke6Qg4e5Lx9iVvEfq-0tekLa2WmknHhFhEXC6IkeJuyMD9rBvDgR_znu_8e3XVMoPsf9VnOq-PXeyl0ofsLpk59qTClYQJRZ3qTUiHupSJvrwXsFn9TV-HaL7L_NXhmkfNr2HxVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3040660e7.mp4?token=edF_EFbF-dcp2cHplY-pABHFhjXPh_vdUiF4IfXfWTdeqXy5SPqif1KKVLZhFB5GoLKTOywIkzVAejIJ3fD3z5A9n1nEpLok8IFkC4XJIZJigW0cRD3G8I3D8UxIuzsxOUjnA17qmkmJWOspT-4EZHR5FQ8mYkK79mb3sA-ycu7Uyh3Q49WfMcdtx8tHt0rPH77oZR3cqXkcOoke6Qg4e5Lx9iVvEfq-0tekLa2WmknHhFhEXC6IkeJuyMD9rBvDgR_znu_8e3XVMoPsf9VnOq-PXeyl0ofsLpk59qTClYQJRZ3qTUiHupSJvrwXsFn9TV-HaL7L_NXhmkfNr2HxVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
🔴
باشگاه خیبر خرم‌آباد پیشنهاد معاوضه ابوذر صفر زاده مدافع‌چپ‌جدید این تیم با حسین ابرقویی مدافع میانی پرسپولیس رو به مدیریت سرخ‌ها ارائه کرده است. صفرزاده فصل گذشته درملوان بود و در مقطعی شاگرد مهدی تارتار دراین تیم نیز بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28317" target="_blank">📅 17:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28315">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5-yU-FZmHu1AjnDA5a6XesERKeBXzOv5BKdFo90pD0vJq9jQ9f2qChQaHU9p3kwssRzS0IhYmLF-fKl9DvTeMySO5kmJduE6KH2ReXGT4dQ9S2fZEW_h_02VMvUcR2l3AQnxBZZZ8bydq2WjXm7oVCqWjk8SxpEVWSEgMoRbAO9PHd1QGXJPrQgV4FkR0RJi7re5Q5zR0qlaQ3mNPWSzNKx_PIEJNROZCH42m64Q4w_kQBpjIDVU6sPVH495vHPMhKK8BSgkGtSAYcQuhvI1Tc-5xqpuij4iZr40r1jSsA_ra9Q9PMTOdCSHg5EQF8HJX3i0sNtHehlLOl2WKhHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8f8039bd8.mp4?token=QDDBw1zmvTjvp7ZmQ6WUqMdeMePm2NdIj2tnHGCwvSkI6wfcV9P2WF7ZfL24Oe12ba6dI7YtQaJIBGBCxcqp5dBXzskmC4vV8mDGI2dyuALl5N97AgberrOGsMUHseAbZpGpOpmKvsMKwkO0xvKFWbKKECTB4JgP1kx6VNjj-lXgv5rANr-OJimkhsKPcEnOIjNrK97d_xLXi9-6tehbIyV3ighCla4CJBBlUbSkm8CqCFsSRmBGlr3Gcs1Uld3Avip_TyjXMgRSQvXmePdLzGUudvajY5CJ8gN_mOdN3xcZj9Z7Ncji27CTaoqyswdbbr39eccMVsQuJ_6vzGUoWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8f8039bd8.mp4?token=QDDBw1zmvTjvp7ZmQ6WUqMdeMePm2NdIj2tnHGCwvSkI6wfcV9P2WF7ZfL24Oe12ba6dI7YtQaJIBGBCxcqp5dBXzskmC4vV8mDGI2dyuALl5N97AgberrOGsMUHseAbZpGpOpmKvsMKwkO0xvKFWbKKECTB4JgP1kx6VNjj-lXgv5rANr-OJimkhsKPcEnOIjNrK97d_xLXi9-6tehbIyV3ighCla4CJBBlUbSkm8CqCFsSRmBGlr3Gcs1Uld3Avip_TyjXMgRSQvXmePdLzGUudvajY5CJ8gN_mOdN3xcZj9Z7Ncji27CTaoqyswdbbr39eccMVsQuJ_6vzGUoWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
🔵
ترکیب احتمالی استقلال
🆚
سپاهان برای دیدار حساس امشب؛ ساعت 19:30 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28315" target="_blank">📅 17:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28314">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmh34n7gMTUNBhD6Ekolz7SJREj1Bb4MWRA8oKbghv7bkAqeUmbSiilBSNTyazHNmF602vMPnq9xISf3V2QzCqLFATsZhL2bIOaxSQ824baZ9WLesYNbUOgvxVY74aJU_C295sLtCaP_zZV66wgtQnWQd8vxLTwVe7RHSAzhv7WZ0kBWJB5meZKXZ_xjnXRvhhDcipWFvReHVTeKZrBGF5p_ftFudkqOl-AuvqjclkUi-KES5tkasOPtbYKj_fRcQPwg3ph_EHjhTStzL4C5UKw4my7N19uLCQifcHGXMhSrd6khTrLNtT5yxdzPpnwNHY4smJcbA4W3xRgfU8ZOxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محمد عمری ستاره 25 ساله تیم پرسپولیس دچار مصدومیت جزئی شده و ممکنه کادرفنی به او استراحت‌بده و دربازی‌حساس‌باتراکتور غایب باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28314" target="_blank">📅 16:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28313">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00386372ad.mp4?token=paYqQucyTQQyg5XXONnXIF1l6BpEEzZnDvc-mOuAoHtAUmu6lJ_pMvrHeVAKDa4ZFNZjdz-JqLhJKkDxIqANU_63OljBsenZxuXm3Wb1tth01qlvM1SpPbsxI8cEur-LxZ4Mcr_ctZtX5AlkjnllN5IqQ2lYf5tEflrqwl7BIDNJPUZRsJsfk4gUfdeu7q8eZBHr57vAs-wLQ3ZxLBTyhrn8wfRF8PtTpNSeqRSacTey_0pbkuvlQU9xwlyCYbrUnj9hAQg4B-OinlPZbIACbAwWHStimIQ8DW6kXTFaJdsZk2b3HhbuiKL90BvfU3OZPeTuFGt7LeFSUUfNBlJ3WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00386372ad.mp4?token=paYqQucyTQQyg5XXONnXIF1l6BpEEzZnDvc-mOuAoHtAUmu6lJ_pMvrHeVAKDa4ZFNZjdz-JqLhJKkDxIqANU_63OljBsenZxuXm3Wb1tth01qlvM1SpPbsxI8cEur-LxZ4Mcr_ctZtX5AlkjnllN5IqQ2lYf5tEflrqwl7BIDNJPUZRsJsfk4gUfdeu7q8eZBHr57vAs-wLQ3ZxLBTyhrn8wfRF8PtTpNSeqRSacTey_0pbkuvlQU9xwlyCYbrUnj9hAQg4B-OinlPZbIACbAwWHStimIQ8DW6kXTFaJdsZk2b3HhbuiKL90BvfU3OZPeTuFGt7LeFSUUfNBlJ3WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
🇳🇴
واکنش‌جالب پپ گواردیولا به مدل موی جدید ارلینگ هالند؛ هالند دهن سرویس بعد از اینکه بازکات کرده اولین نفر با پپ ویدیو کال گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28313" target="_blank">📅 16:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28312">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr5zZAgIQi9h9endlBlGtEHHbCu_KSCMP4VRFCZCKDafQMg37aXRVDX1XKXg8qd5wKJR_wuiNv9PRVclXjBuiINx6G2OS986jPmoBDc4Ppax7TcCCCPq_hWkdz1cedIyBWsZYp6Br6b1gb-EP-jwBJsz_3qL9vGLFQHKK96t0MWszZNhunMku7tKxxha43b1LYvcQlw_d6V2Sxp3G3zvBCm1UA7iuKiOcLOeKFxWNKeyT2is74o69F76Bj3XosyHEvUZDaijeXnU2KzZatETKD48UjgiB49DDw1_aRMlzoaudHSfVLPZuEvFcCKQUeMwBd42K4nUyMqbD3_KQoPp2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شماره‌لباس‌خریدهای جدید بارسا در فصل جدید مشخص شد: آنتونی گوردون شماره 17، کریم آدیمی شماره 14 و رودری هرناندر شماره 16؛ شماره 9 آبی اناری‌ها همچنان خالی نگه داشته شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28312" target="_blank">📅 16:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28311">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnt7SWENw6FIfqB3M7NvuWOyJmtppTXjpilkL7YDX9KTaSsgVlEHF8AZWxQJxE-1Z_hCgMw1bJdOaEpxRdumnQ2b8_JYxdvBKTxLILjrkhoRKOskfl7e7aiXRJ7FhDeicZHZ-4FqnGwYDXVaryq41fGH5ziosNu-6-TJYZGFqRigl9iAZaqUuRVy4Cm_oX_nQu3kpQ4Lljj9UnfZ7iixAlfnCEGQ9I17wrDTC65zKUyd948DxX47V5yUNVtsszRvq3YQDkwv2lVUu7SFC-ki0EWiVYx2sSvBbvCNbJ9PmenMFam3dLl4nZdqhAXl0AqyAa5-M0o8YfgM4AVs1JMtUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ازهواداران تیم شباب‌الاهلی امارات هستن که علاقه‌زیادی به سعید‌عزت‌اللهی هافبک ایرانی این تیم داره و با پیراهن عزت‌اللهی رفته استادیوم مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28311" target="_blank">📅 15:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28310">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lu1MCt1A694PY1rfme5B9qgmHo2-P3enRiAWD9sFiBNXY6kNlLKrYmq0Aqqj6oqS7ZzWc4BiMV15j8sdlPT4N5cb5p9TcvZZ95zNAHEZDkzpcz44s5H-7rN5Er0VsEcvs930DB4_5LDri5WAY4OHGVznJcqbU3TRMVAgU_s3UaLjjLHJi7YpDeUEuomGpfv1iMQ6WFlibXTDpUlliYFUdgekvdnp2LJ83yecqHhHtAgVIRkXgMHuYwWyMunt6b3jaJ99ESshFWZDrpTYltc9lLzM0McpRxPuguoxwkvR_fohxdNuUPMIfWgyz3fhTH-GLAKqZHnmOKt0e-TrP0ZeDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا: ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/28310" target="_blank">📅 15:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28309">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ro69xx8LaufW3EAC94j3naMWEZWnNKytaF_1OIZ4BmXcYTXpXrxuWVSzduhP5l5HT0GNKSrcqgawDMJBYeWxSQBS6zRwbtsosMeiLFLxkfAo8XfVnSxXRxIlkWq2l69ZpWKwPs6YatFdBQnPBfjBq-7l4nY9wwKagqwCLEmInL10LywC5zoM1FWujdGECzVdGzoqBRa_5tKAybEAKmT8iwubvv_iuS5Fhv6cC6n9bBMVwxjBvlGdsnJqbQoSET-LE95XUFf0lSqeUkioL4yUQtpyhPa75Y5BCbufmPKFshRIJ1qB_fEREMWjxZ_azz8OKUcz73qKnTWYWm1kEmAXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته سوم لیگ برتر ایران
🔵
استقلال
🆚
سپاهان
🟡
⏰
ساعت ۱۹:۳۰
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ ‌‌بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/28309" target="_blank">📅 15:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28308">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa9e980fe.mp4?token=ae_8f52uG1jol0UaSVIsQRYbqsR3lQHvW6B0103M9J8lZkNrVA2yHtp2bmSTXb5_V8_KVscGaH08FJiib3dPKqzy3ehmqgwO-d_wllP9ujYvTMu_3Qt2DAgmTHFP9WyTVaANmTx-l1RQ1MqE9TM95PNMUiI1nKGw1KHFiDKrW4gXbQR506sVaRxbfEmZ6tEhO0LmcuHIKQb399FNKkyKq8o5xArRiAIKYiYs2nTYnYcCXEJGdT8o0IaxQVXoPs1YFljl1TsC9dfrhEDxD35cBnMuDQr0Xu9d6l2DUoF7NlMygzXcTzRoUopNhSzvbdKJ66N59fmpKsdQtnkD-dmq_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa9e980fe.mp4?token=ae_8f52uG1jol0UaSVIsQRYbqsR3lQHvW6B0103M9J8lZkNrVA2yHtp2bmSTXb5_V8_KVscGaH08FJiib3dPKqzy3ehmqgwO-d_wllP9ujYvTMu_3Qt2DAgmTHFP9WyTVaANmTx-l1RQ1MqE9TM95PNMUiI1nKGw1KHFiDKrW4gXbQR506sVaRxbfEmZ6tEhO0LmcuHIKQb399FNKkyKq8o5xArRiAIKYiYs2nTYnYcCXEJGdT8o0IaxQVXoPs1YFljl1TsC9dfrhEDxD35cBnMuDQr0Xu9d6l2DUoF7NlMygzXcTzRoUopNhSzvbdKJ66N59fmpKsdQtnkD-dmq_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترابزون‌اسپورقراره‌دستمزد ۱۷ میلیون یورویی به محمد صلاح توی این‌سن و سال بده. صلاح این سالها پیشنهادهای زیادی از سعودی داشت. الاتحاد تابستون ۲۰۲۳ بهش حقوق‌هفتگی عجیب و غریب ۲.۴۵ میلیون پوند پیشنهاد داده بود. سال‌گذشته هم یکی دو تا تیم عربستانی دیگه بهش مبالغ…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28308" target="_blank">📅 15:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28307">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMduFw8TSGw1cJp4FuatQjkIMA53Y1inTXjRRm1nan1up80ywCSBjRjvDnSomv0BsB9oPXQ2aFImb3IYmjdaPBMa6p0fx_m9fJq1f1a2Zr2bfhm8oOYmjopj3J1dzalltkHqw8J29v8stcIMJUjk9l1f4Ua81z4Hb31nmzVQRF_mQD9JS89ykMkoiOP9TPjAfNnl765Mlp8-QAL5o0L1wT4gZNM5mq9wm0eG3RLuA8BKtc-WPb6hV9rFqkRU6Xp5ykwT9tWfH3v9Tc0FxhtnR6uoY_b7A6dnIvPCYF1SK0Hq-yo4nvYsu0MKaV2L467JmVvwrdJzwEs31ssuFRa74g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره‌نروژی منچسترسیتی بعد از مدت‌ها موهاش رو کوتاه کرده و مدل بازکات زده. ویدیوش رو تو کانال دوم گذاشتیم میتونید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28307" target="_blank">📅 14:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28306">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bbedbe559.mp4?token=Te5SZvXwEtxYbS5wtCITI1_QyehQU1e8iNEd43fhCR7ETFqGiU_Pui0zveDTK4KJB6zT6-ZZyd7oQWNjZz5amKXPU3rk6rWRb1YaRlsN8vfygauZeXyWoz4u9rVrLRmMJecRTzgBxJzrQMdgxrJ_vDDx4phF4TU798W4NKMvNeMafyyt7-9UUgQpB4Q6w5C_vhxXvmrgly82H8SDoH67JqISBnkjmNWFrBVLQc196RBKqOdCU5U2-vpc-RMmRo-urrLt9jtvfboxcHV1AwVtHqPs3F1Xx3f0dHYFBZ3naQQ34eIEuvMa_PqrMuY2u_hFRGvVUcPpxbtr0ZVfAOvTPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bbedbe559.mp4?token=Te5SZvXwEtxYbS5wtCITI1_QyehQU1e8iNEd43fhCR7ETFqGiU_Pui0zveDTK4KJB6zT6-ZZyd7oQWNjZz5amKXPU3rk6rWRb1YaRlsN8vfygauZeXyWoz4u9rVrLRmMJecRTzgBxJzrQMdgxrJ_vDDx4phF4TU798W4NKMvNeMafyyt7-9UUgQpB4Q6w5C_vhxXvmrgly82H8SDoH67JqISBnkjmNWFrBVLQc196RBKqOdCU5U2-vpc-RMmRo-urrLt9jtvfboxcHV1AwVtHqPs3F1Xx3f0dHYFBZ3naQQ34eIEuvMa_PqrMuY2u_hFRGvVUcPpxbtr0ZVfAOvTPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌سم‌رو از فصل جدید رقابت‌های لیگ عربستان ببینید؛ چهارتاشون به یک باره خوردند زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28306" target="_blank">📅 14:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28305">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/powXykHs7Fs8jmvfNxd03tZIOdPynUmOz6JLj7cHXPcZTTDnTOy_JKYx_fjy2ZNMIzRupH3sWsJc5rzq9me_S3htf0h81g-hDMUz3CiR_oyGX9Yq7SWPb6Ey-1O8Q1Q6QM_mw5sMtlfP6ZT42MmnApV5O7CRcV_XMiQtraNZER6EGy6JVgYn4eDepRjkq8JdJ23YmBPJhM4l219ZR2eZCCpZrNydyV9EhSqp277h_MV3-DwDEBjC89Tvm5SAfavIuNrlYujjiFgLiDzw1u1QiQ7Rs6EtJ-q8ATii-jbzE4cpY0SnAf4CE8Ohq_TW9RcLLdOvoOeFB9EODrMK8o_pYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دلار به 200 هزار تومان ناقابل رسید؛ یعنی هر یه برگ دلار بی ارزش برابری میکنه با 200 هزار توما ما!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28305" target="_blank">📅 14:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28304">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xy48jQdp5YAe1uwZtr801UpApzssTASmninC4PjfOgBPmFVMBnT0j71g8nN8ePeZMXk-g_CL-YaEWyXna14TLt-OJYPCuuUPJ385OL5pdi3ifHr6XyV56tXfa8xuB12zPw_bXgyT6PUJZJfVt1rChVJymbnEqmcF3wSLSfApllkXQvZuvnJQY-k9agMXMZ0nyoGlT8HKXaxr2kq-Eg9dbd7RRUEH9cu0eP1ZGnQIdUXPsFKR7xtd8Cr6lPG68rZGnbPzFFURHEOh3Y7g_xiuoyVZA-lgasfzgzhlvQQY7-eLT7icJrZzJ_ooydAw9K4Wd0Bz3UFVhKtmypsa_Dha_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارلینگ‌هالند مهاجم نروژی منچسترسیتی موهای آیکونیکش رو اصلاح‌ کرد؛ الان خوبه یا قبلش؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28304" target="_blank">📅 13:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28303">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBEJN3tB-uJl4Q3rU2mDRGwBAXqupXKP3sBgC7bJsHocJbFyP8XaN_k4W1FXFNdNPZ6UaYNM7KxJhLhez1rwX3lopbJEWsPr3-g4-PK0rvDRpHKJ6R1jRlI-Olm9_nU0Ji6AttXNdaWCX-XvA4gMfuuFYIaCeeNUuIa1snNM0Re4_rFbAVU_bD_W4tLZ_NfYmhH9Gow2qLlRFK_fBMEq6U43GldBsmVUIbNBS3ifFcATUHXcvrQoMYetQpoRgiMHxnxIo5g3AJTS6CbWHWRBJRtvqwY55JXIEU3b_FG_-doPnWg4Sw8OdUUd4-Xu44G0Zgux1Fr1HkUkAy1j88lIJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
#تکمیلی؛خبرنگاراماراتی در ادامه خبرش هم گفته مقصدبعدی محمدقربانی یکی‌از دوتیم تراکتور و پرسپولیسه و سران الوحده با هر دو تیم ایرانی برای فروش محمد قربانی در حال انجام مذاکرات هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28303" target="_blank">📅 13:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28302">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf8c217136.mp4?token=qp9gbTMsGumObmsh64S542MlPWnaI-5-0CLWoSKl77W9J17O5niBKRoYiIXOdMYQfR1tF4PETpNd64mZEYy7cYMRzGsPBRfSjxfx3TiHKLpECmNIG06GsxUCNpiu574U0aIkKaGLhhbPXCjt9WVtQ3m0WyRxWkney-diNsM1aHjiDUCdCgsVGd55uRZKiP3bg-Rfd6y6l1v5e8VUqIg6H56TPrhL-9WVIMv1lARfbBKDbrLo23tOZR_zkrJIhF9b82npU6qqhbuS0S07nMcRAYMCGrjT4mWKyt6P6CNIJNX6r7ceS_8n4liLyIEtBi8HBFAzaDknwSkXoen0rR8cmzQy5txK7c-6OVUSwnqFKHv4vWoC3sxfGrA8FGFNnfRewtDmImxstwypfPKL4lEtYebVHJmFNpUQ6MrEsYwd03YKWmbNm4-D8xdC82e0JwAXzNSqkuoSFxLaPtQLr1KMInnr1wbHN-RoYSZnAw19TVYZcpIhqsB6bldhUIq4J9AFxtXAx73E0JJyzfCEABVYZT9ZhOJaj-GSRf7U-Q5grtbqLjNtgiZkWucH4K3Kb2ch76UGs2j3kE2kqbR5Cw9r5lqhasmk-rXngUzPt2UMpvh1bbLhJQFsnlY7TPN3onCr7ZPsy-AdoCs7I7vEvN4dewi5HuQWvto2zKAbRg-0B2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf8c217136.mp4?token=qp9gbTMsGumObmsh64S542MlPWnaI-5-0CLWoSKl77W9J17O5niBKRoYiIXOdMYQfR1tF4PETpNd64mZEYy7cYMRzGsPBRfSjxfx3TiHKLpECmNIG06GsxUCNpiu574U0aIkKaGLhhbPXCjt9WVtQ3m0WyRxWkney-diNsM1aHjiDUCdCgsVGd55uRZKiP3bg-Rfd6y6l1v5e8VUqIg6H56TPrhL-9WVIMv1lARfbBKDbrLo23tOZR_zkrJIhF9b82npU6qqhbuS0S07nMcRAYMCGrjT4mWKyt6P6CNIJNX6r7ceS_8n4liLyIEtBi8HBFAzaDknwSkXoen0rR8cmzQy5txK7c-6OVUSwnqFKHv4vWoC3sxfGrA8FGFNnfRewtDmImxstwypfPKL4lEtYebVHJmFNpUQ6MrEsYwd03YKWmbNm4-D8xdC82e0JwAXzNSqkuoSFxLaPtQLr1KMInnr1wbHN-RoYSZnAw19TVYZcpIhqsB6bldhUIq4J9AFxtXAx73E0JJyzfCEABVYZT9ZhOJaj-GSRf7U-Q5grtbqLjNtgiZkWucH4K3Kb2ch76UGs2j3kE2kqbR5Cw9r5lqhasmk-rXngUzPt2UMpvh1bbLhJQFsnlY7TPN3onCr7ZPsy-AdoCs7I7vEvN4dewi5HuQWvto2zKAbRg-0B2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
🔵
به‌بهانه‌دیدار امشب‌دوتیم استقلال - سپاهان یادی کنیم از تقابل فوق‌العاده جذاب این دو تیم در شهریور ماه 89 که هفت گل تماشایی در برداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28302" target="_blank">📅 12:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28301">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dfe668338.mp4?token=jfIWPkl-5oUZiG-bKvCTGNCIqFExmcht_ugAl8YclhXFiLE3VizaHXO7hN6ZDXvDBlgBWVFMiLmAaWn8qG9RY4xfNKS6PWN-oa1wKVnmu31ePWH8i-hD-bGAbv77E_0KddEMEBqCIkpFMQs9qpuNMtWiVU2QlFTzUxK-r2M5UuYQDqFJ3PaHArnINHMYf0fcmLtDxzusuzTtIKY7F4Deo2F6yoPfQu-0W6geSHTDR2gM10JC0vKCPT8n46owqi4hy__ldJkKdu3feWY89yeaRJJ5q-BKUsH4W1NEYVaJXRJodPjuHJOzFfdL5wUalvdyWuQtBT2eH1BxZaBgAyaf9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dfe668338.mp4?token=jfIWPkl-5oUZiG-bKvCTGNCIqFExmcht_ugAl8YclhXFiLE3VizaHXO7hN6ZDXvDBlgBWVFMiLmAaWn8qG9RY4xfNKS6PWN-oa1wKVnmu31ePWH8i-hD-bGAbv77E_0KddEMEBqCIkpFMQs9qpuNMtWiVU2QlFTzUxK-r2M5UuYQDqFJ3PaHArnINHMYf0fcmLtDxzusuzTtIKY7F4Deo2F6yoPfQu-0W6geSHTDR2gM10JC0vKCPT8n46owqi4hy__ldJkKdu3feWY89yeaRJJ5q-BKUsH4W1NEYVaJXRJodPjuHJOzFfdL5wUalvdyWuQtBT2eH1BxZaBgAyaf9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لالیگا|برد سخت و نفس گیر شاگردان مورینیو در ایستگاه نخست با گلزنی کارلوس اسپی.
🟠
اسپانیول
1️⃣
-
2️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28301" target="_blank">📅 12:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28300">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3pY4HGKUcJ2iszyfi_kULpp4uUk0o631-XM2vUcPnHiG18wvTJuwydN7gKXt0ttMBVorsiQykgv3d1bd7i6Fcd3ltZGDyBp6fTn7sqbhAa-sPVGI37EM_c_mAgZvZQRVm0_Oe0CW2MS3lAM1hxkySgPfTB7wLRP8tcZbk84_UFbSAeK8tSRKXjlcWoylajqJNKz1grv7TocLZgZIdLlzTJ9EEQVu55lP55WOY4t9-i_blGENjY5w64cR5aKvgl5ITJUhTRIpml3g99JEVdTbwf8Mo1fnAEkCZjD8LaUVbBi7Xkfyelt8VHJo5t0EnvhS0TghQJPZIyG5bASCPnRmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام باشگاه پرسپولیس کوروش اژدها کش پدیده 19 ساله فصل گذشته آلومینیوم با عقد قراردادی پنج ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28300" target="_blank">📅 12:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28299">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGogk1Z_HmB1Rk9pQxSrgqpbsR3x7cq8fW1ZycD03oIWc8quK_TmSmeryB3yBP0xRHy7q_eiNlVckg0ov-Z6KBDbh0xMEB1BshnXt31q2o_5DvNR9NPLEPqxo2PP1U94nLWxxvjS1UxytJRFAU6il1QHGFO69yVgxWPK2KEzIdBbqg41WL3VDr2TdfQ7XCUchrsO0XHspJMdR3BAzqyk1o72tk6hq-1ev-FFD5HmUr1ePYrLk5A9DEKto9kOue4ybJ7LmDXn1IMjsfNr-7DyWIHhfTLYscZejDotuk98guOgfb1eQ93GDaZv34Or_iEtv7wDv_nxKPMeDrD7EAbdvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
داداشی‌های‌فوتبال ایران؟! پوستر دو باشگاه استقلال و سپاهان برای بازی‌حساس فردا شب دو تیم که شبیه به هم طراحی و منتشر شده است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28299" target="_blank">📅 11:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28298">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBAqx9EscWZhDEVr1oHI4sfKrgcrkdxXRMhZR76K6J_OzUJYknIonb2ahyMjFMtw9u4TzbRkAjlXDJByIQVWQvKwdmoQZC7wbDqnQt5Oth0SWM3uhBo6dGsTEEp0anzzTI-p0Cbn3OMPhgYwVv8Cp_g0RdO6WbLg_cbDafbmbNeNpznNQ2etUzH0S_LNJV9-0GOsklQ8JKC8vmxiBhV5vEn_7tfHYoNrKpPofiOjTYJHgU-qV5Xr3WIV9oso8fPOdsV7jnGSDjQnfvj7vyouwfzIdmTuCepW3DOI0J9lSzq5D4nU-va1WVmgvEUFchMt4sSQSjKGoe9fls2P6WSrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه‌تقابل‌های دوتیم سپاهان
🆚
استقلال!
‼️
این دو تیم تا امروز ۸۴ تقابل رسمی داشته‌اند که سهم سپاهان ۳۲ برد و سهم استقلال ۳۲ برد بوده. ۲۰ دیدار از تقابل‌ های این دو تیم نیز با تساوی به پایان رسیده است. درتقابل‌های لیگ برتری سپاهان ۱۷ برد و استقلال ۱۸ برد…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28298" target="_blank">📅 11:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28297">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2XLQ9HZo731IoFKhg2587QtKpLlBnM1s33ygpCZWu2LkTGy2HwPrSUc1bqiq7X7vYqcJnoIXE3qujE9_UNVSuc74b0j9JuKfsxpltYCtUXvasFHdFe36vPCf-SCRdPj4qa00MxXdiPJkNJuaVKM-iulOOwKGlAol2C2NosPlrsjvGltTEimEiZs-k_FNPEFPatRcljnNIk1N4LvjQJ9rRjfaQTQs7VXbtNM3gvho-QPCndYJN1gUyo0mMvZEiiMXnFl5ehD5y65qSKsrXa2icE6Idl-n-Ph0Uon6Oo4ApxTHQxqhy4qXfv7pJK5cV1BZdCbk3Wc-fMAIxNkEPnwyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی لیونل مسی در بازی بامداد امروز تیم اینترمیامی در رقابت‌های‌ لیگMLS؛ یاران لئو مسی این بازی رو دو بر یک به حریف واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28297" target="_blank">📅 10:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28296">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7MlxUbEDATZs4nITfRBiSt1yfKoi0MkmaOBh7pVBGfLg2ZrEu34Y4qOeTksp1IYITX63lIweo6LzHHRAG7f-HpGdolAoWzIhDVFhXJtzGL-efYBkBMIIoQwaMABrnf8s29AZlRo7TKpnfpnpf0hg5y9KdhCalJr4kPZMD_DgpAZ6OV14RC4ttCOOyn67nZlSWiKhsHi7W-YB16DPqGs9vZRK0BIo0kkc1MVZk8PltSJZPqp0xp1jIXSJWwZSbYzHZ6YjWxRbXd_iYlRPKlvHHp3aU8q4XWiiNP28S8MtYM5mWnz9BQ9MU6-V_FOH_EooJUuLSA82MeHDz4cEYS5HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
ترکیب احتمالی استقلال
🆚
سپاهان برای دیدار حساس امشب؛ ساعت 19:30 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28296" target="_blank">📅 10:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28295">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNyR_58ocjI5jwdJBQU1bKSSjkPVS8O6qZVmrbDJcE6eBBPtxKc5UtRqBb460X3bysubkV0Y5lhKwTLrT44C6ldgAcgkG5xmwgaUZMsSp1tTGuerd63xmeoLywtrdo1y7Lpm5sJodfRPn9JHBA4NZe8BHLrFNzamjshy1fXtL8xO7QqummLy6UuE20eoWX4nXB8VD5Pf7FCAUGCvnBnC4jnWa5dkY7Ks1CVP_Gu5EdvwNTjZzigsINjNvWQNDVoTgXpAivqzyonUGTuFHnYC-KA7XJMJku0vmFukEDrWf6sWYPMbvn9PnbyqFukrK0gjshT2k9uE1aHOjBCsuSyoSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در سال ۲۰۲۳ بود که لیونل مسی از یک رستوران درمیامی ۸ پیتزاسفارش‌داد. صاحب رستوران خودش سفارش را برای مسی برد و از روی احترام به کاپیتان تیم ملی آرژانتین، حاضر نشد هزینه‌ای از او دریافت کند.  اما ماجرا پیتزا فروشی همین‌جا تمام نشد!
‼️
چند ساعت بعد مسی یک اسـتوری از پیتزا با نام رستوران دراینستا منتشر کرد و همین استوری، باعث شد، به یک‌باره‌افرادزیادی به سمت پیـج پیتزا فروشی هجوم بیاورند. تعداد فالورهای‌رستوران‌که‌حدود شش هزار نفر بود، در مدت کوتاهی به بیش از ۱۰۰ هزار نفر رسید و این‌پیتزافروشی خیلی‌زود برسر زبان‌ها افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/28295" target="_blank">📅 10:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28294">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDOULZSo5i5qRfPNq9a7pea5vcAe7KZKr2K_ykll7EVzo2w7-ff4xVpOVJCRoRRcTo_8hgtfyKvA6UnuofjVATh8RFcxwxv48mqo6tUIQAZ6gBA3Q2WpmyiwiFYgtbu0E2kda9-13P4aLVkl5fHSPs9n9RI1QQu_rMjtqF5h5XfFFLubODilRy3xLVRO5l_psGcrybE4wlTTIIZ3_TEyiQgFfbT04KmRYqJdEGcuUcHVpBDpDHYDlDsdHPByNqKIFYNwl0X1LfcuVHiRuqpQ9xGmxBKlYUu673k_cemxUpjzFYmIazn8XHI0OnYwkvhsk8RXqrgEk4hbu7jnq3RQ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بدنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
؛
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://t.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28294" target="_blank">📅 10:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28292">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0aee2a837.mp4?token=q-5rbmS1I4MwBTNrPhEKHz8kBhVkwWISZtg71IaN3B_5yxpc-HJWfQ9CadAK37bp9M4MZUhyPexX1ViNuo3RgPdO8p63K04Ug83rL3y6G11TZ3fOXLjQ9mtnnfIabJ8yJYoRHCXsD_7nxCb-SZAGaA0T1iqQ-Ualq5XzEyHVenhwdSROsuTPM7ADD68ne5i2ek0xXG0v85xyhXhRuF-j4mStL7AyYygFzWo-mbaMnJaPV-hsYQm_-iy6AeisnLa3ijjZMczGO06o7o-QR2ISE7ojZIT_pqsjdb1v7oGwWuMYN0fi-OVX63G3HhXbJoR8zjUsUYZ5jATB4wHNTqGW5J_vPxGOcAAEiiZV9F4XxgehYmle7SCFznwLzuisDBl82gjorjab72sj29sbM58ceYvnnSQfIwN8Pljyv4zD0X3j7qXE6MVe64CG5CXyNvhI37Rc11B8glSoONQOeFPbCt1fH7Skpdb4bYY0YB8ICh_jqiREcvKurd0uTUM32Pv_hLU70AhEKlSTf0of0VBrc6TXHK_l_jYLYEe0iqulvTcviJjd6YCDvQoMLH3naqbNJ6LfjMLFZjNUFDx1_mJaXlP7hjL6z_kF2UZZMo4hxe5_oSIl2kby2RtIvt_eMDVPb2C7me2qe7xRTyiohWbGFL3CY6of3cOGlRyeecJNTDE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0aee2a837.mp4?token=q-5rbmS1I4MwBTNrPhEKHz8kBhVkwWISZtg71IaN3B_5yxpc-HJWfQ9CadAK37bp9M4MZUhyPexX1ViNuo3RgPdO8p63K04Ug83rL3y6G11TZ3fOXLjQ9mtnnfIabJ8yJYoRHCXsD_7nxCb-SZAGaA0T1iqQ-Ualq5XzEyHVenhwdSROsuTPM7ADD68ne5i2ek0xXG0v85xyhXhRuF-j4mStL7AyYygFzWo-mbaMnJaPV-hsYQm_-iy6AeisnLa3ijjZMczGO06o7o-QR2ISE7ojZIT_pqsjdb1v7oGwWuMYN0fi-OVX63G3HhXbJoR8zjUsUYZ5jATB4wHNTqGW5J_vPxGOcAAEiiZV9F4XxgehYmle7SCFznwLzuisDBl82gjorjab72sj29sbM58ceYvnnSQfIwN8Pljyv4zD0X3j7qXE6MVe64CG5CXyNvhI37Rc11B8glSoONQOeFPbCt1fH7Skpdb4bYY0YB8ICh_jqiREcvKurd0uTUM32Pv_hLU70AhEKlSTf0of0VBrc6TXHK_l_jYLYEe0iqulvTcviJjd6YCDvQoMLH3naqbNJ6LfjMLFZjNUFDx1_mJaXlP7hjL6z_kF2UZZMo4hxe5_oSIl2kby2RtIvt_eMDVPb2C7me2qe7xRTyiohWbGFL3CY6of3cOGlRyeecJNTDE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
گلزنی لیونل مسی در بازی بامداد امروز تیم اینترمیامی در رقابت‌های‌ لیگMLS؛ یاران لئو مسی این بازی رو دو بر یک به حریف واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28292" target="_blank">📅 10:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28291">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqfxIhP2lb0HAzwE5AWgE3jUR62rEuqDy9BScZQueZZyfFHKG-Y78An1vQw1QrIh3EOHPhDDI_76nQWS5VO6pKxosOrl1OYTWbksZhdQ6nF6K2URmnljaV_MGadIS7lE5hljL3r5_Y7awbX8Wi2OPnplzvfEbhoWSroP0dm5LRrxE-_CaqEAyF6VrRj0DkDgSNtt9xJoLaqGkCWIyY6PPVyd1GAkmEZaj4wVjb7Y_e-2NkL9McuG6ko0cDUgfIZaIVGiSMhGnJyIgJ4HYx0og-8wkD8BwkpigKJsXcsfncH2rSU25VdB33-_mI5t5HQi8MbIVO6dRPzzOumk6DqFYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ شماره 9 الوصل به مهدی طارمی مهاجم جدیداین‌تیم رسید؛ طبق اخبار دریافتی رسانه پرشیانا مدیریت‌پرسپولیس بعد از اینکه متوجه شدند که طارمی دراروپا نمیمونه قصد داشتن برای جذب او مذاکره کنند که مهدی تارتار اعلام کرده بود که سن او بالاست و فعلا نیازی به…</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28291" target="_blank">📅 09:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28290">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a83ce844.mp4?token=abdup8E7E4_1hI_W38-kz-57GsErQQ51Lk9bG8ApTK9vVGD8UKqZZR48dscI69baxhOnOrZPndPiZV1iJcMpkeK50FXVpwwsh12gp6dPwsP-S1svHImBswHrgwjI4awF8two74emXLgrVmB-IRJBQJImW2L54TuAaoAbOHV651q_2ehj23xaDk1_-tZYoeQ-i5DUEBgD8nAUn_Mb3BommUjWoy_tWfTJt_ZmPYi_hpAh1PptMjkr_Eg78IW9Cug0V5RivkLl_cOy7-diuUGBvzwSsyDmFvVxZ_eH2pXnmpVLH1UJlSWuRSWM3Ja-9dDtLeX1piPfygb-2eSuz-Uaew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a83ce844.mp4?token=abdup8E7E4_1hI_W38-kz-57GsErQQ51Lk9bG8ApTK9vVGD8UKqZZR48dscI69baxhOnOrZPndPiZV1iJcMpkeK50FXVpwwsh12gp6dPwsP-S1svHImBswHrgwjI4awF8two74emXLgrVmB-IRJBQJImW2L54TuAaoAbOHV651q_2ehj23xaDk1_-tZYoeQ-i5DUEBgD8nAUn_Mb3BommUjWoy_tWfTJt_ZmPYi_hpAh1PptMjkr_Eg78IW9Cug0V5RivkLl_cOy7-diuUGBvzwSsyDmFvVxZ_eH2pXnmpVLH1UJlSWuRSWM3Ja-9dDtLeX1piPfygb-2eSuz-Uaew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوم بالارد ستاره بریستول‌سیتی رور گذشته این سوپرگل پشم‌ریزون رو در دقیقه 85 به بیرمنگام زد. گلی که اولین گل رسمی او برای بریستول و نخستین گلش‌درچمپیونشیپ‌بود و خیلی زود به‌عنوان یکی از مدعیان گل فصل و حتی جایزه پوشکاش مطرح شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28290" target="_blank">📅 09:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28289">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">📊
🇵🇹
🤩
تفکیک‌گل‌‌های‌زده کریس رونالدو و لیونل مسی درکل دوران‌حرفه‌ایش براساس باشگاه‌هاشون.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28289" target="_blank">📅 09:07 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28288">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d382486c.mp4?token=nW2jdlsf7pbTp6r3AyifS83uqhXcIyMSI6uZrCG4Xgv9MmOfW0QTAogPO99dQwfWX7wVTp5EFTKSmFHXZVFTMMVOPVnSAU9TkujK84If-JKznfs-x3I2ufmsZyXxFK2oKzc3nVCgCYNiMlxlARcnWyy73qnYYr_3rd96-B0WV2fWmznX2vK0LD_riU9oirfLNHE7m76SuCy_ufplQHJOPlLfMJxM59yFBDQa8VCxtxLw7pqOx3fuyiCz7lBgHMrtd5vNNbP4Wx9t5h6Uj9fcRe8hOFBK392RMyPMNfz86Hq_rofsS9Ms6rq4mun4S69sdli4WpbA1KQMF8e8oWOxoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d382486c.mp4?token=nW2jdlsf7pbTp6r3AyifS83uqhXcIyMSI6uZrCG4Xgv9MmOfW0QTAogPO99dQwfWX7wVTp5EFTKSmFHXZVFTMMVOPVnSAU9TkujK84If-JKznfs-x3I2ufmsZyXxFK2oKzc3nVCgCYNiMlxlARcnWyy73qnYYr_3rd96-B0WV2fWmznX2vK0LD_riU9oirfLNHE7m76SuCy_ufplQHJOPlLfMJxM59yFBDQa8VCxtxLw7pqOx3fuyiCz7lBgHMrtd5vNNbP4Wx9t5h6Uj9fcRe8hOFBK392RMyPMNfz86Hq_rofsS9Ms6rq4mun4S69sdli4WpbA1KQMF8e8oWOxoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نون‌بیارکباب‌وسط‌برنامه؛ اونجایی که السا فیروز آذر گفت میای کار داشت به جای باریک میکشید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28288" target="_blank">📅 01:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28287">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKFTsR5BVL5DI1lSzIReX85nm9hzu_65r5Ig-otnN_tkh_pMn5eGCGCghorygyA247H0L2ltABTAVj2HykpV1W3mhK622GytX5MfwXC76CN4Yz1cO-I6EySP491trADsEJN_riWGocUpbnIMwhHmLTEpY2vAdl-IgmV-paQ4565NkTXtq3GmNYqpqXcgBWmagmUwoqKqtckuTtgNiFNYMXRsQ5thAE8hrNCabjsh-2a4ClMR6Xl04UkyDJCMGILWxLFxLlijRmF1KSiiv8CB2ICBYOev3iaHrtBoj7Pf0TJcI0ldlLnSIsGMPV6UGSNujgTfAQvAK0Yricf_C2Vfqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی #اختصاصی_پرشیانا؛ مدیربرنامه‌ های‌ یحیی گلمحمدی در روزهای اخیر نشست‌هایی با مدیران باشگاه سپاهان برای پیوستن احتمالی یحیی گلمحمدی به جمع طلایی‌پوشان زاینده رود درصورت شکست سپاهان در بازی فردا مقابل استقلال داشته. درصورتیکه توافقات‌نهایی‌بین‌نماینده…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28287" target="_blank">📅 01:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28285">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUpRepZXiDcYRldnru_uuG67guSypCFVQR3avLURO42VnyEMuQa3JIYpeOV1NCwdKtpaaObABVHd047JbyBCKDEYiNFOVng1jcCz-TZhgOpuOWGjTSfzlLGE0lFWM7qxrluytQaw1rZKgDn4oZbM9UEOoYa11pOnFpmdjX5gCkyLBdxCgcGsSg25BGE-Aj-xA5lqaUQkBQ0PR2cdUvdWOHGtOBfbiSot0RRkXpeaxpYOv8tNH8LmPU-3c7jtVWQcyegHyusCywQlfndxbATspYOQsqmMF06W47Gu6_3moEHpAXNPHQ7X456cGVawJ6T7KdZcTHusH6wTkjZqa7qcAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از تقابل استقلال و سپاهان درهفته‌سوم‌لیگ‌تارویارویی شاگردان فلیک برابر الچه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28285" target="_blank">📅 01:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28284">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cv3GiEDxpr4cI-THNjhkvNnTqj9C4o1dTfXYyaacwlzimPnR6R27MVAvS30kIQAST5PtfLOkT4BpWMHC90mX0jiIJ4EQOwWaaXg9Njsv3nJmIYICFpNJ4WTeyReQ7yfaOeZ1Rxtej29SQ5PzpHDlq-frPk5mDDAiKq4AGJTHtPYGouRLqW0lFUY3zI-pq6de1RJQPljF3wX7qo0myXsP27sSh0nJmNvGuHz5cjYkv885jBJsoMEAb_wH-sg8mx_VcwpQSLbWseXyo5zruLy8AX1yB9SEbezfw4kIHV6K6xufyhVcVZh1JgT8cR2a8WrjETxo-9xRjDwQHIpEIxpyiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌ دیروز؛
بردارزشمند رئالی‌ها با گل اسپی تازه‌وارد و سومین‌باخت پیاپی دورتموند مقابل شاگردان کمپانی این بازی در مسابقه سوپرکاپ آلمان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28284" target="_blank">📅 01:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28282">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLsFrok-_zJCPmU4Hoe085waELudl_pwfNSWi---7zzZHUiUhOEKCBUEDOusf30Kpp3b5DeNbwCdDJAmiCaqPXneu-tq75pAr7IsAqxRT5m_qBB9Q2-4_Ui4EpMSxp_KSts26yojm83KcEtL2sAZ0NSuQ56PQ94oOKKXczHWPea_RBgGMHS6X9THnTnjvqELbAN9eQkJOH9VnG56T-M0pxqne3brfT7b3ez69CwF9IwQKGXFhqD3vExt0iHq9zMi906WJLL57zHF95cVTT6HEcaJhM13dwAJ_jl9roy2SBZFO2CBALfanSIcuLy1C_lK0cKPSupMBlZ49jb5cjdRYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لالیگا|شماتیک ترکیب رئال مادرید برای دیدار امشب با اسپانیول؛ ساعت 23 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28282" target="_blank">📅 00:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28281">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMZ4j9trVBYgVLk8it8ESWWexaGgPeV1ZScqZFlvzLYQsJk0YGK1zVYIZu_IF8vXzIspFZUNHZufuKiZOhFSd3l-MPYWmxcUzYbaaucwpGFMaQhF3hWPAIlFWRn4GLVV3y97QkWEInwokef0l8EX3_XceWXuM2csYby76pRpRSy4txnEBO2L3bdCFloKtpNe5WILVMy9LnQfiT1Ej_jQYA1x2gr4-QI9EgRt7bW6Uep7BLeJNcx19v-VuT36l-DXFBqboahcjGet7g9Lmyec4uTQGCX8HyNJmAMv22YhRZwqosMCayklGQXVfJfTqRkqWsArrl9YgthLlxHAUyh3jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگردیم به روزی که هواداران تیم ملی کلمبیا رو سرو صورت خونواده داروین نونیز مشروب ریختن و اذیتشون‌کردن داروین هم برای دفاع از خونوادش یه تنه زد به قلب هوادارای کلمبیا و باهاشون درگیر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28281" target="_blank">📅 00:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28279">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1ZJQfyex-fgt6Pi2SfH73eBgW1Lc_AgclRagXY8wmMClxYahLH64wJTzET_R_o7NQTjozrPlFwH-dhWFOb9NZHmKGqejXiNInbDmcizj3qc_20C7fDQQOXtTaWRx4ug90YSiiqgE_151W-lMuuv0efnUxcUfjYa8MrMweQ-ZMLhMPcsBX9avUiRGir30KazRCmZf1pY2mO3LZJh45JBetKfIHPWK-A0bTKeew1gLW6Dam0oB1H9Wrl6S0sC3DHNlYEmKiX_Z17_Qrgm4ZDFNKyyW8nj8DJUiqAnBBd6E2ymij1Z9NGzeNr1UAUQf028l-caHwsaU3QiduW_3ByouQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rP7C3tNNHHxq7b3TFB3t2OaZ-PcgbLz-xZfPxtJmSw2EnV7QvF30uiHgAwpDFeM4grYxDfTPQUUxfsgTaEUBXAMyslF12Gz3C0K0Wl64VCyK_bvIwND5ae2zkLsXVVoadyvCnawQm8voNk0zbJun0QhVvsRbkZYdbJvY6OLlJzREY7mVwrYVQvao0HYzi6-8rpAdQoUt-ziqQqNBrAmJK2p2sUWTUhg5EPGhNCVv0khUkfhTR2R5DMlOHGeBj32SRxo3FnejqpL_5s7k8HWCz0Fg0x5UtkCyquX6JEK-f_EzknHTUJCXFAMTAbOwgvmDEQ9hiqPrgs8juC1lIB8OdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
🔵
ترکیب احتمالی استقلال
🆚
سپاهان برای دیدار حساس امشب؛ ساعت 19:30 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28279" target="_blank">📅 00:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28278">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phh2WLCa5O2zOg4MMVl-ipXfk-9huohMxHrrNV6-FoHyaoTOcsoO4B_7xe9uihE8X6XXMX4CC3louPluDKFKyocbqAAPjBG5Cj4YIwxv0pM69m6h35-zf9jTemGR0v1Nzzc9vFX8niOleYP10Wza7VwOSdBSF9J38JAL9Igk_84emhquWtmoIq8lA13uGjP4v7emGG3Yg_erwQRiKiF4xmN7Y-xz4AXBU9koNd50xsY4ZxsE3Z7MbHNN8J0QEIxq1n9rPFxUHLVslBtkRHlZjLnLGT-uSL9WDVqRjiHkL6H532Q3FT4pJlA9XdQ7oTcLCjv1eG-WhmGqZQPZ1eJhhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ احتمال‌دارد یحیی گلمحمدی بزودی‌ازهدایت دهوک عراق استعفا بدهد و به لیگ برتر باز گردد. بوی یحیی در اصفهان می‌آید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28278" target="_blank">📅 00:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28277">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jO-8KXtDaC3gkMLtU92aYPo40QdK_P_gOeMQea9mrMfQoR2dbRbyx4RzclciL5GqCoIrKh3WFh_8J4UI-kHZt3Qus1PWcdajKCO8GYmeKU0C17SVJ006UssnQLAI-7OT2Q8eiqKCMTRX1vs7cZtIwH77Pbztjnvz0OwmgtVdH4bh3grRFmals662zzRYZ7OVFWqUF1_BQikcnDUhdyYDIDX5LdL9tTPOlpu-pQ8KE7iYro5zLGmsXDTRVTJlz6_LXS0oiFwqxYTXUnJrWR7jP9A5-2X9UQoOFP_d4hqtlMuCFfXlQzbdRccYMRTCSCV2VmTREb3nHwPeSDnir50aUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سوپر کاپ آلمان؛
قهرمانی باواریایی‌ ها پیش از شروع‌فصل‌جدید بابرتری‌مقابل زنبورها در سوپرکاپ؛ کمپانی فصل شروع نشده اولین جام رو گرفت.
🔴
بایرن مونیخ
2️⃣
-
1️⃣
بورسیا دورتموند
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28277" target="_blank">📅 23:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28276">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdAZ02KuN7-mRiEhDWAUUDqgbdtCUkJTbJt5-gPpT2LMqrBqBTZeWNs_o3i6DdVZso3mKXfSxwLn_HNgPIwDEVqYAVA-TSqpePIqHNYTLS0qa3SXcDV7-p-7ruo5XLkr66-PdOZKlnbiY6qWBs1E4TKx6su7Scx7_AFxtyxCiAe6r6hwInKg9QMS9wYCJTtYUELCUu0Cs5vkM6PRRdwajHVD5b-mzVrseH4VLFCcP0LH1m9o6ZYQXOd0XriwMDcIA68uqwfYnCpvcbKL48f0kgp3o3CmlL93wyDbdbmR96FxQ3THYvy3NGXZS7qDVdfBHzX9XddVxiA116sipcCjIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌ برتر عراق؛ تقابل جذاب شاگردان علیرضا منصوریان و یحیی گلمحمدی برنده نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/28276" target="_blank">📅 23:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28275">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iD1bhZhGtJPXx1auBLgR_ofE7u4G5i-RiMhNSOSfYEJbOPmTWWkzafvVZfEj7en6Lm82nYir322bDLP0skkL5Be1BjuprZTXPmiJenTBfbVu0NGy_091YoBBmwAbkjfscTFYF6A4uzCawPcTL79Lm0YxOAwLYPNIbaGJiCo_rsO4YNmEMi9iEDSmqJvmYZuP76DqYlddBRpuUvTcYg1aApYRbIAsgfOl3G39lHMYR1XgrCkQhM8-v0cQzmNv7aNopJ4FdET2jQXxUiyX5QKr_PRNE7BqCBqTMtYCCeGwVUKJ-lu9Qa1NAZBqp1xjl4PWEu8V-tFQB0tY9HiZD1lRVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌ برتر عراق؛
تقابل جذاب شاگردان علیرضا منصوریان و یحیی گلمحمدی برنده نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/28275" target="_blank">📅 23:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28274">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0d528c86.mp4?token=U1GtVRDvXQOskKtP0JPP_IjZBF_zVC-DjnQII48XGA2aAbHLCVAh0q-wryL8Q5HvSM7PYeIvaKoIxWlSgjK80r6yI2YnD7aY0kcNbbP9nSdf3sRWekFPr72a_EZdoUC3e9YTyorCZ8B927gwPWjaEhFGB2JGaY1qYZuYdWrnN4ES2YGn-7bziOCDmBtQoMkuB9XaNudIv8w2dBg6Qvv9CD8ISu0ktUwSSeLIf66OP4biPv80yi0O0DRoq4PsUH90Ly-xhjxeGDJSAob1CZLizfUYkXC41un6kcUjR6IcnOIp6kM5Yr2_VQvr0OFkx1DCEjJnMmau2Jm7_Q7I1BH8cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0d528c86.mp4?token=U1GtVRDvXQOskKtP0JPP_IjZBF_zVC-DjnQII48XGA2aAbHLCVAh0q-wryL8Q5HvSM7PYeIvaKoIxWlSgjK80r6yI2YnD7aY0kcNbbP9nSdf3sRWekFPr72a_EZdoUC3e9YTyorCZ8B927gwPWjaEhFGB2JGaY1qYZuYdWrnN4ES2YGn-7bziOCDmBtQoMkuB9XaNudIv8w2dBg6Qvv9CD8ISu0ktUwSSeLIf66OP4biPv80yi0O0DRoq4PsUH90Ly-xhjxeGDJSAob1CZLizfUYkXC41un6kcUjR6IcnOIp6kM5Yr2_VQvr0OFkx1DCEjJnMmau2Jm7_Q7I1BH8cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اون‌هوادارمنچستریونایتد که قول داده بود تا منچستر 5 تا بازی پشت‌هم نبره موهاشو کوتاه نمیکنه رو یادتون میاد؟خواستم‌بدونید امروز 683مین روزیه که موهاش رو اصلا کوتاه نکرده و این شکلی شده:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/28274" target="_blank">📅 23:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28273">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3pSGQ4RLKQzqemIBQkPq-DkYL1kA9_1eE9X3kTdjDnqZevZwqVAjjjwzp2GbMhQh1hzxROmHcdyojIwoh5-aQHHwilUH7COI70CtmutcIqlMHVguY0h9bGuCyEAJ0yiUCjM0z-vESe9ZO9U_r0KwEkJS33nfxkebvDub-oqd1hYngICSwEIojxYZeFscxX-DoBZu4tY8Kf6QoFxbkOyKH09YpibtrtVF_RXoYLdMC4PazZyOUdkamPWckCEYOMmnASK9BVru3zBuJy4mnQtJpBuq1EzIWO4IfAXBJDGOhnC4xohC1C4Bo6xPPl0qQj9JmZetQhvh1zcYeS6kMaP_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇮🇷
العازی‌خبرنگاراسپورت‌امارات: محمد قربانی دراین پنجره‌از تیم‌الوحده‌امارات جدا خواهد شد. این باشگاه‌بزودی‌ازپیونتک و اوندر دو خرید خارجی خود رونمایی خواهد کرد و سهمیه‌‌های خارجی این باشگاه تکمیل خواهد شد و محمد قربانی رفتنی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/28273" target="_blank">📅 22:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28272">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9cf22c74a.mp4?token=vSr_QjZCeJEe7DSQsRKomydXConsSSkD4UtOwNxPrOgeR6omYhfzzBxp8xHEU4cOnMZjOWGvAof5y-C7Tw_31zEDCbGDA_BFuDyiVNDuUPCwygAjvhWl_-0a5rhAf0bbFlcNcQvK4u5fO9mXREtgWZZKQRPCtaO-2ngeY_OuZuDDn-U0YeteS_7sj0CDAjLwj4J2f987BuureGn6PYgzCbGlBnm94pLtr_1y6oIe-gbu-QnPn2pl2pi_YqztrzoZkYpSpZ9XwaE9CbxYK93qE6Vlg9cPDfFNhTAxcy7QAqAG_vtoHd0ZiZFCB3qiQviLyTTwPaycCv4eP3nCfsGsHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9cf22c74a.mp4?token=vSr_QjZCeJEe7DSQsRKomydXConsSSkD4UtOwNxPrOgeR6omYhfzzBxp8xHEU4cOnMZjOWGvAof5y-C7Tw_31zEDCbGDA_BFuDyiVNDuUPCwygAjvhWl_-0a5rhAf0bbFlcNcQvK4u5fO9mXREtgWZZKQRPCtaO-2ngeY_OuZuDDn-U0YeteS_7sj0CDAjLwj4J2f987BuureGn6PYgzCbGlBnm94pLtr_1y6oIe-gbu-QnPn2pl2pi_YqztrzoZkYpSpZ9XwaE9CbxYK93qE6Vlg9cPDfFNhTAxcy7QAqAG_vtoHd0ZiZFCB3qiQviLyTTwPaycCv4eP3nCfsGsHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌رقابت‌های‌باشگاهی؛مدافع‌ عنوان قهرمانی سری‌آ فصل جدید رو با پیروزی پر گل شروع کرد؛ تاتنهام همچون یونایتد شروعی نا امید کننده داشت و 3-0 بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28272" target="_blank">📅 22:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28271">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24c1f411f.mp4?token=a3NDoBmXLqjQQvtskQJ6kH4m9-BI4F-AYBEt6j8iUsNtE62Me7T8QNWocgTrhz02rv2pdw1dB1rfAAoMZOnSSdC1fTA_sUoW3bHVXBr9JhMdSp_fXSpjtwCYGmEkOvVCo9ktQNWj3QweoxHoJ8ztglHCvIHnHZNu1snxg9hs4slZ6MLKkL6Vwob7AO0xVBPEJg8-TNL-X1akoDBT34DnXKPyJYObxB1yVPnmdoPZJ4QpUTw-TBWahLejJodYCDXQ53v76_re3ltFnj0r7S8lloTjCdk-TFKXVVE4LNFkn42f_zfHY9ZbfdtrrW3LalnWLyRgPwuXaEO1WKBGzIZSWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24c1f411f.mp4?token=a3NDoBmXLqjQQvtskQJ6kH4m9-BI4F-AYBEt6j8iUsNtE62Me7T8QNWocgTrhz02rv2pdw1dB1rfAAoMZOnSSdC1fTA_sUoW3bHVXBr9JhMdSp_fXSpjtwCYGmEkOvVCo9ktQNWj3QweoxHoJ8ztglHCvIHnHZNu1snxg9hs4slZ6MLKkL6Vwob7AO0xVBPEJg8-TNL-X1akoDBT34DnXKPyJYObxB1yVPnmdoPZJ4QpUTw-TBWahLejJodYCDXQ53v76_re3ltFnj0r7S8lloTjCdk-TFKXVVE4LNFkn42f_zfHY9ZbfdtrrW3LalnWLyRgPwuXaEO1WKBGzIZSWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
سوپرگل دیدنی امیرحسین جولانی در بازی این هفته فولاد مقابل شمس آذر به سبک تونی کروس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28271" target="_blank">📅 22:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28270">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
هفته‌اول‌رقابت‌های‌باشگاهی؛مدافع‌ عنوان قهرمانی سری‌آ فصل جدید رو با پیروزی پر گل شروع کرد؛ تاتنهام همچون یونایتد شروعی نا امید کننده داشت و 3-0 بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28270" target="_blank">📅 22:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28267">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXvqwAGd5FEAmYM3p0tC1VHEcUFuvwUSDby2rY7ddUK6nV2GRIwmMWME7cuVAhP7uMuRQyv778VRJt6KARmSKk57HJCHd9KbglfGNLMF59s2M6F39ImasNHmgUfmWWqwNfAv461UoGdaUKG3_LWpSrlq-YFQeF6-ZtMYjV0tMmHWy1saOhCMN7N15k7fa0A6Zwbmz9NoCjLnicC8U2WuuugjBi3LNJi6mJcXdHxOcjg2hvKzFsqKrOHifUteWVN_Eo3PhLFSXFXOnt3vEWV-Cl0R-s88aQ25wSW4B3xEW_zO3ytXF-ouPtqAnfSPEf4YRyRwOGnChnHG7cjV1I0b4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JpKDGwSB_EkJpNQiEgj3drA7NgzvaDBcUfZ_jRGlhrT-xeAw_28AaBuYLm9NbDn49hTZN_sWb492gn5MwOXfvcsJl0UzOinj8aHSXTf5fGWUSu1wd82hgXtkiYsLMOyuPKI__ueYAESLITj5DlsAsnSl1P9zLJ5SYfJEDA8cLWzrQK6_Mz5PhzpGG0SQexje5dKXBl1cYB6fsOd3GI5SaU0-zaB3WvEN6XTrYpcefRWiv_u1nKtYcWYLcs0G6CMANvg5ecFTvzMHWUTdU0cXrtylm_MTNxQ5cHMA_w5KamTtPewbKbKXXVNfepTdLIP96_ezZ21Z1QebnhJwGbdBLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول‌رقابت‌های‌باشگاهی؛
مدافع‌ عنوان قهرمانی سری‌آ فصل جدید رو با پیروزی پر گل شروع کرد؛ تاتنهام همچون یونایتد شروعی نا امید کننده داشت و 3-0 بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28267" target="_blank">📅 22:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28266">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDFzlL4z5wgDqye1cCv1DnCQ7ETE5-0DXrwy9SVr6jAu89MEFuYdx6mVSBuXtdkMifccaMhhJ1PvTEqBcs7RiOxd82bzlX_pbT-P6RM2Vd0i18JMTZoO-CNLEXg0_DX-l4g3O14kVMFqA6PRoA7DdkZdCIJuCwOisaZzaukb56JksDzuKyHMXOLaY5mUAQiokFZwED_I08lZx94a_BBWECz-mdL_qcSSLQ229IeXslboOKpNzs238vd4l5eIGV735fdIg0NOwU1Vpddt7BXf-w791VulPI6_5IqEd2BKaqH2RZ2vBVVc-DdejnZ8rLbDeXgTOUO_HE4rOyDk7Yd9ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لالیگا
|شماتیک ترکیب رئال مادرید برای دیدار امشب با اسپانیول؛ ساعت 23 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28266" target="_blank">📅 21:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28265">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgHt9sj5NkDYTqoyidi_sfSGUrVp99U71meLjTo6HueMMK-NSiCasTNbMxo9rWcGJqJw0WiljqsoiF9FhvquC31cM22lAC3_uY6VV_X-9YpwPAv6j4cP5C0ydBV50LOm0bpD1XLVvI88LnXk9VmYIautCyCXqeV8HXzfryMtf_w-IjD7Q9NJ3QcUlPv1djqSh55vO5m_kLdQOnLvE7VCxdaLvsZUseMQrLPMIkyJebf43w2qKAe-froSBMq2aazWs8gMp-O0N20Bx6Z2KYwyQSncQxonb7VFpBCK8Xu6R0cLY5IAVSpTvIRnc4joBDEI5pkk6XiO9IA18Qk8L4Q_fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
24 ساعت از 72 ساعتی که مدیران الوحده به مدیران‌پرسپولیس‌وتراکتور برای‌پرداخت رضایت‌نامه قربانی فرصت‌دادند گذشت‌و‌خبری‌ ازهیچ‌کدوم از دو باشگاه نشد. رقم مدنظر اماراتی‌ها 1 میلیون دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28265" target="_blank">📅 21:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28264">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvvHT1r6ou9gwant-UtcLiBwgV7muAsmQWbbQbskaJh_GQhCuAicqMEqCzCL2klv2uq0nblwC0cYKAL_7BXfnJcyaKlKCvfzqPT423TtjAimJk1BwXfu51D1WZcWE8taaa2rKX6KwDMcB-Nc72LzPU82IipTBmkmocvBqFIxvbxd9J6JPDQfpMUqsyYS4vFYObRmBISeT_xTmlT23Q4pBgojLmHTvhhSDv1xiGkVv1upjX1KD2PqjV7hCrLdHJQ322mhoaC8tbuf4j7Rwuy_tDOxfZ9iSuwbWbo4CpW6lOsHK7cWUIEQbU6yq8BFD1wwSfq-hw883j6UhS4i_Q5tDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رئیس هیات‌مدیره استقلال: اگه استقلال رو قهرمان لیگ‌معرفی‌نکنند از طریق فیفا و کنفدراسیون فوتبال آسیا پیگیر حق این باشگاه خواهیم بود. چهار شهریور پنجره نقل و انتقالات تابستونی بسته خواهد شد و ما برای جذب سه بازیکن آزاد از فیفا استعلام میگیریم اگه مثبت باشه…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28264" target="_blank">📅 21:24 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28263">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/495f39b6de.mp4?token=V23PQuQboebBBmnnfjXg-ZIk3fRij4h9fIob-r1vURVsZezlr55d3sJycm2IP-4RBL1xN2yCsUnjFuKpy8nVqQHsBzZtUHInAelbDX7jAWptINXEC9aKrkayi-8splu8zdrl2MxrL0AAdV38ejyvQc7lE19r3wrmv8g31RbltpxjFw_r4WvbCPu0rLBAtaxCy3HHxQFdWsgi4nI7BhFk63OnvcJfEdY9dV76AlUHseKuLhdmGJS_QqEG2fg7i6jhXDVsuKbYHf8G7P1I0pAwr-hc1_nSiii8oAOcsLRPtyldGOf94ScdXSt4hSpdwpjfluMPe3GrSc0DVK6-CBTU_ScrmK3AAaoH_NiV0fTiJO0x5OCMkBaCJ1eG_O4lvFRbzwcsQDAPmFNluz8iiMiAfCB_r358VZn11nTg-ZgOrg5NtVeUrir0HCX25J1aQOHUA0Fpw_7Meqwfe2MkcF10t5WwHekH4-lt_t50PILkHe7jIq0Zpqv3Xn8idwVOO18UVdSId9_WTVFgavu8f0dr7CjbtbWOzoVRWWDZUGYKechE8BkMGWcp1PxB4z-ZKMNVUAhySC5uarJOPLJ0LvuzoINBKSagW9NyaK7GBtvz3ZWQFumvu6Gkg1HLjXpHeDCj30lrlFTSccOkJKLIsxYYnbhIA0u5Zmgakp1y0Vj3HYI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/495f39b6de.mp4?token=V23PQuQboebBBmnnfjXg-ZIk3fRij4h9fIob-r1vURVsZezlr55d3sJycm2IP-4RBL1xN2yCsUnjFuKpy8nVqQHsBzZtUHInAelbDX7jAWptINXEC9aKrkayi-8splu8zdrl2MxrL0AAdV38ejyvQc7lE19r3wrmv8g31RbltpxjFw_r4WvbCPu0rLBAtaxCy3HHxQFdWsgi4nI7BhFk63OnvcJfEdY9dV76AlUHseKuLhdmGJS_QqEG2fg7i6jhXDVsuKbYHf8G7P1I0pAwr-hc1_nSiii8oAOcsLRPtyldGOf94ScdXSt4hSpdwpjfluMPe3GrSc0DVK6-CBTU_ScrmK3AAaoH_NiV0fTiJO0x5OCMkBaCJ1eG_O4lvFRbzwcsQDAPmFNluz8iiMiAfCB_r358VZn11nTg-ZgOrg5NtVeUrir0HCX25J1aQOHUA0Fpw_7Meqwfe2MkcF10t5WwHekH4-lt_t50PILkHe7jIq0Zpqv3Xn8idwVOO18UVdSId9_WTVFgavu8f0dr7CjbtbWOzoVRWWDZUGYKechE8BkMGWcp1PxB4z-ZKMNVUAhySC5uarJOPLJ0LvuzoINBKSagW9NyaK7GBtvz3ZWQFumvu6Gkg1HLjXpHeDCj30lrlFTSccOkJKLIsxYYnbhIA0u5Zmgakp1y0Vj3HYI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جنجالی و عجیب و غریب حسم روشن درخصوص ریکاردو ساپینتو و کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/28263" target="_blank">📅 21:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28262">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46b6436f17.mp4?token=QZKaMO7uL9gmnKsSSQthsZXHTO-mXqCIV3DPG0G4c5W80DhnyJIkvpXHtVNoJHdWq9s7pU7hft19gw9SKU-ISfPrCTTYei4XRtaF2qxzZEOV-JPOJuS_0SqkolcM26kjagN30Ae45sk7FN50pOCXYyKTlysGih3_twp197IgxyV9wmCL4oxNoOA--FQn20j1BZlEy9xdWehpvgDf34tnpTIXM2hh_Zf8_NIoccFXO4YojS2Kz85BLJpolNLqb6ez60ck-VCMKU9MQ1pkIeHVP3wGTN_IPaMGBo7mLYFv2Qo3GdxMRwPmHa2jB2s80yu2uK-YI3ADul2kvDUTCoeBKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46b6436f17.mp4?token=QZKaMO7uL9gmnKsSSQthsZXHTO-mXqCIV3DPG0G4c5W80DhnyJIkvpXHtVNoJHdWq9s7pU7hft19gw9SKU-ISfPrCTTYei4XRtaF2qxzZEOV-JPOJuS_0SqkolcM26kjagN30Ae45sk7FN50pOCXYyKTlysGih3_twp197IgxyV9wmCL4oxNoOA--FQn20j1BZlEy9xdWehpvgDf34tnpTIXM2hh_Zf8_NIoccFXO4YojS2Kz85BLJpolNLqb6ez60ck-VCMKU9MQ1pkIeHVP3wGTN_IPaMGBo7mLYFv2Qo3GdxMRwPmHa2jB2s80yu2uK-YI3ADul2kvDUTCoeBKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛ دلیل ناراحتی سرمربی استقلال از علیرضا کوشکی این صحنه است که وقتی دربازی با نساجی تعویض شد با بختیاری زاده دست نداد و به حالت غرغرو رفت نشست رو نیمکت تیم استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28262" target="_blank">📅 20:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28261">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8wvlerlIWZns8q5eaBtG9WsBVioi5tQB3i1p_E2kZdvZFEkFgdNQXvPTV88Jvy3-1R8kn6h9dYeFidxgzmM2aII16yozylUtKvrx_HZl_I7wGxy1jIu6eH47h3Ud2waSqJjyGXE8LoC16A-swK3LfPuMwkuk2-0tDhNhAuhWFnxAUgM1ME6oDUUbzVdd567Hh0mE9MhvO_2CRcgZ41P_zA38HO82BFXzRvBjbItSJG7hfqvjZH71s7vA-ycJvWhH8fA2x2rHeNVgOG9n4r_dqj8Mb5fANUJIa0lyEEwt6BN8Ehd3Cu0Awq7rqPEwC_tTLNfW3sgUYyjZ9Ec25FX0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باپیوستن‌طارمی به الوصل. الان بالاترین سطحی که لژیونرهای ایرانی بازی‌میکنن لیگ لهستان و هلنده سراشیبی سطح فوتبالمون خیلی وقته شروع شده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28261" target="_blank">📅 20:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28260">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136a8275f3.mp4?token=oWIptEzpEC2kD29XoeacthCi2Qdq_nIKPtpqTlxrMxA4uU6tJVOupYdSqugHDShWXHKklL_EqIRRYzU0KX4hfasoFo09iwmHHZIYFWmZMqhvNTD0fKbl_HgxgQJBuZ_fCNxF8WjOxjM314n43bqwjatnA4wFUdyfGwLdaPLGzKB_EDMf_ZfTHJCM1HNReUebUEIepeL17cuO8w-JKfaNp0TGbWAauRCEy22toXtApGPEPbjf4trNXmXJ57Fnb1SbW_Toa3YIjDcNLbnjQmYFxmcJBfieiLnZM19OaODgiKwEEv0rJiaR-SZfZQ3KKmULd8COHJlBAhC29vsuTxfpXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136a8275f3.mp4?token=oWIptEzpEC2kD29XoeacthCi2Qdq_nIKPtpqTlxrMxA4uU6tJVOupYdSqugHDShWXHKklL_EqIRRYzU0KX4hfasoFo09iwmHHZIYFWmZMqhvNTD0fKbl_HgxgQJBuZ_fCNxF8WjOxjM314n43bqwjatnA4wFUdyfGwLdaPLGzKB_EDMf_ZfTHJCM1HNReUebUEIepeL17cuO8w-JKfaNp0TGbWAauRCEy22toXtApGPEPbjf4trNXmXJ57Fnb1SbW_Toa3YIjDcNLbnjQmYFxmcJBfieiLnZM19OaODgiKwEEv0rJiaR-SZfZQ3KKmULd8COHJlBAhC29vsuTxfpXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
سولوگل‌دیدنی زبیر نیک نفس در بازی هفته دوم مس شهر بابک با خیبر خرم آباد؛ قرارداد زبیر با مس برای یک فصل 8.5 میلیارد تومان امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/28260" target="_blank">📅 19:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28258">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdcjjOOP9cLVKkh-1F5RneSfCbOCAjpMAbxWAXi0SZOasgxfLYvvXf0ZYQ4qHX9mwvubDp7rgEPA-rzQJ9Oj4bJPj6WQuPcVMlo5DToOJJWItWSdHKGM--_1f8bq9tf5wvo1TZf7f30sDEJ7y9dNfRfIXUuAgtL1H1cP0zhqc4MK9xtOc6ksM-V2oxwj-q7LhL4wgpX_mvP5VrxDzdt1CZ5Io4rSJJ_n4j4RPrBxazqw6SkCQAl9YHNvLuv34TpWXH8GHsmvRqAWkpRMTj8MDcWiYlm5g-sq76XKztiIZqaogOURbzrqSM_c9i9PlpHiOlAPMS1ggZGbhq79_IR5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برنامه دیدارهای جذاب هفته سوم لیگ برتر؛ 24 ساعت تا دیدار حساس دوتیم سپاهان
🆚
استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28258" target="_blank">📅 18:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28257">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_apKGTUSZdM5Jy5h91s-nlxVWk3Gph4tyF7iUjL7DHzPb124DpcN2_r2P5Wh5M5Hb9sZH0iIlSYGpqLZpgvYf-4uzvrT-6cUJkxl3l8lrwnUwq3zt4Gmz0J7SIUljOBLx4m2Z3kP516gKOaDPNSfYP6jy7_YKFjvVgZLvJbNr22HkuVtDeP8k4JaP4gyIsZcRVtWehXI1MlKxq_gSkg0RKBQwe9pkKPm-z0v0g2Q7ja5BBr1jvy9wkEW6_PCGEmXqvtq-eKuSlaBUUzaIXkrz-Kv9JDlwVZ9uio2D8_xMIwEjSjQ8sOXvZJoNhDkGIs4o8anSek637gAREfOx3QSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام خبرنگار باشگاه الوصل: رقم قرارداد مهدی طارمی برای دو فصل حضور در الوصل معادل پول خودمون حدود هزار و سیصد میلیارد تومانه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28257" target="_blank">📅 18:14 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28256">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urKT92osDDn70kyX27CskIyxt16JCSsH8ShxLRzpt_XwhvcqNfZYIIbE87UY8thyu97IBumfj6elLlktq5DOIbeX7qNb9jVt7n3AShpim4bU5n2JeSAFOWqvrlI8RYx-wlqy_Dni60mMfXUOFhbR-40gv_ByF0qHrYA2U_PKzpQ1aDNMI1vt_SfFmRrWD6v0jh6fFEfFHAG4gQt-E1zSCqPDb-QxA4rvHWYa8ovLXwMnLXN4B11e_0uf9p6E8_7nDmGZ64RGyYaXA3CXT1v-ug1kquZ-8sytu8p1egIWqUEiubunKeBuHa85DhbpIcBa5NQVoJWRH4aWxiw18uHT-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ دلیل ناراحتی سرمربی استقلال از علیرضا کوشکی این صحنه است که وقتی دربازی با نساجی تعویض شد با بختیاری زاده دست نداد و به حالت غرغرو رفت نشست رو نیمکت تیم استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28256" target="_blank">📅 17:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28255">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e01212702.mp4?token=Bra92m6SkLxXL_9AQHpum-38Zb8Fi8QXDwNbGcDDKDGQ0snyExWqUCw6WH8oGhccf2Jl8GsJt7_imvTsumVY92PAmW-0bUaerOmLmYJoHgVCDE_85GwwpLhDM7X9DqEt-J0nY65Me4Mbbam_W_eiSHDjosrDHsRHdKWZvrZtIG86sI1z3-mN_3tlwdQIveImzdobKg8JFh0HzPgVhMt3q7f3bJQXSTy-aD2TVPvlH3xhSioBeD0vSfBgl2812YPxac-ZjDm2ywpb0IReR-2AXqT3X_mFXQot3F5lw7eLi0QuLoIshDq6DdlzRUQXI3C9r4aAuukH8JXSBDbYcgZ8FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e01212702.mp4?token=Bra92m6SkLxXL_9AQHpum-38Zb8Fi8QXDwNbGcDDKDGQ0snyExWqUCw6WH8oGhccf2Jl8GsJt7_imvTsumVY92PAmW-0bUaerOmLmYJoHgVCDE_85GwwpLhDM7X9DqEt-J0nY65Me4Mbbam_W_eiSHDjosrDHsRHdKWZvrZtIG86sI1z3-mN_3tlwdQIveImzdobKg8JFh0HzPgVhMt3q7f3bJQXSTy-aD2TVPvlH3xhSioBeD0vSfBgl2812YPxac-ZjDm2ywpb0IReR-2AXqT3X_mFXQot3F5lw7eLi0QuLoIshDq6DdlzRUQXI3C9r4aAuukH8JXSBDbYcgZ8FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هایلایتی‌ازعملکردفوق‌العاده دومینیک لیواکویچ دروازه‌بان تیم ملی کرواسی و جدید تیم بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28255" target="_blank">📅 17:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28254">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1l6ZPJYJw5GqF8YPlMkJxwCfuvmRy4OG7_zfeDn7yc-LlTYbjuA3XStLQCuGowYwgs56almbovLl18jyk1-lxtF9hoTCEv5xdyxTiONpQoOGOvpBGKA8Gs7--DaycT5a0ImPRCu7fPXnt1BodF2Ky71idhlNNwJg_A6mD3LwzzW6tbHyVqeruH9jeJVrWtPIYed-UGadlja83QX-IfGggkFI0q9yfRKnruIQy-rVoDDn4o4dNLOOreGjMxr6m1hsnQfGmWOkmM5ZEeUrlDEJ8uhmm07s7Crvl_g_fX-UR205CHKFg831XovYOMknsNpsfx6EZc_dUO1XYQosVXPnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ژوزه مورینیو: یه‌فصل بدون‌جام تو رئال نشونه‌ شکسته. حالا هر نتیجه ای هم بگیریم. شما میتونید ساختار روتغییربدید همه‌چیز رو بهبود ببخشید، من دوست دارم برنده شم تنها چیزیکه مهمه نتیجست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28254" target="_blank">📅 17:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28252">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyrJ0MEChq5Jd0FlKJlj3jlIVnPpfeIjWCWJTx0XLSvN4gDd0qccMqi5Z3U1CVBvJ9dYxD3-ybkzRqzhM8_EqY5C33n4MyJL9iUtG03FEh-Cw0hG6Idr8E5LkUDeLsvrDCe0KZrFJIiAj_Wznn2DEaDG8WftxP696T4bceMLNEIsOe5o4WqGGUOq6NnsP9_hOPP084RB6-9D1XcB-xSQe9qWriuo9h5R-MIn_26zmBAEdAbrhStYoZ9-7uQS0RRbVN4qQP5eZ20Z52RQTDwMlXN5wCmsAKvudaJGzcVmxblfIaKCoWErTRFRS9POlZ3OqIalD-9iWNM6ySM7EJ9EZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام جرارد رومرو؛
الخاندرو بالده مدافع چپ اسپانیایی بارسلونا تصمیم نهایی خود را برای جدایی از بارسا گرفته و بزودی از این تیم جدا میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28252" target="_blank">📅 17:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28250">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507b6b8171.mp4?token=DqD9hsFk9lIFfjYg1ht3YGnrI8_xOaiDLw9luBYkbcBMPkxNaBiBUeHCYt7jbap7nti927mf98wcgGJf7uOfmtv73bCvHxz5elHbeb9YQzEmeKbnuScbEttxRIP7WFUq-HqbJ9Az4Pawdbd7ubf2NwJcuwEZeQpmPTRT9J99x6ecQpyuCtyyIfCopC_qCBfmWDx38pPKM2C2e8xIM5HyYyMWX3Gah8mazh64anoh_diQZVdS13Y7hjRrRfpFePG_KP9C-Z59RZVF6SR-uxfpmDy0gkdRfHivsFGfygau9B_ZcXxt7ie7fzKU_14ZxTFfbCddP0oFyJpO6JPhImjwm4ujVqHzZvXH4Y45Fzk5gbdf9SA8CZoqnWwvEO1dxuHbuLURYDx4nfcntobmXjcESHdQXvXaWADIQrEPtK3zjBCWDLDrk41g7_M4cgiFkP8uo8G4JRQjhbnYGTdJGIQ6D6hghvXq6YfbQOmexdEzc3PXZF_0-h9kqgb1Q2Qgvzr9JPoOGRHLK2koCqlOMT3Boz4hKfZKwVsw6eXDjFjQiMyOWWbHYIxkLU6IM90ghV8QyTCfnPnaDBfkhAavmTg8YnzgHub1Ui1fN0t2USoX41WJ5AoSaW3AJz3n1qHW4YNuTzSu7MyKAT20LwAhvgDz0h_WipdAarMY2M7WYMbJh70" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507b6b8171.mp4?token=DqD9hsFk9lIFfjYg1ht3YGnrI8_xOaiDLw9luBYkbcBMPkxNaBiBUeHCYt7jbap7nti927mf98wcgGJf7uOfmtv73bCvHxz5elHbeb9YQzEmeKbnuScbEttxRIP7WFUq-HqbJ9Az4Pawdbd7ubf2NwJcuwEZeQpmPTRT9J99x6ecQpyuCtyyIfCopC_qCBfmWDx38pPKM2C2e8xIM5HyYyMWX3Gah8mazh64anoh_diQZVdS13Y7hjRrRfpFePG_KP9C-Z59RZVF6SR-uxfpmDy0gkdRfHivsFGfygau9B_ZcXxt7ie7fzKU_14ZxTFfbCddP0oFyJpO6JPhImjwm4ujVqHzZvXH4Y45Fzk5gbdf9SA8CZoqnWwvEO1dxuHbuLURYDx4nfcntobmXjcESHdQXvXaWADIQrEPtK3zjBCWDLDrk41g7_M4cgiFkP8uo8G4JRQjhbnYGTdJGIQ6D6hghvXq6YfbQOmexdEzc3PXZF_0-h9kqgb1Q2Qgvzr9JPoOGRHLK2koCqlOMT3Boz4hKfZKwVsw6eXDjFjQiMyOWWbHYIxkLU6IM90ghV8QyTCfnPnaDBfkhAavmTg8YnzgHub1Ui1fN0t2USoX41WJ5AoSaW3AJz3n1qHW4YNuTzSu7MyKAT20LwAhvgDz0h_WipdAarMY2M7WYMbJh70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
بااعلام خبرنگار باشگاه الوصل: رقم قرارداد مهدی طارمی برای دو فصل حضور در الوصل معادل پول خودمون حدود هزار و سیصد میلیارد تومانه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28250" target="_blank">📅 17:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28249">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2XFLwN9fDqxD_2BhpFSgUuNiEJT7S2DEMteMeQ_2Ttf8VXdEXh17C6qfAPgjySk0tdZtuC32Z6OyQmzT4sn-WBAR4lvDXHTsl0QkYBddhCcsbFAK2jMsKPWVUhvQiuL3g16k7-Evq1JT3nVWfPwcNsKn1CpyxbrFsqqiGn5Df-sbvpxz1MVFHiHdxr-6wJ-9Ijsc3N-Qjr74CBEN96_QialvW7ISu7LNWiWnli-KJ5M9lQjZPgYkIa3LXHMb_GJpZWLgxKCMHocFDNxN31QHPhxV-LPSRUSuYDEwQxYaiVhIwEVvU4tCnWapKh9W3y3L4Zowyup5tB57iHdqW1k0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
رسانه‌های‌یونانی: باشگاه‌‌الوصل امارات 1.5 میلیون‌دلار بابت رضایت‌نامه مهدی‌طارمی به باشگاه المپیاکوس یونان پرداخت خواهد کرد. با خودِ مهدی طارمی هم 6.5 میلیون‌یورو بسته‌اند برای دوفصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28249" target="_blank">📅 17:14 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28248">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7653009269.mp4?token=kyzs_4seHR9HERZexpKY0_aC6QFSjmEsrmvZL4UItSvMFgk3_fGKOxx1Xwdz0eQys4BnnGzuFTmUW2-R7P0KSm1p8l3QCGJs10omlarkkOUt3OWjWwM0JtSd5xKl4ulc07ldvcXUqfbSV-6utKU6FvTJpWvDR3J3WF4ulq4vT_gQF7k00RIz1zgeu70jacra1ZR-l9TQwQ-7jZutjcuYedsATQCfU8RcUvBkKzJcLn0JEWTlxZkEtHWqEkxX_u8v3KYW14tKWYYvSecsnzH2USXL3PxztmTe5-2jmZ9mMu8w2gIhU_TPepaOFZHIlOTqgQO67lNoCS5-J6IGhahZcXYlrXIUbXwB7yCfetiRPL0-FWRmjRvfOrGLAPC39usvpaQqJWY7mEjbGxcnvOFoISZbPCvlHEhICUNqfEpbCLayhDhx8sL0MWwTmOe2ebYjmr-dclGaJKsGAZ5eiasQHq4cyIml51WB8GjEG18EdUtklRsU62WojadpwrlPu3261fgi3xb_ULRbdt4l8LUPYKrHzqNNOiD801DpGhk7-kO1Eqecy6H_owbrUFf8MrYSWjzv6UJJgH_NJiz7tzthtEI3NMXpQf6bYHRFJ-LM-gIlf2KJyB_DRwjLzxjVTMhYultdiZl80zeqNFyuPJGyp366LW53lWrrzHuXhUKjPqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7653009269.mp4?token=kyzs_4seHR9HERZexpKY0_aC6QFSjmEsrmvZL4UItSvMFgk3_fGKOxx1Xwdz0eQys4BnnGzuFTmUW2-R7P0KSm1p8l3QCGJs10omlarkkOUt3OWjWwM0JtSd5xKl4ulc07ldvcXUqfbSV-6utKU6FvTJpWvDR3J3WF4ulq4vT_gQF7k00RIz1zgeu70jacra1ZR-l9TQwQ-7jZutjcuYedsATQCfU8RcUvBkKzJcLn0JEWTlxZkEtHWqEkxX_u8v3KYW14tKWYYvSecsnzH2USXL3PxztmTe5-2jmZ9mMu8w2gIhU_TPepaOFZHIlOTqgQO67lNoCS5-J6IGhahZcXYlrXIUbXwB7yCfetiRPL0-FWRmjRvfOrGLAPC39usvpaQqJWY7mEjbGxcnvOFoISZbPCvlHEhICUNqfEpbCLayhDhx8sL0MWwTmOe2ebYjmr-dclGaJKsGAZ5eiasQHq4cyIml51WB8GjEG18EdUtklRsU62WojadpwrlPu3261fgi3xb_ULRbdt4l8LUPYKrHzqNNOiD801DpGhk7-kO1Eqecy6H_owbrUFf8MrYSWjzv6UJJgH_NJiz7tzthtEI3NMXpQf6bYHRFJ-LM-gIlf2KJyB_DRwjLzxjVTMhYultdiZl80zeqNFyuPJGyp366LW53lWrrzHuXhUKjPqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
هفته‌اول‌لیگ‌جزیره|شکست‌عجیب‌ودوراز انتظار شاگردان مایکل کریک در ایستگاه نخست رقابت‌ها.
⚽️
هال سیتی
2️⃣
-
0️⃣
منچستریونایتد
⚽️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28248" target="_blank">📅 17:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28247">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNZVuiRLRQSKaQeYF8OkpY65DQHYWqdXG25u8ynWKQIfleiF2KssUeHk1ralU4D-8UfbsUT-CzAbcC0YJcfIFubjeEIxK9F6I7MqX58lNiPijGLYbN2QHDT9w_qbUlq_5YET6FzJzVZ0PJ9YeZbCw8KMx1V6suy95UyE9D7r8nF0pD4n1VGoeYzVm-WudZr7u96gSxd3iM4DSrQBFgq7ocgOQTD7l8HdV_fiI12offKiOw47zDvxYJPk3YCN3xgmp9ftPFnIgiRvtc7vkvJGj5uPvfXNgi2wRZwIwN_Nhi8f_6jXPNRO9R079AX-v3Sef-bQnirEk48zNdZEhHXnGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
هفته‌اول‌لیگ‌جزیره
|شکست‌عجیب‌ودوراز انتظار شاگردان مایکل کریک در ایستگاه نخست رقابت‌ها.
⚽️
هال سیتی
2️⃣
-
0️⃣
منچستریونایتد
⚽️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28247" target="_blank">📅 16:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28246">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbZ-4iEdgPtSPwdhQNJeQ8mlC1CY2YcTX4OMxl9xz5_lyPdW1cpfNS8oA5gATxVBFC4BC7Y0eAuLRYHBOQOiB1UyVM-q_6nNwJRI_yU2z4mW2rACtKVvD0sBcm5OQSaWR1fw298biG2e0RYR2Fgh_Jqm3bRacLNWlRy3ghKmW3GyCr4pt_7xaYH6cZaNtvJQ9BkMrSYmoG_YRxNMKQ4t3dMPPSL90F03M1zeDMVdhGPYihy2bh-gGpOkQKoq7doTdEvDHucchnjAczhmPaBMwb1IlYyqrZvweBHDA65tauje5CxZ3ysFJWQoHYWPC0fL8j7Srh0O3osE2FQ69IMS5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعدِ حدود یک‌ماه از بستن سایت و پلتفرم عادل امروز پلتفرم ایشون باز شد و از این هفته دوشنبه شب‌ها تحلیل رقابت‌های لیگ رو خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28246" target="_blank">📅 16:52 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28245">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOjE8kMIPO2iwckTA0ZneZwj6CmzTy5vhVK5Ckjl00NdmjlYmUuF-jwt-CacyB57bFpRLMISyLE7WdDwuMg0LVnWVhtsCcFcKdTIY5DS880SMv-m9lAbETuSMSwORk2Ub2otE3Qf8R3X6-bh-vCMil-02Iz5DueJCD7fKCp0-DadZqi5WR4Y4papt0uiZ7mAnHcy29W7mJ9YSQCqqhk1Y4VkKYOu_6eBWKIK-xi4ABNwOGygYgC4MUD_Ij7bPeA7q_VyVmgJExneV0t9GOXJddA9dx6Ht2U91mE6k7DqExLJ3T8LumMC7GBXBlzbnMd3hq19Q-TE2CeoyAOpC9aQAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌ادعای‌رسانه‌های‌اماراتی؛رقم‌بندفسخ مهدی طارمی 500 هزاردلار ثبت شده است. مهدی طارمی پس از غلامحسین مظلومی، فرهاد مجیدی، علیرضا نیکبخت، حامد کاویانپور، ایمان مبعلی و محمدرضا خلعتبری، هفتمین بازیکن ایرانی تاریخ الوصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28245" target="_blank">📅 16:25 · 31 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
