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
<img src="https://cdn4.telesco.pe/file/EO0Bb_JHu0cFOZvaT0eEsTScVUdqID8C85REbE7mNDK9OQqx4b1nAgYtTMc-YT-g_3Sw0l88g3DXi8iRgQez8q5P_V70wsJM969k96u1aLl184wNPQ6MvxX315jGIhFxf6HaGCCDiIsDgcNQMlB_BsxNc7dh_M-0R3548TfZopx6mNlYWyUUJr5ZHbVgwRBIOkPOl2iARAmajqS-8EModarv48BvDp969nFclUzJoBCiTfNrmiPK045PeD4rbzhbDX6nBgQNDGasdpTZhYbr0jHBsQ3lty3r1Zrn31uCKtjELRmY4JgTpjrFJq8CzWsUpVP9tfNbGlGokP7IJ8N2KQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.47M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 20:39:24</div>
<hr>

<div class="tg-post" id="msg-697811">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfP45LnWt-BHPdBFPncXAjcutrDYkGUp7pEORr_q4nVawq31b1qk2UdZTKeeQY64b4m-7NMHrwljrmFzknAOJxMLXLRvZ8Um53zXzL7U_crQhRnmdIXd0hqiTRTanE1vyUcbdg9a5aAAntVRwVTeMCopryS1wf0LUwFnBC7HOgUylEkAeLp5nRezvJ25bwVUmvueTZSwhgKeOPyOyRONgaD8x8P1H-d9_VJlDYplJYQn4JgP1nYnajY7dKM_0v7NU0Qh7jf-v_w7lNowEVUW8sIWRyO1pmBRCwZESYU2P2ctlqijMT1vlOOEjIowHfuXt3gG4Pbb7lc2QpF_EvDqrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3bc8d410d.mp4?token=SV9SvB3P0JjcIb8N9MViMpUe5WUqXYbtKTRhoLHyQa2MQL3mICvkM4Ag8R4nNI1_3VCpOBdBC9GMpaPee3veeXcVdp3cpIk7mVZrmYE9GaXyLTKBhxFF6izEDlWZ-FI70U3smOR0HBDtw50UEQk6IxxVrWKF6RsKJvuIIjngg66r1IqpyywiluHITmbt7jhjiPRlEF0gTeywIBFLD7-tzW8CkVrmLJObV5bHH-jmBamt7HvvOY4PxBm0SNjUATiHZNCNmWUBghi2r8BgRaD-kkkNNJssahPdmCfyl_kcNKIlJUlNejjzwBisWjskqqQeJj8RrWr0wHF3fvWBhjsjxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3bc8d410d.mp4?token=SV9SvB3P0JjcIb8N9MViMpUe5WUqXYbtKTRhoLHyQa2MQL3mICvkM4Ag8R4nNI1_3VCpOBdBC9GMpaPee3veeXcVdp3cpIk7mVZrmYE9GaXyLTKBhxFF6izEDlWZ-FI70U3smOR0HBDtw50UEQk6IxxVrWKF6RsKJvuIIjngg66r1IqpyywiluHITmbt7jhjiPRlEF0gTeywIBFLD7-tzW8CkVrmLJObV5bHH-jmBamt7HvvOY4PxBm0SNjUATiHZNCNmWUBghi2r8BgRaD-kkkNNJssahPdmCfyl_kcNKIlJUlNejjzwBisWjskqqQeJj8RrWr0wHF3fvWBhjsjxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله جدید یمن علیه عربستان سعودی و ستون‌های دود از تأسیسات انرژی در شهر الهفوف، واقع در شرق عربستان سعودی، به چشم می‌خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/akhbarefori/697811" target="_blank">📅 20:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697810">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
زلنسکی: قیمت‌ گازوئیل به حملات ما به پالایشگاه‌ها در روسیه بستگی ندارد؛ این موضوع به انسداد تنگه هرمز بستگی دارد؛ همه می‌دانند!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/697810" target="_blank">📅 20:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697809">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
شریعتمداری، مدیر مسئول روزنامه کیهان: کابل‌های اینترنت جهانی از زیر آب‌های تنگه هرمز و خلیج همیشه فارس برایمان دست تکان می‌دهند می‌گویند؛ چرا نقش ما را در این جنگ فراموش کرده‌اید؟ ما نیز در این آوردگاه، جان‌فداهای امام راحل، آقای شهید و امام حاضرمان هستیم‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/697809" target="_blank">📅 20:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697808">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1198c495c.mp4?token=rgK2qbgxUoBRll2PXP5qYccleVmKH_KRTp-VqLfOeMpE9Tg0GKFpctZqfOmQLX5FQd0bbqNYaa8A3jjwmDsYGPVjpb5mP1nRsfMMKh0VZ0eM733fdkiksyUAjSO7n3SaQCKW85puZTnlV18a2XKQG551R41t-tCoEF80GdFvvALRHmpRmLt9sdjR6gd5fnRvkPB0BM0Jdre93fLSOdktNRElEJF85p6uT30-ZtI3EwdBMsRhZGY-6XJa-iWJSF0kPe-y-9Gf5FtORplq6MGAye2O6WKvVHvYdNNW13bIOXnwnoOmt5BxEypJesDt6Ecl3gIjdCF2whMHXR3YEALYKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1198c495c.mp4?token=rgK2qbgxUoBRll2PXP5qYccleVmKH_KRTp-VqLfOeMpE9Tg0GKFpctZqfOmQLX5FQd0bbqNYaa8A3jjwmDsYGPVjpb5mP1nRsfMMKh0VZ0eM733fdkiksyUAjSO7n3SaQCKW85puZTnlV18a2XKQG551R41t-tCoEF80GdFvvALRHmpRmLt9sdjR6gd5fnRvkPB0BM0Jdre93fLSOdktNRElEJF85p6uT30-ZtI3EwdBMsRhZGY-6XJa-iWJSF0kPe-y-9Gf5FtORplq6MGAye2O6WKvVHvYdNNW13bIOXnwnoOmt5BxEypJesDt6Ecl3gIjdCF2whMHXR3YEALYKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از حموم چجوری موهاتو خشک میکنی؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/697808" target="_blank">📅 20:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697807">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
بارزانی، رئیس اقلیم کردستان عراق، تأیید کرد که میانجی ایران و آمریکا بوده است/ ایران همسایه ماست و این جنگ، جنگ ما نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/akhbarefori/697807" target="_blank">📅 20:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697806">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/147c7ee345.mp4?token=lm5jdjyqAJVYkJ2BOyUNwfprdrUJT6fNod_F0mNz8CBV5HbOuhLFb0oe2ORsvLJURcDMbqLKEaSZ5EoGg7aGl0-lr_K6NwsqARSkwd0wvOiu_V2Aml52V6uznmo5DQu2801Q8sihDl5lo5rCY_X7HlhDyFeqHo3KOGM0iTPmCV0imWCJfsisuUhtXyZEkzVgy8ZNTY28uJyE6SXUz5bvAD_iJqd95W7vOuRYNlSosl8Gwuxsfe4Nwp9rM9bLDPz0m-nTMTNtwqVirytlFzZNuXSgJ9woY_le14X2TyYLdFMKAA_DD6eY_Is6jYRzCSw4SI6ontLlsDFp7j-IY8Ws5Rl7OsWxnlqMu2l72eK_eCyckXaArXUuu5igAEwVgxMmxvSzV7-FvhC2cnO35iqQfTV1zsUabW18FZXpVX62xd8w-DV1-iEAP8XxapCl5WlCn1F53Uj9NT-suqxDqBshVjTXQvj9WmyoaoLAq4-E_bCkdttGhOApyMFLwt-Ik87ioUA3N4k7RVDM6doFm4DIjTnemJXLGZTqsmfbYW0BMkZplvltmhHKnTMaTdcuyLSOKCLOIz4mnO6VP4iTYAKGxUtzn4U0x767GYYBqqvgWTh0-oxg52URo08h5AZNvGwAOgNvLji236E7iG1Z_dMW0yXIedMbT7kv09xfu0gcXDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/147c7ee345.mp4?token=lm5jdjyqAJVYkJ2BOyUNwfprdrUJT6fNod_F0mNz8CBV5HbOuhLFb0oe2ORsvLJURcDMbqLKEaSZ5EoGg7aGl0-lr_K6NwsqARSkwd0wvOiu_V2Aml52V6uznmo5DQu2801Q8sihDl5lo5rCY_X7HlhDyFeqHo3KOGM0iTPmCV0imWCJfsisuUhtXyZEkzVgy8ZNTY28uJyE6SXUz5bvAD_iJqd95W7vOuRYNlSosl8Gwuxsfe4Nwp9rM9bLDPz0m-nTMTNtwqVirytlFzZNuXSgJ9woY_le14X2TyYLdFMKAA_DD6eY_Is6jYRzCSw4SI6ontLlsDFp7j-IY8Ws5Rl7OsWxnlqMu2l72eK_eCyckXaArXUuu5igAEwVgxMmxvSzV7-FvhC2cnO35iqQfTV1zsUabW18FZXpVX62xd8w-DV1-iEAP8XxapCl5WlCn1F53Uj9NT-suqxDqBshVjTXQvj9WmyoaoLAq4-E_bCkdttGhOApyMFLwt-Ik87ioUA3N4k7RVDM6doFm4DIjTnemJXLGZTqsmfbYW0BMkZplvltmhHKnTMaTdcuyLSOKCLOIz4mnO6VP4iTYAKGxUtzn4U0x767GYYBqqvgWTh0-oxg52URo08h5AZNvGwAOgNvLji236E7iG1Z_dMW0yXIedMbT7kv09xfu0gcXDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفیر پیشین ایران در بیروت: پیجر من قبل‌از انفجار به‌صورت فینگلیش نوشت «یک پیام فوری دارید»
🔹
اولین‌بار بود که با چنین پیامی مواجه می‌شدم؛ روی صفحهٔ پیجر نوشته بود که «برای مشاهدهٔ پیام دکمه را فشار دهید» و به‌محض فشاردادن دکمه، پیجر منفجر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/akhbarefori/697806" target="_blank">📅 20:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697805">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
۶۰ کشور طی بیانیه‌ای مشترک اعلام کردند متعهد به آزادی کشتیرانی در تنگه هرمز و مخالف با وضع عوارض بر کشتی‌ها هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/akhbarefori/697805" target="_blank">📅 20:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697804">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0943e68ce3.mp4?token=aQH5IODBeiJ1kiSuzdZPN5BSPVXmdHGDQzA360imeMgoUmi5fKK03Vvsxg4KzqPdkXfN5NGERsXKGz_WM59Z9t5Id-F6C4zcT-B8N0KZZdV-VQAGGzQ9T9WlSi2RibaeiQKHORLP9zfxbj3rN197_2PimHqG4xBFYgNMRharFS8apPN7Q6XyAD_CzDpJQj1Ez3aC5HU5aLPZqN83ktq3UdE1s3mOEpHhRVHhuod_uCYSLIt0YeMYJs0YuA6bgiyLykprYnOyXVXQuy4ch-rhNgJLM1c9OX9IVAbPBZQE9psAZbKxkCwt5oFota5YjDNJdUPtSyYVloT52ZeGiKyf-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0943e68ce3.mp4?token=aQH5IODBeiJ1kiSuzdZPN5BSPVXmdHGDQzA360imeMgoUmi5fKK03Vvsxg4KzqPdkXfN5NGERsXKGz_WM59Z9t5Id-F6C4zcT-B8N0KZZdV-VQAGGzQ9T9WlSi2RibaeiQKHORLP9zfxbj3rN197_2PimHqG4xBFYgNMRharFS8apPN7Q6XyAD_CzDpJQj1Ez3aC5HU5aLPZqN83ktq3UdE1s3mOEpHhRVHhuod_uCYSLIt0YeMYJs0YuA6bgiyLykprYnOyXVXQuy4ch-rhNgJLM1c9OX9IVAbPBZQE9psAZbKxkCwt5oFota5YjDNJdUPtSyYVloT52ZeGiKyf-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان مک‌آفی، برنامه‌نویس در سال ۲۰۱۹ پیش‌بینی کرد هوش مصنوعی طی ۱۰ سال به پیشرفت عظیمی می‌رسد و در صد سال به دشمن بشریت تبدیل میشود: ربات ها قدرت می‌گیرند و چاره ای به جز بمب اتم نداریم
🔹
او ۲۰۲۱ در زندانی نزدیک بارسلونا درگذشت ۱۷ ماه بعد ChatGPT منتشر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/akhbarefori/697804" target="_blank">📅 20:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697803">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a30c6a92d4.mp4?token=r2AkJEOXTxHkz1bRH8jyrSKae3H0sIepKCD36WBbp-OLFZwb2g_cYVdWh_fTjyuKzd8NcwE7pPh48D_ZyVayLsPbgl-K1sCAxLQJNF3KSkWjKYQcG5qOa7NqXwS1TWqA6OSUYZq7YsNxeJstaO5h4H5svJvSoWBbZYRkwaSeY_3Aw-tUXZ9-4Q3-DexaVOLJwkZvQx42qDdax8f1T5scEHIGaR2skxajpmKu2vj6kvy7H-qc2DnwbbfVWwqzSZD51EDKhaMINpL7i_V2GwsrXk-94LlUrnGh9TumU_r4uUbzBUER77bpezWOwYSGiQ01k2VY9wU9e0w6BG1CaMsFQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a30c6a92d4.mp4?token=r2AkJEOXTxHkz1bRH8jyrSKae3H0sIepKCD36WBbp-OLFZwb2g_cYVdWh_fTjyuKzd8NcwE7pPh48D_ZyVayLsPbgl-K1sCAxLQJNF3KSkWjKYQcG5qOa7NqXwS1TWqA6OSUYZq7YsNxeJstaO5h4H5svJvSoWBbZYRkwaSeY_3Aw-tUXZ9-4Q3-DexaVOLJwkZvQx42qDdax8f1T5scEHIGaR2skxajpmKu2vj6kvy7H-qc2DnwbbfVWwqzSZD51EDKhaMINpL7i_V2GwsrXk-94LlUrnGh9TumU_r4uUbzBUER77bpezWOwYSGiQ01k2VY9wU9e0w6BG1CaMsFQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراضات دانش‌آموزان مسلمان و والدین آنها مبنی بر ممنوعیت ورود دانش‌آموزان با پوشش اسلامی به مدارس در آذربایجان
🔹
بیش از ۹۵ درصد از جمعیت آذربایجان را مسلمانان تشکیل می‌دهند و معلوم نیست علیف به چه علت این تصمیم را عملی کرده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/697803" target="_blank">📅 20:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697802">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">25-1 Ane Manaee (1404-02-14)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/697802" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیست‌وپنجم؛ بخش اول
🔹
واگن‌نشینان واپس‌گرا؛ عقب‌گرد به حیوانیت پس از هدایت، با "تسویل سازی"و "تلقین تدریجی (املا)" شیطان. [01:08]
🔹
تأملی بر ابتلای حضرت یونس و قومش، و سنجش "توقع" با "تفضل" در ترازوی الهی.   [12:28]
🔹
تمثیل قطار هدایت و استعاره واگن‌ها از سطوح قرب به خدا و انسانی که مسافرمسیر تقوا ست. [19:40]
🔹
فهم اینکه "در موقعیت خوبی نیستم" کلید رشد معنوی و آغاز تغییر و رحمت الهیست. [26:57]
🔹
استغفار، گشاینده درهای نعمات مادی و معنوی [31:00]
🔹
جلوه‌های خلقت الهی در دنیا، مُشتی ست نمونه خروار در برابر صحنه‌ی هنرنمایی بی‌پایان او در بهشت [34:36]
🔹
ثروت، شهرت و ظواهر دنیایی؛ عامل فریب خوردگی انسانِ محروم از حکمت حقیقی. [37:53]
🔹
هر چه انسان به تقوا و اخلاص نزدیک‌تر، مسیرش خلوت‌تر، سخت‌تر و پرمقاومت‌تر [44:46]
🔹
”خلوص نیت” تنها راه رسیدن به قرب الهیست. در این مسیر، رضای الهی محور همه چیز و فراق از محبت الهی بزرگ‌ترین رنج است! [49:40]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/697802" target="_blank">📅 20:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697801">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff025506a2.mp4?token=EkBHKd00OTCuYs-w5kR25AepKZ6ya7Qj8bCngXFe9iwEkHODhTLnWIegggSoJbN_MYuvLuZZnOtRBya201hM659sfBgGSlfRPdgc7XEPQ_6AeXGhjR5omJ-l2Ft2LRUHkvddgKGa4_LhHHTpa87hrt_uC974fPtseooaPcJmneLwfrbqRiOF_FG1yvXEMtPY7UFoCFJkTJiIlJSoBGliDLGZ_7PkBDlSzeGq9r4P_qyomeuOBgsflCd9MN-ueYAlpvM0xt0hjUvmyCSbxfCE8tWgWedQdtlLDGjP6f6cdNhR-qoYFs8Zx7eywBan7g-y1N3z0ijk0KV9d6Mb6Y_otg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff025506a2.mp4?token=EkBHKd00OTCuYs-w5kR25AepKZ6ya7Qj8bCngXFe9iwEkHODhTLnWIegggSoJbN_MYuvLuZZnOtRBya201hM659sfBgGSlfRPdgc7XEPQ_6AeXGhjR5omJ-l2Ft2LRUHkvddgKGa4_LhHHTpa87hrt_uC974fPtseooaPcJmneLwfrbqRiOF_FG1yvXEMtPY7UFoCFJkTJiIlJSoBGliDLGZ_7PkBDlSzeGq9r4P_qyomeuOBgsflCd9MN-ueYAlpvM0xt0hjUvmyCSbxfCE8tWgWedQdtlLDGjP6f6cdNhR-qoYFs8Zx7eywBan7g-y1N3z0ijk0KV9d6Mb6Y_otg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تو هم همیشه با برگشتن نوار لبه وسایل چوبی خونه‌ات مشکل داشتی؟ با این ترفند آسون خودت تعمیرش کن #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/697801" target="_blank">📅 20:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697800">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عرضه مستقیم و بدون واسطه انواع فرش و تابلوفرش دستباف، با بالاترین کیفیت و قیمتی استثنایی!
با حمایت از کالای ایرانی و هنر دست هنرمندان برجسته‌مان، زیبایی و روح هنر اصیل را به خانه‌تان هدیه دهید.
✨
چرا باید سر بزنید؟
حذف کامل واسطه‌ها و تنوع بی‌نظیر طرح و نقش
مناسب برای سرمایه‌گذاری و زیبایی دکوراسیون منزل
خرید مطمئن مستقیم از تولیدکننده
📅
زمان: تا ۲۴ مهرماه
⏰
ساعت بازدید: ۱۱ الی ۲۲
📍
آدرس: نیاوران ، خیابان باهنر ، خیابان فیضیه ، اردوگاه شهید باهنر
منتظر حضور گرمتان هستیم! برای کسب اطلاعات بیشتر پیام دهید.
📩
📞
09127599612</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/697800" target="_blank">📅 20:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697799">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
دو درخواست پزشکی علیرضا بیرانوند، شامل آسیب کتف و ارجاع به کمیسیون اعصاب و روان، رد شده و او باید اول آبان به خدمت سربازی اعزام شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/697799" target="_blank">📅 19:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697798">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1723a778d.mp4?token=IvHlzT2rnKGGrjbRhYEA9W72-A6p2E5TVKzTQ8cRb_bO16ZSIgHWqbEDHgKCiIj0bSdjJmqtZYmguKwoXlF1CCz6H7bVanHGhU3MseJLT3KV12hVrlvcHIvqB2Cf5_sM1li-ZsdfEQoVzFfraZJJC3XSn8Kr2ZzyrDp_8pDcRzIhA5eX9okXQeRP8SN9xMmFPEs_diK8KlZ9-9eQf77-VC7VLHVjcC1Tycr74rctnDGubs0KBt2--83PlzsXgU7sRK3ccfdxVfPzm93IY2TmIZ1t_1ZzJrhviBtRKQL-pbq2XgsK0Dbndr0lLZW58wCG6tXYbZMnPpMMV_H9GXWJzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1723a778d.mp4?token=IvHlzT2rnKGGrjbRhYEA9W72-A6p2E5TVKzTQ8cRb_bO16ZSIgHWqbEDHgKCiIj0bSdjJmqtZYmguKwoXlF1CCz6H7bVanHGhU3MseJLT3KV12hVrlvcHIvqB2Cf5_sM1li-ZsdfEQoVzFfraZJJC3XSn8Kr2ZzyrDp_8pDcRzIhA5eX9okXQeRP8SN9xMmFPEs_diK8KlZ9-9eQf77-VC7VLHVjcC1Tycr74rctnDGubs0KBt2--83PlzsXgU7sRK3ccfdxVfPzm93IY2TmIZ1t_1ZzJrhviBtRKQL-pbq2XgsK0Dbndr0lLZW58wCG6tXYbZMnPpMMV_H9GXWJzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عناب؛ میوه‌ای کوچک با خواصی بی‌نظیر
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/697798" target="_blank">📅 19:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697797">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
سخنگوی کمیسیون اصل نود: زمستان سختی در پیش داریم
🔹
پالایشگاه‌هایی که مورد اصابت موشک‌های آمریکا و اسرائیل قرار گرفته بود، فازهای بسیاری از کار افتاده بودند. قسمت قابل‌ قبولی از این کار جبران شده است، اما هنوز به نقطه مطلوب نرسیده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/697797" target="_blank">📅 19:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697796">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/714fb5cb99.mp4?token=WL16jTBCPV7dNUmN2vi-hixqGieU7Ft3dVyCCvREBCr5ObNpuOCamlQ6kN0zCni9aglDXNhnT9BR4O-EuOLz5DsKS6osaVwxibKdlcvxI_0lJpxv_7GLR5a2BzNF8thNYd-ewigUIgjSbtI_64nU-miMuNIkURNy29amSec0sbNkTROCRUFi_yMeWjQ-tckRy1cZfZ3dSOLjcqLPPDYgVwxpFqZv2Z5pFneeWVyEkdY2CNG9YBKGkrQlkis-vQ6082iC6ofTya7i9T_Xkg26hDy3TM_KtT9yeHGOGLMSSienJAac3jZTOQcmOs-DDu_MkRfRfw9rfDwBNsahnNjrdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/714fb5cb99.mp4?token=WL16jTBCPV7dNUmN2vi-hixqGieU7Ft3dVyCCvREBCr5ObNpuOCamlQ6kN0zCni9aglDXNhnT9BR4O-EuOLz5DsKS6osaVwxibKdlcvxI_0lJpxv_7GLR5a2BzNF8thNYd-ewigUIgjSbtI_64nU-miMuNIkURNy29amSec0sbNkTROCRUFi_yMeWjQ-tckRy1cZfZ3dSOLjcqLPPDYgVwxpFqZv2Z5pFneeWVyEkdY2CNG9YBKGkrQlkis-vQ6082iC6ofTya7i9T_Xkg26hDy3TM_KtT9yeHGOGLMSSienJAac3jZTOQcmOs-DDu_MkRfRfw9rfDwBNsahnNjrdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عکست رو با این کدها به هوش مصنوعی بده تا این خروجی‌های فوق‌العاده رو بگیری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/697796" target="_blank">📅 19:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697795">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W61gos6hn2oCux8QaFOGFodAwikIOELE73d1tdKRSWMt7GtIdtKe4lkmXhbccGMDQVJgXH62sASf74sKCvOoE9OmXwLD4U-5sze-2DbDhifJY0KBdkcP0bjqyxUcWAEd3QjVRKCaoGHdEzEbj6l5RJSf1hWUwuhrcEEnJM6YxKtLS59r5FEiNGoPCBLX7V7r_qFNQLtrsjRaLAMZAnXSpmkfhQGnQToOIqC7EgzHb91e4jIZ6BcWO2vGFfqmT1qcP2U_BnUdF7cNzY9fmJbHg6Q9GjSJv-ZTACywPpUtGpCIl83845Z6jbtDdaairNRPE5ZgHOwNr7TtP2IVUWENGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان تجارت دریایی بریتانیا: گزارشی با تأخیر دریافت کرده است مبنی بر اینکه یک نفتکش هنگام عبور از تنگه هرمز به سمت خارج از آن، هدف اصابت یک پرتابه قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/697795" target="_blank">📅 19:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697794">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ادعای لندن: حمله نافرجام به فرفورد به احتمال زیاد در ایران هماهنگ شده است
🔹
پس از حادثه فیرفورد، تحریم‌های بیشتری علیه ایران اعمال می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/697794" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697792">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
رئیس پارلمان ترکیه: پیمان دفاعی «مکه» علیه کشور مشخصی تشکیل نشده و حتی ایران نیز می‌تواند به آن بپیوندد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/697792" target="_blank">📅 19:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697791">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d32Bdbgd-A-ko0XBbtbEDfD7y8rPJOHH5mzzMIAeE2Fl1IhA3ZZ8GxswB8mzKJ3XerHxZwKoXH1cPXekabDRt5SLoeik0rC4ZmA6nrrEdtk_2d6HbGwpF9k6xXvirOx1d4ny9wgq8Z_QH89b_xO6srYs_o_C4plPAdBo0pm1I9DgRjYukFEjS8k1ByAb-P38WiL10Y1nai5QHHgiTkCq5oS4j7V0OI-5qZtv4Q6W8zqjZV9oNmDcHHHdARLBYpU3s_LsWYhwGwM3dtCAXHTBV-qZobLWLPqT904iR1H4GoDiYZlERBpveayRYeUGjGSNmnqDeDTP5e1TOn8KzPO7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت خام برنت به بیش از ۱۰۶ دلار در هر بشکه رسید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/697791" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697790">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFCWZxoWG1jX_itwuG1R-yUDXpZIhedcA38TSnJNizZ6K934Lmdy83FcsTVfjq-MB6t6m6PCR1SMVHRQ1QAsbVHlI-XbERjuc_MnD5krrIGEDTguNYmqH-kuKBf88Pfsgkpmdvr-4A9-dgOHzDDiHh9r04UsSK3u0WTOnR6PeWt8-Ld7TrTXbGTf8QdlSBHd-ZVJuKxzOinsNl4GPeJ3t-KTBNTjhY5eLN8JScMsyYo4BcQVCByv7TjQ00S3_NPRo6CAf8J0tcXe5lanzkrXiWCMYcSXoZDRF1tcLawsfElIzbOgK9hbt8JdWC0dxcRIpp2tOo6p2hKL_edzEKVfXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهار نوسان دلار در سایه محاصره اقتصادی | آیا فروش ۱۰ هزار دلار به هر کدملی اشتباه است؟
🔹
بانک مرکزی با آغاز طرح فروش ارز تا سقف ۱۰ هزار دلار به هر کد ملی و اعلام تزریق ۲ میلیارد دلار به بازار، به دنبال مهار نوسانات ارزی و کنترل انتظارات تورمی است؛ سیاستی که در روزهای نخست اجرای آن با کاهش محسوس نوسان قیمت دلار همراه بوده است. با این حال، تداوم این ثبات به میزان منابع ارزی در دسترس، نحوه قیمت‌گذاری و چشم‌انداز تحولات سیاسی و اقتصادی وابسته است.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3251807</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/697790" target="_blank">📅 19:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697788">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGhp240HHPaEbfiaD3k0XUohZNN6URA__HNU0h0zlEf9o9tpaG6rEqa-JXDwxAeMK8qJeqJFsqMI1jmXN-ViVQH5s8LtCLqKEVZ8o25YYOTZaBL88_vaJ2fAYRTPNYN8Qeacg2kVDrYoSNWORwssosxSjm4z78i2fu8SM8TTog0uJwoIonfxfwfj0zxmteOD4ZkH4_mtRnjYwAQ0YeBP_ILR4v3BLAadtKp1httE18GQkXvN6L2PB-hEU8D3cx2KuBHtp_HIETidM6XF3lfHUyJsGEQmqApRrjxLMZpTYTMwHcmOdNadYyR1zFnQK9p1WtuCooGZ4CXr8zTKbO3-Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRMdOxnd5J4XyK2E8bJNSff-sTPbMu-xzjM0QFz_624xgDfGDypvEob2WFdr6hFi-0HK6OxqpeJxwcM47I4bRH2G0OUPOV1tuahLdX1WX2HIZnSCiNKZYzR693d_kHJ427YghBPjJssonwmv3v9io8BmHzAcd69KRR5FwohVWdEqnz5I0YqB_kU5GcxZP4cQgOTIyMkKsJnLkXJI4jAbY2GRA1qcvAQsB-jpEQ4zMowTp0sjyz9zzkKu9wEGTDyxRsZnFBKOY3LRgJfVrxq5qBC7r3Ng8WieOkUinrVo40HKC2Ed9wFlI9ZXb01h5MAxgkST_GelCw_LCIU3xKd6gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گوگل از دستبند Fitbit Edge با نمایشگر اولد و شارژدهی ۷ روزه رونمایی کرد
🔹
دستبند Fitbit Edge با نمایشگر OLED حدود ۴۶ درصد بزرگ‌تر از Fitbit Charge 6، حسگر نوار قلب و قابلیت تشخیص ضربان نامنظم قلب عرضه می‌شود و با هر بار شارژ تا هفت روز شارژدهی دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/697788" target="_blank">📅 19:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697787">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای گاردین: پس از دیدار مقامات آمریکایی با یمنی‌ها و اطمینان از اینکه کشتی‌های آمریکا هدف حمله قرار نمی‌گیرند، واشنگتن از حمایت نظامی از عربستان خودداری کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/697787" target="_blank">📅 19:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697786">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a11cf508c.mp4?token=NgwwivRSPKdgu8NKlX8y8kqwmeir_tCfNiGgMZBrwvjG3JrVC_ytEvPraaamcubCRCfkQ6x40dtEfQpLD8PRILIEmPw7p7qu8LC5novLSbYC62tn6t4e0QVZyEQRPX6tkJs9Eas2k8-unwxgN8675Za34sNlChowKaGQUdebBHwCAXjZ62AlCjzBg_fofmqhWjA6NwFSJPOcPiDvESWWRdD_TcZ5rmsl80oZnjGmLN0BXdNCu0IqeJD6A-N6JBMGPn6G4DcRFN6cZPMjNUznTx6MmI55Ozpf-Cdy7Iz4chjVySAV8y_1UVcxOruBw9Lsc0zTA6Eo_3X8QThq5KoC3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a11cf508c.mp4?token=NgwwivRSPKdgu8NKlX8y8kqwmeir_tCfNiGgMZBrwvjG3JrVC_ytEvPraaamcubCRCfkQ6x40dtEfQpLD8PRILIEmPw7p7qu8LC5novLSbYC62tn6t4e0QVZyEQRPX6tkJs9Eas2k8-unwxgN8675Za34sNlChowKaGQUdebBHwCAXjZ62AlCjzBg_fofmqhWjA6NwFSJPOcPiDvESWWRdD_TcZ5rmsl80oZnjGmLN0BXdNCu0IqeJD6A-N6JBMGPn6G4DcRFN6cZPMjNUznTx6MmI55Ozpf-Cdy7Iz4chjVySAV8y_1UVcxOruBw9Lsc0zTA6Eo_3X8QThq5KoC3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلنسکی: قیمت‌ گازوئیل به حملات ما به پالایشگاه‌ها در روسیه بستگی ندارد؛ این موضوع به انسداد تنگه هرمز بستگی دارد؛ همه می‌دانند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/697786" target="_blank">📅 18:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697783">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f381241a7d.mp4?token=VBoG_oswABEQoUZVj3PS52RzrcsdAg2oft9_p07q5WX4t47Klt9Lf9sQzheyUShP7b7KtV-HBpvInvuvcPt23dX3lsaREZ3i-KwIP34xu9r2Uw2aW8UYB3zmNEM0bgHhShfLLgF5R6s13Zmo40ZIwxy-PRYbMGil1Ks2jj5hGF2-3GppW-KrFIh1nSPXoFrJl4GOFz78-8sy9heqEngVmSvvi1urmSYpUNKMxdgD3qrXbxuX1zjy0Kz-uiMnhI-tH0kokCHM-a8goWaU9n01KHSqbz9Dy8pZczGuTkC2iVLvdznTmrt2D1_nVXyvFoWCZJ1jMatjcE6c_Ge2APemB4CucxWYGbK_KXK3RvDeu-ljVH0BE9pD9rUtB9kXbIbpYq2NOegBSX1mWIlLM01DM8htI2CY-etE7ZuPKWaZZMLF0Cg9iBtxRzKp4RwyI-8qCB2MbEiyl4gyC4kSuN8C5hgG3otp4q0-Ps-LMvT7Y32ev2U6rXFoIFKhm96dwTQ2TGXQkFtSl8NmRrYuRzXNLv8gWqai5Z6eNBH26yinK_doCdgAtlfOsps2MJXni7L-HCyCpmMY-sUPv1V-EHUw7S2FvANITb7rfrhqnwd6xyLcGo6GF8IhthDrrwnC-BukI9cPfEDXr7zuybpReZLN7UvQi66UMrBwKMkH_fP1T3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f381241a7d.mp4?token=VBoG_oswABEQoUZVj3PS52RzrcsdAg2oft9_p07q5WX4t47Klt9Lf9sQzheyUShP7b7KtV-HBpvInvuvcPt23dX3lsaREZ3i-KwIP34xu9r2Uw2aW8UYB3zmNEM0bgHhShfLLgF5R6s13Zmo40ZIwxy-PRYbMGil1Ks2jj5hGF2-3GppW-KrFIh1nSPXoFrJl4GOFz78-8sy9heqEngVmSvvi1urmSYpUNKMxdgD3qrXbxuX1zjy0Kz-uiMnhI-tH0kokCHM-a8goWaU9n01KHSqbz9Dy8pZczGuTkC2iVLvdznTmrt2D1_nVXyvFoWCZJ1jMatjcE6c_Ge2APemB4CucxWYGbK_KXK3RvDeu-ljVH0BE9pD9rUtB9kXbIbpYq2NOegBSX1mWIlLM01DM8htI2CY-etE7ZuPKWaZZMLF0Cg9iBtxRzKp4RwyI-8qCB2MbEiyl4gyC4kSuN8C5hgG3otp4q0-Ps-LMvT7Y32ev2U6rXFoIFKhm96dwTQ2TGXQkFtSl8NmRrYuRzXNLv8gWqai5Z6eNBH26yinK_doCdgAtlfOsps2MJXni7L-HCyCpmMY-sUPv1V-EHUw7S2FvANITb7rfrhqnwd6xyLcGo6GF8IhthDrrwnC-BukI9cPfEDXr7zuybpReZLN7UvQi66UMrBwKMkH_fP1T3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراضات دانش‌آموزان مسلمان و والدین آنها مبنی بر ممنوعیت ورود دانش‌آموزان با پوشش اسلامی به مدارس در آذربایجان
🔹
بیش از ۹۵ درصد از جمعیت آذربایجان را مسلمانان تشکیل می‌دهند و معلوم نیست علیف به چه علت این تصمیم را عملی کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/697783" target="_blank">📅 18:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697782">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23fac10c5d.mp4?token=T7PmIlEdL63paLU59CC9T2Ga-O5zAyafLjom-TEiODL4eFtTgZx_JKx_hqtRZ_U8OYepBpMRRhx-RSWtRtvve9Ja9IbiEH2RdJS7ttdFQ2Yve33BEjNzqafXHrOhusZcYinOHt_MRJGPSb7SXWQgxrdemTN_PFvt6FxuJnNfy5GHBmI_jIRDX9PMzUtBzZI54MXuK8bVvciqHkMHLhz5EwruRJf3wpsQyUpPF_5cSHeOmqJuoio5OdpgGxo05nz7PSs27YsbmMlgwIZKLVW2p-xTGa_Zh-gLO3TcP2qSYsDVRGgjON1y0_E3ekrCiYT34PuXPfC-YwheAcTw3xWt4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23fac10c5d.mp4?token=T7PmIlEdL63paLU59CC9T2Ga-O5zAyafLjom-TEiODL4eFtTgZx_JKx_hqtRZ_U8OYepBpMRRhx-RSWtRtvve9Ja9IbiEH2RdJS7ttdFQ2Yve33BEjNzqafXHrOhusZcYinOHt_MRJGPSb7SXWQgxrdemTN_PFvt6FxuJnNfy5GHBmI_jIRDX9PMzUtBzZI54MXuK8bVvciqHkMHLhz5EwruRJf3wpsQyUpPF_5cSHeOmqJuoio5OdpgGxo05nz7PSs27YsbmMlgwIZKLVW2p-xTGa_Zh-gLO3TcP2qSYsDVRGgjON1y0_E3ekrCiYT34PuXPfC-YwheAcTw3xWt4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با چند تا مواد ساده خرما رو به طعمی بی‌نظیر و مقوی تبدیل کن
😋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/697782" target="_blank">📅 18:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697781">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0167075157.mp4?token=bs1oEaP2mFWweALFQOGradKJFqQk8temkKuddsDjiMNBKu_qoWKIW7QHk1yzGOYkdvalMdMzPN4YagMpU4E-asorLjN52qBP0Ua1PQ_QTKA0j5yZVbHMqZEJ5mVeenwWhZMRwbWZ15xnHpPI3mY2OsSGBKbKQeDcfq1ze8mR9SkK77jWhEMZn92qYXavoy7Lr1LhuMBULt09OdRebzNKBb5YJO-_46UO3oxMgSO8vmM1u3NWAVCLHIYj59eyr6Bo2Ezo4UbwHm951eZZu9b1G8Mq3Yvj_fLYZqUhs382fxWc5rM9eOlQD7V27GA3Gk4qHxjHA49S8to5cQCCz8tcng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0167075157.mp4?token=bs1oEaP2mFWweALFQOGradKJFqQk8temkKuddsDjiMNBKu_qoWKIW7QHk1yzGOYkdvalMdMzPN4YagMpU4E-asorLjN52qBP0Ua1PQ_QTKA0j5yZVbHMqZEJ5mVeenwWhZMRwbWZ15xnHpPI3mY2OsSGBKbKQeDcfq1ze8mR9SkK77jWhEMZn92qYXavoy7Lr1LhuMBULt09OdRebzNKBb5YJO-_46UO3oxMgSO8vmM1u3NWAVCLHIYj59eyr6Bo2Ezo4UbwHm951eZZu9b1G8Mq3Yvj_fLYZqUhs382fxWc5rM9eOlQD7V27GA3Gk4qHxjHA49S8to5cQCCz8tcng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخست وزیر انگلیس: همچنان کنار عربستان سعودی برابر حوثی‌ها خواهیم ایستاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/697781" target="_blank">📅 18:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697780">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ادعای جدید ترامپ: به نظر می‌رسد ایران در حادثه فرفورد دخیل بوده است
🔹
ترامپ: ممکن است از اروپایی‌ها بخواهم ذخایر اضطراری گازوئیل خود را آزاد کنند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/697780" target="_blank">📅 18:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697778">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
رویترز: انگلیس دو تبعه ایرانی که با دولت ایران در ارتباط بودند به لیست تحریم‌های خود افزوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/697778" target="_blank">📅 18:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697777">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcf4f85208.mp4?token=OdUDxuobA-FmA56BwU0wSVhNvadQMeEF0YdKXdPPalV5tA0xnklJFbeakH7jGCczmqoHIEnbYJIsbX35YM52HP2KL6JQvcHIbNsMm9IyH6zjR6fVuFAMpHJSUJZESSkjuyOeA-ruSwVPPgYDAVFimuT3Cn44tZgY-f0KDIQQ521Hv11kJ1CEyHMZ8EGNIZhe58QNth968YLOSA0T4kF_zIgImruzXSCowt1S2_ZkwYu-fArOTMjKN2IUib0yu4G7kdtAN74KX7QlFM6ziYZEESZbIU_3wtI9cLtL6cpcq2F_MiWFvLe94dowlkm1w8Fxv_cOVCm839iJAMDnnHLA5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcf4f85208.mp4?token=OdUDxuobA-FmA56BwU0wSVhNvadQMeEF0YdKXdPPalV5tA0xnklJFbeakH7jGCczmqoHIEnbYJIsbX35YM52HP2KL6JQvcHIbNsMm9IyH6zjR6fVuFAMpHJSUJZESSkjuyOeA-ruSwVPPgYDAVFimuT3Cn44tZgY-f0KDIQQ521Hv11kJ1CEyHMZ8EGNIZhe58QNth968YLOSA0T4kF_zIgImruzXSCowt1S2_ZkwYu-fArOTMjKN2IUib0yu4G7kdtAN74KX7QlFM6ziYZEESZbIU_3wtI9cLtL6cpcq2F_MiWFvLe94dowlkm1w8Fxv_cOVCm839iJAMDnnHLA5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصور کنید سیاره‌ای بزرگتر از زمین که هیچ خشکی‌ای ندارد؛ فقط اقیانوسی بی‌پایان از یک قطب تا قطب دیگر! این جهان شگفت‌انگیز TOI-1452 b نام دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/697777" target="_blank">📅 18:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697775">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
معاریو: برآورد نهادهای امنیتی اسرائیل نشان می‌دهد اگر ایران اکنون [به اسرائیل] حمله نکند، رویارویی به بعد از انتخابات موکول خواهد شد
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/697775" target="_blank">📅 18:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697774">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fz_mrWAIoKhBL7_Cr2bEV08hNEKwxp6j4OWPa3_m2GOu7Q4EKIiObouUaTo2QZlOp-z7WPKGB9ob7MOlhwA30GfLbtn9P2-Ju3-I6Quf-I6odAylfQm2YWxT6bJ7_F7zvsyZDIQFMaAY7ITXO0cZ6Ql8OPLkq-2TUNn3F8ACQ4B8Oz099si6tJ9CXM9cxdRV73q_XP7QYKQNHamFuTyFlThgbfcWQtJUjcj-862mZzBKGAYNkHPllzUGCiXN3hPrIk4S3Jw-xqpsYUl5e1wSUsgDTI6_zATDWpL206dQImBfddiLzA4XxRwRYZc483XCbEBBHSMZF9iGw2FB_v-rDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
تندیس مشک حضرت عباس (ع)
به یاد حضرت عباس (ع) باش؛ همان علمداری که در سخت‌ترین لحظه‌ها، تکیه‌گاه دل‌های بی‌پناه بود.
این تندیس، یادآور وفاداری و سقاییِ بزرگی‌ست که هر بار نگاهش می‌کنی، دلت را به امیدِ یاری و دستگیری گره می‌زند.
✨
مشخصات محصول:
▫️
ابعاد: ۲۲.۵ × ۸ × ۶.۵ سانتی‌متر
▫️
وزن: ۶۷۰ گرم
▫️
متریال: پلی‌استر
▫️
طرح: مشک حضرت عباس (ع)
▫️
کاربرد: مناسب دکور مذهبی، هدیه معنوی و یادگاری ارزشمند
💰
قیمت: ۲ میلیون و ۳۹۱ هزارتومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/697774" target="_blank">📅 18:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697773">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6521f24038.mp4?token=PT4viiCCFL7lnpo1IVHMnssCRFaWOD6xmGnGvXwIf6qPGaXzaQsuDXnkg6zidJmCMD3jY-FXWhfJCLfxtSWUOj_canlmwuPKIPrT8__WvvQD4R6ge4QvINguJOT_6q5ZqP0_TQ8qXe9DpG5C7Nw-bEkwmD_iqGAVuOfh6Po9ZQOx7tHreFbUTw0iioS3LTuJsZf0LN1tZKvDqdZJbo-44eWwccIa5gGPS_e5Vs5wta-zUN3r_jDQf21LQMbZ0sVl3ywjPlrz1PmARtlIzkfk955BPy8bjNJ6hOPb5oq_oiIDWPTZ5TdBOtet1GJ87JQ2V3RsxTcctShRYZcFq8vFA4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6521f24038.mp4?token=PT4viiCCFL7lnpo1IVHMnssCRFaWOD6xmGnGvXwIf6qPGaXzaQsuDXnkg6zidJmCMD3jY-FXWhfJCLfxtSWUOj_canlmwuPKIPrT8__WvvQD4R6ge4QvINguJOT_6q5ZqP0_TQ8qXe9DpG5C7Nw-bEkwmD_iqGAVuOfh6Po9ZQOx7tHreFbUTw0iioS3LTuJsZf0LN1tZKvDqdZJbo-44eWwccIa5gGPS_e5Vs5wta-zUN3r_jDQf21LQMbZ0sVl3ywjPlrz1PmARtlIzkfk955BPy8bjNJ6hOPb5oq_oiIDWPTZ5TdBOtet1GJ87JQ2V3RsxTcctShRYZcFq8vFA4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از خم شدن تا دست زدن، همه افعال حرکات بدن رو به انگلیسی یاد بگیر #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/697773" target="_blank">📅 18:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697772">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
فرودگاه ریاض به مدت ۵ روز ( تا ۱۷ اکتبر) تعطیل شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/697772" target="_blank">📅 17:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697771">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbnncOiPoEToF4TzBPdTD6XMuokHBuka4_kTeY8cuMik8V5KaJFohGVQcyBnoU_kMZ8MSok3RjlLIt_TKZtrkZQqnvOrS3_uxZz-tlz30ZJaQSBJJqve_UyLxWrDJ197bvoMFJkdbj8U4MOWqXtIQcHZYEOQbXCpoLHHqlk6ecKUcb-40mDApK3xAK7kzyRI-VrGfl3YbydGLLVUY02HtsJNlu_YE0ScM74Coy1Y5PrRof62eG5mKhaAy7es6sLpr21jH3Xy2ADxT7pmmYRq8jlRNUlxBHAKr1_dQUp0vR7UvY86ztip0SJZfpqHHe3cok1e7uZUdxCN-TdpFJE2dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن‌پست هم بسنت را به سخره گرفت: پس از وعده نتایج سریع؛ ترامپ برای جنگ اقتصادی طولانی با ایران آماده می‌شود
واشنگتن‌پست:
🔹
بسنت، وزیر خزانه‌داری آمریکا، وعده داده بود همه خطوط هوایی ایران تا پایان سپتامبر زمین‌گیر شوند و ایران تا پایان این هفته نفتی برای فروش نداشته باشد، اما این وعده‌ها تاکنون محقق نشده است. پروازهای بین‌المللی ایران ادامه دارد و تهران همچنان نفت می‌فروشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/697771" target="_blank">📅 17:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697770">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
هواپیمایی هند از ادامه لغو پروازها به مقصد ریاض تا ۱۵ اکتبر خبر داد
🔹
همچنین هواپیمایی بحرین از لغو پروازها به مقصد ریاض تا ۱۷ اکتبر خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/697770" target="_blank">📅 17:54 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697769">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
گروکشی بر سر حریم خصوصی کاربران؟ محدودیت بانکی برای پنج پلتفرم رمزارزی
🔹
بانک مرکزی امروز در نامه‌ای به بانک‌ها، خواستار محدودشدن خدمات بانکی پنج پلتفرم رمزارزی شده است؛ تصمیمی که می‌تواند تسویه‌های ریالی و انتقال وجه به حساب بانکی کاربران را با مشکل جدی مواجه کند.
🔹
اما ماجرا ظاهرا فقط یک محدودیت بانکی نیست. بر اساس شنیده‌های مطرح‌ شده در محافل رسانه‌ای، بخشی از اختلاف به درخواست دسترسی به اطلاعات کاربران مربوط می‌شود. گفته می‌شود پلتفرم‌ها خواسته‌اند پیش از ارائه اطلاعات، مشخص شود دقیقا چه داده‌هایی، برای چه هدفی و در اختیار چه کسانی قرار می‌گیرد و چه نهادی مسئول حفاظت از آن‌ها خواهد بود.
🔹
حالا سؤال اینجاست که چه کسانی به دنبال دسترسی به اطلاعات شخصی و مالی مردم هستند و چه تضمینی برای حفظ محرمانگی این اطلاعات وجود دارد؟
🔹
مگر حفظ حریم خصوصی و دسترسی به پول، از حقوق اولیه شهروندان نیست؟ چرا مردم باید به خاطر اختلاف بر سر اطلاعاتشان، برای برداشت پول خود معطل بمانند؟/ بامدادنو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/697769" target="_blank">📅 17:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697768">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
استقبال لگویی ها از جدیدترین زیرگذر اتوبان اصفهان!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/697768" target="_blank">📅 17:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697767">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
فرمانده ناتو: در صورت حمله روسیه آماده نبردیم/ در صورت حمله از سوی روسیه آماده‌ایم همین امشب وارد جنگ شویم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/697767" target="_blank">📅 17:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697766">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daf2238e41.mp4?token=bUKhzFYDbmBEtart-5AdIzvR_zY07kMKBDZZxJ_jNmXTFTPbJ7S9eVW2gpCYT9hy0lCrd86xM541aNBfaSLf3u72N9o8FGyctiTwAAFewEjoYQEgEreMfJojaO338DuqSGASn0dzY_PClNuKjWbep-eXeQ-v7G9XDFY9anKfcXHcW5LhKiw7pqMtSLMfoqokkKxkem63YiC2bk4r-Z45MdLtANRH3WzDuo9KDvZXCinUCvSKyxz4AjIdhrTcOj9i_V2aLqrfevcrRHWMltiz9nzHthnPz9Qu-Kp0SmTy4UAf9I_6jMFSvlHCKOzCK5AhHM1Jewyz5yX8J40bwC3ejQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daf2238e41.mp4?token=bUKhzFYDbmBEtart-5AdIzvR_zY07kMKBDZZxJ_jNmXTFTPbJ7S9eVW2gpCYT9hy0lCrd86xM541aNBfaSLf3u72N9o8FGyctiTwAAFewEjoYQEgEreMfJojaO338DuqSGASn0dzY_PClNuKjWbep-eXeQ-v7G9XDFY9anKfcXHcW5LhKiw7pqMtSLMfoqokkKxkem63YiC2bk4r-Z45MdLtANRH3WzDuo9KDvZXCinUCvSKyxz4AjIdhrTcOj9i_V2aLqrfevcrRHWMltiz9nzHthnPz9Qu-Kp0SmTy4UAf9I_6jMFSvlHCKOzCK5AhHM1Jewyz5yX8J40bwC3ejQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفندهای ساده برای از بین بردن بوی بد غذاهای گوشتی
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/697766" target="_blank">📅 17:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697765">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a75bb2600.mp4?token=nEOnq5Witax1inzutjS7r4x21VElKW9k4Al9JaHZpZRBOHSVyVi5BglVX6Ptnw7EPdGtfQHX4wTi24KZM0fuGPjbKw8iDVnL8rwM_lrZr-LoFzmiRcdEGBeCTt8cRIHJeUZ9Tyni5D9Aevf7D2mibddYRRhf46pr48Fw9e2Yi0z4LAR48bt3OAbeLbQunOPGsWqDzKIkiK2gBJUImkLmQJLuMyg20yZQzK-BBrqipswC1yj4yQKsnY_85Cj_igHR0PRF-CuhcXy-HQGwMATrQtETfZ0kRsnwlwxDnXo-l_BBo88i6rsb05RozmBttCIoMhHIBo2nHAbcVnE0olHcJzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a75bb2600.mp4?token=nEOnq5Witax1inzutjS7r4x21VElKW9k4Al9JaHZpZRBOHSVyVi5BglVX6Ptnw7EPdGtfQHX4wTi24KZM0fuGPjbKw8iDVnL8rwM_lrZr-LoFzmiRcdEGBeCTt8cRIHJeUZ9Tyni5D9Aevf7D2mibddYRRhf46pr48Fw9e2Yi0z4LAR48bt3OAbeLbQunOPGsWqDzKIkiK2gBJUImkLmQJLuMyg20yZQzK-BBrqipswC1yj4yQKsnY_85Cj_igHR0PRF-CuhcXy-HQGwMATrQtETfZ0kRsnwlwxDnXo-l_BBo88i6rsb05RozmBttCIoMhHIBo2nHAbcVnE0olHcJzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دارو هست، اما ...
🔹
سبدفروشی دارو طبق گزارش‌های مطرح‌ شده، با وجود شرایط دشوار تأمین دارو همچنان ادامه داره... پس نظارت این وسط کجاست؟
🔹
جزئیات را در این گزارش ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/697765" target="_blank">📅 17:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697764">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25fa87ee98.mp4?token=Iq2UX26R6AKMVTcdrzZ_i9lhF9ts0IIiXuI6Dqp2FkkPmqvig7x9k168E229M2fi0is294ZIO5AyjioqnS4AsOZC6UpFRoJus5ny5wmXyF87Y9S5O4SjltpAalU6--9uzRlDvRF16Tf3oNbhLATRxAU43NdwYucXDUnAdSrVyCyYwsyX4ViQNGVbk0SNFBhweCON_nYoUY2fhnuS90wxWiCCJsrj2hG9R8PTGjd9h5c7YGGV3FyMnJ-jUirjt9GISY3T7fh_fRhJN7vnKF3PoIbfJiqw0epyONYe5WN9ghVQ_3WrvDHmJvgQHbfMJlwRC2RVSrZj1ttNAGXijJqv1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25fa87ee98.mp4?token=Iq2UX26R6AKMVTcdrzZ_i9lhF9ts0IIiXuI6Dqp2FkkPmqvig7x9k168E229M2fi0is294ZIO5AyjioqnS4AsOZC6UpFRoJus5ny5wmXyF87Y9S5O4SjltpAalU6--9uzRlDvRF16Tf3oNbhLATRxAU43NdwYucXDUnAdSrVyCyYwsyX4ViQNGVbk0SNFBhweCON_nYoUY2fhnuS90wxWiCCJsrj2hG9R8PTGjd9h5c7YGGV3FyMnJ-jUirjt9GISY3T7fh_fRhJN7vnKF3PoIbfJiqw0epyONYe5WN9ghVQ_3WrvDHmJvgQHbfMJlwRC2RVSrZj1ttNAGXijJqv1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جلیلی: اختلافات، ولو موجه، نباید موجب برهم خوردن وحدت شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/697764" target="_blank">📅 17:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697763">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cw4GliwVcCtp86m5V--Z1gZXP_Y3C4mvBdbO5GuS2kJQwn3bDmC3pP0eTYP29XfyllOHxk5ZMs5wZmHbEk6VEhbFg-0l7UIgpA47HltxWPTvs595wGWXo0fDcoolugpioqKHToH9RbClMCoybUT_TfkXlKR7haL_k5mdcv0-UrwvybzJ20B71c2Rujh4AqHVZYUAEBnDUuOVxT6nTMvaFu8_POH5vpF4u8-ywzzMdBqGYRX4nBoYRcBZGvotzh6BETug7oUhay0L7ZDyttLcWq-Acqsvd8n28wBZ_Me5wHNoDmK6nDG2Wy8jo_fFDxuKt5of2IQYegxWQCLNKprUEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سهام بزرگ‌ترین مجری پروژه‌های فولادی و زیرساختی کشور عرضه اولیه می‌شود: «فکور» در بورس
🔹
فردا، ۲۱ مهرماه، سهام شرکت مهندسی فکور صنعت تهران با نماد «فکور» برای نخستین‌بار در بازار سرمایه عرضه می‌شود.
🔹
نکته قابل‌توجه عرضه اولیه فکور، ارزش‌گذاری سهام آن است!
🔹
قیمت پایه هر سهم بر اساس ارزش‌گذاری خرداد ۱۴۰۵، تنها ۳۵۴ تومان تعیین شده؛ آن هم با دلار ۱۹۰ هزار تومانی در روش‌های درآمدی و دلار ۱۲۰ هزار تومانی در روش NAV
🔹
اگر عرضه‌های اولیه رو دنبال می‌کنید، جای فکور در پورتفوی شما خالی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/697763" target="_blank">📅 17:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697760">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a9e2cbd701.mp4?token=us_5jmwVXwzpb8TtRCPTtju-A6Z-OFOYIxhQRszVz_wbaiFRoNtztHacZpEAXoPpra9kDe-GKBMrT17anw2AmVJEmDiOwSpBubq6M4NZC9LNq9bejSjLDSgPM2TcMhb7-x21sNzDcScXdMYPBo2XHAz5h0H2MLC5l3X-5BbPlx7_-Cafr9Rd57oX22mLjBYjR6XMkPuRgLkJkyf1YLa0tketFT5ORRhdAsBbnMmf_LxxJbIrxjdiOgErBESXsMq-38WIS5pjQgDtafusieEIK6H2QdAqzUD4g4RACx0dDBfnV0FV5-p5K-OMsvFd_h5SbNoYalaozkeQe-vm81W0lg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a9e2cbd701.mp4?token=us_5jmwVXwzpb8TtRCPTtju-A6Z-OFOYIxhQRszVz_wbaiFRoNtztHacZpEAXoPpra9kDe-GKBMrT17anw2AmVJEmDiOwSpBubq6M4NZC9LNq9bejSjLDSgPM2TcMhb7-x21sNzDcScXdMYPBo2XHAz5h0H2MLC5l3X-5BbPlx7_-Cafr9Rd57oX22mLjBYjR6XMkPuRgLkJkyf1YLa0tketFT5ORRhdAsBbnMmf_LxxJbIrxjdiOgErBESXsMq-38WIS5pjQgDtafusieEIK6H2QdAqzUD4g4RACx0dDBfnV0FV5-p5K-OMsvFd_h5SbNoYalaozkeQe-vm81W0lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراضات دانش‌آموزان اسرائیلی‌ به دولت نتانیاهو در تل‌آویو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/697760" target="_blank">📅 17:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697759">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
اروپا ۱۶۰۰ مورد تحریمی جدید علیه روسیه تصویب کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/697759" target="_blank">📅 17:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697758">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سوره مبارکه جن/ ج۱</div>
  <div class="tg-doc-extra">آیت الله جوادی آملی</div>
</div>
<a href="https://t.me/akhbarefori/697758" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره مبارکه جن| جلسه اول
🔹
(00:00) چرا این سوره به نام «سوره جن» معروف شده؟
🔹
(5:00) جن‌ها از نگاه قرآن چگونه معرفی شده‌اند؟
🔹
(12:00) آیا جن‌ها هم مثل انسان‌ها تکلیف و مسئولیت دارند؟
🔹
(19:00) جن‌ها چگونه با قرآن آشنا شدند و  بعد از شنیدن قرآن چه واکنشی نشان دادند؟
🔹
(31:00)پیام اصلی این بخش درباره هدایت الهی چیست؟
#تفسیر_سوره_جن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/697758" target="_blank">📅 17:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697757">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e62b3d1f2.mp4?token=fZ-5PiY2pMQdGsVKWeMhUIil_r1KZarGRJ-6C335HJSxxmzQbOzXAPeExnkjAeYpYS5cPUrQ83LrnPRbOyxsYIX3UHOg2866pmpovSBDLOhooTOpN0HAzn_HiDty0_ABC37Fvsfk_we9KEM6gTPIYudwDtcHgFEMnyoQib7fwvNuM2058NvD7sMzm8T2c2oZdbSQBU7ZDT6DHPhVYu9b1zZOBiZ5JM5Qxki4Lly4laqJmNqv9Dpa8VOf7LP8MZvjKp_SwpVuvCYA1TE-rs8wQiwUp6IuVXmGRFHwKmRgQvkTBZ7D52UqF0sJ1MZcIQFMe-V0yRd97katMDcGlZ0yhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e62b3d1f2.mp4?token=fZ-5PiY2pMQdGsVKWeMhUIil_r1KZarGRJ-6C335HJSxxmzQbOzXAPeExnkjAeYpYS5cPUrQ83LrnPRbOyxsYIX3UHOg2866pmpovSBDLOhooTOpN0HAzn_HiDty0_ABC37Fvsfk_we9KEM6gTPIYudwDtcHgFEMnyoQib7fwvNuM2058NvD7sMzm8T2c2oZdbSQBU7ZDT6DHPhVYu9b1zZOBiZ5JM5Qxki4Lly4laqJmNqv9Dpa8VOf7LP8MZvjKp_SwpVuvCYA1TE-rs8wQiwUp6IuVXmGRFHwKmRgQvkTBZ7D52UqF0sJ1MZcIQFMe-V0yRd97katMDcGlZ0yhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروی دریایی سپاه: سومین نفتکش سوپر تانکر در تنگۀ هرمز مورد اصابت قرار گرفت
روابط عمومی نیروی دریایی سپاه:
🔹
صبح امروز سومین نفتکش متخلف از نوع سوپر تانکر در تنگه هرمز مورد اصابت قرار گرفت و دچار آتش سوزی شد.
🔹
این نفتکش با خاموش نمودن سیستم ناوبری خود و با بی توجهی به هشدارهای نیروی دریایی سپاه، مانند متخلفین قبلی قصد خروج از تنگه هرمز و مختل کردن نظم و امنیت آن را داشت که مورد اصابت قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/697757" target="_blank">📅 17:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697756">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ایرفرانس حضور برخی خدمه در پروازهای تل‌آویو را محدود کرد
🔹
این محدودیت شامل اتباع ۳۱ کشور از جمله الجزایر، تونس، موریتانی، عربستان، لبنان، پاکستان و اندونزی می‌شود و اتهاماتی را درباره تبعیض بر اساس تابعیت و خاستگاه ملی به دنبال داشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/697756" target="_blank">📅 17:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697755">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فروشگاه و رستوران خود را با هیوا سیستم هوشمند مدیریت کنید
از صندوق فروش و بارکدخوان تا ترازوی دیجیتال و گزارش‌گیری لحظه‌ای فروش؛ راهکاری جامع از نرم‌افزار و سخت‌افزار فروشگاهی، برای مدیریتی دقیق و حرفه‌ای.
📞
۰۵۱ ۳۶۱۴ ۲۲۱۲
📞
۰۹۰۲ ۴۲۹ ۳۳۲۲
🌐
hivasys.com
📍
مشهد، چهارراه ورزش، مجتمع ایلیا، طبقه اول، واحد ۱۳۸
مشاوره رایگان تجهیز فروشگاه و رستوران</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/697755" target="_blank">📅 17:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697754">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
کویت و ترکیه هم به جمع کشورهایی پیوستند که پرواز هواپیماها را به ریاض متوقف کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/697754" target="_blank">📅 17:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697753">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83038e5d9d.mp4?token=dU1VTd1wb6zJ-IM3tFrtY-wHWQnbqdxx_IckOhUvMpD9qRxjtEXqmM2KTyHvgST884eZVK9PxVvIBoW2zgpEGSaQAoeOwawZmZN8PdgGzE_bw8rqB5CGAxE5jv5lNe0WQdU0uEjvMEhv7S7d2fjqSChRoeUXpHAttuvkgqkz742rmj3szRZHrr8sO568Nl5hb9jSYGIZasuAPC_jz_wtw8EUMX6pJenue4UIcv2PX9v39WFbDvRhnZWT4rZQH_HhDSLhn_XZW15cgBb_6oKPN7WntsPO9DbZ08XFOlDJCquhuK3UJHjzqkTV1HDCJE27eIINKBjPUnY5wDMpEjkiTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83038e5d9d.mp4?token=dU1VTd1wb6zJ-IM3tFrtY-wHWQnbqdxx_IckOhUvMpD9qRxjtEXqmM2KTyHvgST884eZVK9PxVvIBoW2zgpEGSaQAoeOwawZmZN8PdgGzE_bw8rqB5CGAxE5jv5lNe0WQdU0uEjvMEhv7S7d2fjqSChRoeUXpHAttuvkgqkz742rmj3szRZHrr8sO568Nl5hb9jSYGIZasuAPC_jz_wtw8EUMX6pJenue4UIcv2PX9v39WFbDvRhnZWT4rZQH_HhDSLhn_XZW15cgBb_6oKPN7WntsPO9DbZ08XFOlDJCquhuK3UJHjzqkTV1HDCJE27eIINKBjPUnY5wDMpEjkiTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های صهیونیستی: ارتش اسرائیل در حال بررسی این احتمال است که انفجار ناشی از موشک حزب‌الله باشد که در جریان جنگ شلیک شده و تا امروز کشف نشده بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/697753" target="_blank">📅 17:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697751">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vB2b3qdKibFp_qtWmQi1wj1IlWvf_V9h4VtNf00LqO08YAWt--vkZv0MBVS8B7X56m6JsGaZ2vLh7KNhU-IMHdcQ2x5eWlPbkq_tssHFhenD-Yt4kxmV4FE-jNq4DMWXg91oBFXRcyBwF09_rcRzQYtP2dXmuWKcpMq2vMrXZVckHsRTWIbV1FAEBS672KQ-XZQW-NCpQ7pwoWEByvAopn_x-YRn7gltpS2fRB4in2mQ2JLcdBBC93ERlYG7apx2zOGFR5IIE2qrkUWiIyxray8Bo07qxFg85Acmcr2QdT0Brdn6xYPmYErW1pakkBy-X51FHkjYRnYkzO7zBMQgZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2GoEEjPYnQAAjFc5XcTGhOoRPggMX54pVIygFqlnE-N-x6RB4DM_lHuF2kgkc5Nj_PqB7KYpDt3xSL_ixBoFDmjBVpbfie1AVjhqCZuhUQB3NG2KJf8mXFAbj1syTirNpp8fUHLIkMMvc0l3smnnAwZ-FFiXqGFL2Eau6zfL4yDI9qZ16SSAKF4I-p7KnWWCrjOo_-zf47pLQSsJrGUhj_JNPPyQPmA4GKDzs5QWGkGCdSS_oufhReGjjskuHXIOZUG-a6XmHPZe7_jWFiZTR2w4ZbctTo4XC7T4J0h6eOneb0WCROr0AKinZTleNVMQzeGmRG_aKRUdLQZCVoMXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
صورت‌حساب تحریم برای روبل؛ بازخوانی یک تجربه تاریخی برای ایران
🔹
نمودار نرخ روبل به دلار نشان می‌دهد از اسفند ۱۳۹۲ تاکنون روبل ۵۷ درصد ارزش خود را در برابر دلار از دست داده و بازار ارز این کشور سه قله اصلی را تجربه کرده که هر سه با موج جدید تحریم‌ها و کاهش درآمدهای نفتی همراه بوده است.
🔹
در قله اول (۲۰۱۴) خالص خروج سرمایه به رکورد ۱۵۱.۵ میلیارد دلار رسید و ارزش دلاری صادرات نفت خام از ۴۲ به ۲۳ میلیارد دلار کاهش یافت؛ در نتیجه تولید ناخالص داخلی ۲.۴ درصد افت کرد و نرخ دلار از ۳۵ به ۶۳ روبل جهش کرد.
🔹
در قله دوم (۲۰۲۲) غرب، دارایی‌های بانک مرکزی روسیه را مسدود کرد و نرخ دلار در ۲۸ فوریه به ۱۱۹.۵ روبل رسید.
🔹
در قله سوم (۲۰۲۳) با تحریم نفتی اتحادیه‌ اروپا و اجرای سقف قیمت نفت روسیه، نرخ دلار دوباره به بالای ۱۰۰ روبل رسید.
🔹
بانک مرکزی روسیه در این تجربه‌ها با ترکیبی از سیاست‌ها مقابله کرد: افزایش نرخ بهره، کاهش سهم دلار در ذخایر و افزایش سهم طلا، کاهش بدهی خارجی، تقویت صندوق رفاه ملی، الزام صادرکنندگان به تبدیل ۸۰ درصد درآمد ارزی به روبل و ممنوعیت انتقال ارز به خارج برای شهروندان؛ اما اثر همه این سیاست‌ها موقتی بود و بعد از مدتی نرخ دلار دوباره به سطوح قبلی بازگشت.
🔹
تجربه یک دهه نوسانات ارزی در روسیه نشان می‌دهد سیاست اقتصادی هزینه‌ی تحریم را حذف نمی‌کند؛ فقط شکل و زمان پرداخت آن را تعیین می‌کند: گاهی با تورم و رکود و گاهی با نرخ بهره‌ بالا و کسری بودجه.
🔹
اکنون که ایران با شرایط جنگی و محاصره غیرقانونی آمریکا روبه‌روست، بازخوانی این تجربه تاریخی می‌تواند به فهم بهتر شرایط اقتصاد ایران برای بازیگران اقتصادی و سیاست‌گذاران کمک کند./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/697751" target="_blank">📅 17:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697750">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDN_jnFykPelLHp8RqcdAvGGgLTTpZSCHOC-Hgr0jn3r3z2jrTwq0nsnPH_l57Lf8jpUzeJV6RgPCHrDJXrY_OAWTcTCQUB-Vub4qLCFFjxfIq57hSQ382PQZjdeWKsXbIT4X9wVRNVq3oUiS0654B6v_gAQddQipHfE3tAErjDa0wY6V7tvIfc4tNFwqTkvnEleQTSboqW99gQBv-pmy-tgH_I33ye0ctkoVe4SrUyPPnGa0eBjg8l7HPf_fvrEetIIc4Ty-SwjkiF5boJ0urRh2iTZdPvMbzzNyal1bNcuzru-1P2McNb_ORmrgxU1Z09lnftEtiMc8ir9D-Qaag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این مرد احتمالا جانشین نتانیاهو می‌شود/ آیزنکوت بعد از پیروزی احتمالی به ایران حمله می‌کند؟
🔹
اگر آیزنکوت پیروز شود، احتمالاً شاهد تداوم سیاست‌های خصمانه اسرائیل در قبال ایران خواهیم بود؛ چه از طریق عملیات مخفی موساد، چه از طریق تلاش برای تشکیل ائتلاف منطقه‌ای ضدایرانی. اما رویکرد او احتمالاً روش‌مندتر، محتاطانه‌تر و بیشتر مبتنی بر دیپلماسی پشت‌پرده با واشنگتن خواهد بود، نه اغراق‌های علنی و یک‌جانبه‌گرایانه نتانیاهو.
گزارش تحلیلی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3251903</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/697750" target="_blank">📅 16:58 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697749">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNoifL-uhKShXPw5cVuF8Nup8fWzjr9wwLmEd911xrE_hNJ8Oa_lwDTsP-VNlDsN-R6j2NCBUCBQJV3_jvyncjZfT2XBCcnTFmsrbRuxOs85AzjoyjbEAIth_QOO-eQiLG6NNSLN5DHtVuU95zIMfaHaUYHm5hBV7F-MVWoUyPubvjUgpmYiIL60wYU1QRMuq4RhuotJ55APnNquve2m5XG0CHS_Dm6GHvbDojTxstWT-9JjdpgEzrScmQxDvvc4HOYaOeDtCm1j-ZkQ_WtdZjurGnHcPap6HXVk_ozl09M0YLlPcZ4ePE5yh7bnK9JhFsHCK9h_0WHAg76RKWEwcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر کشور به چه چیزی معروف است؟
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/697749" target="_blank">📅 16:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697748">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
اسرائیل هیوم: نتانیاهو پخش زنده در شبکه‌های اجتماعی پیرامون موضوع انتخابات را به دلیل حادثه رخ‌ داده در شمال اسرائیل، نیمه‌کاره رها کرد
🔹
بر اثر انفجار یک بمب در شمال اسرائیل بیش از ۲۰ معلم و دانش‌آموز به شدت مجروح شدند؛ هم‌چنین منابع اعلام کرده‌اند که دو…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/697748" target="_blank">📅 16:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697738">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M63IZAPVe2px6dp9V6BTdqgyLExt3Hu2yRKvk9tuf_5QookRZXHFAwKRuavr7Y8KLU60aP_YjjWa0Hm6ZhNZ285eJkJ_doFcNaKu_yYnkMjKhAQt687oPXYmuBpQNu4qPBFtNwRPiawrgnVvI9ALgnH_FBO8q7GISQAqACdgYSiC2xQh4wC1_T311635qlbmuBD11cJYY16AZdszzmwyKchd4_gFThtrt6xpPdliLFDKIdhkxgQcDvzyl_UMvwMCR_zxPNBXhVnufmHTocC8qiI-7XagEs2oKkvCWD8EgU12yLjKmKN-Gf0FK05opSrYk5bTEZ11bM_SsXSFh8i9ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cUZ4OF9mKKUtSib8tduf-91bBS93cYrEGB0RUYl6t3H95jMYH8stXwS0RHazfnOx00eBjLaFfJ1glsiARALOXX5QzqVQZ_tDhW-oMERG4Mg1Loksx3V7xMFJ3ftbL3xyKD_uNp3LUNBQ6rQWSeD_T77ZCcDI8bSS8v8vLkHKbzGI-K8RXLHkQLgHDDgq114bHqVotQjOkESVGErHLutbMq3QR7P8HOti7E8jHvxCO2KElvxP31jzrlbAgXWku7P_pWJ_9j8Wq8urq3B49Ts41UAoKI4N0jLaFZw9hgEyvDSuyNljeCaB7rsllDf0VMW2YFOBFpzIJ9ImSPX3Um1gMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bq_2hmzXM9-U3DrA26RcFaw7U0tWl5H1osY6qraluwF3qWzn4qJ-T3drQcnKWiMecFqFJApShIF3Chm0uHqJLv8yECHy8IcPwBqYhp1hJw1s8vibVCidLkGHAJjRM_Y4IMnIULm0sjNiWYUrKKjHVxHvw5BN1yM9pJaAuUtEwerF-ZOYGxQtRLg9vv8XjROKiECXLVei2_SCrGctsbiAPqZb4vy9TFNEhTZUtqWhC4q5bJCGNRceIZm4YYs7CeKEoUSONkh_cAtGc0jzWgnlcDgPrkvJu_8ls_ZPKtBjQCnpKP7btOBZmr0tdAhHYMWf2qGEBf8iZaNxWIVosNVVTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PjFbNqLm43s3Bz4pi1vYqLoTcKRvbbCjbrJWaj_V5y1l2kOfuIYsKqIK2xSp-0AUv9pwj34uB4ppERjvIwG68_YqlcGfGKivKE5odcCNBrBgGnN_ephCe0UGoRNudlu7Q6TRD-JfBmAqRWHQvLElXMR39XV0EjbcJx4pU9h9ukgidNcHS3E6GqFlLGouVgEVOMugo16IAiFlQzD4d_q1AhNnjAWcSygX_d44PeqyDNJqgptoPKWjRhKBXqRAH5NEFudQcWylraYRGVMfke17gebNsqUiEqv2nttZuUCXfKFuQxjMszR1dgxmDYgjm23hbUb7QqySOtDrp8xsjVamxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eDwkMx9lv0N7cUSiYZk0mr0-Iscl1VcMRZPWuy6VmkkAs2N_q_EFQyv4kIus9c7D7_Yl0ljAC6th6VMQNfF17FEegX0AHCHN8lWVLIqixdhaG3Nv_evtXF_ppkPZmm7wpI77gXW5EI4qy1XrqQf-DZyIExSeyLfldHHDTPWIXRSDMNyeQbATixIC9PFS_4INAZzKV6kBo5kV4Gw43SO_QrMME3KHqIV5nqxsKGKxQNpvtOvCk4FW-MCDzOrpd4Jfk1Pl-9UMlQBgG5S6EMC633GbAa4MbRjtyuO3a3QyiJ094cmEQeGlfu_EzhK4-mS-usc2UzYiDLeMxHiX3fWR7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LKThreGiOS8t4vLfVk0A-GqaGjAJ42qLq-TCqW58MXzEwuLYkdGU8K4CqGvDlHT8iNLgZH6LP9dbjmGIfRa2RInP989J-s8b4egqPyAf-k-_EwrRGasYnfX5f4C6la5wn0rrRyFJS7qXcs6-2Kh2nkcG7y8M94bscrpH2L39rst6l7SM4pTmRhfL1HbS3EcewUsl6_p6r7mKDYvfOLyb30jR81hfBiKAPZHn1Jl_WumXvpq4neTYP25wvuZBNkNlKNHjotQxjsYhKAIZ45lstH9y5Z83v_zKtp_P7d5eLqQtsg2TQI5nefEiBAvxTXU4XQHl7ro1G2K8Fl4ua4fyWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJfn8FSEO1dh2DBkcqE-Zw0o-d4_p2zv9RWiMcH1_htrsPRhk5x7omh1NKO3OpEYEqkX4cwuHnkui0PY6GVlEQ_QQpP8_Qw7zw7IBgCtn8MWJs_L5VvGDDkhoWZj_t0alNTKBGphsELV-g4_9RfEpPTg4KzY98oJ-UrPsiRedvgkj3nGcn2s_bevh8DeB_c3kV3Qwr7sBVgPIexBUqjmMlBVrBcAQdnGzIig9ykmDH8mIvECswjt6ygD4COKur97Pnzca7dX7Zo92AorO2RUeYu_eE33ZV6FjFPvW17vhZOlW9FEob0uGFsaKJwCft-kDFUFDRHFsWkzzMAsEqPA3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBXrL0ORP9A5h-J4ijTrA8wASYQ5k7_KDTl_zpia0gOHTUUPOCLoDMz-biFMwqDZnUx2a3-XbEgmHAZHGGilsgsRgQsRcmGvu3seRd2L6HRX5lgLgUz9cmHvMxzHi--4ANqcC4lpoyYzDAo0lS6bcYZfBt1AKLOvGw28PeX8aFxwaddni-11rstEdJ3a8ykl1y3bnm9CAncazu3BF_94D9QqU1uL3EkWZFSHHaaoudWj_EcUoJ6HYHaO3PAynBaBngOXVB8QehjZgc39wDSLvdXbmNnr0Nh5okAGZZj1JIkt-ktD7OdpqeenhjOFvU00U9NPxnMIwf5x8ndMy9Ld5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0KpJe3jULtPzjbriVdw4AtZ69Tfy3FVMP2WD9kfdAVtlgEFUWQuVAawsfjnm06SSLU6Wumx-q3yRZmIpLdZ-uhXiR2Y3CincWAnhE22PcnpdxUItv85WVQqMf69qNQX-F5RRcnNxxqq0f0ikHpqjercoe7qTSjI9UmIpfcQTiDXX8HK3UMlshlz176rzM990qfwbT35UPerHsUaoOPUH7Xz1wrrpQwnFGM1z_1MH1saIB5HSaRjp9wRrpCK8VFkfJyuxRM9FEfIjTfOtelB_g8ocL3mYQr5edB6prmaWYotQFGDh2e7bN6NPHLYqukvpPgCl8X4e4muA16misX-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DTv0Sql5v5cvx2EQhG-PQAOgXKsHSbKOmJT6wxjBrc8wc0HewVz3rNxUhdrcoWhajA7sqDQyWOHQ8AHNd3_w2JKEXuF69f1Bb2wNvknZaMMRTg1mvhkjg4Ia2c8JuX9slTgkdhATSwqYd0UhLasDmjliPE_kNuWbQ_4o6R9i5k860Tr1ML1pSNiyiMjNXsxN0eGUtw0Ot6QmQ93Z2Pxyf_8SR-ks_k-GyeMgZm8eGoovBQ5bkRQbkUcnCuO-PCrOqE3Cjb_pX86FmEXDfylc59JpiY6IPjzD6SKBS7UUfBTuI_SmeEFqjb5broaYl0AP7T9VPxHwLP7tWl2xCwPiiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
صف وام
🔹
انتظار برای واریز وام‌های ازدواج و فرزندآوری، دغدغه مشترک این روزهای بسیاری از خانواده‌هاست.
🔸
چنانچه شما هم ماه‌هاست در صف انتظار بانک برای دریافت این تسهیلات مانده‌اید، روایت خود را در چند جمله کوتاه برای ما ارسال کنید
👇
#صف_وام
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/697738" target="_blank">📅 16:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697737">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
سفارت آمریکا در عربستان برای سومین روز متوالی هشدار امنیتی صادر کرد
🔹
این هشدارها در روزهای ۱۰، ۱۱ و ۱۲ اکتبر صادر شده و آخرین مورد به حملات اخیر به فرودگاه بین‌المللی ملک خالد در ریاض و حمله روز یکشنبه به فرودگاه بین‌المللی ملک فهد در دمام اشاره دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/697737" target="_blank">📅 16:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697731">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IergDJGYYlt7XOn3xXv9s8biPKwcB_I0VqoJbahhbRZ9DgTshu8q0xA5DSjpZF_bHE1z4zqfc_8ymfCAxLtFwLSZbnqg4kZseGq0BxgDRFccG7sOG6sI9hxuYL7ZiLer-QEOrZXX4AT7ybsf1snYckism7_MAr4q64OMOJU9hq1Ma74VrUE9XEHVMCpyDdzEak9rH9kKeHXE3OcajCNU3lUkIIpVO9osu7yD4J95ZxeENNEk27A-wPGq7DEXNmKfSIIDF5nPof-S0ihUjYi5mjqybXVNk840P_lI3OZ2cFn7OvqhYykyB-1LYxijA_vbhbjixPEv9sd9AgtSQy9ryA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ryf31BfqPZFswV90eZgLHPdzWuS8zdfPU-mlecjQsbwteQAMm_MTHsf45zDr_HOHQjJUCpz98ED0AD8pM0skaVhaWPMdrsgcKnDMR-BDK0r6tm7jl9rU7mwRQUAbYPgF3Wq7JEznmmhFqIp4DyMqb7yBoNZOFJyf_-ixDHvufjZOjZahm0TQaw6EUYxHPpnFJRi6ljrLvV68cBtJKpnBmjRUp_9KdGc_DTTIAeEWOzKvK2ld6ciHjatH3o-BqqEvZNC6t1D-jMW_OEdh7_E4LZSdNFdMb7CJNrKbjQmQrQ53U9Z5k5NLROdMHBPXUSYCXqEG5RGM4ek7pAv_RKZ3iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iudp2vaLbBAfDakikeB53vSl3sWfYpWsa2eHc-wi4gpa5S28F4QGtqZZgT9uR9wM61aRpwfOVXM2TD3Z2SpsDnSn5EHeoyR4yU7E3fmu5PRx1Gy0nLFVYm0EX7VxL7mWaeGgo9xtxBhy56gXpeJdd7EVQfIctUpb2VBnLkLabpGUvFF_-jaZBxNnBIPtsNyP_FGk7n2WdLQHsMg1d8_c6Yu0Vi52uIrQdcBGDzUtSsWTRQEJma_jyUNkXMudU8D7jinjutpqz9i7hNftEzpVcnt576MgWljcNOGQnHGuh_VpnQOJstZJBpf9N-b1nLJgCW9z4Csuxt40mH4NQtJiAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qt9rh10K-WCbbCY1fYwd13WOfJ2vCBbOo2PNJBnazSLOL5bP9bt378Ss4omzWddP6oFr75iMPU8Dg-voRAXS7Ib_EYoOVf_-7I7H_G1AO42tSYVnizEsf3EdN01P96eSOfQyxpJf59Xk8uqaF0q5EZoAfPVHfcAKqmwDq8Ar-iFCrO-263AWjUpxITb5qHLBIbI2dDPwj0EvT6Wwtp61VOK0r2OJocZMsphi8YyDxQxm_UWdU6vd7mW3LlPOw87FoE-TiX56tB1JJ40xm8o5Uht66pIeTNKn2aIiEt5YZvPHwrVShPAKk61hCT2D3brsuo5mC3fZcqV5nMEo0Gd92g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z5L1DzgIf0MTiiXOgL31UyDIYuqrl6AZPOAKJ9466QocgMPpHpna-j2BUNSyXMWetGKT9EanF3aN71mlGiwgZQq8oYLzR4pwhzd4t5gZnUGTnuXXceBIhFrgDwIGA_Lme53iJfizcruAK-Vdc7a9fwbSf8EHVZtBxbJP6H7Sh-1uyJzJ3CdN_fMVhwQYl2X9olIqbSRLNf1aiIVw7kYHnAJkHb37qYkJCFSSq_7EHsQRUzTY0UZQZSyClGM29sewm-5w861G-z7T4e9-a3U3Tt6vnpw5WV63wa2wpaE4NQpP2lCHORCA7U4HPWMHoNXh-SnmMSKRvwl7e5DtY2I2tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n9sYXxDiVoJt_L_i8-W_ldPeTK5RbgqU42938jmCeZ81enH__--riaaLUvBTblaixL7nZr6dgUaQgjH7liOvuYq0aEDKqXO67gGSrb4b3fKRP4EepDGqsTBad_ILBapX8B_9lUNSfBlW92LtaBXsrOPxwDo56l65PkRzFVQ1zmEhxzTE3QhZU84h-YASQ509OCUIqiJ7VNXjqJFaaVIlDssgfGiOjkImsB7JP0JSymdbi_7u7uq6R2EI2JWeYV8c8VdpainZHXT8_X6SnCUWLvl7lD8hTKj5TTBElgyZHaEfCH6ZIgCkpyeVy7cMkl2x3xJi6pVJmOuZyeysatZgbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فوت‌وفن آشپزی؛ شکل برش مواد غذایی چه تأثیری روی غذا دارد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/697731" target="_blank">📅 16:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697730">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: حکومت سعودی از پاکستان، درخواست کمک کرده و در سراسر جهان به دنبال سامانه‌های پدافند هوایی می‌گردد
🔹
مقامات سعودی گفته‌اند که موشک‌های رهگیر مورد نیازشان برای دفع حملات یمن رو به اتمام است. سعودی‌ها همچنین دنبال استخدام جنگجویان خارجی هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/697730" target="_blank">📅 16:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697729">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781b50284b.mp4?token=iiyb3xsYO2LP1BZrEkwlcYQXS5JmCmV5LDXUx3HPjX14W97XiyHcvC0y-qS6IRcJQD5ZBhSOij_7rmzjFh3Z1aWniz3RqlGrC0RUeJbG-I_h0IRqsmFhy1WvRx3m1BwtObs94wVEJOer-og19LnWcMCxA-ZkSaBY6Tef0YXWQeIh5GsdYji07c0xv_uW8-PBLix9kZmhAnOzQ7wUabtpk1F7Ks_R7C1e2LFGC2VTBfA3wEirZPjLtNKGODEaAXdSxlV5GFTJ9SYTye3CWQ3n6GzkzszYmceUKAenFTUP1_pHxyeEB-TSuVkKoPC4FHENvdpYNGPcIsRukhKeuH-EMZmFN3xvkjMXzuyD5IQmM1CuxTM4QULS2QeKUurBPfl1dCN5EkS0fsz9yEMhuuzAfb_1Hfu8z6Nha7cfPtpAMDMNeJH2FWnKpXpXU67AoFZk4H0KtFKSzTPCsiSNDp6S8ihGuq74JkzEBBvu6InpzeiLC4hzfU9RZZyI-qn-40oraj3aZeyGcLtn_NZLmUyFM-NbpjpK6iXNSlGdVfUYvQ8LD1H6WjMTOE9bJUeQUpeOc6X7g4Gr6tLTfbUOLByUmAh3QQU4Olc7CYMM0Bw4J6ZmARBPdLp5Z3ABlxdP0QRlPme2st3XcZzYl3NoyHpxQxnoS3NIP9pCUf_sL7Gb3ZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781b50284b.mp4?token=iiyb3xsYO2LP1BZrEkwlcYQXS5JmCmV5LDXUx3HPjX14W97XiyHcvC0y-qS6IRcJQD5ZBhSOij_7rmzjFh3Z1aWniz3RqlGrC0RUeJbG-I_h0IRqsmFhy1WvRx3m1BwtObs94wVEJOer-og19LnWcMCxA-ZkSaBY6Tef0YXWQeIh5GsdYji07c0xv_uW8-PBLix9kZmhAnOzQ7wUabtpk1F7Ks_R7C1e2LFGC2VTBfA3wEirZPjLtNKGODEaAXdSxlV5GFTJ9SYTye3CWQ3n6GzkzszYmceUKAenFTUP1_pHxyeEB-TSuVkKoPC4FHENvdpYNGPcIsRukhKeuH-EMZmFN3xvkjMXzuyD5IQmM1CuxTM4QULS2QeKUurBPfl1dCN5EkS0fsz9yEMhuuzAfb_1Hfu8z6Nha7cfPtpAMDMNeJH2FWnKpXpXU67AoFZk4H0KtFKSzTPCsiSNDp6S8ihGuq74JkzEBBvu6InpzeiLC4hzfU9RZZyI-qn-40oraj3aZeyGcLtn_NZLmUyFM-NbpjpK6iXNSlGdVfUYvQ8LD1H6WjMTOE9bJUeQUpeOc6X7g4Gr6tLTfbUOLByUmAh3QQU4Olc7CYMM0Bw4J6ZmARBPdLp5Z3ABlxdP0QRlPme2st3XcZzYl3NoyHpxQxnoS3NIP9pCUf_sL7Gb3ZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌دونستی یک کوه آتشفشانی چگونه تشکیل میشه؟
🌋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/697729" target="_blank">📅 16:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697728">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHBLF1YkuWmiCp9tDl2924Iopa2dJdwn1a6mtCLKVXZP8YyZhRiIkiL4ocnwZZ_q6yvaEiXxpx43sXT7nepA5hYkFFufFTy3IKQLQ34pb6ivpzes1Wbyb6_2F4G5nG6jbkeg_-SRKTnWw4IAN1GfwZzyRvdUNicB5hD4HrJK1ZKG0s4e6qfpQ05L3nhVeUbaNEjPuvUHYPi1g5GP4wUI-0S_mTE62-GhY3O0UaC2i6waTq_0ZJGuwzLPr3i2FPWg7dxddsNWNeZfkoICavahLTWTNlEkwyee-C7ao_aJh24se_4sk-SdUl4W01KpF4m45c7_2gJjEzFPpMaH7EjyYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو کمیسیون اقتصادی مجلس خبر داد:
موافقت با واردات ۱۰۰ میلیون دلاری لوازم خانگی به صورت کولبری و ملوانی
حاکم ممکان، عضو کمیسیون اقتصادی مجلس، در گفت‌وگو با ایلنا:
🔹
با واردات چهار قلم لوازم خانگی با استفاده از رویه کولبری و ته‌لنجی به صورت مشروط و تا ارزش ۱۰۰ میلیون دلار کالا و قطعات تا پایان سال موافقت شد.
🔹
اولین شرط برای واردات، ثبت کالا و قطعات در سامانه وزارت صمت و الزام شرکت‌های بزرگ به گارانتی آنها است.
🔹
دومین شرط هم تخصیص ارزش واردات به ازای سابقه عملکرد کارگزاران هر استان است. تولیدکنندگان هم می‌توانند قطعات مورد نیاز خود را با استناد به این مصوبه وارد کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/697728" target="_blank">📅 16:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697727">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
اسرائیل هیوم: نتانیاهو پخش زنده در شبکه‌های اجتماعی پیرامون موضوع انتخابات را به دلیل حادثه رخ‌ داده در شمال اسرائیل، نیمه‌کاره رها کرد
🔹
بر اثر انفجار یک بمب در شمال اسرائیل بیش از ۲۰ معلم و دانش‌آموز به شدت مجروح شدند؛ هم‌چنین منابع اعلام کرده‌اند که دو نفر نیز کشته شده‌اند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/697727" target="_blank">📅 16:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697726">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsLPkR9iymlhOycT2jwp9jjgdkcfovZoz16NtAHajCFPbIdIbWxkkOTpJ5SAinf_Rq9BDZ-90DOKcA2uffJmvGxDC1LlgJ14g_bKU73SA9z8uULZDAmYrdO29brl5S2P5kKiZt4R3XAMLH3ObjbiDpZcT2xFuJn3rLfONv0LcGqY5HDM6ygj80hX2zapJ8lKiO3VVzRw09w2Wu3zP4gjnEMEHC_lQx0Cj9D6axmk-6pdRo-vuIK_7NGkv9tnHBUS65Yeez7h1D06L8kRnJ5asIaDQSNfK_0EVNoNI2HonU59ry8C8mLKhVRh2s9JyES9eKbYZK6HdGsDgff2h6gXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت خام برنت به بیش از ۱۰۶ دلار در هر بشکه رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/697726" target="_blank">📅 16:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697725">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c54b922675.mp4?token=Qxin3sxSvOppONxM0PxRb4em4kjfCJm1EwiHwAXPxG8qDVewp1VPwDz9uk_Um43S6Vuk0vmkMEFSdvKZwn7AwFKgI6-3jLFfKcpM7W6a-D0UhQHBIdVdey0PHPEROE_SDJcoTN9X7avg85lWs0TYNmyvZ45JnenS-l8U0dEur1WtqEcYDZmbLZNF6zJwmYrh05aIRG0XIRYxFWg8o34IS10kJ-_ozPq0HVji2GFmgAoiFEqWYitog_CWA8uQ7MkqnEyR3_XRI2QqygngG7tV3n-y0KgHIRoBEyQ0_hZPfLZmgb71x3tVPriq5njJbz7CvKakZAAd8FkNKoI9FhuAyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c54b922675.mp4?token=Qxin3sxSvOppONxM0PxRb4em4kjfCJm1EwiHwAXPxG8qDVewp1VPwDz9uk_Um43S6Vuk0vmkMEFSdvKZwn7AwFKgI6-3jLFfKcpM7W6a-D0UhQHBIdVdey0PHPEROE_SDJcoTN9X7avg85lWs0TYNmyvZ45JnenS-l8U0dEur1WtqEcYDZmbLZNF6zJwmYrh05aIRG0XIRYxFWg8o34IS10kJ-_ozPq0HVji2GFmgAoiFEqWYitog_CWA8uQ7MkqnEyR3_XRI2QqygngG7tV3n-y0KgHIRoBEyQ0_hZPfLZmgb71x3tVPriq5njJbz7CvKakZAAd8FkNKoI9FhuAyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو جنایکار درباره ایران: کشورها، حتی آنهایی که به ما حمله می‌کنند، به آرامی و پنهانی می‌گویند که ایرانی‌ها باید سرنگون شوند، آنها ما را خفه می‌کنند
🔹
ما مطمئن خواهیم شد که آنها(ایرانی ها) سرنگون شوند. آنها سرنگون خواهند شد
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/697725" target="_blank">📅 16:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697724">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p93AGVJCN42ZFQDE4hGm7glybqx7TSvDslCOCgLjUh3cOoMg7hqn1kaPpJXTSnl4w61p9_57QtqQzmpdtyPrWlCWrlhrdobvAC_IiU0ccfqIQ7QC_v6BI5ltBRQA0lee20lag9_TMgPS3izn0ve0RTjhkC7IfQo20RhdOmd4zNXx-ZjEX3q0uoNyoppSWnysYqqYoDGApiUsbLeIfxhSmlr3fovDmy5fQatnt1dioNtDuwpZTkyLCinOB2IkydXj6_eYWtFwsNYNW1I6sakyKqJBID9rCak8-mX-2CNB671tFHz4wVPQxzbte6eKfx28qmS3Oy8Gh9SmEAcHlnTbgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله اسرائیل به بعد از انتخابات موکول شد! | سونامی مرگ در ارتش صهیونیستی | ارتش اسرائیل توان یک جنگ تازه را ندارد
🔹
هم‌زمان با آماده‌باش ارتش اسرائیل برای احتمال ازسرگیری درگیری‌ها با ایران، افزایش تلفات ناشی از حوادث عملیاتی، پرسش‌هایی جدی درباره ایمنی نیروها، عملکرد فرماندهان و فرسودگی ساختار نظامی این رژیم پس از نزدیک به سه سال جنگ در چندین جبهه مطرح کرده است.
ترجمه گزارش معاریو را در وبسایت خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3251877</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/697724" target="_blank">📅 15:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697723">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66efb43c89.mp4?token=pKb1FhrqkPmoYIW2k46I60jNQ0eUUMLS6iJw06547ZEA0hZPQM5GMuIw24vKz3tnNTVnT5susAjNap5aeQ8IeJZKKxUC25IkfZ7ePI9VsJ0DH007sncC3QptYK1XD9FMILnLCVeCzcpDWD85NoeUgBT0lZOLh-2ag29ORdBk4_teNIrKA5KX5yEYoStgYLTsM9l4mrrgs6KNUjUXmgVho0AjA-bUE2LaqR-VMM1M_MhE9hrGdl2pCL3sn2qrv2tl_wwYqII5pfWSTAg0CDbBZ_Caz93nL96zSn06OXXZpzrZfIPvwx4Y4fy9L3rWi-R8T-Lrpu7OjfwDmn3ASY5Zpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66efb43c89.mp4?token=pKb1FhrqkPmoYIW2k46I60jNQ0eUUMLS6iJw06547ZEA0hZPQM5GMuIw24vKz3tnNTVnT5susAjNap5aeQ8IeJZKKxUC25IkfZ7ePI9VsJ0DH007sncC3QptYK1XD9FMILnLCVeCzcpDWD85NoeUgBT0lZOLh-2ag29ORdBk4_teNIrKA5KX5yEYoStgYLTsM9l4mrrgs6KNUjUXmgVho0AjA-bUE2LaqR-VMM1M_MhE9hrGdl2pCL3sn2qrv2tl_wwYqII5pfWSTAg0CDbBZ_Caz93nL96zSn06OXXZpzrZfIPvwx4Y4fy9L3rWi-R8T-Lrpu7OjfwDmn3ASY5Zpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کندوان زیبا، تنها روستای صخره‌ای جهان
😍
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/697723" target="_blank">📅 15:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697722">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیوپنا(پایگاه خبری دانشگاه پیام نور)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT1BL7BFKY9woTyFlX2-E5hoUhdjeL2zhXG3eJgM3aWhcWl_Bt2y1ME9nkmsND5f-d5gjnhsqQPC98FE49ltrRwtX4BVNitYNoJy25kBBKUOeSMslzxxn_yfDfXTHEid5FKYlXfg7pDg3Xw4zRuPYXAGrc_ZrQv4oalp15PEb9Hr-kJ7skaWg4ecn_mgZKJvqEK14LCXDC7I206MvSNjUB52BcEeXNy5nH7COBBjfphCR2q4B67Y-KARm1z6v3bhayMwoJM1nsPfXZb4R2DBN496trnjcHMxfTaAbcXlu4NBSbo99AChRGsc_-_z-477KQ1kC9Fsv7p9ZKJS6CJWjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
دیگه وقتشه انتخاب کنی؛
⏰️
دوشنبه ۲۰ مهرماه؛ آخرین مهلت ثبت‌نام بدون آزمون دانشگاه پیام‌نور
📌
فرصتِ طلاییِ تحصیل در بزرگ‌ترین دانشگاه دولتی کشور یادت نره
📍
سایت ثبت نام؛
sanjesh.org
┄┅┅┅┅┄❅
💠
❅┄┅┅┅┅┄
اداره کل روابط‌عمومی دانشگاه پیام‌نور
@upnanews1</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/697722" target="_blank">📅 15:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697721">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
احتمال لغو، تعویق یا تعویض میزبانی جام ملت‌های آسیا ۲۰۲۷ عربستان
🔹
کمیته اجرایی کنفدراسیون فوتبال آسیا به زودی درباره میزبانی عربستان در جام ملت‌های آسیا ۲۰۲۷ تصمیم‌گیری می‌کند و به علت ادامه وضعیت جنگی و ناامنی‌ها در منطقه، احتمال لغو، تعویق یا تغییر میزبان مسابقات بررسی می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/697721" target="_blank">📅 15:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697720">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
‌
وال‌استریت‌ژورنال: تلاش حکومت سعودی برای تبدیل‌شدن به قطب هوش مصنوعی اکنون با خطرات جدیدی روبه‌روست؛ چراکه دیتاسنترها جزو اهداف [یمن] هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/697720" target="_blank">📅 15:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697718">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbzxgyrnbDA2CvuzAeob2l3jDU0FmSfSlVgxPq0tB_85qhf7HavLuKzbU8ijIOmut86ACYmPu6eXMsdzcDTwWiOPNjivNler8EXkH87eCZsOf0JnGB87UrTE05KwLNFkgIl_Jn54X8uZ4GUlLRU__YSPCcoH9nDCXPdFYEtKVi8zAEEsP7GRr7CIBrGy_k6WYIXdvrZWxVZdyL37V4Hd6n7UiLMAAaSibPp5cwSSG7A8UunuEhsX7dP77uwYePcnYmFPeHhdbnuAk6kzcS0AOSDMBk1GPQkKm1QotLFk89K5n9hIwNlDqw8cgQJf1s5ITe8wm5a0xbACNxyXRWpnng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز ابر عظیم زیر فضاپیما هنگام پرتاب؛ این دود از کجا می‌آید؟
🔹
برخلاف تصور، بخش زیادی از ابر سفید زیر فضاپیما هنگام پرتاب، بخار آب است؛ آبی که برای جذب امواج صوتی شدید و محافظت از سکوی پرتاب و فضاپیما به کار می‌رود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/697718" target="_blank">📅 15:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697717">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh96qJBaqTr0s91qgrx0PP6xDNmJcT_9SmzyQWrcJCN-8ABjuk07ulbn7KgQmvduB5NXUcVy-2qH5wZUCoL2T1w5-fVg3N-hbXAHHuPzNpAAz69e1CoO_ZmlWlc33e91FHr5rpchfprxlYc8NjaMoHXUeqetlMy0CdEal4L-_lQHLybXtEH-_cPeESTRWXNGgaCMrOnbkpHMGBWBVt5tprhXnCnG4lR3cDGjTt9oz7IREg69EqyXd3-XIL5nw16xdhg63IIMpuM_sRRnRW_cmWyTHBr829khTrf5nOWdwwlv9RWpQjdhlC6_N9wPPRZnxY_QA5tqZduJu5JXQzDIQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چالش تحریم و فرسودگی زیرساخت فناوری کشور برای اپراتورها | تحریم، واسطه‌ها را ثروتمند کرد و هزینه فناوری را برای ایران چند برابر!
🔹
جنگ، اختلال‌های ارتباطی و فرسودگی شبکه تنها بخشی از مشکلاتی است که امروز زیرساخت فناوری ایران با آن روبه‌رو است؛ اما پشت این بحران، یک چالش قدیمی‌تر قرار دارد.
🔹
تحریم‌هایی که سال‌ها است دسترسی کشور به تجهیزات، فناوری‌های جدید و زنجیره تأمین جهانی را محدود کرده‌اند./ دنیای اقتصاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/697717" target="_blank">📅 15:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697716">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HJt-KzEJxJwJsB7hPPl31g5sLshBugcv0FMs7YBxP_hvPOm4zE-dcrdYNP34qwZ95enZIXb85loo9iM3rJ6DRKRvt46tsNeOoT75mP3fnmEQ8sBXLUgUAR7S_9q2xFLJiob6s5SmQQg3ZhPB7nTxYPp6LLdXNDPQjmG6yFCT4RVpgE7L-eMESzIN7qsjDxKuQO_aT6oKs_y8Y9AqCAn8FlFpW9POKOBhZ0rpCuAj1VU8b7jUHgKJ_du4HjJpq26M7X5W7-QKv1GJjZ_yas9kiGzmUycotreMvMbOF_nfaEw-4UQFR6mHLO-j2bj9v5jg0_Po_xgBJOSwUOdZQLsN0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین تصویر از مهندس مهرداد اخلاقی کتابچی، وزیر پیشنهادی دفاع و پشتیبانی نیروهای مسلح
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/697716" target="_blank">📅 15:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697714">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7382f953.mp4?token=BA2Qvi-iJ9TM5I2RQjEHS8FPbYE4XnDrwjyO2NRgXqIJTl5wiYnwOe46pSStBOiiIJNLsEfcquLbZN7FsjzHHook7aArY4KXVbbXFoF-vSvheDRRODUw7eEaV_y6IkHDFzPZlxA2szrMgCbVRHxE1l0Gk9oknCCnNRlcLHaP9Zcr78sv-r0k-gnoT8eb0YvOeHLIDpnABcKZY1_760bk1CiWJgRY__k9ZhWLePIjBf6o9dgUlX_E9SiPDM5F_BewhmYs7blH3bizT0xFvLE_YuIlifhgp_rucFVLSngWoqJrUl4sWZmzB9QcsnNZrNtE5F6Y7H2F7jCEm58Wi3VxsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7382f953.mp4?token=BA2Qvi-iJ9TM5I2RQjEHS8FPbYE4XnDrwjyO2NRgXqIJTl5wiYnwOe46pSStBOiiIJNLsEfcquLbZN7FsjzHHook7aArY4KXVbbXFoF-vSvheDRRODUw7eEaV_y6IkHDFzPZlxA2szrMgCbVRHxE1l0Gk9oknCCnNRlcLHaP9Zcr78sv-r0k-gnoT8eb0YvOeHLIDpnABcKZY1_760bk1CiWJgRY__k9ZhWLePIjBf6o9dgUlX_E9SiPDM5F_BewhmYs7blH3bizT0xFvLE_YuIlifhgp_rucFVLSngWoqJrUl4sWZmzB9QcsnNZrNtE5F6Y7H2F7jCEm58Wi3VxsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش غیرمنتظره پیک موتوری به تلاش برای سرقت؛ بیرون آوردن قمه از کوله‌پشتی، لحظه‌ای غافلگیرکننده رقم زد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/697714" target="_blank">📅 15:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697713">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/934c3687b9.mp4?token=tcoqqfyFdV1qMPD0nkhf2oJBZuka5k4XoIfosI1AUS_H3mPd9_DJi5-5QDL4tW87yKgWR8eH2m2CtnI95lPgFUxKf7cGrer9SNT_mgoArlpXfiMqlmYEA9P6TZQRsVnqUVWz_HJU5z1DttqOMKRFQtZ3-FuNH2MaEd5-hM6s1tVOK4einKlIbkcsbQwO23z9PlqOqr_wzkZX83gFj_WqEPT8ArzrcUc3MuohyVTA4h-RR2OFV9_kxQSfDH4Z5GXxQCZYus-DzDj_VljJCwfe6i8jrrBRNQrYhCBazvymHY46Igs0sT6ueexMfma5_ZiLzrKmVYdnffps48yiIMdZVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/934c3687b9.mp4?token=tcoqqfyFdV1qMPD0nkhf2oJBZuka5k4XoIfosI1AUS_H3mPd9_DJi5-5QDL4tW87yKgWR8eH2m2CtnI95lPgFUxKf7cGrer9SNT_mgoArlpXfiMqlmYEA9P6TZQRsVnqUVWz_HJU5z1DttqOMKRFQtZ3-FuNH2MaEd5-hM6s1tVOK4einKlIbkcsbQwO23z9PlqOqr_wzkZX83gFj_WqEPT8ArzrcUc3MuohyVTA4h-RR2OFV9_kxQSfDH4Z5GXxQCZYus-DzDj_VljJCwfe6i8jrrBRNQrYhCBazvymHY46Igs0sT6ueexMfma5_ZiLzrKmVYdnffps48yiIMdZVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا حالا فکر کردی چرا جراح‌ها لباس سبز یا آبی می‌پوشن؟
🩺
#حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/697713" target="_blank">📅 15:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697712">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جامعۀ مهدوی/ج۳</div>
  <div class="tg-doc-extra">استاد علیرضا پناهیان</div>
</div>
<a href="https://t.me/akhbarefori/697712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جامعۀ مهدوی/ جلسه ۳
حجت‌الاسلام پناهیان:
🔹
2:10 چرا ظلم بر بعضی از جوامع حاکم می‌شود؟
🔹
7:50 رخ دادن مهم‌ترین مقدمه ظهور امام عصر
🔹
27:05 مهم‌ترین عامل در فرایند ظهور از نظر خداوند
🔹
31:10  پیدایش نشانه‌های نزدیکی ظهور در جنگ اخیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/697712" target="_blank">📅 14:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697711">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91de7b54ce.mp4?token=btFGz76Bv8XWR8k8aeFT_nHpQwjBGC2JmSzeJaj_hpyPXeOfCdDzLG2QHQ0uaMMtzDY18K8uTvmAkhIhoUSKi4rA4mai4yQvtosAg3UYLKdMly1IGXads0bId-ReGajXwu-mBd-ZSH6DNbF0DH4BmHXepkuQfrBZVGHEIkHFAcGzJVMOPYDjsd5M3kjriuBrX7sZwiIJ0U3a7Eqs_H23gacBvPMsn48ByOTPsxs95qZ_AzLkWvznAm6loaQC5FTvsEetZ5RVzr44raYIvdU4IKbBdmxmWF4Xc9rF0CLYq349SFrg_POiXj2KtGy0YyCTNtaV1CuXD4YnukXKRNAeAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91de7b54ce.mp4?token=btFGz76Bv8XWR8k8aeFT_nHpQwjBGC2JmSzeJaj_hpyPXeOfCdDzLG2QHQ0uaMMtzDY18K8uTvmAkhIhoUSKi4rA4mai4yQvtosAg3UYLKdMly1IGXads0bId-ReGajXwu-mBd-ZSH6DNbF0DH4BmHXepkuQfrBZVGHEIkHFAcGzJVMOPYDjsd5M3kjriuBrX7sZwiIJ0U3a7Eqs_H23gacBvPMsn48ByOTPsxs95qZ_AzLkWvznAm6loaQC5FTvsEetZ5RVzr44raYIvdU4IKbBdmxmWF4Xc9rF0CLYq349SFrg_POiXj2KtGy0YyCTNtaV1CuXD4YnukXKRNAeAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای یک متخصص: گیاه‌خواری مغز را کوچک می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/697711" target="_blank">📅 14:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697710">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7LXcYH9jYubnrBYjnFEZgUZ0iOBp_YPdEyxvJNhioWMQn7i2eM_eblN7tQO8FbU2tR1VtjuuWGtD1JH6Qdseb4xWTwyDVJJJcnPT38YvZOKJS9umGK3LKSpwD58NmOoevfGdpQxtbpvk4cOBy7DQUbSyJQNfdg0jUvHOSABS_yJdgZsaxGwKtsWMxU7jxNtJNnj3kqLBxS-o46cW2KtCqKBcerxGrvGfgASmbL1XdsXF118slYu43oc0mPv4yS1UytSnshtRuOskPUJ3V4JDUZVU2fKVXKNEzcsW2pLd-5BmHauK9JzLt_ChUQCI52ZU-ogfHfWV89Wm8rySDWaZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
دو جنگ سال ۱۴۰۴ در مجموع باعث استرداد ۳۳۷ هزار و ۴۸۰ خدمت سفر در علی‌بابا شدند.
مجموع مبلغ این استردادها به ۱,۶۱۴ میلیارد تومان رسیده است.
از این رقم، ۱۶۰,۵۶۷ استرداد به ارزش ۵۷۲ میلیارد تومان مربوط به جنگ دوازده‌روزه و ۱۷۶,۹۱۳ استرداد به ارزش ۱,۰۴۲ میلیارد تومان مربوط به جنگ چهل‌روزه بوده است.
📄
این آمار در گزارش سال ۱۴۰۴ علی‌بابا منتشر شده؛ متن کامل گزارش را بخوانید:
https://B2n.ir/jr9328
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/697710" target="_blank">📅 14:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697709">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
سامانه امداد تجار اتاق تهران؛ همراه هوشمند کسب‌وکارها
🔺
اتاق تهران با راه‌اندازی سامانه «امداد تجار»، بستری غیرحضوری و شفاف برای ثبت، پیگیری و رفع چالش‌های کسب‌وکارها فراهم کرده است. فعالان اقتصادی می‌توانند مشکلات خود را ثبت و از حمایت‌های قانونی و بسته‌های حمایتی دولت مطلع شوند.
👈🏻
کسب اطلاعات بیشتر: ۱۸۶۶ و
https://digitalchamber.ir/emdad</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/697709" target="_blank">📅 14:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697708">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b5df263ea.mp4?token=gk65wKYKAKyrSVXcZIpH9HZx4sFraS0Z18cagV4gWWR8ctNOnNttui63lrAEYkw4t7wXDgGDmlVrvPFIdySilM-DjhAtzkNOSDoGtVGljgjViBUaFYtCii17PSEYBNPnjZKgm4H8u9x1xDhAGrLPvtBX7oefaKKNserN8-SXmqNNzVFTaTtHVH2TCY83fP2kxL3-G6uoWwYldvFmt3idjjpEHqQJo_gADM26YPdlM3f127zL-tgb4DlqAhqJOItwJe7JU-8fmAzRKeH63jH_oTKdTYEuKGGe_oIssxG58_56f6-c-9iWuflI0FD4nrL8t3beB7LvCnZDm7Uwluh83YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b5df263ea.mp4?token=gk65wKYKAKyrSVXcZIpH9HZx4sFraS0Z18cagV4gWWR8ctNOnNttui63lrAEYkw4t7wXDgGDmlVrvPFIdySilM-DjhAtzkNOSDoGtVGljgjViBUaFYtCii17PSEYBNPnjZKgm4H8u9x1xDhAGrLPvtBX7oefaKKNserN8-SXmqNNzVFTaTtHVH2TCY83fP2kxL3-G6uoWwYldvFmt3idjjpEHqQJo_gADM26YPdlM3f127zL-tgb4DlqAhqJOItwJe7JU-8fmAzRKeH63jH_oTKdTYEuKGGe_oIssxG58_56f6-c-9iWuflI0FD4nrL8t3beB7LvCnZDm7Uwluh83YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌دونستین خطرناکترین بار دنیا چیه؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/697708" target="_blank">📅 14:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697707">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6D5_FvfdrzW64dc5BW25EgItBYgpFAJ4bC41IhvrF3YnJ49bHrAGCbsLarlWn1f_7xqHdd8Hr63vQstG4UHV_8DaBKt8QAlGR7u5IdoeQbOnXxEnl9nsTUp51rUtKON_Nt1QJGSVvZcusAJ8qvtnKY91ISvHB5tiLmB-coL2v7dPRiTSBQ0oQ3Rz-6wiDZNubMFFNY3u7ZxSp1gcbwbOD2Ay53up4IhvYFSzE5_9YmXPQNAFXxVT1njxFIMRFUoQrVILJ60P-XfkdDZD7EkX5b3HF6UfPLSH2hcz692P0DPXMSeBwvS6dKpMh4NuKtZLaT4htbenIMx5TVfBU2w7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قبل از انتخاب رشته، این ۷ نکته را حتما بدانید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/697707" target="_blank">📅 14:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697705">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a578c75cdc.mp4?token=EEbmfMtXkeXqWzK5rDYjnH0gmqaknAsMP9RcJIG6niE-vS9dLFA3rh_rsvWmC0lta_7UkLWX65GlAuctR8bhcwKz6JTp6qRCozQq32gvuUl5tvV1x1Uk0DqNNXpIo71d17Cri7dIwHF4LRf0ipFoHvcNY1OwhOaCDScq6NfEjdArMbhHixBkOSdnv57gyjaZHkSWsnqpQ5cLp7nFcxcy6SkJ-5VRvf1dvXz6Qiqo0HCeJCRD-nNk6D29Y9GCEyG88zgxoX9_8enTxieQxQWw9ExfNE4yc9DgIMWmxWMfo6_ozpKtyQk3ke2GcQ5ownQWNlyxtZKs2_byeoEzNTuxVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a578c75cdc.mp4?token=EEbmfMtXkeXqWzK5rDYjnH0gmqaknAsMP9RcJIG6niE-vS9dLFA3rh_rsvWmC0lta_7UkLWX65GlAuctR8bhcwKz6JTp6qRCozQq32gvuUl5tvV1x1Uk0DqNNXpIo71d17Cri7dIwHF4LRf0ipFoHvcNY1OwhOaCDScq6NfEjdArMbhHixBkOSdnv57gyjaZHkSWsnqpQ5cLp7nFcxcy6SkJ-5VRvf1dvXz6Qiqo0HCeJCRD-nNk6D29Y9GCEyG88zgxoX9_8enTxieQxQWw9ExfNE4yc9DgIMWmxWMfo6_ozpKtyQk3ke2GcQ5ownQWNlyxtZKs2_byeoEzNTuxVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁨ ⁨⁨ ⁨
♦️
قبل از خرید کفش، این تست ۳ ثانیه‌ای رو انجام بده وگرنه قطعا پات رو اذیت خواهد کرد!
👠
#فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/697705" target="_blank">📅 14:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697704">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daejODigavYSWVWxE4fP8gfQNJTsx8mD4zhwM3EZFxnpdvfANw01IYP1wBMBIBIEbghiwjeUZQGnnx6-0c5TqPToBVXe9dcwbbuyS61KKHvkw7JPb980SH3k5BCwLHUhEPBpMvw6vKJpj8qkWRAtZo10G9DEfD7ztmo9g8oPxP_lJDcOV61AUXccswTdlZjVMnczwH8BDizfOcS3gX35q7mWDyNasDFL5oUKd0W9JEixTdWLtHigyWDy43Mi5PkoC5XVSxkgQ7TGCzfe5gF9pWD_F-jBDxr2IBstuQAQAzW3MbB0dFVlmYPcRfmDdZlZm0-eZiiHdElxHvEAW_lHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقایسه حداقل وزن تحویل طلای فیزیکی در پلتفرم‌های خرید و فروش طلای آنلاین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/697704" target="_blank">📅 14:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697701">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
کانال ۱۵ اسرائیل: ضعف و درماندگی عربستان مقابل انصارالله یمن نشان داد که پول در خاورمیانه امنیت نمی‌آورد؛ این انتقام خونسردانه و تدریجی ایرانی‌هاست
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/697701" target="_blank">📅 14:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697700">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/20abde47eb.mp4?token=kN20-HRm_183T0-IJYSp58efzwhqBkSjI5REbQouZ6HyUrCPN6YtGVID738XTtZ-xChtd3m4qW2QzQgzhvU_msl2jqJFUrtIu5cOL73_ipOrb7UkZXC3Hvj31paZr5tGk0__P-JdZesdBPYh_NyadwmkZf2vj9Yj9kQ0GCQ177KF9Yw84HrVxKdjAw1vcHPsHVo_lBA8TeljJ1yrGopwWUx5h8f33vdo8FQ9c8SkqgExwpwqvCR4ihWhEOCzjCsHQjYYYksAOWkxjSUrPExJ_6sVHLzKvAgkCrZIzJ4um1joBRAGWzGI4xbR4j_RWfc7anhtXjcdP2pVLnacWrv-GA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/20abde47eb.mp4?token=kN20-HRm_183T0-IJYSp58efzwhqBkSjI5REbQouZ6HyUrCPN6YtGVID738XTtZ-xChtd3m4qW2QzQgzhvU_msl2jqJFUrtIu5cOL73_ipOrb7UkZXC3Hvj31paZr5tGk0__P-JdZesdBPYh_NyadwmkZf2vj9Yj9kQ0GCQ177KF9Yw84HrVxKdjAw1vcHPsHVo_lBA8TeljJ1yrGopwWUx5h8f33vdo8FQ9c8SkqgExwpwqvCR4ihWhEOCzjCsHQjYYYksAOWkxjSUrPExJ_6sVHLzKvAgkCrZIzJ4um1joBRAGWzGI4xbR4j_RWfc7anhtXjcdP2pVLnacWrv-GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شادمهر عقیلی: یکی از مداحان داخلی یکی از آهنگ‌های من رو تغییر داده، گوشش دادم جالب بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/697700" target="_blank">📅 14:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697698">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/251415bc2c.mp4?token=iimF8j1SbO5eEsg7J8opUWMJjZpkoaUUo_fTQfp6E_T86C4DChTczK_VrWmZ0QKCUv6uthTkS2rSLVn9g34VAF3ppFqIN4pAudxmtE17DFBKbXZcMhDebfruMlWDUUD8PTNGorzHZfclB83qJbX3Rj_ICXIyXkb84TD0_R-dmHUFm_Xm98VsTpoLb_fmzmlKgpZMISu_SEqWYCzQneG8mzZeliD7pnBSJmNukBehcmk8b6pSgvqFh1jyA4QfILIhl60OK8OVeVHGqFrdRqjjUvpn3DOj28Mspx0Rzg7ksGFFPhJ3voxMM2zoOJMyeqcIJtVu4ntf0N9Yc3h8Pvs7FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/251415bc2c.mp4?token=iimF8j1SbO5eEsg7J8opUWMJjZpkoaUUo_fTQfp6E_T86C4DChTczK_VrWmZ0QKCUv6uthTkS2rSLVn9g34VAF3ppFqIN4pAudxmtE17DFBKbXZcMhDebfruMlWDUUD8PTNGorzHZfclB83qJbX3Rj_ICXIyXkb84TD0_R-dmHUFm_Xm98VsTpoLb_fmzmlKgpZMISu_SEqWYCzQneG8mzZeliD7pnBSJmNukBehcmk8b6pSgvqFh1jyA4QfILIhl60OK8OVeVHGqFrdRqjjUvpn3DOj28Mspx0Rzg7ksGFFPhJ3voxMM2zoOJMyeqcIJtVu4ntf0N9Yc3h8Pvs7FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخی منابع خبری از شنیده شدن صدای انفجارهای شدید در اربیل عراق خبر دادند/ تسنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/697698" target="_blank">📅 14:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697697">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
وال‌استریت ژورنال به نقل از منابع مطلع: محمد بن‌سلمان، در پی تشدید حملات موشکی انصارالله یمن به ریاض، رفت‌وآمد خود را به کاخ‌های به‌ شدت حفاظت‌ شده و مجهز به پناهگاه‌های مستحکم محدود کرده و تحت تدابیر امنیتی ویژه قرار گرفته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/697697" target="_blank">📅 14:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697696">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HD-6ePFgrAw9tKRaXWdFRhi5GRS1HWUFLfIjwPiy_O_laUL2TVC1FMhjytPFO06f2zTJl0u3kO2PxWWnPzKS42h3MM0X194MPWbRKUESOGm5jh5Pxilg3NCXxIEahNVCTdybOfqDGwxtS4EuqLoBuEYJreK6roFlJ9Ruy1rcL9vRz_7pT28zwVKBtUSCkHat8NMXADKRoSe07bgUzpstrSG9wEB77vKKkaThqIUOaENSbPHOkLvtcTN-2Dh7kQY_z9vUWIUeGZPboMGw7vvBaBfwLH2mGWtO1rEBiHnfHHywK5dD8LA8QZBWFU-YI8jTm0G-cn3n3Me3exf08x1yyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر وایرال از آگهی ازدواج در فضای مجازی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/697696" target="_blank">📅 13:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697695">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aWK0rejPv-y0_LhUZNRSEmokYWZsOaNB9r69R3TkyAWbb2WUUkdFdp5RLM4xWkIc-nGrSfnejYPyRDNu5T4PmOGW3TYtuqUD-qu3HFo92paWmCu2FlCtH5CorP4VxXAi2RMPE3UY9spf_KYwjsFbDmzM6yKRny_C5EG-CnF1nTYmmHHJGMd7Lffn2E5geHRpVky8HY4SA6VWrmufkC4w7NhTsnXzHCYlKvoQcaWmtvwZZx1JLUqM1y8T1BRULFJUjnYi0m6jqTI5vFvljJFSd5McK5PoUjJ7TUBYe5RodOc0dPYJBL16HQKf4QRz8JpqXdcAt2padLR9anLL3INjuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محاصره شهر تعز در حال تنگ‌تر شدن است و کم‌کم انصار‌الله در حال نزدیک شدن به سمت ورودی های شهر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/697695" target="_blank">📅 13:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697694">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06683e3b4.mp4?token=YYUVsVKB6oLuob3ND84QTrwzH1AIDlUAPUTeejxftZO4XPk24gqZ9GOVQ49zo0959IkeQEHlnBpqqtkWD02I36PPZ9fllL60uE1MtttvLMvAqNtaY29XyDrQ0TuzOijJZji53BbSiAUz5wGTBbYBX197BMUZ2pHDcHFFQSgv_4YziEp0qAI6jX8kJ5_hk2lbfNC5c-Xr65iKPN69ZfvA8JGhWDvoe3Vi3zhm1fGjacOi022_5iD4P7-bmelKhjQzk-YghXzmSwOiRCPIhN1HOKgOcIfMyJruxOKvEi6yDAtDGQYqJpxl3r2oZBrkS9Ts1DRue2dPJBO9bqcLUL63KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06683e3b4.mp4?token=YYUVsVKB6oLuob3ND84QTrwzH1AIDlUAPUTeejxftZO4XPk24gqZ9GOVQ49zo0959IkeQEHlnBpqqtkWD02I36PPZ9fllL60uE1MtttvLMvAqNtaY29XyDrQ0TuzOijJZji53BbSiAUz5wGTBbYBX197BMUZ2pHDcHFFQSgv_4YziEp0qAI6jX8kJ5_hk2lbfNC5c-Xr65iKPN69ZfvA8JGhWDvoe3Vi3zhm1fGjacOi022_5iD4P7-bmelKhjQzk-YghXzmSwOiRCPIhN1HOKgOcIfMyJruxOKvEi6yDAtDGQYqJpxl3r2oZBrkS9Ts1DRue2dPJBO9bqcLUL63KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پل قدیمی زیوه ‌انگوت اردبیل بر اثر سیل تخریب ‌شد  #اخبار_اردبیل در فضای مجازی
👇
@Akhbarardebill</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/697694" target="_blank">📅 13:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697693">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3wLPQMfzbFZc1osRP0jUVk4jYfutEvIdTmQZyggF33H77Z9Jx93siyv06TTlILDgzaRhKcfItVehKeVtHxlHwJ6vaSI2DouDfMP1_fz4Kb2RBvItGaMSQNUKWJ_JagsIm7ACS6vI6XTmbAbALKIDY2CORrpkBB7mkPpu-0JVHgRYjN-DsGZF7tdwuWNkeEthtwIQsj4j4ZpD2ubzOUR_r4TdAAE-Nq59wghTUpzBq9E2wD5h9js47yPt6mTUECOQDRKVyPoWjW5gv84dltedm8mdwD-hFac_J6c-IlY-ajGhK41_ijNSFOHnjj8ei6A13KIdaShqA1BeghfH2sH0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای ارتش آمریکا برای شناسایی نیروهای ایرانی
🔹
ارتش آمریکا راهنمایی برای شناسایی نیروهای زمینی ایران منتشر کرده که شامل تصاویر یونیفرم‌ها، الگوهای استتار، علائم درجات و تجهیزات انفرادی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/697693" target="_blank">📅 13:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697692">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da07b1b7c3.mp4?token=VuUBZEfgVi6AAKqj8MkAhDuHbTawDFH_eW9b_-WYqXwXCd3kbpiF4nkAez36ixrXieMU8SVFTo6LGSRUrSwII82scl4kL2NSmV8NCRT-Qgd7K2cYRg-KEo83mZLZdx4Fv37Grn9Lj-f059vkkXL0WDuBmb6sVmsoJESFDX-ZwfZ7hGCgefDAXJPzY3172naRIMJOqaui6o83vZfZbjSAKx1RipTouc0ojA9eCeexNPEEa4VCPOzMuRccZ1sJvqL51gZgXsAE0yY9UpInL0MJWs0RsUkaLJ_IQitNpHqIYAaDtwLmqU4FMV6rYthL9WTfr1RIZx9A9PEIx4C8wjzwgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da07b1b7c3.mp4?token=VuUBZEfgVi6AAKqj8MkAhDuHbTawDFH_eW9b_-WYqXwXCd3kbpiF4nkAez36ixrXieMU8SVFTo6LGSRUrSwII82scl4kL2NSmV8NCRT-Qgd7K2cYRg-KEo83mZLZdx4Fv37Grn9Lj-f059vkkXL0WDuBmb6sVmsoJESFDX-ZwfZ7hGCgefDAXJPzY3172naRIMJOqaui6o83vZfZbjSAKx1RipTouc0ojA9eCeexNPEEa4VCPOzMuRccZ1sJvqL51gZgXsAE0yY9UpInL0MJWs0RsUkaLJ_IQitNpHqIYAaDtwLmqU4FMV6rYthL9WTfr1RIZx9A9PEIx4C8wjzwgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلنسکی: همه ما موضوع غلات را فراموش کرده‌ایم؛ باور کنید ظرف دو تا سه ماه آینده، همه درباره بحران کشاورزی صحبت خواهند کرد
🔹
کشورهای قاره آفریقا و برخی کشورهای آسیا و خاورمیانه با کمبود مواد غذایی مواجه خواهند شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/697692" target="_blank">📅 13:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697691">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
ادعای رسانه‌های عبری: در سایه تنش منطقه‌ای، رئیس جمهور آمریکا و نخست وزیر رژیم صهیونیستی چند بار در طی یک هفته گفت‌‌وگوی تلفنی داشته‌اند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/697691" target="_blank">📅 13:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697690">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
روابط عمومی سازمان برنامه و بودجه کشور: در پی انتشار خبری از سوی برخی رسانه‌ها در مورد موکول شدن ثبت نام خوداظهاری کالابرگ به ماه آینده، ضمن تکذیب این خبر، تأکید می‌شود که فرایند ثبت نام متقاضیان در مهرماه در حال انجام است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/697690" target="_blank">📅 13:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697689">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ویدئو پربازدید از خراب شدن موزهای وارداتی که در فضای مجازی پربازدید شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/697689" target="_blank">📅 13:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697688">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JK8osiGsbCQuG_euWq77A18eLnc3xN42RSx2fMbjnBM2C7zcPXeac1FQn71eS5KszrTwqlsezGkLmDCw_6X-Cq8ENn8CeZEqQgCAZGiW06wvINvb1uXRNq9U5ApGuozs_NVrKhw6VPKr-V7ZjiJ4vZy4PKYax2jFTyipEOKukMA8SUtN5iV5EhZTTA9ClEqLHULblC9g0CTQnQHsZmIz7tNa7qx7SEt5mLhIspy9SxNeZ4fzMKHPqIRZUPaxX0mP0PT1f3rSF4RjUU6LMmARX_sM6A-blYppeN7CXAMSquGrDfDkpLxfDxPSmIjGgXs3oRNy1Qp5ze6TP5udfwxzJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از عطر و گلاب تا خواص درمانی؛ با کاربردهای جالب و کمترشناخته‌شده گل‌محمدی آشنا شو!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/697688" target="_blank">📅 13:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697687">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromویکی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtQC2cc6ANCOlq-QpPAJgL3LDizkrXW_juetQy6Z_vVKUJKnQmoRkEn4Vztmus00aQkcYGPFqINJQsM5uQaYQMkduO8L9nz1JfmFTSc-8jSAZqF4fBviIXp0_lwQZ_wrRq7-Wom8V8m-TI0hB8FWYSojPumT2WwQsvig3_JrYse9kYD--SkDfNpm_JanODYE-LM7xQunFYsDI2r5e1tT_r-J25Mx5UhKHy933jik--3Wwb6lc60loXIxFt6IIYYA97HhkHuJ-fgvWOZSUqG2iy47sJRA-yjHLyuM8UL1qXqwv7EnSveQrT7GQ9ap7aFXHBoxGXxBC0H29Ft0_Afvhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وام میلیاردی، جهت خرید خودرو!
🔹
سقف تسهیلات: تا مبلغ ۱۵ میلیارد ریال
🔹
مدت بازپرداخت:  تا ۴۸ ماه
📌
بدون نیاز به سپرده گذاری
📌
بدون نیاز به مراجعه حضوری
📌
با همکاری رسمی بانک‌های معتبر کشور
پشتیبانی :
@wikishopsupport</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/697687" target="_blank">📅 13:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697686">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
بیرانوند ممنوع‌الخروج شد
🔹
سازمان نظام‌وظیفه اعلام کرد تا زمان مشخص‌شدن وضعیت کمیسیون پزشکی علیرضا بیرانوند، او حق خروج از کشور را ندارد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/697686" target="_blank">📅 13:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697685">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
سخنگوی سازمان غذا و دارو: هند از ارسال محموله‌های داروهای اعصاب و روان به ایران با هواپیماهای ایرانی خودداری می‌کند؛ موضوعی که پس از توقف پروازهای مستقیم، تأمین این داروها را دشوارتر کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/697685" target="_blank">📅 12:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697684">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494438b8a0.mp4?token=lVd17zftLmzn1yKDg16yUnSWd87angxSXvsW7iTr4bT27sA9cmFepR6ubcfkXBNsWollPUoUiWtt2t1M22sVEQ-NPOxhLc22Yqves8t-58iO293o-IGcow39O9cOb_AGVtAt4XpwcBOw8OIpKivqReydiiXyXgpir44CWqHujcv_Lkg-W1ZKrL1hKRO08WyyHRBgUCofMNMP9tubPX0bz_nD4yEIuOuU8wmSt-ZTlNhf9-twEw34ZBYHjYJwP5mHWzNi-4A9NIvAFcSi4wOQC_KSdnqWseaJ0Gfo3NB44wXBQjSPTe-86E9Fx1txTvCva2_e_-Gaw7kXuRCoAAkG90nL-8zFazUK6zcXXJLXMsAsPaNTHhbskgeVuGIRQjEjPgt-Jg6ZHWLAj4G8Et-vBDLW2iX8CNW3QmjdswpMWxEJrlLtH8vZoaqcksdS5zwhtXgCNPzAV-RMqVehK3fY-dy_fj9l-6Cxv7CSRs0PzT79T37tQp_GZEoF4_D7VI58LcsgjjEAPFEXlrcLhUbCfi1f3EXzfuUwMMfV8DQD7FUBQP6XEwbvThaV1vRo9EwXHm3j-4V3D4gCKOzrHs1gJtMHRj8D4RpWICXFllfOboGnPbkXb-c5OrMQF9yVzFmnVhGfwLIjs1oitoea1FBrES487wXFZNfB-4QqriUFgh4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494438b8a0.mp4?token=lVd17zftLmzn1yKDg16yUnSWd87angxSXvsW7iTr4bT27sA9cmFepR6ubcfkXBNsWollPUoUiWtt2t1M22sVEQ-NPOxhLc22Yqves8t-58iO293o-IGcow39O9cOb_AGVtAt4XpwcBOw8OIpKivqReydiiXyXgpir44CWqHujcv_Lkg-W1ZKrL1hKRO08WyyHRBgUCofMNMP9tubPX0bz_nD4yEIuOuU8wmSt-ZTlNhf9-twEw34ZBYHjYJwP5mHWzNi-4A9NIvAFcSi4wOQC_KSdnqWseaJ0Gfo3NB44wXBQjSPTe-86E9Fx1txTvCva2_e_-Gaw7kXuRCoAAkG90nL-8zFazUK6zcXXJLXMsAsPaNTHhbskgeVuGIRQjEjPgt-Jg6ZHWLAj4G8Et-vBDLW2iX8CNW3QmjdswpMWxEJrlLtH8vZoaqcksdS5zwhtXgCNPzAV-RMqVehK3fY-dy_fj9l-6Cxv7CSRs0PzT79T37tQp_GZEoF4_D7VI58LcsgjjEAPFEXlrcLhUbCfi1f3EXzfuUwMMfV8DQD7FUBQP6XEwbvThaV1vRo9EwXHm3j-4V3D4gCKOzrHs1gJtMHRj8D4RpWICXFllfOboGnPbkXb-c5OrMQF9yVzFmnVhGfwLIjs1oitoea1FBrES487wXFZNfB-4QqriUFgh4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر چرخش زمین به‌تدریج متوقف شود، چه بلایی سر سیاره و زندگی روی آن می‌آید؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/697684" target="_blank">📅 12:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697683">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون آموزش: صندلی خاص برای فرزندان مسئولان در دانشگاه وجود ندارد
وحید کنعانی، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
شایعات مطرح‌شده در فضای مجازی درباره وجود صندلی خاص برای فرزندان مسئولان در دانشگاه را قویاً تکذیب می‌کنم، بنده خودم نماینده مجلس هستم و فرزندانم در مدارس و دانشگاه‌های عادی تحصیل می‌کنند و هیچ‌گونه تسهیلات ویژه‌ای برای ورود به دانشگاه دریافت نکرده‌اند؛ اگر مستنداتی در این زمینه وجود دارد، ارائه شود تا بررسی کنیم.
@TV_Fori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/697683" target="_blank">📅 12:48 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
