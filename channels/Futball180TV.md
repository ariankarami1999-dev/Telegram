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
<img src="https://cdn5.telesco.pe/file/OZ0kO7YCOaPhZVJM_qAYITFKP-GQ9UlfiMZcIVc_7r0_QuK1_2pIqB99mHEcVlFPCmFIXPEloULgymVVa238xJETU1OrUXKYP13cGRcqu23592m5HkSwGE7x3IMWhoRoy8TJqSSae24QcxJ2dSX6rK2-BG6ZIPZOUEf4A9edlz-ju4KUTkydvvuFEgeskiETUcQYAoloZhWz-f6lKruLI04oU6SFSQassomQRIMXDwrv5B-wTg5o16Y8WdU7HLSUqTWTxw_Wwuj9YvgVR-sdR3pvVIwuwNSnEMPtApcomS4RdFDD7gGVCwpNreLjj8WGu9aoiUSJY5YOQI5UxSsWuA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 313K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 10:30:37</div>
<hr>

<div class="tg-post" id="msg-91806">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t44DSadR-AQJ-VxLWQGSLrIJTpWMEtVmx3zncl88TLg0_SxGJ2pyd9Exa4Rihdoz0etH4SFdjbacTaXeC8Cs8tYbNVVQM-GfFtMBOeWDvV7UJEoQeOL0An7GuowoyMQsIL1J0ZL0MklQV6Gsk9LjhNxnlGCj4DYOMD80CP35vh4qu3dZjiMUyGDZG1greCbDtUL9V7BFPOU3_7cwsbZWkn7gNCb4Xlas2IKE4AnPlkcq4BrmpBOJv3KitIASBtmuEKNu15glFEzE72sjKEK1_RdJRKzdHjtQLTIAE80FMmuEre_AiROwv46_Xo6-M2fW6AS64bErQrf0Mp6IE1u_Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی با 38 سال و 11 ماه و 14 روز مسن ترین بازیکن تاریخ تیم ملی آرژانتین شد
🔥
او رکوردی را که از سال 1957 در اختیار آنجل لابرونا بود که در 38 سال و 9 ماه و 8 روز به برزیل گلزنی کرد، پشت سر گذاشت.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/Futball180TV/91806" target="_blank">📅 10:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91804">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNs3vYATSGbT4PRwMBYWsaIKNxL-ZN5Iv37GRFm7IlTS6J7YVgEAmm9KZ_xTA9JyhLrFTrlJlG6_j5cSI0uqUiwkRtjRzoSGoLKahhgTMNAFmzARI3o1N557ftMn55Mk-8rmjnWr_y_Frs-zpowWYs5tGG8zMyUbMBkt9k9D4p3qcxZFCF68yJfcgwajXY00lq9BAWApGKYconpkPISBzMDHfbO_2cQFhOHPtymSI8NzXpcihRqLaY2Tihuy13UGR_57AqljZg62lYArZjJF7WZYHf5w7medSDykAnLwaIcNyqc7N1MQ-V4SXMOeJJ6Vwh2jm3pOMuwz2h_gjOu7bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TUYgEpXj9UvceXEIrBIkc7LVQc6IvcbhGJqSAzkd5lUF7enoeRk5lTRjSoaguMJXDsqh-vnYZWS_LrW-V-IC2zFhr--ZIwlLGfmTrfPMVkN_GYXP-rhmzF8jKxsPKwDH6wOvyYBYRuk5MzZLFzOmHtyZtdALSrmpepWbyZDra8js723XRri2bJ2Z5LsKi_4zWaOWFRm6-jNGX3zKxciqZAnht7OJrCHsFiNS4_AOUWUpB_XFR8pASd9e0K6OzBpCSrYWIK-rnpKzubqfCyKjWvOTCY8h1BxQMtF8GxZFZc5yGqAUU9wlrxXIhxA1wGhi3m-Ko5Lo3ACF2x5nivt94g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
خامس رودریگز:
🔺
وقتی به قطر رفتم، پول فوق‌العاده‌ زیادی به من دادند اما زندگی خصوصی‌ام کاملاً به کابوس تبدیل شد. فرهنگ آنجا آنقدر متفاوت بود که نتوانستم خودم را وفق دهم.
🔺
با دست غذا میخوردند و به من هم می‌گفتند «بیا، تو هم با دست بخور». در آنجا دوش گرفتنِ کاملا لخت ممنوع بود و این موضوع من را خیلی عقب می‌انداخت. میلیون‌ها دلار داشتم، بهترین ماشین‌ها زیر پایم بود اما تنها در خانه مینشستم و گریه می‌کردم.
🔺
شهرت و پول از بیرون عالی به نظر می‌رسد اما وقتی تو را در جایی که به آن تعلق نداری کاملاً تنها می‌گذارد، آن پول هیچ ارزشی ندارد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/91804" target="_blank">📅 10:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91802">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bI6g9RBNo6y8E1n-EM3jc1jIGAfhZpydQLSSlFoi7Nelg5yJtn7NdAyqb7CrxDofMl0pnojpuywKZLnqv7oA_hp-m8PPnY1qVEcGQ9GGBBCWFOi24tlG2CHauv10eijQm9pjCxq5uc_-MoP6mURF2tfghkM8afuaCMx1SbhIiWrmWxGyezfNndpst5zYwkCzyJtFgJPFrdpLGKAm_j2tEHi9BYi-6Cm9Lb6U4Hwmr_ejEPK0i2vRqhR9y6YzOK-klv08V5Y1vvjrNliyJNOFKbirVRsmcOgRGBjwAr1IEXn-a4keccLee_yoV-mBg1NFfPMABY70F7Q3a_taQPccpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XfFHjpodc-uVxfY81xYMPMCOtkzBYfglLGoPGet9j8QjvN1mMWtXSz7I4z4qcH3YQLNs-2C6M6lOg5b1CbUtGLB5UPdri-pP_ByY5XrE_Ya1ZEChzVs7Gh3xoFmK7S79j8IAuyWJ3KRyC_-sfPMbLSfPk4wLr0-zrnVGB6wrPzp8qbdT9j0_0dk8qAEDODfWz94V8QE3QJKxQczrhFV2JLq0ZVvumoDMXUXMASA7vx2OTfF10fCQ_4icVUvHgmOUFmdgYYN_n_dfOHIelfcHsfwiayJGPd67Ednk9cjX0enqasWIEMUyW_IAHlEiY0YF3-KI03bMQWeJDnd5UIyXSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
🏆
-
ورزشگاه سیاتل (Seattle Stadium):
مکان: سیاتل، ایالت واشنگتن
🇺🇸
افتتاح: سال 2002
ظرفیت: حدود 69 هزار نفر
🗣
پر سر و صدا ترین ورزشگاه به دلیل طراحی سقف که صداهای تماشاگران را در داخل ورزشگاه محبوس می‌کند.
🔻
برنامه‌ریزی شده بود تا میزبان بازی‌های بزرگ مانند مسابقات جام جهانی باشد.
🔺
6 بازی را در جام جهانی میزبانی خواهد کرد (۴ بازی در مرحله گروهی + مرحله یک‌شانزدهم نهایی + مرحله یک‌هشتم نهایی).
🔹
مهم‌ترین بازی‌هایی که میزبانی خواهد کرد:
🇪🇬
مصر × ایران
🇮🇷
🇧🇦
بوسنی و هرزگوین × قطر
🇶🇦
😀
بلژیک × مصر
🇪🇬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/Futball180TV/91802" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91801">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a3bc142ec.mp4?token=GI7usFfn5IiS6U_PMOdvgyHpltNCx7I_vVFyujsPM0rJEspy65nEU_kcqotZmhxWnDbaYkxXzENQ8oMBkTV4q_cMWGRcSbXqJzHqzC-x-Z-pwsXfD2KvEBU6zpTcVB73q1U5cjr3I828-qQKgmMknF3VnH1x77SoR96TAj8N3QIgm1_FQM7snaxxyTARpaJ0_em5-UR_UtjmHaNQv6F6Je8YtkuwHAEcC9j3ANoHdQzJU3aGbfyY-5VQ7fLFegeaEhklvOvEsRLKrrD5c_GcJkPhNpZxvDXtJcPDAHz_S_55rLwzrqoKCEVwn3zwsTQhEZ01G6CgPi0NRKD4rR1Rzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a3bc142ec.mp4?token=GI7usFfn5IiS6U_PMOdvgyHpltNCx7I_vVFyujsPM0rJEspy65nEU_kcqotZmhxWnDbaYkxXzENQ8oMBkTV4q_cMWGRcSbXqJzHqzC-x-Z-pwsXfD2KvEBU6zpTcVB73q1U5cjr3I828-qQKgmMknF3VnH1x77SoR96TAj8N3QIgm1_FQM7snaxxyTARpaJ0_em5-UR_UtjmHaNQv6F6Je8YtkuwHAEcC9j3ANoHdQzJU3aGbfyY-5VQ7fLFegeaEhklvOvEsRLKrrD5c_GcJkPhNpZxvDXtJcPDAHz_S_55rLwzrqoKCEVwn3zwsTQhEZ01G6CgPi0NRKD4rR1Rzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
گل‌دیشب لیونل‌مسی از این زاویه جذاب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/Futball180TV/91801" target="_blank">📅 09:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91799">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzkbkr-8-Z_nO_tAX3PZLdx2fSuikVV1eEmMRXrYc_dtgdCc6JDj6uY_YXMYhXYpRlv9Cz9TfpZamur0AKr3cw4STZAa8xbznzyCyUR4fiFo7x9O3qvKpls7Eus1ESzRTDhRq-SAOrCThIyDIypxsFax5v4oa7IqC4Dol1dsQDC-c-Ahbvp6WgV1CgwiVvUNwSumIoeKHsM-9HvCydln7GgMNs_X5XvM1imxwCm0mzydJdLOj0WXoAVpLCrmgr4uycYYzDQygwZfsj-Ibd8-R6dqkArGRk50rWlcDtqgn_-VofpITeRDGToc4ahubkL2RgMDUpTseQpJIqNpmroMuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CNfoW9Zgow4uHvK5qsf5M2p9wa0t1F1ojkjeoWDPiS4cdNfaSzjPxE1qNofXqRjseWqP3_0520zz88EnXpbBm48b1d1ZB5gJXbmqYnwIeYG5HJu7M59ha4cWmmrA-DJtdjytYp3-pAu9B2KfBvwnn6ocbY156rhG7fGFQ9_lduDJEZGGG1N_t4ZQoOCjLS2qbja5N4DM66c9lpucGaa3dy49M4X29jXmZxUMOrHBLcXjRtsnuxfOyMYZffaKsPyGGQ_fLVjFlWOW9V-QkeLFSZ4-v8MNVp_sVFYDcVkl7NCLY3mE5cEkI_KBCEV1yRCIM8YK6AxmklCoPUafYSyiTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سوفی رین مدل معروف اونلی فنز: هر کس تو جام‌جهانی آقای گل بشه یه شب میتونه با من بخوابه‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/91799" target="_blank">📅 09:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91798">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFlEsmiUiDFqYtzPc0_qEFqHowH8JXBrgr76zUfEM1QR_JQSFqzMbPslhyEonfwBHM91KeBrexf0nQs1FJVxdCrgaKRY4HM9PXhdcPqJM0Euos_btLukY4LaSPd6yBQIommuVAkKCZN7APiqyR1I5_cwrBDWyE7OlCOIq6InNnjnFD1SvDQ9_GvrAbfFfpO2kWdLJtBbaKUxUo95uFXab7ABCcKYATaGSnovX9dgPBGRjPyRLxeQK8XPZFXqEVSvqME1e41ys7k2WtMMP9ve4w9uKoW9qDqRXO_BHZv1t2BPy_QH3QLOeV0bWIPLp4GxXPo32NB0DBfs776Y6PimTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
در ادامه بازگشت سلیبریدی‌های بی‌خاصیت، دیشب پیام صادقیان هم بعد کلی کسکلک بازی در ترکیه و کارای عجیبش به ایران برگشته و در تجمعات شبانه حاضر شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/Futball180TV/91798" target="_blank">📅 09:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91797">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
سپاه در جواب حمله دیشب آمریکا؛ حداقل چهار موشک بالستیک ایرانی به سمت پایگاه‌های نظامی آمریکا در بحرین، کویت و اردن شلیک کرد. ولی خب همچنان آتش بس برقراره و مشکلی نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/Futball180TV/91797" target="_blank">📅 09:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91796">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HApsA2FcExXZprFLy8nZMhW5pZ_CTqAhksu265ycaH87cYYCM06P-8YJHKA1sV7BdZAXwYpb6vGvL7KrYFPufRaDSCz7Zwp_riuEl3FfM9ZFS_ifT6oRrC5kjl4W5GGmAYcwNo__011AULVUT17gDOhcBh3a1ULVZ73EqKv7bVXjELUYuHF6TAtXGUYVgTGBOba-pPMoHIufaoB4Q7cURNgKPeUYosBOvwl7lZJRUxoqe4NhanecuIlKDFOd0Bw0KrFNexTlyoUjVwnJlsEqBKUMdkgx4cghqjN6EWNWs2_V5Zqvy8YmQWTNRlWAf9OyvkYADDehyJoLq_zcVo9Tvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رودریگو دی پائول: میخواهیم با جام قهرمانی به کشورمان برگردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/Futball180TV/91796" target="_blank">📅 08:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91795">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIbLa1Sqc9MaNuou7qwEBxLIiD7-SnSRvn0NwmrVLM35-Knj1It0qg96xnN1T11NAG2NnP6GNiqDCLvWFWjjxDIIUkGcXUC8ECejfWBnbmauTMyZpgaVgc840v73HRd3vpGlWa8Qn495FpZ11QLW2ai1hE710zF_9b5VW4jzburB0lTJghPRrBrOgdufg2kZAlVT2ytO4NngKd9lbEdYEalOH9pT_4rQv0VqgSLKbeiiZ_QWjHKpfezMpueq40kq-XhmSv3q-Xpr4wS_EIHWrOtnVv1WiszN3hRS2W7EUnB_ajfcLoe1kX67a1LFPX4U1OA82ulbSEQfDWZwGZ96CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی با 38 سال و 11 ماه و 14 روز مسن ترین بازیکن تاریخ تیم ملی آرژانتین شد
🔥
او رکوردی را که از سال 1957 در اختیار آنجل لابرونا بود که در 38 سال و 9 ماه و 8 روز به برزیل گلزنی کرد، پشت سر گذاشت.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/Futball180TV/91795" target="_blank">📅 08:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91794">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=P2m7nFfGXuTOd1N09Dc2O9MEGlb_PW7Vxm-sT5aHoO4j9LyFFWZnqxrVfMeSx9dzYrrTE9BEo-He2jdaGmA3epPrYdAFdCN0a8NEL3ZldjcK3oeDPxCX9Q4J7PQB8KOp6Uf86lH5voQQcCeJcPuKnXJjsVJpCAGaH2o87VGWgtw3VkTufv4nWje0CqBnCb--Hy__9WDg3xtsbh4tTS8A6yq0JOXtJg8IDymfoQkDjrZhLdepFu92n7sAOD9E2r8KTURHvDlwnYErP3J_EYDnulvpwfkTdfAeRr6YreUBCOGb6vCpLZt_1JzSuxKjzpfHvfwn0HFnVDEGXGtiEnOHXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=P2m7nFfGXuTOd1N09Dc2O9MEGlb_PW7Vxm-sT5aHoO4j9LyFFWZnqxrVfMeSx9dzYrrTE9BEo-He2jdaGmA3epPrYdAFdCN0a8NEL3ZldjcK3oeDPxCX9Q4J7PQB8KOp6Uf86lH5voQQcCeJcPuKnXJjsVJpCAGaH2o87VGWgtw3VkTufv4nWje0CqBnCb--Hy__9WDg3xtsbh4tTS8A6yq0JOXtJg8IDymfoQkDjrZhLdepFu92n7sAOD9E2r8KTURHvDlwnYErP3J_EYDnulvpwfkTdfAeRr6YreUBCOGb6vCpLZt_1JzSuxKjzpfHvfwn0HFnVDEGXGtiEnOHXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گلزنی مسی در بازی دوستانه بامداد امروز مقابل ایسلند که با نتیجه 3_0 به سود آرژانتین به پایان رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/91794" target="_blank">📅 08:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91793">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcNhc3zaD8BH1mYmSdi7ET641-cRB6fJaoHOZxBweoBEbKPjeteh2wu3bJwlooMvbFedzZ0IZQNOsKK6WrxsQMSi6ptgMuSzE2nZvi-405kYVjpPifLzey34lU6NZkriFA8hy342HKRe8M9_s3OnZ5EFgecvAZtqI1GZGeDRYZC5opAdocALcdy936jvl4poIk_LImEchgNNw0qjchBtJ52qbr65LVxq2Hj0sdJIBJv0sMNcf1Xp05fjvYCYpgDQY3Uj9yWM2aqdFT5Hak6L6pa8ZmLk-QE-Bq_GARjRqkyTh3o6F8Cl4VVUZEnCIo06GYzdKxuiQY1k0o--xo_95A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرزو رئیس اتلتیکو مادرید:
کون خودتونم پاره کنید آلوارز فروشی نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91793" target="_blank">📅 03:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91792">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07800c01b2.mp4?token=sId5HnOVrV5gaX9Li5an-Pa25ree7rvbh_obIMEfBMWfhwgvCa7WZuvB-8sBNwSBtEV8t4JxPad_rDwBfim50ZdcJsQKtB8_Ob7PPM1unRydBNIrPRcBNDd3_jKqMotsa3hgpWRNlQn2gr6tdb66d9jYJQdHUtskwLWVfjbnBtk_zj0BNGPp0PmyQHDgWXoIyMHta5zeZoigicuK_kIHoB9d0MyLLkG88-iGkqR4BJlrPBR2n4CBkh67ixESYAhVmD6oq8Ei533csrSFxv8YQLo7-C9fHgZZgFvOIDPhh-dwCPXtzxW5I-CqmMgUMLJIlWvlokmhV1ajSXgOAl3seQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07800c01b2.mp4?token=sId5HnOVrV5gaX9Li5an-Pa25ree7rvbh_obIMEfBMWfhwgvCa7WZuvB-8sBNwSBtEV8t4JxPad_rDwBfim50ZdcJsQKtB8_Ob7PPM1unRydBNIrPRcBNDd3_jKqMotsa3hgpWRNlQn2gr6tdb66d9jYJQdHUtskwLWVfjbnBtk_zj0BNGPp0PmyQHDgWXoIyMHta5zeZoigicuK_kIHoB9d0MyLLkG88-iGkqR4BJlrPBR2n4CBkh67ixESYAhVmD6oq8Ei533csrSFxv8YQLo7-C9fHgZZgFvOIDPhh-dwCPXtzxW5I-CqmMgUMLJIlWvlokmhV1ajSXgOAl3seQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که بغض تتلو بعد تقریبا 3 سال حبس، پشت میله‌های زندان و درحال خوندن آهنگ شکست
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91792" target="_blank">📅 02:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91791">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RL2aw8x8lrb558ZDsPZ2hf8019L22srCnQbI34vRm_aX_aAKfBHuFmV3pVM-2IoI1l8S5VAHzT8SZDLvd1atvuQQa9Twh8K89myuR1FLHSotINc_WXalkZLIiSoZARQ86V34qttNIXbj3s4QpKfS_Hs5nyRXWnj17QHfxRn9ayXjhlgJ76u1lbpHdTC9Yeey-SyxuYY3xmfqIrzA-dSIbaDTnZmyc5LBGtqCgc3nuyQTz_CUhsAt1VGaJVMCAqpmj6CMrpdXidsrG4D_5_g8YY6usjVdhZJOXp8bx8XJx_P5j33gSq_XBrqdOaKcGRqym-q7LUX1VLLSwEFF7avxTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔻
خوزه آلوارز خیلی نزدیک به لاپورتا:
🔻
آلوارز شخصا با یکی از مسئولین رده بالای بارسا تماس گرفته و گفته:
من نه با رئال مادرید مذاکره کرده‌ام و نه قصدی برای مذاکره با آنها دارم و فقط میخواهم برای بارسلونا بازی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/91791" target="_blank">📅 02:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91789">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201d3221ec.mp4?token=lWJP6lsmBOa0Wv9JF8rIZQUO9GbzNhxIhkLbMhLW2l_tR7pkk27SVGhFMD_JpDdZjwpcfzRL3FKKsFgEXHwO42f_SnbQYpcS5vRhXEKgR_NgUng3UkBid8sGLyfzOZu64Lkh8wnjTOn1ufhHLIJ1LoPqSpuVgR6dv1pfvRSdadyDFXzbDKvoIF0m_K4Bliygoc9wb--JxkWfA0v3besF4Sa10De0fTkZ3EDa35DuwPqSBoFK4v1ljGeAQOkbTsA5va9ZmF4n9f13Ody7kWToV1VUtr6O-7zBfOehxe_NlwdPsRA0YoJYGWiHbULz2vQgqYR-Zeh0iq3UJZ6T4QN7nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201d3221ec.mp4?token=lWJP6lsmBOa0Wv9JF8rIZQUO9GbzNhxIhkLbMhLW2l_tR7pkk27SVGhFMD_JpDdZjwpcfzRL3FKKsFgEXHwO42f_SnbQYpcS5vRhXEKgR_NgUng3UkBid8sGLyfzOZu64Lkh8wnjTOn1ufhHLIJ1LoPqSpuVgR6dv1pfvRSdadyDFXzbDKvoIF0m_K4Bliygoc9wb--JxkWfA0v3besF4Sa10De0fTkZ3EDa35DuwPqSBoFK4v1ljGeAQOkbTsA5va9ZmF4n9f13Ody7kWToV1VUtr6O-7zBfOehxe_NlwdPsRA0YoJYGWiHbULz2vQgqYR-Zeh0iq3UJZ6T4QN7nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات دیوانه وار اوکراین به خط لوله گاز اصلی روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/91789" target="_blank">📅 02:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91788">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
وضعیت الان اینجوریه که:  آمریکا داره ایرانو میزنه ایران داره پایگاه های آمریکا رو میزنه پاکستان داره افغانستانو میزنه اسرائیل داره لبنان رو میزنه ترکیه داره عراقو میزنه یمن داره اسرائیل رو میزنه اوکراین هم داره روسیه رو میزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/91788" target="_blank">📅 01:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91787">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
وضعیت الان اینجوریه که:
آمریکا داره ایرانو میزنه
ایران داره پایگاه های آمریکا رو میزنه
پاکستان داره افغانستانو میزنه
اسرائیل داره لبنان رو میزنه
ترکیه داره عراقو میزنه
یمن داره اسرائیل رو میزنه
اوکراین هم داره روسیه رو میزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/91787" target="_blank">📅 01:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91786">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
حملات هوایی پاکستان به پاسگاه مرزی افغانستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/91786" target="_blank">📅 01:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91784">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🇺🇸
آکسیوس: نوبت بازی آمریکا تموم شد و دیگه خبری نیست. حالا منتظریم ایران بازیو از سر بگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/91784" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91783">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🇺🇸
آکسیوس: نوبت بازی آمریکا تموم شد و دیگه خبری نیست. حالا منتظریم ایران بازیو از سر بگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/91783" target="_blank">📅 01:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91782">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
حملات هوایی پاکستان به پاسگاه مرزی افغانستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/91782" target="_blank">📅 01:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91781">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
حملات هوایی پاکستان به پاسگاه مرزی افغانستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/91781" target="_blank">📅 01:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91780">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfUB-1qqEaddmABPm7CIVEiJIB0vZmMRFvz64pB_iTHZ8belA5Hr-7w_1DEyiqJFxQja5sNRRogY8BYSvgrPdzSk_c8kW0SGNb5cIe9BrqQklBwsrhjZ7SK2H6j2gGXBvrjYPxb09q0XGaE3xICJmnpBRGZqGUBNUTbCgU-Y1ZB95m_eg53GOgsOin32YZXq76dMcTMfvHkRMLkf6iEojGQ_GNiGu8Gab8GKYTSK04MAuPlKxi4EQnY5sN4wAdsQfchUQYpzZcHD2wPfeoqpI7GdToQ6AULP9EdaHKF440mb1CDeuCmz-P4Oxm2H2LT-LF9mUKMgsaRPewvZDDS0xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙁
سید مجید خواب بود کی بیدارش کرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/91780" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91779">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
فهرست اولیه اهداف آمریکا در حملات فعلی به ایران:
-پایگاه دریایی سیریک
-پایگاه دریایی جاسک
-موقعیت پدافند هوایی بندرعباس
-موقعیت موشکی ساحلی میناب
-موقعیت موشکی ساحلی قشم
-بندر تجاری قشم
-کوه مبارکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/91779" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91778">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
خاورمیانه امشب تو اوجه : اسرائیل دقایقی پیش به لبنان حمله کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/91778" target="_blank">📅 01:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91777">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یه خبر از آلوارز بریم؟
🙁
🙁
🙁</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/91777" target="_blank">📅 01:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91776">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یه خبر از آلوارز بریم؟
🙁
🙁
🙁</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/91776" target="_blank">📅 01:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91775">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aca6ef1dd.mp4?token=LkWdaWIV8zjO46V-fwcXRs1at2Oui3RxCx47pGUgouTn4W2R0UbN0aCsGD_CGLbQMuU8iJB3OrWJZGJ--HH2EJVMoZL2B3Q35dov4IZDRWGJFfA96YjNI0WR8ujzPYAzwiS-H5cbS3W-RAwiejZSUaniQzbrVB4qf0rPt3zRVUQQ93_vPyo36ZWtZ9SUysmigkmiTM6WZqL2CkjrsZOFkwb1J4eNlxR8mGQlFPppzgysH3Ihd0WCxW3Zx3QELmi_2NObpRMZsAKB2aunsjSUOSGKNcJA2OREhrHDUItmsszWWbbnsHeBjWLTOl-VGIDzd45PALPVoMs0kFzOsXYOZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aca6ef1dd.mp4?token=LkWdaWIV8zjO46V-fwcXRs1at2Oui3RxCx47pGUgouTn4W2R0UbN0aCsGD_CGLbQMuU8iJB3OrWJZGJ--HH2EJVMoZL2B3Q35dov4IZDRWGJFfA96YjNI0WR8ujzPYAzwiS-H5cbS3W-RAwiejZSUaniQzbrVB4qf0rPt3zRVUQQ93_vPyo36ZWtZ9SUysmigkmiTM6WZqL2CkjrsZOFkwb1J4eNlxR8mGQlFPppzgysH3Ihd0WCxW3Zx3QELmi_2NObpRMZsAKB2aunsjSUOSGKNcJA2OREhrHDUItmsszWWbbnsHeBjWLTOl-VGIDzd45PALPVoMs0kFzOsXYOZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی از بحرین و کویت هم‌اکنون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/91775" target="_blank">📅 01:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91774">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
صداوسیما: کشورهای عربی شب بیدار باشن. باهاشون حسابی کار داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91774" target="_blank">📅 01:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91773">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خاورمیانه اونقدر عجیبه بعید نیست نتانیاهو توییت بزنه از آمریکا می‌خوام شلیک رو متوقف کنه و به میز مذاکره برگرده
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/91773" target="_blank">📅 01:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91771">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
حملات شدید به مناطقی از میناب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/91771" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91770">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
ترامپ : فکر می‌کنم پاسخ دادن بسیار مهم است،آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین الان در حال پاسخ دادن هستیم
این پاسخ به کاری است که آن‌ها دیشب با هلیکوپتر ما انجام دادند، من معتقدم پاسخ باید بسیار قوی و قدرتمند باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/91770" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91769">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
سنتکام: در حملات امشب از چندیدن موشک‌کروز استفاده کرده‌ایم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91769" target="_blank">📅 00:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91768">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: آغاز حملات موشکی سپاه بزودی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/91768" target="_blank">📅 00:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91767">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🇺🇸
⭕️
سنتکام: پاسخ دفاعی ما علیه جمهوری اسلامی در مواجهه با سرنگونی بالگرد آپاچی آغاز شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/91767" target="_blank">📅 00:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91766">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🇺🇸
⭕️
سنتکام: پاسخ دفاعی ما علیه جمهوری اسلامی در مواجهه با سرنگونی بالگرد آپاچی آغاز شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/91766" target="_blank">📅 00:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91764">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYBonctKPMc5W3DVznby2R8oL5EPDbB0yQ8oP3BLTNzuAB0R6LAcP9s6ZXNyT2TzpHqM2-GDk5FZRbaQ-OfeaqIYJoQjJIuK99m-HynZJyD2iPu9AfS9z8p50inEHbqEcNGmo1nrUUJdI2FHWe6eErz4zBKPQN5sYxwxu7CrcGHb-L9BFIDDgDQJ_1OajLGc11VQ1WIc3PzKklFuwz0ZcMoEMPS9us96J069fvHyk5FIa3Bvx3FK8h_A2pLsk1FlXWy1pmDZ84S6kYnv-OuhN8EClW1D84qEJ1UbozTj1w3sCwvJk7pPNrbrK6-N2j4azsp7RybiE5zQndzz4xAIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حداقل چهار انفجار بزرگ در بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/91764" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91763">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
💪
بسم‌الله الرحمن الرحیم  گزارشات از انفجارهای شدید در سیریک و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91763" target="_blank">📅 00:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91762">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
💪
بسم‌الله الرحمن الرحیم
گزارشات از انفجارهای شدید در سیریک و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91762" target="_blank">📅 00:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91761">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
پشماممممممم خبرو داشته باشید افسردگی بگیرید
😐
😐
😂
تیم‌ قلعه‌نویی در آخرین بازی تدارکاتی با منتخب شهر تیخوانا مکزیک فردا بازی میکنه
🙁
🙁
🙁
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91761" target="_blank">📅 00:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91760">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
پشماممممممم خبرو داشته باشید افسردگی بگیرید
😐
😐
😂
تیم‌ قلعه‌نویی در آخرین بازی تدارکاتی با منتخب شهر تیخوانا مکزیک فردا بازی میکنه
🙁
🙁
🙁
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/91760" target="_blank">📅 00:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91759">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trQtLmmJfy7prQn3scSMLWyXxpSiI_9T9LwYn8a2nixPEVZ0Po5pw24GLydoqVmWRdeCR0FkXGiRXfNUSN_O-8p9YanX_FTbdI_kUu6b2wBban23L7K-yOKIplnGUYAZPfnFIiFJ_NLs04h3It4o5sBKtNZWSP0ew9mtshAFmZwE8QKXmjgh8q21Vme50PIx00hgwAy3A2hO9deiya7rGVe_vpBBaVzmbzcEeignJpfPnR7jgGcMj8jVsMoS9oBlpcsfXHuCqVaPf9T3EmUuDrRmeqmBT5n3QWO-4K03Z_S1DEHXH3vSyHbRfXd3jLIv9cEFXxtkgw6MnnkDttLoUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
موریگی دومین گلزن برتر فصل لالیگا به فنرباغچه ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/91759" target="_blank">📅 00:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91758">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2XL1LHgyFMv6TBDXv8Gf2E3Pb68A5SNkuZzl-fJKREbZdWj_BSpB9jbcqoyCzL39qg8Yd2KN5nn6mP_hFkKE4Ul3KCIcqOAySJGlj95c3Xlr9aUPUVFBlyV9aPO53GgA_HwiINOtymlwq2vbQLVvDzmHWnW-LlWPZt-0TCPwg9xZc54D7SYJMFLNEVDzBa6v5H3jLR26HUjor9D0mg8G4he81YkfJfWRHR909g7WoxBl4gXDd1XPG4zNn_Bz0hPYXdcniJfT-Kn65oiz65ZMHt0Jda82fcDBzkE39FdkmmRPpK5tQDbAah_2Ftihn47bhGStvNFD7e2sRaxbUotOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🏆
#فکت
؛ هیچ بازیکنی در تاریخ جام‌جهانی به اندازه لیونل‌مسی پنالتی نزده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91758" target="_blank">📅 00:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91757">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1wJEu7gwC_3u96BfIBEItg7muUQesDccbolsqmbcr7TnNivohW0aGfQqdR5CIaldeH1nCjmXEOEg0cAQF1WiEe3JkXFR85vQ03Ol-QeeASBMXCXuR7nepiWTf0Ms8i4Fh5v51BOjq_-j4ATIYv6YK5c5urS3uVKmM_w_PQ1rWUPkuTI-hZkCJTs1RnQuB_PXeagxyJtoVsas5ZCXzO886pFchb6_-3udKns4PuaheJRLbhznuDkCKQlzXzTat4mmL6vlJfFVlXmW4lrY1foBBxqUmDVVFY3DIIWJ-0RV1FNmMlqTR35j_rasLTmtmFOTMbGxbJH_dHNcVuK_Y4-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇳🇬
نیجریه
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
چهارشنبه ساعت ۲۳:۱۵
🏟
ورزشگاه دکتر ماگالهیز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در
۱۰
دیدار اخیر خود،
شش
برد و
سه
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
نیجریه در
۱۰
دیدار اخیر خود،
شش
برد و
چهار
تساوی کسب کرده است.
📈
میانگین گل در
۱۰
دیدار اخیر پرتغال
۳
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نیجریه
۲
.
۶
گل در هر بازی بوده است.
🧠
اگر دنبال جبرانید، یعنی از مسیر تحلیل خارج شده‌اید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91757" target="_blank">📅 00:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91756">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دوست دختر بعدی وینیسیوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/91756" target="_blank">📅 00:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91755">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAhRxgPrhPqWcIeYC6wgqx2jhqi2gS06sULNjdRfzfaVTT9IG8G8NbxqlMdVM8067WL8_bHPr4GoQzhBsD5g8T-0UtVkZkTTKkMTXETZ7XyBT_6rWzYYfegechV1riY3hl4A5-hjeH8zuixpjJX5auyyWPUr4J1ZLd52xicvHKl3MfrySH8ALHWTp4T5LlX5O35NbHOFvtIpoDLHEdxipRoaxOHnDGEC6BtioD7U2V4iKK9ySwKSWRvBL3V1pWNp7zZF0p5VNVeLPAmh8lMFXW-VWeWsUtflNsbGePe4ktGKshnSIq806pcJaAO1y3FVIYlC4HF__G8I5wcdTL6Bfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوست دختر بعدی وینیسیوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/91755" target="_blank">📅 00:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91754">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07e18ed18.mp4?token=pjIx4KbDU0joMWEDNaTdLlYW14M96SZPISJfeiKP3IdEFli2FNfU2plObHa7TUAQ0yVoS7xaBlFNFlB500oTYne-LkG1Wd7aS_f5Vm7ZqTMze_ApmUaujBMvDB1v7P8DYAQ_av5dHWhszxd26jWrQqTUJhZAXGE9m6lZYGoSIMBN2lglBS1S81t3lQZqWP0K4CjY0h1jSAw1ltXmqF8-LJ3rsBEwkk2l0Z5jiN-0GxKDPLySnUxKZQ0PPf-T5oeLaKcjKblmw-wc5fbf_ObDRuO_3GgHn8yAis2_3jTs4iL7Q6Q8zUYo5TZPtDB6NZDQeFRQeYeKEaRS6Jz0ejtEWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07e18ed18.mp4?token=pjIx4KbDU0joMWEDNaTdLlYW14M96SZPISJfeiKP3IdEFli2FNfU2plObHa7TUAQ0yVoS7xaBlFNFlB500oTYne-LkG1Wd7aS_f5Vm7ZqTMze_ApmUaujBMvDB1v7P8DYAQ_av5dHWhszxd26jWrQqTUJhZAXGE9m6lZYGoSIMBN2lglBS1S81t3lQZqWP0K4CjY0h1jSAw1ltXmqF8-LJ3rsBEwkk2l0Z5jiN-0GxKDPLySnUxKZQ0PPf-T5oeLaKcjKblmw-wc5fbf_ObDRuO_3GgHn8yAis2_3jTs4iL7Q6Q8zUYo5TZPtDB6NZDQeFRQeYeKEaRS6Jz0ejtEWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به جام جهانی ۲۰۲۶ هم رسیدیم ولی همچنان با اختلاف رو دست این مصاحبه نمیاد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/91754" target="_blank">📅 00:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91753">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50e12c65af.mp4?token=j620HgrCMBeYc-5igaqk1CkJSFgK105R-axFL0mPadGEHJ6yVgaU2Nibpq_DgGwDj8_YRp7t6cwPovjuQqfJwyD9OG7NuFGbNwpt4L1_EWMMWSYKvThXRU6LMpF5RASFrY-UrxNwqaMD4BlzWln37L527y0kdTqEAGxZ7OjDzpDyh5_C_7tHs33qEIykHQOFWRNO1pBPONobpTKh9ogWTcbQRzqZ5U11HqMjn20cC9dJAr7rgV5ajLV0DUY7Fo3myGy2Bt7Rjxv0VOnYaAxL7587l2o5KOTv3mXja9v4w_PfqRku6cGjJxKbEuAM4gf6zgmcDsHD2JzAyKWS2E6D1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50e12c65af.mp4?token=j620HgrCMBeYc-5igaqk1CkJSFgK105R-axFL0mPadGEHJ6yVgaU2Nibpq_DgGwDj8_YRp7t6cwPovjuQqfJwyD9OG7NuFGbNwpt4L1_EWMMWSYKvThXRU6LMpF5RASFrY-UrxNwqaMD4BlzWln37L527y0kdTqEAGxZ7OjDzpDyh5_C_7tHs33qEIykHQOFWRNO1pBPONobpTKh9ogWTcbQRzqZ5U11HqMjn20cC9dJAr7rgV5ajLV0DUY7Fo3myGy2Bt7Rjxv0VOnYaAxL7587l2o5KOTv3mXja9v4w_PfqRku6cGjJxKbEuAM4gf6zgmcDsHD2JzAyKWS2E6D1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کول پالمر و ژائو پدرو ستاره های چلسی تو موزیک ویدیو جدید و مستهجن مدونا حضور پیدا کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91753" target="_blank">📅 00:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91752">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الان توییت میزنه و میگه: جنگنده‌های فوق العاده زیبای ما در راه ایران بودن که فیلد مارشال عاصم منیر بهم زنگ زد و به همراه چندین رهبر کشورهای عربی ازم تقاضا کردن که حمله به ایران رو متوقف کنم و اجازه بدم تا توافقی صورت بگیره. منم قبول کردم و همین الان به خلبانانمون…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91752" target="_blank">📅 23:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91751">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325c4beb65.mp4?token=cWi2wTsEPPY1VIf6BRXk2OVgIQibUD-HnOtXqaLW6pv1UTix9jT-lM_C4VUjdbYGgrHfOg1DYuwCieSjGP3t7UPsj5e8mHzSpEpkcYiT7VSL7MVtLl2eK1PPVzyfazJL7mP_JTQgqWUcHcAp2OXfR7YXvRPi_aFvj4v4eBvuxhePpRQvOuUl44pcq2jyuYN3lg4sOkXYlasC_LwJRrDJ6_PkbMBWZxtN2IGTvjh1woKJR9d0jW3aK3HX7o3kzkzkuP1ssBV9y9m9Q2zP4SjaItyuBYnoW6C4Sps5VEzu51gzIuLK8wT1tUare8KXLj7eiWMsVtRzkyITR6HYwoxipg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325c4beb65.mp4?token=cWi2wTsEPPY1VIf6BRXk2OVgIQibUD-HnOtXqaLW6pv1UTix9jT-lM_C4VUjdbYGgrHfOg1DYuwCieSjGP3t7UPsj5e8mHzSpEpkcYiT7VSL7MVtLl2eK1PPVzyfazJL7mP_JTQgqWUcHcAp2OXfR7YXvRPi_aFvj4v4eBvuxhePpRQvOuUl44pcq2jyuYN3lg4sOkXYlasC_LwJRrDJ6_PkbMBWZxtN2IGTvjh1woKJR9d0jW3aK3HX7o3kzkzkuP1ssBV9y9m9Q2zP4SjaItyuBYnoW6C4Sps5VEzu51gzIuLK8wT1tUare8KXLj7eiWMsVtRzkyITR6HYwoxipg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
فوری از ترامپ:  «همین الان ارتش به من خبر داد که دیشب ایرانی‌ها یکی از بالگردهای آپاچی ما رو سرنگون کردن. دو خلبان داخل بالگرد بودن که خوشبختانه هر دو سالم هستن و هیچ آسیبی ندیدن. با این حال، آمریکا چاره‌ای جز پاسخ دادن به این حمله نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91751" target="_blank">📅 23:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91750">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961fad6eab.mp4?token=gCAw4hZDIEvg342JL8SM04YvWvGilNgyWo8_wcfKPOLZbqKlw07mYQjODWy5erS0vd58pGqLRKrDx7iyPEwb30FrGlHQwyVD24MibjbT-kwySxcZKQJJmz9J4sa_1UUoYql3M9QBYT6ETWagTuvML0F7tqrKDfuM9ucseqlUbZiS0v8Zm2EvhYvBooagLYo6tVI7Tcmgi1T7DlYcBiBpXnRF1dXhttJ6VMGU29fndw8pBmc-FqRfluEuvUN23s6bRzj22yWs9VNguq_BivJ__31qKmxp7lsm5Ol31APHeeLznQanCeuTCThK0_J8FNsqWomF8dOwRYvTBZifAuTMxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961fad6eab.mp4?token=gCAw4hZDIEvg342JL8SM04YvWvGilNgyWo8_wcfKPOLZbqKlw07mYQjODWy5erS0vd58pGqLRKrDx7iyPEwb30FrGlHQwyVD24MibjbT-kwySxcZKQJJmz9J4sa_1UUoYql3M9QBYT6ETWagTuvML0F7tqrKDfuM9ucseqlUbZiS0v8Zm2EvhYvBooagLYo6tVI7Tcmgi1T7DlYcBiBpXnRF1dXhttJ6VMGU29fndw8pBmc-FqRfluEuvUN23s6bRzj22yWs9VNguq_BivJ__31qKmxp7lsm5Ol31APHeeLznQanCeuTCThK0_J8FNsqWomF8dOwRYvTBZifAuTMxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🚨
🙂
سوال روز از رئالیا؛ دامفریس رو پرز فرو کرده به رئال‌مادرید یا نه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91750" target="_blank">📅 23:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91749">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">📌
۱۰۰ میلیون تومان جایزه نقدی - بدون قرعه‌کشی!
📌
​
​
✅
قهرمان جام و آقای‌گل رو دقیق پیش‌بینی کن و کل جایزه رو برنده شو.
​
⚠️
ظرفیت محدود:
فقط برای ۱۰۰ نفر اول.
به دلیل حجم بالای درخواست‌ها، اولویت با کسانی است که زودتر پیش‌بینی‌شون رو ثبت کنن.
​
🔸
برای مشاهده شرایط و ثبت پیش‌بینی، همین الان وارد کانال زیر شو:
💵
​
https://t.me/+5uTOXJ02mftjNzQ0</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91749" target="_blank">📅 23:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91748">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cUM30ZKtVLdmiunf8Q-n3E2MXmMnFqzYVSOgwKqrAef-VTAtI7tvosnXr00vTJgXQ1U9g1VTuBuBKjaNx1p9lwzxVQJj9eAEFwo6946Xppnq3E0G6oiN8Foy4SfavCFXBiHYGDShZ_gTHLwdxhbxsNeaY4z9Z-52WmBXe9dYnTWdVPJfCXS5NgyYVswC9W5cBIK4YzHGUnwfIvl4Qy5a6RB4HxONB3YsXUJqjyAabA7utQLRkgvcBh6KUUmW1rLZKvjW8a4xUO418_yHXeu7rlvpA1JANQ19uC9k_imky-irR8xy-qvOUO0PD9Q2h-6e2eQGoCFZs8XFU4vwHT8zkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
۵۰ بازیکن برتر جام جهانی ۲۰۲۶ از دید ESPN
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91748" target="_blank">📅 23:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91747">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igoA8Kvk-oESfYewqVjSP4nhZWNWF5B0-NB-Cz0AUqFCXneMCz8jtE-CeMTZdIcbglodT94igsqEGhG3se0zU1S2B35BwjmX8w2D27XJv3ED1wVJpqgSdej1beX_qKf4d9-Go9NVwgUICqeiAxeOjZ1ELBCG5aiE4zz2-JlpQ4vhMqlStw01ga6HcDWbaJ2xW4q8Fs1KvLcGKIllxKG_26juDu5QVM2AKzUp2G3Q-zk36TWFCVSIgnT5q0G3KYLf1iEVaqRg7aBf3sU46iTddi1anE6sx8wrDGqW6HbKQ-d5ChoNfWAhqiwMd5zlB2b5PGFm3cndPguMCXqozxgIvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💪
🇮🇷
🇺🇸
فضای پروازی ایران کلیر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/91747" target="_blank">📅 22:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91746">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
کیه‌لینی رسما رید به رئال :
⬅️
فکر میکنید اینکه رئال مادرید هر سال توی لیگ قهرمانان یا میرسه فینال یا جام رو میبره، فقط یه تصادفه؟ توی دنیای فوتبال همه میدونن قضیه چیه، ولی هیچکس نمیتونه درباره‌ش حرف بزنه.
⬅️
حتی اگه توی زمین همه کارها رو درست انجام بدی، وقتی طرف حسابت رئال مادریده، فقط با بازیکن‌هاش نمیجنگی؛ باید با یه قدرت نامرئی هم بجنگی. همه‌مون میدونیم وقتی داورها اون پیراهن سفید رو میبینن، دستشون چطور میلرزه و موقع سوت زدن چقدر تحت تأثیر قرار میگیرن.
⬅️
توی لیگ قهرمانان، بزرگ‌ترین رقیب شما یوونتوس، بایرن مونیخ یا بارسلونا نیست؛ بزرگ‌ترین رقیب‌تون نفوذ و لابی خیلی قدرتمند رئال مادریده که توی زمین روی داورها اثر میذاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/91746" target="_blank">📅 22:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
بیانیه باشگاه اتلتیکو مادرید:  - اون قسمت ویدئوی پاپ رو بریدین که می‌گفت طرفدار اتلتیکو هست!  - ادب و احترام رو با تشکر اشتباه گرفتین؛ برای اینکه سوءتفاهم نشه، هیچ تشکری هم ازتون نداریم.  - نه پیشنهادی برای خرید خولیان رو بررسی کردیم، نه اصلاً بهش فکر کردیم.…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/91745" target="_blank">📅 22:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91744">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGqg9ncPNTWJ4oMY_qwa0Wvst1Rpx6V5r8hXKnSongtUS0UHju6vHr3Y47HWAMusR4mVdlGx7q7MR2QiOBFlBdg1-Y7TweRAQk1y13kdN26ib4lzebQ-NClgsiNkT_UhgoqFYONyHkrLPgRFkYJT0ZJTAVWM4Ve0EyE1_71ZV0W1_BWJjxWX8_V5xukfpUhQAhP3effV5hlRyappCO7m7qCI4zHVeoTRLkdur18y_Vooecg5RhDL2TM6_IHQkra-yoCkEpcurishRtnpRVPBMUao1BZxAW1ykjR6jqftbM_B8_89ufli9zcayF84a_ELZaBpCwe_w8u4U4yh8aRLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بیانیه مجدد اتلتیکو مادرید:  «پی‌نوشت: با استفاده از رابطه خوب با رئیس جدیدتان، بیایید ببینیم که آیا از «دزدیدن» بازیکنان از آکادمی ما دست برمی‌دارید یا نه. خیلی ممنون، رئال مادرید!»
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/91744" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
#فوری توییت اتلتیکومادرید:
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91743" target="_blank">📅 21:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LQ5q_PEpIz77sYlQuoMAv2JybnI5DD13NNh_OgMiTxBKIxnvQ7kTY2FbpRI1jV1RMv-4yiab1UrTZHBNBmcUrBKv9YXZ1wAQEkVgYpOEP3ACYTj3N0ychl43KUtw2T1f-HauYbg-Lgk5uXng0FSEPPWHV05SWpPJ55vHAGoKP36bdrlov2FuC5dfzJljvKytv5khZlH2DqQeT82agaau-XviBXPjoJjs5JL7LiLoUKGLY4eDREW9bZgLIC_UnlYdGEPeKbHMtpX_I08HewbGx19xjlQ2qx-0Qhvnrv44GYxNlSbLcHIbJlBejfIE7XUYVYEHIKm5As84Mm0rM4iKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توان مقابله با این طوفان و این حرفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/91742" target="_blank">📅 21:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adQPFJsfE5nsszSW_3rmNYurMl0bihsJge5i3o0jmjYosjv70AYCjG3okgKna8tcy0MikSTGFeD5TYLalkCiiSYT3WApPsxfwwELiTdv_0BHODA_WAW_ASpbEiwohkHK-aw37x503B3nlFdCFYhiIMy6V7ZJXKS43ApQdTOZXXE5ia04cFBk-DFb0KWr2zUxP_L_QpL_ijNrmQ7VEr9I1IeGUMFjdUDtuAzpusEl518VWYAoukYjoE35uUg7pjETQh-PvJZ_k82cRsmk1QV1mUKlK1oKtObJoCaJw4ntPrchcrEo_UhRMREljv2qwkPQ7cA5phyX-EGvAi30Nc-GQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/91741" target="_blank">📅 21:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0NDnAF5rOV0Z1lR_IH_fXSGlQ50nzzqDQM3DIggX6IBc1oyhPCXhy3B6ANOqAmTn2rcELb51zK6-3mpFMxSgDYP0zz96AsUSINfP3saLocEeF1myPXWlWdM9A5dnBQ7v-xJ27kbF5SsNjl9Kgifq0Vem5SY2j0gXkNLxt7rKhXcF5hzyPMMZA4fReL6fecvB_f2enavYV4Uj4282je2t4rmxl68fFlC6p-48Jlr1vP9_Rwkjcf-X0zp7Mt03FdIVPXOxk-oEZjnNwUcFrRE0hH8dognKIJRZ2bUq0bJ4lwl4KaTntWuHlyQ-YplzvZ5MPtNxOiPl6ibk3wbK92s7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
روزنامه Ser:
در بارسلونا تأیید می‌کنند که مدتی است می‌دانستند رئال مادرید این اقدام را در مورد جولیان آلوارز انجام خواهد داد و این پیشنهاد رد خواهد شد.
و معتقدند که این موضوع تأیید می‌کند فلورنتینو پرز بیشتر مشغول آن چیزی است که بارسلونا ممکن است در بازار نقل و انتقالات انجام دهد تا تمرکز بر تقویت تیم خود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/91740" target="_blank">📅 21:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91739" target="_blank">📅 21:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
حمید رسایی: از آن فرد بی‌خردی که اینترنت را وصل کرد در مراجع قانونی شکایت می‌کنیم. در شرایط جنگی و حتی پساجنگ بازگشت اینترنت یعنی خیانت به جمهوری اسلامی!!  +منظورش مسعود پزشکیان هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/91738" target="_blank">📅 21:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
بیانیه جدید رئال‌مادرید بعد سه هفته: با نهایت احترام اعلام می‌کنیم که قرارداد آربلوآ به عنوان سرمربی به پایان رسیده و‌ از تیم جدا شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/91737" target="_blank">📅 21:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تو تاریخ‌فوتبال بین باشگاه‌های بزرگ هیچ تیمی روز اول ارائه پیشنهاد بیانیه نداده که پیشنهادم رد شد و تمام. پرز با این حرکتش هم یه ذره میخواست رئالیا رو آروم کنه هم کیر سفتی حواله بارسا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91736" target="_blank">📅 21:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91735">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Soz5mKzuMnA0X9ZUoaSRBLJ4mM-voMm_9hZArHEAlY_V_8I57WeptyygxyqGUyqPZhfVeYtVZkeRlvTT5Si_8wsK7ZyuTqaEn_DMbRsWQbk-rx40uyXxgFDgmD4kGhqLyX5efH7ndXsLyDRr4AIJN-cgPGzMlgTdDbXp0DkQU0W0eySvhzPE09UVt7UrvtUoSouxcxX5otOzNQbmPlB6vQuyVkaLtJkAlqWShwuvLBSDQumxp0SstTv6ARBzv0icHxD6oUXjMZEeO1761fIC7TAVRFmo9Rv83c_UWYxWTdN9ydWrcPUb6RhGkuS-6_X6o0f7nZjXLUDfvGqRKqOldQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
لامین‌یامال: نظرت راجب مسی؟ امیدوارم اونقدری بازی کنه که نخوایم به بازنشسته شدنش فکر کنیم و‌ بابتش اشک بریزیم
وقتی به کمپ نو می‌رفتم تا مسی را بازی کند ببینم، چیزی بود که شاید مردم به درستی قدرش را نمی‌دانستند، و آن این بود که در هر بازی که می‌رفتی تا او را تماشا کنی، بازیکنی بود که باعث می‌شد از جای خود بلند شوی.
همیشه عالی است که هر بازیکنی گل‌های زیادی بزند و پاس گل‌های فراوانی بدهد، اما کاری که لئو انجام می‌داد بسیار دشوار بود، و آن این بود که در هر بازی چیزهایی به عنوان یک بازیکن منحصر به فرد ارائه می‌داد.
فکر می‌کنم مردم وقتی او بازنشسته شود این را درک خواهند کرد، و این چیزی است که آرزو دارم هرگز اتفاق نیفتد، این چیز باور نکردنی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91735" target="_blank">📅 21:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91734">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ولی عجب کی,ری زد پرز به رئالی های که بهش رأی دادن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91734" target="_blank">📅 21:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91733">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/91733" target="_blank">📅 21:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91732">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🚨
رسمیییییی :   اولیسه ، وتینیا ، نوس ، پدری هر کدوم با ۱۵۰میلیون یورو به رئال مادرید پیوستند
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/91732" target="_blank">📅 21:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91731">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🇪🇸
#فووووری؛ اتلتیکومادرید اعلام کرد که فروش آلوارز در گرو پرداخت ۵۰۰ میلیون یورو از سوی باشگاه خریدار هست. در غیر اینصورت زنگ نزنید مزاحم نشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/91731" target="_blank">📅 21:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91730">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/91730" target="_blank">📅 20:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91729">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🇺🇿
#فوووووری
؛ ماشاریپوف بازیکن استقلال بدلیل مصدومیت جام‌جهانی رو از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/91729" target="_blank">📅 20:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91728">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/91728" target="_blank">📅 20:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91727">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOHh_HizoKJO07TfUUpyxOv6oYWnJH0c1YyA-JsVS6IJ30oT2VUqlZY5YvWmqqVZyWS8CjbKk4Ne9rVsrFkVWR23lry5Yj0saxnWwywXwbTkRP7Aqb0nb2Y2_Pzqpe_Ka2nvP0XAnQSoJrC9agzOMSc5RYoPcUdaIWBbJk1Jl6w9xf6P9etgujlDt72rFKs1gi35tJFNGONqcgeuHphsqc1cYDbmzyX8HrnSfnoJl2kIXdvKmi2pXkVdCbNjy6D0_fQ2OHo0hty9GLD_spHMlrpPkPXdfJzZKl13FIARF5EZadYzdLfVkgFntk7xMrwLrC3_15HERM6hQcBj6sMhUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/91727" target="_blank">📅 20:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91726">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvTRFQ3C4ekKIwxcI6iUchpVGWMHarl_QgKiE6YYJMyRLqik7POg4yPzgSm3IxzZKBFWc-Me676utYev32Io_ilXHRrXM3sfxAmLSwCjcHsgXPOhaP6eROcJr4ys4pvsNBTIGQDiJsPThwiRbMSaWHPnQPizZ7B-X4VC6ufxNyKlVub1T3rjm_wKJfgExdhTnLt7OlslWCuOMYbJBvG2pkwbIPNwLBUP2FOwb4m3CcRMoNkNp6nwZiNA2wgsMx8nimonR3v1JldBSzbbeXVj7kp23WEL8MsLJ139rkD1vEQI4f1aVtB0d9GGqlYS6BWpcJOlpLXXsUyyyd2J0Q1A1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووووری
؛ بیانیه‌رسمی رئال‌مادرید: اولین پیشنهاد ما برای جذب خولیان آلوارز به مبلغ ۱۵۰ میلیون یورو تقدیم اتلتیکومادرید شد. اتلتیکو این پیشنهاد را رد کرده و خواستار پرداخت کامل بند فسخ این بازیکن به مبلغ ۵۰۰ میلیون یورو شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/91726" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91725">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roJLwr1dQEEhdf2gB5dT2ogf1vk5Fe3nb96PMKIFFr0hEvXhNM894Mn_cjMpRc6nFNwofQgg623IIZczsKUyweGOwZpxLvIpvQUObAjG0AhJA5M3D50OYfYYU7faUEf1bnLOpXSrFZW_lKmPPoGQEBkqooRWk-dm_TqYefNyOYrA2RfkdaEITO8hdVlPZ0XEz2FU8mtsgNEgpVJvWbkXl_dRFXYDfrIVKLwtchOihDl9wPaWOfOxg4spdOG5jCwYHACheIzgTKEl4pscTYQOEFKDRwXabjWEzthbUKRKXwjaY_jEB85gxcYX1U7jAwsQY2QUUo331_Saulw7adZ7mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو ناتالیا اکس نیمار
چه جواهریه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/91725" target="_blank">📅 20:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91724">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🇺🇸
فوری از ترامپ:  «همین الان ارتش به من خبر داد که دیشب ایرانی‌ها یکی از بالگردهای آپاچی ما رو سرنگون کردن. دو خلبان داخل بالگرد بودن که خوشبختانه هر دو سالم هستن و هیچ آسیبی ندیدن. با این حال، آمریکا چاره‌ای جز پاسخ دادن به این حمله نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/91724" target="_blank">📅 20:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91723">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWXAi0i8RSCnhb_NkP4tjsTaEvjY1JPhuVpAkc7ue2FoWoB-46Znr5TdRInVSDa-fVrM-iJCW_TJp-hO8GPtSfnrUtzoPE33zaPf-RCtUN9C-AvN-pds8RAXFt7lf_C5cRIqTcK5_J6yiRn17Vc_rbHK7hJxcm0rpRcXFtd811ptkFd6w7vSgka9YipmFQ3FKI72UUAEuS5G_CULvtkers9j2XqYM0McDEpApu05yPTrZm1VJqSYZcMPVgoHy9JRreTq40YeiVNaR5mHOT3d3925on0VU1z3YoplnkHDOBOoG5NLZDLAqXwFzgDUNjQZOcYbk_CqT-8rY8R2ucapBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
فوری از ترامپ:
«همین الان ارتش به من خبر داد که دیشب ایرانی‌ها یکی از بالگردهای آپاچی ما رو سرنگون کردن.
دو خلبان داخل بالگرد بودن که خوشبختانه هر دو سالم هستن و هیچ آسیبی ندیدن. با این حال، آمریکا چاره‌ای جز پاسخ دادن به این حمله نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/91723" target="_blank">📅 20:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91722">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iu242hT5M4vd7QLlmQNE1xkuYmtVJOh8JqKAjMvRc608RCwelmTn2AjgY4S63UYEvi2K43BeYkZHDH-nLwf1ATmAvaYL2aSM-vRjiU2fh2-VyoTyax0nAdFoa9egSfXJ6j30K4CaFtnf27SZjEHbPR7bGEUoHr_9g49Y38IayoXSy8S_ljZJRA6O1WJHjiqWDSqpwL7Xc7najhczD3l172zwsbbFRSRT3spuFFTuJQK9inomDOL9YzhLVEMxlpXIiexX7zp2e7PmXGPG8h_ZRMKmj12AzVT11fAzTDa94td-5tyUHPm3vx9sLEJjPN5XNYl6yJt_luh86wM_eNIK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برندها با بیشترین تیم در جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/91722" target="_blank">📅 20:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91721">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qNeFdAQFnFbkXZwag3jW-uGcdMUcuORjv4UkMlZ5y9T3-EOWju5MLzdSEaCV5ZCJ44zC1l3cO6XVY6BCMeZ70l0x1DilMopvJ2PzXsdrVcI_DFbgsR-R9jwL1gYh4RnFAP0KqE14Riy8pnPQ_9POSdA6IEL2F-mBDA-gZd2AMrdrRPHnSMaZXg-TNbWU6oQVEmZGICkPR0Qsbdqa8ojOXk2KEE_qxEqths-YSZ5IQW1KNAa1dm4XqNk6ui4IXlIZULW9GUAIg_YhkhDYeXYLhS_v1UQSt6GIhahrkDRM-iCtdCq2PoGKNcq2qJR88_2vxdbQgq8Utc5EZpFEJOdYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚽️
فرناندو پولو خبرنگار موندو:
⭐
-
برناردو سیلوا هرگز اولویت بارسلونا نبوده. برناردو خودش رو به بارسلونا لینک کرد و گفته که رویای بازی در بارسلونا را دارد.
بارسلونا سیلوا را فرصتی در بازار می‌بیند اما بدون فشار یا عجله! مدیریت دوست ندارد بازیکن از نام بارسلونا برای بهبود سایر پیشنهادها استفاده کند، اما این به آن معنا نیست که او به بارسلونا نخواهد پیوست
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/91721" target="_blank">📅 19:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91720">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7285144264.mp4?token=cHSNT9YJh-U6TGuKIA7Va4FMwFTbgRoGv_YyxdDxKNaqLCGwvt3-xjFwwSvHk_BQKFyTArVa0sE_KI-RypeVPCUpgKzBEwJ4MbZ5EjhQIPYRsqsDqdJpIrcUBHAoaufCODmIhR2co3kWoZ1Z4UIjEbxFZPyKhxt1Zld9uGojFgGx_cOVMVKct-RZe1MFu92XQO_o5We_2IpBtyRsX_CYpK0n84U5sZ2QxW5hPZYMwHjCJ4XDcg9dTdEn4UraZeb0mYiBOtxMffmilhl5ZjAE0Obc_H9YZLndQwpC4BwQdxzn8UtLD8JvkSR_YKfMEcdYImVa12ik2ttsFKUp4TriVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7285144264.mp4?token=cHSNT9YJh-U6TGuKIA7Va4FMwFTbgRoGv_YyxdDxKNaqLCGwvt3-xjFwwSvHk_BQKFyTArVa0sE_KI-RypeVPCUpgKzBEwJ4MbZ5EjhQIPYRsqsDqdJpIrcUBHAoaufCODmIhR2co3kWoZ1Z4UIjEbxFZPyKhxt1Zld9uGojFgGx_cOVMVKct-RZe1MFu92XQO_o5We_2IpBtyRsX_CYpK0n84U5sZ2QxW5hPZYMwHjCJ4XDcg9dTdEn4UraZeb0mYiBOtxMffmilhl5ZjAE0Obc_H9YZLndQwpC4BwQdxzn8UtLD8JvkSR_YKfMEcdYImVa12ik2ttsFKUp4TriVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔥
این سوپرگل تر و تمیز رونالدو به عنوان بهترین گل فصل لیگ عربستان انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/91720" target="_blank">📅 19:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91719">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
وزیر ورزش:
به فیفا اعلام کردم اگر تو ورزشگاه‌هایی که در جام جهانی بازی داریم پرچمی غیر از پرچم جمهوری اسلامی بیارن یا شعار علیه تیم‌ملی شریف ما بدن قطعا بازی رو متوقف میکنیم و از زمین خارج میشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/91719" target="_blank">📅 19:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91718">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpSQnPjbhyag_8WdoAZ_UCnUixxvXLYo-IroiotP4V7pQf53ySC3G64htcQ9P-idTsfRyT2uw88WgtTlrtPb9UcgpxNzgAXU6xwocDqirU9axapsQwFmMKNv2XIlF-A8poBQLFyF8IXvA500tlLJovYOGj5J3lZ3ZIHIX6DBoZIi6S-BQjSOpOzeobPG1qzwrpQemrttN_ibZnRb36mk1PWe-sobfcMTW6XxzNGP1X5DNy-ESo2OmcAO1zk_1lmEqRKWWyq_7poSRlwXKi6CZviVHOXumPF3FpAdSDxjEHhkjrn67Ofg9mQRxoyc7a-tllAhCa7iPPIKDurJFr_j4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورانیوم غنی شده که تو پات نداری داش دیبروینه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/91718" target="_blank">📅 19:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91717">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
فوریییی
❤️
🇪🇸
یه خبرنگار نزدیک به اتلتیکو خبر زده آلمانی مدیر ورزشی اتلتیکو به دکو گفته از جذب سیلوا کنار بکشید تا ما آلوارز رو با ۱۲۰ میلیون بهتون بفروشیم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/91717" target="_blank">📅 19:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91715">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/huksKTJWIgZebieWyV8L_at4UHI8KL6uC37V8mt6af-4s3aVriYpG0aq9eZWUEflyKm8Dcldd1F12QzyNowvF-I4f0b3pmpuEe-zxvvh_D66DEVrGTm0qMCOYTmsy8mXlhyg9brc_C_C8gk_WG_Vsc_Y1Iheg5hLsNjyfwz6lHGSnmQ7fNuUegrJ6B6GN-6XvusCbRY2LPfl6shq9xHqh5uZEJ3HHOZKXCxfkpJWv29jXcPKMKgo-7yCKyt88WayWp7i5Z2HJJ8Li9uRzSQj67xQV8z3JoRE2K8HBitB0fLI8kUS88qvSSicR7KmYlo-0qtJw70grPIlsiY4nwxZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dDA2jU-GaRhuHaLMvohk2RD6zyyNeF9FRd904qoTP_p6D3dgLHM0jqS5Zf3f-w3tWMVFs0WMU_EFFx5y_mYTn0LjBW7sCR2j4a91ZmzPVCCINPkGLcy6AhW7Zyi-8YHeXirCM8_ibD1cL0LrBbGcTeOWlU4eDpzXwzyPm7DMO-r_3yb05rr7xYRyRtmD7-xzLgQxNZdtmjPod0C4bdouBGsSl0aP1GPDza2Bvu5cQKmcuyGSSNpjzyAbDJXS6FEZYFBX5-dSfflfMXkxo3Bl8LZx8ZkLULG366jGyrqTS55elw1duCMuzdZap82tLbGo6NSfxRhXAcy9GDGlWWS5HQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😀
🏆
- ورزشگاه مونتری (Monterrey Stadium):
مکان: مونتری، ایالت نوئوو لئون
افتتاح: 2015
ظرفیت: حدود 53.500 هزار نفر
🗣
با منظره کوه‌ها پشت جایگاه‌ها، به‌ویژه کوه Cerro de la Silla، که یکی از برجسته‌ترین طراحی‌های بصری در مسابقات است، شناخته می‌شود.
🗣
استادیومی بسیار مدرن در مقایسه با سایر استادیوم‌های جام جهانی (کمتر از ۱۵ سال پیش ساخته شده).
🔺
چهار بازی در جام جهانی میزبانی خواهد کرد (۳ بازی در مرحله گروهی و یک بازی در مرحله یک شانزدهم‌نهایی).
🔹
مهم‌ترین بازی‌هایی که در این ورزشگاه برگزار خواهد شد:
🇸🇪
سوئد × تونس
🇹🇳
🇹🇳
تونس × ژاپن
🇯🇵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/91715" target="_blank">📅 19:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91714">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حالا فکر کنید روی بازوبند مشکی حاج‌صفی اگه به فرض محال که اجازه بدن، قرار باشه بازوبند رنگین کمونی ببندن. چه شبی بشه اون شب
😂
😴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/91714" target="_blank">📅 19:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91713">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxRr9H0DPzDhWmXr5J9WXTCViE7holk73NANg05jnx0hawC0sgbifwu2yNrwbCBVm9S3AVgjTWhk9znpWotWYOmwO0t1mZ8c1aGk6tg6zHnxgCprKFHp4Kl7SYSwoqOjlueHU6txlB9roCua5I2mGzNuMtLOZYt3GuXKVvPnC2sI-U41w3TRWE5hk8Gz8jsaty49_VelLQdb2sww0TOHtvmj-WjXy9JWTxsSWXWR8pZ8bZwfKUh587goaOOBxkdqzVz2hovXJ3z8F_MSvzQ815PrRmUJIOxFjHIccLWHxXYyRv5CMIO_VS6evkGotRugQh0qGk6uQ7WPiLMLfmPcFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
مسابقات افتتاحیه جام جهانی:
◉ بزرگترین پیروزی در بازی افتتاحیه:
🇷🇺
روسیه ۵-۰ عربستان
🇸🇦
(۲۰۱۸)
◉ بیشترین گل زده شده در بازی افتتاحیه:
🇩🇪
آلمان ۴-۲ کاستاریکا
🇨🇷
— ۶ گل(۲۰۰۶)
◉ معروف‌ترین شگفتی افتتاحیه:
🇨🇲
کامرون ۱-۰ آرژانتین
🇦🇷
(۱۹۹۰).
◉ از جام جهانی ۲۰۰۶ به بعد، کشور میزبان به طور رسمی بازی افتتاحیه را برگزار می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/91713" target="_blank">📅 19:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91712">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIUQ30XZITy-9ZrMHrK13jKY98IIhhPVm1plQqCaXgk8u8r6wFpKP7aSqLUHpWZ6Rv3s2i9__o0Pw4_vDvkM_uUmiDznRIynw6g43GjnWWeHCmpgxyQEtRcCSpYyrFc5gyx56uSXOQh6qJ9AALpQGBERYj7FxSZzwNHiwx84hkL-hE0vHWPC1kaA-6OyB14z2WqGVLi2yjwFl_K8QF-ckbktszSC2DHV7T1rrYtAK3jtgkLWvmQM9EGVmMNRYGFacvhHLVMV4QB-1OcTn9ftY8jMdBWPo8Smtweckts4BPnoMBCautU14lHjhaBRQivUi5yjKKyCpI91-MUhrUy7Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
| آیا می‌دانید؟
👀
از جام جهانی ۱۹۳۸ تا جام جهانی ۲۰۲۲، تیمی که برزیل را حذف می‌کند، در سه تیم برتر مسابقات قرار می‌گیرد.
🤯
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/91712" target="_blank">📅 18:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91711">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7i8YZ7N9tWzjacIZAkKzaC7wkpzkVMgmdBA4VC70kT0ASu6sF6r4bxARPH3Ie02mmZlLwKs6gz3WPdRZMEQD90nYxS61_CiaiKAcwlRVoKnZlO1YbfX8eo4w1WeG8JRppbxgKTvjpNnBrJ4GlYJavRWrEzXON25sv-mPg-fTAFAV3p39RweOu6DWTcnZUzetqm7YEk-X_YX902XjRzvZ4t37EoUIwVu8tgouhDrBozFQ_EJzAnRuhpk51SSvSvPXpD9JKb1Apxn8TFiBd5R7k26UbZS8RN-Ag5LMk0RH5y3ZmSAUVg1dxqMZQ4un0tLLHhgvCPR84D98EwoqlTM3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رونمایی رسمی فیفا از جایزه بهترین بازیکن زمین جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/91711" target="_blank">📅 18:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91710">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vG0QNzrCOSnAngfT6mGRAJ8Wye48FT5lJPcJdQ6iL9VR_RlgqiH-6wKTk2SpPrWByWC2MPnXH8Z79jQw0Hs2SW1H0mAvWxBLydiQp8LA5O5mfoqkGEcfCAAQA1c4eu12MsOx_TSfclAO3YD7iG21bkDUZiaud_l4HHlu1TmoFc9nNOYqRNTdVx-kbzEXOnAFtqlHCNvyzSV-A1BLC-DHFBxvrHRTz4AO0n6tmu23CC-Dd5vSl_R_k6WNBY1pNuJTp7aV1E7VCRWLGo-AWDJbOMb9bC-2hjif-NWXK12nhz9sAZYw3nS9S3aqUu_G9nMnZbINiXNugPc1VVKzXjpfjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو :
🇪🇸
🇮🇹
یوونتوس خواهان جذب براهیم دیازه اما تمرکز بازیکن روی رئال مادرید مگه اینکه نظر باشگاه دربارش عوض بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/Futball180TV/91710" target="_blank">📅 18:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91704">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oq_wWMidPPoRv3IUH8kdlq4nlUUYdvL_ZaqDkcE0Dugx34e0dr-7oOAkQqkzu0zqJClvpVHtzxwYpbVays3G_yVoHZAPLm0u31MExB3tlhG001pf7GEgDqvXp-OKV64-YHfNS7q02N-Vd4ssJJFruX7R6kcg1FCPuG9cwEUuNi3g411CK-DDu6uJEnU84gwtT75C6YnQX17O11o5hk4qcrg9--N-ARbgRKD0PhWuYVcWT2kBUtBwDmnE1soEQNcBKHkT04A7Ph7tHA8W3-HY5uNaKWbK3yPplZdul_-CZ6KVZLloQozU1LXQJnXAExAeQw6UrQ9ZRC-ppjovoFggVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-I_zwOsem3eMVtQ6EE-hh_q8ozeXRZ1Oby4MQQOrF4mX8YMpYStzj7cKEjozPsQU27ZyBGgMNdWsEkpO-vB5-7Ckk3-FRUrycg1HXTNYbekRN2zdMnqYfbxGRTIjdRaG9d7_P6XAMPR4_HaJiKhPip1Sb1HuF3KgtX2aoY1O2RzarrGZsqTJxwDtK2m-7zNWYST3k0moVALntArcCtT5xY82Jj5JSk3jeOsdIqBdvSHBxi7Z_ZWxfARoEWYZFJyX173nETnm46eLEt6_YUFu5igNnPGAM_G97K5hQjTI7fsoUYwUe3v7NVjrtJo-kRuFwSgjK8uzDFvulLqXBt8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K2WPT0vhnnSacDiQmIktIasb4_JtNAHi9QOvJWSxAI3QlggOq2wM3tpCJPmnYwdpaCci8IOOoc0F44WgolcP62mbxSdRCUc-vWaRCpBa4P6JVMpOdMyeuXCTyFEEUL-ZJvrVq0ca-1k2DAhBkmfqOY9X0H2AMAkxGMQOUIpPC27wlo0SvihKci7_piAi0CLzYB7vkHv-eggMa1vD7judboMhHvfQ_OlIVTpI0bOynGoYLFKVABq2pycDPUlxRugOleYqLrLaMTIfT08yeS2GNhHZB0SrPSM2jYnl4RDYbmH5tPJ6AjojkaUXkEmwnt1K8B-mGlc9JoiHsp4OlZJKfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این دختره توی اونلی فنز فیلمای لختیشو میذاره بعد یه پسر برای قدردانی و تشکر از اینکه دختره باعث شده خود ارضاییش لذت بخش باشه یه BMW آخرین مدل براش خریده!
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/Futball180TV/91704" target="_blank">📅 18:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91703">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69522e0ec.mp4?token=kFK6jLOM3Xf2LTHAYqhd_iUZe0ODGBDjwCxEZbMZjwsuiqWvoOV7SRcXxiJ_p9d51bc7jlRtlX98m8ApJYN6RrUq7LrHhSM9cuNmrtX4gPSsIOgzcdfcdmB9pN46LIExN9thUuzNa0_sEkJfx0isixfDFheqdSPeIAafG7Gb0WUIUOCS9-95iVVy0eT5QctgH9k9FWAnu1tl_jnx8csbaR-2CTJSux1gAAixyJmXpjRfe_hDkIOSO6rUDr_vZI5Sm6uopICZUHIEbzaujIeSnXw5SYsfZI4fqtDqZx17wwjUt-ciCzJo_EG9Gd7dFS3KeFBjQYCxmc_0IDhDf-GsMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69522e0ec.mp4?token=kFK6jLOM3Xf2LTHAYqhd_iUZe0ODGBDjwCxEZbMZjwsuiqWvoOV7SRcXxiJ_p9d51bc7jlRtlX98m8ApJYN6RrUq7LrHhSM9cuNmrtX4gPSsIOgzcdfcdmB9pN46LIExN9thUuzNa0_sEkJfx0isixfDFheqdSPeIAafG7Gb0WUIUOCS9-95iVVy0eT5QctgH9k9FWAnu1tl_jnx8csbaR-2CTJSux1gAAixyJmXpjRfe_hDkIOSO6rUDr_vZI5Sm6uopICZUHIEbzaujIeSnXw5SYsfZI4fqtDqZx17wwjUt-ciCzJo_EG9Gd7dFS3KeFBjQYCxmc_0IDhDf-GsMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
۸ سال گذر زمان و تفاوت از زمین‌تا آسمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/Futball180TV/91703" target="_blank">📅 18:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91702">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tteHtSFL0OVm9nBOBxmI6PMBn-GX7U6lb3PCjb1xh2LUDV0rybZPbeqKqoBSOzxf1R9k_-3uTmG-smuHrpNhTx1dfjIWcK-73eiJn_Na3sbJCtiAJS_opecvi6G1ki3TLB8eFu3MrVN0EJsX0H3bBg6Yo4N6xfM3Z_XuvUpiO9SMuiLzk4-QW6ZvboPT_Rh3at-r8V7teAIDAclS6I4D-sQDrjis_5qc8zAI5cU0kqv8vw08MGCfS0UoF_rkn0uyj5T58N8t8_aBrSXGYLtChvdNQHTSXoVUVHR1Gjs8QXNltgY6gznx0__br1XsUwF6M7C_g2h0f8Zsf9TY7Xosew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوریییی
از رومانو:
⚪️
🔵
نیکو پاز ترجیح میده به جای اینکه الان به رئال برگرده یک فصل دیگه هم در کومو بمونه!
تصمیم نهایی با ژوزه مورینیو است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/91702" target="_blank">📅 18:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91701">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jS0hIXZInmWP7BoPzmtiMfC4CHo3W-OHQ9tPKD0A-tt7SNLH9RntV00SFAJmmtlBU5_OgeRT70xZlKh2gXReduAb9YwLajxvbycoz-DD6iiL_VnY0PmY8I36Jmui67ohD4bb-mcG4Wu5Yss_9IYuG084m_YYb21uIcfSLT0hJrHfzQCReYaxXhDSlGBmxMFaPiiaNyROIetQGkFHah53RumaNEkKme1cggO8Pr71-USIxDpqFSuLWnscuby6zY15kvu4z8s9o7siAdPVOzY2ctZGzvQVj7MXplCrPDHqJv6na80sLlGpLBkRDi8SHmKDMksBZmAAVtmjkw1baumrfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توتواسپورت:
پاریسن ژرمن طی چند روز گذشته افتاده دنبال جذب لامین یامال و میخواد شانس خودش رو برای جذب وینگر بارسا امتحان کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/91701" target="_blank">📅 17:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91700">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn3kwDn2DaLODSleiR8EGYX0frqkqpG2rbRV-29eozZgMndnsyDhR1eiZV6KvP0Y_KrYv8MFpuy-tJKP0pK3fgQQJ6g5tXn520V5MMF-bGLLYypd2DqSux_jNU5CdKuCOts8BzrGDaq4trjkEzTVD5oKGMwG5bBxTfsi8Bdj2l7-npm_S5Rm_V1MzSAQcN1s73vf128iZ2PUuC_mRHzeYLnsgs9mWl4ALyruWJXVx8jYnP1QsFp1H5zULytS6W9XM0DG795eGT3GQkUTLbFKaloIuXwzDvgy1Gmi2KDup2P8S9dgM-XpyAb1obqNmHk-mmsYKo6cwZDNIrqFWi9Z-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇯🇵
تیم‌ملی ژاپن کمپ تمرینی خودشو که داخل مکزیک بود بخاطر شرایط بد و‌ امکانات ضعیف به آمریکا تغییر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91700" target="_blank">📅 17:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91699">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fba6ae20.mp4?token=HfQGF78xnBEHL2HN2QKgZh2_fkq481yVA6Xyg0sZCpnH5g9PXX5-vsoMIFzu5y4FWfisDTAmYEGxQDjb1dP147paw9_2pWdtoHrSFYIAqnTLHRJDUh7bpNVr8cMGJtjxQKTgBICZWOBVL0euVkiMx9C6iUIWXUxf6Um6Abbgox4yCmkrVlbsAJ0DOBU807H4265qwguQ0F5Hg692i1LqEHHGkPVvW8DXhiTmlUkl3ZbVitCwO5ozXKVQvejNbgmC0yLsYSjGlnDLTztMkmB68UdW6IUcr8rYENJoOpeS_CZBYG9o4BwKZQWfUBW9zyxkEVw-cXmwhXK-1v0ttlFayg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fba6ae20.mp4?token=HfQGF78xnBEHL2HN2QKgZh2_fkq481yVA6Xyg0sZCpnH5g9PXX5-vsoMIFzu5y4FWfisDTAmYEGxQDjb1dP147paw9_2pWdtoHrSFYIAqnTLHRJDUh7bpNVr8cMGJtjxQKTgBICZWOBVL0euVkiMx9C6iUIWXUxf6Um6Abbgox4yCmkrVlbsAJ0DOBU807H4265qwguQ0F5Hg692i1LqEHHGkPVvW8DXhiTmlUkl3ZbVitCwO5ozXKVQvejNbgmC0yLsYSjGlnDLTztMkmB68UdW6IUcr8rYENJoOpeS_CZBYG9o4BwKZQWfUBW9zyxkEVw-cXmwhXK-1v0ttlFayg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو تیم ملی نروژ برای جام جهانی به سبک وایکینگ‌ها
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91699" target="_blank">📅 17:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91697">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ua1htH2J-RP-U1mcn6eH_XWhhwkvbf9bWtWwCNHPXOx642ZFpB0F9qV2geA68x6k7cLftyvYrYWYsRDReU4TQRFARkda_7H81LQdEPUamby-HO6AF5aSWxi6jiAzmrJ6amQyhizveM-ywhBh8LCgN0MLWFsqCjldwFR5yz3KY1w01fHZzMGbBwaH2XdMEth6CNATj11GbRlaBOhKjj9G3ZNMdCqdBOK0F1yAb5MMJYtsU08BbU6wUHLONsgTnh9IXFiREewM8h1xkhVk9d1LiWifzVhkj6JpPKGcOtKRcBeNFtEUHULjTq0ri2umyibNiUZ3BrhHeTB46EcygZ-gaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmHeAskCCNQJPZ28qs8du10XasWEyT_N00-pa88QA4oNNJFu1cfSxib25QEIeQ3wQVS3napGhxxiTvXIOg21Aog4sFsjl_ON93Mq0q0j6VMLyRn-34NEeyiSUeWNPMi8RF9nmEveRZrIkPVpAanqzjwaiqYRdV2swwhxFZDZVgMqviJ2fTaM0Z1pPoLA1Pt_5zSwSCihf3qNVi2vd4L9bjYYh9MbuoM9XJwyUYT-3t7GZqWpv9Z4BBMU6iLtF9LKbsETOjIA-79Ie0T2z1bu9wmvAWNaycqzm9sqtvFRxqUj3_RunY14LE1Jjo8LW79aZ_ozVwi-z0wUuXZDJa0okA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Newcastle
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/91697" target="_blank">📅 17:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91696">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHlQo65d9mp2gFS0ZhG3TM1iUcH8rYjw1xMS0emOd6jcG1_DpwAcUgqWi52SZS_t5qME3NrBtMGCyZtjG0fLBWTipDUHspr0uzDSRKEyUircxNvLe5KdTYXwJQ8F9CfzTq-HZDLWBIusc9-gUCzHjOrjXGXWNkhZm_YO1mvnzF5E2WEyxpqmBBNSrTdUNhKiKupK0pT8Tq27QJyqUjdopzn5ke7r1_ccVxXwvFq6bwx5eN1SJGk54Q6jKe7XgCt3-TKnHmbxfQxqFP6JYMQqmiQaeoYGfDrFa5Wasmzu_UaY74-J-xo4tTIcc9Or3Eb7olRbAxo8xYhxP8MkPOaTKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گلوبو: نیمار ممکن است مقابل مراکش به میدان برود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91696" target="_blank">📅 17:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91695">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyiRlcW7hwklNBXIp-mYK2Z7qdSCz3HFVt9zUgH_pP3za4pzNGSusqxOPuhVmo-Jvp4eyGUJFWLOyv8sbfx3U00hsYOYJNe91OSj918GLgwOkpC1lizutYTMWZHlz16gKKn8cVmfMbf_MygR4YKIdbFGSSo-vw9W6eYd2dEYgeuNVtI22Ans3n_aZnv_8-AWA--ZE34XrcdIl3_qdMsg--BBhmXSzVixSLUZeX6gle4ErRyA-o5nqwYHnFBhN4BKcC8v3_RvfA8b76U2yVfUIVwMB7xOTq0_YVTmx9b6VyLoVJXDchKJkWUobVl30yWl9_1Yufost9PE4KNS1V1HBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: منچستریونایتد درحال مذاکره فشرده با وستهام برای جذب متئوس فرناندز هست. رقم درخواست وستهام ۸۵ میلیون یورو هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/91695" target="_blank">📅 17:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91694">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eek6Gc11PaV0yNjuaOpIpHZi--DJuSney4QjnIRm04UFzJ3nIfyNu_6ZwZV9xloFZeXuIfwuoSa-U_zwVKxHam2rnEphimO-1NKEeNJP-sEZdZ8zB3Npp5pPAc7Bgww0pPuV2bE3ccb0kYu2TLS4Hlj62uBRKcitaTZx1At6H7w0OKzNvt768O8j6dTsOZn0xzPsmo7EZ2RZwEOlWZc-waPA8IoZVEeWHvnjqStX9mW7Ej_EpuRYDPF_bg-QY_G52xLNCqa37x7mvr3oI-MzaFp8ozNk6aL_ffGcjco_nwGl-Rm3plBFEAyPDdnLmMLJI5qsH4fWjV0pl8mPgIMRDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
⚪️
رومانو:
براهیم دیاز میخواهد در رئال مادرید بماند و برای جایگاهش سخت بجنگد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91694" target="_blank">📅 17:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91692">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bp-REOOU7t8FX3b-bwd1wwxeP51_FgQxUiZsztwyWVq_AWHy-rH_ZQqyjbdHRmVXZ0A7Eqx0uHi-qtYYsdPuvHhQV_fQ9ANV2A2tEJG-dH2qLehNkJRaS3ac5L9JYSTucziF_OIjRSC-Lapu8dqdcnpbOquFYo_-o55clkpzN0vN5DDKrqh8g4ymyUUJtZUrIA0YxFqaDQhotZQ6WYowjcuE7pPwSap1tyibTmSi8KEdeCx5VN-Qrko25MBbG7cbSPFpYxk5j5x_4TvKxXGDvd55_8lVgtsL2MeYJFtze-SIL8VR6rqkHxzqn0EU2w4drXYQn6CwJD1X1wDDT1niUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYfXNifr4TunRmYHvDikRRGHHEwLdAF8A-eesclgd3nzbzcovaHqazDSQcOq6ptjqZ3F5OPe2SODkQ3N6fUE_rllpusDOoDitwrfoITSpiDekG_3rH4XLATHN5REc7S5d-UZUEPAIBskazB99Caeh0fBGOK5dC4gGwOj349pqexXy_doFrWCjcBjWXQVMMn6F4uS5Fd-P1A2gSFL73dWOHAviHGodpNSu4UgNfiKvpig8N0CuqdKv_el6CaMTdeWvTPxNcICLvdG8vTQtcUqAxaW1LInX_Qh443eynaZyJgvyFabSoTHXKBpPkYFL1x9yE_Mwms7H4pQw7t0Xc7xTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاینات پزشکی رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/91692" target="_blank">📅 17:12 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
