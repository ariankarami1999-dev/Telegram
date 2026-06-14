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
<img src="https://cdn4.telesco.pe/file/NUIVp5sXc4mLUFnGkYtWYqTUH0o9d3nRD2hFLP1oWZ4FEQKW7B0vxN-UAoGh85xLLm9Brr4M2QsURcyj1pr8fkrPo98mM7rKVK-od_KhHaoWZLIGjLP_yn6L3V_gbGTK45G6vE4-mQAuwb3OGtpFbvIuHjy7kOE4zUdgjAcgqNBXK2O_1iwERdrolucPb52KqZ916QTxs5ZcKsu75rCUxS0cS081Zf-s_zStKGg6k38xKRHDc92E17Snm1FHSzSLLM7h3gPyNOZH7L4rQ-5XJVkwKK7G_Be9adoEEuBYriLd5uxbszbdZUvuvY8miYXQJqwiE-o7AaZVwXIp0ZwUPw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.54M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 00:14:42</div>
<hr>

<div class="tg-post" id="msg-659494">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_4AjcYGz4GTQe45U30G-L6V_V22yNLsaBlrXsYNq3TQVmF3TQ4QRiQ9TRqjtmYRD1UlsZIIRxjCUvHz84Iglf6rRCSbHI6Haz2fazz35IGunjmUToqTnsCtizCk0CsQIa-pX0FRsNR4MnzBTkwSbWG5nayDvcq48m7zzx5ksSTv1Sy7lhgMjPfxbB6e-vmS9y-wpgx_KfDI5TPqUbK-gYfxGJV7SCHjMOwEx2gln2EFc6SevWKQoZpfq5HwAzT-eL51OWWvDNZNZwgYG8ECqn653TN1-frsuEY1pWb8YXK9youRY1veM-ysuqD9vRD8-iJdc7E2au0oTQ2IS0DyOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: دولت خود را موظف می‌داند از نیروهایی که برای دفاع از کشور و امنیت مردم در میدان حضور دارند، حمایت کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/akhbarefori/659494" target="_blank">📅 00:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659493">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
یک منبع آگاه، خبر برکناری سعید جلیلی از شورای عالی امنیت ملی را تکذیب کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/659493" target="_blank">📅 00:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659492">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-WfXiTiyORztfKwxxqrpl0zwFPDEC3Xf2ZaP2PxUg3UZpKD71QIuXwlKJULj4-egaGPvFte0-trOOTVKXPgGlrO7WILH8iNbEl_ooComCruUDnHMBWoNdFS9WSg-vT5GU65U4bSLwOfEVKIfnf4PZg2s75T2cCkMrL2fSsYh3PNkNtCb6Fgrap92tyEpaFf96M66N6dso3GNg5Gu-BG6AIX89Yq1rIaFzQPBarxcvh6a7OZ_Kzh5qpSF2a5NVBkkT5EwFYB89FOn_yWTp_MkG9X3lCNFjECGN4HNI_UWIEgkphF6peuoOo2rokUx_wfF7EMpHACFggD2qVxI6Xf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کجا رو می‌خوای بزنی تهمتن من؟
😍
توییتر خبرفوری را دنبال کنید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659492" target="_blank">📅 00:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659491">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IduOYC143p8pvWJSPg2Y2aagcOA3LCCkk026kwiuYhEaDtR_XLNB0HiBb3fQODyJ0KRpFDNANycscVi0G587eeKrTrcOajY2x-CMzxGPVTV1fv5gUfD3MfsedJHjsmAcdug8TeCDhwrE_UKoGoL6k_UsiGC7F7z0RDpR8gJCQyAbHdLHoTukZYTGe38kHGk8OO1r6DOdJEDj4_5wevV2GOaSaYPiYODgzOCZrKGHxzcoUB1hFLfgJaNca_zF5HGkHofoYNwwbRd2V30Qt_JcR4VQmS3NPESD3JM1af9iaDImyzSqRw4bs29d36aA6PiYv5rWMbuG8kNB9tTsL5J0hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/akhbarefori/659491" target="_blank">📅 00:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659490">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
المیادین: جنگنده‌های رژیم صهیونیستی منطقه صور در جنوب لبنان را هدف قرار دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/659490" target="_blank">📅 00:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659489">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
کانال ۱۴ عبری: یک کارمند کنست اسرائیل به جاسوسی برای ایران متهم شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659489" target="_blank">📅 00:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659488">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcXelqDQaTJewDgXNHFA5E5D_Mxdg3Xau10GfM4_nkqyeXrC7l9P24ovYu1cyjiik_s9zDCUMpGT7WvjhDMdbDMBCzlgmNS6G8UXhWa_FKEloqvG4KWLZmuTPqvTZ_eIJLVCSc-FxexqWlcZot_n6TyL1_05sq7JiLrUtpiSl6jkPI3WxWUuYqYNLw0VmldbtRVxvqKStaxqShcx9Yh0gsr5KDdTkwXUDxYd0Vfq-n58ZAJdj6rMPZpn62bZY-1vjiUUoKMoT86nNvNb1t-00s2s88rYCt732RANed021V9c80Q22zvzL9rnWEVv6J0HpuZn0xqxLoaHShwDR5s3wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چهره عجیب هوادار ژاپن در بازی برابر هلند به سوژه رسانه‌های اجتماعی تبدیل شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/659488" target="_blank">📅 23:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659487">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bffdcb7ae.mp4?token=fOvUrHlSajD_bpZ_KD-a-tYx5uZywdN97NOPTVBQa4y7sj_yldfeoCG2PscRMSTa2af8DDQGLHmPbxdFY_r43ub4Cv28uj2S1J_G4jZtf_yLg_x1ZzseRpPuZgFccuU_jebtPyF4nseR70WZoX51qF3_XnIUidt1AmoNQbEOfUf4zftNNrs4Awx49ja85rG7gVNEySqdlt_6F8CWJllJLMluTk42yYYqlgf42kho7ew5n3Lj62kXC2wJQzY8ZNvCaAFyrUzuytt_p244CQchS1MTWKqwyJFJ2wFxY32khBesXHNh3EAb5wpXBUSORaqnhMQfeFsnV55aA-hunjnL3jleNUolB2lZW9u96H0kO1JlK-XCBdeBSf0Pv2DuJpSPDrTFqtzn7j-_fQD_FOI9P8suLSczR26oHuCZ_NrZAeqiMpdI2fxAH0p2JOEd4dVWGDsEorBUnetuhUV5EIzh1M9EVNC4y-uQZZYW8Dy7181hL3dO0WAgML6qcWcSB8EdLjMFHzSy3kotnX9eH2jBd5b8vMup7HyGZ6em09puYuou5irqsMUllLpaZ1wMHL_KIgz-6ZcXBuIKlPmGLxRdtpLmuYxzbcgaxrS59bp7NfeRGMgh9YnyDpDkN1SEDqUNxruvOgSi2lY-pClUe0zfJgu40uWGo9SOPnIq4J8tKKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bffdcb7ae.mp4?token=fOvUrHlSajD_bpZ_KD-a-tYx5uZywdN97NOPTVBQa4y7sj_yldfeoCG2PscRMSTa2af8DDQGLHmPbxdFY_r43ub4Cv28uj2S1J_G4jZtf_yLg_x1ZzseRpPuZgFccuU_jebtPyF4nseR70WZoX51qF3_XnIUidt1AmoNQbEOfUf4zftNNrs4Awx49ja85rG7gVNEySqdlt_6F8CWJllJLMluTk42yYYqlgf42kho7ew5n3Lj62kXC2wJQzY8ZNvCaAFyrUzuytt_p244CQchS1MTWKqwyJFJ2wFxY32khBesXHNh3EAb5wpXBUSORaqnhMQfeFsnV55aA-hunjnL3jleNUolB2lZW9u96H0kO1JlK-XCBdeBSf0Pv2DuJpSPDrTFqtzn7j-_fQD_FOI9P8suLSczR26oHuCZ_NrZAeqiMpdI2fxAH0p2JOEd4dVWGDsEorBUnetuhUV5EIzh1M9EVNC4y-uQZZYW8Dy7181hL3dO0WAgML6qcWcSB8EdLjMFHzSy3kotnX9eH2jBd5b8vMup7HyGZ6em09puYuou5irqsMUllLpaZ1wMHL_KIgz-6ZcXBuIKlPmGLxRdtpLmuYxzbcgaxrS59bp7NfeRGMgh9YnyDpDkN1SEDqUNxruvOgSi2lY-pClUe0zfJgu40uWGo9SOPnIq4J8tKKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سپر انسانی توسط گروه های سرود به دور زیرساخت ها و اماکن ملی کشور تشکیل شد
🔹
ویدیوی فوق ، سندی ماندگار از تشکیل سپر انسانی در ۱۲۰ نقطه زیرساختی کشور است که با حضور مقتدرانه مردم و گروه‌های سرود رقم خورد.
🔹
در پاسخ به تهدیدات اخیر مراجع نظامی و رسانه ای غرب علیه مراکز زیرساختی ، علمی و تمدنی ایران، رویداد کشوری «ایرانِ یکصدا» در سالگرد آغاز جنگ ۱۲ روزه برگزار شد .
این مانور مردمی هماهنگ در ۳۱ استان کشور، فراتر از محاسبات کلاسیک اتاق‌های جنگ دشمن رقم خورد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659487" target="_blank">📅 23:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659486">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0WEl0RYdPdWD--UH6mCU0jf5YJh_vGopvO2-u5fUNVxDrqMS-nO9qxnddFDSFAgqn7ipAX-bIL68BrIQqp9H0nGZvpPm7NPbKyyc6z3iG_FG6OunYf8mufUC_8Buw3kJajHJsTHtjcf4sCNSSqcltlTk2pn8smmRsKX58o2fSsUZV0qIxvTtAlkLE43L5JBrdj0_d3OUnydpT2nOsdRSKny8u_PFU42udCrdS_C_3CUioDCyqAIsg6jyyH1IJgledZ0b3wAkrD6F2J7Za0rNRQuNbNs4_XpKjGRDvVPHIgWkyicsEfmx27ucsaPhQTZLzYhi2jlSz2eS1xv0Jrmog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام دکتر علیرضا زاکانی، شهردار تهران به مناسبت اولین سالگرد شهادت سپهبد علی شادمانی
🔹
شهید سپهبد شادمانی با اینکه از فرماندهان ارزنده دفاع مقدس بود و بعد از آن نیز در عالی‌ترین سطوح در مسیر جهاد ثابت قدم باقی ماند اما مسیر گمنامی را برای خود و خانواده‌اش برگزید.
🔹
شهید شادمانی در همان مدت کوتاه فرماندهی خود بر نیروهای مسلح توانست هدایت قوای نظامی ایران را بدست گرفته و رهنمودهای او نه تنها تا پایان جنگ ۱۲روزه، بلکه در جنگ رمضان نیز به کمک نیروهای مسلح آمد.
🔹
رحمت خدا بر روح بلند او و آرزوی صبر برای خانواده‌ی ایشان.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/659486" target="_blank">📅 23:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659485">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
با ورود نوزدهمین و آخرین گروه پروازی حجاج به فرودگاه بین‌المللی شهید دستغیب شیراز، عملیات بازگشت زائران حج تمتع ۱۴۰۵ از مسیر شیراز پس از انجام ۱۹ پرواز به پایان رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/659485" target="_blank">📅 23:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659484">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
سی‌ان‌ان: یک منبع اسرائیلی گفت نتانیاهو به دنبال دیدار فوری با ترامپ است
🔹
نتانیاهو تلاش می‌کند پس از بازگشت ترامپ از نشست جی‌۷ در اروپا، آخر هفته آینده یا اندکی پس از آن، دیداری ترتیب دهد.
🔹
ترامپ روز یکشنبه پس از آنکه ارتش اسرائیل، بیروت را هدف قرار داد، به شدت اسرائیل را سرزنش کرد و گفت حمله به پایتخت لبنان «نباید اتفاق می‌افتاد»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/659484" target="_blank">📅 23:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659483">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ادعای یارون آبراهام، روزنامه‌نگار اسرائیلی: در ساعات اخیر شتاب قابل توجهی در مذاکرات برای امضای تفاهم‌نامه میان ایالات متحده و ایران، با میانجی‌گری قطر و پاکستان شکل گرفته
🔹
هدف آمریکا ارائه امتیازاتی به ایران، شاید به شکل پول یا تسهیلات اقتصادی، در ازای امضای این تفاهم‌نامه است/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/659483" target="_blank">📅 23:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659482">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rc152XX-a36GF4YtisfY9_xXHpk1ihj5xjWnwdvckEVqt8YUc2JNdKZeSs--Vsa8_CeMAfdBNWHdvlXVIdciCi8TAEBl4XfsHDqaf7jw1lfP-djZ1Ft-FhL9eK-AlLmsz8VjQiIH-K-7bCRd3AhkkK-FEcaUSfIRwpjNVAGF9LSxZ8RIeCAX8VtcRBwXyCz6PIpmPhNa92-65NMZAtUtmUCN2ZmJlVU9n4GsUXHgMXVnE4xhB8EglQCSEkCQwPInQommekY9--m-753ZUXhA4NC7DPNOo3ZGBST1lfkiJhLweLiE5IQvaken0LXxD_lmLQ4edq6Z9IuAiNGcdeRhog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت جام جهانی فوتبال ۲۰۲۶
🔹
همراهان عزیز خبرفوری، برای شرکت در این فراخوان کافی‌ست یک ویس ۱۵ ثانیه‌ای از پیام‌های حمایتی و انگیزشی خود برای تیم ملی فوتبال ایران ضبط کنید و برای ما ارسال کنید.
🔸
صدای شما می‌تواند انرژی‌بخش ملی‌پوشان در مسیر جام جهانی باشد.
🔸
پیام صوتی خود را به آیدی ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/659482" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659481">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
توحش بی‌پایان رژیم صهیونیستی/ ادامه حملات هوایی و تو‌پخانه‌ای دشمن صهیونیستی به مناطق جنوبی لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/659481" target="_blank">📅 23:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659480">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ورود نظامیان صهیونیست به مناطقی از خاک سوریه
🔹
منابع خبری گزارش دادند که نظامیان رژیم صهیونیستی در ادامه نقض تمامیت ارضی سوریه وارد مناطقی از جنوب این کشور شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659480" target="_blank">📅 23:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659479">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ولایتی: ساعت صفر فرارسیده و پرتابگرها آماده می‌شوند
مشاور رهبر معظم انقلاب اسلامی:
🔹
خطای محاسباتی در بیروت، صبر را به پایان رساند و فرمان صادر شد.ساعت صفر فرا رسیده و پرتابگرها آماده میشوند.
🔹
حزب الله پاره تن محور مقاومت است. اگر آتش شیطنت در لبنان خاموش نشود، دو بازوی قدرتمند جغرافیا یعنی هرمز و باب المندب شاهرگ‌های اقتصادی‌تان را تا خفگی استراتژیک فشار خواهند داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/659479" target="_blank">📅 23:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659478">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6qj27t_bu-oYVvJw-qBlWhEplowmjZkjF4zWcwVj-PzD7G4BRms7p-teUthYD3Bh5RttS7_LqPCXxrBBUuQVG73aqNixmAgSABgPjoj3Y_nwIQ-Wvb-Tiy7z6vxvtns59vQ9c3Ux1MtAe-fwvsuqcqnOA8Ab89TE1GFZBISFCgVem4mP1MUCZ5b05F7hEKrSbYmPwqYKAp7XAJzXPf0QCXCYkN2lOFY9vPAi-NBtUMv4I4SPUji7sG0dswSRD8Tz5HHI8HlcRrJNAVcVS1pLa1Fa4kHASiYVvlNb9xVaYtSrmb0LmA8eC6zkrTbXh-0vY3nGh-UwDRXV5US-ABebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تسویه حساب
🔹
فرمانده قرارگاه خاتم الانبیا در پیامی خطاب به مردم اعلام کرد که  فرزندان ملت در نیروهای مسلح «دست به ماشه» آماده شلیک به قلب دشمن هستند. سردار عبداللهی گفت که اتفاقات یک سال اخیر، از جنگ ۱۲ روزه تا «جنگ رمضان»، علیرغم خسارت‌های سنگین و داغِ جانسوزِ شهادت امام شهید، فرماندهان و مردم بی‌گناه، یک فرصت بزرگ برای «تسویه حساب تاريخی» با جنایتکاران فراهم کرد؛ نیرو‌های مسلح به  مردم و با عنایت الهی بر سر آن‌ها آوردند آنچه لایقشان بود.
🔹
هفتصدوهفتادوچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659478" target="_blank">📅 23:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659477">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
رضایی، سخنگوی کمیسیون امنیت ملی: مقامات نظامی می‌گویند که احتمال یک درگیری دیگر وجود دارد و برای یک جنگ بعدی آماده‌اند، اما معنایش این نیست که لزوما امشب یا فردا جنگ می‌شود، اما منطقا و عقلا باید برای یک جنگ دیگری آماده باشیم
🔹
حتما برای دور جدید درگیری با دشمن آماده‌ایم و تمرکز کشور بیش از آنکه بر حوزه مذاکره باشد در حوزه ارتقا توان دفاعی کشور است. هیچ تضمینی وجود ندارد که در آینده جنگی بر ما تحمیل نشود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/659477" target="_blank">📅 23:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659476">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
اختلال گسترده در سامانه‌های جی‌پی‌اس سراسر فلسطین اشغالی
🔹
رسانه‌های رژیم صهیونیستی از بروز اختلالات سراسری در سامانه‌های موقعیت‌یاب جهانی (GPS) در تمام مناطق تحت کنترل این رژیم خبر دادند.
🔹
این اختلال باعث از کار افتادن یا خطای جدی در سامانه‌های ناوبری و مکان‌یابی شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/659476" target="_blank">📅 23:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659475">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzC7lr2Vl--BoXaxfUqZSmt7-qHTW1yyCCR0ZXpMtnBACzAcStfsB2IPqcdp4dUrYer8Jzjbazt6nT0eXBoMOzKSCfVkCPhqM16cyj0orXLGyk3v5Xb1_Bml1Z0gkXwPXgKAihQkXCZyMMaZCHj9sG3jAJSgl5qQzytJx4MjV21tdoZZ87QDOwHFZQbi8U3f1owKgFEfMrDOmZYPECyCri7z4iCj3tsJavJ4Win-n4f5X68Q1UHibq8K2ESrgZZAbCqD5RKsSLLPqgBHQg2zbhLVQvMoyAz70LdsqmVItDoOieolbIA4BGh8VBAl2uJIuG4Ga6GowFCsqo2Kj4CpGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر در واکنش به تجاوز مجدد به ضاحیه: نه لبخند دیپلماتیک آمریکایی قابل اعتماد است و نه توحش صهیونیستی قابل تحمل!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/659475" target="_blank">📅 23:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659474">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
جی‌پی مورگان: طلا تا پایان سال، ۶۰۰۰ دلار می‌شود
جی‌پی مورگان:
🔹
افت طلا تا محدوده ۴ هزار دلار، پایان رالی این فلز نیست. این بانک مشهور و قیمت‌گذار با وجود تعدیل برخی پیش‌بینی‌ها، همچنان انتظار رشد ۵۰ درصدی قیمت طلا تا پایان سال را دارد و معتقد است در بلندمدت حتی رسیدن به ۶ هزار دلار نیز دور از ذهن نیست.
🔹
به باور این بانک، تنش‌های ژئوپلیتیک، تورم، کسری بودجه دولت‌ها و خرید بی‌وقفه بانک‌های مرکزی همچنان سوخت اصلی بازار طلا هستند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/659474" target="_blank">📅 23:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659470">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kHfvPQ5RsDSU9cRZ4-kO6zwn9bZQkkh75GxB0Bx6JQJ_Q7jZHSgIgWSh5C_O8oy5b-d5lhOEANGe1_E--LCKWqDDxQPW_UCk_TUng_HG5nC9P4lqQhFXbD16yGbjRfnBWYzOVhSMZgmciffCwO_iYlmLGDTsZLqtUtA3nbhdF0vqz7gbzTQ_g4ly4LJDzGuDN0JILb-lFeSoarGAYGAvnfkCcm02gMjQAyI01OzXRS0loanf6wL-Jod3_k9RsO1HdT3JUSyBI-PwAzM_onS3GDDbM08EPrfvsqdNEV24wqWxD3tPetoQkrd7m115TLfSgQoJdYqs5DJbDKp-9MfaZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ueqPc476RvWlKpuWMVCsSYA9ftTK66K9edTknbYVRlLTxopKSJoyjqdeiQLzKFI2OEnN9tfjJvnluBlHUtBg6M_DgsOqh-UqyhJxxcLMKR5tfivXiMQxoOJYz1dAEcblYwryR-H89HoOafQsUDsiHfxV6TuEXp3w5OLGunKsqIhZCW1acXawdjMgs64yK7OClOczAApO_34IvgPTkKsSq1IYWAXVnWQNabHc6LrETtTBHPsQY0SldzoNefBXch97FbKNxm1ov8UOLDmhsA6amTepiQ9-yTIsQBBVl7Zcl92XEQx5q1VuMyE7hy5qvJH0Ptk_RgwS-Es5aoRfDrpcGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRjbXBBcDJvAsvzHCZMyQiWmY28HTSKOYiKE4qu6KUgrHNqO6ouwKTaVOQFjRJMobLGP3BI9uAhpimHntEbXX2yq20H-BQx_6d1XVoA8wmTn_5i3sTT2TiqLK47T1O7rJMrf-ngiIx0msMcEqiaU9bHpJb8H8LYbYQfQ0tiBZfRFTsuev_aR9lEIJz1YeD9L25bGhDBwybUcBhHRvIk2CXCIyUyab-0jNbAacokna-c8bQBcrrInBTmBD1ibZf4xo9ZJ3edDqhj5pEeUXyg7d05orv7ybyxP5AJxh6yRPSOVMxBAELQI_450M9wstV32Oyulnj-4p2wagpWSHmDnnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvFQulMEdgsvgXF8ErF4QDqaHu6RAlWAcuULTWl6bKPZqOdGP9i1c5onDRXQNAXe8nbqdqXuWPWyZBuboONjmFzxpCYj6p79fSS4oEDQKORD_EUAh0kTpvMTLA98i0QUKAjUOioeVhQv5SdLa7lswmOyoFJbQMzpY7UT3yRR8-JMqGzGemDgjUXQm-5ieJt8iBkY0iU3f3NdZcdR7fyM0klRlpRWXH767oEtvTTlWlo_dS77Gy-VuVAdNFJHv2krBdBEeXWt4fyh8CoivSd4yCzuFMD5DiFv_mbARtLkVEq7aYv7R5OT-WebnZ5MdugeUHowknew8VFB6Uexrlk4lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از عزیمت اعضای تیم ملی فوتبال ایران به لس‌آنجلس برای دیدار برابر نیوزیلند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/659470" target="_blank">📅 23:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659469">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_MnaH__g4bKNmIAbVgklcmjeB1cwuSkT2ROk1tHr70PFa6D_SuQpwm8-2FA1Qg6YqaR4Y3TEKFOMFsrsu-FUrIwKVTI7Gn3QD15sX1QcY1PKbgRuFsQJA8nIXFYXZnNZgMLwaWrdCjacO_ANKBAQZdRdSK88LHQntNWWSy9N5mK37z7YpfNdckrkCr7SgrMhkTDkhr_SMnDBE7IAgJV4n8ZKyK-vP5Kqdobz1t87H8g0N-cMYiYVDDZp7ETwOGplPw6GP-dVIkUJQMGw8D3zK_BOw9WBW--mqho1otn6IAzPKr4WaLJUAVFCquj1XlTreQfun4FXcOcMvTJcar8JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلاکارد جالب جوان عراقی در حمایت از ایران و لبنان
🔹
«ما از عراق قلب‌هایمان با ایران و لبنان است.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/659469" target="_blank">📅 23:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659468">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46eeb5f33b.mp4?token=GQ13resFYw7XgcMqltXh3dBVeDVE21IcUDu1kwJOU3GtfWlnufPpy0LcCtRwvz5zUMHq5OtIDm3BG5JKHHd29j56ZhxAqNRAWPFqUa4leb9tYyYvN4-feB7LDgvfTKWxXwt8FBtju-J1EcpAXMVDMtJ4N_-G6A_0Yy2Mqq3rahhLAOFUD2__Xm2ViP2UJh5ksvF7XXTTsnNhajjwOTBIGKqfXGgy11gz_wb4ePZ5CbD5dvT163RD4GQzk_QwyJFT0e45zN2qjY6ec5pMjwCoVLdY7JzvnyGDZbMk4jHj8s1kxsOKADEavRrcWwHbxr72ZKxgWXqM0QotPrVIeQlVTnrf-Y5YyYMIdYMOVjoUw51lyinGCyem7yKfRdNbwUavKTtgpqKQh7Lz99LgrFNtfWD99mI4rKPBOxYK5hoZv2MoP_aw0Pwr8d-3h_UV8C_GFZs38CQlc4tilYp72ia-6dFu7YYTeW-iW4-Iesin-qHKv6aJs4s44SScInrtRxPbZM6Q7gFh1575Q70_hYpTPzOkqvfKv4KuaW9C9NBRxfTMutnE7YqBmlA-Mp8ke_h1Ix55F_0SJ0aGda8t-46MAisgWp23GQyxS4sSbItcBI7LNxE3nIrp40h62AVKBu61QYLo3CbXXaxrjD6j7Ww0ZSYx67jsSj0UIybzwBHjA1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46eeb5f33b.mp4?token=GQ13resFYw7XgcMqltXh3dBVeDVE21IcUDu1kwJOU3GtfWlnufPpy0LcCtRwvz5zUMHq5OtIDm3BG5JKHHd29j56ZhxAqNRAWPFqUa4leb9tYyYvN4-feB7LDgvfTKWxXwt8FBtju-J1EcpAXMVDMtJ4N_-G6A_0Yy2Mqq3rahhLAOFUD2__Xm2ViP2UJh5ksvF7XXTTsnNhajjwOTBIGKqfXGgy11gz_wb4ePZ5CbD5dvT163RD4GQzk_QwyJFT0e45zN2qjY6ec5pMjwCoVLdY7JzvnyGDZbMk4jHj8s1kxsOKADEavRrcWwHbxr72ZKxgWXqM0QotPrVIeQlVTnrf-Y5YyYMIdYMOVjoUw51lyinGCyem7yKfRdNbwUavKTtgpqKQh7Lz99LgrFNtfWD99mI4rKPBOxYK5hoZv2MoP_aw0Pwr8d-3h_UV8C_GFZs38CQlc4tilYp72ia-6dFu7YYTeW-iW4-Iesin-qHKv6aJs4s44SScInrtRxPbZM6Q7gFh1575Q70_hYpTPzOkqvfKv4KuaW9C9NBRxfTMutnE7YqBmlA-Mp8ke_h1Ix55F_0SJ0aGda8t-46MAisgWp23GQyxS4sSbItcBI7LNxE3nIrp40h62AVKBu61QYLo3CbXXaxrjD6j7Ww0ZSYx67jsSj0UIybzwBHjA1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود اضطراری «جی‌دی‌ونس» به کاخ سفید همزمان با اوج‌گیری تنش‌ها در
منطقه
🔹
شبکه راشاتودی گزارش داد در پی افزایش سطح تنش‌های منطقه‌ای و نگرانی‌های جدی واشنگتن از تحولات پیرامون ایران، «جی دی ونس» به طور فوری و اضطراری خود را به کاخ سفید رساند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659468" target="_blank">📅 23:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659467">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_RhheZ_agzM8sYluTfcMvAN1P8TP256-wAdA33AU-kBwAPcjlO4e-NK37TZhSVu4sCFH69w-YHKZQKnVfomyDeTYB8ooDY3OWFAQFv-r15wbhmj2r2eomib5xMxWQdimk72LE3KWXE_EMcQDB_u7vosxmV8Ozi58URHTuyL2B43Ix1xfSXjwnpzvhqzmkSH5rPeXQ_03F_X2D0NKuF5q9FTCSUG3f3K09IHtt3xTBTeCIuUVNuebO9FzfvR6UDaXRN7xTE2q_I8Vt1biQTzin6uKK50_zeVms4dKQSAA7hoQBnL6nwr0qtiuK9fmwrvIIr5pGTn0A5ib1h-u3gr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار برای ‌نخستین‌بار؛ تصویر شهید «حاج علی موسی دقدوق» در کنار شهید حاج قاسم سلیمانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659467" target="_blank">📅 23:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659466">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0Z2fQ7OFzIe2lVfeNBbCZRYwiHP_6upb5kDtMYZ8LYjMiPv9jyxTYqhVYvAHrHpsdmSxXDf6rdU5ppwv_5VueScXEukvmo5ZHyvQYljsNYvyFRP54YrrS3KrD1rHgEFdmF6mOVL0cTaz5wPYM1bB2etuf4tp91YFrSdRZHHgXxPE-FfPzHsrHW3iEKkygnF2jRn4oyfJ7ecvgDAzo8TWoGwtSzStGM5jtpIbows3uIXjmQV5hEqA2t_acWoynIfg6kzOPRI3n89kEQWDcS1Lplk0cDQcgNaaoMTePMpG3X3m8mpJ476JqGLbNPCc-w250UznpOA1OK7JCck_KhaTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه درباره تداوم جنایات رژیم صهیونیستی در حمله به ضاحیه بیروت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/659466" target="_blank">📅 23:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659465">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufIMmVtCgjjXZgDJkVMJjfbgUjOKCZ8zXrU3sdHamNCQHdfgl_T0fW-_VT8ii6SEgsIX_UapJj8NEa_diNhQTvsQpkIz5STtSyNB1wBKr1Be0j-e3FumovosWdhAFx4gpn7Znpndfps3WK6gxwtKDlX2oXjnU9vA-OIhlKRGFEWyr_cqzXNpdiJsMdFJJludVzmtTCI5xynuMztacuN9ssRLZjR5dObpYuWjVUjJZJNcnlkovdZv-2lNgl2U6Rczs-nj9WVt0vKWF6rK5mjMoMyqWh0OQexXFVNpVhZh0CbQMDnYdXrQVinVR2oygvadUIGnVo2crQSa9fv98hQTDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درخواست کمک آمریکا برای مین‌زدایی تنگه هرمز
شبکه WRTV:
🔹
ایالات متحده با پیشرفت مذاکرات ایران، از گروه ۷ برای مین‌زدایی تنگه هرمز درخواست کمک کرد.
🔹
ترامپ برای مذاکرات گروه ۷ با مکرون به فرانسه می‌رود تا در مورد توافق صلح ایران، مین‌زدایی تنگه هرمز و پیشرفت در مورد اوکراین و هزینه‌های ناتو گفتگو کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/659465" target="_blank">📅 22:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659464">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
سه انفجار مهیب شهرک «الطیری» در جنوب لبنان را لرزاند
🔹
نیروهای اشغالگر رژیم صهیونیستی در تازه‌ترین تجاوز خود به مناطق جنوبی لبنان، شهرک «الطیری» را هدف حملات خود قرار دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/659464" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659463">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
اعتراف رسانه رژیم صهیونیستی: حمله به بیروت با آمریکا هماهنگ شده بود
شبکه ۲۴ تلویزیون رژیم صهیونیستی:
🔹
ترامپ از حمله به ضاحیه جنوبی بیروت عصبانی است اما این حمله با آمریکایی‌ها هماهنگ شده بود.
🔹
درست است که اجازه موردی برای این حمله گرفته نشده است اما با توجه به هماهنگی‌های قبلی، اعلام غافلگیری یا تعجب آمریکایی‌ها قابل درک نیست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/659463" target="_blank">📅 22:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659462">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سناتور آمریکایی: هیچ تهدید قریب‌الوقوعی از سوی ایران وجود نداشت
‌
سناتور دموکرات آمریکایی:
🔹
اگر ترامپ می‌خواست جنگ علیه ایران را به‌عنوان یک جنگ انتخابی آغاز کند، هیچ تهدید قریب‌الوقوعی از سوی ایران وجود نداشت.
‌
🔹
ایران هنوز موشک‌ها و هزاران پهپاد زیادی دارد.
‌
🔹
به قیمت بنزین نگاه کنید، از ۲.۸۰ دلار به ۴.۲۰ دلار رسید و من معتقدم که قیمت آن بیشتر هم خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/659462" target="_blank">📅 22:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659461">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ینت اسرائیل: دونالد ترامپ از نتانیاهو خواسته است که آتش‌بس در لبنان را اعلام کند و شروع به عقب‌ نشینی نیروهای ارتش اسرائیل نماید تا ایران پاسخ ندهد، اما نتانیاهو هر دو درخواست را رد کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/659461" target="_blank">📅 22:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659456">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rBLU3WbjI8gCAHRT9KQC6Go4X26zttfOknb0eKdpfAWiQgtZWJ3Z-5kv7nWtjC-nJmbmoe7chV8AVSEHj1-jFZzpuRrPBxVUKbws70Uw3HX_SIy3PBdBsnFbU2npsJ6s15m97ttIV_Z2bk3JcEgskmk9psLXsHV6omKUlNKHd9maVfkCEojsN4KrfBfL2Pd34Hj9S_Ph85hwrL5NUk2IXmzNIMAvNc13UqQQa0jWSXkV18GjbXbMMfuY14JABVt29o7iMWqGL_1KNQP78ZZiq6oTmFCnZZkgZLj-j-i-fZcxj78UhGGbzbNyrKh8W5SiZ3LYV9WhrbUVbKgXTHSyWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffGifxHmSLMz3L1fuLGoUGJh8gIlhGLeV7XeyNBLB0Vntyd4kAya5GRCYHnj7BgeKZ7YZkc5Uek3sR8GFJkJZivk9j76-sPcFzv2Ecw2eECPbEg7EDsuiCJNangrLr6XtM_pKZNX2ZWCqHSuBim85_SC4aIKaEHWqcgWUGuJirZ6JG9qPpJXftfzx5XB4JWEuju2ozooAceQV_iODuU82oPgxt2MPlTqPrEkioagl8Pi0G7b9sIQ7XXCEQTziRYWxsmJCkp9ni2JxjaLqBh9a-SP_YhUeFlfCAqDBcz5n97cu0cNrGq2vQfaUtcf14LPykGMVfF3jintqqirjgi9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AC5mMRMZl38SA7QWLLa0NPtrETgiYjUpp3ZE6HfAcHGLbPOONYmRBGOa4vAgBBvcEi_vtJLkWxsbWz-s30yHhXSu64orgtNLjpIYbfSuKQ6RlVYMIQoAbr73RoOU7luT2lmQPVXhw2L-J2v7KwHB7T8oXS1L4_QjYybFi1SbP8HRfTyPG0qoI_YjQcrt4AKKkEZdxSK19cO0N9ul7bMzEeFHwwARL2E23Fsanoz8dOvPA-4VcayBBxgBodANtU9CcP7Oue9tq5MfWdFanQuZ4hWRxAkF36l65hyq__O1RBltPdEhIGng-rIgPoOOHTSaZ1k5EedBQo5aoQyilkE5jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/joMrkQjcplX40CFrWoKph4WVAqKNsmNS_Neg8W5RhGHN1J4YqTp7E8RxQ_0Wpq9NotvYov350_BSUQ82BaH1tCnx8ttaCd2jtDWREb7CBcGjrkCaSaJvTg7iWbJ-Jd4V5efmhqUR883uxeaQ3MLw5tAQjUF2ckVRyf0kPtOdxmWlinrqEWqkHbTqgL63WoKUbrGQ1WZBp4P8uewacDsg3LgHDdLJYMjsolLNrO7O2Yt7Yhxl8WfOBz7ugwpr-F0PH6Odafs1KkaLd1vC3uSRCYA4SJa7SHRhuFtRwYeWotsgIv_0JJT_d2pAdPTZXwruNroxzvysnL7UqZiAbYv55g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oAA5fVOo61ZNxPcIRtMBQfszab-E2Y4TlUaBkas5gemjNUcAJa7WA2qJdtBtVFJIWY-SBOCyxrz8lNSaLAqhzP58gfeguz-YXOacUVtjshCPfM2dE-i1zzUg6MI_ojq1BuNimxYRtH_9b1SVYPCC6UAXZttf1uHiGDyaNqzaI94Ub3N9e7JrvLBYBnuuFBK4fkF638Oj_NA3OaeXCbaryb3399uamoFKIVgCQAglMWBvE_MxLg7l-DImNljEBssOHdLR5Mg0j2AcZSIWWiD1ex0XQkXGWGVDcOosCh38Fro_q_0-tbgwalCuEeuesTMCc-ohR2_yYOqT14UJJOVjog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چرا نفت هنوز ۲۰۰ دلاری نشد؟
🔹
با وجود اختلال در کشتیرانی تنگه هرمز و گذشت بیش از ۱۰۰ روز از آغاز جنگ، قیمت نفت زیر ۱۰۰ دلار در هر بشکه باقی ماند.
🔹
این در حالی است که در روزهای ابتدایی بحران، برخی تحلیلگران از نفت ۱۵۰ تا ۲۰۰ دلاری صحبت می‌کردند.  پس چه چیزی مانع انفجار قیمت‌ نفت شد؟
در این اسلایدها ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/659456" target="_blank">📅 22:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659455">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jz2hgawWGBF1P7lFKvDTuK7JLrLmCDCR9szd6lnqUnvjJTH-EIAPnQtsjqYPoah3UNApBSGRv05sNzMnkStbyo4VcKener0NXQeDNmTAGhD2Qdc1-Dix86Lqepegj6Oi47H6Syy1hadVDyFcRcygpp2l-QacZ-NmuiXoL46WphapwOl5aqmW9kNxkg1bSL1T37W22g6XYYYFAKO1gErrNgZLN4uwvs-f_wyysaEkb3x5fiuVzzTcK5om5bR7g1_OR6UNbzEgrThkQrjDPqJHyJ7zgt6Yx-s8WSDHI9nBdUqYJ3MO4E7zMFv6m_B161r_Sw-ml0bVQmREGRrfd83KBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: هرگز نمی‌توانند هیچ بخشی از ارکان مقاومت را تک و تنها گیر بیاورند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/659455" target="_blank">📅 22:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659454">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
هیچ نوتام جدیدی درباره محدودیت پروازی صادر نشده است
مجید اخوان، سخنگوی سازمان هواپیمایی کشور:
🔹
درباره برخی اخبار منتشرشده در فضای مجازی مبنی بر صدور نوتام جدید برای محدودیت پروازی در فضای هوایی کشور، اظهار کرد: هیچ‌گونه نوتام جدیدی در این خصوص صادر نشده است.
🔹
نوتام مربوط به محدودیت پروازی در غرب کشور، همان نوتام قبلی است و اطلاعیه جدیدی در این زمینه صادر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/659454" target="_blank">📅 22:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659453">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/615a222da0.mp4?token=SYtotm3rHDM1ZOUEANsXP5RVkB2-2c5XCq_WkEbZUzWslTDGV13eY582_dy11XWrAbCnsBmF2EKFuExUSE2VKUJLibY3YY4faIwtZJ9X4h3wQqbClyzadxS9LFUPZYgQZMPkYtbDpSzlDDnwiS9yhORTVe4vR9vfJ-7zQ-nocZYMqx4_DjuqQ6-oUt3rYhja0L4QwXj8EAUDm5vnTs81pk9vPnna1tL1EkfrvD_Z9L3aQdV818yk0Vgk_qLMnjCr2G8i4ZN7oLHchQGjWgKkAg7-mO3cAduuNaIWyBLkGOff7X_nlWLbQ_IBFCcQVxJilYEsmfCR364xZ4-GRxPMcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/615a222da0.mp4?token=SYtotm3rHDM1ZOUEANsXP5RVkB2-2c5XCq_WkEbZUzWslTDGV13eY582_dy11XWrAbCnsBmF2EKFuExUSE2VKUJLibY3YY4faIwtZJ9X4h3wQqbClyzadxS9LFUPZYgQZMPkYtbDpSzlDDnwiS9yhORTVe4vR9vfJ-7zQ-nocZYMqx4_DjuqQ6-oUt3rYhja0L4QwXj8EAUDm5vnTs81pk9vPnna1tL1EkfrvD_Z9L3aQdV818yk0Vgk_qLMnjCr2G8i4ZN7oLHchQGjWgKkAg7-mO3cAduuNaIWyBLkGOff7X_nlWLbQ_IBFCcQVxJilYEsmfCR364xZ4-GRxPMcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روایت جذاب از مسئولیت‌پذیری و همدلی؛
🔹
این انیمیشن یادآوری می‌کنه که صرفه‌جویی در مصرف برق، یک انتخاب کوچک با اثری بزرگ برای همه ماست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/659453" target="_blank">📅 22:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659452">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImKZdOikNP9Pn69UECaQo-A2AnSqjZE_Zena2zkml7eMtuHF4riFoCp80RtthSEsQnNSSVrBOQIVGPdJSGncW9CO5DrverqDTSVCCy1Tk8VwxrU6f0vx5zc87ciIkICDbJIRztU_0L_1yJizn_11_kQzFUeSoRr1W3mqsMDw-gGiQGriDGYm1UXMAoqWFIVwS8CUhJkwrfB2boWQpzlm8-kLHxOOglMNlUXhX3QNkTJQCDP9LDFzB57cb7rczODByd-TVRmC2DRz85Q0gbZqYstk7UTpRlN1C6cgD7AfLk-1Okt_cm7c9GmdJ5S3oykoJoHN-g1VSvCTE3FFT9DTYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم رونمایی از اولین لابراتور سیار خلاقیت و ساخت | Fab Kids (فب‌لب کودک) به همت سازمان فناوری های نوین و نوآوری شهری شهرداری تهران
فب‌لب کودک یکی از مدل‌های تخصصی‌تر و نوآورانه خانه خلاقیت است که با استفاده از آزمایشگاه های سیار و تجهیزات فناورانه مجهز شده است و در فب کودک برای تقویت خلاقیت، حل مسئله و مهارت‌های علمی و عملی کودکان راه اندازی شده است
📅
دوشنبه ۲۵ خرداد
🕙
ساعت ۱۰ صبح
📍
شهرری، میدان صفائیه، خیابان شهید طبایی، مدرسه وحید کیهانی</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/659452" target="_blank">📅 22:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659451">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca0d181bb8.mp4?token=arw64IiWMA1kOxd_c3WRRC8xejS9Wu20gYq71YN7jPlne5T6vRv9DXyud2ZvjPfT2vb4yfLzGJEPhFGOsVn1lRSu1FI92l1k0OTONMD0da-_0qnhJMpLSjca-iaIQp9DqiIvf7T18bXv4gjRmY-h40vxm8ACim0MHIm8SLsf5jWt0rysaiEQ83hUkEdA5Ht48ce5Ib_FPTIWkTBjq2k1y2qSOf7FEdjcA2I9EJEydabK0Z8SNvk9_tY_oSebUVHrgezO-q5wmLrB60MlhzcVlOKbIfv7Z0VNcHkocGsSj8_qmsNdWCleEJ3HQcoAeIApBK92WIiTDxOim0YSYVS7qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca0d181bb8.mp4?token=arw64IiWMA1kOxd_c3WRRC8xejS9Wu20gYq71YN7jPlne5T6vRv9DXyud2ZvjPfT2vb4yfLzGJEPhFGOsVn1lRSu1FI92l1k0OTONMD0da-_0qnhJMpLSjca-iaIQp9DqiIvf7T18bXv4gjRmY-h40vxm8ACim0MHIm8SLsf5jWt0rysaiEQ83hUkEdA5Ht48ce5Ib_FPTIWkTBjq2k1y2qSOf7FEdjcA2I9EJEydabK0Z8SNvk9_tY_oSebUVHrgezO-q5wmLrB60MlhzcVlOKbIfv7Z0VNcHkocGsSj8_qmsNdWCleEJ3HQcoAeIApBK92WIiTDxOim0YSYVS7qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد دو بالگرد در ریودوژانیرو برزیل و جان باختن خواننده معروف
🔹
بر اساس گزارش‌های منتشرشده، اولیور تری، خواننده و ترانه‌سرای آمریکایی، در پی برخورد دو بالگرد در جنوب‌غربی ریودوژانیرو جان باخت. همچنین در این حادثه ۵ نفر دیگر جان باختند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659451" target="_blank">📅 22:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659450">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d995e7c9.mp4?token=I0rhmWUPoHc2AmePyao_d_XD2kzZIdz3JGUYPi8Wczeq_8deqmuw2lcfmiUjPNB9oHPuhWk5j-Yya0LXFZJbpMXI97x4gGxqtvt9bLKsae33FVxDU3mBlKRnJeFyRatEdKFdiB5cczNa75DscKQypCVhFv5Jkw24GpG8VoMRNEZuB3SNkwxu_XZM8mUBkU9p9NZFepdmKXthZSayQ8Gd2c4tL8Z4W18-fyxdn4gUlH6MkF7aziqTCR-bZb_-rkYhC5WyDWADQbBckMN3DZDypQU08-Ehj6XaozwSY_nGedD4ApCkrENGcBKuN2j7BdYiD8CLwK9dhMAHiXpeKdmTGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d995e7c9.mp4?token=I0rhmWUPoHc2AmePyao_d_XD2kzZIdz3JGUYPi8Wczeq_8deqmuw2lcfmiUjPNB9oHPuhWk5j-Yya0LXFZJbpMXI97x4gGxqtvt9bLKsae33FVxDU3mBlKRnJeFyRatEdKFdiB5cczNa75DscKQypCVhFv5Jkw24GpG8VoMRNEZuB3SNkwxu_XZM8mUBkU9p9NZFepdmKXthZSayQ8Gd2c4tL8Z4W18-fyxdn4gUlH6MkF7aziqTCR-bZb_-rkYhC5WyDWADQbBckMN3DZDypQU08-Ehj6XaozwSY_nGedD4ApCkrENGcBKuN2j7BdYiD8CLwK9dhMAHiXpeKdmTGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل هفتم آلمان به کوراسائو توسط هاورتز ۸۹
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659450" target="_blank">📅 22:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659449">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42d742fffe.mp4?token=vqDy1BKeLFhrkcoTgzCfg4V2mLXXt_KaIohsaRkvp_87STKnLHpgkzhpJDVh_kvKqY-kpFDgAx6mS21F9aDMbLTb81wlH8R17gg1_u13IMF0AD0dluSCKq9hCGz15U6UblNHp7WYlzQf0BQyYehIxg8ujZ3GbPKdPJuHNuu-tqQgiLeZIPHcq5CRgh8ebs4gMi4_hRUQgJKuLJwMbVHS3pA2yvWxE7Uu_OjE-doneO-gghm2ybFD8W_4KvIzLFIEPDIZGFAzriy_7XYxihn60K2R6M3mJM8xn8HkflyMrewPeRi2cyyCgPtehDFutgJTVTh9wXLNeGD0FXxNnyLMtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42d742fffe.mp4?token=vqDy1BKeLFhrkcoTgzCfg4V2mLXXt_KaIohsaRkvp_87STKnLHpgkzhpJDVh_kvKqY-kpFDgAx6mS21F9aDMbLTb81wlH8R17gg1_u13IMF0AD0dluSCKq9hCGz15U6UblNHp7WYlzQf0BQyYehIxg8ujZ3GbPKdPJuHNuu-tqQgiLeZIPHcq5CRgh8ebs4gMi4_hRUQgJKuLJwMbVHS3pA2yvWxE7Uu_OjE-doneO-gghm2ybFD8W_4KvIzLFIEPDIZGFAzriy_7XYxihn60K2R6M3mJM8xn8HkflyMrewPeRi2cyyCgPtehDFutgJTVTh9wXLNeGD0FXxNnyLMtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: شورای عالی امنیت ملی با قاطعیت مصوب کرده مذاکره کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/659449" target="_blank">📅 22:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659448">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtlW2lyRaZKYoLfS69GFmb0txjWbuPI7Zedq7AVeml1JZqsgC6HE5sGq8QIgrbpUs24zG4lRjs7MyPjpEL0irJCJ_Ek8Uk73EwBs6B7-P0Dhwjc8cwVY2zLZfrkTk48mwgPO90wdNRru6XXLEUVye0bPfm81eaj4nkjtcSPKXZHFeEkMNNa6FG1W6Hdoc21Z-UqYXm3pHXvIUVuMurt6ZtGALhg1gw-NgoCOei5DaOI5EcQRsrLUs4Bqevy-sx21sd3liEN3eQhJq5WuAI9uydL6phhMwDuaAYvT7C3u5ze8Dhla4R0YqAgOAd_YrLhKZa2MCGHqB1nQkWOyugeO-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
از فرشچیان تا کیارستمی؛ مروری بر شب درخشان هنر تهران در حراج کاویان
🔹
عصرگاه جمعه ۲۲ خرداد، مجتمع ایران‌مال تهران میزبان رویدادی متفاوت در عرصه هنرهای تجسمی بود؛ جایی که حراج خصوصی «کاویان» با حضور جمعی از فعالان اقتصادی، مجموعه‌داران برجسته و علاقه‌مندان هنر برگزار شد و مجموعه‌ای از آثار شاخص هنر ایران را در معرض فروش قرار داد. آثار ارائه‌شده در این حراج که ارزشی بیش از ۳.۵ میلیون دلار داشت، طیف متنوعی از نقاشی، خوشنویسی و اقلام کلکسیونی را دربر می‌گرفت.
🔹
در این رویداد، آثار هنرمندان نامدار و تاثیرگذار هنر کلاسیک و معاصر ایران به نمایش و عرضه درآمد؛ از جمله استاد محمود فرشچیان، غلامحسین امیرخانی، حسین محجوبی و حجت شکیبا. همچنین آثاری از پیشگامان هنر مدرن و معاصر ایران همچون منصور قندریز، پروانه اعتمادی، ژازه طباطبایی، نصرالله افجه‌ای، عباس کیارستمی، کوروش شیشه‌گران و صادق تبریزی در این حراج حضور داشت.
🔹
در کنار این آثار، مجموعه‌ای از کارهای هنرمندان شاخص دیگر از جمله حسین علاقه‌مندان، منوچهر نیازی، علی شیرازی، بهرام دبیری، رها محسنی کرمانشاهی، علی رخساز، محمود زنگنه، ناصر اویسی، خلیل کویکی، مجتبی سبزه، علیرضا آقامیری، رضوان صادق‌زاده و محمدعلی ودود مورد توجه حاضرین قرار گرفت. همچنین اثری از «آدولف ویسز» که در سال ۲۰۰۵ در حراج کریستیز ارائه شده بود، از دیگر آثار ویژه این رویداد بود.
🔹
یکی از نکات قابل توجه این دوره از حراج کاویان، عرضه اقلام کلکسیونی در کنار آثار هنری بود؛ به‌گونه‌ای که علاوه بر نقاشی و خوشنویسی، دو قطعه جواهر دست‌ساز اثر ریتا نیک‌فرجام و دو قطعه شهاب‌سنگ کمیاب نیز در فهرست آثار ارائه‌شده قرار داشت که بر جذابیت این رویداد افزود و توجه مجموعه‌داران را به خود جلب کرد.
https://B2n.ir/bu5751
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/659448" target="_blank">📅 22:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659447">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebc07bf83.mp4?token=DnV6t028VGXpQmNCSHf6t4zcgGTEJyrjyBs7tNMPaRfAmaWwIhJrac2FergwR8jo4gpbFeUZinpr3uNlQ_JW3qG3JOgDVAPjYeMYxSZCm154TE6_b7v6G2EXIkwiAp0FA6cAssf9jI0m247WvR5g1Ro94nWcghgnHzQPnYriePTA6M_ijdmp-hIulhlMgDI2dm0jTq8QtTp5LVgWaMlmGi_KOihASs03irTzEq1jhtBZ0ue5i59hvvJIdT-5w_aWJThaAHT2Z12ABZsJdt5_jbxBCXeW7O4_VuCWwCVeJaVJr-DfZWtvvGsrll3oUWgzxt4Zn00s3Urw5qRFSrhEWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebc07bf83.mp4?token=DnV6t028VGXpQmNCSHf6t4zcgGTEJyrjyBs7tNMPaRfAmaWwIhJrac2FergwR8jo4gpbFeUZinpr3uNlQ_JW3qG3JOgDVAPjYeMYxSZCm154TE6_b7v6G2EXIkwiAp0FA6cAssf9jI0m247WvR5g1Ro94nWcghgnHzQPnYriePTA6M_ijdmp-hIulhlMgDI2dm0jTq8QtTp5LVgWaMlmGi_KOihASs03irTzEq1jhtBZ0ue5i59hvvJIdT-5w_aWJThaAHT2Z12ABZsJdt5_jbxBCXeW7O4_VuCWwCVeJaVJr-DfZWtvvGsrll3oUWgzxt4Zn00s3Urw5qRFSrhEWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل ششم آلمان به کوراسائو توسط اونداو ۷۸
🔹
گراد؛ انتخاب نسلِ شیک پوش
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659447" target="_blank">📅 22:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659446">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ رژیم صهیونیستی: ایران درخواست ترامپ را رد کرد و تأکید کرد به بمباران بیروت پاسخ خواهیم داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/659446" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659445">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
لغو پروازهای غرب کشور تا اطلاع ثانوی
🔹
پروازهای فرودگاه‌های غرب کشور تا اطلاع ثانوی لغو شده است. این تصمیم در پی شرایط موجود اتخاذ شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/659445" target="_blank">📅 22:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659444">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6d836523f.mp4?token=D6x_FVWMAreJYtnU0EvKvvYNM67qshfTzQmCsKd1PRX2Nv7nqFswUwQu8lZSUG5ChdobCFSSj9Duo4VbhiMZmxhXz_kU9eeuKzWGD3XQh-tEx4XX_JaCeiFq_euwzrzd5ejshQMS9IY-f8htIsPxfsmbL0fw5AOUjVQn4jaKh5EFhSFQQFl-1lvm8IelOtGQdT6PylIkavbwsYkKAhe1_d49-v0budMIHpwOOvXnhnYDvsexth_I1a1eq285b5Bc1T8kRQyiW9g6OOMI18rGfAdczYwc-idfxzjkB3czvUrUhfUvbth9b17n8pdrBf1RANST7oScEf0IMjORNNP6ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6d836523f.mp4?token=D6x_FVWMAreJYtnU0EvKvvYNM67qshfTzQmCsKd1PRX2Nv7nqFswUwQu8lZSUG5ChdobCFSSj9Duo4VbhiMZmxhXz_kU9eeuKzWGD3XQh-tEx4XX_JaCeiFq_euwzrzd5ejshQMS9IY-f8htIsPxfsmbL0fw5AOUjVQn4jaKh5EFhSFQQFl-1lvm8IelOtGQdT6PylIkavbwsYkKAhe1_d49-v0budMIHpwOOvXnhnYDvsexth_I1a1eq285b5Bc1T8kRQyiW9g6OOMI18rGfAdczYwc-idfxzjkB3czvUrUhfUvbth9b17n8pdrBf1RANST7oScEf0IMjORNNP6ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل پنجم آلمان به کوراسائو توسط براون ۶۸
⬛️
🇨🇼
1️⃣
🏆
5️⃣
🇩🇪
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/659444" target="_blank">📅 22:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659443">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
اعتراف کابینه اسرائیل به بن‌بست راهبردی
؛
پرونده‌های ایران و لبنان تفکیک‌ناپذیرند
🔹
وزرای کابینه امنیتی رژیم صهیونیستی در ارزیابی‌های داخلی اذعان کردند تلاش برای جدا کردن مذاکرات لبنان از پرونده ایران به بن‌بست رسیده و این راهبرد کارایی خود را از دست داده است./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/659443" target="_blank">📅 22:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659442">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-6zK6JyDWONv1-VGMLG08emBhbQ9uHOl2PMQpKpJtGND1MbaQgx8rg7lFzEToriA_Qre96LXs1XF0fKQaZMioyVByidiFyyLzzbErP0xTDitukGSsLJDOG5JJgUnXDN9h7yCSkAiwzyxjim-O1frqa2amE6joAmxZbl2HZXq48UGi6rGXsqjZ0m8fs9orZPi92Sqzb8J3Pu1uJx0wlJlsjPoIRf9jIk0K6fZgL0M-xscHAmc5lexrLd8UbVCWQZtCMYTEKn-wmi6X4J9QOWkMFE-dunKsondAeWZkQWGIjmcSNiVXMuXrSmB1LeZG0I_34iCdOb_zgO0ZZBP-y0TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند جرعه بنوشیم از حکمت صد و بیست و نهم نهج‌البلاغه
🔹
سوار هواپیما که می‌شوی و از زمین فاصله می‌گیری، آدم‌ها، خانه‌ها، مزرعه‌ها، شهرها کوچک و کوچک‌تر می‌شوند. آنقدر کوچک که در نگاه ما گم می‌شوند. ارتفاع، اندازه‌ها را جابجا می‌کند.
🔹
امیرالمؤمنین علی علیه‌السلام…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/659442" target="_blank">📅 22:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659441">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYv8dZy0sdQTz7gEbddXS18Ip1JMf5KlrRijctpQ3TCxozu-s0dUSlvstAfsj7ad9tW4skaZsLnHsFKU0xcQcze-YiCsjAk4ZhIer3m2D06eHlF9i8UD8nDwFWuqBF_G_RNfMChJ7mVKcwqXLIvYROCUs3cs9hOWCzI2-plcVECq_QFZVtg-WZHu_PJGuxco5Zy4G65ZsXd5MIUT45vraUFQtJViqWUAbtblAwAXpgXlQ-w1BmpiNdqknVSoa2zxLx3pyuwuElW-QDN2HDEqJPRL0DtcZeFs_5Fpps5h6q4aoENl_gFLljMJkBE_5El0PtNpCa6EbAq8uVp8bav27Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت آسمان منطقه و ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659441" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659440">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b1f60ac5.mp4?token=XMCmOfzH0eSzGEzCP3p8_oS7nQD8hqfUWZOTvrYvo_o5DpFg69zSS_Thv3f7OZaMfltMRA_f1tKD4HJ092oi-NsaKt73At8RadUZWpmAhjwYPpNLNADjLlCRZJeytlLdfgGdujXnfcfq9KP7B_u0aj3KvdMWTOBzyn2lgANk5k0QbHUPWQbEkTTsl5H53gYDz-ON5Ly22sa8WgL915PhuneEGoRI_iz7426Ai-wrZUfh0DBGp_2sZWmXX8cpy_IC4Ert91_kKZT4dUiCsCP9Uf6vo9QxqO3hSU7DFUb7Is4J40EROSL08L2yBUPPxEF3xwD_aRzPju_GcKUo71MfaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b1f60ac5.mp4?token=XMCmOfzH0eSzGEzCP3p8_oS7nQD8hqfUWZOTvrYvo_o5DpFg69zSS_Thv3f7OZaMfltMRA_f1tKD4HJ092oi-NsaKt73At8RadUZWpmAhjwYPpNLNADjLlCRZJeytlLdfgGdujXnfcfq9KP7B_u0aj3KvdMWTOBzyn2lgANk5k0QbHUPWQbEkTTsl5H53gYDz-ON5Ly22sa8WgL915PhuneEGoRI_iz7426Ai-wrZUfh0DBGp_2sZWmXX8cpy_IC4Ert91_kKZT4dUiCsCP9Uf6vo9QxqO3hSU7DFUb7Is4J40EROSL08L2yBUPPxEF3xwD_aRzPju_GcKUo71MfaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوباما: ترامپ در جنگ با ایران شکست خورد/با قلدری و بمباران به هیچ جا نرسیدیم و در بهترین حالت به توافق قبلی برمیگردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/659440" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659439">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ رژیم صهیونیستی: ایران درخواست ترامپ را رد کرد و تأکید کرد به بمباران بیروت پاسخ خواهیم داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/659439" target="_blank">📅 21:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659438">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
واشنگتن‌پست: قطر «توافق مخفیانه‌ای» را قبل از جنگ به ایران پیشنهاد داد
واشنگتن‌پست:
🔹
قطر پیش از شروع جنگ ایران با آمریکا و اسرائیل، یک «توافق مخفیانه» به تهران پیشنهاد کرد.
🔹
توقف تولید گاز در ازای دریافت تعهد ایران برای حمله نکردن به زیرساخت‌های انرژی قطر.
🔹
هدف این پیشنهاد، محافظت از مجتمع گازی «راس لفان» قطر در برابر حملات ایران بود.
🔹
این سایت در نهایت در ماه مارس (اسفند-فروردین) هدف حمله موشکی ایران قرار گرفت و خسارت قابل توجهی به تأسیسات وارد شد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/659438" target="_blank">📅 21:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659437">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwJ7YdhvFsW3wJQuwdefWx3zupw8z6tFoV-4qnx_1smmQaF80jBvpj6QErEMP_QD2rmlJ2ET-U3h4ilEOh3Of6xyRota3MK0fEneH7T6lJLO3ZGtjqC-1as3k-2ElUOOZZbzvR7Ox-AA1n0sNGyO92N3aQRCX_pIFgOdSoh0rE0qEpegRYV3nm9b5wYmii_Hi9SVODvRt1i0entpyobowJeUaRkIp2c-l2yS0G7EHYbDltnbQh2oEZhoxf8bmotwohQYbVpHf6cVw2wHiPrMeJCHmMu-o7pgrIQcKBu4nQ9YPWgLzVJc9O19yOjtlb41Svl-UlYLcQsYqxU_JvPljw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راه خلاقانه آرزانتین برای برخورد با افرادی که نفقه نمی‌دهند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/659437" target="_blank">📅 21:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659436">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
تماس‌های خانگی رایگان شد
🔹
شرکت مخابرات همزمان با افزایش ۴۵ درصدی آبونمان تلفن ثابت، اعلام کرد مکالمات درون‌شهری و بین‌شهری برای مشترکان خانگی از ابتدای خرداد رایگان محاسبه می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/659436" target="_blank">📅 21:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659435">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lr_jkDytvVbZM63yT26K47F3GVINjWkd-QyQ6IHgbWAiAZGnN302EWP7UolCPqANvg1aS0tgmP2pviv1w2lmmigOSwFYIteWVtA2EUfDYbu-qAzSbYEBiVnk572CW4SWV1xAeIAQmEFfRNYmb0CQjO_93GF9vn4fCAsxdbcRXDdzHdawkmLZvo2qkaB6pQhTMR7IW_7FBapc2pLjY4aQMYkdLZxFM0KY8G2nTndjlrVaf-ldekDZKZ0Xknpa85jHHqTXVwwung3APPWuT_FQYDYMgyp3DLZnvI-VNOBAHfdJplOQdwqd0nBzCAFxMkugdh2H4m9jDa736igLiE8ktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حتی شاید مطمئن‌ترین محافظی که داری، مامور انتقام تمام خون‌هایی باشد که ریختی
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/659435" target="_blank">📅 21:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659434">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
رئیس اتاق بازرگانی مشترک ایران و چین: پس از مذاکرات، صادرات و واردات از چین به بیش از دو برابر خواهد رسید
حریری:
🔹
با رفع تحریم‌ها، تجارت ایران و چین پس از چند سال می‌تواند به بیش از دو برابر برسد.
🔹
واردات از چین در ۱۰۰ روز اخیر کاهش یافته و بازگشت مبادلات دریایی به سطح قبل از جنگ چند ماه زمان می‌برد.
🔹
مهم‌ترین دستاورد مذاکرات را نیز رفع تحریم‌ها دانست./ خبرفردا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/659434" target="_blank">📅 21:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659433">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/355711d5b9.mp4?token=Fm9iWknq6H0cj4EZBb7WsQAXr6gT2B99iTendrS1MZfTyt5H0NBSUf-ubvq6QxKMjiIy0l35oEq-T3iRw1gZsmeqcEztMXm2VNVK3mpiWe_wtv4YK0evu7h5zU5hez_R4Ty-T6kz1wN7b7lFr5vecgmQau6iK9ohCiaBgrMSB5J-n9YPYrP5DRH7JHdsNzYEwMjQVpKDrhzZ5e-_TJP4IO5ZULoKHBRi-5CGBUCG_VeURbMHkwq5h9rk-D7-rmglBQr_IuHUQRK6vHbshnHHv6j2hnu8olKBRQbgUbcDOOEJmH8K4JAa3ParkAElPfolGMPHFqITMugOjl3V1SKiHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/355711d5b9.mp4?token=Fm9iWknq6H0cj4EZBb7WsQAXr6gT2B99iTendrS1MZfTyt5H0NBSUf-ubvq6QxKMjiIy0l35oEq-T3iRw1gZsmeqcEztMXm2VNVK3mpiWe_wtv4YK0evu7h5zU5hez_R4Ty-T6kz1wN7b7lFr5vecgmQau6iK9ohCiaBgrMSB5J-n9YPYrP5DRH7JHdsNzYEwMjQVpKDrhzZ5e-_TJP4IO5ZULoKHBRi-5CGBUCG_VeURbMHkwq5h9rk-D7-rmglBQr_IuHUQRK6vHbshnHHv6j2hnu8olKBRQbgUbcDOOEJmH8K4JAa3ParkAElPfolGMPHFqITMugOjl3V1SKiHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل چهارم برای آلمان توسط موسیالا دقیقه ۴۷
⬛️
🇨🇼
1️⃣
🏆
4️⃣
🇩🇪
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/659433" target="_blank">📅 21:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659432">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_BktAsy_1dgZesuY_XIXDTgMjWgUDy349nFMM81-comLc30r5TI8VC6h9S50UAP-VfTr7yKNfnLbI7dp1ZMrMf7RtaTKA91UQEw6crnNYcsGoXRifV8XxLhb1gzVCEkmlyIx5Qtq0OTLpQP4_NQcJhV4-mu6-E3v8FRQWCZnqnkf4AaUm3-Gr1O3EAsPXaPKJt6BLrcEuu_5-IZ7t_dQTh6MxrPBXfEZLWqRH2dUbC_WGrCHsH3YEsG-a2UbNC41GuBh7ioIzB6IeXc6tJWhlbXKuyh5n42dUqbvMmcbxsTrQ-0-Wd2-AqGu6Q9ESKIzAeMgRzqpk39YYTcF2PySQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیروزی عظیم حزب‌الله در راه است ان‌شاءالله
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/659432" target="_blank">📅 21:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659431">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یمن: نتانیاهو بدون چراغ سبز آمریکا، دست به حماقت نمی‌زند.
🔹
ارتش فرانسه: ناو هواپیمابر شارل دوگل در غرب آسیا می‌ماند.
🔹
دست‌کم ۱۲ نفر در سقوط هواپیما در شهر باتلر در آمریکا کشته شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/659431" target="_blank">📅 21:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659430">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
سرقت ۳ میلیاردی طلا از زن سالخورده با ضرب و جرح شدید/ متهم: پول را برای خرید طلا و ازدواج می‌خواست
🔹
مرد جوانی که با حمله و ضرب‌وجرح شدید یک زن سالخورده در شرق تهران، طلاهای حدود ۳ میلیارد تومانی او را سرقت کرده بود، پس از دستگیری اعتراف کرد انگیزه‌اش تأمین هزینه خرید طلا و مخارج ازدواج با نامزدش بوده است.
🔹
قربانی پس از انتقال به بیمارستان از مرگ نجات یافت و جزئیات حادثه را شرح داد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/659430" target="_blank">📅 21:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659429">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7013e1863c.mp4?token=vw8TBLaZG_O-IdZdVI44cT7m_K8r7nrKsak-hm9T_o25WcZFeN_de0-ry7vtCVXiIw9CWSxZmujdDG5ziCNIzd6CZ2auuVwZ0naSLHx1Hr6u-MjGfv2CPOq7wNaEgzd3-nIrwktoe2CQHYImOmwQRMj2Sh73XFJ3IqsU8UKRezTo_XRupVNowiWuo2tUp3hFYg-vzCPYY3PkggQ_ep0WYkx6icgZX5cVMbnJk-Y_QYE7UcZ2ZWU3C1d6pZvj91P8hDYxre4GsWp4kd_Ofzv1VTpigP6bAoifVqBccauiJLt_6-UdPd5NdY642xhfiC1Z5c-WvikTxwsFIBzMs2U3QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7013e1863c.mp4?token=vw8TBLaZG_O-IdZdVI44cT7m_K8r7nrKsak-hm9T_o25WcZFeN_de0-ry7vtCVXiIw9CWSxZmujdDG5ziCNIzd6CZ2auuVwZ0naSLHx1Hr6u-MjGfv2CPOq7wNaEgzd3-nIrwktoe2CQHYImOmwQRMj2Sh73XFJ3IqsU8UKRezTo_XRupVNowiWuo2tUp3hFYg-vzCPYY3PkggQ_ep0WYkx6icgZX5cVMbnJk-Y_QYE7UcZ2ZWU3C1d6pZvj91P8hDYxre4GsWp4kd_Ofzv1VTpigP6bAoifVqBccauiJLt_6-UdPd5NdY642xhfiC1Z5c-WvikTxwsFIBzMs2U3QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد دو بالگرد در ریودوژانیرو برزیل و جان باختن خواننده معروف
🔹
بر اساس گزارش‌های منتشرشده، اولیور تری، خواننده و ترانه‌سرای آمریکایی، در پی برخورد دو بالگرد در جنوب‌غربی ریودوژانیرو جان باخت. همچنین در این حادثه ۵ نفر دیگر جان باختند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/659429" target="_blank">📅 21:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659428">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
وزیر علوم: از ۱۳ تا ۲٠ تیرماه هیچ آزمونی در کشور برگزار نمی‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/659428" target="_blank">📅 21:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659427">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c9c5aa976.mp4?token=NtN8l67ngx_b-x2e5c1bhdFGm2mIPwUnxSgjRoIn6-Wf0RxA1OvRNIk_GE-dtDtKZBt_eXgAddbGGXvjy0XgMsVnk4RNg-RBAaB6LxpZIUZR79-yrpP_XJVrKFwZ4q5zBaW4z-O6O8y0U_7YcOfQxGbVBSKHUbrGS0-XU2brXx95m_SliFQ3Qz_8CFK6LwvDz2vO94fkEwkIPpHxfIPDdOJvp7SMoGUnrHQOFq4VzV1E6zULpZw4ETaFt-TdquS0IxJYJ2VVmoAVlX98ehjtQDIoE9aye_3MiZZhFA85pI8QN_zfaBGRwEVPY-blODTS1qfbrMGRQpU9v80Y-NsdDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c9c5aa976.mp4?token=NtN8l67ngx_b-x2e5c1bhdFGm2mIPwUnxSgjRoIn6-Wf0RxA1OvRNIk_GE-dtDtKZBt_eXgAddbGGXvjy0XgMsVnk4RNg-RBAaB6LxpZIUZR79-yrpP_XJVrKFwZ4q5zBaW4z-O6O8y0U_7YcOfQxGbVBSKHUbrGS0-XU2brXx95m_SliFQ3Qz_8CFK6LwvDz2vO94fkEwkIPpHxfIPDdOJvp7SMoGUnrHQOFq4VzV1E6zULpZw4ETaFt-TdquS0IxJYJ2VVmoAVlX98ehjtQDIoE9aye_3MiZZhFA85pI8QN_zfaBGRwEVPY-blODTS1qfbrMGRQpU9v80Y-NsdDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان نیمه اول|
گل سوم آلمان به کوراسائو توسط کای‌هاورتز
⬛️
🇨🇼
1️⃣
🏆
3️⃣
🇩🇪
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/659427" target="_blank">📅 21:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659426">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22576d836.mp4?token=Ea4bTXs45ZPHS7JDdpeTQUo8aBYJk8-t_KMouFvs8sLKdheJK1PAuweDpBxHxWO8hw_kWWtigjhRN4lExvVoj1dNAcTq5z3WRTQ3l3CCEhGs6xEPxJ5iimvfLgBhd518Zdq338hoAtjlLhss_GQnIjvVTmEtdDh2gOegetOur9eTlkpbOluaYpHh3FHSH6k85L4P75uR_nXSFU9POO76w88K88SfwUS4VcfDBENIAFI6TJ2VOHquDISedTDtwG3LbK310lNz9WBkFcxcJXuQ4ygiMdBWUTmoBIEDpuGqBmIBcU5Y9ICb_nZhlBUAiw9O8mc0IUOhem2ZnxvisYxV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22576d836.mp4?token=Ea4bTXs45ZPHS7JDdpeTQUo8aBYJk8-t_KMouFvs8sLKdheJK1PAuweDpBxHxWO8hw_kWWtigjhRN4lExvVoj1dNAcTq5z3WRTQ3l3CCEhGs6xEPxJ5iimvfLgBhd518Zdq338hoAtjlLhss_GQnIjvVTmEtdDh2gOegetOur9eTlkpbOluaYpHh3FHSH6k85L4P75uR_nXSFU9POO76w88K88SfwUS4VcfDBENIAFI6TJ2VOHquDISedTDtwG3LbK310lNz9WBkFcxcJXuQ4ygiMdBWUTmoBIEDpuGqBmIBcU5Y9ICb_nZhlBUAiw9O8mc0IUOhem2ZnxvisYxV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آپدیت بزرگ تلگرام؛ پیام‌ها حرفه‌ای شدند
🔹
تلگرام در آپدیت جدید، امکان ارسال پیام‌های پیشرفته و فرمت‌دار توسط بات‌ها را فراهم کرد؛ قابلیتی که تعاملات علمی، آموزشی و خبری را حرفه‌ای‌تر می‌کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/659426" target="_blank">📅 21:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659425">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
اتباع خارجی چطور می‌توانند در ایران ملک خریداری کنند
مدیرکل امور اتباع و مهاجرین خارجی استانداری خراسان رضوی:
🔹
اتباع خارجی فقط در صورت داشتن اقامت ویژه یا فعالیت اقتصادی و سرمایه‌گذاری قانونی، با دریافت مجوزهای لازم می‌توانند در ایران ملک خریداری کنند.
🔹
خرید ملک به نام شرکت‌های دارای مجوز نیز ممکن است، مشروط به اینکه سهامداران ایرانی و افغانستانی به‌صورت مشترک حضور داشته باشند.
🔹
هرگونه خرید ملک خارج از این شرایط غیرقانونی است و سند به نام تبعه خارجی ثبت نمی‌شود./ اخبارمشهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/659425" target="_blank">📅 21:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659424">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aeaf8fb29.mp4?token=YG7Vr239iZc7gpflEm03eqWSr7tCc_W1HU5KCaTNqwP4S-aI9wLqA9g54xrQL7j_k-l6HS4Gh4g82NFFyazkUGbZzKGBu1rvu1kzaAf5auy0d8hcTGV60qSrNRwz2s1_dvA-hqT9bYw3nIIiGy4ko-Fxv1e4sHcFqbhvmot0lfqs2vMW1_Fb_DZr5_NcQJjZFuVxf5GUkAcXM0mxWqY1n-6e7EcLeVRxr2BTAZTnOgBuxutg6RE6o3T6qox2QDUa6g9jp54xAgLaKrhQT8wxfYGtM1rkhsYNOC-hCER5jR5A3vLkCMql9ZN4A7E6jKjr9FCnYmM0ogRx49z4FMrC9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aeaf8fb29.mp4?token=YG7Vr239iZc7gpflEm03eqWSr7tCc_W1HU5KCaTNqwP4S-aI9wLqA9g54xrQL7j_k-l6HS4Gh4g82NFFyazkUGbZzKGBu1rvu1kzaAf5auy0d8hcTGV60qSrNRwz2s1_dvA-hqT9bYw3nIIiGy4ko-Fxv1e4sHcFqbhvmot0lfqs2vMW1_Fb_DZr5_NcQJjZFuVxf5GUkAcXM0mxWqY1n-6e7EcLeVRxr2BTAZTnOgBuxutg6RE6o3T6qox2QDUa6g9jp54xAgLaKrhQT8wxfYGtM1rkhsYNOC-hCER5jR5A3vLkCMql9ZN4A7E6jKjr9FCnYmM0ogRx49z4FMrC9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم آلمان به کوراسائو توسط فلیکس نیکو اشلوتربک
⬛️
🇨🇼
1️⃣
🏆
2️⃣
🇩🇪
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/659424" target="_blank">📅 21:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659423">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukp9WFF9dYHNzTLKuUPmVG1vGILStubk4DVOxI-PaqILFnvXzpKYtv9M3DpBaFXq8wdSur0RWwHklHWlXoac2La_63nGgXsLvVY8weSSNZ2Lv1CroidHBNgfw5R2u75JzrSP_XYy8Vr37HOobpS0VAK0XAmRiZ61QtxDghEEYVsiQkF4LX7j69Ktz5OzDVLVqxlOTD3N1g71ftQ2Kg7u530k9sN7hV_oMBf6e0OXRhaeQ6kfX19tbHoG6i2vWGaJtBUO51D4Sml_VKlUtu0bFYOuUbLzpvGUJTbGaC5HvDBhNgD5m4vVcY61BmSX2KXtR4o38vD-23PWMj_o08NKkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: ‏پاسخ رزمندگان اسلام در پیش است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/659423" target="_blank">📅 21:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659422">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
خدمات و‌ کارت‌های‌ بانک ملی فعال شد
🔹
خدمات بانک ملی ایران پس از بروز اختلال موقت در بخشی از زیرساخت‌های مشترک شبکه بانکی، مجدداً برقرار شده و هم‌اکنون در دسترس مشتریان قرار دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/659422" target="_blank">📅 21:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659421">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ادعای منابع الحدث: یک هیئت قطری اکنون عازم اسلام‌آباد است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/659421" target="_blank">📅 20:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659420">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07526040b6.mp4?token=sia2kmzCgjJlPBr0TGupwwJ-qPcIAOlIUKeMRyrZPiJUQUsy8E5z9CKugax2Nw9-aQFFWsIbBRDRCK3jycZ6OzjyYjS-T0dcQYXfjjvvr1NaWmGwbRvjAz8HQJZhsdrtsWczQqN_VR1FJUsA9UViFVMGDUy9sH3nWT8OBRRIecn_P6Z3ZwkFbeJeqLzFLS1mt95RyMxPb9-bilGrPgUMCCP3ffhGdeR98KGiiY1e_Fqqjy3rAxPE246XQt5abgl2pDEbM1gG2o5xN00wwd5VlM4Z-cC07t8J-xImMvFp3GF9dKvSxad7FFiRfpZ1Hhloy4wPkAJf-TYw28Bb1z3_bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07526040b6.mp4?token=sia2kmzCgjJlPBr0TGupwwJ-qPcIAOlIUKeMRyrZPiJUQUsy8E5z9CKugax2Nw9-aQFFWsIbBRDRCK3jycZ6OzjyYjS-T0dcQYXfjjvvr1NaWmGwbRvjAz8HQJZhsdrtsWczQqN_VR1FJUsA9UViFVMGDUy9sH3nWT8OBRRIecn_P6Z3ZwkFbeJeqLzFLS1mt95RyMxPb9-bilGrPgUMCCP3ffhGdeR98KGiiY1e_Fqqjy3rAxPE246XQt5abgl2pDEbM1gG2o5xN00wwd5VlM4Z-cC07t8J-xImMvFp3GF9dKvSxad7FFiRfpZ1Hhloy4wPkAJf-TYw28Bb1z3_bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آگهی تکان‌دهنده‌ای که یک بحران خاموش را آشکار کرد
🔹
بیش از ۴ میلیون دانش‌آموز آفریقایی به پد بهداشتی دسترسی ندارند و در دوران قاعدگی ناچار به استفاده از روزنامه هستند؛ واقعیتی که دو روزنامه مستقل آفریقایی آن را در قالب یک آگهی به تصویر کشیدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/659420" target="_blank">📅 20:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659419">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/147dc7a2d4.mp4?token=BFsGRyGj7PG09lC8lvltR6wKcgDebK6ngnunwkzNkjj8pBPbUlAtK2fL0h1XlJk69yjeff75AreChIi0VcOwq4oVe9Z7-xGzDXryby6UItMMRt8RKrF0oQ0gmLvg5s6bhzOQLOAXLZFkTcjbd8UepJnF1jJhGVv8b_sYw4a5reoNGOdWiBK3yvC6vAfr74bGlfHYedtTJ5yoSten4Et-H0F8y8kCAVyDRetfdvTeaPQZzLkLHfKuqEuBE_Pu2nTcEBFy3H4D9DKeucpWb6qSdWCacRM4Zm9OC0S8Vn0NY2-lO_0vFsMiEuT2pGmiH5WlF7b821uGvebI3EDrR1mG7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/147dc7a2d4.mp4?token=BFsGRyGj7PG09lC8lvltR6wKcgDebK6ngnunwkzNkjj8pBPbUlAtK2fL0h1XlJk69yjeff75AreChIi0VcOwq4oVe9Z7-xGzDXryby6UItMMRt8RKrF0oQ0gmLvg5s6bhzOQLOAXLZFkTcjbd8UepJnF1jJhGVv8b_sYw4a5reoNGOdWiBK3yvC6vAfr74bGlfHYedtTJ5yoSten4Et-H0F8y8kCAVyDRetfdvTeaPQZzLkLHfKuqEuBE_Pu2nTcEBFy3H4D9DKeucpWb6qSdWCacRM4Zm9OC0S8Vn0NY2-lO_0vFsMiEuT2pGmiH5WlF7b821uGvebI3EDrR1mG7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول کوراسائو به آلمان توسط لیوانو کومننسیا
۲۱
🇨🇼
1️⃣
🏆
1️⃣
🇩🇪
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659419" target="_blank">📅 20:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659418">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i11-FA16LBu9OCDiL2xG7bajXOb84CZO77Z0sVeZAAlwHFUg4dcIYpfxYn6luxtNCJ3FTLtMc6XtlGcfUREAjbYSCcAkV0pqyAhr8oyzpZLzwixeKNlCVpY5xhESG8maX9pwPVnNlBpETLbAxdGE0j2kBhVB0wfa-vZk0K7wCNWk9JXC1YIZVNXu_Hl5oxDywQNYufSjqGELkCTIlILGHTZuq0J_BKgGSVEyUny2epYYLwJopBXZ46pJhjKIGjRZyopZEPf_rG0iHnKocELw0-2fbrgG-PLygLFiAnzr3wHnJfFW9Vy2FjjSE_PON2q4CFpGEva2_ZmNjdPS0dYdbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نقره در ۱۰ سال گذشته؛ رشدی که کسی باور نمی‌کند
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/659418" target="_blank">📅 20:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659417">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzc7j3U52VtRxIoRgEpUuEEr-0F-jzI0t7aEPrjKVj0JqfmaEqN90z4sPyBRuG0jRQfJ06VawR9HgJD403gLot-vXsN3Er3_4XV4Z85oVvR9MS4SVInLlmdLM25agk050ljOYFvMEWs-VjjiiNFBkRWcrQm4x0hQBGd-iG3VstK5GA1N5P-IQGbzt6uw4Tg7Vh5UT1EZfHkaGyRc1pc-Mlk21QdUssHi9FP4CTg3pAZGBw5bUydNlXJAfvHU0UxVVTQuOL42Xxi3rpVjjvB6YRiUmeoPLC7tx8KLwLS0Dd3uIToruY7282iOQ-SMfsOhzsKmnXRbPq1H3NooFyZJYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/659417" target="_blank">📅 20:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659416">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
خدمات کارتی بانک ملی تا ساعاتی دیگر وصل می‌شود  شرکت خدمات انفورماتیک:
🔹
ارائه خدمات حضوری در شعب بانک ملی از ساعتی قبل آغاز شده و خدمات کارتی این بانک نیز تا ساعاتی دیگر برقرار می‌شود. بر اساس این گزارش، تا ساعت ۱۳ امروز بیش از ۷.۶ میلیون تراکنش در بانک…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/659416" target="_blank">📅 20:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659415">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سخنگوی فدراسیون فوتبال: روادید تیم ملی ایران در آمریکا ساعتی نیست
🔹
تیم‌ملی با پرواز چارتر از تیخوانا به لس‌آنجلس می‌رود
🔹
قلعه‌نویی و طارمی ساعت ۴ صبح در نشست خبری شرکت خواهند کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/659415" target="_blank">📅 20:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659414">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a462ceaf5.mp4?token=GmYJsBXnX9ILvPHNktQGUwqnE0RLVmevYvUrSUszDA6zpVp110hsUbRM8MBjJZQrxWyAgwPaA3RbAjEdEQSWO78TbfQotH8Uc02FBf8A0WBRTVlG5DYuSaZ8h3gpKfYvOBaqSoC50qMyd-Y1UFFt17XIfR24fp-8udnWzlhec2WCppXMGKKeC-rg_K2i1yNFlNQb7y65P3ruLQYvtzicdbey0NAh3n1uPVOiAP6P6dqYzCe9r99qUNxU8C8eC97f8Ndbnn6JQACP-ilRFoNEsExxcIWmpNWsw4bEZvnlN2-VSruU2lX3LUNr73kVgRNwiR8EPoeURdZl2a2q3EKLPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a462ceaf5.mp4?token=GmYJsBXnX9ILvPHNktQGUwqnE0RLVmevYvUrSUszDA6zpVp110hsUbRM8MBjJZQrxWyAgwPaA3RbAjEdEQSWO78TbfQotH8Uc02FBf8A0WBRTVlG5DYuSaZ8h3gpKfYvOBaqSoC50qMyd-Y1UFFt17XIfR24fp-8udnWzlhec2WCppXMGKKeC-rg_K2i1yNFlNQb7y65P3ruLQYvtzicdbey0NAh3n1uPVOiAP6P6dqYzCe9r99qUNxU8C8eC97f8Ndbnn6JQACP-ilRFoNEsExxcIWmpNWsw4bEZvnlN2-VSruU2lX3LUNr73kVgRNwiR8EPoeURdZl2a2q3EKLPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آلمان توسط اِنمِچا در دقیقه ۶
🔹
آلمان ۱ - ۰ کوراسائو
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/659414" target="_blank">📅 20:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659413">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Th2mOTOxImwi3VxYe2mx7cgyTWFttRot0ZzsMO3y42-nTA_ng_2HU9e6ACw5SEwE9CF-H9Y6u1YDGmvIPIif_qOZDq6gfk16pH7QXJMI-baQXdK89vhj-NpK4ufyHBxDwptqWz9hjSCEwRsQRPVBRWgck0Kye_p4d7dPRigfl0l47EIDOC2X02msn0gbP-rQzJgvdwsX0f4DjOhOhBPRqJ2ms_8O8uSXxvhWzprkHyK9Vkso9eNPWId2PHlbMQds4QY9nvbL9hzhuOLKqXYdSuYLF43ycArBg6dutKamujfjpaGcpuX21XNmOem5UWBeMUBhZ8jJM2ZVOZ3e58tlvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده قرارگاه خاتم الانبیا: فرزندان ملت در نیروهای مسلح «دست به ماشه» آماده شلیک به قلب دشمن هستند  سرلشکر عبداللهی:
🔹
انتقام خون امام شهید هرگز فراموش نخواهد شد.
🔹
نیروهای مسلح با توان رزمی و موشکی ارتقایافته، «دست به ماشه» آماده پاسخ به هرگونه اقدام دشمن…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/659413" target="_blank">📅 20:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659412">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjXZ178j9ADvGslZEDw-kCKwhFjAzU5dM0rmBPMW2Q1zdq-i_nvpHmLVoz_Xggd49LdWqG1g8kUsSMYOpWc8bueDAMSHmKNishjs5QG_XY_9gnSd4OWRU7ldIZ0pfyy8SPTjyQFDQsYzmeU58TTTIJL3GGY7xiEI8BHYoB5ymfMjQa0IXcNQ3q61Rn-QxJlvSIiaRE6aXj7aAhMumK06DT4zd80OzD21uVdfxXosOWDNsXpBDy0wdENTQFQ-2zLCiSO14d9I5T5bCKyqpTvwit_ZRnXHLT3bZ2u0ApmE8dgcb47-opds5cMPQgOf8XTsuZPtM4Vq82iO_ts_d6I6jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: پاسخ به حمله امروز اسرائیل قطعی است
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/659412" target="_blank">📅 20:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659411">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e324ef00.mp4?token=D3AMmbRgO4wzGDQMm91z33354bpVwUGHDzCKk3ViddFpn_Yu4ea65LKTdn20fD_MHdzTyxeVwEl63-etM6qRiXjFODjQ5N5C3SaLaTY8SLIVQGU2e7K_plCBhSHZ78drK6E2PsEJK6uFdbDnIhSgSN6P8I1KtpLTeINScTGjca4PcHHPP9weLSS654TVGdWxt2qWXQLt5yPG_tRVYd94o0Ba5hLXyE5bNKXWKiJO96tzEJ4OfcT_gshW_LTLCyIyqBAYYK8MjB0j7qLcJJd3nd4rr5Fe5KiTKiISQu6wdg14O2jifzYpAjCoTFjbvLqyySHMXkF7AwTBuV3fq_SyPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e324ef00.mp4?token=D3AMmbRgO4wzGDQMm91z33354bpVwUGHDzCKk3ViddFpn_Yu4ea65LKTdn20fD_MHdzTyxeVwEl63-etM6qRiXjFODjQ5N5C3SaLaTY8SLIVQGU2e7K_plCBhSHZ78drK6E2PsEJK6uFdbDnIhSgSN6P8I1KtpLTeINScTGjca4PcHHPP9weLSS654TVGdWxt2qWXQLt5yPG_tRVYd94o0Ba5hLXyE5bNKXWKiJO96tzEJ4OfcT_gshW_LTLCyIyqBAYYK8MjB0j7qLcJJd3nd4rr5Fe5KiTKiISQu6wdg14O2jifzYpAjCoTFjbvLqyySHMXkF7AwTBuV3fq_SyPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور مکزیک به دلیل هزینه بالای بلیت، به جام جهانی ۲۰۲۶ نرفت
کلودیا شینباوم:
🔹
به دلیل قیمت بسیار بالای بلیت‌ها نتوانسته‌ام در بازی‌های جام جهانی حاضر شوم، قیمت بلیت ورزشگاه آزتکا ۱۲۰ هزار پزوس (بیش از ۵۰۵ هزار روبل) است.
🔹
من بلیتی در اختیار داشتم که آن را به دختر جوانی که عاشق فوتبال بود اما توانایی خرید بلیت را نداشت، هدیه دادم.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/659411" target="_blank">📅 20:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659407">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3D2SEhezGCmopEB66RgpF4CxI1pSHgwxjAXoIBP-7IbAdKZKvoDMf4lQ7-j48w-hZO4gi9QFPDapW435D5c3AxSBQUJu7aGRTq5TEH4mxSTDvpokPhUUk3crx7FGNNJOnDlRPd3m2sXAnDHlAkX1ePgaml5YODCMqLnx455oWg6Bveao_eZlgqS29mh9dC0cteMDxXuHOBfB59Gwk1V4VgafQm-IWNcmDkLTYDHWxcuwzGW9vxhsF1MbqZcxeymJ36wZAJ-kiwBBHy8kAHcc-NQZ4KuVB2W-wmQQnMMyEtZSDXhI4klrQiw4qVmYWjoX7PGC6jOOR1naCewgVAfoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TggUQTGv3gYDibXorgCTy4PHLlH_HfWKGCjTq-Zlo4zWDfj_sLEvCMnKgSpblU5Vf9qzFQxdv8Wo4Uqs3wZEGrgousIPXQJDeUvrwjm3SYS8EFvLSiKsHDcdotqEJshdmjQ910HOtWqHke_roI0zaQ5ktGjVvvna8zTU0y0cBtt8WoP1VA37eAIr0zsxEKFOEYPYS1-dxExpRsY2sV69Ap3171zs5t211mRto6UEhgpET57If9dvyplq5od4JHo650U7oVFLtprJLQgLernMW4Kf4qa6Ood0BgiWG5tr_KClFCy5G-BxQuWKT7kHDdi9QXzX-u3WKCnPkGqENkKX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hV5nsSJdinSx7pwyGIQ0uj3xZt1Hi3Veb8rKhWtv-dvqBGHXztqZU9wxuLS29MGZSbFVOqsTtjLRxnOYrimf7AUTQmdGADS9hqeAdOMFLhEupc718pSJ6-MRUaO_hxsAc3842kXcXMJPjZWev6_aorY7hBQ4pN8OkfXh3_oPDtvG4yTZ3GDal1fhC-gVS5y094bRdvYb4wYqu3omjLN_8F3vz8C2QSguPCuNLwy5xkfVxG59nRk6FfY3iFJhv9G6BQsjwccM6Fo7j2vvmOWhjuwOox5LN764-5MqMNNiX6jMepsdxcwGrDg2nmX111tMIIyhoAb1ySiIQ7QpQ3IBjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ry6t1iJs36DwXRdmJdiOjphhgn4c1KuN_WZULGWFxvosvS9zdRqvfJcR2acP6SeeCfFj00w5mWMSzOZ6arldBKCrq2uh33Zo9GyQ1gm2hbXUMXo5Jx69679qH_AgNecLwcVNC_bKuvXvyVBYezSdZEDudJKNBSdaCoCl9XkMb-flwybOJlrdstwLUeXlYos5KtAFnmquqr4SjDuqYqLATqGiUrNDlRFRALASdyelqd1QNd_720cQwJwkOchYa1l65JQJ6wJEBaYAh3rDc73LsJOmjDkRAP2qFeJSR8XSYB7q3fHdAd6nmFXlRgNIoadbgO0kzqhEyJVMN2TOuBauWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
لباس‌های بازیکنان و اعضای فنی تیم ملی فوتبال کنگو در فضای مجازی حسابی سروصدا به پا کرد
🔹
این تیم آفریقایی که دومین حضور خود را در جام جهانی تجربه می،کند، کارزار خود را از ۱۷ ژوئن با دیدار مقابل پرتغال آغاز خواهد کرد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/659407" target="_blank">📅 20:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659406">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
تا دقایقی دیگر پیام مهم فرمانده قرارگاه مرکزی خاتم‌الانبیا (ص) منتشر می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/659406" target="_blank">📅 20:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659405">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
اظهارات تند مقامات اسرائیلی؛ ترامپ ما را فریب داد!
🔹
رسانه صهیونی وای‌نت به نقل از یک مقام ارشد اسرائیلی نوشت: «ترامپ ما را فریب داد و اکنون در شوک هستیم. آمریکا به ایران امتیاز داده و ما دیگر نمی‌توانیم بر روندها تأثیر بگذاریم. ایران توان موشکی خود را تقویت می‌کند و اسرائیل باید هزینه‌های سنگینی برای دفاع بپردازد.»/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/659405" target="_blank">📅 20:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659404">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbygljE4dChupfCP1snY6efi6dPlBFpriSfpOt-1KB6Py6gY1Cdx-8V9_Fgo5TGpNzdWnVYkC-BxvKaudOG_s0utYhx9v0ONYy3Qd8OxyIClzYygIsdKSnzDfeZPD-1R77YqheisEwx4KzPR-f0JTlwoQiDtBAel19x5Cb76B61sqFB2XfdYMnwdFZGrH2x3k79UhX8Hghfs69fJlcxcThN8TULj8Wd0hKP5Ke9-OK7yiwZ7zoBWm1IQYIYIWyOy7vfK72TNa2bZ7ReCcZXdUTVvCvKE143VJM8Y53TjFuVE6rVV4c1FwONMsupDJUC7g825fpW35oYe0izBVnTFmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین جهش سرمایه تاریخ
#بیمه_البرز
مجمع عمومی فوق‌العاده بيمه البرز، افزایش سرمایه این شرکت از ۷ به ٨/١ همت و سپس ۲۹ همت را به تصویب رساند.
▪️
افزایش سرمایه چشمگير
۲۹۰ هزار میلیارد ریالی
▪️
و تمديد مجوز قبولی اتکایی از داخل
دو بال قدرتمند بيمه البرز برای راهبری بی‌رقیب در بخش خصوصی صنعت بيمه
بیمه البرز؛ توانگر و‌ماندگار</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/659404" target="_blank">📅 20:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659402">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/haG2o64uxPnI0hZBfsjdB2aiDbQufzfKNV7qQ36fFk3j0-xirsbXmNLeH4XMOv-gbyUjs3YZK9Iv2b2tE6Zlvi7KSnnr3OCv-TMpzhbnezwwgTT6bAQzYy7D0xpjQuuGiVH-3P8A5MOVIekuOJ_lRZ_8jZSmlCCZ9sn2d3Yh-UwRCdlWuhCWVWl40c1QjlsC5iLz8SLJ3Qm6BFkXURZP7WC9uLZvsLWttZLNt5roGCIOSpSuNPeIvOrushkk59w16_w_wtW3SxkDdiKGBTizxWjXo3l2oQ1LnMFbUTyV6pPbLVFy1Vnru7cAMvj_jG2gaSe4jDt3lX-u_8vYvxhKnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNZ4wO-MdAJO7NfhTSIyFqfRmu3i5V0_5izR8PT6qRCdjHLVXM_tH5NuvaufTnck4J88wR0xYIccTb31bk49IAdjXE-mxOqnVnqvTw0foBmYSkW6ZzNWPPoygX-ISSftif3AcJA7wDHc8qSWL-YpcH3o6ijYxDq6ezfWYIVOc94Nuvxx-sHnZ6yB7Wl3AsKXb14tdTENT9P_mXNKe4v-gxgph2rfMvGucOZxLFrrJFchOSgIFqL0jkD-SXNsGIKuyUpBxa3l-NVbepHwqh7uyDtYQanMfXzUBtx7exTEqn257HUAYPdEXSvr7quaGx7etd7_g_6smp-ssA_Gzm78HA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: بر جاده‌های آبی سرخ
🖋
نویسنده: نادر ابراهیمی
🔹
کتابی تاریخی داستانی که روایتی است شاعرانه از اراده، مقاومت و هویت ایرانی. این کتاب روایتگر زندگی میرمهنا قهرمانی گمنام است که استعمار کوشید او را «دزد دریایی» بنامد؛ اما مدافع شجاع ایران و خلیج فارس…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/659402" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659401">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
۳ شکار امروز پهپادهای حزب‌الله
حزب‌الله:
🔹
یک نیروی ارتش رژیم صهیونی، یک تانک مرکاوا و یک خودروی زرهی امروز در جنوب لبنان هدف پهپادهای انتحاری قرار گرفتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/659401" target="_blank">📅 20:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659400">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
عطر سیب این روزها در میدان آیینی امام حسین(ع) جریان دارد...
🔹
بیست‌وچهارمین رویداد فرهنگی «عطر سیب» با حضور هیئات مذهبی، خادمان اهل‌بیت(ع) و عاشقان سیدالشهدا(ع) در حال برگزاری است؛ رویدادی که هر سال، تهران را برای استقبال از محرم آماده می‌کند.
🔹
اگر هنوز به عطر سیب سر نزده‌اید، فرصت باقی است...
🏴
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/659400" target="_blank">📅 20:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659399">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9NYS1TsPczvO-pX2JaT_2kpVcFO__aA2cHqv4dn_BmIx4jPC-mbXYk7TYHruh4PAWChfe0g-SdSmqcq2ns74s_8G_d3Bu_QjYIUF96BPEaCrbWgQtWzcL_3I0n59Aj3uZYFZAAXvs91zom9u5HuVYowz42U8YbqW8ShpcMk5Pvf2AM5XHJzVSqrW9rE1DBR_mPEvCyTq6mKHraeae4pSgvhHasQepm-LIats3RiwRwypMyZGwfb3mH4KlaxLk-Q5bbLnn8wTTxX6nkYFMGehjqbe1gpU6b9Je7cLW9MCU8DX5nsbc84sfo2KcHGpqvjwCImZMG8aEAcIdQtG1ZnQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیگ ملت‌های والیبال/ کامبک کامل نشد/ شکست شاگردان پیاتزا مقابل بلژیک
🔹
ایران
2️⃣
➖
3️⃣
بلژیک
🇮🇷
۲۳|۲۲|۲۵|۲۵|۱۱
🇧🇪
۲۵|۲۵|۲۳|۱۷|۱۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/659399" target="_blank">📅 20:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659398">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQk1Fmphld7IaXDqXleTmRBxRS0hrCD82GC4l6KEI4bB15z3lF-880__uf-iF_v6QYadsFOz4ciZwgfLtc2T-uel8_nNT2YQ2Q_pnFhS6uodO_Bz8Reab_7UrhWIGazLXNpD_ESDUXQj14WgB42eLQxFQjB5MZ8f-pClwp8wI3jY96v9NHnHLccJUOvg4emYFcfa7OqCIVtv9tas0_b5zbC0AiR4ahs3axkdDzBKEtbF4yQfWZ3N6erHKVd_6ay2YqC6LoGMJU0EVuNpB6RInRpiQ2oVYTW4oHImbUulYT4jJki61eiBcKOovE8tUnVy_BNeG1BZW5YEUuYMDza2Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پنل تخصصی همایش «نقطه تصمیم» چه گذشت؟
🔹
فعالان اقتصاد دیجیتال در پنل تخصصی همایش «نقطه تصمیم» مهم‌ترین چالش امروز کسب‌وکارها را «عدم قطعیت» عنوان کردند.
🔹
دانیال احمدزاده، مدیرعامل ایران‌سرور، عدم قطعیت را بزرگ‌ترین چالش کسب‌وکارها دانست و بر اهمیت یادگیری…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/659398" target="_blank">📅 20:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659396">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ترامپ: از ایران درخواست کردم به حمله اسرائیل به بیروت پاسخ ندهد  رییس دولت تروریستی آمریکا:
🔹
من از ایران درخواست کردم با حمله موشکی به حمله اسرائیل به بیروت پاسخ ندهد.
🔹
به نتانیاهو گفتم که هیچ حمله دیگری به لبنان انجام ندهد چون این اقدام توافق با ایران را…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/659396" target="_blank">📅 19:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659395">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
تا دقایقی دیگر پیام مهم فرمانده قرارگاه مرکزی خاتم‌الانبیا (ص) منتشر می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/659395" target="_blank">📅 19:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659394">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ترامپ: به نتانیاهو زنگ زدم و گفتم: «تو چه غلطی داری می‌کنی؟»  ترامپ:
🔹
به نتانیاهو گفتم حملات دیگری به حزب‌الله نکن.
🔹
چرا نتانیاهو باید چنین حمله مزخرفی را انجام می‌داد؟ من خیلی عصبانی شدم. بهش فهموندم. او اصلاً قضاوت درستی نداره. من این رو بهش گفتم/ انتخاب…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/659394" target="_blank">📅 19:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659393">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
مطالبه ملی از قوه قضاییه و دستگاه دیپلماسی برای پیگیری حقوقی ترور رهبر شهید انقلاب
🔹
امروز مطالبه خیابان‌ها نسبت به ترور رهبر شهید انقلاب، فراتر از محکومیت سیاسی این جنایت، معطوف به پیگیری حقوقی آن در مجامع بین‌المللی است.
🔹
افکار عمومی و گزارش‌های رسانه‌ای نشان می‌دهد که مطالبات گسترده‌ای برای ورود جدی نهادهای حقوقی و بین‌المللی به این پرونده شکل گرفته است.
🔹
در چارچوب حقوق بین‌الملل، ترور رهبران سیاسی و دینی کشورها نقض آشکار اصول حاکمیت ملی و قواعد بنیادین روابط بین‌الملل محسوب می‌شود و کنوانسیون چهارم ژنو، پروتکل الحاقی اول، قواعد مندرج در اساسنامه رم و همچنین بند ۴ ماده ۲ منشور ملل متحد، چنین اقداماتی را مغایر حقوق بین‌الملل می‌دانند.
🔹
امروز خیابان از نهادهای بین‌المللی می‌خواهد که در برابر این جنایت سکوت نکنند؛ چرا که بی‌عملی در این پرونده می‌تواند به عادی‌سازی تروریسم دولتی و گسترش چنین اقدامات خطرناکی در جهان منجر شود.
#WillPayThePrice
#تقاص_خواهید_داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/659393" target="_blank">📅 19:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659392">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ترامپ: به نتانیاهو زنگ زدم و گفتم: «تو چه غلطی داری می‌کنی
؟»
ترامپ:
🔹
به نتانیاهو گفتم حملات دیگری به حزب‌الله نکن.
🔹
چرا نتانیاهو باید چنین حمله مزخرفی را انجام می‌داد؟ من خیلی عصبانی شدم. بهش فهموندم. او اصلاً قضاوت درستی نداره. من این رو بهش گفتم/ انتخاب
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/659392" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659391">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
مدیرکل تأمین اجتماعی یزد: منابع مالی کافی برای پرداخت حقوق خردادماه با احکام جدید فراهم نشده است
🔹
حسن زارع، مدیرکل تأمین اجتماعی استان یزد از صدور احکام افزایش حقوق سال ۱۴۰۵ بازنشستگان خبر داد.
🔹
وی افزود: با توجه به شرایط وصول حق بیمه توسط سازمان، تا این لحظه منابع مالی کافی برای پرداخت حقوق خردادماه بر اساس احکام جدید افزایش حقوق فراهم نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/659391" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659390">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gw6tmP271sMuI524TP3kytBgHF3_3VCVILRu4M1B-8byXm8ksr4_H-7jfc-nbGr5oaifBhVLucw-1hH7aplQbCjD5R_dTSg3Ic3CElxomxrTZtbBpE5VpMbNsUMrmzb9uugfRs7QiVKxolgtm6WQF15QHipIbP8biKBDHm5FDdFrnjCEqn2fabj_3WzSmH9n5xeWPQGMTYWn3zKxliOCLjFgIr-Taix-nhA4qjrjXkrtxxqCQ9BKcqv32ewnpOCsFt0bAzvXUwm46yp55mkIGirKxx00Eilg7vl1MSpmtXalbnKn2oa_nFpdJIJAjkxBy6JB2N9P_MkWBK5Nq4CEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنچه تا امروز در جام جهانی ۲۰۲۶ گذشت
🔸
جام جهانی ۲۰۲۶ از ۲۱ خرداد ۱۴۰۵ با میزبانی مشترک مکزیک، آمریکا و کانادا رسماً آغاز شد.
🔸
این دوره با حضور ۴۸ تیم و میزبانی مشترک آمریکا، کانادا و مکزیک، پر از شگفتی و بازی‌های فشرده دنبال می‌شود.
@amarfact</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/659390" target="_blank">📅 19:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659389">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
گفت‌وگوی تلفنی پوتین و ترامپ درباره ایران
🔹
ترامپ به پوتین گفته است که توافق بین ایران و آمریکا بسیار نزدیک بوده و ممکن است امروز اعلام شود.
🔹
پوتین نیز از مهار شدن درگیری بین ایران و آمریکا که می‌توانست کل منطقه را شعله‌ور کند، ابراز رضایت کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659389" target="_blank">📅 19:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659388">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca4a065afe.mp4?token=oYHMvTMiu__6c0pj-LBhf-VTMPQO9OMQ9iCaPTA3b_ZKqVOoGliu04Tn3ZTmSHAQ-Jrjcc2UZZgotfB6xes7nyVdE2BGomdcFyvKOz1Yxm0wHqIGO0Vr9zjDy9qzpFT5VTkHpJQMbl3RiCC0FMljanDT8cucnFXVGJ_2sm4wYDGscgMxaK_G5Yhh0MX3kmyVDJL0funRMIjDYBxQOaueeHO58-rYWTci_YAl98FvKBOAsUC1vUkOkrztiZG9YXxV89o48w0_l4ctmGetMQDRm-YZuovhBBHTM4U7FGtr8CBCF5UxR76vE-Qu0vGR11JRas2yZ4qZXMpadBcnubXofQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca4a065afe.mp4?token=oYHMvTMiu__6c0pj-LBhf-VTMPQO9OMQ9iCaPTA3b_ZKqVOoGliu04Tn3ZTmSHAQ-Jrjcc2UZZgotfB6xes7nyVdE2BGomdcFyvKOz1Yxm0wHqIGO0Vr9zjDy9qzpFT5VTkHpJQMbl3RiCC0FMljanDT8cucnFXVGJ_2sm4wYDGscgMxaK_G5Yhh0MX3kmyVDJL0funRMIjDYBxQOaueeHO58-rYWTci_YAl98FvKBOAsUC1vUkOkrztiZG9YXxV89o48w0_l4ctmGetMQDRm-YZuovhBBHTM4U7FGtr8CBCF5UxR76vE-Qu0vGR11JRas2yZ4qZXMpadBcnubXofQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آچمز شدن وزیر جنگ آمریکا در یک گفتگوی تلویزیونی
🔹
«پیت هگست»، وزیر جنگ دولت تروریستی آمریکا در گفتگو با شبکه سی‌بی‌اس مدعی شد آمریکا در تمام این مدت بر تنگه‌ هرمز کنترل داشته‌ است.
🔹
مجری برنامه در پاسخ به این ادعا او را به چالش کشید و گفت: «اگر چنین است…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659388" target="_blank">📅 19:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659386">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بازارها چند درصد روی صعود ایران شرط بستند؟
🔹
همزمان با آغاز رقابت‌های جام‌جهانی بازار پیش‌بینی‌ها و شرط‌بندی‌ها روی تیم‌های صعود کننده داغ شده!
🔹
حالا ایران طبق این شرط‌بندی‌ها چقدر شانس صعود دارد؟ در این ویدئو بررسی کرده‌ایم
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659386" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659385">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
پزشکیان: عبور موفق از این شرایط نیازمند همراهی مردم و مشارکت عمومی در اصلاح الگوی مصرف است
🔹
با وجود ناترازی‌ها و آسیب‌های واردشده به زیرساخت‌های انرژی، دستگاه‌های مسئول تاکنون شرایط را مدیریت کرده‌اند و با مشارکت مردم، بخش تولید، صنعت و خانوارها با مشکل…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659385" target="_blank">📅 19:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659383">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‌
♦️
پزشکیان: مردمی که در بیش از ۱۰۰ روز گذشته و در سخت‌ترین شرایط از کشور و نظام حمایت کردند، اگر با تورم و مشکلات اقتصادی پی‌درپی مواجه باشند ممکن است دلسرد و ناراضی شوند
🔹
دولت خود را موظف می‌داند تمام توان خود را برای بهبود شرایط زندگی آنان به کار گیرد.…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659383" target="_blank">📅 19:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659382">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‌
♦️
پزشکیان: مذاکره به معنای چشم‌پوشی از اصول نیست و جمهوری اسلامی ایران در برابر هیچ‌گونه زورگویی و فشار غیرقانونی سر تسلیم فرود نخواهد آورد
🔹
مذاکرات تنها یکی از ابزارهای تأمین منافع ملی است. دولت همزمان مسیرهای مختلفی را برای تقویت اقتصاد و ارتقای جایگاه…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/659382" target="_blank">📅 19:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659381">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVEFxPykYGRdiBB52kbXcEjeS9OqLgrzyu0AyUO0oc9J59C9NTLUQxbmYr8r6iCs3_W1glsQ906rPwqhzXO2Pr_m5SD8WMNJqPigIKLRTCk74Y8oQ_OexN0Z_glXRz3-13cmPfbQ8DvygwsNWS1-y2TV-VAKstMhsaMamKV1vsEmB_KY9IIcdWogNcbQ6Yf15jWiWkNy_ozZBRSDXy-1Jfzz8oVRKTl2SDSLgOWieeHni2Ar61SwjGulGEBIzfCf55ZT01jaLqSpzN7IvOhHgBNMruyVC8d8Eq1vt1om_5gN-eReXtTU4UMJTTIG5S_cs-9hZRy2OlNncgCMZ_2d9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پنل تخصصی همایش «نقطه تصمیم» چه گذشت؟
🔹
فعالان اقتصاد دیجیتال در پنل تخصصی همایش «نقطه تصمیم» مهم‌ترین چالش امروز کسب‌وکارها را «عدم قطعیت» عنوان کردند.
🔹
دانیال احمدزاده، مدیرعامل ایران‌سرور، عدم قطعیت را بزرگ‌ترین چالش کسب‌وکارها دانست و بر اهمیت یادگیری مداوم برای بقا در اقتصاد دیجیتال تأکید کرد. یوسف مذهب، مدیرعامل آموت، سیستم‌سازی را راهی برای عبور از بحران‌ها و ارائه خدمات باکیفیت عنوان کرد.
🔹
زهرا مکرمی، مدیرعامل کیف پول من، گفت این مجموعه در شش ماه گذشته تمرکز خود را بر پایداری سیستم‌ها گذاشته و معتقد است باید از دل تهدیدها فرصت ساخت.
🔹
امیرعلی نجومی، مدیر روابط عمومی سپهران، نیز با اشاره به توقف توسعه در بسیاری از کسب‌وکارها برای حفظ بقا، از تأثیر رشد هوش مصنوعی بر کاهش برخی فرصت‌های شغلی سخن گفت.
🔹
صادق شریعتی، مدیرعامل اقامت ۲۴، حفظ نیروی انسانی را مهم‌ترین دستاورد ماه‌های اخیر دانست و گفت صنعت گردشگری با هر بحران بیشترین آسیب را می‌بیند.
🔹
وحید ابراهیمی، مدیرعامل گروه دایان، نیز تأکید کرد حفظ سرمایه انسانی در دوران بحران، کلید موفقیت در دوره پسابحران است.
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/659381" target="_blank">📅 19:26 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
