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
<img src="https://cdn4.telesco.pe/file/jwQxZF53Dzr6mso90X8byu7b_3WJrjmq-3tYPuXMJtjVf0swgvqy-_bpHZ9rmZR_rdb3oa1L0Fyx-stJ0I8CnzQWdnoLUQsFFCwhn_b5rlX4FErNnEzPFIZ6OyqkMfx5x9cP7UFIqdW1OnjNh3T_DTzzaEJBuVk1BNsCsk7LiZ2XN4ctCyi7-w-GbyJCiFfFhjjUFVLzbcIUQjudmjngADiARphbNRlM1lghiSiRaZmKQVudMQ1Lfv96fsLBG9_R4oKqFmi5qZ6f_p5B3Jf5U_H7-Op5h7g1Hs74JbqsoKMo9rJxlt63sz9_Quyc_VNvXY_v-ocuSh-7ydX487sXTA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 132K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 15:35:27</div>
<hr>

<div class="tg-post" id="msg-69681">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5020dac98e.mp4?token=LIU8FS3w7IyZJ7n2LfVD9NleqQDgJNfMvJtyl7lziB3z-eQXHGl346IrqcZG1cH95KLoV_wTRDDjuudBju44cWvgo1e6HXg3paKu1HY1W_6pto2h5FkgVdMrHjKesX4-GW0lrRssGTj14BfupSPIrdWjFpon06Eqj4LYT03BrB-GtQ1sSjJajM4pE4bVPyWbHT2KEQlHmv6TAZNGi-izTIR-fF0jU0qe6ybV5QC0BZFDgkKMROcsGF42_fl3t-jMjVGxeXz8Nr9QlXIKtCQwWlq5q0TwyozsbyVyzQnueSNVfOXEG4-ejlS-q8z0X4zJFuDDQE8UzqdFkD3u9rNbQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5020dac98e.mp4?token=LIU8FS3w7IyZJ7n2LfVD9NleqQDgJNfMvJtyl7lziB3z-eQXHGl346IrqcZG1cH95KLoV_wTRDDjuudBju44cWvgo1e6HXg3paKu1HY1W_6pto2h5FkgVdMrHjKesX4-GW0lrRssGTj14BfupSPIrdWjFpon06Eqj4LYT03BrB-GtQ1sSjJajM4pE4bVPyWbHT2KEQlHmv6TAZNGi-izTIR-fF0jU0qe6ybV5QC0BZFDgkKMROcsGF42_fl3t-jMjVGxeXz8Nr9QlXIKtCQwWlq5q0TwyozsbyVyzQnueSNVfOXEG4-ejlS-q8z0X4zJFuDDQE8UzqdFkD3u9rNbQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سردار کوثری، عضو کمیسیون امنیت ملی مجلس:
ما هنوز که هنوزه موندیم چرا شمخانی با اون همه سابقه نظامی، اصرار داشت اون روزِ حمله جلسه بذاره!
رادان گفت نمیام و رضائیان، رئیس سازمان اطلاعات فراجا رو فرستاد.
پاکپور، فرمانده سپاه گفت من نمیام دارم میرم اهواز، ولی به اصرار شمخانی اومد.
وزیر دفاع رو هم با معاون‌هاش دعوت کرده بود.
الانم چون کسی از اون جلسه زنده نمونده، نمی‌تونیم بفهمیم چرا شمخانی انقدر اصرار به برگزاری جلسه سران داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/news_hut/69681" target="_blank">📅 15:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69679">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aij0ldap06_vRnGE2IecD3r_SG4WHDA1IIH0xWSzCng0YKXp5xvHT6Tt_YuzTvf3eq87oXVTj6zDQI79eQenAjDcJglEsmUgb-XlA4TruDMRf-O3lbdJzGioBEeOBpEJjmocygxej2XduT2HMjeAJAhGKLuSUhn2shO6Y_WHaMOKMVo6PS08meGJbiSFYc7dt44pKLUuY2AFsVdBHfkXDkW_tUaQP93K7VV-nbJYN4GIVqDlsVYZX-TZLSZF0x5Z7_ii7DdFe4qtkv9g2IjHDsv8ne0VgJARgAFUxbNGpcak5ONvQ0xel-gyekAbYmumQ1DpYPyjCpHlue0OByQ5zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JlxHxDPL2KHLIBfaaplYkuq2KE3bXpkEAL2E6LCKGZJpBvOUb7Dd0bhE3WOiCDgrlMvIcmZLQCYxOHEV_g1xz7z3G5cAjLM_XmdJ37QLa8Jh0_lYPZ5Eol4kHS5rXw4ls8b1FWWHFF6RBV07zvUlim_f3iUama-Y5aGPC5IUj8-2szKjyVxWuDCyl1xgZ3efdB3DM6ORgrZQ9C40qcqNn8po6I7Ct3S7n1x1I1kQIcnp_LoyK2qu4uuWipz011dGT7QZZ3-S6P_nGWyq0EZ3oUDeqWAAwzK8c8iYJ60uc6_dEcJayUaHb83Kf1Og6s6Q7SqXRQgA66Y69oB85OPQxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⭕️
🇸🇦
🇹🇷
🇵🇰
ترکیه، عربستان سعودی و پاکستان پیمان دفاعی «توافق‌نامه مکه» را امضا کردند: «هرگونه حمله نظامی علیه هر یک از این سه کشور، به منزله حمله به هر سه آن‌ها تلقی خواهد شد.»
این توافق که مذاکرات آن از سال گذشته در جریان بود، چارچوب نظامی سه‌جانبه و مهمی را در بحبوحه بحران منطقه‌ایِ رو به تشدید — که پس از حملات اسرائیل و آمریکا به ایران پدید آمده است — ایجاد می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/news_hut/69679" target="_blank">📅 14:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69677">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b215003af2.mp4?token=aIy4tmBwmBKDwbpzsPpgGZPG0C4zeifUdzSeIkQAeDLI2rX74yv0L7n02ACR0neVs3M-J9N20NQFGK6gF4cQOxyj4R4PARFOzF9BBPJs9wGHYU48Ta0WKBGybzGUhVsR2G3h8kU06imw0B_kOqtAv20h6J2nWiHuiVK55v87kqqKWxPkb_oSjszql2B7ekGd8OYgi_QFhsTpXdF_QJUQnjeGxNdZDiMPwqJJyYWSl3hmV3Qnhr18tVujywYfG5OIds_eihmufM0cihVlhSkpi8qkI65XgL2pAY5YGahYpmW9tgToFiyGwj2e5NCbCXVfzp7CMVgoyqYn0la2Qu3i-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b215003af2.mp4?token=aIy4tmBwmBKDwbpzsPpgGZPG0C4zeifUdzSeIkQAeDLI2rX74yv0L7n02ACR0neVs3M-J9N20NQFGK6gF4cQOxyj4R4PARFOzF9BBPJs9wGHYU48Ta0WKBGybzGUhVsR2G3h8kU06imw0B_kOqtAv20h6J2nWiHuiVK55v87kqqKWxPkb_oSjszql2B7ekGd8OYgi_QFhsTpXdF_QJUQnjeGxNdZDiMPwqJJyYWSl3hmV3Qnhr18tVujywYfG5OIds_eihmufM0cihVlhSkpi8qkI65XgL2pAY5YGahYpmW9tgToFiyGwj2e5NCbCXVfzp7CMVgoyqYn0la2Qu3i-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇹🇷
🇵🇰
رجب طیب اردوغان، رئیس‌جمهور ترکیه، و شهباز شریف، نخست‌وزیر پاکستان، به همراه مارشال عاصم منیر، فرمانده ارتش پاکستان، امروز وارد مکه در عربستان سعودی شدند تا در مراسم امضای توافق‌نامه دفاعی سه‌جانبه شرکت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/news_hut/69677" target="_blank">📅 14:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69676">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/637fe07403.mp4?token=eUy1TUYaWNaZ-demEq9QqbXMcXlbDS2gRciiAogFIbrEbKDLQtdu-Ezl3LdZ86YePeaOVDd0f96REknqHoH6_iAzTEjVZSHbh5y35il000r1qyZenRwnjZEfa-pmiR_2OEoa6ZET2Dxsa32PbpinVlWkMVM66WBJW6B7o-WH1u9pqaLUmSMzf8XZqLDup0_H_fXWiY2VE0kmgh142wDKWAdBFfpZKQpE-5Mfzirexz-li3Ku2wSa_WvVx4aZreapgm_B4dI_yBk6pid1fOuMqh06579d_JGe66O13dYgLwFKDx0jr5yasjaVXBB1lK3sfPmOt5dNZE7bKlgpu7gLqw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/637fe07403.mp4?token=eUy1TUYaWNaZ-demEq9QqbXMcXlbDS2gRciiAogFIbrEbKDLQtdu-Ezl3LdZ86YePeaOVDd0f96REknqHoH6_iAzTEjVZSHbh5y35il000r1qyZenRwnjZEfa-pmiR_2OEoa6ZET2Dxsa32PbpinVlWkMVM66WBJW6B7o-WH1u9pqaLUmSMzf8XZqLDup0_H_fXWiY2VE0kmgh142wDKWAdBFfpZKQpE-5Mfzirexz-li3Ku2wSa_WvVx4aZreapgm_B4dI_yBk6pid1fOuMqh06579d_JGe66O13dYgLwFKDx0jr5yasjaVXBB1lK3sfPmOt5dNZE7bKlgpu7gLqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از صحبت های ترامپ درباره ایران به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/69676" target="_blank">📅 13:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69675">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a5084b0f.mp4?token=vi3v6xlGf1pCVJY3dpMTnQU9dMSXlSDDiwODnqtI8Cfa3icAgRw9GTj-RHbkvl-oPBoLNvHbw5GoP9Y8VBOAQbBBM4pbxxTO4B5AEWIB8k7e_NJXB_sP1J1S3BDiNT3mVmNTRXK498VN3DXzz_MTLGVAigm05XyEC3DzESB3art940j5Ym2NC_LsigqJifxnVy95hso3ZOgpdsbE_eUn9Tj27Jr3Wj8Sv2OtEdSLxSDB_dsPum43tHKL6YTIvj5_dnSnuRvf8PB3AurIPfc956LEoxPGMC57kPKk5qy3pQA8sOWYzwrxPpIxp0OUoa5ajK97KmZxxaLo99ptrUX67g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a5084b0f.mp4?token=vi3v6xlGf1pCVJY3dpMTnQU9dMSXlSDDiwODnqtI8Cfa3icAgRw9GTj-RHbkvl-oPBoLNvHbw5GoP9Y8VBOAQbBBM4pbxxTO4B5AEWIB8k7e_NJXB_sP1J1S3BDiNT3mVmNTRXK498VN3DXzz_MTLGVAigm05XyEC3DzESB3art940j5Ym2NC_LsigqJifxnVy95hso3ZOgpdsbE_eUn9Tj27Jr3Wj8Sv2OtEdSLxSDB_dsPum43tHKL6YTIvj5_dnSnuRvf8PB3AurIPfc956LEoxPGMC57kPKk5qy3pQA8sOWYzwrxPpIxp0OUoa5ajK97KmZxxaLo99ptrUX67g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
روایت کوثری نماینده مجلس از عملیات اطلاعاتی موساد؛ «رد لاریجانی از طریق گوشی زده شد»
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/69675" target="_blank">📅 13:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69674">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
r16
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/news_hut/69674" target="_blank">📅 13:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69673">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkG5hthzF2YoFGFRJgs4odJMyRdhOM3WK4YepLg0xM6RDKt08v-yD6SlBrxijT8lxfEpBI2qNr3x-yslZNwikjZsFAx4M909oSlgZlMRAOT2lRnhSiHaDQRed2bN_J1wVZ_cOLjyMRm0ByxfUGOndziXhyDil2qescE5NyyooAlS7moFLdYtMBK9tUJWJoAQuU9KBGzt8dI1kj5DCWPN_pLCk_a3Oa23Pr4bw1J27cT2TU6oenZ8ZSiDma2daVhWj5H1pzxQtltGxUH_K_zVk6bWrWF1QN7xNodTqV4G2H-rJhLhuvRYUEdU_65qgNX63EES53SULS7IdviuehVBjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r16
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/news_hut/69673" target="_blank">📅 13:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69671">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0c63da7c.mp4?token=UXu1hHRjxdwOvmzMS4km79tY7jOvELJ1d4gaMb4slNFX_LZ-SkIZxqp91ynScPI6x3JN7iD1m96rJGFL0kW_YQf3A20pkWlWYLovmU7UkVd9LME4igpLqv4QiaimPSXzTt2LdiJukmSMOUY-gtvKGjJUnWXsRwlEWIbjkymaa3u2piHqwFY9iKNVHcDIZBseocT_Eh6Hm3PNWOgTbgVDCRnI03HUmI0Tz5D7KAvVsLgdvwBGxcGUaCNWibMmq1kWKjYnxfanUnn2Ta6TscXxaCLzi-7Yrt6B3adyGieWTIt-kE_HdTbQMd8RK-WGopsuBog0E8NDwzsnin-Obxz5xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0c63da7c.mp4?token=UXu1hHRjxdwOvmzMS4km79tY7jOvELJ1d4gaMb4slNFX_LZ-SkIZxqp91ynScPI6x3JN7iD1m96rJGFL0kW_YQf3A20pkWlWYLovmU7UkVd9LME4igpLqv4QiaimPSXzTt2LdiJukmSMOUY-gtvKGjJUnWXsRwlEWIbjkymaa3u2piHqwFY9iKNVHcDIZBseocT_Eh6Hm3PNWOgTbgVDCRnI03HUmI0Tz5D7KAvVsLgdvwBGxcGUaCNWibMmq1kWKjYnxfanUnn2Ta6TscXxaCLzi-7Yrt6B3adyGieWTIt-kE_HdTbQMd8RK-WGopsuBog0E8NDwzsnin-Obxz5xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تا حالا نوک قله دماوند و کاسه قله دماوند رو دیده بودین؟
۸ مرداد ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/69671" target="_blank">📅 12:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69668">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10354b943b.mp4?token=MFV18z25psGHfitmAOS4f-AyHPSXIz9yiBl7f3Qtf8ulc-WIz8YTFh90x4SDB_ZUgaFvTIz5UQgHpIt7pr0PbaWenElVWZgEeWJveOKjWJhAbyUZ3V_h4G5jwFKEFGBjB1j4JjpXNlDRGzIKXzs0bYHvj1dJiEtEhFnwdpoJwqGS9OHxdc6Gw_SUZkqc6vx4mjvTmmrZHY5zvRkpZf3IXHsWZi5HG9jaKg2YG3BXsd5xON3ZV2zMz8ThoJYH8ksJu_aUTlttAarpOQNtph5wvhkeHsvD-dOU0KLxlCXPb_21R176bVRoN0LxUSOl43WfjlMtCkfSdGMURqw363sTlw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10354b943b.mp4?token=MFV18z25psGHfitmAOS4f-AyHPSXIz9yiBl7f3Qtf8ulc-WIz8YTFh90x4SDB_ZUgaFvTIz5UQgHpIt7pr0PbaWenElVWZgEeWJveOKjWJhAbyUZ3V_h4G5jwFKEFGBjB1j4JjpXNlDRGzIKXzs0bYHvj1dJiEtEhFnwdpoJwqGS9OHxdc6Gw_SUZkqc6vx4mjvTmmrZHY5zvRkpZf3IXHsWZi5HG9jaKg2YG3BXsd5xON3ZV2zMz8ThoJYH8ksJu_aUTlttAarpOQNtph5wvhkeHsvD-dOU0KLxlCXPb_21R176bVRoN0LxUSOl43WfjlMtCkfSdGMURqw363sTlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🚀
🇷🇺
پهپادهای دوربرد اوکراینی در حال حمله به انبار شرکت روسی "وایلدبریز" در شهر یکاترینبورگ، واقع در منطقه سوردلوفسک، هستند. این انبار حدود ۱۷۰۰ کیلومتر از مرز اوکراین فاصله دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/69668" target="_blank">📅 12:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69667">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff4cea8c93.mp4?token=Hre9ROwgkw1iKkQFegFQyUR6i1MZ7chyoNC2ZBTfVjhH-OqZlOSyVeW_HDd3g6GXS9RdduUIANK7t773POLtetkco6lJr--2jT_tiQ0S1WhbXsMKaGFUR19xxLZmRcqhEZl24DpJgldJp25pmmpauzkzs3OqkWhP_2qkE00mQd4hOEZbSMD9RvdXnpgZulHHO6V28ykPrrU9h2PdTdeSHvpwmK7OW6p3hTyUIFMEHp0Jl-rBwa0RoEO_gGX7FACbri5Z1gwh6reyBVIFIUsfQ41C6FD9G5QMGTWTV9oj0esmjXucapwBU7V64Xso1BZGy5WzgDtkzOoNbueJ7ppSZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff4cea8c93.mp4?token=Hre9ROwgkw1iKkQFegFQyUR6i1MZ7chyoNC2ZBTfVjhH-OqZlOSyVeW_HDd3g6GXS9RdduUIANK7t773POLtetkco6lJr--2jT_tiQ0S1WhbXsMKaGFUR19xxLZmRcqhEZl24DpJgldJp25pmmpauzkzs3OqkWhP_2qkE00mQd4hOEZbSMD9RvdXnpgZulHHO6V28ykPrrU9h2PdTdeSHvpwmK7OW6p3hTyUIFMEHp0Jl-rBwa0RoEO_gGX7FACbri5Z1gwh6reyBVIFIUsfQ41C6FD9G5QMGTWTV9oj0esmjXucapwBU7V64Xso1BZGy5WzgDtkzOoNbueJ7ppSZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسره رفته خواستگاری، بهش گفتن 114 تا سکه باید مهریه بدی؛
🗣️
اینم قبول نکرده و گفته کمه و من اینارو میدم؛
369 تا سکه
1382 تا گل رز سفید
کل طلافروشی رو می‌زنم به نام دخترتون
یه سهام کوچیک هم تو یه کافه دارم که اونم میدم
امیدوارم راضی بوده باشین.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/69667" target="_blank">📅 12:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69666">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
🇺🇸
🇨🇭
آمریکا حتی به سوییس هم اجازه ساخت بمب اتم رو نداد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69666" target="_blank">📅 11:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69665">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ca70a3a5.mp4?token=Qwwt2UXY3sEnGN27VcZ4xZ5MYRmZghZdOcHnH2u-Uqc0R3U0HCp3VRCTo_DR746iy79AbEIIwEpBHX68SsbZUusztmzLcfPIBgHYtcfVuAvAoN-C6YV-zLBezqDe75IkPSt6sR9FYJUZhNtzLsWBUqE7tYhQtBNZDgymcEwSTpDNFl8F6pQVeMBD-bQ635PWmmrMPeb_GOhTBJHbgv4ccF2OOGwJpgWxgEno9cOUklUomy3FX9iAhT7I6IY02pSZO4Ui_ucHnWLSq5Ul7Iu5zoKswnykou5Wb7FQKDdIC3XfTuJFABmLckLjn5k5IJxg8rtZYZDcJTWqgFis0OC9rzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ca70a3a5.mp4?token=Qwwt2UXY3sEnGN27VcZ4xZ5MYRmZghZdOcHnH2u-Uqc0R3U0HCp3VRCTo_DR746iy79AbEIIwEpBHX68SsbZUusztmzLcfPIBgHYtcfVuAvAoN-C6YV-zLBezqDe75IkPSt6sR9FYJUZhNtzLsWBUqE7tYhQtBNZDgymcEwSTpDNFl8F6pQVeMBD-bQ635PWmmrMPeb_GOhTBJHbgv4ccF2OOGwJpgWxgEno9cOUklUomy3FX9iAhT7I6IY02pSZO4Ui_ucHnWLSq5Ul7Iu5zoKswnykou5Wb7FQKDdIC3XfTuJFABmLckLjn5k5IJxg8rtZYZDcJTWqgFis0OC9rzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از شعبه بازی این پیرمرد، قراره هر لحظه بیشتر سورپرایزت کنه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/69665" target="_blank">📅 10:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69664">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntXl6689R5LdgdbzQEyB7FzosrDSZw4THKAthnLJ-ksgsorub6hsyNKMnFztrGOPY5g8Csld7gvJB7P6xIwIW-MG0MR0T9sWTOHmwRK4EFFUkWbtGup7wYyMpDmzakJZSt5vp5uyCKDQa9P7D5SEJQWsnsrEiwEx_W_YuvD9kobxwlJzoQ_AEFSnGRZlDd_-r6bVy2mm-3lSk3hc7VshsLhPfiet6-ILR6UbT4aKoaVHpUY4MPMDjwBNfR9AfgKRyDrqH4DtVq66DfefDQf9JPgiOma_qeOuKpw14jGp43Lfgq-W5v4hclduX9eh6dKf5AOZrxac396R83lBOaTobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
عنوان مقاله ای که ترامپ در تروث سوشال منتشر کرده؛ دونالد ترامپ در جنگ با ایران پیروز شد!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69664" target="_blank">📅 10:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69663">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c98f66ca27.mp4?token=t6nNDfAMNb4ltdPq3jVrSwE4tQ3_ejwYfY1L5WKAMU1SId5i_HSNFSiDOelYR55k3H69imq3-ZcEE8ehdZOAeAhHz0gvfMEX7GIbUHzp1BjtNUJIWnztVsirrzwK1vhOh0hWV-Nx52lHkq_fJRJdWcBtrkG5PH6XDVpbNhb-6EL7KaVrgt9dTT2uHNLTMghv6AKBdWi3Zj9eLTiHL92idO87qQ7S2CbLQ5jA2Ll_PFzoKmM7id2IpDlXRMeEh8Cg69wV9Z2-Pizd0DIDVfj8q1GJMnGY12WRvMII-i_MyoSleYwCtPoQJZ9pML-Q1OunXQ0Z7BqP8o5IzWuKnXCPFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c98f66ca27.mp4?token=t6nNDfAMNb4ltdPq3jVrSwE4tQ3_ejwYfY1L5WKAMU1SId5i_HSNFSiDOelYR55k3H69imq3-ZcEE8ehdZOAeAhHz0gvfMEX7GIbUHzp1BjtNUJIWnztVsirrzwK1vhOh0hWV-Nx52lHkq_fJRJdWcBtrkG5PH6XDVpbNhb-6EL7KaVrgt9dTT2uHNLTMghv6AKBdWi3Zj9eLTiHL92idO87qQ7S2CbLQ5jA2Ll_PFzoKmM7id2IpDlXRMeEh8Cg69wV9Z2-Pizd0DIDVfj8q1GJMnGY12WRvMII-i_MyoSleYwCtPoQJZ9pML-Q1OunXQ0Z7BqP8o5IzWuKnXCPFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
این شما و این مجهزترین اتوبوس های مسافرتی چینی!
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69663" target="_blank">📅 10:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69662">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d6484080b.mp4?token=p7sPwD9EDUbz1euCjBLoCtt9RBnguiJAg2JIoIDKKTiyATbaM3ODawdXsJ8cbHvt4v48yid3DzvCs-PfNnIbyT0AdCxq9QL_VIU9vgzWz5ZA_lP23PZ8PjiBomY1_R-DM36Texl0PiDoXQWnD275pgrKVIqb7ZfI9jbkI3-Jgsz3kspDO8HJdB6YDvD7pHerKERqluOuh55YfBvRe6Zxcfyr_XP7uFflnG8ohOSGqmPTgrPjj39eOyyXua_eRJE6um0OPuD2krTyqRz3oNqSfkSCT7-xlxm_43ytLZYmXwAl6wb7b7K0P-x098t-wZQFghTgnN06J-RPf3tNtnhJoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d6484080b.mp4?token=p7sPwD9EDUbz1euCjBLoCtt9RBnguiJAg2JIoIDKKTiyATbaM3ODawdXsJ8cbHvt4v48yid3DzvCs-PfNnIbyT0AdCxq9QL_VIU9vgzWz5ZA_lP23PZ8PjiBomY1_R-DM36Texl0PiDoXQWnD275pgrKVIqb7ZfI9jbkI3-Jgsz3kspDO8HJdB6YDvD7pHerKERqluOuh55YfBvRe6Zxcfyr_XP7uFflnG8ohOSGqmPTgrPjj39eOyyXua_eRJE6um0OPuD2krTyqRz3oNqSfkSCT7-xlxm_43ytLZYmXwAl6wb7b7K0P-x098t-wZQFghTgnN06J-RPf3tNtnhJoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو دیده نشده از لحظه حمله به بیت رهبری و ترور خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69662" target="_blank">📅 09:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69661">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-release.apk</div>
  <div class="tg-doc-extra">4.5 MB</div>
</div>
<a href="https://t.me/news_hut/69661" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎲
همین امشب با اولین شارژ
🤩
🤩
🤩
درصد شارژ بیشتر بگیر
همین الان شانست رو با موجودی اضافی امتحان کن حتما بزنده میشی
👌
👇🏻
👇🏻
🌐
Telegram
🎲
🌐
winro.io
🎲</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69661" target="_blank">📅 02:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69660">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwDbAn4Ipdewpcs6iMxU-NWcug6WIhinsG2sCt-PwAjpgptCAnMHsVdJYziFsuCRPxnegDzv0HJhR87y0tZEBb8P_PSyISvhOcOjBwiSMcUwV4BgBTZ-uJt3c2BjN53IDApS0mfteQ6uV-1BSOFyCgi0CV-l7am-tvLgVp4llyrhKbnumrjwuAbtsEL1RTfUV7M0sXFZtd2K9d2rrDvR75FokmQT_PdwzfbYPLWBnF2LlB7TUvfycA5PJaEhodH2V-Ie4r6AkUvg46DT-uBym49jRMGHCBttnKsatg-xkrUVznyGR-rAkHga06wGy-M9XcTC3jXJPkuRRRYtm5C69A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑️
۲/۵ میلیون شارژ کن ۱۰ میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر در وینرو شارژ شو
🎁
✅
به ازای هر واریز در وینرو به ترتیب 300 ، 150 ، 75 درصد بیشتر شارژ شوید
.
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن
⚡️
🎲
ثبت نام آسان و سریع کلیک کنید
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا a15
🌟
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/69660" target="_blank">📅 02:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69659">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwSkpo8xbqXcSpd_tT5TGIX0MkcUhN2bMKrfX9NPuhq60FO6W3-Ib5sqIO7G4KoaGWMUOvJnWFuLLCxz9mMd_1y_iS8iHdXwc0Nsbey4YovH6aD2Uxa3TfL5Goxklq6lWdA-t2OHA0boYxNPwPVi5gLCJHKvXZSSg4vq5C-oETYW_rRtKHfAOScjIf_iy9lOlOKD1P7Y6AGf9lUwl22YkA4kL3u4jZbnB4GlWf2pRbWJmA1G8MI6b8EineZj4fqNbreE_DYPMWTArQfCAsDQWuhPN30cEp1qDcdS8GfHApbbmGIggBpysbHMuY3L0H1i_BvhYUxD1jRE9ZMu9bPqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇹🇷
🇵🇰
رویترز:
ترکیه، عربستان سعودی و پاکستان قرار است روز جمعه یک توافق‌نامه دفاعی مشترک امضا کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69659" target="_blank">📅 01:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69658">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iihkg8ps8XN7Pt7kwrdEI4aT883p-g2iKrGTc7B56yeZ1UKUqO9-1nJ5SdSKA35rv4mlE8D6vsQOabMDsTKnbZ_GfbBKyp3KNfNU7Dr8qTG6vdZfCJEwl0B27aBY2E-f8UhJ9Q90MnLtGvWUKMCbnuGB0-77xqk1_mHVqiFgJcNc_L3sDdnPKbHIvkp2NiLPHXBaoldTHIZx9j9mejWuIrlDD0bbXanJ2szeAIssZZK5BNSfnucMLypClKmwsdHtq8Cg5goBkhqOpM-v7q-YJNq-dJYDSM8LM83VaYKIIsFqvA-OtY5-hLLbA8m6MQ_tMw_Rh5DYyz75RVAn7MA4Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سی‌ان‌ان:
🔴
یک مقام ارشد سعودی؛
اطلاعات موجود نشان می‌دهد سپاه پاسداران ایران در حال هماهنگی با شبه‌نظامیان مورد حمایت ایران در عراق و حوثی‌ها (انصارالله) در یمن برای تدارک حملاتی علیه عربستان سعودی است.
این مقام اظهار داشت که این گزارش‌ها به‌ویژه نگران‌کننده هستند، زیرا در شرایطی منتشر می‌شوند که ریاض در پی کاهش تنش و انجام مذاکرات صلح‌آمیز است؛
روندی که به گفته او، پیشرفتی مثبت داشته است. وی افزود که پادشاهی سعودی «برای اتخاذ تمامی تدابیر لازم جهت مقابله با هرگونه تجاوزی، درنگ نخواهد کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69658" target="_blank">📅 01:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69657">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pm5kYG_7IhQle_vD2sfR20gBOghF0eNRXb7kujxifkfvMnyRvBQYTit4BpvqIVAzWxqDJGEUqGJTUU_vD45r-9bFUuEoUGnXRsS7gEnZd-efJFVs23gUIZVg32gQVhqmGx6DxkLk21eEjf8vMuBg4bG9gZcqrSGLb1rRZ7qmNGQLoUBgJ8aG-ZiI1lp3rhAY4xXIIdYNz4O4novVJp1gryok55SeBd3Jp7uPaKC-mCdJGGYGZsTBdJ7KyXcmO6z6VANKz-22wDwiW3UkWRZqDfgHU9jin1JvJJJ8gHj2xxf_G_q2B4Z9vQPJazC3c3XjmZkt8uArQLomonw0bX1YDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
کانال 14 اسرائیل:
محسن رضایی میتواند خودکشی کند، ما برای او مهمات مصرف نخواهیم کرد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69657" target="_blank">📅 01:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69656">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac1c12b672.mp4?token=FdBHju8y2_N3lU8KYeJXUTRQmMK5euQZfMHfXo8IZlyawKht08yhtNMAmy5yLTtZkYJRPH7696opX5535Rpwo3IbZ0JLJRgWw7j7DdGOuT--U-xR1t0OZ_z2I2MyxtQrIreac2xqFeoIZa2F_XRzqn4It7BVD4LsomnmE7wGUS8BQs1fh1gl02BCO4kzE-x3H1Ke0ijqNd2LvGdHDaHJPRhCLbpAvxx-rR6T7u1mAl3inMaPNP8Na_riLoPlLt2KFGeC-1U0irJRjDOxFoVxVn2kC0ADJnkNJwYs_oAvA1oOGGwcQJY2aM_oFoTXobvIj6lMabS9PxwNwq7z-3m2mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac1c12b672.mp4?token=FdBHju8y2_N3lU8KYeJXUTRQmMK5euQZfMHfXo8IZlyawKht08yhtNMAmy5yLTtZkYJRPH7696opX5535Rpwo3IbZ0JLJRgWw7j7DdGOuT--U-xR1t0OZ_z2I2MyxtQrIreac2xqFeoIZa2F_XRzqn4It7BVD4LsomnmE7wGUS8BQs1fh1gl02BCO4kzE-x3H1Ke0ijqNd2LvGdHDaHJPRhCLbpAvxx-rR6T7u1mAl3inMaPNP8Na_riLoPlLt2KFGeC-1U0irJRjDOxFoVxVn2kC0ADJnkNJwYs_oAvA1oOGGwcQJY2aM_oFoTXobvIj6lMabS9PxwNwq7z-3m2mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
تفاوت اعلام مرگ دشمن از طرف ترامپ و اوباما:
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69656" target="_blank">📅 01:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69655">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7820062e8b.mp4?token=lst-zwH0WHUpmvFrhRDFZp40VoYGgW-mIIaGuxa_NBtDiJi0nCtXQ4QWrrHvgEpcus4wfRWZziFT9CpCgw3k65mxRTK3MTtdLn3mHSB-_SumVQzyuoW6-gsWbZbhnvfzXFI2_yZTLLJH5NoTT2mfa2BhLtU4vuNqWynJl4GGun3UEyC98ms2OieGg0e4S06NhHy9I8RQT1R5Zdj13HnYiQW-IjQgjzzsbO7ZddcNg4kkPM_03NwC4JIsh5XRPgXUqrv8p2jmTloaT6hsLQvj1ruhPsuO3NGCliJkR4R-OM6LLrYmTQGvPjMciYX0tiVX70aacTrK15IDO23K6AGowQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7820062e8b.mp4?token=lst-zwH0WHUpmvFrhRDFZp40VoYGgW-mIIaGuxa_NBtDiJi0nCtXQ4QWrrHvgEpcus4wfRWZziFT9CpCgw3k65mxRTK3MTtdLn3mHSB-_SumVQzyuoW6-gsWbZbhnvfzXFI2_yZTLLJH5NoTT2mfa2BhLtU4vuNqWynJl4GGun3UEyC98ms2OieGg0e4S06NhHy9I8RQT1R5Zdj13HnYiQW-IjQgjzzsbO7ZddcNg4kkPM_03NwC4JIsh5XRPgXUqrv8p2jmTloaT6hsLQvj1ruhPsuO3NGCliJkR4R-OM6LLrYmTQGvPjMciYX0tiVX70aacTrK15IDO23K6AGowQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: آیا توافقی برای بازگشایی تنگه هرمز حاصل شده است؟
🇺🇸
ترامپ:
نمی‌خواهم بگویم [توافقی] حاصل شده، اما در حال حاضر کم‌وبیش باز است.
ما کنترل تنگه را در دست داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69655" target="_blank">📅 01:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69654">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">😐
آقا یعنی رو دست فوتبال بد اولترا توی کانال‌های فان ورزشی تلگرام نمیاد
😂
😂
😂
@Futball_Bad_ultra @Futball_Bad_ultra</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69654" target="_blank">📅 01:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69653">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/INx0aej_ba-m5-_bayWjOxiAPa1mkLd4k_K-zw8_otwEWIKhFi0SzGi9zsmAnXwof2c6tGJbe4UH8T_3nRkQCSMEDhEaK9phTBOi1UVeWQRB7pgXEJdM8nt6nvDkjV3YD4IjR6vG7ysvmEXk4rQjpR_GS6MUITA6aCZZc2ySgRBDYNEnlOqXoam6Nb6nyCDMH8NJQ7C0Yzm91Lc-2GtoB3ZgQicZDq5WRMAInV19jRUEvk0-duHUpkE2OqwQnsaTWkFP3d7MLy9pI7pcDiS2rDnM0ptQwq9FWrKQXVZ9wjoaZqqs-SoXu12xeg1yTWd3iejUyDYSYsx9bJofg8fUFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
آقا یعنی رو دست فوتبال بد اولترا توی کانال‌های فان ورزشی تلگرام نمیاد
😂
😂
😂
@Futball_Bad_ultra
@Futball_Bad_ultra</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69653" target="_blank">📅 01:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69652">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6e63add2.mp4?token=SPEW942bI6ouGENO4qoweoIlRkvYn1ZLiKzEr6oavzE2B7CLJdP4GbtCQ0Jcq8IDVJ5PPfakVBl60lwHBiPyM4evOfqOwSRiPIrevqL9xoZCxQVX5TWBRi4V9Slmqt2eP4rB1huYTMVB0ggT0JZ-oE51pKRAg5GLvaI9U4tJge4HLzWeOSvjDdbAapF8OoWnecAKOmCHq0deyZLVgWOBqzlhHgq8O_6wzqesYYoIeamfTN4B1_P3tqKykP0qKcEr_CaB13GE8Xe3bGlb9WVwGDyCTpsUdLE5R9GkV4i40eK6OW8TlUilVAhjMZAWFzxtlUfaH3sJKp5zu8JGdLvEQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6e63add2.mp4?token=SPEW942bI6ouGENO4qoweoIlRkvYn1ZLiKzEr6oavzE2B7CLJdP4GbtCQ0Jcq8IDVJ5PPfakVBl60lwHBiPyM4evOfqOwSRiPIrevqL9xoZCxQVX5TWBRi4V9Slmqt2eP4rB1huYTMVB0ggT0JZ-oE51pKRAg5GLvaI9U4tJge4HLzWeOSvjDdbAapF8OoWnecAKOmCHq0deyZLVgWOBqzlhHgq8O_6wzqesYYoIeamfTN4B1_P3tqKykP0qKcEr_CaB13GE8Xe3bGlb9WVwGDyCTpsUdLE5R9GkV4i40eK6OW8TlUilVAhjMZAWFzxtlUfaH3sJKp5zu8JGdLvEQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
به نظر من، جنگ به زودی به پایان خواهد رسید.
فکر نمی‌کنم آن‌ها بتوانند این وضعیت را برای مدت طولانی‌تری ادامه دهند.
من درگیر مذاکرات با ایران هستم. اوضاع خوب پیش می‌رود.
ممکن است به‌زودی توافقی حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69652" target="_blank">📅 00:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69651">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed7984246.mp4?token=cwnFLzn7axKyx9hN84SRgbG-Rvc2hFYZMd4Dhh0q4DoIlQyOvtcU5qj0YAuMXLjDV84Qrt2hnN4KCZqs4vJM2SW3H9nJhgpUGqkN-TznaljtKDaxkvSxo6i6Lfp3F9a3dJqoKn1loIdMkJQBBF0E5cCfEkKXP2YAZKhoAyFKUtiaoUfvhD3t9v0VsMgJ3rIvCUcTgQMH4nXIv9XNDs0ImvbAnO6lS4yL6CasBqcQDx2dyt8ZOD09vpW6RWp38iC2JVoNhGth3ac1xBcAwn_mw_64dRBc5TIpGWTlXkFsbVHsT-Dcgopwl22cQj6YJ-_Axs-k3LV04Hh89uPlFyYuog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed7984246.mp4?token=cwnFLzn7axKyx9hN84SRgbG-Rvc2hFYZMd4Dhh0q4DoIlQyOvtcU5qj0YAuMXLjDV84Qrt2hnN4KCZqs4vJM2SW3H9nJhgpUGqkN-TznaljtKDaxkvSxo6i6Lfp3F9a3dJqoKn1loIdMkJQBBF0E5cCfEkKXP2YAZKhoAyFKUtiaoUfvhD3t9v0VsMgJ3rIvCUcTgQMH4nXIv9XNDs0ImvbAnO6lS4yL6CasBqcQDx2dyt8ZOD09vpW6RWp38iC2JVoNhGth3ac1xBcAwn_mw_64dRBc5TIpGWTlXkFsbVHsT-Dcgopwl22cQj6YJ-_Axs-k3LV04Hh89uPlFyYuog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حامله شدن دختر 20 و 18 ساله توسط همسر 50 سالشون!
🎙
خانوم دکتر:
یه آقای 50 ساله به همراه دوتا همسرشون که یکیشون متولد 85 و یکیشون متولد 87 بود، بهم مراجعه کردن.
خیلی جالب بود که دوتاشون با هم حامله شدن و میخواستن تاریخ سزارین‌شون تو یک روز باشه و این برای من خیلی عجیب‌تر بود
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69651" target="_blank">📅 23:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69650">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5609274449.mp4?token=WDaezKTfhcAsU8STP0qG7j13cBJuXouJPBsgvef_VPbouzuWFDJcfcqcQmx6ydqX3LaiVHh-KNWUispkBhiTMWtRa9Hccban_UM3SJ9G8Iswy0XQBUqnkMMN2Ybo70DmMKAZcVuixxSBzgzNLRuTcy8EJE6y2mEOt3OCJpQgdbXXRhfCcST5noG4iDhiLP8m2t9TE2i6pW0vH7uXlJQuw295JvnqYzkogU6vbTdcNtzXboR7IWTvBK1zKKn7SgV6odNKKCuzAFyzfAXsVAQaWg4DXvA1_qNVMpyDV4bV3Q-g3a59ruJ5ROaCRfIZW9jhB9vMHahiR50qaA1wP-1RdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5609274449.mp4?token=WDaezKTfhcAsU8STP0qG7j13cBJuXouJPBsgvef_VPbouzuWFDJcfcqcQmx6ydqX3LaiVHh-KNWUispkBhiTMWtRa9Hccban_UM3SJ9G8Iswy0XQBUqnkMMN2Ybo70DmMKAZcVuixxSBzgzNLRuTcy8EJE6y2mEOt3OCJpQgdbXXRhfCcST5noG4iDhiLP8m2t9TE2i6pW0vH7uXlJQuw295JvnqYzkogU6vbTdcNtzXboR7IWTvBK1zKKn7SgV6odNKKCuzAFyzfAXsVAQaWg4DXvA1_qNVMpyDV4bV3Q-g3a59ruJ5ROaCRfIZW9jhB9vMHahiR50qaA1wP-1RdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
انتقاد رونالد ریگان چهلمین رئیس جمهور ایالات متحده از جیمی کارتر در قبال رفتارش نسبت به ایران و شاهنشاه آریامهر:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69650" target="_blank">📅 23:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69649">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vJZ8DvYpjyfm4rSqKcCjlHdWReDa0b_b5JXLY1uYZFJM7dsBxiEhJi50NS7awhsuiUzIHM-dnDHoh2LbPiEsBKZwABb72qsiVgx-AK0iLBk-d08BvYsBVf_lgvvO4fQogPSos4WAsB-38NE3UoU6A5B7GWIycy4LO5Eqfc3CiSxdZ0S6OkLAMRebRTgfT9U0WUuvH0_Ov0ZXs4lsryf-cHMXSj3UNjclZsWS9ocKOfOy0H6kl_jkQxHgLkQL1gT2_UJEwXpxq1yYKgd4gpKAWGpQGMPa7Xh9qyyFwzTh5ri5UzwuKWCcDHY27pr2qBu8b-ZKxA1P0D9wy-2TUj0Utg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
«حمله‌ای عظیم در راه است... صبر کنید، بی‌خیال؛ آنها می‌خواهند مذاکره کنند.»
این همان نمایش دیپلماسی است که مدام تکرار می‌شود.
استفاده از زورگویی، وعده‌های نقض‌شده و اخبار جعلی به‌عنوان اهرم فشار، راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید. ما به نمایش‌های بیشتری نیاز نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69649" target="_blank">📅 22:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69648">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/164214744c.mp4?token=khp79lJymqzg-yMYF4IKPK2gc2uzr8qF2o8v7uSr59LSJyfLKDIwlTWG5kcNrsvsA5GWF1auZofodz9M-DX_4XDgca2J5U2i2Q0gkjolCO-lQP4cTHYNrybDN1ua4hwhHfeGE3ZKw5qzaPWs8GYg9RC1lPJi8U-hySAA8G9Vo77yphEHP7z6UormgoN50WEzH3N1k9MoeCIYxJKKmsiALTETqeK5sAoxNfh6fHUAeedLl28wDG21bkUSfMI1NlSL4TCMkLYUqz5qciksI1nE5dtIHyzjGb7L7SGyUQwkWdTao5qZ9f6tU7OlY4hE-DvG2qGtkuCV2Pmmw4gdHHtxUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/164214744c.mp4?token=khp79lJymqzg-yMYF4IKPK2gc2uzr8qF2o8v7uSr59LSJyfLKDIwlTWG5kcNrsvsA5GWF1auZofodz9M-DX_4XDgca2J5U2i2Q0gkjolCO-lQP4cTHYNrybDN1ua4hwhHfeGE3ZKw5qzaPWs8GYg9RC1lPJi8U-hySAA8G9Vo77yphEHP7z6UormgoN50WEzH3N1k9MoeCIYxJKKmsiALTETqeK5sAoxNfh6fHUAeedLl28wDG21bkUSfMI1NlSL4TCMkLYUqz5qciksI1nE5dtIHyzjGb7L7SGyUQwkWdTao5qZ9f6tU7OlY4hE-DvG2qGtkuCV2Pmmw4gdHHtxUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان:
پزشکیان: ما بچه که بودیم پنکه نداشتیم
مجری: آخه آذربایجان خنکه
پزشکیان: من تو زابل خدمت میکردم
مجری: آخه شما میگی وقتی بچه بودم
پزشکیان: من تو زابل خدمت میکردم و پنکه‌ام نداشتم، حالا چی میگی؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69648" target="_blank">📅 22:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69646">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
گزارش غیررسمی از شنیده شدن ۲ صدای انفجار در قشم  @News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69646" target="_blank">📅 21:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69645">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
گزارش غیررسمی از شنیده شدن ۲ صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69645" target="_blank">📅 21:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69644">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c949993e0a.mp4?token=df93ywEfEkRL3djm_BZPE_O4WxAJ3mDkj3qcOUX_220yt253XQzPm8SE9R-XhtljgrImyvdm_adtbka9nQ7gJjCPDTi8sNKEsKEM_qgygZ_w_-QADPHNyD0ZrjRFQ9V2lqJp7ab2w4VpQEx9D3BAMJh6w6PqqY1oD71Fs6z5oSrEVbhV-45eVFOAMLB89a9PA590O3TLU3yJipaqJOFDnLT4HBYTbw0q1lsrKVdfSkoaDazBno7a6XayrEpwEEYvn_NZ7L4s9nGjeIUgj6rjECxCnCp4RcPwGIR1WnpD7e_RnnqdS4KXqbTBUKDXhzZqrRptrMZh6ZkrqAGUulbldQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c949993e0a.mp4?token=df93ywEfEkRL3djm_BZPE_O4WxAJ3mDkj3qcOUX_220yt253XQzPm8SE9R-XhtljgrImyvdm_adtbka9nQ7gJjCPDTi8sNKEsKEM_qgygZ_w_-QADPHNyD0ZrjRFQ9V2lqJp7ab2w4VpQEx9D3BAMJh6w6PqqY1oD71Fs6z5oSrEVbhV-45eVFOAMLB89a9PA590O3TLU3yJipaqJOFDnLT4HBYTbw0q1lsrKVdfSkoaDazBno7a6XayrEpwEEYvn_NZ7L4s9nGjeIUgj6rjECxCnCp4RcPwGIR1WnpD7e_RnnqdS4KXqbTBUKDXhzZqrRptrMZh6ZkrqAGUulbldQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
تصاویر اولیه از تاکسی پرنده‌ای در چین که قراره به زودی شروع به فعالیت کنه...
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69644" target="_blank">📅 21:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69643">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQt6-rNFUIPg89b2cZOPdA_FjJjNIBehmhSMVf74AzkGA1uJ2ZSc3E-GVE7s9nQKHmU0KSUdRW11DuN_yNxEvHbXaTF8Uj8RHyQTE5ZSFVth_rzZdoUqtEs4bBVDS0YwgSmWNied4WwKVeqAr6NeAn_Soxkx3VWRDwybXtm3Uamc_QfkWYqwgnUHIWkjRT3xLigRAzoihUy40X5ewX2qom35vRncFCm6EeSu4tE7FDY_kN3EduVzyUgn93E12DukpAw7SzPw2fMZ5LWitza93sGaMdqEjRXwaY7p273uLKLjg7bt3L8_0NLjrFkdKrNJdDDywwf68gFSsbFn8MtaIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
خبرنگار الجزیره :
تنگه هرمز: به نظر می‌رسد توپ از زمین ایران و عمان خارج شده و به زمین آمریکا افتاده است و اکنون چشم‌ها به رئیس‌جمهور ترامپ است تا در مورد جزئیات باقی‌مانده و تعهدات آمریکا تصمیم بگیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69643" target="_blank">📅 20:49 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69642">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvUdDdGRoElL5UTvCVk7QNkds7A4EMfgyNjSULvjvDXkCtciKm8uFflNs2NRQvPvdMAK47y4i6N7ML-JNlTyIZAN4nRbFNYBcId-lRmGKzIrCzUZqudre0OLJ8Awevw5i3scXdu1QjtQdoYd_x0pKn4U_ibGTfXw4aUDgp2tf9f5-e525ISfhreL1j1pT-FzhWYZhKCCQ2j5wKN__r6Y5-Aa6W1zH8Ac1xW5jphSAtST9WdEjF-VoaLM0Jbe6G335RpL88mo0hvauP0yGi9FTNRHAP1jzn8bNM4VAfqgtY8n0V-wZ1JSEVo6thKmBU0NmGeUmTYX8H3iF1SYf5JTsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
رسانه‌های «اخبار جعلی» طبق معمول در حال پخش شایعاتی نادرست و کاملاً بی‌اساس هستند.
من از عملکرد «پیت هگسث» بسیار راضی هستم.
همه چیز فوق‌العاده پیش رفته است، از جمله عملیات ما علیه ونزوئلا که نتیجه آن در کمتر از یک روز حاصل شد و به ما امکان داد تا یکی از بدترین جنایتکاران جهان، یعنی نیکلاس مادورو، را به دست عدالت بسپاریم!
در مورد ایران نیز وضعیت بسیار خوب پیش می‌رود؛ کشوری که با هدفِ «جلوگیری از دستیابی‌اش به سلاح هسته‌ای» در هم کوبیده شد!
پیت در میان نیروهای نظامی از احترام بالایی برخوردار است و پیشرفت‌های چشمگیری ایجاد کرده است؛ از جمله حذف سیاست‌های DEI (تنوع، برابری و شمول) و افزایش آمار جذب نیرو به سطحی بی‌سابقه.
این شایعه توسط «واشنگتن کام‌پوست» (Washington ComPost) — که یکی از بدترین رسانه‌های این حوزه است — به راه افتاد؛ آن هم با وجود اینکه ما به آن‌ها گفته بودیم گزارششان کاملاً دروغ است.
در واقع، من عمیقاً معتقدم که «گزارش‌دهی» جعلی آن‌ها مصداق خیانت است!
رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69642" target="_blank">📅 20:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69641">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d50525385c.mp4?token=B4D0G9A_QxtJc_OUJdq7c8C4Dcd5P9Q46VgLsOLFZ0zhXq5alMTpNTkJM6QRpdPUwrJUKcckRhOzOGwEtk_R_FtQ4nQQ0Sm-_89hPjWbkNHwGJrRRvbsRV9iZpq2IzDQNa82UDqCIKZTohPV7dUAjb0CRdMhIGUYVrb-yx0HLh-iEDa4nuOHUXfWDNYn6k9WgMs3SgK3bm8jfQ6BAsPHl2A29GsQaHFLTD26M4A4jD7HSQ9xfYgQbbR2Q-mZ8m-LIY8xWBPOWf8h33XUeme42GkfKS8qzFxVyz7JjX6RMsyYlSbV_MTV2_Ab-cnK6iiOwc79bJ_5KoWocT40z-7JooWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d50525385c.mp4?token=B4D0G9A_QxtJc_OUJdq7c8C4Dcd5P9Q46VgLsOLFZ0zhXq5alMTpNTkJM6QRpdPUwrJUKcckRhOzOGwEtk_R_FtQ4nQQ0Sm-_89hPjWbkNHwGJrRRvbsRV9iZpq2IzDQNa82UDqCIKZTohPV7dUAjb0CRdMhIGUYVrb-yx0HLh-iEDa4nuOHUXfWDNYn6k9WgMs3SgK3bm8jfQ6BAsPHl2A29GsQaHFLTD26M4A4jD7HSQ9xfYgQbbR2Q-mZ8m-LIY8xWBPOWf8h33XUeme42GkfKS8qzFxVyz7JjX6RMsyYlSbV_MTV2_Ab-cnK6iiOwc79bJ_5KoWocT40z-7JooWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
دیشب روسیه هم یکی از سنگین‌ترین حملات خودش رو علیه اوکراین انجام داد و اينجوری کی‌‌یف رو ترکوند!
4 فروند موشک مافوق‌صوت زیرکن/اونیکس (3M22 Zircon/Oniks)
24 فروند موشک اسکندر-M و موشک‌های شلیک‌شده از سامانه S-400
115 پهپاد تهاجمی، از جمله پهپادهای شاهد (که بیشترشون از نوع جت‌دار بودن)، پهپادهای Gerbera و Italmas، و همچنین پهپادهای فریب‌دهنده Parodiya
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69641" target="_blank">📅 20:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69640">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtGQ_EZvReeMCKq-zslIvdFveDqbnxScDnTqBwkotipm5tRGEdyAgorMb6hij6E-MrSezwbjmnksv4yddtYYsNmxTKKFrVwbcCzfVHQf1py7QdpYRRqqgWwXDCssV2mhFXd-3c2A1eaWOjNE5J_AeamY016FiQOKmYYcgesoAtHWFHTL17OGl4sByZYqtryGJ9qUWf3gydPzw6zFGywNBFxF7xhmrdvRazrwHtMtEH-iY9j7r1olI8_nPQ-FtdEprTwCo4WRKMumBqX0UwjJETexAqFYMTvWdqlFaCjYFPQwnHZbPefJtR1-DpXEVukdN755_5ja0_-6YD7XidX9dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
پس از استعفای محمدباقر ذوالقدر، فیلد مارشال محسن رضایی به‌عنوان نماینده رهبری و دبیر شورای عالی امنیت ملی منصوب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69640" target="_blank">📅 20:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69639">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇴🇲
سلیمی، عضو هیئت‌رئیسه مجلس: متن اولیۀ طرح «اقدام راهبردی تأمین امنیت و پیشرفت پایدار تنگۀ هرمز و خلیج‌فارس» در کمیسیون امنیت ملی در دست بررسی است.
🔴
براساس این طرح: عبور شناورهای متعلق به آمریکا، رژیم صهیونیستی و سایر کشورهای متخاصم از تنگه هرمز ممنوع…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69639" target="_blank">📅 19:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69638">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇴🇲
سلیمی، عضو هیئت‌رئیسه مجلس: متن اولیۀ طرح «اقدام راهبردی تأمین امنیت و پیشرفت پایدار تنگۀ هرمز و خلیج‌فارس» در کمیسیون امنیت ملی در دست بررسی است.
🔴
براساس این طرح:
عبور شناورهای متعلق به آمریکا، رژیم صهیونیستی و سایر کشورهای متخاصم از تنگه هرمز ممنوع می‌شود.
محموله‌های مرتبط با رژیم صهیونیستی، اعم از نظامی و غیرنظامی، حق تردد از این منطقه را نخواهند داشت.
شناورها یا محموله‌هایی که در اقدامات علیه جبهه مقاومت نقش داشته باشند نیز مشمول ممنوعیت خواهند بود.
کشورها و اشخاصی که به ایران خسارت وارد کرده‌اند، تا زمان جبران خسارت، مجوز عبور از تنگه هرمز و خلیج فارس را دریافت نخواهند کرد.
برای قانون‌شکنان، جریمه‌های سنگین از جمله تا ۲۰ درصد ارزش محموله، پیش‌بینی شده است.
دولت موظف خواهد شد با همکاری نیروهای مسلح، مسئولیت‌هایی مانند هدایت ناوبری، نظارت بر تردد شناورها و حفاظت از امنیت و محیط زیست خلیج فارس را برعهده بگیرد.
این طرح همچنان در مرحله بررسی کارشناسی قرار دارد و مجلس از صاحب‌نظران خواسته پیشنهادهای خود را برای تکمیل آن ارائه کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69638" target="_blank">📅 19:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69636">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a34485680.mp4?token=s3vA089Nht_FJnqbmwAm_NFFa2bYKxpZ-xpNKib9mMLurYPb7X5Fq2b_a_O-yq9h_oX-u_LiMqbGnSuIl3wSwtRkX9tmg3sPS7jldyPFJl0U4w1K9TLxpLlp4eofCjh6drWAZ9hq7swaw1cMDgX53ywcFoPe3Ej2Z6LXS0ePy0Wk0iZpCrUEyPrc_6wuGQsbVIII-INQaCCFtC2tsT0Q_-aUeOejQlzWiMOHEaZ6eFW0TK476b3Fv06i554EnaSsMllogIhuW5HzKBGFNI0cLZE5RRWbLVGwHbCfzuDWanksEXQkCKvtivXrNxRQvZtC7jKbub70mNTd5_qdndLgHrAX9RiY7Vjh0Yz5YaDlAR8CEgm2peFouPAQPhQv7pHQonswHej1d3cImarL4iV5wkY9UULZnfE4WeXxNmmZ-vHb8kUPNrXNPOH8ufn0fVUn4NFH0GI6BITmYHKy7QO0nnnQUTsV8yszUuqsSYCoqJU2kh92J_JwDES90-U3JzKOVsGC2uJRgDalbvcQh85iAJ9WqQ9X_Ki2uUKrSaYL3OjnIhRoVMGiJgm459Qdn0BpNWBmQOnp4SooOTa7f42cr4fGcflt9DR-tduajH8rU8TIIytIBgUfmwtWPK39LZ_s4jFPvPgbpwrGEXAkm9_Dh9NEjtkdo5KfQ59wLEvHEdE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a34485680.mp4?token=s3vA089Nht_FJnqbmwAm_NFFa2bYKxpZ-xpNKib9mMLurYPb7X5Fq2b_a_O-yq9h_oX-u_LiMqbGnSuIl3wSwtRkX9tmg3sPS7jldyPFJl0U4w1K9TLxpLlp4eofCjh6drWAZ9hq7swaw1cMDgX53ywcFoPe3Ej2Z6LXS0ePy0Wk0iZpCrUEyPrc_6wuGQsbVIII-INQaCCFtC2tsT0Q_-aUeOejQlzWiMOHEaZ6eFW0TK476b3Fv06i554EnaSsMllogIhuW5HzKBGFNI0cLZE5RRWbLVGwHbCfzuDWanksEXQkCKvtivXrNxRQvZtC7jKbub70mNTd5_qdndLgHrAX9RiY7Vjh0Yz5YaDlAR8CEgm2peFouPAQPhQv7pHQonswHej1d3cImarL4iV5wkY9UULZnfE4WeXxNmmZ-vHb8kUPNrXNPOH8ufn0fVUn4NFH0GI6BITmYHKy7QO0nnnQUTsV8yszUuqsSYCoqJU2kh92J_JwDES90-U3JzKOVsGC2uJRgDalbvcQh85iAJ9WqQ9X_Ki2uUKrSaYL3OjnIhRoVMGiJgm459Qdn0BpNWBmQOnp4SooOTa7f42cr4fGcflt9DR-tduajH8rU8TIIytIBgUfmwtWPK39LZ_s4jFPvPgbpwrGEXAkm9_Dh9NEjtkdo5KfQ59wLEvHEdE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی تهران برای افراد بالای 30 سال هم مهد کودک زدن !
یعنی شما صبح که از خیابون داری رد میشی ممکنه یه مرد 40 ساله با کوله پشتی عروسکی ببینی
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69636" target="_blank">📅 19:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69633">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6nAyAB8dNzrQPMGFbOcia1a06VIGlEssVgM7VwgPAm6WR03FLsXIzR327FtCGKqRq_nxvoBmqlP_gVO4sFMrquLGWd87w0BN15Y5FUe3tGjrvn-akRdxZ8j68Eq11Ej3XtAyO77tYvqqwO99zySUsp0db8wfhPiYM5L-uSgEYJNA-OmzcwSJkSe-WXYsEi2Ei-fcvtry27cn3CKev1OeZ6tncMdEiQoOQ1-50RJevRI1Fxt-JEBdi5xNTX2_cqf3VdR-NFzmPRchiP69vHEOP8z3xbilnkczZiD0oxwAhhVOCPfPKc8TJHRXA66h3wDgwZcyZHJ1oL3prdZ5kGnfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a607d311.mp4?token=uCrCSISEn4dgbs1K2PrfW9QDPFIuXqr7dA6Xunn7GoJwMVp96iC4DBzE1ITEEw3YaYyAFZFFo1UaiUuGIOm7g5I8YIhMxoOzR1Wq4ioCwGmmkxBxjxrnGkm8aFkdKeBgY1rSMafvyExhlZD1secuo_v-lgXVtLUZtouUSjPjSAYMTLwtanayZI7SNsKKBExSc0hq6QO2KX63APRr4_Og6nGpYzTfkAkoaW6KKbTDgkF8DPMpLGpugSmRe7CK2do7gTQyMmPEG-YMqTzVgMFXL6L77Y9u0svF1vnx-3YN81cl-GKHRBRdUjw0Nq30_H98VJquoyB8_eScFIhdV-NZqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a607d311.mp4?token=uCrCSISEn4dgbs1K2PrfW9QDPFIuXqr7dA6Xunn7GoJwMVp96iC4DBzE1ITEEw3YaYyAFZFFo1UaiUuGIOm7g5I8YIhMxoOzR1Wq4ioCwGmmkxBxjxrnGkm8aFkdKeBgY1rSMafvyExhlZD1secuo_v-lgXVtLUZtouUSjPjSAYMTLwtanayZI7SNsKKBExSc0hq6QO2KX63APRr4_Og6nGpYzTfkAkoaW6KKbTDgkF8DPMpLGpugSmRe7CK2do7gTQyMmPEG-YMqTzVgMFXL6L77Y9u0svF1vnx-3YN81cl-GKHRBRdUjw0Nq30_H98VJquoyB8_eScFIhdV-NZqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69633" target="_blank">📅 19:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69632">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69632" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
با این سایت به راحتی میتونی کل ضرر های جام جهانی رو جبران کنی
بونوس هاش واقعا عالیه
👌🏼
بدون قیدوشرط
❌
با هر 1 میلیون شارژ ،
🤩
🤩
🤩
هزارتومان شارژ اضافی بگیر
🅰️
❌
❌
طرح شارژ رایگان فقط تا پایان مرداد ماه</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69632" target="_blank">📅 19:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69631">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqUEepvtrb3naDk_AO1FHyj62hZm_NnGJw7XtH3Z8CULXYwCPLRVV1MQSjoX0PEo7gxIXEf2QpbBRUTfYyyOJhvjLE7aHjUB6nYtMb1W66-fsdZW5vWbKCejVgxnQgrH6xGNNDRvJAipjKwk6TvA3NWfYcvhI_wTvKbdtHxEjlFlJcrPw9siR5yhXjzV4-1NRnja1a3-G-sQFbE3irtkyE7bwAgBzdCgcDImWfNOacWJcOoNMSUAKi_NrtrnqT5Z6NaX_vBsT_eAoxXvhcSqJtw_TS-_i60-g5WYtTixXohlJlisAJXQAYyCaVbyugfsLOK5mWr_EzwkUhYkMACk4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛍
#بایرن_مونیخ
Vs
#استون_ویلا
زمان: جمعه ساعت 15
🚨
تجربه پیشبینی مطمئن با
🤩
🤩
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🤩
🤩
درصد برگشت وجه در  صورت باخت:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g15
@betinjabet</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/69631" target="_blank">📅 19:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69630">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47221b6a95.mp4?token=qO8gxhP222Zv_2FXO0s28MsfpZJdkxqDM4v3vWSmi1E_gJlFqdoGJkhkl1Rb0_15u8GOgaxLja75S6h2bX2tX0wDpx3MLRtqw81nLQcCVepzEW0NNKjfh687TX9t6Tylo90-M0J6B0rMpONUKtMhgHO1P_bw-RJMMFp0itdm97-zOXyb4y4A7YqEYdFvGzkvqSbsNCLaEb80Dx2-7qaebYXPy2GThhpbQuJ75SIidTS7FJnbAnQGm4KPM7sHzGST3l6RhM2VqVWdaEinlHWrqmdWgfKMqCnqd4BU0BoGa284TMlfACf56ciUYnduWxrfdimNJRQS_X8K0NNfut7L_JrgvDqrBF8-7M0ZVP2qvy4jUsszhNdW1liYkeLEKxSjilWteKFd-QwxPV9rpYdDg8wwDvRn-a2iK4eRKKkWESokp1gB0fWT9EPxYvSnMBASFPmTswe-hQUUisGjf9FCevjJjSJVRaCsazNmDYtPFHRis9UkQb3P3fWquoA7dKw_Br1Q0e3EyiISLjB2iGIR-bt96glMSrPTwGfDZlGdvcxWiuomM17N9A_v29laAMWaek3rj9qXdqIn-TMi9ysv-A6eBgf7vglwADsvnGLW4-U6WC55qAqkNDA7SiXPf54XcMDimE1XGq4NUl_ngj-KxJwOwmrOLt_Q7IAoYw5WYec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47221b6a95.mp4?token=qO8gxhP222Zv_2FXO0s28MsfpZJdkxqDM4v3vWSmi1E_gJlFqdoGJkhkl1Rb0_15u8GOgaxLja75S6h2bX2tX0wDpx3MLRtqw81nLQcCVepzEW0NNKjfh687TX9t6Tylo90-M0J6B0rMpONUKtMhgHO1P_bw-RJMMFp0itdm97-zOXyb4y4A7YqEYdFvGzkvqSbsNCLaEb80Dx2-7qaebYXPy2GThhpbQuJ75SIidTS7FJnbAnQGm4KPM7sHzGST3l6RhM2VqVWdaEinlHWrqmdWgfKMqCnqd4BU0BoGa284TMlfACf56ciUYnduWxrfdimNJRQS_X8K0NNfut7L_JrgvDqrBF8-7M0ZVP2qvy4jUsszhNdW1liYkeLEKxSjilWteKFd-QwxPV9rpYdDg8wwDvRn-a2iK4eRKKkWESokp1gB0fWT9EPxYvSnMBASFPmTswe-hQUUisGjf9FCevjJjSJVRaCsazNmDYtPFHRis9UkQb3P3fWquoA7dKw_Br1Q0e3EyiISLjB2iGIR-bt96glMSrPTwGfDZlGdvcxWiuomM17N9A_v29laAMWaek3rj9qXdqIn-TMi9ysv-A6eBgf7vglwADsvnGLW4-U6WC55qAqkNDA7SiXPf54XcMDimE1XGq4NUl_ngj-KxJwOwmrOLt_Q7IAoYw5WYec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
🇱🇧
ارتش اسرائیل (IDF) اعلام کرد که در ۲۴ ساعت گذشته، مجموعه‌ای از حملات را علیه "اهداف حزب‌الله" در مناطق جنوبی لبنان انجام داده است. این اقدام در پاسخ به انفجار بمب در منطقه مجدال زون انجام شد که در آن دو سرباز ذخیره اسرائیلی کشته و چهار نفر دیگر به شدت مجروح شدند.
ارتش اعلام کرد که این حملات، انبارهای سلاح، مراکز فرماندهی و سایر زیرساخت‌های حزب‌الله را هدف قرار داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69630" target="_blank">📅 18:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69627">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_djTzwtK9pdTbOt5ZqBB1N1T6WgM6vRANX7LuL3rcj5Yw8hV9skDJQaps_duR7ZUBPgtdDNP4CnmJoCPwjdE6V5qmkrhEuPCEdD652yhg3snk0PGwwuH5qADit8cwJx6JYaZl4UX5UQonf_Wfs1Tk_wpNe-72rHwVKoarnDpPrdLFWiN0cFIHKY0JD-Px-ORIko8Z-IaJ7c-GM5-oihfkJ84Kx1XWNbNDLOj1smS0hEcVFJT4GWFd939hYDnRfkROqQvYJ5r9K6kLbGOiX8thXwRN-02joiAUtdXpR4edHfxNyI68tYtWB02jpY_yo5ndfoSOGH543jxFtJBtvgvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb7351e85c.mp4?token=BapYh7Ll6f2Syoqmj23XLQcX7uxN1lhjHzijIwAUnlZ0yUeAKaW2WrJuHSpJZA5KTrqYHd_0RP9kji3GT6pzQQR-noTMMq-uyBPtUY74436fOQn9cdTaumv5JWVREKPJhfVnUvrdeSHjYa1wp8moLgfI_SLNLAFcSGu57cX29odmRjbDuDGynRB1MGQPubmfMLvMZ0rdU0PWQPfVlodSH1C_eIfoWw7fEKeuxYDezc-mNXal0PtXrq4n42Hhj3tXVND05ERZUEKS5o4uEwPusvkrT8y2ptwdU1WAin2sGZ24BBsgsArzqsKVCEeiy73EDX6x8Q170DYy_0YShZPJ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb7351e85c.mp4?token=BapYh7Ll6f2Syoqmj23XLQcX7uxN1lhjHzijIwAUnlZ0yUeAKaW2WrJuHSpJZA5KTrqYHd_0RP9kji3GT6pzQQR-noTMMq-uyBPtUY74436fOQn9cdTaumv5JWVREKPJhfVnUvrdeSHjYa1wp8moLgfI_SLNLAFcSGu57cX29odmRjbDuDGynRB1MGQPubmfMLvMZ0rdU0PWQPfVlodSH1C_eIfoWw7fEKeuxYDezc-mNXal0PtXrq4n42Hhj3tXVND05ERZUEKS5o4uEwPusvkrT8y2ptwdU1WAin2sGZ24BBsgsArzqsKVCEeiy73EDX6x8Q170DYy_0YShZPJ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
زلنسکی:
امروز صبح دو پالایشگاه‌ مهم روسیه رو هدف قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69627" target="_blank">📅 17:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69626">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67d7912f58.mp4?token=n2z6pooBFRba_gzq-x-9E7Gd2ztXtmYneutwFH79juQmLUJ29VpP1WoPA5mxUJxwQJqAJea_I0LDZBhp32AoQudb4BqZU8OYN2J8k8LX9_H7wkFKa8fLDWphSzmtkGxivDDRbdGL8jvPzzzE8jE8OsKA39GLqWa9zCumNYP-LuYVgs8WVWpg51ePuvnD411MXTohrpvG8PuQt96KixDp0UkRV4OeKvE8FHxWruouKvjVO8HFvR08ueVVzYcXyxl_IcOFFq8aSDMgFYcQ0PA_CBY2qjEOht6bjJYnmxiD8MixwMjWp1LpWfVtsUlJbAPHc_00a54whQoSEPqS9An7By6j5zW04ZuFlUti4Yni2U60fURQV4xWXhPpQu12qHRWtnKVb5rkk0pa9HndplCURSk42RtDkv7wAGVz3mO9kLft-hqDmRnv2DDFqCH9HikapEuX93zWI7p2b7V0xZzNhzg0YucKgw99P2vCVhJINjn5UDCySQivzWcMeA3tTCi8O5f0tvLK-b3aw7JMaQ9OdbCxvxCu7bheHthhWa5_JIX8r2IHDt1K6yxeD0eFlOnt1FPTspnsocRm6eXnMmaZvQxLpJ_eXKfrpHTtnX_xMUmw_luCj4ZamvkBSKZ-G7kZ8Sw8IfmW2kJxCbP12JqJqozPBGcINX0fCS3XwWxrMw4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67d7912f58.mp4?token=n2z6pooBFRba_gzq-x-9E7Gd2ztXtmYneutwFH79juQmLUJ29VpP1WoPA5mxUJxwQJqAJea_I0LDZBhp32AoQudb4BqZU8OYN2J8k8LX9_H7wkFKa8fLDWphSzmtkGxivDDRbdGL8jvPzzzE8jE8OsKA39GLqWa9zCumNYP-LuYVgs8WVWpg51ePuvnD411MXTohrpvG8PuQt96KixDp0UkRV4OeKvE8FHxWruouKvjVO8HFvR08ueVVzYcXyxl_IcOFFq8aSDMgFYcQ0PA_CBY2qjEOht6bjJYnmxiD8MixwMjWp1LpWfVtsUlJbAPHc_00a54whQoSEPqS9An7By6j5zW04ZuFlUti4Yni2U60fURQV4xWXhPpQu12qHRWtnKVb5rkk0pa9HndplCURSk42RtDkv7wAGVz3mO9kLft-hqDmRnv2DDFqCH9HikapEuX93zWI7p2b7V0xZzNhzg0YucKgw99P2vCVhJINjn5UDCySQivzWcMeA3tTCi8O5f0tvLK-b3aw7JMaQ9OdbCxvxCu7bheHthhWa5_JIX8r2IHDt1K6yxeD0eFlOnt1FPTspnsocRm6eXnMmaZvQxLpJ_eXKfrpHTtnX_xMUmw_luCj4ZamvkBSKZ-G7kZ8Sw8IfmW2kJxCbP12JqJqozPBGcINX0fCS3XwWxrMw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇰🇵
🇺🇦
روسیه در حال آموزش نیروهای جدید از کره شمالی است احتمالاً به منظور آماده‌سازی برای عملیات آتی در اوکراین.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69626" target="_blank">📅 17:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69625">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d7f55ab9.mp4?token=Jbz1R2qlDWVEUV21gtV_LZjC6L-d8fLi_1RdfXsfRJyIjy4s16RTddMc2xskW9nVnrlYBJdMVvv9f1l2YWTQtHv4blMOULCPbxu5UaNBPhcIEauicKy20n2Sv5WxGdiq6lJ8V3POkLjuqkIsAdQb2VsHui-uFkztXZbsKU0dFXwjA5lsBqeM0p5nLfwNnRSVEkYvhciiqYvviCpq1mZ6hcuWb1l5HWEOfJHQUpbkR3R4vJza4CWYqXYRBmGFPLlo2Ke_mpWijHZkjaRPy7gF-4L3ST-DoZSI1EOAASNgZiHN_FC_HS-BnoRybd58EwuGm24mtcweRD4ahZWypZFq4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d7f55ab9.mp4?token=Jbz1R2qlDWVEUV21gtV_LZjC6L-d8fLi_1RdfXsfRJyIjy4s16RTddMc2xskW9nVnrlYBJdMVvv9f1l2YWTQtHv4blMOULCPbxu5UaNBPhcIEauicKy20n2Sv5WxGdiq6lJ8V3POkLjuqkIsAdQb2VsHui-uFkztXZbsKU0dFXwjA5lsBqeM0p5nLfwNnRSVEkYvhciiqYvviCpq1mZ6hcuWb1l5HWEOfJHQUpbkR3R4vJza4CWYqXYRBmGFPLlo2Ke_mpWijHZkjaRPy7gF-4L3ST-DoZSI1EOAASNgZiHN_FC_HS-BnoRybd58EwuGm24mtcweRD4ahZWypZFq4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
خرازی(برادر زن مسعود خامنه‌ای):
«آیت الله مجتبی خامنه ای سه سال از دفتر رهبری طرد شده بود.
برادر وحید حقانیان(از اعضای بیت رهبر شهید) عضو سیا بود.
پزشکیان الدنگ و پرت است.
قالیباف هیچ چیز از دین اسلام نمیفهمد.
خدا لعنت کنه دکتر مرندی(پزشک علی خامنه‌ای) ملعون.
دفتر آقا فاسد است، حتی دکترش هم فاسد است».
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69625" target="_blank">📅 16:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69623">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/761165b2c7.mp4?token=aygh8u3wawM4WCvXUqTfuhYbxb_1m9vvDQvn55vTSXhDnsmGHK4NcGGtim3Khgtw5JlQhJdVV8ArQo0KFJxpL6goRoAoa_BO4DoZZEvwYjk2fXpd703Bz3hDy2oEIZVHfc5pZJJLEkHSkHnjE1AJHLEkGn5Wt_tHyjvJBoO3xmixH-B_o8kV3dts2Te92IDRwDp9KJDUH1O45blkF8-ACuGb4IDVSm9MJyRf_Ldykm-0BJVdF7qvI4acHFu_h36fe8WZwyrxiSWiSO0jxH95ddT6B1LtGyjiRdXuLPFq99q2NEuWfigvDwugrsYPhKnWv2dJH63hgg2AvVI0JX0Fvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/761165b2c7.mp4?token=aygh8u3wawM4WCvXUqTfuhYbxb_1m9vvDQvn55vTSXhDnsmGHK4NcGGtim3Khgtw5JlQhJdVV8ArQo0KFJxpL6goRoAoa_BO4DoZZEvwYjk2fXpd703Bz3hDy2oEIZVHfc5pZJJLEkHSkHnjE1AJHLEkGn5Wt_tHyjvJBoO3xmixH-B_o8kV3dts2Te92IDRwDp9KJDUH1O45blkF8-ACuGb4IDVSm9MJyRf_Ldykm-0BJVdF7qvI4acHFu_h36fe8WZwyrxiSWiSO0jxH95ddT6B1LtGyjiRdXuLPFq99q2NEuWfigvDwugrsYPhKnWv2dJH63hgg2AvVI0JX0Fvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
❌
🇸🇦
در حملات موشکی یمن به مواضع نظامی عربستان تاکنون بیش از 30 کشته شناسایی شده و انتظار میره تعداد تلفات بیشتر بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69623" target="_blank">📅 15:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69622">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇮🇷
🇴🇲
الحدث:
توافقی میان ایران و عمان در خصوص بازگشایی تنگه هرمز در ازای احتمال لغو محاصره آمریکا، قریب‌الوقوع است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69622" target="_blank">📅 15:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69621">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AA4HcWauSOGhWMOe6KKpGoqh_1jqp9Q6KhiireVO6VyPbwA9Upam5WATQl-ZUBtvTiQnZpkewkbVkACivCwJ3FdQcbdu7wkvpkms57pZDizkanoXqQy601up1cRopTU90KGe51xGe-l8pi3ocSrLAlZgHsd3relpkar30EC-WIypC9Zrl_bt8JgZmS6-telJW5eFWPa0gDcApG5zr6zovQRe_c_ibeVasNkauMOLxXF8-QqNKKwcFlolWERRLEtTpmLL_cyUYzsa4IEmySNF1cM0AckWMv2bCEVQ9l_s1leXTRq5xO0XfU5JOb1rmM_-lADKb2vLzkIHEVuHk35gWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
🇺🇸
واشنگتن پست:
🗣️
ترامپ به طور خصوصی به حامیان مالی جمهوری‌خواه خود گفته است که می‌خواهد جی‌دی ونس در سال ۲۰۲۸ پیروز شود
و از عباراتی مانند «ما باید جی‌دی را انتخاب کنیم» استفاده کرده است.
مشاوران تأکید می‌کنند که او هنوز به طور کامل در مورد جانشین خود به توافق نرسیده است و هنوز رقابت بین ونس و مارکو روبیو، وزیر امور خارجه، را حفظ کرده است.
🔴
یک منبع این موضوع را اینگونه خلاصه کرد:
«جی‌دی دارد به موفقیت می‌رسد و ترامپ آن را می‌بیند.» و خاطرنشان کرد که ترامپ دیگر به طور معمول نمی‌پرسد «جی‌دی یا مارکو؟»
البته او با مشاورانش همچنان برای این انتخاب در حال مشورت است
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69621" target="_blank">📅 15:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69620">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDJcwQRM43hwqP1-_x3PiE9bTBjHjw8mx8mdTXGuN9cLrc5eAvZmV73tNYx36Muub0-nX9cmORVQWlWO1ooEV86g0yTjnqPuEu4wb8fL7IPqiQaviLHIzrg6MtHjb2a3WFDfBgQX3ASB8mJ1P7PvBrYbHQNV7j8AzmA3fPz0tFSKJHCAutTuztDnvfc1mof-qCn-pMpYQO16oEuZiOC66kVEz-a071PpIwp1OjV5GyKjJHUz2RuKPgdbaAtZH1XPjvrrEccZWuT1h1lSwne6lINupQt0EuE4zELjs2gGWWEhJuh-rJIjyj6Ao1Cdr014N6enfW2br6jAkzaga0OBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
آمریکا از ناوشکن جدید کلاس Arleigh Burke Flight III؛ USS William Charette رونمایی کرد
نیروی دریایی ایالات متحده مراسم به آب‌اندازی و نام‌گذاری ناوشکن جدید
USS William Charette (DDG-130)
را برگزار کرد. این شناور از نوع
Arleigh Burke-class Flight III
بوده و بخشی از برنامه نوسازی ناوگان ناوشکن‌های موشک‌انداز آمریکا محسوب می‌شود.
◀️
نام‌گذاری به افتخار «ویلیام چارت» از نیروهای نیروی دریایی آمریکا که نشان افتخار Medal of Honor دریافت کرده بود.
🔼
ارتقای سامانه‌های رزمی
نسخه Flight III نسبت به نمونه‌های قبلی Arleigh Burke دارای بهبودهایی در بخش سامانه‌های دفاع هوایی و موشکی است.
مهم‌ترین بخش این ارتقا، استفاده از:
◀️
رادار AN/SPY-6(V)1
این رادار آرایه فازی فعال (AESA) بخش اصلی ارتقای ناوشکن‌های Arleigh Burke Flight III است. این سامانه برای کشف، رهگیری و مقابله با تهدیدات هوایی و موشکی طراحی شده و نسبت به رادارهای نسل قبلی توانایی بالاتری در شناسایی اهداف دارد.
◀️
سامانه رزمی Aegis
سامانه Aegis یک سامانه یکپارچه فرماندهی، کنترل و مدیریت تسلیحات است که داده‌های حسگرها را دریافت کرده و امکان کشف، رهگیری و درگیری با تهدیدات مختلف را فراهم می‌کند. این سامانه هسته اصلی توان رزمی ناوشکن‌های Arleigh Burke محسوب می‌شود و در نسخه Flight III با رادار AN/SPY-6(V)1 یکپارچه شده است.
❓
نقش عملیاتی
ناوشکن‌های Flight III برای مأموریت‌هایی مانند:
⬇️
دفاع هوایی ناوگان
⬇️
مقابله با تهدیدات موشکی
⬇️
اسکورت گروه‌های رزمی دریایی
⬇️
عملیات چندمنظوره سطحی به کار گرفته خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69620" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69619">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b6e5f9de.mp4?token=CAo4oc30J5vpSy2AttzY9HGmcNMt8Bh5O8OYxcKX9aOQMerxgDZmXNJo4WV8rPckQaCaNylZHsSXch4OAeOeLZiDRz8g2FGECXLGGj7OpYIg_RE6ikqr9g6Vc5hUQJCVREJrKW0yliu4KV6Wfq95z2_qX4Wqp7N1rpZs1GMndEzPTYXI9yTXWxv1YssSwFNcqXEUWrX6WurzZUnYQ6zSSqnW4bhwqrfPxpXyAPUxwhwOFsj2zBe0JmvUtpHI-ixv0A4o0-VRm-NAbtVA1JxojBfzGvCFea0W4ErIL_KFLuccSne2Z9f_fo7M7N5CkzVApt6GUksH037SjsunnaHpTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b6e5f9de.mp4?token=CAo4oc30J5vpSy2AttzY9HGmcNMt8Bh5O8OYxcKX9aOQMerxgDZmXNJo4WV8rPckQaCaNylZHsSXch4OAeOeLZiDRz8g2FGECXLGGj7OpYIg_RE6ikqr9g6Vc5hUQJCVREJrKW0yliu4KV6Wfq95z2_qX4Wqp7N1rpZs1GMndEzPTYXI9yTXWxv1YssSwFNcqXEUWrX6WurzZUnYQ6zSSqnW4bhwqrfPxpXyAPUxwhwOFsj2zBe0JmvUtpHI-ixv0A4o0-VRm-NAbtVA1JxojBfzGvCFea0W4ErIL_KFLuccSne2Z9f_fo7M7N5CkzVApt6GUksH037SjsunnaHpTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
مراد ویسی تحلیلگر ارشد اینترنشنال:
قاجاریه در عهدنامه‌های ننگین گلستان، ترکمانچای و آخال، سرزمین‌های ایرانی در شرق و غرب دریای خزر رو به روسیه واگذار کرد.
حالا جمهوری اسلامی، از سهم ایران در دریای خزر به دلیل نوچگی روسیه می‌گذره.
مردم ایران، این روزها رو برای تاریخ به خاطر بسپارید؛ جمهوری اسلامی در حال رقم زدن خیانتی بزرگ به ایرانه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69619" target="_blank">📅 14:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69618">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de4ded641.mp4?token=KmZvwMcjs7jezlO2UPndyrALIwZUx5cEfNnhKN1vUk-trWgojOOAYw6eFnSbTyGdOVCfBGMtL6Xfm4W1ukAUu3h7YAJgz_FuThRgD3Z_BalqiYM8SOTCykgSBbSM4d_ZLwPxg20d-dKoe3iTbkRdHSnwtjuR4C0Kl3ppCNcX1gv965Ah0iPR1sTybvzCqahGMVI6BeHTo4fNAXYLHzs5aEU1ahKXH5yeYuORpjbR89eHq-mPmT2T2WQAi68wNrFhLHssx8kfin34tjja5hvYA6auYfNW0lqtLFOWFqDDZen5V2n_bUzAPHAiuHcAsxHWt_y0iF4c2Zm564zMdKojmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de4ded641.mp4?token=KmZvwMcjs7jezlO2UPndyrALIwZUx5cEfNnhKN1vUk-trWgojOOAYw6eFnSbTyGdOVCfBGMtL6Xfm4W1ukAUu3h7YAJgz_FuThRgD3Z_BalqiYM8SOTCykgSBbSM4d_ZLwPxg20d-dKoe3iTbkRdHSnwtjuR4C0Kl3ppCNcX1gv965Ah0iPR1sTybvzCqahGMVI6BeHTo4fNAXYLHzs5aEU1ahKXH5yeYuORpjbR89eHq-mPmT2T2WQAi68wNrFhLHssx8kfin34tjja5hvYA6auYfNW0lqtLFOWFqDDZen5V2n_bUzAPHAiuHcAsxHWt_y0iF4c2Zm564zMdKojmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو ای از صحبت های یک دختر درباره مادرش:
❓
کی گفته هر مادری قابل احترامه؟
از میزان اشغال بودن مامانم اینو بگم که تو سن 13 سالگی پریود شدم و وقتی بهش گفتم منو تو خونه 3 روز زندونی کرد و گوشیم گرفت و کلی کتکم زد
بهم گفت تو چه گوهی خوردی تو هنوز بچه ای چرا باید پریود بشی؟ و این خون یه چیز دیگس!
از 12 سالگی هم منو میفرستاد سرکار میگفت باید خرج مدرسه و خونه رو کمک کنی بدی!
همینطور که اینارو میگفت تا اول دبیرستان بیشتر نذاشت درس بخونم و 15 سالگی ترک تحصیل کردم
مامانم گفت لازم نیست درس بخونی باید بیشتر کار کنی چون خرج ها رفته بالا اجاره خونه بیشتر شده باید بری کار کنی
به محض اینکه هم 18 سالم شد از خونه زدم بیرون و الان 6 ساله نه میدونم کجاست نه شمارش چیه نه باهاش حرف زدم
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69618" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69617">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e79de90eb9.mp4?token=F5l2K6VzjiaqXb5e-4QIbTZeyq8MoBvOUYJarqMBefOeUWUSoYK9PjXMxB9cMLUAdSdQ_r9WITLrFBCV9282Q6MEqN7iQZKSwcQt2ZF-SrCm_Ibu176v86vU_EAaIhHFew5BeBCy3MlFabRtpNVfGj7VYHwy6YMKvgFobN8oO0Zsz7eMRjBDvz11ds-e1BE2Udoj0AmFuWIMGNhXomd4JCW_tMLeOvFx1ZP75suU7TNIPHwgtAtUQ-8EzEpCWsz9n4SM0J9lLw0Ih7D6ZivKR7jkz3o5tETzqbT1VUFvcKRJe7l_mT2sbOzwNfZTltwfX-6J7nUlQBY1_C3TAGYknQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e79de90eb9.mp4?token=F5l2K6VzjiaqXb5e-4QIbTZeyq8MoBvOUYJarqMBefOeUWUSoYK9PjXMxB9cMLUAdSdQ_r9WITLrFBCV9282Q6MEqN7iQZKSwcQt2ZF-SrCm_Ibu176v86vU_EAaIhHFew5BeBCy3MlFabRtpNVfGj7VYHwy6YMKvgFobN8oO0Zsz7eMRjBDvz11ds-e1BE2Udoj0AmFuWIMGNhXomd4JCW_tMLeOvFx1ZP75suU7TNIPHwgtAtUQ-8EzEpCWsz9n4SM0J9lLw0Ih7D6ZivKR7jkz3o5tETzqbT1VUFvcKRJe7l_mT2sbOzwNfZTltwfX-6J7nUlQBY1_C3TAGYknQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلمی که یه خانم حامله ایرانی از میزان تکون خوردن بچه‌اش توی شکمش منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69617" target="_blank">📅 12:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69616">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZrOuSPggZs_r1sMkfcCGo3zbaT_67y1-j42uckEq8F6nFmIEwNhQxg-0bGIl89B6fPecfYxZ-lmt7hmbJtksBkVIseskN48rybobMdR5AOe1OLSPhh_t23k_BNm2cVNIsAWmZtiqb7w3XPF1d92RORfLhSZQcg2TICwI2yo_luuAZFxNxsQbPWtioLeX4h7Yag6xPBl7Hj_CWk20quYt4f1GTB4qiW0lXbBHnPRrA4PkGb1BMUd-tMJGpyzVmvpf6VnfwjZ0KkpsYUVZS8bJL6nUfLhXZ9SgQWYE4MkYjFIH2ijM6RwaZ0emJh-Q8Sy08BVl9S7QTwb07GnfoeKuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش واشنگتن پست
:
دونالد ترامپ، رئیس جمهور آمریکا، هفته گذشته در کمپ دیوید با پیت هگست، وزیر جنگ، درباره کمبود شدید مهمات در ایالات متحده به شدت صحبت کرد و از او خواست توضیح دهد که چرا به نظر می‌رسد او در مورد این کمبودهای شدید که اکنون تهدیدی برای محدود کردن گزینه‌های نظامی است، فریب خورده است.
ترامپ در جریان جلسه کابینه در کمپ دیوید به هگست گفت که فکر می‌کرد مشکل کمبود مهمات "حل شده است". هگست از خود دفاع کرد و استیفن فاینبرگ، معاون وزیر جنگ، را مقصر دانست و گفت که او اطمینان حاصل نکرده بود که ترامپ به طور کامل از میزان کمبودها مطلع باشد.
در همین گزارش، روزنامه واشنگتن پست به نقل از یک مقام آمریکایی، اعلام کرده است که بیش از ۱۳۰۰ موشک بالستیک تاکتیکی MGM-140 ATACMS ارتش ایالات متحده در جنگ با ایران مورد استفاده قرار گرفته و تقریباً هیچ‌کدام از این موشک‌ها باقی نمانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69616" target="_blank">📅 12:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69615">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58d9f385e0.mp4?token=E-cSJsIhcuFzgerbmiSe-KVzj-IpEARKbgaYzxleo5B26vTdcWfNj-4o09bIF47S16eityjXhjFqH20BVrjwu_RiTIOI3kc_Nc5hksd4jtCmD-Kejgi3whkEpWfG3PorcyTbCpKyAHK65gAswLOppV6rqFm6ypwOp6xm5Zo5nFkAl52kU6P2T4KYbiZPXWJP3A-4kB3bot_f_5vchkUcRhgO2O4MEsK6QD2DMVX90PIOwwUrxeVaT0Qsogb6O6Clic-6n-4FSstxTRL8F9k-MqBt81yfkLwkpr1X0x3-z9T3_cGcWhXx9VInWbt6Zfhcf7dglZcea1ZbHc552KBVFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58d9f385e0.mp4?token=E-cSJsIhcuFzgerbmiSe-KVzj-IpEARKbgaYzxleo5B26vTdcWfNj-4o09bIF47S16eityjXhjFqH20BVrjwu_RiTIOI3kc_Nc5hksd4jtCmD-Kejgi3whkEpWfG3PorcyTbCpKyAHK65gAswLOppV6rqFm6ypwOp6xm5Zo5nFkAl52kU6P2T4KYbiZPXWJP3A-4kB3bot_f_5vchkUcRhgO2O4MEsK6QD2DMVX90PIOwwUrxeVaT0Qsogb6O6Clic-6n-4FSstxTRL8F9k-MqBt81yfkLwkpr1X0x3-z9T3_cGcWhXx9VInWbt6Zfhcf7dglZcea1ZbHc552KBVFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این نقاشی هنرمندانه با ایجاد خطای دید، باعث می‌شه دیوار صاف خونه طوری به‌نظر برسه که انگار داره به سمت بیرون خم می‌شه و برآمدگی پیدا کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69615" target="_blank">📅 11:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69614">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EODbq3-D-XduwTy2z80-I8ayVFp_adNE-MFcSTDYcYawt4-7MmwYBUzbob8wTQs2wR_YHFJKVgdyl-3aTH6gbt3JNj_2UkREui8CsmjZw870NDO8qYkPKyqVsWo0ssgFaTFH8Y6hn8hReTG2fuMS9COF-J-9hsCvWdJ9Squm_C4iFNq7HajL3WYUl5XtlEkY0MVHKwQEfpQgP_GofvChKfynVPZpKgRW_QFUgZSjxnG6BILhm9TOM4AZGnkFzvmwrlb17ao0AmhzJwOISiOheg44wT9HUZrfPurJkod0PdJfU1bdZJrujenvFclSsxrMHX3EY_hCy4uTtq6KFMVxiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرکز عملیات تجارت دریایی بریتانیا (UKMTO)؛
پس از دریافت گزارشی از ناخدای یک نفتکش در حال عبور از تنگه هرمز، هشدار صادر کرد؛
این ناخدا گزارش داده بود که صدای دو انفجار را در فاصله تقریبی ۹ مایل دریایی در جنوب شرقی «کومزار» عمان شنیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69614" target="_blank">📅 11:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69613">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b71c6863.mp4?token=KvQ3r83tnXUE38awRgzpoArHM8oeQuOy1Cw3WNrrwWJPOI5htDvDXUxuxNrJlJOyDEnN0SJfONFOTWuLe2gME3Ngsm46do5h94cX4R1uJsodYFEgj8fz66qu0Ix3rBlqeGlKtOADOcF2CdGdj94GWcqE5g_qDamOmbPs5pPtHz7sXs3-IySM_xcqKJJiELpZ0YsX9WmrP_NV6WMilaLluIA0AGTl5hX1pwJUAEiXU-OM5kDR-HB6498YwQihFx-GOh88lXFamHXPPgaQsc1dF4gCbIRd8N6GCK-x_gPzdvbKIspxvJk-kKcXpnH_l6nhPWDcYjpUgJAY9Qh7s16uuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b71c6863.mp4?token=KvQ3r83tnXUE38awRgzpoArHM8oeQuOy1Cw3WNrrwWJPOI5htDvDXUxuxNrJlJOyDEnN0SJfONFOTWuLe2gME3Ngsm46do5h94cX4R1uJsodYFEgj8fz66qu0Ix3rBlqeGlKtOADOcF2CdGdj94GWcqE5g_qDamOmbPs5pPtHz7sXs3-IySM_xcqKJJiELpZ0YsX9WmrP_NV6WMilaLluIA0AGTl5hX1pwJUAEiXU-OM5kDR-HB6498YwQihFx-GOh88lXFamHXPPgaQsc1dF4gCbIRd8N6GCK-x_gPzdvbKIspxvJk-kKcXpnH_l6nhPWDcYjpUgJAY9Qh7s16uuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
حسن روحانی: اقلیتی می‌گوید اگر این جنگ تشدید شود، امام زمان زودتر ظهور می‌کند! می‌خواستند برای سخنرانی امام زمان در تهران جایگاه درست کنند.کاسبان تحریم ممکن است خوشحال باشند که جنگ ادامه پیدا کند.
عده‌ای دنبال کاسبی از جنگ هستند و از ادامه آن خوشحال می‌شوند.
در جامعه ما گاهی یک اقلیتی هستند که حرف‌های عجیب و غریب می‌زنند.
یک اقلیتی هستند می‌گویند اگر این جنگ تشدید شود و گسترش بیابد، امام زمان زودتر ظهور می‌کند! برای ظهور امام باید جنگ را تشدید کنیم.
خب یک عده افرادی هستند که نه با اسلام آشنا هستند و نه با مهدویت آشنا هستند.
یک عده هم هستند که دنبال کاسبی هستند، همان کاسبان تحریم در واقع. آن‌ها هم ممکن است خوشحال باشند که جنگ و آشفتگی ادامه پیدا کند.
افرادی هم هستند که ممکن است یک تفکراتی داشته باشد که ما باید برویم جهان را بگیریم و تصرف کنیم و همه را به اصطلاح هدایت کنیم.
من در سال ۸۳ رفتم خدمت رهبری برای یک موضوعی، بحثی پیش آمد در آنجا، ایشان به مناسبت فرمودند که فلان آقا، اسم بردند، آمده بود پیش من و از من سؤال کرد که می‌خواهد یک جایگاه بزرگی درست کند در یک میدان بزرگ در تهران. گفتم جایگاه بزرگ برای چه؟ گفت برای اینکه وقتی امام زمان آمد و خواست سخنرانی کند یک جایگاه مناسب و باعظمتی باشد در شأن ایشان.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69613" target="_blank">📅 11:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69612">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEX13jEFcdikcO3uyXDBLpJ3PnavghmihNplatb8kSTZzX-ckXmtsqSjDCn2W8groUQ49nf3pQ77v0O2LF61-qvVhzKajSrC0Y16jU9MiGMCCU6lRT1dVp39MvVZNp2Pw1K0CLC-off__h2SR7HUfdBsRxR_w45DLcCsbkTQlzLrfVnRN7V-0sIFii8IW65I_phMepF7FmIP1h4UXEkLlzjFGVRj05KlSLCh6l9g3iLkE6crRtFXrd8PdZ9Y1YhHYVBEiwyfKSwLjScgLuydlL9ScRcwGaFljFunt42yItVVQqu4yIxct72AvF2Q9MxkBBg_6o9BSUEM8X0G1hXoGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐
اکانت رسمی تلگرام زیر توییت یه کاربر:
یه نفر پرسیده بود: می‌خوام بدونم دورف(مالک تلگرام) کجا قایم می‌شه؟
تلگرام هم جواب داده:
درباره خودش چیزی نمی‌دونم، ولی معمولاً منو خونه مامانت می‌تونی پیدا کنی
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69612" target="_blank">📅 11:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69611">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69611" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پنالتی
راحترین بازی پولساز
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید راحتو سریع برنده شو
👌🏼
💖
مرجع
بازی های روز دنیا در ‌پلتفرم جهانی بت اینجا
⭐</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/69611" target="_blank">📅 11:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69610">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58d65b8db.mp4?token=Vzx3eYACW_yW3WlzeqjmM2Y9HRlVKySdVmtgTdjpkK0o2XM3vN0RhkQq67xKCPXUZ6_Mm8EK8FAs5M7xz6rHyftYBXXR-NdJLYMyhSk4__QnFr3K0Ed3Z1NB-lRDSzFm5_ARsJNfXweU9TGv8ZKjF5qM9Kaf0FqGJ3qlVS6lwiykWYGXzpxvZP-T_ZzDhcc8xN0gz0ChLjqCLJzdVDGGoCFcjijrgLvKpcO3rf3qzgS2WinMvU0q6Pd2VMH58euN_nEqIPEspEcCJE9G9bvGiK_pcuuEBfFmpBHV-gll3HJ6vTw3___1FqHfk9Hn3NzwcVZI03OhodohXyzX4dF3rzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58d65b8db.mp4?token=Vzx3eYACW_yW3WlzeqjmM2Y9HRlVKySdVmtgTdjpkK0o2XM3vN0RhkQq67xKCPXUZ6_Mm8EK8FAs5M7xz6rHyftYBXXR-NdJLYMyhSk4__QnFr3K0Ed3Z1NB-lRDSzFm5_ARsJNfXweU9TGv8ZKjF5qM9Kaf0FqGJ3qlVS6lwiykWYGXzpxvZP-T_ZzDhcc8xN0gz0ChLjqCLJzdVDGGoCFcjijrgLvKpcO3rf3qzgS2WinMvU0q6Pd2VMH58euN_nEqIPEspEcCJE9G9bvGiK_pcuuEBfFmpBHV-gll3HJ6vTw3___1FqHfk9Hn3NzwcVZI03OhodohXyzX4dF3rzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آقاآآ این بازی
#پنالتی
چقدر خفنه
⚽
🟢
بازی خیلی حرفه ای و‌
#پولساز
پنالتی فقط‌ پلتفرم جهانی و معتبر
#بت_اینجا
✊
همین الان ویدیو
#آموزش
پنالتی زدن ‌رو ببین و با شارژ اضافی
🤩
🤩
درصدی که سایت بهت میده.
💖
حتما ویدیو
#آموزش
رو ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r15
@betinjabet</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69610" target="_blank">📅 11:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69609">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1558a77094.mp4?token=mqdDePgx6ChujnH-So-T438paxZ2W_rxx5JQ1NBTJllmSwqjkadTusJLt7zKT5tPh3ihxmsJoUYyJAbpntjghSBoRyqpjwfIHi8BLlYklgZa4JaiBJ8zvnG9rxdjNJ53rdcjFKKLUvBm8uuvg7YeYjtCVvahytpP1PC5-f7IOcDPpHWOb1HQ1pXbbzuclvOi69cfBTkNwIbBJNHXmIK9zoAOgrV3lSfIqggYhE_u1WWmsMmNWxcV3wFiukzqxVrBBs5fC2LuMQ05706ql8uC3Hfv3Haq93FshTmRZqYya3N1AHgd1PC7oFaCoh6Qsy3XeT6CdnA6UWgpd0gc-YRGmA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1558a77094.mp4?token=mqdDePgx6ChujnH-So-T438paxZ2W_rxx5JQ1NBTJllmSwqjkadTusJLt7zKT5tPh3ihxmsJoUYyJAbpntjghSBoRyqpjwfIHi8BLlYklgZa4JaiBJ8zvnG9rxdjNJ53rdcjFKKLUvBm8uuvg7YeYjtCVvahytpP1PC5-f7IOcDPpHWOb1HQ1pXbbzuclvOi69cfBTkNwIbBJNHXmIK9zoAOgrV3lSfIqggYhE_u1WWmsMmNWxcV3wFiukzqxVrBBs5fC2LuMQ05706ql8uC3Hfv3Haq93FshTmRZqYya3N1AHgd1PC7oFaCoh6Qsy3XeT6CdnA6UWgpd0gc-YRGmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی که حامیان حکومت برای موشک‌ها درست کردن
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69609" target="_blank">📅 10:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69608">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc659092fa.mp4?token=QfHkNIIS4pSXEFZCT54HI5ZE2fDJbErOxPjj0ekDT6RJ1wUAthZirGVJ1uS5CGHtsQp_wG8e7cNzByPGZH8KHHN98HaQmd2iGckGY8VM2neu-IwECSHR_ZMz714MOIb8-xBcLCHsoqQa1w7SfIU0kPN2ocXaQ2E9i4ID8EHEtH99OF3nhYbRi-jnV5EkI7C1TT6fiA7XmKNTLDB8zYnOGRKwH537u5w9hf3VIeLpMC73yAg5omCRzbLkR_wMHsyYFT7-wtKYFQNV_1jVC4-o7ZlW2zrQoZngy9NOZRmhk_eXyUP4yt_KyEQBUo6jibALoz55hEdb_l4G95koAlL4DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc659092fa.mp4?token=QfHkNIIS4pSXEFZCT54HI5ZE2fDJbErOxPjj0ekDT6RJ1wUAthZirGVJ1uS5CGHtsQp_wG8e7cNzByPGZH8KHHN98HaQmd2iGckGY8VM2neu-IwECSHR_ZMz714MOIb8-xBcLCHsoqQa1w7SfIU0kPN2ocXaQ2E9i4ID8EHEtH99OF3nhYbRi-jnV5EkI7C1TT6fiA7XmKNTLDB8zYnOGRKwH537u5w9hf3VIeLpMC73yAg5omCRzbLkR_wMHsyYFT7-wtKYFQNV_1jVC4-o7ZlW2zrQoZngy9NOZRmhk_eXyUP4yt_KyEQBUo6jibALoz55hEdb_l4G95koAlL4DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇮🇷
پزشکیان:
حوادث دی‌ماه پارسال قابل فراموشی نیست؛
یه عده بیگناه هم قاطی اون اون افراد تو خیابون ها شده بودن
وقتی روند به شورش رسید اتفاقات سختی رخ میده و ما دیدیم شرایط اینطوریه گفتیم کد ملی اعلام کنن و هرکس اضافه تر میگه هست خب بگه
کسانی که کشته‌شدگان رو ۳۰-۴۰ هزار نفر اعلام می‌کنن، نامرد و وطن‌فروش هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69608" target="_blank">📅 10:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69606">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8bd143a1.mp4?token=MEk9OZCR2iPu2bUegePqVg7hM61yi0rU_r7l5ZhJooA3lrtxO9AI5bzPx48Dx6ZD46i7BlR7QDwavqYbGmHcQoKbqJYcNjzgL2vTvXVSek0J0OSHeKxM0yR3FYHnaSDuRKGJckDauCZmj8F94DjXdQk9UkrtKxLvohFODpRxlhRzDGyuVG2LLPwhdnTUooH8E3UzlK2XaMlHg-EQbB8xOQhSY0qBUsXKVQ-5n77B8rwvMxTVVICWZWc0Fl4Sd_ijp3BTzaKbX8k6LAm1CwlfxvcOZls4vBkO7AagutgWGmT60y-AUcTiL8-ooX2Q0eTsf7Aqtcc5vLryYXqpZ_xseg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8bd143a1.mp4?token=MEk9OZCR2iPu2bUegePqVg7hM61yi0rU_r7l5ZhJooA3lrtxO9AI5bzPx48Dx6ZD46i7BlR7QDwavqYbGmHcQoKbqJYcNjzgL2vTvXVSek0J0OSHeKxM0yR3FYHnaSDuRKGJckDauCZmj8F94DjXdQk9UkrtKxLvohFODpRxlhRzDGyuVG2LLPwhdnTUooH8E3UzlK2XaMlHg-EQbB8xOQhSY0qBUsXKVQ-5n77B8rwvMxTVVICWZWc0Fl4Sd_ijp3BTzaKbX8k6LAm1CwlfxvcOZls4vBkO7AagutgWGmT60y-AUcTiL8-ooX2Q0eTsf7Aqtcc5vLryYXqpZ_xseg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
باقر خرازی (برادرزن مسعود خامنه‌ای):
ما باید از جمهوری اسلامی گذر کنیم. علت اینکه این الدنگ (پزشکیان) رئیس‌جمهور کشور شده و بی‌حجابی کشور را گرفته این است که هنوز از جمهوری اسلامی به حکومت اسلامی گذر نکرده‌ایم.
خدا لعنت کند شورای نگهبان را که این "آشغال" را توی پاچه ملت کرد.
چهل سال است با آقامجتبی رفیقم؛ او بسیار تندتر از پدرش است؛ اما یار ندارد.
باید به نیت حضرت فاطمه از هر شهر ۵۳۰ نفر جمع کنیم و به تهران سرازیر شویم و کار دولت پزشکیان را تمام کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69606" target="_blank">📅 09:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69605">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e59bbff0.mp4?token=MB8f0VvKXzdp7O6zUxiFRIbY0bapKlyaRpDvO8iYVWHzZHsc-71OFfjiIewQc80FN8H3UzQqZgnaXinILjZxMFdLbB9kG9z5tG1sAexypfA8-yBUz21rm00jrVvOg8_sgC7YlqozXU3i50iu96wO93DsdjldDGqxNt7-Dih-wk2UMwul5Zy3zpbbg1bsfS-l-EACAI46uThZCjNeM7qRy1nDkOpJDsTmo8bWbbv0_4TPLMzYxnKn7F5Yq4xOQr0HaRBJLN_x6xHN0mCd2jmOSUaIF81iSinvKd1bGlazaLToGw9chcbU-nAEiZFtJSjpSl8OX-4IlGMg9E-fdWDU0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e59bbff0.mp4?token=MB8f0VvKXzdp7O6zUxiFRIbY0bapKlyaRpDvO8iYVWHzZHsc-71OFfjiIewQc80FN8H3UzQqZgnaXinILjZxMFdLbB9kG9z5tG1sAexypfA8-yBUz21rm00jrVvOg8_sgC7YlqozXU3i50iu96wO93DsdjldDGqxNt7-Dih-wk2UMwul5Zy3zpbbg1bsfS-l-EACAI46uThZCjNeM7qRy1nDkOpJDsTmo8bWbbv0_4TPLMzYxnKn7F5Yq4xOQr0HaRBJLN_x6xHN0mCd2jmOSUaIF81iSinvKd1bGlazaLToGw9chcbU-nAEiZFtJSjpSl8OX-4IlGMg9E-fdWDU0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
ممکن است دوباره قیمت نفت را «بالا ببریم»:
«قیمت ۷۵ دلار است. ممکن است مجبور شویم دوباره آن را بالا ببریم. خودتان می‌دانید وقتی آن را بالا می‌بریم چه اتفاقی می‌افتد.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69605" target="_blank">📅 02:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69602">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79ecaba828.mp4?token=LKdj3NB_QUA_EviVdIjsLfJQH6Lp0UYbh8ZtEBzJxBWOmSuUO1qqUso2I9C1AWlNZ0TgB_iXubtoP46wrCG8l00Fjeohre9fAzEgdGdDXKG5OoAom9OJ3awPpqq00oTlTTdbPUR3N5RQ8lEkiPZAOGQm2Zxav961TSjvMarRtNynsX-slIpUi991Z6Yru-JXIbVo6pvSu6DYqWCGhkhe5dsa8PScKvlGX3F3w5tXDHDVxgwVYlRIGnRBtndtzhqnnFxVt2uTM3lBwCGMzTbTsFfG1-wXZ9WJnwOja_xVyYhKt6y6t09Ei9ZMMrNuu5ptrZvyBjX2vMUS-_mnLknKsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79ecaba828.mp4?token=LKdj3NB_QUA_EviVdIjsLfJQH6Lp0UYbh8ZtEBzJxBWOmSuUO1qqUso2I9C1AWlNZ0TgB_iXubtoP46wrCG8l00Fjeohre9fAzEgdGdDXKG5OoAom9OJ3awPpqq00oTlTTdbPUR3N5RQ8lEkiPZAOGQm2Zxav961TSjvMarRtNynsX-slIpUi991Z6Yru-JXIbVo6pvSu6DYqWCGhkhe5dsa8PScKvlGX3F3w5tXDHDVxgwVYlRIGnRBtndtzhqnnFxVt2uTM3lBwCGMzTbTsFfG1-wXZ9WJnwOja_xVyYhKt6y6t09Ei9ZMMrNuu5ptrZvyBjX2vMUS-_mnLknKsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ترجیح می‌دهم با ایران توافق کنم، چون نمی‌خواهم آدم بکشم.
ایران به ما احترام می‌گذارد. آن‌ها به ما احترام می‌گذارند.
ما در حال گفتگو هستیم. ببینیم چه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69602" target="_blank">📅 01:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69601">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca4b2dd818.mp4?token=fSS-MEZnlJBh7olT5VouV-qK6bA0K2zyiIAsK0ZES-MPl9_d3ZVfMFeSG5OWk5-VXQptnzZzIKEbjmlR5Joa416Np2XjtPm1TCaTb8OPzvhcw8wkl3YiADTvGA6hKAiadHfO536r28Sc037_DsnOHzUQQDcQlVog-3XBGtOPG1E2w6trIIzl4sM9qiv17PFhAeooQfaYt39uMQvjCVHiiVYbSKlIB8I3_rHifM9XUTQ32dkSmAi26vRQ61YUP4W8s-2fd-J6cmnlP8Qf7jSEOQnrxesR6OdHuY0WRBS6ef4e-w1b-tt0_WOWHfJg43CY1Yh1C3FzHn7k0YwtrVRmug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca4b2dd818.mp4?token=fSS-MEZnlJBh7olT5VouV-qK6bA0K2zyiIAsK0ZES-MPl9_d3ZVfMFeSG5OWk5-VXQptnzZzIKEbjmlR5Joa416Np2XjtPm1TCaTb8OPzvhcw8wkl3YiADTvGA6hKAiadHfO536r28Sc037_DsnOHzUQQDcQlVog-3XBGtOPG1E2w6trIIzl4sM9qiv17PFhAeooQfaYt39uMQvjCVHiiVYbSKlIB8I3_rHifM9XUTQ32dkSmAi26vRQ61YUP4W8s-2fd-J6cmnlP8Qf7jSEOQnrxesR6OdHuY0WRBS6ef4e-w1b-tt0_WOWHfJg43CY1Yh1C3FzHn7k0YwtrVRmug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
هیچ‌کس نمیدونه که کلمه «dumb» حرف «B» نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69601" target="_blank">📅 01:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69600">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇷🇺
🚀
ویدئو منتشرشده از شلیک گسترده موشک‌های اسکندر به کی‌یف و حومه آن در روز گذشته.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69600" target="_blank">📅 00:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69599">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hToQmLSvpXRSkMCcdq1h9c3UVBFe6MXBIjUk9AxSCJDSJs2h-dNFwFG_v8k8XIcesZtFNMiJ9nxqbyZjfnybe9yIdN0EsR9Npb30LQBZ9_cQLjPFkQZqZH7Ei27L4zhWcyzS2DTLdTBnaLUGVStTe3cPbvgDBRmIlBdY4k2AEoUpvgZiTa1DIoaRw-kdNoKzM5HV051DJEYQjoA7BqRHYhSbRBihxmI0tdY4wrETbJyZ7K7Nw50yjL4YS60trTtAkH0lGVk6nOFtBOa4iScpOoBJhQf17W7KfnOZKnpSCzLUdb2sLmHLzD1pXOcNQ5z25r8r5hwnC90B6SO5pKNmsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ مود:
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69599" target="_blank">📅 00:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69598">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82acfe6016.mp4?token=QQZRwi05qrx-vPdAzDN4g9LwjzLfVkitEzy3vmMh2YfM3LXtaCybfrneXiwdAST6flFW993uIV6TySOmcAY12zQor-BSbBRwsu0Za4nRrzwk05U75Ef7ztkEqF9qCliBKQTtMC1EPUVP2kYWJlcFVPD_6ekl_xQUbcHLN18ANVUSqh8ngr63xDZ6HKQo0kH4oza8eqyMCNuU7f9dQnrxkAQENNCDenZQoeg8UvT9KWSdYzbcAvvV9KwLSmEnCRWARzJeHfbACijF9C13xRJXHQ3DDOzxRTtRhkboCYKP3_Xo3kipwVRAV_wVXQwoeBKuzmvIYo83GpoNR4YA3wJj1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82acfe6016.mp4?token=QQZRwi05qrx-vPdAzDN4g9LwjzLfVkitEzy3vmMh2YfM3LXtaCybfrneXiwdAST6flFW993uIV6TySOmcAY12zQor-BSbBRwsu0Za4nRrzwk05U75Ef7ztkEqF9qCliBKQTtMC1EPUVP2kYWJlcFVPD_6ekl_xQUbcHLN18ANVUSqh8ngr63xDZ6HKQo0kH4oza8eqyMCNuU7f9dQnrxkAQENNCDenZQoeg8UvT9KWSdYzbcAvvV9KwLSmEnCRWARzJeHfbACijF9C13xRJXHQ3DDOzxRTtRhkboCYKP3_Xo3kipwVRAV_wVXQwoeBKuzmvIYo83GpoNR4YA3wJj1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فیلم وایرال شده از یه کارگاه آموزش فن بیان توی تهران.
چه خبرا؟ به لطف شما:))
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69598" target="_blank">📅 23:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69597">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51c05821a8.mp4?token=MQs0ZAQlnvifDscfIY17RjnVti_nMh1mfM_GK7PobmD_esDCpFtL7N_vw4Ex1fjKmFQN2HOg-gkPj_5uspSmhd6TGRd19joYzRJJXyqIC2Xg5U21QRAX90jmohSaGh52zlvaiLBHhVLq-mJjwzvlLQGnfHYQ2zjeS4qH6ais1RioBoAc9hNYpOT953sMvcGMqeNww3DIC1BBxjjiZdbtlrH34mPP2aTNgdwUCgFEfJospv_kxU5HJiVkcazeDlSnb47dGmUYtXmrCumDmBEj0BZB35XQ61wvVqCvQvVOnKMZ9vjlXiP2dSKP_BbCKMdL13h4fHX4H0k-dUKYAkCwLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51c05821a8.mp4?token=MQs0ZAQlnvifDscfIY17RjnVti_nMh1mfM_GK7PobmD_esDCpFtL7N_vw4Ex1fjKmFQN2HOg-gkPj_5uspSmhd6TGRd19joYzRJJXyqIC2Xg5U21QRAX90jmohSaGh52zlvaiLBHhVLq-mJjwzvlLQGnfHYQ2zjeS4qH6ais1RioBoAc9hNYpOT953sMvcGMqeNww3DIC1BBxjjiZdbtlrH34mPP2aTNgdwUCgFEfJospv_kxU5HJiVkcazeDlSnb47dGmUYtXmrCumDmBEj0BZB35XQ61wvVqCvQvVOnKMZ9vjlXiP2dSKP_BbCKMdL13h4fHX4H0k-dUKYAkCwLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
دیروز یه خبرنگار از بقایی، سخنگوی وزارت خارجه پرسید چرا جواب صحبتای ترامپ رو نمیدید؟
بقایی گفت چون باید رفتار ایرانی داشته باشیم و حرکات زشت دیگران رو الگوبرداری نکنیم. آخرشم یه تیکه از یکی از حکایت‌های عبید زاکانی رو گفت : "فعل و عمل ما را و دعوی ایشان را"
🔴
حکایت کامل عبید زاکانی:
شخصی اَمردی به خانه برد و درهمی به دستش نهاد و گفت: بخواب تا بر نهم. اَمرد گفت: من شنیده‌ام که تو اَمردان را می‌آوری تا بر تو نهند. گفت: آری، عمل با من است و دعوی با ایشان. تو نیز بخواب و برو آنچه می‌خواهی بگوی.
🔴
حالا معنی حکایت:
یه مرَده یه جوون بی‌ریش رو پیدا کرد، یه سکه بهش داد و گفت دراز بکش تا باهات همبستر بشم [ کونت بذارم ].
جوون گفت: من شنیده بودم تو جوون‌ها رو به خونه میاری تا اونا باهات همبستر بشن [ اونا کونت بذارن ] نه تو.
مرد جواب داد: «درسته؛ عمل کردن از طرف منه، اما حرف و ادعا با دیگران. تو هم فعلا دراز بکش، بعدش هرچی خواستی برو درباره من بگو
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69597" target="_blank">📅 23:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69596">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
ترامپ بهترین دوست ماست، اما می‌خواهم یک موضوع رو روشن کنم: "موجودیت اسرائیل قابل مذاکره نیست.با توافق و مذاکره یا بدون آن، هر کاری لازم باشد برای تضمین آینده‌مان انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69596" target="_blank">📅 23:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69595">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Esgard-VPN.apk</div>
  <div class="tg-doc-extra">42.4 MB</div>
</div>
<a href="https://t.me/news_hut/69595" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پیشنهاد_ویژه
فیلترشکن محبوب اسگارد ‌وی‌پی‌ان
تقریبا با همه‌ی اینترنت‌ها کیفیت اتصال و سرعت خوبی داره. حتما امتحانش کنید
لینک گوگل پلی:
https://play.google.com/store/apps/details?id=com.vpn.esgard&referrer=628035</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69595" target="_blank">📅 23:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69592">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ezILjjJjI7Z4JtoENyHlV93j__KN9atCm9ulJIYPtY1pZ6iR7jtJISPJEZLiGYm_8R8qW3r-o1xDX9E21TXZHkp1260QW-Eoe53VqgnCd3D4zh9sqKoOL93jjv4Sz76kzqQS9ttO8cZD6g5bQmfm1txk_h7sJtfQCsU0Bjh3ybhOXjLQSIPBEu1ziYj1E8N6XNSwfuJZEJ1JFS6QIj9CBBL9Ggoa99jwd-HoFV6l1dgvrZWs_wuND-DGpsPVBqC2xEB4J8WdGAYjXrS1sA-f1gFY3Tc_plA8iaNSdUP4TLJY-Uebt8e-NP1cBE5SfFnHoWPbLZqmKP2w19_6p4Sv0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cvridhx3ZcYY4yoIMQ3fL8dADiQbKfbinSq9AnB6qEzrTMhF_uO8dkAD-lycwBYbBA4cl1ZqZg8Vg624rU-tGBrmVZ3R5OeC_Y0WgJeaWvbneku03JoF7wTBmSqdMRBlAWm9OeZZIOk4v5BpEE2dFWn5rvV93mo4M-oNIsRrt_RTAyz4PTA14XWP1CPDGxDxKS0tDpzIgr2v4V1Jh10AByO9l9p3P0_hhtB-CfPLJBdYnEi4tgcaBEqyuRTexDG_cf8zOwFSDGcbJyT6rz8vtimcIHcVcDyZBPcSWZjQTxduwMBqhyXaucgdjOElgJgl8PYPjAAAT2zcmuTaTSP-Lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6780226a9d.mp4?token=FlcTAY_cRWajPS_FfYZPLLHm02E3v2aXylobG1vOr4cit__75uc3p94cFcrcOGgKZfNNQO-Ra0HQbcwHl-2UOBI5fDemmkQg-4PzArl931N_obYTKEzb5jsN4VUv7IlVEOX-UXjUNDb1kE7mrI2jgcFnA52tODEeW2wCOvHPiI3s5JDiZBdHmt6IyxBy6x0YtHwf1LI8PztFN3DYupC9kKG_MViC5ONJIbtspYcm3fM1QKu9KAovQG0mQOamx7zLAWxFw69Es-cl249P8rtD8AXMDFmulPOmm9FJ1lnHnBvbc9y6s-Y7hnqtRHsrim4-njwK_VK4u0YAcg5kAQw_tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6780226a9d.mp4?token=FlcTAY_cRWajPS_FfYZPLLHm02E3v2aXylobG1vOr4cit__75uc3p94cFcrcOGgKZfNNQO-Ra0HQbcwHl-2UOBI5fDemmkQg-4PzArl931N_obYTKEzb5jsN4VUv7IlVEOX-UXjUNDb1kE7mrI2jgcFnA52tODEeW2wCOvHPiI3s5JDiZBdHmt6IyxBy6x0YtHwf1LI8PztFN3DYupC9kKG_MViC5ONJIbtspYcm3fM1QKu9KAovQG0mQOamx7zLAWxFw69Es-cl249P8rtD8AXMDFmulPOmm9FJ1lnHnBvbc9y6s-Y7hnqtRHsrim4-njwK_VK4u0YAcg5kAQw_tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو لیگ دسته سوم تایلند، بارون میباریده، ولی همینطور فوتبال بازی می‌کنن
یهو یه صاعقه میزنه و صاف میخوره به یه بازیکن و اون بازیکن فوت می‌کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69592" target="_blank">📅 22:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69591">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiZ4FFAdjp1fMtApvkIFazQ1tP4yeZn90d4efwVskL3fhzyXXK2bum0OMYBs09hulSxTzlE9dvoJL1bIsuk-2FtvuTfG3h2TAxI468J4PrGDvNTURiJiLxJPrXLsm1Z-Fw_0py2lMb74KIQDrt4ijcvJSKHIOm_fgU_hWjVeOXhmvKe8466P-cOkSfNCne7cpVFzRh-PniM1u7vq_vcjZ2e43JgBjoOQa7wR9v8ijp7APoHWItxJtrnZN0r_zb51IDEMMFqxS5_o3A8qnJhhGewMsjeuGsYtRh1hOM07SevUutok2HAUCNDUVdif2zR4bGGMWmCyShIeP6jV2Xltkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
🇮🇶
وزارت خزانه‌داری ایالات متحده تحریم‌های اعمال شده بر شرکت هواپیمایی فلای بغداد و چندین فروند از هواپیماهای آن را که در سال ۲۰۲۴ به دلیل ارتباط ادعایی با نیروی قدس سپاه پاسداران در فهرست تحریم‌ها قرار گرفته بودند، لغو کرد.
این لغو تحریم‌ها، شرکت هواپیمایی فلای بغداد (که با نام عراق اکسپرس نیز فهرست شده است) و دو هواپیمای بوئینگ ۷۳۷ (YI-BAF و YI-BAN) را از فهرست ویژه اتباع تعیین‌شده توسط OFAC حذف می‌کند و به تحریم‌های مرتبط با تروریسم آنها پایان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69591" target="_blank">📅 21:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69590">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUh6kaEpr_zIOcIqmLhdPRBs5A_WxwJSbAI9rBTZsqutnErtgsYGCBhneWYhyUUx6kZPUubrXv8HYLFwPKWvoRYiU9f-BL-zNjHZXeg039jyfS1qd9v3VY-LCRapElUMuEd1lie7zeFTWI6fF7nKXNDPYV680rhPIfr1cwEmRuY3yI5-Hv-PO7izKsYr383YdJ1f4aX2c3Y_NRBCoYhEi2svVJAjVp1HDyg544YdldRJ1TEcFLnrxTzFR70BCfIF3mR8m9BeOKWEWeaBnOA0AGIG3DxXy7FcvlOx9lEzWETEZUd7xxpooK0tbGqezecgG3VWsorEIThflb71ItBraQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی:
ایالات متحده تقریباً ۴ یا ۵ روز پس از آغاز دور جدید درگیری‌ها، پیامی مبنی بر درخواست مذاکره و حل‌وفصل مسائل ارسال کرد.
هرگونه توافق در خصوص تنگه هرمز باید صرفاً میان ایران و عمان باشد.
ما هیچ‌گونه دخالت خارجی در تنگه هرمز را نخواهیم پذیرفت.
با اجرایی شدن توافق جدید، مسیرهای موقت فعلی در تنگه هرمز بسته خواهند شد.
بخش قابل‌توجهی از مسیرهای تردد کشتی‌های ورودی و خروجی به آب‌های سرزمینی ایران از این مسیر عبور خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69590" target="_blank">📅 21:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69589">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca751f3e8.mp4?token=IEoaFhuoTL4glVWLHInCzwF4hBFwYA4p_cWXT8S9pdcD2TWXzKAXzuxGGmgIQcEz1kTp9OGzoV5vrJ0fOAtQBSsOGNShrDPzUcIHkbJhTGbimmsznKLSlBCXc7D1GK-LsU-_dEjYub3deLMnQV-KfWVytGQTxDbYtcqPZT7l8tcqsifAagsaos2fRdxI4gkeXCokc5CgQd3K7tHb5u6m09nxew6xY-3k1DjrWtg3FF0imi40bjWM0aXw2oNpMfMJiPPOybe2owHD0_qeSU-gSWb9_FGyxOIVVad6sKv7twnkZcP4Xy_NxDKO7P_Kg7GarZXGrC8o7vOd991mev9f0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca751f3e8.mp4?token=IEoaFhuoTL4glVWLHInCzwF4hBFwYA4p_cWXT8S9pdcD2TWXzKAXzuxGGmgIQcEz1kTp9OGzoV5vrJ0fOAtQBSsOGNShrDPzUcIHkbJhTGbimmsznKLSlBCXc7D1GK-LsU-_dEjYub3deLMnQV-KfWVytGQTxDbYtcqPZT7l8tcqsifAagsaos2fRdxI4gkeXCokc5CgQd3K7tHb5u6m09nxew6xY-3k1DjrWtg3FF0imi40bjWM0aXw2oNpMfMJiPPOybe2owHD0_qeSU-gSWb9_FGyxOIVVad6sKv7twnkZcP4Xy_NxDKO7P_Kg7GarZXGrC8o7vOd991mev9f0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
❌
🇮🇱
امروز در پی وقوع انفجار در ساختمانی تله‌گذاری‌شده در «مجدل زون» واقع در جنوب لبنان، دو سرباز اسرائیلی کشته و هفت تن دیگر زخمی شدند.
حالا قراراست بنیامین نتانیاهو، نخست‌وزیر اسرائیل، و یسرائیل کاتس، وزیر دفاع، ساعت ۲۱:۰۰ به وقت محلی نشستی امنیتی برگزار کنند. محور این جلسه، حادثه مرگبار امروز در جنوب لبنان است که منجر به تلفات متعدد در میان نیروهای اسرائیلی شده است.
به گزارش شبکه ۱۴، انتظار می‌رود مقامات سیاسی در این نشست درباره انجام یک واکنش نظامی قابل‌توجه گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69589" target="_blank">📅 20:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69588">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12fe6dbab2.mp4?token=ZAaeXpxz60vGRalSsCHIy0s-IOwhgcDnX-2PIBBDaIwSl8VgtQfIGYx64OATKB5_JDizJcoXhN2N02WFMa7Egi5Ah57wktDlkb3AIECHlvjXiFK-KyLJ1qZiDszFRkTpz9B3a8fQWJLa4g_q-11Q-6cR_n6_UBI1Ih7gs1SJIY9POC3UC_Ad54n-BgIuzMo1lrbQIVNUT1sFdG8D_B4i2G9qRZ-bmBYbK03fHJjgvf7pBvqM_wo8i_awAd6vqvEylsDMDj9fAd1O_rJlUCIQWNcmANt7xXGNoaEc8bOQgZOUYyKa15klI90erX9JDsrQQhoVzNpYZzDgTk_9oNtlTY_LfLkCmmnfLcVJWkKzqZRIZfp--fKgd7K-wRmCpEziAvrO_o9BdvK5NhMq4SNBInz5BOf5kkiHtl8rXTVgcMqmK8smevfMk1RRtt6gkIm0SOzne0rRk28OPpedJjdOd-Ke6sy5J-tRcii5stZy-cO5LinUTYMLf_Kq8ed-JXuEa_eKZ4Fd2JGcwYoGox3AgK3miEWXolkyDjP3juQEsyaeljhwb5F5rv4uiviyXpxIJscrKmOxmh-DSaliMbhxYb8UKFx5_nUWgEURgOCcKwAmo9UUOxHqkINpUeooW4u4aOYHhkz5zruXAaLqDMtgGc8TyktPPKddASw06r5xQgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12fe6dbab2.mp4?token=ZAaeXpxz60vGRalSsCHIy0s-IOwhgcDnX-2PIBBDaIwSl8VgtQfIGYx64OATKB5_JDizJcoXhN2N02WFMa7Egi5Ah57wktDlkb3AIECHlvjXiFK-KyLJ1qZiDszFRkTpz9B3a8fQWJLa4g_q-11Q-6cR_n6_UBI1Ih7gs1SJIY9POC3UC_Ad54n-BgIuzMo1lrbQIVNUT1sFdG8D_B4i2G9qRZ-bmBYbK03fHJjgvf7pBvqM_wo8i_awAd6vqvEylsDMDj9fAd1O_rJlUCIQWNcmANt7xXGNoaEc8bOQgZOUYyKa15klI90erX9JDsrQQhoVzNpYZzDgTk_9oNtlTY_LfLkCmmnfLcVJWkKzqZRIZfp--fKgd7K-wRmCpEziAvrO_o9BdvK5NhMq4SNBInz5BOf5kkiHtl8rXTVgcMqmK8smevfMk1RRtt6gkIm0SOzne0rRk28OPpedJjdOd-Ke6sy5J-tRcii5stZy-cO5LinUTYMLf_Kq8ed-JXuEa_eKZ4Fd2JGcwYoGox3AgK3miEWXolkyDjP3juQEsyaeljhwb5F5rv4uiviyXpxIJscrKmOxmh-DSaliMbhxYb8UKFx5_nUWgEURgOCcKwAmo9UUOxHqkINpUeooW4u4aOYHhkz5zruXAaLqDMtgGc8TyktPPKddASw06r5xQgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فاصله ایران تا آمریکا با موشک فقط چند دقیقه‌ست، اما پیاده باید نزدیک ۱۹٬۳۰۰ کیلومتر راه بری!
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69588" target="_blank">📅 20:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69587">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0660a7fbd.mp4?token=eVqGj8AHB3Bmzv_ieTbaSB_5-OXsIE0eXRk_zjii2hgqFKvpjwHUK-RCkkkhopxwQrZE1igOfpX4AHBH7WQSobBVIT-jv1sxmJhz_vdhVM6DLJgwz6wMN_ZsYzIaxp_JFCR-fCMTPfL1El9yXWIi1lM2E0Y5obz3LGZOhgbZydYfbVF1uYdukBPvW8EkS9jpl6vf1PCPDdlBagBqporfz-zKicqsDPDtoFMM-JYcLAlYMSBdBoymSoi_3qefr5Jh1M3VO04p3e3DrOJSlK1h0Q0TQ4EC7bSDYREpZLwxJRofbziWnj-ageby9VC4VIjfDE_AU87HgErBt-eN02el0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0660a7fbd.mp4?token=eVqGj8AHB3Bmzv_ieTbaSB_5-OXsIE0eXRk_zjii2hgqFKvpjwHUK-RCkkkhopxwQrZE1igOfpX4AHBH7WQSobBVIT-jv1sxmJhz_vdhVM6DLJgwz6wMN_ZsYzIaxp_JFCR-fCMTPfL1El9yXWIi1lM2E0Y5obz3LGZOhgbZydYfbVF1uYdukBPvW8EkS9jpl6vf1PCPDdlBagBqporfz-zKicqsDPDtoFMM-JYcLAlYMSBdBoymSoi_3qefr5Jh1M3VO04p3e3DrOJSlK1h0Q0TQ4EC7bSDYREpZLwxJRofbziWnj-ageby9VC4VIjfDE_AU87HgErBt-eN02el0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
ترامپ بزرگ ترین دوست ما هستش اما به صراحت میگم وجود اسرائیل قابل مذاکره نیست.
با توافق یا بی توافق هرکاری که برا آینده مون نیاز باشه رو انجام میدیم.
نیاز های الزامی سیاسی مجبورم میکنه این مراسم رو ترک بکنم.
در حال حاضر توی یه رویداد بسیار مهم نظامی سیاسی هستیم.
این جنگ موجودیتی هستش.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69587" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69583">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19fc284b17.mp4?token=b84r6RRLlPi2x6WgfITwKmu5EjCX7YiCQwpcVcJRJnI97G-BFipdFKoDcvDO2U0fMMDC_t3tLdsNmNR1Pc79L1w5yzUnpt7bcKRdEQwPn48hpkU1VkVgtEuEEBgoyvlcKAVV1uCZmyqeCzmYB8uD_2XsGqVMsaBAEokBZhH6VnIJolxKhMsjlqBGcais0uYJxJDGfpFeXzm5FbZIWSK9HNyQt7QTNW29P9xGluZpcVIcEzYYV0i5Hxl6lunKe79qnwYWooHjxUntDj1Y79wawC5njAgGj1Gu31qE1RociLP8F9vHRZdHrcYdj2JYJMC0xFeegkR-bszjtqdeHzWJPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19fc284b17.mp4?token=b84r6RRLlPi2x6WgfITwKmu5EjCX7YiCQwpcVcJRJnI97G-BFipdFKoDcvDO2U0fMMDC_t3tLdsNmNR1Pc79L1w5yzUnpt7bcKRdEQwPn48hpkU1VkVgtEuEEBgoyvlcKAVV1uCZmyqeCzmYB8uD_2XsGqVMsaBAEokBZhH6VnIJolxKhMsjlqBGcais0uYJxJDGfpFeXzm5FbZIWSK9HNyQt7QTNW29P9xGluZpcVIcEzYYV0i5Hxl6lunKe79qnwYWooHjxUntDj1Y79wawC5njAgGj1Gu31qE1RociLP8F9vHRZdHrcYdj2JYJMC0xFeegkR-bszjtqdeHzWJPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
پلیسِ رشت یه ون آورده وسط خیابون و شروع کرده داره به دخترها اخطار میده؛
بعد واسه مشروعیت دادن، یه مصاحبه از این خانم رشتی رو منتشر کرده که‌ با میگه:
گشت ارشاد رو دیدم احساس امنیت کردم.
امیدوارم این کار ادامه‌دار باشه چون اصلا از وضعیت سطح شهر راضی نیستیم.
چهره شهر اصلا عوض و زشت شده.
الان همه فکر میکنن رشت این شکلیه ولی خوب‌هاش رو نمی‌بینن.
گشت‌ارشاد دغدغه اکثر مادرهاست نه فقط چادری‌ها!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69583" target="_blank">📅 19:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69582">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
منابع عربی از حمله موشکی سپاه به بحرین خبر میدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69582" target="_blank">📅 19:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69581">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d659457195.mp4?token=vDdqhiY3U88m7mJQ0ZFThDP9hVMYg31LZy0m0vbyvvP6xtr9MxbaEndE1EqM99WDEGjYv8xd_trK90FEc0F5rOS1MYwe9f_I8RshO99L3AvWvTnQax9vAbJBUyuzoDUepHVAvWoRS5KZ0tu25KBs-EajVM3lqbgQHZ6V8AxCQYTWMTKNfQwgRSgAz0F9WiwXKCc5MvOzwCVQMuMrg4gWs3j6u2l-oe5Xu3skojl4-IsRVo4FEcCpv185MAxC5KIqjwVcE_v_hTBKqb9OV_cmild6_Nyr0C3SAUwUE6DnJRUkGEfEENCjPAJCpYRGX68lqBikoVRS0hWJqaKoeTGalQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d659457195.mp4?token=vDdqhiY3U88m7mJQ0ZFThDP9hVMYg31LZy0m0vbyvvP6xtr9MxbaEndE1EqM99WDEGjYv8xd_trK90FEc0F5rOS1MYwe9f_I8RshO99L3AvWvTnQax9vAbJBUyuzoDUepHVAvWoRS5KZ0tu25KBs-EajVM3lqbgQHZ6V8AxCQYTWMTKNfQwgRSgAz0F9WiwXKCc5MvOzwCVQMuMrg4gWs3j6u2l-oe5Xu3skojl4-IsRVo4FEcCpv185MAxC5KIqjwVcE_v_hTBKqb9OV_cmild6_Nyr0C3SAUwUE6DnJRUkGEfEENCjPAJCpYRGX68lqBikoVRS0hWJqaKoeTGalQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مصاحبه تاریخی فیلدمارشال رضایی و خنده مجری:
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69581" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69580">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtCJCfDovWZAMJKKYuzclUeY0PjogTfCaRx8D-r5lDwaN9LxzkfyAusCCzraQJBOM2NcbgC8S_D79DcA1Zoc621Nt_WfICIVJWi9UBCo4hBc292pOL1LuLCZkkqVfePS7fXsokfSgXoXlRth8vXI8MUHbGKO_3JRXnGVsKtrTZUsxx10LDBhkqmK9mPFQWeQWdzUvCyBnxiiZfn5YBM41ve13R37AdA8UgeBcHLzM8K2E4gehtTmrtFTy919VlftERZhnpTajbSy88UkwLKJNuRL68wX6ZxXps8CwWHD-7OurP9x_M2uSHFCyKeJCYJmQhrjCHSfU4167T88sT52MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پهپاد مافوق‌صوت Quarterhorse آمریکا به مرحله آزمایش نظامی نزدیک می‌شود
واحد نوآوری دفاعی آمریکا (DIU) برنامه توسعه پهپاد Quarterhorse شرکت Hermeus را برای ورود به کاربردهای نظامی دنبال می‌کند. این هواگرد بدون سرنشین با هدف آزمایش فناوری‌های پرواز مافوق‌صوت، سرعت بالا و قابلیت استفاده مجدد طراحی شده است.
مشخصات اولیه Quarterhorse:
⬇️
نوع: پهپاد آزمایشی مافوق‌صوت
⬇️
سازنده: Hermeus
⬇️
طول: حدود ۱۲ متر
⬇️
پیشرانه: موتور جت توربینی با فناوری توسعه‌یافته برای سرعت‌های بالا
⬇️
سرعت نهایی Quarterhorse: تا محدوده مافوق‌صوت بالا (هدف نهایی برنامه Hermeus رسیدن به سرعت‌های نزدیک ۵ماخ است)
⬇️
قابلیت‌ها: پرواز خودکار، استفاده مجدد، آزمایش فناوری‌های پرسرعت
⬇️
کاربردهای احتمالی: شناسایی دوربرد، آزمایش سامانه‌های آینده و مأموریت‌های نفوذ در محیط‌های دارای پدافند پیشرفته
پهپاد Quarterhorse هنوز یک پهپاد رزمی عملیاتی نیست، اما آمریکا آن را به‌عنوان یک سکوی آزمایشی برای توسعه نسل آینده هواگردهای بدون سرنشین سریع و کم‌هزینه دنبال می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69580" target="_blank">📅 18:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69579">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3689824738.mp4?token=gi18u425i3JUpUbs44R1Kidi6KvCHj1dBuFbokGfuFx7rcly8_mzu1BRUlLPfkaYzWXgpBVUq614oud7Ldl0_7mKGu8U0pdENk_bCHgFoH6xbSt3B9TNZNeQe3K7RwoG_bep3pAmNF6RcIXrc4rOkU4Q-pWzV_n0rAQsRbO4WHQxYyFp1_Uf3yBwBxZeork2Ckc8wPKkwS1QKoP5-IgjisoKESfyG4qUKJ804Z7mZnfrN1eqREb1y_hTX3h_ydwOkDcPmSAFatJfix-YNODaPr7tye6SYrW-cxBgMyrD3AJW3j0L8GblFv9GA8yg0YgaojxwCo6FaMJBLYrhmVNv8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3689824738.mp4?token=gi18u425i3JUpUbs44R1Kidi6KvCHj1dBuFbokGfuFx7rcly8_mzu1BRUlLPfkaYzWXgpBVUq614oud7Ldl0_7mKGu8U0pdENk_bCHgFoH6xbSt3B9TNZNeQe3K7RwoG_bep3pAmNF6RcIXrc4rOkU4Q-pWzV_n0rAQsRbO4WHQxYyFp1_Uf3yBwBxZeork2Ckc8wPKkwS1QKoP5-IgjisoKESfyG4qUKJ804Z7mZnfrN1eqREb1y_hTX3h_ydwOkDcPmSAFatJfix-YNODaPr7tye6SYrW-cxBgMyrD3AJW3j0L8GblFv9GA8yg0YgaojxwCo6FaMJBLYrhmVNv8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
یه سرباز روسی توی دونتسک اوکراین لخت خوابیده بود و داشت افتاب میگرفت که يهو…
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69579" target="_blank">📅 17:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69578">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fdacb808d.mp4?token=b5ad45qwB-91H4suVt2ToLoPxy89cF7gxvtzm4-zxHLa2S2DjfvXiR4onc-Tic4cyUaDzhCXM6lKpWCvWqyn8ILULsJz17V08cxw7q8lFtewQJSjbwG1dLlWtr5I1Rh2IqeYXi6TofDLu8lVLK0Vb9tX_VyJaaKmDWpD-sfR1ZanceMUEf7njuzl2co80szrXF8t_qhZtJRUcQqLWKXmzqxJMVe_66I9XQfetQZWsR6dCjVt1rXkisKS1_2l_Rig5QIu5s8zs4X8pOySFw79EcujMe0Q0qbjMtL6xBdmYq5x8NegzDVsipWQYxvA1OZdGdzx0vaA6M6jiLC1E3ph7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fdacb808d.mp4?token=b5ad45qwB-91H4suVt2ToLoPxy89cF7gxvtzm4-zxHLa2S2DjfvXiR4onc-Tic4cyUaDzhCXM6lKpWCvWqyn8ILULsJz17V08cxw7q8lFtewQJSjbwG1dLlWtr5I1Rh2IqeYXi6TofDLu8lVLK0Vb9tX_VyJaaKmDWpD-sfR1ZanceMUEf7njuzl2co80szrXF8t_qhZtJRUcQqLWKXmzqxJMVe_66I9XQfetQZWsR6dCjVt1rXkisKS1_2l_Rig5QIu5s8zs4X8pOySFw79EcujMe0Q0qbjMtL6xBdmYq5x8NegzDVsipWQYxvA1OZdGdzx0vaA6M6jiLC1E3ph7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
توی مراسمات اربعین امسال آهوی ایرانی کباب کردن و به زائرین دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69578" target="_blank">📅 16:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69577">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbTUwY1GDxZj-vcDhd255pEpg-3q3sY4CCxFTQgUC2_L4UU9Ufh8bwpbHXc4-zCK0agLrMC_NkNpIZzzmj2av1q8C9Mo40YSWYFoXid_jO9S5EY3VRcp_e_zeymGBrUVptMrKxsXuRR7fU2brWMVylwmym6Cu6TnKs361AuRjXseuU0byCr7iG-zLJ9czrfFjNGPTAYOZTTF45Psl3R4Ha2g4m9vbX9rQtoOnfDrBAqObd5VqepSTQcIuTNHzy_fLzq-dW1PXrU9LA6u0wdSzu5L3ACqhX_e1BznjhgJ_W_tt8kryJOjWkV2S0V-NG-G5rpF07qX3DBQy8deDd8_oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
#فوری
؛ ارتش اسرائیل برای شهرک المنصوری در جنوب لبنان هشدار تخلیه صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69577" target="_blank">📅 16:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69576">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66218d020e.mp4?token=r9sJNIrWql_yps66H02DGLFBmjUuZTxTUny3n6rgCTu3i5zz335EvURM6mGeOoyJnb-j1KxAngl1H0fX5J9MUF-GxkZdYupxVOmtDfF8WtbQBHAmmRJVH6Yaw7o36-3of8Zw0XFK5Q4svEXVcIfaQcwFV4ZW1Jd4Ci1sNN8uvH32RySOWoaDaVFUyQqKISd9zD8R5t1mZZvs-qEZhzEjvyBABVJROBBWqsk0pklD2IaRXu8efJQJUTa-OMlTzilS3Sjdb2YLyhVnK15nBXcKZZkysGVQNmxmZZam8J9vRMeHOUzgXIjcsGH_2S1CTRX7RDZjCGCRTpAjUuuQBboDlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66218d020e.mp4?token=r9sJNIrWql_yps66H02DGLFBmjUuZTxTUny3n6rgCTu3i5zz335EvURM6mGeOoyJnb-j1KxAngl1H0fX5J9MUF-GxkZdYupxVOmtDfF8WtbQBHAmmRJVH6Yaw7o36-3of8Zw0XFK5Q4svEXVcIfaQcwFV4ZW1Jd4Ci1sNN8uvH32RySOWoaDaVFUyQqKISd9zD8R5t1mZZvs-qEZhzEjvyBABVJROBBWqsk0pklD2IaRXu8efJQJUTa-OMlTzilS3Sjdb2YLyhVnK15nBXcKZZkysGVQNmxmZZam8J9vRMeHOUzgXIjcsGH_2S1CTRX7RDZjCGCRTpAjUuuQBboDlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
وزارت دفاع روسیه تصاویری از حملات پهپادهای جت‌سوار گران-۴ به سه کشتی باربری در دریای سیاه غربی منتشر کرد.
وزارت دفاع روسیه ادعا می‌کند که این کشتی‌ها تجهیزات مقصد ارتش اوکراین را حمل می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69576" target="_blank">📅 16:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69575">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/474cba356d.mp4?token=fB8PmxzqUXktaLdEfH_Hwj9O0MYLwKZBiO4UtRptXkvvmSQxu21kG5JpRYiGcJDWSbHowa4Cls213K5QQJVDzvGmMW0CCPLB4WlxtSNJsiHCDgC5RRbWkSByzL9-FOnXIPZY8O7MvmKXh5Fw99R2sW5h6i0T1YOlwvJlJQkMS7fThUQnbl4SS1861qkWc0m_KHy5ddITw9FK0sCecrMldaCVFBqx-8AqE4uyoMC6kIs2vGdTYod6m7nA8ODWtXK9UPdUgCeHey739f3nZ-fYLXXZTp8BHLW8z60yhuKy8sNo7Gu1HdVmXaZk23nwyI7y3mRTFY011ZkYiVN4FTuZ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/474cba356d.mp4?token=fB8PmxzqUXktaLdEfH_Hwj9O0MYLwKZBiO4UtRptXkvvmSQxu21kG5JpRYiGcJDWSbHowa4Cls213K5QQJVDzvGmMW0CCPLB4WlxtSNJsiHCDgC5RRbWkSByzL9-FOnXIPZY8O7MvmKXh5Fw99R2sW5h6i0T1YOlwvJlJQkMS7fThUQnbl4SS1861qkWc0m_KHy5ddITw9FK0sCecrMldaCVFBqx-8AqE4uyoMC6kIs2vGdTYod6m7nA8ODWtXK9UPdUgCeHey739f3nZ-fYLXXZTp8BHLW8z60yhuKy8sNo7Gu1HdVmXaZk23nwyI7y3mRTFY011ZkYiVN4FTuZ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی صداوسیما خبر کشته شدن ترامپ رو تمرین کردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69575" target="_blank">📅 16:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69574">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M25DhNtCxVwGbTuYmByWlFEMRJY6Vk-yiuNbu1KST-wNPJcEBereKjOhReUZkIhC8vM7EPa0xsi4FmurC8lG6WKZOBhz8h0JB4TanlGWkdIqcjvblDKkvX1ZCV6MEW3VIYqEc4pKYxJwvocOntF9lJxjssjBIepyWNIXBFAjKnyeygmoRqqdyXMvHAzsJcP6bOxMElx72ljZsiCaO3hPm2jlWRs__NyqA2MkGm-PpWwakhN0NtJhgGZh0mxXWtMYLL_obRJBJYpDcdkcFjL7RETJHoFchd8qqIZ_7ByzpRsrPuGAoLf8Cf8EegfmOQ4_H_XzWw-TtTsUPDpK1BeJHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💢
📉
قیمت نفت با کاهش های پی در پی به ۷۶ دلار رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69574" target="_blank">📅 15:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69571">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IwXxc0b1B9O6N4SrB5mrs3ekUqzqJmL8i0hhDsntj1LcVb0DYfI_bPn4Gjx2fk4N6WJkK77pa_Hdo1YYMRem-TqA8Kyoe7ISbaJnNfW8zDpmDCo5eL_Xd5IOD50_Bhhf7wT4tMH7EKvaZ56G-osqYMHk8tjkoNI7xVx6_cOaLFJDIU4YAn7mJxQkDbe0vc_WfNEHrlGrLwK6RjSI9TpUilCGDHezV6luQRPPc299UdmufVzn4yOI_Og99Fw6JBPvVBrTdR6Q2s0FrXoSFtZ74aid_EAmXK8EmJa26jjWkIt6itBANW1ER2SWKl1iF2ywlaoCiamFaQqfGRfDNfolxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kAPYGMtcD3fbCry0Lt8C1Oz7ZRUyo30XZXgX2gfYmghrEvc4P7VafhJkKsQF72BLNRThHIXm5i4hpclY2txC0mypg_lNbw1g6II93BnNIxjdvTaAFyxdvjtgT4BY48XWM-qz0NM7xgaYrLse3v337OnW_4PHSGdi5vK36PZux6-uYic5W-8W4xZwb9q-ZdMrGCRZ9Diu1stO-DLe6KXZ2C0NN8wjggaVZC_p5BbpRdb0zEkrJfjjzVOUQHrfBhoaDkl1jGnpGtyfzkzM-ftwUXX9DO3waxMjXGkGfDcfR0ZjXK---zYkaMh2UKf5MlrNZFdlHZ0E3Gp6EVqjzUcSrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MqVEgsWtqxKj1XgtmnT09qGewwpKnn7odq6Z2UKmacUq_ok1ab0GWgiTrFq8E5HwwmovxPGi2Dv1Ts3C_OCHs7SpLzM3iN193RF8eW8TpzHs-vWaxZLHFOifiL0G9xB66rPNsYlRtXkMunnYaizRq_DpFE3aYDJzUQKTIWxhiZeRdziPpdo75mOkzeC1Lx77kid13E-oJZdLtfklvngWGZKA30jDGYBCApCqXD8Vs-dcmC1ct0N0PAYXrZEQZzHzqCClezapmcVBlLjHcDvD0RMenuNkQW1OF3gUn3VzdYHLTlyiZhNLZ0fWJF7pPp5tyCDKlkt7Gj7IbMG1mQMveg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
پست جدید و لاتی کریس رونالدو؛
"
اسباب بازی‌هام
"
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69571" target="_blank">📅 14:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69570">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL8_UR3z7zDF538YARCrSG3yswoEwJEH6UPP6H9aX5OL5KSA4ed2b5TOZsW2d8IIwgQhpBLAx_GkIXdbqSzOnq2mUYwVhD2DdDk1PkdBKBVvG1sfczlgiTQ5b5vsEVJxz8EUI376EG3xaPbZjCRye8tTUItBgPfFogqJhnTjgr1R-3EhVk0mMVVfBo3kmYkIPJrkMl5v0bMueP4jkx4LWC-yClgH2Z8XGTtE406MAn3_Sb_czO_U9OiPggDluL7hkJ-BDrkKJjdvjT6UcjDp5Rwc61wrbxj_6kgBuOjf8XSkp-M_5aznR0Fsbzeh5STeNQFdGRV8BXYuzq15LIl2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
دسته‌ جدیدی از سوخت رسان ها برای مذاکره وارد اسرائیل شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69570" target="_blank">📅 14:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69569">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpCpKRSCX0C1zpuEZmYsFI0bVfwNbmqhPafVJOiXp47Zic53s-wO7KPTVpQVJQlE013wtlYEdPtHUNoAgKr6QboHTB5WxRKPlcoV2BS2G0sdx-dj8nRkRLftODUdOl5MofjP8A_yuiZSHrleVMg8TTa4Km4LoDYRhqcxjkZLT7Dca51D5jUXbj-HJocOeuy12WrMLwLwYDaehNsFGRfdN0a9YR0Q69tl29tQDsrOevvhxD3ElDC0nZ8WNV2azKBlD-x2zWYnI2Mcb7Npi_y0Yh1IeXw7Z0goGBi3DF72r7hf4RZ-ahmroMjc5yIG-dp31O3DoDgy8_jJYYWfn6maMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
❌
حمله هوایی ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69569" target="_blank">📅 13:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69568">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f4b05f8c.mp4?token=tLAbYmuIrU7fW2hVqAau-0w58xIQsOVgJzv-UPBdHzlk174riyrj_LtUB7mBT_tIXDc7lNLFnm56qCUvnKgkLtNAeGqHBJ6r5MgG6dWLSWP6iU2hNGqZDuHN4jTxY5gKV34XMw6KxruWheTyGQxRcySpWDtAV0Wc_9kPpFg_qykkxlIkOO0wMawpCVb-jj2Mn-OLp4LPyTwuh4-e8PHkLSEcnT9DN51hYitWjh0MowQ4AXFjL3BORioGBcYbGHze968_ySGJNjs-HWTp2BbK8c84xe9LfJ4fVTZloah0XuXbfrXbyLEX6woooZvYyqwWaOs-pm0ZwBmUG5Iv0LjOAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f4b05f8c.mp4?token=tLAbYmuIrU7fW2hVqAau-0w58xIQsOVgJzv-UPBdHzlk174riyrj_LtUB7mBT_tIXDc7lNLFnm56qCUvnKgkLtNAeGqHBJ6r5MgG6dWLSWP6iU2hNGqZDuHN4jTxY5gKV34XMw6KxruWheTyGQxRcySpWDtAV0Wc_9kPpFg_qykkxlIkOO0wMawpCVb-jj2Mn-OLp4LPyTwuh4-e8PHkLSEcnT9DN51hYitWjh0MowQ4AXFjL3BORioGBcYbGHze968_ySGJNjs-HWTp2BbK8c84xe9LfJ4fVTZloah0XuXbfrXbyLEX6woooZvYyqwWaOs-pm0ZwBmUG5Iv0LjOAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
دیروز طی یه مراسم تو روسیه، یه چترباز از هواپیما پرید پایین ولی چترش باز نشد و سقوط کرد و درجا مُرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69568" target="_blank">📅 13:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69567">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwlqrdnyARcqMF3YFLF3mLBNmZjelOL4_SgzJAGnN0xwWnOb3yplG7mOvEpXMsJpppRUY-y-TufZpeZdhpyepETlxKO2zWMZXa3TZVb6RlzfgMrHN7e2rezl5kGcy8H_KVJ_pI9rD3Y6kGyHT-Qxf2preLc1B8aCzELlu2FM7ar5mIEMw10zq33q7lPD2Fm9M8bswUsN1TnQtm8g9D9XP5q6gjOTnID2sbEkD_Vk9XcrMK1knNmdOyET9ynJo_TAKxkjT2eOlobaUqKiTYRzVvPEDJrQMxiRWyaqYetRD3P0FFGnT8Zl5VlETHleJ7a5ABc6LYEp0Oc-zk5b37-jJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
دونالد ترامپ تصویری با هوش مصنوعی از خود منتشر کرد که در آن با لباس نظامی در کنار ژنرال پتن و ژنرال مک‌آرتور دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69567" target="_blank">📅 13:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69566">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cc20a5985.mp4?token=f9dBhHNbbof4jSAyQqTuubUV8RWBdgva0qLWezDE_CPsSXc52yymubeRAgyy67fKxX7h9XnUHKeVMvJsJbvKdhsGLPe5Qykr6Izy34JVCnKIv8fhN17LgQUItz-kvlJ0UVHu_3gzKYueo0wQJah1tXRLgWfmnFodrtveck1j0S4TI4aFtghR22nEhAj3saFBywQtG26oxwmrJyQhEZcWFoADV-16Xu6IkMRfvv4fxVqr-JDHYymVBj_W1nevWZLfY90xXTm6ff6_ZJEIx1kCYc_GkHSwl5uwKBxW4_V6hMCZZOlcB_-ufNUuq-ckhcrBip0DxmRUVZAYucC352iu-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cc20a5985.mp4?token=f9dBhHNbbof4jSAyQqTuubUV8RWBdgva0qLWezDE_CPsSXc52yymubeRAgyy67fKxX7h9XnUHKeVMvJsJbvKdhsGLPe5Qykr6Izy34JVCnKIv8fhN17LgQUItz-kvlJ0UVHu_3gzKYueo0wQJah1tXRLgWfmnFodrtveck1j0S4TI4aFtghR22nEhAj3saFBywQtG26oxwmrJyQhEZcWFoADV-16Xu6IkMRfvv4fxVqr-JDHYymVBj_W1nevWZLfY90xXTm6ff6_ZJEIx1kCYc_GkHSwl5uwKBxW4_V6hMCZZOlcB_-ufNUuq-ckhcrBip0DxmRUVZAYucC352iu-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درباره ایران:
خب، اگر دوباره پا پس بکشند، ضربه بسیار سختی خواهند خورد. آن‌ها این را می‌دانند؛ آن‌ها این موضوع را درک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69566" target="_blank">📅 12:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69565">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336dcdad36.mp4?token=K2j_uC1jRlWeqbJpJjjjUu8JTBIVecD27bFqnmP41bIEcE92tq66VZMIGtagSSUZAUVdv1LIc1b3perbTGn32GUoyDB4JM_QvXLe8ZXiJv7LtVQcOuzr7VWyi4e5hj_CdUiNLt-J1qpjZOXTkJZKROYqv3pDniVCM0-2or0XSI_AbjegA4rCLeZfobXleMj4Z6iGM6-y2zWOQ7TOaVboiG-YIYK8aAU6aWB4VJLKvgb-YkrQvDTiXmmMIcKTFsYCv8kTuzTMkVt7OgGwZjF0-BxeS4a-18ppGCoyVm9BrGlax0Dy06IdZhBtiPt7C0ALvvRfhuUNEKy4h5tWbGMWRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336dcdad36.mp4?token=K2j_uC1jRlWeqbJpJjjjUu8JTBIVecD27bFqnmP41bIEcE92tq66VZMIGtagSSUZAUVdv1LIc1b3perbTGn32GUoyDB4JM_QvXLe8ZXiJv7LtVQcOuzr7VWyi4e5hj_CdUiNLt-J1qpjZOXTkJZKROYqv3pDniVCM0-2or0XSI_AbjegA4rCLeZfobXleMj4Z6iGM6-y2zWOQ7TOaVboiG-YIYK8aAU6aWB4VJLKvgb-YkrQvDTiXmmMIcKTFsYCv8kTuzTMkVt7OgGwZjF0-BxeS4a-18ppGCoyVm9BrGlax0Dy06IdZhBtiPt7C0ALvvRfhuUNEKy4h5tWbGMWRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فریادهای مجری کشمیری(هند)صداوسیما درباره تنگه هرمز:
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69565" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69562">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba5ea669d.mp4?token=jYjaYCQIvwYMdcsdj2Tcr8HdyGKD-bZ_BdLHsBQvlKBMsgRD8u0KBy2bgegWumbNAfNFPiKn8d9vzmqI24uh0RbnWQkm0XOjnb8dql_79DnGRPBxrmm7UoD56an8M2WDJfC0rFLquqcpwydUv3cKWq8cIUphn8sa3MDd_4VcDg_4CmZ1cORNz1krIj7gQpQ1ucW-TYiDBP1uTu7H2tyaLuZQnkFqnx522cQiwpbquGkCQs0CBjUuivwuedq6-awrHsUBs-VZAnYe6DIGPNidwNPs8MLU-5t5K9z3_hwn_iWtzjPgOlxXvXC3vNyiknPYRLtPmXQDDHtvpWM4SYWVSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba5ea669d.mp4?token=jYjaYCQIvwYMdcsdj2Tcr8HdyGKD-bZ_BdLHsBQvlKBMsgRD8u0KBy2bgegWumbNAfNFPiKn8d9vzmqI24uh0RbnWQkm0XOjnb8dql_79DnGRPBxrmm7UoD56an8M2WDJfC0rFLquqcpwydUv3cKWq8cIUphn8sa3MDd_4VcDg_4CmZ1cORNz1krIj7gQpQ1ucW-TYiDBP1uTu7H2tyaLuZQnkFqnx522cQiwpbquGkCQs0CBjUuivwuedq6-awrHsUBs-VZAnYe6DIGPNidwNPs8MLU-5t5K9z3_hwn_iWtzjPgOlxXvXC3vNyiknPYRLtPmXQDDHtvpWM4SYWVSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی :
به عنوان یک سرباز از‌ همه ایرانیا تقاضا میکنم یکمی دیگه این شرایط رو تحمل کنن. چون ما داریم در کنار آمریکا؛ چین و روسیه به قدرت چهارم جهان تبدیل میشیم. این شرایط گذراست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69562" target="_blank">📅 11:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69561">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1729d69d0e.mp4?token=L3vs9NZukl2zWHFVYF_dgs8NnfPwzVf0zs3P3Awdj0EJQD3TkeS87r03uVptnnxRtaNyZsgjy_2qEUC1OuFN8eb5VQvz8Vr9Imvusho8kkUfW0RphOS5PwOX2TlqrL1vO-E7vsdCeOEWKW0aEfdRRmCzgjnxxoycWoPX8PGAQoi2USYt5vj3EYMGXI6mItvyHhf8r_7R8x7ntKkNgZuKSXCUEDMcyhqcjlb21UJ7M8sXga5_40L5JxWL-YuyZPfNSFI-ZgSQcxjs5Gz2vcdlqTob7YFWvrDKgXIr9DcRLLSiXCrmnc4cD4FIj4_qgRjB_EmFb18XzynkUS9KUwJPrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1729d69d0e.mp4?token=L3vs9NZukl2zWHFVYF_dgs8NnfPwzVf0zs3P3Awdj0EJQD3TkeS87r03uVptnnxRtaNyZsgjy_2qEUC1OuFN8eb5VQvz8Vr9Imvusho8kkUfW0RphOS5PwOX2TlqrL1vO-E7vsdCeOEWKW0aEfdRRmCzgjnxxoycWoPX8PGAQoi2USYt5vj3EYMGXI6mItvyHhf8r_7R8x7ntKkNgZuKSXCUEDMcyhqcjlb21UJ7M8sXga5_40L5JxWL-YuyZPfNSFI-ZgSQcxjs5Gz2vcdlqTob7YFWvrDKgXIr9DcRLLSiXCrmnc4cD4FIj4_qgRjB_EmFb18XzynkUS9KUwJPrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکیه دلقک:
تا ۴۸ ساعت آینده خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69561" target="_blank">📅 11:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69559">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/npRjcLYzRZsOZthyBumXfxCUT7oJarjnrn1uWth57Xe2RBU900Ic3Yju_MkTP0WMwZnU-ce3hOzMoGrgYQZ5x8FbrLp4gX0Ee4mDSF4mi6j7gg5O9XX2dMkoyOwfpvgujZAxGM4dtT2wcm5jh9g7IbA-7RgMjfMt0Y2kJ6zN4qJ7cnwH1dYlkbpnLpD_LpY4EJxrghIThJtOli1Ra7-Nz_cK9EWXo2HGMmqLi5sC6YckBPe9CxUMPQZohLRVxy2k5IffNsvOoiNO9_vHbIbrGlSYKkvvLiGbRmGRLDG4lSxLaBQPksx8onnOyKqOspHIKqhEa2qAjL4iaxDmL6LO3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2fe475d0b.mp4?token=Uk2hpCZ6D309enhwVzxRICjlER7WsGNw_nbH2ITx5kLfLYEj9eMV09pYvtcqPPJ3-OqGe2FdkcC5wDfM2RHzFFPVs7jf4jp7eLZHQ2Ub1yAeZP0Ge-GGjKWn-VZynEXAcCHKfLP_7n-fCuf2itFxN3f0BoGaKqu5D1a6Dd-uU301D4i-UUDtU7FiNA4QjslFSL9YXjfvgq8S7mXzHZVrXLyC6Yf2Kmf7swEIi-WmKoBJxFzuaSTOJuWlueEv6zKYe16BknO5xIXTEADnTAdqMQfsalmCodT6szsAMeTqT_eoLLoyX5xCR-labvmqDA5XAiERKTWHZQvdy-f31Jn4rg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2fe475d0b.mp4?token=Uk2hpCZ6D309enhwVzxRICjlER7WsGNw_nbH2ITx5kLfLYEj9eMV09pYvtcqPPJ3-OqGe2FdkcC5wDfM2RHzFFPVs7jf4jp7eLZHQ2Ub1yAeZP0Ge-GGjKWn-VZynEXAcCHKfLP_7n-fCuf2itFxN3f0BoGaKqu5D1a6Dd-uU301D4i-UUDtU7FiNA4QjslFSL9YXjfvgq8S7mXzHZVrXLyC6Yf2Kmf7swEIi-WmKoBJxFzuaSTOJuWlueEv6zKYe16BknO5xIXTEADnTAdqMQfsalmCodT6szsAMeTqT_eoLLoyX5xCR-labvmqDA5XAiERKTWHZQvdy-f31Jn4rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
🇮🇷
جمهوری اسلامی دریای خزر رو فروخت رفت!
در تازه‌ترین قرارداد، جمهوری اسلامی دریای خزر رو تقدیم روسیه کرده و یواشکی دارن میبرن مجلس و تصویبش کنن.
سهم ایران فقط به ۱۱ درصد رسیده! شما ایران رو فروختین و شرمتون میاد بیاین به مردم بگین.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69559" target="_blank">📅 10:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69558">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6f67c295.mp4?token=jCwvwTTTnbH1kicYVNBj8JnZmfED1Y32GTis69jrXNJU3Kl3SY-7tWhy8gm8MwbMkn7sNngx67X4KrrkFYD3mF7doOk3f6XDfxO1VhgXEb2IJ-7_FHUoq1OupoRY5WvfixgKALW-UJ7VVBcjY_aGDld-_iAKfYDnvlca21_mICe_qfFyBOMjmley670WWiJ72tDuzPV7Q6L9o8jykFmu91BQ0XRGxRDkN1SzEk31_zOYFpwmJgSh4eUnK5cfcri_fmW6hpN-dfXQH2PtX4Dla29L2eHXpKgD03abGfAWUUTqTHtitG4itBfFWXD5CX0LcnmS-usZx-EKHmDyQ-PbXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6f67c295.mp4?token=jCwvwTTTnbH1kicYVNBj8JnZmfED1Y32GTis69jrXNJU3Kl3SY-7tWhy8gm8MwbMkn7sNngx67X4KrrkFYD3mF7doOk3f6XDfxO1VhgXEb2IJ-7_FHUoq1OupoRY5WvfixgKALW-UJ7VVBcjY_aGDld-_iAKfYDnvlca21_mICe_qfFyBOMjmley670WWiJ72tDuzPV7Q6L9o8jykFmu91BQ0XRGxRDkN1SzEk31_zOYFpwmJgSh4eUnK5cfcri_fmW6hpN-dfXQH2PtX4Dla29L2eHXpKgD03abGfAWUUTqTHtitG4itBfFWXD5CX0LcnmS-usZx-EKHmDyQ-PbXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پرزیدنت سابق، جورج بوشِ پسر:
مذاکره با قاتلان، گزینه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69558" target="_blank">📅 10:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69557">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3bMDxCQdgedUlSzkDcFi6LrtGVBDd_nAdduogwVa1nrA7EF2vl6NzkCvtOgVsV2X6vwz3mvlUfX-zLRXtJGoSwBd8TRaMBjOK7cfv5EijQV3fCuIf8sgLGYQkreYu810NDrsdeYoR4QLINDTd4rf2u_1WKTpX5tpgn2QQD1RZHqyEIhwVQmdtGAGscK-aEfZRX7i1KMDyNjeKa7gTloyoDc1hXxX7onBBJFMU_ekIWgnkVLvr6qsfOKko3W2rvoi2rR0N2TfJ0L8M4SOFxfpvMQ2C4xSn5yNu-sL9moizP2VXc88BehGcKHOhxw_EEs3HMeehszgMNDbaGaKyv6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇴🇲
🔝
بر اساس گزارش آکسیوس، آمریکا، ایران و عمان به توافقی موقت ۶۰ روزه برای بازگشایی تنگه هرمز نزدیک شده‌اند و احتمال دارد این توافق روز چهارشنبه از سوی آمریکا اعلام شود.
🔴
مفاد اصلی توافق:
- کشتی‌های ورودی از مسیر شمالی در آب‌های ایران تردد می‌کنند.
- کشتی‌های خروجی از مسیر جنوبی در آب‌های عمان و با هماهنگی ایران عبور خواهند کرد.
- برای عبور کشتی‌ها هیچ عوارض یا هزینه‌ای دریافت نخواهد شد.
- مین‌های دریایی در مسیر مرکزی ظرف ۳۰ روز پاکسازی می‌شوند و سپس این مسیر برای تردد دوطرفه باز خواهد شد.
- پس از این دوره، عمان و ایران درباره یک توافق دائمی مذاکره خواهند کرد.
همچنین قطر، پاکستان و عربستان سعودی در میانجی‌گری نقش داشته‌اند و کاخ سفید نیز مستقیماً در مذاکرات مشارکت کرده است.
طبق این گزارش، عباس عراقچی با این توافق به‌صورت اصولی موافقت کرده بود، اما تأیید نهایی باید از سوی رهبری جمهوری اسلامی و شورای عالی امنیت ملی انجام می‌شد. یک مقام آمریکایی و یک منبع منطقه‌ای نیز مدعی شده‌اند که این تأیید روز سه‌شنبه نهایی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69557" target="_blank">📅 09:43 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
