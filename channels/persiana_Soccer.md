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
<img src="https://cdn4.telesco.pe/file/bC8nGo8IFHZlc0sW81leGcvMS5Uvexffysfy767EXYUttGequJWde1AnYyJ4EFza-qJg4jn_YCXxZpBweT7ow3qkGDa73zsDb4gakyBNnJITcYnse0-XBk_1mPBHP-aBn-f4AvAoNYqH9G0DuPIULpmVKDh81uFmmOghuehFYdDFayqPbBhBB7H93570uKy0CVu5wNxOFiIMkvC0D9EsCDVEj42eOM-ciPx7J6VD9T25lJIAj8o2zJtaYg1TUdonVqU01b1-lMUrJKnpiQ8CMLi3rUterJEgHx04B7IEsA4i9rHjQVfamwiWXc44uwhCYw6qeo_HjgRdzHsp8M2d7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 498K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 20:10:43</div>
<hr>

<div class="tg-post" id="msg-31204">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b8e357fbe.mp4?token=g7wXQuAVCtvwTx54lTBJix11fCV9Ra9-A4QRKYy1VTAfXkpku5ARy_PF3NQdzSAHhhT6y9D2bpfzv3J9wugMwYWEhwn26egL62-Py-cSsnKJW8DgsFRRnHztymtUaUkwuUcvlfHMLHuxh7-X8saynQwObwOagRfLHd8zI3Hy55Ru3l24_l4M_XzjnymoCRksSbMvv3N6BbljuTRYHAvJMPWJkYC3iCG5UFWJel4Y1Squj8dW61sfSG97OTZS9NQCVkbwFkcyaH68RGTbi2hezosJFqS9OsV0PBI_9WR_4sBe964DoIe6s3ZRMYhBWDtD01q3VdZuoHr8ZLA7nSukZUrFs3HZoAtrF5les5TezTwpiTijQpmkb-rvbSf9_gPoah55tZXHiLpReeFuAMSUmKZNqWgdkC6VwuLrXLAh0lfy6vjBY-HIfR2upocJPdqqyTnGSz90VgTQloox0sudJMqbBdhBjNkZkKYOdH9eAmThz8_MllUJKbVBpkUbd3hDrUWH60IiwqouORclpy5RysTw-D_cGtlcKdRKkfsMi2NZQwu_tm1zE-MN7P2ReJy1HlBSJU6kdt88kiPWLchVEmiUXJIdM1uWXyItr_hBdRohYZBZ1cRGzbFw69-lboJA3bFu2YU_pMT11qiOzYPPBwc0LVCNFonWfEiecB8WEVI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b8e357fbe.mp4?token=g7wXQuAVCtvwTx54lTBJix11fCV9Ra9-A4QRKYy1VTAfXkpku5ARy_PF3NQdzSAHhhT6y9D2bpfzv3J9wugMwYWEhwn26egL62-Py-cSsnKJW8DgsFRRnHztymtUaUkwuUcvlfHMLHuxh7-X8saynQwObwOagRfLHd8zI3Hy55Ru3l24_l4M_XzjnymoCRksSbMvv3N6BbljuTRYHAvJMPWJkYC3iCG5UFWJel4Y1Squj8dW61sfSG97OTZS9NQCVkbwFkcyaH68RGTbi2hezosJFqS9OsV0PBI_9WR_4sBe964DoIe6s3ZRMYhBWDtD01q3VdZuoHr8ZLA7nSukZUrFs3HZoAtrF5les5TezTwpiTijQpmkb-rvbSf9_gPoah55tZXHiLpReeFuAMSUmKZNqWgdkC6VwuLrXLAh0lfy6vjBY-HIfR2upocJPdqqyTnGSz90VgTQloox0sudJMqbBdhBjNkZkKYOdH9eAmThz8_MllUJKbVBpkUbd3hDrUWH60IiwqouORclpy5RysTw-D_cGtlcKdRKkfsMi2NZQwu_tm1zE-MN7P2ReJy1HlBSJU6kdt88kiPWLchVEmiUXJIdM1uWXyItr_hBdRohYZBZ1cRGzbFw69-lboJA3bFu2YU_pMT11qiOzYPPBwc0LVCNFonWfEiecB8WEVI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
ویدیویی زیبا و دقیق از آنالیز بارسلونا مدل هانسی فلیک در فصل جدید رقابتای لالیگا و UCL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/persiana_Soccer/31204" target="_blank">📅 20:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31203">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbbf119a08.mp4?token=rNf26FXw7py_uU5IU6JluPsav11AJfsyYeXvsWSO-UOfVTa8vz9GYteQDlSKUijBhnkjo73ftR67PQoOg1IVnpEKg5Gd4UasEEcsFChBtInu-ZcOSudhTv7L_d1VbA9YJMw7u_XyZRSyBoU5RpT5yaQF8TbOVEVBw19qr8njfJW4F_ZdY5EEf1MEqbzLy1J4Thpz5L4WRUtt4kCn9EeU3hxEc3acZGtPP47sWWfCriArOIcmU4QKYTnYhp_1GmQqu447bMgfSSpoz0NW4rjDep-xEOzsuXwHKtoB8tGkibmP2AIfQEvlTsLg4wUnxYD8zJqJystWvPtkudmgvwWwvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbbf119a08.mp4?token=rNf26FXw7py_uU5IU6JluPsav11AJfsyYeXvsWSO-UOfVTa8vz9GYteQDlSKUijBhnkjo73ftR67PQoOg1IVnpEKg5Gd4UasEEcsFChBtInu-ZcOSudhTv7L_d1VbA9YJMw7u_XyZRSyBoU5RpT5yaQF8TbOVEVBw19qr8njfJW4F_ZdY5EEf1MEqbzLy1J4Thpz5L4WRUtt4kCn9EeU3hxEc3acZGtPP47sWWfCriArOIcmU4QKYTnYhp_1GmQqu447bMgfSSpoz0NW4rjDep-xEOzsuXwHKtoB8tGkibmP2AIfQEvlTsLg4wUnxYD8zJqJystWvPtkudmgvwWwvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گل‌دوم‌سپاهان‌به‌فجرسپاسی‌روی‌شوت دیدنی احسان حاج صفی کاپیتان طلایی پوشان دقیقه 38
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/31203" target="_blank">📅 19:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31202">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFMqi4p7NulyZI266KXlG0B-bDoNilO_tANKEzjeU2r62-gu3QeNAMKcJtXGzhCQZXsas_nkLeiL81zR-HLWfHqEij1Q9cYl-knGqCRx-tm72Xk4f08n9aju_IwrSFNAGBekKck3GW7oq8dqzKhIkuupw7_RFlsfYZjKtEmwqlgrdpYmX7IkZbiUcSM7iEZkrOMz9nWG_JcbW7_RMPnidwyLkZV9jed88awooFUfM2O8-vtZUCjVYS7jUlgCfTMOe2aph-2Wn8gHWhVgT8wORVuVs-t9zdSrEPtfw7CO3s2CNuxU0Ufub8RReV7Q4Bt4b8jtYGVWr3jNKceHSLyVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خرافات جواب داد؟! یاسر آسانی ستاره آلبانیایی تیم استقلال به دلیل مصدومیت در نیمه اول دیدار با تیم‌تراکتور دربین دونیمه تعویض شد. آسانی چند روز پیش با حضور در برنامه عادل با او گفتگویی داشت.
‼️
پیش‌تر نیز عباس‌کهریزی، پوریاپورعلی دو بازیکن  آلومینیوم و پرسپولیس‌نیزدچار…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/31202" target="_blank">📅 19:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31201">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194218a84f.mp4?token=O5D-e-J4yRihxga4lFNneyXo9wUwIbDwjILEi6j7-PNXXiUZRHBQq_DxoTHnlbQ72xNsnnNIg2BeWrSulb259QAe5f9-Mn16pARlFnFKjkCGKy0zgG2lOlhggbKyUrC3FG8wKyV_lB-skb2SkcqtyeK02p4dbMaUH3oExJNIFLFI-tEldGCAQMypHjSoSAjFnjTYMwzjC6mmk1tHx83YQTFjMgTkOXEfsqHGaduSnzheV4_7CySYGUMsG7FqrVGU_LRTY3on8-yBoaQ-sf_ffSxmTV73FsS3ZpGNn-Eh0aT2C3pT6s2PQ_7dNA52Y9XQ2hlkJlyJhvhrVBAHe6Q0OiAzT_3ucKGAgypdVMJZwhEm9OwDX9JWbhOhugiMhwYXVtXxrhlGam0OX94JsRkybp2Oizy7skbCFflOrFEft7F4W7q5SI_cTnFd5gohQ8EEihzRMN9cjruAxkwjTd3xt_nZW4Y6b-UNGVEp41OfWihgV7Ogzp-H4NF93HS89--THzbk_vvOQxEYUmDZrOudtxNQDc5W0-IHZ5s1s5ELpr9hTAzJgOByWdtYErqhgxYWYzyEW-oig3h5KONGWEyBXgIuKp-BFYsFKy4X1jB-SxIxsYFyBxVykR7yV5w37HxiDMuxaadLLUiFCHNxSsjvqEJcM6c7RGs_Vd0V2vBBjY4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194218a84f.mp4?token=O5D-e-J4yRihxga4lFNneyXo9wUwIbDwjILEi6j7-PNXXiUZRHBQq_DxoTHnlbQ72xNsnnNIg2BeWrSulb259QAe5f9-Mn16pARlFnFKjkCGKy0zgG2lOlhggbKyUrC3FG8wKyV_lB-skb2SkcqtyeK02p4dbMaUH3oExJNIFLFI-tEldGCAQMypHjSoSAjFnjTYMwzjC6mmk1tHx83YQTFjMgTkOXEfsqHGaduSnzheV4_7CySYGUMsG7FqrVGU_LRTY3on8-yBoaQ-sf_ffSxmTV73FsS3ZpGNn-Eh0aT2C3pT6s2PQ_7dNA52Y9XQ2hlkJlyJhvhrVBAHe6Q0OiAzT_3ucKGAgypdVMJZwhEm9OwDX9JWbhOhugiMhwYXVtXxrhlGam0OX94JsRkybp2Oizy7skbCFflOrFEft7F4W7q5SI_cTnFd5gohQ8EEihzRMN9cjruAxkwjTd3xt_nZW4Y6b-UNGVEp41OfWihgV7Ogzp-H4NF93HS89--THzbk_vvOQxEYUmDZrOudtxNQDc5W0-IHZ5s1s5ELpr9hTAzJgOByWdtYErqhgxYWYzyEW-oig3h5KONGWEyBXgIuKp-BFYsFKy4X1jB-SxIxsYFyBxVykR7yV5w37HxiDMuxaadLLUiFCHNxSsjvqEJcM6c7RGs_Vd0V2vBBjY4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
آریایوسفی ستاره‌سپاهان به این شکل گل اول طلایی‌پوشان‌زاینده‌رود وارد دروازه فجر سپاسی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/persiana_Soccer/31201" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31200">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b6aefbc83.mp4?token=SPLRJ-a2vKzdj27nKNW2hW48-1q4M4XiUi5UOcHXqfsENBdzmRPBu5Cob91vWAThaFObGUSGM6MTIoWLzBuNfiXIKTU_1NfN-QeZG-YSfOYohc6ustfTINmavc5gVLvtqeVG9pygXyk2LqRo7BccbeT-_xUvrxjIUAeQ5-EYF_v6nLny2_adJ_1Z4eZi4SSf9MqA0wsuxra6keGRu2m4SqK1BdT5GPbGgGUwBqIHV8r-UK9A1a1CmQS6zCYpAfBh8ZxaygdT5HIQySzc_7DC0ESTOdyGcQ-kTewktRcUoO5Frr5IMWosfQtqTLuobIx8DvwEmIcmiNLdApz2LvHJUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b6aefbc83.mp4?token=SPLRJ-a2vKzdj27nKNW2hW48-1q4M4XiUi5UOcHXqfsENBdzmRPBu5Cob91vWAThaFObGUSGM6MTIoWLzBuNfiXIKTU_1NfN-QeZG-YSfOYohc6ustfTINmavc5gVLvtqeVG9pygXyk2LqRo7BccbeT-_xUvrxjIUAeQ5-EYF_v6nLny2_adJ_1Z4eZi4SSf9MqA0wsuxra6keGRu2m4SqK1BdT5GPbGgGUwBqIHV8r-UK9A1a1CmQS6zCYpAfBh8ZxaygdT5HIQySzc_7DC0ESTOdyGcQ-kTewktRcUoO5Frr5IMWosfQtqTLuobIx8DvwEmIcmiNLdApz2LvHJUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
سپاهان محرم نوید کیا امروز ساعت 18:45 با این ترکیب به مصاف فجرسپاسی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/31200" target="_blank">📅 19:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31199">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrLJNDEmu3Ch2skcHs6xqp11KUvd6f87V9miTvKFmDCMeqtR07pVlMz0GF-cbnSEiBMPuZhcfyhGKVkQ8jh3P-QLjhF2BSkRQ_E9CwG8BjWHTuQlgOSt1qs0bGflSTJd9Wpby38O2TELoGPuUX2b_zinzuMllFEU9xl1ZU4vjzwpIKixvR7slrFqtnXsUY4gZ7dud3DQyVFh8tqj1UZpZEgARGvZWwZYnR3A5VqqHsvRpW0g-7EWwgghe1vR8m8qQpHqf6wtQW9omVO2M--IX51YqjuvK12L8hhmOlqtm-3-l2mlYiB2tItFMmydkQEshkOafJLQeynX6PQTO4BA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بالاخره آبی‌ها گل رو خوردند؛ گل اول تراکتور به استقلال توسط سید مهدی حسینی در دقیقه 74.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/31199" target="_blank">📅 18:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31198">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1b0fadf9.mp4?token=acjvlU8kZ_kMgZuh1BFfOda9MRBJvwl3ZoJRnAezjf37g_o2iJUnMkOW8NXK7H1ht7Y1tRy-BWt0xNnuCebNyYKpieayrEwC-T588fUBfy9xTQNGoteAmNi_ofiWxwnlbCJje4tpcFINv3EhkJJVxbfv6qapLmzEGsvgP-zWu98Heg2aHqhNFcN7RI5P-y6en9vzsXPZpFTzQC9RdPYBPDl9eSmo01fpzk3A8loHoEbEw7BzFRItwz5WjO2X-eqBQs93qnII6lmkk1Fwe1_-BTg87bT7NOrkRsg-yVXJXw5Xsw810Km0xAHyrWwwFPutER1nLVVQqwEEodfhPoZ3Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1b0fadf9.mp4?token=acjvlU8kZ_kMgZuh1BFfOda9MRBJvwl3ZoJRnAezjf37g_o2iJUnMkOW8NXK7H1ht7Y1tRy-BWt0xNnuCebNyYKpieayrEwC-T588fUBfy9xTQNGoteAmNi_ofiWxwnlbCJje4tpcFINv3EhkJJVxbfv6qapLmzEGsvgP-zWu98Heg2aHqhNFcN7RI5P-y6en9vzsXPZpFTzQC9RdPYBPDl9eSmo01fpzk3A8loHoEbEw7BzFRItwz5WjO2X-eqBQs93qnII6lmkk1Fwe1_-BTg87bT7NOrkRsg-yVXJXw5Xsw810Km0xAHyrWwwFPutER1nLVVQqwEEodfhPoZ3Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل اول تراکتور به استقلال توسط هلیلیوویچ در دقیقه 68 که VAR هند بازیکنان تراکتور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/31198" target="_blank">📅 18:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31197">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d03b757a.mp4?token=UMAq3XnGFLcwqe1bhFxak370shKkDHghQT3IL_0F_F20XavHp-DpbdY1WIDa53_1vq4AksxYjRgSFAoasMkTlSRMUlr5xneOUK7ttXYj1nX12fYd163BS8zsasf-zd-UOg3eAXWAbOeSPBJZut6Hkf9Vz-spi_13C85_rsmdW2peYxfxDyHq4Dy0rYLefQwvpQGQhISScH1G_zmU1ZaD0LkfUfw6QlqU9t3CLS2avMCucjTHyM2L9xRdLTiRbVc8dam_7Vv6EU2MHKAkGeP392Ipp44x8K1nDTP744zwAm6UGw8L6m9dfAQep0pfqceGAbUY1ouOx_ZN3FGGjrZQ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d03b757a.mp4?token=UMAq3XnGFLcwqe1bhFxak370shKkDHghQT3IL_0F_F20XavHp-DpbdY1WIDa53_1vq4AksxYjRgSFAoasMkTlSRMUlr5xneOUK7ttXYj1nX12fYd163BS8zsasf-zd-UOg3eAXWAbOeSPBJZut6Hkf9Vz-spi_13C85_rsmdW2peYxfxDyHq4Dy0rYLefQwvpQGQhISScH1G_zmU1ZaD0LkfUfw6QlqU9t3CLS2avMCucjTHyM2L9xRdLTiRbVc8dam_7Vv6EU2MHKAkGeP392Ipp44x8K1nDTP744zwAm6UGw8L6m9dfAQep0pfqceGAbUY1ouOx_ZN3FGGjrZQ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
استارت‌انفجاری‌ستاره‌آبی‌ها؛ گل‌اول استقلال به تراکتور توسط سعید سحر خیزان در دقیقه 28
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/31197" target="_blank">📅 18:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31196">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsC_rsAsxqwFueO1tzh1gubQqPZu8ZfxLosfQFnG6FXhSHkpEL50TYyFs8ZvjvVfu6mEtU7ogJZPhaAyOgSbbBT534uW5sMkLAjQC-w522HujyCShkFJinq2rz0ipJ9qIoNNsOMtR_ouIS_3GJ9M9Re5Yy6UrrOl_9a562xkd4LZswcegFcc-F3F71C6rrhThjb7TgVBD8orPfJZYkE4ieCU3NpyRI_USoAo7DBdwKUjtmuhyGnpfUw9ip7ZBWlrq9_Bg-UK6BqFAFkX80w85ikxSYqult8J9YlzZQu9RLz9ikEIDcJytlkTmBqur71l9VEJEmU5oNaXiSkMbe-T7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
سپاهان محرم نوید کیا امروز ساعت 18:45 با این ترکیب به مصاف فجرسپاسی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/31196" target="_blank">📅 18:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31195">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVKQU3UFImzyd5xIGGfzcfAt3ErVevc6kw9fvHDoQjF73iTKTCtRRoPXpJ1cpTM6RinqmKjSrLuf7ZY1Qx5cwN4bCXgsBRufI3KS3SvaIARJzI4bREJEdMKELiTKWHZTYI8TMLbkbNIT-jJ-6Gixhwsa5tsfj2xaq_h9HyJnseVu8uEjzYHl_yBv8vJnsnww098T-xlPV_821R9p4Me8Kd67tHWHgJ493puWKGD81jFSMEC3Bk3Wqt9mEC5EyilLqN0a8EUZs7OwEYospQIw7LPdR0zO8vCmd6azsU6sv2Q8wm5_nlM7JSiU0-NbAbqVmdhPq0xgnr3Qb_L0x9G4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
استارت‌انفجاری‌ستاره‌آبی‌ها؛ گل‌اول استقلال به تراکتور توسط سعید سحر خیزان در دقیقه 28
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/31195" target="_blank">📅 18:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31193">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXGrRlaub0GZOrrsojrW7PzxcxtV6EtLcJxhfPd2Hgq1EpXnhTm1LcO-NrVGYQybHmF2aDzqwTma5Wo16YGJWphFzZuHwoZwgZTxPKnpUCP6C9Clm51o3pyOg9zfl2ZUiEKiV0pO3RxWTOB0WwP8ys_LuqsNovwLYnTt5gzC1XsQWY2zx8aePC5PtuyE-zBp0j1evp3mLgl5Tpvx4VPY3QHIyfSl-VvuIWTNJ2rNoiyEwsNxKmNrsriFyC7aCcc7_Qy4euaKTA-oPkqPUmZCce4ZBE9mNxre4X8d32IDSooVE_FSFvJVt4cyMkDLmw3CmGHq5vpoJsNOeiXxNVWYBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/abUn3iZsAgHB_-ULtqt_cR4_4tWPQPtG1AYT9ZyxJVyAnoFEJ_9L047-5bkVnjmT2xGPmL-LC7WQvT_taOmCFfZh2-fDtzrUiHzzP_tuXsbLZxOQhjJgK5ztyQjxzwZ_aoTtjFnQtCeaWuRZFRLgTOJVO-GFtqtcVINxYJfwCqm6v_OIqHTzLqIf4IyN0pbMpMXfbDPn_caBdRUsCZHBCfRezJ2Kz29F1cdMX8XruRmlgbd53N2lcP2LczQvSckPxFteNblUYkaOCRrCY-obXTdc2bqSKHgo6c71G6MrxwQj9Vt863AfeGeeMpQqeOFWiqLl6mC98UDIIqGzIdjydg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سوفی رین اینفلونسر مجازی مدعی شده که لامین یامال ستاره جوان و پدیده بارسا اشتراک 12 ماهه اونلی فنز اون رو خریداری کرده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/31193" target="_blank">📅 18:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31192">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b022014318.mp4?token=Wh0T6kUoeIcSLAwVdHuD2rwRDHzvcDA-bLhB3m05URkaNA0QMa_hkervb7Cy4CzU05KHliMvcmQ9I5HOfsawmqPwHPZyTvgx7Xdeq06x32c6fTk2uQbBASmtYvDAvJoxZGzsyCYZEljkz2RbmEG5iOpew_S7A1uvyfxYw7o43_5fEFBgmpeRoMZX4_JOURfixhyW6xFsA8hlxm8W-3BU3KWYP1k8_2Z1-AYIuSELYJtJAsEOAjRpmBz9hv-P8lyiSo0ONoaV72X5M7WlOsy6Pi7jWw5njxuqYQOqxnKZ3f_8Rown7PzUFj77AFin-Y6DH7OqzCGhBIXM_O7CssCcTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b022014318.mp4?token=Wh0T6kUoeIcSLAwVdHuD2rwRDHzvcDA-bLhB3m05URkaNA0QMa_hkervb7Cy4CzU05KHliMvcmQ9I5HOfsawmqPwHPZyTvgx7Xdeq06x32c6fTk2uQbBASmtYvDAvJoxZGzsyCYZEljkz2RbmEG5iOpew_S7A1uvyfxYw7o43_5fEFBgmpeRoMZX4_JOURfixhyW6xFsA8hlxm8W-3BU3KWYP1k8_2Z1-AYIuSELYJtJAsEOAjRpmBz9hv-P8lyiSo0ONoaV72X5M7WlOsy6Pi7jWw5njxuqYQOqxnKZ3f_8Rown7PzUFj77AFin-Y6DH7OqzCGhBIXM_O7CssCcTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی‌سامان‌قدوس‌ستاره33ساله الاتحاد کلبا دربازی‌امروز این تیم مقابل خورفکان در لیگ امارات؛ در پیش فصل باشگاه پرسپولیس خیلی تلاش کرد که قدوس رو به این‌تیم‌بیاره اما مخالفت همسر او باعث شد که این انتقال انجام نشود. همانند مخالف همسر مونیر الحدادی برای بازگشت…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/31192" target="_blank">📅 17:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31191">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5UwhbCmReQZZdplv35jhMFtPODMOxaXPELMeo5dtETgeFHNMTSHBnmAtB9h3HtJWLL2OMosVlaWhrPHZG6yFJMvBL9jj7vZxqxzRmKGnE_qOfAgjKOEV5Jz_fw_O53lpoGGWF526XGqfWMpgq20DtQRZ6-M_vcy2Yzkft8YBzazjk4WLF7S1j6unoYCl2CHBiVx-TUQsP-fOaiuXlEjhWP9SDNmEMWFYKYE-I0mzr909264hq812dJIUlvYiQpbz50WIzLNIWddYdMLhjdSH4IIjEWTxevzQfjOid3yFSOI3GozBkWRyxJ3Y4QcWD3uSxK-_MHrjfPYu7_ohsvMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
باخداحافظی پدرو از دنیای‌فوتبال؛ از ترکیب استثنایی بارسلونا در فصل 2011 تنها لیونل مسی باقی مونده و همه خداحافظی کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/31191" target="_blank">📅 17:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31190">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be0608b6a.mp4?token=DaQKpE5dM8LSN8zF6fYEZi6Mm06nuX4Xx2ce-xoFolAsDT3NllSTxax_lO0MoiOLoyV9lu-MLs9V0K74GAfsNxPQRpHSKw5rGq2ChnKhbKwKzMTArtkxt95_0ksjQAg3hNHdsLvGyUVzazoYtZm4PGsOzTAylDSHkUlWOO9yfvjn0z_OpjCRSTdfy0X5bE2w6rSDkaGPS9N8Vp7nw12wc-vYElywhPexI8MvIrvu3oib_F3QYGBNCQo4htuoaKB3N7r8kAjt1Gukh0B-qXcYOC0Sej3R3MSaM3hiFWUUwqVx_kf7L2oPWjRTFD4K4Z14Rx8N0OZIivnSNG8cLc3C7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be0608b6a.mp4?token=DaQKpE5dM8LSN8zF6fYEZi6Mm06nuX4Xx2ce-xoFolAsDT3NllSTxax_lO0MoiOLoyV9lu-MLs9V0K74GAfsNxPQRpHSKw5rGq2ChnKhbKwKzMTArtkxt95_0ksjQAg3hNHdsLvGyUVzazoYtZm4PGsOzTAylDSHkUlWOO9yfvjn0z_OpjCRSTdfy0X5bE2w6rSDkaGPS9N8Vp7nw12wc-vYElywhPexI8MvIrvu3oib_F3QYGBNCQo4htuoaKB3N7r8kAjt1Gukh0B-qXcYOC0Sej3R3MSaM3hiFWUUwqVx_kf7L2oPWjRTFD4K4Z14Rx8N0OZIivnSNG8cLc3C7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شماتیک‌ترکیب‌تیم استقلال برای دیدار امروز مقابل تراکتور در هفته هشتم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/31190" target="_blank">📅 17:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31189">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04026264da.mp4?token=XGaAxDb9AII_GA0uR6j5UJtIOexgB4xJsr6N99l4fukZBA3NBZFNyvJ4RX1-9k7SqvUR2eIk-Z2AeKu70u-g1P0MecH-PmrMlLjk-UOlgB_vbE2e_DfeFtVoGltBkFypvAMa0Rp14tN1M-GFYJsq9H5R5T6iCWf13ycynBf_7pvBzVqVX05yupiNE3s8w-DJuHA6XyRL8mM72OJtwDucw2Dsu8W8bAcEPo5x0ZZSH5c6I1DbhiiCNgAQtn5t2riGnb5tuaDSlOe2OxFwlKknJq9VuXx2I4OC-XjuXS6Fs17W0v_lZWGQ1WegGzyHiRNUJWyFKNmjSHix--fFfWpc-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04026264da.mp4?token=XGaAxDb9AII_GA0uR6j5UJtIOexgB4xJsr6N99l4fukZBA3NBZFNyvJ4RX1-9k7SqvUR2eIk-Z2AeKu70u-g1P0MecH-PmrMlLjk-UOlgB_vbE2e_DfeFtVoGltBkFypvAMa0Rp14tN1M-GFYJsq9H5R5T6iCWf13ycynBf_7pvBzVqVX05yupiNE3s8w-DJuHA6XyRL8mM72OJtwDucw2Dsu8W8bAcEPo5x0ZZSH5c6I1DbhiiCNgAQtn5t2riGnb5tuaDSlOe2OxFwlKknJq9VuXx2I4OC-XjuXS6Fs17W0v_lZWGQ1WegGzyHiRNUJWyFKNmjSHix--fFfWpc-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالیکه هفته‌اخیر سارقان تو اتوبان همت تهران تلفن همراه‌آیفون17پرومکس پیمان حدادی مدیرعامل پرسپولیس رو زده بودند. امروز همین اتفاق تو اتوبان تهران - کرج برای مهدی تارتار سرمربی سرخ‌ها اتفاق افتاد و گوشی جدید آیفون 18 پرومکس او مورد سرقت قرار گرفت. خداروشکر…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/31189" target="_blank">📅 16:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31188">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5Bj0XN50YnqgXIhQ9pv1yd4Ssz52DsZz0yFe2zvGRarxHE2nJnl9nO165Laz9l8vfMNlXJHA12tJ9_8HXZIUXqGw_y720RSFFIunO7G8eefsS65pBcbXoScAakqAM_1tMgLzpmFHQdLzumsh0rK4VAuWfgz8STQKAE50dijuNqKSkBj4mPyN2SNv_Tl7bcUBU5y-XhSyD3kWxPRxRxLoff_-OzHP_mfNAA22raBISLYzwB7i3p_YH1G1Hgk6kNVnTPE0vHA0kPZU7q9v7qSGyKo77g_EziYWBz5sD7jBs_fMrmQ7w1PMm3_zBfGZRI-3rD2do4r2g5SolcN975kjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌پشم‌ریزون‌وجنجالی‌فوتبال در دیواندره؛
دو مربی به اسم‌میثم و ادیب 5 سال توی تیم فوتبال ستارگان دیواندره‌بودن‌که توی این پنج سال به بیشتر از 50 کودک تجاوز کردند! به کودک ها وعده میدادن که اگه باهامون رابطه جنسی برقرار کنی توی ترکیب اصلی میزاریمت و میفرستیمت تیم های خفن تهران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/31188" target="_blank">📅 16:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31187">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbLLG_lAOd33JpKa2V3UzQ2xbVS7ieacM24-YdJsM5QSZP7OaFNzpvPhhD3EmCHOnOehyxDxG_2TBODCmNx4f6Id9lkYrEswP_VbSlHoKHoTbE91gSrkF7EDB2dxqtYiIKO3YUMtZgACPhRMrnjDQIOTJTS_CWQgYJPvN9eIIVqKq0Nu8Ywlq-8ZE2px05hR3MAolb65SSvsK39sQBZuX8_fPxWe2MfKJ4XzlxP5fwxLgm_95Gr1kuwVE_lJxzfk9jqLVt8N5pm-H0yXF008nN864yEP6-L9a7cDJzNiJdP-tyTS6xuPGHVEqo9jSUOz0vy-1y6ngzAopmiGxs1mWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛ شماتیک‌ترکیب‌استقلال برای دیدار حساس امروز مقابل تراکتور؛ ساعت 17:00
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/31187" target="_blank">📅 16:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31186">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmKjVtE1vdI1xuRsy8kkuoD4_T7tIxKhuGI_9FArKaiG8wYrOdmE-j6PWuyrLNpBMGlWfRw8a4qGwF1Dua1RrjpoW7CQhlv1DlZQ-stEwmJFR3fGbjgyng7UYLusuqn2vmcFx7nX3X6onFImR3fEBrb9fJUDZaYlkhHlltp4gTP75H4QQ2phH_ge_ILDJJB6rSNHAdCuJqlkJatSznj_MzFB9ow4OQ6faMWpWLkInexv58htuz2tzGCQ_or9tutWmlrvpMIDfk-DiFQItA0JF_cN0aWIu2iMAoBJ_JBcNUf2ZG_27FJLtc6oFXH3lxVRNkqxuiip-neo6iYwa5OFWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛ شماتیک‌ترکیب تراکتور برای دیدار حساس امروز مقابل استقلال؛ ساعت 17:00
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/31186" target="_blank">📅 16:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31185">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZ63jdLzobLayL9V01MAIcoXB1KFEosKYdMxmVGXgkUVIm2w6bmPKopSSqiIr09tL7gG5CG-4VYerfQDRBByv_wxu29ZJZyC0tV1ZBLik6uUpXP3oLcJZr9oUngVfonz8c0ZAoFolfYqTZ2IeJk2fql1MXoizpGod2QaNqsPaLt8-AQYidW5o0GRwv-6D4KzzlfjYpm2WcYCPVHIu5UXI5i679WiJ-yZFFLeBmqtemq9-ucnxntGI3SOVW5pK_Pzlj5KEa7pyuahJQ08DAoGcHaJMimQ2TVKc95B1tU_mnpRp2RfT1vS6FlWaGr8dGinvxhxBjFMKfJljZvOkJiaFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
به احتمال بسیار زیاد تراکتور با این ترکیب امشب به‌مصاف تیم استقلال خواهد رفت: علیرضا بیرانوند، خلیل زاده، محمد دانشگر، دانیال اسماعیلی فر، محمد نادری، سیدمهدی حسینی، تیبور هلیلوویچ، هادی حبیبی نژاد، مسعود زائر کاظمینی، امیر حسین حسین زاده و شهریارمغانلو.…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/31185" target="_blank">📅 15:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31184">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9307641030.mp4?token=Vest8un-mPwYs4dNykVPoRlY98rE1gUxepxftXQ8SFBvIjyON8m0b_9_ecyF6h_GJXkNFmfXyXD6IrP-b9Zj8e6KAYBNKQhOMehUTxeKuBkaijiWUT8Pn75zE10k4f2VlOZIeFdy3k9oro5YdFRcFjtYy-xSa1UR_NsjnrVCuYVzVpV4V8oxnPotHseGfS8njdRC4hViAij1GzzlZs1w9CJUx136DwU8Zz7NdrmNBzJAM1meOR4DZjOrp9nKNMZH3GV3HRxS8zbp_kG27NIAXrHINWnm62PL_KGwMh_jGaLpsWJlrj5JqbanB5RZMZmzVei4kjEOEGyW7DTFN5_rp4xoo_EP0idF42-hn-PZTbS_4NYyrR4wUA9xKSUuN3aQDLWyPk-r7AKRvps3O7mwzsbftoEnJQGPBGJZzzE4PaaOZUbQUXHitP-GMjg33apPpkwXItnYuyKJPA3OE1vJIiuj3xg6At0hfk65TOlsfykaCu-P8EHvz13iI11Ymn4uJGTqrf8AGu1s6CqJaHLFpYkNzmyQxR79eCe7UKkYYMVP6MM_HJXIfo1OR2y83vbarQkhGGCDM8RPqzol0IK_JOqMS94ZR7a0P_xGbrnrQOsNS6o3rkTWhk0ZJdlxPFNNHaHFy9Ul0sdyGMtud0bhAJ0L7tlZVhwitR1s6EL2brQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9307641030.mp4?token=Vest8un-mPwYs4dNykVPoRlY98rE1gUxepxftXQ8SFBvIjyON8m0b_9_ecyF6h_GJXkNFmfXyXD6IrP-b9Zj8e6KAYBNKQhOMehUTxeKuBkaijiWUT8Pn75zE10k4f2VlOZIeFdy3k9oro5YdFRcFjtYy-xSa1UR_NsjnrVCuYVzVpV4V8oxnPotHseGfS8njdRC4hViAij1GzzlZs1w9CJUx136DwU8Zz7NdrmNBzJAM1meOR4DZjOrp9nKNMZH3GV3HRxS8zbp_kG27NIAXrHINWnm62PL_KGwMh_jGaLpsWJlrj5JqbanB5RZMZmzVei4kjEOEGyW7DTFN5_rp4xoo_EP0idF42-hn-PZTbS_4NYyrR4wUA9xKSUuN3aQDLWyPk-r7AKRvps3O7mwzsbftoEnJQGPBGJZzzE4PaaOZUbQUXHitP-GMjg33apPpkwXItnYuyKJPA3OE1vJIiuj3xg6At0hfk65TOlsfykaCu-P8EHvz13iI11Ymn4uJGTqrf8AGu1s6CqJaHLFpYkNzmyQxR79eCe7UKkYYMVP6MM_HJXIfo1OR2y83vbarQkhGGCDM8RPqzol0IK_JOqMS94ZR7a0P_xGbrnrQOsNS6o3rkTWhk0ZJdlxPFNNHaHFy9Ul0sdyGMtud0bhAJ0L7tlZVhwitR1s6EL2brQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افسانه‌یاواقعیت؟ بعداز ۳۰ روز در قبر چه اتفاقی می‌افتد؟ روندجسد انسان‌ها بعداز مرگ به این شکله.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/31184" target="_blank">📅 15:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31183">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4rrCwIYpavfo4vIMek1sxLLLdi4DMqq-5zGx0NZ8Vjx8r8L42LbBrDtORZ7EoxpgQKR322f4V9j7bf9z9fP_SgPtdshiANM7NNlCqNX8Tv9rSWLvE2aT4pShqpL-0RLLt3BPNRzbeUzGsPB1erfIFRq-5qZTqLiYrYmDYPXlrzu7mAUkR_7Eblid_cTm_1p7LhVRz2-cXHFYFbRq6SE_hLg4O1iVn8tobXHc7jptzoMW0mD2qILWbkVoJwtnRgqYpBuhKhPzpRPGGJrORPJzoJYNRbO3c4IbAjc346id0F-O5Xw5Qag56wwKeWFxXdOALuPG60mfWitCLk6PIAHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌امتیازکسب‌شده در تاریخ 5 لیگ معتبر اروپایی در یک فصل؛ یوونتوس در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/31183" target="_blank">📅 15:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31182">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c815bbaf15.mp4?token=uYlrGVlgRL0h8UszYl7elCoHLQQFY7z2DSAqwFDUuk_lmO_kstoibf9dCaNmHebqYY2OF7-UhKPNiIMfjf51Zc20vEmGO2Gtq1scScZaQbB9WNj9pEGcxTuf5DDvjPVtgi2MEARJQ4HXeVqGIbGM_Mq46y8gmBRnRn6qZJ6pRBy6cthbEoq5cfEBZbvhCKweikrY-82SSiEZVlUeBwNmOXujNO9joDvf-a95JXccRWw50bhknCW-GlmHxxza-51yf1hvfkXShntFhbv1UklSgZ1Wj5gOYav724X7U0GPAwp9MkC_g93346JzKJdDmdZyMCXWVGVkTZlSV7Klcf21JCcpFdgDA0FA-dynA_LM6nt6M6BS3ZQEgppUw-V0iosHaoiY6Ct7IAMAdsFZ7337_VYLZgfM9Yo5VXDQ6uTD8N_HNRCwguo6EQsuLurC-lZmPmgJg5nm8K-5EJr93rF73-dl7i_aSYUGrkrQkaynQ8v_OwrWxRe6R8F7H3Mbuz-f2b4tuTWT1Dc-5d_rBBipPZVZaGzi-Kij0f-G5c9nk-d31-q9BA5F3rJGZ6b1bQ6I3-N4HsrYWgtqFMxruSF-cYsgF052Aaj61eo0HuxVZSCmDzLgoejjdFYiDMAWu4nZ2Uepzm0gGjJ26R-KJSeSIKhry8kv5hOY8hUOHTPdtEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c815bbaf15.mp4?token=uYlrGVlgRL0h8UszYl7elCoHLQQFY7z2DSAqwFDUuk_lmO_kstoibf9dCaNmHebqYY2OF7-UhKPNiIMfjf51Zc20vEmGO2Gtq1scScZaQbB9WNj9pEGcxTuf5DDvjPVtgi2MEARJQ4HXeVqGIbGM_Mq46y8gmBRnRn6qZJ6pRBy6cthbEoq5cfEBZbvhCKweikrY-82SSiEZVlUeBwNmOXujNO9joDvf-a95JXccRWw50bhknCW-GlmHxxza-51yf1hvfkXShntFhbv1UklSgZ1Wj5gOYav724X7U0GPAwp9MkC_g93346JzKJdDmdZyMCXWVGVkTZlSV7Klcf21JCcpFdgDA0FA-dynA_LM6nt6M6BS3ZQEgppUw-V0iosHaoiY6Ct7IAMAdsFZ7337_VYLZgfM9Yo5VXDQ6uTD8N_HNRCwguo6EQsuLurC-lZmPmgJg5nm8K-5EJr93rF73-dl7i_aSYUGrkrQkaynQ8v_OwrWxRe6R8F7H3Mbuz-f2b4tuTWT1Dc-5d_rBBipPZVZaGzi-Kij0f-G5c9nk-d31-q9BA5F3rJGZ6b1bQ6I3-N4HsrYWgtqFMxruSF-cYsgF052Aaj61eo0HuxVZSCmDzLgoejjdFYiDMAWu4nZ2Uepzm0gGjJ26R-KJSeSIKhry8kv5hOY8hUOHTPdtEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زرگری حرف زدن جالب و عجیب و غریب ساینا کریمی ملی پوش تکواندوی ایران که در مسابقات آسیایی ناگویا مدال ارزشمند برنز کسب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/31182" target="_blank">📅 15:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31181">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjAquGmFGvjHkProacQxYopNyIxEl_UiAh9jCebB5rtyRehGcXPNoNKpegebtk8h8ZQKwGLQp67ziGtIqdjV8S68UwqkYYZD9qZsXaercvu7xYcMBz4L2S2F-h_y_0om-a-93zYWXUxqMVz1Izx4FS8DJGz4AnO_lMMD2CSqghKtajX5nThJue0uuGbVpZTBI5Wqc17ruta4GB5vjKMs_PEGKEKt9VoN1qB8fEJNsHt51unYp6oYv9eFQFJ4xgnJ6H3p4wl0xqfZ_odtvMdGjnSkREgoVDDUKtgficIKD4ZVt-F91d9UuKFw_vWbo6KlZV6xIY92wE51gLV7lVoRMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درد و دل‌های امیرمهدی‌ژوله‌درخصوص وضعیت اقتصادی سخت‌واسفناک‌مردم‌ایران در شرایط فعلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/31181" target="_blank">📅 14:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31180">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMGi0ydpixFO_GKqhz699dgWGefWt2Hj40SGoHiZchHkUKzZOrFML_SK_acLOLi1bQSq51oR_8CyigQa_Y1XzrMnnOhps9p3mw4PvCw0nd8_Nt6eaOsYhuLFdOA-NmZBrneQAPOSBigwf8B_aYFEdctrg2jzaEB5gcKIScbsxjVuk5bP0pDOK9nQcd7g2XPb1FqvZ3Pf14ffrDDB1ODsjQsAeUPo2wYaQyNpHoQGvczOLYup9Wpl_npRh6iyhUUOye5Vf2cltfSUE7RKijQSHJ20VcakSe70lHAMquvXoSVZHvSTLWfoGrXNWYdh3okrddI1jOplaDsYA_NeIeWM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت رنکینگ جدید فیفا در رده‌بندی تیم‌های ملی مردان؛ اسپانیا، آرژانتین و فرانسه سه تیم برتر رنکینگ باقی ماندند. پرتغال با ۲ پله صعود از برزیل عبور کرده و به رنک پنج رسید. ژاپن کماکان بهترین تیم‌آسیایی با رنک ۱۷ جهان است. تیم ملی ایران با یک‌پله نزول به رنک…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/31180" target="_blank">📅 14:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31179">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ja4AzGK6C1sX-uUOwSfsXQH6gDExuh-J46S2vvG6L-id-kinIHfbt3I0e4H-jb6R2dCu_eTSP-doYAqCsReRLTTB49ZzblJ2SmWLYWJMGhxB3Jfju-DVt2wMRhAfJR1Sm45Wq3RRxJnKp6Dnv0JUkk3AksRmuVu0dXnjM7xFbkeG1lndra2wrqdCUrtniRASKjpSxfV7eKqNyNkdRY51nYd7Lk33C3e9xQ59GgO95idpo0AFxcZ2B1yUlxUMPfZpb3FnGGN6dW-WrOlCKma_X0TnnPDtE4sPzo32UoJ2hwY9_x-puu32ed0FYM7MBNGWOmIJl0cDRvrUoarvoluDfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
ترکیب تیم منتخب دو قاره اروپا و آمریکای جنوبی درقرن‌بیست‌یکم از نگاه هوش مصنوعی بنظرتون اگه باهم بازی کنه کدومشون میبره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/31179" target="_blank">📅 13:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31177">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G4CwrmkgJ2Y6rWdjD_uRPcwNNvXYe5wWwZeY3BeLZ9WESkcCcVbYyCcgiAEzDkq9vR3AxZjolaijaATrPxZGjiYVqonhQUo8gISIcVwIH-lSKa5Oq-fc-SnDwyvVWuhhsI4F0yXG3_zUMC6qpUp9d3Hz7kU8c0ptV4q3bFFPMaMveyPQ6uDFpP4Z4YSzAE2pb1WP4jcukTmfpIRQXWxKOIturt4oNswKoerEn5UcdjCBKPuTdEZCxfa5JQPWGz_kdsxR-5-1YCutyr0RVyJoKTDgx91tdMYHfXCZ39ff8ZaUhDgyF-ZALI93S7vcWjh6Yy9YEl6W-qeUOITeJe9Gnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQsIgKnKk6TtV7JzDS2MRVsbVbo8lQgGzhIa1rTjdLpaatU0wsxqLuKxwJA9zNjyFqcOG9INszBxwff6n3v5ov6mqao-bzj-peEBc6VQsvGOUzjgcaDdi535dhZ5cqLuqiCZjmgGeoYyHmMkyOc0X_XKI1NFl_J7XS7k_CtO4gn9SfVCDHu3n591af83z-WA-6bA-Tud4sfoYi1MhdVdL-Uvb4LgF23MnoBJ1bTT9m5gq_6hTMEL5j1urw1PDsQ3teAIdb_d4GwuJBaXou1xaS0JPBVhK5kR4C82UjuK-DdAbQ9qOpTY-VkISuuFCuvRi5pNmnGzE-gE73QhgJDy7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج‌بازیکن‌برتر قرن‌بیست‌ویکم از نگاه هوش مصنوعی در دو قاره آمریکای جنوبی و آفریقا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/31177" target="_blank">📅 13:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31176">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFLEEP1Awoz1D7UNmJoS0iqkE7e-3rZkbClfT5mmkEPRkdojOArnwG-RTNhiOgWj8STQ56oVrLlRRVS6kWPUE82aMGWumGwhW03znAa7JLmO-JQXa-hvirApLqXPvq6lIMTK-ebC2_iXr5DmggGVPW0Y4jf9KNgVT0WMfixyvZbQZRl8I2sW5lOvpIlL1j_Ro7Ya4kIf83ljI_kzGt4WWl8efLYJKGYjIlqL9yCZeqGEzUu3ZdoawHdvPaGgAeIhLfuwSK_Jh-F73DxHr1XUPal6E_S0mnnFZh-afkR3cmgqieYfv05FRQB-Hh_W2tCtxYZlQl39n_zMOyaF-yR_eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
به احتمال بسیار زیاد تراکتور با این ترکیب امشب به‌مصاف تیم استقلال خواهد رفت: علیرضا بیرانوند، خلیل زاده، محمد دانشگر، دانیال اسماعیلی فر، محمد نادری، سیدمهدی حسینی، تیبور هلیلوویچ، هادی حبیبی نژاد، مسعود زائر کاظمینی، امیر حسین حسین زاده و شهریارمغانلو.…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/31176" target="_blank">📅 13:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31174">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXCSlu08_r1euDMwWKg60uxwjzp5Gq9aiZ-CZeQEyYUsBAxaka6wQRlTS1BSK4MCSn9fTi3TpqY8djaCEvImCarctCv7HsKT1ldx7JZ4v3_67ugN078gGWbJgiJlqFqOpKUNCceshZEfvWYsh3kqsJZuRJW2kjDBep-lg7S7FAeqqcyCszs8wV4J2eufRytbsaRNpYN5ICXrL1UFtInNswlx1obbf7f4l2xAEbJMQChOcTOO2COc1qDv_BAcR1FNh6uH4ZXe4zDwYarVG-sndXxZqgArkoGnHhL-V2-oy-hFHsmAjC-2YCsAbnLPLiMsALn9KEU6SXLw7UieaHJacA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد پرتغال، هلند، کرواسی، ایتالیا، فرانسه و المان در فیفادی مهر ماه با کادر فنی جدیدشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/31174" target="_blank">📅 12:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31173">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb012b6f1.mp4?token=Ybxm0UjoCEd_RTyMq1ROlubpLFLk8XjYUuLz17QFQ9wdHn9cPpmo7v-btDpQz6VnKb2YBX5V4MEr8vFR4FndQWDPiaY24e4Qx2A2hSMam9FJ67wQ_c5Ygie7T0awiZjPmPlClQH6eBZ3D84AMbqSIUWETwDNE7wY_EyJ_dI2OyfjAakIsA-_DgjhGfjYnNqn-FUMxfZylK1iYUN-3NMkPFpwGoskxCbAynL8X4kh-egboMuxpnV6BvFIPCcUZF5_7Srw-U4r1jTe91MS_ObHn4j-wmWeCuUPFIWZUGFV9SnbIeVfCrX_21VPfsa26JojnI-a02B9KechaWYwsoEI3lh6ydd4Kuc-apWLkCv8jE0cq3E9ksJTlXhNTme1kvB2_skXgp8JF7355CdQN-PB9WNVlFrS5dekfLv0WrC6uGpWXPgvLCwbI4rlSURWtGEdHS1fZh2Uyv3wjmldCwDnbB3op88HGgaDOviX21eRUR1B7dGFFPwjqYgt3ol_f9ZfgCm-BfWRhjqivY9w0LiU7u9Z8vfNjqSpOUEiiSJvSLHJ-qLwNx1JHo1m45cvQU0zFmVAbSfofTtZ0pUNST4QLswU9AHMH2nZF1Fu3gyaSw9LeCF_vS9aBSmw_YzwKf9G1FiHjao5KwWlaj7qjS_jVlSiBoty33Fsaj_6jqM4rbc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb012b6f1.mp4?token=Ybxm0UjoCEd_RTyMq1ROlubpLFLk8XjYUuLz17QFQ9wdHn9cPpmo7v-btDpQz6VnKb2YBX5V4MEr8vFR4FndQWDPiaY24e4Qx2A2hSMam9FJ67wQ_c5Ygie7T0awiZjPmPlClQH6eBZ3D84AMbqSIUWETwDNE7wY_EyJ_dI2OyfjAakIsA-_DgjhGfjYnNqn-FUMxfZylK1iYUN-3NMkPFpwGoskxCbAynL8X4kh-egboMuxpnV6BvFIPCcUZF5_7Srw-U4r1jTe91MS_ObHn4j-wmWeCuUPFIWZUGFV9SnbIeVfCrX_21VPfsa26JojnI-a02B9KechaWYwsoEI3lh6ydd4Kuc-apWLkCv8jE0cq3E9ksJTlXhNTme1kvB2_skXgp8JF7355CdQN-PB9WNVlFrS5dekfLv0WrC6uGpWXPgvLCwbI4rlSURWtGEdHS1fZh2Uyv3wjmldCwDnbB3op88HGgaDOviX21eRUR1B7dGFFPwjqYgt3ol_f9ZfgCm-BfWRhjqivY9w0LiU7u9Z8vfNjqSpOUEiiSJvSLHJ-qLwNx1JHo1m45cvQU0zFmVAbSfofTtZ0pUNST4QLswU9AHMH2nZF1Fu3gyaSw9LeCF_vS9aBSmw_YzwKf9G1FiHjao5KwWlaj7qjS_jVlSiBoty33Fsaj_6jqM4rbc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
سر الکس فرگوسن اسطوره منچستر یونایتد:  «من از مرگ‌نمیترسم؛اماوقتی یونایتد برنامه ساخت ورزشگاه جدیدش رااعلام‌کرد با خودم فکر کردم آیا آن‌قدر زنده می‌مانم که افتتاحش را جشن بگیرم؟
‼️
امیدوارم‌ساختش‌زودترآغازشود؛چون اگر ۵ سال طول بکشد نزدیک ۹۰ ساله‌خواهم‌بود.…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/31173" target="_blank">📅 12:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31172">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3-rj7n5EcyxinDKpbAWUkLoe-s3B_yUxtrgs356D-ZSmRgMHspqQHvorpAerKX2tMt4keNeRCVs0W1dZPm9sldbVWRfS-ow-42U_oDvuNGWilq4bikYA9O0ZAwoZHDvUuF27zCyY7A4uy3qgAlrUgg7Myrym40fWvMS4D909W4jR6jJtJoYmn0Bw5DudL2idNIU3EyOu14egJ8IXzGXBinZNlT_4fWRNlj_impzRNsdMqaufXu2lEDsZvXSBrjZrjl1vtF06bUTWeznDsUHHI_QeudReTxG1u4YjfKlGDxEpB5kRa48ysakzWaoqiMfu-SsX7iPRv884CusmJGPFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
سر الکس فرگوسن اسطوره منچستر یونایتد:  «من از مرگ‌نمیترسم؛اماوقتی یونایتد برنامه ساخت ورزشگاه جدیدش رااعلام‌کرد با خودم فکر کردم آیا آن‌قدر زنده می‌مانم که افتتاحش را جشن بگیرم؟
‼️
امیدوارم‌ساختش‌زودترآغازشود؛چون اگر ۵ سال طول بکشد نزدیک ۹۰ ساله‌خواهم‌بود.…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/31172" target="_blank">📅 12:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31171">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKcmIrZAdUydv2DtKtcK53DJSV-w-uhT_bbSoIa8mq7yvIEyDPMgRgoiWHbssh9ZrRV8EwmcL322QxhJGPJlB-JGuDFR2SHzvoypKnKeSFyC5UNJjGFXhEESg3kgGR0J54NXBwLvnyPNkQkefaYhP0AzsbQvKLc4FYCmHJzbPMhrmozE3Rsvo8FHMScD4BzCiPwNm8WaNT0iQmePME78DS8MX3W8S_iH-mwPD84mKLjm288Q-Ek6Vtqp_Zv-jzyx_qONF7Anct9Q0P6osAjox1OO6PAaKjDp-ay8ThGulh3VZvVRnia4e1HmzX6sHFvZq7Pnn-5JMRG8-qyLRe7aFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
سر الکس فرگوسن اسطوره منچستر یونایتد:
«من از مرگ‌نمیترسم؛اماوقتی یونایتد برنامه ساخت ورزشگاه جدیدش رااعلام‌کرد با خودم فکر کردم آیا آن‌قدر زنده می‌مانم که افتتاحش را جشن بگیرم؟
‼️
امیدوارم‌ساختش‌زودترآغازشود؛چون اگر ۵ سال طول بکشد نزدیک ۹۰ ساله‌خواهم‌بود. اما می‌دانم که به‌هر شکلی در مراسم افتتاح حضور خواهم داشت؛ چه جسمم آنجا باشد، چه روحم بعد از مرگ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/31171" target="_blank">📅 11:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31170">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nE2ciBELWaFqHyq-nP4H2F8LaCkw-7UqoJJMJvvdSeCpLWVr--Z3erF5k0YAI-YObRx1j6UV-80fRCPmzB8BKYL3rqU2dPBnCStWaLm-o_s_F4tbR0chdJy6ADhIEqBNsCw6fC9j1AVxj9i9tgM1GXNgQll3jSmrBCKI3oC_sf6i7nm8zBVegYAuVbe7eP33SRjC4sX4xunk96E4dTuZxwHUVs2TF1cotNXmFVfkDepOCCLIBdkJbNQtJCylyWVSQneZxIe4PYxW9Us4mPDAfU6qE1AXMJGkUUZJfp-sz1S1oTQR_aKoncD3g4b5Nh5xhgREMb-QDvAzbtmYt4YRug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
به احتمال بسیار زیاد تراکتور با این ترکیب امشب به‌مصاف تیم استقلال خواهد رفت: علیرضا بیرانوند، خلیل زاده، محمد دانشگر، دانیال اسماعیلی فر، محمد نادری، سیدمهدی حسینی، تیبور هلیلوویچ، هادی حبیبی نژاد، مسعود زائر کاظمینی، امیر حسین حسین زاده و شهریارمغانلو.…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/31170" target="_blank">📅 10:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31169">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbbCu5rIKxFHhqNmdAGh36Hq6fjSEcHB-97AwaFWn-9ZFGIkkHhh2zg4Lp96UZJBc6XqgC7MubV0TAIMp2QhcK5c5iQ7u1f4ZojPO61sYBgQ_py7WuX4mwy-fC30KPWg-auutXj_HV3f8wrhpkGhLE98cHtA70LyNpx5taIGP7_5tAbOwEBSCJw5EfWAkt9-HsvzIjbN_IUMVSdqwTj4sBO3diKZt1hkgn3kHWGnDXxcUscf6GK0P9uq1gh6oV32VOhlNJ94x-qxeXX4iuw9KoKx0QZgx1RmgUfM_bxnlvYXaj1lw7zujVAKAfXb5LUvU7MgMooxrqqQQ25uHp2iig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار فردا مقابل تراکتور در هفته هشتم لیگ: حبیب فرعباسی، صالح حردانی، سامان‌فلاح،عارف آقاسی، رستم آشورماتف، حسین گودرزی، امیرمحمد رزاقی نیا، روزبه چشمی، اسماعیل قلی‌زاده، یاسر آسانی، سعید سحرخیزان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/31169" target="_blank">📅 10:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31168">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe9b0bc7f.mp4?token=Kh-_vB-396W16kFCimkZKfkcpUceDsH1UBD57cO0fClpDM0zjXvob8Mg7QT7g0KiwdKz-VgLxGSZwsOzdYpagxTeqcRimYr5R-UztlKGICQwHFPtKsxKZcD-r0DR-mE_v80BnT6430ap_XEcZiEyoN7P4q0IIHyyrOBSEPJ1ddkNRNbmIJP1ZqsYJrukE-na6mf9gQF73TN9hwxCTugYRx1XQNTo8HZJ0Qmr0sYHvN1yDOkSI7noUr25rWVPPhvTu3VAkSO4i64gggK6JEz19bLgFXVSTLiVntJLv1xbqJOKaSk6MhxvYdvf1M8Gkcw3sMppKe1OCgj7wpdm6-5GXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe9b0bc7f.mp4?token=Kh-_vB-396W16kFCimkZKfkcpUceDsH1UBD57cO0fClpDM0zjXvob8Mg7QT7g0KiwdKz-VgLxGSZwsOzdYpagxTeqcRimYr5R-UztlKGICQwHFPtKsxKZcD-r0DR-mE_v80BnT6430ap_XEcZiEyoN7P4q0IIHyyrOBSEPJ1ddkNRNbmIJP1ZqsYJrukE-na6mf9gQF73TN9hwxCTugYRx1XQNTo8HZJ0Qmr0sYHvN1yDOkSI7noUr25rWVPPhvTu3VAkSO4i64gggK6JEz19bLgFXVSTLiVntJLv1xbqJOKaSk6MhxvYdvf1M8Gkcw3sMppKe1OCgj7wpdm6-5GXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استایل‌جان‌سینا و همسرایرانی‌اش دراکران «مچ‌ باکس»؛ جان‌سینا و همسرش شهرزاد شریعت‌ زاده در اکران فیلم«مچ‌باکس»محصول اپل تی‌وی درکنار هم ظاهر شدند و توجه رسانه‌ها را به خود جلب کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/31168" target="_blank">📅 09:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31167">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9398a1a1.mp4?token=ngtAtCXc3ylGHAu-fSkcEmvsVeQeaLCdh72umV9SbUoAF9Wf9Ge6uyA7TME0e09b2TzgFFfM1avIzEN-zDPf6msBX1e3NpKlara1TP72j-kzhg7Oz__kh8SJWePQRyM1b0tbI2MdGuihTTGnanYQXxdsMIRf9cKtIfyU92rrgMB5lIkdiftfD10P3hC4hL79ifL8FcBaRroJOuaLJwBYd856K5me4Gcm9bAlmKxjSKzyVuBLU-lN6XK38R4E7QfB8_eahxe81RE13DEr5Mja9RyVKMr6dPSeLJMg0LWC0bFxs6TWiNZ6C5fK9-kxYD-ChaOnJL5y3zVJ7pZymE3BPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9398a1a1.mp4?token=ngtAtCXc3ylGHAu-fSkcEmvsVeQeaLCdh72umV9SbUoAF9Wf9Ge6uyA7TME0e09b2TzgFFfM1avIzEN-zDPf6msBX1e3NpKlara1TP72j-kzhg7Oz__kh8SJWePQRyM1b0tbI2MdGuihTTGnanYQXxdsMIRf9cKtIfyU92rrgMB5lIkdiftfD10P3hC4hL79ifL8FcBaRroJOuaLJwBYd856K5me4Gcm9bAlmKxjSKzyVuBLU-lN6XK38R4E7QfB8_eahxe81RE13DEr5Mja9RyVKMr6dPSeLJMg0LWC0bFxs6TWiNZ6C5fK9-kxYD-ChaOnJL5y3zVJ7pZymE3BPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
شعرخوندن‌بازیکنان تیم ارژانتین تو اتوبوس برای مسی : "لئو تو مثل اونشب تو قطر جاودانه ای. مارو ترک نکن همه میخوان تو بمونی و..."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/31167" target="_blank">📅 09:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31166">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc91c2c757.mp4?token=CnnBw-at6VeVCj7Hw3C5OCBEPJ8g4FivzPNL_MQT7bCXKikTKjSIE8OkSe4wzx7Rf7JNvR56PxlWG3-iwkaPFyyVTeoHX8Tj2SuB58BeRQT1WLKHJXp7xn5NhH0TFXIoKHFTQv-gKbEZK-NXr7c-SUSIGbx-rfazBWIjPQi22G-Npk4QP2r09-f1EthCmxkMH4zZv6yEZyRqPzxOQs5a4Spz2KlRLz2jqqrg7pCMaBPoFpxJOGP93x6WIwxu0tgtSe069RL0r_JznS2TFxRec3jv2MvLNn0A7BNHE_iKfTdffj2p4GLlnUwncYme3RO0zDErZ4msmA8W21bP4u8lWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc91c2c757.mp4?token=CnnBw-at6VeVCj7Hw3C5OCBEPJ8g4FivzPNL_MQT7bCXKikTKjSIE8OkSe4wzx7Rf7JNvR56PxlWG3-iwkaPFyyVTeoHX8Tj2SuB58BeRQT1WLKHJXp7xn5NhH0TFXIoKHFTQv-gKbEZK-NXr7c-SUSIGbx-rfazBWIjPQi22G-Npk4QP2r09-f1EthCmxkMH4zZv6yEZyRqPzxOQs5a4Spz2KlRLz2jqqrg7pCMaBPoFpxJOGP93x6WIwxu0tgtSe069RL0r_JznS2TFxRec3jv2MvLNn0A7BNHE_iKfTdffj2p4GLlnUwncYme3RO0zDErZ4msmA8W21bP4u8lWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درد و دل‌های امیرمهدی‌ژوله‌درخصوص وضعیت اقتصادی سخت‌واسفناک‌مردم‌ایران در شرایط فعلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31166" target="_blank">📅 00:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31163">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8K6lBDkSOK1jWc24lWFirJeRHOyPBcYktFWcTETESa9_bphMxMhUZRHBKC-cBFKehpENMpeuBPJdctXjeufsQnTHEgTe9VKUc3VUxNwyeYYPPiS0PalEGs1zCfMC3x21MULEc0d6epOyLdz-DXDpyPXiBjfEOPf6R07JAYRFCM0oB5NTF3Jisf0NkcsPICI1Y-SXcwDBfcIjKfi-ZySOBKTBoyOknCtC0LQLUpzeY4pW_hk8UUtDRSiCDtDBT7iVDzJUT73cYM7xSGDEiTKcki9mLrtsW9q6zz9AjtFDC84syx8sYrZR-J1UKKNjEZ1Dqr59s3Sa9eMzN7Bt0nBxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ بازگشت فوتبال باشگاهی با تقابل حساس استقلال vs تراکتور در تبریز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31163" target="_blank">📅 00:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31162">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2QX9B7VhZZZHh63plbWvQt8aOEh4PEpu1Q7c0zTqAU_69XA_aeR0EtzOf8-RPETWRPGbTPTJX18Ln3X-966k_ljDKOhJ0pDhDvpn819MSudBTI1O6rnlzqXiGy11gueDj1nNcvnuGPjVLFmKVDw1Hy8-AHkYe2G831fUfzC_uL06nMZrnT2nhWbIBHlLa7OqAb15NyZmdyeJK1_zm7y8E1ppnYJQdsb5HqgPEkjXp9O9iJ3pJ3A6zAtUV3yKU2znUYVvPD0tW2cbcRIU1Vc9Ph2a93K-wI2R3MvMthTGrBPTfPQgTv_ezCUDrAlaGUZu9PxKhQSow9rips0TN9BxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛ لست دنس مسی با پیراهن تیم آرژانتین با تاثیر روی هر 3 گل در جدال با بنین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31162" target="_blank">📅 00:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31161">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKI6TeJ7xp1oNq16ltkBqSfJ3fELdEkZy3iO-4pF6lAOKeNeNouXzAsfeINhBWU9DChUTuC1sg9ZuByInveX39IUb72rgU1G_-mua7a8QVLO40BwCW1ih2fNrpveC07y3pKjPorucrxMYaCTz5y3flCadlII2Hw4fCA56WWAmj0JJciWOGvz1MGnRa44WALGwqu4LKbM5wfiCFN-s0LdO5QR7OdZ2wSq80_yn0z335EtByCzW4sp37hPJrRBdGVthiwXBu2QGIHrE89eZcXh0JwRbmeZj0sEeCs2Sc9WBWW6We0WXFYIMaXYB4jA8luYJN80EVhNinYLIDF1Bmib9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
محمدرضا زنوزی مالک تراکتور پاداش 500 میلیون تومانی برای بازیکنان این تیم در بازی فردا با تیم استقلال درنظر گرفته است و به اعضای این تیم اعلام‌کرده درصورت‌برد درمسابقه‌فردا به هرکدوم از بازیکنان این تیم 500 میلیون پاداش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31161" target="_blank">📅 23:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31160">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_q1O2AQ1KP3eK5x7lQN2TsCSWKZt1q77i9R8NHpX7QLEfp131y-ztVezkk_SN3s_FzJ8olj6vrwKRZ-u5I4dnHEaZaBh-lJ00OybafSgetYhVtkUQ5Cw7KZrQUo8uu93wm_7P7ZxUkQpwwJz_5G27K1F0EAG0CEKyeQHD0lZNXU5_wPzTvKJNtgq71rCIfSdlR1ksMvsY_NJKnKjOwB1ofafA5ouwL-YVaZn2ILP9BK7M7-SK245PEFNP0s6U-L6JX5ArPMT3cfj3Gx662j7k_mZGObDBoXyV167MQPQcPFEPAPfk5SOsEI8ChJ_b7YTF4YzNxAmlI6YeBJTgc3-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه استقلال به جمع مشتریان مبین دهقان هافبک‌دفاعی 21 ساله تیم الوحده اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31160" target="_blank">📅 22:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31159">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7faf22359d.mp4?token=cp3wRz2yhu5wFoZ9dLBfVFqdNx3OzOeMdfHP_0ZNEnqCLpt-SsyCuNEEjw_ExTVQfLL5dcHQNCevIMKtFrujaRvt4UyZX8CpCw93b-ZeIoqVwv38joUuo1QSBw7wSx6dmNchgB8uq_Okj43-KZa9QIGY63xdHDi1NRR3mQfXMhJE00NxUXjC9TUyabBojTPXv1UyCh3W9ZS3Lv9whqfsLS7zqNKBxdGn1IrNNJQ6SfCs7_7mpZrKTWsCKJs2bO5iFe0hkX0ZZIwQGZJWuOVpQJcHFFYCWK3rihivruNnXLQMeWW4GtbG6-TGi2Tx_UvC1XvClLdhwUiLlv2zJfinKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7faf22359d.mp4?token=cp3wRz2yhu5wFoZ9dLBfVFqdNx3OzOeMdfHP_0ZNEnqCLpt-SsyCuNEEjw_ExTVQfLL5dcHQNCevIMKtFrujaRvt4UyZX8CpCw93b-ZeIoqVwv38joUuo1QSBw7wSx6dmNchgB8uq_Okj43-KZa9QIGY63xdHDi1NRR3mQfXMhJE00NxUXjC9TUyabBojTPXv1UyCh3W9ZS3Lv9whqfsLS7zqNKBxdGn1IrNNJQ6SfCs7_7mpZrKTWsCKJs2bO5iFe0hkX0ZZIwQGZJWuOVpQJcHFFYCWK3rihivruNnXLQMeWW4GtbG6-TGi2Tx_UvC1XvClLdhwUiLlv2zJfinKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو زیرپست‌لیونل مسی: لئو، سال‌های زیادی برای کشورت جنگیدی و یه میراثی به جا گذاشتی که برای همیشههه موندگار می‌مونه. بابت تمام کارهایی که باتیم‌ملی‌آرژانتین انجام دادی نهایت احترام رو برات قائلم. یه بغل گرم رفیق.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31159" target="_blank">📅 22:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31158">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fB-mBCYEM2kpeFfaosmDDpRETgVlJYuZG-H0rF2DWzKaSJBrPyHssxdb7l9orwBrjhhruQ0kLduqun9SI9zuCxvsHKsxxAf30aMhPSe-7f3nk5CN6JQ9bK1x8yxvI5HnRpI1S8i2DWVsYzucbAQk2OxNjltRQ513pCpRAZRBYM3fCX0N9VYR--xAgHtG16bbS6b5ov2DOmQJZAO2FzoFcz32HYYcAoofu0hKasd01YNLsZA-qEEGPaXYGjUG-kLjCumN1kKbHtqw11HoF-QH2S7keJRVhqz01366jdMt0jOm0JFcfnXFhFLq3m5vKMzFmuBQiZx4GBkpDjO3A55ilw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت رنکینگ جدید فیفا در رده‌بندی تیم‌های ملی مردان
؛ اسپانیا، آرژانتین و فرانسه سه تیم برتر رنکینگ باقی ماندند. پرتغال با ۲ پله صعود از برزیل عبور کرده و به رنک پنج رسید. ژاپن کماکان بهترین تیم‌آسیایی با رنک ۱۷ جهان است. تیم ملی ایران با یک‌پله نزول به رنک ۲۳ ام جهان سقوط کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31158" target="_blank">📅 22:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31157">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxAZuReqzK90zUK7uwnINk2EPCBcGKhD_hvzyPRhUFTpeuuZi9rM0-jU87xxtuTPZdgM4GQVFzw8wxlgwpASygknp8Wpv-Bh64mtn0JSPcolQmsFvCRTKpowH2JvNIJWZwjgfHmrtCsBX1je5oNkAxlkDLyDT9-Au0Rbung1qJHilMBeqFJVzDIr0hkagx2Du3Ojgja860Vpeg8dLTBN5iv-pzido-8dox7usvNWzAiyO_nmr5CAQJRPWkdRSKDTVA1DCprmPQUelDmuXDa2HB_TfmkUxXpHaJn_nYW1bUAwe_T3QUryKZo1JRCo6ENVIK9t0HNEZebRnojUv3cvWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پیرس‌مورگان: لئو مسی خیلی‌بازیکن بزرگیه و از خداحافظی اون من ناراحت میشم ولی مارادونا بهترین بازیکن تاریخ فوتبال آرژانتینه و رونالدو از مارادونا بهتره و بهترین بازیکن تاریخ فوتباله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31157" target="_blank">📅 21:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31156">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLp4E7Cqo9WclbUs3ixbOafPc6YXi5oS2D2HNAzTgWcfTUj5X4lPIvJQoHkR3uOan-8NYQ1uOZdndNFxKFW5cyuRKJsP4AK17jSHFnx_v1FjAyzFsQT7wwBXnaqJLSSXouN10E42RiuyjEj4h1Ncm2K7mwl-SZbmC6KODPN8GfEzpqME2NHyO5ZeuaIa0ZxynOqLaT0DSmCxg29TbxyoikciB60cO8dbpHY6FEgMyqxEkTCkdd6C5Kr7V2-hBE5pKJnTLS0KGLMUjxJSqtY2fvUZLl7lqswYN8BE7yk1QY5NFT8xkfnWIG0NBanGuY8n_K7FufOivlP-XfoLyr_Pcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
محمدرضا زنوزی مالک تراکتور پاداش 500 میلیون تومانی برای بازیکنان این تیم در بازی فردا با تیم استقلال درنظر گرفته است و به اعضای این تیم اعلام‌کرده درصورت‌برد درمسابقه‌فردا به هرکدوم از بازیکنان این تیم 500 میلیون پاداش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31156" target="_blank">📅 21:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31155">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBk_IJ-ZnZyzd-6uHgVB0rbZlgTYQ6dc-81urQrzp6ldptkY_6DVX8pU1k1hp5Rk5pzxlk3MaTbbaHQYoaEhEBbIzPuAzQNKNwJZhA744JgcKwJEeCBbNc3avyAU8HyZr_mivae_LTUpF7x2mtWJHOzo49Z3r87P8Q9FeeJ8JUl22SAqLoCjiklXX-lJy2QX1vm-sBa1giQrVfcdcG52RFm_MAXchhGA2QXHdSZM1H-Xe2bKBWffePsJm6bD-goAgVM22oo1m1K2mMyL4cfXg7nhKo09oMTkGiG8ciuaQucLB1_EaBtwDokh3I9AqH5Y5jbSpms2EELbJ6wceAIbSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پیرس‌مورگان:
لئو مسی خیلی‌بازیکن بزرگیه و از خداحافظی اون من ناراحت میشم ولی مارادونا بهترین بازیکن تاریخ فوتبال آرژانتینه و رونالدو از مارادونا بهتره و بهترین بازیکن تاریخ فوتباله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31155" target="_blank">📅 21:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31154">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
هوادار تیم‌ملی جمهوری دومینیکن در پایان بازی دیشب‌این‌تیم از ماریانو دیاز خواست‌که بوسش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31154" target="_blank">📅 20:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31153">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8pKR6M8SDMzEhP-ZqXptdv4TlsEz2vlLVy9WblgG_54S7eBhbse_-I7Uqy-5vTVi1RhH_tifNx2nevvB_OPqwiTkfrHw84Nm2_EUJCwj7myyYrVgRl9ukQKBNjKE62TdmeGr7F-4uhNRna3t7NRjOei7OEiO9zaDhd7Ul740My0w-oORty9KDbjsvwUhRoK_5CLQgYmhbgAHFYimNoculfPO-THW4iDaMeTyQsLfO4cLaCAnhk27criBiqgQTApTq78_XssDHkoUNZGux3-Hg3aK7onZelKZxAzDq9Cvgh76OlM0Tz_qpM4bi4OlMFZs-RUD03Q2IEmCgnp_kpSSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌ادعای‌رسانه‌ها
؛ علی دایی و همسرش دیروز برای‌حضورتوهمایش‌یه‌مجموعه خصوصی رفته بودن قم؛ امروز دادستان قم به خاطر حضور بدون حجاب همسر دایی دستور پلمب تالار رو صادر کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/31153" target="_blank">📅 20:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31152">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe648d4e8.mp4?token=HK2fniCp9pjzYWaxU_5-GCTO3YvOyI_UztlCwo4hlMqdJXaS5g9hsYB0MNyv2xZkn39n_ujSsf37po4bed5nZU3g6AnN72tJDpu1n2ZL5KexCLYUxWctNIl1G-L28G6NbAGbR2XiAgh2296SjgF_FF5mJuI0LMpqwjbKcN5Sg4XXi4yiCxKKcmHbGeBYlZ-tVlI3sAL1II6oMBeBWgGk-GqJuqojZHnfJs3A_b_Wh6H-T6pkRbayt6jWfNqf_5R1n6c4BW3Lmnldsl6QpC5bmp3qCQQACoF6GtHCtvcF_ziYzLcH6nrtNqVoiVmRRiV65fRE3PXYdfq2u-_IF0SMDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe648d4e8.mp4?token=HK2fniCp9pjzYWaxU_5-GCTO3YvOyI_UztlCwo4hlMqdJXaS5g9hsYB0MNyv2xZkn39n_ujSsf37po4bed5nZU3g6AnN72tJDpu1n2ZL5KexCLYUxWctNIl1G-L28G6NbAGbR2XiAgh2296SjgF_FF5mJuI0LMpqwjbKcN5Sg4XXi4yiCxKKcmHbGeBYlZ-tVlI3sAL1II6oMBeBWgGk-GqJuqojZHnfJs3A_b_Wh6H-T6pkRbayt6jWfNqf_5R1n6c4BW3Lmnldsl6QpC5bmp3qCQQACoF6GtHCtvcF_ziYzLcH6nrtNqVoiVmRRiV65fRE3PXYdfq2u-_IF0SMDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید شد؛ با اعلام حمید مطهری سرمربی فولاد؛ رامین رضاییان ستاره این‌تیم 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31152" target="_blank">📅 20:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31151">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gM-eUhzCPwl5fueEqjvxSiL_LTWLJzKDa1Z8qJ_E2D9Odvu5P_OcQVNB4sR0ArByBArv7rW8O1u1TV80cf5jV-wGB2eopicm19PsNVY32Ki6H3wObkk_vnv-OAJbUWECFKDyKb1AJWLza32ffIuKUiRAhBqI8Cl7Cvrszh2jexrsDY0Xqf6-ikv_bmwrmlYHE8qTDp_sGB6nw6GoLplCHSQEjmhcEO3Lfg3QaCjCUoM-AuZpuUH7sJwFj50m4Yglc7JwWumxRUyqYvCy_i1HBv6DtC1_hWhSFkWY8WEfw6cBVpTWtAmjaPIkKXQDLigKZknhIhxf6o5RILFuytvm4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پدرو ستاره اسپانیایی سابق بارسلونا، چلسی، آ اس رم و لاتزیو در سن 39 سالگی از دنیای فوتبال خداحافظی کرد. پدرو تنها بازیکن تاریخه که تموم جام‌های معتبر مستطیل سبز رو برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31151" target="_blank">📅 19:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31150">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/819a21a6ba.mp4?token=sMI6wNwv5wVuypZpeRo4811ogVzpKpLU4utiTSxXy5Kwscf_1wgmc5S5Dllzf4ROF2M3meq-ulDkXdx5S76gO_OckajTBM3BDDz9Lga3o5xAW7C0UxqJZExtGoDkuVexZvHX1BgRNQ9dSM-viA1Lr-cBRj5M5bQJXPuLRrMksyLerVmWC-N4qcj4U27f0C--m9NOy8VCOjssJJ8PYCLfhhl-__zp2HN61eHoqYL75aqaibtF22iu_Baa648ahI5D5r2RB3OHn9qrPjsx5YJZ5zkypFWgSgQ0hjVcooa2ZaSP68mcZtE_xvD3versJvCHxUto7_u1_YG42xWL0eTDWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/819a21a6ba.mp4?token=sMI6wNwv5wVuypZpeRo4811ogVzpKpLU4utiTSxXy5Kwscf_1wgmc5S5Dllzf4ROF2M3meq-ulDkXdx5S76gO_OckajTBM3BDDz9Lga3o5xAW7C0UxqJZExtGoDkuVexZvHX1BgRNQ9dSM-viA1Lr-cBRj5M5bQJXPuLRrMksyLerVmWC-N4qcj4U27f0C--m9NOy8VCOjssJJ8PYCLfhhl-__zp2HN61eHoqYL75aqaibtF22iu_Baa648ahI5D5r2RB3OHn9qrPjsx5YJZ5zkypFWgSgQ0hjVcooa2ZaSP68mcZtE_xvD3versJvCHxUto7_u1_YG42xWL0eTDWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عصبانیت شدید نادر قاضی پور از سوال مجری صدا و سیما که گفت محمد رضا زنوزی مالک باشگاه تراکتور ثروتش رو از راه راند بازی در آورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31150" target="_blank">📅 19:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31148">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJRAytzPr7Hf4KooXqQlrNE5uHT2E7JG2Kgp6B9xPbbCWbuX3u9OktcKHfvpq81m75-uIC4czK6a4z82FU3g7JnCxGyF5WU8lkO_4hd4z7vSfITUoecub9_aDnoohdFAtNsC3Ov5Ws5cdAjB0eAYLBbA_bR6NXlU1lgHQtoeORonBwGbYn4QyRLq0EK1jibhBfKkmqkIdg82OsT674VFT7KFoq-Z6jfDDlbH8fjeDEtU0JaMMwAKHlgkN3nRa3F52NV4BwEku3QVcu9wt_KaADs2fb0qqShlVjwzMjH7sPLtZLLrOmZAXhDOCujbl8lxqmDltHD2WyMG7cCGTY5Wzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رضاییان از بس گفت تو دوران حرفه‌‌ایم مصدوم نشده ام. این‌بار یجوری مصدوم‌شده که هم کشاله‌اش کش اومده هم از ناحیه خصوصی بدنش آسیب جدی دیده که ممکن تا اواسط آذر دور از میادین باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31148" target="_blank">📅 19:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31147">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPJcq0DpMnjPGwsPEET-_4jHYo03auvcjlHCJgRi8Y--652hhthyaUWu_y--jJWAfybQoFQKGdSpa08iBED8tImZoxVCr8GP1Uz3TJmABlR-HBYDZ2C56661TV_-xGtTscz65okCvbvsAobg6gaZya0qLOUBPKTmMMqGjG1DegJoF1oiv-4jMywRc4s-PUV2i894yodP-KxH88wsHjb-ExhVEQFPmvReRis5i9i1dSW98mqSycefofUBXFKjobFvnkeXpLHWzhOdPkgDchRzJA-hMf4_TuVeHe3G02j4z-_7fsB5SJ1nzrOECMpUn1PLqTrWxYgije7A562YLz7RxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بعدِ 3 هفته‌کسالت‌اور و حوصله سربر فیفادی به پایان رسید و از فردا فوتبال باشگاهی شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31147" target="_blank">📅 18:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31146">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a875cd8726.mp4?token=tYAb0UiHDAGD0YLjYCL15uEwc_J4x4nO75-_bYMjrhQ7JxFS1GTe7gO4eeQl3FrjMG1asPuMojoTxmMhBhyfoPC-lW3jAD62vEXOO0fcylbAdVfavBPbkutc7ZzvwUAJ3enejCbmQnIZJ61R6wUqBrM3B_MFF9valarefb3jb-M24IPODmS4R_6l_9AQVFo-kRDRURNWsOffy3SyuxB7bPlyfzxYBOk6kqDPFG2dTIxiuOSc4tvDm-KXEm2RbJZdqaPQJOiFbOARwhfsUffde_gjqs36pwheDKSuPrfHFhtmQ9jUzMHEVSO3BqXBV5joTYPjlQFnY6SY-rsr8RWhYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a875cd8726.mp4?token=tYAb0UiHDAGD0YLjYCL15uEwc_J4x4nO75-_bYMjrhQ7JxFS1GTe7gO4eeQl3FrjMG1asPuMojoTxmMhBhyfoPC-lW3jAD62vEXOO0fcylbAdVfavBPbkutc7ZzvwUAJ3enejCbmQnIZJ61R6wUqBrM3B_MFF9valarefb3jb-M24IPODmS4R_6l_9AQVFo-kRDRURNWsOffy3SyuxB7bPlyfzxYBOk6kqDPFG2dTIxiuOSc4tvDm-KXEm2RbJZdqaPQJOiFbOARwhfsUffde_gjqs36pwheDKSuPrfHFhtmQ9jUzMHEVSO3BqXBV5joTYPjlQFnY6SY-rsr8RWhYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این هفته هرکسی برنامه داشت امیر قلعه نویی رو تیکه پاره کرد؛ این بار نوبت به تیکه های سنگینن ابوطالبه که اینجوری زنرال رو چپ و راست کرد.
‼️
ویدیو کامل قسمت سوم برنامه ابوطالب رو هم میتونید از طریق پست ریپلای شده مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31146" target="_blank">📅 18:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31145">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riWMvmy3QtFlSa08kQrezV076i6qKl21YGj5O8SEn0nk0o0Blny62q4CAKRlqFtU9c7rhgVTPskJm2tt-Jqc-0a_fmUC10VqLLfOXzq42bXeU9frh1v7YbELxUiDvzgEr0Sckccc_K1fDp83w9WuPkxWzgTUHrdiWd2khqTu3sqFlp8_o0xErPJ-C2-BpkWV0_VOInMDcFwcgSjlHGJlmiyYuwW1SLXo3S8F8DxPsOKExzvjSFk13htqqtR5iOOfdpXx57Gzi64ICOPZS67lUQSyhXa01q01fqIX8ntsU4o9nnIBCtOnONLJ3npD-1znZEce7CukJgVYy317YwBNrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇫🇷
نمره‌ فوق‌ العاده‌ و‌ خیره‌ کننده مایکل اولیسه ستاره 22ساله‌تیم‌ملی‌فرانسه و باشگاه بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31145" target="_blank">📅 18:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31144">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fa4ce212.mp4?token=EPSjRBpTqRcGGN3tTzs5PjW6ysXjtLw9p4u8zKTNWg5XpU-RENjcCo8AkN23UBK9sbvGu6EAKO5CHShnQileCpMQdKAbbmh_RobBiWcb_A5Xf9gI9ctgtaS5rYtv-CsJEsPxISuLjihcUorgaskYjL5iJeArO2vY0_enfwNTLZ_BWC1Q1aI_jEEOxKccoRDFMx2xpLmgf-C8mcLCnrzU6lbgfTcnyIcmOVz-9WcuO3SWqnb2KTxUhRrusezysELYTxO8g9AcwviM8GWB3W-wBrffiAbgAw0z3vS-4zbIzzX3oV7dsqkSZUG-r3zpColDmVsowDPjn7T3-1-OvqJWbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fa4ce212.mp4?token=EPSjRBpTqRcGGN3tTzs5PjW6ysXjtLw9p4u8zKTNWg5XpU-RENjcCo8AkN23UBK9sbvGu6EAKO5CHShnQileCpMQdKAbbmh_RobBiWcb_A5Xf9gI9ctgtaS5rYtv-CsJEsPxISuLjihcUorgaskYjL5iJeArO2vY0_enfwNTLZ_BWC1Q1aI_jEEOxKccoRDFMx2xpLmgf-C8mcLCnrzU6lbgfTcnyIcmOVz-9WcuO3SWqnb2KTxUhRrusezysELYTxO8g9AcwviM8GWB3W-wBrffiAbgAw0z3vS-4zbIzzX3oV7dsqkSZUG-r3zpColDmVsowDPjn7T3-1-OvqJWbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
استایل جدید مجری ممنوع التصویر صداوسیما در عروسی؛ ایشون سال 1401 بعد از اون اتفاقات تلخ پاییز از سازمان‌صداوسیما قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31144" target="_blank">📅 17:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31143">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ec12f29e.mp4?token=mkCR-PHmcadia6Pkn2lbExQyXrKcKHc7ZjQ4oMuO84TBwadPj7Fqlk8ghCpbRB0P55T6BQqOo-Rgm-PdJ7GNVIMZjpjtrppdLRuiECw2iFmLBzaW0l6RD1Ol13yEnBFl2Qxk4I4KNQuNoXkmIzy_mMJXbh9IBTt2vSP08Cnn6jUw-MUZGNECQod8Rkp1eA4V7qrz_PRIDL__K794G__jptA7VB9kphHi3QkKZO17I0NPQOFwkmWIenRD09GHja7Qq9x6yoep7qYDrA7W-cR12ORLbMjuAzCsypo31dGnPE9Czq9SYd7_rNLSfOeKz7DoYOdIPGbjfzHYmtTC1OCVxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ec12f29e.mp4?token=mkCR-PHmcadia6Pkn2lbExQyXrKcKHc7ZjQ4oMuO84TBwadPj7Fqlk8ghCpbRB0P55T6BQqOo-Rgm-PdJ7GNVIMZjpjtrppdLRuiECw2iFmLBzaW0l6RD1Ol13yEnBFl2Qxk4I4KNQuNoXkmIzy_mMJXbh9IBTt2vSP08Cnn6jUw-MUZGNECQod8Rkp1eA4V7qrz_PRIDL__K794G__jptA7VB9kphHi3QkKZO17I0NPQOFwkmWIenRD09GHja7Qq9x6yoep7qYDrA7W-cR12ORLbMjuAzCsypo31dGnPE9Czq9SYd7_rNLSfOeKz7DoYOdIPGbjfzHYmtTC1OCVxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های جالب رسول مجیدی مجری شبکه ورزش درباره اسم یکی از پسرهای لیونل مسی که چیرو هست. چیرو به فارسی یعنی کوروش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31143" target="_blank">📅 17:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31142">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piA5L6m7-2q80wfnqhm_NbBkJgnbeFpGOxwpSiAKQ-b2bvLL7VUhlYM0DIKANXDUSpCMWTeosXxeqwt_CuIZmzMUNh1xfzhG5Z4pTaYaGUBQTAEJ99J3sADlXg-ekgB32PbxNpOTsGGPzDElv-lHUK3gPQumdoC3dJeMeCW95ltJpKIXZjrVN7xpbMQwPuPvaYCAD1F3wGwyfylJYQg5oVwaXU1j35TOWGRAWp7Y9FqLmQbhHO-nH5j8-TnVZB8RaG1OazdzzoRYlRdltd_gDFE0IwrHx-qSnyNH87hAmAe4MUOHVY6GPlTPX1OAtUCGMLBTpsOPLn2IQ00fqk2qhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌عجیب‌دیفنساسنترال: کیلیان‌امباپه تصمیم خودش رو گرفت، اون آخر فصل از رئال جدا میشه و میره لیگ انگلیس؛ امباپه فصل بعد تو لیگ جزیره:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/31142" target="_blank">📅 16:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31141">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae97c5b61b.mp4?token=TLSVlXaIjAbNHlP-6U8CynzSnyM3sUw-6Lb8YpcHeMZ5yW707jHNM9njmMI6pz70QcLWTDqHHqmVfA06BzURQibOs7Pq7INyj5Gn2A6ZHruun_CiE5Djw2DtDXiJH0cVzWZCHtePudI_ZV37IVS6bm9KwtQCTXTYV5GNHySQjKFp96Lid4klY2Z2Gr1pKAT6Ai-k2rCVcRRgUcYEDPlRWWH_uttj-VdK-onorq8boogYk3nRfVVsDDzdu7JeF7r6yqKQTIY9StdRez_y8Rwd39-7udxK9PqPLQjkvCfg3QVDIph2PJ-CkvlRU_W7G7h7vRp-QnZyaVAn9swstWXnMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae97c5b61b.mp4?token=TLSVlXaIjAbNHlP-6U8CynzSnyM3sUw-6Lb8YpcHeMZ5yW707jHNM9njmMI6pz70QcLWTDqHHqmVfA06BzURQibOs7Pq7INyj5Gn2A6ZHruun_CiE5Djw2DtDXiJH0cVzWZCHtePudI_ZV37IVS6bm9KwtQCTXTYV5GNHySQjKFp96Lid4klY2Z2Gr1pKAT6Ai-k2rCVcRRgUcYEDPlRWWH_uttj-VdK-onorq8boogYk3nRfVVsDDzdu7JeF7r6yqKQTIY9StdRez_y8Rwd39-7udxK9PqPLQjkvCfg3QVDIph2PJ-CkvlRU_W7G7h7vRp-QnZyaVAn9swstWXnMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناراحتی شدید علی آقا دایی اسطوره مردم ایران از خدافظی لیونل مسی آرژانتینی از مسابقات ملی‌.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31141" target="_blank">📅 16:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31140">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVHsNRLdDdCZoZPjAcMUtlQ75-bgU8JrQqzQ83loWxBobxkxKJVLcNr5lzs9yBwt2x28FCe-ge3ixjv-XFJoKn41Biyz8w6U0ke0HfX3VtTKQtuLwTv8l9AqOpeEhrqhfVqnstzkqjD8q8UuRdkG24ADQiEWcU-b44ui1UX72i7Q26h4an4rtrBTBl3olVBxolA44j1nk_m_xHfyIBqZh_JT_HynYFLGjKMHMMqY564vFKJ7ilzDNYuPTJ61x-qUH8AXHfgbohNKYL1dc6FRVwxRrh7SOYw1EMFqskKG1wlm_PH4xe98sEQ78PJ9ssu9DIzXYLfq4UuaBV2FDww2YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه آرسنال دقایقی پیش با انتشار این ویدیو خبر از تمدید قرارداد میکل آرتتا تا سال 2030 داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31140" target="_blank">📅 15:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31139">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uo_Rc5xru-epMPOlj4BPTA5bkX1Wh6pVeV_jIBVnZZTU6WppNm08t-tBxa4PSACG_yL0kHaHR5EXOlHWUrhoSPrXgjvmXZgU4eMKTSkhu0ksJuwPj3jVbsRRDcC6wcWsCnCKGg5ziIHajixAxPIIhpWL52MLuVRJS6jxB5sKWqISh12ZPP4JfxJiWbh6-Lj6MZVC9vJxOu-MHLW7MqdYCAO8DVCaP8vDEx6KxYrNkNgDSOQ-HNlxET_4ZR_-bDndCW33fkK7KtKAeLWCRIyHHdSVAnSgs8bJrXAM7T5AsoBAVtdvbeYpoyvLTxFl-QEeUB9lJhzp9NfcNpeGM46vvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج10دیداراخیر استقلال و تراکتور در تمامی مسابقات: 4 برد استقلال، 2 تساوی، 4 برد تراکتور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31139" target="_blank">📅 15:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31138">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b5a302929.mp4?token=PDITKlZR4uaB702tsuEN8Ka0TevN--RqtRTbscnkRQ9aNpV7CWE592gE4QDsZbRAdlLU0bxN4SztL0bqmk4ve64070ieP0KR6CILa45N9FFtr-8m0Hd1PGRWqQNcks09Y6qqIvRB7yG-90wcsq8FPaOVkO3na9TH21KBgC75enaDbjbvjg8LgfkxaIhUmY1mQJv90TlkF4sJh9xih8dNZAKSvqhoWM51BzhpQZWt52hdiMX6K41wjkBSXzjZtp1QhRbsI6rjM1A5sYnf4bQdTQDckKuu5ORto6j8hmzMVZuwUtXY9Z-2o8FF2OWxumnSy7iZ33ewFmV_t7UOS96Oyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b5a302929.mp4?token=PDITKlZR4uaB702tsuEN8Ka0TevN--RqtRTbscnkRQ9aNpV7CWE592gE4QDsZbRAdlLU0bxN4SztL0bqmk4ve64070ieP0KR6CILa45N9FFtr-8m0Hd1PGRWqQNcks09Y6qqIvRB7yG-90wcsq8FPaOVkO3na9TH21KBgC75enaDbjbvjg8LgfkxaIhUmY1mQJv90TlkF4sJh9xih8dNZAKSvqhoWM51BzhpQZWt52hdiMX6K41wjkBSXzjZtp1QhRbsI6rjM1A5sYnf4bQdTQDckKuu5ORto6j8hmzMVZuwUtXY9Z-2o8FF2OWxumnSy7iZ33ewFmV_t7UOS96Oyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
میکل آرتتا برای تمدید قراردادش تاسال 2030 با سران باشگاه آرسنال به‌توافق کامل رسید و بزودی با حضور در باشگاه قراردادش رو تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31138" target="_blank">📅 14:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31137">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCMKz93PHU96H8j83T6IDHaGu3FF5iDJnYUwy9XS2DI8p5xU3patsZoUpmEs3u-E4fKcesjIssMG1-mpE8BquifXeVh4gXLsPqX-SbTMRYBfG6AQFgR5e5DpnexxZooFhJn7l5CP_vjn430koqDAUh8N7upvvla2JMPkjtCkozPEwRo38sZnwrMqnvGUYSOUUh7de4XdLISK8telJz3ojZ4KFd4PAdcPel3ZC9kpSlPlflTRHPKEnjriUH6pQbjbOBAnF9Er6G8UTOyaK6gxZIGmq6lRH4RZH3CNTjJS2vIQU8AYbdjA2z-g74TmdoP7IxjrEVcgnd5ObCKcJ5HNJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
ویدیویی زیبا از تموم جام‌های لیونل مسی با پیراهن تیم ملی آرژانتین که از 2021 شروع شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31137" target="_blank">📅 14:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31136">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkJddQEfUxSOHjK1POrcyiqQfWcdVx0b5nedKEq2p8isx68GQHtz_4go0TADVXWytIRUfEreg6f4eG7xbNKwOYoqzFJtZxiqe15JMPXpcMfKlDF-tCYe4rByJ2clzPvahv01E7mpaa65r5VvVRTdIrci4pNvxqe9VODF88TyO19KnQUoxn9jX2VaDg8X-z0ZL5sCPdg9evDusvQrarrrERWN6UZh1R6Qjb4ge_z8g1U4n4g2YcQP6nFCzMpbT55plWdS9q59QLtsI69jH1UEZyD1q3RLWypyC04g490SWIAOXJYRUTRv4taZEBpfVCNoZckdFhMUmPPWDZ38-1CLsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جالبه‌بدونید؛ پدرو همچنان‌تنهابازیکن تاریخه که لیگ قهرمانان اروپا، لیگ اروپا، سوپرجام اروپا، جام باشگاه‌های جهان، یورو و جام جهانی را فتح کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31136" target="_blank">📅 14:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31135">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d783b6322.mp4?token=U3LhfWVEFa-S-fZQQIu--W3OmkPXDhKFSXLeqLl3SWgwkSayXMcHv5mBCjfr_EmEp1oxWlglFUYTxSi954pGaFmCgyI6UTI-pHqEhh1Z7P_-fUNKgz6thLFQl4k2JgGtsPbL1uuRSVPh1bm4pcSQ_pQPtTk9RAavudYqBxSZw0Z0HP7ZFXirzd2ZyWP0hslrhUJtxFP04C1lk1yc00v5pQhWmy_psS2VGmHz2mmbUxcik6SFCvv8ggLJaKX0nD9Z86cHh2UCnuii-qcIt7PGwSfIMI544132Nh4nvtdCW4jh_xQeEf-w4jyzIG_FpgZA01plhahVpiO0EN0k4OxOyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d783b6322.mp4?token=U3LhfWVEFa-S-fZQQIu--W3OmkPXDhKFSXLeqLl3SWgwkSayXMcHv5mBCjfr_EmEp1oxWlglFUYTxSi954pGaFmCgyI6UTI-pHqEhh1Z7P_-fUNKgz6thLFQl4k2JgGtsPbL1uuRSVPh1bm4pcSQ_pQPtTk9RAavudYqBxSZw0Z0HP7ZFXirzd2ZyWP0hslrhUJtxFP04C1lk1yc00v5pQhWmy_psS2VGmHz2mmbUxcik6SFCvv8ggLJaKX0nD9Z86cHh2UCnuii-qcIt7PGwSfIMI544132Nh4nvtdCW4jh_xQeEf-w4jyzIG_FpgZA01plhahVpiO0EN0k4OxOyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
مقایسه‌ارزش‌بازیکنان دوتیم تراکتور
🆚
استقلال بمناسبت بازی حساس فرداشب دو تیم در لیگ برتر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/31135" target="_blank">📅 14:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31134">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3866613d1.mp4?token=qN7_GU2Ctism3QTKVukcY1QIsOUakI5BXsAMk3DNpE1iDvYM-v1DFxJd7o8Q_0uJ3_4PxKYaDPYZcu7Pwp23WVg4zSmH5-UB_QN73nVhUPJA6MnXAtSJLKVIH9GbBfAtpQUd4I7oORZeoQ59nHXVgkPfC76N6iP0FbzTtjjnNd_E8XN_e_GxRQU-ibRncPpM4fkA739OUaBQ5vqsFfHYN-mc1IVjAa4PHg_-Jn77s2b6NZGNV_bIH23jnfgdca4LSjB1rrkDvCliIi1gC784YqoZFdEBZzsMWn6jsMZmLRYXsghmw7UEB1NkaSNPbPikFw6TY-H_cAfcAT-EeBqblinrMNfQfuJTAv3aS9-UkWkHR8vcQWgAPGV6na3MZGspUIDsn3oPZGKiJrsSBh1JXLQf8BUorxjjhpTgP3HFlI9xJnQpaHBfGMbhYBdCixWGb8SphyqvoroloiHmOguBYzSJeOR5G574fCF01gvH69zmi9b60V4FCc8gWDx92NDPUcMeM7THRbtSHbknd4b_DmA-8dX_nNm7AqcNJH4qiUzY3JYv5OcvMqSJqUWrMl6VIXyOQL9abjoIS_zXnvckbhibfP3U5Vsj1E5tmBwPAhUxe7nYnqd5g8QjSyxoXs-Naiv95eteC1lLKQT3HepPlSoBygrI4WUtaRHfu1_Y4Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3866613d1.mp4?token=qN7_GU2Ctism3QTKVukcY1QIsOUakI5BXsAMk3DNpE1iDvYM-v1DFxJd7o8Q_0uJ3_4PxKYaDPYZcu7Pwp23WVg4zSmH5-UB_QN73nVhUPJA6MnXAtSJLKVIH9GbBfAtpQUd4I7oORZeoQ59nHXVgkPfC76N6iP0FbzTtjjnNd_E8XN_e_GxRQU-ibRncPpM4fkA739OUaBQ5vqsFfHYN-mc1IVjAa4PHg_-Jn77s2b6NZGNV_bIH23jnfgdca4LSjB1rrkDvCliIi1gC784YqoZFdEBZzsMWn6jsMZmLRYXsghmw7UEB1NkaSNPbPikFw6TY-H_cAfcAT-EeBqblinrMNfQfuJTAv3aS9-UkWkHR8vcQWgAPGV6na3MZGspUIDsn3oPZGKiJrsSBh1JXLQf8BUorxjjhpTgP3HFlI9xJnQpaHBfGMbhYBdCixWGb8SphyqvoroloiHmOguBYzSJeOR5G574fCF01gvH69zmi9b60V4FCc8gWDx92NDPUcMeM7THRbtSHbknd4b_DmA-8dX_nNm7AqcNJH4qiUzY3JYv5OcvMqSJqUWrMl6VIXyOQL9abjoIS_zXnvckbhibfP3U5Vsj1E5tmBwPAhUxe7nYnqd5g8QjSyxoXs-Naiv95eteC1lLKQT3HepPlSoBygrI4WUtaRHfu1_Y4Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم از روزیکه جواد خیابانی وسط گزارش مسابقات یورو 2022 ول کرد رفت. عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31134" target="_blank">📅 14:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31132">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbFHosYGuaX4U9j4NHXdFgxhj3Pzq7qLak8EwGc55ntVJaKWxklgJSkGMnLd_Sqlf6CpXXAmMJH8Dc2bLO4-pWjO1-bh1jfWGd6rDN8Tc9EcuOmpXk1PbNGgoQgE3IX8iUNmA4qlnQu1AYiTuSjc-ooxUl5DnKXqAIpebzkx4mY5knaPH3bRW-RND-01DQI8J9R4hAVckWsIWyj3qdJY8w6MDOIEY0SgebEBAvtfKZqSNpeZPH9RjgfeV7rFMnHQHLhD49nt-wljw8yNCq3NNUjVFVxfb2wOKdKmXYodhHHRT3ax-zaH2GUsiPjYN3iPzRpKx-imAe14bA7ht00pHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فرانچسکو توتی درباره‌ افسردگیش:
بعدِ اینکه فوتبال کنار گذاشتم و پدرم رو بدلیل کرونا از دست دادم، همسرم‌کنارم نبود. بااینکه بهش اعتماد داشتم همه به من‌میگفتند همسرت‌داره بهت خیانت میکنه.
‼️
من تلفنش روچک‌کردم تاببینم راست میگن یانه، کاری که قبلا هیچوقت انجام‌نداده بودم. بعد از چک کردن تلفنش ديگه نتونستم بخوابم وانمود کردم که هیچ مشکلی نیست، اما دیگه اون آدم قبلی نبودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31132" target="_blank">📅 13:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31131">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lt1ZSMRluTR9O_F8FDygbqKmwpk2BRi1DC4Pl7bU5LDRKTLgvnLqhj2WFpyXdeo4Hn0MGHQcGTbLyqaoldqLRFI5w-vehaQinRgFxSagIoJof4AEqJRBbqTjR9mG3GyTrhsBnBMG5LoGV5EEsCaMPArvMbXNLx1JRkt7COEHXg0NyWBGJ09fNJKS5Ccm6d9qdFQPo6Y6nu37GUwYUVU3tcYwOK_EL5zvfu537F2kfNYUzdBgT-CjxcRMdAP7N69LfUDW5KSawkUONZxBrIwgKbHYnsmHvK0r4Q4O3XZ63OP2UpPodXhgLhaZOqcI6pyXUEoLIIWhFqRSphrAu26MQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
ویدیویی زیبا از تموم جام‌های لیونل مسی با پیراهن تیم ملی آرژانتین که از 2021 شروع شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31131" target="_blank">📅 13:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31129">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ceb15f26.mp4?token=MIYi6HgzbljxplJawgDE4Y9U8G57cCpmab1Aq-lTUfYEJQBnUWPbR2Ss7vmt9qDy7_5_NyKHS2HtLp3r1MWhO8vOgPac8HSp1tSKG3zrDwh2ZCViuFfJYjR4tk_GhegcgEB-Ks5OlYNQuw6oNBSkq9mPbqaQQSp1dg5wp_Wu2fqlEFbzX0Bn-XgVY2kfbdHaHratLMxl1CB1L372NB1VomJ6Pjt5UKa4CQyQqUk0wzjRVqSCK8QEzKcX8tiA8_jvvw9xH0AOjWKs7ayJ-k8NMh8L66aor4x-1TyOh-DMdnAty9wy3vem02vriGRus9dcB6dLd5b2r4wrfMX2BwHbzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ceb15f26.mp4?token=MIYi6HgzbljxplJawgDE4Y9U8G57cCpmab1Aq-lTUfYEJQBnUWPbR2Ss7vmt9qDy7_5_NyKHS2HtLp3r1MWhO8vOgPac8HSp1tSKG3zrDwh2ZCViuFfJYjR4tk_GhegcgEB-Ks5OlYNQuw6oNBSkq9mPbqaQQSp1dg5wp_Wu2fqlEFbzX0Bn-XgVY2kfbdHaHratLMxl1CB1L372NB1VomJ6Pjt5UKa4CQyQqUk0wzjRVqSCK8QEzKcX8tiA8_jvvw9xH0AOjWKs7ayJ-k8NMh8L66aor4x-1TyOh-DMdnAty9wy3vem02vriGRus9dcB6dLd5b2r4wrfMX2BwHbzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
دو ویدیو از علیرضا بیرانوند دروازه‌بان تیم تراکتور در پادگان حین خدمت سربازی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31129" target="_blank">📅 12:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31128">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7oDgU5_zn7FTti6GSrep5BsEfg2DuRbQ4RS1t06j9Exy_SA7Jeqft9aHykSyj5FDWcfVuxTlvVa95SndnC9X1YxF2fghcmjqUncn2tTI3aj2bxEyst37nHQAg63Ehb0KJyhsDy6TbC0SETXR3cEUuigRUkqe0kbNOe4XmK-HOo3h9k3GGJ-u2Y9bMCBbcFJwZ7Ka3cH1GJ2mugZ_Ovv2ChO7Aqe1-Ctik6DgOv4gk7N_oj3iZjvWxE-Q5_M4RC0E5paxFBetF1YuuxYk3DnQmhFyG2QRULTkqeBCq_EjlgiUd4MSwjxeptEomikLL673Dfwrce7-o7LVXSIA1LcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ رامین رضاییان که‌دربازی با روسیه از ناحیه خصوصی دچار مصدومیت شدید شد حدود یک‌ماه دور از میادینه و احتمالا دیدارمهم مقابل تیم پرسپولیس درهفته دهم لیگ رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31128" target="_blank">📅 12:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31127">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9llgabZl4pZlg8PUfBgH_cAMIiYHLLnLM-Fqh8fdSIx1UxfJc2ZDghZ49Yl-2L67dCOB2p5p1wJwxInNh8fFxQT6DSU2WlH-SCWtXW8cm9SrfKT37MOlAYkrS6tGTdNZRUQ3OLxG_lRe08rjVal5ee4bp3tnSFDe6yi0xAs5Dzu_pm3pdko74XcT-6sRj204yPwacYXPwzM4ANkU94F_MOwJmnQQIzomKCmdtWuW2ZIUx5U6QrTYBQ0MmurHCDkERX-YpkuCEODioj6QShQuY6fBMmKG-yprGv4v4C1kcZDO7ytp4iZ5xfP8S6H0poeyCFJQvqTtgrLeB7_kihaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
#تکمیلی؛خبرنگارباشگاه النصر امارات: کادرفنی‌النصر از عملکرد مهدی قایدی رضایت نداره و تصمیم‌نهایی‌اش رابرای قراردادن‌ستاره 27 ساله‌ خود در لیست‌ فروش این تیم در پنجره ژانویه گرفته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31127" target="_blank">📅 11:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31125">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce783c6799.mp4?token=Y5xZYrsYVmoXoXvTaKYxAMDYiYlnoDj5nnRfySX--zsrY6-oK7CaK5nb39O9_USWJlTQ4LzMNxtky_zUJy4H0H6Kcbb6Vfjr9DgcOhiluubumZKH4gBRtLh8VMaFdthwIkNcv8jf1bxa6NC5fl4qBUg2EgnSe4FwRHPu7hSPRlkbJhg4Iq47fwi3auhUPcgKZRnWLMM6SS1T97wbqyXv0zHGikPEi8SfzneuN3MsCgK7UsQXF5n5jhrp4a2NZhvb6Cbf9tNa0iKoAVgOuNV2aZPmh5KyyvRW9wMol3Vf1qRRsAor-SET6ZMGM9PB8H7bR_CzDrmPhN5IeBVOKr-9zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce783c6799.mp4?token=Y5xZYrsYVmoXoXvTaKYxAMDYiYlnoDj5nnRfySX--zsrY6-oK7CaK5nb39O9_USWJlTQ4LzMNxtky_zUJy4H0H6Kcbb6Vfjr9DgcOhiluubumZKH4gBRtLh8VMaFdthwIkNcv8jf1bxa6NC5fl4qBUg2EgnSe4FwRHPu7hSPRlkbJhg4Iq47fwi3auhUPcgKZRnWLMM6SS1T97wbqyXv0zHGikPEi8SfzneuN3MsCgK7UsQXF5n5jhrp4a2NZhvb6Cbf9tNa0iKoAVgOuNV2aZPmh5KyyvRW9wMol3Vf1qRRsAor-SET6ZMGM9PB8H7bR_CzDrmPhN5IeBVOKr-9zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تشویق و خنده‌های آنتونلا همسر لئو مسی درشب‌خدافظی لیونل مسی با پیراهن آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31125" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31123">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz14x6qzaBsEpr6u1LxY54UaOrjjzMmVglmvM5_HlvoSUlmNDJLYP80GDmXiQvtO901ildOiVdAIB1XL1erbn-jPbRESfFfn6VPNYeHmy9M2n73axj6qH-ezzM3A9S6Efk_s4jGWSZBp4WYwooOCf5sQIdbKy9SJAuUgWmdj8DQ1OptobIjsIZFZ-5_DW_3dbxd0YuMf2HnyFl0UDwiY-ma1LPd-JyMG_HR8p5-g39nIlis8UIgxLGEjV-H5fDseoTGpysK9g6wv8yZcbjttOjYGfjPIWUtBIF1S6ozNM-_jn6ebYvZOzzohtuO9UJ2sIplyLNw9R-WGpMIruE2qHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد لیونل مسی
🆚
کریس رونالدو با پیراهن دو تیم ملی آرژانتین
🆚
پرتغال در تمام مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31123" target="_blank">📅 10:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31122">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmjDf36Sk7L3ytDupQDLce2nc8qCjzi903A3a72J5Gu6H_8FhpMQ4JZX8t3B_K_KrVd0QLkjuaFVvBk2sMxHHorKm14lyVtlXvDBo0A23D_FDulO6lghQThoIsQocmf2xW9qRwJzsJmNSHhNr4aFxNOGh2BjFJ73aSaLigkTd92AN5NwMA5-1J3yToebx2IQyuvsHpoOKRCZTbzNCR-5aScz-_CwKqdIPmVk2rFyy2NurfIvnT6hH9YQLuvwAFceec722_RKit5blATfpsBKLXmptq06P0zpOuM3rd816SvtR5XVxl26_g-tFBX5YLZBn6E3tw1Vnl8qOqQYzzxZbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام 126 گل‌ملی‌لیونل‌مسی به تفکیک هر کشور به مناسبت خدافظی همیشگی او از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31122" target="_blank">📅 09:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31121">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxyxdBreVPhz0ZybeVXRJMx3vEBtk83ots2CVACoYfY2eY53cdqv1YbOZToNMvqLWPKiyh5qIwlj9dJfnGGzQvWbm-JiOa-PXrqAQTwG7G8i1Zz7TOdUFYJBIpMAOOZ9PuF_CXKKgGhLedMTESp1OgSETfXmL11FGbgIjkyK5xOKI9Sr9ip9GPz32ufzpB2ny2brrBSd6Dmp3hMcg6Cs_Qk2C3EYuAKSvyOakeZFzwJiudkSBFbTvGPJoxELR7e_ELKsB4MH9E1uu6FaofDKLcr-xjX1ic839OPhWjyNr1yugwrc52wKYfgNh4WoTRuz_W2_VZBw9Oq2Zat5Ez-NDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
هایلایتی‌ازآخرین‌بازی لیونل مسی فوق ستاره تاریخ برای تیم‌ملی‌آرژانتین که بایک گل و دو پاس گل همراه شد. دقیقه 10 مسابقه متوقف شد هواداران لئو مسی روتشویق‌کردند مجریان شبکه ورزش فکر کردند لئو تعویض شده. ببینید خودتون عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31121" target="_blank">📅 09:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31120">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">📹
گل‌های‌دیدنی دو دیدارمهم و مهیج امشب رقابت های هفته چهارم لیگ ملت‌های اروپا 2026.27
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/31120" target="_blank">📅 09:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31119">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbwD2taQa32Y3zgra8tf0jQ27hwTgOTM_-SpAPxQ2ZMXxKRux7w8ChBHOYmeoPBsH3uCnxccjBmf6Yzk2gQlXNXToI7B7GlOQhOGlKBO7VtsWpM_k4UchyLEgWSc7krkJE4eKwHlo3zey0MpwczumSIO1C5L-sb73NOjrE95Jw4UwXD_F9XNtv-VVOlZfNEk_6-iDDfsWbmIIiqyo1SVtjC8YR1Gmx24v-3HYMoAX8FKQbGqt_SQp8K44c_qC1RD8fx_kTl-bcW6KoeRbETopyTO87g37O6zvxHQ3P8iGM6PGPrj8THDmw_m5OV_r-D7R5YN38SORCC1xT-jppU8eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ شب خداحافظی لیونل مسی افسانه‌ای با لباس تیم آرژانتین و فوتبال ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31119" target="_blank">📅 01:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31118">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxxVHOu8mKjo-0clT0mJEkJueWfXbnmM4MN7vwObil1-zKZ-hgTxwzfK4wd7SfLqVi0vi7xcCzN47BzoNmmYXY5Mm1r3-MEJgec-2f9daPtF4UU8yRy8CQLmBU0ZdwWCoad_KnHoKqDe38yMxoNSthggfPNdocPVyOif07VHSdah1aOlMNAUC08gU7GxGTsKepiWgHo053ZMhByXTM7YP08-CQfr7NZ49AgbSC7oqNolACzsKPc5GgQFGEGFkQhZ9ckk6kmZpUsH4LCj1t6O_xvp82HZacYQBX6ykFweXqQ4oSQi6RVsymmXIWVPzBFqgAZDC6CpjihcqAY7jhTdaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌‌دیروز؛
کامبک‌اسپانیا به کرواسی با دبل میکل مرینو و برد سه‌گله سه‌شیرها برابر چک
🟠
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31118" target="_blank">📅 01:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31117">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
هفته چهارم لیگ ملت‌های اروپا؛ پیروزی ارزش مند لاروخا مقابل یاران لوکامودریچ باطعم کامبک و پیروزی قاطعانه سه شیرها با درخشش هری کین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31117" target="_blank">📅 00:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31116">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQmMZrQdcX-c1j-tY_3PVa731Mi6PdVi5pdGked7KmlPX5C5sqCP_Q9pdyJ7JTRWnqDRir2B6MzuVQrrrM6uwGYsbU8dercscDZ2c3KHlB7onJYLyEGHduSs9gBj-v3gguWykY4i5Yt1B7Oxl9GbUS1AdHcSXf6n3I6ldXzLYNJi2a6eYfZ3EeQIQekv8kGTAzN6dfOnK-hRLRijWUaLfhmKfXhLIiRO0vTl2voU8hxaLMs5tlx1vKbC8evixq6s92MiuUOpw77k1WdhjMJQ7__AM3S7iUfKuf98UBnULGOqxC1qKNZaAmx7BApr8iGEF2m944nJpvZfobY8QcA2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز؛ جدال خانگی کروات‌ها با اسپانیای دلافوئنته پس از تحقیر مقابل انگلیس   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31116" target="_blank">📅 00:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31115">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZJ9mf20_ECHShiaBNXsUZQhSMH6zxc3H51dj0FeEa96WVpZeWMeTAJgOIIXautoM6XJJherf8WrJ_p3P8tGsJL_CddTyejhP4tx8zrR1s681hFW8wEvbaDW3LgHfajVdtCCoTfEzDjHjvBaAdkA_xdAhGrCAm7qF89r6u6fbKhikhhHDi0cdORISoMyZdd22by0UL_SICIjXMgZi6UqO2dX5deuwuZ91ill6RHbY3xas4KreC3T8XLDh44k7k8lqJG-Lo8fA_Gjhp3q93WcyH4yoc9Ll-zFVq5f-UQiJ7XIpiDvr8IgBIcT-A6gv1Z6TOk4WjrwXabR5R1l70BInA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه العربی امارات: رضا غندی پور و مهدی قایدی دو ستاره جوان ایرانی شباب الاهلی و النصر از شرایط خود در تیم‌هاشون راضی نیستند و به فکر جدایی از تیم‌هاشون در نیم فصل هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31115" target="_blank">📅 00:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31114">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXub57jPAxNIh4vM_Kp3EOULxrt2NqS0Ep6vidQAWsSgojqAYRcn2CqWQZ5lLkzs4lmwozGmJrGT8Y9mldDAP4yXz8PQGhZVYrUEKpLZsbquOOtpxPox2JrFf8-VacFC8oKBxb1LzMgf7oljwBDP5ayxwGnlcUkhh0V1Zg440ulfbcDylyKV82Cxx4_yJdVkXolRxkaKGGCEZn0l40JCmopLunGmq64r7i3rTQk2GUmvdldGc2M7NYfyQXswemJxpKYBbdSGlhEdYyuz77ARgGpweW9xPtzZ6GmDReWUoeb94ySDmPKpdwfx3Y4-vCfwLkilHJbCOBOHuZpStX40yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته هشتم رقابت‌‌های لیگ برتر بعدِ تعطیلی چندهفته‌ای‌وحوصله سربر این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31114" target="_blank">📅 23:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31112">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNinz13DLgJXJ4I5KGbcOaaOdM-5JxZchVq9cd4Uwt1y9K58T2zE3TQjFt3FfNLPCGv1UZSmgSbfdxHn2cs5OrDyKt8Bx935pryrTaobemwGloH2lXYWmNJQeLYn63Sd-4VYgHVqifSDSVmYbJ2vzvipVA1U2KMxiobwkGbAIaASKwtJ0ohgNzBx5Ly_vqToqS4JfP7DWTI_bv_TXdKIzDzlDt5RpG-nqrz9_KnKyWsmfDdw5LrMEdGi9CgYhUkwAZBaoA51rFDuminVJG53sUZ1Fssx_7vNoPGQd106hhTfZqC_rpSZex0n6nDBwrQBqne2VUEwSyPaFMWTw7e_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ATYKkAar5JWxKGIC-MAoqPNoMTm7B0AIiJ2zj_GHxdWY-hvep4qshgknjnNeCeTckIqZog0pkhVgsCushb2-WhOqwmO-rNVTHrLj6JXml3l9Q9BbL4fBDGPCUBh427iV_kZqEOHzbbeqePNQA7IrIrlWcXWBiopmNo0BQtwaEeBXsu8-Q3ZQ6sNoQ0bMQLadcwBqz5UiteeKdB_A-55hinxz_DKpTpCznOIwpcc1UNC5P2d5ZwDFyKxDxaJeYh1Gsl8SnHqVpM7Ls59I5C94NR8pG-O-T8WYh3wtDiMno2SFVBS6xkt71ibEyR86aT1UVgFI3XLCeAaZQJ-U4OeQPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
در آستانه چند ساعت تا آخرین بازی لیونل مسی برای تیم ملی آرژانتین؛ دانشگاه بوینس آیرس دکترای افتخاری خود را به مسی اعطا کرد که بالاترین نشان افتخاری این دانشگاه محسوب می‌شه! دکتر مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31112" target="_blank">📅 23:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31111">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh-JBjz1kF2K_H6QJI21QbDyx4YiV79t7LNBqC8q8bqRbKR69YOMeJ-UGkF3XaqojZU-dd-ObiDjlpSpOEtwlbuS02sGoL1XRZEs-0rP2hyGZ-em5pTt3ZuOXPkb2Lnv1IEMK1fSo3bPdiVUifW3bKzX5PGyDH0A86pQ-RoCz2PptL6OIkFnPJJFtwB4gceGA3Sg-9eNApSMfVV_EbeYSVCOJWYvMZW5mob2ivHYXvzi4be-8gQU3MoixM5ki3vpx4mblttipkjP8RaWq8LBQR6jwwiDlj8ekTBa57kktiK6zIR47mBH7SbDpTZY8ej7tDEN3G4lY79IpGL1RyUkmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال
🆚
مایکل اولیسه از ابتدای‌فصل2025/26 تا به امروز در تمام مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/31111" target="_blank">📅 22:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31110">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT3IE9h9WiOSMNOwf6K9hCGT_8-riaCx3585COeinHcvhEYTGETwoWeSCoErSEx_4_Sp4WXwBvy_YqqAa3eCQAzF2lgvV_sF1JJI9ZzHOm-6DTtf-DG9y7V1YdyWLugD0i2cfdyCk_nXZ_JGx8YL1JeougMRyS6yn7LJ986XFNNSRkA8Wlkr0cUpRkeJxON6ch13c1DwsHd8tjN30YnY5kJ6nAuNK69HCB1AfNFZG_tUdgmLZ0soFKQXeweQ4Weg7iCoNJfbpD8WXs5U4o-3JxkSJhGwfcNCwe08wsao6bUc5PbSGdV3fSyoUxEnHKU1tejMFw6Xg0NunaLmFvFYPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو: به هوادارانم قول میدم در آینده چند بازی مهم یا یک بازی خداحافظی با پیراهن تیم ملی فوتبال پرتغال انجام خواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31110" target="_blank">📅 22:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31109">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-s83d7QJH0sHPy1C8bStC4RlBaS08JTb1CROoLLdHLrrNztZTR7vn0Y5iJXJhkXxhXCVlcxxEACUI41vyhXjdymvOg_RIoM5etI1DcAfkILrgEFdHmgtQMvy7S3--xbdhmxHUyoa7KGETnG8-qvqu7rQY9XDV1hIj0yJrEMgQKrmtsI4HQ-b3rFmy7cO3I3Eo_53Y7JlX0AV1eXEMvrwmedBZBg3ZEoRtJQ5jt9ImtVdxjWAiUZrfbfNoCLyOUup0HEYKsnQ5k4t0-JqWZzxwWGwWQ0r7UoRhzpNQyZLdnHdN91TqPllHDvR3fwbxcYigPpN9ZkCFN59UtkOsUr0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
آب پاک کریس رونالدو روی دست فدراسیون فوتبال پرتغال و خورخه ژسوس: تا زمانی که این آقا سرمربی تیم ملی باشه هرگز به پرتغال برنمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/31109" target="_blank">📅 22:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31108">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuL5FvJyVoNDP7kGlwmSVTt2XZlWB1QzFrbKo9-TemUdDbf-CnjXjIwfRIClpoeViLnJaR-5r5RuioRrSPh4gkh_gW_usAo1txf8TchWB2vgGSsjvSnNVERA5_MUaMaQ-tXbJ6qEqkE8oW66hDYx-XQNVrXXYe1Gt6ZEtpEpwzda7VgZxU4fyrVjcUloI0m0Yefs0A2_ZjSLxLhvPPRXXAwIIY4MC93DjwHMV_rBAwMe6LofUhQroURro_ka8rTEppoMtwnuQpP2SSWEKQEaA9O4qaKHwgG6H4X0Moe7Z6xq-8RvvP7_PSEh6eSeTL1kzg_DQKio-p9hb-q4QXRCkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
وضعیت پشم ریزون خیابون‌های آرژانتین رو ببینید که مردم‌دارن‌میرن‌سمت ورزشگاه برای تماشای بازی خدافظی لیونل مسی با پیراهن آلبی سلسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/31108" target="_blank">📅 21:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31107">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FT8khj4q7cGwaRbKuNstexSD1STlq9Z-eKE0_72mxm8SC2qcPW0xF33n2vkITHX_Uj5kgTTXHRnQu6gKF75lcBZHlUBiavoiIk3-UlRH6ox241v2U1Wx8neB1-OL1n1ypXcQd_ro6yC3BOX2s0drhw1aMgJmJUbRtMyxJNJKn6F7gPgwR5rjEcbEDZtNZvbPQIumqRY-KziWgLM3fEjLKOfXm13z2r7qLkIvkGH1QFkebtJPfAvomP8eK-q881l6CdFbBadqUf7W1yP3wyK0_d63qGa3578kagxZQFxXrFQ2-5hUGIsg5h9_G3m1cD-WlCcz4zwaju76tQ06QVt21g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وقتی بارسلونا رونالدینیو را به خدمت گرفت، این باشگاه چهارسال بدون‌قهرمانی در لالیگا، پنج سال بدون قهرمانی درکوپا دل‌ری، هفت‌سال بدون قهرمانی در سوپرکاپ اسپانیا و یازده‌ سال‌ هم بدون قهرمانی در رقابت‌های لیگ قهرمانان اروپا سپری کرد.
‼️
باورودستاره برزیلی همه چی تغییر کرد. جادوگر درسه فصل‌اول خود، دوقهرمانی لالیگا، دو سوپرکاپ اسپانیا و یک UCL را برای هواداران به ارمغان اورد. یکی‌از بزرگترین‌ بازیکنان تاریخ تیم بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31107" target="_blank">📅 21:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31106">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a77e7bd5.mp4?token=d71otoGmrw7dpHorrNdDFDu6zsTF_4t9a6lYP-MnD1SZNE5gNH5qkSv3WFAgLZ7WjBwMv_41YHmDZomcP00UNLFSshgf7Qg_4vmZJwdMPJLSoLBueLiHhR9TBc4j5TMmQEzOub38Nen82Kpf0eHTZrQd_vxd7nubZ4M_Zj_KkyiWQXiI8w-FHgzUEcDc9Ema1hz3EIST5GaxBfvwXyyncPmegXsi5dGMT7Z2-nsvkOAM2J9ptSRDIDglgnXICtCEzF4PM3Q_vpei5dBNGohprOnrK_4KWTtjyIf8VRqPuHcxzuGd8nNt5UGNuBVk47By_J8oneFFr_tbz6NaDwIPAQ9vX1fmQlxJP3uhKF08UzRhfazdTbJz_4L9K_A5VrYsG8f9-Jm7jXQ1acw-7DX6o-qOzoOvpjmMV64HVd7WltJ5TsE0IwwGcuBjl3cbkIDUCK083BcEtXdcSzLKWxgdJ9ezvFLRSr-NyJw6b08dY34cBvsPD4mfp0AVPRukJ97FsNWajKdG5DpaU1Nqt5wEk6zz35FIFeszalnucwR2KeabcAeA0FtqkfkrWSDeJbE2MEHhEP52NzgdfL8_dHZ_Ox7NFdE3RwqFGpThvrXlWYR6XuPgihF898l1lS9uJgye_OyZ49KMNFWcnpVrDhDWF3yA5zoqAvzNMDv0K4J01ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a77e7bd5.mp4?token=d71otoGmrw7dpHorrNdDFDu6zsTF_4t9a6lYP-MnD1SZNE5gNH5qkSv3WFAgLZ7WjBwMv_41YHmDZomcP00UNLFSshgf7Qg_4vmZJwdMPJLSoLBueLiHhR9TBc4j5TMmQEzOub38Nen82Kpf0eHTZrQd_vxd7nubZ4M_Zj_KkyiWQXiI8w-FHgzUEcDc9Ema1hz3EIST5GaxBfvwXyyncPmegXsi5dGMT7Z2-nsvkOAM2J9ptSRDIDglgnXICtCEzF4PM3Q_vpei5dBNGohprOnrK_4KWTtjyIf8VRqPuHcxzuGd8nNt5UGNuBVk47By_J8oneFFr_tbz6NaDwIPAQ9vX1fmQlxJP3uhKF08UzRhfazdTbJz_4L9K_A5VrYsG8f9-Jm7jXQ1acw-7DX6o-qOzoOvpjmMV64HVd7WltJ5TsE0IwwGcuBjl3cbkIDUCK083BcEtXdcSzLKWxgdJ9ezvFLRSr-NyJw6b08dY34cBvsPD4mfp0AVPRukJ97FsNWajKdG5DpaU1Nqt5wEk6zz35FIFeszalnucwR2KeabcAeA0FtqkfkrWSDeJbE2MEHhEP52NzgdfL8_dHZ_Ox7NFdE3RwqFGpThvrXlWYR6XuPgihF898l1lS9uJgye_OyZ49KMNFWcnpVrDhDWF3yA5zoqAvzNMDv0K4J01ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رودریگو دی‌پائول ستاره‌آرژانتین: هر جور شده به مراسم خداحافظی مسی میرم و از دستش نمیدم. اگه زنم بگه یا من یا مسی!!! من مسی انتخاب میکنم و اگه بخواد بره خونه باباش‌هم مشکلی ندارم. من با مسی رفیقم و کلی خاطره باهم تو تیم ملی داریم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/31106" target="_blank">📅 21:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31105">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q67RdQbe0OcCLP5jA47Jktxfj8T2iNJVzHw5QEk0GuYjDh41t8tbCvSrwy8yU0aPxpDjQyeYEyBQyhJ8-UfXaBhpWyzy7esro1VXjHrK6WH92GBBtOLmcjuVqS4Oa3BuadCkKmJezk_LxLi2WkYfF6I06_Psv8gLTLYsGorp0mZvJR6A3jdKxXqm8DHV6rs1dQKS_uIhxbnQEHbJ7E6jK2u-LE6cVH71_GS3c76SIARAgmcb4SsjBz2pbJ7loy_Dkt8HmzZPEq0EbCtmhAh956dERYZY_S4zc1uzkKKUaOy4MP5Og7jsh56fVraJb9AK8vPpEBdWjdBAZ3KYcMFVPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مصدومیت حبیب فرعباسی دروازه‌بان تیم استقلال کامل برطرف شده و او هییچ مشکلی برای دیدار با تراکتور نخواهد داشت و با صلاحدید کادرفنی این تیم میتونه برای آبی‌پوشان‌پایتخت به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31105" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31104">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmnL_BI-awjBsM8xFJh8dr4NklvkSSKnOHERy_rf2zmPhoEosTkhlnSiTbaw2ffii5p_9kMrBPenOar2S4PAlKEUo17kvqnxkMaP0mjLBGnDng2x9TaTwDGi44VUoj-iSQ5SFckkzq1IT6tCV_B7-wftOygS4Cr9SnsL1bbwkPopfwW-FF51TqfLdy5tn05jzPBwSNekgnPEcMkeENk8etjqxwzdKWAlwh8VAS6tz6jmPJ3VZ1EydN5KSgoMfE_In2-gyXR8sLDEw_IF1PjXl30rhZXEb3wk7ualyjIlaCj207Oly1RY29soPoueOATmQGxiwBgX8Td4wOCn57zWVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش کریس رونالدو به صحبت‌های ژسوس که گفته از او عذر خواهی نمیکنم اما در فیفادی بعدی به تیم ملی پرتغالی دعوتش میکنم؛ رونالدو: حتما میام!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31104" target="_blank">📅 20:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31103">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGksyqKcEhVDgIdXW5x0rr2aF7b1tuP_PeUC6ZV-rRvHaxxB7xoaSKjy1-TKL93oY_n3YQBGdXnRXwnIS9tg9AjwykCJqM_yD-05fcVyiG0bS50KxT7mBqFkQvoQ-7tyd8UHnyFJ_S34-i067vONvhb8B87qEoqhshsdqGmDV6RCkX6APyKOyFhD-PgQsJ7sKiFyUas_XVOZS1-Jp8dIs5w5wZkXIZodKLSbdQ9TrTPsuX4Lfcd9YVsyR-zbSGB_iNBRxi_ityw46PTvESX4SC7RM1NRHi9eN5mGbyuYkx5Ej6m245knPIYWzND7Uqxp_TZ-7ZHekRA85o02SHQiNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی باشگاه پرسپولیس؛ حسین کنعانی‌زادگان و دانیال ایری به دلیل مصدومیت دیدار روز جمعه مقابل صنعت نفت آبادان رو از دست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31103" target="_blank">📅 20:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31102">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKQjeAt74K17V9f06oiMT39hb9infPm77PyElQ2lorS7yFoGSKv3i_P4Wh4dWBmeCyf8H63mV0J_Ha-zAf6SOJJdheiYwcWq0qrPTo5In9BWRkavnLw8nQ3XZzwhXW9Ur1tD058yQN8sGLkbikUtmb73y-Ssbb3ONYSS7e3n_aCwK-IsCX6FlMYeZVFH5j0Te8Tk4cUk0iKqZU4op1D5zEGLdZPIYE4bGHUXv8o-CzYPxV9Gd15_-BgapMjgwBVF85WyDlcb5pevuUvguUhoh40FeTfIo0pA5UdWQx0ehq_bJSEIXAd_LAqF0cMzM0F7fyk6e2rXnRmgmvWuB5Zp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جود بلینگهام ستاره تیم‌ملی انگلیس که این هفته یک گل و سه پاس‌گل به ثبت‌رساند و نمره فوق العاده 9.8 از سایت فوتموب گرفت به عنوان بهترین بازیکن هفته سوم لیگ ملت‌های اروپا 2027 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31102" target="_blank">📅 20:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31100">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQfXNs1ljAf77JdQHRY_KZSV_wKN7YNoAKQ2OeJLqAerlj873VPytK3t1kykFSrPmXenUNPlhNA8xwAkhnz6CHOGxClOcRJyUk5ig174QBoAO1RCbjYkT38RpvHiTPjZ8t3aKobrxIJAaEcg0kCA8I3e_oxbYDCiC8I75PoI0nUbm5PamdAljbRQw_G193NsPdJweg58swg1kZRxrHYZX7E1vK7XZdb9yj3NNVe0ffwwJfIy85LTQFlNoLFtAZTKJuBUO7HneSWyvjyJlB4BjKCzbC9NJFPyLYQ2sCRRnN6IqDw0e1jLnarAR6vY53wEmDa7GMlHUX2v3uCiarkYYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛ یه‌خانم باتیمای‌بزرگ فوتبال ایران قرارداد میبسته و ازشون پول‌می‌گرفته و در ازاش با داورا سکس میکرده تانتیجه‌رو به نفعشون‌بگیره. بعد از دستگیری این خانم اعتراف کرده که با بیش از 40 داور سکس داشته و باعث صعود خیلی از تیما شده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31100" target="_blank">📅 19:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31099">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-1ZOcqg-GDv7nzmKk-GOIBEWKOYE0rV1go6jkgf5S9bhlIzE8nk_0RsMZyXsbjKYn9kheeyFzDq9mg_4WpdkhXUdFVv9-tWhXCDe4Mlxb2rBld61Abz2J4eglQ_c5XUNFACIlfuIxbCcyiYDegEnRtucFDnVUTpIH0zYxPr58pfj4EuJcbX8Mhs--mrnWWNbiTBfGSyhjZ8WCJrMZqq0BtowYxdw0GftlTYODvxoIxhpa94CEZ6KiPPgVyeqzigdMd4NpV2udyhScVPtLxSvaZXzmukuzvGStJu2_0SoD4en18el6pYVqQUjw9JYpg0CDoM6HIqeDwqckDWje6PTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
فدراسیون‌فوتبال آرژانتین قصد داشت که بعداز خدافظی لیونل مسی شماره 10 این‌تیم رو برای همیشه بایگانی کنه اماقوانین فیفا اجازه خالی موندن این شماره درمسابقات رسمی مثل جام جهانی یا کوپا آمریکا رو نمیده و باید حتما به یه بازیکن تعلق بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/31099" target="_blank">📅 19:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31098">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7UEO5UEWsOtuPIizNPIx9TUz-cng0ChEPrKIjGmAz3UvrHKSHybfsRmRO67vYB7VLPoSVfdT1Gexi4kqQNZ0BgNosJRXZxu1N0X2P1W5rqCjlS5m_gWZAL1o-sJ2dwGIt9Zb7sdm86N2FYqukdd7ob4Zvb60Ce0IhfxtaH74aUn7YREYQ-F0t4FQZGJkvMGJ6DUPQADOKfDaitU42wEJUo2AVzNxULf-Qcvuol3CIupsfdn_SEK9SdlySujTlouX9asmbw8iinJ6FEEe_0uhLws1i2tMDXKRJbBjTqIy19Kb2M_zEqIJ2bw2ueCTbnPXIbHX3zVgLtq7y9OcQEd6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
فابریزیو رومانو: دنی‌ کارواخال مدافع راست 33 ساله سابق‌تیم‌رئال‌مادریدآمادگی خود را برای عقد قرار داد باباشگاه آث میلان با کمترین دستمزد "سالانه یک‌میلیون دلار" اعلام کرده و درصورت‌موافقت روبن آموریم کارواخال به جمع روسونری خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31098" target="_blank">📅 18:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31097">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERSruTK71UKENZG0ac6pXB1MFIxXk_vMkGLFh6ZHYa1uV4ZfdJdFL9wkjaoTnRo3qU3C3tjV8ESRjdrVhTRBNPKrmHo0Kia_2NVVXDZrwXsO45R6KeToF-p4G3qDwzXiN3qTolPhX4uEtl_7l1oFi-DFfOKMw-u6okRQ81iiVg6amXZJEdPmJjJ-iAuZxIcgcowMtRcZpmTaSbEIC1uBw3tkOpBEFifOVAxf0qZFroxTBSQePipA-Zkd_Y_6LMRo8VqJ6C-Xb3Uub_kiD6rGLSBo5Kr8oEkXGHgkPkMzow3MV--RxBOrQbAKcKhNvE4FZADmBykrlfiaxTC_9E-bfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
امشب فقط یک بازی دوستانه نیست؛ امشب قراره که برای آخرین بار لئو مسی با پیراهن آرژانتین وارد زمین بشه؛ پیراهنی که باهاش قهرمان جهان شد، اشک ریخت شکست خورد و در نهایت به بزرگ‌ترین‌آرزوی‌فوتبالیش رسید. بازیکنان بنین گفتن امشب فقط میخوام از حضور کنارمسی لذت…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31097" target="_blank">📅 18:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31096">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12aaf08506.mp4?token=PwANFodblS_GL5bPYxSGCZBwCxeULBPdgqPdpWgPnHcoHRzv1Z_syzB1nGW00of1Jw8uXoST36PdI1OS0s0zzAi2Zkv-mVBBHyjCdb5jeQj5ATD6zXUJn91eLO3A4fE_R4ePxbcUII0dRDjzVW9QbSXPuRXUfP9tGgFLOn5IvFkXTF7HkOD9UQpkBqPMO5_L4q31ytaeBlHOI_o84vocvRwb_tvAm75dZJZ5R4uvSkKgJnzos0Go0OKooplazgEXG-fohl1fZqx1WJg-63VWApqV9x86vajZ89YYwWP5G46rSSbqeeoYb6rzsfYi5v4lVrvrzkf6RTH4T02kUgXQ1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12aaf08506.mp4?token=PwANFodblS_GL5bPYxSGCZBwCxeULBPdgqPdpWgPnHcoHRzv1Z_syzB1nGW00of1Jw8uXoST36PdI1OS0s0zzAi2Zkv-mVBBHyjCdb5jeQj5ATD6zXUJn91eLO3A4fE_R4ePxbcUII0dRDjzVW9QbSXPuRXUfP9tGgFLOn5IvFkXTF7HkOD9UQpkBqPMO5_L4q31ytaeBlHOI_o84vocvRwb_tvAm75dZJZ5R4uvSkKgJnzos0Go0OKooplazgEXG-fohl1fZqx1WJg-63VWApqV9x86vajZ89YYwWP5G46rSSbqeeoYb6rzsfYi5v4lVrvrzkf6RTH4T02kUgXQ1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ شاهکار زین الدین زیدان در بازی دیشب؛ فرانسه درحالی یک هیج عقب بود زیدان در ابتدای نیمه دوم مسابقه 4 تعویض انجام داد همون بازیکنان کار رو برای فرانسه در آوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31096" target="_blank">📅 18:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31095">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd044daffb.mp4?token=u2BTj3KdAWcyu3GA3XrXOr3hcoNKeS0t5lYF4e_jSp5r3GLRrAhVWjV42qhBh56qsjR-uR-lUZwbibwXXtF-iuKnEwGDckO-dpJ0AFxH1Gfa18W-Txd-sm9CMCM5vpPvXxis8Zg2bKOZgqCvyR6YrLtOyxdojPIpDg2ENhgkY1r8aY4e08_QAVsk2ACbn4nfEAJ1AzT3ppQypa3YJmG_RVwc4XCYd9nDd9F6UmiKpZ0eSXx_6xK3O6Q_lzSa1rmeX5dRtfVNzuFaC7l3ZxOFcxUgTiiUb6QVrP3Y-cURcD5Q6wOo2tC06NDg6uhMnyjJ_ocj0bMYemKkFp7g1rTTMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd044daffb.mp4?token=u2BTj3KdAWcyu3GA3XrXOr3hcoNKeS0t5lYF4e_jSp5r3GLRrAhVWjV42qhBh56qsjR-uR-lUZwbibwXXtF-iuKnEwGDckO-dpJ0AFxH1Gfa18W-Txd-sm9CMCM5vpPvXxis8Zg2bKOZgqCvyR6YrLtOyxdojPIpDg2ENhgkY1r8aY4e08_QAVsk2ACbn4nfEAJ1AzT3ppQypa3YJmG_RVwc4XCYd9nDd9F6UmiKpZ0eSXx_6xK3O6Q_lzSa1rmeX5dRtfVNzuFaC7l3ZxOFcxUgTiiUb6QVrP3Y-cURcD5Q6wOo2tC06NDg6uhMnyjJ_ocj0bMYemKkFp7g1rTTMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لئو مسی از سال 2005 تا 2026؛ تیم ملی آرژانتین راس ساعت 02:30 بامداد فردا در دیداری دوستانه به مصاف‌تیم‌ملی بنین خواهد رفت. دیداری که آخرین‌بازی لیونل‌مسی باپیراهن تیم ملی آرژانتین خواهد بود و این فوق‌ستاره آرژانتینی در پایان بازی برای همیشه از دنیای مسابقات…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31095" target="_blank">📅 17:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31094">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbRuEHLWt2cRBnslG2ds4kWS2qf-1YoJkampc0JK0zqXjNhmBgrWSo8d8H3pXwq8b6_dhfDIuhprGU9wJsY-_GyEpjrHQcBGqxGhmQ38aBWsQhf4X4xbhK0kMfz8tZRvy6rIQRRM7xN6gqgNdvyI0XaK3uqXZQbX3uGr2Xx32zD15Icig_R3Wws7A3wg69wB-9q1I6fy4wbv5Bz1pAvHNEhN2Dy3h5QTFjFTUiJyeOvnEtona5bjNSXLxFUXCdRSjN-DzpciMHls2-mv_VnKwHKqKj6EzqwoSKAGgpTEHZxs9XACWRBv3sbeki4sDC7lnY2OmJqcmczlKWfAl-KfTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ادعای نشریه فوت مرکاتو:
نیمار زمانیکه در الهلال بوده به سران این باشگاه گفته جزیره میخوام اونام درجابراش‌خریدن. درامدنیمار درالهلال به حدی بالا بوده که درامد سیزده روزش رو به خرید جزیره اختصاص داده‌. نیمار در تیم الهلال به ازای هر لمس توپ، حدود ۱.۱ میلیون یورو دریافت می‌کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/31094" target="_blank">📅 16:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31093">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1a596a3d.mp4?token=WxDMFch0WaloVa-EHyk7lZMuTMTzIWnP7d61qMgVOpiVYM6RnX7LoLieIV3lY_kyfdXLnSQrgFRL3JPM7lKyEX6MMRQ_FgYVSrGudbYPvIYU1mEU6XL1Cr0vdlmjDeMeOXdkpvYPukFLLbhT0qDUdy-m_ySvfUkSlcHI_PkV1bbuloHnExovVHkJR9GvuaEjFV2M3BmOsgbxiiEHz7Hb8KNM5ZS-IOvl2z-lf8h2SgHUqSHduqdiHLEzyDUysbMUH4aTKLrl0JiXFZEvw1Dbz_d6ogcRGzmjJmA-UmFKnjYbsPXQ4__bMci2NSrckmjiP3EK_dqpT2K7x8Jpkwfw0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1a596a3d.mp4?token=WxDMFch0WaloVa-EHyk7lZMuTMTzIWnP7d61qMgVOpiVYM6RnX7LoLieIV3lY_kyfdXLnSQrgFRL3JPM7lKyEX6MMRQ_FgYVSrGudbYPvIYU1mEU6XL1Cr0vdlmjDeMeOXdkpvYPukFLLbhT0qDUdy-m_ySvfUkSlcHI_PkV1bbuloHnExovVHkJR9GvuaEjFV2M3BmOsgbxiiEHz7Hb8KNM5ZS-IOvl2z-lf8h2SgHUqSHduqdiHLEzyDUysbMUH4aTKLrl0JiXFZEvw1Dbz_d6ogcRGzmjJmA-UmFKnjYbsPXQ4__bMci2NSrckmjiP3EK_dqpT2K7x8Jpkwfw0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیدواژه‌های تکراری امیر قلعه‌نویی در چهار سالی که سرمربی‌تیم‌ملی‌بود؛ همه‌ی همه مقصرند جز ژنرال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/31093" target="_blank">📅 16:17 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
