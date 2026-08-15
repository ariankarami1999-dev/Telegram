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
<img src="https://cdn4.telesco.pe/file/ms86JJlYhOMwDwdhKjAuwSRFrJM-QQoBJ4Vksim2gQxrU3u_5tQbS09L1oiDw60ecVAi5yZiRMRaE2jnu2C_fPXsCZGIP3IrOhMqtkaPNR6V7O5FUIxNXe5ZAnq61a-QFtI9g248dTpHZpDpSniHwGNFP0FaxcqsXvZFas0AStdfZsWgk4r9oo8VDRn1jJ1EkS_NYO09CIH1ob1qyPIOGnvTbAbqRAD3oiXbSkZKgwzHtoZCaogcn5VcjuKHqINO-oiADkSpnOa3Qd076Q8jUapUd5Hwvxe5vnPdAtiYzHREJQ8j8TSPI5m11kwutiYfcFXOX20n-MJDbUZzxvVp_g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 637K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 17:19:09</div>
<hr>

<div class="tg-post" id="msg-27789">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d76ee0536f.mp4?token=nCHIgSt7sNq0s_styE3MNKTrz8At1mijBgBGc9WlD5jJOaPPFRxIr3mLjlSyBu-9ls7W_pH6Z85tLLZAkT-vX8RdInspoyHYDiwcDMqYK0-HKvcI8U-G6LPOCq_tPt9FvOM5K6_hOAdS4p8nj3rGmOAci-5oHhzNu6Tha1zi-YeEW1Un71DRzw7Y-5R_tlgjW57DuTeXp3lmJbl9_YGNzJ8ltW2YfcfvJl0BVOf2ObHVlWA5zMWKQU3xiHv2JYTnxab1AlgyZgrbLjaWEScW7de3GOdDiYhttVEb88bifwpgthl8SwK4oRRYGJRiDLuudV99CSA-qV-jyTIPnt78VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d76ee0536f.mp4?token=nCHIgSt7sNq0s_styE3MNKTrz8At1mijBgBGc9WlD5jJOaPPFRxIr3mLjlSyBu-9ls7W_pH6Z85tLLZAkT-vX8RdInspoyHYDiwcDMqYK0-HKvcI8U-G6LPOCq_tPt9FvOM5K6_hOAdS4p8nj3rGmOAci-5oHhzNu6Tha1zi-YeEW1Un71DRzw7Y-5R_tlgjW57DuTeXp3lmJbl9_YGNzJ8ltW2YfcfvJl0BVOf2ObHVlWA5zMWKQU3xiHv2JYTnxab1AlgyZgrbLjaWEScW7de3GOdDiYhttVEb88bifwpgthl8SwK4oRRYGJRiDLuudV99CSA-qV-jyTIPnt78VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«گوهر فرشاد» بازیگر دورگه ایرانی-آمریکایی: رامین‌رضاییان‌جلودوربین‌ها گریه‌میکرد و ادعا میکرد که حاضره برای مردم جونش‌روهم‌از دست بده اما در دایرکت من درخواست‌های زشت و مثبت 18 داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/27789" target="_blank">📅 17:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27788">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط کارشناسان حقوقی‌فوتبال: آسانی مشکلی برای‌بازی‌کردن ندارد.
🔵
هوشنگ نصیر زاده و رسول باختر دو کارشناس حقوقی فوتبال: بازی‌کردن یاسر آسانی برای استقلال کاملا قانونی است. درصورتیکه قرارداد او در فیفا و سازمان لیگ فسخ میشد و قرارداد…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/27788" target="_blank">📅 16:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27787">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLdsD3WJb8Qo27hADt7CHBrg2Il-bULJ6OfUvsKYzhvbeZYKdg4VQIYQTKVinOx0zNoq1kZ_Rj8V7R_B3EZ_0GXHRRqA7aiJZCoSb2bjnPckFCv41WgNTBf_pHoC7EL0xqy01oph2iKGDT3LC7ob1EI_bvq6utURkH7XBJSkrn9IGdr6V7ZRZyI_YSd7sYuaX5yr17NPRjQmoezQGW4IePARAxR9NNozFMtzUg7OAYCtv3U1I10U8qDVs-Vn9MofUNxtN7-ubjBsFedRA8qcdIfI6xdPMFGdHHs6DVFYxHp--FEODItbEqcRDdlJEmK1H_JhdovgcXr2TiqFATIbYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین رضاییان بزرگ تو آنتن زنده گفت تو امریکا حاضره بوده که حتی برای مردم ایران جونش رو هم بده اما گویا ما بین بازی‌ها بفکر عشق و حال خودش بوده و خواسته همونجا ترتیب این بازیگره رو بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/27787" target="_blank">📅 16:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27786">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F992kacYh7ky0eE9OFTD1ytrZLglZlO-_RlJOokYqnjKdl8C3gg6FZ98zB03x40846iXvvQt5aCgeEwm_56_3XAEtRqO7XP2SQzzHtCuWQEZCeH-eNoZ4hXOtd6_FByOkyDvrJh3afMHjC_Ds96S_wNo6HQibmo88vjV1To5WMv3uWabS6PES1Tn9tPxcWLAOgguoXHqi4Kgx8dOmotO4jClmSay2-lznusU5CyQPeK_wfCYUL33gdqK4bKT8VrmgHNQcTjdtAXzcTq7RRd5GLugExLrY2i5zlIT8O0kUX_OugvwEnfZ-TOrJDZ5yopsT1GBNmTXPETxZde6jHOkBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌ های رسانه پرشیانا؛ اوایل هفته‌آینده‌هلدینگ‌خلیج‌فارس مدیرعامل جدید باشگاه‌استقلال روانتخاب خواهد کرد. محمد رجائیان مدیرعامل‌سابق آلومینیوم‌یکی‌ازگزینه‌های‌تاجرنیاست و درصورتی که هلدینگ تایید کنه مدیرعامل میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/27786" target="_blank">📅 16:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27785">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbcuHMmXQGF2AQdFHjuQ20Wk3JXFkwvK1iccFC5vQAXZbKtsjMpn5xQHgQXUqh6JfuRScENxFatjkAoRZodEwZOcP7S9-naBpl7T-5dUn1RxUBx5X758LthC9xt4rFxZOyRvNLyfG1pX_FxoPhEOFsnm-C2kicEYTW98WBeWc11M3zigSYeWwh2q79ayzKgQYVyuFi_zJR1xXOMEegOkRW-hTutwmKFKS08e2urHllm28Yg6_-7csT168Qz4_JH1hBo-0VsR2k7ugCA_5i0l0a0KmOPXWbTW8m_x_NOP1IT1zgFv0N_SdZPmaJPUw3FTxlbv3hLj64nLoT92g7xoKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب احتمالی پرسپولیس برای دیدار امشب با شمس آذر قزوین درهفته‌نخست رقابت‌های لیگ‌برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/27785" target="_blank">📅 15:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27784">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3GplRFnQd5WPWeCu6vvdTzDNnU4iKLwAIJF-VFm7J2dqFnna-kH2aiUqojD9NDaE1u9ve8io9fS0Zblq2xOSfiaH3XslMvGdEhpbXRxjn86vu2vz0kCsHJutXCrOT2CY6WelNN3vmeJ-wUj9KoWDDKCFJZUb-54R9GEqn4ctIxY3Adz1miFtQRBP50sT9o00f9VO4hep-ZuA50UaxMC5L3fG_hIWmDphPeskzN07LOi73kGumL7co9Yq0GVRgwnSqUe5O7dRy6MQwOfJRnXh-YE47DqZ-IICkkGtKPlYWDasQA6I3A265Pei0hzufTyLt33bQBJ6zyQ0LwATQZ7Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خانمی به اسم‌«گوهر فرشاد» مدعی شده رامین رضاییان تو دایرکتش‌درخواست‌سکس داشته و از او خواسته در ازای دریافت مبلغی باهاش سکس کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/27784" target="_blank">📅 15:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27783">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4420878c6f.mp4?token=CWyjJrpRFHMO3ZBHoYpO7trlbSVeQtG2o0unuZLFBoJXwYmCDP0W0UBAiBGM4caHF4xpUIi6J95VpVXugYRwVmHEx4APzW38m8vZVMW8-pQ_iSXu3iN1bArvUNnDK7xDqiVKbaoqxw-WqsFoaK17F7S7Bc54gzCdLvYYn9ytmQmcgiZzOS_Nz20A5bbqOdUNzM8V3RiOmCl4KgPZGX6an-yhCsOJ7FudSrzzvlkenf3JM2j7PBJMz5WZ0DwpcfFZrMBiDJz4FksRM0TQl0hdr_b2lFOZjcgxLqBb4rHjwV3jmgQBvT2pQTFSMwMh6yOC02A9b9SXEim_YPbZ1Kb7Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4420878c6f.mp4?token=CWyjJrpRFHMO3ZBHoYpO7trlbSVeQtG2o0unuZLFBoJXwYmCDP0W0UBAiBGM4caHF4xpUIi6J95VpVXugYRwVmHEx4APzW38m8vZVMW8-pQ_iSXu3iN1bArvUNnDK7xDqiVKbaoqxw-WqsFoaK17F7S7Bc54gzCdLvYYn9ytmQmcgiZzOS_Nz20A5bbqOdUNzM8V3RiOmCl4KgPZGX6an-yhCsOJ7FudSrzzvlkenf3JM2j7PBJMz5WZ0DwpcfFZrMBiDJz4FksRM0TQl0hdr_b2lFOZjcgxLqBb4rHjwV3jmgQBvT2pQTFSMwMh6yOC02A9b9SXEim_YPbZ1Kb7Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
دیشب‌عروسی‌هرناندزمدافع‌فرانسوی PSG بوده که حماسه‌ها‌خلق‌کرد. امباپه از دیکتاتور به گاو چرون تبدیل شد، حکیمی دی‌جی شد و دمبله خواننده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/27783" target="_blank">📅 14:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27782">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AObI6SftixGwqEPLlaYX2cuc6oPNJjlYNuWQKXhX5ro0gxY0m0kkBvgCPToUT_FnDPPDyzzalIxewtpT1vVGPoCrnwlp_r4CNe8Wmr3jHZM3X_tbI-kxYgFxVgBDxYYONMWBwrJ4Nl06oXVQxCUf17Jynq9FxXGqKugHn3xf5DAxyPPW_1nS25EGBMw-Nb4kmAndy7MCYvkaAOVQyKUYvWLwWbq4xh_VeAlfG3ekPWW3E02pjKzGwjiMz31SBgiA4L6oTUvGT3jn2QBpAVB8jRl8bIXMgzvz3OCJ5OKLse_Fw5m80CFOfrXGwXMuHG-4jyn-XY_TGxdOQzsQDQYZnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
ویدیو لبخونیِ لیونل مسی فوق ستاره اینتر میامی که خیلی‌هم وایرال‌شده مسی به پسرش متئو میگه: متئو دیگه‌چی‌میخوای؟ پول ندارم دیگه همون هات داگی که خوردی بسه دیگه به‌همون راضی باش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/27782" target="_blank">📅 13:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27780">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kze4zntFW01T1zHhI9H6ZPz0f6lSV4g4JwqrwoFQHdX70zMSrdqIQdr9JVyy26tTkTf0EoRpu2Xu3o3lzwrK9cCUQbp7jpajsmFjUz0OTBCQOcVtPmB7nxcWBmGIUl2i7Igm2GK592WkNRXWHyERly8yFZSLyjxGbaqIVbW_zH9NbWIpJLo9VgPoDw8eUrlDMVP6EJ3DQNA6KuGXnPSMxuUHthi0S5PqJdiWDx0RpJABamr2BqYggUb3KyZ52isyOvQ_aaaTaP-sgpH5DaNCXk1Dm23b7RgsfdBoAozWTmQt0rBw4rdQm1tycaWnMCHyt28tuJHX-tvUnKQnjQEpkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/27780" target="_blank">📅 13:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27779">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">📊
🔵
سعید سحرخیزان، اسماعیل قلی‌زاده و صالح حردانی بانمرات 8.8، 8.6 و 8.1 سه‌بازیکن‌برتر دیدار امشب استقلال مقابل مس شهر بابک شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/27779" target="_blank">📅 13:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27778">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46566583a.mp4?token=nGCFCVRJbX5IGx4ao0B-Krm_mH4Axajo80mwgSzpxkLC7WflhqNy1lFQcaaMxHvOP9NnR5DkOFkkGPsLTUNY_ImmlOesIFjvJK9MnSjdRZXdR0mx7UFbboZjzvYSYbcnRCZvdlE0Ftm54fIR8ZAjKLXo-Be6hsaf5Z-uENGjwH8aeIDib4pwdC2Fm4n9-RXNhYVhdCmua2oD_R32e6M56Anzcfd3bVtbnvdtFS5AzKwvBfoV_sKRQz86XtiiCKhm_JmVBeTABFYwuuFoNxnftW4MplUp4UU867XHPHKWrgvUA2JX6GFxG-v2pTmaSZm87qYrcVQfWgBLF9F2emVBjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46566583a.mp4?token=nGCFCVRJbX5IGx4ao0B-Krm_mH4Axajo80mwgSzpxkLC7WflhqNy1lFQcaaMxHvOP9NnR5DkOFkkGPsLTUNY_ImmlOesIFjvJK9MnSjdRZXdR0mx7UFbboZjzvYSYbcnRCZvdlE0Ftm54fIR8ZAjKLXo-Be6hsaf5Z-uENGjwH8aeIDib4pwdC2Fm4n9-RXNhYVhdCmua2oD_R32e6M56Anzcfd3bVtbnvdtFS5AzKwvBfoV_sKRQz86XtiiCKhm_JmVBeTABFYwuuFoNxnftW4MplUp4UU867XHPHKWrgvUA2JX6GFxG-v2pTmaSZm87qYrcVQfWgBLF9F2emVBjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇪🇸
رومانو هم‌تاییدکرد؛ فران تورس با عقد قرار دادی 4 ساله از بارسلونا به PSG پیوست. پاریسی‌ها 55 میلیون یورو بابت این انتقال پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/27778" target="_blank">📅 12:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27777">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoAVNLYJsQhbzLOxfM1Jb4DybSW85ddkOMYXDOuJwAsGHbyBTN0rC6bDxbS9C4XKQhPqFJgi2KpQXOy830FLgMvqSrGaakoitL5CnKk4MdF6xiUX8sWHUmZsIJeNvtPCeYthiLnGtG-KTrAWhvqMwUURFcS7AKUfY7eCYmOaufyTHUG4al0IscZ0F37Zr5OPBg5p-YYmWL8Ikqy0h-7iv_njKDoysj85SXzwmqNSetUDog1c5l489YPSyi2CbNcNKAiyuFJvFk7lTCxQp8DzvOv0pGg57KCyLWeGhm18BudogxJDtLQruREf4JemncTcgKstZoCUrploW9H2MQwq9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مدیرعامل بانک‌شهر فرداصبح بودجه لازم رو برای جذب محمد قربانی دراختیار باشگاه پرسپولیس قرار خواهد داد. مدیریت‌باشگاه پرسپولیس‌آماده‌اندتاسقف 800 هزار دلار برای محمدقربانی هزینه‌کنند. این احتمال هست که مدیریت الوحده یه مقداری مبلغ…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/27777" target="_blank">📅 12:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27776">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5fwZgAvzZuWdytjYMM-wL92SxCttp2nQims3sD5KLqVecMQaOnxqv_uHwYeR21Ja810eqLS3HN5T-ygljZT_6inseDIRaZPA0iHSZdUA8wx_AtHAR9JZB2gR3vAmrXipdOd6kumLLGKm645uTIvhfBhTxxU8x2qvmlI7ETuiiwPoBowIfZBhJI-Fmniz5uel6HdatuUqtoQoEysK_5Jmqj-6jqvSAhxP1_p-Uw7OYXdIom6Z7JlCWC98I69Etp6RhG1ZobpNAk-6ZxL5L1sHMbdH6tS1lVERLPt1rZMeeT1JvipGP37WbsiBpXT3mq5TV7crQyjXODU20kBeu3Tpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
نتایج پنج دیدار اخیر پرسپولیس
🆚
شمس آذر؛ پرسپولیسی‌ها باچهارمین‌پیروزی متوالی مقابل شمس‌آذر فصل جدید لیگ برتر را شروع می‌کنند؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/27776" target="_blank">📅 12:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27775">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5920f02928.mp4?token=HnDu_aY5YBI4C_7w4bfWpUMHMy41oI_4IbJ6KOucYGpSK9KJy4fAf8dD0Z0x8F_OWrjqsECBUrKSxMBkziDWiudxwoCssmU4NMiLD9Bw0oMhnhxx2quvwKdDsDcONbmEQS2XBiPj9gmRjyNF04WYDSz7qJ90iZBwXdVBMou0bmhA6pynTnDEO58DW1TlBQqvEd1sU_rxgoGkVJOoeSSfl8EjsablJlLfA0A__1RYkt-ZJPeObdgqLroIDsghBNeQdZb_za4Rk6KNoRpZHz9UjpDbpJAcZXU-BMimHIBloOAeiNxi-MjGRuvsIsBpUXR1SqjP6Zup77z1GheRpQ284A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5920f02928.mp4?token=HnDu_aY5YBI4C_7w4bfWpUMHMy41oI_4IbJ6KOucYGpSK9KJy4fAf8dD0Z0x8F_OWrjqsECBUrKSxMBkziDWiudxwoCssmU4NMiLD9Bw0oMhnhxx2quvwKdDsDcONbmEQS2XBiPj9gmRjyNF04WYDSz7qJ90iZBwXdVBMou0bmhA6pynTnDEO58DW1TlBQqvEd1sU_rxgoGkVJOoeSSfl8EjsablJlLfA0A__1RYkt-ZJPeObdgqLroIDsghBNeQdZb_za4Rk6KNoRpZHz9UjpDbpJAcZXU-BMimHIBloOAeiNxi-MjGRuvsIsBpUXR1SqjP6Zup77z1GheRpQ284A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
حضور هر 3 پسر لئومسی درآکادمی اینترمیامی؛ طبق گفته نشریه‌آاس قراره که بزودی هر سه بازیکن باعقدقراردادی‌بلندمدت به آکادمی لاماسیا بپیوندند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/27775" target="_blank">📅 12:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27774">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LX_fwcd0dS9ncGN7wRtOhU0h8d7_z2VHhypjDPdhBUc8eo-bLLFbafN8VtXVIgLVjzkPxgUaXMvelZHr5Uf7vTUGntQ8xGaJgSCY9RsG3JN661FYbui73zm2wN8D-BBdFDaBBUTKZ5GkiS6bnTM8sy6yQwnmVB401B0YOYYSkgu3j9bRpopgs-5F9lqL5-P9DKLLJkCncJi4SsVAtNKVNwMlQ2t6oe8ax0YeNiRqqjVspd-nSVOBbAk2Ugsa1Yntk6kYaV6m1i60NXw1Iv7pJd9FvqpFhj2TmhidkJV-MvC2rgsshK5YZU2OYkpmXgBb5bi-psFB-zh1m6mW8GHoQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛ از مصاف شاگردان تارتار با نماینده قزوین تا دوئل کلاسیک میلان و منچستر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/27774" target="_blank">📅 11:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27773">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6R22PfuRzNfVcgCN6G1sfD8CDZQ0BfbSswpR5hllVnEBBsduJ6dY6zBDzaHihRUweG6NY4o5gkhDkdLMUraTGvlaJRkfTCVPTuVqSfUQ_skKjZJ9FbE3lYqksFY6XzPASNotK6n-0kqh0SI8nmVThpEN0gamqYFTrhsckpy4j3xynTybVl6RjzCIUlOvFmfb1tM0pT1gGjLrWK2Xd4JeFKz8tvKbCuKz47jhpSnenRdsvJW_EEffd4q9-fVXbl0O4mjC5vGjDT9zm9iTxodosAPvr3A8fRZTIfNJ4fwrU2EyLy5oErysWiBYVghHYBilJR1b8B4ea8MMGzMOdYK-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال تاساعات‌آینده 25 هزار دلار به حساب جوئل کوجو واریز خواهد کرد و پرونده او نیز بسته خواهد شد. همچنین سهراب بختیاری‌زاده بخاطراینکه نازون به‌فیفا شکایت نکنه به‌مدیریت استقلال گفته مشکلی برای بازگشت نازون به جمع آبی‌ها…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/27773" target="_blank">📅 11:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27772">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eECp6p-tcD4YRbL5075kLMu24LlqxttnrcPf07pNM6HtOh11yrbACpXD5qe9iohn-v3FiEONBLgIYZlS5bL5khmhwo1w9UjkBYXdfhM0pvMmg5vVb0me6OUYt_9Cj7v-OWJzyurlxv2cDvAmBaJy4BVK6dvUqU1M_Zj3Ore07S4YuYy7FdIZE36oVShNPgk6DJyHKHMJfZjYvCma4p83YWyNEfKBL0gNCy_UjOPX8eQkG_kCSjwNn5qsNlOkD6cQWC0Zc6pFxI0zKzXoH6aXsaRKIiEzuCzq-fqJoc-sZBXddmGUSz-QZ4RN_nktktPTm4S72WbRAn7kS60UhAEzZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی_پرشیانا #فوری؛ پیغام جدید محمد قربانی به‌باشگاه‌پرسپولیس بعداز درخشس در دیدار امشب‌مقابل عجمان: پای توافقم با شما هستم. رضایت نامه ام رو بگیرید به تهران خواهم آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/27772" target="_blank">📅 11:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27771">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1Y4ssT0rrBz_wexRae9APFqZURUvSeRe0N3GqogMCVVkHGbFE95aOxLS0ohZlQuMpmeOJgumL6_cu9nIDNbgIEI4ll1xBGFhBCIQbA_hjeLSWtqbfOF_hyFnaDosgoC12YoGOYLu9QFPdaO6QGP6C1fJMLoNPw45FpC3bxtjbxo7UmgiB3EkfX5iOlfZTlyAasObUXZui6w0fThCdoDHDN6tNSEv4KHibo4xHNtfBLRZKx42dTaUjcZFYJbD9G7urACRXH0t81ifMGhxWJTweeuZe08RLVeVeEjs3xFSXpAh6ca-X6GsuIEP0MByTlOqZFXLSGFGJ8A-L6HNBISYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال و دوست دخترش در پارتی شب گذشته؛ به محض اینکه تمرین بارسا تموم میشه دست این بچه رو میگیره میبره پارتی‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/27771" target="_blank">📅 11:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27770">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebfea836a8.mp4?token=qeSuevx6Kt-AZ0gjxAjhG6HbuhuoSmMYGeAgMj-KAtp_e40_TnapEsb0178VIP8c729200pCNWMHt_mIlmVF1EkkcIJUDQ9dSJcZWbeeAfeE1jkMfRQvcHXatNhzfpHzLP_zJ2eWbUzZFNR22hKmCBzDL93tcUbdr7OFl1DiaMVgvKsuX4UeE3dlGRf6pHUXq47DWVY6dTwnHf87AlIlM5iFm6Wv6CckLuwrfuxM6BOLduMKW3_ejDXvWzU5O3PJwXHI0-ipcxRbE05y0Yq160KrEAtXphbVQHlXr76-chzFtMVtQ3gY_JMla4A7Na3S939oAfgp97qGcZe4QEJiUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebfea836a8.mp4?token=qeSuevx6Kt-AZ0gjxAjhG6HbuhuoSmMYGeAgMj-KAtp_e40_TnapEsb0178VIP8c729200pCNWMHt_mIlmVF1EkkcIJUDQ9dSJcZWbeeAfeE1jkMfRQvcHXatNhzfpHzLP_zJ2eWbUzZFNR22hKmCBzDL93tcUbdr7OFl1DiaMVgvKsuX4UeE3dlGRf6pHUXq47DWVY6dTwnHf87AlIlM5iFm6Wv6CckLuwrfuxM6BOLduMKW3_ejDXvWzU5O3PJwXHI0-ipcxRbE05y0Yq160KrEAtXphbVQHlXr76-chzFtMVtQ3gY_JMla4A7Na3S939oAfgp97qGcZe4QEJiUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ویدئوبازی محبوب Chicky choice
🌟
فقط کافیه مرغ از خیابون رد کنی و پولت افزایش بدی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
betinja.bet/affiliates/?btag=2760677
⚠️
فیلترشکن‌خود را روشن‌کنید و روی‌کشور مناسب قراردهیدمانندالمان،کانادا،امریکا،ترکیه،سنگاپور.
⭐
کانال اطلاع رسانی سایت:
👇
sr24
💠
https://t.me/+K0fAOE9hCUo3OGE8</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/27770" target="_blank">📅 11:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27769">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936415b58a.mp4?token=HxlRvY3_6v1kDk37-tXT6Rzhb0V_m24CSDbANZSsTyJa0iS7ZgMMSnxqcF31wC_-zADy6c1AJbm4QpnnuNIdJvq078cXO6RLJlmxqsX_0Q6cMPzxhlpdtdrBNUb8YtiO_h7esZ6l77CRtJrfleN_DCW65CwtnyWqZ6KIPZ_AT5ZRWIrA9i3H9dJ8t6lowYMvWRXIrsOukZHpEgi8TXJy2Uy5mZbNAkoixMzmYR4S3a07OF8EQ1CMewrXwGdb5tCE5eYsjG0iXDcRSR-lKm9UIW6vPCrUm_tmBYcEz84Cx6s7K4zBtB-cIN55YG793G-anN4tDB9NifzzdFD4TippGlUQwzJC5dCZ6hAY6GhtNjmOms2mhzlTkUOVaJbgMmUDFLsY51MyfCgtoV2a4JFzn01A8Z4ePlddHxinn8amUeLFAMfhQKleymcg5ntxR-F2dWSirU-cIbI2DDrYPmeRtzm6RpnJ97yZEYNs_F_2V7JpyGb_TPKa3Vm3puUaeOr6LslEABvzId6mqBWmeq8QHVVmZRXq92s412u5_uHN8Kh-agsCNh_N_OuARE_Oml6R_kAOW4eSxfYHOG1kfvGxC6GH8eIfHGPgDGX9t-fEXQtm5MNT_HiYenvN0cQ17RoeNA_ykvyIkeFXnWNMAyci31F2dUVQPiRdRgHBkncC4ZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936415b58a.mp4?token=HxlRvY3_6v1kDk37-tXT6Rzhb0V_m24CSDbANZSsTyJa0iS7ZgMMSnxqcF31wC_-zADy6c1AJbm4QpnnuNIdJvq078cXO6RLJlmxqsX_0Q6cMPzxhlpdtdrBNUb8YtiO_h7esZ6l77CRtJrfleN_DCW65CwtnyWqZ6KIPZ_AT5ZRWIrA9i3H9dJ8t6lowYMvWRXIrsOukZHpEgi8TXJy2Uy5mZbNAkoixMzmYR4S3a07OF8EQ1CMewrXwGdb5tCE5eYsjG0iXDcRSR-lKm9UIW6vPCrUm_tmBYcEz84Cx6s7K4zBtB-cIN55YG793G-anN4tDB9NifzzdFD4TippGlUQwzJC5dCZ6hAY6GhtNjmOms2mhzlTkUOVaJbgMmUDFLsY51MyfCgtoV2a4JFzn01A8Z4ePlddHxinn8amUeLFAMfhQKleymcg5ntxR-F2dWSirU-cIbI2DDrYPmeRtzm6RpnJ97yZEYNs_F_2V7JpyGb_TPKa3Vm3puUaeOr6LslEABvzId6mqBWmeq8QHVVmZRXq92s412u5_uHN8Kh-agsCNh_N_OuARE_Oml6R_kAOW4eSxfYHOG1kfvGxC6GH8eIfHGPgDGX9t-fEXQtm5MNT_HiYenvN0cQ17RoeNA_ykvyIkeFXnWNMAyci31F2dUVQPiRdRgHBkncC4ZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ درشرایطی که ماده شش فیفا به برخی بازیکنان اجازه‌میدهد خارج‌از دوره نقل‌وانتقالات ثبت شوند بندچهارم ماده ۱۷ به صراحت می‌گوید باشگاهی که با محرومیت دو پنجره‌ای روبه‌ رو شده، نمی‌ تواند برای ثبت زودتربازیکنان‌از همین استثناها استفاده کند وبه همین دلیل‌باشگاه…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/27769" target="_blank">📅 11:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27768">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq8QY5MSJjIR5o5NDj22UTIMtAdnqDAD5r2bPuzDKQUImveJjK3PqEQnmmbNZZJMhgkiiesDXuxEt5wiWbcsL3LAfmrhzJn7QMCdPYVtVsULAiirYxA4PHSutJ6QqF0_ALHxG4S37YbAStnysW6fYOeMR4vxBxOsQKto6P3x9JjIcdN3zi9NEAnMVUnCavFVSJpXS4q5MEHkCcu8iiwv2nZVYmouE9rgCadaJG2atzCho8uxwTmi_XnJbcRZs5d3ynI-HM7KneuZRW5jNOqoCP-Hmh45FbcTYciBbiLDYbFbk0FZU4oWcPYNpr2Xn4CEcBL7ZgMCdpS4d4I75RIa1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ امیر جعفری مدافع چپ گل‌گهر در هفته‌پیش‌رو برای‌انجام‌مذاکرات نهایی و عقد قرارداد باباشگاه‌پرسپولیس‌راهی ساختمان‌این باشگاه خواهد شد. حدادی با ایجنت او مذاکرات مثبتی داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/27768" target="_blank">📅 10:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27767">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4107ef1526.mp4?token=B7p4eowpHQSoCgIxJ9LN_0o_ZswEcWNiwrhXrfAYBjf0Wm9dlHUWpw7L3RdzIjyjK1T6hv_6gD9dB75xmA2rk1LA0eFhlMMYYuBMKvAdZxT_1wBrtdSwldRUQXRne0Cm7kfJVZjsVuM6kHsQZWuRhwa_xj9cr-S2Yuf5mWNyk-L9ivn5jByWyIaYKxoUmAlQrgfX4ietgk90rlN-PRhsArcDv4tbIFRxNltoDlPOIJWGuezjBcyHTY-FA8utu2YKxVuV1-R_a2g8T56BMXAKWxho7tYW7e5K-kdgDvY6hl3zpAsEtLLkmX5_PTpdquLUXyxUslAaokSiXyemgJzjVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4107ef1526.mp4?token=B7p4eowpHQSoCgIxJ9LN_0o_ZswEcWNiwrhXrfAYBjf0Wm9dlHUWpw7L3RdzIjyjK1T6hv_6gD9dB75xmA2rk1LA0eFhlMMYYuBMKvAdZxT_1wBrtdSwldRUQXRne0Cm7kfJVZjsVuM6kHsQZWuRhwa_xj9cr-S2Yuf5mWNyk-L9ivn5jByWyIaYKxoUmAlQrgfX4ietgk90rlN-PRhsArcDv4tbIFRxNltoDlPOIJWGuezjBcyHTY-FA8utu2YKxVuV1-R_a2g8T56BMXAKWxho7tYW7e5K-kdgDvY6hl3zpAsEtLLkmX5_PTpdquLUXyxUslAaokSiXyemgJzjVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🇦🇷
کریستین رومرو با سران اتلتیکو مادرید برای عقد قراردادی چهار ساله با این باشگاه به توافق کامل رسید. رومرو در دوهفته‌گذشته پیشنهادات دو باشگاه آرسنال و بارسلونا رو رد کرده و گفته بود به سیمئونه قول داده بعد از جام‌جهانی‌راهی اتلتیکومادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/27767" target="_blank">📅 10:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27766">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVzZ5R7um3-BfDCPfT2tpEyVEXZvHQrWR_PU1J3GefrZPIFrSWTDTKNynobnKQYDzqPP1FfIvPmDJutzvwnwAczPxd7xEfEsH1HWfM0EmGeb9NuGqjJcnxaJffkTcNrqm1_xLIRyzqIKXmhGxDq5dSkhWJD1FClz2AMa6U5nVi7x3f217Wqjp0EBVStyzAYzZHo79r5JiSRUfyB2Dz-Z3FdRdK30VJmlQnU0LkdgZj2PZyU913qANHlyv42ZUsc4EikCmPyliYYzhV5k4ZpCRKn32zTwdM9Y_P4w_0sOQSYX6mJaxMYr1m3YPiesvv_pPljjnzvqwdJmXGTjcncArw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعضی‌از دوستان این تصویر از بسته بودن پنجره فرستادن و میگن‌که‌صحت‌داره پنجره نقل و انتقالات نیم فصل نیز بسته خواهد بود؟ جواب خیره! فیفا از نیم‌فصل سال‌گذشته آبی‌هارو به‌بسته‌شدن دو پنجره محکوم کرد به این شکل یعنی پنجره نیم فصل سال گذشته و پنجره تابستونی امسال؛ پنجره آبی‌ها نیم فصل بازخواهدشد. تاریخ بسته شدن رو نگاه کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/27766" target="_blank">📅 10:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27764">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_JL1NPFeJZt4laWIMpM0aiCeUX12nIGPWtIvr675Mhl_e8H0p0eo6rmukvPmmNrKxTl2oUyhxTGir24pa6jMZRSjN3HRtL9D5qKp9H3zVPWtvP8-RSGOTs6sCu4IWQHkz-a-vWFbaPF1OBILPI9PvFuyv2QIGPCkrzvZI_O82CPlf6SxAzIJ4GIRhMKv7tEpFTqebVcOvK8hFLMhahYfeAGycX-FBE5bRI74vD7a8p4igDz_v5H_KtdIHK57Ty19NOXAnfLCHBzQQ3vnYtTMBJfHyBae64drHwYCsZ0tKEi14-ADtc0iTHfo22kMuuQlaoG3kwTVhMzY9ho2idOYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CYri7D_bRWu-FnICbutanl8Vl-9eahtBhnCaefymrLp65Jnps_bZjkVYyefcloMTJNnlVOlLbH7__qDBKdUTXjnDspm31wZgtgYx8oVKYy9aDCSmJTjDh8ju4rMFTLnSusSn5BE5tsuN8NQXUdrdd9kWDS-T0vIjhsYaKQNXPFocub3-57BFJhN4bfjJzIH0deLFGHArAMNye4I19m9tz8WXogKbd0uv2DBeWfQhzGO8UGyoCHJ2b836oH1yGvHYZJ7MqErNnuU12K-cEsTlpg2Fg88RA0_1_z3LW8wtn5eO9Brcf3l922h-qOe-SOMhyHyMKL5hOERb4HryrzsAzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال و دوست دخترش در پارتی شب گذشته؛ به محض اینکه تمرین بارسا تموم میشه دست این بچه رو میگیره میبره پارتی‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/27764" target="_blank">📅 10:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27763">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBWIhe-KzSKPiKlSc3YCX1UEHod7vOkXQul-pWMKiQIGDEqTdsQa7R2rB-8kHCwr9dVndrSep6ujPsIym33kqRYYHgZU5sJlEn1Y-RIuYfap92rTjsgn0V7bLVA1AHjOywBxz5h6-rbd2zbiN9WcDnybEiOtcetfwUJnZBapoP27gP23dTGWvEjQ3LJPrnRBbQAxy0s2_CApvCTP5nmpRBRSL1n73DX_faxsOcnYEp10y2l5GgEd4XUF3k8NN4Z38wkEA9WGDgwiQO6luiYzIFn1fJ5i2ofX3cGzAyc0VcCTcWjV6AVRqQn5j2D29_fXm2rVSKbRsPOBQasSD6MQ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
حضور هر 3 پسر لئومسی درآکادمی اینترمیامی؛ طبق گفته نشریه‌آاس قراره که بزودی هر سه بازیکن باعقدقراردادی‌بلندمدت به آکادمی لاماسیا بپیوندند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/27763" target="_blank">📅 09:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27761">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1Y73LJbIoNkPjW1xaD2rC8Z5Oyoxc2uk1EY02-gQZqexJpzrld6PkqjNzjl3RCIhWSI8F6gu3ZglUKxw-f6bARtWSn5AKP-17UuWDU4jjJ-dSTY6Ysqf28arhGbmLNGwbSW1ytWlZNB5Eu7GhlBJLMX8cBI0uPPAIzx4DaT8j37-BGb8hOyY0pqhv13ogsse5G1yCx2eP7cyi6C10O6hapeZQ06OAcObr-8CX7Ss5TtgSfvrEf9GdG-6uvWP9iglUuIO2SbR1hpsotUF7t6ir4UyvaPgrskx_sPsPQjDP55mbSGVX0kq1TsKaAPEzcmabr23QnOGJAI8V_MXN9HDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌برتر؛ استارت آبی‌ها در فصل جدید با برد قاطع مقابل مسی‌ها با دبل سعید سحرخیزان؛ فرعباسی با کلین شیت فصل جدید رو شروع کرد.
🔵
استقلال
4️⃣
-
0️⃣
مس شهر بابک
🟠
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/27761" target="_blank">📅 09:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27760">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljvGZtsJ-Ob7hSbo_IJqZndI1V1jsSXl6W-ih1pF3cU-b1k4LS6knppEzAvScQXzsJfMVq7H4bbtq8DYl6Z9vi1fiE_DlL3SDiuD26NHtx9FHTmh2pTZM3pJjp8dNC3W_mwF9cAbzDBlRZIhbVmNE0GZnuz1NwIwtMS8R6Yum3QlqftTgQezUgN1Gstznj837LbqaZz4pYCWuU_AvSb6aE71aqkfh5SE90d71qOHoitTv9ZFDCLpnio2aopYBsGYY1LHUV0FPqDLXLPDgGvavovlQtD7RZJQObqVgyLbWR1oohqDraZrSB1TSOdl37LcrMA1sDmkHq0YNXr3j3X15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مدیرعامل بانک‌شهر فرداصبح بودجه لازم رو برای جذب محمد قربانی دراختیار باشگاه پرسپولیس قرار خواهد داد. مدیریت‌باشگاه پرسپولیس‌آماده‌اندتاسقف 800 هزار دلار برای محمدقربانی هزینه‌کنند. این احتمال هست که مدیریت الوحده یه مقداری مبلغ…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/27760" target="_blank">📅 09:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27759">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3eb80a731.mp4?token=IfcuoAD-0yJPdnzws-Kv-BkEf5saHHsa3a7vnvkO0JffX46HUT1WP8TK-_3L-MQZneYGi8OrWNaxIsEaRpcyjqbqyvAj-oqZ3mI6Vcn1bqvc6qg8nvHoqD0OL_5dbnVbP2Eu_ICIxvsOQ6dc4F6enD1qjdBo_ZZdPxOO1R7fH3v-guGJuSs0lx0zXVvROvD4sAKVxvc07XRnMc82DF-DDjyuvuMipVKSHywwd8_7GrCBMW_U-XZelVT8xLhZlAhYnpnUpT6B4VaRUKLxFzQpcKQDZ7PJ0MNSOt5xthZIRC610UKd7FO3QtNf7I0OuAFYdfxNb53D8UBam7IiS5xTRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3eb80a731.mp4?token=IfcuoAD-0yJPdnzws-Kv-BkEf5saHHsa3a7vnvkO0JffX46HUT1WP8TK-_3L-MQZneYGi8OrWNaxIsEaRpcyjqbqyvAj-oqZ3mI6Vcn1bqvc6qg8nvHoqD0OL_5dbnVbP2Eu_ICIxvsOQ6dc4F6enD1qjdBo_ZZdPxOO1R7fH3v-guGJuSs0lx0zXVvROvD4sAKVxvc07XRnMc82DF-DDjyuvuMipVKSHywwd8_7GrCBMW_U-XZelVT8xLhZlAhYnpnUpT6B4VaRUKLxFzQpcKQDZ7PJ0MNSOt5xthZIRC610UKd7FO3QtNf7I0OuAFYdfxNb53D8UBam7IiS5xTRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پریچارد کولون بوکسورسابق‌توسال 2015 آسیب‌ بسیار شدیدی به مغزش وارد شد و پس از گذشت یک دهه‌سختی‌دیروز درسن 33 سالگی درگذشت پریچارد در تمام این سال‌ها توسط مادر و پدرش نگهداری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27759" target="_blank">📅 01:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27758">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Op3NNYK1fmzkyDnyaKOKoL3167H0bBki0_uj9SC5-3P6_b7hpI6iVFzl1ieDHUnFhE4Zr61LgtxQaeknIs08ipBBB3Wwdj4qwfR2hKAYFgVf-JInwSnZhfjHIexBcmU7vtOTBfZypKZ0sym2A_iADdGMY_z3QUtWKmnDYOqzIePLtTh05CSuSZ70xgmKAxNYVfYHOfw_ZUg-JdU7EvtpVq9ocWPd_iRpHKqRvPufVL26sT_NMl92kS60zncafQ2gojtvka8p0CX4sW6YE94bJuUIPgUZM-A8XcYfiB2t7rJDvvAqxFMsxn-JzR2fykmr-cEOf0ipb2OJT6tlqylqyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اگه‌میخوایدواقعیت‌ماجراروبدونید کسری‌طاهری و دانیال ایری هیچ مشکلی برای عقد قرار داد با هیچ باشگاهی درهمین‌پنجره ندارند. دیگه از فیفا بالاتر که نداریم. استعلام‌گرفتند گفته‌مشکلی برای عقد قرارداد با باشگاه جدید نیست اما چون مثل انتقال پوریا شهر آبادی و پوریاپورعلی…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27758" target="_blank">📅 01:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27756">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl-su2kF-lvuzP3244zvdTXx4GA66qG8s_FDSrbFloBn08Kg4ZDO-ci1iCwUzIxK9_kyiWqS7DSHuGxAH1Ms83_RHxK2xelCyCK49J2ksAP-pukWTJDqcS4raxLV0asnp-1g5bUq303NYYVU9HrrXbFOtYEqZlKhfep2EYxo2yKWnnxvGrvNHffRu16mWmmY76B4qWiC5tAULgWOP8E7jmTy82Xm9SXl2z3ELoath3tJLMpFr6EHKD3RKwlJbCalJOVduyky2vp-rgNKZukhd5ObX6okMpOIHpAZ5JSrVnSDgb8ZjDw_d3MPoG5xV5sP9fJRZMMGBhugSRc3g1dCZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛
از مصاف شاگردان تارتار با نماینده قزوین تا دوئل کلاسیک میلان و منچستر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27756" target="_blank">📅 01:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27755">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvyReSWjKoDgwtGhxPZuB52ZGjw_upWT93FbYsOP8tVvjammlcPuSq4SRnKX2obPyuMVGibfuNFSSfFrH_Q2nztPJOZjWJNfAAihMQ45Qfcp9qA8P-qjaLWgZQjg01Rw1t3tHxeBYxAfRVTy2Vj7Fa0FNc32XeDekkBOIAywR60Vhy7uCyL84pZ4HKP9XN39O9wheSQgKG7jSjR8JwZeyuCSTjFE5q7mkhUxHL0mWcOJo_kQIV_WIxsuMK5W5bk4mCVp3UqEQff4q54yXmhK9NQJPQZBs-TgIIbh9rWfvB4LKPzh-ByoclHuglXBIYOH88G-BEhsp7D9rWA-SacZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدارهای‌ دیروز؛
از برد پرگل آبی‌ها با دبل سحرخیزان تا برتری تراکتور و سپاهان در گام اول
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27755" target="_blank">📅 01:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27753">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuiOT7FBZ4EZ5-ncpovnASrctCvJIgMVZWDjwx_LIT6xXQgiI1qqbM-nIs0mUIKiiZywZi-MISg0Q1IYQRuT3X92DpWQqFN2BL0EdMolY8wi0kxpRr5btbk8Z5LZQX8YCRHU8Tj7Cy1qLwe1Ue7I5v7oIEPj6AwgS2isxQvQHOxEkfonW0I-haruUWN5LEdfPMCS4Ha3NE0K7Ng7qRNnB85NYRsOi0OVl7aW-8XmNAmda5dA5tUJWTFIQJPv7zehw4_OxPvGUezust3TmoMulX86sPo8yTaAl4N6t8kTyws8t2PRswtDPEvh-LtXAbhCFxf7Z_7Y3rbqiRYc6SQoNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#افشاگری؛ علی رغم تاییدیه فیفا مبنی بر اینکه یاسر آسانی هیییچ مشکلی برای همراهی استقلال در فصل جدید نداره و کارت بازی او نیز صادر شده اما علی خطیر مدیر عامل سابق آبی‌ها از مدیران تیم ها خواسته که در پایان هر مسابقه بابت استفاده کردن از یاسر آسانی شکایت کنند…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27753" target="_blank">📅 00:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27752">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-xvyVi3SbLYN53iO7zERgLCDZ2ZJC99Ds8zi25LgIAMTc_4ha0HtFSy4dYVhDekxc01Ht139K6Oz1NIuU6kUZYGT0ARjJtajCpor-iU8S9dtKHEhJ2jexNrWsJOiKG35bFi0xTxAaAqwEgBpKKH48I8SdW_fCDfbYHF8JlU5jDhSjMQEWkzK6Yrkye3hs98qvtljlSPKNtdr8WZKt-P7I20bHDz41unWwg2Lk47yB3E_iSzhNMq2qAgtuVPZN4K6JsNmA82htPHTvozMWugp75xkdmRfOCXIcqRa1NsjlAx3R-KDO06YySsOAtnAFeKeoiR-5IVpPvghrv4UyvHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس پیشنهادی‌سه‌ساله به‌این صورت که فصل اول 55 میلیاردتومان،فصل دوم 90 میلیارد تومان و فصل سوم 130 میلیارد تومان به محمد قربانی داده که مورد موافقت این‌بازیکن قرار گرفته. قربانی روی گرفتن رضایت‌نامه‌اش‌از الوحده تا روز…</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27752" target="_blank">📅 00:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27751">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLA2J1V6BrzHMFm8htXoeCZ5IIyB00QSH_CYP9vzNaspkIkglw1XUWaQavuPAY5TRACnl1CBkZu1twBYnyqoNCF8brHI9B4piosAOC-xTxSR0gCLrpaWId9oXUqWB_PIabQhaUq73tTrLrdyUhbzhptEYDm9n2TfOBamGM-T7w4f70pkFujRYEroJKZdYrqXgNCElOXOp6qgx8c4U0Sb4ytUoJ5DR2bSUJl6UOAVZfZEVQqoYP6Y0rj4c4hBYbQU1bBfMjhm_3PEO8iy_fWUC5kHbKvniYcsvf6H1dituT_KKCNctjZxjkxTTPAuj8MnOnC5aQxBjZ4KuObjrYjSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور که پیش‌تر خبر دادیم؛ رحمتی سرمربی گل گهر امیر جعفری مدافع چپ خود را از لیست این تیم دربازی‌امشب بانساجی خط زد و اعلام کرده این بازیکن میتونه قراردادش رو با پرسپولیس ببنده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/27751" target="_blank">📅 00:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27750">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRMsM_BZaARA7eMktjae2yZvxEVG0zovG9MAxnQVWW5ez6rqjeh9rhxtvH2fjchQ_xdUkexZbZht0gvDAw6OXfRpW4EXPNw_1_eONVL98u3jjNNQyp3TtKOTU2tuNkSJdKFM-D4DEZxhcmuLTE0n7wjkLrSHLFKnaihp-7viAQLmxUGUcQRffSkdxhRPRkWA6V7J7-Cy1v-VcmBu5ntt0iSg9_QK4VByfj6ZAfATwholike6vYbE0eYf2LfJqqZ6X8BCu56cpumh7UhxxG9DBx_YOpjMlpCnADKGpFzCaEbvTKedmQEt0rsXJhv2WYAcM6Cx2jN5_ZAv0NhxX0VkpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تصاویری از رونمایی باشگاه پرسپولیس از کیت جدید خود در فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/27750" target="_blank">📅 00:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27749">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsxTuIS7L7nsuWFNMOcMlA-yqEkRBLyuIG9fVVEd_HZhC6MIFlBHEPW4M1TKo53X8Fjb7e-LmXStm6apI4QH46HsRkfpdvT9OBaGgOBQ8kXomE_2OFSxxlwU_NvOpsErIwyVKBEggFNjmGCxzQ98m84qizJ_YYDMgUIqDV8gcTGGb_B_3FqwSI3eqth2oij-u6EeDoMfZnlK-cJxsol_4q-c1u6XQ9ltvUUKSN4i79e_4_W29jBRtzJ84HsiR1DevK3e9yEF2zPrTKoQ7TUAFMr3hg4m63Tj3JBTooshiPRPf4sj4TZRYv36n0Y7LWhJkfE4O04OVF0xRY5b_id7aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ به احتمال زیاد بخاطر بسته شدن پرونده داکنز نازون و جلوگیری‌از خطر تهدید شکایت به‌ فیفا مدیریت باشگاه استقلال هفته آینده با نازون توافق خواهد کرد و او به جمع آبی‌ها برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27749" target="_blank">📅 23:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27748">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=AVWBDs6DnGb0FdHoVv-whh6HxgkhmK3c4vMC_yHtf3O27_QBliyX3-ZFi8_M5rEbLDAECu8Yl0bZJ2kynsv76-M3jZ-fffaTsgpqcuxu1cFvNLKsbHFwlVtTzXi8lWqYnSteleD9hv6dTFRGRFmKon531lUk7FVt4lRY-vrGc1PYAPSo86uQCVipM1jKel5x7MZEqXOVsx1tBSyCdpfCl3k0DSW4cfKcCmT_HqJ7VMkFBZCTRzEGLN7eduD_vHszAdIPUmnWaRf1o9-qz-Z-zs7K9GqddYH756wVT3Yk-HVfVg1q2VLORZ645YOKP3kqqahZjutgwr6P7u0qgFkdsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=AVWBDs6DnGb0FdHoVv-whh6HxgkhmK3c4vMC_yHtf3O27_QBliyX3-ZFi8_M5rEbLDAECu8Yl0bZJ2kynsv76-M3jZ-fffaTsgpqcuxu1cFvNLKsbHFwlVtTzXi8lWqYnSteleD9hv6dTFRGRFmKon531lUk7FVt4lRY-vrGc1PYAPSo86uQCVipM1jKel5x7MZEqXOVsx1tBSyCdpfCl3k0DSW4cfKcCmT_HqJ7VMkFBZCTRzEGLN7eduD_vHszAdIPUmnWaRf1o9-qz-Z-zs7K9GqddYH756wVT3Yk-HVfVg1q2VLORZ645YOKP3kqqahZjutgwr6P7u0qgFkdsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلیل‌زاده:
اون‌عینک‌لعنتی‌مال حسین کنعانی بود و دادش به من‌که باعث این ماجراها شد اما من بازم میگم اون گل آفساید نبود؛ ویدیو رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27748" target="_blank">📅 23:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27745">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWyvciNKwdXd6ZLeHUiktHHlYZSrXl8n7bJTKRKcWCCRhFQQ79sQ8RYaaJINdhFl__GflVjEUvsuscNTUdTNsGFy8fXavizU5_tvWRLUcbNoooUqgIuh1uk7jhukZjd1Dm5foj6f6NZQVU1qiImpNmiPAXc5mpuwDKaBtLR-C1fup3TNUcoGNF7_HTnuN-oaiSNXHUMbUVpsffEc-Ni3HYD1F1ADtxRcZbMa0kGjDeME4yXG9QdHhkXdH05OgTVjkqaKuh_8VsTfVQjPwhUJ7E7ztMeOwbWGsTQEmKvjVJeTHePzbZNXAt2qOrJfc1GfVXWJBT9ceE41xBZfGYJOUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lHASf1AyKSECVI4JiHr9IldFy9fb9iRAKYcoCOyjwtC8CwhZieitnM44yeNbizEHh5R0CH0oihOdKT81GrWibnDmD1OROty7sc21rSaMIch3EsGP9CsHXLKaC2JOwSzJXUGzk0gTW_YB06ZAMUDgEofVMUCTDnZK3XfuouEFh1ixtSlnoBi4OjbdbuHiLPEtbWxvQP28oTzB_5tZkzs07zxee8xxSoKQoPu0hu9-QuE5bcyVGG0EUaTOhEbw13HWjLPpfAMZkdi5rV-G9yb7miQaTHJm8PLUamPYqjJV94q8JOwey8HvAX1vLAYZHRU8wedYVohUSVYMw0MwNF491g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
دو ویدیو زیبا از فوق ستاره‌های تیم ملی والیبال بانوان ترکیه با کاپیتانی و رهبری زهرا گونش که اخیر قهرمان لیگ ملت‌ها هم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27745" target="_blank">📅 23:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27744">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foc8G1KxWxP9C6z8W9CXYzQsxwJ1JQcYO0Idhi25YfnN9PsxW7nFKElYhNQoD7bXP7srUwmmgw-BGbo-bi17ozxP_0esVqvZf6LawdG4M0Tp0IuXJ82Jc1arZhwDm7wefjtkGz5upQukcjlHR69nW_mW3uehxwTsQyCsmvjWb-RElBWs8_9HYibLhThIQR6tQ2z-K9EnbFNHRET4KhNfJZDpbMX41k4CTnY5lamON-C4Q9LQ3i18-GW-2GX4e6HQGSJixb-GTAetB06KPaD8GrCKlubJyRiC9uY4i-8DMNJkwTAmLd5-Ma0HoI7iVl0qLezKwAQv91C8KJb5xpQXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
🎙
محسن تنابنده: وقتی‌حال‌مردم کشورم خوب نیست سریال‌ساختن‌ارزشی نداره. دوست داریم فصل جدید مجموعه پایتخت رو بسازیم اما شرایط جامعه به شکلی ست که هیشکی حوصله سریال دیدن نداره. هر زمانی که حال همه خوب بود میسازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27744" target="_blank">📅 23:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27743">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhqt1Jx92yzmaKr6TSUMtLvFj_BuUDbw-OJXS5-Wil1XBaIZ6r4EEW8ygur54ZTczfP6H0kBmgogiecgFM9RUSdJF0XPwMOGM7r7d0hIUQW1oGv_nYb1EAg37tQJ0-DfNeNtjIWcLDvAFevFG5vscUWF4yMUW_1lmaImml3navax0vygscB4vwzc_TpI7MyJlAdHsuzm-05s2As1aXtAGJlEV2J2h1Aj39LAICBmVDz1MX6HyGSVHLiOfjvDiQ92wrumVh-tBSvm8Z04_FoRjlR8D7Smo1GZfRK3bvfxEE7zmIdQIE8VPm1fOHxnJ0zkRExfey5N96mOEzq2mP4UAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس پیشنهادی‌سه‌ساله به‌این صورت که فصل اول 55 میلیاردتومان،فصل دوم 90 میلیارد تومان و فصل سوم 130 میلیارد تومان به محمد قربانی داده که مورد موافقت این‌بازیکن قرار گرفته. قربانی روی گرفتن رضایت‌نامه‌اش‌از الوحده تا روز…</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27743" target="_blank">📅 22:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27742">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsoLlcVlOvFmwW_OjE4nPOl_vjc7ORxvZSk5Mj2zerYb33fhhBZYS9Da5Gs4gbbT9dizRzZr56GcMreLLIZ9nXxL_rBlSh5kYni4WwUasGGO6Y0Xutu2Q-PUSeu64YMwdHEHh9bRy7qgroaoq8YyFGj3cZzoew8QHewvP5SOfnX5zCa0DCkvMoUX5MteYH0-h0GFxXAucQEMbE86jj8Pt_UeaQop5iVN3yEcCLrKI_W9HChSKRFilP_dJoUhCbq-lt-Djnq3yYxD6eJDiUZpVjfpZzRc2UnpX5LAiIdQs6nz27NMJJa2J34XPsJsDV7GJRxx0MnTnh2x0jRXYWvPcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#افشاگری؛ علی رغم تاییدیه فیفا مبنی بر اینکه یاسر آسانی هیییچ مشکلی برای همراهی استقلال در فصل جدید نداره و کارت بازی او نیز صادر شده اما علی خطیر مدیر عامل سابق آبی‌ها از مدیران تیم ها خواسته که در پایان هر مسابقه بابت استفاده کردن از یاسر آسانی شکایت کنند…</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/27742" target="_blank">📅 22:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27740">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LslJ7I51H6UhdRX8lJgFh-c0Q9AxYHCOQS0pC7hW5qqPkRP3EgdLiTng2PbhpKzfj1vOIeeB5KCZt-4TtIzUX384jA-lq6GNC4sdnZzR-AoF0JnaBJMhmqyAayXNbB9UnJDD8ZclY1jC0gTus2p-QgWaLSgSxItv3WOaKZecA3x0ZqZeaURezCH2URQap8S6N18rfl47xQfTRPBe2ldD6s8LZRKKH7VnO15sNsTI_Huqkzo3C-f2042v6joAEX1SG4pgZkhmy1agmQQDVc0XnhJ8UEbuIaLVmmoCDzfZq4QO_xpqMofS1D6Nuz0zjujrzr18XZg3NgLM82LFhmI7gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ey2MU57BgYVEGTwUq0shWbUeyWCxrQlsfqJqd0lykAHwwnW5Tf-iu6II-PDAAEItj9sFhF1MP6aAn9h1qLAkIxtorSFExYdXt5Sa8BArhDu4sLow4tU2V-BcGsTrmhc3HrfvJb1cXoNaJOm0Rq3hdF2LC0mheXVgZoKNRacy_WVHHJwpn_4Ksqb3Hm3SuurskPQuxl9uTr_3kv2dJtisng8bkFfWoSjJQHbtWDzCnlESqj3j-APrSzuNxsdf3S31cbyhdIoTvhnX7g_FUCdciRgDq7Uwd3KB1dSUs79XB_t1vOXTx1XMLfjQga_4d_kOww42ZfM8zaICD-O6e9rV1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔴
رونمایی رسمی باشگاه پرسپولیس از کیت جدید سرخپوشان برای فصل جدید رقابت‌های لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27740" target="_blank">📅 22:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27738">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jxEOEzv9YiAnaHfbs_dIVKsPK2zf4CHGbMQKcvmNg74oybQ0jRjLHGbnh3o8lvpsWUPMkLC-99U8NYA5z_bbQyvhtc-UqeFegWnT-9Tx0-dvJVfNIyIe0i8GjiqTLPBApekwhFothp59vA3sYMY9hC9b19R_csFXmIDkqDrlggWA9YW9ozm-QtLu0Ds-tMZh6g48-QOXQzffxDqAO3ctQmVE34Yb3xM3juOJwwvwyjBJKKxeTaYWvq7gfpjCfFeIjCdcBNJhp5YZsVjh6I-NRbvtz-Moqm6Mfyo7Tuduk1WRvyGSnufmFQUt1ONMBfyDMj9U0EqbmR-XOIV4BqJ2Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICnBi2_CIUi7uTSgzyHHEMumWR6J47pkHN21PtU-uf-3hPmot_FsgWAgD83_WNZVf1Pi7l6kGJk0HaWANHTKztVrbK-bah7KpkFEMlDRB1XQm78ioKoqj8ARt7YtS5BUOP8fpXgeVdFy77Dca7ZQi3zwL9nlYhDbs5KMyDWjPpZkfpEaO_0PhG9SfoV8auJ1dx-lGN3QcO78vHw4D7aIe-TXRcNLTks_p4-Owu_FJUhSx37OyAkDT4QZ-CxIMA7-sGOFOJBei9u2sZO0Z_pIN6IxYR9DFGOfSH4q02qNCcf2rCFrdV-RX2uehGJ5Ev_SrcMrw8Uvu6NPq-PaGBQBGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ سوغات سه امتیازی و ارزش مند شاگردان محرم نوید کیا در یزد در گام نخست.
🔵
چادرملو اردکان
0️⃣
-
2️⃣
سپاهان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27738" target="_blank">📅 22:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27737">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b99364b6df.mp4?token=WlK9vq3YaY5CS7vRMu1iSUkeG_b9h3vHfxm9jXChYkxp_jG6A6DEmlVxI6WctWWHVG0yzuKIlQQpT8cyraXGI2phOPMki45QTjK3_uuapEIYLpLsQjza0N1XFfJJ1m3rq3ipWNdmGTfsbWcq8vvTZz8FO_QBDxjv0VHiTi2MYzn2jjd7__RbxRrJq74Xl3hEv1qNR0OQcQBELjya9Tx1trXDua8_1o4Fne4EDIiDUEoFSZjWy_qU73ut6N2_SjDY1bNWrR_fC2x89nKDl_2gkDNXXfMt7OWpX60Xkk_SNOzG2u4EZzgmZHcyzCkr8tH-Se6Ft51gsQUFYgLrXVYcEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b99364b6df.mp4?token=WlK9vq3YaY5CS7vRMu1iSUkeG_b9h3vHfxm9jXChYkxp_jG6A6DEmlVxI6WctWWHVG0yzuKIlQQpT8cyraXGI2phOPMki45QTjK3_uuapEIYLpLsQjza0N1XFfJJ1m3rq3ipWNdmGTfsbWcq8vvTZz8FO_QBDxjv0VHiTi2MYzn2jjd7__RbxRrJq74Xl3hEv1qNR0OQcQBELjya9Tx1trXDua8_1o4Fne4EDIiDUEoFSZjWy_qU73ut6N2_SjDY1bNWrR_fC2x89nKDl_2gkDNXXfMt7OWpX60Xkk_SNOzG2u4EZzgmZHcyzCkr8tH-Se6Ft51gsQUFYgLrXVYcEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سوپرگل برگ ریزون و فوق العاده تماشایی اللهیار صیادمنش در بازی امشب لخ پوزنان در لیگ لهستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27737" target="_blank">📅 22:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27736">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80eddbb6f7.mp4?token=F6Chqvcv-bVknGZ8SZz6-lA7Zs9-gL1QD5B0-fIbw3dsrzg7Rk_LgE_PE5xMXMRLGrIveVvOKTTJr52-PXflNdfBX93nx9sgivHeic9DWZ7S78_1m4tSG8M1SKSmSUoTl81SNiFRcXT8vnySbstl0mG-syiTNFTYSYHHxds-rGSw8dYZhaRjZON7k99uDWr3zrCcZVWzmyLP-v4582wBrR1D9xciqnFgxjVaY-JjlqzlOFgdOXyJTPuPKzAs1cgNTg_MtSGnOB1BNK58Bjwc-beizu_ft6uhwjX7JULZz15CTq2SkG_RMR37gDOwPSCKYtz8FeHnT4s1j8_ODwODig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80eddbb6f7.mp4?token=F6Chqvcv-bVknGZ8SZz6-lA7Zs9-gL1QD5B0-fIbw3dsrzg7Rk_LgE_PE5xMXMRLGrIveVvOKTTJr52-PXflNdfBX93nx9sgivHeic9DWZ7S78_1m4tSG8M1SKSmSUoTl81SNiFRcXT8vnySbstl0mG-syiTNFTYSYHHxds-rGSw8dYZhaRjZON7k99uDWr3zrCcZVWzmyLP-v4582wBrR1D9xciqnFgxjVaY-JjlqzlOFgdOXyJTPuPKzAs1cgNTg_MtSGnOB1BNK58Bjwc-beizu_ft6uhwjX7JULZz15CTq2SkG_RMR37gDOwPSCKYtz8FeHnT4s1j8_ODwODig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
🇮🇷
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس پیشنهادی‌سه‌ساله به‌این صورت که فصل اول 55 میلیاردتومان،فصل دوم 90 میلیارد تومان و فصل سوم 130 میلیارد تومان به محمد قربانی داده که مورد موافقت این‌بازیکن قرار گرفته. قربانی روی گرفتن رضایت‌نامه‌اش‌از الوحده تا روز…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27736" target="_blank">📅 22:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27735">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcb2c4a260.mp4?token=cIgAtWQh3_rUz4D17fB4EK0BCUonQvimgelPNx1I4SE57ratVUYNCKNUXOcxO5iaVNtNtQIl9eKiq2oO5dgOFDLj3AYlN7HrovhRduyhIgX4v_M3k0ZeU1jrE0wTyKGc9H5bWw8s_lhsYBnNfvCpS-a1wu6HrH5DodFZqPCHlGbdbj5Zu5xNm54bBLYlSRZ3isi3dEqXObMQOo7W6HIXqS3SloicH5NXplLiQcRO0S6vdyulof-JJPCV-Uk38sQbea5rpYs-uY8FxoC8civy3l12WuMWVfaAnvNS-gfWweE5BkwIEeH1VHhfMtlWbgOrngPABa7IPrNc4A7BgmaOzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcb2c4a260.mp4?token=cIgAtWQh3_rUz4D17fB4EK0BCUonQvimgelPNx1I4SE57ratVUYNCKNUXOcxO5iaVNtNtQIl9eKiq2oO5dgOFDLj3AYlN7HrovhRduyhIgX4v_M3k0ZeU1jrE0wTyKGc9H5bWw8s_lhsYBnNfvCpS-a1wu6HrH5DodFZqPCHlGbdbj5Zu5xNm54bBLYlSRZ3isi3dEqXObMQOo7W6HIXqS3SloicH5NXplLiQcRO0S6vdyulof-JJPCV-Uk38sQbea5rpYs-uY8FxoC8civy3l12WuMWVfaAnvNS-gfWweE5BkwIEeH1VHhfMtlWbgOrngPABa7IPrNc4A7BgmaOzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ ترکیب سپاهان برای دیدار امشب با چادرملو؛ ساعت 20:00 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27735" target="_blank">📅 22:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27734">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-usX5anndCcTf-m5mcCuaGIoDfWrD6XiP2RaVufV1SXwn9op-injDkC3flTAu76ftcxu7h1OV_UCIAt9Rgxy7Fep0cK7F9ehPKQpS8k-K4lSkERrtmuw3vsciLDLUj01TV7D0dri3ZsmNd0oer96X-hbUryIxCPn1wwMb_x4NWDoHD0DRvVI6x4oIlV9WGWBoGe3TR1Zir9HFXrMmvNksuPAzUBM9Qy5BHdpyO-0c_aIDEfj64EhC0oLHRnK2T-tKZCPV8UXLvAj-MlHd5-_eR3nqxP0EywHcFjDK7DoYVNSQNyCbqUURX0A2div0q9dCAxPjnPNSLMdvByiTDhsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چیرو ایموبیله مهاجم سابق ایتالیایی‌ها و باشگاه بشیکتاش که‌تابستون‌سال‌گذشته قبل از جنگ دوازده روزه چند تا از ایجنت‌ های مطرح فوتبال ایران تلاش کردند او رو به لیگ برتر بیارند در سن 37 سالگی از دنیای فوتبال و مستطیل سبز خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27734" target="_blank">📅 21:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27733">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9ewBlkAGQGdXhJavFK-tThNTGx081jj_1EolGgQPjauHhw4JzEG7ny7ydzzXBBRBqqlOtYVcv0YSSKDUWfyDhlKkBM9ZKEYTag4t0huUAl0i1_O6BSWDlW7pxIf0xss9BM-1b3pTaNZRSv_2YTEvGBVLYs0SLrfU0VW8nYG7S-5wd4w9OSHFPsQ4Zd-RS5gmJ7yFsOsWoKKWCijpXr6M8ndf2yysPjwONp14DI0nyyW4MGPK9j4eVeLx-jPx5ARG19qZtSCy8nJlEf8hirrAvJtLkgRmBKXjW0VcXPfs0Q3PH5hNv7sB6hedMSgW9Lb5cT6nuDxwgQrvXHdoeue_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
طبق شنیده‌های رسانه پرشیانا؛ سید مهدی رحمتی سرمربی گل گهر سیرجان موافقت خود را با فروش امیر جعفری مدافع چپ 24 ساله این باشگاه به‌پرسپولیس اعلام‌کرده‌است. رحمتی در این پست قنبری شاگرد سابق خود در خیبر رو میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27733" target="_blank">📅 21:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27732">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDhEr_47bFregnQiNqwjjQ2RaxWU5qyg1J6KQwmAiwf722xKVRUF2LdL83BSfqNoTg8DU_vsEDvjLck2siaVnXqKHKs37mJnVJSdVwOrnHhNIzuTYsCS4XgkXRIb8RP4ZU2HeSx48M_XPn-onyA89fiP89GIv37dbjYYg8kHy1ZB_4xzEa4q8GvHt927mrOapiOcfryZQb8DgRn6mY-5seGhZiv2rDT4bw4i4dEwNlBdPMznkZ-Na8tFjYgxC-xgKBkS9laOyr2xURxtwI5rLU5UxjJNBKbSeTbZSisvhl-OKeW8nVuGasQOPjsL1q8rgoPeo4jAqVJWBJZmnICDVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌برتر؛ استارت آبی‌ها در فصل جدید با برد قاطع مقابل مسی‌ها با دبل سعید سحرخیزان؛ فرعباسی با کلین شیت فصل جدید رو شروع کرد.
🔵
استقلال
4️⃣
-
0️⃣
مس شهر بابک
🟠
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27732" target="_blank">📅 21:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27731">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rs2khp6gGp5QmqDbABQ7Fc_DlhpMBIXs9wwgQDHttQLeURFlA0ZlA9BS5cA3W1EMzu12eo67b-suDkiM7MvIi6optLde4eEQeMrHiV_7OBjoqOUqFFUwIzWLPLuf0tBbIPLqrdz4ixeGAAWIY3CJZCtEoWO78ezJRyKLJd2AIt8LhGeMNvrQ_QkvC30if2OP-AytXzpkeh7R4J7S4z75g9Hb0Y7ePVysy2XjPvhgybWkJSlA5DoI89BSfc7SEx2uIi0kr6eizVBlAdKM1awlt4BohnWGQ4DPwLRQMtjHRn-xG-uGtMbkcuk4ahVR88V2hrOAlRr-niGgvwHCEROQvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دبل‌مهاجم آماده آبی‌ها؛ گل دوم استقلال به مس شهر بابک باز هم توسط سعید سحر خیزان دقیقه 56
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27731" target="_blank">📅 21:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27730">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d884286cc.mp4?token=iTTOZqogKQkIYsAV7D9cIkkDXG0JBEPDYD03kodhn5ucr9BEyXNBmzkw9arnZuJZ9s5n8u20SAielC2HkZpovSvQc3X0dELtdQGnGylqUgJ4DwDSOP_pLKByyShUA62yt2PXVud_3hpWDuWMPdQ1-d8lqi1pKFnRmzpa_7tIGylF4nHvtUzcn41bN5YqVBp44hg26w9-fQBduPs6-KFFLUkpsgeOQ3IjS6Q_XwUBTpwEsm3CMQ-_zyQUS08DHPa7IlTHSQcudLFbgiPg6dWqf2zLtKv_B8TaOFE7hlMmH4dvYCwWxOx24qMqwhvaiP-TZzBITP6k4kvPvEJqmAFfSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d884286cc.mp4?token=iTTOZqogKQkIYsAV7D9cIkkDXG0JBEPDYD03kodhn5ucr9BEyXNBmzkw9arnZuJZ9s5n8u20SAielC2HkZpovSvQc3X0dELtdQGnGylqUgJ4DwDSOP_pLKByyShUA62yt2PXVud_3hpWDuWMPdQ1-d8lqi1pKFnRmzpa_7tIGylF4nHvtUzcn41bN5YqVBp44hg26w9-fQBduPs6-KFFLUkpsgeOQ3IjS6Q_XwUBTpwEsm3CMQ-_zyQUS08DHPa7IlTHSQcudLFbgiPg6dWqf2zLtKv_B8TaOFE7hlMmH4dvYCwWxOx24qMqwhvaiP-TZzBITP6k4kvPvEJqmAFfSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
تازه‌واردهاگلباران‌شدند؛ گل سوم استقلال به مس شهربابک توسط محمدحسین اسلامی دقیقه 88
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27730" target="_blank">📅 21:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27729">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3f9408f8.mp4?token=B9gVy9CfCX67RW6ixOpS5wbbDkbr6ZbPFH8w2mGL8JGRmUNNlCDD2bE04JE7hGH0GByK_57L4vwqeTojR9JCsSIu8zrWtPNYNo75vJA1P3xTR7Vs4D4HKf_WCj1Blt3MClGGZtlKBVIGCG5r4DxVLyn06rJDv2TP76MBq7K8wqmxi-1peYJyrTT8eGhYn0UWxT85NutK6LWnOgxsnk7B1I0i88TPNHIV5zqNuMuwk3fxu6IsovWtM1UpqPvU03koT21p6R7AhuobSSFlhVDYWsbsupFdOQmdLH_Y5we207j-NbW4fICVWyrhA9aqfwTQcGnzNTskO6mWCbyq-nL8fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3f9408f8.mp4?token=B9gVy9CfCX67RW6ixOpS5wbbDkbr6ZbPFH8w2mGL8JGRmUNNlCDD2bE04JE7hGH0GByK_57L4vwqeTojR9JCsSIu8zrWtPNYNo75vJA1P3xTR7Vs4D4HKf_WCj1Blt3MClGGZtlKBVIGCG5r4DxVLyn06rJDv2TP76MBq7K8wqmxi-1peYJyrTT8eGhYn0UWxT85NutK6LWnOgxsnk7B1I0i88TPNHIV5zqNuMuwk3fxu6IsovWtM1UpqPvU03koT21p6R7AhuobSSFlhVDYWsbsupFdOQmdLH_Y5we207j-NbW4fICVWyrhA9aqfwTQcGnzNTskO6mWCbyq-nL8fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
دبل‌مهاجم آماده آبی‌ها؛ گل دوم استقلال به مس شهر بابک باز هم توسط سعید سحر خیزان دقیقه 56
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27729" target="_blank">📅 21:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27728">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a75e1bc211.mp4?token=RkxtptfYdYU0YVCjNmy2H6SvZc6AyBYMMBmET4eoWN37fZ6IrYhGKHnQ-FYpFN_yJiJmjCZpzY9p4CKqqCL1kGtsohAI1xcmUi0xP6wXGGzq2ltF1MeWfmnon6xIKRSskwV6LWKSI9yHAdbhCjHBFvwszGYR-riNWzPoJytbRcps8Hcjf25Jdeh3neKLgsg4d1-X81tahJzJVgN6U6sZ9pi5oiN7etM9kUF4GZ-BG9b7i6bdsxykDHWsED-q1c9sKoZMoetpxecu-anX2X6JgQjkeU2cYrvPV8rHPLaKbgQr4ZDjO3_M0lldanvSWPFwtXNBn-99kY5nfKhdyPS14w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a75e1bc211.mp4?token=RkxtptfYdYU0YVCjNmy2H6SvZc6AyBYMMBmET4eoWN37fZ6IrYhGKHnQ-FYpFN_yJiJmjCZpzY9p4CKqqCL1kGtsohAI1xcmUi0xP6wXGGzq2ltF1MeWfmnon6xIKRSskwV6LWKSI9yHAdbhCjHBFvwszGYR-riNWzPoJytbRcps8Hcjf25Jdeh3neKLgsg4d1-X81tahJzJVgN6U6sZ9pi5oiN7etM9kUF4GZ-BG9b7i6bdsxykDHWsED-q1c9sKoZMoetpxecu-anX2X6JgQjkeU2cYrvPV8rHPLaKbgQr4ZDjO3_M0lldanvSWPFwtXNBn-99kY5nfKhdyPS14w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
رونمایی رسمی باشگاه پرسپولیس از کیت جدید سرخپوشان برای فصل جدید رقابت‌های لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27728" target="_blank">📅 20:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27727">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a0da2836.mp4?token=HVDGPJ9xFeTYz4EYN6Snj8AA2QLhdDh1wWful3ytZeRsUKWQ1Lo3RryYLMtxRdu7YuomkQg0FTDJR7_AgwsIcCp8G6_5GX2DHZ5YP7pxJKYmWZKsEMqSE33CFcPucfj5NVslAqIftEBjMbFOhGtRiF4m5Xv8cRvdSm3niCiK2IuFEa5O5wnTi9UwNJdkY271-2HwIslyW2qxDtZXW2KmzdJ0heTjyahYew-bGo99kfKWllz_bEADL30hFwyygku7ZoFdyuNt1LphHyuB5Zm4o69EI6ZFuCpjRHpTgJpc4CdlOa1EB8STtdRPgts1MAo0uCbesNoXtImpI9fts2wGFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a0da2836.mp4?token=HVDGPJ9xFeTYz4EYN6Snj8AA2QLhdDh1wWful3ytZeRsUKWQ1Lo3RryYLMtxRdu7YuomkQg0FTDJR7_AgwsIcCp8G6_5GX2DHZ5YP7pxJKYmWZKsEMqSE33CFcPucfj5NVslAqIftEBjMbFOhGtRiF4m5Xv8cRvdSm3niCiK2IuFEa5O5wnTi9UwNJdkY271-2HwIslyW2qxDtZXW2KmzdJ0heTjyahYew-bGo99kfKWllz_bEADL30hFwyygku7ZoFdyuNt1LphHyuB5Zm4o69EI6ZFuCpjRHpTgJpc4CdlOa1EB8STtdRPgts1MAo0uCbesNoXtImpI9fts2wGFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گل‌اول‌استقلال به مس‌شهربابک توسط سعید سحر خیزان در دقیقه 45 روی سوتی گلر مسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27727" target="_blank">📅 20:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27726">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWpLb5DNLoncxxuJcCLh8u0YBzO081O7-R7y1gHPoYk-870JBc4WMFJMKC8Nuun0lu72zmnlK4l2JjXPk_5m9zVvdZFtFPgVgcWRl7Tfx_Vcc7voM1BW2n8QmzJ3n8ObO-jJ65hktYXILT3iROOcA70giwQaOxiigLcKAEs5Aw2T6I2AtHSRIGf_DlCA9bYoqRQoOcsGjNUmYPNL6QWtRJOA5m_7dNslrzZ_dhGL2bg8vn1QeJOQ5AzTebk0DyK01qVy2bhQLLPgmVwul8oH85MEvm5ABSCi9K7w1koYtxXr5VTLZ1Y8naQMgAAQdO-bkHzX-4iMfwQb3AzP5rff4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27726" target="_blank">📅 20:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27725">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e32a2d766b.mp4?token=JuA7SlVw2utYFtb4vow0TL9NyQH1GnhPcUEvNHsXkat4ueuFyk8xYfgVtUO59wusGwshz8fPq4kF3hnTbMgoqtodx4A7nR72zkU16mFB1y9HcrsjbltRdikK2j7NshPAVf1ARu9X0WFtHKZHQ0lOPVOWryY1U4fVEjReM1A5ILTCEqrkhY-HW0D9i0RBiYqmgZKZ_OI5fgC94pSftUkb7hSTNbn5hgS7P_dY7zoHmpIW_4H8Wh2OiLCd1_a0xJ9laH4cYbQ9zowYwX0EhCw9b-DC0S2IOH_7zGL33dzN5nnlL416bJaMm4rtgVNKLhrqSb3NWyGYLvfu5mMfRLb0Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e32a2d766b.mp4?token=JuA7SlVw2utYFtb4vow0TL9NyQH1GnhPcUEvNHsXkat4ueuFyk8xYfgVtUO59wusGwshz8fPq4kF3hnTbMgoqtodx4A7nR72zkU16mFB1y9HcrsjbltRdikK2j7NshPAVf1ARu9X0WFtHKZHQ0lOPVOWryY1U4fVEjReM1A5ILTCEqrkhY-HW0D9i0RBiYqmgZKZ_OI5fgC94pSftUkb7hSTNbn5hgS7P_dY7zoHmpIW_4H8Wh2OiLCd1_a0xJ9laH4cYbQ9zowYwX0EhCw9b-DC0S2IOH_7zGL33dzN5nnlL416bJaMm4rtgVNKLhrqSb3NWyGYLvfu5mMfRLb0Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گل‌اول‌استقلال به مس‌شهربابک توسط سعید سحر خیزان در دقیقه 45 روی سوتی گلر مسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27725" target="_blank">📅 20:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27724">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32b2ae1951.mp4?token=IgiULwX2jlZYIIEAwyQkOr3zGrYssQZ4H0r_0DtZMeiBnrWi8pSIAeIK5b4Q2aHtKGNh9wpnzEaJ-qhN7SUiBrdGeQLOCOa5V5YdiwhwKFyMz-8N2y6hp1JtpPz-lw5CFlK0U86hSqA8ea-L0juxl9nDJtoSfz6AJQOIe-l-X3TnTWyRVRGjs5Oal64D6-gpYx_MLAnyXMQeYwJVcQiYOGnw3qDZcgpthBkOyZG7L5NmyERMH93l4My2W2KnDXpqLCNu05M1hpBnLvRjKVVz1uqviT0XJIGafnMvTdT-T30g364As8Kw9dtcKQa9IEDjc8UgItrFs3hcnBjIuxS-oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32b2ae1951.mp4?token=IgiULwX2jlZYIIEAwyQkOr3zGrYssQZ4H0r_0DtZMeiBnrWi8pSIAeIK5b4Q2aHtKGNh9wpnzEaJ-qhN7SUiBrdGeQLOCOa5V5YdiwhwKFyMz-8N2y6hp1JtpPz-lw5CFlK0U86hSqA8ea-L0juxl9nDJtoSfz6AJQOIe-l-X3TnTWyRVRGjs5Oal64D6-gpYx_MLAnyXMQeYwJVcQiYOGnw3qDZcgpthBkOyZG7L5NmyERMH93l4My2W2KnDXpqLCNu05M1hpBnLvRjKVVz1uqviT0XJIGafnMvTdT-T30g364As8Kw9dtcKQa9IEDjc8UgItrFs3hcnBjIuxS-oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شماتیک ترکیب استقلال برای دیدار امشب مقابل مس شهر بانک در هفته اول رقابت‌های لیگ برتر.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27724" target="_blank">📅 20:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27723">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEE-qxsOgKWOcJzfxYNoXbaTGTwMYwlXvBcnWKBXOAMlM4NegN9rTGrFthoLEPOE3qkNqcy2WTjxChCvnGo48h0x2BiPhYddpHdYE9O633cvHUdqWmcnTp6Z5SYzuGQqjROOwQoo5FP0ib34-s-Lh85eCbYrXXmt73Fp7--EuDYKFyPx-rsFcpBtj0v3XNG_3-9mcthPMdD1MLEBI6Bsmz4CmXmBeZHrxepvQfQxfq2nGpiHjVjxBwzPdRzIusuinFFtSvqhowlTa9XyfG-Z3Wnm-QiCcwKhk6yWJtFhFKM3dhWhDs5z79VzTnI2I_-d4rvP6qlWhK8qmAieqRopUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دبل‌ستاره‌بلندقامت‌پرشورها؛گل دوم تراکتور به پیکان توسط شهریار مغانلو در دقیقه 45+1
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27723" target="_blank">📅 20:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27722">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TupqVRfSCGQ_ecvtE31yyPS1qxu1bR_x3JWkFEhqHwjXFuItjer4CkrY_IBNvfXFqVki-3bLdp9Xg3qmIdBSHwOljh_HWzTbdJPD-8iASX8Ck8lZoL5PCP5JfMb9nlQXTiEy_QS9Yb0gHDy7OsZlDG8mxqLvNkv3wlusl9FZduXMpuaS67d-UZW0tkCvdETn7xJah4u9iuhncMjtwvm7_moqHPDuWeELpt4mGoOh3axZ_0n09LK4FGWMHq5iCbKd7l4ySzRBASL4B--oOe8kJhfHuTjkZcKGNN9Z6Ra_45PRq2sp2E7id4d9oyUX46ANzFu-Vg5cuavRs58X__w66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ علاوه بر جذب دانیال ایری و جذب احتمالی محمد قربانی؛ باشگاه پرسپولیس یک بازیکن دیگر نیز جذب خواهد کرد و پرونده نقل و انتقالات تابستانی سرخ‌ها در این فصل بسته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27722" target="_blank">📅 19:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27721">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8QoJaeP0qO8oe52OlP59D91nUwPpPpA555bWeKzEGiAXV1gDfjp5-7UglMpsTE2lJTV3Em35CWVqhkv-sRszA57cMrEjxWKxHUPrpZRLfNw_8yF--4BrZbZfn_oZeD5DZhux8SlTtkX64sK0_ETdMRojV10TUOVN6HdDsyKnp8qqJqV7VvT4UrJYpy1XEKl6M9IKYOvz5jf5_rGqtaz4Tzq_v4QQxaKEkul51TBgPEfEYlRpaflcqDRVKbOEXXKh8tozGViKhsk9arvnO-lnTCOMJJKtAscLU25njfGxQJ4QzE1mhn5S3jZ9J9J3gNJCIkV5swb0A4TJQkPuBoboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
همسر رضا جعفری مهاجم جدید سپاهان که آماده دیدار امشب طلایی پوشان مقابل چادرملو هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/27721" target="_blank">📅 19:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27720">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIYQX-KgAO2QNKHn1zKJ2-Z8uYpNcdDn3KGWXTNuh8l6UAHokTTQLz-UQxkrtO6eUexJcrXYRy7ItC9VoyuHDcIWhd5NPZCaVcO0iE9ghmlgCDViHNpbvw_UYzquZcXqKG1iJruqyzy388EdAGnk-e1LiMhcxR94mTPQnHZKGE6aD7L5pQhFQPHIROgK-mpQmMSvx2KLy4RTUcLaVF0vFh6DMcDjJykbpbmsvy-BPnMYWJSf2BSN5Az-_PVO6jOhiaEO_6GsrMQIfg8--br27o_Tc-FrgOkRj3awnhmmsVQOR7wXFAtEmz591EXYDjKCS53s5WnFngtC-f-if_fuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو قبل‌ازامضای عقدنامه؛ با جورجینا تفاهم‌نامه‌ای را امضا و حد مالکیت همسرش را مشخص کرد که چه چیزهایی به او تعلق میگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27720" target="_blank">📅 19:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27717">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osQPpvrGDY0pSuRECRqlQJSqWsyw9KLMBRN9OEIYd2UALzdbVUeC5OKl0_8I62gPJ3PQwl4SAjEs-rBHX_83eeLFyrPT1yQP2Ro7gyYv44NBNnFW3nyg9qMpMdfMsrc8bbPzZxWEbVCyZdCxtBQLMRDthMSAHO1-uQ8fhCtHopo2Qtvd5VOtjuJl23Qgj9sIniwp1-YD8A7QYjSEfo0Zth05r6YwuYzbLSsKACb1tpInbKX7E72_hLU-BgUG1_Gsh1MdbMozkr3tDyNidn60Z8QiCLDQDkdA3eaDz7r5-uZhEEl1YZwqdpfKramUWvGHw17oLGu1totWu0s5HgzaDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو بمناسبت ازدواج رسمی‌اش با جورجینا یک قصر در عربستان به ارزش 22 میلیون یورو ناقابل به او هدیه داد و به نام خانومش زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/27717" target="_blank">📅 19:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27716">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/342fbf13e8.mp4?token=aqkmvJaCdBp4SkS5e_ic1Sa-ly8_YrcWg7tP93vtxseUhSOibPeeRr5ljiU1toN8w5bLSRsm62SPZhex8Un9eC7WrmIBKlxXg4ZVVxadAcff6w_TOh6tqCW_agd7Kf0119rKmviaToxG_rgeGZz9bFnZUJDdUBqtFgV0HNfdnGcCwIqC6V7CyRr3he5y1AF17S45KUDOuV2MFeV7n7Sb6hkusBGPKjYfIhmk6S9kSWqSjGN34tOqfYWATLBRqR1HRJ1VX7pXjnd9vbDPaBwKjNogaZAUdvX8eHoDbUMj7XGoZKKHzD-NeOZ2iKRSTr_fJTfLo652Qs0-0ks4kno0KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/342fbf13e8.mp4?token=aqkmvJaCdBp4SkS5e_ic1Sa-ly8_YrcWg7tP93vtxseUhSOibPeeRr5ljiU1toN8w5bLSRsm62SPZhex8Un9eC7WrmIBKlxXg4ZVVxadAcff6w_TOh6tqCW_agd7Kf0119rKmviaToxG_rgeGZz9bFnZUJDdUBqtFgV0HNfdnGcCwIqC6V7CyRr3he5y1AF17S45KUDOuV2MFeV7n7Sb6hkusBGPKjYfIhmk6S9kSWqSjGN34tOqfYWATLBRqR1HRJ1VX7pXjnd9vbDPaBwKjNogaZAUdvX8eHoDbUMj7XGoZKKHzD-NeOZ2iKRSTr_fJTfLo652Qs0-0ks4kno0KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شهریار نیومده‌گلزنی کرد؛ گل اول تراکتور به پیکان روی چرخش دیدنی شهریار مغانلو در دقیقه 36
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27716" target="_blank">📅 19:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27715">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c3a29973.mp4?token=f9sSgWyu-ls_5TQ7Jl3ZHOvSdwZq1xBKA_3qEnAUQTddIdd-QD5eOFOrRumEVWm7wgnHB7ahb3l08wEND5GUi9q0wazZ9WiqWnchZAr2e7tc7wN7OThAB4J_XvhAhm-0oBYproGDWRAd677J5mIjfrj12f9VYEgJkq7JA8fYItGkmDBzXXAORsXtj9BreGrNHhzgvU3JhocRCYAI0gE3k_-mkLiiOrd3LBJFu3UiXrSLGzl84s0dQP_V74St_OBhK9V3LmyeM5is1JqiBDmfeAYF3UxvkLVujuxxWMOFZZRA3VJKnkUCXxiMdpS5mOQBw5852ljTagtbfRqjfTyVyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c3a29973.mp4?token=f9sSgWyu-ls_5TQ7Jl3ZHOvSdwZq1xBKA_3qEnAUQTddIdd-QD5eOFOrRumEVWm7wgnHB7ahb3l08wEND5GUi9q0wazZ9WiqWnchZAr2e7tc7wN7OThAB4J_XvhAhm-0oBYproGDWRAd677J5mIjfrj12f9VYEgJkq7JA8fYItGkmDBzXXAORsXtj9BreGrNHhzgvU3JhocRCYAI0gE3k_-mkLiiOrd3LBJFu3UiXrSLGzl84s0dQP_V74St_OBhK9V3LmyeM5is1JqiBDmfeAYF3UxvkLVujuxxWMOFZZRA3VJKnkUCXxiMdpS5mOQBw5852ljTagtbfRqjfTyVyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ ترکیب تراکتور برای دیدار امروز مقابل پیکان؛ ساعت 18:00 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27715" target="_blank">📅 18:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27714">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILRZ32amTt_rPPrXspH8Sv6RQub176K-tdCHq-z7Z2wpmJgfwxUam-yf5p-A8Z8-fLggh80s1dB9T9WJwDrO6r7xBJkevWAjwC8F1H7qR6HXzUtkn-wxX2lla34dM_q5ejRzzMmsBOn0IQcdso-6ahWcb8pDMvIqBAfqxfHn8fn724or0OVgtnQsXK3W7mC85Fz9uyXfUk5L973DMsLWKmpz5ygL7Spd2b3z2Y0GOzw0tQO0ycYDvkRA1_h3ra7H4ufjUIlim2SnRy73RIeYU6orYXY-SlrgIa81bkhVXqLt_BYkYZJ2952-xsQ49S6v9793o_msMTfC-7DcGVS_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ ترکیب دو تیم استقلال
🆚
مس شهر بابک؛ ساعت 19:30 از شبکه سه سیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27714" target="_blank">📅 18:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27713">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWk9OEjjpbvieowWLwXezTpgzMZEqTpChYABHkIqEwzJwuNBpfsrnlsRNEM-wXoRVxBhftaXkuwnp_SSHZx17BRhRQcUc02ely9-DAEUpz-W-1aFkKZPW--hAu_96A2YY8I_B-PV3GNoOedevy_uBjC7ACOiRUv4Vt602ejx0I3g431pILZXRjNh-7_1WK3b6wvxwMoTLY_J3pRypRfseOgYloQA7EQLPNbERstU5JBQ1_thzWqVzF6k8_tDdm_a3dgLcN-w_QiJRBmLye_4MNGpQRtoQQtxZJNjTyRqcR20Mnt3XMJv_ot3-l2b2wBzm1CsAD7WT6UBryawUOcbTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
شماتیک ترکیب احتمالی استقلال برای دیدار امروز مقابل تیم تازه لیگ برتری شده مس شهر بابک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/27713" target="_blank">📅 18:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27712">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3436fa84.mp4?token=Ogf_DKdivomqC8hwCq6R-w8dg8H5B98_CqJxrLzADcsoK0d7lhcLa6HNILOv7VvYokc22Jj9FLKlLDXQKLJcVQGAznDtY6HjCAW3AYAKShseoNFHVS-XJvxgRgR4Cwlu3zNpDN0EAsGaR_NnDYd7Q2LdtOkZHrry7QZXDWNFM3kx4dc-cXPNHjGmwMN2tXx66gOJErLozmY-YHz39XvBadzM6tCgHh8I2MGNP7Igz7pN3wfZ62sT-sVSzi3vORUOI3wr5OLs7_Ru3RK524QLMDuk1iOHChW9z9JIb2g7gGVWMJ-ILhdDnbZM5i6NPRcz_ie7HT8bKH5dzpF8B9NP3LYWpAnX13JPeZlrZep26nSwMBnwbsv0-xY-c9wqEdQfkCo67wycqXsaSbH8yKNelQWCNTjBLxSE5ddEd7nL1lOivV5N2ocEeTR_2NfHAMyms6hrFNi_yBoWinFgTFckrQjZZ4eEzJHJ-yyGzZfFwkwmmGjpa_BbkAKTbUAcDyZGGqHOM24HM_fz-3AyqTuUxXHnJOZ5RVdkRlB4ZLLzZa90f7K9vMIsiqogv4vWFzFOueKuL2USn20goCrPK4SkvH9oUvOcDvf7ZZ6fm3n1_rHPlbDmXjLoYDvvDVdESc1qOv7JlOIrBFkqSUTMNeLckDamwTjm1qobFF7bMhGZhk8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3436fa84.mp4?token=Ogf_DKdivomqC8hwCq6R-w8dg8H5B98_CqJxrLzADcsoK0d7lhcLa6HNILOv7VvYokc22Jj9FLKlLDXQKLJcVQGAznDtY6HjCAW3AYAKShseoNFHVS-XJvxgRgR4Cwlu3zNpDN0EAsGaR_NnDYd7Q2LdtOkZHrry7QZXDWNFM3kx4dc-cXPNHjGmwMN2tXx66gOJErLozmY-YHz39XvBadzM6tCgHh8I2MGNP7Igz7pN3wfZ62sT-sVSzi3vORUOI3wr5OLs7_Ru3RK524QLMDuk1iOHChW9z9JIb2g7gGVWMJ-ILhdDnbZM5i6NPRcz_ie7HT8bKH5dzpF8B9NP3LYWpAnX13JPeZlrZep26nSwMBnwbsv0-xY-c9wqEdQfkCo67wycqXsaSbH8yKNelQWCNTjBLxSE5ddEd7nL1lOivV5N2ocEeTR_2NfHAMyms6hrFNi_yBoWinFgTFckrQjZZ4eEzJHJ-yyGzZfFwkwmmGjpa_BbkAKTbUAcDyZGGqHOM24HM_fz-3AyqTuUxXHnJOZ5RVdkRlB4ZLLzZa90f7K9vMIsiqogv4vWFzFOueKuL2USn20goCrPK4SkvH9oUvOcDvf7ZZ6fm3n1_rHPlbDmXjLoYDvvDVdESc1qOv7JlOIrBFkqSUTMNeLckDamwTjm1qobFF7bMhGZhk8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ درشرایطی که ماده شش فیفا به برخی بازیکنان اجازه‌میدهد خارج‌از دوره نقل‌وانتقالات ثبت شوند بندچهارم ماده ۱۷ به صراحت می‌گوید باشگاهی که با محرومیت دو پنجره‌ای روبه‌ رو شده، نمی‌ تواند برای ثبت زودتربازیکنان‌از همین استثناها استفاده کند وبه همین دلیل‌باشگاه…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27712" target="_blank">📅 18:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27711">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cR0sje3m65gMjkS_GHSWGuLWhBxM-9gItSJFAPFSun1DKKT1ZuPkW0oNyztBgkSn52Qa7r1rkBKRwhcyPammqIpRjiXgZot4b301t_hH1YqTIEAs2A13-QsDKGIEQ7bsG9msvBBjQWavMMHnpO9U-H31ZRWoNG07OW3SVnsNeQShkOKfeHIaEOCLclL3Xnot0IOPX81_EbSgU4Gw02_LXhugI_-VJuQiPFOca8LFf67mbyIAMgeNxnfseBZZ7__O6pc2aov7q9TEmvkuaP6-YM3XRDIZdQKG2h8rIRqGinrwqyyo9J9hdc54WWZiFnrHSsUZ1YPJZtMlGKy_EBKnaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
مهدی ترابی ستاره‌تراکتور از ناحیه کشاله ران مصدوم شد و به‌احتمال‌فراوان همچون مهران احمدی یک ماه دور از میادین خواهد بود و دیدار هفته سوم باپرسپولیس در یادگار تبریز رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/27711" target="_blank">📅 18:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27710">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDGRwbLvii5RbhhN_f0SAp8hQs7IxSSf-0_s5_aobkM8FGPIikbCJ0_UV21ck0ILiyENxluzbsx4kveCG6XEDm4Qka4uGA01BlVFVMgN_0HloXjYJbp41goGE2xj6YUx3-N2A8YZpdE7sF_ddTGHosl1-ZyYWTqYCYCW1uVP99oJcgh6FyqkvBmZMHPmMoyJc8MiXpuc_iknqdSb1jBRXixVSJL1Rgj2lkj5Z4F5Kcndaij5IOTUKmWqneFvG5wDRngyOsz4mqJP2pSltE8rI2P0UAdP2BiohPdYUEJNIOOdNo546tCcCDmsiAaFgQ88DhGlgIACJH_zRD7FU00EsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
استقبال‌ویژه‌بازیکنان وکادرفنی‌تیم النصر از کریس رونالدو بعد از ازدواج رسمی‌اش با جورجینا؛ وایب صورت CR7 خیلی خوبه. حلقه دستش رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27710" target="_blank">📅 17:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27709">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcUHwFXHV9TpQP2pfdSXImlq5g3m4X6sbQJCmTKFnOF3OY9JCCCG_d3qILP0x0Fr_YU_OGsVRb55KiunxstpooBoDGIOaN6k5dGglvbOJEDosKM6c2n-vbqon13-arG01O-94mzlPWI1CxIvEsW6JnRuRH5QW2oc_nqI9QTzifSRigWnvdgVziPfPUPWvANhHmUisvwQ1DncGkx5KnEqx4BHjKfZJ5woYnH8TRN9RY0hDtMUb4Gx_D8__dxaphWWdcCn-RFm2iI_T5wRVC5K8i2g3bBkVkEVQPSOpwUPH6344dljJimbVtUGmmaSJSZNXueNpLptOj29FxZWh_52CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
الگو برداری باشگاه تراکتور از دو باشگاه بایرن مونیخ و منچسترسیتی در طراح کیت جدید این تیم برای فصل جدید لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/27709" target="_blank">📅 17:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27708">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6acf648940.mp4?token=HsCZf0uYQ6P2G0QbttTxXPcGRgChaGNYoBo12mPMO9lSQhmcbxwVEixQoaM5R5NrVVmtR8eoZRJq4Qa8L2IOxPAmeuSfL_ckkW-BHC_qCKJH2mKf4qhMlOODNXpLtlwXnh9st7S1jU5fU-8mD2t8u5xRVFYZHK8hyVQomanFz1sjK44KUnUDPm_5iHJQNXm45bcCf8tGAVLaGWLgiD9kYGQ3SWYWHn5a9Lf0JoccEQ4_u0efilLjh1jPmGW0TahEntjM77Uj8g2FWOx9W13y0pgrquMQ7eldJNjxu6zXd2FKGsNqlzCDM1FWpKtzAwRFDqri1mvaVKgob6JIk04hxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6acf648940.mp4?token=HsCZf0uYQ6P2G0QbttTxXPcGRgChaGNYoBo12mPMO9lSQhmcbxwVEixQoaM5R5NrVVmtR8eoZRJq4Qa8L2IOxPAmeuSfL_ckkW-BHC_qCKJH2mKf4qhMlOODNXpLtlwXnh9st7S1jU5fU-8mD2t8u5xRVFYZHK8hyVQomanFz1sjK44KUnUDPm_5iHJQNXm45bcCf8tGAVLaGWLgiD9kYGQ3SWYWHn5a9Lf0JoccEQ4_u0efilLjh1jPmGW0TahEntjM77Uj8g2FWOx9W13y0pgrquMQ7eldJNjxu6zXd2FKGsNqlzCDM1FWpKtzAwRFDqri1mvaVKgob6JIk04hxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛شروع لیگ بیست و ششم با مسابقات استقلال، تراکتور و سپاهان مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/27708" target="_blank">📅 17:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27706">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYJo6ZkLWCSIw_LPzTglezP0DLoAvKWowFIpEjGj8tRh_8N7HAoGPAuHkqOkw3vP-VpNtqzl8nyhZBl_5OA53fRujdrfxlDn5fDAxBvsF1c01i8lNu4fzPUXa5tCTAbYX_bz_hofyPpI5iNGk6l9PmYptN1OGStBikKcet06p0FDxUF7XwunrNtcXVYkb5ocJ2CyoeGnAP_4ygqpp9nSh_c7hxhuuEoipXKCTTFXptkLfNt_ES8M8P9bBv4lZcKug7FmClCqpN97pjfqyHlOykM5qlGpK7ljo95_9RM131y6nEjdsgkiv-YE4jKBGagp_J8tG1oerqAHl_23uAj3eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jgot6FwItVQmsBr3UmbCbNUJoT8GmvVtGEX9VNtjYodNdpc1qexADpv4Hu2Ne2TFlMtCbX_dVU_LkE2vrNOEHADVFQKRlZsM6JH0UcEi3wxC3GsznXIJYTNlfOvPKYDhvLDJkDj86NdSvhdIwIYQU8oGJlXQZapoypqR063QFRKhj3tRxdAsT_34McB_mXjqfghu0uM96D3IUaSrU4ysxpcDIfJgIDsvCFWruaGxroUxkGufmXUWnbxWDLyAA_VBXeTwuoWmWFq1itw4Mr9LU2HiIGrs4GGDnU9Jub60k4yXoDKtzNRBMVietDZdDarWlyKyl5INSh4z1BUce3Fnuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
الگو برداری باشگاه تراکتور از دو باشگاه بایرن مونیخ و منچسترسیتی در طراح کیت جدید این تیم برای فصل جدید لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/27706" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27705">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKPKBOpKS4F3DexDRoP0aprhnOkZN8DZXhZblz4IRpEAPB0mEl3AOAzIW-0pYwNgjvI-ktHHG0CaNz_ClWYkKDpLAXd76iUUpzLtvk6aiWLOtmZtA-y3W8IYqOqgafh6vm-UnAAjoqK6IE1t0Ogln5KMIKw0QYGP5OhKimUXAsT9MqHVVYjEG8EXnd3p_w6Fk4OJUD2ZI4O1WG4Ml86WJN7HPeTkuKGuXLEflbbqPKB-AnZlM18S3xA4pU1BJ-wQ4JnB1lpN6HYlodrQylzl7Uw2A1rZMGAVKCVvrIC3aXVP3toySpW9jjEh4MXOHXJ5qkHPNSshoaVvTEb6Eqgwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل کارتال ظرف یک سال اخیر با این دو ترکیب کارکرده. جنگ ۱۲ روزه واسه اسماعیل کارتال خیلی خوب شد. فرارکردپشت‌سرشم نگاه نکرد. الان هم به جای کار با علیپور داره با لوکاکو کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/27705" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27704">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwF7jsxkToMgi_gEJH3SMsAVOqmTgmAXL5SJWrg29ZhvILSrAYT8-8miICq_bb6Y29oJKaxXzyaCkx-DLOgym30x3M_1aApZ5w6RgQSL3vLQEBuhsfQuf5Ks1GbI1MiFXB84iiifvrdiQzLD52vysGlgCDEXDgt3ecEeu-nXmeFgAf6gGfIwzJqlbuphOSRPQehHpx4kdPRG4OZ_KJL9wXCChzSna1ZecxC9UVjhIdhq1KPxlW9V4NcljxchjDWgZH1YOmjzNgR8YUzHKhj0OqksjacbdgGj4MLZBdb4w8eXzzDuhkHVgg7ESXz9oslx2eYjoun1ttrWH_5_x7DALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
هفته اول لیگ برتر ایران
🇮🇷
چادرملو
🆚
سپاهان
🇮🇷
🗓
جمعه ساعت ۲۰:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/27704" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27702">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gpucZcq-FcMV7yGs9cP1EagXBw6Outx4_a-7MWCYFhq7fY8EuqxJRps9QpWXPAt-sADYZs3bDbQ4t3nVlfgOvXm89HtnfXTFpcy_bl_LaXYIrDNrQZlA5_zADvO22yPVK4ErA53YpDZ0mi-DTosRICuEJHmZh77VAph1w2_8rgE5ky4grEh7e4uRjcADh3TH9FiVeqKYeuflx7rF_cOMYTLDImbqj7UBxMgoFEUZDQxKNbcDT1cGQ9L27QVzUjpZQfafjZH_Oz7DEgnWYbiW3Fqh2iBrbpT2dAN7az9GXznUVAKWj2P1aVaGdqqsftnxV8Vnd69tAeq5Y7zTsgVVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfKwd-lY1jbNRjSEAeDF4ggC8dhT-AUChOvKXY2JSh_siiNLOWjfgf3OStDLy5YkO9scyx6qIHcfZu3HK7PQ_Rm1uLseveDzmFMc-YXT2U9ofH51qRagbomWQL6-mgr0UVrUCY7DAxfvJXs87Jui1XJ8rwYQ9QRJ_-_8u01gROnIcmbjvVyU2R_lEknDwCLO_YxoZifvh9etLLoJccCyM8EZPC6sddQcbF1ih4-LmhrTgkoQVKi2g7hwYq8sSaHSmFFefCRrXwvAZZQb2bRRaoPwnVLScyMlvXTSHC74YNPhGMPlppiW7Y3qFRfVJhH7cfGCA-4ZLVKmKdXgvroVMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📹
ویدیویی از مراسم ازدواج نادیا خمز دختر پاکو خمز؛ خودش‌خونسرده ولی پسره چه استرسی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/27702" target="_blank">📅 16:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27701">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQaa_151opE3ygmn_-JC6uevFGVcoKGM_i2HR4A5EwcwHSe7cwWJALu5r9i-x8xA8y7kZ6dsUvSAlcp-E0PY3IfclbvTplxWSHIZGzVJZ6zT1kJB9cTJ24GQjLeiG_psG0l1R_sgsLZp9RlBTmfwmMM_6WpSg2GMrvanzbkQJwERjKSX3YlLnSZTukZLgRw2_GEoWTDmG8w_iinJWJl3yb9Kcxe9Vwiq6lnFL4VsuQ8e66X5OcSF4dxzvo91-J9tCX6kjHPCFC9GMyovrDHT8xTDl1C7dO0hQMU4T-NCv_ECHRIq6qHgNCWNraBSASIoQO_vVBPx2maJzVw6R6p4Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام باشگاه پرسپولیس کوروش اژدها کش پدیده 19 ساله فصل گذشته آلومینیوم با عقد قراردادی پنج ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27701" target="_blank">📅 16:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27700">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‼️
🇪🇸
🇩🇪
#تقویم؛سال2020 درچنین شبی؛ این نتیجه رخ داد و بایرن مونیخِ هانسی فلیک بانتیجه هشت بر دو بارسلونا رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27700" target="_blank">📅 15:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27699">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRKbttdzUB-4M9JoKki_GJPwtsL4NIGt4og-8fDOPtszVADunofbGXHXM54GCNH4j7L2P_CAxFI4pB8juYjl7EOPfHslAQuVD1hLuPQcsWnVIWIwUuck1QNus0yhDZPSZjE116mB-iwxYJR6nBVTCR0IWahqLcIyPK6e8ezkUJbIBD537GK4Z2P6tJg6wXhG80wlqNkvfbMLbKU55v1JR2SQPgxixMMrDiJPjxTPZXCafWjNXINl3GEuPyRxB6qHctlPWPQmo_M_CnpwO-XaA4W7cXcuRLNhVeJNYNdB9UDhrpQzrCS_9oNyxuPFbezjZlytWGbCWi1TXuHtqPrB2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛شروع لیگ بیست و ششم با مسابقات استقلال، تراکتور و سپاهان مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27699" target="_blank">📅 15:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27696">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MU8FrHpmrAWJqhsXbAqVKhs1lp8JNo0oZx9H67fg5Y5nhFCGiGtBx6_dLbKg7TrwxqmtEd0ClK31m7TEWiRZSx61jOUcEwvktrgrJcB2m1yyqckFDmfhw5pZe0FBPz2FsK9T6gQzkr6gd4RIoIdE3zOifAFfT4_sHGNmJ-M1x59QM8tZ49xezbt3vo9HylX2q9T0QwlAg4sCUCTn2AcAmUOeis_wuiDcMcej5n8eCohApNcfo70vamDNQWXqNm6Xsb0RNVGvpWMg6NeBSx4NS7wckMWIyB7o9gfEOa7IeFEYhuu87KPF1X_S7UVObe9HKLUAvkl0HI3AKIGVpKnujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ به مناسبت شروع فصل جدید لیگ؛ تمامی قهرمانان رقابت‌های لیگ‌برتر از ابتدا تا کنون
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27696" target="_blank">📅 15:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27695">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDVe13AVAIXfrtkDiBuKv9xgJvWvYzL8aFqMyjXk6sbVM_WJTt3GBWVYVORPdDcLG3FT19RSOCIymPSFk6K34vKkgiYHQU_AauS3xM4Rw83y27K3yYhXo-OiTTx83PolKNOvVopus58q4ZHaJcXHFfow9NhFyJghSEx3RQQYFpgVzIkCXR24W9J-WIALzQ1GodyGgmRpp7R6txakxo7N3enbbf-2N0pkgcOJJXnDM4PaVhgVVK5NpDmajpBTdSEF5OY7AJE6YDRadwlneVcaYhSatx_nlO7Cscyr2SYbdPkah7gNTbxz1S_in9_iN1tb5ak-mMj7jESXpiCiGChJDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛ موندو گفته:
چیندو اوزور؛ بازیکن نیجریه‌ای که در بازی دوستانه از هوش رفت و پس از معاینه، پزشکان‌مرگ اون روتایید کردن و حتی باشگاه‌ بیانیه‌ای برای‌مرگش منتشر کرد، در سردخانه به‌هوش اومد و به بخش مراقبت‌های ویژه منتقل شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27695" target="_blank">📅 14:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27694">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VToOQO5vwM9zHprzg78Rc1SCcOsjhrevmDyX0RFA73I_J0loasr9o6699Evqn_ShP6GjIghbGNtZyDyBI_od6HahxqNJg0WQfRiu1vQhQsMYJoRdRYUsgv4AInEh-IcgbsW_osok9tptoHBHuPSBs_wNWRnvQdQKdg5TCt-lHewwCwBr-Slq60gByeY1OTEpXXMEcCojrnbY32002i3E-bAvT1Xj02C42ah2-ni4hLYAtWchALm-leGaKMT9XYmPp8fSg1waSOP5L1U9Dl6sk82TiNfMl4osfw7JsMz1xxWxaDbesHFDdXHpPSPKyDmqs4TZhmxPCYdJ72hpRKyD_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه‌پرسپولیس امروز ظهر به نماینده مهدی طارمی اعلام کرده درصورتیکه این بازیکن‌ تمایل به‌ حضور در لیگ برتر داشته باشد باشگاه پرسپولیس حاضر است بالا ترین رقم قرار داد رو به طارمی پیشنهاد بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27694" target="_blank">📅 13:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27693">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3094b93ff.mp4?token=CjwD3k2G0iroXcNw6B4Vb9YRrnoL4WlbJEblI3k5FbVklMieWiqAPfXZwcrVMJJqmMW7utJcOTnyMOFy0BzsTatZ4d-M-sIr9EjQhlz3Z2yU-cOAqg7USzy2AqI1qB8B6guIbDvEh8KigOajslOa3dG6NYmBFOFlFi_gIF36XLbrCuSHb_oYY0THdk1jd5P9nn2EUrBh3TP9O_BDqHjEDXwtFewCqYZYKxBNj-GUDeZvKl-_LGCn-z1CscY3DDPFb4-ZZ8tJolABBSnIx2CEOSFal1vhkbjhxp102D1m1wm3DjYZfeIoUzSv_xCl-Oa3pPKY6XXf6MC4hujgO9uT9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3094b93ff.mp4?token=CjwD3k2G0iroXcNw6B4Vb9YRrnoL4WlbJEblI3k5FbVklMieWiqAPfXZwcrVMJJqmMW7utJcOTnyMOFy0BzsTatZ4d-M-sIr9EjQhlz3Z2yU-cOAqg7USzy2AqI1qB8B6guIbDvEh8KigOajslOa3dG6NYmBFOFlFi_gIF36XLbrCuSHb_oYY0THdk1jd5P9nn2EUrBh3TP9O_BDqHjEDXwtFewCqYZYKxBNj-GUDeZvKl-_LGCn-z1CscY3DDPFb4-ZZ8tJolABBSnIx2CEOSFal1vhkbjhxp102D1m1wm3DjYZfeIoUzSv_xCl-Oa3pPKY6XXf6MC4hujgO9uT9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌سائوپائولو داشته‌ازکشور واسه‌بازی دوستانه خارج میشده که تو اتوبوس تیم 86 کیلو ماری‌جوانا پیدا میکنن؛ حالا سه نفر از اعضای تیم و چندین نفر از کارمندای باشگاه مظنون شدن و در حال بررسین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27693" target="_blank">📅 13:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27692">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: هانسی‌فلیک‌به‌سران‌بارسا گفته اگه شرایط جذب خوالیان آلوارز فراهم نشد با لوئیز سوارز مهاجم 28 ساله اسپورتینگ قرارداد ببندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27692" target="_blank">📅 12:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27691">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fb5D7P2oOjS9FAM0BZLvTiNFNGufpKeW5zQdxwi6_cZt80XJzBc1vX497vzN_t7p7efCeHFcjAxsyHCAecGYD0jZhmpjaZVhZPsJAKxbgUaTFCSvSBB4JXsFEfMqyqrszkvPMEsSIiwl5-MqeYmKESkyGgJ0Ub4s4wSLYaMG2ikWHKyMfzrwlyx1JJIC-LtDnhBropaLGTp44XSb7jU-mTkM5w7QYzXdiIdqF9SI0YkgqSaC_J1e5JqHL4b1lhwsugQ7-TbfmyEZQXyhlv18tj4w2nI1Jpunj1GRzx-5UcCZgde5Gr3aWBtNqtDO7rjB1cDQoCS4EEA0wGSDkRrCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
🤩
#تکمیلی؛ خولیان آلوارز امروز بار دیگر به مدیریت اتلتیکو گفته هییچ علاقه ای به ماندن در این تیم نداره و از آن‌هاخواهش‌کرده تا با انتقالش به بارسلونا موافقت‌کنند‌. سران بارسا بعد از رونمایی از رودری سراغ نهایی کردن انتقال آلورز خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27691" target="_blank">📅 12:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27690">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmPVpRi-xMKKrrCEVhsk0S3m2mG--pwal-4cVZBm69rW_YEtKQhejv5dzuyXK_qLEEytiEga_FW3QFa1SsPJKv9hcLiOYX6R2bLdpVVWSkhOiZu_0JonuImjKraBEWMFbFWAfSkVSXcQ_f9awaMxCe1AZI0uNdym4V4ICHzj7B3Dzv4uJ5Vc1mXnJMxcbX0ElBxFvGM0pFMJ5OXj5IpdFRW3QSO6r4mUxewIt-LYh9I6bznEFndewNZOOMDHC4KJrGgUmWqtd0yteiRqfvyOmAuJazQCDtUG_8OrCJh0TiYmt9m_pK6_ouJ1VkPogHwUjmbgJv1__3dzn05ZQ85_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفا؛ درصورتیکه پنجره استقلال باز نشود این تیم درپایان نقل و انتقالات نمیتواند سه بازیکن آزاد جذب کند و تا نیم فصل حق عقدقرارداد در سازمان‌لیگ‌رو نخواهدداشت. این‌درحالیه‌که رئیس هیات‌مدیره آبی ها امروز عصر گفته بود که حتی اگه پنجره باز نشود ما…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27690" target="_blank">📅 12:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27689">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/extWJ8_FgGiYwnCxzk9KybngeJIxoIfBjKEaG84fk9Dzr5ULQaW51DVbabcj4Zk14HkNgYx7bS8erWR2396RWYsBDokkpq_mfxd3_k3rNgjYpz8xjwDuyZyUgDbezGYw1VOv_s7rE7w12XSBHgXVtezBeaEkuPzjt3AC2aroOEgzIIF_ATRxLiJwsGOSwzT-GULBRB8LY8L57i8KHv9lnpRksGISEkBA70g8pomIbfQdgw9PvbeS2szYGz3Mj-uWbXomGwC_71NjFsG5Vpo3u_y59n8rIzE72ddrPsyPTsBN2uKAUbdVZDGpV6-q2uYcV-H19Mv8QHuEA-OXJI_9jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩵
تلگرام‌ِ‌عزیز۱۳ ساله‌شد؛
تعداد‌کاربران‌ایرانی چقدر است؟
۱۳ سال پیش در چنین روزی
«تلگرام»، شبکه اجتماعی‌محبوب‌ایرانیان‌متولد شد.  تلگرام بیش از ۴۹ میلیون کاربرایرانی دارد. ایرانی‌ها بیش از دو میلیون و هشتصد هزار کانال دارند که در طول سال بیش از ۹۰۰ میلیون پست منتشر می‌کنند. این تعداد پست در مجموع بیش از ۱۷۰ میلیارد نمایش به خود اختصاص میدهدکه‌نشانگر کاربردهای گسترده تلگرام در ایرانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27689" target="_blank">📅 12:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27687">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeWoOE17G261abpQngWYg4F9Yp4X0fRFr6Siy5JfVyaF02pV7rODWstbInUH57ZiVPaXDXAn4zIumgJ4SBPSuOmy1D4MLU2iagTIUimFp1Ju7SmOsE6gZqeV-WqgkLbQ0TDlHC-qrp7vdvpecryvGOn8ji-Q0T316AD5hR6nbboA3xc10SHeJA6Ls7EJBitnCtMPP08SRP6U3wMKFmoqoS01wclYVUf2NKxyyqTj6ssNNSbUzaWrgXZAuv-ID1P82rCpYfsznms_GkQkQIFyIo52bWXtp251rSloiTgyioqVnSbsmjD4oB8xtntMYQrPz0mROwI9IHawloa1ZRlBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
صحبت های مهم فتاحی رئیس سازمان فوتبال باشگاه استقلال درباره پنجره و آسانی: پنجره استقلال روزچهار شهریور باز می شود و استقلال میتواند سه‌سهمیه فیفا خریداری کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27687" target="_blank">📅 12:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27686">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFOI8jMvvUWU9iXTPlVAR48HGAyiYDDWjBDVX5O-MOoyGjeb2PgIC9R7iLpFozniQKqgzpvUvaKCkbOObEteHD_a0FOPeNogCHP7s2DdJ7bMr8I970X44q-DGABPAnerMnXAkWZbHWtlDkpqH8jmM-alQWn75hFfZtlHgnK_bAWmGvCNKNpguTLHSHNMZVEeRLp-TGqFhUXxRlMqaLlnBKc1tGC5yL8pSJaA-Vfv6vGXvpuEz4sXnngXhO0IxWykwIOgw7S69KilGk4zN9ZgzKpofAlnZkxmh7feD2FpbYnaADtZaIAjzhGAdqzTGuTY1FErvGNm0tHvEcIurTKj7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در عکس‌هایی که باشگاه پرسپولیس منتشر کرده علی شیخ الاسلامی آنالیزورسابق‌استقلال دیده میشه که به نظر میرسه به کادرفنی پرسپولیس اضافه شده. البته‌عجیبه‌که‌باشگاه پرسپولیس در مورد اضافه شدن او به کادرفنی اطلاع رسانی نکرده و مشخص نیست شیخ‌الاسلامی بعنوان آنالیزور…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27686" target="_blank">📅 11:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27684">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7cd0640fc.mp4?token=VlvXWSL-Sv-PGFpefPBmWMOw2fFNI5ELZ5yP8PnjgIL0eDVd8tggMznWb7UgbX2b79timqt4XUzB6SDa7xWb20TnC2s0A4mg_v44s0b86oPJKKyOvUSlOW94sem0kKSpc9IBGDYU2UM3HM6sYVkQZqui3jxgRzrMPX1N49oiQhEuL0leQNRoF6WWNO4qoaSypWtGT27thnbQ0_hu1IPbs5FlzT4p31ad-Bq8keRsX3DvRkVd7Bt1Mp5fg6eVh6hTtWdSsntAC4bml2AvpCZxe2Hpbh4J9J4tNeEGh2LAPBZCCUpRQhD8CtbVKDMo4SR6VFD7gB7PgJiDOAurXKd3sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7cd0640fc.mp4?token=VlvXWSL-Sv-PGFpefPBmWMOw2fFNI5ELZ5yP8PnjgIL0eDVd8tggMznWb7UgbX2b79timqt4XUzB6SDa7xWb20TnC2s0A4mg_v44s0b86oPJKKyOvUSlOW94sem0kKSpc9IBGDYU2UM3HM6sYVkQZqui3jxgRzrMPX1N49oiQhEuL0leQNRoF6WWNO4qoaSypWtGT27thnbQ0_hu1IPbs5FlzT4p31ad-Bq8keRsX3DvRkVd7Bt1Mp5fg6eVh6hTtWdSsntAC4bml2AvpCZxe2Hpbh4J9J4tNeEGh2LAPBZCCUpRQhD8CtbVKDMo4SR6VFD7gB7PgJiDOAurXKd3sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#افشاگری؛ علی رغم تاییدیه فیفا مبنی بر اینکه یاسر آسانی هیییچ مشکلی برای همراهی استقلال در فصل جدید نداره و کارت بازی او نیز صادر شده اما علی خطیر مدیر عامل سابق آبی‌ها از مدیران تیم ها خواسته که در پایان هر مسابقه بابت استفاده کردن از یاسر آسانی شکایت کنند…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27684" target="_blank">📅 11:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27683">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/405e5ce55e.mp4?token=EK6syPFmGTCuInoe1e9njrTZDT4HIS7nli1IpiY_hreOo8Ybx2lHMcXz4SVaheaOhUYoeur9h_2cv2V-BnrdgrJg12hlw8hjgIxTLfyY6PtwvZ0DoUgfApGiRjGuuzGfRaUD-on2jX_m0rQddY4s6iZ3n2yDrP3Q6yXineT4TGviHXxIPg7hh0UResKosS-x7Zo-0hTbm0gdt7vPlKT6DD9wFB9c8fOn-q0BBQEQFUJsx4OAHgXvPun9x0pb64AgzZ9pLVw3z1wdyzdm7sfFjY-KB1cPg_5xSM2EPpbfvgaXdaIZoRo-mP9UgetHYod6zoxVoWaFVt9_0qsAMAXJp6NLHgA4WALnuxvfVEHUIME20qZfpYM7m-uPKH7YjZzSE4mLlhvBfhipr9Tl7TYcwKFhJ6MO_T0s4pi1Wwg4udO7MJe3E_p8jdqaa0AY5swv0R1pHDq15eWtJdbz-jD-J7aqk_YMptuKPZs06TFpK241hwDo4yqAJKlTw6KUdbwzdS_Yh2wIzwgvacV7FYBWEVZC94ysJIO9aF3rck4XXIzgekUF-KvLVKdgoy-DWoONHgzXUCXrDuueH_ViPhfucZaoIR2RWIv1Gxq91adyhfXU8f-mLtgtrdvod4-PWQ43S_Q_cxrhP0hxx-KqYND3D3Uk8ftsLkXwlgt8HIQtOF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/405e5ce55e.mp4?token=EK6syPFmGTCuInoe1e9njrTZDT4HIS7nli1IpiY_hreOo8Ybx2lHMcXz4SVaheaOhUYoeur9h_2cv2V-BnrdgrJg12hlw8hjgIxTLfyY6PtwvZ0DoUgfApGiRjGuuzGfRaUD-on2jX_m0rQddY4s6iZ3n2yDrP3Q6yXineT4TGviHXxIPg7hh0UResKosS-x7Zo-0hTbm0gdt7vPlKT6DD9wFB9c8fOn-q0BBQEQFUJsx4OAHgXvPun9x0pb64AgzZ9pLVw3z1wdyzdm7sfFjY-KB1cPg_5xSM2EPpbfvgaXdaIZoRo-mP9UgetHYod6zoxVoWaFVt9_0qsAMAXJp6NLHgA4WALnuxvfVEHUIME20qZfpYM7m-uPKH7YjZzSE4mLlhvBfhipr9Tl7TYcwKFhJ6MO_T0s4pi1Wwg4udO7MJe3E_p8jdqaa0AY5swv0R1pHDq15eWtJdbz-jD-J7aqk_YMptuKPZs06TFpK241hwDo4yqAJKlTw6KUdbwzdS_Yh2wIzwgvacV7FYBWEVZC94ysJIO9aF3rck4XXIzgekUF-KvLVKdgoy-DWoONHgzXUCXrDuueH_ViPhfucZaoIR2RWIv1Gxq91adyhfXU8f-mLtgtrdvod4-PWQ43S_Q_cxrhP0hxx-KqYND3D3Uk8ftsLkXwlgt8HIQtOF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب‌ابوطالب‌حسینی درباره صحبت های عجیب‌گزارشگرافغانی حین گزارش بازی دوتیم ملی فوتسال امیدهای ایران
🆚
افغانستان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/27683" target="_blank">📅 09:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27682">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa916cffe.mp4?token=P2rCtBn-ShiX45Ku0DmTpToG0sSgox9M74yd2pH__2blki9ArFosC6B9SiJoAxWjuYus989bktpGoGo-Q39WbMXtgFWiK4RyqhNM2qIs4NIhStcTuz89HzhMdNxhsbrEwZtPLqSZDzFfgXYU28AUoluzoWoEnKl6i4-Cy_Bk4iEVu5mzW4GGNdWVht6BBwguc-ykCG5nzTA7uFcbWBZ0GW12tLwG4C7G4b0i9mI3DM07JCQ5ZB1Q0VOgvol0_HnqMT4NQkBfw2Gl46vFP_XDZDG4JbcioPedp5dT2_z1mX7bLnzp6y12G-tNiAdq5Hu3OowsrrCFTwOsHJ7c6UzwOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa916cffe.mp4?token=P2rCtBn-ShiX45Ku0DmTpToG0sSgox9M74yd2pH__2blki9ArFosC6B9SiJoAxWjuYus989bktpGoGo-Q39WbMXtgFWiK4RyqhNM2qIs4NIhStcTuz89HzhMdNxhsbrEwZtPLqSZDzFfgXYU28AUoluzoWoEnKl6i4-Cy_Bk4iEVu5mzW4GGNdWVht6BBwguc-ykCG5nzTA7uFcbWBZ0GW12tLwG4C7G4b0i9mI3DM07JCQ5ZB1Q0VOgvol0_HnqMT4NQkBfw2Gl46vFP_XDZDG4JbcioPedp5dT2_z1mX7bLnzp6y12G-tNiAdq5Hu3OowsrrCFTwOsHJ7c6UzwOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویویویی‌جالب‌وتامل‌برانگیز درباره داشتن "ادب"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27682" target="_blank">📅 09:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27681">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7f8a7f15.mp4?token=k79xuPYjKeE8ILWrKiI6jYWD67n8i5os_R6yJiBcVDif8eImTrtV7V_L2MEkPDEW2OhL5SmUiF-ZJBhRiKEvpvN3WtXeM0EcS_A3lcGBTLJIL5-rPHd-btekiUeVG9bmdTcJZz5a22Cu-Hy_g_cxl0Z1PpLbHljKGg8JipM6GixeDPDWHkvzehAGT-3Z6u287--5Cmfm5CQofM4HRBRa4WDWzwpSqzkw2zl45eex1rl06jYBVK5N2LMTUaVpDtKeIiC_tUJktsk0tknqL9-XNigomVI3sKHd3gP2NhEVmhjCarVslGmtXozVX6zjubZVJJGe0B7f76nrNUGyN_CRtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7f8a7f15.mp4?token=k79xuPYjKeE8ILWrKiI6jYWD67n8i5os_R6yJiBcVDif8eImTrtV7V_L2MEkPDEW2OhL5SmUiF-ZJBhRiKEvpvN3WtXeM0EcS_A3lcGBTLJIL5-rPHd-btekiUeVG9bmdTcJZz5a22Cu-Hy_g_cxl0Z1PpLbHljKGg8JipM6GixeDPDWHkvzehAGT-3Z6u287--5Cmfm5CQofM4HRBRa4WDWzwpSqzkw2zl45eex1rl06jYBVK5N2LMTUaVpDtKeIiC_tUJktsk0tknqL9-XNigomVI3sKHd3gP2NhEVmhjCarVslGmtXozVX6zjubZVJJGe0B7f76nrNUGyN_CRtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از دوس‌دختر لامین یامال پرسیدن‌چرا نامزدت رو بعد از پنج سال ترک کردی گفته فهمیدم لیاقتم بهتر از اونه و منم حق انتخاب دارم و انتخابم هم یاماله:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/27681" target="_blank">📅 09:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27680">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pp3yVKL-Hq-5ekPMDbcfr7jo5cRonfypmYaJ7a1ogGfSQTYVZpJ_Z33LE8uhP-t_B9-i57NK_U7HlS4mKpz5zhK5ZNBHYZFoSUYbJ8bDRwzZRhHXXKTw9OK-wHoHWuuKcIOaGNFCvKcjD0Q3vKA6O_nPh2brTocrVN4vDdIk5aMXNSMSvVZ3KR_o7IuAZLJz_p41mEc6bWM11V5dbzwErP_1Ee2EpC7w0txNRRJZ8-Sec5i0gS9LEuudwm5ixiXudqi23T-Qdx94iR4vUE3DRXktJ9ziADlyPPLQqJNL8ulWYgdr28nVBqnSO1brHwykDFbVdqV0xkvVaaSoz7Pnjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
سیدمحمدکریمی، محمد عسکری و آریا شفیع دوست سه ستاره سپاهان دیدارهفته سوم با استقلال رو به دلیل مصدومیت از دست دادند. این سه بازیکن فصل گذشته رقابت‌ها رباط صلیبی پاره کرده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/persiana_Soccer/27680" target="_blank">📅 09:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27679">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea083066e.mp4?token=nAnMvxB4z0YzUmp6oFUwpv2gakPiBdHY3Ai2LpjcDSxqFs3_8z6gmt7XAdSkPnA7vUMx3hxzDLsWcguymxq1mdWYpAs-GTKqKUCtMBbDlpJ184tjq_cGwNHZg8S1mRpxNOWe85eJUOAYLBpej5bRaaXl67U1Jock5ebKgZqlq12DH1FbrcHJ5Q4noX8erpU-1tOz9AF7erw2rNCZGvWMOnRB5KdLLATdbyZSvv9tt6bHIJlMBRHTvy5qj2oollKaLmQlJDHA214wqJnhInvxEKtlbIJucEQ5fkrCjjTNZD2WiDHVNdiPwun7mhKKH6jdYoOr_AtA-hm_oNpCoPDYlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea083066e.mp4?token=nAnMvxB4z0YzUmp6oFUwpv2gakPiBdHY3Ai2LpjcDSxqFs3_8z6gmt7XAdSkPnA7vUMx3hxzDLsWcguymxq1mdWYpAs-GTKqKUCtMBbDlpJ184tjq_cGwNHZg8S1mRpxNOWe85eJUOAYLBpej5bRaaXl67U1Jock5ebKgZqlq12DH1FbrcHJ5Q4noX8erpU-1tOz9AF7erw2rNCZGvWMOnRB5KdLLATdbyZSvv9tt6bHIJlMBRHTvy5qj2oollKaLmQlJDHA214wqJnhInvxEKtlbIJucEQ5fkrCjjTNZD2WiDHVNdiPwun7mhKKH6jdYoOr_AtA-hm_oNpCoPDYlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌‌تند رضارشیدپور مجری‌سابق صداوسیما به‌‌طرح عجیب بنزین ۸۷ هزار تومنی:
هروقت درآمد روجهانی کردید بنزینم به نرخ جهانی حساب کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/persiana_Soccer/27679" target="_blank">📅 01:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27678">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rm9WHDlWIxjNtb2LdHWN9k_uvE_L7BkAWhPv5EOwiIqmK61GBJRbUDi7Jp_HEvqniiggTyI8rP0EegwF_154rj24xXYja0nSV93DTm0-WGh23pmzFIvfFd8n72HwczkdFOEsPliSP47ZTlS_IC5goTk3GQ0sZGZtLM4s4vXwaBstGahXLqn5pLfuv0rUUUCnRTQ3b5NYP4337XICB_tBIyWj1qQfB4wrqbD7dWbABNGPLIu08nfKdWVEKZtwGCrK08UQIPU1GGm9QbYwRC0njfSjA7kklsJLFsBnNqJYKk6oE_LCFEY-1khGrSmUcHnL9l56ugGgSJmRunIUXDprJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛
شروع لیگ بیست و ششم با مسابقات استقلال، تراکتور و سپاهان مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/persiana_Soccer/27678" target="_blank">📅 01:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27677">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsHVuXxfkcEHtDIl70kTSmC4DFro_64efCGZk-Yz89llgAyMVCgAmesxxCVqRkfFwv7n-Nz5rYdMfbDadWTwfgB_8FYhM-70d1wbTC_hNeMy-9PiDr5dQ1rjmjjm4ILv5yYLHbwuqwwi6r5u3e6O6ujIcKkOkaEK8NNCRDxebPWJrBH5sa_Zv55za_SaB3eifosw2Bw3ZN1pBmeQMQyPlTV6jdTRiRy6Z0nWcQSEOdLOUpHfyS4xsmwo5Uj-vkVOpCRJ5sef-0mhxhHid6AlgOgeFqeQK_xd_guCOX8yCBX4xWc-yOwIPmDqhjxYvFuvt2Lt30uHr4grVMDz8ffU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
حذف‌زودهنگام اینترمیامی ازلیگ‌کاپ درحضور یک‌نیمه‌ای  اسطوره لیونل مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/persiana_Soccer/27677" target="_blank">📅 01:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27676">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7bEU3DO1hp0CRgllps8Nrs75UKhPJIRfTcsnD4pxCo0bXRFr1D_0GuFAMmAWG3PkYQP1KEhXYBdnfuTSJzzpxtDL-7uJjXX6HfOZjeRI5g538hdu6J-f6bC3Y5ffi67z_ZJuR6rXmVnMuikkwXxSVvkOxVpzoaFTqa5ApaibVocA7Np1U3TAp4UhBIOTdLVosha4ulMwvxDoE5X1812AqS0QuLgYSljACGSE9BmgyQfF2aEmvvotyfuXE5J3nfeYnWq5C1r-m3-_OqbQEKpR7ubl-H7G2_05CSlTRsNFjrh-NpDIDj-yGOVe5QuqBMAbzGA24cx9oaQz-yluvwBsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تمامی قهرمانان لیگ برتر خلیج فارس در فرمت جدید؛ هنوز تکلیف فصل گذشته مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/persiana_Soccer/27676" target="_blank">📅 01:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27673">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSmxEyeVyLByVggyDcgw0ETk-31DorXOktfF3q0gGBbXeotFsRa483nsr-q6w-A09aAp1D2115MVkJShX2fSr5MG8b0z3eNhjgPdenBAtThlMBMGg9ThHoc3B5PhotcJkNN-xg4zfJ5WLZQKVrBkDHPomYPMojmf4le5nXhU2U8s-Imdkak1d9JOeoUkj_8KGWx1Yq6qxiMf6VV7kyoT_UGzfjfMf61rzel0YyFRyXy8PCm5-XGtirbtrYnkE50Bbmr61AAoywkkTk3UT8DyAmgAEXl-o0fkIBJaMX_f3sNDt7sZVsVxhhDOZKSNGuvRWx5QTADCrTu4u-N9rmQyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZgFN2yVrYoYdfdPVaCepqWSx2TaKh50ywOAHDn3H1O35pEpGyHqngM3R5vP8zIAmRKuveBAuhnJ4SOUkcrNeZrnLgOZMezkt4fvqb48pkiwP6V08ZvF5Gg5QcCPnj0iurOxS6nnhObgjzbKq-mksJN0G9oiVp1Unn6MEUe2Li2xDAaiS04wo6FiQVE6vcNJbh_3AjJV_uc9Otop_DBausvgANJhXef4L6JD5R3udsmS-SVMwAnPaMO5zG7KOLsqJoJbMbO0NMFX14wvCFKSmDU-ssWWwXjiOoAwYuILmXu5klswpfUfLBycwsN3xAnlHiTizSFeqdr6nocK0kzNd5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
🇪🇸
#تقویم؛ سال 2024 در چنین روزی؛ رئال مادرید تحت‌هدایت آنجلوتی برای ششمین بار در تاریخ خود قهرمان سوپرکاپ اروپا شد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/persiana_Soccer/27673" target="_blank">📅 01:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27671">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsy1FgvcOuKWia-Q8OZAgL3st48EC3cdbWmLETByj9CdG2mRzXp6BwM26tIApeDfwBnesqzVQ_DWwrbDhUdtC5X3ClOX2QtyAJ7Wi0irXdGMmC-lspYLxQcRsu_HOmq61IZ_jGSei8h3B4F5R29i8MS9XwPh3UK84J_GFNOGyrJQy9DwbhJSd4VKkoJOo1-7_Jvut8AD8A7sNaAjv61gluUIeJkzlsKvtBTAwJMJem3gLzJ_CGqaamiNUCTYq9rvktWGvFSOnKN-QHhVXNLivEJgPt9z49TAxbwrfbeSYoPnHI7XZibQuLhN3YxIoKsIog3xPtUu2J6ZhF0hwHWyxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6583225e2.mp4?token=mv2DGDCddzitxey04TuHrOP0q-uTD7T6iEg1C8iteUBonVe4Fi1Q8UTPpiKy0uJrWKCvDK5zFMlehh61wKTgNjaCf_G15Adq-8LvralWwICqZTPzVenfX6AYgKIKfD0ydjHU3FLATNw518Fw9RhaqGapLDDieav2glSlV4snLSrkAx0dbuMiFAWwrnIuPtekc41ZHTalgGi65BZcVEyRUyU6LSvuXYyggwYieyUdhcj2-oFjTiPKON6jy7UAZ0_4sQLq3HjDcgnI0fBNvWS0BohXHwNDIhNtJGAZWgaDajPHOkxzYz5-K4nY0kzUceD0tAM9BdpVQ45itI2MHhI9pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6583225e2.mp4?token=mv2DGDCddzitxey04TuHrOP0q-uTD7T6iEg1C8iteUBonVe4Fi1Q8UTPpiKy0uJrWKCvDK5zFMlehh61wKTgNjaCf_G15Adq-8LvralWwICqZTPzVenfX6AYgKIKfD0ydjHU3FLATNw518Fw9RhaqGapLDDieav2glSlV4snLSrkAx0dbuMiFAWwrnIuPtekc41ZHTalgGi65BZcVEyRUyU6LSvuXYyggwYieyUdhcj2-oFjTiPKON6jy7UAZ0_4sQLq3HjDcgnI0fBNvWS0BohXHwNDIhNtJGAZWgaDajPHOkxzYz5-K4nY0kzUceD0tAM9BdpVQ45itI2MHhI9pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇪🇸
#تقویم
؛ سال 2024 در چنین روزی؛
رئال مادرید تحت‌هدایت آنجلوتی برای ششمین بار در تاریخ خود قهرمان سوپرکاپ اروپا شد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/persiana_Soccer/27671" target="_blank">📅 00:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27670">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GW_oiZTSaTq5tnCaFiB6oSa4eMwyvR8VS5SSgQkZs2hY8Ab_qTsVnezo9O_5tF4fWMhCWQ4Z80Pwe6jUEcaYoRh-ghggAWnecVTAmIWnjX839zqBz5o2BVfj0A2LFQOn__TD-tLc_Hg20ClUMz6ZE791mBd5cKCQteJX4M_z9IZI3GCm3NZmDisB-0x-sx1vy4uhrmkJddTf2u5SDerzZZ-Ms6-R_rS4SzS4nlH-3bpZAjU116qsxtbKfa15HMYYlXONBtiDH6lSmztxzHx4IIn0-4bA7woMatG4oB2acrfGyG9duud7zoVX5yJ5BwL3SPS2me_GfaTXPFgKK8GHJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛باشگاه ریوآوه پرتغال یکی‌از دوپیشنهاد اروپایی محمد محبی ستاره 27 ساله سابق‌باشگاه‌استقلال است اما رقم پیشنهادی این باشگاه 400 هزار دلار کمتر از رقم پیشنهادی تیم استقلال به این ستاره ملی پوش است. ایجنت محمد جواد حسین نژاد و محمد…</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/persiana_Soccer/27670" target="_blank">📅 00:33 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
