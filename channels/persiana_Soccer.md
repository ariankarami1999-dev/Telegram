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
<img src="https://cdn4.telesco.pe/file/fK9E2iL09PAcfkBnyrTi4PSNrmDCnb6pBZolFUEdYxRLFkQVg5xVmPK4Ab0-PgcqjBDnhSO9aL1iMsLOzNRF7kp7iCgpebXVMz1GubhEmOQOIjIf4oMLbWH_g_VGM0iMHXByNIapYX49KnM_5mXVEssh8T-Ph50pfQ6Twjg5z4Kk2wOSkfzeFtoYltdQ1aQ3j5lpi3BysBLpOxQh0jU83AFh_DAXpj0BJfDLv3k2MYTbYOfQHvVG_7sYVdnwgbsz8wRpd4UOoOsfgf4cvXNe2cqWbpkY3G0sqtTq2LpQxPZk6saOrrBFNBZOyJhdONF12aZ3j1A0x7KgOU5UZf-DmQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 602K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 19:57:32</div>
<hr>

<div class="tg-post" id="msg-29119">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fedqSG8yGwum-Y49iHJDlOoaGV5azJym7WmEyOIdXKajHhejboNYG2MqJWDo217QndVGS_QA2dQMwz6BZgJtV25oOlVeRWvknFmG4IELFVhX7RzL--22tj-5z_uqPZSY-X6jfFKqgeTwMvYhyn9yvWKuh3uC2qXvsVy7B0mDMPCSR5qrPIncPazQbI99YnhLSI5aRXRf11atY7rUQ01y34vpbNaPvxt2FAfduKtN7WPhmc2MZh-km4nO8-nFwtGVoDK-Aiwu06BXGgSNMYMQGhwwTXxir_p6ZER8arzTNYuQgAyeQJrQbMrD3xiWwboNrZQnO0LD1DX_heOSXiJMAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDzUGwconhZO35XvDTlMzraXzb--yicwbjvby9SElzQCBxtqO7LZeQlngwZYdDt3pgAq28MAxbZo5bqlBdtZR9SaKPwCkHpkX--e9toJsAfDkAXD2w4273ZPqahxf6pH2CMLuF-4mrWVH2Wzp0ASknyYOhishjdsrMymEEXFTl5phR7-J6GFunQw5JfxwNMwZkfhiv6FpZnHHuGaoRgFu1hNo5vHUBfKuKZX-AESZO14Xtj_rKcZgmr9gsfQODIkOsD3gBnIQXZfXImo2kFf_P1-MV03Fm1YyLePnaa3pOljBBLopcOFOFVksHAvyojGQQ-VRoSIckp4_Pqmd7fxxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
خبرنگار باشگاه گالاتاسرای ترکیه هستن که میگن امسال گالا قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/persiana_Soccer/29119" target="_blank">📅 19:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29118">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DARHFybZGpY54D9fP342nFE-N5G8jM_SXz7oXq7BnNPRfOkjldt-TlZvdY9dTpYexrH8F5PftGWQofDZCqH8rki7PGFmk0bQnNE71i8N2Enx9nYT2dme6PbvjAbits8wrre3lu1X4vMQe6dIFm_qzRLNOfyU-HPmZEF3-c2d3v6cLQAO7O1QnrvNtBPKRfGKzQUYUbjuoAH5ISK2fqFhT5Adhmli5wFAapBgqnKWkYwWG7ZCHbL3hazG_dBQs3pS2NE6p7RsAR8ywzbDm0tx8R36tuO57XwBcRifo6cRVtatMDFdDAprpKpWD8Op_OoxhhVG4ja7rJKmuzUHCCbWaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
ترکیب کهکشانی و پرستاره بورسیا دورتموند اگه در سال های اخیر‌ ستاره هاش رو نمیفروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/29118" target="_blank">📅 19:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29117">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fdd45dc7a.mp4?token=QA2-oUbJOg4C-FIiRJTWYA5m7F6ZZMIhv7ordwXYEGXDbjMUJ3m5fYWdd9t6erDfQOE4boMH05PejmyJ6p-C4FiC73Vh7wb1DmR0PuSG8kaeKvXaHfpZPDzkj6sZFHFEGoBEkEZjJbPOO_Y6xoF0S7IaTy2v84cXR3MxBct4zTOwGwSxKTKDHglXJCu1CbHg6Rg2RDiio5Xcds8zqDMQSpHxvHFE8j7DgqD62qnwf6H7JRKOyyyKb3aYspPN87K2NIsWiT3Jp-hztJHVu-x-lYCar7ZgZpCZDi-HmhzDLLigdrmM6alvmuijhvR7U1cxkXZAjkmiVDjtfY5NSJmcMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fdd45dc7a.mp4?token=QA2-oUbJOg4C-FIiRJTWYA5m7F6ZZMIhv7ordwXYEGXDbjMUJ3m5fYWdd9t6erDfQOE4boMH05PejmyJ6p-C4FiC73Vh7wb1DmR0PuSG8kaeKvXaHfpZPDzkj6sZFHFEGoBEkEZjJbPOO_Y6xoF0S7IaTy2v84cXR3MxBct4zTOwGwSxKTKDHglXJCu1CbHg6Rg2RDiio5Xcds8zqDMQSpHxvHFE8j7DgqD62qnwf6H7JRKOyyyKb3aYspPN87K2NIsWiT3Jp-hztJHVu-x-lYCar7ZgZpCZDi-HmhzDLLigdrmM6alvmuijhvR7U1cxkXZAjkmiVDjtfY5NSJmcMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
برترین‌های لیگ برتر پیش از شروع هفته ششم رقابت های لیگ برتر؛ حسین زاده، بابایی و بیرانوند بهترین گلزن پاسور و گلر در این فصل لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/29117" target="_blank">📅 19:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29116">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFfSZ2BVOqIksreZvLFlXGzn8bK1KLnVISCbYNmOnuqPXKbpI9n40BZyfnzUnXkW8ICmVIWI6urzrouIr1_Y4bbXpCP_bQTfMe1SXiiXRhx_sCWfBr2wRCDwJxuO9aBM_k26MoYqEFbfjEgD7wCW26V6m5ZaMwmxDzUWD3KAf5bdEVwiUQGWccO3ii_xahqxLvsXaNmr_pT7kgf0NSu8dkJNoHwVK0iN7mGqDd_CCe5wR9lDadPBWLiElyvhOE-_dfo8JCTsNLZZjMyH_wrC1ls8yliXEne-ptqemcEPDkGXNMaIpQJZxPR9ZEWsZdgMFf8cXuhT4QLGC_zJrL3pFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هانسی فلیک سرمربی بارسا: یامال یکم از ناحیه خصوصی احساس ناراحتی‌داشت و امروز جدا تمرین کرد، اون مشکل خاصی نداره و با ما برای بازی بعدی سفر میکنه، فردا تصمیم میگیریم بازی کنه یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/29116" target="_blank">📅 18:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29115">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oK_68ZN1nHLWoN9e9tIPrxnQQ9jiPgJ25OSth3eC8ygMWr3PJ11DcYNGxO_vL9s1ONGS0LvGwbLfCtOunYLQUpUuRPe1gHkyxKll31bLJ5eFI8P2cfNpcrSMGdFe16jHb6XCln3NoBlREiLOxecr1djSfYrvauE5Qb-rlsqLdy3TXNnZl8kgigCs0_Ma02heSZ7KdQcKOkj-71hAyc0sI97IwetVzK8_7YywrFpHX8XTKYjyNrh3eZVL-zSh8pjSy2M6leNjisAQeFEGc5w2MGMrvVH3DMpn9WuHXsQsmVM2XGpzNCZ8ItHVyii8bRWlSPEhlIHFcRlJIJD5xKI7bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لامین‌یامال درمورد دوس‌دخترش گارسیا: هیچ دختری تا به این اندازه منو شیفته خودش نکرده بود؛ این هشتمین دختریه که لامین یامال تا سن 19 سالگی باهاش وارد رابطه میشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/29115" target="_blank">📅 18:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29114">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8b6e65ab.mp4?token=PuSPnQNto5TX_uUSFoffTTdGZrSXVcjMervnHF7KIoby-ib-zbDwD7dhuWdFr0vOXM9RSO4QJ9zt1BFV9DeKu5LAbLeHexHgWFZ3ehxsvL1lC3CKSVulUInjrjSOuy30cALLWQCe3GNBHAztjzSZ_ihN4xBX9IOceGG6h061u8PKy4BKgJ4m61DSsgeUzwbSLTZCEIDZcpPHgRDYyGLBPAnd2WFzJczAqxnhx5FICz4BZ4qzttpLE3PhL9YTqCOJWs0koxXErSDalBQlc_OAFUpvfUuBpLqTmuRnm9IkEPqWP4pWWCwJ9nM7IQEoYcOoOTzUDzNKSN4dmI6PzcQ9iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8b6e65ab.mp4?token=PuSPnQNto5TX_uUSFoffTTdGZrSXVcjMervnHF7KIoby-ib-zbDwD7dhuWdFr0vOXM9RSO4QJ9zt1BFV9DeKu5LAbLeHexHgWFZ3ehxsvL1lC3CKSVulUInjrjSOuy30cALLWQCe3GNBHAztjzSZ_ihN4xBX9IOceGG6h061u8PKy4BKgJ4m61DSsgeUzwbSLTZCEIDZcpPHgRDYyGLBPAnd2WFzJczAqxnhx5FICz4BZ4qzttpLE3PhL9YTqCOJWs0koxXErSDalBQlc_OAFUpvfUuBpLqTmuRnm9IkEPqWP4pWWCwJ9nM7IQEoYcOoOTzUDzNKSN4dmI6PzcQ9iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت‌سوزی‌های‌عجیب و غریب وینیسیوس و امباپه در بازی شب گذشته مقابل بتیس که منجر به اولین باخت کهکشانی‌ها درفصل‌جدید شد باعث شد دل هواداران رئال برای یه بازیکن بشدت تنگ شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/29114" target="_blank">📅 17:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29113">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtjtEOmcsnJXQyrMlch-s5XgZyAsnQ47t3iGLQADUGTYbWcvZqx0MikOl28YOZAxC2dvdHWJmYdjQ4WbeZD4O4uCKS9pN_Vxk4loYDmXs5co4mQ8PmUmTHH2HeJvfwq-l8fgxG-3-yxkCvsR6RgEkZxTtJzYychji_PBSkxluNvT51yBwzq5n3agBgYD14H8UKKLiVbDXEx2SnbGbFn_aWwKBZGc6-zdAi81D1SfDZSJyp92ldQezL6gvBNbxI9mj2UKwKctT1SUUrs9_zKZ0YzfKOFfJCFQVA2aE3ljsMH3HJTpRSUMGmq7yUsFmQTwVYRRXkSaorx4msO0gysZvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه‌آلومینیوم‌قرارداد مهدی مهدوی مدافع راست 20 ساله این‌تیم روچهارساله تمدید کرد. هدف باشگاه اراکی درامد زایی از این بازیکن در نیم فصله. رقم فروش این بازیکن 450 هزار دلار تعیین شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/29113" target="_blank">📅 17:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29111">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca78fd8d27.mp4?token=UtI7-NnGdnwyzaOGamBOxUKzQKMy4P-TywNABOcn3A1twl-oeDkhSKGUhwB9WPsE8O2pUC2Pv1LV_hkfeHygldVQOq3_w32c_-0aCq6BBAJgeQE1zuLkRYra0yjWNEDxf6Fd5LDXxo92WPW7cOrHGXgGOuTkIPcggeh-ay8igxPMLt7S__RzPgmSO50_2MPR1OElTtoCfjonvm-BAAKN1nqrPLC6BKaxK-FIx3GCQUxDU5Vlc-MkMskUOhVRHn6_ZTDKiZ_4rgpsSpuXrwsXUWdWsTiGaNP1npxjaNLddxiMMDuj8c8y7daoOL2m9jih6GYCYZXdxeh6dmrzaVq9gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca78fd8d27.mp4?token=UtI7-NnGdnwyzaOGamBOxUKzQKMy4P-TywNABOcn3A1twl-oeDkhSKGUhwB9WPsE8O2pUC2Pv1LV_hkfeHygldVQOq3_w32c_-0aCq6BBAJgeQE1zuLkRYra0yjWNEDxf6Fd5LDXxo92WPW7cOrHGXgGOuTkIPcggeh-ay8igxPMLt7S__RzPgmSO50_2MPR1OElTtoCfjonvm-BAAKN1nqrPLC6BKaxK-FIx3GCQUxDU5Vlc-MkMskUOhVRHn6_ZTDKiZ_4rgpsSpuXrwsXUWdWsTiGaNP1npxjaNLddxiMMDuj8c8y7daoOL2m9jih6GYCYZXdxeh6dmrzaVq9gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
خنده‌های‌تلخ‌ومعنادار ایسکو کاپیتان تیم رئال بتیس پیش از دیدار شب گذشته با تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/29111" target="_blank">📅 17:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29110">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abQQEqLYzw2NvKF0P68I-0N3ZIJWJwavjnsp-A6SaczeDcmp8y5o2cXH1fHs0kE1gZp51kzUbICpLuU-uyVvJHxsjqTtJLC2DDHZkqyApoQLk-dtOiFCcIPzFaQ8gBlxChwb7Lkye0ZWzf5i2EMth2nF3Sc2LzI4m4s4tFYHltFUke-y1SVlF1Ez7wNPXHmECQt3nhK_wCfOmOXa8b2iSRBXr8dHJffTsTNL4CexAcI7039o4y6BFYcLdkBDtqcGdUU4DENxWh-BuMcTiCGOIuQsGbQ19RkQBPtngSIurGO5lXACWbhXUrVDRj-RgYTuTm6gHX8ArhfK_adlZpmIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فکت؛ درپایان‌دیدارهای هفته‌ پنجم تنها تیم تراکتورِ جوادنکونامه که‌موفق به‌ثبت پنج کلین شیت متوالی شده و هیچ‌تیمی‌دروازه این تیم روباز نکرده.
‼️
همچنین تیم‌ های استقلال، تراکتور، آلومینیوم و فجر تیم‌هایی هستند که شکستی متحمل نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/29110" target="_blank">📅 17:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29109">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l00_fjHICW7sldOWsOoTNR03WFIqHxKss2-d39TuTCXbW-wGraYDBXc6tx10JhHEPWmiwP0peWSAZW3zdShrYDPrUsEHmKKV6Z9TBjylKuNwRhQGE3aQ7Ji1K8nY0tx9nlQvwPRNzqpeMD_elI89Ernv7jNVtsReaiN09888ww5W-XntX7vKAua8VBbVUQWI0xOX-FAz98z27zJM4_1Rz5emb7AOrw_ILbD2zc6OYcbwPB0RhLG2o-ecNkib2kwb8ofz33vLXWxB9qrxosU8B2NnMpti8QFoUIH4-R9-T4GFAm1SyomyChH_wekTjXOlvFRmt5LzXbSFq9GMDYo1IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد خلیفه گلر قرضی آلومینیوم اراک علی رغم تلاشی که کرد دروازه‌اش مقابل شمس‌آذر باز شد و در واقع گل بخودی بنام محمد خلیفه ثبت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/29109" target="_blank">📅 17:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29108">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkSZWHyVOU0WjdABo0njIqlxCs1lJ3oGDYluxq4x2bNsHf4OebF37t4Vg9d4cFqk7g68z1yk75z71qovIQaWNzlpNa7nb5FZxvTqCCHdWqrreTiP2SEe6rRRfBYcQLdYx3UxRKL7nGDthz43g0slYJWkwvgKT8_DrJjsg7fKjoRiXeeG-M0qGLVVBHvg10GDdVeItyBE9nVfzf1S3_ksfqLCUD4J4qDDPLgCwrMOFMQ-BYOJMiSjj2EpJ-ce8PgIPHAHaUIFk4CcWQNdgVyQFyQG0lrcOaPIEXFlF25V1pxifsrxUFRcNWEi2nci9bZbY0quVAv261ZMdt-_oB8y4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات مطرح شده؛ عارف آقاسی مدافع میانی استقلال مشکلی برای دیدار با آلومینیوم اراک نداره و فردا برای آبی‌ها به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/29108" target="_blank">📅 16:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29107">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxtgmmfKvnq2A4DidvOtpdu87xHF6zYptHKOuWK_HnPyFqOnR5uxovfPTBIg0a5pVFBnbjuXYWRNqVW-O58YrAaBNCJ7q6-SOf7xj81onrhE--Ne6Ale3-Cf211Nikd0WSXt6qPVitl6_t01CI1Wp79tKVFRne_LQ8UMyt73zl_KgHwF_m6BGGyaOZuZQt-2ftT0nmjii6WpBd-JkftNDfo_eWuQRO_NpEmzQ9BPAWHIhVgxHegyuGpSU2plMJ3vOL6E8Dah_goguD7a7rpkRDQ9xfpnuh12pLeMx_PhV73H7UV7tNrXfyyoJL3Z1dwyPNqWGFvv6RvKsE-BGD2Jbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگارمعروف‌شبکه DAZN ایتالیا که گفته اون اوایلی که بعنوان خبرنگار مشغول به کار شده ماریو بالوتلی مهاجم ایتالیایی سابق میلان بهش پیشنهاد رابطه جنسی بامبلغ‌بالا داده که او رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/29107" target="_blank">📅 16:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29106">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3e17cbd64.mp4?token=eik8Va73xn8AhZVz1_RBi4cFEn5m-Ns8s-WCPVm5DOl15GLQNlw-8fGJnqogbyqM58sIFxrhHv1PYYP6XMniDBNhQsz4BTKdvGT-rasw1-cZ_y4tZZmxQBzdMdF1yyDJ3Gjf7qtqbBypr64ESKkDN5E-p1dydbQ9RduMp68Gb2fcuYaHeL9nFojDVVd-qh1I1T5a6jpakIe2jRdxzZzSnscyLHZ19bgwGG_-4QH3KzUWTA0wUeSTekzlzoqID3ImFElbXkqVBAW9ul1z1UaGZrg_WMQtwljEPnllX5789HBKCvQB1A3bQ_Lu366-Z5QRH_HEitkAaVcx97lvmF4OBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3e17cbd64.mp4?token=eik8Va73xn8AhZVz1_RBi4cFEn5m-Ns8s-WCPVm5DOl15GLQNlw-8fGJnqogbyqM58sIFxrhHv1PYYP6XMniDBNhQsz4BTKdvGT-rasw1-cZ_y4tZZmxQBzdMdF1yyDJ3Gjf7qtqbBypr64ESKkDN5E-p1dydbQ9RduMp68Gb2fcuYaHeL9nFojDVVd-qh1I1T5a6jpakIe2jRdxzZzSnscyLHZ19bgwGG_-4QH3KzUWTA0wUeSTekzlzoqID3ImFElbXkqVBAW9ul1z1UaGZrg_WMQtwljEPnllX5789HBKCvQB1A3bQ_Lu366-Z5QRH_HEitkAaVcx97lvmF4OBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پوگبا:
فوتبال‌خیلی‌قشنگه ولی‌خب نامرده. ممکنه امروز عاشقت‌باشن ولی‌فرداکلاً فراموشت کنن. امروز میتونی یه‌کارخفن بکنی، فرداش دیگه هیچی نیستی. من دیگه‌تمومم‌میفهمی؟مُردم. پوگبادیگه وجود نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/29106" target="_blank">📅 16:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29105">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQl776hScuGh_F__hfBTnySKy8-wMLBoZacwNhzow_qPsKXBxJqyVMufTU7u1Eb62HIkN5gUvmLV327TxjfIkXAF39xGNhgBjIOQUVb-1DvktyZsSWnI6-DQcWsDvyUdk1ozngtjIXmx6n3PJSvjp0h0ydFTR4AsaRtptlWvQe7xng68YuoGUWWQf_m7Zeh9V-hiO4-N6dNXi97wv2qT50S6db7ezv-6t2g3bqJpzGTI1zPRiKssgItzbuOC_oBYfgPYtsl_B0EX4EYhXGVHdmGsUnQHm8YsUWvNK74PS_g2oC7pofCjw6hCh8jsAXWX-q4Pj7W1rlx4OgMmATZHUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
برخلاف‌ ادعای‌ خبرنگار ازبکستانی؛ طبق پیگیری‌های پرشیانا از ایجنت خواجه اکبر علیجانوف انتقال او به پرسپولیس منتفی‌نشده است ولی باشگاه پرسپولیس باید همانطوری که با رقم مدنظر سرگیف موافقت کرد با رقم علیجانوف نیز موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/29105" target="_blank">📅 16:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29104">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0cgV0Npz-oZnE_XZyBWuYDG45EjjueWZGcSnsfQW3EHcL_RwsH-Fco7bJXwVKDlcJY-lvmX9l9qln5n4W5HCgtgUBqgSt0uF7FONj1MV93EAbsnrUIeLtWbW3B9Ipnhp4xcQpTRhTNoWBEwwiPxyHGYQ7wwykklw0MhULnkCwM0jlWnuWputQSq2LiEdyS_TFwxj3fYzhHzBRHygUtA8xYAo78Lnto2o-cpkC4Vkcf71s_PTMlOR1oiGLm2itAePlrtLuPvOjHpG8GwOLv_qPEl_Ann_hu3rP74DaFxW3j3n9xzzTW97zMpHkSZ2WOUD_VSIlJbmEfIt7fQWb6m0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آنتونلا همسرلیونل‌مسی:ممکنه درپایان فصل لیگ ‌MLS؛ لئو مسی تصمیمی بگیره که همه رو شوکه کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/29104" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29103">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWJG7E9Qj8KzmHvaQaDQAtPuk3V_7ZzFe0iRgrb6_wm5lJCCZ5daP3pWBmiTJCvhVTbf8tuiYSHmjd3pGv7WK_V_Yk7vndqt8mcF_8LUIcxZsYZJZrXeEybBK_cuzIV9_BvA9Wy5lrKbR4y518OBv-QYljFPcPh6cGeCdd2TKzpbMmJI6C1iP5XMXy5tmOCINLTPpggWpwVJVi-jEXzoGQIz6OMfTHegMfMhYr4Dsi43MPJ6fuBPnbKnTCs20wWitOTM1u26z7nCAhdfqQEG_bgjChT6TeMy6fbW_gXyEBBWXQoM_HLEzwXLhx7Ze71njNx_SxvgGXyZb3XPoPiBLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نادر محمدی باز هم روی پرتاب‌ هایش پاس گل ساخت؛ هرچقدر تو لیگ ایران قدر این پرتاب‌هاش رو نمیدونستن و مسخره اش میکردند تو لیگ روسیه هر هفته داره پاس گل میده. چقدر هم خوب انداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/29103" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29102">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vulTatCxAjwoowvepV-32QAETPc9sa23i9W0cQyECfIsoaAapJ4NP_4eBB1GGKqQ8MsMKerRaopo9m6l8bB5XN6Ib4KI5Faum04Ms84ErtAvk8fDxFNJHaw-NeRkPwryShGesA4YYkWRSnXULYhZw27gDGjFfyuhiTV7FMo7ro_GJmgPp4v0s0vWwsqi23bF1F1JlBu_Jo_u1nBpwbemcQIZhvmqS5HocMprF_M0WAYixatYgTATBZ00wWoZ8BrHsfmJjNRqaYpFmJuOgBgUZzmRaFixxwj3EnCl57BRqa7wIQrKO5WH3Z0TjfTWdGgNVfUuk7k952xJJuMiBJbMtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته ششم لیگ برتر ایران
🔴
تراکتور
🆚
گل گهر
⚪️
⏰
ساعت ۱۸:۱۵
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/29102" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29101">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrRN1aoF4QRFzU2btr8ZESIigV4i4M2sWXUfeA5jKehMLq2uQEAXQbRB-zIsiylgYefjucPG8sFv6_g1w0a4QZ8k8mEG6YGVgvSoWXTn3KIpBnC_NLxk7LdSB_uu0cjcvPyWK7q5oA4e7gE0I2PEcFNOceNJcmJa9dGgyn1aW8X4bYxtbAacMtc-zDmK1vp6JCYM02B-sdUg73IZ76fE5ybP-0I_Hq6MLu4y1ZqGNtdluGv1orCvWOiloRXd468-zNriBYdI62kYp6ZFnKRwGsM9zK-8kxo6t9jP8I6-L6ph-89KtwAmc5_s7hHZ0mpl0gTWgB-uE-x_POxqt2xN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/29101" target="_blank">📅 14:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29100">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMBSmK1qO5Kvb5lgx3F6sysW6PdY7pbX1b9fjAphnh62_N3XcpFtusDF6fiStpkG4NnWPGgws02Y5pHRuh9PBHyIGs4Fs_iiqWeCxeHa69Qt2jx3d24gtyK-Fos1ep_uf4eFHiYrcIaTk4pTsB3SlRZtQUa9PYeXeCPHYDzAfRHizapNKFwh-mMa2f_jXwWJbnuMKCLlYw2AgAh8PLvlJaWMKFodjl2tH1_Zid3dpZyzg522ZFppDFQLupCZ0d1PBYPoApE7RY6NdOmNS2qxtwIcVaFmcgLXlfMQK6v5xXE4A-x82ea6T30FCRnxceHU6ErarwSl6bCFDQx_TgGqKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطورهفته‌پیش‌ازتغییرات مدیریتی باشگاه استقلال خبر  دادیم و امروزهمه رسانه‌ها این خبر رو پوشش دادند. حالاطبق اخبار دریافتی رسانه پرشیانا؛ مالکان باشگاه پرسپولیس درپایان‌نقل‌وانتقالات قصد دارند تغییراتی در مدیریت سرخپوشان ایجاد کنند.
🔴
طبق‌شنیده‌های‌مو…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/29100" target="_blank">📅 14:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29099">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFd8RE17VbsAEIaIpIaq9gedMts79L09eI4CZM8He0ehfJOqdw12veZFXcq46UDxJ17NwV3ODw9d07xeL4agQaxBdOIi-JqMnd3wDXfVVOgLX2sS2Q0eAAFOjIOZXLGZZIssIMPkoAp2WuU54aXXd-nvZpg_K4OZk_syTYCcChKKMk55fZg82L2nQWmipNSWkFlHOHUAV5nwUtKlMqwlaEFZNSP1-SSh2orF6rDVV-dv8uIMKogymZIdCOZu75kRXi5fLCDJOftaAh3tGX1-ZmoYVG2VqpKeaaAruEkM4qKpAf9LBstmDQr-ib4aPxvEybG7j3APUXOPhO8UPMfP0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ریکاردو آلوز ستاره پرتغالی سپاهان تا اواخر هفته جاری به ایران خواهدآمد و در تمرینات سپاهان حاضر خواهد شد. او مشکلی برای همراهی طلایی پوشان زاینده رود در لیگ برتر نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/29099" target="_blank">📅 13:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29098">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yp7XI74rxJ9Lc-LsoyZDm1YVeA4G8nuFPxcLIBDhDSSh2adAXIKAyXSfaR-6NngiVecR9xTcIQh_NAh8mWfKuEpOqYshUcLHQJzpSWEOfYZ1fSGsttr6TxfobKIMeKIZrMf-4lgGCf-0BO7XHjZxYU-PISzGv30C8n9kzVdM-RrDSbp44zhysAKXTPoUHNuSus3SXHVGdoqR0MhOgtOyxHlnwgggZeepK5AHHBNKsHEWZ7lVnNylftbmk3yhPt762tw0SMz6770-0_vDbhXrkA4LtDNxbwJv0d2bqDomAt23a3-WN2tNm6RrOqb7k3D_GOCdPwomDN1q9BKrNgF0Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی استقلال به سامان تورانیان مدافع‌راست 23 ساله این‌تیم برای دیدار با آلومینیوم اراک آماده باش داده و به احتمال فراوان حردانی از لیست آبی‌ها خط خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29098" target="_blank">📅 13:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29096">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MrDLGju7TEh3LWn_SdKWjgrxj3oeiRymg_6okDX3syRncVRhDs1UU9EN5U2gFbWSezVM9Qp0ifyW8y59zXej8T2WRUMCfKNRV6ldBv3C45mNhnhf50BYQod9ItLi1oxlYGHaup4leLC5H2rptwP_rGLiuT5QVqlPn9ncbJFtFXvovX08cUkioayF_qAbrYhggH40GsVH4q6oh_XxDILorc86rR-bQ8eP2LzdidyygksKjXzV_JjhxOmvCEfb-ss-oY-Vl7XuXRV57csWPMuacfOk31Mx7-1Iu71BhzYt_P58co31K7Yc77VtzH71M4W0mXmv232st5fTshqPvTyHaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhnzDyrgfACZsLQTLTsxBYQ7047zzZnITE4DmVfp2ngSTecLVYLLQBEuv2aIFNeQyC4se9XRYltxxvjA8ryl9ZlLHhQih-1cRFFqhYjcpGJMFw62FjqmyCRGXgArVcCB5tEoG4ySVumQq7y9v1MTbRRh5TF_nt3K-J58hvGD_voR8TN71qeUHVc058xhe0rh7SyrO6cQuMitKSDx75tUNDwfVeBwZevMk9uFrOTVc2D44r3viywKuO65u2LlzokI4AQiMuGk0ReaAA4hjBrsVy92RHlNr4KvgR3vZeu4414Vd35OZHffh1l8BFa51kGgJJeXmSMNPVkYPNkg9MNJ_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوترکیب‌متفاوت از تیم منتخب هفته پنجم لیگ برتر بر اساس نمرات سایت متریکا و سایر رسانه‌ها. بازیای‌هفته‌پنجم امروز شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29096" target="_blank">📅 13:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29095">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxsPp5cIEG9K2MUADSx-jihMd1AuDopsrSKOSYP6B_Uw3nkgWFU7dcXeh-Wur36sd6BA1TjbB6UpdYQIR1_Z5dlCP64YDK6Vgylm51PoyX03aZ2BcfOKQ9sVMgBXi-Qw_v_o9e0T87RqfgUEkX8XgEsjF2cv9HRNcIwg0rHIr9hMf6iBWXEugEx1z3DDH9pP8vocTdlPEN7ouav2tqcFI9uHMsEgi-JGqZVUWYAoc8wlCmAcVSFoOL6GaBoNkSyorGUqwMy0Y9pb_oApRAbuuRLVZhyfnaD0ptp_jrUF0q8GTNiInojnE225Bo0Fm3pEiuZv8ZuwMmMVkF6pVQkBuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیوکامل‌قسمت‌اول سریال جدید "مرد سه هزار چهره" برای دوستانیکه علاقمند به دیدن این سریالند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29095" target="_blank">📅 12:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29094">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bba3aff6a2.mp4?token=Gj3jS6zpzoEnH0xIdwl2f4tmJZxCd9bqXrtCR8TwZWQoluGD5bB7Cdpg-xfgCNNpBI4Lg11EONKTUoUmsAoJZNuCQVnOFttMNbK52ZCA8shAAphslN0EP4KHI5df9MTSKA8IGzxZY15wREAFabE5Dua4r14G4QqqqgatUaXMoWyBBtH_qGXDXVFo2k-u00jg3__IaAnqmwD91l4o7GIdaGM8Apl03RKq4yM5CwJnOqQtn07wji5JcChg5LSaoEricf5KwovEgpXvlXaUWor0sKFMHc0__sCE8upBr89kVVQ6LpjFNkCjVnufWFrk92nmJE5XMIlhS6A20Laj5FlnPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bba3aff6a2.mp4?token=Gj3jS6zpzoEnH0xIdwl2f4tmJZxCd9bqXrtCR8TwZWQoluGD5bB7Cdpg-xfgCNNpBI4Lg11EONKTUoUmsAoJZNuCQVnOFttMNbK52ZCA8shAAphslN0EP4KHI5df9MTSKA8IGzxZY15wREAFabE5Dua4r14G4QqqqgatUaXMoWyBBtH_qGXDXVFo2k-u00jg3__IaAnqmwD91l4o7GIdaGM8Apl03RKq4yM5CwJnOqQtn07wji5JcChg5LSaoEricf5KwovEgpXvlXaUWor0sKFMHc0__sCE8upBr89kVVQ6LpjFNkCjVnufWFrk92nmJE5XMIlhS6A20Laj5FlnPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
والنتینا با اجرای سه حرکت یک‌ضرب قدرتمند و تماشایی با وزنه ۷۸ کیلوگرمی در رشته وزنه‌برداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29094" target="_blank">📅 12:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29093">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxGc7ygGBFd5B-VCGJ7H6orZtz3MD1R_QxxgMb97y0We2siU4PIrfe8SVD21tJ3znmrI7mzGEZFsPovXfkMeU67w5Hsg3LawVHyta0bPAifQ5EyrYTo9W2xHioGKJCuKIhG4WMrRUa-Ml7VcEPgsllSKKWzoYL5L6imBsXJr7CYUCgsNH6NVSdGftTh_R1eqRH9E_VA7JB3pH-rQn1sF6GUYLLmBtmKPGDwIxk_xuJVinTRwx4aeT0jelaSTnmdmDlIbuwt6138h7ARRZcCYIizsVv85qv1ejMeHh4kMjSv5-XJrzd_l-emeQoIp7zT1nCU-sjrenZZBhhhTmWvjhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراتفاقی‌جالب؛ فرشته‌کریمی‌کاپیتان 37 ساله تیم ملی فوتسال از دنیای فوتسال خدافظی کرد و با قرار دادی 1 ساله به‌تیم‌فوتبال‌بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29093" target="_blank">📅 12:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29092">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lgu0xdBPj8jweTlCoxVX7CxZoAZ79MZT-hJdV865B4cXkQlKtgGLYYFDXeaTATnu5qoqYUZ-upi2uqg_mcrm3JMJ5L37BFlMz7e1PHepdGPAEaUEvV37NtuTmN_FbwQtSR917KIc6ASBih8RYA0XGcP5OsyTT_ldn3P1Z7ANMjdpJ-MThIDYmJBb6vLCHNIQnsOSjIoufQFz9v7HIL54S8-ZiCFNJPLsQjiEMXzpQFecPscIaAobj8vm4nIYac8R961BseapEFB-UOyMWOpw7JxjjeAIwCQSj0jqajRG-pru5cs05tipZSOnSFiBkqvSMALvsd4iWxTn2G8PVHnV8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی استقلال به سامان تورانیان مدافع‌راست 23 ساله این‌تیم برای دیدار با آلومینیوم اراک آماده باش داده و به احتمال فراوان حردانی از لیست آبی‌ها خط خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29092" target="_blank">📅 11:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29091">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAtrAP2T43sUJ4WNda-6f78fIX-sNOoXxSC-93mGvqFs_8w-_IwnZaItIyFUkbKVr11zpBSpxmSLoa-9pdvcRzcpqBcXfCxDIax2mcZLnSFRNvNRXzNS2Oh2Vqdj8cS9oQHspsPtK6oo3RnWvmwy4R88_V3JTBnyNWqm3w00RH4Fn6iolIvMogj0sO4rwshbgiKlLRThwLlQP3QEXI1DquL0VtPw1h6zgbyDot9XyBA5HaZzAKWcmEJ3SA8hXwrq7xv2eKfHqNZUwoLu3MYMUYFqvxLgJSYK2T6Eh_B7PxZ73P3r8gL6XFZT8XriyghupQcT0t_AshjcZa7CPrRyUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ محمدحسین صادقی وینگر پرسپولیس اصرار به جدایی و گرفتن رضایت نامه‌اش از این تیم داره اما مدیریت باشگاه به نماینده او اعلام کرده تنها اجازه جدایی قرضی به او رو خواهیم داد. ظرف 24 ساعت آینده تکلیف صادقی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29091" target="_blank">📅 11:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29090">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇹
سسک فابرگاس سرمربی‌موفق‌ باشگاه کومو درکنار خانواده‌اش؛ از دختربزرگش که در تصویر مشخصه‌ پرسیدن رویایت‌ چیه؟ گفته روزی بابام بشه سرمربی تیم بارسلونا و تیم ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29090" target="_blank">📅 11:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29089">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdvLd6pYfyvpJTkISIcocA6jDfqfaw0nRYswoR8SUM9EbGAcm3XNnFPJGGdST4n01yKAZ6mmfo5hOO9_3lLIihZf6xDfDDHg75oeJcZwric3QPGBSQtGgGsF0Dgc3OZNtfFYCj20qChjnR1CI-AICngVMksTUshiBoQKUbQPllDvnBqq6qnAo4dG_OprXMCbDiaojDAoKKeder2S-ogQrPCjs11QetLMDqfEBJUwcEA9LFiTr8xPW3p85EjBlqqJ1jscmdVYHOIQXWR5UPxSSzckJ5rZLPA-DcQHCa-ntqqS7V57DDMKMoLAjjkrVeqxRnxc0IB2NZJfHiRpvLIdLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز تنبیه علیرضاکوشکی توسط کادر فنی تیم استقلال؛ سهراب‌بختیاری‌زاده سرمربی آبی‌ها این بار صالح حردانی رو به خاطر چند مورد بی انضباطی موقتا از تیم استقلال کنار گذاشته و احتمال زیاد در بازی با آلومینیوم سامان‌تورانیان فیکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29089" target="_blank">📅 11:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29088">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/527972a3ec.mp4?token=TnPg-gCPtpiHL-KsNc8RDupqSfG03TBWwM5h7bxsqOY2ldKMbRc5QonlDfxzmAWQWmoX-dto3H853AGx5ttFJqEPt3BYBUzlN8yvTauzov6k3tZoEkgLvea8bAYxpji-r8DBaqP_ed6oTKIEdiYBJXEF1fIFk_JnSvHct7taIR8y1SDub_a4jb-f-So_JVWALsLk8k2DHGekx6FhfbZUMwUPCY9N7EoUnE_z3Q8QC4_p_tf9zIIyySqxefj0U_HQQ1lEG2MaS2WD7J9GUFBEa75ezHt2PziU9etBaFQ3xRNIi-u1wq68bEZ_tfzJPdhRLJcbzJ4RbuuEeFuSdSrdcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/527972a3ec.mp4?token=TnPg-gCPtpiHL-KsNc8RDupqSfG03TBWwM5h7bxsqOY2ldKMbRc5QonlDfxzmAWQWmoX-dto3H853AGx5ttFJqEPt3BYBUzlN8yvTauzov6k3tZoEkgLvea8bAYxpji-r8DBaqP_ed6oTKIEdiYBJXEF1fIFk_JnSvHct7taIR8y1SDub_a4jb-f-So_JVWALsLk8k2DHGekx6FhfbZUMwUPCY9N7EoUnE_z3Q8QC4_p_tf9zIIyySqxefj0U_HQQ1lEG2MaS2WD7J9GUFBEa75ezHt2PziU9etBaFQ3xRNIi-u1wq68bEZ_tfzJPdhRLJcbzJ4RbuuEeFuSdSrdcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته چهارم لالیگا|اولین شکست فصل شاگردان ژوزه مورینیو مقابل‌ گربه‌ سیاه خود رقم خورد؛ رئال مادرید باز هم نتوانست در خانه بتیس برنده شود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29088" target="_blank">📅 11:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29087">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hksjnNB2lERVmlVx_lI20VIGOsHBcantPaPW1eVtwZLKB4hqMipX7upvzAkF7kXlgBRpbVSiR3I8syWMabhEDGKgtTnLq2SATe2nh5zNifLDRgEkpcJzQGRg3X4dlygr9b0uZde1Yu3oWAs07NPuw9fOpSeKiH7SF1aBa7ZDc9HBG0pjVgkhhkPsCTiCpy_YzdJLrK6IF2J51enkEuewxw2tEVbEfrA8xILBnqDPOAC44IsOADu9F6DFCRcgZuGVcCWvhJ7LMSx-qqlVU1cReZ8hk-TlSmkC3QxfP0GOBd0AGc3xHehX-KccqDi49twM1RW-uQrZeEvA8XOsejLf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29087" target="_blank">📅 11:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29086">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5nUS8EAuI8Q6gsicYED3HeQTzJxsiwowlxGqpVG8yPIoEXpdlfU187tdOiv_yn3xvzny7RizC-rsmq4p5Q9Ic5X6CkuK8P0ATvJl6EH8Vtr-Kns84Qmo32P1IhHH5Bn9Y8HnfxIKeVa4wHq154deNvH0CJBj-oIZUp14lzis_wPWDLC_bFeYow_zfdkZuNlC2xw2moSmqWRtW8JEBB4eiXgCF5uerFkKQdljOvbZh2UVvd3OFF--CmNWpJJqxdN5hp-XlPX45XVTUBysytP-V9sl9GVVHQrVEkBjrxFuJ6oBYXX8OVzl5pmrWIAcjSC_pnn3kzh_5LMSfqWlVassg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد رافینیا ستاره برزیلی بارسلونا در این باشگاه وقتی بازوبند کاپیتانی روی بازوش بسته شده: 29 مسابقه، 25 گل زده، 12 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29086" target="_blank">📅 10:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29085">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyEKdvvS1w2qrJ0LiAZGYgZeqZHLl66MLv0y7663aYvmo9lMs7TOz3_1DcPLzkvCuAifJHDipMFrk3F6Uy5K1TKh301_LRY31hiQ4PosQTrEkCycVrwfkXa0LUjRjywz19yCxqvfkUuK1UrAicH5_Rc4oD5yiLgshpvzw-VdpyzYMFJbluFlUgi5HyBKHZaCdAlWMNWS57mgGa2YeIJrdYl5wFFKyBww9iN1OpLouUjsolm6cghgfDpUuh3h81BknpTl9hqRS17Fuhef5NhJNB7gNixn7hY2dhBJv4DZWOrq3_3NI66RpL5uPhTGBiLrKHDxF-UeIQrEwNPQuXKMtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی #اختصاصی_پرشیانا؛ درخصوص فرهان‌جعفری هافبک‌تهاجمی 20 ساله ملوان همانطور درروزهای‌اخیرگفتیم هم مدنظر کادر فنی پرسپولیس هم مدنظر کادرفنی استقلال؛ درصورتیکه حسین نژاد رسما قرار دادش رو به استقلال امضا کنه به احتمال فراوان فرهان جعفری راهی پرسپولیس خواهد…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29085" target="_blank">📅 10:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29084">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVCrUfGaqoWnk9jrsM_xAEZBrKkK5uwsTgl7MALpUaAOS20jXemnO-p6kIx6DKrLtPx1H08R0PTkA49aGp9XBfOH_WkohoRUxEfJ6BfTu-NcMQXX57drGP7IDe7yxhuv3hIG__dk__jA79ziOjLogS32jfcXVEZRKS-aj8l9raPmUZeIApInsEPovDdlWdz4Gf7_pJC8DBkq5bbyhhOONjmVMx9wiHlrP9ZsYydqYwtNmff2K4FwRjzxAwkiAHo-kK-2zgOZO9kakTQIOjsFOyaGvXkjl96C23qF9YCEZL8Z_RHoAxKaOYyB5AZfvgvPW0ztRFrx5I0OV2EA8G4p6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام اسامی داوران هفته ششم لیگ برتر؛
پیام حیدری داوردیدار استقلال‌شد. میثم حیدری هم داور بازی پرسپولیس. بازیایکشنبه و دوشنبه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29084" target="_blank">📅 10:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29083">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLeAePrSs5JA5C7AFnmIs957Kp41Q95SiX9pfZpoRGf6-tWL4F3EnG8MxO6-akPEGbls4bkIVc9MuFscLWpFau0Vp3yHCv9gBIkdFoSvaYWNFldFjpNfJLacy14oOVMt_e1PoEUF0DKzSkiYaBM-der539UdO3rzqI8AM7RtWoD9uS9pZgLN8uizU96rcbMJvY0vYhxCszd-pUMkXvngIfGrfo_Mg6Qy9mTjuQU4qf8ogBzQQpfGbqvRYa1URUuoxzbnC4z0EgkdiGLZ7QnOOR1HUnaYGn8IxQK-dYor0lBy6fbVtF9NCRYzXFpf0zqImbtzM1NDblOdkM6jS5LP-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاون‌وزارت‌ارتباطات خبر داد: حتی اگه جنگ بشه هم اینترنتمون‌قراره‌برقرار بمونه و همین که الان اینترنت وصله‌نشون‌میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/persiana_Soccer/29083" target="_blank">📅 01:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29082">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAhHO7y2F7U6-QoTjc7DktF8xgDD7xe4RT0p_g1GS5PbgaMlt4yX4FhCb4KFQWcejMk8vmVDZM_Du64kDzDx5nGW1-UwY23qScbyYl1EXcjOtq7lR9g0H8iBFbHGFUy3GscA7Mh9TT14HWtHkMeH1vTEJKcSQFXs3OpslbLCki4SyE3QfbGLiqeOqZGOPXTY-kj_WZYgWqRLu_DQpv4Ln_7IO2KXvbUHbu23NuXDeRWUHsFFk0BRlqNrWPq3A6dmk4EndIt9BHy1TG0p50r_1_HwZEm9xUQsN6Bv0Wnl0pF78mozKLjD1zqu80iqPI8LKcdKanilDFPrHJRGsdnwWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/persiana_Soccer/29082" target="_blank">📅 01:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29081">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pfq_zW4UADcp7eWDJN3k4fwBqMC08Ml8dctsjwy-871-obAwxDG21gEihOjl118RzNXHaqCtPHiJvKk2JIJijVHkjp6kU7UY4SFmzoS5gv8FqBO7b8p5kWLqZ2MaKJ-e3jLLfY3YEvwHs9EH7ooam4gnKvp2LV67CFMJ_Ygxo2GOXv4uWyBePwm3zne8pPly2GM7O5WH0riNt_CBL3P83Ikr7-QHcHU0cgvZ3KCHOFYndcnE_zm2shzIr-uSEcGMRaOo9NrPHdY6YOSEDBdPYUyb0uNn8lcXZMupi7tNH_D7tGpXQPEv5nW9uHP0Q3X2p_OsRm2cChMh596IisK3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/persiana_Soccer/29081" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29080">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNo-x4s6CtzWhCcXc9pxiyGQWdb6I33NJkZFMeav45OEUNhE4vXfb3YCOon9MINysawdRXMxBg7hvpqhMhJCsbFDYcdQ-uZx5O8CUTAVJ4AUOtLP7r-JsTi7dgO5QIjwkt6q3B77HQi-QHeWkFGWYJPr5NMeE12ffv3oXFdcPCAmF5m5PrOoVVhmQJJxDIpwlqmOHIHBo-C7ShkdDI9nerphIq42ByeZshkcfYIk3JyMj2x99TvBzSc-X9Efcgr4AiniMyT-YjiYCA36W891Qq0QMOWXbVx8tIg5pMdzoKeTVWrpZZiGWpSliIkwAB2rojteGvOOKURPLPlDj04UDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/persiana_Soccer/29080" target="_blank">📅 01:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29078">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL3IgvPq6xfiffTvwianQXXMEH283d5nmEJ2upohcPY8kIOfHgY9Upj8efU47R_-LbOr38QEfTX0YRy-lAfG1A9V5f353dpf2ZUaWOEMdyhPYyrIsYsgaLmQVHCe2s6lewlVMGbhDftucDLGuTQSivNwCZMokFFtCy3jHUL7uFqtLyUVz3ZXCbIvFLiwDLR1nZGFwUrEGQYy-Ljy9JrYnPehnTMTql7wvhBmzrQfNDW4RNZGpyMAJV2ig-MsLlNJ5dypbSMrBlUyIige0Qgb8bmVreUGHIfrw16-noDsNpCw8WHJ7NrEz37MP6Xlfimh9BcdDV8HM5CVNU9gevz8sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/persiana_Soccer/29078" target="_blank">📅 01:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29077">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEWaUkdesOqXtgBMxUxxSQ9oH3DMxX-CRLh40ZU0ZLx8Uxx8w_zZP71wfRYjH90JaDAyCgAuWlq8OWfP77kpo30hR8R3QobXpftdObILLECsmvdZbicLazXFimS2SDrWwrVHNiGuH4TW39w6l5P__7t77BRCCXo3rlfiz_dGfeXmVoidc-6Fhr-HHtmdXooDqj-gpWaOBmZ0mLfEgdBRVrK20rTRZjs4cXNFMjc_f4DN86iheZtOSyk4amnOSghhhe16GCScWcmLT3tGJLDBm3Q49Hpmw1F1OftCBWDnGLW-wLvD2l2DxTXKNDyp1vvmXwMOvr-cJXtQ6_G_QQjSdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ از جدال مهم سیتیزن‌ها با کاونتری تا دوئل شاگردان نکونام و رحمتی در تبریز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/persiana_Soccer/29077" target="_blank">📅 01:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29076">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYrQBjCz6HX-SHvdTr6iPrsEItSyBSzzsSTtkGEmJirzr7DuivsoUGJzpGF5LX6x9kOhC2fM-M5okdklI2UndI0x3PYQ2bjxqULdTr0cVNBeYuqZRrC0erU5BhL_PndJunuMTukTit16eaQmb6ChNcw87AL2A22MJMqSLp74ErodRDCrzMYd7j1BCy4bHHjiJTxiQMrysCap8rKGPYBpu0WiX9LGY8hDfecaGF5KufKBxf18_MKrXVume9dXPjtQKas2LvsnzoXJbNc4b8kvhDbm9ihUbmh2NmRY14IXrdUNS2itSTylyJ64hh_c5UGmzxYDb4Q9ZlNqxitHhQgTEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبردلک‌لک‌ها با دبل ایساک تا شکست همزمان و عجیب رئال مادرید و PSG
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/29076" target="_blank">📅 01:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29074">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qlav1IT0-570124oPYtArymsDlKHpk5ml-8nSwc_VWgFBT2Svgwa2XIFNEz2_PYaJYO3oJ8TiM5sx5aeY5xiHz81MWTI6FrobCFP3xADKL1A8GLUNmllEQMYEX06uYIa3fmLjYqL5_KFzOJ7I5Jl3CvOXv13AhlGI6poGE2FVTOzK7NoPwk1ZWR7XpMQBlGwpKWKmuTo9JDySOLt1SmWnriNb7grMYO4MqvOKh84wl3lnG2_VZxNYR8yl3XvZ9rqDKmrYB-XYw3_spUZJs-hP_tFjQFz9UeqqlCYhKpKVf6twWWTefO9xxkANkyesqc2Yxvv_LCjY1jv5_25Qwvopg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده لوئیز انریکه درپاری سن ژرمن: سه قهرمانی لوشامپیونهه، سه قهرمانی جام حذفی، یک قهرمانی سوپرکاپ فرانسه، دو قهرمانی لیگ قهرمانان اروپا، دو قهرمانی سوپرکاپ اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29074" target="_blank">📅 00:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29073">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRhqNyBEtqY6E4OkYgbiGyMTxgySm2Vfa9Q3hsxpH3zkal3vkBQeAdUT7BP0FABr4VCludKo2jY0pOQzmn2v7qqd3nVyVPAEx5rZCjCgamDTEiGz9p0eZuqiGbpiSU33i5EcO4bqyDqzr8H_dVDszRggDag8_IVFTv0DGq6eA1jSNykX5d7YHWuylGn9tXpDBA5YZSR3ykeozs2hwDY8CvjMu8NrFE8h5wKSJIc5jv96a0iD9822gOlKw-5mTBLhDUatrwR0QJB-x6fC29eaGeLfvQXSm_sG3vZ5lSmWnbGk1lN3U_d8-asGb31Lv06F2Istn8i-1tq0HITDWAsjOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا|اولین شکست فصل شاگردان ژوزه مورینیو مقابل‌ گربه‌ سیاه خود رقم خورد؛ رئال مادرید باز هم نتوانست در خانه بتیس برنده شود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29073" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29071">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRbVZxgLlH8kfuowAFTzBZFNPgFsZUv3iGb6MlMw7ASEmo816oZLKVObPpJ6G4Mz5xiKmtSJHajEEYhpnlS6EX4zB8crHV8mc1b0uLyX8ntNNyaGkiKZ_LcrWF4iii8tSA_VKau74VvmxRtukbbCZ3qNpb0-fgfFF14OAUli0E93Q1oakwiiHrlB66C9zNV1n_qdc4iyQ8Wuq5t4sUp2U7k4rgmtPRN0moXljeWCIJt2S_J2yE79HyMioNVKzqgbC1SIZvoIITabIHE5ZTWdthIJWiZI1IWBC2x23BGTXcL9jhNSV7eWtQWgkVT1_1IwJRhRA7yQXgsjtScSAljZGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شاگردان آقای خاص بالاخره طلسم شکنی میکنند؟! رئال‌مادرید از آگوست سال 2021 تا به الان نتونسته تو ورزشگاه بنیتو ویامارین، ورزشگاه خانگی رئال‌بتیس این‌تیم رو در رقابت‌های لالیگا شکست بده و امشب هم تو همین ورزشگاه با بتیس بازی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29071" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29070">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGp8U5NsWlckF1XA5Jr_lNg3yoAKkXqo3zSYXVzPiojsEgF3lza2vOhn4cuwrgveVjx_u0IfpHzVF0f-7oZ4Q7VDSgM2haPK6jucz9e59hv6qGnoUnysld5QM41Il-Xgyakt3grZ1e8w1F870fThpyTWSvnQp5CCId3ekP4kWBL7Nja0kPdUyYSdPBbBpbO5KlJ6tzIuFlZdexKBeKr8cYaYwlXQ6Hvtb5PhRkyu-M5B0iSXaGXt9K_7NNUMf2_r3mZ1KdvrC1c2Cu3r0Octxt8gNK8kxPr4KkSG9o5QvEErgTKBdH0PlMdoKeBfvJuLZLCillXqMLnLZIBO2jeP_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/29070" target="_blank">📅 00:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29069">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
سوپرگل‌دیدنی‌عبدالکریم حسن مدافع چپ قطری سابق پرسپولیس در بازی امشب تیمش الشمال مقابل الشحانیه در هفته اول رقابت های لیگ ستارگان قطر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/29069" target="_blank">📅 23:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29068">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pd1FM-Xki3P5h6oDYqg_zU-GGkK-2r9QErn6S_v9uXCCBmIzQls0UnbvjpipgzD4g6Xlf7r46-4xd4G6tfJ17FTh99ebHnSLe0NHP_5z3jo0FfmND4KnOOxDItgiIB1s_XeetcveSFUgO9PIhp4HrGCjDisEAfo43q0FqDiv4qOKVpM5HmucCM8CD3rtRXaE6YKcmWvP11XqEyXbW7NSg98JmJIVf6_bBiaEsbLERUrib-_A1dgiOMD4wW14BBfDGsVw0YZ0PiZrdBOXdzXEgxxciRwr3DjFd3FqUYp5Zi47gonQxLYOaBhxhmPrrgj0rgFgOmHvd86DU5suGxMC-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پاداشی باورنکردنی برای نمرات خوب؛ یه پدر مادر کرمانی به پسر ۱۸ سالشون قول داده بودن اگه امتحاناش روخردادقبول بشه دوس دختر ۱۷ سالش رو براش میگیرند. ماشالا پسره هم کم کاری نکرده و تاتونسته‌درس‌خونده و همه درسارو با نمره بالا قبول شده و همین چند روزپیش‌رفتن…</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/29068" target="_blank">📅 23:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29067">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGlmelvZxmQll7e8gnZiQIBXmotLVVWT532fAQnneVDYqCMUd9ejSFM-wkIm8TcJmLE7H9FqcYJ4vQ-jB4tRBgr00oBcpARYBIG546_eEiZq_VCcNl8A1V1ZK6kkakxNWcatDr-rDtI9k9R6j-4EtYsXy6sCBMfbaZGw2TFbSkEkpMGe5K-iGf5ZHvUcez8oHqnEkuHooZqZgwLP9qjT1bWlf1s7Z9Olh0gai69Qm2iURUjJTnLj3z7yQm4_aSBMTs1RNe8-N0s8MIWTND-Fvo8DCge__HCXxlKK8xfq0DvvgeaLepAfhHIr4asfEs7v91WMJP2vvmsua30pFhEQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
پرافتخارترین باشگاه‌های ایتالیایی از حیث گرفتن انواع اقسام‌جام‌ها؛ یوونتوسی‌ها با اختلاف در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29067" target="_blank">📅 23:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29066">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRSRmuqrKlK5E5sN_Y797B5Pn0Gs64b5mI4OrpsCTsjmWGCc5qdiIeADWFbbyi9F0gIjBAcsNUn8oMrGRRxjoztBaySOy_73l75a7S3rN0ZWlve5tS1Y88_Ja0-LjWKZyT9hYB5keI1Cva_KVa3FfDQHOBPZThBSM0yytcr64J1IJzUPXfcvMpa_PG5whQkhVwMDK2Q7_GX3hoRl-T9kur1D-sE2BHMhT6NEvo3zJnMuxgCwZhJE62t6jYhFRGlMxbat3ZSSpiFaAnIOOQj2wD8xlHcFLRZT0pGZFhituN2JY20grYSn2iHvOADwBQZYQ9aB6f5vpP2FkT6kYbbFog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رگی لوشکیا ستاره فصل گذشته تراکتور که با قراردادی دو ساله به این تیم اومده بود بعد از جنگ قراردادش رو فسخ کرد و با عقد قراردادی رسما به الظفره امارات پیوست.  این هافبک آلبانیایی در ۲۵ بازی برای تیم فوتبال تراکتور ۶ گل به ثمر رساند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29066" target="_blank">📅 23:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29065">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWvSRcCICRiskRIHH_E3LOUgTAvhTNZyT_9hyiW8t1x6rPD_4UsOgAfdSs_U3jtoQkQHvQPzR7EDb47mrJcftCo3t-IZsLUTWvVVueIM4h0BsRNbibImzsaw-RUK8dClQVA2-KnLhuivcStFleJVNo5QT51heNhkBPKzu_z2O9enngJC1pJR5RlEPVxn4-geqAJLOnnth5tMwgW8oJmEfue9Tiwm5UMe7Q6ChuwX222luNOHuWNhpq0Z4Fng0FrIQnzbZkQHLxJ8Y2sojyf0efIxXm3_2g0GVeQCNvMfpl3IVoYTsN5d3oYVfajW7ti8W1h1M0RJJyPxfwotnymOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌جنوا ایتالیا به‌این‌شکل‌از استفان الشعراوی ستاره 33 ساله ایتالیایی جدید خود رونمایی کرد؛ الشعراوی یه زمانی در میلان فوق العاده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/29065" target="_blank">📅 22:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29064">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXOBGBkOXNA5VaaRiQj8REq_B98Dz-bTnicnvw3jr6BiguV1QNzpcuy98KiFg6Q60114ezuBVHwKk-9QxrC5lSf-dn8h4-YDvqcZOve3lmbN8G8kTm1_ntqtZBW-3DPqSmG_CHFIKoDQxF6TPVG3KQC6iwH4uw8OrmzXre74D03jPkm6bI9DEx-tLmeYWZmjnE91BXvdRr87ikXUDVe0zeoalsi9eGEl9kuP7R6LeeFh9vYy-RKLx-GXsmU42VZ-NssRmg_Q2zM2wn2RZYxi35200MuBZsPKa-4cvkBDE46tmFbWekuOlIS7e5QijGROaUyRMnmdg-I8W3_Zg91n7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میزان هزینه لیگ‌های معتبر اروپا تو فصل نقل و انتقالات؛ لیگ‌جزیره بااختلاف بیشترین هزینه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/29064" target="_blank">📅 22:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29063">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJGalCUD8dQ8Eo39gyQQNaLEgyWykLhrhsk23sfNpv-1L4ytPORwgxZMRucHomfyokENOW1CiL-B8q9VoRNw2Y1Im2Xu9ty2WwXXPUObNy6xscZ5osbjUmWuG-AIZVn7VkE1lkts8JBxBYXo5eNviW8smDcrjB5wnIEwQS1kT_EWvWN_IecC5djEfQKY-lyNTW_VqP9P3upeDxQzt4GajpZSEwreRONUz5yFafcDOEBi_B40723wUTlrCexyM4KPHiEDNHWatQWpyv9l-FUHC6DAGkJNf64WcOcr6DXBBj95UB1X2o1GkSAlSlVri9uYnDWpy2f1xWb-5RIFLV4Zag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ویدیو صحنه‌ای صالح حردانی در بازی با پرسپولیس اصرار داشت کاشته بزنه اما به توصیه سهراب بختیاری زاده یاسر آسانی پشت توپ وایساد وباعث اعتراض‌کاپیتان آبی‌‌پوشان به کادرفنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29063" target="_blank">📅 22:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29062">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsjCYlvdTcIJd8bPpmthLRiVHKd8jYdLZrvNaHlyxRBXurMNCS2xkzXP8xT917CyC39zBIfWRLCmG8C7PiFxMOXgcxz5imp-R-Krh9oexDiQPcjweH2xfZy2C96MOaLkmPPoe-dB96Y2GKvFnLmVy4aauamDwxPvSW1LTtcK-ecyW4eiWjGUXJYIR9HllDiEWd_26sDB-e85x4mHqjgwSeGnKT7MjIn5iA2F_cMnssO-Jw8KqylgLNrnPGcPsLAFKCB0ConxUy5tlVWfeAJ5YCYaPGqKnnaiX9jHQMw_CxZBGiHHVScqQqpOBTmtIfxEVZGSuMvDsVtgdJqHHwurKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
فرصت‌سوزی‌عجیب‌وغریب و دور از انتظار طارمی 34 ساله در اولین بازی خود برای الوصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29062" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29061">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSiJHjTOy5GxfFw7O7zNRNZ1H656WL6mfBGBwUTcg5QZqu6FrI55YngdxTTm2J6YibzsqRC2BgT7I2iXB4vphHNA9VbzOr9l9JbWW_P2bpCJZFnl5Vb-4D4OunV4bF6WXLfLxahXKrK1Frn-UPgrAYIysGXRvzjLVMhLiFmUOnDYTU8_UjVdFgkgkWLeGMWOAL9vFsG0_qgyOvhYzsE_NHrHGYB_PFOLOxf3s6CzoWRGAbEM2vmq3U0zKX6EcXDIgOXXd3h0FRA4B_XO7gAMeptZHdspnt7cOyj9oky4tnE4rnSkTlT2i3VIkjmArXGfMSCSLc_yRZ-VHx_qtCMsJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل بتیس؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29061" target="_blank">📅 22:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29060">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34787ce1a0.mp4?token=bsgZlKmSrpDtmtF4FNtXOxFck1bhOMVF1ygx6CwXX402YuEvZweRnnlP6aVFrlKIFgjkRBmDIBVXvbnfVqsTmyJsQpSZw1FEMqgg4ITq0eyFmrQG_xr-3LlSehsqImG8WWL3Za6_stxXFZ-ATWJh3y3kZeKIAjlmSEAFF3Wxg1ftS1dLBoNmCr3KRbeYNWHSIXADLw2SfWe_yAjXdFV2Cpzka3ka0crl-tGvfIY-DzLK9dYigyKppd15qVOdWKGaPfRNfWnBeMY05Cr7lrbmOYMDEL3y56Xcawwg0GIAJIObOoIycBjBbH9brmhMqhoJdTnsaUTtECunSkIpxl0Q0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34787ce1a0.mp4?token=bsgZlKmSrpDtmtF4FNtXOxFck1bhOMVF1ygx6CwXX402YuEvZweRnnlP6aVFrlKIFgjkRBmDIBVXvbnfVqsTmyJsQpSZw1FEMqgg4ITq0eyFmrQG_xr-3LlSehsqImG8WWL3Za6_stxXFZ-ATWJh3y3kZeKIAjlmSEAFF3Wxg1ftS1dLBoNmCr3KRbeYNWHSIXADLw2SfWe_yAjXdFV2Cpzka3ka0crl-tGvfIY-DzLK9dYigyKppd15qVOdWKGaPfRNfWnBeMY05Cr7lrbmOYMDEL3y56Xcawwg0GIAJIObOoIycBjBbH9brmhMqhoJdTnsaUTtECunSkIpxl0Q0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سکانس کامل مخ زنی به سبک مهران مدیری در سریال جدید او بنام مردسه هزار چهره که از امشب فقط جمعه‌ها از شبکه سه پخش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29060" target="_blank">📅 21:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29059">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEXEEVADXqmquCQ_Wg-jKgCkJF_OvfcsKq7PSjhBXf5dFy0JR-2vr6pS9sYkX4byCvaYRu3pgwfFEe42o_J_jMmUzsLInGSl-APFqu0080FI27A5mDnHhWxEI2rMGfRFIfgYvP-BYuIs6erBnfno2R09ivdhrojCoviUCpDZ9Uaz73PoL9gXk6CpXcjyHbuFmmDP1MZ6wXlSNe29M5jrKLhtKy_WhfoBOutrVG35H8thW7p0YQgyePDoy9pFiYmezckyW-MM5TB-CXU_XZSfvcGYKbVAWl73vfiuLKoBEFUnv7kk2RJXev72bkMXooxIzXZRdmcqspW6kZRE1jUq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا؛
شماتیک ترکیب رئال مادرید برای دیدار مقابل بتیس؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29059" target="_blank">📅 21:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29058">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf2bf71bb.mp4?token=E_Ry246ESrQWAxLG6-f8J6NY68dGI0ageYZmA70EVVBXjQAH_bSIfSh3Sk3E9Pg0nv0T47rEe7MBAMYxyJjaXdng2lsIcGRq8sXBo6I4qIxXx04_VhHiCYvE3o869wp4lmK7gm2C0N3KDc3-eJ2wx0bE0sdOHisQU81G-MModjWTPAEcCUufRFgoIq9YP18PCKS_34vDodJgqF6uA_3vcf8NWVNhn8FLiUoyfDlBf1KGW6ifQYylgBu3WmAxUq0uU2v39Z2N9bAUMeSyelPoY4kARSzgQAzrFkI3VZ_U3x9ffgq8CbqbhQIq50Nb7sutfIiA1uG2TGggXQ36JOUjGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf2bf71bb.mp4?token=E_Ry246ESrQWAxLG6-f8J6NY68dGI0ageYZmA70EVVBXjQAH_bSIfSh3Sk3E9Pg0nv0T47rEe7MBAMYxyJjaXdng2lsIcGRq8sXBo6I4qIxXx04_VhHiCYvE3o869wp4lmK7gm2C0N3KDc3-eJ2wx0bE0sdOHisQU81G-MModjWTPAEcCUufRFgoIq9YP18PCKS_34vDodJgqF6uA_3vcf8NWVNhn8FLiUoyfDlBf1KGW6ifQYylgBu3WmAxUq0uU2v39Z2N9bAUMeSyelPoY4kARSzgQAzrFkI3VZ_U3x9ffgq8CbqbhQIq50Nb7sutfIiA1uG2TGggXQ36JOUjGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استامپ‌من‌کیه؟ بریده‌ای جذاب از سریال مرد سه هزار چهره. امشب‌اولین قسمت این سریال پخش شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29058" target="_blank">📅 20:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29057">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e99ae53e7.mp4?token=uxfSwWmGja7HpRkuxhXIdjI5B1iImTvqZ8N348Qs37TwrPyPmnGnCIgnT9unvEUgtwGcgOjd27KEbrKCXSJ8ppHeIPI6LdfCqV20u8BY_mJLLeodUklrgnLHLwezov1yAJz5MhLQy2WkS7xB_b1kG5YJ6r3VsUR9OIgyWtWSYiP77V6K4mNi2NSGW1SpTAyhKVFmAvhjTzUwQOs_FzMMQfy5Y6_YVL5UcyhrQkIgYK4oI0v9wxSKWaGg2Pis6BfCukp7r1mjaWIST5NBfJK1pCT0zSgqxnba0dVoWB82klxwqBnivGvypfKl5B62hvGW12Ki3Qi3m4GYRG06gihyAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e99ae53e7.mp4?token=uxfSwWmGja7HpRkuxhXIdjI5B1iImTvqZ8N348Qs37TwrPyPmnGnCIgnT9unvEUgtwGcgOjd27KEbrKCXSJ8ppHeIPI6LdfCqV20u8BY_mJLLeodUklrgnLHLwezov1yAJz5MhLQy2WkS7xB_b1kG5YJ6r3VsUR9OIgyWtWSYiP77V6K4mNi2NSGW1SpTAyhKVFmAvhjTzUwQOs_FzMMQfy5Y6_YVL5UcyhrQkIgYK4oI0v9wxSKWaGg2Pis6BfCukp7r1mjaWIST5NBfJK1pCT0zSgqxnba0dVoWB82klxwqBnivGvypfKl5B62hvGW12Ki3Qi3m4GYRG06gihyAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇷
🇰🇷
سون هیونگ مین کاپیتان کره جنوبی:
من همیشه‌گفتم‌که‌کریستیانو رونالدو الگوی تموم زندگی منه اما بنظرم لیونل مسی بهترین بازیکن تاریخه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29057" target="_blank">📅 20:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29056">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6oyZAiWfCkkCzKFuyjrYna1yD2pgBFazBeQARXLS-wVfTzdJbtFGiZES0I5FofO01lnoOiRAfraE_jTQj0n3ONXbP6Y8o6ks6glvLXv3k_iaudz4yC8bEXRW3JGBp6mzPG4rGXStqiP-UpUMv1yvG1C35uNI8gUP_ooFLZo6XjxunpV_oM_rmyjmNPgjo8cgxnmTgJ1uETu2J7PDIOk9S5CnGuUplkCESHOwGrwXueBduIeVwQAdFK3ee07I7NZcAY6JenRJQARNtBuN5BhPWz7UfXk0liaWM-r_kPWSi-LUj5YFzQuvIWnBj7qQYXHpI-opfd8R5bb3OrDv7Fcag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29056" target="_blank">📅 20:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29054">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAMDbSQj6H7jKkbcUz1bs67Pr62zIX63sPYqhPJ0qFl_OnXR-DkAMkP8grlw242OC0WJh79aAXR36ceDTBk7A_czO9eAHafAPmHL5RmdmzwdMH1HZ_zbzdxdohcorE375sg7VNt8XNrzkK2Lyxku8RepBy7S08GLSEegaKDHbVQyc6g8QX_yo-uNXXcmeprfE3yWCfWvQUlqlsBm1wkDI7GBzCS8zyjXHxN2PckYdXtSk-dWjamRKV7gubJhnVJy2ChS8fieKyE1A_gtnLwMRlWPhIl6oHSsdrq1afT85nSmyzpudUQl0VYZi5nDfmtXg_3YxDKu2IFjiXCv5waRDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OrfbVtAgxQrOiZJF6dfxfvSE0Ilr5G2nuMGqtLues010lZgsPyJ9CeIFRqr0rfiyZzYQgZxMvMHScro9DtImNJMTYfC9ZJXUrpp43uxXJoZ4KIei_2rYDmC5ok__U_SKKVNzKL48d_c_1wGiDYpJUk_jUY5XVu3oba-k-4YSsV9UHn45Ix1DNY9IYDKFvYxOvPFuQHZaXErpQy_rg0z8lQ2VzIaaxS-1V8VhzcpgwqrdKDHnBJazMILgpTIul4PCKeKvdZOTlvR5DGp1TxqYNXazEl9iCyZsxbeNhKQP4FQ7zZK2emaCheyRsStViZ0jGrRu7gnMXOyMRutnQEf9GA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکو خمز و شوهرش برای ماه عسل رفتن توکیو ژاپن؛ تو کامنت‌ ها ازش خواستن یسرم به شمال ایران بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29054" target="_blank">📅 19:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29053">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDbaHqxNVweq3SHN96Of8Jq1OdxABE-Dcb4iwNEurWpScJ4Ur3CabDCKVAjzX3-tM2WgbYL-V9Z5Dwr6ULpWNuVp5fPk0Yt2irg78WNxOhXbytz25G9VflBS0Mgd786QKM9NKh5ZSB-rkGtXnegZzmibXFKHSe5u9QVv6voPPMT4VLYEdCzucGWQqNHRiiYh7IDxJm6O_4kYtpEYXRIgTwwpyU_zt6GoB2JBHjSvXXyml2QGQuJVYRbMm3uAPuqazZGbP0-ItlnEmZy-HzVtLlrt7hB6cy9WCbt_YLW1_JNYt2-Jwbk8qRwEC_vR-5JMv4HwWv1EKDpQ3oJ14lpFFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌جنوا ایتالیا به‌این‌شکل‌از استفان الشعراوی ستاره 33 ساله ایتالیایی جدید خود رونمایی کرد؛ الشعراوی یه زمانی در میلان فوق العاده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29053" target="_blank">📅 19:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29052">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef0797e3.mp4?token=kUknXcUy7gDSeTDCOPw7oX13Oh6jOWhUJePfim4V7lkgnHwZdvedE7dJhAqi-kO-K2Q9YlJvHv6TnIQVQgidnA_nALhllf3l9njQkL0tSTxIyghY-p9QDo3FxAhVdwuEVhEGOkHADrIdjwk3sMgxdi1rBLV4Rzns_X5XStCBDWjhnMpj_9ubZqD_TL69EYUN-9Wm3wjP-owNgfuhWDlJXk5SfAEg1CLWYIGA95J8sy3E8tlT5MYfF08q6S9UzTsR2WpeTyLsFThKg_DHZKTpuW5ZnUihwzF9dR7GFD1t4ee_EaMfbeR2lWYrZRLKoLI_t0t7SYkX8mJViFbGBmKn2EqyEPBQoDr_XnHvwqbnzEMrKcp3p6WCva2QEIauXW72VS5OG9ShxulyRvHRO88OwAT3NSPFxzxmGbj39RhiG9-WXlTnJs57oAZ5OOloB-6gJRcT8TAMrjqgF97oJ0JZQfBDoa3wGrFmRMBoyQaVJ_H3gjtFduFTGm2YMA__VhDEPs0gUigczoozpd8Wpf8QWHzLS133c5jtfBGVxVlAh8_2TYqeWcPQpGFQDtRuvsDVZRxKunUI84aqVMxa8Gw1Fx7x2ElmmTfNPtNYBDbTVvM4Ufdj78SwpRfQ4Hz3KP3MxDEetYpshD5NeP1oLBchP--w3ZrWRzoJc_x6B0-OGC4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef0797e3.mp4?token=kUknXcUy7gDSeTDCOPw7oX13Oh6jOWhUJePfim4V7lkgnHwZdvedE7dJhAqi-kO-K2Q9YlJvHv6TnIQVQgidnA_nALhllf3l9njQkL0tSTxIyghY-p9QDo3FxAhVdwuEVhEGOkHADrIdjwk3sMgxdi1rBLV4Rzns_X5XStCBDWjhnMpj_9ubZqD_TL69EYUN-9Wm3wjP-owNgfuhWDlJXk5SfAEg1CLWYIGA95J8sy3E8tlT5MYfF08q6S9UzTsR2WpeTyLsFThKg_DHZKTpuW5ZnUihwzF9dR7GFD1t4ee_EaMfbeR2lWYrZRLKoLI_t0t7SYkX8mJViFbGBmKn2EqyEPBQoDr_XnHvwqbnzEMrKcp3p6WCva2QEIauXW72VS5OG9ShxulyRvHRO88OwAT3NSPFxzxmGbj39RhiG9-WXlTnJs57oAZ5OOloB-6gJRcT8TAMrjqgF97oJ0JZQfBDoa3wGrFmRMBoyQaVJ_H3gjtFduFTGm2YMA__VhDEPs0gUigczoozpd8Wpf8QWHzLS133c5jtfBGVxVlAh8_2TYqeWcPQpGFQDtRuvsDVZRxKunUI84aqVMxa8Gw1Fx7x2ElmmTfNPtNYBDbTVvM4Ufdj78SwpRfQ4Hz3KP3MxDEetYpshD5NeP1oLBchP--w3ZrWRzoJc_x6B0-OGC4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#فکت
؛
رودی‌ژستد،کوین‌یامگا و یاسر آسانی سه بازیکن‌خارجی‌تاریخ‌باشگاه‌هستن که در شهرآورد های پایتخت موفق به گلزنی شده‌اند. جالبه هر سه تاشون با گلزنی مانع باخت تیمشون شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29052" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29051">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c83a1c1d.mp4?token=TpcPGGgM8_U0tnGmdSnwkAAAJBSGQs-Z_S6evkB7_iAlNKjbB7dU-0JAanSrKYt2FsGS3eqcdt9JYTqM3WrkS6jS0NW5-tDgnxfMfCiWztyg48bxzFFUeXqradhEYWQb-qOgLd8BD-yIg4a9KNd6EIZvMX2OYqQ5Y7cRzF2ooW_OcayR-SNfACc4yKSN-hVUDYzXhYo72nu_fQlSueJoby6mXAMDNz1M3Mb8MDxJ6TNFGm7iDTllKUQ2zSu5saiCHYzqI70sTGvq3kak1Qo1tVCUp8lR_GYQpniMsySJVxzjniZ0uzBYgCjutMjWjmvfbGyvBe2nMOwaJ2---sKw_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c83a1c1d.mp4?token=TpcPGGgM8_U0tnGmdSnwkAAAJBSGQs-Z_S6evkB7_iAlNKjbB7dU-0JAanSrKYt2FsGS3eqcdt9JYTqM3WrkS6jS0NW5-tDgnxfMfCiWztyg48bxzFFUeXqradhEYWQb-qOgLd8BD-yIg4a9KNd6EIZvMX2OYqQ5Y7cRzF2ooW_OcayR-SNfACc4yKSN-hVUDYzXhYo72nu_fQlSueJoby6mXAMDNz1M3Mb8MDxJ6TNFGm7iDTllKUQ2zSu5saiCHYzqI70sTGvq3kak1Qo1tVCUp8lR_GYQpniMsySJVxzjniZ0uzBYgCjutMjWjmvfbGyvBe2nMOwaJ2---sKw_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29051" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29050">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_I_sLpXHq1Js7eexg3I5_-2TCvfrwmRvndFAS09sQMemoLPvKO_u_2Epkhjbd5W9C3VoQjdfDjCrms0AxumnhoRTNnPbRhmdXYTUuH8bjLptCSims84Efi-tdmcCXSzhjwmT_ZTxOfbz7Cw-rmNDn-xpIMKce3zhyLx72sIBeFc08pU0NzfKSGW4u1BgstpQPMprT0DBIzhXVW69jTDy26dXktXAymRBKQQblqKZDKITrbR0dWHMtbDyWKwLrW2Xj8mCJofilNtSdotZmmZeVDq1csbWfnZIkDadM2Wv0zuGRmkFWvPm4tTBhJ7QC2fbJ847RiGQj6ytxlL6alCBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
هفته سوم لیگ فرانسه
🇫🇷
پاری سن ژرمن
🆚
موناکو
🇫🇷
⏰
ساعت ۲۲:۳۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/29050" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29049">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sq7iSx-MtSqulyRhz650TrZLtdkdLzrcFzDGniGylGX_21gGcFbEhpM9sWnwUDG8xUI-SsXupZiAu2fYd92_1v71cRf8ogFVXHg197aXVvZOoar1Ham4VDgDwT9mytLCKy_O09urgfhDcWNCRg37TDjPHlsLQnRHBg1V8GmqLFgeLuoz3QDtfVrNuarh9vK1JEa5Fv4MdpBy6InRLrQjtesWNt2D6Erb2MwZ0OkVCsWYq8RiYMdBkBPIm43s6KLxhV0-f8Nt2yisIhuSBUIzjHhigfbjfzgKRaiW2teJv13GNdTc7O4BtDqFRsnb5ejqZlE3377M0inTDZCPL6cNOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عمق اسکواد بارساِ هانسی فلیک در فصل جدید رقابت‌ها بعد از جذب ژسوس و اتمام نقل‌وانتقالات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29049" target="_blank">📅 18:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29048">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ea3s2hYuor_9sx61SDTnbaOepSfHwCI0UeNXbZ_GD5taOCvz0dICWiNrj2XOX-WX3UXp389K3NZdHDBeZBVsug8tboBkHpPmDHyuVncW1dw06wYFm2ylJduDfHTge09t7vZEqDqvgaqsAvJ-bb7SX8mreRpOcXZQbJQbfvF6KcsBXt37Hy2-QuYXzN9ZjopLK0e_eAeiP87wJjsHJgeBcXPHItVwt2rQsaxikEf9JaqXAXKwQHMfz08WRENjLgqVPLmNnG0p_rtlR2hvu9RHg9eK6Fb5ukYV0Vu0p06gmDu9IxvJeJlc60ReEUk3d1NamX4Lig6pqKqIGJ8awQ6DSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ یه‌موضوع پیش‌پاافتاده‌ست ولی چون زیاد پرسیدین لازمه یه باردیگه‌بگیم؛ استقلال در سال 1399 و 1400 دوبار درضربات‌پنالتی پرسپولیس رو درجام‌حذفی شکست داد اما طبق قانون فیفا ضربات پنالتی صرفاً به‌معنای‌تعیین تیم صعودکننده به مرحله بعدیه و نتیجه در آن…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29048" target="_blank">📅 18:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29047">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CivBzlwqclHTT2X-4T3JUS4XNRpRAGc6Xm9C8UbAVhvuI0M1qPlDbGKX4gPGaTpdk7tdNLGWL3verqXOEy3qbW5x8hYc65Lve9mw1dMgTZkj29mCeBbtd8tmYu1wG2lysKZvY9hJt1tpkghttDdvLREp4AJTwDuq6Fm2QmcOfJ3LtplJFTgYloSI8WwQfHTUexiktHv-66USneUbIR2YT9BN0OK-UjJ2LLQL-msndLhPuCWmLX5xGUipgiCz9rVecpZYxhbP9YC-S_GZe88zbCPsBo2lgl9nhLW1vXXfNBgU1wsvOkBMXpi8uq0oIvef5xDqf2uiFqi3m0Jj3N8IqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29047" target="_blank">📅 18:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29045">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAcZBga73Parw7CKZHRkzwtG0fxv30kMBQAuaBAbYrH3n8Dca54lZSvIsKabYUcFAWZ9kWq_UhiujMI89QxPQj88KksmWY4-rreLX8f5DYPu5S7lv-lm2JbWnDL93_bXdoLPFG8_pzOKDY7kK6FMPcbSRLS7H0mBpCsrhPURuXAWrqW63dYrFJCE9MzGi3rYCU4xj5R7nWg3nzm-Gsznpiinz5kcWBXB6dg5lglUFLV1JwhRiqjYOUL8q1eyoeLcQbT5qnWXPK0Zd_liGwbMfRmSFzAC_qfFF1kVxztLeAJxxehuB6QCHF2rUZFXvGP0FvFibC0Pp_NM5PiBppyoNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656f3ff7ee.mp4?token=H0-w4zbptGKoEvCtUiZM_j6x5XDHufbtD9MnMyORTsjpCHAHfSEPKfUYmnz1Yc_yLWxoBCyQ0880XhyaElWDoA5R4pErFlXwZwx2yWR8zv2QCBZbhIHp751fL10sjx0iSHqJzhdKgQvmW51xL9uwM2-Z4z29ndzTrnqsBgI8JMcF3gtJ8Dtj2-H7qXfE6ICgwx8sM89L9AGKKJxP82BstxVty1aotyUepi0-nFQWmizQq7xNiV6vTltWJ-XAPw6-1AGDshmHxXrdJbMlm3K8jTNnkBYjEBZmrJRnGyIilHJXcr5WwUxtEM-Y5_1sa3iSVlprLy4mOZG-0XQ5-wLxIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656f3ff7ee.mp4?token=H0-w4zbptGKoEvCtUiZM_j6x5XDHufbtD9MnMyORTsjpCHAHfSEPKfUYmnz1Yc_yLWxoBCyQ0880XhyaElWDoA5R4pErFlXwZwx2yWR8zv2QCBZbhIHp751fL10sjx0iSHqJzhdKgQvmW51xL9uwM2-Z4z29ndzTrnqsBgI8JMcF3gtJ8Dtj2-H7qXfE6ICgwx8sM89L9AGKKJxP82BstxVty1aotyUepi0-nFQWmizQq7xNiV6vTltWJ-XAPw6-1AGDshmHxXrdJbMlm3K8jTNnkBYjEBZmrJRnGyIilHJXcr5WwUxtEM-Y5_1sa3iSVlprLy4mOZG-0XQ5-wLxIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زهرا گونیش ستاره تیم ملی والیبال ترکیه که بخاطر علاقه‌اش‌به‌کشورش پیشنهاد لژیونر شدن و حضور در رقابت‌های‌لیگ‌برترایتالیا رو رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29045" target="_blank">📅 18:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29044">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40fd4582cc.mp4?token=MjXeYUR5fpGvvAnqfFPy1jsn0x6D-FEbC7rzy9pFEP5o6gkt01JMSM9-449gSBBv7VDc6mNrDQ7RgyS_5j1YT37XzjvqpYoty4KGrvR795URHUztcbVrcwdOT7w8GjObVPedRZDJ-q68i8TKeSl6W8yQcXgkH0TNW2e1IuiZIobCO-nHZG98mpUblte3IVjXhrQJC4zSQ11eH8Hxb3PCmWLqP-epHr2f45gn0hvvtxyojzUSx9KpQEhFWqRQjXSRqTvhpDMI-2sbP3-O1vyv1SwO-WvG_cl0dxWFhVM7lyjW81DrqDP1LCGuRciFgoM_aaSs3of5tv1oMLr118ttpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40fd4582cc.mp4?token=MjXeYUR5fpGvvAnqfFPy1jsn0x6D-FEbC7rzy9pFEP5o6gkt01JMSM9-449gSBBv7VDc6mNrDQ7RgyS_5j1YT37XzjvqpYoty4KGrvR795URHUztcbVrcwdOT7w8GjObVPedRZDJ-q68i8TKeSl6W8yQcXgkH0TNW2e1IuiZIobCO-nHZG98mpUblte3IVjXhrQJC4zSQ11eH8Hxb3PCmWLqP-epHr2f45gn0hvvtxyojzUSx9KpQEhFWqRQjXSRqTvhpDMI-2sbP3-O1vyv1SwO-WvG_cl0dxWFhVM7lyjW81DrqDP1LCGuRciFgoM_aaSs3of5tv1oMLr118ttpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درخصوص آخرین وضعیت اوستون اورونوف در پرسپولیس‌دیروزتوضیحات‌کامل رو دادیم. در این حد بمونید مهدی‌تارتارمیخواد اونقدر نیمکت‌نشینش بکنه که خودِ اوستون اورونوف درخواست جدایی بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29044" target="_blank">📅 17:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29043">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4aFbEZIgs9Eo41S4rmMXP_ijrpUVMLRsOq0lfi0DXMk278zuMc7CL-8VddTWHkujN69YJkrUpwl0im4-FJFLu3DHzq4JA7BVwoH3lUNhiWBKc_FSuZoKaeWPWq8sQC5usMf3EoNk3T3h7s-dk7HGg-Vgfg30AdhlG6k-_9YD6aF7iH9w2Ipy-LBJrHF1WHfEhK92lLSdKiivqUt3si_vMcFdHbukzG40FhC4lyq87PtVN6buck7qO2Kg7s3WtJdXJcUrPbRPn_mq65fCM2VY2wG0TwHvrCf5U50467CLmTTp4mpi7k3iYXPEgjnRIUHFS0wHAstst9vnSkPuamKKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نظرسازمان‌لیگ‌عوض شد؛ دیدارهای هفته هفتم لیگ برتر براساس تاریخ قبلی در روزهای 19 و 20 و 21 شهریورماه برگزار خواهد شد. پیش‌تر اعلام شده بود به‌خاطر بازی‌های آسیایی تیم امید دیدارهای این هفته رقابت های لیگ برتر به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29043" target="_blank">📅 16:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29042">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔵
👤
بعداز تنبیه علیرضاکوشکی توسط کادر فنی تیم استقلال؛ سهراب‌بختیاری‌زاده سرمربی آبی‌ها این بار صالح حردانی رو به خاطر چند مورد بی انضباطی موقتا از تیم استقلال کنار گذاشته و احتمال زیاد در بازی با آلومینیوم سامان‌تورانیان فیکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29042" target="_blank">📅 16:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29041">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKylIWKh89UKS7pCeMFtKkr28-fFCki9NxwE4izwedkRoCN7MSMmKvOcVcQBNuE0WmmLF3KHDclcNyG95Ee0uXjlVI3leeza7-fLShagGr5CKpjetdbiwnpwAWJ7RdPsduOaXJjEijtril-a38Dq6YRmYFY2Yi-0T_vmdy9hM8P9menqsC3JZqzem82jlXabYLcXR97dfID1jl4xPDMHnSSViZxFKy1IwUn6lnjM8NJy-fKik90LAd5NFgBzrtmAwQdqYdWvWygVEzqGfL2SMxw3vJ5GKxk63yRbgkbOvZwJ2hO82iHyrlauMsP16msqvHbxBQIbTQ5qSne2rbRY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ دلیل ناراحتی سرمربی استقلال از علیرضا کوشکی این صحنه است که وقتی دربازی با نساجی تعویض شد با بختیاری زاده دست نداد و به حالت غرغرو رفت نشست رو نیمکت تیم استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29041" target="_blank">📅 16:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29040">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ur3Bmk6CKtI6mebh5-zH3dDGxFk0aQvL3YHiLOnfxbxT4TW6uFGnhZ6EamhUIEzE_FLd-FGHwopy4pZCQFD3w44KndDSHScQStWfrzuxtkF5sZlilDdv6M-4P0phgllHdRqDj6Y1G3tiuJe5hbpFu4lr26Y7DpOgPM_XXvEDOc-2_-wUlh2DRyvXvLpYSnmfogL9n0GIdRtmKFiSts6pt_rWxXEgGhYVyLVVzK8WIcnGk9QPjnILu3-yg9Ab55aqqxcWd3Yhj6VufcoxN_cLKnbx64h-gRKdpptU2M5tq7ozagxHKYa8GAqhHrvsKB1-ehy7YJdPQ77AiH5O6Q77Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای هفته ششم رقابت های لیگ برتر؛ بازیایه‌هفته‌بخاطربازی‌های تیم امید به تعویق میفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/29040" target="_blank">📅 16:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29039">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fa8ecb976.mp4?token=MP9jt5SqBgW3m0J_GHFOk0ZZbHyityri-N6f__648WuhqZvrxUJss4ahYzxAfeg0p7IQWniUr4L1XLYVZnR2yJBFqWk3hOVgN9gzSJ29OKUWlUNU7d-cZ74tyvgkgjq3DyJJ2OjWteQOBWfiJq1iHR9l98s8i2JP8xK6K9iQpgfAb02X1rZFDOG8lvOcKkw0of09icWms1XMzeCBv5AC4HLWBY5orKZ2JWT6ktFxtQj7NeHxIFfLf1ALfEbBtxsWdkYIoCDvtDL9Jj0Sg3IW10-0K1_cyViOHvEoJ0hwjNDL3MHfz_wwpYffq-4LbiwajWh55x73z61er1zf84__iFjeYHBCs7qRiveIh2CXljUtwmO7DcBkCwZTIlXF9E6ZX9zMEB875AzfLo5aINTP22oN80Tm9CY99UmaHntM-JhId4sqtgIqlBUXuG8BqpL2QqZ6tm91fJVXp1JufvzRBVW3RZ_MAzfQSzZGSF5VoY0xr99Lqb5SeFO4YclteLGdyx0q5nazj3zBOJf6d2hpm4fv-_G_M5hGFW-TSKSstaeBKgcv50lV2Ya43f3hAT_rfWqQtEvEdd2i9lDCPZmpLSBPhvlY0XRi4wXrF6vm4nZra1wjK4o_dB6VIdzjBoEBNC6mCWAcEwCk6IJ4vObxcKl_pdUXlyX1xWLSI2gzhYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fa8ecb976.mp4?token=MP9jt5SqBgW3m0J_GHFOk0ZZbHyityri-N6f__648WuhqZvrxUJss4ahYzxAfeg0p7IQWniUr4L1XLYVZnR2yJBFqWk3hOVgN9gzSJ29OKUWlUNU7d-cZ74tyvgkgjq3DyJJ2OjWteQOBWfiJq1iHR9l98s8i2JP8xK6K9iQpgfAb02X1rZFDOG8lvOcKkw0of09icWms1XMzeCBv5AC4HLWBY5orKZ2JWT6ktFxtQj7NeHxIFfLf1ALfEbBtxsWdkYIoCDvtDL9Jj0Sg3IW10-0K1_cyViOHvEoJ0hwjNDL3MHfz_wwpYffq-4LbiwajWh55x73z61er1zf84__iFjeYHBCs7qRiveIh2CXljUtwmO7DcBkCwZTIlXF9E6ZX9zMEB875AzfLo5aINTP22oN80Tm9CY99UmaHntM-JhId4sqtgIqlBUXuG8BqpL2QqZ6tm91fJVXp1JufvzRBVW3RZ_MAzfQSzZGSF5VoY0xr99Lqb5SeFO4YclteLGdyx0q5nazj3zBOJf6d2hpm4fv-_G_M5hGFW-TSKSstaeBKgcv50lV2Ya43f3hAT_rfWqQtEvEdd2i9lDCPZmpLSBPhvlY0XRi4wXrF6vm4nZra1wjK4o_dB6VIdzjBoEBNC6mCWAcEwCk6IJ4vObxcKl_pdUXlyX1xWLSI2gzhYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نکات‌طلایی‌درباره‌قطعات‌مهم‌خودرو؛
این پست رو یجایی سیو کنید، رعایت کنید که هزینه الکی رو دستتون نشینه و برای دوستانتون هم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29039" target="_blank">📅 15:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29038">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQ3IX-Gq_tj59sRJfLYZ4ZEJ5C4_EACxBSl1ORhLBWnwmpM4RLgDaEQrI6_cGjdngdsfm3gzlAJIJ_aik5TrrzXUd3GKQFVbGk32FVrCBJ-eNEIW8ovlx4fL9_DsInZwIA3HNUg_2jqaveknJIskJuv9JOBGUBQRh0_Zv3hw7VAvfeD-fdyS1reMhQ88DkB2yYfP8Ji_Vl8aRmYISJkiMRhYLqRZmz__ezdz9ifx9uFI2Nv8Hk_Uz6yQq5P2gPygA5TR3MWqkaL5OI1UHmHMVgN869gKmRn5mVzhJ0_dS9kKcPV1d9wBZifKzNja1hm0MnYj-UR-6SiLyq7wfjDJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس قرارداد زینب عباس‌ پور مدافع میانی جوان تیم بانوان خود را تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29038" target="_blank">📅 15:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29036">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEaTzOB0VHCXqE4vPzOiRuHhqOz_sF3OGf7Y-4Nm6ahmC9fYQ8nWzHrLfUkM25gdmsFqj6JdscYZSzPBszyO_xD7XDaZ27qyc3M1P6OsPtkBseH04YAfn_cN3KFt2uwNZBEFPM2lvtpi6IZoK0qwkCg0RWYN_NqvDRfSh__ZqOoFTfv5pd0e83qLEDF38E5vrxMMZQhloD1gtUiR-fPk9NbZYHXM_ahDXMqqtpidPLXSISJnH4P-ikILgRrFF6HWl2nn_itFOY2xrAfe54vtKzHbdItPnwNd7VEH1GuIQA2whfOvccruDlNZDvLWwICe0_xHSrhCpTCS28xnGWHT4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vztam1vXcVEceGe05Jvq2-Ea2dbss5v5d1oSVMXqDJ-xaTHbLazLg8pJ3CjRf8JIeTbkGKZTpMMp-KJZL3JoEmgg7NkoE_KPDu5DoqpzrSF7M5w0GeZ2iPgldcUwLbNiaxf9S18jhbnvAkrpUfV3g6uQMWw9ISKAf5aT9fyjaGFEPCXQFAbu5UN--QoBihPmWXA7xNUu2VsAHzWQme_LdXCWaMwiSoh0X-rRYB0nf19vhK5_G10ZJ7Mq6cjPSBsniObWg-oZJrSuSRtyRA2Mx5yGWiKshWYG5s50xiiy8r_ZbIr8V-AcpIjC89cR-UitMXoh-u887xJqOSfDh2wC1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوستاره‌‌جوان‌تیم‌ملی‌والیبال و فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29036" target="_blank">📅 14:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29035">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75386b7e5a.mp4?token=oS-UlZnyWjAWuoX3Xgo6KKTMMI0ThoLQV1l1gbQEzoKv_kHNUOU9vr5_-gfW5tBMI7jPBeP1Dh_cPxNvJc5cmabtB7yXcyhjWgQMyRQkQZFAUlSZPmkPefIjIgP2igvhOzQcdPWYfNoKHY5gwvk-1_wfR6PqVuu65cnFipKvXi1rDKiyUxJQE6AWdJVFdw2Hy8Mco4JjjhQsAEbt1GPcvyFSlpbmDxzIAZWTq3K-raMDdOerDdMqm_slxChOk2TtY2TYZSmHoVPxazhgP8f3EUX5njjwIiTW7lK0bj3KCjxvvY6k-px0vi5dx07rvv3I99cWBmERhoOKOc73B1jjQ7SbjR5dlu6iUyzJwu5JuhFv5gIcJjiyJKl3hRbazFmYpW-lcDKIM_rWcGP82kxFruWyoQ3EUnHagCtjV0EIsDzJK-pY2qh61K8LQA31Q53idjfg-Zn8BnuY5xgMGo0F8U6tHnAdHamxD7TP7kefLHO0FTK1EHNqj5jDdIG7WdpQXkdV2UTGJRT9dCIK05ZciOQb9bfyPnDrAKzMxsJP7k55ZAODVGjUh_gUD10vR5fu_Fd7qCvngW_i2ISyp5Bg8IfBiOCT3ZfLbWFBpF8eTVMNrOH3XJsYH6UqN-UmMp-EVH0_prWEgKn5J_dE_e4kOUc8_-FOAWQRbOBXTJUl-Uc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75386b7e5a.mp4?token=oS-UlZnyWjAWuoX3Xgo6KKTMMI0ThoLQV1l1gbQEzoKv_kHNUOU9vr5_-gfW5tBMI7jPBeP1Dh_cPxNvJc5cmabtB7yXcyhjWgQMyRQkQZFAUlSZPmkPefIjIgP2igvhOzQcdPWYfNoKHY5gwvk-1_wfR6PqVuu65cnFipKvXi1rDKiyUxJQE6AWdJVFdw2Hy8Mco4JjjhQsAEbt1GPcvyFSlpbmDxzIAZWTq3K-raMDdOerDdMqm_slxChOk2TtY2TYZSmHoVPxazhgP8f3EUX5njjwIiTW7lK0bj3KCjxvvY6k-px0vi5dx07rvv3I99cWBmERhoOKOc73B1jjQ7SbjR5dlu6iUyzJwu5JuhFv5gIcJjiyJKl3hRbazFmYpW-lcDKIM_rWcGP82kxFruWyoQ3EUnHagCtjV0EIsDzJK-pY2qh61K8LQA31Q53idjfg-Zn8BnuY5xgMGo0F8U6tHnAdHamxD7TP7kefLHO0FTK1EHNqj5jDdIG7WdpQXkdV2UTGJRT9dCIK05ZciOQb9bfyPnDrAKzMxsJP7k55ZAODVGjUh_gUD10vR5fu_Fd7qCvngW_i2ISyp5Bg8IfBiOCT3ZfLbWFBpF8eTVMNrOH3XJsYH6UqN-UmMp-EVH0_prWEgKn5J_dE_e4kOUc8_-FOAWQRbOBXTJUl-Uc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لبخونی‌صحنه‌جنجالی شهرآورد 107 پایتخت؛
کاپیتان تیم پرسپولیس غیر مستقیم به سامان فلاح میگه من کاری میکنم به تیم ملی دعوت نشی‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29035" target="_blank">📅 14:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29033">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxvDEhwuJ2xqd8LP-2aY-yv1wm0bayFgghzLk28T7aJxnuTd4lgIufhGpiXU7W-LdfjepBKCooCBdcvQfF022BLC4KWhYTWT-dlSqByNXKBqgEfopuLmVoI7P2uvY8V88Vkq4gEGEXGX1eVO32gbDZYVN_MHzBC4BtlxvKxtD7ZtAwHCoj1afopOKteBGikK4SrIiOIH2gXd5XeHTI4b6bDZ11RY9X8CysYe_Q_yhG3yDCa_V5zAkk6Tpcz6TM0D0_KWYz1ja-2VDa6BljsHEl2GNxEDMGnmv5V4adbDfmIz3yPWTXha0gTof4fuGuMyhDph3Nwlx9Aq9oBiVjGQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ez_Ouphhpou9x0kFkZPGlrkpjAPF_FKBFxsz-i1KaAqhIB2uUl2vhtHdKxj5Rh4AkDr7bJ-wXU4blMqkbn2EDdBh1MrP85gFmOe8OVmvd-htP-T-ugEC-pB2CWuWTqprwWXvl1AAlKwoEi7uu42e4dNnE3X6exvY5x1jhuYLX_Gmc0TLesWsO7F4867pb9jV_RrJw5VSJMOf4O-AZW_eGtlSRVC5pK118ISVF5llA1hm9yTeKhYAeQ_DpKen4hCNr-mjCvyoS7hlwflsKhnbwTRZNJseEsNvJjCi_VsDMjmcAEBlQ_390VpBpxLbd8CcwRlN8wJ05IfauZFGFpRa6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب تیم منتخب بهترین نقل و انتقالات لالیگا و لیگ‌جزیره در این‌پنجره؛ باهم اگه بازی کنند بنظرتون کدوم ترکیب خفن‌تره و میبره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29033" target="_blank">📅 13:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29032">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQmIdO92uYLj5AL3HmACFZn6Au45GvQfJsm0uPsgFZu29o8Q8XlAiKj_f1GlvvlIHc1TzELNOkNQ8F0Tqk-beCUgbUKHl7G-wp63GcEx1W-AzdbrgPrFm-qvyuOe_hQrNsaZLUQtcdAPufwwgnMM0Jh_QGB7RMplxxNCT2T68o6mjMQ8xAnRxWrcZq24UXZGxHBtzpFwIQaqAmnlFWSDLyuy9dGWz30EMswx2oyLHQF6fTmXPSF4_8UimOC7uaoKImizudr_chHkOCLOVG7YdZXK9_exMM52WS6e7OhMsp2EW28-4ORGO47o1cmiDdIckVF1u-x02YEOn6C3YcqDsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
دیگو سیمئونه سرمربی‌‌اتلتیکو مادرید:
3 بار درآستانه گرفتن کاپ‌قهرمانی چمپیونزلیگ پیش رفتم اما هربار کریس رونالدو اونارو از من گرفت. قطعا اگه رونالدو نمیبود من الان سه قهرمانی UCL داشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29032" target="_blank">📅 13:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29031">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/989a5b2f6a.mp4?token=Q7MsoIK32bL4HXbZy-FBmEEuyOgR_HeIUPG3TI0Ec0OgvZNf-3HJgZruI_At6-UldJR-OjZXExOwCjlnKA5cDwlHF7l_j0ZSIBUEHyUfQjXrKK8Nyc9Zv2yZZxazcMuFNgDzofZqFVPu3Gkr---zryuyq_w4YnUIGq59qbfFW2CXzmyD0mRNQYzvqGjCgw4Mwttg5tlE84HNzCMHGWGuDRGyjALS9zInM_CZTsU1SxuSvMpOGQ88eQk_r_V8ud4dasiAfMVKbnGcDrqCC2q8ISXDsBeWztjHVgwq_EZuXNBoNV8OxhuQJeHYlCkNEJxMdLvw3lLgMy-X1R8uz0F9BTUj1BqloBMQR70FnpbpQqgXbzrbIQtIrwIZUVWUI9gVtMIs5uoK9DgBf3aDbaBUFxTVVb69PNDvJtjc5PXy27MvRU5u1o5BYOk6OMsVZpDixK4UMRan68W4_e0dKUr0IClKjQQeCH_w91zWUvMs4h1dx2z1fbcYHptgmIvSdKXWE7wqKPkWD6lGF0mxPjoHebHXny8zVCvZeqLztCZ_fL6i3_muBurPGPb1WKLbGFEbStCHNoNGQzUslkN83-2Wvy-gzBmU0npUcPL7LBnBa7OHtpV32ba01nvWHfOipsdkYsWikNCuyWs7QfFeA75eINceojJCcSRWNzbmvqmh9aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/989a5b2f6a.mp4?token=Q7MsoIK32bL4HXbZy-FBmEEuyOgR_HeIUPG3TI0Ec0OgvZNf-3HJgZruI_At6-UldJR-OjZXExOwCjlnKA5cDwlHF7l_j0ZSIBUEHyUfQjXrKK8Nyc9Zv2yZZxazcMuFNgDzofZqFVPu3Gkr---zryuyq_w4YnUIGq59qbfFW2CXzmyD0mRNQYzvqGjCgw4Mwttg5tlE84HNzCMHGWGuDRGyjALS9zInM_CZTsU1SxuSvMpOGQ88eQk_r_V8ud4dasiAfMVKbnGcDrqCC2q8ISXDsBeWztjHVgwq_EZuXNBoNV8OxhuQJeHYlCkNEJxMdLvw3lLgMy-X1R8uz0F9BTUj1BqloBMQR70FnpbpQqgXbzrbIQtIrwIZUVWUI9gVtMIs5uoK9DgBf3aDbaBUFxTVVb69PNDvJtjc5PXy27MvRU5u1o5BYOk6OMsVZpDixK4UMRan68W4_e0dKUr0IClKjQQeCH_w91zWUvMs4h1dx2z1fbcYHptgmIvSdKXWE7wqKPkWD6lGF0mxPjoHebHXny8zVCvZeqLztCZ_fL6i3_muBurPGPb1WKLbGFEbStCHNoNGQzUslkN83-2Wvy-gzBmU0npUcPL7LBnBa7OHtpV32ba01nvWHfOipsdkYsWikNCuyWs7QfFeA75eINceojJCcSRWNzbmvqmh9aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29031" target="_blank">📅 13:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29029">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXvMaQOP6wEYEaRzLb6Z4rPkvwETA7v29xD3UO93mkicWmjSdflWbaVmZLfDlyj6H5C2S2inIqbA87RPPk31VRjQUCHH8SKfu9pegWE8eoprb_BrURcfc3tr62x29XG_2Cm-jHlE6RAgXRoL3QVtY2hxfH0BB--bNTipTmnn6aFPIK4--B8SvzvdT-5p5W6P6wMABPJsdDj_Iu0wKLuzECO9C3Cw_uIOcwhcu5pU-tBLOir_hGqegjJzovcVFmEWs-RHCq8r88ruEZ5wGuq8gT905o-AcVKEJ_6tiLkzBbA5sVwOmVl2xT87GlmcrH3ZVQJvwlyd67Lv7DUKlycvmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
نشریه ESPN: احتمال اینکه لیونل مسی و لوئیز سوارز درپایان‌فصل‌جاری رقابت‌های‌لیگ MLS ازدنیای‌ فوتبال‌ خداحافظی کنند بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29029" target="_blank">📅 13:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29027">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P271S5EoRlksWzxfGhrCI6tbm-wmPyye1v48a_ekG2eF1RGxU0hAzXDsU3I-PqFzQCKptVUmTIPWvb9qHhX3vPhHu_3RzHspLYs67axPnc_to8y8aGsIaoOaThmKGFwWeXMgOfkPaq88fvkm_xMckKY4WapMAcy5vyf4EHwRB-asEeZTDbCqlzKiZsrjJnMuSRzN0JAuzKEJWDLsa-MyTKajojysKcpPBjVSD89rbrS1dfNqLqIFga6eieeUNABIfikUOrdE5DdRXkiLmb_mA6tBIBRu1tdq233RPKcL6dCiLBhf5EobfdWetUGyPL1LrgffqB43j7xv7OD2jvApjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ItugbFqMBCsYe4mtXLifsYnwQzrtoq4QcXo-daz2JgTSOMjRLbZZENH5rZKR_yw0Fwb_644SaZHXfM4u_Gmg4eddWiVAkRxcvidwNRs39iedbBAobpdBuGeQNBXnTcZ2_6PJ0SKs9u9EK_7c4NbdMLMe4tc0KMPCZdOd2AZKyEt59eF5Cf9-szscWPwtgH7lcxT81mUC7Vm2J8FFPLNhZCjxbeTL_VQJl-pm4WQRr5Yk2lyJthecUgS9cLBZo5iLWjL3EhoYueK_k9IFSJPPFqUr5Kl3Scx0W5I-bh34AxRI4ILB_2RtP7x55yqVi5AVCJJumuaVhsjIZ2ayp-qWgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب تیم منتخب بهترین نقل و انتقالات لالیگا و لیگ‌جزیره در این‌پنجره؛ باهم اگه بازی کنند بنظرتون کدوم ترکیب خفن‌تره و میبره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29027" target="_blank">📅 13:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29026">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2LyOiq2Z2QTuo36uSum5C5oeZe7Gc_2E0cjO0PRv-Vj5Z2fp2sDlsng8VHifGYwm9e2D7q4q0sUOadmtV9-KuGhDSh4SfEw7P7zf62dfgAjfCAiPmg7hN1Mv1HcksaWruuNADuCiH5Emm6m6PtKuqB1RYcthuMxqMn5z052R1xNC6jLTfpV5B2Cd53scRn6-1gsA9P_1B2iplPozSDwQ99FTExjqw9LBirFzcophwOV5uZPegMMjTt2liSR1UMADhxceJu5qFiDFYdlFRbe_iAi_e6x9x8Y-gVRVSxAwSeOGtfr_DvleM9tHT9AcS_7WbuQFUA_Ahzz86Sc2x7XuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سمیه‌اسماعیلی‌ستاره‌کُردستانی ملوان با عقد قرار دادی دوساله رسما به تیم بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29026" target="_blank">📅 12:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29025">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ywb51s5hAPRfHiR4lvYewtj-2xnkNrvcOuXoKZLdL6guQ5lPKGehJE460C_4mO1YT3K6iABy6Atu5DMytY9QPDOSq0D1V4LOpDB9gTIx_OcsfjbarZop-kuDOdkyktKEONDtjH4C7VvGzkLL_mXbPm6h3KlgLTDdsSmLZoWsRG7QqOuJcYZ0ImmY1vfMyco4kYMmfsulH515w8ACg_zSu-quURjAaBd6EWittkrV9QdHYmWWfF8ENOZey8VB8rlfxB8CHaf4oNS6PBS9Na9YPqQx8SLk7yAIrbtUR7guacPzxk2G4UZSH7BcYQTo7VPCtbCcr0i7DJ7-EOR2EMG94Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29025" target="_blank">📅 12:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29024">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQBDVwXtDQbcee7MpVp9vf3zCBzjnSmvq0SQ1EIyNb_nTnUTCkkM9liffFq3Nyhd9RDpz90eSwjWxcgUAbzrWctD2UY9BuF-iHDwlztcKiPWZQcD12dBwVfUUtZzNxuyPZjawA9zsh5kIlLakAWRXiEyRhNd_JgKJMj7phwvk1FJtU-wbNJ4FFn3ZQOBYRZOewVV5UZan5efiE8JUY4HpWEkYiVmfuOP9w_JY2cbG5SnajjLvaywSmyheXxizTuZogFXmPDBge2Z02VIyf-322bZbxxjP4GBUx6YbUSCEq-sFV2PHuv9EEGpo17QrWvZgbZ-ZMFAaqt-9yQNObcUkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه‌نفری‌که ثابت کردند که هیچوقت برای شروع دیر نیست با حضور علی‌آقای دایی از ایران؛ اسطوره دوست داشتنی مردم ایران فوتبالش‌رو از 23 سالگی شروع کرد. ماهی رو هر وقت از آب بگیری تازست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29024" target="_blank">📅 11:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29023">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ebccea1a.mp4?token=SOqdNmgXqGEHWnf9K2RITO5lXz-z-RPON2aMrF7eYxJ08I5p2PRWdk4DiktVHWSyqlVIq9SUS2tzMVPVLK5W8MVSa-E_IZ40ZsEiur-ygPF_n8sCuEPbOVBlM8hxqWI6LC6ak97lQ5veoKOJpUkmQv_aYuCx5osWj5cb3VoLiuqAd1h1FPNN0OeMGDVeHhwyefOJvs9IBk0zlZrXz0DJlx0ci0bctu-W6_Z1vh0wJmmHowNvvx_AlmAveGOuU0dCFrypdwpb6MOB_RW6Y3aIqkabP-sm8c9-h-ccwafDg35mx9dIOJlfTQXg6vAGXsHgUi3kpo-dzbnkMyrGRrcQuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ebccea1a.mp4?token=SOqdNmgXqGEHWnf9K2RITO5lXz-z-RPON2aMrF7eYxJ08I5p2PRWdk4DiktVHWSyqlVIq9SUS2tzMVPVLK5W8MVSa-E_IZ40ZsEiur-ygPF_n8sCuEPbOVBlM8hxqWI6LC6ak97lQ5veoKOJpUkmQv_aYuCx5osWj5cb3VoLiuqAd1h1FPNN0OeMGDVeHhwyefOJvs9IBk0zlZrXz0DJlx0ci0bctu-W6_Z1vh0wJmmHowNvvx_AlmAveGOuU0dCFrypdwpb6MOB_RW6Y3aIqkabP-sm8c9-h-ccwafDg35mx9dIOJlfTQXg6vAGXsHgUi3kpo-dzbnkMyrGRrcQuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/29023" target="_blank">📅 11:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29022">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">▶️
تمامی گل‌های هفته پنجم رقابت های لیگ برتر؛
دیدار هفته‌ششم مسابقات از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29022" target="_blank">📅 10:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29021">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCB-yrmZDXR_BcHJQKL6J5WqYn3WinzIjzeLTorZU_rCyZoYG41KE9vESQXhyj7kI0WE8_qhw0PZ1RzyVttWBa35-Lx28inUGEN8GBFIQkWpD6RRg8xVSohKTW_sIkslVlfRqQzk5shv6oNp5qFdfgQXnxhNuZsxM95F16nU29PAf_h50EUPBLVpl8q5pWlqejXe9adu0xTHlIrRJ1RBepI0yvn3uopPQFJPvFQAnGK-nMpuNX6LhtPxzPorIehmBrtfqTW8qPxNviRvulJ6cL-xtJxznV44En90IpYKZkhz2Sq9O1oxK_gtUO7OvXeYotDAqkI7F2o9TwY1_R4GHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های ما؛ باشگاه استقلال در نیم فصل تموم تلاشش روبکارمیبره تا رضایت نامه مهدی قایدی رو از النصربگیره و این‌بازیکن‌رو به استقلال برگردونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/29021" target="_blank">📅 10:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29019">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pg1gHI2wgAP0JpTLC2p7eMZRY40vQvXeki-_ejDYmsutKTAv8Pb35bjFAP4wt8nOXej_30b5OK1KjoAi6pwCG46sUguiiaLz0pLVShk8fR2odHL23O4I5JwK1tH6tDgo1dKYPNKQsEpDJXi7jijTtq3drGOCpowwJOA-B8AvpdayTtszI9Y7J5qvvUcpeo9SDztADpdB9Tadqi90h3T3MeFxVRFkZPMM5AK-ibjBRuQgds6Sfu485n38z4g1AsiUELp5N3wMwMEQbM4pWqLVKqx3gQJOgfF-354sLzR19gS8SScF0CGozjk9hxUPtFHN_DhV6qT8gbXn7hAXqI_Zzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AHrKTM-7XYrBH3uFqw3hH4MzK4VhDI45lvay5gfrlI0Xb-Q-BDAWk0J5Hp6P6lHWzlZebEbQ5rx6GwRHMvs10O3kqdQO3Cyob8zGmrP7ZmiI2koI0GFpM1XVah5VYa45UOESjJiK3hZCUfoQJm9W42FWFb0H96oCQhHhkMZyzVFgBeti-STy4Vk0DkTHunnrM5kF0GG-JDU_GGP-d12dBSM9eDbIo4MV6ETF0fee8_oTtbD1hXcjfdQrpakSm4sMTvdbOkve2eb7xgMuLz1getvuw6K3fAtHROO-g4qgPDEYYCyAVqHxEaNe3o1LfRe-FyphFxXT1045vsVnMCEbEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوستاره‌‌جوان‌تیم‌ملی‌والیبال و فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/29019" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29018">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiXQKlBB_05UKo-bLpsKjmR4v0nppks5E53JeyJLFYZcbIyyY6DfNmerJpBy-gWqNr8tyoY_UZqAEoJx53HqYptg23Vj-IFHDTWXpGdEiOeLZoo5oQ7kDRO-eOFZ4oogRm0HwltWHksNTV4ypUZdc5-7TzR-bXBlJtW-uNhjkecswI3Sa_3m8yGZqgXhOw0bxvfceL7wrZI1npwJR5gFI8Hl39FiecQCQQpK87kW81AHdfCSMSmj1jVMXjxTwVDPvlitDaEH4zbls5li1mv8yvYqQ9vJHZ-gMGtpccFN7MMsgs8BleMFsgiVzsfR0LH2avsdRAnCsgl4A95WRpQnTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیزری‌جدید‌وجنجالی‌ازسریال«مردسه‌هزار‌چهره» باکارگردانی مهران مدیری. مدیری درنقس عراقچی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/29018" target="_blank">📅 09:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29017">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfgI-PCuYYxY5zHl1V5gaik7m7jz7FvvfNWDMLTrituuM77VigHr89CO9Vi_mqH-qFbwOkoyCxBpr3wLrskmbpXC6VKObUP2Krpal6-2_cEjQIkcaRcMAUVR6EkdEX8h1M8iRXahijIw4Ck9_pZuy5tWiISfg4IHrRIgcqo45suSlnQeL1cQcgz8T-ygo6P-RJyeJBWkK-qTiFyG0tGdPOhkv9NxtDVwFdnYuiqwLUM8MbDvCbjXF2e67y4UwjZF9pkHH_xY6xccexoXrzPQ8_AaTX16lEGS6qyTerSGrZ6l2JI7uVKDAX91gNoaZ1a_xpN5rQ0AdR0JcDAgOpt-XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
گابریل مارتینلی و همسرش بعدِعقد قرارداد رسمی با باشگاه الهلال عربستان؛ مارتینلی در الهلال سالانه 22 میلیون یورو دستمزد دریافت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29017" target="_blank">📅 09:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29016">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVilKjxf-WZ20CPkJ4OQJD_WNXjmawBvrF_t8gOOpdTlOeVRY89vTyde3BtFMPYeWR6wE3tnMLwxgQ2Z_8WRyWxXrWBwZUF-U584sxPtAR8lnkB8LdqfFCmYsMkNvJHI7Qk9M8XNQfM0eQpyXGVV6F6XQJjrngesM3sUGIp6dg8BbVDw911gGZlBEWOanCKRN4LEdtcwuoIAX03cZgn-gim62TuWJ2zAFNKk40hKVvy9pxeBOeAOxvAaCBis9lrhnpKqNvixP3P_7MeL2BZkx0xRlzb-R1qTPBsI5eE53SIxIt_12lmWlybXjm3tZcbmG-2fZJB5c5Q8u2ltRo53PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لوئیس سوار: من قبلا با لئو حرف زدم و هماهنگ کردیم که با هم تو یه روز از فوتبال خداحافظی کنیم. قرارداد سوارز بااینترمیامی درپایان‌فصل تموم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29016" target="_blank">📅 09:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29015">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PF0ZflRfMkUx6f9asxHBXMf04EMGYjN3NlHZaL6lZS748Ev_VRum6FGuro6BZq1vT4cVERlR6VT-vm5wnpfclQdRFgfAfO75YAvYk-M7Xh38E1snvOwRZaFLuf5MT1Ui6TN2QXSto7be_CzJ0Ek_fdOkigmeuc0rtmdraaxFda70T5XzJfh4PLSQebpKdRzIxDfyDu8utV1U9YevGA-WQWR49bPR9IvHayMi__Z6E2fDq4OBadqv4SWJ_XfR-ErOqFFweKjLZZ4ob-9hvaecxBoIpSzN_prHp64_qXmRsqm-CPncwYE7Rc_N0ubAMEzTGKTqulHlJ_vOAvyUTKYweQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی دو تیم رئال مادرید
🆚
بارسلونا برای الکلاسیکو حساس دو تیم در روز سوم آبان ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29015" target="_blank">📅 09:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29013">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikiC0e2C4HYIFBTn3Mk7Nk0XlM6oKWdt23z4zzU9Pi2dRH63gGDH9JWGDA1KDNtGhHhGyI66YzNSveQJ2i09tgTmWtuiPnE23rtX749XJ2Bz-Re6NE7wFHuT5UVHAPWkKVZTYI3GpZBfAbUkSDMruDPsvYtfCUck4G-WYgh8o_IK0hU3k8gSoqwt9hlWE_RhMXntz-Qd38JvBuOb5aaedc5EJ4Ac5SFELsvJOUk1yn4rr8KrBOLGVKNnGkNfFgZk3v-G1uE0Hy-tzN_zYyK0YK8XdGqOozaGVWzourUH7J_tWJ9ZT_vT8iGnyNXGL-c9dVvH4FVV93ZxGnDPG-TXYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛از دوئل‌شاگردان مورینیو و پیگرینی تاجدال‌لیورپولی‌ها باتیم تازه‌وارد پریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/29013" target="_blank">📅 01:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29012">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSxYGyDO6oBUwVFutezXmdnB9eSWA_3988Z4cldENVZ0Zo7HjPNaxk9D24P45e_tuRT_vbG-P9mFw22viP3Vvrqh7cR7U7KoDLLhVhpR02AuZiT9sBXUiiiE3qp1N8WsftJujfO4KAOtbdAqomgebKn8dH8X2aI9B2W5zDPzXqhlxB0tlJSBTPD2iQzfzTHkKKTQ2CiSMyiPLnVJWICDFRSQXqe5lZxal50XYgcyT_mTHbGrCoa59_roJSRLf1zeqFIdqnbnqU10KbXQkq4pTM_n5gDuXP-dxjYL3sVPA2A60pYtuieJTeOUv77S1efYhrqlLxEh3fTlKvC-JAFeGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌ دیدارهای‌‌‌ دیروز؛
حذف یاران نیمار از جام حذفی و برد لخ‌پوزنان در حضور 64 دقیقه‌ای الهیار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29012" target="_blank">📅 01:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29011">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bfa115327.mp4?token=PLurfFDZYWhu8sCEZmOp5blfbGOddwmPpShVE2oiJQr2-VXCBSglTS4AABk2Fml5b2as18cCJOEDqxSbGWueVGnoORN8VLOXs82LBuLZPcfxj_gSWIpHoLxVHWaC7fG3495Bls1UOQt5rSKoe80t6qn9ceijIAVSxeVfdpyX7BNhdNb2Y2nq5eK956A-2lQC83WoMmWAGg2W9tPDzQsQVKno5EPNkKKB_LD3Uq7XAyCUslR23tXJ6MXMh6ciEyAjyReQwNkB87ZgeUD05hHUDGvIRSSque7UL0RJNcKdW9fNt3KujRQnPwR0xgdOGaCP487BzXVbRTvPyunQFjB-Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bfa115327.mp4?token=PLurfFDZYWhu8sCEZmOp5blfbGOddwmPpShVE2oiJQr2-VXCBSglTS4AABk2Fml5b2as18cCJOEDqxSbGWueVGnoORN8VLOXs82LBuLZPcfxj_gSWIpHoLxVHWaC7fG3495Bls1UOQt5rSKoe80t6qn9ceijIAVSxeVfdpyX7BNhdNb2Y2nq5eK956A-2lQC83WoMmWAGg2W9tPDzQsQVKno5EPNkKKB_LD3Uq7XAyCUslR23tXJ6MXMh6ciEyAjyReQwNkB87ZgeUD05hHUDGvIRSSque7UL0RJNcKdW9fNt3KujRQnPwR0xgdOGaCP487BzXVbRTvPyunQFjB-Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
ویدیویی جالب از آنالیز کامل و دقیق دو گل استقلال و پرسپولیس در شهرآورد 107 پایتخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29011" target="_blank">📅 00:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29010">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBq2ceP3WqiwndwLFrNNagf4_MJSXW2cQz00LyOv2ULyuvms_MIlrLNmWZe9QFb1_0C3yfeb9n4eUYfxTzVtkWSgvu-Rz7E-ayyBxBw19W7MMGqlPt2dizwc-1ne2QPx0MrYtGyfCyljNEzECYnne7Z_a7iO30Nu6FYYCchu_JDUUp2o4z-_fICgC0eZLwOlSWtgkr76HSOfDYaw0_V7ny7ZeZMJafOgffY9b_MX6it4I8xvINmmTvZx5uTdd0Tq1pSjR65ZNdu5xd3GIzCPQKziHOxR9YtSVdq5xgUOp8_tJD_TBGCVwTrQ1kheMHT47jRxJK0sAVx0ux978_uIjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
پاختاکور درپلی‌آف‌لیگ‌نخبگان در شب گلزنی بشار سه بر 0 الحسین رو شکست داد و راهی مرحله گروهی لیگ نخبگان آسیا شد. این تیم اخیرا مرتضی پورعلی گنجی مدافع سابق پرسپولیس رو به خدمت گرفت و با این بازیکن در آسیا حضور خواهد داشت. پورعلی گنجی به بازی امشب پاختاکوری…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/29010" target="_blank">📅 00:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29009">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5FGiltjMKQhKwTRoGbH9sUjgxoRKDU5z6tLCGyJpcQE_2ITKUaKgsPhz4pUUHjINF7CkaSo5h4cm13NCFVSlXEDax8YYR6uLhrgIVwEsjNQU2p_B3D_idWiDrLfmyChvndSyzCn1s5osDhXjTrncu1OBHQoADDj74pc5_LUxvvpHG6-ZwA8ygsd_OpRdj6FwT-RMdE_OdmKVa1agA47Azo4fHGyxYOmD2qIAxLJFqFFC-KVTlz-R0j0okCClSGS-PzEvzHWFEk8ERuM7Flyt9cplq5hNoU6jaofP2FXD-FFwZXvpMh03ipQsA4fsxhx95mEstdO1CAWXDS5Jmmv1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ روز شنبه هفته پیش رو باشگاه استقلال 70 میلیارد تومان به‌ملوان‌پرداخت خواهد کرد و با ماهان بهشتی هافبک تهاجمی 17 ساله این باشگاه قراردادی به مدت پنج سال امضا خواهد کرد. تمام توافقات بین طرفین در روزهای گذشته…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29009" target="_blank">📅 00:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29008">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikzUOM_5tcIhWbiey4_FEIsmOV4Zl3AKe3u69utBg3MRrcNLlOVRVgIg96nzujJvoSHcWRd4DTDbIzPQDgEoeHNB35T9dgbf5GqIQ0QTRf_CYMkJVDmZRGw43z9dxelvuatWw-ocIkDO_9sATWAVeZUq_5t2e1YH3GoPLX4I88zhIzFA-sg_zctypBw7wOlIdfQF90RENsGiIU831eYF9sUtEUACJYWNuu_BVYAfSPV16efe1Pt-_LK4Tfa4dY0Hsnm2aQphBJYWaS0MJBeWKxNJY7zbkfIuX-vGEUh44Sfvnja_sjxfHMBLucW4QaEGriyCbQRYyjtBlYGkAv_dbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
مجری‌ویژه‌برنامه‌چمپیونزلیگ شبکه TRT SPOR؛ که گفته امسال بارسا با فلیک قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/29008" target="_blank">📅 23:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29007">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEMI8Xo5YIKWBZnsvpJYRKEmsBR-drxWJOs2RQrVJZUTx1fmbpkvaX9sscQtAE5oDyEoIzDixHLrKKjC_-f3itiHStf1946X_prLbR60Ahf1IL_X2EnjnI0P7phOG6_BOx_gZpv6bb5D7a9__843hgh9IzfFSA7nb807ktNPXhtocxtKnWTnYUFUtxNnB1fTvZK2rRMmoNa6tWeqZjJkjm88d-DmjBCA7Rbsov81YvVGKNXWEKVUE_zmG-VLLwi6eyPDl131RaYX6yIo4y9qqnB9iDSxgjHWKjduDgt1RSsz1jAfAz7FYFJT-ddQXxTf7EAndMsoQjAsG7f9NaalFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
بااعلام باشگاه بارسلونا برای نخستین بار در تاریخ خود به درآمدی معادل یک میلیارد یورو دست یافت. این میزان درآمد عمدتاً به دلیل افزایش درآمد حاصل از استادیوم است، باوجود اینکه تیم بارسلونا مجبور شده است تعدادی از بازی‌ها را در استادیوم یوهان کرایف و با ظرفیت کمتر برگزار کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/29007" target="_blank">📅 23:30 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
