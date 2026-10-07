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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 13:03:45</div>
<hr>

<div class="tg-post" id="msg-8022">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=vTEDeV4Y_qx3OuD5OJFkf04C2nMKI0wvv5FL-uKqypew7jCrTYyVSv5HaJPjliYOaxbgvxLcBpImOf8yJky1wefuwHGcch1F9XO944A-RrrLRSw_VlW15dgX3piJSEDpz6hLR1caKXAGeDVkVEqNJCISht3Dt6ptyg3jJcb2t-lLf-FpVSVqDKYwBl1bn6y2s5D2hY63XhXKbkHQX5_W22aJud0RtZDaEQsFZCyX9XQsP5prrhrQ-FCQ6MPXmSsGzDiic5FkzIkxBTUqMXGjalUW3penAqtd01czTfYX5HfkGdH6UEMsk7iInDJiQEMjkhToX7660wPwDfSa9tTzzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd9cce13.mp4?token=vTEDeV4Y_qx3OuD5OJFkf04C2nMKI0wvv5FL-uKqypew7jCrTYyVSv5HaJPjliYOaxbgvxLcBpImOf8yJky1wefuwHGcch1F9XO944A-RrrLRSw_VlW15dgX3piJSEDpz6hLR1caKXAGeDVkVEqNJCISht3Dt6ptyg3jJcb2t-lLf-FpVSVqDKYwBl1bn6y2s5D2hY63XhXKbkHQX5_W22aJud0RtZDaEQsFZCyX9XQsP5prrhrQ-FCQ6MPXmSsGzDiic5FkzIkxBTUqMXGjalUW3penAqtd01czTfYX5HfkGdH6UEMsk7iInDJiQEMjkhToX7660wPwDfSa9tTzzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابزار Muse Video متا هر هفته ۲۰ تا ۳۰ ویدیو رایگان به کاربر می‌ده.
‏⠀</div>
<div class="tg-footer">👁️ 446 · <a href="https://t.me/ArchiveTell/8022" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8021">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPq_u10OhJDa0AMEpJXEwynHY7H05CnwJfl78hnFF1VNgat77CzbXs6q82A_T-Zr8R8ZU5sZa70s29HqqIqtE-rDx9kSiR_TKecRJJmyAjuhjkUbD5uDXA2d4cOYGXFFGZ5Owl3jgQGgYARj3chxo2F84FviEz3ouxTaumhdpczaZLMXgRzrENi3HS368k4UrrqIDoJHFhtlBzVvqQn1wA1UkdsUY_PVzR5OcfEwK1XlAPwlGVIHMAL_SVRnYqNGvccr2O38y_uEwMo8Gt2d718yy0-hg8h4JSZSdoPNNsrCGLMDpOi5oc2G24MaadYXkaDjeHmDZTfNY9gn3yY9tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 490 · <a href="https://t.me/ArchiveTell/8021" target="_blank">📅 12:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8020">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/8020" target="_blank">📅 21:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8011">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/ArchiveTell/8011" target="_blank">📅 21:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8001">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/ArchiveTell/8001" target="_blank">📅 20:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-8000">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Izv2GD3xj_nrwhnVAJk59YOY9-BNtGNDlIcWHqH1BP43mfXxYIFucjQdSEPDoDAa0_xOMAFbdfjS6bcRyzlJOdndlk8KK4J1ebft6SINoNsnIPqOUhUb94uX9s1ou78MVOr12xozFSt-HvmY250aQa2tO0itnqyAJ_sDJIozcSmvJFMIF86kGdr9EmYVIJZdrDwFZaFn1mKnm04yyqXKjgyThyeJ9krBA5CB4Ta0ijz8thZDUOyW9WpnbPCAwBzLg9RrCf0h7b8klGiV2y4drjHrlpsjDzVhe-macNqr9Fa7ktFlKKN2_UD5rNLIZuknHmkbhkTtov41bwHCDcYnpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
اجرای اپ‌های اندروید روی آیفون با Husk
⠀⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/8000" target="_blank">📅 19:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7999">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ی ابزار عجیب برای اجرای اپ اندرویدی روی ایفون!
😐
البته تست نشده
به زووودی</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7999" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7998">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7998" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7997">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7997" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7995">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a0863023.mp4?token=Kgr4dGgkPLWkxidcFeWvx8FLiIHiLBdf_dWJijIPgg0DgyAoGPnAmF4-3M1KrKXHL7VWWFUOLXluhEdEDLBpqaiBOVcDnr86Wd-nDayvkupagCDA5JWC7zLmf5ixQuxV862TL3jeBGQ4rHGV1qRF6VdN7u4b0CcGXc89AWaAYqdHNNq0DAV67_Wg-h6aeBSUzD_BY006UAxapRvLrQlAshFgq38tqCAR141BENFDQVWuakVLuBFR8shLWm9elDTy4DuMY9_AxM3B58cqW1dTGyAtpSlhhxB6SSl5saakcm_EfnVk2DoRmcFlpW1pxiEHqiPVGqaQXW_hVwvKDBFgQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a0863023.mp4?token=Kgr4dGgkPLWkxidcFeWvx8FLiIHiLBdf_dWJijIPgg0DgyAoGPnAmF4-3M1KrKXHL7VWWFUOLXluhEdEDLBpqaiBOVcDnr86Wd-nDayvkupagCDA5JWC7zLmf5ixQuxV862TL3jeBGQ4rHGV1qRF6VdN7u4b0CcGXc89AWaAYqdHNNq0DAV67_Wg-h6aeBSUzD_BY006UAxapRvLrQlAshFgq38tqCAR141BENFDQVWuakVLuBFR8shLWm9elDTy4DuMY9_AxM3B58cqW1dTGyAtpSlhhxB6SSl5saakcm_EfnVk2DoRmcFlpW1pxiEHqiPVGqaQXW_hVwvKDBFgQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
بازی GTA V الان به صورت رایگان تو مرورگر در دسترسه
متخصصان موفق شدن کل بازی رو به فرمت وب تبدیل کنن، میتونید آزادانه تو دنیای باز بازی حرکت کنید و داستان اصلی رو پیش ببرید.
برای بازی کردن حالت داستانی
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7995" target="_blank">📅 11:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7990">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lk-Jd-Xb9-6ixhUHpIJMKwAvHK-5kvWMHNo7-Ji_72ggKhtaoeLjBcnjrC18Mx0sa5L4HWzEwJQx7aY2laq1H0yWfZDgRD-wGgi0JQ1StuXHmKY3CSrC1_kHG-uyfbyLfJrqLcxyxznfT3YO4zBuktP4iAtxz4fXVr_90k0gg0NzwGmcIyxlQrZcsBxoWVc_OBmhm5WHkpBPU9sqED3eMqjtFQbgdwjkna3nVd9gMave97soonlzFVyC69pjGnbYqPNv5G0TBpGui8aRER3K8wyx3gu4X2mzeOV6ZREu4urL2sqYIHHKoP1UpfZ-XPBogsha81Hf2fzY3Ujs2fS-lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lQRIUAa7xAg1j5P-W-3whKoq63ObpOHil7HlFmRMIQ-xMaZ6o2WAyW2CvBafe1MGDHb95hi5mwTr_YJD7awdRq1HYpjUoaY9XTZWZTP4M9U-DCGXh5XzcfF4uC4-sr3b3oMGvVhWeBf8NVA1j9pauuwsecBlkiNen5XHy9kw6F_MSPzGyBZ00ir4uyxFHqZcpKN1D3bFgaudRatVuS7UO6owLB2-l0Wm8EwY4ykWioe8-t3oFjsLe7348vWDas_PPZIzpJDEjgp42W_6rbHlLfaL7GB82NcOaaHC_5E1p9qKQI8oj1_RO2LjAu6mwHn6YRpENO_pIJUviZbMCuHxcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0zQiTsaEC021OjpVpE4Qs-b8kHCx38gw68g3PsiigObtHRDeNmLNsyP7r-HOLY4cv4lKJj5wprH-d0HnDCS-Mc7RMvp6ruLMBKNV7HodjYfMppbchL52U0Mk3wzrL4E_b07M7U4KmSt7qZAymvyzeg_3T8SuYW1FX6qcwOKEb-Gz4HpDxklDsbhYWBBNMarmL63Tknevh8lHSegStcxP7tGYgMh6knrxnUJc-M743i4T8SdozP-YrekzpoRVtbwVXU64XQ8pgOiYf9xuABtuy-bnJDDQW_UWjGHg4Q79bgN5j5HteIqLnpF4TAJZWKG_5CKqJjBBUWk7YCQlr-k_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZTdP5zK6Ct2GlUudrSqpfZvdHPtoPvx-bj2fbjhgcaJ9O3bI8JqfzfU0-5x2rUJDBuOZo1yQXQD6TdtsYbAa5e2GeRGc2XtQZxtidc0PrXfJbCU1qumKM-H0uNu8sSDtOHjzlCHIj_X10qnxwl8jiKZNMYjl7k9MF7Fa7cdBkFR8z2NWetm7LXWq0J7n2Mn0rwQH3SfCcglWDu5WNMe7e7GJFm3hxF2zzGliuFWVGa4_Hqm_DgnzNHkAmoxMebugWG09XKGE5LsMbDwgxs8MHflg0Luu63ZRcmuVS_-iTFEawKHZ1y-I45Mgr5GAYNSSEDmTRTuXolBKuUImLXelcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWJ7qMQznaasLzMvTTHZzf-W1QjNMUZq7L_ZKmutC53tR4ZHW9TqezjG9Fau3EV00t0_y-L90s191LirU8ogRj6ET68RBS1ttukqrq6aSb9OiQpZsgkaE_XYELxK2wAuPHGMQ2F9A3J-s_0oCly6AhLOPQUrR4zCVHSryK0f2e8Q0x9U-4sdsOiY_E5ezE_S9tCm8-SIzSAMSrUwq6ZP8i2Af1RELGddI_EG6bVsRtB6o_pov7nynM1c9ukFUetBUN9CX_b8En3IlLaQnIrobXwbc7o8fzicYxWxoVPzZcV5h1jqiCOpvX8nKnW35Cq27INT_Hqr72Gl3hgfFy5nvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7990" target="_blank">📅 10:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7989">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVzqBpbdvGPvLQ5dYQRLy6mHyZL_qnk1T5RYg5ARzWtq9qitGzjTuAQYRVBx13Fj3Xp62qYbcYI6g7qO0W5vvPyrX1fdz40eosratR6f-ZBFFWmqO51Zr3YLkubMHKsxn14h0ZeewisfHbFAByMzoSfO13C916eWnCzWn0IDb3RCXrX58dgTl3tPN6T7XUnQx5oES7jtAz7EtlmwsYh4LZ97e2P3kdd-gdr2XDdl3qEpVzyz3LZ-aEUdEOqO6VaWD6du-AF2pmg5fePUHMkTcb3gJrUPrr2SWSjtUTs9kaHliNgCIChXqdoa-JiAGuyV-EwBZs2b52K2EhlJ8lfRCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Nano
🍌
².¹
منتشر شد</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7989" target="_blank">📅 00:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7988">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/7988" target="_blank">📅 00:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7987">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nk4EJJ1qNcFPfLGOERseeXDy2JqAdtYlgw1ek4tnDJcIUjoTCbyi6kkgpS39BduDgt60rSC2OTq-dalQ_iWCc5Od3wQ3xd0ED_mkl-31INpi7-yDPHDCwwt56IZxanm_pRTefe5s5DOrYGAO9kKxWew9HMgL9-EzdUEOX8sZLCVCJXf1pSfLwxkjObR69lUzyXyV-vypb_FbZDlGg9AkKII7ow9yvZqMZjRyF60l4OAUuFXfNgKjYKVt3T9Fb3pIqZyW_OjaNKvrNqL5gxKurrUmdjyV0aNgnuDgjfd8obMAZwvf_eXXkRVsjb1BDbtLBAv0QAGxyHRGU3GpEiZsqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7987" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7986">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vuGEx5tSjaJXJ1JQfWEfGb0_DAH8vvivdTrm34pcFMGk2VAs5Ev55bMJOb2G9ZRGwfXWu1atAK3qr_9Fnm45s78nsDKPV7JDEQlTVf7Bnn0duKdT-fuMFaVa7qT_D0v6UvptwucqBViwX84-RYPPrClJ7XqQbrh5pCypySeu6CK-o23mmJTsJzovet12SB-J5-ELO-AsmfzRPbK6errkVV0ohZSb1oSlHL7QIYdFjjWifZYrLbiWH4xuQmSa4u08duPZR9rUc6g0FfuG7IAliysQoYI4HoNVE0DDHjSe2Hsq1RntXIb0lSKOI7hTQVIW0EwBAD3I4Z1MegOfCGApSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7986" target="_blank">📅 22:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7985">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ir2Th4wSaEdhpTMRi37_jIZotP-E49zkycPd8qlmuRJGX4waghKOhtxDf1e7imrLsnR8Lkc_JDRPL_4kJONYX-udnAirH5f9KbU4PHv8L94XAZZMgFUo0qm_YdLwNOZJl-T_5D7RTVTz6dExhda0GBq0P3lQzuF_cuJkxLaIsmlWfJKmUmtA2AI6lLchXSllOGz5231F9frDWeoS_9tUBfjmTncLQZUXe82D9cn548fuoLnTlercE9WY0tGGuAknxfWz51jrxwE6AQJB1R8aufCetbSNYV6vbWcTcpOInXDZf3UDi7zCDoou3Z96Slh08FFqx8BmHPv1eQMdXTBtog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7985" target="_blank">📅 15:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7984">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7984" target="_blank">📅 00:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7983">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7983" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7981">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7981" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7980">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7980" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7979">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">قرعه کشیِ شماره مجازی رایگان تلگرام؟؟
🔥
🔥
امشب در کانال تلگرام آرشیوتل
بالا باشین
⚡️</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7979" target="_blank">📅 19:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7977">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfXu4kCGboDZqLa4CcCHHV_rI0t0fK3RwOARDeQiFHAiAkHZ513xfg12Zcl4xE2ZrD0EUZ1R-57gUFyzpfdOn0guCmeDD5nzIH0e-9wJoKTm040zvv_T2bQd1FlFfnDgO1ZAYsyL5gpJtOYA0Dzl1mDv-RDSbShOeCwfka2-jO92Rucjv28Y44Bz4siKF3DgaHOqbjILUbHZ2MrVmhfxYNhzirpcKs6IAZEchqQ0-3iTdAvKo11P2lsGDiKGcmSVRz5perBJT1caD7BITBk7e5FKh9GyGx58X9rQnI-XLVa7wkOMITazOgHI92r_X50UyAR5YtFasFl49MIjcPihIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 سایت جدید برای استفاده از هوش مصنوعی های محبوب
💥
🆓
با این سایت های معرفی شده میتونید توکن دریافت کنید برای استفاده از مدل های محبوب Claude و GPT
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7977" target="_blank">📅 19:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7976">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHPg-irptsD3ZbOJ-u4Ul18SR2H5RCfXUF75nFNUnjuv_ln54tdwK2PGCoMU9pPLMJpqL-yqyELwdVs_15vVEQYs8pBSHMAWqhYKYGp2yF2_ORIGORu8LuiBOYf9sf1tTR-V6i74h2mKwqF4dCQgWlYU_XrBI5AfOIJFYtMhp-piuVZ2QFG0U5s8miyHxHU0ZOIaDrs6rxeOSJhLn357dqR8xzwv_uCXC8J95f-iDQ9YVKlZAkUYNEBfaYGG8VN_vduvZdixiD64FdIwV2RSISHLQu_H31G7xuJbqqD4iyHJDo3fOKL-pA-YRNxgaeQonegIudhlQhIyVSuj-3ML_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7976" target="_blank">📅 18:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7975">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTHMSNJVC7IjSJGHBdGjejj2d5rsJLjyxfqwHTeLccst1jXrbriPh2iX9uUN_fFCg6uj82G1_drCTzHxwLgz8ACwPUCkxj6Gf1CtqMGInB0ZNWAUOm1fjUo_z5X15JF1OYhgWSlTYXO-mOH4Gbb8xhrTuzFitQ2ArSChrhDa_o1uIi5PYm3P30CY3TaffAtw0wabaoVeoW0O6yRfwKBYuiRZuZNMQrHF5xm2j01OIDjDNmfovOZrR-DfzmZSx9I37CRzExymvPGjXPchHCl5mZ-66IPBcmFVLMb8_zijqY9iv3Tf6b5oM3Hh2pSLTmHXUS0W8kWxBJlOQjldvZLrDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7975" target="_blank">📅 16:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7974">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUdflPNJfYoZOzeelH4VyWRn7fbhFlwuMzp6uKz8Q-04qOKJXrayNwtPta-neUlNkFMK4wmoWLPSca9BOoSHFpLHWlWf55-I9P9Zs5CwcvZCdzE8iW6PUAdjrqqQi1cWMeSigVSCpTSK0-kJrT_bqW55_tpHRXjjgYxbpDCliv_l2L5KONcK0cZ15OPEIrHHQP3W7SrEGBeUzy3TCqw0XDCgSWM72IQZBwVoFp3U2pvaae7iseOaj0aYMtBdGyAo5qQUjJH8bG9SBNpL1SweUl8HwZjQE_sMYxEaKNkJD9zM7hjv3dHlhBt-jxjkcVQZVJLaYCWVeT66THH8CAcPoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧠
راهنمای رسمی اوپن‌ای‌آی برای مدل‌های جدیدش  ‏اوپن‌ای‌آی یه راهنما منتشر کرده که می‌گه با مدل‌های جدیدش چطور نتیجهٔ بهتر و خرج کمتری بگیری.  ‏
🧠
انتخاب مدل: Astra برای سخت‌ترین استدلال‌ها، GPT-6.1 Sol برای کدنویسی و تحقیق، Luna برای کارهای تکراری ‏
💸
کم کردن…</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/7974" target="_blank">📅 16:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7973">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fxJk9y86SfUw4e96hyZHhNMlXbZ3HAQN7rxWHj5HFqw2ItDUmrwWte38Mb6YDoM0mBVazTI1JQx7ZzlzEvFQSsQtx0JC4w-EEPtcqop7OM1bwpxgcgTRN6wUsSClpe1s38TpkKs1z36H31cqVVXXhaWvPZ0HXw_WCVl_Ra0HBGpWRuA1htFuq2UGzMBngx8w3vlDQbB8J00LxpNMrSqeT3hWBT6nUOk1gbH2LaKphzPPgulc4L8ZnxrSpPj6TGJBC_xZ-5FtqHfsWr-uqyz7E5IFQav2fGQJg56cIa5Uu1M7e0-TN3tp12eQSyLRTXpc_Msc8QUmAEwLlxdNFX_Ngw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7973" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7971">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YA1JMRt9xNNoUmxImuEcaIvo8pds_5eJBU7yu5LJHX0--R20KmXFUp7npVRcN-0N8d5Usm99AnzauPi6-X1V5IbKJeczL0Q1zw-oXozuU3NFeJ2_QbHE2We3oDaG5beGbnHSZcu6NwPqtv-3GCuVubyeyhTJ78jRK2OhYktwS8YtwNWsCbe2r7w5E5XSHN0Yj5GP4Ms22Os_QKN8jKAZBzgb-ozKIpe0DO4x-RgITP0KeldUn03r4d_F0VvL7NJiDK6q-f3PDMhMAsg2k7EHi-YSLSebD246tw1BEuExwJViJwX3nfa9cnxgMJLovOU0wpNgMTbhc2nJhpywv1ydaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7971" target="_blank">📅 07:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7970">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7970" target="_blank">📅 23:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7969">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ651ihEdMzYDzi49M5-hS_lHXZZxdi0s2ozb4IZ3Uonv3gXTwDqb8DlAy_ytmsPWHjf8R4vvbawWnZh5cYrKm0N0U5x44qEUFz6i5URAFLMvUYxm5xzbtJJcKtEsbEAfUeU0VCg-lV2PFb6XDxkDTp0YHkZPRqCfocxWYdrh65q2w0Lqs0KkHazIyHHwElOSVCSkVSu5ORkZBzJdqi9tl3J98Gcgy0-3FywqU_8JAKovOltGx3zeRJaObPeMi2_r6BnPo3cVkq4YKUMudSph0QzLQyn9lr-XsGh4Krx_pDmZQVcKu9_B1HflqYm5TVLk4WTTXUC10K5N_md7eXhtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7969" target="_blank">📅 18:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7967">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7967" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7963">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j94xVXRdGK798WeDxPlT7NgY6s0ZapRhtUSCpefk7Mu-yasaiXkPBJTMBSetwkJgR40zvNzLjWJ97WLl3vs_ldKh9bpdgf_Cgah0l32VeeJ15l0ZZM6__hzD7LhgBEGydF8omey64usuTROWtvFe-pH7fwtyEbu2-qqFx-WMpCzzN8kGDrtdM1Hksr-0KBXb3-rpGJdIxI119SYD9a5WYRHWzmAhRKxP8S2KN53iQ5NWvpWp0vhR8erHGUM2nMN5Mr_c14lSngohdkVh-A3F85BpMBYgQw8jKOhoTyGZOeBfv1VGqgARAC2uP2q0Xnp4DrYbfSA610cm5b8ZWh-oFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7963" target="_blank">📅 16:39 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7962">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BHaqj_LGTn4xrjBaLfaNHJfoDo-ya6LfiaAcjksOUGOhhnVysr-ME6Ue5R0xsg7MmP7sJCM50_s9xwqxSyu7WLYRfZnE2VCaXY2t0In44777ytSLBxZn6jWntK2I7nfGFAqB6qzx8v9ZcYA8gzA0yFESB_smJ6T3QcjgKAfLHEWKn7N3KM40FOn1RWm30TRFKaBCX3NxYNke3Hbqor5xRxBGw4RBZM2QjTeEP1t_fxkPfI7Ok-5o09ZlGocIQJUlrSbtWsNgQ8G3mSzZNY9-W8YBj6zbP6KFOEx1O4DWcg89omadH9B5hATutAKnZ-qllN6XwSSH1o8CEkSiDoeClQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7962" target="_blank">📅 15:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7961">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/In0lWbXSfiE9hOD5VhCgZfdcSjTOdeWj8cl1bW19YF092HSEqLgf7DetQitx2_o9zeZU2fjm5wOr2W0tAGnaLhvCMkaHvFa92VaUVYe8bOpBHVcSF9tt3Qe0AtaFaGPQYiu72s9Px7d_jjcAS6GgdkqI1GpaJxN_KOgpa8Q2zeIFm1cw8hyUH8Bu4R939sD3jpJu1m5UPuP7Zy3c4yYk1THnpAWq2HaCkSF-LMJQ1m-OpPK-LKx-_FlpX3Qs58OiT4pFiS2qA__LnetLhq498_7w2XmNJF7RjIb2o0cmXsQCZXBBpQoOZTP3rXu2BaW8W9mnCvsyH99WqgLUgDkTyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7961" target="_blank">📅 14:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7960">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLtt51WQoYUEKDk-h-kfNoVSAcHB7bN8yE3tD4agv41Z9EYjQuHo29Qeiabue36nGyatgFBL6q7kk2zcakvk6iwV_ZCbgYi63vbmA1399fZxcAzd2N_ZNnWbeVNjamBGT4hkDxZWV7bVUcOg_Nuq2ZYnb2sEdcnKwQpyTz9CR8ds7tDcVjGVgu6Ld_W3BKqjel2XaiEFMdZtxOiOkoVefeP6I1rLkF-rSwG9UxL3hqQRjZyiHaXQtGz7FpNj3ovrMls7CAjPQaTXUqYs502YQkxv9_6CT63mqt5jbwHEnlMK51Ig3kFILlEJI6zdBIGSUcrMa0pRfJ8UsNP-70aFeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧲
جست‌وجوی تورنت داخل خود qBittorrent با افزونه‌ها
‌‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7960" target="_blank">📅 14:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7959">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7959" target="_blank">📅 01:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7958">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">Unlimted Gmail , outlook & Hotmail?!
🤝
🔥</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7958" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7957">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ulk0YPAFh5aULp9rlLeudGw1fWY2Jalncj1HYJebFe1GrZodwoPSbiuLofOS2iBcv2q3PXg3d0RDjWDjhK6uYDNZXDbO7uN_CjbAFN25s9HWTLYBvMFApgue57l3ckA0sCOxyyIYfsiHP0MhvOR-dljytiJKX7zszSchEjwk7YUt4e1yJsPrB0FpRAc3saZp3UbXf0R7UW65C07F76MzXJDTqv7beuNudVpJA5cs0lGeTckBc-3R_Av_AW5tjSR4-2o7pFVSe01oxcGk56TdzHraThuj7ASngjtLUVr78DFrl7G6kF2lYa2eZoz0OMI9YwaA22PFFwDmw_UvvGDjPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7957" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7956">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpkfjjC5Fselg6K6J6UZfCQEHFGhWoYWE8J8crG0k-3_RMYlti_uzk5bIIO7TyAWEu9m2QOUuztwDVY0lQWy30XQ1gQeYKTH2m2KBvP0xBxakxU_fHGiMm81_FccpstKzBI-GD8oLWvcABxzRsT1Fgul5_qMqq2udxYnuurYO2Lohuwzl1HdhuY4Lc-x2tHFqo741SuGRjb6MR9OtQzqpSPcfpxXBqrzJoMP2wzvfAJ_-KJwfKKdBWt_hBd7cEbKsJ7MVRVsBm78Icta59arSgKpJAXXk0BOqqwUkTKCZalOJ8NSlF710dEmQclg0VKlcnqx460zMTtDVdpLOkgCCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7956" target="_blank">📅 21:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7955">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqGibb7jqPsLjvcHwJLrAsKxbTqFVvXr9sew-rDuwFIZ3N7_Tr9NqNS6Lt6ncyjwc1biQtaonDB1i66IREW75VVmbq6d9ExFlJ9pSL1-x9EwjSVbu1OFGY736ZWiWDbgHyJjF5XbCXXnP0Zh_p4DY6YBs1KR5TbNC-5YBe-bCQVjKkAU6Wc6dXj3u97K6NFR6msGVw_0QhPZ5zHKSqgE4MQJpScUl81zotlEaVl72j_72MXrDUzu4921s3LLN8mlZMcn-q7jjCyYP97Ee1x1m37aZHN_gRLIn1lawmtC3wAAttN2vlId2q0hyBXtvJryZm7ZIIk26huK6BMTt3WnzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7955" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7953">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یه ابزار خفن داریم برا پایان‌نامه نویسا و دانشجوعا
😱
کامینگ سوون
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7953" target="_blank">📅 14:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7951">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i41nkJ8JcbCZxikyeJGRhrTwbpPzK7EUXcIMYFrR2DkZUJiCFEzAhaIjTkNiFgK5BpvMiAMXpaPqNvWwcYqc-i2HRkAdbiXLHg5r36e8w3mCgCp6UDOL1X5dr0s4TxlNN2RVEF3y6JcDQ5lE3A5zkLITp0caXHLRDLbHeC5I9V2kzbhCPn1HiYdZ4NeHqA7WY9JXF1YoCu4OOVMrpQ_3YMkhjkjcQRX61ltgwtHwVEqpgJ_sV4ECG7Eq5RoDKUmOKiv2LRyrStGfGE3rPErJhU_q0MnCkfZIcLmHQQvT3DY81gz3tKtTzcYjn6_2lBpp8qbGkC-2Jd0yGQ3-OSJZXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7951" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7950">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یکی با Gemini 4 ماینکرفتو توی تک فایل HTML ساخته
💎
gemini.google.com/share/3b1ebce6a7f2?skid=90fe9306-4951-4d36-a127-d2ffd952d39a
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7950" target="_blank">📅 19:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7948">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5-Ct1fg3UUVNmxeIzjWFzG5KEO__bIX_DxOaG9s50G8ecn9XEC89MpU31Ug5_TJC-lp6ogJjUtxHbawp5BaniISelp1BlGHN89IGI6qKFROGWmKXVrXWZ0ldX-ED5JQGgZ0y-zb2jzf8p0BeMUEdV1-X0XsbyRppUNWdEmJXDYX50y_yxk15rpiBZIr_TapDU0J1wXpPUxgT-D4ecT712BO3mbTnG-8efq5yWcJSITqmUawUEz5whCGCtE9kwKFz7cl0IRDGlUgSNnDk4SYh-TQutOn3p0BTZyrwapg6NQrjv9_osVgnXjfnsZulr4VKtu9Xc3l7kTy7YwDn2kQkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت اکانت 1 ماهه Nym Vpn
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7948" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7946">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نت کی خرابه؟؟
ایلیا یچی خوب موشک اورده برا ایرانسل
✅
🗽</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7946" target="_blank">📅 16:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7944">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دم همه اونایی که بی منت ریکشن میزنن گرم :)
❤️</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7944" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7943">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0CJonbUod9Ha7Jx_mw6OTt7n_W11M11U5uuUIZOSO2yYQ2RZUoqtRo-Oq8FLLWpDliugKsBGbFTaxspV3oqtRjXys-GKNkj-TDCTHutjm0onHGVMPYcYyhGW8c_7MpsxA4Uk-OQe4Bf-u9I_s4DgHN38-M_-1LqPoNXi7Jy3Sv5lsAcCcmz1tFrrc223PcfV5nqh2i3b6-9ewhvCr5-ezd8CY7fVJJ2q7jvnf9s4g1bPK02bay1MnJonTUCkshG5pcsR5PY8u5m4B-VLtkCXR3C5z0Iq3wXhVrbZGd3zC6YIiGjFBzS4uIhOLiNKR9as8t_W1CrxHAJj9FkHpIEkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtDTZxx-C12tFxYDnJPD3dU2mr320o9LM4puCcOabRwWQpyX7jtAjMOkuHRhfUW3kFRxdxOHyJ6YcdhBEmkx1K1zNBhEIkwdyo2pi8WMWzGEOnGkN4KDyOzU-GRTcxhG2ukWbabPo6bZO7Ef0pYEBj82sMKuibUSaJvQ30tvyOdQC_f15w6-sPme99vqUw9RPOmv0Tm_UPPeOlO2LesLeCtmgLV3a8iHTtUujBLYyT3EwVBxHGCsBI7aJDrsjYBAh0EKeNGmBGp4_qYtXiJHknKKzihe0fN3kxTMymm1leN3aiA0fgs-Ezw4mkDGTISbxHh4KKZv6Irjhl_9_ORs9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7942" target="_blank">📅 12:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7941">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_0s6sB08pjaIpi9_90l8-DSy-lKhhUJkW3zqIcD4w6R0VSVbiM1GAmW5qigOSS93U8NYrxasRjkcE6lCuqllYyDuo5tXSCUTUMp3IQdZyOHvXTj9M9fS5zX1JMu7cicBBfvCZqoYaFxUKrVUyOlPzoLyjHtrbSvc9_Hnh9P2ftrFH070w1GoctvV9cy-CUq1SkzFCzJawauxHLLm__hy_3mXv4OCjIyRQTu9rcb3PiRKTdF7MkzKimv_pOqL54jGZ6JsD-inlKk8dBmKUwDFh9F3pioIr9m-IgkFRgeSV6-2VtuJKJYqId1VNTxCBeV72ZsbEXGtfXKfTfo5LGHcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7941" target="_blank">📅 10:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OS8fqm10zKbCiE2egpDOyxex4ypqvNi7IE7j1i0AEq-RaMUqhuYpTzgGr-y6tyaIyfNeDM7iZnShhSCj72jAmdUt5VrgFp0FfFilO3AasTGsKG5FORD3EoaU1m3p4Izn7hz3i6tNk0UJNK3qJ-d_fBQnbXj3guVA49usDyu8sBDSxeUHM0bNRnDy72gHc70r-f9UU0gIXiO9Sxp53fK7qoGMRS62g31yDD9DP2K5H7nFJvqMO3yiirZbIEYfsMI0ycS8jaQH5uoZZQNJPAKGTWWGK7oV3fgI1TK8VM7Ayjm5qclXFGSSrsFEc3-AA69cGSA3Ttmk133BGnCdVqIs1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sizHgCn-AoZsjaSMapjhQQaLpSqjiA2xT-8tA-FSZCJYLsdQEGF_m_jrgAz7Hr75HXUnyL7Xk6qBsTn_eTxnCc1W8XVpqGa7i6-9T81tcC5DDujB3P-VUWNLaOpCx-8g6yXblCNaSrz5BrqfbxZDdR4VbCwO4y8EXoDXODXvtUWv14muSYYpQ8ZkqMmmBoriit1pSNhlUOqPouuDQUSteYC9BQYDvX6mFf1FXGWxOZfZP2GnbIZVPKeBmBxLkg8U3vn9K_bYVJptr5cKPdboT6JMqMvG7e1unbKt-PCyeP7RiiYi20A3unySx96jTIHNFW_gLNp0A6XI4kQYyZBrgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pEKylGmoi2lWLJsD5OqiYDrtwWkOuonRaMvA7BCTgy6C2a0scU_xQ33RQYkVV_X9UcrizACXJBr6RQYc5cLw7o6f5LnxNaCkqxZkVmXYYZVGDrOcQ1x4TRw8E44UJrNvI3yjYuRHqFOmZTY-sgNu_d78iLDuazJtXU4jVOJfLwxig4HnFUc44FyBbTilEdjrpnrNOtu2tEmh1CNWfxzDPe1NLhsW8nZ5jtnXnnSEzg69vjbi1BuO9glUacb36P-CKW66rzRKfHoYl8MSojCsMEMdzB7LuLVBQmkJqVccxyfxax8qBAEzV6mTAmbR6xbny0DTEeZOKIJ53ru89O6ATQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X910Tk3yM7RicT-ykG-INjgUA4t_wm3iU3SBgyQCPai1qB1X7L7WYMnTLBp3uSgIXmbQ7ynp5K2zfG3NudSUnLbgrAbOFv6n4f052nUbnWZAFwh8n8ujsiLREMsFfgSZV1qSpBbDx3KtizSBWtZkNANyzr-7kHa_e_1-KHPIZEqJgcNX-KEid62H66lQZhUCk7FuaCDhu2MABoO8RXB1R4jYnOKSfW_MjhdJKL0alNh_I-IGm6DVXCquWcAxhfG4MRtORdhW3WE-CwV5tr9yU5gQgPWotWordcoQAtdBtFV2p2OuXN8mEEPkZaPrKUC8ddpssrXUuAj3KCnOcGELSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJmsRUoko8qiVrl7XMXUjpCKyAeLe_phQP9TIvjCWiE5VBLWjsnCGnOAy0jPDvtLSWy9GV29_G7fBq10g7twbjuNb7cgpLM1e1ZzWQEDcMzCKgUG-HUUTNRXNItcGFe_55fvqsKHOLM4IHI-KMAddHLvSfVAcq9DyLnxtHRuQvO0ncnmrQiPVcMBAT_z_HklMPiUxqWOZppWfqBS0gxE_S1w2xZifYzxQtrWcQAVCGixfbYmW4IfRuJVIMJJ3ViweDXJqx9Sv1m5_P9fkr_lSSsGxfSvKOoGIavBJ3dNkuYw898oF_MIOu5WGuysHc9ZLURJqXHJQLKeXCWdDQBy_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zkky4iw73wcm1wzwCMN3aQyXZgsyy4WHKJZRlbr-Tw1np5RF5B00g9RR-qWwYs4U8C1UzaBPbW0sLTAv7DN6hOVSBf7rHGJ433UkluA7sFvMxLVss_rDQyF2PYkejp2cvHfni9AKijCM7_9g7W2BMuZTv_J_VN37vgqbimHWMeqKu8j7oZrHXHXBpzOTFgPaulzXQ36t_HpyzLftZ0Bs7KMldM00KvKAe4pZBlal7IBbPfd2TlEIIVaVgXWakWQzTLiRj6tbZrDWF7mLjcuT7VF-RhNZwSNRb7OOergriVEaA-GTPz-SuId8_D6hzkXy1BuZEWbfzC585_ogAuN3ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EC0OrLRjD1RMoSYlWjjjfBdRQZccqnA0764ZmCDRYk_dRea9u1q3ncTArAezvmVSzbl2gFQHJM4Jl1ALSK3fUsFNhMkX53hR77Iml3ar3yU6ZWSJBZEyB9znlNcssVqPKpsmhokDnHQ-FyzgNQCDNtjiknq8ZbqaD5ss0XtX5ad80NB0jUZ_U0E6Bt7jq7YFwzoM9wZJAxSP9q-MUfkNAhznS0In4H97sgcVEwOpMsDm-Fp8UdSUsNJh4DuWlpVeYB470LZOJ0wsyhRwe9dPkmkZfjSA3r1JllG-cY9zxnYPaGAGvXFo0NOYlL9LE2z07xlSTnC8CBz7vyB_ADBn3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7U8sAJmX_FN9X4zn1zCJhoQE-DVNHL7qB2HwymwnU4y4H79LeGW85xG6w6Bzp9sdTo-d8ehLTwyXov5VBrrLHH1TtTxgMT6JqLFbK6SgB8G9ILFz42sh2CBWuM6kCyov0R_faoP2Ic4M1zCD5LSc9Fel6blLfCgQeAIxfrpJHRB2Hr6dXyTrJaPrCsSHRXik0Mde-dJyOdNd9d-sLAmQoTGRk9cnLZ6zxpneP43gt-m0urYr-PRiKwjlFe_6wJIYHU79hDsBmRtZddvgp7mzxsi9tGHv74heFEClbrkZzTlN_FIxuBelTt51k9mre_x-a7MVq04pz_w9aLV4eyKOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/auJClQk3gcWT3bCanf1gblblejBHKpeDPn-qT4DjQkXvmfLxYEQuBaerHZjUJ2eHHfpSCHdvUnsFKElIjBhsHey94KHcyBuCVpBm5RclD7kANpK7m39mkgQNq_KdgY8WgGimIUCXBp8xc0D4kgKMyh4G8MQi9_O9EbnMzZqWvHmnc47pKrYAlxY92PMyp42L_9iRRFTe0Zruli63wD328E47wCJk9qNh1YpJjxcwzSSgi1uepXhzBGk_M0Ff7mzsApQJxcz6Kg-iHgBoKzxSc2MY8yshDnWpkEfCJAQPyO0v1-He0lO9mN1xthEj5YKtWtuduTTNih7KmIcgDWgQvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tuzHjQxqiaUx6UeMT7RZxKjp6ONZBQn2cyM469uKFsGZTPzIsCgIrFXCf_x2GwKOFq7ze-6KpyfZrJgDf2uqK-XSiX_z8bv4iOfRlN17bcKVpyHWlCbNISNZN_VuCj0SqfMNOYkzeqDWLO6opdf7GN4a2FedAchpqnecISA5lb7LpKRsQn3ktbGU5ADgr9iEyVRX-IkYgZi4AVYX_jsemAvcB4yNo7w56i_8ou_QKVO_Lq1j1nSD563cphhLslFhvgaOH5A5sfRaP50ObTHtrg4Th63mnDS-fffPgiV_XuY270PDXDnD8JlUQi_uflzks8PpTpRrWdbEBSJZJzJ1fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXxgU0Pj84wFG-FUhAMV6Yb9lAXAxMSKKKKBKPzhmWn_EEASf205iMfbZUhewpE7KLtX8T9-LhXoryfjB0QL5RSyCI6h6rA5IxweZElMD2fPAcXPD2qkTgaKChvqP0xdQxti6hy0FYiij71OsmptPxMyMTuWFxtcyG43Shc-PwVqJgZcqilsX43JQNazMKu8s-sMJXp4S03Rz2aesTufWGKRPhATPijYMvSBjwJYmA_RxEGOtuEkR4IZheoZOunKp4Z3Z3L-vH9kIg-s7tsqKkKBl6C3dIRKzY2oaSp8Ee9KysYcctF2mwwB3vDDwRNMxnw0sDoXep8QXm-9a8D-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Scg-cyfH7ZHAGPjAW7d3q0ze_xjO4FrlkbVXsXJxBQkJTByznP1WsM3Vwowta8ELXOCbyldUa_RNHUMrWIG0ZCOlSb8rRK13kExdGGhDf4EleSA5jSFKlEePqFyQZPaui-heGP1wbAX7D1cXUmYzKvnEpOmhBZgBb8rJliMVlIPdHPzbBNFse2dM6y8TmCg3ahYxdVGplZqslyQvAKqcfW-ViU45IKlGTu2X0L54F63WYXY5_gIdzxWXoFhctx4-vvjHKIsFc-0PErdLnbiIv64vgR38x_Rqr_Z4vgS82eJFkmdDf1x5kZV3lHhrub41v4w7dY7uwbpeLDmpVjs-wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvhqQySLWrJNmuXayBZnBEP4SA_15VNqVPkbjYy7lx5ZfalHyAYirPBpc79QMfv3Rja9hxqkxVuZxz_L4OqZPkdHZcKDSnMeSjiUhiXeq2CzDGiJGVX7lhrGzgnb7G2Rofqg6sFUsT29liM0zTKaW4Df7tIAYbVD-mSaxasMG5vFyf3pqjO3LosXy4iSRpMIuhIrlh8rx3TLl6rMSU19WlsDpXpMxJGMylcAp3ZsOgffFjVAz-CNui0DMA0kYNOtBQAKQTdyNDes_rrj4srMCPMKoKiGio_CYRZJipi3xNZGlvfEORH4986Y1vhilddxbPDQrSVUELcQhJ-T0Vtsgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ni-1GMjV6-zsvjbyhtS_4UkJ_B7PG44xheKeC4_TBCZQJHrUH-Fz6c2s4iyjdNnYY8hnK9Y0GuxN2RWn3MJYUSPvP-LHdG2ZBT61jF9cYy5Suq3yDcmrAqx9Ek6pXecmpwuT0cPTFgc8M_iLzfaOp3POPCVXJVogfhAKKOh-JxCK1kcmBDejuiqAd3cABES6XPwQ7-VqZrkWfcoAp98sKRYbyI2WkH-I_phS5CMxqE_GErSWf4nk6WWGBs_96AGdMQBZnuStwTej_1MogIyre-wwWIzGCSvuZLyygWtlt2UwkWybw5-KCkdbIie59UG7tiLR4oUG9mBWHnkr48R_mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCEihgxX4wMlXdStddZJlTlQi1CzlyimKaaxenC_Qyva3RlHDaM13uOeBMYYTN6xvZUMz2PIaZm7KT87mXvqlrjCiN0P__kEfpFH5lorD69IdO5QlmgJZpVDTcNUlaMXVp1qIwl5NnWYs7_Kui0Gks8EiazmfTBIgd3QWbX_uL8pqQ0LtL0-qVhhPv0LjjwQs-CNEgTnuA9PWMoUj-ZfCNx0eLjT_Ry8ylM8e5MaH0gyF4wae8N6N7EYn_Wmf6Hwpn8DD1iuaQEfCIqwOq97vDZfFIKqXJdxq_5Clwg5kNZrxVdGVriAUDfj_zzcWvH6NJFznuSBnvbrf6oxtterJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFgSbohLWoNdhghEjqPlvU57wtZ43Gn_QkcLWi6exyqEJRoGiReoQJP-AvYYg3Lq6OHS-ZJDCiHCp1MzpKsJfy06tAwCQlk_WLLfCZotCl9T2czabT7t2lt3fBeRieU7_Wn8BQMGPbm-KA53If6NgkwMbmB_EXYp1HPWZ_eSYGAZ7D06SgIkWoy2LL6xRdXx5HsWqvnmDwYrY8qtFjuoTpsg0uxaYftimqv86av8qxucagtOFut3eCZnjJFmiqpAN3AqsIaVqol4LmvJpUKIC9Igp8Q3e5aB_PkY6cBTN6PQtoewsv7ZjcVbXHVkcwkRmdYCK1tZ3ZrfCggXgT0cJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBILFUH3OHVLBht7biGrkXOR5sn1wDjo_0y8OLxqVQu2hrty-JLi3aRLTUPZT4AM91cXkXGsYem4kEBsA1MqvZ7YNtBoUzE1lrIf_pC44ptPpCanzP-kROiVhecrQJqHqmw9bT9CHxf3gLfhow4AssmrPqxF34HImb6nEXsRYLQmN32N4lDP8l3TNDK9X8A56E6DROeSlBvjIKysxTm3wmHRsZmwbyG94YTVpB6KtrcxXWxkZkQld7Lw0ezgxLo7p_LysMET3QuagKsSE2UXrgyA8r8rhD--04rKmBZ0mnlI6taGLvXj2rQgz2-IfWyFDaZ_-9Gfaqr_OcGJV6skpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dg4L8ymhLAHountvJTHPt1iYf0m56sFRNP0C2KRgW_xJCF0rlmTSMRMNmFu4tPz29hhk5FrMZLjkTTcuOsUopjTqFVT2e7FyFhx1aiAH1WZCrAzbDIX5gEVOYOoLFB-8bE3eykhxia45TWzQTIh97mKB5tw-VT6Z_JfvJMF-d5CsV2KXgpRZOeSWoN2jcpeOPmgp0_PP3742dPSAz0tPOo3i825nYfZlQ_Jxs0xkJvnLicxYoemRSOqbtWvfAjGJR6Rvdzwbj0FqZ0og_qIduWvQo-j7vKlBgJXn7H8FI4t9ffyTkCVbYgSPZUeLKGrlVdu_kYCuW0Q60Avc62Jdhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjBMflAW4JZ60aWkGg50Fv36aRtDTHhecWX8kWLq2oU18n8u3ROmEtIosQQbBanVNOfsPDjTsuMl9pjqCdnzrrpsJI2P3hm78V48l_10K1UBIZvqvGoU8UvHLQlhoCdIzDBx9UqlIGtfdeBEORkqdz61el1afnOxfv_BtK8IXibvh-DszYWm8H_idQ2Hov7B_cFWvQrwT9pup1w8KI2-nkaNOL77gf42y4R3hSk6Vf8eKzp17pFnMgZcq5ETHw4AmuB4aTXWy-z4mKyXzn2IMnDKsqB491W5x_aepCjqYDupjP7PIBxJAf6rofRRyVi60_Zwm4r1mq1yVYMDcqUg8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1Yn5LqYDfTJHEHvIxy7ABlK-G03s_0oAnghu4tEU_ebpK98mes2OdirXtYdLZhlrFE3px6ZvNex45Z9DXIjKcg4D8289Wn9VoafnY8w7MGf7uMvdWZg4ISYecB64_pRIw0W6PTYNAtBoUh6NTuFFqN56v6Z-mdVdL3LBhMMZD4fDniluNrUvGW2MPzNsO5aG4FXQer8sJZQqeBSe1z_qboqyejSMEyK0qRZGos-3GD0e36OarWsXMVodYq492ktkOymdw97_QGuXZvP0DRPWwyrqfNoMtN6XImaSU5cxzNIBqau7W_RkJMolnm6g19aYDKSjRsBFAyaTmcRtMO_kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A4qUCHR9N9cXoer7AnZU6XPYx3ebYOeP2NgiZOntxZKVLGkJm5UEQYFlGW6KGUmwmYagtMPVaqplhiUucGuVyHrs0sh1mb60QuEI_WfqQWZYvZven3kJ1SbwlFUuCxq-sah8woYF44EcoYHT-8ZVhTOrcUeUzanw_CHhbMkN3L-VQTpntLzRpDXoIfrBf8Y2aRKlHFzVLA-uYhob-Ly-BxCb1jlQAvTnffSmROkJ4x6cFx2IBH2-Y4GIrD0g_GxgX4EDr71ogpunHQoKsacctNV9rWb_TDBCzteQswmamV70cxFhtwvubxuuXjc3LEhyUJRtLyR2Dz_PZKblqqIFjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqgrX7N7c-IOsVI_H-4dNEdUTdIY3IG38fw_z4eHr8AqX3xIDnrwZNnNWsypBRU2k1J12gzKqIfAxF5qRwGwO6DkseD2DXtQry-B5J4JPLttLGhU08EGT5zRwZAj6hobsbA847_zuwPTBaIl_n0bvnlqMenWEclEH0LyH85PsaIF8GVqensExR9u038foHFh3BSnlgStblV8lGiOIEM65_Nd5YAIECOfG0pPtBstvay2g1TLTkLhiriv3QE68mCx-xLiK74UFABnvj3zPnjxiYNqCYGZPUxx8Vt8Vt2G5DplMwxxv3iC75YTSNDv_-fqmHK-SdhnxLET8A3pEjVpzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgfgBuCnKNzwfJmsR4rBYfL3CrV3r-GFjeUYPMqPKKmzId1MIXD1htsbUE1TqCQMinnCmfpZduY5oTLKrgLd1hCDI_jr37TuOIFJwf45RXFkH9NqMj2d-1SdXOiO65Uv1q1pL7UI6mjX83B25iQ6wJH8bvbRy_OYE0n3_cbJXhX-UEuP2dYi6YfhU4LFhrutIjeLQTCEfHE87Troi6Z_WDv9BRmVT008BmfFyQPHVWSxMPpK44IxNid2-xhSYB4YKNZUx19K9Hqxhi-MOYyEPUS45Sf2TYb5WOiWbEL5LXEMiIVilXEuf4z1PjVrLWqf_FVKFlTFMnz7IRC-Ds9AdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcG4qoExPTeSbhP17Dnafmskvk2nQGjlGfHi0nnYxQc3N24B5XrVN5v8EKy-X4EaKHgQn9aARNQ4LYKP_R6Dp1ge5rl5SAPwEDAJ2UGrjAQfwEnEaJKVwWq-Z4m5073YkH_8tK420XAu2Evv-9_p--v6daxkZxVBa-B2UWvfdv1joHO0uq9HOzlh6dh73mWa36Qq_lb6gyTQgVuBSdJYyQAQwMfYEkLGlj3Kq-CVa2utjzZkuUBJmS8g0xDstAADymxQO4cC7YUkiuPIbMMQ86jL8Y3lv5chPMoDraEq7NmXFa9helCbAB4oT0x-gy9_R332tKfB-7r74oEJ2rViwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlnqm5gD5if8o7TVWqHCNbDlUoZOfZ8Ddgy_-V-u0Ggbe_8OTacBE7PaiMv6l5KRK08Bs8QLE80gzZAu-8T1bfAQRKnIy_BlGWSZfef0wttdMiiwAr_5sHexgy2h8lk8NCmVw2f-75uiGV7LGxd6KgWCcZSP4yq9bVeB6pV--hBzD-TSu1IozJQ9bXTZwcDL5bdl4t3jS1udUGL71lxgZHHOGDxS3hkLVcUZvUVD0_mkxTSJU5AIiTLctkLyhUIdFW7pEM_SCxtF7HWS6hUNfBSTEThy6FC81tnS3cExnOYIw9iEIZuQk5UjR5cuaB1XcyMeLk1FrQBh49O90xNhOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSc6cOFGKOA9p3uE5UCk_qGbre_DI4UPgCCJlaRwlJSRoZ10T8qlTMqDEYr1-WaClMK6VCv1SDZuJyhPZOKzdkj5_Ak-az5RXoRHRFK_Md9xvwC3r-GytyB4U8DMU0c20HmCcirUvcekFyCtb1Y0HIbibFNrqwfO5ghUdq4x4O4b-mgeqRo-ar2Kn39K8StOouxKzccLI4FA4xV6y6GMfLYumUkM85puR9F5LzdrQKKF9gxvH5oQyufEH_Sth9zK6Iy_PT_jMdBLeGsqrjAbtkkJ1zqh6mJO_CT2lWUzivYQL_FsjLCOtCeSo2G6BJGsmDwFLdTVYNROARnOUouRJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgJWydRzhDLcpfzeRHS-4hp1WXOpe1YnUqtoUpMTN11V2ZHSFxBeM4R7DJ5fqhJ_kV59CEoZayEwpNGTwRqPh4S5pCvo9y3LNX0skoTBEYQTW83z6ewnlH7CuHNeiVPq5UQK5QgFokTFRfbNH0k4t7ehsMdH6qe28pSj43Gk715POPvw1AKbgiaptV_aa0m6VKoB4zX8k8SsJHoxLgIaEtvcIOUt9HkDaL2jRbfCnnVlzPRO7DPnWVz7Tp8NQH-Z8Tokr_XyX6GdIt4rs3ECkS4T8RwIQHcdsH-I5bjOgVv2QXNQdCMA0Q2hjY9W7bmXWZDkruOTNY-9iUOpGMlrmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdPziPM1u--0Y1FO7LuInXGliqQ2q4AxtjZC6OPTNl1J28xMocS-cWV639CNtaj_L6pENX76eKaagqD9OOqqXvEUgiZC_VwD0eHHZEiLQ28rOO3FuhaUeBslMi62RPnvLDo4DPNpe0fWU8OmHZBhBxz1xoH7OPTmH3VGFf24cwWkiqgCAXNLQehfHEFO_M_ZHlH_BK_XbaEU_NRwDovIxEUz3dxL_gEcoemshthWXQnvKTz3e_SbkQUSPIF4_OknHDjo4qhB1a7C0epqkkr16P7Qhaa_MmLmDkiebujYXk0ZuUEaHceWdvQGl1IibRlOpSW9krY7XwVybIV1a8ZruQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=UXUSYOdRiY2lOIVk9MfsM53UCUswanZJTGDFCAmaTxuFOWVc2YhTTEXo_iO0sxdwDPGKAHNvuzJFSOJh7cQ5pF_fB7Hk6wE-1QyQVczT9WHwWizI41cKtKEb_rrJLe5qC_VgH4SV5UQ_OHKl9bxQa6uaUV1Ozvmp7Z1JTkcRG6mj17_zsOjWJbsO7mehDEhjFZ3MfoBsKNlmfXkPmSZCw1nrVi_cWpC3hXKhT6XSbS18dfPjKYhygRA_tUqakJsYg4IN_9f1HPvRJivUBoAOJCbdh5ojJJuKMWsu6xiVoVbzRHRJe_AmGEdlJi0FFE6bzcqPvmgKa2aiEle8XC25Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=UXUSYOdRiY2lOIVk9MfsM53UCUswanZJTGDFCAmaTxuFOWVc2YhTTEXo_iO0sxdwDPGKAHNvuzJFSOJh7cQ5pF_fB7Hk6wE-1QyQVczT9WHwWizI41cKtKEb_rrJLe5qC_VgH4SV5UQ_OHKl9bxQa6uaUV1Ozvmp7Z1JTkcRG6mj17_zsOjWJbsO7mehDEhjFZ3MfoBsKNlmfXkPmSZCw1nrVi_cWpC3hXKhT6XSbS18dfPjKYhygRA_tUqakJsYg4IN_9f1HPvRJivUBoAOJCbdh5ojJJuKMWsu6xiVoVbzRHRJe_AmGEdlJi0FFE6bzcqPvmgKa2aiEle8XC25Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zrd7CeqQKiU3bh9hOyb7v0CRCCpt0MAjH3v6TQG6Moabh28s8zc4yR0xTqSDGiOUKjTof2c0DeVPzWkkMYF_-0i5z-FMDdPV5bXhRCfl_OVgX1DbYf6FwJxxWHXK4HFVSRLAzHCopOm_v1ILOGkv8Qcvz2CCQNCHGDa_DiskTiFJNy8_gVB6jJnG7Ebw3gJw6kZUYy9S0Jv5KAyryJmbRbCKpX1fxIQNi29v78oic8zdZ6IYkfJZ3HcxWHCyZO4Cca4Q66Mkk43ZnFRLxv8b_2KdQyglgLUIDleBRXMIdAa1zB9S4gY58ypEpen-vDAN6qm7soNY9KJBH8tvMoEGnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMkgf0p_wdexhpLhsfnCRiVSP2GbVZuSzR4x8Y0YGI3FU1JtrqMUiYMl-9NUF5tohCvMMQOScFo3ze5991F5imK5pLVzMDiKH7n9xf4Au5cRkstwgog378MkYZ-k5xVA8Dtfy2jgSaZhWbOXkCykzv3IFSvGw9m-Lyg819mIt0DX7A2q7KzhnEJrBbeUWZPsrcACmyBMcSPf0OY1Ulx8hjK-fy0X5MZgbF7Oi9hBnKH7zOrLEvd0g9wHptYHmTTQpQEidovq-sx1Y9DtF9uQfSkEdQO8R_wDG0JhKa6aKLONEUbu4tW94s4E-MFCfsUvIouZq8wfAI607rwx58N8BA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NV15HtZ3CZqxpbZxgRCiVxzwcdSKnlII9eAaVtfOh_SoRXt2ZFNHWqMTGoAK1IkiaQLYQfTFp66FG5oiPUihh3PtbKjMMcEaf2mLEvfVOBfAmKeOczzwzfj12m5GR7c85PDq3Xjg69YzJn0d-XZba2HtL_FG4qVQxgKUkojVCHfmTeR7TUO5n7CyDyJ2J90pNxWLi9VXOOYKJnmNzEpzoUC8MzT6-bVRUHPDTWB9bJP6xIZoUnxlKEjfr1NZYIqHYmcwSvyBZ1NJAeyYVoWy-EXwdT4LVu9aRWET3Snilz_gH66ODjmBwvx54OPml1O72Sr7tuLaA-FpcnEaL97htw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a95fgdiAGdDD3ipZjlmVx0j1N-1I5DVlnP11keJ-m3BVwo5qMfY32ErXEjloyZGS11qc_H2ZQk5ctpdWZ8itR81Wnz8SomHIpYNDpCTn1YUCyTrCOS4dTf-8hYyWGxaj8HXQlF7JfSYJ6Bx9ILOIcvN5XzIKmgR19wZOShTc6a_PGyPLPPjzBd67BW4-ppvus1BUwAxDU-fYytTxUMz0FhjIs0cWzTA7IgU2vLv5kSJcQ5rxqk3HOJGTIX7nyikZt8FOwhZIjbxn9784if-UsN2R-O_tHnK1dFEQ5xoG8xbcj0iwyo8ESsqgiQ3orCPyACcuYYLp1GAt4ksF0N7vvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYoT1N1TJ83NifMSu6bYp5ReMtT22knIWS2d2zuDOdvrtYwFPTySlrcStL7YYzfeGvJwIEUBNRki0MkNLNyNiagGeCNpIXlm1hp8JIwpAnE6QTSzXubBWUFp2PDBtkSTI7bL7CU-c87pRqukpuBFChy_UuKqjwnqSR2b0Au5qsNGhUEDA99Wqw9cspro5CxRSAIjV6v8yAq4sAXOJJHil4xvhOFkr369bIZZfar3uX0DS1p2C3G-1Up3wP-aV4Us41amok3wTy1tY1J_q7ZWoq_OVuN7i7nv2_T2_QQRnKUvYB2-DSf7kTXv_Xa6jeaqyV0GpzE_P4ozZz8oGpBIQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpZlO0xHH7XEhHBWTPKkm5Zhiw3Pf0vAIKwNbALIDyi5rcGpOvIEk0eSxzPMG8fMJjWx1aDVmqn73IfIySW4iInAoxQcvsUdXufJX3qCee6QaUAGVieHX6UBZWCKAMMhpB29hHr4Eu4ug4h5-SvVT8EZ7OeCw8UCQw3HZfV2g5WvfDat9ytOppkabCYK5wYeKi7u7YQHXBJqtn9t6nB5C6acGAG4g1TVwEzrUEI3GvntTdJvS_ypt_nxq7VdjOD9v9xhP2M8rDr_sI17TCdbMtYIUXEN6CQrRZEOVxGQTp3vdNQpedRVdBBh08z1myS6X4odp4iVk3qvoVGtEEu6vA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiMsQQWhrDcDuyoBdeR9a89zOt-r1Z0ulREd_YZhV-FveF25-OOlO3s5BtgF12snaxF_NDxqd2rKGfKBWMYOMTqBVhuCVINRooILPTxs7zde8i0SiJ7hPrSB3jU5Gqi4VUsckOF6hRhN7F9iao64eMCzLj8DSWL0ZT7ns9clor51ObZrXiS2SQsG3HsnzHhC1OQasAbsCrn9OhazHeR7wcuspAaHutSp1Y3DiA2KOHw2fo2BTr2BmHV7aQdcE4Zt8SB6I1JZ7DSamsO--ZK43SfhEPXeTzCLPX4_u0Ys20ksFoeobrSJ7TQ5vDLnxMeshLmHWpz6uJ3JzsjavePwmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDQCs0sdOx-Kcer_y4M0mGojTFIq7EC1qWkO6gNwYkk8t9I-OOLnSzz-SLykHGLOUFPdD47XItSdLda5YPCx3N5h2HFoiDscSoa8e7iPCkpHKbIbIfCfhxrRoOGsM251y2C699484OQT8UF5zy76xdpf3Fr7bHD6WIGNdXu4ffQVDN809nZuzQ9TN_hWJVY7QVZCsUTl1habMel7lxF0pZY6E1-srvDniTTillVHQWAxQDCDzK_m0NdAYe6lz25lpG2WuwLD5uEgPBVF4sxBwxj1y4f2QHAgog1oeRMr9-STrtqEQhUUnjfzVFspXzqf3BJ_voLbOGxxbhRMGe-Znw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7oxDSNmn9lpt6n3tGh_e1dY0ggNcmp6ZuPStH4EvnUtmx1s69Gary4ykm8QQIXCh_t5k5LMqcpSRsgeFWrYfVrSARbjF6TZLgPg1ZS2OIclrwMk43WJaW5Rxt8nA6LdQXnFtxHSf03-fuHQrjqVRM2LzYgc1hXJwPf-YMpIr3_MVMwIbMN2TOIezRqSrsO1Lt-YTy_yFUYCCdylTecGduPbRCGqCdMXAthUibuGszBp7NFt3D_u94_m0EH5FV-MCXeL6uKUDe9lrcekcOlWWqj1Hi_ZS2loffgqhP_Oq6GKteRfP8XB9lWiDT_PzNTIU4EFgM5JSEsLMWc9fikmIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCoRc4-roOOi-CjY4B7Sh1dxQmmBLv0FuTI_C_uzlPOBbgzFqoF__0TVW1_WwPJuiX82qspap1BM3ypxpw4kpVzaJvXx0wHmnbPlil9myGdXD6thEoFRDjgnrEaQ19Q8Oz3vZNd6es5KZckUBLTt7yZsXrBD7VxHZgp_EkrJsKE8p7Zqaa9iRrPRC7l4LHAKXHVb0fWJuLwPiCKS3ak7qdf9oboXqx68WUaOsHh2kLeSkcselUaoYB2H_GG0_4ECGGn9twBNGvKUaX9m1MEZH6kuni9eWivJH4nMJq-OvBGDyVIz8Fo5Yl_umiSR1l1p2H6IlzwEN77eOXOVuosJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYw7ZU5XzyFG2R0uC_ZajUQza46C62kmQrjdPgUGgSQP2la5ziGnDBDk7CXig60f2_OUZt8-OUKrNNpFaJ9Yfq-g_421dupK_emSKWmJ_Ze0365ahj5qwXIMcqmj0JQM2W65qG_SQgtRgfKopWvpzSEgcu0n4PMU8tj-c8Ache21tN-ERM4cQR_ZUY7maazMMoRodqLSQjOmCq0iLOoOGaV928IrsxbdGG8JuYRKg-5kWk5dJBBAnLVfu6yznO6qpnGRBWOaU0iXia2QOfHoO-kXrZAb5gjqV1XDOnBxGBsILUj9eN-7v0EBkLfbeHNa0_wd2rNp7UhpkyDOqbwKuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPJQpt8oGX81B34IGv2ogOnzN7ODogT6GVwkeLPDSjFBEsw-KpDF1t9MCBSJuAXmwqsk1M8aqWmcbu3VnX0yFlSdHpy6Ilzm-BJ4Pn3eLqlTBcCJmvFgckhcIz7_cQ5kyFAuMCT5dI-3yU86WOPd1bsntDYqpjwVyh4fkLKq1y7WoSCCCYvPZgehdEKXARDGQAGfk3foHjaoyNcJaW2nRgg7YzYkLh3NRAdbYOYlV7rS5fGE1yFJRsI6OtDZbAQb2hxXDjNahUgRZloDy5_yCUhViHgcvxo0nJ-c9d2TgBikUPkOr_UKzfKY8cP2RHaMA4_1u_VnUcV8Pvd6pCxvnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCsKmj5P69sfcgNzab_cagfXQ0mOnmfnbzEpT3yQI3pqp-CKfiv74Y-0iDhOroG5h3nznM2WiSdrQPUjsA5FHAtsJ1Bquyr2NqVFrC8oQROEjQveATZ7pye85vTsJKqVFpQGcLsKRUuheubzpqI4nzA7XHwP-DWBV0WokkE0F2Ysiw2yNZrmQrNN8wmX3oNYVfQANGSToG4r8OXEWowiRIXEjeX9j3Y89ox8Jy5hUlz8CQuvUbOxE-0P3QeQeWI2i9HNrmIQhfVnNHsS1PmGSQPGcWN7tR1bsL__weVUAX3Q4UYx7q1SCvpee7oFl2eGbMUYW0K5tMRsQt2qEKGlXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRuI4jBhXKNiawpHLqvN8OHoWUZITUT7uCVVgwm0KcCoNzfjeYLNTteEOwHI9WYBiQ6O7nDxgpdG2a0tEZLNM9_YSovz4A3E1SCi6QiAJyNLeQJ9lw-FQxLGud20LiHLbO_ACvAu6ord8hff3eNyBLEmGizrrgvVBN96v5b0U2lNpKRWo6kZP6LjS3TkFC5fFLQfDb4I-XkWHkYu9IQ52EBB7MWdLWkRJFoTVoDqLd1wNz3IVEWAZqJVvxYH6h4fSKYjGi_xaKXfHWdoSL5qWqXj1oquXs-DVBnukrY8qkg6WpX34k7lXF492HV6eD7MxjQoVYr0WEPUQ6k-yhFR6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is2dxtFspVs_P-qwC1AOUju2qJQ7rAJIaD_nc5RuJWbCtF4lAIwqzf80rHflBLts31KXBssOme5nvmvqFRaySfKPv9RiqI2ay5YZPoOOvdWpr2P-p1xM-a1cTFJ6usHzzvZQkVameZ0b9cQhuLldj9hrsmH0Uc23JV-bgUSz8q9uubGDW4QEsd9WPHmcpXj0AgL26wjL5oECVuYjYReZ12qFZlTBmruJIgNk6GrNWhvuB1zsXdrZv9ekMqpdtGEG0SIfty_k26N9kI822HhSyXr8ZhIFWKGBwkvurTS84m6FCGzBNKzrUF4-5EKTgtLh9M2mo8fpYUGrRkxP3Y2r7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHLF5uAyAq-fpjycW7PME3bH2Hr8cqd5WOsIMaTGoA__k7QRkWlClckXRK6vmO_7bd9Gv_ANM0lz4Zvd8Gh4lL8dAap5Ae8iNl11JBxPQ4tB0gaZvxlpEf6LORzmSqT-k3L2ZqLFrVv45qmkoHBJ88P81AiCG8e4zPd-NL77kKVLz9LpAWnPsJKYpG4UXXl9SXhGci2cM2Ch7x97wtd2sA3sOCsrQndHiq8ww4i4Fe_15R1Yq7UZEj96E8jgMpT3uiQgOicEh6zQ9IHXkKJONcFpZMabaacrP9bfkUNJhYEc8Om2Va0ejkqyq__A-A0YvLH289hLF3w2SEzro6GuIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4aTpJLV4Oty5mGAKswwyYKaUXg7LVKiKLClJEC3b6ZCyr4foKF7IN28fGgFRCBN9PqM_aRnfV5N1sAOO6hVjJzsGsYkYH2WOYPTxa1zJ27OvjuEWSgyxlq6-Inmjt0uMzMo-by4_02hBtsGRdx28-81gPD1yaH2tyumTvJ1I0La8urgTBoweuspS0Qb4PnUxnHdr9wLuyyoqi0WhOR5RRkVEqgnTHqCw4aiAdi3CknqzTrFVJNRsLv04b_GJtKFwLKb-eVt1vLFJV7Vtn53NiCI9vEQzaGoTIivU8P3XCW4jIgBRLwlq860Bq2QsGBAtr6-u-_9BIf0wtF-Ds8glQ.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
