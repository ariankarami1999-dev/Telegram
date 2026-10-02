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
<img src="https://cdn4.telesco.pe/file/mM_iCbSU3kev9xxpdCLSqktQrqH9MEaHz1s5fnTiewCoZ5v2ixrFWsS1bvaTI-_th3tQVtI12svRScHzpUyko1O2Jv36sgtZeS0-nWqOHVrkXQmug37LVc9DfHYBPoIWjFejhKVTu4nGpQbb8MY9Q8LtMyIrc8jAUZHGeosWqeOpDBGDS7EIK__qc7wKNGnCHos2vkYohaYshZ0ssJ6pxXD1-sTgqu-fjYYJGMU0jVQdghHq1aEpioRbw2CgqLJiaLhwE2tE1Pfh_4YSK_ttvw8nH_BPhkuUg-SkWUu3mjednWPmUpRaVp9L5n3GCA5ghGoHZfieeUrSpd04x9Kncw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.31M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 18:42:43</div>
<hr>

<div class="tg-post" id="msg-694878">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن چندین انفجار شدید در شهر ریاض، پایتخت عربستان سعودی خبر دادند/ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/694878" target="_blank">📅 18:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694877">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d25rLaS8CtUwnQBRfGK0Xz0XO_QxifWa09EBze_poM6mNweyDKTxds2TzIKJfXx7J_t0kyvTEZ_kTq-bsWazX89PcAO47Idr9Hevu6RImLoX1lsFUz-Z8ueEFtPW4AVLskx5_-M-yTTcALwHluL_UwUwNIBggJuXSA0gc-BLBV_dicJzLTtli0frgUF-roMBejmYXMffIAA6SBgJM-p_hk1tVSvEFxpmm7btiaXFtGMFKNXofRf7EIhcXhlTxqp96JKTcAWnyc2V5RU54fJZpiMInYwRa3MITBynT8BpZwgiuFAQYYetKhdqm_cTrvb7mBj06swdTCNlEDmXLVxqvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرویس دوره‌ای قطعات خودرو هرچند وقت یکباره؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/694877" target="_blank">📅 18:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694876">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df570e359.mp4?token=A6vO9_38HNkw43XehxpiRs6akqkc2EMB027EB2hCL9O7bSP_GH1IxVpApJ3PeULNREjS7YjRzTMFjUnvJryIESJ3j3MGeT4eOvB-_HaUkkOOh6KEc5DCCjZAFbcuNVwiXcnjajX_BOE4hM8OJxeTjZcIL4Ml1rJ5ERO69s_OH3iYPgrcOSCXPv0-AcrsnZ9timhDuYcUytUTfHDwKcf5t9kUkCcGjLQrbAbbbySjmlouqrud6XsTx09qHZM-pjMbSBIde_llmuwPA2VMQMACYd6xfp6lM4KDFr4NTscbEtMNcO8Oo1G-r8MD-imzWejYwmGLAURAU6ha_qxrcoTPGrkwe6fasGLi654col-1dqKESZcsd9U_LJK-5bU07Qnj6vlZrJ2F2wBQSf2NsC01dZAF4ko-tmT2vTi0WIfzgI7_kuUiAJzu2N-nosIEgRVw1g36HeH59eu6EPLla6hhtbD-MiIwNByugtVD-5l1V2xeu2QqgGHqfJFwzfhfFf8a0lu8ZzLLsy7yDbbWPpydDxkpdPZyS3wji6IGB2UFMaPy9PRbXLYjcw5_OxXHvUAHWQQ7Tn29O6Tw0lxwwJqrachRhK6Df2xsgOR1nsAi2dCXf1Boy9m_oKP8EaV5MKm2KNaoA3YZYd2eNkGdYqnVfGktA58_gglNoJwtASVrDV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df570e359.mp4?token=A6vO9_38HNkw43XehxpiRs6akqkc2EMB027EB2hCL9O7bSP_GH1IxVpApJ3PeULNREjS7YjRzTMFjUnvJryIESJ3j3MGeT4eOvB-_HaUkkOOh6KEc5DCCjZAFbcuNVwiXcnjajX_BOE4hM8OJxeTjZcIL4Ml1rJ5ERO69s_OH3iYPgrcOSCXPv0-AcrsnZ9timhDuYcUytUTfHDwKcf5t9kUkCcGjLQrbAbbbySjmlouqrud6XsTx09qHZM-pjMbSBIde_llmuwPA2VMQMACYd6xfp6lM4KDFr4NTscbEtMNcO8Oo1G-r8MD-imzWejYwmGLAURAU6ha_qxrcoTPGrkwe6fasGLi654col-1dqKESZcsd9U_LJK-5bU07Qnj6vlZrJ2F2wBQSf2NsC01dZAF4ko-tmT2vTi0WIfzgI7_kuUiAJzu2N-nosIEgRVw1g36HeH59eu6EPLla6hhtbD-MiIwNByugtVD-5l1V2xeu2QqgGHqfJFwzfhfFf8a0lu8ZzLLsy7yDbbWPpydDxkpdPZyS3wji6IGB2UFMaPy9PRbXLYjcw5_OxXHvUAHWQQ7Tn29O6Tw0lxwwJqrachRhK6Df2xsgOR1nsAi2dCXf1Boy9m_oKP8EaV5MKm2KNaoA3YZYd2eNkGdYqnVfGktA58_gglNoJwtASVrDV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یامین‌پور از سفر به لبنان و نقطه صفر مرزی در سالگرد شهادت سیدحسن نصرالله: مردم مقاوم لبنان، مشتاقانه درباره حضور مردم مبعوث ایران در خیابان ها سوال می‌کنند/ ما حامل هدایای چفیه و انگشتر متبرک به دست و دعای امام مجتبی خامنه‌ای برای مردم لبنان بودیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/akhbarefori/694876" target="_blank">📅 18:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694875">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
وقوع تیراندازی و درگیری مسلحانه سپاه با عناصر تروریست در راسک/ تسنیم  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/694875" target="_blank">📅 18:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694873">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
الناز شاکردوست به یک سال حبس محکوم شد
وکیل الناز شاکردوست:
🔹
حکم یک سال حبس و دو سال محرومیت از فعالیت‌های سیاسی، مجازی و هنری او به‌دلیل انتشار یک استوری درباره جان‌باختگان اتفاقات دی‌ماه تأیید شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/akhbarefori/694873" target="_blank">📅 18:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694867">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWer6rQsX4SMDc6gL3vE83a_L56aDuwrb6G0o7wSDmt1_OfMAPfgXGG7On3Y7T8WT7crCZtX3mtqlkzF6NfJlnPkiYj-0IRUEuHkb3o4seoLFmbMhKkNopoU95mFSfwPggFyPHFifX-beTfS0y6rqllfFAeZ66glM9CHCn2R2oaAeVp5iA1ZQ4k-1eOMIdsVorz5SK40Kuum37eftNKiGy_Jtz1HLV1N668GlhSQxvTIh3hKCGjE4J3x4mYPA6TfV_ur28nWmE4xYl9z-b05-Hw9UBXgvqAQuT5BxcfYHXG7pIzg-jAmWiYGu9AVJ-sqbIHVv70q3-2t_eNIETFdGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kKBRhqHzJL0vcPo-OXqvzkPYKd-fBnknK0JjtgmLDspqquniBnwEKJqfnhSv60nJz_dFS0VwbZUM24F7DTb8QytQBF_yWkHOeonqB7tTXKatVU7tR1RPKa3Me9TIUfe6ZeuwEUbGjASERfHW9zy2sFsYnjDVVpsVEywPkgsbTA86roKLx6oYUufUo0kepTNKTB5cP6jGS_Lzkcp1OuhtdgvDr7eUP0unlZ8Anrn2WHB38XmR52d-f0VEduYVYEvE0PG65tKLey0AQ3rjNr68lYlGTHPBCWNLf9gzAGK4EODxc_sI9sk2kY8MssBSrGDHRxrncEK3D1vKK-jkiEz-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KFZRH7wUmUEj8AxECvK6-PIiQSLAzU1Cc1R3t7lUP8uXpJdXGAqBsoqnXn-c5_xl5C0aoPpsXRTPxr5RMEFLidgNbL8QnWvvHNlm1GK1hyd09a5feHJFRNGEobiXuAgx_0j7kqrjInWlsqAUofgp2tVIs38hDoc5zPzDzbtwNbtDbuIMGrkWOeimY6nu7vTx2UcsvMpSruvIaAkGSWPQ0GHzNS3dPKZNt3gyk_YEryAbTab9vmRWsxi5P6y1wOVfIb2vbgJ09IS1nN6yaQ7-7jX9hRc0HGx5Q3uy5X6Dhu5pqxgKdEJn_HlIHXg-xE6mxirgJpeFSNQsMIJyI6XArw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onvb7_8U_4B9fKKsa-T83KBALGQd3mtHtSdGtIqJNcKNa2mZ7QTEdXS9tP84aph9lGPR2GeDUYArT09i8hGQmxih1DdrngQQKIdnppOZ7dq46ZqnBbm_wesswf9mwZW7cWe3rdPe9ZNLOumiCuLjqCNkEUSHw0vv_ZvaDWTrit2IPFm-fctw1KBuLKI2N2NYwH7MAl44wnx52lSWXuwDVMfiBF8-05oM6MiSxB2Bm9PBPVKYCue7sXvQKR2i_8vDVbynJPnv2LBYCTqlGB_NLIbz0j_PX1-IEVl-t7MEJrtftXMC7EEThzoNZj-eoKrtuXZUTRh2b4N69YhB7Rx9-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FMUvBo24zMh7A6FYlJyD02C81eEpqTPWAHQjONjvD1aiMqe_jGD79jfHyDW0OwAoazCoNUtwXW1BQi6tn70K1RYm4xcbolGcfQxDqUj72bJPcV8mpreaId_5jX40Vok6GRr5ZyGe8VkbIMm5in1xatQF0VR6RBAlxujwROFuiBmZyXPhVeaU6JyHm8SSwaSY-I9dET_9IqCwrX9V9cxIt7_KjkKPHEgwViTwmyTVp7DZOv3ZGviv1JhpWUbnsrPs7MYLpVl_5sdKHFJtPPSpD4H01HU0787LCsvv3JOStg24y-bJ8q0v6w8tb1ZiCE7v5w7v40ihOnJPSE2WoqnDNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNi8H-V6PQ7t0ASTdBn7e3m8EuhqNaYJcGeGlEZbfgrTN_jqGbrhljdfLC1dTrroZ5vkh4GEOSYgbamHyaKl_TkvPn06ewK1TQUkx9W-vVjCb4xsp7stfleCJ5JnKRYalVwteHxZcNWxPMxkferlKetT45Af1w1Q1Q-gyHI6O_CD3qM0vB5EsSs_aTsbJ8uM2HrbVHo7a39iSJf5ps1joWfagTv-Gjhyz9FNxWazKdONdFNwJ3jYgcs0TKruvLeIv0VpXbvrQCUzANE5rIFbgeTuaAFsrssB1Xn-Zg1qjaszxyY-FFW-DE5s2Ke9MGixCp6JHpx7McCQ7bBYTeS90A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اهمیت تغذیه در سلامت بدن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/akhbarefori/694867" target="_blank">📅 18:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694866">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d9f749cf.mp4?token=tfIeSUjYyM64qoWt81Ac0Kvt8eYA2PZ6vx3fbNGvkxX0O45iqm4goJBScNVMGtowziTQyay-PDRikWWUNz6IdpPe4d5Ghsx-r_1NFUIfLPdIN9qugswxFPom--7X9u-8QOZledBtrB2i2Zb-WzpRlrtOGmqmiX3KML_7JV9sdfJoQ0QjutY-f5h2Yv7air_cgkqEEsWbpt1G6lZ5sjLerisAvmKZTfEP8kxvA9E0xs-IdVhmByi0RbEyNYDcmwCBfyPeq3pVs9omIjRZ6CtY3eQWF-Z7ytiRelDgOQyqShIP6jZVmCXOF3zMHphKWsDOIHFidfIqanF1Eo00Yj4wr02r1BrjA7gR3p_DtV21C5B8G56Wr4Z0SdiCgmkBo_7sCfEAD8xqP4mYKKq_-i81JpLtQTp7LXtm-uDPv_DpVAlUylAg7ZtDUwl3_WttW2ntnBu-FZpzRnHa4zU0kbxj5w3cW6d27kX_2wu42GtGtLeleYuj5IrMPhhSRbg1lNKdeREtFH-Z6eBkaa0v9gDsikB1avUZCivTzBGFI4fMorIrmkh51uQD8aDKXSec5JyMSRnDC-DyJsUJEPpSPkxyFf5DqXAGCAmGqcXCS6aHK_QRdW-KHk8Z7DN8kAN2hW8IoCHoHeuBqLvi0xSCwRnCJ6JXqsq9jg5gLg4CRm_wHj4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d9f749cf.mp4?token=tfIeSUjYyM64qoWt81Ac0Kvt8eYA2PZ6vx3fbNGvkxX0O45iqm4goJBScNVMGtowziTQyay-PDRikWWUNz6IdpPe4d5Ghsx-r_1NFUIfLPdIN9qugswxFPom--7X9u-8QOZledBtrB2i2Zb-WzpRlrtOGmqmiX3KML_7JV9sdfJoQ0QjutY-f5h2Yv7air_cgkqEEsWbpt1G6lZ5sjLerisAvmKZTfEP8kxvA9E0xs-IdVhmByi0RbEyNYDcmwCBfyPeq3pVs9omIjRZ6CtY3eQWF-Z7ytiRelDgOQyqShIP6jZVmCXOF3zMHphKWsDOIHFidfIqanF1Eo00Yj4wr02r1BrjA7gR3p_DtV21C5B8G56Wr4Z0SdiCgmkBo_7sCfEAD8xqP4mYKKq_-i81JpLtQTp7LXtm-uDPv_DpVAlUylAg7ZtDUwl3_WttW2ntnBu-FZpzRnHa4zU0kbxj5w3cW6d27kX_2wu42GtGtLeleYuj5IrMPhhSRbg1lNKdeREtFH-Z6eBkaa0v9gDsikB1avUZCivTzBGFI4fMorIrmkh51uQD8aDKXSec5JyMSRnDC-DyJsUJEPpSPkxyFf5DqXAGCAmGqcXCS6aHK_QRdW-KHk8Z7DN8kAN2hW8IoCHoHeuBqLvi0xSCwRnCJ6JXqsq9jg5gLg4CRm_wHj4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور ژیلا صادقی و راحله امینیان در خانه شهید علی زنجانی، از شهدای ایرانی حزب‌الله/آرزوی فرزند شهید زنجانی: «دوست دارم آیت‌الله سید مجتبی خامنه‌ای را ببینم»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/akhbarefori/694866" target="_blank">📅 18:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694865">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd7792b6d.mp4?token=s_0ezOxy15tYrAH56L0m3ZGrrjNMJxk_qtP8HK9nAKLN9OPZ44ZOIfcFHj4neAuLbon5ckp5zxLKPj-IyYRO2nPXiLE9JYB2-hwzGDnQVoWqCj6WC1KOBzx_zaDz0F2ZRx6Se1Abtqld8iqjS4o-0FUpV5k20j2Nuck1GDDb8GNRWB19ko1-JgneE2WCgAd8cqxh8-yxUsmh0C4fkJD95P71TuJdCkTskRN4jWlkqaU4e8es3cSsV2ltfTdyNQIPvZMasMkYTD3KNEpEllzBVQAR0335Ti9kAK6peKXSLG1ZLfRQ8g6j1ONeX-KC-5eLWWh6MmdezpX_JGtRXs_dcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd7792b6d.mp4?token=s_0ezOxy15tYrAH56L0m3ZGrrjNMJxk_qtP8HK9nAKLN9OPZ44ZOIfcFHj4neAuLbon5ckp5zxLKPj-IyYRO2nPXiLE9JYB2-hwzGDnQVoWqCj6WC1KOBzx_zaDz0F2ZRx6Se1Abtqld8iqjS4o-0FUpV5k20j2Nuck1GDDb8GNRWB19ko1-JgneE2WCgAd8cqxh8-yxUsmh0C4fkJD95P71TuJdCkTskRN4jWlkqaU4e8es3cSsV2ltfTdyNQIPvZMasMkYTD3KNEpEllzBVQAR0335Ti9kAK6peKXSLG1ZLfRQ8g6j1ONeX-KC-5eLWWh6MmdezpX_JGtRXs_dcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا مدام دچار سردرد میشیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/694865" target="_blank">📅 18:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694864">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ترامپ جنایتکار:اروپا همین حالا موافقت کرده است که مقدار عظیمی از ذخایر انباشته گازوئیل خود را آزاد کند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/694864" target="_blank">📅 17:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694863">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17bbb7604.mp4?token=NfomL9bbiPR3m1-PQ5RGdYprhtcofWS70quMYka8L4azpxBkWOPc1fDu1DPanq55vw9G5u5ePFTrBg8R7OCbH5v_QVJbFZt2WySAVhqQ7IXeMerNPa6N05p7Ndh_qAnGG-0gwR6g9Utk-ZjVBiaqQEuXNJo0xKk-n6gPsiyojm8gNThQUEUiYlgq9Ejsbmwo-aZlbbNI7ur0RD1zLa_PQ-qk00gHM1Fyp4BN43wFAVNiAP1wUBaTmisooNjXbbOsxZR78isik2DYgxKMkCNQDtQN0caGMg11tiG-JBdf2qjdSlG9lVn8L-3wbRbx2cNG1BO7kvR4G4ddJoTLpqkMEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17bbb7604.mp4?token=NfomL9bbiPR3m1-PQ5RGdYprhtcofWS70quMYka8L4azpxBkWOPc1fDu1DPanq55vw9G5u5ePFTrBg8R7OCbH5v_QVJbFZt2WySAVhqQ7IXeMerNPa6N05p7Ndh_qAnGG-0gwR6g9Utk-ZjVBiaqQEuXNJo0xKk-n6gPsiyojm8gNThQUEUiYlgq9Ejsbmwo-aZlbbNI7ur0RD1zLa_PQ-qk00gHM1Fyp4BN43wFAVNiAP1wUBaTmisooNjXbbOsxZR78isik2DYgxKMkCNQDtQN0caGMg11tiG-JBdf2qjdSlG9lVn8L-3wbRbx2cNG1BO7kvR4G4ddJoTLpqkMEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی مرگبار در خاک‌سفید تهران
🔹
گزارش‌های منتشرشده حاکی از آن است که مردی پس از درخواست طلاق همسرش، خانه پدرزنش در خاک‌سفید را به آتش کشیده و در این حادثه خود او و مادر همسرش و دو همسایه جان باخته‌اند؛ همسر و برادر او نیز به‌شدت مصدوم شده‌اند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/694863" target="_blank">📅 17:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694862">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10f8148314.mp4?token=SsE4fLo7MX3mQcqoCWyVfnjuJ_tpMliWhZyy0yvM-HfgTmwk5E89ioVI-7XVv97_7HEwIqKmmRauSqrc3H102I8L85W-Mzhyy2qdloCoZzKpfDmEs_UNixmdnGavRwkv504yYmbmzOqy_quVntTjwVBsBshtPlp3ei6rakDtRhwl618IUI0IaKt2YR_Vc8_hIl_uauponaN1gjbxlx4SqT-Y_TXQOR8pWb8jwV1JV5zB1BODjDLIYwKC7qeOCOhW3y2KTBfllk1e6Kq_uX6znLxLrLmIASpf7eaH5urZ-tURLg1cMfEbwFe3hFfs9Fvw_A1Je3VaE6thmcMo9i8Z3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10f8148314.mp4?token=SsE4fLo7MX3mQcqoCWyVfnjuJ_tpMliWhZyy0yvM-HfgTmwk5E89ioVI-7XVv97_7HEwIqKmmRauSqrc3H102I8L85W-Mzhyy2qdloCoZzKpfDmEs_UNixmdnGavRwkv504yYmbmzOqy_quVntTjwVBsBshtPlp3ei6rakDtRhwl618IUI0IaKt2YR_Vc8_hIl_uauponaN1gjbxlx4SqT-Y_TXQOR8pWb8jwV1JV5zB1BODjDLIYwKC7qeOCOhW3y2KTBfllk1e6Kq_uX6znLxLrLmIASpf7eaH5urZ-tURLg1cMfEbwFe3hFfs9Fvw_A1Je3VaE6thmcMo9i8Z3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت این روزهای پایتخت اوکراین
🇺🇦
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/694862" target="_blank">📅 17:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694861">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
رویترز: آمریکا از فرانسه و آلمان خواسته است مقادیری از ذخایر اضطراری دیزل خود را آزاد کنند؛ در غیر این صورت، ممکن است با تحریم آمریکا مواجه شوند
🔹
آمریکا از اتحادیه اروپا می‌خواهد طی شش ماه آینده، ۱۲۰ میلیون بشکه دیزل را وارد بازار کند.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/694861" target="_blank">📅 17:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694860">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHiWasJHq_PyDOH_rYsKXhQhPX7uWXSUKt3O0XcrrBRzUW1tI7tF8XZdjQVtcCWtuoPukb8_v1vpC1l0dFdNQpvs8gOUJnNfuZhykqjqUOrzKj6oaq9V2ru3WdXDHklRP9xPAKG_vNMBOf79NyrVxxYRqc68LLaGEp3uNxYrEPlN28tqBOi2gvYqwy3IRRILGvkT0noBtTgMNlvWykxBXjc1F5LaSVjaNmPOEtPiYfHBA63i-xDqzcEmsleEd2MPIeCHpJV5oGFrSHANHG5jwS8KxJWBb7bQpeqR1n6vsGK0MyuYX-Hpwo8rUVJF5uQog_UlR1I7gcwmfufUsGzu2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرلشکر رضایی: واقعیت را ایران رقم می‌زند
دبیر شورای عالی امنیت ملی:
🔹
پس از شکست‌های پی‌درپی، بدترین رئیس‌جمهور تاریخ آمریکا همچنان بی‌وقفه حرف می‌زند؛ و حالا حرف‌هایش حتی از خیال‌پردازی‌های خودش هم فراتر رفته است.
🔹
می‌توانی هر روز در عالم خیال خود پیروز باشی؛ اما واقعیت را ایران رقم می‌زند؛ با مردمش، سربازانش و موشک‌هایش.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/694860" target="_blank">📅 17:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694859">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
سازمان غذا و دارو با اعلام فهرستی از محصولات آرایشی و بهداشتی از شهروندان خواست از خرید و مصرف این فرآورده‌ها خودداری کنند
شامپو:
🔹
Loreal
🔹
Moluoge Oil
🔹
SUKIN
🔹
DISAAR
ماسک و کرم مو:
🔹
Pantene
🔹
Moluoge Oil
🔹
ECHOSLINE (Ki-Power Veg Mask)
🔹
RESTOREX (Hair Mask)
روغن و سرم مو:
🔹
Pantene
🔹
Loreal
🔹
ARMAME (Keratin Argan Serum)
🔹
ENZO (Hair Serum)
🔹
LOSSOFF (Magic Complex)
روغن و سرم ماساژ سر:
🔹
Max Lady (بادام، شترمرغ، جینسینگ)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/694859" target="_blank">📅 17:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694856">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMs3va9czvvFlUe47xT9eDCiGgrGoCPzcW6aYBIIRme1H6y0FfoE4UBmm-nkccWqOh3kzDko3SEapdAbHyY7oVHERXvASVyN7YHzuJkG47BbWj4y3zV8mWzbv1M5w37KZwIEOkDCuWAC--4Jf_dz_K_LoyBtRhPUTRmvtrJ3WUPiyTrjTQfmerqdvc892DBlKu-iWQaSS1-ir5SzR5yfgNYavStUrFYiKpTwWuepCzz5QIFK6mwv-rciG-WtvN0wJRSHIZX3ja2FIhU4hXDRnMoozvCnMhhh3IirdH42SkxJPgDdPfhusqSIgH-xhdAJVB330Rj6ujGBrzy0UJ594w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFxNzd8RBmsOzJWXhOlVlA0QzhZebHI0lMA9xR19vi9-7OqFNyuQQXCZveL4JvaZTZbkCkXZ6718flHBHAlVfccimaEkVM349r77D4PG6nRC8JPSGAzesjMjrbwNPcpVjoAXH9n6SUCpnPmcIHkcQ31b7Fn46gFDhte_ZSAndxVLcDLT5_PsPxzSwurh-ogt1bN0XlCETlVJVyNpdfuVIpqdn4SzlYiZXHlRZiRXZTCVH-4PH_gEukFbm9V43ixBUi9adE-bHyHO8Y39wUuhfiAg1acbjSzNTkdmsdFXtomCJhfSrHtPQ4pFyIUamvEajP_kGdR46IPMRaCy2HjqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrHYsp0Rna6HUqEErxZWQfNrS_liXlu2EbZKzLFyOuiiwmGa8HcqkGAcoSRelbxvfZqoOWZhjayStgmnWRCsrOBPRYucjqsozgp8VkE9pPmM1YD6xLX6cwRa51RdA5o9JkiT8R2Dmstk2UY7kjE4L0s0qV6aawhV4UfwJgsQoXMmLsFfB5Lj6Hfg9w1v7UR8sUvk6mDgiWmY1V3lx-SbeM_DweVGnDxOShE_xzd6iReqPIPaFfkw_KKFVSu8L01Gp8BTYVPXKgEfDYKwLD1wN2EpPvs_3Noo1gQ0G9x3iKR2CYtCwKxvPLAPzR8ws81A_8XHnfyz13UTdhE-I_ei_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مارین‌ترافیک: پس از هدف قرار گرفتن ۴ کشتی، تردد دریایی در تنگه هرمز از نیمه‌شب پنجشنبه تقریباً متوقف شده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/694856" target="_blank">📅 17:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694855">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a843756f6.mp4?token=p_duVwYccr8JQ9otkx0R9PuGPFd7PPS-5NWbXsRhbGO1K6d4DUh_bypgnJVIXaOVOgsJPCcIot7h8IbZjJWm1aUCtUhXtmWE7qeeX-3ZrUhZt_50OeStakDa5r6GlTcxqPY4-iXgT7r0QBVjUjEbbo-wjsdVspU-ZfVk3qZZ4mbzdHiLcqsrnKAmsZkePvXiZ_PKAubYMxoh9VzsbyGzoJCca93Nkp5EOB6tuaAnkKxMbIrQcYNlmzppTbqy0RTYLXIQL5lh-q2sg8wGeTa-sGbsme_moxL-MqG-fVqAfWZn3M53Q_v14o8Jeu0DhIj9aq2RDwjhHWRfJjv-rnFTnbw_Ryd3JYNc8wG_rFp6asBffFZ2MMPs-KDjaHKvBc4cXfaiX7RrkMdJSgYCKXJOnyDt29mNFpUyT9aMvJG_eaWKNIdfbeLRlbxbD94BO2kXorMol-3bqPYtBcm3xSeDrCbqem6T6cT_rLKIV1LuHPpySRjt7XmA2gko6JLjUAXPDlc4m8ZlWnzk9mdaWa2h9nMcpLVMxAxFuVzTVFXfyBKTA4DH0mSB14a8Vf3pIRlUpfcyZFnEtKFF9ksMBwCM_PkhmJ_ARFzPf5ESfZySQrrEvrAHoc5xmTNBdzlS6Ac6LqFP_Q6BWudlovC5W594Gfpsi5UzlnloaeV8llnOK5M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a843756f6.mp4?token=p_duVwYccr8JQ9otkx0R9PuGPFd7PPS-5NWbXsRhbGO1K6d4DUh_bypgnJVIXaOVOgsJPCcIot7h8IbZjJWm1aUCtUhXtmWE7qeeX-3ZrUhZt_50OeStakDa5r6GlTcxqPY4-iXgT7r0QBVjUjEbbo-wjsdVspU-ZfVk3qZZ4mbzdHiLcqsrnKAmsZkePvXiZ_PKAubYMxoh9VzsbyGzoJCca93Nkp5EOB6tuaAnkKxMbIrQcYNlmzppTbqy0RTYLXIQL5lh-q2sg8wGeTa-sGbsme_moxL-MqG-fVqAfWZn3M53Q_v14o8Jeu0DhIj9aq2RDwjhHWRfJjv-rnFTnbw_Ryd3JYNc8wG_rFp6asBffFZ2MMPs-KDjaHKvBc4cXfaiX7RrkMdJSgYCKXJOnyDt29mNFpUyT9aMvJG_eaWKNIdfbeLRlbxbD94BO2kXorMol-3bqPYtBcm3xSeDrCbqem6T6cT_rLKIV1LuHPpySRjt7XmA2gko6JLjUAXPDlc4m8ZlWnzk9mdaWa2h9nMcpLVMxAxFuVzTVFXfyBKTA4DH0mSB14a8Vf3pIRlUpfcyZFnEtKFF9ksMBwCM_PkhmJ_ARFzPf5ESfZySQrrEvrAHoc5xmTNBdzlS6Ac6LqFP_Q6BWudlovC5W594Gfpsi5UzlnloaeV8llnOK5M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهدوی‌کیا: دوره پرولایسنس مربیگری در آلمان در یک سال برگزار می‌شود؛ در ایران ٩ روزه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/694855" target="_blank">📅 17:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694854">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cf4f9e119.mp4?token=sH9IZY10f9SHcX1iZ-WPbxSi7bOOD2pZb-J2cXpeRwSMhUzAp8DKwDbTU_aIgt1xb6P82zH04NB1J85-iAYB9WCnBrvaQm5XkYLfobH-jOS5Xe92zbrsXnFtWEaqPtpZJN4P8xDbEiH9JJoLe2nmakUB6hhcK6KM8iYBxuISShHCFujGN-MRB0Op5KoKXb4wg6BbBjzM633l0eOKMECP9x3GHIO9IsxutUbxRVww8lmea6hLbPXa0Jxj_d9JCFf_6aB4xMB4LSC17drYwvrGATbwpowN_wGqYz98BzUjxt4VvAeEQ34r1BM5SiNov-uJgtZCM0r_6IdJ6aYCrxlKwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cf4f9e119.mp4?token=sH9IZY10f9SHcX1iZ-WPbxSi7bOOD2pZb-J2cXpeRwSMhUzAp8DKwDbTU_aIgt1xb6P82zH04NB1J85-iAYB9WCnBrvaQm5XkYLfobH-jOS5Xe92zbrsXnFtWEaqPtpZJN4P8xDbEiH9JJoLe2nmakUB6hhcK6KM8iYBxuISShHCFujGN-MRB0Op5KoKXb4wg6BbBjzM633l0eOKMECP9x3GHIO9IsxutUbxRVww8lmea6hLbPXa0Jxj_d9JCFf_6aB4xMB4LSC17drYwvrGATbwpowN_wGqYz98BzUjxt4VvAeEQ34r1BM5SiNov-uJgtZCM0r_6IdJ6aYCrxlKwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناهار مجلل یک سنجاب؛ پیک‌نیک لاکچری راه انداخته!
😄
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/694854" target="_blank">📅 17:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694853">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/694853" target="_blank">📅 17:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694852">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xt76b2Jz-rOMDUEDM8YC_mdeetSR5zIgG6hm7HrTTZJaBuWZ3k7qfxeauzHB0CEhhMKygV8FmR0uOUjxbRvNnt84FhJcX1iv1Bz3S0PqK0dYp47gms2GvagG-tWifqN13i6qFYOb3Z778LbpZeSR7pBDGGqDrL-ylh2rLaIHN32uxt3VfIo6H04T5lYFp7PulqnpSpKcKjpd1UtuWNHpBTwEpFKWLWUODVNrKoWh4FhxP6LIkrnkqUZKfDi4oy_V-IWTVg4-Rv_7smxHUNjmsbC3VH4K1tWEG0ODan2x6n7zfSf7pydmJpdETo701LKD6H69jEvB9zg3fQZr1CSN9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت تتر در صرافی‌های رمزارز ایرانی به بیش از ۲۶۱ هزار تومان رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/694852" target="_blank">📅 17:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694851">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
حمله با سلاح سرد به یک روحانی در رشت
🔹
فرمانده انتظامی رشت از پیگیری ویژه پلیس برای شناسایی عامل حمله به یک روحانی خبر داد؛ حال فرد مجروح مساعد گزارش شده است.
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/694851" target="_blank">📅 17:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694850">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
انفجار جدید در تنگهٔ هرمز
شرکت اطلاعاتی امبری:
🔹
یک نفتکش با پرچم پاناما هنگام عبور از تنگهٔ هرمز «هدف اصابت یک پرتابه قرار گرفته و ستون‌هایی از دود درحال خروج از آن است»./ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/694850" target="_blank">📅 17:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694848">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a854bc709c.mp4?token=jqHoiWG4p9ofmpA6nm_nh5TC5hEwFT-2KopEHrOO0dIbpBVra8oFJ4huld8P0cl3Dabhsn63uHZRNv1cl-zPuKtqK5Jm3r-Wvr-2Fah8wLQ6YfWaGb64iSYKdJsTuBk4YuRl01qtI_Og3zuGwpAdiXWkyZr01cmtIbbN9xkTY6UApIeuxRNlaty06lLyf5Ep0IkPllW2WdFuA44sEhReM-ISo7bwXo5Nl1TCuh6IxX_tYTRUCKHdRExgkGo8yVvPLIQMQXm7-fTbj4PZfg_7f1AzDObLy0FLu08atvgsrF4vxxtAkHq7DkfqbqhuY-xKFwj5b3iugw0TZKZI5GQyYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a854bc709c.mp4?token=jqHoiWG4p9ofmpA6nm_nh5TC5hEwFT-2KopEHrOO0dIbpBVra8oFJ4huld8P0cl3Dabhsn63uHZRNv1cl-zPuKtqK5Jm3r-Wvr-2Fah8wLQ6YfWaGb64iSYKdJsTuBk4YuRl01qtI_Og3zuGwpAdiXWkyZr01cmtIbbN9xkTY6UApIeuxRNlaty06lLyf5Ep0IkPllW2WdFuA44sEhReM-ISo7bwXo5Nl1TCuh6IxX_tYTRUCKHdRExgkGo8yVvPLIQMQXm7-fTbj4PZfg_7f1AzDObLy0FLu08atvgsrF4vxxtAkHq7DkfqbqhuY-xKFwj5b3iugw0TZKZI5GQyYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قوی‌ترین قدرت فک متعلق به کدام حیوانات است؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/694848" target="_blank">📅 16:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694847">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Ey Jaan Che Khob [ GisoMusic.com ]</div>
  <div class="tg-doc-extra">Bijan Mortazavi [ GisoMusic.com ]</div>
</div>
<a href="https://t.me/akhbarefori/694847" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
بیژن مرتضوی
🎼
ای جان چه خوب
#بازصدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/694847" target="_blank">📅 16:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694846">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
اولین تصویر از «اسمیت ماچهار» خلبان ۳۸ ساله هندی که در پرواز فلای‌‌دبی با خلبان دیگر درگیر و با چاقو مصدوم شد ولی اجازه سقوط هواپیما را نداد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/694846" target="_blank">📅 16:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694845">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311e4221ee.mp4?token=v3vwvZrBBawm8lH5HBo3zcr1ur8Dx_1UWHNymOPUfCEmGH1BsOCrb7-En7Kw6TDeyP_8148HcGZgA945l977P31dZneJwOVBdZTEcw8r8cXwbAuEQTYVMMapfIQasM-Ue7RFaxDcFHD1Vvj7AXLVtrrHssqJcm5mVj8URlJoFS2lJP-weBZzotcftKS2l2BkQ3S3ZcRjMKfSUdVupPJVLDrGHK8WxqnNqpIzqIANzphZ3awEwdA3Q3N6gBclCtChQEXkSUoOZPo85rHSL6urflCGkhobsmNNLDqUoKeXff3NduFPAFSYe77_MWgyYRPLX6CdXbpGLwqCuoiEsDxSWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311e4221ee.mp4?token=v3vwvZrBBawm8lH5HBo3zcr1ur8Dx_1UWHNymOPUfCEmGH1BsOCrb7-En7Kw6TDeyP_8148HcGZgA945l977P31dZneJwOVBdZTEcw8r8cXwbAuEQTYVMMapfIQasM-Ue7RFaxDcFHD1Vvj7AXLVtrrHssqJcm5mVj8URlJoFS2lJP-weBZzotcftKS2l2BkQ3S3ZcRjMKfSUdVupPJVLDrGHK8WxqnNqpIzqIANzphZ3awEwdA3Q3N6gBclCtChQEXkSUoOZPo85rHSL6urflCGkhobsmNNLDqUoKeXff3NduFPAFSYe77_MWgyYRPLX6CdXbpGLwqCuoiEsDxSWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای اینکه بفهمید کی باید به گلتون آب بدید فقط کافیه نکاتی که داخل ویدیو گفته شده رو رعایت کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/694845" target="_blank">📅 16:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694844">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84f7ffada5.mp4?token=LD07oVyAWFYdRmS-w4GHH9TUq2XvHcQnhJVMNbkGoVXDDuIhiyyed9KD9OHQwAtFW7ZSivd2J-Vf-1AVcWZb6BjiyKglOGcT-ui-k4s34gNki3lZmhp2zWIIZfJJaUpw8akhBragixndCrlUGjLDdjglV46CsS8kXGkjIcysGIFG5KkX-dRGqdOOEFbvcQ6Lh5p2rtjjgJDal-czbKcySpBHnMU4vIOL9l5uEYD7fBCNgPKx-pupsl_0Kna0wzzeb3NzSTCwL4u8r3frOJ5siFejkL1UkjoSzN_Ux8apmOfgeTjcp4TKkHaDLdmB-zCu0NFNaQWKU1Y1r8VR56plnJ_qxeEPkBbBYWLYYO1rhqVCRr1EycQy5bM1CS74YJwZiTeXL4oMB4rdcQV8YBLFUyKVt4HwKBd24_Ok-2230nKFEwjirCyiWE-y3zEzM-X-Ja6flk07qDSWTOjuiy5loNs7P616uvQ4QjRWGIAacDbGkTbeMqRNHyoxrQc6XjYTJLOII7wp18V5dQ3-zKGFp3XL2wiCIx2ye6dOiCOTgEedUBQvpUHY26CusnEPq6MzHFmdB_8MBoe1f_dIxcM9n_71VdvbTOSbVADnY2IVAT9pSF9Ne3kqVATIQXFkuIwBOVWEn1EjddIMQxv1JnvXIhsFKQj7SgvQzrm5ZYV5KT8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84f7ffada5.mp4?token=LD07oVyAWFYdRmS-w4GHH9TUq2XvHcQnhJVMNbkGoVXDDuIhiyyed9KD9OHQwAtFW7ZSivd2J-Vf-1AVcWZb6BjiyKglOGcT-ui-k4s34gNki3lZmhp2zWIIZfJJaUpw8akhBragixndCrlUGjLDdjglV46CsS8kXGkjIcysGIFG5KkX-dRGqdOOEFbvcQ6Lh5p2rtjjgJDal-czbKcySpBHnMU4vIOL9l5uEYD7fBCNgPKx-pupsl_0Kna0wzzeb3NzSTCwL4u8r3frOJ5siFejkL1UkjoSzN_Ux8apmOfgeTjcp4TKkHaDLdmB-zCu0NFNaQWKU1Y1r8VR56plnJ_qxeEPkBbBYWLYYO1rhqVCRr1EycQy5bM1CS74YJwZiTeXL4oMB4rdcQV8YBLFUyKVt4HwKBd24_Ok-2230nKFEwjirCyiWE-y3zEzM-X-Ja6flk07qDSWTOjuiy5loNs7P616uvQ4QjRWGIAacDbGkTbeMqRNHyoxrQc6XjYTJLOII7wp18V5dQ3-zKGFp3XL2wiCIx2ye6dOiCOTgEedUBQvpUHY26CusnEPq6MzHFmdB_8MBoe1f_dIxcM9n_71VdvbTOSbVADnY2IVAT9pSF9Ne3kqVATIQXFkuIwBOVWEn1EjddIMQxv1JnvXIhsFKQj7SgvQzrm5ZYV5KT8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راحله امینیان، ضاحیه بیروت: هرجا رفتیم، اولین پیام خانواده‌های حزب‌الله سرشار از محبت به مردم ایران بود/ برخی از خانواده‌هایی که دیدیم، بین سه تا هشت و حتی ۱۱ شهید تقدیم کرده‌اند اما با این حال خستگی در چهره این خانواده‌ها دیده نمی‌شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/694844" target="_blank">📅 16:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694843">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
امام جمعه مشهد: تداوم این مقاومت، تا یکی دو ماه دیگر آمریکا را مستأصل و بیچاره خواهد کرد و در این انتخابات، حزب رئیس‌جمهوری شکست می‌خورد و شکست این حزب، خیلی از کارها را پیش خواهد برد
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/694843" target="_blank">📅 16:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694842">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a9b73139.mp4?token=lJXcvF2PkYvRJDn0a046lANYy6nP1-Cq_dcL3c-hktFdFUjEGbrf3Uu-1BEWPX6INctaoI6uTqTx6vwteD8IqEQY4_GuicEDQyoPJfgEhUbFr46uXzRsnL2QbYvQ6vjZlp-vcIRyJFC09UD_RJjw9qAiGmup1ziimqO8xzD7-qXC7UBqKg5M0HEAuGnNywt0cpYb8zmCdh7hdObDM9kZ6GNYK5U02sQBWSHuGjlpB5hOsWJBQUzZDaESUJYA4O1cnQpGqNjtjMKaQemSSudYYuCzb6AU6inL_MDKnCqIXLmlOOyZy5JICzOUNEDgZ_bucR42PNFoam5SnqpPurdkYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a9b73139.mp4?token=lJXcvF2PkYvRJDn0a046lANYy6nP1-Cq_dcL3c-hktFdFUjEGbrf3Uu-1BEWPX6INctaoI6uTqTx6vwteD8IqEQY4_GuicEDQyoPJfgEhUbFr46uXzRsnL2QbYvQ6vjZlp-vcIRyJFC09UD_RJjw9qAiGmup1ziimqO8xzD7-qXC7UBqKg5M0HEAuGnNywt0cpYb8zmCdh7hdObDM9kZ6GNYK5U02sQBWSHuGjlpB5hOsWJBQUzZDaESUJYA4O1cnQpGqNjtjMKaQemSSudYYuCzb6AU6inL_MDKnCqIXLmlOOyZy5JICzOUNEDgZ_bucR42PNFoam5SnqpPurdkYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خراتیان، کارشناس صداوسیما: تهران رو دوباره با سنگرشکن می‌زنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/694842" target="_blank">📅 16:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694841">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d1d1e36eb.mp4?token=hhoztyct2gEeWb8bHHtXGIao5jLMMzdT3NUnSXhJFNKzDhZz7nSXlgZbsL5RaT7gWkSfyIVb7BwwAiaKq4grtaW1SS01dg_BUpthCsjH6dWEKR6uvNQm9-R8--XEAP505uNds6DiRaqOvncPMCxx5qkhAgLF9LqJWo00aFQDWRvAqvacKa0ec-kvtvnM4DTFz_hXmdg957dFcT9oKbEmKIh9u9zrDAIvXEEJdlZXig-3-o6UbenYLT5Z_EUG4SQThXkgS9-leRPuIUb0uY7OZVZRVM14VWBWH_yia9pc6fHS0HjRDgNIEFXDf3t-O15hJ6Bzy8XfQlsNcDrdTX4tVYdTVxSbNbZNEHkroKrNsx0WhDh_Z8CVCfw-KWUqJdj7pqQfKNcwdFt1XxWavfVGM68CqdUfEGu63gtfdK9wRFOCqCWE6cj7nfEdlxn3CDrKvwxd4zkvV43qBf2py9Yc9yTsqc0coy_ra6GfNzJ-HHw9Uj0IPi1j-9V-YzC_oc9sa8C-IdfgWVOm_hkqVNLwM46ahBNUfMiV2RP0H8WelZD-0VTII882bKlgStPLwBXayTCnRrxKAwJ2qZNwKVr_6Gkc4XHLYqM-Zc_mkgmDrA1DCsIBwhWL_ZPrzl6fSMlVqirem7IYryBA1LTgJDPcGlnJURWKEJrHsZ6ep-MECUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d1d1e36eb.mp4?token=hhoztyct2gEeWb8bHHtXGIao5jLMMzdT3NUnSXhJFNKzDhZz7nSXlgZbsL5RaT7gWkSfyIVb7BwwAiaKq4grtaW1SS01dg_BUpthCsjH6dWEKR6uvNQm9-R8--XEAP505uNds6DiRaqOvncPMCxx5qkhAgLF9LqJWo00aFQDWRvAqvacKa0ec-kvtvnM4DTFz_hXmdg957dFcT9oKbEmKIh9u9zrDAIvXEEJdlZXig-3-o6UbenYLT5Z_EUG4SQThXkgS9-leRPuIUb0uY7OZVZRVM14VWBWH_yia9pc6fHS0HjRDgNIEFXDf3t-O15hJ6Bzy8XfQlsNcDrdTX4tVYdTVxSbNbZNEHkroKrNsx0WhDh_Z8CVCfw-KWUqJdj7pqQfKNcwdFt1XxWavfVGM68CqdUfEGu63gtfdK9wRFOCqCWE6cj7nfEdlxn3CDrKvwxd4zkvV43qBf2py9Yc9yTsqc0coy_ra6GfNzJ-HHw9Uj0IPi1j-9V-YzC_oc9sa8C-IdfgWVOm_hkqVNLwM46ahBNUfMiV2RP0H8WelZD-0VTII882bKlgStPLwBXayTCnRrxKAwJ2qZNwKVr_6Gkc4XHLYqM-Zc_mkgmDrA1DCsIBwhWL_ZPrzl6fSMlVqirem7IYryBA1LTgJDPcGlnJURWKEJrHsZ6ep-MECUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شباهت عجیب شبکه کیهانی و مغز
🧠
🌌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/694841" target="_blank">📅 16:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694840">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
وزیر اقتصادی به منظور پاسخگویی به سوالات تعدادی از نمایندگان در جلسه علنی مجازی هفته آینده مجلس حضور خواهد یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/694840" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694839">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b931f137f.mp4?token=MI0QeBa055eoNHMKypqNnOXPbsnR2OPllpDlMXBNE9iQAGALrXQj6p7FmSmA07F1FG5Q-1tkeKmzqHBL_f5QK0wKAAZ4OHGSB9q1SDWmVNnVBiJsfXcN1hEGY4PNksQrNgzVm6-Mccn3lVnVPLA1utxX_IAt2biYCZ6p0ZPcLbMjysNyVPxmPpUmpvYqQUD4uGQ_ucKuHytESU8hPv0UhqxQgn21Kyiw-pywvqXmR2tEHkrVg2ZAmy7UfaeqwfPGZhe5RnjoNltJBZqmDNFf5VAdOCtOPX8S1KbhiuWAwFia42zhom2m2xQCQJAnk_NuVPubKuwF3a0HbfJlnxlJag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b931f137f.mp4?token=MI0QeBa055eoNHMKypqNnOXPbsnR2OPllpDlMXBNE9iQAGALrXQj6p7FmSmA07F1FG5Q-1tkeKmzqHBL_f5QK0wKAAZ4OHGSB9q1SDWmVNnVBiJsfXcN1hEGY4PNksQrNgzVm6-Mccn3lVnVPLA1utxX_IAt2biYCZ6p0ZPcLbMjysNyVPxmPpUmpvYqQUD4uGQ_ucKuHytESU8hPv0UhqxQgn21Kyiw-pywvqXmR2tEHkrVg2ZAmy7UfaeqwfPGZhe5RnjoNltJBZqmDNFf5VAdOCtOPX8S1KbhiuWAwFia42zhom2m2xQCQJAnk_NuVPubKuwF3a0HbfJlnxlJag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان کوتاه و جالب از یک فرد کمال‌گرا و یک فرد عمل‌گرا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/694839" target="_blank">📅 16:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694838">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUvIbqqsBJTrX3Ai8VAYOXAVwFXoU-RCA8gIgvbW0Vsok9DdApxkgSSAxq5p54oaRqdgdcPcsPRcyPl4WeF9xDqhfdXEDbvNW3J_cPybvut_5sU4qE60eqjF-fOg0s2JW4BnD4bYnb2W3cxsfzGrtg2NZBxz0gK6DBa5c2vHL8Pr5G6nl2RVzMoSckMs_QqZJFCEZbmlYr481t-R2DN1AhMcg7I2KMYWQkVruD-SP3dd6L6qIg2silLJx-HidpWVLH1kM1fv8V-UsK-RbBcJbF4Qn5lkqE88oMnj6nRZK5xbEoinH0qgbB-1xEmWTdbqXoNmvQzdE9u0W0LJaJfIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طلا و نقره تا مس؛ همه در کاریزما
🟠
با
طرح مس کاریزما
می‌تونید بدون دردسر خرید و نگهداری فیزیکی، آنلاین روی مس سرمایه‌گذاری کنید.
✅
خرید و فروش ۲۴ ساعته
✅
امکان خرید قسطی مس
✅
دریافت وام به پشتوانه دارایی
✅
تبدیل آنی به سایر طرح‌های کاریزما
اگر به دنبال متنوع‌تر کردن سبد سرمایه‌گذاری در کنار طلا و نقره هستید، حالا می‌تونید مس کاریزما رو هم بررسی کنید.
ارزشمند؛ مس کاریزما
مشاهده طرح مس و شروع سرمایه‌گذاری
👇
خرید مس
خرید مس</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/694838" target="_blank">📅 16:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694836">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9473f5b877.mp4?token=lu4DALJjpyuJ0zYUpibkwuBw91LeQGPb9Xlp6LMp6GlYvRYXmu-KhtmfK4VKdZXMxeb7DYl1DlMJaefFdkXNMCj9TuDIACp211tkGlBDYH8-LF1r7NVKBLOScWNTdHoFjIc_8kIIyxzgqnfwmXdsszv7h672vsoaqDK5MBNqLvM1a-mqdbwJ0bT9qgOeQW_cW3Pc0x_UGh6-IYU3xS-h6U86U-XKl420wRL60jIL8zbiEayMXJ7F4zyO7yc3VLfGWhMtU0p69G-4EUqXLuIDGqpEfkR6Isk33H8kcZzHn0c4952T98EID4E_fNxnhnq9nNGdtYMj7BLJHKgXOuuMgmwSo4fUon75N3YXoTtoKXP2jRz9duCCIU-afyXyGLs_vixRPjxbw5ut7o-1BWWNwHDiR_EHYeUlNc5jNwHLKR3as3xh38pzq-QNbk0CCLlZLLQNqj6HaMf71yzfUH6dJNh48PvBed0P5I8Yplu3-n73lF-3pkSJZh2lsTwEZAUnqPGLfiUEh3uJV-3FgMV7khCrPjH02086l3iLwtfBZ6JUCpfBL2_hiL8bU0sQWcyG1LpZKzwxsGNS5PNgYi0pg7JLbqtHoQOa89r05yQU-JZXG19b5pxB5mxF2rQI2GtneI3O0hN5csN4j8UaDJxPLElYbrYxMu-ZoSDbrh6TLH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9473f5b877.mp4?token=lu4DALJjpyuJ0zYUpibkwuBw91LeQGPb9Xlp6LMp6GlYvRYXmu-KhtmfK4VKdZXMxeb7DYl1DlMJaefFdkXNMCj9TuDIACp211tkGlBDYH8-LF1r7NVKBLOScWNTdHoFjIc_8kIIyxzgqnfwmXdsszv7h672vsoaqDK5MBNqLvM1a-mqdbwJ0bT9qgOeQW_cW3Pc0x_UGh6-IYU3xS-h6U86U-XKl420wRL60jIL8zbiEayMXJ7F4zyO7yc3VLfGWhMtU0p69G-4EUqXLuIDGqpEfkR6Isk33H8kcZzHn0c4952T98EID4E_fNxnhnq9nNGdtYMj7BLJHKgXOuuMgmwSo4fUon75N3YXoTtoKXP2jRz9duCCIU-afyXyGLs_vixRPjxbw5ut7o-1BWWNwHDiR_EHYeUlNc5jNwHLKR3as3xh38pzq-QNbk0CCLlZLLQNqj6HaMf71yzfUH6dJNh48PvBed0P5I8Yplu3-n73lF-3pkSJZh2lsTwEZAUnqPGLfiUEh3uJV-3FgMV7khCrPjH02086l3iLwtfBZ6JUCpfBL2_hiL8bU0sQWcyG1LpZKzwxsGNS5PNgYi0pg7JLbqtHoQOa89r05yQU-JZXG19b5pxB5mxF2rQI2GtneI3O0hN5csN4j8UaDJxPLElYbrYxMu-ZoSDbrh6TLH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یامین‌پور از دیدار با خانواده شهید هشام عبدالله: میروم انتقام خون آقا را بگیرم
وحید یامین‌پور نوشت:
🔹
شهید هشام عبدالله، گفته بود زندگی بعد از آقا را دوست ندارد، در وصیتنامه نوشته بود: یاصاحب‌الزمان میدانی از رفتن سیدعلی سینه‌ام چقدر تنگ است و چه اشتیاقی دارم برای پیوستن به او. نوشته میروم انتقام خون آقا را بگیرم.
🔹
هشام اسم جهادی "قنبر سید علی" را برای خودش انتخاب کرده بود. ۱۰ روز بعد از شهادت آقا، هشام شهید شد و ۱۰ روز بدن ارباًاربای او روی زمین باقی ماند.
🔹
پدرش از همان اول اشک می‌ریخت. می‌گفت ما همه در همین خط شهادتیم ولی هشام زرنگتر بود.
🔹
گفت روز قبل از شهادت هشام، خبر شهادت برادرم را دادند. چند روز بعد خبر شهادت دامادم را. دیگر توان نگاه کردن به چشم‌هایش را نداشتم. حاج سعید روضه علی‌اکبر(ع) خواند. وقتی گفت "علی الدنیا بعدک العفا" انگار حرف دل پدرش را زده بود؛ حرفی برای گفتن باقی نمانده بود...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/694836" target="_blank">📅 15:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694835">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
وزیر امور خارجه پاکستان: نباید هیچ‌گونه هزینه‌ای برای عبور از تنگه هرمز دریافت شود
🔹
به‌زودی نشستی در ریاض برای کمیته دفاعی، سیاسی و راهبردی بر اساس توافق مکه برگزار خواهد شد.
🔹
بیش از ۶ کشور خواهان پیوستن به توافق مکه هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/694835" target="_blank">📅 15:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694833">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df48f7cc4c.mp4?token=aNsIHUamWi8Cl2tKEih6SnKiTWq7Rp5GVaLQUAc34o-yyomgb5TFgRuQvVgQ7hpnGIjF9mGQb-UNOHXH14TAUrmPiQ6WtVt8UhZu0slZPDpIcvElULQYRaBNRZi6H5KrjyjLpKr6PlhXna7nFUXFODvW14wf5VbBK4fwzu13vGJS1jbVnSG8lWTMcfKL2l4nwmr5tAwGgHjQ7nwPt79EAEAh0EdoJRckXJc2hP7S5XItscnIKMMQNKE0RypIUuzYwGvSdvlBHWQEi9EDqaSOpq67_ef4_N_7No7kScyoIeMNQB9bUctsX1USNGFp9wUj-bOBV-RAnxX4tctBIyTfVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df48f7cc4c.mp4?token=aNsIHUamWi8Cl2tKEih6SnKiTWq7Rp5GVaLQUAc34o-yyomgb5TFgRuQvVgQ7hpnGIjF9mGQb-UNOHXH14TAUrmPiQ6WtVt8UhZu0slZPDpIcvElULQYRaBNRZi6H5KrjyjLpKr6PlhXna7nFUXFODvW14wf5VbBK4fwzu13vGJS1jbVnSG8lWTMcfKL2l4nwmr5tAwGgHjQ7nwPt79EAEAh0EdoJRckXJc2hP7S5XItscnIKMMQNKE0RypIUuzYwGvSdvlBHWQEi9EDqaSOpq67_ef4_N_7No7kScyoIeMNQB9bUctsX1USNGFp9wUj-bOBV-RAnxX4tctBIyTfVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از عملیات صبح امروز در منطقهٔ منزل‌آب زاهدان با گروهک‌های تروریستی  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/694833" target="_blank">📅 15:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694832">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2e25f8b4d.mp4?token=ZjhmAWWYVtIYmEQkxVBaeqjJ4AHWLpbMzHVlDnP1T3rcVwrdDwN0oNKJv3H6FwOVXjnSd3z65f_HVpl1n0NKjDVErFecRGQ7Q8KMLpHm4NoRabqAj90l4XmJkLisQ8aPgI6Yuaa02tuvu6obqJWzrFCV8oD_lllanrgICaTXzYuSL8q29_djlW3S-v7p7Be7GgfOA3juOSzYZjT7BudsUQM-3HkMi9wHcHvMhEIeCi4WhF4jr7EiS8h4F1DMyjAQgledL2oFutPx84K0lApRoAajMETuGPExaF3axQD7tT6V4NoKSerR9nZhinS_yyuXBExfZh32-gw9LDOKlsyGVWKgaFksaGdNXP2uC6LhG0b43QHyc2Vng9xlwfLZmqHPQknJfP_2BihMl7T1PNBH5Ak4ZsJWBLxZQO2IMqRtOYe5t6X3tSFL2D3K2zTgh6jq528h6v5jGcyPeGhbfzzHAOK0UNbqfl5OAIyDi9NctMxEKnI5eRPdxBS4yMxpS68SerkTJg1XgYE2eq1ba-OkoAVgQxh4le8w0KIQ3yCOGsnW3kDOz1jPjgd0mAFClpPZRPDtKwF0AVfn_6tJzPzs4MetMUZmH5HyESGj8nND5DKu4QrnQVaSODq01ILrfS3NoTwiIpqbJg0fagW4sZaYP3gB0qLctjFNYFU5HKuVMrU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2e25f8b4d.mp4?token=ZjhmAWWYVtIYmEQkxVBaeqjJ4AHWLpbMzHVlDnP1T3rcVwrdDwN0oNKJv3H6FwOVXjnSd3z65f_HVpl1n0NKjDVErFecRGQ7Q8KMLpHm4NoRabqAj90l4XmJkLisQ8aPgI6Yuaa02tuvu6obqJWzrFCV8oD_lllanrgICaTXzYuSL8q29_djlW3S-v7p7Be7GgfOA3juOSzYZjT7BudsUQM-3HkMi9wHcHvMhEIeCi4WhF4jr7EiS8h4F1DMyjAQgledL2oFutPx84K0lApRoAajMETuGPExaF3axQD7tT6V4NoKSerR9nZhinS_yyuXBExfZh32-gw9LDOKlsyGVWKgaFksaGdNXP2uC6LhG0b43QHyc2Vng9xlwfLZmqHPQknJfP_2BihMl7T1PNBH5Ak4ZsJWBLxZQO2IMqRtOYe5t6X3tSFL2D3K2zTgh6jq528h6v5jGcyPeGhbfzzHAOK0UNbqfl5OAIyDi9NctMxEKnI5eRPdxBS4yMxpS68SerkTJg1XgYE2eq1ba-OkoAVgQxh4le8w0KIQ3yCOGsnW3kDOz1jPjgd0mAFClpPZRPDtKwF0AVfn_6tJzPzs4MetMUZmH5HyESGj8nND5DKu4QrnQVaSODq01ILrfS3NoTwiIpqbJg0fagW4sZaYP3gB0qLctjFNYFU5HKuVMrU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا مؤجر می‌تواند مغازه سرقفلی را تخلیه کند؟
محمدرضا مهربان، کارشناس حقوقی:
🔹
خریدار سرقفلی مالک ملک نیست و «حق کسب و پیشه» نیز در تمامی قراردادهای بعد از سال ۱۳۷۶ کلاً لغو شده است./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/694832" target="_blank">📅 15:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694831">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
بارش باران در تهران از بعدازظهر امروز
🔹
هواشناسی تهران از بعدازظهر امروز تا اواخر وقت شنبه، رگبار و رعدوبرق، وزش باد شدید و در مناطق مستعد احتمال تگرگ را پیش‌بینی کرد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/694831" target="_blank">📅 15:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694830">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0daf03b707.mp4?token=CR72ggCYpLQx0Xm5g0FCLrmPqRZWntWK5BLkJPVpvp0TY2bQnezFXwXW-TzW6GUNBdgqyo4E3b5cRhdQp0NvI1S6MyDP67e3maqxnTjNQlfYE5bc1Qlc2wviKLKNA_3K-DhMPOLJ8Yz8CScnlwJYpt4Z1mkyeTr9Zg3i5psy72zIURMefeFm9LVtnxYRon15JrRX2WveS65aW2WR7sDpuclXNQg3Ka2PAkKCr_4jNUZij4MCq-SM4ALx7SrbHLWxRJXfgwm48DFuHBnORj_9g4giBmcyGxKvSK3XTXod2jxVNOYTFJN1PhWl0Zqx6SYXiiuQZ5P19_cmT0lZgmrqcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0daf03b707.mp4?token=CR72ggCYpLQx0Xm5g0FCLrmPqRZWntWK5BLkJPVpvp0TY2bQnezFXwXW-TzW6GUNBdgqyo4E3b5cRhdQp0NvI1S6MyDP67e3maqxnTjNQlfYE5bc1Qlc2wviKLKNA_3K-DhMPOLJ8Yz8CScnlwJYpt4Z1mkyeTr9Zg3i5psy72zIURMefeFm9LVtnxYRon15JrRX2WveS65aW2WR7sDpuclXNQg3Ka2PAkKCr_4jNUZij4MCq-SM4ALx7SrbHLWxRJXfgwm48DFuHBnORj_9g4giBmcyGxKvSK3XTXod2jxVNOYTFJN1PhWl0Zqx6SYXiiuQZ5P19_cmT0lZgmrqcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ماهی‌ مرکب فوق‌العاده‌ عجیب با چهره شبیه به انسان!
🦑
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/694830" target="_blank">📅 15:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694829">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
تولید پتروشیمی امیرکبیر در سه‌ماهه دوم ۷۶ درصد رشد کرد
🔹
حسام خوشبین‌فر‌ مدیرعامل پتروشیمی امیرکبیر از تولید ۱۴۶ هزار و ۶۶ تن محصول در نیمه نخست سال ۱۴۰۵ خبر داد و گفت: تولید شرکت در سه‌ماهه دوم با رشد ۷۶ درصدی نسبت به سه‌ماهه نخست، از ۵۲ هزار و ۸۴۸ تن به ۹۳ هزار و ۲۱۸ تن رسید. تولید شهریورماه نیز ۴۳ هزار و ۹۰۵ تن ثبت شد.
🔹
وی با اشاره به موجودی ۵۳ هزار و ۹۴۹ تنی ابتدای سال اظهار کرد: این موجودی در کنار تولید جاری، به استمرار عرضه محصولات در ماه‌های ابتدایی سال کمک کرد؛ چرا که محدودیت‌های ناشی از شرایط جنگی و اختلال در زنجیره تأمین، تولید سه‌ماهه نخست را تحت تأثیر قرار داده بود. فروش شرکت نیز در سه‌ماهه دوم با رشد ۳۳ درصدی به ۸۶ هزار و ۶۴۸ تن رسید.
🔹
مدیرعامل پتروشیمی امیرکبیر تأکید کرد: در ماه‌های اخیر، شرایط عملیاتی شرکت به وضعیت نسبتاً باثبات‌تری رسیده و با افزایش سهم تولید جاری در تأمین فروش، اتکا به موجودی ابتدای دوره کاهش یافته است. تثبیت روند تولید و فروش، حفظ پایداری عملیات، مدیریت منابع و تقویت زنجیره تأمین، محور برنامه‌های شرکت در ادامه سال است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/694829" target="_blank">📅 15:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694828">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
نیما مرادی؛ ملوان ایرانی که در حمله اوکراین به کشتی آنا به شهادت رسید / فارس پلاس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/694828" target="_blank">📅 15:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694827">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f31925287.mp4?token=ZrFeAV2twsnMsgd7UlFE-oOUHZh3wa8bPXsky1BFVhjBCPv2GIkTN1BPGjoBPG16TjnD2EuPPW3NshLzfjDaCogn6_RQcqB1tzNbYEEa5BeaC5j2kLi_DAZrGJK8klxKB_IeKBRLcVhIboAWXNvXBArbWm1DVaEdnIUmzu8JyZQFMYB8GhkR5XUBsyTTFMLgI8tYIwu6qPbMDq5it5ahSU73R2BGo53HFR7aDAarJmQhoBtQmNnVQPZZ3ihRSAIAEwNpW7C_CXiOdbxH5WbvixarE-wkuUEQe5QSREQjdWjujXKGM1HJCSEG8ewxF8gpJJllSNhb2Ht2ip381hR_KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f31925287.mp4?token=ZrFeAV2twsnMsgd7UlFE-oOUHZh3wa8bPXsky1BFVhjBCPv2GIkTN1BPGjoBPG16TjnD2EuPPW3NshLzfjDaCogn6_RQcqB1tzNbYEEa5BeaC5j2kLi_DAZrGJK8klxKB_IeKBRLcVhIboAWXNvXBArbWm1DVaEdnIUmzu8JyZQFMYB8GhkR5XUBsyTTFMLgI8tYIwu6qPbMDq5it5ahSU73R2BGo53HFR7aDAarJmQhoBtQmNnVQPZZ3ihRSAIAEwNpW7C_CXiOdbxH5WbvixarE-wkuUEQe5QSREQjdWjujXKGM1HJCSEG8ewxF8gpJJllSNhb2Ht2ip381hR_KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این وب‌سایت میتواند برای شروع یادگیری موضوعاتی مانند برنامه‌نویسی، هوش مصنوعی و سایر مهارت‌ها کاربردی باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/694827" target="_blank">📅 15:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694826">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ff295b82.mp4?token=JlNT1ycNkuQee9r9co1_nQ0FWULPQ_8bw_JVFBvAXdUn1f7VFdAvxoCQ3okbWNzPVIfikb50170o1dGO-Ad-aAJrnPb_KvmD3wyR1sBvlaC5yyum6ik7zP729f0c0SWz6cLtb6hYMofUdbA2_W4zBhSSvMmvcTt3z6fsbLfYL2Rw7sLscdr1m2z8oKLMLm6C-Pg9XVtzNZf10ufPOU-5wqGtrd6KfWdmHk5bS-RJq_II-cosg8pdcY0hLztSFyXwKkmJW130nUF1v2yBc4pB7OBvJNQqRxApocYIZT4hqPr4vpVZwva6pREr7pBh_r9UbD98w35FG8rNqGgov3LAJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ff295b82.mp4?token=JlNT1ycNkuQee9r9co1_nQ0FWULPQ_8bw_JVFBvAXdUn1f7VFdAvxoCQ3okbWNzPVIfikb50170o1dGO-Ad-aAJrnPb_KvmD3wyR1sBvlaC5yyum6ik7zP729f0c0SWz6cLtb6hYMofUdbA2_W4zBhSSvMmvcTt3z6fsbLfYL2Rw7sLscdr1m2z8oKLMLm6C-Pg9XVtzNZf10ufPOU-5wqGtrd6KfWdmHk5bS-RJq_II-cosg8pdcY0hLztSFyXwKkmJW130nUF1v2yBc4pB7OBvJNQqRxApocYIZT4hqPr4vpVZwva6pREr7pBh_r9UbD98w35FG8rNqGgov3LAJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دکتر یارقلی در برنامه نزدیکتر: گرم، سرد، خشک یا تر؛ مزاج آدم‌ها فقط به بدنشان نیست، به حال‌وهوای زندگی‌شان هم گره خورده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/694826" target="_blank">📅 15:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694825">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
سردار قاآنی: باید کمربند دفاع را از افغانستان تا یمن و از ایران تا غزه و لبنان در سراسر جهان اسلام، محکم کنیم
🔹
اگرچه شرایط دشوار است اما به حول و قوه الهی حرکت جبهه مقاومت رو به جلوست. امروز شاهد وحدت ساحات در جبهه مقاومت هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/694825" target="_blank">📅 15:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694824">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2887e453a.mp4?token=ecLiTlS6KzeR45Jx_RhZCLBUt2t2B4fHX8o6U3G0VoLXkSMm8PjP7gbnddve5l3tP2BF5Lxpg074Goo9L5PtTnZhrVwL7moceevuq8HvcSoS0zc5RRUHwhSUITeFsKNFQLrtjhv0v4pGCqaaVXnp2OsQ_nU_Iz4EyArDc3jeS7qd1PEL-xaUwwPXwFGemzQYaZ4DaQDOZx8r4Xxj0Frf6e5jJE1Cb-zEA75CMnO7e2B02Vt6GjZOqKFrEiLgCsnxvjpLCIs1i5jv-_rpPoQvn-a5YNV8XzkS8jxLlaq0Z83wQDD30_qKWfz7DznneJeRbORn1Qe1EOZ94cbeA4Mqqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2887e453a.mp4?token=ecLiTlS6KzeR45Jx_RhZCLBUt2t2B4fHX8o6U3G0VoLXkSMm8PjP7gbnddve5l3tP2BF5Lxpg074Goo9L5PtTnZhrVwL7moceevuq8HvcSoS0zc5RRUHwhSUITeFsKNFQLrtjhv0v4pGCqaaVXnp2OsQ_nU_Iz4EyArDc3jeS7qd1PEL-xaUwwPXwFGemzQYaZ4DaQDOZx8r4Xxj0Frf6e5jJE1Cb-zEA75CMnO7e2B02Vt6GjZOqKFrEiLgCsnxvjpLCIs1i5jv-_rpPoQvn-a5YNV8XzkS8jxLlaq0Z83wQDD30_qKWfz7DznneJeRbORn1Qe1EOZ94cbeA4Mqqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی از گران‌ترین و کمیاب‌ترین کیف‌های جواهرنشان جهان را شاهد هستیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/694824" target="_blank">📅 15:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694823">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teEYIE_oUhUaHVwlukBLRyQA1931WLHfyWqs9jirPsiaqpPOMBqmw2J9Uofhs5yhM9pWJdggvIXhJok0xcbFli0coxMMBOYxVzwvrggwO4B0xb21CmtKBKklfjQCbhWqP7kY2nZT0pApxgiQufT3HVrHXGEBVT9vgf9GMhSTcYtUe1BNahsZK3KkcEoaR9guvyiLGNgq6WBkLldq5ZlLckiToj-a5xyBQnsPRmX7Pb9EBCudhCjtBaKsUiRL1oWdUFLmw1v0ySj0AyE61z8YvkRodjklplwaQBPhhXj3h38_U9ao4YLEuIGRXJvdn0wbHLj_mWkB1aOjjoKpyExyIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زاکانی: همه وظیفه داریم برای حل مسائل کشور به دولت کمک کنیم؛ امروز نه وقت رقابت انتخاباتی است و نه مملکت به خروس جنگی نیاز دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/694823" target="_blank">📅 14:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694822">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d23dd6ae77.mp4?token=TY0Ikqhl_QL7Ty2cI527nleh9RIP8_LhSfHCFmTUJFjCd3a5SDvOva4Qk7JAOPXEQqr1CwvE0aS7EblV-VZRJKVTSy7r7bKCkxG2CJRMNPtzHzwclk5oqnzIP5UfjUg7n6Pdt8xVWP7XdrsAAaGPOumGHI840ccwNfFEiXLfa3k5EAmZ43JR2LljXtVtPT5oBC52JLWG5alUUtmWgbl8y5g5SfFrpJVztmneqidMiyZq68oyXne2bYiK4Tkuo9x6AY5SwbjQCUKAjLmixh8OM_ZdYlxOL1tjCDJx_pflviVZ2OrMkTFLee5Mb-ki2IL5VsFpsNATb6ccVMkzC0M1EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d23dd6ae77.mp4?token=TY0Ikqhl_QL7Ty2cI527nleh9RIP8_LhSfHCFmTUJFjCd3a5SDvOva4Qk7JAOPXEQqr1CwvE0aS7EblV-VZRJKVTSy7r7bKCkxG2CJRMNPtzHzwclk5oqnzIP5UfjUg7n6Pdt8xVWP7XdrsAAaGPOumGHI840ccwNfFEiXLfa3k5EAmZ43JR2LljXtVtPT5oBC52JLWG5alUUtmWgbl8y5g5SfFrpJVztmneqidMiyZq68oyXne2bYiK4Tkuo9x6AY5SwbjQCUKAjLmixh8OM_ZdYlxOL1tjCDJx_pflviVZ2OrMkTFLee5Mb-ki2IL5VsFpsNATb6ccVMkzC0M1EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دماوندِ باشکوه
🇮🇷
🔹
خلبان ارشیا جمال‌پور، مهرماه ۱۴۰۵
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/694822" target="_blank">📅 14:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694821">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYmZakOyp4whiqa8BvZ-v_zmwWwgzpjKYtwnP-LgqUawWB_QMgP4AsVuuMm7jij8UCa6CRYOZV0nqiqos1U5fMhmOOw0GNQMSbawxRR09Z528FAMkg1HCuZW57-UM5E15KQZhGDfCEFBwE5yg-j2c-a131JIpRfC55IsNR_YXKF8e6UG4IXOjSojjzQIwmomJDxlV_MK_2-1cHUQDG39Gix49JCeDIAUuc4dg_wGsGWYOMK1PZlXRgxnSaNGOexNhHel3rAYCLWZNss-QIHFKCCl4_76LkrpHHomSxrp3aj99aitXaDVJR5d7IKy_qMB3bbCq6JX4jH1pwr17RqobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریستیانو رونالدو در پی خداحافظی از تیم ملی: یه زمانی، همه مردم پرتغال رو در جریان حقیقت و دلیل واقعی رفتنم از تیم ملی می‌ذارم؛ تیمی که همیشه برایش همه توانم رو گذاشتم و از هیچ چیزی کم نذاشتم. فعلاً فقط می‌خوام برای پرتغال و همه هم‌تیمی‌هام آرزوی موفقیت…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/694821" target="_blank">📅 14:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694820">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
در پی انفجار یک بمب کنارجاده ای در یکی از جاده های استان سیستان و بلوچستان، یکی از نیروهای مدافع امنیت به شهادت رسید
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/694820" target="_blank">📅 14:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694816">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3f76a5f0b.mp4?token=qtJuSCNBpQx5YMOZYT5EPKXisslKrY3M5e1r0g5FBXL5Kifda14n57gpj-lU5XfQ8PBIp0oXxySr4bzGX2phRH7K9ccTA-VfaR_3thf28HAFYerEBUrDcn5GHxY0tmZRAcJjDqCUxg5aVmpqZE22bGYnQwiLSL1CxilYX48tLKyA6syA5h0-GF278VpDWZWyhCa4M0wINcZ3ajeP5ECnp2UyKJqjlgXZSpjnB8r680JnCvtMKfDJhHjC05eWp2DCQ-h2pABh06No9TloSiM4Qmdm2oBvgxd0IDare--Px1c56G1xzqXJC7PxsGO3ZzT6OVGN6JOv_y3aWDPFjKgjFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3f76a5f0b.mp4?token=qtJuSCNBpQx5YMOZYT5EPKXisslKrY3M5e1r0g5FBXL5Kifda14n57gpj-lU5XfQ8PBIp0oXxySr4bzGX2phRH7K9ccTA-VfaR_3thf28HAFYerEBUrDcn5GHxY0tmZRAcJjDqCUxg5aVmpqZE22bGYnQwiLSL1CxilYX48tLKyA6syA5h0-GF278VpDWZWyhCa4M0wINcZ3ajeP5ECnp2UyKJqjlgXZSpjnB8r680JnCvtMKfDJhHjC05eWp2DCQ-h2pABh06No9TloSiM4Qmdm2oBvgxd0IDare--Px1c56G1xzqXJC7PxsGO3ZzT6OVGN6JOv_y3aWDPFjKgjFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی از مدل ویرایش تصویر Ideogram ۴.۵
🔹
این مدل با هدف حفظ کیفیت در ویرایش‌های چندمرحله‌ای و جلوگیری از تجمع خطا معرفی شده و با رزولوشن بومی 2K و هزینه ۰.۸ تا ۲۲ سنت برای هر تصویر عرضه می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/694816" target="_blank">📅 14:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694815">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
طبق پیگیری‌ها حاج آقای قرائتی در سلامت کامل هستند و شایعات امروز پیرامون ایشان تکذیب می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/694815" target="_blank">📅 14:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694814">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
هشدار سازمان ملل: قیمت جهانی مواد غذایی در سپتامبر به نزدیک بالاترین سطح چهار سال اخیر رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/694814" target="_blank">📅 14:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694810">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2320c82e60.mp4?token=CaNUGHZEz_-UQYzTluwZelE3XCg82D1O8xPFmmjbNfOWQy2TZwKhGi-tm7kCzFdfB5-CnCyJS8JS9NFrbzjU-llp_Cbc-6JOKYwpYMeaWVQvGVI6f6Uz-9tVtFbqdec3Id65fLq0kBcffnxjk_VPABsDcMeSkY7Z0FmzpdH-ZclhKlb1dFxFH4RSU1-mOcSj__PRmZAY1jT7LKPzSMyCo6oqMOsLaYiI0YhkVU2XBtiBzepBoou44_LmX-vdz1Igt5iZXmMXODKWkomBONKIfVRoqcV8CmhxTzInDdrG6Yq2TbVlDTX4UsHKeR3JqqxN63uRRGhfntL4tAY_2ar4IkSYMZM8gnUcDTw3YJi0mgPVmDsaWqNg11fMaTEluiRi48acxA123wxUhgjPzXJ6qv2fKypuQdu6uCBhldN4fHk18LNuQyCunHvk9wcG2fPavReYtUieYvz6E0JoDflkpziLYovD58eBcT0CmJZe7XLwTjoTtlc6semlDL5bBiJss90BpibphSYKMfIxy6NjKacQZqarH5L37a6WmW9KiS9AWpp5fcnyKZMCHhs_VuUD25QsQWEFmn35MyvjUKeUst_3zfjXB74a4sJWSVQxRafIx2bgW8Memmma-pokUsAe8SpCRYtVePDHYPvkMpCNjTyOYlQTmlWFIJsRDZ8qO-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2320c82e60.mp4?token=CaNUGHZEz_-UQYzTluwZelE3XCg82D1O8xPFmmjbNfOWQy2TZwKhGi-tm7kCzFdfB5-CnCyJS8JS9NFrbzjU-llp_Cbc-6JOKYwpYMeaWVQvGVI6f6Uz-9tVtFbqdec3Id65fLq0kBcffnxjk_VPABsDcMeSkY7Z0FmzpdH-ZclhKlb1dFxFH4RSU1-mOcSj__PRmZAY1jT7LKPzSMyCo6oqMOsLaYiI0YhkVU2XBtiBzepBoou44_LmX-vdz1Igt5iZXmMXODKWkomBONKIfVRoqcV8CmhxTzInDdrG6Yq2TbVlDTX4UsHKeR3JqqxN63uRRGhfntL4tAY_2ar4IkSYMZM8gnUcDTw3YJi0mgPVmDsaWqNg11fMaTEluiRi48acxA123wxUhgjPzXJ6qv2fKypuQdu6uCBhldN4fHk18LNuQyCunHvk9wcG2fPavReYtUieYvz6E0JoDflkpziLYovD58eBcT0CmJZe7XLwTjoTtlc6semlDL5bBiJss90BpibphSYKMfIxy6NjKacQZqarH5L37a6WmW9KiS9AWpp5fcnyKZMCHhs_VuUD25QsQWEFmn35MyvjUKeUst_3zfjXB74a4sJWSVQxRafIx2bgW8Memmma-pokUsAe8SpCRYtVePDHYPvkMpCNjTyOYlQTmlWFIJsRDZ8qO-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون بارش باران در تالش و انزلی
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/694810" target="_blank">📅 14:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694809">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enUEQM2pXrH3PgMqMRhv8dINYWVTk2f7gHYDpVjLvf4dcXG789xHZkB6gSFNtcesaiqabY5qFonprLqSil5OvJuQ46qqGejQOmvyEHPBqHsoLNq0MGg6B8HlpayC-wG1Lu_MWW3njiP5kGu995f1NiJtl6lR0I8gUXckeBTI7wUL-BgQbwxxy9gZfXf_E0ieJcw-M-8JX_jSjQgDsN1t-M2js8e1O907V21YlvvV84T-CRqI2QROe6If11GBfCT5grPeAAxZUKVFSpWqupNc_BKyMx0RN3q3539IqZtx4VFGVssWyY4lnOXLlEDyGhIL_j6u6Kq7xfeEVsgR_0vUJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایتن لوینز، خبرنگار آمریکایی: حوثی‌ها ممکن است واقعاً عدن را تصرف کنند و دولت یمنِ مورد حمایت عربستان سعودی را به‌طور کامل شکست دهند. اگر این اتفاق رخ دهد، ایران عربستان سعودی را محاصره خواهد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/694809" target="_blank">📅 14:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694808">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30be1d248f.mp4?token=i9LxZ89KxGVSlYMljdRgJ6NpdA32rH6u3Y0eppwg22fb61OywT2SodaGHQ2mSPWYGZU-763D17Ao4QCQzl9qutOkh5NZrYa5ahw-SDRPnbe1K_V0TK3TKXBK1U3G4ohMW_Supg3SOS0xTayjRU3Plz0JNcD6TqMrVXGFTgJnHnf3n1lSnrtrybWkvxEOxdvumRO55dVyaVo84TjBKFIGCklKB6AtEt-3WloIAkgWd4IeZrvU7yhzKPE-OVfQH8OnHALJNJsZ5aYY7mn2DdLY45uF8nYf98zo-Q9eLNuBS1lKopl9_bHHw-mFwRTtFAtX99fvdzYgRYmU01F6Mx91_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30be1d248f.mp4?token=i9LxZ89KxGVSlYMljdRgJ6NpdA32rH6u3Y0eppwg22fb61OywT2SodaGHQ2mSPWYGZU-763D17Ao4QCQzl9qutOkh5NZrYa5ahw-SDRPnbe1K_V0TK3TKXBK1U3G4ohMW_Supg3SOS0xTayjRU3Plz0JNcD6TqMrVXGFTgJnHnf3n1lSnrtrybWkvxEOxdvumRO55dVyaVo84TjBKFIGCklKB6AtEt-3WloIAkgWd4IeZrvU7yhzKPE-OVfQH8OnHALJNJsZ5aYY7mn2DdLY45uF8nYf98zo-Q9eLNuBS1lKopl9_bHHw-mFwRTtFAtX99fvdzYgRYmU01F6Mx91_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه‌ای که لایی‌کشی، راننده را غافلگیر کرد و به یک سانحه تلخ ختم شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/694808" target="_blank">📅 14:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694807">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/949eda02ea.mp4?token=Wd2DJ8i-mHxHMKGecgNIOP-fEuXcrUI3KL4tMvpcsupXAx3HbQrI0_hrSDOr3EjlFSXVpE60lNrvZStkBZ9GTUFnRTTbRTwrP5bNRnRckOQz3YGGWKLQAu5WfaFwhqFQlRKkxbJSGW2n5q3nLoef9VDbrx8TT8JjPgqJNwttNhhOZ58AHGij4TApyNwD2FoqkxNjxSb3j8bPoCWTW_jl8HHD8PAFK_DLrvgQ-_m_L08h7xXZ39U4qJnq44iQQYUcfHFDfKZhn_BphWRBPEipRajlTAPCN6Lnv1Ew6IECDujtqTyzU-QqnhkiSPqfTuqjdpg4mRdcntxCgelZm4gOyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/949eda02ea.mp4?token=Wd2DJ8i-mHxHMKGecgNIOP-fEuXcrUI3KL4tMvpcsupXAx3HbQrI0_hrSDOr3EjlFSXVpE60lNrvZStkBZ9GTUFnRTTbRTwrP5bNRnRckOQz3YGGWKLQAu5WfaFwhqFQlRKkxbJSGW2n5q3nLoef9VDbrx8TT8JjPgqJNwttNhhOZ58AHGij4TApyNwD2FoqkxNjxSb3j8bPoCWTW_jl8HHD8PAFK_DLrvgQ-_m_L08h7xXZ39U4qJnq44iQQYUcfHFDfKZhn_BphWRBPEipRajlTAPCN6Lnv1Ew6IECDujtqTyzU-QqnhkiSPqfTuqjdpg4mRdcntxCgelZm4gOyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«حماس؟ نه نه خمینی»
🔹
ثبت لحظه ماندگار از عملیات وعده صادق ۲ - دهم مهرماه ۱۴۰۳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/694807" target="_blank">📅 14:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694806">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d07df237.mp4?token=vI3v2M-msrhwQRjJjC7GqmqWythQnkPN6Rt3wyHwCVyeH60RbLL0cSnigm8A3Q5O_GGpvmiZDq2hZ9Kx7U6sJ0WXMSjEhh6GQ4E-H7VF-IAhOWCmZ3UPu7e8LpEgtRn-6G0u_LPmsqq-1RM5zlDenkMBSWcvKrVeblK8cjZd09U2Nin1hUzo7i23hId0OejkLUd89M3eCOcklNT8IgBjWXZr49gnkNsgG_eebyoNNiTLRQrb871gSYI90_l6sW3YuEjkWGfvRbW1Jlu-nYv7vfPXZjdROJEM2vOgxVjWnCtPm-Nu30b8yyG1eKS33RJhOPnA0PBGJLnyVcuYz-mYdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d07df237.mp4?token=vI3v2M-msrhwQRjJjC7GqmqWythQnkPN6Rt3wyHwCVyeH60RbLL0cSnigm8A3Q5O_GGpvmiZDq2hZ9Kx7U6sJ0WXMSjEhh6GQ4E-H7VF-IAhOWCmZ3UPu7e8LpEgtRn-6G0u_LPmsqq-1RM5zlDenkMBSWcvKrVeblK8cjZd09U2Nin1hUzo7i23hId0OejkLUd89M3eCOcklNT8IgBjWXZr49gnkNsgG_eebyoNNiTLRQrb871gSYI90_l6sW3YuEjkWGfvRbW1Jlu-nYv7vfPXZjdROJEM2vOgxVjWnCtPm-Nu30b8yyG1eKS33RJhOPnA0PBGJLnyVcuYz-mYdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط پل‌عابر پیاده در پردیس بر اثر برخورد خودرو کشنده
رئیس اداره راهداری و حمل‌ونقل عمومی رودهن و پردیس:
🔹
صبح امروز یک دستگاه کشنده از شرق به غرب محور قدیم جاجرود در حرکت بود که به دلیل خواب‌آلودگی راننده و نبستن جک، با پل‌عابر پیاده محدوده خرمدشت برخورد کرد و پل سقوط کرد.
🔹
هم‌اکنون تردد در این مسیر به‌سهولت در جریان است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/694806" target="_blank">📅 13:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694805">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ایلان ماسک برای دومین بار: اینستاگرام فقط برای دخترهاست، اگه پسرید باید اینستاگرامتون رو پاک کنید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/694805" target="_blank">📅 13:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694804">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
امام‌جمعه موقت هرمز: تجاوز از خاک کشورهای منطقه، اروپا را هم ناامن می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/694804" target="_blank">📅 13:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694803">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fcd2152fc.mp4?token=gD4TOJr6DX04cyOjzqIOnPfmh41bPEvxkTBbKjJwVYtb8DzszTk086VPc9N-sztR4RCzPuuJvdUnoUpbMKYKqWZ3jDWtOSknUNor9aArDdmDAx-9YhjqZYKyen9coWMVkvKb8sWuquzqrGBA978UPwDwBa-TG6-KiVJ5nmlPsAvjtmFB9RUh8zr-Z5IFo1pQP8C45qjJEkFGpsybbJhhl7tehfj-brfvTSH6ya_ySZi7QSnVtgAGljjPlf_dVyFxEq0jCmXpblpHkZeJh14pzNwXYX7j9Mwd1qFe-FJCGqtKn3zE8_4UOkhoxmNNg-5m_oJmXXCoitiaB4P8czB57Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fcd2152fc.mp4?token=gD4TOJr6DX04cyOjzqIOnPfmh41bPEvxkTBbKjJwVYtb8DzszTk086VPc9N-sztR4RCzPuuJvdUnoUpbMKYKqWZ3jDWtOSknUNor9aArDdmDAx-9YhjqZYKyen9coWMVkvKb8sWuquzqrGBA978UPwDwBa-TG6-KiVJ5nmlPsAvjtmFB9RUh8zr-Z5IFo1pQP8C45qjJEkFGpsybbJhhl7tehfj-brfvTSH6ya_ySZi7QSnVtgAGljjPlf_dVyFxEq0jCmXpblpHkZeJh14pzNwXYX7j9Mwd1qFe-FJCGqtKn3zE8_4UOkhoxmNNg-5m_oJmXXCoitiaB4P8czB57Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لاک‌پشت در حساس‌ترین لحظه زندگی، رکورد سرعت خودش رو زد!
🐢
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/694803" target="_blank">📅 13:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694802">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ادعای ترامپ: شاید پیش از انتخابات میان‌دوره‌ای، وضعیت اضطراری اعلام کنم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/694802" target="_blank">📅 13:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694801">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5192e0fc7.mp4?token=LOp5fPOKvjGJyov1E5J-Nri1lAfZo0AGJ3P7utTXdz3V7_W84q5SRPz7ysMRo1CIQ_WI5xuQnKjsYEVFjb6ZY9LwVwNoIgNdG0WHkb64yHavmFsXhfyWrUzGb9-417wqLSBnDpNvXUXGB7VdLU7JJIZOOFUjSSWZsCFv49FmcmYmMPMxYjHrdmSLp1arYufxWTv0BSiyzCr9LAI4Zygv6RFlOXQeKl9voxeuAymDZUjjXydXwEy_YW34sP7vD9BdMh7kl8E7zRLAK3IHjLq2bghWD4XLJYjJdjWnGWVgD4d-IubhsS7_TR4k8Quwj9KvRHXahuNkzCUBiVYjCfPElA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5192e0fc7.mp4?token=LOp5fPOKvjGJyov1E5J-Nri1lAfZo0AGJ3P7utTXdz3V7_W84q5SRPz7ysMRo1CIQ_WI5xuQnKjsYEVFjb6ZY9LwVwNoIgNdG0WHkb64yHavmFsXhfyWrUzGb9-417wqLSBnDpNvXUXGB7VdLU7JJIZOOFUjSSWZsCFv49FmcmYmMPMxYjHrdmSLp1arYufxWTv0BSiyzCr9LAI4Zygv6RFlOXQeKl9voxeuAymDZUjjXydXwEy_YW34sP7vD9BdMh7kl8E7zRLAK3IHjLq2bghWD4XLJYjJdjWnGWVgD4d-IubhsS7_TR4k8Quwj9KvRHXahuNkzCUBiVYjCfPElA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری صداوسیما: یه زمانی تلویزیون برای اینکه زن و مرد کنار هم اجرا نکنن، «طرح زوج و فرد» گذاشته بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/694801" target="_blank">📅 13:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694800">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
سخنگوی کمیسیون انرژی: قطعی گاز و برق صنایع تا پایان سال ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/694800" target="_blank">📅 13:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694799">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
عضو سابق شورای اطلاع‌رسانی دولت: پزشکیان به این نتیجه رسیده که وزیر نفت باید تغییر کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/694799" target="_blank">📅 13:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694798">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZfH3hNqM-wIz6mnoUP2sfqAF98gd2ktZVLhVvukyTnWcUCnqbdLx_WHov1KAFWxmsQ0V9dTE_QBA0uB6nTfqCwjzThLBAl1eMNHfmks1DS9XOomRcbtSR60BA7T_fioq-o4nt4zkcLElgCmlm_RVLSE4fQnpOWdiX1TXjvfE5wJvLPaILw6H5LuCqRFbd5qY_aVqZW6xT83mx0kC_b952pe_H-xmyvfhErbekM8NyLWo64tc5mNWW2uyJFv54W22uuQH8kFbpHBx4VILSFHO1lZg5xGTECwgUeupNV2OyXBKvx1ZDfeVhESjzUNOClRSHSox6Mi9kvSuPK5u3udng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیت‌کوین دوباره به ۸۶ هزار دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/694798" target="_blank">📅 12:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694797">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d9c593292.mp4?token=lizNmzHXFHjoFdH0TdY__v4hUUkguYqcX0vkyhv5UfXbUa6q78hLSnKQkMFHg7h-jgGhetpwYQt2r5xXK5MrL3jcU54NeZ4dK19w12oSwcsvb8vvK_MsLfo0N35BrPipr9oCuHLd4_pw4AeSuXO5AAiFHnBVlZAck_51KEINyJCkoEKa_udpsuZR4hXlqZ7fQ1PqLUgXHHiP5saeXvoZLMSqBjfrIS9H3zYi1A-tFwLonyoJZ2UIS7ovOtUnSlz0LXM2fp3U7dk70waAjExAG66f0jytTu0b_kux3gOG_9ODxtwA1Sx6c2jUVKebbHYAQlp7h2rpSdLkVa3Ix92Yiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d9c593292.mp4?token=lizNmzHXFHjoFdH0TdY__v4hUUkguYqcX0vkyhv5UfXbUa6q78hLSnKQkMFHg7h-jgGhetpwYQt2r5xXK5MrL3jcU54NeZ4dK19w12oSwcsvb8vvK_MsLfo0N35BrPipr9oCuHLd4_pw4AeSuXO5AAiFHnBVlZAck_51KEINyJCkoEKa_udpsuZR4hXlqZ7fQ1PqLUgXHHiP5saeXvoZLMSqBjfrIS9H3zYi1A-tFwLonyoJZ2UIS7ovOtUnSlz0LXM2fp3U7dk70waAjExAG66f0jytTu0b_kux3gOG_9ODxtwA1Sx6c2jUVKebbHYAQlp7h2rpSdLkVa3Ix92Yiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناگفته‌های شهرام صولتی بعد از چندین سال: زمینی از ایران فرار کردم و هنوز یک دخترم داخله ایرانه. اون زمان بیشترین پول رو من درمی‌آوردم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/694797" target="_blank">📅 12:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694795">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2ZYkmWkd1cmAwsbD3QVIxnZLuiqyUgSdsxcZKCRqSY7Coz3ItamMUj3-YFXVAjuuCj7y3wh4prOje5pyhZ2hGs3Ce5GYHX7I-AsaPSXCseXjCQJ0fks8t97qSYfRuKyx8tM8V-3TiqlaaWiFAD2cbeimq5Wv5ijYuxeJYx4d4N94ksabmj649WEoTlNi8kzGXeqGZ2RD1cuUG9sjz454l9qP0IjxgmfQvoawwbkaT6sJz1VlCgRslNJHhUh8jaUzKe3mgp1oQv1iQEVPmSSi6TG3Qz1RRYHdDmbHq7J_MNbydnrp_aTkj3VhTa_WwsdZYYOzs9ekNA7mToF_v9veQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qTuerQyYxvG6wxpf3Oyj5V9Iaa4mSdd8PDRUEDA_OE41ujmgN6KdhjSlUqEgN_MIK1HSTjgpFzYwUQsKBCcvtcFtpw3YnS_632ZwPWXb6vaYDK5TFPwHABSNx0vLdXfTh0du3vpk89v96ohkg0_ZmTDupFF9J-z6VOEm0RMDkoGy2KnQ6k8lgmgL_-7ZkVJOha6rR4b_A04RBM-9XYvCF9u5LtVEFtmJebQuKM7E-6zAtuNb8gFcKfrbusfqrq3syWStXx2JKgNZ8Y6uD7MAesIAuksHGddbH8y2D9Anzn__RjX9MHhUCNRyxFNldC2ILPWJGdslN4r6Eml8YADXdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تحقیقات روان‌شناسی نشان می‌دهد باور به خوش‌شانس بودن می‌تواند اعتمادبه‌نفس‌مان را بالا ببرد و حتی روی تصمیم‌ها و رفتارمان اثر بگذارد؛ گاهی فقط حسِ خوش‌شانس بودن، مسیر انتخاب‌هایمان را تغییر می‌دهد
#سلامت_روان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/694795" target="_blank">📅 12:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694794">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KO5DbIgbDhbw53C2rOueW1XqoGWniIaLUpfhkLLvgFvXrCXzzn1weeyJx8zTHuXmUOTVxD4CGeX2KljD0hek3HECK84Ep7dalkTNi5Rz39PV426u8u0P3fNM3Bu-beltuGlKrCITLfWW8Mfd-cGxfqO59J-FJBq51cYrieccg4WkHtIeFmAAa9OAYVqa07bvxsF-W5kTeOMV0mKLPll6Lw9izL5i89XunQDI0YGAslXyNl5BVW6tIcqkLexoSGBxQT25diLm9mv12l1YLf99X_6y_1-5V2aLG0eSXlyTjG5BTvoBEDJenPl9_6v-uQvOlHzenRYs5YIrLFrDe6Dlaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عصبانیت صفحه اصلی اسرائیل و شبکه صهیونیسیتی ایران اینترنشنال از حضور هیئت ایرانی در خط مقدم جنوب لبنان
🔹
شبکه صهیونیستی ایران اینترنشنال در گزارشی با واکنش به سفر اعضای جبهه فرهنگی انقلاب اسلامی به لبنان، حضور این هیئت در مناطق جنوبی و نزدیک خط مقدم را مورد توجه قرار داد.
🔹
حاج حسین یکتا در ویدیویی از کنار رودخانه لیتانی گفت: «همان‌طور که در دجله وضو گرفتیم، در کربلا نماز خواندیم و صدام را بالای دار دیدیم، اکنون مقابل چشم اسرائیلی‌ها در این رودخانه وضو می‌گیرم و نماز را در بیت‌المقدس خواهیم خواند.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/694794" target="_blank">📅 12:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694793">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
رمز ۲۱۷ ساله ناپلئون با هوش مصنوعی شکسته شد!
🔹
یک کاربر با کمک مدل GPT-6 Astra توانست رمز ناشناخته نامه‌ای متعلق به سال ۱۸۰۹ و مربوط به «مارشال مارمون»، ژنرال ارتش ناپلئون را تنها در ۶ ساعت رمزگشایی کند؛ رمزی که بیش از دو قرن حل‌نشده باقی مانده بود.
🔹
رمزگشایی هوش مصنوعی نیز توسط یک پژوهشگر حوزه رمزهای تاریخی تأیید شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/694793" target="_blank">📅 12:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694792">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQ3j0_pQpY40p5lU_oWelO04N9Y27pBG1DJXIv9LYHnKrOAYSvQAp1WXV9W4UlxZQ2saPXj57xApY0jdswuHKjB0D5EiK-YGESawN5FQHbC66jPnJ5vOYFFgQqKb0bI-dYmvw-AbNlMBt69YCjgD6YUw9OgeTrCtItONKNwwWla3tyaU8McFV0ZubcBqOEMIk1gz3_vx_Lf0Qf2693ZVzK_qQdlqTTu1rA5i2nuLgYF5ySAzj3rfdQ-PIW312IqjCV6tnZRXWKJ6DoMNqc4DcEpq-mn_DjK2QSrsmFFw80wv0QUtOjsaq775icBaNPWkRiAba_fPpOtym-jmCLgcPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرشایمر: رویارویی ایران و عربستان مثل رویارویی گودزیلا غول پیکر در برابر آهوی ظریف کوچک است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/694792" target="_blank">📅 12:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694791">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50b553390f.mp4?token=uXSJ2BHuluP8DoKcow6RMUlDqeQxGYzY4IyeVc4ibWSL7yWPGJqxg52lyDy7Q-CjjJwCGlGrYhtqhAXfzlvlOGSUv5dlqewpgC8HQU1yPWTQaY_2F6trhBh8xWuFXXBH7rK1uhlOfHzSXeOfky0enudwQozNdjdvi5Hdf30w_pDFRdlk1ScpV8YJOoIgAKnd95Iz3sRyY2PhgmYvuPqtWiuoEul6lVpFIIczdU0AFeiuh0ga4LdEqiPHSqve3aQHsetaCbNn3j2Ht1Zq4vahnpoEHvVPaanelespiDDKb1RtuNvsBrmEJ3DCDpucp5O70RKIZKwVV8GSI9hIdDF80Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50b553390f.mp4?token=uXSJ2BHuluP8DoKcow6RMUlDqeQxGYzY4IyeVc4ibWSL7yWPGJqxg52lyDy7Q-CjjJwCGlGrYhtqhAXfzlvlOGSUv5dlqewpgC8HQU1yPWTQaY_2F6trhBh8xWuFXXBH7rK1uhlOfHzSXeOfky0enudwQozNdjdvi5Hdf30w_pDFRdlk1ScpV8YJOoIgAKnd95Iz3sRyY2PhgmYvuPqtWiuoEul6lVpFIIczdU0AFeiuh0ga4LdEqiPHSqve3aQHsetaCbNn3j2Ht1Zq4vahnpoEHvVPaanelespiDDKb1RtuNvsBrmEJ3DCDpucp5O70RKIZKwVV8GSI9hIdDF80Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط درخت غول‌پیکر در اندونزی ۴ مصدوم برجا گذاشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/694791" target="_blank">📅 12:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694789">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QDFRjjKa8vyymlSvvz5ctFo_7xA4rfvvj4NaEKa7ky4AqZgQMJHbcCSF-9eK90KKHlkZi9yqj9MM5CPsM8ELEY0zQefUofMaLkAKR_FpY6BYZGE1Pv1s1MShPjbsgauJ22woekxYDBRsrjEDfJhLAbIIaFWbcNNvMINU2x4ERxLv_LhqcL-OjhcIVblqFbvMAXMPXG1CGV4DafGC4pSGMRAy-GkY05yAW9CwcGO8IEdPo7RN5wDfkntI55Y22hw-WCEMfiYgeG9m5OZIm6mkxnX9z9Jreo7rpLUAN3RUutuvflOML-aPab8YtM9Pj1S_xIj3R47M_eJ6WNffNWFwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyUJwc2SDcwRcm2YIUzkEjZsVfPBjn6f-rvqgJaVw4dRSACAwfdpxYpUWmzYS-eSAkbp13BVZwhERrisD-xvVbkwg-LZcWlID8l-l7o24x2I576mXryRvAP7EH8FpBrC925tBXfWDFww56N-D1ZTCJxUo7dXDJ5Zk8qabvzIo7YqMYkFvtJiRE5llU1V6i99zfcS-xMKb-4Cj0A7faSgCwpTiVfA2yS3oN5K76ik7DbuKzp81dApdgj9-9108JC2iTXI2psCNeSRiD3yGJwP_Vcgzk5gtSFxySHaRSXcmOVcu0Jx8iAd4YlGkElt1Gr4GRM6hV2NO8eU-auQB1XR0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ارزش سهام این غول ورزشی به کف قیمتی سال ۲۰۱۳ رسید
نایک که حالا ۸۲٪ با سقف تاریخی خود فاصله گرفته، ۲۳۰ میلیارد دلار از ارزش بازارش دود شده
@titretejarat</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/694789" target="_blank">📅 12:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694788">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cw9YWN2KsyHJIw6MhzBLVh-g26rR4Kuh2H2GF01hjWrgCXCVUc7zKhx_PdyjJjmOUdrTj0hfIKJe_QOStSl7GLgD6YatSFiDKTH3Sc0UcZWtk-mgGfCs5smOu7IRyxorF2lnAepaRKaIBe3JsPzBosRvDp3rG3cl9KzzxBT4HiXhULvNiplNFxqlkAr1ZZ17kvJZZS-gDREACKEf5CoTImM-G82GcWTsp4iQ9O6VwiASuNHzw1H19mtRYm3TB73QbKSIAqdpAfPO4TmFCBdPDZrELcLjf5vfe3mbGdlcZItHOmFtBbKUf9DVaGz5Cj0bDKbJV30bh8C13JsrBeL1kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری الما، خواهر رونالدو: خیانت، غذاییه که بهتره سرد سرو بشه؛ و هر چی انجام بدی به خودت برمیگرده، تنها راه، رو به جلو رفتنه
🔹
بعد از خروج رونالدو از اردوی تیم ملی پرتغال، شماره ۷ این تیم توی سایت رسمی یوفا به لیائو رسیده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/694788" target="_blank">📅 12:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694787">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c348615b0.mp4?token=U-3Sn8lWJz7exSahMeJ62U-gOvDRgjI0t8DUzK4Px04r_9Wi-8X-Fnwji5RviNZHQw2bD_rotArda8otagq2JVwP5BZbrtAIdf1dVzbnpr3-18e17z-nP0okiKY-KF1Eg8GtCh_FT9HSOV5GmnhRJDPsMnSgapC-HP9qFwDXB3Egtrelq33F5bXBUzcohtWJjPthfxwh-8pSWmoJ1azdQNv8NN3OnQ6nzVkqBvk3H56qsWkppXtbq8C9abqWRS7BPeAHvfvCStarpj7q82jp_EeDEt8PUGnR9kvfLn3xPS0C3SqtWvOe427VYPCaDlx-00Dzuwm5KAXMmUzNWLVpJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c348615b0.mp4?token=U-3Sn8lWJz7exSahMeJ62U-gOvDRgjI0t8DUzK4Px04r_9Wi-8X-Fnwji5RviNZHQw2bD_rotArda8otagq2JVwP5BZbrtAIdf1dVzbnpr3-18e17z-nP0okiKY-KF1Eg8GtCh_FT9HSOV5GmnhRJDPsMnSgapC-HP9qFwDXB3Egtrelq33F5bXBUzcohtWJjPthfxwh-8pSWmoJ1azdQNv8NN3OnQ6nzVkqBvk3H56qsWkppXtbq8C9abqWRS7BPeAHvfvCStarpj7q82jp_EeDEt8PUGnR9kvfLn3xPS0C3SqtWvOe427VYPCaDlx-00Dzuwm5KAXMmUzNWLVpJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بفرمایید کفش کروکدیل ۱۰ میلیارد تومان
🐊
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/694787" target="_blank">📅 12:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694786">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
تصاویری از اعتراضات دانش‌‌آموزان در فرانسه
🔹
۶۲۵ نفر بازداشت شده‌اند
🔹
۸۳ مأمور پلیس موردحمله قرار گرفته‌اند
🔹
۳۲ معلم زخمی شده‌اند
🔹
صدها مدرسه به آتش کشیده شده‌اند
🔹
خودروها و کلیساها به آتش کشیده شده‌اند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/694786" target="_blank">📅 12:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694785">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ادعای ترامپ جانی درباره حملات ژوئن ۲۰۲۵ به ایران: آنها درگیر مواد مخدر بودند، اما در عین حال روی برنامه هسته‌ای کار می‌کردند. اما این کارخانه‌های مواد مخدر و تأسیسات هسته‌ای، به‌شدت هدف حملات قرار گرفتند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/694785" target="_blank">📅 12:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694784">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/513ee42a9e.mp4?token=UYJkCHdDjkVogbNOKYyZ0xwbnpLEKDojJCcNmkaZ4gmnRhoI3_ufI6KclyLGgm7O9p9MbLd1Pq-sIAckGV9cnIcrTDIjWHJz635OCIBiBe_RkGdD5_xHhseJucdmHX6zvsdEyaWmewt8edxMhrQOsaDVt8ygC8OAJutprH4xonsrMKweXMVhZeO5_PZVkm67151fNEioscVrLl7ji7xjd9AtJR0OOWrFWjiNGHgdiVpFeusTv8kMSgomnmC3au_I8MKnq3N6yOarCs_zPO_jLqKgtE9RsPkLuA_E0uNy969DiedzqjkH5dv01bHxzkA2db9KN-ohHRaKf4CYcX8Sxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/513ee42a9e.mp4?token=UYJkCHdDjkVogbNOKYyZ0xwbnpLEKDojJCcNmkaZ4gmnRhoI3_ufI6KclyLGgm7O9p9MbLd1Pq-sIAckGV9cnIcrTDIjWHJz635OCIBiBe_RkGdD5_xHhseJucdmHX6zvsdEyaWmewt8edxMhrQOsaDVt8ygC8OAJutprH4xonsrMKweXMVhZeO5_PZVkm67151fNEioscVrLl7ji7xjd9AtJR0OOWrFWjiNGHgdiVpFeusTv8kMSgomnmC3au_I8MKnq3N6yOarCs_zPO_jLqKgtE9RsPkLuA_E0uNy969DiedzqjkH5dv01bHxzkA2db9KN-ohHRaKf4CYcX8Sxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ جانی درباره حملات ژوئن ۲۰۲۵ به ایران: آنها درگیر مواد مخدر بودند، اما در عین حال روی برنامه هسته‌ای کار می‌کردند. اما این کارخانه‌های مواد مخدر و تأسیسات هسته‌ای، به‌شدت هدف حملات قرار گرفتند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/694784" target="_blank">📅 12:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694783">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pouDPdGOurakPH-lLRShdQ9IY_pLc6Bm9I92aBvoOfuJ1e3wcoSKHtl16u8S0eiY0Uh6kt0EwjpWJdO58mZf7DFCL9Mqj8l9UfDHNbzeCCVi44UJ9B9OLyJIIZLko1lB1cZIg2pZdtldYeOzWBE5y31QvnKD1l-scH2Gvc5yWEwXSP53L3McFrMY7t8KVH1Xj7ru2tBwUrtP1I0w5Z8u-qUmOFbEhVY1n9RMjQohEo4pg_Fe4rwCDyaU3IukmRhK9Yu70m7bvwwtftFLDWVsJMg89T6poT227GtmKZ2z70Mt1sRocyY8Un4agTD8Q0Di9rFy57nNSVYIpQv_yVulJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ نابغه: قبل از دستگیری مادورو از هوش‌مصنوعی مشورت گرفته بودم، هوش‌مصنوعی خارق العادست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/694783" target="_blank">📅 12:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694782">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a6d833d56.mp4?token=F1qdwASri0rrw-OcmiM24C5YYkWzlg_AqS8NgqgR-tHPBOaiY4eazy6RBtIEIiowj5JjnhTbllXdWXbQx6s_EgWrebd0tSwR3x377dtIxRipqr1cl50S21SWBV0xe8zfm3gE0mF5-M8ffFYf_CAY6oxBwais98W4emE4BfyLl8DkFS9QAiBzbznvD5Rl_Zk3aitc_Kh4XZYHuXVyzUnC8OcK4bZhjQCm88fnccA_i6jmNqSV4hlMnNGFFJ4478rNL-vI2IcB0YHlRFV8fQK6uekiR4zphPtvR7Uydq4T_VwCJ1qytxfv7rUJi9-nBpzOd2vB51BoV05wdZGFGlTwNIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a6d833d56.mp4?token=F1qdwASri0rrw-OcmiM24C5YYkWzlg_AqS8NgqgR-tHPBOaiY4eazy6RBtIEIiowj5JjnhTbllXdWXbQx6s_EgWrebd0tSwR3x377dtIxRipqr1cl50S21SWBV0xe8zfm3gE0mF5-M8ffFYf_CAY6oxBwais98W4emE4BfyLl8DkFS9QAiBzbznvD5Rl_Zk3aitc_Kh4XZYHuXVyzUnC8OcK4bZhjQCm88fnccA_i6jmNqSV4hlMnNGFFJ4478rNL-vI2IcB0YHlRFV8fQK6uekiR4zphPtvR7Uydq4T_VwCJ1qytxfv7rUJi9-nBpzOd2vB51BoV05wdZGFGlTwNIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نازک‌ترین ساعت مکانیکی دنیا؛ ساعتی که ریشار میل برای فراری ساخت
🏎
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/694782" target="_blank">📅 12:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694781">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
شرکت فرودگاه‌ها و ناوبری‌هوایی ایران: آسمان ایران باز است و ما به تمام پروازها سرویس می‌دهیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/694781" target="_blank">📅 11:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694780">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8bbc2f536.mp4?token=cCpPpThSmuorizl29wKqEpnUWxJRXBqtJOODTZx89d84fQgZHKP1AaTFrABHzQlLWysYUifcjKStMqiBGQs1amwOJsAyYntPXRhoO2EH-15OMqmwy2BjjZVAk-4_xrTJGFP61E3tXJhLYenmcpku24dYTED10OGVeFwKQ4U8dD42eS8dar7sMVZvTd1UQIHjZRd7_5mTIO_sVg0QP-RqH_n2RUB1QsXSgUQiMmp8UD7ufh7UzkGm5Rnow3z5_fpvGNtw1v6fmhz-lfolydCz5lQnMakO5DXwDuB-J17OB5r-95mBV96fqvV8_DNAZc2S05_xmAYGRIgsjQj8Y_U0mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8bbc2f536.mp4?token=cCpPpThSmuorizl29wKqEpnUWxJRXBqtJOODTZx89d84fQgZHKP1AaTFrABHzQlLWysYUifcjKStMqiBGQs1amwOJsAyYntPXRhoO2EH-15OMqmwy2BjjZVAk-4_xrTJGFP61E3tXJhLYenmcpku24dYTED10OGVeFwKQ4U8dD42eS8dar7sMVZvTd1UQIHjZRd7_5mTIO_sVg0QP-RqH_n2RUB1QsXSgUQiMmp8UD7ufh7UzkGm5Rnow3z5_fpvGNtw1v6fmhz-lfolydCz5lQnMakO5DXwDuB-J17OB5r-95mBV96fqvV8_DNAZc2S05_xmAYGRIgsjQj8Y_U0mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای‌
ونس: وقتی به پرونده‌های منتشرشده اپستین نگاه می‌کنید، فقط یک چیز کاملاً روشن است: بله، این دونالد ترامپ بود که جفری اپستین را به پلیس محلی معرفی کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/694780" target="_blank">📅 11:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694779">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
آمریکا به‌دلیل ملاحظات امنیتی، خدمات کنسولی سفارت و کنسولگری‌های خود در برزیل را بدون ارائه جزئیات، تعلیق کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/694779" target="_blank">📅 11:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694778">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
وقوع
تیراندازی و درگیری مسلحانه سپاه با عناصر تروریست در راسک/ تسنیم
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/694778" target="_blank">📅 11:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694777">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ادعای آکسیوس: گروه آمفیبی، نیروی دریایی پیاده‌نظام و گروه اعزامی دریایی سومین گردان تفنگداران دریایی، از پایگاه سن‌دیگو راهی خاورمیانه شدند
🔹
این گروه حدود دوازده فروند جنگنده F-۳۵B، حدود ۲۲۰۰ تفنگدار دریایی آمریکایی ویژه، خودروهای جنگی پیاده‌نظام و نفربرهای زرهی را به همراه دارند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/694777" target="_blank">📅 11:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694776">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dd987a56a.mp4?token=TxFON8htmdEsLUR3udNo96GJqHAjL_0LsXxgrqvFFTMvkrqr9q-KgfnHr65r2LQBjVgut-L6KFHlH8ui1yLxacU9-gJRky3CoANkQmuBsL4d7W8kW4KeVqCV06VSnn8yGUPS-u9tUlb00KQ8FwU4SwD9aRqwD_PiiC3te1U_ZMIhFlmNu-maYQdKzTp15IoExzqB6qRqMrUHFOOPmkFRUiSBvUJvbSXutI3z7lAN3qDTNE2M3sKk-DfuB5Ez0g2gqM_xnnW4-CPTL7s1XjV7193XNSLc4xoqFc3jsoSlfmleA7RSQHBBv6F68ZOUExxY5w0-2-YQqkmJPHgCTVOyxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dd987a56a.mp4?token=TxFON8htmdEsLUR3udNo96GJqHAjL_0LsXxgrqvFFTMvkrqr9q-KgfnHr65r2LQBjVgut-L6KFHlH8ui1yLxacU9-gJRky3CoANkQmuBsL4d7W8kW4KeVqCV06VSnn8yGUPS-u9tUlb00KQ8FwU4SwD9aRqwD_PiiC3te1U_ZMIhFlmNu-maYQdKzTp15IoExzqB6qRqMrUHFOOPmkFRUiSBvUJvbSXutI3z7lAN3qDTNE2M3sKk-DfuB5Ez0g2gqM_xnnW4-CPTL7s1XjV7193XNSLc4xoqFc3jsoSlfmleA7RSQHBBv6F68ZOUExxY5w0-2-YQqkmJPHgCTVOyxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این مدل کفش برای افراد دیابتی ممنوعه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/694776" target="_blank">📅 11:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694775">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F48DAnta8yN-laJYWqf1XwFNR0JyLpvrlEvw8sN3VP_6bhfpBotR_Ay9Qc0BEDWG1jFq2HJpOnmPg5-TMVH4jdioNRqEVvfH5lWO3mKkDuPHcvaYWw0h4FnQicE_9Nb6nVdcea1v2pli4wzB1VYPtTB1St_EnQtiimy4lGmch-PgiU3oHyzPAO3R35zNceOYpqS5fHY4INvnA7-kzwVPD8SFriN-XdZGxnPswhUOn0tG8y3pwC28u6-tENkmtWp3lrmpxk7BW_MRxnjVbEnTPJ8VsG1sOlFdPrg7ZRtdPHC8bDwb4zJ9skayG8vVxKiWzHRaJOIlxfEw9TBaSAjNfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هم‌اکنون/ حضور هواپیمای نظامی پگاسوس B۷۶۲  ارتش آمریکا در تنگه هرمز
/ کاخ رسانه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/694775" target="_blank">📅 11:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694774">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148764d5c.mp4?token=MhRlr3ZOe0Qeqka9s8AteBvITAj7Ubr0cRnjTTVsrDlYYCfJx9qvlbagW1IyIa4ZlAEFv6e8ys3My8fIItTS6cMuY67s-7YabWu-_JI9ReeLgNfwUFbFr7rfMLDF8A_XvY1ouidVbebuaX9fc8RLL6JWncI9MiCQ7LYWcRWFVLEzBZ1MRLAKReZluHqdFEFdAf04vM3wI7UgCRYHw3TuvEKdecHidDyatTB_thEeh6IX7e3JZoNg_YUVQmmRuYs0UcrAuqfE84K3Z0M9AI1xU7WSgvAvQbQ46EDD71PUtXhAQesH-KFBdgqYQh63D2mb5GwVbbMUv_Jme2Gxaafmgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148764d5c.mp4?token=MhRlr3ZOe0Qeqka9s8AteBvITAj7Ubr0cRnjTTVsrDlYYCfJx9qvlbagW1IyIa4ZlAEFv6e8ys3My8fIItTS6cMuY67s-7YabWu-_JI9ReeLgNfwUFbFr7rfMLDF8A_XvY1ouidVbebuaX9fc8RLL6JWncI9MiCQ7LYWcRWFVLEzBZ1MRLAKReZluHqdFEFdAf04vM3wI7UgCRYHw3TuvEKdecHidDyatTB_thEeh6IX7e3JZoNg_YUVQmmRuYs0UcrAuqfE84K3Z0M9AI1xU7WSgvAvQbQ46EDD71PUtXhAQesH-KFBdgqYQh63D2mb5GwVbbMUv_Jme2Gxaafmgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور برزیل: ما اکنون نفت در حاشیه استوایی کشف کرده‌ایم/ ترامپ از شدت حسادت، تلف خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/694774" target="_blank">📅 11:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694773">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53b02cbab.mp4?token=bHBAnlX3dHyhcT71A5pEiYIlugqRI53ztKxFs-eI45FTLeUmfGp2WJCVslduFMBjkimgQxXdZME3cpQxuuqyV3LVPyba_4X9oYl4kgWfdkC6zQkbHRSII2EIB0qG-PcHTBQ9gFjXkCBlfIF8gSX354m5aaEm8n0l1iePoXEtizc5H3fLC6ytbJwkM73y6DaatKyMu0YGKH63bowlGixHDYmG4UUQw4okpJzQIEbQxBHAcYByMwwbtnEdB9voxob8_4YbdcAYtAuuUqBlmKrOQu3SGn7iP-jr33k3aNU-widu5Rb62TFCPkiFCLAzuu7zpI1xYwOvBgD4ectnLPjDsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53b02cbab.mp4?token=bHBAnlX3dHyhcT71A5pEiYIlugqRI53ztKxFs-eI45FTLeUmfGp2WJCVslduFMBjkimgQxXdZME3cpQxuuqyV3LVPyba_4X9oYl4kgWfdkC6zQkbHRSII2EIB0qG-PcHTBQ9gFjXkCBlfIF8gSX354m5aaEm8n0l1iePoXEtizc5H3fLC6ytbJwkM73y6DaatKyMu0YGKH63bowlGixHDYmG4UUQw4okpJzQIEbQxBHAcYByMwwbtnEdB9voxob8_4YbdcAYtAuuUqBlmKrOQu3SGn7iP-jr33k3aNU-widu5Rb62TFCPkiFCLAzuu7zpI1xYwOvBgD4ectnLPjDsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی وایرال شده از کلاس تخلیه گریه برای بانوان در تهران!
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/694773" target="_blank">📅 11:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694772">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
وزیر جهادکشاورزی (۹ مهر ۱۴۰۵): بعید می‌دانم نوسان شدیدی در قیمت برخی کالاهای اساسی وجود داشته باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/694772" target="_blank">📅 11:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694771">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ممدانی از آمریکا خواست به دیوان کیفری بین‌المللی بپیوندد و نتانیاهو را دستگیر کند
ممدانی:
🔹
اگر در دست من بود، آمریکا به دیوان کیفری بین‌المللی (ICC) می‌پیوست و حکم بازداشت بنیامین نتانیاهو را اجرا می‌کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/694771" target="_blank">📅 11:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694770">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yt6HHixc9KiGJzgMqA2wIktUTQnkuBNzdlwdebG5QWDqju5w4n4jH5YEaXT-Cfo5tR8d_bdvZ_GcbOPMXEX2YzhjN0VZXJKY6hh6aOREGSZuRCsBLmimnVQXvUg00Cob5dqigoQ7F_blkXB6z7pSTRJOUN9ejHW_jbrMmyeRv40E1Lt0-Gdk3KBovlN6BH5k386KgWgQTPAz4ivW9GZ4neqxtHc6Fio7Bpk_jh4wsEJIuwvNl3vo2YMAioBYA2Vv1Y4eaTLJVSbhENLwrOGQ5UuIXSX1eYsIAfgsbmnrhUqEgqn8IIHwKDBljGYCBCfotTrHcb6g23utTS9-G5GCIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارلینگ هالند از شرکت هواپیمایی نروژی به‌دلیل استفاده بدون اجازه از تصویر و ظاهر منحصربه‌فردش شکایت کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/694770" target="_blank">📅 11:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694769">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmPKf0c9a2S-GOfXx1QMbFYTCA_4hn-tIX3wuu4RXU1jk7NcnPPkp2AcXf7rg-Voln5wxny23u_620LKsUXX8_tAzRveE6Q1OuGMxVe2AeGCVrAz4B7VPOZEVAGxKZ9hy2MgUUzFNUGwnQjTEQK0fA4uslL-NoVwPqHNuzZPYVtK_MFKOkZDHU19KxAemb3I4eNb59Vrblot9dnt9NqIf2YnJEwkvNnA0boLSW5j2iV_26dKSBvP65vk9mtdsOC78xgs-rhdNYg9h_aL7LxL9m8QG4HmudUIAgcSeQY_rtUTRWeTh8Fk4Ey3kimFkDlo5oVVHzfeF43N5gGKjN-Whg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترین‌های خودرو در ایران
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/694769" target="_blank">📅 11:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694767">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fa0-F8I5XFgI2qr5B-L2Baf-3Jx4Eoene-Qc4oZomsbxKZtKdr2d9618k6IQjgCEF2dJzDvV0zPwGdhA7ggQ46CQU-0CeSQVZhi5n6U8JL8xyyymH1n4OdUdi4G3cwwCkrEMamuoswaf8YEAQyuuiQh3j4A3m9N59vPJgJf-ItJtEmjyzEzrl7PLR9ilid98tJh01_a5DKVX0HU88kF5U2jnh9L2jrcpLRG-SaneHT1LqgeiQbieCecxJJF-0Mhsoh4z5i_NAqivded1wSw75VXkp9UOzjfcMGlJtUW2Z25KiTjvb-ODU8FFF9mOD_OKJoFB4TafgMKC4GOh2UlVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCUp70oXqU4v-b5D5uHVQJypjneD9INcblvfqMYQ6l7XY209gF-FZ3jikTMuCOZX7Q4ELVL63CDUOV_Ya258DCT3Y35zkF-zVCXoQC8rOgUadpOFMC0Inz8j2lTG9_TdoHXrYOkWuRGpcJ5x8wajgy22_8tcKHRDihlVnGfHm1F5SShQT-giFUuD9WRlwk9G479rgkH6e7BlzaEACnpGaVidRBaInBfHfX-MddWqysRrGlctF0_cBU99ph7FbMIIwU8OZHpgUUL3NCVOg9-pIFcWgq9h4btoFqQclcHASFdJgwz0C91vpNqno3q8p65h9KL7yi3Z7psaEJ2to9d7pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ناو هواپیمابر روزولت به غرب آسیا اعزام شد
🔹
آمریکا که به اذعان فرماندهان کهنه‌کار ایالات متحده پس از جنگ ایران با کاهش شدید مهمات و کمبود کشتی‌های جنگی روبه‌رو شده، این بار در بحبوحه تنش‌های واشنگتن‌ ـ‌ تهران، ناو هواپیمابر «یواس‌اس تئودور روزولت» را راهی…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/694767" target="_blank">📅 11:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694765">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ecef6a0b2.mp4?token=pO4JDG985YeH6hCfAsTYQYVgZMLbnhLi6-38jgC-cs-zHK09uRfgPiXpFLz0lZu7hgyRF8n4r-8N30dXTIPWkSsVJQlApXp0K3pToPdOABWJJcwq9Cv9eOpioDkjLVly0y9Kphgc3Klbi0hw1mr4Mh5-AgtSQroh2fxH2aXxjB99aesGELEOemZkSD5EkJzBC8ob5NXUe_zQMVdRj5ICeFd_kpE15G8nFJPm4OE_e3OJal2hb3qTL_-QuBAZeH3oWoDO7wWN0HQRCZGmsSBSZLw7BZRADDTBlr3Fx_ZsK2uhQb7Dqf1HFbGDOz4S_6aYf3NWyjBN9RWSz6I_Yw_Cyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ecef6a0b2.mp4?token=pO4JDG985YeH6hCfAsTYQYVgZMLbnhLi6-38jgC-cs-zHK09uRfgPiXpFLz0lZu7hgyRF8n4r-8N30dXTIPWkSsVJQlApXp0K3pToPdOABWJJcwq9Cv9eOpioDkjLVly0y9Kphgc3Klbi0hw1mr4Mh5-AgtSQroh2fxH2aXxjB99aesGELEOemZkSD5EkJzBC8ob5NXUe_zQMVdRj5ICeFd_kpE15G8nFJPm4OE_e3OJal2hb3qTL_-QuBAZeH3oWoDO7wWN0HQRCZGmsSBSZLw7BZRADDTBlr3Fx_ZsK2uhQb7Dqf1HFbGDOz4S_6aYf3NWyjBN9RWSz6I_Yw_Cyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ به التماس افتاد؛ اگر رای ندهید دموکرات‌ها مرا استیضاح می‌کنند
ادعای‌ترامپ در سخنرانی‌ انتخاباتی:
🔹
ایران می‌خواهد به توافق برسد. شاید توافق کنیم و شاید هم نکنیم، چون اگر قرار نیست به آن پایبند بمانند، اصلاً توافق نکنیم؛ بیایید کار را تمام کنیم.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/694765" target="_blank">📅 11:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694764">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b553c78bab.mp4?token=re5Szmtb4K_efmPmdHyONPSBo7KnDOwslYzdQYDOulzyzh5zyT_ihzrMj6ieR9CqJzUoup72BLwcXsS4Plica5LUU1s77hTZBFXouoi9Pz2zZSYF_sO7P5dFMV3EgCVGxkaq3QsXnaMjKNYQIhYRcezoPvRJbwGTwuHYS_sPobuTEZK6cqu0_KjBGj_DC8Fb_F2tpKSmvryhWWYNId2ftQjpTw5d4JyNJRKdWxZpWm4OHkRg8MRkJVb_ZiHZcWGnDxLmotcpihYeJEK1perQKggAoEj_nuB9713SZZn5agXHen4M64HO2z1DPxwBaDxnaOXEjlaRIDxDpoZXEm145zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b553c78bab.mp4?token=re5Szmtb4K_efmPmdHyONPSBo7KnDOwslYzdQYDOulzyzh5zyT_ihzrMj6ieR9CqJzUoup72BLwcXsS4Plica5LUU1s77hTZBFXouoi9Pz2zZSYF_sO7P5dFMV3EgCVGxkaq3QsXnaMjKNYQIhYRcezoPvRJbwGTwuHYS_sPobuTEZK6cqu0_KjBGj_DC8Fb_F2tpKSmvryhWWYNId2ftQjpTw5d4JyNJRKdWxZpWm4OHkRg8MRkJVb_ZiHZcWGnDxLmotcpihYeJEK1perQKggAoEj_nuB9713SZZn5agXHen4M64HO2z1DPxwBaDxnaOXEjlaRIDxDpoZXEm145zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسب های وحشی در سیاهکل گیلان با شروع پاییز در حال کوچ از مناطق مرتفع به مناطق گرمسیری هستند
🐎
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/694764" target="_blank">📅 11:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694762">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
رویترز: ایران در حال تدارک‌دیدن پاسخی شدیدتر و وسیع‌تر در صورت ازسرگیری حملات آمریکاست
🔹
پاسخ شامل هدف قراردادن مواضع مرتبط با آمریکا خارج از خاورمیانه و حملاتی مشترک از سوی هم‌پیمانان ایران در لبنان، یمن و عراق است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/694762" target="_blank">📅 10:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694761">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
مارین‌ترافیک: پس از هدف قرار گرفتن ۴ کشتی، تردد دریایی در تنگه هرمز از نیمه‌شب پنجشنبه تقریباً متوقف شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/694761" target="_blank">📅 10:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694760">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd954cd0d.mp4?token=G5nSUSwLPRknqtrBU1HtLeI9_iACpaMuLpOjbysZP1wNB6Oj7fv-239uMIHWqSeAC8yWEjDW2zPfB__dJMR08nvIKcXoklxxkJReyZ4OlHhfxIDdUCI6ucfLclU9NuNHM5PnYTW9NMWRYog3u703qTzzu9JkXmsPB9kmDN2cWgf7eV5bpNPV04Q_UcIRfO_xGv4oaFK3OxQHkuR66SnkRzsgpO3DbBLEIiVlCBM2evqSXpY_I9i7Ofs27aaLwM53Wzbp8Jg5NoaUEArbqqhb_OAvudv8UXXSgGl0AzA6nqMDLMKTGp6EyRjSGPiifCSo0IseV7dfLUvNtObJl4F_ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd954cd0d.mp4?token=G5nSUSwLPRknqtrBU1HtLeI9_iACpaMuLpOjbysZP1wNB6Oj7fv-239uMIHWqSeAC8yWEjDW2zPfB__dJMR08nvIKcXoklxxkJReyZ4OlHhfxIDdUCI6ucfLclU9NuNHM5PnYTW9NMWRYog3u703qTzzu9JkXmsPB9kmDN2cWgf7eV5bpNPV04Q_UcIRfO_xGv4oaFK3OxQHkuR66SnkRzsgpO3DbBLEIiVlCBM2evqSXpY_I9i7Ofs27aaLwM53Wzbp8Jg5NoaUEArbqqhb_OAvudv8UXXSgGl0AzA6nqMDLMKTGp6EyRjSGPiifCSo0IseV7dfLUvNtObJl4F_ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار به رانندگان؛ چراغ زنون می‌تواند خطرآفرین باشد؛ نور شدید چراغ خودرو ممکن است دید رانندگان مقابل را مختل و حادثه‌ساز شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/694760" target="_blank">📅 10:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694759">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
روزنامه یدیعوت آحارانوت: مسئولان پرونده حادثه فلای دبی تاکنون وجود ارتباط ظاهری بین کمک خلبان این پرواز و ایران را بعید دانسته‌اند
🔹
امارات نیز با ارسال پیام‌هایی خطاب به رژیم صهیونسیتی خشم خود را نسبت به پیش داوری‌ها قبل از تکمیل تحقیقات و مطرح کردن ادعای…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/694759" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694758">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
نظرسنجی جدید آسوشیتدپرس: ۷۱ درصد آمریکایی‌ها از نحوه مدیریت ترامپ در قبال ایران ناراضی‌اند/ ۶۹ درصد گفته‌اند این جنگ ارزش جنگیدن نداشته
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/694758" target="_blank">📅 10:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694757">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v17yvVG6aBt_U_y4oFyfSPEAozuZVqSvdNBJwa30NzXjHFQuuhoj4uof405KZhSEjjk_P_V4ZA2wyWeNZrxDHpFnQHp_eaLNNzBtZqeawo_9yqUyWFdsleUb4rw5rj7b6p6epZXMIBK59rJfv7WjssRJpethc0YUY5WsvG4VF4odu3Z1SlgF54Lvn-GuXxS37ZsW7m2ga-GH6gekuzrMaij1mUlEUHLzckA8E7aB90fZVf7RRFWGX24o9QKefR9O_4C0m4sICaZZSlTgK9dAy4shBFDgBk3NOP2cNLiNygmTQq_DhhRD_8vs4gGR9sXOByMQspRMBO91KiOb5elIDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واحد‌های وزنی طلا
🔹
از سوت تا اونس، همه‌چیز درباره وزن‌های طلا
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/694757" target="_blank">📅 10:22 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
