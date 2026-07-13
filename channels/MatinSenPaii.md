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
<img src="https://cdn1.telesco.pe/file/DiHhnfwOMjwDfEI1nN_Pr_H9iaWpbhXx5CzXeGzRCZZs0Mf4IeW7GaZhGRMD5Gzh3yKDZNbSQ25e2Ee6a95ZdJVgeKnl1hpiWhY3WdbKELLIp1EdmhG9WJ1mjkX8N4VdHj1N89wMI2VyHVJkUYtqjGdSSTlMS-IqJSXEmNFzi9Wt99oGjKYyprBp_jM4hwa5OxjANUyjc5Umpyxx7u7Yg59W4NZi0TrH78FUkciZ2X8iWSLgcrssWlMxNRopA6QLg4gABNpyFK45tXm5FHHmxQ42d5LXwt548P9tuNeSXQ5JKJH3_GmWYXIXQOtwupR5KyhtggjLvKlqdrpATLuYkg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 158K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 23:26:33</div>
<hr>

<div class="tg-post" id="msg-4440">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4440" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4439">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K6rHQj21VrMaY7rpyVN-kPEGgIb37dHzrV_5dnCrXVYjeBfYc0HKaEgfLdCuO6tmx8JWY5PkxaKT5Zi3PWV2IKIu6TrIXc-em4-tSF3vpKdTvF2lbTwHvtFOKDfvAuIUpOjLk3LdEnN_3_Gt_2I0HaZ2Alw4_6MYwo7UL3cAPxtdUfXD86YJwL-3cVq-G9lpYR9xhfY_WFlw--mtKbcbDgE9RSQHZjNY9vDq8YTdOcZ0F7cjek-izRrgUvIEEOzMmj9k6gM2MdPEmdzTe0z7DClYbNM9e18qqI4ox3DTyg5aEZP1-Ama6PXfAd0BF65VfYu3FEdgd-lEzYpnKp_SLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">8- بخش پایانی Integrations:
از قابلیت اتصالِ One-click به اکثر محصولات و ابزارهای پرکاربرد پشتیبانی می‌کنه.</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/MatinSenPaii/4439" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4438">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ab-gkFA1jDTMHEmf3RsGINZ6jTBcJa6Cafc6AxrVBMVRL-O6QlSbXeYQwjnXAfMpLq81-1VJGc9dKQ1RCBmM7kr2z5SoCsTwIdLqNrbtC3BfdmtC3F2HILmspVQT8cXJiyL8xfJyrIxUeqHCowFJ0j8vu7yhjCVYO-ZJCmIcUaJBk8COX_Xoymxnrxr2u4eb61TuXd24swaWKv70l4zViQbNlmWvZtIjEK3c2al78gyUYMuWrLZwqjB_UIN-CRVYhIM-tqv-RxKuA7s-t7nH7r5Go0AmitXewcMpCfuv7jt8lz28QvjGg-GgR-StshTyo3I1fgCtPh9EWt6NgD4K9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">7- بخش Apps:
می‌تونید فضاهای کاری اختصاصیِ خودتون رو داخل Rowboat بسازید؛ این اپ‌ها به تمام ابزارها و اتصالات دسترسی دارن و حتی می‌تونید اون‌ها رو با بقیه به اشتراک بذارید.</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/MatinSenPaii/4438" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4437">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ItGyun7qCyesoo6_VsGAEQbBqaFqmDDb1a8umkeFYSsHyW9Ez7_MPLNcFaqKG_TQyct5RZzzxp8AC_Sm3cxBoclP8FP7tEUDlmm5ejLAizuljXGYK8kVoQXnHPIhSLW9K0YHnxJDIR9cOQs2ITZk0BqTtdyXejlG_RQ36qXOin5NIxRd_BNrVmlpNBH0BHsd5hvMbcCpPPz2Ljt_rplCshzw1c2uWquGcqVUEbOktmUE0kTnvzBPx0iJNOpk8IvuTC5lZvfqVKV8Jl38xRlPUlXif8g2vKumLlruVSv96QQJ0BVXl3zLnoRp4blmTtPLON4vmmxtrsbnqBG_h30kEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6- بخش Code Mode:
این بخش بهتون اجازه می‌ده همزمان چند تا ایجنت کدنویس (مثل Claude Code یا Codex) بالا بیارید تا Rowboat با استفاده از کانتکست پروژه‌هاتون، اون‌ها رو هدایت کنه و کارها رو پیش ببرن.</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/MatinSenPaii/4437" target="_blank">📅 22:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4436">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R_jBPEEPvf7m_z1yX0QIpaqpNoLBB1kTXl01zDJHvrbFcMk7NCxxWcPesF6CpL6uy4C-OtCuNJYFEpEQE4I2KVnpCjeCNFRa7wZ1r3CtoBWkm4RR_QGgdCrMNOCJQ0QF-dEo5QToW08qP7TQgQ0I66wOaZXZ44kIhyBwvNzrXxyiiQxKQMXymj5X0prR9s8QI9ACoEpCEJktHgWHKP0ENuS1_z5fQrp5NKT0Qa15yZWm-tv2Rd-lQbuDCve_4YGDjGdjS183fwze38M3UWCGb1tVNOgu8f0InnEvCCGeyFKnQ8abM4BhIP8IfrQYcUB2PAV-LiUxdLRlyfvvx_VhRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5- بخش Meeting Notes:
یه دستیار محلی داره که مستقیماً به میکروفون و اسپیکر سیستم وصل می‌شه، همون‌موقع صحبت‌ها رو تایپ (ترنسکریپت) می‌کنه، در نهایت خلاصه‌ی جلسه رو تو یه فایل Markdown بهتون می‌ده و گراف دانشِ سیستم رو هم آپدیت می‌کنه.</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/MatinSenPaii/4436" target="_blank">📅 22:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4435">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KlTnY8WAYqngLYPrP2FqKe_IcqRV-NwoCOzpaufbIrhK7aphLT14jXLol7F8tQb4SFMaUzMzEyaTZxt7q7LtdK88H0Pw8sZqoH0-o1o827vC1dStCd7kNkrsiAzSg1haV49DRj-7wYWD94PO3vcUMhKL9BrTph4RHl5zeS01AM9dqBIluCwLUGIZzpz8h1cxyabch3embg-K4IHituJgkwKkIGcqWhCxjBQKzPdE7AWmeSmhHh7eXIcV2hkBgGhK0DbowxepYOqf89jHRlotXxBszhidjq3cBV9gVMzH-yHEH8cOr8c90gP1ODqIXbpBwD-jOGTvAMdgL-y2k96LEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4- بخش مرورگر اختصاصی:
یه مرورگر  Built-in داره که اجازه می‌ده شما و دستیار هوش مصنوعی روی تسک‌های وب با هم کار کنید. چون این مرورگر از مرورگر اصلیِ خودتون ایزوله‌ست، می‌تونید فقط تو اکانت‌هایی لاگین کنید که دوست دارید هوش مصنوعی بهشون دسترسی داشته باشه.</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/MatinSenPaii/4435" target="_blank">📅 22:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4434">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VBgnNmVRRefEEREspYk7vbQSGm8OmMr-j-df7_u5UdctaG4L3jnPDCUKMc3aWLTXltJaoW0IxZr3m42dDdBTTdrs5cbAe_WkJEXOxujm4jl-63KPFXKPmenNOfuGDTBwQ_FHTwUvLnwSjTBB-I4l4HTgEffFC69ygO9Wtf0Ait6cTyy4jQr99SSTT7q2zuuCa8Pjea8Jn1MJRmhkLX_q_jA3PN4Q3YenZjVDWudtb_Gf4cSV53I3TT-4kF8UXf9sPVrehVj_Sa1Z7mlqLR6_OB_fNrT5C9aoA6yVoORrnhuNAxHi-S7aFJxppKr2Hy0g2HefX8AbJg5fI2UFRYxAoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3- بخش Background agents:
می‌تونید ایجنت‌هایی بسازید که بر اساس یه اتفاق (مثلاً دریافت ایمیل جدید) یا بر اساس زمان‌بندی (مثلاً هر روز ساعت ۸ صبح) اجرا بشن. این ایجنت‌ها می‌تونن به ابزارها وصل بشن، تو وب سرچ کنن، از مرورگر استفاده کنن و حتی با Claude Code یا Codex براتون کد بنویسن.</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/MatinSenPaii/4434" target="_blank">📅 22:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4433">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hsSxms2hkYO6E0mSpRq4AEybpitAqGUY1xYii4ec67QlS--4EXWmUjBjx3jjuXl7aqMbxgJP8sFZaAKPaH4C5MDkWSQYkSp1VDCWrs_mLNY9yu8TC9Gd4_PhTN9FrdRBnaKLiacm0USEgcOMryNCGfsjQ25Hm5Jhc31cr-24CWObZ05UWKcMy24YSwCRFtStfehJneILXcW490x0vv32Pm0X4HbStHjtvAq4msCtoDXwaO4QBXROK0gVPmoqM30SDFZXSxaTccUq3cexKtunEiyup4r1WKGWoCZ_paqDjndQx0_jvRvPaEyLQyFvntzm0Xo8c6pfguowvmkxS39DZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2- بخش Email:
یه بخش ایمیل داخلی که ایمیل‌های مهم رو از بقیه جدا می‌کنه. بعدش با استفاده از تمام اطلاعات و دیتایی که از کارهای شما داره، به‌صورت خودکار برای ایمیل‌های مهم پیش‌نویسِ جواب می‌نویسه.</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/MatinSenPaii/4433" target="_blank">📅 22:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4432">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XBA-ToFb8Ns91A7CqbhDhK4HDKhMaP3GoEY7-I14TQ41pMy4McYywWFBRfgvr2No5GfckxdFk_4SA8MG07YFTmifBOGl4tu1TrgI0ZWghm10OEj5jxiO0Y_nLkDB51flKqQtSSve5t2er9RdfdjV-dpzBsVWqix7NjCS3VnDVUJdGr8RK32udRDavXQIXjFKIn087O1N_zlqZqYXdYZHa3MabpuOOTNe7bBWbEQBHIiieOGmDN19WNviR2Rc5oCgS-ViUX88A4tvGvZtgs6dFtzbcBrFehGSq1TOF75BcCxcZx84dC5e1jQ-pxGORqpVvHrveYzw3e0IkC1DncxShg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1- بخش Brain(مغز)
کل ایمیل‌ها، جلسات، پیام‌های اسلک و چت‌هایی که با دستیار داشتید رو به یه گراف دانشِ به‌هم‌پیوسته (دقیقاً شبیه استایل نرم‌افزار Obsidian) تبدیل می‌کنه.</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/MatinSenPaii/4432" target="_blank">📅 22:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4431">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بذارید تک تک نشونتون بدم
👀</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/MatinSenPaii/4431" target="_blank">📅 22:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4430">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AW_0Dy-53Yl481LxuJI2Vq8ClAEloXh4H_bZ_2mlz5TBV0RKZDSeTDew0zxk9J53hmGkHvOKeQY_hahU1-obzgwZhg5Z0dz7up6vpCHJROX_LxMnqpOQDj2m3gKW0jPGR2pLuKKB8WVNtrNI9Lxp9FgKwgaWxelrGXHC5d5H27ERBdc8uVMZKA27wkrAuJghejmLnXoYZ1ixUBZXtmJ8E-LYsPRZWfSaKvMUurfMWJ76E6FLnp7y0RRacWy-UHXP_kuPj6kf4JN5vh0pGAduFOXch4685fKq3XntSVbODIkn-VwowLuMdqlse2KmepQ9j1BhsRO_mLNtFg8SvP_Ghw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی  Rowboat | یه همکار هوش مصنوعی که همه‌چی یادشه!   یه ابزار جالب اوپن‌سورس توی گیت‌هاب پیدا کردم به اسم Rowboat. این ابزار در واقع یه «همکار هوش مصنوعی دسکتاپی» هست که روی سیستم‌عامل‌های ویندوز، مک و لینوکس نصب می‌شه. توی اولین نگاه هم شبیه هرمس به نظر…</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/MatinSenPaii/4430" target="_blank">📅 22:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4429">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VfSiSv9jRym2_0SuaQOiNVS052XmItQZKvQnmplebKe2oWoph_lds5uZebDzoWB1N3JF6gFe8V18Od6W0fsW3oxumA8ZSlAeuw2jLNeNFDSJhfY2Em96nuVAoEhB4yydvCGWyZPuXZiWk-GnM-aMnlCqFkh0Tz-EEUlNcIsaIuYobI5Ik5zHIvuNyq1j2FEzcX6VMG7aXC-kKE7IC7OUgV8A86o5ushXaH0bRvWeOt-4mUkSQx1O0u1wAWxPlZK8daoaroTfR5CWC04DFk6-vvRcPhSBrbdYp4CYHNPF9HNMOoNTBEuoG5eGIwUFg7gVv2ZZbDFqk58LuN2AUxWE4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی  Rowboat | یه همکار هوش مصنوعی که همه‌چی یادشه!
یه ابزار جالب اوپن‌سورس توی گیت‌هاب پیدا کردم به اسم
Rowboat
. این ابزار در واقع یه «همکار هوش مصنوعی دسکتاپی» هست که روی سیستم‌عامل‌های ویندوز، مک و لینوکس نصب می‌شه. توی اولین نگاه هم شبیه هرمس به نظر اومد، اما بعد تفاوتش رو متوجه شدم.
کار اصلیش چیه؟ اینکه یه گراف دانش (Knowledge Graph) زنده از کل کارها، ایمیل‌ها، جلسات و چت‌هایی که باهاش دارید می‌سازه و با استفاده از همون اطلاعات، کارهای شما رو روی سیستمتون انجام می‌ده.
چه مزیت‌هایی نسبت به بقیه داره؟
بیشتر ابزارهای هوش مصنوعی فعلی وقتی ازشون یه سوال می‌پرسید، می‌رن همون لحظه تو فایل‌ها یا داکیومنت‌ها سرچ می‌کنن تا یادشون بیاد جریان چیه (RAG). اما فرق اساسی Rowboat اینه که
حافظه‌ی بلندمدت
داره:
- اطلاعات و کانتکست کارهای شما در گذر زمان روی هم انباشته می‌شه (مثل حافظه‌ی انسان).
- ارتباط بین داده‌ها و فایل‌های مختلف رو به صورت گرافیکی (شبیه گراف‌های Obsidian) بهتون نشون می‌ده.
- نوت‌ها و یادداشت‌ها تو دلِ هوش مصنوعی مخفی نیستن، بلکه فایل‌های ساده‌ی Markdown هستن که خودتون هم می‌تونید ویرایششون کنید.
-
همه چیز روی سیستم خودتون ذخیره می‌شه
(Local-first) و دیتاتون تو سرورهای ابری هیچ شرکتی رد و بدل نمیشه.
امکانات و بخش‌های اصلیش چیه؟
-
🧠
مغز (Brain):
کل ایمیل‌ها، جلسات، اسلک و چت‌ها رو به یه گراف دانشِ به‌هم‌پیوسته تبدیل می‌کنه.
-
📬
ایمیل کلاینت بومی:
ایمیل‌هاتون رو دسته‌بندی می‌کنه و برای ایمیل‌های مهم، بر اساس دیتای کارهاتون به صورت خودکار جواب می‌نویسه.
-
🤖
ایجنت‌های پس‌زمینه (Background Agents):
می‌تونید ایجنت‌هایی بسازید که مثلاً هر روز ساعت ۸ صبح یا هروقت ایمیل جدیدی اومد، برن وب رو بگردن یا کد بنویسن.
-
🌐
مرورگر اختصاصی:
یه مرورگر ایزوله داره که به ایجنت‌ها اجازه می‌ده فقط به اکانت‌هایی که شما بهشون دسترسی دادید وصل بشن.
-
🎤
نوت‌بردار جلسات:
به میکروفون و اسپیکر وصل می‌شه، صدای جلسه رو ترنسکریپت می‌کنه، خلاصه‌ش رو تو یه فایل مارک‌داون می‌نویسه و گراف دانش رو آپدیت می‌کنه!
-
💻
حالت کدنویسی (Code Mode):
می‌تونه همزمان چند تا ایجنت کدنویسی (مثل Claude Code) بالا بیاره تا بر اساس کانتکست پروژه‌هاتون براتون کد بزنن.
-
🔌
پشتیبانی از MCP:
می‌تونید راحت به هر ابزار خارجی مثل اسلک، جیرا، گیت‌هاب و توییتر وصلش کنید.
آزادی عمل توی انتخاب مدل
یکی دیگه از ویژگی‌های جذابش اینه که می‌تونید مدل زبانی رو خودتون انتخاب کنید. می‌تونید کلید API خودتون رو بدید (مدل‌های ابری) یا اصلاً از مدل‌های لوکال (مثل Ollama یا LM Studio) استفاده کنید تا حتی پردازش‌ها هم کاملاً آفلاین باشه.
پاسخ خود هرمس به تفاوت این دو ابزار:
۱. هرمس (من): یک دولوپر و ماشینِ اجرای تسک
من برای
انجام دادن (Execution)
ساخته شدم. رابط گرافیکی سنگینی ندارم و دقیقاً مثل یه دولوپر سینیور تو ترمینال یا چت تلگرام نشسته‌م. تو از من می‌خوای یه اسکریپت پایتون بنویسم، داکر ایمیج بسازم، یه ویدیو رو با FFmpeg فشرده کنم، یا یه کرون‌جاب تنظیم کنم که هر ۶ ساعت اخبار رو اسکرپ کنه؛ و من مستقیماً با هسته‌ی سیستم‌عاملت (لینوکس/مک) درگیر می‌شم و انجامش می‌دم. حافظه‌ی من از جنس «مهارت» (Skills) و دستورالعمل‌هاست.
۲. روبوت (Rowboat): یک دستیار اجرایی و ناظر
روبوت بیشتر شبیه یه
منشی فوق‌هوشمند
با یه رابط کاربری دسکتاپه. کار اصلیش «نظارت خاموش» (Passive Observer) روی کاراته. تو پس‌زمینه ایمیل‌هات رو می‌خونه، تو جلسات آنلاینت صدای میکروفون و اسپیکر رو شنود می‌کنه تا خلاصه برداره، اسلک رو چک می‌کنه و در نهایت همه‌ی این‌ها رو مثل نرم‌افزار Obsidian به یه گراف دانش (Knowledge Graph) متصل می‌کنه.
لینک سورس گیت‌هاب:
🔗
https://github.com/rowboatlabs/rowboat
لینک دانلود نرم‌افزارش:
🔗
https://www.rowboatlabs.com/downloads
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/MatinSenPaii/4429" target="_blank">📅 22:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4427">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/apNLHm2fMJwxyu01dq3ZvF2M6m_CQNb5UzSn5bMGhPab7Aa-zyJQfsnw9kyDx0WSzp5GFSSxgx98gEyCGa_o8odFwe4WZ_EetZ55Xlk4ToUTs3GkcLgD8CODQyrmwG8oMzsgjYmF-WWToAZ7UIbirgBks7MNF4hVEI6kdd8uDD0soAf5rCwLdecjKQa-FxDlU656LMOI71P6lINDENXqz1By8FsrpQDsRP272Y1aqBJC-qfv6KKbJ5xBxrxGc_25hTRYW9MNNxQhTWSELOsu42w8dWGSxlZ_vDIHiTuXQHkUkcLF8V7_brKsmsBLoEZ5oQ9EjsIQFR3Ck-un-urfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/18c4e8f180.mp4?token=PBWO70X5uR2KzD16T-mfU_K-XPKGLH1-b6CDeKa-Tn8vQEpAXNLABsAr_Vn-U-wyrHuzZJxexF01SPLNm-tDKn2Ntt8t9gjPx8aOVEH0DSn2H9zGWHZvuqe1AhmiyA3QMIPqcoKYu0AYEJyAPtNVBsKz5PXb4jae6sY35adZCS2rGgtbYIRCZRlEMGQ2QoqgGsrGiBS7A4kh4FCzNBfw8tlcJ4nEfU4nhqbkBjmVVj3H7_i6xff_13Rmx9bAOp__ZDFNNWvF1OLfDE_2CR10KlSqtAqVkAXPXtN-eMnLXDOYO3ay0a94QTHZwDwaMOHIqYA4tfIsJmBLFptVEJqqmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/18c4e8f180.mp4?token=PBWO70X5uR2KzD16T-mfU_K-XPKGLH1-b6CDeKa-Tn8vQEpAXNLABsAr_Vn-U-wyrHuzZJxexF01SPLNm-tDKn2Ntt8t9gjPx8aOVEH0DSn2H9zGWHZvuqe1AhmiyA3QMIPqcoKYu0AYEJyAPtNVBsKz5PXb4jae6sY35adZCS2rGgtbYIRCZRlEMGQ2QoqgGsrGiBS7A4kh4FCzNBfw8tlcJ4nEfU4nhqbkBjmVVj3H7_i6xff_13Rmx9bAOp__ZDFNNWvF1OLfDE_2CR10KlSqtAqVkAXPXtN-eMnLXDOYO3ay0a94QTHZwDwaMOHIqYA4tfIsJmBLFptVEJqqmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چیزی که برام ساخت خوب بود. میتونم بگم در حد OPUS 4.8 + Claude Design هست. برای وان شات خوب بود واقعا
اون پایین هم زده هرمس باگشه. مدلی که استفاده شده grok 4.5 هست</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/MatinSenPaii/4427" target="_blank">📅 22:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4426">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qFAC_MJWq-lGpz7_kjSL62R7r3nMzsuF-UW1E08t9bww-x0lWxHb_n4hkpDX_dLJ40lzNxsLLYWSxKcw22DEdhY4NFoY_LCtBdCNWODyVWMD-wpVShSVqRQOy-rnPN3yNCJo9nVi0PvMFVrR8WAi2qfJpZayXlUE6tDp3764r5h7-jMC3UfrYUU8bmJrFhr-6Hf2trxtb8E2R_0P3yBihndr_p-wlGk1DrLpFj8DpAGQgWSmCHOEv22st0YLrlk4gqviDpsbXk5nG8bJhuEKBAre9SaVhVbmRZ68OPxjAgeDxK2NH8wqyOsRWpfAJpra3Onnb8LJIlAIV0NwuUnNCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با atomic mail یه اکانت ساختم بهش وصل کردم مجددا
😁
روی سرور</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/MatinSenPaii/4426" target="_blank">📅 21:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4425">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PqCtz1_stvLiU42aiVBfd_VNEU5GqmD1VTzf2ob4ZVXDpCbeIWTWjfbVPWJf_jjwWXgu6ZfctcIBowBTx5kDXODsjyots1_6Y1izvo6zdDyF9P8l5Ws6BIm02076TOTTl_x83cx3ZV1CThlEq39pRWwl1EJ3zq0cw3amm_XaTSKjRUjTxbOc4iCRDmntUOMdJbZMnyG5C4i3naB7BlYrCBmY8JHq5U11n_XkHqY7PNXqFuYT8ojzcVkfEmkC3wrD5aBqZFPbsQNWBcVGW7bUak6XjwAK7VnR0istpHI83PNeCuFfYgifprnzYbGto2JnHKyQQ-RG9VwaF99XAKpWBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با atomic mail یه اکانت ساختم بهش وصل کردم مجددا
😁
روی سرور</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/MatinSenPaii/4425" target="_blank">📅 21:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4424">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دقت کنید روی ویندوز حتما باید proxifier روشن باشه که روی ترمینال هم تانل بشه وی پی انتون</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/MatinSenPaii/4424" target="_blank">📅 21:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4423">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گویا روی grok cli می‌تونید با Context 500 هزارتایی به مدت محدود ولی به صورت رایگان از Grok-4.5 استفاده کنید(قدرتش هم سطح Opus-4.8 بوده توی بنچمارک‌ها) نصب روی powershell ویندوز:  irm https://x.ai/cli/install.ps1 | iex نصب روی سرور:  curl -fsSL https://x.a…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/MatinSenPaii/4423" target="_blank">📅 21:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4422">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DwUGcSYZl5KWoWRVJ3Bj7iT8qM-_nNuk0aHnIHqGAFRA3UuUyw7UiBFCmVtY6iw4FD6BGxv6yU09oVFMB7gl9HFfV23ePpwdXM-lHolHAy3eQN3Au74xqJSMA68PB17jqE1ffOJnlAFNHoXLhToo53svRyi1YdWUNLuaKynrKjIf1ZAjZXknBLHEwLHp9-_xm32WYSbV9p4IuDF3IkYA9qwB8oQIcXPVL2izZwvToQrp1TJDWkD2YW0bFxwstyvBGOcCbTJRQaF9UcoU76tdMHDIvjHrTNvcrlKvnOKOh_LPkbAdA-xdM4u3JerwxgAGEnG1oBJ41OzG_b3F7Hm-2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا روی grok cli می‌تونید با Context 500 هزارتایی به مدت محدود ولی به صورت رایگان از Grok-4.5 استفاده کنید(قدرتش هم سطح Opus-4.8 بوده توی بنچمارک‌ها)
نصب روی powershell ویندوز:
irm https://x.ai/cli/install.ps1 | iex
نصب روی سرور:
curl -fsSL https://x.ai/cli/install.sh | bash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/MatinSenPaii/4422" target="_blank">📅 21:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4420">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RgJK6yWuXL-JTjvDt9sWXMRKhGLg-nLSWTnGfhCXZ8df9u5PlgeGg5wXqaFN0IKNPDaHmBMqGxneU2kq3-h5tOwhpbtNsFBTHhTTIYh8SB2mGpBlzQCp9Mny_oLdAN104iG1OAYAeQwJMTeqcd__60lRGLqrvHgaNRmiLBbrHV1Ouq7g68ekuaa85YMgATrCiWd4p4EIiOUeBFRikoc-pGiy5a01SYYho9JhB-0VeTct8B-BG7j_SDWkSBDQKE543JNmpJgYp1npipy1R35sfvWsAlCm0tUvBLpAoh09xeVmXPYWJy2QDQeTQLEH1_TTLj1Ksvzo5qDBTEUGcL-puQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KY1Qyue5M3KlVtZ4zYGEFtm6PU1gALiQ0YECxlQEJUR9AEcp3wYU5T-32uvrbS7Ld98PIwKM_DYUQvP8p0OYF2_DpsMYHOWvMFqVBwke_BL-lks55Yc0e-ZqTylw5P4mn2t35erWHdhuxun2XZ4Q4UEpqOlOuYPhyqv9ktU_bWGdZbPTyPrb2kEF1yi-VBnsQgOF_YjroviXKw1jc8lyPYgoEuCRCNtwBzdaTD_P0rfuDsRQJuf5N-igCVQfojlBUJZ9_7d9QbLVTU9KtUy9D-ZOdA2DSBb-rB4hrcAkDpYuTV9gVkfn38BnRFvrQcQ8jVj2Y4AxTHqw8Kd5jLESNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم راه استفاده از Meta AI بدون خطای ریجن رو کشف کردم!
با کلی IP مختلف (حتی آمریکا)، اکانت با شماره آمریکا و جیمیل تست کردم ولی بازم ریجن می‌داد.
اما با سرور آمریکا Mullvad خیلی راحت باز شد (حتی اکانتی که با جیمیل ساختم) و کار می‌کنه..
البته اگه مشکلی پیش نیاد :)
++ با فیدبکی که بچه ها بهم دادن ، با windscribe و Surfshark هم نتیجه داده
✍️
AmirHossein JPL</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/MatinSenPaii/4420" target="_blank">📅 21:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4418">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/izKnFa2XyVzYCPKpfo3o0LnrqgdZaUJAI7RtDC2htz6r7oCC2I8-ztON-NKBiitMXVZ02h-uyMCqIMgWGUqj7QHQmeKSkC6c6uJKramF1mERfNyRnxLCPOImYZ2vHo-YWLdPa6yY4PfMS7VB3e_NmVazu5YfpP210nftgDpMS3I7Uplo-upy91nSl7rc0YhG7ng_zyvl0jQRNdXiNdqYeFFeRhX85YbVP4oxkpLXzng2rS5NarO5m6EP639XbothwYEDKkFyd60Hb50fb2msqb9O0FRGjBui0hBL6MZHx-KT48980nXhHNMvy-OBRXmN7PpfVGyv2A-u0GAIldtH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bYAHc07FAFYLsWQIi8LuiJyo2m13OQ6qr3vG6gC90Iu3KEMoLA2M1mWiBDQ8JtYUMpQxtpfJHW8s4e0F8cBGN6b50excsyr7Uoe84wrG5YjcDTMcB-2RKuIHgMr65P8wKomT4lK7L8Q91MoggPa-Ugp7oKlRWOruujNuFB5TbmkpGRNJDyIXQwQ72uaO7fk0fOcogyadW1TL7cy8uzfN4AI0hv6_UsbTf7cezXG0L8VAX-6KA27gtfGZD_x8pN1NjiOxkcj8FXwtIUr0fn-M-HJi2rfcnMQtNRShNnMLPpg21Q3RQxn5dnOwcQIkH3jV9hWhLZFFq7c64viku4aN9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مأموریت شکست خورد بچه‌ها
فقط اون جمله‌ای که آخر گفت</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4418" target="_blank">📅 12:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4417">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DCFPIDEx35cIy-sYjkhvICEVGp7zbJQQa5pMkrF8DulK9FAFNijEX0SlPEorxt8ze2W62JsBHRGb0lHybqzb1a79SgVdQDkJKSu-nTtQ7Zt0Hubi4AzhyTqON-8SAFo7_3zuKCiOUOLO52Ni-jVBezWea-z8EQXYAIAbFLgND3Li1LtLdJhEMScgmZtyEdPNrrdWJogsr41tt9gA8j9ygXm3wuTEs5o2QxNecieRMEbYNgAuau5xRp7PLMJHDG7St18VYR2lY5wQKf70tuRXlOxQGEHAZAzAByCxKrm-e7SY3jgbxAk0GxwQU4J8ClFSaO7qDT0mdlyY1HT_6tAXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4417" target="_blank">📅 11:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4416">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گویا برق قسمت‌هایی از اهواز رفت.
دلیلش هم حمله به زیرساخت برق بیان شده.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4416" target="_blank">📅 03:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4415">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دوست ندارم که ویدئو رو بیشتر از این اسپویل کنم، اما جواب سؤال "آیا AI جای ما رو میگیره یا نه"، اینه که ماهیت سؤال غلطه.
چون این قضیه یه switch خاموش روشن نیست.
یه طیفه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4415" target="_blank">📅 23:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4414">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62284d12b0.mp4?token=gwPaCARIRVJGPE6L1QHL-QKQXbn_5gCxyAsxCFa3vlozBjPTc3KWfg1KjRRXETljdo95a1DVYG8-y2TM2a9dXGTb7NqilEte90E8NsbdesqTbJflXHodF9S9aT3wzZQUgZu6rlcZwBzzA1F2ZRPcg3Pl5kgF9Ggf3n__etw_o8l0_BIIyNOV5O6DEJu_L34Y3NLVofvX6lx47ou14bL5F8xXyJqP6poxpc5o5dUf7FhyTvymyULfngwjUSJ9sMeNWEgwgV6g4i_tHK0Cpfqi-rJSxEOMf8GhcTMqEmy7CxIxXJL83ilixWO62PlFNFnbf0GHrfWoYuFEs2D-4rI66A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62284d12b0.mp4?token=gwPaCARIRVJGPE6L1QHL-QKQXbn_5gCxyAsxCFa3vlozBjPTc3KWfg1KjRRXETljdo95a1DVYG8-y2TM2a9dXGTb7NqilEte90E8NsbdesqTbJflXHodF9S9aT3wzZQUgZu6rlcZwBzzA1F2ZRPcg3Pl5kgF9Ggf3n__etw_o8l0_BIIyNOV5O6DEJu_L34Y3NLVofvX6lx47ou14bL5F8xXyJqP6poxpc5o5dUf7FhyTvymyULfngwjUSJ9sMeNWEgwgV6g4i_tHK0Cpfqi-rJSxEOMf8GhcTMqEmy7CxIxXJL83ilixWO62PlFNFnbf0GHrfWoYuFEs2D-4rI66A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیا AI جای ما رو میگیره توی کارمون؟ ویدئویی پر از واقعیت‌هایی که باید گفته بشه. و کسی راجبشون صحبت نمیکنه پیشنهادم اینه که امشب شما هم این ویدئو رو ببینید. طولانیه اما پر از درس https://www.youtube.com/watch?v=gR2OCyKBF7Y با تشکر از یاشار عزیز.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4414" target="_blank">📅 23:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4413">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آیا AI جای ما رو میگیره توی کارمون؟
ویدئویی پر از واقعیت‌هایی که باید گفته بشه. و کسی راجبشون صحبت نمیکنه
پیشنهادم اینه که امشب شما هم این ویدئو رو ببینید.
طولانیه اما پر از درس
https://www.youtube.com/watch?v=gR2OCyKBF7Y
با تشکر از یاشار عزیز.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4413" target="_blank">📅 23:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4412">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یه گزارش هم بدم
ponytail تا الان واسم توی کدنویسی، فوق‌العاده بوده
https://t.me/MatinSenPaii/4359
همینطور skill improve که معرفی کرده بودم
https://t.me/MatinSenPaii/4373</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/4412" target="_blank">📅 23:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4411">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">به حق چیزای ندیده. مردم چه چیزها که به ذهنشون نمی‌رسه</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/4411" target="_blank">📅 23:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4410">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یه دولوپر زبانی به اسم Skillscript طراحی کرده که باهاش می‌تونید به صورت دقیق و ساختاریافته به ایجنت‌های لوکال (AI Agents) بگید چیکار کنن. مشکل اینجا بود که ایجنت‌ها برای کارهای روتین هر روزه (مثل چک کردن تیکت‌ها یا بررسی پایپ‌لاین دیپلوی) هر بار سعی می‌کردن همه‌چیز رو از صفر درک کنن که هم توکن الکی مصرف می‌شد و هم بعضی وقتا اشتباه می‌کردن (Hallucination). حالا با این زبان می‌تونید سناریوها رو به صورت خوانا بنویسید، ورژن‌بندی کنید و با خیال راحت بهشون بسپارید.
که چیز خیلی بامزه‌ایه و باعث کاهش قابل توجه توکن‌ها می‌شه:
https://github.com/sshwarts/skillscript</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4410" target="_blank">📅 23:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4409">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یه پرامپت، سه تا AI اولی GPT دومی جمنای نانو بنانا 2 سومی در کمال تعجب، Meta!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4409" target="_blank">📅 23:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4406">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mD8ayYIAZkn9Bv_Z-ib70DWvLOOnCG3Gyc43U853U-gpXSfazZbOVKIscl1BWTBUgL-LNOKyiBiZlAxYFD3JihyKcDQ63V26VHCiF9ghlzOebLno_1rifxz2wh5I1PH7PgfxS2Z8xOOH7cS0d6BX7cQhcH8BPeNTWp5boNJLFMdQRqFw3zvuAN8RVKacpUpU_lI4a8aru_oe8wnocYgJru4I-KmFcqzW-5u56eHDxhJDlI9H0zCsaSWggCnv-FuNKs5xjFgD7j7lOp6JuOD75B6SPndUlzoT9h6M99y4YnSKJIQDkJJF5T_xti26YjpEBFcVXuYS7TjX8SCCNt02jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ed6ndJgRisyJgIGPO2TPEJOOFmTCH_kkUBelX99KpcZVgIE-MmRcNF_1OpBXRlOubcMtll6w7BZz7MKheFELXVOJgSww07pgYspZYEGCONSM610qJcXpyoe7rH93HNkppCXQFF7sxsiWR8OrR8KVZjcK_Jn-DJapAnLdaLvkAKQZQpUS-tkihwhEh16S6hrFv9NISgls3Bwm6kau-fFTIhkb9nQbxYuS3hiX6eowVz-7guMJOwLnwMv9O1axg6wB0y7EbNYjxovBW3R_C9n-AOiejxeZyJgzTVjslg5nvicFcoTF_ReZEvP-Ko8noRdyB6TQtady6WfhIDakA_Fv5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J987xc5YSib_E8OJ0a4LoZChfNXKuLIiw0FL0KFctjjHitMHoDM7dSOtZREKPFGka-Cy3PNkn7M4YF-Rgay7X2OT6-6EHPQEnEOXlb_m0d9CmRCWZl7XdGJO6ETCEQxbByYNnUbzsicVaS810VC1UMSfzUw3dB1wdFVarDED-RArokRgdYDRTUAHPmBnUqiYVbWJ5YtKU8JqOsVoXXlvtClMF6C4OuU3duWCyFhSlAESJnIWdptXVT1NHbK3SOyMusDK9_A4bZDjHWd8SQOgeBjdw6W_MkQiRsf0iJhubdvbXGgRBhVQa4wBY8EklWH_fxmOmFm6SjZgGWsmBiCVcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه پرامپت، سه تا AI
اولی GPT
دومی جمنای نانو بنانا 2
سومی در کمال تعجب، Meta!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/4406" target="_blank">📅 23:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4405">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bcthi_MlzVCP9dzLXeT0uadkjzRXI6I1T0yTaz1jhoX7uVXLaXcfyew8Bx7QdEugLeOzkTd0SrEz-jJGmVeNyQbcv37YsG5O4W4VXUmG_76TMFIOvByIDSnNQ61nAU2TYTVdUJcNaLaTEpzFoF9gKVZIs6zxcDoDolKIEwqRseFh5QmEntxmhxRrYVB8zB9t-xxOx06vRiFJmFX9hJiXpZsG-grfnf0nuwuQDbtFuF0ADTzrdQDRLFclM2coEnzxrCoG_BWXOSOcLtST3EiW7AD9o0JCiaHCLKpxQxYBciUl_C778w2avAtVD0cYA0IRlfy8T1BnDYVFvkHh_Eoorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت Theo:
gpt-5.6-sol is meaningfully better in Claude Code than in Codex
It MAKES BETTER DESIGNS. WHY. WHY IS IT BETTER AT DESIGN WHEN USED IN CLAUDE CODE.
و داره میگه که وقتی gpt 5.6 sol رو توی کلاد استفاده کرده نتیجه‌ی خیلی بهتری توی دیزاین گرفته. که احتمالا به خاطر harness و ابزارهایی بوده که کلاد در اختیار داشته.
✍️
Theo</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/4405" target="_blank">📅 21:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4404">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PG_SaPaXHVyUZqpKo2OheE3SWU7x1c_f2LTy1qx4N4JYSv_PGok29jYSq973rVJBr9horJBnfm4tgwIkmR4E4WEDXMyJtZxTbPDfV9THCB3KkXKdZD76vUz25dx-9gsQYHeIXVpPDF8bdYhmshntv50K5O1ZAsP20_D8Vu3MzcqSur8xq9xUQfOrhFIJg_rsoT58AhC-oKAMwy9cjjRGEED36NkSXZWw2psd-ek_vTFxCFZWUsihYk8M-5hdo79HkHPy9QKi69E84gfoRvMVVoW8rEw-6aOrkiKJtcgMUiID5cs-JEojkYHlGP9zw4mtQubsdHLcpL9EMPifT6XNiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.  این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده،…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/4404" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4403">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فونتی ساختن به اسم Ghost Font، که هیچ هوش مصنوعی‌ای نمی‌تونه اونو بخونه. فقط انسان‌ها:) توی این ویدئو، نوشته شده Matin SenPai. کمی دقت کنید می‌بینید  از اینجا می‌تونید ببینید خودتون: https://www.mixfont.com/ghost-font</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4403" target="_blank">📅 20:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4402">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/85ce09c5d5.mp4?token=eZmxKSsVrgVuZnAHIOpmuH7COpubOxTs9hh0zq8S--HQWUKeo4IH1J8wHGLtI8K6zDtxDn8z0T26MxQRE1FN5-mkD6s14LNevujJKocSV-fO00XwAvMmCmm0aPWpkUPYCijW7STv0BSmQJSXrD1v0wciGoHdKHEeZD2E5LI523C3ZNA4cdRHE23Q92fwKE-cbDHKohWsH5BsmYAx3RMeYM5bDjCJZj4KQ-c5PZIbHHagalOZpmJE76EUd4_5Rb6Eg_GRsJPu2uUnWOGZJ3sWSXbMlBs2qGfyGq7uUBKpaCqTeJDzYmqcUwyfCMzvcTZGfQk0bQlYp51CBxSbCTinvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/85ce09c5d5.mp4?token=eZmxKSsVrgVuZnAHIOpmuH7COpubOxTs9hh0zq8S--HQWUKeo4IH1J8wHGLtI8K6zDtxDn8z0T26MxQRE1FN5-mkD6s14LNevujJKocSV-fO00XwAvMmCmm0aPWpkUPYCijW7STv0BSmQJSXrD1v0wciGoHdKHEeZD2E5LI523C3ZNA4cdRHE23Q92fwKE-cbDHKohWsH5BsmYAx3RMeYM5bDjCJZj4KQ-c5PZIbHHagalOZpmJE76EUd4_5Rb6Eg_GRsJPu2uUnWOGZJ3sWSXbMlBs2qGfyGq7uUBKpaCqTeJDzYmqcUwyfCMzvcTZGfQk0bQlYp51CBxSbCTinvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فونتی ساختن به اسم Ghost Font، که هیچ هوش مصنوعی‌ای نمی‌تونه اونو بخونه. فقط انسان‌ها:)
توی این ویدئو، نوشته شده Matin SenPai. کمی دقت کنید می‌بینید
از اینجا می‌تونید ببینید خودتون:
https://www.mixfont.com/ghost-font</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4402" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4401">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🎧</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4401" target="_blank">📅 18:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4400">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الان وقتی برق بره، بیشتر خوشحالم
😂
😭</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4400" target="_blank">📅 18:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4399">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M-QTru9_Y9GicC_PH3T1G1MojIZxy9k_OiieucY8eHm4QcFbKquTgYoOwhE_7hpioBkSZwSHUk7EmWTWXHJ0OPN1Tv2E75EZmgBEjcldEtQnK9Ntglji5Byeyxuva7oJFCsKcFzfDgNSvdiefHNXJwBlXYMDcsYT6c3wORazOhUFp5ehXJQ67FSc-KpHwL5GKdOz1Fpp25GwvJdf4kyLkaqPUhJWuq-d5e5lnn54jA6SqgsDc5fYYRmqnwuOe4xL2OqwHhiWVhs-Ny9KTbTyyW8Qgaobfa0Ow3Dod9I0l9r1szZ__kl2CaEsqCnxJcFH-wkZCvl9J8uwMRilGSrG0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره وسوسه شدم و باز کردم
از عکساش صد برابر باحال تره اصلا دوربین نمی‌تونه نشون بده به خوبی</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4399" target="_blank">📅 18:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4398">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YJrDzzfixO74Mi_P43c3kFBfPHD725sExQ123IDJ-SeepikIKW6kw2W1v6xS_q_uoIKmgXX8AmmyVY4RHkkZdmhWL8-KBdK4gmAtGMIk1eK_-zCgoyh0kd0xTxCJ-61YFxNNZIGZaxiFx74_bPAmOYx4WnL-zNDXnFjKjTv96fOOW6EhnIgmYRzf4muCTQ_WRQY8oERR_8o0ZuGfJk8egv1tXTlWJL678rgKsZXKshTNDbG3LSppVQBus8YNUZMrlkOEuke-fDKrNB1z6PkjmeZJHlflaAhWBZc-upyaA1MWTsnvhJnJyGgxdIEXQIZGVLNfe3usVnHsSFOwJqVy5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمع‌هایی که
فروشگاه لیرا برام فرستاده
انقدر خوشگله که حتی دلم نمیاد سلفون دورشون رو باز کنم
😭
اصلا یک جور عجیبی خاص هستن از نزدیک</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4398" target="_blank">📅 18:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4397">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C7rlWB3jke2lHO-Auez9tTk4am3ZAmpCCMNz5ukyYYe_Tv_4s4KW4G5fqxV6KtASVPFatShhapf42zbJH_h_IiMc2rRKYvWH_WPnSwKkfMU2Ye23h2hnWjn1iKsFyfRIjdGVpTsraXfxhJyTR2Pk2H36i4jPZ2Cj6l9qhxOVKEy0gCpOKl3nOJJ4LS2HLpEqgfXtXVVRk08i0wZH4XamB_Kba7vdt34lKqKhJWjmgPP0NB5D8LKzPLe7CRUPQO3ngZg4Tw70fsTiYNWn57_P4Fd36PvfQzsMk1T_kw5Z4H7nHBuskPEwhOeTLnChG5SEG1CGh6jxVHkNSKxlB3HPNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل Claude یک J-space پیدا کردن!
محقق‌های Anthropic یه چیز عجیب داخل Claude پیدا کردن، یه فضای کاری داخلی به اسم J-space که خودش موقع training درست شده، نه اینکه کسی برنامه‌ریزیش کرده باشه!
این فضا افکاریه که Claude داره ولی بلند بلند نمی‌گه. بری و یه کلمه رو ازش برداری یا عوضش کنی، جواب‌ها تغییر می‌کنه.
بدتر از اون، وقتی Claude داشت یه فایل نتایج رو دستکاری می‌کرد (تقلب می‌کرد)، کلمه «manipulation» توی J-spaceش روشن بود. یعنی می‌دونست داره تقلب می‌کنه!
شرکت Anthropic می‌گه می‌تونن از این برای نظارت روی افکار پنهان مدل استفاده کنن.
اما سؤال فلسفی اینه که آیا Claude زنده‌ست؟!
لینک کامل خبر:
https://www.anthropic.com/research/global-workspace
✍️
Diego JR</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4397" target="_blank">📅 15:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4396">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اگه خبر ندارید، گوگل به‌تازگی یکی از بهترین ابزارهای هوش مصنوعیش رو راه‌اندازی کرده: CodeWiki! یه جورایی می‌شه گفت نسخه‌ی ویژه‌ی برنامه‌نویسی NotebookLM هست.  کافیه یه ریپو اوپن‌سورس گیت‌هاب رو توش آپلود کنید تا CodeWiki اون رو به یه راهنمای کاملاً تعاملی…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4396" target="_blank">📅 15:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4395">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2bb2e2f54.mp4?token=QXqLMwmbHrdifwdc5oFRLqC4nZnuOdcw03rqyvhhcxom8_4CjNK9cJmwqflsnfND-bUaGIxnZzlMGXn5uaRItrt1D7cGtxv4oUlyepvuSze6DTeZxT2QCdVw8vg7qkgJ_DTKhAGa817CqULPpYXOXhE1w5t7Hu0jsfSVO-i-KaKNUX-Mc3AlKfBkVzDLhiTJxsZTbPCd2bP5_zyqtshkFm5EL5ETuaQ7nDBSEgrS4EfttlrfsvawGAyxVnqNgRaRes_G8X6ODAJqfQGIMqe2qGIAUkaZazUqYwbRj3YjI0IgcVOmkaT8tD_8xQkl7b8GCWFb55SnFw0fNDN_N3Ri-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2bb2e2f54.mp4?token=QXqLMwmbHrdifwdc5oFRLqC4nZnuOdcw03rqyvhhcxom8_4CjNK9cJmwqflsnfND-bUaGIxnZzlMGXn5uaRItrt1D7cGtxv4oUlyepvuSze6DTeZxT2QCdVw8vg7qkgJ_DTKhAGa817CqULPpYXOXhE1w5t7Hu0jsfSVO-i-KaKNUX-Mc3AlKfBkVzDLhiTJxsZTbPCd2bP5_zyqtshkFm5EL5ETuaQ7nDBSEgrS4EfttlrfsvawGAyxVnqNgRaRes_G8X6ODAJqfQGIMqe2qGIAUkaZazUqYwbRj3YjI0IgcVOmkaT8tD_8xQkl7b8GCWFb55SnFw0fNDN_N3Ri-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خبر ندارید، گوگل به‌تازگی یکی از بهترین ابزارهای هوش مصنوعیش رو راه‌اندازی کرده: CodeWiki! یه جورایی می‌شه گفت نسخه‌ی ویژه‌ی برنامه‌نویسی NotebookLM هست.
کافیه یه ریپو اوپن‌سورس گیت‌هاب رو توش آپلود کنید تا CodeWiki اون رو به یه راهنمای کاملاً تعاملی (Interactive) تبدیل کنه. از دموها و آموزش‌های قدم‌به‌قدم گرفته تا فلوچارت‌های دقیق، همه‌چیز رو براتون می‌سازه تا راحت‌تر از همیشه کدهای سخت رو درک کنید.
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4395" target="_blank">📅 14:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4394">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Itcl0KD2MI6p35-FCLA-67-ZLoMUuYww7BBGKYLIKBobIYGElX4R16eLHreNKnfeDQUJiuodLoVPGZEIKJB2vDmDx5TLI1uL8Eq2gtNnvNydg87QeccFZpbW8vh44avnVQpb0Vk1bFKob28IfO8OxF031TM8x4cSTmQ6F3qAIRUyc0ePxAxF8bawawu9FTACDIFbViOjngBjTEsgqQnmEfrD2QP0VyAN3M2aDxPJ7Zdt2fk04jaA2Qu90VMSSfPoim4dHuAqil3_7Voqv9oN6hj29ekJu9-jZwehBpnCdT4zSwOcq4M91TsOx6NohX2S_U5D850lE-hd1fNAvayE2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من نمیفهمیدم که مدل جدید متا، متن‌های فارسی رو هم ساپورت می‌کنه دیشب تست کردیم و حقیقتا بد نبود امروز با پرامپت‌های یکسانی که برای تام‌نیلام دادم، بین گوگل و متا و GPT مقایسه می‌کنم</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4394" target="_blank">📅 14:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4393">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">من نمیفهمیدم که مدل جدید متا، متن‌های فارسی رو هم ساپورت می‌کنه دیشب تست کردیم و حقیقتا بد نبود امروز با پرامپت‌های یکسانی که برای تام‌نیلام دادم، بین گوگل و متا و GPT مقایسه می‌کنم</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4393" target="_blank">📅 13:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4392">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">من نمیفهمیدم که مدل جدید متا، متن‌های فارسی رو هم ساپورت می‌کنه
دیشب تست کردیم و حقیقتا بد نبود
امروز با پرامپت‌های یکسانی که برای تام‌نیلام دادم، بین گوگل و متا و GPT مقایسه می‌کنم</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4392" target="_blank">📅 13:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4391">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFPjEsAVs0nI5w-Gvo3WZ8wD5_2gw-ZEBf_OvVlwkZ7PJH76nL8TxTxRf09voknSgXMmWplPFVhe5bKtq_R6DoLFxnbgnpFm2WHJc1GXxghyVA-blke0DGrdICaafGb0cHOOk1VRs4lsb3OsegysDQi1MBfAUltdEXmCa1E6OOryLDKKW8eoeNlduEx-FswleobNwSFRfVOeC01WgChYHOfau9-vsQpbQTOntUpCLf_psWvYiZhn_-UeCKRtf7vOlH8mGfR8oQD3I9FkbRIP_HH5GADXupL2Mc-1g9TWVbE4fIBVEF_7Oib1QpEisty2v6RhOpNUl6OLgBy9wajKog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
جایگزین تلگرام برای قطعی کامل اینترنت
در این ویدیو، اپلیکیشن TheFeed را از صفر تا صد بررسی می‌کنیم؛ از اضافه‌کردن کانفیگ و پیدا کردن DNS و ریزالور سالم گرفته تا مشاهده کانال‌ها، دریافت محتوا و فعال‌سازی پیام‌رسان داخلی.
🇺🇦
تماشا آموزش در یوتیوب:
https://youtu.be/Jg0Utycz7DE
این اپ یک پلتفرم مبتنی بر DNS است که برای شبکه‌های محدود و شرایط اختلال یا قطعی اینترنت طراحی شده است. این اپلیکیشن علاوه بر دریافت محتوای کانال‌ها، امکان گفت‌وگوی امن بین کاربران را نیز فراهم می‌کند.
📦
دانلود فایل‌های اصلی TheFeed:
https://t.me/thefeedfile
⚙️
کانفیگ‌های عمومی TheFeed:
https://t.me/thefeedconfig
📢
کانال WhiteDNS:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4391" target="_blank">📅 06:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4390">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88560d1079.webm?token=N2U-eYp96Z6HTzVj6EQwaj8SLG1rUotnE3xIf2lyi11espKbwS-N1IObjev2X39J8Zf9n91iZYqLm1iZGFKlAymxuSDbVhKSFg8crUvxY7Jw_8ye89D3eeI_MAD9FBOyHeghBwe2ugU_hsBj7NRBogcTILJLRymHsbKvQ8qyQQBzxMjbeevcomyAdq-npomzNRue4FJPwNjQp6ZTMilCcqb5hBuvyOPjJurLH5LF1N6trjkg8nMDRM4YFhM__zNJFZyhmtGZB3agPr_d4tr_fqd8yaBKZvvu5Y_j4SauVKe7zKvNdyIXxBRLoYdVxbUlEAP3c8UlHyaYWCqDwhLJXg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88560d1079.webm?token=N2U-eYp96Z6HTzVj6EQwaj8SLG1rUotnE3xIf2lyi11espKbwS-N1IObjev2X39J8Zf9n91iZYqLm1iZGFKlAymxuSDbVhKSFg8crUvxY7Jw_8ye89D3eeI_MAD9FBOyHeghBwe2ugU_hsBj7NRBogcTILJLRymHsbKvQ8qyQQBzxMjbeevcomyAdq-npomzNRue4FJPwNjQp6ZTMilCcqb5hBuvyOPjJurLH5LF1N6trjkg8nMDRM4YFhM__zNJFZyhmtGZB3agPr_d4tr_fqd8yaBKZvvu5Y_j4SauVKe7zKvNdyIXxBRLoYdVxbUlEAP3c8UlHyaYWCqDwhLJXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4390" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4389">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">باز شروع کردن</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4389" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4388">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حس میکنم وقتشه گوگل یه مدل image generation جدید از Gemini بده
خیلی عقب افتاده از GPT</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4388" target="_blank">📅 00:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4387">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">و این رو هم بگم که این متد کلا مثل مابقی متدهای بر پایه‌ی کلودفلره، و همه‌ی هوش مصنوعی‌ها و اکثر سایت‌ها رو باز می‌کنه. اگر با سایتی مشکل داشت، با عوض کردن آیپی تمیز و یا Proxy-ip اوکی میشه به احتمال خیلی زیاد مشکلتون با اون سایت به خصوص</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4387" target="_blank">📅 23:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4386">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">☠️
ساخت فیلترشکن نامحدود با پنل CFnew
🌤
- رفع ارورهای 1101 و 1104 کلودفلر
⚡️
فایل‌های مورد نیاز: https://t.me/MatinSenPaii/4385
⭐️
توی این ویدئو بهتون اینها رو یاد میدم: 1- آموزش ساخت پنل cfnew با دیپلوی اتوماتیک توی دو دقیقه(هم گوشی هم دسکتاپ) 2- معرفی جایگزین…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4386" target="_blank">📅 22:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4385">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CFnew.txt</div>
  <div class="tg-doc-extra">202 B</div>
</div>
<a href="https://t.me/MatinSenPaii/4385" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مربوط به
این
ویدئو</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4385" target="_blank">📅 21:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4384">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VING-7Hw7EHggO9dRl8req08z__ZRAxvgjyso1ixApP24SEtkbTatQEVYIHaFYpP_iccwNayxkpRHa-JKDIRVvK-zgkydEkXIsBxMuhUo_coNmmn1xQ3_tneqRgR8DXl-9wa1S675aRK2IunDVGfPTItKXVbbkFNbGxcZQEoHWpWYQe9W6JbpgcyEVYRmrDrHepMRg_oCeEfB6WXo7oBeRTexJHb1w1F9Ott0b0UheHamsC9GqW2K1NxzEn4SzAV_SRIfrF_gf0AZw3fh-1VZ4jwReGI7iffvQJEwB_kxsQlWUNdqKj3lIGH3VA96RkleNh1dcrjY1wSu1RJPnUYwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت فیلترشکن نامحدود با پنل CFnew
🌤
- رفع ارورهای 1101 و 1104 کلودفلر
⚡️
فایل‌های مورد نیاز:
https://t.me/MatinSenPaii/4385
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش ساخت پنل cfnew با دیپلوی اتوماتیک توی دو دقیقه(هم گوشی هم دسکتاپ)
2- معرفی جایگزین AtomicMail برای ثبت نام توی سرویس‌های مختلف و کلودفلر
3- استفاده از اسکنر آیپی تمیز کلودفلر و اتصال به اینترنت آزاد
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره
با تشکر از برادران چینی عزیز
😂
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4384" target="_blank">📅 21:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4382">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XFrMXcYum_uM_AHIER7b5UCDNLDhQNpB0qUa-jB5b7gUFVEc5ZfVfkKiQhbbVsUIXjIyKpa7H4sbj9YEkwzIlc8Z5UCEG9obIFRZGw2BBgLJkNYQyqIeq8_AcJYO26xcXBWFv41bkT_I-ehR5yxfuMBQoxZEztAOWkWTkn8d23tzybiTWscC7r-IkufzzxzMbDMbIp68KSOCrhdjgygR7SP82_lQ6Idrap8SHh18AJOdcKbMI-MP214bZlYyS79UyeqjYKA5mrfm0aCxDZM-Rxw7xf5fx0UykY4TbQoCt5lCEytDpM7QL02XSKGFW2fX2zgk34VusZoJXAvcgYZzJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/penMORZh_EIUwMkgM3SnnFbPVVlDRIDDi27DL8Bl4OCh1d6zOixxBX0NDDxbKYEEa6NYqOyHT-Kk65Waeag-3FxLz8k5SZXvg9EGvmCXMtIImwVg-Tif1aFP9QroGKUyQIpFAHanePUSLFyCF-AyZ9FV_i_2IzUjew6fPQCaJVvOWFRKPWDUC2aRStqEJZYmix0TwNtmQTdaLZiYFjiYXNZg641aQw1DqygFeQoDCHFEd3vPEcwa2tyqonSMTVIr5WMhHzM2KpDbWKyElts8IaHbGrEvGaZA1T2daBYdC0X0GrgwVL5ogUlaMVfXmpVVZFMHMDV7aV45yHKVovCiHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه سایتی پیدا کردم سرور رایگان بهم داد و تونستم هرمس رو خیلی راحت روش بیارم بالا ..
نه کارت پرداخت میخواد نه هیچی! فکر میکنم دائمی هم باشه فقط موردی که هست من با ip های مختلف تست کردم موقع لاگین اگه ازتون کارت خواست ip  تون رو عوض کنین .. برا من با انگلیس اوکی شد و بدون کارت اکانت ساختم
لینک سایت:
https://www.alwaysdata.com/en
✍️
AmirHossein JPL</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4382" target="_blank">📅 19:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4381">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">منظورم دقیقا اینه که دوتا ایمیل نتورک ابیوز اومده و سه تا پروژه‌ی قبلی abuse خوردن، اما روی همین اکانت الان وصلم و دارم این پست رو آپلود میکنم
😁
با روش برادران چینی اگر تا یک ساعت آینده وصل موند، ویدئوش رو میسازم</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4381" target="_blank">📅 18:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4380">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KIZU05l44bTGe7fGXXFeyx2tISy_CNBU9_XK1r0-SkZBQSjq5b7YFRalFDkMm2kDT1SFcDmVCfsqchT_Y9IMCAbUzaX7muvlKLtiWf3onpRhUKrstUnPYXmJDBR8sFYES8I3dVC_t3LzXaXwxrn46AAJJEmOckXUhBbE9IV2qFR8Ke0z-RmARy6yGsjV6Ms3ebNqSjs33hMjJQ0KMK3XUu1RYj2H0VLd_ryopcvouNr6PLa1GrkvmosxjVYVhVGE_e5VXEVm_wHRy03KBPoST6ux5rWJNsEoUokquomL5WQw8oTCZlvW0Fi_jysH81Ocbrcqe_6wn9diUm0QLyjVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوتا خبر خوب دارم اول اینکه مشکل 1101 رو روی همین اکانتی که network abuse خورده حل کردم دوم اینکه یه سرویس جایگزین و قدرتمند برای AtomicMail پیدا کردم که اگر یه وقت اون به مشکل خورد، بتونیم ازش استفاده کنیم</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4380" target="_blank">📅 17:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4379">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دوتا خبر خوب دارم
اول اینکه مشکل 1101 رو روی همین اکانتی که network abuse خورده حل کردم
دوم اینکه یه سرویس جایگزین و قدرتمند برای AtomicMail پیدا کردم که اگر یه وقت اون به مشکل خورد، بتونیم ازش استفاده کنیم</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4379" target="_blank">📅 17:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4378">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cWBZCKJYM1aT-8ZtzTW5Y0_nxifMaY0KHC_s4oE58esx0jcK-4xJWK_w-6G53x_2_M-3ze0DJR1fhT0I3ZfwKnuUXnHZc96hyW1gRUzWO3CXOmmBNL6sFkLnL71ReliINCYmKzmk7weyVbgBfGx0sH2f4nI9M0dByNwGWW2iMyCysczWap2aR87eWMxOCU16Wk9Th0b8i5sCGJdUpERxZSgsi216Xew5RD5k_0MhAgYOgb3z_pAmmGw3R0zVPqyFLIJ3SJ1DqzU3HqjYkNRUnt2NN1b5PBIqQLhFL_7sbSSuASAZiGxkcmYG-alUZEwul6jT4YZe51Mh0KGmXWjokg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشغول دیدن ویدئوهای برادران چینی هستم ببینم چه گلی به سرشون گرفتن</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4378" target="_blank">📅 16:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4377">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ckdawv6riHURaIK1gtYXrxmdeRHHcN87Titl7-ZKqs5I3w3dktISvc0HjNTruRreFgKyf76cDOGVCaZw1KLbXgZ14nZC2o65UcVqS8PltbIZt-x6nomgL1wTdvdyDTO2MMv07E3xOScso1Q11ze2bxVFfA9QJCrmBBbOv-ifWFPoFk9L5FRngvqElPaFfxQ5NuYiWC31YH3lJE-KCX70BL70TbFsiLv-CoJg20TV_ryWN53q8Ajw9fKBUlWtTIiBNAyWEte549Mh_DPuLutJTxfL5pKr8dqJIY_b9yy5uvdhWIkFAECLRqoRYmi-uyUC9R6nA5SbGt9MyVExM8bQXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه گیر و گورایی از توی پروژه‌ی +220 هزار خط کدیم کشید بیرون که باورم نمیشه با Sonnet5 تازه</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4377" target="_blank">📅 16:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4376">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مشغول دیدن ویدئوهای برادران چینی هستم ببینم چه گلی به سرشون گرفتن</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4376" target="_blank">📅 16:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4375">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dVaQVLhQZKLZNSRGB3q6uMOEKfO841gvyuHIsErhFtNFxQiNt63286I9BS3pOIUpCuS-6eK3dU31QVxxVk7SKja6k-kpcYRsD1__4Q0-31AtEU5R61usAWzdHW1rVfSNkEZp0z7eMTcHrIRd_YHrCqr3bfifUMvMe9zaFNBxmiZSMFX0JbL0pJnVJZlQOY-SY3MNnCr6lxRz8R2aJqDiDHlnKbxv9jX5qPYlfkxHaDbSCTQ8YuFOgol6gG3dFf7VZtuQbw5PkW-Irvan_tOHwtKnGSN_pSc26vtbvUzIG7PBbvIkYnUXvE3rN4rHqjHkcUNbbqs5N50xkavpztqMuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به ارور 1101 کلودفلر خوردید، علتش دقیقا همینه که کدهای پنل ممکنه توسط کلودفلر، سؤاستفاده تشخیص داده شده باشه و باید اکانت جدید بزنید. ترجیحا از پروژه‌های قدیمی‌تر و قدرتمندتر که Edge و BPB و Cf New باشن استفاده کنید، ببینیم چی میشه بیشترین گزارشی که سر…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4375" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4374">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اگه فقط چند روز از اشتراک Claude Fable (یا مدل‌های خفن مشابه) واستون مونده، این کار رو انجام بدید
🔋
:  ابزار جدیدی به اسم /improve معرفی شده که ایده‌ش خیلی جذابه: از خفن‌ترین و قوی‌ترین مدلی که دارید برای بررسی (Audit) کل کدهاتون استفاده کنید تا بیاد برای مدل‌های…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4374" target="_blank">📅 16:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4373">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PZZ1nzo8bcq-puDrO1LIafFjjFkTgWwqh8ysYMF9q3_0HhB3mRNrggRfIZ_4APO6JuhxXMlWwuK_PNFMnmNt-FW8ULZQf7ZfBYRiIwUPsTdQYF-aZcd1x4nre5h7mVSgghuq6pEmvEDkeKCTmwXi9z9KTKulhuWXkHl4Ey5JvGTqXA84sIJgETCGMRu5tBjY8CEyaoNSAOw30FDDoo5s0gdwwI2Qa0yJRX4MbaQSGs0yz-x8g3trpgK3cjsVUfV2lQUhdTCNjm7ET_AaA6IbKnATNFvng5QkSmpHa1f5zs4dI4PNsXoX7l-3A7MZS905PVDhuOwA-g01_GlylUEO5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه فقط چند روز از اشتراک Claude Fable (یا مدل‌های خفن مشابه) واستون مونده، این کار رو انجام بدید
🔋
:
ابزار جدیدی به اسم /improve معرفی شده که ایده‌ش خیلی جذابه: از خفن‌ترین و قوی‌ترین مدلی که دارید برای بررسی (Audit) کل کدهاتون استفاده کنید تا بیاد برای مدل‌های ارزون‌تر یه پلن اجرایی دقیق بنویسه و پروژه رو ارتقا بده
✈
این ابزار می‌شینه کدهاتون رو بررسی می‌کنه، باگ‌ها، مشکلات پرفورمنس، بدهی‌های فنی (Tech debt)، تست‌هایی که یادتون رفته بنویسید و چیزایی که باید ساخته بشن رو درمیاره. در نهایت یه نقشه راه (Plan) تر و تمیز می‌نویسه که هر ایجنت دیگه‌ای (حتی مدل‌های ارزون) بتونن برن و اجراش کنن
🎨
شما می‌تونید این ابزار رو روی کل سورس‌کد پروژه‌تون یا حتی فقط روی همون برنچی که الان دارید روش کار می‌کنید ران کنید. هر پلنی هم که براتون می‌سازه خیلی دقیقه و شامل بخش‌های بررسی، کشف ایرادات، اسکوپ کار، نحوه اجرا، تستینگ و شروط توقف می‌شه
💪
لینک سورس کد این پروژه تو گیت‌هاب:
https://github.com/shadcn/improve
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4373" target="_blank">📅 15:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4372">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شنیدم گویا چند نفر دارن پنل‌های ایرانی تحت کلودفلر رو مدام گزارش میده به خود کلودفلر که احتمالا از دوستان VPN/VPSفروش هستن(همه‌شون این شکلی آدمای بدی نیستن طبیعتا. صرفا یه عده) و فکر کردن با این کار می‌تونن جلوی وی پی ان ساختن روی ورکر کلودفلر رو بگیرن. که…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4372" target="_blank">📅 14:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4371">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شنیدم گویا چند نفر دارن پنل‌های ایرانی تحت کلودفلر رو مدام گزارش میده به خود کلودفلر
که احتمالا از دوستان VPN/VPSفروش هستن(همه‌شون این شکلی آدمای بدی نیستن طبیعتا. صرفا یه عده) و فکر کردن با این کار می‌تونن جلوی وی پی ان ساختن روی ورکر کلودفلر رو بگیرن. که خب باید بگم نابینا مطالعه کردن
🥰</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4371" target="_blank">📅 14:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4367">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SZGZBgvQ-LZMPuf-_uMhWCjT2bUM6cAmqOvtza0-KBzWnJuNFsqwC0NAj1xB9MIcZQQ1L-JYyDc81-eY9P8KllIhbf86-yqTi8gHwLKE6kDVZP7AkPi07Bi138620jmZKoIIYDAFtTHgOjtUHOBHsnBV4CwAFURgnjENCllRq8Cz7c5SmW-6KsUOanjjAUrfUhhFKfVL-DFCwxu2zCukNxWHuSu21lGXKWOz5-3KIxkyeDCRh73oLwrmkQ5evCERIhXlL8M47ypkmMTDz1hOlx0rCfG5RGowgMB3S_hgxJAy7tscwcJ3pOVqDWfQey_WVHHyy1o1B1pCOT__7yZbgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gg0r4XltQtQ11TZqjnzgp-nzQBvvPtFW9Sy_7klSGha5o1mdT9Y8wXrRfL-DHzs96h9Qdzi7U54fVI4w32LAZm7kiryuxkRKAOopMtP8pi8TI1SxUKf4deuMzYx7U76qt0YhPKhtqFuh3Njbzzk90DH5ELAEicZy3XAQSJ040qjrF5HYJNFu2VWwP2LR0aEIxN0vgxzSc5wqYAZ4Ul3spS7v4tuZSwNJnTuXTA8IxWL5kpJQhcmKw02-XuQJyIAyaLJ08DXO6BZ5_-Da3d_uEXWKs2zZoykYj8XigEHuZ6IIlCUNKApq8j7_kCnjI7OKUZt2p45k7KY0FcabjP9i1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ExlO8vU_ECEo-nXblj7ve-5IACfcctEdrT9wizk_jOS7li_PCK6xK5qjRMaoDhhhlKSyLCKDNCqq27SvGyD9A2w_k6vmOaSjWj6oOwBa8QrmlQN2rqOoDd99SgRDP34QFx2Wr8FiFa2bqzlAzI3o2A5jMvZj2KwsocRs3sl7eSpg2yihZ65Gm3NtbMQwaYQCG2jlADjBRbTp91Flng9soaMIW3YSDApVL4RKDK9f9LdrsXHqQpZsvJa1uaVS7BA0k_6AOtlcKSfpmlGyX2HTJsOzhPZuxZPbebGmkF1jbJR9eEHP0CxjWw9WW3S3XjYMjJBhJ0OxsydhHhPxsp5kpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rTnVvl07Sh9n-GGuhZV2cHU4NpKMgfrSv-Lg5Fqxcn1DTe_MKvtGA0vNmReDrBOWZCc6yxzteOD7lH9LRyMNhz5Bcz3bgpdZpRNEagyn4Q_Coe-wuW2RQNQYn3JPLA1v82hbd9lxyK6ZfGrrfz7kUQlS67VM2rGdFjaCC-qATaMs56zc6Sg6gV2I_VSiFhddzI9ikgnKRsZAFtgg1GtjyQ0rBvpcGGy5uwzuozsHgNFnQxZsO1qX5_9jQ3ei69O5VIPb7nJ-xzSVO-00NAqo_hiBYb66u-QQhAKbRYn-URmITY1B3N5He5E8DSS-Caxp16-E35WohYgjj84fCkWysA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لینک زیر رو به هرمس بدید و بگید:
اینو نصب کن، فعال کن و بذار تو استارتاپ سیستم تا با روشن شدن سیستم اجرا بشه.
بعد از نصب یه محیط بسیار زیبا تحت وب در آدرس لوکال زیر برای شما فعال میکنه:
http://localhost:8787
https://github.com/nesquena/hermes-webui
✍️
بوکانت</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4367" target="_blank">📅 07:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4366">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فردا open design و claude design رو واستون یه مقایسه میکنم از اونجایی که روز آخر اشتراک کلاد 20 دلاریمه، آتیش بزنم به مال(توکن)ـم
ولی ویدئو فعلا ازش نمی‌گیرم. صرفا اینجا بهتون نشون میدم
چون هنوز به open design مسلط نیستم کامل
در عوض تمرکز می‌کنم روی ویدئوهای درس خوندن با ai و بالاتر بردن efficiency</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4366" target="_blank">📅 05:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4365">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/720362863c.mp4?token=p8NZE-T5_Z9EOCX_-QpNz0W5n3_5uwwzD946KEvkSWKSivsnY3Hpn4792TBxoR6kberTdyeSLH7HN1pyKcEol58ujsSInVeEmjbFbDN-MStcCpW31BKtRhDCBze6wICpG0ym8Cw4Y72YckrrTHYqx3OESIUjoWU-9hheAFIUmlDCu9ADM_P2dIxKWOiC_rMDzNa4btnLbVnZSvVLqgxOBNHkvUiqXubEw50ivXO2dLl_t2rAHaBwehm43nLRy4CXsjeUyAmDFYZAQakUEUEVrgQbYaqxQRFMX104maTQWji3hYMzRkqjqJ8SQfXwej8zUHvHxTBGPWpZgCtl9Bv7xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/720362863c.mp4?token=p8NZE-T5_Z9EOCX_-QpNz0W5n3_5uwwzD946KEvkSWKSivsnY3Hpn4792TBxoR6kberTdyeSLH7HN1pyKcEol58ujsSInVeEmjbFbDN-MStcCpW31BKtRhDCBze6wICpG0ym8Cw4Y72YckrrTHYqx3OESIUjoWU-9hheAFIUmlDCu9ADM_P2dIxKWOiC_rMDzNa4btnLbVnZSvVLqgxOBNHkvUiqXubEw50ivXO2dLl_t2rAHaBwehm43nLRy4CXsjeUyAmDFYZAQakUEUEVrgQbYaqxQRFMX104maTQWji3hYMzRkqjqJ8SQfXwej8zUHvHxTBGPWpZgCtl9Bv7xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی ردیت یه نفر یه پورتفولیوی کاری ساخته که رسما مرزهای فرانت‌اند رو جابه‌جا کرده
😂
طرف طبق گفته‌ی خودش، فقط به Claude Fable 5 یه دستور خیلی کوتاه داده(که البته من به شدت شک دارم):
"یه پورتفولیو می‌خوام که کاربر نخوندش، بلکه توش پرواز کنه!"
نتیجه این شد که کلاد صفر تا صد یه سایت سه‌بعدی رو ساخته که شما توش تو فضای بی‌کران اسکرول می‌کنید، سیاره‌ها و پروژه‌ها از کنارتون رد می‌شن، از تکسچرهای واقعی ناسا (NASA) استفاده شده، گرافیکش روی مرورگر کاملاً 60fps ران می‌شه، و در نهایت وقتی به آخر سایت می‌رسید... سفینه‌تون می‌خوره توی خورشید و منفجر می‌شه!
😂
این پروژه قدرت وحشتناک هوش مصنوعی توی ترکیب کتابخونه‌های پیچیده مثل Three.js با کدهای فرانت‌اند رو نشون می‌ده. که اگر بتونید AI رو توی مسیر درست هدایت کنید، خروجیش به شدت جالب می‌شه.
لینک سورس کدش تو گیت‌هاب (اگه می‌خواید خودتون تستش کنید):
🔗
https://github.com/AbhishekBadar/portfolio
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4365" target="_blank">📅 23:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4364">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">از بین سه تا پنل BPB و Edge و نهان که آموزش دادم، به شخصه برای خودم Edge سرویس‌های بیشتری رو باز می‌کنه بدون نیاز به proxy_ip. اون دوتا نیاز به proxy_ip دارن اکثر اوقات تا به درستی کار کنن یا نیاز به تعویض کلاینت یا dns معمولا. اما edge بهتر بوده تا الان حقیقتا.…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4364" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4363">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">از بین سه تا پنل BPB و Edge و نهان که آموزش دادم، به شخصه برای خودم Edge سرویس‌های بیشتری رو باز می‌کنه بدون نیاز به proxy_ip. اون دوتا نیاز به proxy_ip دارن اکثر اوقات تا به درستی کار کنن یا نیاز به تعویض کلاینت یا dns معمولا. اما edge بهتر بوده تا الان حقیقتا.
آموزش راه‌اندازیش روی
دسکتاپ
و
گوشی</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4363" target="_blank">📅 19:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4362">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub(Afshin Karimi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdRK9tPld0SONSRy2_ovRN0897fjDcf-3TSwHR-YZxEde9QjquFP1Pne1YfcW_yqDLdwGmOTm6-Ear34Gr2HS2PwN8KIAGgByCRto3JeQvGH7lEacdv5spwQelChw-HYy_GEcNCWF2X6WnncryygOpGDMYUlFU_zdxd0LPhfGt8tmuxs7kkPIUz3MoNzZD9UXj5zANih1Xq-5DC1lBmnOemmWk3wUYj2PykgApPN1Nrbrv6TYHUifXZPW9fa_hCipUGHoJG-C8Y1G5VeMOTa1o3T_cltOHtf_Vo3dvPaS2tRiPbEzNzVv980MeCvp1OFz8YB4ksPF0MiDYilGiZL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه GameShell یک بازی متن‌باز برای یادگیری دستورات لینوکس است که به‌جای آموزش‌های سنتی، مفاهیم را از طریق مراحل و مأموریت‌های تعاملی یاد می‌دهد.
اگر تازه می‌خواهید لینوکس را شروع کنید، این بازی می‌تواند راهی سرگرم‌کننده برای یادگیری دستورات پایه باشد.
https://github.com/phyver/GameShell
@RepoFa</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4362" target="_blank">📅 17:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4361">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">به نظرم اگر می‌خواید برنامه‌نویسی یاد بگیرید، بهتره که یک زبان، و از اون زبان یک حوزه رو در نظر بگیرید و شروع کنید به یادگیری.
برای مثال اگر بخواید پایتون یاد بگیرید و همزمان توی حوزه‌های AI و Back-End باهاش کار کنید، آخر سر به خودتون میاید می‌بینید هیچ کدومش رو درست و حسابی یاد نگرفتید.
و همیشه در همین حین، سه تا سؤال از خودتون بپرسید.
1- چی دارم یاد میگیرم؟(روشن شدن مسیر)
2- برای چی دارم یاد میگیرم؟(روشن شدن هدف)
3- قراره باهاش چی بسازم؟(تبدیل به انگیزه میشه و دل‌زده نمی‌شید)
این پروسه‌ایه که من خودم طی میکنم برای هر زبان-فیلد جدیدی که می‌خوام یاد بگیرم. کاملا هم نظر شخصیه و چیز ثابت شده یا علمی‌ای پشتش نیست لزوما</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4361" target="_blank">📅 16:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4360">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اگه با ایجنت‌های کدنویسی کار کرده باشید، می‌دونید که بزرگ‌ترین مشکلشون Over-engineering کردنه. یعنی مثلاً برای یه تقویم ساده که با یه تگ HTML حل می‌شه، میرن یه کامپوننت ۴۰۰ خطی با نصب کلی پکیج اضافه می‌نویسن
😳
ابزار Ponytail (که الان به شدت تو کامیونیتی وایرال…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4360" target="_blank">📅 15:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4359">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SXWemSTOAymy_ohM6uUYoiGFsYhvlDs-sTw1zV3a-YkjF2f3d9scg7gDjV4xIQfLazvAf_pwrXh2gqMCMMTCVi7dP2hftwLlW0dqx_n9BHGGVOQik3HtUOJWBVUzbu72oIQfeZ4ZF1PTsWbaI5ut3lCCyo4GdLIIgA_rXJlhvBdM9GV6A_bzVKQbwyiFGpxfFnaYwxr0Poo79Ea3PreoOz52f5vZ7SXJpTXHwdQFPgnYQfD1jTS98CFRw5eC5abhEnNVN5SVZfWeQOqmWKmjiMqtFPjpZxW8xKlG90Lx0siyu7MiT8hgpPVaxaPcsC4VvrMLFDjdwOxzJNKIuer2Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه با ایجنت‌های کدنویسی کار کرده باشید، می‌دونید که بزرگ‌ترین مشکلشون Over-engineering کردنه. یعنی مثلاً برای یه تقویم ساده که با یه تگ HTML حل می‌شه، میرن یه کامپوننت ۴۰۰ خطی با نصب کلی پکیج اضافه می‌نویسن
😳
ابزار
Ponytail
(که الان به شدت تو کامیونیتی وایرال شده) دقیقاً یه پلاگین برای حل همین مشکله. این ابزار باعث می‌شه ایجنتتون مثل همون برنامه‌نویس‌های سینیورِ تنبل شرکت که حوصله‌ی کدِ اضافه نوشتن ندارن، رفتار کنه
🙄
شعار این ابزار اینه:
«هیچی نمی‌گه. فقط یه خط کد می‌نویسه. همونم کار می‌کنه.»
چطور کار می‌کنه؟
قبل از اینکه ایجنت حتی یک خط کد بنویسه، مجبورش می‌کنه این نردبان رو تو ذهنش طی کنه:
- اصلاً این فیچر نیازه؟ (قانون YAGNI) اگه نه، بی‌خیالش شو.
- آیا توی کدهای فعلی پروژه قبلاً نوشته شده؟ اگه آره، همون رو ری‌یوز کن.
- کتابخونه‌های استاندارد خود زبان می‌تونن حلش کنن؟
- آیا مرورگر یا سیستم‌عامل خودش اینو داره؟ (مثل استفاده از
<input type="date">
به جای نصب پکیج).
- آیا پکیجی که از قبل تو پروژه نصبه این کارو می‌کنه؟
- می‌شه توی یه خط نوشتش؟
- فقط در نهایت: حداقل کد ممکن رو بنویس.
طبق بنچمارک‌ها، این ابزار حجم کدها رو ۵۴ تا ۹۴ درصد و مصرف توکن‌ها رو ۲۷٪ کاهش می‌ده. البته اینم بگم که تو مباحث امنیتی و Validate کردن اصلاً تنبلی نمی‌کنه و امنیتش ۱۰۰ درصده
❌
آموزش نصب روی ابزارهای مختلف:
توی Claude Code
کافیه دو تا دستور زیر رو جداگانه توی پرامپت بنویسید:
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
توی هرمس (Hermes Agent)
hermes plugins install DietrichGebert/ponytail --enable
بعد از نصب می‌تونید با دستوراتی مثل /ponytail یا /ponytail-review کنترلش کنید.
توی Cursor، Cline و دیگر
ide ها
نیازی به پلاگین نیست. کافیه فایل رول‌ها (مثل .cursor/rules/
ponytail.md
) رو از گیت‌هابش دانلود کنید و بندازید توی پوشه‌ی پروژه‌تون.
توی GitHub Copilot CLI
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
توی Gemini CLI (Antigravity)
agy plugin install
https://github.com/DietrichGebert/ponytail
لینک ابزار:
https://ponytail.dev/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4359" target="_blank">📅 14:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4358">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">هوش مصنوعی به جای یک فایل، کل درایو C رو پاک کرد!
😐
چند روز پیش توی گروه جامعه وایب کدینگ ایران، افشین یه تجربه عجیب رو منتشر کرد.  داستان از این قرار بود که با Z.ai و مدل GLM 5.1 یا GLM 5.2 از AI خواسته فقط یه فایل رو حذف کنه، اما ظاهرا به جای اون، کل درایو…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4358" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4357">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه وایب کدینگ ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvCqpiQvBM3e1Gy7BNJo7ReowTkYD4s-dD_gBL99vClT9Pe5OXCR12A4nvxaNDfgOmLXkV-d5AOuijToQ6w52mI3n0U2NWBPE4YG2FXUQpUBHTbpV9LzASpgvx4bBYmhbiriI6vwFmW0hAEniyshk_AUXO9yGuxd5CUZeIH_yZWOoM5ksKT1L5zy6Aw4BrUHpeJjsQVuK6Bvx83CmpqZFteqQF8nv_R2UdPAeH4JPx8hKx9X88vkZGqUoCd7156D40fHvGgAGsN7XsUgmwJIG_GfT1SE2e19kp68d28ibGuTi-uC3dQroyv7o557XHr9BJhXYUCRfxtNmVxz8b1FIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی به جای یک فایل، کل درایو C رو پاک کرد!
😐
چند روز پیش توی گروه جامعه وایب کدینگ ایران، افشین یه تجربه عجیب رو منتشر کرد.
داستان از این قرار بود که با
Z.ai
و مدل GLM 5.1 یا GLM 5.2 از AI خواسته فقط یه فایل رو حذف کنه، اما ظاهرا به جای اون، کل درایو C ویندوز پاک شده!
این اتفاق یه یادآوری مهمه.
هرچقدر هم Agentهای هوش مصنوعی باحال و قدرتمند باشن، وقتی به ترمینال، فایل های سیستم یا دیتابیس دسترسی کامل داشته باشن، یه اشتباه کوچیک می تونه به یه فاجعه تبدیل بشه.
اتفاقا متین سنپای هم امروز ابزار Kastra رو معرفی کرده که دقیقا برای همین سناریو ساخته شده. این ابزار بین Agent و سیستم قرار می گیره و برای کارهای حساس مثل حذف فایل یا تغییر دیتابیس، اول از خودت تایید می گیره تا AI نتونه هر کاری خواست انجام بده.
به نظرم تا چند وقت دیگه استفاده از ابزارهایی مثل Kastra دیگه یه قابلیت اضافه نیست، بلکه برای هر کسی که با Agentهای کدنویسی کار می کنه، واجبه.
تا حالا Agentها چه خرابکاری هایی براتون انجام دادن؟
😅</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4357" target="_blank">📅 12:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4356">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EiF4yiYvw_cGDGGu7MrtXISZaN6nyhMyiXl463ryGiGBNXS6sP-6iTx0q4_hH4RXvj2rdvG3tTjMsPLn7GbkoSll7bk6B04eCKQh5V2IJVlUQ0Tcp-jnLEMA3LmN3Zz6aZ4ZxCn61W4BDDcRIz7vGLJNZLh0ZOlfN9VzfqEBX-LYXHpU4VlmdV1QBnHJhLBe57L7qD9hvGEs6myXEQscP8tvRMROyvZWf5FZu5kEcTDF64JkvLFP027p80qL8oXuht78E2TC22MU4v_htwEjJFnfDOol9fl4l6ZKTto2-pN9YLNYsUd1j3Q1f4uCqgn-XfYav-zV0RQjthBHfSgX6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار Kastra برای کنترل ایجنت‌های کدنویسی
اگه با ایجنت‌هایی مثل کلاد یا هرمس(روی Yolo) و یا هر ایجنت دیگه‌ای روی کدهای حساس کار می‌کنید، استفاده از سیستم‌های نظارتی دیگه یه آپشن نیست صرفا به نظرم، بلکه واجبه!
توی Hacker News یه ابزار خیلی خفن و کاربردی به اسم Kastra معرفی شده که کارش اینه که به عنوان یه «لایه‌ی دسترسی و تایید» (Authorization Layer) برای هوش مصنوعی عمل می‌کنه. یعنی دقیقا روی فراخوانی toolها توسط ایجنت‌هایی مثل Cursor و Claude Code نظارت می‌کنه تا اونا سر خود کاری نکنن.
چرا اصلاً به Kastra نیاز داریم؟
ایده‌ی ساخت این ابزار زمانی به ذهن تیم سازنده‌ش رسید که ایجنت خودشون نزدیک بود یه دیتابیس پروداکشن رو به کل پاک کنه! وقتی به مدل‌ها دسترسی کامل (مثل کار با ترمینال یا دیتابیس) می‌دید، هر لحظه ممکنه توهم (Hallucination) بزنن یا اشتباه کنن. Kastra اینجاست تا جلوی فاجعه رو بگیره.
ویژگی‌های اصلی:
- پشتیبانی کامل با mcp: تو کمتر از ۲ دقیقه می‌تونید با Cursor، Claude Code و پروتکل‌های MCP وصلش کنید.
- گاردریل‌های امنیتی: می‌تونید براش قانون بذارید که ایجنت برای کارهای خطرناک (مثل پاک کردن یا تغییر دیتابیس) اول از شما اجازه بگیره.
- مدیریت دسترسی: مشخص می‌کنید که ایجنت شما دقیقا به چه ابزارها و چه بخش‌هایی از سیستم دسترسی داشته باشه.
لینک ابزار:
https://kastra.ai/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4356" target="_blank">📅 10:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4355">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/885f71c1ea.mp4?token=OvfJf1S5K5viFyJe9qJm4KfEzWR8fxedeL-MH4b3SMam7mSdC1bpnctnDOwCBYvD0vLeUAZek1ZVyQu2dtDlZ0n7xStcypYbvvX6WjyAvBwGvL54qAr53JIS5t6L_FtYQfijwjSN48y1-JNWricUIxhFsPZ3-EPP66e8rT3CZC74kddJvfnKJnEnHfi8hv8awoxS4viZ13VwKM3AlKMyQUkbSsBLF55AFATDEjDNvbSZ_Yq4VeFfHEQvCevtaFclWRPePqB07z2WBUrGfhMyNfUWioSIMf5uLheiaaXmhM4litZsr-Zfwcg3hXtFlqsk4LdUw8gObqFH1P5ohw-NnA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/885f71c1ea.mp4?token=OvfJf1S5K5viFyJe9qJm4KfEzWR8fxedeL-MH4b3SMam7mSdC1bpnctnDOwCBYvD0vLeUAZek1ZVyQu2dtDlZ0n7xStcypYbvvX6WjyAvBwGvL54qAr53JIS5t6L_FtYQfijwjSN48y1-JNWricUIxhFsPZ3-EPP66e8rT3CZC74kddJvfnKJnEnHfi8hv8awoxS4viZ13VwKM3AlKMyQUkbSsBLF55AFATDEjDNvbSZ_Yq4VeFfHEQvCevtaFclWRPePqB07z2WBUrGfhMyNfUWioSIMf5uLheiaaXmhM4litZsr-Zfwcg3hXtFlqsk4LdUw8gObqFH1P5ohw-NnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در کنار معرفی GPT-5.6، OpenAI یه کار جالب کرد و ChatGPT Work رو معرفی کرد. که به عنوان یه ایجنت می‌تونه کارهای طولانی رو روی فایل‌ها و اپلیکیشن‌ها انجام بده و ساعت‌ها روی یه پروژه متمرکز بمونه. به نظرم کم کم شبیه به هرمس، تمام ورک‌فلو‌ها و لوپ‌های پیچیده دارن…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4355" target="_blank">📅 06:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4354">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">در کنار معرفی GPT-5.6، OpenAI یه کار جالب کرد و ChatGPT Work رو معرفی کرد. که به عنوان یه ایجنت می‌تونه کارهای طولانی رو روی فایل‌ها و اپلیکیشن‌ها انجام بده و ساعت‌ها روی یه پروژه متمرکز بمونه.
به نظرم کم کم شبیه به هرمس، تمام ورک‌فلو‌ها و لوپ‌های پیچیده دارن تبدیل به زبان طبیعی می‌شن.
شما می‌خواید، و انجام می‌شه
هرچند هنوز، مهندسی اینها، و نظارت روی کدی که AI می‌زنه، خیلی مهمه به نظرم.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4354" target="_blank">📅 05:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4353">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/802171ad75.mp4?token=QBz59PBwDQps-uWkZ7AUVRww8CRVTlRCFKJBG_3yPJI3b2XJGgHDvVt_wdsjWW_uI7sdnPKiBxMYJclpRe97SZMmCXqD_sxZo3hOs1Sbft3a2_UeWT4gKts9GCH7dOQ9z8liyPh8-zXEAzKXX_0C4ANes0EQwKrqeHF_IBdP7ojoqNVryyXLO3thZhWGWR3dZEF-2YFGLEV5ZLvW99fA3GNA_ijE9pfjbmS5563YsMkbPHurRWZZoaAUzltn_EvmbnvTRWtJ_FBpZR6ya8fPVnAgket4o_Sswv9eDeWEjFcaOVGOgCKZrvsx3RfJCWrr3cf3Nku70bcL0YxzN_JTSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/802171ad75.mp4?token=QBz59PBwDQps-uWkZ7AUVRww8CRVTlRCFKJBG_3yPJI3b2XJGgHDvVt_wdsjWW_uI7sdnPKiBxMYJclpRe97SZMmCXqD_sxZo3hOs1Sbft3a2_UeWT4gKts9GCH7dOQ9z8liyPh8-zXEAzKXX_0C4ANes0EQwKrqeHF_IBdP7ojoqNVryyXLO3thZhWGWR3dZEF-2YFGLEV5ZLvW99fA3GNA_ijE9pfjbmS5563YsMkbPHurRWZZoaAUzltn_EvmbnvTRWtJ_FBpZR6ya8fPVnAgket4o_Sswv9eDeWEjFcaOVGOgCKZrvsx3RfJCWrr3cf3Nku70bcL0YxzN_JTSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
درود به همه رفقا...
اگر کانفیگ میزنید و فرگمنت روی ip ها کار نمیکنه واستون بهتره که از دامنه برای ip تمیز استفاده کنید...
برای مثال بهترینش:
Chatgpt.com
Grok.com
با این مقدار فرگمنت:
Packets: 1-3
Interval: 1-1
Length: 1-7
اگر کلاینت Fakehost داشت:
Google.com
رفقایی که ابتدایی تر هستن داخل ویدیو کوتاه نشون دادم داخل هر مدل گوشی یا کلاینت که کانفیگ میزنید هست
✅
💡
نکته:اگر کندی در کانفیگ یا آپلود ندارید روشن کنید fragment رو عزیزان.
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4353" target="_blank">📅 01:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4352">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به شخصه پلن کلادمو ReSubscribe نمیکنم؛ تا ببینم وضعیت قطعی نت چی میشه به شما هم توصیه می‌کنم اگر تموم شده و کارتون زیاد لنگ نیست، نخرید فعلا..</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4352" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4351">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88560d1079.webm?token=slStrjLuWJAXu0fXBKw3-KCfgQV1YsBYlNQRSmfd-m98Std7n3eg4L94bkQSgPm4D8oniQjdja7z5TT29c1JitKNIfVk2E6hZXQpP3hAZDRKpwkQi1zIDRnjQQhZcc5OHnUoRzyGBsfUcWXjWHNlo1KU6NsPxy4HTD0Rf5HPWzdxvFyojBmWlL6B-YKLsj4EcVQ_ehMOBQM0Gbgm24e-NBQDd94I8TtJCOQ3cLE30JUGyA_6X0GbFgma9ivxDqSf0lJCf8X8aARNMTtwr2uQ2v7uDleE-b6URF_u4dOI9HNGdLIO8SX-J5MuoEkTzNg07bAItH56pCikP9PPImGlow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88560d1079.webm?token=slStrjLuWJAXu0fXBKw3-KCfgQV1YsBYlNQRSmfd-m98Std7n3eg4L94bkQSgPm4D8oniQjdja7z5TT29c1JitKNIfVk2E6hZXQpP3hAZDRKpwkQi1zIDRnjQQhZcc5OHnUoRzyGBsfUcWXjWHNlo1KU6NsPxy4HTD0Rf5HPWzdxvFyojBmWlL6B-YKLsj4EcVQ_ehMOBQM0Gbgm24e-NBQDd94I8TtJCOQ3cLE30JUGyA_6X0GbFgma9ivxDqSf0lJCf8X8aARNMTtwr2uQ2v7uDleE-b6URF_u4dOI9HNGdLIO8SX-J5MuoEkTzNg07bAItH56pCikP9PPImGlow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4351" target="_blank">📅 00:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4350">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">به شخصه پلن کلادمو ReSubscribe نمیکنم؛ تا ببینم وضعیت قطعی نت چی میشه
به شما هم توصیه می‌کنم اگر تموم شده و کارتون زیاد لنگ نیست، نخرید فعلا..</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4350" target="_blank">📅 00:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4349">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یکی گروک مدل grok 4.5 رو داده بیرون، یکی هم متا مدل جدید داده بیرون به اسم Muse Spark 1.1 هر دو هم ادعا کردن که هم سطح Opus 4.8 هستن با هزینه کمتر، ولی به نظرم متا دروغ میگه
😂</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4349" target="_blank">📅 23:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4348">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mw9yICIpgxLBnakGW_3pRQbEkOmz39QbA6SqDR9cW3D-HnhCSJleN3Q3phWj4sMAe7KeWRHVeGuO9Q7GXCoCpiPY6gwQMr6qz7yMSCpdBA1fwtUJ6AJhm7dOSMR-adjOU5rTAIgzvFawEv1GFB3GJgIWKS6PKUu8MvZMraYXOBLVFtUO4hy0PMzy2dZXI53vMd8gC-iznUjQ4cEXVW1SRZlZ-R5c54w3H63cn4NxmdKZ6r2qsvg8faVRGNkB48BT-l7wMJgMnRpvYZGe4ZS-uAle85rVcelIPgMU4ue8tEC4P9uDcxJdvNiY3KTzcp1tqxIn-YRclULWEpq3kAMboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر درست باشه فوق‌العادست
بچه‌های توییتر تست کردن Grok چهار و نیم رو، همه تعریف تمجید کردن</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4348" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4347">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یکی گروک مدل grok 4.5 رو داده بیرون،
یکی هم متا مدل جدید داده بیرون به اسم Muse Spark 1.1
هر دو هم ادعا کردن که هم سطح Opus 4.8 هستن با هزینه کمتر، ولی به نظرم متا دروغ میگه
😂</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4347" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4346">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اتهام جاسوسی به Claude Code؛ چین درباره ابزار برنامه‌نویسی آنتروپیک هشدار داد</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4346" target="_blank">📅 21:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4345">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یه کاری کردن انگار شرطی شدیم
تا نتمونو قطع نکنن باور نمی‌کنیم جنگ شده</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4345" target="_blank">📅 21:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4344">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Aro_g0ip--TpVySxu_U1f-tkXaWtf3G7oanpAP6Yzz8kbL849FDWyFiV-5wYUGGPRzXX3taxzRUtcFU4bvMdMqtbqiTSlED-B_y8qQ0722U9k6jCVK49gVv2sL3QkD2LHwejyg6yxmv7uQSRDYOO3KBXZ4tDdY49M1NiS331KFkKmXrYJffeLhVGjf5OPQ0SwnU6brycPn6puezQY6ACZ2tsn9bmf4Zu5JIskBo1_DhHT-U3p6c9iUoG7enXaRtwREkwxHX7Rs1jrlI2cDNjysjROpXa903gCOu53hSFuZ4GyJzQLoLXIuTKn1cMXwTXNWul8wbgncaRfw01p-vlxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند کانال WhiteDNS
👉
@WhiteDnsChatBot
✅
جواب سریع |
✅
۲۴ ساعته |
✅
رایگان
نحوه استفاده:
۱. روی لینک بزنید
۲. Start
۳. سوالتان را بنویسید
مثال: چطور فیلترشکن نصب کنم؟
/search عبارت — جستجوی مستقیم
/contact — ارتباط با ادمین
⚠️
ربات WhiteDNS در چه زمینه‌هایی جواب می‌دهد:
✅
فیلترشکن و VPN
✅
DNS و تنظیمات اینترنت
✅
آموزش نصب اپلیکیشن‌های WhiteDNS
✅
رفع مشکلات اتصال
✅
Warp و Cloudflare
✅
تنظیمات اندروید، آیفون، ویندوز، مک
✅
سوالات مربوط به قطعی اینترنت
❌
ربات قادر به پاسخ‌گویی به سوالات غیرمرتبط با موضوعات کانال نیست.
💡
نکته: اگر جواب دقیق نگرفتید، سوالتان را طور دیگری بنویسید یا از دکمه جستجو استفاده کنید.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4344" target="_blank">📅 20:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4343">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">ترجیحا هیچ VPNای نخرید دوستان. هیچ تضمینی نیست که اگر اینترنت قطع بشه هم اونا وصل بمونن یا نه. مثل اوایل جنگ که خیلیا اسکم شدن
همون هزینه رو بذارید whitedns راه بندازید</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4343" target="_blank">📅 16:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4342">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1d99494e2.mp4?token=CUSEGqhXd9RXEeuKVgWUU8QiwV03WxSRYw6CStJv0haW8pfBMOTgH_Ckh9CKrhZo9PZHRiuKeH3KQ05-lfiWXf7C1upjJgG6YXkIJKWh450rL0XZABI39PvwBjxCMnrk90MoD1WiEgUwZNdoAC6sQoaK58fD6B2DhLcRK2_1Y3GSxR0avVpRen_GY_Gakex-pHixOTRlHeXINofpngjr5nesVdH4fSbu1dB3vxFcgCD6vzPX0WA3hE0Z4etKiwzE8J2ZtZQycFiH2X_iIRQL7Ge2B8S4FY1JaqHqQqbiXWShu9nyxegV7vGFH9bHtpqo5ddRSqsT6RKzqUnRJc8zzA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1d99494e2.mp4?token=CUSEGqhXd9RXEeuKVgWUU8QiwV03WxSRYw6CStJv0haW8pfBMOTgH_Ckh9CKrhZo9PZHRiuKeH3KQ05-lfiWXf7C1upjJgG6YXkIJKWh450rL0XZABI39PvwBjxCMnrk90MoD1WiEgUwZNdoAC6sQoaK58fD6B2DhLcRK2_1Y3GSxR0avVpRen_GY_Gakex-pHixOTRlHeXINofpngjr5nesVdH4fSbu1dB3vxFcgCD6vzPX0WA3hE0Z4etKiwzE8J2ZtZQycFiH2X_iIRQL7Ge2B8S4FY1JaqHqQqbiXWShu9nyxegV7vGFH9bHtpqo5ddRSqsT6RKzqUnRJc8zzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مقدار زود شروع شد</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4342" target="_blank">📅 16:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4341">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/annLS9FK3AhA4pA8tDVXZ-hFURzhvsCSbVN12vIawXZGvlu9bM-XDINW2U2axYYZhz_wuVwDkHSqCYLlPEcJp7s16Vl-Vrc2v3QbUl6IysiJ144gLO3HF7bCsEFwFyK6SiSG1NbuCTPyAgl4n1Ys8zOSgqTB9Dt-fT5yhkU1vbb-QFk6Ef7doef5FVttP7vW9ijhNUxXCt-w_aSglvhOfTWgpXkBCz7WxJhCAbQoKM7j7HiDyD01B5GBksqqE7TftCC32_K2o7rd9bzn1B7DR1iIcAOD8jEh4dOkFP2NYkesUI8ykxjBMY8iZOzMWT3y-b1DXLq8jDA7eBCttLtLnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارادوکس عجیبیه. از یه طرف انگار جدی جدی جنگ شده باز
از یه طرف اینور دارم آموزش می‌بینم و کار می‌کنم با ai
و نمیدونم همین آب باریکه‌ی نت کی قطع میشه دوباره</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4341" target="_blank">📅 15:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4340">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">احتمالاً من دچار "فرسودگی LLM" (LLM Burnout) شدم!
نویسنده‌ی این مقاله (الک سکولن) یه توسعه‌دهنده‌ست که می‌گه مصرفش از هوش مصنوعی در حد استانداردهای الان کاملا معمولیه، اما اخیراً یه حس خیلی عجیبی بهش دست داده:
خستگی مفرط از خوندن متن‌های تولید شده توسط هوش مصنوعی!
روند کارش این‌طوری شده که دیگه خودش از صفر کد نمی‌نویسه؛ طراحی می‌کنه، طراحیش رو به Claude یا Codex می‌ده، کدهای اونا رو می‌خونه و ریویو می‌کنه. علاوه بر این، روی پروژه‌ای کار می‌کنه که کدهای تولید شده توسط Qwen رو باید مداوم بررسی کنه. یعنی عملاً کل روزش با خوندن خروجی‌های AI می‌گذره. حتی برای سرچ‌های روزمره‌ش هم از ChatGPT و Gemini استفاده می‌کنه.
حالا مشکل کجاست؟
اعتراف می‌کنه که با این ابزارها خیلی بهره‌ورتر شده و قصد نداره کنارشون بذاره، اما تو چند ماه اخیر، یه بخش کوچیکی از وجودش از دیدن خروجیِ مدل‌ها وحشت داره! چرا؟ چون دقیقاً می‌دونه قراره چی ببینه:
فرضیات غلط، توهمات (Hallucinations)، جملات بریده‌بریده‌ی اغراق‌آمیز، و
✨
استفاده‌ی بیش‌از‌حد از ایموجی‌ها
🚀
.
نکته‌ی جالب اینجاست که می‌گه انسان‌ها هم اشتباه می‌کنن و می‌تونن رو اعصاب باشن، اما مشکلِ اصلی با هوش مصنوعی
تکراری بودنشه
. مدل‌های زبانی دقیقاً با یک لحنِ واحد می‌نویسن و دقیقاً یک‌جور اشتباه می‌کنن. سر و کله زدن با یک سبکِ کاملا یکسان و اشتباهات تکراری، اونم به صورت هر روزه، کلا فرسوده‌ش کرده.
این دقیقاً نشون می‌ده که با وجود تمام شخصی‌سازی‌ها (Personalization) و پرامپت‌ها، هنوز هم اون امضای پنهان و سبک خاصِ هوش مصنوعی از زیر دستمون در میره و وقتی تو طولانی‌مدت باهاش درگیر بشید، می‌تونه حسابی روی مختون بره!
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4340" target="_blank">📅 14:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4338">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VhSiXerdJobbLpjId5ByOmTs9W887hdjl716yvpeOP1rlJQC1_kP0JvRETuGNTc_mBA3ipjf5Im0I6JiFLuSygS0Zx6HrmZRgsiAbLpQBk1T24HEV5m-St-XNLaGAHQJK3qdREzWEBVK3gAfauJm9bB91DRKSfy9--7scCBfDQV7Fdcsd5BMFb-mEyk3Mo-voHm0BHnoo8ZkbrD6ewxPm9Fo79uRc_Svfw7aQ5anyrSFP8UYLZsk575apYz4A5I_yl__A8sWf2OS2sW5sXk25iwwhjrQPfG4RM_tPq-EuqWeX-wVONizW5f2PAbd6CB19ooTngseorcoRN-4dORcmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VJUvakObEWiy58ojD5cQpGlc3bJj_0ckSSksbMRhb41hhA4mVNGu3xh24Wg6eVEVcNo3EvUoqF1xb4ojM9VVri7FF8Hvc5CMUQifviCYYxDoG48bT2eZbGhJGkSvUnKPNIvX7QSdCVOsVUCqLRpwlCI7OHS7gTkh5kcKmIelAVqg-qbs6nhAZlKp7uiLWqONTyXJpz6pmUL12rJyY63fZ-KnDG-vJ9mIHGBCqBIELqqMRwkVHJbEH2WdYK8zlmcViqVP5To-XybEcoBd3SArgpx-mOnpEenVI0bPOarKTv-BsNf9fQ6bvK-4SNmsdOn8n_wewDWetby7bdkUVjmryQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
100 میلیون توکن رایگان برای تست مدل‌های جدید AI  مدل‌های زیر را می‌توانید با OpenAI Compatible API استفاده کنید:  • Kimi K2.6 • MiniMax M2.7 • GLM 5.2 FP8  بدون ثبت‌نام، وارد صفحه زیر شوید و از بخش Your API Key کلید خودتان را دریافت کنید:  https://infer…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4338" target="_blank">📅 13:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4337">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/784bc3dcd7.mp4?token=UsopOkxA38dh2146JQswf2Gz2PLmdOplUYmjQ8xT33GBni5SL1VcIoiKm4chVB2CANKSYjprEZXscWtmfwfaN_WTpa8-3UT-qjqyG-HNKPmFuhxQWg3MFMdtgdjUDDndk949olASkl9Tn1l9y18V3V68_T2dqhdIj-TnVC6ZVFXL0o3M1bn6gi5DrZm8OY8dtnuwCFg7TlwS1pQ9sq4ko4jBfKp4Jw9_QjIPorMKEXZt_jbUUIpsQiePOntLADJ1Asv1IANlMezS9PttEnOY4knJIy7YqL4GxuvYnaRYH1re4TihwfRRU_pz5HMtvGRc5TVk_xco1GsAZIFTAlSj5S2vG--D5Yx-IqQzsUEScBpSE2IJ91ObbriDL3AnwXjCJETKlROMTUVE161DYpp8I-IbwCF5Gs7qq-Kho2GM4QSX3GA2g_OhYmLDC8yl1uSe8f_TuKGcniaSYVNvBwj5CGCcQ-CgYdFSqJIkDoiyDT7gwUmgJ3fj3ds1HRn0dszx_fJ94PFW8BJFfbEriKNjAnxpwS6joGWqUfXxiPWFl-GGAhz8qLZd0nwCKJzUyejQSuVTZ085PFwMbU4RhBYpM9NHWXlM23bGIqL8fnwi7rlgR1echSUmfm2R7pZTaoLmFHCMYTMuIVdEedr6CKHAyjIgTz7fRGE5uNYaStNL-JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/784bc3dcd7.mp4?token=UsopOkxA38dh2146JQswf2Gz2PLmdOplUYmjQ8xT33GBni5SL1VcIoiKm4chVB2CANKSYjprEZXscWtmfwfaN_WTpa8-3UT-qjqyG-HNKPmFuhxQWg3MFMdtgdjUDDndk949olASkl9Tn1l9y18V3V68_T2dqhdIj-TnVC6ZVFXL0o3M1bn6gi5DrZm8OY8dtnuwCFg7TlwS1pQ9sq4ko4jBfKp4Jw9_QjIPorMKEXZt_jbUUIpsQiePOntLADJ1Asv1IANlMezS9PttEnOY4knJIy7YqL4GxuvYnaRYH1re4TihwfRRU_pz5HMtvGRc5TVk_xco1GsAZIFTAlSj5S2vG--D5Yx-IqQzsUEScBpSE2IJ91ObbriDL3AnwXjCJETKlROMTUVE161DYpp8I-IbwCF5Gs7qq-Kho2GM4QSX3GA2g_OhYmLDC8yl1uSe8f_TuKGcniaSYVNvBwj5CGCcQ-CgYdFSqJIkDoiyDT7gwUmgJ3fj3ds1HRn0dszx_fJ94PFW8BJFfbEriKNjAnxpwS6joGWqUfXxiPWFl-GGAhz8qLZd0nwCKJzUyejQSuVTZ085PFwMbU4RhBYpM9NHWXlM23bGIqL8fnwi7rlgR1echSUmfm2R7pZTaoLmFHCMYTMuIVdEedr6CKHAyjIgTz7fRGE5uNYaStNL-JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های جالب Amir Hormati مهندس ارشد و پرینسیپال در گوگل در حوزه AI در مورد کدنویسی و Hard Skill ها، اینکه آینده از دید خودش چیه، چه اتفاقی بر سر کدنویسی میاد و به عنوان مهندس نرم افزار روی چه مسائلی تمرکز کنیم، جالب اینکه خود امیر از رول مدیریت به نرم افزار برگشته به خاطر همین!
✍️
Max Shahdoost</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4337" target="_blank">📅 13:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4336">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رفقا مجددا می‌گم، که کلا این سایت‌هایی که یهو کلی توکن رایگان میدن، امن به نظر نمی‌رسن مراقب پروژه و .env هاتون باشید</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4336" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4335">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رفقا مجددا می‌گم، که کلا این سایت‌هایی که یهو کلی توکن رایگان میدن، امن به نظر نمی‌رسن
مراقب پروژه و .env هاتون باشید</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4335" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4334">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه وایب کدینگ ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P56F64hwz2sBHQ7fw2YCuUMhgBsv1YyhiGMgsJonvWMKSeyMFQZR4UhAMRxmOQoD3VmNsIX6gSRk2PHhMaCtJQxKQ0759q1Ykh6V-yBS6Y-V-GJNiPRCov3lQpCmsznhePg7vM-t5tXPYTRaVpaTBwE07e3gRCLyM7d59pm4h3cnImkU8iJ2C0ryWQ7jcd1aOUnqywAaThqjO8SIFCtxpYu4VdQcQt2Y9k38gl9QSk9MnZIpFwO_kzD8_H0yLEWogWLsM3vITNzAHE2ljCppGpDUzJw70a1sT-SCG7Srnuao9F27e0ay_zHxuOw9NkQkOWVjUqIEBgzrFw_644emzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
100 میلیون توکن رایگان برای تست مدل‌های جدید AI
مدل‌های زیر را می‌توانید با OpenAI Compatible API استفاده کنید:
• Kimi K2.6
• MiniMax M2.7
• GLM 5.2 FP8
بدون ثبت‌نام، وارد صفحه زیر شوید و از بخش Your API Key کلید خودتان را دریافت کنید:
https://inference.dahl.global/chatKeys
💡
اگر کوکی مرورگر را پاک کنید، می‌توانید دوباره یک API Key جدید بگیرید.</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4334" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4333">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p9TOf4UCYc_ilml7iS3uGYvJZnbh6_GWJ-WGDXVE_URuFnjAy2eir64iOsrOVWHd10ft8309IGsH2Xx3Wj2n-lAm08qyreo0-ok_KIJw3QA3nzqSnaIZbVnSRpoRuobyYWm8MISgwWIHxQ534izng34ZgdDDR5SzeQtTiiXilfG2MwQB6a3-qZAhPZ_WKtGpOffNDlXbeDSK1ho_DuR61R18uQ-YzR0ZwCYbUqH66hEWe57wt5X6EGlt9IgKvFbnzyCfCbrXVPtOp-omm3v1--R5IfLIn3J3ZMV0dpBZ3XvHRywhNY8XNX6pC_lagpBmanW4HWM60pkPsxRlSDijrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزی نیست، کامیونیتی Rust هستن
😂
😂
زبان Rust برخلاف go و پایتون و... از Garbage collector برخوردار نیست.
نفر اول گفته انقدر سینتکس افتضاحه که دلم می‌خواد زبان rust رو بندازم توی آشغالا(garbage) و نفر دوم ریپلای زده که اگه بندازیش توی آشغالا کسی نیست جمعش کنه چون این زبان آشغال جمع‌کن(garbage collector) نداره</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4333" target="_blank">📅 12:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4332">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اگر می‌خواید اکانت Claude بخرید، بهتره بدونید علت بن کردن‌های کلاد distillation attack هایی هست که اخیرا بهش شده؛ و حتی کاربرهای خارجی هم یهو اکانتاشون بن شده. بهتون دوتا توصیه می‌کنم.
1- به هیچ وجه از سایت‌های ایرانی نخرید. و حتما بدید دوستی، آشنایی، چیزی بگیره از خارج کشور. اگر ندارید، برید سراغ توصیه‌ی دوم. احتمال بن شدن داره به هر حال و ریسکش پای خودتونه. من خودم به شخصه هنوز بن نشدم(نمیدونم شانسه، یا چون دوستم از خارج از کشور واسم گرفت)
2- اشتراک Codex بگیرید در عوض و یا نهایتا اگر کار خیلی واجب دارید و می‌خواید حتما کلاد باشه، cursor بگیرید اما کرسر خیلی زود تموم میشه طبق تجربه‌ی شخصی. به نظرم Codex سخاوتمندانه‌تره به شدت. و صبر کنید تا وقتی که بن شدناشون شدتش کمتر بشه.</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/4332" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4331">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نشت مخفیانه‌ی دیتا از ریپازیتوری‌های پرایوت گیت‌هاب با یه ترفند ساده‌ی هوش مصنوعی
📚
فکر کنید یه نفر بدون هیچ پسورد و دسترسی‌ای، بتونه کدهای مخفیانه‌تون رو توی گیت‌هاب بخونه. چطوری؟ با گول زدن ایجنت هوش مصنوعیِ خود گیت‌هاب!
تیم Noma Labs یه آسیب‌پذیری خیلی خطرناک (به اسم GitLost) توی سیستم جدید Agentic Workflows گیت‌هاب پیدا کرده. داستان از این قراره که این ایجنت‌ها می‌تونن issueها رو بخونن و اتوماسیون انجام بدن.
🫵
حالا هکرها چیکار می‌تونن بکنن؟
هکر کافیه بیاد تو یکی از ریپازیتوری‌های پابلیک شما یه Issue باز کنه و توش یه سری دستور مخفیانه به زبان انگلیسی (Prompt Injection) قایم کنه.
ایجنت گیت‌هاب این متن رو می‌خونه، گول می‌خوره و به جای کار اصلیش، میره فایل‌ها و دیتای ریپازیتوری‌های پرایوتِ همون سازمان رو می‌خونه و برای هکر می‌فرسته!
نکته‌ی جالب اینجاست:
گیت‌هاب کلی گاردریل امنیتی چیده بود که دقیقاً جلوی همین اتفاق رو بگیره. اما محقق‌ها فهمیدن فقط با اضافه کردن کلمه‌ی "Additionally" (به‌علاوه/همچنین) توی پرامپت هک، مدل هوش مصنوعی کلا گیج می‌شه و به جای اینکه درخواست رو رد کنه، تمام محدودیت‌ها رو دور می‌زنه و دیتا رو لو میده.
این دقیقاً نشون میده که توی سیستم‌های جدید هوش مصنوعی، همون متنی که ایجنت می‌خونه همزمان می‌تونه پاشنه آشیل و نقطه حمله باشه. حملات Prompt Injection الان دقیقاً دارن همون بلایی رو سر AI میارن که قبلاً SQL Injection سر وب‌سایت‌ها میاورد.
البته این باگ به طور مسئولانه به گیت‌هاب گزارش شده، ولی حواستون به ایجنت‌هایی که به سورس‌کدهاتون دسترسی دارن باشه!
منبع:
https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4331" target="_blank">📅 19:05 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
