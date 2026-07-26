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
<img src="https://cdn4.telesco.pe/file/PYvkd-GTfp9RNpmKWmsuepLgvDaLAPwRDvz7YXofKsG_C-LMOf7PppC9eW_AR1JjDu1K_zN3hSYYsV9ZmGs0Yvd9t9vJtqDQ2kyyeehLKb3SxEHnC2DC1ZTBOhWV31OlZ2_VOJObeSwD7RND4WcFRmHN-6gImuHzvbII2IVMA4DCYaneKJmq-OCEsQ8rB9lZ77kIVRFKR3aBTMjCWrpe6RkuDQ9_D03xAY7anW1INRYqyVoWhQt-8sjCmR_XioTG0M8xRlyi6QyQhaxWppCN4PquuF7D9L3iiRnocQRSCwcc72X2cDpSFRp02KffArMwGsL_Si4hIyiD1LZatzbH-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 148K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 19:05:58</div>
<hr>

<div class="tg-post" id="msg-69019">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd02960948.mp4?token=RTbYuxlLCDmMEleV--o4CYoWhHtAJTMpxA8zR2b5U0Q8CZxmA9vLL2mhJQFE-SrJrMQ8aed_DmZpDxFeiVzV4FrtqAoKyv74n2NwJtx4Owg2yxHMXTwj_JmxqngP0X5l9eeVlGQl2ipywCAOWRS6rGOjmOWcL7Xpi0OoJRNqDNQaGe9c8J01QB-QGl42Mj8XKiUkJlU1D0Sk7zDaBZJfRdfCL1PjX-aq6IWLOMb5OEGvR8iIBU9DAZNVsL5KL_Hk9UQm8qeedY6OuqSci7M2WbQQj_MD3D-70bKY_CO7UKVxSVArmqRPGLv_KJa2Nc9xNXtszCkvnJMWubkluf4xRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd02960948.mp4?token=RTbYuxlLCDmMEleV--o4CYoWhHtAJTMpxA8zR2b5U0Q8CZxmA9vLL2mhJQFE-SrJrMQ8aed_DmZpDxFeiVzV4FrtqAoKyv74n2NwJtx4Owg2yxHMXTwj_JmxqngP0X5l9eeVlGQl2ipywCAOWRS6rGOjmOWcL7Xpi0OoJRNqDNQaGe9c8J01QB-QGl42Mj8XKiUkJlU1D0Sk7zDaBZJfRdfCL1PjX-aq6IWLOMb5OEGvR8iIBU9DAZNVsL5KL_Hk9UQm8qeedY6OuqSci7M2WbQQj_MD3D-70bKY_CO7UKVxSVArmqRPGLv_KJa2Nc9xNXtszCkvnJMWubkluf4xRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ویدئویی دست به دست شده با این مضمون که اگر فکر می‌کنید ترامپ واقعاً دنبال اینه مذاکره کنه با جمهوری اسلامی سخت در اشتباهید، این ویدئو رو ببینید تا متوجه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/news_hut/69019" target="_blank">📅 19:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69018">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=N70qWbOSlzoRyX8Bx7EdCaQvNZrgp_NudCwccpi4IC_qeQaW1oR6-PGjVruMftNUyweJ95s3dClptGn68oVSHwauOEXldrpzwR_YcDEilzfmn27PXz3YCKko5xJlCvAQG1iEhzp-dH6xajMANuaRSyvBnqeB8sOHcy7sgHXYxZ6m-ObZwRHhMRWfw7UoOEjSntZ9PolKkBfApFVE849zcgERDctq0oiBcZJe2cIMxQH5462YZlVCthigKTaXYuE8_BIWjW1ySOaUcre_9lxk6NSR6tIm7GOQE6nOxRZjX1F7dzJTJgQ0qfosOPCFIjNaBD53ZH8lyAocnXLNZwxhog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=N70qWbOSlzoRyX8Bx7EdCaQvNZrgp_NudCwccpi4IC_qeQaW1oR6-PGjVruMftNUyweJ95s3dClptGn68oVSHwauOEXldrpzwR_YcDEilzfmn27PXz3YCKko5xJlCvAQG1iEhzp-dH6xajMANuaRSyvBnqeB8sOHcy7sgHXYxZ6m-ObZwRHhMRWfw7UoOEjSntZ9PolKkBfApFVE849zcgERDctq0oiBcZJe2cIMxQH5462YZlVCthigKTaXYuE8_BIWjW1ySOaUcre_9lxk6NSR6tIm7GOQE6nOxRZjX1F7dzJTJgQ0qfosOPCFIjNaBD53ZH8lyAocnXLNZwxhog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
مداح حکومتی خطاب به ترامپ:
"تو گوشِ کَرت اینو فرو کن، خارک‌و‌سه جزیره مال ایرانه"
@News_Hut</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/news_hut/69018" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69017">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hm0Jj9lN-z4W_ajLriiR0duhnv-GVsedoKabU3HUh_xVWPaaEiNHZP2pnE0E7Z5Wn1v3DBraNagsuc98T9koSw-IXT5uFD_DRDxkQUhUy_vj9eHNFLrxLfB6jd3yqeGTY8-fqSMdd17ra4PdyySddpgaC_FXXm2Yg71_58kdB6fhJJ4qEFwr0WYHs_NglLvAqRb1KM8jPhVlA4kE6kLQxlUKT328V5FsUBEoOZzLTNY_Wf0IjhoJ-pgVZkY2inqQu3K_0Q8wWFxOPx_RmaZWXEGW6s3BRk2mAtDZXJjbWd8yzrYyfmNd_Q22YXXnOUcQn0mv-j11SpdFBMAmhlkGzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
العربیه:
- ایران به پاکستان اطلاع داد که از مذاکرات خارج نشده، بلکه مشارکت خود در آنها را به حالت تعلیق درآورده است و تمایل خود را برای از سرگیری مذاکرات در دوحه، ژنو یا اسلام آباد ابراز کرد.
ایران به میانجیگران گفت که با ایجاد مسیر جدید در تنگه هرمز موافقت نخواهد کرد و به پاکستان تأکید کرد که باید طبق یادداشت تفاهم به مذاکرات بازگردد.
ایران خواستار آن است که مذاکرات ابتدا بر تنگه هرمز، سپس بر دارایی‌های مسدود شده و در نهایت بر مسئله هسته‌ای متمرکز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/69017" target="_blank">📅 17:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69016">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=BQ1Kl_QBWfL4UaDlToECrfqBqKIIzJbLsFgBe9NSieB1yFFBIIWVFy9ywWa5LSdknTDWi-PI6MPP-ADN8g38Qr1I_O90NEtKAW9EQNewHx7oT3iw2PpygbAcgZPpisb74Kw0NqGdUQ9Ngu2YRtYgJ2tFpOKTtuN9JkHsqPkDDn2ZP-medtUm0T5MIqfWwTVN2AwfqvID7ZqXFrqIK62CoAJM--bYx68MermWiVayfjAgx1tOyNMZb4x7aSqofA6QWsAFRFFuX3n5vCDRiA4t9vHjN8w6CF8_q5v7qRLVbxqEuWgaVJlJHRJriHul5DGMJWX28LF-coPQ_smNW87T9YE2QcWpyPkOufrymRIxsHLHEcv95wDFi4lkXj13cR0w6SFsbBSXeIGHtI1rRIa8KVEZDhC4VGalJUrPiD34Z5NGFgg4U5cp_byFaJMoADdFdJhQC9TQnyB77_738ZL9wRDuk4ahbVLqHB1-2-jF5cqMJzZbbd-eAhvnaNNtXNiWaOANZd4hiclRUHi1z4ZIfXVQouxwJ5F4S7CuYuIrlREb383iNQntAiMHFCWizpG6ZPevm2uyAxPj3OudlvpA0TmLNunx-GcLhoe1Nw_xce8KDLVAckK_L30FhTcoL9IBN1EpqfsKu4OROWI73ArjMr3Sg5QjFEbbVEgz_dQ-RbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=BQ1Kl_QBWfL4UaDlToECrfqBqKIIzJbLsFgBe9NSieB1yFFBIIWVFy9ywWa5LSdknTDWi-PI6MPP-ADN8g38Qr1I_O90NEtKAW9EQNewHx7oT3iw2PpygbAcgZPpisb74Kw0NqGdUQ9Ngu2YRtYgJ2tFpOKTtuN9JkHsqPkDDn2ZP-medtUm0T5MIqfWwTVN2AwfqvID7ZqXFrqIK62CoAJM--bYx68MermWiVayfjAgx1tOyNMZb4x7aSqofA6QWsAFRFFuX3n5vCDRiA4t9vHjN8w6CF8_q5v7qRLVbxqEuWgaVJlJHRJriHul5DGMJWX28LF-coPQ_smNW87T9YE2QcWpyPkOufrymRIxsHLHEcv95wDFi4lkXj13cR0w6SFsbBSXeIGHtI1rRIa8KVEZDhC4VGalJUrPiD34Z5NGFgg4U5cp_byFaJMoADdFdJhQC9TQnyB77_738ZL9wRDuk4ahbVLqHB1-2-jF5cqMJzZbbd-eAhvnaNNtXNiWaOANZd4hiclRUHi1z4ZIfXVQouxwJ5F4S7CuYuIrlREb383iNQntAiMHFCWizpG6ZPevm2uyAxPj3OudlvpA0TmLNunx-GcLhoe1Nw_xce8KDLVAckK_L30FhTcoL9IBN1EpqfsKu4OROWI73ArjMr3Sg5QjFEbbVEgz_dQ-RbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا از انواع بمب سنگرشکن و هسته ای اگاه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/69016" target="_blank">📅 17:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69014">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=eCeyXEAS90Ms4bWk3r3oXJqZ-geH2lnQq1q9eYt8Cv6prDnTVR9N05lABubjnqTmZd2c3MBqYru2Yz9HiILcp-qZxeRhf2DddfodKWfRhhgIEVWGfxeHUxJWKQJqw5Q867b50IkfS9oMYzzA_lTshzpyaMjxY3zZFAUNZyoYVfPYJgykUwGvg3Pj5HgfZk6JGDqglVDBP2AhcFwAti_cBYYsS3c1OHvMLPdhNDRonAkHqsTbLlmcpvm5Py75mLG-hcdDEsDpUFxEXZLl3gsjNTkw2RbffeLB1UCjl2CSxFXBG183KOYMgvkZZ64Z0tNBNxR99ozHss3K3BsOvk5BjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=eCeyXEAS90Ms4bWk3r3oXJqZ-geH2lnQq1q9eYt8Cv6prDnTVR9N05lABubjnqTmZd2c3MBqYru2Yz9HiILcp-qZxeRhf2DddfodKWfRhhgIEVWGfxeHUxJWKQJqw5Q867b50IkfS9oMYzzA_lTshzpyaMjxY3zZFAUNZyoYVfPYJgykUwGvg3Pj5HgfZk6JGDqglVDBP2AhcFwAti_cBYYsS3c1OHvMLPdhNDRonAkHqsTbLlmcpvm5Py75mLG-hcdDEsDpUFxEXZLl3gsjNTkw2RbffeLB1UCjl2CSxFXBG183KOYMgvkZZ64Z0tNBNxR99ozHss3K3BsOvk5BjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👑
شیوه برخورد با آخوندها در زمان رضاشاه از زبان خمینی.
رضاشاه، روحت‌شاد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/69014" target="_blank">📅 16:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69013">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g75wtzPZw2SblXu6oXv5BZ6InUgOfJGiJNDS6VdHetuZLJ77wDSsl7o_Q20Kk2v4W4U6ri0uz2DrjIBinIkSc3s3Ik-Vd9TqKtwMcYNL3Epxj6dhCKz2Ugmjot4AA_9G9360td4-p1TFkLN27Bj0JLgmTxb-gzuahMSos42sSYWuL7NeFwp7CxexRid0KLmW0QrSxXka4tfSMmxkregjXJssT1N2CwPw-gWjm6dlUHqfG8DA4vrtEpOETP5upkUbokYxGH4f88BjeK2Mb8ekMwYkaz_mhl68CfeJChCOtIeytOtriJAaR-ZuY76eRTu2aNIzk3FoOnkWr7X1Vxg3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
العربیه:
آمریکا و ایران به پیشنهاد مشترک پاکستان و قطر برای ازسرگیری مذاکرات، پاسخ داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/69013" target="_blank">📅 15:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69012">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH-NTtkv-Up4LkjTEf8KPckOUWDbxnriyLA65RRPt518bla9DVh14li0S9MDzsQER3PcDHiPudoI6M4KoZM2dVGSesa3Z8ETS24l_waza2LiJR2m9jBeENORsPlnQAbCSk2jvygpAbbH8cG0R5m9NYdJ8m4G2jOr6I3Jna1M-s2eGNhXr4Ewz2sl8k3-CWn3gR792ZZk6IjakKo4j_uNu3t4Si0IPQyIDxw1_IsnCoCGrNgbO3Z1BqftXM48FenACPR7_p5QcwBnNno2FCtHncE98frk6EkT2mdOKgV4u-V0Xf_YC7V20_Cr4s7f0GzrpSYQWkn_obU2JpqxbS8PZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امجد‌طاها روزنامه‌نگار عرب:
ترامپ حملات علیه رژیم جمهوری اسلامی را نه به دلیل مذاکرات، بلکه ظاهراً برای انتظار جهت برگزاری جلسه رهبران اسرائیل و دریافت آخرین تحولات از سوی آن‌ها، به تعویق انداخت.
این وقفه بیشتر به خریدن زمان شباهت دارد تا تغییر مسیر؛
تأخیر به معنای توقف نیست و آخر هفتهٔ پیشِ رو می‌تواند سرنوشت‌ساز باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69012" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69011">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=NbvSKvRjnN_HwY-a8jtZWyDeSfKANY9kv1huz5KGbphcfVLwFPxE_3BT2cwqowx7Eb0D4vgY9Xk_ArsMpQ4TbFMKvqviI5VaeaGOC0LNd80fi2Gl8AP_0cy_HpPuC5I-drxN1XKYHIBjbNAMBLxhLavwa22snLqaC_GnBZFRpVoMcxsKFP4kl9yKvJ-y-Ye98Nb0o3zA0iZtzkgm6LvKkSHZdoN0ats_RO4IYcgjtXq40UwTNWhLlttsl9ZCgohtUWnZkSNN_JoFmNnTy2wM3vhp1e2BT5Gq4q8w-IxvOku8Jl_rnj_0qdRn0R_2_gJWn06rUMOcZXUmMehfzJrjGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=NbvSKvRjnN_HwY-a8jtZWyDeSfKANY9kv1huz5KGbphcfVLwFPxE_3BT2cwqowx7Eb0D4vgY9Xk_ArsMpQ4TbFMKvqviI5VaeaGOC0LNd80fi2Gl8AP_0cy_HpPuC5I-drxN1XKYHIBjbNAMBLxhLavwa22snLqaC_GnBZFRpVoMcxsKFP4kl9yKvJ-y-Ye98Nb0o3zA0iZtzkgm6LvKkSHZdoN0ats_RO4IYcgjtXq40UwTNWhLlttsl9ZCgohtUWnZkSNN_JoFmNnTy2wM3vhp1e2BT5Gq4q8w-IxvOku8Jl_rnj_0qdRn0R_2_gJWn06rUMOcZXUmMehfzJrjGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
فردا به دعوت پرزیدنت ترامپ به واشنگتن سفر خواهم کرد تا با او ملاقات کنم.
پس از آن، در مراسمی به افتخار یکی از دوستان بزرگ اسرائیل، سناتور لیندسی گراهام، شرکت خواهم کرد. باید بگویم که او از زمان تأسیس اسرائیل یکی از بزرگترین دوستان اسرائیل بوده است و شایسته است که این افتخار را به او بدهیم.
من با رئیس جمهور ترامپ ملاقات خواهم کرد تا در مورد تمام مسائلی که در حال حاضر در دستور کار است، از جمله وضعیت ایران، گفتگو کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69011" target="_blank">📅 14:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69008">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LHRd6ziU10MYZnjCkxjDvNuFiNRsOj-aOyCzAUrNjbvjUMQhaZZ84WLOxJHPEo7Uzx57X4NuPAyMhpycLadJLe16etp81qA49RuoCtMFXsZ2EQ0sjb_hAOyC3aOPpJprHuUPYIyw0XA8bnc-ZmEz4UdExTHcejfp_5wl-oU9F8yHBTS7Cv9_a78m8Xdn0tgzEOqI8iXLm2QUkJQFX-iPPakMEa3osK6eLUGzyo_sio5s7VuRzfPu9vQLHY-VMmclYr9Bgd-nH-OgVOTLkwZ_0conZDDkAC2ukaakWa7labGcCnqIiMiCwbSF1h4eTsQA9E_f8jTV-XFTZMsPicRGbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VhM_LCqynRbZ266g7KnyCRJf15p8chELdYMfkhw7O-NrCFhIvTZnrZXaOmB8yCxUT-651pPxhDlBomOxB6vDR3MZZ3g-NciJK1f5yd40ZEuzige_0lmBbWmC7d1jFGbEG8x6_Xq5zT7yPmdhHXJ4mcS9H0x7cjnACicR-64aIgyxfg6LQ9g3QQtKszryCl5vO2-p5rh_Xf2EDXVJRd8ljP4P822trlz6lzQM6a-GPlf-3rU4DWTWgBIsnCeyXbYlWnoNNGTnOtN7WyV8vqMiZZA5fC6gOH4ZAxn4xm8FLGanscRTWdEVpvkdol6OxdmcQeFlL0QJhxBjYmbD8yXJvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=ZdIxXiJCFaL4XZS92FtVJC5xM9j3FGyFbqKW2qNBMvoxCMl5AkclwiJzavpF6272f3nhgGpaZz-QBmOITzARcSrqQgtqssgd311r6rP5QRV8KAe2OfenqaeXQ4XtSun0Xi8poVMAc1700s7thEkHqAYK09ygf1nnhEj0I4n22Yi3U3IkhC3fztFguURofM_MEZf4-Fn2Y1huMlRs3RnANsEZBmAcV1oES679xrAqb5_iMbvD5BBXn9TpMQdw7a5j5oujQJOxYR4bej7Tu13oA9vmmhufe3Ro6ScsaFq_v6N3BVcM10VtG3UWxHSNWwK3nTggJktV8ynK1sKjUpaEOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=ZdIxXiJCFaL4XZS92FtVJC5xM9j3FGyFbqKW2qNBMvoxCMl5AkclwiJzavpF6272f3nhgGpaZz-QBmOITzARcSrqQgtqssgd311r6rP5QRV8KAe2OfenqaeXQ4XtSun0Xi8poVMAc1700s7thEkHqAYK09ygf1nnhEj0I4n22Yi3U3IkhC3fztFguURofM_MEZf4-Fn2Y1huMlRs3RnANsEZBmAcV1oES679xrAqb5_iMbvD5BBXn9TpMQdw7a5j5oujQJOxYR4bej7Tu13oA9vmmhufe3Ro6ScsaFq_v6N3BVcM10VtG3UWxHSNWwK3nTggJktV8ynK1sKjUpaEOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۴ ام مرداد، سالروز درگذشت رضا شاه بزرگ؛ بنیانگذار سلسله پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69008" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69007">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇷
محبی سخنگوی سپاه یه لیست از خسارت های آمریکا گفته:
⏺
در حوزه راداری و پدافندی:
۷ مرکز فرماندهی و کنترل
۳ سامانه ارتباط ماهواره‌ای
۶ رادار پدافندی پاتریوت (سامانه‌های پاتریوت به قدری ضعیف شده است که موشکها و پهپادهای ایران بدون رهگیری به هدف می‌خورند)
۳ رادار کنترل و مانیتورینگ هوایی و دریایی
۸ سامانه راداری کشف و اخطار اولیه
۷ رادار دفاع موشکی هوایی
۳ سامانه راداری EPS
۲ رادار EPS 117
۵ رادار برد بلند
۲ رادار پدافندی
۱ مجوعه راداری تاکتیکی
⏺
در حوزه پشتیبانی و لجستیک به منظور کاهش توان عملیاتی:
۶ مرکز تعمیر و نگهداری جنگنده و بالگرد
۳ مرکز پشتیانی و لجستیک
۱۲ مخزن سوخت
۱۷ انبار پشتیبانی تسلیحاتی و قطعات شناورها و هواگردها
۶ زاغه موشکی
⏺
در حوزه زیرساختهای عملیاتی:
۶ آشیانه پهپاد ام کیو ۹
یک سوله آماده سازی جنگنده اف ۱۵
یک سوله پهپادی که ۸ پهپاد آکبند در آن بود
۲ مرکز فرماندهی
یک سکوی سوخت‌گیری ناو هواپیمابر
یک آشیانه هواپیمای پی ۸
۴ سکوی موشکی هایمارس
۵ آشیانه جنگنده
۴ مجتمع پدافند پاتریوت
۶ سکوی پرتاب موشکی
یک ایستگاه پمپاژ سوخت
۲ مرکز مخابرات سیگنالی
یک مرکز داده‌های اطلاعاتی
یک مرکز هوش مصنوعی، پایگاه مرکز پردازش داده مربوط به شرکت آمازون
یک مرکز دپوی شمپاد (شناور مدیریت‌پذیر از دور)
یک اسکله سوخت
۴ شلتر جنگنده
۶ رمپ پرواز و توقف
⏺
در حوزه عملیات هوایی:
۱۱ هواپیمای جنگنده و بالگرد (روی زمین)
۱۷ پهپاد شناساییی و عملیاتی (۸ تا آکبند بودند)
یک هواپیمای جنگنده اف ۱۵ داخل شلتر
یک هواپیمای پی ۸
یک هواپیمای ترابری سی ۱۷
۸ هواپیمای سوخت رسان
۴ بالگرد سنگین
۶ موشک ذخیره
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69007" target="_blank">📅 13:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69006">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⏺
🇮🇷
بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
مقامات ایران و عمان در تهران گفتگوهای سازنده‌ای درباره تنگه هرمز انجام دادند و رایزنی‌های فنی و سیاسی در این خصوص همچنان ادامه دارد.
چندین دور گفتگو در روزهای جمعه و شنبه در سطح معاونان وزرای امور خارجه برگزار شد. در شرایط کنونی، هیچ تغییری در تردد کشتیرانی در تنگه هرمز ایجاد نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69006" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69005">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیوی تعجب انگیز از داخل هواپیمای یاک-۵۲ که در آن تیراندازِ صندلی عقبِ اوکراینی، از کابینِ روباز با استفاده از تفنگ خود، پهپادهای گران (Geran) روسیه را سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69005" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69004">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=nLicy3rafCJLsc3AxY-i47xiglqh5HAJKphrTAD1wZMMpOLba0HWtW2357NB0ELBFhal1YeTatQ3vk-THhJzsKN46jhxjgvseEE2DAEaWuyO6U6KMXCXwFD5HtDpPwfqpO9yY1niNwIAD82z2ZiG6RS2Suu4oPUD066stiUDqvzuQCf98FuWUpCRR1ZDBhfyfJnjCN02as6FOQtXudSbV5ABQ8WeXMYUnm_l0LurkLothAqh0f1_HbMLmd797tfRisDN2fzOVW9u9FzcXF4u4e7zvBTiuWl_dDSghQpusTY8C5VI1ltJkhWxPFgrB_z4gg-lD-JNMdNVf8HMmQOBjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=nLicy3rafCJLsc3AxY-i47xiglqh5HAJKphrTAD1wZMMpOLba0HWtW2357NB0ELBFhal1YeTatQ3vk-THhJzsKN46jhxjgvseEE2DAEaWuyO6U6KMXCXwFD5HtDpPwfqpO9yY1niNwIAD82z2ZiG6RS2Suu4oPUD066stiUDqvzuQCf98FuWUpCRR1ZDBhfyfJnjCN02as6FOQtXudSbV5ABQ8WeXMYUnm_l0LurkLothAqh0f1_HbMLmd797tfRisDN2fzOVW9u9FzcXF4u4e7zvBTiuWl_dDSghQpusTY8C5VI1ltJkhWxPFgrB_z4gg-lD-JNMdNVf8HMmQOBjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اکبراعلمی: مزد خدا بود و پاداش الهی بود که مجتبی انتخاب شد
😐
خدا امسال سه ماه قبل از قدیر ؛ قدیر رو برای ما نهادینه کرد و خدا برای ما مجتبی انتخاب کرد.
شهادت میدم والله خدا انتخاب کرد مجتبی رو.
با این انتخاب خدا کاری کرد نه نام خامنه ای نه راه خامنه ای تعطیل نشود‌.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69004" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69003">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=W95ah6vXvS1e38BtdKTfRKVsrzhnUMEEzaAnJ2DdWH0QtETjQDtLz2truOJWa2BIiRV_EMWyY_uoWg9Cgekhl17XrVCdmLeovwyD5koiRTJtYCpaGiXopE2FyAmvoDGrTXby4qFd6wW1FRgMHwDFbsfFpbWw-SQCJEf68E0cUVUPX0TVRgHe2at-8vUz5KpzSibIuJjdOtrofibvSi4duAv4y1nprf0TDQC66lQcxZgiySLYFr7_AQlIhbqqFKuidbEYh_p8Lp8umU-nnVkzrb3ln_q8O9W0w0aT2q8jcezWq5c2R7u04gNYJb3-pHhHMi_cvVNfuQ5wTnaJuJJzpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=W95ah6vXvS1e38BtdKTfRKVsrzhnUMEEzaAnJ2DdWH0QtETjQDtLz2truOJWa2BIiRV_EMWyY_uoWg9Cgekhl17XrVCdmLeovwyD5koiRTJtYCpaGiXopE2FyAmvoDGrTXby4qFd6wW1FRgMHwDFbsfFpbWw-SQCJEf68E0cUVUPX0TVRgHe2at-8vUz5KpzSibIuJjdOtrofibvSi4duAv4y1nprf0TDQC66lQcxZgiySLYFr7_AQlIhbqqFKuidbEYh_p8Lp8umU-nnVkzrb3ln_q8O9W0w0aT2q8jcezWq5c2R7u04gNYJb3-pHhHMi_cvVNfuQ5wTnaJuJJzpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبل از مرگ خاطرات آدم میاد جلو چشماش
من موقع مُردن:
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69003" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69002">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuT63B1GKxsVNAKqRniCAOCIUaGABCPKioWq0veF0wpQxRwTHMm6yPBV0vdUTlHocifarYQ8ElQsUtVhu63bzxKlG-Z_7mfp5OgN5AaJ54_h4u7Cupl9rgFSjPAZxU6QtIbvb2mfwj_K6_9x7ZHcilwXNxuYBtTpvJk7gFPr5ACnYCP2drwcV-bDDfAIPEH7pdzpi5a_2GHx0NRlHcYJtVTJJ6gm7QejECQ6My_r1932nS6XVRD1g47NZH-n-SodnHdVZVy92kFiUtnGbm-BHW8VsX5aGGx3GdLnkB5aIoNtq4e4NRlpwcY32lGxZ3XcbMW7bLH0j9J8wN2RinIZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک پست:آمریکا طرحی را برای ربودن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران بررسی می‌کند.
نیروهای عملیات ویژه آمریکا در حال آماده‌باش هستند تا «پیچیده‌ترین عملیات تاریخ نظامی» را برای تصاحب اورانیوم غنی‌شده ایران از تأسیسات هسته‌ای به‌شدت مستحکم‌شده، به اجرا درآورند.
جوزف راجرز، معاون مرکز مطالعات استراتژیک و بین‌المللی، گفت: «گفتنش برایم ناخوشایند است، اما فکر می‌کنم محتمل‌ترین راه برای خلاص شدن از شر مواد هسته‌ای ایران — دست‌کم آنچه اکنون در اختیار دارند — یک عملیات نظامی است؛ زیرا مذاکرات پیشرفت سریعی ندارند.»
یک منبع آگاه از برنامه‌ریزی نظامی روز جمعه به واشنگتن پست گفت: این عملیات بسیار پیچیده شامل هزاران نیروی زمینی خواهد بود که به تأسیسات هسته‌ای ایران حمله می‌کنند - از تله‌های انفجاری عبور می‌کنند، از خدمه ساختمانی استفاده می‌کنند و یک نیروی دفاعی بزرگ را در اطراف این سایت‌ها حفظ می‌کنند.
به گفته آن فرد، از آنجا یک تیم کوچک از نیروهای عملیات ویژه، عملیات واقعیِ بازیابی را انجام می‌دادند؛ فرآیندی که «بسیار خطرناک» توصیف شده است.
این یک عملیات لجستیکی سنگین و دشوار در یک محیط رقابتی خواهد بود. ارتش ایران کاملاً نابود شده است، اما آنها هنوز از افرادی که از مادورو محافظت می‌کردند، پیشرفته‌تر هستند.
بر اساس گزارش رسانه مستقل و مطلع «های ساید» (The High Side)، این گروه از نیروهای عملیات ویژه می‌تواند شامل «اسکادران نقره‌ای» (Silver Squadron) از تیم ۶ یگان ویژه نیروی دریایی (SEAL Team 6)، گردان دوم تکاوران (Ranger Battalion) و گروهان ۲۱ مهمات ارتش باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69002" target="_blank">📅 09:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69001">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt8n_TpB0cFjFBi2s1PaMRRl7PeUTtpqBFH-tTkq0ukwrlfIKpSJxcmGN8y-huDKaIl8z1c6C81fUyKW8TVDbL0wRwS2GvXHXXPojazRy2RjXhMUYgpwUuZqg0OlzsAHF4YLDAR-I5IbhwIP8rZfNty-kmGKl9aYX_vlFNLMEilg7YouudwY9vBCPnHHdGClvdeWc61AjJwwY5IO-y2QAsL0mDL5-1NDDcijEN4vxhcQgmeEGeWt89siWnFBvwgMRCHWPUfWRmUEdat0O24bLGL2pfRSIYHWhWlw3PwNKr7T6BvBRu3F3BcwDVOBYnZ3wVV85UeV0FIWuubvnIQmUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
رادیو و تلویزیون اسرائیل:
با وجود تعویق حمله آمریکا به ایران در روز جمعه، روند پیوسته ورود هواپیماها و تسلیحات آمریکایی به اسرائیل همچنان ادامه دارد.
آمادگی‌های نظامی آمریکا، حتی پس از لغو حمله برنامه‌ریزی‌شده برای شب گذشته، همچنان در جریان است. این تقویت قوای نظامی، بخشی از تلاش گسترده‌تر آمریکا برای حفظ فشار و در عین حال، تلاش برای بازگشت به میز مذاکره محسوب می‌شود.
در حال حاضر، حدود ۹۰ فروند هواپیمای سوخت‌رسان هوایی به همراه یک اسکادران از جنگنده‌ها در اسرائیل مستقر هستند. طی روزهای اخیر، محموله‌های تسلیحاتی و موشک‌های رهگیر بیشتری نیز وارد شده‌اند که یادآور تدارکات و آمادگی‌های پیشین است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69001" target="_blank">📅 02:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69000">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae9373361.mp4?token=pRKZ04vyMhnhri09akDm1LPWReurQFVrzBBwIOcV7MfLIsmlOkOMJXWIvmdCcJyH3RwX7u7OlNPY081RkqkruGP-sv8g4xNM37Jdh83kmrFJoQ8sRVt3mAnFDYLLfazwnRfc205MYHPn43-T_twUCcy68UHwT4GQlOuYDZ_sGyVweYx3EdRGsph_cGZ4ULZ1vcuntExI0noes-i0IvayLJKsaHNJGXX-dHmYt3uGRqv9mqIB-QnR0d1IcQVb_I6B6YJM-8Ouu60wk8MnoyElCvB8s-c5ekhGa9SH4dTg4TLNQihOGFxITReOCsebZRtDDBXovv2wJ0P_dTvk2QOtjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae9373361.mp4?token=pRKZ04vyMhnhri09akDm1LPWReurQFVrzBBwIOcV7MfLIsmlOkOMJXWIvmdCcJyH3RwX7u7OlNPY081RkqkruGP-sv8g4xNM37Jdh83kmrFJoQ8sRVt3mAnFDYLLfazwnRfc205MYHPn43-T_twUCcy68UHwT4GQlOuYDZ_sGyVweYx3EdRGsph_cGZ4ULZ1vcuntExI0noes-i0IvayLJKsaHNJGXX-dHmYt3uGRqv9mqIB-QnR0d1IcQVb_I6B6YJM-8Ouu60wk8MnoyElCvB8s-c5ekhGa9SH4dTg4TLNQihOGFxITReOCsebZRtDDBXovv2wJ0P_dTvk2QOtjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو خاورمیانه همه دارن هر شب در هم میذارن.
🇮🇷
واکنش عباس داوینچی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69000" target="_blank">📅 02:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68999">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=VbAC8Km6g0iw-dtMVHakNoh0kZ31HqXXWtp60VQ1BztEoBUIq-h-Wf9gykRv13WBo6BSxex5mEkqpvhV72SS_P_RD1sZZ11SthOdgchxJMCvt8S0GkJZPsXCsqAQ7h7JuFCuMHZxD1ILsOtPrKFAgiQ7NJUqsH8_wqQtzh5ARyw7NjOW1lnUrdz70rY1AMyA63_ePTl_eQ0w07rcgQVRfSgcnOr02hB29PhTgPbsgopdXS8zDBAoi2uJSDZHdOdYFptuXHPnAh6vhcBm5Z6q4mEsEpf5zG5Z8zlhDu0uQEybVw4RFJQA4-PSz5IcoHljVzY8tUXf-ZZVbq3xPvuHGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=VbAC8Km6g0iw-dtMVHakNoh0kZ31HqXXWtp60VQ1BztEoBUIq-h-Wf9gykRv13WBo6BSxex5mEkqpvhV72SS_P_RD1sZZ11SthOdgchxJMCvt8S0GkJZPsXCsqAQ7h7JuFCuMHZxD1ILsOtPrKFAgiQ7NJUqsH8_wqQtzh5ARyw7NjOW1lnUrdz70rY1AMyA63_ePTl_eQ0w07rcgQVRfSgcnOr02hB29PhTgPbsgopdXS8zDBAoi2uJSDZHdOdYFptuXHPnAh6vhcBm5Z6q4mEsEpf5zG5Z8zlhDu0uQEybVw4RFJQA4-PSz5IcoHljVzY8tUXf-ZZVbq3xPvuHGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
محاصره دریایی ایران توسط ایالات متحده همچنان با تمام قوا در حال اجراست. تا تاریخ ۲۵ ژوئیه، فرماندهی مرکزی ایالات متحده (سنتکام) مسیر ۱۲ کشتی تجاری را که قصد عبور از این محاصره را داشتند تغییر داده، ۲ کشتی را که از دستورات پیروی نکردند از کار انداخته و برای اطمینان از رعایت کامل مقررات، وارد عرشه ۲ کشتی دیگر شده است.
پیش‌تر در روز جاری، نیروهای آمریکایی عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «چارمینار» (Charminar) با پرچم کومور در دریای عرب به انجام رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام در تاریخ ۲۴ ژوئیه، نفتکش «لاوین» (Lavine) با پرچم موزامبیک را در دریای عمان از کار انداختند؛ این اقدام پس از آن صورت گرفت که خدمه کشتی چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران حرکت نمی‌کند.
نیروهای آمریکایی همچنان بسیار هوشیار، متمرکز، مرگبار و آماده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68999" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68998">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_grE6OHQBPvQvezozuJenYYGsYRXjuQknrzZPEc9mW5gvXTELXK_aSk-YtmRDlCjPIsst2tPyrdAJbInR1JWlIB3UvcdiKT8wUGxsA09eBBV-XHRhZyehHMmjUDfYlqQEQJKG_KsdC9Qb8ufsn4KCdU2EuVTn_KdEq8pmmSoUqv8U4ujFPyKYku8IKjEii_lBaFJvgfJ0p9aAWSJUjY0vi9Z2rcvjaNYOYTGmpRh09VE2543mmK4fnwnoiesIjP4TR5rjWdQuc6mALXba7Kgcq2d8wV0HjNT_vdDNCy_J5bWpw_VqKYtZzHBWfi5foN-eOGT8fP3E2Dvj7DsUcJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68998" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68997">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
اوکراین، یک کشتی متعلق به جمهوری اسلامی را در دریای خزر هدف قرار داد!
تاکنون مرگ یک ملوان در این حمله تایید می‌شود، رئیس جمهور اوکراین می‌گوید این کشتی حامل محموله نظامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68997" target="_blank">📅 23:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=EqniXM4m6OMvdVX7nYhd37oSTOtnhjylTQz6K0iXvzlVTVz2QFVAjtZX-WAl79IaswW6c4iGHePJCKMSozZnk7xkFTz--Fkuoa4jVj3Leodf23bFlQsfY3F8idnhHcEikkTycY3HPsW95z_Obdx21euLYZFC6XpJKxSR58UX2MQICBYggEtOw2GTyCT2bhfymbctoyFFUGdFzl_v_B-Xkaqn0PZ8Mg62FnJAOfih4fm5SV3RLjohUktBNWtWJBQeGxRGIGKatOr6oFvekW-FoS7_FrAZLgyKS_CJvYxPzKc6AYAKJV9tS79B6xhtE3ZBX_L2Yl3oIGS8ma8InFjC2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=EqniXM4m6OMvdVX7nYhd37oSTOtnhjylTQz6K0iXvzlVTVz2QFVAjtZX-WAl79IaswW6c4iGHePJCKMSozZnk7xkFTz--Fkuoa4jVj3Leodf23bFlQsfY3F8idnhHcEikkTycY3HPsW95z_Obdx21euLYZFC6XpJKxSR58UX2MQICBYggEtOw2GTyCT2bhfymbctoyFFUGdFzl_v_B-Xkaqn0PZ8Mg62FnJAOfih4fm5SV3RLjohUktBNWtWJBQeGxRGIGKatOr6oFvekW-FoS7_FrAZLgyKS_CJvYxPzKc6AYAKJV9tS79B6xhtE3ZBX_L2Yl3oIGS8ma8InFjC2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیروزمند:
تا کی قراره ایشون ( مجتبی خامنه‌ای) بیرون نیاد؟
🎙
مجری:
تا نابودی کامل عوامل جنگ.
⏺
پیروزمند:
خب اینطوری شاید ده سال دیگه طول کشید خب ما تا کی اماممونو نبینیم؟ اینطوری همیشه در موضع ضعف میمونیم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1C3-VgQcfcryqgOkebK_uQ365IIOulvJo-pLPGzmcngvq6gxp1Ex58Hfgta2j1xmSjLUHa_-E09v8344vGZhO2k5rDxbCwPLHG7lJ7aQqNZXYElPU-Lk0YA9GcJYyq8xMmN39iGmoEnE_tsIO1flK473XF3cPR-jqEERP3r7f2RaPP1-JejBJXklxqXGIa5eWLkMzzhJo9J9AE3xkElaN__iOA4Viec5x0uGRWfqGTP-JE8awT5hpXZ7pBrRUmpZdETrcqSmTZGuaJn13x6uWxiA-F_5SoeVuAp3SMnBSHp0lxNf4_LbSi39qte2zIazTLnqamE5MYVlB9VbEnb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUc1DqU0SAG3Uh48ed3v2uA0KRGQPwuHqVSNTxRri1oMwOgi8CNC6Ys20fKWryVrVCt1JGDJc2eXDvxQB3CiOIn5_qmiArDnVI0o3uN3db95SDRnjv0V_J3aO9B18yltNBgTNsz6syH56RvvFsmmWZiSJtZNTFAj5QhNdDPpZ9AN86vurG6ELLncSPKVcs8iy_sMabdUuSgjzeDQqvj79Pd5WO0hkhKkDu3w02m65vozczk0xQs4vay7TtG85eK3iI43-Gfx1fkzGmR1z1jWuy9ATegvdJPqZXEpzTl-xFu0TTVVk0gO4IyLsfmG1xvCBfHjRSuwsdzjJtOOwz3pOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5v7W5kj0oqKG-bbrFxcJV7DJvEZj-gIIAHfGSHvC-GfGt8c8pC4-DyUA2hF9hduInLEWCTTPkthdQrVVAfhYh8h8E5doXs8pVo0_IwqvHbmdSxjr6VoaJ1NnBxkQqzPST-3obnV7VmWD58EOoRUwvG3taqjKCS9Dkh_2rPNpKmYQPAeliJQAsogFhtmNdfL6JYw3o09DqGKhZikj_9PxXcFh9BHEU8L1a_r536lQYefYABXfiv8rRXwFdiwMgc97TnDRO8p2iGXL6S1Poxp1Yn-VGQssYE71ojmLHmOQ28-bLYYAm14JFYT02ML8jSbfUC8lcM8-taGDzpCM3YQ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=HJK6uHUOUXnzVoZ8JyvJz9fcP4_8_fqgDlKY9JAJVCTKLzp09VaMMnVtLhScW8A0Tl0dgdTgjfW45nCyO2vYJ8Y5qByuk7u1IcFHMfdpsDG1ud0WPh7Rogn9H-yvv0Xyiq_stj25tR3GT-RR7GRmR_7XptandDAwxCj9hTQ4nCLpo7Qw5rYqQgE658qyvuAP2knVUKq0waQHkCyXirdlZNPe6ORFVKG5aNnvBaOqGxBzFQu4g03pZEpaUQ87k5RmhGAV3VEN8UGRGWMLbYcBZPgpxvGI0PBT3k1UO_02ATBL7P7J3Ge-FnMcboSoFJyRrO1Qh7Xwvg5A04nCjOoFkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=HJK6uHUOUXnzVoZ8JyvJz9fcP4_8_fqgDlKY9JAJVCTKLzp09VaMMnVtLhScW8A0Tl0dgdTgjfW45nCyO2vYJ8Y5qByuk7u1IcFHMfdpsDG1ud0WPh7Rogn9H-yvv0Xyiq_stj25tR3GT-RR7GRmR_7XptandDAwxCj9hTQ4nCLpo7Qw5rYqQgE658qyvuAP2knVUKq0waQHkCyXirdlZNPe6ORFVKG5aNnvBaOqGxBzFQu4g03pZEpaUQ87k5RmhGAV3VEN8UGRGWMLbYcBZPgpxvGI0PBT3k1UO_02ATBL7P7J3Ge-FnMcboSoFJyRrO1Qh7Xwvg5A04nCjOoFkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ساعاتی پیش یک هواپیمای آمریکایی در فرودگاه جده فرود آمده است. به نظر می‌رسد این هواپیما یک هواپیمای آواکس مدل E-3Sentryباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiNtDerKPD8-BH5ePc1HtFpadmJN-f8L_dc0KZEQL6FYCBtFLm_XQi7FgI3rDNO68uKjqsRWqsoUAiXID0pUrUhbK-nH2GHcd76dihjE1pLnriOLRnrwtAsKmdREu8jhgor3NTtzFg_nU3tYxN3zDszuBgkPtLVJZSIEvh3LlIL7jbR64HRAV2yJNJ3x9UbYevFe5cIG5ff_hUFcEllLSTN9JkFmhNAXO6TkdYRwWIYvxGAwAEqjVOvmz4MPrQoCPgJ1M4ZJALuCvsMe5OiWBEVlCT2YtPUP-9tJihEejyf0joj1S-hQ0YbINHK5OPdDyJG7s9v-A_4QCr9YRlQyeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4bab692977.mp4?token=CQlwADdAL5l0bB6PXKMrOkbW0PPBpQA32yCRZLavwdDw7Z4fs9V3MH7Fo8o0OA5Su6FQpTtiBFI1xeiWpnaSuvXR6pSmlSaUOK0BM6qWfMfVDVj4oon7YT09XJSsT9knLFBVn4y375_2a01Aiq8dcqbzeFpw5LE0n0XLsQgCcXua1s6wD1U8zSbyX0KzCqqHoTGoUFQJGtFMUwzewOhA5_REMMSRpSWu5kbV9MTISM1a91NpzFnN5C14lgu2YTxN2jH4DFvOYiIPAbQ-XhFxjXkdVZYkMWHXio0yPItqgd2EpLe5TvRnX2ILuZsvS-Mtst3und3kUAhnlcL50WGm9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4bab692977.mp4?token=CQlwADdAL5l0bB6PXKMrOkbW0PPBpQA32yCRZLavwdDw7Z4fs9V3MH7Fo8o0OA5Su6FQpTtiBFI1xeiWpnaSuvXR6pSmlSaUOK0BM6qWfMfVDVj4oon7YT09XJSsT9knLFBVn4y375_2a01Aiq8dcqbzeFpw5LE0n0XLsQgCcXua1s6wD1U8zSbyX0KzCqqHoTGoUFQJGtFMUwzewOhA5_REMMSRpSWu5kbV9MTISM1a91NpzFnN5C14lgu2YTxN2jH4DFvOYiIPAbQ-XhFxjXkdVZYkMWHXio0yPItqgd2EpLe5TvRnX2ILuZsvS-Mtst3und3kUAhnlcL50WGm9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلنج شکن معروف اینستاگرام که هر چی داف بود میاورد پیش خودش و نالشون رو درمیاورد دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=ppppKPTccOL62CZawbdi_fa7NLwRoTnpH1MwCMZ-4bKnef6O9N83B4hnwATg5KbyBYun6LrOpn5P77Hwps9GytlgX1LLZCNFjexA4v8Bd_dcY3YbDoEkdb9YTPr_9_9ZnJyXMXrIfGGVgcrnHj4E89iWpoq8xw8dc_xpEwbKzspWVeDDK2bM-tgvAQwQGyX1cEtUaPSP7tGz1hTHqdmlTU7ghbhJXaI7xQdsOVMlHSUiNp9XaTdWmptrY_rGgYSwoYMdi-2d_cAtnBCO6n64j_-gyuKECA4AhcCv5hWmXgb2MQcDGTi4ctS6j79AOnsb0R8HgRAl5jp-rh2NAsbSKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=ppppKPTccOL62CZawbdi_fa7NLwRoTnpH1MwCMZ-4bKnef6O9N83B4hnwATg5KbyBYun6LrOpn5P77Hwps9GytlgX1LLZCNFjexA4v8Bd_dcY3YbDoEkdb9YTPr_9_9ZnJyXMXrIfGGVgcrnHj4E89iWpoq8xw8dc_xpEwbKzspWVeDDK2bM-tgvAQwQGyX1cEtUaPSP7tGz1hTHqdmlTU7ghbhJXaI7xQdsOVMlHSUiNp9XaTdWmptrY_rGgYSwoYMdi-2d_cAtnBCO6n64j_-gyuKECA4AhcCv5hWmXgb2MQcDGTi4ctS6j79AOnsb0R8HgRAl5jp-rh2NAsbSKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تیم‌شی‌هی سناتور آمریکایی:
جمهوری اسلامی گروهی افراطی و تروریست هست که 47ساله کشور رو تصرف کرده و ایدئولوژی نفرت انگیز خودش رو گسترش میده.
این رژیم اهمیتی به سیاست های حزبی یا اینکه به چه کسی رای داده‌اید نمیدهد.
آنها میخواهد همه ما را بکشند.
ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
حملات موشکی پراکنده به کشتی ها یا تحرک قایق ها در تنگه‌هرمز نشانه قدرت نظامی نیست بلکه دست‌و‌پا زدن یک حکومت در حال سقوط است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9esvzNIcONC4nDcq0aFOW64uckWHK0D0RGGrp6XFurg7jSMAxzKQaU9h8tYv_o-uvDrez9OHZRi3gvVDzljrhXH0OGfeZ5qdt7D0WT6cVoaiPH4aphSUDI_dBFrLjfJBUdP481ABIw3qN8IrogosYTAimRWGDU6bSQrCw9rtbr7zBNx50IFYgvbBOth6y8oUhpk2Yn75UP5qOgVVxub_ThhRGEhOD5SIV4jMfGLtukxI-IWPSovwwkGbO_YMXj-JaKS1aKMc10lIm6lT6rZl2eV_vY0qKza4YSNqkeQiapqTgM2P1y2Yn06Np6Gb8NsFZMgA3mN4FWKgZ_Q6oPKrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=S82Bcwkw64cGr0aFghk-HLuP12WbWgSlvk_2vgwKHkNthW2UUPhq1aroT_DASsbiyekipfaWYXaSkm6modCbA7A1d-s2FTunTTFOWMnSwlTWK36InRqlJIjYWxB3fi2jeEj2twdV9fvItHGSy86rht-5SxID5muwocVyKpzp6q6VYdhd2DxBk3-al7_wnv4SapMc6NUfubKiAtjSuqIP2TENcq3k_XoGDbdaHbKEbjzqemWjN5aEKzTuvqnvWJphSXwfkOm8Tig07LtobQKwjRfwmtDsJHxD2Sv1ZEKO5V95qciP60QyWED12B5v04o5l8nGi6Ubz6Xfutg-0nK5nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=S82Bcwkw64cGr0aFghk-HLuP12WbWgSlvk_2vgwKHkNthW2UUPhq1aroT_DASsbiyekipfaWYXaSkm6modCbA7A1d-s2FTunTTFOWMnSwlTWK36InRqlJIjYWxB3fi2jeEj2twdV9fvItHGSy86rht-5SxID5muwocVyKpzp6q6VYdhd2DxBk3-al7_wnv4SapMc6NUfubKiAtjSuqIP2TENcq3k_XoGDbdaHbKEbjzqemWjN5aEKzTuvqnvWJphSXwfkOm8Tig07LtobQKwjRfwmtDsJHxD2Sv1ZEKO5V95qciP60QyWED12B5v04o5l8nGi6Ubz6Xfutg-0nK5nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس با انتشار این ویدیو:
مردم جاسک، اسلحه‌ به‌ دست منتظر اومدنِ نیروهای آمریکایی هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=acM96Z_E74w0qKpUzkwm6sW9o0Mw-XdH-TorcDQG86V7zqt_rVAUC33Nbjt9qDEBCenaz7CNbvypw6NeIAIjHaaRk3I-_WoutiSo6DIl266BBiGhSX_Pg7TYjFwtLE1NE9Q3VEg26SCNLh6SoFi7nEenADB1KbSxqwd3BXE-WsQzPqHUEH9F2d4tgdWxToHJgYzxIwk8Yp4AhJvVIrbtn-XTVXSZQsFvWRnj7txTvtqtu7jNK1ioumkz0cjIFOuGQ4gJIOu3JW4pq5k_rAin7JZ8ulkZIX_8JT-kSWMuGAKmAAqgljqMuID0gM1Dobr8Qf1JHL-RmOTFEtLa_B7CTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=acM96Z_E74w0qKpUzkwm6sW9o0Mw-XdH-TorcDQG86V7zqt_rVAUC33Nbjt9qDEBCenaz7CNbvypw6NeIAIjHaaRk3I-_WoutiSo6DIl266BBiGhSX_Pg7TYjFwtLE1NE9Q3VEg26SCNLh6SoFi7nEenADB1KbSxqwd3BXE-WsQzPqHUEH9F2d4tgdWxToHJgYzxIwk8Yp4AhJvVIrbtn-XTVXSZQsFvWRnj7txTvtqtu7jNK1ioumkz0cjIFOuGQ4gJIOu3JW4pq5k_rAin7JZ8ulkZIX_8JT-kSWMuGAKmAAqgljqMuID0gM1Dobr8Qf1JHL-RmOTFEtLa_B7CTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از طرفداران حکومت، با انتشار این کلیپ آمادگی خودشو جهت
مبارزه زمینی
با آمریکایی‌ها به رخ کشید
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=vFm66_OVeP9O_AiXpNxCNhVzY4vQrRlcABBOlzKpxNHKyHlN_zLk9ngB35PWCZ91RsAKjKpeOOo1OQW9LeR-GH5zQTioIVPJ9njX-lfWNNdAA8q-AS_-QukUEH3cBClPUvfkZT_KSZmbESn3QXQGSFyBlL0XXGRvNvWRrNfA6R2z6Mv2xE9BE0ViYr-Jro4MY57lGA4JDCMx9NmnTn09wV27xU9QqXKCZ_PhNSQ4XOPJPzWMoC3aj0W_Gi94Rwyu8ifS4kmG7BpXAY9MRgHWveKG6_e5GsC81I8AWDWVXw_Hmou9pJ3ke6pkxxgL3H6rgyBt-4R_l3ku-__575q_2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=vFm66_OVeP9O_AiXpNxCNhVzY4vQrRlcABBOlzKpxNHKyHlN_zLk9ngB35PWCZ91RsAKjKpeOOo1OQW9LeR-GH5zQTioIVPJ9njX-lfWNNdAA8q-AS_-QukUEH3cBClPUvfkZT_KSZmbESn3QXQGSFyBlL0XXGRvNvWRrNfA6R2z6Mv2xE9BE0ViYr-Jro4MY57lGA4JDCMx9NmnTn09wV27xU9QqXKCZ_PhNSQ4XOPJPzWMoC3aj0W_Gi94Rwyu8ifS4kmG7BpXAY9MRgHWveKG6_e5GsC81I8AWDWVXw_Hmou9pJ3ke6pkxxgL3H6rgyBt-4R_l3ku-__575q_2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای دیروز پزشکیان که تا به بحث مذاکرات رسید صداوسیما سانسورش کرد:
بعد از جنگ 12 روزه، علی خامنه‌ای رسما اعلام کرد که ما دیگه با آمریکا گفتگو نمیکنیم و صداسیما هم اعلام کرد.
یه روز رفتم پیش علی خامنه‌ای و گفتم خودتون گفتید نه جنگ - نه صلح، حالا ما چکار کنیم؟ گفتش که برید مذاکره کنید و ما به دستور علی خامنه‌ای گفتگو با آمریکا رو شروع کردیم.
تو آخرین پیامش هم گفتش که برید مشکل رو حل کنید چون تو حالتِ نه جنگ - نه صلح نمیشه کاری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fPtRxmVGHL1u8IzZ1ioir-G8hCDmXEM7WeWnvne06qRV60u20klIqhi9bJkhPPHCehreZpC0oPvzJ4-7pbXWhn54gwrLjFrpG2NzE10YeMJU_37ZfuWRLJBGvjLfYWg4wizEdpuFZJ_yHTTV5Ul48UUCJEXw1L-IlsweEZQfzP4VD85dHg0hub5ckw1O7tWv611MEz-67ZBFYThBDzqENLQclW2RbR9yyiZGJJdAS_eUUlB5IME1cowQMMGR7KDST1yM-VNRTdLh8fMmx21MPH5aBJUUObaPeWtOiUbZMALDBYK8-_cshZprHjWG1PBbgDxyiM7YgOH_stKA0s3SIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=fPtRxmVGHL1u8IzZ1ioir-G8hCDmXEM7WeWnvne06qRV60u20klIqhi9bJkhPPHCehreZpC0oPvzJ4-7pbXWhn54gwrLjFrpG2NzE10YeMJU_37ZfuWRLJBGvjLfYWg4wizEdpuFZJ_yHTTV5Ul48UUCJEXw1L-IlsweEZQfzP4VD85dHg0hub5ckw1O7tWv611MEz-67ZBFYThBDzqENLQclW2RbR9yyiZGJJdAS_eUUlB5IME1cowQMMGR7KDST1yM-VNRTdLh8fMmx21MPH5aBJUUObaPeWtOiUbZMALDBYK8-_cshZprHjWG1PBbgDxyiM7YgOH_stKA0s3SIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروهی از طرفدارهای حکومت با مقوا عکس رهبران ارشد نظام درست کردن و اومدن تو خیابون
😳
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=dPjNpC3M51PUP8fuWL3nOCgI9wn0_07oazf6uHJqu11bNQ4ceTZMJS_a_mG0HxV1-8XPwpl41DrhPgi7PivH9HBgP0XNnwCJKWNzDCIdo9GV96JyXSubMWBNm1tzVVWKBiyDHOTe6_Dr8SPpQxUmC_fbjMYxs6swtmu_flui7tOBfxlOXvANfkD8_7doo4_-lS9E5FATL36UjPPwapGBVyZ_3jqPo_AvtSnSwxQ5JPSHKiSuH7sMbHhdFc86V03UxO4X75RdFjCVoZjVnX7TRuZUzXXtUmWtfY0dQr8zTd1TfzhSvIQGWi2q42-HoZN5gTJEwp2XJukK4AvhsAkyGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=dPjNpC3M51PUP8fuWL3nOCgI9wn0_07oazf6uHJqu11bNQ4ceTZMJS_a_mG0HxV1-8XPwpl41DrhPgi7PivH9HBgP0XNnwCJKWNzDCIdo9GV96JyXSubMWBNm1tzVVWKBiyDHOTe6_Dr8SPpQxUmC_fbjMYxs6swtmu_flui7tOBfxlOXvANfkD8_7doo4_-lS9E5FATL36UjPPwapGBVyZ_3jqPo_AvtSnSwxQ5JPSHKiSuH7sMbHhdFc86V03UxO4X75RdFjCVoZjVnX7TRuZUzXXtUmWtfY0dQr8zTd1TfzhSvIQGWi2q42-HoZN5gTJEwp2XJukK4AvhsAkyGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تغییر قیمت یا سهمیه بنزین قطعی است.ما علاقه‌مند به افزایش قیمت هستیم!
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfAhIxf9UGpIBo6T9iNUpTIXqs8KnKzR1D6CcwaRx4mIim_iO__QPaWeLASoqC4tjvA2aRrMZnuJiPEVwYQFh4GmP1hobaRua8r238OoC2gn9vCzwkIJnoPTlnsYb9UmaEsn8JkDaId0cguu2WBBtfRLT5K1GzGykT9WtiL_qvsqI0ZoByGqXNEli247qXldiPeWI1EiYcZT5UsjhDs5YImBQ_nrZ0oM2t_9x9rkpwwGeNBgsRTzfO3ih7A5_Vb46fiQRfwRKF5gj6Zrp3lHrJyzFRSxYgDMJ2ZQeknOpZLKthcdN5T1gygDHudoDWfKGUVxZjgqX7nuUjttCEADnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68977">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=A3QnCY3xh6Y6RJwRb2cf7LqartYX-8WCAioTIhJ7O_coS5znrERAjaFNiOjRMRINDZnvEdalH8GfXCymvJKsPcFH3_bG-q0bhDXmcXoxs6YsR2Lcz-oI9nJ_Fr-sibjFXvWeOQO5uYObEnRdZsGdVfZCccKMo5DXO-CAcoJXJbkZ5V9AreORkQ_o-ffFX3GH7qv9jk1oiFm0W1NQdqofiZL-R_OEbkp9ILqRwHZ1IW5sVsegqqAoK8K_mK15vO9fhLf0Gm9KZqrRhQZDnVxkQpfA8VpG1ppaA30NJ0hstwZ3biEfVyQAlRd84pzFSjWkSl8Q1QaEp1bEEE1Nvhwx-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b75ab51b.mp4?token=A3QnCY3xh6Y6RJwRb2cf7LqartYX-8WCAioTIhJ7O_coS5znrERAjaFNiOjRMRINDZnvEdalH8GfXCymvJKsPcFH3_bG-q0bhDXmcXoxs6YsR2Lcz-oI9nJ_Fr-sibjFXvWeOQO5uYObEnRdZsGdVfZCccKMo5DXO-CAcoJXJbkZ5V9AreORkQ_o-ffFX3GH7qv9jk1oiFm0W1NQdqofiZL-R_OEbkp9ILqRwHZ1IW5sVsegqqAoK8K_mK15vO9fhLf0Gm9KZqrRhQZDnVxkQpfA8VpG1ppaA30NJ0hstwZ3biEfVyQAlRd84pzFSjWkSl8Q1QaEp1bEEE1Nvhwx-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حمله موشکی حوثی های یمن به پالایشگاه جازان شرکت آرامکو
عربستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68977" target="_blank">📅 12:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68976">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqB_Lc4YquB2yLpVwsPt9wO9eku_EKrc86ngfvZXQMcrqWuauo73r103wQN-zYJ7ySlDm_cqdgJl7yVh46UAw3v7UCrj1dtZwPp9zriftxg5DFLow2SkgNPSpxDl2XW7siVsn0rk_GsBsTGYMwwqCdQLFr208H_lo-7yLXw5wlMrmh6VPpS_qQxODfF1l_JEdpFaMqFiJue6isaj1qzFpojWb9Sdu5BRraCgu_sW7hMTLjAwkLh4K9WT2djAQSAfbq8HTiaEKvVxCc_TE3YHCbRuI2DBWnE5jr_urqY-nD6Cx088vv9M3vl8GXzGdeHCAEosTqVHMAhDlVWrnb_FIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
سازمان عملیات تجارت دریایی بریتانیا گزارشی مبنی بر وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68976" target="_blank">📅 12:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68975">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=t7rLtCfJUlsPg8BdDLV7_WM2YdKQraCDyGK6ku5bGEKZg_U8BYCj4hDiHLsr09g_MegRGWE-5am6TCNIDL3nkjJ6UR0qwq2qkqCXL2_mFGit-hgAp1fwdwlozZAlgXBqi3ZT09bMjlr0bLoawP9U2hFsBYgd0Z2TIoC2VvkKYcATjfFX6reswsjMacwciifD8muM8pCZeop4mU95xzscrTy5W5fMoVI9vl78RE0FHP5RwM5hFgYhWdbvQZXx5ROGo0AQyUK_NxgIsqh3hXSCL7qmQ75bCpW05Xt1dGPKexqW51WUnhKfrSNVswQ3HdOHkwQp7zqlXsMaHCGxFeEpbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb03afaeb6.mp4?token=t7rLtCfJUlsPg8BdDLV7_WM2YdKQraCDyGK6ku5bGEKZg_U8BYCj4hDiHLsr09g_MegRGWE-5am6TCNIDL3nkjJ6UR0qwq2qkqCXL2_mFGit-hgAp1fwdwlozZAlgXBqi3ZT09bMjlr0bLoawP9U2hFsBYgd0Z2TIoC2VvkKYcATjfFX6reswsjMacwciifD8muM8pCZeop4mU95xzscrTy5W5fMoVI9vl78RE0FHP5RwM5hFgYhWdbvQZXx5ROGo0AQyUK_NxgIsqh3hXSCL7qmQ75bCpW05Xt1dGPKexqW51WUnhKfrSNVswQ3HdOHkwQp7zqlXsMaHCGxFeEpbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
مجتبی خامنه ای چندماهه رهبر شده ولی حتی کسی صداشم نشنیده. اون حتی به مراسم تشییع پدرش نیومد. خیلیا هم معتقد هستن که اون مرده. نظر تو چیه؟
🇮🇱
نتانیاهو:
حرفات درسته ولی طبق ارزیابی ما اون زنده هست
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68975" target="_blank">📅 11:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68974">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">💢
ویدیو وایرال شده، پشم‌ریزون از گات تلنت
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68974" target="_blank">📅 11:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68973">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=JQckucXDvD0a1eUuL4N8eofib1pHqXIhgrLtEXD3N2LqAYy_KBRq-aKHYM_0B6ACo5P3Vo1ON_kNGeoq2-RzkepZc-7GXkP-n-DVKb-G331yvrffVvOZOlsvtqoEf1hqtIMxUPWYdZ4ZnAkxY749qkdITWnDhiJ8sQAKDGkDXsiL4AWB6e427vrY_N9Far8tf6ylmebIPHidEuGd1hqqXMbNG0gkbdV6F8LutjGgwFk_X6SJpZ3GnwBczKJ75pXzR0AbSTqwqNTQr5wRAlTgQq3EQ_VEtDDICh73wWjqY7LB8gY2Kc2OPLmfIMVxcSUp38fVfKJZ1vHUvWHT1-2C6DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c123fd5ae9.mp4?token=JQckucXDvD0a1eUuL4N8eofib1pHqXIhgrLtEXD3N2LqAYy_KBRq-aKHYM_0B6ACo5P3Vo1ON_kNGeoq2-RzkepZc-7GXkP-n-DVKb-G331yvrffVvOZOlsvtqoEf1hqtIMxUPWYdZ4ZnAkxY749qkdITWnDhiJ8sQAKDGkDXsiL4AWB6e427vrY_N9Far8tf6ylmebIPHidEuGd1hqqXMbNG0gkbdV6F8LutjGgwFk_X6SJpZ3GnwBczKJ75pXzR0AbSTqwqNTQr5wRAlTgQq3EQ_VEtDDICh73wWjqY7LB8gY2Kc2OPLmfIMVxcSUp38fVfKJZ1vHUvWHT1-2C6DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از یک تحلیلگر سیاسی که زمان پهلوی هم بوده:
یه نفر نشسته بود تو کاباره داشت ویسکی میخورد.
طرف کی بود ؟ قصاب بود !
به بغل دستیش میگه ما ک اینجا نشستیم داریم ویسکی میخوریم بعد تو ببین اون بالاسری های فلان فلان شده چه کیفی میکنن و چه بساطی دارن پس.
اینطوری ناراضی بودن مردم از پهلوی!
مردم رو اینطوری ناراضی کرده بودن روشنفکرا.
بهشون گفته بودن میدونید شما خیلی بالاتر از اینها هستید.
انقلاب رو روستایی ها نکردن انقلاب رو روشنفکرا و دانشگاهی ها کردن بعد اولین ضربه رو هم خودشون خوردن.
به مردم گفتن عاای شما وضع اقتصادیتون خیلی بهتر از اینا باید باشه ببینید اون سرمایه دارها چیا دارن که این همه خورد خوراک به شما رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68973" target="_blank">📅 10:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68972">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=JISvFtqv0_05RVbhKEP5Nn7OHOYbSfDHJ1Eim6rmPxKUu7Zdwn0QeL__v1hEU0kJ5GCXYwZekL1HnZqKhtza1_Hba7VNTxxIWEjJmFFVruewi6HVD8s4-GJLG4fnwkDO9gdbqj7o3xDSqejgSUfeMOMya3hmir4kBBKxjmFsA4TrktoDveC2DDxUMWzYS0Ys7Ihk0K69RsE0VIU4VDY0cygQZinGGLXjunvVcgmMycJMByB1lE4WLCLJ-FqVvEBh97UleIKHez-0RFPg4CYe81bHdc9ETckwNy7ofL2lwPtCbjd4XJBs4Eu39AJwYwW55yqDHsxdlAuRwiYdovDy4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6904f498.mp4?token=JISvFtqv0_05RVbhKEP5Nn7OHOYbSfDHJ1Eim6rmPxKUu7Zdwn0QeL__v1hEU0kJ5GCXYwZekL1HnZqKhtza1_Hba7VNTxxIWEjJmFFVruewi6HVD8s4-GJLG4fnwkDO9gdbqj7o3xDSqejgSUfeMOMya3hmir4kBBKxjmFsA4TrktoDveC2DDxUMWzYS0Ys7Ihk0K69RsE0VIU4VDY0cygQZinGGLXjunvVcgmMycJMByB1lE4WLCLJ-FqVvEBh97UleIKHez-0RFPg4CYe81bHdc9ETckwNy7ofL2lwPtCbjd4XJBs4Eu39AJwYwW55yqDHsxdlAuRwiYdovDy4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره رهبری ایران:
«حالا که همه اهالی رسانه اینجا یک‌جا جمع هستند، باید بگویم که ما به دستاوردهای فوق‌العاده‌ای رسیده‌ایم که رسانه‌ها هرگز درباره‌شان حرفی نمی‌زنند؛
برای مثال، در دوران دولت من، رژیمی که زمانی قدرتمند و هراس‌انگیز بود و بی‌وقفه به آمریکا حمله می‌کرد، سرانجام سرنگون شد
رهبران پیشین آن کنار زده شدند
و اکنون توسط یک دیکتاتور گی(همجنسگرا)اداره می‌شود که با اختلافات داخلی دست‌به‌گریبان است.
با این حال، من شخصاً برای باری وایس در شبکه CBS آرزوی موفقیت دارم. او زن فوق‌العاده‌ای است.»
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68972" target="_blank">📅 09:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68971">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=v0CRUNZPCgx6C58mb5rIqm6RHxTpWSfwQbIHXHsxEAIY99GKCaTZsd2GESFn2Pk8ITsH1QzYdYQw0qFg-8muGSORn8ZDytORIxD8NOoTVuK7ahoUSCKLHMQhby9Rpv0bXUzhmCJXcI5Z2wAviA8OomA2I_9u_dCtxXhP6F3Dt2aKW0jc1Pt9O3xqaJbOBtq7JYWb45IU4aDmfzKCioAFwp7WgoisonxbRnpsHPmqW9FYPb5FicG5NGnYShtCtBN2qUiRi59EZBn8jdXpTAwxPjT48PD2_1c_V4Wi_sNwuxbzVv9LJO17DX-2IiwJjKekf0tdPlKsTn_9xF-hTH7jDzYeAA4-J5vUrABYbnaf2OWfH-fQt2P5VLGZ1N1Hd_jsEyl-WbhnSNE3V8CkaPfBjMXC0Ag1ar75O0vPiLM4iPYHtlHF6_D2ZcVLwSd0WRTvjapA8gsqUbTSF7RcCGTRgmMVYKSWO6ESKdh8gBUER1WZHe26KxzanMVYExA_-IeWAnZAVmMMu5jnktjkzkmdafSbPN6_QVS1YUc05RHswSYhN6FZ5FyJaVcA_83UbsBLh8fFuIqHkHQFMMgW6aK1wA468rCGDxPbxDlu9h_P725YSPqO_begANrqNkXmxGpuYZdl4oVtoVGEs6C_wtPBIPrmSxPg0o79K3N9xkKfW6c" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0fa071929.mp4?token=v0CRUNZPCgx6C58mb5rIqm6RHxTpWSfwQbIHXHsxEAIY99GKCaTZsd2GESFn2Pk8ITsH1QzYdYQw0qFg-8muGSORn8ZDytORIxD8NOoTVuK7ahoUSCKLHMQhby9Rpv0bXUzhmCJXcI5Z2wAviA8OomA2I_9u_dCtxXhP6F3Dt2aKW0jc1Pt9O3xqaJbOBtq7JYWb45IU4aDmfzKCioAFwp7WgoisonxbRnpsHPmqW9FYPb5FicG5NGnYShtCtBN2qUiRi59EZBn8jdXpTAwxPjT48PD2_1c_V4Wi_sNwuxbzVv9LJO17DX-2IiwJjKekf0tdPlKsTn_9xF-hTH7jDzYeAA4-J5vUrABYbnaf2OWfH-fQt2P5VLGZ1N1Hd_jsEyl-WbhnSNE3V8CkaPfBjMXC0Ag1ar75O0vPiLM4iPYHtlHF6_D2ZcVLwSd0WRTvjapA8gsqUbTSF7RcCGTRgmMVYKSWO6ESKdh8gBUER1WZHe26KxzanMVYExA_-IeWAnZAVmMMu5jnktjkzkmdafSbPN6_QVS1YUc05RHswSYhN6FZ5FyJaVcA_83UbsBLh8fFuIqHkHQFMMgW6aK1wA468rCGDxPbxDlu9h_P725YSPqO_begANrqNkXmxGpuYZdl4oVtoVGEs6C_wtPBIPrmSxPg0o79K3N9xkKfW6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بررسی اهداف احتمالی حملات آمریکا توسط فاکس نیوز زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68971" target="_blank">📅 09:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68970">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بعد از سیزده شب، امشب جنوب آرومه و خبری از انفجار نیست، و متاسفانه این آرامش، ترسناک تره!
#hjAly‌</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/68970" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68969">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzA5sHBWT2s0fEVI7C-ynJ-rcr7nF_9Uy38PWY02SZ4nPYxnQh5n-WgJVfK-bvyUcJ4QyQkZ632BfPqATQ0ePJyv3H1uMxLEeC6c_HkokVyCMK60H3NWA_uVAsa7HBzeIW18MWRd9x97N6DZYbt-79uVi_oX0eY-qjHoi46zPt1GI-FsukE0mZLBRS-WxkzQS2-32OQ6kqM-XOSNVT6MTHfGU2Pcv5YMKK2JlZe1mXUt1O8c34CO061g739E8SVJVeEobtczbGztfldWrMeAkCUaJtS4wAMZ_NVea1SauwoN0bs9tbrhyHYEbiaUCZEKrbMrPE6A4eqW-RB8GhYg4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه فایتوکس به نقل از مقامات اروپایی:
در اروپا این اجماع رو به افزایش است که ترامپ پیش از کاهش تنش، آن را تشدید خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/68969" target="_blank">📅 03:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68968">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=aJm2RKvtHNN_EKDCyUDpbUI1bgGs-omA63xX3cq1I3YeH2sOHdDCtnwIOX_RDWCjB-JA3FGWr3TxyrTzjXBSMvTKlAIWhHaeL3_wd0e2QN1Px-bYhZ4P93gr542z13xliytMpAPJTp0YzkR1a6fl-4hKqCuB1_Ck1QdFl2CjyFU0oTd72CB07FAq0SJgwpomdagUU_FhyvRscnPFtyu0-Dwcb3ZxPcqn8cWJQRodbwMKbowhtpw8xujyOHrzcQURRxcp1swdzGCAJ-wSre8-dwFIa6IFuSjKceeqaSA1jTxntkte9NJ39vCYj65WiZNALVYKNNMcpOBgFBURw8cK2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b03773bd.mp4?token=aJm2RKvtHNN_EKDCyUDpbUI1bgGs-omA63xX3cq1I3YeH2sOHdDCtnwIOX_RDWCjB-JA3FGWr3TxyrTzjXBSMvTKlAIWhHaeL3_wd0e2QN1Px-bYhZ4P93gr542z13xliytMpAPJTp0YzkR1a6fl-4hKqCuB1_Ck1QdFl2CjyFU0oTd72CB07FAq0SJgwpomdagUU_FhyvRscnPFtyu0-Dwcb3ZxPcqn8cWJQRodbwMKbowhtpw8xujyOHrzcQURRxcp1swdzGCAJ-wSre8-dwFIa6IFuSjKceeqaSA1jTxntkte9NJ39vCYj65WiZNALVYKNNMcpOBgFBURw8cK2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پدافند هوایی روسیه یک پهپاد اوکراینی را بر فراز انبار «وایلدبریز» در سن‌پترزبورگ سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/68968" target="_blank">📅 02:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68967">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA0ZdAg4mT3i6xKuUpcEwvbQa0vaC7lXCptkGd4S5KknE_viZ1rkJqdtsoY4b8Ifh1ou4GGuHM5YxkgIOUb3xHN2_WRSMd2MWYjr-qpIARGd1mPQufBktLpJmBEZZI92wksaQsP-ghiDFgxg4o53QGxonjIDx3s9KoaHNbJ64aqOnX9GNV4q-nBsnA6wurkCL7Y0RYOGCgMSDprBeB-QpoXxh0D1FK2Tcim8mlvjHd_XRhsUTbHp1B-3osZbx1Frrnuj_lPgMhrHKZZIusyFMwON59f8Npswy6UcP3L7zSAwPW93hw-qYRxcjHjC6QRuVdum0253ronNuOaWzNtzEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ارتش‌آمریکا: یک‌کشتی مرتبط با ایران که سعی در نقض محاصره دریایی داشت رو منهدم کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/68967" target="_blank">📅 01:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68966">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOuefJxmvrcuJBjW7ryef8iMhO1Su9bq-kgMDmgsXelS0KS10r2CO-4Xr_GZX5extcHrE86oa726FwatAa3yHfRhSTqV8t6dpCtu8j4aDCfNNj6xhYpfn5Awmm4Wp7zN5UGV8M5n27ap3ifHYhjb5eRk597SgvpTi9jP1Pw_BKZcKCI3ozbv6HYtd2GSatHmUdOk37xyPCqbTR0trbgIj4BhN235h5N6N0uOYC2BV2l4Ovsd03Ng7ui0fi30eyHnya2tRtR1Eol4RA_a3o_3hMYAW90UONnpcGRep_o83Wv8cWGIK7lESyCZyr9RE7WRji3rx0G7Y5tN6FK59B86Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/68966" target="_blank">📅 01:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68965">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poWhfSlD1siljrhp__2hJCTLZKBvAfjgGlMhyM2eNGZ9In6WSyM06jmTRb27XvujzxjVYx_yu2sKYkPBpb73dgK97iKUuM1xA4G_HPACPbvNr78id9En9O5OYo5W18eHTtUCYTNq2UPJ1pDgQ3oC4-VatFq_yYeo5q4xA9I6K6jW-mwhV4Ha1kI_WqjyA3ITZKBL0WOCcxAiXzTrLv4s5D3zSJiXBpC_Ms69ow3X-KhZaMqHcFQmYIJNS-0cMuDmqJjilznajOUoUXhWDHV8iOBdyNA1wOZuHM1mIBhD8dd7aGxdXuLDR0OXMWQ2pvHfG_1HWxLrVjF4E5ehArFo-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
رکوردهایی که ترامپ تو این مدت تو مصاحبه‌هاش ثبت کرده؛
«ما ایران رو شکست دادیم.» - 106 بار
«ما ایران رو نابود کردیم.» - 95 بار
«توافق با ایران نزدیکه.» - 88 بار
«تنگه هرمز بازه.» - 75 بار
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/68965" target="_blank">📅 00:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68964">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2Zs2L5H9LgpZ5pRawLERtRsCqC-J5qLLjCjKBZEduX2Y4HMPnY3gzW4Lk8xOsDSMgoahbeeDNPGZJWkcK-XJx2up6BIAd1Q4EeHqrMVQzhmj35Phj_Vf_EmiDdOsKBhSXQ1UYYtn_xFZFWuSElHTTsUeZOAhagA2-YXbQsOxK4Up5tctyc4yapp6WqR4KIiv-cNrfFG9FG9zO_O99854vljuX6X4tKFFzJ8WWP18dhV0QM9ZvTCJuynWgBSf8Rou-_CYjowS8kBVNPQX5JowXth_nR-rLsX5CZ02RNm47l7Th9o2peP1KNSxP0-jk9-RBQKXKys1skAcRKknMHh9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
عربستان دقایقی پیش به بندر حدیده یمن حمله کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68964" target="_blank">📅 00:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68963">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎙
خبرنگار:
آیا شما در حال بررسی یک حمله گسترده به ایران هستید؟
🔴
🇺🇸
پرزیدنت ترامپ:
"ما آماده حمله هستیم. ما کاملا مسلح و آماده حمله هستیم. ما با آنها صحبت می‌کنیم. شاید یک نقطه عطف وجود داشته باشد یا نباشد... در حال حاضر، ما به طور جدی با آنها صحبت می‌کنیم. اما به نظر نمی‌رسد که بتوانند به آنجا برسند، شاید اکنون بتوانند."
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68963" target="_blank">📅 00:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68962">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68962" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68958">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSmu5rlqHY99vC2mpi7UKlurndUX_Io4qIAyhZq6i0MuUYFa4QT9W8rAWzZ9TTdGQvPkOwJlOdhq4VkXT6gPLgVnAoKXfzLmSLscdOIqqs_FT_TFrU-IRGmBtosqk5SmU9t1iczsbNEKqb8kPTvuZj8mgCaC4BN3rLsaRkpGOkl1NtcY3TAPhgv83rHRsBy2tGZQOIHX3Y2VnoK3aoJzAD_D6Se6lcwIOxXJy-5BhdMJ6DTymNkuLSVyWJqXOxa3-kB9kngFvh-Kg-o3IliOCU5THO18oFBlRfbMks7ydF73JxYQMayI6KBvCTaDsJTriLImTCH1xBY_KKDNpv1JNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2ZCQdsy3_-HHGSkmV9H1h2-MtFAwIbSWRzecIWFmmPgnQzrKsHRStdluvcZfXx9tJMJNuDLi0M53KKws06gcNWZxvjTIqQqwAOdypTWPru5tfwvJmhA3gSHEbcck_g9YP9Uz8ysjkUBVloT5GDA3SFOT1A0X9Ao_D662iySbacLqa9RCCkgn2OqMsTVM1USzetOdddV5UP5Ob1cwb0q77_mYFtaV-dOkZotMffakLmZSI_KULTxDLxTfJHbAjdrzHiVGB2_ewkfkUopV5M1VZXY5Qh3UTEjsJ6VE8HjVRJelsUjBllB8MiitCec4TeUYm3QLQ1CXt-rO7HKWR-P_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=UEEGDWeyUCqD3dohRqqiVqdKMac1idme98X1pgkXmHtyjdYGAC3rJvouK3agC7zC-O-1L8IbQ0eL5fZdqLC7viUaXhTXVf-sF1VS0Ss9_lN7HQk2-t-wZ-zWkpVVOZOE_Urb9G2WM8_-_iB02uH9MnJWdnjvJAQHU_HrCC_cIXOOPgtGihcbRve_57rFESdJhQgGT1B87w4VjFPC_85MSDDU6Llq5RKQKibZD-qmhYG_GriiI844zAMFP5UNJS_rWii4Aq-4B0x0IW8UwmFp22gJtC6kT8dZkQdbUV1kPENhqEUhBrvh-RhNSes5vtNE8SZ89B6P831CtRYyQQSL7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123a793b7.mp4?token=UEEGDWeyUCqD3dohRqqiVqdKMac1idme98X1pgkXmHtyjdYGAC3rJvouK3agC7zC-O-1L8IbQ0eL5fZdqLC7viUaXhTXVf-sF1VS0Ss9_lN7HQk2-t-wZ-zWkpVVOZOE_Urb9G2WM8_-_iB02uH9MnJWdnjvJAQHU_HrCC_cIXOOPgtGihcbRve_57rFESdJhQgGT1B87w4VjFPC_85MSDDU6Llq5RKQKibZD-qmhYG_GriiI844zAMFP5UNJS_rWii4Aq-4B0x0IW8UwmFp22gJtC6kT8dZkQdbUV1kPENhqEUhBrvh-RhNSes5vtNE8SZ89B6P831CtRYyQQSL7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
❌
🇷🇺
یک حمله دیگر با استفاده از پهپادهای اوکراینی به مرکز لجستیکی ویلبریز (Wildberries) در شهر سن پترزبورگ، روسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68958" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68957">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=X30k46uH57t-34lHuz7lPD8cHikidBGyCSDThbIDuQt00dtl6J-GAgo1nnj95fmFmHmMOPDiAp--04tn-Gi5dQ70AUshwaQvVVIGGN6fWl4zCHIVzh-wtf2K5YGGAoJKuLPDxZ0f7GoGja3HJYz2paAH64YP1_MX644uRkXniKeX-9Gl6-P9-cep7DmlcRCqb_MCi4IxqQoD5Psky5EWRp4DJWnowhQ8dxFSDfzeVO5xZL_a3iy_qdQ5gYIPxgTcczzON0PPQFudYHZx_3dZMNwgn1yZbn1CCtMPNvXmJ034i41E0UMO5URMcnFOYIQDWBxIhIlGw7avOGfNoST7QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6ce9a3c4.mp4?token=X30k46uH57t-34lHuz7lPD8cHikidBGyCSDThbIDuQt00dtl6J-GAgo1nnj95fmFmHmMOPDiAp--04tn-Gi5dQ70AUshwaQvVVIGGN6fWl4zCHIVzh-wtf2K5YGGAoJKuLPDxZ0f7GoGja3HJYz2paAH64YP1_MX644uRkXniKeX-9Gl6-P9-cep7DmlcRCqb_MCi4IxqQoD5Psky5EWRp4DJWnowhQ8dxFSDfzeVO5xZL_a3iy_qdQ5gYIPxgTcczzON0PPQFudYHZx_3dZMNwgn1yZbn1CCtMPNvXmJ034i41E0UMO5URMcnFOYIQDWBxIhIlGw7avOGfNoST7QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ :
وقتی توی یه جنگ
داری قاطعانه برنده می‌شی
، باید چیکار کنی؟ دست از جنگ بکشی؟
ما با اختلاف زیادی
داریم این جنگ رو می‌بریم.
همین الان هم در حال مذاکره با ایرانی‌ها هستیم و اونا
آماده انجام کارهایین که قبلاً حتی حاضر نبودن بهش فکر کنن.
🎙
خبرنگار:
شما به آکسیوس گفتید در حال بررسی یک
«حمله گسترده»
به ایران هستید. نقطه‌ای که تصمیم نهایی رو می‌گیرید چیه؟
🇺🇸
ترامپ:
ما در حال مذاکره باهاشون هستیم. شاید اصلاً به اون نقطه نرسیم، شاید هم برسیم.
🎙
خبرنگار:
ایران کی بالاخره کوتاه میاد و پای میز مذاکره می‌شینه؟
🇺🇸
ترامپ:
شاید کوتاه بیان، شاید هم برن توی یه غار و همون‌جا قایم بشن.
اونا غارهای خیلی عمیقی دارن که می‌تونن توش پنهان بشن.
ایران، باورنکردنیه، ولی شروع کرد به شلیک به همه جای خاورمیانه.
اگه سلاح هسته‌ای داشت، حتماً از اون هم استفاده می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68957" target="_blank">📅 23:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68956">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=U9j51F5-DPH0-_mKbC2bGpEaCF6SH1cNc0r8Xlybkw07oCmWDqb2FwttQa_jzOKxjKMy-QMy2y7dUsrxRPu2RxJ2Fn-GB7wQgC23N4KrTTnEEafBJ7WsHksPLVlUd5tZzXGC6PjbTmD8min9JJFaiWQ71FVG5lo_qfwrm2HC4VKiuZMWSaYqOAEG-HWxoy-JsR6GTxWkzRUK0S9fqV6J483efVn3XQlM5LFD-fpP9LVMXhgssg8gRChT9qq6JCm89qf2kmb1i-IJBAG8-DMgXSUv1-F4_pzOSueezmbZJZjEdjGu0czFgmPizCpWKuj351gpyaqumdvMhOpm95PIew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07608d16b.mp4?token=U9j51F5-DPH0-_mKbC2bGpEaCF6SH1cNc0r8Xlybkw07oCmWDqb2FwttQa_jzOKxjKMy-QMy2y7dUsrxRPu2RxJ2Fn-GB7wQgC23N4KrTTnEEafBJ7WsHksPLVlUd5tZzXGC6PjbTmD8min9JJFaiWQ71FVG5lo_qfwrm2HC4VKiuZMWSaYqOAEG-HWxoy-JsR6GTxWkzRUK0S9fqV6J483efVn3XQlM5LFD-fpP9LVMXhgssg8gRChT9qq6JCm89qf2kmb1i-IJBAG8-DMgXSUv1-F4_pzOSueezmbZJZjEdjGu0czFgmPizCpWKuj351gpyaqumdvMhOpm95PIew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
یه انگل هست که باعث اسهال شدید مردم آمریکا میشه. کی دوباره میشه کاهو خورد؟
🇺🇸
ترامپ:
نمیدونم. بهش فکر نکردم. پیتر، زیاد کاهو میخوری؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68956" target="_blank">📅 23:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68955">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=Go00Z7hB1fbvJSW5VqC8gPzK4CmkSA6_guZcXOqVEy1S9ISK1EDboRbx7BbPl73FVQydtYXDg4kddjMzXG6v6uhD1NJxd48J2qJRME1rVY26_O98uRiCh7XEQUbv5ovrG6frUjYTZGVoCoEeWH0twY6RwSR8YJodv8Lql-2p1yb--t7_yC4jPjkDzLXy2NAPAKDbxOkbMK5wELWuz5bxBfeqeYwYRTC18onqNGQ2OKDEXK8pVYRCy7zh_7LVhRw2XHxcGA2LQ-NgTlHkRc3qiDx67eFcTI1VZxM-Mu0Esp1Iq75U1CiM6nVRwCTzFbO70ECSUdGbXRLB874ahcZEBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f8a8816d.mp4?token=Go00Z7hB1fbvJSW5VqC8gPzK4CmkSA6_guZcXOqVEy1S9ISK1EDboRbx7BbPl73FVQydtYXDg4kddjMzXG6v6uhD1NJxd48J2qJRME1rVY26_O98uRiCh7XEQUbv5ovrG6frUjYTZGVoCoEeWH0twY6RwSR8YJodv8Lql-2p1yb--t7_yC4jPjkDzLXy2NAPAKDbxOkbMK5wELWuz5bxBfeqeYwYRTC18onqNGQ2OKDEXK8pVYRCy7zh_7LVhRw2XHxcGA2LQ-NgTlHkRc3qiDx67eFcTI1VZxM-Mu0Esp1Iq75U1CiM6nVRwCTzFbO70ECSUdGbXRLB874ahcZEBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
وقتی من وارد ونزوئلا شدم، همه مخالف آن بودند. اما دو روز بعد، آن‌ها گفتند: «وای، این فوق‌العاده است.»
بسیاری از افراد همین حرف را درباره ایران هم می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68955" target="_blank">📅 23:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68954">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=O02V5BGyZL6l7bjJUTdGV0ukkAIwUVH4dF9FsmPuxtCOFrLACu2SUIUFnt5YKWF1l2ADQ2EE9GFF13cjG-VGVj6yD9_VNgV4ruMhMPT4SETfoyBcBwY1THmCZSnD-GkbgQaum2uzePJLdiy0TKIvmeVu66bOa6KB68_f-P531TDTlh7lPCUzA1wRL1ufJT8N0RIx2LqNembE4i_ZpE31Mx0IOWLmPGormKcoes-91GZmOu4GnFpJUFQ18b5TzmN698Is_WE1dVVFqBjiy-w1nMWZFISVZA4nx54JQyEBLs8JxuxJXPP9GUh6BMutTTRyOM6avm87nWctpKpZ43L7cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37416b7d0.mp4?token=O02V5BGyZL6l7bjJUTdGV0ukkAIwUVH4dF9FsmPuxtCOFrLACu2SUIUFnt5YKWF1l2ADQ2EE9GFF13cjG-VGVj6yD9_VNgV4ruMhMPT4SETfoyBcBwY1THmCZSnD-GkbgQaum2uzePJLdiy0TKIvmeVu66bOa6KB68_f-P531TDTlh7lPCUzA1wRL1ufJT8N0RIx2LqNembE4i_ZpE31Mx0IOWLmPGormKcoes-91GZmOu4GnFpJUFQ18b5TzmN698Is_WE1dVVFqBjiy-w1nMWZFISVZA4nx54JQyEBLs8JxuxJXPP9GUh6BMutTTRyOM6avm87nWctpKpZ43L7cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همین الان هم در حال مذاکره باهاشون هستیم. به نظرم هر روز که می‌گذره،
دارن جدی‌تر می‌شن.
من معتقدم
توافق، راه عاقلانه‌تره
؛ اما کاری که الان داریم انجام میدیم،
راه ساده‌تره.
همه‌چیز آماده‌ست و هر لحظه می‌تونیم اقدام کنیم.
وقتی وارد ونزوئلا شدم، همه مخالف بودن. اما فقط دو روز بعد می‌گفتن:
«وای، فوق‌العاده بود!»
الان هم خیلی‌ها دارن همین حرف رو درباره ایران میزنن.
به نظرم،
ایرانی‌ها تا اینجای کار از همیشه جدی‌تر به نظر می‌رسن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68954" target="_blank">📅 23:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68953">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=gJg2zOlx2gTIXkdvqnfJWIjjCrDTUu9c27SVRxVwO9nrIXTv3a2aDgaED2zGHPEgPICJtsgp45-zFZxOFYS2soXElJUwc8aa3luhrAbZstXmQfDGVs8YjM_zBlrteTpjUGgapiYRvV027nAoB1Q2Xa1rFnO9KVkhnEJeKsfar2d1Y-_67QIoi16oZZQYWQoO0mZz18_VZ-wVEIVUmaDowJb2kF2SqfsYJwnwTWeoEzA3SktmiZCPd6aPcMS44d4nTvVvvsP_wIQEgto-Oejl_shRNHsSJNx7PXie8g71ITHzTE_7qn3tJSiSjb96IURwejCgAI02Ye3BM48-Gd9xvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8206196a.mp4?token=gJg2zOlx2gTIXkdvqnfJWIjjCrDTUu9c27SVRxVwO9nrIXTv3a2aDgaED2zGHPEgPICJtsgp45-zFZxOFYS2soXElJUwc8aa3luhrAbZstXmQfDGVs8YjM_zBlrteTpjUGgapiYRvV027nAoB1Q2Xa1rFnO9KVkhnEJeKsfar2d1Y-_67QIoi16oZZQYWQoO0mZz18_VZ-wVEIVUmaDowJb2kF2SqfsYJwnwTWeoEzA3SktmiZCPd6aPcMS44d4nTvVvvsP_wIQEgto-Oejl_shRNHsSJNx7PXie8g71ITHzTE_7qn3tJSiSjb96IURwejCgAI02Ye3BM48-Gd9xvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما درباره بمباران نیروگاه‌های برق غیرنظامی و پل‌ها صحبت می‌کنید. بخش بزرگی از جهان این کار رو جنایت جنگی می‌دونه. شما هم همین نظر رو دارید؟
🇺🇸
ترامپ:
به این سؤال جواب نمیدم. شما از کدوم رسانه‌ای هستید؟
🎙
خبرنگار:
نیویورک تایمز.
🇺🇸
ترامپ:
حدسش رو زده بودم؛ نیویورک تایمزِ ورشکسته!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68953" target="_blank">📅 23:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68952">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vD8w9Aag3Ekffqatji8uB8LKeIMxSZGfALv_1_nfngQl049E9r5vd_v5-67SxhQN3_8IzphlcoIQ640W1j-JlrWj50xNsoqHtSgOi_cK2F4FTf5rspYCZYxuUAhExO-fJqwdpWOGFe2141QInZvufpQ9ZeZAODoJldACA8-Egbo27bUkPXOD_ZXPDVaR8mmwymKQGkBEmqE1yQVwm2j6xpx_fuQtMw5X1W1yi4SQZ4eTrih7fawIX9HTK2tSdudcxhVWX7e0c_XeIbSe4g4FKc00wVjToRjXF7ThdEPm93nY3wUZ9_lPFXdGtW1YDeBZ53OKpFSJWRa4CH_2Emp67Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
صداوسیما:
دشمن آمریکایی دو موشک شلیک کرد که یک نفتکش (یا تانکر) حامل گاز را هدف قرار دادند؛ شناوری که از دریای عمان می‌آمد و قصد ورود به منطقه را داشت.
نیروهای آمریکایی گمان می‌کردند که این شناور قصد حمل گاز ایران را دارد. اصابت دو موشک به آن منجر به کشته شدن دو تن از خدمه و آسیب دیدن موتور شناور و در نتیجه توقف آن شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68952" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68951">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⏺
ثابتی خطاب به شهریاری:
تو دیپلمات وزارت خارجه بودی چجوری شدی استاندار؟
اصلا بچه شمال شرقی، چجوری الان استاندار در شمال غرب شدی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68951" target="_blank">📅 22:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68950">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🇺🇸
نیویورک‌تایمز:
نهادهای اطلاعاتی آمریکا بر این باورند که رهبر عالی جدید ایران، آیت‌الله مجتبی خامنه‌ای، بسیار بیش از پدر و سلف خود به دستیابی به سلاح هسته‌ای تمایل دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68950" target="_blank">📅 22:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68949">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJARYmXyqOS8kjdjrbaXANHq4wgysiiFNZlu_jfQzpr2PpNG546ApNW78Vl3JbmSZY1Ok120hHHAYfZuFWDsCJi0t1kXoc94n9Zb16Veagykp9n-rxbk-pHLfa2XHb_ViDD67r3l_OgS4TbpCAFj2KSABULNO_SUPweB0zvbo8gMkSSW5WQQIEjsrIpu3YucZj_kVpoY5oNp18N6YaEonz0x77v1XMrgF6gDx5jaf_-YLmioZD8yJJi-XFNA6FBAAKqgpk2SBZjx5U9fYrHd553VIcWWP3BEK6qrzBb9eMsB6bZk2grsJ0HzkMpZvOZRdBGVg21VWqsHWV94uRODyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک‌تایمز:
رئیس‌جمهور ترامپ روز جمعه با مشاوران ارشد و اعضای بلندپایه کابینه خود دیدار کرد تا درباره تشدید حمله نظامی علیه ایران تصمیم‌گیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68949" target="_blank">📅 22:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68948">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TY5G4SQeVez-0HiH0spQjJE4P2FTtmAaFDOgpekwy55Azta4cOoqOLz3EHwXWTvnbZnkA4hXILDXV_KzDjkSAOAc3NTLkulRFqkAfOdrjuuY8Kx4d1DTJiOA2kcTG_k7Y-7NKO5OlH8247CXQqTVhb0M9b9d_yaxg3yfOLQD1fzfgeRv_H5YY1G9uPpVbW-wiWB14g4irfmWUZ4QThcn_Zjgml0TlO_69UgRaYFTyuBjNG9kTX515FF6QdqNUCJtB2sHE76tXVINiHGgIgpDXttqcmOpWwYIzZaNfFrqT65QHEzULu9URi8w9vxFKCYlOdNQA5i7W1OKdXx_bKRBvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68948" target="_blank">📅 21:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68947">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c449631.mp4?token=ZtUiC69KlmkM5eFI9XNzODsxRzIOAFt6NgPauiDsQn-TXWU-Jz0tcT7nap1tZqOw4gbagDCTKx3u5I2sJPdG36B__3rKKkOiiGO6Sp953IGSqOYmrGDgBWyOBNWXpVRM6rgT7TAihAa3up3llBuTJjGxSGMyBSO6ntd1ZMIpZlthws11jqsleO8pcj97yZrVBntpGwjz9sEWOGii9LxwyW_bo-ewDBubVj5EzaR9XySTyElFh3GkxSnpFoYUpdcjB7es-ZRtv3bntqjU8x1y3r-8OxrB-Y2qWx-Be1mzFvBXG77Ca4_5Na3Yua5iRcrHvQ97w4tBWo1AGwHlDe4cRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c449631.mp4?token=ZtUiC69KlmkM5eFI9XNzODsxRzIOAFt6NgPauiDsQn-TXWU-Jz0tcT7nap1tZqOw4gbagDCTKx3u5I2sJPdG36B__3rKKkOiiGO6Sp953IGSqOYmrGDgBWyOBNWXpVRM6rgT7TAihAa3up3llBuTJjGxSGMyBSO6ntd1ZMIpZlthws11jqsleO8pcj97yZrVBntpGwjz9sEWOGii9LxwyW_bo-ewDBubVj5EzaR9XySTyElFh3GkxSnpFoYUpdcjB7es-ZRtv3bntqjU8x1y3r-8OxrB-Y2qWx-Be1mzFvBXG77Ca4_5Na3Yua5iRcrHvQ97w4tBWo1AGwHlDe4cRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
آخرین مصاحبه اکبرعبدی با گریه:
ماهی یک میلیون تومن به خانواده ها پول میدن
وقتی روغن یک میلیون و هفتصده ، این یک میلیون روغن برای چی میخوان مردم ؟ برای جق جق در خونشون میخوان که بریزن صدا نده ؟
حالا روغن خرید ؛ باهاش چی بخره که چیزی درست کنه ؟
نمیدونم این خدا هم حرف گوش نمیکنه ، من با کسی حرفی ندارم فقط از خدا میخوام به همه کمک کنه
فرقی نمیکنه فقط به ایرانی کمک کنه
به هممون کمک کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68947" target="_blank">📅 21:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68946">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIFwfGJQ6zZrLooCbChEYQIuoxvHs9lHW5kv65CMJvkZUepM0-bfBAw_y8AoXdVD7YjeX1wCeprE4zvEMC11VAonY4pENahzUS3nLAiQbMhLIEF5uUhoKQGy9kBTfBmIUDUy1d03tt0YjjtDMsKxEAQW1HASuhiTGU77P5SSoKkhp_r9F6AmowcK0DlguaX6Sb-d79WKusz4ZbKtTer6fn9m4WhvQn0pjnXMfViIWnAHFNs-OJW6UBylBprMhXIv1JZ5YCnpuHXP77S0ikuwjswKkoIynBS4eYVbVK9nUwDMU2sXhoF1BLZB-93LUNc1te6tWWQ0khXZOlNNcUxPvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی، بازیگر سینما و تلویزیون، در سن 66 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68946" target="_blank">📅 21:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68945">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Geega17C5sERcwgArGYxWqACV8b2h4nY4oXg9lq_h0DbCn1gEaD-I7FAQQFYvogVUPLm6xXn1cjZUGdcXNwPeDifOE2rm1maAHOHthBzK-IlO2lLvYjoG7z7duCdcYndug8-AcjVoK_7FnJdZg7XcMxUWBnqrw9VYEUnQtMn6wfGBZ5frS8nR8WywwMjs2RmRG2UdB1bhqZIBmbsMeCUfFyKf7PkBGEh3mRSsr68DRbUqoOWGF1wjlOd58W3qC3q5dkOvN8624klITIw-nOZy_0sqWaMM2lYv9_iKGHnAvhAh9jmYWH2EVfTh6fV5bmtFD3kEWQ1TpLAFLTWyutHxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
علی عبدالهی فرمانده قرارگاه خاتم الانبیا:
از این به بعد به ازای هر شهیدی که از ما بگیرید یدونه امریکایی رو به درک واصل میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68945" target="_blank">📅 20:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68944">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2066d70166.mp4?token=tjrA5KpQmvFclnPbE0hrj26EIUVAjS3FhRAsBRvH14L8-k2ERGq8M0szGipy3szCTarVoik5ZWo2oVdvKSoW1b0-reRjqq8G5igqiu0RAKuwTnzvHuEsLL0PPmQOaxW1V3dDvGzG_qg18XwxqSAREuv1RnSLA3ZLFuUtPy1L8n5KggzbenxTCJ_rtwkjQVe9rhPk2LC1ojYAY-bSxxEcsbI2ma4tr7QMzKFEiid5EgUvQebnXrQ1rfEp6v6m0yyRqnvikEAU4YPx-uzpTnBrrxQxAtzJ8r8hzbcM9DctLSpMY6FGMJELcR3hYpIKu3SvbNrgWl4_8_G0PvQJwrWlBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2066d70166.mp4?token=tjrA5KpQmvFclnPbE0hrj26EIUVAjS3FhRAsBRvH14L8-k2ERGq8M0szGipy3szCTarVoik5ZWo2oVdvKSoW1b0-reRjqq8G5igqiu0RAKuwTnzvHuEsLL0PPmQOaxW1V3dDvGzG_qg18XwxqSAREuv1RnSLA3ZLFuUtPy1L8n5KggzbenxTCJ_rtwkjQVe9rhPk2LC1ojYAY-bSxxEcsbI2ma4tr7QMzKFEiid5EgUvQebnXrQ1rfEp6v6m0yyRqnvikEAU4YPx-uzpTnBrrxQxAtzJ8r8hzbcM9DctLSpMY6FGMJELcR3hYpIKu3SvbNrgWl4_8_G0PvQJwrWlBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما از یه بازی فکری رونمایی کرده که توش باید
بچه‌های جزیره اپستین
رو نجات بدی و ببری
بیمارستان خاتم‌الانبیا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68944" target="_blank">📅 20:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68943">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckkTTrATgO8F__NyFBpOt48NdCxTzq6s0yRGOeoujewB7iFRlSZbMGER1U902wCuWOcmfZxk993wgRfvC8FQRczaFf0ey0WjWYbuoPgqYXKihllIoLYfZKCw0-yl1B_K3C0pgPs5uUmzD9l85prf0Lof0QLFlc9rk-i0RsVdQE9qE1lEJ6_qBleMBOXctVhuLD7Q-amNu3G4rsHBAt0SDETYuLl-EA8ZZeVH810ls4J1eCuXXR2_5NvOPv1N-620KCQoE4ylrZq9Hzg24FVCFJ8_rULOfyOenLhRwjYkAvtpNL3w4Ec9yg6fsgsxt5d76iZgGuHbhCad0nLyYoanKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ:
رئیس‌جمهور شی در دیدار اخیرمان در پکنِ چین، به من گفت که تحت هیچ شرایطی به جمهوری اسلامی ایران سلاح نخواهد داد یا نخواهد فروخت؛ و این گفته شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، من به حرف او اعتماد دارم؛
ضمن اینکه خودم هم لطف‌های بسیار بزرگی در حق او انجام می‌دهم.
به همین ترتیب، رئیس‌جمهور پوتین نیز با وجود جنگ هولناکی که در اوکراین جریان دارد (و روابط همچنان برقرار است، همان‌طور که با رئیس‌جمهور زلنسکی نیز چنین است)، به من گفت که به ایران سلاح نخواهد فروخت.
او درک می‌کند که من به اوکراین سلاح نمی‌فروشم، بلکه به کشورهای عضو ناتو می‌فروشم. آن‌ها بهای کامل را می‌پردازند و من هیچ اطلاعی ندارم که آن سلاح‌ها چگونه توزیع می‌شوند.
بنابراین، به عقیده من، دو کشور عمده‌ای که اغلب در ارتباط با موضوع ایران از آن‌ها نام برده می‌شود، در این کار مشارکت ندارند. اگر چنین می‌کردند، برایشان بسیار بد تمام می‌شد؛ و قطعاً به نفعشان نبود.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68943" target="_blank">📅 19:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68939">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jFYHd8h3CFKsJD-uDB6LdG623XRWnPcp20kbn_mL3L0l4qcu6eqpZBTugN96xN6UHnvsje6GTj8clNMMu-vZFYfyMCMm11e4fF5CS2MoBsCjZ0Pn-vCyowoLhUPKnLR2rQCIAzq5TXyC6_jFaBYTFZgej-guOr6uBgWxQy4zw0UmR8RxY7loseQgd9MOCVC8dcHwIIYLjE6U5WSQnEIadUURPE_u1ad0dDj3XxNq96_JCIb9RuqEVVknNEHgsQqRkRGilyDNWSD4U9_lixcM2Cnu2ijyAdB7kRBKOtFvzUGwD2WEWsf1A6ws8rkd3GQd0QvMMZjONLGCgYc515n9ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k35E9yFNmPVWAgqdsdWGRHGXu_RUgzEkhf-rxT5OvWyQHFXb9QL2Y4jaK9Y3x13BjfcywUGENN8-tdeWRQVT5EHabfnIqWUy4NaG_vMucYFgxD-vtQq7-npr83xpqwSxs9J21GzfeyU0bvvDbWeq3Pj7qFs8aNRfFa6NQgMTY0dsTxeuIATqCgSw21p6T4g6eDpQeW03f1DYM5APDCtFHw_SW9Q6J0ZYaf62swIbGPcndINn8VStWaB80dZxXpw85HTqx5QwOtSuZn97QIsku22SAiRVqcxSdZMtvsc2kx4qAs4yGEvvNZoU3XqLiUsIR_Kq__oJDP0k1p1kMZnzkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vl9HtzFvyXsrCugxucVsaCBM28d__NFPByOlIinv8svT96dQ-NiGtnxf9C05dDfMoKg_310LUUfqlQ7dZbWhqxpi-DZui9DkUYjPQrV0U67Ufj7XQFya1qyJTX2VMx0YuuNGEWpfUpDkDWVWu2go8dfgkqm6IConLewoEjzo-UtnA33R4YHXLaeiGG-oaTt6nzA736o6uz2H8yaQAhVBPD6BnwxXrKONsDdyzjTKS2v3SP-0htPUbZGJwE8NdlXZNn7zYBhB46H5BbzYpr3WL_cSppvxVL5_PSHlondxxHw7ugDWOWtFXBxh7w3CoCcWBoYEUi-1y9Z6Myn1V7dkJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=l2ZypD-PtbFrczp4KiobDBt4MUf7JBkIGd38eS7e_zSY_KegfAO9D2u7pui9etJzuQWUoO84VXjTE4e0dL4s_IHHVdQcRXke_wel4pKM4RB2NklgwMeBgw5bsnhRVunOUmQYBPAlanFBTwVNmmffDQ1K3Qk5-UMtB--6tRJa5B1puF8Fl2Zb5SN_xSahU0zAeP3chzu9sJNonuMAReW1uHSm5rSeN07Qen45zanc5BpScVfNAZtFSB_FFU_tCGKC7uQZD_AUJdsiFF2BLQ40LpiHIIHm9AbuIGCJlzEpnC3M_miJ4z4EvnKI9GMWwORhsjeJUj3riLr6aGuh3RkxqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee9c5ea0f.mp4?token=l2ZypD-PtbFrczp4KiobDBt4MUf7JBkIGd38eS7e_zSY_KegfAO9D2u7pui9etJzuQWUoO84VXjTE4e0dL4s_IHHVdQcRXke_wel4pKM4RB2NklgwMeBgw5bsnhRVunOUmQYBPAlanFBTwVNmmffDQ1K3Qk5-UMtB--6tRJa5B1puF8Fl2Zb5SN_xSahU0zAeP3chzu9sJNonuMAReW1uHSm5rSeN07Qen45zanc5BpScVfNAZtFSB_FFU_tCGKC7uQZD_AUJdsiFF2BLQ40LpiHIIHm9AbuIGCJlzEpnC3M_miJ4z4EvnKI9GMWwORhsjeJUj3riLr6aGuh3RkxqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ویدیو ای از بمب‌افکن(B-1 Lancer)که گفته میشه در حملات شب های گذشته علیه اهداف نظامی در خاک ایران شرکت داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68939" target="_blank">📅 19:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68938">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=JrvJQB1tGtwAgQ_SzRBRSm97-jMywGbyap7ppU3Ywk7VzT3iGauav1bM3eq_kc18k6geNmGeIc3VljvjPsrmfLIusv18jXCSyAo78_TM763b05eyLpQxqjLvJ5hjWVEvMR-5ypOWT6g8boJ5kuV9l3gjohA-4FLyWQzgGHdNcEVvp_JpOCeJPXgnpxkY1nEZhMtj4PS_rpDZ8bcmOBZ85GoroPijgvU4urClOri2JmapalVMXhz14WbEh4WMwGRLuBIYyW3tCoa--49wjS46kCIKzBGV2rTiz3t7BU0FDhwLCA9GwMmcEyf7GYieb34rnZWJJbFW9my1uhxwH3VifQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecac465f34.mp4?token=JrvJQB1tGtwAgQ_SzRBRSm97-jMywGbyap7ppU3Ywk7VzT3iGauav1bM3eq_kc18k6geNmGeIc3VljvjPsrmfLIusv18jXCSyAo78_TM763b05eyLpQxqjLvJ5hjWVEvMR-5ypOWT6g8boJ5kuV9l3gjohA-4FLyWQzgGHdNcEVvp_JpOCeJPXgnpxkY1nEZhMtj4PS_rpDZ8bcmOBZ85GoroPijgvU4urClOri2JmapalVMXhz14WbEh4WMwGRLuBIYyW3tCoa--49wjS46kCIKzBGV2rTiz3t7BU0FDhwLCA9GwMmcEyf7GYieb34rnZWJJbFW9my1uhxwH3VifQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
در هفته‌های اخیر، آشیانه خصوصی وابسته به سپاه در جزیره خارک هدف حمله قرار گرفت. در این حمله، چهار فروند بالگرد آگوستا وستلند AW109E که توسط شرکت خصوصی بالگردی خلیج فارس بهره‌برداری می‌شدند، منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68938" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68937">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUc6RnZC3ENqmFHcWkrpjm72uT-mNlMcNaRJcXStoydA2zGetZbFc6Ishb1oVqzfR5cQs4MHZtLVFEEccvCMCPwd5a2Z1hJR9HATHiEa3MYVJES6NRhW7ecqXJ4288ApxE5eoZyNlnMofA5Ilv2sQovcMQTJ9Ec8xXjaAWQrdj-eqO3fRREwKhm6Xqd_gAaMlnufizivy-K0PcXuLIns3JStWjwnuo-UJLbWrniTYSGYlS98e1LghDJ-tGAQ1LP3mtavtfS_6r57lPxtc22jRSyAwXjO0F6ha1cmukS3fC7-B6J80Hkbp_I6x_9MswPznZVzqTFvGyjKb0bRqx0kpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رئیس‌جمهور ترامپ روز سه‌شنبه در کاخ سفید با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68937" target="_blank">📅 17:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68936">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887792c366.mp4?token=Axv4S_VNeegmNTbWCjmHcqWrV--0be8An2mdjf_QuW-8Kpq-j50729hpM79GhiBAA7qibh0LSCgL3Kx404Zty4psGhkqONOYgBYeeXJzw462E2Z4w2FpNomrPnWJPQWiSKuHc3khTgJAL8HT7p6DVL2wUGF00bwmFhuRo-qgenwyFuG0AQW7aQO2QtJeCGOGE4jO4A7_p5C6ytemPCkYpO4iu3jzLpZyUFIOfcEnMLKA6s-Vz_2e-UY-sFhLjoAIo9dJHFRFBxN1s8LFVouRlCO-iLuTW_CIekAJxTrX3-rjJZm9yrwhy7-30u-O2z1DsmOHoLZQJ3lxaIWGpRE4mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887792c366.mp4?token=Axv4S_VNeegmNTbWCjmHcqWrV--0be8An2mdjf_QuW-8Kpq-j50729hpM79GhiBAA7qibh0LSCgL3Kx404Zty4psGhkqONOYgBYeeXJzw462E2Z4w2FpNomrPnWJPQWiSKuHc3khTgJAL8HT7p6DVL2wUGF00bwmFhuRo-qgenwyFuG0AQW7aQO2QtJeCGOGE4jO4A7_p5C6ytemPCkYpO4iu3jzLpZyUFIOfcEnMLKA6s-Vz_2e-UY-sFhLjoAIo9dJHFRFBxN1s8LFVouRlCO-iLuTW_CIekAJxTrX3-rjJZm9yrwhy7-30u-O2z1DsmOHoLZQJ3lxaIWGpRE4mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
❌
👑
مقایسه تسلط زبان خارجه:
وزیر امور خارجه کنونی دارای دکتری علوم سیاسی از انگلیس
با
نخست وزیر ۵۰ سال قبل ایران دارای مدرک کارشناسی علوم سیاسی از بلژیک
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68936" target="_blank">📅 17:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68935">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=Cr6SX_VNaC4_hC5z1wd8wNoSWIKMeEc-ucHRk9cck_OprkPBKU96zZesN0sdXbqoRBnBjH7uhsRHkppSz5_GrhT-a7Gopz-rn35pzjqPknAxPhuK7kAgrjLxGLLPsMrVlFcAVtOtChfjZ7nS_FgDUPOkiNN5oKijwIrZ4c_izej1uDfaxuZbipfzVtYZ-nA8W_Lue9cYRSFo7RK6F3eHgXcsOljuKnMUQ1F88v9mI1WCkWiau1c2K9KQyoLi6dD9cJjeivoA9bX0FEsS_PlCAku6vu7BjF5yxBtyL1wak0imKe-PSUodM0SVeIWgz--gYp77F7pQB16aolzsCY661X_JYPGEdAGkVUzpGlwBUYk-0qvrEX5a_-P8oT4qTtb8TYi5LhWtcKvfabePCI8WpZ7syfDamQANBaIUQh8Z7dolP2U2mLJE_0D3WvVR87DTaAASpxiUnSjqCxCjSRMLKJvVNrWEBUf9N7SN8DKxqcdtbRVgnGGbfrw06hMxLNsboSSFx3r9jo1-dHHEiCnw5cxFxkG_ZE_Pw_HD1vYAFB4wm9LYo2UnZO9h4vQFUjPkBCQuGDjz1J7AO8bjKGj_o_96Ytn_ivNpusFmxZdU-v21tNuycpZT0bz05GBX72CTzPShCIjXEuVkx15TSNBcZ2ezWJwqmnB1vhIsH1eUvTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3860b62c.mp4?token=Cr6SX_VNaC4_hC5z1wd8wNoSWIKMeEc-ucHRk9cck_OprkPBKU96zZesN0sdXbqoRBnBjH7uhsRHkppSz5_GrhT-a7Gopz-rn35pzjqPknAxPhuK7kAgrjLxGLLPsMrVlFcAVtOtChfjZ7nS_FgDUPOkiNN5oKijwIrZ4c_izej1uDfaxuZbipfzVtYZ-nA8W_Lue9cYRSFo7RK6F3eHgXcsOljuKnMUQ1F88v9mI1WCkWiau1c2K9KQyoLi6dD9cJjeivoA9bX0FEsS_PlCAku6vu7BjF5yxBtyL1wak0imKe-PSUodM0SVeIWgz--gYp77F7pQB16aolzsCY661X_JYPGEdAGkVUzpGlwBUYk-0qvrEX5a_-P8oT4qTtb8TYi5LhWtcKvfabePCI8WpZ7syfDamQANBaIUQh8Z7dolP2U2mLJE_0D3WvVR87DTaAASpxiUnSjqCxCjSRMLKJvVNrWEBUf9N7SN8DKxqcdtbRVgnGGbfrw06hMxLNsboSSFx3r9jo1-dHHEiCnw5cxFxkG_ZE_Pw_HD1vYAFB4wm9LYo2UnZO9h4vQFUjPkBCQuGDjz1J7AO8bjKGj_o_96Ytn_ivNpusFmxZdU-v21tNuycpZT0bz05GBX72CTzPShCIjXEuVkx15TSNBcZ2ezWJwqmnB1vhIsH1eUvTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عباس:
چهل روز جنگ و محاصره بود هیچ کالایی کم نیومد
بله قیمت ها یکم افزایش پیدا کرد که طبیعیه
یکی از مهمون های عالی رتبه ما اومد ایران و تهران گفت من وقتی شهر دیدم تعجب کردم
گفتم این همون شهریه که جنگیده و محاصره کشیده ؟ من فک کردم الان بیام تهران شهر مفلوکیه
همه دنیا داره به ما احترام میزاره جز خودمون
من رفتم عراق حرم اونجا استقبالی که عراقی ها ازم کردن عجیب غریب بود اونم ساعت 2 شب
این استقبال از من نبود از وزیر خارجه جمهوری اسلامی اونا به من میگفتن قهرمان
عراقی ها این همه شور و شوق داشتن اونوقت صداسیما یدونشم پخش نکرد
یه نفرم اون وسط تو حرم گفت مرگ بر سازشگر
با مرگ بر عراقچی مگه مشکل حل میشه ؟ من اگه وزیرخارجه نبودم باور کن پشت لانچر بودم الان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68935" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68934">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🇮🇷
تسنیم:
حمله پهپادی به مخازن لجستیکی ارتش آمریکا در صحرای عربستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68934" target="_blank">📅 16:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68933">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ubj6I0CMXC78sQU48HLMLtWdFyAqlJMYRD9jUHHdgx27dweQa2hCKy9ILW0gM9O_GW2intMov4FFXveyMQcHX1dPiYVTcBgiEWiuCq0CL9JLbAzqNs3lkCZ6PKVvOOhYs0ZpufLt36h6tShWmAwGC1i40Nh2NYS579q_tDZjgMSrllUmFoQuHjunHwa1tMklrQzHlstGgJgf6hfSJfxFo_heXvLFAHgWk_bKy7aqNpf3QjyfmC2KBjFDSexwwxYdlA2yUXA5IaaVfOYr1PIBbRLOE_KyjITo8felhBkGemszxF13RGUiyy61uCaF7dt04SMCTrD-4JAa2FMdA_JR-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت حساب وزارت خارجه آمریکا؛ سیاست رئیس جمهور‌ ما:
یک سر در برابر هر چشم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68933" target="_blank">📅 15:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68932">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csRRYK9VpjQab_EEv1PlfhRYbHDbeboOfVPgEJM7Aq3ATq-be_GrMOeYra1yK7JC7GoGfrbI9ChzTOPzqG3tRdBGJRniSptjWIjKBEi-lkLo2U-YI6YwrAhCdbvS9m1pqQnQDLeMg2S7bzDCiBqdAIH16Oy8jWZfzoDu9WStredKbWP22xd30YLlEVKuBGtCTY_XEpZN8l3UyCP5XTQDqsPwgbyUNoX_DltRxZUaTxQ0O7MYblQ4obagJhE20hY_m_6i3TMPmoOsMJCMpH2HjwRDcwY8NA5pOlxLnFw7UQIphDtrcFlgU7JLleJe_w58v1h6eDJX9lAPGSv5n1CwDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
وزارت امور خارجه آلمان اعلام کرد که این کشور فعالیت‌های سفارت خود در تهران را کاهش داده و بار دیگر از شهروندانش خواسته است که هرچه سریعتر ایران را ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68932" target="_blank">📅 15:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68930">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jfo28RXyf1-sPPtdFHxfqqgH2HYFJxNMYq0ty0T91Ax-zI8WsbtnU0EzgvxQ7hw7ubDp5CRx4Lm8w_DQPskBYJrmFxtd-F40-hkg-Qk1LcynRqkiFYI7Z7vH0pIXBsTv-5jA9H3FqexZzq6O3PmcHe_MFHGMycTI7cRI3w4IbPiuW08IgPFZhNWyuqTUUEFY8HFk-LyS5su8GtNMr_9KXIe7O8w9bfJBc4lGS2PloM0oSpYbDZhd1nBTYgMI9eXwVhmqdjC4-i6rckbzeG6L2nWiZzKYrLU1CIGPxcXkqg44CXpmOiVCULyoBSGxpvszQQtrtPRV3uESe0af_K8pDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EGJtkHK0MecAG2yvKLVu-6vHH7vap5KWnce1Ot0Ep1GMI1Qi4QKe8q2L8CxHQkxMBvXoVrhiGcYWyj0--DHAtjAZ-_PJV-VHlsjhRwPABYnox7MFzTfyQpvLayjmEik-M4X60g29aagowgQqtCVCmmeJRV-FRSRpOHm70JgmNBDvIkWFFhfeCK5TG5rUEjXqb5s-M1EmSF_d_6hNu7Y8LW6rBE7l_nLnvO39oiXgQ1-DneJGtZTrw_cBQlD2iCW14E-banx_f44sQllp8rj71ifgADSvYH8kCyKShCKV4JsP8TbJK-2_EjYUY864gOuO_Eu-rmmSRM8SuSIHGT5AuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
تعدادی از هواپیماهای تانکر سوخت‌رسان آمریکایی به پایگاه هوایی شاهزاده سلطان در عربستان سعودی رسیدند، این هواپیماها از آمریکا به این کشور آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68930" target="_blank">📅 14:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68929">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=hULe8yLzGZaPfYL2Y0ycALhmgQp8ijgbDoF_KiaXyBmf8A-5g0Iv2VwB7Fcj4522B7S9z9MgBZ9FMuoSmxkmocIspG1C-WybY3opzm1cfg4PjUVXXnxE2bnxTnglMchVrDdkuOuKQ28M8LlsryvX6hu-ttD17PwXcfIpO74OVxrKEmyk4_dL4sqjwWrRVbGnbhV9p4uHR27a-8U8Gbehbu9l4enS0I95s2qLo7VieAKybzRsVSWmczralbMA8j7Tp5sC12jALrYXIuzG66BQS_TV4KUD85_t-7HpAiA0TRf9AuIcNaYe6Q7cIOsvSNNZABLfVUYHwQP95N8kpVPxGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46bb7d382c.mp4?token=hULe8yLzGZaPfYL2Y0ycALhmgQp8ijgbDoF_KiaXyBmf8A-5g0Iv2VwB7Fcj4522B7S9z9MgBZ9FMuoSmxkmocIspG1C-WybY3opzm1cfg4PjUVXXnxE2bnxTnglMchVrDdkuOuKQ28M8LlsryvX6hu-ttD17PwXcfIpO74OVxrKEmyk4_dL4sqjwWrRVbGnbhV9p4uHR27a-8U8Gbehbu9l4enS0I95s2qLo7VieAKybzRsVSWmczralbMA8j7Tp5sC12jALrYXIuzG66BQS_TV4KUD85_t-7HpAiA0TRf9AuIcNaYe6Q7cIOsvSNNZABLfVUYHwQP95N8kpVPxGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی:
کتاب نوشتم، «قدرت مذاکره». نتیجه‌اش هم داریم می‌بینیم.
همین دیشب یکی از وزرای خارجه آفریقایی به من زنگ زد و گفت میخواهیم دیپلمات‌های مان را بفرستیم ایران، برای آموزش!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68929" target="_blank">📅 14:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68928">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
«به اطلاع عموم مردم کشورهایی که پرسنل نظامی امریکا در آنجا حضور دارند، می‌رسانیم که برای حفظ امنیت خود، باید فوراً از مناطق واقع در شعاع 500 متری از محل‌های هم اشکار و هم مخفی حضور پرسنل نظامی ایالات متحده، دور شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68928" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68927">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gA5-fEOTjdbSjKAn_FCRCBOiD85UnpsCwiXabdRcLd_2mWLAhOjGfAQDwqwTy267LlcVKtJZjnnanplFr6WkRS7IFE463btW_EMok2BLFK8Rk_67WeGbAr6z8sgAKZQnoYQtd20r3wrOhH0GzjWr1ori6RN9WJojgo9qnp9RUNy-L9LmRaFVTVJik96FjHz7oGA9D5i5yG8hEOW-WSzXZLRqqNZgo8AthUeoKt0Hd2Fw05BwJFedFf0Ycjstm3S5ar0yTVCjBh4h-qt-Puy77YSAI7sGF-V3KWYW7Q0IHWVYBd2aepDAFtrrEok8iDk-8YzwhDtDP0v8HK98kZ2afA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مناطق هدف قرار گرفته در خاک ایران طی حملات شب گذشته امریکا
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68927" target="_blank">📅 13:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68926">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDa1MlzB2v_G3eoZKo8WC1T06juhA_3OtxDf4y9kPuHbHHMiiMyHRkbZEHGTBQngBLIJTywzJKnpxPWywFPAcCaEjFn4eHLa9iCPKGH3oaBDUABkehc4IXkWDgLo9jrNBtLbJjJesmGnhrzVnuEOfSixRF_htgWo8sz7wSmYIei-jbc5r0VLTbVF-zLOC5OVu6ZHEdnW3fBn9tSuLwq4pn9EtmvmXv6k1HOuNjJnxJk0wlSDQ9xKug-jjJyjD6k_SIxT1sco_PR_bvTsd_lWXA8MUuJrjeXZ_kc-_gHHcf-Prx-_NWa_NZPCFeJ8OdfK44ZwPcjljnrF4uwPtVMjuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
جیک تورکس خبرنگار یهودی کاخ سفید:
نمی‌دانم چطور بگویم، اما من در خودِ «کاخ سفید» کار می‌کنم. از اطلاعاتی آگاهم که افراد زیادی به آن دسترسی ندارند و با اطمینان کامل به شما می‌گویم که آمریکا برنامه‌ای برای شکست دادن رژیم ایران دارد.
آن «کارشناسان» حسابی غافلگیر خواهند شد؛ هرچند بعدش وانمود می‌کنند که از همان اول هم می‌دانستند، پس... بگذریم.
به هر حال، خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68926" target="_blank">📅 12:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68925">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=bDqKg5yeDeYp1bhcCRgYz2WWEl2CuhAlTibZgeApadDnVzTN2NDWxCOzWK_8PmrN4crw2oIYYzhp13LAexi_YZLbfcnX2-M95-iuEZYPYRhsQcisMhhl6BvnZZetgxxhFRtBvP-mwoCffhS0r05LIZdYdrrCM3j2zqMXCX0CRxfYHsidkI1T6x1XsWMTDUw2wlhsRZhdvutzUyQJ_7VW-Ak9ja4kzi6v0ycYu6SFV4EjnW7ZQtQMAdgjoy9ceW983GiKIQ2cd1vd4CG935AAyjmawyLXG8RzowJyWaAIbS95OVdZxPXPLHeTicqhMKtV-Oejf--npdkjU4u0qEFZcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/899def3cc4.mp4?token=bDqKg5yeDeYp1bhcCRgYz2WWEl2CuhAlTibZgeApadDnVzTN2NDWxCOzWK_8PmrN4crw2oIYYzhp13LAexi_YZLbfcnX2-M95-iuEZYPYRhsQcisMhhl6BvnZZetgxxhFRtBvP-mwoCffhS0r05LIZdYdrrCM3j2zqMXCX0CRxfYHsidkI1T6x1XsWMTDUw2wlhsRZhdvutzUyQJ_7VW-Ak9ja4kzi6v0ycYu6SFV4EjnW7ZQtQMAdgjoy9ceW983GiKIQ2cd1vd4CG935AAyjmawyLXG8RzowJyWaAIbS95OVdZxPXPLHeTicqhMKtV-Oejf--npdkjU4u0qEFZcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حملات ایالات متحده به ایران برای سیزدهمین شب متوالی ادامه یافت.
در این حملات، محل‌های گزارش‌شده‌ای از موشک‌ها در یزد، انبارهای سلاح در اهواز و چندین نقطه دیگر در مناطق جنوب و غرب ایران مورد هدف قرار گرفتند.
در پاسخ به این حملات، ایران صبح امروز چندین موشک را به سمت اردن، بحرین و منطقه اربیل در کردستان عراق شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68925" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68924">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=kJCBOcD6WiMP1vUVMOLjZXYEjSkAKM-lHTjffBuHxojRCd-LG5UoNa3DHGdPNdDxbhWjmWeoa3M72rut_Tly675E0rPAtw92qF7YHHeyGl1-4o7AMLrNemhZYc92-LcBvxQWkkujIFg0l-EQ2YJH2lHEVHLThaXrBCzWxaZgI8LvW-HDnWixCvvQgFo6pivdEaBcvA1lIJGoo2enR1GsUeN4FCd1ODMggJu6vaZn_HqfGT_jXZVjC8S7XdkNP-PQDzpwj0IXlJTXbTP38TAYu9fvsNSmREjO_VVZ47qBqe3ar30rJNm5_KzzDs4UI8bPjaV_MynKKQM7Gtuy9PbyXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9dc866f375.mp4?token=kJCBOcD6WiMP1vUVMOLjZXYEjSkAKM-lHTjffBuHxojRCd-LG5UoNa3DHGdPNdDxbhWjmWeoa3M72rut_Tly675E0rPAtw92qF7YHHeyGl1-4o7AMLrNemhZYc92-LcBvxQWkkujIFg0l-EQ2YJH2lHEVHLThaXrBCzWxaZgI8LvW-HDnWixCvvQgFo6pivdEaBcvA1lIJGoo2enR1GsUeN4FCd1ODMggJu6vaZn_HqfGT_jXZVjC8S7XdkNP-PQDzpwj0IXlJTXbTP38TAYu9fvsNSmREjO_VVZ47qBqe3ar30rJNm5_KzzDs4UI8bPjaV_MynKKQM7Gtuy9PbyXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به اسم ناصر نوری گوشت سگ به مردم می‌فروخته!حالا مردم متوجه شدن و مجبورش کردن خودش بشینه تمام گوشت سگ‌هایی که داشته رو بخوره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68924" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=eL-2RCnZCwa-Nebh5XU41My3IqaFRx8_v4PJyEcwPSaD2VflPLQLT2BPeW10Femb7jVfZywmqdqP4hxtaJzTItufNcfBriIGoR92WfeI_2aDGP9nVD-e1BQ5rkFwoHlhGJp41rIRUExGtWWbVUeDT-x_FCLulA4FsrXsOqV1_HRVWoMOCoRRIuZOJ_t5LgnapWReP3IlOm_vHpjG39RyCsyGZB9m278ImduQplctkFspNXUTHaH7CX6fKtQkNkd5HUT-9hPYmq4kxobEMmEr36TbFSLIshSmBVKFbquj0ALzFrirXBZR5qdrfmuVWvZ_eUtzyslZz6csNeSz8DEgqIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=eL-2RCnZCwa-Nebh5XU41My3IqaFRx8_v4PJyEcwPSaD2VflPLQLT2BPeW10Femb7jVfZywmqdqP4hxtaJzTItufNcfBriIGoR92WfeI_2aDGP9nVD-e1BQ5rkFwoHlhGJp41rIRUExGtWWbVUeDT-x_FCLulA4FsrXsOqV1_HRVWoMOCoRRIuZOJ_t5LgnapWReP3IlOm_vHpjG39RyCsyGZB9m278ImduQplctkFspNXUTHaH7CX6fKtQkNkd5HUT-9hPYmq4kxobEMmEr36TbFSLIshSmBVKFbquj0ALzFrirXBZR5qdrfmuVWvZ_eUtzyslZz6csNeSz8DEgqIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=FtxUjUtr3OMTJro_311t3cNgZgL5aBJC3zg1xMuim9eujFzGpUMueldj4_OdWCxSbjnpZ8fxiyrrYkh1VpolDzL25CvJTAqrNjnXIvbKP8G6Lfas2QmUC2seTX6hUfR7rSSUZniPOONcAjL06Mh9ytmdspG-7CDMtCMe_SlVGQJNm2ddFZf7f0n8CIQiXBbyXHmbFscpgIzylAwIqZObl_Hq4IxDLh9O0rlyYQ2cH3dHjAk4IxG8UiqUQJYxMTt2c7srojExdfZdB0BmAX8PKqb3Fi4RHBcNN5drU2tErds2-QivJ5_cBocRofpnPAgkaGa3zPcgHQSQag4HmPhzuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=FtxUjUtr3OMTJro_311t3cNgZgL5aBJC3zg1xMuim9eujFzGpUMueldj4_OdWCxSbjnpZ8fxiyrrYkh1VpolDzL25CvJTAqrNjnXIvbKP8G6Lfas2QmUC2seTX6hUfR7rSSUZniPOONcAjL06Mh9ytmdspG-7CDMtCMe_SlVGQJNm2ddFZf7f0n8CIQiXBbyXHmbFscpgIzylAwIqZObl_Hq4IxDLh9O0rlyYQ2cH3dHjAk4IxG8UiqUQJYxMTt2c7srojExdfZdB0BmAX8PKqb3Fi4RHBcNN5drU2tErds2-QivJ5_cBocRofpnPAgkaGa3zPcgHQSQag4HmPhzuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=FRBQLidxoYqO6ofmTQEB-oXFvC2qdAb_Mq2Oii0-U9Q1fdvJwlEr9sAzGOwIU6vD6EAinPpyWs6jDqtiJBIthZiaaTQ2pt7CtY87EHnFe6Ttx15bBGb1S8UjdRguyX-c1ac4T_FCIVWzkI0kQTjCMbxgcVs1qQ08XP71XcA37Q7TbOuvm7pHPqofhn8EyIMLljKDgHsEz7K9Uv9pZv0Nx5QYD1dsg3p9Yqc_iPSZbLyTH6M7PBhpFZk6eJN47ZsbhVBcsfl7jRPnJusoBOvA0g_Wv5O3FzPmNzoBNvqgbS_C4t-etQlWX_ZzleD6DYIVBbvOrApB7rjG_esCt0iFZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=FRBQLidxoYqO6ofmTQEB-oXFvC2qdAb_Mq2Oii0-U9Q1fdvJwlEr9sAzGOwIU6vD6EAinPpyWs6jDqtiJBIthZiaaTQ2pt7CtY87EHnFe6Ttx15bBGb1S8UjdRguyX-c1ac4T_FCIVWzkI0kQTjCMbxgcVs1qQ08XP71XcA37Q7TbOuvm7pHPqofhn8EyIMLljKDgHsEz7K9Uv9pZv0Nx5QYD1dsg3p9Yqc_iPSZbLyTH6M7PBhpFZk6eJN47ZsbhVBcsfl7jRPnJusoBOvA0g_Wv5O3FzPmNzoBNvqgbS_C4t-etQlWX_ZzleD6DYIVBbvOrApB7rjG_esCt0iFZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جواد اوجی وزیر نفت دولت رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=hfYR5cJxhoCRUCef2DuIn8ew3zbi8MbZtsJJfV9ykrKg0LAY75JPVX2bivZyQYUR_n24enxm1EKJPKs1960G7w7pqahcpTPGEZexcLHO5kPIknxSSBriLaVQIApFJ-aY27gXhnlv19Eu3E9603VbXUkoma6oVNMmllmWh77AEhqFCO-_cH8QSu7HB5dNQjxFN41eHQzMpkAnVpMhXvu0Njp9xureAEnyCb9ICMbiJfzEekIxBGJMzLhWYTEbKVzy1led6zw6tveSpUM-1oMU9tTqOmsYG-_MvIDJrQi7Co811_8PFSgVO4ASCBmLov_ZAajPINlnGHX_5VVzTTBfsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=hfYR5cJxhoCRUCef2DuIn8ew3zbi8MbZtsJJfV9ykrKg0LAY75JPVX2bivZyQYUR_n24enxm1EKJPKs1960G7w7pqahcpTPGEZexcLHO5kPIknxSSBriLaVQIApFJ-aY27gXhnlv19Eu3E9603VbXUkoma6oVNMmllmWh77AEhqFCO-_cH8QSu7HB5dNQjxFN41eHQzMpkAnVpMhXvu0Njp9xureAEnyCb9ICMbiJfzEekIxBGJMzLhWYTEbKVzy1led6zw6tveSpUM-1oMU9tTqOmsYG-_MvIDJrQi7Co811_8PFSgVO4ASCBmLov_ZAajPINlnGHX_5VVzTTBfsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VH5t-MsJerd292TMcrcG5hZcv7Zxh9dG0tlWukwGHtDAT1eWeMNi65kP87oGiNVjVeeWKJ0nBQSLmmjiIO67I8NP8o38F-nZI_hHlY-wffVBoz1p5wd0Iv74hEqRZWWJ03eFyTkLQTfgc9EkAz8H644QdCx2yOYKKRCG-8oPzfNi99Mr1A8SGDrhHHyNNAMNmkfvB-GWxcyQKahYEHzNTcyLDHFUHVXBnvw4xZg6uQR7mUoqy4_X0o9NiOqyO5Te3sjz9BRRjKHXlu9UmBBkUhelut-9iDagQpzIhcFLmqjM9YKSOQ-QwgEgd8lz7BP0u3TIpoPnff6TZULWifGF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKg7Uq1BsXArbrCIG2ouOfEHug5SuRRpaklYBLoKnXNo5vdkVCm7QWs_hlh63sf25ffPXh3CEInU7rGt6nlorFobujSvJm_xRXO7E3cCp9RV3qvyXs8rxAB21dE4YfHM4Kp2KRn_4AwYD6vX4V-gAnUYOHB1dQ6oIalAH21FXpLiv-ihAQ9iLFVc5IFHBNbiWMj4Yp-l5i20gGAwXqjFQnAAaUGKmG55hVl_uNliJtxn85g0m_CsBlSCogF2ep3bxeVY7e_cWOa7-KmHu2uutIFdAuvjmyad0ynonW_4_JEumL6Nl2XXb9f0cha_HOokbDOBo9-OLFcZOSJi6GTdow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68914">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkmjig72srtSxQ3spnZwoWo_p1RRVmwEvO-IUZEvF6-GfnfjNMCa9yvLQYC_7PEbFQAwkbO8-hmqoMU3yiyC2mvbNbiejoWzqYV-uCfrfZTaQQvmP_yQdB6A8pGkgGpZ8KDdJF6oiPtP3lESJS5nS1EPA5dcbahlWwYYp2sj-6fRyzzTKsLZWGF0z0Kdmjx_3lbXG9CAozh7t2wwRPKKZsN8OPjBoztvzLwGF6-CNhBqfRlJWPiH2MT_QJb3fkiQi77iK5gVnQc8-Veq26mtCUQFW9vbqjG8fRJaWYDG_VUXUNxJTNRsRJX1K_me3tg4Ayljy_aCBw1EJAn29DoYFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=nVEpT5QM9hZPQscBfNVOtOTHJxCcht69lIVptnZ0YNm1CaSqIdoKrBan9I7o9uL0xmeFAzGLyhjJk0i8Ma_yRGvKLRMpt7mXI0Nj4SoVjXrGYLzPV1alJe2WJeIjhuVocAEVMGdrF5Yp_LtL_4SAWAUDtAc-YhreyD1n7ng9hKgh5oIsQzqD2WDjk8_KYde2ftx--DO1Wu-w0AwFUX5WoatWkZktWXqZsdP7J32Lvrz6LjsBvvDKrmR8hzmp9QstSKkaBDSdwnTraHttswhcI2IIifb05MFK4eINoRxPXJAyl0N1So_VyFWrWSOPUpibTyrNpo3m7sR6wPpd1W157Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=nVEpT5QM9hZPQscBfNVOtOTHJxCcht69lIVptnZ0YNm1CaSqIdoKrBan9I7o9uL0xmeFAzGLyhjJk0i8Ma_yRGvKLRMpt7mXI0Nj4SoVjXrGYLzPV1alJe2WJeIjhuVocAEVMGdrF5Yp_LtL_4SAWAUDtAc-YhreyD1n7ng9hKgh5oIsQzqD2WDjk8_KYde2ftx--DO1Wu-w0AwFUX5WoatWkZktWXqZsdP7J32Lvrz6LjsBvvDKrmR8hzmp9QstSKkaBDSdwnTraHttswhcI2IIifb05MFK4eINoRxPXJAyl0N1So_VyFWrWSOPUpibTyrNpo3m7sR6wPpd1W157Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بندرعباس؛ امشب
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=vDvNRP_WoKyuo2ywRQJcA_TrHzgs-bHudcWBh-GQj-_rad2FbqMtrSkNDdcUBMyXAvdgUZXZKu6mnv6aK5FpgMQhpYUVtMAw8uGq3p8j_V7yaUmM0-Z4I3uymUYzlV1qU90KdaqeAu8LVt8ntys3ZrevvOH6Q6IeQFrHh1V0qnS-B1CT8-ZIuQFgP7fkgT1DRB1b_jJN5fOHk7lTI2VqK6PGzgt6sy4Yu1kB28qM5EZdtpeB20hwS81HNQuTrKHtwlw6lxMshzzzQ2o_Am8I7Tt2OHy4gRzr2dpqTdAUYPXudl1Q0pwovuzT78VTcF6zFC3kPgjyHGwpqhgiRRbejQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=vDvNRP_WoKyuo2ywRQJcA_TrHzgs-bHudcWBh-GQj-_rad2FbqMtrSkNDdcUBMyXAvdgUZXZKu6mnv6aK5FpgMQhpYUVtMAw8uGq3p8j_V7yaUmM0-Z4I3uymUYzlV1qU90KdaqeAu8LVt8ntys3ZrevvOH6Q6IeQFrHh1V0qnS-B1CT8-ZIuQFgP7fkgT1DRB1b_jJN5fOHk7lTI2VqK6PGzgt6sy4Yu1kB28qM5EZdtpeB20hwS81HNQuTrKHtwlw6lxMshzzzQ2o_Am8I7Tt2OHy4gRzr2dpqTdAUYPXudl1Q0pwovuzT78VTcF6zFC3kPgjyHGwpqhgiRRbejQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=fSAVyVtxxe69cmNIufn2NRbLJJyyofUtIzzsJVzNX9MNG-jnp0bHTixq6bgnaQ2eTIiFucyHoLWvOBfddoGeUxA01w8xr5n7As2kwVJqdDBbIhIukpOYEOrz5eJ-zrTPCWCaR4ukxXq1ge3L8-G5YKNVgv1vi88jGLnImUGqEXous_cXWPiPQPHGUNEtrUcKBcZ0wxJHxTc5EN2Fum28YIQff1lXdqjCjHp0xAdmsz40ln3VYe7sGwCCxlyUeX2tvVgOS0wmZLuariZkHsscWPpyaBfXCiD0s8BOO9IcfL_OHjFzWoxPZxQMJaSLGhzdSdp2NSoW4salb2JpHl0ZlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=fSAVyVtxxe69cmNIufn2NRbLJJyyofUtIzzsJVzNX9MNG-jnp0bHTixq6bgnaQ2eTIiFucyHoLWvOBfddoGeUxA01w8xr5n7As2kwVJqdDBbIhIukpOYEOrz5eJ-zrTPCWCaR4ukxXq1ge3L8-G5YKNVgv1vi88jGLnImUGqEXous_cXWPiPQPHGUNEtrUcKBcZ0wxJHxTc5EN2Fum28YIQff1lXdqjCjHp0xAdmsz40ln3VYe7sGwCCxlyUeX2tvVgOS0wmZLuariZkHsscWPpyaBfXCiD0s8BOO9IcfL_OHjFzWoxPZxQMJaSLGhzdSdp2NSoW4salb2JpHl0ZlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGotkFhj8OwW6Tb-veiePLnQFA2a5UtBEv-kmrkoCCICnLEkv3NseViwTVBCJHKcQ-GX4DPZMBMP2N0G5YTyuDjrFMJoleMCHWRye6LMZfOg9SD0JyZ0oyXJspJM1jt-nSCpHJC97qXlo2SMXffceep4sPmj3VOxrL5ggWl_sqV7ZqLlXvGl3MRIbtVVetWRGH3JwR_vdAMHbkis9IsFn2fo-P3V22PWWZ82rYBCN1ajsV7ElI6qZlJ5BJJf-2eiBMqr5OlGL3CfkUYeD6KQBwQHMDHq9GcVgmTZM94r5Ok5_hwhiqfnkefbU7AdHnnwn_R7uPSrxcpnyVwgL4tXww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
