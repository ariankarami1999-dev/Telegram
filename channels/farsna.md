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
<img src="https://cdn4.telesco.pe/file/ouquaWHB3DBYjZAOPjNOk-eGU45xnRTuqpdNHtRoPeu-4L4BcLctl8Gbw7MQBj9cHX8Ua5aCa9JrqHQFUIPOsXZD7ncSouyUhi2HbtgDUt9HMH6ad_RSwVqnIj2kT-AOkMvkMo9oO_SKr9ZmaSKyw_elSW_AIYwzzJFeCTiPSPxSyf7Mt1cB_4kspi3kPf4ry75ejHCmJYnGuW5Q8Pv8DaU8eUf1Nwc_W3cGxsHh7NEEyJl-2qLooy_nDTXBDzL3jXODjaNEWXBWAvkgnpxuHieX_9CVbeSRqG-VOEMQ6NvYynPYA6zc0zNEmv0Xf86TU0SsYk5DSKvaqyIJ2XQnUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 00:39:06</div>
<hr>

<div class="tg-post" id="msg-455404">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4136877665.mp4?token=ZyXADOrIrzn7JamP5YmWH6dAe2QgrGmuFhCyyBHTRgdO9lfQSLiEc-wpxPDhLevoaDP1uNu2MGrGFqT9CMQCFV3A2jbziwV0CmLDkx5P83cHVKMZ7_Y_uFfcqaFBFBBKi-3Sprv1Vgxh1_gM43RibZEMEmjI1MY2qoQu1iQNpoCkGbGpIdUWMjHVSjELzXoMUnACKKHc8KK3uiPlPl5uJ-u0ZUNXiy45ozZzXK1Qi3BzskTEqXFS7AC5KTzZK94xwEtc7PF7nz7eTgB65XkdkBiAhhlLi9myYWO83zbHTJdybfuRAEtlGztXEBasjVuMmHK4RKT7a-B8wlBEuDeA-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4136877665.mp4?token=ZyXADOrIrzn7JamP5YmWH6dAe2QgrGmuFhCyyBHTRgdO9lfQSLiEc-wpxPDhLevoaDP1uNu2MGrGFqT9CMQCFV3A2jbziwV0CmLDkx5P83cHVKMZ7_Y_uFfcqaFBFBBKi-3Sprv1Vgxh1_gM43RibZEMEmjI1MY2qoQu1iQNpoCkGbGpIdUWMjHVSjELzXoMUnACKKHc8KK3uiPlPl5uJ-u0ZUNXiy45ozZzXK1Qi3BzskTEqXFS7AC5KTzZK94xwEtc7PF7nz7eTgB65XkdkBiAhhlLi9myYWO83zbHTJdybfuRAEtlGztXEBasjVuMmHK4RKT7a-B8wlBEuDeA-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ آغاز تحقیقات از متهمان اصلی پروندهٔ حمیدرضا رجب‌زاده
🔹
سخنگوی پلیس: پس از دستگیری متهمان اصلی پرونده «حمیدرضا رجب‌زاده»، تحقیقات توسط کارآگاهان پلیس آگاهی دربارۀ علت و چگونگی وقوع جنایت در جریان است.
🔹
همچنین متهم زن پرونده که درحال فرار و خروج از کشور…</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/farsna/455404" target="_blank">📅 00:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455403">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9IbzrbNAJm3YDHhdWHUe7Y3BPbrYO4qn5ymbv18p1JBmY7q5kKQGLiwaNP8qtpIBwuMP8N1xjWbXibN6lf-wYj_Jrm8ShiceF4iz79hP-Tyr0sG-lDu8piUhi90Y834H_gZJbYbC_jrArU-0rWRtjho5RxMiSpHjdsehMRDaFJFYn-hXoatcdyZ_nUUGobID32mqHUrzvgKOoVyzCbZzmukm8OxSwoQNCBXnRQDx6ka7-Yz4OABt3JqntXZjP95vpGMf0BLZ28FC_nooQPhsohIvQQACq0-sXE-cOwnjSI8fFrkAtJDiqvuUNjjn8ARIwsselwQkrIx-26_Ts69hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: جهان آمریکا را به خاطر انسداد تنگۀ هرمز مؤاخذه کند
🔹
وزیر امور خارجه در گفت‌وگوی تلفنی با همتای آلمانی: ناامنی تحمیل شده بر تنگۀ هرمز منحصرا ناشی از تجاوز نظامی آمریکا و رژیم صهیونیستی علیه ایران است و جهان باید هیأت حاکمۀ آمریکا را به‌خاطر پیامدهای امنیتی و اقتصادی مترتب بر انسداد تنگۀ هرمز مؤاخذه کند.
🔹
امن‌ شدن تنگه هرمز مستلزم توقف اقدامات تجاوزکارانه و مداخلات غیرقانونی آمریکا از جمله محاصرۀ دریایی و دیگر نقض‌های تعهدات آمریکا است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/farsna/455403" target="_blank">📅 00:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455402">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/280903eb5d.mp4?token=IuqGMITqxod-1ZeYs72kAyUO9AIbmF0w3-N38lp3bdvX97gCp-J789XJ-7rGA7Hn7vwdXdVCywa5F2kFs2bXrW7EvNTv4V8JxYsr8LUzrAXfqD-l0N71UgfLOQPwzlEx2IfmvjSu1wlvnVYMRRvwuowqnHBMhz1ItUNFzgzeJ7frgZDpsqwBV_Wd0GgePYArJStWtOrs2Qr5hPXTGRkEFpfh82f1U5yTv7HbFE9QPGq7hFl1qM8iawe7dcSkgfjl_IxD99zeGeIjXQXRQDx7StT39xsubMBA6w6iezNtMKTFgqnvkipfFe0FOkuHHNVOE0m80Qtv_xXtQuVkYClK_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/280903eb5d.mp4?token=IuqGMITqxod-1ZeYs72kAyUO9AIbmF0w3-N38lp3bdvX97gCp-J789XJ-7rGA7Hn7vwdXdVCywa5F2kFs2bXrW7EvNTv4V8JxYsr8LUzrAXfqD-l0N71UgfLOQPwzlEx2IfmvjSu1wlvnVYMRRvwuowqnHBMhz1ItUNFzgzeJ7frgZDpsqwBV_Wd0GgePYArJStWtOrs2Qr5hPXTGRkEFpfh82f1U5yTv7HbFE9QPGq7hFl1qM8iawe7dcSkgfjl_IxD99zeGeIjXQXRQDx7StT39xsubMBA6w6iezNtMKTFgqnvkipfFe0FOkuHHNVOE0m80Qtv_xXtQuVkYClK_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاد شهدای میناب در محفل عزای حرم امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/farsna/455402" target="_blank">📅 23:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455401">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUHepa_Q2_gZCL5UhRcceplOq7vETDbwnQkZCcbHm5kTwUG14XS9HgIzNeSp6a2l9nFP5776co0ZezmbRFBqPR7F2jg1s04Bk4J07YI9fWpKXovxvj0OeHQgfdakygHGGPbgdz4ydIstadmohriP5oIcYeQJ65hMDcEgnERx65r_WiaiOPp_1b16199W-wD_K0lmkre2faQWTLz0u3wLCUxqkzCntJP8R3eUb6Mii-FmfvYGNedo26ZpexZkMzZ4bY_GRmWsRuHygzBOaOC4Z5ZupLgFEBZEdrRUldCvaTaQ3ar0Bkh5xmOFdgeiI8subTVZm4Xri0zOVuwBN4BICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چادر بر تن متهم؛ احترام به حجاب یا اهانت به چادری‌ها؟
🔹
انتشار تصویر متهم زن در پروندۀ قتل حمیدرضا رجب‌زاده با پوشش چادر، بحث دربارۀ پوشش بازداشت‌شدگان را دوباره بر سر زبان‌ها انداخته است.
🔹
استفاده از چادر توسط متهمان را در گذشته هم در پرونده‌های مختلفی شاهد بوده‌ایم.
🔹
یکی از آن‌ها، دختر قمه‌کش شوشتری بود که با موهای باز مشکی‌رنگ در میان اغتشاشگران قمه می‌چرخاند اما بعد از دستگیری با پوشش چادر رنگی  در صفحۀ تلویزیون حاضر شد.
🔹
یا شبنم نعمت‌زاده دختر وزیر پیشین که مانتویی بود پس‌از محکومیت به فساد مالی، در دادگاه‌ها  طوری چادر به ‌سر کرد که فقط بینی‌اش معلوم بود!
🔹
پلیس به فارس گفته ما الزامی برای چادر سرکردن افراد نداریم اما از آن‌جایی که متهم زن باید حجاب شرعی داشته باشد در این پرونده که متهم پوشش نامناسبی داشت مجبور به استفاده از پوششی شدیم که برای این مواقع پیش‌بینی شده و آن هم چادر بود.
🔹
کارشناسان می‌گویند که باید برای پوشش متهمان زن تدبیری ویژه اندیشید؛ اختصاص چادر برای متهمان بدپوشش، از یک سو بی‌احترامی به زنان محجبه بوده و از سوی دیگر شائبۀ مجرم‌بودن زنان چادری را اشاعه می دهد.
🔹
برخی کارشناسان هم می‌گویند باید پوششی دیگر همچون مانتوی ساده و بلند را در ورودی مقرهای انتظامی و امنیتی قرار داد تا متهمان زن درصورت نامناسب بودن وضعیت از آن استفاده کنند که خرید و اختصاص این نوع پوشش نیازمند تغییر قوانین و تخصیص بودجه ازسوی دولت یا وزارت کشور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/455401" target="_blank">📅 23:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455400">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🎥
حماسه خون‌خواهی و میدان‌داری کاشمری‌ها در شب ۱۶۳
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/455400" target="_blank">📅 23:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455399">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8cb4fd355.mp4?token=CH2pjvxM2qUtjtD0eE3i8cWofwS5rLjX8rfRMxPyvAwC9rCkiVTyughNRApsK5b_2_k5Qwlo47v-MoC5g9HkkUxIAeUzgugcacWU8iv3pwQclKlGzahnVH7ykbuC05G71Mm9Vush8G_vHj8keiZ9486RuiwCqNa6jMS-QnFToSO5yupo4PQQwyoGN5T_uMcCQtKSzWtoXvIkcN5DE3wJmZflef2QlAtku11LnHAV_kU4KMjie_XBBpzVnMFUZam-szLiD6gTStvKiszmPJJ07uXXZxLTZcZ1mSAuBtJlTdL_ikHjbeM6W2lFEv2xnEate3S1NjCmMLAAah3rXHnmfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8cb4fd355.mp4?token=CH2pjvxM2qUtjtD0eE3i8cWofwS5rLjX8rfRMxPyvAwC9rCkiVTyughNRApsK5b_2_k5Qwlo47v-MoC5g9HkkUxIAeUzgugcacWU8iv3pwQclKlGzahnVH7ykbuC05G71Mm9Vush8G_vHj8keiZ9486RuiwCqNa6jMS-QnFToSO5yupo4PQQwyoGN5T_uMcCQtKSzWtoXvIkcN5DE3wJmZflef2QlAtku11LnHAV_kU4KMjie_XBBpzVnMFUZam-szLiD6gTStvKiszmPJJ07uXXZxLTZcZ1mSAuBtJlTdL_ikHjbeM6W2lFEv2xnEate3S1NjCmMLAAah3rXHnmfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم خون‌خواهی رهبر شهید بر دستان بروجردی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/455399" target="_blank">📅 23:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455398">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52d79a4d93.mp4?token=EReY_QTf8g9FC0b5gE9rdt0qugnP8YcuRsvRnUBvy9N8nQrS0vHv23U875N48iCz72LdEKrPltfzyFCBZX7hO4HJoNLiVlR0TJ7y_8Iw2AdiS4mU47VqhfkwIuVHGtXp_pkxqv1X-sG0GT59DJ_cqG98ZeseKjg4rzu5zsI_ZvAT0zjUCPwCpz8eNOU6onYrwWyyTEfOrPp0BGbuk4iXPlAgiD7QuwnT-W2UOqH8BEMBiImltqP6o11o739r9IBGRSYKBlVIEFbz30Nv2Ch3uyqwoBQIQwMawMrznEsz-majO0sHrjCpgEK2p9DCMJU0R7d6mlg3IydFsXFCkz_tZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52d79a4d93.mp4?token=EReY_QTf8g9FC0b5gE9rdt0qugnP8YcuRsvRnUBvy9N8nQrS0vHv23U875N48iCz72LdEKrPltfzyFCBZX7hO4HJoNLiVlR0TJ7y_8Iw2AdiS4mU47VqhfkwIuVHGtXp_pkxqv1X-sG0GT59DJ_cqG98ZeseKjg4rzu5zsI_ZvAT0zjUCPwCpz8eNOU6onYrwWyyTEfOrPp0BGbuk4iXPlAgiD7QuwnT-W2UOqH8BEMBiImltqP6o11o739r9IBGRSYKBlVIEFbz30Nv2Ch3uyqwoBQIQwMawMrznEsz-majO0sHrjCpgEK2p9DCMJU0R7d6mlg3IydFsXFCkz_tZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع موج ۱۶۳ در چهارمحال‌ و بختیاری با نوای نوحه‌ و سینه زنی همراه شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/455398" target="_blank">📅 23:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455397">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lplJ6F1x8n57_I0HK1mJtJadSqamTbvoke8Yn-lWmUZTDT42RsNu2iJXOgRht4L4lZy8U56B_ecemvoz96nY_gnur04qO-xY_piFLrtvB5uRQS2KXT4tcjtQ9HDQi0jMvj0BGj4ntSaBsP1JM0UnF5QbNmu6R7LYMD5b862E03cQVjWbSiTV3S-F0PUz6zztWxbPbWN3RXhRNDC5skMNvONFuKTC-ny3CDO2WVseWVzMQ5rgmmXqHP1Kj8gntZQF-CuK4j_Wqa98s5_GWWPNFm91_r1gOVBILJxo_-nQEw2oX8LXfs4hmp_h01oHtWpFuSVkIgme52-sbmJzEPCUmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاج: قصد داریم قرارداد قلعه‌نویی را برای جام ملت‌ها تمدید کنیم
⚽️
اعضای هیئت‌رئیسه اعتقاد داشتند که باید برای جام ملت‌ها جوانگرایی صورت بگیرید که این نظر خود قلعه‌نویی هم است.
⚽️
پاداش آقای قلعه‌نویی به‌عنوان سرمربی تیم ملی ۷۰ میلیارد تومان بوده است.
⚽️
در فیفادی پیش‌رو ۳ بازی تدارکاتی انجام خواهیم داد؛ بازی با روسیه قطعی شد؛ ۲ تیم اروپایی و یک تیم از آسیا که در جام جهانی هم حضور داشتند حریفان تدارکاتی هستند.
@Farsna</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/455397" target="_blank">📅 23:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455396">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4cf20f78.mp4?token=C1eWvLuRniDee2ii5tRbhlISlDhljWNvsYYUZPLOjDAznryNRgiZZxZOzYZUp0e_8j8-4SpVfki_WxYvpG-iaVkSzJR8KZTyMxWMXjlsGQlr1eSSEFciUsYi6Mar2Z_qLs7DDf9nHeEBlCBk58NemPaBFnmtJNTizoKSVuBnbWO5EyF9AeVfhRlB8WmvQbkDM2vAnq04odSbmpmS4YuoW-JSVC4O8jo_OvbkeYmEMV0ONpuEvPT-1g3rLwQog60Hi_dlZAx1BSdnmCdMOOtgAupwFwPWr1HcIz83XBcog2A6uFrPUrEDTFtwfIfpWOlQU6Z11tevAcy3lLADG5TdPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4cf20f78.mp4?token=C1eWvLuRniDee2ii5tRbhlISlDhljWNvsYYUZPLOjDAznryNRgiZZxZOzYZUp0e_8j8-4SpVfki_WxYvpG-iaVkSzJR8KZTyMxWMXjlsGQlr1eSSEFciUsYi6Mar2Z_qLs7DDf9nHeEBlCBk58NemPaBFnmtJNTizoKSVuBnbWO5EyF9AeVfhRlB8WmvQbkDM2vAnq04odSbmpmS4YuoW-JSVC4O8jo_OvbkeYmEMV0ONpuEvPT-1g3rLwQog60Hi_dlZAx1BSdnmCdMOOtgAupwFwPWr1HcIz83XBcog2A6uFrPUrEDTFtwfIfpWOlQU6Z11tevAcy3lLADG5TdPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۶۳ شب پایداری گنابادی ها در حمایت از وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/455396" target="_blank">📅 23:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455395">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8836ef1e8e.mp4?token=u0GX4a3GNCeGGq28XXbolKSENuPkHmQ5plFxQcDA_kfRXlUoE_YvweXE5pOTeH450hJBrneaGE9C0o930NnoTvgr8vdbCBI1EAQthxXLD8OmDWQJunpCsuzQlWEx8oCpZJu91sehr9oLhXwdqJOyAY9aG53_fhGriVl5OrBq9rMd_NJ_Nv0u5CQeDpC7huIvfhRs4veyj4Nfq-kJVxwnXYb8lzDyI5lBbZK7TR68za_J93xYwaZbZ1mPONP0CLVAD9yb2oCa54uSh9NWPYnplqnToecceh-LWCd7QpyE6l2Al4tRYwr_n-yytfle6Xqgqj05cqyQXKtyC_neMWWe1U0V7s1jEEZWV7ttrF7dOmhELOjYem9X5xAyh4KuiDj4e68oWts4a_uStY7eVevpNj54Y8AVSej7g9rBBHk4PfayC5u7SLDoe1r-NbnvchNrknSbMPaoEFcMzeQEZXpcoXMo4641YuFn36ZGbs6qowSO2iyl-sx65TUODBLwoBs_MKSD7X89ipvT2LB7GV-8eKVioFCu955WNjCZSgTK6z2hoD1mdbzvEILxtTiyLkNkyNr_XDaN5uYVScO7yeI3tjUKbd4nyqsCq6W3aHiPNJE1iUTxdLp8aHBSUxWPREDR8dJj5wf6iSGP8GgdwdKtt4plJFafXXxMvyKvsKIODno" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8836ef1e8e.mp4?token=u0GX4a3GNCeGGq28XXbolKSENuPkHmQ5plFxQcDA_kfRXlUoE_YvweXE5pOTeH450hJBrneaGE9C0o930NnoTvgr8vdbCBI1EAQthxXLD8OmDWQJunpCsuzQlWEx8oCpZJu91sehr9oLhXwdqJOyAY9aG53_fhGriVl5OrBq9rMd_NJ_Nv0u5CQeDpC7huIvfhRs4veyj4Nfq-kJVxwnXYb8lzDyI5lBbZK7TR68za_J93xYwaZbZ1mPONP0CLVAD9yb2oCa54uSh9NWPYnplqnToecceh-LWCd7QpyE6l2Al4tRYwr_n-yytfle6Xqgqj05cqyQXKtyC_neMWWe1U0V7s1jEEZWV7ttrF7dOmhELOjYem9X5xAyh4KuiDj4e68oWts4a_uStY7eVevpNj54Y8AVSej7g9rBBHk4PfayC5u7SLDoe1r-NbnvchNrknSbMPaoEFcMzeQEZXpcoXMo4641YuFn36ZGbs6qowSO2iyl-sx65TUODBLwoBs_MKSD7X89ipvT2LB7GV-8eKVioFCu955WNjCZSgTK6z2hoD1mdbzvEILxtTiyLkNkyNr_XDaN5uYVScO7yeI3tjUKbd4nyqsCq6W3aHiPNJE1iUTxdLp8aHBSUxWPREDR8dJj5wf6iSGP8GgdwdKtt4plJFafXXxMvyKvsKIODno" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجدید بیعت گرگانی‌ها با ولایت و انقلاب در ۱۶۳ شب حماسه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/455395" target="_blank">📅 23:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455394">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3156abfe8c.mp4?token=qmuNiDvxDn6l5WlOLdf8gpFTDdooR1ZmyQld-49aZbFEuTuMZPTF-lxxBGo34EgCADDXB016WyJ3rPDHXhDSyFQkxf3pYyqZlAQ3TtgEOKhhRXQ996P1Pomg9WAc13B6iqxLNuNP5Q-cFWThhMxlFD8AqxIXKzI2ZIOzAw9-Nla0P8rwtEevQuoB5DZj34WYEuXyyPyNo3NP2u8FOGd1rv4lj0XRHNTnWKWugXIA7pgcu6BeWyHDzYfihLBe6tiyFJCCVxTZVnwRr6ZhEoZ5X0td71oQ2jdV89aUGP6NDUzHZnIsjgd8ODi7nclhxQHlhdJD54ci35V1-Rn0w2rr9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3156abfe8c.mp4?token=qmuNiDvxDn6l5WlOLdf8gpFTDdooR1ZmyQld-49aZbFEuTuMZPTF-lxxBGo34EgCADDXB016WyJ3rPDHXhDSyFQkxf3pYyqZlAQ3TtgEOKhhRXQ996P1Pomg9WAc13B6iqxLNuNP5Q-cFWThhMxlFD8AqxIXKzI2ZIOzAw9-Nla0P8rwtEevQuoB5DZj34WYEuXyyPyNo3NP2u8FOGd1rv4lj0XRHNTnWKWugXIA7pgcu6BeWyHDzYfihLBe6tiyFJCCVxTZVnwRr6ZhEoZ5X0td71oQ2jdV89aUGP6NDUzHZnIsjgd8ODi7nclhxQHlhdJD54ci35V1-Rn0w2rr9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گردهمایی بزرگ اندیشمندان شیعه و اهل سنت در حرم امام رضا(ع) در آستانه رحلت پیامبر اکرم(ص)
@Farsna</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/455394" target="_blank">📅 22:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455393">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آژیر هشدار آزمایشی فردا در جاسک هرمزگان به صدا در می‌آید
🔹
به منظور آمادگی و ارزیابی عملکرد تجهیزات، تست آژیر هشدار توسط نیروهای نظامی از ساعت ۱۰ صبح سه‌شنبه در سطح شهر جاسک انجام می‌شود.
🔹
این اقدام صرفاً یک مانور و تست فنی است و هیچ ارتباطی با وقوع حادثه یا شرایط اضطراری ندارد و شهروندان نگرانی نداشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/farsna/455393" target="_blank">📅 22:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455392">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c800cb1309.mp4?token=Z1IgtI9tTo3tF5uz3scUVcA3rwj03MlsLtjwcVmp1pfBTIzNc63msbOV4sHc4UgqZOA_RCS9RZqFkCC_AruOrDY7sROwjXiR2pC8lP6_SuSQtXYTVhGu5TNSkdWcfCYRAMA-S0TtgUXqP4kbOgt7d_MHDw-anyf4XD6-r9vbSpvGg5lak3WikqOqIcGPx9Fsl1tqrRSS0KOfZdQD-ak94deANaROq4gq457IVjZMivc-XF2MkO6xV06UxT8coIYAFN4nTyZodP10GOaQE5x540xdM2heQz5y_8xb1DcRwVJYH0OuIdaPF1h3cvQus13CUsSQbdDhnHuKZUlcIvSwRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c800cb1309.mp4?token=Z1IgtI9tTo3tF5uz3scUVcA3rwj03MlsLtjwcVmp1pfBTIzNc63msbOV4sHc4UgqZOA_RCS9RZqFkCC_AruOrDY7sROwjXiR2pC8lP6_SuSQtXYTVhGu5TNSkdWcfCYRAMA-S0TtgUXqP4kbOgt7d_MHDw-anyf4XD6-r9vbSpvGg5lak3WikqOqIcGPx9Fsl1tqrRSS0KOfZdQD-ak94deANaROq4gq457IVjZMivc-XF2MkO6xV06UxT8coIYAFN4nTyZodP10GOaQE5x540xdM2heQz5y_8xb1DcRwVJYH0OuIdaPF1h3cvQus13CUsSQbdDhnHuKZUlcIvSwRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کنوانسیونی که زبانِ رضا پهلوی را دراز کرد
🔹
همزمان با بحث‌ها درباره کنوانسیون رژیم حقوقی دریای خزر و در حالی که دولت مسئولیت نهایی آن را به مجلس واگذار کرده، رضا پهلوی نیز با فرصت‌طلبی خود را مدافع تمامیت ارضی ایران نشان داده است؛ موضعی که با سابقه خاندان پهلوی در حاتم‌بخشی بحرین به عنوان بخشی از خاک ایران و مواضع اخیر جریان سلطنت‌طلب در تضاد است.
🔹
رضا پهلوی که در اواخر اردیبهشت امسال، برای نام بردن از دریای خزر از واژه «بحر خزر» استفاده کرده بود، امروز شهامت پیدا کرده و با اقدامات نمایشی و نوعی ملی‌گرایی قلابی، نام «دریای کاسپین» را به زبان آورده و به خود اجازه می‌دهد تا درباره تمامیت ارضی ایران و پیامدهای حقوقی این کنوانسیون سخن بگوید.
🔹
نکته جالب توجه اما تناقض و رویکرد دوگانه پهلوی‌چی‌ها در قبال منافع ملی و تمامیت ارضی ایران است. این جریان در طول ماه‌های گذشته دائماً ادعا می‌کردند که ایران هیچ حق و حقوقی برای مدیریت تنگه هرمز ندارد.
🔹
به‌عنوان مثال مدیر تیم رسانه‌ای رضا پهلوی و دبیر خبر سابق شبکه سلطنت‌طلب منوتو، بستن یا کنترل تنگه هرمز توسط ایران را ناقض قوانین بین‌المللی دانسته و آن را نفی کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/455392" target="_blank">📅 22:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455391">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/108142470c.mp4?token=Mqqg-2Gz8i4j87fIbtpanp6egLibv8ZPkm31QPA1x5hto969bGcP6bU1AnjV9ixvPmKOQx2KE4ALtNWqJQl9CLD1rBwoCiHdvCsTS6T3cghgmC8CxIUoPmpqZ46Pw-aIxxMx_uhvZzCcira6fSmRVE-MuBZHIeVIlMIg97RYtn8LpbgvCCuewkg6kmXJZ5YwAZQJdFMvCQrYDYRJMwDlPrAk6cCr_rxiqkGIU-SvLn0JOYFSv9txUE8xenGWUfCjrAdID-SIddCftulpMJOIfqBkVGroRk1b-tL3t2M18wkiV9GjQ_Su4YPP6Up6YwnpZog7Vor_lpr7Bmg5XevjxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/108142470c.mp4?token=Mqqg-2Gz8i4j87fIbtpanp6egLibv8ZPkm31QPA1x5hto969bGcP6bU1AnjV9ixvPmKOQx2KE4ALtNWqJQl9CLD1rBwoCiHdvCsTS6T3cghgmC8CxIUoPmpqZ46Pw-aIxxMx_uhvZzCcira6fSmRVE-MuBZHIeVIlMIg97RYtn8LpbgvCCuewkg6kmXJZ5YwAZQJdFMvCQrYDYRJMwDlPrAk6cCr_rxiqkGIU-SvLn0JOYFSv9txUE8xenGWUfCjrAdID-SIddCftulpMJOIfqBkVGroRk1b-tL3t2M18wkiV9GjQ_Su4YPP6Up6YwnpZog7Vor_lpr7Bmg5XevjxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رگبار تابستانی با رعدوبرق در آسمان مازندران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/455391" target="_blank">📅 22:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455390">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8bd9832e9.mp4?token=KyWQR0vk9xnbPQJS_Bu9vh1-7aqVdVFHH9OZv574MjeAu5pKCwxS1ni2sjadANZLz2lZnYr1yT2_Fu58TicYCKbNg9Wn9JUI75FzrS44v-qzlbXb7twbM2d-Ky6iggxFnQrtCdHlWbWcNRIlCDlnmu_HZhArVk0nqUf-xpD1Pty1UlKZU2C8gXyVl4V3i3uhRtWYI63hU9lPqzl5x8nDm7nf4oQ99KyiHW08J4e3YA_7x-UvLxvWD7p_cGhsojg33VRHERfDsrCO8ZBcjR5sREjex1y4VPBDCgCeYUKMGOsAM0pKSssfEyFPFTtPU2kXZj2ogohh5XOkvqsj343wdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8bd9832e9.mp4?token=KyWQR0vk9xnbPQJS_Bu9vh1-7aqVdVFHH9OZv574MjeAu5pKCwxS1ni2sjadANZLz2lZnYr1yT2_Fu58TicYCKbNg9Wn9JUI75FzrS44v-qzlbXb7twbM2d-Ky6iggxFnQrtCdHlWbWcNRIlCDlnmu_HZhArVk0nqUf-xpD1Pty1UlKZU2C8gXyVl4V3i3uhRtWYI63hU9lPqzl5x8nDm7nf4oQ99KyiHW08J4e3YA_7x-UvLxvWD7p_cGhsojg33VRHERfDsrCO8ZBcjR5sREjex1y4VPBDCgCeYUKMGOsAM0pKSssfEyFPFTtPU2kXZj2ogohh5XOkvqsj343wdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رونمایی سپاهان از لباس خود در فصل جدید با الهام از نمادهای ایرانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/455390" target="_blank">📅 22:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455389">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs6I-kTfPHR0AliFsOtJDp-Lke8lAmpixlRCO-tQE91c5s_Q1ge7-YqXzTrXA0hJ71AhZHNB44SuQZx-rHd9GGIRtk99wWO5cSUKDG0Timr5klwqA-oNt2FHMIGve9KMhIe9gJZKZ4PxF4uxsw_gZi3sjW_Lln-Y7HKWgimo8_Q7xpogISODOmLde8LAyYDcVfhA8NOsIyFL0OBhZY99wkiRNGVuHfAvNxXOG1y_6vPIy_QvdBbBUoWGEgjUhkzGom_diJFfvgHzvwXaphqEKTGL_W8nL0_yjeFTxkhEbLR3-kt9BKDW7QcSvQl6ddC2zAIAaqypuVlCytdiOHYxoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظامی سابق آمریکا: روند خروج ما از منطقه آغاز شده
🔹
اسکات ریتر، نظامی بازنشستۀ آمریکایی: ارتش آمریکا بخش قابل‌توجهی از ذخایر موشک‌های دورایستا و مهمات دقیق خود را مصرف کرده و ذخایر تاماهاوک نیز کاهش یافته.
🔹
در نتیجه آمریکا برای حمله به اهداف عمیق در داخل…</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/455389" target="_blank">📅 22:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455388">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f2acbb8c.mp4?token=fl4-HJtCLHmZTY0Is4oSBUdJMhXQJkwInksHNqbqfh1g97HMlpX7uPjaT_lGnNrbeyWmehTwLJq3l0-uuLVjf0YWxgM6mHfRwEMqhENHRT-swV-TddFrNnhz4sn6bLpzzYc51CRjo4XWmzlYivv8sS0woAyocGj0RB6lBjR71cy0F2tg7BxF2RdX9soQ6ohmCFri-ejIugwPDtMav4hdVXB1125Xf9DRUecNFUQ_3YmiLvFkjPe98W9RaPOlc3RILOZ2vt0bjeZc9mc3s2suOUbqJpI4F6uq-UnsoOy70C39wltbAm-KXziCnFrOVlq22bSoYFBdVvK8WnMZFCppag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f2acbb8c.mp4?token=fl4-HJtCLHmZTY0Is4oSBUdJMhXQJkwInksHNqbqfh1g97HMlpX7uPjaT_lGnNrbeyWmehTwLJq3l0-uuLVjf0YWxgM6mHfRwEMqhENHRT-swV-TddFrNnhz4sn6bLpzzYc51CRjo4XWmzlYivv8sS0woAyocGj0RB6lBjR71cy0F2tg7BxF2RdX9soQ6ohmCFri-ejIugwPDtMav4hdVXB1125Xf9DRUecNFUQ_3YmiLvFkjPe98W9RaPOlc3RILOZ2vt0bjeZc9mc3s2suOUbqJpI4F6uq-UnsoOy70C39wltbAm-KXziCnFrOVlq22bSoYFBdVvK8WnMZFCppag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقوع انفجار در یک مخزن سوخت در لیبی
🔹
منابع خبری گزارش دادند چندین انفجار در یک مخزن سوخت در پالایشگاه الزاویه در لیبی رخ داده است؛ هنوز علت انفجارها مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/455388" target="_blank">📅 22:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455387">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaOVLOj5U3W3Kn8IgmzJ4IELMW_iQyeHLiAQR7bSHWR9tf_BzR_Yvbr2DIA7bX05Y0JmeBpBzLIrR2qs3mU3pNXueMXhrlHjq4EXk1QZK4yBab-EhWe6HjL_n4rwWl2CE1c0bJpp4PdK_oPzG734ytIJu-skrF08HdF5Z_HaJRHiDjRMtmhhvbh2r-mk9sTVUBfHtfbpb7Kw0L8xrtH5K_g1WzlRsOmKHqfPNX_qCnhBdnslQlY7GKfyAo99c8CGCbzctQKd-hr_Fhrg3JOi34A-ICQElanh32SfarniN0Pa7NZDE9nuNWUgFrDSh-vkO0UaIe7deWgj-Y2U70afSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ بدهی ۲۲ میلیاردی، برق از سر کشتی پراند
🔹
پیگیری فارس از توانیر مشخص کرد، علت قطعی برق مجموعۀ متعلق به فدراسیون کشتی بدهی ۲۲ میلیارد تومانی به صنعت برق بوده.
🔹
البته فدراسیون کشتی گفته این بدهی برای به ورزشگاه آزادی است.
🔹
طبق آنچه وزارت نیرو می‌گوید، هفتۀ…</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/455387" target="_blank">📅 21:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455386">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIQU2SCBmEjR1AmjhJ7L4NqawwgYtf4JJD2IHo-UfJKC3IEiFat4SWROEV2A14ndO2d1dvxSZHJjf1bDHepTD1uqOAp4X6-W2gk__bOjdwxXb5Pb7PJk1DhqPytyLH1kMeP8G1EY7fQu5LJ8tf1pIdLErexxONTPRoIxWC4XNs8F1-1VuZ4RGPoqEIGCHud2Eyb8NBJ9sBtcrTUSiRIPdF6DdEZIsjBIHxwHaT61ZpwqzD3wac9wGWBi9-5qpAm-LcTbplbtyWL2ZTHD76cOZr0XDKXhM6LXcCDQG-OUxrO3GTI6JtfNiI9esUw7A3-RtU45T7FXtG4Pho_Sy6aF0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظامی سابق آمریکا: روند خروج ما از منطقه آغاز شده
🔹
اسکات ریتر، نظامی بازنشستۀ آمریکایی: ارتش آمریکا بخش قابل‌توجهی از ذخایر موشک‌های دورایستا و مهمات دقیق خود را مصرف کرده و ذخایر تاماهاوک نیز کاهش یافته.
🔹
در نتیجه آمریکا برای حمله به اهداف عمیق در داخل ایران با کمبود سلاح‌های دورایستا مواجه است.
🔹
آمریکا عملاً در مسیر عقب‌نشینی تدریجی از غرب آسیا قرار گرفته؛ هرچند ترامپ احتمالاً حاضر نخواهد بود این روند را به‌صورت علنی با عنوان «عقب‌نشینی آمریکا» اعلام کند.
🔹
حتی ممکن است برخی دولت‌های منطقه نیز دیگر تمایل چندانی به تداوم همان ترتیبات امنیتی سابق نداشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/455386" target="_blank">📅 21:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455385">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f39aca476.mp4?token=pVkuqeK3h6dKMr4-jjJTI8_90HL8LAH-lcPndcyNFSwy3T8TJ1Uk4NomUokuv1aEroBzJeCL8pV2UI-Qv6UZui8dbi-a6X7yoNFUBoU8h9HUHehUppn9272hcrnQOL1Efy8AMCeYI32ogGTFRNlBzf0r220TPynWd11Im2UTw1XJMHWUjMAfsGvtD-nt17kHDitdlTm0K0tPljtbHcSFSTRuvwhSpxHsIOIwnkRvegk4f1Ti8wvhzTrOsjuQnQ23fv4mpqa3va7_KjmiUaF9Csdge4mdJIMDZGsLoloeOx0c83FkIetB9S6V8lvySZoRphjmqNQwOFPakzYvT6U-yE8sxV7VIm668hMz0WM7lQrMSJJiHc4j6SLsEkT5oJwvMqtRkLqqe2ZPGcgwQvkr9_Giym16wav2kRf7YIZ4CJ6PMp-nnYkqCF-fVi2bjivA4mSqBTivGtdfRRwu8j9kqdjSZRDy0QN5xgOBLeBQp_QmvgmOXbyIIHw7fJc1XGUyBKMSuueX0finA0dtrCCY11fVeebFHVueJcHByv47hCRIBkELQTWx8MZUkwzbDZo_Tq-4a4fTn2tU7pa6Su8EHEDE_eTOkNBxUWR_RcsajCn7kiMT5K9IHChhaxwzR7UvIVi2IwD5l2XI6pyhC46PyKCKvxLhg117HPDn16r8Pxc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f39aca476.mp4?token=pVkuqeK3h6dKMr4-jjJTI8_90HL8LAH-lcPndcyNFSwy3T8TJ1Uk4NomUokuv1aEroBzJeCL8pV2UI-Qv6UZui8dbi-a6X7yoNFUBoU8h9HUHehUppn9272hcrnQOL1Efy8AMCeYI32ogGTFRNlBzf0r220TPynWd11Im2UTw1XJMHWUjMAfsGvtD-nt17kHDitdlTm0K0tPljtbHcSFSTRuvwhSpxHsIOIwnkRvegk4f1Ti8wvhzTrOsjuQnQ23fv4mpqa3va7_KjmiUaF9Csdge4mdJIMDZGsLoloeOx0c83FkIetB9S6V8lvySZoRphjmqNQwOFPakzYvT6U-yE8sxV7VIm668hMz0WM7lQrMSJJiHc4j6SLsEkT5oJwvMqtRkLqqe2ZPGcgwQvkr9_Giym16wav2kRf7YIZ4CJ6PMp-nnYkqCF-fVi2bjivA4mSqBTivGtdfRRwu8j9kqdjSZRDy0QN5xgOBLeBQp_QmvgmOXbyIIHw7fJc1XGUyBKMSuueX0finA0dtrCCY11fVeebFHVueJcHByv47hCRIBkELQTWx8MZUkwzbDZo_Tq-4a4fTn2tU7pa6Su8EHEDE_eTOkNBxUWR_RcsajCn7kiMT5K9IHChhaxwzR7UvIVi2IwD5l2XI6pyhC46PyKCKvxLhg117HPDn16r8Pxc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب دربارۀ  هدیۀ مرحوم فرشچیان: هر وقت این تابلو را نگاه کردم، گریه کردم
🔹
استاد فرشچیان: از امام حسین(ع) حفظ تمامیت ایران از خلیج فارس تا شمال و از شرق تا غرب و سلامتی هموطنانم را می‌خواهم
@Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/455385" target="_blank">📅 21:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455384">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/232f89712b.mp4?token=GUupvkEqAngilMCRlGSd6Dn9u8DWtVdV74oSnS2VlGsp9iq7aG6rqa2_Ru_qRba-GZNpPk4FLdvpvvcgwdYCYanPPLWbbdTMjHIzluIs9YtzTxD2oVyyYygU96bgUg7CKd9zWrKe3rREXeFe5NyOymTDZ2Z941mAgnPRQcVzp8fs9saaWoLcPdyF4wppeCwwK7r2yKExKlQJgIvXBWn_jjxvyyfZrX69Frtz6-p0byDSID1maoG5l1gRg3lJ-oXPwzW8I-Xs7GETAcYh1n6vwQxkt05LsyOQL9Tyg970MBoHujl4obRsOXjVItSS6hXqPtfoOuvWnzdXOz_im4OTD4C8hjTaw_3a9rFBCGOmBXkw3WGx-GzR03oNMYgPc7BtS7bh6tNVtiapgFDv2kEMMjsUxuIhqgZ_MeQ7HP5c56sp41ntZrfFykhd_IruUIIknoVzYYX-mQuCFV3HE_SvmtnMTJPz7KnS3sYXyVQmhtqBkcVVjKOoWOFst2WTWDhJIPNoNEKh5uDopRdRzUm7h0Yev_Fh9tCfb47jjahO17Q8zBHql1AyduR2WgnrMdVlABKwOSxbKOA6tKKbtVv-obst7DR1uLzuUNFWp_5Rk6joya1ILoTNc-7-WygrEHDFNm4oQ1tYTh_Pb-6Qg6Nf6amLnNS50eK8B65dImCAnnc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/232f89712b.mp4?token=GUupvkEqAngilMCRlGSd6Dn9u8DWtVdV74oSnS2VlGsp9iq7aG6rqa2_Ru_qRba-GZNpPk4FLdvpvvcgwdYCYanPPLWbbdTMjHIzluIs9YtzTxD2oVyyYygU96bgUg7CKd9zWrKe3rREXeFe5NyOymTDZ2Z941mAgnPRQcVzp8fs9saaWoLcPdyF4wppeCwwK7r2yKExKlQJgIvXBWn_jjxvyyfZrX69Frtz6-p0byDSID1maoG5l1gRg3lJ-oXPwzW8I-Xs7GETAcYh1n6vwQxkt05LsyOQL9Tyg970MBoHujl4obRsOXjVItSS6hXqPtfoOuvWnzdXOz_im4OTD4C8hjTaw_3a9rFBCGOmBXkw3WGx-GzR03oNMYgPc7BtS7bh6tNVtiapgFDv2kEMMjsUxuIhqgZ_MeQ7HP5c56sp41ntZrfFykhd_IruUIIknoVzYYX-mQuCFV3HE_SvmtnMTJPz7KnS3sYXyVQmhtqBkcVVjKOoWOFst2WTWDhJIPNoNEKh5uDopRdRzUm7h0Yev_Fh9tCfb47jjahO17Q8zBHql1AyduR2WgnrMdVlABKwOSxbKOA6tKKbtVv-obst7DR1uLzuUNFWp_5Rk6joya1ILoTNc-7-WygrEHDFNm4oQ1tYTh_Pb-6Qg6Nf6amLnNS50eK8B65dImCAnnc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید دههٔ‌ هفتادی که الگوی مدافعان حرم ایران شد
@Farsna</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/455384" target="_blank">📅 21:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455383">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b27a8c503.mp4?token=AkfdEfyNX1u_4mHKg2WfeUo7B5n44WD-FVXXeKfUrkYAml_Szi8Eom5wNHg6TB5dOv1oFl5OZ9ZOOR2usMZf1Xo25X06xko-rn-Yp4Xzj-kRmountzKYqqz5g5Xp0hCnJMydjR5jmA4CxlW6Zo6lRWPijdNbY8J3HyTebtdMWgBC5Ts0u5ferEaBKh20tOnUOVr0LVjjiZ02lmFDZXauIFIwa4OBIIKz_7H1dr4Zra1xIjlxdstNLsiWU0O12oSk7-ZD0MRCgnl75nhjZyKsoCshFxUW08F92gv_K1xN1EWADqiHrQ5e0WLdH5JBWYThiccQWpjVY6uMhC7aJ9_LCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b27a8c503.mp4?token=AkfdEfyNX1u_4mHKg2WfeUo7B5n44WD-FVXXeKfUrkYAml_Szi8Eom5wNHg6TB5dOv1oFl5OZ9ZOOR2usMZf1Xo25X06xko-rn-Yp4Xzj-kRmountzKYqqz5g5Xp0hCnJMydjR5jmA4CxlW6Zo6lRWPijdNbY8J3HyTebtdMWgBC5Ts0u5ferEaBKh20tOnUOVr0LVjjiZ02lmFDZXauIFIwa4OBIIKz_7H1dr4Zra1xIjlxdstNLsiWU0O12oSk7-ZD0MRCgnl75nhjZyKsoCshFxUW08F92gv_K1xN1EWADqiHrQ5e0WLdH5JBWYThiccQWpjVY6uMhC7aJ9_LCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: اگر مردم در عمل ببینند ما صادق و صحیح‌العمل هستیم، تحملشان بیشتر می‌شود؛ حتی اگر مشکلشان حل نشود.
@Farsna</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/455383" target="_blank">📅 21:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455382">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b060ea1bb5.mp4?token=ZiOT_1vPtuSyLorrPQ5C8IxxSgrEcISTeArp-unzPu3nu3bv6Rihw-jBE7MxTXNRGtyDmU7OuHAslnUp04-Cmm-8eK08DCxAnSwnLuMrFBPnqPKNGegYIdyVav19eK3zXI5IcpaxuAN2W_r-7iQJQRtrOfDsssjLLSmy13r_dEbRLtlDi_O_GWOABObGyxxRu_IzD9At1wFEKmAYZNPGiEy02B6IrLiGxDlMuwRrGFeEjGtKlFy-aT3MnQwe7nJ3d-dpkEtWnANLbJTBQJ4Q899zetV4VQDeJ859VqFG-YZDRcVuccE_sRwwYXspfLMcFr8jhrx-iF9NOQy6FP_WroCzjScfrsUdjQO7EvYlLqPAsNzyeA3-26IkjMnhe78BQ2L8YNxQV8MuYR18BBKFio3nXZ8wDb12fy5EDRdLY2Tj3RMSz0JenzQqJ6raWzyzib5vQs8ruwrMdHLye07aO0tM8ooSHaAWY3EFI7WmVCDI5p-Cc5QMFgqjIGh3o4uUunnZZjxeJPLHWAo5d_AtlaNLw06Ek_luD6yPfBCqJYNf_cHgAEksjUvpJsvwY_F70mMxYPEGSSdGuy0bFqErHSD0pBkKPxryEhO3Rxwz_wrB4dn-unIdczg3mY2HOe0FOoCNJbvirDs7Cp7JS5XZSBNRWdQTRosknf-I1Hoej70" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b060ea1bb5.mp4?token=ZiOT_1vPtuSyLorrPQ5C8IxxSgrEcISTeArp-unzPu3nu3bv6Rihw-jBE7MxTXNRGtyDmU7OuHAslnUp04-Cmm-8eK08DCxAnSwnLuMrFBPnqPKNGegYIdyVav19eK3zXI5IcpaxuAN2W_r-7iQJQRtrOfDsssjLLSmy13r_dEbRLtlDi_O_GWOABObGyxxRu_IzD9At1wFEKmAYZNPGiEy02B6IrLiGxDlMuwRrGFeEjGtKlFy-aT3MnQwe7nJ3d-dpkEtWnANLbJTBQJ4Q899zetV4VQDeJ859VqFG-YZDRcVuccE_sRwwYXspfLMcFr8jhrx-iF9NOQy6FP_WroCzjScfrsUdjQO7EvYlLqPAsNzyeA3-26IkjMnhe78BQ2L8YNxQV8MuYR18BBKFio3nXZ8wDb12fy5EDRdLY2Tj3RMSz0JenzQqJ6raWzyzib5vQs8ruwrMdHLye07aO0tM8ooSHaAWY3EFI7WmVCDI5p-Cc5QMFgqjIGh3o4uUunnZZjxeJPLHWAo5d_AtlaNLw06Ek_luD6yPfBCqJYNf_cHgAEksjUvpJsvwY_F70mMxYPEGSSdGuy0bFqErHSD0pBkKPxryEhO3Rxwz_wrB4dn-unIdczg3mY2HOe0FOoCNJbvirDs7Cp7JS5XZSBNRWdQTRosknf-I1Hoej70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی مو‌سفیدان سیاست دور یک میز جمع می‌شوند
@Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/455382" target="_blank">📅 21:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455381">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b228c55ff.mp4?token=urGQ5WMjz1LLOJ075CKTTt-8WvgkATq3_Jx0pbnpfSSUGnbJxmgE3f3jkCKvfPGqNGISMnD8O0Fv_78B5yKHDuapiSJpXG5_44m-fObj9_5FXBkDigW1jc7xGmS97n5hohknbsljWmzNpYEFJ7ld1zGQsO__dj6FOeczORP0I77sUzvhL4sIYN_Qie-NXXDOS3HRvFej3Sh0gVduuiLxzRgEfDRcmXSE1Lm8CCnPBg3Tf3mtaMcraoIqYIgQAm-m4XkoqTeksyG6W-HafJbhman1vwlIvfgQRn97bWyVvTGv3qXNv98-EDk2_x_DglNFtezBz7t8wFtPAxdpFr9_2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b228c55ff.mp4?token=urGQ5WMjz1LLOJ075CKTTt-8WvgkATq3_Jx0pbnpfSSUGnbJxmgE3f3jkCKvfPGqNGISMnD8O0Fv_78B5yKHDuapiSJpXG5_44m-fObj9_5FXBkDigW1jc7xGmS97n5hohknbsljWmzNpYEFJ7ld1zGQsO__dj6FOeczORP0I77sUzvhL4sIYN_Qie-NXXDOS3HRvFej3Sh0gVduuiLxzRgEfDRcmXSE1Lm8CCnPBg3Tf3mtaMcraoIqYIgQAm-m4XkoqTeksyG6W-HafJbhman1vwlIvfgQRn97bWyVvTGv3qXNv98-EDk2_x_DglNFtezBz7t8wFtPAxdpFr9_2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: قیام عاشورا سند بنیادین مقاومت در برابر ظلم است
🔹
روز گذشته در آیین افتتاح «محرم و عاشورا در آینه اسناد وزارت امور خارجه» تأکید کردم که قیام حضرت اباعبدالله‌(ع) منشور عدالت‌طلبی و سند بنیادین مقاومت در برابر ظلم است.
🔹
در لایه‌های عمیق‌تر این مستندات، تجلی عزت‌طلبی تمدنی ایران در تقابل با نظام سلطه و قدرت‌های استعماری به چشم می‌خورد.
🔹
به عبارت دیگر این اسناد، تاریخ را از سطح تصمیم‌های رسمی به سطح تجربه انسانی نزدیک می‌کنند.
🔹
اطمینان دارم این نمایشگاه روزنه‌ای برای شناخت عمیق‌تر پیوند تاریخی ایرانیان با مکتب عاشورا و پاسداشت ارزش‌های اسلامی و کرامت انسانی خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/455381" target="_blank">📅 21:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455380">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZLB3PemLIgU2bSdjDc-8y70jzHPC8BtbH5HcaoVudKPSmbG8S_hEQXQeXEC0VhDNrJVtEhxbhvsLrPbHmR3nbvbyQYQSS5ZmuebCqL45OCVn50lPK-CYuPRsHHejv55rqxX4-0EZp4aMl-6mJSdt3UeiLYnyUu8cYTWliDDY6Lo31mSfDMpKHUZ7d8J4Xfrr6QCHY5YPISs8LIGQR-fljPdpXv5iWSbrnZWgd9bfISGEbPUXhgz-RQ7__1CzJEBog8eQPRd2UbK5xw5apTZbVfk8Okov1xE1ruzL2Y2KYqzEiELsH5pQjyPFaDn3JQBm36_lDqIxkw3jJcwwR1hrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
#یادداشت
|
چرا محسن رضایی به شعام رفت؟
🔸
انتصاب محسن رضایی به‌عنوان نماینده رهبر انقلاب در شورای‌عالی امنیت ملی و سپس انتخاب او به‌عنوان دبیر این شورا از سوی رئیس‌جمهور، می‌تواند نشانه‌ای از توجه بیشتر به هماهنگی و تصمیم‌گیری امنیتی در شرایطی باشد که تعریف «امنیت ملی» دیگر به مرزهای میدان نظامی محدود نمی‌شود.
* شعام؛ جایی برای جمع کردن تکه‌های پازل امنیت
🔹
شورای‌عالی امنیت ملی یکی از مهم‌ترین نقاط اتصال بخش‌های مختلف
#حاکمیت
است و مسائل امنیتی کشور را از زوایای دفاعی، سیاسی، دیپلماسی، اقتصاد، اطلاعات و تحولات منطقه‌ای بررسی می‌کند.
🔸
قرار نیست هر دستگاه جداگانه درباره بخشی از امنیت کشور تصمیم بگیرد، بلکه باید میان این بخش‌ها هماهنگی ایجاد شود و تصویر مشترکی از منافع و تهدیدهای ملی شکل بگیرد.
🔹
تجربه جنگ اخیر نشان داد یک بحران امنیتی می‌تواند هم‌زمان ابعاد نظامی، اقتصادی، سیاسی، رسانه‌ای و اجتماعی پیدا کند. از این منظر، شعام صرفاً محل تصمیم‌گیری درباره «جنگ» نیست؛ بلکه باید برای مجموعه‌ای از تهدیدهای
#به‌هم‌پیوسته
، تصمیم‌های هماهنگ و قابل اجرا شکل دهد.
* چرا سرلشکر رضایی؟
🔸
در حکم رهبر انقلاب، «
#تجارب_ارزشمند
» و سابقه رضایی به‌عنوان یکی از «پیشگامان دوره پرافتخار هشت سال دفاع مقدس» برجسته شده است.
🔹
رضایی در سال‌های جنگ تحمیلی ۸ ساله در شرایطی تصمیم‌گیری می‌کرد که اطلاعات ناقص، زمان محدود و هزینه‌ها بسیار بالا بود. این تجربه، علاوه بر سابقه نظامی، تجربه تصمیم‌گیری در شرایط بحرانی و شناخت از منطق تهدید است.
🔸
حضور در فرماندهی سپاه و سپس فعالیت در
#سطوح_عالی
سیاست‌گذاری و مجمع تشخیص مصلحت نظام نیز او را با میدان و ساختار تصمیم‌گیری کلان کشور آشنا کرده است.
🔹
وظیفه دبیر شعام فرماندهی عملیات نظامی نیست، بلکه هماهنگ کردن دستگاه‌ها و تبدیل
#تصمیم‌های_کلان
به فرآیندهای قابل اجراست.
* امنیت امروز، فقط میدان نبرد نیست
🔸
تهدید می‌تواند هم‌زمان از مسیر نظامی، سایبری، اقتصادی، رسانه‌ای و سیاسی وارد شود. عملیات نظامی می‌تواند با جنگ روایت‌ها همراه شود، تحریم اقتصادی بخشی از فشار امنیتی باشد و تحولات منطقه‌ای بر
#معادلات_داخلی
اثر بگذارد.
🔹
در چنین محیطی، مدیر امنیتی باید بتواند میان حوزه‌ها ارتباط برقرار کند. از این زاویه، انتخاب رضایی را می‌توان با تجربه مواجهه با
#بحران‌های_پیچیده
و توان پیوند دادن میدان با سیاست‌گذاری مرتبط دانست.
* ترکیب دو انتصاب
🔸
رهبر انقلاب ابتدا محسن رضایی را به‌عنوان نماینده خود در شورای‌عالی امنیت ملی منصوب کردند و پس از آن، رئیس‌جمهور او را به‌عنوان
#دبیر_شورا
برگزید.
🔹
نمایندگی رهبر انقلاب جایگاه او را در ساختار شورا مشخص می‌کند و حکم رئیس‌جمهور مسئولیت اجرایی دبیرخانه را به او می‌سپارد. کنار هم قرار گرفتن این دو می‌تواند نشانه‌ای از هم‌جهت شدن سطوح راهبری و اجرایی در مدیریت
#امنیت_ملی
باشد.
* انتخاب برای یک دوره متفاوت
🔸
شرایط امنیتی کشور پیچیده‌تر شده و مرز میان جنگ، سیاست، اقتصاد و رسانه درهم‌تنیده‌تر شده است. چنین شرایطی به تصمیم‌گیری سریع‌تر، هماهنگ‌تر و راهبردی‌تر نیاز دارد.
🔹
از این زاویه، سابقه
#دفاع_مقدس
رضایی، تجربه فرماندهی، حضور طولانی در سطوح عالی مدیریتی و شناخت او از سازوکارهای مختلف تصمیم‌گیری، بیش از آنکه مجموعه‌ای از عناوین در یک کارنامه باشد، مجموعه‌ای از تجربه‌هایی است که می‌تواند برای یک مأموریت مشخص به کار گرفته شود: هماهنگ کردن اجزای مختلف قدرت ملی در برابر تهدیدهایی که دیگر یک‌بعدی نیستند.
1️⃣
تجربه میدانی
2️⃣
نگاه راهبردی
3️⃣
قدرت هماهنگ‌کنندگی
4️⃣
نزدیک شدن سطوح راهبری و اجرا
🔸
انتصاب محسن رضایی در این چارچوب، تلاشی برای متناسب کردن مرکز تصمیم‌گیری امنیت ملی با شرایطی است که در آن، امنیت دیگر یک پرونده جدا از سایر مسائل کشور نیست؛ بلکه حاصل
#هماهنگی
همه آنهاست.
➕
متن کامل را
اینجا بخوانید
.
@rahbari_plus</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/455380" target="_blank">📅 21:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455379">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GptZoUte6uwkfj4wGIgEIg86_PjcEut2YLEZjHhjK_tNw0g8tNT8rSz1hT1Onj74Q5m1R8EjvjPrs3Vn7Wv3VYD-6LmuqlUbAKWo1W0GCgCHaMzMYVpVNMsp9vQbh7TDUGxVnEJ1cmFBGNVsG7YZ81ns1pnQ9G4_r4HWCCVjWiMrnNzBih_tWDnk9EqF4u9OZA5JGTR0v7aj2HfrUCOrIalwLsOnTyxgLDS9SEa15XOus9Q7JWYlGjKy27pq2l220P0LskEeRyGaLds1k9fEW3tt3ByTJzgZEUNUQrP6ma0qXBIgj0CiXAKOngo0pqUYj0lnIWTvaSb1SE8DUSIoXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسوایی اخلاقی رئیس فیفا فاش شد
🔹
طبق گزارش یک نشریه انگلیسی، رئیس فیفا در زمان حضور در یوفا برای مدت ۵ سال با یک زن که همکار سابقش بود رابطهٔ غیراخلاقی داشته و از سمتش سوء استفاده کرده است.
🔸
پیش از این اینفانتینو ابتدا به خاطر زد و بند با ترامپ پروندهٔ سنگین اخراجش از سوی یوفا کلید خورده بود.
🔹
حالا افشای رسوایی اخلاقی او در ٣ روز گذشته او را بیش از پیش به در خروج فیفا نزدیک کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/455379" target="_blank">📅 20:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455378">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8756ae1c.mp4?token=S5TTcZhApKni9kYoUo8ufQHW7PRSkAGyl3t_NYBEXYQyMOj2PyM59bg-YViv8cmfdlqaWcyeM8aVkyKAaTktxol52RfQANtTcBmjUVIhXw7rXIdgdtsPvhw2LxLlP1_aQi5pNQsq0Cu4lZNyHoKIhwnWES5XddRdb4hDhdFIEJy4QfzgLm25zIvhcww1sloEBzdd8aZdXuXzNFlEZjt_6IJ9AlR2w8dH9LsokyW67tvp_zwUZxJRUzSeF_69W4aUK-gzaW73M96apMNOqO4yDrK0wgiypc1Al9552GOaVnGQwjHV2IAyVdKY5nXoWYniAWa_z9aYKx3lScTzTyu9kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8756ae1c.mp4?token=S5TTcZhApKni9kYoUo8ufQHW7PRSkAGyl3t_NYBEXYQyMOj2PyM59bg-YViv8cmfdlqaWcyeM8aVkyKAaTktxol52RfQANtTcBmjUVIhXw7rXIdgdtsPvhw2LxLlP1_aQi5pNQsq0Cu4lZNyHoKIhwnWES5XddRdb4hDhdFIEJy4QfzgLm25zIvhcww1sloEBzdd8aZdXuXzNFlEZjt_6IJ9AlR2w8dH9LsokyW67tvp_zwUZxJRUzSeF_69W4aUK-gzaW73M96apMNOqO4yDrK0wgiypc1Al9552GOaVnGQwjHV2IAyVdKY5nXoWYniAWa_z9aYKx3lScTzTyu9kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۴ مطالبه رهبر انقلاب از رئیس جدید سازمان بسیج
🔸
تعمیق و گسترش فرهنگ بسیج و مقاومت به منظور تحقق شعار «هر ایرانی، یک بسیجی» با استفاده از ظرفیت آحاد مردم مبعوث شده و اقشار میلیونی جانفدا در راستای ایران قوی و متحد و حفاظت از انقلاب اسلامی
🔸
تقویت شبکه‌ی اطلاعات…</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/455378" target="_blank">📅 20:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455377">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXTkr3H5Sfn6ydswZE11iSaSZ69opPCP8DnARxSYHauGVbF5amKkCFO4rPVe2tJz6OLhVntld9u3vZYsyoomZWy_HRi8NR8-rOlIFAXVqSJmvYC5NH6x5_yupvhvSz3qzcbLEbMttIx1LcCMsOwLNeGxo_o8cWOEzevb-gdTasZ9PQWrw9WD0EadHKl_ZbgcQ5o-NuGPSY3G8WcvFSJ-pOSkB4TbqBaxdtoLo4AxEOuwQpsyn6kvv7rewbH4qf5Lgz0dIngJBPcD3Li9Ni5vl2CoTP2m1vdBN-wt606Uyuain_a90cRvR7s46dKcKNYDv1GyG92Q_VuZjXIJG8jI3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استیصال ترامپ؛ ایران باید به آمریکا غرامت بدهد
🔹
«دونالد ترامپ» رئیس‌جمهور آمریکا امشب در پیامی در شبکه اجتماعی تروث سوشال نوشت که متوجه شده نمایندگان جمهوری اسلامی ایران درخواست غرامت برای خساراتی که در طول درگیری نظامی پنج ماه گذشته به آنها وارد شده است، دارند.
🔹
ترامپ با جالب توصیف کردن خواسته ایران نوشت: «من نیز اکنون درخواست غرامت از ایران دارم،‌ برای تمام افرادی که آنها با بمب‌های کنار جاده‌ای و درگیری‌های متعدد، که آنها به خاطر آن مشهور هستند، به قتل رسانده یا به شدت مجروح کرده‌اند».
🔸
البته ترامپ در این پیام هیچ اشاره‌ای نکرد که نظامیان آمریکایی کشته شده در منطقه غرب آسیا و هزاران کیلومتر دورتر از خاک آمریکا، در جریان حمله و اشغالگری آمریکا در عراق، افغانستان و سوریه و توسط هسته‌های مقاومت این کشورها کشته شده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/455377" target="_blank">📅 20:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455376">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64259362bf.mp4?token=TKo65kfi8DLoyzTE8HA1s47kUZcvNMFzHFpyfvHxCzR_IDn3sHIPy5wuSEy_Wvl9LqfQWy7GFtckRzGKakQ4zx5LZvvCNVjYgCmNMIMrHros6GvsJs5f2Xl0royKDTM2Sn37zVx0jME3UHbh1mNG5uVusK1Knjab3C74s91KMhSoYqMK4Z7rkyXeN9iMv7rcYQqCG48cKmEdR6R4PccaXe6FNEesBP8ouSuuMWYymX5s0SxAY74OKk2_agnU08nTjXOhAnZMU7EBXaTA4tPBzjY2N67-tkA9_MNsQLOJOb62NHX83nfUilIjpbsCNSLynM-RJLjl1H90onv_W7S5Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64259362bf.mp4?token=TKo65kfi8DLoyzTE8HA1s47kUZcvNMFzHFpyfvHxCzR_IDn3sHIPy5wuSEy_Wvl9LqfQWy7GFtckRzGKakQ4zx5LZvvCNVjYgCmNMIMrHros6GvsJs5f2Xl0royKDTM2Sn37zVx0jME3UHbh1mNG5uVusK1Knjab3C74s91KMhSoYqMK4Z7rkyXeN9iMv7rcYQqCG48cKmEdR6R4PccaXe6FNEesBP8ouSuuMWYymX5s0SxAY74OKk2_agnU08nTjXOhAnZMU7EBXaTA4tPBzjY2N67-tkA9_MNsQLOJOb62NHX83nfUilIjpbsCNSLynM-RJLjl1H90onv_W7S5Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میر سرتیپ کیومرث حیدری به عنوان جانشین رئیس ستاد کل نیروهای مسلح تعیین شدند.</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/455376" target="_blank">📅 20:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455375">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsq26edPi5KZyERshTutpv2pBLmsGxwj-q4qpTcOK4UiCgzpaHFoVPUlMNojowVZfB5t0qFNJCrpDc6GqRECTe9Ve-5-NvpdByVc0aSJ4gWY8Qi1HTCqCFJgpgrO8VKINb87Afch--qSTkTwj6TIzEmbVktIHLPxGnDid_rt0kibnmOwfpiztjrjRC5Ctxy7WzVjL2tgxawRWQxxQ9rQ9qjxix5opl1v-4-kUsgenY2Nag-Ja9S4YM-bu4NkX-a2fy8hVTvyQ--zQYV6eaD8H3uZtf_JIM0Xa3QT8lgIuJIHgh1IZ8MlAJEb90lVbAXQPC_-iRycxQTIcGX3WLLYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس جدید ستادکل نیروهای مسلح را بیشتر بشناسید
🔹
سرلشکر علی عبداللهی از فرماندهان باسابقه نیروهای مسلح و از چهره‌های شناخته‌شده دوران دفاع مقدس است که بیش از چهار دهه سابقه فعالیت و مسئولیت در حوزه‌های مختلف نظامی، انتظامی، امنیتی و اجرایی دارد.
🔹
او در طول سال‌های خدمت خود مسئولیت‌های مختلفی از جمله فرماندهی لشکر ۱۶ قدس گیلان، جانشینی نیروی هوایی سپاه، معاونت هماهنگ‌کننده و جانشینی فرمانده نیروی انتظامی و سرپرستی فرماندهی انتظامی کشور را برعهده داشته است.
🔹
عبداللهی همچنین سابقه استانداری سمنان و گیلان، معاونت امنیتی وزارت کشور، معاونت آماد، پشتیبانی و تحقیقات صنعتی و معاونت هماهنگ‌کننده ستاد کل نیروهای مسلح را در کارنامه خود دارد.
🔹
جانشینی رئیس ستاد کل نیروهای مسلح و فرماندهی قرارگاه مرکزی حضرت خاتم‌الانبیا(ص) از دیگر مسئولیت‌های وی در سال‌های گذشته بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/455375" target="_blank">📅 20:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455368">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UugaDZLWhmZYPYY6D_JLTjA_Z-sfEjHXWbJ2J1c85CgwR7fssXhKpWNgeZzN_bjuGYhUZNXyTq6rOsuuxj36Q-789MLQT0HesnSdYeiYvTqlLq551k8Bglra8qyFTJr-1ICWLCzE-BUxpqdlxaH5dKFbWb-tU-BdPiEAqf8v2AkvJ-xFgrXxJlV6LN0YO_JBIZuVYgX8Z5_gy3C10dAi4YBqwMxWbNYPeob8g_7LPSymMDIAgI8jC08_AJ5aLo3tujOrNvLc4fcfnLJal1EF_pXE30eqA3vagjnVwsE-mFU1R7woS7yQZYAzzR7-NjoyumXQYgwk5wof2LYlPq7IHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C96W2XdDDhEoEjEsG4hmUPkX9ocI6xqdwYEWv5HuppqJpZuqOvQcepwrCBKPWCt-ZCdHFR24CjVVoS27GJqEiRyU1HwMCLnTdg8yfVtvW4FaLGLQdT0XKIoZf980ow_RPnbXo0ObM-rnvRl6amp5BEIJqExLsDcRktB2hptrmgSWXYJaELnZogx-2FM_mhArTWwGD6FW-XiSARx8bUydBwDf38kSsREnSdA5QijdwUtAidjKBdV3tQel2SjvAGAqozzo7HZVLRG63-Wi7KvpLI-Gz-KOK_2RvzV68UVxQb0LM8VXTj-ZTWgqMYfCcpre73wuKuTbjazPfVCUzJ0z7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a8K53b0aRl_24OCed87KMhj6iM_2JW-YWtpIS5JPHli1AfGfBTQIKzPt48u6nnkaAPjrUFUBG4eFVuGwnyfhMIcyXs6TgMXrb5JeHxzVyUgt0gjDgFFtpIQ9Bb-AZQbPPqCmlrYLGy_1kqb47QVFKOBa1lg94D7z9eqS1qmD662JPCmqTRSn4J79sTLct0edMCWTj7IqlnIl_PrxLvCwxBjWfHk3jyFLPlanV2D-hmPAUG3wJBvuWns0t-k3hBw7LoHeL7lUdoWVfDvHmbJHZ1tWRTdefg3djxBP0rWLZICFPmjC9UN23yz_4PcAf7BdUEPB6khhyAXtfspk4I80Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gdJwE8HZFNGlfIkBPx5wHgVrfZALcENg_pDpa4cpE3mgD-h3WF1CucJp4rZ7PlNHkd9WSU6GB-YhXZeSGMrLizI5gPgvfsFfHRk3ieVOxiSTpqFBVaEMMLinQGuLyi4EM7ZXrHuWddM5Avp7Cyn9QiYVgk72YBS1jhfTth8AJHGpLoKDHig_byswaUs_cY2W4wSKFCa9XaQaabmkESsWOBzlf5L3kwshCc83M-Sb8daztjkL4hRswY65masXs91gAqfpSSGchXoThW4v_XxuPyGj1QUQJqECi7ZHkQnoA9p5sriuIzk9TAROg4KiSuvC-ZbCo0uLpgyeDnLHkvMM7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WJTdhgFmMtoP0e20v1MpfTG9ivhNIri8KR9I47CLGC8KouTf7ZhkflZfrRyKoSdPsILPt-gzgniK5Cu76DqWjLEeF3t0G4JPCWkRB_mkkPPpExB_8cctYGpjPXQ_s5CQjKM-OzZtaSqFPlvuMjwnH0In9LcTAvDWPEH1UGjS84q9ZCBM19Rk6l43KuADIyu4jk36pMFpXd_jaOS4s11OyEuifCeWP8ymmRvebJTcJD8FA52Dkg0uo2XNbqK_K0-HYV7LGidvdZcp8erCvseT7kurZShJZ7s2HjQCf69HT_Fyn95QMnJt_b4l87gdBH5_JY5rFY5n_Ul6Ja_5q9PAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Npet8KpwhVjSkiYaK9qqgCH7DCxAKepxwgHWQKUVyuQ78AavIi1UwXCmtnjN83TSi3FvIISVJedWu3DC7jPilGKqQ0LnXNPMXgiGVPEy7Xx1pSfYL9C6dLLgNLZyniTSNOFHbVjurD0Cu3-rD7nNYrUkZakXxI6k4rvqb5PD7AlHgjcmoG7e-t3ypkdOhjYKM-6xAJN1_bVwRYAyzm5qJxvBV-m78eQ2LvVIEHyzXi2_g6OkHhhkKvOMRXxV1K82eShKDDAFKsmI4l3sra0GBZYeOcaZ75J8_9lrTjOlGq_w5QMCrgxlmQQnn0OHg_HKu-W7VQ45eVI9jwaZHjrjaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RqJlRB5tZE_BljfvBCjPMOkCUMQCcIzXsPuyHWf3bRc8bdei0Qm_FYLQWkXd76pZnqeg8ldf3KaUzXfezt01FxyfpLOlB5mUdlauSEAhWMhSJ1vvvQH4UV32x1OvhCHllr2UiNkUJfDbSqGfpkxXVOfwXuaumaJ7L5PAVVeLh6lJcvhyu8CSNx6Dnd3Hzc_qdjKyCHGWbdlY2I_woGHBE1IP6S3H4FnDNTMmE6cwLm3l6fKO4-56YcZWXw6jj7VMtVrro0qcHfOCYP8w2DEBRf9ZUdlZWkBpot4U-UbiqNqUT6TJebo1h0eYiKOa7y-XUMOulopFJn4IJP9zi9jJvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع پیکر مادر همسر سید حسن خمینی
عکس:‌
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/455368" target="_blank">📅 20:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455367">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed2fc31183.mp4?token=d2O-pbgIMFtp6fGOsjtbWzUrGSWyGfyIUvCBOae8lTe1UiAL3NLl9-ivzOm3DvIf1wqzhDwObBWxfyJ0KtgWAq4UEc7eE6IG9IueR2tq5KOYb9afYsO0NMmv44CPG49IVdbU-XF-tNGWidpiWo3kqrGmYsMZ_4TjX_frj0MksuZZMNCTIjUpNKCchgbed3SL40mJkiLjQnNY72uqxc2BwYlVuygdZyHG-C9R1pBbR9rj4sa7ePUY09pvHjHFOeXcWKlgztyxe3y9q6UoEMHKvmUokJheaP7OKI47ef2yTj2jfWZgXSWKupcMC-1O1skQj6h7h7I-BF5smhbnEQxaRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed2fc31183.mp4?token=d2O-pbgIMFtp6fGOsjtbWzUrGSWyGfyIUvCBOae8lTe1UiAL3NLl9-ivzOm3DvIf1wqzhDwObBWxfyJ0KtgWAq4UEc7eE6IG9IueR2tq5KOYb9afYsO0NMmv44CPG49IVdbU-XF-tNGWidpiWo3kqrGmYsMZ_4TjX_frj0MksuZZMNCTIjUpNKCchgbed3SL40mJkiLjQnNY72uqxc2BwYlVuygdZyHG-C9R1pBbR9rj4sa7ePUY09pvHjHFOeXcWKlgztyxe3y9q6UoEMHKvmUokJheaP7OKI47ef2yTj2jfWZgXSWKupcMC-1O1skQj6h7h7I-BF5smhbnEQxaRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افسر بازنشستۀ آمریکا: ایران معادلات را از هسته‌ای به تنگۀ هرمز تغییر داد
🔹
ویلیام پاتنم: هدف آمریکا همیشه این بود که ایران به سلاح هسته‌ای دست پیدا نکند اما امروز تمام تمرکز آمریکا روی بازکردن تنگۀ هرمز است.
🔹
اقدامات نظامی آمریکا تاکنون نتوانسته به اهداف تعیین‌شده علیه ایران منتهی شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/455367" target="_blank">📅 19:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455366">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GP_7ecKDgf1U-rk2Ux3B-Rmf08VE9mTEjuM_69FNPLzwQQsXguD6uJEmWoLwRaGE2rvtGsf3K270t7CsEywUuLPcMmTg6gE5IjTTfCeMU-6WTj6xMulr6r9u7qSm3UkqT4ic6qOys6GoSpe91BQB47Spp5AHmgaiJPYWF2dkqL4cc0m0AYtE0FZeSJnwRoAbFerStR0HZLsJ7etJbRwpup2Gjv2BFEC-av5arQ5DIk3E6S0LNm1vDC1wmIrsq8og4HBZOM5qEWQehK2Tita_YEY52Es8wQzoxi6f6e5CP21q05shargXdzkrdZSt5zbLMkU6LhfnFZ_HVjzFCLRB0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولید جنبلاط: صلح با اسرائیل غیر ممکن است
🔹
ولید جنبلاط، از رهبران دروزی و رئیس حزب سوسیالیست ترقی‌خواه لبنان، در گفت‌وگو با الجزیره گفت: «ما امروز با نقشه‌ای جدید از مرزهای اسرائیل روبه‌رو هستیم.»
🔹
وی با ابراز نگرانی از حجم انبوه آوارگان جنگی که از جنوب لبنان…</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/455366" target="_blank">📅 19:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455365">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مطالبات فرمانده معظم کل قوا از فرمانده جدید سپاه پاسداران
🔸
ارتقاء مستمر و همه‌جانبه‌ی توانمندی‌ها به منظور بازدارندگی حداکثری، و آمادگی هوشمندانه برای اجرای عملیات تهاجمی پرقدرت علیه دشمن
🔸
اعتلای فرهنگی در سازمان سپاه و تقویت تقوا، بصیرت و روحیه‌ی انقلابی…</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/455365" target="_blank">📅 19:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455364">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nbe1U7_xjIKZG5J0kLHNhriufyJjxbLqYREYeeKAFFf-7xD2zgP-1HRwGt_d3hOpF6xYZfLGKQIev8JeU_gHyy5UpKPwlqXTB53YwToIrkx4zWqJZ_KvhBltBo9zKpUss2B-0ElrWjgnKQFvuSke0qzzKibv0KMq8ebmbWtBKBVvdHwrnAX6R5weJreIKq4BduYw5nP_oj1cIij28vGcpoHn2Hcy8d2j_I6ox9VHKkKa4lpugsz2C2nsQPOMkvfgBZMQHl9BRKb2IMQTFZAfuot_yIdfVk8SRqfe_NhQq3RZIl9Wvz_9xwqogHmd2dvPiqPFrk4ZlD3B80UODvV1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انقلاب از سرلشکر عبداللهی، رئیس جدید ستادکل نیروهای مسلح چه مطالباتی دارند؟
🔸
ارتقای توانمندی و آمادگی‌های همه‌جانبه و روزآمد دفاعی-امنیتی نیروهای مسلح و بسیج مردمی
🔸
فراهم‌سازی امکان پاسخگویی به‌موقع، انقلابی و مؤثر به هر سطح و نوع از تهدیدات متعارف و…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/455364" target="_blank">📅 19:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455363">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">۴ مطالبه رهبر انقلاب از رئیس جدید سازمان بسیج
🔸
تعمیق و گسترش فرهنگ بسیج و مقاومت به منظور تحقق شعار «هر ایرانی، یک بسیجی» با استفاده از ظرفیت آحاد مردم مبعوث شده و اقشار میلیونی جانفدا در راستای ایران قوی و متحد و حفاظت از انقلاب اسلامی
🔸
تقویت شبکه‌ی اطلاعات مردمی، افزایش مهارت‌ها و آموزش‌های لازم توأم با بصیرت‌افزایی و بهره‌گیری از فناوری‌های نوین برای مقابله‌ی مردم‌پایه با تهدیدات دشمن
🔸
تعامل سازنده و مؤثر با دیگر نهادها و سازمان‌های حاکمیتی، دولتی و عمومی و گسترش گروه‌های جهادی، بسیج اقشار و محلات به منظور توسعه‌ی خدمات اجتماعی اثربخش با محوریت مسجد
🔸
ترویج فرهنگ بسیجی به عنوان الگوی مقاومت و پایداری مردمی در سراسر جهان در برابر استکبار صهیونی-آمریکایی
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/455363" target="_blank">📅 19:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455361">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuFfPcTFE4oSQYP1iGqKemJFTEwcRiPIPAvoLxkyPXc8mGl53WGPMNWJQm4xrFPKUdRNv0X0i_KYKEQkiiUxPYFQ_L8MKHmXwjtmS1rqQd2p3_HLFkInqN8fqoalmuPJIHmOao409XGhkDBP_sJtQJe78Xz9LzPc16CcAxv3w2BIdasrq8bMmEuuc1_WKUahBRwnhbiPgl83xBbJHxF8ZNq8Ojq_x-d4gmhuQ1EFiHCDvUd2IpEXsEDS_9ulpOQWuc4kK3FuFkqyhtvDyce3NAX14dS-hnRPhI3whJZa822M0zTbXdYefvCi7LqWnQNq-hRofUxZE_gn_5pfIjZDdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطالبات فرمانده معظم کل قوا از فرمانده جدید سپاه پاسداران
🔸
ارتقاء مستمر و همه‌جانبه‌ی توانمندی‌ها به منظور بازدارندگی حداکثری، و آمادگی هوشمندانه برای اجرای عملیات تهاجمی پرقدرت علیه دشمن
🔸
اعتلای فرهنگی در سازمان سپاه و تقویت تقوا، بصیرت و روحیه‌ی انقلابی به عنوان گوهر درونی آحاد پاسداران و فرماندهان
🔸
گسترش مدیریت و فرماندهی برخوردار از بنیه‌ی معنوی و علمی و مهارت‌های نوین در سلسله مراتب سازمانی
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/455361" target="_blank">📅 19:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455360">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kh4m8zFIyT7rwJ9Lg-evFTxd73awYBtJGAHa1AYDzeZP9nWeRaueCHGlmU33YYSGpY6orcdG1bhlZM4sPcLJOiUJqLXACX0A3GGM1HLQ1tDZOhpZDWaPhmW33IzuUSgJIqoBDPzeeysVhm7Ue5-Qhvx0_nkOx0VPJWxjwg4lppEEXlHlryaU1afbUqc1IN6BS8lLSkiO5fwpIlWRSJJWejykLsCUukWwJzXvRyUrgczuhYWp7aivJhx2imCh5-ptOCaW95EXk-sfolp29opaGpcUBz0dsGeR4ke6iMaMkUJ21yRNBiv8wdojTuPwhsAtl2cnCnOavcIbtKoytUorKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رهبر انقلاب ۶ فرمانده عالی‌رتبه را منصوب کردند
🔹
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده معظم کل قوا، با صدور احکام جداگانه‌ای مسئولیت‌ها و مأموریت‌های ۶ تن از فرماندهان و مدیران عالی‌رتبه نیروهای مسلح را ابلاغ کردند.
🔹
براساس این احکام، سردار سرلشکر…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/455360" target="_blank">📅 19:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455357">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
تا ساعتی دیگر احکام انتصاب تنی چند از فرماندهان بلندپایه نظامی جمهوری اسلامی ایران توسط فرمانده معظم کل قوا منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/455357" target="_blank">📅 19:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455356">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">زمین‌لرزه‌ای به بزرگی ۴.۷ ریشتر در مرز استان‌های خوزستان، ایلام و لرستان و حوالی حسینیه به وقوع پیوست.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/455356" target="_blank">📅 18:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455355">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0893f142a.mp4?token=MtoQ0-oSpJpHfLZT7aBBlXeBplDbpbjUvqXqg_IfOo6E-BavbmlSztF4gBo6efUC4bArNRfxF3sJRfrfYHqT6dYh2uyaKrErccsnVPProUM5AQfTfWhRvgW1wp9IICoRlub7E-9DxriaJRMTMes8ZGe7o6B744LTU2TluGwArb9jrGOw27xosfZ-cHIdEabFaOkkP47-hS4uo-4IXa4QTAgYhqVMIcIfWg5YV28WA1mHOkP8zmU6Wx4RFUUgjWagKOV-fIFECLesn7hW2Dj1meaT9VOZSElydwyBtKK3Lnf1wDe3rysTsDUrcIxbl1NRHDZ3WPyEnwwOW9yvWStt8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0893f142a.mp4?token=MtoQ0-oSpJpHfLZT7aBBlXeBplDbpbjUvqXqg_IfOo6E-BavbmlSztF4gBo6efUC4bArNRfxF3sJRfrfYHqT6dYh2uyaKrErccsnVPProUM5AQfTfWhRvgW1wp9IICoRlub7E-9DxriaJRMTMes8ZGe7o6B744LTU2TluGwArb9jrGOw27xosfZ-cHIdEabFaOkkP47-hS4uo-4IXa4QTAgYhqVMIcIfWg5YV28WA1mHOkP8zmU6Wx4RFUUgjWagKOV-fIFECLesn7hW2Dj1meaT9VOZSElydwyBtKK3Lnf1wDe3rysTsDUrcIxbl1NRHDZ3WPyEnwwOW9yvWStt8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آموزش نحوهٔ برخورد با سلبریتی‌ها در یک سریال
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/455355" target="_blank">📅 18:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455354">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPjrNp3WBHPM8isaOU7-CHTsKQ-tyCLSn5AfUwnTLOFyT9dZQBMYvUqpTt0CE7dgvSmmlm9w0tsc2uM19uypAugTWxoArffRNcaIRTtXcwiJghw13iVBGsU36G7bEeVKKKDjBO4SE13UBTOw7sHXBTFRCm7NyU0YxUox1XD_ZBpP7t9M_e-hfak0Q165eVzVa9sUOwe73YnOZ8FyVBkRezGCKetpeUcfCNH9lvpbCtmpVyOL6LesnuHaeIRBASMoO7q8IaEyPYMXeYugQArol5maeEg7uGUj3937OUoZkhPR4fFHE5I5rgKN0SOtScTCY1VIX-vPxgxByZf3_fUYNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: با توفیق خداوند پالایشگاه آرامکو در جیزان را با استفاده از پهپاد به‌صورت دقیق هدف قرار دادیم.
🔹
این اقدام در پاسخ به نفوذ پهپادهای دشمن سعودی به حریم هوایی استان‌های صعده و حجه صورت گرفت. @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/455354" target="_blank">📅 18:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455352">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FobmflJpS7MCUcGjmdUxAragLY5LLODCgjKuvOMiupBM9BAeHUVm76RXpCiEgDanTPxEgMMgPMJMSWGKFUMMZUFlzyzhWMQmTHnrWQwz_2IRpXprB2AfPJIH5sAoTLe2J7Ad0spxiNZXRRSnwt71XcMkp0rqI9va901Ej8WnAvQ8vhQTzDTrst2GOq__5gdA4FBw2_pY-W0KjKSKPLFkYzc3DCLatBpu1b3rVC-sfK4BUAwybu5b1UP-biNsDBmMaazQoMU0H-Uo0UiCxBd2LShpdmUawp9uVOTxCbmRO9XhpAwuWdJotMWEgmvlR9EXcKtwnL7EKbOPmMznloJwGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تا ساعتی دیگر احکام انتصاب تنی چند از فرماندهان بلندپایه نظامی جمهوری اسلامی ایران توسط فرمانده معظم کل قوا منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/455352" target="_blank">📅 18:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455351">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae8b99ad50.mp4?token=nlRzqPxObW5hekZcoobManlsftad5jzf6v1aW9b5XDXyREh_WX8rNNykfzYrFuarAksMdBA3_36DBc2mEfqUnoKkgqyTx4QolRb1I7sHQ_Z78majXMT4BR3ZEoeq2a3N2G_tSv644sLoL4gnDpvE-8_w454nDbi3-jsRr9rNnWJc2otNsP1DJWU9aZqunojisT_F-jMHCt0zrs3WJVfDcaq9HyKinrCsAtNZ4Bf2p66AZ0I0t0uj1Djxoz3RrTDXd755_IO-1VeZ3u2HVy-llVvaseaX5xbWqFzmh6oHsY_vbJiz7UPoEVS8bUT1Pc91m6qYyzlDXCaxcT6jTkxx2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae8b99ad50.mp4?token=nlRzqPxObW5hekZcoobManlsftad5jzf6v1aW9b5XDXyREh_WX8rNNykfzYrFuarAksMdBA3_36DBc2mEfqUnoKkgqyTx4QolRb1I7sHQ_Z78majXMT4BR3ZEoeq2a3N2G_tSv644sLoL4gnDpvE-8_w454nDbi3-jsRr9rNnWJc2otNsP1DJWU9aZqunojisT_F-jMHCt0zrs3WJVfDcaq9HyKinrCsAtNZ4Bf2p66AZ0I0t0uj1Djxoz3RrTDXd755_IO-1VeZ3u2HVy-llVvaseaX5xbWqFzmh6oHsY_vbJiz7UPoEVS8bUT1Pc91m6qYyzlDXCaxcT6jTkxx2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاکسی پرنده سریال پایتخت در واقعیت وجود دارد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/455351" target="_blank">📅 18:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455350">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1921d9c71.mp4?token=ZyZQv9YwMv-Q2D1PSSwDWf3wI0gbewYR55wBAjhRFNlXNtAtT6nNukq_8Xl1bmGnQakawlyiavy-6BjhrkkgGtb9FIfwQvPSJ0PMau4zJ4koHr6OZC3sRAfs98mBKN4XXebhcEg9uIV1iX0Gc7l30AtM2HA-R5HPGaffAdtFsN-hMJH88TQkyHyLHm3IH3z4Ywm5Z9zGzrKEgSfIi5vbhcLwtaLZOKkrjeDW68tjX7_1IbOXCWAFLIKJe877dvI4wl0F2b8ZuwwKH22nKt_szvQVa2-cO_3aCFFt5G-K4DncsSAwmOUus1V8HFmDjNcElaeVy99_ltfGq7JXCU9F5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1921d9c71.mp4?token=ZyZQv9YwMv-Q2D1PSSwDWf3wI0gbewYR55wBAjhRFNlXNtAtT6nNukq_8Xl1bmGnQakawlyiavy-6BjhrkkgGtb9FIfwQvPSJ0PMau4zJ4koHr6OZC3sRAfs98mBKN4XXebhcEg9uIV1iX0Gc7l30AtM2HA-R5HPGaffAdtFsN-hMJH88TQkyHyLHm3IH3z4Ywm5Z9zGzrKEgSfIi5vbhcLwtaLZOKkrjeDW68tjX7_1IbOXCWAFLIKJe877dvI4wl0F2b8ZuwwKH22nKt_szvQVa2-cO_3aCFFt5G-K4DncsSAwmOUus1V8HFmDjNcElaeVy99_ltfGq7JXCU9F5DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چه سردردهایی خطرناک هستند؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/455350" target="_blank">📅 18:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455349">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3205d65f27.mp4?token=IynMFTrwKVBd0vZ-flk2qF3w0hbD5KqIDv2hpOxg-yXdPyljdDLsRjAaUU5B1al2BE9wFA-tPRXC1EK27fekqLwX4X82-mHYF4PRu92QAQ5vNqz3O_XXqrbmJ7DimG4d9wBU5P_uCmJF3Se-mgpyTQ0cWjNQ7Y_3aC1G7CGgt23T5oAnBi8L2B0EZUOd81VM9DILaCyojleCQpeNMA7TdjMdP-8114oU-_M1LuFELDOp1o5tQOedifcQrISCME_pFXrnPZR-kKgSKxVu1QU5rSAMlglNkd36LkbYtpgi_ePBlL-l-vZ4YJgNzA4bd8OBq3KNGVB-Z1GoEHZIKKM_bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3205d65f27.mp4?token=IynMFTrwKVBd0vZ-flk2qF3w0hbD5KqIDv2hpOxg-yXdPyljdDLsRjAaUU5B1al2BE9wFA-tPRXC1EK27fekqLwX4X82-mHYF4PRu92QAQ5vNqz3O_XXqrbmJ7DimG4d9wBU5P_uCmJF3Se-mgpyTQ0cWjNQ7Y_3aC1G7CGgt23T5oAnBi8L2B0EZUOd81VM9DILaCyojleCQpeNMA7TdjMdP-8114oU-_M1LuFELDOp1o5tQOedifcQrISCME_pFXrnPZR-kKgSKxVu1QU5rSAMlglNkd36LkbYtpgi_ePBlL-l-vZ4YJgNzA4bd8OBq3KNGVB-Z1GoEHZIKKM_bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین تصاویر ماهواره‌ای از تنگه‌ هرمز
🔹
ترامپ می‌گوید، «تنگه هرمز باز است و ما آن را کنترل می‌کنیم» اما پایش‌های دریایی می‌گوید معدود کشتی‌های عبوری از مسیر ایران تردد می‌کنند.
🔹
داده‌های شرکت رهیابی تردد دریایی مارین نشان می‌دهد عبور از تنگه هرمز به میزان محسوسی کم شده و جریان عبور از مسیر ایران برقرار است؛ پایش‌ ماهواره‌ای این شرکت می‌گوید تردد در تنگه هرمز روز یک‌شنبه نسبت به جمعه ۹ کشتی کم شده است.
🔸
شب گذشته تصاویری از شعله‌های آتش در نزدیکی تنگه هرمز منتشر شد که گفته می‌شد شناوری در منطقه «کمزار» آب‌های عمان در حال سوختن بوده؛ ساعاتی بعد تصاویر نشان داد که یک کشتی که می‌خواسته با اسکورت آمریکا وارد تنگه هرمز شود، هدف قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/455349" target="_blank">📅 18:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455348">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54ef328501.mp4?token=u7vXbL6FnIJEK7Nb-VrTXY76hlj4ngFuPz-LI_o-0n-wWG6VzJxN_6VQ89lKXvKh8Tw5gnb5iAXfYs5qkPP2YcZax2XQzBg7oPu2ydla1WuVnHtZ2l4zHGI0wWXrteDZfaZj7woGkD9SpNGBMMfEO6Nl2GFykFkMdZhszYfy9068rRYjjruRu895V4ZxwEQGVmX1QspGpLtEq4a7gA64xbyjSc_E771vACAOCrijcGqyv6bp9yYquMAMvcmri8gB5Yj3p5pI42QP6cKFGRQ47XMT3xCLsTjEfWA5rkDwa4Fsma9-LoAefRD3wKoweYoihx_B0cih-2aAUlq-Yk26rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54ef328501.mp4?token=u7vXbL6FnIJEK7Nb-VrTXY76hlj4ngFuPz-LI_o-0n-wWG6VzJxN_6VQ89lKXvKh8Tw5gnb5iAXfYs5qkPP2YcZax2XQzBg7oPu2ydla1WuVnHtZ2l4zHGI0wWXrteDZfaZj7woGkD9SpNGBMMfEO6Nl2GFykFkMdZhszYfy9068rRYjjruRu895V4ZxwEQGVmX1QspGpLtEq4a7gA64xbyjSc_E771vACAOCrijcGqyv6bp9yYquMAMvcmri8gB5Yj3p5pI42QP6cKFGRQ47XMT3xCLsTjEfWA5rkDwa4Fsma9-LoAefRD3wKoweYoihx_B0cih-2aAUlq-Yk26rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغوش خالی مادر پشت کیک تولد دخترش
🔸
هنا دهقانی قرار بود ۱۰ ساله شود، اما موشک آمریکایی مدرسه و قلب پدر را ویران کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/455348" target="_blank">📅 18:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455347">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84326ff6a4.mp4?token=JqiHeRQcEv9GNeqnyFwsUvkUmJmZEyfBHen9ftDoajVnLkwaS_IGo2Nd9eHmYTNC8KbJWpjmxX3GfZfqi_slc1HD2A1bpE9UOzUBxcfAbswKwy0aEGbHG4Tn3w3bcEZptoroy0gKYbx74ccSF8Xo5TV5cMTBKugxoWyNYlrCYD63NuQjWP-eCy3YJZOaoDUOdHMnSm1NJ5WjBWaV1aElG9dDjCPCpSL91B8WGT_LZpyMASBEwcLnLpYh-lw-yYYdzMipmEGEbg4TM7Tj8JzpRSyJRzcR6jetHTyg32NQhasHUcUBHn3jt4ss7TjxtXGASeVjm8VANqngp56Fbso-oRDgOYXLRSsLBennTzo-iGdJF9Ic0aRnxVMBL2rmKF4eyS-5eXufH018AZGl_YKh069EreEzWhwSGFzhUrjf8SPsO-npEodiTaZS2ZSoDLyhA8xWtmUmtJPMxb1XZjk6kmN9Xtz2PtNQIRMXgCnSPba-fhSl_oXEY64fsVU1XnDEdtLMIEm2kCktltBuvvsFVbZxlhnXmFQiVDmRFKdS0K-fvDp5BSz2BrHhu9TAlPPjb1qRzYt0r8hzedbQm_Is4o7YRvJVXT_hdZQBXdEdB5B4HGmhUJFSgcUNqeMyA4LKiwtoBFYYcr8xqrbbkfSWn_rH-CDnphMlk9DBVXULG8U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84326ff6a4.mp4?token=JqiHeRQcEv9GNeqnyFwsUvkUmJmZEyfBHen9ftDoajVnLkwaS_IGo2Nd9eHmYTNC8KbJWpjmxX3GfZfqi_slc1HD2A1bpE9UOzUBxcfAbswKwy0aEGbHG4Tn3w3bcEZptoroy0gKYbx74ccSF8Xo5TV5cMTBKugxoWyNYlrCYD63NuQjWP-eCy3YJZOaoDUOdHMnSm1NJ5WjBWaV1aElG9dDjCPCpSL91B8WGT_LZpyMASBEwcLnLpYh-lw-yYYdzMipmEGEbg4TM7Tj8JzpRSyJRzcR6jetHTyg32NQhasHUcUBHn3jt4ss7TjxtXGASeVjm8VANqngp56Fbso-oRDgOYXLRSsLBennTzo-iGdJF9Ic0aRnxVMBL2rmKF4eyS-5eXufH018AZGl_YKh069EreEzWhwSGFzhUrjf8SPsO-npEodiTaZS2ZSoDLyhA8xWtmUmtJPMxb1XZjk6kmN9Xtz2PtNQIRMXgCnSPba-fhSl_oXEY64fsVU1XnDEdtLMIEm2kCktltBuvvsFVbZxlhnXmFQiVDmRFKdS0K-fvDp5BSz2BrHhu9TAlPPjb1qRzYt0r8hzedbQm_Is4o7YRvJVXT_hdZQBXdEdB5B4HGmhUJFSgcUNqeMyA4LKiwtoBFYYcr8xqrbbkfSWn_rH-CDnphMlk9DBVXULG8U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهی که شنوا و ناشنوا نمی‌شناسد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/455347" target="_blank">📅 17:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455346">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حملات پهپادی یمن به مزدوران ریاض در «المخا»
🔹
شبکه سعودی العربیه مدعی شد سامانه‌های پدافندی مزدوران این کشور در المخا در حال مقابله با پهپادهاست، هنوز درباره تلفات احتمالی ناشی از این حملات، خبری منتشر نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/455346" target="_blank">📅 17:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455345">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ccc08889a.mp4?token=WrOJtln0d1eZoUuDL_UZi4dzR3cc5HWJYvU97MATACVgVRglKEZZ5W86LWAcyH6B5UNwkwjkL26WckFwMx43U-MV3UrhyrU7E8WzNDOV4lVH6fKwTd1gmu4H3Fshja6bN8PgMeg0DBZtErJ7Gva4vkXIq846qzwSEkoPXFzEmCXfukuZDOrK-viYtpwZzM-tlrxkJUYmM9bb1B4wJFk-f3tpQuhyEvnNKs8PDvPdF3XMnjpUM-reVML-2MTKzrR_8STRh_llSBVwPOed9dFYQ90mvOcaAJIMhd7DmWf_yIDfAaZXx_-fUYf_SPM6XdAAbqzfiEYAO-sz-D1Ndn4UAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ccc08889a.mp4?token=WrOJtln0d1eZoUuDL_UZi4dzR3cc5HWJYvU97MATACVgVRglKEZZ5W86LWAcyH6B5UNwkwjkL26WckFwMx43U-MV3UrhyrU7E8WzNDOV4lVH6fKwTd1gmu4H3Fshja6bN8PgMeg0DBZtErJ7Gva4vkXIq846qzwSEkoPXFzEmCXfukuZDOrK-viYtpwZzM-tlrxkJUYmM9bb1B4wJFk-f3tpQuhyEvnNKs8PDvPdF3XMnjpUM-reVML-2MTKzrR_8STRh_llSBVwPOed9dFYQ90mvOcaAJIMhd7DmWf_yIDfAaZXx_-fUYf_SPM6XdAAbqzfiEYAO-sz-D1Ndn4UAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سودی که از کنوانسیون خزر به جیب اروپا می‌رود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/455345" target="_blank">📅 17:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455344">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1361d468b1.mp4?token=AQ9LknnaYhVzIIZSsiaqwfJwiX_FUbpXMr7wWi3cTCp9V1ujYaa7CWsBTNejIxa7K4NClJ2p1mUt299AaQ7Wq3yAMTShqnL3e1PALnfH25ZxAa-S6mRlF1kc1EcyoKH43qJHlJUMdIeEbygCNODrjBCcuAwnHpLLzoJKQZWgtaPB2kUgAbpDQMZGhBVyopKBOoa932ORJU3ac4cteQC-bYilTwZkj9a7_IsPvafsGFrQEZgAiph_IZU6dN03rZvAetd-cI4T7zcRYyDYZc0NFqEWTrtxDC7FwUJo1l_KLkxAgxImTHsR9hmJDdAQ8Zd7TaNd_aay1quOFrpjjpk3Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1361d468b1.mp4?token=AQ9LknnaYhVzIIZSsiaqwfJwiX_FUbpXMr7wWi3cTCp9V1ujYaa7CWsBTNejIxa7K4NClJ2p1mUt299AaQ7Wq3yAMTShqnL3e1PALnfH25ZxAa-S6mRlF1kc1EcyoKH43qJHlJUMdIeEbygCNODrjBCcuAwnHpLLzoJKQZWgtaPB2kUgAbpDQMZGhBVyopKBOoa932ORJU3ac4cteQC-bYilTwZkj9a7_IsPvafsGFrQEZgAiph_IZU6dN03rZvAetd-cI4T7zcRYyDYZc0NFqEWTrtxDC7FwUJo1l_KLkxAgxImTHsR9hmJDdAQ8Zd7TaNd_aay1quOFrpjjpk3Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: مردمی که به خیابان آمدند معرکه برپا کردند و کارشان خیلی باارزش است
🔹
کسانی هم که به خیابان نیامدند، اما با وجود گلایه‌ها، کمبودها و گرانی‌ها با دشمن همراهی نکردند، کار بزرگی کردند؛ دستشان درد نکند. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/455344" target="_blank">📅 17:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455343">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad0c712aa.mp4?token=ezHo2LZKlwzOh_6OMMPb8Ke48ZywxUBT8wW9nLzhoRMUxkfmfdvyq1HEACmzDvt2ywJFw4N-7WZZ_sBwDRhZcOzycx_IVFWrF4TWB1TUERk5Tgyybh_Gv5Lu7Xb1uJYo-JI5cNesrtSgOc_6OY5L8fugbakVT4PLZO3LDPUpYLZHSAQQsIihRSMwDkgAezIykGRA3JAq23dn83xPZD_DByglhI2Mmykh-QZJtkviJ9sSj7_BYcwxLsfxLxQzYctyddvESy-6E2ZKQQ8-yqmFghLtODC5arkIjwthd-N2Zm6MDJXBy_XIvPyvvijcTMSL7gouAeoU21s_Gy3r6O6T1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad0c712aa.mp4?token=ezHo2LZKlwzOh_6OMMPb8Ke48ZywxUBT8wW9nLzhoRMUxkfmfdvyq1HEACmzDvt2ywJFw4N-7WZZ_sBwDRhZcOzycx_IVFWrF4TWB1TUERk5Tgyybh_Gv5Lu7Xb1uJYo-JI5cNesrtSgOc_6OY5L8fugbakVT4PLZO3LDPUpYLZHSAQQsIihRSMwDkgAezIykGRA3JAq23dn83xPZD_DByglhI2Mmykh-QZJtkviJ9sSj7_BYcwxLsfxLxQzYctyddvESy-6E2ZKQQ8-yqmFghLtODC5arkIjwthd-N2Zm6MDJXBy_XIvPyvvijcTMSL7gouAeoU21s_Gy3r6O6T1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چین در محاصرهٔ طوفان دلفین قرار گرفت!
🔹
تلویزیون مرکزی چین از وقوع طوفان سهمگین دلفین در چجیانگ خبر داد؛ حادثه‌ای که با وزش بادهای شدید همراه بوده و وضعیت اضطراری ایجاد کرده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/455343" target="_blank">📅 17:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455342">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a39091f25b.mp4?token=F8McyYssLmH-lZ8FXYBbC1khpnxC6fKj5_LwRs-nEBH187piCfVaQnqlTEN3TvbhK7Y1SyP1rN_APxjWOccPKV9F-6RhICeFd9wLbKaFE7SZfKJi4JazOw6YrFfqFlTN5X1tbWjzvxDh5-sTZA_tcZ98C6veydOLUmh-MtzLzjoMRTniiSTMchAvwI0SiqZNoMAN1e3Nx5FpDRv9Vf0qz_lNOzWygvcykjvDzUgx0yrtJ-bY0CsYv7SalXSaWcg4M4E4Qd8GzJAv1y5nk7pA8EAkEQG1eTKOCo5R7a45_WCZPXDRV1PELXpxQELkgqzgEorQihsBGkSZsuA4w-NXTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a39091f25b.mp4?token=F8McyYssLmH-lZ8FXYBbC1khpnxC6fKj5_LwRs-nEBH187piCfVaQnqlTEN3TvbhK7Y1SyP1rN_APxjWOccPKV9F-6RhICeFd9wLbKaFE7SZfKJi4JazOw6YrFfqFlTN5X1tbWjzvxDh5-sTZA_tcZ98C6veydOLUmh-MtzLzjoMRTniiSTMchAvwI0SiqZNoMAN1e3Nx5FpDRv9Vf0qz_lNOzWygvcykjvDzUgx0yrtJ-bY0CsYv7SalXSaWcg4M4E4Qd8GzJAv1y5nk7pA8EAkEQG1eTKOCo5R7a45_WCZPXDRV1PELXpxQELkgqzgEorQihsBGkSZsuA4w-NXTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: خدمت رهبر انقلاب رسیدیم و از هر دری گفتیم
🔹
ایشان از لحاظ جسمی  در صحت و سلامت کامل بودند و رهنمودهای خود را ارائه فرمودند. @Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/455342" target="_blank">📅 17:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455341">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89e6f90d9e.mp4?token=u4Nho8aFzs9rDo4l6PaoqqSQe3DfwLlkLqlR9XW_sXmjbr3u311hBF_JpokxmmjldZFSOnTK18dvIWH7tU-c1Ba-s-xMUO0wXpCT6SzTLUDc2RV5Q3piHyn0HjinF8vt_RSf4CmT5In0_OsWsoNLTAXquEo-pXi1Re8pm6FJD8Rjo9vD2GdwqOd_6b9bJd2HKT8FRwXTdUTWWaxP2Oo_TZlWkWg9aJp7L9oZuzBPT_bTkcXkcFxUMzsy1B8VqoH9ousapeE_KryWc-K-ACu6lAUyHPbTdzemjFYARyPNKSjFD3YPUCz8ooZCHOqn4LAN0LJjgpoGnPkUKClDgxVuBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89e6f90d9e.mp4?token=u4Nho8aFzs9rDo4l6PaoqqSQe3DfwLlkLqlR9XW_sXmjbr3u311hBF_JpokxmmjldZFSOnTK18dvIWH7tU-c1Ba-s-xMUO0wXpCT6SzTLUDc2RV5Q3piHyn0HjinF8vt_RSf4CmT5In0_OsWsoNLTAXquEo-pXi1Re8pm6FJD8Rjo9vD2GdwqOd_6b9bJd2HKT8FRwXTdUTWWaxP2Oo_TZlWkWg9aJp7L9oZuzBPT_bTkcXkcFxUMzsy1B8VqoH9ousapeE_KryWc-K-ACu6lAUyHPbTdzemjFYARyPNKSjFD3YPUCz8ooZCHOqn4LAN0LJjgpoGnPkUKClDgxVuBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس‌جمهور از دیدار ۷ ساعته با رهبر معظم انقلاب
🔹
پزشکیان: رهبر انقلاب بر حفظ وحدت و انسجام ملی و توجه به معیشت مردم تاکید داشتند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/455341" target="_blank">📅 17:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455336">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QmDRO17JV0WJaEvSUWdpQLC0U82_gq4PktMNn8QkTZ1zHr19wPE7pPaCQd73N_xnaBluHb39HZ-XcRwegCur8bQB6_kD86zpaM0GsEDubx6_q0nD2KuaVbyhKe1kFC7bzJA7h8yDXKbYGLcZhDLofDGLwbYWTlQxEghLo3npvicXI8zwVhFpSHpuP5T5JWTIsQcIKyjG4EilFsQ2ofW6Dc6B73Xcluq10qar0BJEPLIdfHrS_gOOHIy8z076Fve0YG1Fz_0_n_EAV9538BA32XNWoqUdChI0TpAxz78wW-b9l2mrCihi42ZM3iaxExMiila7Uko0tG7Mcg0D0tftEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqOf6tX78IAak5xrUKVTf8mOkzl36JGxPyyqJzEr-5yGz0iwMxt_Xzbe2U-CCqxw1rmpivb9qNIb67igT_dLeGToZ53mOjmzqhvO_ggURlLU5gFc022sEs8VOC3YKNq-u7Xne7eEziukY8S_TdccelBMXdeoGSSHaH4Bb1m4xWcdKJTdM3U1ooik49K2S7JWR_3A2H1MKzD0DxQkwAaP37YZoexwYDS0W_0UQdqVL_Rygeg8047peL8HU5BC0aoCsbmnEGK9VI2sl_AOdMxpviNEJWdsSRHaY6GH3Mi5HbKn2UgcswsYK-Yl1we43Flo0bygMfhASCwX2kCmx8Uc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EvKsicmJq0-FNba5Eu7m6TcLO1InH6uUeNMu2ApqVBFMNNkTCJCY1bb9Fa9L2MngceEprGf8Y25NMvf5TW50_CxM-BmCPoVRm8CZQKfU_M_9Gid459HuMnrfs9YYFKNvJoRnZtFq6W35zjd_mzFDNzAzj1wzY7WgCzKJ6wu8vsFauM6hEATvmcrTG-n-oHcxuTo1i9ntmN5xoSvVrYUEUsVfzmUiDSOdafBcXLUjT9YYIYEzjUpdF1aSXoLPkd5FGM_GO3YF3p2cndLC251i9IjEl3q5mz31F586uQKy5brr0TdK4anxxI1uT3-mfqgr0ta8TIIA2DzBQ6bA2bcKOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tEbFMTR8EL-shnwHrvx6omVfLQPCnr1cSAkhgLijIPghsQo5MvaBrzYylwm6s7bnw_jZ_P_AmFbIWxIexrHA8vLYrydYhMRilN8c2ZHd40LBS82bh-9FwUE0ytb3wlSMRzbyh7fRJ7A9569sjHvRM_i1jHNtj80DToBwYK1ZLNJ7AhK8DQgECGJCtPrE56wIJnxAeRRcg74_OLZ2S-9b0HGzng9m12qZuU6v8SddJb8Ce1r05GLozR_qOdqezQ7YsspTLjDvjKiJ21XCqvYLljGWZ7C-6Ubv0P_-EqB9FAK6D-Aqr9_l_SdxNdY09W6xr9Yk-v8STewcaTG--lLI-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ieqNmG4MeXVMvk7PK4cTnr3FC65HC-tUK5nt22rHX56IRzbMzeqypZ-43bQmLExMMAKGiSVUvTQQxW9jeF6WbN4_LjmC_9Vq81QpphhGv5wQNce4AhJxZab_67VJTDduMWfWjTaTAlL0tUEtyBhbX1fFJTVceRapOt6W3dEpB3VtD-RREDzz7J4fmLVyCeVoH7f3QU1n121VXPSaQHKQ24zCDn5QIZwq04yO7xL0CZqWsgfNrIxkucYow2pZrWLtvqs5Osrj69AX9FsAa5at_y1Ab0l1WyjLbR5jDJ4rJcVoRY-7yHBmshh6FI81GiVt0OMpVW1LNWjSqroqfakSmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسیر بهشت، آمادهٔ میزبانی
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/455336" target="_blank">📅 17:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455335">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab61161747.mp4?token=H94hNXnLscQ5aqlqyGebMkUyYWMyRQmdngRugclJ3Ym7Z0wlqrXvU7xbR1krJGyn6012L-EnRBjosEfG2Zjr_zm3PPF6P6fMy9W09J_MmFUZ3zUYG1ASGrPUR3VaESRvmL_saZBkaveM8K8fB6PVe8YS354BCqH-6At4gdFTCrQf5zr8l8dAG3yYV2AWOoaRRTz04qBNy_GI-auDMCa8jVh8rx1CxezvwEyrBkQA2EsCH2VHzP0uu8_lzNvpSIHDFCnsmRP682i1ck0n7qP0FWHSTgdles2u1RmLf2FmDtQ7bKHTxLZ0c65TZ_Wc0cCWoYN2oV4J3526nmPDZMA0Vi8zJ42PZId78bXHil4f_n_jk3OTvsoEOEPJczyf_e6_1uwPNlneLLCUMtsBLZ4jLiI4AVK_1tHzhZTfkr_VZ8FSvoLtg350fNE869qHQD6WCaJrLEh75Ce_4PnOAvGTHntMPm7RErQWtC3RlSQ6ZboYVpavwdLGTNFNHet1NIoZisDVB6_Hxq6x-0xx85k82XvPqa0T2SjnVt8aIA9Mp0gY8sJ1Va5vJQMCMzGHRJ5fPRxJkhrJk6_mRXRYdlYVewC3sXOtT1Wi0GX1-lDSAZMAAxg0vcBOC8dHWMFnbTcCc-Ap1POmy3wOqkW7ROm-E9P8UT528yX8PAixRh2TQK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab61161747.mp4?token=H94hNXnLscQ5aqlqyGebMkUyYWMyRQmdngRugclJ3Ym7Z0wlqrXvU7xbR1krJGyn6012L-EnRBjosEfG2Zjr_zm3PPF6P6fMy9W09J_MmFUZ3zUYG1ASGrPUR3VaESRvmL_saZBkaveM8K8fB6PVe8YS354BCqH-6At4gdFTCrQf5zr8l8dAG3yYV2AWOoaRRTz04qBNy_GI-auDMCa8jVh8rx1CxezvwEyrBkQA2EsCH2VHzP0uu8_lzNvpSIHDFCnsmRP682i1ck0n7qP0FWHSTgdles2u1RmLf2FmDtQ7bKHTxLZ0c65TZ_Wc0cCWoYN2oV4J3526nmPDZMA0Vi8zJ42PZId78bXHil4f_n_jk3OTvsoEOEPJczyf_e6_1uwPNlneLLCUMtsBLZ4jLiI4AVK_1tHzhZTfkr_VZ8FSvoLtg350fNE869qHQD6WCaJrLEh75Ce_4PnOAvGTHntMPm7RErQWtC3RlSQ6ZboYVpavwdLGTNFNHet1NIoZisDVB6_Hxq6x-0xx85k82XvPqa0T2SjnVt8aIA9Mp0gY8sJ1Va5vJQMCMzGHRJ5fPRxJkhrJk6_mRXRYdlYVewC3sXOtT1Wi0GX1-lDSAZMAAxg0vcBOC8dHWMFnbTcCc-Ap1POmy3wOqkW7ROm-E9P8UT528yX8PAixRh2TQK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پژوهشگاه رویان: اروپایی‌ها ایران را برای درمان ناباروری انتخاب می‌کنند
🔹
شاهوردی، رئیس پژوهشگاه رویان: پیش از چالش‌های یک سال تا یک سال و نیم اخیر، سالانه بیش از ۵۰۰ زوج نابارور خارجی در پژوهشگاه رویان پذیرش می‌شدند.
🔹
بیماران مسلمان از کشورهای اروپایی، از جمله انگلیس، برای درمان ناباروری به ایران مراجعه کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/455335" target="_blank">📅 17:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455332">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fedab4855c.mp4?token=Q4nKnliThZhGyN55aQ5vgFzIfCKtIQe86BEZUNF7jysGYG_ZyDIY6Qn2Lnyw56nYRWb2RLFFWM5jFHVPrVlc6D80fXj6BoTR1bcMF3QT7BC9_l8ffyyuvl8FgKXEgSy4XHm24lxQkkqCEuF-1dAkTvq3PSe0-bFQw1fvMyfaI2LLgPaQfvGQ6XZ4ZdmgmUz9CNe_hyO41eWt9_PkcD53vPrRxnNEQecDBkQu9MaSiPrDRYQ3PnKUG5d9fMuOCGmGLciPq58YwcwwaYdROA4wXLm-cROaVoeLXsPD1UuMxh0sfLsOryJVeUCQsNsc9xinoZajzUvqlD7ATKzwJC0YvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fedab4855c.mp4?token=Q4nKnliThZhGyN55aQ5vgFzIfCKtIQe86BEZUNF7jysGYG_ZyDIY6Qn2Lnyw56nYRWb2RLFFWM5jFHVPrVlc6D80fXj6BoTR1bcMF3QT7BC9_l8ffyyuvl8FgKXEgSy4XHm24lxQkkqCEuF-1dAkTvq3PSe0-bFQw1fvMyfaI2LLgPaQfvGQ6XZ4ZdmgmUz9CNe_hyO41eWt9_PkcD53vPrRxnNEQecDBkQu9MaSiPrDRYQ3PnKUG5d9fMuOCGmGLciPq58YwcwwaYdROA4wXLm-cROaVoeLXsPD1UuMxh0sfLsOryJVeUCQsNsc9xinoZajzUvqlD7ATKzwJC0YvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سی‌ان‌ان: زلزلۀ ۷.۴ ریشتری غرب کلمبیا را لرزاند
@Farsna</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/455332" target="_blank">📅 16:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455325">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMA6NBWkiY8qaX5x8_wCxp31MrX3XYaClteceYUwDvumTHNclZ3BNRmrIlopi6P5CKB1zBK_BK8tEi8fAt3xjotGRuOwZilaWujwPQUXSXjopw3O-Ykg8Y_mLqoIt9GHr82mntfA-yFmiWfl6F8ijvf2sWxpDViPMK0IC5jDhnDkn0b3MysLJgm1OASJO4XZfEN5FvmlbToeDfd3ifryCuY3MYpBS_OCVISqjSAPWaWPg0fkFsrvN6NqZtpbKlUEYL6E548woP6H5TAnTZ-9U9bvxIKDSuawCb-sHe76kYV22R1dYIm0m9DcR8qKDM9WmHYNgFkLcix9bI7vh4QWSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CkealDVSyT3EdGOyFtiQYVaTP4np9kxDwzSr7CcxQ-zZipVypbhQlyShY2IiC8hJw4YtK-aWAdcGOpONqgBM1ks0ExjdyTRc6nh40Jw_GhwKkDW_71KrTIqvM_uPFTKLUTd4p5A2T07qb1FMO90nTEMknZBn01vDGXnZcoRxfCh2JwmDYQFJXgqW9oajYkUpwZMhhWjLLl7-ztmTRaNRK7pWLUk80OcTLon7zRjDqMpvbPyepXcJR5KpDV9RzCnbiVkFz7OMwnqTvqLJH7FcaZwx5rtHOamQmP2lLfjQzIRa9DPli-MK9ekapp_7uXz27fJtoeXukIJqRmulq6mohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQtP993Yh5zOC1GxLxXHjT9I1pITeTfX8FcNPj7BLMx6FVLkfIQ01ljDFWTT9YWudR4tbhAOcvwJB-Q9Kk8Rm1MngAs-DDUS-u8sZlrvNch0jKXLYcPpoGfALxw9aYcdF0ydCJhFb82GwU8yia7pGymuqmW1cee514l2K3lKamZFaeufnGRHhxfnv14YyR4MQd5r_vKAt7ztKj4BDiNjiEkI0qmw3YlsHWNhgAkRWWrfdudKgOSlpap9bbxHAGXcOSr2kM_JnbSary4n5hJ1zL1Frz4l0xLwJAccVQ9ZucOTP-MpwY6BW_YFbIi6rDGTTr9QGVHnvwGtVMlizK9mag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MBG0Q5cYpqaD5QoWMhFMV4MV8zJm7KYX07WWJfegjVMItjxcTpfedayETP8Pqd-Nnl-nI5rQe6-ZhNOMDIdci3ZTwmq7S0NBZ4j52Fil4_2923WPpphVY0JaTU_KmjrmK1YmYzu_1F9eZFPVBKtOhw0hrjIeFT5qmCTooATHFhit5VPSbKLxRajS1bHrxxiiwMEHd-OFk3K-vcG6oWZUHZa8rrt8EyainzND5FU6c7xgdG-RDkVFRrIQrgcAUoTgHDV62k7KvC7zu6xMCVNIad379dfMHupwSZLopk3SGkW7zaedRDfV_HrWj1giLpov-DeEk0r75zxq6WQ708yCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYFxxPlQM_9RTg5VrHmDiIz7vcNtKSTg9eoVcKe_oLFL8szZovdDWjzyf8dXFjzgctl4Nboh1MYVJK3AK6hTwNf8hvpMxTWlmhcaQUnCoxD2i3wguXwlT_dNb6WqhBnYEA7X6rgx_9pGqs6pQSAHky8DXrpJ7KE7fnDH2QwXEEOTSBNJnCwEOjMrI8Lafb9P5n3M_wcWP-eYnYRvhGSqwKU44Yuyn7GnOsOT81_TWSvXptNb_cpJ7xy03EslpTWJ4NmiXPKLvpDOcIKPwd76Wk7fuAp57rcBLe_Si3ZDzYzl1s8saJ9KNQDf2tmPx00iQmOl_lRIVGvbJEAz2IrFXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnjq3uDkoQhDWH2lcOUASI02LsGcH72Fbi0tQK_LcvQjJLl8KZtJTiuVOZoi2epNjJWXN0Q4fXYfradMUYLHYykeYHMlHbYS6KGPzSb-L5wDn-OEd-JimeQDKDaNYYwnYCgbWCuLf_fXAq4jE8_AH4O99i6T8bMMDXwROaEoiXxKoUcqqhGYIRHbqwLiO6vKk9n5uWgS9BibvXKqXwMTGSxaG4R7BjlrWFAkYimow6RCVFhITubmF_O1hDUqEvrR0lZe4kMmNC7XQd3lu7SofsgB5_lWPU8BJHaenbE1XoH_D8gjh2t5kX8fnqAWKUigZwXkCrfnO4KYZNhLYiVBoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o1dsH45kaxvIb5Yi4cBEQUEpg-nZLnEvLqsqzyDATBr-wJhumMhPKj4UMGPJCOR1cJ12hQMIKX6TZ-CNpmzjMQ5-y5OsccMAaJPP4_XNLk2rjBcQQrsYccXwzbCfpRwS6z1c-olEkJSSh4QLXFLR2aJ0hhKAy0xpJ26JT8v43exdPWSD5K_MHd113jmIfUBbaDXKKiN513qo4_K1g1opOGuMbpQYpgkZ6wVXAtzttYCsqrVIqMlUleJ5nwxjgr9TC2xx1sqKYKbBhdiGwsssm8gLBIg8fG9rm_0Y7akhk3YhU-xs1yQNnmGii7qEqZRtvt2cweZxM-ZN2kuQg6hIuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم تجلیل از خبرنگاران قزوین با حضور سخنگوی سپاه
عکس:
امیرمهدی زارعی
@Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/455325" target="_blank">📅 16:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455324">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYAgdxWAAo60MKlLFeLG8Jk903RY3BfMUlnzYY8k5S0HYlL2wPMxWdLX_Lcqhm1woWFF_GCgkWCHkV10BYLuzs2tAZbQVPRO3szNSXOAAh3uhJc5EDBAKvzy2Y6UjCowdTFqL42sAent-QPVQ2_UiXqhwE_AG73aMmILa9Tx-WQqhq4lsU2MM3UWCfzvQBKVCmGdxZp0ALban36rseeqGXo3LaUFtDOqsrLhvVbDUKc6sO_adaoA64lg91qQUpedRAmMPJKixjo_z1qEIG4K9PIoWAJ9UVxqZ0bxsKeURGxbA-GaMtOmANhcoC1ImaHuA6_VXKkWbPERugbYnsnr_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باغ‌وحش غیرقانونی انزلی به آخر خط رسید
🔹
باغ‌وحش انزلی که بدون مجوز سازمان حفاظت محیط‌زیست ایجاد و شروع به کار کرده بود، طبق شنیده‌های خبرنگار فارس، امروز دوشنبه به دستور دادستانی پلمب شد.
🔹
زمان ساخت این باغ‌وحش مشخص نیست و مسئولان محیط‌زیست می‌گویند «تا چند ماه پیش هیچ گزارشی درباره این مجموعه وجود نداشت».
🔹
مسئول باغ‌وحش انزلی علی شرفی پیش‌تر در مدیریت باغ‌وحش صفادشت فعالیت داشت؛ مجموعه‌ای که به دلیل تخلفات متعدد، در سال ۱۴۰۳ تعطیل شد.
🔸
پس از تکمیل باغ‌وحش مسئولان مجموعه برای دریافت مجوز از سازمان محیط‌زیست اقدام کردند اما محیط‌زیست اعلام کرد برای این مجموعه مجوزی صادر نمی‌شود و نگهداری حیوانات در آن تخلف است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/455324" target="_blank">📅 16:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455323">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlYgwnZ7twaSYJ4iTkTkI_cjVLm-HmWVZk18OEfk6tTUsCa7A9-L1-iKYaA0PeunzkaXxiQLF83VxGyhZbTrdfWl1-FYeMPZau2271_7dpVq6rF6AB6xZH3OdIz2NWvmM4MEBktQg4sE_absGTHXm68qssxzUEpG8cJbYcvT5tVGaUb8ePaI59WTduQdkmowGwCdMwkvEO-JEiq5SqXfqAh1ZuxVMDzRQCHP7gFzWQr0H9aQ9xTuaXFwBe9ipB9skJ7Vx76h1DdLk82zCuz842fHA307SGXIxqpDm-Srgi8hKiFkzkWZwfujzxbfwXiHdu9B3tT1mJo7UC8hqLVa1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور نظامی اسرائیل با پرچم باکو؛ حفره امنیتی کنوانسیون خزر
🔹
باتوجه به سابقه همکاری اطلاعاتی، نظامی و امنیتی برخی کشورهای همسایه شمالی ایران با اسرائیل و حملات این رژیم به کشورمان در پوشش مخفی این بازیگران، به نظر می‌رسد که تصویب کنوانسیون حقوقی دریای خزر، دست تل‌آویو را برای حضور نظامی باز گذاشته و کار ایران برای تقابل را دشوار می‌سازد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/455323" target="_blank">📅 16:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455322">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CV--mf_yF7dVQ3pp96emsXeR-5m9QvZGM6lxgtltUm23eiHUpJcPkftwiW4KF9NLwM2RJaFqrVE6S9wmTWC98X0miRYE34Q38ljC66fTokEosEruZX_eWoyGbbFhp8LwLheepE3JH48D3h6f3fQ9xBWw7n2eCMgqSly0v516tHMH8sVksnpJ4wRVt0wRSkMFhSderchdmquR6Fdx5gMFEWULYgiA9yzp1grERbsgr_2qQbN0b2WnGV5mARhQgW_rNMx_UUui2BUNxx-XAQTJBpTe0TU6ufj0EEwMeObB3daH4RxMcDG01utDBDst9XXTGPbGfiLB7isztCQ1HtZjNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیار و گوجه هم شناسنامه می‌گیرند
🔹
رئیس اتاق اصناف کشاورزی: «برای گلخانه‌ها و محصول‌شان شناسنامه صادر می‌شود.»
🔹
صاحبان گلخانه با مراجعه به سامانهٔ یکتا و تکمیل اطلاعات ابتدا برای گلخانه و سپس برای محصولشان شناسنامه می‌گیرند.
🔹
شناسنامه، فرایند تولید و سلامت آنها را از ابتدا تا رسیدن دست مصرف‌کننده را نشان می‌دهد؛ اگر مغایرتی با استانداردهای سلامت وجود داشته باشد مشخص می‌شود.
🔸
چند سال پیش روسیه و هند فلفل‌ها و کیوی‌های صادراتی را به ایران بازگرداند؛ مردم هم معترض بودند که اگر آن کشورها به سلامت میوه‌ها ایراد گرفته‌اند چرا در بازار داخلی فروخته می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/455322" target="_blank">📅 16:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455321">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/657a35c5c0.mp4?token=qIO9hPQhoHmtNVjbvyYnQ0OmGeTHgM2WwjqY_5-ApdvQaSf8R_jlRqQI4eKfgQXdPpnS2MVDiYM5z0p72CCjwz-EBcM5QZ1Chvf-LuCZu_gnvYFLfhebexwKN1mw5x6fKDASeco2RUt3B2N74xSRf84ZZNxZha0PSx5Al4glV4hZQ9DAIqPbM8dHAvPM8vVQhQ6pzv7KcwH6Gx3wqIKOYpKav_aQL6qlEwFVhDfr4WbbErdJo-_ofm-xtRGyv6nZr2yPhxmYcSOrxbI6TgQI2QLLm2iezQeTw6BED4vOUVN5-uadefmXsZ9BUmJfu0NhvTlGdc52ToJqicx2NPJC9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/657a35c5c0.mp4?token=qIO9hPQhoHmtNVjbvyYnQ0OmGeTHgM2WwjqY_5-ApdvQaSf8R_jlRqQI4eKfgQXdPpnS2MVDiYM5z0p72CCjwz-EBcM5QZ1Chvf-LuCZu_gnvYFLfhebexwKN1mw5x6fKDASeco2RUt3B2N74xSRf84ZZNxZha0PSx5Al4glV4hZQ9DAIqPbM8dHAvPM8vVQhQ6pzv7KcwH6Gx3wqIKOYpKav_aQL6qlEwFVhDfr4WbbErdJo-_ofm-xtRGyv6nZr2yPhxmYcSOrxbI6TgQI2QLLm2iezQeTw6BED4vOUVN5-uadefmXsZ9BUmJfu0NhvTlGdc52ToJqicx2NPJC9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نقد هنرمندان به تبلیغ عجیب یک تاکسی اینترنتی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/455321" target="_blank">📅 16:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455320">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2571d3c962.mp4?token=mVlovMaYhHvQepvEFrr0LN6kIDq5BGs9D4KLnEUS0u4ji9VTtjjSp8SwbmX0iKyC75YHiimKb709JA9Y1Li0e-X7Z-xklAknOdj0oqYHLGv7Q36zDk9L8o3HaPZ49QcTt0CZyZer6PhAc-Yd5kPXpSOb5MCVY3OiS49mHwMFnYWtrxAwquPTAwVt_UgqW3zz46JrRN0XWPCwc-sJ0g_XnlE98Yza0de0qP43X1x3-Ckd9OWoqaBXwzKxzh1-qTX61Ivw40ztHNTBycs6jSb40VeL-yKEJ6UWAUwpAFtlOqE6eL7WqlYL5g3KzSaZb3XDEdbOq4rF2AvSPa_fGLKXlmD1_ZyiqEJLr6WxGCeVK2mzAL4H2t2GTm4GB2hJ0Edj9_kZ1DTJgJwm87DEjlbP1UM8wWR7QWfPwzmReGsPkRB1eePvJ4oERcq8Kx5iuOQKVnwzXny1KcoQ6eT0Nmy4_KjZVHF1uCZ48I-RFf_s3To9MWKKX5S55mwBOE45Ly-lk5GxZjuXNtfQKdoCAKkskU6SeYhpV2_zjjEzGKJjKvU8XRbIwhI5csh00zRWRglLnKW7pHa5oP_KJQ50CHi2MP73oGRlVc76U7G2nqE6hnMilv6UzFavG2g7_jieW_tjptJVomuE8EKENOE5kGkogATCOxjwUr7hV2zh6Mevr7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2571d3c962.mp4?token=mVlovMaYhHvQepvEFrr0LN6kIDq5BGs9D4KLnEUS0u4ji9VTtjjSp8SwbmX0iKyC75YHiimKb709JA9Y1Li0e-X7Z-xklAknOdj0oqYHLGv7Q36zDk9L8o3HaPZ49QcTt0CZyZer6PhAc-Yd5kPXpSOb5MCVY3OiS49mHwMFnYWtrxAwquPTAwVt_UgqW3zz46JrRN0XWPCwc-sJ0g_XnlE98Yza0de0qP43X1x3-Ckd9OWoqaBXwzKxzh1-qTX61Ivw40ztHNTBycs6jSb40VeL-yKEJ6UWAUwpAFtlOqE6eL7WqlYL5g3KzSaZb3XDEdbOq4rF2AvSPa_fGLKXlmD1_ZyiqEJLr6WxGCeVK2mzAL4H2t2GTm4GB2hJ0Edj9_kZ1DTJgJwm87DEjlbP1UM8wWR7QWfPwzmReGsPkRB1eePvJ4oERcq8Kx5iuOQKVnwzXny1KcoQ6eT0Nmy4_KjZVHF1uCZ48I-RFf_s3To9MWKKX5S55mwBOE45Ly-lk5GxZjuXNtfQKdoCAKkskU6SeYhpV2_zjjEzGKJjKvU8XRbIwhI5csh00zRWRglLnKW7pHa5oP_KJQ50CHi2MP73oGRlVc76U7G2nqE6hnMilv6UzFavG2g7_jieW_tjptJVomuE8EKENOE5kGkogATCOxjwUr7hV2zh6Mevr7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران تابستانی خیابان‌های یاسوج را زیر آب برد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/455320" target="_blank">📅 15:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455313">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDGc10XFQlSk8hs0J8wYpIesxBD-OMwZDY-EAz2Y4S5iUnNHTBpU27d71SDMnsM-uez5OF6_FXuemB6wEpkynUVgrdLBY7G5IJ9SQHSNiuELWMxlyRoZXGu9uTkVa8K5WzcVkrCxIFJK7-zrrTMcTrWlx4CjWYtO-a1koIjCVPiBtzPartxpt3FKEb_MAdRDPpuOE-Y-gaY63yMj5beTONrrLnlDmbjXpaZLsPXC7E_WrCibNuf5i32EKdnBqiaWaUdKCE4NBoV3gS7GqoknPA-88mvrHelkvEYNdIzFCKn6y7i7Bkgq-2OGk90_cdzTWr_v2Yf0ToZ29ZFVicudbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/guXAQs0SwdkwLXNhFZntnx68bRMOPdDeij470i1jq4toa99CXpikBaxuFsWw4LwJgZ6Rlo5JHlJqVJmHBY_z9ZCNf8mftIGo0lvHFvBDVKvpue4NQcqPWHgI1EVKAEAMnrJlXY-D8uKVwTxc-l3NKRtfvjdGAMHqByfR8fybBA2vwBLDqxyEZo2F8CnsOAuC59CCbQVOlLP5ynjIF-7C2Kznr0StuxwbU30Mr2PaGqF6l2iJSF9XtcEkOawiyfRjbBbwvKUDGaSSjynr9ISNpQIMOX24MSQoAvsg5X65JJFNIN74HVDdABsTlopk07X1Nf8QLh9CtegD-VekH1zT3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FhAN54HdYD-HNKcNfWlHNw9qzJsP4tw8ffTbN9WNblrwqgRa1CowoaIJtEvHzlXxut4-vvk-p3wAyYJ2XtJ2d_jG24zeCc1jkAe1fgIeDZEFmXY-IzDvJiFRc2No0_VoDR1BkWHoIahWBKNf16J9D7Q8O75MpVBCV_BJovcIjghsMbsAPKkXzLJa6p7tjw2jlFpKlvYCdCS-muX_UpVcKLQFCgjR32BZDA1ukHzsEAo6ondn9CSdi7zGftQHTMUQy5COMPcVVdJ7LbBR5acglHMY0JNba7MUnRRw4NN7S9QMlLVcTky6DttFIjC1qHs-tt7MnXv_ZDSXZ_rS3qbt5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tscpHlZpixeYhqXqvRESDe4ivwCBIy4vJNp3xk8hCpsVZsQQBbv6bjrSUkXNpOFSG90QeKyhWSzoxlROvrKiUtDzenWrUgWuCzzlO84ymttViwX1ARnc-2FR0u_lcSw0q4yP6GIHdSKO3-Bjx69EyDcgqaqDd5rhqs7ynv44f6BLPMVbB7zePUxAGJmgTnbZXfmexLlhJsxeIAHUUYI-ISZpqssY5AOian7D_WbTZUVnH6eBUDlsLECnnjWmJUMZwysQJbjnm7RJdfQVLXcH1UyXNXBq6dtRAPaOI0g7o1SP9H9heFinkTzi-hDQurKwv9FTS9ztmUoHSYFFuPHIKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/THf1SftUhzXvrHzuucHiizIlXKqX6yv6PwuxJklLTO1N9e5kmyGMWHtyu_GY-ivtHTOum9MuGPF1PZ9JSRRgfCf53V1OTAVGbRUB0oP29S2HCVWSscXZfXlO1nV9Rv9CpeH76fASHYFOhqgRINmyHL9twps44fvYRlGu2A8PJ9JbwfShxiIz4fUixBrL9d3hPbDRWQT_DCARAw8GLVCSj5SUlJZpU817mGPRydlVDv5U-V00CxGYemGFZ9jipqCa_Jwu9kYnVaQeHl5d1eiwB3EkISrQl-vsquDatFzNA11zj6jOxSUMf_8XhfW6Xt252jCsiM0hO7Lyq7MJYecutw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntK5q2WOlFsPqVraMo3AKMkskoa-fNivn5j43r5AeFO38Ti9Eux7_8hPWH8JltcUd0jfB-qMCiJ89zviAGrhmVQaQWtNOZaXto8QQ6d1sQXIniZA4plYxmvg53dPVlQlofYUxcoIIq6R8eKWRM7GXlDsgMKR251hSUTcjqJU8WO7-OOg9a5XdDj3kfKGMFBjr6rmaXevp3EJ6w2aTlvUjj2DY7iR4qd_qb8Bp9WUKzeyA5CqufDQxY9eTlWIwvytsGqdDxg4vO_4_lN0UOkDFVeSdLLuxTflMVfReq-sLCL1LqA6_xb6I0KT3eZB1pdyV63g0y7WE5-eFDGqljLqLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Me44qhIEBHdshV6mLBDfpFVym5vRu6hLZ6AasDnlPBLgiPXIzro3bfW9cKV8DZNXP_zAvD--tEnck3k7L1eecXc8RSMhbidNwxiCglkLlKi1Sl3rBALo2AkDhd9gRSR2wWZ2zqAKpaorNw9UyNScYlURQ7BQRbXmnCLTziFBlLxBusyn82V7LDVNVyMereD64gpN16FsF59J4q1Z46jamdx09T1_vK9JQRSOsAU0hftsoVOgmmasZ-rK3L9g-Gfjb_DesBH9Gt6UkEsaxSP854uen5KwXaI76BUBU2iaIfC2yCuulTlXBxg8WjwP-tLlDqpigdhU8W8-nhOV8_Kpog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور
وزیر اقتصاد دولت سیزدهم در خبرگزاری فارس
عکس:
هادی هیربدوش
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/455313" target="_blank">📅 15:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455312">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvPkxT3XjX48mKIeMF2hgTwhi0jCEkDTcuIJbOcs6Y2jARKD330V22Om_Qa4mUlCBCcMZEL5BzzMHdQlYaPp06Xj9s4lbu4Is-gp_5nvVlJhoheaUwI0ddQNmQ1WBKUo87Ffcf0HDga3riXT-Vo1FavgPvBPFAf9C1-HlsREmsR8iQWnb44J8GpdJiYNFdDsrGSdeUYkHBQsi7WxoRr7eTPcihcKrGnn0y2bz0JxH-LHSvc5d_2MnShRez_MsugYsRRdGtfK3gHIoBdixTlLgKdSB6z7oQlYhAh2XxizFhj9lybN1LAlolFktQn0WtT8qclHiDn94l7Eulc9GA3V1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پزشکیان: هیچ قدرتی نمی‌تواند مردم ما را وادار به تسلیم کند
🔹
مردم با حضور در میدان، تهدیدها را به فرصت تبدیل کردند و همۀ معادلات دشمن را با وحدت و همدلی شکست دادند.   @Farsna</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/455312" target="_blank">📅 15:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455311">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdLxo_pi7acTris0K4mk4wUc_EezeqnYVD9c9_mCrpFt6MQpFlj6xqKgllruLNoJP4hlJ3LB3nuLocwwI-kZ2xvehuZe3YpIHPBPPryybgzz3CcgdGs0QQayVBbAu13SP0xJRGJ7ue9MBDA_tBJpuICi3E-MCQCLngqXDDhGKEzOXAUbEeZQleZOdUqrVjQFSUR1KNR2_3Sb8rf4_01ZR3mY3fkIBYyyVy4bmKV1mjEs_bWN285GYF5BbeFCMIeqKPdLiTllWnQ8qJORe4Buc4TV0nPPNqQpW8HcloqhhVY6wEeAXQZOEDFZOSZXAd8Q4LBxgO-xNwIEGuuwq0VztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: موشک‌های ایران قابلیت‌ تغییر مسیر دارند
🔹
موشک‌های ما قابلیت هدایت دارند و حتی برخی موشک‌ها می‌توانند در برابر سامانه‌های پدافندی دشمن تغییر مسیر دهند.
🔹
حتی اگر برای موشکی یک هدف مشخص شده باشد، می‌توانیم آن هدف را در میانۀ مسیر تغییر دهیم و هدف…</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/455311" target="_blank">📅 15:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455310">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/192af346a6.mp4?token=QQNv_pLQXj08O2sfshRiqMzi5iKNYIxTDeJQsAFlt2r3H06rOrg99QcuNVhg_MP10VVwlaCk6zMB2zZ8RrnAy0LR2rRaJdtmXFWCThSO-j9mNhqKNX8A8DNg4WkUVvl6hwtr7dQx-haaTy4fSDpe33wEw1aG2P4_joSF6dWgBUJhoTMS64i6Z61h_TxTtNKIeWgpDpgzzg-cBB4I-WUUrrLRDxOFuwrU6x1WXMSWQZ1hCEV0fu2Utzzw8PZKmjl7Q9t_xTAId8loqyyhAl5cO-DYuoSXRvpm3-Cjem857IXHFc6f9-uYIPGFk3IDBVnrPQHAaAxwULcdm_QC7TIDjQZo89bHNSkViB8fdbk9MAVGII7riKk-XVZgOoX9TwAEEGjraVW_mTM4HkLGTDA27BCapFTEyMI0LmjWuj2XCqVYX_xaue0iOx9zDY_VFwFESXxZgoiLABR9U0IIYHB9Tv_z9wkFDfSzHpqA7nT94ipjEfsc8H9oFo-7dTDbOchZqDLvy8gKxohufteeDLe43xam1WJcwewl2Q-Bnjkj05EWzAXM7HkxFXESSMHFUHd58jKCvSmxhd0yfvZCUUyvaxpUnoX1px3tf7GHt2FCu24vUh4vwvCUeNFXcWlR_TOOeGr2Z34wWpDRxtagblVbZ9TMUW1In66Ric-kCyxhMec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/192af346a6.mp4?token=QQNv_pLQXj08O2sfshRiqMzi5iKNYIxTDeJQsAFlt2r3H06rOrg99QcuNVhg_MP10VVwlaCk6zMB2zZ8RrnAy0LR2rRaJdtmXFWCThSO-j9mNhqKNX8A8DNg4WkUVvl6hwtr7dQx-haaTy4fSDpe33wEw1aG2P4_joSF6dWgBUJhoTMS64i6Z61h_TxTtNKIeWgpDpgzzg-cBB4I-WUUrrLRDxOFuwrU6x1WXMSWQZ1hCEV0fu2Utzzw8PZKmjl7Q9t_xTAId8loqyyhAl5cO-DYuoSXRvpm3-Cjem857IXHFc6f9-uYIPGFk3IDBVnrPQHAaAxwULcdm_QC7TIDjQZo89bHNSkViB8fdbk9MAVGII7riKk-XVZgOoX9TwAEEGjraVW_mTM4HkLGTDA27BCapFTEyMI0LmjWuj2XCqVYX_xaue0iOx9zDY_VFwFESXxZgoiLABR9U0IIYHB9Tv_z9wkFDfSzHpqA7nT94ipjEfsc8H9oFo-7dTDbOchZqDLvy8gKxohufteeDLe43xam1WJcwewl2Q-Bnjkj05EWzAXM7HkxFXESSMHFUHd58jKCvSmxhd0yfvZCUUyvaxpUnoX1px3tf7GHt2FCu24vUh4vwvCUeNFXcWlR_TOOeGr2Z34wWpDRxtagblVbZ9TMUW1In66Ric-kCyxhMec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس‌جمهور از دیدار ۷ ساعته با رهبر معظم انقلاب
🔹
پزشکیان: رهبر انقلاب بر حفظ وحدت و انسجام ملی و توجه به معیشت مردم تاکید داشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/455310" target="_blank">📅 15:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455309">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‌ دادسرای جنایی: پیکر حمیدرضا رجب‌زاده اطراف تهران کشف شد
🔹
براساس اعلام دادسرای جنایی در پی قتل فجیع حمیدرضا رجب‌زاده و دردسترس‌نبودن پیکر او، سرانجام با دستور قضایی و اقدامات جنایی پیکر وی ساعتی پیش در اطراف تهران پیدا شد.
🔹
با حضور بازپرس جنایی و تیم تشخیص…</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/455309" target="_blank">📅 15:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455308">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f435611b7.mp4?token=b5G1EGYSeqDGATmjVLY_khCcd9chHJreEugy67imCYw86O1SRkWcgDOaoMOl-8Mi55Ru4dHjkUmYHG3qin231xYtzl5FRUy0AvG2quVs1hll0d_pk40khmDEUC9beSUscukvGqHzmww1fLFHhe7wxigxKgivVVmrMpqyjb6taXZS-eoOgwuz87ggDV6YenXzOamsNHmZzOd2UNIYc3cJQe2Vjx3-HMDg_BljQr433sA11xE1QX9WuvraSf9_L20crSTnzeoJvg_MAbh2ahtzaDcmDcvyd-ud96dIfe5A5k8YpIzv0vusrYzoSDbMhd3ZkYY5jE1EoNnempwWixV21A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f435611b7.mp4?token=b5G1EGYSeqDGATmjVLY_khCcd9chHJreEugy67imCYw86O1SRkWcgDOaoMOl-8Mi55Ru4dHjkUmYHG3qin231xYtzl5FRUy0AvG2quVs1hll0d_pk40khmDEUC9beSUscukvGqHzmww1fLFHhe7wxigxKgivVVmrMpqyjb6taXZS-eoOgwuz87ggDV6YenXzOamsNHmZzOd2UNIYc3cJQe2Vjx3-HMDg_BljQr433sA11xE1QX9WuvraSf9_L20crSTnzeoJvg_MAbh2ahtzaDcmDcvyd-ud96dIfe5A5k8YpIzv0vusrYzoSDbMhd3ZkYY5jE1EoNnempwWixV21A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید سپهبد موسوی: هرچه تنبیه شدم، به‌خاطر خنده‌هایم بود!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/455308" target="_blank">📅 15:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455307">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_-pGH7fuT3Wd8FGl0bQGrVzxvFnTJW1Hj5xckOV7A00ivQOhgTbCFHlp9t8jKHHUibKAHUA1bY9TsoILD6Il4LFrvslylLq75Ja9OUHaUDHnksXN86BNlB5Y_jElgarDl5W_tnQac4ZLapZcd_9988HKeujS6lNOL6CXTsTf8S8YiqRu-gYIww5YllaS3rXeTjECQhJlCm51Xn3a4en9TiRTlHfZGCkbw0CWBPPBDjZ5l0Z542IkhFLod8ph0Pej9rbUGOad0m1OaO8LLvaBZTlwJgYgO1mPCR1Qy3J0PJ0GEyiXR0JFSbtPeofqu_G2napR3q9oPOryvsdbniLbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: موشک‌های ایران قابلیت‌ تغییر مسیر دارند
🔹
موشک‌های ما قابلیت هدایت دارند و حتی برخی موشک‌ها می‌توانند در برابر سامانه‌های پدافندی دشمن تغییر مسیر دهند.
🔹
حتی اگر برای موشکی یک هدف مشخص شده باشد، می‌توانیم آن هدف را در میانۀ مسیر تغییر دهیم و هدف ثانویه‌ای برای آن تعیین کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/455307" target="_blank">📅 15:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455306">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‌ فرمانده کل ارتش انتصاب محسن رضایی را تبریک گفت
🔹
بی‌تردید، این انتخاب شایسته، بیانگر اعتماد و اطمینان به تجربه، دانش، تعهد، درایت و توانمندی‌های ارزشمند جنابعالی در عرصه‌های راهبردی و امنیت ملی کشور، طی سالیان متمادی خدمت صادقانه در نظام مقدس جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/455306" target="_blank">📅 15:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455305">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDNc-SClcbz8o-jwBVMpgbQGpEhFDoCOF1O-7RH_-GRNrIb4CJOoFHigkpLMFLhWCH0BDcXFaUR-6XBIP7l20QhCI6_SomoCu-qcq6j-odwMV_tjY_wX1NLEbz0ypHhQgicp3cFUKTxrdsc9d-Fugn9ywHdJawkFg9xbpViqO2Df0HUmBxSKGIxGdGNAQJRbJJkk-4zoReCa6U1wNoGj1uyKXNl_VgiTtVq3HUraHIbEEzwuJ6XwQlaAqGSgh40qMs5iIVIkndEYPmA_nOlyGEqaI0kNEjWw2dpTTW18_1ks_gZ0Z2Zcv0CBjhh_wH-0DGAyZXPxoncm-OrBayrpeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فتاح» انتصاب «محسن رضایی» را به عنوان دبیر شعام تبریک گفت
🔹
در پی انتصاب سرلشکر پاسدار؛ محسن رضایی به عنوان نماینده رهبر معظم انقلاب و دبیر شورای‌عالی امنیت ملّى، سيّد پرویز فتاح رئیس ستاد اجرایی فرمان امام با صدور پیامی انتصاب وی را تبریک گفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/455305" target="_blank">📅 15:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455304">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRFauPEDYnXIGc4SciltWS-eJerkkN4E91h7sEpnYFl4KncXtnn77-rHwLdurJjzU-mOTl2k5r08sy6b5PYT4QzNHEIF6Qke0f8Aq_zOMH28YmZuhP2YiTyy0-qo-DZuAkdlpLfL2P6gM8zsqo46N0ecnQwQgJCtt3BASIwOouXxda-Gj-MdX4A-Kq0fUr1IMHKEBMVL8g7IiWkL-3IYhm58IAjilpJtlB_Ee0xw088GbopSq5DGPcXTs-nqGqx9VIRXROAiiqllH99yRb2O1YZMc0zGcyA4HGCLRLzoUE3j5wBzp7E-EN1icXOxqSAMoiPp2PUu_UrOyRbIRjIdUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسب رتبه نخست سازمان منطقه آزاد ارس در حوزه عمرانی و زیربنایی بین مناطق آزاد کشور</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/455304" target="_blank">📅 15:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455303">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/455303" target="_blank">📅 15:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455302">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجار کنترل‌شدهٔ مهمات در سیریک
🔹
فرمانداری سیریک: انفجار کنترل‌شدهٔ مهمات عمل‌نکردهٔ دشمن امروز در بندرکوهستک انجام می‌شود؛ احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/455302" target="_blank">📅 14:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455301">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec49f80d3b.mp4?token=JE7S0vIS8ME2kt9dVwmbsq3LuMqAkY1CRtEOx9NQ3wA2GNQcoAFbQEHGxDTjCXbhd5hhqf1q6C0k8w5zv0ZmwUM1H45gehii38V4fg-74rDE6cOgXV5XvdY8oQut1-0xmDLSnpspEuE9_8V9ftlWtXAOoRS1egDXbvIsZBx_01PAYwhWgOPQ3h9ONcWRn4JV0DyalCZ3maSn64YPxv-W9TpvCWLj6_va1yVRRoUD9XMUocetH9hc7R29RThFC7Jp7tPYk5fBiLQwyezBv87P7cNKvXM-BcqoxNdTwNMCVTVGiJq03kkayxB-fM6KF1bdxGHx9NxkCbtBqHyPYt75Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec49f80d3b.mp4?token=JE7S0vIS8ME2kt9dVwmbsq3LuMqAkY1CRtEOx9NQ3wA2GNQcoAFbQEHGxDTjCXbhd5hhqf1q6C0k8w5zv0ZmwUM1H45gehii38V4fg-74rDE6cOgXV5XvdY8oQut1-0xmDLSnpspEuE9_8V9ftlWtXAOoRS1egDXbvIsZBx_01PAYwhWgOPQ3h9ONcWRn4JV0DyalCZ3maSn64YPxv-W9TpvCWLj6_va1yVRRoUD9XMUocetH9hc7R29RThFC7Jp7tPYk5fBiLQwyezBv87P7cNKvXM-BcqoxNdTwNMCVTVGiJq03kkayxB-fM6KF1bdxGHx9NxkCbtBqHyPYt75Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگیری پزشک قلابی عمل‌های زیبایی در شهریار تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/455301" target="_blank">📅 14:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455300">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUeFgLZ8ZIwFyGX_7qh2P_Bje5rDd9WU_6-4YPpxlBf8t2VfmT0b_JstPK8c7JBhUm76iR_5fiO8C915LI1BQVQOZxH8AaKLVB2brBkZnbZyxg7esTU8V44GedTFkJUa5S0jM2w6lGYK-FAR1H7fihIewY3An3-TAQ5Uk-s0bCcxGlPczVA3scjtpBYghEG5O6CGtaOdxnJobowPTv1NlpBikti7seJ38qVGfCDLBtcIyXGxnTsdDM9HS32AUhtYDXpIlhXUD7w2ah25nNZJHZvBtnYcFz5UwFL_-0uaP7Lg2cDXIu3mMfLWU_PV6WOixrKo8k_f--QJ1_BD19cehQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلی بازارهای میوه ‌و تره‌بار تهران در چهارشنبه
🔹
سازمان میادین میوه و تره‌بار: تمامی میادین و بازارهای میوه و تره‌بار شهرداری تهران در روز چهارشنبه همزمان با شهادت رسول اکرم(ص) و شهادت امام حسن مجتبی (ع) تعطیل و در روز پنجشنبه همزمان با شهادت امام رضا(ع) تا ساعت ۱۳ فعال هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/455300" target="_blank">📅 14:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455299">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f43b18398.mp4?token=iODdQSavrVEWJK9Gd64kPJYb1aePndQsjec9jR2Ddek7KZdDeTxD5xmOahtLrjladAPz-M_G6g4auxpSGle_-kEccB_aGkjoneWWZaUMRCIdR7bwqCZY2fzSAdwTGi7GRCnDUvyO-y2gE2qg4UmNAhT0PE7gKyWcWzjtsIzvLrDBNqCXViPe_gkkUGyt161A_FL14M2_2hJ3NfV1O1MiFTzAmCz5ohOJsQJTQlo2xTGuUkW03IqUxHnzMSn1dSOZEtrD6f516F8xaNVCoLT49k3LLGKeVdTPv6J4XnUuX_tm4Qb9PhrLjT56ZcmryHG5i0AeotvHrmZ39MtFksQ0nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f43b18398.mp4?token=iODdQSavrVEWJK9Gd64kPJYb1aePndQsjec9jR2Ddek7KZdDeTxD5xmOahtLrjladAPz-M_G6g4auxpSGle_-kEccB_aGkjoneWWZaUMRCIdR7bwqCZY2fzSAdwTGi7GRCnDUvyO-y2gE2qg4UmNAhT0PE7gKyWcWzjtsIzvLrDBNqCXViPe_gkkUGyt161A_FL14M2_2hJ3NfV1O1MiFTzAmCz5ohOJsQJTQlo2xTGuUkW03IqUxHnzMSn1dSOZEtrD6f516F8xaNVCoLT49k3LLGKeVdTPv6J4XnUuX_tm4Qb9PhrLjT56ZcmryHG5i0AeotvHrmZ39MtFksQ0nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: هیچ قدرتی نمی‌تواند مردم ما را وادار به تسلیم کند
🔹
مردم با حضور در میدان، تهدیدها را به فرصت تبدیل کردند و همۀ معادلات دشمن را با وحدت و همدلی شکست دادند.
@Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/455299" target="_blank">📅 14:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455298">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حملات سایبری پیشرفته به امارات
🔹
شورای امنیت سایبری امارات از «حملات پیشرفته و سازمان‌یافته» به بخش‌های هواپیمایی، انرژی و آموزش این کشور خبر داد.
🔹
این شورا اعلام کرد که حملات شامل مسیرها و شیوه‌های هجومی متعددی بوده که تلاش برای نفوذ به سامانه‌ها و زیرساخت‌های دیجیتال، هدف‌قراردادن حساب‌ها و داده‌های عملیاتی و همچنین کارزارهای فیشینگ (Phishing) هدفمند و تلاش برای بهره‌برداری از کاربران به عنوان نقطه ورود به محیط‌های هدف را در بر می‌گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/455298" target="_blank">📅 14:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455297">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b7113c7d9.mp4?token=AFFvp2XXC8E8xPD1B-gcPheaz58cPINEQu2-CpVGpe-24h8fUlebJ3425W-lesyCmD62xDHlzMN72PAihqs0cxgayc3O1YYwzBkRT51QVz-zr_rNWXe0fOqtvANP70WMan6blbvu8wQtGu2QeYBAYXFZiRIq-ODayJC1_IZVm5yrotFOgDtOCcmWIdakFFebOYbimwPmaNQUtIBGbsRonYVZtf02cwfqpIFvyrTR3cKOy8O9GahlzHvQaGKaiFKk28nOK5o_ecI9SkZnsxs1qO0w0iC_Y0i2n0KDPNZjd8A0XbHfvsE-T9suBlimidSLS5tlXJvjktpG6Go9PWazJT8bbr1VBPE4vkeQ5y-MQ55Mx8j0jHKx3w6sV5SrA9VFzhxoGUZFJCndnEfqZDzPWUIgTCmzKNdciWcszA0WE3qOwTfNm-eVreDTSLkr6fkpGD9E9DSZyoOb6pBTUEidEwZUp0gbrvW_BO8tHgt7-eUUGa02HA9V4qkyxl-lErZ_b3j86unxTeOUtt40LVZA9QNh-ugNSf1wYsb_9WO-XlOUpAbjYOorPrxbnwBvkCr04c9VgsbRf-7mkkINEl8jg-B4Iewh1Nq4j0GfD2SpijuzVItXxCal_rTIPmJ-uBb8PWwXNkMGuBEekmv-8VwZGzGVDpxVW0PoPPRF31N9H0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b7113c7d9.mp4?token=AFFvp2XXC8E8xPD1B-gcPheaz58cPINEQu2-CpVGpe-24h8fUlebJ3425W-lesyCmD62xDHlzMN72PAihqs0cxgayc3O1YYwzBkRT51QVz-zr_rNWXe0fOqtvANP70WMan6blbvu8wQtGu2QeYBAYXFZiRIq-ODayJC1_IZVm5yrotFOgDtOCcmWIdakFFebOYbimwPmaNQUtIBGbsRonYVZtf02cwfqpIFvyrTR3cKOy8O9GahlzHvQaGKaiFKk28nOK5o_ecI9SkZnsxs1qO0w0iC_Y0i2n0KDPNZjd8A0XbHfvsE-T9suBlimidSLS5tlXJvjktpG6Go9PWazJT8bbr1VBPE4vkeQ5y-MQ55Mx8j0jHKx3w6sV5SrA9VFzhxoGUZFJCndnEfqZDzPWUIgTCmzKNdciWcszA0WE3qOwTfNm-eVreDTSLkr6fkpGD9E9DSZyoOb6pBTUEidEwZUp0gbrvW_BO8tHgt7-eUUGa02HA9V4qkyxl-lErZ_b3j86unxTeOUtt40LVZA9QNh-ugNSf1wYsb_9WO-XlOUpAbjYOorPrxbnwBvkCr04c9VgsbRf-7mkkINEl8jg-B4Iewh1Nq4j0GfD2SpijuzVItXxCal_rTIPmJ-uBb8PWwXNkMGuBEekmv-8VwZGzGVDpxVW0PoPPRF31N9H0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیا فشار خون باعث سردرد می‌شود؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/455297" target="_blank">📅 14:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455296">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qke7M1o3Jxdo1aJC8f9qrVi_CehKWwGJ5pOcK78JLUEzbzkdU8cggNgIwbCj24tPLrm0N9iis3hXzpApqZMXdR4oU7jRTvlzP9wijgDuVNR4_f0TKVtjA9hfgdHDwagU2mwXW99gOIXyH5rP8IS49BIBQuA3avZYMQs6fFRmwvo9LXNrYiclYUW38zqa9vklkPfBRZX1ofnn19TmiPETRyxye2iSOTueVCiOBbQh8-SE8EcrG3htLX8UNTmfa_BZg8D2TgNsJZj2LLnMXthtxzodKSeqmMlvB2IhipSEPbK0Huc63vuo0H5uljCmlci0VO4ykXXKyIbA2TF1kBYkOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعزام نخستین محمولهٔ ریلی قیر از قم به ترکیه و کشورهای آفریقایی
🔹
راه‌آهن قم: برای نخستین‌بار یک محمولهٔ ۵۳۵ تنی قیر از قم با هدف صادرات به ترکیه و کشورهای آفریقایی جذب و پس‌از انجام امور گمرکی در قم، از طریق ریل اعزام شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/455296" target="_blank">📅 14:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455295">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فروش متری خانه در تهران آغاز شد
🔹
مدیرعامل سازمان سرمایه‌گذاری شهر تهران: عرضهٔ آزمایشی خانه‌ریز در تهران آغاز شده و از این ماه کار به‌صورت گسترده از طریق سامانۀ شهرزاد شروع می‌شود.
🔹
قیمت خانه‌ریز معادل میانگین کل آن ملک است و افراد می‌توانند از چند متر…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/455295" target="_blank">📅 13:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455294">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انهدام مهمات عمل‌نکردهٔ دشمن در پاکدشت
🔹
سپاه استان تهران: درپی انهدام مهمات عمل‌نکرده در پاکدشت تا ساعت ۱۶ امروز، احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/455294" target="_blank">📅 13:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455293">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اتوبوس‌های منتهی به حرم رضوی ۲ روز رایگان شد
🔹
مدیرعامل اتوبوس‌رانی مشهد: خطوط منتهی به حرم امام رضا(ع) در روزهای چهارشنبه و پنجشنبه، هم‌زمان با سالروز شهادت پیامبر اکرم(ص)، شهادت امام حسن مجتبی(ع) و شهادت امام رضا(ع)، رایگان خواهد بود.
🔹
خطوط ۸۰۱، ۸۰۲، ۸۳۱،…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/455293" target="_blank">📅 13:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455292">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🎥
شکستن دوباره ظرف توسط شرکت‌کننده زن در «سرآشپز»/ یک لحظه سهل‌انگاری، کار را به خراب شدن غذا کشاند
@Farsna</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/455292" target="_blank">📅 13:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455291">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgFa0fcyBhw_gZomh7hu-ObvAW4YjyQvE3Qt7kv69MwbWokDwt3sDdgpCy20kHVPVeFcCb6h4ZjZmVcaYe2B7_WC1gmGvDVtcUyLhe8fyeDG0h7IGh381Zu7dbXKaTTLbE9cBu9Gc93nGZ0ApcAAPlHWbVNVuKjJv1xNuvbEp0u9uaqDJAd84qu7xGpDUFFko5VxJ6AQCy1tUHtL3KJfAKRe-UWrjihMWEMJuye7GAYEZFg3kYRi0fjcCXyTbmviLba7OD6ozBmX0oKP_L6eYglcPohoBAsUIUnB9L5AD7PMvrehdQM1bK5xTbnfsKgS2UretaocQWVeYxXk6zwRjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تأکید مدیرعامل پارس‌خودرو بر تسریع تکمیل‌کاری و تحویل
خودروها به مشتریان
مدیرعامل پارس‌خودرو با حضور در خطوط تولید این شرکت در ایام تعطیلات تابستانی، از نزدیک به بررسی جزئیات روند فعالیت و تکمیل کاری خودروها پرداخت.
بهمن حسین‌زاده در جریان این بازدید، با تأکید بر ضرورت استمرار و شتاب‌بخشی به فرآیند تولید و تکمیل کاری خودروها، خواستار تسریع در آماده‌سازی و تحویل خودروهای تکمیل‌شده به مشتریان شد و بر ضرورت برنامه‌ریزی دقیق واحدهای مختلف برای کاهش زمان انتظار مشتریان تأکید کرد.
حسین‌زاده تسهیل روند تأمین پایدار قطعات مورد نیاز پارس خودرو توسط شرکت تامین کننده قطعات در گروه را یکی از الزامات اصلی افزایش سرعت تکمیل خودروها دانست و تصریح کرد که هماهنگی بیشتر میان مجموعه‌های مرتبط، می‌تواند ضمن جلوگیری از توقف یا کندی فرآیند تکمیل کاری، زمینه تحویل سریع‌تر خودروها و جلب رضایت مشتریان را فراهم کند.
مشروح خبر</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/455291" target="_blank">📅 13:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455290">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/455290" target="_blank">📅 13:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455283">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JV92T2eQuXXNloQIJmxVL_NsYaxu_KdZl8RFcVEhq-KMeNxCIAHrLeVMGPX1_o9gEdF_jRmpYwt_i5lc7AltPA5DZC7R8VxtEPK_wNIOxhUL6tiDBQOWA_3nJUlnlHJO9ir4H-_bjc0o7DgY8JC4Wvbm1qJ-4sB_tJtTKQJRmQYB-hX2gQeApAv3vMiuR30WhKTTF3rMPKktCKatvJdmVia6BAJ217bpMUZYqyFAfRL_dHvp1kNeRsSiKpU-NwwlwYFGcC7DERVvb6N3yw_uQEwAtulUcUSA1c1oSy0D83Hkhn6BxHcCVp3ucHKovklU7a67Ic1VLdjIl2zJ8WC_OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jgpeU6rOCdAjFlhLvjJ2th_2kh5a2pDbkoU7OCfHOdRJgLYNX5Ne1BFGNwiMWTAMATNT2hRc3wUSkX3FVl7Z5rwpdej3dSajsoqXCuDjKyVw0Pd4x7FJRzyOgfyOR-KVzqMz3wSSy7kAthQ5A5onaiQok3DhKWJEocKUojdFVsHxymUP9bNNtElcfb7PEx5QoRBH3Z40CJKlkeoWKhUWIy7X37O_OZmhtQkcbPVd5ok7k9xw8YVUh4O3sV1yp2OzNnaDXOvl13DncEQ8dehDBEKHpiV8UchZ2BYzCHqELXMpdE6jT8TTt_Xfs10mbGDT4YyoL1u4_mA9mn4ymBW4Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uF7qpPG66imAMSdWUmtnwzuyW0u-kLOVbwTPGz_fV6_mAnePgjJwSCCwEMoawuX5bRp5KLP4Y-SJNhouGiDe6xWNA2BtqRPvMhRbjgKEnRfSWqnLVeEcUDEpFchfEKiwZSSK4U-vwjqOu2ih-U00-dagseSUYIeQppqrtp0yLcWiK-VGkd5iZ32tG-CF0J_nPad0FwYWOAkZce3Ggav2BZB8-Po1Az2Lya0Q-g3fRKMR2WqkhxPnAjjxQ7aJqcplWQc8AW4LettNKKcMwzuzw_kNMTkkTZ46qGXTnfCrRDd0htQt39NVcOQWonG0MxWQyteYm77FWhGfqLs2CrPlQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xs0rdoL58fAu6HxmVmJWlfbe8gvRxPmNM9PI48ePJGwK_GN8scnHBE7KhcVyPOGl_aVdtjaSjcyaXu2gus99cBX3y4TZLDWDbiT-Hdu-FCspxqOEONZAItyyyCS7IsEIoyQbgWMwUxpUWPYPrEgpKMMnHhY93F5X5iEmR6LqRm5LsT3vBvGwEiFp-VIuXP2GKQCzYijPd8C6OqWySZx3hxw_gdncYB8ycbJdOUmKfnX02URnBYsxYOSDa4-O6Iy9btXJU0HfeJjU2tJIiKny9o1bpJUrPu9Ww5tFYDjNZZUalSHfNm33farKR_eNwsDtyehSPMxl6puocVWwJ9F8Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jI_tpBOISOsR7NLz7xCE_G48gAx0loMzwI6CPCw97xuAEL1TUxlXqULrn0_yqebD7-AzAT8FeTzjE1ltV0e7jmCSFXANrZw4O3rshkNY-_92I-aaL6RFAGWAf1jeaLHG13E6wNA0Dewcy_qJZPgyYk_RCVEQAit7W1QVduZtNP_s576afGKNfNi-XKbA8aZOXLWKugesJXZB8J_lrZcKrJfoSNO8VmVJ1a4D441eZcKfow9ecBDQ7ixi2711gYRFGT8rxfML19NTaFdp8jGntkRkDn-20Udz0nEyAtU5i7eu7Op2tlUSZJsSh6_XxoHZNeq6ZEEl4ci9g4gEoIEm0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PIznW7OG6gNPIUefBHKlpx6tz_f8JyyZnD8BQ4jp2W-MYndpeIJIsCJnurTF43gT4bJwB9eKX1aSz7et5CHSahn8ALsfTdwJaiDUaVSYUY_ukiGrS4dM49Zx2P0e4ONBXvgWOs1ik-ErrRwVshiCOxuE2K-ULb3t1IbfQWti6wlyDu8wZfir_TrH3rDqcSSzvOaHnPUuhY-jj_UbvBPKkuWEWxO3hmG3NlkhaiiJdymmt1fKpZ9Cj9xvINFSbNQdeyYHYiByK7jCTLYEjPCi2jdgMm--clUJYsXbOhuB-UQX37_b5vVa-9o85XUo184DnCX-cvwLNprQmHj15wb2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dw5Zk8X1bT0HvNy1bfUXP5LBl6ZvYxUthQG2l6LPCw9EqvkeSRo0NneUjuOcJDL8FqyDGEz7F8yJXRoOnlDq5YenDr3xCr0WipchoLodbakUbJBGJSurVmhqfZm33qxSynj67Ao0-fBnxlw1oesFO6D1ZEtUDvMGVhxIW8FnsY43N94rOQjHaTM_jKA0gBJmT-mbxf1EISd_cK-2xs514viGCOgDl8C_YFFR1FZJ907-77_6MQo9OzMBCiPLW9F-75Yz2wz4C0jRkdPdIiq-iElqZ9dRPxwuounMKibSagPzjch6AzIlMBdzq1TZRogpbnImPIto6pF6_lEas9pRtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: پاکستان از قالیباف و عراقچی برای سفر به اسلام‌آباد دعوت کرده و این سفر در زمان مناسب انجام خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/455283" target="_blank">📅 13:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455282">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d37c01a31.mp4?token=mw3iyQsR8oDaeezKSGOeKInXRJT8fb-22iYOh1dXXXKzl6Yf3B4G7BsFcwdN-tWFdwvuLRN3przSgLYbqnEph1wMwba7m1BRkGF4rc3lB9N5lV0YWpHQdun1BQC4KRV3Zg-iWuPMY4JthIcJmr5zpZNJuUGEOX0WNlZT3gOb-LWsGjvYUuxi7MEjKcb0s3OfM77wZXwOmxokq6KGJPz0jPwogllXImb8DaWRRoOojzlB1cO0_-iG326DPlbGPahVn9Z33RWBonZQEplgKewB5Qz__L222k2nuwzgaooTxM5F3Jt19bomkV1T_U3b1Hdp-gP9Gp_XkqMXOnO1ABm1eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d37c01a31.mp4?token=mw3iyQsR8oDaeezKSGOeKInXRJT8fb-22iYOh1dXXXKzl6Yf3B4G7BsFcwdN-tWFdwvuLRN3przSgLYbqnEph1wMwba7m1BRkGF4rc3lB9N5lV0YWpHQdun1BQC4KRV3Zg-iWuPMY4JthIcJmr5zpZNJuUGEOX0WNlZT3gOb-LWsGjvYUuxi7MEjKcb0s3OfM77wZXwOmxokq6KGJPz0jPwogllXImb8DaWRRoOojzlB1cO0_-iG326DPlbGPahVn9Z33RWBonZQEplgKewB5Qz__L222k2nuwzgaooTxM5F3Jt19bomkV1T_U3b1Hdp-gP9Gp_XkqMXOnO1ABm1eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سازمان اطلاعات نظامی اوکراین: ۲ لانچر اس-۴۰۰ روسیه را منهدم کردیم
🔹
سازمان اطلاعات نظامی اوکراین اعلام کرد که در عملیات پهپادی در منطقهٔ کریمه، ۲ لانچر اس-۴۰۰ روسیه و یک آنتن کنترل پهپادهای روسیه منهدم شدند.
🔹
به روایت مقام‌های اوکراینی، در این حملات از شهپادهای «ماگورا» (Magura) برای حمل پهپادهای عامل حمله به لانچرهای روسی استفاده شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/455282" target="_blank">📅 13:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455281">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOWNvIMgWBsuzyxPxGn8NcTX5MfVqGTVUSPXHaeusPZ46yV6rpG9eYEEu08JxBHAIZYqAkJVFiY1LrjAfNzjHHGxx9-DtQ0n7VA5n4-WDLQm5c6XXbp2XYUC4xRor6Vp_3Ph0lVhZGx2CwTMAREWNq2s_lQP5SrgMGCPnAZvI60rZyiTHB3qdFaEYuOMs5xzjsjVKbx940P8XNQ5BeKJDSSTl4gIp3vhP8MvF9l05a8qitQ6EJ7avPwLJ37JKSd630oBI6DmJ4DF8AesGE4D6VRBol0GF4f3p0ts-56ykD1dmDuqse3CTJVizcSDEU4o01rTjuk56Y4tG2LNpZQesw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی به لیگ ازبکستان رفت
✔️
مرتضی پورعلی‌گنجی مدافع ۳۴ ساله پرسپولیس به پاختاکور ازبکستان پیوست.
@Sportfars</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/455281" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455280">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎥
بدهی مجموعۀ آزادی برای کشتی دردسرساز شد
🔹
بدهی مجموعۀ آزادی به وزارت نیرو برای مصرف برق باعث شد امروز برق قطع شود و حتی شنیده شده برق مجموعۀ انقلاب نیز قطع شده است.
🔹
این اتفاق درحالی رخ داده که تیم‌های ملی کشتی جوانان و بزرگسالان خود را برای مسابقات جهانی…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/455280" target="_blank">📅 12:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455279">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AskwXeY4yJ_r3L44NaN2VOJ_sRpJJbC8TgQ2QdVtX2Zd96ftC4868BaPI_NcipI_TkdIG9IYXtNQ8pXnHE1GSW5SWFal6ShsxforrSVDRAldK4RVfISUugcH6sKhNvm96umeRA79VEQ8A4aBGL26FZG_MsBZDpBSGO4dPunoHgyN6bDox93vNeB7252u3-fAlmbAkuWtM-95Elb3IbGwYIjvxHbXBxAFx-WxEwkt5wXqhUmxdUvTgCL_Mp5fVYBfg2RxFxZX_Haq5c0mNsN_Ik7z-9aJPnpFmWzzj2lGuyzpj34wnspiU6c8tdTLv7D_MYfmwcUNiIZOlMT0kv0z1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس با عبور از ۵ میلیون و ۶۰۰ هزار باز هم رکورد تاریخی زد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۹۴ هزار واحدی به ۵ میلیون و ۶۵۴ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/455279" target="_blank">📅 12:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455278">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b222dc371a.mp4?token=KXkVJkeTY4ZOekIJBJIMCdCMeFD9D9zASOo67fl5s9vkyVnjbVw1ysrjvrEKd8cdbs8PrUzrK5nGG6GkgUfK5Tq0dnOxx0W4VriMKrMISWSuZfHe1p5KKMQmlsO9vUqJjOG8FAw9n0qZ87HyWwT2TTuq2G8MHJhCkcoGeN-dn-AXnlrEuGVw2OhOKYPc7TPVJ3pXwlRfoi2cCTgKr6fXh1Er63fE5ZUU1pGYMx8E1fIet7GS5E-6idnW9ed_Rh2BURaGh5-aq6pnOrEq3P60BVhG2rGvWbNRTwEabhRqwgfh_U34zcfHUDMhOhaoJk5HYaVRwDbciKNhdStunTDLGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b222dc371a.mp4?token=KXkVJkeTY4ZOekIJBJIMCdCMeFD9D9zASOo67fl5s9vkyVnjbVw1ysrjvrEKd8cdbs8PrUzrK5nGG6GkgUfK5Tq0dnOxx0W4VriMKrMISWSuZfHe1p5KKMQmlsO9vUqJjOG8FAw9n0qZ87HyWwT2TTuq2G8MHJhCkcoGeN-dn-AXnlrEuGVw2OhOKYPc7TPVJ3pXwlRfoi2cCTgKr6fXh1Er63fE5ZUU1pGYMx8E1fIet7GS5E-6idnW9ed_Rh2BURaGh5-aq6pnOrEq3P60BVhG2rGvWbNRTwEabhRqwgfh_U34zcfHUDMhOhaoJk5HYaVRwDbciKNhdStunTDLGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: پاکستان از قالیباف و عراقچی برای سفر به اسلام‌آباد دعوت کرده و این سفر در زمان مناسب انجام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/455278" target="_blank">📅 12:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455277">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cc9a50c3c.mp4?token=GUYWbMEmH4pxJg0U5mIFJpWwJjfjZ6V0mnVbG2gH5RWINL_icfMjqAFVUu9LRHonic1mdiH-G8QygzhYk-tJwV7AIZqAQksixhYpdVloobszTqUiVQUa-BmU2OsFm9DIypZYXQO9tumLOG99KEYwOCXiC24of7xZpmgzCpAVyLSEdS8PyunjAYPwgR38uCiVMETw9lw6WaZ8FbfS7oVjb5HhJsrgEXzwqcx4fcnP_YgNrs5ES90H-Ur1zrfkIKzDHTB7nfysjVw3aFk5lXOs1U_ZYpnpb8juoG7E-OBzioxUAoNJ08foOtVfKL6KWy_vg3LrIZG0e2E9SSOjEc8CBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cc9a50c3c.mp4?token=GUYWbMEmH4pxJg0U5mIFJpWwJjfjZ6V0mnVbG2gH5RWINL_icfMjqAFVUu9LRHonic1mdiH-G8QygzhYk-tJwV7AIZqAQksixhYpdVloobszTqUiVQUa-BmU2OsFm9DIypZYXQO9tumLOG99KEYwOCXiC24of7xZpmgzCpAVyLSEdS8PyunjAYPwgR38uCiVMETw9lw6WaZ8FbfS7oVjb5HhJsrgEXzwqcx4fcnP_YgNrs5ES90H-Ur1zrfkIKzDHTB7nfysjVw3aFk5lXOs1U_ZYpnpb8juoG7E-OBzioxUAoNJ08foOtVfKL6KWy_vg3LrIZG0e2E9SSOjEc8CBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: قاعدتاً خدمات دریایی مابه‌ازایی دارد و باید آن را دریافت کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/455277" target="_blank">📅 12:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455276">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWqBebWsFy8WFBi3ck_BRqhlsYzAWyVyHbJe6Ry0R7njw2uAn3WTTs--7-u-ooBP1VlnrJthflwWADIYGOAxwOKi3vgBSJEFnoTZ8b73YjnKtt-GrEECjrPwn931BOLlEnHEYACvM5aNzOsl5ohRzIM0fh1O-MbdNUN1-pV9-tA8pBGtnpSDeZeZRK8twa709slLcLWxehduD5i0pKd3fRtniC5mrZ-16RnzByH6uzwV8NBVvPFRtsIEzM8T3n3m-xos1grfL7lQIjMRVexLH2y2ka-psQLsD8JJuQ5OR3TBPDosS2gGJ8F9PSuOyLzDU_RcFVFapTXVaB4UEmLLMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تعزیرات: سهمیهٔ گران‌فروشان نان قطع می‌شود
🔹
رئیس سازمان تعزیرات حکومتی: در صورت تکرار ۷ نوع تخلف، از جمله گران‌فروشی و برخی تخلفات مرتبط با عرضهٔ نان، با قطع یا کاهش سهمیهٔ آرد و همچنین تعطیلی واحد متخلف برخورد شود.
🔹
بیش‌از ۱۵ هزار پرونده در حوزهٔ تخلفات نان در سراسر کشور وارد شده که حدود ۱۳ هزار پرونده از این تعداد مختومه شده و حدود ۲۹۰۰ پرونده نیز همچنان درحال رسیدگی است.
عکس: علیرضا مولوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/455276" target="_blank">📅 12:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455275">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18e0493aa7.mp4?token=he7Jg6bxWLczFeOomrts0mmSWX9r_fjGeYo7jVTRTS-elxZnvLZN0fhv_5zXH0j5YsPAu6hGJZWgzgUNkt4mXPCmOgjesZygmobIgQ714O0HDKUpFO-9I1YNZQZTwV7C6D_xIcus_qDOdVrWy_XXttD38UQ25IcPDOzQ2vBpwG-HKQslDXasj0Rwyl4tVbi-rlvQIfxGqO29t3RJ6qvXn4NNYpOG1BAFTKapzSjH2OHzWT3lyODLzrxeilGplK7LlTc5A0NKVc1AweiFrKVf3BwRfL0GiJ5jfOJaDBgxww0ODBZGXnpcUXO7nb4gtvKsuStH13Q0vARCrUiIKzjmKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18e0493aa7.mp4?token=he7Jg6bxWLczFeOomrts0mmSWX9r_fjGeYo7jVTRTS-elxZnvLZN0fhv_5zXH0j5YsPAu6hGJZWgzgUNkt4mXPCmOgjesZygmobIgQ714O0HDKUpFO-9I1YNZQZTwV7C6D_xIcus_qDOdVrWy_XXttD38UQ25IcPDOzQ2vBpwG-HKQslDXasj0Rwyl4tVbi-rlvQIfxGqO29t3RJ6qvXn4NNYpOG1BAFTKapzSjH2OHzWT3lyODLzrxeilGplK7LlTc5A0NKVc1AweiFrKVf3BwRfL0GiJ5jfOJaDBgxww0ODBZGXnpcUXO7nb4gtvKsuStH13Q0vARCrUiIKzjmKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
محسن رضایی دبیر شورای‌عالی امنیت ملی شد
🔹
معاون ارتباطات دفتر رئیس جمهور: با حکم رئیس‌جمهور، محسن رضایی به‌عنوان دبیر شورای عالی امنیت ملی منصوب شد. @Farsna</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/455275" target="_blank">📅 12:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455274">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e338aa971e.mp4?token=YHN6T2p5As27-HVOkrD1wP7s6phjM42jG1hOa3C9lFusZMOZZXwHJ7s3CCDzWk_TYVOhM7yBHk6PyREusweBu684xvgwVN04gX33m5T_Lm-2Cb6hhfBAkr6lM1hiDRyD6BMTHDcQ1TdW0VgxNdI725cgPeOdB1lcQlKHzGtBj8Wrb5FM4xjTulnHoKAe4Sn-90tRlXwiVhTLQvC3nKnk70_qBPqrfLZSPMB-ptqgGEwhU-PPxax6UNRcF1Ogq8v8hfwz00OXHO8FkciXiB-hrMDJph-7cWvfr06xVZbt9Zq3-C9lzV9KA5Ou4qz1wiYpJ-L-MqJWU-q4STiQOoG0Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e338aa971e.mp4?token=YHN6T2p5As27-HVOkrD1wP7s6phjM42jG1hOa3C9lFusZMOZZXwHJ7s3CCDzWk_TYVOhM7yBHk6PyREusweBu684xvgwVN04gX33m5T_Lm-2Cb6hhfBAkr6lM1hiDRyD6BMTHDcQ1TdW0VgxNdI725cgPeOdB1lcQlKHzGtBj8Wrb5FM4xjTulnHoKAe4Sn-90tRlXwiVhTLQvC3nKnk70_qBPqrfLZSPMB-ptqgGEwhU-PPxax6UNRcF1Ogq8v8hfwz00OXHO8FkciXiB-hrMDJph-7cWvfr06xVZbt9Zq3-C9lzV9KA5Ou4qz1wiYpJ-L-MqJWU-q4STiQOoG0Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدهی مجموعۀ آزادی برای کشتی دردسرساز شد
🔹
بدهی مجموعۀ آزادی به وزارت نیرو برای مصرف برق باعث شد امروز برق قطع شود و حتی شنیده شده برق مجموعۀ انقلاب نیز قطع شده است.
🔹
این اتفاق درحالی رخ داده که تیم‌های ملی کشتی جوانان و بزرگسالان خود را برای مسابقات جهانی و بازی‌های آسیایی آماده می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/455274" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455273">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_SXfxl82RwL8TJSBHlTpOOVGnhuWAO1A5zL8ZEdfJF2RNTYWbRAPHLdtFIZ5OEv8E_HJf9dQWg8mzWwshc4i4Ju0Q8s4ByTOAu-I0d4Ic08fDmBxhKfcgvA10Dzrv0oIPDJ5BI6Sd1tNea6Xi-yizf_LEQWBNtWqu96lLICAioy8a0W8TGGQzZIBekJgJ2276f42df9mv8cn8qdPhtioPKwep5NHgf50JFyqDH-sRuLpvHvD8kYZm-EMkLsxzWyYA9pEwmgeUBl-UG-3iRenibA_5TZ0DpnW6cL3AIDjewg97iGI8nMwKxzzWy_KxEKaqxojYC-XPo26l8y0FNiSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وعدهٔ تازه سایپا به مشتریان در انتظار
🔹
مشتریان سایپا می‌گویند این خودروساز ساینا و سایر خودروهای ثبت نامی را تحویل نمی‌دهد.
🔹
برخی مخاطبان خبرگزاری فارس در پویشی اعلام کرده‌اند سایپا با وجود دریافت وجه و وعدهٔ تحویل ۹۰ روزه، پس از ۱۰ ماه هنوز خودروها را تحویل نداده است.
🔹
حالا سایپا می‌گوید روند کاهش تعهدات تا تحویل تمام خودروهای باقی‌مانده ادامه دارد.
🔸
اوایل اسفند سال گذشته، تعهدات معوق این شرکت ۵۸ هزار دستگاه اعلام شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/455273" target="_blank">📅 12:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455272">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45fb6fa172.mp4?token=hhD4fM1cusaIbkXonwvBBIJ8p-Op_POiEaSc_EmTvGn3alPz9ckXjUnzqOEllF3rNk3yVJF55sGyzeXQKsTI8e3sCvmKwvP6nckKEwEoAoQTTjifjfvQIKrxX1wM_wSzqc48sYIoKzvkWnXym2jV6UB9hJQW8fFYUjm6LsnQWRip4WajvTJSvL1mn6c5SVHx7gpG-yTaD28UWLh7iYnAliIppc3jcaMKpqo_qHwZZ6M700KfYdsZuO3QeODKRFvpkUOD-FegQnHXBZNLnD2FHGMHzD0B_kA8YxV3SOzFHLnY12x7uEyvGxIA0-YUbX4-tDxkOT5H7huWmH8it_QfIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45fb6fa172.mp4?token=hhD4fM1cusaIbkXonwvBBIJ8p-Op_POiEaSc_EmTvGn3alPz9ckXjUnzqOEllF3rNk3yVJF55sGyzeXQKsTI8e3sCvmKwvP6nckKEwEoAoQTTjifjfvQIKrxX1wM_wSzqc48sYIoKzvkWnXym2jV6UB9hJQW8fFYUjm6LsnQWRip4WajvTJSvL1mn6c5SVHx7gpG-yTaD28UWLh7iYnAliIppc3jcaMKpqo_qHwZZ6M700KfYdsZuO3QeODKRFvpkUOD-FegQnHXBZNLnD2FHGMHzD0B_kA8YxV3SOzFHLnY12x7uEyvGxIA0-YUbX4-tDxkOT5H7huWmH8it_QfIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: تنگهٔ هرمز به‌خاطر اختلاف‌نظر ایران و عمان بسته نشده که با توافق ایران و عمان باز شود
🔹
بازشدن تنگهٔ هرمز منوط به تحقق شرایطی است که در پی تجاوز نظامی آمریکا و رژیم صهیونیستی به ایران تحمیل شده؛ ما هنوز در جنگ هستیم و تا وقتی که محاصرهٔ…</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/455272" target="_blank">📅 11:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455271">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJXU1ygsOFxUQ76WqZYgyVKLLisFjN9b22fyAu6jScv2ZYVgbNS66FYJBZRkLoXqNfXqQabxduFq2zm8gxCWcKr16l34IaV8EIMbavsIfwHoUrawacMaGL_sn3afd6FhM45ny_XZ4_kX1Tit9w9PxvB1qxFoHFAyOseq4D8a2nGnIt5nuXTHyd7K54xnYrj6dCuTmuTF5JuX98_OzXjRuLp5F8QCNtqD8TokULyhl6k5cA87fyqpJRKyVntPCEfX1Acbz4iuKMwhm6r-iLHBHgQPtHUTpRmG4dQs9WhdFIElnbC2B2g_ovGf3RoillC2f_BOZ83_rzvZfCduoVtEtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خضریان: کلیات طرح اقدام راهبردی امنیت تنگهٔ هرمز در کمیسیون امنیت ملی تصویب شد
🔹
عضو کمیسیون امنیت ملی: با توجه به موقعیت راهبردی خلیج فارس و تنگهٔ هرمز و لزوم اعمال حاکمیت جمهوری اسلامی ایران به‌منظور پیشگیری از تکرار اقدامات خصمانه علیه ایران، کلیات طرح…</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/455271" target="_blank">📅 11:58 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
