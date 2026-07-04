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
<img src="https://cdn5.telesco.pe/file/hUEp8XfCtW9Z6zlJulYiyVgtsTiHF-ATVrStROt45Au4lncQBrxpxkxE7MvsHaoE6Zzypv5CecIUaIn9aYTa55D7qhKNd2Vngcow0IOj6Umwcwd4b-edKrosf-w1w425pidIkYSQV3Qdb7y4ZL2MrwEUyVKmuPjcVKW111328VUdbsaei5kQxiNrTjUSLn4JeCOXsUqvsKrI9lzosuOI6nBw6JBlGS3gM_Sz6SXo0_e2SKkn-e25XQe4MakN7q-C4pq7pVTW1eKe_F5Az6keGmkQ58VWRcVod2aEOO1fLVT-udjXUOk75JkbwNwi3UguNq6Que5AjQA_57XW3YpmiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 645K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 04:34:58</div>
<hr>

<div class="tg-post" id="msg-98107">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfwDc8GzQhDFX-A2sk6vhyRZXZdo-RSTLkU2Qbd3FDWI_VvZ0NpdoBOazq5lVBsWtfSp6rWknwWGjZq_S8fcN4lymtjMz7_OoHwi1aZClX0UgIXGfv4GxvuYbCkm28HMqB37UEFaP_0niNEFYQJfYaoPXTtQTF8lQux8X-WcpYp8rDBKoTOTAnm1NYzVE70dY5K0jxmNv3E1SJk7PrEK0RPpxRx78BBe6ImxhamUC3FfNpUE_LTO-0XUy4nX2yM2TdolGh2YkahDGBZBJJbVk4pmQgOl_nEojvZvelGbEXdPwWfcSm_jC4qdV2aS9UAjXQPOm3UnYmuqmDXGj1jJjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاتوووووووووووو
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/Futball180TV/98107" target="_blank">📅 04:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98106">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhL5QKPpgmcCSzyQLpH2gambaLVK7xP4Ipeyju8ORd2b4yughgGtaoz_1FbTDZKIQg_RhUfnFPOqbE2xtzcAhJpLRRLwS3tQYzNmCiBEte3r6g0tsQ_hFugKgZgsy-jptq8QmiFkromwJhj9uN-V5SV3C9Ouri3kef6xE2Jd68tAENIOkv71UUbvt_WG5LswHQQKxqQyc3245VS9u12pj-rZaskVarNmFLcHTqlKUufAgLjGwe9UkxrXPt-zd0pgwbLoyHIhCh1FUkuPEKTD8abBadvYe7l245Y8ip4zLAV5_rJ7yaopJB_gKJV5Yxlx_vIeZr_8Ml1T0dQ8gVxigQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار خلقت در ۳۹ سالگی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/Futball180TV/98106" target="_blank">📅 04:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98105">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🎙
🇦🇷
🇨🇻
لیونل اسکالونی:
«می‌خواهم به حریف خود تبریک بگویم، آن‌ها امروز ثابت کردند که یک تیم بزرگ هستند. وقتی می‌گوییم که در جام جهانی بازی‌های آسانی وجود ندارد، این واقعیت دارد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/Futball180TV/98105" target="_blank">📅 04:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98104">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPzHPiI8HNGSTeBHLkBxHxGA8bllAtaGpOXUrOihAk3sALiF_hl32aivKoGKWm8tm_M5jWHwzn7XwUThYmv6ImzWULs7sgDl_GMXNrVuwgZuFf7xFQdUo7tprzWuf_pmOi5mxHxNZKrxv6-ZZInoU56QQqaFSjtAXCFsb6NhptLAq4MScLkadzCVkyOHvKF-RYnNFv0ifV7SoAOvlrZ3TqOUoBu0aVvKl3izGDKUSD7ubWMe6FnD0GXF3P06bAQ8kJBy12H2tKors_pZ3_9Kjxr3IKP96Z8wshPqmX5khjV-d9Eq8cXGS1B8qk0vEu1o-JQGDwaSu7mgSFCldYaUFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/Futball180TV/98104" target="_blank">📅 04:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98103">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTAnSbrxUj-NABfceo3i9xAZizEnVN8qLI8Fe6xBaTkMCp-pKfx4SO2mH5rIkZcd3IDCa-RilTZqqqKg8O5NIbsthdKAEbDdj-uOZvDjllkxdgKa5-lrF5q-8onXpiTSUyaZefm5ywwDGxfit_FXjPp8vMRKOXMFnnaMsunQwOi2PEVJejiwTfH1wTsysNBziLj0L68IJG7LMxsjTWrXDJrGe18cwl_qn6S4DhynYuCop5t18EO2j3GATF7uLODOKYFRqVQdBUxyzs_cKJ9qjRCiWW0nqJikebTz_H9VZIe6YaBprDjk024p8VtOcVMkz0vUy5UclNy-rI_sU20-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🇦🇷
#فکت
؛ آرژانتین (از جمله در ضربات پنالتی) در ۱۰ از ۱۲ مسابقه‌ای که در جام جهانی به وقت‌های اضافه کشیده شد، پیروز شد (۴ برد مستقیم و ۶ برد در ضربات پنالتی).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/Futball180TV/98103" target="_blank">📅 04:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98102">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWIZsjDzRmotjMsgoXnhCDc0G3rX_7R2qR4WgSTqeNpYO0jga0o8URV_xWNGbcz5kRaC5-hVTVYfuMt-RmPzweCz7_w6-VxdDBNIw_1f5AXuou7Dk8OIIn5wpeI08UnxryG70nqa3GeSZi5yzCAL1FcQ7B-eVMxRBHeHKmCAFbQuSQWGeYvxvVLMdtXpVRYKt_9QPIND_h_pLulqKwdO-MfGfRzFgXPIJ1DLZ1xiJ4pwButKIYGNOoifmqfQl7xavlp4YZv0n9Ty2lGK-QMb0UcsaxoLXbDZ867Isu3zxeTmsio6tudJ-uYcEQCPJnh0S3-XnhRpR2HZ3qkiReKK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
گلر کیپ‌ورد مقابل آرژانتین
🇦🇷
|
✅
— 8 دفع توپ
✅
— 5 دفع توپ از داخل محوطه جریمه
✅
— 3 دفع توپ خارج از محوطه جریمه
✅
— 1 دریبل موفق
✅
— 8 پاس بلند موفق
✅
— امتیاز 8.4 از
📊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/Futball180TV/98102" target="_blank">📅 04:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98099">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNDX-vm_3q1qYLQenxpclrb2mhKo4MmeRxuehIvDdcNBuJUipgSJOxseCMhDYEOjMahw1XpOPUxkQZaTtkM3LHYHnB-rBJ-UeY6z_sx0im7BLhO6Z3tnZ1bmil-ZFmyTRIxqOWafuuWelPiAmRZil8D8fgtHgW6aH7MhvoBRQBNDAmvOOsVRDsGZxVCfrGpgbeiDYR3Lfa9LXDY1j8JOIyIDsxsKjDjU70pew6_PpM-jlGQHQgHGYg4jfw_u9VKQWB-_InNppSgGQTRQV1iK3_AL9HNivK9HNTclACM-V-mgbjMTnCq03w6ohzvFiiQREdmO5OomhF1rc9Oa7UBCYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
📊
مسی در مقابل تیم کیپ ورد
✅
— 1 گل
✅
— 4 پاس منجر به موقعیت گلزنی
✅
— 1 پاس منجر به گل قطعی
✅
— 6 شوت به سمت دروازه
✅
— 2 دریبل موفق
✅
— 8 نبرد موفق
✅
— 5 بار دریافت خطا
✅
— 33 پاس موفق
✅
— امتیاز 9.5 از
📊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/98099" target="_blank">📅 04:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98098">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خوب اقای وزینای عزیز الان ما بخوابیم یا سر کار بریم
کیرم
دهنت تموم برنامه هامو بهم زدی</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/98098" target="_blank">📅 04:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98097">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuXlTmx_CJ3BOtQFvDfaeaxCy610jU0a-QSGwoZegXCx2LhOCv8LEvvtZ2itGboQRCv2G-9xx8wiC8iEII6Rx0XBvt62lANZNR9maK8eQ-qmKjKBbYRgBWdRTxc3wzIPlSCaoywlXoOebnVKWsU6g_LTRkblZl1pBdvPJ6ImXdVMhdo9eYg5TAxkKM2DKAmxAKjakxfIYkhQHcbsEYkwVCf37K07Px-Zi8RPkCsVOzH8z5Vx63DRh8CYmTtli5uQmSZkJx8LhF_ZrXzH3kaQAzBkL-xezkWh2ZHwOaXak1r6YM5buPvtEvk4TzmTufDrKjiTeOgA9g0do2G_pdYEwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشک‌های لیونل مسی بعد از برد مقابل کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/98097" target="_blank">📅 04:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98096">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLqdeChgKj4KCnqEu3NNSWhnRY6vn3d8GCg_Z-Obd7nprJ8ZEQmOB-RGufKUwS0X3i6mStJGx7thiSSf_PmFK8CuROBM97rYIsyYAIpegJ5T0HB1I0iT1a80bYYh_lyW0B3DHR82Vde0zOdep2zbh22Mj-7POnvdUIGEN_D5suaYBRZmdJ1SwkMmtq-fvFr1n9XGIn126Q1chUj15f6x-UyL7zSi5DVx7iiJBIG3w7zzj_wT34z2I_INFrW6y74XCm_Uo9ON_2mW8C57MZ_WjUv01FEDrwYL1licxToz_gaI_lAoXUMz-QQUMWjysK81CqWWEfw48tBuOtcxISXhCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیپ‌ورد سربلند ترین بازنده جام‌جهانی...
تا لحظه آخر جلوی مدعیای قهرمانی تو 90 دقیقه باخت ندادن و تو اولین دوره حضورشون در جام‌جهانی شگفتی ساز شدن
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/98096" target="_blank">📅 04:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98095">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی؛ سکوت برای کسانی که ندیدند؛ خدا با آرژانتین یار بود! کیپ‌ورد تا آستانه بزرگ‌ترین معجزه قرن پیش‌رفت اما در نهایت با جادوی لیونل‌مسی حذف شد
🇦🇷
آرژانتین
😆
-
😀
کیپ‌ورد
🇨🇻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/98095" target="_blank">📅 04:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98094">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vutdl29VRNxiGmERJBSWRL7EwdhVUkDKmTFA8su3iMG0HVZ5fjXHhhh3IzpGK5vaGovp_D27jNzd0VC2nz1DRH7JvvK2oxsEc6-DKv0WSYswMKHhxTazJtY_ct0mondsbUerq32DU1g7uS0GSXnYed_jzROJ3HA0eXL_vLkT5SZGaGsCbQXVlUyXInhS3wDj8jFnHA7q-FUUrXBij-TWcI2VHl6g4M4KPjgB_8IoNDdBDLKBoTt9ILc5GANCKPBsArFq2xvApHcXETA3YX0ODegr5GUTYBV1qEJM-s1TxxgDQ4Vu07lfsVl_lIyIboFZXF_vqEHfwHw1YTied4vKrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/98094" target="_blank">📅 04:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98093">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MW1KDzBrGtQzL8uQojaKXS-IdYhWkQ-hKYuewtuAlfXRxmQUS6wlDuoCx3hahBeJqPTTb6gauDe7bptQLGiz78BJe6CVGXu_1Wc5muUr114jQawKrDm4JTWZGNl2a70Vq3g1q47_L9YqdOSkV2hTaaNq1f7fJjHAsh8XBbpXY3Jwcdn7JTBVaC0hdt4VyPfGwLFw887MALZX5uOzLLDYP1wJMxWC26_0VXnGdqKkLkyfGGyn9hBTUp8jlFGSqq6ejklBpYIrd2-Aiq69oWu7Zj1zTC2oAXjgIdRYA1J1Zu6bN1lkJbni3cDJMnz2L1GxbmQ63IVqmX7MFMkT9E7wdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی؛ سکوت برای کسانی که ندیدند؛ خدا با آرژانتین یار بود! کیپ‌ورد تا آستانه بزرگ‌ترین معجزه قرن پیش‌رفت اما در نهایت با جادوی لیونل‌مسی حذف شد
🇦🇷
آرژانتین
😆
-
😀
کیپ‌ورد
🇨🇻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/98093" target="_blank">📅 04:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98092">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انگار این بازی خدا میخواست مسی رو بکنه
😂</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/98092" target="_blank">📅 04:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98091">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaGiHuVSfpRiBSTuQlpu4ywgupMCzQCIY-mBvqn6YxwrzMHVn7Dvu9SCtMf25TVw4AFEyoTTSWmq_rbgykiokpIn-azenDN0zX5YYqDqLMIJZJ7u6jYX01p05LDbKSw_wobso_zTMDODOXGYOWq6qh8RtM1zsCos5LxVt9zytd9YH6N_QfijkWGNn2teqBn_xFCIyj0ozjaPS3HCrP3RsdM4nMh7zdGwIfuS5eNI-3wCqHwnl0rfmMhpAx48n01RRCez0N23FFjbv1AiYrJBS_GVY8Wp9GCJbcBr1ZQ_8QX2JrULIKFMM4ywkJ3_r2-fScgWC6b-NU3WxBqbssy4uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی؛ سکوت برای کسانی که ندیدند؛ خدا با آرژانتین یار بود! کیپ‌ورد تا آستانه بزرگ‌ترین معجزه قرن پیش‌رفت اما در نهایت با جادوی لیونل‌مسی حذف شد
🇦🇷
آرژانتین
😆
-
😀
کیپ‌ورد
🇨🇻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/Futball180TV/98091" target="_blank">📅 04:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98090">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">با اختلاااااااااف بهترین بازی جام جهانی ۲۰۲۶ رو دیدیم و یک دقیقه سکوت برای اونایکه خوابیدن و گفتن ارژانتین به راحتی صعود میکنه</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98090" target="_blank">📅 04:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98089">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🚨
عصام‌شوالی گزارشگر بین‌اسپورت: از مدیر شبکه میخوام هفت روز بهم استراحت بده تا این بازیو هضم کنم</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98089" target="_blank">📅 04:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98088">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آرژانتین داشت چهارمی رو میزدددد</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98088" target="_blank">📅 04:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98087">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98087" target="_blank">📅 04:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98086">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تخمای مارتینز ترکید</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98086" target="_blank">📅 04:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98085">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
🚨
۳ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/Futball180TV/98085" target="_blank">📅 04:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98084">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6c46fd63d.mp4?token=o4Fw7Htu85Q1iqOwyrp9pIrMk7vyjkehYNbA0KEtbqoIEOCjXffjs-wEjP9TuGXcKtSIP8ChmIIyL9aFuM34NAeaa_j06BnQCQ5DWNDyg9KsSap8Z08MochINYGwIWOgYYAvxsFnghU1n3GgMfGpFyjH93LmfcHP_3mVdutqxO4JFF4zVgtX7ziFGaUlQxHVS1n4OssKwjyyB2PqwsA4rhts_j-gRepaC5RJ7lDEYE2pGimniOyCLKVW3F5eeGkd0CT7HAJHnrz5AjbXhTPPrXqy99nYGAHYJa1udi3pgCGzV7ktKmIFWkCndllchwTbgAHUdQgk7Ta1Hw23lTo83w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6c46fd63d.mp4?token=o4Fw7Htu85Q1iqOwyrp9pIrMk7vyjkehYNbA0KEtbqoIEOCjXffjs-wEjP9TuGXcKtSIP8ChmIIyL9aFuM34NAeaa_j06BnQCQ5DWNDyg9KsSap8Z08MochINYGwIWOgYYAvxsFnghU1n3GgMfGpFyjH93LmfcHP_3mVdutqxO4JFF4zVgtX7ziFGaUlQxHVS1n4OssKwjyyB2PqwsA4rhts_j-gRepaC5RJ7lDEYE2pGimniOyCLKVW3F5eeGkd0CT7HAJHnrz5AjbXhTPPrXqy99nYGAHYJa1udi3pgCGzV7ktKmIFWkCndllchwTbgAHUdQgk7Ta1Hw23lTo83w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل رومرو به کیپ‌ورد با پاس گل لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/98084" target="_blank">📅 04:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98083">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یا خداااااااا</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/98083" target="_blank">📅 04:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98082">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کیپ‌ورد خیمه زدهههههه
😐</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/98082" target="_blank">📅 04:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98081">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پشمام بازم مارتینز گرفت
😐
😐</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/98081" target="_blank">📅 04:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98080">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/98080" target="_blank">📅 04:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98079">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmDx6itbVz_0uFxPfSl-Vg1oZYjF1FmDOZ6RghuCF28HTYAYPraPvy9qkuEgJDR8T0Cr_JZBkrCmz4U4-qFBtwo0QGLrRV6BYcBX3ESZw-tTVHVd-4BGiA-r8nirpbCttQ-ss0gk3pZ3PjzO3igkJGd9uBep50XxwdtdTPFpixSFC7as33VgN0dcy_-zNf_B8BA6PU9nVvSAkdvHrhqQAwXx7IkLNgLlSyIhovaTbb4Hjd62tsr4abifYYIrq0JJ_urFxiYf9b36b6eB7V76KkYwMV6L8-zhm97YKe93AS9gRRxmxhuY1HqrgY1La7nCXMIytEpxE2TeDlKtQVTkMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
• لیونل مسی، اسطوره فوتبال، با ثبت آمار جدید، عنوان "بازیکن با بیشترین پاس گل در تاریخ جام جهانی" را به دست آورد و از مارادونا پیشی گرفت.  • اسطوره فوتبال، 9 پاس گل ثبت کرده است.
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
👑
👑
👑
👑
👑
👑
👑
👑
👑
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/Futball180TV/98079" target="_blank">📅 04:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98078">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مارتینزززززز چی گرفتتتتتت
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/98078" target="_blank">📅 04:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98077">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پشمامممممم</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/98077" target="_blank">📅 04:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98076">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/98076" target="_blank">📅 04:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98075">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cF0YXcuwueKYhIt4uEvKmxwM4mYc9cOXHheUEEoIASixzTtxWumnpvRMhA4VgYTF1fSrEveaqZ9zVGKDhJe7ykD5Mo73xu1B3wsEy2GwlmFBJLMK6eNld9pUCe2X2YYgf0LGaaRrIprEJYlzuROEF8cm_OL75_Lighv6dGxbom1zcVQWxeQqYwP4v7h6G5qW2BBjWtMtg8By9GTff8ZnllDui7HYSBdvudRzdhy2q8I4PRcwlmznhXu8BaZ0L45rseknLXz4HPDzSFAMPqMqRMWfJQKlD7tcG_V5L0bSa-nWhLkUCmfN4iXpyUCAYo55bDPiBfVd1LfZ_-TitlD0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
• لیونل مسی، اسطوره فوتبال، با ثبت آمار جدید، عنوان "بازیکن با بیشترین پاس گل در تاریخ جام جهانی" را به دست آورد و از مارادونا پیشی گرفت.
• اسطوره فوتبال، 9 پاس گل ثبت کرده است.
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
👑
👑
👑
👑
👑
👑
👑
👑
👑
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/98075" target="_blank">📅 04:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98074">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اسکالونی داشت گریه میکرد
😐
😐
😐
😂</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/98074" target="_blank">📅 04:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98073">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پاس‌گل از اسطوووووووره
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/98073" target="_blank">📅 04:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98071">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سوووووووم آرژانتینننننننننننن</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/98071" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98070">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رومرو زد
🔥
🔥</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/98070" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98069">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گلگگلگلگلگلگلگلگلگلگلگلگللل</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/98069" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98067">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رومرروووووووو
🔥
🔥
🔥
🔥
🔥
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/98067" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98066">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جاننننننننننن</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/98066" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98064">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98064" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98063">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0e6e57be9.mp4?token=q7HT9gwgsmdeKGDh7eTOakWIFnzxkE97TaWQl4E02pbBmixS6ucVvN-6rH4QdeoaEedHEk4L_pkRgsoFVn8rvA923sk0ifEIcmWyP62hlS5ptMnfSJh_e_aJ7tI7rftaxF-S0E0-UakgYqw5FVI27kc1d52lz1IR4Evn2vO4eqwN2wy0tMpqKQylO50zPrTrsIaf1XggVkPpk_JP0Xy1cnqzwhmzgEIkRf32FeITX0JCsoTdcJ03Ij1yWbh2VHZ9Tj6TRuTAJspDeXM3mMZJ1RYr23CMi75MP8S-ddNhsq-IjdjH4ZumoNMkZvykZO9MsPYESKrLOCFn81UvymW7SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0e6e57be9.mp4?token=q7HT9gwgsmdeKGDh7eTOakWIFnzxkE97TaWQl4E02pbBmixS6ucVvN-6rH4QdeoaEedHEk4L_pkRgsoFVn8rvA923sk0ifEIcmWyP62hlS5ptMnfSJh_e_aJ7tI7rftaxF-S0E0-UakgYqw5FVI27kc1d52lz1IR4Evn2vO4eqwN2wy0tMpqKQylO50zPrTrsIaf1XggVkPpk_JP0Xy1cnqzwhmzgEIkRf32FeITX0JCsoTdcJ03Ij1yWbh2VHZ9Tj6TRuTAJspDeXM3mMZJ1RYr23CMi75MP8S-ddNhsq-IjdjH4ZumoNMkZvykZO9MsPYESKrLOCFn81UvymW7SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش اسپید لاشی به سوپر گل کیپ‌ورد خداست
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98063" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98062">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_C99qTf-VEtM2GmzJaesbOps2RfRatOdKB71wk9Sn87vQMcRqLC1pN1x5gdA7_efAl6kgK_g2IONGm2OL96Bdfi9nWOV__a6NX8ce9p_6oFmHOtYK4CHd3adh9sPt1yfGgeZ2_qRhCqyIYggUw0CQeXKWig3_YlUrQCvmQ12FGdARCzr7P5eSNlmiGMF-_MgB_c9i1VSc51Yz5TMvMtoZOqMRdC0ocHe7oKGedtM2xo-tWHxcT_klqwItET5GQMUPdh4oiadIxwHybrkaKRuOoCFm7xy1RE80fv3kAYXZ5APPWheSc8YsAS8GsPgd2uxUTe7j7HP48syMvlBKnexw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون شرررررررررررررررح</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/98062" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98061">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آلوارز یجوری بازی میکنه که آخر سر اتلتیکو مفتی ردش میکنه</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/98061" target="_blank">📅 03:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98060">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">جادوگر غنایی رو اسیر بگیریم ایرانو درست کنه.</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/98060" target="_blank">📅 03:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98058">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آغاز نیمه‌دوم وقت اضافه</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/98058" target="_blank">📅 03:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98057">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دیگو سیمئونه هم تو ورزشگاهه</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98057" target="_blank">📅 03:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98056">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سرمربی کیپ‌ورد رو بیاریم جای قلعه‌نویی</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/98056" target="_blank">📅 03:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98055">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اینجوری که بازیکنای کیپ‌ورد جلو آرژانتین پاسکاری میکنن تو خود بازی فیفا هم نمیشه
😐</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98055" target="_blank">📅 03:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98054">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وقت اضافه اول تموم</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/98054" target="_blank">📅 03:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98053">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بازیکنای کصکش کیپ وورد یجوری میدون و پرس میکنن  انگار دقیقه اول بازیه</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98053" target="_blank">📅 03:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98052">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وااای</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/Futball180TV/98052" target="_blank">📅 03:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98051">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مسی داشت میزددددد</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98051" target="_blank">📅 03:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98050">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98050" target="_blank">📅 03:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98049">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کیپ‌ورد همینجوری بازی کنه میره مرحله بعدی
😐</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98049" target="_blank">📅 03:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98048">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/182721537d.mp4?token=Y7pKp-GY06xtZJmikRhd3LYLz9iN5KkFhoNonaLzY7xGXjwCpOpzSuMvTS4Ysp01LVMqacHJY8xQTaeOz_6-Ru14UGSNwAPy568qmvveFl_I2r-2P5oyFZP-lZ12mgV3Rk2o19zx8nBW1gxySGb49kSSN-edWO-92Bs4R2Owr-v27QUZ8iRi9iYU_8UitHUql0Yktwrhs-Cs14nOil1Pxx7pKKiumFsR4EGrJzgVzXRh5sNgYHa5kklEVinigAPoVF_pQAsFMtZESWq6aFyZgtRt6ZkmxRxwyDe7aixlUbRvlEJNxZbRaTt9fABleiYw1sQvTTkWkLIM0vYKyKwQDXMckZfQWpJneS-ePzughH6eyBGi4GjEgcs-K8jjoJ-7B4onfyeT_VKAKC81HjxWchJB8lY9BWE_PJ496wU3h3gPDQoOIj90LHc9LsUy4hd9qwa2t_eMXDnMxAj0bO8WyV8UU363BqBveo90G8xTp9sNRWbtZsYyB8z_nfXSM40eSiwp6xU_0PK85ZAQUeE5c0YhX-xPkFk3o-ccojYrtij3mrWQjMoNL_D_bbccbpOVmec02-UtpB42ExhRUY3rlgxYxI6KWfqUJNwxct_I4c8L4HA2A146GIgHmTyZsq510b8s_2YWUCsaSTAyZAhEM2bWAl7dL8c1HRbnxeGsg0E" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/182721537d.mp4?token=Y7pKp-GY06xtZJmikRhd3LYLz9iN5KkFhoNonaLzY7xGXjwCpOpzSuMvTS4Ysp01LVMqacHJY8xQTaeOz_6-Ru14UGSNwAPy568qmvveFl_I2r-2P5oyFZP-lZ12mgV3Rk2o19zx8nBW1gxySGb49kSSN-edWO-92Bs4R2Owr-v27QUZ8iRi9iYU_8UitHUql0Yktwrhs-Cs14nOil1Pxx7pKKiumFsR4EGrJzgVzXRh5sNgYHa5kklEVinigAPoVF_pQAsFMtZESWq6aFyZgtRt6ZkmxRxwyDe7aixlUbRvlEJNxZbRaTt9fABleiYw1sQvTTkWkLIM0vYKyKwQDXMckZfQWpJneS-ePzughH6eyBGi4GjEgcs-K8jjoJ-7B4onfyeT_VKAKC81HjxWchJB8lY9BWE_PJ496wU3h3gPDQoOIj90LHc9LsUy4hd9qwa2t_eMXDnMxAj0bO8WyV8UU363BqBveo90G8xTp9sNRWbtZsYyB8z_nfXSM40eSiwp6xU_0PK85ZAQUeE5c0YhX-xPkFk3o-ccojYrtij3mrWQjMoNL_D_bbccbpOVmec02-UtpB42ExhRUY3rlgxYxI6KWfqUJNwxct_I4c8L4HA2A146GIgHmTyZsq510b8s_2YWUCsaSTAyZAhEM2bWAl7dL8c1HRbnxeGsg0E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
سوپرگل استثنایی کیپ‌ورد به آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98048" target="_blank">📅 03:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98047">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">الان ۹۰ درصد مردم دنیا پشم ندارن همشون ریخته</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98047" target="_blank">📅 03:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98046">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ای مادرتو گاییدم جادوگر</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98046" target="_blank">📅 03:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98045">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گلزن کیپ‌ورد رفت بغل زیدش
😐</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98045" target="_blank">📅 03:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98044">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ای مادرتو گاییدم جادوگر</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98044" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98043">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نخون این کیر خرارو غنایی کصکش بکش بیرون ازما تورو خدا</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/98043" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98042">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پشماش ریخته از گل خودش</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98042" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98041">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">چه گلی زدن
😐</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98041" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98040">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/98040" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98039">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وااای</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98039" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98038">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کیپ ورد زد پشمام
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/98038" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98036">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گللللللللللللل</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/98036" target="_blank">📅 03:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98034">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMfepr5tbxGaNrmOZj6bhp9lqnBJQ6UXwGnLPDc1sFKpWB0fZ0gweHEcxl5TDTDP3H8R6hnBQTf7vGlb8kkEeTJGLUru2m0cJKy19GN_7XByWBlcmboKgg75cg1dmSesqhPj3vBqKyreyltjCSajKps8vbTOwjlNQna7t2uOSv2OaJII4vPLRRllzp_yu2_jYxp-iFVRkjuq9XDJYejbJS14EPaCyIaM-Hbx6qPrJJkNZax9xLtIqRA2346ZvfLM7lAkuaXkMH_PQiCMm7k5m2lIYuly2lOXnhWPefEKAQv4GoaLoOnoUn3szMWHxtE806OMqbCeozlUXJWs7rccAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Abyok9WZjOdsUpqT5yCxOFVQO2q3Q00ASTnPNXAtCgh3futORyFHE-8ycCX_pljm0ofAz2mchOenQ4ZumIZnwJFmu0jm38Mgt-0JcV1k-p8LDcOWGJ0DMxb8r9CnQ_Q9596CRxxbTbsOZV8LyHggQLWVbWqrcFOoX3zWfpSExNprP6VDdzDwbyKltJ1fDhfV1WMOJ8xBW11ynYT8TMJQjkcBiyQfe0pmVo46wfum27PrcEAfdczz8WKXojv9rInYDc7DQZF96dqjnCuf1RAZ01LmHlzzugwTvTDhs6fILflTFwfaHpNa--7C86sYD-UyXCze9IsWZImSh2ZmkVzvWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇴
🇬🇭
ترکیب رسمی کلمبیا
⚽️
غنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/98034" target="_blank">📅 03:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98033">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بازم خطری شدن</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/98033" target="_blank">📅 03:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98032">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/78229061b8.mp4?token=Gznm2OPvrOoJtoYkG4O43cJm3gc1IbPDpgQ9xYnAg--lDFEjlmulGi9cKreoWPC8ra2WVD1wYJzD4xkySUf386Y9-LdK3sr-dGHB3k9ZPeH0WgynNsEIUz9l8IbyLexoj3jYXQUI6028F2CrgiX_vaPbYYkWhl2mUPZECvsxJMuOBNVHnpKfnAVi6dWY7G-MzOrtA2J5CPpfd8p0KDatE-T3NSCCbyRgg0P8xeJZEQ2OeHkupoplkPR1_2nubUmkaYoGHY16kAQYKAGxerlUkkQcj6BxWbtWdApLtuPhHLviiF_4TQdDPVoDFCAppkebq1T4mP6cA3ocmyEXhHyjMpN_mYbuEr0bt-3RsKRdzBgPJht3B6RugkEZeY8VsHX64w9XnSvWpqB14o87_lV8eh-fSBLTPJ93niPAXpqArZ_pG72KGDl1JFNNTj6nJ4zh5URUhhKBsJHW7QCS-9R3GSzf0UIZs3sInatTU057gjZacxIj1NQdwJqShnXGHbUaUO69yg7RtYiZmAQWsBP1ujgUm8gzxbbJiiEyF-JLbZ-R8y26D6Kxw9LOkxSbi6izt5Yp0WPQKhwz5Taq-sa-QMzOEIzuEX4ZpLLAQ6gOpXMldHN8JIt-573PnEU3Ml9p6YIZr7o0UTXgk-sG04dCwY5fptWk1jbHp1-qWpeMFFM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/78229061b8.mp4?token=Gznm2OPvrOoJtoYkG4O43cJm3gc1IbPDpgQ9xYnAg--lDFEjlmulGi9cKreoWPC8ra2WVD1wYJzD4xkySUf386Y9-LdK3sr-dGHB3k9ZPeH0WgynNsEIUz9l8IbyLexoj3jYXQUI6028F2CrgiX_vaPbYYkWhl2mUPZECvsxJMuOBNVHnpKfnAVi6dWY7G-MzOrtA2J5CPpfd8p0KDatE-T3NSCCbyRgg0P8xeJZEQ2OeHkupoplkPR1_2nubUmkaYoGHY16kAQYKAGxerlUkkQcj6BxWbtWdApLtuPhHLviiF_4TQdDPVoDFCAppkebq1T4mP6cA3ocmyEXhHyjMpN_mYbuEr0bt-3RsKRdzBgPJht3B6RugkEZeY8VsHX64w9XnSvWpqB14o87_lV8eh-fSBLTPJ93niPAXpqArZ_pG72KGDl1JFNNTj6nJ4zh5URUhhKBsJHW7QCS-9R3GSzf0UIZs3sInatTU057gjZacxIj1NQdwJqShnXGHbUaUO69yg7RtYiZmAQWsBP1ujgUm8gzxbbJiiEyF-JLbZ-R8y26D6Kxw9LOkxSbi6izt5Yp0WPQKhwz5Taq-sa-QMzOEIzuEX4ZpLLAQ6gOpXMldHN8JIt-573PnEU3Ml9p6YIZr7o0UTXgk-sG04dCwY5fptWk1jbHp1-qWpeMFFM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
گل‌دوم آرژانتین توسط لیساندرو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/98032" target="_blank">📅 03:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98031">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گگگگگگگل صحیحههههههه</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/98031" target="_blank">📅 03:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98030">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyoKKE5qoPyC9rHGsmcZGZcgDEPvKQwonP553I0g3_1LPMKNf4YxKn2vsN6zaFesaJCUDlLqilnAaSrjBdwQN2gpU_TuYc5ejBFM-GgeZcLwmYRd4Ssxl8TD4dMwkN-3O-4FSritBhn9NdtILFixvoaIgkX3nv84J-LPYsJFNI3_wqvmCb2D-fAAodd8ziUXbPMa2aUjv9LDaJ2UKE9KSFqVmqz32JHSqYTF_cIiUuRD3Q9-K0x2V6oJrcvV9Jepjkzo7IMuY1WaMRak5gQSjNsFAJgvJHyCJ4m8l-hIqZpg4TSkZGJscbH1QnSw1o3NBCkvBFHRAW6uF2h0Ks7anw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حروم زاده فالوورتو گرفتی حالا صیکتو بزن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/98030" target="_blank">📅 03:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98029">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کس مادر جادوگرررررررر غنایییبیبییییی
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/98029" target="_blank">📅 03:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98028">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">لیساندرووووووووو ویزینا میزینا نگاییییییددددددددددد</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/98028" target="_blank">📅 03:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98027">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">لیساندرو مارتینزززززز
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/98027" target="_blank">📅 03:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98026">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الللللهههههه اکبرررررر</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98026" target="_blank">📅 03:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98025">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گگگگلگلگلگگلگلگلگلگلگلگلگلگلگلگللگل</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98025" target="_blank">📅 03:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98024">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSbx9PHaWijiQs_4jzox5lc9C4NqoLjFnnsXSIOERl7psdWklk4h0n06RZa26I1sFuTHOHcEaxfT3VKSuihQZ9lMXg8vrIh4tTDhyz0NpnQzb2Wq3gQrPEFfFlPslJbZWoRYhJS2InWfOljFu5b7aweWsRSBoaFMfK5lWsG_2wXEZOmfwF5lKT0rK9cxn-7TZTSy54h30YmZsQdZHUVJGdGIsBrG1olNt34JCqwVA5ZQqUAXr-e6gkYOzcwsXVqVsCLGFPO8TqMu2wfpTIdaAyQ7ayuZP3fP2gj8pLYbiy2lSZ9ihO4iZQQkS8Abf2Q0KvTui0__lnOcawQABt8hrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همینجوری داره فالووراش میره بالا
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98024" target="_blank">📅 03:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98023">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گلگلگگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98023" target="_blank">📅 03:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98022">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گللللللللللللل</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/98022" target="_blank">📅 03:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98021">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آغاز نیمه‌اول وقت اضافه</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/98021" target="_blank">📅 03:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98020">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mq45OuwGj0j_niyvxKxwcEVejaKbqrtTuef7RBOyp-BLkmbSW_EkuxqZblYKx0UbVFaJaDjrk2LmuG_J5Ol0Ug3UX1PWIHXPejbrgSYHU13iZKhAMMzVjpc5mhizM5QylKjiVarCP_uPtSCXS8akVvxQc1smtoPN-hAZmnP4SQoio0MicKtovkh4zTiFtntw5SBaWVpMdjZNCA827JJxFx3QcpjL0SGkWBYrOcuDIW3Nivh4jfGHtDxYD1FuY2wTfhHxIq3AHVhg-7P5Si52vs9A7YO_BJl8jS0NapYuTi4QKHddeZKAqhBOFszLe8_NbUUSsDoPcvnEr3348Dvwig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
نمره گلر کیپ‌ورد در بازی
😐</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/98020" target="_blank">📅 03:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98019">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اسکالونی رو نیمکت ریده به خودش</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/98019" target="_blank">📅 03:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98018">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
😐
پایان بازی در وقت قانونی</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/98018" target="_blank">📅 03:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98017">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یک دقیقه مونده</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/98017" target="_blank">📅 03:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98016">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گلر کیپ ورد چی گرفتتتتتتت
😐
😐
😐</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/98016" target="_blank">📅 03:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98015">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/98015" target="_blank">📅 03:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98014">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vh7sFPTczOoshM8Ab2v4XuE9raa1gW6owugMJE5J9D1V-33d8Q-gsaZLH4R8zMCCigR0DKRHVw1S9M7wd_uaKabdu7eJ43GxcEtCQsM9TgVvWjPRIJ2FLG6TEypNEyMYxkdiJk1IE4qvzO6ZpaFHNglSkCHUZTNO6pcUzhYDjhieIxIToDHZvqkAFqLZRqWR71bcnN-TiUMGMGe8JGvFLGwJtpo6UdqAyiq1ReqK-ZckR_bC44OI-shS-P4eWRkF3Wbz3sxM4ijPVR-5u-nuOXya2TUV1-88n0DMZJZzQrlZXXUiOw_rmn1DGHbjMmgz4FeBUlj3l9j59HXPcyVMMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکالونی پشماش از وضعیت آرژانتین ریخته
😐</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/98014" target="_blank">📅 03:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98013">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حاجی گلر کیپ‌ورد بد امشب سوپره‌ خدا بخیر کنه
😐</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/98013" target="_blank">📅 03:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98012">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
جادوگر غنایی لایو گذاشته میگه کار مسی امشب تمومه و حذف میشن
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/98012" target="_blank">📅 03:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98011">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
جادوگر غنایی لایو گذاشته میگه کار مسی امشب تمومه و حذف میشن
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/98011" target="_blank">📅 03:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98010">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
جادوگر غنایی لایو گذاشته میگه کار مسی امشب تمومه و حذف میشن
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/Futball180TV/98010" target="_blank">📅 03:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98009">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oh6KWjsd9dN8qZjiCFg8mRNPiqBfvY5OYP1CAxsmrWnBmt6hT1h7pISWKbr4cKrhVQaeFc_BfwSYlw-Afe18WY9Bk6X1lgxvb_9SXOAULvJHy0zuBBrXOV5UBpJBCx9IH7I5twZGqC2YeXlDTJtCX-CrQHD34SFTaXdlM8Q7E8UFnC2KRE-FynD4R53xPfcAqCK6gEj1Ix3UMMp5V-ynePFp5cd0p_dj5Tohv3ZU9Kkb8kWihDpFBRy-c8O0Qnt74oU1VCunBGmpCM6cA_35hF42hMLYLZqdeJP9BPXcCDH5Rp4EtSbmlk9h48nORY2vOF-0QSRjd_T9dqcqdc03fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گللل کیپ‌ورد به آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/98009" target="_blank">📅 03:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98008">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab8afcddb9.mp4?token=PG0jfoNNXUEKRN2mCfae0PqBzS1Q6qIcEPPNMjEMdcM4T47BRgXaOJxyo7JHPpybir-NUcG4Gxr3lBDZQhyhWOtWgjJLEGoyQ99SWTtiBQKvtLlY0vmfaZ1VYjrI7Obf9rfuo_YpMhHZF_tgRWy6nNxGZyMjeDTUkizhNPAitjY6lMFhneGJuz-Kpzeavlhuh6dsC1aR53-gbFuGMKNKEaSmaGph1HSVGIld-olLMsFzAXAil-AOEAZERlX8AK_8nLhVS5EFKXaDXmJmiSopMcSIJay34MmX0MrplIEkb5Oe9C4iNY43okBmDngPTU2_cI8sjGNFCSMWUCQtGQumfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab8afcddb9.mp4?token=PG0jfoNNXUEKRN2mCfae0PqBzS1Q6qIcEPPNMjEMdcM4T47BRgXaOJxyo7JHPpybir-NUcG4Gxr3lBDZQhyhWOtWgjJLEGoyQ99SWTtiBQKvtLlY0vmfaZ1VYjrI7Obf9rfuo_YpMhHZF_tgRWy6nNxGZyMjeDTUkizhNPAitjY6lMFhneGJuz-Kpzeavlhuh6dsC1aR53-gbFuGMKNKEaSmaGph1HSVGIld-olLMsFzAXAil-AOEAZERlX8AK_8nLhVS5EFKXaDXmJmiSopMcSIJay34MmX0MrplIEkb5Oe9C4iNY43okBmDngPTU2_cI8sjGNFCSMWUCQtGQumfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گللل کیپ‌ورد به آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/98008" target="_blank">📅 02:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98007">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmS0qThwCYyAdP0gcg8c2CMHf4P4-zC8cvVrbGEJIbFYGntIG6ntFuVo8nDH6-TxfJUNkQciHwKP552cj5b1AEfE7ug2-QFhpDlDr8Vjix-oQLWA2QiGz5Zi2CZRDkc7w2_IPa5wf9DeKsyO_-jfj9OdWacB1T3n6-JToFDo2Xy842qV-TcFlP3vwfxcE8jyFm9mNXptj3MoxbMH4Tl9q8zkSvzy4SpptMRncDvK3PHY6oQCl_KhFzgDCmIAs4OpgKFkkr2kzSVrboC13Yq6qaMvecTvfmtUIZCBTkDgUsc_EnzZQVtBVcTK1WY0aC06JLk1QhZ_7PEWTc7sgPsd8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت مسی بعد گل کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/Futball180TV/98007" target="_blank">📅 02:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98006">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">جادوگر غنا کامبک زد.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/98006" target="_blank">📅 02:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98005">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شل کردن چرا یهو
😐</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/98005" target="_blank">📅 02:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98004">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کیپ ورد گلللللللللل</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/98004" target="_blank">📅 02:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98003">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شروع نیمه دوم بازی
🔥</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/98003" target="_blank">📅 02:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98002">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CK0Eb3Xffj_Y7LZgm0Rg5WgZkLmlgBMJZ4zJkCli5eLdtM4Lkw8CwQR6hudnulugGbdYcH5XMfbhZ5X3NhZyj5O4ZOEEI03d_DW-wJsUyNztY3CYAXexMvdPytrgYpMheaqOOJIvgTQ-81eEAgxsJifHLgmSVSpEoQghuw76K-jIJmmo7dwe3-X0ILHYUDmbeB4v5V5wQcY97F6o8aDjFIbj7GCCc9heUsLbAJ6zdY0wfPe3aJdaNPJ7bN7aVxybNNTn7jekFN_nqku8OVY-8kjJ6AEaGUyEH541mVxHR6ANmV3h3VSHxt5VHFHbJxfjjxTh3p0g7YevUbgeJ_IUGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🏆
| لیونل مسی، اولین بازیکنی در تاریخ شد که در تمام مراحل جام جهانی گلزنی کرده است:
‏مرحله گروهی
‏مرحله یک‌شانزدهم نهایی
‏مرحله یک‌هشتم نهایی
‏مرحله یک‌چهارم نهایی
‏مرحله نیمه‌نهایی
‏مرحله فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/98002" target="_blank">📅 02:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98001">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZDC23mFJPQAxLDIhcUlJSRWtQJ0UVgUVEpp_wl8OVPnDR_b_qM8SufejNf2ILfeDwERL6r_hAf6p_eHkv95qOq2_wdAbXNJNM2QQloHjKgTsNb_cgJTcT915JgPQMiBE3a8M8mY0lCQ_BPgkiQapHQvxjNQlw_3ODsy1G7q5cDL_ixQMCUxhrPc38M2pQSuRRBorgVJ31X-jYv32oTTDLAnqPC-etFLiuRb_E22wZivneOf3vzn6PZJBUrr153oMW2GbDwr-KEtNGYGLnHKF8qcDmvhdB2dFlIZzcO0Kz7sefs33veFMh4mghFdVaZ0uc0uh1669RK89heG6vnHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا جناب مسی آرایشگر حلال خوری داره
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/98001" target="_blank">📅 02:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98000">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSI3J2Vrn76J2xFGht_CmU1cye7Og8tzJIQc0YgiAh-z7Ck4sNVH8bFjegAVN7KnHSEt-GPtgbMpzCh88r316byq7EohfcOq0Qtc2byx3snye0CMW5rTXo4L69_cM3plOqWPOZ3pEh2VHObSVKgI1D7rG09ntuNtPIzG7Mx11BWuuFh7r5_yN95Hz8PlKppELS1Gg4VdIL3giNxGNrOf7Kh4haeuY_k5JKrYe7c_y6-uDCUtvcYJOFjdM2B-7eUDmaiTFdoQmU1ndq6wtAjmLYLmVwqyn8GoFZbg5pO1V0kRc8se-kv3Wb2oWdDp2Tw4NUn4v_OCdn7IeWgSq9q5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🏆
| بیشترین مشارکت در گلزنی در تاریخ جام‌جهانی:
‏
🔴
لیونل مسی: 28 گل و پاس گل
🔴
کیلیان امباپه: 22 مشارکت در گلزنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/98000" target="_blank">📅 02:26 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
