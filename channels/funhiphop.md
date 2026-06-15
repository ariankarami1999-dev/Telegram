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
<img src="https://cdn4.telesco.pe/file/Y0GVVFWNdl89FFHo9uweoVjy62afyaji048Co82SA5r_v5K1oceFpwZNnIbWMZfYk93Mrw9elDWFwmNZnaEH2vRxTC41jIkRO15q9SJxNhi1t3tFhHF2tReBajTCTeq256ZIWhACnnAbJWWZMFuuyV4E7sbpazD82ZeJeJ0cJ9UJ9EwgFKpoRLPFaYecIliP343BryodvU0w5GHZDnb8XjAMvTuy3QMrJTWGlm_0Pqr01NcZBIaIWfIPa-TrdOQ90mqLWF4dvK04b0KAXUWgn821YVhSlPRiUNfNJnu_bUURogb22qy0Rp7AH9g-yVLk1hWSKFbC8tJB_vj0_LMcIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 171K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 06:22:01</div>
<hr>

<div class="tg-post" id="msg-77926">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbnmLfOtuw8SIvln70bC_xWQRpM5-EE7sj_wGVEr6GxfwfBzKicP7QhVGi4I2G3BlL1uskcxNnVrSVZK3-b1NTIydnbJewd5nwPt3q0NrPc4ksUDo-Gd49HKXR795rceFpsfVSoQh-xy0oB1NYAC8NvvvalMdL5dBgyZNEsiJQ-SYY-SPdIRVeQcLxjw7d7NjJWZzSgZK1cra15eiBxKL3SW4S8bEltG619XGks-OjmYmieAE17ZRG-S1ojAIBJi_nNQerC2A3GP6NTOp3E_-wewFlOlbb8fXwrb6-7xavU8qKea7ee8Vs3REzUJzPY-47a7CDITDU-E6Uz17vqYaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/funhiphop/77926" target="_blank">📅 03:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77925">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">از اینور هم خبرگزاری سوپر معتبر مهر هم شرایط ۱۴ گانه توافق رو از قول خودش منتشر کرد که اونا برا پوشش دادن زیادی خنده دارن خودتون تصور کنید بخندید.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/funhiphop/77925" target="_blank">📅 02:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77924">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">با باز شدن تنگه پس از امضای معامله در روز جمعه</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/funhiphop/77924" target="_blank">📅 02:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77923">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SN2FwL2gHGYBBxLkqvsRMeXYDqgjlCh7XBh8CRTdPeOihW9VXxSLTARrzthEP75IUph5myecyTIochkaBZRtP9Ew3uASEBS0zM4DAbb6k7_lb_O7vLjNX97uBQJh4m0NjcGSZ1Cz0Xx08yH8iYSolc2Qq8bnqMp-mGbbnJcOZVM_aMB_bupDichWP6fFqQIerARWVLq91dtt4Ulu0MVqfKjrvz_uYTCrXL0tklwWKKiwZLbM2YhjP12Et2gBkeIjiV8IM2Q8IjZkJW_VPo8yPBM1Ldmvc5ddI3wBG1Lhx-WbH66UVHN_7PFo4XQ-lUiaa_f7IJ91TeXrXJwcv7U3pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این معامله بزرگ، صلح و امنیت را به کل منطقه خواهد آورد.
بسیاری از رؤسای جمهور تلاش کرده‌اند با ایران صلح کنند و همه قبل از من شکست خورده‌اند. (اوباما به کص ننت خندید)
رهبران منطقه برای اولین بار رئیس‌جمهوری را یافته‌اند که می‌تواند به آن‌ها در دستیابی به صلح واقعی کمک کند. (هنوزم داره می‌خنده خوب به صداش دقت کن)
با باز شدن تنگه پس از امضای معامله در روز جمعه، به منظور پاک‌سازی مین‌ها، نفت دوباره در هر دو انتها برای منطقه و جهان جریان خواهد یافت!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/funhiphop/77923" target="_blank">📅 02:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77922">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فارس: ترامپ در ازای حمله نکردن ایران به اسرائیل، پیشنهاد خروج کامل اسرائیل از لبنان و رفع فوری محاصره دریایی (به جای رفع تدریجی آن) را به ایران داد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/funhiphop/77922" target="_blank">📅 01:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77921">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ویویویویوی خبرگزاری Ynet به نقل از منابع آگاه:  ترامپ به ایران پیشنهاد لغو فوری محاصره دریایی در ازای عدم حمله به اسرائیل را داده است.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/funhiphop/77921" target="_blank">📅 01:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77920">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1eec5a77.mp4?token=MLZPOjWwY0JZccjf5jh7UPNWua1XWw_MjcuaHrtWxHv2KI_fGFSb75QCZmBcZyvS5bfd6d77r1triniKIN5HhhMiME1wohGaQMoXbuNl1Rg7MJNmK-fD2bBZfELRYJ5Q-2WeljfJmh9OwwgcALH6CzitXyc_NR12TkL0d0kekI42c0dY9egq0XYOGl59KoyVgydhOzKFrjXGS9adZnMAIUSSzLRUGXs7kTo7u037HcPaz9TDu-OfjxWkCC0kAdTIK54Ue_LXySWG1EeHL-GsGXmnTeXrlWpIDrjFSt9XPlMgBIxH2HRfDI9lWd-MlvLG5stjPiafPNpU4dmIE-D8Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1eec5a77.mp4?token=MLZPOjWwY0JZccjf5jh7UPNWua1XWw_MjcuaHrtWxHv2KI_fGFSb75QCZmBcZyvS5bfd6d77r1triniKIN5HhhMiME1wohGaQMoXbuNl1Rg7MJNmK-fD2bBZfELRYJ5Q-2WeljfJmh9OwwgcALH6CzitXyc_NR12TkL0d0kekI42c0dY9egq0XYOGl59KoyVgydhOzKFrjXGS9adZnMAIUSSzLRUGXs7kTo7u037HcPaz9TDu-OfjxWkCC0kAdTIK54Ue_LXySWG1EeHL-GsGXmnTeXrlWpIDrjFSt9XPlMgBIxH2HRfDI9lWd-MlvLG5stjPiafPNpU4dmIE-D8Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من هیچگاه علاقه‌ای به تغییر رژیم در ایران نداشته‌ام.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77920" target="_blank">📅 01:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77919">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">شهباز شریف: به توافق صلح دست یافتیم. جمعه امضاش می‌کنیم. دو طرف اعلام کرده‌اند که عملیات نظامی در تمام جبهه‌ها، از جمله در لبنان، به طور فوری و دائمی متوقف خواهد شد. پس از مذاکرات فشرده، خوشحالیم اعلام کنیم که به توافق صلح بین ایالات متحده آمریکا و جمهوری…</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/funhiphop/77919" target="_blank">📅 01:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77918">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این زیر یکم فوش بدید خودتونو خالی کنید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/funhiphop/77918" target="_blank">📅 00:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77917">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaReMLNFSysJDaNVr1AjPUP7KcG74_dC_pMYmL68SCea_TnUcC_KXNDbPEhvM010SyiqHrvIQ45ChtNHj1_V8xyP7stry2zCqaDgylWxZPlmm4AO8e3CFhmZNBR9sTzjBPX9omvyaUMG8LU3XUOTuq6eYVf9zq68hN91KLoh5wAp0aw1JCT7v-yia66b51z5CpVOQQQlTw8OUWh31sZ9sAcyVy7E4mVkuPtVuj6vjk1wg2WdoothS2S3_BzWbFM67qZjKUeo3nQfk5pDDt2XMqBLykiU6NUOgDy5YLOoWHeR8mRC2j2Wl0dEJSRLJzu7psBXUZ_OEdKReREfttILfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف: متن توافق به دست اومده و ما انتظار داریم تفاهم نامه تا ۲۴ ساعت آینده امضا شه و بعد از اون هم یه مذاکرات در سطح فنی برا هفته‌ی آینده داشته باشیم و ممنون از همه‌ی طرف‌ها که به پاکستان فرصت میانجیگری دادن و به امید صلح پایدار.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/77917" target="_blank">📅 00:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77916">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ژاپن گل مساوی رو زددد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/funhiphop/77916" target="_blank">📅 00:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77915">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ چند ساعت پیش به وال استریت ژورنال:  قصد دارم به زودی بیانیه‌ای صادر کند که تأیید یک توافق با ایران است، اگرچه ایران هنوز تأیید نکرده که با شرایط موافقت خواهد کرد. این توافق به صورت الکترونیکی توسط خودم یا جِی‌دی ونس امضا خواهد شد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/funhiphop/77915" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77914">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">هنوز چیزی امضا نشده کیرم تو چنل هایی که خبر فیک میذارن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/funhiphop/77914" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77913">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گللل هلند زد
فن دایک
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/funhiphop/77913" target="_blank">📅 00:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77912">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ چند ساعت پیش به وال استریت ژورنال:
قصد دارم به زودی بیانیه‌ای صادر کند که تأیید یک توافق با ایران است،
اگرچه ایران هنوز تأیید نکرده که با شرایط موافقت خواهد کرد.
این توافق به صورت الکترونیکی توسط خودم یا جِی‌دی ونس امضا خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/funhiphop/77912" target="_blank">📅 00:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77911">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">توییت جدید وزیر کشور پاکستان:
الله اکبر
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/funhiphop/77911" target="_blank">📅 00:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77910">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQgfKIG65I1-Gcky4oj2Ode12EaFBaj_XIp6_iRc76KVUII_LWFwqseRU0CX2hEWZFMcQGyz00iNoWlJ6tRNU52yMQv4sYY5_MVBvQnK_WG5jzWliMuOf4BAUTVhKj00hf4WZHlGddKEE12klNZDCAiNI8BAMA9o-adaW0rAKVNAkeGOrxwGZVRuRMR-IJ_cjfwfQi4PJD1s-orru_LxRk0sitf-2xp3bRiYsY5nhrZQZ4VUdj-fo6O57uqkbo-PPcZ-IAu5UoyAFERFv9cOeDJj0vBpcd5Li1xFT6mL4R5TBGW5p1NO7ZhP3hiF8e5edIfsRSgtFloI9Rga0UyYrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از یه جا به بعد جدی جدی داره تمام تلاشش رو می‌کنه شت پست تولید کنه:
ویکتوریا کواتس از بنیاد هریتیج کاملاً فوق‌العاده است! ممنون ویکتوریا. ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز به زودی برای کسب‌وکار باز خواهد شد!!!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77910" target="_blank">📅 00:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77909">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0800033b0.mp4?token=CuvgElOHeBvW-E8FJXCYvHdWJTL8LIgwrvA9I7VHIJq6CuuHntIOVzbdOW6KV_Vsh5jvDkbIcuZSwUdiNRsv7NOemeX2pCliOKmgWLlOrz4YzP6ddebVDPJew1x5TcHwxgxnWWoZgjTVXROjX9kgrcPWJdr0NaOrqtIZChiHKjq8uuowBpTDOSkwBblJ1gFmkPpm9JWoVWTGcAOce7OIYPzfqWh7UF_HwBcNJv5dQmb0AGkofWwrIiojEuSZKbrpx9zPoVSXnsYg5tCZ81A2HAY_YQEQxUWpgL-gASXx3gPjovHWiD4H4X0qTQisKYmcAlDioHixEH5CHuPuN2-tYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0800033b0.mp4?token=CuvgElOHeBvW-E8FJXCYvHdWJTL8LIgwrvA9I7VHIJq6CuuHntIOVzbdOW6KV_Vsh5jvDkbIcuZSwUdiNRsv7NOemeX2pCliOKmgWLlOrz4YzP6ddebVDPJew1x5TcHwxgxnWWoZgjTVXROjX9kgrcPWJdr0NaOrqtIZChiHKjq8uuowBpTDOSkwBblJ1gFmkPpm9JWoVWTGcAOce7OIYPzfqWh7UF_HwBcNJv5dQmb0AGkofWwrIiojEuSZKbrpx9zPoVSXnsYg5tCZ81A2HAY_YQEQxUWpgL-gASXx3gPjovHWiD4H4X0qTQisKYmcAlDioHixEH5CHuPuN2-tYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش بسیار تند باقرشاه به بعضی کارشکنی‌های بعضی افراد در مسیر مثبت و سازنده‌ی مذاکرات.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77909" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77908">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">آدم شخصیت و استایل مربی ژاپن رو میبینه عشق میکنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77908" target="_blank">📅 23:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77906">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کی قراره چنلای فوتبالی تلگرام فارسی از گذاشتن عکس ممه های طرفدارا تیما با کپشن "کاش فلان تیم قهرمان شه" یا "من دیگه طرفدار فلان تیمم" دست بکشن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77906" target="_blank">📅 23:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77905">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ویویویویوی و عجب دنیایی شده پسر کانال ۱۲ اسرائیل: یک مقام ایرانی اعلام کرد که دونالد ترامپ به ایران پیشنهاد پول در ازای سکوت درباره حمله به بیروت داده است. ایران آن را رد کرده و گفت ما خیلی زود پاسخ خواهیم داد.  مقامات ایرانی همچنین تأکید کردند که «ما برعکس…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77905" target="_blank">📅 23:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77904">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مگه قرار نبود امروز توافق امضا کنن؟
چیشد پس؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77904" target="_blank">📅 23:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77903">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItFAo8Z11BvoLRRCQ2Zbbg1AYbc6uqlHEV0k1d1MU61Y3XtA6JT1QjYKebesIR_c_X_mMyZ5B0s6G2nMncDuSkB2yAVIZV-9SpEfX5l9svehHVH2_4HmWyt7t25sG6KG8LtbAKImr0-ZuvGm99VhJdGtxYzMxSosZuHsIjkEm5gmSIRpYs-m6SQkQmYNsvi3TApXDdgYxALYrn3tNa_4VoRfxYu0-N42Y8SoamNwzl6pkuKlMTOcVS0hclw78Jpc0BlrAOCN9aR5qfA3jF9dwJa-kd5NM8FT8zzYB1Y1TyHIz_N4ekR9FRU0_LVzbC9J6DpzglgYpJ4lKeE008btlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خارکسه تابلو
😂
@FunHipHop | Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77903" target="_blank">📅 23:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77902">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKAv58k_eZ1eXZKL_CHCORkswvz4-kPt97YRIwgTSxh0RU2eLYJtob5cww5JZZsuoLsGV0jRDxEky1BE4WounRKh4OfOWA9jgUQCBeM92lay0-KxV-zN58N3MnR1lL5d7rqf8-IEwAyjlUHjUDK7p4p0sCNJ-0djqpb29WhM0arNajq1UNuq53j3q2yJiXhEQaZAir49j8PYI10BIJUYTDXEqUnqC2QENFRwigBpX14aRpbMWWRaP6KM0ZiBbpVDySMpYFDiEMbN2_ziZQT1Nnt0IpqaVWy5-q0Qjxz1-wPezG6dMTcbWlcOUKoUjI2gbwqHDj2uTW0gOycarQ6aYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خارکسه تابلو
😂
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/funhiphop/77902" target="_blank">📅 23:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77901">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس در گفتگویی عمیق و تخصصی با شبکه خبر:
هدف اصلی این نظام نابودی رژیم صهیونیستی تا زودتر از 15 سال آینده است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77901" target="_blank">📅 22:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77900">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4D6WeUkOHod2mlQ8zuBhvRUoQDb5FdMPYC_I60bYlTEY-9Ht-iBybiKQ4n6sd-SRwsv7EMqw4PcTLLTqy63CoSIViNvy4uq_z54MNTqUckvzsDOu7xnCw7b2RTcS84ytT9AwfdvVvGVXclPhAcD7q5rqiDfsHqnVknzpxpUi85K29kvxuHqDaQq8ATEmE78yIjStnNNvJbcdLabH4g8Ekrp_M7fKwT559U_tEeFaCK0yLEqITRbUY8i7k0qZrUPVQs8kUZRSG0m3Bc5T7hbpLc9HBAXq-x6pgbh0cFX4j7SKDYUaSM2GNUXprdFP4-FzyshWe_JAuJ5qUcVewJIwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقرشاه عصبانیه:
آنها هرگز نمی‌توانند هیچ بخشی از ارکان مقاومت را تک و تنها گیر بیاورند؛
مجاهدت‌های رزمندگان غیور لبنان و
دیپلماسی مقتدرانه جمهوری اسلامی ایران، حاکمیت و تمامیت ارضی لبنان عزیز را تضمین می‌کند
و بساط دیوانه‌بازی و جنگ‌افروزی رژیم اسرائیل را بر هم خواهد زد،
بچرخ تا بچرخیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77900" target="_blank">📅 22:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77899">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">هفتمی هم زدن  فشار بخور برزیل فن  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77899" target="_blank">📅 22:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77898">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">همچین تیمای تخمیی اومدن جام جهانی بعد ژنرال معتقده که تورنمت سخت تر شده
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77898" target="_blank">📅 22:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77897">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هفتمی هم زدن
فشار بخور برزیل فن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77897" target="_blank">📅 22:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77896">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گللل پنجم آلمان  کاراسائو پاره شد   @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77896" target="_blank">📅 22:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77895">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b73WiSrlAYDOVi6eAFIrKQZOtWh1HYf2llZglN-U2AxeFPG4jbmO6twAAHGI5BcRakalqfq23I3P4x-H1wXj16RhrtNfQNS2z9-shrO1LGkAXUZsG0ZsUMs-s1QspaJX_H_wRxiwSdLVCrjlfFtX5kqQziRsMSeOCQZ6kU4KCEHArDDBlswvtpg37Yg_nZBj-t_KRAk8memRtmRrS_6c8KdL0fsrgzsICU35lzjS5FufFT8IziGmOcKsCNFyYg3nXpOxUs0wcZwWftUXL-tvu1ne1SvY2s7Hi-YQg75WlHHZJl5GLIYIs9UsTiVgkTSwqJY8adgk8b8YvDw41OHc8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقریبا شامپو شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77895" target="_blank">📅 22:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77894">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گللل پنجم آلمان
کاراسائو پاره شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77894" target="_blank">📅 22:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77893">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">باب اسفنجی امروز زودتر فست فودی رو بست، فک کنم یه خبراییه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77893" target="_blank">📅 21:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77892">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">این ترامپ کونکش واقعا ریگان پلاسه</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77892" target="_blank">📅 21:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77891">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ویویویویوی  کانال ۱۲ اسرائیل: اسرائیل ارزیابی می‌کند که ترامپ به زودی امتیازی به ایران خواهد داد تا در ازای آن ایران به حمله امروز اسرائیل به بیروت پاسخ ندهد. جزئیات نامشخص است، اما مذاکرات پشت‌پرده در جریان است.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77891" target="_blank">📅 21:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77890">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گللل چهارم برای آلمان
جمال
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77890" target="_blank">📅 21:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77888">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSJd7cwGrj_6md7yGWclkehkZJ8vKgdBfErIzos9AWvfNCMTfsuNcbBPBoeOKjm64Is6tSBY0C6AiGKLbXnUqawPr0LJxyF-0pyNfLm1HeSq7MgsC6TA0UsnQgQgLQuIIXzsdR7LxvsAxyIOpttmL70mhB3WaXIrJIeXyMM_YBAE92neFyzS49VObbeIjnlYX2kKTLpkz8ZRKN57BtWYKndKWR7iOrl_gsBRIR4fDIv6lmXD62VCmlkYUT3mk_0KVk7NgrFUnnkIC1kObCAbK6Da0kG-TH_nHs-uXQ5oZj5JSyMd2ABEIgsfS8pcAhARrUIx-LrrWVwWR9mz5wcDtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae38bd6df.mp4?token=mLUPD4bXsEFmyNvztCpEqhJYdf6_Z9ZCJWuj_DVXBEuAu1ELrbGmmqRF9J9gQD61iXS4niK_PKqPJlDXYuM_PZSuIkZcPlD6drQZkTreIcrT-qBZ0Uxaeqnxk_zb-tlK5jGDlFTfgjf87JxtNUNlRaH342XdOg2iSBZw0Y9hpPFq1DewVq755GigynDv9N6ESb2jNi3IBs0RM4j_prv4K7d_pI6dFEl1pctqPzNWaNH6bsSI8UpagSNQPvL-AET8rdYwi3UPR_OD3aFY9Os9x2XEpJCHGLdCqL6vUHFGfd-0qP28iue0ks2toL4ruLd1FQQsFIMs3HAl6XN2WYk62A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae38bd6df.mp4?token=mLUPD4bXsEFmyNvztCpEqhJYdf6_Z9ZCJWuj_DVXBEuAu1ELrbGmmqRF9J9gQD61iXS4niK_PKqPJlDXYuM_PZSuIkZcPlD6drQZkTreIcrT-qBZ0Uxaeqnxk_zb-tlK5jGDlFTfgjf87JxtNUNlRaH342XdOg2iSBZw0Y9hpPFq1DewVq755GigynDv9N6ESb2jNi3IBs0RM4j_prv4K7d_pI6dFEl1pctqPzNWaNH6bsSI8UpagSNQPvL-AET8rdYwi3UPR_OD3aFY9Os9x2XEpJCHGLdCqL6vUHFGfd-0qP28iue0ks2toL4ruLd1FQQsFIMs3HAl6XN2WYk62A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کسی که به مرد عنکبوتی یمنی میشناختنش رفته وروی صخره حرکت نمایشی اجرا کرد  موقع اجرای نمایش افتاد ته دره و مرد.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77888" target="_blank">📅 21:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77887">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گل سوم آلمان
هاورتز
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/funhiphop/77887" target="_blank">📅 21:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77886">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گللل دوم آلمان
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77886" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77885">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ویویویویوی
کانال ۱۲ اسرائیل:
اسرائیل ارزیابی می‌کند که ترامپ به زودی امتیازی به ایران خواهد داد تا در ازای آن ایران به حمله امروز اسرائیل به بیروت پاسخ ندهد.
جزئیات نامشخص است، اما مذاکرات پشت‌پرده در جریان است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77885" target="_blank">📅 21:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77884">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آلمان خورد
🤣
🤣
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77884" target="_blank">📅 20:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77883">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فرمانده قرارگاه مرکزی خاتم‌الانبیا:
ایده مقدس فتح قدس و اسرائیل و انتقام خون امام شهید هرگز فراموش نخواهد شد؛ ما منتظر کوچک‌ترین لغزش از دشمن متجاوز هستیم تا درس نهایی و فراموش‌نشدنی را به آن‌ها بدهیم.
ما با قاطعیت اعلام می‌کنیم که توانمندی‌های رزمی، دفاعی، موشکی، دریایی، پهپادی و پدافند هوایی ما قوی‌تر از قبل شده و تحت فرمان فرمانده کل قوا، آیت‌الله سید مجتبی حسینی خامنه‌ای؛ خدا سایه‌اش را مستدام بدارد، ارتقا یافته است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77883" target="_blank">📅 20:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77882">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">آلمان چه تیم خوبی داره احتمال زیاد از گروهی صعود کنن بعد ۱۲ سال
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77882" target="_blank">📅 20:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77881">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پشمااام چه گلی زد آلمان
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77881" target="_blank">📅 20:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77880">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این آخرین نبرده، جلیلی برمیگرده</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77880" target="_blank">📅 20:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77879">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLnKL14XWVlkMJUP7l8cS-FPUR0ZStp0Zpok0g70SEhqDiHllhzROQApGLvbpVijcuo0WExJBD_HEe3xLSpMWN5vdvNDrDbGs_oYXIMzxRZFFn4-4TqpgERZEfkUrcFUfUynLoyelcQTkhu4cNyz-mgwDsbFiLYNpOj3ne79bKJp-mQJvljAS0rFWCvrcfOevCrbFChY_t3XN9f_i42LI-CDTw4_3uuv-TLVe6FSIoRgVi_FiC5kZ5RgBfr1LQqzrSizccmuYY4Qgqayz3hjKzue6iGfsbxz2Kop4OBXiTpSPLjaMO_b1hjHAte-91iq1ks_6ed2sBJ4R_81H4U-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس درمورد میانجیگری ترامپ:
جنایت امروز رژیم صهیونیستی در ضاحیه بیروت بار دیگر ثابت کرد که آمریکا بدون اعتبار ضعیف است، زیرا حتی قادر به کنترل این رژیم غیرقانونی نیست.
پاسخ قوی در راه است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77879" target="_blank">📅 20:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77878">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ت‍       :  امضای توافق امروز به صورت الکترونیکی خواهد بود و پس از یک هفته تفاهم نامه به صورت حضوری در اروپا امضا خواهد شد.   @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77878" target="_blank">📅 19:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77877">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خ در ادامه: قرار بود امروز صبح توافقنامه را امضا کنیم، اما حمله اسرائیل به بیروت آن را به تأخیر انداخت. به نتانیاهو گفتم که هیچ حمله‌ی بیشتری در لبنان انجام ندهد و هشدار دادم که این حملات ممکن است معامله را به خطر بیندازد. اصلا چرا بیبی باید چنین حمله لعنتی‌ای…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77877" target="_blank">📅 19:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77876">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تران در ادامه: با وجود حمله اسرائیل به بیروت و تهدید ایران به تلافی توافق امروز نهایی می‌شود. از ایران خواهم خواست پس از حمله اسرائیل به بیروت، با حملات موشکی پاسخ ندهد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77876" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77874">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ: توافق ظرف دو تا سه ساعت نهایی می‌شود. حزب الله به ناکجا آباد اسرائیل حمله کرده بود و هیچکس آسیب ندید ولی اسرائیل در جواب به بیروت حمله‌ی بزرگی کرد و این مرا به شدت عصبانی کرد. به نتانیاهو زنگ زدم و به او گفتم لعنتی، داری چکار می‌کنی؟  @FuunHipHop |…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77874" target="_blank">📅 19:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77873">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ:
توافق ظرف دو تا سه ساعت نهایی می‌شود.
حزب الله به ناکجا آباد اسرائیل حمله کرده بود و هیچکس آسیب ندید ولی اسرائیل در جواب به بیروت حمله‌ی بزرگی کرد و این مرا به شدت عصبانی کرد.
به نتانیاهو زنگ زدم و به او گفتم لعنتی، داری چکار می‌کنی؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77873" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77872">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رسمی:
توافق نامه بین ایران و آمریکا توسط ترامپ و علی لاریجانی امضا شد!
پایان جنگ ۲۵ ساله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77872" target="_blank">📅 18:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77871">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEeQyR3JujvoZ5H-C6Kxck49_ONhrmXcbJu2c85RFaIaKjxK8aEW4Z123VxPnSrCDISLRRDWPG9i-WUG89bGoAibTPm2_lzM1I_PjATPpJSR8IG6uOAjExNXhvcR3667qJcwcrUVpcFYRytE2AaTy5yNRnDXHei1Q0cjT8AA-pNkwLeAEmruwrUc7p8hyVOBpKaf8yod2i2hIUADs_jJVliz0-EBq8pqVFCM1MrKOOiBym_IvOdR4nAG98IhyVf-FHprA8fBexa_UrPRBswQeJ4_w8bpOdx9vxOCwVlWsyjR1PTSptwwWt_LEzKO4ODiq77RyVLRfdVGu_wkpSq5Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهش گفتم 90 درصد زیبایی دنیا مال توئه
خندید شد 100 درصد.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77871" target="_blank">📅 18:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77869">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dDHa18KWuhb-Cq5HNjBru3gPcvGBCclQB7RuscHkw9R7TNCh1f3dxgaXIiz9CV8InipZAgvQthMpPM6afOlcCIWzPkmRUMsz84LCqMBM4l04drqp4qIs_k2FrnEtiRd0u5GrZd1Ggl-TAl1lkGMH9mEFer0SBYev5UW2EV23Qdw79lIKoBOTFqAq_H6N2Rs3Pi7KjTF4nwOuQtw6r4RisYV9Uzc4NrAWIQP2yYb6RoHoIZH5L5juq-TaAsqUpfg17f64LsD8EI5dy2j6aH0gOfqdmSK7HkLDzt-Z6dSTChNRw9ebh1Cjn_SFfTiSl2ZqMEVXaFCO-55gcT6IXIudVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YSrPLLV0tcH5Cs2K_xQ3zv4TAC85MdoxGN3ZFsx1D6oUNyOvVrlTvYlKPDGAnORnf-LtHRPdY5IV8yvg88ahfJ_vJFpznlVCwyD3oHVOykLrTSzW5uSCeUSRNDwzXBsXVFlL-OE1BAtyNvNl7AbNPC5LeSGtPBAoBo7HdH7m6uQe9u43BRdeym_e4lbSg6vJp0HBX6fd5giHLrNwqS0K9uejZu9EllLW5uyFvCFivmOgXs3ZYyDr0kfZJhBSU0ddEbTpm6f_Ku81QF6U2YM-eDgiVHkr7o3IktEfdAcA7A9NiIgVtK8jThfLwINwcNk4F3pKJglq4Btea44L64HkUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هوادار ترکیه تو بازی صبح امروز با استرالیا :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77869" target="_blank">📅 18:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77868">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/funhiphop/77868" target="_blank">📅 18:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77867">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyKyL1X3mUU48EQnnyxV_IRHpmTmNU4he1TQxEGQp7mSvPOR7Ei8avzx_YRzBBEOO113ddJc6_ETka9lgDx1MNbiosVNIwJFWAaGAJRXWYVvrF6HwIUX3b1G1RIhMKKpDLzdTaUmsP7nfP5mMNs5Jt2o_UkzHRYK7mtMnC684DxHJXf4FiFNODWRa2e4I8H1DFAiolH6onfNEG5r5V3ziLE_65oWL_8NTrlhxJhmmJX61W-iogSYHhkl1-xRbzU6GSeW1hjGlLN4MXz4HMYKQq6AKhwlSTvoY3T2IUM8_rR-iwcEpuRpL_rQGeRmtfAAmPeNy4g022Oh4yJHo21iDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g24
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77867" target="_blank">📅 18:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77866">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3-bmW1WL1_fn8Wvks-oKWOh51abv7PKDzjGIlgOznO46AqecdbX_px91Hw5F00HYLgWbMS5Wb3CM1AYMU9w1QG7UTGPzFNsF88fl7SjaYEYVo7M8XW1FgtXTsj3cejqr8O1YajcPzOuN60AxPZF75u6BN4H1J_sJ6uSVbfI_1kyh9-0SVDeZuOs6y-hFmQFyXSHRBUm0HpWVUR_hm_XYguJWwxtQ-PGzsDnZy-_YhvUJBQ4hLUhwSFxVkqwelj1z8Oxu1-WQQlkn-T2WoMJyDEgoUJICnj5FxbczrzuMSBrjl1R3Eco0wSIrOIL8mwGRllwtKEDrbY2zcmFAfDEVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
حمله امروز صبح به بیروت نباید اتفاق می‌افتاد، به‌ویژه در روز خاصی که ما به توافق صلح با ایران بسیار نزدیک هستیم.
اسرائیل حق دفاع از خود را دارد، اما حمله‌ای که به آن پاسخ داده شد بسیار کوچک و بی‌اهمیت بود، هیچ‌کس آسیب ندید، زخمی نشد یا کشته نشد و نباید این روند مهم را مختل کند.
نباید حملات بیشتری از سوی اسرائیل در هیچ نقطه‌ای از لبنان صورت گیرد، اما همچنین نباید حملات بیشتری از سوی هیچ طرف دیگری، از جمله حزب‌الله، علیه اسرائیل انجام شود.
این می‌تواند آغاز یک صلح طولانی و زیبا باشد — بیایید آن را خراب نکنیم!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/funhiphop/77866" target="_blank">📅 18:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77865">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emldtZlwY7_C83jQAKMx9PksL-nQRlaxRC0Dd1VaIyoOIKi6-Q9ZbHbYeTlj_2l-1tYSOS0ekuVJ0iEXKg5zlLztE_WejwxIapkhgGrbgPRNHFBlEKxN8qN06MJ1p1B4BY3vgwiNoqRbQKmLcXqLjxJfsq3iOOGNFPchDDu8ZMJAist_Usu_IdmH5mMf3TCK2FP9QqlH5FQc8-L_TFgESYo8dNzQcgD3iwfcSPSmRLa1_2fttmhaid0NwcEyF2b1NOZRYtHN5Zgza-PTmvqq31VQJUEz_3NpNv9nBA_xlHYaYFgpc75WirXAGxvinylDNKD_P13Fn6XVYkrAIm9LLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید رضا پیشرو
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/funhiphop/77865" target="_blank">📅 18:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77864">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CV9JucaKRgEfg8XXeePsneWA7u0F6prBIIJ2TR8ade2fhjnjYRtYi2U2qMj4QVTuUW4q9memXbu8oOTVybOg8w_etKC6MNrQpLjKRf4mkphI_wmk2D8bhlFXwpEZOAZw64y5KjyUT6A3OscZPOBWOxSFxZly9uoLDTgcUZmEnKxsrzoeaqDZYFrOONyL_N6ujvPL0V2yJ9RXRIHM-dcjSUCx0b7V5hMeQ_hyAc7SEAj1EYoJlpd1v6RvOXBBl9VzvFrEa0Ov1LoGY6npnkKwaqgrviWJdkKos3mjr-uzQ97_SXt2hzxhtuj6SRLbXa9ksjKQR8vOL_yxYja63kX0HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش ویژه | ارزان و با کیفیت
❤️
🔥
200 گیگ فقط گیگی 2/800 تومان
💵
100 گیگ فقط گیگی 2/990 تومان
💵
50 گیگ فقط گیگی 3/600 تومان
💵
20 گیگ فقط گیگی 4/950 تومان
💵
10 گیگ فقط گیگی 6/000 تومان
💵
بدون ضریب، همراه با لینک ساب
🛡
کیفیت مطلوب، قیمت عالی
🛡
پشتیبانی تا پایان سرویس
🛡
⚡️
جهت خرید از ربات اقدام کنید.
🕶
@Hunter_VpnRobot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77864" target="_blank">📅 18:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77863">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">طبق تحلیل‌های بسیار پیچیده و عمیق بنده، سپاه به زودی چند تا موشک از ایران به سمت اسرائیل لانچ می‌کنه، ولی احتمال می‌دم شدت زد و خورد اونقدرا بالا نباشه که بخواد آسیب جدی به مذاکرات بزنه و آتش‌بس هم همچنان برقرار می‌مونه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77863" target="_blank">📅 17:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77862">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGVDNuNckDqoXPAU9NoggrKaed-umXdf_tNc-f6lmd3xw1jr7phTbnBu2w2p9xFl7XBU_ELkgAnQTVLsTXkdJxL3-L9sEc61q9QkYdPSQ9FPvAQTuffnUVZwGdgNirvMsFKKX1b5UhZsLalyvbecqCQYPYN8NNdrb6xUYRT9UaaP33X9byz8xCqnXvZB0_MpLTvtOO0mP5thCioFOE4Ad23QQJ_EvQjnv-gMUqqnxXr4xLONvop7Rhgnjzwb4TIs_WCUWyCR0uQr_kYQQ-mWg0JV0J2TdfdDMBGejLQaT1TZboPHPgUs4tMsQyJF9NIgITnMmMmy6rRVp-1i3oKq9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توئیت جدید باقر شاه
با وجود این شرایط جدی میخوان توافق امضا کنن؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77862" target="_blank">📅 16:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77861">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تا این لحظه خبری از ترور نعیم قاسم منتشر نشده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77861" target="_blank">📅 16:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77860">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66e866b19a.mp4?token=MhLwt5g890JibbE-ylhGcxIhIS4WQTvtKEfyIFxzIQ8X4mO2aPMZqovHOvbb6y_BxvJoEOfZ8diVLtK4ZjGJmUlTjv1TPwKHk8CCE6rv3KCifxupDO6DNletDqGPjrdtGY7ch_Hc-9mmDeAoAJBVfs4ESEeSoafCC2dKkJSraYbg-XzOBBOoQMUenaz42--forGKBSt7gSOTv5iN9QHmstA01QFWA7tBalHwf0g5XcbxNPGFMTDVCRZaDXaagA5m2eFP8hPH0B-b9EQQEt5lpJbf_liOWUQI57KXYqsiZGdI_fgA_pjVASSrKOzu89iN7HkAot7WmTlk4o0V1Kn9Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66e866b19a.mp4?token=MhLwt5g890JibbE-ylhGcxIhIS4WQTvtKEfyIFxzIQ8X4mO2aPMZqovHOvbb6y_BxvJoEOfZ8diVLtK4ZjGJmUlTjv1TPwKHk8CCE6rv3KCifxupDO6DNletDqGPjrdtGY7ch_Hc-9mmDeAoAJBVfs4ESEeSoafCC2dKkJSraYbg-XzOBBOoQMUenaz42--forGKBSt7gSOTv5iN9QHmstA01QFWA7tBalHwf0g5XcbxNPGFMTDVCRZaDXaagA5m2eFP8hPH0B-b9EQQEt5lpJbf_liOWUQI57KXYqsiZGdI_fgA_pjVASSrKOzu89iN7HkAot7WmTlk4o0V1Kn9Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
پیامبر رفت تو یه جنگی؛ لت و پار شد و برگشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77860" target="_blank">📅 14:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77859">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کانال ۱۲ اسرائیل: هدف در حمله به ضاحیه جنوبی نعیم قاسم بوده است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77859" target="_blank">📅 14:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77858">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اسرائیل دوباره شروع کرد به گاییدن ضاحیه بیروت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77858" target="_blank">📅 14:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77857">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZuAlZJAk8CaLVAGXetCtSEdn8z3IFwLIpGT7_Ylh8cptTtrZwKMcSNxw4KxaBz3yzj1soB1IY814nBy_VvPJRhDp_nF4ElvXAqG5lplyair4flKwHH1J8DcJyP_xKo5DTCwPWbJzcKHh6cwzSWVP7Mol48v5CzAsXBpLQm0Zt9iFL-B2-DALPwsFfDAhbRGIrxbk4eKZGgdzBks6A7XyHPzYxynRzXbrqgb-P4TBB5dLDESbifhcjGyque40u46gRbSV7kbv72Yhy5rK3jWDtm5cghIwg6YYfiXOEaByRnmM1evFP2HBZSI1O0qptu3d2FKAz-WFAQCvAP02ZGzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77857" target="_blank">📅 14:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77856">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">امتحانات نهایی و کنکور ارشد بخاطر مراسم تشییع جنازه علی خامنه ای یک هفته عقب افتاد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77856" target="_blank">📅 13:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77855">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">امروز ساعت چند قراره توافقو امضا بزنن؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77855" target="_blank">📅 13:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77854">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دادگاه عالی امریکا ممنوعیت ورود پرچم شیر و‌ خورشید رو که از سوی فیفا به درخواست جمهوری اسلامی اعلام شده بود رو لغو کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77854" target="_blank">📅 13:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77853">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKzBA9imd93w72jLtXd0Rjc5ZRdtMy0G9vRGPXqitv97j0y3-LYw-Ys8wp9XC25WaNr2g0HQpOyEdBnT3OtJJfn-1eP9Fa3-VkVzC90fDvhvv9jCNhHZ4HpBufZSxRaBgp3Ng34ohYSf_8KnfeqZ0pOCvm138bUHScfw3G1Kreuqdr_Q0UGZlbwL8cA5UzFBQ4Mr-QR45g9K4P_gYqfatk2Dx17glUcncuSq9rM3NF-2qGGihfHCa2pzVyESVsaFVEsa6dTfHxRHupbNFNf0y6hiTWcW5KoFvKJyFmzGnXiLHR1FXxjQW4Ghq9iIrpPofTuiJloUxLcNWF8THcsBLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میرباقری(رهبر پایداریچی ها) دستی حزبشو کشید.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77853" target="_blank">📅 12:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77851">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aVT112HP9GIG4n2L0oHDZDYy8v2OyjjePjLT_8gcixogjTn_olMhxQ7V1NOTiHZDpiHzrRY7eMF_GPJvXckU4Bp6sJxOiVslVa-Wy7vZiLcsjKaaxxjcdv8vmNV4pbK4QrjziaEmpAd5AaPoTKplVxls_7FDjBSLda1IoK-hG2pkcTn4B4k8t3S0MU20ikHTNSB2mwhy8D9DlVtam1LPHcROzhk6WMZ_hUbZRK2wPhuWBPBtJmqFUt3Q0qPY9poLRs0mm9Eesa2NhOqqOFFCEpjcL3GzGRCzMqbUr9DGp9DZUnX2ew81Fj5ObTZRw4lXRswbthT41cspRssPvWuxEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hjpPtaZfGFynkksf7R-iWw4jL7V75zaqBCgoCBviL_raL4Mm_G0IVI23hSgO-DvKQzINvaN1zhRKf76JFfgjKEl5L-b1kN6sYU9tb4WnUa_z6-g5E1crOEbZgG-a0rlr0YZ8Ml4v5N_AcJbIMlLMSV1gc6Tk9jt5MX6v9NVGzGtNNnOmMMRzI2iSAsK1TdiE1AXUAOdBMlV-NpVGg7TeGvhBcW2m8uuUIA8Eu_czmkyfVwGoUXlbnWU8DN8QDkml2qPQmhJiuKZCPufHdn1XJ0zHtE-9gCJBI-jC42r6LglRfRm3Gj-qlCnWsfBkIjCXwAijQvVW0ASLG7boiK2X3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز تولد این دو نفره
🥰
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77851" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77850">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DV3CDXNiidoX_yLEiofpBiuIlCUBE6w96O-bn0TfLL-mkT1GNI0LZhFCZOvOFWLif-Z0y5H5c_YX7wKzkqIN-dbCQRBAjYTk9_Kh4Ekk4ASqHZOi_D7LJnsXZTvITfh7M7oCGqBNcDQT7KnnRgZXjuMwvZdoJu9GoBiO5ngKJQfAhjPmIxtqO0ofWbxbsX-BHA1-H-vtc5quGuWYQp0dOAvMhYFbbJzMq_NWKTxnI7oZRieK-Y1gLLC_Zy3C969gcxxvgAgivqBetqnmwQ360ezg1caLnnEthtp-aP19aYHwyQLe-A35tra5trz6l6MXMu-AO6EArOAsNQAQBwwu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام‌جهانی امسال چقد عجیبه.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77850" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77849">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77849" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77849" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77848">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juNOOS9oLs7H_JmbJGLwByL3u_xQ2rsmRfj-x8bpjs1tv6WJ1Ycd1_F81u55JWxFAgliSopIzpuxSvakoWN6C8W4UtBxiG3miOArHwfEc_dZeqFG76kdlIj7A9ahQEPdMMy_vBk8adPfDxm4oT7iFhjw28ft4AlmD46Jgq8OwQgow7evVTWbdTqaU4IWNQyfQj4hQ4Gls_ODRdKnRLo7mDPmDD3wBq-qS2bYaht2U2W4KB9kuYV9fHWXW2JqVm5B0jeBpFMV449KK0WpxAo38nYMYKjxofIwUGHNq-KEBvYIKbLW61FAl7uVo_oqMk318QJGCVAhej8LrE-qdS36bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r24
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77848" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77846">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De5-UaXH75xDRwrQRH0micc3A1QaXmAumJdD5CbXT_kLDVCD67bYbdhgnUuaMri29TvM6AoI5eC8A4p4TiHP7F_KZwI05qA11MPYq1oFOXbEChPRQz5grC1pXkFCZBNT9l0DSAaEzTL6MtsuFkLCItpvA7IRAQWMIhu--5Lp3QOzMBN-XEuCFMbg2G5tKJR-g1xOsqAmDe1E1OR2oeB9ycpGF86bkjI_5fIadHrWX4Bz38cOYH-FW1nmWl1mfB1YbWeWHOcY0KpO_FHhuG1s_kqelJoUTE0m_46ILnS_tdJM9T1WSz01OaFEUuIohk0buK3pGMUfVFh8CS5X95CUyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسمو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77846" target="_blank">📅 08:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77834">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTEuxdgh1Z2P0sXlk9QUJcDt5gniWYHQqFusSr-mzygGFYTxQyfGMbsClu3LJwUBFDyarTWy27GOW8R2fffofIKgfb0ZTkf_InZKvJp3CelbkJ6JtaZL33r_sTJN3wl2jL1dUeNoGb-ZVRjGVCChAEt7usGPScM5TXGNafClJCu8pB6NRXL6h1uyCECcEkkI2kBodyzLap3O7mkq-M5pUEn90RJ2bRMthnEqM9oQJrMyBGSiosLXKROsGjXsDmX1BQVHtf9fX8IDTpm6esb2SyiLYo1q5PG39ZTijrsg-e-371Zc_kIrMXyazUaw05Tub_t7YFuWPoPmJfKLOQHbyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خارکصده هم باز کسشر پست کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/77834" target="_blank">📅 02:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77826">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گل گل گل</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/77826" target="_blank">📅 02:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77824">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اشرف حکیمی چرا فاز روبرتو کارلوس گرفته</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77824" target="_blank">📅 02:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77823">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آلیسون یلحظه شد سیدحسین حسینی
این چه خروج کسشری بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/77823" target="_blank">📅 01:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77822">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مراکش زددددد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/77822" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77821">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/77821" target="_blank">📅 01:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77818">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnut4GSJZKiCViOlBxhZf_xDXXDvgk1chRRgp9A41-W1n2s_zvUPxhVTkQGugW6I7pK5ZayYoymmoaUDQchu4ASvEPVUNFzEQPF1VQZxfsaWfJLD0RDCcqmQmcD-nHzbfIMtjy22EHa3ptquSTCzYYlTa6J7SSk3qkiyln_SksV4TQWDigDyx9wbaxQZhhb6SiSmYiXNxV08ytBGs5lDPmLULhj0U0K46P_WKXGnIXVp9FIOe-yqFkuUN2MBO7COzRaLBOaWok9id05nnzLskbOevvdPRsfYEaHdHma7zqLw46HBvzMdvVJt51ceuQvSiVnI4CwCksajYmyJ0gx5nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب برزیل واس بازی امشب
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/77818" target="_blank">📅 01:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77809">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">قطر دقیقه نود و پنج گل مساوی رو زد به سوییس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/77809" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77808">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به ynet:
هدف این توافق این است که زمان و فرصت برای تمام رویدادهای مهمی که اکنون در آمریکا در حال وقوع است، خریداری شود.
این توافق واقعاً چیزی نیست که دوام بیاورد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/77808" target="_blank">📅 00:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77807">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfdQ-RvAnSjRY_FC3jpBxzYmqfnJLZCZK0Y9y1bmFvk8PaLWqeiIZMxyU9EGmE2KOo_xChTXDAimiVfrjtKMM3Sqcx2PDQuZUiAddskIWyDY42d_C_hu0gVwNmlwOBzPXWckF0p5YN-YfDQ3ihJvL5MSwd2XRL0kZa4Bgy2ZUB-3q8uXmoPeKCfMgmz466ykxz-TRFn5TXMhDkshV8mSLhKutXixa0mIWjp6bQ7KHl4Jvo4ipoGbsISwatXETRM6Yyw3Sk16rP6d0c2IyBV-3Flk0IdikroG1dip9qgc7KVHJOFdNiX0Buh_fAB3dwHu22nRyVUVIC9DK-OklN8qGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه ی جدید رهبری در رابطه با مقابله با معترضین اغتشاشگر که دوباره ری پوست شد.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/77807" target="_blank">📅 00:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77805">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">من خودم خرداد ماه کف خیابون بودم</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77805" target="_blank">📅 00:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77803">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRfB8YYhDwKO4WSeVo01JbV7HAxWDjM1or-WiFXjOKBV5xom0JD1pg7_P739LttGpijHWQoDtOP1sAUDVPFJtfGqH6ncvOtYAbrF2HUiyD0V0npJZ69BAZZmfdROhJkGhvPCd3QU1zyBgyjzzW2-aIkQX2s9IG0lqe0dPMAPp1as3vzR0DXhtncBPXx1GfOJoRWnQBhEVIx2p_ClYoMPMDD0-pLw6IIYsFgHUlcmnOJrFCYHCdPfM7qJ_WwuZcXGwybLC5BnRCfeud9BcLH5TSBSd7Dv9rKwkzi45c6GrszxszW6BOFvLxLvvIdN9bpxQNueCJO2fTPahew4JDDqSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنده یاد تا آخرین نفس پای رهبرش ایستاد
💔
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/77803" target="_blank">📅 23:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77802">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">#سوینا_رضایی جوان معترض ۲۱ ساله در خیابان ستاری تهران  کشته شده به دست نیرو های زحمت کش سپاه پاسداران صدای او باشیم</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77802" target="_blank">📅 23:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77801">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dO4xd3HeoKKhhvTAOf3FogIlGu26oph83wgMewrJ5g5pNJH_N8eYckyH7Qckb37xiwPwFiDw7seLRd7hBU1R-bTVTpzwUDsb4X9s0XPO905UcP6zhrxx8JjF4R27bmzgdd6uF3JHMMe9ZkSm86S4Ns48ih6CeshTmg6NWiuwh3w5VaJ6q-Rcu_UohW7nYHhZYZJYXxWfexAhO58xj7e_VThuplmRX_aGX4X2AvEb_qMhj40KTpCWesPKvUZ7qgGWDervLdEwksU2ys7awCWGi-MhX-BvT3Cg3YCjPNRJuuRxlvYBwmwVXQwBXGBm9opAdF41YVaV7PR0UfHEpFY61Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#سوینا_رضایی
جوان معترض ۲۱ ساله در خیابان ستاری تهران
کشته شده به دست نیرو های زحمت کش سپاه پاسداران
صدای او باشیم</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/77801" target="_blank">📅 23:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77799">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آقا کجا باید عضو نیروی سرکوب بشم</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/77799" target="_blank">📅 23:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77798">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">از نیروی زحمت کش سپاه و بسیج و پایگاه های سرکوب خواستار شلیک مستقیم هستیم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/77798" target="_blank">📅 23:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77797">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">منم به این اقتصاد اعتراض دارم
ولی به این نوع اغتشاش هم انتقاد دارم</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/77797" target="_blank">📅 23:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77796">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حجت‌السلام نبویان:
طبق متن توافق، ما مستعمره آمریکا میشیم. آقای عراقچی هرچی آمریکا گفته رو گفته چشم، رد نکرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/77796" target="_blank">📅 23:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77795">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این آخرین نبرده، جلیلی برمیگرده</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/77795" target="_blank">📅 23:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77794">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هنوز توافق امضا نشده اوضاع اینطوریه، امضا بشه چی میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/77794" target="_blank">📅 23:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77792">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الاناس عوامل موساد به مردم شلیک کنن</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/77792" target="_blank">📅 23:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77790">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نیروی انتظامی، حمایت حمایت</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/77790" target="_blank">📅 23:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77789">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نیرو های سرکوب وارد خیابونا شدن و اونایی که علیه مذاکرات و قالیباف شعار میدونو سرکوب میکنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/77789" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77788">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اغتژاژگر را باید بر سر جای خود نژاند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/77788" target="_blank">📅 23:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77787">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc96beb56.mp4?token=bkIqtL7LcR_MhQWGsSnsXPGB6v3AlqJnANc1lNzTJ-Bft30J-VMnUHBi4jBl_pjSq-YZHTF0UpP3nWNHvXonBHQNEfimitgc-AxyGSC7BIL9d6NS8vVCfQo2pZtX4iMQgjB067ebb1UTaNMrwRMXF8L2m9cjv-rAnmFnAOVKM9uHMq6G_KEb7wTHv8-C0Ky8MKtnUwSgOUuhKIOjxYtziB7WDUpYlHYHkgZAvNN4kGyXPqnJQMziVm_j86Kq4kgr20WujNZrrnUhRkM4S1GQtZUuosY3BAZ3G3VpNEnytceV7ETM4DPU18-QGjQGbhZC14AqQMw-mvEAaD9H_1GGKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc96beb56.mp4?token=bkIqtL7LcR_MhQWGsSnsXPGB6v3AlqJnANc1lNzTJ-Bft30J-VMnUHBi4jBl_pjSq-YZHTF0UpP3nWNHvXonBHQNEfimitgc-AxyGSC7BIL9d6NS8vVCfQo2pZtX4iMQgjB067ebb1UTaNMrwRMXF8L2m9cjv-rAnmFnAOVKM9uHMq6G_KEb7wTHv8-C0Ky8MKtnUwSgOUuhKIOjxYtziB7WDUpYlHYHkgZAvNN4kGyXPqnJQMziVm_j86Kq4kgr20WujNZrrnUhRkM4S1GQtZUuosY3BAZ3G3VpNEnytceV7ETM4DPU18-QGjQGbhZC14AqQMw-mvEAaD9H_1GGKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باقر شاه در اسفند ۱۴۰۳:
صحبت‌های ترامپ از مذاکره با ایران فریب است و هدف او که آن را امضا کرده خلع سلاح و تسلیم ایران است.
مذاکره با ترامپ به رفع تحریم نخواهد انجامید و نتیجه‌ای جز تحقیر ملت ایران ندارد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/77787" target="_blank">📅 22:25 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
