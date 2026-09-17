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
<img src="https://cdn5.telesco.pe/file/lqfnATbmRtCiMl6RavzFZ4ffRXFUOPzN98sckN0Wh96DUrpH70Xfcieq6G0qYroBBf8IHti4GUDH0Xjj4rx27zRjkBaEwbrid7FM34JRYFrgrzllY_L8iHuu20UPux02ijM4wOw28U8rGojtZ4QidRUFHxN2HXIPSOmvi19Smi1koMM5jhIjDalsKJ212qshhP975QyuwZBFNZQ7tx4KAdlsu5x2sPLIIXaSUEfpSMWLeYw4JWFdI5C5N011vWPphvNPbEpFZFUYUZI2fkfhmQ1mpTgqE-r1KD2xrXOuQ48jVSrKVDLWaC_UN1EZAHNXg8RTSdCnO6pY8NTu5n8GUw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 410K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 18:02:50</div>
<hr>

<div class="tg-post" id="msg-106768">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_nwAJWRzqLJSrO-5_5hr0ug_9Fli4HOQZwyJBxjKSpnF42pxtWBYdpNYdjrEmoxAbLTMlJ1qKgogweIUWYD9xi7EtgAKreCEUp5YqbcN4JBvD5YIHoqRTmjDRsZM0OT_6NE2FsabG-CBwOR3N7owA3g3WrmphK4q5q0Dz1VQfeTdIEkBfn6T2qps5wLlM8JGNTZtgH-_W1DB7glRDGSXichXDfLhwNutCQ7OSd-Gn4W71-Wrvl4K3Lym5w5J0DPG9rEfKnDst8CEFfJqtTys56GxU1BnGcumlSnUqJhSk6fHM-VBfNXkxsWN1JqMGaq1tkgvH_UPBNx80ISkzDTFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
برنامه سوپرجام اسپانیا 2027 اعلام شد
نیمه‌نهایی اول
🇪🇸
بارسلونا_ اتلتیکومادرید
🇪🇸
⚽️
13 بهمن 1405
⏰
ساعت 23:30 به وقت ایران
نیمه‌نهایی دوم
🇪🇸
رئال سوسیداد _ رئال مادرید
🇪🇸
⚽️
14 بهمن 1405
⏰
ساعت 23:30 به وقت ایران
🇪🇸
فینال سوپرجام اسپانیا
⚽️
17 بهمن 1405
⏰
ساعت 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/Futball180TV/106768" target="_blank">📅 17:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106767">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d8b49aaa0.mp4?token=XXum9JZhozBzqZzccbQ7PUs5eHvVJEMVeTZyCvsfxF138nOdgoYEIWlmIOxR4hwtxHekghZqeWHK7fweJb9B3Eh2D_2iMjXRajM00Qfp1fF6RvxgxSCEVm86-YIYOHN6Jyd6Ri5RGy2x5ypGWX8nXUrn4vy90wFi4i94W3XAWN5xt2hAirhv3HzR_nyzi1JwclHbCxQtvbW7x_Ie_uBzl_x3kD_i4kfv8nio8TWYOCTi8ZkrN-hLdOYdbhZBRegnylwzg2_KmFlfGZDE9NdPECVfz1jg9S5LZdkB_AIOx4-F6k3XuNyvMBasfg0tHmgA5YW1NEuKlOkwtmPrTWQKjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d8b49aaa0.mp4?token=XXum9JZhozBzqZzccbQ7PUs5eHvVJEMVeTZyCvsfxF138nOdgoYEIWlmIOxR4hwtxHekghZqeWHK7fweJb9B3Eh2D_2iMjXRajM00Qfp1fF6RvxgxSCEVm86-YIYOHN6Jyd6Ri5RGy2x5ypGWX8nXUrn4vy90wFi4i94W3XAWN5xt2hAirhv3HzR_nyzi1JwclHbCxQtvbW7x_Ie_uBzl_x3kD_i4kfv8nio8TWYOCTi8ZkrN-hLdOYdbhZBRegnylwzg2_KmFlfGZDE9NdPECVfz1jg9S5LZdkB_AIOx4-F6k3XuNyvMBasfg0tHmgA5YW1NEuKlOkwtmPrTWQKjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
انتقاد جالب میثاقی به زمان‌بندی ارائه‌شده از سوی سازمان‌لیگ‌برای هفته‌های آتی لیگ‌برتر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/Futball180TV/106767" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106766">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106766" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/Futball180TV/106766" target="_blank">📅 17:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106765">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zihdd_Q1ZNA3cYxXPm8W3rqI2hFZE5PbZC6rOn7vfF5o375WWMjGIVoXhqoiJiFR4NyJa--XDS1bHmv-n8kpJ4d7YdVeOZXXXxoO-Tz9Ks0sjKNZ4z307U4ls0u6Uv3LXYbC1buoFUbswRiGsd7mwp5nhLi1Jd5ewg-RjcIfecszFTs8R2Nx1sGqtupXr3i-evue20pW1rtjCcqyqxKEJTUXgiM5q5uhBzQtZIYRD5u-ZLZg5_jGdAbNY6zb8uNsXhdSwHmyn4hKkyD-KGM2YIU2AVB38cswEHg9tV6VKE0QaSBJxtiVhHesFGOJJrFEkFMW2Tjmx9wKMvLNCE61iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
وقتشه هیجان رو به اوج برسونی!
🦖
با
TrexBet
مجموعه‌ای متنوع از بازی‌های کازینو‌ی زنده، و اسلات‌های جذاب رو میتونی تجربه کنی
🦖
تجربه‌ای سریع و روان
🦖
دسترسی سریع و راحت
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/Futball180TV/106765" target="_blank">📅 17:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106764">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acdc40365b.mp4?token=jnqM4q_XkTS0jLjlzAlIYMc4vrX2eK7zzoxEo3C7eJpMlJPFLVWyC2xk4B5KziaUIYnuOG8znIbXorCZ1DkXgy2lCOhhvuTw9sxcF-v8l8CD55bwtTisptpIx7MAhwNSXy-csn5PyoabXYLTp1dRjsKp44VwEN_fXAnwIrrxnByKHZbdSmhFqfLgWBw8lr-Hd6zWF6vGKBxcQrP5JpfqcWiv43QZ6dz8BhUnK9nMP8f9pxHYbFfM_S8LvDtycRFc11HiRgbQhL91copzcu0I8XZs2Xpbk3eLwGBL1wLTKl8K0GypOdCVP9DIFSXaeDQ7d0rMc2_NbVnhqYce7mC44A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acdc40365b.mp4?token=jnqM4q_XkTS0jLjlzAlIYMc4vrX2eK7zzoxEo3C7eJpMlJPFLVWyC2xk4B5KziaUIYnuOG8znIbXorCZ1DkXgy2lCOhhvuTw9sxcF-v8l8CD55bwtTisptpIx7MAhwNSXy-csn5PyoabXYLTp1dRjsKp44VwEN_fXAnwIrrxnByKHZbdSmhFqfLgWBw8lr-Hd6zWF6vGKBxcQrP5JpfqcWiv43QZ6dz8BhUnK9nMP8f9pxHYbFfM_S8LvDtycRFc11HiRgbQhL91copzcu0I8XZs2Xpbk3eLwGBL1wLTKl8K0GypOdCVP9DIFSXaeDQ7d0rMc2_NbVnhqYce7mC44A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
واقعا چیشد که به اینجا رسیدیم که یه بازیکن فوتبال برای خودش آرزوی مرگ میکنه!
صحبت‌های تلخ بابک‌مرادی بازیکن سابق استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/Futball180TV/106764" target="_blank">📅 17:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106763">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmbddO631lmbAHaIdSDRX4I4_IbYF0QfUH8dImh3YzxOR2J_wnkhOsRFsXy77XHzP1ldk2u7WlWv6W-iO--35RkXXjbU8NLqZwlIyIpdV44GE_nlVwYjkIUe_0k5FEfcxWmj71vS9NuIHFOR0qyGSbT-dIbfAS_wiNZO9K5zuVGXGJFoD-56SdiHVWQ9SkNeAuBGjUPGUceThI47QuZRMSTNKTwWJLYoGdaj7bOMYwvxixZn7gWawTh75jDglIHEqUD9emZ9L54xqTrCdQxFx-Bq9HiCrLX9lLolRe0VvGQ4wTQ2ba3Ux3WalddGnkaaGUT8g23BzL6U4J9uWiV3GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📊
🥶
کیلیان‌امباپه از زمان حضور در لالیگا به تمامی تیم‌های حاضر در این لیگ گلزنی کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/Futball180TV/106763" target="_blank">📅 16:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106762">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db11bb42ef.mp4?token=sPVX7IXylE5n6nzH-zlwdsXei1skHwUswMSSG75lwzCSYN7Mz9HBfjT9_lWk73gwOZN_5dHAsWG8hu1sSJvCRRARnVYuuyFRMiaIC74JlODYEga2giATRywogW6rLsSmavaJLeRcOCawX9-85Jx7M7347JRJGxLVt2-BwJLw5xPc4KdZmVEHNHE_n9XFggF1iSDw-19__UyMUU4epmK5yNcuLtm8Xe_NkTUer8Tc6PUjSIMwETc-Uvnr-I49qEu4sigej64gaAmdtiWqK0G5gKT0aK6nxhuIVvRcX2_cUZ8qQy8pYSyGawYi1zneGL1blUITwW9FKot_HletbgrVmSYDSxUmr-U5ZRMRm3QJTcco2kEuVMDHjb1iCQHSnupKf6Or0PpjU-ydctL41VM9JFIdryDvLkOQwvv0NM5TMeJPILnQLYJ37HwYLteZyoTGfubDcRZsYAveOoMJvzf15BBqWFKYt2mw82YmVbrojPcjd9LU5kHNtb13Q28jcGjYASjPeo6sm8dWbFhNkYmwFj1iFq0meU1zBlis_psYrf70oyE5N2LumVQlCubY3sHUtfbOXSqgXXf1aU7MQE2nlIlcX9lEF4irBXh2hfoGFvRM7WHfH0XF9hiTFXC-j_qZeqUwD6oc3-g0GR3lYtW4i2qa9i3yaFFECkS8CFZlTwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db11bb42ef.mp4?token=sPVX7IXylE5n6nzH-zlwdsXei1skHwUswMSSG75lwzCSYN7Mz9HBfjT9_lWk73gwOZN_5dHAsWG8hu1sSJvCRRARnVYuuyFRMiaIC74JlODYEga2giATRywogW6rLsSmavaJLeRcOCawX9-85Jx7M7347JRJGxLVt2-BwJLw5xPc4KdZmVEHNHE_n9XFggF1iSDw-19__UyMUU4epmK5yNcuLtm8Xe_NkTUer8Tc6PUjSIMwETc-Uvnr-I49qEu4sigej64gaAmdtiWqK0G5gKT0aK6nxhuIVvRcX2_cUZ8qQy8pYSyGawYi1zneGL1blUITwW9FKot_HletbgrVmSYDSxUmr-U5ZRMRm3QJTcco2kEuVMDHjb1iCQHSnupKf6Or0PpjU-ydctL41VM9JFIdryDvLkOQwvv0NM5TMeJPILnQLYJ37HwYLteZyoTGfubDcRZsYAveOoMJvzf15BBqWFKYt2mw82YmVbrojPcjd9LU5kHNtb13Q28jcGjYASjPeo6sm8dWbFhNkYmwFj1iFq0meU1zBlis_psYrf70oyE5N2LumVQlCubY3sHUtfbOXSqgXXf1aU7MQE2nlIlcX9lEF4irBXh2hfoGFvRM7WHfH0XF9hiTFXC-j_qZeqUwD6oc3-g0GR3lYtW4i2qa9i3yaFFECkS8CFZlTwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🎙
رست‌دیفنس در فوتبال از زبان رسول‌ مجیدی از معدود مجریان باسواد صداوسیما؛ خیلی جالب و شنیدنی برای عاشقان فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/Futball180TV/106762" target="_blank">📅 16:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106761">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
با اعلام کمیته انضباطی فدراسیون فوتبال، شکایت پرسپولیس از استقلال بابت یاسر‌آسانی رد شد. سرخپوشان پرونده را در CAS پیگیری خواهند کرد و به تیم‌های عربی نیز کمک حقوقی خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/Futball180TV/106761" target="_blank">📅 16:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106760">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/915324d20d.mp4?token=OvF6vqKtTefManZpQ5VNECUSSP1diPMlc8SHwLnbnJ4n4Nd-QS9XVXX7PQbdfEfW4cWesm1YLZUfya2rnFiFL5UvUAR2_ZAUimpmyyOP6tp3NvP47-DFJ7Pjnfx4FqnQD59bGnfomehvMnfBKM_SmVKgUAkINAPeTNkOQNWm-TnVgshkQy5d2TKZLA0XeT9DmqhMQgi7Rg4oWVC3NDATa2eO7wXnA0xeOhS-m_94LuoDhPRqPzfzBC8_QR678oX2C9b1lsv_UVcHVTH0PruGSqMkTneQchdMwWyZt5eLuXeMmiBsaNWVObCOnHcQPyBoiPXUF6_fDnF6Ow4I1uUCB3qEb-fO11mSEF7CP8qA8zdt_KgsPyCpsLgdfsD32yFzqO2sJ5tiIr4HzuAZcCEf62FuzPn1mwDqu6S-yzTwWXKpRGg-iWoYvH01tYmvW2-Ug3xG38Hn-2Kp5OSABoD9I5P20bNZEE-GJLf8MEqMQJgcrvnwbhWe_bAOKG2cU0eYDXW7aLXB2-Byx1bJMJ0-PG7ZvBHaZ7mzVgGza3TOzMV_TqHJyRyWA11mZqExq6gfjzByPhIewPkxGOoJByCdq5UlIz6VTZQbJy1z7_KCOoAAP0Vam-KZnfDHVv3ZeynJtKW24SDUpj3lold9Jvn5v-Xs1aLqtSJqhV05KjtFtfs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/915324d20d.mp4?token=OvF6vqKtTefManZpQ5VNECUSSP1diPMlc8SHwLnbnJ4n4Nd-QS9XVXX7PQbdfEfW4cWesm1YLZUfya2rnFiFL5UvUAR2_ZAUimpmyyOP6tp3NvP47-DFJ7Pjnfx4FqnQD59bGnfomehvMnfBKM_SmVKgUAkINAPeTNkOQNWm-TnVgshkQy5d2TKZLA0XeT9DmqhMQgi7Rg4oWVC3NDATa2eO7wXnA0xeOhS-m_94LuoDhPRqPzfzBC8_QR678oX2C9b1lsv_UVcHVTH0PruGSqMkTneQchdMwWyZt5eLuXeMmiBsaNWVObCOnHcQPyBoiPXUF6_fDnF6Ow4I1uUCB3qEb-fO11mSEF7CP8qA8zdt_KgsPyCpsLgdfsD32yFzqO2sJ5tiIr4HzuAZcCEf62FuzPn1mwDqu6S-yzTwWXKpRGg-iWoYvH01tYmvW2-Ug3xG38Hn-2Kp5OSABoD9I5P20bNZEE-GJLf8MEqMQJgcrvnwbhWe_bAOKG2cU0eYDXW7aLXB2-Byx1bJMJ0-PG7ZvBHaZ7mzVgGza3TOzMV_TqHJyRyWA11mZqExq6gfjzByPhIewPkxGOoJByCdq5UlIz6VTZQbJy1z7_KCOoAAP0Vam-KZnfDHVv3ZeynJtKW24SDUpj3lold9Jvn5v-Xs1aLqtSJqhV05KjtFtfs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برخی از راکت‌های تماشایی سوبوسلای در لیورپول؛ واقعا عجب گل‌هایی زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/Futball180TV/106760" target="_blank">📅 16:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106759">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jscVdzDbDJbsYOjRWTyp7bDioksbcvGnQgzNjsUNpTcukrU5kl3F7ulT9AIqIQmQ4QqdLDQeftm8M0lTrU29VbWygWpp2v1BxPDLmfRM6pJ8Mac-Ub47sxc5tUVU7tzEsBrzcRCfSrgbyxSa3eJHaLoWBysq4vWJ0RpZF1nFGc2xiuPWmdQ_NFugniu-rlxQVxz15L5WR4dCY24plRQgSMv0DEjVHQUugPi5UNFzxgju0d1cbxIFYUF2bvpkhWrEYqFIp2lkZODQD6AaJ0CAgq-EZUq6qyAgXAted6jnro4x6Xf9kuN4qMUq0M8jBzxV8YIe1fuPg1nTH3zYUkprEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
سال 2018 که فرانسه قهرمان جام جهانی شد، کل مردم فرانسه برای امباپه دعای خیر کردن و نتیجه دعاهاشون شد این بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/Futball180TV/106759" target="_blank">📅 15:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106758">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ab14c70f7.mp4?token=U6maa61XQmWS1OVC-l7fhwXAGr20ExTl-IW4UAgF51l_ISj-XKHPyb497mQyBtUib3FMtbXKBvO_COFivDoGA7AEY5AC4nfLZ3T_32R-zqf0W5oITqj8kwFwwwdeZ12aoKWs8iVbYIGh9-qwaNUqAvehX0W1FUnYjIRGgGXCvQetgxVhKDcc2XEVzj8PaxeQ3Sei_dDYHh397B5XYh-Z9PuTpXNbHe-Aajq4gfvws3Sibu-bEB0GixCVuTvDTFriMJQZzOGQXMRWbR9q5B_HYgCHfvzBaYev0ZlNfiG-Zm6N_zkQWh5UepSjxgTvVV3Sp4NAtPni1IE4sbzFCoUNyEN5UJCL0FgrIpgio_r7gKhvQ7al4xm_xCXHQ0wN9QxaYZxkf-TB0YsCDeZwkYO5mKiNkc53wmKKU12swwfLquL0aJCVAmpOo4zx5JQH_qzoLwOZ4--CB3BUTMbDaPHKTWwNWtXITgQMGWIzbmBtDd4jWhjXjZesrG16yQEcy6L0zgy6GtRMgcHsb1Za_-K5J0f6QpDyMfvQJsnmSO2uHYyQmkdbtmBHhPVk32Lx_31Q2R3oB7LCTVsMkaoIOK4-8wguF4a4YQlcNkutWn31jLAzJqiP9ykqQdBkSnoMKv1Sn2_GoFStlA_J6wz6p5x0hurmmX0R9ivzfh_aF20dkiU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ab14c70f7.mp4?token=U6maa61XQmWS1OVC-l7fhwXAGr20ExTl-IW4UAgF51l_ISj-XKHPyb497mQyBtUib3FMtbXKBvO_COFivDoGA7AEY5AC4nfLZ3T_32R-zqf0W5oITqj8kwFwwwdeZ12aoKWs8iVbYIGh9-qwaNUqAvehX0W1FUnYjIRGgGXCvQetgxVhKDcc2XEVzj8PaxeQ3Sei_dDYHh397B5XYh-Z9PuTpXNbHe-Aajq4gfvws3Sibu-bEB0GixCVuTvDTFriMJQZzOGQXMRWbR9q5B_HYgCHfvzBaYev0ZlNfiG-Zm6N_zkQWh5UepSjxgTvVV3Sp4NAtPni1IE4sbzFCoUNyEN5UJCL0FgrIpgio_r7gKhvQ7al4xm_xCXHQ0wN9QxaYZxkf-TB0YsCDeZwkYO5mKiNkc53wmKKU12swwfLquL0aJCVAmpOo4zx5JQH_qzoLwOZ4--CB3BUTMbDaPHKTWwNWtXITgQMGWIzbmBtDd4jWhjXjZesrG16yQEcy6L0zgy6GtRMgcHsb1Za_-K5J0f6QpDyMfvQJsnmSO2uHYyQmkdbtmBHhPVk32Lx_31Q2R3oB7LCTVsMkaoIOK4-8wguF4a4YQlcNkutWn31jLAzJqiP9ykqQdBkSnoMKv1Sn2_GoFStlA_J6wz6p5x0hurmmX0R9ivzfh_aF20dkiU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🚀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپر گل پریشب سوبوسلای به تاتنهام رو از این زاویه باشگاه لیورپول ببینید
🤌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/106758" target="_blank">📅 15:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106757">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swzwFfJ6LsX6hht1srRvI1fPSAuwZf6ehIN07vzF6TLTNtXhFeus6ypQLsJJCP2Nsj221cu4i6PLQ3NgzdfB9jzejSa5Mt2Hd7CM87Y9T2iZYy1Xs66IPW_Jti90r_oelfJdgaB7N5FISnqnx-TYHUzT8qQZp_7FD6x0Wstoc7nZoXM7sroCwXVF61TW1EcN21pOnUqpzjRVwgKveaqisiDEhhFbKQfnteYdSIlGkqD6R0kZr_KO7RijXFJFqzll7AG7ygQuPjPE9LJqYnPXsbx7o7IiymTTe9y_ZSuJy_wVpn0zBmPs1WxTPv5KBDPmTNUPTD45syR0NoJIBRnnKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🎙
کیلیان امباپه: "جایزه توپ طلایی؟
به نظر من، امسال زمان مناسبی برای من است تا این جایزه را ببرم.
بهترین کسی که از من دفاع می‌کند، پای من است.
هر چه که بگویم، مهم‌ترین چیز برای من این است که توپ طلایی دوباره به رئال مادرید برگردد. باید به سانتیاگو برنابئو، به هواداران مادرید، بازگردد تا شادی را به قلب همه آنها بازگرداند.
آنها بیشتر از هر کس دیگری، شایسته این هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/106757" target="_blank">📅 14:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106756">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/758a2aee2e.mp4?token=EfPa4ec9LGQEiL-l6m-b17HnASYyVzRPn3nOpW5m35FlyipA0ds0mYWz-SGXyxvsbBtjB_GVpEie9Gvki1Q7x-ZqBRIb2M8Mhqr5Shj6y1-iRzwoHGN5YTURrdPjT4w6NW_Yi5G92rmafp2s3kYLeG968Rv8_9uXpROmdnMBPiHCsIsHsFmNOqnFyrQlQstXteoBiVyABVDCYSRMIrIcBR5UBejzBwquUbNT9sbRGbT_3uoXKs03JW6frp3l4Ef9du_x5Th-MiBzeJCvNIFylnruX0cYdGQaLebyJfHe5Qr8-cr-TXmxFTDXDZtJKhRKmX8k3bR8XDfFZsuXIGTGlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/758a2aee2e.mp4?token=EfPa4ec9LGQEiL-l6m-b17HnASYyVzRPn3nOpW5m35FlyipA0ds0mYWz-SGXyxvsbBtjB_GVpEie9Gvki1Q7x-ZqBRIb2M8Mhqr5Shj6y1-iRzwoHGN5YTURrdPjT4w6NW_Yi5G92rmafp2s3kYLeG968Rv8_9uXpROmdnMBPiHCsIsHsFmNOqnFyrQlQstXteoBiVyABVDCYSRMIrIcBR5UBejzBwquUbNT9sbRGbT_3uoXKs03JW6frp3l4Ef9du_x5Th-MiBzeJCvNIFylnruX0cYdGQaLebyJfHe5Qr8-cr-TXmxFTDXDZtJKhRKmX8k3bR8XDfFZsuXIGTGlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🇮🇷
🇮🇷
مقایسه فالوورهای ده ستاره سرخابی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/106756" target="_blank">📅 14:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106755">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDmgnS5bQEalceOawyy996MyZPYSl5dJ1FJ77vBloZvu5ZnQY4cfJC22q46mQDtUpZ-pI9DOe03tWDVq3G5gnfgFG_iCo-Z0wSZILdI5GwCbT1qB-jyUcPqEcakOpessoBIUg3XkwYsnjPBkZ1T9joQxADmgmgi3DqjRAx0FXZsR9ii_SHQRvXpfzYrU3v-6nEPUMhVtPPlvMm_vpek5WfvqwtmHiVoKuEyJj5Nz12CGEMmVF-4s8LU8BWQUPc6Ahjz_rOTjYP0m-8TfeURRnEsnWagcEB4Xr654Pt3weV4HmVXUUbyAHc8ycljTJKnTHXLfyHAA8sEMjogC8NSlDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇷
شبنم‌علیخانی کاپیتان تیم‌ملی والیبال بانوان ایران به تیم استقلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/106755" target="_blank">📅 13:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106754">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=i5tI6-X1SB9ev7Q1x_3LW9imtiPCvkmgzswYQxNcq5iB-OuHpdDlcUW521WFGinF-4pSzBj_fBKOjFPKa1zEPCbvo0UAKAyOxOYcOOh4sAkdOhf2UJe_HaX5RF--lcZ7JnVC-pLwonphS0FM5eqUVU7So6vXNZS8Ikko_qGSYGdda1lc3atJZjRCwF-rPj5XcE1IWPKES1O58zmg68hwtPktBh-NKGt9HgT7pdUPkrDvkhkjsQKsPiJuV8ZCJPiyMTOAQAmdpalFRqAHbp2Zj5Mqkgqn3kO4J8Dl2J5NYXaPkMs08-BrgEg_n8U9PmbWDLQPDRJGupZ7zgZb4gPwhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=i5tI6-X1SB9ev7Q1x_3LW9imtiPCvkmgzswYQxNcq5iB-OuHpdDlcUW521WFGinF-4pSzBj_fBKOjFPKa1zEPCbvo0UAKAyOxOYcOOh4sAkdOhf2UJe_HaX5RF--lcZ7JnVC-pLwonphS0FM5eqUVU7So6vXNZS8Ikko_qGSYGdda1lc3atJZjRCwF-rPj5XcE1IWPKES1O58zmg68hwtPktBh-NKGt9HgT7pdUPkrDvkhkjsQKsPiJuV8ZCJPiyMTOAQAmdpalFRqAHbp2Zj5Mqkgqn3kO4J8Dl2J5NYXaPkMs08-BrgEg_n8U9PmbWDLQPDRJGupZ7zgZb4gPwhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
حرکات عجیب مجری شبکه‌سه برای توضیح عملی دفع سنگ‌کلیه در برنامه زنده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106754" target="_blank">📅 13:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106753">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2975c02c1e.mp4?token=rCl9x0y02vIqa2CXNLEzyOhxHC7KZn3U_TkvuD2q6LoLRZLj9kjKAFVpTu9VVmIJnoiAkBHJWVuXEEm2e8gYdHXjXxZrEZHM4NaotKLC5lXtws8DWW8vq0BngHbclQ2zrsH3uJBVJCePGrxRGn655HTmr16AwRsKTov8TzNY0H1CulIC1XFR3vJPsMjvqc3RId7NbbrscydJZ-GWNgDRWoYR3C4euQZxaQ581ibmncHaCqueXg1YCommwM7JnTuxilQQMEPMlqsAufLdwuQZfusD3nQRd8F6otr-FEGV3VfRJsE2ApkByrLvoRNOhT5t2J9CjplbY7AEEhnc1phRVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2975c02c1e.mp4?token=rCl9x0y02vIqa2CXNLEzyOhxHC7KZn3U_TkvuD2q6LoLRZLj9kjKAFVpTu9VVmIJnoiAkBHJWVuXEEm2e8gYdHXjXxZrEZHM4NaotKLC5lXtws8DWW8vq0BngHbclQ2zrsH3uJBVJCePGrxRGn655HTmr16AwRsKTov8TzNY0H1CulIC1XFR3vJPsMjvqc3RId7NbbrscydJZ-GWNgDRWoYR3C4euQZxaQ581ibmncHaCqueXg1YCommwM7JnTuxilQQMEPMlqsAufLdwuQZfusD3nQRd8F6otr-FEGV3VfRJsE2ApkByrLvoRNOhT5t2J9CjplbY7AEEhnc1phRVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
▶️
✅
بهترین مکمل برای جایگزین کردن قهوه قبل از تمرین چیه؟ به روایت استاد هانی‌رامبد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106753" target="_blank">📅 13:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106752">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3wPLSzp3L64qqsfsiMlXxVtOGIUEVfIjKJvf2b-dXai4bfPAB9JCyb6KKGNoBNJMsT1WaHGMiAkL7MEyw2D4nVrurxzTY0SPSpoLn6GPeH8zgaiMdlC8mCEdJjLyJumY-zI-d6fqIPMqeHKLFJ065iKqbOKJsgGn3dLQpC6vkle9GAz7wnm1G37jp9sW0Q3wDPdP6aDV2rQBIb-x2g6bUvGAla_xDIbY4bOv3ypOd8UlDPdcoMvz0syMLXKyo0IFmKliPlfHoSW5S6iVMDvAK8LkEkNbztBQP2sLnxibvNAv0vvsQl2Hs3k9sKxcPrA6CL4LV3LDsihISShTNXfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
با اعلام کمیته انضباطی فدراسیون فوتبال، شکایت پرسپولیس از استقلال بابت یاسر‌آسانی رد شد. سرخپوشان پرونده را در CAS پیگیری خواهند کرد و به تیم‌های عربی نیز کمک حقوقی خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106752" target="_blank">📅 13:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106751">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDOCYIT1gd-q2RV9TY3S_FF-uZJrDJiOG1CO5M6rK4zrsi8Q_J1rLLXCDTYtacek-UBr-DfHmshJtmN-PgSssXTPPXXWgmpWkEPQpJI6T2rdiqkTb3h6wsTeM-6Z1cOmxXF19Eo3Z_CxYfW6sz6x8fN5miLK4XM0kV6wTo5Egi5bv9DOcMkhszodBaYHJ3qNkv6YobjzxL-5lawiv-lvNYGfqmSV4vZ9WDix8UIHUjjEIjSaRCQyJy3f38Trej-Ol89b2qJHlZAGlEnfETenyoBi-NMFdVcNcuWrueUhycxpscstjY_tzPJbPlQSgRi2Bwyd_ivNoHoHCQhdLkVGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
با اعلام کمیته انضباطی فدراسیون فوتبال، شکایت پرسپولیس از استقلال بابت یاسر‌آسانی رد شد. سرخپوشان پرونده را در CAS پیگیری خواهند کرد و به تیم‌های عربی نیز کمک حقوقی خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106751" target="_blank">📅 12:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106750">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddepDEHH8_baNh0ur-ypsPOMKnKOM_7EidLr51yAeQrPugN1wz4fUbreDaBv8Yjdw1HkrX5Y7jSeCE86pbsDLGT0tp-nxMitDT3j4iZDytj6E7xNiNhiRMPypbNs28KzC49Vdtb2FI24YjSLak7Zsl51qMZoDLTQsJSNr73QvgTA9TJoo2O3OvIw6qYeC9K6GdsNyekOt6MDFaMZrkNRPzJxmJ6RipXR-nbeCJXUH6TDJiJnWZEpuxpV82Lyzv4gnOpsI6zRJxX1SvjMrM36WgajRk6eGMLnPjbn4rhap2_MnyVzqfOQV3Sx7xHrCnoObQ_SqPYcQNXs3NAlB07Lbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🫣
بالاخره روز پسر شد
😁
👍
‏در تقویم هخامنشی روز ۲۶ شهریور روز تولد کمبوجیه پسر كوروش بزرگ می باشد و این روز را در ایران روز پسر نامیدند. برای پسران عزیز زندگیتون بفرستید که حداقل تو این وضعیت کمی خوشحال بشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106750" target="_blank">📅 12:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106749">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEi7vDRY9PiSnCw4WcnCbRdWrbAksjTruKbb1TW-x-RDp35qxbq2hTV1WIfTAAHf53kgDCLK6wXChECvs-FGiP55q4nW5-D2uofcs7Q59QYRzGtPsDhrAGG_u8U55zloLVDqV0AwIvOcJwhVX-qg_xcVgzaeJcFT7YrHY9sYGfaRiOy2Fy5JbFdST_gX2YollzFUX932UTNtQFJd7sRWZOZ5TIfL4CW98JzyzB9OFc86pkSveh9OY7BAg7enZjZ2nlxnRwqQz2NMRWZIsXGAmUNtV2m5zD8cmz5FvCPFwqV69SL_aAs1stYsdoVCZ9f5OK8r3HTMM_8drvnjdv7OTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
💵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بهداد اقبالی میلیاردر ایرانی به طور کامل سهام باشگاه چلسی انگلیس رو خرید و الان تیم کامل برای این آدمه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106749" target="_blank">📅 12:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106748">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🎙
🐐
🟣
دیوید بکام بعد قهرمانی دیشب تیمش:
🔺
هنوز باورم نمی‌شه مسی اینجاست و برای اینتر میامی بازی می‌کنه؛ برای همین هر وقت بتونم می‌رم سر تمرین تا ببینمش. به نظر من، با وجود بازیکنای بزرگی مثل هری کین، کیلیان امباپه، جود بلینگام و سایر نامزدهای توپ طلا، مسی باید این جایزه رو ببره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106748" target="_blank">📅 12:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106747">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb69509038.mp4?token=Lzol4gm1kbJHTnln-PrQUuTKHesxyJYIieoziyUPN-vewQZKECiCW3q1jmhwGhvAXOKvHYwaq8x5rOsoMaFndvyDxy1-pF9BJiFmw-42nnu3szp76JVwdcS_j39MuKuZNR1hBpJ22PXg1L1slbZdDcx2Bue8liKFNJep31Wyq8844DI1TiXUwSfWu2wWBM1yIP4r72P1xIQnqzea6Ou2MmGDPpyTnYgcAupOX2lv274TDKBL4Oo5YYIjTpRHadWuQxrDu2AeibvrJ8LjZWD694aEAJkuGr5_9fvSrT4qVkCkT4RXTFLSyPYywiC7VIRvU4zfDYk3PqcEe36zjpR7lkXXfMsYF8Pq7YgwzyxP0OST6ccycA5udOD2aM4GLNNCQNHINEs-mYbejygLW54Li3te0OPAMuq3-s5FRKXW0wPz8vx70syt0eaQOeFi0hQHv7e3pGWzBjAYt8R9u1ldHJl1Pnsel-dTcu8RCZgr144-U21mA36P5kD9JOlcvG03xoGYJq06aJIyXSRCLPS7RS2ty7x_TJaZjROBwK0TCnxBXrMl7XICwdFLi6nxIm727wf4fduAETGkJZuYbiJMkkDUWK3VwgAtByWmJ9sCwY9k4qjQdX5-gx7onoeyUv8iGIBDu7AfNNVt1sCMHMXs-AsU24Pz7t2Gj7DTvQSUOIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb69509038.mp4?token=Lzol4gm1kbJHTnln-PrQUuTKHesxyJYIieoziyUPN-vewQZKECiCW3q1jmhwGhvAXOKvHYwaq8x5rOsoMaFndvyDxy1-pF9BJiFmw-42nnu3szp76JVwdcS_j39MuKuZNR1hBpJ22PXg1L1slbZdDcx2Bue8liKFNJep31Wyq8844DI1TiXUwSfWu2wWBM1yIP4r72P1xIQnqzea6Ou2MmGDPpyTnYgcAupOX2lv274TDKBL4Oo5YYIjTpRHadWuQxrDu2AeibvrJ8LjZWD694aEAJkuGr5_9fvSrT4qVkCkT4RXTFLSyPYywiC7VIRvU4zfDYk3PqcEe36zjpR7lkXXfMsYF8Pq7YgwzyxP0OST6ccycA5udOD2aM4GLNNCQNHINEs-mYbejygLW54Li3te0OPAMuq3-s5FRKXW0wPz8vx70syt0eaQOeFi0hQHv7e3pGWzBjAYt8R9u1ldHJl1Pnsel-dTcu8RCZgr144-U21mA36P5kD9JOlcvG03xoGYJq06aJIyXSRCLPS7RS2ty7x_TJaZjROBwK0TCnxBXrMl7XICwdFLi6nxIm727wf4fduAETGkJZuYbiJMkkDUWK3VwgAtByWmJ9sCwY9k4qjQdX5-gx7onoeyUv8iGIBDu7AfNNVt1sCMHMXs-AsU24Pz7t2Gj7DTvQSUOIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
وضعیت دیشب نیوکمپ که هروقت بارندگی بشه اینجوری استادیوم به گوه‌خوردن میفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106747" target="_blank">📅 11:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106746">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
✔️
اعلام فهرست بازیکنان لیگ برتری تیم ملی
🔵
علیرضا بیرانوند، سیدحسین حسینی، پیام نیازمند، محمد نادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی‌عیدی، امید نورافکن،…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106746" target="_blank">📅 11:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106745">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mC352ZpuV3S-29NFMASH21OCxf-i33N3rCAFrPDjdd0GQ8vXy1MvoT-0PdRdzXvaN4y68oUOQ6-CPjbQU-xuVtKxsTxA6RDEy04GQwXGlhSgGDyMMtv482GERdQYF10OGLAGgixQC_hdy0AXki-PmFHo73c2iILo19LDH4DaobL_bL4UCV-ZPHtCL0F_QlQw8trv72jgCKMhOCaMGm45AEtWIxsSEau01oR8yQlY8lVtwtCfCzMOVP5MIyqJ3aS7odvID-0Y31QRglJyu2CVKu_P16e6JIOM3nFsi9LpUuXW-QB1mg8zNpJ0g3Uljy_BpuSb_PTQwIdzwTqfVQP9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
اعلام فهرست بازیکنان لیگ برتری تیم ملی
🔵
علیرضا بیرانوند، سیدحسین حسینی، پیام نیازمند، محمد نادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی‌عیدی، امید نورافکن، مهدی لیموچی، مهدی محبی و امیرحسین محمودی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106745" target="_blank">📅 11:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106744">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b540a014a.mp4?token=FeItlOhyP38T5FdNiXWVOg_BxkbzwlrqXaWGGoPOo2xqJCONEa4mq3oapIkEgMaVMy5rHbtx5TAdZJKf3Jocv2YEYhfsDq2KhhoKW9qYv0uJXbxMUQJXdyAPOor-Lfm2ijpuMn6y87OjxBlw1xs8hzd9aLwP7A7aUcprc-JDLgu4Sm4vPS1VilT8A8wI1vp2Pk897BHHCj-fYq-0SZNNCZpfP5mN3e94NvDyZIHfHnfu1lL0uBEpfQP2Rv23u8J7rsZ7f-eb-G3e4W56MYlse7uUY0fluwVsqA_SH6rS1MUzGSA74kesHAw9sOmH19p2r5OITWwQ6jfYbVNGeNkSBIAbcaVZyGTc4kLunGgdN74mMgVUgreuRV3Aho7T5fUENxj9WAmeQ5DF7frD3TX4FR8SV0ZU4g8lfZlkepIrW_BGWvkzRG_10IDWE_jzEsJd85nqMI1uEwcGvvfUAQ3QhkceE8l45g1-_lh-bV2Uug6y5T1hb-rYK0hPzQSwRgGPQh4tikO3wdAEfsSYf4DBSfRxbI9lCF5VTVh6gLx-2B9UQ1vu8fNf6v1k-QgSCT1XH8hiSexBjVEwDcdFZUx8yJCHCfLnpDSk-QsjVbznRurxEsKuLKB8Zgw5fSg4JtZXHwFyHOAv2qD4wJPvvEW8fg8q_OWjsLPWL_9DrS0-kmY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b540a014a.mp4?token=FeItlOhyP38T5FdNiXWVOg_BxkbzwlrqXaWGGoPOo2xqJCONEa4mq3oapIkEgMaVMy5rHbtx5TAdZJKf3Jocv2YEYhfsDq2KhhoKW9qYv0uJXbxMUQJXdyAPOor-Lfm2ijpuMn6y87OjxBlw1xs8hzd9aLwP7A7aUcprc-JDLgu4Sm4vPS1VilT8A8wI1vp2Pk897BHHCj-fYq-0SZNNCZpfP5mN3e94NvDyZIHfHnfu1lL0uBEpfQP2Rv23u8J7rsZ7f-eb-G3e4W56MYlse7uUY0fluwVsqA_SH6rS1MUzGSA74kesHAw9sOmH19p2r5OITWwQ6jfYbVNGeNkSBIAbcaVZyGTc4kLunGgdN74mMgVUgreuRV3Aho7T5fUENxj9WAmeQ5DF7frD3TX4FR8SV0ZU4g8lfZlkepIrW_BGWvkzRG_10IDWE_jzEsJd85nqMI1uEwcGvvfUAQ3QhkceE8l45g1-_lh-bV2Uug6y5T1hb-rYK0hPzQSwRgGPQh4tikO3wdAEfsSYf4DBSfRxbI9lCF5VTVh6gLx-2B9UQ1vu8fNf6v1k-QgSCT1XH8hiSexBjVEwDcdFZUx8yJCHCfLnpDSk-QsjVbznRurxEsKuLKB8Zgw5fSg4JtZXHwFyHOAv2qD4wJPvvEW8fg8q_OWjsLPWL_9DrS0-kmY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
آنچه در بازی دیشب بارسلونا رخ داد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106744" target="_blank">📅 11:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106743">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-Eht22afIexjk_2-ViajeFB2mbyDX1y-fV4kzGsi-MiL57oMwd-TscsECtyVmcTTzsOEobIah6eBro3MYFcbg4aRCtNjY2SOlxPAPICZXoX4TlBQHU5IuGk8bS6RcgmvGk57bDvWoXcoK1sHic0U-8d28tZTAaHxQIjzG1MTAeSG3lhHLSzePWm13EnlHgODWOGYJwlrh1e94lBtIGzGH3MTz8n4sREFNQqLT19CAqrk9_nLT6a2UQfIQKDGeCA3O689MIF3PpChs3N0HdwapGS-TxeWNywCm2yaZ1TlJq3OFqrdmhF0MyJ-5sfc5qDxHNLH4eFL0VT0LV8CQjajw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📱
علی‌ضیا هم رسما با انتشار این عکس اعلام کرد که زید زده و دیگه سینگل و این‌چیزا نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106743" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106742">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106742" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106742" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106741">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MD_yEX2LSvcXmh0V3rtCzF10-x02lMczFy8f9yNOcGe_MDvLIfhyqO9UQ9e954TvyhzGEBICDuJIru1YfTwjfMfPI9fEoFUzJ_aiuk2ZCRyrOi5xtLmj7DKKs-q8CSUVqC5aC7_reNOzSppnibqPMnyLtuWqMMral4qmtfMgrI5i5fm0sv5Rnnbo0wG3VE4uErcjv1VogJvIFx2sFzyq9Ov6roIajm8aHWP7PDXuBWLizKPup1SUmn7X22SEybWAiNrl84I_H5OCS-bULJMqTCQd7O49EqQoNstm6JdTZBqrDVCqi7jXJavgW3eUi_IvEjaZk3qiUKdbscujuFqCiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ان‌ئی‌سی نیمیخن
🆚
یونتوس
نوریچ
🆚
منچستر سیتی
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106741" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106740">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee3ee373ec.mp4?token=uVIBMUZKFOAzTMFtdZnxHr7zAq6xEll_os6vvr9NvblHG02dRFiezlJjDxPfkYLcnBgPJH32TuhBLgVGNpuM0bYwXpD_E9JrgdcLQvqtIK5WNJz7dhLXN_m92D-H3ILS2tna3_Tjz8B-hu3rY35KTZk9G_mGGWgS9XykQAw1oOl9taoJ1ITUJUr2hkd-P7NTaw7Z8xu05Ka0GK4ZGyMFMVLAl5zwDxu7KyPuHkEUhef8pq-6CpJsUxfZ7UKEzBgElZPeb8hwFmOpcJvwWliRAL35iNvcu2V36sxymPb6CarwPd_Pj5Gys1_QKDWK26ZTlg7O2iPrOfIWtdJXIVC8WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee3ee373ec.mp4?token=uVIBMUZKFOAzTMFtdZnxHr7zAq6xEll_os6vvr9NvblHG02dRFiezlJjDxPfkYLcnBgPJH32TuhBLgVGNpuM0bYwXpD_E9JrgdcLQvqtIK5WNJz7dhLXN_m92D-H3ILS2tna3_Tjz8B-hu3rY35KTZk9G_mGGWgS9XykQAw1oOl9taoJ1ITUJUr2hkd-P7NTaw7Z8xu05Ka0GK4ZGyMFMVLAl5zwDxu7KyPuHkEUhef8pq-6CpJsUxfZ7UKEzBgElZPeb8hwFmOpcJvwWliRAL35iNvcu2V36sxymPb6CarwPd_Pj5Gys1_QKDWK26ZTlg7O2iPrOfIWtdJXIVC8WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
از عجایب فوتبال ایران؛ دیروز حین بازی تیم بعثت کرمانشاه و نفت‌وگاز گچساران یه نفر درب اتاق داوران رو شکسته و تمام وسایل قیمتی تیم داوری رو دزدیده
😐
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106740" target="_blank">📅 10:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106739">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebaf856a1.mp4?token=T15vaTsUkWwht5ZaAza3gDrt5DlJB0fTU5a2DGRWuLZWAgwXX6J5Pu8r25z3YM6052FM-MEePIXQisWANcxS71luUWs5o0L73CNjfIk1Ifw4mrhEGBXLuQRszAfWoqUL5TVJEQycF7awx1Vf-d3OhFJptA1xJq7zih8sAKMvSvuNwAir1Zyseoc1WnY2RQHT_8vtLUaG0fpVnPZDCjuMEZ3DwF3JDHG64cBAlT6cFfzEJ7l-ym2XS5dw89_fuelI2_kIpx_gY4S1FbLWFnyDl2WfCqFOj7LFSoRrouTj_6iUaN1n6pFCrz_K6XLlmD7cGIfhC-Fv11sC9I34aozAag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebaf856a1.mp4?token=T15vaTsUkWwht5ZaAza3gDrt5DlJB0fTU5a2DGRWuLZWAgwXX6J5Pu8r25z3YM6052FM-MEePIXQisWANcxS71luUWs5o0L73CNjfIk1Ifw4mrhEGBXLuQRszAfWoqUL5TVJEQycF7awx1Vf-d3OhFJptA1xJq7zih8sAKMvSvuNwAir1Zyseoc1WnY2RQHT_8vtLUaG0fpVnPZDCjuMEZ3DwF3JDHG64cBAlT6cFfzEJ7l-ym2XS5dw89_fuelI2_kIpx_gY4S1FbLWFnyDl2WfCqFOj7LFSoRrouTj_6iUaN1n6pFCrz_K6XLlmD7cGIfhC-Fv11sC9I34aozAag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇪🇸
🙂
آرزوی هوادارای رئال مادرید:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106739" target="_blank">📅 10:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106738">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
⚠️
خودکشی سرباز روس با استفاده از نارنجک پس از زخمی شدن توسط کواد اوکراینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106738" target="_blank">📅 09:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106737">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/704ad943ef.mp4?token=F497xBLfKLUrsrQVYVuqBiXJouMEhmIHpUCatYn-479TRYVrRi8j5UAUXUHiPLJxMrKEcCIyaYTTW1FDLmM-q8z1o2R3E-rN_V7aAdT5BWr0KTZ68bbHPyblkSPG-pGTOdjUxG4Wf5O8EIoVbQg3FY_O95PqH5HZV3h1zhg2oOImaW_67ADUwOTIEOZ_BgqNYQLKpUTwVsSTiqGpP4CNHvcmkqX9_dUnNPdyq9fsO4bDTpR0fFlhGG8s-88toLG1SjBfO7__nMpsovXHLbFOuSDpGUH_o3JCAvEvyJPGBgojHhYiSfPMoTv46QKySxnIsKCKANP00codJxNOGrla6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/704ad943ef.mp4?token=F497xBLfKLUrsrQVYVuqBiXJouMEhmIHpUCatYn-479TRYVrRi8j5UAUXUHiPLJxMrKEcCIyaYTTW1FDLmM-q8z1o2R3E-rN_V7aAdT5BWr0KTZ68bbHPyblkSPG-pGTOdjUxG4Wf5O8EIoVbQg3FY_O95PqH5HZV3h1zhg2oOImaW_67ADUwOTIEOZ_BgqNYQLKpUTwVsSTiqGpP4CNHvcmkqX9_dUnNPdyq9fsO4bDTpR0fFlhGG8s-88toLG1SjBfO7__nMpsovXHLbFOuSDpGUH_o3JCAvEvyJPGBgojHhYiSfPMoTv46QKySxnIsKCKANP00codJxNOGrla6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
کادو ولنتاین سمی مسعود شصتچی برا زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106737" target="_blank">📅 09:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106736">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546d8bc40e.mp4?token=f8szgZIsRJEaFijR_7r-TbQJix2sPUX3bjFC6nj-ua3UNU-WpzekZC_w4bHQq6IflVe5Vwr4bXP03Je3AMLXTlrdHq05AvLIFGgXjhEcT9V8G-lyXqB2fZineyh6IwTvL3AWvR35DhEAHPM-fe45mx_Z0KR_yclgh2V6BTWyvYFwy17zaWrxTjjtbHzb9Z4Bxjxi5x6PNZJ5G7Cq0M9Bro0V45lfysJ4xVLIgrqG4z6AM2n1njcHBrb8ZshJTImBDP0tIhH0CXoCb2D2IcUbv0ysiFzp8DZ0udiXxRat9roM5dfFRE2KAbxtdYfPbVuvrcWBj4fJQIXrGzZMsup8MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546d8bc40e.mp4?token=f8szgZIsRJEaFijR_7r-TbQJix2sPUX3bjFC6nj-ua3UNU-WpzekZC_w4bHQq6IflVe5Vwr4bXP03Je3AMLXTlrdHq05AvLIFGgXjhEcT9V8G-lyXqB2fZineyh6IwTvL3AWvR35DhEAHPM-fe45mx_Z0KR_yclgh2V6BTWyvYFwy17zaWrxTjjtbHzb9Z4Bxjxi5x6PNZJ5G7Cq0M9Bro0V45lfysJ4xVLIgrqG4z6AM2n1njcHBrb8ZshJTImBDP0tIhH0CXoCb2D2IcUbv0ysiFzp8DZ0udiXxRat9roM5dfFRE2KAbxtdYfPbVuvrcWBj4fJQIXrGzZMsup8MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
یه زمانی نوکیا به تمام ایده‌های ممکن ساخت مدل جدید، نه نمی‌ گفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106736" target="_blank">📅 09:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106735">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3Ast5JPNJPsL3mXb9c_dcHDh5s68sYgsWPbofGieHpZHC-JleGXBYPlVggowE6kt56u64w1cnAdVJoZoxXnqtfVrXVsO65uYlxj49TQGCDOrdHUqSuCv0PFhxVjRrojlfHm2V9x9kvqTm4J8dQ6kYRmRg-YDgAw6xaHb9Wgyxpn7Z19IyGs1JWJ6sI_H3JegKQ_-IzkCzJzXPCQJBzUYxfXBimRO7Tca8MKFojkBayq8qmHpDZvvQdKrRxOgO2smLDeUp9K8ae4G2uziKV8WFTHRxBwddt05dEHMOGYjyD6WCW6wSUdaI9r7SACm1JU7oeYAPrFsaaaGMmvMM6hBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🐐
با قهرمانی بامداد امروز‌ در جام قهرمانان آمریکا، لیونل‌مسی به ۴۹‌مین قهرمان تاریخ فوتبال خودش دست‌یافت و رکورد خود را بهبود بخشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106735" target="_blank">📅 08:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106734">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106734" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106733">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qpBzNDTltf4RzCvf2mkfDAMM-TxMj43EZksMn2s0xZGuLtNNViPcJdhnMHKduwFF8dpVDjduUR_aNro6x3zr_IG9e6DyIdCMO3WACw5jD1Ru-Tb-uXDlaB3Ia9VypsxuC-rsd-aeAD_sTj3EOG9aqYoz8jBII94VuhbcbUS2Y4f7TB50CTAmjYbiiYBZcqKZYlljlHvwGk5sViE-Ivl3rDvmeVPz2F50umUBEd4PFh0UiBzhfw_OMwC63y7qxVJTSNSjiWGZjEi0lea6vG1kbw9XcuxbcbO-h_GAXsCoGlbQKGY0pFBmaKQUJfGFfuu8HKoz88qk7V5u3LHF5rKhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106733" target="_blank">📅 01:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106732">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0WhiJMG6vE7RIivrQMvMhV9elaB5nD0JgkNMSgsRO2lih1oVmuw1pH_xrKY0d6kLwWHYfiEJw4s-vTdDwQFS3XldyMb8pVc8ZMaRHyy00HK9aMGlUbY4FkTkkhf1imyxyrLo7HyOALYS3ULRap2_Hm0FOYUYqMANjVaRkzUUtgBa7S1gn_Y0Yb0PyahszMUCepfZ7RNHlcRUThO0cwtJ8-m6YK49vHuLNxuKDIIE15UYaAggTrq2mnalG5f2UZNVO9Z5sBC9DXzxbbpcdvouiMhzP_M0HG5KwgYVbS9uNxMWObPiQUyJkCbVqLT4tDjlWSGKKQg36IwgKJveOvBqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
تواضع و فروتنی رافینیا کاپیتان بارسا:
🔻
من میخوام به لامین ، کریم و گوردون کمک کنم تا گل بزنن ، میدونم مهاجم نیاز به گل داره. ما خانواده هستیم ، توی خانواده باید مراقب هم باشیم و به هم کمک کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106732" target="_blank">📅 01:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106731">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8hh15YjvQT_DTH89JUcqfnNkYLZhbNBsmTQHvFb5_mgw1-ILp9J2KwF8V3d6fuYLOIEhClf7R6oARG9GpAmJuthGU9MOxAXRPJoJKF8vYxsO-uZEKbybtjE620Xmr73rOb6nsZAqiNFjwOckiVhst3XOMhly6jz-Bu36s6k-oHHmxsbmY38e2_32frt2QHXhqzXg5-jfsyTw0N0uhWlOv1ukLbNL0HrNv4n1sadWEsjlyeD0Q7rRqmHbUJ7HOOLQsUrUUPu8PEoGuC6i1GH7Vc8wbSFk_nju7DV-0S0jIuCD3K4TuScFd8AtGGvmWJ5JOJNewj5v14ghH91JB5DWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
تواضع و فروتنی رافینیا کاپیتان بارسا:
🔻
من میخوام به لامین ، کریم و گوردون کمک کنم تا گل بزنن ، میدونم مهاجم نیاز به گل داره. ما خانواده هستیم ، توی خانواده باید مراقب هم باشیم و به هم کمک کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106731" target="_blank">📅 01:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106730">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OruG5Z5-NvGhTtE23GvPSeIpSNodngndruvpCloegsWaUOF1cfa6E3nM27ckrgv3fxcr7T6igsnb4JQcgOLR5bOBLeXmy-3Rv0id8tZshW7GTWflo1uVPtqAHattrcQwsGeg8EK3ygErbKq923x4mJVri_iPH8j0iUiJmkdskasBhu_3k8njwPGtiv-AwObt7Y-cBZl4x4JxhN0nHKQkur85UmNOsuSF63WGlt4CpBzIlzJA6ci_WF2WpTYuo9tWShL0x2G70zaSl4jFC-69cBtYYJWAiFLnOoku7kGr-98ap-b3OFrHnKX2nTIhTHTFqclhGAZfWpyM1Pwu1M9-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
شاهکار این‌فصل فوتبال اروپا بدون‌تردید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106730" target="_blank">📅 01:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106729">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1vtGlGvIldsanIz0rTnZtpSbMBsJa6Ogs1SRKPTeQyN8lPCqP7zstLq3fu0CXo6HzH3NWteEgAJBMJbKxVAvCz6txxQbvqCCOzVEZHUshjXUHky2YrCmUdSoTnzrc4Ow7GM6RMo-xjZWbMrxIJqCtrVkWIkEj0N9mC8IyCjUCibw25QT5Mg2udRiLJyp3N7cal8Sjn1RC5m1Yl51eLwY5zvk4waQdqSQaIna0eZ3asxE5jFoV9aXEzPDWx9pJtlcnoqnSEuRrpok1PmC8KoDdc9yjC1wcAuGrL3wfHVzSxNA6MgM4jOAhWgttoQuxacl6qXuLUU8vSQrHvn3gtQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇪🇸
وضعیت جدول لالیگا در پایان هفته‌ششم
⚔️
برنامه بازی‌های هفته‌هفتم:
🇪🇸
رئال‌مادرید - اتلتیکومادرید
🇪🇸
🇪🇸
بارسلونا - سویا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106729" target="_blank">📅 01:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106728">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnMS-_w4WksUEjysUE_snxcIeqd6XYO2fUju-Gz4sSnL6E3RFvVIkQe02XTC3n9qVROV28OcplLJrKG335cROGgZXa9sJ83aA1T71Pzg1CRk3pyENNtRN6RrZY7TnZYagagg6YfmZ9B71p3pCkcKDBPrPRiNi3LQs-_71a6Yq-8mP81FKQniJNbyRioX9-VDMzLgx26JbfIPgj8CNTbxmtCma05ikBZwUSCTAf9Iw7xwEE-7PdaIOL45hgJJZHm_-1zraynjaxpLOWx38hU51wylr3Qc9Cnxh5L3-7pdFNviHoZvrYfZRBK6xx2eyf2YDg-9AUpUZbcLjAlC11qtLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
بارسلونا بهترین شروع فصل تاریخ خودش را رقم زد؛ 7 پیروزی متوالی(لالیگا و UCL)
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106728" target="_blank">📅 01:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106727">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLRbLcwLqQ3v-oj4kgMKTr6BtIX1XHzTS6ZRzdxachTFNN0ZQi1-B93bSwUetEgvPSLgQY3NghRv_97wiZPMAwZ7zHjryhpUw9ABoIaFq_BWtMC3iAnO0PVJk-58Ho4iznWOOm8qnewlOdwrkUu_GLuxyETfGR8zROnX2Xj5uJx0RK4Df-q7jDu-ojpZvmECoDLUYcjTrBdsCHI40rTbbZWuNQPUPjPtJhOAViJSQNZkq-qsJS7q6bUhDLu27sgYguhHgVvRTwBKcCsEuLdquEU3JpVSOwCYVO71QfRa7Hll0-ER9ZRdEABsh-WBBYkJMMUDuPUDEWcppp5Wa0Or9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لالیگا| بارسلونا به لالیگا رحم نمی‌کند؛ همه را گلباران می‌کنند و یک سؤال: بعدی چندتا؟
🇪🇸
بارسلونا هفت - سانتاندر دو
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106727" target="_blank">📅 01:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106726">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">لامین‌یامال
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106726" target="_blank">📅 00:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106725">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">هفتمیییییییی</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106725" target="_blank">📅 00:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106724">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گگگگگگگگگگگگل</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106724" target="_blank">📅 00:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106723">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fd0c97753f.mp4?token=ANmBG4L08jm3Xacagfdy9AU9ilUjtT3FbRXnbp1-ZdXEshJTfT91D35xdTWIDvipmzzeslTy4Fi6eocGYeZdmjsCFAaKusaZPXKq5pB9zMFjDHh2NnFKEYPcWwKzr5bfV8E875TP02hMa8mqF0Ws4C4duTBJIH4C8-Lq5mt6AYb_HKfyXSx9NPj-InREcaTaArFAk5bMtfu5yh2f180mPG9BxlWXazUFSFqIjQ383PCBPoBybRY7_4GYjjWJtqKM7cOxU9SqahnJeHxpXlfxQL_vNzEb5f9vbYrUsN4uJx3PI-D2wLDFnc1yyg4mx4doEwUrnK464s7nvPyhcSmrpA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fd0c97753f.mp4?token=ANmBG4L08jm3Xacagfdy9AU9ilUjtT3FbRXnbp1-ZdXEshJTfT91D35xdTWIDvipmzzeslTy4Fi6eocGYeZdmjsCFAaKusaZPXKq5pB9zMFjDHh2NnFKEYPcWwKzr5bfV8E875TP02hMa8mqF0Ws4C4duTBJIH4C8-Lq5mt6AYb_HKfyXSx9NPj-InREcaTaArFAk5bMtfu5yh2f180mPG9BxlWXazUFSFqIjQ383PCBPoBybRY7_4GYjjWJtqKM7cOxU9SqahnJeHxpXlfxQL_vNzEb5f9vbYrUsN4uJx3PI-D2wLDFnc1yyg4mx4doEwUrnK464s7nvPyhcSmrpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا حضرت عبااااااس چه گلییییی زد
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/106723" target="_blank">📅 00:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106722">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پاس گل هم لامین‌یامال دااااااد
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106722" target="_blank">📅 00:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106721">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">چه شوت محشرررررررری
😳
😳
😳
😳
🔥</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106721" target="_blank">📅 00:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106720">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گابریلللللل ژسووووووووووووووس</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106720" target="_blank">📅 00:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106719">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">چه سوپرگلییییییییییی</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106719" target="_blank">📅 00:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106718">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یا مولا</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106718" target="_blank">📅 00:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106717">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b622b454a4.mp4?token=Ojwq7WYWF4b_AUBRInht1wdufFm6O5ndJ_N0ohdfbYGZT8DHfjYc0ZIZfXfNwWHAWX0EbAnLtIKBZF9yjvvPLBSDxmsygFC370u8G7Ok94yd5ataLPTX-oaQ38Hkarwnfj_hye5cK1q8cRQ8-Tut7nEDMrSlny742lhyvf9c9wvUO87UN2hntSUS8AA2Cu-Vh2atb4N4gfJ3VEvavVA3jx_CIbB2dPY3wznDh_Qptj4e82gI2c0jdOpp8C9dMZ71cOvfnN01rh6w_Pjr5ZCj6eTFAzHgvM7C_GKtPlmn2a9o6d3a0Cqpnis4MWMO73SbYcfqPsO4tmmcm7iiSjEtuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b622b454a4.mp4?token=Ojwq7WYWF4b_AUBRInht1wdufFm6O5ndJ_N0ohdfbYGZT8DHfjYc0ZIZfXfNwWHAWX0EbAnLtIKBZF9yjvvPLBSDxmsygFC370u8G7Ok94yd5ataLPTX-oaQ38Hkarwnfj_hye5cK1q8cRQ8-Tut7nEDMrSlny742lhyvf9c9wvUO87UN2hntSUS8AA2Cu-Vh2atb4N4gfJ3VEvavVA3jx_CIbB2dPY3wznDh_Qptj4e82gI2c0jdOpp8C9dMZ71cOvfnN01rh6w_Pjr5ZCj6eTFAzHgvM7C_GKtPlmn2a9o6d3a0Cqpnis4MWMO73SbYcfqPsO4tmmcm7iiSjEtuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🇪🇸
گل‌پنجم بارسلونا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106717" target="_blank">📅 00:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106716">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گلگلگلگلگگلگلگل یامال زددددد</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106716" target="_blank">📅 00:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106715">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گلگلگلگلگگلگلگل یامال زددددد</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106715" target="_blank">📅 00:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106714">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a4e9698bbc.mp4?token=eHni_bfBaM20KDW12q0Ah_8tUPljOFdEFzhQdoewN0dkaAHjpGkBAuZD1Die2rKKrx6yfpvdh8dt4qFYeIjS1c40STg2pk3jX-GWEvzQ5piKHNfmwRgjUUipDfoMl1ZSmYWnK9JvUCzJj9gB0gA1kMvHPJdFqJB4FzfiySTjbrj_KHgCEtmM18M4DdTKYG0BfMbJB0OmOlm5ToKmV53l-j9V-FrA5Ksu8rx3HrPRJ7AUQKUZ-lF_zdzAZBbFhPmfKRE4Z4IZ42H2eKu8Q2nZ0Dnwpr7e-UGHDe4fxIXJo7gM_ykkz2t6FOzjC9Ohott_kygNW1NcnCqYOhIB4jo2SIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a4e9698bbc.mp4?token=eHni_bfBaM20KDW12q0Ah_8tUPljOFdEFzhQdoewN0dkaAHjpGkBAuZD1Die2rKKrx6yfpvdh8dt4qFYeIjS1c40STg2pk3jX-GWEvzQ5piKHNfmwRgjUUipDfoMl1ZSmYWnK9JvUCzJj9gB0gA1kMvHPJdFqJB4FzfiySTjbrj_KHgCEtmM18M4DdTKYG0BfMbJB0OmOlm5ToKmV53l-j9V-FrA5Ksu8rx3HrPRJ7AUQKUZ-lF_zdzAZBbFhPmfKRE4Z4IZ42H2eKu8Q2nZ0Dnwpr7e-UGHDe4fxIXJo7gM_ykkz2t6FOzjC9Ohott_kygNW1NcnCqYOhIB4jo2SIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ریدمان محشر شزنی معتاد
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106714" target="_blank">📅 00:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106713">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رافینیا هتریک کرددددددددد</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106713" target="_blank">📅 00:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106712">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گلگلگلگگلگلگلگلگلگللگلگل</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106712" target="_blank">📅 00:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106711">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">رافینیا پشت توپ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106711" target="_blank">📅 00:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106710">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سومین پنالتی بارسلونا
😂
😂
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106710" target="_blank">📅 00:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106709">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پنالتییییی</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106709" target="_blank">📅 00:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106708">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وااای عجب ریدمانی کرد مرتیکه معتاد
😂
😂
😳</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106708" target="_blank">📅 00:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106707">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شزنی ریددددددددد
😂
😂
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106707" target="_blank">📅 00:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106706">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-9HAqRr9DPjd8Nc6rpAnYCbtoBREkIKnMPCvHzik-fUxPpzJ2ZsWAnPsx2stwHLAPl36ZaZQ6tcM-_AKCwdBwZVpnF-mFyFwuvnbKQgzVUivmnPvTo9g_wIYVyrnod_24m1tPj9tdH9TLjXw_VyXanWOMACEdQ80N9XU7ALtl8gYm9bHUXg_A3ZCJ729gqCm66zvXqst5V6dzoeWuY9YaRFKYTWLSRIF6LvmppqjAuTKF0OXcR0xPDFa5Z6nP2eXsFDtB7_I23CwFSqnHW9n6RAfM1NZZ5NaNp6yVkO3AbyBA4mEqDiq4BpeXViG0LKhLDRIM2J_hS92-jXCdBPfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل‌سوم بارسلونا توسط ژائو کانسلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106706" target="_blank">📅 00:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106705">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یامال دلقک کارت هم گرفت
😂
😂
🤣</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106705" target="_blank">📅 23:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106704">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33d7bb9281.mp4?token=E2dnzJ8rA6Oss4pLLCPlRVVf9eSc_kHvTtzl8C3iAGpnuGyHq2SkuvLG4-gk5dOT2tzWI15aMWo987w3ghFdATkukvD8RNuqPawZx-pAaNAF7R3K5PU-IQUNj96knNBeygAozIOZNdEM0YZg0w11QZmV-lgP6FcKkSmUUixn1i_9Q_6pPkIA6ZQi4vOQJ--8U2YwLcqm8USFK8ED8oydeDmBRZRfmA1Sxec3yaOdvQ2Pq48aOJYfLJtWdYTpzgunIA9YMyhOsUFpjlsGIZkLER4l8GN9XpV9CUQZ62ZJnWjP8bWnaOiNTiIVBmpwXvrkvAXFjBT5WmDc7Njt4LEsJoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33d7bb9281.mp4?token=E2dnzJ8rA6Oss4pLLCPlRVVf9eSc_kHvTtzl8C3iAGpnuGyHq2SkuvLG4-gk5dOT2tzWI15aMWo987w3ghFdATkukvD8RNuqPawZx-pAaNAF7R3K5PU-IQUNj96knNBeygAozIOZNdEM0YZg0w11QZmV-lgP6FcKkSmUUixn1i_9Q_6pPkIA6ZQi4vOQJ--8U2YwLcqm8USFK8ED8oydeDmBRZRfmA1Sxec3yaOdvQ2Pq48aOJYfLJtWdYTpzgunIA9YMyhOsUFpjlsGIZkLER4l8GN9XpV9CUQZ62ZJnWjP8bWnaOiNTiIVBmpwXvrkvAXFjBT5WmDc7Njt4LEsJoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌چهارم بارسلونا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106704" target="_blank">📅 23:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106703">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9b1574719c.mp4?token=s5I9Ix-McvzU2mL0V4B6RORVm1OZDdcUNQ1ryi6xMU4kikAiqjw9ofX9d2D5yXeCMF2MiU2dR9IOtjMpna43lp3QUsIdgpjKP5SpKoIwvlr3HLz1fdv0t1Fi4HkBBJaIL4JZN1RrvKytjnbnxmBc42_y0ifdsXGAa59UwoLKPk_o4mMFXwws79P2epYmi4hT-TyOLtW_mYLuku1YidVmhL2XeecJnXDpntVh1ZtFSBLhyzj-BCfuK_33TvjwBLF1fX6Y56tiomakQVtV3obPD8zRrlYfw5voF7zp_pS4cP1BAuXMd4oKrVW4ojjVEUzxuTA9IQQPe4y4eZXwO5YoRlmpsUibvSrK-BWG9R3-ylm58YjKNIfhrOpqJOjlCadeO50V3KfZc6RsqZgCCpoAxdGf-2eAXw4-CV9ZWB3F1EdsUadulI4PkUOVB8s1z5PqBAmaISjNnChJ3hgpLXH8y_fEW9l8FKx5R2tO1lEkS_X2AcOJOmaLnUIuW-vfQXcZV3nw9sbjEn0ba1gv__obAU-ktFQpTNIa8GbfdZo11cCq-fJLZhDDp5nb6p4d7dIeJvbBGnmkxecbx5HTxpFyJoi6eBtdfTkTwd45onV_6I9u796YTJLA1i76f1p1_hUPnMBsme8rziUhi1WIzCucc7HBoVL1OxV2-ZIr86ie4DU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9b1574719c.mp4?token=s5I9Ix-McvzU2mL0V4B6RORVm1OZDdcUNQ1ryi6xMU4kikAiqjw9ofX9d2D5yXeCMF2MiU2dR9IOtjMpna43lp3QUsIdgpjKP5SpKoIwvlr3HLz1fdv0t1Fi4HkBBJaIL4JZN1RrvKytjnbnxmBc42_y0ifdsXGAa59UwoLKPk_o4mMFXwws79P2epYmi4hT-TyOLtW_mYLuku1YidVmhL2XeecJnXDpntVh1ZtFSBLhyzj-BCfuK_33TvjwBLF1fX6Y56tiomakQVtV3obPD8zRrlYfw5voF7zp_pS4cP1BAuXMd4oKrVW4ojjVEUzxuTA9IQQPe4y4eZXwO5YoRlmpsUibvSrK-BWG9R3-ylm58YjKNIfhrOpqJOjlCadeO50V3KfZc6RsqZgCCpoAxdGf-2eAXw4-CV9ZWB3F1EdsUadulI4PkUOVB8s1z5PqBAmaISjNnChJ3hgpLXH8y_fEW9l8FKx5R2tO1lEkS_X2AcOJOmaLnUIuW-vfQXcZV3nw9sbjEn0ba1gv__obAU-ktFQpTNIa8GbfdZo11cCq-fJLZhDDp5nb6p4d7dIeJvbBGnmkxecbx5HTxpFyJoi6eBtdfTkTwd45onV_6I9u796YTJLA1i76f1p1_hUPnMBsme8rziUhi1WIzCucc7HBoVL1OxV2-ZIr86ie4DU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم بارسلونا توسط ژائو کانسلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106703" target="_blank">📅 23:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106702">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ae99f7d7c3.mp4?token=opToq2kTZLFCMEnPICKq8hz6k-VEseUo-KXMv64SLvd7CrXk0Kzr4ljtN9RtJQjkEieQ4Rfhju4ieLXAchcSpUBREL0C2oDioOeu77qoSxaUAjNZ4J0bHZO2jZIVgR_Q8im0XZzoF0WBOcd2rzhBae6Jqh-aSepWs2U5KJ0ZTWGJ90QtdyXePG3GKN7O8F9QTpAgZzCORdBDWHt4GBvNx-LrdVNYluXVavjxH97h-whsHfLH26crbpE01-goQ5UMSf7eA1s1L185cvPC2sjz3pyrfRJlXgiV2Q4JaMK1oLYWfbcW2xm2fI0jOk6KMzEKg9i35ebfAkpg1ez-AKmP5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ae99f7d7c3.mp4?token=opToq2kTZLFCMEnPICKq8hz6k-VEseUo-KXMv64SLvd7CrXk0Kzr4ljtN9RtJQjkEieQ4Rfhju4ieLXAchcSpUBREL0C2oDioOeu77qoSxaUAjNZ4J0bHZO2jZIVgR_Q8im0XZzoF0WBOcd2rzhBae6Jqh-aSepWs2U5KJ0ZTWGJ90QtdyXePG3GKN7O8F9QTpAgZzCORdBDWHt4GBvNx-LrdVNYluXVavjxH97h-whsHfLH26crbpE01-goQ5UMSf7eA1s1L185cvPC2sjz3pyrfRJlXgiV2Q4JaMK1oLYWfbcW2xm2fI0jOk6KMzEKg9i35ebfAkpg1ez-AKmP5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم بارسلونا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106702" target="_blank">📅 23:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106701">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">این دلقک توپ‌طلا میخواد
😂
😂
😂
😂
😳</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106701" target="_blank">📅 23:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106700">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یامال ریددددددددد
😂
😂
😂
😂
🤣</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106700" target="_blank">📅 23:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106699">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پنالتی دوممممم برای بارسااااا
😐</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106699" target="_blank">📅 23:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106698">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل سوم بارسلونا ژائو کانسلو</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106698" target="_blank">📅 23:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106697">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بارسااااا خوردذدذد</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106697" target="_blank">📅 23:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106696">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106696" target="_blank">📅 23:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106695">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رافینیاااااااا</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106695" target="_blank">📅 23:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106694">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بارسلونا ۲۲۲۲۲۲۲۲۲</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106694" target="_blank">📅 23:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106693">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106693" target="_blank">📅 23:29 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106692">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پنالتی برای بارسلونااااا</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106692" target="_blank">📅 23:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106691">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2a96773e1c.mp4?token=PoolVByt5jD9WoOocaA0vM5jSou6XEsKiVEZvEhRkpO0AlQPH8SjxXyr6TCsC2rV5ZiVCgk4296ZP39EWK8MiR7G6UbIAiRg-VUKoGByGHBJHTXfDj4et-1fH6WuMNe4s8wdkJBgFflHezmQbgDsX7DetWn6Ebn-pQa_BUDPo3qGIvkG-K0GQ2GQWU3KfBHcnyWDivmEFSY_1T-2TKwa6thVRqAGYYAHrUpdnq92W1lRWEBMubjOkqVhSClyoP5Eal9V74TZ9Ms-1WcxjV3ABchKyou2lF0SFTstRkg8BNtnNjp6YCuDqNJiwad_DmGrvv_ZDDtPCKWa4u497rJLqTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2a96773e1c.mp4?token=PoolVByt5jD9WoOocaA0vM5jSou6XEsKiVEZvEhRkpO0AlQPH8SjxXyr6TCsC2rV5ZiVCgk4296ZP39EWK8MiR7G6UbIAiRg-VUKoGByGHBJHTXfDj4et-1fH6WuMNe4s8wdkJBgFflHezmQbgDsX7DetWn6Ebn-pQa_BUDPo3qGIvkG-K0GQ2GQWU3KfBHcnyWDivmEFSY_1T-2TKwa6thVRqAGYYAHrUpdnq92W1lRWEBMubjOkqVhSClyoP5Eal9V74TZ9Ms-1WcxjV3ABchKyou2lF0SFTstRkg8BNtnNjp6YCuDqNJiwad_DmGrvv_ZDDtPCKWa4u497rJLqTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
سوپرگل اول بارسلونا به ریسینگ توسط کانسلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106691" target="_blank">📅 23:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106690">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ix2Y7447wO6ZYY4vJxnzkicgfKmhBm9dvzmn7TeYTSBz6VY11y4igoKsiKCX77oFAJ-OXfK2C-NpTplpeJo-aw_4PSc0c7re2K8rUd9XjDtJzjUC0C9SEbMORfcs6NA2gTqLEnlmAnGQxe1aihUWA_0HSzW9Qq8L4kXCafGITn8aW9r3WOCMabxo3P-6P311ze2u-Fh-iIvCen6sjoN31IJdwI6tqRjOazXN0kvUfbxU8aAdoQfcYAAWftg5yECm5xTaHX52HyAuhtM49NYvJ_DsSDmCcWvOg9gzJAYz_bcMkrGBB450HeQkZmWi-fjHcA7VBo4TI6uDzvYETWLq_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شماتیک ترکیب بارسلونا مقابل ریسنیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106690" target="_blank">📅 22:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106689">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCEaKuNMDWcWIQToRvBHLSdg7GICsSN0pS6Y5AJ2o1w_pq3odeWjWMQ5Ohy6goigOTaeSlYuAOp-D2TBOz_mgDOKWkR9lqsHqmDNeCh2Gl3AoJsOWWEyMZaOSFJM7qeU-Gatl3CCVLdBa9RRFG051ywuQvzefB3jnPLv-67rCqubAFYaDgZl7U708FgEE261LmHqMBqMXd4s2tyJ5zN89sKBsLqkx3xh12fhcmJPJNAOqgkdbABcgWGag1HWXOaCcH7RHNg8rEd9LJiL9g-gXVINkFVfT5pqNyuTuu3BtbhDgoGphLlDWM3zbw_OVdoPb3QuX57-FHduLC9U8G4bRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇮🇹
🇵🇹
لیگ‌اروپا؛ ترکیب میلان و بنفیکا
⏰
ساعت 22:30 شبکه ورزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106689" target="_blank">📅 21:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106688">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e46b13203.mp4?token=gmtRbKlWLDSsZolzNVnr_cjA6SZfN4BpWKpz6awm4qnvbvw4pzSwZk_qoAHZEHA6XUD-kbAv3GPEb8N3jM6caZrGUxZ9A4BHS3Ng9Qpwf5mbhzeol6g2MLgWOXbqDMc4nlUeLW288WEC6vbzFFEdBpYI3QTRM67SJ-GEJoypn-SunaTeTzFR1ycftFOynuLMaecXYoJY7TR3x7mgNJ9oMc1VV39Z-pIIWLqydzcXYPE_atqus-MelmWSQvsufb3Uihb5T1ZL2daKFTPlJgy9lp_rOe_NPuxe00T96BMRMWpr0S6piSazVeP5IqOEgayKqboaxJ-qmGZivuXqmfeBag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e46b13203.mp4?token=gmtRbKlWLDSsZolzNVnr_cjA6SZfN4BpWKpz6awm4qnvbvw4pzSwZk_qoAHZEHA6XUD-kbAv3GPEb8N3jM6caZrGUxZ9A4BHS3Ng9Qpwf5mbhzeol6g2MLgWOXbqDMc4nlUeLW288WEC6vbzFFEdBpYI3QTRM67SJ-GEJoypn-SunaTeTzFR1ycftFOynuLMaecXYoJY7TR3x7mgNJ9oMc1VV39Z-pIIWLqydzcXYPE_atqus-MelmWSQvsufb3Uihb5T1ZL2daKFTPlJgy9lp_rOe_NPuxe00T96BMRMWpr0S6piSazVeP5IqOEgayKqboaxJ-qmGZivuXqmfeBag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
همین حرکت دیشب رونالدو که
کیرشو
میگیره، تو ایران خیلی وقته توسط بازیکنان انجام میشه
‼️
پ‌ن: واکنش رونالدو به شعار دیشب العینی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106688" target="_blank">📅 21:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106687">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2943ca3183.mp4?token=dXt5BI-va6IT0F_ump1weqr2meCLqb549JXgvBfhxPzOdYZnodQzU-sxm4bNvafVTML8i4cwkRUkyWs3DJMc-S2NzjJH4s1D2CNMYTLApo5l6BMTjYJUAx7I2aFZkTUI1yDOe5kGy7FGRKrkZNHNkQGN3ESDrIo61spatoDJoNC41_u_0yMUhCGVMxuRdXqfc1rBlrAFN7QhEZek63ivuYvfyxqxcWQuT_gu9LBoEd7xymV8ZC3RV09SEMZKqMrkZE_uTYgsJHDAm3YfRHAVX3MwQ_vSlBcjzkBioZjzbfmFym6uUpQvlLDJlEWSgr--9hb4WLrNWWZKv83Nl1mFPzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2943ca3183.mp4?token=dXt5BI-va6IT0F_ump1weqr2meCLqb549JXgvBfhxPzOdYZnodQzU-sxm4bNvafVTML8i4cwkRUkyWs3DJMc-S2NzjJH4s1D2CNMYTLApo5l6BMTjYJUAx7I2aFZkTUI1yDOe5kGy7FGRKrkZNHNkQGN3ESDrIo61spatoDJoNC41_u_0yMUhCGVMxuRdXqfc1rBlrAFN7QhEZek63ivuYvfyxqxcWQuT_gu9LBoEd7xymV8ZC3RV09SEMZKqMrkZE_uTYgsJHDAm3YfRHAVX3MwQ_vSlBcjzkBioZjzbfmFym6uUpQvlLDJlEWSgr--9hb4WLrNWWZKv83Nl1mFPzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل اول اتلتیکومادرید به اوساسونا(جاناتان دیوید)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106687" target="_blank">📅 21:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106686">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f3f55505.mp4?token=QPDDKsnZZJ8-KJtz2Lwm4Ox5aAVw7npBULrLTu8fCDKClNhvPdqKLYytMD6GROeYxRnHTOzNJzjnwK5EXlGqX19DBRMvNbW7oqQ6VP0jyJ27Iqe9yCbona2_ik9Ak4XgT4k4SpPJ6oHXjcBy9MVyRphyNvBMr4DudFLT6gPU8tMVewYkfpK7Ve3czkN8J3QAP7zI3CMy0leg7R1MD5wOJTbPG7PQjvYvjeu3VNVPkD6pPASRCb_uiQagbqUB8Ncs4RfxdzOgSM9lkyqj9QoUULEjZyZzW7EAowcDbI_AoJNYYihKpwVuqMdbVCZsUzRjGhKVe466J7nERu0Irbn7MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f3f55505.mp4?token=QPDDKsnZZJ8-KJtz2Lwm4Ox5aAVw7npBULrLTu8fCDKClNhvPdqKLYytMD6GROeYxRnHTOzNJzjnwK5EXlGqX19DBRMvNbW7oqQ6VP0jyJ27Iqe9yCbona2_ik9Ak4XgT4k4SpPJ6oHXjcBy9MVyRphyNvBMr4DudFLT6gPU8tMVewYkfpK7Ve3czkN8J3QAP7zI3CMy0leg7R1MD5wOJTbPG7PQjvYvjeu3VNVPkD6pPASRCb_uiQagbqUB8Ncs4RfxdzOgSM9lkyqj9QoUULEjZyZzW7EAowcDbI_AoJNYYihKpwVuqMdbVCZsUzRjGhKVe466J7nERu0Irbn7MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شنیدنی و جالب علیرضا مرزبان درباره زنده‌یاد سحر خدایاری یا همان دختر آبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106686" target="_blank">📅 20:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106685">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f63c731d.mp4?token=MQToTnjHsir4meya3mlVB_GH1HU5_DOvi3sM7i8ab8ARzK8FbtVo2OCLcfOSW1kpO6tP05sxQs0P88A6BkqIGcBHw4fv1VYvuUDFd4zLXFI-_e7L1ZocGNgceXoc1ntWyMeQnLjMlbh_XxW1MmpoeO6VytdctcmLaG1zsTYu5u3YF8xpJwSgOuD-551vK0dHB0cHmyUB8lHw69HgzF2SAfWW3zEIWFgWTq45VmJlt84qO0adxWHE5zXYkFKYV4nM32_auTmv8vXuJ4KhpdMaOYt_eUBUeaIAzPo9ZPjTa5cBUOPZPhbB8gBxQxnAoWAs-_mRQ0Ip7dLrLxcefasP3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f63c731d.mp4?token=MQToTnjHsir4meya3mlVB_GH1HU5_DOvi3sM7i8ab8ARzK8FbtVo2OCLcfOSW1kpO6tP05sxQs0P88A6BkqIGcBHw4fv1VYvuUDFd4zLXFI-_e7L1ZocGNgceXoc1ntWyMeQnLjMlbh_XxW1MmpoeO6VytdctcmLaG1zsTYu5u3YF8xpJwSgOuD-551vK0dHB0cHmyUB8lHw69HgzF2SAfWW3zEIWFgWTq45VmJlt84qO0adxWHE5zXYkFKYV4nM32_auTmv8vXuJ4KhpdMaOYt_eUBUeaIAzPo9ZPjTa5cBUOPZPhbB8gBxQxnAoWAs-_mRQ0Ip7dLrLxcefasP3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📊
ترکیب‌رویایی قلیچ پیشکسوت فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106685" target="_blank">📅 19:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106684">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bac1a39777.mp4?token=lVKCIjQ97k_aOZR4Ldux6rkIM1jPlM3Kp8frjH0Bq0bPyGpt2p7yV_SfWqhBJ0z0MGTuJRQk6rea3y4Qts6Cm_SRx31qfBeydN0QMbQmWaUtrDMS2QuRGo5stfez8OyYGCoy70D_6xZDJI9GWtU-CRjGWSSG6Hsd8IAYTaW8mTaLr1cnlGS6i7uAeZlGOYdfIWLqejcaw3InczQlcvmtTqqfEs1Sgh8YmYlu_C6Uu3ic_GlYdANUkoEYAwy8_oSog5MI2DUpQCwDa4uoqmUASZ-LMjNLh879_mfr0qk2CjXkDKNrUHnV9FJu0Huy9LAEQFeJF63MCMd0zISuSKfyRivUTWwNTAbNBCDgUlg9Z8A9ybMeuj6QGkS9lmFj_2q54Uzv3Yqx2gaZCGrKlbFbxysW4oQyWjw5AZBNTHrzFVs5jPB62nP-V9Hhvr7yOUe_fUjvqnZTUP31KYWLA2GS0IK8SxI4iEftIEYTHg2CXg7yjnK7-LIdNtHZIZe_p6jnnkoyCUBpq2nu0Bk6W4i7G-KEwRhsy5g6a8x4airz6HfCEvUA8GUw12P_RPOWNL_c2ZTILVM2GZvwkjGchq_D22Vaqx2AoDhCSiVRkFWK2jE4Qrh2xEh5-OBBYNMgd6HGev4y5U1DMLEiD79ImWM6jLtDytkU5qHfeOHRskepj1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bac1a39777.mp4?token=lVKCIjQ97k_aOZR4Ldux6rkIM1jPlM3Kp8frjH0Bq0bPyGpt2p7yV_SfWqhBJ0z0MGTuJRQk6rea3y4Qts6Cm_SRx31qfBeydN0QMbQmWaUtrDMS2QuRGo5stfez8OyYGCoy70D_6xZDJI9GWtU-CRjGWSSG6Hsd8IAYTaW8mTaLr1cnlGS6i7uAeZlGOYdfIWLqejcaw3InczQlcvmtTqqfEs1Sgh8YmYlu_C6Uu3ic_GlYdANUkoEYAwy8_oSog5MI2DUpQCwDa4uoqmUASZ-LMjNLh879_mfr0qk2CjXkDKNrUHnV9FJu0Huy9LAEQFeJF63MCMd0zISuSKfyRivUTWwNTAbNBCDgUlg9Z8A9ybMeuj6QGkS9lmFj_2q54Uzv3Yqx2gaZCGrKlbFbxysW4oQyWjw5AZBNTHrzFVs5jPB62nP-V9Hhvr7yOUe_fUjvqnZTUP31KYWLA2GS0IK8SxI4iEftIEYTHg2CXg7yjnK7-LIdNtHZIZe_p6jnnkoyCUBpq2nu0Bk6W4i7G-KEwRhsy5g6a8x4airz6HfCEvUA8GUw12P_RPOWNL_c2ZTILVM2GZvwkjGchq_D22Vaqx2AoDhCSiVRkFWK2jE4Qrh2xEh5-OBBYNMgd6HGev4y5U1DMLEiD79ImWM6jLtDytkU5qHfeOHRskepj1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
🇮🇷
سورپرایز تاکتیکی سهراب بختیاری‌زاده؛ استقلال چطور السد را زمین‌گیر کرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106684" target="_blank">📅 19:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106683">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be6891deda.mp4?token=vAQ2D0Vx5L_mOIjJKFh7lfbhfEj8zHGrgQZbg_EfjgDSPiDfLoopCHIscBfHgkftX1StyoAfEf_FzmDUIl09a0kTGnxr319QJeVJr9cltiYdfnH0npoBcurzX31hE0lWZbz4r2lKM9j11MhNF-Ab4zjuPHjMn8PlfJ-fqL_sZpjOOnSkoGLoed_bJoCLRfoP0rCW9MOeeIUUHOYnuJoBmbtgx8cXRpGiBX3N3BxevR5DtNs_4W4xMrx3s2tSaxfR-rNPF_DjT3NpIyahTZTz1eGxxVwIcyW4OzfYabruoojKWT9f8rnQNgJGcfRKRyvvj09CNeBR-5yVB58tQNG56AkDGEMyHK1tubePIHlKu_Jg1fkJ_zwVUUMZvBG4m1LY2xnIoEN8447XCw4FHr9Ta3QecfkxJFzAzJhRUVCzqhcDCdLJZ1j8eTBFtOwCZsGjHuy5oLm7DrbnNRKYZw8pYluQ2u3hdkl6vfKB72Tnxgb9vfHP64H0vHJjTZdJ9P-WOMnTzFpH-LrYdi8CPyasMFmJySmrFVScbFRTXSon5sdSogAPWtB7g6-VWCIX8YBtTNflLc8Z6lz5oLghRmn0gNfB6ywfM2dfXk3lMZm8QWvJ01PY_c-d8e3yu92Lur3R85yEFpMwQ-PEDcAwuTFDklfJvKGhT1nuLwZCmuJ0s3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be6891deda.mp4?token=vAQ2D0Vx5L_mOIjJKFh7lfbhfEj8zHGrgQZbg_EfjgDSPiDfLoopCHIscBfHgkftX1StyoAfEf_FzmDUIl09a0kTGnxr319QJeVJr9cltiYdfnH0npoBcurzX31hE0lWZbz4r2lKM9j11MhNF-Ab4zjuPHjMn8PlfJ-fqL_sZpjOOnSkoGLoed_bJoCLRfoP0rCW9MOeeIUUHOYnuJoBmbtgx8cXRpGiBX3N3BxevR5DtNs_4W4xMrx3s2tSaxfR-rNPF_DjT3NpIyahTZTz1eGxxVwIcyW4OzfYabruoojKWT9f8rnQNgJGcfRKRyvvj09CNeBR-5yVB58tQNG56AkDGEMyHK1tubePIHlKu_Jg1fkJ_zwVUUMZvBG4m1LY2xnIoEN8447XCw4FHr9Ta3QecfkxJFzAzJhRUVCzqhcDCdLJZ1j8eTBFtOwCZsGjHuy5oLm7DrbnNRKYZw8pYluQ2u3hdkl6vfKB72Tnxgb9vfHP64H0vHJjTZdJ9P-WOMnTzFpH-LrYdi8CPyasMFmJySmrFVScbFRTXSon5sdSogAPWtB7g6-VWCIX8YBtTNflLc8Z6lz5oLghRmn0gNfB6ywfM2dfXk3lMZm8QWvJ01PY_c-d8e3yu92Lur3R85yEFpMwQ-PEDcAwuTFDklfJvKGhT1nuLwZCmuJ0s3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚪️
توضیحات مجتبی‌پوربخش درباره فساد ۶ عضو ارشد فدراسیون فوتبال جمهوری اسلامی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106683" target="_blank">📅 18:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106682">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83fb9dbe46.mp4?token=g7JPRpb752CNd98FCacgoJE2FATm3_mHbxixrJMxYKi3Fh_UNemjcSvAk_uqOC-2FftWjkt9vgw0bIopEHK3UbUIY238_pO4bSazlbSRI63gY2LV-tHM4CpiA4IPLXNuqjNGzzWjW0MOrYmuYQ_fBqikYMCFV_qUJF8JPLOq76Q6sL5atI9bviqZgmbEMH_qFBHUkkQyk6Ir3jQJ6rkHUivtiIoJo1sAdiog5X1lgfVm4r1uSUYocBz_92GOKKDYX-ABuhhEfwaWUSJbXlWBhdzOhYNDCX-0f1F72VPqSux-wRR67VKjh03MwU3jcVaTfOlXAqNxaRLz5Tm53pYzqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83fb9dbe46.mp4?token=g7JPRpb752CNd98FCacgoJE2FATm3_mHbxixrJMxYKi3Fh_UNemjcSvAk_uqOC-2FftWjkt9vgw0bIopEHK3UbUIY238_pO4bSazlbSRI63gY2LV-tHM4CpiA4IPLXNuqjNGzzWjW0MOrYmuYQ_fBqikYMCFV_qUJF8JPLOq76Q6sL5atI9bviqZgmbEMH_qFBHUkkQyk6Ir3jQJ6rkHUivtiIoJo1sAdiog5X1lgfVm4r1uSUYocBz_92GOKKDYX-ABuhhEfwaWUSJbXlWBhdzOhYNDCX-0f1F72VPqSux-wRR67VKjh03MwU3jcVaTfOlXAqNxaRLz5Tm53pYzqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
قائم‌پناه، معاون پزشکیان: اگر بنزین را ۸۰ هزار تومان کنیم، می‌توانیم به هر نفر ۷ میلیون یارانه بدهیم!
❌
پ‌ن: ۳۰۰ تومن یارانه دادید، از ۳۰۰ جای ما دراومد، برای ۷ میلیون چه بلایی سر ما میاد ...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106682" target="_blank">📅 18:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106681">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106681" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106681" target="_blank">📅 18:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106680">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvpPsWYfZep7-0w18cDbiewPmDLUYODZ5psuNsXw1wS8M5uobK2FEnKFV1ddix8RL3uh1GCMKRGSLlFcjcJRrvlgjeJV3Ciuz4UCE05s6JxvWW-ehig1fMXxZ29rkZWVvwop0EF0XHU5kiIIEB3tYja9UV4MHfTHVj_-OCefAPpOZ134Eied9Zr5UsuQcyeHZQfo2sQ_lEPfZQvahNqxCR-QvckSWcXJtRfPnqpbhofuGQbDc8lEaV6WUu79-zvJKFd7G_WMCUiYTE4gurBYGRCwYzXv52wIYc04oNYRucm0NqN3UI-Bo8gKRrJwx7rkrl5FHtSWK-V-qc-qaZzbWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
راسینگ سانتاندر
🆚
بارسلونا
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
راسینگ سانتاندر: ۲ برد، ۲ تساوی، ۲ شکست و ۹ گل زده
⚽️
بارسلونا: ۵ برد و ۲۱ گل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106680" target="_blank">📅 18:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106679">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpki1gwcLLVjLoRjwJtDGiGuzBrHBlJqYzv-351Hdlc087G2OHvLmHVDDOOFmNYj9xamc9qWayhsPTKiZc12Rmw-nkn1-zGLEuMfxSBmaXW-D2tq8wt9rC6yQsMKn_KyxMES4kC6e9onV0ww0zxy4ZpswHgEpBROk9degyktEI6GYcoOPE9GBd-JmdOo2J-60NrTuWOh36k_jGrZjqUHZ9t-RS-enfpbdIu_ht8OTClLU22mIuydRU25q9a0jjLJJKmHzSsVZ6aejw5nOalaPIll6aL-zkQBRABh2fL0VlZLSsRTIvu_hnw3RrlOZXuaArr_LDPJ8tECx6u6Z9vzEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اعلام زمان‌برگزاری سوپرکاپ اسپانیا
نیمه‌نهایی: ۱۳ و ۱۴ بهمن(۲ و ۳ فوریه)
فینال: شنبه ۱۷ بهمن(۶ فوریه) در استانبول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106679" target="_blank">📅 17:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106678">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3XYLQRINg2okpT1RLM_HjsF674stKEDjLRQrW5hKDVBap58D4oWQQ53fJ291sfUR7JpLAQ4eUSkQl7XnU911iBwGvOaULQEXa3e_wW6zn85oq2BmjVlERmjBJ8po8tiaQZaf7t6QjSPTv53GedG4M59qWtEiJOT597ZFoa4pbGVFWOvQVZmHUADacYOkTjUFXGbJ4WgowKLQZhNM2BZa6qszPcJfXGGY9OnBADec8emK8GjlJOQ0-fv2gQ6qa2q0RgeXOJgF-U-p1eL3vSxrD2-S0Qx47wFp02DXGCXq5emQMn2pzWHbC045obTDbVTN9cydzKluVCmdPTKED4cjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
مقایسه افتخارات ۵ نامزد اصلی توپ‌طلا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106678" target="_blank">📅 17:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106677">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15009e843d.mp4?token=X0Iy0b8HurfVOSGoIN6Qn74ZTOSdKkHveqOh0HTfhnuyImliNWx5cwtWILIWPtha1jUqx4Wa35YwnpFU5UyzjBNLxnpzCC8qm2IVKe6XgUCOBCSfxpyhUy5u7m_-c8AFmtsq6roMwc9I3OnY4vgchs55jSXjuSPUipJft6YtgguHtG6tfmz2gKwNmbCrmpguCDNbRMTB-6Q-WzNbQpIiuY4sLhQMZ5GiaXGowmWLHyV5kQRrgYM78nLOx_iHjLdbuT0MLAoZ7jrUmfMRnrRzcdEBPELbv_FiWqVk3gTokFmUaMn-ZvCF9t-GnLcJLS-l0akXl9DPWHekC3wp62NiwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15009e843d.mp4?token=X0Iy0b8HurfVOSGoIN6Qn74ZTOSdKkHveqOh0HTfhnuyImliNWx5cwtWILIWPtha1jUqx4Wa35YwnpFU5UyzjBNLxnpzCC8qm2IVKe6XgUCOBCSfxpyhUy5u7m_-c8AFmtsq6roMwc9I3OnY4vgchs55jSXjuSPUipJft6YtgguHtG6tfmz2gKwNmbCrmpguCDNbRMTB-6Q-WzNbQpIiuY4sLhQMZ5GiaXGowmWLHyV5kQRrgYM78nLOx_iHjLdbuT0MLAoZ7jrUmfMRnrRzcdEBPELbv_FiWqVk3gTokFmUaMn-ZvCF9t-GnLcJLS-l0akXl9DPWHekC3wp62NiwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
واکنش دیشب رونالدو به تشویق لیونل‌مسی در ورزشگاه العین امارات!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106677" target="_blank">📅 17:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106676">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268cfcdc63.mp4?token=gMJSNU44r1bX8ocdH6g0_iuWMTSQIbBcy8NT7RakrB7y0_sEAH53Y0xu1YS-cwAzq84bydMa-p-eGNKT3ZtYANFxrfGE8UD-vkZDmcXkGVQPbVNsrMJKH-rcB9H6J7U6b7vpZ2_ep-Muok-byf9v9QJBGy-Qi09Y6-miBB2kdUKJtgIwd1tKQr9Ut7-FENsL_x1sYEqhgEXWNJyxhPgUsgYGbRCgu2VrpptF3aDVksKCOyVTk828kjEtm1Pxhduh9ihG5FSGvI-gqYCj78MzTiRBPWhhnFekUCBQhbNfXYAeHBtzlKMoyhCxKTJYgBzFq4IHO-imVRT97h_3IZ60HI3TnmTHTleL7F0eJBVmbXsmsusfzu8K3hzUrBK9f1Heez_mAjPfdJQX5rFzxf0FsFkvGLMNOir1i5_-O-o4vkf9m7hU0DUAOyjbLF43CHBQA7885Rz8hqvY7mNoYtx3fFTGNzIcIx6YHLhpKCJngzD1fkrZKlzZBVAbJbQMLliGVZm0g7B4pzzSwiJSa7V0nCJmi0Kfa4awgSBR0vcFUZ5UrTsGIx_dN3PsTFT1dUcmowg0LIbGMLLIqgRClS-zpx3Naq5hUe-e3LFuJh6Qiry5CNWsV1oYbNUM9H9Yc3ppaU_fm7nBw9p6aWmUHDCCgmcagb8XEORXq54b5xO7AMU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268cfcdc63.mp4?token=gMJSNU44r1bX8ocdH6g0_iuWMTSQIbBcy8NT7RakrB7y0_sEAH53Y0xu1YS-cwAzq84bydMa-p-eGNKT3ZtYANFxrfGE8UD-vkZDmcXkGVQPbVNsrMJKH-rcB9H6J7U6b7vpZ2_ep-Muok-byf9v9QJBGy-Qi09Y6-miBB2kdUKJtgIwd1tKQr9Ut7-FENsL_x1sYEqhgEXWNJyxhPgUsgYGbRCgu2VrpptF3aDVksKCOyVTk828kjEtm1Pxhduh9ihG5FSGvI-gqYCj78MzTiRBPWhhnFekUCBQhbNfXYAeHBtzlKMoyhCxKTJYgBzFq4IHO-imVRT97h_3IZ60HI3TnmTHTleL7F0eJBVmbXsmsusfzu8K3hzUrBK9f1Heez_mAjPfdJQX5rFzxf0FsFkvGLMNOir1i5_-O-o4vkf9m7hU0DUAOyjbLF43CHBQA7885Rz8hqvY7mNoYtx3fFTGNzIcIx6YHLhpKCJngzD1fkrZKlzZBVAbJbQMLliGVZm0g7B4pzzSwiJSa7V0nCJmi0Kfa4awgSBR0vcFUZ5UrTsGIx_dN3PsTFT1dUcmowg0LIbGMLLIqgRClS-zpx3Naq5hUe-e3LFuJh6Qiry5CNWsV1oYbNUM9H9Yc3ppaU_fm7nBw9p6aWmUHDCCgmcagb8XEORXq54b5xO7AMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
روایت مجتبی‌پوربخش از اعطای مجوز فوق‌العاده عجیب کشف معدن توسط فدراسیون کشتی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106676" target="_blank">📅 16:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106675">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d14f705b.mp4?token=OB8KdolT-HsiB75Z1PUCRU4PIUnnrNonxb1EkILcUTAudc9HnNX5GVCZnQoqhIV-mS92KMIxFdFXPohZ4OMywROGkJRCYG1xwAqh_KLQ83boVJsEk2_up6JJLXn9jMTPGIM4zQ2tz_PGPA4zsknf5dUNPVkXo7DuwoAGB7ZySRb8fB_H0tMKL1Y2xDWE_LRktRVkLgvoTiMvbNa-SxOgoJdEA3gFTmKBSV6ZbyBMg7623IjCoQesHJ0HWUtTWQcO-FM92erVgZLaA3TvizDNs5i8tHfxpwZxbWgumUt7OMtRpp4--ceMvehTQX4u-ZoFMtK9G-qRb6kF9wpbtMFTzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d14f705b.mp4?token=OB8KdolT-HsiB75Z1PUCRU4PIUnnrNonxb1EkILcUTAudc9HnNX5GVCZnQoqhIV-mS92KMIxFdFXPohZ4OMywROGkJRCYG1xwAqh_KLQ83boVJsEk2_up6JJLXn9jMTPGIM4zQ2tz_PGPA4zsknf5dUNPVkXo7DuwoAGB7ZySRb8fB_H0tMKL1Y2xDWE_LRktRVkLgvoTiMvbNa-SxOgoJdEA3gFTmKBSV6ZbyBMg7623IjCoQesHJ0HWUtTWQcO-FM92erVgZLaA3TvizDNs5i8tHfxpwZxbWgumUt7OMtRpp4--ceMvehTQX4u-ZoFMtK9G-qRb6kF9wpbtMFTzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل توتی در یک‌دیدار دوستانه در ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106675" target="_blank">📅 16:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106674">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nalzeKwf4eQqMcoFNNhtjpPcEerrssvhXfiO51wW2MpLLBZovTmyJgHdUaVl6UYOJAFvw89cZfd4lUzW6hDWW20DGWuoNsUOtHfFYUHqRTdPiPmxOA_ys24Gu57Iq75XKYMKjPJ-XvrTF24GjnE3ODE1r5YuoRrmpCE_u_8BN3S5jNLda1zrtrlCfTNEwBo03U33d-HFEMyu-KEu7kt_vJUuMPWGUkFGGkWQf3ie8FurXvID7St-msqj3ZZFQsZhcf86-mqVXvJIcHWmIC2HUZ0igVExQGZNK0JXXLiognhz2Q7FScZxUX2iFDZRlaWt5RkaQvC5nQhqR1Zyt7nrRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
مصدومیت حبیب فرعباسی سنگربان استقلال جدی نیست و این بازیکن به دیدار روز ۱۶ مهر مقابل تراکتور تبریز خواهد رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106674" target="_blank">📅 16:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106673">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21bbacd491.mp4?token=g0zsTA5Fn5a5gVBBWmgHvPSGPsMKoN8nWGXJBdDhGmnyV1bnpk2HiTuZ7Q558gQHGwY7_NOM9hbslnCTmaCH2IDbCYtPS6jGdfmOvilUm2yfmento05COVeDIPOvPRzjUW8ihyPkc2JecYQhOP4BiBemQS1DXeuvr0YYwbXsn9bHTF-lCwntAyIDw5M9eFUbehNJxZGFK_4PJ1KE7F3wPC6Boohyjn_Js_hfBSiTIREQ5r70Zju7F_MKt8yjKaOPCSQSpa7je3MKxprDHKonb9kuk5kqa34lqZXMHHNvHi5M5rw7UO1AM8jUeXwYopjEvveU--t430c9IWCH9BkwBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21bbacd491.mp4?token=g0zsTA5Fn5a5gVBBWmgHvPSGPsMKoN8nWGXJBdDhGmnyV1bnpk2HiTuZ7Q558gQHGwY7_NOM9hbslnCTmaCH2IDbCYtPS6jGdfmOvilUm2yfmento05COVeDIPOvPRzjUW8ihyPkc2JecYQhOP4BiBemQS1DXeuvr0YYwbXsn9bHTF-lCwntAyIDw5M9eFUbehNJxZGFK_4PJ1KE7F3wPC6Boohyjn_Js_hfBSiTIREQ5r70Zju7F_MKt8yjKaOPCSQSpa7je3MKxprDHKonb9kuk5kqa34lqZXMHHNvHi5M5rw7UO1AM8jUeXwYopjEvveU--t430c9IWCH9BkwBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
👀
صحبت‌های عجیب و بامزه پارتنر مهران مدیری در سریال مرد سه‌هزارچهره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106673" target="_blank">📅 16:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106672">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6760fc381b.mp4?token=JWb7JOKhlWbJlRbAmYE1uJxcWbWGLxRo-A4TJVFegYrbIJOFhXwYY0Q3pCJ-z_meZa028wPXTZ1Hi9OjGZCCE75KbQ92WMflh-xfSLfK0p7R9FW_u-sET0WnkR9ZsZnx0VrUZ0p7oIizsdk4FYNMEyBza417r9nDJsXpOyNdSIuoBFcf43ANPqaOWx0Syaln_VpAcnCE1FThpXkJODpveAjnEK6Cf2SgNALdd7WVMTE9FVzsRB4dvZHEfBisE5p6xjbGcprX6GF-TVeD9AkMDDdG2UOcTP0DcVJMUepWIBL6WqV6QbCwehMwLaKCKIdnbYHzk2yTFjqvw0ZF0Urx_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6760fc381b.mp4?token=JWb7JOKhlWbJlRbAmYE1uJxcWbWGLxRo-A4TJVFegYrbIJOFhXwYY0Q3pCJ-z_meZa028wPXTZ1Hi9OjGZCCE75KbQ92WMflh-xfSLfK0p7R9FW_u-sET0WnkR9ZsZnx0VrUZ0p7oIizsdk4FYNMEyBza417r9nDJsXpOyNdSIuoBFcf43ANPqaOWx0Syaln_VpAcnCE1FThpXkJODpveAjnEK6Cf2SgNALdd7WVMTE9FVzsRB4dvZHEfBisE5p6xjbGcprX6GF-TVeD9AkMDDdG2UOcTP0DcVJMUepWIBL6WqV6QbCwehMwLaKCKIdnbYHzk2yTFjqvw0ZF0Urx_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از استاد آریا بام رفیع دبیر زیست کنکور تو چند ساعت میلیونی ویو خورده و خیلی وایرال شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106672" target="_blank">📅 15:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106671">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c4e1abcd1.mp4?token=jaj5wVcGRR15ZHy9pt5EviALgmfUPaxg4q9KovdDqUB5r00r5jUO0puzkJ-ANw1xSAJdVTT4ocoug4EAP19iGN58W7AYJjQhKiqTAw1KhSAbpPhYPtp4e2ONwGcZrkQ_AGaOwf5ujQ_n3k5sDYrrBnyCpybOPygAPTuoxdaYR-SIKtBlXRAR7Ac4A5zGnNxL9Itv038xjxIqIfjs1f0l1FccDszfqnQoEno9mZnh63Rb-Y3ah-pB1-V2rM2nCoIc0wGpxYNiXqNROkOka4AIVRXw0exMvl5JteuD3XUYDkfF90p6Gta3sWl2pm12SIKzPT3UWEa0yvAZLLbsfqgsOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c4e1abcd1.mp4?token=jaj5wVcGRR15ZHy9pt5EviALgmfUPaxg4q9KovdDqUB5r00r5jUO0puzkJ-ANw1xSAJdVTT4ocoug4EAP19iGN58W7AYJjQhKiqTAw1KhSAbpPhYPtp4e2ONwGcZrkQ_AGaOwf5ujQ_n3k5sDYrrBnyCpybOPygAPTuoxdaYR-SIKtBlXRAR7Ac4A5zGnNxL9Itv038xjxIqIfjs1f0l1FccDszfqnQoEno9mZnh63Rb-Y3ah-pB1-V2rM2nCoIc0wGpxYNiXqNROkOka4AIVRXw0exMvl5JteuD3XUYDkfF90p6Gta3sWl2pm12SIKzPT3UWEa0yvAZLLbsfqgsOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
هانسی فلیک: چه به عنوان مربی، چه به عنوان هوادار بارسا، در فینال چمپیونزلیک ۲۰۲۹ که در نیوکمپ برگزار خواهد شد، حضور خواهم داشت.⁣
❗️
خبرنگار: لطفا به عنوان مربی ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106671" target="_blank">📅 15:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106670">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a617f5cf34.mp4?token=ajyTX1Y-MwNviwzWK7ijhBiQ3jKnWRXJFuFPaqryiLh5UPQgTUsLVKr8iMcW4qK68H3e9B2dBQ9eLYSIzFh_TIUE1HSjofLZ27I9_0EoCHKrZsTByIrkwuB0oh99vWWdrfdkh2uIQqmmZFQT0y8QBlId5fKReGOufWTlBMs7Ot2uF8p_lI9D1biYS1HYOfsBu4QIqd7x74DggATJqhKZ-_S_MJGb8VklD-ZkN11eYkGtfUEClF2hoo4ExckTDMXZrANMb98iTRqETs-_Y3xKxDDf7Gtej3bWxkoOjHKjrZYyWC1Dh4aHfQzNtj-PTOOkFu5XTnaImtQyAN4tnnV0Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a617f5cf34.mp4?token=ajyTX1Y-MwNviwzWK7ijhBiQ3jKnWRXJFuFPaqryiLh5UPQgTUsLVKr8iMcW4qK68H3e9B2dBQ9eLYSIzFh_TIUE1HSjofLZ27I9_0EoCHKrZsTByIrkwuB0oh99vWWdrfdkh2uIQqmmZFQT0y8QBlId5fKReGOufWTlBMs7Ot2uF8p_lI9D1biYS1HYOfsBu4QIqd7x74DggATJqhKZ-_S_MJGb8VklD-ZkN11eYkGtfUEClF2hoo4ExckTDMXZrANMb98iTRqETs-_Y3xKxDDf7Gtej3bWxkoOjHKjrZYyWC1Dh4aHfQzNtj-PTOOkFu5XTnaImtQyAN4tnnV0Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
صحبت‌های هانی‌رامبد درباره ضررهای مصرف سیگار روی بدنسازی و عضله‌سازی؛ حتما تماشا کنید بسیار مفید و کاربردیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106670" target="_blank">📅 14:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106669">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4b40a7a1.mp4?token=fosqxvNgTOtt7FG-0sOLqXlsmY1AUajXh4uTjzFgRLpt1wd5_vc_YwThD9s8menffEFK3E6xx6PlnCCQaOmEj_42C2CwDKUQb6iqhKT4rQNOTk9fwq7HUCexJN27NVrmZbN2bx4w5ymoKLROrmxQA-K_XTsl4jSXj6mLqDPhzBlmq-uySQfFC_8ntV9VJf6SzlopVS7TRnue-hrRGKWkSjQHf3eegNEdEy8G4eKiScM8AgXHA8O3thGRGTzi-f3N17Wx_NgRtzjUDldq_6CwZO_FFzw1KYb2c_9tLFy0Tm8EjvtQXFGlVONf6tah-BP7Mn_VWipoTHja_8s5F3LhlDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4b40a7a1.mp4?token=fosqxvNgTOtt7FG-0sOLqXlsmY1AUajXh4uTjzFgRLpt1wd5_vc_YwThD9s8menffEFK3E6xx6PlnCCQaOmEj_42C2CwDKUQb6iqhKT4rQNOTk9fwq7HUCexJN27NVrmZbN2bx4w5ymoKLROrmxQA-K_XTsl4jSXj6mLqDPhzBlmq-uySQfFC_8ntV9VJf6SzlopVS7TRnue-hrRGKWkSjQHf3eegNEdEy8G4eKiScM8AgXHA8O3thGRGTzi-f3N17Wx_NgRtzjUDldq_6CwZO_FFzw1KYb2c_9tLFy0Tm8EjvtQXFGlVONf6tah-BP7Mn_VWipoTHja_8s5F3LhlDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇪🇺
🇪🇸
رودری: قهرمانی برای بارسا دست‌یافتنیه اما بارسلونا مدعی اصلی قهرمانی چمپیونزلیگ نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106669" target="_blank">📅 14:25 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
