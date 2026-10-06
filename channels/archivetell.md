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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 22:44:37</div>
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
<div class="tg-footer">👁️ 667 · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 671 · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 745 · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXtjgG7malE0R-qQtFIG57sYQIP8obyfINFjDOwWFQH31y4B4tZ7Ll7A7lXyjMlWXr9yjiJhO8ACGF47ER-E64S9R953jIoKwqmLn_Nif6fSDGaMVWOgrVfhH4zSOVHyf7gG1lCgRrCDHBFrSTqfTq96dSqWgaWYGNQanHV3epS40sfOJulGcByakmQIrutZ8vu3EEW4uA6qZRf_rpi3kiffNptej_Zac0PuBOqtKo-BonF15RyI3LGQJpdm-lgwg2WqFziLLldqVrkiz6G7GIt0q30weVTt5UffNs7Uwkah3k9qdCBlMiGjB5ycKGKDAUVTrURs8zd_hUJMVNCuOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B5s3zpicJYtB-gmCgJfAVk3bBIJHWVhmClELWTY55gpjtOsu6Tw3mk09mqMujw7J0hv_xK1wfoouSEgC7Fn5S2wdpvyJNfc9LfGtJOh-mgc8nC3uYQP4R3z-kBL5qOQUPgW0ywInSgdmrS60m6MAj0ELlJK6u0qN1oqV8dTZEF6BYPFE_KBgHb21VAQ4J3xmInYCrMFOEtmi5Rv8LaT-bjE7tMZqwsml84icfLt5GVS3T8bMEB-ZzsNKHMAd-5enue4AYfKdRpM8pDEwwhfBUIAVHrNy0gMBof9MrUeUVYoOkuy_OC5_05hoprW4A0EHyI2uotNiiw6gp_sd4d_GIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vf_XeoeegBTZ8-6y_w4qCJiPapjZHM1qMcKFLCg9skuZ38iY2l63E5hPMIbsysn39FnDp6I7CLSqqM4VGN9opl1Hi128yTDPRter4gaPIlJMzMKewmFN2ex5aZYBfGRa5CuDH0qiHaYdXy9lWtf1cz1DJw49FoAV0jxrkrGDH9517WNhtpIBW2r3tGdqX-anEEaSVZZOJFYgwI6UA3JBxRrcgRRO9_aQrDJgE0Ob6QC4B4ynAbfk9QPSv-Fvr-6rOmY07X0LhBoMS_SZ7f3e2dt1zX00TF_I4ADlxh_ydbSjOSbUDp6BQQkYYSJ2UnXMdLrArV5mHhii6OwUBxQ-bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z8YmZjncSDYzLmGGaRbZu4zY-1UCNrJ7frEpcdG0Z6JaZS6HQylbKJJ9tVrUYl_Ssp16bQq_CWfgMtA2v1DbYpsemLj6i6XaQtNf6p2mErUbFr4EhznObibvB9tEAKPXw8EXpx3kkQLAvKBAlXcba3y4OywGIuPD5Agn7EHPtCT-FHgSd5x3y1dHNzb5VNlkCFrA53DLdT6Khxq10kiLHyPceL_qCRG3iI7Ai8HXwRxxfsoq4U7AMWyx3yVACEAG9LOeUeegHE-fPPdq9fVsgFrJzHDT4SvbDckQNZEZH79tmc2Cykq08bWQAJkDtb-GV-brORjbo5xsvgOz7B-2Mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_1u1G8RMVN8UmsP5H8cXuaqcMTlU3GQrn8XycS1vE_2ZK_fJOfDHfd7mjKvv1vhgtzc9JYdpEN6yRl2AlhDio9pjmZcbzSvMfmJXjqjR6yheBUwdjJdKuJRhXRyZ6R8PlAOOoxH5clxhx6FRjzPfjUtFEVDhW9aJmMnRkmhQ1Z9nZSQFGOF8XXnCjWWKzrnqCvOLN036dmM0u3hDDuSOTsgHLbf7M5q4madtMJIijD2RuZobMKZ7j5206UMYF6n-2XXbt6M5GP0zhhtteREpwl0Ozht4WH5nIIUM6Z1zIJqPv-Dxfia-DkfjWr_HDFhrrV2hPniUJzocS0n3sF7vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdTq9aG87zCHOv6oodm2D4jbYNFXAmsqylNQZnZ0scPHKn_qeESo4JRQzd_-qsP9e3dCRysdxegkh-FSKi8ffmtYdJr3KuOFEve5D9iqWQHWrSTk-3LNgBlTFEslRyz9URcPVkJgqleiRu-xwq7yBa5S5xgmYz6rIL0pDPGb6jqsoSE75BC3LVzwKUHzgijLVKgvlacA-TGlRwXs7pL2S5cKIiXprXNb5Rztv7ujRXYb_SvjB1xgRdL-VH-P9j347unXzbz-DRqM0xuBw0-meBnC8XDell0hKzA5Zpg__oKsUugZF1zvZre_EMOb8UnD2DUsLlz8E3xea-QhHA2fhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbH8zygGdNqDHx57me62rZBtLmewjKie7nozy5JkX9U4Vn3EClzTK7sJIkh8XK4Y2mtcfmCN4TMzwwoxt2xsiLWUjFeYpmm0e2waeSFHSMdnbc4mL2r338dLtbNhlHFSKlBb6Tb4SsZIQPkWUnPB44QheWVsnDChC43MS8AkoVc_6aHdpYtHZXbP_9sFfUKXHwzGjydYPVJCYacH1jotzAV1hflDr4Z6mKLY0wp0625kW4tlFp4ifK1mdMcrO2vAh7Rz0_BV8R4dG5QYjaBtEv8M4apHjrFNXvr7t8aLf8VPMJmNagLHnW6_7F01v5Af-Ha3QYA0Js1Jhga1stw4iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiNzfhOzoawI8pKVV9MrdP-WaLy3bEkwTWg-hcz_Z3FtSY4U0pEzQi3w0W4cZ2CRD_0RlXUAnPbL0sX0z2_k11YeBvblWa93m8-mK4VJ5kmGY3cgwS89h0umQJBvkogWrJCADzGjhzS7QlT06bpCSmI3WNwTMIi4mFBMAeGATMKNlxZgPOAiXBEdQcdYCOI4MJPH1-5Q-Gu5gD33fdcvM-KOv6dzw8Q0uBT99Ix5EPrDYKdBKPkrU3v5ymnSPdayCewCEUQ2Fpur1DGJlZS_LmLGVSUXFQ-v01QTmnkPhjSn0KpMC-_SmvV-3v_rrr2Q93iZoXXdjpXQ96eJmDA7hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gMvHhnDThrgV-y19Gk7URttFQvgYlBp_GkshWhkWv5rE38x9V7-Tx4Fv7axKhLJPKJpDIZvTSRGi7lNWiIIDMsblRL4-_uuZL46KobeMBi71XR8Pp6kmWauODFtO47Sj5HUCg4DPr5hqDAJIEsiEnL57n2X5GmNlfsQSyhy-XMdc7KshpMu67rcEWQdcR-DqecQCJefv2yHYVtj4o6GWidcpwksTCRf09_-X_p7kZR4z4KV3xtoAuX7K8BXS2u1efeyLkIkaEXBQnYvFIzpjYKFyQY370_tAPC5zzT2g5Dq0l2DEAbQVd4gZrJ2XdanrrJsBWcn4FsEg9j7Wa9YHyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pb7OTlPywv5oyCBe9PviVmQhXCpI9GLbekA4BiPmijicnJmSff2PiBZNVWieYNGx-iei9apb36iWWFpST4JeamaaSqyDpZD84j3WM8fMFA7OnsMAkfaSVIfYjugT9M8KCurjoNsNzcS7Sx2Gi4rFvxNbruOJbz0UxGl1ZgnDnbGiu4vZBaWFxAafy6-lt0_Net-Jt89g0HpNVBlNGNSlYnxFlq96iCcBiwqiX0hcNZlceyAEnTymlB-pejNjemnf-1arwE1fWW-VUyMSP0H9x-usfvtBWR0u774KrrdJ2prxP1hil9f6RAcAIYJJ9AHyzdoYZRhiDUAiCLKXLhwUFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P75E3BanIeFHcqP6_Lg3Q32X-UKsGNVw2V1R5fyUpxSMXb0grtp7oEWpGVozuC_6WntBOVkfykOAy0fCKoN9pPvRG5CTBbaTAwNcRKhH3ltkdrMFPye9ePu3_U0fSbJKurowhoBjo9O8QhTmAWG-8hGJKVc5ZkGtHcfIKc7DRBCGW2Rul4egw2qTWX726IewuzKfbY4kaKt5n-M10YgaXpde3eAyGg72awyGhkHcmEmCWFmIleLOb-RIzYvI8O22YDfwESTeRaGRzYLLm0QF6N_-_jw1-bQEddTg0kwf4ggR41-Wb0dOLmaB5oA2suS1CiqHv4TU3Hf70jowjrhmVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT5Xp5AVV28C27Jxd1Ypq6J-hdU8pmvMCQvBz-ULkBgwN9IOkhmkIoYN3PN3shRqCYWcUaz7Dp5DeHwum8wpapVpm1Lnv6vaQDRjSrc_Jzcq5aNYSLvW1LzcgsSN8uAzpDqw1mWB4eX832cEvZ_ZmEuzrs2e_HWNT91s8ozcdwz7kyDT3XeQzInMf5Wl0KHP10BhUThKeW7rjQS2Llvx-yG6DW9TOeMsDeLoe0FENpGEP5twLRYzJ938zaaLEphOU7jKmf_Uj9IsOZ7FSBnn0WZdXZ1vvZMEgR36nvh8haf8vk46IltMNiKrbh7zJaVy-kqlxXtIBnmtip2IzFCiwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwJiUKIIUj0IY7NN7wrZvmF6cNufRZny6F_4-2I0RKf350AWV1w_DaiYOUu6r8nL_fc5jMkoQOCNrkFr-iVvCFn6oSklfePFvD25UZtJVCoxsJRgdWZFcZV078qN3karZA9GNnwkqv1Ya7oBzoF5T8pxvxlwhpqHWsZPJiQ0JVZsf853DaP818PT3FXZo-PA-fsaoKKkKGLY73j0Y0U1mpv5EdTUt1Qg8jKHZnMUrVh-dhiyjurMfUVQdqyb6LhexL5ogJsq6u9T_bhc3InC_Qx297zC-C8gR4oMIwGtWsYgiFxHuB-o7p4-JVi0IgNIGznnHliPAx8igVbswcVUAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LAwLZvaPIK63hCuTHbwcswebP_w7BDSla9gcr2F67QDRGY2_IAZ0qGatycRONWaG2VZ8_aeozHRpUiO0QDjse9e_GJbLOsiiMe1Tj3DRbu1v1faRMeOnyL1DUja2YfWqnZbp9ttwoOn8hGU2oNAe1ko4lQqP3F9juftmBi1uKXlxknnkY1K6gN-Oqfa5CHB89KUNxJpX8wySe0G2QQIps4f7Zm-K54KEgkyk2irvrTawjpxkSt0jlKG-RcTAJmbbZyl6gKzhKHBffUozzc1zicYUkh8LW1xykfkax7ZHcc8EJQNnMaSHMoZJsY5tCWTsOLbC5z225ceRjSdYgmDFQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AXlDOdj4cY3-TTffCeB-ets8K9Eaqi4_8p8Pbp9PGAKPFdxZXoSoGl-4NU8GtOy4DtUqprGrBZPfuX4BKsJlUcCe9E1RWSDFze2KgykfkT3Y10bNiYId4SPjQrgFGM9yywEYisn1pNNSBK5jTDIMoZTcdrebksBHeAI94DXF-oKRK4EW7sBsnE4paEDDCEHnn7JWfhFGFLavdGsk0H8rEAyvR5kbv_PHyaxwpHPxlr-1zDX9kX_QXKDLRaVxNvMRMg00kwk7xpAjmB0w1PshFy7Hv2P1yKDSJ5Qbz9JvPttTFBoggsmKFpQ7PILRvt5Awyuej_Se8hcpOpUJkr3xng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGXW0ziZSm8sUT7sRPb__agHqFReQAQl6_cuk4qKWIG9iv5lM3KjtC8DV_2tLSj-Avhggy2WXLAsWK2a7bfmDzq4Vx5Uc8NhV72jPHx29kggGzrwy8f_hime8qM367q-fQ4obxebt-L8feEw8UBtTBV7PLMPxr6jG2IcAp7xigAX_AQIFDIv0OfTpbt70M-fgS-2jkPiaM82T1a2cfpxBkES5PyUPwo_OwLTntHNUVrVPAppf6UjmO2flenz8IAb-EklEDQPLTAoyfo9nDVE7EaZvHQhlMDEO29xgM6asrGUh3-HwpJM_Pew8BCUeAVEaXNdXwJRXDH92Ma5WBPTbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_Yg8GMz0GN3IrZtRr4Xgx7je_BYxqvP1D0GJxkdBeoSvmZdmYV4mHsRx8fMb1Z1RyVUelCfFMBCoIebu9jEOUnGCx7i23Ny4JnIaUnPidIY2r9Vg2KrqG4ACCZzv5WIYLzAU6loNKHUgLacxN_9Z0nEgiK7LqrsDWy6J111Sbvj5LfU--h6RhnLH8YI4aYwADKAXz3eKm9DFkR1Awys4TnwRNbYatRwMPd4IGamaal-CAg7O62zn0w-EgTDZanrWQw1kpLfBXI227OIFwHc_zWOQrggr-kfOjARYBqhjWp55bXZ3-LAOrr-unzRJctSnRHl2cl3VjDQUlibKgN_Gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppU1DnVER8Y_jOTRR2GyVz0ZEujcm_kDVOcJNVcHlG_KSmToLAglhlJkf8Y6lCkj1XBxZQqwJzyRqgZmvqzFVwXuPV4Rimt_dF-23t1lwtgLMm6qsClkSOyGkaLXbDn3LBAYMnp7Dwknvdaq8cu25prRzW1N-3-OivtsIzoNwcEyMEA04b7gQUB7M_uRMnGNwMSzLhp4hX2d_vQ7yh0j1Z63P530IZ2vMgrEfpN_xR6h2lilQM1HrpyxmdaTRop-weZJoFPIAiAbmiS5Xu_oVEVoatwCfZE-x3KCq1UFwE5llhQpmkL8TRpIoBtiwYikm5emAGKuUMPlFoBlLLhIOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So4ZU0uPbsulaI9KAYNlH7R1QlmvZZJndJ3tWMib3Cj7ZEUuhWalHIQqZBBuvIURO8b9w_rkEsQQ_QrRN85CtWpxFbIUBxSW8bK_mvV3QbCqvmxOsHZD7DSg8udnGZ8Tq-ihxeJxeArTEuLw5x5WvgS90latEAT3RnXCKOoWAuTwQcua3nQwemmsIh4FV0ZvnlUTH4Kx6RvOnlBvu3JXpBk74_nBUMWmcCdL7j25B-4l1jIJ1mtMJ7CT5iRaNU2fR5TKFocrlraL-FmC3LOK_gNGkcKqginVJJTF_hD07bnkWatTbAnywy4_2NwEZAe0vIvXkqR8uX8I7G6kByjrRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReQ3UlsyC51q2faeq6PL5ScQ7se-ukgDhBpPA9bGgC9Cv6ouiYWDyyJHnNRLS1II6HyVv8aDirM-zNbx8qBR2PIhEA61crO-rmfi2qaDnpwbR1sUCE7z81cx8iIEaxbHquFpTJt1XYeAakwWYXKtDEKFcwpZlunnubw8qOqtxRfK51iPqvk8SfU1wJSY3kVzUKugAqVDAuDczS1us7mnFujysx6oBduhunkYLtvGRfeuERx9iI4DJKH7o4rGWNltKshiQxhYo5ntEu01eJUUpHnUF4LM0qsPK__Gby7uM778RGJBZgwXQ3fs7-pKk-zbdLFrqtQ5xKJ1u_YFPNfAvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRA0kGpGW8YkNxcNLZHfOD-DGx3o9FNVOyct-UWXZO7K-J4PjKM8b4vqpZCQlOPGO4ZSiuvlry248aLCvjbZrxiMNZ7td09ZI1Ijyq9nIRrg8_Bt55dyxUDe3a8ywvyIOskwgkRKeBoO7fecWVoJpRNbxeeqyafpLsmWi8jx0QaaMs0muC0pkypipuDAOyiK1cZXxs4od9FgelDT3wbYaem4jbxnTFggBVPx39MEAaKWZkHGPtathGtr-bfRsE146n9ZRLrCX9-AXXENfyCckwdfONLVxdNMJqD2rgVtYteqwf4oZi16MMTohx0T-P0dCS5G2AiRNUb_8g_nEKuesA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7943" target="_blank">📅 14:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7942">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiO9SAxVfsQUYhTz0tGmwHHAM5JDa2oCwwvEVC0wt5nHq6Usot7e0nC4cQAOIfLIIzwewUjucSOkzBgUSnk_uA9uGIBFNLd15rq1zuCQmpVrE7RgWpS7f4Dwk0EBwoP1H6J83cZIrAaR8DzTX3tkWAb7B0I0SzFtdQoeRwXSCpf8SYme9IV2R45JnbLk0xzyj1yMEJ6HugEoajjSiJ1QpMxRAFWyBN7U-NA66FWFJg_9m4wfhEGaQANtBZ5SJw6Pt4emllOCGTOtsOsh2hSDKCQGWJQWPjkbZ4TC4Co5dIg6EfprSFtxn9I-xypZ60r-8FKN47fh_TUyOJzk4vd4pA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SS266Md8HnsktS7jjlyvUoSet7y6ceplU3Sb9EYh59CkfbrHsx7AVKzy9vNlV6_xv1kVWj1yQAOs5QG0Odk-34oP_1QkFh1INfHJe5HmfqtC3V0U_F5eorgRKlLopIzNXcl9BCnRD8zPi6WeryCuqyQIFgHuNdZJtMMukJw0-9NKienjJPaodRoX0sS6z597z1BkAC9QW7ces7kiYJMJ6j75hL8lHPRr358fdpNYA8O-AdsJvjNgBDD75LzRy5gY7hNBnXmulZ33VoFkqX7ApvNWuXt4yzlGLiCXMyV_nlnRyv7c8rrGX6k2ElmAQcXY1Tp_lIedpzc6ubkOkb4IEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ne1pqtmldRLChV32Xmb5TrJ3XkgI4LU8-I4Fpl-Kz0FJtG-l-oI35mAvDRFbgSqAh4pyx4LXw6sEX5itf73Bd3W7xnXEbeFqR7JWDCmJ-r0fRd9tcy9VgoDu6hxB_iPbWs-l51eMui7kyGL45UgS2fk7Xuucwp9tyPRpf7PX7bzxkEOzTJsAJZspWxuXJql6W9VW56eBb0hw6GeqYXS5m21Gm-W2Gu8s8BG2hPv1IslHL5IQSEyMjdFpy0I38Y8O3ZRB5AvCJdZ379jYzJuMdl-OO5Wz8ErWq0rpUSmdK1Qt-KtEUIRujQc0_WjhFRtSv5kHjHTETf3HRGts6GezdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IrLrtEg5tU3lTB48QLOYSiArqtSjP477-8fEKfUxDwn7jI1a3Rz9Pq85eSZXtWWvXLz0VcfcdcB-z_9J8zrzg2DBX2ej-9oxI7ofLVmsgDzlTQsL_g-w46AoodN5W-C9yts42JVZgXkmyS7veJkS9A8hgwF6vQ5dnZ2y70CeCeIf0cEZvpTiik5GaRbgVLlLTU-AB-DwulsHoA4Y4j8_YDZ08m_3YXZOsrhRDASGJ5EcLSdqhNokXOxPTwpiFUCJy4ZVFjGaJ5ZxnrkAHXNPOIZSRyBVmISUuRae9BHGxNGwk_M3_CdNkKcwwe3_xDic0rbjacewmfY4cOD5pjLrig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CDJZ8omrttVxjDpeEyPey99sBCJEdau9JqrGkjCFZQi3asV__E7Ls9r08wvVoWs3HH_wKR0oawn0zPqcokztueiO-QwdiIAGDUVEmL6YBy4cmgeT0hSiaxz4k4TLUyCuZXd3QyfQu7okPUdZ6Yyr0XtZLSBHQFbD_SukRliqoAayfY9zSleenmGOIKkjCC-HU5H32h87IwJHZi5sJHtBK_N_uPnS6MT5YJ0COtM_1JND5GO4OXN385Z3am7vG49VLuSctUEL1C_0WTd64v94v1SEYnZhxco5gLZ0oxVQJ_AbcC51S3KHM8nYy1kAY5xsrOmn_u-leQTDqje5-e4F2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVU8vL6USIt67KStBbcZ4RKK4sOC89bs2mXec8mhR7gC5O7dgx9ALEsGWQbd8Qs6jwTPzICI7fCkFyty0gYAnNFg_q1hCnsIn9vCQcNPFdY7HVdwwlAkZPccghTLoy8u-djPPtBkNTeS2jBX6Or3TujB2EP_PozLqUXbOhv7aHFLy-2cTmNREk3KK1jiYcpzVxOQ7GDF1lyeEHs30Klh3s5sV0WqdlvR4VY2oLl3dNVpOYFGWmYurJoA_pWlCIDbu9A7BzoICEFts6_h1VnRNCVhB--YUeH6uMSdetJMpWSj-14SU7SFy7KGNhzEpv8CAWZPR2GSy02UJr54C7B9mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nj0IC5NCAA9rxXqUU2kTmkIe600tboh7sfq3swqegKxS4ztP5ocLjj6v8z-bdQ4PJCacf64Zrua5Y9u6QRo886FUDqeFPAB1Z0srq6hVOhfAQAIERQYYkxg54TQ-hd-0LRS6Ej0VpGrbIqO_D3wq0pB9KZJLn1ywFP7xdT0jWFGTWkkeEELkKqK5A4jD-CtopmcKvec3lR-hCSZV6Djjgx2MevlYfr4ETqFdbI0wkFxoKlMVywBg5SViKBDcBkXKwMxfU1FpYPs3_mmKWo1NKd1tPaCxsfi7u1R_e5Xh5hY7xc5TJAiaxtVP-66HEUcRsbUu55jgpqQMZr1dRdbaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qcoonJhvRIqXNOxf6xokeGaV8p1lsWXf5eh2rt-mXK_8ikn9MFNmM1yYaRsrJ5WLx-x59SEgl76u1reMpZm4ZFPPkSO7PwtfYI7VUXSswfyoFdID79p2orkmhNXek0W74r02y0HtwrP9LMFd25L3dUxBF4bueIpXCstwxVazaaj1ZomYwfaPvBdj6JCXEsJmy4QYWmByQd_NzLobRXdDjD-X4LvFbNudl0cfSWyTyx1aXAmJELaSd1Fn3yyqj7GFLq1-HSlhE03Ya7Z-NOZnEGcUOh-4ERt8g33ze-RuoTfRWEVZl6n_Inl5fT4GX5APF4V1H8kheOQUiP2ZiUfjKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcTagZ-ylI8jnCAyRnvcQBFCU4OLnwl6fwjGXEmHBflz1BZW_eO1DrW1-7yojirlvXxr0Gkc4MMNzeOcpb0GBsJA_EE64x9zt_9eee4SZkMYmIky5m62xk_Gl4dMG9lzgAvwNZ02E4Mah9LrliFD5w02NBBzMlvLWadX206Plz2yWyBkiqFzWdTqD2OCi-cU3VnFFwszLjp4_11Gv-ZGy80gfuruyT0hO8bS8QSU_o_vIttd87KbEDN1j9RPFdW_p5grSuHS2pEkEALJPqNSZkNWrI85rIP6zH_QVzM_cdhVPrUOQF7Rl9DWytR5Fx-VxkxQlTkfvdSU2xIvnl8mGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYkMhqR8ljMY_dj2LNicw6jFXPYjl3ko-YXHoID8enonmfJa2Sv8akq4xWyBrfQMRD05-Ruwg-vOwrfoRwkgyhkXzrlZtLNfLNWwqBhZM6sjMa-AgvI77hPFVd7-F07iU4H-XUdw9a3UvOfEo7zv26edHby-Sb9YxdC5QKGXOv3hi3QrOLulQtGEKbJcv8dJFY7-97JC-2E7KT7KkUmiEdEjESB-gGyXzv4VyKozC0F3ELi08p-8eVJnTR1oNwkWt8AfEYQSJ7QXFTisfkATO6lk8sKbUQavhyq7KCTEFzhygxrldEsLjmZrJoeY7ohmj6D1_ReN52LpCtJm0FYTxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mwK6dXFG40kyfd6sAMNMisE_OVArNSF7HvuHF9W5YKEThj0P4DSUXdTU1VP4yWNXzVXAzUOxfVf7xIPsVCBL7vARiK0NFH_AAs8Izw1vO1Jk_z1GfMpc_P7v_cRo8RjQLoPMT0MxRq5FGNwo5KyAyOB0rrRPHVhAdcwhK_ON0yXzIiHdaLMeSCM2LwlkOkoctb_mUT2nETFFgxpno1_PzeaAeEDZ6rWl5TqK45mBgNVh6N0axQ2X_s8U9sIOP_s6RhZ1ljbOjMNqxZo_5Ql0t27VXgUWEdNboBMdKfN3Z3t9lMnsyOiK3ULK2xU6gEBs3Hi0GKXItNDegfpoCPquJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I04KnfBg_07CyZbw22hV_PS3FQ4T-CG77GDcWm1riA3VpOtxkTE2DkCq6835NWbqXZCJmDxz7PrkmFXbBb24xmv5f_Sog0i2J6djfmZBMySqy1W67tnyVfSgib1FlfoMPYxxDxQqhBe_cC1tMGCgIpCKv0OhTxwT4zSEJOhoYmuChf--TyPsWqnR4dXR2zWTW4GqArz-wgNLE-YEcnyXHaJnfRV2leo78FfggMSF20qyCAS-sqk9BLYGCg-biLvz3l7a3R7g9c8gxH60t-Rcg8VVQOlN4Jb7r8i2n95l6hM29ezmPCDiGA7AhPsgZCLr8YNFDrBSM_kXTsqNRtF3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OZ3N2YCseOGAEWKcXgYjQ61-5-hJnbOYH0Ug6-W4YyR0odhtd92c1bcTr9clME5IAVRxM7CEw7noIbE334cha5hm55GVQ-GTXArZhU4-TFHikOLH4D0Qa9UFZ2u15CvcA7-4oGItS88fRTcLPWDXUsbAj59018DSWDwo-q1-7CrsbxfLIViAEvCba7A994Cu4aqiFa_G9qnraDFxIpIsida6xd7G9GBgC44n_0lEv7NxifCDYb9fZcwMFNIeXXFgkl1eV7T2J_Kt5Je4LwD4nl4pRGDtslxf_cHAxS5VfeGTecqQTD5zmzCNPT_aLSdK4QY-v2OhKnsoiInKiVoWXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/frRjcpWp2bxAnn_DueEA0Sayy6BLuGLAenXl94pYtANnAquTbsg2QNZcVXXNiHihVCW9ZJJxWuGKkBQBnW_luIg6wG39PzGqlUnRewTWhmGB3Kq7qmdbtf5uxpe8zKNGvogk3-HoLcsWUE35aKBh13jM64CAMhh-SJNx7_UR0ytXKZbtxJbkeF83u0011Vs7moslMOo4cryBeACSa4jdWci-gGLYWEKk4LutTb9ZG1ARnwqqBW-ZqamfsFCwmSunTkkqJ1-WE42Obg-sY4rL2WTn06kLB_nFJB6SX0diHb8wp9S7tNRKbtInToka-60_aPGebJ1rrJS9Zt6wkocKEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vz3rN-agheLS11RRVHvDein6GEzVuNcJYtVVuiKIzuknB-HWVtJyJ7d_gthlsxr0yx0op53edlW3jxgvKyXAu0svb69QUTz4himPPgrLz3bMafR8R5AmICcaD_sm3ryT1xFAxlHBukUR_FEbu6HUuO6xQMc9unvCv_ux9iKie2IwfN5eNGTkgB3_I_mKEpp2vxxQ2DJrqzraoADxtJRDs6-ZrjoMC0dYlyZTmk1_YyzBU0Viic2JVDI6OlE8DWVg6JU-EXHu0xWzD_lHrp9lpfvlNKwaTzV8PqDhWiXbQfoDILvj3dSm2B9YOfgamOO2YC73HL0j8XLj5f9t-G4nsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnC_3uFx5s-3mR7oYE5AUyL1q30hPvq0kYEqCxkhp662F7ZGTAXoM6tEaJSzKrs_FMCms2shgauy7tTKkjza5Y1jh9_ICmsx9Pq2Ri5jA85Jqg0J_k5HEXo5fCRQSAwbJ_5ksrWQwzN_H_n_vg_WVxlDIViPqrzcwEmNWg7w6i7cQttk8Ay8xA6ocXf5sQBN5blRv1psjVJyJV0nQmlHCds2IF1rUQ-OMTWDv4G3uFmMfRlGpxwJRAm0iMLmqrnA1XVvdxv5_sdl6a2EekvaDbXcwmdKZrSrUf0I28GeE6_tc_lrcSOE-OGVTHo1xlPsHEEE2SwhAXvXRJ-FMwS0HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOUIG8s_8ZKZQzWbXOv47EoEQbC2_iqNCEhrs0oK_Wxgqz32cAQVvG7JNrMONnIpcOZ3TP_IpOunPUNiiSRknH49eejMWFxm0Wa6H6b1gMV4Jpax4P5lKVmKICwI07waw8lGgPv_xKJf0dEKPtAWbvBln1A0UmVQZqj_4KDDvBbKSQrYPni037JQX6r5wfEW0ZI-D_-LlKhHLp9SCY2w_wGK3dTedJzHXEkxzUlbotmZ6obZp1KWGsSbssW2zhSuh6c6V4BC0tMWuPGGoRi_ZSqjmfHW8Umi4UBsi4qVLpRljt16lVJGlMpw1R_NQyaoJCDx-ZOGyZ7nLUEm-FhYwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snnA9-VytmDDdbq7wWAZval4Ci54e_tYXcBjm5cMFvxsRfbRFC7a0smG97ZF_qYTYom0zK77Gder9ud8_j3QwVslI_Cof4mA6lBPGFwjynBddQYEYGz7yzKB5HQSpOyQtan64pV-1xl3Pm6tPLK00VPUQpOdJqnNOxxrxeBxGIYyw943YS4oAxnH-tH9OzvucZfZZs20A233DX9KTF_Nlt5RcT5gnhDBqB5y-CwajRnYhr2H9wdWe2LypVBjvaFkfwLx6WgBiZ945_ERSy4EhYr8wedMUxCiHwvjvFkAuehYjwMztlPVcKZItcwzOpx2iRyTelTWQVNr0Agax7uXwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6NW97jGwSwoszRBwL3o8GicCuKOU5gjWegFLT90o7KGLZIWfiRy6kqJDAeHHaN8PdpKYlXFPY4P3MicmlKlIwziijD4KZaQnaXjflTJqwERBoHnOc48MkL9yDYDwSh0VPMgkFHZov78VTYBDlNjJum6OGZ3Ly9-p_YCyZC0mwOxHlLZxBOJAPVGL0QxGlv3MfqTdnsQ67SSC_6fCD7tCezPGErrdzpTfGnxMEbDrUhWdmKztHzUsxmcmEO_v3Awgopeubr3A9f4HEwJee0kGO1WvLTTC6wDqvhOlVm1zH32Kbq0bAYNhsY5JwYSPlM_2w-mWU59Q_Q0AgmUldIAfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vY6YTTzbTXaDF6abcGGYFLKZ3-do4Ldis5dgNk34qfJchw4FOlcaa-xXBHiGwFD_vlhOh2yR4ECc6KxHC6mJufvTKgrAco9yZhG-gxXn0bX0osYstJu6f-c1tqei08Yp9bDa4MTM7v64LtXWbQ5K7uly0LN_mlmAtM9-XR0afzLNOhIwSznmGVym9aERPqMLm7njmY1R8UY4_eDoJ6gTw9lRgM-sYIYg2t0pLhhRal-wTea9vEp5MS4gWv-PRrv_buw9IHp0lrvjuwMzuVMwsM5QeZYQxHIDR73dJf8ThRVownFdJRPHy2y6nhSO4roiFhmPXqk41MZxG-57bV-AFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qFq7MJi94gwk8qKNCklMR8z93HZ6c_Bsb4yai6pLxvYc-NqPOaa2Rj1Qernuswo4BbVDrM1vNeQcI7kKL2Q92fRg4ZOwvCQ-qrO60fJcWkEyPRR0tuOXDmeU9hodajmrGfJKplyq9jpA5YSDQCB9iI5-GH6X0THMUJe7gtqpgu3X4idIRR5qkOvt3d63HjL6izF9NO9qKya_VC7Umz4RwiOfQ_iivPo_J7K5CQCc3R9EPZa1p5MWUUiYOTEHB2aqdXIzyCpShZsdqM50YTvATI46BEFwy2Cih7HfkgWSlQef_lYVx_84wFMaRduoKZPz50nCH4IDUzaZQEDVm7tBxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DBk3-DxDlg2E4_cYA9-hqf8kI-fwU6Iefo77vjY2XzTb8MYjp7JZq7D5IZ-asT0qk7yxK5Q0HufwTYNP-ASIRApdjYPR0-vk_6XihXzQZFhy6oDnEhQ2ZVyjv1xZEuxId4uaC4w0ljMKoZ5sEkYeKMOqQetwK875mPnZ2WbIxFkHBoXNW7m2yV_npSvQ_-b6_RfI0WekGDaF7fRVIoWkUw6paUCIwGXrzGmNjjGhLHSLUozY4D_sGvoK3RvmO6UXROxuN4x8CrYyMf14RtwpJ7eBWhcyOsnCB3Fv48S-N-OwpyVUi8sLG8WiXHz6bG_KtLK6xqcsg7bImEaDDAeL0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lBHwCkW60_dY1qvUo1tGr1Wx3fGvnw6bK_1fBqzh1AJtC1WvlAJAyADkJlIXXVMU1EhLSJIsT9FrwjQ13sfk5CIqN9S5CdqosxDog7HmgooGIx0Cd508GUNw5KCmbZRFckbVXZnHxU6Oz6zvtzLxAvsUhUqBOM2iIoGKuDB6ZlRb7hPZ4N0rYNU7YSQ_cSGHHKClZBLF0k_IoFNFqaIJpLJc5tGgeu4Uu0_bvoRhREoL5wiJ20-XA-SyJE3kDIiUjSWbjeclqTjnl0__fSxntGZHnRFGlgLgm8qTY1_0sOWdFt_-uidGnbebko0-8kgbSpb7kb8Cq-Jiyb8wrWBzOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrDzQ9Brz-ocq3MBk6uoZd2iXCiSZU6_JbJg3nVzHPN7mvOrsG2Pr_M_UCKKX0DQmviSsLH_vEtoy-RFmRGVM3jUdUdzGwaRs2xDyKSnjSmZCDpTq7G1S6irqSW3VmpRLW1gaILJUA7rAtBdDHlxWBK3o3y5mPvT_1aqFEtrMsHxwmGVUh_68ZiuvI2t7mgxlyemzzfVoNnQnghBrXYtkYzlb4SAnEjz3lLQEDKhLzHZdwjoX97MFIFkEjWZJ96jFaFVyIvUg_bZKS-6bB_PT-a3mTW8QR4-s4L8mbFo0nULf09qfS2910tOl5i6TrRyHw-_UvgJVPfTXGyCaIYLZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAMtdAxDdBLz0q4tl1Q_swxEf2Dpu5bZuwf_rWxno4r9dF3lLYwDGynFJC90vN8IMNBCYVnLlYociaZiE9gZ-sp2iwWPgQM6sVwPWaEyY8z-QOv-kLml5I6TL-J6e-2TZUG-D_NQbyUFTu_UGtuSS8nXn4boctS2NfzF1eW7UVyqJv8b88eAOrtUypSAEqBTMPu0QKCj2ZHWUFo8fumpSlJGxaIo9-JHpPsv9iPqHa5AVA31TbKba9ZOS8JcpUVxZko86KHAzr0SsVjgr9wKIjA-Hdu7OcbIgTOJl9ge8r6acTivD7oNr9GURrNrEGsHzY0RNiwMajayqo6orgcv7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWfZlDGnMAiEjSoDU-mIsXUQdTCekk-FgATrE_ZeedTMIYKb19fcLsj2T05Lh3qHqZflLogEAFiVOE8Si2DxX35OJfJhNITslIigEzZz1JqjCh76FtzAzR4Eb3VLoGhVwyUzVZ_rQ4pkPXKKvFmhUconohTI53JViQH5k8kwXQfrlF0jPoC2vHTIF6uWtzWj-d3BMj_ms6ONbRONmA8NgwrOo1ebtDWWQqjIdBAOEJSgI_qCzsw3dZwPVR_YqG5BvRSIrwWiMnVmICwlbOHg5MuoaouM-ZNlyu-KnlyP2RawalPmoLQH0GzVBbwpWV3y4gTTyXNsb3VgjEL997vvVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLNv0eocVvysnVUEzJE5LuHQ439lSVm7jA_dIN_GylW9K4CgmTrgizhHO_GYVrSXw43mCNWK-CLltmijyn6c-U3gZwvMQfTLeK1aT4zG44EnBAE7TwCvv7VnSV9re-thVnVJsyC0plsNsw-jUqbKycCHOimH0U952ESU0KYXNkYjLU_tYr-cAGeCXLjIBlOPPwc3t94HeDyLNS4nkuzf3ip37AJWjaJ4zoJ4yAysHN5Hgd6RZarlrFBZ9jI5QZDnTlGUlqplMxX6Ikx8rRJGXah8H6Kj68PtcXFKhnEKfCJiTaOYa4WN-_iZAgi4VOIAqyUPjYawbv2zBkmYv-RqZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKJBX8nQCHDS3gU6iaFrQx723yRaXxH4b2btq9D5TsZhd3jMTRTYtzY-MFwkghEXQIZWzYB1x_L8LptGZ8wbPRT0g1XH7UFrpf6XGVSJPah42GJY7FDd2BKCBbrsUFQyIDNZdP65JhFDZSowgBwVWRlSBIDUgfLJn10sG-SipE0IeC3p8UdEGI3la7lwlv8iTrjWM9sQ7oCs613yoYPS5jhtEyS3PV-MDazMAsYteELdSYFmH6ryGAc4g0RIo_k_lni2VosHoScuGTp_75OVFf-6Kg8s9UDMASAGqXLs2vTdp3_5yfqBcEHpxx6tlm_T6k0MkJeZSHND5AfguDG3qA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAzsedZZa7PP9vNcjwNoUdtndSPpums_Y7NcFL26g0uNiVCHkO8Bd9_pDgL2IgQb860VeTo3RxpBIxl-D9OSK1GUPrxOmAPioawk16BUHl2h6J8ADFwdGFkQVRecqyipUIhXLLFEJJNAr_Lkp7O4yD3nwpQiDk0mj3grSiRrB-ZPiAHiWmabSKFjKODbIrR9KWiwunLkOkqUCSyk__no3ymJd_9OThcriyfnxGVTkgMIUQoR2KWSJzrMRieGJALVbeJwL1pvNpkGHryQ9q2tlXHxl0HtO04F6JOPAROJAnw3x7fxLvxb3oOfxg3BL7y3EV-NvMU9DNJ1pXX1MhRvxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRAg_g5DoOM1dDC4_zNcYGtexDrXLT2Sb6Bys0Tbfh0ZNHydb7a9slxQi-h25tRRFu3HE7OqIL85BpqNf3eCVLUJuIRQS4Hp9uKy4Z3QcnuQN795zKopF03TOUVnp_HBtDBpJRYdORNxGSbaFFZrj4AWjhwWcqEE6cXFV5AAJUgjfn09v5iXP1e6IC1xE4iBSTbqKaZLrSDvq_nmu5exQrDixd3APe_ZsM52da0M7Ry2E02F1CH9ZUeaXA8LKw91KcMGSfXHjbbmxHifDxDorqmGm4lcaUdtnvkLtG_BdMU2FhpJfmMZfgE-RC6sIeGBskHsuqRD_ZmeumpecU_OvA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=MED9mYvpN5tNUshYRqfncf4MNR_1y1Qsqdo4C6ZvojvaSfqTY3aRqihjZBs3H0ng8LHSgZC7KMiRIroDyjy3p6FerWEo9k7kLbDzWAH27SfAqklqTmBJMm5Dx1Y2aOSYS-q4arVUuGbmPAJDtndJE25X98pio7dOtncKhFCeknIEgcYSf22ReqMVP981e5pGZMeXPm0DD_Al9tJzJ6wX-Eu23N9XBHEVo2Dv7FTQvRyYnhtOb1M4drtHOWEEBnZeZf2hpAjkKlclBq70eBmN9D5ruXOOUAP3Y8UORisX_NWYcnzNCEIxVrgEbLaIZuq_5VCtPVb2ZPDkf3MuUaboVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=MED9mYvpN5tNUshYRqfncf4MNR_1y1Qsqdo4C6ZvojvaSfqTY3aRqihjZBs3H0ng8LHSgZC7KMiRIroDyjy3p6FerWEo9k7kLbDzWAH27SfAqklqTmBJMm5Dx1Y2aOSYS-q4arVUuGbmPAJDtndJE25X98pio7dOtncKhFCeknIEgcYSf22ReqMVP981e5pGZMeXPm0DD_Al9tJzJ6wX-Eu23N9XBHEVo2Dv7FTQvRyYnhtOb1M4drtHOWEEBnZeZf2hpAjkKlclBq70eBmN9D5ruXOOUAP3Y8UORisX_NWYcnzNCEIxVrgEbLaIZuq_5VCtPVb2ZPDkf3MuUaboVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lk22wFXfb0T4QPQPASJ75_LywNPAmUwsF9JhBepoNHsuks9tFhi9hO7XNi7yo7G7PfuS6n8bQewZNtX57wTvaKQ_ssbBOikeBYfdh1mp1Cfc2KBLsj7uH2ZgT5TWtte_QBJbOAwgtoqg-VX_f6oPcJfj0HG7_o6rIsfuxoovam1o9dhlVzBQBmyxiQIoxaiupexsbRIZyK-j2R28lGkA62CgOPTUEOPOj-hqNMipfuxWVX2xt9KZ2TYJAZd0pMPbD7oSl4r32SlEmqrZVdP6FZoMTTOqzjn1wNMC_DbolqTu0X0tapn03AdvZ4s4ZQJv262ZxuOmM-4uuus5VXggbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N06G1qOD4uvvOVop8OiE_ue9dEp7BCgDXNJJFVYsSII56RG2--jY5u_xoAifFV_UcgX2zE0ILwoU-S3ptWQBQAmE-qMf1nuGv8CHC8ShZt2FDCk9-beTMiSNmh-5Mp2D0mF3StdetZ3ItGa6eQsdcMoqgblNnqSHKkQ53E3sDgFD4JXjZ9qyV-OkHB906cQ2wdROis9SNfNq69ZCnzRx45gtrqj50nNu9a63LsGZqHiXCFWPexjtzwwH4R7DC-lgXDv55VM-dIAxvCZsb2tqDKdaKp9uPsWOe3jwebfgPBn39nxdv1qMkVKZjg2v9USXFUF6ITvLL-5icWuylTq9TA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzwGGA7SRTLFtcR4qm6EqFDuzCdzavmoaYdhiz_M0gPZZcqdghxm46lGh9mxLnlORxBm3N4h8eIDXCvycDbz7SwgCm02DC80XfVm4qBck06IGX381umiNe3GOLV3lx6rXhLKCZEkOo5MoiusLgyMYigPPNnZhiOXOGo7DXcxDmWMfQqT6K7bT499HVd0Oxua-rPfL7VA5EP0gNA1DERl81cNSpYWSe7vX1TKTv4xGstRlUe7Vf4ejvToHRw46wXKykjQfE9lThWqa9ZePzcq9Uu0tychW1ECljdYI-x-9I8KdJtPxBswHyOV1j_1HqIDJL12emvLNO6mIYuPUhyrDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHMrviH541jDZ0hnHT65Mej09TLcKq8bb22acgomJPed40qdTuPdJ8dPbcNFT0XgEyrARFkSKn43QVJi4mMEGXEZbXAGkyOacGg6OXp9LELbrYs3A4siJXPlMm-ri2SGzP7Z8a06HM_fjYTiiEyuxBpTm6MY4n78qVVlxlnHiLhzUvu1fj51uNza1albqcbtjliRMWA0OI-7qdk6m1LlhUQxKhmtXKoHOkdnV93PHjBF87-M6zkjp499cJ7Oyf5IIhO29J-ZckPtxbnU8HQ8QzT_6zBMYSpMHriBtXlmnjYyr8PYV50_spR7HHPfh32qwztE7o9dcuj7hUWx348RdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikeOOJgSD4SUIfFvwJgcbKb0jCM_xIGxUir35soOzRnzwiAfSHwkKvUOdltkHRSGgRUvTfoK1VQmEzwEsp2QVyViAKNiGZ00h8-RHc8x5NVV2im85BzWWgIntiGmz757KLVmgvGOGvJV9argPuyJIB7tJyhIUd-Ra-Sttf4-moObTu65vDOsj8dqQ9u6sahmtBSbxeKC7Euh6215BWOlUF9Y7xk3A4ICnKx8x7PU59Rt2srHPdWrLCrNwwA0r-wWssPRAE8_U-W4SUDdn2aWmA_Qvq2DknBUqFA4CTHKYepaedR2kdfe1ELeuSpf569MoGvg1PEcuH_nbFcmpyj_iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9znhnOWucNnBZxDYxL_t_5jdsZ2eLSUPqTZX9QtzgNJs9wFJeSYU8vSdqbFDe-gm0VE5EjypTlJol3eHSwYwC9zhQdIlmPyjnHaVYAy8l_ISNR46JuTbTsAaYjmsyAX06EYEgYkCEj8ISgzTeHfZN1ghI2sGrag1R9TeIETVS7e1HBySLsI0xESAeWfuc5EYrBSXdi-MShO-q62oOUiO3_ne4NJdF3oV6wUxgHzXQtRSCN63ZxceNU0IDZb4zoVLAh2sXZdWk_E-rK0nbcvEl1QMXuNcZsqkr5Lb1IOpHRwrTuOVuXLk0lMYMXt7_7rdV1m09UxwiHR6Y9b8dQReA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7J5uJSeuK_E4G9I6FXk43zLZ0zwQacZrQLYYnJbo0LJ0IoRVFlSDYzwxfH2Kbgu8EeHsFC0vZzdG8yZW0Bbz_pPx6fr80WK9D-SwAkXaEmZpgMwjvWnV59HbL1_YlsgbAogXnNl66OJMMDHVmN8n3qFkxTpw1hQwFzhuhwPsiQjTKXVL3kn-aA8kN3suRp4dXKl5loiU80GfcRFoxk4x4fUS4RoNGqUn9PgbJzfCXQHpf-9ZXkyzMin7KJDJPGdLhKim8AFZs6yr3gC6MJvOtJtcxPPSC5iDRLcOvaoju0rplfZEQHPO507SjM9xSFa98_OzI_XnQWgvDZ4eJpXzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrB58BXyqqUHjH33P8VILrhX8nEbRnIK6Qkm4MUhCGe0AyR7uiaw_ReVvutTejXDu6MENnsCPDyJTt2J6qrrjj_l6k79hF8QJxmNP0G803m3b9E_x1JBcRXOCW0ktFN4zG11zxBvLebhdA4houGJ_s1B2EbjSWcQYI1Hzjnoyk9W-OKSyAcjPS5DF5psxxSnLAL15wZe5--bbst2aMtfczCb-2EtQTu8vynYEjd7PNYnRMszzy_yIDJkW8cXLDPaakGfYKPL6RISRBoscOED1wIk_kAdgnj4mDVGPCtvDrlkhU2kgNBhlRofXi7Mr_tiAbiRmg_TqeqDoRBfH1xjlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyybCbtQN2QayMzTYz5_YKJ7Ta909GNG2maKM5zl9vxrBT8ceEsk4VqPtPDHWJrrPzfAn43hqjwSyqUyLthnjczl24agFvCWnFMcHEswEEwD7vtxPoZvVpDTbUBGKnlo5I8PTaSI8naNLPGqmE4kQC2nazrISHTY3faUZmCRA_FfQvDu7eHgEsA7xxnWbnRxFNB7HtgMsnaUPcV6jZa6Dn9kG4ThmgjticAWSbrTuN9s6GV7J5zUDiN_tGDod2QC92Ums-vB45MXy5oHmUy_EFtGevDaqNuj1DUfAlZZC5VNK3g7wRE1waROs37jklBPB89FJQ114Uw2Yx1cln3qIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBEudJAPDJvkZ1p4OVcwa2tI17STdyHcn4MRVyZmm97RgbWgJL16sH6W8YV1QhW45oh5-Bwwz9hG-ElWMdN8vHxzW4SVVlhlFuliyA7stODrgVQq2iPZeZJ0cVqBUqkuLl_ysTO4HRncKUNQM3r6gydEBV8Mag8d5Or_mvAZRkhADR52V8roHkFcnr-BJCzARXM4FPQvN9qK2fV8jAOsn2VsSk4P963YN2_8M5ZcZ3CbZpuFp7B0yTY7PiOi8-G57nKHC61_xZkLNuhGKef7huA85TW2Aw2HkSz4M5X61xk2aig3KUyNzJd-0bV59MWqyeSE2ycoaeZwb8DAsIRKOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUUbLiflBqGkn3LkbyxPEACq2s7CFJw4xV5tbNevWXim37B8f_n0wyB3gTqtLXxhuOIAJF72ActMabSe8GH6PLHc86HlcgjNDc7yato3zBkQtkyNPKZVhND6XeSSzvvusr5aS6nRfuSSTlKUJgqbVubunKFAzmc12DCxZFDQZTnOTZlkK_uUegDjgBAaGYLgKxxVg4pqGHo2lYaxQ5v30sqnP8naegPveGn8-BqOAegHEjY7Ah-AFRPMgu4gr5p_MZJPh91QPvxns9B2PoQIv-1RBbohq-rcEOe4BGqyz7Y0IrwQd2KQ49PHH7lQg10voQ1w1_RXy5CYLji-G1gFLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLIokyDjfhLqnvJV24f2KRn-pboBR_NrRv7GmXEXcgCCI9iKcVFlRtTKowF1aXxmR0Xs0F5uPrbIdwS4zc90cTT--8biH7ALCTxyWDTRo8nL9XT8JhKUSVI70xUKrwPuZZzpU8m0pWJ4_fE76g-HmEImihuvj6EonQMvuzlz6xODK6DdZXYI3GEM6Ta3GigqNzgDTtWD87WjGjKFbTKs9mgWJkWPkTnMTnAdSA1fZ1pgzWah-RYTMGhhuXmtriKuVtkuBo1LwU05B-OjRIg-K2hhKXTs_GhUtGXjKGA9F57xhxlZhprluzQ1BeS3MFJahn5k0ajTYsHQC9G3CbrHOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKURKdaZm3jOTaau41EVS8CAmjz03TI4lKB0oTAoBkKLicLK1wa4Gdf0-AU6CdM51_QFPW_h9vu9FOFb1vdpgxirwpqb5mL8J2Jj6XTOCWiZcNq9OdFxQ9nJcab_LOqlmENcXPfcXXNhbKhYoRdMM4vLI3POnp97aGywjkMn407zNiejj1JHHi-WX2rC1I9Gtqlsdh5gWXtYAnMjbCIUvAwpVUvR9COayCZnp7KL7LHMS8cL-QmVwxjmv6iFgoyUhFyhW9Mr4kbw-If5Kxx-BXsjdg-scWydz3GR9OixM5WFKKOhilqE_tmzbMue3HnILatbUhc3pvmg_J_u0cQT-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWz0D-sK83V2ulzSr9LQrhuqG_ug_CH7beU-C6uVR6xK9eaEyqKeIip8Hft3fAh2t0C3tjyLveCeXt_foSr7nM44EUQcAyaRjPrxNi7Af5l_Wq_1HZiWvQZB45EqGnVtawdaN9pwzyQsMsPK2dgQo9PO1aS95hSGcqyfJlnGJslyaOdwBhuhMl_9CRa9UGIOTrbqOtCsSzgsaYGilXREz7YdYK-MAqpsM9t0Qtsx-w8f4hJ4-naiNS6e5h3qsO-_0KBaJuxATZPxnnlfnP-WwEqR3rgRpTT0RlijV-_F0bD0qcRvpqGAa_CC70AWkf-Kj4JimK1ntLAJht23Rs6Hnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQL-K69bRM_wrd68CRZRFP58UrSWDaIUuMGIqoZBcRyPuKyXzRsVuKW6UyGkW_XWN6Gmlpt3N88hKf1cmNgsM4_xlJLyrGIdsianyY-sIcwMjh2QCAS-yWGk3XnzJPVJiOgG12mz4-GmsuIFSOTXGx4wA5U7eN2iat84Xkpbz3TZRJVYZ8wF3InAsNs24rI3qDJNrKqoT_EsFEk_m8AbNcfpPKuqHuGK2yzEUsLJP9Oilp_t9VuKCMNxqDV5QdlgeLyRrNTQ89Tg385APIPpReAdc-G2hRYqGCgtmzOsfVFGWMbKrGkFhleVMlmWSfVgEAvoHZXpQw51wLe75g7dwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niH3kcTmRYNDEEqHFLgTygbClsnyVCtbtyDJUeq-Zuzryk1WgFJt1qtZxGH46iGAZQ2Z5J8dlTIcmuX22MxHXOWK2oSJUJT6l-lDPqabMeAj8UaVIcvzqWhi9Kpakpt3rUKEFE7mVsNW6kPq9QfCVJYx2FGoQprpCOflxcUjDuDk0Bi84VgJHlnv3J8ut2sNDvYmm6WZ_BXfPU-tbX3CnYSOHvuDDSJUQZ3JdeseSQrF_jNBf6_OM1PnZ3JDQmEUkDf2QDqNWBde-JpS7bWcyCjFj5nLjBVdR7E-seKQ4-JkC2Bw-MfIfje4r6K7HJE_Cad9oOdgjpS0V62lvg6g4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0uuRm_xt1Z_UFm_JFqkbz3INisVvR3O5a_HiFdM6ENGvJwKm5w-1AgwgP6u5qTqXUHi2t8zt5ZCPezu-fgQagkmy1VvmyYlUwJKQpu8T828U97DO6LSxHx4CHlC17E-QBlD8dwC_OC1c_yrsdCnye6P3zGEJttTAUAhSgHhqv9hyXPWeS-J_XwHjtEPsM-0qATCmjKUlSP9skxecen4zirj0GhC4uHDteCwSmCcs93qbyen7LKtelEqGGLehPQGo_MwQGzuHFM7gJmc4LK1DxwBBHnDJk1zUeyF8IHUy06qpaPGKFWNTO-BrfcR_l_m6j8zmgO15BPAV2KPZ1j2oA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjOOBFAVZtz_PhyYg5qO0NCvkA9YvsQuYuBFfI2LZYlCtRt_KCvG5_8KLvE_IwkJeW0BoXde8JaPOqPgWHq-JDEprt5Eqe3etA46VxpjIc40QGgmaLX17ffa7x4ITrVwJrXhVvSqD7dwBtioeUmUOCMKEB3eh4hvP6TKzxDeonnvgRcvzrQFIRRI6Q4DGxltlhx3C87g6Z4AZWj_l95dvI3y6f2Tjz8Jk25_u7aSw-SfEubuP2x3fgUKPmMkFddN8-CfTNzzfTFV9n09BFAPRpztyG1kdcJSphV2hy2o3sqO07laHTTdW73QgbnrXkOfdHD2omBFQoFA6nhsu4mpbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oVQDwP7uRWqbLgdA_bURGTV8fZNkQK0Qm2od2p__xhG2S7jHEB30qijSRvOKT7oFedJGOUjGS-F39Az9d3J53W_PbHfv0yzBkIcwCjhI9xnJjFAlp8UwFb7w35-27YTO9UPbuGsQ_znnsUSe88apJYnqc-9LGISerVkA8S9Gn-vT93fM5Eon7iGEGy3IWlBalFkRED5YKr1OJYhsIvry4LndCEFFblkWfotjr0xY8iVG_rZT_nlMg8_AEXOa4CIZWW6d2Zn9c1sDFvTVY_A9E5J5yr9XaI27-nyZixeBO3yK7R2XjMFFE3AtDINY5ezTdwH0YfOf1u2g-NMcUC5weQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8yoORdqaYPXsMUwmtF_dYDpHMsfEsEQ5vPLTqM6rMMOseNP0gPby8ItTNSuWTg_X8CRAKFZ8dLCIybc-MhZh6kh1NL-nfGeLDomELtq9UevHIUQ6b7446unoCUM6mu1wRQAoUUNUQrXl7Tb20Zxgn_wuhKZEKPDsugWhZPfEwoboenp5l_Wfn4kT8tbf1LIGalQp53_ujTzbdRRWVhi_XDCfQYzFDRSfNUzVJj9i6h_4_MZpzj7RX-mDGUvg6HnqntCEtiONHA5ZD8pzf8sdO6DX5Zr456EgY_51jhyzDpmbdH5cNZHZN8ODS9WssWzyfp-Sf4nj5COmakkkY6XVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WtdOY6iw61zmm0StZjONPTj8R4BbAlrc6ZayrlF29CdzWfI2BYWzIQV0TlPxSHjys5Hf56svMU1WURlgxOTMxMT2Wx5EdCH4iRuluFHw_C34JMMOmqaxUVUxG4T3ZS4eZfYGndjrjauMFkUR6wYvc-3-EFbM9K0Z5PI_oAmTAy2n7ZvteASdm4nIZsKngRvt9boz4HYGOI9GQdaRraFOHsZ3GJ1sN-7Ks8rP2Tnve3vszbwWnHBXNnMmgeMRDL2pFIQV8R70PeFPd9bGzEe7DM2gzbcg782PbSpAutXGGsdSzVKqGd1DmPymLTwHTwbCfnj3zZfbm-kC1vr328bX8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=UPhnYgpCdrk4o_DiTOK-hz8UT09wIQFcxMfc2HwsmAkQdepKCjpoLwFFXrVzNkDLM6h0TJsSAbu_EmvL-AfrVLf7SDZz2qYggORJnrqZ6eWhmjvZFKxDlOO6wXeFreQldOJYs7IrqWnD9niGOrpOlYUAa8btJ0xTMagcvo4e90C1lWjIeQ9hJzIj6XeKyA09CTRs97EKypFJew8WuUUzZH0VTtyXF2UxBYeBpNncW3PSQ4tOK818ijd0K0FrxMuVoXYo1l7Nrb_KDVIwGMMLQE72cBWucMvVeAkU0IHhMQ-49j_xOLkRfiacwUkllceCyOvJ4bNkMUsJCcEf7--2sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=UPhnYgpCdrk4o_DiTOK-hz8UT09wIQFcxMfc2HwsmAkQdepKCjpoLwFFXrVzNkDLM6h0TJsSAbu_EmvL-AfrVLf7SDZz2qYggORJnrqZ6eWhmjvZFKxDlOO6wXeFreQldOJYs7IrqWnD9niGOrpOlYUAa8btJ0xTMagcvo4e90C1lWjIeQ9hJzIj6XeKyA09CTRs97EKypFJew8WuUUzZH0VTtyXF2UxBYeBpNncW3PSQ4tOK818ijd0K0FrxMuVoXYo1l7Nrb_KDVIwGMMLQE72cBWucMvVeAkU0IHhMQ-49j_xOLkRfiacwUkllceCyOvJ4bNkMUsJCcEf7--2sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
