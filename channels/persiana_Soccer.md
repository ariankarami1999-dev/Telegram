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
<img src="https://cdn4.telesco.pe/file/U5RxoE1iJEI-7fuDf2Nu3CUZgIY21fSNpUzBk3d7MsUOesjVB_JTLs1WrH0iSJ6TQ58el6lburtmLbi_ji3nIjJmCcouh--SjaOMlD9uJ7zs10IxhaoPn_mKQAIsX7NPbfS67bDOqeIkXPqG5DshmCe2Xl88gkzsCAEVDDb5pXm5cIBbDuMFS1nI2hk0Uu27FO63WGbQkd_hBQGQEH9JNOk1OUJXfJ2tNXHolytDMwauVwOA69O0OPpTjNB7FNfIDptGTkKltf54R4kZkultVfFaJrHTyRXdZfpVjKiUnYQPF5hxQ5fa0wob56sHdKQP5x_zL691FNsqiRnu4y_nUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 488K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 16:17:25</div>
<hr>

<div class="tg-post" id="msg-31314">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmmNMIgVSxGIMd2VnqBCPD55xh73a5LMkYcaahGZjiAfHoHTHfrA-q0WTlsDMkDwRe56xaGfRfKSvZAwCmJa4NlzwWxI09L1yGcHsgEdWe1ggHc3pA304TfqJfCqNvWIP8DXQdXOqzu4osNHDpqGLPIkgA1hV_1Na_NOGf9lo_TbMA4XQY8Cp3tVYPKA-34IU1lwUb72ic9rCQcSVOtd2SMGT-mdCmzw8BGOMLmjhN0orQGQGgDF4M7YpPN128f2skkFAjWJPDrGNsYkKvL4S9vPL-dyc_ZBP0xb56lD0yvoUOmpdlSvMV-UNj7ISzIZhlKAHMAaxkGF7DxRltIyLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو: به هوادارانم قول میدم در آینده چند بازی مهم یا یک بازی خداحافظی با پیراهن تیم ملی فوتبال پرتغال انجام خواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/persiana_Soccer/31314" target="_blank">📅 15:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31313">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRdq-Zj8eAkqrfcgV206J8Lo_c4YTFiBmGuddQsTBDdbfND1trCiLPr-hV14H9nmXwnt1LLs_ADSP9Z6rfuSZeTMJazUmAN3glwObkbsI7r8DjoYlKh0B9O2Kh1MLtEjhGdw_xYtYgn0jtEcoPaE5aonMDOwuUDL9maYW9M3aY_Kwm0eWsLUhEK1HxBVMZprNYtiJMx3970eH8lliAKRojEmGM7Xf0S9072_Cc2A5ivDtY5ZgqWpNgg4FDNDGJOF9Gok-nfsVfQs0SM3pTYDgwEudNuFQSkUvNaqlUacr40GwcAkDNNAoAdT81K7OnKXRwvAhBMvMhU8ucS6nVZoSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باگلزنی دربازی امشب با ملوان؛ علیپور با گلزنی در بازی ملوان به رکورد تاریخی علی پروین رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/31313" target="_blank">📅 15:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31312">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cldavU2EBl8EFmp7ZP3vUu0kvZsIAodDP9ZARTpJGLPxzz-FmX00P_5jtctr7cK5bqiSwK-yrniO6onKd8kA7ySj4v7A1CxLKeO8n6Gk-DsZHyyyjJKC5F1V_DQ0hu4A_qhrCzQv44DwIUxfSvY5mB0EfYLEQ5vsQbNn2LDHM4M2pGeZF6fNRTlKiuYTjFPwoTN69-i1C3nZPCjixW80RVTCKdb4IV7T1rD-v1ErFcV7KR9CoFUK2bRTGCOfsLVJw6jPVVHb9IiMTpbiGM2BRkvFiagddaJQcw25ADyfVCGsWBJjSiI6cUcWfteArfzv1hqgdKSdTfxiY8xQJ_DqfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه‌های پرشیانا؛ علیرضا بیرانوند ساعتی‌دیگر باحضور درسازمان لیگ قراردادش رو با باشگاه تراکتور فسخ خواهد کرد و راهی سربازی خواهد شد. او از اول آبان سربازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/31312" target="_blank">📅 15:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31311">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IY-92YCHK81HXWDZg2LDs33-trlHwW-hEHNGoJRzjXR1dDTgfH6cu5EIbUoCCVauLqAbw2teLl1tHLTSC5qJFripwDBw1f6axvJhVWqTZCdkB9R7oVORqurGh19KU89Xxmrde9RgzUHxF0qQpnaxnLCTnXMsnDndvhQtS4PmOEWSw4l_hGGsItKiCZH_CDSwUj0Xq3O6sM4z1s0IJBIOFwYLcgqxquIE-mklhDbwjShzyUvvk_iX-r8ftSwWoLsb6w8JwG5FO5dmL7QuZes_8ou3o8kx_a5jBUCP77Y3I4jDZWr5HT9VvaVRIaNSYI8qB_Tupp-_A64IS2gTrJGkfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام‌باشگاه چلسی؛
کول پالمر فوق ستاره انگلیسی آبی‌ها قراردادش روتاسال 2034 با این تیم تمدید کرد. یکی از دلایلی که پالمر در چلسی موندنی شد علاقه شدید دوست دخترش به چلسیه. پالمر از منچستریونایتد نیز آفر رسمی دریافت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/31311" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31310">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAgEy4syLZAFjEGiaTmyFJsLtuwmYW_IftXE7adEHA5_MkphsnuEBTZHzRo44XhGguQpjpime8UUvmW1J-15Vtli6cBbCPZnmLMQIL1PSGvI34E6g0lXqGT0Gv9HP7k1Uf9ptOTS9sYQYKwZ1yTDD61AHbFi_qY-j6viU9XpS3009cGMb8PS1bONlfdQsANTTihXtJ2SXMP0PKHllaaxwqukObtw55ofkCDpn47kKb2DE23VSZmg_5EBrPeX1_MIv0VSgzsh-IM07rMBgar4Nd3dnh50vCZzem8Yg-ta_ZMk5dUI_r0-O8Fw4dxdi2ByVbKBE57CtdxshQ6x2wJqDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیگ سرمربیان تیم‌های لیگ برتر در فصل بیست و ششم؛ محمد نوری دومین اخراجی فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/31310" target="_blank">📅 14:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31309">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQijyyUscIcDEZ56XXDg3pkJdKK2AuVEwE9k5Y1bWBNewJV2c2Oq__h1mkbT5c6Jgi3dPH9oiUmc2i_Pgqnl0v1Ymsk-gJfJ5jBiYAVNkw1BZsP3USvyfG0BG8mAdeMpZ4VMxxf4GG8p8BCwGRpyeLME3WBh_kOW6lpOcFnPeXAHvCgv5DJxKCkkxZthQo9fYtAcw9FZAxQHKLLYSDvdQMacXLiXTqpYgqMzqxJbsARIG6bNkCOpwo5X81nkEh1JswlX5kfaAkGHNpSkW_7NkfeIs_v3HTjK2omlTIcufBJb0902dNIjY2gTpXrI7ohpaZccMbJlvy0Y2CWn9cNS3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
گل‌ پلی‌استیشنی‌وتماشایی پاری‌سن ژرمن در بازی شب گذشته روی همکاری دیدنی عثمان دمبله و فران تورس دو بازیکن دیپورتی و سابق بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/31309" target="_blank">📅 14:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31308">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrqTIK82KexzZO0Jco4EO7VPZvd0ItB_P1aPwpVApEslQt_IiesfgzrhhC4hh9pzCpAl_eE-JX88MrWtg6ze4g93u6j8Lwy1N_bunP_pJs1UCygrvSvLC2ofnIDji9c_HKHscdkfFxCjeu52T4zY1eE_HqNWp601uPdACyzV-jWOVqQDWfO8KMGJDnBkvjaRDdz5bDnvy4A8vhs4ooV8cw_GzXyXzjavcsGptHzcNilE7xGMVN0OiH2bX2o4-49lZXJy1Xhkti3o9Z5NOynHB9Ejxbkut4o8EUJ-2JqBm6lVF2iom-6p_YZIEXSkoY1bV6SYtguhf5m2G-M7KUI1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/31308" target="_blank">📅 14:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31307">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTmyO_fekyb2uO7eVkuM6as9OSf7aWECeU_cNZ-Q892GipV_7ToJi7sBTWiK_o4JzPpYzRBXv6YB0chJDXta-aXK8hTFVGjmpP7UtDYol8PtIg2HQH3KIJ2ULCPAn6BMT-cibvspcydo9wlgA62zR3OwHdNVfUmXPI5w2B3c0H9_VPO4leAe2jecys-Bcesr5JgjV1AXEPpJCPyiNHcgCFWfos7XVbil1T_aoUzsBpmza-S-OmSYLxhVKeb4oElmGjh8uwC5AplCwa89uVmAgMGyAfIJPLfD5xYjnQyeHkcCQNljtdguSl95ACEtlktWXu4jb3MRdV0sYVoEWsHVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج رئیس فدراسیون فوتبال: هیات رئیسه مخالف دادن جام‌قهرمانی به باشگاه استقلال بود ولی این مورد مجددا در حال بررسیه. اگه بخوایم‌جام هم اهدا کنیم توی مراسم برترین‌های فصل اعلام میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/31307" target="_blank">📅 13:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31305">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ne2JTTFTvURc0Vr622vtA0O0NAD_UtAKFSJ6hVMTZCQov59Mn3leRTypcWef6JmgoqzJ0lc4VbiooK7jcgkP4qVgR4VTnid66zABm1yP_BqROguPUBEbeX8ACVb5UG6GxbwD7OmKb7om9C1duiTZKJZWt3NRdciAh4agZjUfAZMhLEFE6PZF-JDjGRnU1mMz4v66LX5aykdx5UkmpGmefVF131npQHg66_2cCeKvddIHISvkhCZ5f0x14kHemxQhNNUkTQgO7YpkyZGq78c0EhI5CyazouVfn_UReM6NpNYCQOI_j91w9k_SYCyxpOHMvPTNzKaLLaghK4E5J_PN8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKY5_fmCI4U5PlHxbIcoUHWgBUi3zHeiSPz4JiMkGlZsX353wkvS8rn8FSe281XAdTuRebKmYLksAv8dh6vlhmndknsi1EP6hx_uY9dUHDMsMqhhBscIUu3rbHFwLvSeUtp6CTJXKXf7zItA0cnsNLCk_Kpj-KWXgU2ye6AIJIQI8zZgkPnvBClvdN1BJuAKV0P1KektRJC1C6H2t5ekrSXE59QBLufNxXXv5ioz-r6bi3ce2zw_RHBSVKa7_3b6DtXNuepT02_W6WahXohL0wA6r9-Az1c-b6-zzv2zgMZSuKBVMrKWZfYvF8_Eit6SKnKUPjIKDQvzq_Cq7qdvjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/31305" target="_blank">📅 12:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31304">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCK5tuaGvVu9Rft8BLqmyUm6Vd0W3g9vjTnuHpdOqi0aeZ1gfeYqqaWhOUykNidP-4KQ2ex6iZe635hnGrVJFMp4sp9MaZbEOj50lFcuCt8rAubJlOHy3Cai-VIs_SamyiBVxfiw7XgMzVB9ZlhWqA7-wfLVZraUhsuFbO3V_lhajlhkRvLkkuKOJPPFxedWQ1L9VNls4P9qb42SrJuSYJk0vvn5kPJI2_QBKVogWfyeg8IwOFz_6ytzxDvrpWDu7yVRme3zziA03gNPK_QdCpVlRfZgSTSu6E1yMkbixkigsmgBhcrVop9zQCKXkq20nLK3ov7uCUkflY4B3Y9Q-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گلشیفته فراهانی با جان سینا فیلم بازی کردهه؛ چه لبیم گرفت ازش. الان دارم میفهمم چرا حکومت داره تلاش میکنه گلشیفته رو به ایران برگردونده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/31304" target="_blank">📅 12:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31303">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jp3pxa72eS0-ABZXv7Q9LGuJ9rW0lPjHlEL6V6Gx4NQVbWz6OwS2WEQNBbrUT3I3A6dUKZTUGtTW-Zya1ftjwDAiUK1PPYPdXsw9XYrSoIFO1oW4j9UHNDbIOGRNJ9mdkF3lKBLdWbohcUoyEKQ1vr_61pCIE9UtnOJeHLWtFIv_e6QHDeT5uNcsvriT3_hEPPNP_YElxkoh_KK4yFSEl_l4JjgqtGSzwEmv2nqXfbzq6SFD6Ay4w-JgPV5951323-oTuwUU_8KHTbaazbqd465CytrFP2raKvn-YLRYCmQTwrMgtlGaQaq95eoLrAEX5taHQTk5-XSlVs2PWSfMTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
گزارشگربازی‌دیشب‌النصرلحظه گلزنی کریس رونالدو: دردوبلات‌بخوره توفرق سر سرمربی پرتغال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/31303" target="_blank">📅 12:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31302">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSwhW6N3CO5mZNrBWw49QO6SUE4uaCl19YyeVVC6JOUm69AOB94PgKVoeJ3d_j7A7FgbQU-Nd1L464gHg4Fm3ZpEW6RKh51CI8Rntu7rZHu5lD7z_UQlj3hb3M53d7S2Ix5i2aS3R5qdPE2Nsj2R7MBI2rF1qSNogxSm11YmPGQZxe57lEZrEpoiBBH6uWjV-MZxf8n_lZ4AZYUdPKxOsTCoU00yU9igGkZ_IUiy6u-6qHs8nvr2O25pJsvGjxf_tvA7CNmW8W4pUVwSw49IBSUrebSfBTJpdlrtSCgvHIE-9GpowUwUV6UDRm3xLYubS0gudmM5r-f91oHOVnYhQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگااام! مگه میشه؟! صدا و سیما: مرغداری ها برای افزایش وزن‌مرغ‌ها توی‌غذاشون تریاک میریزن، برای همینه اکثر مردم بعد مصرف مرغ بی حال میشن!  نمیدونم چرا حس میکنم هرروز از این چیزا میگن که مثلا مردم از گرونی مواد غذایی غر نزنند
🥸
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/31302" target="_blank">📅 11:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31301">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCBfOBbzrsH1cs4-htOQdcZVcNjAYj3JzRXT6IeIlFpSi_2uEtFmCwydlDeojYyCZZ-OXKyoRkXEsYeRLV0I2jK-wwivDY1MGlwvDwzLLRSou81nahTGrZ80WoCgFnDyczMgJVXketP6B6aANm2Qh2L5bk4WD6WovMDtDHmkhgRgSOSgTNTISsh1A6M8EV9XioI3Vc_mNYp7Us6C2dZlLHJqwK-eqfXHYXDkNhh8bhN-W8wJFAHTilvaTFaDoGHswXP6qPUaZVzaHKZfgsad_bUIgU6G0fh4Hse2F6SXu0AFu-Vy2pTDS6g5d33UEnp0rwgonuemd-iqkGZKU-GcKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ایکاردی‌بالاخره از وندا جدا شد؛ درخواست واندا نارا برای دریافت 250 هزار یورو نفقه ماهانه رد شد.
‼️
ادعای‌واندا نارا مبنی براینکه اون «شغل خودشو فدای زندگی‌خانوادگیش‌کرده» ردشد.  مشخص شده که دلیل‌افزایش‌شهرت‌واندا نارا ازدواجش با ایکاردی بوده‌که توی‌ایتالیاخیلی معروف بوده. همچنین واندا باید دو سوم هزینه‌های دادگاه رو هم پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/31301" target="_blank">📅 10:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31299">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3341162dbb.mp4?token=dU_aoT9nLG-Aek0Ate5Dtf1eu2wWW5agPORl3Qw7KkrCFXBMM6PU57mcbtFLgmlBQT5aU_aMDMJn_vSrlXV3XS_8PeRwqqPMjY6TPlH_Ni1sMAt0_iehNvQdQWlw9RroUh4QEMAEkP6tYtd0NL8zLSmx7PfLE7RB72aUC3vYCOlybqo2R5oyUEG2OL5MAfiY4WKK397PB5NK27WNqhEQjOxcubIHbbFQzLWYfVN9RX4fuvA6c-2-esasJJQgY7ppAtmGWtmPFHsNQLLRrgKtpped9xEd9B-CUNd9nEysT1UqIa-96aSISvbIMC4AW5Dn7la5zF5hJdfGdh17T1-PAlE5OpfERMirIkaBr-5qwkQIfZbbfThVzX1o2Q1nFQcyoc5D2UBF1627WsUo8CycoYwLiDjXZiRz32pFDxdj3mvA4LAmhW8GbIN2mB11i9-3c5cqykMPbRup7Rjvv-3jslGzO72LVFmfJ8cDTIHazGzRYL10Nf0XSDVmBtcF7VNv0mWwHfHKIK-OQahaVU0KcMWpTxmWXBKvbA94p3lvgr-jE2I_tK9uepFDRunZX85B5ntuj4w10NMLI5-yKspd-pbBCU0sBbW-W6bWPWqakdDAqXIz07GUKMuIbc6FqX4xL71fn-VMwQZ00QNBv7Tz8-1hJpJtJK0iSZLj6YsacrM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3341162dbb.mp4?token=dU_aoT9nLG-Aek0Ate5Dtf1eu2wWW5agPORl3Qw7KkrCFXBMM6PU57mcbtFLgmlBQT5aU_aMDMJn_vSrlXV3XS_8PeRwqqPMjY6TPlH_Ni1sMAt0_iehNvQdQWlw9RroUh4QEMAEkP6tYtd0NL8zLSmx7PfLE7RB72aUC3vYCOlybqo2R5oyUEG2OL5MAfiY4WKK397PB5NK27WNqhEQjOxcubIHbbFQzLWYfVN9RX4fuvA6c-2-esasJJQgY7ppAtmGWtmPFHsNQLLRrgKtpped9xEd9B-CUNd9nEysT1UqIa-96aSISvbIMC4AW5Dn7la5zF5hJdfGdh17T1-PAlE5OpfERMirIkaBr-5qwkQIfZbbfThVzX1o2Q1nFQcyoc5D2UBF1627WsUo8CycoYwLiDjXZiRz32pFDxdj3mvA4LAmhW8GbIN2mB11i9-3c5cqykMPbRup7Rjvv-3jslGzO72LVFmfJ8cDTIHazGzRYL10Nf0XSDVmBtcF7VNv0mWwHfHKIK-OQahaVU0KcMWpTxmWXBKvbA94p3lvgr-jE2I_tK9uepFDRunZX85B5ntuj4w10NMLI5-yKspd-pbBCU0sBbW-W6bWPWqakdDAqXIz07GUKMuIbc6FqX4xL71fn-VMwQZ00QNBv7Tz8-1hJpJtJK0iSZLj6YsacrM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
تفکیک 980 گل کریس رونالدو در کل دوران حرفه‌ای این بازیکن؛ CR7 تنها 20 گل نیاز داره تا به رکورد فوق العاده و تاریخی 1000 گل زده برسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/31299" target="_blank">📅 10:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31298">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vvp9Mwq-_a8MRjKHL8TZHvM5pcT_UaJtEPKhSLgDXvEmBHJeB-SpBEKywA0-7rQ8Q3epr4MjOAM0dU4dVFVoCeVaUeG5ocBwsDy490qLmpIpc8_4wzTNirX8syzveB-bnSJo3ta-K4hs5pHyUSa7-EVeE1wdVky2XX62NiXOUNDwBTdThAAQyBPKf4JT3Bbz1FecavlPB_sRlTcnG65PdupcEsjncMPUmusRTQ4JRJW94qqEL28DZO7cctKTrRXSdipum6lH5Txn2Lh2MirsWBYuZpzmbTrr1R72QPeISu_wJBa1KjtAflrOMutWLnBz_pOOccykFAdz8yY4jdGbPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جدایی محمد نوری از نفت آبادان؛ با اعلام باشگاه صنعت‌ نفت آبادان، محمد نوری پس از شکست مقابل تیم پرسپولیس از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/31298" target="_blank">📅 10:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31297">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kytNJgYQROdt8eCoCcUgIE3fQb-Rr0MbSmV670vIRaZEW8KWbm8Pi4icTFA-P3HVE5o93W6j0i8VJbjROe48fBKOgzkcLQYpc0QF7ais5urcae_0TNdmk-LlN0uSk9z8XW6k0MxLZjZt6WZOTQDhO8Ao8i4eW7fsB6bCCWrNZNIIjLeOfqVFJdVB7jbj5-05x6Git49B4cCL368huKeW1H5McTXGhqd2lboDeFbGY0VgcSc7TnHbcDIPMQbwT1vvPXjUbptl2rHHYYX_9y3lhyCYOeZ3mGQoWToHGbrZ6P2B4UdoTm8Gp7WOnvaaun6AwOTBakVw9GQP89kAWEnNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان‌نظام‌وظیفه‌به‌علیرضابیرانونداعلام کرده تا زمان مشخص‌شدن‌وضعیت کمیسیون پزشکی‌اش حق خروج از کشورو ندارد. از طرفیم نکونام به مدیریت باشگاه نامه زده و گفته بیرو رو دیگه نمیخوام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/31297" target="_blank">📅 09:41 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31295">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxMsGA6cnGgMOC3YJIzHxQKvjpL1RyNBhmkjFE-qk4n2yvEbAGe4jtHMdG56Y44bfY4vpC4Un5xz2xRVejzyxmR1sPJfaHOrBoxQkE9K1Mx3Sh2vb_4RBabABvjjnW7jIsNOqA4fsGqSKjGmSJp-AyeDg733-imz1nR9sCtTT__gnHM1DHfvILQvODYijdMw_CG1jEUmhzLpywmw27h8bGNRu70TQ4OULi0oxaaOAWGPyIWKPYe5LUFV8Va3Pdm6hJjkUw7AntmqNnFSkxcwHaHE1bRA628Wj71w2yvNP-65DndLGczB9R6hNzy8WFmXwhFmAH0P5PHkV573cQoO5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/31295" target="_blank">📅 01:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31294">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXI_ObCJknLlbpzJXLSNMddYt_zXT4cC22WNvoN6La8-xdhp8sP_q1giZnJnAUx7tGcMu6XDVc-YOP_-ouKQ9ij0rO4nLcBSvURcf4GtKUm5z19T7SIADdYydyiPakrmOJXkfuQxhJphnKEpOGzjKvdMoIhvfXHxFdvgrGmvyywrNbZxSXZ3lO0LNg1r9on3FsXlyIrE_JjWRMXeYE1k9VKgIWZYdOhAC1iaDdIbTokenSG1tZP98UnSOeJlJUQIrO3MwIUFdxYBb-vFkbT-b4p3A4gQPIsHfjAwsnQubgi-DtgFfXpb8i3r_BicJfOt8L2udnxvAJuQamLPLmzmGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
نزدیک‌شدن پرسپولیسی‌ها به‌صدرجدول‌لیگ و برد النصر در شب گلزنی رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31294" target="_blank">📅 01:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31293">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7qadi7nNkuu-SErlmtZyVq6BTzhyFuWcsYa_h_LeN5GSL_LZRgTht9Jv62gH33NzIiyIXimLQ1QEBU1hUPbuFV-WfzThiOjLrciTT9QMAaCVY_ybzFf9aUUUMKIq7_D6FtbDecz6XrigbEHsikunmsYhVVbYLqeA3RULF4sBC1AR2Jd0T8nFgxxMZvttKpgp7C4NZER9OHANzYHyu6sUGaPd01UuDnQrY6Y38liX8Q-n1iAmBLaXTB3KNPi1R98HcgmwShBXBl0dzA6m5wRHenjbJFGUeBDyx6RkTiv2hIpWuekN49BvF1U2IXhy_auvX1q5Ew1Mmvygl4zpjGNag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛برنامه بازیای معوقه هفته هفتم رقابت های لیگ که روز سه شنبه و چهارشنبه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/31293" target="_blank">📅 01:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31292">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz0d6ZhUdde9rX6Z0vMNkqBgiYFqSR0KipwKXzzJHSC5PFH4csombh6jXYsVGAS1ZMI2oA2RzmD9ohr0feZbKtWUOmwEIc8hJve8kwTPGAcLt14yb06un3YHIXPeZRibCwA-vgh6IbKuVBkOYRE3n3h425WgIE1nm23ITIgQ9AlVcb5gqdJ1uP_7Ecq4OasMXXviXb8YXKp0dPaUBP7dnWjHksA9PMtzOwkF-4WkeM5mQiSi9yWk-DZ39iQTYiXNH0TGTOjyjHmo9HNH5pzdUGcu6HR4TL6ZskIMWqpfm76zrESHYdGorbxECVWoSIeB88DOEcInxBJ1WQlp5ACxWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ نبرد شاگردان تارتار با صنعت نفت و دیدار زنبورهای وستفالن مقابل وردربرمن برای حفظ صدرنشینی در بوندسلیگا   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/31292" target="_blank">📅 01:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31290">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT_WYKXeHTFQt3zLzGr78y0e_nDfYr90kZY7pNcvn8b1Ag9V4UEyDAqfbr0DVxqPwzfiAqNndUUrQ2XOP4fnqaflK7fTYhrk9H6YMmKVoK6ZyJA4fhoM1FwB1_KsVDLkl4Cir556RjhzSsaj7kigjC43VKmI5ZBdXPMLrlvkCBbNol3VqNdM0_XMitrzjzYKCthU_l83Jo73MK9MqaLWOqFA8VxHS7txPuzBfQ_G0mFXyBgofzz26DgTqHz9qBxdM4YobMITIhEgrwzjRawCIk6J1ZGPb_7RbRnIKBhFRrfXc2X4Qd8P26sEMH8ok-YEu6savLjx3FVjyPM0GcsnCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
گلزنی کریس رونالدو دربازی‌امشب النصر با الدرعیه؛ این 980 امین گل کل دوران حرفه‌ای CR7 بود. همچنین رونالدو به اولین بازیکن‌تاریخ‌تبدیل شد که مقابل 160 باشگاه مختلف موفق به گلزنی شده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/31290" target="_blank">📅 00:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31289">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDyjIWhksiCzYzKNFJxbg1wg5yWogtHm2811MhYtQ2Y4BV3atjceuCyG8erRFobsm0XOsvveaQDJicCPZmxhJ3VUgu0bOQdcXfiOljRcXwXSbKIKz_krDavu7fTb2LSgDWNiR8iKULkB7t4SmETUvhvEIFkNdNIZv3OdmlBcfZBneejRMb8B3FOSR51n6QGG_nmcPqRfzaxlA8E8VXa-NOP3EPewy_aGw0IIqgdizrhzNnOjUtLKbJxDfbBbzCrMNmPGyTewpb0aiaq4URkgEAHkz2uw-fQQNcLetkcy35qnbR5XqRqyrasqGd3IFxMk1idQpJx4l5yhDVBteVHZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دختر خانوم پا اسکولز اسطوره باشگاه منچستر یونایتد: جود بلینگهام بازیکن مورد علاقه منه. بنظر من او در حال حاضر بهتریت بازیکن فوتبال جهانه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/31289" target="_blank">📅 00:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31288">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcUfRoutML9IOS5ZluyshPKFBDL9yxYYZaU_z_-VosLRnKIVKd3MuqUWTZ-OQhutAJlylAPOiswiiHm1MJBt472crUYrwr0VtQ1_21lksY0bsalBsQjQDIzo4cb0dcpN8gB-lRCUylmC-HD8NM22O-GCH0cp0K8r9EA9ItHdBabWBRrrSWxmYSdzYGGWfo5mGjM1AmuEfLyQ1S3KGh8VCIy7cis_s_XxROwDodqEVsZsJyEYS4buHOJj98SzxNv_T33xsj-Tlv1BnKeDQsC9_NzBdfeBK4O8Z_LDLUJAxoTiScWXexrSz0L6-lgyMimLOhMTWwxSQy_GAQTDuQRoAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان هفته هشتم؛ البته بازی‌شمس‌آذر با پیکان و بازی‌های معوقه هفته هفتم بازی مونده تا جدول رقابت‌ها تکمیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/31288" target="_blank">📅 00:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31287">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
سازمان‌نظام‌وظیفه‌به‌علیرضابیرانونداعلام کرده تا زمان مشخص‌شدن‌وضعیت کمیسیون پزشکی‌اش حق خروج از کشورو ندارد. از طرفیم نکونام به مدیریت باشگاه نامه زده و گفته بیرو رو دیگه نمیخوام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31287" target="_blank">📅 00:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31286">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcV6RQONWAXjhr-adHgYyuQ7xKBPOtzXOOJZOaBOgGKPqpoRLCJHfzwqI3zbw2q3VI0l3pbg45vBSTFhIi6C_6oXIlaK4GWCcd7CWB5RUqzKHHcv-apOpAbAEECbsVqLVKNblM3qzGw2a2rI0z5ZKxZ9pikN5i875RiA6aJJLz5gmdjeDKIrGOxzzsJthTSIlVnmz_2RhzEIT_q_4ChdRUPeCBlHe6QBNdZ0gJBKSdkW-4T6dEnUJOktnxtzR_0PUeP8UQLQ2_CSHUX07-oMauZZ6iZFU-aVNmRsLd3Vq9Q4f8kK5Vs0JYsx25ryNxt9K3phORS4tRXUrGu6qA5nDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ علی رضا بیرانوند از هتل و اردوی باشگاه تراکتور تبریز اخراج شد و با صلاح دید جواد نکونام برای همیشه از این تیم کنار گذاشته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31286" target="_blank">📅 23:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31285">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUIk85HOso4TwVVDlkBKfbVf_VcU-3ZodZvIBNAEGG0ndPuk9xEaCLNK8iuiu6sMRJ6UCBsrccrCy1JHv-yLkhtVooX4zi44YinUwUnAYlb62Zrk_kPdw3UqiYyjeuXiFa2T_x8G-LdekAeV2eHY8cC_nK6KzsOhpxtPyFzT-o7i_skfvOirk20eZqpaxoPp6tJuLWqX7itjclEWVNKLwFmC1EWNu6-e7nOFduAstURO7Dbc8TTpj4hFHd8I3uPnf53oeXDuSDLxNyyCfk2MDCURgK9q2jdcBOJ1K88X6MG-YtvLzVdtWEsTqI4ASyB6NIWrioC_sePr_kKsNFanOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جوانگرایی‌بسبک‌تارتار؛ حضور پویا اسمی بازیکن 16 ساله به جای ابرقویی نژاد در ترکیب پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31285" target="_blank">📅 23:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31284">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsC5UtbWYFLIPCEg99c3lroxF4_gizKMJIzCi0HzRLhAiOTu7QfuyrlXw7kwxb9x0O9lvSplEg1_vUbWRjoRME-Mbcn0EKO5dArRjuzrpNXOH2oy2pV5d9OupbCmlEhgw9_is3flUq-7HYDnLj4Pv507mvvf4Mp7xcLvmBejUydqk8oXYt_f44_-n8VCfovRfgInEFw0p0wLdEVubvgQjsvSCDGpHJfu8x-355Al5gETR49zdXn4AzUti_3N3a6URb8VQKt37S_Bso4lg1248WVRUaVkLcVsuS_4uZ34G6sLzb404ABclCcj0SCqTnzzIw1kyy98BoZ-0xWZbyLfmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج رئیس فدراسیون فوتبال: هیات رئیسه مخالف دادن جام‌قهرمانی به باشگاه استقلال بود ولی این مورد مجددا در حال بررسیه. اگه بخوایم‌جام هم اهدا کنیم توی مراسم برترین‌های فصل اعلام میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31284" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31282">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iC9NPx70psNW5at3fXFr2f3zYFZydAxdXXSmoqMfA4fJ4dF2waDiNLI5TsiRDozA3EDPFyCKwzDk2Z1mA6L3kvx7Nksd8u57w1-ZR7yRpp-0T55AnUTaH2m7Z5jpH5iVrswfUpX77g5xtlKTv9PG_v2NimCQxSpByiGVx8Bf7X9tT5ANGTlSlWlLGlJNlTMeB4GehTbKYJ6-0ustdPbs7ktjpvPgr2O6-s0aPc48Y10pqcK7r-EiPBNn6iApFicd7IjyOkJKchoBAmrk2Rc7CuSJ_wfupTl4hIFHfD8-vnGmzKqR0f1aDoxqS1VXaHgXfCuZB37XyENoYMSVMU5DXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h78pdM4vmhxYIHKTIkNMI6wLGXL8BZtGZ4GQ3IeB74SsJkmTLgo7VPx1sSbiXe7WkiXfSZo_QSGj7DsDbPirTpGxCymvPQPW-c71kDJjBLSS-3OFjkVlNtJyIM8BzrKnoOrm8J22GgteFQ4BuKYjaCL3M9TuLzvC6NEcxzqkghf_CS5_lv7URp643wY112mJUxg7GPkWKmFc3Sj_DkUK89V6b90pHs8WcQUfwR76HCr6ZamR24USx8KKt0bYzDXih8woIG_yVCL-XBgcAzm62m8lPXlVVKDcyyXvBQvEOe88TcqFS7e5e0ol8ZZKEqrI9VM0obBx4SRqEP9AWjSOxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
قدمت باشگاه‌های فوتبال ایران از ابتدا تا کنون؛ آبی پوشان پایتخت قدیمی ترین باشگاه ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31282" target="_blank">📅 22:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31281">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJeQZ6fJDS7gMVdVyb0p6dM4ZelB9Lks5tN-1Zf_No4aIU_FMGcLTvut79MyEUOFp7wpMfsTn8usAzRYxNb2LZW8wXrp2zGRo4JEt1ppEuLUHdM-yuiGmq4mxRyfbqnJtVRkFeRMzK4dixM8dl6DAlBsiWqRdG290Ag-j4ahsj7jDsNQMgAhwxXUe9IdPRDL8OCFti0KaPwwocQtHE-4rF76BNkyY0OLUqt8irMJXHYLaTN59nfnDHbNPLp_TdYHq_KzkA89Onn0b0dApP4RYW9KoUoBZKh6U6N-zV0CwHBPxo4gBs1Fj35u7HAH-rBP2HmHt45s4Cdp0pQ3Ros53g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم لیگ برتر؛ دشت 3 امتیازی و ارزشمند شاگردان مهدی تارتار درتهران مقابل برزیلی‌های ایران.
🔴
پرسپولیس
3️⃣
-
1️⃣
صنعت نفت آبادان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31281" target="_blank">📅 22:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31280">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhnJLPOLCgaWQsIYEu-5h-3FDqKlKVX8sC0dsyULh-dQ24yogKJFJHEDgppWuCBM2KqXAokxvD3Zz06egdqnvWlObB5TOzHELATkjeM5YWByybuT6HXuKRG3HPmSPokC0vs0_ZakmLBFhrUWB9yjYWbkjS4_FN_65UN0bPP-eWNJPRJ1EWpW66nNAbZT89RXdp9J2oWtqGpac2XpJBF4GgilHONzZJen__-367ZkOsr3XhcE8ldMEiM2zHM6s9zdarRkncLwyPpor9SWlLJenPWeX4BFW0oTfPVxOuBqfZyoKIKTW_vmSpgC7GPqEEXXHA48E00CBXfxLNkr4TyikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دستور واتساپی‌شجاع‌خلیل‌زاده کاپیتان تراکتور به‌بازیکنان‌تیم‌تراکتور:همتون علیرضا بیرانوند رو آنفالو کنید. او دیگر جایگاهی در تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31280" target="_blank">📅 22:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31279">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🟡
👤
#فکت؛ کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/31279" target="_blank">📅 22:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31278">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ فکر کنم تنها کانالی بودیم که بارها گفتیم که رئیس فدراسیون فوتبال به باشگاه استقلال وعده اهدای جام قهرمانی فصل گذشته لییگ برتر رو داده. حالا هم طبق شنیده‌های رسانه پرشیانا تا اوایل هفته اینده فدراسیون رسما در بیانیه‌ای استقلال رو قهرمان فصل قبل لیگ…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/31278" target="_blank">📅 21:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31277">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfqIqR2hJ3gN7TNfqeA5TVBeeetPL6QCG_itVyIMIj54EAUo5TE5PniuG1Yc2Bm6Pg7kFF7RYoeUZRK6y7K_riHjea3iF_BUeTkIEofbLKlpmdMANisMqsNNDpHIdm6r15LWAIaoxyx-hIp4T9oHcYNc-r6pw5Xmzy5fHDcG6wkbxfAUQ_trdcOm24nsA8hxjI0S0kxbDbX3u7zXMEqWVQFB5E4yew2ZNWF-ICcX1toEbnk4wkO8XYq6dqFfavcW4eXbQP49GxvMSTQq6js1I9smuqXEpjFoUSzshZG5LmgnnDEsAD9DQLhh4oSkY_nGG3pHxiCXo-VQq5bYOexRFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدمت باشگاه‌های فوتبال ایران از ابتدا تا کنون؛ آبی پوشان پایتخت قدیمی ترین باشگاه ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31277" target="_blank">📅 21:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31276">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQJF7dW5IhHLndHXPF_Ws-IktJ0SzjFDX6mLk_uXuOPJK3e1uBtyzX2Dk3rhrpAv0zFz02THGfTynrUhV0yKjvdIwN0fDgdcMe590eTLlBfz5w2-cGfSDfqt2HfMFj3qEWrJIXAfYWAKaSJ-oGPNyv8bmu5sXk29lrGRhyWn2687rGacwuPk56LQwLuw5t3cMh6u42GMC9ah8toiD4gLabFfrRZJP6gxfvogDLTLqq4aG36l1ADXNPP18eUOja5F9kMBBD-2lr6ZoiaGnFFHTpIeFzw-gcxrdgyorpl7PhMkCcmE8C8VVwQpJzJ3SUx62g5gQ6obdiVdW_-mHlyEVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام وزیر آموزش و پروش؛ به احتمال زیاد مدارس بزودی و در روزهای آتی تعطیل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/31276" target="_blank">📅 20:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31275">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNk29e83U9ZlFwbBLoDUmU7LecXMY2aggjyzssiTQjy3ElY30Y9Yii5UHRNkPOX91jZjR43K8erPZdX4KFSUjCvYDsNSwtYA499y4ABRJkNvYq2QUOIknIRiSjxSsehnsU7H1aWxIf8X0DTglf6weCU8MHGUJXNp2f2uf0eYHUgcJOCY_gIYOaFh9Zs9142xOQmegCKWWlcqIIf7ikAD21ovgWeyYR6pIwHEjZCHFq_gDjrnZvzzQVJNvAK7T_qRI5Sui2fH7VuPkwQ1exvLkSYRPuGOLIoLy_QCtrSqv9wkmU1lmvogC5cf6WvzSNydIW2UUe8E6y0N1JIpfVEoqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ ادعای بن جیکوبز: خطر این سناریوی فاجعه‌‌بار وجود داره که باشگاه بزرگ منچسترسیتی به‌طور کامل از دنیای فوتبال کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31275" target="_blank">📅 20:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31273">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGfOX3gKjUKHFb0aBrTEidDKo9gx-uk7vVbx1loPOluEQHdhHPBppwLF0AGIcAwaRs2Krhd_7V_l8XhzKhydh8zUHBanbsJuK0FqJuP9qVf4yfThHHK9zlTViin2KJgIjsWoyRed7iVr3digw-Kgw7douc3Je04pWU6x_y6ZwtRqR0EqaPbvSYwEAv259-NXWZPCNjmPFA-jc0h_hJ7mJ00I_rwt7xLZDK9gkD8ZEfNxN_uVSz_51ibfUNZoI0-HyUO6_uS_pxB8uzF1rW3F9vA87gG20EzksPYBdUZveFNaUNQTjGWUXiN72yV7guzfK2WB-l-oIIPF8N9o1lD_Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TBLL_Bhv_oTkBZ4rY2kPpcyOrHx-ovsf73XAYXh-xizAwHNFddYhmLcVBCcd0cp64cuJHjda0EzMSoXcPOpa0s6NE0Jr_Qtp81MOi7Pq5HUKU4Ib73Ye6hbqObt6pT8i3cXVQ-t7OVMcUhYsgMdLsjrpFUew_hFC8fD6Jgl4T_hkUWgz5rh1yU7yC2bv_WSoD35yi4A0BtGzAWav9FV3OGtp9EievfcjTEBJhu0qez0EAdmONNRzaoS3iA9wvQe4mW-kt_MaffWQnuzkCffQV65dLjugVDsrjvhn0vsbDRcIzYS1Q9MuMklvbrfpvfgsX2BVqQEqYzpXahxUSSPphg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
تفکیک‌ گل‌های کریس رونالدو و لیونل مسی در مسابقات ملی؛ رونالدو 146 گل در کل دوران حرفه ای خود با پیراهن پرتغال به ثمر رسانده و مسی 126 گل برای آرژانتین به ثبت رسانده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31273" target="_blank">📅 20:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31272">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e9e6b867.mp4?token=jqbSjMocs6nrIyKDw4BZNvaXEoLq0ameghpaal40OXXe24wnYD4Zpcadd7TOxZBIfOO3DJIFwaJ00WU6TZb0v7v1hzBYP3GM-yn26zzFCzLzSRD1djr6NAzFmDSdaK4NALXz4jdl5nQyetxNkpKvwb78dj0D3At8QrZYsCCoZkcIKSO0Or6_qUUOX4BCBpDEQfDEXFSW74PcVnrkZdMEqOUSD-N9NS78sQmeFTqBCVfIX5O4bcLbE1Dy9ePQZv5_h-L83eSws5oFabIqD1Rnz_eK5zh0-Pm1whtp2g4ueLPgP5X15FGnqId4itLHF5puuPHkn2unihy7zvgR9NBeLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e9e6b867.mp4?token=jqbSjMocs6nrIyKDw4BZNvaXEoLq0ameghpaal40OXXe24wnYD4Zpcadd7TOxZBIfOO3DJIFwaJ00WU6TZb0v7v1hzBYP3GM-yn26zzFCzLzSRD1djr6NAzFmDSdaK4NALXz4jdl5nQyetxNkpKvwb78dj0D3At8QrZYsCCoZkcIKSO0Or6_qUUOX4BCBpDEQfDEXFSW74PcVnrkZdMEqOUSD-N9NS78sQmeFTqBCVfIX5O4bcLbE1Dy9ePQZv5_h-L83eSws5oFabIqD1Rnz_eK5zh0-Pm1whtp2g4ueLPgP5X15FGnqId4itLHF5puuPHkn2unihy7zvgR9NBeLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌های عجیب و غریب دروازه‌بانان باشگاه‌ها درهفته هشتم رقابت‌ها بعد از اتمام فیفادی مهر ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31272" target="_blank">📅 20:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31271">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnARFsF6EAIX2TpmvPriUfW7sDj3QHjKLjeeShpZgVrNVUgYfbozM1uQAOL9W3oNZlHT-odG5BifBP7sP2RO71uCDnccHF5vB0Y9QACaCR6esdFsGnIozpnuF8uITc884Kdsqw0MMLDekBslCY600-dMMuwHK5XIKmPS8-w40ruVglJtYFVkIvYM8wPbXrV3hoMec-12V7-6VI0KcHLsTaJjyozIveKfmAlwDcVpfMCVyE3K1EiR1jPQgTaBIl5Uj01jEwy-pswYLHgknOzje7mECDICIhFmyGx4oZceYAy3xP87QyK0WWnLfC10lvKyOhFbvH-WuiFVh8hbspPZlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی رسانه پرشیانا؛ کادر پزشکی باشگاه‌استقلال به‌سهراب‌بختیاری‌زاده سرمربی آبی‌ها توصیه‌کرده دربازی‌روزدوشنبه استقلال مقابل الغرافه ازآسانی استفاده‌‌نکنه‌ تا مصدومیت امروز او از ناحیه ساق پا کامل برطرف شود. بدین‌ترتیب‌به‌احتمال زیاد آسانی در…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31271" target="_blank">📅 19:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31270">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان هفته هشتم؛ البته بازی‌شمس‌آذر با پیکان و بازی‌های معوقه هفته هفتم بازی مونده تا جدول رقابت‌ها تکمیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31270" target="_blank">📅 19:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31268">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ievn2Ia_FAN6Lc85OT3rJ7jjz17Syi3sjf5jK7hApyL_2dEHP-BjUTyn0cJnGyQsSlZyDdYJVJws_ggRUEs9m_orGOlJu8CDgpXu7C5PUWXE1p78zTqbcFvWm1Q2C1_dylqLYj_E4JmA561jBgMC2kJVOcupihzciTLDJqlW46hU7kb8aPmmkZSIMrv5vvP07AV8D28If5Juef90gRS3zRsXM70daJBzcK6E3fl5S5r1Zm5Ej_DffXwopJIMNWrtu2crb5ZWIlM5syIOhl5JGgpW2kPSJtJYrhewmnsn8oIY-jsNGqanzypK9WzGlcYQ0EdExTKhTP4vBwgYnxERKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ وزیر آموزش و پرورش رسما از تعطیلی احتمالی مدارس به دلیل تهدیدات جنگی خبر داد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31268" target="_blank">📅 19:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31266">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cyFBFF4JMDjY8QGNCa2MdYDpGBUiJ5ResQMxVllUACPBc-a40W4L5XL4Hse8FiVZWbw7XYYXeOLBW7lDVS9zlfj02ghRsAZFYxp-H_ooVYnaZn6vGG_1-48ZexuTBck9Ml-KuL0kcf6jS60CL11LhhQRXlWzCul-bWTlJvAY7uB814b80aF7A-LF2_TDZeKhQTYzze6XeggOaXZerplwBhUWxrOPVgzYsy4NtNv5ztJW6ZX0Y9VNhEIOgW8mVXL6VLzv61cYuDqZ4bRfnyZ1jfcToUgoT03uzed57Q3DUDkviWDsr0IAGjuSmoKttGSeoLPIRK0lMy-TuRmW_vZY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UoU_nTxQxTOF9JVTYqI6MnCX157JPGn2DkqIZvj1kCRY2ibOHroMcc6AgqfFcjvAv0TyWVOl5q5HQ-16UZ59kgzY_bGMTdh8M3cW8vvz-Ozx90-pmPvpaGe5UYu-d7cnv05br0fK2rKxc-YzdGPZuFwkXGAoNJsDkswWuOHklQvNNrYs9eigSVUcWMgFA6OmIwyFR9lbd-cWymPwAHtRAHnLLupccsB_W1XRZ-2Izuwdvz6n7bn8xOZ_xqjdKWRnUP6XMwHvR65yqQft0YKWASh9E-vffN9C29xNrY7SwH3KkDT5-wBzscsgHx0lAm6JAqbP-ubWt2NsP2VVaErXhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بانوان هوادار پرسپولیس درقلعه‌حسن خان.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31266" target="_blank">📅 19:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31265">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO5V0JleN84hETIaTuZ70VfSu45pApF5J1eoeGUB9_ZdsfPPIj9rBl7F9gkj6Q5evgNwPKriUCjs_GKbJCPE7DK05PIhngsVgrISL_LxMyrLP0qlFk-TH0Vxke2JFJ3g-2Y33XSRsO2iPzrmKPvGth4RyORDHZcUx6nA1FJ9CMILyv7elyqgH1vGmopd-St716V-qUmsNezRZT4HjKgE__p1eNzrE8RM4GctbsbzMeTE1Qhu__M121LYs3YVRBLROPXP_viw26dFIuB_zKHorJXBU5jd9tACqy_uoH0oe8Oxps0DLGv1gZBp_kcOwTe3y-ubdKZKsGw2OdTfG03vzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم لیگ برتر؛ دشت 3 امتیازی و ارزشمند شاگردان مهدی تارتار درتهران مقابل برزیلی‌های ایران.
🔴
پرسپولیس
3️⃣
-
1️⃣
صنعت نفت آبادان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31265" target="_blank">📅 19:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31264">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYitYc3lgpR2HEx3OeY8gfRNw1DuBo_D192kApt8Ocq2RMBKRrvJSxLW4BMeY8fY-6Nf6tPsFrLHsBeTvH0JT07pr1GOgpWLEnprBi4Zc9xLIssVvmpdoH4R4punWwJ_Qi4B14DHXWjAYyBjs4suU4nl9rCuNEC4_tbxafnegEqg7uTfV6vXsAKxV8ctpfuRKb3To_FFizIyA4ISTQp9ZGZZF64uRbtmQ3YypQgHeV3W5wr7glijq_ERrzHmf1Ix9ugzLoA4MVejm0oG6_aB_JW9lc4kJOn6PjMVCY9IDENgL6lE_c38P2hGSo_bk1F33dyxbZKOEMqDzAH3SP_8lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم لیگ برتر؛ دشت 3 امتیازی و ارزشمند شاگردان مهدی تارتار درتهران مقابل برزیلی‌های ایران.
🔴
پرسپولیس
3️⃣
-
1️⃣
صنعت نفت آبادان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31264" target="_blank">📅 19:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31263">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpKk5UEi13-_bniJqZVaR-n0at28vtfRfsx3f9ZsFVkNH1KZzgAGgQduTYvlgeVEGbRoJzK9REvPTIKts7_TPfsiglKf-kwgmNwvimWIS5qQoZaTCXLhZ2raG_JH1CeWoHDaNz9pVoIms_I7vIokzKu-jFgkiOnQgEpvfBVNPzI1gkCmtVAdm-q3HRBGf3K1SAODb3rXCFjU0mPFMqSN1fGnN4Z1_cK2tZAYl_iVWqPNU42aUC4Yv_j9YqJAVG-NE73k4FpnMcSIuGK3NbjIzhNsiA42N9G_5hz2Vf5NXyiAcYTmyyFi009t2BdT8-gWDYLyOx3RSb82CokBTSAdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سرخ‌ها روی‌کرنربازم گل خوردند! گل اول صنعت نفت آبادان به پرسپولیس توسط باصری در دقیقه 66
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/31263" target="_blank">📅 18:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31262">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866119f609.mp4?token=X8v5RDOYqWonQ9aVkuJA7vq09gn1mbJJmzvW-gGrGTBxQbTJyUAwYDdB6VMW-B6J9wA1uOhQqajPBtDIaBv4JJs_nQoJ1eAO7DoHu1yfVbGVENF_4Tg9iPkJYGVivyMVJj9ByD976sztj3Gm4PiezYodotXXjw_N-taugD_d7rIEVRFBidl6tBm07mpEaP7fuyV8t72poqP15SOXfOrO6DXN7ESpr76BWfsVkhtwePcGBhwcV2D58xGffhIzTWkbN3uGoEZ4PCeoKyMVoungzUE5fzvu-i9OqCA6rEKtk0as92DtU-rV1oz0QnfxMa032qoa-VZR-jNXwTCb9hSVbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866119f609.mp4?token=X8v5RDOYqWonQ9aVkuJA7vq09gn1mbJJmzvW-gGrGTBxQbTJyUAwYDdB6VMW-B6J9wA1uOhQqajPBtDIaBv4JJs_nQoJ1eAO7DoHu1yfVbGVENF_4Tg9iPkJYGVivyMVJj9ByD976sztj3Gm4PiezYodotXXjw_N-taugD_d7rIEVRFBidl6tBm07mpEaP7fuyV8t72poqP15SOXfOrO6DXN7ESpr76BWfsVkhtwePcGBhwcV2D58xGffhIzTWkbN3uGoEZ4PCeoKyMVoungzUE5fzvu-i9OqCA6rEKtk0as92DtU-rV1oz0QnfxMa032qoa-VZR-jNXwTCb9hSVbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اولین گل‌ستاره‌ ازبک سرخ‌ها درفصل جدید؛ گل سوم پرسپولیس به نفت توسط اورونوف دقیقه 85
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/31262" target="_blank">📅 18:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31261">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aaaacac90.mp4?token=F7Durz8R3qNcCrAqTDCXXXM-JoF0chDe4UHuJNeGsb1BAdJLzW-APgXDvD5fgS0F7qmI-Lp7-lHRUQfV06YB70ZCwEkd70OvH0tWUTxGFugNF1zbPJkV5IH0Vxk1OBeSjMu9_id2vrirnp3k1N3KWBn8vMWWTGjpxINJlzZbIOsJlKmWxz1z5bCHpEkElICSYd0LXoheG8_U7FY9pbQbCuQPXYNnYbrbDts0H-Tphd4F9OfD5CFpe3R6QSzE9tfJ88GiUxzMsfxFZVdl0muD_SuLUMjMmdizdf6uFEHLx7SidmknpYviVZIbDsepYH2E88Ig_5L6tP0XolWRvH0W7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aaaacac90.mp4?token=F7Durz8R3qNcCrAqTDCXXXM-JoF0chDe4UHuJNeGsb1BAdJLzW-APgXDvD5fgS0F7qmI-Lp7-lHRUQfV06YB70ZCwEkd70OvH0tWUTxGFugNF1zbPJkV5IH0Vxk1OBeSjMu9_id2vrirnp3k1N3KWBn8vMWWTGjpxINJlzZbIOsJlKmWxz1z5bCHpEkElICSYd0LXoheG8_U7FY9pbQbCuQPXYNnYbrbDts0H-Tphd4F9OfD5CFpe3R6QSzE9tfJ88GiUxzMsfxFZVdl0muD_SuLUMjMmdizdf6uFEHLx7SidmknpYviVZIbDsepYH2E88Ig_5L6tP0XolWRvH0W7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
سرخ‌ها روی‌کرنربازم گل خوردند! گل اول صنعت نفت آبادان به پرسپولیس توسط باصری در دقیقه 66
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/31261" target="_blank">📅 18:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31260">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd9e6967b.mp4?token=GFAxrf4lXC1hLwBfn9aAmuGZOb-WJjzxCLw_PdFBUwlt0HNJjxJxKqa1QyohheglJ95i6VA9v1TtcpDclXOKlAVsApXra7xSz_fUNfHNhFeOVX4MPREwgS47rJ8L2c3J7HaOrv3-EAgBj5AzM8OPPiJRiR7gfd37rju1LfYQsiNeMcJ0kW7_OljWzMC2SNESSkhSzqxTu0rKtDjy3qoQXMgFqy4iRvd_Ppg78ly9kJKAgtPs4l7ytTf0wBiSvKlnQ02pVP6phNPkQ6Bc9cJnZaWtcjiKSFEejhPQRcb3p6jvwZqPpci4bAx-BADYtEAG52T4zPybS3KjyUDKadukgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd9e6967b.mp4?token=GFAxrf4lXC1hLwBfn9aAmuGZOb-WJjzxCLw_PdFBUwlt0HNJjxJxKqa1QyohheglJ95i6VA9v1TtcpDclXOKlAVsApXra7xSz_fUNfHNhFeOVX4MPREwgS47rJ8L2c3J7HaOrv3-EAgBj5AzM8OPPiJRiR7gfd37rju1LfYQsiNeMcJ0kW7_OljWzMC2SNESSkhSzqxTu0rKtDjy3qoQXMgFqy4iRvd_Ppg78ly9kJKAgtPs4l7ytTf0wBiSvKlnQ02pVP6phNPkQ6Bc9cJnZaWtcjiKSFEejhPQRcb3p6jvwZqPpci4bAx-BADYtEAG52T4zPybS3KjyUDKadukgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تثبیت‌پیروزی‌خانگی سرخ‌ها؛ گل دوم پرسپولیس به صنعت نفت توسط علی علیپور در دقیقه 50
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31260" target="_blank">📅 18:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31259">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db73f92ec5.mp4?token=syQ4vpSn6egFCOc0TTIwQErq0xttnBIfaWLiIDg8ARgJgPN39hvUcw9nBG_k-qWJACwkgXmbgC2QayAGXESxjV2NILn6JZpe18uycOrFUIW6EM1-Cka-i5WzugCydJRAsgMASydn7zSJo3fALO5pS3fAZADYhxzcGWTCpwTZncJ-hE7H5_7jf3CxACyuo8zosoEzqQR3L_vhcdfvIzSkylThVPpGcbk6DTKaPephDAq4B2bOkuQ9qmM2aBeVMjzU_En_RC5Mjdh4uXo6BEpCK-ZIhlsgj5EIAgNdDhx4_D_5M_D2ZU5vOy0iyfEZuLpbxC_cpUjrJCr4FmMO1qpdHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db73f92ec5.mp4?token=syQ4vpSn6egFCOc0TTIwQErq0xttnBIfaWLiIDg8ARgJgPN39hvUcw9nBG_k-qWJACwkgXmbgC2QayAGXESxjV2NILn6JZpe18uycOrFUIW6EM1-Cka-i5WzugCydJRAsgMASydn7zSJo3fALO5pS3fAZADYhxzcGWTCpwTZncJ-hE7H5_7jf3CxACyuo8zosoEzqQR3L_vhcdfvIzSkylThVPpGcbk6DTKaPephDAq4B2bOkuQ9qmM2aBeVMjzU_En_RC5Mjdh4uXo6BEpCK-ZIhlsgj5EIAgNdDhx4_D_5M_D2ZU5vOy0iyfEZuLpbxC_cpUjrJCr4FmMO1qpdHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شروع‌طوفانی‌شاگردان‌تارتار؛گل اول پرسپولیس به صنعت نفت آبادان توسط تیوی بیفوما در دقیقه 5
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/31259" target="_blank">📅 18:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31258">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjjS-LULEfVvyiZe1JZODxg71Dh4C5_2s_36XLTTNwtA5EByhHlgq3JPnuQdJu7mhI7bnQYy46_TiVlb2uQb9o9UisEMski5wgNOi-L2MURX6h7EKvmRkhNwBEQ9RGRSkJQH6KyX7Vq6Txs9SqBTBc6neIgATXw16yHwDqjLUhGbyTSXlQ1mCSxp1-mZB31ICW1dVILRxYotCAk03mfRDVEhxmhSkXFwMEbNIh6EXAB2n5yIIC-07bnmExkMJ1OpyV759VBujai4c-MEjN5L4F6ZfqADydtIlpdRWQHSCghn9rb2AIx0krsTC9JWd3QXQQwvEHMako5TfqXp4ebJkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
تصاویر جدیدی از بازی GTA VI؛ این تصاویر در بخش موسیقی وب‌سایت بازی قرار گرفته‌اند و نگاه تازه‌ای به فضای جهان GTA VI ارائه می‌دهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/31258" target="_blank">📅 17:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31257">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0462dcd97.mp4?token=ZlXi4osGunxgax1qPFOVJAnw8f_blNB_Ehy_0ZSRSsqljglREpqKD8UULSFc94KGT-6IKVQrgV8F6q6IV4NbTf1p7_k_ExnLeAXbnsBAWzMfu0XnPvHXcM2ulWT9sYa53iNeDqXkmLJ3bdpnlPlR3dA78QitpOYE4StEhtXdPQ8QIz0Bnggm4EFSYrvzrpP7O_e5vGtdy_GmOlbuxCT1g_XzbcmAtyROPMBAtlTf_8bsbjm3zH4BCx3HTNQjFlL6DpSLOvvtAa0cwYxNlZ5czfogNbqlQd4f1JAb_jY8otBtKgd4tGBTsQklq9DJNPVa8pgfptj-ReIGug6e820_UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0462dcd97.mp4?token=ZlXi4osGunxgax1qPFOVJAnw8f_blNB_Ehy_0ZSRSsqljglREpqKD8UULSFc94KGT-6IKVQrgV8F6q6IV4NbTf1p7_k_ExnLeAXbnsBAWzMfu0XnPvHXcM2ulWT9sYa53iNeDqXkmLJ3bdpnlPlR3dA78QitpOYE4StEhtXdPQ8QIz0Bnggm4EFSYrvzrpP7O_e5vGtdy_GmOlbuxCT1g_XzbcmAtyROPMBAtlTf_8bsbjm3zH4BCx3HTNQjFlL6DpSLOvvtAa0cwYxNlZ5czfogNbqlQd4f1JAb_jY8otBtKgd4tGBTsQklq9DJNPVa8pgfptj-ReIGug6e820_UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از وقتی که مسعود محبی مدافع تیم خیبر توسط رسانه‌ها بولدشد و باشگاه استقلال نیز به دنبال جذب او افتاد هر هفتههه داره سوتی میده لامصب. این چه اشتباهی بود که تو بازی امروز کردی پسر خوب!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/31257" target="_blank">📅 17:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31256">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/499a1fc96c.mp4?token=jWZFb21vr5zXJ-5y9TDsmeFOUz2vqS5PKkVfrGhf6Z_fnTGR_6DBDX5tdhDpVcR3HxmnSLksyjg9HaPIgAAJyHNh7gOk5ufQbZMdIqKItOu-8ULUTwb1vJ-XGL3PI8heZ2iN5eIqztAUroKfJ_SoJOr4cwVCBJBI1xUu_2yOBNaWi77aCFA3tiD8QsFyUaozepI0-_ZtgeYPS_WKglXrGtTqXLr-2Dxvt4hcEORpVn5fidOc9fb-fpEsXw22hcK7-ramc3tcywTTVnbcqxQqqRfhvaOja5gm6mL1C_xo7hpc2iKn3tCXoX0gWnKYCblN12CvcXRLSzMdb_lBK6xbuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/499a1fc96c.mp4?token=jWZFb21vr5zXJ-5y9TDsmeFOUz2vqS5PKkVfrGhf6Z_fnTGR_6DBDX5tdhDpVcR3HxmnSLksyjg9HaPIgAAJyHNh7gOk5ufQbZMdIqKItOu-8ULUTwb1vJ-XGL3PI8heZ2iN5eIqztAUroKfJ_SoJOr4cwVCBJBI1xUu_2yOBNaWi77aCFA3tiD8QsFyUaozepI0-_ZtgeYPS_WKglXrGtTqXLr-2Dxvt4hcEORpVn5fidOc9fb-fpEsXw22hcK7-ramc3tcywTTVnbcqxQqqRfhvaOja5gm6mL1C_xo7hpc2iKn3tCXoX0gWnKYCblN12CvcXRLSzMdb_lBK6xbuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شماتیک‌ترکیب پرسپولیس برای دیدار امروز مقابل صنعت‌نفت آبادان؛ علی علیپور، کنعانی زادگان و ایری بدلیل‌مصدومیت این بازی رو از دست دادند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31256" target="_blank">📅 17:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31255">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7613725c1a.mp4?token=LV5XnRUQ76YozcPK4DqRDDkcz0QNe3i4gQJlvlLrtIlcxcPOUsGYEuWj3pVQPvxnSFfO3-ugEaBG-7OEjZKrGD9d74-KiH378E_5PAtnm1LBvQ1o1Uv34-cWGh71tFY_gwKqb2lgA3rnDUpOIwNiRDKaem7xE4H7puG0qAy-0UhTLQJlKbL3A2CZbVlxRtlWDs4wx3kZl7_Ae_cRc0N6NCVAYTjWUB7R6cTXAyPfN3R_lZdGyXO3sG5AR36cFTO-wqJAED7cYKp4y19J40-gEwnx7Qs28fwap_Y4T6viUlCETOHEUvNJeJWHKwIV0tOZmrIxlEW3gJNaOg5RUz_nVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7613725c1a.mp4?token=LV5XnRUQ76YozcPK4DqRDDkcz0QNe3i4gQJlvlLrtIlcxcPOUsGYEuWj3pVQPvxnSFfO3-ugEaBG-7OEjZKrGD9d74-KiH378E_5PAtnm1LBvQ1o1Uv34-cWGh71tFY_gwKqb2lgA3rnDUpOIwNiRDKaem7xE4H7puG0qAy-0UhTLQJlKbL3A2CZbVlxRtlWDs4wx3kZl7_Ae_cRc0N6NCVAYTjWUB7R6cTXAyPfN3R_lZdGyXO3sG5AR36cFTO-wqJAED7cYKp4y19J40-gEwnx7Qs28fwap_Y4T6viUlCETOHEUvNJeJWHKwIV0tOZmrIxlEW3gJNaOg5RUz_nVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بخش رسانه‌ای باشگاه خیبر خرم آباد در اقدامی جالب شماتیک ترکیب این تیم مقابل چادر ملو رو به این شکل "یه نوع شیرینی محلی" منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/31255" target="_blank">📅 17:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31254">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mfjr-TtLTUgdFXJaeGym-0ErQrtfxtSM8lAXXJOz6YYoTo8BYnYUscRbmDV0w6Rs__IrqhPHIe1iikzL35BYugFAYFUtcoqR3SoqCwlav9-R2keJUddCz71cqle8q03XapEPY9JymaFji4bqcgMHKDdQ94SpzFVQb_ste6lfFz38uFW_KDDrEDZJ5YxyszTjEVZtF6QRvr_GbbnEcNYk1gvcfOIaoftptuDBP1LESt4ToZFb3VT4SAuleGAckMZmdgRz04ywpeJJMbC5JTCmcKPNNXax2esA7URfTKeZdsntzrQX0Ga0t_Za2BAuCyGOV0cU5Ra0FP1wKrnJocJkIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان دو تیم پرسپولیس و صنعت نفت درهفته‌هشتم لیگ برتر؛ مارکو باکیچ و دنیل گرا از لیست سرخپوشان برای این بازی خط خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/31254" target="_blank">📅 16:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31253">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
#تکمیلی؛دستور واتساپی‌شجاع‌خلیل‌زاده کاپیتان تراکتور به‌بازیکنان‌تیم‌تراکتور:همتون علیرضا بیرانوند رو آنفالو کنید. او دیگر جایگاهی در تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/31253" target="_blank">📅 16:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31252">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwfSqK8MYizz2gKfKCuovOGsCbWRO4hxy8Iztw_Nl9C4FRhRZe9fmxYy6WwCfhYPie7QtmzR4E-Ny70Gy9YIPAEHwxJ51DPOhzQzKTNPhVihacDce8XwFyJgo9cvBBfk4a1d7IBrcoE9Q7netVP8lgcBocU7TbvY8wllxd_vTTF_5ahqq0gCVp6ysGBoTreeqoSSQZmS8cPvgdbhEEnPp9kG0HiherQITqNNRCOdV8QsANIB7VfwsUadS6M7LljoiITY-AcyK2F6IJ4eVgKXrHxtwCZdL0zxut5DKCwY1hlY4LoYiV70Y71YYqjW4CoAvqaV6OsWzYh0ap4fdW2QVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛ ترکیب تیم پرسپولیس برای دیدار امروز مقابل صنعت‌نفت آبادان؛ ساعت 17:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/31252" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31251">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImHwxb0tGiTaoUNFuCYFKrsZPh6vogBjEB04sjv-IOTARb1193MnqC3WwJuznGt0dBP1KsdH1Imqz7IM7l8sFAIsphfN18M0SpsCfB1Sq7kF9q-Ee5IA0KrA-OPe0592yVkZVym8fRfmOjFkJDCsO4eemZmHnS3vDJcpIX3EdhC8BGSpnA456YrY6FfqOlfqoJFfUhLAOQmTmJrqsIYtoDgPAPh7kpDu9HzS7a8K0EFMPS8no-WthHDc5fNW3t_92wGg_xClXVVYBIsrnLiaFczkpeKC76Y88SGdB_MSz0go9bpZmXkPe7s_edK7juJzL7EWopnaATN6-FnIE4kwdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ همانطور که‌چندهفته پیش اعلام کردیم که جدایی دنیل‌گرا و باکیچ ازپرسپولیس در نیم فصل قطعی شده؛ مهدی تارتار نام این دو بازیکن خارجی رو از لیست سرخ‌ها برای دیدارفردا باصنعت‌نفت خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/31251" target="_blank">📅 16:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31250">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdRzS_J43VDdhWOrxtDUiGMPQ-U_WjSL-zCc1_b7IAg6xZf9QOQFh2Q9n6cVs47ZizP0bPEM3JShScAWr9nq30Ce-PNDx3gjDnHJqrvruY0vT3fh02-tKASxSbJjD-gBYP2Sew0x9bKrDKR4KIsvmbaAUqtXLKmKZSuKla5em42G1nI6H9e7z-Px8I2n_uUD7WUFTzwbuQKs_DWxCIYETl1KXM9-c2HgAYFhCVvyPlR8jHGHa4z4I20X_18tLBsvE4nZ-fG1F2uZIv5YFFDdPKOrS3W-qWZkkQykFf3QTag1Z9LgY8wEnBjMyHvSpLGbfZlf42HoWM-GzMDhFBs_pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
به احتمال زیاد پرسپولیس امروز عصر با این ارنج به مصاف صنعت نفت آبادان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/31250" target="_blank">📅 16:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31248">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Du6kYk89cSMQqqnEHS3bBzB4UE19ZlM6_7zr9p-tLtaWAqCHOSzMJzsyT1s09twUwWS4DnWRccgU8bxsNbCCCLtnyMsUxTzC5Oe_ygaNLkiNltuIWwz3GhRtlKl6WiL14Ga-MFl6CNb4fDtbk6g6LI37xq8fNXYdfIvYYPAaujPmeb87z8DyuqLE03IsOTSr3qLLLBI7z22p3-tChK6soX9oChpbtXyWGoItIFLWiPupIoPThQWtwCjJ-9QMvqKanWXH3v9zlT4DEgNf3RTGfcvSPhgjVDEmGE0GjQqToaWSf8uJY0Fxag8gy_sIVzKsDj-efjz3-B8Dur3iCB_k2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Afo0Jkxz-NuFDraFCjOn-_Xooz1NiE1-FHzMpj0AFrMaORYKeCVBHLCnapRXoSCD7MEamRd7m-h6SeKQxTsr9XPAKdjYL5zYUvBEnq9O8P2VbTnXw7S1Cyvlpm_gln_SBTCiSexIzgpep1w_Hpn64IbNaMGBKiL6JQd7pcx-VPW7m0LKVkHhihaBE-IvuTqPwBapgkofnvYQzDDbZnFxUmbSo3pYPsV3rgSEclp-7fErUny2PrVhJdCE5NYxcG6cve5E629zUbdoJSHr_BeNexp3qHTYnclq0cKlU9VQyh1m3yKGufoG2GK0v1i2fU7S_T0SgUlMjOBGI5VNH2wwQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تشویق‌ده‌ثانیه‌ای‌لیونل‌مسی شماره 10 آرژانتین و ایستادن به افتخار او در برنامه ورزش و مردم بخاطر خداحافظی او از تیم ملی فوتبال آرژانتین در اوج.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/31248" target="_blank">📅 16:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31246">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLhg6x459T8l2DGcs1oxCeFyR2XmmgRyepvGd6fnbc6rzYIjX9Gc3x518oyFWkYbr19YRzruhLURXEfQTvwCKL813QOgIAAoG4X27A0-_DxX01pIdtWeU4HoieuOuNAcUGQS_NBqmPMTQNlIbmJIOz_U7dW5yGOAykF1aZ3nRxoDj3oIklnzCR7XVcqgTHREoO3i--kyzkCzsi-0V53FpYYhdTFDrq9L2PZ-csK__rBY6PLqo7LogKiotRYxe_Zp01aChsItkZK_CRgqhbQC08aQNdzXoOpuqxp8FnV-ukHpZ8Z50XPNTMdMD_BbKfmcgvuYPQ3-ywhBx9D0lIucKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیمار جونیور، گرت بیل، محمد صلاح و ادن هازارد درکل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/31246" target="_blank">📅 15:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31244">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2089087958.mp4?token=bOvFt2QKYy5BpFH42H5_067qFsL-zQfe4UnfuEMrl9FFlHEBSmqRrmP_6Kx8S53ujvpf4u0K8mX_6T9LitUgBZZCW2BZGdLfl9gsTsm2f3uMQjncZHUFnLkaMvdtVt_NxH0niaKD8KrkVYrycvNBZ2nciYSAW22VIMFznmu8pDJUMCpIa1aKVSVsAXqz2bjEg_alJ-XvYVHs6mxnLr4BPyxEOpIohIKwzt6dL83GpuMoXPX82jaukvHIl4zS3O4Os3QUuXNmfnuYOlF-0eCO47EzuvJSTy4qqqiK7Gc1PD_TB1drhSmO6DHlEwj3nV0roqoEErFL32dcEp1kH2kaqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2089087958.mp4?token=bOvFt2QKYy5BpFH42H5_067qFsL-zQfe4UnfuEMrl9FFlHEBSmqRrmP_6Kx8S53ujvpf4u0K8mX_6T9LitUgBZZCW2BZGdLfl9gsTsm2f3uMQjncZHUFnLkaMvdtVt_NxH0niaKD8KrkVYrycvNBZ2nciYSAW22VIMFznmu8pDJUMCpIa1aKVSVsAXqz2bjEg_alJ-XvYVHs6mxnLr4BPyxEOpIohIKwzt6dL83GpuMoXPX82jaukvHIl4zS3O4Os3QUuXNmfnuYOlF-0eCO47EzuvJSTy4qqqiK7Gc1PD_TB1drhSmO6DHlEwj3nV0roqoEErFL32dcEp1kH2kaqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
شعرخوندن‌بازیکنان تیم ارژانتین تو اتوبوس برای مسی : "لئو تو مثل اونشب تو قطر جاودانه ای. مارو ترک نکن همه میخوان تو بمونی و..."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/31244" target="_blank">📅 15:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31243">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otqvyL00mN-kAgxVjNixDpj4WgDCbvT4hN3hyX78eDhXInKszHLIJCUyAXBCy75wd24M_R55S05Hca7R39hMWXgpJoPGOAGyK4rbDldNiCuXT09qLVSEcNBJn190tkcLZVoWRmvTuSpFL9Tg8oMs6I5crPHZRw4LiHu-LMZ0b8cttmrnliBD_9EoV97edqHXpAVzfRamN90o1soIU3UgaqHUTOk9HVnv4Dgs0qRN0eBQ7WozIzaIp8q_fSCS4zvnAeWejZ4U09ZDDUGAmJKCvNUsjzgYi0kPRf6ErcRdu4a5w8iB2QSTO_pdjFOsu0XT2w8OmxGcokyctPWoSGG31Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
🇧🇷
#تکمیلی؛ با تاییدیه کادرپزشکی باشگاه بارسلونا؛ مصدومیت جزئی رافینیا دیاز برطرف شده و او مشکلی برای همراهی آبی اناری‌ها در بازی مقابل ختافه در هفته هشتم رقابتای لالیگا نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/31243" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31242">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33992a38c0.mp4?token=V84UYcxW_VAVJwf4Wl3E5wr9WAPAA5Dut_CM-PPnMXQANwb9DOOFKB9EYcWqvCbRsUG12GyCe-Kx_R5kUvrdRoEFlzCR9Og__B2C4ZAj9lqyBx6_CtZVYcGLwIHqiJHgQRWPgmEUCiI1HlK6tGGRmPFveM4yx3_czakoHkGAwRlnPvnwa3BP2g8wEgHeDq5XksuGuN9MgWlknoAl0qFvAy0m7RIYk6HVuHi2Qr6ITSOj56sa8KM7vseUvakI0xDNTDPgcPlAZuAavcKZNfa2bk04IG4WZexG7gUjkePtuH060iBeW-Z-X3XMWVBE4VbgWtSoOkFsN2tzqzZPQs18gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33992a38c0.mp4?token=V84UYcxW_VAVJwf4Wl3E5wr9WAPAA5Dut_CM-PPnMXQANwb9DOOFKB9EYcWqvCbRsUG12GyCe-Kx_R5kUvrdRoEFlzCR9Og__B2C4ZAj9lqyBx6_CtZVYcGLwIHqiJHgQRWPgmEUCiI1HlK6tGGRmPFveM4yx3_czakoHkGAwRlnPvnwa3BP2g8wEgHeDq5XksuGuN9MgWlknoAl0qFvAy0m7RIYk6HVuHi2Qr6ITSOj56sa8KM7vseUvakI0xDNTDPgcPlAZuAavcKZNfa2bk04IG4WZexG7gUjkePtuH060iBeW-Z-X3XMWVBE4VbgWtSoOkFsN2tzqzZPQs18gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهترین‌نمایشی‌که‌یه‌مهاجم مقابل ایران از خودش نشون داد. استپ سینه‌ هاش آدم رو یاد پرایم زلاتان مینداخت. همون استپ سینه‌اش رفت تو گل ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/31242" target="_blank">📅 14:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31240">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQY8b7PKcdHsId_BMAs9UJi96ysnNR4_Bv9IEKD6vbklavM7NW4UGZRS68RpYmSZYLD5K3WeIwq3aAMKm1MB_sLD0-MsdzN2YfpDj24Q9BA1h6pvKwC2ynsfD1aYDuGuzF30kVJUHRfFY8cKcJn0RTFzNA-5iX5eAgcEq4-NR-1yMzAc8EHBLkrMxjpx1g2Ee_v-q9OK2PoLzIoJevjmp-rcM_3F8kMh_hkK5260AP6GyRtuE7FnnHpk8Q8mvsV22PdXYwUCRLFXhi_VCXQ5AALdtjSLjS3HD0vM7m7MdQVBI1onw9XDPpd_PjMBjuJHB8a3yrchloCvqGjzCMjJfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k5xsPLbU6LnGa9Qn8KkajnyLBvXWUgf3qULTouousj0M08y9FEwkY92rL_wyj_gLkvt0QOcQLpj0D9cHuBIE4pcupGmadBM0ANdtDTVCqjl8O37La4XqWK9RxCVxrLypRETnY_yDPsxUCruKB8Zz3jPM9vTsOlIphfBJm-xGgdYcuGRt5JTd9I7jmrMLNiq7A9l-jlniNc95ogzk40M8EG95QRi4EhFIsrcNKN6-kea3oe7Kxaob6JDoCbGc9TBx5NIMOceShrPV-XkyMAqwFhwXK0EvTALzOw9d9R_qpm15im9UNYYN-sd4AnO32zLu4bE9hnH9GC9ncsEB_PzOxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
حضور بانوان هوادار تراکتور در ورزشگاه یادگار در جریان مسابقه روز گذشته پرشورها با استقلال.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/31240" target="_blank">📅 14:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31239">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5gi9piKYDMrDv9lLpx-PKRnem2ySLEV4CEAKDXDF3aO1AA5xSJ4DhI4BKv4LgvgwEPhFSdiNkpOvKqNXzNc0NoTSKfAJDoNdGqZEjXxC1D1uijlQ4Tv2Ben-vLzbyBC7w3CRok5CTyEOQEPfMLZl79YvjKDROTcRjvxF4PMFAVPZbiyBTQEXuiuiy_7zB9vCSBrsSiIiczg5-S7utw8WDp1e9nQmhb6hJe_WNB4osUCyuv_EQIKFokLKGn9IifF71GI5_tYWzxxZYncXCuFQ4nHL-wVqoqhJCnrtmtI29FwZmXOG1McnzASVZjeDF-iUpWTvgL9QYgD-0Ai6lQ-oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های دو تیم پرسپولیس
🆚
صنعت نفت آبادان درتمام مسابقات: 48 مسابقه، 31 پیروزی پرسپولیس، 6 برد صنعت نفت و 11 بازی مساوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31239" target="_blank">📅 14:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31238">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DchmgLEQjQJQ1zM581exPN7f8Mraa3HuJWhi8zl2zf8XWVBC7dyZ2NhCNaB1kgtvIHWJn_DAizyavQ1F_5weoCpxy9D8kjHWhsph9V8kNNaEVYbmULJbmy03FjbxmywcWEUfXVwbmGyoE20amC42HfNOIfPT65W3dnYQeR4YLH7sk-lCf0uiBAd_cgC2KwVVbYzuqXRPpQ5GnpACPC6GIwf_gQ_OPOjCPzsmdUsXfoqISxotW9w4Gx03_I7suLRgvH_Qzu-3EpNFqgZpdisPnEXg7Zz8HaCGUGcMDtn49H-LZTxJKR5s2s9P6V4ejwmsXITrxBrQz_8d8u8tShMA8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
دبل نیمار دربازی‌بامدادامروز سانتوس در لیگ برزیل؛ جفت گل‌های نیمار از روی نقطه پنالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/31238" target="_blank">📅 13:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31236">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hCiBzrCGBeOEDlI1T8eOBQutjCsFeMNv-ZqEiY5j80louPVwx17c0Ek8i4XPRwY7_gnc2lwI1elXDLOofojPuBvIf9LOmfS4rkgozPxgbOFbPYhYmaNDq-vCe4MqrDmHnyiz-h-jlSxA5CRmcNjFZGJ8EvhpGimlgFzFW8Xx7jb8AOmuTa7NgEr-jaDvpSXIcpDOT2XNgGv87hZ1IPKu6Jr_EDlVqDDufK1ZfhlQxqXtSDOTp6zMO6IUEF1Z5v9IPrfu38swo7651QOT2h6Zli3qx0q-xYXaSLKGgVff00zb1kOYfZvQw6FKxcAhqbggEHqYxOajnOmYNx07WKE_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCnkQ4mRXIx7ktNOGd7xdw6FAmL96Plb7jKwFX8eKzaZW1uzTVy-AeWEs08Rwe3AfL76n84chBEjoJ2HslCupNSoCYQfHJLeNeOE_qYF3Yr_IGJ5oUfMXPgP-qhpibCWSCKUNPKZ7bsVPz-r_IiBdwfaEm3-JEU15Bgea2wTwRqOfHaxicBzco6zRialbVdD7pjcdX3yhmvdB8hjT3uUe829lpUaBtslYc8NTr-N5dA40X6t1u8we5Q8iyRcC0OBfL-e4aa8BJKwaNL_7TH0HfO_zt1L6fyaw7RZKUHZH1xdgfBLukpadONJ2P4j27Gp52xgPDwhjJ_pwxEYeNg00w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صحبت‌های تلخ همسر خدا بیامرز هادی نوروزی اسطوره باشگاه پرسپولیس که با گذشت 12 سال از فوت هادی هنوز لباس مشکی‌اش رو در نیاورده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31236" target="_blank">📅 12:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31235">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9z43gO4CbgzJq_otcIpYNmDP-Fn5VSh3FAneH3yqeqhRCdTYJdykR13fttt_szRm0j226T_15v3PB8dK8Y2PTBV95b1kF3104GiUn6w7Ux05l6Z_Y_tUvBxjErHFdWIDTCE8aAgGPW0p5C9Kg4jLH6SGvyD3GLa3tDTz0znEPnJ0qV0DFlsGi9BCFpCOBf328dlRrz2_Yc1Bt_zdFfBYqwCJ4t4vIabISRQDQHnGs4WG6qN4CDSvrPoIQhJKi_lVZo-SocykOUmYckimtzhtvFhieFOEc-AnsDVYRqmn8qEY11sSlTz2omHGXo03veZsarsFLxymDcO9UwBgG2bqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعدادجام‌های‌معتبر کریس‌رونالدو و لیونل مسی دو اسطوره تاریخ فوتبال در کل دوران‌حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/31235" target="_blank">📅 11:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31234">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awZt3rLsi2ujbfjUTlLwAKHoc2PrmKqrC77JyBirBxw4JhisyPFifPWIO6mpkajol-KKBA4E5vV1rwiLGrLV1uvgRL3YRRNTxEKYAXpAZ_SjgJ8RXQIurgHZfCnC70NLMBVUpTEAM1cYi9fxWlzCrTQFbCUqbaulb7Lv74cIxvxWUTp5oeqL5cHSNdUpwzyIMePy8XyJEpzUQ_qCTgY0i1We6fRSGEr4JiGsHD3G11xo5XBY5etQrJbI-n32o76C5sH4ivNCeTSlPYE-sLhWHwofcl1IENRL9cEan7OkyYIkwePyD-sukf_7E6BnHDHlVNzCvmtKFIwsHaC5_MZ1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
باگذشت‌دو روز ازبیانیه کریس رونالدو هنوز هیییچ بازیکنی از پرتغال این پست رو لایک نکرده!
‼️
این‌ویویو روببینید تامتوجه بشید که چرا کریس رونالدو اردوی تیم‌ملی پرتغال رو اون شب ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31234" target="_blank">📅 11:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31233">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
این هفته هرکسی برنامه داشت امیر قلعه نویی رو تیکه پاره کرد؛ این بار نوبت به تیکه های سنگینن ابوطالبه که اینجوری زنرال رو چپ و راست کرد.
‼️
ویدیو کامل قسمت سوم برنامه ابوطالب رو هم میتونید از طریق پست ریپلای شده مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/31233" target="_blank">📅 11:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31231">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEQsBpKFjMQ265rSCoT1rFDknWI7j5X82TaOnZ2ZcomeLm85CCS1jHDSxy0Xjz3cpQqNobKgRhJ7nlFFA_Cgtgde5A0BK_dilBgLCsirnzAsl7Zrc473GUkpUjkXCJU8aIWf2o1EnNBxJiSLJFhDzR_9NzLFZOpXJACqB16CPaeg37HL6yHey24S8zyPGyHFMe9bjO4u0e5Gqo5C4mfjYKfQHWf9iKV5Z6Svvm0BLlzczCijxkephm1ytRB2y3G050eZ6sYoczC9CctqWE_FS3QzLRnGJvjLYCFU5znQEahqyQYOPJHlzd_9JdDj-6n88VwvubK475QWKuYf49mnZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
به احتمال زیاد پرسپولیس امروز عصر با این ارنج به مصاف صنعت نفت آبادان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31231" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31230">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9ILuHPE2PMkfQ-bYqfxJ5mRMWYf8B8HPZG1J6n4fbVB0_2IUDYzbe8TWYpLuwUCM2YNEQ1qiFGkXeO-OLNxPCGOSJar5a1tWpINIhW3SU1_YJo_96s9UMTQ3oNH2Yw0-wGF5AcqP5eO2-3T-sA8Mi7Apy5q7N-n5sN9kqBoAEAuWrDyTdLb5668ZgSfActmQvHMgiC72tHOSMF3DUP1-A7D54yCT4CZPEy7e_Fw1TL_htpK-ynYS1wHJoXc4UNsSwb4qPtcH1PRHhBSxTQjww0nguTJrEoYkRZlkTaSR57KDiMH0N-ezZR4pmO5s9g_9FKsuBMsaWc9oDmEnlBG4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحنه‌ای‌که علیرضا بیرانوند درپایان دیدار دوتیم استقلال و تراکتور به‌این‌شکل‌سراغ‌یاسر آسانی ستاره آلبانیایی تیم استقلال رفت و جویای احوال او شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31230" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31229">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9af88968.mp4?token=E-Vgn2-vaG1oJoMJXhOBImQaQOrxOQYVDJ9R8ydejgXdPezJaVeFeVRlTkxpNA2wicvxI7ET1iiGfWGvvU5NCO5KUG4Ar1mOmN5Uf8ls1ayiffl9RBt_SVCAlpcat4E7z7SN6HBUucn-umZKYYqWDL0CYU3FPr4wyl_OfZp__vO7wJgHeHi7UZg7teuxgRq0VBBqE8UfDpY4HpQ7PPKKGCVAzFHArRg5XPErCmrKm8QgGPPchycTxZbEytQguLlYoQ9IJxW83fMfRHMOoHzjPJhMDitK8r05xRV1CaEKB-iBvW6VtiTM7SZP13AF5n1KFuaiEYS2bYjHtQUsFB6m6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9af88968.mp4?token=E-Vgn2-vaG1oJoMJXhOBImQaQOrxOQYVDJ9R8ydejgXdPezJaVeFeVRlTkxpNA2wicvxI7ET1iiGfWGvvU5NCO5KUG4Ar1mOmN5Uf8ls1ayiffl9RBt_SVCAlpcat4E7z7SN6HBUucn-umZKYYqWDL0CYU3FPr4wyl_OfZp__vO7wJgHeHi7UZg7teuxgRq0VBBqE8UfDpY4HpQ7PPKKGCVAzFHArRg5XPErCmrKm8QgGPPchycTxZbEytQguLlYoQ9IJxW83fMfRHMOoHzjPJhMDitK8r05xRV1CaEKB-iBvW6VtiTM7SZP13AF5n1KFuaiEYS2bYjHtQUsFB6m6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
ادعای نشریه فوت مرکاتو: نیمار زمانیکه در الهلال بوده به سران این باشگاه گفته جزیره میخوام اونام درجابراش‌خریدن. درامدنیمار درالهلال به حدی بالا بوده که درامد سیزده روزش رو به خرید جزیره اختصاص داده‌. نیمار در تیم الهلال به ازای هر لمس توپ، حدود ۱.۱ میلیون…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31229" target="_blank">📅 10:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31227">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JA-y0eMu-ZIv8Dx8APEDnPSW-_IAUBZCsHY0ijGeK7aH2yCMur06El0BHp9tbEq4ZCyB-c-567weEDXqdkdlNbfyjmeftpem7q-f3gVtjEp__p_BTQ3zIDjjBxHeFyDv1ylWpmayPUfcolPf0HFk8dBXi-2vmL7eV7WUtjxCzlnBeCKWPmQfjPxpyVG69BM6Co6JyoM2nIVvdIHy0xc4TGTaUP0Tk9nYYERrkF7m-S8LOVCIdOGMt7Yp_Q2qQ3aOsfs8cX7t1JBSmeeYSxHHHMllJ5cWUDPiYxvd8RBclQJCMrQu0uyIWs7aSBsc6XNlcoNSObD-m_CpEYXkc_vLtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
به احتمال زیاد پرسپولیس امروز عصر با این ارنج به مصاف صنعت نفت آبادان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31227" target="_blank">📅 10:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31226">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFJTkPDSQ3Y3R6vFDbKtUFZsgY-WQw1EZgOWvCN8d2WMsymXaURcyBm37i1KKwKTZB68mG50yaR0U23vS5B7YAtQBuBj8kJmDcUZNfF29a5XvLElsLCP4JVNqTgH1gR6c5_RMo4TPBq-jF8WC8uKSVbj6RUT1cboD8Txla9sjTzqM24DOpKbe88qksht2s0cSZnq8MOoiEjHWvh5Im5syuqFb_annTSa611koTl-ANRDZi5sLwPrVoHu3V-4v1r98KuOSljCA-JlL9vdt1OWPlKyIMI9TataU6uW6JKTj5iVuRctKK5eRyw7fm63ej55ecHNNAq23rTYeHmvB1OiFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ نبرد شاگردان تارتار با صنعت نفت و دیدار زنبورهای وستفالن مقابل وردربرمن برای حفظ صدرنشینی در بوندسلیگا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/31226" target="_blank">📅 08:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31225">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg7O3rVsj5-2V4B1ZUCIWbTtARLvMXzaSTuoiHUNUOVXHemmMGp-QYLXmRJyhxw4L7AAJHHW2ZeLpkoF-mKlYmE8-pPZ8Rhrie2hJXhMzaKkhMJqCjMMe2IbJo4a7frXr_oayH3iI2U1XSIwaA33-ASokHt-8kbiIcfL7Uuz6etAWEOmcT-12eb60TTWUjIlgpEoT0PSYBmjCcYRfqG6YdQkur_B42ez_zYsPKQcUOcobN30kkJGxrrZYMb_q94PSU-tLD36kayCoKN741nYeUHleUw8MltwG2nIznH0v7KdMYkPu8OhT1HpZ1PcU84k8kGwECvygswqcgZ4sNxtZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
از تساوی‌در نبرد استقلال و تراکتور تا آتش‌بازی سپاهان با درخشش حاج‌صفی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/31225" target="_blank">📅 08:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31224">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛تساوی‌شاگردان بختیاری زاده و نکونام در یادگار تبریز به کام پرسپولیس و سپاهان.
🔴
تراکتور تبریز
1️⃣
-
1️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/31224" target="_blank">📅 01:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31223">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRGQWxrWKcuJnld4L-BBnU2JfwGiz23ski8uLgXrFsNrKniPB4AQuIfW76CoK49fF_x7CsO0i9e0H8c_jcvmmOh2LavQq4uvG0XY4zN0ULqfF-8qbX4yr1xb5zAMAMqu2kIa7txb-uAOghOwgZXJTx9IyKBZ8AiVwvPRnX9cs9adGAmGy9gQE1Af2S0bWzV15n_XQsWDmybKh9oqisbv1i-tYnkY2zceuSX1RStpIiIk_Y-gzKPdliPlWODF3Mxeo1aTNUduziFtmCw3QwYQ1Ab6mFySqK71eMq8edIzulHJdcRf5Ay132BdIBPsF8ggc5sm-1a7tNQso3_wGqDGLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحنه‌ای‌که علیرضا بیرانوند درپایان دیدار دوتیم استقلال و تراکتور به‌این‌شکل‌سراغ‌یاسر آسانی ستاره آلبانیایی تیم استقلال رفت و جویای احوال او شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/31223" target="_blank">📅 00:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31222">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
علیرضا بیرانوند به‌دوستان‌نزدیک‌خودگفته تا تیر ماه سربازی‌اش به پایان میرسه و در نقل و انتقالات نیم فصل با قراردادی سه ساله استقلالی میشه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/31222" target="_blank">📅 00:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31221">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a328e3cc8f.mp4?token=vpR5JRSP42GzkUYx-M7c6meoxmQOp75iOMXuvvz-pcnQ7cbDkyLReN-yzFC9mYfd5CjbQihVXlNPf-fSAZsgbSO3yGsY03sAxTGD6FDpx1qETHTlDXug5ppucrDUJ44CKeDLD4JDPEmZ5IykN5U9tF4LeRv59865jy2dWq-4HGY8hmzugF8oyzz1N00eDrY1yKuTwzDYHVKSTo1juAqnsDydJAwxjVNUs4umZKcfZijndSn7UJCSac_GfhFCd-OGH1RmYeX9sVN9YoKV0zLl6_5-OtweWqCScopb775zSsjEyJVunPoGH6C338lDozQ-0YXOgYxdCUb1-055EFfgXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a328e3cc8f.mp4?token=vpR5JRSP42GzkUYx-M7c6meoxmQOp75iOMXuvvz-pcnQ7cbDkyLReN-yzFC9mYfd5CjbQihVXlNPf-fSAZsgbSO3yGsY03sAxTGD6FDpx1qETHTlDXug5ppucrDUJ44CKeDLD4JDPEmZ5IykN5U9tF4LeRv59865jy2dWq-4HGY8hmzugF8oyzz1N00eDrY1yKuTwzDYHVKSTo1juAqnsDydJAwxjVNUs4umZKcfZijndSn7UJCSac_GfhFCd-OGH1RmYeX9sVN9YoKV0zLl6_5-OtweWqCScopb775zSsjEyJVunPoGH6C338lDozQ-0YXOgYxdCUb1-055EFfgXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های تلخ همسر خدا بیامرز هادی نوروزی اسطوره باشگاه پرسپولیس که با گذشت 12 سال از فوت هادی هنوز لباس مشکی‌اش رو در نیاورده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/31221" target="_blank">📅 00:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31220">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhiygH3RLaehSp3SsdU5vqlJLZE1xS_VlojP4aKVqIhD8GM14OGks-INiL-IFtKbHkbRXPADiBc3JW_-6Rnn3LqlVA6KbxKAT0clT8dO5E64LoNOV6HP5MSPv7rMIxpcsUcKe7Bi6xNgZCvxZMLD1AsY6IO2gBsvJoAdbSIY0e_50X52c57k10ZyCLf7aztiGtpSPPGHBnIO2oYtDScdPki-AemOkPr_DVwf_scS5-_B6c-uhLsnhXv08v3hyoEpSTIozOp50usTq6wuQ0beBEAB0PV8p4pcM7IPKqX8bBQ7VXi7VFB_Cs-2iRwBJV89jtCxN9RZNYjjljBzZmKesg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت؛ کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/31220" target="_blank">📅 23:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31219">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeNm84laawcis3NDet8Js9Cj8Qdjj9X9YFqxs0k_NWuoU7KRNBlK_3NRVNsZ7fPf_ao5krxdZh0Q_5AutoNG6PO9rw-xVhtmsaf1c-P0wPR8qHR3vE0h09L9aomlmgdbfb0alu-knY_T_nFh74S6KvJiN5PtQAvxWjR7CTXhGILyIJxQqa8XxYivqipKwzgiBBRxJfc6gbyhmTmmdr7gvPJYZF1zzLupR4WnFgedwv9W8RlpJ-c67e0kfUzYV8Yd6kvcLN7TIq_QXWimGyL_tnp69NChWUdyaLDSU4MvBi7NsSe6ZrIi1_YlHg4rEeSF_nmBNG_7B1-UK_dvQCymNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شجاع خلیل‌زاده بیرانوند رو آنفالو کرده و از همه بازیکنان خواسته‌که‌این‌بازیکن رو آنفالو کنند. بیرو بعد بازی بااستقلال گفته تصمیم نهایی‌ام رو برای پیوستن به این تیم در پایان خدمت سربازی ام گرفته ام.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/31219" target="_blank">📅 23:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31218">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxzzNEgOkNrSrQLc3fDnf0oF0nY6HLIEGvvIYCBxIMQWe6EuQVbAaR6fP9BLT9L4bWvfv9EnrmqrVZxU1p8Bre9QK-69G2oEwk-p5FadLe0S6etjybq40uiGeSHW7tKiuInWBzJk8IdZZldMcdAuU9Bm73Lt9TtMh5Ti2eKJFCr6Zr2T0Y5iVOaHN7Tk-Mxvj3LEzXrzE5SKomlGACIaRCY1C7Sdjgt5CzvBiTZLEN8Rl15ekGz7zUhP_-KT3JIDlPwJ4HZx1SAVp39apr2NI8Sn47Xi6IZ-t5KkU7l0_i6Y9i2PveIRoc3azGNiluFeBy6DpEBpOUHwrbcyOYOtCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت
؛
کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/31218" target="_blank">📅 23:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31217">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e52465a28.mp4?token=MIUh3ep2IUYFqUnvMHXBCkl0G3EkLxJZIdRvMNU27BcbvRSIIvc3RpzcGg_at6WGNhE3U19s6bVStbHIsgDV1ZO2RezN31HMK8wfO8kOKDbKon6sQoqp-It9x7-jkQ8Y57CBt2uIjr2z_Hnx65lWEBuukvMXRFlKzSUDz4P7uFTbujqtdLyjUSXA_sO_FtfAB3x5Mx2ndMXVjP7OAUkz_j9TpUpxsf-NHSsPZZDHS_eVr9J1fiMNqQ2eDQn125tgtCHanhcwUO7YZsoR522KqrYmMeLWQziQkExeUWty6VHRgb849CgZrTEQEeq1ovooYgsu3LLzsqRXPELIlaTOhTCabBfZIDkq0o3YWrKlbbLiiIBHzrSbTuhNf7oTzFnFF3IOho6vyIS4qx_F47KonDdfhVn89kiLKYxNoZuCd6q1cpgYg-J-3zmmneE8msPrwxYWXa6uvqB46Oa7Wl25B6Xio__0ibDTo9lFp7gM3sLcaLioA24qs-5YXTkrjpEXSsJTdd8w6cjbrPHonHX6yTibf5LyqbxZd7ppQDV4XCStFmXvljw_RRrH9Wmw4aMoNdYgSyV6_F1Myvn9ksgH-gyZxPfGUFPm-KDBDzM5fBwl5b3nW03in1zvuQ84biDTa0dif1l-O3xJ621IfADr2mSShpgeMA4YHMZvgnyAlrU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e52465a28.mp4?token=MIUh3ep2IUYFqUnvMHXBCkl0G3EkLxJZIdRvMNU27BcbvRSIIvc3RpzcGg_at6WGNhE3U19s6bVStbHIsgDV1ZO2RezN31HMK8wfO8kOKDbKon6sQoqp-It9x7-jkQ8Y57CBt2uIjr2z_Hnx65lWEBuukvMXRFlKzSUDz4P7uFTbujqtdLyjUSXA_sO_FtfAB3x5Mx2ndMXVjP7OAUkz_j9TpUpxsf-NHSsPZZDHS_eVr9J1fiMNqQ2eDQn125tgtCHanhcwUO7YZsoR522KqrYmMeLWQziQkExeUWty6VHRgb849CgZrTEQEeq1ovooYgsu3LLzsqRXPELIlaTOhTCabBfZIDkq0o3YWrKlbbLiiIBHzrSbTuhNf7oTzFnFF3IOho6vyIS4qx_F47KonDdfhVn89kiLKYxNoZuCd6q1cpgYg-J-3zmmneE8msPrwxYWXa6uvqB46Oa7Wl25B6Xio__0ibDTo9lFp7gM3sLcaLioA24qs-5YXTkrjpEXSsJTdd8w6cjbrPHonHX6yTibf5LyqbxZd7ppQDV4XCStFmXvljw_RRrH9Wmw4aMoNdYgSyV6_F1Myvn9ksgH-gyZxPfGUFPm-KDBDzM5fBwl5b3nW03in1zvuQ84biDTa0dif1l-O3xJ621IfADr2mSShpgeMA4YHMZvgnyAlrU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج و جدول رده‌بندی لیگ برتر در پایان مسابقات امروز؛ تقابل حساس فردا پرسپولیس مقابل صنعت نفت آبادان در هفته هشتم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/31217" target="_blank">📅 22:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31216">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKXEqiyMI4fh_0_IlsqP22L_Ewkr9SK_1wVAYnlXHZ9O5t9KZGUn744TK-hqW9g0nIHm4nqTz3CDRSgkhM7kIP5xro1vqcO3pdfFX_ee2tvs5fOEDBvPfR2sjrQGEZS5mBjZ2FlmMjwpjg4v4OVGWUewtQgQyMxWNEespSHJ4MCMF9t3roiAWnRdFl-LbWAlswECzwHpRyYxo0oucaOsvHFu4dVESYZhc9jEOVQnlvXHmFmhLgH-7Hi4tLP9Iz1-uAZemv9eoLdN0oanKckhmT9tSi1LFZqF-XnAUrYxepGRUBlKN2UqEKncgipQxHUO-BzO498IE9_KSBEacO5jGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛جدایی‌دنیل‌گرا و مارکو باکیچ در نیم فصل از پرسپولیس قطعی‌شده‌است و مهدی تارتار به مدیریت اعلام کرده نیازی به این دو بازیکن خارجی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/31216" target="_blank">📅 22:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31215">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_UDx9ZSfG1KA6Xoos0IIZUfS5CRg_137K0bPz2BE_LL6dWZMFwdkIF306Zi6WheuuJakHEce8S2j44-lm62wPhInucYZtHwbIHxNB0CzDfZapdVcge39tLCmfEFaGamXyLlK0sXDbWm7hRcRlRkaIhE1tk-iVpK-00T81feOK8KZmUNjgKeGh7XUbqDCDgKTi4DZsYeGzRxlsW_xgg0EAuZVcRgu-6Qi2SC122ecYSDvKmy2i7SAGJoQu8RP7MCGJMR5F5y0NHREivkXxY6kLyYxw7V6tDj1TDfSLdAMlZsxSV-kBjtVyNQR_gcwnmgEbqG5_xlUB5EhmbYQIf6yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ژاوی اسپارت ستاره 19 ساله تیم بارسلونا قرار دادش رو تا سال 2030 با آبی اناری‌ ها تمدید کرد. اسپارت قابلیت بازی درچهارپست مختلف رو داره و در واقع آچر فرانسه جوان تیم هانسی فلیک است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/31215" target="_blank">📅 22:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31214">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3eWL6RvXgolN46DP5s8BsNYPYJTZ-zcaYeL4yiK57U8P5Pet23W71iwdrhSqaORIMa-bdAnzWX9S5sKxFqg6nDb-6MZAsewuL_uzmlQUPV2SIeSnkO4T_QGqXdetUw5K5H4i7TqOjI5VGzUBKbqKlvPOgP2m5XLT5rt43MC81ThNbXE1eqAYvy9ktnNkof6WvNaDfZb1Bd_ds1c-tL-sIqcRMLMoVaP0TYcGITlrVFOYilKiNQUrenv9-2_PXQsNBATi9lSUPkLKWUzD8ScBynA1JpXhMV-lzInkrK6VT6bfLyY9EgfLEpjHlEf9emx4sYMdrCIrPyVvrnu_YAD-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ال‌ناسیونال: اولیسه خواهان بند آزاد‌سازی ۱۷۵ میلیون‌یورویی درقرارداد جدید با بایرن‌مونیخه و گفته درصورتی تمدیدمیکنم که این بند رو بگنجانید و هر باشگاهی "رئال" این پول رو داد بند رو فعال کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/31214" target="_blank">📅 22:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31213">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e828d2e24.mp4?token=cML1nSptB3nUUoyF_o__ITnC1OJMJSvg7v0oBkkD9ksJhy7eIWtAqOk-KnoAnH3E7XGkQsFRzryvePE53pMbk3oh_usmacp6EPI8dI-iZ35376YrhOvJy8k4wbgF4OY8OkubY_YZWM12ynq7CZtGiENjjAaOo42WI0gF7Un76QJgCLuClV7hWtkeDin8VWVvezq4az4b6cliyorq8T6Bj48yrX2_hWwE7VHWPsEyFeuDUB7ydPB88LMewGPElE-5X0X9RDR2NDCeOWc5w1n-jqf_o_AMSUIiPNwkf-pU_hhJkg0DJ2I56EhA2Uz-R95vmWtFtLDGRCtdnBXInvSPDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e828d2e24.mp4?token=cML1nSptB3nUUoyF_o__ITnC1OJMJSvg7v0oBkkD9ksJhy7eIWtAqOk-KnoAnH3E7XGkQsFRzryvePE53pMbk3oh_usmacp6EPI8dI-iZ35376YrhOvJy8k4wbgF4OY8OkubY_YZWM12ynq7CZtGiENjjAaOo42WI0gF7Un76QJgCLuClV7hWtkeDin8VWVvezq4az4b6cliyorq8T6Bj48yrX2_hWwE7VHWPsEyFeuDUB7ydPB88LMewGPElE-5X0X9RDR2NDCeOWc5w1n-jqf_o_AMSUIiPNwkf-pU_hhJkg0DJ2I56EhA2Uz-R95vmWtFtLDGRCtdnBXInvSPDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
مهدی طارمی مهاجم 34 ساله تیم الوصل در اقدامی خیر خواهانه 8 زندانی در تهران رو آزاد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/31213" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31212">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObyQ2OQKafjnBy59W6aVVMjqvSrKhIio5np997BL_2JLMKnqyPYW_-gpACy_3s3YOOIPPwu1eJUriC0yC1QwGQDgnkZ4xexzdyEKbocyfCnCeOb7Cn3EhCd1MqcZN9fuvpQNqYrxsnylkNooPMlp09ETVCZlsYmO6UpSSoswEe8S23BBAqLQ0pPCKa5zFOm6WzHP6l86w5ITC_0QsHM28F8eQYyY8Cn8uBlf4WjFh4h_Ijrj7sWUQy0OpDVCCrFk-ZSjE97frk9KX54gnBZXRNo0Vyy1pdMjUMfQP3Hmf8dId5FocU3kJmctG6M_IE3XmyrD__tWe-1soLgAGnHMzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
واکنش‌ علیرضا بیرانوند به احتمال حضورش در استقلال: استقلال تیم بزرگیه. من یک تصمیمی گرفته ام و 100 درصد روی تصمیم هم هستم. من نیم فصل سرباز هستم و بعد از نیم فصل بازیکن آزاد هستم و تصمیمی خواهم گرفت که به آینده ام کمک کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/31212" target="_blank">📅 21:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31211">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/31211" target="_blank">📅 21:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31209">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJFP3G-DASF_g2FdJINeIGE-v9FSPHkNAuU8z30PUqS51syR6Sucrn9WZ_m6TeJcBLLTrVCdEaZmQhPppm9N_eVV_zq_cMj81iHDluc8bn2F_4YcYKzpNiVztqj8FL_Qpz8iyYgBVhr93mPScDC3BOSIebVJMkmmKPtAQqfME3E5sqPtxBjN8lqJfUJTlbM8oowPPcCXzJGXtZiNItWscYDh8lVt_SgYz31SeAGgCMqpOJ3KccsuL-5cWL2NytQhZWMW3U9f5jXwYIa4Ku74mBCWSa0on2slTrzq-JQp7wVBjFW89ydggKvVyOCgzdEJMequZ-aN1V1LBdAKZSY8-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQFG_74bYlD4R9MMrCuSdTdfqiZwWss9I2imEGrbVlv12_cub9RNa4VvfVUSsrkIR8Xz30A0fYQDVxTto-FjszmVDdeCowMbYPVoSJJCI00Cn_00Pe2ovtR2xzPzWt9B_7FM0D1dI3TtU8J8LUAlpjLJrVlq_lBmIs97BDAgLuftOSwvcfSPCSEVQelPhub370dCkMxqMxSI-jPINmj_bf_owMT3L1rSmF8obPmF0AONtagNWHGGwhmHc699OmxPuSMF0oN6YzHaB9tZ91W_GOqky4SvsAtVdm77sq6987Rq_d2KHJcZ-zMA8GqufixIbYvoyJziL8ppmbvHJxSYMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
گل پنجم و ششم سپاهان اصفهان به فجرسپاسی توسط مهدی لیموچی و آریا شفیع دوست؛ هر دو گل خوشکل و تماشایی زده شد جفتشون رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/31209" target="_blank">📅 21:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31208">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd5e0f0ae9.mp4?token=UnOzMKabzyxHcTFxsEgfYNsOxX4SmPeTSDcOw6hcwBID5xhVEfkUIX7koCCr2UkRQXxsHXNFeijGco-Vzazp762-OdfH1TD4v_7RGBT5cQ98OtRUHXXC5LWNZWS5BbG9jJQvUtoZnsvlSLiDGrqksghL5j82awgPkxeNz0wMx3kPsr3mFj2x0m6DnwOUFdNTJ6vvMgDjJSOZ3WTB21KT2JAaltlXYLBb8JqgdjQv62850Ux0_SVYK7DQIwZhX4yBI2yNd3-BbbOyrwbObB68XaGH1O2C3tGV90CwiTTMsJy7JpfPe9uva3N2CCM6VgrJdpaD194gtzPZuVY0hlCHUAGDFkpXy5LKvhxxhjQro9zmCQtorS4Oe3QB61BJNu7OBUg1mO-B9-Oc0iiPOuhz7UOlbZGSYIUgvVPeWZviZCVlVbUowzZQi-xjR8ThHEaI1DU24gjQnn3H4N8tG8pvlmQowByDVqTMYvn-GYYvt_ycwHLwXzvRsvq1KqLcWQMH2bjcx3n-Bs-4nhK72lEPl7JbnoQvfCRCGiypObJB0ZHDj4hhYM76CKd1RNW8NfIYpKxW6rFMbv859cQg7bV6X2hpEPEfasp930vuuatuGhODNgrJ5kH-Envp20DNU94pX15QUeNmN9BFPBXB3MACj24Kc8O87gic0f2tDrPytHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd5e0f0ae9.mp4?token=UnOzMKabzyxHcTFxsEgfYNsOxX4SmPeTSDcOw6hcwBID5xhVEfkUIX7koCCr2UkRQXxsHXNFeijGco-Vzazp762-OdfH1TD4v_7RGBT5cQ98OtRUHXXC5LWNZWS5BbG9jJQvUtoZnsvlSLiDGrqksghL5j82awgPkxeNz0wMx3kPsr3mFj2x0m6DnwOUFdNTJ6vvMgDjJSOZ3WTB21KT2JAaltlXYLBb8JqgdjQv62850Ux0_SVYK7DQIwZhX4yBI2yNd3-BbbOyrwbObB68XaGH1O2C3tGV90CwiTTMsJy7JpfPe9uva3N2CCM6VgrJdpaD194gtzPZuVY0hlCHUAGDFkpXy5LKvhxxhjQro9zmCQtorS4Oe3QB61BJNu7OBUg1mO-B9-Oc0iiPOuhz7UOlbZGSYIUgvVPeWZviZCVlVbUowzZQi-xjR8ThHEaI1DU24gjQnn3H4N8tG8pvlmQowByDVqTMYvn-GYYvt_ycwHLwXzvRsvq1KqLcWQMH2bjcx3n-Bs-4nhK72lEPl7JbnoQvfCRCGiypObJB0ZHDj4hhYM76CKd1RNW8NfIYpKxW6rFMbv859cQg7bV6X2hpEPEfasp930vuuatuGhODNgrJ5kH-Envp20DNU94pX15QUeNmN9BFPBXB3MACj24Kc8O87gic0f2tDrPytHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
گل سوم و چهار سپاهان به فجرسپاسی روی دبل دیدنی احسان حاج صفی و آریا یوسفی در نیمه دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/31208" target="_blank">📅 20:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31207">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78ef0133d.mp4?token=PA8Ldo8IAzg6UpFiIK_x3P1HaQZLXtgsaEi0Trbs5inBJP4VmfEaX--1iyhIfPgZxsX5Vdf-WmAy0waUWPzzNpo1tY2QFx-VSJX9cVHREpdCYeRqXQJ4d4XbmG3T3Vx9YRJuhysAP4anSo47rX1JIRZ3tlgLWJ72CAbTN6UsQCB67QtlHUnNHgsC44SEXCWq50rMzUYK_Iy7i-DHQp51SN01Xq49nQhfjPlwfgvlfo4KSRdGjLf5k6ShEvmN7pXex_sD5h6PCYfQPOjWYIydctzo1HVnofHHWcbaGm8AFZGKz5Bnf5KfKqWFUpQpIJD8IYdusiur889r9xmKvgyU9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78ef0133d.mp4?token=PA8Ldo8IAzg6UpFiIK_x3P1HaQZLXtgsaEi0Trbs5inBJP4VmfEaX--1iyhIfPgZxsX5Vdf-WmAy0waUWPzzNpo1tY2QFx-VSJX9cVHREpdCYeRqXQJ4d4XbmG3T3Vx9YRJuhysAP4anSo47rX1JIRZ3tlgLWJ72CAbTN6UsQCB67QtlHUnNHgsC44SEXCWq50rMzUYK_Iy7i-DHQp51SN01Xq49nQhfjPlwfgvlfo4KSRdGjLf5k6ShEvmN7pXex_sD5h6PCYfQPOjWYIydctzo1HVnofHHWcbaGm8AFZGKz5Bnf5KfKqWFUpQpIJD8IYdusiur889r9xmKvgyU9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
گل سوم و چهار سپاهان به فجرسپاسی روی دبل دیدنی احسان حاج صفی و آریا یوسفی در نیمه دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/31207" target="_blank">📅 20:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31206">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l61PbyacY6flCZ6ZLJyeFHaKCAu2ijoKx-hJYuslocex_IZnSgqoeFWWoMFDTV5mEhvvFfQIntFokdyqUYUsAVL2MRPiQwevPfIBbO0Ak8m0qjJvqFHbSVvcTN80YujxzvLDH15vxd0vMYL_jzum_yKvGtYL-iLiAFIMtwkBgr0_VSz14sFLbDbquxjtnCh5vv9LBzAwF7B_lYCu7Ar8vO4iUpa63itpL_YuaO64sAFpXIQeD1wKIi6TiUSxfWBSqaBugEJszBjnjL9luOJAAUpDI7siLc2INDIfyg8EoHZj1hKszgKaNJDV7xo7HFWFqN_CHOZvfWDEYDq0jGRaBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دونالدترامپ رسمااعلام کردکه تاقبل انتخابات که ۲۵ روز دیگر شروع میشه به ایران حمله نخواهد کرد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/31206" target="_blank">📅 20:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31205">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c2c2b307.mp4?token=MOWi3CBXOq0jro2RSRa01eIExHV8Athm6e7LBqOYR4HAycZtA0PLjE6TjzGBKVlfBrXHarJE60pgLgq-ZPHVn6XNh7EfAUqYpXq7yhPK4kmHgr75oHbKIxnzUply2IhbHyI6NstRWcZBrwuI_N9AlO7rT_D2iUy8ggg71ePmst2QZV-xZGVKMoegQWuoM8UqrrIO01eP7tF8TnyrUXbx9kr7jbT35ZoZjT1qOy3xwc1FyUkH5b5TgCYUBBi8j0zKlLolRZ2FYuA6XGx2HJy6qS1iPLc5BXPDSFAlBBxn_p1TeQPoJ2YHRuRx60ZBUb1pcjl_pqXfTImXdMLoSu-v7Gwp2mkW6Lnv9zo6UJwjkcxEm3ggo5Rs4TS83r4jZhkvzUeKxVO8dPFCQuuEmX3wv2NMsLnqPJDLpVPxL3aA2Dw7vE7UbN_kgH2Mv5W17DuxkFux7dnn1S4xkCPV0UFMh_vNteXUMEv6BtmqMQPttd2oHCiHb2tz6KWMgm7SZZIyBxaF2qXmqOQSilhBKv5LTBrB40c19CY7juCcNLre0d873kJV5dlo5ANcSzEdydldvNJYLt4iOLseJK_VlsE8qsKYvdfca1fQfiF5My4cIM082FD5VAzF0SIiDX9pClq8K5MI93olZCYE6uT5o_b_47lc0ct83D3tI67aT6rIUkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c2c2b307.mp4?token=MOWi3CBXOq0jro2RSRa01eIExHV8Athm6e7LBqOYR4HAycZtA0PLjE6TjzGBKVlfBrXHarJE60pgLgq-ZPHVn6XNh7EfAUqYpXq7yhPK4kmHgr75oHbKIxnzUply2IhbHyI6NstRWcZBrwuI_N9AlO7rT_D2iUy8ggg71ePmst2QZV-xZGVKMoegQWuoM8UqrrIO01eP7tF8TnyrUXbx9kr7jbT35ZoZjT1qOy3xwc1FyUkH5b5TgCYUBBi8j0zKlLolRZ2FYuA6XGx2HJy6qS1iPLc5BXPDSFAlBBxn_p1TeQPoJ2YHRuRx60ZBUb1pcjl_pqXfTImXdMLoSu-v7Gwp2mkW6Lnv9zo6UJwjkcxEm3ggo5Rs4TS83r4jZhkvzUeKxVO8dPFCQuuEmX3wv2NMsLnqPJDLpVPxL3aA2Dw7vE7UbN_kgH2Mv5W17DuxkFux7dnn1S4xkCPV0UFMh_vNteXUMEv6BtmqMQPttd2oHCiHb2tz6KWMgm7SZZIyBxaF2qXmqOQSilhBKv5LTBrB40c19CY7juCcNLre0d873kJV5dlo5ANcSzEdydldvNJYLt4iOLseJK_VlsE8qsKYvdfca1fQfiF5My4cIM082FD5VAzF0SIiDX9pClq8K5MI93olZCYE6uT5o_b_47lc0ct83D3tI67aT6rIUkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
یادگار رستمی ستاره 21 ساله فجرسپاسی به این شکل از پشت محوطه جریمه روی یک شوت تماشایی دروازه سید حسین حسینی و سپاهان رو باز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31205" target="_blank">📅 20:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31204">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b8e357fbe.mp4?token=E_r0G8j7ov3IvmZGszQyUFmim6RX6aR-e6sZ5JN4bhLX7vGrG7nYvSsTKLXbx9CfU3yIJuKzWyS9hRrzCX3OuuR9P7t6qeX1qXdc6ROVzky6t8ZMgk7sI7_tFxG7GIro-Ha9OWAb0Vc_4hL0Obis4nwfCijiqbziF1njYMgrMPDyi2bZb_RJtAu2bUfOczMgUgWxfuoo-djKgDUIx_jzOm0jaz5H68gtuV9rcBVMrOOYBgunZF_vnQRK1H9FznQ8sbw059GtnpUzCmAu6tBuLu3Nat596WoIJA3Y56UbaW0b3C7oLaoVZed_l87SLpFnS_BbbPHVILx6enuXDeANuCEc-JPZJ_0mwdhW9sLucYQIRROzs6NL0T5ULyjKrAld67YeBXhaT03EDEpUtkcPrIBvGzBbI81lY5R1AQ8q17LZ3mkx6W_DEUrXU4ff2DUb1vp4vxJmbanz68_qyJdbkaCHUz6kVVR3yF3KTtKAk1R4ltv885QQvNWWvvPmNAcO9OFd4OenYfEfRBlthTfM1bZcrnguZGHBMwXC1Ry-brt-Rs_fGwUkVvVC4B_yEEteX0pQRrHIxdFJT0YR5YwMcUUdzT4onDkhJjHyYT5p0nUa0bDGsubkjLXbVkkVSSR0ilFDApya2oUDnbVDWuUwJMoNyse2iTC3kOIdwDrxPek" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b8e357fbe.mp4?token=E_r0G8j7ov3IvmZGszQyUFmim6RX6aR-e6sZ5JN4bhLX7vGrG7nYvSsTKLXbx9CfU3yIJuKzWyS9hRrzCX3OuuR9P7t6qeX1qXdc6ROVzky6t8ZMgk7sI7_tFxG7GIro-Ha9OWAb0Vc_4hL0Obis4nwfCijiqbziF1njYMgrMPDyi2bZb_RJtAu2bUfOczMgUgWxfuoo-djKgDUIx_jzOm0jaz5H68gtuV9rcBVMrOOYBgunZF_vnQRK1H9FznQ8sbw059GtnpUzCmAu6tBuLu3Nat596WoIJA3Y56UbaW0b3C7oLaoVZed_l87SLpFnS_BbbPHVILx6enuXDeANuCEc-JPZJ_0mwdhW9sLucYQIRROzs6NL0T5ULyjKrAld67YeBXhaT03EDEpUtkcPrIBvGzBbI81lY5R1AQ8q17LZ3mkx6W_DEUrXU4ff2DUb1vp4vxJmbanz68_qyJdbkaCHUz6kVVR3yF3KTtKAk1R4ltv885QQvNWWvvPmNAcO9OFd4OenYfEfRBlthTfM1bZcrnguZGHBMwXC1Ry-brt-Rs_fGwUkVvVC4B_yEEteX0pQRrHIxdFJT0YR5YwMcUUdzT4onDkhJjHyYT5p0nUa0bDGsubkjLXbVkkVSSR0ilFDApya2oUDnbVDWuUwJMoNyse2iTC3kOIdwDrxPek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
ویدیویی زیبا و دقیق از آنالیز بارسلونا مدل هانسی فلیک در فصل جدید رقابتای لالیگا و UCL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31204" target="_blank">📅 20:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31203">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbbf119a08.mp4?token=dWzn_VNhDFafvXvNRSMVw7NJ6VX9TrjmZEjjjm8ikHrPvTC8ItT971rgtnDjMGeRqfAwhrEIF5WkrydwL4S0o_zrkbyqjQkcTTJZ20JCiRybFI17L9jTXE1F_1DKdgU-ztEsRsVkxF4WMRnssl8_v0-VYbKJfELR-M-RrEc1uK42Lc2Nmh4P2AmIKBKDaQRPEApg9GuKZEeQSY8fL3p_s4L52Ohs7e19sT5g577LL_3ENqecFwCc7V1Tfh04I3t-NR1Ta1DPbt2oXgkwvd-bzLyEieDq6u0rUdO05lBzn1DsdOsRfeIsHlMYpJUtYEY2WMaM_ArBzzDjLHa4k5grUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbbf119a08.mp4?token=dWzn_VNhDFafvXvNRSMVw7NJ6VX9TrjmZEjjjm8ikHrPvTC8ItT971rgtnDjMGeRqfAwhrEIF5WkrydwL4S0o_zrkbyqjQkcTTJZ20JCiRybFI17L9jTXE1F_1DKdgU-ztEsRsVkxF4WMRnssl8_v0-VYbKJfELR-M-RrEc1uK42Lc2Nmh4P2AmIKBKDaQRPEApg9GuKZEeQSY8fL3p_s4L52Ohs7e19sT5g577LL_3ENqecFwCc7V1Tfh04I3t-NR1Ta1DPbt2oXgkwvd-bzLyEieDq6u0rUdO05lBzn1DsdOsRfeIsHlMYpJUtYEY2WMaM_ArBzzDjLHa4k5grUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گل‌دوم‌سپاهان‌به‌فجرسپاسی‌روی‌شوت دیدنی احسان حاج صفی کاپیتان طلایی پوشان دقیقه 38
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31203" target="_blank">📅 19:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31202">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkFYrV7LXuUxqYtM8mKX0nCrQj0g-FUrXIkSSX7TQ1M-sxqPgQEpI80hDf0REj2YskV_ERyovxMiBtHoCnrPlxiYifgGd84HY4aRTUWa12aUJ9lCzxbfy575c__zY9Tp9YGqkTds-s-l7oXrN3EOYAXuCTAyVpR5X4JnSKHLJ4TynA62lyM2EQ7DStEI0EI-zTwrjpEL6YMwvgEv488Vrb5PFqInXJlISRV6co92F7Y7e2uvsHcCU63kA7ZhXnQaHXOUWQS_2nRsawxvsAX3XJCWZmHCGRd9AkwZKYYxgeKNVLIQq6jDd0LpY7ZFJGyes30tCXLliwuiXURuoLCzig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خرافات جواب داد؟! یاسر آسانی ستاره آلبانیایی تیم استقلال به دلیل مصدومیت در نیمه اول دیدار با تیم‌تراکتور دربین دونیمه تعویض شد. آسانی چند روز پیش با حضور در برنامه عادل با او گفتگویی داشت.
‼️
پیش‌تر نیز عباس‌کهریزی، پوریاپورعلی دو بازیکن  آلومینیوم و پرسپولیس‌نیزدچار…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31202" target="_blank">📅 19:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31201">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194218a84f.mp4?token=TWueapx8FwRY14O1xnN6DAwmkn6o-kg9Dtj8j2WOleXV3RL8TuQsavCtNG2nny8PKUaWXS0Pc838yJrF88HRD9LjbZKlcvD9fUvSl60z0tRQmQUW8r4XS6wH6u8SFjy9n5EJvTrbXSe6uaSHFcl6oLZYuIOmIPMP5gNUSPUwuoYU6MzkvLKpBLtC8_KbXcahQZdYsywx6inf7nKV0ojQgmfG080WHTYcpxbMbgUeVeLf05ICPida-kWfzfIp8xMTrz9tpixPnHQjxQImLT2NhcyACiSTCinz2LYBk_KdMITstbaZgS8Un-ZiAwqKhdmK3SNkx85jA76TiQACUIJOL7m8VA0tCkrYaVeUxIq62BSHH8JhFMmSLhBiP1vPy9beaZY5LGLJWDqFYTRj7LrQT5fVH64e-_joo5CH1lRo_jYzC2VUUn10cOIdyu-e0I5NgehmQPsIY0hJ3vAskVhunAmkcQRJn6-o88q_lyNpmEtCSWtCRqBtb1XATCrQ7kZPhVbnSE8-jaDFt8RL8AXq3KEqi5IrtX8HZXW4P5U-xRVKk2QKWHKRGWIlwC5Dq4T5e5xqhE7pNGWf1MPpauv5-f4ndmcETgzPk59MYY7QzakwkNqpo3P0LNBwUXg9DOv6l--MAdLP1JVVFFRZ3hUoZhKKw8wTGHowq4_FYLmxr7I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194218a84f.mp4?token=TWueapx8FwRY14O1xnN6DAwmkn6o-kg9Dtj8j2WOleXV3RL8TuQsavCtNG2nny8PKUaWXS0Pc838yJrF88HRD9LjbZKlcvD9fUvSl60z0tRQmQUW8r4XS6wH6u8SFjy9n5EJvTrbXSe6uaSHFcl6oLZYuIOmIPMP5gNUSPUwuoYU6MzkvLKpBLtC8_KbXcahQZdYsywx6inf7nKV0ojQgmfG080WHTYcpxbMbgUeVeLf05ICPida-kWfzfIp8xMTrz9tpixPnHQjxQImLT2NhcyACiSTCinz2LYBk_KdMITstbaZgS8Un-ZiAwqKhdmK3SNkx85jA76TiQACUIJOL7m8VA0tCkrYaVeUxIq62BSHH8JhFMmSLhBiP1vPy9beaZY5LGLJWDqFYTRj7LrQT5fVH64e-_joo5CH1lRo_jYzC2VUUn10cOIdyu-e0I5NgehmQPsIY0hJ3vAskVhunAmkcQRJn6-o88q_lyNpmEtCSWtCRqBtb1XATCrQ7kZPhVbnSE8-jaDFt8RL8AXq3KEqi5IrtX8HZXW4P5U-xRVKk2QKWHKRGWIlwC5Dq4T5e5xqhE7pNGWf1MPpauv5-f4ndmcETgzPk59MYY7QzakwkNqpo3P0LNBwUXg9DOv6l--MAdLP1JVVFFRZ3hUoZhKKw8wTGHowq4_FYLmxr7I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
آریایوسفی ستاره‌سپاهان به این شکل گل اول طلایی‌پوشان‌زاینده‌رود وارد دروازه فجر سپاسی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31201" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31200">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b6aefbc83.mp4?token=Erp9t_pZJacdCEwkI9nZBs4NrVpg3lEg3uoc-vITs9mwFlAqUe4Uc5hZq_gFZnX6T4UXavGoVC0oYpqdVBE6CLA04AoxV9N4SmGiwyJKr6S_-lXvSt_nTPLYo9sv1BvByd0dMKnyc_RZZuLp5YNOiYQBZroZ2apXyyCOrpsssfj35AcvMD4xFFahLKo73R26s5fdvyYVQWz0JV3lnfZnYZLjDwjd7cCFtTx_LFbr4QijcM3nh4hCM0fLPGBLXF0N72BY5ei_1P1BZiTNi6ET_dimlN8oFVkdmNffgTXzbwAffnqGGf42aMfu8hhquhXjt86G4VTPV8I3ds1ECawHtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b6aefbc83.mp4?token=Erp9t_pZJacdCEwkI9nZBs4NrVpg3lEg3uoc-vITs9mwFlAqUe4Uc5hZq_gFZnX6T4UXavGoVC0oYpqdVBE6CLA04AoxV9N4SmGiwyJKr6S_-lXvSt_nTPLYo9sv1BvByd0dMKnyc_RZZuLp5YNOiYQBZroZ2apXyyCOrpsssfj35AcvMD4xFFahLKo73R26s5fdvyYVQWz0JV3lnfZnYZLjDwjd7cCFtTx_LFbr4QijcM3nh4hCM0fLPGBLXF0N72BY5ei_1P1BZiTNi6ET_dimlN8oFVkdmNffgTXzbwAffnqGGf42aMfu8hhquhXjt86G4VTPV8I3ds1ECawHtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
سپاهان محرم نوید کیا امروز ساعت 18:45 با این ترکیب به مصاف فجرسپاسی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31200" target="_blank">📅 19:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31199">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nURN0Cck1ydZsgW4MjXV6wSlPQ2KM6311UmoO9ztsQnBe9K-Blti8yD2ejQui8vOA9lj8qNwuMRlxa-o7M5r37zQZ-eIl1nCPVus2OhkQOwMC4CcnSAtLg3Uesw2OS6VUbssE8UyCtQJ5jwwy01_cHfhyQrukrO9FUAN8aklbR3KdyXQCZe6JHNiM4IVq9NQM1zKRV100ucJIECJfg8m_qURtxU4wKIXls68JKVRpdq7Sdr_R9TI7D_BasXa7h5rj6mPk6vfA2ibcm8NX5Va7lSuTab4a_p5dVKNipbsjaO_Cm8F_Hp1aYHs9XNA1N8TkwN-Oj6l2OgxXojC5u_xxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بالاخره آبی‌ها گل رو خوردند؛ گل اول تراکتور به استقلال توسط سید مهدی حسینی در دقیقه 74.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31199" target="_blank">📅 18:57 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
