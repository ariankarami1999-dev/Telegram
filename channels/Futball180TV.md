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
<img src="https://cdn5.telesco.pe/file/l9Ok3GDC1DKY2enHntFJFNcOH_b8T7gktxg69k9FgjctNIlr6-kkfK_MUQREOZU1RMSxLi6V9BcBdldG3vKrxMc0PSSYSWPwTlC79eRM46_6xLhZGzmhYA5CCFJVdIxV00uV5-SF2lFKKTgfsbxpYQnslJZfXWZS_xWtQesJVM3iQATWgOH1QujRmMQu3Nllil-c-CLD3426uVDwN5kEfwRA7oDNJv-Po8PxJNn4ZVNwry4KbwWpZ45B2Ta1DPk0GI16Ti47j5JnbhfsvFwJANQNqbJS7m86DDwZldqLt3nhXgyObQ3CqpUGaH7VCAIFDRrA3EOb0JaXYEFUKr8I2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 650K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 02:47:14</div>
<hr>

<div class="tg-post" id="msg-94085">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzhFZ2KvQtvpMlx2SZZwirCD-Q4F8tGtT8tr1KGdLpa7_qS-1LJtH2T05fe6gh27MDGXSnmXszGRNo5wZIDmxPRJW2c5yHYfQfxeCGpwPMVvh7UpAlscEGWjOBqTYffycEYVwKMA4TQvLyOI4UAdoFbVqd3CjUXE7a7MXrXvJbl68djV3_3OdzVzaj-IYNZYfqlo2udMqoBak2-PkHYswRzVfViZ9U5yiqS1dJdfagTBslG7ATbZomQ-4R7e3fs5oh76XxDXmHoh7guB3tFsFv0bPi8tf7j44ts-FjiadZIS6TXVT9hRebC4xVVVgVYMsfb4sBArUIfVA9NoaRpMjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
طرف حدود 800 هزار دلار روی عدم برد غنا تو بازی امشب بت زده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/94085" target="_blank">📅 02:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94084">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بریم برا بازی تیم کیروش و رفقا</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/94084" target="_blank">📅 02:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94083">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f241bddbcf.mp4?token=Rq6ijluDOXVmbT-seCxNPR8EffIzt8Aw5n5v3Ewr8E1I_gebqwpFNSz5hCT2ld2iWYrqTMCL-sFoIWxQTsaNW6G6ORqLoHQhO8iDNbkU_EhsGTq6ww_Xk8-yDJrYgp0YXD6SK2xKCVH-IR0EBzkTXDexrSFo3qrE5qqVZIB-Aswzkm4ywI3_00k3xGRwsnNLqstnrjhPsPZVCdenfD0NIvUkshz-Orf09QSt3yPocUpzx3ZWOs1nQxwmVN_hGSu7jJ9FLpIlY5gyp0N4GkOilBtLbVEESjX3_EFpqQSYc4XXCQhiS3zrg0S0NekayzXxCEHDMXBLxKaeIQSBSJ3zSXbKYI5e8yxlgB8GeNWJtneuoNK0cDYqlcr28O9AW45uBnCqckjUpuAneE-Beu6YCjeNOfpuNt4aPQpYSDAsWXWtQNP1Ujy-rPMxGSyMjTyBwwNZnS69egD_qzpb7h-X2o8jV0h4yCcf7NAqo8PEd78Nq2pkfwyUPHyCKvv7oglrePWsRH5ha2_LQLcE7-M-gsXCHVqK4V9wPnC38UNNj1GqIj2facQ-2eY8ADQKqas6F42BBgECQlUnoSijECEsZkgodwSTA9Yg5lMikD27dGMUkjnefdrEhu5NrXKpRCUsB2VYAAYLCtZalVTwdjx2xbn-bp4x-PA7ytKVTz_cDjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f241bddbcf.mp4?token=Rq6ijluDOXVmbT-seCxNPR8EffIzt8Aw5n5v3Ewr8E1I_gebqwpFNSz5hCT2ld2iWYrqTMCL-sFoIWxQTsaNW6G6ORqLoHQhO8iDNbkU_EhsGTq6ww_Xk8-yDJrYgp0YXD6SK2xKCVH-IR0EBzkTXDexrSFo3qrE5qqVZIB-Aswzkm4ywI3_00k3xGRwsnNLqstnrjhPsPZVCdenfD0NIvUkshz-Orf09QSt3yPocUpzx3ZWOs1nQxwmVN_hGSu7jJ9FLpIlY5gyp0N4GkOilBtLbVEESjX3_EFpqQSYc4XXCQhiS3zrg0S0NekayzXxCEHDMXBLxKaeIQSBSJ3zSXbKYI5e8yxlgB8GeNWJtneuoNK0cDYqlcr28O9AW45uBnCqckjUpuAneE-Beu6YCjeNOfpuNt4aPQpYSDAsWXWtQNP1Ujy-rPMxGSyMjTyBwwNZnS69egD_qzpb7h-X2o8jV0h4yCcf7NAqo8PEd78Nq2pkfwyUPHyCKvv7oglrePWsRH5ha2_LQLcE7-M-gsXCHVqK4V9wPnC38UNNj1GqIj2facQ-2eY8ADQKqas6F42BBgECQlUnoSijECEsZkgodwSTA9Yg5lMikD27dGMUkjnefdrEhu5NrXKpRCUsB2VYAAYLCtZalVTwdjx2xbn-bp4x-PA7ytKVTz_cDjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
اینوووو اگه نبینید امشبتون به فنا میره. خیابانی یه کسشری گفت که مغز خداداد به گوه خوردن افتاد
😂
😂
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/Futball180TV/94083" target="_blank">📅 02:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94082">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc078c31b9.mp4?token=uInIQuNNy5mFLCijEUbEvzMR96HXGYYOMfvCXU4pdCvf5Q6aofKcRQiTQqAVFA5CR4NXx_kT2xuihNmz2EJ17r6rDULAcFwWYY19MWskfI73IwOPA08pJq2VvKG-0XDukBtDrTYZ-JYHaK3ZDPsG-FEtNRYV8luFxUM5wUUhIHcXGWyca6XBYGLFzNCbBbYkr5HYWy3VLs3-QVXtTqQrqpZ3rk3zEy3oKKArvTt3ONP0cqH6ln0pxrFzsWwDSu3oADhv7MchpklvrQ-qbBM-URHMfL7GEldI_9HBZyZ8jF8na2naFSjE6bWdZeD_RGG754HWTmZ6N7woeisbGzIk_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc078c31b9.mp4?token=uInIQuNNy5mFLCijEUbEvzMR96HXGYYOMfvCXU4pdCvf5Q6aofKcRQiTQqAVFA5CR4NXx_kT2xuihNmz2EJ17r6rDULAcFwWYY19MWskfI73IwOPA08pJq2VvKG-0XDukBtDrTYZ-JYHaK3ZDPsG-FEtNRYV8luFxUM5wUUhIHcXGWyca6XBYGLFzNCbBbYkr5HYWy3VLs3-QVXtTqQrqpZ3rk3zEy3oKKArvTt3ONP0cqH6ln0pxrFzsWwDSu3oADhv7MchpklvrQ-qbBM-URHMfL7GEldI_9HBZyZ8jF8na2naFSjE6bWdZeD_RGG754HWTmZ6N7woeisbGzIk_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
فیروز کریمی خطاب به بیرانوند: این چیزی که ما دیدیم خیلی هم تنگ نبود
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/94082" target="_blank">📅 02:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94080">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hdR9XZrE1LK7gAjWGR3T10fOzJTVKwOlSYP4gn4WkwabDw_VPqGTq1BQxInkolxwocJ9bU4Aezi4ZUyyKHSZ83eRYWw5gx4Px1ZkUITSrryqYC9a7jWohk9TFkbdVwzrhM5U5kZo7vM5LcdVpenIsYOK-Q_5WAJDtpgpwCMDVeVD0V8Ga1K9SRGw59qrH6VRYdB0a3bmo0Z3kDUzed_hN-WuPEuBviAoEk77u7FZ4Or1POhhU5rPE4IlAhG0an6ppyKIYXXjhAS5m5xOw10az63AZVwxvKumUZnNfRGRm5X1rIygzO6LSd9_pYTH1mehvpnRbyzJ6rbgcF29u9RHxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NwZ8RTUV30hUGQgQQU3_dPPPp9Qf1VErbEcNcQn2Us85K99oxSTHCXqn1dmvT_GHzRVgG9e31TkG0gKbGzGkUD7WYbl2annxeN5zyf-T4giYkreFDnUOUDLK5VamxtTA4WINJcqrg7NoDYr1xrxOh9esU39XI0EvHV-UN9AWa2uVjZuB7GGMgf0ZN2lTSj1pS6zgAtnILXMv_8FAAmHkCKWb6h3RRmxOVw0wayyE01AUCJfZ3XuUgzIpILO0PNPeROk_iQXCL-nm4IXPTMLOPyiKltS5lMTa0g-3xNxkqTAOdq9EtwFkdH7NL0AHXtmy3a34-LWN2zygunkZoH5izg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو با ریدمان امشبش قشنگ خوراک میم یه عده رو جور کرد
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/94080" target="_blank">📅 02:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94079">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP7aSWWwif9WE59vhTpraQY3-cEraT0m3cGtRCQ6zXfZiErJi865JZcKO90ZJpIgk5b7WX8iyrH6OWYWUXRTwr192t4nE_E40y2fuAf_G9u1_6NaWAO6XjylnWmCF_ABKVbZlHoBa-_77oMdqLyApkM4HkBW-FUjoSdziM-qCDeRU1jQ1GrVFWGLqt_Ru-5WXiHO1FUvGCvn-0q0tNfbv0yl55awGbt544MeCDh0jSAAEGBcLFVA8VCSbSoIb8JDyA3oUv82VHzb1WFtQOGChtwlz8USHEFsC2-KOre76p44H5_ldVjdN2mTNzjQjtVu1kMU014-2KT-BpSWfBNh-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فوریییییییی از رومانو؛ ویکتور مونیوز به لیورپول پیوست.
⚪️
20 میلیون یورو از این انتقال به رئال مادرید میرسه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/94079" target="_blank">📅 02:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94078">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3VHgC_wpAXIZDmUbiMscCIm1x7UWB8yxFrnNw_65fWE6hxnPW8r4J8zO8QTr9Eqo3bmwvpblPagKnMUO76jmT_hKNUSXRV3_wP96h45qPf5l8Rg2oYzPtOA5cK74zEkWmlr57g0Y1mEa7ezbHPAAu7oLDqqkehmGTjKLHSHhPJG1IUymMhHDtFvYwqfvOt8sUPagFjYFFkev11uhVZJSXwJmxXp7iQPixeP2-G9R-sdGPyEJ4IlQDYP9j7hg5Xfbklu2XLU6k9QYp5zeQn5-fP1YyX2u4FMLyW5lzRE1fN4_93mfxM9rsCol32SwRnoxXZD4jAELrANpuQZn7YE8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
دقیقه 94 و درحالیکه انگلیس 4-2 مقابل کرواسی پیروز شده بود هری‌کین به این شکل خودشو جلوی شوت گواردیول پرتاب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/94078" target="_blank">📅 02:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94077">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJcBJMc_7HrQ-IC6lxcMJnNYoyvrfPr3er7qDySkCTnnR4CO7PImGxKS-xLrRWHGy15ENo5w3sGxVTgWrgkFp66XUHax5x6C1-59ER1UhxuVVPfduGbizBP4jg6H9QR7jXrLdXylfR9tEn1nxO4SdQau2yDUjlJBqex6HirCk9Y2QbC4SrMnC0r91oNWClJL_mPrLwQWjDl9osXleRJvVu3rLfGlTTIeSX00An24B0q93mx9mrsutss27SOkWL4iWNs12ZhiIdTU8BFr_56f8Odp8g06wN8ChWtOTBb063RUMq7gv2IYxwIuJQTvTawYAV7oItFpXyz0qr5RNkBmWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
انگلیس برای اولین‌بار در تاریخ در سه جام‌جهانی مختلف بازی افتتاحیه برنده شد
🇹🇳
2-1 تونس (2018)
🇮🇷
6-2 إيران (2022)
🇭🇷
4-2 کرواسی (2026)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/94077" target="_blank">📅 01:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94076">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfvfqByXRglEK5IJ0z6QDRdemRucmWceTjZUzM58TWTdax5Q_7trhfGCJiERciu-PkjSLvqPg-pMrNFBByqB-hpomkRO5XxG8jtgQQRPtPg67ebL24Ec3vqJA4iYI32piG-oFCAz9JAs8l9IOMSNZgvUmwWHREWidQUxH7on-jCYN9D3WG6m1zC4p0Ns6hezpsxp4DBOhZY_lKHX059QN0YBKZNI9CQqKjUffuflxd_LRjHkWiEyktqNtscvQDZ2nXdnalfPCJIp7yLOS6LmYAxvLJkJqgivlkREUuzj1v25wbkaUMR7guMs4kV9ZKU280OjQTCcEHTyLNNEOSo0mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه یه وقت فکر کردی کصخلی به این فکر کن که بارسلونا بند 30 میلیون یورویی رشفورد رو فعال نکرد و به جاش 80 میلیون یورو برای گوردون خرج کرد
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/94076" target="_blank">📅 01:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94074">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fd5R9rJzLRK4PJoEZqviFSD2NC_t4YE8CYaZpHSMPyM_-_74o4K0dnkndTMp-GmTqj-wMgbKiNR8uqdnIOkWRuKVF-jqMxCbRCgS42lC8lJKMuGRxLIiRh1MrVOvFRRLpryaw9uir5Yy7C8lWUvgQfzDu8Xo_Fl7DnRPX-dlYjndfP1p4NWZgW4lXlezYWeggVWPZwdoflLNG9OnlsJzgGiZfoM4Wu4HYV8peYond2SzMyMvTWANLAhM9URvUn8EBCvJG3SMepiG4lW2fJ3f7-X1CdSEjR39bEDYZzgGRvxebxe_yrDHxeEyS1vfkvPDa_dXM1Al4Dy7dKc281SyLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/elYaOu4sqb4FyN2YUFeX453AyowOQiSc8iijhLFYC9qV_EbmJr6pUQWy4L6w2veypIIjKFidGODjD6uz3NNonT97N6TqqLxbaXx313c5a9hgtUHhN-ypoqs7QpvkkD0hyk1ARWDP3O0VMJDMXZ571H99RjlS-VdPgDF54m0OWQM3vLUeVSRyFjIFHp-sexJ5LtRKj6WJNwZXupO0iXXopcGkKdnMy_L07HSgMs_Ge7oECTMW1LJWqeTXkm0mvhB4TwmU-wJqDjCUR-elAJuN-n1uQaVK5b9XAZ_Kdgjku0XpkCD7T-DHcQ0H7b_mIuMd9lo1AIr03FPdy5iogPh3WA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">داور VAR بازی انگلیس - کرواسی هستن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/94074" target="_blank">📅 01:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94073">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q70DFNdi8WW6DLlolVevkFgZf-S1BWU03_Lo_6h4mxm-laX_EUg5h01NNrHkCbJmR7Zha0JIFDI9XW-6s3Ic9eh5GnCaDbUEZ81wzb5RHxnuRYz0qSPqP3WazoISRx1Z7fC-cVFhTrVh6n0FrYfAOxZnfYsw-b87NLdIyn7lCGv_YXK63BksolILERo78edl6TVfnN78Ia7oeQU334C8Vfqky4oiYvvFafOMFjyuErgigvdrN95kcT0XOj6wj7WcVhqhG9KsJBfsfbRMB-9xIG2lNr9PSizC2JsvqnnNPdpkj_DtlWYJFnZctQTnD9qf2ov7tdLuRSPDsEuaud4OFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚠️
دارایی‌های مسدود شده ایران که طبق گفته منابع مختلف قراره آزاد بشه:
🇨🇳
چین: ۲۰-۵۰ میلیارد دلار
🇶🇦
قطر: ۲۰-۵۰ میلیارد (شامل ۶ میلیارد بشردوستانه)
🇮🇶
عراق: ۱۵ میلیارد (برق و گاز)
🇮🇳
🇰🇷
هند و کره جنوبی: هرکدام ۷ میلیارد
🇯🇵
ژاپن: ~۳ میلیارد
🇺🇸
آمریکا: ۲ میلیارد
🇱🇺
🇴🇲
لوکزامبورگ و عمان: مبالغ کمتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94073" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94072">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4wrcXkvbSlJ1ouRPRKVU9JVYr36e5lcXtVIFGNPZnrCf_vN_AYRvDuXSAmsvO6rRs06Utv8ZkqBxaqJgFhLzDeOsx12irNYhbf_WcbS-DD4QOwFWPaij10XnEFKnnLC2FOHAAUdL1kYA2_EYeijcA_-W7rJaGYDQ18KAkTz9itY2im4cGbzOPNrVhdPRrupg99pbyU_a189navA6bXHujVYUiWuwMfz_bJE7Yd345a_SmhA_YZWZxx5lpnax7sUVLmo5NWmPY9D9_Tv3BZCJddypHI85hHt2Udoq3mkDn3ty-zB408MF5A7BWDPJ0KFgCCtzfhIUsvrksRFirIOPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی در کنار دختر ریاض محرز
😊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/94072" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94071">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suyKSoKH916eL0eTRk5_Q0sKCgh-ulYJeQyMLI67y4ob5FQZdcG_XleqLMYpPJt-RdtbhMlKqvwofveGn6m13v5cvVzvEkByNQXDTJOXVEfoQrrsfMZUUCG-bRuEuP6NAlmokV3WvCbhDssvSlj3opTgp63LO2ugtaPz3jOXAb1xwuAGwpmQDL-FrRP5wrG09nY6Rg3uWy2lYCqo1RlSveNUCDkekrVL0Vk7HbisyiCcPfbhRyy_YiPlZe3Vk6vHVAkRmfZiO5YdH2ovA90ePXvPVD-ZfCmiwF2KUT9vcIFBZ5d8a4E6T6-dg3lKdUr_vW1j8R8eixoyf4QmQaqwdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلزنان جام جهانی تا اینجای کار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/94071" target="_blank">📅 01:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94070">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/94070" target="_blank">📅 01:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94069">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WoLTkj0p5NYQOhUyzQZJEp9-KQt_GmH-WkN5tSv92B4nImF_j8GFMZtzMASC9LjxVBVo2lvKvk_CJ4PvB7vyH5L7haGjniUh83CgHsQH6Ar618iaE2V-uUUCGtbhCv5IP-bJyy0caEcWzPm5SF_Zp0t9WeCMnD5wxiU4YkEQYQkGe8aVbf1Z3jrVDbrACrG4YsNHH4KU0qnxny3g-I-_y2KhK2ub5hUv4g1H2cpZFEsUAye3nnZt-8aIxFaJt7ck4FTlkSV8oPMSqOdxXdRZuvYTK3E_KXkylFr1sg-2Jr1tZMFDrCY4si3Nm3eIA-R52pruXegpeprnt7SFEu2Jnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/94069" target="_blank">📅 01:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94068">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/F_X5Y68lfPaDcjzk_r1mlIXzNScvn0rv10mN2ZiNUCvtXbit4UZYydpJ2yIQeuV3IeWWQCEiAgbY-YuU5ZvA7ysguo16EYJu5xGPx7iucUGMhhIdLxAJaQ7LlHeJ4YpqXXy7z5FgrSTgYc0urcssiaCW9ETDKFWDM3U_pujqjzCmFcWAeIhvMjyjMIyaV8JJejN8XpM4PpI4_xleFp73FyS6S8w8_HBMDeITdm2bBiqhUTyvjx7U9-nHEBNNVNXtTtUrB6Nmi7Rp9Tf_P57oYVjq6cE1QxM0BD5njHs0lRadHyffhjx7u-KPPFtaY_dUKQ1f8FaFVw-v3khENkJCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/94068" target="_blank">📅 01:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94067">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJfOivE3ZEihNvWcwE98aEtjHeE9J-vSN7fHWJHxuQDX6jYKaET8rk2ljTNSfn5YTKitj9ty6OgbL5AK_m8XsoruosfbgIM9Z5xLI22KNUD_jkYsuMKIyZ9QY5Qx4fapo2fWwVacqsU-mKC-q1HkCv8fV3PowZw19tlyJFCTmnefZkK2gR7l3V6gwA-0ooyqR5Jr4PiX7LUpXZZqH069DNF-hFMUjNtWUnaHUA2yTa3aQ3swxcH4-7rYDFroLhSfUHjqFquZC-k92EUkeBQAdusek2dp48TTNeqCV6K8qWyZ_Q9zSFsC9bs3pnND-xPxXsGNqE3N9gLKyBQzo2X_kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جود بلینگهام جوانترین بازیکن اروپایی تاریخ شد که در چهار تورنمنت مختلف شرکت کرده است:
• جام ملت های اروپا 2020
• جام جهانی 2022
• جام ملت های اروپا 2024
• جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/94067" target="_blank">📅 01:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94066">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANZrgGXMlXoHKoHalNd801hUalgc9QwHxVmYOz2uRMRHHX0l679r1GybhOWFiZ0QXGyaQW3ctM-Al0WSd3Tz2Z7ZFCu1A-bZFHiXTdtXaL8izppnBW4zurQdoTmX1OpgT5Irma45iI3wyyfYoamkyCWwfd0hW-W2QAV_DACE69xdFZ_Z2rJooNI14O0J3XdQmizzXcJa7v_isxL5jgidi6iGIPqtJvVR1hd__P5I9XUF8sqnJJa3ZggSd4RUPGLU-_JIEhEu3sxuDWy51ILv4qt4gN5fq6dZVQwykPOvd5XouudjHDkQV4cFV5psdKtmRoD2luLQTU-elsxIWteIeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری‌کین در انگلیس؛ ۸۱ گل در ۱۱۶ بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/94066" target="_blank">📅 01:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94065">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsz6YYPE6yu1yGzyibPwQwm3nd13_sK3UVmR5DbwFYH8v9zPHe1omN6baSt5ZTiEF9CEPollDauQp7Eky_qkVMe8dHVS9FtYu3yFwGMFRVgbk2ToERvow4Zvw8snzL7kPwOEpvwn6iAaHXjKRhfRztsGql2TH4Od6gsdEDCPA7SZJKzDNCjwbs3MKt0X-QpfyKds2bWs0p6cSDPclE7oVW-HYIkQ1lkv1wzH5rCgse0n79k2t03Lc7BXSOlIKm295rG41ViVCjOdNpfKJRcY5jR2z8E9oq5n-WmlZcJpQF0mswb28U1sDaeuzEU65GWRec79hmWc8_yYrgZ2iJ3vhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | شاگردان توخل با گلباران حریف وارد جام شدند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس 4 -
🇭🇷
کرواسی 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/94065" target="_blank">📅 01:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94064">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEJb1DCgdaW7v32YemtuBvb65DiJ_ygxScZ7nCayAW4VUo5vX4Z5pxTXF2a5W95BHb6D8_SLP8PyT_lKVxoGNXNlBqPQm7vkL3kvYrlp_7uUxFFEEtv8m_7YWerrA_abeqRNTMM_CkouGEiiAPNG7avqbbmb2u1UMyRoZFzcombImb7COQ7K9_8Qi7LLR0hlIEv_iUdW0LwwlPqFpm52iglMK5cUBTNCe5Zbv3fXCVrBrW1B6JQQh3qDuFsP2LuZc6Y4e8dFYdPglo6IFky6JtPQw8OSkPHDztxp49jYcqnDlDqHrXQx8IK28_zKDTaxM1oobbUI-6kCYQ2mRyoxQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | شاگردان توخل با گلباران حریف وارد جام شدند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس 4 -
🇭🇷
کرواسی 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/94064" target="_blank">📅 01:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94063">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9YQcMcshowomChWzKiBLIBNP-eH3rioGiGL8QiknatrL_0jJzKYWNigjZSYqhGgzuujSSOIYep_TGmdK2lVVUZcmC8M0IirH-uUZcmugzlKOQXxaWZgWhQMUCR0E0NEp4-G0UY0IGiQMH_JxDdr-NP9aKMJYxVCbUVP6LaWZ6LhSp_cttxIJp87rfO0r_cPqZ9VSYqg-92Asj1MyZ5TV2i5xMbWWkZaa0icGwtV4jT7zErIFlCAudGUMuyWPCcFtKF18Z4lLusxBxyN4_3s6M7HuSusAGVVMu3ZddB-_yQoxbZwRRCSbmmDFv1j8_ew770qNro2Grbv2G-aqJZwmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
آنتونی گوردون ستاره بارسا مقابل کرواسی :
‏
🔻
۰ گل.
🔻
۰ ایجاد موقعیت.
🔻
۰ پاس گل.
🔻
۰٫۲ دریبل موفق.
🔻
۰ موقعیت گلزنی ایجاد شده.
🔻
۰٫۲ برتری در نبردهای فیزیکی.
🔻
امتیاز بازی ۶٫۴.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/94063" target="_blank">📅 01:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94061">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PU5P4cEEet2dXvC7bVFTHHBQNKzZ445NEbnbhodwiq3fb6o9Qt58o9RRk0Z2MJQEW06MIobQwI7vESUJ_SAVNxihVY7diyYbChEIHHML3E8iYPF_Om78lyAwDuyIuFqM61MdSP1U2Nony4UTsxKEHzCiW43MuEZsjEgLkZpXudF4oSMyYHfdbvWGLBm467Ng9Mse93X_4N9JgAG4ZOCoI2D0gE6yWOE-x0wvYodVYJ2GvwSS9CrxXZ7-9qL6MBaYjYMBFHI77gJjXel_pAxK8opBpTellsMducpUP8DwYHgr6i8C0lhWxWntHoOHRW79wbx3P5QFa-UEhhX_0q6qtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMSNBdNIZbp4xClGMlnBWxSQoN0AKO81Nn2N1TBZ3t4gBkwEmY7Hr25gLlryNvZ4OZ4IDD3q4k7C3Ha9mkMbv4aQPRc1A5fLXwGmrj16Ojk8qzAL6eX0vNojiptwVpi8uAJgY7Ce_xKZiFDBow7RzdK2p71gJYHwVSrgw5Nndt087nOe6QFeU3tPCxbch_UhVpemNFnLjKk4cBVEd5wkAtr24oYGYpfPFY1ePdaHQI7lqiLreGB_Mp5XBQQ6Pb4MTWc2xoWOM1MUO7K3flz7XT6YxxkIskXQ_O1aPL5E-v8mdq4e_VIpF93VPK_-im9a0FFjt0juzbwSbiOZni8DGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بالاخره دلیل درخشش انگلیس تو بازی امشبو پیدا کردم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94061" target="_blank">📅 01:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94060">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRdKaB-UhJfbnh7PT0lQjUjTxlihJgIcNhs3sd2sHzmt5npewClTRtX9GS-E-DRmJj6N6Ccj25eIhyOABsww41qQ-yIXc5FW-QKwJInKviY6UTr8VWEbDKPvdvHohi01CtCFkc3SAqHUwVtkVvsgnjbWmlx2lSAbkH0rXB5m1esrz2EVf30KF2bhpwzjKIZ368Z66FAd6bEoEt41WOnVvdOiXGwloPlIXe4Sf8ibsa6HdlEoIcJuIHwkwkdjegH2RNQ-LqKBDZHi6qf8rBcC77H8Jx6AFID1EwXic0khywaQCcSI9RhvJTAVIuR44JQjXrDlTY3Wk5GZdIiQBEu_Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | شاگردان توخل با گلباران حریف وارد جام شدند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس 4 -
🇭🇷
کرواسی 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94060" target="_blank">📅 01:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94059">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c11f876f5.mp4?token=KHRcxF6eUxO2tuvnKPblfGVTuIqG--SS3jkIQV-tMRct-JH1zL_z6e_o0yuj78tnvj01PecsMJsOmtkDx5FoiFm8v7rd9VhAqRdDS1b47oXj71v9WPXczEDvHIGKB8n4Pf1l7BjwuWSQPz1QiJ8pXg4pfaqERTE1oPEl9kIuRlIU-DU5SOrxDLRwev7K-Ef1SPttZNTx2k7tnefN0ebW4R6W9QqHpgG1kx4xAUObxAIvVXJqTfpBqtUzqhuivA8vzMcS1OFvexH2Cr3yoZ2jXrJd_g8hI5LEJvY3FLcro4syUmpuEzuBOFfdbdz6QKQ0lcjkQ9cBi-5mbGTSrbMge77Wcp9IgDF1vzuruh6INGAiJqD4TRDg7lJl3NBJM4UG3eqM7Z8WXWWkeSxl3OVVfUkaTFWg1CHbR6WRfKygnGU6b2nBMep__Nk7dEwE_Ke0OZ0mIDSsTtBfeMBfw3lw6XF5jbsDpan22h7kBgGEcLXpOm3d-IwlLXiRUexcC7-z2LKS8wC8cYhVjBwMGMEa82FahvMBmhEXVJggFKx61fTk-n625UOgPRGYGB4-BReXM7V-34IT7CgtDL_BrH6pj0WqlqIw9ZBn-g7nl80IpAdriDqolmay7ErsJsuS75zT6PG5Tv_ycqiNHJQ1XtFiImoUpSUu_5sP_CJJrXAsFzs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c11f876f5.mp4?token=KHRcxF6eUxO2tuvnKPblfGVTuIqG--SS3jkIQV-tMRct-JH1zL_z6e_o0yuj78tnvj01PecsMJsOmtkDx5FoiFm8v7rd9VhAqRdDS1b47oXj71v9WPXczEDvHIGKB8n4Pf1l7BjwuWSQPz1QiJ8pXg4pfaqERTE1oPEl9kIuRlIU-DU5SOrxDLRwev7K-Ef1SPttZNTx2k7tnefN0ebW4R6W9QqHpgG1kx4xAUObxAIvVXJqTfpBqtUzqhuivA8vzMcS1OFvexH2Cr3yoZ2jXrJd_g8hI5LEJvY3FLcro4syUmpuEzuBOFfdbdz6QKQ0lcjkQ9cBi-5mbGTSrbMge77Wcp9IgDF1vzuruh6INGAiJqD4TRDg7lJl3NBJM4UG3eqM7Z8WXWWkeSxl3OVVfUkaTFWg1CHbR6WRfKygnGU6b2nBMep__Nk7dEwE_Ke0OZ0mIDSsTtBfeMBfw3lw6XF5jbsDpan22h7kBgGEcLXpOm3d-IwlLXiRUexcC7-z2LKS8wC8cYhVjBwMGMEa82FahvMBmhEXVJggFKx61fTk-n625UOgPRGYGB4-BReXM7V-34IT7CgtDL_BrH6pj0WqlqIw9ZBn-g7nl80IpAdriDqolmay7ErsJsuS75zT6PG5Tv_ycqiNHJQ1XtFiImoUpSUu_5sP_CJJrXAsFzs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل چهارم انگلیس به کرواسی توسط رشفورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94059" target="_blank">📅 01:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94058">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رشفورد</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94058" target="_blank">📅 01:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94057">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بالاخره انگلیس چهارمی رو زددد</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94057" target="_blank">📅 01:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94056">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گللللللل</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/94056" target="_blank">📅 01:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94055">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">لیواکوویچ نبود کرواسی راحت 6-7 تا میخورد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/94055" target="_blank">📅 01:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94054">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پیکفورد هم خودی نشون داد</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94054" target="_blank">📅 01:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94053">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIKMaUfXkh31aH-u8V9S0P3shD6VY6gxvHP4vT_UKp9LNVRONh4guLbAocyKNadwdiK2saeNbi7Or22PG2hlx-TgvdGuZXZcUJm33lJZ1rfagwQFMExGdPbRiTtj63M1XTRQpp_mxurtPRsmfLG5Jq0kC-12hDX44-q42gTNE48ccdd0utQX3DWWKH5ZdOfm0mrrwziyeDhGoePKiKHhLVcXksZsMb_Pvobnv8TrJ0Ytt38xiAJs24Tyxc_nzRYCWf_B2bhO8XXWIu9gcPWJuyANYv5UCHOrn05jZoj2fMwBf-oygKEQMmkAWVhYHK3_o7oVfI00iI9g4hyoDGqX-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇭
🇵🇦
ترکیب رسمی غنا و پاناما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94053" target="_blank">📅 01:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94052">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
#فووووری
سخنگوی وزارت خارجه: همین الان تفاهم نامه بین آمریکا و ایران به صورت دیجیتال توسط رئیس جمهور پزشکیان و ترامپ امضا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94052" target="_blank">📅 00:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94051">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">لیواکوویچ، کل نیمه اول: 0 سیو
لیواکوویچ، 15 دقیقه اول نیمه دوم: 7 سیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94051" target="_blank">📅 00:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94050">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بدون شک بهترین بازی جام تا این لحظه بوده</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94050" target="_blank">📅 00:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94049">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مودریچ هم تعویض شد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94049" target="_blank">📅 00:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94048">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پشمام بازم واکنش نشون داد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94048" target="_blank">📅 00:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94047">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">لیواکوویچ یه تنه نزاشته انگلیس گل بعدی رو بزنه</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94047" target="_blank">📅 00:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94045">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rW0vi_2RGo6Ftpd2F8Rq6ZR0obOW_smn5WVm8bJ8H8zjfY2pKA0UWoBgTD1Zf8z7W7288We8mAKhPM_Km97RtkH9dRZ10TUqLNlzF1I2MOfxlPnKMvzxcTDPXIxbWoT2buBsmKUSaxOrz_Zbz8zLMdVly84owjssW0LH59yR4c62baTn3jeZxVku-PhsUB9Tk4_Ox0D0Jx-NUrJrvi-dEPI3cvyVMc15pKhWDEQZ2DomToo4PigBr4keumHASOlyue2hHlM9keKIhPis_KveJR854g8Ccma7imd7RpxD9UNE_abmfhn5LC1GGnr7kl7A_jl1ZUiMAqHNeCg3wO93_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d8mo_WoRkn7yfpaiyexC9XRG0jlykdtwqvkd0emVfVEIAZyU1cxWN-HwxairdqE8uY3HCewRhIvk2cPIUtmOGCArHRTRJvFwzYxLGvrBpg5r_Uel_dBm_maNmMaG-fEVFFGBsQXODbBySrs4lJZwmxoEvZDTE_NuuZFE6_Uxjbf9rhFmWwCK8iAWlMqiOsT6ud-JhIR21CpJMbV1JMX08PBNmAD8NjLNFzfOdjQELox1h8wfz4uWh1I1oKhpBAUXuQuXrTEm8OvxjZVwbdMHd_mQVbq2TXkj-G5xvnLedc5XQhhWaB7pMUpSnTG0GHq9Ad_QaUEN9S0Yl-ZOZ9-1wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شادی گل همیشگی بلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94045" target="_blank">📅 00:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94044">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انگلیس نزدیک بود چهارمی بزنه</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94044" target="_blank">📅 00:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94043">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گل سوم انگلیس به کرواسی توسط بلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94043" target="_blank">📅 00:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94042">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">عجب بازی ای شده تموم پشمامون ریخته</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/94042" target="_blank">📅 00:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94041">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انگلیس سومی رو زددددد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/94041" target="_blank">📅 00:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94040">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/94040" target="_blank">📅 00:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94039">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بریم واسه شروع نیمه دوم</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94039" target="_blank">📅 00:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94038">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZUc0zbsV2KjwqE0NxN2AphyQX2LGgeWsJdmyqhg8_YzHyX_QZvBo5DLNyIJRtYXUNWU_YrBg2LqEEv4nwcpur8h_WE2RZ3bc2nyYNUCdWrEB19ChMzwSZllygDjZ9bcTKaAKH7PCu7a1J9dwGpn1a493kax4wr-XdaYMJ1f7Mz-ccvk9z4r7qCUEdDA9O7U9YuwZaLPty6teMuK-4Pl0BIZeZrW6gmYsj4eF6VNSGmocTkIEp-7r6vuWSbYtGkyO9J9BnUctn6xb1TYSE5f-qS1OcgO7czbWltln9YCCPM38Kii3rlrYeE_FsEk1w_GO0n3naYwkj_Ihk8QP-MMMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری بانو میا خلیفه برای مهدی طارمی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94038" target="_blank">📅 00:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94037">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r21Jhomq2QjXetac3j098lXcbrBxI9MaGHG0220eXwC3tFJ2kA0e5yzGDsZsFXdooUzpF08qyweg2tKN3Y33_mGLYUUa5qIQmGRFxmrd1nOk4gxNWLuLkHiCCy904KQj0mYiKwlIxMG4OQfOElXC6rPigDoLJIkw82lcK-XtoQl9wO6qaKH8NWf50krEOrVV7yw1oEZl_EBe4LXgg864UiUKlDPzwdX69UnqkcI2MNWCQ9Sfd1oH1y9BKdq7ViuyTuPQIAC0s0fuAj2LD9VuGJLQTcCtMTM3Hcup4defzlZWk1GhbXxwTplZdw3OqkcWdi7ZHP4W5KADlKVtKhRrwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هری کین با ده گل زده به همراه گری لینکر، بهترین گلزن تاریخ انگلیس در جام جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94037" target="_blank">📅 00:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94036">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پایان نیمه اول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس 2 -
🇭🇷
کرواسی 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94036" target="_blank">📅 00:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94035">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">چه بازی ایییییییی
چه گلاییییییییی
لذت بردیییییم تا اینجا</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94035" target="_blank">📅 00:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94034">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3d4cdc8f46.mp4?token=q0QTIVUVLk12VNBmdM8R_dQmrV2NiSW1vJJDCZ6SasvtAn_HYoVJCZ2eMBXJK8mhfS4XKgqzpCS28dtnq2p4JIhRAgi8FJCe27l3Ve3qBi68nzMtWPsCszHhwrRUtU3FQDClGNvLZAoAY_BfEmLbETfJ3G0owrXmMIUkmZ-MlbfDEZNRganBZAGUrgynGffWPw0SfkwWhrRoHBGKGK5DIV60Jx0UnZK-eOJQ_f88p3Ni2SmQHxm6ZIXWwrObsNYke0-qlVMlHM0lL9USm5JEFPU9MzK6zJuWjLclsYDK34MJi4RcB9UOdBzd-5Km78NBHd57aKdCzdKUSetZ3AkZOKcMVjfukXPP3zUE_eXLT71hSvd_TYQi1Kse-rEV-q_jPg1XpsNHWjn34l3qCOv3LQ37hhkC-H5tlDWLOnEAt8WkyGLZ9KKAk0It-wOqZ1QraApJAtoCCBdShu9uyOgAVwyFLcitra3xSaowtTEL1odPmtHgBD-yzvaUhyrmaoeMCCyprevGegO3-VxNDrpsEmPrbDMscZXVUO03UnMCo7Isw1c_mSodpciqaCvQ0pbG_dFn5DkuSH8ytyG-m5GnZuutjnKUbk7OSgWMHD2HaRCHqQda8o0Tz22HgdZCIGUKLOTjHqrjGc_w70LKU0QjeSKq58DfBos4yLILxUYMUEo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3d4cdc8f46.mp4?token=q0QTIVUVLk12VNBmdM8R_dQmrV2NiSW1vJJDCZ6SasvtAn_HYoVJCZ2eMBXJK8mhfS4XKgqzpCS28dtnq2p4JIhRAgi8FJCe27l3Ve3qBi68nzMtWPsCszHhwrRUtU3FQDClGNvLZAoAY_BfEmLbETfJ3G0owrXmMIUkmZ-MlbfDEZNRganBZAGUrgynGffWPw0SfkwWhrRoHBGKGK5DIV60Jx0UnZK-eOJQ_f88p3Ni2SmQHxm6ZIXWwrObsNYke0-qlVMlHM0lL9USm5JEFPU9MzK6zJuWjLclsYDK34MJi4RcB9UOdBzd-5Km78NBHd57aKdCzdKUSetZ3AkZOKcMVjfukXPP3zUE_eXLT71hSvd_TYQi1Kse-rEV-q_jPg1XpsNHWjn34l3qCOv3LQ37hhkC-H5tlDWLOnEAt8WkyGLZ9KKAk0It-wOqZ1QraApJAtoCCBdShu9uyOgAVwyFLcitra3xSaowtTEL1odPmtHgBD-yzvaUhyrmaoeMCCyprevGegO3-VxNDrpsEmPrbDMscZXVUO03UnMCo7Isw1c_mSodpciqaCvQ0pbG_dFn5DkuSH8ytyG-m5GnZuutjnKUbk7OSgWMHD2HaRCHqQda8o0Tz22HgdZCIGUKLOTjHqrjGc_w70LKU0QjeSKq58DfBos4yLILxUYMUEo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇭🇷
گلللل دوم کرواسی به انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94034" target="_blank">📅 00:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94033">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کرواسی گل مساوی رو زدددد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94033" target="_blank">📅 00:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94032">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پشمام از این بازی</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94032" target="_blank">📅 00:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94031">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بدون شک بهترین بازی جام تا این لحظه بوده</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94031" target="_blank">📅 00:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94030">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گل دوم انگلیس به کرواسی توسط هری کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94030" target="_blank">📅 00:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94029">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انگلیس دومی رو زد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94029" target="_blank">📅 00:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94028">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94028" target="_blank">📅 00:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94027">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گل اول کرواسی به انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94027" target="_blank">📅 00:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94026">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کرواسی گل مساوی رو زد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94026" target="_blank">📅 00:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94025">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94025" target="_blank">📅 00:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94024">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAPOJJ-SkvZRMZp1A11DP3C8bPJTlQ6ocYXV5t1CeaVDj4f3SWKvmmlIgKjau0dBq6LCZEJTMfhemp5eOdzZLKvczKNDeXkgpyRAkk-UgIwTaV4YtwNp_iHqOj0TmJMm0cQOmI8Hf04ZNtw3DiSu7xwZ037IgNYMVTIXWKKMfgZrcbRNy7iIP-oS-KpnLgniil_VeW-Obk5lT8SG8q49UpwuV6ZSyQsENYTrB03zoN97lEzc9-yf_EGi63LN8yLjOn9n6GpSJy3S15PvzkYWU1KG-xM2uw6vdBNsEI01TgwJYlq4pUfAr1Sk64LX95DJ3H5T-7yZfhcfGHLUK0_Fzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پست جدید رونالدو:
این شروعی نبود که میخواستیم، اما تا پایان فاصله زیادی داریم. سرها را بالا نگه دارید، روی بازی بعدی تمرکز کنید.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/94024" target="_blank">📅 23:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94023">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/938fb471c4.mp4?token=sy6JQ3WXzlrPyKS1-1UPzCF4giQp7AqfJHuKkKrm4i3QueZR5ap9abP386PpBrraVoF9D-hH5eTuR_TqpEg84Q9ILoid42aFkPmN918MZS-SXJT7VtPaGEN4otWpIMbw1W5HFa3B5du7lsoHWlyHAa5A0VbMQjX1A2YI7h6tqJofc3PtYdsuXKC-j4Z9H2EIL1HNK6kHNavFwOxR_blf8gntH1UhNmjDSk3X2xckshCo-3nZXxXQ8XU4IIp05DZzu0XasfdjXIHGC8CU_WHp_MxIZ7sHTW9j14JLIFmaga_oF_M6Td38BYhfRfenR0D6jC_dhAzyNb62HJamc8s4qjP4L9sfYTfVWTA0OQtf1SRfPor-TRYhP30fQzvCIfNiETGRwAVB038aMe0FfZH-xIw_SFoDoWjBmzE0-xWhzeEG2XCFdWD6Qjpk8KxUS-2NcEQ1UtiABouK_YoXo4TZ0bcSVarj-fYUpkC72CS98VsWGYUQdHweRg9o3g1tVpbE1RLi5VgohA7lBb1Egr0Xi_ehA8xVApCsohy-yB_-kVJLK4mz51QTBx0rPyffuGMd5zaGGEAczBHTm5P4V7s95FEVPta2CYBJXLT6fUYdADcCubC6bWXUkejyMQNyrqkrfs2M1Rhrb2Zawbs78u2ZkpnclnYKUJlK1Lx_5M9TaGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/938fb471c4.mp4?token=sy6JQ3WXzlrPyKS1-1UPzCF4giQp7AqfJHuKkKrm4i3QueZR5ap9abP386PpBrraVoF9D-hH5eTuR_TqpEg84Q9ILoid42aFkPmN918MZS-SXJT7VtPaGEN4otWpIMbw1W5HFa3B5du7lsoHWlyHAa5A0VbMQjX1A2YI7h6tqJofc3PtYdsuXKC-j4Z9H2EIL1HNK6kHNavFwOxR_blf8gntH1UhNmjDSk3X2xckshCo-3nZXxXQ8XU4IIp05DZzu0XasfdjXIHGC8CU_WHp_MxIZ7sHTW9j14JLIFmaga_oF_M6Td38BYhfRfenR0D6jC_dhAzyNb62HJamc8s4qjP4L9sfYTfVWTA0OQtf1SRfPor-TRYhP30fQzvCIfNiETGRwAVB038aMe0FfZH-xIw_SFoDoWjBmzE0-xWhzeEG2XCFdWD6Qjpk8KxUS-2NcEQ1UtiABouK_YoXo4TZ0bcSVarj-fYUpkC72CS98VsWGYUQdHweRg9o3g1tVpbE1RLi5VgohA7lBb1Egr0Xi_ehA8xVApCsohy-yB_-kVJLK4mz51QTBx0rPyffuGMd5zaGGEAczBHTm5P4V7s95FEVPta2CYBJXLT6fUYdADcCubC6bWXUkejyMQNyrqkrfs2M1Rhrb2Zawbs78u2ZkpnclnYKUJlK1Lx_5M9TaGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول انگلیس به کرواسی توسط کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/94023" target="_blank">📅 23:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94022">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">هری کین بالاخره گل کرد</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94022" target="_blank">📅 23:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94021">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تکراااار داد داور
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94021" target="_blank">📅 23:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94020">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">هری کین با قدرت شروع کرد به ریددنننننن</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94020" target="_blank">📅 23:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94019">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خرااااب کردددددد</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94019" target="_blank">📅 23:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94018">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خطا از مودریچچچچچچ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94018" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94016">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">برا انگلیسسسس</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/94016" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94015">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پنالتییییی</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/94015" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94014">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بریم واسه شروع بازی انگلیس و کرواسی</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94014" target="_blank">📅 23:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94013">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jm_ZpzBa7_m7AeBmGNkROGCzi2esBmdIVUJtmIBM1oPga2D72q8yfYXkXyMeEhNsFj9ks2RH6frgX4AVM--23lF5Pqux8h4vZ1jvofUhJkj2n2bFx5wWCUs6YYakKJdQQ9oPfc26JyRZlYQzpuZ-yhg5QDsI2ZhkHqnBWoXyHMcJ4yMjj18bC8kuNGam-WdL8sZFr0mAse7d2UqeAV9BDeOGsrJHmWVwT3TcLSNATJYybKRaqk-9fEYcI0vBMQ46IDXXFhQs3JzZ6-iT1GDJFKWuM8RuBtmQguNsRsXq73JAHwXGirkwQCXLqej3bIi81qSk6XHYIGMiorToMYgMXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوش و بش یورگن کلوپ و جردن هندرسون پیش از شروع بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94013" target="_blank">📅 23:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94012">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAeAXfSLMG371tMkicusfLVF7-9Wp5364O53RruoJpN2LBWSLeUvWOYFKEXjtZxpcX6jD14dVToPc3iOP-N22ZJk1Y092vNxlsHO4xxez3m35DoeX_fnbPQ7Bajl7B9Qn8vlAmT44gMrQ_vBswuPUSgSMfV6DMdrFlXeCLwaoZFt_vLDxoJddOZTeF27sQrvoA1aTxzS9UA7AH7Kr6NfyNxx6Vu1uBdwpLlq15fSSiW3-hb0UpxAmXRGIDmz041B688BXgb5E-jn8qC8EXQVcwcDfw1wTADPlPwUh6kkrXF16jxjIZSTtEQvSdeUsn8p_qtOXf1jN-iKSJCekZhlng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نوس، بهترین بازیکن دیدار پرتغال و کنگو شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94012" target="_blank">📅 23:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94008">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UtllcBvxNjtvxP0_H58pn8WuArqo7cby7RwfTsXrcY6GAO3zmBgR-T2saZ6UJuOc2fg_KfPVov4fU2ibufGs4f7DECUnZcZcdiA8Pkts4l_oN6zbQ6gN5tM0UxBn5vpOA5vZP0xfXCfYKSAKiXNzmBfOdzA8A_E8_wBEwpPrxnxDYyTwZPMKWDT1O6rkhwuQyBCFVwMv3zEnSNvx5OOVWsAgm1T1mA5HGiPRRSj56tabsEQEWheYBIouKNtbbr8RI7eACdTvXVLnh2R4GrsOhKNXwXc89pPFzzQ-MQqy0qZi6m5Op5PN6PSrziywxuKU0kI-IgL8A_RukwL1EIEaAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hMpwO99-fp0P957ajpP0vCb_p2sFNNIHg7qiinuAFytgXPFMhWEVHDnDaquhERD_Xr9tQrb9fyYNoDMpiRKtxq-eBemYnQWlE3CuwOuhB0OkkGbrfPUnVR9XsuTl5ongbhQHOfdp1wqA45wFblMJoaYHZddt_ZUgUHxReLeCfv3hskzqplf_kkMjHfFnjEY6m_pAJsP5p74YfHsos9xnpjQkr5lCu61nWBwYsQUIv-uArF0xUltfzEBY86apoPwQLfiY-nddrwkEwXIj6bugSToIo091g7XpUPO4neyjLpXc8I0v72lWg_lGBvvnnCHWC1vinKI8LTwEyNlrwqx5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AbnTQFYohBljIS8yU85KtNmcU1RRaOYjDicxKsWZ4pm25iKcSElofnOdQ9_Hbhgfva0Bo_1zhIPLa8Vml2wFM4CrMFMY85ee2NjA9HQftHEK8m7IcPEDh69h9eICB5uJwNogdhlKZv4WFrNYltTuMr7g3z9XHMK44vyhIIhOSMTk-sFtWzI4AgPtwR072VEs6laNd16Z-rlbKJ-eAbTmTRpDOBaO6MwYELUim_xa4MhR1-aJfBh54rlWRprRIylg3K1J4PhhOwCUv94w9GkJ2xAHvdWvwcCcVR_IBvfTD17_ePvhCwMjFmMzYHVMnHH584Y89r4nSfxjFnkv-lqGrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/unHn8508yR0cklA5kk_mr0j_ab1X-3sHC6-TayksN7tr3whOaynwTyxH8H4fiS7_cOena8iPIA2gFWFzWZaEhRFutVvVU-KP17TW-YmbdHVohj3n-WGNFPCaSbkqw2PeOvATEZwymbgOcxYoUlrbTJeehwUR_2tJh8TfdsG9f3ddZrlVPVslPtzXNoMHrVeNC7u_PoU_OIe8SacCml9oUc8s7_UfgW2vg6_9ydmyZogoLCodX2W1ncEHqtK6Gi_1BJjtL1xAR_Yk_IVy7mR5OX_-Z74XkttLAZE_A-g2Y5_6EtK13qyKNWs9_E-RNeAUVmuLyRqDg4mnLhDaNfj6Dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
👀
دوباره این عشقتون سر و کلش پیدا شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/94008" target="_blank">📅 23:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94007">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFPWA7fMiD02vGEVE3Gc_oUU30ZqIH7aIM5VX7hY4SGM_WrfElyNUOG5zBkhrrgQoA2UTFtcJe97BG8pC5SVh8pmozKDLr9U4XT4XfWVOkFipUEpF6KdfptnLt1IAW_M7u4hZVJPYx0Eruc_xjw9wTlhRox2vggdAliiBZsoMKhWPQpinvBVCojHUJWyCnq-iLMmbrCIyKKCt2462anw_W5QOKX7nm6WMbqMnRcZDI-tVfLd6b_bUB3gowyDpcjhMxxD1MynIrNKeWAgtIO4CLT6ZJsXF-B5s43lfPPdyxNzCSSbiK6fyZG7GRNMzLju0_tpE_Y1pWCvNGkyun31hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی داداش یامال واقعا کیوت‌ترین آدمیه که میشه دید
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94007" target="_blank">📅 23:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94006">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjEW1C7wF_GtUx2j02cp1bbLVVOobMAjL53OaMWkakW3LLeUqec3XUvatwI8YFasxh63RmlSZX67AxfrPlFPH3YV4jM-Axi8QQRYdl0z-QDSw6v7XGHsJPUTlzVUvrRVFKZrxmRb3_FOVA5SkhjkIfY4Kd5h8_laDcy7sNM9xgeMO68o18DgMAzv7DwY2T0Sy_V7IGQA8VoFWBD8MlEtaDNpXpZw0QyhZ5Maqy1zFvPW2fAryriNWam6X2zebWxKhbAxzM3vqcVF6Dgc8_FZMpNrKGGye1gzQwjJaGY9KPoY1rVrvzC8gI-kGJIer4p8HsqDH8XrauuEx_qVp5s9Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
با توقف پرتغال مقابل کنگو،‌ رتبه ششم رنکینگ فیفا به مراکش رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94006" target="_blank">📅 22:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94005">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNLSpGffeys0ycpul_MX0WzWEU5MHIa_3rPBdsQCB_lBJfTym0Pe_VDrIiJoRoamd7HMvZasTOsZcFY8k48XL4eVgYR77nTpn6OjXkDSdPa7ECU4iOkb2A4d72Q-NJTNZRYSPv2D76TrfVVBN5RvRJCTo9GObanaI-3-0AgnQPy1nX5DfKR8Ynhlib5OadF98vQRBIj0Y22qy7L2q8S_j9T65nR7uEvONUiTfzzrMSCmUXpGESwdu0kkvAUT3mUWg_-1dfV0yZ5FYQaY9A4ma_JEL2Wjt1jhW2NYd86RtEByFjrySMXxQ4eHNUoi_vn1zibBddYoieP9vzazuXyU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
تنها ۴ تیم در تاریخ جام جهانی بودند که در بازی افتتاحیه متوقف شدند و سپس قهرمان شدند:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلستان ۱۹۶۶ (تساوی)
🇮🇹
ایتالیا ۱۹۸۲ (تساوی)
🇪🇸
اسپانیا ۲۰۱۰ (شکست)
🇦🇷
آرژانتین ۲۰۲۲ (شکست)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/94005" target="_blank">📅 22:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94004">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
#
فووووری
و رسمی متن تفاهمنامه ایران و آمریکا منتشر شد:
— توقف فوری و دائمی خصومت‌ها بین ایالات متحده، ایران و متحدانشان در تمام جبهه‌ها، از جمله لبنان.
— هر دو طرف متعهد به احترام به حاکمیت، تمامیت ارضی و امور داخلی یکدیگر هستند.
— توافق جامع باید ظرف ۶۰ روز مذاکره شود، با امکان تمدید به توافق متقابل.
— ایالات متحده بلافاصله محدودیت‌های دریایی خود بر ایران را لغو خواهد کرد، در حالی که ایران به تدریج ترافیک دریایی را باز خواهد گرداند. نیروهای آمریکایی در نزدیکی ظرف ۳۰ روز پس از توافق نهایی عقب‌نشینی خواهند کرد.
— ایران تضمین خواهد کرد که ناوبری تجاری امن از طریق خلیج فارس و خلیج عمان انجام شود، با بازگردانی کامل ترافیک پس از عملیات پاکسازی مین.
— ایران و عمان درباره مدیریت آینده و چارچوب دریایی تنگه هرمز گفتگو خواهند کرد.
— ایالات متحده و شرکای منطقه‌ای ابتکار بازسازی اقتصادی و سرمایه‌گذاری برای ایران به ارزش حداقل ۳۰۰ میلیارد دلار را آغاز خواهند کرد.
— تمام تحریم‌ها علیه ایران، از جمله تحریم‌های ایالات متحده، سازمان ملل و آژانس بین‌المللی انرژی اتمی، طبق نقشه راه توافق شده برداشته خواهند شد.
— ایران مجدداً تأکید می‌کند که به دنبال سلاح هسته‌ای نخواهد بود. مسئله ذخایر اورانیوم غنی‌شده از طریق مکانیزمی که توسط هر دو طرف توافق شده، حل خواهد شد.
— تا رسیدن به توافق نهایی، ایران موضع هسته‌ای فعلی خود را حفظ خواهد کرد، در حالی که ایالات متحده از اعمال تحریم‌های جدید یا استقرار نیروهای اضافی خودداری خواهد کرد.
— صادرات نفت ایران همراه با خدمات بانکی، حمل و نقل و بیمه مرتبط، معافیت‌های تحریمی فوری دریافت خواهند کرد.
— دارایی‌های مسدود شده ایران به تدریج طبق رویه‌های توافق شده متقابل آزاد خواهند شد.
— یک نهاد نظارتی مشترک اجرای یادداشت تفاهم و هر توافق آینده را نظارت خواهد کرد.
انتظار می‌رود توافق نهایی از طریق قطعنامه شورای امنیت سازمان ملل رسمی شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94004" target="_blank">📅 22:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94003">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnFCqBP_ZKif1zBQpb8GhpoHJUd8h3qKLbMaYNxEeRRpKgQqdPB_g6sU10cu6jYcczJsOP3dFAT5yhYwVaPMY3x93GKtH4uWi6ZX9Qz_aT1Ei6r8JLSb7jJcArcQDYZbg_FJdhhLd3vZm364pBo9yeEFRyssaosKOkswAd_m1nqsGr9_WUHZK3W7FlcnfINgIfKl3SCf9xGFEZd9ipR17SKLpGB2CuRMNEfJ-skulmd6N9LCDkzLW-pbgsaqp417R7c0KHbWiI3erj7tcb2_ZtsOfQdr05X3LjXnMASE7cIWfE8hZst_raDXAX3kmleifFo9NgRacpCq8sJCH89bqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇹
📊
عملکرد فاجعه‌ رونالدو در ده بازی اخیر مسابقات مهم و حساس پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94003" target="_blank">📅 22:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94002">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEc2DH3ko34aWTfaM2BDwvjYJ5wqE0mB2nr_ct0zDQMuYNXl7xrL54aiJdtjgeitH2YAVWHHjL4ZS6QBTarrzahttcc2GUvP3qY5O5UhkNJV4qLWbPTNKI62H_sVBWCAz0gavYTPGBTJzsKTVnpJYZ42Bf-saB2sSGuKm7HFfmz-CCUn6eYa7Z9jxdJULD5EpbuHX-BtZJeTEao0kRfJ5_i12LJmLd25m4S0Fx3D1mQ4qjF4v-8c2oac2kih-HdjqffrDX7DfUbWcX7YPU2_q8QGrJUwfNWcNQ6kNdizah-YOBHzLD0OTTIeTnc5BrP3US4WwbQWThd6pT5L3B_Lhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
عملکرد کریستیانو رونالدو مقابل کنگو:
⚽️
0 گل
🎯
0 پاس گل
🥅
0 شوت در چارچوب
🕺
0 دریبل موفق
🔑
0 پاس کلیدی
👟
25 لمس توپ
✅
19 پاس صحیح از 21 پاس (90٪)
⚔️
0 نبرد زمینی
💪
2 نبرد هوایی موفق از 3 تلاش
❌
3 بار از دست دادن مالکیت توپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94002" target="_blank">📅 22:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94001">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQcAp2DlRdD0hkUDmYBUdrs1MaiQSCIGsRaa7F_ziFGWE-sKXSyTq8hqn0BMoaCJ3Fcjn1tNn6HjFNXbFBu7PAER_2qLLwD3eZ56haNDuqQiNkMX7RmDSlQXgIiWWfzAU1p5GbKGt1auGkgW26M3s54KO8v8DsPLsFwllzxYBVhydDQWl5p8zrAblHf56XNueRRqh5EDjYOwLJDPZvdgpPQMF5YkoNzybXWCkj83XxhaUWbCS-qJq7x3h37aKxAkT9Elh_hUln0anU50Tfo9aJ1Tj5UzB5VOFBIo0yJrgwMhCmmivYTQ7i6NvtZwjY1k9DncwQiuj9h9Upy2FbJ5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
❌
پرتغال برای اولین بار از جام جهانی ۲۰۱۸، نتونست بازی افتتاحیه خودش در جام جهانی رو با برد پشت سر بذاره. آخرین بار این اتفاق در تساوی ۳-۳ مقابل اسپانیا در جام جهانی ۲۰۱۸ رخ داده بود.
🤝
😀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94001" target="_blank">📅 22:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94000">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckqZ6-QM81LPJQ2Efrz9XsELK3k5JVcaiGz9ru1avMtTs5rz4e5xIpF2x9vL9p19o9Xl9UR3hgKnP9S0ZvuIKaHvWBvCO8ODUaor5M09Msn6Jlw_M6fwK-W7aGC7p_H8PpepoLCjIsNU4OVqXEdXpKiCQKoBKIBsIEUbUKq5KZQjg9PTxR6jjylMQIRVU5grqujxAdbrhfZyH4bfujTKEwrnuzpQBvHFAU5EGokVc53qfDjL02GkP28DwqAwfnVSPaYXU4qFqsBhYozmd29lS5Ji472_WcnSG6G4kdck9Fr-HDfwMdrE1u4ACFZy1j-2_GiP-DNmw3EUXkf_R1X_Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🚨
نمرات بازیکنان پرتغال مقابل کنگو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/94000" target="_blank">📅 22:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93999">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAuZMpEQJEYQJeCs690u0hbuFKfK4Bja64H2E6ngtGbsylx7XdnVC83phBXboofWzw_GoRG4eHnuTjTu9tWNnVtCEQAfrUZKyFpKwfnSkkay6KkmUwUTRXeqS_lonz1LWXOWWmsQCB7VQ6adipQPSzzJ06raTuC87Z8YFk-qv5iIPmLK9Vl2lLsdZrhGCm2_6CnxoPCM_0W7Khhb0ggL15GB0xY8DjCx_td7wR22rVpWmnHMMuVckl0ja_kv9kPD6V_lwiHSHZM2X9bV75hZ1_GnLcMagoOM9Pv7ia71cJp8B-ENZYEePgR2IxMXkZWEy5HVR3KjHpEWTTlhzwbZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇨🇩
آمار نهایی بازی پرتغال و کنگو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/93999" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93998">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6aoZIsfwqWj0-hecjeQR-EfmevnvmH8bJSht08sjLvjgXQ_rGPS73wh-clGPCdzOt4-sK6zH8hgr14UO1-TAbNvUWnV7R4xyHCSAQIrz-xAYMhl9StOW4pT3bEETctwt64FKnRsvbLDS_-K4Z3Yb3Lw02K8vqFv-xFxBv9VpA1zTLmDJqvMJzPM3DArEMR7fIiga3NHg5p96GU3zC9TFypybysK6UGpmpTOFSofBsG05QbkrjYZlACpLWCwRSmuxaMiniB5ZUl1qfDdJeNkFWv42thX-Mq-KccL2imIjG9K02eNDDAymdnu8Zn8-gYjrGkqXSx2e3UYVrNbAfzcgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|تقسیم امتیازات در جدال پرتغال و کنگو؛ رونالدو و یارانش متوقف شدند.
🇵🇹
پرتغال
😃
-
😃
کنگو
🇨🇩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/93998" target="_blank">📅 22:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93997">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">۵ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/93997" target="_blank">📅 22:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93996">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پرتغال ضعیف ترین مدعی بوده تا اینجا</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/93996" target="_blank">📅 22:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93994">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hE1uxbVlju48FxHM1PEwngoXxOZ6b4f5jFO_veEkxeXWb_rAM9MiykS7j592mcDP5StEcZNL-yZJahJBhuRB3sHVg0UVekscv9E5bte-sPAJvOc7MiiSfLwcuaOz5PeSVW4fEvipoLxBLyoYjV9AN-5l6VA6bEdIe7RXPhjPWKw9InjBJWemhteREHp1CZuYRng3_9a7XnXVEa1xm-IJIE5PUE52GJ_nU83_r1dmUht0sKXDPUGiJhK3m5G7P_VdVlODhjioBqd_nTzRGas91kmiWKN77taQER0XeN8M2oQmkBZN3ArLrFoCUlICy4W00nmlhqGY9XQKiUFvuHbRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BquqVOcs6hGSFup6-hjRTULNNPEAXZgbdIDBKFG2yckfJls8MIzn33jO7eE1NuZlrOL1ieCQRAgNGAIWd4dlNF1kCtv2L9JOzwdl9NkZ2H6hfUbDUG5_cHnuOnOUFjTdGhykWzbr1BtzCL7N10lJ3gd09_A9tbR6DcJ0KEZGRxFywuzp6YmwlbKgYGEgWZBe1jDp-KWV2huR8YBlnHWZQ7kwF5_bqjww4H6L91kIz9uxhRFf_OIB5ErC6Ql5QUWADP1WK0X5EwORrQIRRrwG1l15YCK21dqA3uV9yXw2UJ1JBitSuN25VEHSP_N1-OWnfgW7vAlvokmI5ugFomdIdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇭🇷
ترکیب رسمی کرواسی
⚽️
انگلیس
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/93994" target="_blank">📅 22:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93993">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcFOpP40v41qgNXAgjpPxx83E7jHosuG4kxMrjEqAgKQ4jHa-PlHVcriE3mJt7xU5KJveaUpTcITJHE0kTtQTdYFjc5FuH1VlWBCrCGmrNQO8Yr4UhpwG3vAG0U4Z7tgXv_6-rFY2Jh8fX1rBj4Wxz1JWrRqwCbAhqCLtaB9kN2Ft87cYDL-UMUVxqQG3-hOurql-7DUQqdfooEALwh73K7nuaGK3iG4N6yDYCN-CNcHz6yZEprB8MwytU2_VkUMQ2LZXRl8j9tvC_Mm9_v2Qm0-hf0lXkM-xipqB5S8HMahiCUOgl-tMl4-NK6x449x_MyJwk-wBHVXr2G3tVF9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو این توپ رو گل نکرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/93993" target="_blank">📅 22:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93992">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وااااااای کریس داشت میزدددد</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/93992" target="_blank">📅 22:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93991">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گلللل دوم پرتغال اما افساید</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/93991" target="_blank">📅 21:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93990">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سیلوا با کونسیسائو تعویض شد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/93990" target="_blank">📅 21:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93989">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بریم واسه شروع نیمه دوم</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/93989" target="_blank">📅 21:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93988">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkslZm-Sz5LEBVLmPp9AUAfkbRBIipUQersWOYYIMnqjQKPgs8_3iaTssoFj-aefBr3qfK3H0e03YmHAPXycQiMa8ipJq2lEbXXfYxsZR_OYc3QHSVKfvrvdZaQ9cG_I3Y7YDMMeKdMTjzC-1Q6ccVBzlZfzlyN_SXBT_OQwh2-OK8N9jjMkLq93Urt_LCFycyTCNGms83FV5YpJtisr880pafFrqPXeR9Huaf86ICmlEVDBNoJNDHREzkcLR7wxLJd0vB6_QmvCuPGO2g74jaBQbxWf4nCLkMgjQvmXfuyjBXS9x8QkCQBqufQQ-L8eFduKSfGSQNMV2ZZToKKszw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
وضعیت آمار بازی تو نیمه اول:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/93988" target="_blank">📅 21:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93987">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPHyljT0eDh4JftAicDB_hog-XI1n4ngdIBqkYpgb2YneOwGQ9DWOmsWHmeSZGNTIk39DIhsl5IQ0MFMFrp0XNALtHNYU99oJkQVXSrYNFAnR_OMmxr_BIVKwoD984MhAqk1lErKlxxKFUz9Ll-3d05K5D0pBqTVed7zDLaR9nO-kjX_w9s25Aum66Nmdi1Od8vYCeD7IFMrNJPFh0NywTdNw0Y7C8EYTxKyTmB3Syr8mcFhISiOSi1IR7HgFZnOKP5Pnv_0p7CQNkrDt71ACi_hBJioeavaIVBeniyXmu13CdT_qYCrr-lpt_l1TiT13Z66bkRmtxlo9MolhrvcBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی به قیافه من میخوره پرتغال رو قهرمان جام‌جهانی کنم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/93987" target="_blank">📅 21:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93983">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1K5VL2rALuBJlTvP5i1aA1la6ATNSQmcJ-6tnGYG9e9-m9z-w92P8aoKUGztLrE-jl_2fo95qTyCnSyOISZO8dkLdVSfPg6yIOPyrc5yyDnr4o7rIQlxqb7-VErIbX4Zlf-iM3BHJbvTEB0a9_5OLgNpXdt6MCZd7HhaiSVI-sq7ERI2wlXr8myB-wVfl4EtS8Gk0B1K-8wNFDf_AEneQaUoTitZARmtzNMrInSQ_3LCC4vhrSr_Zg5rtwzq6f9RilqUVoTjoCXJTyv1eakjpD0EyfFIc-Kbg_JITp2fjHFEa8ySwVAYgcfZA0emb5rnpTsAEMGk2WsLxqKMjJywQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6K2Cog3nUzPQSAjMC_IiW4KKIiIWZWlTaitm5l53JE7E4kKl-7o3dGvgzEfPCs6mpcWPwt-kue8xbE74dwLYP0mMfisKBZNqeDWHCgPrkdhMKLIOO0ULrNyxWBIQsxmpGWtiQlNd2ImDSwV6whSf7DCUBWlUfZvdMy7WHRFoAAtyj7KtG5cfB74llHIS-7HQJmrU7hX598v6Q-Fd6cVDSYMkkSqTXo9SK3o1HiOMOgj9SZdUFBKf-67AcchHKyru7_sSdSVSjGE4pMV6OIHPktLVNeXqsmaQrkcOxKSpZbjGp2ngKMrBmiNrLt8qzwCV2-0vi6qJfMH78ZesAttug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uswXIckOBsoJRsbDXW7gEy6htEpQ0vYFrfPWaQKCjIdXnNkWxPTW3ruCVcvIJBWGEc9qLMlvEuFo3vS_RtwXwmcvQl1dpmpTeMpcLzZrvhHRX2U651P2fHaqYcxiumBk2JPLygOMF8Ecvu0uedYP0MdXjXRC7gz4LBm3PKEgU51kI2g86jgN7J3hGQ36C_73RB_twBs__ILbxP88tQW_svLOGW5FyyNsxzsyvkFuAqF2jHrEWia3g8zdLfg4JGOveMz-LodziMswrlh_aeRlTGUypZZFsxckAzCQ0umdAlFY0FmuTz1KIHdH9S1QmTUuP1Of5UqNSTURpJj9CucLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rYndzJH792wy9zZ7snMpqsH2_ypdIu81eufkBOBauNMjJOyuLIGLpzuVN3dqJ8ZcQS9Qs_Y3amUlo3xmjL8ZnlBO8ILKU7SwQLyUa73jCAerspLt_PRAr1FnYxlmZE8r6aYUFHdlT9XBuXJ8AtyM0M7P116ZzS30sudZULpQ2_LG3qWkVfGf3i6sgZ9RgGWovCr27Jx27LTQf4ogTCUBZIx-4sJk0_Lxuk1yjp23yR3-LLnHoEdfC9RPPWUv7w6yOdeoRlHw2cHNapylIXQSG5wixsCBCZgaSmAH0BxbwzWfXR6Wgad6marVT4dM3E6u7GvjQidbsD0prRlGdVDREQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Vamos Portugal
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/93983" target="_blank">📅 21:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93982">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پایان نیمه اول بازی
🇵🇹
پرتغال 1 _ 1
🇨🇩
کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/93982" target="_blank">📅 21:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93981">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇨🇩
گل مساوی کنگو به پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/93981" target="_blank">📅 21:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93980">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مارتینز پدرسگ این چه سبکیه</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/93980" target="_blank">📅 21:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93978">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پشمام کنگو گل مساوی رو زد
😐
😂</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/93978" target="_blank">📅 21:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93977">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFZ_sNVGx9SoBlUES9DYFLG7lqAaqtb7OrcekCGvmLfE_B6DOKaAmYfHEriz3rSumLK17y0WEf3VWSwnbhoGCpqFXOcLMhLtr24vkH-ujfeVkfxjrCPqs6F3rjdy1RkUpHGvF86OYfnZqJH3rmciRp9yAo7sivQSGAqwSe_9ib5fsYddP0x4eTAjjnZdhJ4NSMQ8mcSe_pHZFMJEHBOxAqNht9HDvjWr0OWMTfDJRVXNlELGf1McfCyMAbRE6QnIpf5ijMJG_IGYlQs0IlzrJtj17pv93DUDL4Wj3SG6ESbYY1ArjmTMKoizAUVwhZemGzr88EQSrzJNxtzGx7_B2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر ژوتا تو استادیوم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/93977" target="_blank">📅 21:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93976">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3nkmlrgvVadNiFhbRmfYhKwmPpH-_jWEuqZaQMxIkYq5XJoE8Kh6AqIBu03XxXryW62g6co7CgcFfSZpHVeGf4El2ga0DwfT7eBZw2ra9gvfyJb1HdrKoQk7mflPMx2D1QGfsFvTDdnFGunoicKEfKYK20DcybHifhxNuO1wiGYQ9xoJIGzRc07zK6ucmA0AG15u_ydM6azTzjpmS51EuRycd839V2CFOGx1sxlvsAblMDwZLj1FA1HHBHXpEIex83Mp2bxQVd6Xoc3vv1cqpX7PxnWnvn4XkZL7da9ec4qeXAabUMCJk7-88iCjfzW3g8iII9r7DbYSyqbQ24bRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
فوری از آرشیوو وار:
تکل برناردو سیلوا قرمز مستقیم نداشت چون این حرکت به عنوان بازی خشن در نظر گرفته نمیشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/93976" target="_blank">📅 21:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93975">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St5d9ut3yW3Qk6A41U8wEujmJvNZ2qmvRhJzov0WASQ0pVOe73-49nz-NQA8GYlHGALR8wAxm2lWw92qLGEa-LFhnGEU8diGBmqPzMI98fc_JTTFPNkglS5EDSdj2MIpUf1xmi7IJf5blxaj34pcvHj9kecsiAZtQJSLCaE8adL9DXqgNXcV1QGYA-tcuqw8FMwKgPQbH0Srab0a9f17AQHU0nEHwcKxP-5PCqV6tDOCNlea2qKYItJOrVB7LA1NwIUJBrmUcUd_s26cr0ajF7JTvcyyOsAM27tLFGJzZM9kk78TH6z-W0NU5Kc3T5UFUHvmW1jp6fcMQUqoamMKNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتغال عزیز امشب زیر ۴ تا نمیزنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/93975" target="_blank">📅 20:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93974">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کارت زرد برای برناردو</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/93974" target="_blank">📅 20:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93973">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d7a7ea661d.mp4?token=h1vd58eKhHzo3dYXdVHTcp5jQHGCXujXExgKWktyIGYJ4De4-A1-0KWkQDRmmcTjOzN65tD8hMQzEjBWkLDuMVY9xXQVs0ZPr6fLysgkRpvJzvPrGzHIiRi4iLljlzuzirpLzimG4gOsKHPRWILt41aN-GHmrFJTBs4Txh82AokDTZqh1qjYxx7Ju4jA4h1ThDJkwHlQm6Y7HueBmS7MltRFlaL2hc7WEavOyP2uSZ3wwaWbih3WxkeUPj8JnJS8VzJ0GE0wB995WYc05936djz4Wz6WjJ9xXDDXUF1tWe-RBlnJJF90Yzj6DLaWo3BJFuaLwKsX15nKh4mMMXw98g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d7a7ea661d.mp4?token=h1vd58eKhHzo3dYXdVHTcp5jQHGCXujXExgKWktyIGYJ4De4-A1-0KWkQDRmmcTjOzN65tD8hMQzEjBWkLDuMVY9xXQVs0ZPr6fLysgkRpvJzvPrGzHIiRi4iLljlzuzirpLzimG4gOsKHPRWILt41aN-GHmrFJTBs4Txh82AokDTZqh1qjYxx7Ju4jA4h1ThDJkwHlQm6Y7HueBmS7MltRFlaL2hc7WEavOyP2uSZ3wwaWbih3WxkeUPj8JnJS8VzJ0GE0wB995WYc05936djz4Wz6WjJ9xXDDXUF1tWe-RBlnJJF90Yzj6DLaWo3BJFuaLwKsX15nKh4mMMXw98g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل اول پرتغال به کنگو توسط نوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/93973" target="_blank">📅 20:43 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
