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
<img src="https://cdn5.telesco.pe/file/Bu7VwPAiDe0HgWd9MwAf7bpL7nhVuGYh-q5tuMwakQCqlxQP7OhtJJigRAdxLyw5MWa3mpy17CY4oOPmUJwgjfEmmAt9OX8yHEH2uDmqgiP_fNGWPoKs-o7OFlJ3ZfdmuIEW4vZ33QDHrgpThJ5DoCul3BsXERGfDpMSjDDXGzZFS43PTSJ2j3AqK-WzuyNOaRxo97lQyHBwqT_j92G69z0ejbzYMn57_rqWSJWQBExq10GZ-BnzEe3xF6hbYyltbpNixSgrzpXnsl2Yxra_K1C2Z_LeUlC_wDFVw-FedoZ0PLxMtbqbvycGnnXT3ntatXvpPRLRIpikpZAPf-XiAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 391K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 12:49:28</div>
<hr>

<div class="tg-post" id="msg-107855">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54734be7bf.mp4?token=SUOrWlfaD20m6KtJG-rCWVz7lqwNHoePsRDg8Cesui2cP4Y5dVvImJkbuLRqmDOQBoWsEhBOUI9E8DZKuKI3IbfoU3wI1Fs1BJymKOwvEu4KV6_u9iHxBv0O0GZM7eeOFG7_Zhk1w_BR7r53NMbG12GUniyVV8iR9l6qhmvo67cBZn17nIUTyiIoargddAYZtlZ9dYmiIBGsAf3LeAoJMgyUjyQpbtC32tmNKYcQGj9ffDboduMVmTUm8oMabB1-POJ8jou7rj5FMe0OlcI2oQRy09eDx5XZ-sPBZ3TY3qNt_wbPVsN5nVh3JyNzL9fQYsqqF6kr070fqATq41fOxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54734be7bf.mp4?token=SUOrWlfaD20m6KtJG-rCWVz7lqwNHoePsRDg8Cesui2cP4Y5dVvImJkbuLRqmDOQBoWsEhBOUI9E8DZKuKI3IbfoU3wI1Fs1BJymKOwvEu4KV6_u9iHxBv0O0GZM7eeOFG7_Zhk1w_BR7r53NMbG12GUniyVV8iR9l6qhmvo67cBZn17nIUTyiIoargddAYZtlZ9dYmiIBGsAf3LeAoJMgyUjyQpbtC32tmNKYcQGj9ffDboduMVmTUm8oMabB1-POJ8jou7rj5FMe0OlcI2oQRy09eDx5XZ-sPBZ3TY3qNt_wbPVsN5nVh3JyNzL9fQYsqqF6kr070fqATq41fOxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
خاطره بامزه علیرضا بیرانوند از شب پیروزی دراماتیک مقابل پرسپولیس در ضربات پنالتی …
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 914 · <a href="https://t.me/Futball180TV/107855" target="_blank">📅 12:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107854">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-nnFjcVNBWoDL05djS7sQ2VXNJ6ppY-bw4cCFUQinQLty0juMwpwI0dBnZHSXXwRbNWLRYZkj1-aCmJMFS8OtJ6XQsFDMHe7sBSLfNR1uAFHgSSraUDOXgWYAQ0oCCZsylHjCPoiTxqMtugKP-Wbeetx-VMSe4S4QxDu2lwmg0ZrmsbAz1o9WNOjyYHOY9zqP1wvxwr98KFEfRQ76fkNFw9yDLCphVtK7AHrXC8MezhgHPF00JVcw0cYhRnqL_UTF0bWMJrNlMJsWYyOsJ_CiEB-AiJfCoIWbUu9q6eFp2Kt_R-t9sQluVE1vinivPNA71vFydZMbZtDuWgujqQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
استوری مدیررسانه‌ای استقلال در واکنش به مصاحبه شب‌گذشته مدیرعامل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/Futball180TV/107854" target="_blank">📅 12:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107853">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AooO0Tdr-L8My6ZInB6T6CgziYMbBvj3mkKo7Q-hgbaF3_OAOl25d3R_QlA-ojwqDs5-z0w3NQ2-Ay6ukYEGsIE4wr6mP8iaCJ6Eb94I2JAmFJIaE6NBm31OJ_fnuFTb_4R7KDK8fscHvMUdNT1bKJXHLnYqqXp-zAho-RQfzDrDk27n_NCNgpIVtwZf59oOlRafxps2gF-1WptOoBNcpF3LDjpqUyVIXX4er0ZgmiG2JwZv5Hc65R_NSRlSxCX-AFniesis0mT5eEiVkyC4QZKGrOBlIfCiiMs42-eKulRgiQzsZkg-GfN52qRnL6bsuao-s0_Ii8I856qKoG9kEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
هیئت‌رئیسه فدراسیون فوتبال اعلام کرد که جام‌قهرمانی فصل‌گذشته به استقلال داده نخواهد شد و پرونده این موضوع رسما مختومه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/107853" target="_blank">📅 12:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107852">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f754e7f64f.mp4?token=aJyo7BOPIahDdsJUAv6NTGt65n80gxqZbTPxgs9I-tvm-V7ZY0pbJXHl1YIxpzZR8Hu5ocO4uKJOgNTApHW1Qx6cl9vBcih_AQsx2ai7AcxPj66GkHiQzg0p-_-iQ5dIlB3Mktkz37H7Exg5_Mx7cFA22tcjHs2aCBEXXJP1LbM3nt70X0E_jZ_pz2DBybY2Ubk3wHMbphle3KzgGPA_ukMvkXsHJMYt4WKXM8ffxDfPyVw86Qd1P_YqHivEgnE-IOXybz54RZPpTbuxub-gqTLG7VOGrS1hM0QAbbf3nqSV18SgPXajpNfTo9gr1sLMPWaX-FkjxDXLPg5sGUoxcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f754e7f64f.mp4?token=aJyo7BOPIahDdsJUAv6NTGt65n80gxqZbTPxgs9I-tvm-V7ZY0pbJXHl1YIxpzZR8Hu5ocO4uKJOgNTApHW1Qx6cl9vBcih_AQsx2ai7AcxPj66GkHiQzg0p-_-iQ5dIlB3Mktkz37H7Exg5_Mx7cFA22tcjHs2aCBEXXJP1LbM3nt70X0E_jZ_pz2DBybY2Ubk3wHMbphle3KzgGPA_ukMvkXsHJMYt4WKXM8ffxDfPyVw86Qd1P_YqHivEgnE-IOXybz54RZPpTbuxub-gqTLG7VOGrS1hM0QAbbf3nqSV18SgPXajpNfTo9gr1sLMPWaX-FkjxDXLPg5sGUoxcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
چالش فوتبالی با چهار اسطوره محبوب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/Futball180TV/107852" target="_blank">📅 12:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107851">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atmqeKrhVYIu2bCckIZEtkNACAZOkXbzuqYvn_wV72n6YJNEYsme6eoX9gZWkpL4cU8CJnI6Y_y_TTqea8oi3R1H4fmSOOkCub7wXVGiz2vNcpcseSIpsiA-XuRTIamNdDSZe3yfcQI2LyPcmy-KJHH6PsKimeMnrahJo0rMOmsWEg3k_NDW5YdwlnBBdYnU1q79zYtvNL4m96NoTamFeEkdLYAr2MmeHDdto4eTHAiKwXNbXz594UAhNgEY2bpx7K8E2e3QwD2TgagyhDv5UBLjJNJzjfvU1NzFW4aL0uGJIgDyDtkGSGZItqUuoVzdbC-Lx9Q62VBnaBi1eRTnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
عملکرد مهاجمان بارسلونا در این‌فصل چه در بازی‌های باشگاهی و چه بازی‌های‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/Futball180TV/107851" target="_blank">📅 11:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107850">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fd2204c7.mp4?token=JPE-f16qXeogq2iynClAcluTQBc0gib6HPFrgh130Jh1KliG01fMNvPIk30YqCka0ylpC_HB1kkPeSzD5aM7N-tXmZqjdLRSW7XnuJVhnoMNUZ4oZI16oQOz1S9xNIlD5UZFwbK20JXzLDFYnf27Ar7GhQX4tgrLJFkktyMeMIVUBwx-A1eFHwDyBH789c8pBtKx0HNZn5bPzIwdBz0LbKor2-oIajQJoG5kFI67yyOrlY6L-Oyhkw5WydvNKNPqMX0noOm6Y3afkw5sVdeqG9gZcJwi8IbzvVpDlVOFeH9i3KCOgLslbJ9xgySWT_GycChladrNCvC7UFf60GQkzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fd2204c7.mp4?token=JPE-f16qXeogq2iynClAcluTQBc0gib6HPFrgh130Jh1KliG01fMNvPIk30YqCka0ylpC_HB1kkPeSzD5aM7N-tXmZqjdLRSW7XnuJVhnoMNUZ4oZI16oQOz1S9xNIlD5UZFwbK20JXzLDFYnf27Ar7GhQX4tgrLJFkktyMeMIVUBwx-A1eFHwDyBH789c8pBtKx0HNZn5bPzIwdBz0LbKor2-oIajQJoG5kFI67yyOrlY6L-Oyhkw5WydvNKNPqMX0noOm6Y3afkw5sVdeqG9gZcJwi8IbzvVpDlVOFeH9i3KCOgLslbJ9xgySWT_GycChladrNCvC7UFf60GQkzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
خاطره عجیب حنیف عمران‌زاده از وسواس‌های فتح‌الله‌زاده: حاجی توی عربستان چمدونش رو زیر شیرآب شست می‌گفت با دستمال کاغذی کنترل تلویزیون را بردار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/Futball180TV/107850" target="_blank">📅 11:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107849">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8daf57827.mp4?token=HzCgT57ZTnCJ_xraI9aqCqwkgk8brtRf3RJ2STJcH5SNtZXgKc0yZSUJoAlturYTLhb9F6HcTA6OFMf5ZspSVPIjUtIz54dF58uZVNe8pTQmz4jF35zXoYZVJC0BkPoyDdW3GyIc2s_aUr7XKJuR0HpupCW_mZX4DiLL8nIVOl6Vo-jV81GFG9F9zomyoymbnQZWsWoUryhYtjbWbBK65K8WdS9NzxL-uYPp6g_b8YweWIBl--tWaNr_79g9oc0xpXGWqePE5MurZBigqLgyP1bPoTRKAoGrRcogZMT1OIc_9PmDuPxuFC1MhHi5oJdgRF1Js2mqH0GW2VcNwd7elQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8daf57827.mp4?token=HzCgT57ZTnCJ_xraI9aqCqwkgk8brtRf3RJ2STJcH5SNtZXgKc0yZSUJoAlturYTLhb9F6HcTA6OFMf5ZspSVPIjUtIz54dF58uZVNe8pTQmz4jF35zXoYZVJC0BkPoyDdW3GyIc2s_aUr7XKJuR0HpupCW_mZX4DiLL8nIVOl6Vo-jV81GFG9F9zomyoymbnQZWsWoUryhYtjbWbBK65K8WdS9NzxL-uYPp6g_b8YweWIBl--tWaNr_79g9oc0xpXGWqePE5MurZBigqLgyP1bPoTRKAoGrRcogZMT1OIc_9PmDuPxuFC1MhHi5oJdgRF1Js2mqH0GW2VcNwd7elQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
‼️
سردار آزمون به دو بانوی تکواندوکار ایران یعنی ساغر مرادی و فاطمه احمدی که در مسابقات آسیایی مدال کسب کرده بودند،‌ نفری یک میلیارد تومان پاداش هدیه داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/Futball180TV/107849" target="_blank">📅 11:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107848">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👀
‼️
🇮🇷
صحبت‌های شروین‌بزرگ درباره پیشنهادی که در فصول اخیر از پرسپولیس دریافت کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/Futball180TV/107848" target="_blank">📅 11:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107847">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107847" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/Futball180TV/107847" target="_blank">📅 11:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107846">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRMOMtiCNAArsRAaCvPkZFncgIeWvGAwHJbQSRsMy9tpdeJIKTtv4bpPiVmaC5Da5-n-5nU_4F6lpzkWftwRoppt1ETySlQEIlqDcvtTyeTycl_4S6JrG_BpANpJrbMziscpatZ2Zy9sSd_DIAxfxNzEIiZrbONrZSnCOE4pRrs1P0MEDjH4KhpmmBiG3_XkefkiucC3uSUSouRR2FVw5BfxMIWnzsCMckNRlILwuAzmkzs2wTAVP3HEdAYJOcFwn7l2egsElRweOtVSFc-AYBS0Ouq9b4AVXVRQDeujLXLKB72Izigmlo7WzZa9MqQt6u9ozb3wL5JML8G04NWlHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
فرانسه
ترکیه
🆚
ایتالیا
لهستان
🆚
بوسنی
سوئد
🆚
رومانی
نیوزیلند
🆚
ژاپن
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
http://T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/Futball180TV/107846" target="_blank">📅 11:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107845">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/294e1e1160.mp4?token=XXLMkEgDfQR7b_FxvJxWHdbCznT-JNS8rtEe7iLpbTl2I9ygV8ScJCYUTSQfr0mtUeztRDv6Gs2NykxkBSO11v-Qy8xCg6esZ_GcJygAgTW8VtMLD6oBdbOEwijyxWyY80r622Fuehl3Vk1td091dHbCPdFu4jnYxghuGQNk0k-gA2dtlbHWnw3HHVeh9i7MEgzKuDp9TdPeo-eYOYO82j2irNx_YDrZw5zCubHFk1rFZpdBqdZLWQfp18D2-4p84Dl1ZcL918PWSQtildPeJ1WNzGW1i4toa-TKd-mp_F1U7MWVKPg4OFpxeCJM7wv2oqLXf5y3nDV12y7650imlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/294e1e1160.mp4?token=XXLMkEgDfQR7b_FxvJxWHdbCznT-JNS8rtEe7iLpbTl2I9ygV8ScJCYUTSQfr0mtUeztRDv6Gs2NykxkBSO11v-Qy8xCg6esZ_GcJygAgTW8VtMLD6oBdbOEwijyxWyY80r622Fuehl3Vk1td091dHbCPdFu4jnYxghuGQNk0k-gA2dtlbHWnw3HHVeh9i7MEgzKuDp9TdPeo-eYOYO82j2irNx_YDrZw5zCubHFk1rFZpdBqdZLWQfp18D2-4p84Dl1ZcL918PWSQtildPeJ1WNzGW1i4toa-TKd-mp_F1U7MWVKPg4OFpxeCJM7wv2oqLXf5y3nDV12y7650imlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚪️
حاج‌صفی کاپیتان تیم قلعه‌نویی: امیدوارم در‌ جام ملت‌ها باشم اما قلعه‌نویی‌ دنبال تغییر نسله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/Futball180TV/107845" target="_blank">📅 11:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107844">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‼️
🎙
🇮🇷
🇮🇷
بی دلیل از استقلال تعریف نکردم؛حمید مطهری سرمربی فولاد خوزستان: کاش سهراب بختیاری‌زاده خارجی بود!
🔺
حمید مطهری می گوید اگر نتایج سهراب بختیاری زاده را یک مربی خارجی می گرفت، همه کار برایش می کردند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/Futball180TV/107844" target="_blank">📅 10:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107843">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZVxP3tVogRrY6Iz4Ucn5FAmedTtZaXNZqZCUzjcOdplY9yT8KuMH4sfTQALqsq5u--ngRU8-t_GaZ_EERwU8nWUB7Ukwy1AHEAI10zIp5HT_jCJR5wI9lZOvR6a7-GUlGQbOexf3n5QhZtq--1MAIvTJUCYN1m56an085vL3HHE7JdQLgYz5hyEqzhntLcoxoX4-p_45y5WIrNgchAceUR9faZecwf1G5mjrxG0UCFU1dJNVMb5pfmHOh2PbVmybcBqPgem7F4ZmFdQe4ZsmCzs4nlEz_CMsj9pM2Fx_rWIvS0VtmVc557R8CCTt4qDD6_HfoDFF15IqEzO3sCsjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💸
گران قیمت ترین بازیکنان اروپا
⚡
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/Futball180TV/107843" target="_blank">📅 10:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107842">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75399136b6.mp4?token=Tz8JhZsFJJET9e_OG_C_OUhqAuQvfFxi90wBnHuvEm47Fj5J7nHwmOr8jTWwB6obCkY4X1cM3IP2E3ksuP6oBBhmKt6_rdZnsJsvu9Zn8JIMZB-PnPmRhAb5MxM72LBO-jUCpinJd247nksMO5i8WhdWyi-vZpylBTlTzcfsoKHh_cA9VghPaxSuZ47jIiX8h5WoywnOuXo8ZeiG7vGcN9mEwYpxtn3FwqF1Agwo9bNTZdRXp5DJntDltXxcYA7xGwpYujOE4dlYZ7AgIUWeNkRXJrfcav7Y0xCXMMKIoVo-cINPZu_JNNn-Vtth9dJVfNS5Y_orOTsFI8zGyyYDM7ioQdqTaazG1TToK9be1VPtJyNeG94u2pRUwmhS1kVvUMz8NeFnDg5cEtT4mFsXA5VdBa0mYDGKhZi5OJPg-oNrC3B64ml7pBB28sWjBr54FyoX-Cglh3ByC3wAF99c6Lid9DVma2edthye3hP5r9-R8mEAqy_m3_LZ6qxTr_SEhFLbGAWg6FQPh5qHcSKdwg1Waxyaiv-7MN3HUg2FHVnvksEybLqQpDr1f5lScRWtg1pAERb875zQqJmQNKSNezaui0tjRU1M4LCBUxGx-4gDe2f4VYRHZGS_TECpmFa0IlWrMOt7MPazv1sHJFbi6Zl-bhHOemjayvAdnxxWGDo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75399136b6.mp4?token=Tz8JhZsFJJET9e_OG_C_OUhqAuQvfFxi90wBnHuvEm47Fj5J7nHwmOr8jTWwB6obCkY4X1cM3IP2E3ksuP6oBBhmKt6_rdZnsJsvu9Zn8JIMZB-PnPmRhAb5MxM72LBO-jUCpinJd247nksMO5i8WhdWyi-vZpylBTlTzcfsoKHh_cA9VghPaxSuZ47jIiX8h5WoywnOuXo8ZeiG7vGcN9mEwYpxtn3FwqF1Agwo9bNTZdRXp5DJntDltXxcYA7xGwpYujOE4dlYZ7AgIUWeNkRXJrfcav7Y0xCXMMKIoVo-cINPZu_JNNn-Vtth9dJVfNS5Y_orOTsFI8zGyyYDM7ioQdqTaazG1TToK9be1VPtJyNeG94u2pRUwmhS1kVvUMz8NeFnDg5cEtT4mFsXA5VdBa0mYDGKhZi5OJPg-oNrC3B64ml7pBB28sWjBr54FyoX-Cglh3ByC3wAF99c6Lid9DVma2edthye3hP5r9-R8mEAqy_m3_LZ6qxTr_SEhFLbGAWg6FQPh5qHcSKdwg1Waxyaiv-7MN3HUg2FHVnvksEybLqQpDr1f5lScRWtg1pAERb875zQqJmQNKSNezaui0tjRU1M4LCBUxGx-4gDe2f4VYRHZGS_TECpmFa0IlWrMOt7MPazv1sHJFbi6Zl-bhHOemjayvAdnxxWGDo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇹
آنالیز انقلاب تاکتیکی گاسپرینی در این فصل با تیم آاس‌رم که حریف سختی در اروپا خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/Futball180TV/107842" target="_blank">📅 09:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107841">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
🎙
محمود فکری: باید به قلعه‌نویی حق بدهیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/Futball180TV/107841" target="_blank">📅 09:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107840">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75fb30e6b0.mp4?token=qgvLYcnk5mfCSooUfsfYVI4ZPufLkjRY0agBTX2LgGrktTBRhXbySws-9HU2RdNHZRj9j_2AelTVk7EX0OoBkxSiLf_8lrqS-iWOAfiKs3bNDM3MSkEtlgT1lL9jtKVJLBNkl7MhBn1qiVCW5aK9Pj769DzEXwnLHTGHaa_UF6TPqQMhdagTV-yXMNjYdsRKZcYYK6-7MDixojIN8hFeK63F2Pc1w99C_Z8k5CzlaADwDhNaBEKCKUEi2YdJAk_Kt0ntETURCK0zHBT4tw5OlhmwRS8mxZlGXSVw9izKDSxR3R1orarc1ouZruRibFjqJ3iFyXW7sF25EpmsJbhmCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75fb30e6b0.mp4?token=qgvLYcnk5mfCSooUfsfYVI4ZPufLkjRY0agBTX2LgGrktTBRhXbySws-9HU2RdNHZRj9j_2AelTVk7EX0OoBkxSiLf_8lrqS-iWOAfiKs3bNDM3MSkEtlgT1lL9jtKVJLBNkl7MhBn1qiVCW5aK9Pj769DzEXwnLHTGHaa_UF6TPqQMhdagTV-yXMNjYdsRKZcYYK6-7MDixojIN8hFeK63F2Pc1w99C_Z8k5CzlaADwDhNaBEKCKUEi2YdJAk_Kt0ntETURCK0zHBT4tw5OlhmwRS8mxZlGXSVw9izKDSxR3R1orarc1ouZruRibFjqJ3iFyXW7sF25EpmsJbhmCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
فوتبال جا مانده ایران از امارات، از زبان شهریار مغانلو؛ دانیال اسماعیلی‌فر و برشمردن مصائب هواداری در کشور ما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/107840" target="_blank">📅 09:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107839">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e551facae3.mp4?token=MRk2nAqMLLtBzkb8Qme6RKN2r5iJYg4VZxFK4WB0aMTyFyzVU4a2tRX2kho56AgGrRS00Z7HvicSvf1ANHyrXLebEDpkoma-T9sdPZkP567mZbnaO4hM2m74NUA2b8SSnbvx-Z3OZ50bU8ksdY33C_gkWKdOPv4PtOQ21QAPgFRsstPjYqKZPJLdUxZf530z6DlhaVBTijpRmnZ5vR__PLnlNPgsNbapIV5sYHQl2UtYQG4z4pL6j8WvSiqozWQ47jTX8qKYOSJA8HEWYpXSDI7HZqqU-y2kNIc2OG-a6iGh16gFuYvwiqHtLk2ZUqtGLjTHawSyFhkivMXUHJUiNYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e551facae3.mp4?token=MRk2nAqMLLtBzkb8Qme6RKN2r5iJYg4VZxFK4WB0aMTyFyzVU4a2tRX2kho56AgGrRS00Z7HvicSvf1ANHyrXLebEDpkoma-T9sdPZkP567mZbnaO4hM2m74NUA2b8SSnbvx-Z3OZ50bU8ksdY33C_gkWKdOPv4PtOQ21QAPgFRsstPjYqKZPJLdUxZf530z6DlhaVBTijpRmnZ5vR__PLnlNPgsNbapIV5sYHQl2UtYQG4z4pL6j8WvSiqozWQ47jTX8qKYOSJA8HEWYpXSDI7HZqqU-y2kNIc2OG-a6iGh16gFuYvwiqHtLk2ZUqtGLjTHawSyFhkivMXUHJUiNYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥶
🇪🇸
جدیدترین پدیده آکادمی لاماسیا بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/107839" target="_blank">📅 08:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107838">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107838" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107838" target="_blank">📅 01:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107837">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fk4WVu0W4NC7656oYRRmKNOaVD6Gx_ataHhpmAL8lG3pGsA2xCz6zlnXbR3NP8Au9OwIorVK2_8FnMdcOT_Dz4JuzSgwYIlXULcj1e-w0wDxuRZO9XNdnOVyyuuLQpf65rh0yI5zU-_hI7yYn4HeyWeP8BVFlavSagW5g8Ltd7sy7MXsb-C3ikDkRoHJ8JLaye2KxKcBGRjmb7AWsVmbwHAqgItC6gOQ6AyRvXBl7Vgjm1L_2witnNlqlhnsEw_5y_0eWYkrmZLZmVcCUsxZY_oDDJ3wb3fFaLC3nHhmxbrcNd-k7nCkdVf2uwOmwZ53NlLCtPtU6GyjZ66hDC-NEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107837" target="_blank">📅 01:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107836">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/107836" target="_blank">📅 01:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107835">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hahHgRQmqv2WdRcnzbFd4UDPAcGzB-qq761i19jX9VjbwiXFOo7-SWaqPC0e0zlFXoQkE670wgv3gz71NVwSixrSyYYqG24vDraGrE2k9Ipb-OskdSHBOsEFhV33xbReKzpnlPvLcRhjgt2-Eh_UA88mIOQclCt5IPXyuyuWkVOQbhGTAuuKPKQEw7roFs9Y4xcJNmthzkwCK8svBnsY8ricHQPPiEz_H-5o4QpO0IDcGrPMjXK4_31qtKe9WOc-rdVpFyX4AehDiisnKzu6rBsS219pZTH0PAru97FNVhC2_RzdnQ74QoqiCJdIps60k_Tl2nZAQwfAFQBIsjWUMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
🇵🇹
ژرژ ژسوس سرمربی پرتغال: آنچه بین من و رونالدو رخ داده یک سو تفاهم است که به آسانی حل می‌شود. البته این بستگی به تصمیم خود رونالدو دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107835" target="_blank">📅 00:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107834">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHoKyXtGJQ8_h338tcTS4rFg2NcJV47UydnCuixlPbufzLn48AyKWOl-QO5JChRygHHPG-1d5SBV9wuY-KDo2EVgSU7DzoTrSAuqGz1UqdD-z3J_bz47R0bZs5r5txewvrzxf2EkHA1HXXb_9vAAmtFmnaGbMXlzp3QS7eD2vXTavqta2HPKwpWju_dOPAweq31o2juFmuIzZACEtU80sobRzswwCERIti0C69_BNgwvqQOD3Ax3fcxoIBYK-4DD3MTRpR6d9Xxq-Te2UpfJxFdnn2I-wCLjOo0NfnZqbGNVuVU82U4ZN-enpxJ4QW9RaSPtl20u9GEOIEoOt_Lx2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
تیم‌ملی پرتغال به مرحله ¼نهایی لیگ‌ ملت‌های اروپا صعود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107834" target="_blank">📅 00:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107833">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e30d963cb6.mp4?token=d-Z3ACm3GiJKnSMfGsVgIJWl3kbqPWYp26MvFL-9IZwDcOqwURnu9BtFUHvbwuhXp_ST6j18RoH_8EQitj17UritUAM0EXsC5M5ghOvu3OvrxKk4c2NJ_pm5PszeoKgRg2Oeo8lHl026iJNZPvUlhNhGBgRHua-6oDK1wES5bHC-XF6p_gbVL-_lW2g7kgxCzXxHjJia0F985DgIWoFLxeAIplC1oPVy7KBKWVEYzV8EoYWDRf1-HMStAFQBol1EtMdJhM6m_8lKD2TqbVVP3LnmxzXLzlupg0QnHC4m8H5GtzF-Ebdu07ujEtwcCwgeaxqojNasgK3a0G3QpMi5c5Rad79sz9eL-QwzuXsZpIZ6KnPLczvnweI7JH3Z71M6xXMKOTXfdVedyh4kq04I54TB2S26asTYEl-xuEQgTFePfi54fa8Inoie2O1coGrTma3JrOArtlt38qLzjQg-G0wbStBaIbYcVykVh7YVSBxvvDtVUP52o03h2V_zzSbJ2Ea6DqW_uIWUgwpT45rwlISEo3YYnDvEbRogKulsYKnKLxI_vMirvggqienKEtCt8oE9a5aDwaJvTbCKh7v8LOij3TJixtZ72T6FZRiS8Ciszvgs4pACNmPqv9Pbyaa6w8_dZ6LfDBInM4vNVq0FCFDBKw-6JXdFOGUzMoxvz6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e30d963cb6.mp4?token=d-Z3ACm3GiJKnSMfGsVgIJWl3kbqPWYp26MvFL-9IZwDcOqwURnu9BtFUHvbwuhXp_ST6j18RoH_8EQitj17UritUAM0EXsC5M5ghOvu3OvrxKk4c2NJ_pm5PszeoKgRg2Oeo8lHl026iJNZPvUlhNhGBgRHua-6oDK1wES5bHC-XF6p_gbVL-_lW2g7kgxCzXxHjJia0F985DgIWoFLxeAIplC1oPVy7KBKWVEYzV8EoYWDRf1-HMStAFQBol1EtMdJhM6m_8lKD2TqbVVP3LnmxzXLzlupg0QnHC4m8H5GtzF-Ebdu07ujEtwcCwgeaxqojNasgK3a0G3QpMi5c5Rad79sz9eL-QwzuXsZpIZ6KnPLczvnweI7JH3Z71M6xXMKOTXfdVedyh4kq04I54TB2S26asTYEl-xuEQgTFePfi54fa8Inoie2O1coGrTma3JrOArtlt38qLzjQg-G0wbStBaIbYcVykVh7YVSBxvvDtVUP52o03h2V_zzSbJ2Ea6DqW_uIWUgwpT45rwlISEo3YYnDvEbRogKulsYKnKLxI_vMirvggqienKEtCt8oE9a5aDwaJvTbCKh7v8LOij3TJixtZ72T6FZRiS8Ciszvgs4pACNmPqv9Pbyaa6w8_dZ6LfDBInM4vNVq0FCFDBKw-6JXdFOGUzMoxvz6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
گل‌دوم پرتغال به نروژ توسط گونزالو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107833" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107832">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e974e0edb0.mp4?token=AvPQeS7x2lANVTwFe6DmbyRLuCFf5rVDXuo1R4WOuy7zRgLyd5DZi82ZvsobA0cP1ohb1iKT8_0dU50hiRjadJPl0LTiiUs6eNYo2LDD6dC2Gwd7_1yZboxm-RXLU8gEvZKynJFHZnNCXKXtS3dP1gKVizCLjGT5aTI8vowpXdjqLlJ1tX7y2YmJQ73g_k9T_0ARfIBgaZXGgpxXbVsuFTHMDUiowX0GxHz6fJctExoEhMF-xjwiZ-FRvlJY-bFG8dR0XedhkdnSpeaqEBbxCjEXhpUmJsIQFRkHG_x5s1ydjQtVAP9tKvFYAnUZJFGBsUwMwGgend5kwlVjUSh_9Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e974e0edb0.mp4?token=AvPQeS7x2lANVTwFe6DmbyRLuCFf5rVDXuo1R4WOuy7zRgLyd5DZi82ZvsobA0cP1ohb1iKT8_0dU50hiRjadJPl0LTiiUs6eNYo2LDD6dC2Gwd7_1yZboxm-RXLU8gEvZKynJFHZnNCXKXtS3dP1gKVizCLjGT5aTI8vowpXdjqLlJ1tX7y2YmJQ73g_k9T_0ARfIBgaZXGgpxXbVsuFTHMDUiowX0GxHz6fJctExoEhMF-xjwiZ-FRvlJY-bFG8dR0XedhkdnSpeaqEBbxCjEXhpUmJsIQFRkHG_x5s1ydjQtVAP9tKvFYAnUZJFGBsUwMwGgend5kwlVjUSh_9Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل‌تساوی پرتغال به نروژ توسط ژائو کانسلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107832" target="_blank">📅 23:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107831">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2872cf61d0.mp4?token=Fbro9jKEpLi5HVL4MI0m1BNgWbEBtoCNM0Gu1aSLTdWQ2XfIgVIahsZoumyUdxtxGCiHa2ljUxZGvYS_mOG_e1WcONBGqhXpUfIg79jyQuEn8AMDoWBUbHbMLJcpw4RcKNXC0AA4eyNgwj_-T9sXOg205aCfIAc_NZtbdaaDLKG5s6xb0Aiua65p29fRSYOMBohEf7Rpi4tfeE8ElDHngKO788BxeSSCefGwXWoDbwGF0NLIENtU39vGVz7fmYkMTC9Ktmyf3PPuJ2ltkOWhz0gSjDmVbHFVjGH8933XR8Fq_OLxXJp4uTQXWP_8AiPFgbMP-HiARzYmHM4-uvbASSIp9vBviu3KtgfN7nGyhV6gNRCWsJZaoOprSJQVTGtu2FfNjqMZaVloVB-Pn23NwwOpdXWUrxkFbGW5leDMJX4Q9j5RhqelTzV_YbN_kX0Ge5n-x8Na6xnVMhepIUm-YxZteJn_6kfNfYS3XijR7fR781SgDBcszbtpD13QMc2ItSySSD9ULTnYCU-AA_n4X2Urlx-cah8AhhoG4jTbQBlQUl-bs90v8fVtezwoUN-db3-l5dFdR9gtk7W7KDVdE0T-lYK8ycsFtpS1VRC2kzYRSsuwHuSe_AnMJItNcQi-J0ihyF0ZxH0qWqh8q_bkHy0_fKaF9hu-Op-d25i7UN0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2872cf61d0.mp4?token=Fbro9jKEpLi5HVL4MI0m1BNgWbEBtoCNM0Gu1aSLTdWQ2XfIgVIahsZoumyUdxtxGCiHa2ljUxZGvYS_mOG_e1WcONBGqhXpUfIg79jyQuEn8AMDoWBUbHbMLJcpw4RcKNXC0AA4eyNgwj_-T9sXOg205aCfIAc_NZtbdaaDLKG5s6xb0Aiua65p29fRSYOMBohEf7Rpi4tfeE8ElDHngKO788BxeSSCefGwXWoDbwGF0NLIENtU39vGVz7fmYkMTC9Ktmyf3PPuJ2ltkOWhz0gSjDmVbHFVjGH8933XR8Fq_OLxXJp4uTQXWP_8AiPFgbMP-HiARzYmHM4-uvbASSIp9vBviu3KtgfN7nGyhV6gNRCWsJZaoOprSJQVTGtu2FfNjqMZaVloVB-Pn23NwwOpdXWUrxkFbGW5leDMJX4Q9j5RhqelTzV_YbN_kX0Ge5n-x8Na6xnVMhepIUm-YxZteJn_6kfNfYS3XijR7fR781SgDBcszbtpD13QMc2ItSySSD9ULTnYCU-AA_n4X2Urlx-cah8AhhoG4jTbQBlQUl-bs90v8fVtezwoUN-db3-l5dFdR9gtk7W7KDVdE0T-lYK8ycsFtpS1VRC2kzYRSsuwHuSe_AnMJItNcQi-J0ihyF0ZxH0qWqh8q_bkHy0_fKaF9hu-Op-d25i7UN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل‌اول نروژ به پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107831" target="_blank">📅 23:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107830">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d1f2465c.mp4?token=qpBa4Y21U-s3wdKPhRisc56v2oKSxQD-KSyDnXjPbFGt3CAresZZPMR3s5pufeYAMuW4dN2wGUKMYIjqR0Rv4JPn0x_DwYydDyzEufXmhlSQf6hQuRPsYrWED7Ih-2KPvsu6Ba_VbOfuB4rutoUxPhXftjgH55UMRJ7U60qpYwQJNmG8maMLnZaYzdEGAUkaPF8qPdssE8okksBEsgzyBqt7KDaj6MIETEsnNK_lDhpdXxleYIAQ1imdmtzF-I3iV5k_yNAfMLIik95tzQbfb_ENFMa-uubqq8d0CtFEbaKEr46FRvuccC9LzWDI1PYWJaJAvt_Y_eTRqCDW3lGn_g2uO-Q4zv6I7Oug5lLfcvBSIqRGoOqYfRwZfLb5R6quXxCL7R3KuyYFZWcE7HRKroTiikXM9g7oEcZySVZu5LlcwqZIk5_9EevyVWOc9ihf9KjZqAgfehd4lqQ1r8BJ_MSj7wunLL6ZT7Sf1vslKBujhWQxl6Jy6t_EVYRVP9KUctzp3PFRyS412JRB9uWIPN-cccrOLAgLULnmzuIDhWH0A2Q3zxaMaBQvLVLC_NZquLXMqifCj0q1Zsx4G29AVGupQX7wSeXRSUwfokj--aCF1Qs_7GHycWJcL1O7uNp2WmEBkxyjxxI9cyh-T9DRWAbltzKyC41FZD_CPIzjKQc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d1f2465c.mp4?token=qpBa4Y21U-s3wdKPhRisc56v2oKSxQD-KSyDnXjPbFGt3CAresZZPMR3s5pufeYAMuW4dN2wGUKMYIjqR0Rv4JPn0x_DwYydDyzEufXmhlSQf6hQuRPsYrWED7Ih-2KPvsu6Ba_VbOfuB4rutoUxPhXftjgH55UMRJ7U60qpYwQJNmG8maMLnZaYzdEGAUkaPF8qPdssE8okksBEsgzyBqt7KDaj6MIETEsnNK_lDhpdXxleYIAQ1imdmtzF-I3iV5k_yNAfMLIik95tzQbfb_ENFMa-uubqq8d0CtFEbaKEr46FRvuccC9LzWDI1PYWJaJAvt_Y_eTRqCDW3lGn_g2uO-Q4zv6I7Oug5lLfcvBSIqRGoOqYfRwZfLb5R6quXxCL7R3KuyYFZWcE7HRKroTiikXM9g7oEcZySVZu5LlcwqZIk5_9EevyVWOc9ihf9KjZqAgfehd4lqQ1r8BJ_MSj7wunLL6ZT7Sf1vslKBujhWQxl6Jy6t_EVYRVP9KUctzp3PFRyS412JRB9uWIPN-cccrOLAgLULnmzuIDhWH0A2Q3zxaMaBQvLVLC_NZquLXMqifCj0q1Zsx4G29AVGupQX7wSeXRSUwfokj--aCF1Qs_7GHycWJcL1O7uNp2WmEBkxyjxxI9cyh-T9DRWAbltzKyC41FZD_CPIzjKQc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
در مورد شکایت از یاسر آسانی؛
🎙
حدادی: چیزی که عوض داره گله نداره!
🟢
نامه فیفا به استقلال را خواستار شدیم
🟢
مدارکی داریم که بقیه باشگاه‌ها ندارند
🟢
آن سال هم هواداران استقلال قهرمانی آسیا را از ما گرفتند
🟢
رفتن کامنت گذاشتند عیسی محروم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107830" target="_blank">📅 21:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107829">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2aee117f1.mp4?token=c5fjFjP16G6sNepNt59DqF7aytMExnavIYGppwPVL8yWYVXDiZwcUQMMFTCAaKFRtegbP7Nt9d98uvPYzv-Qk_AhC4vv3iVbpVGKLScMJdWgZnn61f7U2EGGPSwNrwqcIjRSHxhOc3Rls_HjZnK8a5W9hWmQ_Lfz0_X_gefOUNS-EM6p0xgBXA02Cxqrrc20pcIfesnptgtInunh0vUgJ3W6hw-KW3BsOkmbU5jHrO3WsL5ao-ORXV8ELMdK3YhUyWwHrD3-BQ2vVetfbZp0wEwjy48URahyQeI-YIVrwIIStWpYwGRBhfpVJdRT_wTbLbfMo5CQ4Am-gf-CRFQo-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2aee117f1.mp4?token=c5fjFjP16G6sNepNt59DqF7aytMExnavIYGppwPVL8yWYVXDiZwcUQMMFTCAaKFRtegbP7Nt9d98uvPYzv-Qk_AhC4vv3iVbpVGKLScMJdWgZnn61f7U2EGGPSwNrwqcIjRSHxhOc3Rls_HjZnK8a5W9hWmQ_Lfz0_X_gefOUNS-EM6p0xgBXA02Cxqrrc20pcIfesnptgtInunh0vUgJ3W6hw-KW3BsOkmbU5jHrO3WsL5ao-ORXV8ELMdK3YhUyWwHrD3-BQ2vVetfbZp0wEwjy48URahyQeI-YIVrwIIStWpYwGRBhfpVJdRT_wTbLbfMo5CQ4Am-gf-CRFQo-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👍
🎙
تمجید و حمایت زیدان از رونالدو:
"فکر می‌کنم اتفاقاً باید از کارنامه فوق‌العاده‌اش و کارای استثنایی که انجام داده تقدیر کنیم. اون باعث شد ما جام‌های بی‌نظیری رو ببریم، پس به احترامش کلاهم رو برمی‌دارم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107829" target="_blank">📅 21:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107828">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af8a71f26.mp4?token=hOizXC4xeq6CBlDJWRG7KJ0hRHlRHzEMJpS1CziTSVIdJ71mvvHYupPOKaUJdehylGNLh6ekzlmGFIbjt9JLr-m85b1hkw5Y0A5RjrxAP4xdD9tWShls6tlXJt7CAASqLtvkXjWOvu1GN0h3vtBHpxXdAULOvVhLrdkDAlF3B4iqxLr7loO6FJCxkMv6r7CbRWuz-AOlYiZ5JqXNRJZ0vhtdCxnopZLH-9OHdd1PFqnY-2OOhby55_3cZ2hGdRH_c-OMRwfjEkkNNeLVzGwSkDYcyHKZmXi8Zl9OzqITSmGJN3dpT4q-hs--A5BtaPj6FhlhFIxjSN7CbMoBhawfTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af8a71f26.mp4?token=hOizXC4xeq6CBlDJWRG7KJ0hRHlRHzEMJpS1CziTSVIdJ71mvvHYupPOKaUJdehylGNLh6ekzlmGFIbjt9JLr-m85b1hkw5Y0A5RjrxAP4xdD9tWShls6tlXJt7CAASqLtvkXjWOvu1GN0h3vtBHpxXdAULOvVhLrdkDAlF3B4iqxLr7loO6FJCxkMv6r7CbRWuz-AOlYiZ5JqXNRJZ0vhtdCxnopZLH-9OHdd1PFqnY-2OOhby55_3cZ2hGdRH_c-OMRwfjEkkNNeLVzGwSkDYcyHKZmXi8Zl9OzqITSmGJN3dpT4q-hs--A5BtaPj6FhlhFIxjSN7CbMoBhawfTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
پاسخ علی چینی پیشکسوت استقلال به مالک تراکتور: ما از منیریه جام بخریم؟ بیا تهران از نزدیک جام‌ها را لمس کن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107828" target="_blank">📅 21:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107827">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56554104cf.mp4?token=j2Nb-is624Tml-6i-MQmTMxPZTCMyQTy8Yd3PWb3SS4Yg4By1ak4O1rbFlPzZNC3IlJ7fbyn9LgmZJFDhdb13MTgRyeBfvKn-wlTkcSXb1FRAdnbdiJDX3L6yskrQt9AqbdvCBTJSrQzh9wt0To1z2ZjigP0EUsHRGVwpci1LBkCf3PqM8VN2Fhtox_VbfRVOhkG2tGkg67_w4jQgAyqMsjcDCTYhCRaeQx-OMYa7KiQDR-DzHAVwFFZI-GbVgXNFU5inJozFUGJtmeAMEM8x-Dzyk5Or4ni0-lcqF4DCn71eAlMlMoVLoNqXOLlHIGkzOvqYkoGL8niFTRoO86rznydVgKEH5Yd3zM2TU-T39upVu9fXWrd2Z6wZ-OdGuH5mo2P8NYscK8UVsPVPT34CFOx9TPrmgHeKdi6g82iqKL6kjFCoMqWO-SiWzRIPHsqHSfb_TT9xA6_2kpevRS0CZjtar0AbmlXyt-TMMV0XbG5PWozjW1i1gjAGF5zmxKPKcxtPSypttx5kRVkgAD2ozCyV3TmJmCYCSmnt-o6XUa4M-p4M5HD8beOocJ081BjaTJyozEx5wZ-pvV2P4BW1fbDmEBwVTMauOk7qkYjYjW-RQiNNi8fsXx5R9AV0P3-ONyF5tNFEJLHaQArdGhca2sr14UvPVK6cwmWuVIFu_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56554104cf.mp4?token=j2Nb-is624Tml-6i-MQmTMxPZTCMyQTy8Yd3PWb3SS4Yg4By1ak4O1rbFlPzZNC3IlJ7fbyn9LgmZJFDhdb13MTgRyeBfvKn-wlTkcSXb1FRAdnbdiJDX3L6yskrQt9AqbdvCBTJSrQzh9wt0To1z2ZjigP0EUsHRGVwpci1LBkCf3PqM8VN2Fhtox_VbfRVOhkG2tGkg67_w4jQgAyqMsjcDCTYhCRaeQx-OMYa7KiQDR-DzHAVwFFZI-GbVgXNFU5inJozFUGJtmeAMEM8x-Dzyk5Or4ni0-lcqF4DCn71eAlMlMoVLoNqXOLlHIGkzOvqYkoGL8niFTRoO86rznydVgKEH5Yd3zM2TU-T39upVu9fXWrd2Z6wZ-OdGuH5mo2P8NYscK8UVsPVPT34CFOx9TPrmgHeKdi6g82iqKL6kjFCoMqWO-SiWzRIPHsqHSfb_TT9xA6_2kpevRS0CZjtar0AbmlXyt-TMMV0XbG5PWozjW1i1gjAGF5zmxKPKcxtPSypttx5kRVkgAD2ozCyV3TmJmCYCSmnt-o6XUa4M-p4M5HD8beOocJ081BjaTJyozEx5wZ-pvV2P4BW1fbDmEBwVTMauOk7qkYjYjW-RQiNNi8fsXx5R9AV0P3-ONyF5tNFEJLHaQArdGhca2sr14UvPVK6cwmWuVIFu_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
پیمان حدادی مدیرعامل پرسپولیس: ما زور داشتیم و تورنمنت سه‌جانبه برگزار کردیم. اینکه قهرمان فصل‌گذشته معرفی نشد کاملا منطقی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107827" target="_blank">📅 20:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107826">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
۸۱ سال گذشت؛ کلیپ ویژه سالروز تاسیس باشگاه استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107826" target="_blank">📅 20:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107825">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_YhsFB5hSWR_uKKWIZDsbnKnGE6cZUVigEo6OH-pkWyTl8-nYgfi22NabL-XW612TvYCssT-2a6TMWhIq7hGxTmsg1LBOOeAfKxPcRCwQ3cV9xZqAqcujQQzeGOfvngSblwaVIZgZmebRc1Zu21MQypN2l2qmc-IDJJM_-utggYbgUD6JeIrwJWns9DD24OhW0bwbalPFZ-ppFYKczDAiCsahn1hI6-gH9pTg6wEGnSgDRfwXYTrnd3u386RKS77NVjZ8PorN_DiafZr_kSrA618zilHzjGtbhXGg7T1sXme9DLC5FFYJgmXngkBNWW0uHD7Tp6dyKlHA3o8W5e4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
‼️
پیمان‌حدادی: قرارداد اورونوف را تمدید کرده بودیم که بتوانیم بعد از درخشش احتمالی این بازیکن در جام‌جهانی این بازیکن را بفروشیم ولی برنامه‌ریزی موفقی نداشتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107825" target="_blank">📅 20:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107824">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
حمید مریخ مدیر برنامه یاسر آسانی و نزدیک به باشگاه استقلال قصد داره که شیرزاد آسانوف هافبک میانی 23 ساله تیم ملی ازبکستان رونیم‌فصل به تیم استقلال بیاره و منتظر تاییدیه بختیاری زاده‌ست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107824" target="_blank">📅 20:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107823">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50712b5d4b.mp4?token=gjwi6Xf7k_MreJ_-DDKbKHLuF_D1NmwDrVFNbUqHSivFbXWtQ5rSe9u8t8uMcTfZRDllrGRT7i7BVhUTSar7ZyMnVcAVYN3igftT6O1SSP-vZNz5AssYJCHuo8ySPBzbvtbCGvAVYCvXWYHe1kH7UQIXzdD2e6jTlXB5FmYtXaYn5YDDadXQGIyC8KU27gVuGjU_bSDq0UlamXvWUROskBxwVVTmKpTJZhMblhCAXCsm_Q-gzOV_0S4luk7k6AdKHPQf4dwaXlkBUsv4lzK1eQ7Wk84mfYF7-Pf9dAIUkbdBEqLhhc_cSx_FISnXHzwU5dPbLjOehF8RYv9Hp82yeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50712b5d4b.mp4?token=gjwi6Xf7k_MreJ_-DDKbKHLuF_D1NmwDrVFNbUqHSivFbXWtQ5rSe9u8t8uMcTfZRDllrGRT7i7BVhUTSar7ZyMnVcAVYN3igftT6O1SSP-vZNz5AssYJCHuo8ySPBzbvtbCGvAVYCvXWYHe1kH7UQIXzdD2e6jTlXB5FmYtXaYn5YDDadXQGIyC8KU27gVuGjU_bSDq0UlamXvWUROskBxwVVTmKpTJZhMblhCAXCsm_Q-gzOV_0S4luk7k6AdKHPQf4dwaXlkBUsv4lzK1eQ7Wk84mfYF7-Pf9dAIUkbdBEqLhhc_cSx_FISnXHzwU5dPbLjOehF8RYv9Hp82yeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پیمان
حدادی مدیرعامل پرسپولیس: قرارداد 5 بازیکن خارجی ما 4 میلیون و 80 هزار دلار است
🔴
در نیم فصل و تابستان بعدی بازیکن خارجی نخواهیم گرفت. ابتدای فصل بخاطر همین کادر ایرانی گرفتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107823" target="_blank">📅 20:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107822">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65b6b0e4ee.mp4?token=JP5IHFdy_wN5YZQRSHsGeBWixbyVydKKqb0PeWkryTvychjXuwjoB0b12IDdLvJ6nNQhplsQKUhgNU9dzCVzBY40lpEnq3lhBMDRZKEXIWTUsaBqilHWdUyH1_1TpNevSUizq2x4USs4m3_DtqP4rxXCtBdMJbr4oCGNNiGNGT9lR1tIudfzXMRG4vinVBGCumllJQZXYEfdo3CbtB9Q4wniv1dWOIdc8kKPDHnzsqk1jDkVgS3F2SjTzV8WNxcOHVo7707ResKHVh6z_tzVKBdXeCUpCPS2FR0piv2YlS0QC3xSTF5jviF4YvFlU-Uqb5C5VsAleNZM4EBRCHk3iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65b6b0e4ee.mp4?token=JP5IHFdy_wN5YZQRSHsGeBWixbyVydKKqb0PeWkryTvychjXuwjoB0b12IDdLvJ6nNQhplsQKUhgNU9dzCVzBY40lpEnq3lhBMDRZKEXIWTUsaBqilHWdUyH1_1TpNevSUizq2x4USs4m3_DtqP4rxXCtBdMJbr4oCGNNiGNGT9lR1tIudfzXMRG4vinVBGCumllJQZXYEfdo3CbtB9Q4wniv1dWOIdc8kKPDHnzsqk1jDkVgS3F2SjTzV8WNxcOHVo7707ResKHVh6z_tzVKBdXeCUpCPS2FR0piv2YlS0QC3xSTF5jviF4YvFlU-Uqb5C5VsAleNZM4EBRCHk3iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
‏همسر
بیژن مرتضوی: تو مجازی به آقا بیژن فحش میدید ولی تو واقعیت دنبال عکس و امضا هستید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107822" target="_blank">📅 20:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107821">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe589a60ed.mp4?token=VSAFn_Foi4zydxPRyFtdp3eZkJ90Fwdi2JtpdgPIWKdkJhK5FphNAz6OHFMxWfhX9mXcYmObNqOsDNQRPBCm_4cegoh8RbTRmaDp5zQ0mQsIAWotHUOfxbx6l5ZGORO2cAVdccbL8QGGGrW4eKVn4FGOW93l5wQ5JkeFDgvzn33WYPMZV18PpeYEo6Cz4sQEOvIISMcsk_REEtiH5c-05XZFZ2gwKCb81cKdPHev2wDogI1oAhk4NqNxMnazlbIVcDXxj797lLxmimigfYe8cguewx0Y3IGB_5C6fKskGt-zSTjujjIOSdUoHtljRVuw4dBSwDNPZorNiHyjMh0otQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe589a60ed.mp4?token=VSAFn_Foi4zydxPRyFtdp3eZkJ90Fwdi2JtpdgPIWKdkJhK5FphNAz6OHFMxWfhX9mXcYmObNqOsDNQRPBCm_4cegoh8RbTRmaDp5zQ0mQsIAWotHUOfxbx6l5ZGORO2cAVdccbL8QGGGrW4eKVn4FGOW93l5wQ5JkeFDgvzn33WYPMZV18PpeYEo6Cz4sQEOvIISMcsk_REEtiH5c-05XZFZ2gwKCb81cKdPHev2wDogI1oAhk4NqNxMnazlbIVcDXxj797lLxmimigfYe8cguewx0Y3IGB_5C6fKskGt-zSTjujjIOSdUoHtljRVuw4dBSwDNPZorNiHyjMh0otQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
اقدام تلافی‌جویانه امید عالیشاه برابر خداداد
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107821" target="_blank">📅 19:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107820">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6340210c7d.mp4?token=gdob-c-dtRO-tAoT21jTK900WIS9kQYVr57X2Kyi_q-BfsgJQqY8QOLP67rDFnczXof7KymNjQcPlifiAmMHCOJG18YUdmtiAJzIpF-IAwovu1iAApvVtAUP7WbEnHA4GteORtRVWt3Og9bmomz-qU76VJzDYnBtgGhCPr2yxaIt5vtZtt3Jd3JoNub53ZO7y-J7e7RvW2-Z8dcz-ccPck6WQiJ3Tj42IpNQY0BwEmF7SntvA0DoFs2FyZvWPOVBVISO7saEChPOPD_gxNb-auYSvWG76PJbY6V_suHsST5MIjpQLX_c21lR2xT1UR95V2ugDAf5fFH4XUCu2zDU7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6340210c7d.mp4?token=gdob-c-dtRO-tAoT21jTK900WIS9kQYVr57X2Kyi_q-BfsgJQqY8QOLP67rDFnczXof7KymNjQcPlifiAmMHCOJG18YUdmtiAJzIpF-IAwovu1iAApvVtAUP7WbEnHA4GteORtRVWt3Og9bmomz-qU76VJzDYnBtgGhCPr2yxaIt5vtZtt3Jd3JoNub53ZO7y-J7e7RvW2-Z8dcz-ccPck6WQiJ3Tj42IpNQY0BwEmF7SntvA0DoFs2FyZvWPOVBVISO7saEChPOPD_gxNb-auYSvWG76PJbY6V_suHsST5MIjpQLX_c21lR2xT1UR95V2ugDAf5fFH4XUCu2zDU7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
مهدی مهدوی‌کیا در واکنش به اتفاقی که برای کریستیانو رونالدو در تیم ملی پرتغال افتاد گفت:
🔹
«وقتی این خبر رو خوندم واقعاً ناراحت شدم؛ یک ابرستاره مثل رونالدو شایسته چنین رفتاری نیست. کسی که سال‌ها برای تیم ملی پرتغال همه‌چیزش رو گذاشت و یکی از مهم‌ترین چهره‌های تاریخ این تیم بود، حالا به جایی رسیده که اردو رو ترک می‌کنه. به نظرم باید احترام بیشتری برای بازیکنی با این سابقه و جایگاه قائل بود.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107820" target="_blank">📅 19:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107819">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae14913e57.mp4?token=EXUDrF75gWTTqP_6H-uja-oFrq96dmhtcupf5NjpKVVr7fJELGNVd_eFX95SBFwYUOiTluNuMz46gPTfs0lGtn3w-iwRkdcGxMUd3l-KaxDGu27xo5Z44QSl-2v8bxwjP81gYliItrFtK1RmzfviowHDtmptFAXpcsaXspEzuVC3Dgb0_TArlgcpobNpxOhiDbDQXVvYuhbiEzFENWlmU_AIe7Z8Cg-rfuO5Ru1ek5CjL5lKXLHohX-PQnmfAfaA99oOLM45u4QLUTFOAylOdufb3FfQC4CStjty1m3sahFUzl-mB4KZ_vby89wsIEkU_wBKanzW_P082h1LcN8kVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae14913e57.mp4?token=EXUDrF75gWTTqP_6H-uja-oFrq96dmhtcupf5NjpKVVr7fJELGNVd_eFX95SBFwYUOiTluNuMz46gPTfs0lGtn3w-iwRkdcGxMUd3l-KaxDGu27xo5Z44QSl-2v8bxwjP81gYliItrFtK1RmzfviowHDtmptFAXpcsaXspEzuVC3Dgb0_TArlgcpobNpxOhiDbDQXVvYuhbiEzFENWlmU_AIe7Z8Cg-rfuO5Ru1ek5CjL5lKXLHohX-PQnmfAfaA99oOLM45u4QLUTFOAylOdufb3FfQC4CStjty1m3sahFUzl-mB4KZ_vby89wsIEkU_wBKanzW_P082h1LcN8kVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
💙
فتاحی رئیس سازمان فوتبال باشگاه استقلال: نمی دانم پرسپولیسی‌ها علیه یاسر آسانی چه مستندانی دارند/ وقتی باشگاه السد قطر با آن تیم حقوقی قوی که دارد از باشگاه استقلال شکایت نمی کند یعنی حضور یاسر آسانی هیچ مشکلی نداشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107819" target="_blank">📅 19:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107818">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70613f964d.mp4?token=QsiUmW2w-lzq7IdI4SvXr-WG0Afpbvk0K0fADvQy6ozYY4xrJYMJ2S5LIODiIEVHp_Z8tmt_ONSkQBZ813Ii2iNqSzxgi67LSMHRCJ3erknknAANR1jsO36tfjDF9y7VjWhEJE2hRAaJclEUrlGk486ya5WlFBU4gFYA3lZUXbUWJbs-V1vUwQnmE_AQmfu0-H7EoqpLMz6U-MgbVImw6B4RtStzEnaKI1Vjdjer4vMGqxWpyzF2lT3xu1sK7O674HgtF-rBnIyAc92PRQcJ2-OiOJWQ59y8Aab335XfeMYxlUvuzckP_-KUub7jGRg1nJgtPLeurSqph6xNSp7ITTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70613f964d.mp4?token=QsiUmW2w-lzq7IdI4SvXr-WG0Afpbvk0K0fADvQy6ozYY4xrJYMJ2S5LIODiIEVHp_Z8tmt_ONSkQBZ813Ii2iNqSzxgi67LSMHRCJ3erknknAANR1jsO36tfjDF9y7VjWhEJE2hRAaJclEUrlGk486ya5WlFBU4gFYA3lZUXbUWJbs-V1vUwQnmE_AQmfu0-H7EoqpLMz6U-MgbVImw6B4RtStzEnaKI1Vjdjer4vMGqxWpyzF2lT3xu1sK7O674HgtF-rBnIyAc92PRQcJ2-OiOJWQ59y8Aab335XfeMYxlUvuzckP_-KUub7jGRg1nJgtPLeurSqph6xNSp7ITTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های امیرحسین صادقی بازیکن اسبق استقلال و تیم‌ملی درباره وضعیت وخیم اقتصادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107818" target="_blank">📅 18:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107817">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf836fb3bd.mp4?token=tXboIadOZBcKdv8E3Cb_UtTLMruNzxS3Q1HGyWTrbZ6rlU7xwfabNfSwoWT0iCGYjh9TuvQ5uSC-ersOkjEYEKg1DjrPgbrgVia0wqas85ioazW8e4lVo2llvc1OpCH25RV7WWAWhdxuckGsTlbay92HWK0SRYW3ZmUCKOAwNcsN70dVr92-C-j31XHdd-0PbAiAon8ve6ktd2oySoqEiO1myNYqHxNCoYkyvKuVsw0D_z_F8G1fTij90Nq8vHRl72Ref3MrrahstusKPiNxwkGiwoFBVEFFX24tHqrPwsFyOLm5WJQGl1vCdrj2uY6lLlO-uK8YqN09uXqnNsQnEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf836fb3bd.mp4?token=tXboIadOZBcKdv8E3Cb_UtTLMruNzxS3Q1HGyWTrbZ6rlU7xwfabNfSwoWT0iCGYjh9TuvQ5uSC-ersOkjEYEKg1DjrPgbrgVia0wqas85ioazW8e4lVo2llvc1OpCH25RV7WWAWhdxuckGsTlbay92HWK0SRYW3ZmUCKOAwNcsN70dVr92-C-j31XHdd-0PbAiAon8ve6ktd2oySoqEiO1myNYqHxNCoYkyvKuVsw0D_z_F8G1fTij90Nq8vHRl72Ref3MrrahstusKPiNxwkGiwoFBVEFFX24tHqrPwsFyOLm5WJQGl1vCdrj2uY6lLlO-uK8YqN09uXqnNsQnEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
فریادهای عجیب یه نماینده مجلس جلو قالیباف به همتی رئیس بانک‌مرکزی: به والله میرم خودمو جلو بانک مرکزی آتیش میزنم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107817" target="_blank">📅 18:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107816">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esKZieHQyh9Q3TjnrIceZfEbNjw-_6dayAiuzW4I-8cLf_r6SN3p_y7Yq_M1Sulz65MVVo0r2WCUHtkyY8K7vO9zPBHNdBcfQy2pfjaehVu6AciWI5l2QX4Y2RNb0j6MPulxfsFfr1UOFJXW5xzvKyg08wXmac3xfS3D7AluNQ2UZEzNapxr0WH4fPyOHqR4wlUNABvEbGsCUHHbFzwkPGeTuqbNyyWpdXdBYZCqJ151uOfdB_k2w1ycy1whYpCd5MfU0rezNsgNN2326Nf15lsYpGHIDiYaf6e3fLV1cIH154pZgRo5YUrmVLeSJF45MI0e0Uarnm3PW5PPUFx7Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
فدراسیون فوتبال پرتغال قصد داره برای فیفادی بعدی یک بازی ویژه خداحافظی با اسطوره کریس‌رونالدو مشابه اقدام آرژانتین برای لیونل‌مسی تدارک ببینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107816" target="_blank">📅 18:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107815">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0576436f6.mp4?token=elqySRzAFlIiwobQXfd1anjqCrMreO_u_FGNsHJCeIzXuY2ONg-fOcVviOK07NYZIwW8ZqWbKvi24anWOvG9zNOa5NjuQFTJM1aUtnvBSutrBbC7Dy-_P1i3qdFxVaT60zebf8YPfHaVAJdoSgDKDGrfI6qFXGBqGjWPFq9stev-K5n_OMFaePkwFh7CPUAQBvSC-Sq92JTEp8fpEOc8SJ5UL-PikE68gEygEMmsjAzLGLbL4OWVW6heBA-KKHhppEsOu6rRckjbkYSMpRloExnS4_be51wqXOj15-P96F6K72TjOYTMteyXovnMvjyeglC2UskC_y0cNr1-XItFIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0576436f6.mp4?token=elqySRzAFlIiwobQXfd1anjqCrMreO_u_FGNsHJCeIzXuY2ONg-fOcVviOK07NYZIwW8ZqWbKvi24anWOvG9zNOa5NjuQFTJM1aUtnvBSutrBbC7Dy-_P1i3qdFxVaT60zebf8YPfHaVAJdoSgDKDGrfI6qFXGBqGjWPFq9stev-K5n_OMFaePkwFh7CPUAQBvSC-Sq92JTEp8fpEOc8SJ5UL-PikE68gEygEMmsjAzLGLbL4OWVW6heBA-KKHhppEsOu6rRckjbkYSMpRloExnS4_be51wqXOj15-P96F6K72TjOYTMteyXovnMvjyeglC2UskC_y0cNr1-XItFIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚽️
مهدی مهدوی‌کیا اسطوره فوتبال ایران در حمایت از مهدی قایدی گفت:
🔹
هر بازیکنی حق داره بگه بهترین مربی‌ای که باهاش کار کرده چه کسی بوده. اینکه به خاطر چنین مسئله‌ای یک بازیکن رو به تیم ملی دعوت نکنیم، واقعاً نمی‌دونم چی بگم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107815" target="_blank">📅 17:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107814">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107814" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107814" target="_blank">📅 17:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107813">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tv9hWShUZRN2mD74qiHSNA8xzTewOjjRDlJgK2NXtk111CmS46vItCPYlZRS063umOL7IJ_s7z0AJm12BH01CoNCOjKZGA6et3AYU6MopkQ1j8QcSKSTRSh8__XidM9KU1frIhwufvg0vsvxCVAdOCpHjtA0UrVZ2IRdQnRTAiHfQ0S_g40-9qHhh5WK0bBpdA8k_xd5cbv6hUYcjfX5GOw_OL1sQuQJZLdxF7cURutuXI2mjE-OCT3MPYO5anSDVPE_i1peyUw5ZyUUh2RJ28hUNNjFW6_Dmz0OkX2nY0u6dOQChEBoZDBUQ7UHMZcA51LWYG6bR-J-LPkTQiOGvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز نروژ
🆚
پرتغال را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
نروژ: ۲ برد، ۳ شکست و ۸ گل زده
پرتغال: ۴ برد، ۱ شکست و ۹ گل زده
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107813" target="_blank">📅 17:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107812">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_hMnZgumTRBQe5LXm14boVTu63HcWFxAxjnsDDNkgRJ0iGoqu_PFtEvbKb-4ObWwfgqgAksSdLQV2F4nSLjBUwEtq35xcRofOtz41KSn_NcgeyZ0otG5rPvO0EPbFySaYlBWtw6M6FdA07gV35HKbl2e-YcKaFfDsy365LIedXrrzJjXhYVQfIo49ui3SYUfzOAkA1T2G_5sgJAuuIXk8La_XWiJ_SvYGZFPJTvUu5VSMlSEJpYTl9cjQ3tKO_vLA_bPghOy37Nqwmo3ZDRH5aWE4p1vVvnwexXJnkWvP2dvdE1g6iha_Rg4ipjV6pU3D5gJhKNZSKEMEVhhBGj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
⚽️
براساس گزارش منابع خبری، یحیی گل‌محمدی سرمربی فعلی دهوک عراق قرارداد خود را با این تیم فسخ کرده و در آستانه حضور روی نيمکت تیم‌ملی امید قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107812" target="_blank">📅 17:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107811">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqIKijK_tYNv8MLewq68fS0PBN6yVnWvveUEZYUzgNbmdxTp2fIqUgfVZ4C8cU4WVRKTc-XKz1hCf74eUBc6nmQ3_1MaSd9HQqTdJYOrKlTEwV7X19wV8QSXq4oC3Oi3_hZf1JlIThAyIRJAdojT6LInQXOkfQF44sLgZKFmPcfWbNC_KFX39vLUdjzsv981ihIcxOQPysb66r_3iEKd9vvMEQbe7wfW7POS0T75ve7E82oscp2jCZaHxgGqYrHEn6j14ywOJb9fckft0wmwagU2wRVERUSt8e0n9c1b6gds5eCIQSJYFy4S0SItMhLxAv_W-_sb50u3Es0eQzvQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
مارکا: اندریک از نیمکت‌نشینی‌های مداوم توسط مورینیو ناراحته و میخواد ژانویه مجددا به صورت قرضی از رئال‌مادرید جدا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107811" target="_blank">📅 17:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107810">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
⚽️
لحظات تلخ احسان حاج‌صفی در تیم ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107810" target="_blank">📅 17:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107809">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0177fa0248.mp4?token=p3fi-2b57W1Mfl-CREkqv8D9OQWuW2RMQcu3qTMTNTw-GWrxIcVlFijmF3TQeNXckhxuCPwju_wBnBxuAQQp6tmMD_ak1NpLMefWNj7ry_jAHUOgJlT78EDyZIBCkttdqQSLxPfWzeXzgo5TMZ8oagvp0jZ2rC9kveZq_uiY62taREgdnS_g7bBBILAsJykLQ6bmsrOehGYPUmnsAc0NohjKecn13y-F-6jGn5VevUUEB4-AQL7JMwYK-yPrJ_FDEMOvxNx36f-1UE0jBN_hQG4ayy7pnSkyVVrXoX1DxVcUpCwBSyRqO2RPlL9fmCT12UW7HVteNjb9UeH7KRsSXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0177fa0248.mp4?token=p3fi-2b57W1Mfl-CREkqv8D9OQWuW2RMQcu3qTMTNTw-GWrxIcVlFijmF3TQeNXckhxuCPwju_wBnBxuAQQp6tmMD_ak1NpLMefWNj7ry_jAHUOgJlT78EDyZIBCkttdqQSLxPfWzeXzgo5TMZ8oagvp0jZ2rC9kveZq_uiY62taREgdnS_g7bBBILAsJykLQ6bmsrOehGYPUmnsAc0NohjKecn13y-F-6jGn5VevUUEB4-AQL7JMwYK-yPrJ_FDEMOvxNx36f-1UE0jBN_hQG4ayy7pnSkyVVrXoX1DxVcUpCwBSyRqO2RPlL9fmCT12UW7HVteNjb9UeH7KRsSXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
⚽️
علی‌فتح‌الله‌زاده مدیرعامل سابق استقلال: قلعه‌نویی نتیجه نمی‌گیره؛ من بودم عوضش می‌کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107809" target="_blank">📅 16:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107808">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e1845ed89.mp4?token=Qi1eIjBc8S6VdemL6XVd3l-57Mc0oeOH2AHl7y_1vrLPty8MOGPfUTtJfSCskYfdQbFGz91l-7WZ2Uq4dmLKy4B4G3bnuEUaAhkdZ6qGr9zMhL1QuNfH6S1PROCKeZb6PoB0KaoRaMFY3eIC0jNPhc1r-8CtG1OYBSLV_g7KAw4HLat5CkQPNrp1nLvnOIWhgL4aCp3p8DRtP1qat4f210ZfjlZBPG3XEhBgndSySQbCnMuL-PEvOOySmgse6rcfxFBmssrOjf3BidhDT1z-laIk1_WGzLnn1iWBOY2OGLK1P_pPGBhFThzqXfGzF2w6MVRth8qoj9r1-72v--jvQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e1845ed89.mp4?token=Qi1eIjBc8S6VdemL6XVd3l-57Mc0oeOH2AHl7y_1vrLPty8MOGPfUTtJfSCskYfdQbFGz91l-7WZ2Uq4dmLKy4B4G3bnuEUaAhkdZ6qGr9zMhL1QuNfH6S1PROCKeZb6PoB0KaoRaMFY3eIC0jNPhc1r-8CtG1OYBSLV_g7KAw4HLat5CkQPNrp1nLvnOIWhgL4aCp3p8DRtP1qat4f210ZfjlZBPG3XEhBgndSySQbCnMuL-PEvOOySmgse6rcfxFBmssrOjf3BidhDT1z-laIk1_WGzLnn1iWBOY2OGLK1P_pPGBhFThzqXfGzF2w6MVRth8qoj9r1-72v--jvQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
میثاقی: فیفا دی سوم چیشد؟ اگر قرار نبود بازی کنید حداقل لیگ را برگزار می کردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107808" target="_blank">📅 16:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107807">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63df69c40a.mp4?token=R3RVytjZDEfiJ_ElacZLufdttc0lzIpVBWIbs6BMHu0H5kdQaTB-yo8CRfkwVrQuwfuWKupJ0HHxbdsWRjrj7bF6ZaysmVYRPe04MC2zFBP68In6WSsGsCZfb_1MAhhCrP7RQXLp27CjySmE--MSrf6KNmuoME5LAeDeuNB5mbiKFjsfqJouSoNrtI9-44Oikx9muNf_-vsaH7oK04pYZ6aNFwIsyG6zxhwmq5cAi1i6nIKxAg27Sq4hJ15-uVOQ-8EVWlSWSGQ2Sk2n6uajgPpSYcnwxCO5_C9o1CvwskBr5BL3xKZQXfMotiXqTTg8mRVYlaqgxfWUmCqEPcBh-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63df69c40a.mp4?token=R3RVytjZDEfiJ_ElacZLufdttc0lzIpVBWIbs6BMHu0H5kdQaTB-yo8CRfkwVrQuwfuWKupJ0HHxbdsWRjrj7bF6ZaysmVYRPe04MC2zFBP68In6WSsGsCZfb_1MAhhCrP7RQXLp27CjySmE--MSrf6KNmuoME5LAeDeuNB5mbiKFjsfqJouSoNrtI9-44Oikx9muNf_-vsaH7oK04pYZ6aNFwIsyG6zxhwmq5cAi1i6nIKxAg27Sq4hJ15-uVOQ-8EVWlSWSGQ2Sk2n6uajgPpSYcnwxCO5_C9o1CvwskBr5BL3xKZQXfMotiXqTTg8mRVYlaqgxfWUmCqEPcBh-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
رسول‌مهربانی مجری دلقک و گزارشگر صداوسیما که با این الفاظ دیروز جنجالی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107807" target="_blank">📅 16:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107806">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dc22c75d3.mp4?token=dk38rEsWUbfND2SR_6k-nBGaG_sssPA_Iyva3nex6P4xqknU9YG5qRhYl-3aBjNP2f3Q00QH_YrnIYOTk01dzVsQGILfGnFR2jhnakzSGxbCsYz0N4PdSUF6obtJ-azMSj1_NiiZESp6KH1beTCFSyiFOzHGTrDmkj_I-uww5vtpKnIDDuu7WstiCGf45gx96wIQIk_aKYGR1yZYTdFweRndhsLescdNGdWcFAsRmZ7pLM7Oc2nBbXlf22lVlrrra8Ht2NZzfimaB7ISas-_TJUjC4Wj5xmJ6oXaLQBjxCL3vmShFfaVezQ5VrSsC5qrNMN_oRBLwR8Y85vwcCjXSU35Wfc1dLyYUKSfemQ9coqJY0tRNKl6v4dTtRAnk9WVsrqRvNZM-yYvgpHWdomvrMNq6MKPdyh6c24PDOl6bS__vPmALyC4cJHBHfJv5ZH2vnnISGc72uMK6o5BdPzIDP-pUavsZia_rWcsiK0hjm7ymrzivpQQ0lPPKGne69OhJhMERw46LIunkQVVY51NqE0L_3UxnD07Je-LsL2Dhh9SMVuidaP5_AVz9Iw6D0NmE215IUGQnfohIdDLGjKRPdfmg2zJlFDbwSUXzQJTwsrU4vis4wCljj1Z7_nMhauYQKzdlufXKKR5CLe4gH6M1nNmqBzB1cYjAvlj82xLv48" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dc22c75d3.mp4?token=dk38rEsWUbfND2SR_6k-nBGaG_sssPA_Iyva3nex6P4xqknU9YG5qRhYl-3aBjNP2f3Q00QH_YrnIYOTk01dzVsQGILfGnFR2jhnakzSGxbCsYz0N4PdSUF6obtJ-azMSj1_NiiZESp6KH1beTCFSyiFOzHGTrDmkj_I-uww5vtpKnIDDuu7WstiCGf45gx96wIQIk_aKYGR1yZYTdFweRndhsLescdNGdWcFAsRmZ7pLM7Oc2nBbXlf22lVlrrra8Ht2NZzfimaB7ISas-_TJUjC4Wj5xmJ6oXaLQBjxCL3vmShFfaVezQ5VrSsC5qrNMN_oRBLwR8Y85vwcCjXSU35Wfc1dLyYUKSfemQ9coqJY0tRNKl6v4dTtRAnk9WVsrqRvNZM-yYvgpHWdomvrMNq6MKPdyh6c24PDOl6bS__vPmALyC4cJHBHfJv5ZH2vnnISGc72uMK6o5BdPzIDP-pUavsZia_rWcsiK0hjm7ymrzivpQQ0lPPKGne69OhJhMERw46LIunkQVVY51NqE0L_3UxnD07Je-LsL2Dhh9SMVuidaP5_AVz9Iw6D0NmE215IUGQnfohIdDLGjKRPdfmg2zJlFDbwSUXzQJTwsrU4vis4wCljj1Z7_nMhauYQKzdlufXKKR5CLe4gH6M1nNmqBzB1cYjAvlj82xLv48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🙂
بازگشت سردار آزمون به تیم ملی بعد از مدت‌ها با کمک متن هوش‌مصنوعی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107806" target="_blank">📅 15:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107805">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab5019276.mp4?token=H9CyHiDIMWv6zTpTQMtCBlaml6OoDPl1sqfXOrd7rGTCmu0f7qlmmKThlqPtxcVbg1X8KXa5ONHAGib677wWYo5yVrtdcdH7B2vagYnfcJYKnMipVQmQOxYSTVggtdU1srlPe60Y-yxWyXHKKdb--D5sQaEjVka5yNUPPHCJqMmqr1FR5erEOYxtQ8BG1M3MclRGSUt6iJBeqLRyX7nExAr6KsM_jMl3S8h97WJC6cMCg8Y5ZRzV9d3nfcB439Q67ToSs9tA8fwQo4589jlHLAzfu0G9T_I8uZxIGC3MW1zIvyYRxenjuAH9ZXQb5RGJp0Y4c1Rttsjxbkwug0IVDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab5019276.mp4?token=H9CyHiDIMWv6zTpTQMtCBlaml6OoDPl1sqfXOrd7rGTCmu0f7qlmmKThlqPtxcVbg1X8KXa5ONHAGib677wWYo5yVrtdcdH7B2vagYnfcJYKnMipVQmQOxYSTVggtdU1srlPe60Y-yxWyXHKKdb--D5sQaEjVka5yNUPPHCJqMmqr1FR5erEOYxtQ8BG1M3MclRGSUt6iJBeqLRyX7nExAr6KsM_jMl3S8h97WJC6cMCg8Y5ZRzV9d3nfcB439Q67ToSs9tA8fwQo4589jlHLAzfu0G9T_I8uZxIGC3MW1zIvyYRxenjuAH9ZXQb5RGJp0Y4c1Rttsjxbkwug0IVDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
ویدیو وایرال شده از شادی رتبه ۲ و ۶ کنکور در حین اعلام نتایج کنکور سراسری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107805" target="_blank">📅 15:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107804">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49b154fa09.mp4?token=dL_A0j7tG6YIIeoVD46iXNhCcPQCxuaMvzDQM3MKjXs9vmnDbWr7jdcFqotJFdyhwN0UnTgcxHNXNT9SQm5TFbn60EKlYmMAFgjAtTQ3RM_IxWWWpcbB76xEBRrhokbC9_3__hMKK8Y6nZoUIRrdUuDWfdfQACXuPfUZLSzq8TJ4aLLJFJ-ulkrVTFJ9wNlj5XUTynjjWtZwL4vtfRC3Q9v1VbigSc9XJtrQzV7Qpn3PKKDlq7gFRjgTFSYG_2F6Z9FiMh34C5f8JWYyWOGemZXnCgNpVLmEB5xmqMjUeZVrkTmNf7lFJ-IToxEmn4bo5RKv_m3rD7t-hliMYqC0Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49b154fa09.mp4?token=dL_A0j7tG6YIIeoVD46iXNhCcPQCxuaMvzDQM3MKjXs9vmnDbWr7jdcFqotJFdyhwN0UnTgcxHNXNT9SQm5TFbn60EKlYmMAFgjAtTQ3RM_IxWWWpcbB76xEBRrhokbC9_3__hMKK8Y6nZoUIRrdUuDWfdfQACXuPfUZLSzq8TJ4aLLJFJ-ulkrVTFJ9wNlj5XUTynjjWtZwL4vtfRC3Q9v1VbigSc9XJtrQzV7Qpn3PKKDlq7gFRjgTFSYG_2F6Z9FiMh34C5f8JWYyWOGemZXnCgNpVLmEB5xmqMjUeZVrkTmNf7lFJ-IToxEmn4bo5RKv_m3rD7t-hliMYqC0Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
👤
👤
مشاور قالیباف رئیس مجلس:‌ تا به عادل فردوسی‌پور تذکر دادم، مطلب حمایت از علی کریمی را حذف کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107804" target="_blank">📅 14:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107803">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0m_D9l5AE24TR_FzWWiMbHskVZpvSALHIOC2fUSBkF7UmZOLDUX0-t9sSGro8AxUQyZOD_uR6pjW0xeR1yN5DOERqTcNJgBrT2kNZGjotXScOP6HYx-lYo7KqN7BKbSUvsX9FR4gbsO0jSCXGRp2UC0-W5iv6q-xdkoYxB_QeoHwqs05wUVx8mQgzkExJh1PMfq-GzZjZJu5buQ31G8m1oZj3VVTok3XOT7Bvlsz3_qgOcwObFYMtVKCm5k8eUUKycXLDQG0ReuJ07N05r7Q0dG2ojoGmzw5NbTRccyc-Wet-eFqBpHPaJttuHiMZ_i8uVixvJnSdLyBmMrvOmqMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇹🇷
وضعیت وخیم ترکیه در لیگ‌ملت‌های اروپا؛ بازی بعدیشون جلو ایتالیا هست که آردا گولر بدلیل دریافت اخطار محرومه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107803" target="_blank">📅 14:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107802">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e464e1d963.mp4?token=vniGIE_Stert8rLPqpb3FtIVjR4fXEf_pf94lOMEuhirE_vyD9em3NlT_M6LuHAZxKG0eb0pqY-wiUwxe3SbMX9LdcO-EBgup42zxJkHOa5Zx6FoJpZQ009mwB_AlrSbxsPh2wZOzVVLnbG6yyFvU0wsl_gYkttOa6JSbD0eNI7ws73ODyr4_LgBo9nltzIt3DAuf__LXFg-qywVWWC5od_ds-XN8cwfwZz7PttPddsAcG6aGyCm_owUPOqVPi5NEiecsgFZbDVBuME0Fhe1PcF8zQMMPQREWIORTGN4yWgweEX2c1N4pY_cIdHhbuPZh_TElcH1rPVPxwohdirt9AthQYJy1YKijCG_0Zl5bCnfLxoatQD4u1dnwikXN6uzqkz1UP5RCd1YuzMQQ66APkZE_83EHrbSiX_XT6T_gckDNj5zKDOn5YQWpxGIGivB6uhAVcjtissJxurB-UVficvdOtkVIq7xTl-zaG-mfnWY8NDa950anK_uXhFnxJ02occRxdMRIaFLnn3rct1eXWYhBhH-tw9nPNfzyiIeqkoaHQZG5uDbO3zNBPctgtcCCEJXDDDQX9AJmePvndasEuUiOvVAch7n3poJHH5aodwT1Qqy3W86ydCAUbyVssrKsyz-ng1jOSPEJQ9Z6thLsTIUAbdBTNMKN66Fa2qNMO8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e464e1d963.mp4?token=vniGIE_Stert8rLPqpb3FtIVjR4fXEf_pf94lOMEuhirE_vyD9em3NlT_M6LuHAZxKG0eb0pqY-wiUwxe3SbMX9LdcO-EBgup42zxJkHOa5Zx6FoJpZQ009mwB_AlrSbxsPh2wZOzVVLnbG6yyFvU0wsl_gYkttOa6JSbD0eNI7ws73ODyr4_LgBo9nltzIt3DAuf__LXFg-qywVWWC5od_ds-XN8cwfwZz7PttPddsAcG6aGyCm_owUPOqVPi5NEiecsgFZbDVBuME0Fhe1PcF8zQMMPQREWIORTGN4yWgweEX2c1N4pY_cIdHhbuPZh_TElcH1rPVPxwohdirt9AthQYJy1YKijCG_0Zl5bCnfLxoatQD4u1dnwikXN6uzqkz1UP5RCd1YuzMQQ66APkZE_83EHrbSiX_XT6T_gckDNj5zKDOn5YQWpxGIGivB6uhAVcjtissJxurB-UVficvdOtkVIq7xTl-zaG-mfnWY8NDa950anK_uXhFnxJ02occRxdMRIaFLnn3rct1eXWYhBhH-tw9nPNfzyiIeqkoaHQZG5uDbO3zNBPctgtcCCEJXDDDQX9AJmePvndasEuUiOvVAch7n3poJHH5aodwT1Qqy3W86ydCAUbyVssrKsyz-ng1jOSPEJQ9Z6thLsTIUAbdBTNMKN66Fa2qNMO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حضور بیژن مرتضوی و همسرش در دربند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107802" target="_blank">📅 14:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107801">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82e592cb76.mp4?token=nQ9Fry-Uuh0yjjEEdZFPLvdBVbwKoJcH6HUDJmn50s8XsO4d5CNdxJGSjzK2JvPUXmIMgdPTVSHkRHw5Pjw2hr12K05p2yJ_dDZ3KEHpoVwta9DOzCR52_1QtUwvNdwo2c-i6b3aVxavbIt-G09ORnUsHnh5_jB7_IzeiKnE5MR302uPN6hVbCb3SJexrwHv93xTRYO56uDQm8L9rI5qTbUAnRF4CeYRmU23EVDV40W4DLiAAvR6Lq9-tFdVPnyL3J0uS_4qYh3aatVuIb_FlnJTN4qAKxT84OixwQJFvSXBU_BfPHQ3OI6kLme1jZjo9uXy0rQ36iFizjGjx1FmDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82e592cb76.mp4?token=nQ9Fry-Uuh0yjjEEdZFPLvdBVbwKoJcH6HUDJmn50s8XsO4d5CNdxJGSjzK2JvPUXmIMgdPTVSHkRHw5Pjw2hr12K05p2yJ_dDZ3KEHpoVwta9DOzCR52_1QtUwvNdwo2c-i6b3aVxavbIt-G09ORnUsHnh5_jB7_IzeiKnE5MR302uPN6hVbCb3SJexrwHv93xTRYO56uDQm8L9rI5qTbUAnRF4CeYRmU23EVDV40W4DLiAAvR6Lq9-tFdVPnyL3J0uS_4qYh3aatVuIb_FlnJTN4qAKxT84OixwQJFvSXBU_BfPHQ3OI6kLme1jZjo9uXy0rQ36iFizjGjx1FmDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇮🇹
یک‌دقیقه با درخشش دوناروما مقابل فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107801" target="_blank">📅 14:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107800">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5581b57d8f.mp4?token=vjGklso303yKsBVZ4lafsOTAnVVCDeNZaPO5CQAMbkMTYpJhJmZm9L1A5saOGUjkFzwruAH5ZBzpFt-sIwf3FOFp-epJOdOgmljPC2sfB_6Je8AhFlQPf1m_b3PzcZI1np0fa13ECtSniuRmM1SwSVZDPGRivsN_KtCoCZC7Bbb4RBeq2hwHESKA1CWowLoe_s0A7_ERPj9OBIDT9ym_wpL4GKZ7irIZmm66OUOlKiPFRiailR_UqJFX1cpv1EVAshZjDYtdwB11BpcOjR4-oHsKS414uYJXuwsmXLoYqJn-4_s2F06BdxUJ4AqcdFLAbQG0orl1pCmRKm_71DWyrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5581b57d8f.mp4?token=vjGklso303yKsBVZ4lafsOTAnVVCDeNZaPO5CQAMbkMTYpJhJmZm9L1A5saOGUjkFzwruAH5ZBzpFt-sIwf3FOFp-epJOdOgmljPC2sfB_6Je8AhFlQPf1m_b3PzcZI1np0fa13ECtSniuRmM1SwSVZDPGRivsN_KtCoCZC7Bbb4RBeq2hwHESKA1CWowLoe_s0A7_ERPj9OBIDT9ym_wpL4GKZ7irIZmm66OUOlKiPFRiailR_UqJFX1cpv1EVAshZjDYtdwB11BpcOjR4-oHsKS414uYJXuwsmXLoYqJn-4_s2F06BdxUJ4AqcdFLAbQG0orl1pCmRKm_71DWyrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
دزدی مسئولین از بانک‌ها سوژه جالب و وایرال شده مهران مدیری در مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107800" target="_blank">📅 13:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107799">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
‼️
⚠️
درگیری‌شدید و خونین در مسابقه‌ای از لیگ زیر ۱۸ سال کشور که در مشهد برگزار شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107799" target="_blank">📅 13:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107798">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46755fa2d0.mp4?token=JK9KLDLk7LCpN8oESzpu4moTTRNMu1mgY6UKlWnOdglriZEmG-Omq-oJl-XudLh6YnbP9K7xMpOgJHv4yoGmNR7mkTKcbqQlfBaHFWNuAtJvZq23039XAYyFs1jTKggmmWj-aaWmkeARuDT3FuWgwkWK4QqtAr4mkZpJMruqGhkXyZIcxSSCIbkcrV4e9MMvMsKxzVC9x_wzwk5twsIX-4wXpzKcPwLm16MKU0L3UUhR8n1F8Ev1c-woF-2CpYN0nE-9SbrBwXPYDvlZ06Qj7sGCohQuji3-KSxSGzu7COuYJO8atyujp-YvseZ_mquBXg95oRLcfDen7sQQu6QNAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46755fa2d0.mp4?token=JK9KLDLk7LCpN8oESzpu4moTTRNMu1mgY6UKlWnOdglriZEmG-Omq-oJl-XudLh6YnbP9K7xMpOgJHv4yoGmNR7mkTKcbqQlfBaHFWNuAtJvZq23039XAYyFs1jTKggmmWj-aaWmkeARuDT3FuWgwkWK4QqtAr4mkZpJMruqGhkXyZIcxSSCIbkcrV4e9MMvMsKxzVC9x_wzwk5twsIX-4wXpzKcPwLm16MKU0L3UUhR8n1F8Ev1c-woF-2CpYN0nE-9SbrBwXPYDvlZ06Qj7sGCohQuji3-KSxSGzu7COuYJO8atyujp-YvseZ_mquBXg95oRLcfDen7sQQu6QNAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🐐
از توماس مولر پرسیدن: «مسی یا رونالدو؛ بهترین فوتبالیست تاریخ کیه؟»
جوابش؟
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107798" target="_blank">📅 12:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107797">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad1675b1b.mp4?token=EOFxaaHUunjXKO-MrCTGTm7TlDN4dEqKSRsMcIFRKkSVvmXZIumidGUqh_CsxM8tlrwS-4wZR4s_MfbDC-fsC4hWAQqYvGiekuLFdt2hmXRqbRWatiQUMOkhCGP8LYTIN15P24t4nLfseBqLKRAQxFA9Ao7FS1pUwUGe5BnWcms32yyuRz_wKg-1mKrFCKCIdvyFoSytE5NgosK0H6JLayuaCwweKSBgBG33mnZTlJYybcgYpRWLrerPmPnJR23yA7tIkLqAGqFBPc3Od1LDTjdD27CFsbmPIAwb96kk0VpV8syupru8HjRIdyzNs2wqh_fZoiVvgvQaWwnzz37gOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad1675b1b.mp4?token=EOFxaaHUunjXKO-MrCTGTm7TlDN4dEqKSRsMcIFRKkSVvmXZIumidGUqh_CsxM8tlrwS-4wZR4s_MfbDC-fsC4hWAQqYvGiekuLFdt2hmXRqbRWatiQUMOkhCGP8LYTIN15P24t4nLfseBqLKRAQxFA9Ao7FS1pUwUGe5BnWcms32yyuRz_wKg-1mKrFCKCIdvyFoSytE5NgosK0H6JLayuaCwweKSBgBG33mnZTlJYybcgYpRWLrerPmPnJR23yA7tIkLqAGqFBPc3Od1LDTjdD27CFsbmPIAwb96kk0VpV8syupru8HjRIdyzNs2wqh_fZoiVvgvQaWwnzz37gOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
عدم‌پاسخگویی سرمربی پرتغال درباره رونالدو در نشست‌خبری پیش از بازی با نروژ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107797" target="_blank">📅 12:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107796">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a683578dd.mp4?token=pZ0bhB78EnwHE9qRaiFlRfMqRXVRIlN3NddeZxsJ5SLgTr6iCi8UPQs2iV_r8SCk3q-Hbb7a_kwOvgFX78Q4i-6Ny97M-hMaqA-L31CV1wFCAdJhtRhtGk37anha89PqYpV_atX67ri1LeuorAORXHzWHYv_O5SmVQRkBJooteEWyIdHKs4BanDSn555oNgIW-6kNY9Jr9-PDzOxfnQ3xsqou2-LwpBrZh6BjGp1MFG4oVTXLRpzl7WH3Mu42dhzNrVadKJ5m5iz2N0uXm6-bjzpqGQ0DuUK_hYxPsCXksQSCo2OCCz0YCYDsxVhWyHA5dCOLvgUUlVVX-L0fNiFjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a683578dd.mp4?token=pZ0bhB78EnwHE9qRaiFlRfMqRXVRIlN3NddeZxsJ5SLgTr6iCi8UPQs2iV_r8SCk3q-Hbb7a_kwOvgFX78Q4i-6Ny97M-hMaqA-L31CV1wFCAdJhtRhtGk37anha89PqYpV_atX67ri1LeuorAORXHzWHYv_O5SmVQRkBJooteEWyIdHKs4BanDSn555oNgIW-6kNY9Jr9-PDzOxfnQ3xsqou2-LwpBrZh6BjGp1MFG4oVTXLRpzl7WH3Mu42dhzNrVadKJ5m5iz2N0uXm6-bjzpqGQ0DuUK_hYxPsCXksQSCo2OCCz0YCYDsxVhWyHA5dCOLvgUUlVVX-L0fNiFjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
دهقانی، مسوول مسابقات بین‌المللی فدراسیون فوتبال: باید ورزشگاه آزادی را همانند نیوکمپ بارسلون مسقف کنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107796" target="_blank">📅 12:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107795">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa3096b41.mp4?token=lVLlgiIFgHkDmQbiglfGTg0DQDpKYgbpktDoZgBwNP3N5iD4K0Nko0-3Qx0cYElsIZJh0IZqqHNmOVKZRyTBVh3reEQcdKRQIhfra0yNdr2keesEBdRgCNbTDLVvgOtAMrMwlDKtXwwRDLKTIp394JKBVdvdnkwc3ZQVeY5gjWuLOI72X4PqTFu0NgunlIodBOh6X-N-OqP2-r_tLB5jv5dpr1AuEvI66SVGAnLZc2sqpNQmq0-Hq05n9A6sURLQvCkUP_Somk63XH9xx1tnAUuAlMjS8TkP_X1XPC8zUy3fzrdb-wLpql7r9UhM8dhcZRo0Ag8GQtMZpGwg7N1RLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa3096b41.mp4?token=lVLlgiIFgHkDmQbiglfGTg0DQDpKYgbpktDoZgBwNP3N5iD4K0Nko0-3Qx0cYElsIZJh0IZqqHNmOVKZRyTBVh3reEQcdKRQIhfra0yNdr2keesEBdRgCNbTDLVvgOtAMrMwlDKtXwwRDLKTIp394JKBVdvdnkwc3ZQVeY5gjWuLOI72X4PqTFu0NgunlIodBOh6X-N-OqP2-r_tLB5jv5dpr1AuEvI66SVGAnLZc2sqpNQmq0-Hq05n9A6sURLQvCkUP_Somk63XH9xx1tnAUuAlMjS8TkP_X1XPC8zUy3fzrdb-wLpql7r9UhM8dhcZRo0Ag8GQtMZpGwg7N1RLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
ترس عجیب پیمان یوسفی مجری تلویزیون هنگام نام بردن از روحانی؛ یه وقت نیاید بالاسرمون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107795" target="_blank">📅 11:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107794">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ce37f880.mp4?token=KdOEsM_KxUPxlh2upV35NSaTLRfQWMy76ppbiZG4Yjz8-YezjJdaOjz7YHuVPzmsDhA2Jo8auAknxgtqq41sQNcGbEzInPO9mPW2Z3Xd7M54bxydUqMwcfP3I8uLMwIfJKmyxlQrHmxuZSZZmOboNeV9H3AOJ7cVhvWtxXOxo5sxo3AVSIxzz3Iv59objHlHJp5hzMQ_5CqasSUY03DSelmEX57T8jjDDbwjHWDGfHYNIzeVcU5YcDT9SFEC4RzsDLPh2nuhtb8mXZJediQ054kC4VA_xLFLLY8Sw9CC_gTG1OW039nPD9J2rtFnOWxYpXl9oe0USvRnrQx9YVEobJ0mFRNkhbF3GMNsdfYSpVobKYAisGByDjJvnHhZBWkxkpA4q5iI8GZjLtMndfDAq6MLVZuPfRVxhqdfzzj4VFfUly7t5JGnja04PvU5vPL7qlXww5hHQgTQIBZd3YZ55FD58j7uDTtsPKOj1-dOwGoXQjLz7BE9QBGP2RwivB9_Y9ghsb2zpIkZIQitekTOfQOcBYxBT0BTFwY8u0iYrN7MD4wL6X6ZixFhWnk51s_f3YX4fDYcmsRmAgvvEuOjOq-JM9mAqcT1ZXwpHF_ZY5kgr5Q3mmJFqCAmGrkxiizoSL8QNfIfxfd1FKqwkFskjDMHrP7r89wvHLWGIbPdsQc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ce37f880.mp4?token=KdOEsM_KxUPxlh2upV35NSaTLRfQWMy76ppbiZG4Yjz8-YezjJdaOjz7YHuVPzmsDhA2Jo8auAknxgtqq41sQNcGbEzInPO9mPW2Z3Xd7M54bxydUqMwcfP3I8uLMwIfJKmyxlQrHmxuZSZZmOboNeV9H3AOJ7cVhvWtxXOxo5sxo3AVSIxzz3Iv59objHlHJp5hzMQ_5CqasSUY03DSelmEX57T8jjDDbwjHWDGfHYNIzeVcU5YcDT9SFEC4RzsDLPh2nuhtb8mXZJediQ054kC4VA_xLFLLY8Sw9CC_gTG1OW039nPD9J2rtFnOWxYpXl9oe0USvRnrQx9YVEobJ0mFRNkhbF3GMNsdfYSpVobKYAisGByDjJvnHhZBWkxkpA4q5iI8GZjLtMndfDAq6MLVZuPfRVxhqdfzzj4VFfUly7t5JGnja04PvU5vPL7qlXww5hHQgTQIBZd3YZ55FD58j7uDTtsPKOj1-dOwGoXQjLz7BE9QBGP2RwivB9_Y9ghsb2zpIkZIQitekTOfQOcBYxBT0BTFwY8u0iYrN7MD4wL6X6ZixFhWnk51s_f3YX4fDYcmsRmAgvvEuOjOq-JM9mAqcT1ZXwpHF_ZY5kgr5Q3mmJFqCAmGrkxiizoSL8QNfIfxfd1FKqwkFskjDMHrP7r89wvHLWGIbPdsQc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
🎙
🇮🇷
بغض محمد عمری ستاره پرسپولیس ترکید: از روستا به تهران آمدم؛ شب‌ها با یک بربری می‌خوابیدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107794" target="_blank">📅 11:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107793">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9581683260.mp4?token=Z25DznlXngBfHtmdFkTZsfYdSd1pHqY8LmVFrD6EgEKrzxEoX24moSGv7Vr-n_98XJ1tVOpcsTGx7dCfM7l0hsA80vDabe__osKDxDmrj8vBb_mJ13RAChZ3kXHqvtvP86JI1q1I15vrcY-KWBm0gNFz0YSsoKf_4U7jmrmL0ZSqMUGg57hLmaL94Ea0y7KE0e_UwC3tPaBSIeMANBcnnlPcwjBU3o7LKoMoGaRYK3bK1jgPaRS1_wIKvINxa3rn43Sqqb9rDFfwurquJrkQ3ebSzuVyqubYoklfxl5nTPGkWtsL1Hcaz-AbRluEbEDKbLUb8xMTbG4eLu9HEf5fGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9581683260.mp4?token=Z25DznlXngBfHtmdFkTZsfYdSd1pHqY8LmVFrD6EgEKrzxEoX24moSGv7Vr-n_98XJ1tVOpcsTGx7dCfM7l0hsA80vDabe__osKDxDmrj8vBb_mJ13RAChZ3kXHqvtvP86JI1q1I15vrcY-KWBm0gNFz0YSsoKf_4U7jmrmL0ZSqMUGg57hLmaL94Ea0y7KE0e_UwC3tPaBSIeMANBcnnlPcwjBU3o7LKoMoGaRYK3bK1jgPaRS1_wIKvINxa3rn43Sqqb9rDFfwurquJrkQ3ebSzuVyqubYoklfxl5nTPGkWtsL1Hcaz-AbRluEbEDKbLUb8xMTbG4eLu9HEf5fGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمایش های عجیب وینی مقابل هند هم ادامه داشت!
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107793" target="_blank">📅 11:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107792">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107792" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107792" target="_blank">📅 11:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107791">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sObxuryt3nJI6HfuVtyEXq_PORYzwHWFPz7_QI-XrDeacua2oKu2-CbbCVEtl2LD6_WArUEp4sDxvoe0sGdG9QetpMRL3inZ_c9tq5IhxBKZTmz5py20_CXyI1Ovy7zGGQDuQarqcXz3Y-DiHWtfCZ5ZfJMwCBadXVJPZ9K2ARH0S5xezbpuOKLdpH9Da2X44klFMO9Jo8haFEZYZi49Nq3MYZ3AoOQ2R_spW4Rk-_f9YjGdL3-efhD097GH6cTvjA6iMWYqd1PrAA90OSK6BsxqEEXWhVUdfW3LN3Y-n0TeAF0WeXcKJEARCTY7dLAG4G71hK_O6_mBcyE9mQzhWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آلمان
🆚
یونان
صربستان
🆚
هلند
نروژ
🆚
پرتغال
دانمارک
🆚
ولز
آفریقای جنوبی
🆚
مصر
مالی
🆚
مراکش
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107791" target="_blank">📅 11:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107790">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6634bc99dd.mp4?token=HcWuj142Y1tLW5c-1uTV5YC1LGjjK687_zM3VHr_QImTQ6CrBnFBecfmxE23mq9D4fdxUC47U4zlfIBSf2fcAcxdFXSyQxz1yXzDsF9gXFQ1a-9yHZ-dj2OE-FkXFZQAIYSl4Gn2zKOgxMuvkJKhuYx7dvCw1SCrmtZ5SOrcizl6yTU54_sICRykc6S0qnUeiqeMbEvrh_GwdbufTwEScdLa_3lSZXkJ1hQbdRoYeALsy1SxB3wmDTU1Y-i7kPcHqXWX0mkxqbbpcBj12EeBTmfJcyBXl6V71_TOIlaM7YwNz-Td0mFjRAFjRrvwYkJNW3j1oY9e0mqV3uS30lZz9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6634bc99dd.mp4?token=HcWuj142Y1tLW5c-1uTV5YC1LGjjK687_zM3VHr_QImTQ6CrBnFBecfmxE23mq9D4fdxUC47U4zlfIBSf2fcAcxdFXSyQxz1yXzDsF9gXFQ1a-9yHZ-dj2OE-FkXFZQAIYSl4Gn2zKOgxMuvkJKhuYx7dvCw1SCrmtZ5SOrcizl6yTU54_sICRykc6S0qnUeiqeMbEvrh_GwdbufTwEScdLa_3lSZXkJ1hQbdRoYeALsy1SxB3wmDTU1Y-i7kPcHqXWX0mkxqbbpcBj12EeBTmfJcyBXl6V71_TOIlaM7YwNz-Td0mFjRAFjRrvwYkJNW3j1oY9e0mqV3uS30lZz9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت‌جالب لامین‌یامال بعد از بازی دیشب
❤️
👌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107790" target="_blank">📅 11:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107789">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/321c017aa1.mp4?token=eaU58VX94e-2R94EBE9KpRxk52Ys2TP-4rSTd94K1fK2RLvX_ORn6EZgmQGd_8EJenNQc-rx4l1OVae_npVM6eCqFu4I31OMv0HGRPSyb5KumiTLoQZgOD1SYABrSMbBRrImP9p-P-DA0bu9Xzd_CJN_E3onUsc2-_0zO5nMkfPyhFdMQJ8dQ21jbaFf42G4XPea3H5kizv7j9YsgZOCgILZ0vSCRMxSO6bM_A_NrVyDOKfB81STYrgpaN0TACfi0QbptoYwLWMqHyJLgDX71YLVVZsP4XnvENNBLiZCG6cS0YVEPBDPpCEVmQQYfD6ZJdLMrFEuR43sH7Xx1IRQ7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/321c017aa1.mp4?token=eaU58VX94e-2R94EBE9KpRxk52Ys2TP-4rSTd94K1fK2RLvX_ORn6EZgmQGd_8EJenNQc-rx4l1OVae_npVM6eCqFu4I31OMv0HGRPSyb5KumiTLoQZgOD1SYABrSMbBRrImP9p-P-DA0bu9Xzd_CJN_E3onUsc2-_0zO5nMkfPyhFdMQJ8dQ21jbaFf42G4XPea3H5kizv7j9YsgZOCgILZ0vSCRMxSO6bM_A_NrVyDOKfB81STYrgpaN0TACfi0QbptoYwLWMqHyJLgDX71YLVVZsP4XnvENNBLiZCG6cS0YVEPBDPpCEVmQQYfD6ZJdLMrFEuR43sH7Xx1IRQ7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
▶️
کنایه مهران مدیری به ماجرای نماینده مجلس و مامور راهور در مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107789" target="_blank">📅 10:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107788">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7979edd7.mp4?token=I-3y2WwUGvn3b35Bae3hIyOJbGm6aTczbbC5bNbuPld-SPYb2ctVXMRbQ7MoO7igDAGIKeUmLJ-5DibsH7tJ3fRBfzLs8TnEZWerduG8U3bD7otnY4ogAQ_mHQjlZ9_VRCdX_dThesFHhD6EX5Jsjywr8tQnVvmRKhp0Yyo95hBB5lUGgbVcBnqgqaaeN0LSl4Rjkr_Z7rRYbp3pqImxnreqGCCpw2Fh8Cdj5HhkG6Hq-Cwg9lmMb3EU8jhnHKp7fpVpO1TB2japuoD3D588x3fuQgFJfIRc-3DEMSl7NLjmjnAAjkmFZhU2DkIUTqwum15FtbYFZy8T-fRO9uupnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7979edd7.mp4?token=I-3y2WwUGvn3b35Bae3hIyOJbGm6aTczbbC5bNbuPld-SPYb2ctVXMRbQ7MoO7igDAGIKeUmLJ-5DibsH7tJ3fRBfzLs8TnEZWerduG8U3bD7otnY4ogAQ_mHQjlZ9_VRCdX_dThesFHhD6EX5Jsjywr8tQnVvmRKhp0Yyo95hBB5lUGgbVcBnqgqaaeN0LSl4Rjkr_Z7rRYbp3pqImxnreqGCCpw2Fh8Cdj5HhkG6Hq-Cwg9lmMb3EU8jhnHKp7fpVpO1TB2japuoD3D588x3fuQgFJfIRc-3DEMSl7NLjmjnAAjkmFZhU2DkIUTqwum15FtbYFZy8T-fRO9uupnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
🇮🇹
درخششِ دوناروما اجازه ی گرفتن انتقام رو به زیدان در بازی با ایتالیا نداد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107788" target="_blank">📅 10:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107787">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95502ba1a6.mp4?token=URJyH8_5KMuvTaRQEkyT7lsInoFbhtq8D8FmYfr76vnfBNHLSXxCCngFXAPV2DF2Nx7GmzpfPDL_QzzCGlbm_tv-li3o4BIexWpSc0VD3h3bjYhUhZL3CWLXpPBFhwe0y6O_1NR8iolgNOPFiNd56CqLVkPgrhY2Rvv9GPSye2xYAABKuNISAAiBNDN3C1zIUwPGMOUQWD3d8vvkOgbgT6JJhBUT7_KSAocw7--YU9lULKoW3uxKNmCmhTuMcnpUbLnqNehPXKXWUXb2g7Be2X23aoiFfqDRZhIDE2AFqqt82v-PqNKybERWGGFH-g2w9MHOw9c67Qs0AP-KydyeBUQtHXqNJPphl3yy8p4_bDijsa0X1GBGSEt7zmlF7iYTRIxGFjcg5afLd19RqlNkJS-Tlz1mQhCvdNE7bEv_uVgC17Xu7JqRdN6oR3z4hw5-zumM3UNvdLiNiX_bta0CerEuqYc9EUS18H_x1AOxceOKwWckyQ1vE0clKbOZ5sx_VjyR_w4uBBQI2bydr645xQNoURafiJv19WJkOBYtTpUsuhj_T3n4JB5NhwyajpB7dH71i76pU1wk7HTVHeUJXlik23Mmj7-Gn6oM0CZ_jU-PJ5Eq22PVpBUtE-roO4RTy-XVpryfSsdJH_sWGmVLz4v6mwYVKSg-W2Cjp3HyKGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95502ba1a6.mp4?token=URJyH8_5KMuvTaRQEkyT7lsInoFbhtq8D8FmYfr76vnfBNHLSXxCCngFXAPV2DF2Nx7GmzpfPDL_QzzCGlbm_tv-li3o4BIexWpSc0VD3h3bjYhUhZL3CWLXpPBFhwe0y6O_1NR8iolgNOPFiNd56CqLVkPgrhY2Rvv9GPSye2xYAABKuNISAAiBNDN3C1zIUwPGMOUQWD3d8vvkOgbgT6JJhBUT7_KSAocw7--YU9lULKoW3uxKNmCmhTuMcnpUbLnqNehPXKXWUXb2g7Be2X23aoiFfqDRZhIDE2AFqqt82v-PqNKybERWGGFH-g2w9MHOw9c67Qs0AP-KydyeBUQtHXqNJPphl3yy8p4_bDijsa0X1GBGSEt7zmlF7iYTRIxGFjcg5afLd19RqlNkJS-Tlz1mQhCvdNE7bEv_uVgC17Xu7JqRdN6oR3z4hw5-zumM3UNvdLiNiX_bta0CerEuqYc9EUS18H_x1AOxceOKwWckyQ1vE0clKbOZ5sx_VjyR_w4uBBQI2bydr645xQNoURafiJv19WJkOBYtTpUsuhj_T3n4JB5NhwyajpB7dH71i76pU1wk7HTVHeUJXlik23Mmj7-Gn6oM0CZ_jU-PJ5Eq22PVpBUtE-roO4RTy-XVpryfSsdJH_sWGmVLz4v6mwYVKSg-W2Cjp3HyKGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
نمای‌کامل از صحنه‌جنجالی بازی لیگ‌برتر بانوان میان استقلال و گل‌گهر سیرجان؛ فقط جیغ و داد داور و بازیکنان رو ببينيد
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107787" target="_blank">📅 09:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107786">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363181b8d9.mp4?token=RcI4wCTiFJPh6ubYf2HFOTTodYhZnW9CaxM01QBG90TPiEgiW0ebkkuuI1sHNIZEx6nbRTNDRH6ZzlQsWqP9r08NCWxvCjUiD7-A1PaoH74oDlwEue_WiovpTtg184p0PtVni5gomz8b9p-8Sdkp0NXxN2b47zms-IdLBRY1Ri14EWQ6kE0rqgbSxb_TRm__f8JwIpPIJJZ7jqECFNB37JVeTCgg5iGsxdu4wk0INaggJLXy92DuAE17_ADPErpqQRMljaQnoPFPYqnPhIWxlbGY_MrARyv4dDT1jVg1ppJ5WdtTU_H-F13s8FIB5hZpWlwJ3u1qv8os2zit0hYnOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363181b8d9.mp4?token=RcI4wCTiFJPh6ubYf2HFOTTodYhZnW9CaxM01QBG90TPiEgiW0ebkkuuI1sHNIZEx6nbRTNDRH6ZzlQsWqP9r08NCWxvCjUiD7-A1PaoH74oDlwEue_WiovpTtg184p0PtVni5gomz8b9p-8Sdkp0NXxN2b47zms-IdLBRY1Ri14EWQ6kE0rqgbSxb_TRm__f8JwIpPIJJZ7jqECFNB37JVeTCgg5iGsxdu4wk0INaggJLXy92DuAE17_ADPErpqQRMljaQnoPFPYqnPhIWxlbGY_MrARyv4dDT1jVg1ppJ5WdtTU_H-F13s8FIB5hZpWlwJ3u1qv8os2zit0hYnOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
‼️
علی فتح‌الله‌زاده:
🔺
فدراسیون با یه قانون من درآوردی سه جانبه برگزار کرد، میتونست با همون منطق بین ۴ تیم اول بازی بزاره قهرمان مشخص کنه.. به استقلال ظلم شد چون به احتمال ۹۰ درصد تو حذفی قهرمان بود و اون جام رو هم از دست داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107786" target="_blank">📅 09:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107785">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/708801c3df.mp4?token=hYeCQCn3HUSiRO6yx42rvQnvPgeRfm2CzNDt-Z365nzlduzSs-ZcY5tFY94UpXh9Zj-K-d3qmlZs_UcwRWZYAJNv374R5pcdNNxP5mmIP_y5_Hh5mDt7mkqYKX5qblq_yXZcszPU6WRcBIWyZmCbdJ6quv1BlFvC9QdKV4xV72EFKX6GofxendJAhdmp-vxuC9ipcKZ3f6fya1iVis0DC7JW46RuqpBjnvU-CJPDxOEK84q_AxWKr5I9Jcr8F3D1W8oNQdWA3MewBaB8wrHft9kOQZpYgYDzgXvjA0iScpRjy0VAb1Ke1UjQ9qM5mq3tfO9UOSzqcZS0xvPMxjxZxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/708801c3df.mp4?token=hYeCQCn3HUSiRO6yx42rvQnvPgeRfm2CzNDt-Z365nzlduzSs-ZcY5tFY94UpXh9Zj-K-d3qmlZs_UcwRWZYAJNv374R5pcdNNxP5mmIP_y5_Hh5mDt7mkqYKX5qblq_yXZcszPU6WRcBIWyZmCbdJ6quv1BlFvC9QdKV4xV72EFKX6GofxendJAhdmp-vxuC9ipcKZ3f6fya1iVis0DC7JW46RuqpBjnvU-CJPDxOEK84q_AxWKr5I9Jcr8F3D1W8oNQdWA3MewBaB8wrHft9kOQZpYgYDzgXvjA0iScpRjy0VAb1Ke1UjQ9qM5mq3tfO9UOSzqcZS0xvPMxjxZxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🥈
ایشون کیمیا زارعی ورزشکار رشته روئینگ هستن که تو مسابقان ناگویا یه مدال طلا و یه نقره به دست آوردن
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107785" target="_blank">📅 09:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107784">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a540d193c.mp4?token=LnzTXiYwJnkkMjz2umUcue3FOrsQgBmFzgPHjCzizw3iM2WDkbNRmynmXJT9-8NTS3ucIpSOqeYVbeGJG-I2LEVcWIZlaNgm4ayYiCEz2-fihg2R0Np2g50tMppIzOeXxEujvtynvkKPcr0WToiGvDnSGvLD3mhbcRKqo9pXCywrO8qedDmkGB9Hp-KkaKWIM1G6mIAuaU0DNN36UZcaQEjd8iwrix5dxtuJcQVctc1GXcRkeU1PDuBTDDPCw5HtJC0g0xj_4YnJBGEzJqVy-8iEm4qapg2HfGisZ9jYkn8SIITrHSVo6XvCYtpb6-tEVfIIc4BIE_M3eyRB8u24hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a540d193c.mp4?token=LnzTXiYwJnkkMjz2umUcue3FOrsQgBmFzgPHjCzizw3iM2WDkbNRmynmXJT9-8NTS3ucIpSOqeYVbeGJG-I2LEVcWIZlaNgm4ayYiCEz2-fihg2R0Np2g50tMppIzOeXxEujvtynvkKPcr0WToiGvDnSGvLD3mhbcRKqo9pXCywrO8qedDmkGB9Hp-KkaKWIM1G6mIAuaU0DNN36UZcaQEjd8iwrix5dxtuJcQVctc1GXcRkeU1PDuBTDDPCw5HtJC0g0xj_4YnJBGEzJqVy-8iEm4qapg2HfGisZ9jYkn8SIITrHSVo6XvCYtpb6-tEVfIIc4BIE_M3eyRB8u24hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
🐐
حمایت فیلیپه ملو از کریستیانو رونالدو:
"یه تفاوت خیلی فاحش بین رفتار بازیکنا با کریستیانو رونالدو و رفتار بازیکنای آرژانتینی با مسی وجود داره.‌ من می‌بینم وقتی بازیکنای حریف مقابل کریستیانو رونالدو بازی می‌کنن، خیلی بیشتر بهش احترام می‌ذارن. تو تیم ملی پرتغال، هیچ‌کس حتی به گرد پای کریستیانو رونالدو هم نمیرسه! تو نمی‌تونی بذاری بهترین بازیکن تاریخ همین‌جوری بذاره بره، انگار نه انگار که اتفاقی افتاده؛ اصلاً راه نداره!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107784" target="_blank">📅 08:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107783">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d08431eb67.mp4?token=AawcBGKaBJkoouq5S9Wv0xAdH0X3cT-STnf3WH49exMPuWVdWd8YBkDful63gKwEG82_19uFlG59Ci2E9UqFo8wnDLYOzslcN0d5PvioEA60R_-nmLDHOpgrnEOPn4BNNACiI_UTGHCDrXhdvI646QIDurBSLxwCVU8bO8BUgRF3U3T7L740xlqcQed_jU_bDvwlKAdTvKfvEAS-_fi-rq3iOm6L0UkNuDP95Uoj3LLZ3vFaYNU73eogz2D9sGFz_NU92fDGWqIYd3y6m3w8Fp8uyQTP5Bu6hxbJRQkUYba3e6pZs_C-0wXYIORq5W_JoYVpPqoxlArisEwIwmB4gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d08431eb67.mp4?token=AawcBGKaBJkoouq5S9Wv0xAdH0X3cT-STnf3WH49exMPuWVdWd8YBkDful63gKwEG82_19uFlG59Ci2E9UqFo8wnDLYOzslcN0d5PvioEA60R_-nmLDHOpgrnEOPn4BNNACiI_UTGHCDrXhdvI646QIDurBSLxwCVU8bO8BUgRF3U3T7L740xlqcQed_jU_bDvwlKAdTvKfvEAS-_fi-rq3iOm6L0UkNuDP95Uoj3LLZ3vFaYNU73eogz2D9sGFz_NU92fDGWqIYd3y6m3w8Fp8uyQTP5Bu6hxbJRQkUYba3e6pZs_C-0wXYIORq5W_JoYVpPqoxlArisEwIwmB4gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
سوپرگل سکسی یامال در تمرینات اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107783" target="_blank">📅 08:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107780">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df11e10418.mp4?token=VL16RxdRpmVEoxpuBBAta4Cc-rO_gOJDyJ50b3OapVxQ6fmHgdxkSok3fv-D6iR3f4IwIPoFCWoodsiVnRheKVnUTDnruEU5zd6IgghwOervavDzUrjIAXfYfPy2IP5TVoq6HYr_gQwXgKAhPEQ7qaRwVO9xkmz0Fywyiv8B86X69JjWglymT1IDoSnt_eWg1CDWMgA4_xcqUZq5VTldXYVDsEpgd3HhZaMxJIT1_y8UOnecQA-aVmc9jPK-oW4eCb6ZfnynTX4QJKODiHhzKj1DvVcbk7yO3SfBE5bTFbwsP63U3PYthMzwEMRJnxpXpHvKlYHNk2L3lrIAwsHTKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df11e10418.mp4?token=VL16RxdRpmVEoxpuBBAta4Cc-rO_gOJDyJ50b3OapVxQ6fmHgdxkSok3fv-D6iR3f4IwIPoFCWoodsiVnRheKVnUTDnruEU5zd6IgghwOervavDzUrjIAXfYfPy2IP5TVoq6HYr_gQwXgKAhPEQ7qaRwVO9xkmz0Fywyiv8B86X69JjWglymT1IDoSnt_eWg1CDWMgA4_xcqUZq5VTldXYVDsEpgd3HhZaMxJIT1_y8UOnecQA-aVmc9jPK-oW4eCb6ZfnynTX4QJKODiHhzKj1DvVcbk7yO3SfBE5bTFbwsP63U3PYthMzwEMRJnxpXpHvKlYHNk2L3lrIAwsHTKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎁
زلاتان ابراهیموویچ به مناسبت تولد ۴۵ سالگی‌اش، یک خودروی فراری مدل F80 کادو داده. قیمت این فراری، حدود ۳.۶ میلیون یورو تخمین زده می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107780" target="_blank">📅 00:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107779">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84ad4f46e.mp4?token=lo7N9LNILY0OHUm6DQ8u9HeMtF0wTYEzWdFpG8EkQfGVnRzYjlJMm61v58WrWLWdq-gLd1PFYEJwNDnRYKqAQZHsS0O3lnKvgzTFCWObuQPYRfIiOga5GznNpgPVcdatz5y7kKZwF0Lgna0HyBISLIyY7s3FTKhuevlBFBX2P3EQ1eX3ENUMtdk5gyHnrlVVZI2XntrWJ98NBnhs22HNsL5adttEsi3EAqGfMbZQUdkhbmS7iBoi-WAjdZnl6E9JRj220usM6y--qA9r9uI0OFGBsleXKwwizD10eDasFJa2YC0S2VYIHgEzYMTp0lFCUqFd95W-NudKVBgPGueMNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84ad4f46e.mp4?token=lo7N9LNILY0OHUm6DQ8u9HeMtF0wTYEzWdFpG8EkQfGVnRzYjlJMm61v58WrWLWdq-gLd1PFYEJwNDnRYKqAQZHsS0O3lnKvgzTFCWObuQPYRfIiOga5GznNpgPVcdatz5y7kKZwF0Lgna0HyBISLIyY7s3FTKhuevlBFBX2P3EQ1eX3ENUMtdk5gyHnrlVVZI2XntrWJ98NBnhs22HNsL5adttEsi3EAqGfMbZQUdkhbmS7iBoi-WAjdZnl6E9JRj220usM6y--qA9r9uI0OFGBsleXKwwizD10eDasFJa2YC0S2VYIHgEzYMTp0lFCUqFd95W-NudKVBgPGueMNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
‏لحظه
اصابت صاعقه به برج میلاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107779" target="_blank">📅 00:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107778">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKInIfFSNNIbvooCUu4ecB5-9fO7IPIg0siBzy2X4gFlGCAnxJIfkHnfiHpyRIhXtz-wUMHCPzekSBslNnt9Pj0l5u5_91SLSCkkUt2OiUsM7DuQIDSK8Yjv2koPKAjw-wu2BDSfl0rlrOHCzJXQqkrg_qAEkTLdJVI0p__qbU85sgieDYpN9je48w8lpjrGSqvYh2tpNCA-Omm7FZXyIKOWq-wWxYD3l7TABXxvIfI3k3pcBk9034px8ZsdOyqt0f2n0bOLQATYiwGKGlOa3Mal0wynHMBeIL9S5--WJNgHIWOyD8BsojL7v7IpIZ09c1Xc8t5he6iO4s4O9AjA0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
لیگ ملت‌های اروپا| تیم اول و دوم ندارد؛ اسپانیا با هر ترکیبی برنده می‌شود
اسپانیا سه - ‌چک یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107778" target="_blank">📅 00:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107777">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abea032aaf.mp4?token=vKWtFyIQqLstedMjdJpfbMvMuql7qfmii-D-xlt9__M1xS6J_h8wiEy_HirxUg4PmWwKrt_YfC7C2WNl67sEZ2EuMZyOXw6oICDmCPGu4AgZLmA_zKLxvXriwtnpPF0o_fULmMQvH0dcnAYFYoIuzkaigTrsnKYxeeaFnxVq5v6BCWrWZZRLrV63w1YFivB_2UrVJTJ7o13t1i86MwvCPQxMGkXbeuyDafegjmwBOrG3JlKjlGllW3KjYxPTwRzrsWwesCV964VJBQrrmcZrUgdK2VyIZEzPAYJA5AgjS6rt5KgZS8UJeED77vbNzTwQNoXTfJX_NGOpz8HJ8pL3Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abea032aaf.mp4?token=vKWtFyIQqLstedMjdJpfbMvMuql7qfmii-D-xlt9__M1xS6J_h8wiEy_HirxUg4PmWwKrt_YfC7C2WNl67sEZ2EuMZyOXw6oICDmCPGu4AgZLmA_zKLxvXriwtnpPF0o_fULmMQvH0dcnAYFYoIuzkaigTrsnKYxeeaFnxVq5v6BCWrWZZRLrV63w1YFivB_2UrVJTJ7o13t1i86MwvCPQxMGkXbeuyDafegjmwBOrG3JlKjlGllW3KjYxPTwRzrsWwesCV964VJBQrrmcZrUgdK2VyIZEzPAYJA5AgjS6rt5KgZS8UJeED77vbNzTwQNoXTfJX_NGOpz8HJ8pL3Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل سوم اسپانیا به جمهوری چک توسط میکل مرینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107777" target="_blank">📅 00:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107775">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f7684655.mp4?token=ppLacZTsDuSSR-lS5fc6M8FLWXR8nHp-TaRLsYCNp4cMDttKrAK-xe8X9xt5UI4C2t9MxkGSK0Mk6lOkRjOZ0TcJVbXiDsBFtm8A4pcyVBkAgYrd7RqCAaeqbiLZSJ9B5Kpf7bY2h1dui-Jbhn7-Cil6CnJGK1SHpeNqj2WVli_O_fwiljWnySj-V2y2lIZYXf_vYSvjBv8l6yOocpAxj6a0d8li_HPERuEBTjCpUNVk6Al4Ksp9d17DhuMMWr53x5b_KGBR70XWMr6jE0Gh_dtXt0YMMJe7IHb9BzVoAcqBwaq0Av2dK0HQm5GqwhrbPZIQ3LsX4TvjMXp3dT-0MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f7684655.mp4?token=ppLacZTsDuSSR-lS5fc6M8FLWXR8nHp-TaRLsYCNp4cMDttKrAK-xe8X9xt5UI4C2t9MxkGSK0Mk6lOkRjOZ0TcJVbXiDsBFtm8A4pcyVBkAgYrd7RqCAaeqbiLZSJ9B5Kpf7bY2h1dui-Jbhn7-Cil6CnJGK1SHpeNqj2WVli_O_fwiljWnySj-V2y2lIZYXf_vYSvjBv8l6yOocpAxj6a0d8li_HPERuEBTjCpUNVk6Al4Ksp9d17DhuMMWr53x5b_KGBR70XWMr6jE0Gh_dtXt0YMMJe7IHb9BzVoAcqBwaq0Av2dK0HQm5GqwhrbPZIQ3LsX4TvjMXp3dT-0MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول جمهوری چک به اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107775" target="_blank">📅 23:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107774">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdcc4901e9.mp4?token=B-WUf-g24rvuepHh4Y4fKDcRZIhfdy1FLMB1MT2JGht7e9fpvBF80MQ6rajjTWHe6fsv1leQ5kghtV4p18L9IUgbJ2P0EOfmokpalEd7Oy_DkS688phmNUqutEPmd6IGl46xO0aouNr80ENEJXkaXi7XMRM73MC8ygF-WBSTt5BrLOEqAKdfL_TqT9tORA-LpNNHfPO6IUW2DR41M9T0BXEq870bwh_uP54J1m6089DPSC2LhwIPafB_vlfA50OGJHZnhQTEq2JEwaPmkUtWrkdAFwkY-VAmgnXtfMKFIGaPIEwwHV5ndtmeGQsUncK57Ug1vRszDbWYAO7akU7SlSFNI9-46WXblAKvrSLEsuOCpGS0d4IvngFZztl457HHOB9DjJffwtJISXZQrcUPg1X1SIuUeUCctgYp489dBiX9qJZaAlcbCjshCSZQ_enBGzsWkvhUAie2DgQPNBAnZis4qZpJXVk-uJslAFYuk-REAFBq2CQvIF_imqd50Z0Ul6vDwX7MPV96qUz1dLCMBUzSZ9g0-hKONiCXydI3J2qeH8vNKQuMRwQ9AV4hgHjx23hVDeKm-bMFOVw2kkqFDzItZb7Yh3FlRxRmr0iiKR0avibEIJ2jtGgHM2jX-YCTuRprKjaeJ_s9t92oHUX9vPgEQRy3ddFPACJKVsYBk4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdcc4901e9.mp4?token=B-WUf-g24rvuepHh4Y4fKDcRZIhfdy1FLMB1MT2JGht7e9fpvBF80MQ6rajjTWHe6fsv1leQ5kghtV4p18L9IUgbJ2P0EOfmokpalEd7Oy_DkS688phmNUqutEPmd6IGl46xO0aouNr80ENEJXkaXi7XMRM73MC8ygF-WBSTt5BrLOEqAKdfL_TqT9tORA-LpNNHfPO6IUW2DR41M9T0BXEq870bwh_uP54J1m6089DPSC2LhwIPafB_vlfA50OGJHZnhQTEq2JEwaPmkUtWrkdAFwkY-VAmgnXtfMKFIGaPIEwwHV5ndtmeGQsUncK57Ug1vRszDbWYAO7akU7SlSFNI9-46WXblAKvrSLEsuOCpGS0d4IvngFZztl457HHOB9DjJffwtJISXZQrcUPg1X1SIuUeUCctgYp489dBiX9qJZaAlcbCjshCSZQ_enBGzsWkvhUAie2DgQPNBAnZis4qZpJXVk-uJslAFYuk-REAFBq2CQvIF_imqd50Z0Ul6vDwX7MPV96qUz1dLCMBUzSZ9g0-hKONiCXydI3J2qeH8vNKQuMRwQ9AV4hgHjx23hVDeKm-bMFOVw2kkqFDzItZb7Yh3FlRxRmr0iiKR0avibEIJ2jtGgHM2jX-YCTuRprKjaeJ_s9t92oHUX9vPgEQRy3ddFPACJKVsYBk4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
کارشناس صداوسیما: چین دیگه بهمون تصاویر ماهواره‌ای نمیده و بهمون گفته اول برید مشکلتون با آمریکا رو حل کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/107774" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107773">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‼️
💵
دلار به 271 تومن رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107773" target="_blank">📅 23:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107772">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91b6171a6.mp4?token=pAq4Gyxb1yZXULGldq6vMyqi2uCNa9abf37RAXHbeLAAevDi6UaGN5rkhAoOwi3MX7Gz5GQ9bt4LAbl7LmaaPK9hUAPYdjnZNu6VE7vdrznmW9eNIIhWuRIeX91uZ-4foilL7Ypei7a8CwYpxU6St2ds0wjX-d81jkMXyHhFheoKKU80WPWvDgMr_cTTS80UeLtX2utjV4gDhb1j1R9ERU0H4gumCmpm_ohxvlKXeXL442MYsVoxWHgCDmzcEY5TQknLKhQOjX4VxxDMxoWJH8TprqzZawBkjz4-Oz5aFhzjd2HwyQOuyCfxToxFvCJmMbMyb1BolodBe4o6LImFfj4x52TSn5jyu09r7FrewOvKwRdCBea_zAyOn5QfLpqT6rzDhXB0jgU_ndKBKfmMOxhZxOyWnMWWgSD1PoUYrIrNxLC2L4cEPRYYRknRIDW4Xq1avWRxXbHtCmUfBBapBGHe2dnMjJzLYWN8GhMIAnWFDAtLkFfBDnitYzbKVUoe0F-PMnXjkZKaOC-md0mko-8d_kzZKG-XWONoGmk5r_Oih7uxQo58MXjP6Pby9_Lp90gg30ppHE0xd7d9ouVFam3yQttFsQ_hg8RRmBzOZWbTwBM7MpUDz0_VDYGE_wSsRUp5ONS_LTDv1BA0TxNTxRcWN1HZ0Chg1xOoA9H5OOo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91b6171a6.mp4?token=pAq4Gyxb1yZXULGldq6vMyqi2uCNa9abf37RAXHbeLAAevDi6UaGN5rkhAoOwi3MX7Gz5GQ9bt4LAbl7LmaaPK9hUAPYdjnZNu6VE7vdrznmW9eNIIhWuRIeX91uZ-4foilL7Ypei7a8CwYpxU6St2ds0wjX-d81jkMXyHhFheoKKU80WPWvDgMr_cTTS80UeLtX2utjV4gDhb1j1R9ERU0H4gumCmpm_ohxvlKXeXL442MYsVoxWHgCDmzcEY5TQknLKhQOjX4VxxDMxoWJH8TprqzZawBkjz4-Oz5aFhzjd2HwyQOuyCfxToxFvCJmMbMyb1BolodBe4o6LImFfj4x52TSn5jyu09r7FrewOvKwRdCBea_zAyOn5QfLpqT6rzDhXB0jgU_ndKBKfmMOxhZxOyWnMWWgSD1PoUYrIrNxLC2L4cEPRYYRknRIDW4Xq1avWRxXbHtCmUfBBapBGHe2dnMjJzLYWN8GhMIAnWFDAtLkFfBDnitYzbKVUoe0F-PMnXjkZKaOC-md0mko-8d_kzZKG-XWONoGmk5r_Oih7uxQo58MXjP6Pby9_Lp90gg30ppHE0xd7d9ouVFam3yQttFsQ_hg8RRmBzOZWbTwBM7MpUDz0_VDYGE_wSsRUp5ONS_LTDv1BA0TxNTxRcWN1HZ0Chg1xOoA9H5OOo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
جواد خیابانی بعد چند ماه نمایش خداحافظی از تلویزیون امشب دوباره به شبکه‌ورزش برگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/107772" target="_blank">📅 23:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107771">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd54269d70.mp4?token=IWHn5itxgoTOH6Otenmx01N0JnFSsVEHG8G8zF_IX6Lhu5A746xnRj_I7fRlvvdgN98iTr5sqfOqFgb34d24txXWlE-Q4URWLXOl5ujx02Ifu-HrP5eIy3YpFwTmiCLDp2LPh3owgQopkRXmPAT9ehtQdYMXkaAjsp0axA7AOA_3FiUF8H-UdlFun7fLx90Pgl-5dZCxuyui6hfwPwWtRNBcSV-gev8dY4e5T-yB462_sZx-NfPyrCeD9ov8EJYhCuW6ff2volS_SyMRWSDlXrsoWxE8m8xQjJpeJZ7yo4uXamN86072dm3U-nwEB5Dhy4DZJ_al0GFc4u2X5etY5BtG4HFFRkSGDXbR9ioCCENkahUAW6qobC3yo9mDiT5xtxJ9MqgF4HE1bIpF33YZjTA-Ycq85lTt0qT6kgtduHcCznPQ1eCGi_jwQr4iyj5eN70LzoaTgrzRBK3xMveU4jTnZoMrJV3RHwLzare6DhNDCMlS0rAkTjo8Clz-Ma82UA3UvTQvj4X9UMQIn_bn4uTSVBMDj3Oof937ED1bdEHR4kZV8uC8X6tNwYy1q4NsafWt79EzfySxMSWWLCGeibSa_byrbxLgQ_dPiJjxWQY3GES1uEabvrDsOF4M-gv_-MCqcUNfSM4CY6Dd8gy-Iwqp6_DOcaIcwScNTZVQus8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd54269d70.mp4?token=IWHn5itxgoTOH6Otenmx01N0JnFSsVEHG8G8zF_IX6Lhu5A746xnRj_I7fRlvvdgN98iTr5sqfOqFgb34d24txXWlE-Q4URWLXOl5ujx02Ifu-HrP5eIy3YpFwTmiCLDp2LPh3owgQopkRXmPAT9ehtQdYMXkaAjsp0axA7AOA_3FiUF8H-UdlFun7fLx90Pgl-5dZCxuyui6hfwPwWtRNBcSV-gev8dY4e5T-yB462_sZx-NfPyrCeD9ov8EJYhCuW6ff2volS_SyMRWSDlXrsoWxE8m8xQjJpeJZ7yo4uXamN86072dm3U-nwEB5Dhy4DZJ_al0GFc4u2X5etY5BtG4HFFRkSGDXbR9ioCCENkahUAW6qobC3yo9mDiT5xtxJ9MqgF4HE1bIpF33YZjTA-Ycq85lTt0qT6kgtduHcCznPQ1eCGi_jwQr4iyj5eN70LzoaTgrzRBK3xMveU4jTnZoMrJV3RHwLzare6DhNDCMlS0rAkTjo8Clz-Ma82UA3UvTQvj4X9UMQIn_bn4uTSVBMDj3Oof937ED1bdEHR4kZV8uC8X6tNwYy1q4NsafWt79EzfySxMSWWLCGeibSa_byrbxLgQ_dPiJjxWQY3GES1uEabvrDsOF4M-gv_-MCqcUNfSM4CY6Dd8gy-Iwqp6_DOcaIcwScNTZVQus8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
هنوز چند روز مونده تا پدیده ال‌نینو وارد کشور بشه بعد وضعیت امروز عظیمیه کرج:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/107771" target="_blank">📅 23:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107770">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9943a67dd4.mp4?token=U3cF1srwiqONuavXtecqoUAkw2NmurPFLeQn0BquUVYGr38BF_ZTV1ZstDHEo8pld400abFdlTgJtPoMbO80heZpGbY4IM7etGjgRuCDgQ_aVidRe5NpqzmhTtQuVIBQ1_yeT4TJSJGxIjekQskl8baN9Q0zuwGhW-sNzDvm5asdhbGMZQ-mlZ__-a-wOeR_EcCmUX9mPip08OvQzfWf5edbWVLySU0Z8hiSnT7vBW5TaWZpHRI7_mLLk0qD1bdydZxD9bYW6dDTbi3lZPyDH3PHogQ3inonGUslvS0GSNrYT4lYa23DBBx_uaQftSYaXekr66NvDx0AzBYLno8GiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9943a67dd4.mp4?token=U3cF1srwiqONuavXtecqoUAkw2NmurPFLeQn0BquUVYGr38BF_ZTV1ZstDHEo8pld400abFdlTgJtPoMbO80heZpGbY4IM7etGjgRuCDgQ_aVidRe5NpqzmhTtQuVIBQ1_yeT4TJSJGxIjekQskl8baN9Q0zuwGhW-sNzDvm5asdhbGMZQ-mlZ__-a-wOeR_EcCmUX9mPip08OvQzfWf5edbWVLySU0Z8hiSnT7vBW5TaWZpHRI7_mLLk0qD1bdydZxD9bYW6dDTbi3lZPyDH3PHogQ3inonGUslvS0GSNrYT4lYa23DBBx_uaQftSYaXekr66NvDx0AzBYLno8GiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به جمهوری چک توسط رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107770" target="_blank">📅 22:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107769">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a73573624.mp4?token=bsUwj1YXuwNgxam8DTxfFfWak_PPMZqGcBtlPzaOnMnBWrgiM8fPaaNdgu-8SH66soak0gGvtqLPhSmge_p4Z8uvHPK3v9A8Rn-ZxXZKQA81nRMzFgJmz69deFxhkX403nFypJpVTAa0CFHATMzIUztlyuUQsC83w32vxIY34Q4qfy90KOa53RXtNl_irEVZIp1gDFV6t1jk1gK5hiFzv8l9-WfVVSVJybgOWe7ZY2yXFS0_M6g2P4Zi__Ric4mgrwGnWW5v65PKvhsRskqvhXa5WBTJXYSV-QNuB1wxPJmFQtNrbV1yN6BZaCTVdd57tQsTOiwE3aQThkVD_zt_ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a73573624.mp4?token=bsUwj1YXuwNgxam8DTxfFfWak_PPMZqGcBtlPzaOnMnBWrgiM8fPaaNdgu-8SH66soak0gGvtqLPhSmge_p4Z8uvHPK3v9A8Rn-ZxXZKQA81nRMzFgJmz69deFxhkX403nFypJpVTAa0CFHATMzIUztlyuUQsC83w32vxIY34Q4qfy90KOa53RXtNl_irEVZIp1gDFV6t1jk1gK5hiFzv8l9-WfVVSVJybgOWe7ZY2yXFS0_M6g2P4Zi__Ric4mgrwGnWW5v65PKvhsRskqvhXa5WBTJXYSV-QNuB1wxPJmFQtNrbV1yN6BZaCTVdd57tQsTOiwE3aQThkVD_zt_ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
گل اول اسپانیا به جمهوری چک توسط یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/107769" target="_blank">📅 22:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107768">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اشک شوق قهرمانی و معافیت از سربازی
بازیکنان تیم امید کره جنوبی چهارمین قهرمانی متوالی این کشور در بازی‌های آسیایی را رقم زدند و این قهرمانی برای بازیکنان کره به معنای معافیت از خدمت سربازی ۲ ساله بود تا این گونه اشک از چشمانشان جاری شود
البته لازم به ذکر است که همه بازیکنان این تیم همچنان ملزم به گذراندن دوره آموزشی هستند، مسیری که سون هیونگ مین هم قبلا طی کرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/107768" target="_blank">📅 21:52 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107767">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انگلیس هفتا به کرواسی زده
😐
😳</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107767" target="_blank">📅 21:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107766">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpDtR4REVYVAcp5L62r7H5Xh3xHBv0oUvYNWRJ922ZaR0ajup7IKmH_PIBGTE9Kjwy0fclt6tzHSSElFteWKXmUhZmVf0xaqclDMeW3jspJDAnGgE0carxshV0F48idlLwfCjG89H_mklwsldZpBve5xywxayw0VzIoofiUJjh1MBjbUf4Q7P0r3t3qaKwPntjXCw1S1GsD_PloUbrhpgWFc6YtdYxUhjksI0LXMYCEK5Nqxrg9BuNf2nWXZoNNGefRQrwK4tcDMyfNUsAB9MYUcgEliqco_HBWvr5cOyqrTvwvlOKfrIEZGgsFf2ieYJ-g9G4__W3G4DLyCOKnKyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترکیب تیم‌ملی اسپانیا مقابل جمهوری چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/107766" target="_blank">📅 20:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107765">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APt4nYqQb3J4z0gs0b_ezhRDpy-csAmXA2I2x4BI69k43FUuAvGU6unXEjG90FmpY03LXxw2cvwr_Lpx8xaWijs70ItOI92h2CzLF0GiWAMBSK0ng7qo-ycpK4iOYt4zUfOmnWwS-efRHLlfb6YCxsT1aeiu7ZcB0mab-HpdTPxTrhzydSYbAx1P_YhZnZ59jGXVXBwhalJ8CcrUKEnkVgNz6wgt_yuBqyTZc9qIdvYfqT8EYLc2mIjg-1DdS9pbnJyph8xUjYeKgRJiALSZab3MUMqvYubRpwsuu7u0t3a_UhyIMmPAfKflKusspJhQwcQ--walqUpDi2Y_Wiwfsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🇧🇷
در سال ۲۰۲۲ رافینیا از لحاظ تعداد گل های زده شده در مقایسه وینیسیوس بسیار عقب تر بود اما او امروز توانسته دو گل بیشتر از وینیسیوس به ثمر برساند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/107765" target="_blank">📅 20:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107764">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZ1a4ri8ebdsYayTaW4JKkqR3EcK8y9TSczutdAbgylvbEt4si0Tvcvkh40wAiLomGyu3WvQw5X_AxsTZ7i4PCgcvyQSYibwhOfp7vqi6SPUFzD4esFFCmt-ssJ4dQdRmYe90thRKE1tTviZjeytuXts_yg8NDUn8Zo66rJX_Odsbr5XTNO-jya-ZrZbab2TmnRoaaUws8MVFUqvMyAIcGs1v1TbqikG6CyRCCEYLTpAck4STGvSt9NB1h-cOmoyyvrmjkRSNZjQ33P7SMPY-BRcKZEQ8PmClKzsxL4nt8HHNsQVGUzuMQ2OH-FHJsu_A3DK3Nz5Bf-zhN0XbbhsjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
ویرجیل فن‌دایک در سال ٢٠٢۶ به اندازه کریستیانو رونالدو گل ملی بثمر رسانده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107764" target="_blank">📅 19:30 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107763">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KW6ZcbDCB_SWcSCUuuUAhdkPoiNHljaQEuAz1gLt8oieu_MRiJQqLuT374kDYzJCdM91BDeTisiWAXIi0oKlHOKjPYJfPT8XDLRPsYqVwUDvukN27NIVenbtBosVIKVHGypHdUlaw9C7AMyeyh-05-ZbfoS-jfE33OSdGXg425tVbLc3qQ0ANM_Y8i6b0x2ZMYPa4t6wMnJw71ukW2_6mzZlcQ8294SYkfMbKFUfhgWlUEBIfvOhN09vuGkvaMW3UiIVVY5e7eqDXYcaG90MP8WHh619ezoIn4QxtQd__4UAlq_v7Vppx9VJRrE2X9Cl4G10NxkpXCKdb0H6QVTB3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
روبرت لواندوفسکی پس از هت‌تریک برای تیم ملی لهستان در بازی امشب، شادی گل معروف لامین یامال کنار پرچم کرنر را تکرار کرد
🥹
🚩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107763" target="_blank">📅 19:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107762">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f408d58b0b.mp4?token=U9_GTeCdoZMJsblq0rjhtmLAfwQSQtJ5vHjs0Pip_JMKwtgQEmZwfs9ROmMlVygPiKOXCYQIs9IyYSWeL0CI8kyJkAH98v9X1wKN2dQBZ-k0baZS6nLYnWM--duTnOWMVXm2225g6sRcfZ-HpxHOmYZXO1BWzuSyhurHfW1Wqp3uNKh7mRB_Lq9NuFlFMZP_yA3uvo0rM8slab6yayBGJh4CKTR6edp9HlJCsYa2JvUT2vv48tc54dj3LENi10QKO76ubu6vI5rqBCZSGj6iZNrDWKMc0U4es-YGQtw4tqAZ72U9tBVeo86POFuD_f0adeLrclxss0gIOk_TvnAtSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f408d58b0b.mp4?token=U9_GTeCdoZMJsblq0rjhtmLAfwQSQtJ5vHjs0Pip_JMKwtgQEmZwfs9ROmMlVygPiKOXCYQIs9IyYSWeL0CI8kyJkAH98v9X1wKN2dQBZ-k0baZS6nLYnWM--duTnOWMVXm2225g6sRcfZ-HpxHOmYZXO1BWzuSyhurHfW1Wqp3uNKh7mRB_Lq9NuFlFMZP_yA3uvo0rM8slab6yayBGJh4CKTR6edp9HlJCsYa2JvUT2vv48tc54dj3LENi10QKO76ubu6vI5rqBCZSGj6iZNrDWKMc0U4es-YGQtw4tqAZ72U9tBVeo86POFuD_f0adeLrclxss0gIOk_TvnAtSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
ترو خدا هوش مصنوعی رو از ایرانیا جدا کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107762" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107761">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtsknTC3ctPjzn1r93BhqRKNqwIXBsEjbImnghUVTR6OJ3TPY8nb05eGUwuBiDRp8u4O06u_UuzCdWNc4qbrQPEB03A1JgCk9JsKQMuLXf7an2fc0YwlpSAHHWZ7U7_BYEwPwFdWWCc3BinIkOnWxrHqQEC8O4gCVQDxND7FBfZsUwLUVXgkPyIJNkqp3fI2YVUUtX8bd9RRg3iAXniXtAzT8NZhswSexx9uphmI07nHR7aSrsw9SWbAoCQHFm6Ai9v_Z-wV3_YXJJQU9XitQkqdtxxQ_ZQdROUba2NsIaDRujZrRdFTj5rhamkVwVeTV464skpSyCOs1BKqwWq2ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇭🇷
ترکیب انگلیس و کرواسی؛ ساعت ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107761" target="_blank">📅 18:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107760">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58fe91d1ea.mp4?token=aToqmQ_ssolyBfqD37z1PiZE9XzLll_r4lRvbDb46EEjv3Sq-cNB4TvSStRi5oBRYtonG5rtPB4slxCsbuJ5rBz9vy29jS29jdt7GGu45UVK6T9syD0V07YI6WEHgxarsX45M2fpwB7vFAbZ0vOCRReANta5bm6joLiltByvjN7wOCXHnLtFwDX2zwipiCY4G8YvEGJaygdsb5HjsmkGlWa3npywi3cX0XRLl9ZVnZ0kEasjeZg2In1k5UTYQEx-5H5xN2awxS28gnB9ZKIuU9UnAtSJUxf1GUesVOaAq1e7mGdTPawbuI4hXnDVR9M1rxxLe28HRdxMp8d7tBu3NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58fe91d1ea.mp4?token=aToqmQ_ssolyBfqD37z1PiZE9XzLll_r4lRvbDb46EEjv3Sq-cNB4TvSStRi5oBRYtonG5rtPB4slxCsbuJ5rBz9vy29jS29jdt7GGu45UVK6T9syD0V07YI6WEHgxarsX45M2fpwB7vFAbZ0vOCRReANta5bm6joLiltByvjN7wOCXHnLtFwDX2zwipiCY4G8YvEGJaygdsb5HjsmkGlWa3npywi3cX0XRLl9ZVnZ0kEasjeZg2In1k5UTYQEx-5H5xN2awxS28gnB9ZKIuU9UnAtSJUxf1GUesVOaAq1e7mGdTPawbuI4hXnDVR9M1rxxLe28HRdxMp8d7tBu3NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚪️
احسان حاج‌صفی: سعید الهویی، هومن افاضلی و رحمان رضایی جزو بهترین‌ها هستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107760" target="_blank">📅 18:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107759">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
‼️
کنفدراسیون فوتبال آسیا برای فصل آینده مسابقات تنها ورزشگاه‌هایی را قابل استفاده می‌داند که دارای سقف استاندارد باشند و بدین ترتیب تقریبا هیچکدام از ورزشگاه‌های ایرانی شرایط میزبانی از رقابت‌های آسیایی را ندارند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107759" target="_blank">📅 17:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107758">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjyWesUi7XS4MqzOBiaeoALOPTKqTY0iDmzGj7llOL5qR58wmDVL6xMCJ9fteP1RgdlMBPdvaXV4G7J5QJAZdibVvPy6oGskJnRCMUbp6i3LeFS4tqfOGG_0GLmHqNDPNxVEcs7YeF6D6qF6lysfzxWRIGaCycAgQzVhTIxiWh7XKVQpUbrHHAVmM9cijP9Xk68VA3manluo7vMaOQZ3V0UMZT_KIwwGmSVQLzy27pm-9Vvzl003iZ0VrOz1JYLQ8YaIFd8ZBCGM8qHrufPdc65jrSt4N_L5DoeMJG5kDj-A6WXLwGUXRIYfHbkNg5O2BzFYWJq_ZgKY7NdiFWmULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💵
دلار به 271 تومن رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107758" target="_blank">📅 17:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107757">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd85597f0.mp4?token=fiIiAs9SQAu-2FTpHqP2Gnh5sBScrgOHl4fMy4h6XqN0tobGWfNrQX6sHKt-XHV5rX3AQmM35di-8_xTTQjFtMNvVS6BHUTKsel2B1DCWj1O1tnFLV-VeIqXRklM6u__-65DCYat7Ma2GalsBPjShm9t7uPdj_P6GdqLJWnuHFCU_K06i9sXgs8PkbcNXirxxLKXPonubQn5SRlcq3z7BEBb0FEOM6vpRwysxy9cYsr2ji-NifKDfW-qZA2n7smFgafq1Oq6wnhs_dvnliHNnDLKmCGEeu2TwpuBqmxd9YRTodk1qVFUk2z23qu_UlhGbeItZopfLfYGeGy99XSx-r8R4ziIZMlfaslxJ7bRqH1ZMUG3cf7yoVw0nq8VwTTNOzXSqyZQkX9OBlIsdavMDzpubi4bth0nfQtQimNy8lqIey2gQ0j8ca2IImH90zBwqe_Q_5DNv0PEidWaQVTgeowIzAXskwNkYWQ8vWPD0b_B_GhD_GRhz7PGZCeozf_j0cn_7hoysYZHEJ6UkF_H2xrHdUj5IWHLGsA-1Wf6IMD1GUPDUSj2Gy2HXByHMzrXAPpzHoI-VbkOu8ZkMKvVA5-quv3zGrGtIYlsrFYMug059oaiuZh9Sb4HhBuVlhfSemAe7zWPmGed4ZxS6_3gMsYlh_YYAbJzECtpGHx1i5M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd85597f0.mp4?token=fiIiAs9SQAu-2FTpHqP2Gnh5sBScrgOHl4fMy4h6XqN0tobGWfNrQX6sHKt-XHV5rX3AQmM35di-8_xTTQjFtMNvVS6BHUTKsel2B1DCWj1O1tnFLV-VeIqXRklM6u__-65DCYat7Ma2GalsBPjShm9t7uPdj_P6GdqLJWnuHFCU_K06i9sXgs8PkbcNXirxxLKXPonubQn5SRlcq3z7BEBb0FEOM6vpRwysxy9cYsr2ji-NifKDfW-qZA2n7smFgafq1Oq6wnhs_dvnliHNnDLKmCGEeu2TwpuBqmxd9YRTodk1qVFUk2z23qu_UlhGbeItZopfLfYGeGy99XSx-r8R4ziIZMlfaslxJ7bRqH1ZMUG3cf7yoVw0nq8VwTTNOzXSqyZQkX9OBlIsdavMDzpubi4bth0nfQtQimNy8lqIey2gQ0j8ca2IImH90zBwqe_Q_5DNv0PEidWaQVTgeowIzAXskwNkYWQ8vWPD0b_B_GhD_GRhz7PGZCeozf_j0cn_7hoysYZHEJ6UkF_H2xrHdUj5IWHLGsA-1Wf6IMD1GUPDUSj2Gy2HXByHMzrXAPpzHoI-VbkOu8ZkMKvVA5-quv3zGrGtIYlsrFYMug059oaiuZh9Sb4HhBuVlhfSemAe7zWPmGed4ZxS6_3gMsYlh_YYAbJzECtpGHx1i5M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
گریه‌های بی پایان بازیکن سابق استقلال در شب دستگیری در کلانتری دماوند!
❌
خاطره بامزه بابک مرادی از دستگیری بازیکنان استقلال در شب سالگرد ازدواج مهدی قائدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107757" target="_blank">📅 17:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107754">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967556808b.mp4?token=paV2cmW7ZJfECL2KZvYM48ifTenQ7q56gi3kCSB1lFVVQa04ALVdtnGasawANmAuBbLlGsnDoQ2c2OiRwQy0j7Zv43Mmgytw_xYQObLhDqZspg5ALcx6UfHMoCpBbcuwtCfA2BE3z6M_Yh1thooVJ_Mj1BQb-cUOS7TybYkuW9UEitXkbWFqb1GjUgbOkU8XmZzM8qgt0joEl3AhJCV2TSr8CbWP7GJ2i-ku5kiD43ZvqQCqyW8xNHTMfdA-DUh1ZHb0O2OqQ-0uYS1-cw29tlNwa2naWcLEcAFS3fng6wKxggKtwVlAEvyWny0Bff_PF9xdVw-1VdAIm6_rsW73bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967556808b.mp4?token=paV2cmW7ZJfECL2KZvYM48ifTenQ7q56gi3kCSB1lFVVQa04ALVdtnGasawANmAuBbLlGsnDoQ2c2OiRwQy0j7Zv43Mmgytw_xYQObLhDqZspg5ALcx6UfHMoCpBbcuwtCfA2BE3z6M_Yh1thooVJ_Mj1BQb-cUOS7TybYkuW9UEitXkbWFqb1GjUgbOkU8XmZzM8qgt0joEl3AhJCV2TSr8CbWP7GJ2i-ku5kiD43ZvqQCqyW8xNHTMfdA-DUh1ZHb0O2OqQ-0uYS1-cw29tlNwa2naWcLEcAFS3fng6wKxggKtwVlAEvyWny0Bff_PF9xdVw-1VdAIm6_rsW73bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
و بشنوید از مدل ماشین دروازه‌بان اصلی و معروف تیم‌ملی اسپانیا یعنی اونای سیمون
👀
🚘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107754" target="_blank">📅 16:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107753">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b23bb5ad12.mp4?token=awh3oi56bxzrBnRQZrZ6DLXUmESsPVyApKZwwYKagcIm0mxNQNT9Zwb4yXtHhh57YA-IAxTMGNnzJdauLyBk46Efq_MC7TZsnwOL_MHvR_OOUSetkhUGIBpelZY3RoNKwO08gh40M8_-ZufSiA94ytEI2X0bGa2246RQ8ez_TuUEyqvWKD1jw-R0vbxs4Xcd8H22L0WmhAPBKNv5ULdRMCcRNAQhNfF4vIIe_XYcd345wRHfw75PoX_3UIt8P-oTeKPxu5daynAqLRmuIgOtoO4HyF-49Hjl13sgK1_GEiFj77EJuIpKtsRQ9Awo0--MMJmFQ-TRHvjPd4kqvbcYp4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b23bb5ad12.mp4?token=awh3oi56bxzrBnRQZrZ6DLXUmESsPVyApKZwwYKagcIm0mxNQNT9Zwb4yXtHhh57YA-IAxTMGNnzJdauLyBk46Efq_MC7TZsnwOL_MHvR_OOUSetkhUGIBpelZY3RoNKwO08gh40M8_-ZufSiA94ytEI2X0bGa2246RQ8ez_TuUEyqvWKD1jw-R0vbxs4Xcd8H22L0WmhAPBKNv5ULdRMCcRNAQhNfF4vIIe_XYcd345wRHfw75PoX_3UIt8P-oTeKPxu5daynAqLRmuIgOtoO4HyF-49Hjl13sgK1_GEiFj77EJuIpKtsRQ9Awo0--MMJmFQ-TRHvjPd4kqvbcYp4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
ویدیو کاربردی از نحوه جدید سوخت‌گیری که به تدریج در کل کشور اجرا خواهد شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107753" target="_blank">📅 16:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107752">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b48e9e7f4b.mp4?token=EHH2o3HZGP3P77ktNRZbzKsJSGlvZmPT12eaoVLcvQxPKiYo9dSFsRw_5CJQvfeQrP_itcY2tJ3rAc1PJZ9AlXEOSAVkt7DIxuFvhaCRhW_5T1a2zv10UxWXULlKFdufSExipQFYNGI67IvJmq7hVoe-UujBZ5ZLrualE2u-p1q9h1pcaZDlOaB4guxPvX7_wZgGge59JZJu40KCMlW6yI3Km2-iwb2cwIjPFTVVaLhg8HRfMdeBMtagJ2fowOsHRZY-KpKMW0US2LMjouNQays-eWFKSppRU7b0aqEDnvbRPeq3BO_99rC2Kt3-s_Jdd74NuJ_f9e0CzY0Tf-aS8y460UpyiT6BQLtv_mWKG5e62A-4cUkaGLCyORUx-lf9GVIKoXi5imPFLVbCDNuE65mc0E7G36dq-YEs_fNERLGf2eAhdBYi07mYMNSzU723wsVj4r8qtLCSfhzzMEu7l85zPQt1oSak02Ywweem_kLjjpENw0qDKtB6ZVZljdy0CqHBaSyudml0zs0LotxwFXLMb6egtW9PmkfR_vnJgJt0oHUiUeCSEIDY-TbRjT9YHyL0RPaRAIxOfSwMeY3ejmI-oxtqnUmlZwhPG3Bqlgyg7KKzcmyHEb_EEgeyt5q06oEQi-4njpdPcnwIs88l9mO0H08CnxWp7MqYRMvcVFE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b48e9e7f4b.mp4?token=EHH2o3HZGP3P77ktNRZbzKsJSGlvZmPT12eaoVLcvQxPKiYo9dSFsRw_5CJQvfeQrP_itcY2tJ3rAc1PJZ9AlXEOSAVkt7DIxuFvhaCRhW_5T1a2zv10UxWXULlKFdufSExipQFYNGI67IvJmq7hVoe-UujBZ5ZLrualE2u-p1q9h1pcaZDlOaB4guxPvX7_wZgGge59JZJu40KCMlW6yI3Km2-iwb2cwIjPFTVVaLhg8HRfMdeBMtagJ2fowOsHRZY-KpKMW0US2LMjouNQays-eWFKSppRU7b0aqEDnvbRPeq3BO_99rC2Kt3-s_Jdd74NuJ_f9e0CzY0Tf-aS8y460UpyiT6BQLtv_mWKG5e62A-4cUkaGLCyORUx-lf9GVIKoXi5imPFLVbCDNuE65mc0E7G36dq-YEs_fNERLGf2eAhdBYi07mYMNSzU723wsVj4r8qtLCSfhzzMEu7l85zPQt1oSak02Ywweem_kLjjpENw0qDKtB6ZVZljdy0CqHBaSyudml0zs0LotxwFXLMb6egtW9PmkfR_vnJgJt0oHUiUeCSEIDY-TbRjT9YHyL0RPaRAIxOfSwMeY3ejmI-oxtqnUmlZwhPG3Bqlgyg7KKzcmyHEb_EEgeyt5q06oEQi-4njpdPcnwIs88l9mO0H08CnxWp7MqYRMvcVFE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجب دوران‌کودکی جذابی رو‌ پشت‌سر گذاشتیم...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107752" target="_blank">📅 16:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107751">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9d2f3d6a6.mp4?token=MsCALjrDfIS9PxRwUCZew3C3xFsOSmWDxYKYYjnUDldT8xxK2LCcSAOKvHPYD98JoAui1BzGyXbApZEG2TOU5M7nzmgxpaiEtmkdozancPGmQTP5vCrHj9WzSCDfZaiMwPoagZMUXIjPhL_nDcyDCp-yT4vaDG5EMjR1fLdXMP2paHTlYAj3FYHPWQhkDzSY2xsL8bu9Ke7OtL9wUz0TWAGDnJiV4oLhwKyXAhZHFaE4EO9cUnQPBdRs18MZVNa9S-QCJNd8VztmHUQ6BzZHK2W69SXLmmFpEQZ3J5ldj9yIfM7GvCh9z8E6OZrINSAwD-7xiDU0oM_L33JjInAumA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9d2f3d6a6.mp4?token=MsCALjrDfIS9PxRwUCZew3C3xFsOSmWDxYKYYjnUDldT8xxK2LCcSAOKvHPYD98JoAui1BzGyXbApZEG2TOU5M7nzmgxpaiEtmkdozancPGmQTP5vCrHj9WzSCDfZaiMwPoagZMUXIjPhL_nDcyDCp-yT4vaDG5EMjR1fLdXMP2paHTlYAj3FYHPWQhkDzSY2xsL8bu9Ke7OtL9wUz0TWAGDnJiV4oLhwKyXAhZHFaE4EO9cUnQPBdRs18MZVNa9S-QCJNd8VztmHUQ6BzZHK2W69SXLmmFpEQZ3J5ldj9yIfM7GvCh9z8E6OZrINSAwD-7xiDU0oM_L33JjInAumA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚪️
بازنده‌های پر سروصدا یعنی اعضای تیم‌ملی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107751" target="_blank">📅 15:40 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
