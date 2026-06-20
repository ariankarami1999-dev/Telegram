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
<img src="https://cdn5.telesco.pe/file/b286uuEr2HykUh3sspM44DvyTD6wkTz7WRqs9UvE78b9WurSwgm2DRO_5fI-NKln9enchnkccnOAmFsZZt4lHg6nb98uWwQgxuXKb0SjOhC5rZLZlVGqNWbifBg7cW-uMLeDF6CIEDIfkOYWmuHit4T8oWfvpkYfTgae3HO4sRoxxclLNdzpGJdy0yCxIMKPyOGlhRashMCR5_gnVkSIb2xC3o9KpJDMOWbg_e0ytexBJhgpltLF2O1WtaRNLuYDK7Pi0TdelIK-PIksolR3HsD2jfiAcV8wnqNKaFE70XP0JulAf2bEbbi40z6ozSOh_8_yBi9hAD6gAJ_AmUCArg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 680K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 21:22:25</div>
<hr>

<div class="tg-post" id="msg-94734">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پایان نیمه اول؛
🇳🇱
هلند 2 - 0 سوئد
🇸🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/Futball180TV/94734" target="_blank">📅 21:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94733">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گلر هلند چه سوپره</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/Futball180TV/94733" target="_blank">📅 21:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94732">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">البته رد شدددددد</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/Futball180TV/94732" target="_blank">📅 21:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94731">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">البته رد شدددددد</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/Futball180TV/94731" target="_blank">📅 21:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94730">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سوئدددددد یکی زددددد</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/Futball180TV/94730" target="_blank">📅 21:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94729">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گلگلگاگگاگا</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/Futball180TV/94729" target="_blank">📅 21:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94728">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY44kEbFaZw8bl_EP7oOvlBuylWk9y7LW_q33iKXw848Pdvb7wgNiYGrXv7sbtGc_U8xLWIibLst76URi5vrdCG851yQFt2_VD2e-uOHGCHNQ_QLTmr9h3v626BuDxj66fEGz9yNHueKwpyJOPryi0j-T6-tEShc101MH9fPrbj_ztWaGlf0XdCPY-odKLu-dzDET1WfgWAsyFFjN_n_fVKaj2LXej4igWxqZgJQvevKaIebdEMglKgt87Wg4WWVT9VxO_X3kT702fxE_eeuIvk9cqynDhbdE9n73ZB4mrtT5fhj2giVA84M1j6M69rfEXB3FPas2ZJDegKeBsoslA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب شاهکاریه این
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/Futball180TV/94728" target="_blank">📅 21:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94727">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رفقا سلام و درود
اگه محبت کنید حدود چهار دقیقه زمان بذارید این چند سوال ساده پایان‌نامه رو پر کنید کمک بزرگیه.
شرط خاصی نداره. ایرانی باشید کافیه
💙
یک دنیا ممنون
https://survey.porsline.ir/s/ngmblc2l</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/Futball180TV/94727" target="_blank">📅 21:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94726">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">واااااای چیوووو از دست داد سوئدددد</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/Futball180TV/94726" target="_blank">📅 20:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94725">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dc96d2cae0.mp4?token=mZ7EMG_0AvuK6YPcW_GuhxMlMtS1TsiC16uJHpH0AD7qkA7O6SJS3DojYqbTBwDqEypHnNWoYg-AHjh0YlgM0gkCWw6bwNJZrwccOfxOHdAfY6rKAr321tLaeo-xVGZiVyOmRH5lbq3lEvK44fVmfTrkQJBglJ33IrVLRQOTKJJ0A2_WWWu4GCyXb8XnF6cv_ngTJLaT6or0UcYeKQ_LUwWG34mFCvJOhP-p7SVE4AFEgbsajbAWlvcxRUoeNDufoyKBieuqywQFDzXkRHfbzraWLUBFJnvgANV079R_sSpP5UTfGvIFVav3TYbXXszCDttStneCgS9R9MWgS7QwIYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dc96d2cae0.mp4?token=mZ7EMG_0AvuK6YPcW_GuhxMlMtS1TsiC16uJHpH0AD7qkA7O6SJS3DojYqbTBwDqEypHnNWoYg-AHjh0YlgM0gkCWw6bwNJZrwccOfxOHdAfY6rKAr321tLaeo-xVGZiVyOmRH5lbq3lEvK44fVmfTrkQJBglJ33IrVLRQOTKJJ0A2_WWWu4GCyXb8XnF6cv_ngTJLaT6or0UcYeKQ_LUwWG34mFCvJOhP-p7SVE4AFEgbsajbAWlvcxRUoeNDufoyKBieuqywQFDzXkRHfbzraWLUBFJnvgANV079R_sSpP5UTfGvIFVav3TYbXXszCDttStneCgS9R9MWgS7QwIYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل دوم هلند به سوئد با دبل بروبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/Futball180TV/94725" target="_blank">📅 20:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94724">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">عجب بازی ای شده
🔥
🔥</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/Futball180TV/94724" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94723">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دبل برووووووووبی</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/Futball180TV/94723" target="_blank">📅 20:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94722">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گلللللللللللل دوم هلند</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/Futball180TV/94722" target="_blank">📅 20:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94721">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f7b1bcc530.mp4?token=opSbVRD87l77ZPHDC2vOZXCkXPC3Liw_isD_usBuzsfm24jzvowikrzLMuxzTELcAvAr3Z8BEsKPZoO831X3dW3RlzTkQC854x4onzFk3WnJOKSg04p-RX1QaEktWOWzHhNmTCG70_h-3b0p_OdYashYkatC9z9-7mMMQfmjy4BtjKlf64TqAVvfJPP45hUgFKVEFrq09QdY144kWcIqk-lkK54CbJRNjI2UYlYPjXYJNaUys_mWMh-t0JKQbqxuGsyDX3tIo37CgNTR373vfBQBAFbMH9X2cup-apaWYkeRquAjkagMtEoNNGLOXlP-0FPUcxQ1lEaEAN7MxRqhj2inGVnidxnLhookNe3Bm8vbYY1ymBFJaBbq4mf8_qXNfcN_9RS-UJnGgFy-09V53J8wqwD9uNVePOFDwiGHdqJifztRthRcWShSW2k59wNk9W7dQ5f-RP4XzzvUWwgVXpGV6dYPJLifGiGI-4nL7OBXE3-06w8k39Fxx7NnrbVdNf7U-rVYRgzXJwr2yJCmYdLFasF_c_CsrWZpIocqIgbiB8gpewuZTOCIofSyJQN_fCsBMftTzqhLGTC81fs4UP0W7wsRB22qROZBb9JOE22c3s2PZsUJHfcEg0DrL67mHwsG30aRoeYtvI5YDm_BTy4zI7WcvXFmUL3Wm7cuheQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f7b1bcc530.mp4?token=opSbVRD87l77ZPHDC2vOZXCkXPC3Liw_isD_usBuzsfm24jzvowikrzLMuxzTELcAvAr3Z8BEsKPZoO831X3dW3RlzTkQC854x4onzFk3WnJOKSg04p-RX1QaEktWOWzHhNmTCG70_h-3b0p_OdYashYkatC9z9-7mMMQfmjy4BtjKlf64TqAVvfJPP45hUgFKVEFrq09QdY144kWcIqk-lkK54CbJRNjI2UYlYPjXYJNaUys_mWMh-t0JKQbqxuGsyDX3tIo37CgNTR373vfBQBAFbMH9X2cup-apaWYkeRquAjkagMtEoNNGLOXlP-0FPUcxQ1lEaEAN7MxRqhj2inGVnidxnLhookNe3Bm8vbYY1ymBFJaBbq4mf8_qXNfcN_9RS-UJnGgFy-09V53J8wqwD9uNVePOFDwiGHdqJifztRthRcWShSW2k59wNk9W7dQ5f-RP4XzzvUWwgVXpGV6dYPJLifGiGI-4nL7OBXE3-06w8k39Fxx7NnrbVdNf7U-rVYRgzXJwr2yJCmYdLFasF_c_CsrWZpIocqIgbiB8gpewuZTOCIofSyJQN_fCsBMftTzqhLGTC81fs4UP0W7wsRB22qROZBb9JOE22c3s2PZsUJHfcEg0DrL67mHwsG30aRoeYtvI5YDm_BTy4zI7WcvXFmUL3Wm7cuheQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل اول هلند به سوئد توسط برابی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/94721" target="_blank">📅 20:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94720">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چه موقعیتی داشت سوئد
بازی جذاب شروع شدههه</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/Futball180TV/94720" target="_blank">📅 20:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94719">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">برابی با پاس گل خاکپوررررر</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/Futball180TV/94719" target="_blank">📅 20:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94718">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گللللللل هلنددددد</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/94718" target="_blank">📅 20:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94717">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آغاز بازی هلند و سوئد</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/94717" target="_blank">📅 20:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94716">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b62de811.mp4?token=GNEti6SVHAef94iyRiB5ExGtPbyyfCN6a364b83fPnCo0gFw2JES2nJBtqA0zDTqVXuwJQtYau_K8ozXbBBuy4zULxo0yLjif16L_tttn3xvjX9WfbqRtiju7cmgsgHkeWgiZemedN8TCf8ka8fiLF7CZh6fJHiE0U7yF_wp8caA95e0sK79EPvfVJplXueFstft3PL_qzIeUcew2n9IuBXjhHECrwAldAb9pxj-9dm6LPkL49lLwqEIn2Y-P-bXGCuUDs7bh-ZaEhAUu3ME_v1ySKeuNY5525gCQGa9pujRcSdSfRi0LoZWG0Q4m0z2sVyymoZGAK25K_XtTunidA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b62de811.mp4?token=GNEti6SVHAef94iyRiB5ExGtPbyyfCN6a364b83fPnCo0gFw2JES2nJBtqA0zDTqVXuwJQtYau_K8ozXbBBuy4zULxo0yLjif16L_tttn3xvjX9WfbqRtiju7cmgsgHkeWgiZemedN8TCf8ka8fiLF7CZh6fJHiE0U7yF_wp8caA95e0sK79EPvfVJplXueFstft3PL_qzIeUcew2n9IuBXjhHECrwAldAb9pxj-9dm6LPkL49lLwqEIn2Y-P-bXGCuUDs7bh-ZaEhAUu3ME_v1ySKeuNY5525gCQGa9pujRcSdSfRi0LoZWG0Q4m0z2sVyymoZGAK25K_XtTunidA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان بازی دیشب آمریکا و استرالیا داور بازی دچار گرفتگی عضلانی شد. حالا با چه ترفندی به مسابقه برگشته باشه خوبه؟؟؟
آفرین
آب خیارشور...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/94716" target="_blank">📅 20:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94715">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xy_Xg4ahjD7sKBqWO28KE2UMObo9DxbI9sYvGSFISpaBrsypGpcZawuiRBBHXncCqbwTL0B3Nh7aVUnDlHzCdgC2O4vA0QxUQTWsBxwOJsuOWijVBw--eOyRb60OnwiCcft9Hxkao7dfgwKRNxGd8hZH9lb7NJID4lh7ZxVYZgF6gUwatkmJXHO71i0iSNvHjI3IJYKbhtXNthE6DjpFLyQxJQdVocmUrEeic0DB4Mc-ueiZs9JV0FoPb7s9HYLVOQKhZRW3oLzRklN0v15EuMxlDvuJRIEw_C4RDMiMFaODbu8HCt1P23Vf_vzRva7xMwPZBwHacRf1SeJ8X5OQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⁉️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایجک‌از آرسنال و رئال‌مادرید؟
🔴
شنیده می‌شود باشگاه تاتنهام با وستهام برای جذب متئوس فرناندز به توافق نهایی رسیده و طی روزهای آینده رسما اعلام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/94715" target="_blank">📅 20:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94713">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2b5xJSA5gkoJeggtLt4ONHOI0PuMgiOQVkw3qnIrO0KAaLSK_aji4g4hD02fQXttdXPnUP9ZkwhBxieFF7bsNUQSurLiY3hqrFsb9S-2P2D_nKnsSDfxyxxMcfavboSKPM5KMlc6SkVTe7g_E_c8wmctzbSFig_35eiQ92On7D9_IBZVgluVJf0JFBBBwXCiciqHhtRir6MGRZrUN9e2gnMl-lNwOUUhb5OfO4_-7HmMCxwnCDjgnx6RYpaMK3p6rKDdqPE7yXw9ucV-L15p9tz_HIFWNc1T4tp1aOCrnmTRpoSiPpqKTUhrODKRw-42aRhuqKeJ8ryMdQMRe54lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OLQ-shqA0Dk2DPkqXzsrf0Qo1rlqHIfWNrBPKbCjfAbBKPaidx_ogUXUr_3-kpDV9_L03I-LV9fjH83ZVgMVK6b6rupTdrO1v328xkfdLnakLgZnvCOEpqzxiMiHX12sYgV8q5VM6E1c1rp2cCat_Ajrjb7RqAtg19GPdu1mS5uPhljeHY05jhTN4jRhbvlW2xH1UZYciIs9Tkix998tkaTAwgsDec4MNJOxItmt55zRCTizPopjMz68u_ypToXW_EV9Fuw3C4YI5qIIv6s223HEd4Z9MNI1e31kD08K0r23JuC7a-W7TEYX5nhXk9qk-WwkXInI3iY45vArxwapuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هوادارای کریس به پیج مرحوم دیگو ژوتا هم حمله کردن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/Futball180TV/94713" target="_blank">📅 20:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94712">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/94712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/Futball180TV/94712" target="_blank">📅 20:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94711">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-yWqqXyTjVpl6cWRyY-SluWLwisvRelHifUUPf3IDewhxzTYPfkE4_6JuS1HnWzmmdE6mxIQpP_vGrCfUubNtymGzC09jfhe-ptNE2i1lp_E-AmbehJk_1l_dSIRYRiCiSNmlHDNwY6DD4USK1B1Eor7jEdTZGsjc1XF3F9D0FKuS48AsDNOorpPXoRvaOmn8DhWkS6RC_SlX9KksKAb6OOqpOlbMwnnWsHUiqMxzotx9G_MkXo_MWWKuQ0-H6BRpDZlFqncu_qCoOb2LokEH7CRgOzVyle0KQE94trqaHeFGOPtZQD1lKcDGm4tcd4ZhbSK6jYSFb9CWFOZBQeXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/Futball180TV/94711" target="_blank">📅 20:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94708">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXfDlLe93VZqerqgIBT1xNpHonawONt4LH4vxErLzCGDyMbQJ0IY3REElNjg7jZLxR_wUF1c0KvNyaECTLxEijsadr7N3DTuUyyrbCacSyoJ2-XCn_fmO7_PCoaS8QRNqYk1MuW8W7tpoYzklUgvoipK_4RKdpBxVdbnPIvvHRPYmWh8OBsx49-dA8Sf4NDI0DZYE2IQ1OIvKdIH6ch5LSMrrrJwLbmuBaaxN65wUS5xaPmwfDAykuJL1fZMC5EYMzj8OUa6ewKFbu9LHpC9nc4SL3Kdfjty783lxw_GOczSZHJ1U6XPr8nPXVuAQKbbPKqxaNYRYhpIQwlS7SNJfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فووووووری
؛ بیانیه رئال‌مادرید: تا این لحظه هیچ پیشنهادی برای مایکل اولیسه ارائه نکرده‌ایم و قصد وسوسه کردن این بازیکن را نداریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/94708" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94702">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aaff8cc8f.mp4?token=Y46e4seUxzrNxBwnFXpqn2O3JBS_zOtOUA_c7RXMyFV37HL9lqzS9dwpgMMZ_z6OEbQMXI5BMZQyoMYTHRPtHGy5Kcyn3oVbYor1m-faPHKA2ibWNOq3yQ7_eCBdnrS63AA-9MjaHrU0Ygt4GtaS_XZ49_U7F9sx1tDMgss8WCwl0OZ0pZ2TSqJkRNNoMZfSX6xkhDGqNlEPuYkZSRWEecro_wcE5yPxXsRiSwmZiZrIOrN6TDYf72--ySzWXHjoKIYxHwaZJfKBLgOh2cFGW9uGYmjZvxbrQ20S846KBpHk0TnoyrPwjasApbcWTPKiTymNdqC92osWQVsf7vd9Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aaff8cc8f.mp4?token=Y46e4seUxzrNxBwnFXpqn2O3JBS_zOtOUA_c7RXMyFV37HL9lqzS9dwpgMMZ_z6OEbQMXI5BMZQyoMYTHRPtHGy5Kcyn3oVbYor1m-faPHKA2ibWNOq3yQ7_eCBdnrS63AA-9MjaHrU0Ygt4GtaS_XZ49_U7F9sx1tDMgss8WCwl0OZ0pZ2TSqJkRNNoMZfSX6xkhDGqNlEPuYkZSRWEecro_wcE5yPxXsRiSwmZiZrIOrN6TDYf72--ySzWXHjoKIYxHwaZJfKBLgOh2cFGW9uGYmjZvxbrQ20S846KBpHk0TnoyrPwjasApbcWTPKiTymNdqC92osWQVsf7vd9Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شباهت اسم ژول‌کونده و امیرمهدی ژوله
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/94702" target="_blank">📅 19:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94701">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad258d1fb.mp4?token=ZNhw-YcQRODdEa7zG4pm_n-XJcoah1ykJrYAlMgaEtS3AJWDOsNkwprUFDjdqcbCjupI2RVDI4L4yXmQlG7Kr4Y_Hv2hP5wvCMuyENEcZpLC32Niyc8FQRaypiL2kNDXGxwGca6u6yIUsoBKWcOo1uYOl3KsEHsc5lTDE_bo7ydLTeY54zuLh2S3dEt8b9OGY0M9yRrWVtTxOhLEfvqTFG2ihN1_f_IpQhT1ILDp-ylLf5cS5u3CUli3MERXKv1MNhfeL2KXr1k0PhHzaBymagPRnhvx3Vi9zUFumwP61m9I_3b_lGX__DrPJMoF0CkVzxvF5PVah0WeY4TTss8s1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad258d1fb.mp4?token=ZNhw-YcQRODdEa7zG4pm_n-XJcoah1ykJrYAlMgaEtS3AJWDOsNkwprUFDjdqcbCjupI2RVDI4L4yXmQlG7Kr4Y_Hv2hP5wvCMuyENEcZpLC32Niyc8FQRaypiL2kNDXGxwGca6u6yIUsoBKWcOo1uYOl3KsEHsc5lTDE_bo7ydLTeY54zuLh2S3dEt8b9OGY0M9yRrWVtTxOhLEfvqTFG2ihN1_f_IpQhT1ILDp-ylLf5cS5u3CUli3MERXKv1MNhfeL2KXr1k0PhHzaBymagPRnhvx3Vi9zUFumwP61m9I_3b_lGX__DrPJMoF0CkVzxvF5PVah0WeY4TTss8s1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
صحبت‌های هروه‌رنار در رختکن تونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/94701" target="_blank">📅 19:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94698">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bM05B8QocGXAyRug3I3V8ujcPDmvS_shUkA__HHbXo_vfvMCAqZnEKmDOXO_GApgKXGk9YI3ac-L6Lo1Ravcd3CrA8xxbGyB5j9MgiifYepqUJK6NLq0KW13s8_Zmv5xvZx_VhWfZkiiUmWIUpwkZ1HJLmGOlmYvZ1R1Gpi5TM_9Vr8o7GcEmaxs9GNhZlHvbqZJkkI9VjAWbq-M4ppCM3mg7KbjJutUJb9NHTz6n0ElKAZG2aQB2vrXFUFnx0xtLOaF7JWqnwBc54q6Ont0HudOPV4hPCFAw3Nji24W2QaOrER3m-lyzY-7rpXAV-UYnZuUVKbJEXG7FCB8YCG4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇪
🆚
🇳🇱
🗓️
۳۰ خرداد
⏰
۲۰:۳۰
سوئد
🆚
هلند
📌
نبرد دو قدرت فوتبال اروپا برای صدرنشینی گروه
؛
جایی که هر دو تیم می‌دانند نتیجه این مسابقه می‌تواند مسیر صعود و حتی جایگاه نهایی آن‌ها در جدول را مشخص کند.
⚽
🔥
هلند، یکی از مدعیان سنتی فوتبال اروپا که پس از توقف غیرمنتظره مقابل ژاپن در هفته نخست، حالا برای جبران امتیازات از دست رفته و بازگشت به کورس صدرنشینی به میدان می‌آید در مقابل سوئد، تیمی که با پیروزی پرگل برابر تونس شروعی مقتدرانه در جام جهانی داشت و اکنون می‌داند با عبور از هلند، صعودش به مرحله بعد را تا حد زیادی تضمین خواهد کرد.
🚀
⚡️
آیا هلند می‌تواند پس از لغزش هفته نخست، قدرت واقعی خود را نشان دهد؟
یا سوئد با عبور از یکی از مدعیان گروه، یک گام بزرگ به سوی مرحله حذفی برمی‌دارد؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/94698" target="_blank">📅 19:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94694">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CrXQFNHdS35nJJzUjyqx4gPwmgksjW93aaYtyuiP6rFDjTClbW35UcEZYPEe8FT09z4_NHgrmJM-Si1VUWbxDh9yRF0pGdxc_GMlTxyP3-HhXxrcnB5d8_7jldm8QmfNYB1aTJ4yiaM9W11NFRydIKRZb1oaL390WGmbWChvJzYa5pJaP346sOU1znB4B-MIK9GQ6ePErhzitP2KHNgJDOJa8ZQEKe-GLMO1xg692zcFgEBvf0WqJuDuNdjXHXT74lZj0aIxdz-_SZYQmK4L72108_fCXnGoSYSsa3HO5OWfFR3NdV1_H4BU-UHrkGC4glOeCNboXRkqw8BlUFEuJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEF6C0e_lM7bUm8tpK-Ev1w7Ew_kt2gg3S5b8A5w-AfWInKLOiOGP8rwP4TtawXtorvvJKfzBKjRtMjoJXgt0F_uuWkshuq__ClkG74hqSCezm8aDxBd9L8C4gj8T-vSM0s0_uhkPraEGs9rymNiuT-nlKLw1eave36q1JvhRKgFzGwc69uGIWolNIpybInwmj_AcIMNTyfiiaC2WAqHoJXKKK_UQdlE0Z4KkpifVcADkvN66AwBfJlCHM8BUExmxQgjeAEKW9ELh_gLtWvqXG2N3iIJTQw_OZ6uHeTSrPGZtseqnm0sWO_-8oo5EIlnRlkxZYtmq_UWthKIW9jFQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CJI5REtV8IKJRoNEGonxRhPNniR076_6U_9JBR5lMoun_W4X3XwNfr8XxpqUYc16mO-jhNlQTslKwRXvn-0mB8HPx36FjipLcWueinBCin2hW9x15DDMa7ZaAmxSYx_meWXvGgSMCX5o2YfuzVq5bBnzDh-8pqsc3yj62tOfiW6F3Dshz4tb3NZYpV3Y0E_fPoXwsxigrREk-SKnrfzy8nm-gUUBdZdO96igjYcSM9GLKaw3TsjZ5r51yXoNIRV6AGW99oto0QflzmfOVhX3b15l7_QewO0KQYPAqeOaLXHZ_dR5f3TlHqU6noaN2HIiKIeNuQJRlIiABH6qW59K4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TVmtmetuXbkkhFbR_ZVnuL6RBAyrxY85xAbor5Atxx2G4t-2sIrQHE37bQ2C1AhTPY2jpaoHB-oC8BX0fY3jVoA5lEmM01UnVKZQbr8dUKuZPPoPguNn5hEvv7f2m8AUn5vdDDSM69jZTXyI35T4ebyp9NAwWp6eV_8CsMmcNXSpYgyzUUB0dscVMY3K6a3y500gLH9YkgDUdz1dxjW3PwfGwxRI3ISqU0N1pdwTrQti-3EFyH9UQxlYYp6wMLv6LlVYCm9NqWGmP56ye6o7UfILRTNTSOFNLKB-8YFFamr-3KktzcIMiUWOMy5Ic3lsaKk7uZbeLSg3Pwg_BfJWOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تیم ملی چند ستاره فوتبال در یک جهان موازی
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/94694" target="_blank">📅 19:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94693">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPy9AP02UUZTnsz4NjL76sBRShwz3NVlC6oLEBECq0Q9oG34wnPpd9NV3E9Sf1HkC7rpT7VQNLEj_U9EXeR4G7H-WprBszaw-kCt3NK17QaHQXd15qVLjqtVf1w3FINZmhVrR7mNEpbuF6HCN-jqt9YgI193HEe7q8SkiQwlUIx4lAjaUSY8ZkBcSuOi0aI80PaIl3KM7FYh7YEc1s7vb6jl0q05AwjuX9cRZf3F8ROZAzAJ64jBXCccUVc8F1ZCsQ7iILMRU2_gGpnKnp3aRfiRHwP5zZnBqb8a0r_Vvmlm4uGvu0ybn2yeG7L4KB20ZMUVD1prxLK6q1uKd05D0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
ترکیب اصلی هلند مقابل سوئد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94693" target="_blank">📅 19:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94692">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNwpYhVBM2n4eqweqoltXGDh9lP789q2uU-qFJDppQSG4T-X95lh79oYx6Z_5BWF2hwLT6fFb8cP0cXZZ5wH38f5kQlxOEtHFovTYuduWZBSDhprZXRezbvfXzNT1AG28l-lwpH6RxkLE3Pj43hLafpSIsW0d07lQi0Xn_NtZr9hzr-SPxuqPFXwpw70Z9T1JMYzFbmO7lt03MqJcGLAbRd2y3X34PK7_FA2PmZvVIqEZS14pIuT4XB0j4957oaRt9fPVtxlnBNPWn55Ee6YPa5vkPHYUipyeh0Z6Dk6XM2qAZXHpMQbkQGFlipV_z7lfVHhD6EZkHBN5JCEbLBwaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
ترکیب اصلی هلند مقابل سوئد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/94692" target="_blank">📅 19:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94691">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juuuZYgbL1G9_Uq4ZVtPapAur0W6iJh0b3sFFune1mDvCUZvgu9Gk2g5N0DKfzdueF7JT73ZDxkO8BjaXgMT0PTvNgANaauEHXuwrHCwoqS9I95kFB8cXS-l5dkwfRvD6HJszqXLFqjN8pkLMxgKJkukYP02T7iYF6MNHcjVpRPxUywetEAYH9VsDaqnEc7O8Gr56SY51DaWPGq3ugQRClG0_F3fbaAaXy-T7NZunqevY-eYPogeSGPdRb2a2sNyaMkTNkjSYncyQc07AltUK6QIkylYeSoJTRgy0WY10fQlCHWKM1CWTiSkg42vzQ1v-WSA6VkR2whD8x5iWOq__w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
هوادارای هلند قبل از دیدار با سوئد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/94691" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94690">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpdY5HAP-MTiqvuMkMZk1i3PMl5KqwoXgvAgf9IzdUR7DBhrOgfWsC7LQmHz4COqASZArb1NaI61F8gDHLb85xni5ODKKuoA2MCA9GmRjnoXECMgCYSIYVL-80B9UuRMdHJFuZiBXwwAwq7NL8BLCUSP8gjdtnIq34q3yoEZ7cAw-jxLGp7nwnlwg9dnZAojuM-0XvQiL1AlNE3BctKuRhoke4EQ_VyrCA5vNF1Nb7ppq9T-W2lWfpnmU9zdC-lmtmgVofNEGrJYjEhI1YwvTmCHSCWKc6yIhVB97yvlU89Uas1co_XItkPWlGEIyqTaQ2e0AchPSedsRGmo4AD6Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در فینال با چه کسی روبرو خواهید شد؟
🎙
نیمار:
اسپانیا.
🇪🇸
🇧🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/94690" target="_blank">📅 18:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94689">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8aUjfqleeTEkBwuUArcQC5jHt-JpV6ekZpvXnpNRlTX2PboM9vzbJP0WFkjriH4yLdnEBc4uuf4JQSGEBd3GeYaX1J5WFzbHGChtKjqOtyp-tssNd5vCsiRiC5b2cZBA7NK0lPiNiOblanyLHNkJINcqeA6cN7mVM3YMdn-57RYMIxscxS9MAKnlzIBP56nBeJK5aHzM4zwPmkMSQyP-e50xuPlIWCDHOxGkfBfDg3V_dLNf3qv6oADipiYtNX6IQHYgM1LLrVk_YoK0ZcGehbjWleTvGf5mpkhtCea3RXmQWmfTinrWcrBu7qODi0AQzi_VJen1z3t0ODcH68Ixg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یک درصد هم نیازی به تست DNA نیست...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/94689" target="_blank">📅 18:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94688">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgUM_YXzTrIbppoM4xVqtuKjtfUKWbFMW4kboMJUTdTHy6137vRRemk7HIQOUUZXVgX162CElHs2GZ-Yki_SGlP0l6fg6nqzhYBOx2ZlIxuPgg2-3zW7dArEGU9V8Y5RD6hujWTcnlMJFdvqWvJ7mhORCC0Q6O5qoF5m9ubHUdUzomqMg26PbmcFUDPUERGKI8U8Rz30ooXFcAKFOGqQQKOT34JQOmXMyrZM9G62fc6-cZkH69z1a77AP99xB510lbrkavE_ukszOdtkAd1kiYZ1LvDp-1K0TwIqaXTGZtAosZPVPu9Jkpywdv1HDA0Bq7wgCQNcqrWwn3dG42bFDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇺🇿
هوادار جذاب ازبکستانی حاضر در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/94688" target="_blank">📅 18:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94687">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsNWAo4Y3No8SkaJuN2iXh92_d4XFVLGp0DLCm4lrHEIfNkUi6FITVxpAXGn9SU7uut-jcepW0qRE4c36qHfZq9gPpSKtKfnqKtsCW-STsCf1u0Rip_SaYtwV_g0NP7P_9peMNIjRcRflaMBwYXU_4rvO1b-SrDQT8-7M0THD0z8CdDkJ7kvIBpJ8Uk_y3pUiis33G4QsoA2ZToizlEdnW6YeqKeZgik1hB2lQZCoZIiW8CPAmHHTRfC_VwEQpE-pJbUGETZMiF2cvCvJZp-xAcD48LujsTeQra2y0foeaiBHDHSk82xrhhnCdkPXRiFmCyHZMBUDv-gwlJ0Xt0Jyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇳
🇯🇵
دیدار تونس و ژاپن هزارمین بازی در تاریخ جام جهانی خواهد بود و داور مسابقه پیراهن ویژه ای به این مناسبت بر تن خواهد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/94687" target="_blank">📅 18:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94686">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9f6fcf9f4.mp4?token=Ud5RS7Qy9Dt3d8Zt8qk8fvutdULP9aJZEaKR4vpyzmkckA2GjuaOlJviOG6I_GY2TGIrL1lQdP1X8bh19TN2ZJD2-9vQLmXdNh-wK5gCZC_7jyJKdm1N5cHuEqRCZbvsdaG9ikN4b618SWy280EJIs2j8N74s_lFXMs9ijDL1-PRziF9GNcJwONll-J5e5grGnR9QhO_sf5YVAP3_WF-MucuIu-_Gj6SjEWlnGMifr90U7IoaC62H3nrK_mnznpBW1Qf1iPpNR0s9hwAX6PdPQHew09xoWNfmVEqpYD77oQO7V2sfmiwGmo8h3z7lGgcwsdzc2Q8osMj8BFdZIDUdHrwu4nSa7ncuAz3Qzlv5DAasZsD7dv6BgYEBHdkm4kEMoyb4rufCH6kyIJemKfeSNcneaGt4eb9wlBDVC1lmpoxPzUsTssepBo6Jd7mrSMmh8ULv7G2C7IGptMlxH4oR_CFTLl0lX_5sHaMT1Y9ZnCpyUQV5k1cj3jAtn1HQFCWxYYKLzWikKwBGHLAV-oT4EYIbIbBTjqpywsMoG3I8qGRaU-R6Wyk5B279EdKiCajt5w4cVE2KWKDo8VbZ3Z7pSTlI1nHB-8MsydnBBdmPZA_36u15j3XQ3R_ypWy6b_ZfGxxC6UauiYs0KbPftJ_E5cc9oDJv-S5gMSIw45Al3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9f6fcf9f4.mp4?token=Ud5RS7Qy9Dt3d8Zt8qk8fvutdULP9aJZEaKR4vpyzmkckA2GjuaOlJviOG6I_GY2TGIrL1lQdP1X8bh19TN2ZJD2-9vQLmXdNh-wK5gCZC_7jyJKdm1N5cHuEqRCZbvsdaG9ikN4b618SWy280EJIs2j8N74s_lFXMs9ijDL1-PRziF9GNcJwONll-J5e5grGnR9QhO_sf5YVAP3_WF-MucuIu-_Gj6SjEWlnGMifr90U7IoaC62H3nrK_mnznpBW1Qf1iPpNR0s9hwAX6PdPQHew09xoWNfmVEqpYD77oQO7V2sfmiwGmo8h3z7lGgcwsdzc2Q8osMj8BFdZIDUdHrwu4nSa7ncuAz3Qzlv5DAasZsD7dv6BgYEBHdkm4kEMoyb4rufCH6kyIJemKfeSNcneaGt4eb9wlBDVC1lmpoxPzUsTssepBo6Jd7mrSMmh8ULv7G2C7IGptMlxH4oR_CFTLl0lX_5sHaMT1Y9ZnCpyUQV5k1cj3jAtn1HQFCWxYYKLzWikKwBGHLAV-oT4EYIbIbBTjqpywsMoG3I8qGRaU-R6Wyk5B279EdKiCajt5w4cVE2KWKDo8VbZ3Z7pSTlI1nHB-8MsydnBBdmPZA_36u15j3XQ3R_ypWy6b_ZfGxxC6UauiYs0KbPftJ_E5cc9oDJv-S5gMSIw45Al3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇺🇸
آمریکایی جماعت اینجوری لب‌ساحل کنار زیدش بازی فوتبال کشورشو میبینه
😮‍💨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94686" target="_blank">📅 18:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94684">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
پاکستان: مذاکرات فنی ایران و آمریکا فردا در سوئیس برگزار می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94684" target="_blank">📅 17:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94683">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c3e66478.mp4?token=iITPCwIDHGTVDZIDojY1gLlj5A__llEGsEp_Sotqiect71lE_3cgCybD646Y8MSR06tGLk4dVEoVTu8bpNGKeUnFBq-sTnHb1U-Jyc7EwKT1LsvTUGJlbXId9U57Q20UDjQ4WX30jhnkxquEmQ6sULcwlV4K7K0vyfTOO_I7DedbTBKnzfiEUsor4G5qTiVZvkN3YLxRPov1dMOALHG3s4WTlgkB0lqV1L6TpDV4GXtSpe7UxX_vqcoKs_5_qn4NQpEa02ws3lcLpUlaXjRY6kxvi-JIobxU4wWHf9xrnsKvR7ilfyCufcHTv2a31tdCVIMzGQ4kWf-JUiqtqpBauw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c3e66478.mp4?token=iITPCwIDHGTVDZIDojY1gLlj5A__llEGsEp_Sotqiect71lE_3cgCybD646Y8MSR06tGLk4dVEoVTu8bpNGKeUnFBq-sTnHb1U-Jyc7EwKT1LsvTUGJlbXId9U57Q20UDjQ4WX30jhnkxquEmQ6sULcwlV4K7K0vyfTOO_I7DedbTBKnzfiEUsor4G5qTiVZvkN3YLxRPov1dMOALHG3s4WTlgkB0lqV1L6TpDV4GXtSpe7UxX_vqcoKs_5_qn4NQpEa02ws3lcLpUlaXjRY6kxvi-JIobxU4wWHf9xrnsKvR7ilfyCufcHTv2a31tdCVIMzGQ4kWf-JUiqtqpBauw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
آلمان عزیز امشب بازی داره
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/94683" target="_blank">📅 17:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94682">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea2896bfd.mp4?token=hqiOh6qAinYW-wNWvC6QLXUY-i4hiExA0qB54_JmdwZpfUAjk4dbMZ0z3IJSFfRLyZpml6mcxVH3RZeqSrjKZRq8sxa0_Q9svhmVsvVaYYe8AUgmMAben2dl8NzZEIF7f-j5uvNWQFIFwit2WAtzaZI21j9czFtwVoF9PK3B8bump0FSWAeihRkMjRwZIFkPoFbU9EW5IXGnk-WkX08-701K6IraiMNs2CMm3cwJiGGUXmmyQcK43dmxiSAZdPOArgsXfGRFu1N3deDpZPCf0WLXr5gGBqPYnpa-Rnkm1ttPhUBvv3YQsSqh2Fsolpaph621QwnWSNnbN5U2SLgV6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea2896bfd.mp4?token=hqiOh6qAinYW-wNWvC6QLXUY-i4hiExA0qB54_JmdwZpfUAjk4dbMZ0z3IJSFfRLyZpml6mcxVH3RZeqSrjKZRq8sxa0_Q9svhmVsvVaYYe8AUgmMAben2dl8NzZEIF7f-j5uvNWQFIFwit2WAtzaZI21j9czFtwVoF9PK3B8bump0FSWAeihRkMjRwZIFkPoFbU9EW5IXGnk-WkX08-701K6IraiMNs2CMm3cwJiGGUXmmyQcK43dmxiSAZdPOArgsXfGRFu1N3deDpZPCf0WLXr5gGBqPYnpa-Rnkm1ttPhUBvv3YQsSqh2Fsolpaph621QwnWSNnbN5U2SLgV6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابوطالب‌خطاب به رونالدو: داداش مگه ۲ سالته
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94682" target="_blank">📅 17:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94681">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40d0e5cc13.mp4?token=SZ6fnjrBlha1JZZeJfjpr31KtJTSCVO7IhR5uHL_c4zlBqfenol-qyla4v5Q5ZrRO3kF-wFKZL1rb65zbD_grKNJ3BvNH-VHkg35Tpd2rGMVuJYXI41iML-IjEQPxPmtWPK8QYIa0OmlD1ScBIg74Bx_7gIIxDd97pjV3-9UGHDro9XvMN_j8QDSMCIhGVsku7DopLOucq7LbqxdYX269fzyStT_150VKANOUO9PzQfp40SSt7OqEMdlidsGPDyLJPjcIIgylwblhsDA89wVP60iWZ0PzkmmSqz61y_9E3h-tSV_qa4ZC9UZhH_RVj8xUd-mLHDHwwplAOI2eLm_YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40d0e5cc13.mp4?token=SZ6fnjrBlha1JZZeJfjpr31KtJTSCVO7IhR5uHL_c4zlBqfenol-qyla4v5Q5ZrRO3kF-wFKZL1rb65zbD_grKNJ3BvNH-VHkg35Tpd2rGMVuJYXI41iML-IjEQPxPmtWPK8QYIa0OmlD1ScBIg74Bx_7gIIxDd97pjV3-9UGHDro9XvMN_j8QDSMCIhGVsku7DopLOucq7LbqxdYX269fzyStT_150VKANOUO9PzQfp40SSt7OqEMdlidsGPDyLJPjcIIgylwblhsDA89wVP60iWZ0PzkmmSqz61y_9E3h-tSV_qa4ZC9UZhH_RVj8xUd-mLHDHwwplAOI2eLm_YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاشیا رو ببین نعمت خدا رو چجوری حیف و میل میکنن
😢
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/94681" target="_blank">📅 17:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94680">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vX75PdT0AH9mXt_HJRjAXqjTsO18kXcwY1fjfVUP97A96FOj8rLustSGjlQW1sJxPAhJMFlZh3EO5k8WUw9gca9MxRu7lofCMnp0JSo9LCTSGCcdjmJlSxaaUzpXGgisApoxH1u47f_HYjYA2qXQCnzdwe2E873YytJFVD6E0C0hX9-GV6zlHWvdNNJyY0a-FwjCpPJxlkSSCHSkWQUXtibj_imUslixJS-wTDLFF9v0kplfVyh4VYYqO_pdifDRGKYDWNveJC4Ejh1LtB3ioiipTDMBpetcOleFJh37OntB1196rqyQyhWBhKMGpwtEQGbHZdqB4l-EkQIwAUJICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مارکا:
بنجامین ششکو گزینه جایگزین بارسلونا در صورت شکست در پروژه آلوارز در تابستان امسال است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/94680" target="_blank">📅 17:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94679">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a1e82acc.mp4?token=Qxj2AINY-qDP_0QkW8dmeCqMlR429gkRsIcjuExQr18-5NIZNRfbIrVzwpi6Rt5itL0BrMrVNyh7YyUw0Ci1h-V6QSqYURk53i6LY7Bs5a62YA7AOQLhvGhxult3N6-Io_G9M2-d1zbWNfFU86ZqYCWu5-K-4VtON5MWRzhXoEBciBkZlT_-D6zBml0XbMPq1MoexZ8JbTHHT0qpJZuXmI2TavxejDe4Xq5IenCg2q5geI-HASi7FT1K_pZQ0kioEUkZaXwyE0t7WKBOjH7CRVqlfevtn0b0JeaLGCy1TWezf2yxch6Mbzfe98AlB7p13f6mqMx3QBJMhddZpIJ0LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a1e82acc.mp4?token=Qxj2AINY-qDP_0QkW8dmeCqMlR429gkRsIcjuExQr18-5NIZNRfbIrVzwpi6Rt5itL0BrMrVNyh7YyUw0Ci1h-V6QSqYURk53i6LY7Bs5a62YA7AOQLhvGhxult3N6-Io_G9M2-d1zbWNfFU86ZqYCWu5-K-4VtON5MWRzhXoEBciBkZlT_-D6zBml0XbMPq1MoexZ8JbTHHT0qpJZuXmI2TavxejDe4Xq5IenCg2q5geI-HASi7FT1K_pZQ0kioEUkZaXwyE0t7WKBOjH7CRVqlfevtn0b0JeaLGCy1TWezf2yxch6Mbzfe98AlB7p13f6mqMx3QBJMhddZpIJ0LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🏆
واکنش تونی کروس به حواشی خطای مسی مقابل الجزایر:
"این احتمال وجود داره که اگه یه بازیکن دیگه تو همین موقعیت بود، کارت قرمز می‌گرفت... یعنی دقیقاً تو همین شرایط. حالا بذار یه چیزی بگم که شاید خیلی‌ها ازم شاکی بشن هرچند فکر کنم همین الانشم شاکی‌ان! ولی به نظر من مشکلی نداره..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94679" target="_blank">📅 17:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94678">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ba1b9f67.mp4?token=Mlq-CSFekGgaJ8jBH4xaeiHCOybgw6oMhngu6Ks2Phz39JlDPJnZ2WAFHeWSL8QPT18cIE7qK3qM0x_WHbpx4bqWxOs4zqIufU1ZIZCS5qF2CFGLHLvSflEERUfvd8OPSrE_eaVRO3dd6UhfyyH0wWLC52N_I0EZuz9UO25D4EwzmIMQMCkA07itS_0pSQENLm49EnBGr0_W4SjGHdK9cXng9oNQm6xYpLQdCrGHhCckd4hh1VvFbkLDF0-3akL5m5okrZz85mwTYTPAWfAuTiRj1uLn9BSUU4UgLljyGYAF2kSJPq6qGfi2mdOGe29J7Zj7Q2ieoAUJbFJKBiMzbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ba1b9f67.mp4?token=Mlq-CSFekGgaJ8jBH4xaeiHCOybgw6oMhngu6Ks2Phz39JlDPJnZ2WAFHeWSL8QPT18cIE7qK3qM0x_WHbpx4bqWxOs4zqIufU1ZIZCS5qF2CFGLHLvSflEERUfvd8OPSrE_eaVRO3dd6UhfyyH0wWLC52N_I0EZuz9UO25D4EwzmIMQMCkA07itS_0pSQENLm49EnBGr0_W4SjGHdK9cXng9oNQm6xYpLQdCrGHhCckd4hh1VvFbkLDF0-3akL5m5okrZz85mwTYTPAWfAuTiRj1uLn9BSUU4UgLljyGYAF2kSJPq6qGfi2mdOGe29J7Zj7Q2ieoAUJbFJKBiMzbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
روایت عجیب یک هوادار فوتبال از رفتار زشت مدیران دزد ایران‌خودرو بعد جام‌جهانی روسیه!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94678" target="_blank">📅 17:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94674">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d6AuiY3Oz2hdDdXlLlazt1JsSLkrLgf_7EQkQgkWUUG9H_GayfkigLEO8MweOi8m4Z3lHZbdSHYXsKGlgOLYD_wWGpAl3Yj268PCLOkdDMI2t9YyQF1Zkdt20e4LVO-l5GQmmshqr8GAdpHiU41rGXJ1ZPApExkoMGCHePGLSahhhL0dR4jbz4jFy1R4sbeyb80XmDf4MUv-LAjk-86JxwFhZTZtus6MnQJMpR4tqboOBPM2suphPWkNfYeQhY61u6rInVDSYXmGVhkNXhDROivjq2vox70_WwCBZhX20oRVW4r6ncm1Ip58Mpzil0NHIwojCiOvD7HbVrqa3kOo_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IveCkmjXkm430fwpMdIL9EEEB_4B3_avhgnKUl_WSj4wfpSDnHxyHDFjcLzRzlOuvdXXqnxRDvfD_NC_4JBQZcjuv3x9sxTcXlc_HbSPAIBnabxl8R0WQZLwpTm1khCv6mAXJwoSGS0oOUJhAzY2jbZ3ue0Fj0EfQDHplJm4tXQ1XibjptvZMtO7u2b4mYNJEn25tRPGbTjoLCIoWeqPr04N29EK1Iic7IjweueygGsMwpcVRFw1bHM8FqGUrwvI4Uyy2GAc6pVb_z3Nd02wxdKX22Pi5uuLWat3dYiH5yGOvnp_rLPdjGkdx3pvlQhC_le-_DopyD88uRLUHqQaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FxIUAM57xcTtQgltI1EA110xiq5R4PsRTDx_y7e2odXDRJMHQlGsUwBssU2ltqhH_L8RR7RgkJoyQhMQeo4nOVwm3sBguV6VBo1MA7BBP7pn8h8_t1ujFMLqLdB82Jl1A7VcHUf9cQPm_OZcdMp3naNKxtVuUzRVG9h2Tlt1Ppaej5lrxnYDAmYyaSmd21FhShdwgsftY7gcwooxGiMCeH-TcQNhtsx-Oq9SLL_JEqxa3Uk4T37JANFuri8qXYLyp5mG2V9Nb40bU0vDjH5uBJ93V_-S1P888VflabmnfV5PvZIyasctFWnL9N-omY1Z4Z-EwaiRRLgMhtUagtKtAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5Cp6jFrdX6Qku6px4Fbb6ItHuj-fMpr6QCpSYSAZnc99PEAK5rlhwuWZr-uB9cHsRDB-P32C6oaX23s5GzuZxrRXKsnFs6kZ6wkSYs6-nr-uiuSgdb1GYyDgyNa2swcb0CSb1uC3BIIUAIzVO-RXeaA1XCsyYX1of9SmHztl--N7iwosdKDjJ4xTkD_yd_9fvYutYW9KPDVsHX0gcUzoBM1uktpixCZPTO_AFReTIdREpD-ICNpUWnpq4C83vsT4Lzw86WgX7Rg5tBcStQENJHBlvfKQMCyqJIy4pt1ANzq0d3QNnGPTkacnT41_kWvz-8pWKtGLDBdAklTt_ZoCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌐
اولین پست‌های لیونل مسی تو اینستاگرام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/94674" target="_blank">📅 16:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94673">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
فوووووری؛ طبق اعلام قرارگاه مرکزی خاتم‌الانبیا با توجه به حملات اسرائیل به لبنان، تنگه هرمز بسته شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94673" target="_blank">📅 16:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94672">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f2f6a0fd.mp4?token=C9PLBKwJ9gB_YW33bmEhxuxog85CpzOzdS8ok7lCGhZP7PkXF88q_Owmu4MHPIJS0di2-1eLalp7sE5g5cfiLcF1d5ri2nyA5-H-ZOwBH-XONdJHgW6tEUmDqzrp5-MbTxi9SMQWfCi9j74CIMTua-h1jTXE1J3_TKePnHXIrRWQK1Nq9XUuIZlY7wlygpSRv2csO-xNmXHOn4yTW61rCpbx9_DugxxzL41CqyzT0mTKX-6SJVbV3cXSGDBDSKMvB6BADexcED6NylOvI9Th7V4rSTWv8KpNzV74ZMNmgBMnckKYV7FK-S-t6iy2BCpN9wup_0rrQXU255e4xBENCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f2f6a0fd.mp4?token=C9PLBKwJ9gB_YW33bmEhxuxog85CpzOzdS8ok7lCGhZP7PkXF88q_Owmu4MHPIJS0di2-1eLalp7sE5g5cfiLcF1d5ri2nyA5-H-ZOwBH-XONdJHgW6tEUmDqzrp5-MbTxi9SMQWfCi9j74CIMTua-h1jTXE1J3_TKePnHXIrRWQK1Nq9XUuIZlY7wlygpSRv2csO-xNmXHOn4yTW61rCpbx9_DugxxzL41CqyzT0mTKX-6SJVbV3cXSGDBDSKMvB6BADexcED6NylOvI9Th7V4rSTWv8KpNzV74ZMNmgBMnckKYV7FK-S-t6iy2BCpN9wup_0rrQXU255e4xBENCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
🇺🇸
ذوق‌زدگی این‌بانوی آمریکایی وقتی کراششو دیشب وسط بازی دید:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94672" target="_blank">📅 16:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94671">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEENWu9ZfVG86dpHInLDoKTkqAc-oeQ11qllJYpe0DbZTu5sjoTkycnBPet_lXQIv7lym1vvgeouoVl95w-PEscbt-st2kd0X-vtnck6Zx4L0XP56M2f-0JSNFVmy0m0ZcbX4uEab6zKeulSMsrck7cE_VJbMIbjkxRg2y4MK0IiWXt0K361mb4JrZy2JmC1seifWTz6vxCOChr6ryz1T8cKHnmCdnW3uaLiJ35M6i-Bbf6PumuLMJuJh4BMLnDtkyZJjYrfIW9BC2WMmiWExtp5uHmf5W4hDJdFjJLJVD0LTisHO-cOzSpXnCjUUco9mnk2JKhEAMDu9kkaVSTIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
کول‌پالمر و زیدی تو تعطیلات؛ ایشون پیشاپیش توپ طلا رو برده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/94671" target="_blank">📅 16:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94670">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b719b1cac.mp4?token=mUmC2e0bZmnP6yLisLofflsorvt5beeszOU-eONRQ3LPe9FbRtJJztVcCz0H5WyHk7o-QkkDKus6beAocF4qe0bUaKC2aQYsDmy0LK_iM1pdonUUMZvNpcDSqfJ4uCUNqlGXxAsoZI8wEAYbrCwTpS1kQ_r_W6c-pLuxr1ezkfKqYm3ZTAEU6Z4DTLvEKxOtBWPEqD_CfEC82jpd0u8iOTMdAnKn2gWe__Y--wk0npbGhvmWzIwZFpcRPMEFI4ju2MF0lb8GDwz3InoPABEUFiFGuinnGQPxxZu5hm-60WFolFBfa9rPecjNQHwSfhtSu3L8jBQf6mu6Tv6gc9-PwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b719b1cac.mp4?token=mUmC2e0bZmnP6yLisLofflsorvt5beeszOU-eONRQ3LPe9FbRtJJztVcCz0H5WyHk7o-QkkDKus6beAocF4qe0bUaKC2aQYsDmy0LK_iM1pdonUUMZvNpcDSqfJ4uCUNqlGXxAsoZI8wEAYbrCwTpS1kQ_r_W6c-pLuxr1ezkfKqYm3ZTAEU6Z4DTLvEKxOtBWPEqD_CfEC82jpd0u8iOTMdAnKn2gWe__Y--wk0npbGhvmWzIwZFpcRPMEFI4ju2MF0lb8GDwz3InoPABEUFiFGuinnGQPxxZu5hm-60WFolFBfa9rPecjNQHwSfhtSu3L8jBQf6mu6Tv6gc9-PwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
سوسن پرور تو برنامه قیاسی: ژیمناستیک خوبه چون میخوابی پاهاتو میدی بالا
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/94670" target="_blank">📅 16:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94669">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👀
🇨🇦
🏆
در و دافای ایرانی مقیم کانادا که شدیدا از موفقیت این کشور در جام‌جهانی خوشحالن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94669" target="_blank">📅 16:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94668">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cd9b0ec79.mp4?token=nCouZR69S-59YTKbSLO00CcSArMxzdy6euw8uvbCJ3ldGSc_cKJo2vdLk6N6mdOb0ToPUJcCd-jWkcgQl2Imr_9SO8F2Q4Q-IToGtujDXJEekRgSOjhlKDqhhbELBMyprfPCQ8vzTmpvLqXuJS5pdLTvLQMyuAntBfZ7ht_hvcnRpeKE36ohniDaoC2BXf5qLdDBdLy5exTeH_e-RbmpROgF62MhyBVtlXyVpe1lQHxnVLdZExmTri7dBfI1vk5CSvC4dXt3CNAM0MFe_HlDjhWIzUL1jEaLwsHL_2UL04Qz3l8iu-8KBVuCpdBFnGoK9FF-53YbG8USywZ-Qw8tRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cd9b0ec79.mp4?token=nCouZR69S-59YTKbSLO00CcSArMxzdy6euw8uvbCJ3ldGSc_cKJo2vdLk6N6mdOb0ToPUJcCd-jWkcgQl2Imr_9SO8F2Q4Q-IToGtujDXJEekRgSOjhlKDqhhbELBMyprfPCQ8vzTmpvLqXuJS5pdLTvLQMyuAntBfZ7ht_hvcnRpeKE36ohniDaoC2BXf5qLdDBdLy5exTeH_e-RbmpROgF62MhyBVtlXyVpe1lQHxnVLdZExmTri7dBfI1vk5CSvC4dXt3CNAM0MFe_HlDjhWIzUL1jEaLwsHL_2UL04Qz3l8iu-8KBVuCpdBFnGoK9FF-53YbG8USywZ-Qw8tRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇩🇪
بازیکنان آلمان قبل بازی امشب مقابل ساحل‌عاج این شکلی تو فرودگاه تفتیش بدنی شدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94668" target="_blank">📅 16:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94667">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa21338643.mp4?token=vVUongkj9Csp8_NVXHv17MGJua2V80W7KTEIyOCNUK9qCIL_aLWygO6OK2_EYotYazrzEL6iu_60R-J65AQ_P9KyDF-YLXzv9hYqBbf3vE4PNi5NscVn9zlMMiG9qx45JKqVqeEzGamTwhAIpjsieYMJEvF4oyMj21CvzNSK8QV0kmmNTe_zIl-r3MEsYUB7oR2klrVFgLWNI-HFQu1cqEWrNZNujYIoln--zMVp99DED1jXV78-P87Za0jd7b1-8iCsQfW9jWBuq6A494d8eHkGM5GmKxhUihPW1n5klFxeNiN3Fv8h-YT-GMDgFah3Jh8u2DvUmgt2clvCGyvmqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa21338643.mp4?token=vVUongkj9Csp8_NVXHv17MGJua2V80W7KTEIyOCNUK9qCIL_aLWygO6OK2_EYotYazrzEL6iu_60R-J65AQ_P9KyDF-YLXzv9hYqBbf3vE4PNi5NscVn9zlMMiG9qx45JKqVqeEzGamTwhAIpjsieYMJEvF4oyMj21CvzNSK8QV0kmmNTe_zIl-r3MEsYUB7oR2klrVFgLWNI-HFQu1cqEWrNZNujYIoln--zMVp99DED1jXV78-P87Za0jd7b1-8iCsQfW9jWBuq6A494d8eHkGM5GmKxhUihPW1n5klFxeNiN3Fv8h-YT-GMDgFah3Jh8u2DvUmgt2clvCGyvmqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
🏆
وضعیت عراق حریف بعدی فرانسه بعد شکست سنگین قطر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94667" target="_blank">📅 15:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94666">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIiMFsbcvxBozwhq3fs4fpe9qCyOkLrAy1T0ZsYgVOJRuuPV81kxx1bMu2Lv-_HHzuNTfFcNxdVvWIk4jZsoqhWBzFth2QfPDcT4X6AqdcMQZGNL9Keg7fcGXJVxfGOOerX9owwFnopqr_m-qVsQ0FFes-FRIYaDjaqvyN_jQZHLLIeU38GfJLOh5REMPDuCgO1eYbZ4XRZB1SlF89nSvwTr9i6TtwBaNJ13F0dm0O9ggxEs_x2O4dpk1GpqLRtSlOJJM7XAgM7zWYLAfzyUn9RHY9y_CueSxlNdQc2t8j4UiKL5EbDYaLSUmnoWlrLQUDzVH5hOskGuAPx7lUIJTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
پر هزینه‌ترین میزبانی‌های تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/94666" target="_blank">📅 15:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94665">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3LvZOD9xu46K-b6gPP6UgnXtVgj1dS4hwDZ4E5GtwCIT_xwBrBJNToxTUd9SlysQZpR5p7erXPHAr3o3nTqd4vJ27UAYM05ITv8XMDHwRkuMBlXgcMG3Tt3OgxXdqVJhS7nQsJfmnU9gnckLKrMeE_f9Gl91eYJe8__NS42k_L44uRP_jZjSji6BbiVVaVuP3nOzd5V0-JgRUXJIRL3wrDOZIL0q5nFWL8ziZ0ovm0NMMaABzonS2sDgMpG_k3-jC_B3bpm-I6fIudEr9TNhCbiH1HyD_0-OEwff7H4MHC7I6E_179OdXscYbyjiyH1JBWfTPaPonU88sJ5Ini6cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🟣
رومانو: کاسمیرو به اینترمیامی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/94665" target="_blank">📅 15:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94664">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDYtt6N4-up1cIOoUFe9x_rpFQds2nT4iTVw9ualcP1_TysON5m2D_XMba2WrdENkTdg7xQ1PePHRh285dUj8eoPc85qT9ra-V86dKwgieaiHIV1HjwP54yDJFA9ZGMyWIyBFC06OpueXLw5s8Wpz6mseO2tr-EPdiAbXed4yCbfJYB91cSJdEHS8VfioeyPN5niwgsHd5fcDSYA5UVw23zn52LMx0LrOm_3oDYZ9QYCprfKha6D4JFvJOEHmfw5Qk8JcmgJ9Rm1Myr0MmqhdulAeYWBmfrQX1nIjx4pr2aiufbcHzeKCGZldglnNrpimELpreKzR0utOszhu2q8pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توی فیلادلفیا مجسمه راکی به مجسمه بدشانسی معروفه، هوادارای برزیل هم به این شکل رفتن کیت آرژانتین تنش کردن تا آرژانتین بدشانسی بیاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/94664" target="_blank">📅 14:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94663">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d39566eee1.mp4?token=C1LEjXHtdV163c0ilymW7jrFLXyPI0EpVWUjcjAkF1bnlthi8HVKoY-jqF_WcVD_oktJG4MGbgkGCnwJGZvQwcA0w27Ry9a1wyrCtauCqa35GjAQvz6qSw62orGkHU9kbOG6w2I8kl0tCt2649gAbblCkOAgZ-tVH6FKgocddWJ0hbVo1tGV9rhORcd5Fwhh4FEBiinI-y6iOQSGSv4y1_U-WUPUbyCzf6AMwZLBFKmKRuGBX-4ISNOhh6XPSoxrcrYEfHIBCpCZ4T-OdlbCmf1675YMRbtbgIPVhVxYhmFwlDJZjvVJItWy5iHJ4FEG_OVcQG-rjfhiN4T-K2ij0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d39566eee1.mp4?token=C1LEjXHtdV163c0ilymW7jrFLXyPI0EpVWUjcjAkF1bnlthi8HVKoY-jqF_WcVD_oktJG4MGbgkGCnwJGZvQwcA0w27Ry9a1wyrCtauCqa35GjAQvz6qSw62orGkHU9kbOG6w2I8kl0tCt2649gAbblCkOAgZ-tVH6FKgocddWJ0hbVo1tGV9rhORcd5Fwhh4FEBiinI-y6iOQSGSv4y1_U-WUPUbyCzf6AMwZLBFKmKRuGBX-4ISNOhh6XPSoxrcrYEfHIBCpCZ4T-OdlbCmf1675YMRbtbgIPVhVxYhmFwlDJZjvVJItWy5iHJ4FEG_OVcQG-rjfhiN4T-K2ij0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
فلسفه کولینگ‌بریک جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94663" target="_blank">📅 14:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94662">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/94662" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/94662" target="_blank">📅 14:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94661">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_5wygKxvHXbBsOnhhpieV4fNqXswX3wXDOZE7w0FEBVtbTaj2FcLnQl-mhNwmNoKn9m36ntoIvCX6d3WHwmaYeFsY-78KuvEvTI4XDkO_RpgON0SjE8s_XOUbRbkpF6K05AItAF4sF83AXPpkXBC9bqylDqI2yIBQDyqHGN16TxMCp_L8kKnU4rQmSWTIjWYzVEtS1WrHDxSZm2EHkcJ0aRZKOulPje_CTeayahTgiHIdrZmDcTtYSi-y8oCEsjmXm49ur2yWQX_5aEqHgNvT5xNEYAEDJZhHApcD2GsBqctk_nMZCx_Qg9rLhBV-TnArTBic6Bs3gbO3ZjzdqL_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/94661" target="_blank">📅 14:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94660">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016b0353a5.mp4?token=EnyC_5kIAR48d39GLXEpjXu57RNQVZcOGPVbpNpDRaV4x9pYSfxnYeuO4ZlyAYX-Z0bzG4zCCTE3DmiCr-dI990Y2Dwppk1QYe5TLVsFEif7JUrGIa5wGvcXY9K2gTm2sHEOEcIRPzP58nAtmeaoPF3h1Da_pk8GhR6GWFCVSeQ3m-p9j2EQN9loiEfNukXmsqVp8d_AAMhqV8YE8Vrlzl84-v6-oPd16e8SbNU-5e3g1afpKZt_DqeyilAKdf9gHvj7KqlYGkUmwDmuOAFuoEFDLjjv90xO9LbKMWL8ICj84k_iwsT1RSBmqwFAvROYN2-5OGyDDCoIsLjXjnplsq3erY7b4XV-YEYPd5DOOhQPfJoAAOiyNJr7XgLKHKQifEVuWeKMkjLje0mSLJj1pfcneJ1Lw59OUeMOH5EpBYOL-xO4Mzqj4UymYcvK7cphXF6J9dIg4TagaH0p7z8h53HG1-SU0xaE8S1SKVfAPzL9gWH5gIAibW6iLYj1QFbJfEzXjJh2YPWJCO7CGLmRD5JKgmXMR90lW62jKZOSuqrmdF_SzSqZh7SWonAgRa3kXeI_FH188580NZh1ROE-BbrUBTRHLzIlXTKhqU6iiwn75fSaE-0DyJQbr56L61slmr-HwNnjZVzN1r41a6RuLR2UmKBC_VMik8dHDNBZ7zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016b0353a5.mp4?token=EnyC_5kIAR48d39GLXEpjXu57RNQVZcOGPVbpNpDRaV4x9pYSfxnYeuO4ZlyAYX-Z0bzG4zCCTE3DmiCr-dI990Y2Dwppk1QYe5TLVsFEif7JUrGIa5wGvcXY9K2gTm2sHEOEcIRPzP58nAtmeaoPF3h1Da_pk8GhR6GWFCVSeQ3m-p9j2EQN9loiEfNukXmsqVp8d_AAMhqV8YE8Vrlzl84-v6-oPd16e8SbNU-5e3g1afpKZt_DqeyilAKdf9gHvj7KqlYGkUmwDmuOAFuoEFDLjjv90xO9LbKMWL8ICj84k_iwsT1RSBmqwFAvROYN2-5OGyDDCoIsLjXjnplsq3erY7b4XV-YEYPd5DOOhQPfJoAAOiyNJr7XgLKHKQifEVuWeKMkjLje0mSLJj1pfcneJ1Lw59OUeMOH5EpBYOL-xO4Mzqj4UymYcvK7cphXF6J9dIg4TagaH0p7z8h53HG1-SU0xaE8S1SKVfAPzL9gWH5gIAibW6iLYj1QFbJfEzXjJh2YPWJCO7CGLmRD5JKgmXMR90lW62jKZOSuqrmdF_SzSqZh7SWonAgRa3kXeI_FH188580NZh1ROE-BbrUBTRHLzIlXTKhqU6iiwn75fSaE-0DyJQbr56L61slmr-HwNnjZVzN1r41a6RuLR2UmKBC_VMik8dHDNBZ7zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
انتقادات شدید مجتبی‌پوربخش از مسؤلان فدراسیون بابت تغییر کمپ تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94660" target="_blank">📅 14:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94659">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07af1e396e.mp4?token=uhkROgfG1E_in2puNYNLgIzhchhL6hnizaOXsVQkL8u409k-s3GYjOENpdCjhjN-Lex046tSMvMsBuyxSMCCmgLS6ddVGE9VQ45yVag-EFjec_5IsFSgv-cB9dTH8RA1-E9kQmfm9cZ6nhz6Y0fOjsQ__xK1ItNGH0ltlG5Uf3lODOpe5anYc9M9Jdjcn_Bqw9skxKjTX5YLto6L5iQKaZZXda_iQoT7hXR0lnM2DQx7p7XnvFvHIv4WzlWy7aonG5fmaLu4tkCnCjImO657gvmXEfX2NDT2hyqOYmXk43B5TYXtbFmVZc5q2-iRHQACpST7yge74UZrBJ7fGjoMIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07af1e396e.mp4?token=uhkROgfG1E_in2puNYNLgIzhchhL6hnizaOXsVQkL8u409k-s3GYjOENpdCjhjN-Lex046tSMvMsBuyxSMCCmgLS6ddVGE9VQ45yVag-EFjec_5IsFSgv-cB9dTH8RA1-E9kQmfm9cZ6nhz6Y0fOjsQ__xK1ItNGH0ltlG5Uf3lODOpe5anYc9M9Jdjcn_Bqw9skxKjTX5YLto6L5iQKaZZXda_iQoT7hXR0lnM2DQx7p7XnvFvHIv4WzlWy7aonG5fmaLu4tkCnCjImO657gvmXEfX2NDT2hyqOYmXk43B5TYXtbFmVZc5q2-iRHQACpST7yge74UZrBJ7fGjoMIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این روزا در خیابان های مکزیک چه میگذرد
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/94659" target="_blank">📅 14:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94658">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acdd4f1167.mp4?token=knRo3QQU1GuuIlpZekmzHLvMTZRprDURrMOI8SBJcoFhDktXHwA3VXMLp8IzM5dKQmjwZfNW3lgWnoBRLmsEiBXDeR8CcaIuAkKx6Vs2VKxw0Sv1EbYIZdpSWPTgCfJyJDuzK2DvUycLHAOmhqAJQ32RHMB6c216GRDR_-c7q62wZ_k4v-UJLyhO5ZH86YObpb3vmbt0KHc67HffEH_n7foWGx17ov2Ak_lemL4VasQWPvwMqQiw2gShBBzn2EGudpL6sunY8-BKHw1CTT6vbDyGojXYqH6WmpOjyfvWsUD_LAKFOy5DyvnULoEiqRJW2ta0rH6WQEus_dVEOjBPfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acdd4f1167.mp4?token=knRo3QQU1GuuIlpZekmzHLvMTZRprDURrMOI8SBJcoFhDktXHwA3VXMLp8IzM5dKQmjwZfNW3lgWnoBRLmsEiBXDeR8CcaIuAkKx6Vs2VKxw0Sv1EbYIZdpSWPTgCfJyJDuzK2DvUycLHAOmhqAJQ32RHMB6c216GRDR_-c7q62wZ_k4v-UJLyhO5ZH86YObpb3vmbt0KHc67HffEH_n7foWGx17ov2Ak_lemL4VasQWPvwMqQiw2gShBBzn2EGudpL6sunY8-BKHw1CTT6vbDyGojXYqH6WmpOjyfvWsUD_LAKFOy5DyvnULoEiqRJW2ta0rH6WQEus_dVEOjBPfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🎙
🇧🇷
وقتی عادل فردوسی‌پور، حتی بعد از گذشت ۳ دهه از شرکت در مسابقه هفته، یکی از اولین قاب‌هایش در تلویزیون همچنان به برزیلی‌ها و اسامی کاملشان علاقه دارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/94658" target="_blank">📅 14:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94657">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPxCRsudOXG1VcFyDdfZ3NOEaV6Gmy58Kv9YgQd8JXAwN_8J61L4mYCaY3S9qYFdN8Vnqvzih9KkHweOgSPGTSCnXDPtNgIJ0Ss7g2Ey5O6oGNjzLZr7CKVT3OiGWQa3oxaHIfKhJCa3e6t5fEAoxk_3XfuiO0yz95m9fEBFNhFNKD1YpBinMvgvQIRLxRDkAnsnu-NNcPamMXfRxFiL8yF15aSpOp4LXqAU8VDOZbAfuauNJlgOx1QJ0ofU-4ElfBU1FiHwyg64hmZlntEgrJS19Zb6VxDFipPgifMznQa9MgRWjwgp4mVWqZQ11SLG7FBVbXYz8LzfP4dwopz-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🚨
فابریزیو رومانو:
آلوارو کارراس این تابستان در رئال مادرید خواهد ماند. مورینیو با حفظ او به‌عنوان جانشین و ذخیره کوکوریا موافق است، به‌خصوص که احتمال جدایی فران گارسیا از باشگاه وجود دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/94657" target="_blank">📅 14:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94656">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">😐
❌
فدراسیون پنج ستاره ایران تصمیم گرفت که سهمیه بازیکنان خارجی لیگ‌برتر رو در سال آتی به ۴ بازیکن کاهش بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/94656" target="_blank">📅 14:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94655">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI3IICUraYlgjcGVn41WSuzX7LZecoRngpp7aor2ND5M1DIhsurbLq95XyyLpSRZQXpzPTlJHCplU7nMkjxCeh-hUW6ekAOrPzgjqJug7OYZzDrkKnjct0O94aUBGKgEee8KgzJlz94RpDt5rzupBgcZ5LLEs5Tu-ByC975Duij8TAaUk2ANvA6xLHRlzmLDXc_acCcKw3V2_pe2IUINB_0lzO2-Gd2ByR0f_5go8QmPg8TLM68XEjvsOLkEJBtXX9mZaQGqYwNDR4kwl_NAzPvTwIsU9ArjlSqe9iy-njEKK9OcI_cyGEt-q7vWeDwM9IYeuSnzzIt26np2UioBwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فووووری
؛ رئال‌مادرید بدنبال جذب هینکاپیه برای تقویت خط دفاع خود است. آرسنال این بازیکن را فروشی نمیدونه اما در صورت رسیدن پیشنهاد نجومی ممکنه نظرش عوض بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/94655" target="_blank">📅 14:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94654">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6b2f32a1b.mp4?token=m-lbb0STkjlPFFWHLzSUDT1TGW6Z2jV08U6dtfMCxwO9KXkzLIEx4Nj6h0q3Slphv5S0wdTZTDDyg1fBLqHpwEfwbXbrFOFTlxKqoV8QAFGMEb6Z8R3MdWwDW5fr5TitFHtC7Uwn5Il3U1gmMseN33hzLnyljdiw7fI-Wncw_R2WDzVWG9f_V1Y2yuhTL0QFWmLhkg_xFk_-r_7QkpYFNHEV_JIVvKrYcBKsTKX_vkycDhr8LDJtA_9n6uhztFYYicOeE8lwJH3NQrNvPGynHs-rmAbGUhMRfABP5Yw23pwV2lwLzyN3nYl7XFoJ5RBBrhQlm_7qX2AYexRivEZwAE4qwi8CimLK6RG3FBJIwLsWPSSeaj-xBs9ei38atYP0E_ZRiM3OKyLiH28M2JnaYM_JGXJtyg8l0w8HX8YVtS_FlpDy3XwUCwqn__7B5NiPA7EaLlz2lzPYIr25I9PmtklaqPJtxDgmdYNLK43iVhPwVzqmCNDYvmlGSa3anJ7MtLMvfTESUczt1e6X1--e2tZJHrcfKy1iR9Dq57HbAU-fIksNZ7-wnSQEKSCUoKdB1rlitT_5bGkjcx5GI48ujKRz0o_ItspO28GaxRVkzET8Nxy9VjZm99q3v6toUg9cThVy8k3Qngwlnjs8DKkZbzCa6iNS1Op2JZsrybg3SSY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6b2f32a1b.mp4?token=m-lbb0STkjlPFFWHLzSUDT1TGW6Z2jV08U6dtfMCxwO9KXkzLIEx4Nj6h0q3Slphv5S0wdTZTDDyg1fBLqHpwEfwbXbrFOFTlxKqoV8QAFGMEb6Z8R3MdWwDW5fr5TitFHtC7Uwn5Il3U1gmMseN33hzLnyljdiw7fI-Wncw_R2WDzVWG9f_V1Y2yuhTL0QFWmLhkg_xFk_-r_7QkpYFNHEV_JIVvKrYcBKsTKX_vkycDhr8LDJtA_9n6uhztFYYicOeE8lwJH3NQrNvPGynHs-rmAbGUhMRfABP5Yw23pwV2lwLzyN3nYl7XFoJ5RBBrhQlm_7qX2AYexRivEZwAE4qwi8CimLK6RG3FBJIwLsWPSSeaj-xBs9ei38atYP0E_ZRiM3OKyLiH28M2JnaYM_JGXJtyg8l0w8HX8YVtS_FlpDy3XwUCwqn__7B5NiPA7EaLlz2lzPYIr25I9PmtklaqPJtxDgmdYNLK43iVhPwVzqmCNDYvmlGSa3anJ7MtLMvfTESUczt1e6X1--e2tZJHrcfKy1iR9Dq57HbAU-fIksNZ7-wnSQEKSCUoKdB1rlitT_5bGkjcx5GI48ujKRz0o_ItspO28GaxRVkzET8Nxy9VjZm99q3v6toUg9cThVy8k3Qngwlnjs8DKkZbzCa6iNS1Op2JZsrybg3SSY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو عجیب منتشر شده از مراسم محرم در یکی از محله‌های تهران
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/94654" target="_blank">📅 14:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94653">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38da867d39.mp4?token=sVHMAcVVeWIujqOCxQp7Nq6HjBfc6miCR8tOHzrsVwj6UN5sTXmNpBDprfvjrDujsL3GVBHMf9p6d_d9LP3VlyNSfOdupMsoPm4SYa-XDxjhvhxIiefEVZIDUBC2p9MU4PNyYBYhfOVJJ01gRfTucJOeeL26ZuxIpCZth9jEi8bG_fvA96DaBl3M1I9zzpDcNiqEOITx_EAIR4kRdcJtzkYsUwdo8ft3nHWjhmK-_I9rT9u6gO3E_skSoAjvI9DccKIILsahppdu_pAymaJeSKdwtJyB7OHtwC7tln0aEJalw4ng9ikC14jp3tPhQDNdpW8hJM6W5ffXC-Mrfqe-uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38da867d39.mp4?token=sVHMAcVVeWIujqOCxQp7Nq6HjBfc6miCR8tOHzrsVwj6UN5sTXmNpBDprfvjrDujsL3GVBHMf9p6d_d9LP3VlyNSfOdupMsoPm4SYa-XDxjhvhxIiefEVZIDUBC2p9MU4PNyYBYhfOVJJ01gRfTucJOeeL26ZuxIpCZth9jEi8bG_fvA96DaBl3M1I9zzpDcNiqEOITx_EAIR4kRdcJtzkYsUwdo8ft3nHWjhmK-_I9rT9u6gO3E_skSoAjvI9DccKIILsahppdu_pAymaJeSKdwtJyB7OHtwC7tln0aEJalw4ng9ikC14jp3tPhQDNdpW8hJM6W5ffXC-Mrfqe-uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇹🇷
حیف شد ترکیه از جام حذف شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/94653" target="_blank">📅 13:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94652">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9405536d1.mp4?token=H7TwrRqpwvx5Izwef8gv0CzIw_PQfECMVx2GsWQGXXdAYM8pSthozkSwo4qHF1w3g5u3ymtOcYyRp0dleFM8xeCXda2NyjILOXd0ojt8OWNYYs6ovRoqW9HRUGVfMY_Uucmot7qpGPrnJMhgEhNy7QX1ioieThncDUHsZo8ddD0pHkD8Hgf78BiL4Ed24WfTUXxY9J6UeSsh_r6VbGopdUAzeExiVDHx5KOqjG0B9xfVyU-NbiYOREhFHCl85R-A9kzWPafoVJ5j81gLio3Hdbhy-LUehXwM7wTVZ49J9M5N7GMF_5tMF6Edjj4jkQekjcqreuBu7hGWPvSHf0BAwQp24_KDzBkRJfgt01H1okUIgbkcXvMKngV8bnbOo9nFuTbtNprVCTpbe0ncnNu0KH3ensMo_3TGN6ZKlo4s4Ouc5edbbBu1_Yjc-1u2SWB0bvtkh292SpZPJSaNz2xqCgiKTyImCe2iRIVUPB8aMX4_s77dSzARuTtna0o4UIOrzXRquI6120P5yqhXxximESilXiemzRLI0wURalzj62H7gXlincbts7zg088zN3ZqiZOuGTx0a-HUZA_27lPgM7ygQqvE0klRkvxq8EpV3vWFh1m2Htu6NVL089aQgSL6wJglHYmV0qB8v6uJeK8NBBeXw2c9rD_6G9TLjafTXCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9405536d1.mp4?token=H7TwrRqpwvx5Izwef8gv0CzIw_PQfECMVx2GsWQGXXdAYM8pSthozkSwo4qHF1w3g5u3ymtOcYyRp0dleFM8xeCXda2NyjILOXd0ojt8OWNYYs6ovRoqW9HRUGVfMY_Uucmot7qpGPrnJMhgEhNy7QX1ioieThncDUHsZo8ddD0pHkD8Hgf78BiL4Ed24WfTUXxY9J6UeSsh_r6VbGopdUAzeExiVDHx5KOqjG0B9xfVyU-NbiYOREhFHCl85R-A9kzWPafoVJ5j81gLio3Hdbhy-LUehXwM7wTVZ49J9M5N7GMF_5tMF6Edjj4jkQekjcqreuBu7hGWPvSHf0BAwQp24_KDzBkRJfgt01H1okUIgbkcXvMKngV8bnbOo9nFuTbtNprVCTpbe0ncnNu0KH3ensMo_3TGN6ZKlo4s4Ouc5edbbBu1_Yjc-1u2SWB0bvtkh292SpZPJSaNz2xqCgiKTyImCe2iRIVUPB8aMX4_s77dSzARuTtna0o4UIOrzXRquI6120P5yqhXxximESilXiemzRLI0wURalzj62H7gXlincbts7zg088zN3ZqiZOuGTx0a-HUZA_27lPgM7ygQqvE0klRkvxq8EpV3vWFh1m2Htu6NVL089aQgSL6wJglHYmV0qB8v6uJeK8NBBeXw2c9rD_6G9TLjafTXCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇲🇽
🇰🇷
درسته مکزیکی‌ها داخل زمین به کره حال نداد اما خانوماشون بیرون زمین حسابی جبران کردن
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/94652" target="_blank">📅 13:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94651">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ff9b3624.mp4?token=slMntuTI8s6FysBntWcFkEQOJqPN2bVdnDUa2mUw2UDe9QEr_LUDBdQYLao1s0m3OUU5b3rqXqywem_8KD1ZBosOlZjx3-2HUNZbw1DmD2RUJDVA4jAm-M7GTXPLqs27dEJ-CUkeB4HwORafWHSlc-YPZ3k0YuYQE66SoUf1ex1xh8wA9d-P2dyDCrVc9wS61lBhKDB6FWUVRuRkRbDR2bWdY3am72IaWY_o6I-w_PDkQn8o3zOs6tsxdP58XPmZAETlSUQzSLThEc8k1fQG7ZaWOErqjsPrmm3s04maY-QuossvT6T5RK-O_x-_1LGfZ9b9gOS5UX2mvn5ckb8MRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ff9b3624.mp4?token=slMntuTI8s6FysBntWcFkEQOJqPN2bVdnDUa2mUw2UDe9QEr_LUDBdQYLao1s0m3OUU5b3rqXqywem_8KD1ZBosOlZjx3-2HUNZbw1DmD2RUJDVA4jAm-M7GTXPLqs27dEJ-CUkeB4HwORafWHSlc-YPZ3k0YuYQE66SoUf1ex1xh8wA9d-P2dyDCrVc9wS61lBhKDB6FWUVRuRkRbDR2bWdY3am72IaWY_o6I-w_PDkQn8o3zOs6tsxdP58XPmZAETlSUQzSLThEc8k1fQG7ZaWOErqjsPrmm3s04maY-QuossvT6T5RK-O_x-_1LGfZ9b9gOS5UX2mvn5ckb8MRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خوشگل ترین بازیکن جام جهانی از نظر خانما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/94651" target="_blank">📅 13:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94650">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7248f9196c.mp4?token=ggkxDB3-YyJGUTopuxhGv-UGM6gcYLjk_OStqTUn_p7ZfWsRigLJkfVNtFJ49PfXRjwQ3nTE5PEKZJHvlgU4h4gcQgfc2xrwdDDFTpFPDYMxF7PTIuT7b8dYvzkI6SGdcX2sLzetIPVUyS_u4YQSEPxK7iqNHo-Rsnk6-YkcuMkv8Kt-oDKiYzkAY7VcPD_1_rXBLDo8NRY6Mx0kvzgwqa4tNfb4KV-9pxr8oA8ZU33fp-M2TAY5ubhKvSBPtFMatnnVUYncylRlS5JnFvLEQrr2JfffQ6_lbA3GE-NmOD_CSznKu8WnT53XYafeEqZnQCCZshccQWtskigmsT6Vao1o4f9I5xrQL_VxUbu8iN5KqRSwo7hj2Ln4v8H7tb8oTwP54hDkhCQfLSkbQU6EQLXu0V262S1yYUjEIuHPV0-pSscvWrswGXRFlFqKTl4fRYyduUkv31SwMT5OryZO6-P-J8__Au-sPrRPzKiYYseesQl0ZCqyjC8pQg6vTgqXDzCfE0VRfpfj-Q7Wz4qPsOawx1BITO6FayBoxFMJtRuVNI5HqHyidoPOObrQ_fudA3Fz3dtbLD9NK4f6dWRxL6qddUPat3lc7LyfsFFPZ16avKrbPlV7-kHL5IQiK-tx9PJOPB_GFB9nKH7u99QletP02dKRSj_0N_beIuGyRxc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7248f9196c.mp4?token=ggkxDB3-YyJGUTopuxhGv-UGM6gcYLjk_OStqTUn_p7ZfWsRigLJkfVNtFJ49PfXRjwQ3nTE5PEKZJHvlgU4h4gcQgfc2xrwdDDFTpFPDYMxF7PTIuT7b8dYvzkI6SGdcX2sLzetIPVUyS_u4YQSEPxK7iqNHo-Rsnk6-YkcuMkv8Kt-oDKiYzkAY7VcPD_1_rXBLDo8NRY6Mx0kvzgwqa4tNfb4KV-9pxr8oA8ZU33fp-M2TAY5ubhKvSBPtFMatnnVUYncylRlS5JnFvLEQrr2JfffQ6_lbA3GE-NmOD_CSznKu8WnT53XYafeEqZnQCCZshccQWtskigmsT6Vao1o4f9I5xrQL_VxUbu8iN5KqRSwo7hj2Ln4v8H7tb8oTwP54hDkhCQfLSkbQU6EQLXu0V262S1yYUjEIuHPV0-pSscvWrswGXRFlFqKTl4fRYyduUkv31SwMT5OryZO6-P-J8__Au-sPrRPzKiYYseesQl0ZCqyjC8pQg6vTgqXDzCfE0VRfpfj-Q7Wz4qPsOawx1BITO6FayBoxFMJtRuVNI5HqHyidoPOObrQ_fudA3Fz3dtbLD9NK4f6dWRxL6qddUPat3lc7LyfsFFPZ16avKrbPlV7-kHL5IQiK-tx9PJOPB_GFB9nKH7u99QletP02dKRSj_0N_beIuGyRxc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🏆
صحبت‌های جالب یک خانواده اندیمشکی که هفت نفری با یه پرشیا در سال ۲۰۱۸ رفتن روسیه تا جام‌جهانی رو ببینن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/94650" target="_blank">📅 13:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94649">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d04b34885f.mp4?token=QObxDdsdtgTLZSJy_PGrfUJ_1RRvnMfcFIUsN4gvmMYeAkMVj-VKEeFxG52fGYXTABawOZVLS7Zxz6qKoWwFlzDc5Q0N8yrOtXv5O0fB37tRraNitoIEsjvMCgk9ghtOVxwV8OdMgXa2JhhHsNQc9236N_CIVaZ7U6MsjR56t-DnWHrFsfoyMMRrEEgkqEEqfrDCV-n9PgC_pA4mjY1K1kWQ8sH-wCAWAoNe_TF5zteapzeCoTzzUGfTqLfRIzvp9n_9ibF_UcwzdRXO9h8dycXibeVUIsZWaSRfZx87A3l8Q8_0XrwwFKMudOISs0lgjPM0VveqvCLvmAtZkpZjrhKerJTsEFNessw6tdm5HEgf77PF7ubUD67lcJis899I8Ebw_gk9tTsathYcqYOIVSSxydQxrAuQhxI43bVVcqIeY-JCni3H3FQyNlHHUjpmhKQT7-CRfral0KIK03ocUDRVkfn1ZOuyvpk8xYH4w5qhpjUQw6J3JjJqVRBBTmZ8bB7Qj-MI9ZlME04qeb_i1_UQD0RphzIH_x6lWctssx1Cwt9H-eoZVEafHKYle_gQx2gMO__iTtIZzowxM5ONQiQ7rzjl9H2yOIwj7jrWBywnGwMyJYqbe6tX4CeJIpM6HxL3fSnvR4duL7G5uHdOJkkSMVtz_1Gq2MJdOzCPqjc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d04b34885f.mp4?token=QObxDdsdtgTLZSJy_PGrfUJ_1RRvnMfcFIUsN4gvmMYeAkMVj-VKEeFxG52fGYXTABawOZVLS7Zxz6qKoWwFlzDc5Q0N8yrOtXv5O0fB37tRraNitoIEsjvMCgk9ghtOVxwV8OdMgXa2JhhHsNQc9236N_CIVaZ7U6MsjR56t-DnWHrFsfoyMMRrEEgkqEEqfrDCV-n9PgC_pA4mjY1K1kWQ8sH-wCAWAoNe_TF5zteapzeCoTzzUGfTqLfRIzvp9n_9ibF_UcwzdRXO9h8dycXibeVUIsZWaSRfZx87A3l8Q8_0XrwwFKMudOISs0lgjPM0VveqvCLvmAtZkpZjrhKerJTsEFNessw6tdm5HEgf77PF7ubUD67lcJis899I8Ebw_gk9tTsathYcqYOIVSSxydQxrAuQhxI43bVVcqIeY-JCni3H3FQyNlHHUjpmhKQT7-CRfral0KIK03ocUDRVkfn1ZOuyvpk8xYH4w5qhpjUQw6J3JjJqVRBBTmZ8bB7Qj-MI9ZlME04qeb_i1_UQD0RphzIH_x6lWctssx1Cwt9H-eoZVEafHKYle_gQx2gMO__iTtIZzowxM5ONQiQ7rzjl9H2yOIwj7jrWBywnGwMyJYqbe6tX4CeJIpM6HxL3fSnvR4duL7G5uHdOJkkSMVtz_1Gq2MJdOzCPqjc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل خودت رو بزن!!!
🔹
با افتتاح حساب غیرحضوری در باران بانک کشاورزی، از برندگان
۹۳میلیون
تومن
اعتبار خرید باش!
🔹
۹۳
سال قدمت
۹۳
برنده در هر روز.
🔹
برای شرکت در ‌قرعه‌کشی
اینجا
رو کلیک کن.
شرکت در ‌قرعه‌کشی
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/94649" target="_blank">📅 13:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94648">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9be9e31008.mp4?token=WvDzIwmBP_KcdJpM29-U2Vv2K02EKcvH9DMiHi7SvO6QdWUL6UJxP6cVmDchHxVVcQ2-JG-sZf-xqAktmzX3okp1uEkATFDSXftPv0fphgsaE1wn12vH9FC58nEazfpU-1ScLnT145ABKNWtTWLFKfSqHl7XYbxoWqyEUPMOr2BcdY-4cobyoOzWk6zYiqSZLRgVn_VXV6yAz7QdGao5vj4Dfl3ok5SWMvrObyxnyLI9M9m6dDITEgsQRGOL3ZMJHmU_Bzok5QmIPjTMnfFiFAsCXv0nL2s4N1a6JcbDZLUNaWhY9Q9e5BLiVkp5KDJbmmN9S0cSZnxixUn_FD50WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9be9e31008.mp4?token=WvDzIwmBP_KcdJpM29-U2Vv2K02EKcvH9DMiHi7SvO6QdWUL6UJxP6cVmDchHxVVcQ2-JG-sZf-xqAktmzX3okp1uEkATFDSXftPv0fphgsaE1wn12vH9FC58nEazfpU-1ScLnT145ABKNWtTWLFKfSqHl7XYbxoWqyEUPMOr2BcdY-4cobyoOzWk6zYiqSZLRgVn_VXV6yAz7QdGao5vj4Dfl3ok5SWMvrObyxnyLI9M9m6dDITEgsQRGOL3ZMJHmU_Bzok5QmIPjTMnfFiFAsCXv0nL2s4N1a6JcbDZLUNaWhY9Q9e5BLiVkp5KDJbmmN9S0cSZnxixUn_FD50WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇭🇹
چالش هوادار آمریکایی برای منتخب‌ایران
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/94648" target="_blank">📅 13:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94647">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68cb5604e4.mp4?token=AT2sKUp4r-pV-dWw8LLf6z68WFJflRwVH5a-YLu7NmnV5nJpqAQuxE98FKAlvZ42PIG6FsaGH2S57boKKgbnFEYI0xpAXwPRFTEpgs9rhJ2UZzr4BYfD3zhSMO0UfbrnAF3I_9dedZ1gSkO0GUwQOYPca5vt0-iMOscY-jGeKPoH1ajUf1Aj3h-nlqdiIw6i3HvWweposjunt3omqSbrkmgFkGOB1K4O2cnFE3U1J9cVQPBCcw8WwdXRIu3huYk-H3twOOMegLZyprLInG6hKLyf1LcqAcnzvtB013SSywB31zbBwSRKfxOkiZ8-2h_OmeAOxnrvD70anDq03QPvJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68cb5604e4.mp4?token=AT2sKUp4r-pV-dWw8LLf6z68WFJflRwVH5a-YLu7NmnV5nJpqAQuxE98FKAlvZ42PIG6FsaGH2S57boKKgbnFEYI0xpAXwPRFTEpgs9rhJ2UZzr4BYfD3zhSMO0UfbrnAF3I_9dedZ1gSkO0GUwQOYPca5vt0-iMOscY-jGeKPoH1ajUf1Aj3h-nlqdiIw6i3HvWweposjunt3omqSbrkmgFkGOB1K4O2cnFE3U1J9cVQPBCcw8WwdXRIu3huYk-H3twOOMegLZyprLInG6hKLyf1LcqAcnzvtB013SSywB31zbBwSRKfxOkiZ8-2h_OmeAOxnrvD70anDq03QPvJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇩🇿
🇦🇷
رسانه‌های الجزایر این‌شکلی به اخراج نشدن مسی در بازی با آرژانتین کنایه زدن :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/94647" target="_blank">📅 12:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94646">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXNevojVWnFiU0XhsIY8fh-0SYBiRw1T_o4gQTgoH5o9kL6BSumB1PmDiyHcg1s0R1Kw9x0MYphd9OcqEWNetcqOgB3v4ETKLknkJrD8aHvt3kmzpGi2hq6sK8Ar3biVHmzCj4sNpJLsHeN7jWXIB2f_grQiC97O4oBZmjdDOIRvvq5ldL_cagtXJ5oQ3ZMb2lcyQQN3CLI3aYJBgKzeAaf-LbrHntntvZKVe97N36arHZGPt2ZseVBfq__e81YB-aYAQtWB3sBhwNLDNY2ahHeUCD0rSu6P1WxqzmvXxszE-sIGd6EIK5BTC3pOnUCkT9at1xKwtDRMBRXu1NKPNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
آردا گولر:
در دوران بازی‌ام با تیم ملی، هر کاری که بتوانم انجام میدهم تا این جام جهانی را فراموش کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/94646" target="_blank">📅 12:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94645">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c72290d26.mp4?token=Nlsc7sXjdizoP6QYKyad3vYV8T-kpkEVQQj7sBtjQtHUjsNGad_CEnM1R4Rk_Kr5USiut0JUgXtAst0P_xufWbni8lV9YRC-Y9i9aO6P_Sh0UhhM1ATPsEp-GzNim1LMP4rwGPMyYh9R56iC0oZBxY12ykuu6BNjtlDoxaaYsL0HGxCobGJxaIV3ityfjxKgHYx-GY-fUkFPlwA11PHJaKyM58TnavVlRl6Gj8Gz43z1r9b6E82JzFQJD0VhQyvvfWZuCLZZwvBNdLUelFsX6yoVvGocNF1OW9vg2N85SSerij6BIWMQVtSrtoGgHyldIzA-enYeppplhpNh4Ktapg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c72290d26.mp4?token=Nlsc7sXjdizoP6QYKyad3vYV8T-kpkEVQQj7sBtjQtHUjsNGad_CEnM1R4Rk_Kr5USiut0JUgXtAst0P_xufWbni8lV9YRC-Y9i9aO6P_Sh0UhhM1ATPsEp-GzNim1LMP4rwGPMyYh9R56iC0oZBxY12ykuu6BNjtlDoxaaYsL0HGxCobGJxaIV3ityfjxKgHYx-GY-fUkFPlwA11PHJaKyM58TnavVlRl6Gj8Gz43z1r9b6E82JzFQJD0VhQyvvfWZuCLZZwvBNdLUelFsX6yoVvGocNF1OW9vg2N85SSerij6BIWMQVtSrtoGgHyldIzA-enYeppplhpNh4Ktapg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇵🇹
اقدام جالب هواداران پرتغال بعد بازی کنگو در تمیز کردن سکوهای استادیوم محل بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/94645" target="_blank">📅 12:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94644">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
لیگ‌برتر فوتبال ایران در فصل‌آینده با حضور ۱۸ تیم برگزار خواهد شد و این فصل هیچ تیمی از لیگ‌برتر سقوط نخواهد کرد. همچنین بزودی تورنمنت سه جانبه میان گل‌گهر، چادرملو و پرسپولیس برای سهمیه آسیایی برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/94644" target="_blank">📅 12:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94643">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c445efe2.mp4?token=fYjZtBwkVTzf0Zb6CMug_ESAkv6vRkhoy5oZoMOt9SkLPDBLaUjTZmcXdMAdIaqnUSJue9gQox1_2TCJF2MpZ0upG2itQyvtcxnpi7dqV6DGV5AsftETbJdvsqf_Qg6pJGxcikx8ntzAIHzv3Mc2iEpymmGv3HMKSlI1a-WQkWa5xvSQN-GaP-MDK9zebHSaW7lpGZ_ao4g7LhNe7nTcdl6LXSX8rpWG3xh27IHttE0lrc6-fEdjgqZyg4zoELqxwyvxdtxEtNfLav3OGPp0BeBxARbDjsRskSgP_CmQzFFo56_-PgVo3nXjU6utMx6CMLQdvA0tP28Uf9tvnP0pRYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c445efe2.mp4?token=fYjZtBwkVTzf0Zb6CMug_ESAkv6vRkhoy5oZoMOt9SkLPDBLaUjTZmcXdMAdIaqnUSJue9gQox1_2TCJF2MpZ0upG2itQyvtcxnpi7dqV6DGV5AsftETbJdvsqf_Qg6pJGxcikx8ntzAIHzv3Mc2iEpymmGv3HMKSlI1a-WQkWa5xvSQN-GaP-MDK9zebHSaW7lpGZ_ao4g7LhNe7nTcdl6LXSX8rpWG3xh27IHttE0lrc6-fEdjgqZyg4zoELqxwyvxdtxEtNfLav3OGPp0BeBxARbDjsRskSgP_CmQzFFo56_-PgVo3nXjU6utMx6CMLQdvA0tP28Uf9tvnP0pRYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏆
🇺🇸
صحبت‌های جالب هادی‌عقیلی درباره دلایل رشد فوتبال کشور آمریکا با پوچتینو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/94643" target="_blank">📅 12:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94642">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSQaSdXO8uxMpOPPozDrdzb7psP8GjSygFndz1h58uFWEaHxIBQFFumiMzbLTpcL8oi5LepLzEj3OWbZsK2J0FkM0fxkoNDRwS2TgOVjcwRCPmKHrSDwLTicj1-mdwzmJM1TGd4zsfZXpyheLmHadgqhg9WOBQf2cRHmeqyb9c37L9KZ7IhXUGvKnJj8gaCOuEQ5iMiqCsyKs6F7OqaosjYy4tKNaratNOvdlg_7wzvGc9Dppd8-JunNgl8exb5XwayyjDrrEsW55shEDJMFh0bzYqTZjSW04ZIcgaeJ38ynVmyKJYdklIlk8utlG20f5hlz95hH9mL6patbiArGjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
وینیسیوس جونیور در جام جهانی 2026:
◀️
بهترین بازیکن بازی مقابل مراکش
◀️
بهترین بازیکن بازی مقابل هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/94642" target="_blank">📅 11:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94641">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhlMdOVZX_WXUGUvEpANagAGOl-ZgI6tFXtuQxrlQ0X2EhezvrvsM9G42L5wT4FwWbC4TS0V13irInW_BSY44_bjTGaX4H1iyCtwxxsWJlp0JisW-4pBFZCyknFyV902uD261MA8K6qErrJucEA4DyirmxRTP9Bg3bHLOsiukP8M0My1AMiL77AyJzpq4TBDBvG5kTn0kcDQuB2pRgoNPBtk_Z6zH1dIY-kRZrAQqYTbM8YYdQjoP3A5iAx3jnQuHMlxs8zPB3riGTBtdlKLtguEc8LPxYjmyYb3vxMGUXP92YNUVbeOfTzPTASLzbjJdy24a3-3rPq-jxhoGXEyqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
تیبو کورتوا:
ایرانی ها یک مدافع راست به نام رامین رضاییان دارند که زیاد در حملات شرکت می‌کند و ارسال‌های دقیقی انجام می‌دهد و باید مراقب او باشیم او میتواند برای تیم ما خطرآفرین باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/94641" target="_blank">📅 11:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94640">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mbu3CEx4Wivhqn10z4AC_v2aq5i0hRi9aag5KcCrI4D4H65KtheGLNVhTRh_Z82tiyDPFcaxEVy8ABGPEDz_4_ESqVT5EUWAevtmDWdigC-8bebp8hV34njYYEX9hx-ROvSrh2h0fn1NuoLdfSkNx3qqeHewaAbKAcl78eUFrJJNZWXE1JuttNGHSWR25OooBiS5e4o-iiwXwlsKMWsnLFVfddR_lM-TJwQ0HvCg3541LDq1ohxAnz21mt-cf0tNaRjA6wkzRzaKbmYbAqxHId8YUhXQ7PT0caXpaE_AbMb7laBbCraxrsXN97yCBAd6UIdOYKg8-Li7HvtV4-FlNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
🏆
تیم‌هایی که تاکنون در جام جهانی ۲۰۲۶ موفق به گلزنی نشده‌اند:
🇹🇷
ترکیه — ۰ گل
🇪🇸
اسپانیا — ۰ گل
🇩🇿
الجزایر — ۰ گل
🇭🇹
هائیتی — ۰ گل
🇪🇨
اکوادور — ۰ گل
🇨🇻
کیپ ورد — ۰ گل
🇵🇦
پاناما — ۰ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/94640" target="_blank">📅 11:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94639">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6bcd7de2.mp4?token=VlY8Ng3kLMWCM7YXivlreCwaY98cB8w7WvCcxqebhq9YQplMgkV6EGwX9Fy7QyTh3rfwkcunmNhNlLsusz_ywqJNoTxqosBUtDmCE--tZ3_qJFF14ozSLQceY6V2Ak9V4tPTW2ogvAWfkFU4FC23nIcnVqwoZP5c8g4X5J1o9cfBjiY8x6b7eVLPzMROlnsVp0rQrHH-CS1pzNGWdxAbqxWgJKq46tgpxw_eLIBl9xDfZ2z3fSFqKv6LVxw_85DBv8Jhb6PWUqL-lWcGzwoCqwwunVPxETwvyfpOgkJfujsORHbzmTnZFtbFFWPcjr3z69hq5WB5xw-y4x4o442W1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6bcd7de2.mp4?token=VlY8Ng3kLMWCM7YXivlreCwaY98cB8w7WvCcxqebhq9YQplMgkV6EGwX9Fy7QyTh3rfwkcunmNhNlLsusz_ywqJNoTxqosBUtDmCE--tZ3_qJFF14ozSLQceY6V2Ak9V4tPTW2ogvAWfkFU4FC23nIcnVqwoZP5c8g4X5J1o9cfBjiY8x6b7eVLPzMROlnsVp0rQrHH-CS1pzNGWdxAbqxWgJKq46tgpxw_eLIBl9xDfZ2z3fSFqKv6LVxw_85DBv8Jhb6PWUqL-lWcGzwoCqwwunVPxETwvyfpOgkJfujsORHbzmTnZFtbFFWPcjr3z69hq5WB5xw-y4x4o442W1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇲🇽
حرکات موزون بازیکنان و سرمربی در رختکن مکزیک بعد صعود به مرحله حذفی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/94639" target="_blank">📅 11:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94638">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b6c764c3b.mp4?token=WeTfPmtZzqxyPZwhp0eUhw7MCejS4lHlLOCeU5D7b25FGSMTzAe5Z0vnQDshs1BQQKh9BbiLQmxZDRDpMKA7fcbP-HoyIjcyOlak-MX9p0Re6GdK0AZPUBRGxnsgCyX__blUXP2GXua6uUxkshNIXFui6pIlC0FbritFW8JeodHTZTUjr_sv1TZtJNdU3O4aBH-BNyZnv1rQ7CBOUz7UvkO3QT38J0oUv-beBdsb2BKINZGoNiDjz6PtSMIACv1H_nW9LH1e18DqVu41ewGgZU9agZgMNrzjDD58MZk8MoCqkZczvYBzAT3Y0df-LElKtF8XgNWH0LZrwxXdxnTs4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b6c764c3b.mp4?token=WeTfPmtZzqxyPZwhp0eUhw7MCejS4lHlLOCeU5D7b25FGSMTzAe5Z0vnQDshs1BQQKh9BbiLQmxZDRDpMKA7fcbP-HoyIjcyOlak-MX9p0Re6GdK0AZPUBRGxnsgCyX__blUXP2GXua6uUxkshNIXFui6pIlC0FbritFW8JeodHTZTUjr_sv1TZtJNdU3O4aBH-BNyZnv1rQ7CBOUz7UvkO3QT38J0oUv-beBdsb2BKINZGoNiDjz6PtSMIACv1H_nW9LH1e18DqVu41ewGgZU9agZgMNrzjDD58MZk8MoCqkZczvYBzAT3Y0df-LElKtF8XgNWH0LZrwxXdxnTs4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
اقدام تحسین‌برانگیز یک‌پدر ایرانی درحال نمایش فوتبال برای پسر نابیناش که در رسانه‌های بین‌المللی حسابی مورد توجه قرار گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/94638" target="_blank">📅 10:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94637">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f084797b56.mp4?token=DFMztJoafKj12emglTrC-zl4c9DaUhn3VTgK90R-iJCDuHvoyEl5I7fMSdkwVCPKsDGV7JFen4lcboVi0sxoIklt6s9AMrxtL1ngHDxviGxSbqMF_N391_pxMINdOyP8cOeUPQANF1RZfxc2Ww90dTsbp6-yxkbsmHk6g_n8pXGS6ASq-ihbJcrSwi9WMIVBeqimoRMl7HO5hSjNVaoIE0SDGpsCgwIc0GhiNb332hq0W08J9FBnIn6kjh0MCMVO5io66aDMxSCqEurPIBG0FKzPazXTDuAxrcRHu8rgQ4tTOFlJEZFaNKW55hm4JjKOmB3lAVgpur3pcqwL2OYQ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f084797b56.mp4?token=DFMztJoafKj12emglTrC-zl4c9DaUhn3VTgK90R-iJCDuHvoyEl5I7fMSdkwVCPKsDGV7JFen4lcboVi0sxoIklt6s9AMrxtL1ngHDxviGxSbqMF_N391_pxMINdOyP8cOeUPQANF1RZfxc2Ww90dTsbp6-yxkbsmHk6g_n8pXGS6ASq-ihbJcrSwi9WMIVBeqimoRMl7HO5hSjNVaoIE0SDGpsCgwIc0GhiNb332hq0W08J9FBnIn6kjh0MCMVO5io66aDMxSCqEurPIBG0FKzPazXTDuAxrcRHu8rgQ4tTOFlJEZFaNKW55hm4JjKOmB3lAVgpur3pcqwL2OYQ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
🇳🇴
شادی‌ جذاب هواداران نروژی‌ در‌ جام‌جهانی به بیمارستان‌ها هم رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/94637" target="_blank">📅 10:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94636">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🇧🇪
🎙
تیبو کورتوا دروازه‌بان بلژیک: در بازی فرداشب آماده گلباران ایران هستیم چون برای صدرنشینی و صعود باید برنده شویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/94636" target="_blank">📅 10:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94635">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d6852b83.mp4?token=Edk5YRGQWTpBv3W3IqEVdEvPjaKa48HA7rAdheQJLerbJmStfQILKRqOf5v8Z9DgwH8KapJLcdvHTPi_1k0KehAFDeIrV5wJJdnNyDScZMe5b8rRqnf1beFHN5TV8NB2PN3pLyeZ7zArqPbEBB_YhdGoOz5lra9HB99tUWu7EbXcExj0X6iOQg4b_j2MXAuf5P53Z8FdVByMVcAZ-JkfEnVU5vpMQ9Dt8BtueGOpreHlNUtaY-kXpa8cCMQGBU5mKh_AKAC-QZXyrK5jiZTq7npB0WBH_GP3vpuY2itTA7skDRCsWOGwu4qcgqJ4CJD4kfUfZ9caOzNoKSFMQwWcLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d6852b83.mp4?token=Edk5YRGQWTpBv3W3IqEVdEvPjaKa48HA7rAdheQJLerbJmStfQILKRqOf5v8Z9DgwH8KapJLcdvHTPi_1k0KehAFDeIrV5wJJdnNyDScZMe5b8rRqnf1beFHN5TV8NB2PN3pLyeZ7zArqPbEBB_YhdGoOz5lra9HB99tUWu7EbXcExj0X6iOQg4b_j2MXAuf5P53Z8FdVByMVcAZ-JkfEnVU5vpMQ9Dt8BtueGOpreHlNUtaY-kXpa8cCMQGBU5mKh_AKAC-QZXyrK5jiZTq7npB0WBH_GP3vpuY2itTA7skDRCsWOGwu4qcgqJ4CJD4kfUfZ9caOzNoKSFMQwWcLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
🇲🇽
🇰🇷
هوادارای مکزیک برا اینکه کره‌ای ها ناراحت نشن بعد بازی دیروز با پسراشون لب‌بازی داشتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/94635" target="_blank">📅 10:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94634">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7mx3IY70F46cqT_ka0iGAMnUMhcTTu9HsA83Q03LTCUlaeJa25qmeBlqMwqdKxeK11RMKD60L18s2Ceu21IG9Hz-h7xu86FF5CBRkZlNL0ANvOR4234GC9TjgbmZFG8ZjovgRtoAbRU8TWaKcM5Ovj-Vq1locBipq4FH-6J04p5JL-ZanO-yxt5r5kdaVzmHiyLGMx3H1oz7jjBliiaB8v6HYYH8To7NerWadq6ZoOIA1BE1--B12Nvphhra4TBmYrpEQWpLSH2vJBdP3A5Ez_-aTAyB0fHbZou-W1FahoGOylcfXI8FqtvGcEVcDdGHltpspJormfBo1EteYClJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇧🇷
#فووووووری؛ شایعات رسانه‌های برزیل: رافینیا بدلیل مصدومیت از ناحیه همسترینگ ادامه جام‌جهانی را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/94634" target="_blank">📅 10:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94633">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhm1ZoCJ_4nzynDTFDtH5FSqI73aHnG04oPfk1HXWZNo50-ztkOs1J7p22uKTd4z688gxjZRypgg9AZNkmelWLCanR63Pnusp7MVbNvZ5RjanZqkqBHjGig9bhbmOYBEGVZm28D8Dj8Lu3JZwMO4v5WQE38a8PAw8RtTFUJQJ2R19jRGIrTNDX77_Ttb_L0DV-B35E9bVyXtIVxhH7q_j0Z8OE_q7yVL2NzMM-9_sZPD9Ckdt4UXF5bz2ca5XP6y5rnWtnQyG72UpgiRzejYNAMS1f9RiuYPV16MtLT2CKGpF_qO4ZPRFrkWTdQlWlVdMY6tXWBLkcWSz71s49C0Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
فوووووری؛
با اعلام آنچلوتی نیمار هفته آینده جلوی اسکاتلند میتونه بازی کنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/94633" target="_blank">📅 10:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94632">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060b592f3d.mp4?token=XAB7QIBGpCQdmtrocAbg_APwHmNvw41NvPIPRafHa86tr5va2ugXd-tOvxxqyD05VJcVQJKwnIG5DI966n2LN0TdxOKD4kyzHci_EZ2ERtJ8YGBd3E-WE7dbKJaruMn-27-tW64U5snewPzjv8qYK2gep9TIkyY78sw5l7H-JtsDgGRUu2gNwTRUfIPCsTzlnmHhEw-jAjcIvW43NsSCbH8wOy4rnjd2szZqanRENpjVRVpIBdoGN_GS_-a8QugqvPgPNjg5Tv_BE8yQdUrTc9rHcyWNQxJ-WCGcUPlbrUEEj61yG0pA_4nLXZVY3ipeLVi3nEuOIi7ZVIdnWVuTRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060b592f3d.mp4?token=XAB7QIBGpCQdmtrocAbg_APwHmNvw41NvPIPRafHa86tr5va2ugXd-tOvxxqyD05VJcVQJKwnIG5DI966n2LN0TdxOKD4kyzHci_EZ2ERtJ8YGBd3E-WE7dbKJaruMn-27-tW64U5snewPzjv8qYK2gep9TIkyY78sw5l7H-JtsDgGRUu2gNwTRUfIPCsTzlnmHhEw-jAjcIvW43NsSCbH8wOy4rnjd2szZqanRENpjVRVpIBdoGN_GS_-a8QugqvPgPNjg5Tv_BE8yQdUrTc9rHcyWNQxJ-WCGcUPlbrUEEj61yG0pA_4nLXZVY3ipeLVi3nEuOIi7ZVIdnWVuTRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁳󠁣󠁴󠁿
شومبول اسکات‌مک‌تومینای تو بازی دیشب با مراکش که حسابی وایرال شده
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/94632" target="_blank">📅 10:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94631">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4864edf2.mp4?token=aBnyksHryxPa-xZZe035LatrtXK-jYqPmQ_Vr5G_CGmauL213OoJjYacHpykHG_ZwcCuVaQz_i9rklrMioBP-WQ1fIPGnbNiuWQLUaKBYywTFoFPNSW9N30-5WIHWfEhOj4DRE7kh9I6ZZeByTjwgaHnLNz2gu1MVArJUfMdAR9eiQRfIO7L5j6YsORCqQGfODIBb5z1ItlCAZZBf1btLW86SzDAWeKyvS7FQL0Tm6EssyTvpktcr1vjxO69_zTJWvT9kkE6w6YIS9PqEQYLSXcGlgTGCT8BUF6xYbxGRV2QwZ7eHzcvTKigSXBJ2jECxh41GNQ_xUPuLUjM0vYoXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4864edf2.mp4?token=aBnyksHryxPa-xZZe035LatrtXK-jYqPmQ_Vr5G_CGmauL213OoJjYacHpykHG_ZwcCuVaQz_i9rklrMioBP-WQ1fIPGnbNiuWQLUaKBYywTFoFPNSW9N30-5WIHWfEhOj4DRE7kh9I6ZZeByTjwgaHnLNz2gu1MVArJUfMdAR9eiQRfIO7L5j6YsORCqQGfODIBb5z1ItlCAZZBf1btLW86SzDAWeKyvS7FQL0Tm6EssyTvpktcr1vjxO69_zTJWvT9kkE6w6YIS9PqEQYLSXcGlgTGCT8BUF6xYbxGRV2QwZ7eHzcvTKigSXBJ2jECxh41GNQ_xUPuLUjM0vYoXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇿🇦
بازیکنان آفریقای جنوبی بعد از مساوی مقابل چک، جواهرات و ساعت‌های لوکسی به ارزش بیش از 50 هزار دلار پاداش گرفتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/94631" target="_blank">📅 09:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94627">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jBI-LCEuVYw7Xvy44Rwp0hcToss2ADiS0HVsWetqaw-DNeQvkYPCW4VF5tbLGddcjwFq0ng-XrcDfll59YfciCMXo2zoB5jvHIwSosOZQkO7JzGxJ2_fYhpIrz24blNczeM7m3jJAEG-49x6BUTOCHnjktF0ayoD9lBaTrULLMHXUPhqgIWOfc0CtBm8XpDBHNwmhbu7RqdQ46j9Z3T95P7EISDJJBBrT-rjKMn69eVZHGD8PArD8phkivLB_V4FV9SvuwIfNAXnLj7yWp6C2pqVQPBPPqxyfU1RRTKcPAUbZqnALGjlWP8QTiv-DC-osZqx39YnWCsKs4EFJp2RGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SKN8rdyCaI6xfgD3fsi-I7o_whE-5TceY5-epklCZyCiv9yRlr1fxIqQghgrRjMT5SAAqD8EZJeB57nOUNH3Ofa-Ooia0bSMFLzDAB0qSFd1T22D2M9BLoVd0ggWqRj25Ss9KmVMtF3NEjjcs2LS8d3zEqo9aU5nYS9C9X4ZXh1TOst_2sDE92YZttdAVMfB4QrjSrVAOjhWIjmFBC_jmr1HfIP499lMY9BSejpycl7XwhSCR5Br_wfO5iY_cXUfVnaHC2AH5DNrLiZWKWpSJe0fxhkyYNRkW3ENreXyTxH58PkxKj7SXZ44OuOkEeoKF7oHFsPXY4Yt2FZ5aqN65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ADSXcIP8m4nRaLxC6Mpsb_wM8HESP40KovkwWx-yuKs5KnOcUtdX7xuXyyZMS72xuLVwdfGwl6F4TAKbz-5ETVRXYuSANRvX4MzeB1AeydlwZgzRVJ4BkIUDB0NwsDYCmcz5Go_ltHkkmWMPX_UmKgQoVXuV5LC-sallzGCOh6xZWZXp8MWDoiQkjUcpEMOTmsaiqpSPzF6cRpfS1T01YE6MZDiCAnM087_EgVJpmXjZEB1rjPDjTTAsueDOyiPz_j1vPSop1xBliTVx3eIVODlEycKGGThO7j1OPDeebApIWLqgOHtKVQIG2fIgY5tcrY4DlOpbcZitrrtgFYYHYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EklHdRlfGbEiUl2Tw9QGc_UQNglvAADgnGlh8T7olHXcvN1G7yTmTadGHVrYZMcQTbyVuXinaTvCZUhvq9i0hKnSFYNAFerp7n9R4iaQZOgk-ZtRcdAREet_WAu7J_-KU0wC2x4oe1fPuMqTdi-OiHcolCgpG7h0Yt8RsVYikJBAm744C3KrmEdNN6VEq8xpMSI3F4xTm15Ry57d-TKb9kc7lqX6JGkJG3E85uS0oDlDPSrl4T19Khl2ZlTt5eEw1wrlVeLxDRPSkDJBKkl39Nbdp1BR_4XAcWRAByB9tqR6aG4LEh_zjRSrmIQOW4uJMIpv-XF1srhvd7Bs2MaW0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇹🇷
هوادار ترکیه در روز ریدمان کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/94627" target="_blank">📅 09:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94626">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c7c76bf8a.mp4?token=uwkFtBKD0A4dwxbz0HUj7GV55sNV4g2KDeK3paItywCKjEqr-3dHmp65MDZCLL21pZV2daPlJt6YyKAuwJ8MuX3xrnInYA5qB1mAwi91dT64SBI_pCCcLWcDESkgi1B2qyrr6NDTmeYMcoTph2tG9hpZyoPT_RRVgbK-GN7JQIzwbSxWtUIHqKdTc97zR3EVvgvazCzo7_Qx371kfWy4mg70BrUp3pnm4f1iT414Za8YZT1NqznSVrFesKjtPTVfWkPpdp9_f7VD-uB5RKw2ZTQ-X22NrcKRff92X1uS_2Az5sGDaUoM0h2dpYvwiFyHZK_zlx_vs8n4pWUl20pOWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c7c76bf8a.mp4?token=uwkFtBKD0A4dwxbz0HUj7GV55sNV4g2KDeK3paItywCKjEqr-3dHmp65MDZCLL21pZV2daPlJt6YyKAuwJ8MuX3xrnInYA5qB1mAwi91dT64SBI_pCCcLWcDESkgi1B2qyrr6NDTmeYMcoTph2tG9hpZyoPT_RRVgbK-GN7JQIzwbSxWtUIHqKdTc97zR3EVvgvazCzo7_Qx371kfWy4mg70BrUp3pnm4f1iT414Za8YZT1NqznSVrFesKjtPTVfWkPpdp9_f7VD-uB5RKw2ZTQ-X22NrcKRff92X1uS_2Az5sGDaUoM0h2dpYvwiFyHZK_zlx_vs8n4pWUl20pOWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇲🇽
مکزیکی‌ها داغ و جذاب بعد صعود از گروه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/94626" target="_blank">📅 09:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94625">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d20f3a10.mp4?token=okDXcyanpQQ04OEz0uauUihDpbQj4wOQXmOH2EfmqXkIma5oMyHXOCYWR32I5AFMMe7FmTWuf3ondfSfXgGmz_To40UCKkY8kxK3RxI-DqVXWQN4DwErFytEFGBvEw4zqL_4HkV1APMTUhlnPHKt66k9yZSS4rbGEcdsIFVCLNDLfJMSOo6wC3NLQ_hRcQSQJ-RAV7RcVtGmjYml02fTSgZLlUXmBEaHyFN_DhJ5y5cV0rKfD_RXvlDlyTupvw5lGN1M5Hyo32UdTw1SwxmnJqyAQj2hlXnQ8WGW5J-Fs9bpUcldg5QsCammVy-XKJP8GWdj3UcJqV23Vwflma_QaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d20f3a10.mp4?token=okDXcyanpQQ04OEz0uauUihDpbQj4wOQXmOH2EfmqXkIma5oMyHXOCYWR32I5AFMMe7FmTWuf3ondfSfXgGmz_To40UCKkY8kxK3RxI-DqVXWQN4DwErFytEFGBvEw4zqL_4HkV1APMTUhlnPHKt66k9yZSS4rbGEcdsIFVCLNDLfJMSOo6wC3NLQ_hRcQSQJ-RAV7RcVtGmjYml02fTSgZLlUXmBEaHyFN_DhJ5y5cV0rKfD_RXvlDlyTupvw5lGN1M5Hyo32UdTw1SwxmnJqyAQj2hlXnQ8WGW5J-Fs9bpUcldg5QsCammVy-XKJP8GWdj3UcJqV23Vwflma_QaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
بدل‌مارادونا رفته کف لس‌آنجلس سفره پهن کرده چنتا حرکت میزنه مردم بهش پول بدن
🌟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/94625" target="_blank">📅 09:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94624">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🙂
🇹🇷
آردا گولر بازیکن گنده‌گوز ترکیه هفته‌قبل: ما از هیچ تیمی نمی‌ترسیم و فقط به میخوایم صعود کنیم و مطمئنم موفق میشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/94624" target="_blank">📅 09:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94623">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7068c129f6.mp4?token=pWwpPSoyo81dfxsH1lDAvtxsomizfEHLb9Z6v7cJAmnULTQyC_u8FnOrVRaFYSkAFagMbW0fidSiez7vPLFMFqkaEDd77B1at8ErvHg04JyBho2tM0plvh5Cso3BtBfPvUvCpQ-Uegon5Pl7aop_lAXnqh5n1yjGbk2uM1Jc1LPi4vtX9HCzigtALFz5EW2anb8XhxMbST1e0i_vhhNxffHNbFvwPGZxVzxcIZI1cq4otAdu1aCDSKhAGLCavvVlv6hxBZxfppCWy761YP_RIUVCp3ctm4TOzsVAMst2HykutQLk8HlUMxkO0hsuqZu_mMT5s00SOItFJzSNTCmlrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7068c129f6.mp4?token=pWwpPSoyo81dfxsH1lDAvtxsomizfEHLb9Z6v7cJAmnULTQyC_u8FnOrVRaFYSkAFagMbW0fidSiez7vPLFMFqkaEDd77B1at8ErvHg04JyBho2tM0plvh5Cso3BtBfPvUvCpQ-Uegon5Pl7aop_lAXnqh5n1yjGbk2uM1Jc1LPi4vtX9HCzigtALFz5EW2anb8XhxMbST1e0i_vhhNxffHNbFvwPGZxVzxcIZI1cq4otAdu1aCDSKhAGLCavvVlv6hxBZxfppCWy761YP_RIUVCp3ctm4TOzsVAMst2HykutQLk8HlUMxkO0hsuqZu_mMT5s00SOItFJzSNTCmlrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
رونالدو که تو اردوی پرتغال حضور داره، جورجینا رو فرستاده خونه تا واسه پسرش که ۱۶ ساله میشه تولد بگیره. پسرش اینقدری بکیرشه که حد نداره
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/94623" target="_blank">📅 09:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94622">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xn_LCKyG2muK-Fi66jt7V7s8vyyylcCr8jVxgjaiUmpDdy_NCoZfvmSW9whkRdPjhq1YoHK2jRFAic5U6W76mGIcRYFcWFRk5N21DfnX0WLi7kQX5ogwZ4Q0Y1VR7xdO3ZMaN3jLbNd1Ww8ejm4X7eOi64m0zuZ9DiWw-HJGaTR82XxMWyX1NfHYQqb2QoVBmVeBcr14PCmLwR2ikrjoQZ3mgkskK_dd7clpSWg5HQMYZcKiuo6AtWSlEF9j2rMZH5cv42AmGoGZNrDKwEjYz__YncfY6eYmpos6jtz41Z93oFOxz5OuEEx9MNJ0MBh64n66BlTZUxj2G-A4mDapow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
ترکیه در دو بازی در جام جهانی:
۳۰ شوت مقابل استرالیا: ۰ گل
۳۲ شوت مقابل پاراگوئه: ۰ گل
۶۲ شوت، ۰ گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/94622" target="_blank">📅 09:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94621">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpTuJHr_r6-0ubTSfNoB-fVKLDufEdXFxo-N__Vo4Vx_wk-fbuV_hWxhJrP3kO9S1Us3JvRxG2HMlEIfpK407KygRPvIJYx7WPA-4dVdn4ztZ2wZsfHGCr0asK5nxZduKV3v4tTgpwnAit2I2cLRM73D_4gmTktrmw4u4VgMbx174WYAq8fE7zyC7L3OdWPysv_hMNqmguZX4G-wMpuBYCjcRQ4Pp6PunRkmoAvkEFLeFuN8TVfpOpEGOYSG2m3dakBiT5mqcCSe5MHvWMvgAHdptvnYfMQt_prXEmDnrOmDdyRyaLitq5RLCt3Ik-_SvK09PH6Nnr9zVJH9gOUFnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
نمودار مراحل حذفی جام‌جهانی؛ آمریکا و مکزیک به عنوان صدرنشین صعود کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/94621" target="_blank">📅 08:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94620">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fy6amzp1J4bK-J9J8YDDn368kLaAm3FMV5IPZk4ngyuWUHQnZJkb1dViDpqtCeB3gDZZ5xJ16C9q4vv8tPdZtLN5_Yz874GB-DMud7GoDUOvMKCHyGaOKxdSn20Xl518Uc4TQw5fqofdbCLgY8DoteUaWohC8sI1qkIn3q5EzsxyTCC_rNwl2yaaNE95CGw15azFzuIE0lk5FjUnR6zULLwwV6L-h4oizkOSiqTRtTlc7ia3L_2hnmFjWY9Pn_GgRXpTG3D6ZzA4Zh-egx8n-o3p9efRQhydbrksosHJ-s2eHecVEvKIB7JBjaLiXz2reOlSGyJ1LvzqTW27wSHAVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🙂
🇹🇷
آردا گولر بازیکن گنده‌گوز ترکیه هفته‌قبل: ما از هیچ تیمی نمی‌ترسیم و فقط به میخوایم صعود کنیم و مطمئنم موفق میشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/94620" target="_blank">📅 08:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94617">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5zG4ZVX0jS3Wmup3aueKEaupRhM2QX8UreUdDmdTGZLDEQl0L6QOME7Kd5Lb0_ECbWN5s0Fm-jpJ0qyMx2xRSWz15W87D8Sfnhy4I3Gm_sQDKuxVBTuKhoxshyIGH5hJ9a2qCgc_1cahXW8nt2nMZU7QuzQWvDKZex19hCVCGz1pQ2qhvLeGDp-174eqdbBgxKLCg9a3UZ5ttmOHQafgzzCPGDY2YNarDa1m1ob7RRMPQv_8xrEXu6rBtHU1addkp4wSJkcNuRPp0xAwOQ5mGdpC6App81dAq9CNL6PxNArUvAZsCl5coejxd8q9aREsCEI9QbTmh2hlBJkeQAohg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yl081ZD4LtQiuOqFVWm0n7Bu_0YaYdp1Lkpl2io6YmQRBd4UZpM1NQ_F6w8FgubuyyE-NNnc9koMj7BRQkL_XZt1fSXQMl3X2Y3qBABcYYLSEVquIz0JOFYgv4RgSrcgJMD0Wbp5iO2oJ9QVVJSCtRPF1LOwRS7Sa7s541ljPaMIat2-ChqYKYiSitPQWJlxktWGm8owDXzA4oQPnMH4dr_NF6YNi_sos3kabApjGigWYcAydItIlgEM_rztwSEgvCDIr3rUmeILEjpuyagx50uKRWKHusIlO3CAqgu4kbuhNprykDVpTe0xs4OQzqoBfUfVQr1HnhLVqARYFegujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/juqVXTs1obF0hqCrhE5wytI9_50cp9Qct4hNbh__Tv3275Fg6CQoF7431-wBk0DqJDSDJsN1cTiMDuhV-eGu714-n6x3Ky-6c7ynUUVlHbXeg9N0aGqruY5N8Y3JpDWYNk6iGad298aTVOuipSoBORgK1N--axAup2pjNxq7ghYiZFfOkmz5TwGbZJTpuplTEJSr3zT4dp0AzUmFNF2SJB1CeFRKSUWEuHl1ubYqQVJSIpnZJ3O-hE5-CmcyoErWIOA41E034sZoVfzB9mGC-yEpRg5rq0PPyBOEIM4r6fiWcrR518RT-e5ihs3S4yB6kzhIwQERapPzFMg9k6Ff8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
حسرت بازیکنان ترکیه بعد از حذف از جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/94617" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94615">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3vM_eg6ef8bOPzgygL6rdaEqfcTDEfQrPSaV73vex1qgjZydW-ip3HGOQsCm_ofdfWj8RCFAkJ4lZ_4iLUuLJ05TbPJSDBmPwIZpHtZ10AmWvOJxuXWPZlPrLCZJ1ykqW4DdEywneaP3GkGrt8k_mNA60GbJM0XTZggoLiyJvV16wCtAyHrVGQi0kG7eZias5kNWtBKvdVWaV_Xc2gz9unxxlft-7NOGWCuMjMlkbh6IdEctw977vQJ36oq40Ul0syTdhY2QAR2bBBuztXC38rv7YlHEn0yOGkCiEofKXfBrqSWncvoLWMFhwMjE3RVSRXi51WK3ktuRP_ZjWNULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|مقاومت فوق‌العاده پاراگوئه ده‌نفره برای کسب سه امتیاز مقابل ترک‌ها؛ شانس با تیم آمریکای جنوبی یار بود
🇵🇾
پاراگوئه
😃
-
😏
ترکیه
🇹🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/94615" target="_blank">📅 08:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94614">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1VRDSAHga_r08vIWKXqB92aRPpwkD98R-BrGROT6m3pZBZbuXwk47oTkpyuBCtpT7aSQ7YrwMvYfJFHoRvSVFzwd1S5gTjrPHntfoFe3Mj0TeoUt1G_LBROWG2R6_BuT1fiSzUg_H4dJ2TH7GSEvP3QqeHOGkwMhmlKk75PjHZmMVaFcgM3Oyp4FFIMkRt78enuVBm4xX7mgfEeUUvNZafAeTkoObSWKoktWPewQ7t7eAPYp_LF-7z5ZzV_rJDc-lYYsBmblcHRqKgu01QakRmA59v-SdAR4qQ5Ni1uKs_kvxZ5YMFZ9UhbK7SfmgE8b6X7yv5ElLhp5HDo3OFRdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی
|مقاومت فوق‌العاده پاراگوئه ده‌نفره برای کسب سه امتیاز مقابل ترک‌ها؛ شانس با تیم آمریکای جنوبی یار بود
🇵🇾
پاراگوئه
😃
-
😏
ترکیه
🇹🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/94614" target="_blank">📅 08:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94613">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
۷ دقیقه تا حذف تقریبا قطعی ترکیه</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/94613" target="_blank">📅 08:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94612">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🏆
🇧🇷
#فووووووری
؛ شایعات رسانه‌های برزیل: رافینیا بدلیل مصدومیت از ناحیه همسترینگ ادامه جام‌جهانی را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/94612" target="_blank">📅 08:14 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
