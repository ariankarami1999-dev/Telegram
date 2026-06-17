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
<img src="https://cdn4.telesco.pe/file/kKowCpNPJWYoPs0AGJhnEIXmHNELLZlPiz0xaPkmljxdzBYOsJWZAQuSXVHvxEwxB9wKZYLUeSr0V9ZIsonXBhW96qZcUiQdWExkajDCU-GHlZjD2orpfmOLfXTJdd7Q1vQQetV_UDt2XTbHLVGOsPOCXSWPOhC77x028mFdEFnau39T8j5xtxiLJjAyL28nGMbZ5Pfv9S73fcFkl5UnfyZMYzoXLJob1uPLm9E_lU0uS986M23m6Ezn6icD0YSlf3nYCo_t9y4quvIx81VAm5c3WiaLR7DQ8NO9FyVCHNDNA4ksRSzHjEgS9HOOsy4djnDTRkiwxsypqA89N3MUaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 223K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 13:42:08</div>
<hr>

<div class="tg-post" id="msg-66346">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1725e10790.mp4?token=dxNSe7dzjBUe7jHOPzatp0_DhkWivvu0ywrb7A7oVhOiRQTv1IhbHXCEfSUlxsDFoic4v3RcGsmEIwijdMTl1AHOunlqa4Zg9xAGxxM5BkKXh0nN9GSv1YZFRU5EDRTsZo_FpHEFNuMI6E1GtYvD_32X61ea1byhl2_wksrSeYWS1wRtefYaYLxzYAUg-a_-A1W_o8S26bVg3-XWs7iN2kzdoFLRk-6IYoAYq7_dd9awAxLDUHEqG3OXDNiYCF95JI-BhdSwoXIO8ODaj4YPwG6je5IWQ3xwHYOIDI0y08rzvcv2YkL00BWPNFcIKm5RnoFBxWis-U7FPfJ073YIjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1725e10790.mp4?token=dxNSe7dzjBUe7jHOPzatp0_DhkWivvu0ywrb7A7oVhOiRQTv1IhbHXCEfSUlxsDFoic4v3RcGsmEIwijdMTl1AHOunlqa4Zg9xAGxxM5BkKXh0nN9GSv1YZFRU5EDRTsZo_FpHEFNuMI6E1GtYvD_32X61ea1byhl2_wksrSeYWS1wRtefYaYLxzYAUg-a_-A1W_o8S26bVg3-XWs7iN2kzdoFLRk-6IYoAYq7_dd9awAxLDUHEqG3OXDNiYCF95JI-BhdSwoXIO8ODaj4YPwG6je5IWQ3xwHYOIDI0y08rzvcv2YkL00BWPNFcIKm5RnoFBxWis-U7FPfJ073YIjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
بالگرد کاموف ۵۲ روسیه برای رهگیری پهپاد انتحاری اوکراین بر فراز مسکو به پرواز درآمد:
در جریان موج حملات پهپادی صبح امروز اوکراین به سمت مسکو، یک بالگرد تهاجمی کاموف ۵۲ روسیه تلاش کرد یک پهپاد انتحاری اوکراینی را در آسمان رهگیری و منهدم کند. این تصاویر بار دیگر نشان می‌دهد که جنگ پهپادها تا قلب پایتخت روسیه کشیده شده و مسکو بیش از گذشته برای مقابله با تهدیدهای هوایی به ابزارهای غیرمتعارف و واحدهای هوانیروز متکی شده است. حملات پهپادی اوکراین در ماه‌های اخیر به زیرساخت‌ها و مناطق اطراف مسکو شدت گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/news_hut/66346" target="_blank">📅 13:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66345">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJszvPg2qluYm2yiUpKE40nwVl7yFYiQH2_HAuERTekoNFTueZZTQ-9-EyDUTY04fj7JJd1p5dRwmsaM8vB_CO7yT8Kwt7chlF0fD_t1nn0a_U1N1RCzY241qVDN8JVRl9nLhaLda5bn4PBlalk7oOOi3T-NOyL2XV0abVsUyq93US67jcPvkP2jDLlv-WTzZ-zTkZuJ7nlIy1ytACMhyws2IXJZF5NqDHsPkzvV8ldo3bMbN6gLxPUAGX6hGirWQR30Taa_-kcZCA1_bZRxWbOFLAxMjiVvn7MWceRLxQsOvfoA1EAvHVCArGRiGIQden63eL-btvL5Lmm1oUNH_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مارکو روبیو بعد از شنیدن خبر توافق
😔
@News_Hut</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/news_hut/66345" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66344">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66344" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/news_hut/66344" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66343">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScyjBYR4GBbhLlK57qhkyU2lC96IWZFOdYhPtup0bPv6prC8VHRJqhQWyirZrQylaakjnLzH6A6MKWwXeNwqqOhT5MiS8tVLAl3Gw5a3CkfH9DDMf_cikXUP-hCxTOEcheLn-jQh8vaXIYcixpHwCNvUluw39ZfBOQm9pD_30VLW0yFjC83kKsSQMhoZqv_4MiB2IpCXU3aC2HeUIA6ewDAh4Svbwfx4l3PH2ZSI4YkvbNzRKVRQSnD23g5vAVrpLcc83e4HxzAhk4IPtk2_Mw1uu0pHAT3anO8ufnrRW_gYMLrJO_VcYNQJOcKm_0eY_BF6g8PSVwQx4ERhzqDcdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
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
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/news_hut/66343" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66342">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHrzQoQ2IKPffqgwpgWQjCZVKY0Z-8lyVKf05aIm26hUoi6dpaFdZm03gsckCLbBksAgmcN4ZZ2Ci9DW86m_j5uilXJH6et2a8hABlUMLUffOD40D78yxTDVrE3GnVqsBj1IVLCZUQJ9r4MDXxNjIfNvs1gVA_AiJxCr0ItOMFM2-GKjFoL-J-bYZbNbVDPXHQigDdF5htu2hgODT49njilX69dNeKQgYFpW53uSBIoQ2KK_YH1e-KLLNCxK_20TVd4y8xmrU-mDq5C9IKT5NTsy9OCwPwIHlKkGhd2-KUu9LkM0aID83nfMvq14V42038lFAAd6oC5fwpfdoYyUjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
شبکه ان‌بی‌سی به نقل از یک مقام آمریکایی:
رژیم تروریستی جمهوری اسلامی با وجود اعلام یادداشت تفاهم با ایالات متحده، همچنان تعداد زیادی پهپاد به سمت شناورهای تجاری در تنگه هرمز پرتاب کرده است. بر اساس این گزارش، سپاه پاسداران از زمان امضای الکترونیکی این تفاهم‌نامه در روز یکشنبه، هر شب اقدام به پرتاب پهپاد کرده اما نیروهای آمریکایی موفق شده‌اند آن‌ها را پیش از تبدیل شدن به تهدیدی برای کشتی‌های تجاری، شناورهای نظامی و خدمه حاضر در منطقه رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/news_hut/66342" target="_blank">📅 12:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66341">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIhpvwUUlx76VuZjsVmmhDm0Y7JfyuhqJ1mBmsly49i1jqWRLTnZ2RhZbBlWk-u4mHz5m1kKPhYuEzkbL4o9x3iPeY9CTs_Ao_5bg499g0gR2BmNSH3yaInMV2h75sRN1V8gfhKEKVzy-TEee3MQzN7vvvBXdDzpNDkauUSZXrSr7U7lIjd29fyBuM0o3EBACTPdHN7WbaFu1OEo_LlaZMgcVbFjuwztGR4xWjKUtK6sKSk5g_j_SqJZJ2gW95g2kARG_gS6iRVDxdY6Z0Hn3HsV1WevEQjJ2eJT5m1XgzIX9GY7Dp_LOq3pifBW2qoEJ7jqs8IrpI-HVk4t6tnrdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تغییر چهره پسر ترامپ طی یکسال
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/66341" target="_blank">📅 12:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66340">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d976a7f361.mp4?token=UrTY5C9CSpwbhC_gL_r6yj_swXtBJK5YPHk3p1HDhURMZQtEGl4Mv5g4eWFdz4NVDUBVuCik94RlOSP6fIbVpAJThPGN0Juj3b0Brcq8JKPg0zjRqkV3hjHWruO9611MlW-xAL02OYolxKb0BoZrnTWjQH6_Os2Cu0w2QdQrWDDx-vTcxGmRYTtP8aykVoiY94Cj1Wa8zLQvj6nHcDUneG9w8mmAa_C2NdqFUqrljwg6kfCUGrNXurlqbrG_nyhDvugdxFKLLh9W24zwnNOmta11n5Jr9Ljkptb1jEjEMc1uQYe-3NdTTUDTqcGWFUBnb9pmCjcTfL0ftAnwsCUHuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d976a7f361.mp4?token=UrTY5C9CSpwbhC_gL_r6yj_swXtBJK5YPHk3p1HDhURMZQtEGl4Mv5g4eWFdz4NVDUBVuCik94RlOSP6fIbVpAJThPGN0Juj3b0Brcq8JKPg0zjRqkV3hjHWruO9611MlW-xAL02OYolxKb0BoZrnTWjQH6_Os2Cu0w2QdQrWDDx-vTcxGmRYTtP8aykVoiY94Cj1Wa8zLQvj6nHcDUneG9w8mmAa_C2NdqFUqrljwg6kfCUGrNXurlqbrG_nyhDvugdxFKLLh9W24zwnNOmta11n5Jr9Ljkptb1jEjEMc1uQYe-3NdTTUDTqcGWFUBnb9pmCjcTfL0ftAnwsCUHuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تداوم حملات ارتش اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/66340" target="_blank">📅 11:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66339">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac69a7be8e.mp4?token=jm2tOWWzLZgkxTZ1evE2dcu1j88cRbmRGAF45Ga8v6S40MDuwd5YUYFFpMcrG6uH3H2oXEi_uDRv991XZG3RSPww2utQD3_uqPfKU0zWis1J1NiR75lcRZgDVQUq_RbNfoW8ZrA3LJNKTixbnU2LxAvDBwibpe-TPBWxIYl6hJ1A0QkChw56d78m9XPjErZq0iQX5wrt_6Di-g-htgVLDa1nJRtid4CsQKhJ3INPlSLLHBZVgAKmv0mUoJf34wBno787BhY_kOaNACZKWrUhA9lEuTlK2ChoEAcipnpTi1Z1hRbtJIceqUTkEXY4O5-gk3_nii86hxFHiqcLyQnsSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac69a7be8e.mp4?token=jm2tOWWzLZgkxTZ1evE2dcu1j88cRbmRGAF45Ga8v6S40MDuwd5YUYFFpMcrG6uH3H2oXEi_uDRv991XZG3RSPww2utQD3_uqPfKU0zWis1J1NiR75lcRZgDVQUq_RbNfoW8ZrA3LJNKTixbnU2LxAvDBwibpe-TPBWxIYl6hJ1A0QkChw56d78m9XPjErZq0iQX5wrt_6Di-g-htgVLDa1nJRtid4CsQKhJ3INPlSLLHBZVgAKmv0mUoJf34wBno787BhY_kOaNACZKWrUhA9lEuTlK2ChoEAcipnpTi1Z1hRbtJIceqUTkEXY4O5-gk3_nii86hxFHiqcLyQnsSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
مایک پنس، معاون سابق ترامپ:
به جای توافق، باید اجازه داد نیروهای آمریکایی کار را یکسره کنند، تنگه هرمز را باز کنند، توان نظامی تهاجمی رژیم ایران را از بین ببرند و به مردم ایران یک فرصت واقعی برای آزادی بدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/66339" target="_blank">📅 11:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66338">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ba759cb9.mp4?token=tr7aex7J9PpV9hgvQjkKfoLRu3-lE7HgdedlUcoPKJjrfxyDwoeIyD2tNy_j5IGC2VqDGrRm-pmTIMvAdAz_kr6CtTrUKosXC1eQ3JJM0ItK0Sc7jGILcEm-xrO_SVfcseTUDBnbLV-kaslMAYXljMZwUPe3AUjuDkhjF_slhXwetz_IupakAY86Z4YOmAaYY7EMDLEkjMUgWaUdp8a0sp6MhCN6AK5j_kLTo4huW1jzG0FGjan9tIV_XqXqOYTFtPUesI7GFW8VHBTvjrAyD4O4T0l61pHSv0oMiQUE69GHGC8XwJsaMhVbYpFcOUNJBJbnqFDZLfEAYIXgwg6Ibg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ba759cb9.mp4?token=tr7aex7J9PpV9hgvQjkKfoLRu3-lE7HgdedlUcoPKJjrfxyDwoeIyD2tNy_j5IGC2VqDGrRm-pmTIMvAdAz_kr6CtTrUKosXC1eQ3JJM0ItK0Sc7jGILcEm-xrO_SVfcseTUDBnbLV-kaslMAYXljMZwUPe3AUjuDkhjF_slhXwetz_IupakAY86Z4YOmAaYY7EMDLEkjMUgWaUdp8a0sp6MhCN6AK5j_kLTo4huW1jzG0FGjan9tIV_XqXqOYTFtPUesI7GFW8VHBTvjrAyD4O4T0l61pHSv0oMiQUE69GHGC8XwJsaMhVbYpFcOUNJBJbnqFDZLfEAYIXgwg6Ibg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی نماینده مجلس:
اگه کسی ذره ای عقل داشته باشه به جانشین شدن فرزند رهبری میخنده.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/66338" target="_blank">📅 10:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66337">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWGgIbAFAh-p3psj_CYS8dtE7AdWjVKeuZ_14Qh31DfCJnw1VYL6LNCxvqdvhXJ2j4Dy9XWGu4UeaKIYWx0egx8CTL7umR0EMNLuRSGMXHyCuW0Y4sha2-_E9DNp6LpiL1ajpnt4UsWrFvg2eQtS2GKoiFSuyEdnom4TjREnhYtnK4Bjrv6FlOeONvs1CKbyF2-RIcSwf4nDuZgWWmT28MIFfktpXQAvi7cL5hJaVF6x_-kJJZ_JPsqvWuGYWQuYEeuETIuWpyl2ZAM28iIl2d80Vym50oTvgIinxL57qGbQP9O-n68AXaF74ZZPGQFwnKgBtQ_9D_hxwL-xAworSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
مجلس سنای آمریکا طرح محدود شدن اختیارات ترامپ در جنگ با ایران را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/66337" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66336">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d9bfbe9c.mp4?token=jiYfqygKWk7QjT8fQ8lkG2vOhHSBKEi5ESo4svb1eg0D86SZcKFI7kw7xizcjjd13PgT5ODHzLlL4D80m-EhBHcgjfVx5P4_iAQqtdj8T4G0E7SKwoOb7mKM8tHvzYJd8mbD_a8SagXL6XdacuCPCv8tVsqEtsS8itG6h8bzAYVmttMh1j_8hc0aLMMmxXyh0H_UDN7db12IASeQx9ZEcfR340gv2cf7yV9NAMZ6GAsgumIShyHGxezuHU5BhtNefBM_ifjpktp3pEwrcA31j6lfPgPUfUVr0xaBMwTQ0fbXi4hAomP7Z6AviGzMNl9v6NdeoIegqn2SwQgJHqeOSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d9bfbe9c.mp4?token=jiYfqygKWk7QjT8fQ8lkG2vOhHSBKEi5ESo4svb1eg0D86SZcKFI7kw7xizcjjd13PgT5ODHzLlL4D80m-EhBHcgjfVx5P4_iAQqtdj8T4G0E7SKwoOb7mKM8tHvzYJd8mbD_a8SagXL6XdacuCPCv8tVsqEtsS8itG6h8bzAYVmttMh1j_8hc0aLMMmxXyh0H_UDN7db12IASeQx9ZEcfR340gv2cf7yV9NAMZ6GAsgumIShyHGxezuHU5BhtNefBM_ifjpktp3pEwrcA31j6lfPgPUfUVr0xaBMwTQ0fbXi4hAomP7Z6AviGzMNl9v6NdeoIegqn2SwQgJHqeOSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس درباره ایران:
اگر دونالد ترامپ به عنوان رهبر ایران انتخاب می‌شد، دموکرات‌ها همچنان می‌گفتند که ایالات متحده باخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/66336" target="_blank">📅 09:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66335">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/555366529c.mp4?token=WXMXb34ih5L4VC1mtd14LvheITyzyWSQUWiRxkLPGA4dxzUAJlPofxbI8aD6wqFyWC383OB0K2qVCFKx1dDixJUHNOH-SvNPmoEgDLMVS4Ju-quCl30lyV3OGl-xyJ5rZ-07M-Hcw9dH9-Zis11AYefNMDBKcoehVDlUp4x-AC2rIIlUIWk6cClEYhZ7iINtXXeYU5gCoNFyHqdNETfFmrXgimVgG2d6Pw9NJ41wWLP_AHV-GIx1PKuY5agivcyeET3pF92o47mLGCLspEC8S_HUzl5nM6Aw7s5km1B8_Hu2z0CImtykHXcC0h31QvflfCOIeNM601t43rlA9ZapSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/555366529c.mp4?token=WXMXb34ih5L4VC1mtd14LvheITyzyWSQUWiRxkLPGA4dxzUAJlPofxbI8aD6wqFyWC383OB0K2qVCFKx1dDixJUHNOH-SvNPmoEgDLMVS4Ju-quCl30lyV3OGl-xyJ5rZ-07M-Hcw9dH9-Zis11AYefNMDBKcoehVDlUp4x-AC2rIIlUIWk6cClEYhZ7iINtXXeYU5gCoNFyHqdNETfFmrXgimVgG2d6Pw9NJ41wWLP_AHV-GIx1PKuY5agivcyeET3pF92o47mLGCLspEC8S_HUzl5nM6Aw7s5km1B8_Hu2z0CImtykHXcC0h31QvflfCOIeNM601t43rlA9ZapSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وقتی نماینده میخواد ثابت کنه زندگی ساده ای داره و اونجور که همه فکر میکنن نیست
😂
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66335" target="_blank">📅 09:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66334">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66334" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66333">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/izX9t_nHwSuFKRcgpXxrV17WlcwJshmHTqzUN0IAPS6ndyEi2xJSF-RCt1zjennBqukmGeQbxvvNuLjBxnvBfkQ8hAVgOlHqX_Gk4Y6LhRmC83M5ZFsREJfmTVYVyZC-1PATCB4g1S6SvbqHQWk4lt8ElDkSjKYUL0QPlFVCAMl7nyNSRwOeh4npPRAfu91_wakTZ6D4ACm14gYcquyPXQLiPNBUCndGg6_9VSUr8UH7SOZ4mvrBQrxX88U85RwpjfeNiEWn5-pK4YDmyKPuBWj81sSgdjrnctc_1kyQCfW_Ua--md2LGdXSEb-p1zcXxcH_pyaybH_GBqVxlBH99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66333" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66331">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
به ادعای باراک راوید مفاد توافق ایران و آمریکا به شکل زیر است:
ایران، ایالات متحده و متحدانشان خصومت‌ها را متوقف خواهند کرد، از جمله در لبنان.
ایران تعهد خود را به عدم توسعه یا دستیابی به سلاح‌های هسته‌ای مجدداً تأکید می‌کند
ایالات متحده و ایران متعهد می‌شوند مسئله دفع ذخایر اورانیوم غنی‌شده ایران را حل کنند.
ایالات متحده و ایران درباره غنی‌سازی اورانیوم و نیازهای انرژی هسته‌ای غیرنظامی ایران گفتگو خواهند کرد.
ایران وضعیت موجود برنامه هسته‌ای خود را در طول مدت مذاکرات حفظ خواهد کرد.
ایالات متحده محاصره دریایی را برمی‌دارد، از تحمیل تحریم‌های جدید خودداری می‌کند و در طول مذاکرات حضور نظامی خود در منطقه را افزایش نخواهد داد.
ایران ترتیبات لازم را برای تضمین عبور ایمن کشتی‌های تجاری از تنگه هرمز، بدون هزینه، به مدت ۶۰ روز فراهم خواهد کرد.
ایالات متحده متعهد می‌شود دارایی‌های منجمد شده ایران را پس از اجرای تفاهم‌نامه در دسترس قرار دهد.
اگر توافق نهایی حاصل شود، ایالات متحده نیروهای خود را ظرف ۳۰ روز خارج کرده و تمام تحریم‌ها علیه ایران را لغو خواهد کرد
.
هر توافق نهایی شامل برنامه‌ای برای ایجاد صندوق ۳۰۰ میلیارد دلاری برای بازسازی ایران خواهد بود
ایالات متحده به ایران معافیت‌های موقتی تحریمی برای اجازه فروش نفت در دوره مذاکرات اعطا خواهد کرد
مذاکرات بین ایران و عمان با مشارکت کشورهای خلیج فارس برگزار خواهد شد تا ترتیبات مربوط به حمل و نقل و خدمات دریایی تعیین شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66331" target="_blank">📅 00:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66330">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9122af9759.mp4?token=DlCvA-Ppuoce8qQCp3mAihszzejvoZ5L6tU_i5Dv0oMOqukNMmshgybS5CRg3e3N_bN_4NnExe0V6eNfYrYXjIkbkxJUUeLo7CF6IYzABl8NpiPocg5eqhvko0No2hcEZL9aLgOj7b5EiGaP3XDZXSuewyY5vzfKopXwM_cNTCeKlyn_3m0-2h9OHVvTqHn-O75YoSIr4bYJCqlPu2W8PgVY1dc6GRv-JDX8RzkRl40swHLZLXlZhEE417mM59-kDmf7NqJz7k61mll_t3GhVkgSvl7HCKRTrHTVZmBHVdwOvWvB-PLEIJhekdJYyr9wE8-9Ab9m4kTvsvr7doK6O29Rt4Y3e5z7HuHBixQPYOFOHnzQrz_tj8wLvzY75LwRM2faCSwZvNIeqhRUOld6AV47Cb_dvXR6ocEXCgMszib-eKG1kyLGNPP5BsRCt43-YHO0uSOgq8D8QHWyFBqIEQKHgEEJnQSZsiEUHSiZIl0ueS2apzeajXQvFQSDvk3ZCShiXxahYfod0yYwS63JP74XktpKn4z7JWAYi0fuOjfHdpWL6_vaZsAOPrkRJvhvQVJhUYLleOyFlBHlXGUrcu_rrWVKk37aAp-LhRnn2EzVfxYauuC-Z1ArbJp3xV8xvn2vCFp2cp8gY1EG3YYDkYpHcJMpfM9mdT3RxA1XueQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9122af9759.mp4?token=DlCvA-Ppuoce8qQCp3mAihszzejvoZ5L6tU_i5Dv0oMOqukNMmshgybS5CRg3e3N_bN_4NnExe0V6eNfYrYXjIkbkxJUUeLo7CF6IYzABl8NpiPocg5eqhvko0No2hcEZL9aLgOj7b5EiGaP3XDZXSuewyY5vzfKopXwM_cNTCeKlyn_3m0-2h9OHVvTqHn-O75YoSIr4bYJCqlPu2W8PgVY1dc6GRv-JDX8RzkRl40swHLZLXlZhEE417mM59-kDmf7NqJz7k61mll_t3GhVkgSvl7HCKRTrHTVZmBHVdwOvWvB-PLEIJhekdJYyr9wE8-9Ab9m4kTvsvr7doK6O29Rt4Y3e5z7HuHBixQPYOFOHnzQrz_tj8wLvzY75LwRM2faCSwZvNIeqhRUOld6AV47Cb_dvXR6ocEXCgMszib-eKG1kyLGNPP5BsRCt43-YHO0uSOgq8D8QHWyFBqIEQKHgEEJnQSZsiEUHSiZIl0ueS2apzeajXQvFQSDvk3ZCShiXxahYfod0yYwS63JP74XktpKn4z7JWAYi0fuOjfHdpWL6_vaZsAOPrkRJvhvQVJhUYLleOyFlBHlXGUrcu_rrWVKk37aAp-LhRnn2EzVfxYauuC-Z1ArbJp3xV8xvn2vCFp2cp8gY1EG3YYDkYpHcJMpfM9mdT3RxA1XueQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
جی‌دی ونس درباره ایران:
🔻
ترامپ هیچ‌وقت نگفته که هدفش این است که رضا پهلوی را به عنوان رهبر جدید ایران منصوب کند. چیزی که او گفته این است که اگر مردم ایران بخواهند قیام کنند، عالی است. این کار خودشان است. این موضوع بین آنها و دولتشان است.
چیزی که ما می‌خواهیم، توقف برنامه هسته‌ای ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66330" target="_blank">📅 00:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66329">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
جی‌دی ونس:
🔻
فرض کنید امارات متحده عربی که یکی از بهترین متحدان ما در منطقه است، بخواهد در یک نیروگاه هسته‌ای در ایران سرمایه‌گذاری کند. عملاً بدون اینکه ما بعضی از تحریم‌های موجود در سیستم مالی جهانی را برداریم، این کار ممکن نیست.
🔴
حالا سؤال این است: آیا اماراتی‌ها در ایران سرمایه‌گذاری می‌کنند؟ یا آمریکا اجازه می‌دهد اماراتی‌ها در ایران سرمایه‌گذاری کنند؟ نه.
🔴
برخی می‌گویند خب، شما به ایران پول می‌دهید. نه، نه، نه. ما می‌گوییم فقط اجازه می‌دهیم برخی از این کشورهای دیگر در بازسازی کشورشان سرمایه‌گذاری کنند و برای مردمشان رفاه ایجاد کنند. این چیز خوبی است، مگر نه؟
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66329" target="_blank">📅 00:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66328">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400d2a3a78.mp4?token=V6USDBApyFXCuHXhA3Jh-4EvC-nKpt8_8QW_zj-mtXQDoSDjxM1XORiq2XaREC9Rtz8LyhQBianLeQURAWfYjUv4x8iGwNUm6X0aXqzm_55CbQOLIJyJoC-psdbVTafvulCKSWIyIPHt8wrdj0hhaEORBH-wf8WzymKtHuwLqfqdOplPVMx7GVXEL72Gyc8-Wd0-WpQmoL69QupFVFa6-iPdgr38WPp56PqAHhWhWCrnmmyDXgy6mnXaO2ZLVbIiP1tDu-UDt76-6iTgle1cWqGTls0UAOJvuasi-45Q_B-UDU0qcAUij1yohDNNrbqNZRUwm2AdxH6GJvSvfHP1LYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400d2a3a78.mp4?token=V6USDBApyFXCuHXhA3Jh-4EvC-nKpt8_8QW_zj-mtXQDoSDjxM1XORiq2XaREC9Rtz8LyhQBianLeQURAWfYjUv4x8iGwNUm6X0aXqzm_55CbQOLIJyJoC-psdbVTafvulCKSWIyIPHt8wrdj0hhaEORBH-wf8WzymKtHuwLqfqdOplPVMx7GVXEL72Gyc8-Wd0-WpQmoL69QupFVFa6-iPdgr38WPp56PqAHhWhWCrnmmyDXgy6mnXaO2ZLVbIiP1tDu-UDt76-6iTgle1cWqGTls0UAOJvuasi-45Q_B-UDU0qcAUij1yohDNNrbqNZRUwm2AdxH6GJvSvfHP1LYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🎙
جی‌دی ونس:
🔻
یک نفر گفت - یادم نیست کی - که این توافق مثل اجرای طرح مارشال وقتی نازی‌ها هنوز سر کار هستند، می‌ماند. این حرف از چند جهت غلط است.
🔴
اول اینکه طرح مارشال با پول مالیات مردم آمریکا انجام شد، اما اینجا قرار نیست پول آمریکا خرج شود.
🔴
دوم اینکه ما می‌گوییم فقط وقتی از مزایای این توافق بهره‌مند می‌شوید که رفتارتان را عوض کنید.
🔻
(البته کسی که این حرف را زد، سناتور لیندسی گراهام بود.)
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66328" target="_blank">📅 00:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66327">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7276198054.mp4?token=twf-8c9Mk6exaHa-BXrCIhjXZuQ8Ghuylzs2D8dUyT-6VRlsswdsAKrEnuc21GDPCSF14OROyIkwx1G0Dxy_nXKME6OWsysPdXN8Oqo8_hxYYe19xDPmHykEvcIUnXSBt30IqNMwwt4UGjrnd3WN6Gvjt7ff49wxmcQZucSvZOW-_FVgTpQZIuJ-52EmpTiZMP153mhsP_G8Eh9eLcRU6ZM-4S3b_wZQ3iHGi4V3A5B_FJJwM2d-zbhaKldxBN1NI-w9w6M6kxH0L2lsH6UHwEHa0pAF7rhopHdULSC-WmKB93yt94OhdmeSp94ev5XEPAcFLFWIb8O3joQjZohe1xMwcRwmZMNKTIXtPQoirgelxVuZX86czn88_mJPqElj9tvdy74qsfhLm_TxUT64zSuV5n5qmvTgL9Cg6tmIuPeyh3X_RLObBsC_6WdViLyyiscs4M3UsuKqJRomZj0-6UqF_XqqwWEAJPV1u0x2J_RjeMIlV9FBUhKIkSCN0joc10HQsnL7DJyAm4AmKt0XjLqgovMwRamUWpA--WoZpT3Gs7ZUULekXqxqika19cMA2Hz6CXXe0zFGRM1OuBaGpF0iDR0eu26MqElGzic3LdyO8pkxNPE2p6MdhALQ9HomaibSgb89oSP5UUXhYr-Y0Xzb6uOCSoDAbIdiG0a3FSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7276198054.mp4?token=twf-8c9Mk6exaHa-BXrCIhjXZuQ8Ghuylzs2D8dUyT-6VRlsswdsAKrEnuc21GDPCSF14OROyIkwx1G0Dxy_nXKME6OWsysPdXN8Oqo8_hxYYe19xDPmHykEvcIUnXSBt30IqNMwwt4UGjrnd3WN6Gvjt7ff49wxmcQZucSvZOW-_FVgTpQZIuJ-52EmpTiZMP153mhsP_G8Eh9eLcRU6ZM-4S3b_wZQ3iHGi4V3A5B_FJJwM2d-zbhaKldxBN1NI-w9w6M6kxH0L2lsH6UHwEHa0pAF7rhopHdULSC-WmKB93yt94OhdmeSp94ev5XEPAcFLFWIb8O3joQjZohe1xMwcRwmZMNKTIXtPQoirgelxVuZX86czn88_mJPqElj9tvdy74qsfhLm_TxUT64zSuV5n5qmvTgL9Cg6tmIuPeyh3X_RLObBsC_6WdViLyyiscs4M3UsuKqJRomZj0-6UqF_XqqwWEAJPV1u0x2J_RjeMIlV9FBUhKIkSCN0joc10HQsnL7DJyAm4AmKt0XjLqgovMwRamUWpA--WoZpT3Gs7ZUULekXqxqika19cMA2Hz6CXXe0zFGRM1OuBaGpF0iDR0eu26MqElGzic3LdyO8pkxNPE2p6MdhALQ9HomaibSgb89oSP5UUXhYr-Y0Xzb6uOCSoDAbIdiG0a3FSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇱🇧
جی‌دی ونس
:
🔻
اگر ایران حزب‌الله را تامین مالی می‌کند، ما اجازه نخواهیم داد که مجموعه‌ای از دارایی‌های بلوکه شده به ایرانی‌ها منتقل شود
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66327" target="_blank">📅 00:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66326">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8b2573c92.mp4?token=L5PJNXhgEX9qhvi_gmdaBDE7DNRGesKMEnN88scOHZ5L_KtLK9Z4_Yp5CipcR0jLOjn0NEZvMMeM1yJWcYVhmNSzn_nZm-r9pI7rcNafrwE0unZZaUmhuUxWmrvt0BP_iqbOacxk1ChBPPR3f_K3FOhhRdX_gGbRE0lTEkmPfN46T5ctn4y_t9NM6JzIWj9QKh2sqtUsG8W1EYqz6w8FfH1bMji1OxhrzVldOocieNmiTh0blNtX9Sq-SebCjL458GW4SPIWycDHekamVKjg548ViBaCi8OPWkzq-uDtX4wTjuIit2zAYJ3LKxk5yFHE50qTRnGr3LmzwPVd-r1THg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8b2573c92.mp4?token=L5PJNXhgEX9qhvi_gmdaBDE7DNRGesKMEnN88scOHZ5L_KtLK9Z4_Yp5CipcR0jLOjn0NEZvMMeM1yJWcYVhmNSzn_nZm-r9pI7rcNafrwE0unZZaUmhuUxWmrvt0BP_iqbOacxk1ChBPPR3f_K3FOhhRdX_gGbRE0lTEkmPfN46T5ctn4y_t9NM6JzIWj9QKh2sqtUsG8W1EYqz6w8FfH1bMji1OxhrzVldOocieNmiTh0blNtX9Sq-SebCjL458GW4SPIWycDHekamVKjg548ViBaCi8OPWkzq-uDtX4wTjuIit2zAYJ3LKxk5yFHE50qTRnGr3LmzwPVd-r1THg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوند و تعریف و تمجید از ترامپ
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66326" target="_blank">📅 00:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66325">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1190f45b0e.mp4?token=mN-K8KBjOJnlvKEK5kjHpQXNfpr326lDyy-VjKXa2miSeqJ5_AlXCcfvbstLpcWoqa0fP2dce0OEnvtN7yEzwquABH89l3Y1LO4cgmyjZOBs4B6o9HU8CeVu7b9rXL9CVYDdM_oXKtP0n5DSRgee-wCbwjVt4GEvcNd6YUwVp__NDkopbik6ZE1KcQL68QQO4WzDAkSVuLeLmjx4_h2AsO-VlhlroCEXjEmHWQTb9N8FyjcpwrS9EREqImpu4ZB4Ygro5AitNKvT2DmskzElMIk2Eb6SYvuMzmaz4s-nWvTCChqm8rt1hDxFKVgHLMalcrwhoRf6wk8fIFObYsH2HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1190f45b0e.mp4?token=mN-K8KBjOJnlvKEK5kjHpQXNfpr326lDyy-VjKXa2miSeqJ5_AlXCcfvbstLpcWoqa0fP2dce0OEnvtN7yEzwquABH89l3Y1LO4cgmyjZOBs4B6o9HU8CeVu7b9rXL9CVYDdM_oXKtP0n5DSRgee-wCbwjVt4GEvcNd6YUwVp__NDkopbik6ZE1KcQL68QQO4WzDAkSVuLeLmjx4_h2AsO-VlhlroCEXjEmHWQTb9N8FyjcpwrS9EREqImpu4ZB4Ygro5AitNKvT2DmskzElMIk2Eb6SYvuMzmaz4s-nWvTCChqm8rt1hDxFKVgHLMalcrwhoRf6wk8fIFObYsH2HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان بازیکن تیم جمهوری اسلامی به خبرنگار خارجی:
مسائل داخلی ایران به شما ربطی ندارد؛ مسائل خارج از فوتبال، بین خود ماست و خودمان آن را حل خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66325" target="_blank">📅 23:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66324">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcce5ba4b.mp4?token=PfQ5T9rqMoOld9OViIVjjT4IZOgXCswiED8dz8vhbO2HR0TPve_XE04zta31IiyT7MrYTQGk7yl7ruQQDEh8DmWYedqn1KtBFxYPT_yYzDVAzNwbNg906PPfsG74n1ChNWGVFQivk3RNmdfjJP795EciacJYM2B8Z2YIxBBDfABNNhOPs5oNA4rqDV0HExtN8s6nWWal5nWjAV-xqiDhoyYVNKj7KWkYTOKlHRhHppHBbIiULEiPe-IzfqyJUwvxWSQN6O0KrzwIDBHQQiUPrXoU0YVf8BUAjgkC4iNDdjtGJRVAl7JBW4X7F9LIkLZec6Lf494sDClkihPdSGvr_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcce5ba4b.mp4?token=PfQ5T9rqMoOld9OViIVjjT4IZOgXCswiED8dz8vhbO2HR0TPve_XE04zta31IiyT7MrYTQGk7yl7ruQQDEh8DmWYedqn1KtBFxYPT_yYzDVAzNwbNg906PPfsG74n1ChNWGVFQivk3RNmdfjJP795EciacJYM2B8Z2YIxBBDfABNNhOPs5oNA4rqDV0HExtN8s6nWWal5nWjAV-xqiDhoyYVNKj7KWkYTOKlHRhHppHBbIiULEiPe-IzfqyJUwvxWSQN6O0KrzwIDBHQQiUPrXoU0YVf8BUAjgkC4iNDdjtGJRVAl7JBW4X7F9LIkLZec6Lf494sDClkihPdSGvr_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرزیدنت پزشکیان:
مشکلات خودتون رو خودتون حل کنید، من سیاستمدار نیستم من دکترم، برا سلامت مردم اومدم
😔
.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66324" target="_blank">📅 23:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66323">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ab7bce46.mp4?token=eedHCo01_Evqx5hizymjkal3gVo3twRcd6JUEt8My8fJ_7l4DVWm-Nj4Wh22O7eTgvu2KwJo9s5JW_OSQYKKhY3lXVkN5HDMmOilfSUDWarUSqunuYDVfmdYCt3sOST13VCtV4BZg-Edys6hCRCShBx-iwcrYGA5clp2RkMNUic0vrPW1dqBpAZmRkX8CbcQmpI5Xon9YPGU1mx6k3YMa3_IiKGEwrjtmIqnZqhTIr9Vfgiir5rxQvquPj5UbQQfTInsASu5wxQTjeMJa5FH1V2JAdBTM115hGV0eos0ty8IBOIbsv_rZT96QHP9liFBj79T5nCHlLTR8yEVS68QhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ab7bce46.mp4?token=eedHCo01_Evqx5hizymjkal3gVo3twRcd6JUEt8My8fJ_7l4DVWm-Nj4Wh22O7eTgvu2KwJo9s5JW_OSQYKKhY3lXVkN5HDMmOilfSUDWarUSqunuYDVfmdYCt3sOST13VCtV4BZg-Edys6hCRCShBx-iwcrYGA5clp2RkMNUic0vrPW1dqBpAZmRkX8CbcQmpI5Xon9YPGU1mx6k3YMa3_IiKGEwrjtmIqnZqhTIr9Vfgiir5rxQvquPj5UbQQfTInsASu5wxQTjeMJa5FH1V2JAdBTM115hGV0eos0ty8IBOIbsv_rZT96QHP9liFBj79T5nCHlLTR8yEVS68QhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرزشی:
چرا با کسی که به رهبر عزیزمون اتهام جنسی میزنه مذاکره میکنید
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66323" target="_blank">📅 22:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66322">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
ارتش اسرائیل، طی دو روز گذشته پس از اعلام پایان جنگ از سوی ترامپ، «۸۴ بار آتش‌بس در جنوب لبنان را نقض کرده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66322" target="_blank">📅 22:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66321">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
#فورییی
؛قرارگاه مرکزی خاتم الانبیاء:
اگر ارتش رژیم صهیونیستی حملات خود را در جنوب لبنان متوقف نکند، باید منتظر پاسخ سختی از سوی ما باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66321" target="_blank">📅 22:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66320">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e376d329d7.mp4?token=lcmk2ciSB4_wn7terkBf0tfJwEtCSR_YcVjcV3J0FNVzzVZKS3FLL1Bt_naQZ05k7DXwOaal3rv_nohS2GJjQLwmPMTjlnvtTMMPN87JV-eI9hZAMy0D5OdTDaMKxGolIDcQc_OPATydL8-Q0GALLdMMnV5f8L8GGNb-0nfv-cJc6v3DeitexcHQ56IU3SxTVHv8S1ddz9NhrZw0fD4D4TOADCASjzo0PpUQBUH7_b-shdfwdIRzYi5XOLq-vROunbBPhHyZFcGjHLD5tw9OQ0_lvfWkqogyvY_W5zWkozVyVhM_s5hR4iGVurkGrXb7cJLILuOAzwA8NnXwFKrWsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e376d329d7.mp4?token=lcmk2ciSB4_wn7terkBf0tfJwEtCSR_YcVjcV3J0FNVzzVZKS3FLL1Bt_naQZ05k7DXwOaal3rv_nohS2GJjQLwmPMTjlnvtTMMPN87JV-eI9hZAMy0D5OdTDaMKxGolIDcQc_OPATydL8-Q0GALLdMMnV5f8L8GGNb-0nfv-cJc6v3DeitexcHQ56IU3SxTVHv8S1ddz9NhrZw0fD4D4TOADCASjzo0PpUQBUH7_b-shdfwdIRzYi5XOLq-vROunbBPhHyZFcGjHLD5tw9OQ0_lvfWkqogyvY_W5zWkozVyVhM_s5hR4iGVurkGrXb7cJLILuOAzwA8NnXwFKrWsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنوز سواله برام؛چرا خارج شد؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66320" target="_blank">📅 22:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66319">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUnZvHqLex3OsEzFq3uqVkGTQ3Y47oNabE926BKr4XFV5Z5UJZKo7UIL7kca-mFU0U426r-719nd0ozBJQ7bBg-8g3KanyNuyFoNNOXMo-HIwH7ZTRTbi_eQULoI9Tz1A8eZBE8oTrfmuMsfhz85nuNraooC9yyH9zPZj4LhrhxhAX13vZXQHWI2Jf-5x5YnYLHUyOvJRRRkobty6mr-l9Lzi4BhsA4RFiB1icLbDvAL0h6vfa44EZQjOxn0Zixrnu46AT6OWYfD5E3f05aQZdy1_I0p0Q55ot98wZ0487PEr4VgUQ9FZwSug1d9WgM_fS9iGKmesCqJ5FtZt3ubFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نفتالی بنت یکی از نامزد های نخست وزیری اسرائیل در انتخابات آینده:
توافق فعلی بین رژیم جمهوری اسلامی و آمریکا فقط یک توافق موقت است.به ملت شریف ایران می‌گویم که امیدتان را از دست ندهید، جمهوری اسلامی رژیم فاسدی است که سقوط خواهد کرد. نوبت بعد که مردم ایران قیام کنند ما ابزارهای لازم را در اختیارشان قرار می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66319" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66318">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/837293596a.mp4?token=N74ucms-Vbn5QGya8AsEME6yLP6psoi1r3QygyhrX5r7Xv_CChK1X9sLi9lq58bkZPWxAwdgRRjlhql8LITiUGPiqnitXBbtUwSPy1WIlzGSPuOJSe_a1bRK0pqB6uH9z3kcB51MN4liJOFbitOvzFcp_IB2Ha2Xgbo2RIzRwyH4V5RHF7sl2Zkawkd2buY_dMUrBRmTpzCA8-daQNzMKFzyub-xDBe-0dvrDlTrOcBPV1rHQ7d7rh2SThA-Vwrx878StGaHZveYukmKe9bIrT74S0EUjSqVMhwLvqgzHja2q2WQ5ibAlwK8cIeRGZvXZNk7FdURz7CWWe9QzrtRyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/837293596a.mp4?token=N74ucms-Vbn5QGya8AsEME6yLP6psoi1r3QygyhrX5r7Xv_CChK1X9sLi9lq58bkZPWxAwdgRRjlhql8LITiUGPiqnitXBbtUwSPy1WIlzGSPuOJSe_a1bRK0pqB6uH9z3kcB51MN4liJOFbitOvzFcp_IB2Ha2Xgbo2RIzRwyH4V5RHF7sl2Zkawkd2buY_dMUrBRmTpzCA8-daQNzMKFzyub-xDBe-0dvrDlTrOcBPV1rHQ7d7rh2SThA-Vwrx878StGaHZveYukmKe9bIrT74S0EUjSqVMhwLvqgzHja2q2WQ5ibAlwK8cIeRGZvXZNk7FdURz7CWWe9QzrtRyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی ونس:
اگر مردم ایران خواهان رفاه بیشتر هستند، رهبرانشان باید پیشقدم شوند و رفتار خود را تغییر دهند اگر این کار را انجام دهند، عالی است. اگر ندهند، ایالات متحده قبلاً چیزهای زیادی به دست آورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66318" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66317">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحامیان جبهه اصلاحات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMHTwvGauQlvqmS2JROyT3KRPuC7V5dOKsYOgMneceIC_COmGhEl_hkU25ruQZLmDE_O7ZUhoxDk4pFR2X-l_-7Faj8mx1vzVRlqw4AGl2kD55Rd6dWVdjvF1Ru_9Oo-Y-wIy7sky6VPgQvB2eIFDIOsEK4o6-1BJsi8lHqknwV11r5EHbKVi3KTDCN6nD9hjrSZYowQB4ZCRhAOahIrvubT7olswhMZkOBGxB3Re14CeMZdIABebT3XXHXSlOq585zGjVknfVRygAuKpzbcXAJt9ZjuW6PkSHtdLXoJzqQwFMdWpQfaza472_Hn_LfJcKqPbMCriX2cwQ34OxDBvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون شرح!
@iranwprldnews</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66317" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66313">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bphyunhu6qs9wqLohRyPFnj4HUqUp_Sqld4gNFIqUMX0bXC5JVSvErLkWQyflN3KSlVBr5mIIS0P4JofAoOlM76YEob2pp5xKjmIz6-ng-XJnciiQwO48nwTTxoccWAKdegml00mshxihz7cr8QeCG2bYODIRaicHykFQZssFh89As8HOreNXmbhe4HNHQADoIyORaJDa5H3nWpL4E1kFOHQiSooeRzebXMUNAejvXp9-SyAFtDjBXwuXyaa7sJMPXM0GtN2ZPCee_6V9p7-xJu76jQOwZDzCqi7yKEbMeYmiy4HTcbdPtqOMlTXVnkE_WI__a2fvfsfOSMasRIiKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
زیر نویس شبکه خبر:
حمله پهبادی اسرائیل به دو روستا در نبطیه در جنوب لبنان ۴کشته و تعدادی زخمی برجا گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66313" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66312">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9Y4oaiyMjXIaVQgchuwCTdPHiYFkFOWPthXbQ-1LHSB3H_sk161u9wPtYeouh_z8VsG7B9R83ggVJfuSkfdjJd8O00Fuy-anZECDQOMP2Nua3fc5fDjliVeK6mfzU6Dl2dN-pzrWTQjfR7Gmo1hNlXU9kq-joi3SZ0cIo2wdqmGJJvCFq9vKsBXVL8gjp3RwCJURpu76AKC5F572sOxMWZdCqkKOTKGQt0HZqlDhzk3x-4cT0ntrRt3dddwQBlZrRYWOtpKu5BFZP09nkDpjAOA3djBYD2Jn_6wz1VaSEiTpj5flKV7omSFYlM7UmlWAsZKlng2zTATmkCvTMDWYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل:
لانچری که به سمتمون موشک شلیک کرد رو هدف قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66312" target="_blank">📅 20:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66311">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c47f7533b.mp4?token=f7385ysPiZEwGoEq5-BhvdKicJ4NcTQXnknhf2UvrtYtc-fQzNFN0KkcOBRlJTNQYoFc5paWMO218iGDM5BzwoFdNpmuWflWzNTfQgSkt1M4UeXFcrMLgQbOvVco_FZa8VSODpkIISnB6ya5ctpFshKx7TF42B1-8t7WcxElojqTH6JlqzRmc3E-nmlLeeYBgVCvvds6xJUxpiHQEQNhsHMAWMrkfiBaiOx81j7tXijDlSS8rLbjTMHO8SBIEZL87It1lYJLU83I3jEZ5LGeLVrNiLXwTPiPwORFcJ66MaNjrcvikrPtj6DQ1cDXG7tFxmfCcwEse2evayB7Wug_6o66cgsyeFPnm9OmHjXlJ5PPkCw0K14KbpwFv8blqvX6tAVDANT5SLjYsZ546XjtcOj15KwuLFKGhPX2-RIVkqHS1tVJ0U9vLYJKXPsz1zXt3w5-OfV7Rh1y_hQq2AMksei5Op2zSx3liHkQ6eaeGgjSvis-mpCgTVX0ImYDJih9hP1K8z71mHvK3UPrqR1f_GfT-J9uafMu1NuojkNLrn0pMXXOip7d2AVWVas1BjCLQhCziRwqeY1lf1AOgDNlRMbSvAoqhqy1w0yEcfdnLSrirm48w9bLgbHbN-1UgmV23XJoS07cOvRGYRNK4EUMNcYomNs1AL4EhfM9Zipq2Mc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c47f7533b.mp4?token=f7385ysPiZEwGoEq5-BhvdKicJ4NcTQXnknhf2UvrtYtc-fQzNFN0KkcOBRlJTNQYoFc5paWMO218iGDM5BzwoFdNpmuWflWzNTfQgSkt1M4UeXFcrMLgQbOvVco_FZa8VSODpkIISnB6ya5ctpFshKx7TF42B1-8t7WcxElojqTH6JlqzRmc3E-nmlLeeYBgVCvvds6xJUxpiHQEQNhsHMAWMrkfiBaiOx81j7tXijDlSS8rLbjTMHO8SBIEZL87It1lYJLU83I3jEZ5LGeLVrNiLXwTPiPwORFcJ66MaNjrcvikrPtj6DQ1cDXG7tFxmfCcwEse2evayB7Wug_6o66cgsyeFPnm9OmHjXlJ5PPkCw0K14KbpwFv8blqvX6tAVDANT5SLjYsZ546XjtcOj15KwuLFKGhPX2-RIVkqHS1tVJ0U9vLYJKXPsz1zXt3w5-OfV7Rh1y_hQq2AMksei5Op2zSx3liHkQ6eaeGgjSvis-mpCgTVX0ImYDJih9hP1K8z71mHvK3UPrqR1f_GfT-J9uafMu1NuojkNLrn0pMXXOip7d2AVWVas1BjCLQhCziRwqeY1lf1AOgDNlRMbSvAoqhqy1w0yEcfdnLSrirm48w9bLgbHbN-1UgmV23XJoS07cOvRGYRNK4EUMNcYomNs1AL4EhfM9Zipq2Mc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه ای که سپاه داره لانچرو برا شلیک موشک آماده میکنه و ایشون هم شروع میکنه به فیلم گرفتن.
واکنش سپاه:
😡
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66311" target="_blank">📅 19:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66310">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66310" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66310" target="_blank">📅 19:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66309">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvqxL6eSSSvlge8gyhCXY6IDKlDsG_Nz99ITo44_h0R3WiJFeen8XpXrUrv9bHzST5gH2HjEw2MDvfxweyFB-Bv-5WaosYuOSqlz6kp75l5jhnBbT_2gC6aCvMpg8L6-CUyrSNJkl4Pitq_DIN5ximinUbVA5pcn6RKKsfo-hVgm9-GJJLSwmsbE5fsdrDrggMwkyy7HyqUwVn1rXHZMvTBWXRK40LL1vC1m-ho6UvXlnmr03t_myitvO5Ycrg5CQWTaz63y68afCo7gQ7w9epEoIu8HQrYxIrm_-dkQyTGif92c0I6Ot0mw_Kb3uJ5ABwmviaNeJ8thlLWMX0faVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66309" target="_blank">📅 19:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66308">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7SwHpoBSlc9Cso5gqwXpjLxpvgCcv_Tr5jiDUplGGP_nU7FI3KYy-KAc95jba4SvjZx-GKcBJF1vprlgMER3DIGPcMuowKBRC6Ppujn_50sBFSim6POlUPEsYYcu9CYN5uoPgI6V3R5Lo29brLiezIvndq-N9XW42ctH4I6hv2mCAQuuMN2zf_-slPZe7fsS2R_D5Ty1dNyh6kP39l8XIQkBWd20eh1f0z7xclAeLn9KQgAyvr7t_tFNkml0BKu8e5NjZ0mhDfynMCnJSs2yoeN9zM5iGq3wGxQ5gi5qdcBC7XGFUatWGls8357iB1-9g7p2nlcZzRC8ObrGRUslA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فاکس نیوز:
اف‌بی‌آی یک توطئه تروریستی گسترده و چند مرحله‌ای را که قصد داشت رویداد UFC Freedom 250 روز یکشنبه را در چمن جنوبی کاخ سفید هدف قرار دهد، خنثی کرد.
به گفته مقامات فدرال، این نقشه وحشتناک برای "ایجاد حداکثر تلفات" طراحی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66308" target="_blank">📅 19:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66307">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8fUruDD4skVyzeGV50Edx_zYTOesb_-AtI2FerqWZtMA0Yswc2g_fj0e7oBvuCGFgKfZyPIlk7cl542B7F0mg5Lqw3a1iaaWbUCS5pcGQ7Eo1v-ThdQkATiDHzA5z4OzCLaxX5Y41UOAHxXJZ5oK3zO0jbXTRgn2DXdzD7u3loMvRCAskd-mQLm5-9u9t4m7AyV67sszFGpwCwFlR6bNrvrCs7GsAaPaH9GbDP5X8ID_c-jwtihBLGcZ_12HEzxitu7dfi-U2xl0SyE8QL0G6O321GoVNBS3NnDyuyJ7l2G8k5rK1_AdDeb81Z8kBVp6EcaYqlQG3whDCKVbqUb0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارتش اسرائیل، منطقه میفدون در جنوب لبنان را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66307" target="_blank">📅 18:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66306">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc0108dd2.mp4?token=fsrSCRJ1l6eVYOjf3VV2MSIUcoSvEkk9_CMUWuqIISRqRT-KXxdoxaKQb3h4URxB8zq75dbw55L3OKLni6q02HqP6-GySasQcXsOzC4mLb3-t-TH9vU9dtfWekxFMjYbM2cvByiqhwGHeJixwLqTp8WeKaZefHeRxGanTi2Ou9YNzrmPatVs9pO4L_xH3l1oVZ9vaWg1gKGKFptJ8KV6uCHBi7N4diD_4uv-91AZIJ8YmVJrjFS7N397JpyEHDTWbJyQj6aFH_vmGKk5NP_I24KE3SX75eVZX01b1uggFAcrs15FP6dHxI8Ko04UlwkO7i871HabLmNG7p-a_CNtmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc0108dd2.mp4?token=fsrSCRJ1l6eVYOjf3VV2MSIUcoSvEkk9_CMUWuqIISRqRT-KXxdoxaKQb3h4URxB8zq75dbw55L3OKLni6q02HqP6-GySasQcXsOzC4mLb3-t-TH9vU9dtfWekxFMjYbM2cvByiqhwGHeJixwLqTp8WeKaZefHeRxGanTi2Ou9YNzrmPatVs9pO4L_xH3l1oVZ9vaWg1gKGKFptJ8KV6uCHBi7N4diD_4uv-91AZIJ8YmVJrjFS7N397JpyEHDTWbJyQj6aFH_vmGKk5NP_I24KE3SX75eVZX01b1uggFAcrs15FP6dHxI8Ko04UlwkO7i871HabLmNG7p-a_CNtmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
ممکن است شخصاً یک کنفرانس خبری برگزار کنم و متن یادداشت تفاهم میان آمریکا و جمهوری اسلامی را با صدای بلند بخوانم تا رسانه‌ها آن را به درستی پوشش دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66306" target="_blank">📅 18:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66305">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPC4iunEkMK-XOWsl6gN1Y_HZlU-jegL_tlKbvv5nD7Gbdovf3QHWOoZWhyyphXB_8YRfP6l1OsReQQhf4xGuuxGPdI2B_9rUfmb7XqbvrdppxU-hvypHKN_Ka01iSfFxMwQnS0HLDHPtI97Z3s3PO3cdPpoK3CXbx2M5ptvVGaxpZ8auvd1WUeC2RkFQdy0SDm1Uz_Im41dZKJFi4H8GpFQ9MjJyVPPmLCNckwFqw5XF_Hnisd-M0Wg-thQp5AxU45Jy_F1ER6LZXJRQXGK_1VZsSTOjpvsqBZ_Hy3ms8IgKY8IflHKokJPInrYpyFq2Q8Db9FweB1yqBnSyUVCvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام جهانی رو پیش‌بینی کن و جایزه ببر
🏆
با ربات تلگرامی «نتیجه‌باز» می‌تونین بازی‌های جام جهانی رو پیش‌بینی کنین و جوایز نقدی برنده شین.
😎
۶۰میلیون تومان جایزه برای نفرات برتر
⚽️
تازه امکان دعوت دوستاتون رو هم دارین و به کسی که بیشترین دعوت رو داشته باشه هم یه جایزه ۱۰میلیون تومنی تعلق میگیره.
فرصت رو از دست ندین و همین حالا از طریق لینک زیر وارد ربات شین:
@NatijehBaz_bot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66305" target="_blank">📅 18:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66304">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKYGzywY9qSaxYsZHuEwvRVntO2pYbJH7mNpYdHxLMUSyebzf2GOy-xdCRAjoULv9u0MK4jY5udVtJG7DViQzd9E3L5kKRnBxX6Dpd1chQ7yDAybzlGbhWlTO4eiO9qfYw1FznAxD_CyD7Gnxj_0GHBLc2Iy5i21Uqn6he1vRWaafhZoo_ggoxIq_g9uHnjNXWFYwD4V_uYOzsvMp2L44_a6-gvwzC6LynHYI5wJ9kqEmm0wxuqfWqC4gDC-tiCgkEbOXeUKrdRrbCqQqMZQDhEHZ2cjQ8FEYpJabbZEGVIe9YKeQ9OUOLS_Xq5H2jmH_sg8HUdE9j_fMoGFNeISUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزارت امور خارجه سوئیس:
قرار است یادداشت تفاهم ایران و آمریکا روز جمعه در بورگنشتوک، در مرکز این کشور، امضا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66304" target="_blank">📅 17:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66303">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehzpRAd9H1vcQ4O5yQAKyp8AV4yju7SHYnwzTjY2pS8wSUYDgw2jPpapnQtuLdqYr-zP5KK2oFkkJguKcSHEXcsTIJCEGzmokgwByXMDy2NGAdlG7_0LfT9Hslu74MLM_PK1VbXs_1T0u7qlZvYM3q4_pKIHRhZ9yxlZtzgh1bkIyrfnhQYJPYtzqM35oZNdRgBtwQXPFeDvXKjQdR2WPnEA1i1ToYscG_uYnVgzQf8KyDheedtemOE_5K_cUNy7Hi2tBBOkADR-F8r5nvjuBORmCreoqrzxfKXhDj5eZECeEtEgDyH5ri9YQSSbRK6KfpTFvtQtuwnAP3o-CekT_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر تیم جمهوری اسلامی که آمریکا و اسرائیل ویزای جهنمشون رو اوکی کرد.
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66303" target="_blank">📅 17:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66302">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66302" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66302" target="_blank">📅 17:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66301">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S84J3zeMi_YcutgYEeTzR9mNrib3oQZVUaV0MOFH0B_ewp7VjiaqWBAhXDKcaRxpz5rRr_EFvlg5_ZXdSpuW4bbJ7y-toB1ewNlABX6JR88_HMxO7LYkKPQsaiP9Pt_fyzP4jIRY7R-9XfInrnSMkSavDxDP5VQaSbZMN1d_SIlKt-DPK0X2mLOtxxteqB1d0tPWVJZeXKP51iF4uLluF4Ccj3vkM4H3OF4iHOiZNzIESlxMPWqYFfBQZojAz6W9T4Olv840yq78zn7ABL79WY-MYcHkOYHP9mZVaD_MkJI6yHGnEG3UoKnjK2CULHqFbRoPK82IwB2rBKsJnnPpuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66301" target="_blank">📅 17:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66300">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d1538e700.mp4?token=kqH1a-C2PIRy85fr1ojBDj4PtfOzy94hFLW5uD0MIja4wF7cKH1HKSiZgv5XuA9RMDcLXVCDzQOsFF7_aXkUauKIt4QnI33CbBFUNi5JUdRlvtxJzuaergoFfiTjT5zIvGCLparj-rk4h5jK2hnwo8K7sykf40tSPfjXYitnYjxhqvB3kfsY0VEXWhzLylsWFf8NH1cXq7gNW8faj5g7BO0zCnGrzzwEuRMllkAzSkBhaVjU4uFkz2Whv52SabeWGcFNzNGYjmZZ-sRkYYgOU1Xl98WSxUllTs8qoPedFx_L9-8SnKH2jemZWAmHlqydA-gNB-agxxUd4RUAIP5VfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d1538e700.mp4?token=kqH1a-C2PIRy85fr1ojBDj4PtfOzy94hFLW5uD0MIja4wF7cKH1HKSiZgv5XuA9RMDcLXVCDzQOsFF7_aXkUauKIt4QnI33CbBFUNi5JUdRlvtxJzuaergoFfiTjT5zIvGCLparj-rk4h5jK2hnwo8K7sykf40tSPfjXYitnYjxhqvB3kfsY0VEXWhzLylsWFf8NH1cXq7gNW8faj5g7BO0zCnGrzzwEuRMllkAzSkBhaVjU4uFkz2Whv52SabeWGcFNzNGYjmZZ-sRkYYgOU1Xl98WSxUllTs8qoPedFx_L9-8SnKH2jemZWAmHlqydA-gNB-agxxUd4RUAIP5VfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگام بمباران بیت رهبری هرکسی که اونجا بوده کشته شده جز مجتبی.
مجتبی همون لحظه:
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66300" target="_blank">📅 17:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66296">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_R96SVowEo_Qrtgi1WV-N_OrofqhctO4bRPaNs9F1QtwyXPwc2GsemtnctWvzQOLiMpi44u7GewyUm5pa8BiXnnp_4jWgNlHdv-Z036maqIMCY4J3dIwHm37qcrdkcBlKjeosK98_MB5lc1P_7-Mzf7wlHlBUNAnF_4oBUU-iT1_j6KTCu4ywULP-24xD-MYKXjt6SsEd6wfZ5jW2L1_UgpkG3lF4jVM0uH0fLL2p-rXjH2tusAOAE-MmrURMjB2eempBo7HQq5G-HqspHcxVMJ-ComsFloDC6HHZCk1efB-IGgNrjeodH4QSn9qmttLnYvPrZqKeaf5UYvEYBfOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TxYhek32LuzjOVTsrgGIOAOTBucu6as_bMr8gDenQ2PFcglQD1gj1tEZ5K-kKnM3dG824AqeP041zK6OSF6h2a7ZRz874USewEc754M3PqRLYDCnP6P3gXKkdb92JqTZ2H82PTOE9MGLKsT2xEQ3gQs_AYkGjBvcr8wjkZJP6cpS6WwsLH3lB1cFyLBunB_REwgptx7qnip77vespE-S48oRndl1w5v45YUosn9lKDORqqggRj2zxaJesnS8gxlBG3_gBhk4COHHSpGRXKqFqZLQ28HyTB_BNmIuVIaTylKc2M0k8doBc7Z2NTgFh8atNfx2pJEzB3El0j-1IMyxDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FWfdscINAV7oDOHt6prz4tggSeOeVk2ezikNnYH9oGDnS3D-YDr8wYzd_omkfb0GoljSUN91P2ml5VopVHh9MokuyDjhVPMPRNoigYc0qJgmdh4dWu0z0zjhtwzqbGBrSjJG1XOTFIf35Qt2fohhBy9MdTuy7m66rtb_HWsfALmVe-4DPLDea32IDN5qfRnpG_dYVZ1ir_3QRHr5gRn1FOqDWPqqlkG2ha9lAPNkNBgYv1BFWWOrb-8WFhFxSUFB369jtM81YQtZmG2199jzk1Gxg86XIBGX4F12zGWPUqFoQyJTEZUqI4A5g_G5mCMAuRyoRxsLWVvDy660FDLqSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hsmEHCExZLsXGLDrE0khscKMLpGasy69wRUZDq7LL5dTsN3GlvUyBzdf3Q_Ok-HcD2_KG2zG13E_AHMxJd_r6zen5D0itHEYje8_6glw5FdjlSaB23I7pZzCDN7Q1cpO0voTL8XLSvyaP3AdkSleFwM3wWycDWRI3A8G4TgLsU7kp9VlKyCUf09G-QjXl99eDP6l2H_0ZPUWc5i92hR2hCckiveUMPLasB230Hyr5stBAGfMAqUFWFxJof3auTpvf2zasjoz-NSncI_g74JwZnNo5agRF_IRBHimOWy8yFX6XOfqi4F3kspzG3hOOJa1IrEfeaZBaPm6md66AQJfkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ویتنی رایت پورن استار مشهور آمریکایی دیشب در استادیوم حضور داشته و از تیم جمهوری اسلامی حمایت کرده
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66296" target="_blank">📅 16:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66295">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c34b0ffff.mp4?token=fqQJ9Qhwz1B36yn5dzqLjStdLHzro4DfImDhtLUnPKQsFWYPDUbpjZ0xzlwOqq52DZI1g13vi1m-VrMsikouahvb5Buv0lqQwl_UVHG1lT4PJW4ssjaBvfywBL4FZg3h-YISj3bXaWLfftrOXvcSGfY-aSpq4Wwa-G-8S1nyeSi3uOMB07e5Vw7uxXSsLVGJwXwM7Ni0pwyNBEOP1d8aYKhBFtTykmz048iGZ75TmLHUUNCVke3ytJed7viwCF5oCBc2Kcc2HHWdRmfrGvXq_2TFcZzL31kisnT4REE2S3y8A9iWgUdIqGoORlDqFCJ1m4lQY1hmbAdF7w4ErMN45g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c34b0ffff.mp4?token=fqQJ9Qhwz1B36yn5dzqLjStdLHzro4DfImDhtLUnPKQsFWYPDUbpjZ0xzlwOqq52DZI1g13vi1m-VrMsikouahvb5Buv0lqQwl_UVHG1lT4PJW4ssjaBvfywBL4FZg3h-YISj3bXaWLfftrOXvcSGfY-aSpq4Wwa-G-8S1nyeSi3uOMB07e5Vw7uxXSsLVGJwXwM7Ni0pwyNBEOP1d8aYKhBFtTykmz048iGZ75TmLHUUNCVke3ytJed7viwCF5oCBc2Kcc2HHWdRmfrGvXq_2TFcZzL31kisnT4REE2S3y8A9iWgUdIqGoORlDqFCJ1m4lQY1hmbAdF7w4ErMN45g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استادیوم فوق‌العاده زیبای مرسدس بنز در شهر آتلانتا در آمریکا میزبان بازی های جام جهانی
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66295" target="_blank">📅 16:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66294">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">واقعا حق اسپانیا تو بازی اول خورده شد باید ۱۶ تا به کیپ ورد میزدن   @sammfoott</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66294" target="_blank">📅 15:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66293">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUv1UMOJLkxN40PIM49jeYejAKIgQJn_mGPyAMtPLUGRwOOlOmCDufO2nx7HHrfWhb-r_FuO_aW9frE8fEliVj9a6Aztz2v5gUYjkbJSKELFwACI_LEQayRUKatB26HAAhvSFT4vkA7O3bn46gFpIxckYU7ebthGUgfTQ10lNWtfvuOqcS9uJaDgKiIn3L-rDU3_ZY1NWMsEoBwBY-MaMGqkBc5YRSjXoO9_bq2OuLgR-4iXzL9chDwsGsgwPR4bNxDu0UFCqaftQNyKxQRsZqU3m4y12jZKAP8lW-D6ucueiuacA0Y0wrpiudQnM4eCdM8-BnBDI7QQxfuCc7Uvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
جمهوری اسلامی هم‌زمان با امضای تفاهم‌نامه‌ «صلح»، دو تن دیگر از معترضان ۱۸ و ۱۹ دی‌ به نام‌های جواد زمانی و ابوالفضل ساعدی را اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66293" target="_blank">📅 15:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66292">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52f8c1feb4.mp4?token=F-jtQJsV_cxwau_f9CLqAMjxR0KVI9wi0bKFdB3x_0yO1ekavY7Qt0vJdpOzDrtaQQAe70HnBCJNlWMyI3nRzy4uCzUirFcAS-xEW3XMjBK_ChHahAeVUYNo92pzKkqBxRHHLlwfsefD6JGctlozI9U99LkcJ1CfaPidzaQ3A7DQldnppozav2vLMI-vpLosnF1niMa-IZkl3slRNX4CI4FX8Ir2AiQZkii_Ss8egcoiueP_cd5Gd-zgYc0WeWvBXWcAiz8_0nIZBQW1tv-Yp2oYtxnoI0xKD6bxMy1Oi1GwXGtHE8CMXWUyKgfoqjgu4S6DxjTVTuSrW9tI20gZjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52f8c1feb4.mp4?token=F-jtQJsV_cxwau_f9CLqAMjxR0KVI9wi0bKFdB3x_0yO1ekavY7Qt0vJdpOzDrtaQQAe70HnBCJNlWMyI3nRzy4uCzUirFcAS-xEW3XMjBK_ChHahAeVUYNo92pzKkqBxRHHLlwfsefD6JGctlozI9U99LkcJ1CfaPidzaQ3A7DQldnppozav2vLMI-vpLosnF1niMa-IZkl3slRNX4CI4FX8Ir2AiQZkii_Ss8egcoiueP_cd5Gd-zgYc0WeWvBXWcAiz8_0nIZBQW1tv-Yp2oYtxnoI0xKD6bxMy1Oi1GwXGtHE8CMXWUyKgfoqjgu4S6DxjTVTuSrW9tI20gZjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
انتقاد ترامپ از روشی که اسرائیل در لبنان به کار گرفته است:
لازم نیست هر بار که دنبال کسی می‌گردید، یک آپارتمان را خراب کنید.افراد زیادی در آن خانه‌ها هستند و می‌توانم به شما بگویم که همه آنها حزب‌الله نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66292" target="_blank">📅 14:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66291">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db26cc81b.mp4?token=hQXMDjVrO8qc2kX1zEcHGuDmPWw5OGgyAuUD6WJNlZNck_6AGg9TLTmkge8F0AS8BLnJLdHnxrxw6EmUQhRyHNoPiy3WbyEcbTfKa6V-gF8kpjsQXzOc3UsPNHgFwUVtFMAnkb33drTXam6a6RDs8HMRKrDU_OwuQslVByXEZAlLKJY8QreT4kNSwn_3tysf1PGoXS0tsLKyTvEUCwGc4_4i0PpU1Sf5vbmk07BvctDrpfXCFVG-4UscC1tDciKmohbnM2EEMvR7OqfqStokLqYNVJsYMtDwJE-7TY9_6Isbdq34FqZfyiY4j9lNWLZgbzLMmcea_Q1Lzn1qGbKh6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db26cc81b.mp4?token=hQXMDjVrO8qc2kX1zEcHGuDmPWw5OGgyAuUD6WJNlZNck_6AGg9TLTmkge8F0AS8BLnJLdHnxrxw6EmUQhRyHNoPiy3WbyEcbTfKa6V-gF8kpjsQXzOc3UsPNHgFwUVtFMAnkb33drTXam6a6RDs8HMRKrDU_OwuQslVByXEZAlLKJY8QreT4kNSwn_3tysf1PGoXS0tsLKyTvEUCwGc4_4i0PpU1Sf5vbmk07BvctDrpfXCFVG-4UscC1tDciKmohbnM2EEMvR7OqfqStokLqYNVJsYMtDwJE-7TY9_6Isbdq34FqZfyiY4j9lNWLZgbzLMmcea_Q1Lzn1qGbKh6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
در توافق من، اگر ایران به سلاح هسته‌ای دست یابد، منفجر می‌شود.
در توافق اوباما، به آنها اجازه داده شد که سلاح هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66291" target="_blank">📅 14:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66290">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaeee1ba07.mp4?token=fdwEQsktvzuG1ccvBaL9t2o5Tp2_-gdsiBv2X0HlbRJp8CIhE-UpyJeCUqj2njHuAtUvJ46mqf3vwhsvsZ24jvAivlmsRulvojW2npBb6IHEZk2jsClEADduc383UStLIpLDxweXXT-Pi5TwYtYg7kV-iVXXLIaln8tkq6R5KDHqGQSpMwYiciA8DxznHl0KYTo3ChV-6Bvg13Sv4fRvgsLBMqgUuYH0sIDpvQEjbxDfYXbLDmx1L1JVzyRG8zsAa5vaphFKO9tjGXPci3N5qp9azmHZctBHct8_u6iHMF0UMiO0oBDaes4T5QEtnOhb2nDZgxzt3qJ5Mw-ib8GZLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaeee1ba07.mp4?token=fdwEQsktvzuG1ccvBaL9t2o5Tp2_-gdsiBv2X0HlbRJp8CIhE-UpyJeCUqj2njHuAtUvJ46mqf3vwhsvsZ24jvAivlmsRulvojW2npBb6IHEZk2jsClEADduc383UStLIpLDxweXXT-Pi5TwYtYg7kV-iVXXLIaln8tkq6R5KDHqGQSpMwYiciA8DxznHl0KYTo3ChV-6Bvg13Sv4fRvgsLBMqgUuYH0sIDpvQEjbxDfYXbLDmx1L1JVzyRG8zsAa5vaphFKO9tjGXPci3N5qp9azmHZctBHct8_u6iHMF0UMiO0oBDaes4T5QEtnOhb2nDZgxzt3qJ5Mw-ib8GZLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
گروه اول و دوم رهبران همگی مرده اند.
رهبری فعلی ایران افراد بسیار منطقی هستند. تعامل با آنها خوب است؛ آنها افرادی قوی و باهوش هستند.آنها رادیکال نشده‌اند و به دنبال کمک به کشورشان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66290" target="_blank">📅 14:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66289">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/059a9cad8e.mp4?token=jObXQJEW68DO3ApSEtUa7uET_b8LF398eO4mC4KC5k821_W0Y6ceSF4K5ulcdqccw-2riacln_eeO_yJwEn8naJES680w3aGQjwcI4MR6CZbrPkHPwAYAzZH3Vue0xi511_P37Q_c9QRm3ck1XltnRtc1OFf3jNqwiPHcta5QDcmJeWfASZ3xWACt2cj5HLLdQaxPPmwNVhq4qMV_uq1XCnN04Qz-mJhyXT7t19-GT5a5rjRjtfXSFIIse-f2OmYqADo_jaj8LymYu7KHnfrTC73P-1ZB0FqGY8VfROqMnztWUdfG0hWQx1fNqycWwFVfqcxRGLMrA57v7KkYQEfhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/059a9cad8e.mp4?token=jObXQJEW68DO3ApSEtUa7uET_b8LF398eO4mC4KC5k821_W0Y6ceSF4K5ulcdqccw-2riacln_eeO_yJwEn8naJES680w3aGQjwcI4MR6CZbrPkHPwAYAzZH3Vue0xi511_P37Q_c9QRm3ck1XltnRtc1OFf3jNqwiPHcta5QDcmJeWfASZ3xWACt2cj5HLLdQaxPPmwNVhq4qMV_uq1XCnN04Qz-mJhyXT7t19-GT5a5rjRjtfXSFIIse-f2OmYqADo_jaj8LymYu7KHnfrTC73P-1ZB0FqGY8VfROqMnztWUdfG0hWQx1fNqycWwFVfqcxRGLMrA57v7KkYQEfhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: رژیم ایران همچنان به کشتن مردم خود ادامه می‌دهد.
ترامپ: بیشتر این اتفاقات در دوران رژیم اول و دوم رخ داده است، خیلی بیشتر از الان.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66289" target="_blank">📅 14:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66288">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b6ac4ffe1.mp4?token=ue_tSrhWGsCRcddlMjry3HqliN5ZcCWiKxEIAua9D92D63XnNGCDvJOW9y5Qn6VlBwuivYAoeK8MeeYw1L68RFJaVtuzxM6_NkfZvBEZDmt2ax8lrInERWpif5aFpNHcp7pbCNjKd-pTJUXkFsG4VGtNy_EwY22FjI40xSKFmhRexwdW0FFibIGes6YN3IqSvYj1m0C0sv8VVFFpEPgG68DqKDvIeTrsSv1c3TpxQ1ahmK-VTjf_8k-aJuXzZqCx3DOca2UVkCPdgzYfcCwUp4yUq-s3qaAAEf9bgAuS1mqbDFWtwUC63MJ6j67PJeIqJnqGKk9w9LoCXPk4r2xpLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b6ac4ffe1.mp4?token=ue_tSrhWGsCRcddlMjry3HqliN5ZcCWiKxEIAua9D92D63XnNGCDvJOW9y5Qn6VlBwuivYAoeK8MeeYw1L68RFJaVtuzxM6_NkfZvBEZDmt2ax8lrInERWpif5aFpNHcp7pbCNjKd-pTJUXkFsG4VGtNy_EwY22FjI40xSKFmhRexwdW0FFibIGes6YN3IqSvYj1m0C0sv8VVFFpEPgG68DqKDvIeTrsSv1c3TpxQ1ahmK-VTjf_8k-aJuXzZqCx3DOca2UVkCPdgzYfcCwUp4yUq-s3qaAAEf9bgAuS1mqbDFWtwUC63MJ6j67PJeIqJnqGKk9w9LoCXPk4r2xpLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد گرد و غبار هسته‌ای:
شما می‌توانید این استدلال را مطرح کنید: چرا اصلاً خودتان را به زحمت می‌اندازید؟ چون واقعاً ارزشمند نیست.اما فکر می‌کنم از نظر روانی، ما می‌خواهیم آن را به دست آوریم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66288" target="_blank">📅 14:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66287">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77169efe09.mp4?token=E8GxFGZrTYzYLZVFgTRu5klaGlOcqzh1whGWyQqnh1akXbH1W0MgPix2qxH4EeOQv0ltaVGaS4FJ3oMg5U7teHiQHcUXqDq6m8qmSrUbQrZD1-WCVdHv7SPVhhdp8nihh4GsyyyneOzpBMQZD0TzyRWyZiKq-ttYUK_5k1shSVtjnoIcMhVDYGXwFcP8tZKVU8qyqV7dxdyqeSPH820rQW9CoUJm7WF7wC83JvDfnwHo-M5F1nihCGv_alB2FeUwk6oimS802iWYcNg8jLAt3tw7eQ8mDKI5lcWB939Ip-8bBt16fewbBhYWScdIyYy9tbSZALBfRztlIyVTw9BHag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77169efe09.mp4?token=E8GxFGZrTYzYLZVFgTRu5klaGlOcqzh1whGWyQqnh1akXbH1W0MgPix2qxH4EeOQv0ltaVGaS4FJ3oMg5U7teHiQHcUXqDq6m8qmSrUbQrZD1-WCVdHv7SPVhhdp8nihh4GsyyyneOzpBMQZD0TzyRWyZiKq-ttYUK_5k1shSVtjnoIcMhVDYGXwFcP8tZKVU8qyqV7dxdyqeSPH820rQW9CoUJm7WF7wC83JvDfnwHo-M5F1nihCGv_alB2FeUwk6oimS802iWYcNg8jLAt3tw7eQ8mDKI5lcWB939Ip-8bBt16fewbBhYWScdIyYy9tbSZALBfRztlIyVTw9BHag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
ایران حتی یک بار هم به ترکیه حمله کرد. من هرگز نفهمیدم. هیچ کس قرار نیست بفهمد.
مشکل این است. آنها افرادی کاملاً غیرمنطقی هستند و این افراد اکنون رفته‌اند.
من فکر می‌کنم ایران اکنون رهبری منطقی دارد
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66287" target="_blank">📅 14:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66286">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5225dce7ab.mp4?token=KCDW_qE9I_LEewKLInFtwl7VsJ8e9MJIFDo_fdJS0FHeTfMRE-2qi-eRa4fKcJI8GisyueP82SpJJ_4E3zXb54pEbRGM0BkxVkpL1Fvm8XeX5m8L5lr9MTLPCR5TnwbHYyNO0lg8WZT0iTpZtC8TiV0abjJXQfANv8DBocvzf5WxGaKbKDdzIBxIMCjD1hu8Zg1K0WQy9MaV0dSd5oCcfGjByKAG-p0SsHvxmHMVpr9LY34w1xyPzJcJwoEM5SNmAiQdhf59RXa1EamCewtzjUaVHVYzpvkqc2lgnzEqPp_ppqLGze1orolPBI5SRxMGwzPWpm7XF6WhstIP8JgwmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5225dce7ab.mp4?token=KCDW_qE9I_LEewKLInFtwl7VsJ8e9MJIFDo_fdJS0FHeTfMRE-2qi-eRa4fKcJI8GisyueP82SpJJ_4E3zXb54pEbRGM0BkxVkpL1Fvm8XeX5m8L5lr9MTLPCR5TnwbHYyNO0lg8WZT0iTpZtC8TiV0abjJXQfANv8DBocvzf5WxGaKbKDdzIBxIMCjD1hu8Zg1K0WQy9MaV0dSd5oCcfGjByKAG-p0SsHvxmHMVpr9LY34w1xyPzJcJwoEM5SNmAiQdhf59RXa1EamCewtzjUaVHVYzpvkqc2lgnzEqPp_ppqLGze1orolPBI5SRxMGwzPWpm7XF6WhstIP8JgwmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگن مجتبی تو LA رویت شده
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66286" target="_blank">📅 14:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66284">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fLZUClug91Uq7NqMx2etMYR5pZocgwZFPiouNj6ycCdXidrU9O1Kv4lFtqjycNrg8h24V3xOtj1uQPG59ugRMQzhFmCeYB-5ciChP9NciFhTU75gxS7aKVh6qYl4gziZtGmbZ1HRlrLJLWAlcx4QTxzCITcAo45N_OHQS8aVENVG2T2Qy9UpQgOJ-D9kE_xXFwZoavvN2qG_cQWtAyKFwA7ZfS-KUC122B9fLomx11UuZs-N16lcO82pavXBPbq2opKbYechJPbxjb5r14yX38z9rHu_7VYLFnMeKFIhnNu_xUA_hhCjHbFRTbT5N3A_bhFyl-dC3nplNY1NN9U-EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H0JFPaB0fdZeiyxfHx3C8nnKNuv9EB4YDiyn0L5skc3IjJGP1vd7VWuVSo5xI64dc4s4aE8py-HvXjZl7Dt8qqH87NgHFiwbeR28i5JRzj3jx_SnS4Gif3AJSo18f4mtRpYjoE_gy-9P-dsTxqFzChoT0QVavLLo4ERIZNegZhNpVCUoo4HpFsdEMhT16rTB660oeuQTg_4xAQVQJR1WyoybtyIIrF0vIRSu6k_SVjvMqgq8HWPEqKHwGrXMtgK6dnthi3gmp6jXtwEDI9NgTYf5aw0VtZ7zw18NDCAhZmKFrXYMHpcJauRPLqjkRE8C5Ic93tH0DUpXXdu4m5OVcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
برنامه جدید امتحانات نهایی پایه های یازدهم و دوازدهم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66284" target="_blank">📅 13:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66283">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
ترامپ:
من به اسرائیل پیشنهاد دادم که سوریه مسئولیت حزب‌الله را بر عهده بگیرد.
جنگ لبنان مسئله‌ی فرعی است و توافق هسته‌ای با ایران می‌تواند پابرجا بماند.
به اسرائیل گفتم حمله اش به بیروت برایم خوشایند نیست.
نتانیاهو اکنون باید در قبال لبنان مسئولیت‌پذیرتر باشد.من از نحوه برخورد اسرائیل با لبنان و حزب‌الله راضی نیستم.بدون من اسرائیل وجود نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66283" target="_blank">📅 13:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66282">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
ترامپ:تلاش هایی برای تغییر رژیم در ایران وجود داشت اما موفق نشدند.
اگر ما برنامه جامع اقدام مشترک اوباما با ایران را لغو نمی‌کردیم، ممکن بود این کشور به سلاح هسته‌ای دست یابد.
ما می‌خواستیم برای گرفتن اورانیوم غنی‌شده به ایران برویم، اما این اتفاق نیفتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66282" target="_blank">📅 13:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66281">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
ترامپ:
توافق با ایران به مرحله دوم منتقل میشود.ما یک توافق منصفانه و خوب با ایران داریم، اما هیچ پولی در آنجا سرمایه‌گذاری نمی‌کنیم.
چیزی که مرا به امضای این یادداشت تفاهم ترغیب کرد، تضمین این بود که ایران سلاح هسته‌ای نخواهد داشت.
چیزی که برای من مهم است این است که ایران به هیچ شکلی سلاح هسته‌ای نداشته باشد.
اگر ایران به دنبال سلاح هسته ای برود جهنم به روی او گشوده خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66281" target="_blank">📅 13:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66280">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b4a7171c.mp4?token=rdfK1r54So_MGT53ulwsJlubIGo51m-H5LOr_D7P9g3wyPbd6A4vYxfPeaqUwTWGR7lK2cmPuQYBQAWI1aAxd2VjigHgsq9iB3bpmshZCRslH6fb9mVi2EeNyVWWSDydjGaenk8L2fBXqATIi1x4Ld2C6aqwNHC21smQs8hUm9aqv_yleQZPXcA02t5XJyplu22m3MWFDsc-HpFdJbf8ZJBctOR0kqGX8WcQDZnGnCVevV0l4vLd1D7mOSpzpuYYrWoLwRDMe3hNuE8kkg3PMAWylY92lNOz6CugCRtoshc0oJ50iilgjU4bpAIQZmpOOFgoWLh6dMfFaFm25NG3lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b4a7171c.mp4?token=rdfK1r54So_MGT53ulwsJlubIGo51m-H5LOr_D7P9g3wyPbd6A4vYxfPeaqUwTWGR7lK2cmPuQYBQAWI1aAxd2VjigHgsq9iB3bpmshZCRslH6fb9mVi2EeNyVWWSDydjGaenk8L2fBXqATIi1x4Ld2C6aqwNHC21smQs8hUm9aqv_yleQZPXcA02t5XJyplu22m3MWFDsc-HpFdJbf8ZJBctOR0kqGX8WcQDZnGnCVevV0l4vLd1D7mOSpzpuYYrWoLwRDMe3hNuE8kkg3PMAWylY92lNOz6CugCRtoshc0oJ50iilgjU4bpAIQZmpOOFgoWLh6dMfFaFm25NG3lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هادی هوتیت، خبرنگار  پرس تی‌وی، وارد منطقه‌ای در جنوب لبنان شد که نیروهای ارتش اسرائیل هنوز در آنجا مشغول عملیات هستند. فیلم نشان می‌دهد که او در جریان این حادثه مورد اصابت ترکش قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66280" target="_blank">📅 13:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66279">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b685347f.mp4?token=JXpzfZuNcqJX08DHW9Y90xl0WJ9InARdHGkhu8S6FzXa8tsGK86GyULljsw6ZQBg4rft5_x7G35xW9hw6vlrXFymis9s4S_6qbcgqm3ziWEUjdrYFPNR6ENfUu6cSCyn_Q4geLa_tUHTQwYtwPTZGXKjL2oZOsnzzSB17J5qkmPcWu1laJQGHvKq0MiqMejJkqL3WH5gs44sieK5n4DvOwh4Z_cC6Bwip1np5pUjAOSGCMclTL7nEO1qqy_6sQITOVV6CdiaTGDINPCRnosN93xxDh965K1CLxioRmhKBWSax5vkfSGAb3fhdZbfhhadpR_7z1ASauIiZySxoFSAjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b685347f.mp4?token=JXpzfZuNcqJX08DHW9Y90xl0WJ9InARdHGkhu8S6FzXa8tsGK86GyULljsw6ZQBg4rft5_x7G35xW9hw6vlrXFymis9s4S_6qbcgqm3ziWEUjdrYFPNR6ENfUu6cSCyn_Q4geLa_tUHTQwYtwPTZGXKjL2oZOsnzzSB17J5qkmPcWu1laJQGHvKq0MiqMejJkqL3WH5gs44sieK5n4DvOwh4Z_cC6Bwip1np5pUjAOSGCMclTL7nEO1qqy_6sQITOVV6CdiaTGDINPCRnosN93xxDh965K1CLxioRmhKBWSax5vkfSGAb3fhdZbfhhadpR_7z1ASauIiZySxoFSAjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمدرضا شاه پهلوی مردی بود که دستش نمک نداشت
👑
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66279" target="_blank">📅 12:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66278">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
عراقچی:
ما واشنگتن و اسرائیل را یک طرف این یادداشت تفاهم می‌دانیم، در حالی که ایران و حزب‌الله طرف دیگر را نمایندگی می‌کنند.
پایان جنگ در لبنان بخش جدایی‌ناپذیر پایان جنگ در ایران است و شامل خروج اسرائیل از خاک لبنان نیز می‌شود.
هرگونه حمله نظامی اسرائیل به لبنان و ادامه اشغال، نقض تفاهم‌نامه است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66278" target="_blank">📅 12:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66277">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d988cc6faa.mp4?token=nu6lGP5UJGSxpLU6amv05kw5ftno68Ilofmg_OdJKTn0SZ6wRc_MG6tDwzbbVBwkEEMemnq7zlTRB_wVC3_LLcfvZ3IrtwCQnd3yjOVl5zaArQm1mpRG5sd46Et7Qwubjk2xvFD6ESTTV8tyU_L9TWlLO4luvdh9uCAeEmpXe7tNX43OBM7aj80tf9um-iRH9dYK5pgsNxCj66c6fG2qJFrQX1t49pI5W3r0kTsAzl5lw2A65UMtwxLyrnPZruw09q0bez_TStg0uDcCayNrPA6CMZIa9VECf3XG2JgqrBZWP8th09hpjuRYehJ1bVKs1J8Ci2fLZ8I-PzqtkTKaMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d988cc6faa.mp4?token=nu6lGP5UJGSxpLU6amv05kw5ftno68Ilofmg_OdJKTn0SZ6wRc_MG6tDwzbbVBwkEEMemnq7zlTRB_wVC3_LLcfvZ3IrtwCQnd3yjOVl5zaArQm1mpRG5sd46Et7Qwubjk2xvFD6ESTTV8tyU_L9TWlLO4luvdh9uCAeEmpXe7tNX43OBM7aj80tf9um-iRH9dYK5pgsNxCj66c6fG2qJFrQX1t49pI5W3r0kTsAzl5lw2A65UMtwxLyrnPZruw09q0bez_TStg0uDcCayNrPA6CMZIa9VECf3XG2JgqrBZWP8th09hpjuRYehJ1bVKs1J8Ci2fLZ8I-PzqtkTKaMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایرانیان وطن پرست سنگ تموم گذاشتن و اینقد پرچم شیروخورشید زیاد بوده که میساکی فشاری شده و پرچم جمهوری اسلامی نشون میده میگه این پرچم ایرانه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66277" target="_blank">📅 11:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66276">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944350c2ea.mp4?token=amvw_t82jnYrJ1cGunVAunchbYW_zL9bflqxLu64uLiHTrGrpFEjxNUls6Hub4WZGQvi65bFYwzkx94ieSs4DBfUTnUQ2pmfsHue71XGcAe0ImX4P2JJgcR317cnKpkpNLu37iC7PvrKIwk6_hZPZ5qSZNCCr1UQoAzg3vaxymzZJT8NLsIh9U9aet5QnJoApHT1ZEOT0MXZWT4ymoJNNEqim1gO6YFc-03WyFjohPNUrqFJfcnK9ZsgCS_vNNE6-UWYNvggf8jAm2RUVBF_czy0DEkGN7BB5ZYgR_Hpn1zfKhM2oHr3KDae9UQ7xQwYfg6vF00ZjPv6yx8SQTIcFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944350c2ea.mp4?token=amvw_t82jnYrJ1cGunVAunchbYW_zL9bflqxLu64uLiHTrGrpFEjxNUls6Hub4WZGQvi65bFYwzkx94ieSs4DBfUTnUQ2pmfsHue71XGcAe0ImX4P2JJgcR317cnKpkpNLu37iC7PvrKIwk6_hZPZ5qSZNCCr1UQoAzg3vaxymzZJT8NLsIh9U9aet5QnJoApHT1ZEOT0MXZWT4ymoJNNEqim1gO6YFc-03WyFjohPNUrqFJfcnK9ZsgCS_vNNE6-UWYNvggf8jAm2RUVBF_czy0DEkGN7BB5ZYgR_Hpn1zfKhM2oHr3KDae9UQ7xQwYfg6vF00ZjPv6yx8SQTIcFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دلیل سود نکردن من تو بازار بعد چندسال
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66276" target="_blank">📅 10:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66275">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78c971246f.mp4?token=mzUp3obS7bSc7LG0YVTN-Drh-YCo232bawE1_V6SOBfVSSNXelYssAaNYdZMl4ljtfjLF_PfA6729anmnFBw67MYvrQGwWNvFQyzQsmF3DLR2rO-brg1NwvX2oDbQjd6LY5unfCz2UnEr3KnjE_vZAekTYOMn1Lcn4NRYB0ermG4didcoeyvKM6ayWErVrKZuCoNOmdVhcMWfH1WYzcr8FLX18MlovRr5EJJjlyMjJfwnGMDDeKOtS0SkpgjHqueBjLteDS7cb4CA1q_cJYd60xBBItq_oiK1EMTmfMJGxlH7zVdFRFn1VxV-JFSutzsoXz9BNPKHyJRWtsPEuWC4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78c971246f.mp4?token=mzUp3obS7bSc7LG0YVTN-Drh-YCo232bawE1_V6SOBfVSSNXelYssAaNYdZMl4ljtfjLF_PfA6729anmnFBw67MYvrQGwWNvFQyzQsmF3DLR2rO-brg1NwvX2oDbQjd6LY5unfCz2UnEr3KnjE_vZAekTYOMn1Lcn4NRYB0ermG4didcoeyvKM6ayWErVrKZuCoNOmdVhcMWfH1WYzcr8FLX18MlovRr5EJJjlyMjJfwnGMDDeKOtS0SkpgjHqueBjLteDS7cb4CA1q_cJYd60xBBItq_oiK1EMTmfMJGxlH7zVdFRFn1VxV-JFSutzsoXz9BNPKHyJRWtsPEuWC4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تصاویری از پالایشگاهی در حومه مسکو که در اثر حمله پهبادی اوکراین دچار آتش سوزی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66275" target="_blank">📅 10:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66274">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696afa1a70.mp4?token=WHqkF0YeUMFJ1MHJ0G93JSqtDWZTn8KO-woeDjE0-Bl-LoW5-aZBr955mdLfNeAzS3aZerDcwnc8orrMNOhSZ9mDXQ2mjuHFsNwcY8nximhXR3oRA1nNzMDs8vj03ugQB0bUZnuK98n5cgsdZIWR8CjN5u5DVfdJ-JcvCjd6lNKUmyH7juWzsAzHgJpFgfeaIaVAYSd9rNR-8Z3yESHkL6rrbklDgftkLef7KWbrM0mzynANGxsoC5lclmftl--ct14JuI790bJW_IZrTREI557cRWAtTOjx3X9gyx7Vuj7InAYSb5UyyQEzM2eyriNj7Q19jOOxdIgYnM2ShVM8jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696afa1a70.mp4?token=WHqkF0YeUMFJ1MHJ0G93JSqtDWZTn8KO-woeDjE0-Bl-LoW5-aZBr955mdLfNeAzS3aZerDcwnc8orrMNOhSZ9mDXQ2mjuHFsNwcY8nximhXR3oRA1nNzMDs8vj03ugQB0bUZnuK98n5cgsdZIWR8CjN5u5DVfdJ-JcvCjd6lNKUmyH7juWzsAzHgJpFgfeaIaVAYSd9rNR-8Z3yESHkL6rrbklDgftkLef7KWbrM0mzynANGxsoC5lclmftl--ct14JuI790bJW_IZrTREI557cRWAtTOjx3X9gyx7Vuj7InAYSb5UyyQEzM2eyriNj7Q19jOOxdIgYnM2ShVM8jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هو کردن هوادارن حاضر در ورزشگاه هنگام پخش شدن سرود تیم جمهوری اسلامی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66274" target="_blank">📅 09:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66273">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f96ea995.mp4?token=FouKjIEHEN4VDZ2aLM71LFYP0Qjd2wZ0k1Q_C_B0jzrNlTpiOefigKewBL5-BLonL-g5ul5A6AWEVXKFnrwFIWsEe_J6adCxf-puaFGazqizmhHop2PI2Mqxuw4v-jieTG96MqUjAVmTSbGnbtL8tinE9e6I0KG2M0wQMEHrMjrfU0QRFjPfBlqssqBoP7ELfJP4YE1hFBi9xq5KpmT3XFQl09Z4s6FUYn4I1TY_LCPEDd8lYiT3jOS0b4arxXp7lIZkdbotUPvzPRdnD7EYZqPJTJDvSkGt_qp2aYW-Ps8-FfcNdPZSFISjKbvYptcKzyIHgWmLIjzgYtg5SroxAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f96ea995.mp4?token=FouKjIEHEN4VDZ2aLM71LFYP0Qjd2wZ0k1Q_C_B0jzrNlTpiOefigKewBL5-BLonL-g5ul5A6AWEVXKFnrwFIWsEe_J6adCxf-puaFGazqizmhHop2PI2Mqxuw4v-jieTG96MqUjAVmTSbGnbtL8tinE9e6I0KG2M0wQMEHrMjrfU0QRFjPfBlqssqBoP7ELfJP4YE1hFBi9xq5KpmT3XFQl09Z4s6FUYn4I1TY_LCPEDd8lYiT3jOS0b4arxXp7lIZkdbotUPvzPRdnD7EYZqPJTJDvSkGt_qp2aYW-Ps8-FfcNdPZSFISjKbvYptcKzyIHgWmLIjzgYtg5SroxAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:
عراقچی نوچه و اراذل اوباش آمریکا در کشور است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66273" target="_blank">📅 09:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66272">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCSoYjZU_fACfVl1JrOFnp7v8uQNIYC_l6MvD7arJvA8Ms9UxwQzvM8oalN4xtUmQTAKhkco7j31gVzed_AVblhYUgaQtvmhLgEyovlkt4uUKDBgFSlIb1dImwO56KjNEc_VG7w2TsAg_dbmXlDkjCZPL3ouJFgFedqRF0jEpLPG3z4_mvL-mBcTxqUIHi0FHIs4wZ9orBlBZBz09ycE2q5awKyShMCXwMoYhzw7BmxaUn3ATgZMW-HIcbf1LXB0-h1uaq79WV2TpkAfyuKrH8Re3JZ5cmPHSiDjw_8nJ_hAk3IS4ETfkRM0Ul9V9qn1mJQ6DXUFs_PdqVgfRvJ8DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏆
پایان‌بازی
🇳🇿
نیوزیلند
😀
-
😀
ایران
🇮🇷
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66272" target="_blank">📅 06:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66266">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گل دوم محبی
#hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66266" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66263">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🇳🇿
گل‌دوم نیوزیلند به منتخب ایران دقیقه ۵۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66263" target="_blank">📅 05:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66258">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
سخنگوی قرارگاه خاتم‌الانبیا: گل زدن نیوزلند به ایران قطعا بی پاسخ نخواهد ماند
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/66258" target="_blank">📅 05:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66257">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پایان نیمه اول
فرزندان برحق وینتون روفرو ۱
کاکولد های گروهبان قندلی ۱
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66257" target="_blank">📅 05:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66255">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یه حسی بم‌ می‌گه بازی مساوی تموم می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66255" target="_blank">📅 05:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66254">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🏆
گل‌تساوی توسط رامین‌رضاییان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66254" target="_blank">📅 05:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66251">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmfayXDbkpV7B8TZyehdnKmHLKW_FO9E19HiabQb8NiwTah_xv_aLUyxK_TJvxH39rxdJu8XCPQ-Y4bePLO6XQThLKMwaI0ry22xeOkALgiq4Gs1SoOA5AZfT8PMQZcjQrKvgnPxGMq1Rq4wJeRDNfkLPVPqNZb8RYnJPUenWUwivbPxuanbG5i9Zh8xANQCTuKYZIRLGW4JTzYUNa2feczd629KfC4S51gc15oqXgMKcthzNWvtic6VKkn6Q9eBrpk6kdlxTkfoqDtuqXHtsD_x4kNQgLxyDwpfiWyRY5bLMj4IB8Voh9XjFIRh74ZFqjOYVWnS8X1NcDpoag8ySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه بازگشایی تنگه بیرانوند
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66251" target="_blank">📅 05:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66248">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇳🇿
گل‌اول نیوزیلند به منتخب قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66248" target="_blank">📅 04:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66244">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-poll">
<h4>📊 دوست دارین کدوم تیم ببره؟</h4>
<ul>
<li>✓ تیم منتخب امیرقلعه‌نویی🇮🇷</li>
<li>✓ تیم ملی نیوزلند🇳🇿</li>
</ul>
</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66244" target="_blank">📅 04:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66243">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e45QJHK-tyauPxGjNvXl5YSUykNRFr_keR8f0Um-QI2ITyU6gjvdI6_lB0QCLlADGkcmdb7zP79Y0TuAWl5DLPA6AXreNJf7IvWVrr6vtqbFtGVWAbO9oVLqp1tSI1pcSabQMMwzPN2g_VbsmIx_UZvjjF7Yl3iEXO5rzgRwTzQkJyNIHX569WYijzSHkP98VxiD4hxZj8dqPk1FwPlJ0wfZ1R-0xXXfRK-GyCQSG_ogBZqqMpmCFVzOX3wq7zmi6vJTcY4oB8ZVePgZK1Aev3Q4thNfwYKL98lm0BCr5ead6-H5HclkG8sfIkzyY6CFm8J8DxdwKa1JloRe9Sdbjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبل بازی
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66243" target="_blank">📅 03:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66242">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حاج علی یکمی تحلیل کن</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66242" target="_blank">📅 03:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66241">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhossein ؛)</strong></div>
<div class="tg-text">حاج علی یکمی تحلیل کن</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66241" target="_blank">📅 03:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66240">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66240" target="_blank">📅 03:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66239">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66239" target="_blank">📅 03:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66238">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hFAWpewwHBUcwtzFio8g1xm40nuW1_X6CN22no4-WOgIOqlR-6KDRUkhPEBNK5eRG3lUmnggl-Oa4SmDUFnD70YdA-WtkzvILlTJhiBHi0B5uC4VQh0QVFtgLLqR_mN-1xkNqbGDL9uLMX_qxTw3-RYGP8gRMkcojPpXZtBaff_BltbQOMM6burHZuo_bVy_WiPld_cHovSNLP2e054xOASWj3ZSutGpM2ytafbnXCKCWjaWfip_v04S-tS5nn_e8wp5aPTFcDSr2EDKjvGT-dse0tElpQa9gq0geicQniarV0YxGpujIDivTANwy4Oz8M3qFuHfGScU-VvOElRf9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
👌
تصویر تراز امشب:
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66238" target="_blank">📅 03:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66237">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
صحبت‌های ایرانیان مقیم آمریکا قبل ورود به استادیوم
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66237" target="_blank">📅 03:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66236">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S71CJaeWyFK5o3SjAJ68NRUUw5C2Or8LRuLkYs087A-AJFXx4kr90kIF1YkH5Jqgq5eVVQFIRNNosBwTZA0CR0XAHvD_gdk2Bq61hGC6L_qMqo9DbOnDDMGMy19H7cl8_1pvUpwn6NCOKkzYTM1QH2IEiE7mT6h95xM1yiRHiVJYa36wSNLf-HdLNID4VUrUjeGvREjpd5nyNh3OZwhkDgs2Xp_4jKNAN53O8JyIsJHNBJkZ6-p9Fw2ErTdrh6HIxscOc00gFzlIebEONply5P4PvesnIzRubhuM8AvuXpWKjprAouF5s8SkOpGUwR6NT7AS_Q19j8MLzP6t4KcJEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی از اسمش مشخصه، باید برای ملت باشه، من نمی‌تونم رو این تیم، پسوند ملی بزارم، یه مشت آدم منفعت‌طلب جیر‌ه‌خورن که برای ۱۰ دلار بیشتر ناموسشونم در اختیار ج.ا می‌زارن همونطور که تو ۲۰۲۲ وقتی مردم داشتن کشته می‌شدن اینا دنبال حواله خودرو بودن.  آخرین باری…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66236" target="_blank">📅 03:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66234">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c366b2c0bb.mp4?token=b9xgzsU60zAsV-SPBQCkPM99i8Fu3Ts6gnuc9lY3x2M1rvRL6asH9GW4TM_KcAg3zy-nYA1XvcjIn7-uHEe2bj9AIpS4O58xNeHA1IKHv_nhJh89vFrNFfnkm6lXjTEf6Eqc4SZEHUDDrv3FWLHgdflZG7kLYqwYWFTunQ3RVKcMmVwGETS4mj1yh-NNX-0hywmLtRJA10EBy8HrqEjyaeQdCDAUzHtOtQn4Pvd1FaLfLWwj_Lkmk8bbig0zEMlF-pnSZwd8kDXh9dmAkfTbD9qaBtFw2uk4Bv_hnIB2Z7ca_722puSp0Oaz7BlBEdrP9C6bsh-Pg-m-KYoLyQ9JLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c366b2c0bb.mp4?token=b9xgzsU60zAsV-SPBQCkPM99i8Fu3Ts6gnuc9lY3x2M1rvRL6asH9GW4TM_KcAg3zy-nYA1XvcjIn7-uHEe2bj9AIpS4O58xNeHA1IKHv_nhJh89vFrNFfnkm6lXjTEf6Eqc4SZEHUDDrv3FWLHgdflZG7kLYqwYWFTunQ3RVKcMmVwGETS4mj1yh-NNX-0hywmLtRJA10EBy8HrqEjyaeQdCDAUzHtOtQn4Pvd1FaLfLWwj_Lkmk8bbig0zEMlF-pnSZwd8kDXh9dmAkfTbD9qaBtFw2uk4Bv_hnIB2Z7ca_722puSp0Oaz7BlBEdrP9C6bsh-Pg-m-KYoLyQ9JLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تجمع هموطنان خارج از کشور مقابل ورزشگاه محل بازی تیم جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66234" target="_blank">📅 02:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66232">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwH2Nj50I0C3_BJnQT83R_hMvufHXWC0VTmLLYVnIO1kR8Hb_CrVxp7REoq4Oc6JZQK12oPuTlAZym9K_OZumACH35kr1m_PgTIk8CdobEVRdEsWBuJmT9ZmPBrkPGIZYEVySTe2quPBT5husTH9TLwrLecJXIKBjL8n0EBKwmcriFgSNPf476rsxoimhDrL-QxbvG_kgznj1F4EZA7c1H3sJ-QE9rPPBYaAF2KpICHPjUhbsqCoEPxZI-EPl7hBi8iCgfoxRarqNOKvgALIa3osMuum3nYyqQOKp9LKoSNnanqdF9GzSmvY1pe_4KgD-1OZXmKKPtZXiAd1bWBNmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی از اسمش مشخصه، باید برای ملت باشه، من نمی‌تونم رو این تیم، پسوند ملی بزارم، یه مشت آدم منفعت‌طلب جیر‌ه‌خورن که برای ۱۰ دلار بیشتر ناموسشونم در اختیار ج.ا می‌زارن همونطور که تو ۲۰۲۲ وقتی مردم داشتن کشته می‌شدن اینا دنبال حواله خودرو بودن.  آخرین باری…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66232" target="_blank">📅 02:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66231">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
#فوری
؛ترامپ:
ایران موافقت کرده که هرگز سلاح هسته ای نداشته باشد.
همچنین ادعایی مبنی بر اینکه واشنگتن مبلغ ۳۰۰میلیون دلار به ایران پرداخت میکند جعلی است و توسط دموکرات های احمق تبلیغ شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66231" target="_blank">📅 02:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66230">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
صف ایرانیان مقیم آمریکا برای دریافت تیشرت مخصوص ورود به استادیوم که تصاویر جاویدنامان انقلاب دی‌ماه روش حک شده  @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66230" target="_blank">📅 02:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66229">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10adb291f.mp4?token=jVRrQl636Qxe-fPfyj2ZElyEJkfj6O4yAt5kQbaZOgAhWGic_oNx4EE7MgKx4y5m0igp6Gx8N8tGyxkF0gXonD6QvmqWQ-53cvSSSUUzy0IMpO4RMTzs98JtgxtyNYxYkvxuBTzEmuxWhAPm2ZHYRAPxMJZUJKIgP__3K0Fpuy8Clc79yJJ9AOCZBxV9mTk-sMV11Is3anlbp3seuF8nxOWHOcI_Vy1xJEKeTqpww-oGRKLDvnq9ldDFj3UwUtnQLJED9PDvtc87IokDuOIkc9_0cm3TYG7TNLtV7PmkyUP0mKhhnBBj3IPaIUOQW5yTgFEy7hYAXDzhYTWwYaNAIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10adb291f.mp4?token=jVRrQl636Qxe-fPfyj2ZElyEJkfj6O4yAt5kQbaZOgAhWGic_oNx4EE7MgKx4y5m0igp6Gx8N8tGyxkF0gXonD6QvmqWQ-53cvSSSUUzy0IMpO4RMTzs98JtgxtyNYxYkvxuBTzEmuxWhAPm2ZHYRAPxMJZUJKIgP__3K0Fpuy8Clc79yJJ9AOCZBxV9mTk-sMV11Is3anlbp3seuF8nxOWHOcI_Vy1xJEKeTqpww-oGRKLDvnq9ldDFj3UwUtnQLJED9PDvtc87IokDuOIkc9_0cm3TYG7TNLtV7PmkyUP0mKhhnBBj3IPaIUOQW5yTgFEy7hYAXDzhYTWwYaNAIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
صف ایرانیان مقیم آمریکا برای دریافت تیشرت مخصوص ورود به استادیوم که تصاویر جاویدنامان انقلاب دی‌ماه روش حک شده
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66229" target="_blank">📅 02:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66228">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lzn_JyT6qnQBfF5rJZRMKqUzx45S6VsEyhYwDKzjHtEpAEssiuSaxiGuLCnWBUkKzqUG1F_6VtbfqaDIb05_dQ2d_uxjSW85CKQOYLAzCCzuEvOrxqRqp79xYbm8hZKizeY4FljiX7bBbApCISyW9kYaU0nbKQOzlWIGt7_AVdSnPiOINWkrV9MA5_c5Gn_wi6NDnY8UUFQQmCyC4lotQUE9pUs8S1y87ybosCcYMlre7WDExZ1YVCIIHJROK7vjpnfFi6-lyTwm2EC_Xte5YLto1Jp4nAoqde_lBwNkxCVQ_Ln8lwuiCPRYMGWoDZ6pSiBKw5nKq23qajvL0OsWFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
رتکلیف، مدیر سازمان سیا، به رئیس جمهور ترامپ و دیگر مقامات گفت که اطلاعات جمع‌آوری‌شده توسط ایالات متحده، تردیدهای جدی در مورد تمایل ایران به دادن امتیازات هسته‌ای مورد نظر ایالات متحده در هرگونه توافق نهایی ایجاد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66228" target="_blank">📅 02:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66227">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZaAp1Lgka_CFMrAln3QZqGz6S7Z3PA426VD6LzW_NTfrKwDHqgkNp7JugU8G7sA_pnRFEZ9H9sPr8yCUaNLQ8OsQIlS4ulbkvNbpd-UhRzouHd48KAjAFAUxwXA7oXX6N-4b2Xm2xAjbURkj623fRg7bvi848pUu61BKN4uTn2_2qAYgEgI7UuxR2cw5rAxGBCrmvZOvgvaWEt-CQW4-sL8ocbzLRZF5BnsuDmZy7aMJbF55jeoeiVNXJNnMvVeDgOL5-rhMprqyte01iDHosQkKuoLMVkDUKKeT_BsuDCkEtV20TZucKo-TDY0AGVfvL4ZhdxODLh3NKAJi_xhEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فاکس نیوز:
نیروی هوایی ایالات متحده روز دوشنبه اعلام کرد که معتقد است هشت خدمه در پی سقوط یک بمب‌افکن B-52 اندکی پس از برخاستن در پایگاه نیروی هوایی ادواردز در کالیفرنیا کشته شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66227" target="_blank">📅 02:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66226">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
ونس به سی‌ان‌ان:
یادداشت تفاهم با ایران حدود یک صفحه و نیم است و به همین دلیل یک سند عمومی محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66226" target="_blank">📅 01:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66225">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31d4a9328.mp4?token=cACUPchrPr0wgJekvZ0xexp_3-w02VpMOytInXmO59uXs9G5QYF6J7b46u-hwZZ3sCNuAHVRPvYQa6BH9JRUw-NH8nf93pPwoSCjeaYtfKmjz7HHLol9gKfb6irqb46lB5A_1NXoFjq-nNpA09CZ1z3enb443_WBf_-iOh101W5uE7LmJHZR7vVCxYGl_wu5GZxewk74mU2n5zhwMVkGxVPAMxU_MKQBIMhmYXJcW9KMWmX02m8K1CxyBhSNlrM0fA8SWOGtQdK31B3UVJcZzjxiaGihuR7JeJdpRvdhzHNYv8vY3Ad6fKlGfoi79ZbBst7qFx4wkLvNLBj4ISSMDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31d4a9328.mp4?token=cACUPchrPr0wgJekvZ0xexp_3-w02VpMOytInXmO59uXs9G5QYF6J7b46u-hwZZ3sCNuAHVRPvYQa6BH9JRUw-NH8nf93pPwoSCjeaYtfKmjz7HHLol9gKfb6irqb46lB5A_1NXoFjq-nNpA09CZ1z3enb443_WBf_-iOh101W5uE7LmJHZR7vVCxYGl_wu5GZxewk74mU2n5zhwMVkGxVPAMxU_MKQBIMhmYXJcW9KMWmX02m8K1CxyBhSNlrM0fA8SWOGtQdK31B3UVJcZzjxiaGihuR7JeJdpRvdhzHNYv8vY3Ad6fKlGfoi79ZbBst7qFx4wkLvNLBj4ISSMDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه ای خطاب به قالیباف و عراقچی
🤣
:
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66225" target="_blank">📅 01:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66224">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b930a8766.mp4?token=Ixxe5Vcl8CfQMAnGu_8tTqeTSerdki5FaBeZCbxtwEtrXTirhJ35Dy06067er5PfK0y525RQdrBLjKl2w8Ng0DcrGBy5jKHTOWDCbO0D5cK_wr6sy_FErefCJIkZQLP3t3Bhv36FqApOpmM0fB4Gn6Q9tEEJCCbz8P-_rNsWyNhTu7Eibb_KTWl4s9Uvjkz3xtGq-rv7Tdl5TEOYirnsV0vHRu2TGWP4VaatxzQ8x97j-28DY9pEYtuczRuWdlXbftizLK9qdxaqmoyYJ91Tjqg0pToWKZbGWc378WpEZv4ZTKPPmvgY55TcT4xZX8t2IXra1eB-87QeVeEEA_OFpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b930a8766.mp4?token=Ixxe5Vcl8CfQMAnGu_8tTqeTSerdki5FaBeZCbxtwEtrXTirhJ35Dy06067er5PfK0y525RQdrBLjKl2w8Ng0DcrGBy5jKHTOWDCbO0D5cK_wr6sy_FErefCJIkZQLP3t3Bhv36FqApOpmM0fB4Gn6Q9tEEJCCbz8P-_rNsWyNhTu7Eibb_KTWl4s9Uvjkz3xtGq-rv7Tdl5TEOYirnsV0vHRu2TGWP4VaatxzQ8x97j-28DY9pEYtuczRuWdlXbftizLK9qdxaqmoyYJ91Tjqg0pToWKZbGWc378WpEZv4ZTKPPmvgY55TcT4xZX8t2IXra1eB-87QeVeEEA_OFpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرف های متناقض اسماعیل قاآنی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66224" target="_blank">📅 00:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66223">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66223" target="_blank">📅 00:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66221">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromProxy MTProto | پروکسی(|•𝓗𝓸𝓼𝓼𝓮𝓲𝓷🥀•|)</strong></div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66221" target="_blank">📅 00:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66220">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‼️
قاآنی فرمانده نیروی قدس سپاه پاسداران:
هیچ کس نمی‌تواند در مقابل حزب‌الله در لبنان بایستد و هر آنچه از حزب‌الله در لبنان دیده‌اید، تنها نوک کوه یخ است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66220" target="_blank">📅 00:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66219">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2752783b15.mp4?token=DT8kmaflLSgAZMbsEulJS3Bnl8-6O1Mqu51vJ0cL6AWLzq3gUsajI6km-SqSRlijk_mINxedkJTh6mUqWjOujoOjUgIoKE4HeMU9PSFw1zQhxSviSmXuwdCTrCdGx84yaYzhpmuL6SDg7L-9gilslvIWBSR-BWrZYeRM00GK-koEDUkXubIQmmyHYU45K87prLCrhng_-1dJ8gT1pf8dhtAR1WRSOYT832IzaccNauoSb9V3t5E6jzd58WzcCYNn1NIKPJDW71y__tBnKL66zi2NwzxDsxICMyzSbXvC6myz3JKHhm4V7nG3NpGUBLbNFPP2XUP3wt3CbtExU7g-UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2752783b15.mp4?token=DT8kmaflLSgAZMbsEulJS3Bnl8-6O1Mqu51vJ0cL6AWLzq3gUsajI6km-SqSRlijk_mINxedkJTh6mUqWjOujoOjUgIoKE4HeMU9PSFw1zQhxSviSmXuwdCTrCdGx84yaYzhpmuL6SDg7L-9gilslvIWBSR-BWrZYeRM00GK-koEDUkXubIQmmyHYU45K87prLCrhng_-1dJ8gT1pf8dhtAR1WRSOYT832IzaccNauoSb9V3t5E6jzd58WzcCYNn1NIKPJDW71y__tBnKL66zi2NwzxDsxICMyzSbXvC6myz3JKHhm4V7nG3NpGUBLbNFPP2XUP3wt3CbtExU7g-UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
شبیه سازی سیستم عوارضی تنگه هرمز:
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66219" target="_blank">📅 00:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66218">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f287535d76.mp4?token=QAKCIC86jb3c3dwnOiRFQMx7dx3NnA-7ZROKcaDAXPZTq0xw0o_SoSB7HUJpNf9XFhNs3z_LNHXyTNQS7JHYfZnnxubKZzRMLYhUJxKDB7DKWAyig-cWzdmc33-A-VIG8BUC4GHeVzZ8PwZ01ci7K9_q9p2bB_rHxxU6T0i5DMbOGk5ZKzk97xnXcDFeb1xOV1wWeCIxh5x0bWUigGodk-3Slqj0Ij7fsfFbYgFC1-3_g2rLSYT7KH9eqoexSgpvvXSJLdhIMvtePSH8qFJlifSv29ea22jE6jhIo0GClYLCdYKzVj_yREAnmPVvJnR9YXbxhq9pMYfgwenxey_8Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f287535d76.mp4?token=QAKCIC86jb3c3dwnOiRFQMx7dx3NnA-7ZROKcaDAXPZTq0xw0o_SoSB7HUJpNf9XFhNs3z_LNHXyTNQS7JHYfZnnxubKZzRMLYhUJxKDB7DKWAyig-cWzdmc33-A-VIG8BUC4GHeVzZ8PwZ01ci7K9_q9p2bB_rHxxU6T0i5DMbOGk5ZKzk97xnXcDFeb1xOV1wWeCIxh5x0bWUigGodk-3Slqj0Ij7fsfFbYgFC1-3_g2rLSYT7KH9eqoexSgpvvXSJLdhIMvtePSH8qFJlifSv29ea22jE6jhIo0GClYLCdYKzVj_yREAnmPVvJnR9YXbxhq9pMYfgwenxey_8Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عراقچی:
جمعه در سوئیس تفاهم امضا می‌شود و پس از آن اولین دور مذاکرات بعدی را خواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66218" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66217">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تو فاک بت یجوری وین میدن انگار بت زدن ساده ترین کار دنیاست
🔥
از جام جهانی تا تنیس های کصشر دنیا !  هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در فاک بت در نمیره !
💵
@FutballFuckBet
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66217" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
