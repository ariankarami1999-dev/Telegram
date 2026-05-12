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
<img src="https://cdn4.telesco.pe/file/JlWpJ7xmNsJuKeO273cEC5OLqsPNU0TLALW9MvYlpcS5FWl7rmkg3g6Wp8739Tdo0IrnEWvQYWFGDOIMYbsug_RgFLYx8hcIclJZx-b-4M-6GnByREquHO8ZEnXMAWAlblaKC2gPNfaLmxK4AGX_vniUpQRcXDHJaGZdDWQOTQDrG5Q19xctlCdy7kpzcAeD_tk0l8aEAYkYI9P5ZxKyWcDCPLFFrCFkGXw06azEUmHMDGqlMqyCf5VNVGOluX1H8f3L_llMtGh00PyIfhtqL7m18sx0YohlWKgr1hYCw7rSpg2l915RbvN5rBxwWGv0wUAUCFQ0_V1VE7l_JQuHhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.84K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-23 03:22:36</div>
<hr>

<div class="tg-post" id="msg-16232">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نیویورک تایمز:
برآورد فعلی این است که حدود ۱۰٪ از پایگاه‌های موشکی ایران به طور دائمی توسط حملات آمریکا از کار افتاده‌اند.
۹۰٪ باقی‌مانده پایگاه‌ها و سایت‌های پرتاب موشک در سراسر کشور
«یا کاملاً یا تا حدی عملیاتی»
باقی مانده‌اند و احتمالاً برای از کار انداختن تنها با حملات هوایی بیش از حد مستحکم هستند.</div>
<div class="tg-footer">👁️ 459 · <a href="https://t.me/SBoxxx/16232" target="_blank">📅 01:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16231">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">زلزله های پیاپی در تهران!</div>
<div class="tg-footer">👁️ 554 · <a href="https://t.me/SBoxxx/16231" target="_blank">📅 01:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16230">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">چرا معادله روسیه—اوکراین برای چین—تایوان برقرار نیست؟</div>
<div class="tg-footer">👁️ 616 · <a href="https://t.me/SBoxxx/16230" target="_blank">📅 01:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16229">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">When the Fake News says that the Iranian enemy is doing well, Militarily, against us, it’s virtual TREASON in that it is such a false, and even preposterous, statement. They are aiding and abetting the enemy! All it does is give Iran false hope when none should…</div>
<div class="tg-footer">👁️ 792 · <a href="https://t.me/SBoxxx/16229" target="_blank">📅 01:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16228">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDonald J. Trump</strong></div>
<div class="tg-text">When the Fake News says that the Iranian enemy is doing well, Militarily, against us, it’s virtual TREASON in that it is such a false, and even preposterous, statement. They are aiding and abetting the enemy! All it does is give Iran false hope when none should exist. These are American cowards that are rooting against our Country. Iran had 159 ships in their Navy — Every single ship is now resting at the bottom of the sea. They have no Navy, their Air Force is gone, all Technology is gone, their “leaders” are no longer with us, and the Country is an Economic Disaster. Only Losers, Ingrates, and Fools are able to make a case against America! President DONALD J. TRUMP</div>
<div class="tg-footer">👁️ 764 · <a href="https://t.me/SBoxxx/16228" target="_blank">📅 01:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16227">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sl6WYwCEC1IkM-F1lasw4HK6c0qsGFuKkvkxBkZnZU1XpE9iOWfKorC1eWjfE5F7To5h2Zj-oI9h8EXkoaJZkCSJZYoL3EPr8CFG-SmcGGUaXkcK2FtyqJm8aEWzYDqcqved7i-abmAAsKF7p4ktJqAdWXSmKOpeBE8CvtbSyK7E_5Cp6B5mPQGRc91OGHdvn-168F9ZKSg4A7eS4CE8rDMBY8G0dWlfUgDdkP1JAxhTMCYy79aMOkCbx6u8nCx98_SIsJPo6nFdWBaD2D2dAItSt0zRYsQgSb1ru6rcK86SbAqkOw-z08Plvq_ESlPKzU5KSU6jV6lIK9iq7QHabg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#URA
— D
#سهام_خارجی
این یک فرصت ویژه ایرانیان خارج کشور است. صندوق ETF اورانیوم می تواند در قالب موج 5 خود دستکم 70 درصد رشد داشته باشد که در چارت می بینید.
نظر به مسخره بازی ما در تنگه هرمز، احتمال هجوم سرمایه ها به انرژی های جایگزین بالاست و انرژی هسته ای هم یکی از اینهاست.</div>
<div class="tg-footer">👁️ 880 · <a href="https://t.me/SBoxxx/16227" target="_blank">📅 00:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16226">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">چرا_آمریکا_به_سوی_جنگ_طولانی_با_ایران_می‌رود.pdf</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SBoxxx/16226" target="_blank">📅 00:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16225">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چرا_آمریکا_به_سوی_جنگ_طولانی_با_ایران_می‌رود.pdf</div>
  <div class="tg-doc-extra">347 KB</div>
</div>
<a href="https://t.me/SBoxxx/16225" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترجمه یادداشت تحلیلی Foreign Policy درباره احتمال فرسایشی شدن جنگ ایران</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SBoxxx/16225" target="_blank">📅 00:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16223">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kl4SW6OSBpuUDLAo9AFfsuzW7AwqFllLff63kxvx9kVrYG8nnxSaI5VOOAnoWsrQ_riGSly82BhkZ9F4KFkQ8NFdc_eS5yd9EkCpfGMGy0o2RTTmxhshZupYbQm_cSUkcs_-qBN4Yle4v_xM1uUJGF5NTytngD80W0VNd1TWthy4mnwB6BMPmr1d5UAR7gopeEQya85vnYnHsuvzX5fmFMBXPE3FyF1HLUOHLqkL9n5UUMPD4U2tVoaP92OHPv8zpNQg0tdr-EcmfBGftMgfGowuSpZWAusUrzYFB0Z1u_9UnvO40M2wtSf5LHeL-jehznfhhcYpSHZzCCEfuM98MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای نخستین بار از سال 2023، رشد واقعی دستمزدها در آمریکا به دلیل جهش تورم ناشی از رشد بهای انرژی، منفی شد.</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SBoxxx/16223" target="_blank">📅 00:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16222">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">زلزله های پیاپی در تهران!</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SBoxxx/16222" target="_blank">📅 00:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16221">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLldwi9JFbdW1otUgwV-gzQ0kqf6J3ifVR8j5A5frqE0X6njDZC-oI4EGNOSRWEXN6VZiP-MymmD4eTTl5BoYJhjLGWZExJgP9IJs_n7hm5LhLNS8r-mgffYze6UtmkSGjBqtQBxyTQhQvLJ-azWgdjENa3nBy0WkARGegpt2RB0bJ2bI1ToVu_APHjmCm4lOz_KMU5thi6Yq1cOwHziwuBPnIvS_sdpdGG9WbGTxpDu4QbPrxIb7RRMDeYewqNZeAEwG0ZDcm4bqWf0h0-1zuaB5KC4dkzwIMA-DfAigAzFyjB3BnwLfptSvfMChi8EghrEgMTc5y7_kHS8KHnIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SBoxxx/16221" target="_blank">📅 22:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16220">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">منبعی به خبرگزاری فارس گفت که ایران وارد دور دوم مذاکرات با ایالات متحده نخواهد شد مگر اینکه چندین شرط برآورده شود، از جمله پایان جنگ‌های منطقه‌ای، لغو تحریم‌ها، آزادسازی دارایی‌های مسدود شده ایران، جبران خسارات جنگ و به رسمیت شناختن کنترل ایران بر تنگه هرمز.
بر اساس گفته‌های این منبع، تهران این مطالبات را اقدامات حداقلی برای اعتمادسازی می‌داند که پیش از آغاز هرگونه مذاکره جدید باید انجام شوند.</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SBoxxx/16220" target="_blank">📅 22:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16219">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTrWPy3OFRLNMLZJ74abaB5H1CkbO_HXreMYNcN4CbFsftiha6OuPHJRzxlLtKROaUO7loGaYI-ayCRPiROwFUvSE5Yhiz5ZBnYLpBWumO-SCRAQnulTBOB77aJfM_ntYxkahoO18tG7L_tGB7MCmpSa36J00ntM-Deg5Pon-EW0G4_vmnebnK9U8V55JyaWn4OuO9YEhEqqQUbHvaWy9stk4a-P7JH8aOie2ygg-DYDV8a1GeDDm5a-W52x-inA5QnJgMUII9usqXqGTWK22z2FGj3qTOXkbyek-FDRB1dm5CFSSY6iwie2Pi1JzNfB3He9O4KTvwx_TDoDVuaBDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توزیع ملی شاخص فلاکت
📊
بالاترین  مربوط به ایلام و پایین ترین  مربوط به خراسان جنوبي</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/SBoxxx/16219" target="_blank">📅 21:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16218">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBhched27f_x6l4I08S5D9NmKBrqsijq81dWFFki3z8vQT0RHeQ10T3J9FCGpUC_MX7bVqnNiKNsqLPc6Ktb5nU9iSjNGP1ASFc3wt2XXevYdi5qixJCoL9nCr52iFAUBwRG2GDKQ4BKXgzz0HnA-wcNPWQOH-AXoS54VB7Etqi6Qb34tB0KtsBGlsTgJGc1ZaaMHMWISCePbEiqIH6o_3HWZ551mEhsoH_09fNR0iWQtWGN3vjqtOTfvUKAJMwJt-JLCVak727BUSGqwHn299u_TrLq5nDOYJMZTJRIKpBQC5DOHBvOIDK2MSu9t-OGzfjPobe7VPYenEzhfXzWtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هند قصد دارد یک بندر استراتژیک در یونان را به دست آورد.  بندر الکساندروپولی در نزدیکی مرز ترکیه  یکی از پربازدیدترین بنادر مدیترانه است.  شرکت هندی که در مذاکرات با یونان درگیر است به احتمال زیاد گروه آدانی است.</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/SBoxxx/16218" target="_blank">📅 21:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16217">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نتانیاهو از تشکیل اتحاد جدیدی علیه «محور شیعه بنیادگرا و محور سنی بنیادگرا» خبر داد.  این اتحاد شامل هند، یونان، قبرس، کشورهای آفریقایی، کشورهای عربی و کشورهای آسیایی خواهد بود.</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/SBoxxx/16217" target="_blank">📅 21:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16216">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOVnJOe6WCwlOasa4F2iECYhHP5X7anHCr9XvZP6NRRHnZzTKYkfxCUzTYlPL3VHUwkhPj8EHq-YpjaovZkz3d8-2LRdF4ULJ9L1Nb9eb_YpaOKVHZwFln_8XKNGa9GE_FzYn1szhd3e8licUSsy7nUzNZbwcNTaiZQ3HVX5Rj5Q_dFR34TDWdlYN3j5-bOouG2lMTarONuZ2A8RzAq5k6GpiIUeOeHB-r4O20D48T0riX1IWoUMurXEIVyiLyYh3N3pPpkZBWzcR2uqb5gnUTLan-f9yjO8DnF31u6ml6zYZu9ggDWDfCTtLHRqMBhTotpMLHGMqn-k32x4AFdgfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه تیم ها دارند تدارکات عالی برای جام جهانی میبینند ما هم داریم اینطوری با خودمان ور می رویم!</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SBoxxx/16216" target="_blank">📅 20:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16215">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ژاپن معاملات تسلیحات مرگبار را در جنوب شرق آسیا پیش می‌برد  وزیر دفاع ژاپن، شینجیرو کویزومی، روز دوشنبه در جاکارتا با همتای اندونزیایی خود، شمس الدین، یک پیمان همکاری دفاعی امضا کرد، و پس از به مانیل خواهدرفت؛ جایی که نیروهای ژاپنی در کنار نیروهای آمریکایی…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SBoxxx/16215" target="_blank">📅 19:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16214">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOQRHlS-pm_JPcy7JaU6410YjBSZop7LFgSgksZL3HOqzvChP4MmJ1jgxwErXSyGLfm8rYIcCFtqVi4Dxwhlg2bqIXSgXUE6y95ZoqnUGmtO5xvsBmst8MrcG5L5Kp7c6D-SiO5_Xmefb-kSnsOv3RS0Wq3mCKD9jxOUhLxLGOJA8OL1tt-lvz648JwUoMyilwIG7VdjE70poNfzoC1HmZs3Z9_Xv1tliw6QOvDLdSnn53LNTZ3-1Sh0pj2MabrplfxxrS22Y5IlvJNzba0f5HXG7Gxlm_EKcDIP9oMn2wtW91c96C_aiLVs51237zTpch0Kz4usjtDxEj8Me95J5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/SBoxxx/16214" target="_blank">📅 19:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16212">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVQJ3NWNXKhVL1dYhcPBJr90Hod2DbNJUINjLFS-s95r8kuYGvhtwGJsgNStITS7gn800pgZ4reDXcKjZ16GNOwiC-v3gVPUc2xqzOFdQOtV7eLUdEyX5zlP5soUnE0ewZzTuXzCRfFmyFz8t4jzAJynociHJDlh9nsTHixnWH761RTj59vhZoroDoOfXw0pZggvy5KFvQMNIsp0NIWYmWWeZByJY5ivyXLrWxS1pJYPKQdRVwUIlFk03-oE5xHaY2cCXIu3TvxU5d1ZYaK32aigqvTV9Qgu-p8nInCK_--O6QPTz1oZYKgIdddjRN0C8HUuhxY9AEj6-c_HCIOUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ !
استخر کاخ سفید را گفته تمیز کرده اند و این را برای رنده کردن دموکرات‌ها سوژه کرده است.</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/SBoxxx/16212" target="_blank">📅 19:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16211">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ درباره ایران:
ما صد در صد به گرد و غبار هسته‌ای دست خواهیم یافت و کل ماجرا را خواهیم گرفت.</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/SBoxxx/16211" target="_blank">📅 18:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16210">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترکیه یک کمپین عمومی در اروپا برای ترویج پیوستن کامل خود به اتحادیه اروپا آغاز می‌کند.  شورای روابط اقتصادی خارجی ترکیه (DEIK) نامه‌های سرگشاده‌ای را به سران کشورها و دولت‌های آلمان، فرانسه، هلند، اسپانیا، ایتالیا، لهستان و بلژیک در روزنامه‌های معتبر کشورهایشان…</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/SBoxxx/16210" target="_blank">📅 18:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16209">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترکیه یک کمپین عمومی در اروپا برای ترویج پیوستن کامل خود به اتحادیه اروپا آغاز می‌کند.
شورای روابط اقتصادی خارجی ترکیه (DEIK) نامه‌های سرگشاده‌ای را به سران کشورها و دولت‌های آلمان، فرانسه، هلند، اسپانیا، ایتالیا، لهستان و بلژیک در روزنامه‌های معتبر کشورهایشان منتشر کرده است.
به گفته نیل اولپاک، رئیس DEIK، پیام این است که عضویت کامل ترکیه در اتحادیه اروپا به "استقلال استراتژیک اروپا" و همچنین امنیت جهانی کمک خواهد کرد.</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SBoxxx/16209" target="_blank">📅 18:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16208">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nERu_0JKHW7At2a3yWR0gk2SiwJadykIeAuMO7SdwGqr5_ZjMDgNvA3LDBkm7KlYUz8g_PWlsIggfqUUiT5-3bu2HdduI7TJkakwG4siM1Y172htTbyE_QEJ1AdO24y50SyNM8SBqM2a3XsAdBynhzLyC7TtxO4FqNPcIC0mtZWxjJIcxlAnTvcF4tNQAEzhO1sy1dRof9i4qNJ_M5Wwn4Wo8LAafjFsmQrBuncxMkL8-_8ExJgIdRoACxE_SvglYpkYvRB3FFLpu1Y0DnyQk6f397QEZGMDLsiaIjXb29XHcpfwGfLg1saJKeiij1l1d_MRezsvR96W9Ba36L1gcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#US500CASH
-- H1
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/SBoxxx/16208" target="_blank">📅 18:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16207">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔹
وزیر خزانه داری ایالات متحده آمریکا
:
تنگه هرمز خودش باز خواهد شد</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SBoxxx/16207" target="_blank">📅 16:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16206">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فرمانده عملیات استان کربلا:   نیرویی که در ماه مارس در صحرای نجف بود، اسرائیلی بوده و بیش از ۴۸ ساعت نماند.</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SBoxxx/16206" target="_blank">📅 15:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16205">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حقیقتا «الکسیس میانرودان» لقب شایسته ای برای عراق نیست؟!  تل آویو - اسرائیل برای پشتیبانی از عملیات هوایی خود علیه ایران، یک پایگاه نظامی مخفی در صحرای عراق ایجاد کرد و حملات هوایی علیه نیروهای عراقی انجام داد که تقریباً در اوایل جنگ آن را کشف کردند.  به گفته…</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SBoxxx/16205" target="_blank">📅 15:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16204">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlCDRE5RIVV69vhoUXOG1C0UY62F-MlNP1zJT4ldvjPvorW6wV1D5TM8yiq7p_Cd0PTqbCbF-RVYqi7UFdDC0jTDZka3447pn-x8p8yUdudtvp0uzxH-DIzgJ_27MIR2XNXdqv7joO3BgWQoVN6M3Xi_d5M-vCro45JX6hJQjFRqkDNdqmfBzwO9G_jkuEuI0xm3stPLvcWUH4jGQnFHbbODUr2-KK_INVK7Oh-Vvq5iL57q36typ16qjCsq_ZUNowbmSVNeAF-vMlIkTgSH6S9RszebWxznQsmsD_oyF5oaU2LL_yDvFSGCTgLSjR99_voISOCcLLhMv_fcidsRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از یک شرکت کننده در رزمایش ضد هلی برن «قائد شهید» سپاه محمد رسول اللّه تهران
به نظر می رسد احتمال عملیات زمینی یا هلی برن آمریکایی ها از دید سپاه پاسداران افزایش یافته است.</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/SBoxxx/16204" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16203">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yj2To00AcNapITa8D0yuUeFFbcyslTZXjonw4bl1Pjwol10ahfxKAkQMTRAklrnFtGbCMx26WCRMufj1-10CDNRPG0kjbqirI8PW69XgNQ6eHqVysqrsotWYsdtYjS4NZNOSpD3URTwi5uJAF-pPGK-MfkzTCVyaihhLX6bsNkJ-iPu1UCLDNIkMzo0iVrzVDwiGaycdFkNoO81tBsGoc11f4FTb91OJN0adS_-Znx67IovPojVplCsZqSjY0RyUtjLzEgtp63HGqDC96wl4HbjlwWVVkq15y6bBqAor8npxw_v3tGbHb_Gy3Q3QUSmQlYHAgN_pGg213BubtrRVFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزان وابستگی کشورهای مختلف به واردات نفت + گاز طبیعی مایع صادراتی از تنگه هرمز
کشورهای شرق و جنوب شرق آسیا بیشترین آسیب پذیری را دارند و آمریکا (گوشه سمت چپ پایین) کمترین وابستگی را.</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SBoxxx/16203" target="_blank">📅 14:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16202">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1156AIzSqSAxI4zbC8HBcfvV3lXN6-BX98oho3jv1OxDoLeGq4A0kOI3s60FqQ6xrzG7-ilOZl7-_lgBI3QF6wu-sQXDv-NtPo0A2JkBLtmSgVe7go2E09DU5YPrqX-ZwkLWSjqQk5O1c5f9-OXnl5SuW1ZIrT9nwLeKvEoP2Qt7mjwgwu0QAoPCnTA0S6RFa1ip69BSconDtHrPLyTFk5IX8rNurxE8I9p9nTnU4GVq2V-ThDGc8hyNSvKHREFW1FBT6TCFxUmslZo1ce2NZFO-n8kldi08Ff405spKIjuDNOoNW6rdtktdHtZa61v-T-PPMkzmHyu8mPyEWzXyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAGUSD
-- H1
در محدوده مدنظر یک اصلاح 4.5 درصدی داشتیم. اکنون طبق مسیر ترسیمی رشد بسیار عالی داشته و در حال نزدیک شدن به سقف کانال است. از اینجا احتیاط و نزدیک کردن تریل استاپ توصیه می شود.
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SBoxxx/16202" target="_blank">📅 13:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16201">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP(Cyclical Waves Support)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-gBv0odQDAJy2G-98ThKSjJ_GyfuoHO5CiuflZC9cIc6HrqAh-pm5lbdzVJYE15KQzagpy2eZSJsuuuEQREpmTLdyaqXozVVXQRgKTkEjL9Gr0bTET8gmju-GPzFEdwpMLZkX68RtKIxcWJoDQxrQH7LKkVl1zlc60twx6sgiP_7deoXPZ76WMlDn251Hv9_ubt9qT4FbynO6nTY1r89whrhIHZsLehdcVcb7aaAjVOcYh89z0FciR16sBopKFuQYx9VfV-9zlbHM8aL_wUsE5IpYROeZgdP28STdygg9GI3hunZjSZS5LmTrZMoGX4925oTnEqa3TZNfoicG5TLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#XAGUSD
-- H4
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/SBoxxx/16201" target="_blank">📅 13:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16200">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uY0UO1RcD3sMKn3L-oKnJbilHn9_6KFhfPLa2G7VOqUS0TLbtosizOp2klTnKlKLS2y7yL53Zkg4p4H5Bvu2pBEldrPiD8vd1SRoL3bx2oEcCkZFu-jXaD5mk3tnfF2WT7sIbLogExDPjqzOlLnIZpNuW4HxN5f1SaFv7OYH1Rn8V2V30hgmPLMmSdYibJk0e1dkpj850hsw3PfCptTzK4W5VHtRfLFoz8-WzybvWNZMA37kNpVKAIB_U5p3td44FnePFb_igYUrFPWKSbiIbn3tASkxgP2v8JAUaIb1-iuQ3xY9aXB3qd9moTLjBzO2YBq_fheVaIq5Hd8a76CmYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ایران و فشار شدید روی ذخایر ارزی و طلای ترکیه !  طبق داده های معتبر، در یک بازه بسیار کوتاه—حدود دو هفته در دوره تشدید جنگ —بانک مرکزی ترکیه حدود ۲۰ تا ۲۲ تن طلا را به‌طور مستقیم فروخته و علاوه بر آن سوآپ‌هایی معادل ۳۰ تا ۴۰ تن طلا انجام داده است.   در…</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/SBoxxx/16200" target="_blank">📅 13:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16199">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">CBS News:
پس از اعلام آتش‌بس میان تهران و واشنگتن در اوایل آوریل، ایران چندین فروند هواپیما به پایگاه هوایی "نورخان" پاکستان اعزام کرد.
این پایگاه نظامی از نظر استراتژیک حائز اهمیت است. منابع به سی‌بی‌اس نیوز گفته‌اند که پاکستان با اجازه پارک هواپیماهای نظامی ایران در خاک خود، احتمالاً آن‌ها را از حملات هوایی آمریکا مصون نگه داشته است.
محموله ارسالی شامل یک فروند هواپیمای شناسایی و جمع‌آوری اطلاعات آر سی-۱۳۰ نیروی هوایی ایران بود</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/16199" target="_blank">📅 13:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16198">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">#ITA — D  اینکه سرانجام ترامپ برای 3 روز هم که شده میان روسیه و اوکراین آتش بس برقرار می کند و سفری به چین دارد که اینقدر دستکم از دید خودش امیدبخش است شاید همان گمانه زنی را تقویت کند که بزودی یک صلح بزرگ — یا دستکم وقفه ای اساسی در روند جنگ ها — در جهان…</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SBoxxx/16198" target="_blank">📅 13:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16197">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اگر آمریکا دوباره به ما حمله کند، با ۲ بار قبلی می‌شود ۳ بار !</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SBoxxx/16197" target="_blank">📅 13:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16196">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">عضو کمیسیون امنیت ملی مجلس:
در صورتی که آمریکا دوباره به ما حمله کند، غنی سازی ۹۰٪ را استارت می‌زنیم!</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/SBoxxx/16196" target="_blank">📅 13:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16195">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">Secret Box
pinned an audio file</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/16195" target="_blank">📅 07:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16194">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCJJ1NxQ2_xvzWZyyWlkymakS64Dx73YdYgOiRxaiqa5Ux7VW9twTUQySXwlfnw3KiqQkqifLcqUHicnqtR429Uj8SGgSyu54Dta1hU5YCKWSGUpc8tNafDvQlCZ48X1_1tz7i7-_nfdH7NBV2j7LFkvI57UY6fzy2pflDBQtpQH8LQzrg-t-YwYDXgf74QUfR0AV62ftPRgN-POf9GoIKFN8rtExUK1W1j0Z-6xcs8YVBsyw7VENzw9W4MrwYk7uszuvNuu_5BneSAHyNRD6M-b4mom2AIbXtrvmTznDvhNO0HnNCh45XsYXQ4Y5XTU-PquDL2lQBgOeG7cGMUz4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلی مایر از شبکه نیوزنیشن با دونالد ترامپ، رئیس‌جمهور آمریکا، درباره احتمال اقدام نظامی علیه ایران پیش از سفرش به چین گفت‌وگو کرد.
ترامپ از اظهارنظر در این باره خودداری کرد و گفت: «واضح است که در این مورد با شما صحبت نخواهم کرد.»
این در حالی است که گزارش‌های اکسیوس حاکی از آن است که دولت آمریکا در حال بررسی یک کارزار حملات محدود علیه ۲۵ درصد از اهداف شناسایی‌شده ایران است که تاکنون هدف قرار نگرفته‌اند، تا تصمیم‌گیرندگان ایرانی را به مذاکره بر سر برنامه هسته‌ای خود وادار کند</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16194" target="_blank">📅 06:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16193">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/16193" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">یک سری اینجا منتظرند چین هم به تایوان حمله کند مشابه آنچه روسیه با اوکراین کرد تا جبهه جدیدی ضد غرب و آمریکا شکل بگیرد و این سمت ما پیروز بشویم.  در یک صوتی توضیح میدهم که چرا به نظرم این ایده یک توهم کودکانه است.</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SBoxxx/16193" target="_blank">📅 03:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16192">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-t3O6C6n4Ek4q16rPoU4wuYnSC2L31FC9lJ8KEwxpbPRVeyhEp0iXh4tb7maHLnc2Sv04EFl2XYIRnmbX4usTtNoehJgUzeycPReGfbOxoww34Bw62Es5qw6Qxjwl6CaGQeGzletmsUQZwaMtv6pq78-Px9NzKGdUqmT3HRfj_DYNw1yeNDs3w_3tQEgL2UIGbFy0HPRpNdfIx7DF_S195puYpMI83XX1TmH_CZYzcCPKwo-uX6oY3-ZmhpS29hxUfAoU8REa2THWmyNUzDMD3-N-rwKTN1UrCFHs85fVLbdsalcLZHoAhxYTlEqfPFaeTQOc9ffM33gScw25EQ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش ایرانی سی استار ۳ همچنان در نزدیکی بندر جاسک در حال سوختن است.
این شناور اواخر هفته گذشته در اثر حمله هوایی نیروی دریایی آمریکا در بندر آسیب شدیدی به بخش عقب آن وارد شد</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16192" target="_blank">📅 02:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16191">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgOwUg9gfrPBN83Me1ZArUCCe3zJoBQwhpZBx97GYSutULuxfd1vqrPZZ2lhuL-ig71AZEs8cyvP4hIeaART3V0_aRk-jB6lMdSovaajVEpWnqXzd3uAylNLm0v3J334unG0ruqBKOEGCovB67joZHc672gwHhuaIVbkoPo1d5AvfP_-myqxGqak4SwCi4QNlCMj_ho42G96g8XPoL3hSRtr1OCrDqJ6r7Mo5ZaM0tPzLEc2HgTNmIN2j96CWmA_lfBsUwqciR3-uVwrnCf3E619edueNPCO8QgDD_9HvAYM8Uf5pSwdFBCg8EhcHI8kKGsC1EUiMgwwZLdYwC8FIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Rheinmetall — D  ببینید چه شد!  بیش از 23% ریزش پس از شکسته شدن خط روند.  به نظر می رسد واقعاً دستکم یک آتش بس موقت هم که شده داشته باشیم.</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/16191" target="_blank">📅 02:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16190">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrFSfk5lbltR5SsU8d777aCOo3drnYs5zpu93yvcCHYr-tJ4knzmJ7TvIIbYueO2a7uISTS3qsfq4U7FqwnRf61SSdNXJqhB2IieL3dYRIrwn051u9cRDy5c5Ob6FH73XpCagrOOrjcT6DoVIg-URCRkmTEHZj0iSuUiN7JlOY2OBD-s-tsaJvoYUCLcIsDqsOcX5C9gDqbMcgm8eHU9SbFw5Ug47ntmeRJkZ26osT0xJAxo-gJN1N2RXMHfNv3vThnGip6xvYHIS2PMKBgfOqrGxEe5gmxGwuMD8wuKKcLSK5UhIMOh_DwGqF2ImGdb8efFwLqX7xFRf5cPBR149g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ITA — W  به نظر می رسد این صندوق که شبیه ساز صنایع دفاعی آمریکا است در آستانه یک سقف اساسی قرار گرفته که به معنی کاهش تنشهای نظامی در آینده نزدیک است.  در صورت شکسته شدن کانال اخیر می توان با قطعیت گفت که فعلاً جنگ بزرگی در جهان نخواهیم داشت.</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SBoxxx/16190" target="_blank">📅 01:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16189">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNgz7jYlGddj3jyNmyGw_2SYGAzL2d4n62RCygP-aSiS7hVa2KNHn22jmPtvE-OuLZetPyliuDrOnBp1VsGe13XzPq3iTcojKqEoU7-g3NoBumPnboKRQodo4HCLuij1ODI2FkTUkisdMe-inRitjs-A_VMmEDF3QREQebEKRz0FRxxYENeqWGfwP--VfyAVejmrTnyanTNACpZMB-u7fXT3BeM_uKWS8pp6MqwcuzOT8thU9UoBWOnZHskc9kRo76pXc9ZSQr3_PXWIQaSWZ0hz-f6xHWugeEfo_6sGd97sNoFO66GBZgT2Ds08UdVSJBIBVUE-cgwJfuwv5K1RHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#سحرخیز</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SBoxxx/16189" target="_blank">📅 01:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16188">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otcmrGu1FRS96uI172jtF0B0r9Mc5hzEUdqDk8fNutFYgiYudfVREy2EOarr33jnXq0G9UL0xJhT_YWFvpy7Kobg7biK9Wk3b3HNzxWqp9p7nD5WRTkD0VWJyDCMQhb8UE4gb_VTq6JO5himUoKtjXd-8b7AwHbziC6QX_RsyvQkSRKWTjLuxnM42A0diUZ_wsynHGMxmGjG-b1G-5FpEgFq2YC3nMoIUngBENS9Hzrr-MQSC9I57mz2dzpTDF_BYJj1dDWzFp7nRcrlqGNTrTZ44O6bfA_fQqwd1yjltGkdB-sHjcDNxnDdKr9lmN3kRgtKBgbF0fnzoWe0iqHpVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#سحرخیز</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SBoxxx/16188" target="_blank">📅 01:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16187">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caucRh-gr5iveEegLEK2sg75vZrCPt4UMrFJBv3pg7b8dPO8vjCu1k4la__0HtLb9unMTS6WYuv_kEHGXPAQ1mIhKOEpqPnFsESKddAYpVbulR92_fNCO2V5X0FTkHsD-ZOhxemUjW0oG-ZUJXCyiXddfoZzhu6q8md9OC886ZLxxLmpCz0PAOZI9etEi3QE9W7769o92D9ldlSsvYvA9lRR5L8rkiiofe5fn28mobpCo5sjwJmOdu8kQDv-nNZtk2AShG_ga1dJ7JeDluxz8rQyQ927N8t3mjYnQH_-QYYYgTHMkXUbbNpLkiRWtfxU1NjsRaknB9r1mgBT1ngJbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نهال</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SBoxxx/16187" target="_blank">📅 01:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16186">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرنگار: آیا فکر می‌کنید آمریکا باید همچنان به تایوان سلاح بفروشد؟  ترامپ: من این بحث را با رئیس‌جمهور شی خواهم داشت. رئیس‌جمهور شی دوست دارد ما این کار را نکنیم و من این بحث را خواهم داشت.</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16186" target="_blank">📅 01:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16185">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGdLNKEM3iGg0YYWaF-dGRVQZuwZWJr2vIs8G9sRLjYv_liriV0yFjh8TcquYI3_SuSe2IVZTw9iJWB9Vxy84zz9TxNDU1tO2ldKDe669EdaoDboK1XFBiDi8_lxUkUQo6Vx0zKjNObX3NASSv2RZq-tiTJqXz4mtbPAvoKXnzqFlvW_V8F3asYpNSU16VB-x23ipNq4I6_VFKjX_iWXo4tUua__7Fm8mjgkrijdDEbPjEcxXFYDz-D9YDbxVp6cvQDhVWkIGPe32g9y-4TxtAFeB6HEb1y76J5Apald2RBDEshfz5moq13mhCtjyqg5uUvUtAc43UzHSFNqQ3SoZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دونالد ترامپ
:
من همون حسی رو دارم که ۵۰ سال پیش داشتم شاید به خاطر غذاییه که میخورم شاید فست فود برا آدم خوبه و غذاهای دیگه بده
آدمهایی رو میشناسم که خیلی مراقب غذا و وزنشون بودن میرفتن رستوران کرفس میخوردن و آخرش تو سن جوونی مردن</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SBoxxx/16185" target="_blank">📅 22:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16184">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP</strong></div>
<div class="tg-text">قانون‌گذاران مجلس نمایندگان ایالات متحده در حال معرفی لایحه‌ای برای ممنوعیت خودروهای چینی در ایالات متحده هستند!</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/16184" target="_blank">📅 21:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16183">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">طراح قانون حجاب اجباری:  موساد به زن ها ساعتی ۳ دلار پول میدهد تا لخت بیان وسط میدان ولیعصر بچرخند.  هرکسی را دیدید حجاب ندارد بدانید اسرائیل دارد به او پول می‌دهد.</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SBoxxx/16183" target="_blank">📅 21:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16182">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">طراح قانون حجاب اجباری:
موساد به زن ها ساعتی ۳ دلار پول میدهد تا لخت بیان وسط میدان ولیعصر بچرخند.
هرکسی را دیدید حجاب ندارد بدانید اسرائیل دارد به او پول می‌دهد.</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16182" target="_blank">📅 21:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16181">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ: با رئیس جمهور چین درباره تایوان و ایران صحبت خواهم کرد</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16181" target="_blank">📅 20:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16180">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2Ze_mZWCw180oZrmV1epOCLlZDE9YcPvvfrgKiiO25IPEStTx4TKOPnNot4fARB4Pi-719N8hV_X_LyBTQzXZ-aEKeqsfP-Tb7ILXXcvI9Qb3FnhIn_hf9WzNQG9E68wWK5salc_6pweWp17taOKRzXLjrb7KgtVhWcaiz9bg-N-3Xub0m89KM261Fr37glS00HCVjWxwKzBx4oN-dHNyO00CelmkqE2Sr2dIlaphf4y6oBnaV6k_S04-WSW90R2FE1vBeFhC1Z8WY_j0jqMIW5eDHSq2WzIlcFKzEjdteTfP15lkgAlH8XIlsfN8CUXVvCuKCUenYPtx5AsttkJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D  به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/16180" target="_blank">📅 20:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16179">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یک سری اینجا منتظرند چین هم به تایوان حمله کند مشابه آنچه روسیه با اوکراین کرد تا جبهه جدیدی ضد غرب و آمریکا شکل بگیرد و این سمت ما پیروز بشویم.  در یک صوتی توضیح میدهم که چرا به نظرم این ایده یک توهم کودکانه است.</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/16179" target="_blank">📅 20:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16178">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تسنيم از نزدیک به تیم مذاکره‌کننده ایران: ادعاهای مبنی بر پیشنهاد ایران برای تعلیق غنی‌سازی اورانیوم به مدت ۱۵ سال دروغ و جنگ روانی است</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16178" target="_blank">📅 20:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16177">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpPddGzrV1-SEzHVZQEmC3AQN8yMEtFotCfKy7O5_OpOAtmMB-n2XTwnegj9qKYBODHrqlQ7rFCqBFBH6rAVzW4N4QXF_Wi-jL0pwI5Icer1QygDioxu6Zp2Pj43YcGBqxcoQw9eIp9Er55D7c4AhCREa_HFFbgvZ4QF_TfcQ1We3-5XWkyUwJ_wUKZcK9UjQamaGCxfsJTAn_ePxw8hTvc-uuenBH2KevvEq5vt4HlzC8tyCN8ZRPKp--uPwhlk3F03L1kXhvzZk44yHoqmHJxXBelkTxFeJ7b72f1FDx9WX5pbktcnd3klUSczrbW-HotRVLO1AvNhh6xFQhyTsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازارها از دست ترامپ دیوانه شده اند</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16177" target="_blank">📅 19:59 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16176">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ به صورت ضمنی چین را هم تهدید کرد که به خرید نفت از ایران ادامه ندهد!</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16176" target="_blank">📅 19:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16175">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ما هم باید مسخره مان را دربیاوریم.</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/16175" target="_blank">📅 19:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16174">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پدرسگ مسخره اش را درآورده</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/16174" target="_blank">📅 19:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16173">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">متاسفانه ترامپ به ما توهین کرد و ما را به دو دسته میانه رو و دیوانه تقسیم کرد.</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SBoxxx/16173" target="_blank">📅 19:44 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16172">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ:
ما ۴ روز برای سندی از ایران منتظر ماندیم که تنظیم آن بیش از ۱۰ دقیقه زمان نمی‌برد!</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/16172" target="_blank">📅 19:43 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16171">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ای گریدم به کله زردت</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16171" target="_blank">📅 19:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16170">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ:  آتش‌بس با ایران بسیار ضعیف است.  آتش‌بس با ایران در بخش مراقبت‌های ویژه (ICU) است</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/16170" target="_blank">📅 19:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16169">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">امروز کله زرد روی Long نفت است.</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SBoxxx/16169" target="_blank">📅 19:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16168">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗
ترامپ: من قرار است با گروه بزرگی از ژنرال‌ها درباره ایران دیدار کنم</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SBoxxx/16168" target="_blank">📅 19:29 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16167">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vI6VHBmH1K8DDDYDPbn7Mr1fYCgmhRbwzpFp4krtIddqttb7m1z_pfG1tQshRZT8WFod2RZ_oEcUm2OYOT6MRisgBp8USDaSkzywF-qwt0TmSm7fUbHqyJmOG_rJcb_TXOLafHIqgPo5TuuByQQoBx_BQXeQOLW97BF_9zOtfRZKbLXAOjZiBay-JG5lMs4AwSORH8CDb20JcR5C91kMf4_GqsIKdGpux9wXkkr4rVc3UG9TWgqOwShpI7CbrbPy6chfc4NCKvbnz-Olk59Zutd4eFp8OUY3ZJPm0V2A3vOL3EBXblZrgrNdAD0z4WNWdXjD4oUHqeGIIbmtVpeMvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗
ترامپ: من قرار است با گروه بزرگی از ژنرال‌ها درباره ایران دیدار کنم</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16167" target="_blank">📅 18:51 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16166">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ به فاکس: من در حال بررسی تمدید پروژه آزادی هستم. پروژه آزادی بخشی از یک عملیات بزرگ‌تر خواهد بود</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16166" target="_blank">📅 18:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16165">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وعده ترامپ برای اطمینان از وجود ذخایر طلا!  در 19 فوریه 2025، رئیس جمهور دونالد ترامپ در حالی که در ایر فورس وان بود، اعلام کرد که قصد دارد از فورت ناکس بازدید کند تا وجود ذخایر طلای ذخیره شده در آنجا را تأیید کند.   این مواضع منعکس کننده بحث ها و نگرانی های…</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/16165" target="_blank">📅 18:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16164">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ به فاکس: من در حال بررسی تمدید پروژه آزادی هستم. پروژه آزادی بخشی از یک عملیات بزرگ‌تر خواهد بود</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16164" target="_blank">📅 18:22 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16163">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مشاور ارشد کاخ سفید هسّت: در مذاکرات با ایران عجله‌ای نیست چون اقتصاد آن‌ها در آستانه فروپاشی است</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/16163" target="_blank">📅 18:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16162">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ به فاکس: ما تا رسیدن به توافق با ایران تعامل خواهیم کرد</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/16162" target="_blank">📅 18:19 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16161">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اسرائیل اکنون از مانکن‌های واقع‌نمای فریبنده با کلاه ایمنی، جلیقه تاکتیکی، ماسک و یونیفرم نظامی استفاده می‌کند تا پهپادهای اف‌پی‌وی حزب‌الله را فریب داده و مهمات خود را روی اهداف جعلی هدر دهند</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16161" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16160">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ht7Bz73lL_QVrlNcptBkUm_9euxQ7DrtSmfgNdcX7OUb8WSAT7n2eYoidONVenc6y_FoZI_dzHD0U0oaO1aZ1EsEZN76j2QQBiNy0qDZ8GoEXKX952t92OsRRsn3tGHjjMQ9VLCOjtKz682HoR2fLH2g2lPg0Ns0XVnT1L0xNItXel4mowOvp1Ok8lpMxSPqbfMX2AI4llPDPMYDvEkJymT280v0MEIixevuIBb_uAaU1aOb1KM7u526TfiFt5ylfmieFnx--SKOZKkw56FnrzzSvjt1r8WTKWx73sYjHOnk0xLqwIBFYPHiPbHcqx2DOW1yAzbGsZebmxAnf6D6Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با افزایش تلفات اسرائیلی ها در اثر حملات پرشمار حزب الله با ریزپهپادهای FPV، یک شرکت دفاعی اسرائیل به نام Smart Shooter سلاحی را معرفی کرده که طبق ادعایش می توان آن را به سادگی ضد این پهپادها به کار برد و خطا هم ندارد.  شیر آهویا، معاون محصول در اسمارت شوتر،…</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16160" target="_blank">📅 14:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16159">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0VqSXU5XMDpzgaxo06fLS71SO1iV2r1RGXyh0VXCEjzqKy9PqUDT_EiySg81zv03XGCxyBdIpcTZ8CLeQNPF7llLU3j7WKPP-3t4G3hA5J5BpNMnpGnWScuGp6vY-ldHRLntUE4PJKrzQKmdhvet1RqDJalPEhM8K25b9xkLpapuSpcTkUih4gcxmknVajkci1mv_nPM3rCVrI5ojiHCuDIpVy-Uu1xrOGa7NNo6iFplJ_GU3Zrb41Jb_ASIQ7otWwOVdaKgya6eWQ_zPdAEKAhNuP8eNoNRFRqfjR_QstV-AFiav7oBUSIOG5cyNh-RBAh3oH5-82PBLDQS3-qyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا دقیقاً در همین مورد یک یادداشت تحلیلی در سایت کار می شود.</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/16159" target="_blank">📅 12:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16158">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پس از رد پیشنهاد ایران  رد آخرین پیشنهاد ایران از سوی ترامپ ورود به چه مرحله‌ای است؟ آیا به معنای پایان دیپلماسی و آغاز جنگی دیگر است؟ همانطور که پوتین گفته است، هیچکدام از طرف‌ها علاقه‌ای به آغاز درگیری نظامی ندارند، با این حال، به نظرم سطح تنش مقداری بالا…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/16158" target="_blank">📅 11:59 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16157">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نمیدانم این احمق چه اصراری دارد که هر هفته یکی دو بار به همه یادآوری کند که دستکم ۲ تخته کم دارد ولی خب.</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SBoxxx/16157" target="_blank">📅 11:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16156">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بقایی سخنگوی وزارت خارجه:
تهران تنها به دنبال تأمین حقوق خود است و پیشنهادات سخاوتمندانه و مسئولانه‌ای به آمریکا داده است</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SBoxxx/16156" target="_blank">📅 11:00 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16155">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رتبه بندی ۱۵ قدرت نظامی برتر جهان از دید من:  ۱- آمریکا ۲- چین ۳- روسیه ۴- کره جنوبی ۵- فرانسه ۶- بریتانیا ۷- هند ۸- ژاپن ۹- ترکیه ۱۰- اسراییل ۱۱- پاکستان ۱۲- لهستان  ۱۳- ایران ۱۴- آلمان ۱۵- مصر</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16155" target="_blank">📅 10:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16154">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqOF6elLBfohEUTIr3eshbv0iDS8gxBJd4FjI-SYXg85_NFXfBCX5W-KnsTkkMIeHnGrAGs73RzurUku9mdYVKa7_cUqWgmpyigSBIqD7MALyJ6Nxe4E4hiFIoGLqKkC92slNnVSGnuAQIx-jytfnKysoKdohPxDwZdMHrY0DMZTkkXQ6rn2Bn8vTq7xSePLShBaR8mr1u3AOvjoSrGmml-NrRTmrUg0V5rDZJwTV7L70p1Fd0wq870TM_77aKRXKPyFua5EhIdx2Y9HIL8CMN96ZZ3an5cjmmx6nZYrAcEZPVne4UcGalCZf5FYpEklRdsFBUNyTOELSc2RxHnmZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کره جنوبی:  «ما به شدت حمله به یک کشتی باری کره‌ای را محکوم می‌کنیم و قصد داریم پس از شناسایی مهاجم، به او پاسخ دهیم».</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16154" target="_blank">📅 10:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16153">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یک سری اینجا منتظرند چین هم به تایوان حمله کند مشابه آنچه روسیه با اوکراین کرد تا جبهه جدیدی ضد غرب و آمریکا شکل بگیرد و این سمت ما پیروز بشویم.
در یک صوتی توضیح میدهم که چرا به نظرم این ایده یک توهم کودکانه است.</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/SBoxxx/16153" target="_blank">📅 10:40 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16152">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">صلاح مملکت خویش خسروان دانند اما چیزی که من حس میکنم این است که یک «اجماع» بزرگی دارد شکل می گیرد که آخرش شاید به جماع عظیمی ختم بشود ولی خب.</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SBoxxx/16152" target="_blank">📅 10:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16151">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سفارت ایران در سئول:   ادعای حمله به کشتی کره جنوبی در تنگه هرمز کذب است</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SBoxxx/16151" target="_blank">📅 10:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16150">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1f-v1jcd_vTH811EAD8krPDtCohILVnJEUNqCNC01kN8GAPpoGslgVopHxbnb23vAGuOllKlCGCGaq6ZGA3Zpsb-6SE-EOzHYa52O0KNqHTNoIfMdPLVxpjO_id760NQqu3GNTEl22YvjovzYno97ablCTs5zbCGrr77HDqftihDuV2vrwuqPRn-F6BTrr06CHuj9mVx8JHkTcWxJaJ0mQHClG6ZggFnFn2e2UOibxc3qUKNAz_coyhGtMysJoxTpRAbIjfyRY8Uk2jaCpKt6Y9kG9Xp30HbiUK-RgXmQQ-JbNy1PHgiUsJMZKA2whhuvtZ12tvR2dWF1dGVlo2FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب از هرمز ۲۰ میلیون بشکه نفت در روز عبور می‌کرد که برای ۷ میلیون ش جایگزین پیدا شد (خط لوله شرق به غرب عربستان)</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/16150" target="_blank">📅 10:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16149">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eu-szVHb5EKms35pQCzpXNNdArDs4ny929JbB0VHzPWd6e7F9ihicerWTgr5Cg0qzhsuCgliwba8rlo1FObaWY6Dh-X5L_KUQjxCU5oBRmTiMz68lSTlY9cgLLYvZMNZnOpIh_P4cdPKEYWV42YyE2AXkhOoG5pDxI-JkIvPaLRz8eAYX9lv9kFUTzRfOPBLuZSB3b0CeP-5zBcViqwObLiCM7IclZ776acykEFSazJPGx7AT2VOddsRLKqegSczkqNgIxjkTWAomW7_eLN79EXghYtYgZblpHwz0wr-0fI39PD86jx-GWZSaVMnFUWPL1ojfVbBQkdcSf5yBQfHuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT
— D
به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/SBoxxx/16149" target="_blank">📅 09:59 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16148">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">احتمال شنیده شدن صدای انفجارهای کنترل‌شده در محدوده بهارستان اصفهان  روابط عمومی سپاه حضرت صاحب‌ الزمان(عج) استان اصفهان:
🔹️
احتمال شنیده شدن صدای انفجار کنترل شده در محدوده بهارستان و اطراف آن وجود دارد.
🔹️
این انفجارها امروز دوشنبه ۲۱ اردیبهشت از ساعت…</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/SBoxxx/16148" target="_blank">📅 09:29 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16147">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">احتمال شنیده شدن صدای انفجارهای کنترل‌شده در محدوده بهارستان اصفهان
روابط عمومی سپاه حضرت صاحب‌ الزمان(عج) استان اصفهان:
🔹️
احتمال شنیده شدن صدای انفجار کنترل شده در محدوده بهارستان و اطراف آن وجود دارد.
🔹️
این انفجارها امروز دوشنبه ۲۱ اردیبهشت از ساعت ۹ الی ۱۳ انجام می‌شود و جای هیچ نگرانی برای مردم عزیز نخواهد بود.</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SBoxxx/16147" target="_blank">📅 09:29 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16146">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">از همه کریدورها که حذف شدیم، یک تنگه هرمز برای بااهمیت ماندن در معادلات بین الملل برایمان مانده بود که این هم تا 5 سال دیگر اساساً فاقد اهمیت خواهدشد.  عصر اقتصاد دانش بنیان و هوش مصنوعی و ربات ها، آوردگاه گردنه گیران و تنگه بندان نیست.</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/SBoxxx/16146" target="_blank">📅 09:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16145">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بزرگ‌ترین شرکت نفتی جهان،  آرامکو، گزارش داد که در سه‌ماهه اول سال ۲۰۲۶ با وجود جنگ ایران، سود بیشتری کسب کرده است.</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SBoxxx/16145" target="_blank">📅 09:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16144">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNGPmXnDB19p1xUChFDuk0rxQw9a4NJs_GyU9RM9J70B9fcWZsVU1z4CfZuPtGBzmBR_RVYu06mj2Hjc1HduO6pkemJOppbS2LuFF0L0F7GFU0vX7I86T7_IGLP8zPpAIfJiUjXV_Vd7Zp5JXEbuwdHXZHI5wRre982DUtwzF9Otxr5YwTzeIjbPkPt534seAqo6O1QhwNOS-XEFgfO-SCAHL51A280cBj2iXY9Ni3zuW6HmVsbuP7fmx-qGatzxY6a_AkDZIBMYil3omcGsRW6WjR317rPkbNAMxc1FOn40YafYotkCSycdUzQriORBMUyKXa6urAorgwb5L0e0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رتبه بندی ۱۵ قدرت نظامی برتر جهان از دید من:  ۱- آمریکا ۲- چین ۳- روسیه ۴- کره جنوبی ۵- فرانسه ۶- بریتانیا ۷- هند ۸- ژاپن ۹- ترکیه ۱۰- اسراییل ۱۱- پاکستان ۱۲- لهستان  ۱۳- ایران ۱۴- آلمان ۱۵- مصر</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/16144" target="_blank">📅 09:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16143">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">متفکر آزاد، عضو هیئت رئیسه مجلس:
تنگه هرمز برای ایرانی ناموسی شده است و به هیچ وجه آن را از دست نمی‌دهد.</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SBoxxx/16143" target="_blank">📅 09:01 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16142">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59886795a.mp4?token=ns5nJ3gTd42Z1UZJvhCXRDPTuX8N5UOIZgZUTy2cR9oWoiwsGK4_Bt0OvdCb2-8IKhitxjsGHhM7qiwoSowt6Vzm2SrarPXdIpVZyE3hfCOm4YumzqxgO54PdBIwG4Kl-wc8qp_WHZ-JArYOuPK8aACwQDrmcPcstSy3A27RqQjMIpPj_Hdo1RULSa15kZK_Jcpr5mR7whF_9nlLWe35EZhDOZGP3rGel2i7oCLYzBCUQ-ErgKrV_xrT_ZHlHg_z1tiViWOlBSHE67HP_qpOR-0BnDGiOFcGvWo_oKMX8b-LMoDPyrmwncTRCMQxcg0924bkvTBdJb4YgO6Y9qXWLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59886795a.mp4?token=ns5nJ3gTd42Z1UZJvhCXRDPTuX8N5UOIZgZUTy2cR9oWoiwsGK4_Bt0OvdCb2-8IKhitxjsGHhM7qiwoSowt6Vzm2SrarPXdIpVZyE3hfCOm4YumzqxgO54PdBIwG4Kl-wc8qp_WHZ-JArYOuPK8aACwQDrmcPcstSy3A27RqQjMIpPj_Hdo1RULSa15kZK_Jcpr5mR7whF_9nlLWe35EZhDOZGP3rGel2i7oCLYzBCUQ-ErgKrV_xrT_ZHlHg_z1tiViWOlBSHE67HP_qpOR-0BnDGiOFcGvWo_oKMX8b-LMoDPyrmwncTRCMQxcg0924bkvTBdJb4YgO6Y9qXWLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو: در ایران، خیابان‌ها را به نام من نامگذاری می‌کنند. می‌دانید؟ خب، البته بعد از رئیس‌جمهور ترامپ هم، چون او رهبری مبارزه را بر عهده دارد.  اما آن‌ها این را دارند؛ من فارسی صحبت نمی‌کنم، اما مرا «بیبی جون» صدا می‌کنند: بیبی عزیز.</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/16142" target="_blank">📅 03:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16141">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بنیامین نتانیاهو:
در ایران، خیابان‌ها را به نام من نامگذاری می‌کنند. می‌دانید؟ خب، البته بعد از رئیس‌جمهور ترامپ هم، چون او رهبری مبارزه را بر عهده دارد.
اما آن‌ها این را دارند؛ من فارسی صحبت نمی‌کنم، اما مرا «بیبی جون» صدا می‌کنند: بیبی عزیز.</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/16141" target="_blank">📅 03:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16140">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">در پی رد پیشنهادهای ایران از سوی ترامپ، طلا با گپ منفی و نفت با گپ مثبت بازگشایی شدند.</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16140" target="_blank">📅 01:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16139">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9_gTdfoL6hJNDD1g5kXib-UnibR_QI3ARu-osS97iJxi5UD8f8qmloMXedoHDFFkIySV8BkAdemfvW-MLQEdYh9LWQVzcHXlbyZHOQ_476yZlO7IPUlHbcxONWrUvpOWhyhds_7rBJlEK1XIquRPaDNI6VZO-7YotlCUXKacpN8mfJOqrHbMn3En1QOSBvRNzPedWiLZSa3vBuHqmSwa8J-Z1SCaxnKLzBfd9VWNm5GfCZyjmVpY2P1OO8NDvP7f0ORc5VBJf96uxKuVHl1qklWkZp-EVvQp9QZJuSFxdrCjO-q9-q1t8Tk51FChzshSOBmv2UpRbC327qXpzQ-qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه چیزی پشت تلاش ترکیه برای دستیابی به موشک بالستیک قاره‌پیما (ICBM) قرار دارد؟
در یک تحول شگفت‌انگیز این هفته، ترکیه مدل یک موشک بالستیک قاره‌پیما (ICBM) ناشناخته قبلی به نام
ییلدریم‌خان
را رونمایی کرد. صنایع دفاعی ترکیه در سال‌های اخیر طیف بسیار گسترده‌ای از سلاح‌ها از جمله موشک‌ها و پهپادها تولید کرده‌اند، اما برنامه ظاهری برای عملیاتی کردن سلاحی در این کلاس، موضوع جدیدی است.
مدل تمام‌اندازه ییلدریم‌خان برای اولین بار این هفته در نمایشگاه بین‌المللی دفاع و هوافضای SAHA ۲۰۲۶ در استانبول به نمایش درآمد و توجه زیادی را به خود جلب کرد. این برنامه توسط وزیر دفاع ترکیه، یاشار گولر، ارائه شد و گفته می‌شود حدود یک دهه در حال توسعه بوده است.
ییلدریم‌خان یک موشک بالستیک دوربرد
غیرتاکتیکی
با کلاهک متعارف است که خود مفهومی نسبتاً جدید محسوب می‌شود (هرچند قبلاً در مورد چین، اسرائیل و روسیه بحث شده است).
این موشک قرار است برد ۶۰۰۰ کیلومتری (۳۷۲۸ مایلی) داشته باشد که آن را دقیقاً در دسته ICBM قرار می‌دهد. موشک‌های این کلاس برد بیش از ۵۵۰۰ کیلومتر دارند.
ییلدریم‌خان با ۴ موتور موشکی تغذیه می‌شود و فقط از یک مرحله استفاده می‌کند که این هم غیرمعمول است. این ممکن است نشانه محدودیت‌های فناوری ترکیه باشد، زیرا این کشور قبلاً موشکی با این برد نساخته است.
وزارت دفاع ترکیه اعلام کرده که این موشک قادر به حمل کلاهک بسیار سنگین ۳۰۰۰ کیلوگرمی (حدود ۶۶۰۰ پوند) است. این موشک سوخت مایع خواهد داشت و از ترکیب تترااکسید نیتروژن و هیدرازین استفاده می‌کند. این یعنی موشک باید پیش از پرتاب سوخت‌گیری شود. در نتیجه زمان واکنش آن نسبت به موشک‌های سوخت جامد کمتر خواهد بود و آسیب‌پذیری بیشتری در برابر حملات پیش‌دستانه خواهد داشت.
در این مرحله جزئیات زمانی برای ورود به خدمت مشخص نیست، هرچند رسانه‌های ترکی ادعا می‌کنند تولید سوخت و توسعه کلاهک‌ها قبلاً آغاز شده است.
نکته قابل توجه اینکه در میان کشورهای ناتو در اروپا،
فقط ترکیه
هم‌اکنون موشک بالستیک زمین‌پرتاب متعارف با برد بیش از ۳۰۰ کیلومتر (موشک کوتاه‌برد تایفون/بورا-۲) دارد. در گذشته رجب طیب اردوغان، رئیس‌جمهور ترکیه، خواستار موشک‌هایی با برد بیش از ۲۰۰۰ کیلومتر شده بود که این امر نگرانی از تهدیدهای رو به رشد منطقه‌ای را نشان می‌دهد.
ترکیه همچنین روی موشک بالستیک میان‌برد
چنک
با برد ۲۰۰۰ کیلومتری کار می‌کند. تایفون بلوک ۴ (با برد تقریبی ۱۰۰۰ کیلومتر) هم اخیراً آزمایش شده است.
این موشک‌ها اکثر رقبای احتمالی ترکیه را در برد قرار می‌دهند، اما تهدیدهایی مانند یونان یا شبه‌نظامیان کرد در عراق نیازی به ICBM ندارند.
ترکیه امکانات محدودی برای آزمایش موشکی با برد ۶۰۰۰ کیلومتر دارد و ممکن است برای حل این مشکل به پایگاه فضایی مشترک با سومالی متکی شود.
موشک‌های بزرگ‌تر مانند چنک و ییلدریم‌خان امکان حمل چندین کلاهک، فریبنده‌ها و ابزارهای مقابله علیه پدافند موشکی را فراهم می‌کنند.
ترکیه در ۲۵ سال گذشته صنعت موشکی خود را به شدت گسترش داده و بسیاری از محصولاتش را صادر کرده است (چون مشمول محدودیت‌های ITAR آمریکا نیست). اما عضویت در رژیم کنترل فناوری موشکی (MTCR) صادرات ییلدریم‌خان را محدود می‌کند.
احتمالاً هدف اصلی، تقویت بازدارندگی متعارف دوربرد ترکیه است؛ به طوری که بتواند اهدافی تا پکن را تهدید کند. کلاهک سنگین آن قابلیت تخریب پناهگاه‌ها و اهداف گسترده را دارد.
فعلا هیچ نشانه‌ای از تلاش برای ساخت کلاهک هسته‌ای وجود ندارد، اما این ICBM می‌تواند سکوی پرتابی برای چنین قابلیتی در آینده باشد (مانند مورد کره جنوبی).
ییلدریم‌خان آخرین محصول تلاش گسترده تحقیق و توسعه ترکیه برای تقویت بازدارندگی ضربه عمیق متعارف خود است و نشان‌دهنده جاه‌طلبی‌های رو به رشد این کشور در حوزه هوافضا و موشکی است.</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16139" target="_blank">📅 01:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16138">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حمله ایران به پایگاه های آمریکایی با اف-۵ !  این مقاله NBC News توضیح می‌دهد که در جریان حملات ایران به پایگاه‌های آمریکا در منطقه، زیرساخت‌ها، ساختمان‌ها و تجهیزات نظامی به شکل قابل‌توجهی آسیب دیده‌اند. برخلاف روایت‌های اولیه که این حملات را «محدود» یا «کنترل‌شده»…</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16138" target="_blank">📅 00:44 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16137">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ:   من تازه پاسخ نمایندگان به اصطلاح ایران را خواندم. از آن خوشم نمی‌آید — کاملاً غیرقابل قبول!   بابت توجه شما به این موضوع سپاسگزارم. رئیس‌جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/16137" target="_blank">📅 00:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16136">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5RyYTkpF1Vgv9WaReJd_fzsay1TC2BAR7M8qYPmTOEWB9kcvRmWPvv83sFhN9XNxYt6Wo9byFRfw7DB-UEGpjEawsvE7JVSlZUjGi-jSvZ_sOwrQ-SpBG6JVURfGUJ4VuMlnyZSvZdLoLCidLZolDpeBwBueAX29GJEqjGPbofPPLt5Ad_XBDJtD5vqM0k16tQD3spXU-vryDIwNJLC9kmaWYhEh6DdqjQveiZDtjoc7N96KQ34EHYIr0Zn3fm9tkI_rFBDs-4Zebph_OuWbFuinLsO1OetosIHcyCBK2dbU8Gm--zGcOQH9R7Ke3K9VyrjLc4ID_SqLiMQNcYNvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طفلی شهباز بوگندو</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16136" target="_blank">📅 00:02 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16135">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBz9zpZBtqRCGOkF1YPGVSycZsLoV8DFXs8wc0JL04g6n62Tr8KcpMhJH9rPBOewWAS_njmfhKsIGpmzQWXB2AfHt2HKVFBIyfoT7vFSG1MadPTx1waconWxGflVVPHuHTZRDkdtKpjJnuVzS8T39Y5fSQsg2AmNJL5Rz_0kK-FYtOZF2ekQhByHgCk4Mb643oNr6MkWW4oDpz6tLp-rMmooUkS4uDx0Vib0YtlKeH7o_UOnRiBvimwcVm5YX9iGMX_i5l6EQG74l_Zu2csW_SCkdwJGd1426GR5BFtNiwxGE6LKmRRd9BWXDv0v1wL_rBvBQYluxYiV-95qp9LFdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SBoxxx/16135" target="_blank">📅 00:00 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16134">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ:
من تازه پاسخ نمایندگان به اصطلاح ایران را خواندم. از آن خوشم نمی‌آید — کاملاً غیرقابل قبول!
بابت توجه شما به این موضوع سپاسگزارم. رئیس‌جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16134" target="_blank">📅 00:00 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16133">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کاخ سفید: آنها دیگر هرگز نخواهندخندید!</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/16133" target="_blank">📅 23:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16132">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jc119ZE5lASPZ9xOMvhTWJQGBhKsgTNXwWE54I-1xTNUFGW5sJ5eBcT06WylTxp7RXCdt1Dshb3b9dS7qzFclAfLPAyXx0WSkTYRZEHLLc_rv4hitcjI5Bc5HW7sGb7XsBtOtxuJZRuLYK3pANU-jcbgaF2_6ZhFGnbKjxHt7pn9MU1st70rv7RpAZoPhv73_eBAVWW7tGnILM9kq5LJbIdRw7PLAIuE6BdMTrUR_s4PalXuPpHZLewfgvRhCIcVYVxC4AZbdHwPccTOlWhB23mbZgVm4XYt1y0ydjaQmyx9AsfXcGDwPE70Tx-S6Rts2JVDbY_50sEYcHAPCptXCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید: آنها دیگر هرگز نخواهندخندید!</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/16132" target="_blank">📅 23:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-16131">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCycFX VIP</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhRb2QaCNqeB5F5sOh6aIW1RgA0J_SeVl8VktsqeDPp6n_Y66gTHW6-cVVSh9r9_41QbROQOTfqd5oazHl99rahqrJIspox59lW1ATCWdvH5s0SvCgEeigWPsAY0AIL6dInPIT9Rq_dX2N1TVxCr1y-2yD-7ujtCYjuqzSFR4azxt2C2oxdTXpRz3Bbp2E9FC_-26XhurYDMoDguy6XtYjI-xUTofz6rhuRlg1fTKB72tdJyC_vyjzVNBTvKuRzCZopIWDELbGG4Vf_Yp_OA3K4EDeh1lHkzo_y43ghWyLc16aLqcWzTGME9sonFZnsdUxzzgOAQla_JW550An6HOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#TOTAL
— W</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/16131" target="_blank">📅 22:09 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
