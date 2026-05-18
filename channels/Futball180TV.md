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
<img src="https://cdn4.telesco.pe/file/Een9M89h075l2uT2fEb4VfdGRLFTwopz-4TyYCNJh3rKeN_NK87iucyNujJ7NqWjhdAewBAuF_BeaM9DYMGeVMSvOzgg8RdTl3USe8T-yieHOGGFGQ6YezKM-F3vgQPG7w5i25PA86Yavt3dJOgcCo0BmGey_XNEd-DO1rhcCau8J9Qty6aoR98MArrDptD0NXWDtplXFAXaCTc3LNE-Q5v5F2DkLJfU4WHeXv_4GIq91hcxuWFT5rBx3yInBrrK46v-gp9t4dc5uNvOPZj18KXcr4w7XuclLrfAhRS-BrXkV2mgpo7oLM31yoBwl4QPjTugIS9gLooqtzXB2gKyVw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 133K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 17:08:29</div>
<hr>

<div class="tg-post" id="msg-90039">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8MoObGq9MKvi3fQlaBt8vRQjjojVJ1auP2a-6Z_8zg3W2GqrBDAKWuohXqA28-Z3bFPn1kunU2ocGBWLsHkJRdQo2VDkshiNfW7V26Ezf-SfLuKHPX11fQvYbOvtKdS210eQ6Ue8lKzAxYUKIKvY8QT8Ub886cU5nLk1uBVHVT7fm8GrPAjKFsPXmdpe8oTZLQ8dFtTLMmslEcvpsyTlKRzqkpgqU4U86VefttEZ7ArcmARBDB-t4uWWfCjQhBNIq26PW3eX4P4f0JKHVzNrdS_y2wu6iNS87ame0gdL0GE1X9t-T7nqZFyNoU46-bsgZaRWpgrmmd3mKN7qZ2jXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
لیست تیم ملی کرواسی برای جام جهانی 2026 و پنجمین حضور متوالی لوکا مودریچ در جام های جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 793 · <a href="https://t.me/Futball180TV/90039" target="_blank">📅 16:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90038">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUo-HomXzjbnxHWjPHIqlEDUC-TumDdaKIOj2Ku2W1-b7SxEOhLKoxyIunFMHGW9kgBxC2NIc7-XgLcvfK56qkfSWngkGTApmJl-YID3D80oUw_mCuGsN6qT9UBNB4ocLyUwea-BfyCb_UB5bBqtQS5jgixnF6p7Uplw-qBgulzWyhQ6ZyWO5VMIAoju1ZVRhvVd0E7kZR6RCHXmR6-duOFFvWnGyHZwu01bxAPlX6TJ0vT9eg39gAJW_9Wsh9YtnV_-pNWjN-a9nDeZKuw5I70wjIcx_mIYPyCYL8S1xm4xZJ9LQ0nQ3aKZSyZVcBjJiDHy1yYpPgyhn9TNgxY63g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رسمی: هانسی فلیک تا ۲۰۲۸ تمدید کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 802 · <a href="https://t.me/Futball180TV/90038" target="_blank">📅 16:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90037">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b5E64H_YE_QolnQINmNyqlCEImP5zN46qPC2IMCayerN-XtyOPTfIM-0X_RbPLSPLJgR7pk4nooVym3scgyMX2cbKyAJhOiTJmSmqdPx5A9vlHarPJhkCQ_3d3kQX-yjDhwOZ9A0yja5_q100z2gPZHpYVUyKsTJGcZK8E1bOIw5_QfuqYe0tjCM2n9zWxlZj5voDhZdxAh-JDcEx4L9qDl6B_A-iiEKQPvXCVwOEMMPPTLC_ifDxF_YaUBzOQfm6_QoQUWptNPO8ye2tSqLV38UEjPVAr-qOJoQEqOkaf74th9mlFOB0w-aQHi-klvkEaAV5GwG3j7abrsKny812Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسمی: کارواخال از رئال مادرید خداحافظی کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 799 · <a href="https://t.me/Futball180TV/90037" target="_blank">📅 16:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90036">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryPaqB1dj8KtuqUko16nj2IkcwBH98cHe8W1uBFLDwDHWG9ZzprqcgeSLvJXHxG3KMjMzz9enBuq87EPjEXLkNRgzfHDaB1p5CkGOYDc978pO_E4E8MCy38MrTYalrFYe4d23h16d6WKXaG_D9EhN2MELqCoGzJwMX_91tZmwyPVfeSMjeOq_B3ox-3Jk83sVlnkHrwruhKiOH4owYmVn3OIM4zqZMc7GL0n_FA-KvIViQVuYWefDqdAioBP1vS9foqlAv2HHfbPUo1Fexgw7smvRoc6YWmfHN9_bgX6VT41iZN-vYKcUNM4RD8y-Oz0RC2ETmRYnb8oOKbqNkQxXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدایای ویژه و شگفت انگیز چیتابت
🎁
۵ درصد شارژ اضافه قطعی
⚽️
بونوس خوش آمد گویی ورزشی تا ۳۰۰ درصد
💹
صدرصد پاداش خوش آمد گویی انفجار و کراش
✅
ورود به سایت و دریافت هدایای ویژه
📱
@cheetabet</div>
<div class="tg-footer">👁️ 794 · <a href="https://t.me/Futball180TV/90036" target="_blank">📅 16:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90035">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMgRTLqGKXHnb2SfK5rhxWfzvYhPeQ_bP98tsgVGqeUOYSaWR5MPZ637LisEgwD3kAFOWWqiC9lodv00MyoNxQJD_kmCAE7I4xa0HGi9shbi2zopcvw379C-CRp3JMUs14h2Zm9l4vtPbaDH-FMXrQ1a6G7zJubuPHdd37exZxK2eewtPyifVQtQAPlP_pePpkMOShPGe44tuvsvCU6_aXDxxDp6MqtZ0Cxm5kozKRpLLy0jWevzGSFNPkzqIYcbG3yYo1sOBN7cQY1G8dPeW5I_PBxOeDbmEUJkw0B1yg7Fh7ikKwbGbDxuTiXObj5ahb1S52LwAxwGitbgHYjwXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رکوردداران بیشترین بازی در تاریخ جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/Futball180TV/90035" target="_blank">📅 14:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90034">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afcf96866.mp4?token=HplyAZstOvwhOuKxEKNNIMQ3FsSeTB7rh7LBCjpC82DHfaouI9nK8IqJcPJM1Y-pQulLIQdxz5QmhY9pSA3T0L2oUuGyZ0TYYgsybsyokoCKJ-CfpF3cHQCaoRkZGFxneIfPhDX_dJJlzZq_Tgul-vAbvSXwQxgppk8HBomXdmtTZp3jvZG1XqHkQk1pShwcnuIpFqIx3lJkbUV8fJVIU3OJzplo8llUBe_O3J-3YIip4cz29aa4VjA4vvPynHPprGT7tCA6sSErIC7vgQC3kJMDgIjSJnET9xtj_kU_gqWoOShEI8rSKbkW3KrwyfAAkXy0zSpPgl9thbi7Jx5BKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afcf96866.mp4?token=HplyAZstOvwhOuKxEKNNIMQ3FsSeTB7rh7LBCjpC82DHfaouI9nK8IqJcPJM1Y-pQulLIQdxz5QmhY9pSA3T0L2oUuGyZ0TYYgsybsyokoCKJ-CfpF3cHQCaoRkZGFxneIfPhDX_dJJlzZq_Tgul-vAbvSXwQxgppk8HBomXdmtTZp3jvZG1XqHkQk1pShwcnuIpFqIx3lJkbUV8fJVIU3OJzplo8llUBe_O3J-3YIip4cz29aa4VjA4vvPynHPprGT7tCA6sSErIC7vgQC3kJMDgIjSJnET9xtj_kU_gqWoOShEI8rSKbkW3KrwyfAAkXy0zSpPgl9thbi7Jx5BKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
📍
Tehran
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/90034" target="_blank">📅 13:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90033">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOhv3fvRYrIDf9dBvhiQbgp2DHnG30551dWt6oaL3OD6Wlf4ftOblC6xboi98LeQdSC-S2fIanGbozBu_h5dsnFqIAmVm7eyLoF-V8qt5Ymk34xX2VMDfNu3xnEjqaDnU9vVRlqxbfmvhP_OJTrDo8glS87lQQN-6FeTi_9bOWqSBs_a-IMPl406kKA1iyFlohlHsy2IfCO6V1maf14YKrT2hdI5WuoTnRyGcvcI9O3LnCD-gcLZAv-yne8Z3_5fseOB26wjn0bcrRCgK3OtOcV6wlKV6ko4mwvLEKekEAuykfVLC5Acuy3rrmZzk8Sg4A-DoqOagHOrlhNt_HJ6kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
روبرت لواندوفسکی بعد از آخرین مسابقه‌ خود در ورزشگاه نیوکمپ، عکس نمادین اینیستا را بازسازی کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/Futball180TV/90033" target="_blank">📅 13:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90032">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90032" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/Futball180TV/90032" target="_blank">📅 13:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90031">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiuWtIcWI0HZ38KVg9YGjzw-LULvy4V5li7E5uT_wZHKFWw-en6xOBqbpfN3SsrjIhKrtAxqg4dLzC0zcTYRByaUqoAcZX2j_Y2YvHojupXYEepBntuJkFA5_Sb4Kh0rZGCIEq2Ydk_o1n2eKkbac1NwR9vxUKmqFl3MvxhIosgaz00uGtYhnsa5MPtzyuZAHjG398SSXQF_cD0rUlaKtpT763TPqqvDMhAiLwgIp01yB4fHGheCgmOeBFpup5PLn1jnc_xFC-z9OYAJfsxl01fiNYwYdM8O9-J-Q1VFM8BQGLbnzJnT6DtkGywoXnnsj7yJY2DdVpIywVDM9n6gzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی جذاب
🔵
بارسلونا - رئال بتیس
🔴
🔴
🔵
به Barça 1xFamily ملحق شو و با هر پیش بینی درآمد داشته باش!
🏆
فقط این جوایز رو ببین:
📱
آیفون 17 پرو مکس
🎮
پلی‌استیشن 5 پرو
💵
4,000€ نقد
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/Futball180TV/90031" target="_blank">📅 13:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90030">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9bd4b703.mp4?token=S73_LN59Apb6pTNztVqXO_fiFC1y0Lf1fBHS0UjnPX3kiK7BnDgc0KBnNDBEXK4X72zx95i3KeuqFnxjqYtcHkCQ1LC9Zd9XB-3qx-ygAbLMuULOllyfDMg0J2B7vVLl4oFG9NPHNk-W6acqq97ixClGrrfso_NXz-FzIwTDhtLTkBHX4v_09UOKuMoJJSuGaqsklY5V6XQrcaV9UBeMvRpvjMvOCv-94BdmZrIGscMQbudrmwGT12sm3EBOC-vdQpl8FJZxvlcZExoazG4q6FsU6oL1z91v9um771MTA0GXGD-qmlxRLMjhzusqkYy88seHtj1bIesjDxJkvlmPJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9bd4b703.mp4?token=S73_LN59Apb6pTNztVqXO_fiFC1y0Lf1fBHS0UjnPX3kiK7BnDgc0KBnNDBEXK4X72zx95i3KeuqFnxjqYtcHkCQ1LC9Zd9XB-3qx-ygAbLMuULOllyfDMg0J2B7vVLl4oFG9NPHNk-W6acqq97ixClGrrfso_NXz-FzIwTDhtLTkBHX4v_09UOKuMoJJSuGaqsklY5V6XQrcaV9UBeMvRpvjMvOCv-94BdmZrIGscMQbudrmwGT12sm3EBOC-vdQpl8FJZxvlcZExoazG4q6FsU6oL1z91v9um771MTA0GXGD-qmlxRLMjhzusqkYy88seHtj1bIesjDxJkvlmPJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استایل متفاوت جورجینا، همسر کریستیانو رونالدو، با موهای بلوند شده، در مهمانی جشنواره فیلم کن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/Futball180TV/90030" target="_blank">📅 11:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90029">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Da8_u83xAAeiIW7AhA6Zg3h7sB5HK6riWomOhZ_HPwlfmJko5PYJXkXlKlnSgz1C_vE-X14_iasNnEIOfpiXsfuy1FXwHEyCo4MuZ44_RwaudNYqS1jV1UTQ481xLliKZv7Wr_hnJ73sIzc4WUdkiWA-eK4w-20xNiLlqq0_eh3kgnEyAMiNr0cLL2U4JSloF5I3utKpI4UTUZ5ezD_c6qxq3TVpw9Ui4NrozqxVensT45O3lqcByr4NPlL5dxTDJOu_Aq5bScMVUqVvX2uZ9-g6lcvT6PNuInOA3Tg0UgCQFdeLNVMpgB0EpXKZDTvoy14QB544vThj1_zEJeagkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
سرنوشت تورنمنت‌های رونالدو با النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/Futball180TV/90029" target="_blank">📅 09:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90028">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441c980280.mp4?token=QlPoSOf49TS56lt7vvvL67icQtDHwyoKHmi95OSYoeTJnBgl6tZH8bxIv57VurlUqyH1zGxysND4DY9e7exqQfJHgGurfC1VtUYqrBJ846cGMrPSDx5V4MUFbvGLij24vWu58A4DYLtAzBMDkvJqx_KGgf0SNRN4YnSQwP7eVQblnxz_aYA86pvSCSCgMS0s6DqpHam7p1Ph_mLuYSqKt_CaSgC9MT7m0R54xwdX2vI3GSWXKRCvhqejaZaTCPejZFpiFmDOjYqw1Y1CZgLc7I31P9DTub2Yf4k3Y98__DfYOlrFoNOGyR90NQZxZ9gC1kYtjeM6me9TU7riOBz2ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441c980280.mp4?token=QlPoSOf49TS56lt7vvvL67icQtDHwyoKHmi95OSYoeTJnBgl6tZH8bxIv57VurlUqyH1zGxysND4DY9e7exqQfJHgGurfC1VtUYqrBJ846cGMrPSDx5V4MUFbvGLij24vWu58A4DYLtAzBMDkvJqx_KGgf0SNRN4YnSQwP7eVQblnxz_aYA86pvSCSCgMS0s6DqpHam7p1Ph_mLuYSqKt_CaSgC9MT7m0R54xwdX2vI3GSWXKRCvhqejaZaTCPejZFpiFmDOjYqw1Y1CZgLc7I31P9DTub2Yf4k3Y98__DfYOlrFoNOGyR90NQZxZ9gC1kYtjeM6me9TU7riOBz2ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
جادوگری بامداد امروز لیونل‌مسی در آمریکا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/Futball180TV/90028" target="_blank">📅 07:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90027">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/Futball180TV/90027" target="_blank">📅 00:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90026">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oltP4hM9K4urcNG0BkvbIKVyNY464KV3ew_mhOzDJpNm-emzLvA3RvmZEPXCPVY3taN-74fGw9C9ufJPzH8J96a7b4l_cWlSRfWVkZuCAxdDeAIBRZ2USIOiAFrXWNtLMpvbiX79ey4frH62qbcrr05sXGefzLPaj8fSKlqOqm2_6xI5hd8uIL-VhRF0fkhLMzWWJue1TkDHnARwZ7nZxwiMV6f48C6mxlk0ii1TkS0sS6cDL8yBOyCg4WoRMFXu5vFozr8DTj-puvYcIO6YfNk4BdlzL45TzIVNTk-D43-AlzqNdoIEegnr2upmJbdUjoNy6nBB-mc4uzm6RwmNYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/Futball180TV/90026" target="_blank">📅 00:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90025">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doFrFVqiVp1kUQQG4GIW6tAUZqaLLONCpJU_VAGOM4FZjGb7uvaQo2T0prP99TFVaPItwhgbAwUchMCO-MJAX15FaXYc1WR_76yNFL7AE4bG-QrDQHjKZCel9T2049mfafWp_AnW9sfEko4rFto3v-ESLKpwV4mzyjTapCx0OWiJ0YWajz1vnmybsPWsGx6N0DacAxKLMmv1RmYcjLq1iRvUTEls-0ED3VBdArH2IVnUJ5pyS8Jx6qtCzwpe9dWpCtFLrhe-0h6J01DnZqh7bFcZoq8imEhQU-R5FblKTgwp7UJBNBqE6uClu0ctLflko5dr8r46D3lovDi5qGE4BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🫪🫪🫪
🤯
برای فهم‌اینکه لیونل‌مسی چه اعجوبه‌ای هست کافیه بدونید که این بازیکن سال ۲۰۱۲ موفق به زدن ۹۱ گل شد و تیم وحشی هانسی‌فلیک پس از ۳۶ بازی لالیگا این فصل موفق به ثبت ۹۱ گل شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/Futball180TV/90025" target="_blank">📅 19:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90024">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af6bf0b38.mp4?token=iQPxfHv7b1Rt9qzeYQLd9CQ4LI2cecB179CBEAGN0aslaCTFpJc-RwzI80dAE7fjEBxuaorsSNNx_j8-zkWimxnhuVvPhjk44LRNmlgLpQzvGvML708NAARgijzVeg-8cMYGlxmMu6Al9T-2wLAfq93Oc4OUyVdFTbq2LsFwMZw-jCeNL-B4UojZyar9SZpX-eehsvGmiFABfM3kVgbDYI6WafAbWaO6dwx-TmPCDGe0m1Me-1W8RanUmQhPGfv__p4PR-G4ScMUnGODlU1Abh6BNViKVnGdXiYtKrUix2RnYdgSYZTR1eJ88JBguc90NUMzUrfqJ22DlnJMK6N3Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af6bf0b38.mp4?token=iQPxfHv7b1Rt9qzeYQLd9CQ4LI2cecB179CBEAGN0aslaCTFpJc-RwzI80dAE7fjEBxuaorsSNNx_j8-zkWimxnhuVvPhjk44LRNmlgLpQzvGvML708NAARgijzVeg-8cMYGlxmMu6Al9T-2wLAfq93Oc4OUyVdFTbq2LsFwMZw-jCeNL-B4UojZyar9SZpX-eehsvGmiFABfM3kVgbDYI6WafAbWaO6dwx-TmPCDGe0m1Me-1W8RanUmQhPGfv__p4PR-G4ScMUnGODlU1Abh6BNViKVnGdXiYtKrUix2RnYdgSYZTR1eJ88JBguc90NUMzUrfqJ22DlnJMK6N3Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👋🏻
پایان عصر کاسمیرو در منچستریونایتد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/Futball180TV/90024" target="_blank">📅 17:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90023">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/109fc9f803.mp4?token=GHWF-am99wfArkI1ejlskA4w4vmG0g_FqM-50oP-vAUcYxgBZcpAYyQJDg1rb9cKgWM3_SB1amjF_vJqI4Y-Du8I66a14OlWM6FuaxIOUI1RNnEwcxsM31nujUm5huicyA3ct3ACJmKgUl6YtxIe2uf7pAE9pNUxngmUJsTC1ZKOBVzLWzWN3e4sl2XnEhOyPN63XE8MaSaS2XSq9HH1_T0lRYYPLtZ2tXxRz1K_JyjcJWfkgT-P5fxQ9skdn1Xo5esn07VEMCYZHTyHx8kIXUIdquBalk6h8vwNGSGqfgb9ofMPvbFNbHksFGTr-awy85aQHMrsT2T6X66mjclPzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/109fc9f803.mp4?token=GHWF-am99wfArkI1ejlskA4w4vmG0g_FqM-50oP-vAUcYxgBZcpAYyQJDg1rb9cKgWM3_SB1amjF_vJqI4Y-Du8I66a14OlWM6FuaxIOUI1RNnEwcxsM31nujUm5huicyA3ct3ACJmKgUl6YtxIe2uf7pAE9pNUxngmUJsTC1ZKOBVzLWzWN3e4sl2XnEhOyPN63XE8MaSaS2XSq9HH1_T0lRYYPLtZ2tXxRz1K_JyjcJWfkgT-P5fxQ9skdn1Xo5esn07VEMCYZHTyHx8kIXUIdquBalk6h8vwNGSGqfgb9ofMPvbFNbHksFGTr-awy85aQHMrsT2T6X66mjclPzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◀️
لحظه شکسته شدن رکورد دوضرب دسته ۱۱۰+ کیلوگرم دنیا توسط علیرضا یوسفی با مهار وزنه ۲۶۱ کیلوگرمی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/90023" target="_blank">📅 16:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90022">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
جزئیاتی از درخواست‌های آمریکا از
جمهوری اسلامی
عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا
خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا
فعال ماندن تنها یک مجموعه از تأسیسات هسته‌ای ایران
عدم پرداخت حتی ۲۵ درصد از دارایی‌های بلوکه‌شدهٔ ایران
منوط‌شدن توقف جنگ در همه ساحتها به انجام مذاکره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/90022" target="_blank">📅 12:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90021">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTTvUZbgUL4hAPpMldq03IPjJMqXiojYj1FluWz4ajijr2Z8nV0s5OzBK3vgI4kzwut1pSz_EI8bl5xSG4fw0lYGAcSbWweCtKH-Rx4nXTScIe-o2Luc60PAGKghRnh19uGX6n89_k3drADBjVQzeQBW7nKqqlmz_tX91a6ueZm8Zj9SBRqjR6ERTe5qd30aB8_SUakbqdWe8wDWGkOrOsZrEKI3hXMRm9zrINF2hqBmlqsyAjTnHTe5QrJgLSahQL6RcwKqt2sRCPdFr3OsyVyJM34_rXk_A5GCb3Q9pY4HpT7amu6Igt0ZcoAPeaNbeoufCo0OWYA9YXXlwfXfbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
لیونل‌مسی از سال ۲۰۲۱ کسب ۱۱ جام
👤
کریس‌رونالدو از سال ۲۰۲۱ کسب ۲ جام
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/Futball180TV/90021" target="_blank">📅 12:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90020">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90020" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/Futball180TV/90020" target="_blank">📅 12:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90019">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikCgWDD4lK8sbF7Gsmz9mZAq2CrB3jRbKGEJgck-97roWU_gm4VViZjTzhCtqFC_nydwZ0Rl0bYSJkdQEdQHRhx_4ZhOfRQ2yHOlbDPy0CbhPVaayc30j7l0jj0z0hO5iAv2zElVJNZSmQeawX4iDjjatNw_rXIb6mMrTInTT0j4sFhCEfYk9Jk8qNs5teDWQN-7D3zlMe-ituxjuKCwL8s4ON5azE1tUGcWz9pA9Uq28ZETdeIpOOhMNrL9iM0sJ98nlUThjHhU34Pn4hHiYWO5Gx4xyuv634dYSKgabFTbhE3k8nDNVtINlrwkEBaIRL3Ek_fwr5XslVBVZLRh3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی جذاب
🔵
بارسلونا - رئال بتیس
🔴
🔴
🔵
به Barça 1xFamily ملحق شو و با هر پیش بینی درآمد داشته باش!
🏆
فقط این جوایز رو ببین:
📱
آیفون 17 پرو مکس
🎮
پلی‌استیشن 5 پرو
💵
4,000€ نقد
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
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/Futball180TV/90019" target="_blank">📅 12:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90018">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
ژابی‌آلونسو: ما می‌خواهیم تیمی بسازیم که قادر باشد به طور مداوم در بالاترین سطح رقابت کند و برای کسب عناوین بجنگد. چلسی یکی از بزرگ‌ترین باشگاه‌های فوتبال جهان است و من بسیار مفتخرم که سرمربی این باشگاه بزرگ شوم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/90018" target="_blank">📅 11:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90017">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D98T9mUB_TAX3Z1p6HDHOCSbjZ0LcnwHAYyJcNuNnlvOklRoPxgRr6euNexgiUpH5ApWGOJp83QictezUtqkPijXcB_vYLgAmxKxKK6f7kuBiNUudeYTIjD8GG9PiMRqHtEeq3lXm4kHasgp4LuaitQQD3oBaXJorhHAfBYnWfqXIiUeDiHIqFF7g3aKjsscRd-NFNlRA9hp1w3T8necHeJzUOdVtu2018qnFI2fwDCxt9hUH_f15os-G_zMj8g7txKHAlgBMyu4H6YQq_cTTBUUG3Ou4w0WOunS13vo_Xg84YkIosRk80oKYVwlbwyouPdQ5R2jbaWOlQMCjNF-oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ژابی‌آلونسو: ما می‌خواهیم تیمی بسازیم که قادر باشد به طور مداوم در بالاترین سطح رقابت کند و برای کسب عناوین بجنگد. چلسی یکی از بزرگ‌ترین باشگاه‌های فوتبال جهان است و من بسیار مفتخرم که سرمربی این باشگاه بزرگ شوم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/Futball180TV/90017" target="_blank">📅 11:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90016">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRZ-W-z9BNJo4SXU8LKmCtld20x9UGBR61Swhf6vLTSRtr1JWzYtyvRlWEHQR5KdLeC7ymRZiEIHxFvnF0NdDpvQHFL8c6ukkO1tEvS8XM3o235pyKYULnknQ-c9qk6xtt1FFBn2C1hTfzwSQT8eI3Yqt21Q-50p2vIU0P7RDIeS4_365r7VxkhFppDqk1F6XJ0VPbf9z5NdfROyI7ViQyfqSzS510U2m6PXFacFfrtSycq8Dzmi9w55hvdm3aQHil89pgoK9Icf9Qzu5qu2j82c37v9S6NgjctGot-zQ0yjXwIaveAo6yVt7eu2SrjPlhNfPXfwRY68HkVUPsc9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🚨
#رسمی
؛ ژابی‌آلونسو با قراردادی چهارساله سرمربی تیم‌فوتبال چلسی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/Futball180TV/90016" target="_blank">📅 11:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90015">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
⚽️
تیم‌فوتبال البطائح به سرمربیگری فرهاد مجیدی در لیگ‌‌برتر امارات به لیگ‌دسته‌یک سقوط کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/Futball180TV/90015" target="_blank">📅 11:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90014">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553b8556ba.mp4?token=VVIxaqT1HsncqMXPw_r5tJzspAye3JRSmHTp5lz4WI8eQkLqGI6rfkS1Kv3I3zSc_a5RS5Pz-9JxqXG_nxwKtqYi95RUSllJFVxJTpO4mZTPH1iYIAYafuMk1bWigVwc_CITxm2sea8_m04ol7JlS5xmHwSzwYlLTQUGsFHWwolnPg2PJ8_S19Gsz4vD3tudX5xNeuyhljWHsZ0pfBMVAsL19eSxu304AIHyywVNZl-S2bYwZndCarTt76yDGEMZURDaNGW9jNvqe-KpoL_LB9lik_OYNbb-q_ObLeyb5jzHu2ZITr7k0AUcQfWrP94sLG9ii6wokhGzPbdYEMpQTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553b8556ba.mp4?token=VVIxaqT1HsncqMXPw_r5tJzspAye3JRSmHTp5lz4WI8eQkLqGI6rfkS1Kv3I3zSc_a5RS5Pz-9JxqXG_nxwKtqYi95RUSllJFVxJTpO4mZTPH1iYIAYafuMk1bWigVwc_CITxm2sea8_m04ol7JlS5xmHwSzwYlLTQUGsFHWwolnPg2PJ8_S19Gsz4vD3tudX5xNeuyhljWHsZ0pfBMVAsL19eSxu304AIHyywVNZl-S2bYwZndCarTt76yDGEMZURDaNGW9jNvqe-KpoL_LB9lik_OYNbb-q_ObLeyb5jzHu2ZITr7k0AUcQfWrP94sLG9ii6wokhGzPbdYEMpQTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
علیرضا بیرانوند: سرود جمهوری اسلامی رو با صدای بلند میخونم و مخالفا هم هیچ کاری نمیتونن بکنن.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/Futball180TV/90014" target="_blank">📅 10:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90013">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c75de85542.mp4?token=bb1SscTNuZ1hflp9QyeyJ7Hx9BK3YmefQ-OlEFYhBkRMxJLoi_Js92A45JPMSvg8jPL-6BhmR37B7pmzzj5XxrnvqZo76zcYEA0i5pmHPNSSUKAmIoHJ8VD3O0NEFIGVA0siM-S9BXqLSQX3bMKZPmaXAQ4g7lwnKHlO0YyqbQThLvI-xuNhTvkYIb2Pcka6U0t1-RdaOgzX8ybrEp9enl9e03M9V3ieye9ijLX8YIBG-9iVAxzJyj5mrbGajYDC5l94hM983e5VP0K0BQ43Sn40ITUlHm8w_YKprwfYHctxCeRleVPpHxXof4B3LP9Y70cIr8Won47__dcL4qB2TKEhogIVB51BJ1efKBnsNgeaoRVCwgssLJdThEmE-j-gALSum-hA767C7fIVGarNptTs1nn2ZMjzsdhwJPP-o1YvaYOPaKm0f7JLrFrEuoDbqTyB0--DxAhxRmSGYHACPnmViYaNQlBeH6xq9nNchyOQCm-eXTt2tT0YuIHedrm_GN5N7i23zVDTRjp_II2mQmlth4vIoXIrbUT1UTtB1nk-QI1ra3-YIv82c2JdmQKIihgiNeltZBB0DSb0JO5vqZHWbMwATHWd7a86ZvTE3_PMCYmRGJ5RMng_WKaH4sRSvOjxKBhfV8EtgCCMr90bUwQc5XWhYEvG7Cp5dOY_IIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c75de85542.mp4?token=bb1SscTNuZ1hflp9QyeyJ7Hx9BK3YmefQ-OlEFYhBkRMxJLoi_Js92A45JPMSvg8jPL-6BhmR37B7pmzzj5XxrnvqZo76zcYEA0i5pmHPNSSUKAmIoHJ8VD3O0NEFIGVA0siM-S9BXqLSQX3bMKZPmaXAQ4g7lwnKHlO0YyqbQThLvI-xuNhTvkYIb2Pcka6U0t1-RdaOgzX8ybrEp9enl9e03M9V3ieye9ijLX8YIBG-9iVAxzJyj5mrbGajYDC5l94hM983e5VP0K0BQ43Sn40ITUlHm8w_YKprwfYHctxCeRleVPpHxXof4B3LP9Y70cIr8Won47__dcL4qB2TKEhogIVB51BJ1efKBnsNgeaoRVCwgssLJdThEmE-j-gALSum-hA767C7fIVGarNptTs1nn2ZMjzsdhwJPP-o1YvaYOPaKm0f7JLrFrEuoDbqTyB0--DxAhxRmSGYHACPnmViYaNQlBeH6xq9nNchyOQCm-eXTt2tT0YuIHedrm_GN5N7i23zVDTRjp_II2mQmlth4vIoXIrbUT1UTtB1nk-QI1ra3-YIv82c2JdmQKIihgiNeltZBB0DSb0JO5vqZHWbMwATHWd7a86ZvTE3_PMCYmRGJ5RMng_WKaH4sRSvOjxKBhfV8EtgCCMr90bUwQc5XWhYEvG7Cp5dOY_IIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکرد رونالدو در بازی دیشب النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/Futball180TV/90013" target="_blank">📅 09:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90012">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sP2Xp7JYZgRS_ZDcmceTAtsJ5gocxEWS3xqgeHqxFGYin_RxuMUlfaotInQY0EE7vTmzfYN3tsL5ukYSxk1z9biNXlu8lr4N0sD9zcfKz4bK134N6W2JfglvrwPQLTiRdczEs3UCcnarkWROKsiMId5DeA5_G6xTkmoqDmY-SdoCLOqSqerctaWg7TseQBrjI-5RDKPJiRM45su-1G_LE_j6mILa7cjtRJl3zbT1G8DgQ0hCwPTNErUnJ7oE2H2PpvtrJx9aDbeRtjcjuik8IjDIdyVxFUu0urgLCwVd_RBzzg5noPWnF2z1nSXYAgxONQ4PbkxaJj1QLbqVzT_CDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش رضا غندی‌پور به عدم دعوتش به اردو تیم ملی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/Futball180TV/90012" target="_blank">📅 09:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90009">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d4fe02d07.mp4?token=DecDruLCGc-oYWeGedxT8o-OiJD19Zcc7wuK0M-UZvEXktUppWXbVhrM5Kq4FzwRsz4sV0GXdqRXoisK4qLloZEq5mg4kLsNIrXaYX2YswDmqsW7PGafC6UC7FEVAZwDzG43WyCdSFrcYlqfdmDDFeR3h7c9fqMDapTiOktL2VpwYisvwu62FFDPYO9NrsxTGLEN8KRv5BNhhjw-bl6UdooCLx4dlxv23c67hy7AiJVCKkqBKzWGBnNIru9vmswEu3_xq-euhXGbiS-Iu-1iIAEr8-9QOH5YseQKfyZGqRpUzSxzEr4HO_49ahsFtTGz_Bz-88nDs3GjiDaeo-8Qww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d4fe02d07.mp4?token=DecDruLCGc-oYWeGedxT8o-OiJD19Zcc7wuK0M-UZvEXktUppWXbVhrM5Kq4FzwRsz4sV0GXdqRXoisK4qLloZEq5mg4kLsNIrXaYX2YswDmqsW7PGafC6UC7FEVAZwDzG43WyCdSFrcYlqfdmDDFeR3h7c9fqMDapTiOktL2VpwYisvwu62FFDPYO9NrsxTGLEN8KRv5BNhhjw-bl6UdooCLx4dlxv23c67hy7AiJVCKkqBKzWGBnNIru9vmswEu3_xq-euhXGbiS-Iu-1iIAEr8-9QOH5YseQKfyZGqRpUzSxzEr4HO_49ahsFtTGz_Bz-88nDs3GjiDaeo-8Qww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوضاع اصلا به نفع رونالدو پیش نمیره.
🙁
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/Futball180TV/90009" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90008">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_byEavjJywDPIhWqQxB4uQU79-Y30MeC3bOfartCpeKOvJkTctejEL2knQk0e55lKPuWOVI9_PSMFRO4LzAZFUhrlK5QhsfBYjPcpFc_1Lnkpg_b9eGvUM-tu_8B1NAOCBocBnF-Yi0B3zCgcb1shoLvtEW4SDSfHAvwuJHPE_h92-L9F4lRKBSPifg9SY_K8B3SvgV2ecKuZkpAKk1X_mUWTULHZEKAojegBWY4TBEwDlpvdAX9yuCOuJ1Ss5Hmw9Jn2T64s-L9XbeNwgtM9ic9A_JI-KF44MYaOr2xXBIAPAHrx9ZDL1du9UwATTl92i0_cz2e_CnxkuIJqgXjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
توییت‌جدید ترامپ: آرامش قبل از توفان
!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/Futball180TV/90008" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90007">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVdsdMiDuINCN0LTXLxTwIck27EZbaFeD1VFOxLjf87mWd2jzCln6jlR8OdOa5XGNRcuPO1iaS7bRHbaqfLVLY3NCGA8ZfHPCFpeCL5aPvlwzkTAni8JUJTZ6KFl_6uEm2Y71Med28dmY63PhQHYRGf2NpL-e-Nd5YbXTOgWEUHdPC1L731EuUomMIn-sUk_PWLJj5mgUThYWvqGkhYJcV8cA_iwEAbkTbbHpgmA4CjtQmVULUYpMvjXqvNePa1PfdDfdDuVt8qBO9vLnxGfIrlufS9C5_ssom-5C_0BrMCKS4U_bQLxP94DDOTu3DfK0Dm-ngT1AIjBlADl5bGeyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔵
النصر در فینال لیگ‌قهرمانان سطح دو آسیا مقابل گامبا‌اوزاکا شکست خورد و رونالدو بازهم نتونست با این تیم قهرمان بشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/90007" target="_blank">📅 23:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90006">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThWbnQAvFT8IgoOmaD_PAbZI0Zzb7wLgaG6UGpX9P0FrP8Z4-cXIbTA_CeahYLmpqPAiu96tcH4LcmU77p-2dZzA1U8jd8L1T8T1EFNtQxM4K6IP089kQULhbzrWfg7SY7_MIKQXVjjo4jdPgOeIoDn8nMv11af5w4ArX_I7gkE9KjS0NfYFxM4pusZfXJRERGtbpfx1l6JsuCc8xXKCcdrKvhpnGr6hG5nsXbjjkw-4pbkZpuGqBT0S90r1nKl4LvRM35sq-ownSD3qS2AO_Kbk--cqb8hAwnrBVAnoGBhkl_hFPwbwi6MGQQRkFvWPfA4pGL-YDpIr_cVbBjZNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از منابع انگلیسی، توافق‌اولیه چلسی و ژابی‌آلونسو حاصل شده است. قرارداد این سرمربی دوساله است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/Futball180TV/90006" target="_blank">📅 21:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90005">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">💥
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه
علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه
احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی
سامان قدوس، روزبه چشمی، امیرمحمد رزاق نیا، سعید عزت‌اللهی، محمد قربانی، علیرضا جهانبخش، آریا یوسفی، محمد محبی، مهدی قائدی، مهدی ترابی
مهدی طارمی، هادی حبیبی‌نژاد، امیرحسین حسین‌زاده، امیرحسین محمودی، دنیس درگاهی، کسری طاهری و علی علیپور
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/Futball180TV/90005" target="_blank">📅 21:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90004">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TO355-8qjFZzt3mCMSDCdST4M571ZdHYPaJOnL0bW-MZkTOpRgupf77WVlARB1PgsO3XADqyjKf3i9nvQ0ZrvA4WeEZ3_oQMDFXK2KBC0V0wUP8etwWj0v6_UBjRFsQIbX5J_iSkNIRIe9PPKlGvTqxlrqUNFJHmsrwQE3swElg6PKegLjonhnpUiXjQoc70sjrFDidi3VDAyC36PJ32leR_nFRqQZpqWSGkNzJh95HeXPaRPRA9mLfhcAfB-SXDXnlLvtB_RkOyqh5B4Ww3ZPc_Xnz6UwdUQVJmEe0KJQKc-da7g26kBTDo6hkxBxjSvR6WcnU5aowtfvGY8nbdjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از منابع انگلیسی، توافق‌اولیه چلسی و ژابی‌آلونسو حاصل شده است. قرارداد این سرمربی دوساله است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/Futball180TV/90004" target="_blank">📅 20:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90003">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAGvNNPrao7f0pTAsSkLMXVPOO2F7nGohM_H_QM3-Cen5-vYQZfLPLr-PZFJcjpFUJpu8CEs8qLOIFx1OfQ9GP47ad-2se5sSvMfW0V7AlTgFiM2H9EzXDEFH_R_Eu6CTX21FXwqMCto31oQuNPMGOcZ78SXTo0_IFlehmYaZOwwVbOxqwk9jEaLhI15fnU5JlKoxAwykK3aliLzl6iNQPGPB8n1GwP2GpI2G4Dx8iU5Nxf_kwI2Ruq5YcJqW_64Rqz-zLYHyFcCD4y-gyezSBE4b03UEfkz-IrdCGcwy8RSECGIpokNWguI9mluXqOxBDiW0USYQd-7juc0DeefbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پپ‌گواردیولا طی ۱۹ سال ۴۱ جام کسب کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/90003" target="_blank">📅 19:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90002">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVgnnq7nwPDgAjXZ1WmswpV3PzHH8QMT7AraA2ZupLGLuwuNGsrknS0YBGj8WpO70m4GvoXgLMyPPNquxZpeseLX9alWWCuk1MV3LUSPI7uiHyfRI0sRMqREd01LaLJqsjEQPyBsG4IdNPIVzGS5g74fXwq-Zf4smO76vA65gkLd5aCdwbLQASMzmnoqanCF8VVLQfl6zJz3mC4jNI2ATYyGH4cT5AEMAIBNeeom-u1eOlz_s7Aoz2OaXLbIgj_kpyBksJV7EagnAsa66CWce3TFz_2MgREKYUQ-SVN3B4k9aRFDpHjk3izYVH-UlhPoTOruVw7V5CQPPO29wNVcEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منچسترسیتی با برتری مقابل چلسی قهرمان شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/Futball180TV/90002" target="_blank">📅 19:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89999">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Waqumvmqy4u2SVMFKrU1rWhSKNJclXFALs9HdqhtZ9xSIgTJedkyeCMOhg7kziFfAs_SDH7fSjx-DmrCCbwWDE4C3-J7eXqUWWr1KyBtjquvJMavPgyRkTlIt_25Et9fkWBZ5FHHfC4r-08CopssR5GFy6gnSEVgmRzy89jAUBsJtbDdoEWzORx9_8JTIjS3aSlJterKDSkvbj-vlexB_OGoCUuKxiBinwJceOVVLNBFa1ARJL1-DHfpDs7NYCc5T9gW9L4K-snCCJQIp454Cmu2leupZ6SaxIbnR45vaMMZZJZqHVrsSezXL2UsSeyH9rojGmIJDs1jEzdDVmPphQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فینال جام‌حذفی انگلیس؛ ترکیب سیتی و چلسی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/Futball180TV/89999" target="_blank">📅 16:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89998">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Py2SVrxdDPhT6_eSUHHM4MK7AM7m1UvHWKMUlQBCeLtVjKkWqpoRv8gzd2qeAn7mkeYA445eUsGQJF4hwVs6iNdeHunKBI4WGu9ia-p9ZvpTmG9X3apbPxHHQMeXkMu06dsvlUa-vMYZW2J8r7Rdc2dEjvhQAoqbjdHZ8AJE35oOX3DomO-RmIrRcL6hvCtW7-muo69cHjkFivJVTOEQXBiluWV99oh9bXfLd15XpqZoExUHX3EKNn-SEEvUTiKaLyd4Nw2PCg70pqNMVSrc2AeGDUneqXqC8HJR85V9xlaLoZVX6AmJzolsd6k_qi0010jM1byg3HJieMj7gYzMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇩
فهرست نهایی تیم‌ملی کنگو برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/Futball180TV/89998" target="_blank">📅 16:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89997">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWRl88-W88MYuDJaXI6DZ2SQeTYbu4BLb_g5CH1Yni2-i_ptitvOZElrAQYKkaz2wBJBc9GySWXOwKmZ_yiftm6YeKJeIss-pW33NJjHD_XM1-JtVZK9t_tPHEXSeJqiYXvUmk53zrw5kv-Jtq-yBIFi73seBh1BN0wtcJjArI0UU7bp5LsaEDu6vTKiD3qJVrIsSoFzU0lb8o_XQz55j-tqQtqJk-pJwrM7wt5Lt9l8dh65wwQFSo-Ki1zkEy-ZugMlSmq2UBnf9k059g2Skqqymv3Hw0Q_lnLiOpA4UzBpJ-pAl2iIVryG-0AdkJtjEhJJXs4GVTqbmJq4rM33mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پپ‌گواردیولا: فصل بعد نیز سرمربی سیتی هستم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/Futball180TV/89997" target="_blank">📅 15:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89996">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01b819c41.mp4?token=Gix2jZCngEVkSo9-VQAZCR5D234SnP6hzgMBDc04fVTK5SGWS3goIlbhIEaIvsvrqd5EoON43Evd8HA_Ii3PbVfTBbIT31ZD-rbUIRXL6PGKDdS1swswXRdrveOxhDp3H_clqVvJJN4f8QByrpajOaC1yf-fMP32ETD4uf4232tQ8Eae4FAY1Vag00UOFRzbQYS0YLpGOX35ApSddg-oDqdPjEPM_M0eYh6DRj-gS9nqTs15pIJkc2QAQs9bvu-4Eg6xMkvfYccJpWnokr0l7pa9aBxa7sqpgl-TvwMjc9XL5ZHH0gDcZgrNS9onuwFsaFqIL6cmvzQ0eTt9CJpOHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01b819c41.mp4?token=Gix2jZCngEVkSo9-VQAZCR5D234SnP6hzgMBDc04fVTK5SGWS3goIlbhIEaIvsvrqd5EoON43Evd8HA_Ii3PbVfTBbIT31ZD-rbUIRXL6PGKDdS1swswXRdrveOxhDp3H_clqVvJJN4f8QByrpajOaC1yf-fMP32ETD4uf4232tQ8Eae4FAY1Vag00UOFRzbQYS0YLpGOX35ApSddg-oDqdPjEPM_M0eYh6DRj-gS9nqTs15pIJkc2QAQs9bvu-4Eg6xMkvfYccJpWnokr0l7pa9aBxa7sqpgl-TvwMjc9XL5ZHH0gDcZgrNS9onuwFsaFqIL6cmvzQ0eTt9CJpOHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📲
پست جدید لواندوفسکی:
بعد از چهار سال چالش‌برانگیز و سخت، وقت رفتنه. من با این احساس اینجا را ترک می‌کنم که ماموریتم کامل شده. چهار فصل و سه عنوان قهرمانی!
هرگز عشقی را که از همان روزهای اول از هواداران دریافت کردم فراموش نخواهم کرد. کاتالونیا خانه من است.
از همه کسانی که در این چهار سال فوق‌العاده ملاقات کردم متشکرم. یک تشکر ویژه از رئیس لاپورتا برای اینکه به من فرصت تجربه باورنکردنی‌ترین فصل دوران حرفه‌ای‌ام را داد.
بارسلونا به جایی که به آن تعلق دارد، برگشته است. ویسکا بارسا. ویسکا کاتالونیا
💙
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/89996" target="_blank">📅 15:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89995">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDYdv3pq7RjBJUa58Sv9Lzmnws2juDEI1SHlI8QNvreJrLa53BktDdJ7V05dUgW8gmvyt8tPXBJJSL0wc9Ex-8ilQl1OykGXjOxQ_q2bVfv0IkugxSs3_SrXQu5X3BUnUCGEE5yipFhe9wXo014TsvMgqxZEombu45oE-HdG5m-Y8IGjBGkBTfHl_TpF2Tpm8L2ADTjsA8lsXxooCYEI5k__8wzqJXtBW0EdrMj6HAFjrc4ChFp3q-wh_wUvUQQyyEAjbTkCRWRURwwGPTBQ2nRF2VbcteMO12DJdjlkeB9xCvX0abjGh-QfrnAOLdZwQxEL5ySKdH6ErRswJWcy7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
نت‌بلاکس اعلام کرد خاموشی دیجیتال در ایران وارد دوازدهمین هفته خود شده و اکنون به هفتاد و هشتمین روز رسیده است که در سطح جهانی بی‌سابقه به حساب می‌آید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/Futball180TV/89995" target="_blank">📅 13:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89992">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZG4qfVoFfa1iQ2jc1KHbeaNNP7EOM0BZAR54fV2akYGr5_QL1Rj7R7A3Y3cjgEJx4sRo1AvY6pBtbDQljS6w0KrNpmj1oFMrZBMaZUiaQm9XUCPj0qcGQ37qApj-NghusWivFQMTzGPqZz5jnztvo-LSQO5bBnZ4HmxGZ26GiZ8PqwRBMkOGjbz0p_PLIHpcIVYaaCPVISgHdk8uEdAEbVZKBCLdEIYYKXfRxpKISP24-xqQvYkq2wvTTVvR3-pybapF6hDToYHJahYqkk_BJC0q85J-img2CRUtnEQ4Pqkufk3JT9PLjwgVZTFrjrR3tP11UgjX2IXrEsFRz-ssDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
تا اواسط هفته‌جاری انتقال ژوزه مورینیو به رئال‌مادرید رسمی خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/Futball180TV/89992" target="_blank">📅 12:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89991">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcdd85ad92.mp4?token=bzXPXX-XAR_mKaDRvQPnZOrKbRegRW8bGuRX5bhvVKzSddTC8_Wfu4X_KDYeMATGBYQ_mCiuFDkOTGhhgDq1zwpwRH4or_aLPFciX6y_Iwik487j02odNCs1uvMMy5SqoI8wSEV6CWiX_9N-Piin-_ciM6jGXaMZbEAw9oEnYVdrFYuiZq4F5SAtjATTuqs9KN8-xJCLqIpm6EHTCFUCVyQzJuAS6ZZznnUj4Th-zSvsoNxBan5TRt51KURQUEakY8etr8VWVnyB5sWgPKu5sKz86fW8SlhlyvqDJwZuxDStIlzVME31VZNlReyk_qM92wOD6HwQ_mQfbRBX7Ip63A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcdd85ad92.mp4?token=bzXPXX-XAR_mKaDRvQPnZOrKbRegRW8bGuRX5bhvVKzSddTC8_Wfu4X_KDYeMATGBYQ_mCiuFDkOTGhhgDq1zwpwRH4or_aLPFciX6y_Iwik487j02odNCs1uvMMy5SqoI8wSEV6CWiX_9N-Piin-_ciM6jGXaMZbEAw9oEnYVdrFYuiZq4F5SAtjATTuqs9KN8-xJCLqIpm6EHTCFUCVyQzJuAS6ZZznnUj4Th-zSvsoNxBan5TRt51KURQUEakY8etr8VWVnyB5sWgPKu5sKz86fW8SlhlyvqDJwZuxDStIlzVME31VZNlReyk_qM92wOD6HwQ_mQfbRBX7Ip63A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آموزش‌مسلح کردن اسلحه و شلیک در آنتن‌زنده!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/Futball180TV/89991" target="_blank">📅 12:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89990">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPBM0OiwD1nZQeeUoNZLdmfTxVMAWWu0Y5Rx-zncFe5IA6StpuaegZ47-GXX6aEJawWCWKtQJ7aN_QRrTZ3_FrHYg0884Xl3ZGvMIeL2YfPxdn5m_RsnADX0I0IDZdKMp5q3uGcAAucB6yL5hbBVLurIiGWUJdaQQN4pNfwFLW_mm2_X4Bc9qx6SEBa3o6_0i2pAuOfQ08lactU9uypmWJ9N3_sjPs-XarKqPL2ndasebfGKE6xy2MDgCZ3mLkw9NIulRaRsYUlNBTQU1UpvCitlah6-gY5h_B2GxytfViJhpwlnCHVu-JWThKQcv46SRDrtDHZqHZJxhJq8119Rww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هانسی‌فلیک با ماندن رشفورد موافقت کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/Futball180TV/89990" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89989">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZA4a7IUL6NaSCIbzpHOdrvAtm88LNyHlWu1R101qcRy3qMUsJjyVOJUuEDGESZp6EhNyFVjahS7B0d5tgEjA-NOqLjw-Dvkz2WMgsKWhBX_JVgx0NT-goErefcKKEWcjo5aq9F6TcFdt5eGdnhJd6tZxJV0B4TJHlOHsMIg5ocfr3R_SzUt-xm0V7ErUqFu3_aCaI7g6uxf6lDdJNkig5w8lbwkfTao9k0vPSAZdIPlGCXKTHxV1OxeM3IivqcJ4xHiSmX30qcmrwno9wNB2lnqw0vwW0J4dDVqNjrr-7n73OkSACF2rWLtYyPcB9vmql_8M-5LsgH29UOFBxDKcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇰🇷
لیست کره‌جنوبی برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/Futball180TV/89989" target="_blank">📅 11:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89988">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuKbicQ5vDYzyS3S6JWM7ct3SbIRau2xhASJ9bCfg80oKOfSDh7v0rWSZdKAjSJRvUplPmgjk-TE5k60-WLm8vyqBjO4FEyZfmLDbewKT5I8EGVp-jyC1eu_0clf-thwcDtp9nQEeI2yzvNim2HxaJcIl6tPkguxQk5ixXzkkZT3_pZk_BN4BOR8Km_UijfvnIPYeVAeMAEIVnDxEttJI3JQmiAeqh6VFQ7dgaNFWriEtsEBqGFvxfVb2BfxHvKigB831hxeQuzcMMb381E1NN43NWTUDD6YDQrSEOaGHMs-asCnXofP-CgL0pvI6at2haQgUmB2CKCfNlRxNp13NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وزارت خارجه آمریکا: ونزوئلا 7340 کیلوگرم اورانیوم غنی‌شدهش رو به آمریکا منتقل کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/Futball180TV/89988" target="_blank">📅 10:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89987">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فوت پدرم باعث شد از آلمان برگردم/ کخ سخت‌ترین دوره فوتبالم را رقم زد
مهدی پاشازاده، پیشکسوت باشگاه استقلال: در اوج بودم اما به دلیل مصدومیت‌های پیاپی‌ای که داشتم، وقتی خواستم به استقلال برگردم، آقای کُخ گفت که باید تست بدهی و این برایم خیلی سخت بود.
به ترکیب استقلال برگشتم اما دوباره با دو بار پارگی رباط صلیبی لژیونر شدم.
کخ مربی بادانشی بود اما اطرافیانش خوب چیده نشده بودند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/Futball180TV/89987" target="_blank">📅 10:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89985">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5QeCiItdu3cftDKMEeVzL0_EboI0JMq5ual-yaXSFHfUmiu74xCLj6EN2cKxYXJIZ9bAMQ9ZPGnme-4c2YRWGC-BKVbv6puulDGQ4dCql8F3o-F9mZvQifMnneWN28BvLqxCMJah2ltOfd2huAutoNF6KHoYCIYMI8wA_zvj92nsrIz35C6j1Nd3_nkzKLjvgAyMaZQ8SU6dVLZDWqEbOYM7o9kVLa8vSmBVh9pYM8uqz_TA1t5pSCasEdqgPU6A7wtl3on9brQgVxFzfCWXQ4BwRCfEP8wFg4bewDmy9rW8spiBMEw4C5ABEBfwi9pjTbmwoT7OpCH2g8xbm9u9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ژوزه‌مورینیو اعلام کرده که پس از پایان دوران حضور در رئال از سرمربیگری خداحافظی می‌کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/Futball180TV/89985" target="_blank">📅 09:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89984">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">💥
🇹🇷
جشن‌ویژه باشگاه گالاتاسرای برای ایکاردی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/89984" target="_blank">📅 09:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89983">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TY4fHyRr6Rb67G8V3v5lvWUzGTyKoSdWkVfBkFheOnny8q64T9S2DJz-7PtQ2y0JMdt9W6QRlM25XRrsGzEDLVzIJY9Xj-X9LYPpR_D6yZarxRUP0Zu9t7bJ-ACRh71do8TEOFigxRFacvWJjALZCGG_HcGJ_E2AdTDWZwe4fKLaUtApQsgqDpG2R1O7L07NFEiLaH_383FgYdgxPKlAuyQnJBP9Z8lA2lX-dfovjLNedczZ8_uBC5ebsBC5on6zuOHBcvJyNh2_ycSNOAOtXE3Zrt4ufxw_O9votTfbs-1ofW4mGKm9B3MpIosLomqKj3gQ2onj39sf5dCmZAsl7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک سرمربی فصل‌آینده تیم فوتبال منچستریونایتد خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/Futball180TV/89983" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89980">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPzEsYZKDkL7V3FYbXSrVwcNdK5SAER9PaQOW8y6jCAbzMatzg9o6gY3-UBGXIdZw0VM0uzwVXjG_D445SbTheWqxJPG-ccg-DGWKwBj01y3xFz09NbnshKge6ejTqCl7KgUJSeDeOyzK4KPvI7yR1w9sw94fyIEckcjX5by3hFONmS7uyeXgURUI6RZFx8-qBSJAICA4iGzTPvLaG3MYxfgBAfZQsifDymNIQGgaI1CzHQPrhWdqyzreymR4s_jMucn0JjOn7S4T9rN3znLs_Cu_X71lyKjRwkWJHWVyYdv-KxYRGjzzajiYSnJ_bIHA6OFz6BVIbnLCwZ5T6SpxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون‌ویلا با برتری قاطع مقابل لیورپول سهمیه لیگ‌قهرمانان اروپا را کسب کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/89980" target="_blank">📅 00:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89979">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsXiOgD6Bi7-vRpVXJmj6_mqTX0NpN9874_zteHNAUABPqjKomMhchN-SEdXepjXIBcXufwCXN9_yerAKplIER4h4fHiX8Pau0FiLu-5Xsy5XCVmuW2ZyEyQLm_4ihlDTlhbjBXinTAZJtk9vYb7otXBK-_V_CUHxWcrgX4HotzFbwUrd4o1jggS30819V5IrOtITNqmwkI5TghT4bzj2E82pxIhw3-Loi9qvRh8P3FJBD7xMDAhsCy1pYbQ8spsLdcEYX5xdJaGfYsvcTYvy17uJPD_DAbHYkKg3XLn3qzkIwel-5cYIBaAje2G1ks4YU1iaWuQ4CzNQ52pQkW9Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری؛ رسانه‌کوپه‌نزدیک به پرز: ژوزه مورینیو با قراردادی سه‌ساله سرمربی رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/Futball180TV/89979" target="_blank">📅 00:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89978">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
‼️
سازمان برنامه‌بودجه به دولت جمهوری اسلامی اعلام کرده که با وجود تورم شدید اخیر، منابع لازم برای افزایش رقم کالابرگ را ندارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/Futball180TV/89978" target="_blank">📅 00:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89977">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vx8ci981lBwNvp6npHcZOcKp2Z-ThN7ZHKJE_Jpp61ImI0F08EdfYTlvTgMZfzxew8z4h2od4sTKpPmIXb78WOCpO6QVat3PCkiCcscr1FZU11dby5gadp-162lr3TNHJQVYusChUrgi9sA7ZUmv3pr5g1OzlSGZd3xNGS29EbX58qce82bLDvknHVUP4BkmMvrS0DyKLJfoOhefbihm982Av6DnAV0zIT2i8r9eJdSt4uLhZJC8WBg8A2nh1P0c0_dXC-f-GAfnYGd1qr7zHgMAQYkgO0Ab3AdrOn96z4xVlsWcxmn0YswEpaYXmd1jNoafMu7YYcu6_oNovUuJAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇱
تیم‌ملی لهستان از برگزاری دیدار تدارکاتی با تیم فوتبال جمهوری اسلامی انصراف داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/Futball180TV/89977" target="_blank">📅 00:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89976">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtwR75CDun8nvXpPQ9J0nVLJ_hMW3xmdJmMxldSz6QhsTDkEerw9wfyxg5WTBuLpC_GYVfpySyL79zC1DMQ0Qe-NsouPBAFkHU6-zBSjaBYzHeVhoUdTlEbpzyZ7H18kN8ZFJbhO6PedeezcRYM5zEngu5kOi-qRTW-Co_LrHOfCRk92Ecc4F4B5-Nl-sUCnQ6mtMtneysE9JUbrEfk7n1RWhU6MtUBVo4IDLrGYzEy5uDyIa4ssVX70olN4mSGZt-g5IOx05WjHEjjLhfQoYdg9z0NpndpfykL_cTBBGEEvUf9uhx81Q_C0zGgBlKmmrJ960kNaB9QbjOfqkoZgsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇹
لیست‌تیم‌ملی هائیتی برای جام‌جهانی با حضور داکنز نازون مهاجم تیم‌فوتبال استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/Futball180TV/89976" target="_blank">📅 19:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89975">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjogqOeqKCjpiRkI_Jrrxgb8fbiHHG4FPN4VgyBCwOr-TvGpTHshG9Ypdkdmuocmbksz8_AeVAudYgj03G1VCr8hH0JxR1y47Pkj5xsjxEtEZbCDfxBzAX27cy8yPnG-PSCl4O86kfAaLQclxxezuxFZutv0cnLdp_A116uZCcv_Js6cT1oa9fSBUngsTjnXI0TrUi-wKhIMdaHfqv32ZVpcxSpAMYSqIrLfFBOqoO3SyPqZxotS_rbO6Svq9_e5c3WZ3mjvEsWvqVWvuGLNcnUzkZcNQ26Cx_GUgS6_pRyGTCDHDpR9MsqNyi8MqV41pZz5HKNmEWEMk5CJJgDMKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/Futball180TV/89975" target="_blank">📅 19:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89972">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArBqvK75u9pZYc_HRqgukfau-JH6VDtxnRxHKareDK5NadWuEe54-N-lYvgKgVpAhWhtYBv8Juy3ViWqECI-mut9qMRDEr6Ip6rK3T_5K4ZKZC1o8ck6O23PFGEAssgVJ10p_b6SftxZoQAn6lnrXTpVd0pU9qhs9JOjmRK0RRPORvC-AFgLs8wr5rSzYPXfD3FsV2OzybDka0AovTnLaumvnNtTBlhifzkfRyF-b2h6dlZE3QyR9yZQnkx37w_n1FNntdDj_OLkNa2zb8rEpdlWXx7gfQF6j_qNkat_bNkouPK-8y5N86OuCjmBuUI7Qyun7e4CipW4fNBP2l221Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇮
لیست‌تیم‌ملی ساحل‌عاج برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/Futball180TV/89972" target="_blank">📅 17:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89971">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKy6oZCAP4QfNMaPYmo3doiZMjJeMgojj-b4Qxbwb0aHYffm_j5A2lLgBQE40GBZuS5KzObq1UWVuDSw61leEVzduw4utDNZMICZoOO9jOyY_Uak0TKsW-xqEJmLsz9aKMkumZSb_fVKMhV9KOlmF9lNmL1lZoHRlJLxXG5yD_5GgULVVAVr4F6Cz5JZPfSmbipOfZCfmGDLul_UU5WZAiWMHMUHF5VFbzs-_5QZDY6OJj65NjrXC69Bqu1KAkDc7f7IvOsImY5NcAUYYNwen67zetWG_kaDhHiZwRnvAwCNUDzZmVcL8iexVdZCgXwodcU2k4nMAMedpzPbPsll2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
اعلام‌ لیست نهایی بلژیک در جام‌جهانی2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/Futball180TV/89971" target="_blank">📅 16:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89970">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🇺🇸
فوری/ترامپ: من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم اما باید یک تعهد «واقعی» باشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/89970" target="_blank">📅 14:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89969">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8OGfzHPOApn_Rj3WQvhOKHl4y1tYu6NxyyAECtJSLDmwDhmfnWdGJoEuCvrtgxs1NyhZVIYKZbqUX7fZjpEAB4AV8R6jr6zStdQNn8qQszBPpmVTAvH0VW_5NXxrOsOPsGlUIstrYQN2fe3i7NtswVWmxDyDZx7SkW8AUY9U-fDY9qs2eNqP7ComkMArlD3UvcVWuNuZzrW1kRS9o77V0eStnp7TIgpSyCYf6IygXntP-u-D4BTMrrlY8Zk35miDvNMgETDNgp6qw_9oBhd-YecvpGS2Rcuypmc21mSXp1TGAve67HabQglqT7VpKyGhgdgFX_buyeaEoTUPafj2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نامزدهای بهترین سرمربی فصل پرمیر لیگ
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/89969" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89966">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhhNRREnPXxjRJYyIp9gLvXaIX09eRyjaQPTON6kqg4eTT-pIhjX2UGCjuMABh5VAGHZ3A_Gal0BWQ1QSeDa4VMX8nANo-zzUkpO344aiuBJeeV_uGQOcw-sPm7WTMP6TiNR2QJBdeTKe9yMZi1cBKDnPhqumeTJ5U8f-aM_oColh6zyxYejIbmQFUh-1s7VyRmzXbH3rZlfOFZiw4clLj9iQ5_p10Xwql0MzEW4N5c0BtsY5nNeuhbBwu8oy8cm5_U__8GcAhn3PYKqYzL51_XDpefvAgE_JRhy-zweR9NZPLCWtXF0PFSGCRJ7_BFF0mNd5H-Kvx0ABuEdTPAUlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇺
کوبا اعلام کرد رئیس سازمان سیا به این کشور سفر کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/89966" target="_blank">📅 12:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89965">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTweV1xqNyOZI9RxeUjNvHc9zg02pEmnvmhWNWAZcEUz6FSlOilUkXoZwmvKXyFRw7hFVKq4WeEJ7E4oxsrs9SCN4-F102EiYfo7O9JDm2P8HEVqOMiDOgaoZZA9o86L2JlYqEnbTrSJXgd15hM8K8IVP6WPGzQCmNS65SY62diG5GChLNexPCCZZLjs45wKsqmhk59NBnFcd52oagZOdBb71rwW8h8-8huTlmmBUOWMEzPO1-wNJhZgmKNoVYc0evkdesG2bG4NU19PWifvpO-6h1atIngDNn7nVDdKeyHKViBG1juUxRH13o7q8C-H5ELGHRkz23K-nHPijkUd5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇯🇵
فهرست تیم‌ملی ژاپن برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/Futball180TV/89965" target="_blank">📅 11:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89964">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwOcayuyly_ZuGtoBgYLfvDYmwJzH3u7BCiTSgJF37TFGQpeP7mTf4X4UT--1hw-O8DqQC4f4-0RWYFmd7ItXB22DLynYwkRKE30IRZqRqZ0KuOzPeMZU1lRDjHxDHoRyye9z5hR7Akrkokm45SKNBkFIO7vUQlgvGRD5cXo0I0oFMn8HdWIecldzXdY-5fKEgQW03NC-b35a0R_8XSHbX0xtwBi7q0Vgir84TamXYxndqzZmcK3zuza3NsbBjBrv1j4TSEKyxd4AgOXjpEi4ZkeRiXbgN3QXoyP79V59v1ciobHeKS2wpwbOL-fv9L0Z1gfbfiDL07IGdIppFfRzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
امباپه: سوت‌های اعتراضی علیه بازیکن مشهوری مثل‌من عادیه. آربلوآ بهم گفته که مهاجم چهارم تیمم هستی درحالی که همیشه آماده بازی کردن بودم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/Futball180TV/89964" target="_blank">📅 09:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89963">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
وزارت آموزش‌وپرورش: امتحانات پایه‌های هفتم تا دهم با نظر استانداران با توجه به شرایط هر استان به صورت حضوری یا مجازی برگزار خواهد شد
امتحانات پایه‌یازدهم و دوازدهم تا تیرماه برگزار نخواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/Futball180TV/89963" target="_blank">📅 09:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89962">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLo0DiMhT_iKTgIse_Au9m8KMFIpjxE_hEct0RT8Y8mgm2EXcapzADmQLCS_hfaZvy4tzNTbQm_K_P5BcP6fGO5yJECPA5icGZvptdl9Lm1AmYH9AxJYBeET4BqaFktNabYssTcnaDk2O6jSyEKCAs5-1DWVlerdlYkOzeaoD0UE7JWQogh6l8pEH8M75d6PvuqWi1cdnXM5tKKa7tzt4Mz_yEuoQRvqlTB2GaHzWAa8E9MSY6BdkRfvCOQcxhvxfRVNbk4Tsb5_82xtd3b7wP6IHksnRFhhcwxPnZGFCLZNjAdBYX8qiLu85fEeUJNSvA5YmNJ5Up2V4qJN3D164w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بازیکنانی که بیشترین قهرمانی در رقابت‌های لیگ در ۵ لیگ برتر اروپایی را بدست آورده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/Futball180TV/89962" target="_blank">📅 09:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89958">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🇨🇺
دولت‌کوبا با هشدار تمام شدن مخازن سوختی خود اعلام کرد که برق در سراسر این کشور تا مدتی نامشخص قطع خواهد بود و مردم این کشور در آستانه شورش قرار دارند
+کوبا کشوری‌ست که اخیرا ترامپ اعلام کرده بود سقوط سیستم حاکمیت‌ش بزودی رخ خواهد داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/Futball180TV/89958" target="_blank">📅 23:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89957">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6579d2e780.mp4?token=rLaZb8JsgCmnegx3M5X31n8C5HFnbC2VLfeBC1K8icOpNX9nonYI6JmYlwlyWPXcv_BKRCJGt-8R-7hMpcsJ1iEhHQIXIHfbQWrTiLxq7OfldtQBivzDK5WM3h6yLEzGKaJ4fRONmS1MzXXz1E4aNecj0BmZDDS2cCaKQjzPGP0p-hNjLmqnJSNTYmWdnE4cDOnmyyBbPECN-krIJTuAjojWiNTBDcxlXYZJUwSi4tvAPy_21H81O3pkVrNZSg99Fke2ACyIXr1tp7Q4lVYQlwcyb01VbOqNU36A3f2r9qpMeaPqq-Ci371yuurQXC1h-rqUoHpNdSe2PE29HT2QbI9foYodUMA5bTX54J7bbKOrmzmmdF65EZphB6pBhdFbFqfCZAfkC0KyW20tuyValPq1Xp4RaOnqhu9fXvhmIX1wFEnWXGog5zZJhnjmn7jC9xrMot9Hncz0WBesVjj4VESvrVHBPqcXe8ONbNlL61LMGow68k7t33doXZ-AelphvzeELnR6Dyw-zV-9yy1k2t7PWQKzQGIUOTlZBsEC8IsCtMcrfnQD1zEdZuVR11NO41fkBDfDCeM5Jv_K9GARu-2Tw0vHESvPQy6TdtCpE9g8D9rjH0sJ_CZ7eFDQLcHd24ONfwuns4C5QuZ5-jjK2fhwuXsTlr1DmZG2ERwIkiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6579d2e780.mp4?token=rLaZb8JsgCmnegx3M5X31n8C5HFnbC2VLfeBC1K8icOpNX9nonYI6JmYlwlyWPXcv_BKRCJGt-8R-7hMpcsJ1iEhHQIXIHfbQWrTiLxq7OfldtQBivzDK5WM3h6yLEzGKaJ4fRONmS1MzXXz1E4aNecj0BmZDDS2cCaKQjzPGP0p-hNjLmqnJSNTYmWdnE4cDOnmyyBbPECN-krIJTuAjojWiNTBDcxlXYZJUwSi4tvAPy_21H81O3pkVrNZSg99Fke2ACyIXr1tp7Q4lVYQlwcyb01VbOqNU36A3f2r9qpMeaPqq-Ci371yuurQXC1h-rqUoHpNdSe2PE29HT2QbI9foYodUMA5bTX54J7bbKOrmzmmdF65EZphB6pBhdFbFqfCZAfkC0KyW20tuyValPq1Xp4RaOnqhu9fXvhmIX1wFEnWXGog5zZJhnjmn7jC9xrMot9Hncz0WBesVjj4VESvrVHBPqcXe8ONbNlL61LMGow68k7t33doXZ-AelphvzeELnR6Dyw-zV-9yy1k2t7PWQKzQGIUOTlZBsEC8IsCtMcrfnQD1zEdZuVR11NO41fkBDfDCeM5Jv_K9GARu-2Tw0vHESvPQy6TdtCpE9g8D9rjH0sJ_CZ7eFDQLcHd24ONfwuns4C5QuZ5-jjK2fhwuXsTlr1DmZG2ERwIkiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت تلخ یک تولیدکننده در نشست ستاد تسهیل منطقه کاشان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/Futball180TV/89957" target="_blank">📅 23:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89956">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltzK4VbRzjnKVy2poGVHMphLR8towjURJRl1VQkTbbYeYZHYKQqcjII6N0UVGAPlIdkngPMkQdYHx3pCKihIs3udLlxx_XmuZM_hL_oMjfDlk6ATszeNyKvoMcb5UuaMGaHueTST5lGQlFja2bJy6TRsSfDE2E33RtJ-xhF03EhEQdwWwzzqjv0t3agVcvxv9nLrzt3RB91sr8LigOcuBzWmR7VRNyuR7U8RjNUMwwZunCb-grabMAWzsui3nI5gsXlD38Ldk2UeWgHJq7Gjc8mq4nz73_ImC2VNxvWqHCVuXfFo6JGk2VR62mt5iIzOSUR_QwFnL_xpy7-BLMiP7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇪
فهرست تیم‌ملی سوئد برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/Futball180TV/89956" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89955">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6k_TrMZJ8klD4XGsKNY-_i6BX5pyzpnGTDY9kHx5ai18T8T5XDNgLhP4dp5qesRnTis-wxk-Q42vkVrnXtsxH3mtHVzR-MW4wFod7a4pi2NHCsbvT_Vfl-Da5FZNn-E2Y6tR1tLUVG1ERddbKEc5XLPh84wjiROZXNgXH5Xc6Xg91BGclbwt0nVCIgpOAnbcnEwzP7mv0gV5J81ZbnoL4p4F-9LV7lfbNcvDRzPgkFtU8gSQVvI9aXySvBYDcXYCLlShn8ADe-qsicklhAZkyAX_c3uBq7bDjwnxRR_HJDPZrs2ee4awo_NpEZEv10tNy0lemScbrOR5ByfDAzMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست فرانسه برای جام جهانی بدون حضور کاماوینگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/Futball180TV/89955" target="_blank">📅 23:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89954">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7cda28878.mp4?token=AV_A3V-8Nld6bx9UMru-RcosH9Rn_w4rTi_MQBUG0-8ryKghVQMr0XVZBWecit6UVooUJ1BdXGgeTZbJCDGdBe3iuQT7EV6xGtLZ_xVUxfJkhkx1oR3vUI9-iyJVG4DOu2iC_ohpWYjLku3QHIzKur4gbQLr4cXsl5-XAQBv0YlDTd0aG8WeqczWIJ2-m_xhAXVeDCrMZ07Js_iPEfm7wjSNDTWdceLSVkB4z8lqLJuet2LRmOnzGymVtbnysq_M5Dv3Kqn44KzYS8hyMTi732EIwYrZ3PB0BqGdQSqGVJaTdbBB1FB6ncEp6Mvbl-gTJubQV0uP9o-vwzkNE-AtrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7cda28878.mp4?token=AV_A3V-8Nld6bx9UMru-RcosH9Rn_w4rTi_MQBUG0-8ryKghVQMr0XVZBWecit6UVooUJ1BdXGgeTZbJCDGdBe3iuQT7EV6xGtLZ_xVUxfJkhkx1oR3vUI9-iyJVG4DOu2iC_ohpWYjLku3QHIzKur4gbQLr4cXsl5-XAQBv0YlDTd0aG8WeqczWIJ2-m_xhAXVeDCrMZ07Js_iPEfm7wjSNDTWdceLSVkB4z8lqLJuet2LRmOnzGymVtbnysq_M5Dv3Kqn44KzYS8hyMTi732EIwYrZ3PB0BqGdQSqGVJaTdbBB1FB6ncEp6Mvbl-gTJubQV0uP9o-vwzkNE-AtrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کاتس وزیر دفاع اسرائیل  :
ماموریت ما کامل نشده است.
ما برای احتمال اینکه ممکن است مجبور به اقدام دوباره شویم - شاید حتی به زودی - آماده‌ایم.
اگر اهداف تأمین نشوند، دوباره اقدام خواهیم کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/89954" target="_blank">📅 22:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89951">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEvqV-VxMKscoisb9O28fSEP4d6yEwLL0LrxzVPFvmT0CtJnyUvlDLs_Lmmvp-1YkYmYjt_6p8c9-mg26_wgGqAmZdIvLFC3vROkhwyrG9H2mZK6rHjDT2X7msZxcCoVS-K-u_8jXJvI0mQGev2kIHdwIE18Tj4T1fyx-NHuofRbL4T5LVvZcnrYr-tVrTTnGm9EhUnCM5tfDOXv4JgxiR6gBX6Y2VBBeYOMMGGoP82K3OBwoPGp_FwuC8-bXerXd_phFHXsjOh7BdtvbBmEvJQBTD4N6-0z_lq0OV59e3lnpOsSfaDvmKPlN5KDPz23xsMspnoYpyx4E9OPUIVQ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
قرارداد آنجلوتی با برزیل تا 2030 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/89951" target="_blank">📅 20:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89950">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVn8mTLERHqmcpF729M1zPahhWLHNk9LzLSusc2_S9YqBdm-zVxMk25oZZU6Mg-3JfwjXkxCSiHr6KY8GbCLk_xcXuVUPNLQfbRicBI90Jh7kxonD8nLYWxQYkXr-Fq2NWJsq0wpIJPNsGoS4mnbMwSkJkoddaCJVj6MMz64cgsfGF0DlYaYvB-0Eo3cQ_GAbtUF8mVZObqIb4etrDjxljh7LmN-N651z5FG-NhrXtHMVHBRoerBEY2kO73EY4LgUntaBUnPGnYO2-BYqrEs39kVrAVtKWDAw21KTN2Np_t7LN8xkKppbKxCp7FkCN9HNtHN0gLYQYiKyTHlww-1bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
فهرست‌ابتدایی کلمبیا برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/Futball180TV/89950" target="_blank">📅 19:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89949">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🔵
یاسر‌آسانی در گفتگو با مدیران استقلال اعلام کرده که بلافاصله پس از پایان جنگ به ایران برمی‌گردد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/Futball180TV/89949" target="_blank">📅 19:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89948">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djq64NQ3F59IiSzUzgO-JAzBu_Hd3hkWSnd0WQ42oP5hBP7Jcf6s7P6tKyYPIKfbl3Yx2IkIAWwryCSFx5QXtqvCfyIg5CJ2U6WYOe9v40QF0tUsI0akL-50eIgg7V8_wYiUVeRovDmINjaWDooftXCAGnBb7jfAvSxLjEUkEpRilj-dWbZSG8GvC-0o3Pt_PSKkQSy0VRRbbhXChx1gipbLyqkfXniGPDO9ntKL6FjCo2BaifXG1wrlH3xfd9SbSTloeMRTWaJ8TjjpyCZsDj-LjK27ViZric79Ui-jf6uF2ZA1CGXn-zJ6jl2MWIJbHzgY6Iqgs1MF5L-ZOn47mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ژائو پدرو ستاره تیم فوتبال چلسی هدف‌بعدی نقل‌وانتقالات بارسلونا در صورت عدم جذب آلوارز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/89948" target="_blank">📅 19:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89947">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/173bf1e753.mp4?token=INs65be6pg5VB3Ji1IWxosSoCQ3B7Uq6OY36Tn7JHq1JrFa1GncRG_CQh97Z_RM_coN-UIq_1PzlIv1qtsnCY_26LZVvfTUdX6JQdLhzr8NEVHPjT0JL8xNApJDj6KkyNGmZlsV-8RJl7gk0q6vqT1V9K8SX1-tT7HcOGRc-HjhHG_jrn-weN8g9EowAwlX6m3wX3z3Qc5ok7izfkvKkSt5tPZFUHe4TWL3zV0q4BwCh1Q5yuDEJa-_0i1nVOun8iCIu378UmhPw4II3J8PChrMue9s5jLlpBMEEnT6e4tn2L1s6sV-Yf62Q-0rRnqa1_BwO06Q_RzBOxsXD4TWrn55OwemNTExPy5-pzLNVVCmY6870b7sLvI6B7czoAcJN4lFp71tvN1gPSgiZBGFjyEOcNbQYqRHrUi99qm1qxlYjrEnlegQ56bAXOR2jyLPxnz5ve3-Xm9-vvw2LRKf1cLZpE8xcpBMA89YzRK1zHrlderPslvzvNHWJf06NgFOibUH2dtivdYH82tIcHUIelrk9Go5wMCrM9cqmcMKfrxgr9RPV_4hOYwPJvFa8PpDNzlJUDyDN5UsS__VVYu_0PU8ak5_REx2BWziHmGlIebD-dCd9jMYCxfa3SCDOmak2TvivPyLsXZ5QlC9wWr652RC6-JF50SXxVyRx5-o-5dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/173bf1e753.mp4?token=INs65be6pg5VB3Ji1IWxosSoCQ3B7Uq6OY36Tn7JHq1JrFa1GncRG_CQh97Z_RM_coN-UIq_1PzlIv1qtsnCY_26LZVvfTUdX6JQdLhzr8NEVHPjT0JL8xNApJDj6KkyNGmZlsV-8RJl7gk0q6vqT1V9K8SX1-tT7HcOGRc-HjhHG_jrn-weN8g9EowAwlX6m3wX3z3Qc5ok7izfkvKkSt5tPZFUHe4TWL3zV0q4BwCh1Q5yuDEJa-_0i1nVOun8iCIu378UmhPw4II3J8PChrMue9s5jLlpBMEEnT6e4tn2L1s6sV-Yf62Q-0rRnqa1_BwO06Q_RzBOxsXD4TWrn55OwemNTExPy5-pzLNVVCmY6870b7sLvI6B7czoAcJN4lFp71tvN1gPSgiZBGFjyEOcNbQYqRHrUi99qm1qxlYjrEnlegQ56bAXOR2jyLPxnz5ve3-Xm9-vvw2LRKf1cLZpE8xcpBMA89YzRK1zHrlderPslvzvNHWJf06NgFOibUH2dtivdYH82tIcHUIelrk9Go5wMCrM9cqmcMKfrxgr9RPV_4hOYwPJvFa8PpDNzlJUDyDN5UsS__VVYu_0PU8ak5_REx2BWziHmGlIebD-dCd9jMYCxfa3SCDOmak2TvivPyLsXZ5QlC9wWr652RC6-JF50SXxVyRx5-o-5dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ستاره روی لوگو فقط برای قهرمانی آسیاست؛
تاجرنیا: لیگ برگزار نشود، قهرمانی حق استقلال است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/Futball180TV/89947" target="_blank">📅 17:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89946">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NH9jefXfrKttUQIo8aHPuidpvDs7bIzLgRrTP24anuxMfj6nihIaXKq52oFCiMhU1lgCjzfgNWV4uiowZO9vb7QqZ7xs6ZvdiEmF6pOfc5cbM94jW0lyZrwaC_G9_8UocrfLH9zkNd175Hb4eBRQpsS9KzXBJd-7cN5hjq5Kp1DRaBc6qcYAwlhXxDbhqtz9jO-YsbKjnpjv_Zwd3QKo43Gs8DIhSwuozx0slLTrL4mpOcdYF5j3fs6zxdaW7Eyq9pmg06-6WpiciTprM0wpbRrhsp5POoKIkrdR-k-7-m0GVyE_7SIE0QbIi8c-YaQk1ySBffgWPzyMLzFcdHuG7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نامزدهای کسب‌عنوان بهترین بازیکن فصل لیگ‌برتر انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/Futball180TV/89946" target="_blank">📅 13:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89943">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e925e8e321.mp4?token=IzCPS69WfLXrKzZ_nmhSzX3iagn44vrEYnZNPvC_11qfE20FANF2H9W4VkJClqFz8iA_aKYR0u7gRk0B1U87BCFmUCVqdwO93_BrBcI-o49pnEd2D1KYMEt0Ar7ydWVACFbTT_xC19KLN0OJ5XuxRvhFtrN3GXpPpawn03_j3-sCyVFD6RQ6mZtXaNKSTDgXgxXAQTBAb-FlMC9xmcd9MpKpf1SPeXV6aH2vz3JSEjG2iMP2X3nGhTAVZAFe9NOjcyNjghWNki2w9t2yuXR6ZQoC7evaKNVZxFkHm20qYt-TNLOBXjhrBb7O9_ucwDWMVeBvuAEWnZ4bHuE8ezg6TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e925e8e321.mp4?token=IzCPS69WfLXrKzZ_nmhSzX3iagn44vrEYnZNPvC_11qfE20FANF2H9W4VkJClqFz8iA_aKYR0u7gRk0B1U87BCFmUCVqdwO93_BrBcI-o49pnEd2D1KYMEt0Ar7ydWVACFbTT_xC19KLN0OJ5XuxRvhFtrN3GXpPpawn03_j3-sCyVFD6RQ6mZtXaNKSTDgXgxXAQTBAb-FlMC9xmcd9MpKpf1SPeXV6aH2vz3JSEjG2iMP2X3nGhTAVZAFe9NOjcyNjghWNki2w9t2yuXR6ZQoC7evaKNVZxFkHm20qYt-TNLOBXjhrBb7O9_ucwDWMVeBvuAEWnZ4bHuE8ezg6TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تاج: AFC چون زمان نداشت با پیشنهاد ایران برای اعلام سهمیه‌ها موافقت نکرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/Futball180TV/89943" target="_blank">📅 12:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89942">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKwEeYqxK65Lwvn7ZiOxUpsBhZDjtg8o-fMEN9VkG2p6ALA4qbrlgGJlq-oKuyo_EO8eza7U_oMXbyKZS3D30opxhwUfC2IzKbksZes0QIe7123z7Ioi_zab9A-tueg6yuyrp62X0uUkLBaTCFLtLfy7Nr3cEZfcz6Q95n-duT-j87gueTCfNCLs6Y_QybxotXA5TO303lgpgb2pZTYBarXV5LUkWJWayGLMtUPPva9NyUgZMyeO8t7kpKa4HmIC7fcnCzfyMJVdf-LGHQodJhRpdjyQ5RP1oyuBiXvOluNQXTfUrcm2Ojf6J-tVWBxh_Nbt-AtQPwCDMxZm-ec4ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ژابی‌آلونسو به چلسی
🔜
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/89942" target="_blank">📅 12:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89941">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQ5ICF_tmY0xdZc_v6Jez9vFWugOkCwAcvmpySyhrVwouIiMIjeQ0NCK20A3kttXsgs6aSAp4steQJgme3jc-fZL2gZHAhtxMqAsBp0N31tKFJIoiH0jwUQPEIHFNr7o9F5ovRtP6DQVAnndarNXUs5Bw3-ntCf4AjSwR8NJvhiqmSG582ZWbWJqvXOr71tEAG7r9v0GgWGx2ddCUZjgGQOLr0J92L2unUAFAv0urTD2bXdVr4pHCE28F8pALWqsTClcwBc9BoB6pPP7NWJMhQVm8JN4BBeq9Sj91K74qcf9W-1_9O_8ZrBwUEeDl0PcUgjJ19jzfLAOTRhgOUc2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی از کیت اول فصل‌آینده منچستریونایتد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/Futball180TV/89941" target="_blank">📅 12:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89940">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWzUj_xhkHo_Sg141dfuEsWPcMaqm8cmD8jDfdwEUNE3uWpS7Nx8uiF4xw6Y2LJPkpngr_A20Gldheun7DqdVBKCcSQyZDQcDKA4pJUcIBKsRl4vI49aWwdUk2toZUlpBtS2LEmY9GSooqOBISUQogPfoyfd-hDMZvcDveeVY9bPhSNts86TFABP1n1FxaziBSNT4NifRcUykVKIVZmbYfoxciGqmQJHEAvFYNdonu4UDzoT1jWRY26deTOlAtUO76auVxqAzDpWTuxqlUAwUKcIXDcLUDMaMKjMMONRE9cpDErA1e_8274T7_ROYB5oFv3GSNGEFRfn0E6b_yRLrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام فیفا، در بین نیمه بازی فینال جام‌جهانی، شکیرا، مادونا و گروه BTS اجرا خواهند کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/Futball180TV/89940" target="_blank">📅 11:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89939">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdmHVoyxpubudSiQg0b8tPE8I6zVEWv-kRedFKhQhp911DvfEalopLZACJ713w7I32LnU2EppTWjORqgTzlVNZ-Wa_J1Pf91v8BuBmq8_-kWmBrOmX2boi6OdlrSP5f1I-YDZmGdlIKkYiV0UHePpIBnHHkJNbKV7PqhE0wksO0lapimGbyRO2ymLcR_P1zDg1GZFevoSwF62VBruptPN4FN8U9wdaA79WmkhcKoq4rNv5lHb_heaF0BQa17l9DtEJYkvX5NvrI8USxht7QQlkDxCE6FqmCo1VLzzytNnHqFsnM0A6Y5j9XIyAUQuEB4a3TrCEFa_6Vp71H6hqp-9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اعلام لیست نهایی بازیکنان تیم ملی نیوزیلند، یکی از رقبای ایران برای جام جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/Futball180TV/89939" target="_blank">📅 11:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89938">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smjmSY422KXo1RFvweP4wOjQpuuFGDPP24CNbzOWhkIB4N-ib-b9wlX_MumdjmpKkY4twOeQciv_ANpt__EwUCkF1wyJYUqs5CZzNtXFXelTPOyFKHEkVyH8cAVMhcuzq8j9MY7kRykktss3tZfBLho57qRmr5GoDsfoHw642OH2Y4kchcSA5Z7V_m-uHAJ2j4RmzQ7FyfQaDBViqMvNww2QqZTzIURMriWmiTSAuiYY5F9uAAOkX_CYX6BxKY-ZH7o_3y-Kg8os-Nbcs3CyTsrssZPy3J8Wj3D0_usn07-WI0NluRqJu6bcUN0J8e49WLqaFS_3Acz9qjiW_dVCVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نصرالله معین خبر خواندن سرود برای تیم جمهوری اسلامی را تکذیب کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/89938" target="_blank">📅 08:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89935">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBc38oRjK790-m9_O2Gqesnl6aymLbZhQ4_8VrliaHRGwuLhRb25V975-tZTzpvt4dBPWtqnGv9acSOwAX-pm5KfIVK6yb3APSOAYe4lczyvoZzvASMgnLRMtlz95tK3fA9BMBK4rzta9VTq3Rz4bucXej1wYZ174qXZousBeqlEou68V14V-ofGKyYfWC5PapE7hF604fvph7S4wOXLdKzcZdrUPO_HtP8Puz3qWqkNkgIyVPWDJnqaH99imlLLTMfpX310hTsysP05kwaSw0902jW96wTGG9QF-OzWw4cVNrV9x0-3cMno1BOdpcIV3S90kwbzTc6ZQxeZnKNWkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🇫🇷
پاری‌سن‌ژرمن قهرمان لیگ‌فرانسه شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/89935" target="_blank">📅 00:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89934">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGjIoo0pu2pwe5aIUUpR2RaVRQ_anscNtJdfs_As53vLZYvRX6tuSPdhpW1z2l7Zp5xA1HTV0UBRMWTMi7kQmjuPTiBbizC6Kh7kRS_B5wv4jDhItBdRYOaWeXU4C71Cew67pF1jwwX0wELPRT-tPV8WQXgMhzWcDdxaA-Dq5f5kEedhYsAb3wQ8pBVW2aSSI564eWMk7mJN30XYpB6BvrvU-sJq3CsZv5JwYCRUWPfYoUE9vYv3r0pNXyEMvOLHlY_MtV91lWqyHGLV9AJUo5dckIUGezyXDGRYkQiirvmE_NYAqo6xT4qPUQs8JWLBIQgShvJ8dbLPmg5mRjrVlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
اینتر با برتری دو بر صفر مقابل لاتزیو قهرمان کوپا ایتالیا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/Futball180TV/89934" target="_blank">📅 00:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89933">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSwSTTWEttpRXknSK1qCoeABHkuR0u7g_aIQXck7b5sQEc-5EobuyeoxdWm7AqWuz30cPX11htMnVDgeqp3ctewgMyzgj6WMFfbkpHYQwdiTWX6T4oT_LZlmXBFLfC5-Tb4Ds-0FxOxZzY20hNp83o5ffFsBd6Mc20FdXV6e3VQ00o6dwVrjrmh_T5qaWp-0J5mcAnQnV_IAHS9ukzx3QXE3xaY1tm7z8aAvVNT1iBMAeFnj0h6eoCQa4mURCo2lder-nDDJ81rAtJVKHdb3FZYOpV2A49RwPHZ_4xPDS-4L5spqVR68__uFyVdoE5v79P1A4cPD59q44k4twepfCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مایکل اولیسه به نخستین بازیکن بوندسلیگا از زمان جیدون سانچو تبدیل شد که در یک فصل بیش از ۱۵ گل و پاس گل به ثبت رسانده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/89933" target="_blank">📅 21:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89932">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXiwRkzSAhbL1CuIOapCPhzn_RI5H3OTWPJsVKn128RV2lY6yv-3Na4kCpzePJXdxfBIhIZvVUV_KcveiU-rkKdMYPHXMiducRw_Ll3qGJ8gGnZIgJ9h4wqpi6w2jRwB4BpMgfyXdL29OEAovOKEXm63yWF_dHT_JZon0hrZyT_uU70u0NG2Vxp5a2sdtCmQiTb4KtvRWjv6bzN_d3aySTDrAVrYslZgPzTjjCgQqwQLjlZ6pKGDbhRwcDQhWRCgsyq1Ai5gLRtk4y1TJ_vhECap5w1EDXv1KSMQ3q8bIGGK30leOE1BhwIFRGORg4PlX_E62AzTbKTEGOjG6b905Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار و عملکرد مارکوس رشفورد در بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/Futball180TV/89932" target="_blank">📅 20:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89929">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
باشگاه سلانگور قهرمان فوتبال مالزی با ارائه پیشنهادی خواستار جذب یاسر‌آسانی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/Futball180TV/89929" target="_blank">📅 17:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89928">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fe1DxpVC2r0GAbX29gWaNH3cn-WFr1JhPsUQ4by2pG8tJ9QJyQHvkDSE4IN0GkZjQXPwYA35Zk_PDJL8GPZJm0gCxr-qvXxAxJPKsj-cu8tcKf8RgOVcSoiNAu1SxrNgcgGG2YXAvCT996IgSH4Nmp5-YINYFBW80cuSo0ARhFaC71Js65FwOCElOHoLTMb_nYFvFXW-K1D9GBJ4B8mkOk-AliSN7q1ylOkudiAYOkvz8KT9ifQIsZB-SO2h9rF4rmA6B-ftX5jTCPKNNURcKeDA9YLwjIkExWFjunJivJlEYGqpzvAWrHFgHX0T2e15hH4k6fhMepjF4dtGhzAT5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
اتلتیکومادرید پیشنهاد تمدید قرارداد با افزایش دستمزد به آلوارز ارائه داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/Futball180TV/89928" target="_blank">📅 15:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89927">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oql98MPjzqd6_wPRvewKDAzfHZUwaWOgH3F1hlBfv-n4AKslax-cM9aP-ZAvahphXkXydkU51TukDQS24ldtmDH3keyOJMGGcs9C8zV-7K0HQYQAAdF_LfgbqEZoXjYBM72FJigjus6ofhKlBZTtp_Bex5gdcHamiFKXGGR-96Oweu0t9Azhi2IrfMvmMnBiAmOJ9OQsyqeZ8etg8qAGSGtG1jDuX-diKdiHVBuREfo_PtEHkvGMIwkczTcn1QsuBqCBp0fkVJYYrV5VqscRy1_2DTGcgZ4FIGV3PjuhvFDuALCwOtFKt2OdUhf2N9FXhTUG-4xlOWYKRgOAs3q7YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
باشگاه بایرن‌مونیخ درحال تکمیل قرارداد با آنتونی گوردون ستاره نیوکاسل برای فصل بعد است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/Futball180TV/89927" target="_blank">📅 13:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89926">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46b010d42.mp4?token=gnUTlmFgWYnIu-tO1GH4G5otxnbjo_ji6gwXPYYthCDfBcD3oRT40ytI8bOG_So63QagVZwCrWKUUMtgeoGaasS-MOmhW66_z_Dr_0rtEwAcA6eaCFwiBul51YOtvhVCxL8WUE4Sh91SC-kJLuAceHFT_4cJVMmIVxeMlFZYP35F95mRW8u_L1fPjgItbW3UTcprBl1V_-X2EOB7EVJLvpbCx81Nop-CYOKtjSQjF0xF0a1Kd_c_HrNdtLoxscot54kM5MMjlJmerXLULXugfSkUDhhnBNM5bBxe-88Uli6nghbPqeIeP8k1fT3D9LWGLrhH6Uu4-vEWChqaqLosjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46b010d42.mp4?token=gnUTlmFgWYnIu-tO1GH4G5otxnbjo_ji6gwXPYYthCDfBcD3oRT40ytI8bOG_So63QagVZwCrWKUUMtgeoGaasS-MOmhW66_z_Dr_0rtEwAcA6eaCFwiBul51YOtvhVCxL8WUE4Sh91SC-kJLuAceHFT_4cJVMmIVxeMlFZYP35F95mRW8u_L1fPjgItbW3UTcprBl1V_-X2EOB7EVJLvpbCx81Nop-CYOKtjSQjF0xF0a1Kd_c_HrNdtLoxscot54kM5MMjlJmerXLULXugfSkUDhhnBNM5bBxe-88Uli6nghbPqeIeP8k1fT3D9LWGLrhH6Uu4-vEWChqaqLosjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در ایام‌آتش‌بس درحال بازی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/Futball180TV/89926" target="_blank">📅 13:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89925">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0PezDb8iu0cFKKZRj3DDWXJuaBa_vawCoKZDGNbHkEw387We1h39jM7OxGwwgpL2HL7QUImqn5JTRCGato8q9PVVWlced0ZGUG48Inu4g-79StqkQepIpdCKaz3XpFEqqs80QgsZpfIRh_Hj7SdUjUG0pMtVltKkmpK1VtdyfYdBqHPGqyHfrnX70UPNnyLjMhfxSMsnoztyf6_smspCQUuP4e9SglVmw82nZOHXbMQAQLEGTGQ_DT3fp7vBB1reZAxEeCLwyZZgHoGeE9F3ogUH0D9DhBLwSnHOl6VIJkzCxEH9LsfsLk_IxhwuIHokASk6oMbwgINku8fdsNbmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
برخلاف اخبار منتشر شده، رئال تا این لحظه اقدامی برای جذب رودری نداشته و این بازیکن بزودی قراردادش با منچسترسیتی تمدید می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/Futball180TV/89925" target="_blank">📅 13:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89924">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUYSDpMj7EDz2mXz96N-9fYph0kJ0sIZDhKHG2TTk5enKOxERkuwJQUtZ9BfGB7p3GXu22QNYgCWHsqHGOVIKSDrzWovpGojspUyg3AnL_Qg-vEpi4S8gpCWHalF20a6C99gdjR-4eX7mDypoxGMEm6S5YMDMY2EJPAfKq_gIb7XQ-1bikTdOdCHkCtA0nQs0fFSY4x4f0efEJG9bCn7l9rwTKmjbE31ghp3xDI7APyCx2m_A7CSwgsA8foHx0vyverOt6m6RrEsKdOZarlPTCrYVzwIJ6_iD_u0gi6GhW7lSJnLRL-PCHaf5ANM9Cb3Gslufs1FH_Hci54Si4QQeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
یک خبرنگار مطرح لهستانی در خبری فوری اعلام کرد رابرت لواندوفسکی پایان فصل از بارسا رفتنی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/Futball180TV/89924" target="_blank">📅 12:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89923">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3vmgZDjeyvB_D6x78-bbFMtRR7Uho5t-f45Y-E3fFmhwot_lBZD53229u0ZWIMzpbIeyVDIt1qnty_d9-dxK4K0_f74l11UnRUVFUCpFF_neNxnd3h2hpqLgOnwzRkgeETp9qh-p6-M_f0gqt9y5SjpPURx_CfSh-gn1RFXzGxMfsFK0U_NKWhfwQ3WAKfZ21E6RR9VPBzeL5eMNYkOjC-bt_rxi4H2BaQULQdBEld64J7sCVGXzKnzH7MG6Fg1CVDxAzpeLofqlfq4UFpYm3OhghukFHiRkCbLWUu-dJxRu-6y0Xod1G42Xgai30hyPX3XPVfgHtKLkoQa9236ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فلوریان پلتنبرگ: قرارداد مانوئل نویر با بایرن‌مونیخ تا ژوئن سال 2027 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/Futball180TV/89923" target="_blank">📅 12:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89922">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heE2N3EOkiJc3jKpjRd4E7rHgVQrq9kVra486Os7ALMswJHOt657tzdZgWSr6GeoMiqL1pgD3rr84rHKRdC-dAHALskp22BlN5BzdqkO57Hlm4fzVfqr5dkYtH4gYh8AxTbXJ6AJBHoxDgkWoMoVCZbk64w2JTuFkXaBNFG9nj5G4tTHARUsMmhNdopTGJrJJyrQZFbwUeQYiF1nR3JueaI1058Jt9jTMsSwfe5Y0vCbBq5oA4EP9mYUiVwckNlU6C4EyhoDkV92Qy5N8So72Ms72DaO15fas_345jpzuTPiU3PWeJjHFcCOwV5s1cq2TuQSPNPUpBd0PEd1-SrIjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پاری‌سن‌ژرمن قصد دارد برای جذب فده والورده از رئال‌مادرید اقدام کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/89922" target="_blank">📅 12:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89921">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIN7DzOQcKvcbfKpcz7Nm7iZYkO1UXmsbZi1k_1UT5Pt9On-BFD0QaRhgRDgOQ2aBoEZUfwGMDruSICN6ihBaD6Hq29T7u1jlcvLwcHcDj8mFlftq6drq3p0JajoAm_RpafzUSJNahmqx_oB_c1OctMDhM6N-8az1U5BW1DrT2aYMiBnGWndbUd1kAdU7NRReIDj-ZYzOxYaA-6BagHnADnHc4UmAJzpCeTL3i1MyDTptGZsNsH81K9KBYX8hc1kCM1Npw-gT6TX8m8FqZR3Ln32yRwOyqS0v-NB0DpTYkUHhWCpo5i1IKWN-HW0DH5vNsmgwPslTLZtMj_4ultNTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
فهرست اولیه تیم ملی بلژیک برای جام جهانی ٢٠٢۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/Futball180TV/89921" target="_blank">📅 12:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89920">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8VVBMO0NF2i3NY9ZGaYAyjXdgaEcvvuFXy5HXneDJhv04mjtiXv_qE3PksBn290zueDudL_SbUgV6Gi2-UNXiZFXutDH_-4U6uQqxT_LpWUIl6ZoOw6R6IQIHcQaT8CrQ7hxYVLTE0I1Lkffj7trUWUZTq7XyJYG1iP8A0_-7DR3oxtsg56mz5z1QDwpw-e9pZjQ2fmpS6V9kWokI1VPu3Hs4yUkRmGnnf3snDqU4vYtxKEZYi3lFMdgQLyFocLgEle0K1WkSNwjPnBlET3cxNoaQRzpPkYlvvpD4SYT0GjpkaIhv2fHcvP4BgS_299B6yvs-LrUJ37cTB1aqDuOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پی اس جی مذاکره با اتلتیکو برای جذب آلوارز رو شروع کرده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/Futball180TV/89920" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89919">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89919" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/Futball180TV/89919" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89918">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTefQmlQrq7CloKm8kGNqz69kWPSTguixS-lgcdDmj4Pv1e4TfNwigemVo4kPOyQf5EODwYxGkHfj--kPizWAGMSCTihNkNxVHYG-dvK-iy_0zkVvzt9ez4gZVkzZDksTJOSKwI7NwUwKFgQvEZCadYXYF0bR5ld7DbzYmLQ3cXSdqvZwPD-Vy-a5CJzfdLgj4whJzB8aW6oFTChTNHYm6CqalV-6Ag2Ie7QTpoIe2xFyUcCgCjyD9-AkqE5tsd3Ojq1NBoNOU7RnfbrK7kQBDMUNKuQMl9n5BY6pAuFg7yBMrcSKUzJmAbFF7qTwL4qRlz2BEkizr7zVfE4T8eNLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/89918" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89917">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇶
آمریکا برای جام جهانی به پنج بازیکن تیم ملی عراق ویزا نداده.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/89917" target="_blank">📅 11:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89916">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745061c8fb.mp4?token=jMH0nZdafXFshvT3IR2aayVfLy4tYYTZ2u6SZf0N_vvv0v_o2n8rtIDHr3x96E6Ot54r1NSkFpsD9AXJ6PEM68vSLC10P8NLDZgL3Qx-8vGj59tRDxai4FEu6E8Zl_rivDRFU-r4eZ4oRQNItAeMjy8ftHxiUjp33yYJgOdXqkr4tzax__xzXltf7JN-Z6c7X-ewm0HXRVrEhpN9YoGW29P0m1CvLOz6C2RBOysb1AiTxszXHRfyDsIqpT6DBMzLWxGTy55-IN5d8Xo1fZ7gPTBGWs_Lz65ZAog0x-rJ3q3ta4pcY70-6DNf9VAhWH8ORkn-WRfbiZilAcMfKCAcRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745061c8fb.mp4?token=jMH0nZdafXFshvT3IR2aayVfLy4tYYTZ2u6SZf0N_vvv0v_o2n8rtIDHr3x96E6Ot54r1NSkFpsD9AXJ6PEM68vSLC10P8NLDZgL3Qx-8vGj59tRDxai4FEu6E8Zl_rivDRFU-r4eZ4oRQNItAeMjy8ftHxiUjp33yYJgOdXqkr4tzax__xzXltf7JN-Z6c7X-ewm0HXRVrEhpN9YoGW29P0m1CvLOz6C2RBOysb1AiTxszXHRfyDsIqpT6DBMzLWxGTy55-IN5d8Xo1fZ7gPTBGWs_Lz65ZAog0x-rJ3q3ta4pcY70-6DNf9VAhWH8ORkn-WRfbiZilAcMfKCAcRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درگیری هواداران الهلال روی سکوها در دیدار شب گذشته الهلال مقابل النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/89916" target="_blank">📅 11:54 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
