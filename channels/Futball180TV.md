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
<img src="https://cdn5.telesco.pe/file/PoUlvBa05GRbPf5Elr3w4_gx1mIswz2U2oMjBLqwSX7n47LgWccWx6r_p3nH2NNjsaBWI_fCpUK4_SQJVV6gvJQ4rE961xHTnl8vk0WLGAfD087BAcY9Bvdiwvcn9G-dTDCSfX4PN4WPyTAiM6KeYZsD5QZn9pi-9DfB0v5qGKHdxw7rqgUioL_SFSuza9GM37h3h2DbhRMg-ZQGzaSb-muhGiLxhuQpkfywUK7jbSWE2GC5rMbLZTv9B9YBjHf3sPtWCFTAwaBwoecJbnHTrlhZSxVJGQlxC_3_WdG8WGnzlPRIRs-HOvZ2SlJz5lcpGATYh4Ki62JDTaUNgOV7xQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 203K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 09:36:20</div>
<hr>

<div class="tg-post" id="msg-91124">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06eeae197.mp4?token=dMu1OamEKfTNa5E29ZfRsY2iqfE3o46rPQVVaRI5vt3lBAwcuWSMIrKhC8VTlgtsb_BYrI5ISEzZ9DBlVmo8sy2nE45nn8sIScZD6v-V5vBJTUkKXHkY0ib_MGSEPWf2AMhC7ZOHvi2q0hOjidyGDisEYljYKNexBMhV3932Ekwp1yEMtdQCsWLDaVHm3AoLwzsq_8byl4oauJiNqXUWWKoTqQft796V5AiOqPJ55IuJU9hknUYv0yJsVEhrOE2YDGVwSVfPo91NY6_KmkIOl6oGrnCNApzSB8bLju4VlvlsKWmKdlLQhgsi1I8qOpDCu3BoiDUEn3OmRClIndSvjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06eeae197.mp4?token=dMu1OamEKfTNa5E29ZfRsY2iqfE3o46rPQVVaRI5vt3lBAwcuWSMIrKhC8VTlgtsb_BYrI5ISEzZ9DBlVmo8sy2nE45nn8sIScZD6v-V5vBJTUkKXHkY0ib_MGSEPWf2AMhC7ZOHvi2q0hOjidyGDisEYljYKNexBMhV3932Ekwp1yEMtdQCsWLDaVHm3AoLwzsq_8byl4oauJiNqXUWWKoTqQft796V5AiOqPJ55IuJU9hknUYv0yJsVEhrOE2YDGVwSVfPo91NY6_KmkIOl6oGrnCNApzSB8bLju4VlvlsKWmKdlLQhgsi1I8qOpDCu3BoiDUEn3OmRClIndSvjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
👀
خنده‌های نیکی‌نیکول زید سابق یامال به رابطه جدید ستاره بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/Futball180TV/91124" target="_blank">📅 09:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91123">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/806ce63d62.mp4?token=OmdJLl82YZub6ek8gkx22PHRwexpBtQRUl2sT5NlW0xeJW7IJrnyGbHCahpr9vkVBcwT9qirBb5XGK-0CCSM5dHH6Z41xk7yEaQPN10Pit8Eb3hWZta7oypfnuvKzA2Nsy3IPZC_1rP5_i9NuIJYFcowCm3_7IURUfRBwgPoCXcLpCc0qqPPKSWtCoyF3MV2vlsUiezpyelkvKZsmvB9E46zmiLYYiwW1F3rA03whiFCk1uKADyZhhDkaQk0x9T19orWtXkv4e3r3B7gbzHodUJt9VJr-mQBVT-VrUi42H56430_X66gbde7BVkLZvfH-f_n5Wtwg0-AC2UnA6q-Lxi4A6QEfsGWPnIPm4m6J6b-STQlyWOkP9mCBXbXeu9fZT8npt-0B79azw1BkZnDANmoXHpsX5C9hn1NJVzTaIr8hr6qpThZ-IWB4Jt9I7xtecNqWTLf4LllO_rMA6wdxRHDzEFhs0ha9Hx6FLiYnHfkUEjT_azn8loqBo0_XBtao96sVtup2vx35TpjoLCkLPZQqGtELKL2ukHxUUnoX-ftizWwCT2_PTr8qH4eEMNiIZGB_05XlIl9IHXcYPfvdqlVNMKHqWpgmjCiQxR70xLW-vxlSrYlVv1pslngxpKeoh9BqAVssmMyHvBoybDjYeHcbm9l5yRnEWbioZiHpCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/806ce63d62.mp4?token=OmdJLl82YZub6ek8gkx22PHRwexpBtQRUl2sT5NlW0xeJW7IJrnyGbHCahpr9vkVBcwT9qirBb5XGK-0CCSM5dHH6Z41xk7yEaQPN10Pit8Eb3hWZta7oypfnuvKzA2Nsy3IPZC_1rP5_i9NuIJYFcowCm3_7IURUfRBwgPoCXcLpCc0qqPPKSWtCoyF3MV2vlsUiezpyelkvKZsmvB9E46zmiLYYiwW1F3rA03whiFCk1uKADyZhhDkaQk0x9T19orWtXkv4e3r3B7gbzHodUJt9VJr-mQBVT-VrUi42H56430_X66gbde7BVkLZvfH-f_n5Wtwg0-AC2UnA6q-Lxi4A6QEfsGWPnIPm4m6J6b-STQlyWOkP9mCBXbXeu9fZT8npt-0B79azw1BkZnDANmoXHpsX5C9hn1NJVzTaIr8hr6qpThZ-IWB4Jt9I7xtecNqWTLf4LllO_rMA6wdxRHDzEFhs0ha9Hx6FLiYnHfkUEjT_azn8loqBo0_XBtao96sVtup2vx35TpjoLCkLPZQqGtELKL2ukHxUUnoX-ftizWwCT2_PTr8qH4eEMNiIZGB_05XlIl9IHXcYPfvdqlVNMKHqWpgmjCiQxR70xLW-vxlSrYlVv1pslngxpKeoh9BqAVssmMyHvBoybDjYeHcbm9l5yRnEWbioZiHpCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇲🇽
هنرمند مکزیکی با آهنگ جام‌جهانی این ویدیو تماشایی رو ساخته
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/Futball180TV/91123" target="_blank">📅 09:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91121">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1Fj-KR3eOvkO-X11__cNhS4rzG0d7VATK6SCJV0AjCKQMvWzy3vn7a8nmiGIBO1lGBG4xrMwwiSlsNHs1-mWcWgHfZre42BZKkL5KOnvfgoMCzcXpDTwVkvUP5SZ4e1cxXNb7VUimjP6dIAokKAj7qA4GpV813vpT7GJDzYrmn_GHRXi-nAo4wR4jejkwXmHQF-iZl-pZY0aJ4a669vqJ29_CS6-ncWe-xHsNv43-iM_0gFC0n6vCOKsPDIr6QtYBYliJdVc31vJ0Ny4S5rv4t-fxUIh_o3b7ZbY1AOk7hxdDHaZ9BB93Vcx5KZog-idtOTjx-O5g72102v9jQVnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfsMXgnJWi7nGlYMQP-nGNtR9qBh6xLBFnYYI1KpVs3gwD3nW_eQGWErzFkKkfLLHl7T0aysCFo-Em_LC-NDFhuT0pwBas0-FEQHWBbOUIbiE4Z4YI3qI7S_6oJCmImPCcYE8h7EtRuT7SoDNelveProXCKLDi8TweUFGQJp45fc00kqGWJ_Xd1FdFQhHHCtd-iy6Bem_jbW8_1oQKWoX8i-SZEXZOt1x4jOdQqpUKEpyR_2tgYcTYgmATomseLQgzeyG3mOuU-CcjOZrZEn1SmAhekkqlS2CHqKBjm0YADog-gTSAbhdzZV3E_4PvoX60wC-ih2nC5H7E3IB0WP8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
امباپه: به جز هواداران بارسلونا، همه قبول دارند که رئال مادرید بزرگ‌ترین باشگاه جهان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/91121" target="_blank">📅 02:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91118">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇪🇸
ورود کاروان اسپانیا به خاک آمریکا برای WC
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/91118" target="_blank">📅 02:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91117">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: پرز عاشق و دیوانه اولیسه هست و برای جذبش هرکاری میکنه. پرز گفته این بازیکن منو یاد اوزیل میندازه و شدیدا میخوامش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/91117" target="_blank">📅 02:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91116">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3j5TMGdgCAhV2Pv5o7GDLoVu_gB8cxON0Nya6yURXDi3kCx0arzpAN_mSvrAedHmTHifmVSjXmNEDKkfc45479lIukioekiW-j8ZGwoqmIqa9do_nGgLWnh8bGpJ1XUzeuizmAL8htx_g2k8emeWGJMQrIdzhCX2GsJyfodLuUvZM2H6YHg-cGdoKkCRf8jjxl8ZvePp17Rweh_2NTUK8fWk7G9be5lYGpv1NT4UgCu9NCiSxplf2q9suY9vosLxMksmtC9MuT8-GVHYgAqNSA1xqP7iAsQkldKlP8N2D4qfLMeLGtxOoWhw07YOeBIGYjlk87tsdp5DnCB142jZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇩🇪
#فوووووری
؛ فلورین پلتنبرگ خبرنگار آلمانی از علاقه بایرن‌مونیخ برای جذب مارتینلی ستاره آرسنال خبر داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/91116" target="_blank">📅 02:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91115">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: پرز عاشق و دیوانه اولیسه هست و برای جذبش هرکاری میکنه. پرز گفته این بازیکن منو یاد اوزیل میندازه و شدیدا میخوامش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/91115" target="_blank">📅 02:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91114">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🇦🇷
❌
#فووووووووری؛ رسانه‌های ارژانتینی مدعی پارگی رباط صلیبی خولیان آلوارز در آستانه جام‌جهانی شدن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/91114" target="_blank">📅 01:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91113">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🇦🇷
❌
#فووووووووری؛ رسانه‌های ارژانتینی مدعی پارگی رباط صلیبی خولیان آلوارز در آستانه جام‌جهانی شدن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/91113" target="_blank">📅 01:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91112">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKempgzb4IDdo-lCOAhO0-JMj8DOsbKlTs3_Rx1R0uotfaTASr_Zond7_aHkptTkIuEOygx3stIIubNgOoPs6NXy0jYMvz8EzF9wu3Jvaf987sEm0AV-VLDikcig7JUm614cm__CRrJO-w-FPld7BR0rCnM3VqjVc_OpblYxwhfsKPog8JNN8zz4u-HFQkscq1vvOeJ6imFAs3nVoEqFDbbqehIXcZelZtDAM9A2PboQTwE2iTrqqN_T2Rr5S-8mKl6D-Y9UBS4LV4J-D7HGjH4p7sj7YVLCN7JMNZckgjCgj8F18Md9_U1Wu9cP6tp06V3i3TfZPhlkEHlptzsZ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
❌
#فووووووووری
؛ رسانه‌های ارژانتینی مدعی پارگی رباط صلیبی خولیان آلوارز در آستانه جام‌جهانی شدن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/91112" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91111">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MktG8yM56tM07r-KrhT0mvzu1K2zogyYISs829eHMKG57zvUZledcWcs0Y_JhOfY7P7xQz5vI09K5w4AAvsMLC2N7mBXDs66RppN9hVr4tk-TjK8RPl6xx5NKsMv2j3c6jznY7nBv_n-VyB3Nw9MLNAsCgDj6Nx-HMy0VEXmIvLtIh7czBz7XjPw9nW_fX7ZWKn2dC5M38zPF465Umt-JhuLzyyvbP2VS2dRK37JFKdWGiI1BkVbKPAjhyoS7_ColyYJ4ccaKnP9h6CvQxSEaF7__QWQo0eQ_LkSaYE_QZKIlE4FyV-f0OzgJKug0PgogyFgwtWTptfjPM9rx5zdGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت
؛
✔️
تیم ملی والیبال تحت هدایت پیاتزا دومین تیم جوان لیگ ملت‌ها
❌
تیم ملی فوتبال تحت هدایت قلعه نویی دومین تیم پیر جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/91111" target="_blank">📅 01:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91110">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_2P8bSu1dgqGwGJBYUZiCLRR3bktI4wGbIUmdA_lFTj3Gg7AEa8RUQozy0N4UcQk_GgioR1e3nQeOD4joczZqNiLbROyCNKnmcunTaaFPmHt9qH_fdLMuxi9QtBde-rPTo3tIFGpcHIeMUZPbjQekZAnNzAIln7ocw9M6DtTbUEdgFLk8-22wghDaAKDWpbh7nqQcq3amB8TPFDf29zAJc5uUvPq0kYReSqqxtzccpFStlDCcxruNiVX9NBIT82PO7kFJ0xSbaf1Yn8o5mnQLUg4LRvlOrC2g0OX7v937MGgvR_d0iVHPnq7sUnB_7PCt6DBxjM6UT0PRFVVNuzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🙂
🏆
هر سری جام جهانی میشه یادم میوفته تتلو میخواست جام جهانی ۲۰۱۸ کاپیتان ایران باشه با شماره هشت و ایران رو قهرمان کنه. بعد پاشد رفت تمرین استقلال که منصوریان راهش نداد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/91110" target="_blank">📅 01:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91109">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🚨
موزیک ویدئو کامل شیدا همسر ایرانی مورایس برای جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/91109" target="_blank">📅 01:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91108">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjCLtEjhx9MES5c_jSZ-DspolCpiUQ98xoSqWZvsEmbBAkYHDWwjjNzhT5JiznB_iDVuqcJSR2taqRWkYphHlO-pe0nsImXgqPehTazCnyFaeu-aofyNeuGo8BH8-fxdhvIg4r3nCC7yOgLZJyzK21o3HDJhvX_MQs52zmJ6yocwhQ2mzDgy1tEgqFkQuO7CHvmjDc_t2sGWgERUR0aFaZ0g3ShPHdHxVn9T5oucwa1VsAxY4VXS-_JtO_BaUGbzqbJzuPHrF-ECphP0NNFA8cB5pfxoid01IzgbSsJ4gs43j6gM0mI0vdTUqa80wzxxrKgbPIJ1ML2ftXaTwuBNYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری
؛ یورگن کلوپ اعلام کرده که در سیرک انتخاباتی ریکلمه هیچ نقشی نداره و الکی اسمش آورده شده
❌
هرچند رائول به عنوان نماینده ریکلمه مدعی شده که اگر دوشنبه رای بیارن، مذاکرات جدی با این سرمربی آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/91108" target="_blank">📅 01:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91107">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
#فووووووری
؛ شنیده شده بخاطر توافق خرکی و خیالی، پدافند خارگ فعال شده و سپاه داره موشک میزنه سمت تنگه هرمز
🚬
🚬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/91107" target="_blank">📅 01:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91106">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpIL_1pEqEhyp084TeXTYSC98kwhvEDzruKmqlonaKbbLaGbMAWyoimqyjyVRtVy6VCRUeTcDPDt1qejOkQEQMHFjE7S7OCdkmskb43OLTy4fqsA1aIOShSMJ_7e874fitTTYHvmI-XALCT_PPt9NBfWIocHcAEemliIUaTV-3ioGlDZZFcq0zB2F1rP5WJLfRxwoT7lfXazYu8rbHhSUrMLCBfR1KkjytfCtBsyvAq63MKlC9dRJ1t1e8VPfb_ptYHapgcpgH-EPI_nfh5LSNhTOAskuOSk2tVMrJM6LV4u49gkkXvklbAqO8ZKSenFwPypDHNxbrSAQ55rlQsW9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارل 18 ساله به دلیل پارگی عضلانی جام جهانی رو از دست داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/91106" target="_blank">📅 01:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91105">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/KnvF7uEZORIc5CHKe8ywUJ8skTEeHyWkbn7ZnU80WujqYI6wHROu2otj60Dtz3OzmwZyQ9LmYA_yEvAkHMaBWbRYn5zVNwncQtBhYyR08YZAMvMrQDVptxZ7OFE6IgROBCUQdRMwWa0j2emNT88kY68hXjIariglvd_h10B25owj1sCqcpcjVH8UGY2zSx-wXVNKQSmkO05vUTPtXeNE_mfM0hnt_LcjERj-_8A0CjLgRhCNZZEcFf9MluJXEAqJSDmf1-8BQVRV9yFxJPGJicSv8HGPXb_KOYVKM4iALCe8S0aWa5qGAqDbntiFkGDJDdxzkA05VLat0itLrORCXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووووری از رومانو: لنارت کارل جام جهانی رو از دست داد!
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/91105" target="_blank">📅 01:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91104">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
فوووووووری از رومانو:
لنارت کارل جام جهانی رو از دست داد!
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/91104" target="_blank">📅 00:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91103">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMqhqjn4wId8418VU6GousgiGEp2zuleRRmp4pWFkUqUcMQ6mhQIxNgUV4RNzycXTbTNi1goUjOO5hS8oqgBiKTdyPXw3ffLvdHvQncM_KLELPC_OIfIbTJW5OOL1L5gKjetS0CD7hkR8oCn_URwn2Kjxfq1o6eoCQbl0-qoBXsAdB1HQPCjey_Z_kUAqvDCT8PeT2mirQOZf57Q52fmHPCQmL_0u01KDU4cQZcla0K96WBF2BgemHBHARB3vlTLIlzSgLzXYFI4iCgJSBmgXo4GWpK6_5A7gYJgaaYDA2nZaGAQcd2agZ0v2YJ6upL08r3oT515QWTJErhlTZqCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب مایکل اولیسه به یک هوادار رئال که ازش خواسته به رئال بیاد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/91103" target="_blank">📅 00:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91102">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f8ee5741.mp4?token=halSPKyIRrEGuPQYf6JcwjDUR_3ulQvN4NlZEZK1C8qijyMH5NXCz3UG1t2Uq4VeyVh70ulIsiZeLmws1BG550Wrs2i11Nsnz2Aw6HPzhQB7YHlr386mUrFXBVChVxPlWriCmbxqnhsC-OtQZbdBrcDNhwLKcRMQJYVhZFh5jRhPxjIqJju4c_ziArNFTeun-LGJBmCaqVLtFmW7RHKnZupRNEcuyXVtOlJiB4hpsZ6gFgt5yDBFMKTdqZY-04D0J8qztC-2YI1b56cicNkOoKvpVSEZt1kDHnErBkcxcpVed9PwZG3Bw7sEQ8uUwufu3roAFsiea4thS9QK5HwtC41jnELI2SGJrf8v8B4ErARTYBzGkRQjaUptATvw0QBkoBIytV1kXZH0jBKEtfYvSPZboV7pJu1HXEfzyO-sh8YccIJJxHLd8tWGzijpet_VFYinak-cjPJ17ls4QlOL3P02O1dUHaDN_-_AblUcojU29XN-X-ZknMTTF_fE153uy3E-FX41GISOfT0bmyjcLih4aXvveiDc5UG0r85YFhM4AJdBRpLH1j9OrILU0IlvkzneVn4TXzCi1uSppuuuhb2ybdyyNgz_f7oaabhok_t_VyvAeWXbZRRE7r-shCQeYxaqQCJp362xOhdafVsua54DZBQxtzwp9i9dUvFU5pY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f8ee5741.mp4?token=halSPKyIRrEGuPQYf6JcwjDUR_3ulQvN4NlZEZK1C8qijyMH5NXCz3UG1t2Uq4VeyVh70ulIsiZeLmws1BG550Wrs2i11Nsnz2Aw6HPzhQB7YHlr386mUrFXBVChVxPlWriCmbxqnhsC-OtQZbdBrcDNhwLKcRMQJYVhZFh5jRhPxjIqJju4c_ziArNFTeun-LGJBmCaqVLtFmW7RHKnZupRNEcuyXVtOlJiB4hpsZ6gFgt5yDBFMKTdqZY-04D0J8qztC-2YI1b56cicNkOoKvpVSEZt1kDHnErBkcxcpVed9PwZG3Bw7sEQ8uUwufu3roAFsiea4thS9QK5HwtC41jnELI2SGJrf8v8B4ErARTYBzGkRQjaUptATvw0QBkoBIytV1kXZH0jBKEtfYvSPZboV7pJu1HXEfzyO-sh8YccIJJxHLd8tWGzijpet_VFYinak-cjPJ17ls4QlOL3P02O1dUHaDN_-_AblUcojU29XN-X-ZknMTTF_fE153uy3E-FX41GISOfT0bmyjcLih4aXvveiDc5UG0r85YFhM4AJdBRpLH1j9OrILU0IlvkzneVn4TXzCi1uSppuuuhb2ybdyyNgz_f7oaabhok_t_VyvAeWXbZRRE7r-shCQeYxaqQCJp362xOhdafVsua54DZBQxtzwp9i9dUvFU5pY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">First dance
❤️
Last dance
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/91102" target="_blank">📅 00:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91099">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e5rluRmqOEQyXoyurpaFvOK9ZImLrh9BfsaE0acYpwEmXh_4VqRD7jLrESNEUsAG19MMoEebzllLConGAXdMajli0sHFl0NLJgmfot_38iQiFxRQk3vTd4ykF7ozm3jH-dr5LWxvq4m3s0RPphROiK_VXwjsogmSDvQYldoGR-1faM5iFbbidB-av7CKUTJZfiaLbhsQ4-trPtwU3WkxJ0rc49J_GfUkHWz_pTQHUzaANE-j8kfGc7cadNw3621NAI0yg-DGLBrihaFXceBth54h3WFaQiPHtulw4Sdyt1rvuxdnfAElWqw9pqSSeNcmgrGJedDLWmT2hsSjShJs8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CneoCr4oz0gBih6dXfr6dHxbrH0ym0_Ltr0EA_vqZLH9KIFUNXjHXucCHH5hpHWvnTKNmY2kK6l3BovYdtVh3DN75sIzX82CmUaRxlViqEO0pKA66x55S9pYDPlT5Kh4y7uVtHu7OIgyImzSBSlUCAYCLBVwcZH6ji-e49oxWaIdZ6UvHbQG2m0yIa-ZdOnkDEhk8aTK0Xq2asp8GgvkGbW3VWyo3h0JMC78kSz5FZzZWIZ0kx8-bnMH83_xsImLx2pxQWo0Zw4QLETLQ1xRLg3-x39E7ffNrsJxtcF04RrSGM4H9l_DMO-lkOeTCYDd8f1Vac_bKsjPEVaGw5Cfbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V_cocnUdCQhxyTZTRd1wYRJCTvq0KLzdl4Pll1rXHmkk8toPNp6Ba1igWs3oeXKq3hDkmFybmYzhZXsmPsu1JSL0AhxA-mWGn6Aa01n84QyP0slfmeAnik6714kZ3AgOYrMLU544MaPpAaAMFdI1n8M5IfIpoVp7XdUZSwrqjJiUqFxlOliMZmqJ3RwQYBgjZmAuyxfQD1m7Zl3FGQxTlF-lwQ2wQN2XuGjpD3aqqN66evh9GxRqWVU9F0dZ6jiBCgZlbjz25tMn2sesB0H6OK37hqhN-b7j2IISoSO0dqhVrqTwfuOguNaIJ4Oo9Mf9A0bS6e4HuwKxXBTfQ1M9AA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زید سابق و با کمالات وینیسیوس
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91099" target="_blank">📅 00:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91098">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFVHGRoY07MQiFdONov6VeF3dK7MPESSe18X8kffbyiXCU14ihWCAdEPxV0ZqWv4qikCHKwX4NQ8ZKVMAJbVy9RGCbnWS4a7N8ukRAGTqXBgUzcV2SopjRpiVF74BI7FssffwnI-Bel5S-X81KEnoOYs3Zn_-5EY_3yUj76z0tOs7aUZIvhDAuASmyFaoE7sJoKOR50DzV-aqPQCJ7fPNxK7uklV6FhpZGIycI6u1X_HJ126pJbui-TdRWh0fjjNLykC-ZlK7CZeLOiCOljQVEQZmboceWBWaK-GSThImuy7MlKI21i2sze7FpKqenCJ39S6-1-tleWXr1KXFvnhyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوتبال همینقدر میتونه بی رحم باشه
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/91098" target="_blank">📅 00:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91097">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJGjKjwdTnvqsf4h0TwFB8tv12-WggwoGLS3CUKpOTPqrj_LkQfN0r5LKiYVUFaUG7cLoddWIlVzc0tAi2eg_LN7x9yzDam8dvLwRWXAj5j7wvCjVM2P1XWsKrYNpcHa8kqVS2VRSSxkb66J2f3rrReH1c5nfp7L2bD9BuOHZZqzMRR4z6IR3o46j_reYrLCK56b0W5ddMbNZOD8uWUNUi731ukjIZVZ3TFzK5qmUy-L38EVv8IojnbN5AmkfUVo1kQ1soOPoHq5gcJWguhvT4wgRtuCjhDT89g400ZW0S-zL_kduIzIYFdb8mQSsIMctm_mkvXDBZjDNUV4dQA3iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ بازیکن تیم ملی کلمبیا در عکسی که مجبور شدند قبل از رفتن به جام جهانی با رئیس‌جمهور بگیرند، لبخند نمی‌زند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/91097" target="_blank">📅 00:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91096">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
پلی مارکت: صادرات نفت ایران به کمترین حد خودش در ۶ سال اخیر رسید.  @News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/91096" target="_blank">📅 00:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91094">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KNj1jpq7KBLdfItDmhBzwo1WlxaBqk5_oxuetzPAP_kh4mJW7xJpzTvMYPhNQ-2KQe8b9mff6V6_HW23p9diX3SZcEEj1yQWVKmLMnOubtLlIhyKoGOWI2O_XY1rhkdaE_hzHR2Ze4VGK0fkdnjbVlTI8iNojyVnt8Kby7KfTjl7kdpKEgJcz7YodDlHrEFxuo_4l6HOQM_Y1v3T_DjswkaPBaXa_uhqA5bWBxTCaJVZyb9G1s3FtcCHwsBAA2jVMcPP1zUMgoN6e77MCrTpPix3hTtVB9hFP0zebNHmwgO653Qktm2qCfl3NZtsJMXZz5-th_3DUP1SLdg6MZyebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OoCebaQOeeFkoLJIBuArAq5tu4LQWZWZ1rSBKm4KhyFRmoxkJlIHYAEs2B9Oi7EgPbFkjXoxp-wFaAMafbQvt_LbqOT6Q54mls-dEUiWSRUSFeLvx6COC9H0hUTHd4w4p69Dm-24wcyFlfxDXde3iMoGbwnOBTH26Arm5uSWOThZH_PHl7_0rFSJNc8lq8Ymgdrn6X33FIJGHRM_lpCqejxS-Jpn2h_RHUhBPSfcOugeD6AD1eIz-K7HGO1ebWMn8KihFo4UrQIkOFFATZOlUJIvXnZLeI5ZuD0x5Z2t2Nk-Gq8CK2KGGv9Dvp8_JZgA_R-C3FgmzXNIGBvxp0x9XA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
انریکه ریکلمه یورگن کلوپ را به عنوان مربی مدنظر خود معرفی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91094" target="_blank">📅 00:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91093">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🔵
باشگاه‌استقلال با محمد خلیفه به توافق اولیه و شفاهی رسیده است اما این گلر جوان اعلام کرده که پس از جام‌جهانی و برحسب پیشنهادات دریافتی دیگر خود، تصمیم نهایی را خواهد گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91093" target="_blank">📅 23:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91091">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZOnDKfIvzhtN5kYUPXKSNx_KDfatM5D3h9g4SNosXl4GfshLkuFkKuQ2xE1woFGDe3n98wYD4JI-KbA6z5z71fdT7OhrgPuKSIuJGB_0AO36jjqPrdm1Z2AdMh15eZ4fLH16ELmkh8IERjqtWIreMUTuYhCivwtsiQC3bISoBUlnhAy1ide986ZJ_7RvUITPovbMAqLlxrO8TOXHpPEjjccSvuw89FLWzdfWrvXQBOgD3DBrp3eWfVwbJWMBuGSq2bFVsw7Y62BxXfRBsqxp3X7VwHoC7jSPsK_jtO0AhERjaH45wa8bt2GVkBIpkOK-WW6EdrTWM_HLq-2SmN_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار بهترین بازیکنای این فصل پنج لیگ معتبر اروپایی در این فصل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/91091" target="_blank">📅 23:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91090">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bd3GXNjy__8H0ovLFBrHcKpShs1MQHemrCtXbxuvPHOrRj_jHF3PUcbpex_At8HhFcZBAMYwKjfztCT1Zv7xYzFOO-azfLcaYIFyrT342NKWNQhHwWIkTwhFbCFKz2k6sahX25UaZ76afJSJMDW52G0t5gMtUXVP1niqYvW8bJW7C1CI3d3ftdls7m8ovgtK7t5d5yiDKaYMj83R6p2yzEP6CXyTTBVthL6CxlrqbwGCxvz25I_6VPBiegZ82xnjWv8HhUb8JvXKytsBKi1t9Qq-6R1hpnacaO_L-J8Lopdh6g72N9NMzCTD3a0dcKw0QgJTyNzGMWVBUJsCtplOMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
انریکه ریکلمه یورگن کلوپ را به عنوان مربی مدنظر خود معرفی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91090" target="_blank">📅 23:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91089">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎙
تاجرنیا:
آمادگی هر تصمیمی در خصوص لیگ برتر را داریم اما اینکه لیگ را نیمه کاره بگذاریم و قهرمان مشخص نشود این خلاف عدالت است!
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91089" target="_blank">📅 23:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91088">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696197860e.mp4?token=mXYmOzuve5HTyshjM4HQCYZhJh3ONz1ASHP60VKimUf-0U8ggwTgaUZimuiTJF2zMg01zIqMGyCV-zfPYOxG90tzEqc6gp-QMNC0Wxj18DlfSoTUXVp1czTsrNqfcgIaDeF0qjfcgjFfqjkEHvltXdVvFtro8-rzMYFX7GjDB72IIREdMeZI6pdGZKPtwuz6PiM6JGDnO3OUy50zmrL8zH9Hi74x3m1zzUv7xQ_nakDy2vSpOuGFzEmzgmZDiR_DTk5I_i6ayGXvdDD9h1-9wzlzLLLFYEaM_NSusDC4mTzfrNjhiyVjalFFFnT7g662qz8oOZXKAtfOhwAdk1Sqgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696197860e.mp4?token=mXYmOzuve5HTyshjM4HQCYZhJh3ONz1ASHP60VKimUf-0U8ggwTgaUZimuiTJF2zMg01zIqMGyCV-zfPYOxG90tzEqc6gp-QMNC0Wxj18DlfSoTUXVp1czTsrNqfcgIaDeF0qjfcgjFfqjkEHvltXdVvFtro8-rzMYFX7GjDB72IIREdMeZI6pdGZKPtwuz6PiM6JGDnO3OUy50zmrL8zH9Hi74x3m1zzUv7xQ_nakDy2vSpOuGFzEmzgmZDiR_DTk5I_i6ayGXvdDD9h1-9wzlzLLLFYEaM_NSusDC4mTzfrNjhiyVjalFFFnT7g662qz8oOZXKAtfOhwAdk1Sqgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل‌زاده:
امیدوارم فدراسیون پاداش بهتری از دوره قبلی (حواله ۱۰۰ میلیاردی ماشین) برامون درنظر گرفته باشه. ما همین حالا هم کار بزرگی انجام داده‌ایم
😂
😐
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/91088" target="_blank">📅 23:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91086">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fb5b6817b.mp4?token=ihYuuVipDC-RU4PhBc6S--XGOVtaKYfiwmsRqBt4RJaAeKyfJTjUZK55bvofd8vR4qx7zCC9A5y6isMKokKItMf53or22p-sPz7h3yQ5SNidcCmO0vBZxK2Pl7Wjbf0uWk_xImmUureQ4cASVYOCTW9UrYgAtDAffKS8JaPjIXoMiJZNneoJcJ8sbyKCR--HtHPcgMEjGfcmCi66ZVe7qpo4cZkh3F8iLFCDTYvb-atGaz5RU1W4o0aaphairiuOsPNvoZxL5M1TKRSZcXpyrvXCWphvul1yG5u_hrMhNq7AweW3PTZjiKKT05jGVrEsIweOKXmkh8aCStLbPHgVBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fb5b6817b.mp4?token=ihYuuVipDC-RU4PhBc6S--XGOVtaKYfiwmsRqBt4RJaAeKyfJTjUZK55bvofd8vR4qx7zCC9A5y6isMKokKItMf53or22p-sPz7h3yQ5SNidcCmO0vBZxK2Pl7Wjbf0uWk_xImmUureQ4cASVYOCTW9UrYgAtDAffKS8JaPjIXoMiJZNneoJcJ8sbyKCR--HtHPcgMEjGfcmCi66ZVe7qpo4cZkh3F8iLFCDTYvb-atGaz5RU1W4o0aaphairiuOsPNvoZxL5M1TKRSZcXpyrvXCWphvul1yG5u_hrMhNq7AweW3PTZjiKKT05jGVrEsIweOKXmkh8aCStLbPHgVBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی در تهران بعد از جنگ خرداد 405:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/91086" target="_blank">📅 23:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91085">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ew2FDPlv1sBMEZHtGH6J9awUv9k0rmReX6vCnrqkCM--0N95q8V2k9J_ZSg2_iZ0HSm8utyuBSpq98Pmk-02CclLLhJfVz1OY0tUzQxvSZkp0BBgRNKNGpit3jImu5O5Y67xgtMfASmP9W-kNtzr2kqAML9WW1YNukbFgr_EWby1kg5OS1jyhy32XVFdpYmTACLHMO6kiWTSjD9HtFlnLvoUr0avSYcZXxIDzUTU38WaTRnFqM7QQncZWQjbrs3KSM1R_v9n3NHpWMVSXWma0EjbSM1rkB341wSfCEeHdcgW-sHL87bDRO3k68JB-mSzHyAXky7sJn-RomYx6WYKLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
موزیک ویدئو کامل شیدا همسر ایرانی مورایس برای جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/91085" target="_blank">📅 23:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91084">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
موزیک ویدئو کامل شیدا همسر ایرانی مورایس برای جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/91084" target="_blank">📅 23:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91083">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwQG48CoxGa2mIsb_X0d8vUZGxw4tWpZ-qftZrCvPjFOqfrZP540wF-Mtx3T0Wm1TEeFBGTJPqb3VHstmh3TINlkvmm815KwmKlLRNlcBbMD1q_pAFGXXVzbfq3676QdCXHqGtciklOSvomkRbUOt20IFb6Y5Edy9hueOqS7H1nHTWBcxmB05_lrs6EfDPkjTxayb6LYf5JHRJz4HmBALmCiMfRalOa6Ej7p92Rk6OIB2xEuRV2tQ1dYe9Jtvq7EuLwyRYUjNDvYZ5B_VevAHjGLo2XmJkz2cbM95DbgGDfk8vE4yuGuzIZehswFZeje8mbZaXJMSICLiGIUbRU0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم منتخب بازیکنایی که اصلیت فرانسوی دارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/91083" target="_blank">📅 22:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91082">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJftvnQ2UNxpoIRh-J046KE3UztshnC2zt2GrcqNhTzV_xqdBlys5gUpvB3cUk-DFldI3UxJ3Bfu1OrOlZPAYyH-3NJesEtInBL0keEPdMsvXKKo549ntY3RqorQojlSGlJqZRtvi4pLVsMOiYaq-u8W0xcJ2A9DVYYC-LdkABpXg8RYX2ZVGqSPPhIQjXhhHs3NG3UZqabqg98GbE2Mb3ounBHRTA7CF8PKaSqF_8R2LX0N-O_XskkeJ3juy4iYyJndKN-ClfVmDVZm5Yd0kpLX1PqwLPr_ZATb6aoCB8xHg3Yz_UF2H6gQpiXoychIGKbY6yBB4QOIdqFzO1DTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه تماشاگران فینال چمپیونزلیگ 2026 با یه بازی رندوم از ریورپلاته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91082" target="_blank">📅 22:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91081">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tetnx6jTqqLs9VA8z2kSV10AsLxreGHRtmym4Qv5XdzAmau9bCiX_GvzlxxWQt26ZlVG2w-U74d_vilVa1a-8UELQZtByGPUlJ_U6AyiDzonzBaNEt8eXs0Wdm-ESvNV3rncbTGWb2hjAKdtNJd1Z1mMYzzXB-gZnMZpNhruecg8a4jVPb7H7UaqmwRBhaHQFPBHGBpMzqNKgY3DU9oziUo0gyYjEgA1B0SNBOea0Sfls2JiJuEQuvJo1CLOMYSI12oH-rysTEZZYT80BM-PDyVKoR1Ep_sYd0YjqrddZHbvkC7zVI-WSzruXVnCtRPFefo4DRTaB3H3Gb0Mqw6kEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برزیل
🇧🇷
-
🇪🇬
مصر
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه کلیولند براونز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
برزیل در ۱۰ دیدار اخیر خود، شش برد و یک تساوی کسب کرده و در سه بازی شکست خورده است.
✅
مصر در ۱۰ دیدار اخیر خود، پنج برد و چهار تساوی کسب کرده و در یک بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر برزیل  ۳.۴ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر مصر  ۱.۹ گل در هر بازی بوده
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از ۱.۵ - ضریب : ۱.۱۹
🧠
اگر مجبور به پنهان‌کاری شدید، مسیر اشتباه است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91081" target="_blank">📅 22:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91080">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/no2yZW2qVKzBBkbQudfz4bBVT1I0xPxg8Q0OMJqJXgAdcbwJdFU9Wno62fti0oVc7kev8cQAEPsl1U4nq-pAxIkQQIWqUUNTFXnz0di_EurHIIz6RgxWww3Hahugyd_aF4DgabvrY4ilkFoJoO1Qcu0vW25I4zefA6_qlFWvsu3r42uktMTyDGGIHhWUGGCROsx1-R3-RMOnJlkILm9TqMO8WSVhqHbgwV5KFNWEieoyVUjmEnOv3FArgjiXgqf9cDY_D1cvnhzMf_SpFynWnFmVgZHMgINMuXCB568AuE3PNfPmXU68NpobLChF1dhR_6Ji6L11aG9sSoQD6IHP2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکالونی: اصلا منطقی نیست که بگویم من اینجا رئیس هستم و دستور می‌دهم چون همیشه درباره تمام تصمیماتی که می‌گیرم با مسی صحبت می‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/91080" target="_blank">📅 22:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91079">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnyLuufDvWI-LHajq8u4gZfm94b70LDNERZDihnsrT-KXfRNHv7U6ackWP2LU4O64ZBSFd9mmLc78sMeo84i5xYBX5_vxZpt_xR9nNBzsItaC0Y3bKG2ey_BuhpX-ixPzk8gS71Fqspi1tERaoYS7HWJ8rI7A5Bwh-_Ec7zGy8O9h6tunQmMW56ghABFsmADvOc9d0g8Ylf9NCRrQbr7vEvblDSY18osHMRkTUjHQskFax3y9N4oMuW_USpSwv4rohYRWIsB1P1nvStlMZpIvCFJ44VB3owkZ7CEJnaFzshtLlYAKcmKJt1iH_RCkXejEsoykQXKnzF3Azsdxszftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین گلزنان فعال در جام جهانی پیش‌رو:
◉ 13 گل — لیونل مسی
◉ 12 گل — کیلیان امباپه
◉ 8 گل — هری کین
◉ 8 گل — نیمار
◉ 8 گل — کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/91079" target="_blank">📅 22:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91078">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f50084c22.mp4?token=VMjbumn3-AkjcKkw62kUsS86-MNxqWviKek6shHjhqVfTKFPzw-Nrq6_xHxPsL0R8yVkvCgn81VolcwxAPMeuneak9JFyOqEvPtvvGLfpQMoL20MVlZdysZf1YgaCpjJGx2E_3xrFBlfbCk9xvki2z5fcEOe6jL11tOnnngYd5PJd2vNiqLOLrbx80yGMxCUbHkYZqywXvkt0mnLUjjMYeE8V40o8p72t0eBiFNJgVFbUJKFyv667mT9bnJxVQOZZIuIsrz46gBfqNQDZWVaaSk8UwHA39riMa9dH-Yt-MUjNfXz5tUnah3lcOy4oRyHgQJu5zgc8NcAOtLVnuar9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f50084c22.mp4?token=VMjbumn3-AkjcKkw62kUsS86-MNxqWviKek6shHjhqVfTKFPzw-Nrq6_xHxPsL0R8yVkvCgn81VolcwxAPMeuneak9JFyOqEvPtvvGLfpQMoL20MVlZdysZf1YgaCpjJGx2E_3xrFBlfbCk9xvki2z5fcEOe6jL11tOnnngYd5PJd2vNiqLOLrbx80yGMxCUbHkYZqywXvkt0mnLUjjMYeE8V40o8p72t0eBiFNJgVFbUJKFyv667mT9bnJxVQOZZIuIsrz46gBfqNQDZWVaaSk8UwHA39riMa9dH-Yt-MUjNfXz5tUnah3lcOy4oRyHgQJu5zgc8NcAOtLVnuar9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگر: بازی فینال NBA که شما می‌روید، ارزان‌ترین قیمت بلیت ۸۰۰۰ دلار است. مردم عادی آمریکا نمی‌توانند این رویدادهای ورزشی را بخرند.
ترامپ: می‌توانید آن را از تلویزیون تماشا کنید. تماشای آن از تلویزیون تا حدی رایگان است:)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91078" target="_blank">📅 21:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91077">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
رویترز : ویزای آمریکا برای ملی پوشان فوتبال ایران صادر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91077" target="_blank">📅 21:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91076">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlRrDEkQjDnfuTFrKWX38tOceA2yBGEReM-0-QurDCx98YejsKt0k88rTKsSG4zDmTivoh6D2T8aAlmHQNXHz_MEWuxLuTw7crlnPGRD4e1KPJpJegfJmhIg7w7NxMHoqSeoIxa2hoSPwEafwzs3Rrlj3QxNshFheGiCxxacm9b4fYvzQ_3okIddXXgHUvWAJZheDY1hneHySvub_Wb0QXH7wgkDSmAp1XHpMpsyzpA1oi7X0XZQ6kv80-UBzKXP5ODHRqWJdzqnHCH3ZRLNCJ2-YWm2CRpttgscKWmXeUnVAXCZD0LlWtLVWREkrIr9lWFpnwiWjfrcDEDJ2Th1AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نزدیک جام جهانی هستیم و این پرامپت جذاب مخصوص کساییه که میخوان همچین عکسایی با کیت تیم مورد علاقشون داشته باشن..
Ultra-realistic TV broadcast screenshot, identity preserved exactlyfrom reference image. Young woman sitting in the crowd ata(اسم تیم) home soccer match, filmed by a live broadcast camera.She is seated in stadium chairs, leaned back, looking off to the side with a surprised caught-on-camera expression. She wears a (اسم تیم) home jersey with jeans, casual match-day styling, relaxed pose one arm resting on the chair. The jersey should look like a normal full jersey, not a crop top, not rolled up, not tied. Around her are other fans in stadium seats, blurred. Keep the crowd mixed and natural. Add a scoreboard graphic in the top corner subtle broadcast compression, digital noise, bright stadium lighting, and imperfect live-TV framing Telephoto sports camera look, authentic televised soccer crowd shot, natural skin texture, no smoothing.4K.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91076" target="_blank">📅 21:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91075">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
انریکه ریکلمه: بند فسخ قرارداد ارلینگ هالند کمتر از 180 میلیون یورو است ، اگر به عنوان رئیس رئال انتخاب شوم او به رئال مادرید خواهد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91075" target="_blank">📅 20:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91074">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e998ac734c.mp4?token=LrACYD7NwcujkkKA9hl31OLGFrCb3c54OJg_d9oDGL1-Q4tOxb8ZmSVZetv02SQdKkMWNqLfrYJZmU5G77229ZJwr310dQ5ExMxIeAs_V3HAAozBDWgW0TrQ6cA39F-EyQlq2v5zRHF7y_m4LLcrXgMN0Ga31Gcb_Cb-SlDhuzRrw-lJzJYUls_PBQ0yZRRgxo7VsW8Xk4ghWAWp-mS7qTg5TOpqSfUzg3uVCeo-SCVykbP7jD83DRq_hlesUDvaqfXtxHFGawJfsuZN2hMVR5VNL2fhIGpssG7xGBkfNAxWb3BkuBV7GuQ_TDjm-jGAtJEHgm8n6ALb-mVgq4nMpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e998ac734c.mp4?token=LrACYD7NwcujkkKA9hl31OLGFrCb3c54OJg_d9oDGL1-Q4tOxb8ZmSVZetv02SQdKkMWNqLfrYJZmU5G77229ZJwr310dQ5ExMxIeAs_V3HAAozBDWgW0TrQ6cA39F-EyQlq2v5zRHF7y_m4LLcrXgMN0Ga31Gcb_Cb-SlDhuzRrw-lJzJYUls_PBQ0yZRRgxo7VsW8Xk4ghWAWp-mS7qTg5TOpqSfUzg3uVCeo-SCVykbP7jD83DRq_hlesUDvaqfXtxHFGawJfsuZN2hMVR5VNL2fhIGpssG7xGBkfNAxWb3BkuBV7GuQ_TDjm-jGAtJEHgm8n6ALb-mVgq4nMpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
وضعیتم اگه یه سال دیگه ایران بمونم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91074" target="_blank">📅 20:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91070">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aphckmaqQcnm5otirqOPAlWPQKVLubxU4Pw9uf8HjIP3E5Bj1Zxfu9xA7-8dAb2K4jZeQK_n6IVphyiXcZFECVHAZeorrMMarWfos-Ly-j40Hp6U7mm-tT5PX-iiGd633BajviQeZuEZ4_OK_KH3RhDR0kAP1hdxj8G0T-Pm2gwVR90WQtUIMsLQVtQBH0i9dUdnRnH639AZsfrD1Z_Jj_W9dvCiHAPG8rOkPSr7VafaLmNcPnzzCi0XpwKfq0NzZ6I_XffOOftbCrtYDf5hA91c8QN5ZjGO9G304IOTf4GO0OM1gzi2qbMqWCyrj9ZftVSTzcJ8FpbCgrpOE_alMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال یا وینی؟ مسئله این است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/91070" target="_blank">📅 20:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91068">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M6A3P8CPbe3-oKuDO8fw4HSNtKW73Y8h3ndNjBLB6I5xaY5xGS9AC-UNwtxFJbcm5L3A5uo1_oehh7khC_WBQuyrptvie1wHKfgthH1wXZpd6R7U_AoMY_VLi0zAKMoOzRkuPxM2RKGmxBb8UohUuNHBIQj1tAAVYN9zxdGhufwMi0B9z-dnf4OHmqGNcde_7PFLtgYVrOgLLUKmkV5yIafQTsGDybE5bRPAjY3oycUQH0quhl6Cjaht4jmAfdONZyEvayysoSzbdt8fhMxGhxkquq_rwPKNn49mfMrP2qSKgZpGVhvwYAkosLWxDp4Ns6IZBx06108yAG3XWGrX0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VMEkrP6a75pYAysLaGAaq-rguqZrCXOSI6UXQaE_q93HVJWdOq_RMXv_dysnlbXbX1rahrUN5Z4Kwhg_PKZHy5TFRwZBgzWx8rE2NbOFlHhsjyj-v0bdIllZntEnF6YFba4UzDgTD4jrihS8am694_wlXCnvQby_L3EfwIMz2pqWRnkF5a1pKea_nuO7__K7dHGr7YqfxztMjeSETHu1JPUx3gPADFnp_NTsVffh_8hSjCINbP6BtYuLGXWK9XGDVRrc_Dlex67bWU6igmGMhFTmjXbrJa-33Bt4QWk6dF0ujzGZEp9b3yqJ6cl-mzLLE2JT5n3nBi2BwxQgFRpdSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز همسر فرانسوی انگولو کانته اعلام کرد که توی دادگاه درخواست طلاق داده چون فک میکرده طبق قانون فرانسه دارایی‌های اونا به طور مساوی باید تقسیم بشه. ولی مشخص شد که کانته هیچ دارایی‌ای در فرانسه نداره و املاک و ثروتش در کشور محل تولدش به نام فرزندان دو قلویش ثبت شده.
حالا کانته کسیه که حق دریافت سهمی از دارایی‌های همسرش رو داره. وقتی همسرش اینو فهمید سریع سعی کرد تا درخواست طلاقش رو کنسل کنه ولی دیگه دیر شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91068" target="_blank">📅 20:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91067">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ap3Ol1pMRuatjxgNk2u5xTY4OHtKDabYo3JlOZdkFVNlnZ6iCwel-a-jJoB4a3hIf4DjPg1QngurG-JtR7FvZ0jghbXobFvBpfIRJTPwySWRZg2JxygI7Hy_J-JqEva38fHf7R1Bp851Zvn8tn0cKGQ3RJoW0tIiif-M3km9MoytkSyiXqDrNximDKlIr5cSAuBuo3HbgC_RcV-GY3fU1Xj2Tkps_DhediqkgwW5eJOmKV9XL79VyIEsP7HF4GGVuGW6130ed2FICmifO3devkvldbKx8b17k9pYwLeD2nDR6Vd76Sf0Zdgfb7WzG98UOL_eFu5Acc1oVCurDaHX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خیلی هاتون پرسید بودید به چ فیلتر شکنی وصل میشیم !!
🛜
دوستان تمام ادمین های چنل ما از اینجا  فیلتر شکن. تهیه میکنن
🤩
🔋
حتی تو زمانی که اینترنت ها قطع. میشه  فیلتر شکن های شما کار میکنه
🚀
تنها جایی که مورد تایید ما هست و  پایدار هست اینجاست
👇
💎
سرعت و پایداری. عالی
💎
بدون  قطعی وکندی سرعت
💎
قیمت عالی و بصرفه
💎
پشتیبانی ۲۴ ساعت
💎
حتی میتونید. تست رایگان قبل خرید بگیرید
حتما یکبار خرید کنید. پشیمون نمیشد
😇
🔋
برای خرید از ربات زیر استفاده  کنید
👇
🤩
@irans_vpn_bot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/91067" target="_blank">📅 20:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91066">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F384hMYZLKCC_-DcridnrbhhaYTZkZABmGqm6p6Rbbf2JqI1t3nnVrPZfxHThmo0Rx1eKOxgs0ACp5LF0F0X6xd0O_ziD1lTu7pKhwJ7Il3BkNBYoF84gYXTwzx9_LZbzHus9-jluA9ftQssxOVaxWAp002mXmkLLClztXXK4imq99UIFFifV8iljj4EVe69ouLMFaBpFNj2DZ7OkRuxWy99JGG1DPTT4r5UgvFshOJ7JwhIjyiw43sJ6jVwVsG4ccChJ1eQDkYZBenIJ_EuMJI-ThBeMAD775CFHtxSOU6Rx65eMG1eg_LUlfMQvXD_pZ97VkmYx-0NXE7NZAWOTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
یواخیم کلمنت، ریاضی‌دانی که سه قهرمان آخر جام جهانی رو درست پیش‌بینی کرده بود، معتقده که هلند قهرمان جام جهانی ۲۰۲۶ می‌شه
⁉️
⏮️
مدل پیش‌بینی اون همه‌چیز رو در نظر می‌گیره؛ از جمعیت و تولید ناخالص داخلی (GDP) گرفته تا رنکینگ فیفا و فرهنگ فوتبالی کشورها. طبق این مدل، هر چهار تیم مرحله نیمه‌نهایی از اروپا خواهند بود؛ پرتغال انگلیس رو می‌بره و هلند هم اسپانیا رو شکست می‌ده، تا فینال بین هلند و پرتغال برگزار بشه
🤯
🤯
این پیش‌بینی چند شگفتی بزرگ هم داره؛ از جمله اینکه ژاپن تو مرحله یک‌هشتم نهایی برزیل رو حذف می‌کنه و پرتغال هم در مسیر رسیدن به فینال، آرژانتین رو کنار می‌زنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/91066" target="_blank">📅 20:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91061">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7uoM7b8AQU-RQvYFA89JoBXM_ky2z7HRAwnqVDeJ3_gK_2LCNdt0R-Y7Z-4OGwAD-g3mczkTKsYL_1h2789ntbHyrNWzuBSZeIsLjKJipBkOQxDRCQ7Wyd7Y-_uKk-QzJkwUo57dCl5958-WzAcE69V4RnuIAB6W25tNvHeuAc24wbAqT98OHZSM0nchQPvSy3LjCzTSJK8WDEJJ6ZiqlVABXNbBxstKjTkvWfbWF512LQIholBcsNnZ5hdSc-qmGxMmcfIROXSFsX4_K-s8mntdWzxooqjrYapnJVC7cClLYV7NPn2ft2D0uHqUo1m-Rf9cpbSPQjno1MEuvva-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-JlucDLONmNQ9VhS5KOWCOxHCWoRkqMheosxtaU6RMYmejwbe4AaiUFUoQal8HzKlGnIPyiqdGnALVIjW9W2mQ-hjNDbXnr5D49dhR2Yxp-EfIHLsbeMZRyxAiNL9UosYEXWOYG1oxec_8bFPpJrNe2f05o6LUomi5Vkxd8zbPlX71Fv2uuxCaVuslAazMqojIqW5puqb0safU5dGU4-FCXiL4NZBW6Lk23SezglFEp8dZQ_mcNO-IS8zA3KQjTZzrShrQ04LlikXcKJ8fs20GuviBbB377V26UYlXUgMUDYX9h_UHYvorXR4CUp_8vFD-pEmrpTTHyQ0fXE079GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/miZltfdfdHugk0inuA3dGJ4rH9QH9KrYcq_C_S-g_tHMc97e31xpWQ4ESrYbVTv2n9DyJuSk9sY0Dhssnx0y8ZyImnaRjLt9UJoYaXEbUBV4XcVkOnIKeajWJRDHTWM8-DK95VGKDrNUDFLVaOG3TIunRGjLv2iO10Wv-Qw2RKLB_bSD5QzqKTRaSl326A5zZmoPtEH3zAEZdp7GRFYCyEl3c-XDkO2VoKWl2MCM514s20vSdA8joG3adIKjdITd-8kQ-ezu1AvknI12sz5NaIoiZEG9n7BNz-foAD0D5iysaNFkwB5WRUs8OP6zypyo4M6ZS7Iu7LNVVwWPywFLbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5Vpd_FTwhxARr5QGPi-J7jb0qJUFpQ2xQbCGmtzOkpBSdE78jwEMCpFBSmg1kni0T9Ty2pwrNUDYlq7XsRCLDmMoZ2EQ-PzxBKpxEi3H6-QgAnihkmHQWRElhK4pvSHAjgn0n3f-RzogLXUWrSeosrTs8tgPYjexWEqU2fHwEqNmQ2jG7n4rCiSKXzt4lK4nOZGlvjn83HttBJZyMCgmAq_AWWtsIP84DxWWUB-TIskzX3zTEDE25CiZAPOtYI7n5gLQYWFEDKMOejWRqBe9KglmYCbWLUAXAnEG2wYahTk3Amg5jdu0QRv5FU-Or7QiMRjC3cQHdBSG365hKSJSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
#دانستی‌های_جام‌جهانی
💥
با کلوویس آکوستا فرناندس، «گائوشو دا کوپا» آشنا شوید، کسی که در سال ۱۹۹۰ شغلش را رها کرد تا برزیل را در ۷ جام جهانی و سایر رقابت‌ها در بیش از ۶۰ کشور دنبال کند.
🇧🇷
🏆
وقتی برزیل در خانه با نتیجه تحقیرآمیز ۷ بر ۱ به آلمان باخت، یک عکس نمادین غم عمیق او را ثبت کرد. اما به جای تلخی، کلوویس کاری غیرمنتظره انجام داد: نسخه محبوب جام را به یک هوادار آلمانی داد و گفت که آنها شایسته آن هستند و باید آن را به فینال ببرند.
🕊️
🥲
کلوویس در سال ۲۰۱۵ درگذشت، اما میراث او زنده مانده است. امروز، پسرش هنوز در سراسر جهان سفر می‌کند و کلاه و جام او را که نشان تجاری‌اش هستند، به همراه دارد. عشق واقعی به سرزمین هرگز نمی‌میرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/91061" target="_blank">📅 19:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91060">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👀
#فکت
؛ چوآنگ تنها بازیکن تو لیست 26 نفره تیم کوراسائو هست که در کوراسائو متولد شده و بقیه بازیکنای این تیم توی هلند متولد شدند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/91060" target="_blank">📅 19:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91059">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdHNBeHy90jzZtq_Tz1jDDsgiyN1Aft-tfw7SP-v5caKRyTxKOwe0rK_zA-72A0rlzMK8AR9imJrh6V9E4dZWuFx75blWTNb0mxCL0C1iCLaidDDuGEmNQtIp5krNr9iUfKci7kJnIC3uCgE2AhfZ1HoP_Qsy6qM1QeND-YtvFtPcnbAne6XaIDL-Rf_sfDLypfO29omoCLAaR4I937qFqXgeRjwkRU3KFs6iOe7bYHB1hsGtvJHZI8LbJ9nJfPcZvqowrynK81LiALYBshQ8bm-B7vqT7xMY24AoUNGpWZNmLMOthoer1JwtStGfhB8CfBR54CdJ53R0O7IOTSqwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارتین بریتویت (مریخی) 35 ساله شد
🟠
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/91059" target="_blank">📅 19:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91058">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBUNmfxT04rhXsamSHVJfHA96-JV3vXH6clcmi7y_EhUxah3Od3YS71XVwpVSvlYLQIHJk_5pcS7TfC3AAoG9EZc1eZ9ICqIhqUnxHpw-GwAsMcwmOOinE5Ey1BExCTL1Gh5sLVRHbH7TR6kDeEYQLoyhsXDKQjlItW4aXfyFtFx-Jpy4s_ZW7YhY_jXyDp_BS98CWwCrjeMToiMfDWCj4sd1WjYXk9JYVXT1pjQzemTnY71NF7L0JAxBJiE6NKMqqv_WVKmYLqRLpPdMpFmQhNiOQE7AZRDud7lmgBhr3XgvsnHyh4nIJv4IUsfWjJoXrdrdzwoNiry9K1WdFcamw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
🏆
تمام فینال‌های تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/91058" target="_blank">📅 18:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91057">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jByt-r_qxpukJPt7LobChI-JSmsL7EEuFKndOCysSce7sNnmCeZC2q9Z-nbvQZn87yZu8VE9C6xHGEbe5reCAEojTQPTzQKYaVWxuXEJ56C_I4wDkri09wfexrxEKtXn6OwXw96qZBUHQC8Lt4E0LKMXNqpubipl5tjyPAYxYx2pYox7Okk_-_eHROz9eRsf732MoWb1HVo7tVF3qSxYiXszqBR1bYsykAYVH6SGB1DpYdRBQbxQF1rkwTqXDveW5Hk3_9cnZH-Q0TakHQm-a_1dJyMyy3YMxM2otrf8W0D_8Gd7x2NFAtqp_sbTHvOvLpF3I4OmIDacJMsSSoAGRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بمب پرز
گفت بازیکنیه که تو یکی از باشگاه های لیگ قهرمانان بازی میکنه
#بتیس
گفت بازیکنیه که هافبک هجومی بازی میکنه
گفت خریدی مثل رونالدوعه
#گاته
دادم هوش مصنوعی اینو بهم تحویل داد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91057" target="_blank">📅 18:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91055">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kVB3qOm2gmblbapcme6IAniEPl9nY-ywYYqRE3ArH8rwpsMXk9HrWLo7D5i2U9_GIUHHGG-jaiiNLES9NaSeTTAW_TPRfVMD-_84clrMLuJtDIP2F-5knP66IpRGvXxtVr0vayM8n75igDtxLFfjSgOU1GdaLMT8vPEb1MsFb5bo0au0ClaHJN9zqPy16PslUUo_rAcgcTJczDdXGxHv98nUXPypUPiqrxv-GVONJzk8W_yUWWo6p3b0Wk0rPt4sPtykegVEoqk7l22xyYeJajynd0jzehrYrYL2AbX0KyoqonML2g5yeYVwGxjy1vEDTLkGjHcGfi3SJlX7pBW9qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e0eEkJ0DTu-Iogy4UAmqlTWu0ZxdZNQIS7daHJcVsgCSf88Y6JD7WoAaDJXOw36le3imX-56w-nscQsluxY4T3Z9iNMWK4A2o-1Ht3H0TiheIEE0q2q42iyYHAaI3ZKPdzjOV9YA2fhzXZpA3N_G3KL2TUSmFtunrjKzO3h5XJwnxbmKy4Bm8CKlxkCx6Pt-Bye4bEZ9Hgu0SNV6g4u4kBT9qIQL_zUtC5uwhQdjVhvie8xEEFxmfaSD5nVJ49BNUAg3W7czEaRaO-DgrBirBzJneB4FCcx6BNGpfrtOeSvxYzOXWEIES-I3KQ_CmFQixonYl-zBokUUCziNTQuOoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ژائو نوسی که هم لیگ قهرمانان رو برد و هم زندگیو..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91055" target="_blank">📅 18:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91054">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6ca25791.mp4?token=UgmxKQGipsm-Hhy63s1H6hzd1GYtMI6bOJAzMH4sWE5OCUU0Df0Oq6C2T6ewKdkFI-wdXHF4OCmzIfbuOJ9l0ck4M3c_au0-2TZW5ZUU-GnBmr93-zgdxOkwbxGbXhId1QGztgqx_oJ4P41uL-MucR0vSQ7z8WTjgS86KcyEiZjG8tkb2GDnLu-fOPrY22IeexK09fJ163NqOeIDPnTP10QPEkiyJz-JcqQUhnRHEvtJOrcDtXeXWf0EaWf_BcdlMspD8G8qRYw5NGs_l8_t-DuXIywFcYlHLFQQzju2GDW3ER-6gu1GK-BYeWXKPDuTWD_-nCgLCBPyXLmmNcFkPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6ca25791.mp4?token=UgmxKQGipsm-Hhy63s1H6hzd1GYtMI6bOJAzMH4sWE5OCUU0Df0Oq6C2T6ewKdkFI-wdXHF4OCmzIfbuOJ9l0ck4M3c_au0-2TZW5ZUU-GnBmr93-zgdxOkwbxGbXhId1QGztgqx_oJ4P41uL-MucR0vSQ7z8WTjgS86KcyEiZjG8tkb2GDnLu-fOPrY22IeexK09fJ163NqOeIDPnTP10QPEkiyJz-JcqQUhnRHEvtJOrcDtXeXWf0EaWf_BcdlMspD8G8qRYw5NGs_l8_t-DuXIywFcYlHLFQQzju2GDW3ER-6gu1GK-BYeWXKPDuTWD_-nCgLCBPyXLmmNcFkPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
على فتح الله زاده درباره حركت جنجالى با محمد حسين ميثاقى: چاره‌ای جز این نداشتم که بگویم آبش را بدهید آقای میثاقی بخورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/91054" target="_blank">📅 18:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91053">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gt4RW7olhqfVD_mVNUe01ya8Y6d7SW6VtsVSyswS1KRDKpJYqU0nz5D2f7B5XMr_yQedomd1zhVcRnS7ir3S1y_7kUXMTBwktkgLCYpvHAd8X7gNXCu9yFXPpSHuH3lopEJcQ-L611JCUqAQgLkQOJsmT0m4649BzeqkdjO9meoB4M5o_aEDGOigogUq9g9K18K78PgtO96MDceKUNCVy-Z8j2lh8NGrYXbXNamvZqlj1p9x9I4cbQ5y5ZxhIyRCzSw3Ga17qAL317niQYVP3-0x_Fm5obkVMeAtJTJI5ck8XaY7J5C_zA0i7xuHywc33Hcz5Gazko-kRFiaPZcKbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
کارلو آنچلوتی انتظار داره نیمار این هفته به تمرینات گروهی برزیل اضافه بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/91053" target="_blank">📅 17:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91052">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEaye0KnzEWVHmfc1S5055vVlw6iHTultptwEZbxyenmMnfXSyjybKugfql6_KGNR5hvcVXEOcpntlx9XT2XE2stTl5fwU4mJWegsNymhmJEpFMFVA60z8hjyvZg1270jnN0cwvzEv4n8LDB_2hxgmI9xsudVcvaQCyJl3wj0y8zzSFofs6uAZgTOSwHOZHfrFsjdKC34rTFQZhVEhKmJZvBnJ8SkG8Uj7EaFwvJ32MC_Kt3_f4jZSYfVfqsYJ5ITFtY8DpITfX_jWtd5uVSRqiv2OO68S5C-zGoiY6JkktvBBJdXptx12g1OeF5uXf0ugEGY0P2pjehrfzFfSjyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی قراره با این استوکا تو جام‌جهانی دلبری کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/91052" target="_blank">📅 17:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91051">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
رومانو هم تایید کرد بازیکن مدنظر پرز اولیسه است.‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/91051" target="_blank">📅 17:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91050">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fb7e52e0a.mp4?token=CX76g_PaqvQPYhXosK3mvU_5aZHKpgqn6cilYre3EPzoHzRfr57XaUgeW8l3u7wlsyBBJKFpLrAmk8j6tJeOTHVHq0-H7TAJmimzIxGdy_iD0dFbPbrqrFRHa8uZyiu6X7TdpTx4h9-YqfDvjVm9NSR-AfnrtdfdYBqrFVThzMt-Z5h0ct57HMN172vNEVOHXWBmYkbzxM0bM0jYetAyL5oH1ldnAJ5vW7iYtzuTMDSdXUdHS8PyUg5C8dI6j0uEysWuyU5Uj82OzJiGvpooQIonTukIr0PMlqYD8PrzjA4oVTBLhBXoPpY2B7vqt9cJn2MGE1Kkc_0EnzxmQbSUzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fb7e52e0a.mp4?token=CX76g_PaqvQPYhXosK3mvU_5aZHKpgqn6cilYre3EPzoHzRfr57XaUgeW8l3u7wlsyBBJKFpLrAmk8j6tJeOTHVHq0-H7TAJmimzIxGdy_iD0dFbPbrqrFRHa8uZyiu6X7TdpTx4h9-YqfDvjVm9NSR-AfnrtdfdYBqrFVThzMt-Z5h0ct57HMN172vNEVOHXWBmYkbzxM0bM0jYetAyL5oH1ldnAJ5vW7iYtzuTMDSdXUdHS8PyUg5C8dI6j0uEysWuyU5Uj82OzJiGvpooQIonTukIr0PMlqYD8PrzjA4oVTBLhBXoPpY2B7vqt9cJn2MGE1Kkc_0EnzxmQbSUzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
▶️
🇦🇷
فینال افسانه‌ای جام جهانی ۱۹۸۶؛ جایی که جادوی دیگو مارادونا و هیجان بازی در ورزشگاه آزتکا یکی از دراماتیک‌ترین فینال‌های تاریخ فوتبال را رقم زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/91050" target="_blank">📅 17:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91049">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUm9h5Ds6ruhpzNTEhL3F9le8bgA1Qy6kOZm6kSB83jKDRSC-xR0QzLRw809IzlV5l1XGKEVk6SqHwDkntUcCoTwld2eNKWgfrWoGrraZDqYkxI112D_otR9ku4NxKnIFPy-46Tp6Vzs_o8HZGrq8adGENrFfVcl0J4wmYYolLbf2ElmDMJnMgFy1qSrRqOWeEO8zfocUtIdQmESukzYSM_zorTP98nOGwZLJDoITTrGdtmB8ZgGDno-X1D84tTMrhAkhkVxoYihp40_zFLG7g-YNd9PXjJxrAWgXPhRGbR7DDGggJzDNWPuiV4fYJwYEgS98mYfe5QkbfnUCfcOEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با تمام قوا برای جذب اولیسه وارد عمل خواهد شد. پیشنهاد اولیه پرز 150 میلیون یورو خواهد بود و اولیسه مطلع شده است که بازیکن مورد نظر رئال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/91049" target="_blank">📅 17:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91048">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b36cf84c.mp4?token=JW9tYPPytyHz3OnQcCWfKTYgQhsEWeDQlyrB-E_XSRJWkWJJ0QUqIi97B-U7RuvB8I5V8hPQvsSpIMs0JFQvWeEuwgRuXjNmN3rD94sZk6eshCWsLObQ61441gCw2eM2L4q62KarrTc7cpgAWYUOLJwCwiMVKo56Sv-z03LxHFDiQ3KfLstRntsfe7Hi6p_JuC6ocGVfer9RG2tOE1RyEyruho-aos5-o7eD0RnOfG7V27LlY6pUoZdt98aqqwE_VdoKqsGfpf-3JqDSJ4B8Lpx_R7V1lpTaT-BQnYF9qjDhw5hZ-9Ehaou97JY-4sCgjvBF8u_11vaYZ-73ESw0iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b36cf84c.mp4?token=JW9tYPPytyHz3OnQcCWfKTYgQhsEWeDQlyrB-E_XSRJWkWJJ0QUqIi97B-U7RuvB8I5V8hPQvsSpIMs0JFQvWeEuwgRuXjNmN3rD94sZk6eshCWsLObQ61441gCw2eM2L4q62KarrTc7cpgAWYUOLJwCwiMVKo56Sv-z03LxHFDiQ3KfLstRntsfe7Hi6p_JuC6ocGVfer9RG2tOE1RyEyruho-aos5-o7eD0RnOfG7V27LlY6pUoZdt98aqqwE_VdoKqsGfpf-3JqDSJ4B8Lpx_R7V1lpTaT-BQnYF9qjDhw5hZ-9Ehaou97JY-4sCgjvBF8u_11vaYZ-73ESw0iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با تمام قوا برای جذب اولیسه وارد عمل خواهد شد. پیشنهاد اولیه پرز 150 میلیون یورو خواهد بود و اولیسه مطلع شده است که بازیکن مورد نظر رئال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/91048" target="_blank">📅 17:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91047">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با تمام قوا برای جذب اولیسه وارد عمل خواهد شد. پیشنهاد اولیه پرز 150 میلیون یورو خواهد بود و اولیسه مطلع شده است که بازیکن مورد نظر رئال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/91047" target="_blank">📅 16:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91043">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NGiWMDjBVfkfl_tw1lAnPIuDij79jbz-w-RXsoOtWI4aPbhtHpRxt-Dg55ij4nrLbuDnS7dXDUwh6G6yTHiflWG5q6FvSK2H3FLNP4hPQRrKQtw41xHqzBVEccUOcqp2KRl1NBUpv3uLkUDd9aieh2IMQ-hrzuGdBfkIrhUSaMAM7Z_9_QRsvPJhonF66A0DpalPCiW5Kz952k7-3JCdEVnZBpwKXPLG4yJd6rWpRc6DN4yICYmwfy5m6o3tF9GdRnPgSqVVQiRl87eX9ValaskkQS_5CVEt714bl5tkX0PImvhbnGtPpKvuuYVPBgvqIAkJNK_aRPvCtapSJW9i9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JDVo76YQX28_xVZSsSGVEezzgssvJ5Y4GNYxjMTri6NMM88tG4QlOI99TrMhB1epakKz5q6YS2nxj5PS-yj7k00hST9_SwlfikBW58PX-uP3KG9Xtaspe6JVHtzKd6G1pRY8dcU0s0i-HpVD1wVW2GycyRDr-HBz1Dr1p1zXQZ-tugWpe6kVXz6X3mB17kOFlkCg7mE0IRSm_mvkwLAlYEJw6D7Ls3BWm-3NEby_7th_jrBAsYIMGEQS9ODiS9zGDRaGhbQm6e-vZ8-1lKy4QbKiX362TaOuB6sqoA74bbrMGmnIKNyL3_r3ekQg9R7KRvWiQKdFTy1rjd6vxDXQSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/joTnyOdphdsnuEyQ_6Q_o09csT6vF3qxvx8ooVKT8wI7XrDGIS17hJTOOWh9xc6YEBf0UC2sxjcUaiBDJiD7xINyis0s8XiSzr4dTe3acD7wslgotg-MxvQjnKsqjCk55OYE9yspb1xcpko475yg124awObyojXb2sNle0ECtcZM5XFdr63_5AmXNLjC7kccu4lDO-YYMyeaYXEs6DjuFh9s4kIat_teoB1ue0IqFGdvXYBdZK9gwpoRnccKVvSOqOwnuyln0Xq2954kW2mfNmlzpzLLKjUDB0MWwxbF6RTFSskjIP3axAY0748RBUwjDzihGVGNouSL7ktl9Sq_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8frmYVv8FV-xuQHuyjGiIcWEFLAH4dT2ohBBpR6Hj_PQTBsPnbTCUBOKAQ8iw0wttOt5E17PN-6kdn3DhYYI2bWeYqqkIUbyfNp13NLYzWpEbZuOS7TQuKBCcxIrMeMUoHSND9kwU5eWR78jIdJ37U0HnkIYze0mHNftbyEND76qxiNfLJffkJsIg_VIyBV4V4DvRxxH_TV7dzLGiyl943i_MPlfIwtPOSXf6buXmjd0hRUlAtZXGwDmu5eM7ZpPZdLzxN-H8LQgXpcFKEei9_jYSvM25JyOW77B0pVNLd3Gwfr47YTbtJqvO2a1jNIRTg3NdOlOeBME_q1cmpGdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت بازیکنای تیم ملی نروژ در آفتابِ آمریکا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/91043" target="_blank">📅 16:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91042">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d407456a0.mp4?token=eHc3e92Cdk-kTVkGiODr3U6zMro1nPrISsaHHzF4PywED5bwxVjVKu-MwBPRJ8tJSftITm3Kk8yhSnsTJup72j3MXh8wbF-PxhKrcAhPXy-C7e-VjVGwMi0yMSAkd5k9I-uOa-t-rkt7J21Faaw4RJGx6tmRpAHl7wysfzOycXNVgCCEBOqeKiUaThLe2GRJfbSGjqH-czAnKTVjxWGBY-tY4MeG8kgQcOIBloYaDsH5vswpU9_3HdMfz4GEv7rZOSLDOvRAX7YwnGZqeL_jL-G8eT7O80gUJy46_VbScCLCHMn8P7bN8oDN6GmA7eyVswwpfVSkekr9D0cLKQKmmgEZReKv7SpUSwBuGIRPbAMlS_7OuqZe3t9O_C2JQFEu9x0pbWCCJwG852cl5V254I2TJYL7k1Ib8Cx0T25EKNhVp3ikuvgF6FsAyAx-pEl-GbJAZCqA1I9MANjlW0TJ0KmA6TpvgpjAFccI0HBBQRyGZDOBc1ZHAMp21_Tu0ZK6yRTkh4WXpGxMM3Lq7NRhEO2XCpD2QNHHmz80AMLEwPfcLQU5IRmWoJRprMF2rvmHY7-Js6WS2H8dY4XE3KWwmP1OGVGbKCUHcBazpm94jx0OY-6EKl2gdibt2CIK2rmkkg5gVKTlVmN9QmJ6MLOZ8YTnT5wT0FxfOgbKPN6YEDY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d407456a0.mp4?token=eHc3e92Cdk-kTVkGiODr3U6zMro1nPrISsaHHzF4PywED5bwxVjVKu-MwBPRJ8tJSftITm3Kk8yhSnsTJup72j3MXh8wbF-PxhKrcAhPXy-C7e-VjVGwMi0yMSAkd5k9I-uOa-t-rkt7J21Faaw4RJGx6tmRpAHl7wysfzOycXNVgCCEBOqeKiUaThLe2GRJfbSGjqH-czAnKTVjxWGBY-tY4MeG8kgQcOIBloYaDsH5vswpU9_3HdMfz4GEv7rZOSLDOvRAX7YwnGZqeL_jL-G8eT7O80gUJy46_VbScCLCHMn8P7bN8oDN6GmA7eyVswwpfVSkekr9D0cLKQKmmgEZReKv7SpUSwBuGIRPbAMlS_7OuqZe3t9O_C2JQFEu9x0pbWCCJwG852cl5V254I2TJYL7k1Ib8Cx0T25EKNhVp3ikuvgF6FsAyAx-pEl-GbJAZCqA1I9MANjlW0TJ0KmA6TpvgpjAFccI0HBBQRyGZDOBc1ZHAMp21_Tu0ZK6yRTkh4WXpGxMM3Lq7NRhEO2XCpD2QNHHmz80AMLEwPfcLQU5IRmWoJRprMF2rvmHY7-Js6WS2H8dY4XE3KWwmP1OGVGbKCUHcBazpm94jx0OY-6EKl2gdibt2CIK2rmkkg5gVKTlVmN9QmJ6MLOZ8YTnT5wT0FxfOgbKPN6YEDY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هازارد، استعداد سوخته
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/91042" target="_blank">📅 16:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91040">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ujkvYav_p1cCxKVUkAokXo2O5lQZHv8BqlL80IBr-en3Rn2hCP02Ol6nrQiOx3RIU69ih8n21cmga_H0vdQ312x94-ywBwcEbNTmlqgvo5U4PYj7nmekKIvniuav5ahrV5C_Hnh0-yJiXbEknfDwPNbS_2F4bcbNVYfGHWgD5wimLZzUHI2iRvUFo5ibWaqX-KZNAANexwhW9JPEseOtqLe3OAXaPyR4SHjcHWDL9d0P5oR2xquBUOar0rp043ZmjSW643k8PjNJ041aCol5x_QquxXBu3ZwBVlixXUJ9y6Z1dTHStcXgfpVPj8n4zZYDkXwGT3odX7G-p1roWI3Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
یامال به عنوان بهترین بازیکن فصل لالیگا انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/91040" target="_blank">📅 16:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91038">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxBmARQhEIlqkNfpEnwA7iWWOwhTzsk7FlXGdax7ayXd5QZPna3wioaxzawLh7HSOiowKCs99Fszj-pXv-cCCWzjpcPmJxZAVQTK8RZI4NGlllxpDrTUOMsZBXMvScTLvcZkQcXqDzTOwNvOhYy1lcC4MXmg36gUdULw-IsIX4li7uXhmkHEjiGxqVI-vkrIYxs1pUGy8hbzqP_8js5-6FDsa5w00OQIHfqF40EpReoRPrrRC2f3M7nF5TaJOpj2a9c62qHvd-4DXrJOWezz6a_NKVzHYdnnZS-A2yrPn4FjulD7zTBz5j060piWhgFZ5H_mb5b7EB6I5olRXBoICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#
فووری
از اسپورت:
اوسیمن به بارسلونا پیشنهاد شده است با این حال فعلا جایی در برنامه‌های بارسلونا ندارد و اولویت آلوارز است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91038" target="_blank">📅 16:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91037">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMM7LU8izk4BPVmFJrXSw2pBMlZl2uKSNCmnJHMOTqO92Pj-8D50q3XJNWQl_7vit9wb7Jm7dVpv3iStKPrQzIpEvIPYIiB8MHijDSvxHn6aJQhQX37_IJnFLAGTcNptwuk6NWQGK1XzYj7FYbcADb1kjUeavJjYFg3utxOHSl2dYNwjCWIONr0hVrP53kH_tWndadP1ibI_IH9-waC5PLA7qh0PEZpCqfi-dQIq1bXwDxTuELe0I7Q-KdGIY8TVb1DsHYcbg5UyvYjxF9VA9OaAyiavi5tn6klaz79bI3S0rFQwXwdJonbMiQz3nTXubJDkMWLkPAKast52EQt1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه یه زمانی حس ناکافی بودن داشتی به این فکر کن که برای سقف برنابئو 600 میلیون یورو هزینه شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/91037" target="_blank">📅 16:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91035">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2ho_cfENpL9ObjvLgDdGNk9nAXSfl-1bnEibxr1iwPHtyJ5-0Evr_bjYxcb-HWoKVC4jJ5rf1M3RrZgWxs06EX3NyAYalQgEWtFn-oNzaM2CL0dXPdCfu2s5UaTMEl3wCyy0cMXHujK3Stsf9uBLnbzq0UD-GztESttUGutgFwUttyr9DjtGGJcLqF1o7JfaGuAp9M-qi9wv3viRLHyxUi58HwfUdHwtxE_dqLLPFIdHXIr_b7KK_KHvEtt3e5XyFpQtKkxSnN78MIo5Qy3D6oTRxFaPowC4NGfNN0ZD6x2MU_y3svz2cE4Qo3CF0g04UB25gc-CNT-6Gelq2vYBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل لیائو: من یک چالش جدید خارج از سری‌آ می‌خواهم. لیگ جزیره را با دقت زیادی دنبال می‌کنم. اگر فرصت بازی در آنجا یا لالیگا را داشته باشم، واقعاً خوشحال می‌شوم چون استعداد من در آنجا شکوفا خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/91035" target="_blank">📅 16:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91034">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e01837206.mp4?token=XaVv7kfcwp10JXbaQhvFIwfc0JrKush0i3lj5Um__73MSlpHbb0ps_GEyBehjQLuwjQR7G8TnYn6fMpHQnLzrLeMMatsHoarxL86-yiFAlx4BS7MKxZVBnwR41ypjqmPoJ1z_Ee-CYiGhZAx4V3E79RLylpffeVivMlIR1kKgF0JwbKeIx-Mq9Zg8Zxz0TqwYFtsSFmqYNvM_1bEbFrEa9gEDiTDbdnKJRjiGR-rnFSftRpM0lW55d196nG-Bse-qpN8LpFjCd5QvHVLen0Ltmy-1fPh_r9rAkZ8PNDL_gxp3uAAy5-A2Mp1OgD7L8YyS-CpjSDE12J7IfOzTL2MGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e01837206.mp4?token=XaVv7kfcwp10JXbaQhvFIwfc0JrKush0i3lj5Um__73MSlpHbb0ps_GEyBehjQLuwjQR7G8TnYn6fMpHQnLzrLeMMatsHoarxL86-yiFAlx4BS7MKxZVBnwR41ypjqmPoJ1z_Ee-CYiGhZAx4V3E79RLylpffeVivMlIR1kKgF0JwbKeIx-Mq9Zg8Zxz0TqwYFtsSFmqYNvM_1bEbFrEa9gEDiTDbdnKJRjiGR-rnFSftRpM0lW55d196nG-Bse-qpN8LpFjCd5QvHVLen0Ltmy-1fPh_r9rAkZ8PNDL_gxp3uAAy5-A2Mp1OgD7L8YyS-CpjSDE12J7IfOzTL2MGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
🇮🇷
یه هوادار مصری اومده به سمی‌ترین شکل ممکن ترکیب تیم‌ قلعه‌نویی رو برای جام‌جهانی گفته
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/91034" target="_blank">📅 16:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91033">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaVuLc7EDU6jRuWcyjpcgYKrSQtrfupO4CTRJItVeER2Wmqpukf3lOME4BICbZV5zG-vVNF4GrsYOttmGjZwsJWC9BSMt8P8t2qx6r4FeAluBO_Nptj8ioM-suZTdJUSo5EFiXKvP7xJz73gZDKU_9DWa7In60340j0dSj3k7xgvVXyd7b5F3OyZhrW3UYGDF_APhTLK0ch22F9HJJTebbrQG_7zJVyxtW0r912Gq-idCTaI47eWmkX3tPIk5XXs4gkhQ1NiqD9Cl-swTLmAEE8xurRIniSkx5I_iAcrP1GSBFAKwSTh0Ik8dVP_9MJ8PvPcpVty2I0bbr3kXBViXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اگه لیونل مسی در جام جهانی 2026 پاس گل بده، به اولین و تنها بازیکنی تبدیل میشه که در 6 تورنمنت جام جهانی پاس گل داده
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91033" target="_blank">📅 15:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91032">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T49BtFz5zZQPCcMV465nrlaPYVax4JWtk7oHp4dU-3djl7vf04Lm22fKwGWmdAc9w2Bvu0qc0SKI43kuk-03OYhvBmeJiWPifhWW-u8VeRZBNOiy8FntMJBgDEvn6FzBBnCJx_Y3QwDIo2Qf87MMzQu1e-T8UbyC6mHzY7U3EP4YPMkXzru2LcNe2r2mgUFDVe1Ji8FtBycuRxJ8Lb8j41haL15-XWvHxt-ZGlyoDeNnXzeiXhvA_t-zWxZrxA8IcMGkxWHp1LGp0y7a2jkc8Rl6by7zE0YcV5zBlFVDwM2lZ8eWqROvX93qq8WrR6JgNaPOQWq9XDoNypgLct0e3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری و رسمی: اندی رابرتسون رسما از لیورپول به تاتنهام پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91032" target="_blank">📅 15:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91031">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltCqq2vdc9f0l-Pnl-EeKfLraYGclKMcGfPpwsZtOtglTkHyOWLpiFWdhbLQy8M-EUxfbqg5nmlST-FA7GWuf3HbRA-xo96cDsIQoAtVoaPQ9qkxAPTxlMQTSA1BodZ4PIEtkZe1vw9kjBLZ_nPFv_m5O4EHs4E-UND3VUFmU6xzdjOrH63zg4v8cq7Y8Tr7P-ClHhpp4n2Zo4xGsHn4fZJ-cY64pQ4e-BpuNjFiVXriZq-OZt47BVgwJKvGtZMA5bCycpPWOY5177r8qd4dI8wKrTuXZwdot_JtUOvhC7GYDrzObVoojPfOM9sylX28BmJLiF6KqgZ1slCgBve0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏆
🇫🇷
#فکت
؛ در جام‌جهانی فعلی، ۹۸ بازیکن متولد کشور فرانسه حضور دارند که فقط ۲۳ نفر ملیت این کشور رو دارن و برای خروس‌ها بازی می‌کنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91031" target="_blank">📅 15:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91030">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40fb78b5f3.mp4?token=IqMOkFjcRIVy55i34nbXsvdjNPa6PJCHYs-MnvFUCjgMoSDajqBAzb5O0DRJ8eC0GPtIdH7uCBpTYOdZUr1s-zDVpoVUgTCayh0PKI33FnxfjxAuHZGVF5qQZh9JosP1rCVmVchcZUqU6P4RBPnd4CAX9kNFBFjxPDefhUiAzSd6ZCQJKnb8xTTibz3PQaomoAQRbbl_7IoayvqEnK-6OL6X9ZBE-v8RRiv2hC_PnZf9xNzjuYwWQdK4zpbeKOyDuSA3-wWE_fartUt9MqXk1GqUs4f67ba_PA4kKWv-1-7rfmgIG-x7pDV03hfFW70_ImXN2biHoMe3v62RDBfyHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40fb78b5f3.mp4?token=IqMOkFjcRIVy55i34nbXsvdjNPa6PJCHYs-MnvFUCjgMoSDajqBAzb5O0DRJ8eC0GPtIdH7uCBpTYOdZUr1s-zDVpoVUgTCayh0PKI33FnxfjxAuHZGVF5qQZh9JosP1rCVmVchcZUqU6P4RBPnd4CAX9kNFBFjxPDefhUiAzSd6ZCQJKnb8xTTibz3PQaomoAQRbbl_7IoayvqEnK-6OL6X9ZBE-v8RRiv2hC_PnZf9xNzjuYwWQdK4zpbeKOyDuSA3-wWE_fartUt9MqXk1GqUs4f67ba_PA4kKWv-1-7rfmgIG-x7pDV03hfFW70_ImXN2biHoMe3v62RDBfyHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کلیپ از یه عروسی توی کرمان وایرال شده، مثکه رسمه فامیلای عروس اینجوری فامیلای داماد رو میارن وسط و با چوب میوفتن به جونشون
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/91030" target="_blank">📅 15:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91028">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MM6eKXM_mT4N1JwDhws7HWaw3cKcxaT5Rbo2WYSzPy-i3KhWUUqmj0idDzJG1IyGzElqRmnYTVrTALgRQ_I1klnxNqZrIrpWeci3HHEvxVHVYuYTLohL0HFk4CfafeVEU6PoSaYq_s-2d3nfRFa7IgL1ftBELbO_avOma1t0T5F24gorXI9O-4jXqtDtBwBTwblNjSfvgKZHZSjUwjRlV6PKsD_iQ2sxjuL2UXIBfOMLgTz1gHuImXMJz8jXkwsoFFGufFC50bwQRCRtaqBaLFpG73tA_mo70m7MX2ypX4L4dqL_7-5OCm4HDjDqJ6uKb7Cnu43jhEnNCw4hhdpUdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXEY_dMMHQU6PgQ5b7joglU0cS9Fwkm1q8pZRcn0HcNINYIfCHVkSYGzqmggkjmMV-K6kfalopHaXr9N3_KSHkmdKQtEUSvs4vIHMdLkDUZ_9aMmEubsQKYivaPguTgZy6oRbOuMpqZ_7NLaWquIrgMGijXhJL6e_kdBWiv9Wg3zAxnVmjwLXt--XO83bwisxoPLluo5r5L0qiXn-NbjuU2XNQrIU3sQSC8mRyfxLJNEBOk2D-G2EquWNrxtE4E2yqsQFoswm4386RxGTa8QJm8sng7jUInHCsEd-PMdjouVQV_t3zXXbOs7RQH6mz69uvYOVGzdX40qvM6rDhuxKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🎙
🇧🇷
جسیکا توگا، دوست‌دختر سابق وینیسیوس جونیور: «بازیکنان سیاه‌پوست همیشه از نژادپرستی شکایت می‌کنند؛ اما همیشه زنان سفیدپوست و بلوند را ترجیح می‌دهند. هرگز با زنان سیاه‌پوست رابطه ندارند. چرا اینطور است؟»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91028" target="_blank">📅 14:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91027">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c893a4439a.mp4?token=XJf2pIT2HHzwuzFXVDOzPacxBor-3bf7HIwASaacpjCafvLDaxv6bbqVQqgEyIAkA1ivZkD0pVaHw8eNgdZUCzL9PA2Skh-HAINrfXlar5hPmq3kUMSWyzwqJDig697b1pILPFeJ3MxlifMu9UkYTeCBgempDQfYo1yYd3dzszZaN2L_b4KCz-9X-NeR7HMPCO1g-9jc9_GJP2fkfv6OxvAhIXQIDONTXSCTlkO4TPbstTyPZs0SyGqBgcH6qeooiPPIs9YJAUyg7JbEFb6jSvV-GecfCU3YRhgwtTp1WTGWpzy5lp5wYAQytRNgPt9lFW5ZBE2KSsk8Vto6iQiZFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c893a4439a.mp4?token=XJf2pIT2HHzwuzFXVDOzPacxBor-3bf7HIwASaacpjCafvLDaxv6bbqVQqgEyIAkA1ivZkD0pVaHw8eNgdZUCzL9PA2Skh-HAINrfXlar5hPmq3kUMSWyzwqJDig697b1pILPFeJ3MxlifMu9UkYTeCBgempDQfYo1yYd3dzszZaN2L_b4KCz-9X-NeR7HMPCO1g-9jc9_GJP2fkfv6OxvAhIXQIDONTXSCTlkO4TPbstTyPZs0SyGqBgcH6qeooiPPIs9YJAUyg7JbEFb6jSvV-GecfCU3YRhgwtTp1WTGWpzy5lp5wYAQytRNgPt9lFW5ZBE2KSsk8Vto6iQiZFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
امیرحسین ثابتی نماینده مجلس: آمریکا بعد از جام جهانی سنگین‌تر به ایران حمله خواهد کرد و ایران را تبدیل به غزه دوم می‌کنند.
❗️
اگر دوباره سایه جنگ بصورت جدی روی کشور آمد باید پیش‌دستانه پتروشیمی‌ها و زیرساخت‌های منطقه را بزنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/91027" target="_blank">📅 14:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91026">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7143a2f59a.mp4?token=nFFREtfQEfbtrX7-K1JolHESDnwngz5ocobTbtw611Dnbc_qJMRZnP-05BRNxjVs8wnZ_NP_yy5EFa-qYwU2JDv2vjuUTCLPkCGMVGwi5ZuqigA5V-KhAZ1vfnzXVAoi9UWZgbwEQBoQexyrr8-EhKkc3-9R9TPHPuPxM2_5L_Bk6ArmcIzxizB5Z2mlgffk6pLRH2Hv1t01phqyuW6DMsAoF0lN77jiBFCZXOIrgvx5UvOza5sI5ipqVrSUr-5fsgMXYl-g99XM509CMSHZWuEAiG1Q-DHkjnw-d7ycOVmnIKohUhTquIaPJ2JRInwJON30WycEtzY4EDOGWUJ0Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7143a2f59a.mp4?token=nFFREtfQEfbtrX7-K1JolHESDnwngz5ocobTbtw611Dnbc_qJMRZnP-05BRNxjVs8wnZ_NP_yy5EFa-qYwU2JDv2vjuUTCLPkCGMVGwi5ZuqigA5V-KhAZ1vfnzXVAoi9UWZgbwEQBoQexyrr8-EhKkc3-9R9TPHPuPxM2_5L_Bk6ArmcIzxizB5Z2mlgffk6pLRH2Hv1t01phqyuW6DMsAoF0lN77jiBFCZXOIrgvx5UvOza5sI5ipqVrSUr-5fsgMXYl-g99XM509CMSHZWuEAiG1Q-DHkjnw-d7ycOVmnIKohUhTquIaPJ2JRInwJON30WycEtzY4EDOGWUJ0Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت امباپه در ترکیب فصل‌بعدی رئال
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91026" target="_blank">📅 14:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91025">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKEafMEN09GeMpLdPEZ3Z9r1SZOnUqsbvzdb9Do0JU42z4ZSWSqXMwXcwpjn4ep3sD9aPf-2UGMkS7pK8U4_DQP5r8Kd1HHyWAfYWATxrn159FW52DnNM-fU6A_ZpnTfJwC6vQdLXp6RKWu6PvEIF7IL_I6VqXKO4IpnLtKONawMhscc6B_A2gCUasgYzUCyHYc8gyc9yTI4Y-YwdRbImlcVyNPzR9CB_TNX7tY8FvLJ4JJ_V3NAqHcOLBkJxpRgmk5SC71tPZGsSQprIiuQZf9XECV2xIatEvH2NAASsaOo6P9-684kkp_f7sb7QuvqarCer1Vkji8FzNggvwEv9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تلگراف: با وجود تکذیب‌ها، فلورنتینو پرز برای جذب ستاره بایرن‌مونیخ رقمی بیش از ۱۵۰ میلیون یورو پرداخت میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91025" target="_blank">📅 14:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91024">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری؛ روزنامه تلگراف: هدف فلورنتینو پرز جذب مایکل اولیسه هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91024" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91023">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFonJw0zwgzaCxfZ1EEsK8EiLxuViwWEQxZq0VfI_wdtC2mM6_6p4cfeeqc37q26_ajJcuXok1Hdk829VsSdeYaeUCV6OICJx0SN1qO3PH4xrB2eOE6MisETbmbZMso9tYAi6UVOvBrsOGxoljqBCi2vwqLaVtrV8pxzKoM76W7DMeSKzwqzKrry0FTBSRS4_WqgZJ3SwlIyLxm5cIQelXh5GEu2eRAl063sVCstrKr8mXLThtsLPNBARIb4d0okrw_rAZpt2Un1VhQAflNcaFx-1KxH3ddTAxeA9xEVb9cYvPLtPT7rgcMWIm36AfLE-qjaAp0RwQfw_uU5Y7lmdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری
؛ روزنامه تلگراف: هدف فلورنتینو پرز جذب مایکل اولیسه هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/91023" target="_blank">📅 14:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91022">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/deHgugTexSHUUTJc8BX1A7x7SBmKPpywz0k1Hu2X2ukGJKMx1xdvuQyTC5Ld-UPIk7ZjurV1HQscMG8lIuraSoCYbOXYQwoLqRvvQxzRnPug7UM7mZmQ-RIdu_1nDXGpbEHPUQieKbWdvnFiGwDK2NsoQ9kcKXlj9q4OGROuOFIGU2u0Gcubi2up2C_h1Cv1_0k9X8Ws6lNYk-fTnLz0-TQKsv2_Gm1osn_juU_T5Gz2CJWhEUlko5OexIcAzX5fcrsP5DWfpM4N5xDLNX4iXpTmFP2VPynwXnorBDKATwCJjez38Xzzt0QwUEvE1BazgIv0TkCKsawQMtHEwXjWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی چوپان هر چند وقت یه بار هوس فحش میکنه یه استوری میزاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91022" target="_blank">📅 14:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91021">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e1282030.mp4?token=N42aJ1nT5-cba5sk91TxOKYXujixYDLkLyc5VNQVL8LibCSTDx1WEWbagPto4bsv-mZ3EbWML2gbTdI5purcX2-oonT5BsLk-MROEDodwq0JyVnlj8cuSl-eit0sozi-iPJcXTWKY3oNExZXUagKq0Wd-W-H0W8S_snbR4ICCwEIWbkWk_cC9OfIepioT1aWtXDA3f_8EWuNvfW5L03NftMJGKefRBqYcaRaXOb_qor9-XyWzhyJwr5RUgIYmbIhVl_G7gRImqXaJBO7k3PVDlP6rcuumCcbybKxRQE2leqLZBGrexavJUToK6hVuPjBUU95IoUuJR8Xbc8kob6zlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e1282030.mp4?token=N42aJ1nT5-cba5sk91TxOKYXujixYDLkLyc5VNQVL8LibCSTDx1WEWbagPto4bsv-mZ3EbWML2gbTdI5purcX2-oonT5BsLk-MROEDodwq0JyVnlj8cuSl-eit0sozi-iPJcXTWKY3oNExZXUagKq0Wd-W-H0W8S_snbR4ICCwEIWbkWk_cC9OfIepioT1aWtXDA3f_8EWuNvfW5L03NftMJGKefRBqYcaRaXOb_qor9-XyWzhyJwr5RUgIYmbIhVl_G7gRImqXaJBO7k3PVDlP6rcuumCcbybKxRQE2leqLZBGrexavJUToK6hVuPjBUU95IoUuJR8Xbc8kob6zlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شهریار مغانلو:
میخوایم با ۳ برد به عنوان صدرنشین صعود کنیم!🫪🫪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91021" target="_blank">📅 14:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91020">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cf842d659.mp4?token=EH3DolpqabIHUNPRvy4FnNCpLW92CY4BQR6vydvJ5IAY2LaQUBd3STIjX08YVOGioTJW4QmC13yrpm2_eoWAYsx2S_SURGoMdJDYvELIVqI-vw5KLdVrWUY-aOQ8dMg15KD6ruCj71XuMGnVOj5DQBPd33QsPsWkePP_DyxL9j-HllK6z5c5JNmEMfTsKj01SkaAkgjPenYRokDD890ayBQ3ODLZ4-MQEQTSBPGhUWcwXIwWwRtyiIz25WWsb6vHHv8hcTTujG652ax7mM06cUA3ySYaYQpO-fZA_r6T8JTr29pwea4sshpuvLOikLWoacQCTjPPVPEZVZlo3qYuLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cf842d659.mp4?token=EH3DolpqabIHUNPRvy4FnNCpLW92CY4BQR6vydvJ5IAY2LaQUBd3STIjX08YVOGioTJW4QmC13yrpm2_eoWAYsx2S_SURGoMdJDYvELIVqI-vw5KLdVrWUY-aOQ8dMg15KD6ruCj71XuMGnVOj5DQBPd33QsPsWkePP_DyxL9j-HllK6z5c5JNmEMfTsKj01SkaAkgjPenYRokDD890ayBQ3ODLZ4-MQEQTSBPGhUWcwXIwWwRtyiIz25WWsb6vHHv8hcTTujG652ax7mM06cUA3ySYaYQpO-fZA_r6T8JTr29pwea4sshpuvLOikLWoacQCTjPPVPEZVZlo3qYuLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇯🇵
ویدیو منتشر شده از زمین تمرین کمپ تیم‌ ژاپن در مکزیک که کیفیت خوبی نداره و باعث‌اعتراض شده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91020" target="_blank">📅 14:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91015">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jb_zhLThUCgLUcLSt66kU8WnJ3pBcR9l8eliSR4_DDxX4wz0L412zlG4LiX5gLPVjmD6NOopu-cgAJrjjCoFcsTWLf6l-5H809p095pBfwGnlNp3hyhvO6OZOWKKozG1NeoyCLA0qR4MAqMWwnD9x0-eQM8PMy2xT5KjuVzmcfcw2Z0OaR3HnyUUTtYXwf4ROZSb4gJiHn3CbpJPRbtOh9kCTI2ewYXFyw7V5g_NMSxigiiCEJESjS2-MZl0JIBos8-efEeDu0kEkfvpizmnMQ_WfEUpC5s7PnUB3CyolwICSXjcKYqqeLci1-wrjW1KRnyfogysPrtct2yob3FLNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMSatLVANNzK2GSOQpXe4EVirt7yL6ZUAKSZtY7LLGVQOEXeM0sWvMK-ZX_VNRCcH3QqqOzfch31Esgwgm8WyoJOKK3N2l5Qr0yLWeVq6b7TqKJ-gzt3ZPqPFUtxVKTQutA2g__6Ah2tx3sgXCDGPcegd9pcgu_iqyp1djbsa8XIKJibJIgGyZ82iUlhw94t6lVaEeVgD6Ly5vHrkX83XWMcM82yAw6i6gew7hdLjk6cSMTlmRZm9NhfBnWwJQ1oNRXlI0RDi5FnXmsxwBrJgkoCbybRu9VJinYZvnqiwQuyHbu3itVnv3sbT3Sxjn2BO04CaLXn4QXs1207Gms5bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3WIfoWrSKHjs36gg7EDQTPNpnx5p4v3fhhcUT5fwa6Mn9k7TSUDTYvK4a-vVvkZlV8ky8nbAW5IkRdYamFSKNDIokmGwM66ZJ00bHvghrlNWbkV0HgyTLFl0K883Iy3cUG_n9w9gctrVI3PrpeNf1dps0TzxxIwO6iqDyZ3ZQMNB-KaP24jaSs8hRVfBOvy2MfKhdkyrSaxLPBAh2J2wdRVni6lnCJvjhxoNHbe2oyQNnga7tUHLnCJC6HIn1Isuj2fbWdVEKAKEPDwDtvrfg9TfMTUTp1J4XG4MpQRKmudwY57xAniFVBy-Inb0lCDkDPNMILZlKz3oVwcL5oSMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZCdaQBEefR-SRiiFF3hALGHNFkO07NXCfe4AFjQn7XGqOaQB5XOlEUXVeWzm3KR2jyMZnT82mRIWmrRH4vZOxKglperuTxhhzXBMkuVYyFNHP6cSM--QiYDI4jL4U-oqyTRKlk9NWBj0L7QODl60SDkiLAGuL5cH-7KJc1dF457_Jllc7mYDHQIUYSJm5QTvml2TrGDOfBigjevlim2O3i6st0UgL9A15awxYgR-C13bakLpKidO8fMh1RGSYN5sYMYL6YSZ6lnJT3-X99Jdl3q4V3cSCCH_jkk44WShM6qxlZkujjHetBSZl6G8t6zoUmbi91xv5UcktO5Dqkw1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QT_NQ5PmnUknjEalRrRmtuJ63zfd4DwybQmA38XYwSqqmMIDhmvXeFMx1xpMCwsivHpzEkYNkfxM2ZoKwVQb56mNqHjqoVUm6ZEl1QrPjwT77cC6TmJiwZMPRwJi5A3kBHgK_0fLU1xENM5AyY03rgorjelJkfV_U9Vs6NIKPmYMSR66z90Aom6Bu91HHppZHhRNjXMPm1M-QtL91r-0ZVfEeYfivuH8GNxmZA_duFe443no_2XrE4tRqL4Cj7DjEuCeIWCvsHyxlPkrYbQ4dLIyxYB447G8SonitTaYzs5UfFkZM5XMkpUEyL36a3yyCBvos8IPrIVfHGRecskbRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
هوادار روسیه‌ای در انتظار آغاز جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91015" target="_blank">📅 13:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91014">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8abc04017.mp4?token=ikWhXGaeB5DjR4ET4YpB-MygkcVkgm8-rpIuGoxkiyPWGOBLdp2y2TaY4h-HNGV6ctrbxDX89G0_jdv_KV7FeM_844DQooMjYZSCvWdzjn3L6bcDFixhE78o0qpFzsN94kUDTvVpm_q83kSMRUhYpkJ1Jr_OZlbJ1G15s2ThAHHHzFY950E9lrEdVVgptQ3pkS66cFATWAe5e9A3HTHqa6PZ8uV1vNpY_MOBXlQH_nxxV7sL04RqbE4Fi6VMOHgrkwp_SmVhOkzh15vobmZSath65xd30TC6a1rxlayMSmSux3zzBiIEA_wcry-zKJrqIy8ZE3XqaXrM3C96OsVJXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8abc04017.mp4?token=ikWhXGaeB5DjR4ET4YpB-MygkcVkgm8-rpIuGoxkiyPWGOBLdp2y2TaY4h-HNGV6ctrbxDX89G0_jdv_KV7FeM_844DQooMjYZSCvWdzjn3L6bcDFixhE78o0qpFzsN94kUDTvVpm_q83kSMRUhYpkJ1Jr_OZlbJ1G15s2ThAHHHzFY950E9lrEdVVgptQ3pkS66cFATWAe5e9A3HTHqa6PZ8uV1vNpY_MOBXlQH_nxxV7sL04RqbE4Fi6VMOHgrkwp_SmVhOkzh15vobmZSath65xd30TC6a1rxlayMSmSux3zzBiIEA_wcry-zKJrqIy8ZE3XqaXrM3C96OsVJXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
بانوان جذاب اونور آبی موقع استادیوم رفتن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/91014" target="_blank">📅 13:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91013">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b018b6c88.mp4?token=uWBHVrPJxLaVRWTC-TLeW__K_B8gpfOT28VJ0SkwCYybESzTpiRzvtJ3p3m3Sb2bcVGlAtHmliAqy9AnC0PNR5NbzqRCeVrI0tjL7fXewOg1oKApLAUJMbWnr4uQ3jNZJG9ZjgLXdeRn9T9fHpd77JxXfeqn7gDPSQkP2J70XBu8FReOH4uCDAxgfF7VUnQWvfBZzdN6cTqg9sXZl5xI3_znFr1d5IP4jO6JvCsMtwS-kbdpdJFoofIvfjxo7hI3sj0HG7bmY7yfn7WuqK5pqYwnQRuw2Bfvxay0S6PogoZmMoC1-hrRJ8KEWnYLZ2O0wFRiTcb_hlov33qpPD9uxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b018b6c88.mp4?token=uWBHVrPJxLaVRWTC-TLeW__K_B8gpfOT28VJ0SkwCYybESzTpiRzvtJ3p3m3Sb2bcVGlAtHmliAqy9AnC0PNR5NbzqRCeVrI0tjL7fXewOg1oKApLAUJMbWnr4uQ3jNZJG9ZjgLXdeRn9T9fHpd77JxXfeqn7gDPSQkP2J70XBu8FReOH4uCDAxgfF7VUnQWvfBZzdN6cTqg9sXZl5xI3_znFr1d5IP4jO6JvCsMtwS-kbdpdJFoofIvfjxo7hI3sj0HG7bmY7yfn7WuqK5pqYwnQRuw2Bfvxay0S6PogoZmMoC1-hrRJ8KEWnYLZ2O0wFRiTcb_hlov33qpPD9uxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای‌کاش اینترنت وصل نمیشد اینارو نمیدیدیم
🙁
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91013" target="_blank">📅 13:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91012">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lf7-_oliKmxqd2NCAY5U_LkF1XKYfvT8g2FLD0DRcfSsi9H4ia-qRmv9tseOhJEN6cr4kQROI30yne947WJdpQJC2QL_PJcAzhfOVidpY5xcptU_r8Lv7Phy6GVSCv0-MZxeiqYK2Zl88pO_PmXNNxSJ_seOAJO5D9EuATK-lV9-M3_Ojlonc1k1grwnJfgdfNXAE-Vbte3QNmH7ZvgWrLpzmha7ZoIVxf5nGCOvZcDAVItLmbT8R9fuAmXTlhDzzvyvTOMR8EF0Ztus4SVcxaR5iaC20H9T1cgkz2Vj83Yw4UQ4vS8BvL_5L0fiWrNyN-Ofb_uuTL3RzxBvflIdzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🇪🇸
#نقل‌وانتقالات
|یوونتوس درحال مذاکره پیشرفته با اتلتیکومادرید برای جذب سورلوث است. در صورت خروج این بازیکن، احتمالا ولاهوویچ که قراردادش با بانوی پیر به پایان رسیده، راهی مادرید میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/91012" target="_blank">📅 12:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91011">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
‼️
🎙
افشاگری نیکبخت‌واحدی از پشت پرده بازداشت مجاهد خذیراوی در پارتی شبانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/91011" target="_blank">📅 12:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91010">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/137c5fb470.mp4?token=a_6-4HMIA5Xl-3iJURwJLDI_o4JvlEtD-6YshmSHP2g904g4MY1BeYz7NGPbqcjtRF7K8SdoLWPDnr_82sLOVU8Vg52dONYrXwdl8K3vjM_V8ZqeXngB18SNZSDt_4gPwxr-tD3d-17NxsrzyX0zqzO1k2aQO4_62IVZm81mLTv3O39qh5ROspU9ssSrosUVQitrQQGKBCiBJB63mFb4XOWMd6DBI6m_UIjENMY_gSrvtCMM7eZCKRJsLwh-nebIWtKByIrV6q-Cx3UYsO-x-CROGFGXWRw68onVqnW2L1LMPWb1KTjEIdTffnGDtc6ieULO7JAVR9q3BsXDhqn2AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/137c5fb470.mp4?token=a_6-4HMIA5Xl-3iJURwJLDI_o4JvlEtD-6YshmSHP2g904g4MY1BeYz7NGPbqcjtRF7K8SdoLWPDnr_82sLOVU8Vg52dONYrXwdl8K3vjM_V8ZqeXngB18SNZSDt_4gPwxr-tD3d-17NxsrzyX0zqzO1k2aQO4_62IVZm81mLTv3O39qh5ROspU9ssSrosUVQitrQQGKBCiBJB63mFb4XOWMd6DBI6m_UIjENMY_gSrvtCMM7eZCKRJsLwh-nebIWtKByIrV6q-Cx3UYsO-x-CROGFGXWRw68onVqnW2L1LMPWb1KTjEIdTffnGDtc6ieULO7JAVR9q3BsXDhqn2AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شیدا مقصودلو شیطون شده و میخواد با پولای ددی مورایس موزیک ویدیو جام‌جهانی منتشر کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/91010" target="_blank">📅 12:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91009">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YerTl2f0tJ-U2qwe0ZMituiGdkm-G7gaGn1GGrEHwmGXjeazNGXEjK27HhpCAM24GZPW9UPArUKW7AwkKAq9eCrEYnuZhoGqyj6uRMztpvM3xuFhqCBCBNkCmGbxRWf8voLuzwOLjdGS20Sb3sl7iXgB3SuY8AIWTwUXnrWUk-xIDGDOzxLnPRljWnZNSKKJWmyX6gjHj3z7CP_lgdLR0fq8V6dSJ6ywJtQ8UeGQiGKng8yD2R2YNspfsaXqccBXa0_BpQQ9obXf-3Y7PWUaH5RDy7HvXR4MTfk9X_vgAkLDEffxItyYYL_AyKiuHWRphNiW6ZcYz8vtvJiKN5-5bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇫🇷
#فوووووووری
؛ روزنامه الکاس‌قطر به نقل از ناصر خلاف: ویتینیا و نوس به هیچ‌وجه فروشی نیستند و رئال‌مادرید باید قید این بازیکنان رو بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/91009" target="_blank">📅 12:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91008">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c4d39e7f.mp4?token=NcnO5p95GQl2shLTs0eMClGlnoeqbJ7tHkvA2AzBxYR4GCunnhGW2Vc27O54m_BirJFGERMOjO-w858Z05OPCk_DFTiBlo0dUfYOsvR40IR5xteZO9yFryJNHL_3uTVRxtLhA6B1tItJXYSn0_p2dQIvIDVtDEtjKV5E0NQMeG71oNPsmjstwSh5r5O7n0JIyG-NnWcCxjg88HwvXTDLsglGKTo_bKDm9UjDQudK9ByX8pDcfyKMgBqT7H2R1scFc0uSQ-nlk1oj2fyrFWsxaF_GtDadHP3flQnsXCurC1Ih6VGcbJqD-bh8RubYwm15ua_o5k6xAQsg-omiHwN6ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c4d39e7f.mp4?token=NcnO5p95GQl2shLTs0eMClGlnoeqbJ7tHkvA2AzBxYR4GCunnhGW2Vc27O54m_BirJFGERMOjO-w858Z05OPCk_DFTiBlo0dUfYOsvR40IR5xteZO9yFryJNHL_3uTVRxtLhA6B1tItJXYSn0_p2dQIvIDVtDEtjKV5E0NQMeG71oNPsmjstwSh5r5O7n0JIyG-NnWcCxjg88HwvXTDLsglGKTo_bKDm9UjDQudK9ByX8pDcfyKMgBqT7H2R1scFc0uSQ-nlk1oj2fyrFWsxaF_GtDadHP3flQnsXCurC1Ih6VGcbJqD-bh8RubYwm15ua_o5k6xAQsg-omiHwN6ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
صف کشیدن بازیکنای عراق بعد بازی دیشب برای گرفتن عکس با لامینه یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/91008" target="_blank">📅 12:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91007">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfpCLm29-J8Z0uNaku6G2mmqKakupS4rQAp_j9QUQg2w8ztdKggaAQg-sU0VyGx7-rPdD5n69cOYEylZXDIyzUhK8jomdv7gu8VIGNlfhL_VHDQAlTf864O6KDpWxSJS4vxjj0yigQ4ETyCB-OKPrh2KVdGqrY8IaGaUZZHAPBCg6pdqVFp5lrXCfn6QiinXHvoVmY4z_Iezf2AF022SHrS3eA_IGGGSIAG7i4WeSPJx9rTt0mHd8JPaDtibTJp_gkhOrfqYsSsq3Wz5NLIz58NktDHsOsAEd2ZD2UfFCMrQNEhiuOIwAS-MMi_9Qhfe9ZuD0OHYDd6ypV-PqI_Qbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منتظر آموزش های آشپزی هستیم دوست عزیز
☺️
🙏
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91007" target="_blank">📅 12:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91006">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b863e17f0.mp4?token=GYIf1JTlV27YJZDc3ho5H6AzJ5qUpxMP86uEj2HkQ3_QG9GqHULof1hXHsSq8AS1g3JsV7kOPd3zA7OtG9SiNHaDM7Ctct6eSA4eMMkKJwXrQgaOtI1l7dvuTpbKZhfWmtpBfAC8nbOPEaMpvpH13Efb6XnBWeIp1GqSilv7HTHaa6XhWFbXDgVj78LJd5bdtVHLCDhv5T-7kNYdT_3QD9AS6VlT-pTfTfHn0-N2Sc70oCrsz6yt6WCSiZjRRSW1Hh5ceq9a-g7H4ka1ibUkxdNW2_-5WYCCcj0ibFffJct8tZ3NvNfH-lz7Ydqs5xjEab-RV-G7qxnLM6l7Y-5frw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b863e17f0.mp4?token=GYIf1JTlV27YJZDc3ho5H6AzJ5qUpxMP86uEj2HkQ3_QG9GqHULof1hXHsSq8AS1g3JsV7kOPd3zA7OtG9SiNHaDM7Ctct6eSA4eMMkKJwXrQgaOtI1l7dvuTpbKZhfWmtpBfAC8nbOPEaMpvpH13Efb6XnBWeIp1GqSilv7HTHaa6XhWFbXDgVj78LJd5bdtVHLCDhv5T-7kNYdT_3QD9AS6VlT-pTfTfHn0-N2Sc70oCrsz6yt6WCSiZjRRSW1Hh5ceq9a-g7H4ka1ibUkxdNW2_-5WYCCcj0ibFffJct8tZ3NvNfH-lz7Ydqs5xjEab-RV-G7qxnLM6l7Y-5frw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور مکزیک در کنفرانس مطبوعاتی یه توپیو انداخت وسط خبرنگارا و یه خانومی انقدر ذوق توپ داشت که با کله رفت تو کف سالن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/91006" target="_blank">📅 11:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91005">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8de806e44.mp4?token=v1MdAOjcYaLvNJsi8SXir_9MqtJfABD-vlwAvf5IZSUtK-z-oxbBGVjtF2hPAudyUkGClWg-mZ03yE9_FD4Bs0S3DaVIz_f5Iga45g7O5bnff2dBiSPjD06f55VCJDh9RQzdLKUIEDJ-ziTjOr25baZV8FrGr2hH1wL7sW_n8pdXBt_as48U_MQLSy7xejQYfdtVmpb-StYniqHOKBazbWeR1M9NIqJC6oIuRgxyKCUN7r7awCeiYduGSJde5DP1b9nFbU3ztRHpoQpTuVjV034THC0p2efgnEY2PtXSdyXB3ty7imQroJ2K5aCT12CS9kQr0FtYQ2BwXFIrDsRj4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8de806e44.mp4?token=v1MdAOjcYaLvNJsi8SXir_9MqtJfABD-vlwAvf5IZSUtK-z-oxbBGVjtF2hPAudyUkGClWg-mZ03yE9_FD4Bs0S3DaVIz_f5Iga45g7O5bnff2dBiSPjD06f55VCJDh9RQzdLKUIEDJ-ziTjOr25baZV8FrGr2hH1wL7sW_n8pdXBt_as48U_MQLSy7xejQYfdtVmpb-StYniqHOKBazbWeR1M9NIqJC6oIuRgxyKCUN7r7awCeiYduGSJde5DP1b9nFbU3ztRHpoQpTuVjV034THC0p2efgnEY2PtXSdyXB3ty7imQroJ2K5aCT12CS9kQr0FtYQ2BwXFIrDsRj4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور با انتشار این ویدیو نوشت: و شما ادامه خواهید داشت...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/91005" target="_blank">📅 11:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91004">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lk5Lm5JhXIvyKS5FPlXErd18v_s_4hrLx2TOGNo56LTN13QBJsJOnmuXEq2B0GIH3omLkPaiNieeojRmWR05hnewDqkSbwoLX6jJ_3j7gJFj0EYB4uVWMq4ij1YQz2R3W9kH5WVI8rXbXlu9KGsu6OT_3K2jcI9w-SEU6idDMqmbf2timivc5oMTBYS4nUDtmwmYEUsd103RP-J-bHj4WjygzqSBub5tJh0L7_l_fkSLO1fSp1D254hK8XYbZskGxcPmdczPDvvUg54q-49ZX7lcN5CR1qBY3Seyn217NuBChgwKW1J1YSh_TLL-JbHhx7OF2OtlWaUnVeuyu1AieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🇳🇴
عکس تیمی جالب نروژی ها قبل از سفر به آمریکا به سبک وایکینگ‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/91004" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91003">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae875521b.mp4?token=FQMYXBpCuVqxZygEu7oihCtqrzxSXVQYMu-sjutHz8ME4AY1HJ_tBKZ2m3NqD9V5SBKv9U9IJ-LNEE39xCu2Acs4eB7P-JI56c8zTsMVOFOLZSpnlVr_27JpYs8lkG1ll55huUL3S8B5mtpjER1emFjH6dznpBJit1N5nOhAx_sFcEC124xxDQIcUkjudytJtp5nUHWpjH2l546BMK8qv2aOWkJnNaNL035wOqcwAkUh8el765risIIZ0agw-dxAClDN7zqqY8xki1N_rfLoxFbMd5YEJld9fUGve3YskDisfTuCOkC4JmgnpttZZMgFsN9AbiGeNh4XVLHPz6gUsJ5Tnjf-pIxi7kO32Si3Zz7iqqw2mqmxdTn4hq09n0D8wwL8KD3E36MA74LpvwjUU7LhSa0q1pRe278mbcKLgzPwTPlIxxAxxim8nc5-wIMv-AQCRSySMm9c9q2TK8ohEidcvIOwiLiUzlw9n1_JHaLzI5MadjlQ3LP2IKUwo6m3RzjQDcJBD39ykHKM6YQyMQsgvKI3FADRnFIJl2DQjNpnZGrli3WpPd0Zdbf0lZQs20LxUMpjYE959HEM7RG9dLUM9t5QDAUqD5HvOU3Ye8H0cYInGpBmLXO022DBlmupT5Im5TFMrWJwO5ejMB6n1dz0z1ynECKDuU2psE9tUFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae875521b.mp4?token=FQMYXBpCuVqxZygEu7oihCtqrzxSXVQYMu-sjutHz8ME4AY1HJ_tBKZ2m3NqD9V5SBKv9U9IJ-LNEE39xCu2Acs4eB7P-JI56c8zTsMVOFOLZSpnlVr_27JpYs8lkG1ll55huUL3S8B5mtpjER1emFjH6dznpBJit1N5nOhAx_sFcEC124xxDQIcUkjudytJtp5nUHWpjH2l546BMK8qv2aOWkJnNaNL035wOqcwAkUh8el765risIIZ0agw-dxAClDN7zqqY8xki1N_rfLoxFbMd5YEJld9fUGve3YskDisfTuCOkC4JmgnpttZZMgFsN9AbiGeNh4XVLHPz6gUsJ5Tnjf-pIxi7kO32Si3Zz7iqqw2mqmxdTn4hq09n0D8wwL8KD3E36MA74LpvwjUU7LhSa0q1pRe278mbcKLgzPwTPlIxxAxxim8nc5-wIMv-AQCRSySMm9c9q2TK8ohEidcvIOwiLiUzlw9n1_JHaLzI5MadjlQ3LP2IKUwo6m3RzjQDcJBD39ykHKM6YQyMQsgvKI3FADRnFIJl2DQjNpnZGrli3WpPd0Zdbf0lZQs20LxUMpjYE959HEM7RG9dLUM9t5QDAUqD5HvOU3Ye8H0cYInGpBmLXO022DBlmupT5Im5TFMrWJwO5ejMB6n1dz0z1ynECKDuU2psE9tUFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شکیرا از ارتباط عمیقش با جام‌جهانی میگه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/Futball180TV/91003" target="_blank">📅 11:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91002">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_oxdKefeGy6DAqSv_8ZJKYSvbSoMkJu-Y4D4WxYnSMEZOrqWyd5vRhHPnKdmVDBmV5mhkZIgSZZnT7jSIn7sA9d-N1ltsXMIpZOBOTUTRWFFnRoK8-TMqfdzkg_SHExYcq3FOAlqUntNt_3TO3Jjkqy5-W8r-af63PigXLWITlt-IS_Dn1WPXBr7DK8b1hEayh-xuhyOdgOoVcujEeXLLnXvb3MG_TETFzFfztcBF_dc--VYPOma_-BDG1iAb1bIF0OcsVr8y7DALGADWl7QuW4i2NrBLK9Qd2gxYNBNYy8GMXHcZrfKwP4qS9VYgPZ10VLp44uz-Ubi0gOZyUNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇲🇦
پشماممممممم؛ رسانه‌های مراکشی میگن که یاسین بونو گلرشون در آستانه جام‌جهانی با نورا فاتحی بازیگر هندی ریخته رو هم و به زنش خیانت کرده که شدیدا در کشورش جنجال آفرین شدههههع
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/Futball180TV/91002" target="_blank">📅 11:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91001">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f1356d4c5.mp4?token=tMHEuyfDzKqQtQ2-HxVDqqeNjAEfOt5mOcBoxioQ5pLiSbvd8RtLEo4kkjih8vVuc3oFZ7UbickfSpcR8Nv9QRkbsqem0LNBAkJb_0BV6Pi3KlOU2iLJ_PpjtEUMsFcyCpF5MyGoazpiY1U2tL_Iou1ZiOB5fpvr239JluHagC0hOTJt9H86Ws6F1OgIc-ZxUkjhsJJWcXwf1-zIj56oAU7jPZYCzpoN4WYJwWFv01HOD_KVA_3KDUulz985SsasYLplC5GoE3Y-E24eUm1P0njuf_oYArbwqfNv-7_G_7NkBml2NPsiEtB-lB93DCIoTZq5HwQ75OwZr43eU-zbRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f1356d4c5.mp4?token=tMHEuyfDzKqQtQ2-HxVDqqeNjAEfOt5mOcBoxioQ5pLiSbvd8RtLEo4kkjih8vVuc3oFZ7UbickfSpcR8Nv9QRkbsqem0LNBAkJb_0BV6Pi3KlOU2iLJ_PpjtEUMsFcyCpF5MyGoazpiY1U2tL_Iou1ZiOB5fpvr239JluHagC0hOTJt9H86Ws6F1OgIc-ZxUkjhsJJWcXwf1-zIj56oAU7jPZYCzpoN4WYJwWFv01HOD_KVA_3KDUulz985SsasYLplC5GoE3Y-E24eUm1P0njuf_oYArbwqfNv-7_G_7NkBml2NPsiEtB-lB93DCIoTZq5HwQ75OwZr43eU-zbRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
تو مراسم اجرای حرکات نمایشی ربات کنگ‌فو کار در شانگهای، ربات کسخل مسخلش در میره و با لگد محکم به شکم یه بچه میزنه
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/Futball180TV/91001" target="_blank">📅 10:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91000">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ql4jC1aC-saDRAlV4XtxZC02lJBsfTjFDO1PJ3mWHZfubm_n1tXB8HxIX6rQ1oJeAFOE1apK4uiEb00-665famvf5Fp_EyToH1CAaTIgB_ImgxhH02zsw9IjltC5tux_fbACP6caBacKSXnFo5hobJ3TqDp9nkqb1Osm7habkEM86FG1Vytn218EgVsBZhkSu4hfpqbhWUvACAX_qES-iZfKrITzXsXNyfesoCKKDnMR3vhE8Fwj2gR-XqvXJ4rqpo5-T5s0aHy-Nwhw9tmClHPS971ts2umMQU7_15T8zKFPaNvxi6R-Mdv3jNHbGyo-vxBVCRxsCXbSA8YjrzbQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو دنیای امروز به بالایی میگن آفریقایی به پایینی میگن اروپایی
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/91000" target="_blank">📅 10:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90999">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1b7afdc1.mp4?token=ow2Ni2V1UUfnulmkCyPrlARZEfa3faQ8H4TRI7L6SpFSRcjiUPBRNGUuAKe1nMjANakY6Q6t6pp8JC-BJwEXnnv3HAPTwNeaReAA2RBrBzaEMwAVCYRAouzbydAOhPO_PSf0Zg-c18NJwv65aHUkX0NYcwzsiCpXSJqrQvkSbQNxAAmQ9-dsicXyeB6lkZ9MzYNbSyEkjpHWp0kIAW28qy8THeOcyTkfZNxAj-qOrWaUfP-QMDeKncFRckvW4d8zJNu1wpdlkzfRwJnTYemBUkInHeNJOWpy_9WCZlYGP9kWTWPecuE6ISwR7KJz513m5UUdoin_0pIzsjOi3tBKmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1b7afdc1.mp4?token=ow2Ni2V1UUfnulmkCyPrlARZEfa3faQ8H4TRI7L6SpFSRcjiUPBRNGUuAKe1nMjANakY6Q6t6pp8JC-BJwEXnnv3HAPTwNeaReAA2RBrBzaEMwAVCYRAouzbydAOhPO_PSf0Zg-c18NJwv65aHUkX0NYcwzsiCpXSJqrQvkSbQNxAAmQ9-dsicXyeB6lkZ9MzYNbSyEkjpHWp0kIAW28qy8THeOcyTkfZNxAj-qOrWaUfP-QMDeKncFRckvW4d8zJNu1wpdlkzfRwJnTYemBUkInHeNJOWpy_9WCZlYGP9kWTWPecuE6ISwR7KJz513m5UUdoin_0pIzsjOi3tBKmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇩🇿
عملکرد دیدنی پسر زیدان در چارچوب خط دروازه الجزایر در آستانه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/90999" target="_blank">📅 10:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90998">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVNjZgPJODp7PDSb9dVwn4m3DQ2OtdqUgRj83ktpUm4hTnov4q83eY4FZePae_hzJB9APjKO8yVqDXWBnF7f9sNHgoc9vbEpEwQmOmRYo-jNEulVIBoj4JJNwRIcXGJA6PQwGEiVctlh-F2C_4XtHiCTBxVFKt0Q98Iis__ZoD14Vk09ek1nYBSk_g2oHVo7pWWr1eEge-EsenQXN8WlOCX7bQMV83-luQZw80HLPjgjwVBZ6t_oE6TW3QdcW-1jXmPaVRtCCY_oR6a04Yp-5oiaHplaFIZWUAipMNmNYjhIVz-w_k8ohqAxw-l9WxzOXh-fuuqjox9PmSF9H9-iag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنا د آرماس با کیت رئال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/90998" target="_blank">📅 09:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90997">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQQk9n-c2R-v5dVN32FvHunF5t6QTW_BoxsCpWjUHuqrHjUZma38nxni6a7Nj2JW5pzC4DXAh8-WUEBUDObMqdGQZqVhOPAQkaE8OhKtd50Sl-0hhGjyp7JCyR_-XCnxL2Qi2HR5Mzv8rqQzYRhKxH9azn_G-neSoQIF-hALbLvgW0Oh4Q9Xd7ciHNoQTbLoduzTpxrcWHke20QHjBNGYjyHTXCdlLGYnEuhMj-UGZB1gLmrlRwhVEZ8AF9AU2TdK_nNVGV1YFOn_yXOJq5mADZbx5-hMNqaqaSN-5xD__USPnLisLAMH0tQc9DXzUCBHpFZWzl_E-7GSjJStIAdDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🇳🇴
عکس تیمی جالب نروژی ها قبل از سفر به آمریکا به سبک وایکینگ‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/90997" target="_blank">📅 09:51 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
