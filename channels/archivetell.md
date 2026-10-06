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
<img src="https://cdn4.telesco.pe/file/jjBIOKkKZ_tWstndsHwXoc5rrIpbWh_0m3CNxxCzHlqFFNERDdgOHFbESvZsGV2uj_vYtIKI8PHYBOvt125hBpme6LIWMr5VogtImecK3m6Hz07gHVebh1iEUQ_3YyyIJOTq8oRQbP6rFxipK4QK_qlPsEkhqqy6qXkz-cMzFFUspw0QHkd-XZ7NZxZ-8AJ74ejWjhOZ67ntuzKu0ZX2mEIKSgnN1HSiINffhDW5JuVDNfnMUF8rE2fyB9Hpzy4E8MSoxuHkCqu4jCnMq_7eqAieItX7tgLh9u9vJGslejN0UhhOY_i5YXYc15ZbYrRYNcvHjhwa0phVbj5oDdqK7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.2K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 02:39:50</div>
<hr>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نه آقا ببین ai که حس نداره، نمیتونه عین انسان حرف بزنه بخونه
❗️
🤣
همزمان ai
⭐️
مدل جدید تولید صدای Elevenlabs V4
⠀⠀
‎
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 962 · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FeO1dsjswYfB7Nmm01tFhPttjXzu6d-keSuZweiaFhM5uEdzJlVL8hvq5811nXGOC1b3EJiujBEHBbEZACaeOsYmQOKaQ5LANEIoiEuyixusCFoAZmlxqsD64rmbnTWanvmRVqQl2fqBWmEZ5QLL-JQRgoq_LXZUBe24CazOUbyBgW366jVhigsG4JuoePWevn5EqLwyb6RvgqxURMN1iKwWFN42Gu__tZGYPSSJrwhyunWvm6BHcLcZW7_w1coxlvNTkw5vydU6gLDd-4yfzgWzzxnp5Vl5jCtaGnYW1CPBlhhvpbUNafE6UiigmmLbmWpPSSo5IYgHw0G8mqvaTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/scpubDov3SvdXlIDAGKCuIEajnI3kFuqZ0SnDthU1-DuYWzBPDvmTIOY2vPD4CSq7dP-S5keluoREmslghxIJqUQQJeJ7LjAdaSZNSgCMNFVFsf3BeRyUIY7i18abQmVLwnbZ-JdR59-SNfYdOeOV_Uv0FoAeFV2m0_7mn1wMTZlGemkVytpF858f12wvRu0aASe-ypxReihpFG-5epcG8wtfQkuU-UtM4dP61CfGRHL3v8NL-2865PFPG5Kv0PWM-kKRQ_DXLUQujEYnPX8pXZCVb-u_dbU9cNM2zEp67HwTHsfNC6kIBoUPL4P0scaKbxAvzBYsu7RDkcx5_ZzAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZkg4BkdZT_aj0CjjJNy0mQRaR1q78fbhNAUbgTF_O-K_peXo_Xrctlj1NK-gFQdLqjW_aRdvIZJmqZ6raNqO5JReHXNUOtq1syyF79qNVCp3PoVDp0p9i2sr2NJUEM-HnLeZML8kbLFWbVTQyFtH_elqEffx9qT2cX3-CjO9aHRavewibxpM10EVUZH0APv0yuodVymXCOeULdqRJdoc7QXJJa-J-JVCWy845hv4a_JjLarq53mImylptolOHU_6uSjBsrhVyswolX0ZxO8ZO39sh7DJcDnmJO6UtBl13FSpOvCfoaTv2LGHsDmA53T68tlpzqIIzgvn0Aqpz7rsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p0m9nE-R63POwXYnhnwwRN-eva2KJhzZBSZ15MPrAjgMVlVTpmcfm9ItTPN1yVDAjKXwSz_T-GZidjSxunk2Pf2Gk6jhf-YlqehJD4X0N9Cp5el2s_uo_mmkBbVSbb-2Znrnb_sOSks0fNcYG3h1vtV30kxi9HLf0uU2UAkRuZH-cQBLIc8KzCWr_kBEwXd_-5B_-xrnEiuon-atckPwUVoqEzUCEIP0AzgoI-5aGDM-Q0NLES54V9RG9Sj92kE8FxnvJFwRdme20rMEHY7wn7xTfC_oOnKCyeC0TVPqZx2H_AQrEmIpIH1SuWe1MSpmLB3n5gVcg_w8APFpKdP1pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UB6-89DKUAYEDOOA_p5ROhXRGp0DR4aT07I4LFvxqdXN-X9GYGMD-0imeVbQYL3S94vQtDOG2hswpYnF_WpxpOk9pWbwXJfAEm5sTTcQ0_MxZjCJZz3BhlthPwnZEmlxpJ7O9_SX0Lji0d_lYgslGKftTLZvylEjNiumjyvthouC6XwXY6YHpX-kQlBpPemvcurRuR_HjrZejyiaGhCCmc9o7EIB4E_eQUlHLkWB9SyWWlWtvZ2XEGp8lYOYoB-qd8EKbRYgzeSfMOqddC8TqTzoRglK06sr_mcEzYLUxEgXSAwTg5nN_pr1I3ihDQS6xwCP2bgyXLHEzml9GvQ1dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQyP67oGi0jB1krn84buOfC4R49pJMReM0ryJYfLMyeaHDHAevwq3Vc1Wnb1qabOscSlNkc_pPTLWyIPbLJ65DDv5AifVHiWGRzXd4qgNQVO_5prkcaOMwWT-mDRiM2uiuVGojzmeIsGnr5SWSDgqRpgNpoAnRWT27JhKBKoalf-iL8ZCGXRIdynCtuC_IV44N_OUqemdiEQ6caGEGdO5kBxxl41ps2BjgeWczxwUh5k8kgl7IUStLiNR_iHrfSeKeAFW1LEFhymIYAMWtb6W0aGol4k4arcD8wNJk7HnRxsJ0QlD49tFefaKNjldRuZBN_Fjk9VCQ_Km6rZNGBJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AbB0cLYc5ecBLMJr_ujX8IJTRTHam9GlMAkZex0qDqj9E9WJMClMAAJQGj4u8_6Z69pvFSMhm8pJexQ1fBFPUoPEiyIflUegonDUw-O_F-0ifhBJx0xDNWQ8L9RQ1VOdHUDyA72Z0Y7Pygud7uiIxwYbPRcCzabhVf0I5JwoYFFkHdU8-O8V09M1DAkP-QknlQqtC6RzvZpJgWb9gO7eBUnGBnWLhrhSgnDi8DbIiVviDeMi5TPLpwV3xpkeOUD-AEU22Wa3_TBJR8oeI-t9hZRtmtaWG5Y1u1N-O6DTRrfoiVdpU589ylpk8MBz0FwsDQaR8r-EFI_BDWie4CxgcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_tul3zJnAvI-vmgIQWvNn2keSTlu_1UYtZoGEdtn2pMGEJUmHde4WCsX075gDX4El_1kq7Ds8zcMqcnIZBceAy32tAjEsIWufHJTUZdJcZqdk34T-njzZ6S3l62bGRo8recWZmmKskA0KXTy8LP0S3i_B83gTGEw9Yi0_BSl3_jbMAkYZDTGPFzPJmmACNaMeyoKjQVP_xDneepB8OpE-ySaPGkB97ao95h7gxpvbF9bYoJMcp4nhVMudUyLRibh-MwgBSUjNxWfjbKFqxA36v_O-wsgmDVIstJRm57qK4zHI1pwA2oLc90lFWR26h5othk7gpGlKP8og583lrWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/khG1QPRVnOg56EOjyaXFyjuIAsymPXgqRriFNQtHr4yD8bxoj8r21_5zYk3cFfcCbjz29AYSx9hMbTeCz2wcEs9jsO_i1Oq1M2YXk4UYwsJWq38_wv9G9OL4qTgsKbgc8DDTEnMdzRJ8YWpHEmagso4cR_gquS6YLQBl8zlMCi7lKWeYJcDj6hjL1o446waunLyJs45kz1rGyeZAX_YzrRkVGCru0PlpDvxRR8-wKaIlyEoXAxO_xAPVsWSykHuNenmnA4El87fmSoevNEMEcXxgcZZDgH9j0RhRH-y2ANLEUfl6HkGPxRmm9YCMuJOPKG0ayYgoDA0C9IPlAhahFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نمونه هایی از تصاویر جنریت شده توسط نانو بنانا 2.1 و مقایسه اون با مدل های چت جی پی تی :)
- بنظرتون نانو بنانا تونسته به چاتی پاتی برسه ؟
😁
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 943 · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epw_ri6cxGd7selU_agoRJXFsTHX51-8Q0Y6XmHs5RMv8ohBBBynBqpj4FOu6CQAhCse-B-bMk7YfTVhkaSOZN5PD-qtfTn6dDb3BAJ8DfA9ScLe8Fg38sQ3COLOKGs8z5jTJ0JaeA6BmhBPD-xH2duXkmOYedbF-OEM0PzqPBlMV0TXVZq8DUi2ZSxibh2OF9-TZGs6Z2UjCR0pxgBXJYPxzFaQ_qMExbD5X8IeiKTZGfoDugQ0feRvjWCj-sQE_ioIjjIFGtYqCqNXHP-r2qVTvNmOh98Dd2n-Q_AaspOS-z0APIilBLusN17eZQ8LDlstkF9jKHE86BrmVgANPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
✨
بنچمارک مدل Nano Banana 2.1 برای ساخت تصویر اومد
‏به گفتهٔ منابع خبری، گوگل نسخهٔ جدید مدل ساخت تصویرش رو بی‌سروصدا منتشر کرده.
💡
به ادعای گوگل، حالت Thinking توی اینفوگرافیک دقیق و حفظ چهرهٔ چند شخصیت از Nano Banana Pro بهتره
‏
⚠️
هنوز ممکنه چپ و راست رو قاطی کنه
‏
🐞
موقع ویرایش گاهی روی ژست تصویر اصلی گیر می‌کنه
‏
🔤
متن ریز یا خیلی طولانی تار درمیاد
‏این مدل روی Gemini 3.6 Flash ساخته شده. به گفتهٔ کاربران، توی اپ Gemini‏، گوگل AI Studio و API در دسترسه و به جستجوی گوگل، Ads‏، Flow و Stitch هم اضافه شده. به گفتهٔ گوگل دانشش تا مارس ۲۰۲۶ـه، ولی منبع می‌گه عملاً از ۲۰۲۶ چیز زیادی نمی‌دونه. گوگل هنوز پست رسمی براش منتشر نکرده، پس این جزئیات رو با احتیاط بخون.
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 951 · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Izv2GD3xj_nrwhnVAJk59YOY9-BNtGNDlIcWHqH1BP43mfXxYIFucjQdSEPDoDAa0_xOMAFbdfjS6bcRyzlJOdndlk8KK4J1ebft6SINoNsnIPqOUhUb94uX9s1ou78MVOr12xozFSt-HvmY250aQa2tO0itnqyAJ_sDJIozcSmvJFMIF86kGdr9EmYVIJZdrDwFZaFn1mKnm04yyqXKjgyThyeJ9krBA5CB4Ta0ijz8thZDUOyW9WpnbPCAwBzLg9RrCf0h7b8klGiV2y4drjHrlpsjDzVhe-macNqr9Fa7ktFlKKN2_UD5rNLIZuknHmkbhkTtov41bwHCDcYnpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F5euQFBjZ1GUZv-3owXEo0K1mbvuc3JwaWH0sE-2kmmU3QQmSkZDQ9-st1juMgHphi_X9GDbMwSgI473znSx22KaGEbw-LhMmrj_4at5-mgPXCjX0Uycwm1pOxmL7DkWRnznw64K1vZVSy4hb6fhQWdDZrX8-fCVsW1tiCsePfeahLdV4QUw5WJ5gqy4B4wpMK4mvNpDKlVkeJ2J65l9zdyYV9YEjE4abVu_nYHdkEHlCjc5HSXw2QZ8pGcw0aow2XCN9oXtI5wxGsthKv-vKErKFus8HFZdByqtk-HxjFEOUNEXxZ9urFzIxH7X4UcDA-p8kWMGeTkFGuXU2heYWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚖️
وقتی هوش مصنوعی خاطراتت را لو می‌دهد
‏
یه زن تو فلوریدا به Claude می‌گه می‌خواد به دفتر کلانتر حمله کنه؛ فرداش پلیس در خونه‌شه.
⠀
‏کارلی میشل هلر، ۳۰ ساله از فلوریدا، ۲۶ سپتامبر توی چت با Claude نوشته بود می‌خواد به دفتر کلانتر «حمله» کنه؛ فرداش هم نوشته یه اسلحه‌ی جدید خریده. خودش به پلیس گفته از Claude «مثل دفترچه‌ی خاطرات» استفاده می‌کرده.
‏فیلترهای امنیتی Anthropic چت رو پرچم‌دار کردن و بازبین‌های انسانی خودشون به پلیس زنگ زدن؛ زن بدون مقاومت دستگیر و به اتهام «تهدید کتبی خشونت‌آمیز» متهم شد (تو فلوریدا تا ۱۵ سال زندان داره). نکته‌ی مهم: چت‌های پرچم‌دار ممکنه توسط انسان خونده بشن و سیاست Anthropic اجازه‌ی اشتراک اطلاعات با پلیس رو توی شرایط اضطراری می‌ده.
⠀
‏
📌
گزارش Cybernews
‏
🌐
گزارش TechSpot
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/io26Ha5xayvtkr-MPvPcMJXzitsQEbcq-TIDoxfa9V5eT_YEz_P7pFwW0OjWpFxNKUPyp6bHTJURJqwr50S95Fj6A0z_VkyuNxOmlny0sBNjTX8JaJPev9EA1QrRdVAacjGlyyFiNsKhW9xJOWFwuHEnfSx526wcOKwb-v0zUV0HqpsY9-baS_1lw_AbIII_qquzZbFXr8LbFleRkZ1G_epmI5KGYBCLGoCAHT0SyWXbGUd-w50vk-g-xUUCMess7hafVGKFMaVGjSgR0o_-H1IV8QzQzYEqZgDXOFuG58ZODKJwclT-4wXHlffvSlnL9sp5400TYsSwTXfLR0wKJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🕵️
هوش مصنوعی رمزنامه‌ی ۲۱۷ ساله‌ی ناپلئون را شکست
⠀
‏یه نامه‌ی رمزی به ژنرال مارمون که ۲۱۷ سال هیچ‌کس نتونسته بود بخونه‌ش، تو ۶ ساعت باز شد.
⠀
‏این نامه مربوط به مارس ۱۸۰۹ئه؛ دستورهای ناپلئون به ژنرال مارمون، درست قبل از جنگ با اتریش. خط اولش فرانسه‌ی ساده‌ست و بعدش ۲۴ ردیف رمز: ۱۳۰۰ واحد رمز با ۱۵۵ علامت متفاوت. کلیدش هیچ‌وقت پیدا نشد.
کارتر چرچ با GPT-6 Astra اول اسکن صفحه‌ی یه مجله‌ی فرانسوی ۱۹۶۹ رو رونویسی کرد، بعد رمز هوموفونیک رو با آنیلینگ شبیه‌سازی‌شده شکست؛ کل کار حدود ۶ ساعت زمان مدل برد. حتی وقتی متن‌های تاریخی ناپلئونی رو از حافظه‌ی مدل حذف کرد، به همون جواب رسید؛ یعنی رمز واقعاً حل شده، نه حدس.
⠀
‏
📌
گزارش کامل رمزگشایی
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=GV5gmtsqjcBJJumkP4R13yggK-7IAKFv9HYzAiIB0EItlqkByFNYPGruzGJvkL2pCsJBi26rRUZo-QxVx5vjd8WisHxiwEf-HDLyHn1hqCKqh2-Yp_efyhWNuW9Mb0W-JlT0GaIgnT6ee3RcQ-9z3Vn4DLQZX3E3wqcypMeecU_-7Q0yJKXHFwUSieuJgKcq55JTTgzKHiSQFPxVa70Et1xkmKVesJAF7TNZe0mX1Q52weIGaY4Ze7_AuKqQPHBTJQjT9FGnqFh7LLF_xh5wPeFHKGL5B7iv4c2t6YKzfKvtFZqM_Jh791CCW4qU2QSwQcEIaEk34ilZCTgRroApMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=GV5gmtsqjcBJJumkP4R13yggK-7IAKFv9HYzAiIB0EItlqkByFNYPGruzGJvkL2pCsJBi26rRUZo-QxVx5vjd8WisHxiwEf-HDLyHn1hqCKqh2-Yp_efyhWNuW9Mb0W-JlT0GaIgnT6ee3RcQ-9z3Vn4DLQZX3E3wqcypMeecU_-7Q0yJKXHFwUSieuJgKcq55JTTgzKHiSQFPxVa70Et1xkmKVesJAF7TNZe0mX1Q52weIGaY4Ze7_AuKqQPHBTJQjT9FGnqFh7LLF_xh5wPeFHKGL5B7iv4c2t6YKzfKvtFZqM_Jh791CCW4qU2QSwQcEIaEk34ilZCTgRroApMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sYN5NLq1Y9I-cRl7ziELdZOO0LxGcGpxU25xEpkSwn5b882mpoO34Tx-wfSys3PYLq-e0T9zrx-OZF4rjmhc2uIOoukLXJo6xZ00b7bGR_e-h8QAfoH2XUQnrAcjEPc3dDTE_xzRutlZL9_hVpTwgBERgC3ncEM1llzvVplzCqirM37EA43OwVXtEO_mC0kcWudNBFSm71lBuY1aq27bXSsHeYOVfJ9LwxTJhCHjBggbUf5ThKBo4VY9p2USLUDAiO70P-6dO1SxVRkeReqfDnpYewaCQEj06S73nJCWPB0t568D_Eq0ZzhxoESQM-slkwmmw0EuLYymYBZx9yRwMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sA7mkVRUXCBhmH-HPpBXoZdC0Ch5Z88KvxFgCtfPzdk13XqfzboRCEDiPE5hSOMlFHzJK8hbokxtXxzcS8i-y86QSnRUXe_t_SfOVrs5nl6nJivR5uNE3XMOMV1ICHgBeoBJAjgMoUrp7KGq_WrH0nEf6tD67zoWvkUgK89NupzRacr7ornv1x_QEi0l2Gu5oylatXLyY5LpWQtz8NgibR_qqudAPeMH__fK1ZiP2CRBnxGk4E0JTAcFMz65J1RXe1tPI5uW5Ld0hLGPGZTJq6W8SFu6AfL4i-KhCx_OKXtpHWXrAShir1D4am5mRe0jH0_Wl653jCtVskCTMJV_pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kxMyhglNPmIkexwto2DBhgG3BDZbL-y8hKPmTpC9SlsWfn1hZcsVT69v2eHhEVlPYD7AWBgCJyLDgDpORiqerohbDJEsu6g7zSrjnTz7XOsimGYPPS9fVJ0sIQHIBN-cOY_sGZzYS4DxkA918MBwv37r-b1XN2zQsZY4yRdgkgNgYxErTSr5FU0bKAGNCxR0O74BF4SPiz37nait28oq5aWUdrXI88vnWXjk9yLdwaeJoVTE_0e6rWzCsNrMJt8nkgvw3PQQykYhnmZqQ6WRiqe70F4UiOfXL3Je6jCYFBpKTkp4dOriY9Oi_zfSNvLSB9eOW46fMMeeBlT7DTV0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7li7HQstMhALObMV62z5ey2GP-XVadNhXh1KbWpohjsO6Mevf9dx-xEaBcismOI0m5Vh8g6S_Z5KxOIA48zyEnX7XRRVKAd7FBe772dwkvxD5yJQCkWfMe-mpxcRRrldkN7ryv1VLuGcxObouRokUnNwyLn7PUJ7nbLLXfEw-yy_ONayDmLJSm4ygqp9vYfRMH9yzT4jSxFKtepx2W7C-PinXtaQQ0ZgAHygQLIRlYs14R-U-1PG6vHZHn5xkhRXa_shFUfjuGbJlgX8f4zp5I_ZbkKNnaSfdJnGbWMj_Xv7cCNsBwMSAa98BYBLd1Ngq-ZcesVwfgZStCAMXSOKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GeWFAHUglFCvskVMZ17DrPBhmwMgn4ra1dXkC3wlWdVfuuJWoqNYx7lIuWWOHAuDHfWPOfwbTdt-UbJPV0JiKr3CFy-cwG_ZQI-y0uS0ZTE_3e8tALobt4SoEXhb7HoZxut3xMpRWh0Y-FF3e2DrOOpVSZ4MzX3infAAI6RL0HFdQ4y-3QqP1A9udFm7iS9aOIzV5DwaYJ-kHDsL6ZAq1bI0-nfCDlA1QvxQQAlwsFStTsH1T71e-A2Tm9ccCT56p-c6MlHSBo6kDyRwT28VNTEvKGrMMlbvp7rn9wB7-MsstZ9N5ZDd_vGIR83AKlOy0iqbaMJLwFhbuYbcWTvo3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🎁
فهرست اعتبارهای رایگان هوش مصنوعی در یک سایت
‏این سایت پیشنهادهای رایگان، دوره‌های آزمایشی و جایگزین‌های مجانی ابزارهای هوش مصنوعی رو یه‌جا جمع کرده.
‏
🪙
اعتبار رایگان، دورهٔ آزمایشی و تخفیف دانشجویی سرویس‌ها
‏
🆚
جایگزین‌های رایگان و متن‌باز برای ابزارهای پولی
‏
⏳
مقایسهٔ سقف استفادهٔ پلن‌های رایگان
‏
🔍
مثلاً دورهٔ آزمایشی ۳۰ روزهٔ GitLab Duo که مدل‌هایی مثل Opus 5.5 و GPT-6 Astra رو داره
‏خود سایت مدل رایگان نمیده و فقط پیشنهادهای بقیهٔ سرویس‌ها رو فهرست می‌کنه. بیشترشون سقف مصرف، زمان محدود یا شرط ثبت‌نام دارن. به گفتهٔ خود سایت هم این شرایط ممکنه عوض بشه. پس قبل از ثبت‌نام، شرایط رو توی سایت اصلی هر سرویس چک کن.
‏
📌
سایت nopaywall
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVzqBpbdvGPvLQ5dYQRLy6mHyZL_qnk1T5RYg5ARzWtq9qitGzjTuAQYRVBx13Fj3Xp62qYbcYI6g7qO0W5vvPyrX1fdz40eosratR6f-ZBFFWmqO51Zr3YLkubMHKsxn14h0ZeewisfHbFAByMzoSfO13C916eWnCzWn0IDb3RCXrX58dgTl3tPN6T7XUnQx5oES7jtAz7EtlmwsYh4LZ97e2P3kdd-gdr2XDdl3qEpVzyz3LZ-aEUdEOqO6VaWD6du-AF2pmg5fePUHMkTcb3gJrUPrr2SWSjtUTs9kaHliNgCIChXqdoa-JiAGuyV-EwBZs2b52K2EhlJ8lfRCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚀
تبدیل هر چیزی به PDF فقط در چند ثانیه!
دیگه برای ساخت فایل‌های PDF نیازی به نصب برنامه‌های سنگین و مختلف نداری!
🤩
ربات همه‌کاره ما اینجاست تا هر محتوایی رو که براش می‌‌فرستی، به یک فایل PDF تر و تمیز تبدیل کنه.
✨
این ربات با چی کار می‌کنه؟
📝
اسناد و متن‌ها: فایل‌های ورد (.docx)، اکسل (.csv)، مارک‌داون (.md)، متن (.txt) و حتی فایل‌های کدنویسی.
⚡️
عکس‌ها: یه عکس تکی بفرست یا یه آلبوم کامل؛ ربات همه رو توی یک PDF مرتب بهت تحویل میده!
🗂
فایل‌های فشرده (ZIP/RAR): آرشیو رو بفرست، ربات خودش بازش می‌کنه و محتویاتش رو توی یک PDF برات ادغام می‌کنه.
🌐
صفحات وب: لینک سایت یا مقاله رو بفرست، نسخه PDF اون صفحه رو تحویل بگیر!
👇
همین الان وارد ربات شو و رایگان تستش کن:
🤖
@Everythingtopdf_bbot
━━━━━━━━━━━━━━━━━━━━━
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QWFKte0T-f6DRBaPO_eahE3y_sm7aqPKVWyyjs6wggQplO4kObr_lDu9muKdayYnxQ3NWJ5iG0AhfyFxiJ0_gI5tL_Mxqp-yEEyeqFfL5zCr5OEIvlixlEwFGWpl2tJhzAJUi2zB3KP5OyVYH-uO8QQNJDoewmW7E6VUnF-pIulKwjTxz6oh9_RwiUS46WNqm4kpWXVE0Z_DFts_N1LpkZLQ6w-FqhZxMWgzj1RtoO9hJC-D16kpxYzcsjo0jN-zthWHwFm3uc75oCjhn870KbUbGRidh6V8VWqKCqpXu-YQWml7wdCjktHXcZcHTX43wm0x8h-RpWo8vp-gG0rNNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎨
کلون متن‌باز فتوشاپ با Rust منتشر شد
⠀
‏استارتاپ ArtCraft نسخهٔ متن‌باز فتوشاپ رو با Rust منتشر کرد و ۶ ابزار دیگهٔ جایگزین Adobe رو هم وعده داده.
‏اسمش PhotoCraftـه و روی گیت‌هاب با لایسنس MIT منتشر شده؛ حدود ۱۸۰۰ ستاره گرفته و همین امروز نسخهٔ ۰.۲.۰ اون اومده. با Rust نوشته شده و از شتاب GPU استفاده می‌کنه. البته هنوز نسخهٔ اولیه‌ست و نباید انتظار پایداری کامل داشت.
‏نکتهٔ مهم: چند کانال نوشتن «هر ۷ ابزار منتشر شده»، ولی طبق سایت رسمی ArtCraft بقیه — VectorCraft، FilmCraft، LightCraft، PrintCraft، EffectCraft و DesignCraft — فعلاً فقط «به‌زودی» هستن و نسخه‌ای ندارن. پس فعلاً فقط PhotoCraft واقعیه و بقیه وعده‌ست.
⠀
‏
📌
ریپوی PhotoCraft در گیت‌هاب
‏
🌐
سایت رسمی ArtCraft
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L5Cqc9LmXL4PrLHfKreWOn8kV7pTPj4DL2W_Lz1NmiUlB6JKVbSdRSXzkA4x0WbaaaapRFwLjFHAc_QGLF3QvdCiDdx-2lC48miQsJTZy-0y2QPTrWHsrKKy7F41473EyJlvFik50ufm3s515uCfmVLuvRZdaYfx3BBq6tWQIJZMieRNsuUqzP7uz-nOj-4cFOjZKhSgh5SlszEn_5uaQdWjPuC-qwoEy_z2Oo0oDxAsMwRPqhkh8MNDc8Brx-_fDFrAWPOc1e7LfzavISxFwoccHB0YI_RW9VwJUyJ3WYhG_C_o7JT5RpFWzKflFGJvvERhrRy8KHIZxeD7dHBYmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚔️
هوش مصنوعی بدون دیدن صفحه وارکرفت بازی کرد
‏⠀
‏مدل GPT-6 Astra بدون دیدن تصویر بازی، در چهل دقیقه منطقهٔ شروع وارکرفت را تمام کرد.
‏⠀
‏به‌جای تصویر، بسته‌های شبکهٔ بازی را می‌خواند
‏خودش ابزار ساخت، مسیر پیدا کرد و استراتژی چید
‏از یک باگ نقشه هم بدون اینکه بداند استفاده کرد
‏⠀
‏این کار با فریمورک متن‌باز agent-wow انجام شده که هیچ منطق بازی به مدل نمی‌دهد؛ مدل خودش سیستم ادراک ساخت، اطلاعات مرحله‌ها را از دیتابیس بازی درآورد و با برنامه‌ای که خودش به زبان C++ نوشت مسیرها را حساب کرد.
‏⠀
‏به گفتهٔ گزارش cnBeta، کل این فرایند فقط با یک پرامپت Codex شروع شد و سازنده می‌خواهد بعداً ببیند یک ایجنت می‌تواند به‌تنهایی تا لول هشتاد برود یا نه.
‏
‏
📌
گزارش کامل cnBeta
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h-nDTUc5dBWUJwA7USbectwTpxfVtwkj9WZ7IyBN_OZCVygpUOlZSUl574-qTGh5Ca6XYUpokTndSjNDB_WYwCC5lQTqSNhaR8L9NlOkjgJuED8lBqJklbxTOKml3wu4oQBaW3I7xFC6Tol0bih7SWY6g3fPPWNKFjadhMkgKyYz59sxJLKr5WyudD46ifVa_WV-pKFSo9kWcUM4I0l4aY48vtb6QnaoG3zCujP_30c4TmF2iQz1SMfHli92hJGIU3gNK0lECGJ3TD6JSenTmO5HwrxJPSMDjkDlPxgjL2QnXfEXhFW_FoLECOISzy6s1sru_WKflu-XLJlFcpBHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔍
اسکنر امنیتی هوشمند و رایگان برای دولوپرها
‏یه ابزار امنیتی مبتنی بر هوش مصنوعی اومده که بدون نصب ایجنت، آسیب‌پذیری‌ها رو پیدا می‌کنه و جایگزین ارزون تست‌های نفوذ گرونه.
‏⠀
‏•اسکن آسیب‌پذیری بدون نیاز به نصب ایجنت
‏• تحلیل و اولویت‌بندی یافته‌ها با هوش مصنوعی
‏• کد اصلی پروژه متن‌بازه
‏⠀
‏سازنده‌ش می‌گه چون هزینهٔ پنتست حرفه‌ای رو نداشته، خودش این ابزار رو ساخته.
‏برای دولوپرها و تیم‌های کوچیکی که بودجهٔ ابزارهای انترپرایزی رو ندارن ولی امنیت رو جدی می‌گیرن، شروع خوبیه.
‏⠀
‏
📌
ریپوی گیت‌هاب
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده: ⁮⁮ ⁮⁮
🆔
آیدی عددی برنده: 2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل: @ArchiveTell…</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel | BOT</strong></div>
<div class="tg-text">🎉
برنده‌ی قرعه‌کشی مشخص شد!
🎉
📌
پست: «قرعه کشی شماره مجازی»
🏆
برنده:
⁮⁮ ⁮⁮
🆔
آیدی عددی برنده:
2045284340
⭐
امتیاز برنده در قرعه‌کشی: 1
⭐
👥
شرکت‌کنندگان: 51 نفر •
🎫
مجموع بلیت‌ها: 97
🍀
انتخاب کاملاً تصادفی انجام شد — هر امتیاز یک بلیت.
📢
چنل:
@ArchiveTell
🆔
آیدی چنل:
-1003718102196
🎊
تبریک به برنده!
🎊</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قرعه کشی شماره مجازی رایگان
✈️
🎁
جایزه: شماره مجازی تلگرام
📌
نحوه شرکت در چالش:
1️⃣
وارد ربات زیر شو
2️⃣
یک رفرال بیار و در قرعه شرکت کن
3️⃣
با هر رفرال شانس بیشتری دریافت کن
4️⃣
در نهایت امشب راس ساعت 00:00  قرعه کشی انجام میشه و شماره مجازی تلگرام به…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">قرعه کشی شماره مجازی رایگان
✈️
🎁
جایزه: شماره مجازی تلگرام
📌
نحوه شرکت در چالش:
1️⃣
وارد ربات زیر شو
2️⃣
یک رفرال بیار و در قرعه شرکت کن
3️⃣
با هر رفرال شانس بیشتری دریافت کن
4️⃣
در نهایت امشب راس ساعت 00:00
قرعه کشی انجام میشه و شماره مجازی تلگرام به یک نفر تعلق میگیره.
📣
ری‌اکشن بزنید و حمایت کنید تا چالش بیشتر بزاریم.
🔗
لینک وارد شدن به ربات
✈️
@ArchiveTell
| Qorvhex</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYjoVpK2z1o2f9u2ryUzKrEzp9M_QbSfL75wi-fjD9Be1MP44ypvwtIf9LISkSH3XonCNu50kOehCr54hqHr5AGF2Q-ZPHbEqE9wKZWIhz1AyLDp6EROtKFBQhONr6TT3Utp4-SFYMuJa82-kth6M9b7RpuKY49BpSHZ56Z6q6DX6IOOBGjOMHWhxElkrwqshRmCJA77ruGpxnUSLVnHernQAS6LoQFH7EiqfPKbhinUoSr_EGXnPwTRi98mtVu34aTI_6na7aBRHsT01dIFtKwblhZmzZO-z2nOP3hw-utPZsOHy2UVqjxlEXmLAqWaP9Ywy0RtGdMOppdOY6CSVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQALhb6AB1z7eTHmigd3CWddr6Uq0PJQJQvzBSaFVeo-hPbt04N6L9Fky_lpDNW6OvKPJIaOQw7cch8UgFXTA5G6vPGnW0iufFFu0cBFDOwx-F8ZgpKNVxicPyXXRVRD4tf4Ee5PmnMx_zFr5Syw8mZJMwktLBO8x78qH_t8h9mFMhMjs2XIJrCUtDUKFrFigh0uaI-JtqoumNsGKF-VRANFWlQ00TYdnDsoitObSMOlljxq7PPben53Vfbe1b6X8W2xQ-W-AlsIwVosegrZ3ygwpVLLcyJZY8SzzY64hQGwxO7ND0RoVnSqVALNgctT22wWP6Ygk0awkzfa4xO4FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📥
دانلود راحت ویدیو با Yoinks از شبکه‌های اجتماعی
⠀
‏این ابزار متن‌باز به شما اجازه می‌ده ویدیوها رو بدون تبلیغات اضافه و مستقیم از آدرس صفحه دانلود کنید.
⠀
‏
🎬
کافیه آدرس صفحه رو از یوتیوب، اینستاگرام، تیک‌تاک یا شبکه ایکس بهش بدید تا فایل اصلی بدون معطلی روی سیستمتون ذخیره بشه.
⠀
‏
✅
چون اجرای برنامه داخل ترمینال انجام می‌شه، فایل‌ها به سرور شخص ثالث نمی‌رن و خبری از تبلیغات آزاردهنده، پاپ‌آپ و تغییر مسیرهای مشکوک نیست. به گفتهٔ سازنده، بیش از ۱٬۸۰۰ وب‌سایت مختلف هم پشتیبانی می‌شن.
⠀
‏
📌
مخزن گیت‌هاب پروژه Yoinks
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsNAx8Wam7PFbwAEUVTHknvirBSLSUb2dTlvecw8iIpPepmpozrWescm-kzLWRX6YM2ug31P0WBcAVajWYZq2Zx3ivtdwaXcKjpzK1YMCR-qGJ4aj9e-zF_TWmayk6DeTNxfmslQvGHQd_gtLbGJ7dEfyt_21FdbSaewilNJASybSPkzAoQ_xIay9prgpe3jkA1-xgfLrjePURXiOpCFgvLDl-RXncJLDUo6veMHIhuzDjN4RLBoSY1oI3sKIEJH5FjG4PwuZ03AQz3dq5iiAq_d_QxvwxVFa6UxIJtXQIwcSi8K_QyvNR8KkmN8D-BD91ZznPJVVi0VLjbhciBiPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
ترفند فعال‌سازی Opus 5.5 روی Gemini Pro (آفر Jio)
🔥
اگه اکانت جیمینای پرو رو با طرح Jio فعال کردی ولی هنوز مدل‌های Opus 5.5 و Sonnet 5.5 توی antigravity برات باز نشده، اینو انجام بده تا بیاد:
💎
اول یه اکانت جدید رو به عنوان عضو خانواده (فمیلی) اد کن.
(دقت کن Sharing رو اکانت اصلی فعال باشه، و ریجن هر دو اکانت یکی باشه)
برای تغییر ریجن این پست رو انجام بدین
😱
بعد با همون اکانت جدیده لاگین شو.
تست کنید ببینید براتون فعال شد یا نه؛ تو کامنتا بگید
💀
👇
⠀
‎
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwXTnPRn8Sa9YGIxFjRRG058texLwCC9V8TnV8MRFfMi55JioErNEJgSCqZvxtQxxVXpP7W7xm-GyMONBHO-cDYOEdhgf_o13PsH27-YTlv6TOxLy1FnrJ2SPFwnYg3jEX3c2LrUh_gW-UR8F9gPDH9EoFBtm7vJfVYhd-resbN3d3O6I6UawmkwHRyujh8eVxHjUcdL0wY4aCYHRGzhCNzgqSujudQeHgGZlp6HfxCxiOTaf-8vQ2Y_0RjTyU-8oiSIBRAwX1y6p8wIcD6FmWYzgIrpJCb1KIzESuBTBamvhBMWmttEparmyZDHp3avhhze-Xq8-75LqY4GmP5UVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QWshti0k9lpA95ijfucIlTMMu1IJKzamTfb5OVmA6fzbqWwT87IxGYuUYziQTw_kNj6dO_bxwYlBM0fOxIXpTL_fx8N_kcO-1utKJRsJA7_bpGmI7HHJl63hr_-Qv3FfIT5MhteTpbDNAzEfXjMNAF5SoRcnVr2brlvboXe9Cb7KF26Q9-XhEMwsMfQYFnYQZIIqSmk9wH3gvnZ-D0A84J7C2mXqTNsPTg5N-MoM4phS_NCKCGdIBvUBJKpiAJAjWyAkybUm7iQcQ5R1d31kexG9Nut_H-_E2NmgCKEz52Y0lhz9xuK-DGrEYsNyP-ewk9d-I5uJzY5IiWxvT_ojTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
☁️
اکانت تلگرامت رو تبدیل به فضای ابری کن
⠀
‏یه اپ دسکتاپ که تلگرام رو به یه فضای ذخیره‌سازی تمیز و منظم تبدیل می‌کنه.
⠀
‏• مدیریت فایل‌ها داخل Saved Messages و کانال‌ها به شکل پوشه
‏• پیش‌نمایش، پخش ویدیو، همگام‌سازی پوشه، WebDAV و REST API
‏• ویندوز، مک، لینوکس و اندروید؛ همهٔ قابلیت‌ها رایگان
⠀
‏برنامه اوپن‌سورسه و مستقیم به تلگرام وصل می‌شه، بدون سرور واسط. ولی دو نکته: برای ورود به api_id و api_hash از
my.telegram.org
نیاز داری، و فایل‌ها تابع محدودیت‌های خود تلگرام‌ان — پس «نامحدود واقعی» نیست. نسخهٔ ۵ دلاری فقط تبلیغات رو حذف می‌کنه.
⠀
نکتهٔ امنیتی: اطلاعات ورود تلگرامت رو فقط توی نسخهٔ رسمی از صفحهٔ ریلیز گیت‌هاب وارد کن.
⠀
‏تو تلگرام رو بیشتر برای فایل استفاده می‌کنی یا چت؟
👇
⠀
‏
📌
مخزن گیت‌هاب
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_7La3AAEB2zdvnkBxaXgQvA_FaFmOJuLxozYOUJ39xzZLvAPYFuCjaOyDSvi3l1ZPto-JeZEjWatMaIfSYoIi1EEMerbW9IFHmsXJHB-vyBC7i3Wvqd8GSLoRBC7SbbI1vurHqIVKZ0uTMjK4LA8bLn0_2Fk_lKpyvP-WheccjqUNg-85HqQkK8eU0assn_kNnD-SpZeElUhym1M6miAuuDHkfd1nvIv1mOhf2xfJjshp1drHk7tR4udFrbDG6tTfRvb8amWowO22sbgQiVIC_IWYimhqWG7FEE92W_l41BN8_FruI5vyfCpMxbKTbWWbJzDG4kO51a5yx3HhqiUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش
‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.
‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری
‏
💸
کم کردن هزینه با prompt caching و compaction‏؛ به گفتهٔ اوپن‌ای‌آی ورودی کش‌شده تا ۹۵٪ ارزون‌تره
‏
✍️
پرامپت: هدف، مخاطب، محدودیت‌ها و معیار تموم شدن کار رو روشن بگو
‏
⏳
کارهای چندساعته: عوض کردن دستور وسط کار و سپردن بخش‌هایی از کار به agentهای فرعی
‏تمرکز راهنما بیشتر روی API و Codex هست و برای کسایی که با این مدل‌ها ابزار می‌سازن مفیدتره. قابلیت multi-agent هم فعلاً آزمایشیه.
‏
📌
راهنمای رسمی اوپن‌ای‌آی
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Idb_j2O-uUSEOOygi1NLmCdCpvhjSeL9x8fucXf4YNIQ9etL6ZiRilCK803JvGGNZTlmoz4oWddlMP0Au5m2L-Osx6STkmuWW_XonCSCYPFihwxbwcqSP0Bmbxf5yNshnZa87hNMEUpSigDb-YBlEZevW6ylAEdqrXIZOcy8Rzq0onc_PhVlAnfx-vIIUV-IQt9xgCuIItg4W3vSwZVf4iiya9Qm_tbWN28sFaMILZG-O-ja4K38AIm9MW5vwVB62qxozLQbK_VP6r7pBjcXEH6WllxqpPuCkgOdJsNSwt0xoF7u3PjA_dbslOZYbr5CLi2HU4KZDv7mpko4RJRLTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚫
انتشار Grok 4.7 در اپ‌های گروک
⠀
‏مدل جدید گروک حالا توی اپ وب و موبایل هم در دسترسه و مدل پایهٔ همهٔ حالت‌ها شده
✅
⠀
‏به گفتهٔ xAI، نسخهٔ ۴.۷ روی یه مدل پایهٔ بزرگ‌تر ساخته شده و با یادگیری تقویتی طولانی‌تر، توی کارهای کدنویسی چندساعته و خود-بازبینی بهتر عمل می‌کنه. پنجرهٔ کانتکست ۵۰۰ هزار توکنه و قیمت API مثل نسخهٔ قبل مونده: ۲ دلار ورودی و ۶ دلار خروجی به‌ازای هر میلیون توکن.
⠀
‏
📌
یادداشت‌های انتشار xAI
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZ3AUAItfVR7LjaC6YpNB-5ven7a_5E87QQVal9byGh-mqCoqkgNpQdmK4F1iqxKoppu3EWj4-GrtZ956wpyLrQYgSTAt467EERwFY3UpuIBvFgN_phPa0CKLHCLUm4s-HStRzCbwVlZSpOYYk6rqGLJaxUbqgLmknSn0LaWTLzqR5nTrqi1_ieWvzlGus03vNl4TqMBcMzu3vkw5DCKVEPC4ckchtj1DYpzv3d3z14nijsO2b5QB4UeJnRZ5hhDAN_LuELwooaTedotjPnmH_qNcaZ1g7D4jlhyv3i9Peu4zuV-5sYfzU4f_5qtMqQ8-eK8dIze4AqBOREO-vOtjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان و ممبرهای عزیز آرشیوتل،
😍
ممنون که تا امروز با حمایت‌ها و کامنت‌های قشنگتون سرپا نگهمون داشتین. سعی کردیم به قول نیچه «با خون بنویسیم». راه سختی بود، ولی به لطف شما هنوز زنده‌ایم.
ممنون از ادمین‌ها و کانال‌هایی که با فوروارد و تبادل منصفانه حمایتمون کردن، مخصوصاً تیرکس نت. دمِ توسعه‌دهنده‌ها و همه‌ی کسایی هم گرم که تو روزهای قطعی، اینترنت رو زنده نگه داشتن.
تیم خفنمون هم که جای خودش رو داره:
احمد، که داره به مو می‌رسه ولی آفتاب شکوهش کانال رو نورانی کرده.
وگاس، که تو روزهای قهقرای من پشت کانال رو داشت.
«اس»، که با اینکه گوگل‌فنه
😁
یه متخصص واقعیه.
محمدجواد، معین، ایلیا و همه‌ی کسایی که سهمی داشتن.
خیلی‌هاتون دیگه دوستای نزدیکم شدین. امیدوارم سایه‌تون بالای سرمون بمونه و مثل همیشه با لایک و شیر پست‌ها همراهمون باشین، تا روزبه‌روز قوی‌تر ادامه بدیم
❤️</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyvzCgbDWzg7nLMe3n0c5iI1Sw4HSclNBhkiMoT0oS3luPF2mcGjPXdxQdx6n5Ssd0b1VSBPTA1ZwLxliJLpkJgKziluCGA9DftuVMtpOHrC0dF6vTGfCvi_-ZiMKi46d7ElYFZ30V-SeooRVvV_GkIEGiwre3RMtv-5WV9FAQOI_ZtbstBkOecVihv41vhpXZlMWbK9o6Kpcmalg8yryX5juBXEn0HYjjPOmxCw1FzVi0FBDvEpFbWx5UQdPetsMula4q1hQubn0DrMxSW5IkDi-bWehqKMzAeUoUbJdEzSiRPntWPWcmrCnrHpZuNmWSbJI8T4SAfBZV5HXArUPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کاربران رایگان جمینای فقط فلش‌لایت می‌گیرند
⠀
‏از ۹ اکتبر به بعد، کاربرهای رایگان جمینای فقط به مدل فلش‌لایت دسترسی دارن.
⠀
‏
🤖
کاربران رایگان: مدل‌های فلش و پرو حذف می‌شن
‏
🤖
مشترکان AI Plus: فقط فلش‌لایت و فلش می‌مونه، پرو می‌ره
‏
🤖
مشترکان پرو و اولترا هر سه مدل و قابلیت Deep Think را دارند
⠀
‏به گفتهٔ cnBeta، گوگل سیاست دسترسی حساب‌های شخصی جمینای رو چند روز بعد از معرفی مدل پرچم‌دار Gemini 4 Argon تغییر داده. خودِ Argon هم فعلاً فقط در اختیار سازمان‌های امنیتی و شرکای گوگله و به کاربر عادی نرسیده.
‏گوگل گفته زمان دقیق اجرا برای مشترکان پلاس رو با ایمیل اطلاع می‌ده.
‏این تغییر در مرکز راهنمای اپلیکیشن Gemini اعلام شده و کاربران AI Plus زمان دقیق اجرا را با ایمیل دریافت می‌کنند. سهمیهٔ مصرف از ماه مهٔ امسال بر اساس محاسبهٔ هر ۵ ساعت یک‌بار تازه‌سازی می‌شود و سقف هفتگی دارد.
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hy6wnF6ZsSLIyBJi7018xz0gigKIIEqAxPo0nwCe3766ygSM5aTUoV-MSa4C7wyd8cPA5d3lsJmTRBBQztFpB_CL3lrru2mIX-HWOtLhhyE_7NYY9ICEAHYsyKh48M3RpufMqrSxOZXWo1ZkK-JYLILGykHYcfc6CXW9IziFltr-kzLCFsJMqjAv3ksoPL7Bg2aPkVYq1jiLFcVh1q4KmLkbcJ_MkFSdzyQ9LVfvHrGeJxtdvXq064rYVSLVKE3ztr_srX_3_lTUBbgfxXOZ-lmtijUvwJEknzOVa2iss7WjfEWM0b52WmG0PkGm7LauIa-hEBuCW-J_bXNxK9Tw8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🟠
مدل‌های Claude 5.5 به Antigravity گوگل آمدند
⠀
‏در محیط کدنویسی هوش‌مصنوعی Antigravity حالا می‌شود از Opus 5.5 و Sonnet 5.5 استفاده کرد.
⠀
‏به گزارش سایت appinn، دو مدل «Opus 5.5 Medium» و «Sonnet 5.5 Medium» به فهرست مدل‌های Antigravity اضافه شده‌اند. Opus 5.5 برای کارهای پیچیده و طولانی طراحی شده و Sonnet 5.5 برای کارهای روزمره و کدنویسی است؛ Sonnet 5.5 نسبت به Sonnet 5 بیش از ۳۰٪ سریع‌تر است.
‏نکته: برای استفاده از Antigravity باید با حساب گوگل وارد شوید.
⠀
‏شما Antigravity را امتحان کرده‌اید؟ این مدل‌ها را تست می‌کنید؟
👇
⠀
‏
📌
گزارش اضافه شدن مدل‌ها
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eKve210xKc1Zo3f8JzKYkTUj4ft5cHtRY4CGsuJhvdeBWAqHLL8KA1UGB1wSrB54XJdTimDHOiyU2WYxEmb0f9hS5nMNUr74GK5vKXZzuZf4pk6zlt0XRYth1AcTJ5LHhb1hi6wK-CP7lqbByXV9pUVdiqSGS9S9REPJMhn-kNxIvt9rrp78Qanh8ZHl92BHV2697awBkp3H-nNulSBjE73y2r55pxA-hn-FFhekTPUkcGMnOxiCGGriIRmjYhve_uXo4covJLyIl1-bHDz7lkYfCBfeUPfFzB-LBuhshl-lbx5a5VoAemEwZxH8UDArue7uGoOc2qeyojlH8YXuNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
مدل GPT-6.1 Sol اوپن‌ای‌آی رکورد زد
⠀
‏سم آلتمن می‌گوید ۶.۱ Sol سریع‌ترین رشد تاریخ مدل‌های اوپن‌ای‌آی را داشته و مشکل کندی‌اش هم حل شده.
⠀
‏رونمایی در DevDay؛ هوشمندی نزدیک به آسترا با یک‌پنجم قیمت
‏کانتکست حدود ۱.۰۵ میلیون توکن و خروجی حداکثر ۱۲۸ هزار توکن
‏ابزارهای جست‌وجوی وب، جست‌وجوی فایل و استفاده از کامپیوتر
⠀
‏به گفتهٔ آلتمن، این مدل در ساعات شلوغی کند می‌شد ولی حالا «باید خیلی بهتر شده باشد». قیمت‌گذاری‌اش هم برای توسعه‌دهنده‌های ایجنت جذاب است: ورودی هر میلیون توکن ۲ دلار و ورودی کش‌شده فقط ۰.۱۰ دلار.
⠀
‏نسخهٔ Ultrafast هم در راه است که تا ۸ برابر سریع‌تر جواب می‌دهد، البته با قیمت بالاتر. نکتهٔ جالب: قرار بود نسخهٔ ۶.۱ آسترا هم بیاید ولی به خاطر نگرانی‌های ایمنی فعلاً متوقف شده.
⠀⠀
‏
📌
گزارش عرضه در DevDay
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IdiVMR4Hrjnbwr7sWHrhaXBlWph-wmRdAelKUKHofAo8NKFDcrSUNXr0K5Z6NHUh3Xr4TIh2Gx4gC0pRUf_1qel1MBYFySP4A0nbAoLAtBB9Fj8Qd5FLyB4QZxOURK-nx2ROaWhueHu1J0Me9daWt7woTRZfQSXpFDFQ4COd7fDcXD6NwMeA4bMfaC7DPIZqhWSTRblFD4mCmmMr8TyCIDuZP654G98ZKCjPubtx2PXJes4DjklLNoUNa7PD-aVB3OKCnT2PNbpAKFeTHVgUrOo1ouZ6WCpjivRARL-whAZl4BwW042DPsBH7ehR0wbwJ-gvqVBfrYLv78oXVmDT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔢
مدل Muse Spark در حل مسائل باز ریاضی
⠀
‏متا می‌گه ریاضی‌دان‌ها با کمک مدلش شش مسئلهٔ حل‌نشده رو پیش بردن.
⠀
‏• شش مقاله در حوزه‌های احتمال، معادلهٔ موج، نظریهٔ گروه‌ها و جبر
‏• مثلاً رد یک فرضیهٔ ۲۰۲۴ با ساختن گروهی ۳۸۴ عضوی
‏• و اثبات فروریزش در زمان متناهی برای جواب‌های معادلهٔ شرودینگر
⠀
‏نکتهٔ جالب اینه که توی هر مقاله مشخص شده کدوم بخش رو انسان نوشته و کدوم رو هوش مصنوعی. البته خود متا هم پذیرفته که بعضی از همین مسئله‌ها رو گروه‌های دیگه به‌طور مستقل حل کردن؛ پس این «کشف انحصاری هوش مصنوعی» نیست، بیشتر یه نمونهٔ جدی از همکاری انسان و مدله.
⠀
‏فکر می‌کنی هوش مصنوعی کی اولین قضیهٔ مهم رو تنهایی ثابت می‌کنه؟
👇
⠀
‏
📌
گزارش RuntimeWire
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9_vrcPCl4i3_HEZG83XvnE9KoHx7BUJGFNySnhY6F08juKX7amRiavPKxXmlFzKfPqAx7kYrsNR0LipGWHJBKCRqd7X8SkZG95w1k5GcYIXfClwz1RAAvGElCvXGvgUstjSf2-LbqAXa0IVjAdr7bHiQjdP-UBnEbCq4_26C0sai1FhYR2iAxL_DWRM8eCJhxbixXws-JEYXjDUykPhvLSwW59vpy-nU3nSmFyk9Rwh6im7vYg5TlWFzw9VziONn_aUBMzISSwexHImvWJIX7KxtFFxOO7hXB_xVU4ugq5KypoIP7_dVJQDhgLGCeTk5R9-oxCt5OfOvQc9XeqJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">📨
ایمیل موقت جیمیل و اوت‌لوک رو با temp.tf بگیر
⠀
‏یه آدرس جیمیل، اوت‌لوک یا هات‌میل برای ثبت‌نام‌های یک‌باره می‌گیری و کد تأیید رو همون‌جا توی سایت می‌خونی.
⠀
‏
✅
نه ثبت‌نام می‌خواد نه رمز؛ آدرس رو کپی می‌کنی و تمام
‏
📎
پیوست هم می‌رسه؛ عکس همون‌جا باز می‌شه و بقیهٔ فایل‌ها دانلود می‌شن
‏
🧩
یه API رایگان هم داره، بدون نیاز به کلید و با سقف ۶۰ درخواست در دقیقه
‏
این آدرس‌ها با plus alias و نقطه‌گذاری جیمیل از حساب‌های خود
temp.tf
ساخته می‌شن؛ یعنی ایمیل‌هات مستقیم می‌ره توی حساب اون‌ها و چون رمزی در کار نیست، هر کی آدرس رو داشته باشه می‌تونه ایمیل‌هاش رو بخونه.
⠀
‏
📌
سایت ایمیل موقت
‏
🌐
راهنمای برنامه‌نویس‌ها
‏
🟢
سیاست حریم خصوصی
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nj0zQRppkTq23PpCtWy7_SA3oGB7t9VTQYeTLwRBlIIM0eb6OEGBYRLRfwylzox0A0bd21RvVq4lQQtBXp5YvSkduXQn3tUH9JGWXgPyJ1mrANlhvlOV41C619r7HMmiRbtHi2kz_EeLCt8EJVfkWJY-xCd5h0s79yxwNKaL3M8Fj5xwjq05trFJNnb96pJs2cRn4VA630G5gr0L9zeQ69XbJuRyYXw4Twn0C2Vg5C6-9N0oOmxN1rj7m_68pQpeM6Lso4jiBoMzRMHOE4VOJCgRmrnrbR96qMn5-5L72KxAwe5QxTTbFqsUi00bmKzvOOLlvybKtrJ1rx7eOH4UMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل های قدرتمند هوش مصنوعی
💥
🆓
GPT 6 Astra | Opus 5.5 | GPT 6.1 Sol | Sonnet 5.5 | Gemini 3.8
✅
با این سایت میتونید 7 روز مهلت برای تست مدل های بالا رو در پلن Max دریافت کنید
🎉
🎁
⭐️
قابلیت ها :
🤖
چت با هوش مصنوعی
⚡️
تبدیل لحظه‌ای صدا به متن
📢
تشخیص و تفکیک گوینده‌ها
📖
پشتیبانی از ۱۴۰+ زبان
🗣
تبدیل فایل صوتی و ویدئویی به متن
📞
تبدیل تماس تلفنی به متن
📝
تبدیل جلسات Zoom، Google Meet و Teams به متن
⏲
ثبت دقیق زمان هر بخش از مکالمه
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBU55-8jgnns0XCjci5B9SKIiqg0UhBx9QkS2j3MLkb_CFA0ofoN2d8BsffRWPAyHLYGrSUKAkBrh2LCg0KZiK4_vD_pMFE0rkS2F5SlN3mVMkpPVJh5kzQEHwnpT82ARPCXomlDa7DGKjFTHPnr6DHfub9hL6tLXFSdldWdmv0b8DfCkgjGNk7LX1sSt7jfIyXtdhfoO5jUKnqt65YHJxNKItvqjFXG4KbEOtiiB82RkPy4SnEa5CNM1UX_vaqozjkk_RAdj88K9zf6S_Muq3AtumIFnuhvTNVHNZwNtdG0RChTttpWKt5VgsunKFIPxXFWZGU9Ro5qulrT5Z_v_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFK56nAuyMIt0-_wO04x58e73giD9B-0Xv3SgScgbH4cPI3rsP4NfAG6g6E5R-_FCEQqT0RMMI2Rz2Jwr61NN73gnls4DQ9DxR75dYYGjO262UHfeArmD9sKqUmnCwgwHIeJ7oWO0wOtCixrU7tYHQ8TPqVRrvZ3EhxfWr2Kd1l2x_zcKhCs0bc8AT2cR9gRP19WCrWOkDFdcllArBBgujOe4nVkQjY24kRrQQUxRRPAPWrwJjYIY2QPIpHvO3Sqp4GTlNYUIGvkNTaOQOY7dGqbGV2ZMXBkeZ_DO2GON70g80La_IpBhOGORxN_M5GSuemECQWPARu9nvAWvJ6c1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⏰
سهمیهٔ ChatGPT امشب ریست می‌شه
‏به گفتهٔ مدیر OpenAI، ساعت ۲۰:۳۰ امشب به وقت تهران سهمیهٔ همهٔ اکانت‌های پولی ChatGPT ریست می‌شه.
‏
‏این ریست ساعت ۱۰ صبح به وقت غرب آمریکاست که می‌شه ۱ بامداد فردا به وقت پکن. Tibo همچنین گفته مدل GPT-6.1 Sol اوایل عرضه به‌خاطر بار زیاد کند شده بود و الان سرعتش به حالت عادی برگشته.
‏
‏
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fout1ms9n4bndFbTu9xdGZLYld6MRSydtjCvLI0eLw2R5x8wMtUqeJW0840mYe67S-c2c-5vP7yUgjip5qUVeZWlina1ZO4510I3iJGcBpRY-doKVLybvjr-6WxQ6MiL2HziSjTRG-IrCrRoz9VN9SwdwlZ2oEOZwK3sCVFyfCRGPmQLUcm4ZQEANT9Qjw3kyCMIXn0viZdXB8IXUI6dXqjlZrRbYWwSX4_1oJA_XiMQA_ohkqo3-ysL4WAQv9ZDacQtA4Vvuvd3KFMvYYyNpxQkLpoM7GnSrPsmVDSmC-aj6sifCY6NTB4SmAihR7IkyCqoW0AG-bFYmtZ8FoL1XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
⚡️
ابزار InkGist برای خلاصهٔ صفحه‌های وب
‏لینک هر صفحهٔ وب رو بهش بدی، تو چند ثانیه نکته‌های اصلی، کاربردها و کارهایی که باید انجام بدی رو تحویل می‌ده.
‏
🤖
مدل‌های Zhipu و DeepSeek و Gemini پشتیبانی می‌شن
‏
📚
خلاصه‌ها تو بوکمارک‌های ابری چندکاربره ذخیره می‌شن
‏
🧩
افزونهٔ مرورگر بوکمارک‌ها رو با یک کلیک وارد می‌کنه
‏
📷
از صفحه‌ها نسخهٔ آفلاین هم ذخیره می‌کنه
‏
🏠
می‌شه روی سرور شخصی نصبش کرد
‏به گفتهٔ سازنده، متن صفحه اول با Defuddle به‌صورت محلی استخراج می‌شه و بعد برای خلاصه به مدل زبانی می‌ره. پس حتی تو نسخهٔ شخصی هم محتوای صفحه برای سرویس مدلی که انتخاب می‌کنی فرستاده می‌شه. نسخهٔ نمایشی آنلاین هم روزی ۱۰ بار خلاصهٔ رایگان می‌ده.
‏
📌
مخزن گیت‌هاب پروژه
‏
🟢
نسخهٔ نمایشی آنلاین
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hu8BCZcblvwG4UDi1vFOFDor3ImwVEc1nl6cKg7-ZCQBsRHyOudg_0mqmDbs7RvDi0IPWt0hoJSNspr8Vrir9TuCSi7Rfnc7bz9ZgXOPsu8a6kcWhvPOP9_FK8R2aacRTPdzGN_ihOjsXpKCN0xJ61TOKt1oo890SRe1Lng3FJEJOQLiMbvwhgSV1AyDzYxyI6tuZljdm7W_Khuzrl-XOWvcZLm9iPKv40sxmVbJJZlY96RIAH_9LT4BZ4A-ar6kgeyeKAk5miBpGl8CTN28alFk-JZKEER4I09MnV7KBznihPH7HWO3fcHOa67p0z9UtzKzlEAsLiprhFglKIXJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8dr1gxGREal66cyVQxG5EBdNnUHAOOBSdYnw3rSkzZ4tLHvR4eSxI8ae0EQtLb8oW00n1YjRhdc1Vp4NvE07-hJ3YI7NnsBcUTiojbm7i1PMNu2JduDXh7ISnREE3_Xosg96xQ-QhPvgK56DprURotNlw3pMrsUIiJNPYSOiKzGDnWgqR2rCP1ZhsNCzULM5cDIOFOKgWa7rr5apDZxcUHl2-FqCqjPwVB_ge6xwyAuv9ufmMv97wR9rAsAd46jLHND37gw_R19JR9RPhOiTQvFUOf8y1HwrBPAcZITp31CEJurDuYwZbpxAnsTR0vO1170T6XXSlj7Q3KMV2DnYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
نسخهٔ Haiku 5.5 به‌زودی از راه می‌رسه
‏به گفتهٔ Anthropic‏، مدل بعدی خانوادهٔ Claude چند هفتهٔ دیگه عرضه می‌شه.
‏
🫧
مدل Opus 5.5 در ۲۲ سپتامبر منتشر شد
‏
🫧
مدل Sonnet 5.5 در ۲۸ سپتامبر منتشر شد
‏
⏳
مدل Haiku 5.5 «در هفته‌های آینده» منتشر می‌شه
‏به ادعای Anthropic‏، نسخهٔ Sonnet 5.5 بیش از ۳۰٪ از Sonnet 5 سریع‌تره و هزینهٔ هر کار باهاش تا ۳۰٪ کمتر شده. این عددها رو فقط خود شرکت اعلام کرده.
‏برای Haiku 5.5 هنوز تاریخ دقیق، قیمت و شناسهٔ مدل اعلام نشده. حرفی هم که می‌گه این مدل از Opus بهتره، فعلاً هیچ منبعی نداره.
‏به نظرتون مدل کوچیک بعدی به کارتون میاد؟
👇
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Am2BeKksg3iFXGfGO3Z0OiEgAJ1YZv4FizTJdqUN5xSDsMj3o_cpdwM7N-Pk-ZDw3HQmqpHYVDEwa2iAJvjIUw3M9YYCggZbfDxNrmv9D89biYQfIWftjt37e9a6fplbpJRbhgdgf3PPJYm82MAoxYAw41AFEpNW1CpPkzIg0IFxeeM-N18ZsUYK9SPRrP7NW-oyO5nXleOnRWICloeQpSBQC9lr2ip2-LdiuT5OyFVhnIc9Ou71iZhJ0hZJd8ypAUBcjdyOYuoK4xXdfE6Nw_MRJZB57HP8oaTUugX2KY_CRChJzHkleoXLmzqanSjfnaQ-S9iF4Pf1dpfiRzz0sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Claude Sonnet 5.5 روی اوپن‌روتر عرضه شد
⠀
‏به گفتهٔ Requesty، مدل Claude Sonnet 5.5 با قیمت ۲ دلار به‌ازای هر میلیون توکن ورودی روی OpenRouter عرضه شد.
⠀
‏بیش از ۳۰ درصد سریع‌تر از نسخهٔ قبلی
‏هزینه تا ۳۰ درصد کمتر در بیشتر کارها
‏پنجرهٔ کانتکست یک میلیون توکنی
⠀
‏این مدل دومین عضو خانوادهٔ Claude 5.5 است و به گفتهٔ Requesty در کدنویسی و کارهای ایجنتی نتیجهٔ به‌مراتب بهتری می‌دهد؛ قیمت خروجی هم ۱۰ دلار به‌ازای هر میلیون توکن است.
⠀
‏مدل هم‌زمان روی پلتفرم
B.AI
هم در دسترس قرار گرفته است.
⠀
‏
📌
اعلان B.AI در ایکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUDrbNJSoiIC449tnDmESgwKORPKYN9h7gI9PmdPm0i3RX58t1cSdLCLfxRpfoYo5G0itWLdFXh0ajGj9ZiSnCMf2ssdzyilcz_tx2pOzGtcrq0de4WSo6feebOr_wR7T6tkXR3Wv4FBG456IFAUj5MZyn8O18tZ71hYz1DAXuSrJVAWahvjPDc0bkwWPrduASiyCnTM3ZTeJ34_WIfULbk6mzQR47b_d_A07AwqoGg9NG_Cf75_DocNACqqg-ah8MbvS9uIrfyVK31H-9qo7CNRSolATozQtn6nx6FYx7AElWd_y08RMWMjvQApGbgvvuK4gtUGgppQSbiwCx7HGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💻
همهٔ دستیارهای کدنویسی توی برنامهٔ ccgui یکجا
‏اگه کار با دستیارهای کدنویسی توی ترمینال برات سخته، این برنامه همه‌شون رو توی یه پنجره میاره.
‏
🧠
موتورها: Claude Code‏، Codex‏، Gemini‏، OpenCode‏، DeepSeek Harness و چندتای دیگه
‏
🫧
یه برنامهٔ دسکتاپ که با Tauri ساخته شده
‏
📦
نسخهٔ مک، ویندوز و لینوکس طبق صفحهٔ دانلود
‏
🔄
آخرین نسخه روی گیت‌هاب: v1.1.0 در 28 سپتامبر 2026
‏کد برنامه روی گیت‌هاب بازه. ولی ccgui فقط یه رابط گرافیکیه و خودش موتور نداره. برای هر موتور معمولاً به حساب یا کلید API خود همون سرویس نیاز داری. کدت هم برای پردازش به سرور همون سرویس فرستاده می‌شه.
‏
🐱
گیت‌هاب ccgui
‏
📥
صفحهٔ دانلود برنامه
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7-x7IINNodrlwQWImWBN35f3H2yjNYZ8E28V8l2RM-d6MmBFf3mTlFuIyvXYVfDcXCuGFO6e28c1TU8hSrozlftWr_iM-9InWIcL9tDCvzb2rSGx-PCHNE9NAP0saWNv1numn53ux-tvC8noEljxWQGj36JGLSTTR2D-7RHKdNyPjj20eB_WTPrsKY8pJFRZCsUj-9GGruw3q2NfU0azPF4flvMR1bts1Z8bN-MV_2YRce-CLjRw_29gwEsLvPQX3gSnnI9ML5nkhUmjK58Dk5DPdNJC7w3O9eTwPRT81atQTnM_wdNmU3pOF7HUCTVAgiTD-CqCbUe0Jb9PYRw5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IrLrtEg5tU3lTB48QLOYSiArqtSjP477-8fEKfUxDwn7jI1a3Rz9Pq85eSZXtWWvXLz0VcfcdcB-z_9J8zrzg2DBX2ej-9oxI7ofLVmsgDzlTQsL_g-w46AoodN5W-C9yts42JVZgXkmyS7veJkS9A8hgwF6vQ5dnZ2y70CeCeIf0cEZvpTiik5GaRbgVLlLTU-AB-DwulsHoA4Y4j8_YDZ08m_3YXZOsrhRDASGJ5EcLSdqhNokXOxPTwpiFUCJy4ZVFjGaJ5ZxnrkAHXNPOIZSRyBVmISUuRae9BHGxNGwk_M3_CdNkKcwwe3_xDic0rbjacewmfY4cOD5pjLrig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vTGIRogemzRKqtBFVs-sg6TfGQ6EVHZlu8Hm-5afxpJZsDIPiwhdpuNRpoMpNvCnEdSkENWLEsXyeAMl9Dx1xoy6Vkwr_ejKOgWQ1KogqXMb9MjoI61P8SO3FjGrj0CQtu2Xkbb1Qntyo6NM2RPrL04-pQGZtQyDEf29Rvknjv4n4ksi517MXaVTQ8ZM9TD7c4WHIlzllwVMo0oYrkXsUYhBCxFe2s9XHOVcvq8DiyRtgxvGCklshgEQzgnGgAZsLxdw1pH0RHiK9v01VkUaTPyPoJ9rhKYT_rBrBZzbVr13Q3LqmW9m_F3CRHsW5n2vUa74llEuswN6MvFogrvnOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tq0kppPn6JKVRFpUpCF5nTSBq7Wz_RKSWnkqxAwPyPNaoMC9EtWQqrBMakwKC7FRohqrn8geetb6WjBFURN4LPtU5_x-SYFHQrdWN-mZt8YqGwuBQRjGC_CRPP18-k2H90ymLoib87SfJXmXyA9ekyRojiOVk667L6NMwEH1epe35yaLyA-eBfhldallip8RQu0uJKgNvhIEQD2XCcPNl5s0yJ-CVA7zNJQMGdxAo6qHGZTF8ybFJ1sEXmBcKQdx_rt1JbtUaOtESpWUeYbRvcLy2WfQJJqb76ydrrbYUgA8Ulh3gFM8Y7uRPaC46s9HG1bYa5pfL77WDJbDI7bq_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I33gf7BQeZVQt1c1foGGn529h2Njqz36CwTXIJsow704A_dt-Nx34DSxciOzCLWBvvfweBVYpN3bGhKv0h7FeIZB9dZZ09-IK8w7qu1JeTmO7g96EMpfGUXQQv2SeLM3gz0JdrNOa-vMq1eMeli4hRfvd2bg0ceJx28BMl0JlX5Af3BmabL-V5HBaqQneiizjDTyhp3DPtPhiyKJVcVl-bSrtdF1SzyU55gbuP0xEv6X9eYjvz_GPiQ-Vscx3h2oHaodBx79o0W3eNZmZIPAolB7qiARZNY6kxSs4d2MshoAmroPTvSI9CLIHVNTTEqD_bcpkuO6U_W5d5fhxEPNGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CaihIMKiLm2XWJU2ceb9dPApEGwTqlC9mlagW2zdPBPY_xiwqdbXkyvOULyvYVizG_EcQRlOsTwLOVyq40EaH5wgIbZwPBWnZ3c3RmRuLEYdaPUv_jxiB4Xp3Q5JFR4QdRPMbYGSW285qdBrWmWHOTDeRlm-vzox3-zvP12fo5SsCxRL6yPDIbF-LxXU85aFmLfiaySec6oPrKAATzwixOST-o16knzqS-UuCSRtqAE4OcKuOq0Klu0e7SPcNUNgdy5x5SEEETSToiLlmSm2vKKlv-ZFz8euDfYc5e8Q1TVQy6RDQ1-RQSfxT7Y-tnOtthYKfMk41czNUeBYGTtU5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8styCO-itYqCvWxZir-tE65MYzG02AnaJUsOKnkU4hyapkhVCNJP74pGKH_BRU5hXTkGSGqqieKqJKEmeZ06U633K6Rb1lxX1Pe00-9NYi59n_l47eINnpcLx1b3sfXFZDelSH6nrY5UhEZEOqpDN57fwMfOsJ9alG7mAkbQCS-LgZolaFoY8iHw-MxIcNHRZE5-FaxVfjeK7FpcWyv1SpUsXowHYU8g3iQ0oppzbw-uyFlHIk59onzdewZaiolPbuMGmrh37liqg18oblA8raiCQ-hV7Cb9uD9Ot-dLIQ9DHwA-6h6qtqLXQI8xLbnmYsJS9lmWJrTk8IE-qGOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
اسکیل‌های Gemini برای همه رایگان شد
‏⠀
‏گوگل قابلیت اسکیل‌ها را که قبلاً فقط برای کاربران پولی بود برای حساب‌های رایگان هم باز کرد.
‏⠀
‏
🫧
با اسلش در کادر چت، دستورهای سفارشی‌ات را سریع صدا بزن
‏
🫧
جم‌هایی که ساخته‌ای حفظ می‌مانند و از ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند
‏
🫧
فعلاً برای حساب‌های شخصی بالای ۱۸ سال است و انتشارش تدریجی پیش می‌رود
‏⠀
‏اسکیل‌ها نسخهٔ ارتقایافتهٔ جم‌ها هستند؛ به‌جای گشتن در فهرست بلند، کافی است در کادر چت اسلش بزنی و دستور دلخواه را انتخاب کنی. گوگل می‌گوید جم‌های قدیمی‌ات هم در مهاجرت ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند.
‏انتشار هنوز برای همه کامل نشده و ممکن است دکمهٔ ساخت اسکیل را نبینی؛ چند روز دیگر دوباره سر بزن. ساخت اسکیل به حساب گوگل وصل است و حواست به داده‌هایی که وارد چت می‌کنی باشد.
‏⠀
‏برای چه کاری اولین اسکیلت را می‌سازی؟
👇
‏⠀
‏
📌
صفحهٔ ساخت اسکیل
‏
🌐
گزارش نئووین
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAOEpa9DAOuWyuiN14iPhJUdHBs84TtA3Z8e2wqXyYcTMYmWPizy1N-oewfAPtAHNI2CmumkSC6fdnS00yZBbya15dDQhzqoLsiF-w6rIQwpnmm4_V9iiVU5V-D8Gf56ZHR0MNapgZm_TsCX2ZrFr3odbhKvCAkBeTNmn7PAubq62NWJNF6FkLSZ4mgv4Ldklxzi9ckaOZTp6sewecpkA8c6OzVXthcYcQZVKKWxuRnhRePHQlIL70eGMvG2mszrnYEV4Y8KUt7W4b-6N2AaX_7-2_0C5P_DcM9T4PahaZxRHPosjiqvAnlKx7GEV5yig2AU7xMZfPqrAoHXtOVIYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
حل قطعی مشکل باز نشدن Gemini در پنل 3x-ui (ارور ریجن و لوکیشن)
خیلی‌هامون این روزا با ارور رو اعصاب "Unsupported Country" تو جمینای درگیریم.
داستان چیه؟ گوگل آی‌پی‌های دیتاسنتر و IPv4 وارپ رو شناسایی و بلاک کرده.
😀
راه‌حل قطعی:
باید ترافیک گوگل رو از یک
IPv6 تمیز وارپ
عبور بدیم و برای کانکت شدن خود وارپ، endpoint رو به صورت
آی‌پی عددی
بنویسیم.
بریم سراغ آموزش قدم‌به‌قدم:
👇
قدم اول: تنظیمات خفن Outbound وارپ
تو پنل 3x-ui برید بخش Outbounds، یه اوت warp بسازید  و اضافه کنید، بعدش روی ویرایش کلیک کنید
🧪
سه تا فوت کوزه‌گری مهم
تو بخش ویرایش:
۱. حتماً تو قسمت
endpoint
از آی‌پی عددی (
162.159.192.1:2408
) استفاده کنید، نه دامنه!
۲. حتماً
domainStrategy
رو روی
ForceIPv6v4
بذارید تا ترافیکتون برای گوگل فوق‌العاده تمیز بشه.
۳. مقدار
mtu
رو بذارید روی
1280
که پکت‌لاست ندید.
آخرشم بلدین دیگه تو Routing rules بزنین کل سرور از اوت باند warp رد شه
هسته و پنل رو یه دور ریستارت کنید اعمال شه.
🚀
بفرست برای اون رفیقت که سرورش تو جمینای بلاک شده!
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚀
شرکت OpenAI از "داتس" (Dots) رونمایی کرد، دستیارهای هوش مصنوعی شخصی‌سازی‌شده که در ChatGPT در دسترس خواهند بود.
آنچه تا کنون می‌دانیم:
🫧
با استفاده از فناوری Astra!
🫧
داتس می‌تواند در انجام وظایف طولانی به کار خود ادامه دهد.
🫧
احتمالاً فقط در طرح‌های Pro 200 در دسترس خواهد بود.
🫧
از مکالمات صوتی پشتیبانی می‌کند.
🫧
دارای یک ماشین مجازی (VM) اختصاصی در فضای ابری است.
🫧
کاربران از امروز با یک داتس شروع خواهند کرد.
🫧
به زودی از طریق پیام‌رسان‌ها قابل دسترسی خواهد بود.
🫧
از بیش از 4000 اتصال (کانکتور) پشتیبانی می‌کند.
🫧
بسیار قابل تنظیم است!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIoN48MhQigQFpmZPygRTd0vYRZ_MvHMau5kpSO8VA1T_ZFr2rQR-wfSxcYsAu8ZOpmOlIjeloHi5uBn1feahGltH7ag9Xpq7WfhPTtUvONh_qcOf8ysxKPFnbvEHW5VXCEd2-hGsJz6eVj4EmULysf84xMpJ3OR_lBkmlQunkIIxWt9ZbqFR1Xkkowdl2iv8nYpSvrsBRc-r6qkx0ywyY3mbQfup-fByxD7uX7Fr4tJUgeOvqjXOSl1k4C_zoRc7inrHYDmAb0E0j3EE_fV7tJD5yFxIEUZQMax5u2ydMLW5j7XQ-YV7w-6D1-0e_7DHVINKWfZiZlDGDLTzSkAcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k0s4U2bOnGBk4GW-C2KhO_4r7rSYOtKn_oFAevcrh_OqvaySe5dk91sHMqkg4qX6-vwOmd4JP-yBH39pDuhHLt7Szh_nCrgk-WhssXi47roXZEsrCnpZsR7iJLUpwNlh3Fq-lk0lInOlCXibUD1yn99Ygy5uswLYnkIMNz0v3tNqZDvVaqQCRtD3i8myWaojbq_iX7H9odV_QHYgl2qDHLgwxoeruTXqU8blTLQkqG17yiu1BzSQ0vB6mEBu3f1DgF_xoJQiYqnMdoEVc591aS0sI_ddIi5xmjjL3MSpftw9dw5pylmW39_0HqrUZJDN30xbO_IkwqCdOQKVm4lZbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fiK_FAGFlLCc8VHhoEailaqiehMt2_KH1adJD19qWya6CXoUArKuZBX-XRBh21MWQWlxtE-e6dfmXeoAzZWufQ-CCTpueIFx2pOr-5f57tP5jixx5rU3-87EurFbQnnlVO3uZuDJu689GcSIbqLNB_LJdSmXbwCllM8j9nMcTHzd4jD1mEt22ySwCt42pCt33M3I-2pfXJ_rdVZsQEdl3l36Qe5URu47Mv-63JKxZv1rN2U3YRX4G6FB-Ez84sFK9nhyNIdvDDgPO-7ukg2-KeQtqGDosFfGzDG3sgRjB1u52-kfBLbVB_KXyH7E7fT6oIKQnQ0gGqR4JGh7FC5tyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfgZHa1bY9XHleHiLzky2cfUB4hFx3ihMb3oHegL0XaZOfen5a-C9Diy0N1KsTEFHoEE3SFnk5lJXkUD-IaxjNoyWCZDrrTtSyfWg8dL1z9nRyzkCzBUSIDJpvydmnziPMqzY2fZ8bhO-wbCXVHwN4hZ53P9qiWVtl7z9uConANfbUcHxQ2gxgRY4Z4V3u_GUSlwH85s6K8dckCQEXAexKoXy-dZEaraE3o_OuguEjqfK1QNm5Yr5bs8wHIKy1CiAI_wDqoefeF2Vv1WmKeDQ1u-OieYNeNSmLWe4Fb2X5K2ts5ZonKEPRX_q7GfGT0ub2PLSCZp59yJYLN7ZBj9Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Om_drxdQrQ9noWH-nJl-qOAsiwRcYdL2Scjr0FD-PUnt8yR3v7sWHEm_gmurJx-RAn_KNJbOWqFfgpxkPoAO7-cRmG_-1sXPDia8-MYc4tSHDSWEqHY4gQ7wTp61Oh00uhFUFhShLmKbFqSFLsNvpnRgMWENVKQDtOQWCujZW5Kg3jJSlzEYIWZaoX71bJ_kJXocu4PU7mPdtA0a4bjrHyQuv7YovhEGhUBqM2LmTCkIogP-Q1GetPPbyAAkM7nFyOrv1_sUG1KQ9Wgar_CqZ_1J26O7ASkE7WjuDFLOuilbh-0JW9Mz0Wb13E058vcY3DD7qonvQYbtZLIX8FrqJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fz-J0R94-tqhFmsfFijQqZ0hxlElZZaLBKO4BfRicLiYJi3ghy1OmjBLvnbB5pgv67BiZca-b5DQh88nZRkxR1mALIV81t2INlB8r9yvtCuktxebC52Y1t6NpVCTuUfxFAQRMed0NQx_5z-323sB3XkSnWUiRYl9jYzZIbEIEVgfMIvpG0bQDjprvnD_sGjRSRp0yh3Vc_ZGaVbFZwteaOlS0vFxHVBo0whwjyVG5p8eLfgd4q_cjsjJaRn_4rQgZq5ltUJRVdB8pOjYPZHDkI2P1GIAFYyaJxvZlo6PeUHnmnIvAfIZxw9SAxge_4dIxIkR89oMlGyXEkDwFauYCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxVGMb-9qq6IFvVZvuyaPexYnVtsM7dOdYjdEtYAJt05gJqRYkbFWmYO05XvOiz9PqLsYYYqs8OCNA1R14VQMZBzk3nIX4Z9ZHW0Hl3lHXQnULl8_NARbMOruG5fPIbOOY4-L-rHs0MfYSze4K6WPx5ULQa4HxQpBlClER-j_0Mi6hXExr45Dcl3w1CsZHsnE79wLFIw2D3OrEPRAy4hxGyQkHfrXQq9FQnAsn8bEqLIKSArvJTqcRSlQu-FylRFpCy0D2gxpwjJxLJKmSydXyL6I3DlrRCY5ft_RDlDoo3r-VKRQ0pXUVC7QKo4hJddA8h-0ikKJGpy_QSkYuX6IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Relapse – PS5 Jailbreak Exploit
🎮
یک زنجیره
Exploit
با نام
Relapse
برای
Jailbreak
کردن
PS5
منتشر شده که
Firmware
های
7.00
تا
13.60
را هدف قرار می‌دهد
🎯
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oT1vaGCd2THQu1DG4wpkK3QSvDfGhM3g6qj5BPHxxBP53qPMIaKE-BmM8CK1idiHtSAV2aN6cyXeV8nDKS7PLyaztfkMVr0ITWAxvl1_udp07oVsdUZ4die1axcV8wU6sKPVZ-cGtbknfXNdOAi9EeJSUzXsZOhLyv5TLUVYaDYRs6TNRRZ8G7X1MXtuo-iAHVnNwumqphlMs30EJkDmmGe0KdIw9phnK5xMy9lj0Iioj3BGr8ssUuuAxgwBL_evC1KO53Pf88xj69vF9SrJ0gd-929KxejE56VI3KLz66A8EImEf-XODqMtZl1JtHZzgEpuEXr1UYbRtLz3R_WUAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های زیر
💥
🆓
Opus 5 | Opus 4.8
✅
با این سایت میتونید 100 دلار API برای مدل های بالا دریافت کنید
✅
⚙
پیش‌نیاز ها :
اکانت گیتهاب 1 ساله + یک اکانت دیسکورد
💵
هزینه مدل ها :
ورودی 2 دلار خروجی 10 دلار بابت هر میلیون توکن
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdSPxrc39387jwbTxV6hjynp1U3MNRbhTeWrCCanyWnaaSKxZIoctc64rbamqPOng7jiZWTD0pNGtu07dHeBQUR_I-be49QU2Sc5YgdhzDkQcCw-L6YgjSC3TaphxdyYM4yVuttM4KEjcZevW92gtgvCQ0tmE-VVgKUTPHjVspLErNTh7_jPZ5tfx10Aw7c3opDQ5ZfyafQNLJ1HZLDUMvt8Bx1P6QBRuQDs5Qre-ANpxKhUUwd6_ypjKGCjgMqqyWdSFO_GuzvYy4uxXQiRkjgapd2po1_dI2KNDuRLsd0a_EJ7SQxirJZc07iXotq3HxTpKYeQ4e0YrtObYyt_Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلودر دسکتاپی deviload برای یوتیوب
⠀
‏یه برنامهٔ دسکتاپی که yt-dlp رو پشت یک رابط گرافیکی ساده می‌ذاره و دانلود رو به چند کلیک کم می‌کنه.
⠀
‏
🎬
دانلود ویدیو در MP4/MKV/WebM و صدای MP3 و FLAC با انتخاب کیفیت
‏
📃
پلی‌لیست، زیرنویس، SponsorBlock و تفکیک بر اساس چپترها
‏
📺
ضبط پخش زنده و رصد کانال‌ها برای دانلود خودکار موارد تازه
‏
🎛
ادیتور Devil Cut برای برش، ترنزیشن، سرعت و تغییر نسبت تصویر
‏
🔄
کانورتر با هدف حجم مشخص برای دیسکورد و واتساپ و ایمیل
‏
📱
فرستادن فایل به گوشی با اسکن QR روی شبکهٔ محلی
⠀
‏لاگین یوتیوب و اینستاگرام داخل خود برنامه انجام می‌شه و کوکی‌ها همون‌جا می‌مونه. صف دانلود تا ۸ مورد هم‌زمان می‌گیره و خطاها رو خودش دوباره امتحان می‌کنه.
⠀
‏با Rust و Tauri نوشته شده، yt-dlp و FFmpeg همراهشه، تلمتری نمی‌فرسته و رایگانه. ویندوز نسخهٔ اصلیه و مک و لینوکس هم بیلد دارن.
⠀
‌‏
🐱
مخزن پروژه
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏
🧠
اکوسیستم GLM و راه‌ های رایگان استفاده
⠀
‏مدل GLM 5.3 شرکت
Z.ai
حالا یه اکوسیستم کامل داره از جمله چت، کدنویسی، ایجنت و API
⠀
‏
🧩
روی همون بیس GLM 5.2 سوار شده و همه پیشرفتش از پست‌ ترینینگ اومده
‏ به گفته خود سازنده، بهترین مدل اوپن‌ ویت برای کدنویسی و ۵۰٪ جلوتر از نسخه قبل
‏
🪟
کانتکست تا یک میلیون توکن و ۷۵۳ میلیارد پارامتر
‏
✅
صدرنشین بنچمارک
CyberGym
در کشف آسیب‌پذیری با نمره ۸۴٫۵
‏
💸
قیمت رسمی هر میلیون توکن: ۱٫۴ دلار ورودی و ۴٫۴ دلار خروجی
⠀
‏
⭐️
برای تست بدون هزینه،
NVIDIA
Build
همین مدل رو با کانتکست یک‌میلیونی و endpoint سازگار با OpenAI می‌ده
روی API خود
Z.ai
هم مدل‌های
GLM-4.7 Flash
و
GLM 4.5
Flash
و
GLM 4.6V Flash
همیشه رایگان هستن و وزن‌های خانواده
GLM
روی هاگینگ‌ فیس منتشر می‌شه
💥
⠀
‏
📝
معرفی رسمی GLM 5.3
‏
📊
قیمت‌ها و مدل‌های رایگان
‏
🟢
تست رایگان در NVIDIA Build
‏
📥
وزن‌ها روی هاگینگ‌ فیس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZXNoF3yL21E3H71DJD6s1bRAmdykCzCvXNizBgCKyWU8TLJZArmTmlZC1xSH2dcTanzegEW_Zn_RQLyUCTd8C3C1zlv0d5tgehVgu5Z-l1Xp1C6l9cnIQ0Q2MOjy-uP9bxLWjafYlxKQI94Z8ych54QPw7lL8UEC7xVdO_B1zujb1a74-ajPj_gf6aXQBQS7lYOETQTrdp637zdChNP7hToEzmujZ3r3el-iH-1rLPIRZUtbW_6WyQUMlawOeI8nkPEf84ktvkWF0xPxpAXVofJ-tw1PSSY1-HI8bxGgtv2CIiESQCbSeJryXTFg1ZGnRLYHch1B8Qfw0c5Yv19sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OqQBOeM_HyAYL-077Lc06HYe3a2HqobfTFS0fHpxnOM9eZKDE_baregNn-shTcVPwgNuvlP2nGfeBofWwuDiSEyPTk-anRL_jneqymBzwFOLRvAH9xI8nSbPzU_HMLBDGhMC9N6Gw2WnDCvajeNF8_EkEQSk7S_66Ul_Hg9r76aLt-Nxj71Ne8VDNCaqfjWXHDWLHRybfS6DhgwKzfFa-srDVVdwMPGKSaiZNFB9_2nZOZQTTytadhHF3NuU2SwvqMZ46uZjzLtVUvNZvG7E5gg9R06sNmY6mGvAiuut-WafY_vHRE4R-sq9d4eKrbZPucPWbmXAIKVEIWQ6QkheMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gok1AdU6QgXk_hzm4YTGmcqEag12QzM0SBApFmcUhvxpV3fJmHElFTL3vjHcU6GidGZVPilIB1yzvGwGm4B2JOLy9d_XvIIgQ6YWMh3oBe5Xlp3Gfe5-_XOBgpesxkMc0jFBeDrjzk3xiS3LVpGFjJ-VnQSAxsl_ehY6U4PbCA5DunOKiVa7lrBYVP5b5MdFKxk4osP43D69GpK47XeZr7my6LueZAYHymLfbXfuB6D-DGULpwixwYuGDwfA2_SvXYFIGRXEVkPn7NngiR6h06BKZbJbzzcW2NN-cbfCCBXy7P0zASfg7_4g2IEcHh3FGoGoQBoKhyUPAXMajCFA6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dknhJ-I8goMIbhrgld3P5E0ONUxBGZeBIDQD1059NURhqOtEl9bDousU-E5f8-PcoeQYGZbBJTjcfq-MAAzCl0Gx86cs5mWEJBmxkMEG5NIDGg2jP_aiaCRicjr92RQfVz7haoi7hFNZzKXXIrMRAsekEbqCkoCaAglZSGIftHZQInD0jvROjUlrcbKXOmx1xA_L6X5vrCQ3n9T7jiTEnxZrRxZx3C_NujKejz6N3EsMYzseOyXgnvawIbfUKjMdGmQ9jIvzIde_2rVk0xqQVT-ueuA3FZ_J9ABEd5xdlumk9070R9RFssCFZ7ZOjOeidphDEeuoWYKaR9GgUF27KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0XeKBHvSUeOG2s8jEMpoql39BB9HWnm-PGK3oDDwZJahp8tbzUOnTcTuZPgo1f-V4mfwTBh4epXJaQf4OX2okorNuHX068v1zhD9pznhph2KLDUMPEZlOBub-M2fpvVmiA6zWsKycFqP3QDhe2DFx9jYMeD2yNvz2WARNWKjnENVSYYznrm9GgaAXku6Th3sITUzqqjk-Sw5ho-KFh1u-pIBZ_dpe00KwNRTEyyrOEGoVw6wAns4Lz2VIx2rHObSG5evvQhakfVMIxwBJVnQyxP11XvV-LKH-poA_QPeoMQdCW5sUmQTWy5ClLHC0vb8ndWwr37GtIqQSxl9vRjfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB13pj8lUTNv1rl6vr32YiQ-2jQJUvPloNH3vs_ZZ_8mfjA4yYnzJfXVbqwcXuui9LeiVFWBxecZ5b4hNWDCZBKK9H9MRBPaQ6s0ST-Sgd6zlGEq9_x7CSsqER83Qxu6nUYFl22m4e87DaMXbTx3CNhKaQ7n1ZbNIVUIJNkAiQYlf9ErhIIqEJuQvvQl4KThfzFLIoUCQeN6Wy_3TPuHIePr02wsz1ccsQrU24qYuSJvxUe70zgVu4y2jTIIdj2dMmsq5pt_9cbV7wr0QxgsdHiY90bI-F_FzhzcSC1oeirHF0x6pGWqnpVJlSF8ttQX1uVWsvFiKVPu7PFuQLLw1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfAkJt3F0FULo5IgaMotLdCRhj7HTo-Luzrn9Dc-G3trsQBY9EfaY4iy12UJv4d8-Z8fXQgzEF3vCaY3TEq-wu7BGmDfe0CvPfWjDcuVB-j4_Qab3hGUONiQMpZ3clQg8-QjMDwTobAb4r7f-_EJs_q4pJ4kXdUO8j7RtZToJ71tJDwKFUk6u07nzOj30WK6dECVj3rZ4SDhtg0WMfoocmsUPUKfjGs_4eutErUKBtZ1alpycZJuzxZH7zeFm3K1ipFwHcat22I3IGp0ysRVqzxnjNT-pJ72PPQCCi70jrAipfurcZX9-y2c9CTFtAqz4wwQtw9k1mxvZZ5vHkMDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gmtmg3w7ggephpVBrqQswcBqyaFzs1KkwmUB9eUVjD4awICVRpdbpXO1pXfIkfonbBJmG3hwkjleuzA78aGJTMA_ZQOi89RKmfKDHfAGFmiMqX8QyqajEwUIOk1uO7Rn-NsOaSGzJtyVUKaZ0tBrH-0nRLWw51zoL5W3PN9Kqg87ze2WfvfyL_TbgYThN6yZQ7Jq7zPMgdhUX9scqKxZXvhtItzueMdbc2goLSlfCh_H5K24M7zrENFESkIJUxkx4db1Eype26kbVKkUIIMIj2ShEaPgV0yQ_tkn5bEPbvPvr9Ure2i_zdjZoUbW5mUvPlfpaGgYN7mqBSNjsGTlSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljVd80m4NdAo5Fkh0JV11HWpvPjj4DPHHxG2I3VxiyZUz1ZKnd5RBDqtcCIEuJ0vnVPhs_t8J8Ekx2b-2srNSRiBLRAmjmg9PGaor1trR6pGzujZQwhjD9d_7joJmr1Q2QF534ZlJ8ca7kxoaXk0dE7oPo96ejnezj7YY84znussSqM-fuGWCX4J2PWDHqk5Oob_BofwTUAzA93v4EyRbp14mldZbpOdsyiF3OlJ6mg0Zckmm7gNhN9zzj5lftsYymjFvIayrKzUNgjTw147louvUfd3XRFiuVWicB4BztwLRkH3Ryr0cBbDhjDfqOGLr76YM9whHQT5IrZVaF_Mig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
ادعای نشت اطلاعات کاربران صرافی والکس
⠀
‏لیک‌فا، سامانهٔ ردیابی نشت اطلاعات ایرانیان، از دیده‌شدن حدود ۷۵۰ هزار رکورد از داده‌های کاربران والکس خبر داده.
⠀
‏
🗂
داده‌ها مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱ عنوان شده
‏
🪪
نام، شماره ملی، تاریخ تولد، تلفن، آدرس، ایمیل و مدارک احراز هویت
‏
🏦
شماره کارت، شبا و مشخصات صاحب حساب
‏
👛
آدرس و موجودی کیف‌پول‌های رمزارزی
‏
🤓
حساب کارکنان و بخشی از داده‌های سامانه‌های داخلی
⠀
‏این مجموعه تو فهرست فروشنده‌های دیتابیس غیرمجاز دیده شده و لیک‌فا می‌گه نمونه‌ای ازش رو بررسی کرده و صحت داده‌ها تأیید شده. والکس تا این لحظه واکنش رسمی نشون نداده.
⠀
‏اگه اون سال‌ها تو والکس حساب داشتید، کارت بانکی قدیمی‌تون رو تعویض کنید، ورود دومرحله‌ای رو روشن نگه دارید و مراقب تماس و پیام و لینک مشکوک باشید.
⠀
‏
🔎
جستجوی نشت اطلاعات خودتون
‏
📝
فهرست نشت‌های ثبت‌شده
‏
🌐
سایت رسمی والکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXZq6KhCUmGfL6Pcy1hxChBEHR36rwqE3437_u0NlG7QpTqNUyrVJ9H1CE0AAU2-9HY0tZ6aESLaUYrF0Vyl8NJ88Hk3H_p057yq5rmUJ3eVK8MYx8XcC0IfNQ7-0hJkLuV80lka-7zTFE0TGETs9m5XhrSd-qIuKQMzH-2KGkZfi43Ti8wHb2RvbpB6kdj1la1l4bG_iU3Pg--X4FQkk21EgC4sCB37EB4C9HTuY6SF6Q9__ZDNAadd1i8IgSCkyiA4aW4QDy4w5e5B4t5kDOS38floMk_-wkgnFi3sUJrfWhpc0rBescNzQocytC06M3cmO_knfcuGcFTQSVelUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎬
اسکرین رکورد با Recordly و ادیت خودکار
⠀
‏یه اسکرین رکوردر دسکتاپ که خودش لحظه‌های مهم رو پیدا می‌کنه و روشون زوم می‌ده.
⠀
‏
💻
نصب روی macOS 14.0+‏، ویندوز 10 نسخهٔ 19041+ و لینوکس با محدودیت
‏
🪄
زوم خودکار از حرکت کرسر، اسموث شدن حرکت، موشن بلور و افکت کلیک
‏
📷
وبکم شناور با تنظیم جا، گردی، سایه و زوم واکنشی
‏
🎛
تایم‌لاین با کات، ناحیهٔ زوم و اسپید، متن و عکس و شکل
‏
📤
اکسپورت MP4 و GIF با کنترل کیفیت و فریم و سایز
‏
🧩
سیستم پلاگین با مارکت جداگانه
⠀
‏بک‌گراند و گرادینت و پدینگ و سایزهای آمادهٔ شبکه‌های اجتماعی هم داره، یعنی ویدیوی آموزشی رو بدون ابزار جانبی تحویل می‌گیری.
⠀⠀
‏
🐙
مخزن اصلی در گیت‌هاب
‏
🌐
سایت رسمی
‏
📥
نسخه‌های آمادهٔ دانلود
‏
🧩
مارکت پلاگین‌ها
⠀
‎
✈️
@ArchiveTel
l</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQokrpO13FlK8M-yqmtrPbDXmQhfj4n984MKj5fV2zuJuozTSE-PvwmdqM9EqC2qaeIiGduAlci8rkqy4S1VK97SsvGEQ_a30BQAlADobZjhvXlgnxgEhtBnilib-OEhKyfKLu9aQHrWHcXnsgsssA46N7T7iRVf7WnJOWegfWkxeMujvbsiOkEBTdtVGv1X5ReQ4JP5PWu1EVSJK_wk-Dujj_ffdt9ibvT4nx-1Zg0fNvMuokXvLCVtxnMH0hXfyCowCSmYvbcCFjptx0TIr1mYf6gp7cnsSpcFcIkqrFN9lLfRitkMVgOYKuVCKwzpy6xkNHokatCNtFKBy-jT6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به بهترین مدل های جهان برای چت کردن
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این سایت میتونید یک تریال ۵ روزه بگیرید تا با نسخه اصلی این مدل های بسیار قدرتمند در درون سایت چت کنید
✅
این سایت یک ویژگی دیگه هم داره ، شما میتونید با مدل های GPT Image 2.5 Flare و GPT Image 2.5 Sunburst تصویر بسازید
🚀
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=DAoLSygAd4gV4i2ZXHak1RH3rE6x_jsM89j_-MVAAVp_PvzwHicu4eQtKKc_6wJTwDGcnds_9PgPNLRe1jLm4sWkMQwqsMOakbIRXIjU-9KNh04XPNCMfBVfToWDvpiZwQ1ek_679sEekduScIalwoLRbd9AVFx2suOiqxznBz5R_Vo1kHNu2lyg2DMUXn3VmLoWuU3SMzMRJSF4p58a2WsEF0O6_Ojca62IiO0mdc-oPK5WFKBs0wbL8II_dFZRbfd_8hIhcupd7hKG0l5sHMHk3QyDiHNrvMYiM7luTtCFgvffHG3hGny3hiFzyD6rJ-Z_4Uzqc8UEEunzaSblHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=DAoLSygAd4gV4i2ZXHak1RH3rE6x_jsM89j_-MVAAVp_PvzwHicu4eQtKKc_6wJTwDGcnds_9PgPNLRe1jLm4sWkMQwqsMOakbIRXIjU-9KNh04XPNCMfBVfToWDvpiZwQ1ek_679sEekduScIalwoLRbd9AVFx2suOiqxznBz5R_Vo1kHNu2lyg2DMUXn3VmLoWuU3SMzMRJSF4p58a2WsEF0O6_Ojca62IiO0mdc-oPK5WFKBs0wbL8II_dFZRbfd_8hIhcupd7hKG0l5sHMHk3QyDiHNrvMYiM7luTtCFgvffHG3hGny3hiFzyD6rJ-Z_4Uzqc8UEEunzaSblHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
کتابخونهٔ رایگان Melies برای تکنیک‌های سینمایی
یک کتابخونهٔ آنلاین با ۴۲۴ تکنیک سینمایی، از حرکت دوربین تا نورپردازی و رنگ، هر کدوم با پرامپت آماده.
هر تکنیک شامل:
🔍
تعریف ساده
🎭
اثرش روی حس فیلم
🎥
مثال ویدیویی
✍️
پرامپت آماده برای کپی
این مجموعه رایگانه و نیازی به ثبت‌نام نداره، ولی خود سایت Melies یه سرویس ساخت فیلم و ویدیوی هوش مصنوعی هم داره که پولیه.
اگه دنبال اینی که یه حس یا نمای خاص رو توی ذهنت داری ولی نمی‌دونی چطور توصیفش کنی، این کتابخونه دقیقاً برای همینه.
📌
کتابخونهٔ تکنیک‌های سینمایی
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1ZQPeqFi4NRxRLTUIKRmH9W7Y2zeocZTuv8VWDh4win4qZt-vPgLi45XZHD_wcLDEOjwbjfdOh_1x_Iuv17K81BgYT8sserxnqxTh-CrfDxSfoS2D27noD808wyxX1XAcvnD8CTzCzaV7I3dI2dhZ0nVZVNl1yKYK3yic0BZA5rqgYdCcRLSDtVqc7_7kcxFsadibYD66uMXNvfz113F9cNoFxV7Ky6OVJaYytOgoyQxc6hgYJSyLxR2XtafXRnzrun6LpIQ1Ye7iIA9_w8HA-wxfqMaac81peVazJxggG1HURemBvaBj22eOT4LQZDRsOeR8CtKHXj2_Bu4wkVNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🆕
مدل MiniMax M3.1-Flash-Preview بی‌صدا منتشر شد
⠀
‏مینی‌مکس مدل سریع تازه‌اش را فقط داخل MiniMax Code فعال کرده، نه روی API عمومی.
⠀
‏
⚡️
ساخته شده برای کار روزمرهٔ کدنویسی، از رفع باگ سریع تا پیاده‌سازی یک قابلیت کامل
‏
🎛
در انتخاب‌گر مدلِ MiniMax Code کنار M3 و M2.7 نشسته و حالا گزینهٔ پیش‌فرضه
‏
🎁
ورود روزانه ۴۰۰ پوینت می‌ده و روزهای چهارم و هفتم ۱۰۰۰ پوینت؛ یک هفتهٔ کامل ۴۰۰۰ پوینت
‏
⏳
پوینت‌ها ۳۰ روز اعتبار دارن و روی کدنویسی و سند و تصویر و صدا و ویدیو خرج می‌شن
⠀
‏قیمت و سرعت خودِ این مدل رسمی اعلام نشده؛ عدد ۱۰۰ توکن در ثانیه در مستندات برای M3 ثبت شده. روی API عمومی هم M3 با تخفیف دائمی ۵۰ درصد، هر میلیون توکن ورودی ۰.۳۰ و خروجی ۱.۲۰ دلار حساب می‌شه.
⠀
‏به گفتهٔ PANews از ۲۸ سپتامبر تا ۷ اکتبر اعتبار ورود روزانه دو برابر می‌شه و سهمیهٔ Token Plan هم ریست شده.
⠀⠀
‏
🟢
ورود به MiniMax Code
‏
📝
سند پوینت‌ها و اعتبار
‏
💵
تعرفهٔ پرداخت به‌مصرف
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMaRA4lUXa2XpoyCSlJcI4TU56A4xFZ9EcMUqCiFqY3T_2u54g6Q39Dpg-gwo46N-C1cKa8JC6gAmy26gtp1RncmMQbOq0xhu-wPx7bjC3I_oUOjFgYlc6Dwb3mv0eTnXZMSoUIEAwr4CJ6SRq5gbysfOnQlaI3S_aeivDnpD4V19sRBpYnmz49DFG8NaJ2Hm1XDXP9U-_OZQ9JKO_8SMOxMa9muIOtWewWXFIc3eHfCucNYE20qYOVJFtnC0_NV77c15fxtpZDgiQ13ZTlpLROnEneFKHgvnFFv33JB7jFelSa-1Vm-nnmYmz07_8A0S_aMl0_fxTisSnjwS8GyuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Railway.new
یک VM لینوکسی رایگان در فضای ابری
💻
از حالا railway یک ماشین مجازی لینوکسی به شما ارائه میده که از طریق SSH میتونید بهش وصل بشید
💥
برای استارتش فقط کافیه داخل ترمینال خودتون دستور زیر رو وارد کنید
⌨️
ssh railway.new
⚙
مشخصاتی که این VM در اختیارتون میزاره :
• ۲
هسته پردازشی
• ۲ گیگابایت RAM
• محیط لینوکس
• دسترسی SSH
• Python
• Node.js
• Git و GitHub CLI
• Chromium و Playwright
• Railway CLI
• چندین ابزار AI برای کدنویسی
🤖
بخش جذاب ماجرا چیه ؟
چند
AI Coding Agent
هم از قبل روی محیط آماده شده‌اند؛ بنابراین می‌توانی
Agent
را اجرا کنی، پروژه‌ات رو به اون بدی و داخل همان VM کدنویسی و اجرای پروژه را انجام بدی
⚡️
🌐
برای پروژه‌هایی که اجرا می‌کنی، امکان ایجاد
Preview
آنلاین هم وجود دارد
👎
تنها عیبی که داره :
شما فقط 60 دقیقه فرصت دارید ازش استفاده کنید ، وقتی 60 دقیقه شما تموم میشه به شما 24 ساعت فرصت این رو میده که فایل های که باهاش ساختید رو claim کنید تا در ادامه بتونید ازش استفاده کنید
❕
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBEDzMdP_2o7z6P4MKTF976y-8_dj3niKQYRmm16UUowgcavkZ0NzQBlki5aKbZl_iopJFoQOAVu0nMsjhEs86kM7INuEdBW9wpAiXFzM58EIShSgiUibDX5rKNODxGx_Swks48u4_8LJ1w_vgYqrZICDNl3j9C5m8w04eBOw7LHzyoYf1-0QAiRjQMdwVUVL-15VW_fCkVdRyTiFiYtUp5Ug5bOaW58jAnjZesVzqM6Y3K7qgkgM0p_BXiFMun_XzQlafYfITZwWlgtW_9e4nlUDDyYcVmntYbsgfHVZoHqCV8T451cZc53dqoKaemGvuT4lPyW_H-wDXTG5OZB_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#حمایتی
‏
🏔
آرشیو Afsaneha برای افسانه‌های محلی ایران
⠀
‏یک سایت متن‌باز که افسانه‌های شهر و روستای هر کسی را با نام خودش ثبت می‌کنه.
⠀
‏
🗺
نقشهٔ استانی ایران با SVG خالص؛ روی هر استان بزنی افسانه‌هایش میاد
‏
📨
ثبت افسانه بدون حساب گیت‌هاب؛ فرم سایت با Cloudflare Worker خودش Pull Request باز می‌کنه
‏
🗄
هر افسانه یک فایل Markdown در پوشهٔ استان خودشه، پس با رفتن سایت هم آرشیو می‌مونه
‏
🎙
پشتیبانی از فایل صوتی برای روایت با لهجهٔ محلی
‏
📱
نسخهٔ PWA و حالت آفلاین، دو زبانه با چیدمان راست‌چین و چپ‌چین
‏
📖
حالت مطالعهٔ بی‌حاشیه و تم‌های فصلی مثل شب یلدا
⠀
‏فعلاً فقط سه افسانهٔ نمونه از تهران و فارس و کرمانشاه روی سایت هست و نویسندهٔ همه‌شان «نمونه»ست؛ یعنی آرشیو تازه راه افتاده و جای افسانه‌های واقعی خالیه.
⠀
‏
👇
اولین افسانه‌ای که از شهر خودت شنیدی چی بود؟ همینطور شما اسپوف‌نژاد؟
😊
⠀
‏
🌐
سایت افسانه‌ها
‏
📌
فرم ثبت افسانهٔ جدید
‏
🐱
مخزن پروژه در گیت‌هاب
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNrMmqjyrqcYdX_EsLzJnmP73KqRno3RQc2RD7L7qV1F9LeNBZgIMIb4SgBK2YakuTepkH3Gc03Qo79J0dvcnAxpXnMfJRF13ceI6A4UOpQky1bsKwMaaxtjP5Ot-rBcCVfXQcUhkD8RM-J8LBk2l1a76PbFcc2sC2_jZTbI1JHGy6SX7a2l8J8Wc048P-VXx7YI3LCEocwb60UY5KlFTzqtXxz-UVJLGoUYtNJD3H1jQm0gFLGiaAPNG1pDIHMvQ7RQVggNSDRQIuorPvsenQzFZl9ArGDWubDZVyt12trss3JQiyNeHj7DNeNAGj5nt_p-yhkX7ija7gD_eFs1qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API برترین مدل های جهان
💥
Opus 5.5 | Fable 5.1 |  GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 Pro 0813 | Sonnet 5 | Gemini 3.6 Falsh
✅
با این سایت میتونید ۵ میلیون توکن بابت تست مدل های بالا دریافت کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfC2J0sOiJSRSkzWTTycIxeHZzwD0gc5Q0EtpFSB8E30OmeyzrphXwgG7CzuSrSDoGQc22_86RYobeS-kqpICruTLevx2L4s5ydL9fyAC47yDUalLkAKHVMrZwz1cwagCDUwoUf14gD1jAactuf5Aq6YklHl6r7S5-kVUbbq-90SJ-awWBiQYzbeQNdbCFjWWd6HjmWt9NlN3FzBFA_fe78SBNJ5I_y_ZDi5VyDqNgoGBv-jXTK0xDXzZ07Lu9fz7bLbBvNQMnHMzvy2uWzBcvZmH5P0iZ7pG_OMY9k_wdKWvr3ddV9UkAziBnZoOeO99--nhLMJPupcj7C1cOBJTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل‌های هوش مصنوعی زیر
💥
🆓
Opus 5 | Sonnet 5 | GPT 5.5
✅
این سایت بهتون یک پلن تریال ۱۴ روزه حاوی ۲۰۰۰ کریدیت میده تا شما بتونید این مدل هارو استفاده کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWb7CAC1kreFR9BQ3Sr-L_FEkda3YaxYmLlau69_aBNzHQPxLMOoTKbYIExjC-8Fdp_Pttah2itC4r-5wwL90slykvKBa0ep5y4-n4p954kOIfhK_Fud_3JvP0_QVslzyJTNwWxi2yaA538JeXopyjk0exg2Uq3xPCvYHxFf3HXKVBpajYwyGGFzusVEIcyBsQW6LPDMscT1ewoXMF8fERsrEoZGOZ13jhcpteYE524eHfaicep9kVOnc5EgpjHYG7W2v0li9VwmOjzq64KwA7AlwHOyhZ9Z7zxKNs9lCppZ_9YIm-HFueA_Jz7AhI94_blOviFaJJ__ffjXbo19Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
ادعای نشت اطلاعات JumpJump هنوز تأییدنشده
⠀
تصویر فروش دیتابیس کاربران این فیلترشکن دست به دست شد، ولی هیچ منبع مستقلی پشتش نیست.
⠀
💳
شمارهٔ کارت ۶۰۳۷۹۹۱۲۳۴۵۶۷۸۹۰ آزمون Luhn را رد میکنه
🏦
پیش شمارهٔ ۶۰۳۷۹۹ مال بانک ملیه، ولی زیر شماره اسم Bank Mellat اومده
⠀
آزمون Luhn یک حساب ساده: رقمهای یکی در میان را دو برابر و همه را جمع می‌کنی و جواب کارت واقعی بر ۱۰ بخش‌پذیره؛ اینجا ۷۷ درمیاد، پس شماره ساختار درستی نداره. ساعت ۹:۴۱ و محو بودن دادهها هم نشانهٔ قوی ماکاپ بودنه، نه مدرک قطعی جعل.
⠀
اندیشه معاصر نوشت هیچ منبع مستقلی اصالت دیتابیس را تأیید نکرده و شرکت ادعا را بی اساس خونده. بررسی Tom's Guide هم سابقهٔ نشتی پیدا نکرده، ولی ۴۸ از ۱۰۰ داده: سیاست لاگ مبهم و بدون بررسی امنیتی مستقل.
⠀
پس ترجیحاً از سرویس های بررسی شده استفاده کنید و اطلاعات کارت را داخل فیلترشکن وارد نکنید.
⠀
📌
گزارش اندیشه معاصر دربارهٔ این ادعا
🌐
بررسی Tom's Guide از این فیلترشکن
🏦
جدول پیش شمارهٔ کارت بانکهای ایران
⠀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9-xLDDHkj_gAZO75BTH_Z1CXzQAsgPfzpe_zBOG0cdrHzcemFdN3GUdq1CjLVpISXmBvLBUZglsjHSQ84T3bNy2fYpS3jaiCROkoypnXBxFHQ2pahrTKuUilW9wBPiB-3qWVXzoRA103dM_31v_qtBt9Oex5_extcVb48g7zXUYQGTd97agohUBYxIyKVA_D1AYJxsyRC-PJayMUzWcYvEwLMVF1fx6PXSoT_Iya11-BnZfct539Mw9_mjBB5J9IHdzq_sw8AJiLiVR9T1kyMupNzbYZBOLwO2PnR7LF9eqLPCqUQYF5nPotOfX-1q9By-Wyo07Acn0kyom0KbF6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های SI در یک بنچمارک سلامت روان، از پزشکان متخصص امتیاز بالاتری گرفتن
‼️
- اپن OpenAI نتایج یک بنچمارک جدید در حوزه سلامت روان منتشر کرده که توی اون، چند مدل پیشرفته هوش مصنوعی تونستن امتیاز بالاتری از پاسخ‌های نوشته‌ شده توسط متخصصان سلامت روان کسب کنن.
🤖
مدل GPT-6 Astra: ۵۷.۳
💠
مدلClaude Opus 5.5: ۵۲.۴
✨
پاسخ متخصصان: ۳۸.۵
- البته جالبه که متخصصان بالینی در واقع جریمه‌های کمتری دریافت کردن. طبق توضیح OpenAI، دلیل پایین‌تر بودن امتیازشون تا حد زیادی این بوده که مثل زمانی که واقعا با یک مراجعه‌کننده روبه‌رو هستن، خیلی کوتاه جواب می‌دادن؛ گاهی حتی فقط با یک سؤال یا یک جمله.
😁
- در مقابل، مدل‌های AI پاسخ‌های مفصل‌تر و کامل‌تری تولید کرده‌اند و همین باعث شده در این بنچمارک امتیاز بالاتری بگیرند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6mkZD1WpnEqiUn1TyersFvMaEa7Va9Ov36WPkTW6kiAREI-drYW-Rx7XbiYeZ6hQ5ckKHWwPPWaVSlriCyRurLp4-_YNnKi8sJy67YMCeXC8VIFpYX0KDWxGL_wfqUWpoyhthU3ndN_KN4Di3YbFXaiOofFABN8hTndkuV8HpyrNO3jsPUxQsajcQh-n6ckyQ_xUKoYpvaiO9BQXpTizVlUEpF7-TVu44jlQYYFMkZoB2WLSdbkFBJIM9cq7Rpo2Jm5E8M93zO9KYjp98t9Abq6T5wtLPBm2Pk3XenuGHr-F_nYLRXn0VUugnFGzredevD1UKD4vupDdIPi3Rk2Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
مهساNG ویروس نیست — ماجرای اون عکس چیه؟
چند روزه یه عکس از مقالهٔ MVPNalyzer دست‌به‌دست می‌شه و می‌گن «مهساNG ۳ تا از ۵ لایهٔ امنیتی رو رد نکرده». مقاله رو کامل خوندیم؛ اینطور نیست.
اول از همه:
این مقاله اصلاً بدافزار بررسی نکرده. فقط رفتار شبکه‌ای ۲۸۱ تا VPN رایگان گوگل‌پلی رو سنجیده. پس «ویروسه یا نه» اصلاً موضوعش نبوده.
دوم، اون ۳ تا اشتباهه — ۲ تاست:
تو جدول مقاله، «Leak (29)» و «DNS Leak (24)» یه ماژول‌ان؛ دومی زیرمجموعهٔ اولیه. کسی که شمرده، یه ایراد رو دوبار حساب کرده.
واقعیت از ۵ ماژول مقاله:
❌
ترافیک رمزنگاری‌نشده
❌
نشت DNS
✅
نشت ترافیک کاربر — پاکه
✅
قابل‌شناسایی بودن (۱۴۳ اپ گیر کردن) — پاکه
✅
ردیابی و Advertising ID (۷۶ اپ گیر کردن) — پاکه
✅
کانفیگ ناامن OpenVPN (۱۰۷ اپ گیر کردن) — پاکه، چون اصلاً Xray استفاده می‌کنه
یعنی نسبت به بقیهٔ دیتاست، جزو بهتراست نه بدترا.
اون ۲ تا ایراد یعنی چی؟
🔹
نشت DNS: محتوای مرورت رمزنگاری‌شده می‌مونه، ولی ISP می‌بینه چه سایت‌هایی رو باز می‌کنی. برای فیلترشکن ایراد جدیه.
🔹
ترافیک cleartext: مال خودِ اپه (مثلاً گرفتن لوکیشن از
ip-api.com
)، نه ترافیک مرور تو.
یه نکتهٔ مهم:
داده‌ها مال نوامبر ۲۰۲۴ و با تنظیمات پیش‌فرضه. اپ از اون موقع بارها آپدیت شده و نویسنده‌ها هم ایرادها رو به توسعه‌دهنده گزارش دادن.
✅
کاری که باید بکنی:
۱. بعد اتصال،
dnsleaktest.com
رو چک کن؛ نشت داشت، DoH یا Remote DNS رو روشن کن.
۲. سرورها دست آدمای ناشناسه — بانکداری و اکانت حساس روش انجام نده.
۳. خطر واقعی، APK تقلبیه. فقط از گوگل‌پلی یا گیت‌هاب رسمی نصب کن.
💡
و یه حرف با کانالای عزیز: ترسوندن مردم ممبر میاره، ولی اعتبار نمی‌سازه. وقتی یه مقالهٔ علمی رو نخونده تیتر می‌کنی، به همون کاربری ضربه می‌زنی که ادعا داری ازش مراقبت می‌کنی.
اصالت مهم‌تر از ویوئه.
پستتم ریپلای نمیکنم. اینکه خودت اپلیکیشن مود شده خودتو میذاری چنل معلومه چقدر به فکر پرایوسی و ترکر هستی.
📌
فایل کامل مقاله
🌐
صفحهٔ مقاله در NDSS
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUH6ntpy0I38oitNyF5Y86vCrjr2IN_oq6UxFYKWVWRM7FGM60u4IEW39kOX1K7Vua1Iph5QolE8nnV07lnPUimQ9swk_n49yPCmXDWSI6lSMM_UuluPEEWmDukBlQsNeAKuSPjWPGnS6MX_IzM6DwKG_wr9wkJoFHkunaAwHUUxI8idf_7MpqGexP7l8Uma_W5PCs-xYjCzPRBH_i6xugkRUtLA8pMhVss9Y6OHyAKxPn78bzwrVRngPNleulhgJnsaK8QOSlOw0kGZdjecPO0pQyQsL34DsHNYjmSSlU_zxyptuVVDJROsoMKFdM5URFV15yiIJPxdvyyv4xDwhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">500 دلار برای دسترسی رایگان به برترین مدل های جهان
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این متد میتونید از سایت معرفی شده ۵۰۰ دلار برای ۱ ماه برای تست بسیاری از مدل ها دریافت کنید
✅
📌
دیدن آموزش فعالسازی
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hg2KcZHWTV8hDLGlu0XOrm5F5L_ItWFJWm9tDa-fQGxb-lbMQoG6I3pxL4Q0TqxUfblC_MiwhMgu44phY58Be4K3BSrGOHxz-JRGf0Jou14X9ymsK8gGV3wmeBn8YKWNf_7WfLWXYb9Zi6KFzd2g50SsiTa_tLbyFmfqoBrcedyV5L6WG6rITRHOygqvj1umbAktSdhUBTNH3o-8kMoP9x6Vk0fYFcEVXeEgd3wSgvzIQVSveSVObPooAEsnw3EuXXGz3yQYZWuJPOiudWr55SOeHvqAlWJp6W9Tfkq5SFiyClBnDFFSyHgK4XYMUBxlrcBDKfXN3U6R8a4zNGg9RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTlM2DhZHBtZQJUm1LwUzUyXZptwzDaaQIa6oCb7ICh-q30q6Abw0UJyROWawS7O_PTiVOtiRaoP1OyhE87i6SGFGsbw7X7TUERWRIfH70qRhKt_Eer2x-OyUPBkcV_inrrPCYimocJfEpQy7E6Dt8ojBSZhm6tbhrUngJ9RZNh_O7EH7Vrzt7wWQSOgiIDFk8b1XTY3mN4uIu4t3r1FJUeErY2eWBKb4AQlc0jbn6JlYRMphhDi3o3C_qyVF_rS8uuvoY84phUuwlpPamhcXY89e6KIHxUMg3oexkfwCa9kgzHhNHgHpvWueo2ZlYrmzhIcgldbGzEBLPVpu-DQSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌈
کنترل نور قطعات با FullRGB بدون نصب
برنامهٔ FullRGB نورپردازی قطعات رایانه را با یک فایل اجرایی و بدون دسترسی ادمین کنترل می‌کند.
🤔
۱۲ افکت
: کالیبراسیون جداگانه برای هر زون نوری
🤔
پوشش قطعات
: مادربرد، رم، خنک‌کننده‌ها و فن‌ها
🤔
دوزبانه
: رابط انگلیسی و فارسی
🤔
فقط ویندوز
: نسخه‌ای برای لینوکس یا مک اعلام نشده
💡
نکته
: موتور OpenRGB داخل همان فایل تعبیه شده و نصب جداگانه نمی‌خواهد
📌
صفحهٔ پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpErzit2TfnkC0Uys-wHIurKQRSi_9ARkyCLBAROPRaiMoPSRGzJ2L2f_b0z10xA5VpyIyGa6sBq6mF_q9WMhhJ8U43ynxW-NahXYTyFxZ4C59Ew72yehUzwdLdc_qaJjNl1hpWpdMC593FQrQ8YAEGXCuNmEmLAQH6DVDpb7bgohAyoec9RSkLWlf-f68D964DccMCVhcrgGXFlguAhZKvdwyvtQ9LyN8YQGo43NW4Nj6xDTidEy1yc2KKw2GVM4uaiOrUUXyJgSutEv0zCzHE8yOXpO5LskI8kjzITsPfJE_4eiNf8z6JvqoLd3MNCJ0zjmDirfaCRSRjnWnHd3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧩
#حمایت
| پچ راست‌چین هوشمند آنتی‌گراویتی؛ خوراک بچه‌های برنامه‌نویس!
‏رفقایی که از آنتی گراویتی استفاده میکنن این ابزار خیلی کارشون رو راه می‌اندازه تا بتونن فارسی رو درست و حسابی و راست‌به‌چپ بنویسن بدون اینکه کدهای انگلیسی‌شون به هم بریزه.
‏•
🧠
هوش مصنوعی دوزبانه: با فرمول نسبت ۷۰ درصدی حروف، متن‌های فارسی رو راست‌چین می‌کنه و کدهای ‌LTR⁩ رو دست‌نزده نگه می‌داره.
‏•
📦
فونت‌های ۱۰۰٪ آفلاین: وزیرمتن، شبنم، ساحل و صمیم به صورت ‌Base64⁩ تعبیه شدن و منتظر اینترنت نمی‌مونن.
‏•
🛡️
امنیت کامل کدها: پنل‌های ادیتور، ترمینال و لاگ‌ها کاملاً سالم و چپ‌به‌چپ باقی می‌مونن.
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0go5cXjFt-Esc0VK-i2Tm5qv1RaxXHsDOAsG_3d_w_nxBjS8-f6Y6GwdTuYh0wKIduwFCG4W5Yl1cwUTSTNnxeo7rR_p1P_n6o0UF8mqYW-C9S9alOsi8YEG_2zSkhjMVqEdtp-fIAFSvUd3Rrvv5omlM6QmY1R-hDIxzcLwtWmc5JBzah4CoWkegiJ9hffy01E1ZZ2jY9k66tWbwNJeo2AjaPdlxdDi8v8PRMl2oBP2D5Aafn-Z7RGB3MUB23UMqXXh0DLXs_kRCCXHvK191bXZDJFBoX3wz4MQIEZvhbE9ClfG2idG75tT5tPgtT-5ixOZ75uu_w8sNbghI_BCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8PuDNd59rp9TrQ6J3Oo1W7hCAtVusNg6__RgHolKgkY6NPwtVNzyR_DHc2zfT24yem_ue8-ey7KeCQ2KFOBtZ0hHegVGy9SFI89j1BB0XJiZtq69IFECLu1pYSXXs8WjMUkfDWYc7R_WOg4ORvFvsBpidarKSbXc26CkRdOxwIXbNhP7uVdmtBLCoo2WAPptO8xoUTPKbhjeU5PSLDfSspYRNsyQ1JVwL4-OJ59iUG0nkYxbov2ilNEDfZ3dlCaXnuZ8n_0gtTi40n6PSk83WpuaH3jopCkzHEKjVUOrnXjWRp3EX1kEgDeP8wN-YgLdQPOQS80xCsC3FzieLjC9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
در
یافت رایگان ایمیل دانشجویی اسپانیا
با این روش می‌تونید یک
ایمیل دانشجویی اسپانیایی
به‌صورت رایگان دریافت کنید و از اون برای
وریفای برخی سایت‌ها و پلتفرم‌ها
استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell
| METHOD</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
نکته مهم برای کاربرای Antigravity
اگه اکانتی که باهاش کار می‌کنید عضو یک
Family
باشه، حواستون به این موضوع باشه:
لیمیتتون در حالت فمیلی، به‌صورت
اشتراکی
بین تمام اعضا محاسبه می‌شه. به این معنی که اگر فقط یکی از اعضای فمیلی مصرفش پر بشه و لیمیت بخوره، کل اعضای اون فمیلی هم‌زمان لیمیت می‌شن و دسترسی‌شون محدود می‌شه!
💡
پیشنهاد:
برای جلوگیری از این مشکل، حتماً از اکانت‌های مستقل و خارج از فمیلی برای Antigravity استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiwyJRo9iGnOwRr3H3_vljVsDlbG62ep39rkjkIq0zY4z3dc5ntXiAiR6OLTio7ju2GmGOsSWmON8QsvjBuE2LkffK3CeSEQ0vpaNfwg_aA5hzqKxMC3enOEoYDd4GBA0kekmlpGGW-JXA5xvS4-nH2pG1VWopzGoBbK-za5F4pcP9zw3DKjIkTLTUTQI2JqXpVB_yuIKyFYxagBLCstRbMb5ABawxD0nWI5JW3L7rccjUUM7gT3Y6OYl6qUkDOLdxSzFId2T-HZn667vtQO4TVnlfmW2uDUGVr6o3BPJ47KG8LG4x8x55qxsOi0dDh_O_tOfeoRoW06vubEuUaoKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
طوفان جدید گوگل، جمینای ۴ به زودی...
💎
کوری کاووکچوغلو، از مدیران ارشد و مغزهای متفکر گوگل دیپ‌مایند، بالاخره سکوت رو شکست و تایم‌لاین اس آی به شدت مورد انتظار
Gemini 4
رو فاش کرد!
🤯
اگه فکر می‌کردید هوش مصنوعی تا الان پیشرفت کرده، کمربندها رو ببندید چون گوگل قراره بازی رو کلاً عوض کنه.
⚡️
چرا این خبر مثل بمب صدا کرده؟
🤔
پرش کوانتومی در منطق:
جمنای ۴ فقط یک آپدیت ساده نیست؛ قراره مرزهای استدلال و پردازش داده‌ها رو به طرز وحشتناکی جابجا کنه.
🤔
تیر خلاص به رقبا:
با این تایم‌لاینی که DeepMind منتشر کرده، گوگل رسماً شمشیر رو برای بقیه غول‌های هوش مصنوعی از رو بسته تا بازار رو کاملاً قبضه کنه.
🤔
یکپارچگی بی‌سابقه:
حدس زده میشه که این نسخه خیلی عمیق‌تر از همیشه با زندگی روزمره و اکوسیستم ابزارهای ما ترکیب بشه.
نانو بنانا ۲.۵
هم احتمالا باش عرضه بشه شایعات میگن
۱ اکتبر
میاد تقریبا یه هفته بعد
👇
به نظرتون Gemini 4 می‌تونه رقباش رو برای همیشه کیش و مات کنه؟ نظرتو تو کامنت‌ها بگو!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3fcVkkOz1WnFBLN4npuLKlDR8jfAd0t21SCJzwslk-K0Wf7oOi-UMBCSGlRJAnhXVFlxOuGK8x43dIYJohkP-QUOjDX9W-bII-JQ3I6UqD-89DQMgTdmgdQSnj0pIOZi-nD3_5sVXBGtoyDs8F48JmlcRB-IdskhbmxuW_98XrI_oSbPhdX4TIDYZ3kZVcRm0ih54DeNtAHFEhWF_obDm_YBORkxo1K5bSkcei4AJvcXQibPu5lV2ESt5xNuNVF-eAouyXgprxFEJ65v9xoWxEEL7TaHo85ohOtWOSNTTGZoq63SOEO-wziqoAJAmMDgvCfNtI_MYYfG21fW4yxhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت
| کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی
به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک
: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
داوری میان گزینه‌ها
: چند راهکار یا مسیر پیشنهادی را می‌سنجد و برنده را می‌گوید
🤔
شکستن حلقهٔ تکرار
: وقتی دستیار یک کار شکست‌خورده را تکرار می‌کند، متوقفش می‌کند
🤔
نیاز به کلید پولی
: هر میلیارد توکن ورودی ۴۲ دلار و نصب با پایتون
💡
نکته
: مجوز MIT برای خود کتابخانه است، نه سرویس پولی TypeSafe پشت آن
این پروژه یکی از ممبر های چنل هستش.
جهت ارسال پروژه هاتون به دایرکت پیام بدید
❤️
📌
سورس پروژه در گیت‌هاب
🌐
راهنمای رسمی فارسی پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7868" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7867">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5y-w50c1JlkHxCiBtWkyzj7nd94E9JzVevxW6qTwT4JuqUIJhBXgzKTBEA8VmkKvQZB1mOhhmfz1Tba3dl7GiAn5jr84DyYiEFCcbaGpoGhDRm6qypDTuUqwUpDskvAJMt3BNjbjDAMBxMdGPaJMWTOPnLHXKrLK_ZyRsqD0RkvaCGFakJ3ypLjUKix07H9B_dKdK4v2INGHw2_onW_a_uOSQ1EtVU3VadCexZNWfAuxXVYaEz7sQlmCV_Grf0iz52W32V8HF8d3DRTIqEjG-1zz5saDYGAnZAt_GRPCUk3uB9E2y7gTI5NiMBj3ma4o5xq1KwjedWl9oQrS_MEEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
ابزار Perfect Windows 11 برای بهینه‌سازی برگشت‌پذیر ویندوز
با دسترسی مدیر روی ویندوز ۱۱ اجرا می‌شود و از یک منو هر بهینه‌سازی را جدا روشن یا خاموش می‌کنید.
🔺
بستن ردیابی و تبلیغات
: تله‌متری، جمع‌آوری داده و تبلیغات نوار وظیفه خاموش می‌شوند
🔺
پیش‌نمایش پیش از اعمال
: فهرست تغییرها را ببینید، بعد اعمال یا بازگردانی کنید
🔺
پشتیبان‌گیری خودکار
: نقطهٔ بازگردانی ویندوز و نسخهٔ پشتیبان رجیستری ساخته می‌شود
🔺
خاموش‌کردن هایبرنیت
: فضای دیسک آزاد می‌شود ولی راه‌اندازی سریع ویندوز از کار می‌افتد
💡
نکته
: مجوز MIT دارد؛ استفادهٔ تجاری با نگه‌داشتن اعلان حق‌نشر و متن مجوز مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7867" target="_blank">📅 16:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7866">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIrlmUat1POHQwLK2ujCzm2vxykpd-xD11YlJcH6L48LQwPBUkU-FlmgzHiXdpc9-a0D9i8DfLxIX30BFgKok10Fc0shjHijdt-w04CFKXhgQ9VmG7ZAXMtmNRUJLhnVImXRwahQjMs7X3p1upiBcug2-9yPVweiIS3Iz1eykwtSUPiv1ekWokyj8mQYx7kf5GaFt9vKDwWxuY1Z9QBkCHPBv933U9bwjgyOgH3FOFA3-g9hk-BgkfH9c7o2wATCAsmGs5P-Lw8OgCARz8IIuzNX33ar5y-NC1hCEhuoEoMiSE1YuKoSvwzfaKiUwgMqu66Mnj9OZapxZoNHe7mlHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧮
مدل Laya که به‌جای نوشتن جواب، تصمیم می‌گیرد
یک ایمیل و چند پرسش می‌دهید و برای هرکدام گزینه، نمره یا بله و خیر با احتمال می‌گیرید.
🤔
پاسخ در ۳۳ میلی‌ثانیه
: زمان اندازه‌گیری‌شده برای یک پرسش روی کارت گرافیک
🤔
بیش از ۱۰۰ زبان
: خودش زبان متن را می‌شناسد و مدل مناسب را برمی‌گزیند
🤔
دانلود مدل و اجرای محلی
: بعد از نخستین دانلود، روی دستگاه خودتان کار می‌کند
🤔
نیاز به پایتون ۳٫۱۰ یا بالاتر
: با دستور
pip install laya
نصب می‌شود
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با نگه‌داشتن متن مجوز و اعلان‌ها مجاز است
📌
اجرای زندهٔ نمونه در مرورگر
🌐
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7866" target="_blank">📅 13:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7859">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VDgmnHvRydtKVTsM-4ygMvbznXZHNJtBHiOlkuw4-z7z56c6VJhlxpOFuuGvJXW2HzGHswsqy-lCdV7y98asaZdiZ0I8lL-Mm3zammd3Ek8I2empu86lovdJKTSSEUzzF0GOwvLNiJPDCTZvLtLhYzK4c3YHZ_jnPWnldLkTW2bkhPfcigzvjLmSYq8ZV5BCU7lOL7fFV755yX4YtVltkiDm5-iZ2lVJL-byAfv8JetZr13B7qzuhzl6Q2hesu89d0qKWdvlF29zJJUhXrCH3tUOh-vf6hPw3oumOQ1C89LaHtQA0wivsQA7eWhcN04On_e6SNpORqROPowPNEr1lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWwULMB61yShUwAbEYj4LwlxKpD4yDXc9pNEy7mss6uW1M5NCZHs2CDV173D6uJJPEx0yucCkEFT8Gdo2fh5eMlvdBHLMgZ02EURQvHIvANSNYrqGQwWAWuOtpSxfwyUzQxJSZkjlEag1M3T_fnZFQHm7p1q9yoH89-ZjRtdmnBf4OkNdCWHmzxvoyGgO_XzQUdk2ccWivmPXf5IFpTVB9VUbA2QD1qGfY5Q7ncO80AYGaLH_g2bDc10taT6khTysetWCX2pmo4N-muR9f6QBVJiCWPJ09H9aKD475O6QnlVuj2C0jxT6nvfoNOV-5yz3wZc7jBJ_6JsIbZjArt2Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YaHfbYkgzKtDa3A-izkWJqVWj3J1puLmxUPcAHz5A2gb1MfnB0AxDaDwGglMk2dLbP7OEUI1zwQfAgf3rgS43zBKubNebr05B94K_AWpMajh-5xJR8jyovfAMzCvJ_MHFWDE4yhh8OVVYW--Pkv0vy1DTd8a9s7yyP7GI7n38iFuYh21ZLVsDAAis0Qqin_wyXhPGNs_J7NbTHCZU5EoPynMoSvXxPp4o8_jnZ_sgfCGn-au_3GkWlv4Yyev3esJ7InZ4_hpfZn9JaEO_26GBQM52sY4pJgO2r7UTvO0vcI3zq5ygwTgyZUbJqDFbp9U6lUccD7YItTrR7xDCcMHEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=C_kCN8sYsSWa5Z4X4IUfxlsPw0sO2doNofhhxCb1dTSH4BOTwXlQgTui5iBsu8DB0ArExQV0eimjdWe_1sLH8WWakQZcrfKyB2uwe9daIH44f9Eny1KHE4gpztkZMd2PrxBMVllKt4gq3X42ORY3_S9znreb18boI2EiHpSNdnJZ4HSB-Z2YDYPaZv7_-ZoSNzI6qVq0A0elpSvsU7GEhGryVBb4Fx4v4gTrd9JRxmabT6PLvD8PsJfY7gqz9sJw13b5w5L3bKWtSOul_ShmoMTXEltUEAiROxcmsYyDOW5dQEtRTrC_UPXn4spC458Gjgk7NuuD1xe9SXP10t4UJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=C_kCN8sYsSWa5Z4X4IUfxlsPw0sO2doNofhhxCb1dTSH4BOTwXlQgTui5iBsu8DB0ArExQV0eimjdWe_1sLH8WWakQZcrfKyB2uwe9daIH44f9Eny1KHE4gpztkZMd2PrxBMVllKt4gq3X42ORY3_S9znreb18boI2EiHpSNdnJZ4HSB-Z2YDYPaZv7_-ZoSNzI6qVq0A0elpSvsU7GEhGryVBb4Fx4v4gTrd9JRxmabT6PLvD8PsJfY7gqz9sJw13b5w5L3bKWtSOul_ShmoMTXEltUEAiROxcmsYyDOW5dQEtRTrC_UPXn4spC458Gjgk7NuuD1xe9SXP10t4UJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
مدل مخفی Space Bunny Alpha رایگان شد
مدل مخفی Space Bunny Alpha اکنون روی OpenRouter و OpenCode در دسترس است و فعلاً رایگان ارائه می‌شود.
🔺
پنجرهٔ متن تا ۱ میلیون توکن و خروجی حداکثر ۵۲۴ هزار توکن
🔺
پردازش ورودی متن، تصویر و ویدیو با تلاش استدلالی قابل تنظیم
💡
نکته
: رایگان‌بودن این مدل روی OpenCode فقط برای مدتی محدود اعلام شده
📌
صفحهٔ مدل در
OpenRouter
🌐
مستندات رسمی
OpenCode
✈️
@ArchiveTell
#Ai
#هوش_مصنوعی</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
