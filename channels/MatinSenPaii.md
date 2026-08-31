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
<img src="https://cdn1.telesco.pe/file/GXGh15B9XxPrhJIbHAQdsZRsSpygSSMgXnzX8jOqIvgUiue2MNyrqFVZrLepYvKkMnJvYwvyBh4gqLrLxWqImhNrKLVRLuN2Yf_ry9ZeyV3EMNoheluExeO7np4tj2AFVPl16E9cEotJCTZRQGKj4Y2_X3wIIK-jpTGJ33MfNCDqIeS28oYwZFFBRPawHt8tf4skBV_xiypwAk4pIfzSlcDdoiCavRRazoa3GwqxfVR40oTjFxBef8eumDUHpr6PksAJdOS8BY-MTNmunInKv9KdjcTN6gFSlbiwsXoyZIkz6MdzqLDk1WZXgc79luafOfUDEJ_Ixv22SMN-24jrUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 06:01:38</div>
<hr>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مجددا:
این api های رایگان ممکنه امن نباشن پس توی پروژه‌های حساس استفاده ازشون توصیه نمیشه</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/MatinSenPaii/5113" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iNvNZSgYNSprXNELgntd9g0ZN5elMUO3UpVx1v3vXk2Jm38bH4uYHjc61RQ_hz5DYKgfq0ooIo_jKFEA54gNDo85YMz9jyFcq4nYo_tJZY5tJIBj0y0M1IrpnVonbqMpDFIn0LmwfM2aoU7httXuyLPyOkdQUGOQeW2pIgtBw-2wOjGsrir9XHGFH3txvQDq_ZlT759S8ZoNQElgaEnsF3nqZiH6Op4dExlNsI4-Lq_HobxJLZ2T0WnQneOKeNwxrpluQ1Pa42poP4Vrbnuw3Z3ik5wdENnWsKwnvnP4ELGAsFz8Q905EWZNC15W1ttIeukOzF-ruttDeEVVXuAWRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دو سه تا اکانت بذارید و Round Robin رو فعال کنید، خیلی خیلی کمتر احتمال داره که به لیمیت بخورید
تا تموم نشده استفاده کنید</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/MatinSenPaii/5112" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YGtSxAqJZ04M9APVaK-W1B438KCekVt5Jr-71Irb5Ds-CTPkFmjgqcoNaZk40otur7lASovVBbIvYdXLd_hlSxO3jI7xng3DSOyDWpTfl3lK1cN3kUbfV5xH-3awW-6jmSxRET_ua8za2AWPw2_P-hy55_ArK6y1dAgRCb4bZp4CcbLZzNntOJPpZZeMsHAKeUFUYvE0vhgj_2M1IkD_fQdKoenSLHHy8qWZpolTHGXOER1WexoMlcihUPcQTCu2vDAzqvSxW59Yn8vCPYGCd_3aOtJzqUjPUXnvwYckRXYutM4lfcA4ICkmIxNg87LajJvafNhWA66Od6R63xftxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VfPoJxSp2Svf8QNoCLlNHNNef0N4B5Vv82wbzxJIte6YWUSO31ViJmBXSPx5Z7dL2fTuK-_x84iO1E6Vi79nV9UV1_bc3qqYflkYMGBVFvU5R1Vo8UrOnM2YlvfJ4y_YpqpmsSkl-XKNr1a6-q0Eem2Jzsm9JTaJ4dBmRPmk0c2DRrHJBC7hdxEAVyJANLb5KkcOn07OTvI0Pc-rvquAtMXbQc2tg_uB4UsErqSDJTGEIlsXAPFWRnjphrifdl4w9i2-eg4LpX1K4NhBY6DczkRZYo3LsCys2ypP0NjvgTQE76twR4GE7irpcbf7M8mXgS64hr5B-B6AP7ePJGHX_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها انگار هر api key اش حدود 30 میلیون توکن روی 9router میده
بریم اکانت‌های جدید بسازیم
🥸</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/MatinSenPaii/5110" target="_blank">📅 17:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">شاید براتون سؤال باشه که من چه کارِ بسیار مهمی دارم انجام میدم؟
باید بگم که 18 تا پرامپت الکی بازی سه بعدی دادم به هارنس کلاد و وصلش کردم به 9Router و همزمان با 18 تا ساب ایجنت داره واسم میسازه
😂</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/MatinSenPaii/5109" target="_blank">📅 16:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J_dm74h42CTTtspPBVgG5d9Exa74PEqroI6gGD1wNZduJgKubDSba6Yb0y6JhZ94JgzcG4-WVjotL_92ngXXE81njSF2dGZ2euZL4KRJhGwQtXKBzyBgasrkUCWReyS2lKr_StA26MHGNFiL5AAgFV7G016RudZGmTKSiiwkBBdexQV6C-D3RyL7Hv5o4te0ztd56hcVj14SMZsxE-gOEYhQQc272IVwJgX1RU3MFKDVU7sTCArD4xY8x8OElAyAaWi-zHq_uyt0xMHp2t2_dv5CUpgCzf4j7DCtBMdUj4JLqR4V385K0LZxwuNOoh4k8jTwyE61wWKV8DxjWA6Duw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/MatinSenPaii/5108" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bGnWnyOUhPyvYDfzqc-MTwyQu7lDlkIckSzUOxi2rwHrMODXfjRWLLHlOj2PMJ7eaX7mdLk9VfGZJykzVlr4PdQB8B6WKmRJjq3NRGJSzV2N-nfKu4SjCIWe0gA6y3hqc-XGSKdd8CB9D3140Wv26WJoMPM08gkOmOvqoz3fyH294xiZ7Vhdneq908mu7cBvX2rl1ZJIb3i4HFLACt7de5eGIHDEbjwYjfgYMcF3Yy2mJSaJioroST29pr-Nkz0W2SJqdCmSoVQqPsXvDo-patBG9F4ToqYkMSTk_cj1LVUGJF6RgczwiCxCY_XvzW8L_NGszgQKVQ4gwE845kddMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا از B.ai هم میتونید api رایگان بگیرید واسه‌ی GLM 5.3 Flash یه ورک‌فلو سنگین دارم میندازم پشتش ببینم تا چقدر توکن جوابگو هستش</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/MatinSenPaii/5107" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/runx5imsbaTCsjKe0k3I6WoAt9aMfxAPC23eu5P9lA11iBz7iQfNPkHlKLxcL0j44xhbDJpzAZUW4d-HaCwZap1PltOQwsbdq8quTwa8oC8xvQhLAaYgz41ZnbscVHmP7Nk0LRzCX3vOVBtwTfkCOu-vEgvAMfnSshr9m1zzielh9G5vH_kWG1QYM8ZKUemgnvIgLPFlwChdpaBoBCIKicEoeu5--T72E4r519l7-XGrAxt3-2HKlqtY2j1bMSBu4Fi7vZnHXhHTqU-BN6U3plGS2Cc0TrjyQNJ7UKSyhX12zipEOjnckukahpfSwg7WQrvpQ0z1YfFnx02KgA3hPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/MatinSenPaii/5106" target="_blank">📅 16:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lt8co9g5vgxzwQE0RZU0r0dSVmSQqlvNGctUUyQYTL694K5Biut4TViL2Jmypj1jBSLye-BrlQiV3UzWQfcXn-tCc9BkrDiK4KEEYwPh_G7-lS0vwUoyofxEgNTMDqy_gTSuBr5B2pN5eefaT29U_F9WSoIZT0HC2HjA22O25LUGgX1am8cLAbW4PU2-WeDFmFMiObyE1hAbBmS67DeLWaUbgONoAdDH198R0Yw38eBerJ4W-e7c5ujVfSUlYLjzgjY4617iv-_em3ZVmnutdHV8oRfS1ZouX7LXcjxgRm4z8QkA00v4k2EwUQ641EhuJ2tHJQQul5F4csIPb5W_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🥰</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/MatinSenPaii/5105" target="_blank">📅 16:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lm8VTaXtXTuveDfVV7aXi7TEnvihphsmuajT1MpgMetN9Gt3oIRklHs9dUB_2s0S8doK36w-jNI1UPWwpVSFW-XbMOj0IeU8OVqKK3xZwQh8qIe7sIYSE1Qzixr0GRrwxR-3zOu4fgmlpdPgEtGtT3GGQGryL5V3Gc4xfXY_l6NN-vX3fd9fLCDVnmQB1b1EnHCr4F9nHNqu_4VRESrVhRA6R_w3tiCTLdI1NwoyHzBA9VxtKxrSFRqFPIzEcFyx8MFPKTjiwzvzS38eAPSHSiB3wcqhlSzWJr5LscA115hBt9O7Jey-biwuZGmxSLZU1GMtRLkAkqf5dnVu07JwHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟
توی این ویدئو، با
یزدان عزیز
در مورد این مسائل صحبت می‌کنیم:
1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور
2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن
3- تجربه شخصی خودم و شروع واقعی برنامه‌نویسی و مسیری که خودم رفتم(به علاوه چیزایی که به درد شما ممکنه بخوره)
4- تغییر قوانین بازار کار و حذف جونیورها
5- اضطراب، فومو و جو الکی شبکه‌های اجتماعی
6- درس‌های حباب دات‌کام برای هوش مصنوعی
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/MatinSenPaii/5104" target="_blank">📅 15:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت: https://app.mpay.cards?startapp=ref_S4FPMh ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر: https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/MatinSenPaii/5103" target="_blank">📅 15:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">و آره، منم حس میکنم یه کم ضعیف‌تر شده نسبت به پرومو Ox Alpha</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/MatinSenPaii/5102" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vlJ947Etx5K9aly0cOKmLTBlFwUPcJdqT6ZV_LfYsYUogRtite3Y2MUnT_bDE3yB9Y32CpoPo8YzbyDkOIZfQWhapQ5Bu-81PVQvinqPCWpwt-NvREafE3l6Lh2FHJUlTA7kLnsy-CdHOynNiI0YILzzyojZ5mxMFYnj-s9trN8PekCdx-kpFdeXltN18mP6ZmuSwpFD2OR77wmmlms9P2RZHu1RgnU2eX49UgmOJpBq1N-g5zKpawWIMTzl7RipxPHprrUD_Sr3CfgsWJA9xIXcSGYmlga7z8-_W28QT5s-uabWYG4x6IeV0ZqPjoDXhrxRF3a8BZqLey92CIRtzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/MatinSenPaii/5101" target="_blank">📅 14:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Lv1FJ34Ut0X7m5woFr0c-qX5qzLKJUWxzJJkwTh7FuYctp0IaGItuo4apZ1ICTVV8HzIX21jAb-Sx_Co-x6n-qgW5Xjp7Y7lbHhghuyBkZDPK31TZOht4iE1VJnoeqjiUosSAceXDV0Rx_sHCRwUc5LQtbPCS32Eneb_gvnTH2KP04WX80aey4kkKCukJqek2wZF2U3_xuWKbKzOQiLvpDOR3v7m0tsqWiEPJzX2BNsw2Pb21ktbWUX0u9KNk1G5fg2HTZqLVktElzznmQMlqbeslWvDEvUzkDWawHgUerwaCxaUHE5bGrVK_XxAg8bZrTJDQ2FtbsV5-pT6AFGPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IKsLadF1AGPgNvlLFd7nZxqQJdiY_RE8sXQCv58bWG0H7DC2ysx2MJpmukTQnh13JJQEf-gCfKWhz6hu4G_zoFPEnZG3H7jE8loG-O0dwtDt7eoLKYceCnY04v-0n7TEn6x2tM3uJ1kgvCPzvFwh2l3an-R4-s-0CCmDSgiAJQOn0dQK8zEajnjI5VqulbMAvm4FHT9lxOKsOn7xjWE5q1outzG34csFn0eBwOVSyh57owA6aFSmf46CZj9Z6d8DGUhVwQoFO1nie83GS7C7HPfZHUlxOPuUJ5TVvViKUTCkQ-I2gJ_p0uLilD2i334ki-H2SwtgZvZv8A_pMIVhcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:
با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.
1- خود 9Router رو
که اینجا آموزشش رو دادم
باز می‌کنید
2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline
3- این مدل رو از بخش Add Model، اد میکنید. دقیقا همین رو بنویسید: z-ai/glm-5.3-flash
4- می‌تونید چندین تا جیمیل اد کنید و استفاده کنید به راحتی
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/MatinSenPaii/5099" target="_blank">📅 14:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CwqUJetqUBxd7nshAFfoNVcRtPds3bGC4x7KFYuSoAWkVBTnFHjUvszOy_Nzg7mt_mbta4FlItDh4bE1W1HXCzVick3aTqKMLXnxTbqOCp5GDoDRzCPilH3XvAcdPtKK3KGtikDBCFfui5L2kWVyoGR8RLJPEI1_IyPppQVu8kt3AB9VFoeWAR4GVea4-mbrT1atB-8CHjKbApDeNkM5F0ufVvq8purAY8T7fbRpDi2y_FK8czppSzdotRb5BBwotgBNKRXa6-bGcz-DLYZ21LVehOtSq7JDw_3mj16b7MPd50johKKZVzlyAe5GLzPbaWcKmx7KwCg09rFiD-tVRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن #ClosedAI</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/MatinSenPaii/5098" target="_blank">📅 13:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دوستان من به نود درصد سؤالات غیرتکراری توی کامنت های یوتوب جواب دادم. بخونید شاید جوابتون اونجا باشه
هم راجب کلاد توضیح دادم هم پلن رایگان Oracle و...</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5097" target="_blank">📅 00:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h1uShLd-f9mWZRfHcTdc6VAdsPVuZ0SQeUQ6HCimiZfVhFOKUxNao-shhCM1Oq16pt6r70GChFy5UcwZBkDYEVwlyUzmLggTLl8WLJyJKEG3HwAluo3unUELMZCzBqqRrBTN2_oBmqgKu52j1VDmAJ5X0f8WZ81STj5-p3fBGcy8IwZjQmlip_g_Du0B0uJ9qd-4jVZupfSSeI_zOmMmJ3wTwDY_ccQRg7fs9o1UN3zn4c9Kb82XuOogWf3qg-FnmaNiI03wUI39WGAt8VynYXvhkocsZ1PduGdw8A14AM6DJIYBWExubv7Yb8OLCJPBWZsljgNkDjL5w2gXBo7DRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد پرداخت توی بازی‌ها</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5096" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AeAMuYZzrTXgRnRBIvBS2GfVJQE14d5YInRLG-3RM5Q7Sd40x_xpUPOrSDZE2rn1Co8wCzrodnoRYHiaNAWBcKEGGGjDOTmopomFqdLIUILuOIWwaPD8Gd8qScsZVxhsj-2IaSmBPXixk4RPC8ueEKw-QtpvShrJzO4m_5XdE4ZPa6SotE0tHYy0q7g2V45n9F8gAizZ_sbckcV2SbVSvEvlMrzll3DWv3oICpfN-aYLE2Zx2JkiT18rxN9Jm7VDJnGcEVNCR5-Pp4uv27eRVUQyd0ACc8eVdT6mPPGGmhiiRQRHlOwTKT3zWDSzmM3NOT__ubLOLanFNW2MEf8prA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها بدی‌ای که صرافی سواپ ولت داشت این بود که اسمشو هی با این تپ سواپ که دوره‌ی همستر و اینا بود اشتباه میگرفتم ده بار مجبور شدم کات بزنم
😂</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5095" target="_blank">📅 23:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">Iran is not for beginners</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5094" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5093">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">روشی که اسپاتیفای رو گرفتم، این شکلی بودش که هی ارور Country و اینا میداد و میگفت ریجنت با روش پرداختت یکی نیست و این داستانا. منم ریجنم رو رفتم آمریکا کردم با راهنمایی از grok و بعدش با خود google play پرداخت زدم کامل اوکی شد
حدسم اینه که برای اشتراک‌های AI مثل Claude هم خیلی ریسک خرید با گوگل پلی کمتره با اینکه شاید یه دلار اینا کارمزد بره سرش</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5093" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ببینید من خیلی از نکات رو نمی‌تونستم توی ویدئو بگم به خاطر قوانین یوتوب. اما برای اینکه پرداخت موفق داشته باشید چندتا نکته هست که باید لحاظ کنید:
1- برای خیلی از جاها می‌تونید به راحتی از Google Pay استفاده کنید. یعنی میرید توی
https://pay.google.com
، کارت رو ثبت میکنید و تمام. اما نکته خیلی مهم: برای اتصال کارتتون به Google pay، بهتره که با آیپی آمریکا وارد بشید که با همون روشی که توی ویدئو گفتم من تونستم وارد بشم. اگر کانفیگ‌ها واستون پینگ نداد، کافیه که Chain کنید با یه دونه BPBای چیزی.
2- تمام چیزهایی که روی گوشیتون از گوگل پلی دانلود می‌کنید، می‌تونید این کارت رو بهش وصل کنید و خرید کنید. حواستون صرفا به اون آیپی آمریکا باشه
سؤال1: اگه یهو بدون آیپی امریکا رفتم بن میشم؟
جواب1: نه بابا. من دویست بار با آیپی آلمان و حتی ایران رفتم. صرفا ارور ممکنه بده یه وقتایی که ارور کانکشن میده و ایپی آمریکا که میزنید تازه درست میشه
سؤال2: آدرس و اینها که ازم می‌خواد و کد پستی و... رو چی بزنم؟
جواب2: خیلی راحت سرچ کنید Fake America Address و اطلاعات فیک وارد کنید اما سعی کنید همه جا همون رو وارد کنید. حتی یه جا از من کد مالیاتی و اینا خواست من الکی یه کد 8-9 رقمی زدم و گیر نداد دیگه.
سؤال3: کجاها نمیتونم پرداخت کنم؟
جواب3: ببینید یه سری سایت‌ها احراز هویت با Passport و... میخوان. مثل اکثر سایت‌هایی که کریپتو میفروشن با Debit card و اینها. فقط توی اونها من نتونستم پرداخت کنم. تا الان هرچیزی که خواستم رو گرفتم. که اکثرش هم توی همون گوگل پلی بوده</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5092" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n9-WVPdC70jVEmNkNp7nRvo4EYMppYhEG3DENK623q76Q83OWUrB0AGKW9XkEtpUAaephalAkCXsCQmvDldjGjCiYEOwc4oIEFF8F-7MW_x7Pe1CS1f-ZkIDSR3euqQGazMRvLf1YZlR3hWPjdZZPgz2a3Wwei88dkFUfw8JDn7o_Upf1l3EJFTsnJeMYAuafff9k1TIGcm1CNJd7pkFqvxhcNAusM8eA8rDyRiUQp9O2or8uXYXQN_AkRK1EQmjm6EIVZxjNPZ9ZF14SR6NFjnwQgxS9LTMT0C6PH3CFKuGdRb60YihyKXzYHFWSDkOsOQKn7aAMIDNc20ICSAgbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت:
https://app.mpay.cards?startapp=ref_S4FPMh
ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر:
https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت برای گوگل پی و اینها:
https://t.me/MatinSenPaii/5092
⭐️
توی این ویدئو:
1- بهتون یاد میدم که چه شکلی می‌تونید توی اکثر سرویس‌های خارجی دنیا پرداخت دلاری داشته باشید که وصله به ایمیل خودتون با اسم خودتون
2- با کریپتو حسابتون رو شارژ کنید و از هرجایی خواستید خرید کنید
3- حتی بدون شارژ، کلی آفر رایگان بگیرید
4- و یه صرافی با کارمزد پایین معرفی می‌کنم که می‌تونید به راحتی ازش خرید کنید
5- سرور رایگان V2ray آمریکا بگیرید و ازش استفاده کنید برای پرداخت‌ها
6- اشتراک Command Code رو هم با همدیگه با همین کارت میخریم توی ویدئو
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5091" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UYJKqvST-WbCUkqWy2GWdTB_-xV--UaXmpK_nxkh5MAQ3evj3cHwwln4buLwLJn_pU9CYSSlX9UeJvR1buDJYkYOReSkahGNabHsFyjeHJiFL0cTGx85q7m9mqsRw96ofD3S8iJI3mHdtSxZkpxEz5AWz-JlQBfGspGMLBV8f-EqrckATYAgsOSqgYHghI5pvcRy9oR9q07DGHQzl4NPGsJDjm7VaROi2tg-f04blRMOQz2-6nb_NPBFRjbgPC8oi178NxDB-Ze4VATNDt5A5obrzL9g5hdRE6XdE-eYMRYceHfc4qFbkGw7d8ohDvKemHc_immT9gOQje432mX2Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی که خبر خوبیه یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5090" target="_blank">📅 22:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5089">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی
که خبر خوبیه
یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5089" target="_blank">📅 21:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5088">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این وسط واقعا چیزی که حال یه جمعیتی رو میتونست خراب کنه خبر کنسل شدن آزمون تافل بود</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5088" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5087">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5087" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5086">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خوب شد امسال مدل‌های AI پیشرفت چشمگیری داشتن توی تولید تصویر؛ تا این بنرهای درب و داغون الکامپ یه کم زیباتر بشه</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5086" target="_blank">📅 13:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5085" target="_blank">📅 13:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5084">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن
#ClosedAI</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5084" target="_blank">📅 13:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=Ed8nXrHmPktNNDPSM_S-cYRxk3bQ7R31zieLDtKeCBy-VK0tdkznpn40nLgww6DQsix5h-rgigMOSyO3IxyaFZaON9OEs6_1hSQwz_JoiUAJ9ZlDIj9R4ee8mZxQpjhVqyPOoGZunUsGOmYagkeJNZJlBKfjmOvGVukk1RHuWvCrsbof5sRN3kBGF-2-IZJeuJc-Xy79ruC4eCghkZeQ4jmA-OTS9sbLWp1zMY1bNW8baAX8tCCTz-qiekAhueiDcRHQxjaUD-asnJUjOEKbucVHYiHL7Mnbdct5WEgF4g6Ja02wxHfvQ0ozEgM9EjvNW-1Isadc0Vxbz0lijZvKUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=Ed8nXrHmPktNNDPSM_S-cYRxk3bQ7R31zieLDtKeCBy-VK0tdkznpn40nLgww6DQsix5h-rgigMOSyO3IxyaFZaON9OEs6_1hSQwz_JoiUAJ9ZlDIj9R4ee8mZxQpjhVqyPOoGZunUsGOmYagkeJNZJlBKfjmOvGVukk1RHuWvCrsbof5sRN3kBGF-2-IZJeuJc-Xy79ruC4eCghkZeQ4jmA-OTS9sbLWp1zMY1bNW8baAX8tCCTz-qiekAhueiDcRHQxjaUD-asnJUjOEKbucVHYiHL7Mnbdct5WEgF4g6Ja02wxHfvQ0ozEgM9EjvNW-1Isadc0Vxbz0lijZvKUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0  مشخصات کلیدی:  1-مقدار ۷۷۰B پارامتر کل ولی فقط ۴۹B برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5083" target="_blank">📅 21:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/u2AMxNctxl1-576LzbiN5cAmsz85l7gevk53ij555_1Lwa0_XtB4-tiHnJda-BKgcnEdg_ipwyC0osn_feUIA0itIRO6JpPJvZ-uqEQWhP4kKY156zzGW2BhSPNEoErDynzPvqu6E6vj-ahenV40I9h18-sh_EON2fG8z5qF7bZBGwijvVXRDuU_8XcTCJoainX11-5Da8lRlM6Rjek7CEmXgupTl7rqaLlG2gt2jScfFMW4AUKNaHPBvI6IcPzxcW43nDqDI79joPZsy12dwmwG1E6t4CnEPeOWRQuKCDxxhjDRfZhCbnWC2pOohseXImYUBCVGDex6L537iXMwUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/kQstzgwRMnecnu-vGHlrHCZZywnEH1AI3Y8bAGbpzT40uBl1rACo_abR5nBA_0G3JU5wT5uc53V4-AfdD6aE_l6knyrSA7T-08edQNM0g3iOoReu7w0P7mkJ4OkCG5EYsxNXPCyR5Aai8-N-2uqcAFdM1yqiYFHx0dAVTLkB5LerRyOA-AfpnkoYwpeEY8fgkCgJW5QqB8KRMFGJdTxixd7eRAj483TGAJKXBNxyv4ZXynBrG-n4xagDX_Zh0cvyMJe1eJAsD9e9Q5KJk0foZTfRqTKh5azYGHtOiUci6ZCcq8Y5QhsU-WFHNpQinufUd-4CGfUHDIxYqS8mO2FWKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/ELkvgs1cF2wKRgBPQVKUZRbALtko7ze3wHqK-Ek5WoM09oQ7SL50HDoX2cDZiPkfArF1le8acYYs_0OIOdkPk6g89IomlSC8eFmS8g8Xko33EocSmf7zMJuFRlYxFKfyPl7CdBNYa1sEGMxXJ81yvdoZwEKf9XWzLC2JnKTz-kB-dBcYsNiQ7LP2C5fdHpABhbSQLdJsvJUXmI4T70aesQUgXbghPaNmPAKgXYBY2U4ubFZ5tnoi7ImvIRdKlACoTg3S8g9AE_0rKdP2V_5O8KmVbHES-9ivPOGU-8dMPIkO2LwXPXpEElx1ZnRgRP-3Z-nLRxHXqWVQwSii-ALvyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راهنمای زنجیر کردن  Psiphon Desktop
با
whiteaesther
Desktop
🔥
🔥
اول Psiphon را وصل کنید.
در تنظیمات Psiphon proxy محلی را پیدا کنید. و یکی از پورت های زیر را وارد کنید . توصیه میشود از ساکس استفاده کنید
SOCKS5:1080
HTTP:8080
WhiteAesther را باز کنید.
بروید به:
Advanced
→
Routes & transports
→
Anti-blocking
در فیلد
Dial through a local proxy
یکی از این‌ها را وارد کنید:
socks5://127.0.0.1:1080
یا:
http://127.0.0.1:8080
بعد
Save profile
را بزنید.
حالا Connect کنید. مسیر  می‌شود:
App traffic -> WhiteAesther local SOCKS -> Aether/WARP -> Psiphon local upstream -> Internet
اگر میخواهید که whiteaesther سیستم شما را تانل کند روی Full tunnel و اگر نه از پراکسی whiteaesther برای نرم افزارهای خاص خودتون استفاده کنید
نکته : قابلیت exit chain را توی تنظیمات خاموش کنید
⚠️
⚠️
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5080" target="_blank">📅 19:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با npm i -g cline خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5079" target="_blank">📅 15:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HuazrdVyjVU-YTuviiKWBwFa7RkpDxkV9oHBG6UAZQp0poBZNw1DRXvtkKORQorWwy5TscJA3I54H78OB1Ky5GAGtKxiVqE1YTIt-kkYvDzo73lULIRcfo6kwQTjtshCoVm0Hb8u17Ty3LdHKnUOJIfWmcAszVzdFvNPk373bJqjNzPxe2av1VSJF4424x4sgqN9D5iuQu6X4X6n1rE92kJGEN37kupE0K3N8oz2rNG2VqImrGdTrDs8f6eLFOG-40feedeWMEPiliiFTsBPhMngIlAcjq1iI2S0Ya4SJQPxfcolfq2Mkqf86DtD5N3J3WUcJsT7ISOMacg31dplKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه‌ای که GLM 5.3 Flash برد برای تمیز کردن گندکاری‌های اون دوتا، مقابل خود هزینه‌های GLM 5.3 که تقریبا 20 دلار شده بود</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5078" target="_blank">📅 15:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">این سیستم Re-Stream همراه با بکاپ استریم رو ابتدا با GPT 5.6 Sol و GLM 5.3 در تلاش بودم که بنویسم
اما چون نسبتا پیچیده بود و تانل هم داشت و سر اینترنت ایران یهو پکت‌ها غیب می‌شدن،
می‌خواستم Claude Opus 5 رو بندازم به جونش
تا اینکه Ox Alpha اومد
دادم و کلی از جاهاش رو کامل کرد، جوری که واقعا Glm و Gpt نتونسته بودن انجامش بدن
و در نهایت هم خودش، اما نسخه ریویل شده‌اش(GLM 5.3 Flash) اومد و کاملش کرد و فرغونی که از Gpt و Glm 5.3 تحویل گرفته بود رو تبدیل کرد به بوگاتی عملا</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5077" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YzLEf9BcpfvxUu9cWTqa4bI6YDxOqZmTVX3Lfzqm-NIthET2FwF5uG0FrKVwJ_G9exra6XLkNqPwuup-Ja2GLK3H47fNluiMyRVT6jplch6naEW9eoqtN003PFCw8Pg2Phn8wEJmVCPpHWjcg_4xis9nLYwJii8FsuWL-4YXveMs6wjKFR-rnFDkxF8RLhol5szUO-zNIgFnlMo0Zzg2c5DzvMCCf-5n15YqKwQxos73P-rebKEGsrasqXZ4FgLcz8ANn0YVroldAxf6E6hakPxbcK1kS2I_fvYn1lsJWWKmKEYXadJkKAL7ypV5QIRhPP54Am94_hzaoyAE0G4ehQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم. دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه  و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5076" target="_blank">📅 15:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pwKjF-l_St-AMsGuJ1Ztc8sHWH8VVwLjSO5RbYFiaIarTEWRYCbz_HxPNQ4fwUDXBAPS0fVEv8CLP3nM1yOu3U0bjPiK44IXFGR0PtzYuHtvhrG42nhNMmoKvYK7IZ9LlGo2n6-8io54X3Qb5Bm_h-JZ2eT5wZ9PEC9CxvnEBv7D2sl3F0ybnJIBsOZLF5sAWnPoN6KfKnuJe3XvdHblqc-frsodMiVFoY8m9Sf1AsjbKqzZklyPtfFDRPJMohd__UQ6pxTfIGrzrmBl2WUABHt56n3uX-GuJhEw-3P4Pmqj3lSXo6-_FVhWz_tkI4yYxhdF7qSoBHZkpdF0oeqdGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم.
دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه
و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5075" target="_blank">📅 14:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eUDulTWnYj3EqN3Ds7KCOhTzZ6FYtONSaEhSFjfrwddb1jryDsKNgxbWZTL7ZZ2s-o99Lg0t5YcOWAU6pErAN2Q057adHUZ3I9jpYf3G6vQ6gpQ3haZgMG_HQTDKjFU9Rr2gEVRQfs0J0cyUZwW8477vykaGOBGuVcoJaLOWq4fHtHlOqPbxo9w0SYfezEFXHtCho3encMW5ZHalYk_bmd0zGKHqeSFjuIUDVvKzocQOOl0lXTjXD9rxMKt6g2GzEAmukSa8Knhk92vFjjo9bxHMgPydT-mV2rSqeAahUmTPqrtjqKZWohwZyf9hys0jgfGfALwBwMT1wVpUczE-6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0
مشخصات کلیدی:
1-مقدار
۷۷۰B پارامتر کل
ولی فقط
۴۹B
برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر
2- روی بنچمارک
DeepSWE
از ۲۸ (Hy3) رفته روی
۶۴.۳
— تقریباً دو برابر
3- بنچمارک
Terminal-Bench 2.1
: نمره
۸۵.۴
— هم‌تراز GLM-5.3 و Claude Opus
4- بنچمارک
Code Arena WebDev
: رتبه
#5
با ۱۶۳۳ امتیاز — بین مدل‌های متن‌باز
#3
5- ارزیابی داخلی با
۱۶۳ متخصص
: Hy4 با
۲.۹۹/۴
بالاتر از Kimi K3 و GLM-5.3
قیمت API (خیلی رقابتی):
- Input:
$0.83
به ازای هر ۱ میلیون توکن
- Output:
$2.50
- Cached input:
$0.04
اما هنوز، رقابت رو به GLM 5.3 Flash باخته به نظرم</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/5074" target="_blank">📅 13:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qoMB4uuQTNg_Zju4yIjua-kCnbN7PhVj3GLM4RlkL0f7g7TS1CJWBqcOwSCPlwwJXHu8lc2WWuv_9OZJVfuyB2BTJeRkERQpwb4N6sqScynvChk6vrPIZfuF_ganF2naKKVUIWmLtaxkaO9Xhw0KlzAp0e7RZi1xmTczkFq-lJTiXcS1uAIs6dts19EglmYIlcIbiAn19WFlImJ20c-aZPOu89Rxt9agPm7zogqq98jlKhhLEPOywqQRTeK61DtBa35plGJd6ICq-n0AE61aHJixlf6fUozPCP8FOMZ2I4svKMzpMJd96Q9ex1I7oyk0pYHt5wpy3L4EAUCni8mR-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5073" target="_blank">📅 13:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lZvRq9XxGsq8zAkkyvZyF_Egla-dS0I0A-hCdNw0TeIYDkGZkGrL1BTBGgWXeyASzSa69e2DbNimch-hWFz1YxmiHE_46lBk-zk8SNURABG9VpIcLCCJh1080iC8cajahjK5COv5T22-H39WDZCo2ikVCSHjpVzxLjaWmrqoB3nv8ZgH-aJ669eEYp-0M0BiH03NTWrQ6fqEkjTk3j3G-yWISrnfFDbr7d7czT50lTwT1PLkxjCdZIuKS94hXPWQKxW5ag8Voly-2nFVr_Ps-PJUQgE7Yq1GvQZIAIt0-EjOJesK9vM9Y_m0TG7hImYhpLzxfLLuNSJlrNOb-OjXog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل ۱۲۵ میلیاردی Qwen 3.8 Flash Next در بنچمارک Agentic Index با ثبت امتیاز ۵۶، توانست Kimi K3 Max را پشت سر بگذارد و با یک قدم فاصله درست پشت سر Claude Fable 5 قرار بگیرد؛ اما نکته شگفت‌انگیز عملکرد آن نیست، نحوه اجرای آن است:
• سرعت: ۲۱ توکن بر ثانیه
• پنجره زمینه: ۲۵۰ هزار توکن
• سخت‌افزار: فقط یک کارت گرافیک RTX 4090 و ۱۰۰ گیگابایت رم اقتصادی DDR4
مدلی با این ابعاد تا همین دیروز به کلاسترهای گران‌قیمت نیاز داشت، اما امروز به‌صورت کاملاً محلی روی یک سیستم دسکتاپ اجرا می‌شود. مرز بین مدل‌های ابری و اجرای لوکال عملاً از بین رفت.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5072" target="_blank">📅 12:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=LFdfj9wqJSsO4BjsPq7UbMgrtPTjDSzKUEcpnVDC3unq-wVH_CwKLn6Kc9bTPFLeITtNIMX6gLcWlbU4aOtXW-rcFufxHMr7CE5ba3nmtGboFJpieGq-5cmNMRSqUYzauCpNYKYrYtIlHfLESvOQ6eNNcDgvfgiU6-OqP3HcJaRdLNHHneGnjUD3VK507PY1AqwCDZc6zsjMPdCmeNakg8f9yk9xQIxkpS9Q4VbK-FA1KeIWazmoMl7TlSh77YRoMqA7h-lIODfpMhay8Qb__Qq27mOtSeISFF8JZlyckUri-4iptq85g6hhbi_bzjv2eFz2i69LH1j1zmJ-KCGLvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=LFdfj9wqJSsO4BjsPq7UbMgrtPTjDSzKUEcpnVDC3unq-wVH_CwKLn6Kc9bTPFLeITtNIMX6gLcWlbU4aOtXW-rcFufxHMr7CE5ba3nmtGboFJpieGq-5cmNMRSqUYzauCpNYKYrYtIlHfLESvOQ6eNNcDgvfgiU6-OqP3HcJaRdLNHHneGnjUD3VK507PY1AqwCDZc6zsjMPdCmeNakg8f9yk9xQIxkpS9Q4VbK-FA1KeIWazmoMl7TlSh77YRoMqA7h-lIODfpMhay8Qb__Qq27mOtSeISFF8JZlyckUri-4iptq85g6hhbi_bzjv2eFz2i69LH1j1zmJ-KCGLvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این لودینگ ها هم جدیدن و خلاقانه خوبیش اینه که SVG هستن و توی سایت و اپلیکیشن و هرجایی می‌تونید ازش استفاده کنید:
circleloaders.dominikakissi.com
@Linuxor</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5071" target="_blank">📅 18:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DUczIKatH8RytUC1od14smeJk1nGszO0It3O2A0F-P-fBNDY499yH5-Nmnx3CdOSLsukJJQHcVIM0HSlea31kTXsTmQf9xnusdrCQbF0fUcYdNfymRLE-g4WUCgIe98AGIYUZDjpF06gPDXIwnQ81wUtUgXJe1N3-st4QX1xTa8VBk4tP9iJcC9XQeQYAouC8HocbL6N5ncj47nnivKNO7S3qOylhZbI8EepUaAy5gfhTzNQN_K9U27yo4l8a6X0fRpBLYaGPnw5XctGx9Zf9mtubkkObXdZp5wsc5GWC3EMJErPshdQPgGGUQ_iT6lcV-Y0N3m6XPODpy0Vlp3MtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچقدر از هوشمندیش هم بگم کم گفتم</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5070" target="_blank">📅 13:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dGyvLl8o39_Oi7fIbOcAqPrhG8WSsUYVccGsuidZf1pzc8imtzxts45OyixSTIpJQBz3i8QqSfgA3gEFJ7SIFt6YoJaAzjNzR6Abr1I4Bf_y-mpP7RtrWchEO2_zeZtLaVE1maG_bbH3ny1mdNVJ06QclicM8Mrfi97lkNsNVXjRJ79eZH-vNkEHY0YznyYm7bqvurxzhztvfU8g2I8a0apE47B1MW0QGwuEGPDULCiAzvr3UxER2dcgkHwM7O1wJgdZYFXVFkXm7sIt-HG5WFLHiu2cjqzaDTgAUmlxN0Faf7Hu5E9pJOvkAUfqzmMIcpqk7vcd5VAhayQ5nNvKMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ Input Cache اش خارق‌العادست
روی خود هارنس OpenCode</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5069" target="_blank">📅 13:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NA1tnA0FxHh_Y1O2CQ7ewzcRqWOLTbplVyKz18K-GjNJJw_lgHEMBX7LlprAtd8L4Tsodj6ysUekkH7ZYAsIrjaEBrdlW--Yyah4pauRhFy-z2gsNiQdcYMk_V9BTlR1J-EKeSt3gVe3X3yVMEDWq4knE5xTQUcuASpiM_lJkjUEUZv5wqOwLrsHUToUZKRA8kUgGHNauXJSC_aRR5zhX4FEBxETgz6iVithF9x5RBYAiaF-OgAJf2AEITs0ggcjxQK5zcnTf5Cl1Gz0rxy9NE8vcDRU80DLtF8evAcbQB0lJKeyHlR7SfHhnA_2DWcIVfFmrWwwXPnzRvmdpfiZ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصرفش خییییییییییییلی نسبت به GLM 5.3 اوکی تره
و راجب هوشمند بودنش هم که دیگه یه ویدئو کامل دادم نیازی نیست بیشتر صحبت کنم. باز ما میگیم درود بر مدل‌های چینی به یه سریا بر میخوره</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5068" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5067">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xbp-ck8fAjYbJWIHanBKfdht5ZmnIzuxqNj8A7x2smjdKVXx5B80rGWOpAndoFwapZa7r8OBM7vUXSuHad08LpNTNn_wkYrFtZulgG0y6VLyHTE8GjHn54N0LitQtq3pHnJXHvXLkmUVUBXSxO19i9WVkAnO0oPoDFF7edX_M1i8JFi4Ep_hmK2BniPby2m6TBsl0VaDz44xyLgCUCHQSwahRfK2HmID3FETLOb8oYcKFa6fEVR2Yyfy0o8dOO_5Ftqu0W7ZC5h43HN9ghSJFyq75KpsBb6K62Rscx_VK8PSVAc54oLk0FToqYDheZTDTtpZN-dkpDCDgaY73-JNRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5067" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5066">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5066" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5065" target="_blank">📅 12:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GW5GGKvLL8ocpIBCltnpi9eOx_hpac8fpfW5MSKeW_y235MP3I3R-q19RgJ0K1_fW0u1gfIKQPP8ZzNdyaSAq2wA3pPGYfhEn00nUrrgrTyajigZ_AVL1Z0ZTDcb9oani5E6Uy5vGCLyN3q9pQtt9sMRzU8_KYJLYuDeILVT60_4COuTCq2rp6iFDYO1iQsOI_E-ZWSZQXwHx-Z2NaFfNPI7hFjHsSuRpjllw_AEtCHpCIpN23hS5nMwBz9LJjTml72EOjZYE1pfXQxXETop_IFq1eeuHPosBKOFmZ1MNpEdQXO4kvFKoqjK53YODaQdlM6oSvUi7U6WyWDv0g1TnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با
npm i -g cline
خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5064" target="_blank">📅 02:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VE__5UTEGxCM92v022liBe2xQt-P9fpXjOfeCu_EgiTFbth2SnWH9oO0PAF51i6gVJJ3yByb6OAYSnexkzKRldLsRihMoILb5V4EwMXoKLexELsbnxgYU3JJ8apwZuW6mThs0GU8Gp0SuhcEq3tFxFHGESmHDAq2elYrypbna-uaJmcY_GA2ZqC8aibp2hr4wtzXb-HmWj0kGtxrS5ER0YyjoK6ojWfU47z81acEoioO5AR9D5y9dsKn3AXop-xGrqDRUF_jCbLALvSrml1Gnq4XxiUldN_8c9AQnWDtEA_Ev_OSFAMC7qJpbLf1FKBqrEkQOxhRHk0jfWKcag6DCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5063" target="_blank">📅 21:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن
سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5062" target="_blank">📅 21:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rLhcgpFKK4KQsQrBt9TXMY2RfNe5LxsKkeMdR5ECKUIkESYv2hiKon1DCjxdmEpewAN3j8TNd2J7AWttDuwSquxrA6ia_kgxCSnnJR38RJrULfh9hT3isl2MC7LdUcwezBG9EY8Dfroa_CEoZR3e7tHTmoWpzOtwT7wdhIrhLccNTYcbiHy_SsWP_p5unFYn4LlVjn8io6kdlP3tybfraMtqKnlhmdIyjxeW2rTzVtlu_bUKpNv5M1Zuq8Mt18dEzO_MkTOFbAAKgEJ8Ydg05EN7LkuPQLT3i9f0os8AKhH9o0dfWN3_XzBgEfV99dHtRpB79G-jANJSce2XbbwZ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sQyUHqy5AojUa5oqCjONyiJKQYzwJQ4RCiyOa6Pgwdy8LmJNGL0bPPsRKxl798icP8YMbaC9bkS3DVEJCoVNXLbZHMJys1iCd-_uegx_19uzrR5UFB0uVTuwRvOgcZj-AVOS9T7GrVQzz_oLLjAaNDe8bCc3ZOhaSUvjG4NwWxH96o99x6LRPQJW24u2zJbfMqzlH0bIL6dq46g3QZVWX7iY4zI9Bp58XypTk8S_PEEO0r5NIYsq9KeDulNGt9_aWb2NcyUCJg6vyj8I8xhYC33xS0lNSY4UlJNLmcXcmOm6UYYK8MCyESFwc-_-2bMJqoTNua0uzF3gl6RC3gXFXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TWB5VrPSHe81fQOaBpPaavrRh9S1oR0eJzQb4pBFDFkaCs_xqRQB4IUpYR5qKXYTyr2Tr0yPnzUq40FmHLUX8c9Niu-QLeApU6p4Z5B9vxrRm6kwPSUOWZ_oZFiFcJ35Yby_h1yLhQ_zlMYVpGpL5CPv6wfkwy9jkvwlSewzHnpp3BhI9ZovL4V3bjtAA0xTTT8YUdYgHDxgyh2GBUrvtLqss33uy-i-jzNthUAD4UOgElHwQOpaReBuC4yYbwkTg_mLBTcSGjd99J1yPyrdm33hgZ7JE6ANMFxNpYzd0uxtXFvdkBBP3G4kZ01cgRX_voktQCd9-3J_OsbLN0mhkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N-P4HvVrNFGYChg7Z5uX80KjDspmLts-HLnRjQ2XDNm_QEmkrq4vX_3_hFf8KXtQFjMLLDeCxyZXf_oV15NlB8yYFRHslaS_xCz-DQQZLuR2mUlM6R9JI9J1pT4FxsSy3PxOmNAEMlpjmA2F7rRlguMUI4tZ_4RkQYgsfGIUWmbBB0vZt6jQnKRkPfhutt4r46f03g32HTNBvmZ2e4QEBRdUhh_PdVyYgBeW-SbIu2zb_TAORAJ2PNMYRS7-vElefo2KL8a7VoYbs1yD2QzKVLi1bYDVM39bvPkNIDss4mxXY1NMhfw84X-Sg7Lzc_Dae-0iOIFj0QCp3vE8Fw9lIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معرفی GLM-5.3-Flash و ماجرای Ox Alpha
شرکت چینی
Z.ai
بالاخره مدل GLM-5.3-Flash را رسماً معرفی کرد؛ مدلی با ۳۲۰ میلیارد پارامتر (معماری ۳۲۰B-A18B)، لایسنس کاملا متن‌باز MIT، کانتکست یک میلیون توکنی و قابلیت چندوجهی (multimodal)، که به‌طور کامل روی تراشه‌های هوش مصنوعی داخلی چین اجرا می‌شود.
نکته جالب ماجرا، پیشینه‌ی این مدل است. حدود یک هفته قبل از رونمایی رسمی، یک مدل ناشناس با نام Ox Alpha به‌صورت رایگان روی پلتفرم‌هایی مثل OpenRouter ظاهر شد و به‌سرعت بین توسعه‌دهندگان وایرال شد؛ در عرض چند روز، حجم مصرف توکن آن به رقم نجومی ۴۲ تریلیون توکن در شش روز رسید و صدر جدول‌های استفاده را قبضه کرد. جامعه‌ی فنی با تحلیل نشانه‌های تکنیکال (مثل نوع توکنایزر و کدهای خطای مشخص API) به این نتیجه رسیدند که Ox Alpha احتمالاً نسخه‌ی آزمایشی همین مدل GLM است، تا اینکه بلومبرگ گزارش داد
Z.ai
این حدس را تأیید کرده و وعده‌ی انتشار رسمی وزن‌های مدل را داد. جالب است که Ox Alpha پنجمین مدل ناشناسی بود که طی شش ماه اخیر همین الگو را تکرار کرد (قبلاً Pony Alpha از GLM-5 و Hunter Alpha از Xiaomi هم به همین شکل رونمایی شده بودند).
از نظر قیمت، GLM-5.3-Flash بسیار رقابتی است: ۰.۱۵ دلار برای هر یک‌میلیون توکن ورودی، ۰.۵۰ دلار برای خروجی و ۰.۰۳ دلار برای ورودی کش‌شده. روی بنچمارک کدنویسی واقعی (Code Bench) در همه‌ی سطوح تلاش از نسخه‌ی قبلی (GLM-5.2) بهتر عمل کرده و با Claude Opus 4.8 برابری می‌کند!
از نظر معماری هم ترکیبی از MoE، Sparse Attention، Linear Attention و لایه MTP به‌کار رفته که باعث شده حافظه KV-Cache به ازای هر لایه حدود ۴.۴۴ برابر و محاسبات attention به ازای هر توکن حدود ۳ برابر کاهش پیدا کند؛
خلاصه: هوش وحشتناک بیشتر با محاسبات بسیار کمتر.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5058" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a-jSD_GCY3WIdtZQIbkx-GaQGJqm-46OkNpyRdQcoJBraF0Y8tJqCw6Dw8aEGY3iACo-2WblInqhSev-_UNhSaz1cr_gIvOBvhuRT6o9H3Fx48C0gL31mLEjYE0kNYqtxhvnz9olslOk5eDd5pBEPTKeOctgbk6_qY8BoBjPjnGaek04B3jbYzc3deVpeXiqNlHjpic9dVWUqJ2pa9KqkePv6dPkMkgl7o4glzLkw0kf9C75uq2Bl0zyvewJTA1tGyMRngTP7Hm_qh5f9CL871zU8ktApxwIOMOKpOeVoH-3jkPY7r0TDzwIyUKr8Q-W7vc2Jw2hC3H8YycBiuNhNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oFAqQWQOBTgR5k006x-lWg65aU5DqzQIIgR60gV3fgedvOFNqIrCn0mxBbmIvRP5QMcvnggBa0y6F3oV6kuhzvxR-byX5M8NF27o6hG0TTu37J52qHZLxxUBY7cFORujOpe5eX67PxMQ1pnRxI9Z6U3aQrhIqlVGMys_klUFwwTzI0_h0HLMIrrUVKBhauJlXVR-kt4w0CUvGDCDCjReylNyx7rfxicl_YuHE9KzwareG9aDSEXd16G01WfTC8dqYhh4EvY6qjg9idiKn8BOZpM9i6Ze-6WIL7F6h0bk9g7Qq09BznTrZ7tU2pi0TtOaqIfWWPu9Wwl0RS-eZXpanA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TrAE1cUz-zb1ebFrZZz9W1hIfd9eJRZFLF16LQ6YlLHauXbUqhL3UERFCytBgWbarBZJRgOadz7Pv97DfPQz46I4j-Q2Y8R2SGkgz4ko2sPlztdYpuTRG3w5hdskkX8lkkbr7ft_4bv8NO3orexo_lkgkdZhl633d4kNBzr9Cg0ume7XQo-egC3lTP_w06Psgpy13gv3vcEJy9OKvLcstEZCTaYuqwnLkgTDCAq6mD1GFkOAtRMAScp0g1lile4wqPq6TLJNlfw97yoEenn68iyOZhbLUmHfiSGQTtyfE_FSvGtMfFYyHTi9Ewyxk4cgE8WoAkGk_A2pWmADjQI0Zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">باورم نمیشه
running Entirely on Chinese AI Chips
😐</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5055" target="_blank">📅 18:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خبر:
مدل Ox Alpha در واقع GLM 5.3 Flaah بود و گویا حدس همه درست بود و جمنای نبود
🥲
اما....
مگه میشهههههه
مدل فلش از مدل اصلی انقدر قوی‌تر
😭
😭
برم تحقیق کنم ببینم چی شد این دو ساعت که خواب بودم</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5054" target="_blank">📅 18:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/INSTiF3YKCFLelFtyIbYtj_akkHtHZg80nBjxop--d1pcHgkphpuiCxt2yZMTkFL3MduwJDZ8FHnDOh0R5SgUjfslUICl0SEknKR6AgiaQg8leNgAjr-6cM9bosN_svEjNJzWq5Oboy6GqApvxtH619B86nmx8-Qh6q6XLiNTdJ8Jfyu5SbfQjYyTLoX92I8MJrjh4lcYS63lfREXmZggDD-WeCVqxLRtQttOKTwwRmSziGqKY-5flX_pjag1g7giwfxKp-DUZNoz_BXf4Nktf8xFhJkqAb3B0H-67CprWtUzPTcUFdq-DRsXWAdkRRWabaYq0KgUkaTuDBzCkWhPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو ساعت خوابیدما
😂
😂
😂</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5053" target="_blank">📅 18:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5052" target="_blank">📅 10:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d2vzUMNZpNLlf-aM4kezx-pqVI6P1Gunwf-Kd3LO7W8cAxJbF9xhXzV0A5u8EHkxHmGgL61aL4iyXf4Lrp4WU7vCa-VFHN0qWk-GhKg03e-iFg2hQ4KZ1I3R52S6AMQy1fRi9R-ZoCAIlW6Jc39L3X6FZpb3RrIe4rbf5AasAcN9M0xfC22aXTLuFk08mDlr2D2rjFUwGLYQrMhTPYuIKCBxU5337r2kHAcrh58MCByRTl1nNzbbJCf_e7X2PPxl8ggOU70LiHRl4CuKVGDnnXwAuTkgQdOCFBdURIixyQSgzd-APBzwX-sHBuNBG-ZS1Pzv59os1vZ0YfpyGDXqpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha
با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.
هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha:
https://youtu.be/FIhoccZtpZQ
برای شرکت در چالش:
1- ابزار یا پروژه‌ای که ساختید رو همراه با یه توضیح کوتاه و ترجیحاً عکس/ویدئو ازش توییت کنید.
2- من رو توی توییت تگ کنید:
@MatinSenPai
3- عضو کانال اسپانسر چالش، Lira Candles باشید:
https://t.me/liracandles
من پروژه‌هایی که برام جالب باشن رو ری‌توییت می‌کنم و در نهایت از بین شرکت‌کننده‌ها ۵ پروژه برتر رو انتخاب می‌کنم.
🔥
🎁
جایزه هرکدوم از ۵ برنده: یک
شمع صدف
و
توت‌فرنگی
از Lira
🕯️
🍓
معیار انتخابم بیشتر روی خلاقیت ایده، کاربردی بودن و کیفیت چیزی که با Ox Alpha ساختید خواهد بود.
تا فردا همین ساعت می‌تونید توی چالش شرکت کنید! چون احتمالا آخرین مهلت استفاده‌ی رایگان از مدل Ox Alpha خواهد بود طبق گفته‌ی OpenCode</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5051" target="_blank">📅 05:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">به زودی آموزش ویدئویی این ویزا کارت مجازی و روش گرفتن آفرهای رایگان و اینکه چطوری وصلش کنید به Google Pay و... رو می‌ذارم
🎨</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5050" target="_blank">📅 01:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d486Jr2aMc64YyGjswNvUybrFhxXk2tlHGwiyRKuGN5rKdIze3smreqsRD9hMwdstZDBDgmD01iEKIDfPB36IBMtmZW0i1qKuOOTT7cA9Eg6EO5TkYK_lStphTYCxCurRg7eCPwgpcNcI_7wZpVbzyQMKW4CZDqjY6VgwmL29kS_EE7n57yEU45G9YXwH-74SppVcddtxjJQxNJArM_LCRRyZCt5pp1f61W6uoQm1iXHv56D_zNtP7EmD39BqtpgAJH06dau70qJqVRUyeCazRKxHuVpDGDTYPkoo7J-WQ8PJWCF2tDAnGeHEyq32lme_LV58MFgcmwADJ-ZJBhxOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرتمندتر از Fable 5 ولی رایگان! مدل مرموز Ox Alpha
توی این ویدئو رفتیم سراغ مدل مرموز Ox Alpha و اون پروژه‌ای که توی ویدئوی قبلی زدیم رو ارتقا میدیم باهاش! این مدل، به تازگی اومده و یه مدل مرموزه که هنوز اعلام نشده مال کدوم شرکته، اما بررسی و تحلیل می‌کنیم که مال کجا می‌تونه باشه. و همینطور بهتون میگم که چطور می‌تونید رایگان ازش استفاده کنید و کد بزنید
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5049" target="_blank">📅 00:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دوستان من کمی از لحاظ جسمی مشکل برام به وجود اومده بود. الان رو به راهم
سعی می‌کنم ویدئوی x alpha رو زودتر بذارم
❤️</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5048" target="_blank">📅 22:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">و خب من نظرم اینه که، Train بشه که بشه:)) مدل‌های قوی‌تر، ارزونتری که الان هستن و داریم ازشون استفاده می‌کنیم، بخشیش از همین طریق قدرتمندتر شدن
ولی خب شما باز اگر نگران «حریم خصوصی» هستید، دور چین و مدل رایگان و contributer رو خط بکشید</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5047" target="_blank">📅 11:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">به خاطر جالب بودن این پیشرفتش فرستادم. وگرنه به نظرم این نگرانی تا حدودی بی‌مورده.
زمانی که از مدل چینی/رایگان استفاده می‌کنیم، عملا داریم امضا میکنیم که از دیتامون استفاده بشه واسه‌ی Train کردن مدل.</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5046" target="_blank">📅 11:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=a2dN_xaGTkx2oqkuW9QjY12VaiETNmIor5bc-I2LZ118MFtelLR-ajBhgFmiRPdlth59gW8fPc4e9u0G8aa4k9RuQsqmGo19Yeh06tjLRTQadB50sDZbdgf56o16T5vIlslFQF5R047tnO3v6joAyiAYjJXp7Jd3gxSeqXrEced8dxX9opPRncmWpvJvCqVZxihJKNnhofQH2wZtZe3wGpPzrrMssQQdxkiy3Uga9NNNMShU06ZfTxRywgI4SjD6RNPk3UCqqFSoen_YktX6hibx7g_o37vSw0k7jCChDoj8RDcvhqYh8ZEZq4YWlvGP6y8hLgyugoQu1R8L6yTMObZf0wFbO5VmuuRFMTYQFTKa9L7ZWGVtogRnQwb7dp_eiJzPXLzv1txGFmj-H1VkTUsYxvQT9aubk2MEoCDBWIWAkFYnDbD2WA9mephtxThBQU15yrNYCIcWhSbUddwlvIqzn642f0Mg2oI5n2s4vc1CSjZVk0Ule6P9Tn4BLlNYrquEjMIZHy1l1XUqulxXAx88-UhqYQhhdj6fDKEoRSqunN45QOm-fX4jPw7MgeXzN9v4EyZ4Rrw5cTUx-Ij45819HsUgWMm_eX9cUD-v20eLv45DCtOUy5cMNpiPS0spNXz9GGIFFshlKreIFN0oOvmN3T2jI_xzeeIpSQyDmmM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=a2dN_xaGTkx2oqkuW9QjY12VaiETNmIor5bc-I2LZ118MFtelLR-ajBhgFmiRPdlth59gW8fPc4e9u0G8aa4k9RuQsqmGo19Yeh06tjLRTQadB50sDZbdgf56o16T5vIlslFQF5R047tnO3v6joAyiAYjJXp7Jd3gxSeqXrEced8dxX9opPRncmWpvJvCqVZxihJKNnhofQH2wZtZe3wGpPzrrMssQQdxkiy3Uga9NNNMShU06ZfTxRywgI4SjD6RNPk3UCqqFSoen_YktX6hibx7g_o37vSw0k7jCChDoj8RDcvhqYh8ZEZq4YWlvGP6y8hLgyugoQu1R8L6yTMObZf0wFbO5VmuuRFMTYQFTKa9L7ZWGVtogRnQwb7dp_eiJzPXLzv1txGFmj-H1VkTUsYxvQT9aubk2MEoCDBWIWAkFYnDbD2WA9mephtxThBQU15yrNYCIcWhSbUddwlvIqzn642f0Mg2oI5n2s4vc1CSjZVk0Ule6P9Tn4BLlNYrquEjMIZHy1l1XUqulxXAx88-UhqYQhhdj6fDKEoRSqunN45QOm-fX4jPw7MgeXzN9v4EyZ4Rrw5cTUx-Ij45819HsUgWMm_eX9cUD-v20eLv45DCtOUy5cMNpiPS0spNXz9GGIFFshlKreIFN0oOvmN3T2jI_xzeeIpSQyDmmM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نکته عجیب در تست‌های اخیر کاربران از مدل Ox Alpha دیده شده که واقعاً سؤال‌برانگیز است.
همان پرامپت روز اول، بدون حتی یک کلمه تغییر، حالا خروجی بسیار دقیق‌تر و جزئی‌تری تولید می‌کند؛ مخصوصاً در مدل‌سازی سه‌بعدی موتور Raptor که اختلاف کیفیت با خروجی قبلی کاملاً محسوس است.
اما سؤال اصلی اینجاست:
اگر پرامپت همان است و آپدیت رسمی هم اعلام نشده، این جهش کیفیت دقیقاً از کجا آمده؟
آیا مدل در سکوت روی داده‌های جدید Fine-tune شده؟
آیا وزن‌های مدل یا پایپ‌لاین رندرینگ پشت صحنه تغییر کرده؟
یا Ox Alpha واقعاً نوعی یادگیری مداوم دارد؟
اگر این تغییرات بدون اطلاع‌رسانی رسمی در حال رخ دادن باشد، ما فقط با یک مدل بهتر طرف نیستیم؛ بلکه با مدلی مواجهیم که رفتار و توانایی‌هایش می‌تواند بدون انتشار نسخه جدید تغییر کند.
و این، از خودِ افزایش کیفیت جالب‌تر و البته نگران‌کننده‌تر است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5045" target="_blank">📅 11:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">راجب یه پادکست جالب شنیدم در مورد یه تیم نرم‌افزار نروژی که 4 ماه کامل از کلاد استفاده کردن و بعدش کلا بیخیال شدن برگشتن روی روش سنتی خودشون
فردا خلاصه‌اش رو واستون می‌ذارم</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5044" target="_blank">📅 00:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5043">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نمیدونم واقعا چی بگم راجب اقتصاد
برق
...
می‌خواستم امشب استریم بذارم و بریم سراغ اخبار ai، برق رفت کلا تمرکز و انگیزه‌ام پودر شد.
کلا همیشه ترجیح میدم کمتر صحبت کنم راجب بدبختیامون چون همه جا میشنوید. و بیشتر تمرکز رو بذارم روی کار که کمی از این فضای حال به هم زن اقتصادی کشور دور بشیم...</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5043" target="_blank">📅 22:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ما الان داریم دقیقا مسیر ونزوئلا رو میریم.</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/5042" target="_blank">📅 20:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">راستی بچه‌ها پلن 5 دلاری OpenCode Go رو من با همین روش گرفتم. اگر که خواستید بگیرید میتونید به GLM 5.3 و اینها دسترسی داشته باشید به ارزش 60 دلار مجموعا: https://t.me/MatinSenPaii/4915</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/5041" target="_blank">📅 19:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/5040" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5039" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5038" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5037">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jns9HD94utYxzpY2eUUBtsxJlort90paHl9XPOr4eRm-VpwhT1PGv-hATEbWXWbzlRIcfh17an7yDsD_EQR2WfVlXVQPmvWO0-X_Y1CEDBgvedWhV5IHz7btZs-w8JjCWeUYfvQAiHxFndk0F3L6ne8fnvmObYDcrRVIM4EGB7YY5LkKc9s7YO0ZtdPU5afxM6Bpa9mdL6GqANTBN6XzJx2rUU2UNa-TaOJD3GxNL1PTYxYn1rd-sTBX23tWiVcmyjukQOokQh_5WOnfyiftOyTKYMKjNg9cwV4zO5-Zr4PlYLyJlJbk_08SXQYOzFboysCHfMc4koPmFdImhOmjig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5037" target="_blank">📅 18:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cGQGLmkXoWWb5K6ZaziO_xs_l7ByQVMB-JK0A80VeZD84NzZJWRXWhvPD25HO3BrcguUMtkmkIBMVU3z-sjC9QLY7HxQlheSqwtYmITkWRz0EzK_9u9U44pwO_nRs2s056HCD8kDPEFUrX3gFXP_bolGSzJrMDfzdguIwCE30fG9oT1QEdFVLRSik8FMPMr--9HZKUlRiePCthxz1KPxIFvQ16kP_DqLUD1MPtOWYs0cwY3aDDFvBWlNRkM6EjkC0pP9_VZktXwHUiGNKRyTGlFxUM5RR5fiHlcmp89uT_QYydaskZtv47RCzfKD7YCghOK91c9zIqznFb0lNv67rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو:
1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه)
2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید
3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی بعدی که پشت این میاد فردا، قراره حسابی ارتقاش بدیم)
4- آخر ویدئو هم توی ثانیه‌های آخر یه چیز جادویی هست. اولین نفر برید ببینیدش
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به هیچ دانش شبکه یا کامپیوتری نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5036" target="_blank">📅 17:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5035" target="_blank">📅 17:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5034" target="_blank">📅 17:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آموزش مدل‌های AI روی کتاب‌های کپی‌رایت‌دار؛ قانونی یا نه؟
خبر:
اکثر نویسنده‌ها بدون اطلاع و رضایت خودشون عملاً توی ساخت همین ابزارهایی که شغلشون رو تهدید می‌کنه سهیم شدن. TechCrunch یه تحلیل مفصل نوشته که چرا قضیه از نظر حقوقی خیلی پیچیده‌تر از یه «دزدی!» ساده‌ست و Fair Use وسط این ماجراجویی نقش تعیین‌کننده‌ای داره
🔗
https://techcrunch.com/2026/08/23/is-it-legal-to-train-ai-models-on-copyrighted-books-its-complicated/
نظر من اینه که حتی کاری هم از دستشون بر بیاد که انجام بدن، دیگه به چه درد میخوره
😂
مثلا فکر کردن OpenAI یا علی‌بابا با Qwen که خودش دزدی و دیستیلیشن از کلاد هست(
🤣
) و... تره خورد می‌کنن واسشون؟ =)) یا مثلا میان بگن آقا بیا این قسمت از کتاب شما رو قیچی کردیم از LLM چند تریلیون پارامتریمون؟</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/5033" target="_blank">📅 02:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خب انگار قسمت نبود
👍</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5032" target="_blank">📅 01:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یه ویدئو داریم واسه Open Code
داخلش یه پلنر ساده می‌نویسیم با Mimo
توی ویدئوی بعدی که پشت سرش میاد، میدم به X Alpha و اصلا یه چیز عجیب غریبی زد.
موندم که واقعا این مدل مال کیه</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5031" target="_blank">📅 23:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5030" target="_blank">📅 20:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دلار 200 رو هم رد کرد
ولی نکته‌ی دردناک اینجاست که هرچی جنس می‌خریدیم تا الان با دلار بالای 200 بوده قیمتش
الان قراره حتی بدتر هم بشه</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5029" target="_blank">📅 20:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l53r-OGe8PVBAkX5MBA1nSpUv2RkrRD0ntRAxQ-vKvSbpk2ZXaRDdSFECHoBBtfOjI949aCG2_Pp3xcwyy-ZKV9E3fn5MQfY9XCHKxg0ysZZhsBvqsoHgoCilNrZtV-gtd5AQpltlT0y8V8eWQlawbNXxG5BciDcf6Xy04aJrR9dqAOdn4Q1QlffhNoHqASAIQnyw131sSdTNaVJJcNI2XNXxe68kgJ0jaLZ8sXVcnrbU-5v9P4--6KMqrTVxPqs_5b1wS-1didrofzwb8tOZn7WPLOsO153ZuqeaKvZhDRdmoxWMJMNDoMu3Y79EngvfqzKIr1zZWJ1L6oshFqZvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسیدم ۲۰۰۰
تا الان ۳۰۰ هزارتا امتیاز
دو برابر بشه میفتیم زیر ۱۰۰۰
❤️</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5028" target="_blank">📅 19:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gC0YywM5fejmpKB5VMbLw-EfAyGGmhnlZKWTlDEFtw_Nwi9l0iL3AxNg4kGej_GgViXXR7PNgOSZ8quz0IlVVezV5RfuaxxeibaDycnNVm31GgUAS2WcL8Rr-zaXaGFD1rJGVyI9vBIQy6CNm0MIePSt0mmVVfIEbsLord8PHOtqUf_9wbfgfCcisy1pk3pcVkAO3GBD7aLg1Fmg9FrKNAgSlgYHuDLvuvD0SJjGU3xtjdOCXJIGT7Sqv1F1f3vykVsCxlpK6EIZ0ePfYddWOTFXAQwb7eveeKNvgScg5Aaax_hXi8LkbUJvKyFNSyhyB8Lsr5pmXPIxUJALM-k9eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OVaD8t34VPljNn-WfJVQrWxmNZFj0s1-Om8oRKqkM0BYi6SZf7Rq6HbK1AdrRmyafmCRYmEi0fwdZuV0aAc8NxLoFrpGbMm1iJFK-n_wr7AvDJ0bUDEv8tuUlNrS1keyTWgBTQ6TMLPE_HGk34teA5gq7NU1xCwn3nAH8nPRZlAYyjlqlvEnnEoNJdsGY3bU4QRuHODenZPSopEIDrwBjEVrfhbX4rQ7ifdj5gWNEViYlHalbTzj-fpxK6DBMxCFq9wFIzfJhvymUeGcnXUClhfTd8AJaPxzZ3R6ziZep1JLqViGBInTjr-NswojeDRFSUDYKgJ8mIS6Nz4ClhZMJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه چیزی دیدم تازگی ترند شده توی توییتر، یاد همستر افتادم
😂
😭
گویا اسمش ووچ(VOUCH) هست و طبق گفته‌ی دوستان کریپتویی، یه کمپین پولساز هستش و فقط هم یه روز ازش مونده.
اگر که تونستم جزو 1000 نفر اول بشم و جایزه‌اش رو بگیرم، یه اشتراک Claude Max میگیریم و روی استریم میریم میفتیم به جون ایده‌هایی که می‌دید. بازی سه بعدی چرت و پرت هم می‌سازیم
😂
فکر می‌کنم نهایتا 5-6 دقیقه زمان ببره انجام دادن این کارها واسه‌تون اما اگر که انجام دادید، هم به من ووچ میده هم به شما:
الف- برید توی سایت
commonsmade.com/vouch
و روی Claim With X بزنید
ب- جوین که شدید بعدش روی پروفایلتون رو بزنید. اینجا باید دوتا کار بکنید:
1- گیتهابتون رو وصل کنید
( گیتهاب ندارید هم راحت بزنید Continue with google )
2- مجددا توی همون بخش پروفایل، یه جای کد تخفیف داره به اسم gift code. کلیک میکنید روش و کد "love" رو میزنید، باعث میشه ضریب 2 بده بهتون.
بعدش بالا، سمت راست صفحه براتون 7 تا قلب ووچ میاد و میتونید به دیگران به شکل زیر ووچ بدید توی توییتر:
Hey @commonsmade, vouch @MatinSenPai
زیر این توییت من می‌تونید همین جمله بالا رو بنویسید:
https://x.com/MatinSenPai/status/2091522197537919325</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5026" target="_blank">📅 17:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kRFI4JOleH5aW5kHgnIbS4e5bDwUxXZubqAg3HFuBvw1TPFiblqGmr4uLNcXTsy7gD7VDKXiLld6ketgYioe47b-Z3ykCYx3k-m9fpnrZwDfjUze3HQ2GCv2KAop1z4O2Kc9QteIWVSUNmcYK6Tp9s7B9_uEyRwYfliyHq2M38orpMUQULkGFfHdoHKVJ19htg_KcANKwDljfO0T5M9JkuBqVauPjwaOG2qM9Y73SahbzDMh1lNTKWVwIe7dDuuC1_oDv5Wlu1-xmpoHFB7dEp24MuFqj73QY5sYVXmYKx3AQ9jji_3aIsac94zNWcyGXDxEe0qSVbW0ogQLxC7sNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خدا چند ساعت خوابیدما دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5025" target="_blank">📅 16:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1357719d90.webm?token=LyMhbPLZL8RHEXv65MkUobcqDZFR0esDiw_WDdt8EoQ242nvdDnYJMrQ2rAiTiFgCoe6JVmzErd_V2ugJBoKJvejufGot9GUuFvlR5c75_wIYXnIPreaMu2Upf_1pgDyjsosc8-Ai-QIhSQrD8h8P5aPtYWz4yNNfZ5OByGk2Fvbo6deo3tJBe1jE1GsYPePq3FxHfGws8l1s5OOXRRzSWS15VZaorE14MnpU-O3c2sk8WYVgTcTyB0J5tzCKaLYbx9JHvm0JlYh5slwmoqDEefEVqCMUs7-7jnaYfnCKAbtvk4e-UkmLFdxXxkFhCuRTOPtgLzkobOt2x6zBhnKNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1357719d90.webm?token=LyMhbPLZL8RHEXv65MkUobcqDZFR0esDiw_WDdt8EoQ242nvdDnYJMrQ2rAiTiFgCoe6JVmzErd_V2ugJBoKJvejufGot9GUuFvlR5c75_wIYXnIPreaMu2Upf_1pgDyjsosc8-Ai-QIhSQrD8h8P5aPtYWz4yNNfZ5OByGk2Fvbo6deo3tJBe1jE1GsYPePq3FxHfGws8l1s5OOXRRzSWS15VZaorE14MnpU-O3c2sk8WYVgTcTyB0J5tzCKaLYbx9JHvm0JlYh5slwmoqDEefEVqCMUs7-7jnaYfnCKAbtvk4e-UkmLFdxXxkFhCuRTOPtgLzkobOt2x6zBhnKNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5024" target="_blank">📅 16:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">به خدا چند ساعت خوابیدما
دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5023" target="_blank">📅 16:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حدودا 20 روز هست که دارم با ابزارهای مختلف و AIهای مختلف کار می‌کنم و خودم رو آپدیت می‌کنم و چیزهای جدید یاد می‌گیرم، و ویدئوی جدیدی ندادم در مورد AIها تا هم دانشم بیشتر بشه هم محتوا باکیفیت‌تر. اما طی روزهای آینده، کلی ویدئوی جدید راجب تجربیات این بیست روزم می‌سازم و می‌ذارم توی کانال.
(آرک سولو لولینگ مخفی به پایان رسید
✨
)</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/5022" target="_blank">📅 06:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ghtojn7zAU88dLITFeJONFaGN-Tu80bQ_KMsd6Iluq6lXLT72DLOEykvlN5u79BXODonq6fX6YHT7RQrNwxDVTKEMbNN9RIrdU38DJl4NRNUvNrAcSp2oqvh9rDeyHFcW_HpKw4ce5cbivZc2inZkJrQXDB-xO-vDZbwmI9C-XkpvGZtOHEFsjBz7w8x4r9XjalAEqogmTSJnkHE5iiD4dPpXcJpr-IJyNH_739ZJzLFA1iZrJdf9sWJrtXmX1mXnRATewU4bgKfsR_cLHs1unFGNt_WtzX25QpUWmvXsybPaBmuoGHNy1DxMQ2NZJA3B4i_FDO8jSY67GH1dL8NHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kb3oLSlBmX6ZTvUpq-ZwW5EnigohvFLbnszYX-VbkJRSM3LhJdiRFEZqhtgjq8GMKTdF7c7_kFfYRypVp9vJxDUZ38tNAqhU0VJ2CIP3ooDqhiypSm4bVb_A9Xa0n8fHraWZ1LWqNjDxuZdh8yANakrmoAyRiRCra6d2UlJ00Oyr1-dEhBkjo73bTEVX8exXCTHlRyrS_XrAGGVXGoRib-4e7166pDGlTCEE2s35ywRp4oq6g3V1462h6xIP_BB6SYUik6nrDhfHKRdkku0S3KdMZbN3PPieb4G4Fcyc8EUC-MajZMdV1nk4X9yyLRtWOUu9pFXNazHfWKcf9vTf2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیلی خوشحال شدم امشب از پیام‌های محبت‌آمیزتون و از اینکه آموزش‌ها چقدر کاربردی بوده واستون
❤️</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/5020" target="_blank">📅 05:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jwZMTOzUDJ5JTFgTdP9jnRTB3CzntiMnGYv4HLn5Xde9bhWW69NVtMsWPveYSwoDgssHDUrr44OWswbDHpKCGbLff0xqss4gTbERJH4s0DdJlcCZAUp2VKr4lBAgGRijX27k2IjrGG7NG4iCnMfnxJtysqwFgdaiB3J2LGpXmulRinKZ8t1_-0Ifl24r0KBig0wCXNiCt3YRpRB5NmaqrCvhuvYtIZ_RAnqgl39zi2Bmct6c11xYSoeKDIxhQmCK0gE5_c31i1KEcNmqbrhTZ4VGrfi7gOzxvHHC3HCjTqnIKv0ALbBtKx2hYh17OT6VQ7EvXemu0y2b1MnZSKQRyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم یا مدل جدید شیائومی Mimo هست یا به قول یکی از بچه‌های توییتر مدل جدید خود Google(جمنای ۳.۵ پرو). گوگل هم ماشالا ید طولایی داره توی این ناشناس مدل ریلیز کردنه
😂
خواهیم دید چه خواهد شد اما تا الان خیلی خفن بوده</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/5019" target="_blank">📅 17:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خیلی توی کامیونیتی خارجی بحث و جدل شده سر اینکه حدس بزنن این مدل جدیده مال کدوم شرکته، چینیه یا آمریکایی و OpenCode هم اعلام کرده که دسترسی بهش نامحدود هستش تا هفته‌ی آینده و روزی 100 تریلیون توکن تمام کاربرا می‌تونن استفاده کنن مجموعا و ظرفیتشو دارن
😂
همینطور…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5018" target="_blank">📅 16:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خب من این آفر سه ماهه رایگان اسپاتیفای رو تونستم بگیرم با همین روشی که اینجا یاد دادم  مزیت بسیار بسیار بزرگی که داره اینه که میشه به گوگل پلی وصلش کرد و عملا توی هـــر بازی‌ای خرید کرد. البته من با VPN آمریکا chain شده رفتم که ساخت این رو هم یاد میدم بهتون…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/5017" target="_blank">📅 08:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SU9ZJ0EEvJrBX8TrNRj1D5d2AJunODMHS-yHVt_o983FSkZa6r4vRz2K7eoxhBSymDij5Qlf_H6TFZ0CZRn58RzK253WeeNUy1Pm4rrAAPqZvaL4rWBKTQf35A6G7Ro-ttk4f1LUJN2jbRleH_7Oa7capRw7OWFOcbkN8poUsh0Y-yhdc5ts1fX_Yl35mpQe1ztvJ-CxdqPEx8cIHfFAA5yAgn3gkE7OtBcPuUDqHyLtvhrmoyfikV7H27dbP7bhzXWVBr9qU3vlVNjm9BCaEJRbbSDKbQms1Lk3pGlZqTg_xCoj1r2VpGPzYCA6NMMYMXJ2HMLss5veTrjlL_cQwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kPsByEzLT2IQpLuZ1UKct9hAafp2QnMUb3oAX62Cn0u2m2eNBPmkfZkaUYVlDirwQRu-LTgrW0rta_sXrF_pdcJnFf4RYT8iVr96it1nmpJns6KqLai0ysjumnhzIdG3iqcqdFJgjEDa4aQaWGUbJGSBWTptqZXXCBO5veMybYHu0nuHyBov-l-WiJtRMRCHsOt_7LBcrD0l-zLAjYK764g1YZUSKmmx1EtgwsvGA3mWpubr-iH_ZERvWV-_5dj5Gbx5QuwwDAbPsA9v8I4xL2ECUBb2e42900YK8DA3hUXCkI_UbKgrl61gDzvBtX8j6jLCJfFztLLlRLDNQ5OwmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب من این آفر سه ماهه رایگان اسپاتیفای رو تونستم بگیرم
با همین روشی که اینجا یاد دادم
مزیت بسیار بسیار بزرگی که داره اینه که میشه به گوگل پلی وصلش کرد و عملا توی هـــر بازی‌ای خرید کرد. البته من با VPN آمریکا chain شده رفتم که ساخت این رو هم یاد میدم بهتون
تا الان اینها رو تونستم بگیرم باهاش:
1- اشتراک ChatGPT(بیست دلاری)
2- توی کلش رویال کلی آفر گرفتم(رایگان)
3- توییتر پریمیوم(فکر کنم ۹ دلار ماهانه بودش)
4- پلن رایگان Hermes Nous Research
5- همه‌ی پرداخت‌های گوگل پلی(با آیپی آمریکا زدم. و یه سری آفرها رایگان)
6- اشتراک OpenCode Go(5 دلار)
7- آفر سه ماهه رایگان اسپاتیفای پریمیوم(با گوگل پلی. هزینه یه ماه بعدش رو هم کم کرد یعنی ماهی ۳ دلار. حواستون باشه)
و در کل اکثر جاها میشد خرید کرد، تنها چیزی که نشد بگیرم آفر رایگان GPT بود که انگار واسه‌ی خیلیا خارج از کشور هم قبول نمیکنه کلا.
و مجددا همینجا آموزشش و مابقی مزایا و معایبش رو گفتم:
https://t.me/MatinSenPaii/4917</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/5015" target="_blank">📅 08:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U_MfubfOKDiM0nC6Wmv-5SvM2JZzMXNwxk_x1jEO_U3jRvl_dpQZQbOO0Ols_zsu4T-h5TuA1lJWp0X3gTiSAORcTcCZijGOEw_yJwfgvJjPjWDAnXO7TvhDGyTvnhFRuH8yw8F5KRTzB3Zmc6vw1zIyCPWjSCUfEpc-rbzVP9Vs7z98fNXkxcCCCZpWHE5ZE3rENJt-p0OGZ5-OR0MlY5ucUg2vE2iCINfsW0iHA1RuZjaWuOqsAB3HTMXTxueZbbEIrYzdTDDRPE7UDD0Be2AF882Z0GKYDyXWa2fI57mII29hBJ5m61xsNtf-QdyBYvNYJET5oAUU229Kra0h_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router: https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5014" target="_blank">📅 08:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فکر کنم وقتشه کم کم یه لیست از چیز میزای رایگان و آفر و... هایی که با این سایت تونستم بگیرم بذارم</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5013" target="_blank">📅 07:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pWmqE5A_sPRHDm_rZHdt9IAzk2MeOpz1s5LFSE9kJ46fpmgkwkTKof51DeqQpiA8O7skbnKql0HyLsOh6j9HuU709OhcBP-59_fs3NJYny2uRsHSbGULsnQvg3_Q0pqWaUaRITO2qDmLaZlcv22G9c073xVkspPzsu_y56a2oMrqaGCIxX4CZx6wYDvQiw7jxnklzGhs0dkt2ZCkL8gNv1EuYmlcdpDDVQOYtvT_CfARFND4PThuDJdW-2Z-CypXryJnviheWpBgvDf6vwdoOqjadoAeCSQHXK0ebUMqPzK-oQarV33r_uIKp-i6NhP_C-Xlf8XwxJQ4UKt9kiztaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سریا هم یه جوری شبیه دی‌کاپریو میگن «اوه این پروژه وایب‌کد شده» انگار مچ معلم مدرسه‌شون رو وقتی دستش توی دماغش بوده گرفتن.
همونقد معصومانه و مهدکودکی</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5012" target="_blank">📅 07:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router:
https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5011" target="_blank">📅 23:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5010">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ahd6sCFlXYDUlxtno6e3ywy6-PyMmuZn6B3H81aK-DhWDXNkDBt2fLqivMP_oNdRSXYspvvH1fRjPVI51sdYH-Snxf7QCe3s1odqHkopE6T0qBn1JMwLejYS56GUCb-yOGI9EAEYYJ-5qjswORG9GysPGGSPDiZj1DbWBt0D-5PmRyGrajK2RBEiPP6myuPpmPsTUuCBAlNoIgHdUwJW8Uu4QI5_93zc7tKnscxd-urUcgLR1OaQBJ9roNZdN7in_XS6SSl0ZSGhLvuY3aDWKDd2bsZqpAf4nUXao8EcXfWmRYcdu-e2-xN2BDZtLmhcsyMjv-IAo2heQj4aVaem1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther Android ورژن جدید
🔥
🔥
🔥
🔥
🔥
نسخه ۱.۲.۱ — رفع سه مشکل اتصال
این نسخه قابلیت بزرگ جدیدی نداره؛ سه تا مشکل رو رفع می‌کنه که باعث می‌شد اپ روی خیلی از گوشی‌ها اصلاً وصل نشه. اگه ۱.۲.۰ داری حتماً آپدیت کن.
🛠
چی رفع شد
1
.پروتکل های wireguard و warp in warp برای خیلی از دوستان اصلاً وصل نمی‌شدن
توی ۱.۲.۰ «ثبت‌نام مشترک بین پروتکل‌ها» رو به‌عنوان یک بهبود اعلام کردیم. اون کار اشتباه بود: وقتی MASQUE هویت رو ثبت می‌کرد، کلید WireGuard روی سرور Cloudflare پاک می‌شد. بعدش هیچ اندپوینتی جواب نمی‌داد و اپ می‌گفت شبکه بسته‌ست — در حالی که مشکل از هویت بود، نه از شبکه.
حالا هر پروتکل هویت خودش رو داره. اگه از ۱.۲.۰ آپدیت کنی حسابت از دست نمی‌ره.
⚠️
در عوض، اون کاهش سه‌برابری احتمال rate limit هم برگشت. اگه زیاد نصب و حذف می‌کنی، حتماً از
Settings ← Identity & access
یک بار بکاپ هویت بگیر.
۲
. عوض کردن پروتکل وسط اتصال، همه‌چیز رو خراب می‌کرد
اگه بدون قطع کردن اتصال پروتکل رو عوض می‌کردی، جستجوی اندپوینت از داخل همون تونل قبلی رد می‌شد — یعنی هزاران درخواست دقیقاً به جایی می‌رفت که قرار بود جایگزینش کنه. نتیجه: هیچی وصل نمی‌شد.
۳
. گیر کردن روی پروتکلی که شبکه‌ات بسته
پیش‌فرض قبلی H3 بود که روی UDP کار می‌کنه. اگه شبکه UDP رو بسته بود تلاش اول شکست می‌خورد و اپ دوباره همون رو امتحان می‌کرد. تا نوبت MASQUE H2 برسه چهار دقیقه و نیم گذشته بود، و عملاً هیچ‌کس این‌قدر صبر نمی‌کنه.
✨
چی جدیده
حالت Automatic — از
Routes ← Manual ← Protocol
گزینه اول حالا Automatic هست و پیش‌فرض هم شده. خودش سریع امتحان می‌کنه ببینه شبکه‌ات چی رو اجازه می‌ده، از H2 شروع می‌کنه (چون TCP روی پورت ۴۴۳ هست و شبیه HTTPS معمولی دیده می‌شه)، و هرچی جواب داد رو یادش می‌مونه تا دفعه بعد از همون شروع کنه.
روی نصب تازه: ۱۴ ثانیه تا اتصال، جایی که قبلاً چند دقیقه طول می‌کشید.
گزارش خطای واقعی — قبلاً اگه جستجو نتیجه نمی‌داد فقط می‌نوشت «اندپوینتی پیدا نشد». حالا می‌گه چرا: بسته‌ها از گوشی خارج شدن و جوابی نیومد (مشکل از شبکه‌ست)، یا اصلاً خارج نشدن (مشکل از مسیریابی خود گوشیه). لاگ خود موتور تونل هم از این نسخه داخل
Settings ← Diagnostics
هست — اگه مشکلی خوردی همون گزارش رو بفرست.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5010" target="_blank">📅 21:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ub2rs5x_gY054Fa2wQeClXAvEm_UbfLrq8WERcLE31h5FwY63_ZvGWe2bve5beiujRGtz0EpAbe_1kFCefoSHdeuw33NgAboqC2RdpMEekofGUZpT8a01udRDwuXnWNiKA_9AXv6O_UFMBG5sBRkhZgEDe34kEg5b9QcJlZsukPmneoLU-yMekOlfpHCqJS4ofiXBhsr05_ULpGaDGPo8fSLzdtmA--kuKAwvoQxAXqPJSCGLA6gjnDtwuGWbwTYCZks7avsOXXlFG90uxof3Y0vjPT7q5Ln_GY2Ke6I4qLJzfh1wAOnzCcaKuvow35HSZo6azGPbsFR7d7YE9lW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kjO-wnEO-GzPUOEZHcrgO40sS27yDqFmOrjWA3Fw6Ue_HqSMgy0pzff_5oDEFzRyq0igZMyUEj-hu0KNHol-XjySTnBnN0oQif-uKeRnvk37zp5OzzfF5QNadwYzkYFQ4A2IXL8A_hfFYvBPLAUsDg3Q1DZX-MZGkrZOxv3ZyAHWx37heQHoMjpsN0eZi-Q17APkJ5o8ImNo2zR4vGXjx3tylhuP7JOJEIeBsOWeemn21lVs2xE24PP1zgOgYA8Rq7N-3wkFip2sbtIeas3dCtVpb0gYwZ0EXKMrlwCMpUUvHYF35Hkmr5bJG9aAo7aUr-kcLYgSbjvL7yyzkEwa9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5008" target="_blank">📅 15:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد
PattNG
کرده و لذت ببرید !
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt
ساب هر ۲۴ ساعت آپدیت میشود.
///
توضیحات:
چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری و تست میکنند و سپس کانفیگهای سالم را فیلتر و در اختیار قرار میدهند پروژه‌ها‌ی
https://github.com/0xRadikal/Free-v2ray-Configs
و
https://github.com/itsyebekhe/PSG
و
https://github.com/Delta-Kronecker/V2ray-Config
هستند.
اما این پروژه‌ها دو مشکل اساسی دارند، اول اینکه تست کانفیگها باید از طریق اینترنت و فایروال ایران انجام شود ولی در حال حاضر تست کانفیگها در این پروژه‌ها از طریق گیتهاب انجام میشود، دوم اینکه روی نت‌های آپلود محدود (ایرانسل و ...) عملا اکثر کانفیگهای این پروژه‌ها آپلود محدود هستند و کیفیت بسیار پایینی دارند.
از آنجا که با روشهای زیادی میتوان محدودیت آپلود را روی کلودفلر دور زد، من در پروژه‌ی خودم اومدم کانفیگهای کلودفلر سالم را از پروژه‌ها‌ی اصلی جدا کردم و تغییراتی را برای دور زدن محدودیت آپلود (و همچنین دور زدن فیلتر دامنه) اعمال کردم (در حال حاضر متد fragment+fingerprint اعمال شده). بنابراین کانفیگهای نهایی سالم و با حداکثر سرعت در تمامی نتها قابل استفاده هستند.
برای دور زدن محدودیت آپلود در نتهای آپلود محدود در حال حاضر فقط باید از کلاینت
PattNG
استفاده کنید، بزودی در سایر کلاینتها نیز این مورد پشتیبانی میشود.
https://github.com/patterniha/Free-Configs</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5007" target="_blank">📅 15:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5006">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vQIbEy-Hu_q_RehW-9AE7NT06apBnj7dLShyAi1I4muD0BWiGI16ET8YC4APdEbLLUvqFwJPkE21O0U0b6k16gsOjzyk_jE9yLF119d7m70n-LVkbvKCSrf8f6jf-nCINysh9iYNIwtjDe9G11pD8BzWRTq0tKugCdxMTh6ExOLTN2dReeRcA0qMBhY621JhXPfLSr0yAsZPAiy9VvuPs6sB-lclyV381Rkngyqkc1om2gNFraT750EajC5hG4VUeuoRwthjDudAd34SCTe9goF9m8Xtc1ndE7G8sRcHZQrS1IUQsWdjF0fD2L6t5PavUjP23NkRfW5ZNXwRKePE1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مقایسه‌ای دارم انجام میدم</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/5006" target="_blank">📅 03:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آقا این Muse Spark هم عجب چیزیه:) روی هارنس درست به نظرم شاهکار میکنه. فعلا روی OpenCode به شدت سریع و اوکیه</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/5005" target="_blank">📅 03:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم لایو هستیم روی
🟩
: https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/5004" target="_blank">📅 21:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بچه ها بازی Rust نه. زبان Rust:))</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/5003" target="_blank">📅 19:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم
لایو هستیم روی
🟩
:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/5002" target="_blank">📅 19:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آپدیت جدید Aether:
توی این آپدیت روی مسیریابی (روتینگ) و اتصال از پشت پروکسی کار شده</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/5001" target="_blank">📅 03:22 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
