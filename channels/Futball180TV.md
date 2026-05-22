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
<img src="https://cdn4.telesco.pe/file/lmQZzzjwMmS3bUOrxjkxT1pYPwMmiHFuNet3BHCvsIEjCLbPqHLo6-G_4hxqWQMBdHGjyBWVqPED3eVrJUGIIcGRjqq288K2_bdC3VwnnrHAHaZ8F40zeYgip3fLyd2lpyPVeOzoZkngc4wuwWcfZq1A1WDqm36HRAGXLpX8W5ZpN8BQYHhFvIV2HM0mFbsvxTVYT5k_ICn8kz0KGiGRhSENEt0UUrB1XKAyDRM2R_xs3_CsSdJx3ddGKx6a_UUvcOLDZ9V4mM7gzHI40dDgeg9SSlN5C9AOwxDBhatpmw9vzT8WFMNCZhWl27cO1PDL8zeJUXK8p_uzDmlttKO4pQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 129K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 19:15:28</div>
<hr>

<div class="tg-post" id="msg-90149">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoAdmin</strong></div>
<div class="tg-text">⚠️
مدت این آفر 3 روز هست
⚠️
💎
پلن حرفه ای
1 گیگ : 280,000 ت
5 گیگ : 1,150,000ت
10 گیگ : 2,050,000ت
20 گیگ : 3,900,000ت
40 گیگ : 6,900,000ت
💎
پلن اقتصادی
5 گیگ : 850,000ت
10 گیگ : 1,600,000ت
20 گیگ : 2,800,000ت
40 گیگ : 5,100,000ت
🟢
کد تخفیف به صورت خودکار روی ربات فعال هست و نیاز به وارد کردن چیزی نیست
✈️
آیدی ربات جهت خرید :
@AmoAdmins_bot</div>
<div class="tg-footer">👁️ 188 · <a href="https://t.me/Futball180TV/90149" target="_blank">📅 18:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90148">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🔵
باشگاه استقلال مذاکرات مثبتی با آلومینیوم اراک برای جذب محمد خلیفه سنگربان جوان این تیم انجام داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/Futball180TV/90148" target="_blank">📅 17:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90147">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMRmR6M3WtiVKPwjtAMYe4oSlFwgIRvF1eiuhSfZ8o48PimvW7YvZm4Yvqn2mZMxD_CzKRCFAxvI8xJmNaHPW1nt-TA55QMBb2wamEvmxvvzPRKz1CytK4Hjpx8lzYvCatwXJvat9OjMxf2cdu2xfQRAO0cfOEkgmLhDgL76KtRRBj8iNiuPXE8UgK8fg8mH_a_3euzWU-EdvqZkjmH4-dpcXsYq67KH4ZSNHhg-m5nZmDpT8vPE9WPcTMHAdb0Jvvq3I2qjdcOZXl4P7slBZb29Iyz5AYBY8jvn3DXPzg2K4b7DwZPcgKx9RSKhfHk-E8cpWxmBj5xJX3Dy7miTkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب‌منتخب بازیکنان خط‌خورده انگلیس از فهرست توخل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/Futball180TV/90147" target="_blank">📅 14:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90146">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mr8Lh7xvCmrzVcO5qKt9gk0_lfaBFLuO1cjmYaybbRdrmHwNPpKvzO6491_w4yNfOzWq8D229DgdZHRoPkWm8fXhYv_rlGyUL9QYf0czJMTK0m3SPlRLu8WDfJg9dkkK6YAHHYgzaA1hr5mWE4-6YOIi7uFBWkURSnLC0ikaxRsISL9veSPeUy5BXPWk3i9WcsK-H1phmNCU3XTjCSmYLxGmgICNxJl9Fb2i-0krLaMg9nC7XKX8e9HUC3dATfRVUQz1FYkOKFbLj_H2OaQ7fHjVKLOfUiS5OnJzP-QnRTws0Qo7-UKCdXt6szWc85nmh7cg45WzWYrjrQcTbXWG-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی دوساله رسما سرمربی دائم منچستریونایتد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/Futball180TV/90146" target="_blank">📅 14:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90145">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDdWxkwaoUP1vlPl2dHESox5Vc7w7fd8xpJ_FFTPWah68MBEPXbzDWglIHO_-CBEvdf-l9GiqCC1DqtXHfioIpepDojo7u6RzF2qDKi33vSgPgeKncH2cJ7YcRDGMw0oQnXef2XXxJMpyD7DRVCOdNZSU5n01EpK8o99gnYQOqm87n5g7YiOR_W6LWDN_qD1c3Z96Xjbkx747REDd72YqUF5cCoNSkdzTHDIwwmKenktjyWAbj5j3f2twS7L9K1wtOgY-eiV5Y7nQbDis54CQsTcuvcv8sS-QiTu1ux1qU6h7or7-hDB6_kRmj0qXnqOYO3ob1YZ7P2Tma6sa14RBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمی
؛ پپ‌گواردیولا از سیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/Futball180TV/90145" target="_blank">📅 14:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90144">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90144" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/Futball180TV/90144" target="_blank">📅 14:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90143">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/om29V94C6VaksurzXCen93h8YHzeRremduOD78qN_qHv-YRCEQDVJcgePWGfZP2ZPSPKRzxNLkvE_DJ_V7dfTH1kjVOm_eFmb6SfMVbk_oZIi_YLxwGYsaxlfdVtP_ii6Z2geFr6sW9N5Bi99D0jHkAvpUwiwDAcMPCr7q0oPKHPzF6TTKIQDn8rVmiOzZ5mHiBAO2WwS-2H1qn1BGtOjJJhzlARYU0kMgww212WPAY90ZLG1ACjLIXsGP1d27ZmrbDb6THWI5Ts4gz0tKDOXlGzNzh2d7JWtyeS44BXrLK7MkaQXb524FR85tf8VC2YiJFzCvPTDBMzGGS6-F0jHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/Futball180TV/90143" target="_blank">📅 14:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90142">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست تیم‌ملی انگلیس برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/Futball180TV/90142" target="_blank">📅 12:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90141">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4mxATS5s2_MnzaK1AE-pqt--wBAToGJnRJBSeyS_KRb-Ax6noKsDUxIen7M4b8RnkEjpclVFWQOl_Z7wOedtT4EQtum4vxG0V07yajHvEgrHxpw-niqLOB-WzsUwLTXvgXOT_14rUk2bKfHnM-komTBeqDmyVx8-uysEPTWElRFYkzXxilV3GVHNG3Qbf0UwzD5g4t0apdOuFo32xmg2UFyVXsSCPueE8dMH94kTrY0nt6dU2Zfg5p3luEz-SCTgAD0OVctuXurtWGasUOJtx8TSlRBTD8O60fA0WzN_8Ui3whzqbEkzeOeVouCJI5KlSAgIcTBNbvy90IHCIjmOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست تیم‌ملی انگلیس برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/Futball180TV/90141" target="_blank">📅 12:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90140">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇪🇸
آربلوا: با عشق و احترام فراوان،‌ فرداشب پس از بازی رئال‌مادرید را ترک‌ خواهم کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/Futball180TV/90140" target="_blank">📅 12:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90139">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🟡
باشگاه سپاهان با انتشار اطلاعیه‌ای با کنایه فراوان به سایر تیم‌ها، عدم صدور مجوز حرفه‌ای خود را تایید کرد و بدین‌ترتیب باید شاهد تیم جایگزین برای طلایی‌پوشان در آسیا باشیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/Futball180TV/90139" target="_blank">📅 12:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90138">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
❌
در صورت عدم کسب مجوز حرفه‌ای توسط سپاهان، یک تیم از میان گل‌گهر، چادرملو و حتی پرسپولیس راهی سطح دوم آسیا خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/Futball180TV/90138" target="_blank">📅 12:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90137">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bq6s36ukWqMNLPhGwlCJYEPZMom8KpCO9J_RDznjIe2_J2DkomHdhm-8iv0tSYwKX_abODzKseFlrZkZyt-yzcGWU_LsKd58EbzLoQxOc_EL4S4KNfwEgW4ggZKKBHdnSSWyYNIn-YTH5Ivw-qRm4kScpHYKtF54sacf9Jl6jyZy4r3Lt012leoLdHxO-04PvODIktmNywY_LQA1-khvYN7ouhVStIbOSBbK58DD8n6td1xj6Es5ymCrxhfacdWKJQRVmvkVn0AUisgSSIao1swCuBvHuI6sg7x0q_2a1zw8STDKShusNzcC-vK-T6XOGcS-o6CuN7Jxl10d6M_gxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کیت‌اول تیم‌فوتبال میلان برای فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/Futball180TV/90137" target="_blank">📅 11:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90136">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
❌
در صورت عدم کسب مجوز حرفه‌ای توسط سپاهان، یک تیم از میان گل‌گهر، چادرملو و حتی پرسپولیس راهی سطح دوم آسیا خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/Futball180TV/90136" target="_blank">📅 11:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90135">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rug-98dmxZ2MoAex0pIBSwgS0BFHqaH5U57tqM75umX2haUgua6vdPu7kD_WIyeW7nm3yL9sUDxA06Z8awx88euiz4waKJQvOepUb0MPu_2tY05J194Cl1BcaWdEiI3IIlhJPuOHm7kMjAvyXt28osJhYCdlTC_hHpK572xTQR5SzIDx_bwfw_iJl83aGYYg5uRdU4hAP4Nl0tQp-JVLVgFDotyYRQC-C34zAx5h09OiQ8RA0lZjOQg8HCQdlLB-NHTVNn7jr0uhLWO4zNxPeN-A3Yc4TnqzF1Ump76pt87FessO8-TQAr8Ff7AjaVaR8DpGn207mwPvCbjm2u2fPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
آرنولد ستاره خط دفاعی رئال‌مادرید از لیست انگلیس برای جام‌جهانی خط خورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/Futball180TV/90135" target="_blank">📅 10:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90134">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGDBkeRup948JIFnfcdNgT-tj51V9YjkoIys3L219ob4prrtLfGFsM-odoNVzuWE2X9gg7uqYiz-IlTSgZLzTLOYfIf4E-QV261WP7zh8NXhWBexDPCXELHi_BgquFpFWsSZe4usKracLjdtrZxZtnKfVeHcvdbc2Kj6oRJ3C_Hf7TGXNuqHcd0toeAjYFfAvpbdfIDEe9WtISqxmrzcug3U0LvHn9NyL_wGimecf7fxQUH7kJWGdxPuqXuPmPQRIBi7aUn6ULI2WgejdjdH3tqcvjepYouq0imANbAvjupCA6Mh2LzRri11yRAptfoXtxCBcU-jwMZi633MoTJrzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کارنامه بازارهای کشور در اردیبهشت ماه:
دلار ۱۸%+
💵
طلا ۱۱%+
🥇
بورس ۱.۷%+
📊
مسکن ۱۷%+
🏠
خودروی داخلی ۴۵%+
🚗
خودروی خارجی ۲۲%+
🚘
بیت کوین ۱%+ دلاری
🪙
اوراق بدهی ۳.۳%+
📜
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/Futball180TV/90134" target="_blank">📅 10:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90133">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90133" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/Futball180TV/90133" target="_blank">📅 02:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90132">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwmbzXIVWr3nktXDUHbOFOGtt35icFhDPY2XVaxHs9lnQ8iRCvZTt-mqPk5l4b72y9GvXdmqH0pyGPPk1vXrl_Wvmtyy4sFcGCiZHajmq7J1p493Zl7P_0ODl5zTBUb1gAyKS1Vs7uAf4cTlzhplpifP1MQTRFBvUshFhYAIKUQIpSEoCZAIsWcEuKdFVdJI-of0oFCfDV6LukjcO2OLJKGEsgdd2N5rD7ta_GAyT6q4_MdTqXiqsfvBO-tWWLeet93urUZuWdgVntiYvac2S5lgHHUMyaJpOMQEMOtzvKknbXla4pd0uizccJ2FIjGLk4VUpKjAcdNmh17_piTagg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
با پیش‌بینی روی مسابقات افسانه‌ای Roland Garros در پروموی Grand Slam Tournaments، فری‌بت‌های تضمینی و شانس برنده شدن جوایز بزرگ رو به دست بیارین!
🏆
جوایز ویژه قرعه‌کشی:
📱
گوشی iPhone 17 Pro Max
📱
گوشی Samsung Galaxy Z Flip7
⌚️
ساعت Apple Watch Ultra 2
🎧
هدفون Samsung Galaxy Buds3 Pro
🎫
فری‌بت و امتیازهای بونوس
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
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/Futball180TV/90132" target="_blank">📅 02:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90131">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sn7qI8AEOYa2PEysKexfp63-O1WS-sSGo0PNNGfhIErcrGZrCiXcXvlmYtPIWHFFuV6C91H0OC5GOZfkjdJ3V2VoG5ELuWvlkSOEofIT8cVMJ0TAqy9iUzjs35vkGH6XJAnnDbKWlhXIqFadqJVqGBuaSSWXIfkXV98RK9Y22Ld1V5Pdvu17Y9hUEq8ghPBpDpOSpRNQLe4ndCAL_TjvI4tnVs_PFuoMjneTc4snWTBFV28Y5fPmQgHcOVcRV3HSIxER3z2w-J2A0nKeroUWp7C10gBw4zB-fdjSLQJWWhcMxAZ89nu_Jd7MSTUWfZvbCxGueHriJ8d-oVFMOSAnsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
دستیار هوشمند پیش‌بینی بت‌فوروارد
✅
🔥
با قابلیت جدید هوش مصنوعی بت‌فوروارد، تجربه‌ای حرفه‌ای‌، دقیق‌ و سریع‌تر از پیش‌بینی‌های ورزشی داشته باشید. این سیستم با بهره‌گیری از AI امکان تحلیل بهتر مسابقات و تصمیم‌گیری هوشمندانه‌تر را برای شما فراهم می‌کند.
🎯
تحلیل دقیق مسابقات با هوش مصنوعی
📈
بررسی آمار، داده‌ها و اطلاعات بازی‌ها
⚡️
ثبت سریع پیش‌بینی تنها با یک کلیک
🧠
چت با هوش مصنوعی برای دریافت تحلیل حرفه‌ای
🔥
استفاده از ابزار پیش‌بینی‌ساز برای انتخابی دقیق‌تر
🎲
ترکیب قدرت هوش مصنوعی با هیجان پیش‌بینی ورزشی
⏩
با دستیار هوشمند بت‌فوروارد تحلیل کنید، سریع‌تر تصمیم بگیرید و حرفه‌ای‌تر پیش‌بینی ثبت کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/Futball180TV/90131" target="_blank">📅 01:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90130">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90dbd94917.mp4?token=GYNC1-uXpWhLNN-99VSwjMqH7ffqlld12QVmmxmBXq_6tbYJuaV7iD0XhKJVJdr0_bBFSfs4w6gCoFDtGVmcejO1mjISiLez_-JiEJQaVjWCjwETXx3xR8moHGNJOVASh_27L1D4zvLN4XMiOaff-PJ6fqjZODHAk1kL_JvQUBXOijocE-AUWrYKbnJ5oOlR_s9Dzr0EzUiQM_MDPXNG5f8qcAp-uANMyIf3wfTOvAgBbXeojQzKxiaZ4tJF5dt3g9bLKyfojE8pPHWFG__z9fQ0mhXLy986n9eoM5Zlvwb6D3J09rQK_h-lcqZNORnIs6m9vz9qrhRqLHbMVtUk0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90dbd94917.mp4?token=GYNC1-uXpWhLNN-99VSwjMqH7ffqlld12QVmmxmBXq_6tbYJuaV7iD0XhKJVJdr0_bBFSfs4w6gCoFDtGVmcejO1mjISiLez_-JiEJQaVjWCjwETXx3xR8moHGNJOVASh_27L1D4zvLN4XMiOaff-PJ6fqjZODHAk1kL_JvQUBXOijocE-AUWrYKbnJ5oOlR_s9Dzr0EzUiQM_MDPXNG5f8qcAp-uANMyIf3wfTOvAgBbXeojQzKxiaZ4tJF5dt3g9bLKyfojE8pPHWFG__z9fQ0mhXLy986n9eoM5Zlvwb6D3J09rQK_h-lcqZNORnIs6m9vz9qrhRqLHbMVtUk0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی فوق‌العاده رونالدو پس از قهرمانی در عربستان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/Futball180TV/90130" target="_blank">📅 00:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90129">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIfh36ICJdxBqDKFwwdSqKSuTELVgPNTf-CvBq6edG7PpwPAAAOV1XDwoDRrC9XQ-zwhEK1DGfg6RvUXUC3mOO7kt1S2krMyj3gBADCIl0SQ11vBlxKLOm9aAXDQI5eEzmC9rSyR7OdmVNu2IC7Fizr7W_WhmsYPMw91Edvs-1H6K6bgG4jZlmFwfM3o_I4H5AvHOFspx97M7WAHgRfThqojHS3J7eDh5N3uspkSPfQtsTz32H9Ax8FPKF0BDURAjLhSBagaPyC5QjNoEHYYJHj08WdJjUodBc3TJtveZEHn_KxR0dAHjJZELOIKBmF5W8JsZC02EU36hqIe-Ut3og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
النصر قهرمان لیگ‌عربستان شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/Futball180TV/90129" target="_blank">📅 23:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90128">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKtK2GiOFTxscUWeO7Z-gZITVqO4SZ46RD-966WjUpoaIeNeLd3ouAN0epAjE4_wR1Q9m6qQA52eJheeYzTe1QW6ayvMPSozWVXxbv0xaeI9fxKVKN4BfB1YR-bh4MxfliwnwEj3ld2NnWOF9lNQiMn9UNn7nbTpm6KCOO9C-3DOBI92Vx-7HcF_zcmurwpFggEwM7QYjhykUQjmYYDvo4Yt6oJE1pe6OAsBiEb5LxDznnao01O_OZ9hRxmGNNJVG0j77JEjU5fCsW-6fpjw_hh3fW9Swo_w2TC5YhwhilxzIfe1IZYBRPRaCu29_Pedgd2QTb1fhwwigO0sAHlRMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقدیم گل کریس‌رونالدو به جورجینا همسرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/90128" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90127">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9421ab7b51.mp4?token=Y8xsAy4WHfBmjTG-KteYP8Qsn2rBaSrqtT0loJIwyC1csoNuudbXjCcFiOscsb25CrE2AGedFVBqGAzWEOHSlBhaH4dBB1vhlbiWgJKbOc2Vk4oj6VN3M9Krt0ZuwBMcRqBeet3iNsG-1sYfwSYm3foBDpaIZjl7QVILujXtJn1wAGKlF4oJOEmCWA5A8CLkEiHe4uamO-JQCZ5C7KNRBgl2B2cdqsy1bNZ_Kdi_ALIfHBmfqhI9Fzn4uOGWFj20wd30sZSypYH1LgMi_YPwElHiSO4pjwWF_5bQDsCDmghgu4YryPibY4CeMMre1AseMTHj1-CtosTaVR-84XFNehtLIEo4Wr2oUFeR62oVRqgfyRBwU0Cx7c2TorjYzMpsVjFluYEwpPr62uPxBvAV6OmVI1FrhNuDHVRoKCxPVxTv8pfv5qreyg5SXpX_Uwgu7avOs16t2057_xPK8ACct4NW_tYMkqskh3KCjYkUlkGZOlKfId5e-Q0HcmGbBvOe5RXj0g39TA6D3Nk0JhcVfxSwvz4b_zMUCZKRCT5rmu7ctDh8iiu_ZwgD6Xl7sikyRQz9xQzbW-S_NgZyf8GXZA4oN0C99-gG7c5sKtEjc4EQPe4rUlRzDwp9QtZWjZRr7kqPQRoGWtDwYdkQ5KPYr6_f3y5E0tFzH1rO6lrGP0o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9421ab7b51.mp4?token=Y8xsAy4WHfBmjTG-KteYP8Qsn2rBaSrqtT0loJIwyC1csoNuudbXjCcFiOscsb25CrE2AGedFVBqGAzWEOHSlBhaH4dBB1vhlbiWgJKbOc2Vk4oj6VN3M9Krt0ZuwBMcRqBeet3iNsG-1sYfwSYm3foBDpaIZjl7QVILujXtJn1wAGKlF4oJOEmCWA5A8CLkEiHe4uamO-JQCZ5C7KNRBgl2B2cdqsy1bNZ_Kdi_ALIfHBmfqhI9Fzn4uOGWFj20wd30sZSypYH1LgMi_YPwElHiSO4pjwWF_5bQDsCDmghgu4YryPibY4CeMMre1AseMTHj1-CtosTaVR-84XFNehtLIEo4Wr2oUFeR62oVRqgfyRBwU0Cx7c2TorjYzMpsVjFluYEwpPr62uPxBvAV6OmVI1FrhNuDHVRoKCxPVxTv8pfv5qreyg5SXpX_Uwgu7avOs16t2057_xPK8ACct4NW_tYMkqskh3KCjYkUlkGZOlKfId5e-Q0HcmGbBvOe5RXj0g39TA6D3Nk0JhcVfxSwvz4b_zMUCZKRCT5rmu7ctDh8iiu_ZwgD6Xl7sikyRQz9xQzbW-S_NgZyf8GXZA4oN0C99-gG7c5sKtEjc4EQPe4rUlRzDwp9QtZWjZRr7kqPQRoGWtDwYdkQ5KPYr6_f3y5E0tFzH1rO6lrGP0o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبل رونالدو در دیدار امشب النصر مقابل ضمک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/Futball180TV/90127" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90126">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92cbf0b75a.mp4?token=GQRja16rPa9RJojnr8tCYcwkvS4xx60KXt_Tq1J67sJl96ks-YORUHbTfma37lMaHhlwNMPodCXQcyDvNKtSlE49S5-jcyBLltYs9jP5a9C_urLq9AhxJ8tumy3MZDVnZuNlJ7b3AdsnXR5R0BHIUNN8vt0OJHDwUIF091jxzwxrtBu9CuHz4ZSnAAN_g6pTfGJ5GzMbiH5jZEXmnVQyWqTAngTo68rLsDh1dkVTBxkteQnKveNWdEUj2Ke8SbsxUd4vxwY6L0rzk-tZDBmy7scgqpU1fs9m3VNMV54iqpIyfrURgdXuEITPTbuhXQsVgJbDYQl_3Hhay4h1Rm0ShQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92cbf0b75a.mp4?token=GQRja16rPa9RJojnr8tCYcwkvS4xx60KXt_Tq1J67sJl96ks-YORUHbTfma37lMaHhlwNMPodCXQcyDvNKtSlE49S5-jcyBLltYs9jP5a9C_urLq9AhxJ8tumy3MZDVnZuNlJ7b3AdsnXR5R0BHIUNN8vt0OJHDwUIF091jxzwxrtBu9CuHz4ZSnAAN_g6pTfGJ5GzMbiH5jZEXmnVQyWqTAngTo68rLsDh1dkVTBxkteQnKveNWdEUj2Ke8SbsxUd4vxwY6L0rzk-tZDBmy7scgqpU1fs9m3VNMV54iqpIyfrURgdXuEITPTbuhXQsVgJbDYQl_3Hhay4h1Rm0ShQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
سوپرگل کریس‌رونالدو برای النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/90126" target="_blank">📅 22:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90125">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlHvcCq8chlHFRqB0ST76sJaZDFvBcjsA8WUnVCTUl9SXoAa7em3OP_ixl_n0O5K_OQRb2SElWdT6OCcekgQ4L2MmOFy-tyC2CAYEFjo91Yy2Hqn1XOjlQGMIRqbqC9APPUXDWm4IiWmiFUAhkr5kmzNhQ7slyeh9GIvQXtgWkUyZXu_SvZT2OLd93VbkogfiwyNeoo23lWnTGpupCtH-LNftmXmzXjaKs7UbM9wqkBValhNiaQ007bANg1VW47kUtYNCBtqCL3yF5qUU3fR2cha-cLhbNeEIYVLjbizzbuST4ivF09ZVDBlLJraEQJyIZoWbg0fXr9uMcW4Wjxafw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚬
فیفا قصد داره جام جهانی ۲۰۳۰ را با ۶۶ کشور برگزار بکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/Futball180TV/90125" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90124">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dM9DI21WTGdex8M5NgL9HdHQEwgrxyMY5fzEk26RBwc6BHzDyCgQgS3_wyXU2pzNunIoXvzVhfn0mCJi-8Y3Lczj4ZLqhqbihNokZB_rJqlq7-4y-k--wY37qfSIAj0kv94hnJ4rmI69Q-VqNMbH_5TgPwG-QViadASUz8B5K-WCcT0NSRzUaFmNCYqf4ZF1YVFdMG-HtJ29kYzPAJHO8zN_p15VdnCfZo8PWdpHzSThsZpS7znqX570ol3SMuHASNlogvHzC0nvvQzrRs4GO_6zdbsUL5ssJ-hsgezCfWP4Qm8Ws7QE8KLNJGA1h7dcVu_vhQyIIPpeVROvRHBR4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دوس‌دخترهای لامین‌یامال در سه سال اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/Futball180TV/90124" target="_blank">📅 19:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90123">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90123" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/90123" target="_blank">📅 19:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90122">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCTqY30e0Qf1m1quRxCNlupCxSrbyi8LV_SW33ykAdWX2_p_ndg_o6jBdMHkLx73yW6kUjCAjXlTDldujxDzV8yYED07ZtIfjPcZlFPnc8YyNC4rZDX7lvy7U8u4vLayovkoCaLCKIOvjXFahjgywFxo5OfMuuVynDpU364RHfMjwXGx0eGavxl2ml7fSYOgvQnwVBR-nPP98AzPduqoLN_ThZoklQkVYNF4GLZdh97G3ZkI3m7dSnQ5hb7emmsvNns2zW3pVRTRiPlMF2snn3xJnLxYgSav6bwfnEfOKCal4Zs8NXkITosOm4E7RyVQWSZS5KRPiUqNHBqA5QzaaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
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
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/Futball180TV/90122" target="_blank">📅 19:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90121">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5UKaMSq511cHYUADSAKJND5hr7dLol9x-QY8-AWc1LFVWFOy3NaEak2XQWGcBV_TG0l16oFM630HuYsKMDgeCwLjnaeSJ9q5STlGs684XnQHhkLz-SbhZbgfwPmAJe6OfkkUQVs8_7oDIj5gLb1OFGPb3RbA3ZoeB3-TkhoR2Iy7Owz9hmjGOZrmaoWzK5Ix2WLaQ9AFupC4MkqfE1iRqAqpgauIWY-lgo5iv7RPc8yOpkzeE1VoPX_gRzkygXrGfXpkXb3ricW9aKJ-bS_fEuJzBR1GgsuBKPjhaJ4iLv9uAHfD4E5nxJFZg2ODh_6F5k9fdevUI3QdSTcS4N4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
لیست آلمان برای جام‌جهانی اعلام شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/90121" target="_blank">📅 18:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90120">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFnxYuF88ZkiwlAOcjqlIpIMBaF1dwDxy82W4NEHO3sADPNZaeLeouGY6N7eHrobTgDcir9JwhroVWKiUKYeTascvfAJEdhpGPdgrIsr5o_psaZZ2J7bA3TLPIW-VX9Dhd95qYEMCpB90s_sYw6XY4ORZCisdPfGCfdGCqMnCljtVm-aaGNaF57cAl1pxHk9iL4SCBcmGi8SXEljWWcI7lh9-nF_657Z_EFPD1jL1CDiZUhtC8dcuYu02TzyZfYbS2gs8oBe_eKtQBv7PbVKrwPKzN8aILJy2BEKgwvV6NCbGLxFV2xiz17u7eyCzTxzztdJytpoVq7di69_YU3FPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آرتتا به مانند آرسن‌ونگر‌ پس از سه فصل نایب قهرمانی، بالاخره موفق به فتح پریمیرلیگ شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/Futball180TV/90120" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90119">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jt9aPsw4KRMoeFOPgzoSYWh3PWMaJB9opsbUoM55TqFndUgLQPTthHyl29_QGu_F8D9_MpVaGD4MgnZYa-h-NEdd3hvzShcIIrLd8i2xeSbe9AdTABuh25vKlEV8ml-iOXa1f7nrLE6wwYJt_ufNbsAYAsXWptKrpHMjm3OXf78iKOkQAt46Z4zyrT5NVWs6ABwBDKhBYPg0QN7NFKFCp3Zb5wolQzlcIfj2xiDr91RGpvV_2nDmUim2pekUhXUeKiLeK2U6pEbPbEyeWEj0ZG1vwTwKOhh0O3vn2JX2H784a-QyA-4LQmMqWMS5pLsniQTQts0zkG6B11kfm25k_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تیم‌ملی جمهوری چک برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/90119" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90118">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90118" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/Futball180TV/90118" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90117">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRQTrvQgYtiEgqzLJSIxY7rKgpIaAsacR1Yu0Dr8aurH_9nriNthItSNkcGEAqHU3dqbVAiVaTnQfw_dDMjxMEv90FHAY-XCIALvTe2owU8c1-zQ2OuhwL1LGQmoMP0CSMej_jpLsHgrcDpX0nQ91z8Un9oC0d77prvZU5NMpONeuY2rtCK8Fki8zIEwcJeLQwRCE6XMu9aytoIvbPoCTsHwLTmoDnvv44272LnfI6YDlajnbjZoi2WCdrmeUWqQqlOFWX3zzCBWWatshxvgrRd9W0RZrf8JhTOcIVEnu6XygDi1rnmSIKlcso7viJVPY6appRuyyvTR1PcyEdYnyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎰
با 1XBET راه خود را به سوی ثروت بچرخانید و از سرگرمی های بی وقفه لذت ببرید!
🎁
تنوع گسترده از اسلات ها و جوایز فوق العاده را از دست ندهید!
💸
فقط کافیست ثبت نام و واریز کنید تا از جوایز و بونوس های فراوان 1XBET جا نمانید.
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
فایل نصب اندروید 1XBET</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/Futball180TV/90117" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90116">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
فرمانده ارتش پاکستان، عاصم منیر دقایقی پیش وارد تهران شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/90116" target="_blank">📅 12:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90115">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHR8OMJ5zxGkFflh7P_8-uICvrOQNmfH94vRQhU6fjxsbvYtuNt4fdRERVt0-Q0qomXiMrbEBPoPeSeYkHYNBqJUOu3ym2l7JWEo3LFzGAvXAzfoG7T8q86i1OXI8oMmhkQcpaKw-nNy_9wlIOZ1dtBXs9zNr9D-Nb25SjOfI4dszeaIyDO4eAjgAkWbL81HoQHrNFZgSimy1LkiUMs6IWNnqLHjFV8tOrJSUdbGLfu72gMw92Cf19ifclbdxFpZIi8oESTdhoNvkapRHuQXrBpRa6XmhGA6oaFB1yl0vAEcVenTZpoiKJdqEbhyePbR-Kqv2YZujm1Kfdn7fDLqoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه کریر فوتبالی لیونل‌مسی و رونالدو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/90115" target="_blank">📅 08:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90112">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVsljdtpvVnsHihZ6lWAOQoCMw5g8K_4iYpCtoZmU5naJqOdkqABy1n_h32LR50wiN-h8k8mliHfAZbXL-WuTjPitqlJm8AOHewnz-4E9_53rymesa24eY3QXJ9cKJnxtXDr5hkdIvSQTNBbbtFZmH5z9ifVUvqJtJIxji43-CsAokWGmYD65hPpVS5DUJGh1ipqIIro4PB1rPzBPpQUqjF23GZQPL1y777cZ-CWZiG7eiHK34kx_ZYJ97dAQfO_Fqirz4n0gix3r3_G0L9j-YPT40hdVv3DKVIuDwYQsauhLvkwW3GHUTt0KNZbf6JjDBMwZC0QkH8KEfnTpfEIVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇺
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون‌ویلا با برتری قاطع مقابل فرایبورگ قهرمانی لیگ‌اروپا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/Futball180TV/90112" target="_blank">📅 00:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90111">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
👤
برخلاف اخبار منتشر شده، سردار آزمون بزودی قراردادش با شباب الاهلی تمدید می‌شود و‌ این بازیکن قصدی برای حضور در ایران ندارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/Futball180TV/90111" target="_blank">📅 00:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90110">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
ترامپ: منتظر پاسخ مناسبی از ایران هستیم تا از تشدید بیشتر جلوگیری کنیم.
چند روزی منتظر پاسخ ایران خواهیم ماند.
تا زمانی که به توافق نرسیم، هیچ تحریمی را از ایران برنمی‌دارم.
در ایران افراد باهوش و بااستعدادی وجود دارند و امیدواریم معامله‌ای خوب برای هر دو طرف انجام دهند.
اگر پاسخ‌های ۱۰۰٪ صحیح از ایران دریافت کنیم، زمان، تلاش و جان‌های زیادی را صرفه‌جویی خواهیم کرد.
امور ممکن است خیلی سریع پیش برود یا چند روز طول بکشد، اما ممکن است خیلی سریع هم به پایان برسد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/Futball180TV/90110" target="_blank">📅 22:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90109">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYXQqy8Ic-lpnU9xv7eYrzF62irSym_Z6uFqQslc2URgdmJgtxFwDfgvFRsovDey_bA34AgAqkn1mkzzD-1mxV5i22jcLUzTEAFpyX43lAamu-9HHLafOhJyzoZw1Hx_5EyQV9voFDyImTqwXcws1PDGkAUIWbbby0slOWLNN0_YJ5BB5w9prDAK0LeRhepduCltLwREHKh6WLHbN2XQqrPjMh8-n5XKElLPHQpQpzAa6KG436T4oJ9wmfIs4AJrU5ZheguG4hIcXfCi3mQycsQ1W5oASUPjlXTcnMeT-jXfNlRDvr3uOFsoFzUibFVnwD8KuficMeEEUgbFFk9rcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون: ایران هویت، قلب و افتخار من است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/Futball180TV/90109" target="_blank">📅 22:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90108">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🔵
مجوز حرفه‌ای باشگاه استقلال برای حضور در لیگ‌نخبگان آسیا صادر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/Futball180TV/90108" target="_blank">📅 19:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90107">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTJ4yBw516P8cayb5ogYclwnJ30GKvczHZLfssr_NJI_-C0P0tWC9Cyv35FoFRoBlJG2SUsERihJhYv_TV1dLIFqJJfUAVcBI7eltgSxJCL458tIVaLjiGCbrEmResvpTaBREy2an0sIPAnKn45CVmZPBqhlXBv0uqkYW_ztpLpTYFaj1ii14pzff67tFfnhh-YRqMoI-DwACipNQQUOfTU-P-t9xvmIcR4DYerSp7IbUhKxGPx43EoZhuNjPLifvM7MQQ9b4seH-_45Fq5egA5myruJ0MP1gq4-bcHuawkN9oZ4DMHK4cFBgz1ExwdcLAfseC53AnjgwiFMeeYHXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید کریستیانو کریستیانو؛
همان شور و افتخار همیشگی؛ بیایید همه چیز را برای پرتغال ارائه دهیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/Futball180TV/90107" target="_blank">📅 19:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90104">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca121cc7d.mp4?token=uZ8LhZi4HD7lSkopLskhSgueAcef8GO8LCwQgA0J3QNgVlbvuPchcsy0wLS7DWPv008KqL7Nh2aUINpsBMx7NVpf9D-lmVlKDiAsFa7sUZZRCpKeHqfik-FzUMLc7fkcxNmFZunpE-d9AHAq0t5t2xvpAACQNMBkckB2mCISdmvFkNNSg9qHDm1-2hudQNocqhYhhsinkGdi09AR9bHIw1SD1S7ZqIBWgVuwZW6-RpUwwtE2nsYJnBRjgjP8xNGsRa-P5Gc1F4-xRbCaHWg7EfdRtYcYWyaXrpXPrXbeIEVXTnPtcDjVr4Ou7xk7wi_ZBRTvQxtl75ZpCgTr7-oITA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca121cc7d.mp4?token=uZ8LhZi4HD7lSkopLskhSgueAcef8GO8LCwQgA0J3QNgVlbvuPchcsy0wLS7DWPv008KqL7Nh2aUINpsBMx7NVpf9D-lmVlKDiAsFa7sUZZRCpKeHqfik-FzUMLc7fkcxNmFZunpE-d9AHAq0t5t2xvpAACQNMBkckB2mCISdmvFkNNSg9qHDm1-2hudQNocqhYhhsinkGdi09AR9bHIw1SD1S7ZqIBWgVuwZW6-RpUwwtE2nsYJnBRjgjP8xNGsRa-P5Gc1F4-xRbCaHWg7EfdRtYcYWyaXrpXPrXbeIEVXTnPtcDjVr4Ou7xk7wi_ZBRTvQxtl75ZpCgTr7-oITA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
ترامپ : الان تو اسرائیل ۹۹٪ طرفدار دارم. می‌تونم برای نخست‌وزیری کاندید شم، شاید بعد این ماجرا برم اسرائیل واسه نخست‌وزیری
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/Futball180TV/90104" target="_blank">📅 17:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90103">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc000d4d3.mp4?token=hGF6QcZpuk4dzAWjYlyyxgwm8q06hRrqd64UOcadW0ROIF7RjseWbBhcSmOp0WR8qmKjoAinsII5GjTp0KIlRIXWMyJgMA8HiugMrckhoYuu6-tp_u9j6tbVvXbsRGBi0wUj7rjaUrmUM8sEtMsi4aVC0JfwJBWX5B7Fo325fGYay20D0dmpH_3XHEoQB7ph6bpK0S-ihiGeOehCMdb8V8RdL82Ru_C_2P-EFECf6E-9_iGaXXiFL0eh3cUp2cmy4LAJ16lFLxTDIQVBCd_SRew1aUL8_WtljYW-nOam8F2nd_sTGvFaEBuwXUDsf4TLEonRsFb80bMgrOHwZlMhlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc000d4d3.mp4?token=hGF6QcZpuk4dzAWjYlyyxgwm8q06hRrqd64UOcadW0ROIF7RjseWbBhcSmOp0WR8qmKjoAinsII5GjTp0KIlRIXWMyJgMA8HiugMrckhoYuu6-tp_u9j6tbVvXbsRGBi0wUj7rjaUrmUM8sEtMsi4aVC0JfwJBWX5B7Fo325fGYay20D0dmpH_3XHEoQB7ph6bpK0S-ihiGeOehCMdb8V8RdL82Ru_C_2P-EFECf6E-9_iGaXXiFL0eh3cUp2cmy4LAJ16lFLxTDIQVBCd_SRew1aUL8_WtljYW-nOam8F2nd_sTGvFaEBuwXUDsf4TLEonRsFb80bMgrOHwZlMhlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جدایی رسمی برناردو سیلوا از منچسترسیتی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/90103" target="_blank">📅 17:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90102">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/252c545abf.mp4?token=bru2CNkhAtA_DEBRFW8n2aFY4TfiXgOasWfjvt8X8IksWb_CL3K8m_2FQd-B5pa_tQQE_2IwxtPlr4dgBmYQWlToU16qLycZf3ppk771XquhJnvHsrMKKkLh6epCOT09qE7UKKsWu0xHapQNjoGS_10-Hsz7zYlI82nSG09Iiku8rSdrUDWIJE2MtmoTB85rgw4029au-k5PGFbhFDxARVhYW-pgO8wPOpGhaAHR6gskrtm-MTzGA834S7Nk6CZYn_rhVE9NVrpFSgbx7sVeSHFs0IrHZqXlYxcW5RC8kuJsGw2oNepdh0Phg1uyvyr5bKdTozTWYUEU29Ym3Xt4vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/252c545abf.mp4?token=bru2CNkhAtA_DEBRFW8n2aFY4TfiXgOasWfjvt8X8IksWb_CL3K8m_2FQd-B5pa_tQQE_2IwxtPlr4dgBmYQWlToU16qLycZf3ppk771XquhJnvHsrMKKkLh6epCOT09qE7UKKsWu0xHapQNjoGS_10-Hsz7zYlI82nSG09Iiku8rSdrUDWIJE2MtmoTB85rgw4029au-k5PGFbhFDxARVhYW-pgO8wPOpGhaAHR6gskrtm-MTzGA834S7Nk6CZYn_rhVE9NVrpFSgbx7sVeSHFs0IrHZqXlYxcW5RC8kuJsGw2oNepdh0Phg1uyvyr5bKdTozTWYUEU29Ym3Xt4vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنتا شبکه‌اجتماعی غیر معتبر روسی با این ویدیو مدعی زنده بودن علی خامنه‌ای شدند و گفتند که به این کشور پناهنده شده :)
❌
سطح اعتبار این ویدیو : 0
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/Futball180TV/90102" target="_blank">📅 17:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90101">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
⭕️
⭕️
🇪🇺
تمام باشگاه‌های لیگ‌برتر ایران بجز پرسپولیس و گل‌گهر سیرجان با ارسال نامه‌ای به مراجع مرتبط خواستار لغو ادامه مسابقات لیگ‌برتر و مشخص شدن تکلیف نهایی تیم قهرمان و سهمیه‌های احتمالی شدند
🔵
این تیم‌ها با عنوان کردن مشکلات مالی و ...، موافقت خود را با قهرمانی این‌فصل استقلال اعلام کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/Futball180TV/90101" target="_blank">📅 16:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90099">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r9cbUQZWU44q5H4nthhviYjZ2-ZVvC9xxzsEtnCH3RaR1ZGdO2anzbiTWgCgk-nbLM1th6wzgb7wtKuo84GmPGT_MLiFWDGO51FxxNihaASxxGnDbwGl454lnS_zLGGRdw5viTP1lgFZ3o0WNhV9pcAYTvwwEKTesj9YSuYLb8s3xRZeam0r0wquHngNNhBDcnPW2YYX6N3wEZkTbl0ZINzyn0M43SGZPj20A_lWjydBelha6G8izHcOPTTRNfzz6zzciHmVHicIMVFBnOEiLdg9e-rskLomH2QXH0DwoVzqU0yx5ZBdBdLTbSspM4tbN65ZToVuuPyW1ETrLtR8jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-2VfUolu23ZGx5MPgheOw4SMEhBkHj_fFUlbP0sL3skKRlp_HWwRclHJcvlwbrnBC8XYiF-V_6LmvTihEu1TFcVFiozB7HG-FNe_g76XF0IZP0StT7m_kC8c-r2vZhqvX3_fBaS_ZvIJ7I5qJCKyt2lnmMM_UpLBtxVSc_60xBF49IvG_JKtKoRfn9osJanayptDsle15TsN40JAbzMSx9aY7fIN3Q4b_Ckv7XNxrRNcOPNLJgg_EF_R6KpCZL02scpRXSNtJIDjmBxQM1QtF3Cpdrq0TxM03Jp1Pdmks-uAe4dSIKqImXpjMY5rEvKEqHUD-D_ezQUFMgOfAK38Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینس گارسیا بلاگر ۲۱ ساله اسپانیایی و دوست دختر جدید لامین
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/Futball180TV/90099" target="_blank">📅 14:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90098">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
⭕️
رشید مظاهری سنگربان شریف سابق فوتبال ایران در حین خروج از کشور در فرودگاه بازداشت شد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/90098" target="_blank">📅 14:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90097">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ece86e352.mp4?token=Vc4YL8SLZj0h0bSFeA0zL89xJKiQmMRKu8DWekkGmxTr9GYK2CQOZT_7HWLBOaBOAZPyl2eh6EC0lGzDMJTJcdsT4i-bw77ZZQ4Oy6Hfb83nRAR6dBqBwCyzrtV010b8xPup1tMFMRMNh-XgGGzQonR5gfZX2oM8n2vLNczJlZzFbpiCPEGqrvAtrpIgEXAxrngFq4BSV5yqf2KYCauZcZMcbqPce49JHifXyMhP4mRHUWwdRFEKeATy-PdicXRmje5WiHLrV6iKnsjfeqnEhbk7dGSBsTMif2_zG0UaGsdKVc5FtyBXoB7IF17BV6s_6notbeDk18ugWBQAzf_--g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ece86e352.mp4?token=Vc4YL8SLZj0h0bSFeA0zL89xJKiQmMRKu8DWekkGmxTr9GYK2CQOZT_7HWLBOaBOAZPyl2eh6EC0lGzDMJTJcdsT4i-bw77ZZQ4Oy6Hfb83nRAR6dBqBwCyzrtV010b8xPup1tMFMRMNh-XgGGzQonR5gfZX2oM8n2vLNczJlZzFbpiCPEGqrvAtrpIgEXAxrngFq4BSV5yqf2KYCauZcZMcbqPce49JHifXyMhP4mRHUWwdRFEKeATy-PdicXRmje5WiHLrV6iKnsjfeqnEhbk7dGSBsTMif2_zG0UaGsdKVc5FtyBXoB7IF17BV6s_6notbeDk18ugWBQAzf_--g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
شادی گابریل مدافع آرسنال با خانواده‌ش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/Futball180TV/90097" target="_blank">📅 13:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90094">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ks_JS-TqPM7iXkbqqaIWILH221HwfgrKkgpOiH_dgp_julBT17WpRNtDBYnQGNiKk1PNTorswGyuZ6K4_ID8AGyvlr4G0SVsjqYE2h3iui5CseqENKpG3CFka33wyyov62iWtWhIpw57nQqsdHM5v_HFlfKltQCVHqsvRe3rMeEhXrjEk3qAFgZPdCG7RV5ZdNnheSmRMbA-h6VxPSiVsR9JBG6QzyrGshtnswAq9qGgeKzM2gBS505W4Zs52QT8LlGnP8uvcMF-S__1PDeW4yrO83PFOuG-4IXDxeaTClKGdHHOFw-TH1iqU21lKUa5tI1OICmogaBtYeEtMwvSnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
توییت تاجرنیا در واکنش به شائبه‌ دخالت غیر فوتبالی در تعیین تیم‌های آسیایی: ‌عدالت یعنی سطح دسترسی به قدرت سیاسی، تعیین‌کننده نباشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/Futball180TV/90094" target="_blank">📅 12:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90093">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56d546629.mp4?token=ErbV8nMCGNftWxoNPT1EzcIncpEwxI1XoI_14mAKthYQdzFGYqjW5bzBHvfl-eEGy1Wnl3pgGE6JRZdjth4fe2_WW3sEnmCPHKlPezq95_-Vlh8GZdxJqklQ1PRVepU1aklGT998UB8v9gGdBX9Gi-jrHtCuO63hi3ERKl9ly76hwKKwbhCJpQ15pOBXUksxfdKCdLowWuU8q_kh7AHQuzYNZ36jRnAo_2-GHI8UziLWMgVFCLWpnz0-HjTUbESbHO3Ls7b7B9y_OaUi2Gh8-Y2MEGvFqNjLnXKZI012U-DjQ2J1qElP-k61AFpULwcyvMU7SeVQE3Ga6eyJK2cYtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56d546629.mp4?token=ErbV8nMCGNftWxoNPT1EzcIncpEwxI1XoI_14mAKthYQdzFGYqjW5bzBHvfl-eEGy1Wnl3pgGE6JRZdjth4fe2_WW3sEnmCPHKlPezq95_-Vlh8GZdxJqklQ1PRVepU1aklGT998UB8v9gGdBX9Gi-jrHtCuO63hi3ERKl9ly76hwKKwbhCJpQ15pOBXUksxfdKCdLowWuU8q_kh7AHQuzYNZ36jRnAo_2-GHI8UziLWMgVFCLWpnz0-HjTUbESbHO3Ls7b7B9y_OaUi2Gh8-Y2MEGvFqNjLnXKZI012U-DjQ2J1qElP-k61AFpULwcyvMU7SeVQE3Ga6eyJK2cYtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما: هر کی جنگ نمی‌خواد، جمع کنه بره‌‌‌‌...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/90093" target="_blank">📅 11:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90092">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🟢
باشگاه آلومینیوم اراک بدلیل مشکلات مالی در آستانه ورشکستگی و انحلال قرار دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/Futball180TV/90092" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90091">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e96fba692.mp4?token=WTJmBW9JO6kpxwsY_9pq0vkJJ4H7bU8IJBJb5fwwVuBQfhhSYuaFFoGVOyj9vQRNyclHyjSulyoy3vqZ9NZ6fmjf_5IVLwAVbM0muktK1TYBoQhGpiaWonfS0tZoRUnd5JSNP2mcHRWuNU2W8lOP460nGihZ1IO6LVXP1skF_b1cxxhLdkt8Vseb_GuG-q7uTKbt6g9lyxjbXp4vfmo_VjblJFnOvpTI-iA8Q_q-S_RoKGixvATpDcLLuaEtOu3oNeuTvtjxUYFUqd-KDcpjq6_Xxhei6oygs6iBeut4hNoJv2XJfnfDHsf6JDaAwa-OYkBYni0otZ5EW98ImOZKdIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e96fba692.mp4?token=WTJmBW9JO6kpxwsY_9pq0vkJJ4H7bU8IJBJb5fwwVuBQfhhSYuaFFoGVOyj9vQRNyclHyjSulyoy3vqZ9NZ6fmjf_5IVLwAVbM0muktK1TYBoQhGpiaWonfS0tZoRUnd5JSNP2mcHRWuNU2W8lOP460nGihZ1IO6LVXP1skF_b1cxxhLdkt8Vseb_GuG-q7uTKbt6g9lyxjbXp4vfmo_VjblJFnOvpTI-iA8Q_q-S_RoKGixvATpDcLLuaEtOu3oNeuTvtjxUYFUqd-KDcpjq6_Xxhei6oygs6iBeut4hNoJv2XJfnfDHsf6JDaAwa-OYkBYni0otZ5EW98ImOZKdIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
واکنش تند مامک جمشیدی، خواهر پژمان جمشیدی به خبر منتشر شده درباره صدور حکم پرونده برادرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/Futball180TV/90091" target="_blank">📅 10:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90090">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔥
خیابان‌های لندن در تسخیر هواداران آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/Futball180TV/90090" target="_blank">📅 10:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90089">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYvd957xLnep1eCAsWao0wVlC47z4skujic0RUg_ptKQftTv8l2Vwu07WdDkhKPUMQu5voB65j7XtBbWl5MtpGWYxYvfjm8mzUmSvYJWRub0gMfMylOEpx0pOMAZZB5yVrhj7pv1MToaa1KGzr5xaFHj_SN8B_aMeVlUg_ABdDvGXuxQDWHBhNFPN1-LBotpsUI0Ybge3Z1TvE4fj6IlK-N642_U7ZTzUavLDjgNkmOuAtEedH6SqTEtClKdO4UnyM1E7p4-tLwJiDXHiUIFzR2Pb4-S6-l4SlqfK6mxb9AUXM1X-1NJYUCf1AmLXAV8DCuJl0NRmwmF6QYOC4Iz_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد مسی، نیمار و رونالدو در ادوار جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/Futball180TV/90089" target="_blank">📅 09:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90088">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f7578a72.mp4?token=hOTg6nplrjAQNtnz57O35FU8qTKFBLRcAYsv3GfeUV1mwL9MA0CTx2nJ67dwm7yfqy0qTPzrqESnW5DAMYM09Jk7zqWgVSLUEtr4EkYBs5TfZEYQEziV-fN6oJlfQT80UvpKyBTw4c7_6yn2r-KP_RbNZzoKqoVdDA3uefLVqFpSTklSiA_uDCyboXPjLq3SHLqHkmtXyfHnXBHru-Vb2-WgJR0hFpQ47egPQawq9FQOolOhrdGBM4Ok-x6vPuDhhWboapYLpmGhjEVe9d_6FkjHML39RdXecQ39b9FkhXcbWWxokN3w7C5s2Dpfqe5BDSgYx_y0KGaKi1frvmKIpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f7578a72.mp4?token=hOTg6nplrjAQNtnz57O35FU8qTKFBLRcAYsv3GfeUV1mwL9MA0CTx2nJ67dwm7yfqy0qTPzrqESnW5DAMYM09Jk7zqWgVSLUEtr4EkYBs5TfZEYQEziV-fN6oJlfQT80UvpKyBTw4c7_6yn2r-KP_RbNZzoKqoVdDA3uefLVqFpSTklSiA_uDCyboXPjLq3SHLqHkmtXyfHnXBHru-Vb2-WgJR0hFpQ47egPQawq9FQOolOhrdGBM4Ok-x6vPuDhhWboapYLpmGhjEVe9d_6FkjHML39RdXecQ39b9FkhXcbWWxokN3w7C5s2Dpfqe5BDSgYx_y0KGaKi1frvmKIpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
رختکن آرسنال دیشب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/Futball180TV/90088" target="_blank">📅 08:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90085">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4882a411.mp4?token=lsGRtr3uk0zg1LslQvC28AlRJeBHgKGp1S_wQ70G5ep9scmsa9S-jmWzQvXl3Vu7-mrrJV1Gq6ikvMUYXTMD6bbmZxz6BbnqmZ3vTeqW5rXbhQBioLDppBuNigEX-Ua7L3OIZfA81ZBorLlyi5h9L42eL215ParEqT3ibqQ7jZSL3Xkd1KuaV7V_81FyKUDlUQ5xa3MvGqNuQ4KSXAxyfwG_O9TzcQRAGp26I5FSv14_uSLDgUlWaRmv7LuXcYqM_ptzHigabARjpUO1CTJ2fx8uY8CFYmB5rtMDsr7L9LB_OGJt6W3fuzyORntYRnEpoIvqBmf25iAKVtpeSk59Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4882a411.mp4?token=lsGRtr3uk0zg1LslQvC28AlRJeBHgKGp1S_wQ70G5ep9scmsa9S-jmWzQvXl3Vu7-mrrJV1Gq6ikvMUYXTMD6bbmZxz6BbnqmZ3vTeqW5rXbhQBioLDppBuNigEX-Ua7L3OIZfA81ZBorLlyi5h9L42eL215ParEqT3ibqQ7jZSL3Xkd1KuaV7V_81FyKUDlUQ5xa3MvGqNuQ4KSXAxyfwG_O9TzcQRAGp26I5FSv14_uSLDgUlWaRmv7LuXcYqM_ptzHigabARjpUO1CTJ2fx8uY8CFYmB5rtMDsr7L9LB_OGJt6W3fuzyORntYRnEpoIvqBmf25iAKVtpeSk59Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارجدید حمیدسحری با کپشن:
تاج‌گذاری میکل آرتتا در لیگ برتر.
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال قهرمان لیگ برتر در فصل 2025/26 شد.
🥳
⚽️
Channel:
@Futball180TV</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/Futball180TV/90085" target="_blank">📅 00:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90082">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=uRU4ZvS-CsYD_nlqFIj80Nsr26IIPwktwbtk9v1yVGyEMlTd_hcHr0K46utSe_iTKYJ0ObEeOFWY_i_AaKKPV6jxqaOQgkA-LoCRFZ-Nk9jmFfN0ITWJJ58BCoVw7MyNVAd3aiF-5t0TGRc-qktnISxQrmDPHe5dO0BohZI8kxw9bDqOTYq4lPV_dbyjukc8PQKBR9HCfHOixgENWnOzqZ7PdZXjpUIbHg01K0OiInzdjQ67ArZvu-Mdm3g4e289dyGb6SNOu_wLmaO-A7hOxU1HE9x4w_RYvMFWJwK_sHWh7r25dHx0OF3T_LH8QgmKyTZ0J9drT98CMxkPn_Mtxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=uRU4ZvS-CsYD_nlqFIj80Nsr26IIPwktwbtk9v1yVGyEMlTd_hcHr0K46utSe_iTKYJ0ObEeOFWY_i_AaKKPV6jxqaOQgkA-LoCRFZ-Nk9jmFfN0ITWJJ58BCoVw7MyNVAd3aiF-5t0TGRc-qktnISxQrmDPHe5dO0BohZI8kxw9bDqOTYq4lPV_dbyjukc8PQKBR9HCfHOixgENWnOzqZ7PdZXjpUIbHg01K0OiInzdjQ67ArZvu-Mdm3g4e289dyGb6SNOu_wLmaO-A7hOxU1HE9x4w_RYvMFWJwK_sHWh7r25dHx0OF3T_LH8QgmKyTZ0J9drT98CMxkPn_Mtxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💙
سهراب بختیاری زاده سرمربی استقلال: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/Futball180TV/90082" target="_blank">📅 20:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90081">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8K5GAMABdfDSmlmd65N_60pZDc1I20j3byP0VDHrIP3F4TOVnDnQ7-X36p60PXTRFpD0uereRM22R6KgN_xqWK0l9HIPKCapWNkG41Z44M3FIbuBseHzThMDzpn2sHb2tdh_7DKOrpjWqdSbT5VqSXiPAD2VWQRNd_B9bO06S4GU-zPzH5HJG5J8QYs_Hcbkel8vgFNIaxnVhoaQN3yIQXX6nbY51zcBnQrxaw-yHN8o5YPLsTgHjFTPYuPAJVmO6-xLLYxxZhTrqALn7Sezzygn2kOwiQqqwee4vV63R2g9uMlfR6XiU-wOS77aLGiC4vukMkWcK3mrTEp-pvPHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
از این منظر نگا کنیم؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/Futball180TV/90081" target="_blank">📅 19:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90078">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd848eb99.mp4?token=f0Npn1-r61KcnhSFOTDslmGowZW6qm5KUh4DgDlp_et8fDdQorbIEtgJDcfFXR5VtJ7AANblAlbhFTu32amRgsQ67yZOYcOO6burt_84M82ZI0cRcPHj24jl3WRA5nB1KhyX7lGFII8K1QikvDBtV-sjCyrJRmgTrv8ohHnHHaLhD0NkZsr89IOXmQvl8h9B2JQmZb9j_IwviQGW_1g9MX_TsHavbnoFTxPrTZYuEve_6OTbvw3ZklJUBWTTaOIYnGWPpArbKUcDo-JQOC_qnmATCr8H3j8P_-9DVn0lAwOJQaMp8ajSPE5Uh_yeX9hwcKGlQcC2LSTQJ431HtJ3tTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd848eb99.mp4?token=f0Npn1-r61KcnhSFOTDslmGowZW6qm5KUh4DgDlp_et8fDdQorbIEtgJDcfFXR5VtJ7AANblAlbhFTu32amRgsQ67yZOYcOO6burt_84M82ZI0cRcPHj24jl3WRA5nB1KhyX7lGFII8K1QikvDBtV-sjCyrJRmgTrv8ohHnHHaLhD0NkZsr89IOXmQvl8h9B2JQmZb9j_IwviQGW_1g9MX_TsHavbnoFTxPrTZYuEve_6OTbvw3ZklJUBWTTaOIYnGWPpArbKUcDo-JQOC_qnmATCr8H3j8P_-9DVn0lAwOJQaMp8ajSPE5Uh_yeX9hwcKGlQcC2LSTQJ431HtJ3tTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
۵ صحنه بامزه از گزارشگران عربی :)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/Futball180TV/90078" target="_blank">📅 17:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90077">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2bf46e469.mp4?token=bW9Hs0l0HbXAAj4Wf9Dii9PyQDJDcP36tfaiWg_3HTPaVOh2TLDOjXU5LdUkTkp1GIcOITVAeXbfPAp1QFP1mcFQ0bT-V17UDrIjJA6_OfyfbnwwcHepyQ8yIBPnp5qvq47yggQglRs9gjX1aTSCDYRnH7emkz023wHu5bdm8AQknGmq-yymEJ-eSPP5lgvI26fweuA6LguXKC1ZJoagZvWYAhzKDStAnvgI0HV8Pt16qjH4N_AoybcttnxE73IUbW4Qr-lnnggwt9rtAc1yntjKG-ObkNZp2qsv3bPFk4C83oXrVoQB9auls-H_yGZX67-GO_pcrHAXOg0ulkSTcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2bf46e469.mp4?token=bW9Hs0l0HbXAAj4Wf9Dii9PyQDJDcP36tfaiWg_3HTPaVOh2TLDOjXU5LdUkTkp1GIcOITVAeXbfPAp1QFP1mcFQ0bT-V17UDrIjJA6_OfyfbnwwcHepyQ8yIBPnp5qvq47yggQglRs9gjX1aTSCDYRnH7emkz023wHu5bdm8AQknGmq-yymEJ-eSPP5lgvI26fweuA6LguXKC1ZJoagZvWYAhzKDStAnvgI0HV8Pt16qjH4N_AoybcttnxE73IUbW4Qr-lnnggwt9rtAc1yntjKG-ObkNZp2qsv3bPFk4C83oXrVoQB9auls-H_yGZX67-GO_pcrHAXOg0ulkSTcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
شادی نیمار از حضور در لیست تیم‌ملی برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/90077" target="_blank">📅 17:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90076">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tSlxPvr8t36H8HtkUe9VlKZrKvuq5wvveHz5AEemktq9Vav10UE-QKPy2bcVaydfVlHalI-7rsLcswQEFWPsMDPgb9mjzch60WG2zQ9sbIa_zxqSQq8yPQV6eKJGx_ZjlY6QuQL6PWuB-bMC7ak0HObxAdRwC8-H4SNGc5Bw0TM-P6epfG2DBSE9uvkdHJNGj4_vnkwCQBGAMeO7P4kkmuDG37_La5_RgfXxMuLoIu91N5l0QheedBg820hWSlJ4DLEZQu9uTi8EpsooaZG7Rb0W4EZEBf9I5QvT2cL9TOH-bqh5WSWWjyIXKGgvPAh_4zUgajV6oXYvMQ3cBcoJGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
لیست تیم‌ملی پرتغال برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/Futball180TV/90076" target="_blank">📅 16:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90075">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3576e35.mp4?token=XQo3OVTMeatwo8GxGNLQEUYZq-D7-z-2yxa4G3YGjIn4m2BwtszlUYz4hW_9xBPK-GjmteMt7ZREwx6XAX6TJpPdaySm6treqEx152FXYyaWmBamXuF911kqzg6HrQ_w3dgEmR46gTUgsixMmf6oyppuYWWU7xscH8S41elCw9tk6nvm7ULCSSHUHvDtKawt0cGrIVBSc9P1Ppaw_GxS5FRnUFqyh3gykEtizEN-ZE4DOPfmu3enYXkblvlZ3V6E7vfh6AQbPQDmILyOStZbAbaNUMCzgV0wOpVjROyemFHx_7sZkhRrMRfRtsIyDtLXlAvVSCJeV9RdQUv8Kdap8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3576e35.mp4?token=XQo3OVTMeatwo8GxGNLQEUYZq-D7-z-2yxa4G3YGjIn4m2BwtszlUYz4hW_9xBPK-GjmteMt7ZREwx6XAX6TJpPdaySm6treqEx152FXYyaWmBamXuF911kqzg6HrQ_w3dgEmR46gTUgsixMmf6oyppuYWWU7xscH8S41elCw9tk6nvm7ULCSSHUHvDtKawt0cGrIVBSc9P1Ppaw_GxS5FRnUFqyh3gykEtizEN-ZE4DOPfmu3enYXkblvlZ3V6E7vfh6AQbPQDmILyOStZbAbaNUMCzgV0wOpVjROyemFHx_7sZkhRrMRfRtsIyDtLXlAvVSCJeV9RdQUv8Kdap8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خدا رحمت کنه زنده‌یاد علی‌انصاریان عزیز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/90075" target="_blank">📅 15:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90074">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1631168f15.mp4?token=CIxxCk5CJWINKnOX-qN2pgNs__AzCBwqhCyFvMDMpSgayTkrXQaGmUz60sSk2JfWcb0OgpJsiRHTMhv_ZL3uNkUjs43OjuYD3qjb2odaKxKGEv0LQPrNnsCGoc66Yavhn5YGCCB7y-zHbMpEHgBAL4NPeQTEs84JHZ5HvjTOUduK17rUB3Y_jh2RJcf6_LAFESrLy7Pni_GAqwRkl1AlGUoBMZ7HZI-gApKJq_DV1ErpVlnzkdCQIUmLVdpnc6Iy7g1HJC3_77DwWJx6gJCwDWniTZa0MvyhnPC0BMbmk2xF99GXDJ9olxujRqnZ-zVsvyyW3SXukWRGFg30E3e2NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1631168f15.mp4?token=CIxxCk5CJWINKnOX-qN2pgNs__AzCBwqhCyFvMDMpSgayTkrXQaGmUz60sSk2JfWcb0OgpJsiRHTMhv_ZL3uNkUjs43OjuYD3qjb2odaKxKGEv0LQPrNnsCGoc66Yavhn5YGCCB7y-zHbMpEHgBAL4NPeQTEs84JHZ5HvjTOUduK17rUB3Y_jh2RJcf6_LAFESrLy7Pni_GAqwRkl1AlGUoBMZ7HZI-gApKJq_DV1ErpVlnzkdCQIUmLVdpnc6Iy7g1HJC3_77DwWJx6gJCwDWniTZa0MvyhnPC0BMbmk2xF99GXDJ9olxujRqnZ-zVsvyyW3SXukWRGFg30E3e2NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
ناراحتی شدید خانواده ژائو پدرو ستاره چلسی از عدم حضور در لیست برزیل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/Futball180TV/90074" target="_blank">📅 14:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90073">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_Guqi5Zmw-dnSeOGR6t0ScFnMmUGMyD1u6cLXfjn9IoJTrvoLCnq-qTOVw25gdiiZsTaaSj8KJIGgeWkjp9LiISMC2J0R2tPRvxD9a8op23tc2KhGYNUBF4WYfL-VFiSyX8yskPD1-VyVf6iCHfV6-eFxeMtHVdNNdZtyl-jVBpax2r70HTxXECehp96Gih7DZU1p9Jnt48DC89U-dWRXUjncD5oytoPLJySOsBq1z30u5qTivzRu9oxgFBLjxA5i3qbTMw5OluXQj5qYbwP3UrHqNvAmQeX4-r08TMeFuGDbdP-y-I2ffgh8oU3_j-6AAhADgh1EoU6OoeS6pOIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رئال‌مادرید با ارائه پیشنهادی خواستار تمدید قرارداد یکساله با آنتونیو رودیگر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/90073" target="_blank">📅 13:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90072">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbpZ0jo8Hiph7fXtQ9HDvQlhyyrbkRQJiTf3GNPfFStuaorvMFEz_HVINXy4TaHF4bAMm3bLyXYHQiEqxYjIDrpxrpzGTnZrdDJ3N4XRE2Q6yGhRmdFRIaBvuiRKJYIozV9OY42Irbfj-SmTxPpGDP3ePiyx4mcHjxbq_zuVUDnadgKdgaF1nrdblRUQ0xuiHmi0PsBEkd5mZYB7UXpGTtY3h0u94yPB_922E3-KOV7nYMFzc3wIiayCaH_aVtIrwuRKv_hJQcQsNImrkfcQQ79gF-rjVMaqO30iuCOwgq7YAmYGofdDbQpJx_BYAlfSz46_aXIPoK117oSHRSaI_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد قصد دارد با ارائه پیشنهاد هنگفت با لوئیز انریکه سرمربی فعلی پاری‌سن‌ژرمن قرارداد امضا کند اما در عین حال این مربی پس از پایان‌فصل قراردادش را تمدید می‌کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/Futball180TV/90072" target="_blank">📅 13:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90071">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c098031df0.mp4?token=s68lxbkzkySxlkzVzXUni3nM1D5DiNWuz11h8BJqgz8j6RkoC4AxTtHi_m0dmvpkcpYNYazlPkvhmOr9_6VkYQ00yn-cvGnVbb7YAFsq6UbK7SUPcjNz4MdWC3vHHnb99dSSVgrvPIzXM6jWb0x1PXnVWsKQJaEcDpCa16XfPoZpSyYjA4qJ70ec2d3W90oqE1KEJcpM6BwqZxC2VIJSyARJwPwaxPg8ef4xXIeuYNsqXaOxybeM5wCc0dWJluQg5Pg7dOA67SAilmA4W9XWO3dfFWc89I00uQcUxii2xAEZTe2XTyxvYZCv2vmUigJnOWuOAKPweHvx-Unq7xsFjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c098031df0.mp4?token=s68lxbkzkySxlkzVzXUni3nM1D5DiNWuz11h8BJqgz8j6RkoC4AxTtHi_m0dmvpkcpYNYazlPkvhmOr9_6VkYQ00yn-cvGnVbb7YAFsq6UbK7SUPcjNz4MdWC3vHHnb99dSSVgrvPIzXM6jWb0x1PXnVWsKQJaEcDpCa16XfPoZpSyYjA4qJ70ec2d3W90oqE1KEJcpM6BwqZxC2VIJSyARJwPwaxPg8ef4xXIeuYNsqXaOxybeM5wCc0dWJluQg5Pg7dOA67SAilmA4W9XWO3dfFWc89I00uQcUxii2xAEZTe2XTyxvYZCv2vmUigJnOWuOAKPweHvx-Unq7xsFjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
پاکتا هافبک تیم‌ملی برزیل و دوس‌دخترش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/90071" target="_blank">📅 12:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90068">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9GeCK1TBdrQrtmCv2oKNqHsYv6mvieIzyvTpBgAcwkMDoKuqtCfan30cknFnOOwhXJcAOXCll4-tItTeIEqXG4PeqIT5JRWQjmfdcuKFwvjn97xzV3oInQZLFKM3FAK7L6fVvDcVrF1pJq_7wrOkUsR7B44MSQwoR5N8V0kpK8tGxKFcJfG7JgoHQL4_UTkJJZi5G8p6_z970q7tvvDfdAvUfWONpIIljzi7qVM5o0TcFCJM1SOm4809zW0lP_mZfwJSu4ONyS0-Y9xfBIUB8jqLhV5K-wusBgSRszSCy-uHbP7OTfJZwwo-bQxv4pi9wjzLIiTbKnymAIhdGBmLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
کیت‌اول باشگاه اینتر در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/Futball180TV/90068" target="_blank">📅 11:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90067">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCqLHzk7jgvNW0wbvHDFpluWuER-E1ykQx10n4GVktZd_3xnjpROQBpihQ9-86FFrKl1QSExIbdzZ4Ir62Rvcbqx-DcHdTTZ1gjftGUc-b_En8LvlVPf58hR1IZUNuyPzS4ixW6ud_0Q8HruZyAaKTaN_JBfOlCRTghR9pj3akITeCntAftzX8g2MQNyNKR-jC96N688T_bMpj23Oa7GLbM8ssZU4vADI-tccJtAr6WVtb4_c9bCycTXq2RnV0wiDZ4-C45FHuPXgqUlRR-9fW_AEShoGVGsZuoHKIWnC83-Gn-vOsszMOv_ieHNbtnWV-8up2_Ulzn5vP1O4OVMWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌اول فصل‌آینده لیورپول
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/90067" target="_blank">📅 11:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90066">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1fd62d6ae.mp4?token=hMlscRcZL6XwAQNdRdf-AoNPk3DfRNvdzMnNfmaHc_jXGrBJZLDOuTXjv5TSorNmC-9hdEuwGOt2aWXHbSjSTAv-_PfdewHof4VhWtI_TamqTMDdgGRyRHN5W-dkYnqDdNDL2GS3ILDHUgf6RyKWLcqszd0zzCd6dECW-i5xbjbFekKLYbjtxfyljzjcf_b3oxIUfA4ojiRhs4IqjAeYB-br86hhe4JzRpUJP-eKo63-NSTPq4c1wQ65sOFujAIuRBZ-yc8Pgy--Mmy9Za0LHvGPkZ0xWrHjTZtCERUGP9HqETlcn-POd_w0q1DcIoPLiBgXjEv_odSF0OBhoxRzdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1fd62d6ae.mp4?token=hMlscRcZL6XwAQNdRdf-AoNPk3DfRNvdzMnNfmaHc_jXGrBJZLDOuTXjv5TSorNmC-9hdEuwGOt2aWXHbSjSTAv-_PfdewHof4VhWtI_TamqTMDdgGRyRHN5W-dkYnqDdNDL2GS3ILDHUgf6RyKWLcqszd0zzCd6dECW-i5xbjbFekKLYbjtxfyljzjcf_b3oxIUfA4ojiRhs4IqjAeYB-br86hhe4JzRpUJP-eKo63-NSTPq4c1wQ65sOFujAIuRBZ-yc8Pgy--Mmy9Za0LHvGPkZ0xWrHjTZtCERUGP9HqETlcn-POd_w0q1DcIoPLiBgXjEv_odSF0OBhoxRzdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپر صحنه بازی دیشب آرسنال
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/Futball180TV/90066" target="_blank">📅 11:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90065">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
قرارداد آرتتا با آرسنال در پایان فصل به مدت دو فصل دیگر تمدید خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/Futball180TV/90065" target="_blank">📅 11:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90064">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9L1bxt1Rr8pfCn3J3IAj9ll0e1Yl0p4EY86pr-X71SPhH-J1qYv7c951CarnZ2o513E1tHU_vDyuLuyhU5Gwct-RFeeBlzaZP4MJhNjogWr1H4wdHFSzfvcuXtJVyEKte0r5zy4rL0nKNnlr5-IarmvNqj4XVpaJq7LTS6UZwBr8wauTDmVygLaRt-juvX9V7PociKOQn_RlF5K0I5ZUteGUUkKNOCkDF4XijMm_ttQZBa3mfRQI3xsNdsQPtDeR0btQJF8H6WrupmcNgixpbRvlDyVRZEOiV1jT3aaUhr45cO0ZojxkcdMuo4jaZDJRZmRj41Fn9OWCFau-YKeEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
با اعلام‌فابریزیو رومانو، انزو مارسکا با عقد قراردادی سرمربی منچسترسیتی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/90064" target="_blank">📅 10:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90063">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4a423232.mp4?token=svUlJN_exTzk7pjzemuW8V7oBl9ftT8Zeh_ThGCcTCTBftqHQEDo1Yl7hvinMd50W9rVN6fjWPJmYATK_Can426pVz9Wb1MRU4Yj1SxxgxN-x1mYvl-EAlIoHh2PewKc1zHGz-7R7AWqwjqBJwoZbWa6eZ617xow9dC9d4k6e7jXzIOvXaqWeHHPT7wzbERCVuWwz6Ui-2swLyKhhrN66d0py0EXswBFqo0wbSrO-wqEKy4ZRZxUk3jD6dQgZJ4EuTXkseRdLZll0mrh15PeKUSDyyETutpFabWx3NQNSQLFqATsVBHJ6VbqBO1TOShFHIl01t2y-Keq6tdHWQ06LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4a423232.mp4?token=svUlJN_exTzk7pjzemuW8V7oBl9ftT8Zeh_ThGCcTCTBftqHQEDo1Yl7hvinMd50W9rVN6fjWPJmYATK_Can426pVz9Wb1MRU4Yj1SxxgxN-x1mYvl-EAlIoHh2PewKc1zHGz-7R7AWqwjqBJwoZbWa6eZ617xow9dC9d4k6e7jXzIOvXaqWeHHPT7wzbERCVuWwz6Ui-2swLyKhhrN66d0py0EXswBFqo0wbSrO-wqEKy4ZRZxUk3jD6dQgZJ4EuTXkseRdLZll0mrh15PeKUSDyyETutpFabWx3NQNSQLFqATsVBHJ6VbqBO1TOShFHIl01t2y-Keq6tdHWQ06LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🤯
شادی فوق‌العاده برزیلی‌ها از دعوت نیمار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/Futball180TV/90063" target="_blank">📅 10:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90062">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da1d08628.mp4?token=eKPMH_JnU5M1WwVVhgTAp8rgZvmW773pIc8e3voit0xzum_m29kCyT9mR3rhZuNs0FRyDJzQHWxMDlJsYpDrUr_whvYUi4c1gW2nssxoAr0ZxwrOWO4BML1CciUUOHHiQHmwQzkwU7hmhis3JOOqGZHVFhs1p9zlchPxv6p2x5Om_vbOcrBbwuJ9yiYOTdP_DqR0GsjIvlUHakntejhRJqHPTn1DC_0khfENrf-b6fuLRleZ1WRFN-bXtmcjI-bh3k-rTxJZy5xA9ftNOMKwhnOaR0Coq6-cpd2hzgoY777EKLF1x3jWWD4h3vVp-MNkvUEnMu-gGLSL5PPGLvGXcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da1d08628.mp4?token=eKPMH_JnU5M1WwVVhgTAp8rgZvmW773pIc8e3voit0xzum_m29kCyT9mR3rhZuNs0FRyDJzQHWxMDlJsYpDrUr_whvYUi4c1gW2nssxoAr0ZxwrOWO4BML1CciUUOHHiQHmwQzkwU7hmhis3JOOqGZHVFhs1p9zlchPxv6p2x5Om_vbOcrBbwuJ9yiYOTdP_DqR0GsjIvlUHakntejhRJqHPTn1DC_0khfENrf-b6fuLRleZ1WRFN-bXtmcjI-bh3k-rTxJZy5xA9ftNOMKwhnOaR0Coq6-cpd2hzgoY777EKLF1x3jWWD4h3vVp-MNkvUEnMu-gGLSL5PPGLvGXcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
خوشحالی اندریک در کنار زیدش پس از حضور در فهرست برزیل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/Futball180TV/90062" target="_blank">📅 09:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90061">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf11ae109.mp4?token=FbWn5WQH4hhdm64i2S-D0IxMu0FSS-BPtmF2YHBQ3hmJi_R6uzXL5wWZXIsiySYGXEKCHhMq7fQBWRR7-dT_ZpQSzBFuRWmAZnfpteH_VTb2tDGcJuTPu6gCcYoH1mQoV8MbS2QwSR5GQvbDzhZ6Mm7mrcHah0JOWR0Z1DOmmGo1B8C4CGKdg_VBjH9RWTQCQ9Vbk3T-ebZZHQ8scRLcn3D_4jOnG5-RQ_YSvp0jykc9GTmOpgDV03Oa7dIchzK6CwsnJvgbecAkUf2MWqR8Jq6a-OILS7ySeA7RVSCopM7f09Ws9SMqZCdTUNFinIPs--rrM8yaGHJZ_91OZTnJEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf11ae109.mp4?token=FbWn5WQH4hhdm64i2S-D0IxMu0FSS-BPtmF2YHBQ3hmJi_R6uzXL5wWZXIsiySYGXEKCHhMq7fQBWRR7-dT_ZpQSzBFuRWmAZnfpteH_VTb2tDGcJuTPu6gCcYoH1mQoV8MbS2QwSR5GQvbDzhZ6Mm7mrcHah0JOWR0Z1DOmmGo1B8C4CGKdg_VBjH9RWTQCQ9Vbk3T-ebZZHQ8scRLcn3D_4jOnG5-RQ_YSvp0jykc9GTmOpgDV03Oa7dIchzK6CwsnJvgbecAkUf2MWqR8Jq6a-OILS7ySeA7RVSCopM7f09Ws9SMqZCdTUNFinIPs--rrM8yaGHJZ_91OZTnJEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥲
پایان عصر لواندوفسکی در بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/Futball180TV/90061" target="_blank">📅 08:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90058">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7e2f01eb.mp4?token=pX6LI2IfNA3q5S-1QMo6HzbsmgiCruHuS2X-xqLqYc64hASooZrbyfGintjs5YRzS0wGBALSeKwxnZ2y1qMRJzxw7k1UaKSz4KnVVnZMvOp73Sx8KWMJhcz8Pc_Iw0iZ5BJRtoNuscY2BMn2c2GBPfgpnvAcl6IkOZe11ijIFjses-ey0brt-mTQj9wZ4EvSpgqQ4yXAQyMUN3rjZDiCK6_ycxFjt5F2OF4-8UR7JPhHcRMRGXtU2CcBSeWYts8HY6vce6gglJ_Q3Mfi-AEPkUlg2xWpPFFWH1AcEnxxvhegn-_dB6ISoDMioBM3tGUOB2_mgfU4SFsHLj5efszjeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7e2f01eb.mp4?token=pX6LI2IfNA3q5S-1QMo6HzbsmgiCruHuS2X-xqLqYc64hASooZrbyfGintjs5YRzS0wGBALSeKwxnZ2y1qMRJzxw7k1UaKSz4KnVVnZMvOp73Sx8KWMJhcz8Pc_Iw0iZ5BJRtoNuscY2BMn2c2GBPfgpnvAcl6IkOZe11ijIFjses-ey0brt-mTQj9wZ4EvSpgqQ4yXAQyMUN3rjZDiCK6_ycxFjt5F2OF4-8UR7JPhHcRMRGXtU2CcBSeWYts8HY6vce6gglJ_Q3Mfi-AEPkUlg2xWpPFFWH1AcEnxxvhegn-_dB6ISoDMioBM3tGUOB2_mgfU4SFsHLj5efszjeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😍
خوشحالی مارسلو برای نیمار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/Futball180TV/90058" target="_blank">📅 00:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90057">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lj7wHfWuUcccBTUqYXjPbYwxJBiHhTwq1BBxiQe6s-DqEd6GCpByGqG89dup-2kRrqcIlqpTxcMFAprXCXpOR8uc6BmpZ9UZUejN07qNEQr66-w7boaULifjMvGy3WKmw1jzWraI24HmCZDnykE9MsPXxlRhb08L_xRrh1h5BxPks5VAwlaDnT34Tr0i-Nfp_-dtR5Qli4t5rzZG2Srq0Ik5mb_B_AIN51q_0xJKQ1CvN76-GhaZIZqzV8dcYBD47W6NshbQfiexfn3LFdTOTeoNhgewfHQcr0sn0d1MHU5HTXvbdf-2iudbp3oXiBi_A0lrxsZqTStrKp48MqLErA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول لیگ‌برتر انگلیس پس از برد امشب آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/90057" target="_blank">📅 00:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90056">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZjxfA1etEWCIk1eGfVJLJCDyhl9t79zeDlDAX-rOq1KYOOrsbqISUxnAHxGe8OLyHZwAxEMIBtDXnipFY2Zc8LQ6kDFCH842TyLdkM5xUbuezRw0QSOG71UZKtqJsl2Xizi8d8Un82azaLtmKUTt7VzwjKOWOeOCQ61vfTQQ2claNE2HeX8B1UjHPOjC68CX7Nkc35gecmKSagFBQH4nAfVO0YZJC5CRCACSuQWHiHssbU8saNW0CLxJsyYr0fbqfJLFdpTTIi1ui9dPfaqrhVRAB26FcsEi25lsCAaa3ZQWwnFANRACx4Z6eBOyhrCatiChloFB2SisdzTKojYhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
لیست‌نهایی تیم‌ملی برزیل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/90056" target="_blank">📅 00:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90055">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7w40lm9D5i3cEXu4V9t93pgb_JbAzV9pNBNuoxOGwxjVP-aCb6v0m6lgtIXDvDfoTTAlrFcLMlFwPYunPaiut96t9Q1Hnc0-qlAMMYutuCEZAm9bd4c212nUm9fY8QXKqUtzaJvrvXpB4I3J1Jg8tBvc-Q4Ug-_p1HRVCE56G7hIQjJbHi6L5ySuhdkWt_zIK8mdgDWQKfxd6SN4WiBt-Hi_jQWEtC4c3nnUZtpTtMvn7eg-bg3YWe-0pI26GwJturSjXnoarrIT1xL0qA8UyAN97X28zc4bW5Edd3Z1qplTWxD4N9v3JyYfCWpqEG7zJ3Mym_KHCCmCpqSXwB7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نیمار بیو خودش رو به پرچم برزیل تغییر داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/90055" target="_blank">📅 00:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90054">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6072fc8645.mp4?token=nGLRoKLXHGDR3iqqtm-7XMQeSy1hM2X4Bfi1MmKVZUiaEm2U_iRUbzDYJtyMq9vz_WwA3B50ULX_rbs2ZBEpn8KDmP1diTcykQ8GZ2gGUNvulBVJIsdnOifL7_T1p8TMxO29XCbHWFf4SpKcKBgjGwORCO0M0UD194kWJNDC7E6CnX90uCWRmYgZonKvLbxH5uN1U1UfoVKrylciTqam8-wPc1Wr6_Mwr6WSN0Gt372oU8Yr96HPU_xGfySmfBbUaOgAliP79TmTtGYU51JGaHn6h1Kw7ZEhSIqDjHz48dmQezUvDWJoqFOGHtaYixLU4mJvjXEmHGJciki2ZKZQSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6072fc8645.mp4?token=nGLRoKLXHGDR3iqqtm-7XMQeSy1hM2X4Bfi1MmKVZUiaEm2U_iRUbzDYJtyMq9vz_WwA3B50ULX_rbs2ZBEpn8KDmP1diTcykQ8GZ2gGUNvulBVJIsdnOifL7_T1p8TMxO29XCbHWFf4SpKcKBgjGwORCO0M0UD194kWJNDC7E6CnX90uCWRmYgZonKvLbxH5uN1U1UfoVKrylciTqam8-wPc1Wr6_Mwr6WSN0Gt372oU8Yr96HPU_xGfySmfBbUaOgAliP79TmTtGYU51JGaHn6h1Kw7ZEhSIqDjHz48dmQezUvDWJoqFOGHtaYixLU4mJvjXEmHGJciki2ZKZQSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
🙂
شکار لحظه‌ای صداوسیما از بازی امشب آرسنال که با برتری یک‌گله این تیم همراه شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/Futball180TV/90054" target="_blank">📅 00:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90053">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdBZ7w0N4G9UxtQK1vPYiEdLTmDJ3MGpbmkIAhqoqYSXrdTuSO8_lejGSlcvB4n2xce3AV3XnOOJLaXoyTl2etwqrLdUOK38Dr8CrD73legW5rodqi9hzWa3jy0cvZHAYo1JqFjFB8Z-SftJzyOFZWrQQ9MBUBWDP7qIjvR1ZwApjiEPE9sb449gFNlyPtETjrckbLGkaMSJxG5hUeNYS8w_LRDRpTfiGmJqAfNtk-qCslH2E6nA7jpwPDMVW6il_tVlg3tQ-74GkrhS40OZdw_MBi1zmmROcv_EwArkIFN-hqQBqf4So4U5flLtmOWzYw-XghdQWV9D4oIjzQGZxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نیمار بیو خودش رو به پرچم برزیل تغییر داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/90053" target="_blank">📅 00:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90052">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🔵
🟡
🔴
با اعلام سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان خواهند بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/Futball180TV/90052" target="_blank">📅 23:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90051">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
لیست‌نهایی تیم‌ملی برزیل تا دقایقی دیگه توسط آنجلوتی در نشست خبری اعلام میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/90051" target="_blank">📅 23:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90048">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
❌
پپ‌گواردیولا سرمربی اسپانیایی و پرافتخار تاریخ فوتبال از منچسترسیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/Futball180TV/90048" target="_blank">📅 23:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90047">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLLmKKb1vsYxS3PKhG0I8V-JGd3Kk9lKrWntFydNloSUvAE7mXidoBzccPvthOQr43lBEQpO4BKjYlig3uhnt6C4qy-MlXesBDa9F6gaaF1ewcXDanCdhnV6A2ZdDMdWllY9Q-k8nH0B_OwLPksL34xur6zY68SeIKtAVfb6P6jvLqx_DAv1AHq3_qEZlQ30X9M1zm8mWtMEBLsaar1S0Up7hyJyF_PvrLWy90xVNLL_b1WmSkZp0hQdvsJJcSLZUw2k_8_2POzYCWKv23h0SfK9GbiB3BxdD32Cz233mulfwHYFqxR9pV4fJP4wneLPS7XGKWtxMexQxU5Szh4qmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
❌
پپ‌گواردیولا سرمربی اسپانیایی و پرافتخار تاریخ فوتبال از منچسترسیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/Futball180TV/90047" target="_blank">📅 23:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90046">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🇺🇸
‼️
فوری از ترامپ: امیر قطر، ولیعهد عربستان و رئیس جمهور امارات از من خواستند که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی را که قرار بود فردا انجام شود متوقف کنیم، زیرا اکنون مذاکرات جدی در جریان است و بنظر آنها، بعنوان رهبران بزرگ و متحدان، یک توافق حاصل خواهد شد که برای آمریکا و تمام کشورهای خاورمیانه قابل قبول خواهد بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/90046" target="_blank">📅 22:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90045">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28244d9b4.mp4?token=WUrRMj3KnGZQ4VUjuHGEb_0lZQuIQk9bhQVxEFwgY3K0fSQsWxH34-G6XVwaoq2TTigHVuMH1cBHuTac7xZDCgooxgXHlMNVXj-GKgA2p7sFgOOaRSJs3knTP08xyaiFfVj-U8KoBLvfdeRPrwzK90zk_tpwpWD7rHlZAp5aJvlKVksU56ueRxhAE75xwq81NuXBktQeJelRuLDNB0kSIynshPZEJZ_qDlaNxAog0pzSz40XtDDiShEqnIc1FP88ISiTS57Ki0vMbUjmbRsSlw80i0lzE-hFPV7toVydmki-A6_HAKAVzKSD56v7aJTJehzxzQxQI_h0zHaci2jVMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28244d9b4.mp4?token=WUrRMj3KnGZQ4VUjuHGEb_0lZQuIQk9bhQVxEFwgY3K0fSQsWxH34-G6XVwaoq2TTigHVuMH1cBHuTac7xZDCgooxgXHlMNVXj-GKgA2p7sFgOOaRSJs3knTP08xyaiFfVj-U8KoBLvfdeRPrwzK90zk_tpwpWD7rHlZAp5aJvlKVksU56ueRxhAE75xwq81NuXBktQeJelRuLDNB0kSIynshPZEJZ_qDlaNxAog0pzSz40XtDDiShEqnIc1FP88ISiTS57Ki0vMbUjmbRsSlw80i0lzE-hFPV7toVydmki-A6_HAKAVzKSD56v7aJTJehzxzQxQI_h0zHaci2jVMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
لحظات احساسی لواندوفسکی در رختکن بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/Futball180TV/90045" target="_blank">📅 20:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90044">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJj5ZBNZWk1CGm0Km9CAOnX7Tc8MhfGKXiMyab9Me0uT2KLOuyTnLvlCtvDpkyuCXPKkPXkxt2nn5rRBCVhbWRe8JMRNGkBTsN3JYqUyEVVsjiAq895iO1nsztBvO3_KEMTEKmsGQOzU9wwLM8XfV16jn3s7WVrxEQu5GGuirXmUEi_yW2zc-jfX8YWodpJjldN1LQLTguzT3lF1PpK-77vqzEfYEMLgDSKcd2gVT6L0je46tC3g5aYGdShxXDz_aGoFeaMBIANbgXalzRgr1mBeLAndT4QbZj5n9jEcFNtLp790Yx0usbcKWnZOt1TT8WD4ykqs5HaC5cHLex2Kng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
عملکرد ژوزه مورینیو در رئال‌مادرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/Futball180TV/90044" target="_blank">📅 19:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90041">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssEN7an1O1s-pKev7bZbqKgNzZBYNCE9CKJYu6P7BlgtSXU_zcDWJ94kua4k2jlhnlj_I2q9sqrFf0INqI-i0tbsqVNxAR9aUYzIeyecGE629IWH44kWJYs9AgujwAL4IcMqbd6nsft1EM1t0TaJhCxsneLd4zUM68LoFIM4XkbCbJHg4wx0e-9Bym6A9x9YbasdtCUeaWt9INYXlqWyud7fMjw20WkZVO1z_LtFqF2gSeZfE9Bt_pz2Ida7kuljZrCSToTCy_rwhVEob-SsFzRdvlrGqyjqhBrXN_VLSzQGUY5cp0QxblPMvELC_XJHOnDqwDZSq8a-teHF3UiwNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌هایی که تا الان سهمیه حضور در فاز لیگی لیگ قهرمانان اروپا 27-2026 را کسب کرده‌اند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/Futball180TV/90041" target="_blank">📅 19:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90039">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsCuA0SVOwNgiogHUQh6vPT4lwmPCGYtCCN4RYpf0_vuNkhapWDo7c515fShQ_oYGGDD8fysi8woUvC2RWR9TMARNdPL38VS2GgiR6aal4-QJ6Gtw066hy2HnKz8NebQv42QOZqHpkShpvfm0Xmjm_fE-xCAN08wsUpAyw1Wg4W9NS4AcEHIoJDyHE6TgQ5QOok-ix82YcHtNTIRmidbGChm8KW0b-1YLdzUfg5AZyznS_9kejeGBqDWcRPXnOBfggEu6WfOa7AsV2iEX6cmMZ-g9DJIoUZ1Yj8-sKwQfAcGIQMGwyN-gsj5Jy4ERcCNqEB8ruCpLVRObLY4bnidxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
لیست تیم ملی کرواسی برای جام جهانی 2026 و پنجمین حضور متوالی لوکا مودریچ در جام های جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/Futball180TV/90039" target="_blank">📅 16:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90038">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNh2UFJPhTLlAHr-i6GherPYPPv22mcsJVtnlmF6GqS4a_LgCbUMF0xvnZY45i44KP2WBHQ5Q0toNQYQA9VxTyGYltIpihqyC7YvrORUXVuYUE0CZNGeHl0t1ccX8ajgcQgpIpthEBx-6yrTdFLyipDQoKBNowM36CzE9fSxUwR5hCwhzEgZIMrvwL2sHLKN9b51Fqd8gnRX5Uib-MvboDQFuSyEIaGvv05zBa6BGsHuyKL7s_m9isL-J9CcN8xmymV1ZHPQoZ1s-XnOd7Fk06ABrz4Untpg3VB3JIOSKFMXRCk2dmueaxCgKz6R9NaxAzTi0ptli55-JRdHiBuAVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رسمی: هانسی فلیک تا ۲۰۲۸ تمدید کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/Futball180TV/90038" target="_blank">📅 16:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90037">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RAaX6R9BmHtNQ9K4wNxfuUv5An6ShQ0rnSN1eZYKO1SLpa3LKGTZyJvap8a4Vhl9IQkETcF1lHgqATQ1ut0e31qrcvASxvkYVKq1rYhfDrSyq6AdtzEKP-xSKvtPmsW5JsS561TLFj9J7y96_cyyQNrslp03i0hKpI3LY-ddJr9-oXXdsQanfOszXnS5MetCciMsCsAvK__lML0XdyOsdDlGfDR1vU-SsdR2jTKRPvUWaIB9CjUErrgof93KVT1FMV2eL5HbrCGXj72PPIGduPVZQ6vAlIoySfKmCZuUjI5VXV6xA5S8CQC5YC3zOdiiZztoa2mRe0DmFdf0ep9oGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسمی: کارواخال از رئال مادرید خداحافظی کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/Futball180TV/90037" target="_blank">📅 16:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90036">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iy9W2HhNEzESFqa5P6PSqQHIeJEgeLSEKBo-6tFbxH1-r_nPByfeR3i8kmp8y4n_SzW4WpjPcOi2wFWchPOhFba1gR3ffCYUnakBamZJl82x-wJ6_pojIOC_NskhRO8fJOvi_X2jN7rZJPmukW1B9GLyUcK6vbyoVQN3FuYq4E8fw8eWpEpShnil3Mvh-GZcLiPszTwMadBZLHgSkof1dKnYAfTpmaGanNNz_pvxXJ1wEbZvuisbszgZYcB0H5umMUwa8aeOuXj4jyptE12ItsZvFMTcHwQfmpQKGE1mcP83Akht-mvTxhIMQ4youdCPEmVxcO4nsflVIi8DUF6tbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/Futball180TV/90036" target="_blank">📅 16:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90035">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8EvLXmWRCtOyMXk8GM5pderC9TJWMx5LHsLcdbE9S1CBz2RNEXz_ek8kxS7BnSdUORkbyP5txNv5fqDCVdGmV5xsETO4_DnnNvcktHJKCOxN3i2J-EqAtySFYFXM0gvjFFaGNyJlTE3fi9rWChslsUrjhMkw1jGfIN-k3HWUd1tcqJZC_ET7LWzM6X1yVhGx_d_J4KBhc7-Kd3kV_y4o0E7C_bGmYlMGC4mAjvnAw5AdDpbhorjsvZpLxdiXYcn43iMR1VvcUQM-OoWi5nfXmAHf7PEHVy-QwbzQJFuy3iabebqaCbeX6JWaMTEbpA_N_QNCPMqeHbxQAHXl0Mggw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رکوردداران بیشترین بازی در تاریخ جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/Futball180TV/90035" target="_blank">📅 14:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90034">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afcf96866.mp4?token=T2bil0KbnDI4iOlHXQDvJV-4NauVGSIQmhE4-5emnCw2r-mL6NJ9T3AqicVhXaN4I318QbqkTipYLarsbzTmFNkzdf5TevCibuVb_ZsT4p1lcOI7lTh6u16cyNA9wFL254-H3OFtt2Nt4CQ8lLVWYrhVj-EZZK2XRL8eSBBhe9Fzqd6_CxQdzLAaWz9k_UHj4ZqUUZFVGxPTOUjXh-RDiJjfjWRi5a71Zh32nSqiOf1Q-gzvncbSaErPJxaTzdaVuT-VKUFzbynBtqy4gPl_lN34jwdo8fcuXhVL83EeoRqyRkO5F18u8QhgOTeGbekH1THc0WgdsOTIRJ249PNANQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afcf96866.mp4?token=T2bil0KbnDI4iOlHXQDvJV-4NauVGSIQmhE4-5emnCw2r-mL6NJ9T3AqicVhXaN4I318QbqkTipYLarsbzTmFNkzdf5TevCibuVb_ZsT4p1lcOI7lTh6u16cyNA9wFL254-H3OFtt2Nt4CQ8lLVWYrhVj-EZZK2XRL8eSBBhe9Fzqd6_CxQdzLAaWz9k_UHj4ZqUUZFVGxPTOUjXh-RDiJjfjWRi5a71Zh32nSqiOf1Q-gzvncbSaErPJxaTzdaVuT-VKUFzbynBtqy4gPl_lN34jwdo8fcuXhVL83EeoRqyRkO5F18u8QhgOTeGbekH1THc0WgdsOTIRJ249PNANQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
📍
Tehran
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/90034" target="_blank">📅 13:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90033">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n26nUkRuFLZXp2ya2uAtAwAgI5bwsD36fgE7huc_RPwN3TomI5W2ewS0ERg6slv1M8_vCWi5SFlaszonFb4O7q41TK8BfMmsFia1EOIsNL2SmVZIKRzN-3jrTp_UdvKzD83NEMCdtdu6W6wnnSUhg-5Ds--tiQRE-VlUH4jfucfPb97NCi9xkpWUtG9yWRYKNukOcLq3QMnbrqnJNwGw2S-589i4ydPBFOSrDDG17bplyUJZabj1sEoLwlrzwcpb42sAp_-KojwkB8WIMh81K70aEew88QTXG830O3NY6T0RhwAUGnmPHoJgqLOcZBbYJz80PSrRNVn6j-KOAQ7-vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
روبرت لواندوفسکی بعد از آخرین مسابقه‌ خود در ورزشگاه نیوکمپ، عکس نمادین اینیستا را بازسازی کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/Futball180TV/90033" target="_blank">📅 13:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90030">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9bd4b703.mp4?token=GE43U_Utno-PJVVXAlRRkaBtekvw-yIAMTrpF8H8j862s6ZfY93AE0YDRUvnkYqppcHde8280cJ9IljBOsgn8qfs01k_BAyYJgdGAimDR-re9hWXRYFkueuGua_VAShTqtkcBQUfWyGbnlUZ9DPU4e-SjF4SXBvUDgYo9_bbNKfnEEJEYGG80ZRL047fvvLkyzPiSfXIKIpNYzns6sPkrEzngWNi6QURo5CN3NekNXwSucbtofhycyN42sCY7MJCFP9WeBR8vTYdtsr6WHinlV1Hvk6ONyWaRDMLy-KawSPLQinWeyiolwAfVDyZSNJ5sHzV_yjPCrbwoK72ARnN2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9bd4b703.mp4?token=GE43U_Utno-PJVVXAlRRkaBtekvw-yIAMTrpF8H8j862s6ZfY93AE0YDRUvnkYqppcHde8280cJ9IljBOsgn8qfs01k_BAyYJgdGAimDR-re9hWXRYFkueuGua_VAShTqtkcBQUfWyGbnlUZ9DPU4e-SjF4SXBvUDgYo9_bbNKfnEEJEYGG80ZRL047fvvLkyzPiSfXIKIpNYzns6sPkrEzngWNi6QURo5CN3NekNXwSucbtofhycyN42sCY7MJCFP9WeBR8vTYdtsr6WHinlV1Hvk6ONyWaRDMLy-KawSPLQinWeyiolwAfVDyZSNJ5sHzV_yjPCrbwoK72ARnN2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استایل متفاوت جورجینا، همسر کریستیانو رونالدو، با موهای بلوند شده، در مهمانی جشنواره فیلم کن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/Futball180TV/90030" target="_blank">📅 11:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90029">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnd4BbiFdzHayG9Vu5AW5nuBoRMzvZAqUp3nYLT1zfnZjCg3TclfyJP3DdIGG1SNmh7wpFVcclRVeW971tsGXbnO4hoRnKhhWkPBRPPwoC5A8YqZ3F2yilfLaHoI0Zz999QVR1FwbALEG_wAitpZBzLj69fgyPrThgfbMFxCQ8w-Ds7zHQSZnhPknEBo8dOSqI1dnICHYGwzketlij7SEw8brvPgJgyzZV0kOm7TYVmaf7Zn6i242xu_KFZ5Y_9-vZfAAG_17lujjjAGovNijV6OmhsAedBoM7hiXcv5Zb0_E4dVVSDIssi7TwUOeYX_pNej2iEOdLvzmQn5ERy7oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
سرنوشت تورنمنت‌های رونالدو با النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/Futball180TV/90029" target="_blank">📅 09:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90028">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441c980280.mp4?token=WSNaye2oaefITrvpe3H56WTTVlvDKViIoX9Zd0VSMLD8FP9T6Zp_2jNaJWbLhFC_1pvg9meNghnpzdPi6KJnE94ZzEmhdbb7pqUixmygivN1BuwuCP1kw0BTHmKyko7tK0rK_C0-D8cKZArEzU9ByIvp8CNylu9Ub8sXE_b2y7qtQGdWWKo9kCsGFwpfy1_ndHAUWIGposgj_PAKLg3Wzv7tmo0SRfb8xAfFu6WYxnS2moyZ5zu6s_x150swmDyaft9EtNxAaiQcITsqzxndXyWgSQoP7xTT5oq31ipydtcgfwRb71N2lG9wTBF9msw6rBLNkQNHcI3uEsvauRhfRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441c980280.mp4?token=WSNaye2oaefITrvpe3H56WTTVlvDKViIoX9Zd0VSMLD8FP9T6Zp_2jNaJWbLhFC_1pvg9meNghnpzdPi6KJnE94ZzEmhdbb7pqUixmygivN1BuwuCP1kw0BTHmKyko7tK0rK_C0-D8cKZArEzU9ByIvp8CNylu9Ub8sXE_b2y7qtQGdWWKo9kCsGFwpfy1_ndHAUWIGposgj_PAKLg3Wzv7tmo0SRfb8xAfFu6WYxnS2moyZ5zu6s_x150swmDyaft9EtNxAaiQcITsqzxndXyWgSQoP7xTT5oq31ipydtcgfwRb71N2lG9wTBF9msw6rBLNkQNHcI3uEsvauRhfRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
جادوگری بامداد امروز لیونل‌مسی در آمریکا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/Futball180TV/90028" target="_blank">📅 07:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90025">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k217td1GOaxF0R5eh4DomQpLRzz37rPKdKm6LszzcPkzysUVIeNO_03RfnlT_1HD3gh9VJVkR4pQD4Crn3tVGMx9lb3uqrhpkmJcChobXGH4SD65N6hBA8P4Xy-1GKUtdvbCtX1Jf7qvHJRGm9gFVtk-mJfNivm1HzMxjb5jF_F1CZD3yY14HL57kKSNVuDRawKTs4o1PMavef1lU510dY-p3x0PZTFpmWZv-kjdo_t1USBufuXYIVDvet2HLfBIiz8plwyt93EKKPuLLzJMVkX-QH9R47pTJJ-0mo9wSlrv_DOwyrEhV-w5mRpOKapzH8lv08dA3Bxbo6tyQcfqnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🫪🫪🫪
🤯
برای فهم‌اینکه لیونل‌مسی چه اعجوبه‌ای هست کافیه بدونید که این بازیکن سال ۲۰۱۲ موفق به زدن ۹۱ گل شد و تیم وحشی هانسی‌فلیک پس از ۳۶ بازی لالیگا این فصل موفق به ثبت ۹۱ گل شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/Futball180TV/90025" target="_blank">📅 19:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90024">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af6bf0b38.mp4?token=kufz7FSWnB_tDtA7zFlvxMeKrdGWVIOU2bSRmJpsN_bIlJNDFIg7LNCMGEJv8soc0jSz4m-qYgl-6y0aFNpDmLtThpcIwb4QaZJpvKdu6B3wts9IdfDTOyaOauE8tKLqgHTPLDOsZ05LLRliu9WEimatXO94uI9hHm6OadI2sQ_HyrLdvNCC9DPWB96vvz-EGHTl2k9pwuPWlceBsQMWk1ZkfgBt2DtFblj9UWTkbAFdhXGUzWqFACfMaCBI07UoInP0SHGbuUstsvcb8z9RMnJwcfOkyAyhkA7WLn7DoIQSMVhDHxjsWb2UBsuv_GbNcQOknlemaLQ9B9-B4agz5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af6bf0b38.mp4?token=kufz7FSWnB_tDtA7zFlvxMeKrdGWVIOU2bSRmJpsN_bIlJNDFIg7LNCMGEJv8soc0jSz4m-qYgl-6y0aFNpDmLtThpcIwb4QaZJpvKdu6B3wts9IdfDTOyaOauE8tKLqgHTPLDOsZ05LLRliu9WEimatXO94uI9hHm6OadI2sQ_HyrLdvNCC9DPWB96vvz-EGHTl2k9pwuPWlceBsQMWk1ZkfgBt2DtFblj9UWTkbAFdhXGUzWqFACfMaCBI07UoInP0SHGbuUstsvcb8z9RMnJwcfOkyAyhkA7WLn7DoIQSMVhDHxjsWb2UBsuv_GbNcQOknlemaLQ9B9-B4agz5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👋🏻
پایان عصر کاسمیرو در منچستریونایتد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/Futball180TV/90024" target="_blank">📅 17:35 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
