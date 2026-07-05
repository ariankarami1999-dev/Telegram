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
<img src="https://cdn4.telesco.pe/file/QB2CxLwPBFIUgX9LU8AuAHjfVE4ZUugFVRPKJ2lLpZz0PWdrsbC9_fBaYuIB6cXXTAsaZRIoh271hOhyqzeiyZAPymb-v4FKLVdxF630qou_-apPfZuTFTesCccIfSnpSBwtFvLQeFsW6pkHfjPnKz2d7VQoaBpwutT83YBnjssCDUjjWlC0uVgvQSRnAVU4WxC_SIvVJlHtiPQa2qAq-flMU-NJHgei2BDnxzHaEebjwWb2BE-Qs9ka-ZNcORnDdDwDW7N9RhXa8vVSDPMad-HijIqBx8rim5rWgh5_JC45YSiRj8V_tYSsqNXD8RKVTHoTVA1n6tDHOEfIYccbTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 21:30:48</div>
<hr>

<div class="tg-post" id="msg-447225">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f38f101ed.mp4?token=b4KJT0TgxRJf7y_IkAJBJJKm24L_CquY4OsS0D5-ItWpZVfHdzSFMJuNunvqJm7Thdk3RBC-QfEVZOc7B7wOy8in67Mhu3ngTP2oOr9bGI_pN099LqnlSCPeOb_GBv5dp7UjjY3XChUQPBCSmVhYeuapXbELEArgNFYBWgdCM54srgh6_A2hLwk8aWuLFS1HafZbQBTmcUhGtX5mRP3EELhblc0FhdmzPryOS_zFlVDcjuQShVJ_aK_JoK3SimYbonIYGpDecmzPdkt_e7GYxVcar381XIHOLOkxgOjJDBeiTwhPZqP4jS2mJHemKrYpcRwBD22GPD58DQo0aNaFBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f38f101ed.mp4?token=b4KJT0TgxRJf7y_IkAJBJJKm24L_CquY4OsS0D5-ItWpZVfHdzSFMJuNunvqJm7Thdk3RBC-QfEVZOc7B7wOy8in67Mhu3ngTP2oOr9bGI_pN099LqnlSCPeOb_GBv5dp7UjjY3XChUQPBCSmVhYeuapXbELEArgNFYBWgdCM54srgh6_A2hLwk8aWuLFS1HafZbQBTmcUhGtX5mRP3EELhblc0FhdmzPryOS_zFlVDcjuQShVJ_aK_JoK3SimYbonIYGpDecmzPdkt_e7GYxVcar381XIHOLOkxgOjJDBeiTwhPZqP4jS2mJHemKrYpcRwBD22GPD58DQo0aNaFBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار تهران: خدمات ۲۴ ساعته مترو و حدود چهار هزار اتوبوس جهت تسهیل رفت و آمد مردم در مراسم تشییع رهبرشهید فراهم شده است.
@Farsna</div>
<div class="tg-footer">👁️ 13 · <a href="https://t.me/farsna/447225" target="_blank">📅 21:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447224">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34db08e600.mp4?token=umLT4Q1BSmo2HdCkpYBUyHlet4julww-iPbBm-vdnMgRhDNuD928s2_Jp8PwHDrcoiCEIWbkV-bwK-WS4sLMY_3unRX9u9v_HdowQ3AoMU4JpSPtqTH1P4kJ28Xt0D_FzolmtFtv7hc9EWcrVuXlVF82860BX8BKGXofaNHFBTDpdjti3-w8nHho-N5QEBUuB-2Xv_ideBxs5VJQ_4qRdt4d0-AAc25qsMHORb69a43b_MDRD0tsdhB9DkEf-awp2ilLBM7iWrk3I96gdxVGu3YPmzhbRVXC4lxPyqR1DhcEFVcUJRp3IEA0-VCnN-l5SEa60tguAN6SucjGpu_Ynw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34db08e600.mp4?token=umLT4Q1BSmo2HdCkpYBUyHlet4julww-iPbBm-vdnMgRhDNuD928s2_Jp8PwHDrcoiCEIWbkV-bwK-WS4sLMY_3unRX9u9v_HdowQ3AoMU4JpSPtqTH1P4kJ28Xt0D_FzolmtFtv7hc9EWcrVuXlVF82860BX8BKGXofaNHFBTDpdjti3-w8nHho-N5QEBUuB-2Xv_ideBxs5VJQ_4qRdt4d0-AAc25qsMHORb69a43b_MDRD0tsdhB9DkEf-awp2ilLBM7iWrk3I96gdxVGu3YPmzhbRVXC4lxPyqR1DhcEFVcUJRp3IEA0-VCnN-l5SEa60tguAN6SucjGpu_Ynw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«جنگ رسانه‌ای» علیه مراسم تشییع رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/farsna/447224" target="_blank">📅 21:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447223">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎥
قم آمادهٔ میزبانی از پسر فاطمه است
@Farsna</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/farsna/447223" target="_blank">📅 21:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447222">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114792c204.mp4?token=UorjZspbJ-vosn8PQ24v9lRW6u1oB8Vp_mmsy2lyweuPRQO7L0Ee_d9DAI4kqZPo4ODQ_ZxTtqpbcl40CFRPgE4JMhNQe6ycu6B5-UMzaxaxA4_aoJ9nZ-vwH8oR9DLuqU2SIrz7gcW_nFSLF6fpFs8smc5tBK3W11emfOJqotLwvySoY68smfPH_sWusTGdciwbv38TTDKy8GDgaOoxh4EtzVFkPb3Bf1YlDAc3vDZHQGihnswonXatQsC85Ln1xyzofPc5ONGj3JC_gDEixnCapxZwQbQHVriDpkebsJIw3b1JgaZhbkCqqDogxxxtFxyAFgv0aPUviQWsIBRRSYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114792c204.mp4?token=UorjZspbJ-vosn8PQ24v9lRW6u1oB8Vp_mmsy2lyweuPRQO7L0Ee_d9DAI4kqZPo4ODQ_ZxTtqpbcl40CFRPgE4JMhNQe6ycu6B5-UMzaxaxA4_aoJ9nZ-vwH8oR9DLuqU2SIrz7gcW_nFSLF6fpFs8smc5tBK3W11emfOJqotLwvySoY68smfPH_sWusTGdciwbv38TTDKy8GDgaOoxh4EtzVFkPb3Bf1YlDAc3vDZHQGihnswonXatQsC85Ln1xyzofPc5ONGj3JC_gDEixnCapxZwQbQHVriDpkebsJIw3b1JgaZhbkCqqDogxxxtFxyAFgv0aPUviQWsIBRRSYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این وداع ابدی است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/farsna/447222" target="_blank">📅 21:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447221">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e437001e1.mp4?token=jKhhP8bv_9NnsP8-y9etrvNYB4ELXxRDNWH8q8joC_vZua9w55lbDofRpmaDLaXA5WgpouOR125mRx1S5C_tOvj3KnZUumJ-SMEqraY9XB5zl7QQyGqWHfs9_EwUwYWjxOyyWZfGb04sxZwEAh7au5AMKhwUdF0IpaRgVKkMUxyORIyEmgLsplLh42CV-b0-SVVtJuMOY9KHSS837N-T5zMk2N4OqwT5K2R56X61L55rEGNhpCb3IMv9_mTT5RSkYaS8gMkLzIaLJSCptXsJzN_i_9EmMvEljLyxP-N2uZzs56CMYYqmpzYOf6XfKsRoPkZEh8ocJTcKqVlMoUEIfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e437001e1.mp4?token=jKhhP8bv_9NnsP8-y9etrvNYB4ELXxRDNWH8q8joC_vZua9w55lbDofRpmaDLaXA5WgpouOR125mRx1S5C_tOvj3KnZUumJ-SMEqraY9XB5zl7QQyGqWHfs9_EwUwYWjxOyyWZfGb04sxZwEAh7au5AMKhwUdF0IpaRgVKkMUxyORIyEmgLsplLh42CV-b0-SVVtJuMOY9KHSS837N-T5zMk2N4OqwT5K2R56X61L55rEGNhpCb3IMv9_mTT5RSkYaS8gMkLzIaLJSCptXsJzN_i_9EmMvEljLyxP-N2uZzs56CMYYqmpzYOf6XfKsRoPkZEh8ocJTcKqVlMoUEIfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطرهٔ دختر شهید مدافع حرم از آغوش رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/farsna/447221" target="_blank">📅 21:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447220">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3ab0fca99.mp4?token=NT17Q5hEziTKf8Q2s1_FLhn94QOg0cZeNLQfMICgXSNDQBABxHXbwUWZT2HPTKbrWDFyUzXR_QtOkUQCIjY3YLI1upMO7hE20KNeWN6mCPjSGJ1FhkFLpLqbx_ahWcHYQXagFobyDsnGNgtpgbp5ArDAdtJROXnJqbcA9BAzLCdLsVEne5gyLQL2cmaThSkjzlf-rz_NucRX8_Tzuc3KvBndv-YtA9kkUX-EUahDiGQFLE6Pnwb-dIojZlBKDa-zcWFTq1S0JiQJDNS_beIuotZxlyvh5FTL_AJKITXHwWwHQ5lK3bcsV_kWbpAwDPh1vdU-9-sZqnsTn5jWsyBL_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3ab0fca99.mp4?token=NT17Q5hEziTKf8Q2s1_FLhn94QOg0cZeNLQfMICgXSNDQBABxHXbwUWZT2HPTKbrWDFyUzXR_QtOkUQCIjY3YLI1upMO7hE20KNeWN6mCPjSGJ1FhkFLpLqbx_ahWcHYQXagFobyDsnGNgtpgbp5ArDAdtJROXnJqbcA9BAzLCdLsVEne5gyLQL2cmaThSkjzlf-rz_NucRX8_Tzuc3KvBndv-YtA9kkUX-EUahDiGQFLE6Pnwb-dIojZlBKDa-zcWFTq1S0JiQJDNS_beIuotZxlyvh5FTL_AJKITXHwWwHQ5lK3bcsV_kWbpAwDPh1vdU-9-sZqnsTn5jWsyBL_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
متروی مصلی مملو از جمعیت است  @Farsna</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/farsna/447220" target="_blank">📅 21:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447219">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1d0c68399.mp4?token=HX2ZJ-mA0JXCw2NcZb63uxhfgiIaean6veDUAYptKyo7Xh_4pCSp4AhAp4KcusWMtGn8DCDrIgkXN6F2YU7E6u3xk6tVe_6H2eOHgzPeSBeNRDnbws-dqmf_yuoMQ0m61VRJJ2HMmyXXtecAfjkqpjENJrNX4CVOscPDhNfjl2Tnj0bgKaeQPmRuInIPdN50ZPhYPD1qbw8aFWJNJm1_9h6SH4DaPnIcYe6-2kdqLi0JH4UMuw_fixWgZz3GY5GV6WAnfdMr3c5UrFUVWQiQsT5OZgrEoyS6E5Q2XDJE-HlkdQfx9Rkd32RWd-So2JUAf5qZ4si3hUGepBJjrFJJEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1d0c68399.mp4?token=HX2ZJ-mA0JXCw2NcZb63uxhfgiIaean6veDUAYptKyo7Xh_4pCSp4AhAp4KcusWMtGn8DCDrIgkXN6F2YU7E6u3xk6tVe_6H2eOHgzPeSBeNRDnbws-dqmf_yuoMQ0m61VRJJ2HMmyXXtecAfjkqpjENJrNX4CVOscPDhNfjl2Tnj0bgKaeQPmRuInIPdN50ZPhYPD1qbw8aFWJNJm1_9h6SH4DaPnIcYe6-2kdqLi0JH4UMuw_fixWgZz3GY5GV6WAnfdMr3c5UrFUVWQiQsT5OZgrEoyS6E5Q2XDJE-HlkdQfx9Rkd32RWd-So2JUAf5qZ4si3hUGepBJjrFJJEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار تهران: حضور میلیونی مردم در روزهای اخیر، نشان‌دهنده دو پیام روشن است؛ نخست، وحدت و انسجام ملی و دوم، تجدید بیعت ملت ایران با آیت‌الله سید مجتبی خامنه‌ای.
@Farsna</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/farsna/447219" target="_blank">📅 21:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447218">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f9b9fcd0.mp4?token=u4BqyXlNmEDsB4B14BV6AwMeQ8C2lhhlNcH-7pPAQtutzkSXrmQYQuaobaeFw9vQpZ5Cl2V53irvJM9OuIEutAonz6tFJ3q8MGsDwFiGXh0jrKQWTwtH4SMsy5EU0c1Ee3odrhxLARIoxAavJZ5K2KE1woctN2W7LJOjxxLqZnUiDkfjVSHWmmZSRpvg3QfbXBjeDGFUir1yTl8NKmaG2EjQhFh1vrEC4J8axT-OtDsdtX6iUpcEeabTaRizOHmlXJVu9LowQhBDVm_XkafEMWmyuyYNtO5wLqxXH5gfl2hKsy6csPrX6mO41ujmZBPZCcUfjLZQUdYBA2h8haPedg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f9b9fcd0.mp4?token=u4BqyXlNmEDsB4B14BV6AwMeQ8C2lhhlNcH-7pPAQtutzkSXrmQYQuaobaeFw9vQpZ5Cl2V53irvJM9OuIEutAonz6tFJ3q8MGsDwFiGXh0jrKQWTwtH4SMsy5EU0c1Ee3odrhxLARIoxAavJZ5K2KE1woctN2W7LJOjxxLqZnUiDkfjVSHWmmZSRpvg3QfbXBjeDGFUir1yTl8NKmaG2EjQhFh1vrEC4J8axT-OtDsdtX6iUpcEeabTaRizOHmlXJVu9LowQhBDVm_XkafEMWmyuyYNtO5wLqxXH5gfl2hKsy6csPrX6mO41ujmZBPZCcUfjLZQUdYBA2h8haPedg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقت سحر بود که رفتنت رو شنیدیم؛ چقدر گریه کردیم چه غصه‌ای کشیدیم
◾️
مداحی سیدرضا نریمانی برای آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/farsna/447218" target="_blank">📅 21:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447217">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4a22b97c6.mp4?token=NXZFXDYORH4bsV_eL1Ef4sgTGxCmvsS0smLdKp39_T-J-ZUi4_9JXfOfxSDg2Ro52EanFYore-TLoZJzvuNPE4KLhFq36ifEVNOQQou9b3L5-MCbx5BGC3wlXXSA8UxF14nWQ7ppSiJiv6-reBE4qKtysT2dpyqEfY1UoFOcMlWn4FFdISbAM8nPQUvkdO2J4BXTpsvZJ8VPL0iQzPQE8TpaGeHDfB6zUiQKNaHDbA_vPc5fUr7vHzPJue1C4ovcdVaTdMJhWKw-QaMFy_XZzH0_iR_ki3yEMXrhMby-qZoXetim53AErauO7lf_OF4x8J29WRVI_NNcScNNomtARA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4a22b97c6.mp4?token=NXZFXDYORH4bsV_eL1Ef4sgTGxCmvsS0smLdKp39_T-J-ZUi4_9JXfOfxSDg2Ro52EanFYore-TLoZJzvuNPE4KLhFq36ifEVNOQQou9b3L5-MCbx5BGC3wlXXSA8UxF14nWQ7ppSiJiv6-reBE4qKtysT2dpyqEfY1UoFOcMlWn4FFdISbAM8nPQUvkdO2J4BXTpsvZJ8VPL0iQzPQE8TpaGeHDfB6zUiQKNaHDbA_vPc5fUr7vHzPJue1C4ovcdVaTdMJhWKw-QaMFy_XZzH0_iR_ki3yEMXrhMby-qZoXetim53AErauO7lf_OF4x8J29WRVI_NNcScNNomtARA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قوم ما قومِ شهادت طلبِ پیروز است
🔹
نوحه‌خوانی امیر کرمانشاهی در شب دوم وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/farsna/447217" target="_blank">📅 21:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447216">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e4e84657.mp4?token=TjBu5ovchEN8V8Lfr_IJPv3WAGreVkjp-OJXrhSjyCJLB7xnpqogkQVFkYPU8MF1aACVhdmlNmB6AbTlxFTFig9jhors4Bg3eqJY1ZZ08FVC2px-2nauv6xZzeEbQDNTBUvm8lvbOov0B5mvbzBAhADKpfES3MXz6OQkAAEs0_MTIfVPgEj-gNXJWhESPXKRkMzwDAjOsclEPROGjD5sIl2IpITe55wCgPmPmQeSOXxi83wATtkdqSRJLn4VyLMNqujionuzYWjd-ZTVB9YB7uGUUkMvrTRC4dX49WSfve-PouMhWuMmWKmnjuo4JIF69t4Pb0OJFOyatYaocn9ENw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e4e84657.mp4?token=TjBu5ovchEN8V8Lfr_IJPv3WAGreVkjp-OJXrhSjyCJLB7xnpqogkQVFkYPU8MF1aACVhdmlNmB6AbTlxFTFig9jhors4Bg3eqJY1ZZ08FVC2px-2nauv6xZzeEbQDNTBUvm8lvbOov0B5mvbzBAhADKpfES3MXz6OQkAAEs0_MTIfVPgEj-gNXJWhESPXKRkMzwDAjOsclEPROGjD5sIl2IpITe55wCgPmPmQeSOXxi83wATtkdqSRJLn4VyLMNqujionuzYWjd-ZTVB9YB7uGUUkMvrTRC4dX49WSfve-PouMhWuMmWKmnjuo4JIF69t4Pb0OJFOyatYaocn9ENw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایمان قیاسی، مجری تلویزیون: درود بر غیرت خواهری که وسط برلین حرفی را زد و حجت را تمام کرد.
@Farsna</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/farsna/447216" target="_blank">📅 20:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447215">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9295861970.mp4?token=HBaw_rjGpJp3phkNwmqp3ib8UbNeEZIFkWA-ungtQSDCd4sw1f6LSroqJHUQhtCv9pNMLdisN6wU2KCINkNhRvyqnGYhkn7Mlk-rEQXtvuETAMpPdGGIw4Su_RfySyhgxmE9GGBgpTUowc002TuXV03xyjatGvXe0AvCNgoBRprikS8dvJ88hhKX22jWeDNemi7oE-j7PIOEgH4QFxSAIvHLFFye6zqdKxjV-y_AvPefP2MjeP3jlL2gCtwr6gzTMKiWI2RH8ocZhYP5_bs9pLShzEmRHxmOpO7Mob-TQ63hWPpoT5k_kKjGCU3S5j8MbAFXu-hSFaRxEKa7HAghTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9295861970.mp4?token=HBaw_rjGpJp3phkNwmqp3ib8UbNeEZIFkWA-ungtQSDCd4sw1f6LSroqJHUQhtCv9pNMLdisN6wU2KCINkNhRvyqnGYhkn7Mlk-rEQXtvuETAMpPdGGIw4Su_RfySyhgxmE9GGBgpTUowc002TuXV03xyjatGvXe0AvCNgoBRprikS8dvJ88hhKX22jWeDNemi7oE-j7PIOEgH4QFxSAIvHLFFye6zqdKxjV-y_AvPefP2MjeP3jlL2gCtwr6gzTMKiWI2RH8ocZhYP5_bs9pLShzEmRHxmOpO7Mob-TQ63hWPpoT5k_kKjGCU3S5j8MbAFXu-hSFaRxEKa7HAghTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام رحیمیان: تنها مسئولی که بدون وقت قبلی می‌توانستند خدمت امام راحل بیایند، رهبر شهید بودند.
@Farsna</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/farsna/447215" target="_blank">📅 20:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447213">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🎥
عزاداری عراقی‌ها برای رهبر شهید انقلاب و عرض تسلیت به حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای
🔹
عزاداران عراقی در استان بصره عراق با حضور در مجلس عزای امام حسین، برای رهبر شهید انقلاب، حضرت آیت‌الله العظمی سید علی خامنه‌ای عزاداری کردند.
🔹
عزاداران عراقی با سرودن شعری به زبان عربی با مزمون زیر به عزاداری پرداختند:
🔸
از (امام رضا علیه‌السلام) یک مهمان برای ما آمده و با قدومش به ما شرافت بخشید
🔸
ما در عراق پیکر خامنه‌ای را دوان دوان بر دوش می‌کشیم
🔹
در بخش دیگری از عزاداری، حاضران در مجلس، شهادت پدر را به آیت‌الله سید مجتبی حسینی خامنه‌ای، رهبر معظم انقلاب و بردارانش تسلیت می‌گویند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/447213" target="_blank">📅 20:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447212">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01c18cbad.mp4?token=fG9OamnbOuUzESurN7KREqEuaB1fHfa34c3Kqjo9JyrxCF-IjkZuSL8KRLK69LJd5FYXE-1mz0S7OyPZ5koNwniLWAsmUTWHIKGTVLB1xjaYTckX4m5MycIs4a7cbvfhnHEGq6vuRaCWyXmhsHkBjgRA6O9AQ6-XG6xdw7eM-HSk0eMS5ciruKjI7y4i_Bu54UsEm8VVIxmj_wBqZ8aVcHDdwmbSIf4hu3GuXDyW_FZo7FG8EuVqmCb-zfBQc-NKB_UqbOlD4Q4U4zh1fFdP6nMHNobrO2ZtowX73f-JbgjOjdlxURbfzT6PfcnrS_WfSdRt6JTCIshDQwKbR4h_A5w1RNwgZEg8LtzpS5HbdRKdSJVAdFB0AR00qCKdAOp49pAEsccg1TD2q-G_Fosg-gm7crGJRW46BULloGU61UNKPD0TLJkxQnsEygiYvdbgZYBeQjSDeiAjWUAJY8kWjEr4eRKFs5ed-H2sV-3EL3OSCsF9FnqRuVJusHvZ7Eidh-CIXFoXSaxyT5wPxQuQ11AjWKgwOM9h_lkJDomuxhXXgLmE4UNKywBS-BUx1EwBdM9tODCkvPth-xlxdldH6XzNAeok13Q096f8g8G-EYtdcttx9hNZWh9VzSCoPmJrEwkLn9lH-X1ryCc7KeyJTTLzGO_saDgIz9LbxgdFsTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01c18cbad.mp4?token=fG9OamnbOuUzESurN7KREqEuaB1fHfa34c3Kqjo9JyrxCF-IjkZuSL8KRLK69LJd5FYXE-1mz0S7OyPZ5koNwniLWAsmUTWHIKGTVLB1xjaYTckX4m5MycIs4a7cbvfhnHEGq6vuRaCWyXmhsHkBjgRA6O9AQ6-XG6xdw7eM-HSk0eMS5ciruKjI7y4i_Bu54UsEm8VVIxmj_wBqZ8aVcHDdwmbSIf4hu3GuXDyW_FZo7FG8EuVqmCb-zfBQc-NKB_UqbOlD4Q4U4zh1fFdP6nMHNobrO2ZtowX73f-JbgjOjdlxURbfzT6PfcnrS_WfSdRt6JTCIshDQwKbR4h_A5w1RNwgZEg8LtzpS5HbdRKdSJVAdFB0AR00qCKdAOp49pAEsccg1TD2q-G_Fosg-gm7crGJRW46BULloGU61UNKPD0TLJkxQnsEygiYvdbgZYBeQjSDeiAjWUAJY8kWjEr4eRKFs5ed-H2sV-3EL3OSCsF9FnqRuVJusHvZ7Eidh-CIXFoXSaxyT5wPxQuQ11AjWKgwOM9h_lkJDomuxhXXgLmE4UNKywBS-BUx1EwBdM9tODCkvPth-xlxdldH6XzNAeok13Q096f8g8G-EYtdcttx9hNZWh9VzSCoPmJrEwkLn9lH-X1ryCc7KeyJTTLzGO_saDgIz9LbxgdFsTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور چشمگیر مردم در ساعات پایانی وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/farsna/447212" target="_blank">📅 20:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447211">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259b338fe8.mp4?token=TLvZ7unqAmT3fdZfXuFXMBkKhGpcd0w6WcDXJ2yUKw8KecREIPgEvMUCwA7J1BB1yoMoEcoQYrMjwidLvEPTU2myMgYyQEFGT4PEs_beZ8JUXq1Tt2rVXDXm_ZyQaSQTguwoYiYFjYJ3ePTLKxNUTefi04B0cPzyHmlIe1gO0rLxmCF4FKI0Ki_dN002qXrca_bJdOMM2m60k70JT4udoBoICE_gKI46_EihjklSXE0E-PnmwJO1t_chS3p1IjTQySMXfdC59ZKkR7g-DfdJN7fV6OKE4hawjZu-4eE4CHH3tpTBE7XCLLDyqhqwWiPx7Y4oViZLyuYidx6FzlCEiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259b338fe8.mp4?token=TLvZ7unqAmT3fdZfXuFXMBkKhGpcd0w6WcDXJ2yUKw8KecREIPgEvMUCwA7J1BB1yoMoEcoQYrMjwidLvEPTU2myMgYyQEFGT4PEs_beZ8JUXq1Tt2rVXDXm_ZyQaSQTguwoYiYFjYJ3ePTLKxNUTefi04B0cPzyHmlIe1gO0rLxmCF4FKI0Ki_dN002qXrca_bJdOMM2m60k70JT4udoBoICE_gKI46_EihjklSXE0E-PnmwJO1t_chS3p1IjTQySMXfdC59ZKkR7g-DfdJN7fV6OKE4hawjZu-4eE4CHH3tpTBE7XCLLDyqhqwWiPx7Y4oViZLyuYidx6FzlCEiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات برنامه اقامه نماز و تشییع رهبر شهید در شهر تهران از زبان استاندار
@Farsna</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/farsna/447211" target="_blank">📅 20:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447210">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dea728980.mp4?token=PtK4KZMSHCiswnjsM5t2TaHKUpwnbmgVQLbemuMvi78yXSuLMpUiFG6LDof33_Bo-RhZNUvLGzaPk5k8L_U8yIFm0C67zdB9LcS0GG_GUwrmDrQuAuM4ZwxbXbGAEbx2qsj7sMobWIdo4ZlitX22sJcUwi4b16VcmTPS3ta1_ezu06ty2aaQZrrqsAF5HfX4kUHw7zes42Kyk03kVR_Bffnm-PZ69ksTIMLRPfA0omDzSm7zGRIcPDRFk0ulUIfs0KkdBcGHcDpnZFyPobOn6o9ZF7JE6GdxrqQ1Pv7CSpWr3gTW-q7vOMxPXv8_2ALRI8UF7LhjZbPO2tTFCPRLPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dea728980.mp4?token=PtK4KZMSHCiswnjsM5t2TaHKUpwnbmgVQLbemuMvi78yXSuLMpUiFG6LDof33_Bo-RhZNUvLGzaPk5k8L_U8yIFm0C67zdB9LcS0GG_GUwrmDrQuAuM4ZwxbXbGAEbx2qsj7sMobWIdo4ZlitX22sJcUwi4b16VcmTPS3ta1_ezu06ty2aaQZrrqsAF5HfX4kUHw7zes42Kyk03kVR_Bffnm-PZ69ksTIMLRPfA0omDzSm7zGRIcPDRFk0ulUIfs0KkdBcGHcDpnZFyPobOn6o9ZF7JE6GdxrqQ1Pv7CSpWr3gTW-q7vOMxPXv8_2ALRI8UF7LhjZbPO2tTFCPRLPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: همۀ خسارتمان را می‌گیریم و جنایتکاران را رها نمی‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/farsna/447210" target="_blank">📅 20:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447209">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af713189af.mp4?token=uMIeg2QJ1cFE4wVJStiNRnNx0I9IbPQKXh0_0dk7C68CVIaCYc_eR9WkiOnAxIb8nG5IYVaU8X9ZggfIazrnOOEypfEj0OmFe5Ru9Bngvxa0JWx33ksptjTb9NgFjZCa9LCaHFNnKi_5Pmk-eZW6udIu3yI5hl4ZHX846dVbTT2lQaqtRC7vohrX1csPkNhKgImrw5X2Q1KYxYgpQkCXpRILN-OrEOoAyNSprnFLoqa2U7SqtUxgJ3Vlb5PrNFcNPYL9V_LJn26GXb5jLUl1fAtAfm9i4iXB7mlRa38ivsSN3R8wNOTQj-zcfXJ13Gvf2oR7NvhnWNGIS7s3REfpdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af713189af.mp4?token=uMIeg2QJ1cFE4wVJStiNRnNx0I9IbPQKXh0_0dk7C68CVIaCYc_eR9WkiOnAxIb8nG5IYVaU8X9ZggfIazrnOOEypfEj0OmFe5Ru9Bngvxa0JWx33ksptjTb9NgFjZCa9LCaHFNnKi_5Pmk-eZW6udIu3yI5hl4ZHX846dVbTT2lQaqtRC7vohrX1csPkNhKgImrw5X2Q1KYxYgpQkCXpRILN-OrEOoAyNSprnFLoqa2U7SqtUxgJ3Vlb5PrNFcNPYL9V_LJn26GXb5jLUl1fAtAfm9i4iXB7mlRa38ivsSN3R8wNOTQj-zcfXJ13Gvf2oR7NvhnWNGIS7s3REfpdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضاییه خطاب به قاتلان شهدا و آقای شهید ایران: گریبان شما را خواهیم گرفت و رها نخواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/farsna/447209" target="_blank">📅 20:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447208">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c01d010366.mp4?token=cpq97S6r1EZb1k6rBbQiubIKhja6701EnkZBn-ai9aHd2IHsh5IxjlpLqYxEZwPqHWvlyPRSbQTXS_g83xVQ1JrcgXc24qxNLoI8ZZeve1sZvvmvjGo_bEMCBfOrn2Ku90Egh3gWj5rRUNxvwpTsMy_5r4Rqp4sqsizbA0JqrYp6Ipe_Wjwn18oMK3mF6SGwANJmGJgdMsAJNAX6UdyQJaH7Fh03z3DcFlfX2NmN-ci976DuND9jxEiy8NyU_Y_E7aN5cX2sWitrn7uWi7vWM7Q8PGy_4yMWmJn35whZRnuotXYH5ipWRXBmuPtcyWFDPrtWjgwP-VvDADRXsdlNxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c01d010366.mp4?token=cpq97S6r1EZb1k6rBbQiubIKhja6701EnkZBn-ai9aHd2IHsh5IxjlpLqYxEZwPqHWvlyPRSbQTXS_g83xVQ1JrcgXc24qxNLoI8ZZeve1sZvvmvjGo_bEMCBfOrn2Ku90Egh3gWj5rRUNxvwpTsMy_5r4Rqp4sqsizbA0JqrYp6Ipe_Wjwn18oMK3mF6SGwANJmGJgdMsAJNAX6UdyQJaH7Fh03z3DcFlfX2NmN-ci976DuND9jxEiy8NyU_Y_E7aN5cX2sWitrn7uWi7vWM7Q8PGy_4yMWmJn35whZRnuotXYH5ipWRXBmuPtcyWFDPrtWjgwP-VvDADRXsdlNxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضاییه خطاب به قاتلان شهدا و آقای شهید ایران: گریبان شما را خواهیم گرفت و رها نخواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/farsna/447208" target="_blank">📅 20:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447207">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a98eae559.mp4?token=eqqqnWmwjpk1ZwRuamAbuDlOahefUux4TnpYXQ_JquY7wvxTfATWTUraMF7uhQiaT5K8qFui6jAnSbvfxaKrVLmNkfqAMR_SWyqMjL7S-J_EnYKw3ALVz9e7-VUhInY2V-7nlem111Nd4E15hc4jMyaW30Xl_pt9k2ok6bKMoeMn1WoiwGTXP-hVp2TJUi7H9U-z7wxRYDLXmZi3p-0OML5564q3X75gMLWYrILn3B9NL-SKprxjSkJffX53RI0SeSRQHcXgdASuwm5KqN56rtED9rS0qwGxQrrZmWNixnqg00k3x1P82LRfjKCppa_5sXn7O03brfqRmzfTWXgJfIrMfbzBGIleAS-gNDyAcYTmkXOESY4oTQOBK4ogUWhKR2uKVktVi1RBULajYjxpiVjg1fa_agcJ6DQh8J1mSNtxdEzKpldkTxM6ftMAprxGk33h_fZcuZRtv1UTx8wEti-i62RTtyDrgsbcALzwjDs3vRpuNxwM2Sgksbnz5jKhxGuGKqEeb6jEHhiQ0eBTIkie-Gv5bQbvcaQCHK6hFqnHnOtU8YKGcMdG4xdalYIF7cHjLqh2iMO2hL67My-Jnfb3XHj4lFpQEOQBiRaSksMWf_lRzA9RNwzwvzon-7K-1wr3LrGQVyV-1dhjObpv_pzNzAKULGuYL7Sc8Ti--5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a98eae559.mp4?token=eqqqnWmwjpk1ZwRuamAbuDlOahefUux4TnpYXQ_JquY7wvxTfATWTUraMF7uhQiaT5K8qFui6jAnSbvfxaKrVLmNkfqAMR_SWyqMjL7S-J_EnYKw3ALVz9e7-VUhInY2V-7nlem111Nd4E15hc4jMyaW30Xl_pt9k2ok6bKMoeMn1WoiwGTXP-hVp2TJUi7H9U-z7wxRYDLXmZi3p-0OML5564q3X75gMLWYrILn3B9NL-SKprxjSkJffX53RI0SeSRQHcXgdASuwm5KqN56rtED9rS0qwGxQrrZmWNixnqg00k3x1P82LRfjKCppa_5sXn7O03brfqRmzfTWXgJfIrMfbzBGIleAS-gNDyAcYTmkXOESY4oTQOBK4ogUWhKR2uKVktVi1RBULajYjxpiVjg1fa_agcJ6DQh8J1mSNtxdEzKpldkTxM6ftMAprxGk33h_fZcuZRtv1UTx8wEti-i62RTtyDrgsbcALzwjDs3vRpuNxwM2Sgksbnz5jKhxGuGKqEeb6jEHhiQ0eBTIkie-Gv5bQbvcaQCHK6hFqnHnOtU8YKGcMdG4xdalYIF7cHjLqh2iMO2hL67My-Jnfb3XHj4lFpQEOQBiRaSksMWf_lRzA9RNwzwvzon-7K-1wr3LrGQVyV-1dhjObpv_pzNzAKULGuYL7Sc8Ti--5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار تهران: هیچ‌گونه انسدادی در ورودی‌های شهر تهران وجود ندارد
@Farsna</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/farsna/447207" target="_blank">📅 20:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447206">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024795ab39.mp4?token=m551MY4xteb9ToLjnnWqrIOj_5HzUYcRyPRTEUcw4wZJK1_zVZoLVRllpHi3wucmLQuF0v1V1xTrtIHBeCbfZ_cJByi-gZkRJrIMLcdxfgnnPpxUinY9U1fFV8qL_Yeksuj2zHgRsFS3Z4s-i6CyH_joUuiJTWBR1-MXCBCZOsWZoJKAaudRWqSXYA5h1-GBGawXMZ4jrf8ZZ_zKR3SGcTerwJSL1kgQCCkMvNct-lORIzW_XgDPEGsLb5WhVZ0SKhl03CKFWrygu6-yUDpa67JR8ovc2XLCvHsm2ElUatcGq1ZIGaklHAJwJOtpFayy0xRP5Nda4RfUR97juhcEAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024795ab39.mp4?token=m551MY4xteb9ToLjnnWqrIOj_5HzUYcRyPRTEUcw4wZJK1_zVZoLVRllpHi3wucmLQuF0v1V1xTrtIHBeCbfZ_cJByi-gZkRJrIMLcdxfgnnPpxUinY9U1fFV8qL_Yeksuj2zHgRsFS3Z4s-i6CyH_joUuiJTWBR1-MXCBCZOsWZoJKAaudRWqSXYA5h1-GBGawXMZ4jrf8ZZ_zKR3SGcTerwJSL1kgQCCkMvNct-lORIzW_XgDPEGsLb5WhVZ0SKhl03CKFWrygu6-yUDpa67JR8ovc2XLCvHsm2ElUatcGq1ZIGaklHAJwJOtpFayy0xRP5Nda4RfUR97juhcEAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی سازمان آتش‌نشانی: در صحن ۵۷ هزار مترمربعی مصلی، سامانه‌های مه‌پاش برای کاهش گرما و رفاه زائران راه‌اندازی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/farsna/447206" target="_blank">📅 20:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447205">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJ8K6PywrvkEG0QW-m22d0mhXCrV2m7hAqqvxm_lB-CKsNCpNONTH6hlpoXvhTz91Dc32KbDCo82WwfiVuSqNUx5awKTf1oU1uhEd0T5SGdlLKvbi-o3x1_poU2rNjJ8v0eUOka3rgjw1Rzjqn1wOXgfMUAId_1gRDfFvUiaxj8h290b_Vip65ce-5dCBPdlCbnABwHvaICKpqQMBBIaG-yM_gMAkFLv7wHvkRG7NWeINYssYJxg2eyWfZMEqX0920eTMhu0kxPduruJJpbqz4YLhTjxnHZPrfagAsQ69LlA8T06NBYcgRzaAZtuvGm6m8kpIX4p1cYmEmqGfSs5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتصاب مجدد حجت‌الاسلام والمسلمین اژه‌ای به ریاست قوه‌قضائیه
🔹
حضرت آیت‌الله سیّدمجتبی خامنه‌ای رهبر معظم انقلاب اسلامی در حکمی، حجت‌الاسلام والمسلمین محسنی اژه‌ای را بار دیگر به عنوان رئیس قوه‌قضائیه منصوب کردند.  متن حکم رهبر انقلاب اسلامی به این شرح است:…</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/farsna/447205" target="_blank">📅 20:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447204">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43293ac785.mp4?token=rSw823IFzjwCskHm6U6Ez6_oCxerXvh3ZJWJu-3q8t4vr8bhdiBetMp70WR-TO27ja-0lVRl4qIiL2AdK7EakUZdSKkQs4r8nCoZMrf7BYFeupAwcvKIyyDjY_Mo6a1YBzjxkw2p40-GCj_z3Di-QMXZKwnvs4bs6l3cX0IpOym3QanC-KtaKQEFGiYW0aeHZ9aGHU42Xv1Srz5kRPvd6hoq-yHT6MIM1i7cDHmu-fpdk16z98zHj-8W5VR6ml6WQuf_ZuF4efgxwgq2I9JT4ywLS1LIVGHoP015WIXiXNeN1SxCUgBFo62kJKZhgKp9gYgiCjoX4Q9TjoQBYc3wDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43293ac785.mp4?token=rSw823IFzjwCskHm6U6Ez6_oCxerXvh3ZJWJu-3q8t4vr8bhdiBetMp70WR-TO27ja-0lVRl4qIiL2AdK7EakUZdSKkQs4r8nCoZMrf7BYFeupAwcvKIyyDjY_Mo6a1YBzjxkw2p40-GCj_z3Di-QMXZKwnvs4bs6l3cX0IpOym3QanC-KtaKQEFGiYW0aeHZ9aGHU42Xv1Srz5kRPvd6hoq-yHT6MIM1i7cDHmu-fpdk16z98zHj-8W5VR6ml6WQuf_ZuF4efgxwgq2I9JT4ywLS1LIVGHoP015WIXiXNeN1SxCUgBFo62kJKZhgKp9gYgiCjoX4Q9TjoQBYc3wDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همهٔ شما مثل فرزندان من هستید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/farsna/447204" target="_blank">📅 20:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447197">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhMunfl8TsDEDbezcmSd7keguT7jNlHQPnzb5Ym3ATO4-VBMUvWb8PzESTrUf6xH-lMmQOJ9qoziEt46lOk6YGP0Kq7jzXzy0QEhbzzWI0j5RUFCVupOrAuMkEZBSiHRyCnnG_GgEtfA9SyyLogG5Z3nvDDLxv5umvJLbm2nThiPEDMmGxkN8tkSlklbDSHFuBsL9E2CjWMp-Y_5bT90VmHKBAgx_G6zUax5bRQY7fZFlsYhN6gYUoF19Ke4dvxQpw3tFyhIjUvLhHMjwIIIitgB-Intl1wuwYStIwfE6UeHNSbAvXlB0tn_sJbtidnmRL5bJ6r0scDtXUbxMlBrWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ruERtvdIl229bGzKUUaDl7Nr5eWuY7qQN6N-GTzHDP3g8Cv35Y7irYay2XVApoMn7Aa_mhXAuoh50wfKcut9Lb8e1DjenXoG0Vb45O1d5BRfJXgT7LR48PnzJW9mp9quEi5Z7R1ywZB57IjWt-nwooUvVdQ-jPZWFWDl2Jc1fhZvh2gqQLbS3TdYT36bCXgRK9Yo_7aaCL2Qg1rchkOe_S3lynYG8rl3TtqcR6z8USCjPvxlChGErJ_SjAbQYHZ4DMNVnVDjGX0srpCGbsvh3fXoHf59F-O-_J9YAEVRQtoJVAs6heRtCifWoJtjdZdUcEH7TP-Rv-ErSxP75liMgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0pC7Pdjlw9Hkiy_HbjyTq6KdYbQHVFy7X0bcx6Y8ph8h-GKPxKe-NtlOo6L4VWHc9A-fWFgOQ9Q9_W35FWbjJg2KRdRZSIpnFDErSp5LvoELLchottqEmZwNtlt6AOm3Ivc7qfiR26_FgE0-Z1540IG9FufG9JjQxP0RNFBvfHVVccxLGDKerO4aTnV29VOc3NkwljiA5RQOIybLOeorl55YZIVaODYdqta7nLpLpw65E-DHz7rlQ0stjrTPY_f7Zbs_8dLrvUfhm4HOyf9wGyWXmM7AMDUXLiwbvkzhrFLaeg5ss_7nvy4xSb7PFU1rINohl-0wHXQD0WXgbrAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKPAt2AjGnbScngVpZwYltbqKEQUA6QuvekOW7bjLhW4lEnBvaRRsal_UzNaeXgYnLGibQSfNC7MUWNiTP5SzCetSP4YI9Bs0a02WRO8opYFJ9AKKzC-C9zudcMqIrcIMr61VHRRyQRivwqLeBpqCXuDiMhFRs7Wji_3Q1PwZ42tMnbpJL_qJLnIwo_D-hejryJTYDtClDFPZcAEwxr0jxcNjcz05i1iDSITJjTpr73wRM3MeSYQAlFxxEDEz0Bk6yFDK4e3aVV32hbTABxkIydR7h5HHOyr8BGDeDJQcb-g8jUTmxHwxoGULUyDoKL_K0fRZfbAiRChNE4X4MvfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/duWk2UR7f23UjJDZgInotAh-2ILTEPq2cL4ZR3c38flOYH_g4KYJT46EwKCqTHrAC7-5nM8XqtBroFvGpXlkN3VAXYBZEEi-hEq-xz28BTigFHnXxbaqrgRPdPVQ-uJQiy1E1B1w9cBfEbOmP8dOLLz7xCm9O3DYEc4Lef8rt8td77eJpWyUHfeYVlf1PJzJ7YA8i5mMtajCDmLBOQdxEBYNhFaFQp1L9orsUkydxiIQuol_u9k2suocLXCoBNdAScEhYE_hQJdot8Z3AHz_duNvhLp6EprXdf0nHHnLIQZAk7lMhC6AFIdsKVVhfamAZ0zmZ74_X8WW6CZ7vT3hYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igbjgAWIm4NHdeBedqn4G4lBjf-_2MX95aHTUsbuhQweueLhZoquVWzS0ygUvBe_gETUnI9sNzomPaDA70-CDEEkqJ9tl6foX_l5JodUFY5Wp-mjmVR3dXSNUXs3M2DsdDj62HlraWMP6BHlkundlUuLmQxtH9mLmNopsrtarbZz1NvUQwwRsXhpOdwZY0cp4FybISYeW3P-SZ47V_C08Dn5rhxIOZsWVWcSRVKdW0u3O4FYqMpoB9n5CnImkIfGn7ecXtGRXnw-QAHNypW0AFdtCsXs2OM32UNfYBhil5uwKtJS_22ougJhoqX1NUkU6-6zD35S7Kowex3lLE7wSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nGsaPIojfRE-CEOeuS69Ntrn8NMhtwIwT7e8hAnlKw7iwMmglzbGhMaU9ihY_SIIe4Dp3z3kQJT2AU_JyVWJHsMHdbOvsxzHqhv5R030vrFeUyxI2vyvFoL29eShOkHMuHtFzAhWQus4mMt3mq-KdheiKHe4xPJfz8tC5uWNAJU7fvObSVA0rE0debOxZrqAdSGgdqwUPFftHVSPNGFn8SFyDPgiTjkvk0KtCCwWdrsb3JN5c2a8AF4q90zxc-zmmFDBhJeo8x0SZvFj1C0VP1OPrYBZ_GeGJBjglITrqpoiQQgiT3TrxVbObXmdu1jduihhQ_Va1ZLesV6AEv6QRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین ساعات وداع با پیکر رهبر انقلاب
عکس:
صادق نیک گستر
@Farsna</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/447197" target="_blank">📅 20:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447196">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c400f5c86.mp4?token=eDVDBXgW2ptMk44stv65shCeRaRj1p195NURFCzPRUlpox9psEmmcTKC1Jfaz4BG-LGVZhcTOqxTgheFJawXBJ4-nGzHif6gWC5pDvPRh2gWIxQcoBjblnFCz93M8WBa91lpfNDxW95H8r-3xR6dyQpZAlGi_uZOy4PfrqEi02ToDblh2ya29Afy_iAUVPJYS5O7-5SDO-5chqRJphza3MnweBd4lQwXLWEnq5_frBoQFTKsTyc8dZFS0dw7C-0HKW2QdwzHOO00YV5z5V8cjU89El0y7pqImfTym9CYXyNzTubPO3WBdZJ0r83KUuR_ZNm12IDzw7ahhd8BWhWNPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c400f5c86.mp4?token=eDVDBXgW2ptMk44stv65shCeRaRj1p195NURFCzPRUlpox9psEmmcTKC1Jfaz4BG-LGVZhcTOqxTgheFJawXBJ4-nGzHif6gWC5pDvPRh2gWIxQcoBjblnFCz93M8WBa91lpfNDxW95H8r-3xR6dyQpZAlGi_uZOy4PfrqEi02ToDblh2ya29Afy_iAUVPJYS5O7-5SDO-5chqRJphza3MnweBd4lQwXLWEnq5_frBoQFTKsTyc8dZFS0dw7C-0HKW2QdwzHOO00YV5z5V8cjU89El0y7pqImfTym9CYXyNzTubPO3WBdZJ0r83KUuR_ZNm12IDzw7ahhd8BWhWNPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دکتر محمدرضا کلانتر معتمدی، پزشک رهبر شهید: رهبر شهید زمان جیره‌بندی حاضر نبودند بیش از جیرۀ همگانی استفاده بکنند.
@Farsna</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/447196" target="_blank">📅 20:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447195">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa8e78c7e1.mp4?token=kGMSBJ5JWVxVLUYd0hw_akMwK-m_OsyKlxJC0bmqikKER1QougAtWYvai6zw72ZdtJG_JS8wf4uzc58GRNz3yoOT3aqzUjNehFE-PiCM1tOtNbrt85UP-L0S7HN7vI1yhxmYOSRc6kKT2qwaBIP-x85lQQaOxz2uWUkewESjpF0A0Y8rCr-ZWO-lUA_fUg4pZxG9AIH7vAqLchR0dKM6ZzVGgur4CERKXp7rnEd46cvIzDWo-_u3bZ9MozxVfjouW4iQHfXCgaNCAGm1zklym7nXxufhsxPDH19v2TdbR5BXORAvy45H2vC1uuJG9s8zx8_FYhtacrndSRWwic-3vl16jQwbfD91ad7ip9oo40roc0_pKpVRY162CM2M2qxNmaQ8nbbC8X6Mk2PLEDH7pl4AU7Ny6kxUQofJPWSV7kiOvoUJBqrz0KtDqZMbkV3vRbBBI1-_zV3yMoZzKWOS5nIn2dONEHCCkZ5xrCvyOouJ8pr5tv2rYeJmaUxboYH6VtzSEj1OxKvOenRumFoyf1gngW22BB9XBwS0aSJcl113PpFIiVfqWCOEVRd0Bz-nVkMFxo7mrFbsYSn_RfDdfqDqtBr16TpprlEDYVQ6PXoTZvgcH_MgNah-VuP4G374i_zxxa_NiZ2UXffvZOkodRSpyz5n6pzXLLAYGXdsBCI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa8e78c7e1.mp4?token=kGMSBJ5JWVxVLUYd0hw_akMwK-m_OsyKlxJC0bmqikKER1QougAtWYvai6zw72ZdtJG_JS8wf4uzc58GRNz3yoOT3aqzUjNehFE-PiCM1tOtNbrt85UP-L0S7HN7vI1yhxmYOSRc6kKT2qwaBIP-x85lQQaOxz2uWUkewESjpF0A0Y8rCr-ZWO-lUA_fUg4pZxG9AIH7vAqLchR0dKM6ZzVGgur4CERKXp7rnEd46cvIzDWo-_u3bZ9MozxVfjouW4iQHfXCgaNCAGm1zklym7nXxufhsxPDH19v2TdbR5BXORAvy45H2vC1uuJG9s8zx8_FYhtacrndSRWwic-3vl16jQwbfD91ad7ip9oo40roc0_pKpVRY162CM2M2qxNmaQ8nbbC8X6Mk2PLEDH7pl4AU7Ny6kxUQofJPWSV7kiOvoUJBqrz0KtDqZMbkV3vRbBBI1-_zV3yMoZzKWOS5nIn2dONEHCCkZ5xrCvyOouJ8pr5tv2rYeJmaUxboYH6VtzSEj1OxKvOenRumFoyf1gngW22BB9XBwS0aSJcl113PpFIiVfqWCOEVRd0Bz-nVkMFxo7mrFbsYSn_RfDdfqDqtBr16TpprlEDYVQ6PXoTZvgcH_MgNah-VuP4G374i_zxxa_NiZ2UXffvZOkodRSpyz5n6pzXLLAYGXdsBCI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماهنگ «رهبر جاویدان» با صدای محمود کریمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/farsna/447195" target="_blank">📅 20:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447193">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/927fb2214c.mp4?token=mKKWXmxUfPtv5qfvauUUcfSj1w2wvOm7wOhrH0bj2yupvkE3-XFSv8jkMg4ZSWw7nZqMmAm5vTYIIeuQxLEqfEBuOCfq4b8z2EyTmWxdGYZFoGWWugWPsP5EFxvtPHCw5az140zEsgbxJF58zwsLzT_jfbhcpnlh3cDAoyFs23JlcZXXKRbwBO3JKCU-TTB4PF5tHHu5wOGRGHWOZ5TYnCZm0NFbeJ_Nr3ct_vRhRAexAZNx5WWS-aqkBFNi5V_erVbafkRKdJ0n21e7k49MWVQgpOOU13VDNfEZlcvCCRL502XRtrIGd3dbxkaoEU0t-yVZDFdH9QEE5bTeMOgI6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/927fb2214c.mp4?token=mKKWXmxUfPtv5qfvauUUcfSj1w2wvOm7wOhrH0bj2yupvkE3-XFSv8jkMg4ZSWw7nZqMmAm5vTYIIeuQxLEqfEBuOCfq4b8z2EyTmWxdGYZFoGWWugWPsP5EFxvtPHCw5az140zEsgbxJF58zwsLzT_jfbhcpnlh3cDAoyFs23JlcZXXKRbwBO3JKCU-TTB4PF5tHHu5wOGRGHWOZ5TYnCZm0NFbeJ_Nr3ct_vRhRAexAZNx5WWS-aqkBFNi5V_erVbafkRKdJ0n21e7k49MWVQgpOOU13VDNfEZlcvCCRL502XRtrIGd3dbxkaoEU0t-yVZDFdH9QEE5bTeMOgI6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی گسترده در مجتمع تجاری در خیابان الظلالِ بغداد
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/447193" target="_blank">📅 20:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447192">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa5b2b7dd7.mp4?token=pxQnw4jZz1d8-nou97v_aAR-QYl8dj4wXwoHfaePuRLhxHhM1-aw8OpuGu2jjYM4A3893qGmV03KgkTflKIsnr0bR5Qr6MxTqIDL_H5ONNJnRWLx-66CVj9LwI72ZxCkgoQJBc1ESAiYw6dDHL4FvaD6SVLLBgz25d0NaMJi_wWIFfAwupR_39m8SsNU-8YNeCz3N0qcoQl2WpPs04WbwX08xr9KIqqbj3BV7h4FS4u6GbTgTcBMe7S_R6elbWmGBT4eEwiZlgo0BUL64Vj4e49NHk74PWMO1E67d6J9f3RSmvzRQgKIz_lx3xscAkr7aRcVEprkLJi7CHLlrl4j_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa5b2b7dd7.mp4?token=pxQnw4jZz1d8-nou97v_aAR-QYl8dj4wXwoHfaePuRLhxHhM1-aw8OpuGu2jjYM4A3893qGmV03KgkTflKIsnr0bR5Qr6MxTqIDL_H5ONNJnRWLx-66CVj9LwI72ZxCkgoQJBc1ESAiYw6dDHL4FvaD6SVLLBgz25d0NaMJi_wWIFfAwupR_39m8SsNU-8YNeCz3N0qcoQl2WpPs04WbwX08xr9KIqqbj3BV7h4FS4u6GbTgTcBMe7S_R6elbWmGBT4eEwiZlgo0BUL64Vj4e49NHk74PWMO1E67d6J9f3RSmvzRQgKIz_lx3xscAkr7aRcVEprkLJi7CHLlrl4j_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
برنامۀ وداع در مصلای تهران به‌دلیل ازدحام جمعیت تا ساعت ۲۲ تمدید شد.  @Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/447192" target="_blank">📅 20:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447191">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c554448e2a.mp4?token=mVgvuWNU8ZVNe_OHP1PGvfia4uk8nHvowjxZG4-xxPhg_YZnbu27O2rz7X9FrF9WdSgaO7mnywhs8NQJcN8VgfDKpe_SLUqlJOewSsh8ZbqqrxK0QxofDY5bqjQ4aelwXa0nqxxrACcgGp-iwRJ72dnkLKW3cN_HuSs7V1RY77n0aC0E6Sud2UKnqAbjc-XQH8wh68JCTeXI5524lAbUcOPWRI3U1Ul6PoftTAHRtNDR6CsBYMqK-z54cnC-vzgc3bHuEHaqugzN9vrit1G5c6Wd38ra8Vj47Aaf-UUGuUo6UNYWez5b-DIBP1HsUKrCr8kywR07gcAmYrzAvNrHXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c554448e2a.mp4?token=mVgvuWNU8ZVNe_OHP1PGvfia4uk8nHvowjxZG4-xxPhg_YZnbu27O2rz7X9FrF9WdSgaO7mnywhs8NQJcN8VgfDKpe_SLUqlJOewSsh8ZbqqrxK0QxofDY5bqjQ4aelwXa0nqxxrACcgGp-iwRJ72dnkLKW3cN_HuSs7V1RY77n0aC0E6Sud2UKnqAbjc-XQH8wh68JCTeXI5524lAbUcOPWRI3U1Ul6PoftTAHRtNDR6CsBYMqK-z54cnC-vzgc3bHuEHaqugzN9vrit1G5c6Wd38ra8Vj47Aaf-UUGuUo6UNYWez5b-DIBP1HsUKrCr8kywR07gcAmYrzAvNrHXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما برای وداع نیامده‌ایم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/447191" target="_blank">📅 20:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447190">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5ebf4ec7.mp4?token=qwP9Hg7n3xhP-kP1BBmkaCbY2etJU_zxocmDL-L0tbLmUCFz5EgFW3or00lJ5cjBJfDOLGEpfKfTIOKUwkLgCf2-NxoF4C05cojptvjGEuEsS4FirQ41CRK54qG-3cO-xBrquO9FKiydpYIpwuXW4tA4eLw91gYBeMaO-9RELKKOPOn5vbuqOVsLNenH0LwGZTG1etOn6RmIgZv7nRzV-ntfhDm0s5WQrE8Gi9Lf4okhVVNj8zrCLsu_p4esMCoe3beu6mh_ozk1_YMKsxFtKNe2HERURBdt07v_7w23_AxiBTu_GnM1DfejVUr5p20LxOseLvrKWTNCLT5629AIXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5ebf4ec7.mp4?token=qwP9Hg7n3xhP-kP1BBmkaCbY2etJU_zxocmDL-L0tbLmUCFz5EgFW3or00lJ5cjBJfDOLGEpfKfTIOKUwkLgCf2-NxoF4C05cojptvjGEuEsS4FirQ41CRK54qG-3cO-xBrquO9FKiydpYIpwuXW4tA4eLw91gYBeMaO-9RELKKOPOn5vbuqOVsLNenH0LwGZTG1etOn6RmIgZv7nRzV-ntfhDm0s5WQrE8Gi9Lf4okhVVNj8zrCLsu_p4esMCoe3beu6mh_ozk1_YMKsxFtKNe2HERURBdt07v_7w23_AxiBTu_GnM1DfejVUr5p20LxOseLvrKWTNCLT5629AIXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت «کالا والش» فعال رسانه‌ای آمریکایی از ابراز ارادت ۲۵۰ شاعر ایرانی به ایرانی‌ترین رهبر تاریخ
@Farsna</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/447190" target="_blank">📅 20:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447189">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMt-1kSf79d6Q7Ny0mKwXzZuRPK95RBfLeXayA9392eaf2Cek4pDF7Vzw2X4lW_FDh1ZcvIZuXO-H9hrjLxbsM09XkwwHxmooBtXo7Pw82dIKvwg2HA3SbVZ8JFpjr-KdeQqI6-P-DSYWMOURLbxB8rRC42dd6fEMdSInNsJeQmQm7mvnmFczFYwnN1_GWQJ-0VFZfCqcHjg7OXbLlYwFMTXPEB9LddAwZKvn6WaZ96O3f4oKvyXz3fUQRI2uCLJcBPshp-CILDJ4FvJvyYpJHb5cUPxAK1qr9quh6gKZ31UAzzrF0CGsIPk8EZ-vEMGM5_qR2X1nrA5QDdR-N_OYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تشییع رهبر شهید در قم
🔹
کمیته اطلاع‌رسانی مراسم تشییع رهبر شهید در قم: مراسم از ساعت ۵ صبح روز سه‌شنبه ۱۶ تیرماه با اقامۀ نماز بر پیکر مطهر در صحن مسجد مقدس جمکران آغاز می‌شود.
🔹
پس از آن، مراسم در بلوار پیامبر اعظم(ص) و مسیر منتهی به حرم مطهر…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/447189" target="_blank">📅 20:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447188">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v56tesAjcQVpj23rsEUZ9YgC2U29ZcYO8qEZ3YJ2Jd7xQ-0O2durMy4bXb9TMt__CXKIYj5h2xUlc2Aa8CQ53lI7N0JK4YbAzbSP8qBmFwV0rLjEHDGK96jBcot58jkJZDH8pMvfcnfLsWDwd19tafSIlww6aofB_niDCvEePEsJhXoGjxmwJ1bcx3rp5r5tcYNnog-7z9rT2Nzo4cUhtfAmZrKluSsmuozRRf0YSnQWxW0dbMnU2mU-RmXnmvE1f_G1yRGDdenDQsc2lZjVTXmzI28iFM-aDeWhbeYGUh5Btpo4U-dz1PQxBmNLZpIeIKVqZwi0je3fCqbRSFRoFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ننگا به‌ ما اگرکه ز خونت گذر کنیم
@Farsna</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/447188" target="_blank">📅 20:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447187">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f43e570ac5.mp4?token=VwbfyWlct2M0-mvt_HagXJO9nNqzOZ-E8CXqPJcptXbIBKXxzfJJ7ECR9Km755952f9YsDHV2DMw_RmWTJxcEDU9JOpBLo8faHBKaSFZpEoZnzQOxKHqP6Ye60S3O3VQfdrY4SR24IpsW58yUkS8-MYMcx01FpgTjwSQ1qmkpNYHGbvzisYo4lU5ZmKAeWvKkg1VqVly5I5o3bens8-N9grEbep7hzEj7P_ZR2EN1QeWuKlzzGL4DLnYg6A2sJgt13XcXNkVCOwCjcjIMDnwdTV9j9y06EC3Cawrx5CiWgYuXSPqppKW2fmRNbQarvd8VRDeyLD8RbG9s4oubtyNtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f43e570ac5.mp4?token=VwbfyWlct2M0-mvt_HagXJO9nNqzOZ-E8CXqPJcptXbIBKXxzfJJ7ECR9Km755952f9YsDHV2DMw_RmWTJxcEDU9JOpBLo8faHBKaSFZpEoZnzQOxKHqP6Ye60S3O3VQfdrY4SR24IpsW58yUkS8-MYMcx01FpgTjwSQ1qmkpNYHGbvzisYo4lU5ZmKAeWvKkg1VqVly5I5o3bens8-N9grEbep7hzEj7P_ZR2EN1QeWuKlzzGL4DLnYg6A2sJgt13XcXNkVCOwCjcjIMDnwdTV9j9y06EC3Cawrx5CiWgYuXSPqppKW2fmRNbQarvd8VRDeyLD8RbG9s4oubtyNtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین اذان مغرب در مصلای امام‌خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/447187" target="_blank">📅 20:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447185">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb6d485518.mp4?token=PVeeZxdhwWsb9xC__XnePIfFLVX0G9Sdtuql3MMUQNKX4SGDUgVuMnR6NiaMKYROJJsSvtSiJBNLYq4YBG6bgYqI_4fdudYC7n6tk5PLDj7gsqlU2sqOabEFv0WyGXy5spNTGGZMUqlqC9E2PLnutFY2VE7qpGSQMOWRdz65j66bvmYzKkgmloLi_HduMHgnu77X6-_sQAhU-ntx5EzXv0LokPHprjub8dqaanDHn-5veOwWWx9-50VdBNJRjJeropLnBGUc9QX0vk01wNeFx8NMtpfsmXatBipI1pbUO90hH-AACviZVtGdsu8TdOAZPyZm_Teo9CsuyCC_PUBotA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb6d485518.mp4?token=PVeeZxdhwWsb9xC__XnePIfFLVX0G9Sdtuql3MMUQNKX4SGDUgVuMnR6NiaMKYROJJsSvtSiJBNLYq4YBG6bgYqI_4fdudYC7n6tk5PLDj7gsqlU2sqOabEFv0WyGXy5spNTGGZMUqlqC9E2PLnutFY2VE7qpGSQMOWRdz65j66bvmYzKkgmloLi_HduMHgnu77X6-_sQAhU-ntx5EzXv0LokPHprjub8dqaanDHn-5veOwWWx9-50VdBNJRjJeropLnBGUc9QX0vk01wNeFx8NMtpfsmXatBipI1pbUO90hH-AACviZVtGdsu8TdOAZPyZm_Teo9CsuyCC_PUBotA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم | لحظه ورود رهبر انقلاب به حسینیه امام خمینی(ره) در مراسم عزاداری شب عاشورای حسینی  @rahbari_plus</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/447185" target="_blank">📅 19:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447184">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67407e3e61.mp4?token=vbfuV9BBV54MLxbhM29F-8jwUqrl2Asvo2OZ9diG9n20f4IaQQIhG4-eNtD4bz4agm8-kcnm_dOyIcJxzWCgMKtk5374breKEEmvQY6eG8fvsRYtNsL7KHCnI0hNf_wnOG6O8rFJQornBFC9qBjTaTBet6k9Euv3oGOcfB-4MkAZR2CiRku5kFc4zmjISEecs6_i9sQcLtTkMVOexqsDAVyH845L_DhxXPa81WoiZUyzm0TTLs80lOzr3J6IhBqgVKPTQlgKFAJ_K94j6QEk2oSbsrZ5-nPRNLHUIkFilqI4v6gSgoMbH6lqppZ7_uPMx1-JOxI-P94GWUrFsQriUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67407e3e61.mp4?token=vbfuV9BBV54MLxbhM29F-8jwUqrl2Asvo2OZ9diG9n20f4IaQQIhG4-eNtD4bz4agm8-kcnm_dOyIcJxzWCgMKtk5374breKEEmvQY6eG8fvsRYtNsL7KHCnI0hNf_wnOG6O8rFJQornBFC9qBjTaTBet6k9Euv3oGOcfB-4MkAZR2CiRku5kFc4zmjISEecs6_i9sQcLtTkMVOexqsDAVyH845L_DhxXPa81WoiZUyzm0TTLs80lOzr3J6IhBqgVKPTQlgKFAJ_K94j6QEk2oSbsrZ5-nPRNLHUIkFilqI4v6gSgoMbH6lqppZ7_uPMx1-JOxI-P94GWUrFsQriUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ساخته‌شده با هوش مصنوعی از چهره‌ها و صحنه‌های خاص و غیرمنتظره مراسم امروز وداع با رهبر شهید انقلاب در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/447184" target="_blank">📅 19:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447183">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjep0KPlwOUdVV_xKMJ2o1QQThwEWjKtxXEa4vQoMvPOmmdIM7o59wtBsEOSGwtCi70ivyMSIZFhZLRzIy0pBhUnnanQ52X935h6HygGBw1Wv15sHY7OcdRR51grbETs0AzWu3ZrdGdklQgW3sncPcW4xJVmXbQDc2D6Ogr-qh4KsU0UYLAZ9-cCe4WUwZW80aYXcQ_E_zMGfxYSKbOfdzg1SMei7Imay8zrUguoXagXCVoclcbvr3rjGQVuIcmDg8gUqszDM2z5ldvkqPsys1j_cNRcvBG_ojq1yzz5JIzrZTuRGMceF2LZMyj_sEpj7B7h_Avk1f49kQzk7JTHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
بازدید مدیرعامل بانک رفاه کارگران از موکب های این بانک و شرکت های تابعه در مراسم وداع با پیکر مطهر قائد شهید
🔹
مدیرعامل بانک رفاه کارگران با حضور در مراسم وداع با پیکر مطهر قائد شهید، از موکب های این بانک و شرکت های تابعه در این مراسم بازدید کرد.
🔹
دکتر للـه‌گانی به همراه جمعی از مدیران و کارکنان بانک ضمن حضور در این مراسم در محل مصلای امام خمینی(ره) تهران، از نزدیک در جریان خدمت رسانی این موکب ها به عزاداران قرار گرفتند.
🔹
مدیرعامل بانک رفاه کارگران طی سخنانی در حاشیه این مراسم گفت: اندیشه‌های رهبر شهید یک جهان‌بینی مبتنی بر کرامت انسانی بود. ایشان همواره معتقد بودند که اقتصاد، ابزاری است برای تعالی جامعه، نه هدفی برای انباشت سرمایه. بانک رفاه به عنوان بانکی که نام «کارگران» را بر پیشانی دارد، بیشترین قرابت را با گفتمان ایشان دارد.
🔹
دکتر للـه‌گانی تصریح کرد: در بانک رفاه کارگران تلاش کرده‌ایم آرمان‌های قائد شهید را به دستورالعمل‌های اجرایی تبدیل کنیم. از حمایت از تولید ملی و اشتغالزایی گرفته تا طرح‌های رفاهی برای کارگران و بازنشستگان. این‌ها در واقع پیاده‌سازی همان نگاه کلانی است که ایشان به عدالت اجتماعی داشتند.
🔹
وی به انتخاب حضرت آیت‌الله سیدمجتبی خامنه‌ای (حفظه‌الله) از سوی مجلس خبرگان رهبری به مقام رهبری انقلاب اسلامی، اشاره کرد و گفت: این انتخاب نویدبخش تداوم مسیر عزت و اقتدار میهن عزیزمان است. بدون شک شبکه بانکی تمام توان خود را برای تحقق منویات رهبری در مسیر اعتلا، آبادانی و شکوفایی اقتصادی میهن عزیزمان به کار خواهد بست تا تحت عنایات حضرت ولی‌عصر (عج)، شاهد سربلندی بیش از پیش ایران اسلامی باشیم.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/447183" target="_blank">📅 19:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447182">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/447182" target="_blank">📅 19:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447181">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5764e1d53f.mp4?token=vwLvIqEfIGTcT8tUy0Iw3TIQjXEYcQcvNIG5WrYpsWomG1IBkI_yUPzcVR5lzjvIIU1TEbxUnq6LCAbjA9V4y6l7VVBY74FSwVYOdYl99Luzqpg8mruVzh69avJFR2e6vM4i280pgMq2yTHLJ9uCKW1mxRdXKC5KeMuASXPx_e_7o5fwZBB3gyNMpOzF3oonGEhLe91OyfDpS2VEjyXL0T9NE3b0UKKdJ1qd-xQBy51xCoN4DHO9AbUK1z8LdsSqnyzDWl2-DBmMCm9c0k2L2eNPiApb-2vz7BzDBcNrV2Yi26HtsVUKPcOWCVkWV-hlYrJ1Ybrsn426hsliVt5Ddg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5764e1d53f.mp4?token=vwLvIqEfIGTcT8tUy0Iw3TIQjXEYcQcvNIG5WrYpsWomG1IBkI_yUPzcVR5lzjvIIU1TEbxUnq6LCAbjA9V4y6l7VVBY74FSwVYOdYl99Luzqpg8mruVzh69avJFR2e6vM4i280pgMq2yTHLJ9uCKW1mxRdXKC5KeMuASXPx_e_7o5fwZBB3gyNMpOzF3oonGEhLe91OyfDpS2VEjyXL0T9NE3b0UKKdJ1qd-xQBy51xCoN4DHO9AbUK1z8LdsSqnyzDWl2-DBmMCm9c0k2L2eNPiApb-2vz7BzDBcNrV2Yi26HtsVUKPcOWCVkWV-hlYrJ1Ybrsn426hsliVt5Ddg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رهبر شهید از آخرین دیدار و وداع
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/447181" target="_blank">📅 19:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447180">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9f3b783ad.mp4?token=VPAOK2NCmIro_XW_Ty_hWG-33957ACx1nDhFtVwfgvSVQb9bQIGHz2dg0SbBk50zRMN5QNib0J46bGUV8VmAyuafe_-bEVJEE98UuE-80v4w_I18kVyJe35wyfD9jX_auklpTYySCgW5k_zXlYg--D9zjTdK0CNSGrPxuexIfTVTQtcvqAkc9ikeYRc6Vdg-2Zz5gBSzj5l0lXzqksTmx-i_JpM0-iun1nbYkLpaquNHwhXTCpThsgHmhvD7Ga_iCSGqGvgUKEgKgiVyK23PbQnjz_LFF1ncAvhN16sb69EV__qwUDf6rY2N3NUKyRg7Z32eUhUYZIedUSuUwFgNuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9f3b783ad.mp4?token=VPAOK2NCmIro_XW_Ty_hWG-33957ACx1nDhFtVwfgvSVQb9bQIGHz2dg0SbBk50zRMN5QNib0J46bGUV8VmAyuafe_-bEVJEE98UuE-80v4w_I18kVyJe35wyfD9jX_auklpTYySCgW5k_zXlYg--D9zjTdK0CNSGrPxuexIfTVTQtcvqAkc9ikeYRc6Vdg-2Zz5gBSzj5l0lXzqksTmx-i_JpM0-iun1nbYkLpaquNHwhXTCpThsgHmhvD7Ga_iCSGqGvgUKEgKgiVyK23PbQnjz_LFF1ncAvhN16sb69EV__qwUDf6rY2N3NUKyRg7Z32eUhUYZIedUSuUwFgNuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاضر بودم ١٠ بار بمیرم اما یک تار مو از رهبرم کم نمی‌شد..
.
@Farsna</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/447180" target="_blank">📅 19:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447179">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ca1bcfcdc.mp4?token=hMlybOekSZkO1dXq2XGmFsKwW4n8dfRa0QJshjDoEETV6OKLjzTDDRhCVXLBPReGClNyb4ADq1ZRwh5qJDjJcj6TumWC7nuUTFF7ZMovyC9iYCue0k57bRh3aEchcxgdzjMwvy0Xe0NyoDmT2Y0vCON5_yixDMRDrq5OrmX-JCMLShqvQi1iRhkbD-IL3zTJFi0Yuqm1yJgeN-jFciqhw5HhZbDZWAjmwvSp0Zb89pDZdYKWSX0sC7AyCeua3O2PWz_tH46Lqb6IyD3SyLjgXO3YZnBHLeNnS3GUuV35e0Cvp2cAHBfUXv80sxK64bN-GQeS0-wsk87J5a5pVvzTgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ca1bcfcdc.mp4?token=hMlybOekSZkO1dXq2XGmFsKwW4n8dfRa0QJshjDoEETV6OKLjzTDDRhCVXLBPReGClNyb4ADq1ZRwh5qJDjJcj6TumWC7nuUTFF7ZMovyC9iYCue0k57bRh3aEchcxgdzjMwvy0Xe0NyoDmT2Y0vCON5_yixDMRDrq5OrmX-JCMLShqvQi1iRhkbD-IL3zTJFi0Yuqm1yJgeN-jFciqhw5HhZbDZWAjmwvSp0Zb89pDZdYKWSX0sC7AyCeua3O2PWz_tH46Lqb6IyD3SyLjgXO3YZnBHLeNnS3GUuV35e0Cvp2cAHBfUXv80sxK64bN-GQeS0-wsk87J5a5pVvzTgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین قول‌وقرار حسین یکتا با رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/447179" target="_blank">📅 19:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447178">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4wO8b8Pb8RwUt8RUt6gyaRYjozdFEMKa6VVnH70A-tFaVjvnp6WV9s5QXA9yrWgPswng4Ybo7k-JiJw_d4tYRQ6mhuP7SsiDnWllMJdOKje0BWQMWXUojNTSlI0EzBEoEKmS3sQtzDt9-0krZo2_63xG5vof24Fe9iviPVqrfqA9Db8WCEGo1V-eiuSqL4Ht0osqRoNKzt6YJNExULJTPw8yyBbc3IcGMMKzeFL0PS6loO9q5KdsiF6cumY4w9lMOI4GMgYoL4H3ynw3L05seo0NH_hrgpQpTt-R-ucg6z82lycBSt3TwRV1H3JSO9PletWzsNO2OK90j33FEmbqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتصاب مجدد حجت‌الاسلام والمسلمین اژه‌ای به ریاست قوه‌قضائیه
🔹
حضرت آیت‌الله سیّدمجتبی خامنه‌ای رهبر معظم انقلاب اسلامی در حکمی، حجت‌الاسلام والمسلمین محسنی اژه‌ای را بار دیگر به عنوان رئیس قوه‌قضائیه منصوب کردند.  متن حکم رهبر انقلاب اسلامی به این شرح است:…</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/447178" target="_blank">📅 19:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447177">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
برنامۀ وداع در مصلای تهران به‌دلیل ازدحام جمعیت تا ساعت ۲۲ تمدید شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/447177" target="_blank">📅 19:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447176">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یک استان دیگر عراق روز چهارشنبه را برای بدرقه و تشییع پیکر رهبر شهید ایران تعطیل کرد
🔹
استان مثنی عراق، نهمین استانی است که روز چهارشنبه را برای تسهیل مشارکت مردم این استان برای بدرقه و تشییع پیکر حضرت آیت‌الله العظمی سید علی خامنه‌ای، رهبر شهید ایران تعطیل…</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/447176" target="_blank">📅 19:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447172">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2ikqEI2Zgav3TABhPr8Exre2soVAevZjpA3Y70V0F9m8pCpplaVkJOQnBc-Dja56M9xZns0-SeiNZuH-FXNlV9awKlWyErTDEnl9cBv2m09JPcJUe0Hm6n0oPd_AYUeG2r9T_U9bfDy8wsxelzBjGvTY_4ENvnsG5JiSKwHjog92pJl9qKSjct337hAR4IYwXSCNfG914Pu5jqkgS7-TG5oJsOwVlzaui5OJF_y_nU3fE_qc9OHlRyptROLvdbnqA0OlsALrstXkudHFDwOWKA3SwdgVkOxl22DJUU52wm9ZKAUt8ElgM-5v1uHdMBl30ZWHR-1XVZLpgI4iszy8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتصاب مجدد حجت‌الاسلام والمسلمین اژه‌ای به ریاست قوه‌قضائیه
🔹
حضرت آیت‌الله سیّدمجتبی خامنه‌ای رهبر معظم انقلاب اسلامی در حکمی، حجت‌الاسلام والمسلمین محسنی اژه‌ای را بار دیگر به عنوان رئیس قوه‌قضائیه منصوب کردند.
متن حکم رهبر انقلاب اسلامی به این شرح است:
بسم الله الرّحمن الرّحیم
جناب حجت‌الاسلام والمسلمین آقای محسنی اژه‌ای دامت توفیقاته
🔹
با قدردانی از تلاش‌های ارزشمند و صادقانۀ جنابعالی، به استناد اصل یکصد و پنجاه و هفتم قانون اساسی، جنابعالی را به ریاست قوه‌قضائیه منصوب می‌کنم.
🔹
مجموعۀ مطالبات مطرح‌شده از سوی قائد شهیدمان اعلی‌الله‌مقامه‌الشریف و نکات مذکور در پیام هفتم تیرماه ۱۴۰۵ اینجانب، راهگشای تحول، شکوفایی و دستیابی به قوه‌قضائیۀ مطلوب است.
🔹
امیدوارم با همت مضاعف جنابعالی و قضات شریف و همکاران ارجمندتان در دستگاه قضایی و دعای سرورمان عجل‌الله‌تعالی‌فرجه‌الشریف، ملّت بزرگوار ایران از نتایج آن بهره‌مند شوند.
سیدمجتبی حسینی خامنه‌ای
۱۳/تیر/۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447172" target="_blank">📅 18:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447171">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571f3614bb.mp4?token=dTvisllvuiE9TJFUqmQSVUMALfkmNZwGWktPXsdxpBfN5so7NCcd2HhJQgywmVANxk3qGpvypl6b2BVVs_1kBnQkv1Kkmo8CIf0jfQ_XNGOHPG9CwXGKzUOT1b7GyVvn2NHiLuQ0xNdcqMS6z0ncaYd16V3BuSrBA1HO9YFBGFGzuZBepCn8d044LanbTa-Sq73J04V6asyrkUPHU3IYHjiLegYDKlcOGuOwoimHPwzK1i0MGsiSc-4xlnxuOebxJTvwPVBsmBBEnMs8FQmh3cPSUf5aWkas_6cuuX_Y7px07HM08mHZ4lx2jX-rmx04dK0cau7dZxDGetWdguRhhbIukRvdamQFuPti331JPEcU86VgeVODNlghjYT8NyBrCvvAfHdGdX7dSRysri00khgh_-_2uCs9gN6uffLetnSEZhpi5Np4xl8FaeY0ydVSpR3eJSLNSBMAaUpAMEKCu4kQZd70UsgRMnJ4UBJtZ6kUkAMThxDPe1qD0qug11WE8s_NG4uNBRjuJMKPJ0J3rtbB7HCdjykitLcwE8hozMDSeTWHJ5_2zWJHuBfh3-7DiB4H1wcttBWUIZAAkjYWHl1wDK4XmjPCpzN0aXTcOQF-7JEdx9FTHsPydJO3JjQ9APE51SbXG1OO9rfU_ukpqJRYVZPxXm9jYuc551tu0qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571f3614bb.mp4?token=dTvisllvuiE9TJFUqmQSVUMALfkmNZwGWktPXsdxpBfN5so7NCcd2HhJQgywmVANxk3qGpvypl6b2BVVs_1kBnQkv1Kkmo8CIf0jfQ_XNGOHPG9CwXGKzUOT1b7GyVvn2NHiLuQ0xNdcqMS6z0ncaYd16V3BuSrBA1HO9YFBGFGzuZBepCn8d044LanbTa-Sq73J04V6asyrkUPHU3IYHjiLegYDKlcOGuOwoimHPwzK1i0MGsiSc-4xlnxuOebxJTvwPVBsmBBEnMs8FQmh3cPSUf5aWkas_6cuuX_Y7px07HM08mHZ4lx2jX-rmx04dK0cau7dZxDGetWdguRhhbIukRvdamQFuPti331JPEcU86VgeVODNlghjYT8NyBrCvvAfHdGdX7dSRysri00khgh_-_2uCs9gN6uffLetnSEZhpi5Np4xl8FaeY0ydVSpR3eJSLNSBMAaUpAMEKCu4kQZd70UsgRMnJ4UBJtZ6kUkAMThxDPe1qD0qug11WE8s_NG4uNBRjuJMKPJ0J3rtbB7HCdjykitLcwE8hozMDSeTWHJ5_2zWJHuBfh3-7DiB4H1wcttBWUIZAAkjYWHl1wDK4XmjPCpzN0aXTcOQF-7JEdx9FTHsPydJO3JjQ9APE51SbXG1OO9rfU_ukpqJRYVZPxXm9jYuc551tu0qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دانشجوی نیجریه‌ای: مردم ایران دمتون گرم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/447171" target="_blank">📅 18:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447170">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa5a4fb9d.mp4?token=f4X9NVxRD8UwxbBnbsdksBcDpwuavotzKm0NxUF6DSCKhtdXtMqjg8e5j3qWlzxmUEmsuJ1WW8ejCE5Jis8e-ll2OvqBzP-wZ1Nnxwqm_Ci5mW8N8Rz226bYNONQ1acBevgJblg7_G9pbkcvBQD5ZqG-5Dmcilh0vpptJc-GfnYZuGRuYSPrfBoRXFUQhmv0Wk8tnKAOsg4mxcd6yyyu3sOqlsd_1VPDVql_6V22jmKGuTr_AxhHWySFqupIaKQvJeFla5cD4ktNZtxUSL9jix8DUlo7ALKntAL12G85tElEJBhWVRAl7-SY2XK2QYY4xQExF2X6w8SqwHyNUDRznQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa5a4fb9d.mp4?token=f4X9NVxRD8UwxbBnbsdksBcDpwuavotzKm0NxUF6DSCKhtdXtMqjg8e5j3qWlzxmUEmsuJ1WW8ejCE5Jis8e-ll2OvqBzP-wZ1Nnxwqm_Ci5mW8N8Rz226bYNONQ1acBevgJblg7_G9pbkcvBQD5ZqG-5Dmcilh0vpptJc-GfnYZuGRuYSPrfBoRXFUQhmv0Wk8tnKAOsg4mxcd6yyyu3sOqlsd_1VPDVql_6V22jmKGuTr_AxhHWySFqupIaKQvJeFla5cD4ktNZtxUSL9jix8DUlo7ALKntAL12G85tElEJBhWVRAl7-SY2XK2QYY4xQExF2X6w8SqwHyNUDRznQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در پناه اباعبدالله، زائر کربلا
◾️
نوحۀ وداع سیدمهدی حسینی برای رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/447170" target="_blank">📅 18:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447169">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08b7196f32.mp4?token=mS2YULWkSRLoBaVSaRcGwCbD9YZmdAC-CEcC48l5WZDuGwoLHYHQpm726a73EC36wXmDUw8JsV7TLVHGcW3t0BREYcMalF94GC2GtEzJAuLrJhmrvIqJymCnylv2Gh4HjvB2EwoNSZV6KhZm6dm_XEIy3Tp9BXxiUU1Dz7TXo9UdrKjnJ48BbDi4-TDSI3kOrOdA4ZaeEnyfbIn1-FtveA-unab8zYuJzB1052Y9MxpEHMmcKBzP0YIj8-F2AdiRwMZC02toOuu7e7GHuU2Poj63JO8JsWLSMT8G-IdhPfNXddFwvJuyRA-5NDWEJJLzL4gwPMD4hQfvQTz5IyR05g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08b7196f32.mp4?token=mS2YULWkSRLoBaVSaRcGwCbD9YZmdAC-CEcC48l5WZDuGwoLHYHQpm726a73EC36wXmDUw8JsV7TLVHGcW3t0BREYcMalF94GC2GtEzJAuLrJhmrvIqJymCnylv2Gh4HjvB2EwoNSZV6KhZm6dm_XEIy3Tp9BXxiUU1Dz7TXo9UdrKjnJ48BbDi4-TDSI3kOrOdA4ZaeEnyfbIn1-FtveA-unab8zYuJzB1052Y9MxpEHMmcKBzP0YIj8-F2AdiRwMZC02toOuu7e7GHuU2Poj63JO8JsWLSMT8G-IdhPfNXddFwvJuyRA-5NDWEJJLzL4gwPMD4hQfvQTz5IyR05g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدرقهٔ ۲۵۰ شاعر پارسی‌گو برای ایرانی‌ترین رهبر تاریخ
@Farsna</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/447169" target="_blank">📅 18:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447168">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33d6aad76b.mp4?token=Stz3eb2lAYeMqwWIRUAmixZoyOptoPOH5zVnGbImoiYtwZ1tBXkY8jPHmmnbZeh4m-G62KOU8Z5m6C-iSkRTl6KiJ4GK09zSv1QFi6m6dzBMRo25ej06iRAq6Vz2UlEUt1jEEvZzhaUP4mBDZeYWFHTxq0mhoBlTF656o2hhlj5yi7rqsn7afQ2bSDIC1f7bpyIck6tDHI83ZhpwXJiDj1pvLTryIMw3DUQGwY8tgnfnQddvc3_DMxbv3FiadXvMWFHlt7dhI67CWnpcEqPWxbmfwi_ZEwQ8ydDRnHwtjCqpOdIshFtVxvizfhfzFLpCCzEuwBqjX2nrFbfskhHdSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33d6aad76b.mp4?token=Stz3eb2lAYeMqwWIRUAmixZoyOptoPOH5zVnGbImoiYtwZ1tBXkY8jPHmmnbZeh4m-G62KOU8Z5m6C-iSkRTl6KiJ4GK09zSv1QFi6m6dzBMRo25ej06iRAq6Vz2UlEUt1jEEvZzhaUP4mBDZeYWFHTxq0mhoBlTF656o2hhlj5yi7rqsn7afQ2bSDIC1f7bpyIck6tDHI83ZhpwXJiDj1pvLTryIMw3DUQGwY8tgnfnQddvc3_DMxbv3FiadXvMWFHlt7dhI67CWnpcEqPWxbmfwi_ZEwQ8ydDRnHwtjCqpOdIshFtVxvizfhfzFLpCCzEuwBqjX2nrFbfskhHdSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت یک سلام برای بدرقه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/447168" target="_blank">📅 18:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447167">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjdN9IYlc3YtEW2Qw8n_Cr6dvT7euaHx3bWEHu4Vc1mR5oF24bx7jYc-PCEI-PHgMvZmpHUkViqASQhHQqRygsAdPWgJzGwVtj9Uxf2jvJtFDOi0GTxDM28HLzyyivddQH9ZIxJqcFxEMFoazEVwx7JMxWk4J8I3MdCELP8DFLAu0NCKb-w_X9CEqak0dFs7h6AUC8qPCNogMc-T100FkqI-KyXtnW1JtgpCVrfNclg75AYo9tCC7NIZRyANj0Fx2g3xKj7l2NVDGzRMXuqrTkQzuv8PlFtwtkmDmkVKupysBjT6YwfM-3sZap-FQ_DVkR-MR97-_Eips8OvXOzOCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
آیت‌الله عاملی: شرکت در تشییع رهبر شهید به منزلهٔ کشیدن دندان طمع دشمن آمریکایی-صهیونی است.
@Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/447167" target="_blank">📅 18:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447164">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خروج ۱۱ فروند سوخت‌رسان آمریکایی از غرب آسیا تأیید شد
🔹
هم‌زمان با انتشار گزارش‌هایی دربارۀ کاهش بخشی از توان پشتیبانی هوایی آمریکا در منطقه، برخی تحلیل‌ها این تحول را ناشی از بازنگری واشنگتن در ارزیابی خود از تاب‌آوری جمهوری اسلامی ایران و واکنش‌های احتمالی تهران پس از نمایش گستردۀ انسجام ملی در مراسم تشییع رهبر انقلاب می‌دانند.
🔹
درحالی‌که گزارش‌هایی از کاهش بخشی از ظرفیت پشتیبانی هوایی آمریکا در منطقه، از جمله خروج تعدادی هواپیمای سوخت‌رسان، منتشر شده است، برخی ناظران معتقدند این اقدام می‌تواند نشانه‌ای از تغییر محاسبات واشنگتن باشد. یک منبع نظامی به فارس گفته است خروج دست‌کم ۱۱ فروند هواپیمای سوخت‌رسان آمریکا از منطقه تأیید شده است.
🔹
عبدالرضا صدیق، کارشناس حوزۀ نظامی، معتقد است آمریکا پس از دقیق‌تر شدن ارزیابی‌ها از پایداری و تاب‌آوری مردم و نظام جمهوری اسلامی و دریافت گزارش‌های متعدد از حضور گستردۀ مردم در مراسم تشییع پیکر رهبر شهید انقلاب، دستور عقب‌نشینی داده است.
🔹
به‌گفتۀ این کارشناس نظامی، آمریکا پس از دریافت گزارش‌های متعدد از خشم گسترده و کنترل‌ناپذیر مردم در مراسم وداع با پیکر مطهر رهبر انقلاب، نگران واکنش احتمالی ایران شده و در صدد کاهش تجهیزات گران‌قیمت خود از منطقه است.
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/447164" target="_blank">📅 18:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447163">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374c4ece7c.mp4?token=XTd4w2sRsyz8YWrRY8c_AMJqdmPC6LCmU4Y-R8ZAoH79w2JwGfUAiOH-_n9k_ecmvESl9QbjOY7N4144MvaVexYS656bPI0OSprxP34UEmACu-2kSBfmF8DTp4foFn65d9EJjwX0Zrd3VYwJJP_pDAfZEmbg2MEjHDZwZ6GQNY1Bn2io7pxXnMh_febiRIc_qcX_sXejgij0XC3tZCjCr0ozH1y-4_TH90E2kHK10d7SJRndC_-RSAeWZgsK24Y4Hjcm2vXBlYxY_sbWAaCxxlRRw-R-brt2tu_eBr9_Tm1fc91OO4PPKezX6Z3lWZoaZmmjNY9ecYFGcCRAjyakUZQzp5KtORGjzn5E2LuupS2LvJ29jYwXvT6JRaSFfqdqMDkvatSFDrPDZrjKnFfBYSYrcrEgCySvxZl-aW8D_-7coXqET6jS9rMmeKU3SoP0ZB1EqftCNgoypGdHyS0ghglJ9iQq1nzm8hSX81LiYVHrD5CL8810zFUgC6O8KH8wKW6XUHCA8SBcpwEViVqr2DyVr5J4eV_0J6aKKeNHpbcvtZBn6EtOTpasjoJ-YWAA2xs9pi1HMN51JeDl6dRQuZsrFTSgPSsjXWcT-GYUOGCFuANTKi5bCgVR58wGv04bxC1CPtEPyjJrKz_9-2_6YYlasFn-bPcPKwYXxm3P3cc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374c4ece7c.mp4?token=XTd4w2sRsyz8YWrRY8c_AMJqdmPC6LCmU4Y-R8ZAoH79w2JwGfUAiOH-_n9k_ecmvESl9QbjOY7N4144MvaVexYS656bPI0OSprxP34UEmACu-2kSBfmF8DTp4foFn65d9EJjwX0Zrd3VYwJJP_pDAfZEmbg2MEjHDZwZ6GQNY1Bn2io7pxXnMh_febiRIc_qcX_sXejgij0XC3tZCjCr0ozH1y-4_TH90E2kHK10d7SJRndC_-RSAeWZgsK24Y4Hjcm2vXBlYxY_sbWAaCxxlRRw-R-brt2tu_eBr9_Tm1fc91OO4PPKezX6Z3lWZoaZmmjNY9ecYFGcCRAjyakUZQzp5KtORGjzn5E2LuupS2LvJ29jYwXvT6JRaSFfqdqMDkvatSFDrPDZrjKnFfBYSYrcrEgCySvxZl-aW8D_-7coXqET6jS9rMmeKU3SoP0ZB1EqftCNgoypGdHyS0ghglJ9iQq1nzm8hSX81LiYVHrD5CL8810zFUgC6O8KH8wKW6XUHCA8SBcpwEViVqr2DyVr5J4eV_0J6aKKeNHpbcvtZBn6EtOTpasjoJ-YWAA2xs9pi1HMN51JeDl6dRQuZsrFTSgPSsjXWcT-GYUOGCFuANTKi5bCgVR58wGv04bxC1CPtEPyjJrKz_9-2_6YYlasFn-bPcPKwYXxm3P3cc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار آفریقایی: باید بگویم ایران برای دنیای اسلام قاطعانه ایستاده است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/447163" target="_blank">📅 18:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447162">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b99a21b25.mp4?token=rIAwqZKJLisZB_PNw6ZvOoxhU92g4NgXkis1rCNnotYCRVXBS15nTeK5Nqle-fWCMQg9QippRiCR--u-96a8hQW9Is6XMde5zv8U4gefRRI0I5p0AaTHmgfXfJjFGAUJshwl2vS3uaePnwmO5qUHKGmTxl8KsGkMX7ontQrRhZNrdNm-MIpkxt56FpBsrpRt7Qiv7qFkQQmXDzkZ2rrS1aAXu1cGFJkWShjFdzsgX3J6tkWVBG1qprE3REy36szgR_hDQFx7h4Eiid9aXSy1CNWG11r4Mi-bL3UIBc7Zl0yPtk1prOQ9wu956BiE8nKvcddZJpZDLSZrV82PmcbjjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b99a21b25.mp4?token=rIAwqZKJLisZB_PNw6ZvOoxhU92g4NgXkis1rCNnotYCRVXBS15nTeK5Nqle-fWCMQg9QippRiCR--u-96a8hQW9Is6XMde5zv8U4gefRRI0I5p0AaTHmgfXfJjFGAUJshwl2vS3uaePnwmO5qUHKGmTxl8KsGkMX7ontQrRhZNrdNm-MIpkxt56FpBsrpRt7Qiv7qFkQQmXDzkZ2rrS1aAXu1cGFJkWShjFdzsgX3J6tkWVBG1qprE3REy36szgR_hDQFx7h4Eiid9aXSy1CNWG11r4Mi-bL3UIBc7Zl0yPtk1prOQ9wu956BiE8nKvcddZJpZDLSZrV82PmcbjjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ هوایی اسرائیل به جنوب لبنان
🔹
شبکهٔ المنار: ارتش رژیم صهیونیستی شهرک النبطیه‌ الفوقا‌ را در جنوب لبنان هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/447162" target="_blank">📅 18:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447155">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZcPjVFot6-0cq-muKRTOPEfApGpK80s6H58w2W2z0F38YSNvOCCcioCq0J2EoYi_Z0XJqhJo3yPalSHSOZLpqzOiyafzP7u6T9NQP3M1XlC99E1AY0HIwpH4S9j1d7vvqxDZSt9fnHxiYzwJR1RhLngkzKUIJM4pHvaj_leQSKnyaro18a8w7QcuMAn0PxR3AVSVuZNxsgvWzULAR_7foc1PvPYA5DeUWPxYToJZ9uza6YAhnHGSyBzQvhMhYllQ2-S_15zItXPN6MJRM9FRCQeGIyUbtb7m9yb2-RTU8oP-6qT9nVE8zyHaN0P173Jy7Y9pSvTZDWGcjTdYV-Q5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PlaFnoAlUgmSzDhiCidfgp1FeLZnbX8qT3xDMmk93urLujKes2EQ_4SF4TA0ZfAbOJwB0EVbTN4DSFh7vAEwXRWpdbAlleeMqSiWZB882KW9NRvoBwbwLtBHXix9kpPlOlYKm1arTfEB4RS14cBmU22XLUVuhIcBbTd1WhBv-bBdmrlqfQABRlXz4sSTZL0hC_Yjp7kMiuMiI6bI8JY4E4kt9-0ejcvkiF0vlOsAcAD8dKLsQbwRkM-FbOalhCn5W69vj2tytbJxarXsczNfn5FFTFlFFmS1LyEiJXdH_bXPUb-ug0qhL04UUBUAezlwemqCKo_8m3mN_5EDXhSdgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EBxoeDf5Zz-L9TwcQ82d7dRvrH3Pyyu9AhFzYp6uaJngyVJBxHedn-UCS3obAc9xQZqFZ4_AmmZksPFc6Ys_UGeJEB_pCkWRtHuFxmR5WJpSmovfn0ij_jqYbO9Rr1L9nou_pdKiLg3Xhjf9hfJN_7XC3P4WgXTVm2XI-q5_haSJxPn_wc2w9ee-x6YrPgVT2ocU0yraeRLN3jXablgEyVYWyNl5Qne3DyyCEzlwsYaHj80aykJIU9TOC_Rlp9PFeUzssi-zY0Z051BoYiuzI-p1-89qfcunNC70bCBWGhj_CbDqxblS9s7MO-C9WuNHA31yNDVtt_UDxN239AscpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pca6YI1MdWOtYQjQUuLSeEc0DfZGdkqZX37imyl0bMBu9uSJvoxB0twoQfWowyzbMMHtQaFSAZcJzC-qdKrhzVTusyvpwD-uvfcQp1PC4I2gu7NDlL-ck9Gfnt1OimfsKwKrBXBubDKPGL02JsFvCr2Thn4DYRf3YGtMIcN2lJPWp-v3Ygs88WM91jXbvfkRL2mLUEEM0mI-TEMjSz20zmNX2IESHeK-HqMUhyicjCcr3cvTpBWcufMwQjXR8HIrOP8T-pO0AelvdVVR4TVfVc2sEBLAbhsUrJw7Ho8dcajbwWPI_Cm1c871YgspSagZT_8tNErUaMUJ6BdPg1FCAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXLsiiwBICuKLvT0bPkvt0j6UJCTBhmqhhV2o2gYUnbAJ0daGXMnQSdWno4MozjtAjLCG2AvCzWlZzUBWJg6C1K_ew7AA-2zxXs_zIkNN6lu1OcuLBFAl2oxGPzmFilNssm2RApZeLpRKtSLRlrkFA-0iTlJntHMlVlUXSfno9xtEjKXSa3ybGvHsR9TbtjpCBz355O0mkQCJu6_t0PF8sg1jkNY99A79N-LjGWsOxEK5W0VeMGgKSOtzc1mjb7C6Sv7DO_a6Js651VsO_U8JfvxxBgnhXaQThRhof9untrQpU8DQze5QdKjydLtHQsX1q-_NTNRFoDylOylSUs0FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6l98uIa5_ZdQt0TuTomctl1Pt3mmffw90k4Vmq4hitgI_h3Kc4zhtUcZTIBrgRk6OcNXfSWq5TZuFM52GqhTsgVXvbrKq82L0d3fmmjazKsq15uTL5Wj0dmwibqSjyF8v853dN1ozKMtKYZtziG1BqZmTdfUyHos6IlzClhAn-rpZgOfOy9eYzxmvHQcogt358rJzwPR1h8OrrmRR39AtOWPJp5wsFRFo3HzcSvtwZFkxUqrF9hrWm6WSKFZsruRm0C-LszqtdKF6oLOGi_rjeP5Jyo-zidmj27PL6epOsZFzNv8KMUMAi0a4i6_KehhwASEWUciG_Sj3VgHlIVMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFaVwefkv8QCLH7d3lf42bPNoi20_MP-la1e27D2L3ldyM-4hCInivFJHBxgh4YLru4oan-eL-FEPH3ETqoauItEUHfpR_-oSUQSeaLshiSn0qHPpR53FdvJKq-H0oND8IBywq9QWbYZKBzz04Mjub7qP2QbMNWLGNJZ-i7R3lx89fFt2h8oKdeOd6Itpg_f3x5yp6oOLMDh7HMgIDe9kgEDnecBdRiAsujn76hdk5pw8qJQ0vr0Z5aUtmtuEaRtfZOw9rHbUoJa6piGi2uLJM1O5k-QsQFa5RIjKAOAgq5Uq9ra5FItwoHtgC3Xa41c_xQqWjTMvK4jG2HWuuoJqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تجلی وحدت امت در نماز بر پیکر قائد شهید
عکاس:
عادل عزیزی
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/447155" target="_blank">📅 18:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447154">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZaok-xJzaDuSmkpwGFI1ffD1g5OTR8f93ITtgoplYXjwy4jUZsAO1NwZVlcMkSyAXfCMzjt0PvhMFa-42hQwp6wltO68266fSBMAelzpgca-MZA8nOyy85d9QSq9IETmROrSJnFHcBotmVO7ASLagK6N2sP5b3PtS5Oc75dZVN1RPdVLmuOniKMkCqel8EvNCvcBKaPsopoi30sWV20W976KnYOq2lPlPeG9EkKNsW0HQZT2BM865E_FkiLgLbD1JLR-tSIY91u5tpyD3y4mGvOwEENhO0ZMoceCR9vGMjEmtX_Jn-HBAyuivoxe31fj_wGOMuuC8IcdiCwvgbBHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: دیپلماسی به دنبال تثبیت دستاوردهای میدان است
🔹
رئیس مجلس در گفت‌وگو با‌ محمد درویش، رئیس شورای رهبری دفترسیاسی حماس: دیپلماسی و مذاکره باید بتواند گره نظامی را باز کند و دستاوردهای رزمندگان را حفظ و تثبیت نماید و این مهم زمانی محقق می شود که کشور در کنار دیپلماسی، آماده دفاع باشد.
🔹
در آن شب که رژیم صهیونیستی به ضاحیه بیروت حمله کرد، مذاکرات به نقطه تعلیق رسید. به طرف آمریکایی تاکید کردیم که تمامیت ارضی در کشورهای منطقه و خاتمه جنگ علیه متحدان ایران در گروه های مقاومت، باید جزئی از تفاهمنامه باشد و به متن اضافه شد. امروز این تفاهمنامه در حال اجراست و پیاده‌سازی آن سخت اما شدنی است.
🔹
ما با آمریکا صلح نداریم و اسرائیل را به رسمیت نخواهیم شناخت. طبق رهنمودهای رهبر معظم انقلاب، به مسلمانان و جبهه مقاومت کمک می کنیم. این کمک، در صورت نیاز با موشک و اگر نیاز به فشار سیاسی باشد، فشار از طریق مذاکره است.
🔹
رفتار دولت‌های مسلمان در این شرایط بسیار مؤثر است. امروز آنها متوجه شده اند که همکاری با آمریکا و اسرائیل برایشان امنیت نمی‌آورد.
🔹
همه ما باید با خدای خود صادقانه عهد ببندیم که برای جهاد و شهادت آماده باشیم و همچنین آماده شکست دشمن؛ هر کدام نصیب شد، فوز عظیم است.
@Farsna</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/447154" target="_blank">📅 18:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447153">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0881a318.mp4?token=heSRQcR1hCQYtpHAk26A_yY7jrSPiXoE2j4o-0xT0GfJ60YjAg3llcVHORAodY3ul9AVTzdTcz7QTgPEYI1wMXnN4VpFUr9Moa70dEpwRocDfHb9ESGWAExFcCE3PuBaaN3NUl-9Sahkx2JtyhQzMzcNPlSEJTtVJ3A4LoTF0boai1-7JsTWDnLfbAnwwO3iwlgIHxomhMw-9Xq4fR-GI-LrN3QjfZqbKIZNWfNetPW5bT3uDtDuKtHs30NJiUSNBBkkaEXHAjSlObvoZq0nAnInGRa4BoMUyqk4Jbpnw-6VdQUw8S44qydOrX1rJVSm6qLLm_t_GVw0y5n3ckftZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0881a318.mp4?token=heSRQcR1hCQYtpHAk26A_yY7jrSPiXoE2j4o-0xT0GfJ60YjAg3llcVHORAodY3ul9AVTzdTcz7QTgPEYI1wMXnN4VpFUr9Moa70dEpwRocDfHb9ESGWAExFcCE3PuBaaN3NUl-9Sahkx2JtyhQzMzcNPlSEJTtVJ3A4LoTF0boai1-7JsTWDnLfbAnwwO3iwlgIHxomhMw-9Xq4fR-GI-LrN3QjfZqbKIZNWfNetPW5bT3uDtDuKtHs30NJiUSNBBkkaEXHAjSlObvoZq0nAnInGRa4BoMUyqk4Jbpnw-6VdQUw8S44qydOrX1rJVSm6qLLm_t_GVw0y5n3ckftZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال خادمان موکب میناب ۱۶۸ از خانواده‌های شهدای دانش‌آموز مدرسهٔ شجرهٔ طیبهٔ میناب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/447153" target="_blank">📅 18:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447152">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/277794b746.mp4?token=Vtk4lV82nkzd4UQ4JwfMfGSAhHqkof8qGMJ5Ekt13kYSstZ2OmsVzCXmJPUx3b6nC0lb96l_jTDF3sNxCLv_6sCYgWd8OKvuCMr-RbJq1G39v0mLG0cZDT0ZlFLBqjzuHUI35BnfjMo1fitHizJj_aL2DtzXONcSW8zckFBbntsFsKi8mdhRfAP9w8qfJLJAmpYT3Ke52zg-KktFnkOj51skaGJjNTmbuUBSGRL8tIHcUo4g4mdubLGHMskuROmbdH54Y8DTz-4OY8BwLYWMzGTBaA7Ec13ScckKRXmRnFb8HzOVRIPRm1ppVy-r8V-6KRrXQ4kYK29LFYmX9DknKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/277794b746.mp4?token=Vtk4lV82nkzd4UQ4JwfMfGSAhHqkof8qGMJ5Ekt13kYSstZ2OmsVzCXmJPUx3b6nC0lb96l_jTDF3sNxCLv_6sCYgWd8OKvuCMr-RbJq1G39v0mLG0cZDT0ZlFLBqjzuHUI35BnfjMo1fitHizJj_aL2DtzXONcSW8zckFBbntsFsKi8mdhRfAP9w8qfJLJAmpYT3Ke52zg-KktFnkOj51skaGJjNTmbuUBSGRL8tIHcUo4g4mdubLGHMskuROmbdH54Y8DTz-4OY8BwLYWMzGTBaA7Ec13ScckKRXmRnFb8HzOVRIPRm1ppVy-r8V-6KRrXQ4kYK29LFYmX9DknKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بلاگر ایتالیایی در مراسم تشییع: ممنون ایران!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/447152" target="_blank">📅 18:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447150">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/987972e43e.mp4?token=V2NTXTURYuzW6aYMLSlISfW-DpxsJ8mOlVZfoaeplEeAav5cd_e3m9HC0yl2xy_xqRdxLo9J6sNev6KaB6niNmZMd6UwQc_DjXJVpSBYfmXLWZJh4je_PLuctzPfpV31sM6Zz-6PeQd_B5leMq5Ld9nGrJ_s63oypcetPr2KMAfgy0BkPJ_OR2sss3vvDpmrWmpjwB0TJCGLre-a0OXcnsy6imv5HMdK_Wp5DFXxTGc1EY9fJtDIDPRRj5k6Xwfn59X_1ukrwWSd-Ttmtk6rOWZnL7trz_hen79R5d3IaMCECSnsM3tJ65gnvZV_Cwbr_Tl_0zQA3YOXUlaCojKx4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/987972e43e.mp4?token=V2NTXTURYuzW6aYMLSlISfW-DpxsJ8mOlVZfoaeplEeAav5cd_e3m9HC0yl2xy_xqRdxLo9J6sNev6KaB6niNmZMd6UwQc_DjXJVpSBYfmXLWZJh4je_PLuctzPfpV31sM6Zz-6PeQd_B5leMq5Ld9nGrJ_s63oypcetPr2KMAfgy0BkPJ_OR2sss3vvDpmrWmpjwB0TJCGLre-a0OXcnsy6imv5HMdK_Wp5DFXxTGc1EY9fJtDIDPRRj5k6Xwfn59X_1ukrwWSd-Ttmtk6rOWZnL7trz_hen79R5d3IaMCECSnsM3tJ65gnvZV_Cwbr_Tl_0zQA3YOXUlaCojKx4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماز بر پیکر رهبر شهید از زاویه‌‌ٔ خاص!
@Frasna
-
Link</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/447150" target="_blank">📅 18:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447149">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgfWSJVERcJuz8oLTzEe1Advj14UbenSEJU3LbvpE1OQvZ125di0hkxYlckuMICnT_E0yoFSQjC3SC7V3IeYnIjbX75CYYkLnQvLqqgPi8szorMrOtT3zMnVIzFnbsHYjgPMq8TSUSvebjm18NoPtju0JFmA0nvjjMH_OjVHRsXuGP9IfxNGD4ARBU5OOusfS7p5G73GM8p1ph8TQ-PT1ymrrqZk0TLB6X7hzjO-ffMl4SCaN-3h8n1qvGgguiNcVkELxFrB2iTikYH64t65Yanhjtxbb_VPKK_sOuueGau1E5GaJOfU43hqzoPG6Yqm8HlL6X0tFX3tPvl2nLQGkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ازسرگیری تجارت دریایی ایران و قطر
🔹
اخبار رسیده به فارس نشان می‌دهد پذیرش کالاهای صادراتی ایران در بندر الرویس قطر پس از حدود ۵ ماه توقف، ازسرگرفته شده و مسیر دریایی بندر دیر در استان بوشهر به بندر الرویس قطر بار دیگر فعال شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/447149" target="_blank">📅 18:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447148">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/754eb983a3.mp4?token=fE_ufwBbUZkAE8SHcL76dsweBP1Wu_1Tuq7RYMcibk5gWbDwdITUMQvj-dyhqe8n61A__xUsYoIdQgGQtpBJH8W6qzSTPQe-6DnSGUPMoJJGMB7EsgHOfxzQqWsULvJem6AJjrI3dN3ex7TOKBTIvaDxTSIQvexVh6Z1medj4yk89mE2ji_yWSK6R2Yjn-cKpcjv6kGrONDXfn6Xe0CgaH7thPih8_LDVeP_2XGZAyRhIijsqQf6NBgSpDruh7xsfMIS8f5HZ7kyVE9dU6TUWoAZeA-oOrUGapdHcOrF6JjsBIlBQ9yVSFRMAFPOPnZYZiwyJRgCcjDqpauTTpmSFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/754eb983a3.mp4?token=fE_ufwBbUZkAE8SHcL76dsweBP1Wu_1Tuq7RYMcibk5gWbDwdITUMQvj-dyhqe8n61A__xUsYoIdQgGQtpBJH8W6qzSTPQe-6DnSGUPMoJJGMB7EsgHOfxzQqWsULvJem6AJjrI3dN3ex7TOKBTIvaDxTSIQvexVh6Z1medj4yk89mE2ji_yWSK6R2Yjn-cKpcjv6kGrONDXfn6Xe0CgaH7thPih8_LDVeP_2XGZAyRhIijsqQf6NBgSpDruh7xsfMIS8f5HZ7kyVE9dU6TUWoAZeA-oOrUGapdHcOrF6JjsBIlBQ9yVSFRMAFPOPnZYZiwyJRgCcjDqpauTTpmSFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم نماز خواندیم هم گریه را به آغوش گرفتیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/447148" target="_blank">📅 17:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447147">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🎥
پنجرهٔ متفاوتی به مراسم اقامهٔ نماز بر پیکرهای مطهر امام مجاهد شهید و شهدای خانوادهٔ ایشان در مصلی امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/447147" target="_blank">📅 17:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447140">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pMKSrWcvShq78oZujgAeBjIJ-R6nR6_RhqyYP-rmaThTwaJOhGZDJT535Wh4QfcVfVVZgUuvN-AaIJBLaa61L3lO8lPvKM9_HJr-xkjMjQPYQcSOTQBxaKyd74wFTupPxuqLa1fwabLFkzOXVZS7JesoZ3tNa7ej904XAXwH51t_KeS-U3HuTsN7xq-Ru0Xpc6IwAXlcs2lb1mS_iPPOU9WmCEv_KkSszGS5_xUemdkqrQ0sNz3pwjLzATU57HRuVJI2M2UEz16PjaOEsMYkAGkbqUq9GN8oz2GYUAlhScIUSe6nk5G4OFUIFk43izun2S_JIgsIp1zup1z6osJOzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnHbafTRtkqFGjEo-2avukC109iChsmOUzYMdb12lgdyGqS0R9ReNpg0BvsEuhrd7ytWpxqPb6OVwaOjN3-WKb8NEdGgPj1N6lQcj4VWcUmGI0aEgezsO6c-gCvAV2BHoRHkpSfmUaz5u6lrTpYTawhyB-LD7LkETikV59x-vhIIMwknKfC71SC9kdBZeXrr4xG4vgkLA9Q5u88iJUpI_ow7QDNJhVrFVzPMeDUEaDQqjMc35mDTGiARVWd2AaYsH-15kgUyWpSH12qVtzFyHJA2S0AvrpFHDChcDvuaQwvnuUgpdCzjf5_3HkFHEUnHYumsdtC014VyM_aytCnZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uvDJ3V0Tt5ykVzCUj4FBhq0EglNTk4Tmq3reUMt6Z0mu64t6r8F7ccPCHgwQuk5YjIic5FQ03hlYGlAVH9JPs6bd_Vz0Xuaag6gHRZt1Acz4QwB5lnAAdzl-VDlGN1S7wtKavhlPjHRcLDibWf3ejsGbbujRRGIRhIqLcKbjRucuovXda606M2BCeOI89AjnnlWSmbCg4l4SfHA3_ZfLsjV364Zl7WeuyN8zwzq0x6ntAkznQke4J8QMuSckJdml6fh2A-h6uShl0EcvLdIii80_fuyjfVzhgAIkk-mdjAPOb9nQUAf_8GLkz6M259rgmLJGix0kRagVhbvfTNLlVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vLhjNclcpVXlH0iYkkm_W3jwxUw97a02SoVy0eEpWNnfvpM8ZjjfFo7YsPW49F7e9speqsFL5JoHH5ZpyOCUGiPp_U_MnfhWxbruUTxARuPimvVwXTIwVcXv8B8ESRH09jLR6dwoNJAc-lUTDP9w89EDX2R3sl8-g9Pdx8dNBjtUeHo-179_oXGqmoKlFwC3b8t04tIxw0RzLKdOeQDIN0lyPw8oYttmNFjUiFIQXrjYroOv0o_ageiRNCUoCQsWZcmL01HX9Qba1BwfYR48SEJguBiIBe1RrhgWP0gRfJLYY_AZIOqbN1EL5cZY6p9zUGeUZ6HsO5bfZoKVpltuTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XDrnmEQxNK8zj6GHne-e1p0YbXdyIKVBckOHiLLYCjaz2dF0LL8GqTw01vpw8J-J_XQ4MWlqQBp6PTWjEHvD0G9YKqhnrrCKHo03nSJyU-L9wzudd2--HCE9zAaSNP7fncqhGz4g3FkkBSkVYHDSGi6UsrQX6wKoCqfAgR_Cr84c9PM8QwTl8WxgbjnmN6lposk2SeirFwi8DIsLMkWQ-3lMtXK7Pm3VdOb8ar0A9czYgWzbjobZZdt5i4sGjcYXCNcmT1sjVNqPwyh5v4uk-k5ZxqjsHHkQrN9tL6j2FYxBS_qvmUDhYKg62r-WB6AKVLHZUOxDz492fRBXDOgETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KNQ300qgON-BDME0lIFDJ7C-jl85bOSX_riu7tNu0L7N6--6L2u7AjuCMs4li8CDV4mUohR3cZYj0smukesHpnRckE1XeiyymYU-KOWvzZoM5MX6o9WgBznvTzZZGihZ7meIPnRjOe_yNktKKiMZtyhZKSCCmgmufyQRR0bxHtix2Ea0VfuTdDmjD2Slp1XJvlCl7wmldFSR1amBaNjdpry9u8g91jE9NR5cldZG63_AXnh6Gb62g_hCuW11v1gJLio2-AVOCEk5b-oBi20O5fszbIsoG5xEwfdWusx7fL8qUke4xMj4Lymfs33uuyGE-S9t4m1viBn6T0uf1iEMgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QLr45V-942qwa5ogYWFsrxmzAKE7L402rYvFKwi2I99zzWDOVCHtLthJjGiQ3de4NpuOKoOPDBBiFoPkyVM6Cj6_FoctshEezB-V_jXYW-VwWzKwtrXJF1n_bArlXpoEb2BuTytcnGGOFfIu07POsY4dDfp4Sk5t3tMOgjvj7LWjEbRT_LPR2o3-H0xHHhbS7oYS9GZ6N84uAZAJCOv4MxR4xPXOZhNxVc_KSRwq_UaPtVC3jTTEj8eUdH-A5nXlsyEH9wan4hWC6J_F0UttstnZK-G14jI1WP1RCT7_j0CSwAHtxRwPaBEZw0Xhc0xa_hu1lmwIKKpcVWcH8gJAiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تجدید بیعت مردم با آیت‌الله سیدمجتبی خامنه‌ای در مصلای تهران
عکس:
زینب خدابخشیان
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/447140" target="_blank">📅 17:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447139">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab59e643c.mp4?token=Tyi53QbeyrHnyJcOYfh7F44mYDpa2YR3cGZCV0AOeK72XJKVsMx1fLrPEfamXITZw2BfkGcjMbb5pkL4UBuJScEx7sSovB_2xwlJoO7BumpuUblupNHcdEjF46HSPPTWb7_zjLwfMPu1T8H9lTzXDxbwmDApnpc_8U9m1dyNs-ztZwrM5ViJV9MZ_e_a-yePUWHBNYGn4gSglu8CSgF9Ese00jfJw3fHkGV478q1C7e8aW_KCpMYIQ4N7AmQS0XrzUhcRjzPROqzU29PwTwQ66xefPgP3yIXWmAcNuvhTN3cD-VCzx6ASQ6tRj-738BsGzXGPaVqVZp8z2jc-XfQWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab59e643c.mp4?token=Tyi53QbeyrHnyJcOYfh7F44mYDpa2YR3cGZCV0AOeK72XJKVsMx1fLrPEfamXITZw2BfkGcjMbb5pkL4UBuJScEx7sSovB_2xwlJoO7BumpuUblupNHcdEjF46HSPPTWb7_zjLwfMPu1T8H9lTzXDxbwmDApnpc_8U9m1dyNs-ztZwrM5ViJV9MZ_e_a-yePUWHBNYGn4gSglu8CSgF9Ese00jfJw3fHkGV478q1C7e8aW_KCpMYIQ4N7AmQS0XrzUhcRjzPROqzU29PwTwQ66xefPgP3yIXWmAcNuvhTN3cD-VCzx6ASQ6tRj-738BsGzXGPaVqVZp8z2jc-XfQWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقا، «مثلی لا یبایع مثل یزید» یادم میمونه
...
@Farsna</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/447139" target="_blank">📅 17:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447138">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شورای هماهنگی تبلیغات اسلامی: مراسم تشییع رهبر شهید روز دوشنبه، ۱۵ تیر، رأس ساعت ۶:۰۰ آغاز می‌شود
🔸
مسیر تشییع شامل خیابان دماوند، میدان امام حسین(ع)، خیابان انقلاب، میدان انقلاب، خیابان آزادی، میدان آزادی و بزرگراه لشکری است.
@Farsna</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/447138" target="_blank">📅 17:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447137">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65944687e4.mp4?token=UzoCBa3K4Cfrpf0cdqqeiiRqIz1e1YxTCeKJbqpfnp8tBvTKVdJTlRACyI_8BWT2lBC8lXSDWzcxIQZ5fU04TJ2QqM3Z5t6tSMskDgQhUpE8u34Pqb8d15W2GLtI1bHY7bDT1ZQTnFq4VF-W2ldTJagrRFsmqR43lBGvqNTEalmKF8H0OU7WyAMIQAIMUJkZU_q44idYNDkWzDoeIsrvu1P0bLvMsBvhlfmMrgB9f-O_6B7PuWNrZsG8JJJsMMB8yTj2ZkE3WgTGhUclM73P3Puf5KI6DwL9_E2jXFOMonG6WAIJn2fUcP0lDU7GgqL5GFNEGNjdf92FCRlyuZE7zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65944687e4.mp4?token=UzoCBa3K4Cfrpf0cdqqeiiRqIz1e1YxTCeKJbqpfnp8tBvTKVdJTlRACyI_8BWT2lBC8lXSDWzcxIQZ5fU04TJ2QqM3Z5t6tSMskDgQhUpE8u34Pqb8d15W2GLtI1bHY7bDT1ZQTnFq4VF-W2ldTJagrRFsmqR43lBGvqNTEalmKF8H0OU7WyAMIQAIMUJkZU_q44idYNDkWzDoeIsrvu1P0bLvMsBvhlfmMrgB9f-O_6B7PuWNrZsG8JJJsMMB8yTj2ZkE3WgTGhUclM73P3Puf5KI6DwL9_E2jXFOMonG6WAIJn2fUcP0lDU7GgqL5GFNEGNjdf92FCRlyuZE7zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوای هیهات منا الذلة در مترو بهشتی تهران
@Farsna</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/447137" target="_blank">📅 17:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447136">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🎥
بدون اینکه کسی از او خواسته باشد، این خانم در مصلی مشغول جمع‌کردن زباله‌ها بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/447136" target="_blank">📅 17:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447134">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc7ec7d63b.mp4?token=hqozgW-UIT5GD6wU42eg-j3yiMzUPKvolKFlaBg0jp7DrqwB41PkJr8PHWBCNXN86r8fLTJ-6dwUVzMA1L7b3oejVJstTz0h0rzERlVCZUfHxS6_1UX3FpqJge931PEIqyLoa394sZjkPJ-01sUX5rG3ZKZoJa56CFo7CwsCsMGfwK-69S5OaMernUVcYr4XEcFGXtfenVUSuWyWKTVL_dJKPUSQVK8q8VXuac5o_LuFMBEgPqNAFJ9a6UbV3SSghDnZ6hFWpwQdg3SImsK6DiiNp4iNQs_za8Xf5teNirAzi5rBlBDhihvV4q07qrrCu8aAvZtDNdR0D2BryE3VUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc7ec7d63b.mp4?token=hqozgW-UIT5GD6wU42eg-j3yiMzUPKvolKFlaBg0jp7DrqwB41PkJr8PHWBCNXN86r8fLTJ-6dwUVzMA1L7b3oejVJstTz0h0rzERlVCZUfHxS6_1UX3FpqJge931PEIqyLoa394sZjkPJ-01sUX5rG3ZKZoJa56CFo7CwsCsMGfwK-69S5OaMernUVcYr4XEcFGXtfenVUSuWyWKTVL_dJKPUSQVK8q8VXuac5o_LuFMBEgPqNAFJ9a6UbV3SSghDnZ6hFWpwQdg3SImsK6DiiNp4iNQs_za8Xf5teNirAzi5rBlBDhihvV4q07qrrCu8aAvZtDNdR0D2BryE3VUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائر رهبر شهید: داغی سخت دیدیم اما خدا را شکر آقا سیدمجتبی هست
@Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/447134" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447133">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700dbb08b4.mp4?token=ILzNBvq1gBClS_pRmwxJal7nolh26JfpNDE1UHYl8ORgGDKEB_atIpGn9OpYvVzYKDwkf3yy7Vzeig643P5R9gqiU5Idoc6HYj-KpV55SQwFyzfmD3DUCqT_JLE_5RQAJmKmb2T5YWV3FlxftRxgXgUoky6hhYCM8iV674qwB3baeUvyzGSLZ7xRzjE5Eaps06kOXjPnHaMtTr-0cjrcm9c_BV45P_FZln_y3lGOuSSjXOVUb4a8brO-LUHj93V79vmzQIItSx2hNWrNjCW-xFmkHBiyTS-HUAgCSekcVwCrrBPc5toNSX28-Qh52oh7dd4GyrNgBWr2HeGnpYbhfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700dbb08b4.mp4?token=ILzNBvq1gBClS_pRmwxJal7nolh26JfpNDE1UHYl8ORgGDKEB_atIpGn9OpYvVzYKDwkf3yy7Vzeig643P5R9gqiU5Idoc6HYj-KpV55SQwFyzfmD3DUCqT_JLE_5RQAJmKmb2T5YWV3FlxftRxgXgUoky6hhYCM8iV674qwB3baeUvyzGSLZ7xRzjE5Eaps06kOXjPnHaMtTr-0cjrcm9c_BV45P_FZln_y3lGOuSSjXOVUb4a8brO-LUHj93V79vmzQIItSx2hNWrNjCW-xFmkHBiyTS-HUAgCSekcVwCrrBPc5toNSX28-Qh52oh7dd4GyrNgBWr2HeGnpYbhfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرگی زاگربلنی، اسقف اعظم کلیسای ارتدوکس قرقیزستان: رهبر شهید مانند پدر امت بود و با چشمانم دیدم که ملت رهبری را مانند پدر خود بدرقه می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/447133" target="_blank">📅 17:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447132">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b151d9ab0.mp4?token=j2dwmM_amOxj_LVla4p-ro4kcwkguhMKUr5T04qXpn1M7HPTZfTzpA9gobm7QNXoREKEAWdO31govbuP0EA0HlvtY8pp1gw32MGk1pYmB0pyLD8bTLNv_dBZcLVpKeTmxlEnoBj1nCKH1ipNxbvFdbg5d9QvS7ax9orGcLszTeK2l3Sx0vPryHPHYyHrCBgfFVjX7b6kPklmcIlhocSGC3Nultxm7lq9fqOK8bC6uJRnujTo_g9UoRL_JDu48r6YPmo5h_d_5vsls2masCTEOnBHq_VptlqN86JBZ1bwcA_kSbnoTQZL99nWtVfZ4yAnNGxm37BSADa3FFV4sgof1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b151d9ab0.mp4?token=j2dwmM_amOxj_LVla4p-ro4kcwkguhMKUr5T04qXpn1M7HPTZfTzpA9gobm7QNXoREKEAWdO31govbuP0EA0HlvtY8pp1gw32MGk1pYmB0pyLD8bTLNv_dBZcLVpKeTmxlEnoBj1nCKH1ipNxbvFdbg5d9QvS7ax9orGcLszTeK2l3Sx0vPryHPHYyHrCBgfFVjX7b6kPklmcIlhocSGC3Nultxm7lq9fqOK8bC6uJRnujTo_g9UoRL_JDu48r6YPmo5h_d_5vsls2masCTEOnBHq_VptlqN86JBZ1bwcA_kSbnoTQZL99nWtVfZ4yAnNGxm37BSADa3FFV4sgof1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انتقام رهبر شهید را چگونه می‌توان گرفت
؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/447132" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447131">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/594503be2b.mp4?token=po4VlMSvtTnlJKY6c-hTA-njuRN-XLDrtyaEOPq13gzvFOM5VGxVxnriaOgvONiCw5gHJtgtoVGFIfhxhSAEuRAD_eSb1Y2xoesy57a_ZD6c5-_nch8ejhRRJG35d7pZNKoEaTvPMOdhLAiBJowCUUWZ9stAgK8-gmM47yzbfokWMCBpoqlsy9kMmUV6Hn4G4bJFHedHtkJWn3GyA1iEABKfDZEb0RqpYI8CzR66xH-A8T8jdZCM4YwmG2Cz8SkxfKd4lP6OEKJgCfEB-Eu6WT4pPrFrVLyYrMmLkZDm_S4nw2wwlF_5pagw8ffyWMf8Hj6iHWY2ICRDgK4W_fl54A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/594503be2b.mp4?token=po4VlMSvtTnlJKY6c-hTA-njuRN-XLDrtyaEOPq13gzvFOM5VGxVxnriaOgvONiCw5gHJtgtoVGFIfhxhSAEuRAD_eSb1Y2xoesy57a_ZD6c5-_nch8ejhRRJG35d7pZNKoEaTvPMOdhLAiBJowCUUWZ9stAgK8-gmM47yzbfokWMCBpoqlsy9kMmUV6Hn4G4bJFHedHtkJWn3GyA1iEABKfDZEb0RqpYI8CzR66xH-A8T8jdZCM4YwmG2Cz8SkxfKd4lP6OEKJgCfEB-Eu6WT4pPrFrVLyYrMmLkZDm_S4nw2wwlF_5pagw8ffyWMf8Hj6iHWY2ICRDgK4W_fl54A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری شبکه سه: ملت ایران تا زمانی که نفس می‌کشد، میناب را فراموش نخواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/447131" target="_blank">📅 17:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447130">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شرکت راه‌آهن: فروش بلیت قطارهای فوق‌العاده برای تشییع پیکر رهبر شهید انقلاب در مسیر تهران-مشهد و بالعکس از ساعت ۱۷ امروز آغاز می‌شود.
@
Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/447130" target="_blank">📅 17:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447129">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87ff6552d9.mp4?token=YWzF2j2DWcOMOg5rsaVJ5mt1aocfqKdZoRQ1MCh9c9X-YuJnoxgG48val-88dxyVoczjkblZ7arm8iT2rxPIRC9VHCmNF9vGJ4BWMyqkRHADAvJnuUsys97AOvcNEsSkHgkIO0WPw2WMY6srWO_q9L9ZYX6yvEvl7SqNXQPIhMtAHUNxdS_fuzvILr5mrRWgnMq3eoFfVAVBDFU04MQsS12FMCFxS5dPsdCA8BlEQHA2dzW76adbuYVyCQJau3DHiUKiOSfdA3hyaYSo_GPRMlzBXD9FsP1sBVle5u2jeqKKH3qCLpC0ehn37WHRoAjonQUJzPLdrbdfJ2qJ3_LVfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87ff6552d9.mp4?token=YWzF2j2DWcOMOg5rsaVJ5mt1aocfqKdZoRQ1MCh9c9X-YuJnoxgG48val-88dxyVoczjkblZ7arm8iT2rxPIRC9VHCmNF9vGJ4BWMyqkRHADAvJnuUsys97AOvcNEsSkHgkIO0WPw2WMY6srWO_q9L9ZYX6yvEvl7SqNXQPIhMtAHUNxdS_fuzvILr5mrRWgnMq3eoFfVAVBDFU04MQsS12FMCFxS5dPsdCA8BlEQHA2dzW76adbuYVyCQJau3DHiUKiOSfdA3hyaYSo_GPRMlzBXD9FsP1sBVle5u2jeqKKH3qCLpC0ehn37WHRoAjonQUJzPLdrbdfJ2qJ3_LVfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تهران آماده میزبانی همه جانبه از میلیون‌ها هموطن/ تأمین گسترده و مستمر آب آشامیدنی، یخ و مواد غذایی برای خدمت‌رسانی به زائران رهبر شهید
🔹
شهرداری تهران، ضمن اسکان زائران، در حال تأمین اقلام و توزیع آن با رعایت دستورالعمل‌های بهداشتی در پایتخت است.
@Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/447129" target="_blank">📅 17:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447127">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروابط عمومی چادرملو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9396129178.mp4?token=VO8USirzZDQonRqkK8iucPi74R4x3dOnm0C_6fy1ABQ3U_1OhPSGGwQWwBSPC6y7DIlMpcPaWPQpBYQZgwLNhopyTrxuMNOWTVXolc5K3m1SHgRUA5H7ve90P6WiOMqCxKbGNjg-PzLPWDAQGEprtZiRSxwAqX0RcjOGKRv0u0pDo0i-VV_8FOZ910C6rEEvMOUNl4vjZxY_RYFSMp6W_IsTF08JkwFGVb1dU4klpk1bpB-nGo4MT19j-CfWjRHLDaMQsNIn5UukiiGdjD5GTxWexAW2mrN1kokj8AuNKzXB1nZh3AugeGzihh21VyNYk-llANUci0hsAXU08TsYcg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9396129178.mp4?token=VO8USirzZDQonRqkK8iucPi74R4x3dOnm0C_6fy1ABQ3U_1OhPSGGwQWwBSPC6y7DIlMpcPaWPQpBYQZgwLNhopyTrxuMNOWTVXolc5K3m1SHgRUA5H7ve90P6WiOMqCxKbGNjg-PzLPWDAQGEprtZiRSxwAqX0RcjOGKRv0u0pDo0i-VV_8FOZ910C6rEEvMOUNl4vjZxY_RYFSMp6W_IsTF08JkwFGVb1dU4klpk1bpB-nGo4MT19j-CfWjRHLDaMQsNIn5UukiiGdjD5GTxWexAW2mrN1kokj8AuNKzXB1nZh3AugeGzihh21VyNYk-llANUci0hsAXU08TsYcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ببینید
میزبانی فرید دهقانی مدیرعامل شرکت معدنی و صنعتی چادرملو از عزاداران آقای شهید در موکب چادرملو واقع در میدان ولیعصر تهران</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/447127" target="_blank">📅 16:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447126">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/447126" target="_blank">📅 16:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447125">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBCAJ9NGNOc9iKkPzbOY1QMUpqRa_W-HNZEZ1OgbLZcf6BUDSjR69nfhE5M3nVuQyaz_U5tr27orqiYEkA6Q_3WT1sHpndgO5tgZ_dkCy3tHMnIO9DLNJWmvAxAMmK2I5_DssmwUVILzGiN8PZBwltOEfaVV31ggYSEsrDUkJrny0_DsJSUlUp_huPUjtyOuZN6CdmbM22n5cjmgSujX2raVfcMTjd3NjcWzzd_S_6hJWddPSDERJdAbicGzDDGlk9Dd4iBd_Q1R8WS1Q4a9xNetipPW5OC4pfqKgVNX-NagY5Eh2S41AHbyw3SumcmyD7RRWid6J1nQleU41sCw7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارمان اربعین بود، وداع نصیبمان شد
🔹
«دلم نمی‌خواست هرگز آن لباس را بشورم. حس می‌کردم ممکن است عطر آقا را از بین ببرد یا برکتش را. نمی‌دانم فقط دوست داشتم همانطور توی کمد لباس‌هایم بماند.»
🔹
«خیال می‌کردم سال‌های سال باید در مسیر نجف تا کربلا نوکر زائران سیدالشهدا(ع) باشم تا شاید روزی آقای دلتنگِ کربلا را هم در همان مسیر زیارت کنم، اما...»
🔗
ماجرای دیدار این موکب دار با رهبرشهید را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/447125" target="_blank">📅 16:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447124">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bdb70b516.mp4?token=ac2Jr-o8yCOf6b6GM16Om2S1wa8BuLGy5HKfwOgcehsn6en2KMwBZfVZL68F_k4ntjCK0VqToBaA_pZpV0h5PfwURXvDp6Te78sxoxZOT8GACnEdcCpNvrs42Yos4x682u5ne66IfpeLg1DYPpNDkkFRnjTJOgx45dhqrmeuh_Stte3ikIMaqX5Sh-rKbyGuuw7e_3yhVqqv_9KiSj83O6FpKWh6Oh_vQqfuKcCxMvN68jzgKUhdCGiE1R2f1vID4pVFAAvBocJdVaoN5J_-DyjHq029S98ajvwoAqhT14J5rofcS80cKYsUT0BFAh1oP1-VtJqDxBtQMV3xAgLanYI2hvQrXa36LPNpB8zWAylpLM0_CuqABCgwUAg2KkWnowvli2-4qlsJRkRnMmk5E2MbpSa5gNLCWmoQRID7DU6yzCvgNXFiGyBDIg62o9bKgH0kN3LJU02MZgtic7voUi1OYlGIg_5gYoiLVg4ybrl7LUj_PYFvBmSGLNKt1Fufqf_23FcfvU9gSDP6RlABgPqNd6f97C0ixLgfKQCxue1cWPbQLqqhyZrWDjnQI7jxGTHUPJko5QZqhcTG-bx1h8Md6ueFeotqkp9-1QOnu3UeEP9o526Jg2XHod4mm3EfdfOAcMQwOh8wi0ayD4AwZ21mh2MNVHfnqB5QHS1ERh4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bdb70b516.mp4?token=ac2Jr-o8yCOf6b6GM16Om2S1wa8BuLGy5HKfwOgcehsn6en2KMwBZfVZL68F_k4ntjCK0VqToBaA_pZpV0h5PfwURXvDp6Te78sxoxZOT8GACnEdcCpNvrs42Yos4x682u5ne66IfpeLg1DYPpNDkkFRnjTJOgx45dhqrmeuh_Stte3ikIMaqX5Sh-rKbyGuuw7e_3yhVqqv_9KiSj83O6FpKWh6Oh_vQqfuKcCxMvN68jzgKUhdCGiE1R2f1vID4pVFAAvBocJdVaoN5J_-DyjHq029S98ajvwoAqhT14J5rofcS80cKYsUT0BFAh1oP1-VtJqDxBtQMV3xAgLanYI2hvQrXa36LPNpB8zWAylpLM0_CuqABCgwUAg2KkWnowvli2-4qlsJRkRnMmk5E2MbpSa5gNLCWmoQRID7DU6yzCvgNXFiGyBDIg62o9bKgH0kN3LJU02MZgtic7voUi1OYlGIg_5gYoiLVg4ybrl7LUj_PYFvBmSGLNKt1Fufqf_23FcfvU9gSDP6RlABgPqNd6f97C0ixLgfKQCxue1cWPbQLqqhyZrWDjnQI7jxGTHUPJko5QZqhcTG-bx1h8Md6ueFeotqkp9-1QOnu3UeEP9o526Jg2XHod4mm3EfdfOAcMQwOh8wi0ayD4AwZ21mh2MNVHfnqB5QHS1ERh4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پرچم خون‌خواهی سرخ امام شهید در کنار پیکر مطهر رهبر شهید و خانواده ایشان  @Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/447124" target="_blank">📅 16:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447123">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f095ce01.mp4?token=nxPWP5L3bSMkrKa0s7q0ShQpD88rIzdRjLQhmWkciJ_Dm8KFsLohX9x8aK5FHV0WO4ZdkDRWfIhO79sesyD_HtiOjsnKb1P2EIaOBqJceb29t2buyiJgh8sdZr5l90oz4C8mMuGZfaSMYdJ1Op1itnD0qOuQVGLLk_tfyf2TPUxadPOlyAhY4V7OkVyWRNGJ6bDBVd2b7dE-GZNBqqVApCmrjuavIAbEQxgbz0cPNoD87GhM1SL6fGQYrVH_wE6wmYcscA50gBJZemytJWq7wjIUGgZjDAKTe3jc7RCrsiESRm62BZpYxTeysDW-qDRLrj39JVhcn7tBeYyOh4ExBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f095ce01.mp4?token=nxPWP5L3bSMkrKa0s7q0ShQpD88rIzdRjLQhmWkciJ_Dm8KFsLohX9x8aK5FHV0WO4ZdkDRWfIhO79sesyD_HtiOjsnKb1P2EIaOBqJceb29t2buyiJgh8sdZr5l90oz4C8mMuGZfaSMYdJ1Op1itnD0qOuQVGLLk_tfyf2TPUxadPOlyAhY4V7OkVyWRNGJ6bDBVd2b7dE-GZNBqqVApCmrjuavIAbEQxgbz0cPNoD87GhM1SL6fGQYrVH_wE6wmYcscA50gBJZemytJWq7wjIUGgZjDAKTe3jc7RCrsiESRm62BZpYxTeysDW-qDRLrj39JVhcn7tBeYyOh4ExBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پرچم خون‌خواهی سرخ امام شهید در کنار پیکر مطهر رهبر شهید و خانواده ایشان  @Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/447123" target="_blank">📅 16:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447122">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWKCso7_AX3WrQJfaiYFbj7l7xQyF7Cf9RGYXpjqfiJeeqyGyihiB2oea_hZR-A5S8Cgw-980ZsxB9RxkvILim9t_WEBYXsIGHuMqtVO0_IzM4RQq6aXAiWVOopGiWVI4WqqJXlerrpBDAGKg3cNb_3102rwk-4XuzVR4SICc6ls4zTBhfIRf67W-sfElAVUntZzjD95ToH7tYFNPRovPxZdAjjguAYHBxOLqQhQuTMsc3ShfRGoxsFLcgxOjnbz7pAW0biaxKD33hgD1q5AiFVd1a9GVnvBbkg8rZUe4NECJ24ypDaqyiOa8xmkO2hfQInlwOvXFJSDWbWBnL5nCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ما شیعیان قاتلان رهبرمان را مجازات می‌کنیم
🔹
دست‌نوشتهٔ عبری مردم در مصلای امام خمینی(ره) تهران
🙍‍♂️
ارسالی مخاطبان به
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/447122" target="_blank">📅 16:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447121">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/593b30b738.mp4?token=RM7-6Jy-YtSo9_-w8yCStdsYMM8u7E5EUamX6ognb1184MLNkFL8xmUS7c6ol1-m3dhSKQuqc5skmiXHK-8GFkDInNW5TBQWBXTP3ixWml3UXu9xZ8pEq42lGSQ_ZiZwABtR2RJJEUuIHwHwLVJmTU9ZJ8bDakMRwqQSw_LTcSr5hpysMYYayHEWOwOF3rhcwUF6dYwm8cQpzDhqw3CbDNdl_JpCVayn7r0Ysj2leHtNqEX-6BzLl-FRCKYKdvdgrV4i37etwcdEkpryGAqx93NbnPzLwqrp0htRn0p8bSKDkOKn9qQo11hFe-xBHwgMzEXPed3nhp4bzZJB40C7Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/593b30b738.mp4?token=RM7-6Jy-YtSo9_-w8yCStdsYMM8u7E5EUamX6ognb1184MLNkFL8xmUS7c6ol1-m3dhSKQuqc5skmiXHK-8GFkDInNW5TBQWBXTP3ixWml3UXu9xZ8pEq42lGSQ_ZiZwABtR2RJJEUuIHwHwLVJmTU9ZJ8bDakMRwqQSw_LTcSr5hpysMYYayHEWOwOF3rhcwUF6dYwm8cQpzDhqw3CbDNdl_JpCVayn7r0Ysj2leHtNqEX-6BzLl-FRCKYKdvdgrV4i37etwcdEkpryGAqx93NbnPzLwqrp0htRn0p8bSKDkOKn9qQo11hFe-xBHwgMzEXPed3nhp4bzZJB40C7Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایرانیِ مقیم روسیه: رانندهٔ فرودگاه مسکو به ما گفت حتماً برای تشییع رهبر شهید به تهران می‌آید.
@Farsna</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/447121" target="_blank">📅 16:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447120">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d79867cbe0.mp4?token=XS3EsMz2A44IEvV11VJ1qTSxGWTDPFdXFFA2KXElGzG6MHCX8oVUIvRj9Fv-K2gaBPuThDz2R5S3TLF8gDXBznLjdxThwSUEcoTRANzrpEcU0bqZrwTn2hgdrPwzb29OjJDFMZAltlsA77Tm8Dn2FTOZlnkeHvWikjzldkl-VRHafi9F_1_-eQW-eT1BqtrYxQegAKOVXroubFGjm8mZIIJ4CCmBU0yjHu2hvqVDeru_zlp8CZ4OXNZSr4clh5CYxU4y2X23Dg5WE4odWp4bz2AAgpGEPS7dEWChn44YA2Kw4G80lW5J6hTTNPTEKqiP1t4A9DQbZbaqpPGqMb0a0ULmEf6CDPiSlYMMgpBphzOGVmtWlNGWVPTvPt5IVdtD5yRrgAB7AgmZ9bWTizl4sNK1JSiO_tGUXUQTW49E2J4n6nqVqP2CcLp4FL3P7OVzDtEdSjgOR5gudkf2kDwqeqvU68l4zW2IccXH2bJEcm7WxgPNRySCowNpVlVmg_YauXVYJACzG6BoajMI3zl-R6Wu45WRuO9qZX2AfAnUl6obqAprnx9mg2-ZGQTTQxJh5fFIPfl8mx4ETcjRcIsgLTJZoq7qz2NQyRvT3YLb-OwvwEROqUdsHbn4B3uC4-rXGp-1wkF1jb4Gg-xrdj1he6dZYpI05i_93Cwx7Oy0nR0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d79867cbe0.mp4?token=XS3EsMz2A44IEvV11VJ1qTSxGWTDPFdXFFA2KXElGzG6MHCX8oVUIvRj9Fv-K2gaBPuThDz2R5S3TLF8gDXBznLjdxThwSUEcoTRANzrpEcU0bqZrwTn2hgdrPwzb29OjJDFMZAltlsA77Tm8Dn2FTOZlnkeHvWikjzldkl-VRHafi9F_1_-eQW-eT1BqtrYxQegAKOVXroubFGjm8mZIIJ4CCmBU0yjHu2hvqVDeru_zlp8CZ4OXNZSr4clh5CYxU4y2X23Dg5WE4odWp4bz2AAgpGEPS7dEWChn44YA2Kw4G80lW5J6hTTNPTEKqiP1t4A9DQbZbaqpPGqMb0a0ULmEf6CDPiSlYMMgpBphzOGVmtWlNGWVPTvPt5IVdtD5yRrgAB7AgmZ9bWTizl4sNK1JSiO_tGUXUQTW49E2J4n6nqVqP2CcLp4FL3P7OVzDtEdSjgOR5gudkf2kDwqeqvU68l4zW2IccXH2bJEcm7WxgPNRySCowNpVlVmg_YauXVYJACzG6BoajMI3zl-R6Wu45WRuO9qZX2AfAnUl6obqAprnx9mg2-ZGQTTQxJh5fFIPfl8mx4ETcjRcIsgLTJZoq7qz2NQyRvT3YLb-OwvwEROqUdsHbn4B3uC4-rXGp-1wkF1jb4Gg-xrdj1he6dZYpI05i_93Cwx7Oy0nR0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما با آقا وداع نمیکنم
...
@Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/447120" target="_blank">📅 16:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447119">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b921516321.mp4?token=dJ7oXLdInghMU921_s0Nhn55kJ4S4dIOkUFKt1HQP4CXhT_IlhbIif9glhEl2_5jG5mqnhm8aHpeFGWF7hds3EGGj5udp1L8k8WcGw56HLbJzseI4CKvP8d8SnzUU2t4CghanHezwT9mVwa_VA-jUb8n8Ww0Pvz5wd_s7OuCDpW7IN6hz1_smVe6fBPP5InTCNA2fMBzpZon1e5hc8KxqN2Q0bq5JELbNPTRUflZS_eMFHxI_lRM1M_-eogzewfWJnrjkg0Iy5jFPfQUo77gpWE6U0UQBLTqlYP-SgV1q_4XaVx44pgvdSgECjv8VZye5ewlfJlTHo2HBzKtp_0DAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b921516321.mp4?token=dJ7oXLdInghMU921_s0Nhn55kJ4S4dIOkUFKt1HQP4CXhT_IlhbIif9glhEl2_5jG5mqnhm8aHpeFGWF7hds3EGGj5udp1L8k8WcGw56HLbJzseI4CKvP8d8SnzUU2t4CghanHezwT9mVwa_VA-jUb8n8Ww0Pvz5wd_s7OuCDpW7IN6hz1_smVe6fBPP5InTCNA2fMBzpZon1e5hc8KxqN2Q0bq5JELbNPTRUflZS_eMFHxI_lRM1M_-eogzewfWJnrjkg0Iy5jFPfQUo77gpWE6U0UQBLTqlYP-SgV1q_4XaVx44pgvdSgECjv8VZye5ewlfJlTHo2HBzKtp_0DAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ویدیوی ساخته‌شده با هوش مصنوعی از چهره‌ها و صحنه‌های خاص و غیرمنتظره مراسم امروز وداع با رهبر شهید انقلاب در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/447119" target="_blank">📅 16:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447118">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLOU2dJqZEIuzxjaCz4TDgLJcc-tza2c-Quhj4Up1n9fRCoH6V6hueSPqld9jAUL7ULnQT10YIoElVwpgI3UILFmi0nfIUJEMERZDXYtZFM1OV3jZx0DtzcE1xxeJaPxNPDHxMmVfEbcH2uBCpDkDycqjs6FrlAdkREMu0DCgmXaoBe3c41PZh53I5HSw8nNDZecYMNYum94JfZgciuaEOvSvAb16LU-PuH3QUquGkYmlpdPCHZsgStnwQnEVwhXm2-DRfVDePc-huB6NspPWgYbgC_6iqtpDGEK4PuKB7_h5NVrXwpPE6nL5s76eV3jPJZPIWlzw14kmkwslU8hCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا! بچه‌های میناب زودتر از همه به دیدارت آمدند
🔹
«حول‌وحوش یک هفته قبل شهادت ستایش، مادر دختری تلویزیون نگاه می‌کردیم، حواسمان جمع سخنرانی آقا بود که یکهو گفت: «مامان ما می‌خواهیم بریم اردو پیش آقا...»
🔹
خنديدم و گفتم: « مگه می‌شه شما رو ببرن پیش آقا؛ تازه من نمی‌گذارم تنهایی بری، اگر ببرند باید با هم برویم» گفت: «شما نه! ما دانش‌آموزا، بعدشم معلما و مديرا، مامان باباها نیستند!»
🔗
حرف‌های عجیب ستایش علی حسینی پیش از شهادتش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/447118" target="_blank">📅 16:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447117">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q03UZLhisKAOOWiNfgt3kL3p9kteWiki5KLHnN3wmwGy4GB5i14ifddaB2zgjHRVqDk8dT--KmCcA5_Yz_L7e8PYUR9EE_0R34birLEq2m9sx6WmDkMCXaHEsHlfq3Nq14KWsFLdsk0gL-fblSJ3BQQwYtiDZjWDOf-b90hZ6rH068aek-c2uB-LBP424ZeZowwuhtKuC2-zr6iyGQZKdjYcxDFkCQZb70bpGvmtO3wW5u93KaeFfIjrBZXMZiDi5dNDfUl15t-m3TNtP9J02XE2BTLu4Mhh4D0-5YHVHBJghszTYdQ_VTbn50Rvs1oPi_qwJJm8ZOqDTG_1mLiRBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
معاون فرهنگی و اجتماعی مرکز رسیدگی به امور مساجد تهران: همۀ مساجد تهران با آغوش باز منتظر مراجعۀ میهمانان مراسم بدرقۀ آقای شهید ایران هستند.
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/447117" target="_blank">📅 16:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447116">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb48eac0e8.mp4?token=HJVeaP8_R0HT4TyQPbq1FWUYIiCwKsul4unjNhEEKPZyW4z0JgH1_F8SeZoMu-kabltMEBWoTeNnTgnK5n18Dj_w1T4mxWuI7p2tULedEJRb-lt52KmjnuEjvh9aSs8wjbsALtfCExKZtsDduIv3Mahski6AzZfSbfO1kOSwEXYqoqZ3hmENukiJaGpmI5WnF-ydH6pHUvNE8BjQWS26NljhMC2nhC3dN_YeVJVNpkqRsFUdFtbpyCHFBvRfMqLkMo4stvwiu8AelcCrJrkFi0-bpQaiGy0B9sWuYJCzrA5blc-Y3yoKgG4CU7OS6ogEmeJaauXZzktS1ZEGVKJZrzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb48eac0e8.mp4?token=HJVeaP8_R0HT4TyQPbq1FWUYIiCwKsul4unjNhEEKPZyW4z0JgH1_F8SeZoMu-kabltMEBWoTeNnTgnK5n18Dj_w1T4mxWuI7p2tULedEJRb-lt52KmjnuEjvh9aSs8wjbsALtfCExKZtsDduIv3Mahski6AzZfSbfO1kOSwEXYqoqZ3hmENukiJaGpmI5WnF-ydH6pHUvNE8BjQWS26NljhMC2nhC3dN_YeVJVNpkqRsFUdFtbpyCHFBvRfMqLkMo4stvwiu8AelcCrJrkFi0-bpQaiGy0B9sWuYJCzrA5blc-Y3yoKgG4CU7OS6ogEmeJaauXZzktS1ZEGVKJZrzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازمانده حمله اسرائیل به کشتی آمریکایی: پرچم شیطانی اسرائیل را در روز استقلال می‌سوزانم
🔹
یک بازمانده کشتی یو‌اس‌اس لیبرتی، در اقدامی اعتراضی در روز چهارم جولای (روز استقلال آمریکا)، پرچم رژیم صهیونیستی را به آتش کشید و از سربازان کشته‌شده در حمله اسرائیل به این ناو تجلیل کرد.
🔹
وی در این ویدئو با خشم می‌گوید: «من این پرچم شیطانی را در چهارم جولای می‌سوزانم!» و در ادامه از «توماس مسی» به عنوان نامزد ریاست‌جمهوری ۲۰۲۸ آمریکا حمایت می‌کند.
🔸
ماجرا چیست؟
🔹
یو‌اس‌اس لیبرتی (USS Liberty) یک کشتی اطلاعاتی نیروی دریایی آمریکا بود که در ۸ ژوئن ۱۹۶۷، در جریان جنگ شش‌روزه اعراب و اسرائیل، هدف حمله هوایی و دریایی اسرائیل قرار گرفت. در این حمله ۳۴ ملوان آمریکایی کشته و ۱۷۱ نفر زخمی شدند. تل‌آویو این حمله را «اشتباه» خواند، اما بسیاری از بازماندگان و تحلیلگران آن را اقدامی عمدی می‌دانند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/447116" target="_blank">📅 16:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447115">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2838ae2b47.mp4?token=N0bj88YDUnBgeHxDRWOA3pEkwzQe3Ud9sqGYF1uWhlZH0YFEuiPqH5b88bPwaoJtoHRFk_RsTh8pkQomwkk0puQSkYVFRnhpRjqOZHwBDQojrwSlByjVqyvTBHj8IvZOw5y9ZnRFwuIJ9-eAh5Zk88dcNMymLB_aG54X4H9G4HM8uL0BiTeujO4Qgi_vCamOFk4xHnuNU5J4UWUA0w-5iCYZUUhSguKk4p1LfOJ__6yI9sq6xuXOLpjZcygEG94un92L3nFD3PdtO4CrZ5czf4UX1jFwTL6wowx2msZvWjkHYtgV5Lpj8K3KNrAW8kFVn47BC26fAMBQkCQVaELRkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2838ae2b47.mp4?token=N0bj88YDUnBgeHxDRWOA3pEkwzQe3Ud9sqGYF1uWhlZH0YFEuiPqH5b88bPwaoJtoHRFk_RsTh8pkQomwkk0puQSkYVFRnhpRjqOZHwBDQojrwSlByjVqyvTBHj8IvZOw5y9ZnRFwuIJ9-eAh5Zk88dcNMymLB_aG54X4H9G4HM8uL0BiTeujO4Qgi_vCamOFk4xHnuNU5J4UWUA0w-5iCYZUUhSguKk4p1LfOJ__6yI9sq6xuXOLpjZcygEG94un92L3nFD3PdtO4CrZ5czf4UX1jFwTL6wowx2msZvWjkHYtgV5Lpj8K3KNrAW8kFVn47BC26fAMBQkCQVaELRkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌وطن مقیم ترکیه: پس‌از شهادت رهبر انقلاب و ایستادگی ایران در جنگ، با غرور و افتخار از ایرانی‌بودنمان سخن می‌گوییم.
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/447115" target="_blank">📅 16:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447114">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMRhzujBI7BkHEiqwE0TdWZpQuYiPAUnwCUzJqJ6ZoxA3jPye3SRzNUzg5CHgKBqGL_QmdQGM2xNEKfiORHVR1grIZhJpqzh-cFvwfy0zeNUBMZnAQ9LuShyuOEmInGOSVAZAu8spDJ16BJTH0f7T18Zjz5O0j0lrmSlVzSMHWORtuBNvY87gnYch7ZfqQ6wmPqQ6v2NOmR8CzAO3jzgi3dqgvyOCnUebHIzxWIGa52I03Gcx-HLdPUkBbUoDtiRiNveigIzRIYdZOrE6byqqvoajvBxsZ2dbRO36eTdsHbNIE5H8DGQ715aYM_lJGg67iW2RJzqC_jJnNsrVYQ0Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پرچم خون‌خواهی سرخ امام شهید در کنار پیکر مطهر رهبر شهید و خانواده ایشان
@Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/447114" target="_blank">📅 15:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447113">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9200c8b77.mp4?token=Vq13vacJ24D6Y9NoitxuhbBeINFPlQIs1WWd96HY4_-G0hRVbIV5RDKXZmLiDvf4GvIttYv00mbAX2R6I67_zD57i7eyN0xILgpJcEkbZlItJK4Jn_x5dYsVvb2si9odS8yFJKfY_Jentq9kIj_of-OG8dtK__6JsE2aDTP9a0X5K3uQy-4vJXDxkC_TRyabVWfEJ1eMnHl57khFxt9hcrc9Op7Kmis_ue61naJwvW-_frlfljKrI5QWGOBn3_snKFho3X_KrEJryWXagQXRPDoqOBLQNygrkJmy8-e9aIE1lLJIZzeOql-ZjvJa-2CuLCQQ-9Em-WTxRVRNoPadAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9200c8b77.mp4?token=Vq13vacJ24D6Y9NoitxuhbBeINFPlQIs1WWd96HY4_-G0hRVbIV5RDKXZmLiDvf4GvIttYv00mbAX2R6I67_zD57i7eyN0xILgpJcEkbZlItJK4Jn_x5dYsVvb2si9odS8yFJKfY_Jentq9kIj_of-OG8dtK__6JsE2aDTP9a0X5K3uQy-4vJXDxkC_TRyabVWfEJ1eMnHl57khFxt9hcrc9Op7Kmis_ue61naJwvW-_frlfljKrI5QWGOBn3_snKFho3X_KrEJryWXagQXRPDoqOBLQNygrkJmy8-e9aIE1lLJIZzeOql-ZjvJa-2CuLCQQ-9Em-WTxRVRNoPadAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ايمان قياسى: تمام دنیا درحال تماشاست که رهبر شهید ما چقدر طرفدار داشت
🔹
آن آدم معلوم‌الحال توییت زد که فکر نمی‌کرد این میزان جمعیت را ببیند.
@Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/447113" target="_blank">📅 15:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447112">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">فرودگاه بندرعباس پس از ۴ ماه بازگشایی شد
🔹
فرودگاه بین‌المللی بندرعباس امروز با فرود نخستین پرواز مسافری از مبدأ مشهد، پس از ۴ ماه وقفه، فعالیت عملیاتی خود را از سر گرفت.
🔹
پروازهای مسیرهای تهران، شیراز، یزد و مشهد به‌تدریج به برنامه عملیاتی فرودگاه اضافه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/447112" target="_blank">📅 15:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447111">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2752606bfe.mp4?token=ubSbyQoHiiMpW2hrtrLfT_LIVpCJ0kI_HWMW31yYhKUI8Z9CDbrjCIPjiwIvCCTXRo8hl5OPk902TXpikLS5NnieYNkQlto2egCENqCoK2Q_6bKALvkH3Xjs5I9ct91m_rxEaomK43jPdE5hgQaHsnPRG6Pco63bGQuGX3EoP8_pPgo1gWeteMMiOM9Ypd9_G_-FPWImN6A8Mf88iiR4bkuzhyxgVYeKlLOB_CkyOviwultZ_ZUMF5tbRqE_gPjpPz3IV8_Y9YQHLwkP0ajtd3WfvkGvvrcHX_QrhNCjrF4ICn6A-ZNaa3AKn69LBdguuTTEZcx_cK1WITBsLwEO8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2752606bfe.mp4?token=ubSbyQoHiiMpW2hrtrLfT_LIVpCJ0kI_HWMW31yYhKUI8Z9CDbrjCIPjiwIvCCTXRo8hl5OPk902TXpikLS5NnieYNkQlto2egCENqCoK2Q_6bKALvkH3Xjs5I9ct91m_rxEaomK43jPdE5hgQaHsnPRG6Pco63bGQuGX3EoP8_pPgo1gWeteMMiOM9Ypd9_G_-FPWImN6A8Mf88iiR4bkuzhyxgVYeKlLOB_CkyOviwultZ_ZUMF5tbRqE_gPjpPz3IV8_Y9YQHLwkP0ajtd3WfvkGvvrcHX_QrhNCjrF4ICn6A-ZNaa3AKn69LBdguuTTEZcx_cK1WITBsLwEO8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت مادری که تنها یک آرزو دارد
🔹
مادر یکی از دانش‌آموزان شهید میناب که برای مراسم وداع به تهران آمده، می‌گوید تنها آرزویش این است که فرزندش امیر در آن دنیا نیز همراه و هم‌نشین رهبر شهید باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/447111" target="_blank">📅 15:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447110">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0t3qTEKRXhynbAJdTkJqLmJ0krlmgRr5Za2YIMc-Jyy1F5qCLD2_Sq_L9U_4ema2lIc8MFt35JZtBUgocnmejyL85uJWEqr48X71jcWRFkbA_NThB3TEDavGhz8oX-yreQm7szq7pPYvfLyJZvkTVFW_vGpGNLKYqj5s3BCXst27UihI2Hx8yPPGEIFL4wZ637m-7uEqmW7Av3ozho2G5CBUbfVTbb7r7Npqatvf3c_ACl-15QKyWqyykBe6U9Yy_y6TxeE4G-DjmdD_21XE7OrpoK8kcr8pDMlqbkwiBDlkILPz2aFL8rGM5uWyHuzDNQ3YMCmL0BHr9ZG8kRN3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«أهلاً بأهلك يا سيد خامنئي»
🔹
«وقتی رهبرمان حضرت آقا به دیدار امام حسین(ع) می‌رود، ارباب به پیشوازشان می‌آید و می‌گوید: اهلاً و سهلاً بک یا سید خامنه‌ای، یعنی به تمام افراد خانواده‌ات خوش‌آمد می‌گویم.»
🔹
آخرین سفر حضرت آقا به کربلا سال ۱۳۳۶ بود تا امسال در روز چهارشنبه ۱۷ تیرماه که پیکر مطهرشان برای وداع راهی کربلا می‌شود؛ یعنی دقیقاً بعد از ۶۹ سال حسرت.
🔗
قصهٔ دلتنگی‌های رهبر شهید برای سیدالشهدا(ع) را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/447110" target="_blank">📅 15:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447109">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7823b63ea.mp4?token=dm2lJJA3UGOhq9pn_P_sqnBtLNkyyHjWO7FEucJrYMok7J0A36OphzB611EKiw3JqosRofwBs3FV33qbZVnSE9IKiKxmlQils_IobQTVmYAXOOxPTOFEMAK8AsP0-5rKOchxIfbjl9hpBR2GQxY4KhenErdEW-iWTLyc9hNmNug-wSlCAs0sJ-FRnfEjjgZQmAeMkV_gzh6yXOGHcrDglanMMMd_ws0nSBLzY59cYfq9XbTmAuTc9secuvlaot8-2PDBGn4Q9tasoe7Bfl3C8rcdhaupnpOxFdTtzOwV2QIXQTDaDvsIEqK4mAtykhTu_bbDuV0SlyF7p6RqbsxpRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7823b63ea.mp4?token=dm2lJJA3UGOhq9pn_P_sqnBtLNkyyHjWO7FEucJrYMok7J0A36OphzB611EKiw3JqosRofwBs3FV33qbZVnSE9IKiKxmlQils_IobQTVmYAXOOxPTOFEMAK8AsP0-5rKOchxIfbjl9hpBR2GQxY4KhenErdEW-iWTLyc9hNmNug-wSlCAs0sJ-FRnfEjjgZQmAeMkV_gzh6yXOGHcrDglanMMMd_ws0nSBLzY59cYfq9XbTmAuTc9secuvlaot8-2PDBGn4Q9tasoe7Bfl3C8rcdhaupnpOxFdTtzOwV2QIXQTDaDvsIEqK4mAtykhTu_bbDuV0SlyF7p6RqbsxpRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هموطن مقیم روسیه: فرزندانم در روسیه دانشجو هستند و با تمام سختی‌های موجود، بلیت تهیه کردند تا خودمان را به تشییع رهبر شهید برسانیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/447109" target="_blank">📅 15:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447107">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgnLt8xq24H5OAVsvJfRzZkGfm6jczp-IpzHpABWr8XwuVBEYkPwH2HO6kxAxoQ8P5eKV2vZM6CQBoYXKhHvreF-j58PnaPGbngkjBNcLJcapw3GWmjR2Vetiv6RW6guc3TRcYsfLfPATVGp0t6UoyYyvViihuTMKUQAI2nUUMJQkasJ7HxI0FtboCmsWJeUvUfZlWlcmmZsliAiGxEdn9h8bPOLqp7TgtE9ixdjeUYBBDuwsPEf7lwKnPneJzVrN-mbVd7XV2NvxP062uQ0tdUd_fqJuiO2MmZklMHc6X5k0oiMQRyIdk3dlYBxUQx-FiqP0zc3v9SQColKz9x2vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی تارتار به‌عنوان سرمربی جدید پرسپولیس انتخاب شد
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/447107" target="_blank">📅 15:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447106">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Il0kwBYIVhEeqGXRuKCRoh4vVOE4CgWbK2xcXWzF9IJHH4pnNUymj7o7H2VLjC9LSL51Yb-UDAAxUsQmZSVEQNKb6ZRNSXC1dSJ4zC9XpR5A3Be7Q0reQmFUWjkx-vmuYMoKN-6GgHhj2lxhk5TLkSTLCZbDm5CbBIR_KdxBiO5F96KxA9wo0sWXPpiMJ6fC5I206R-UfGDrOFR4J_naFNHMcGaphvqlIRosMG9iRHgWJdUEKXNH6dywOEirtW0Yyvlvi9iKUsoTGPbOuITYiFsuLBkOCzehUrNk1zMHTSMHXhK_Kc69XIiivk9ZJspYG1tCvfup8QK-F89QzR1GWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نمایی از مراسم اقامۀ نماز بر پیکر مطهر آقای شهید ایران در مصلای تهران  @Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/447106" target="_blank">📅 15:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447105">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/125ff3acff.mp4?token=hwLypEhXckZTX5T4zd5ZqyvOrxwFTCMbTv4_khFKyLqXaq1uQPtYCHl1EuSTgMNPt4cJMhL-SWhNC0jvWXBp1Dh3Qg4o214P6HdZgwR2SGtSx1DHAM3pqzlSBsItLGC5vlGHR-6BLMo26dHWktBxTHTf5SsaF54FBt1EC9pSpeejnZRr7S3J3Us4lrXpj6yjZyajOk2F-5XuSHixQerujGItwKAc_qYUfVoN84425Z_Fjrb5lZ5RJMbhVm3INjDMRagDpRExvLQVV3sM7wIaTtGcQWjjCdCP3HHIBTEgDXYxWyRV_9_35bPOpFxy0lcK0XGyMdUOENesuaWgukN6zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/125ff3acff.mp4?token=hwLypEhXckZTX5T4zd5ZqyvOrxwFTCMbTv4_khFKyLqXaq1uQPtYCHl1EuSTgMNPt4cJMhL-SWhNC0jvWXBp1Dh3Qg4o214P6HdZgwR2SGtSx1DHAM3pqzlSBsItLGC5vlGHR-6BLMo26dHWktBxTHTf5SsaF54FBt1EC9pSpeejnZRr7S3J3Us4lrXpj6yjZyajOk2F-5XuSHixQerujGItwKAc_qYUfVoN84425Z_Fjrb5lZ5RJMbhVm3INjDMRagDpRExvLQVV3sM7wIaTtGcQWjjCdCP3HHIBTEgDXYxWyRV_9_35bPOpFxy0lcK0XGyMdUOENesuaWgukN6zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این بوستان یک‌شبه تغییر چهره داد
🔹
همزمان با آغاز ورود زائران مراسم وداع و تشییع رهبر شهید، بوستان رازی تهران به یکی از مراکز اصلی اسکان مسافران تبدیل شده و هزاران چادر در این بوستان برپا شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/447105" target="_blank">📅 15:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447104">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3b8409e0.mp4?token=bMoXEGmBnBSreu6Vd9cvyiU9lq15T_OTxT1hFENCdUN8vkoDpTD3yqjIAKFh86zbWjx9VSXO1DUAK7i951HQs9m3DpkryiIYc6ckm8eYBPIs7vKpiPQnrVd2VrXKwPydT5QetSg3lsYXjkNmWGdX6QuCqMLe8uKRjdYKwJQMN6KMGxFfbyLAK2VoqffoK3EN3Z4Hi5v-dtzS2-IGW01U2F2z9x8qxf9lnJwte98fc-5r32iGozq8-rIc10fvDOe1nXFU4U1OYDSTG8ui4J58rDP-X4vTuUH003ISzKFk9qJvkv8Q4zXVPWnScSCwe5mJPAXRH-45Z7Xdmo27bNFWRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3b8409e0.mp4?token=bMoXEGmBnBSreu6Vd9cvyiU9lq15T_OTxT1hFENCdUN8vkoDpTD3yqjIAKFh86zbWjx9VSXO1DUAK7i951HQs9m3DpkryiIYc6ckm8eYBPIs7vKpiPQnrVd2VrXKwPydT5QetSg3lsYXjkNmWGdX6QuCqMLe8uKRjdYKwJQMN6KMGxFfbyLAK2VoqffoK3EN3Z4Hi5v-dtzS2-IGW01U2F2z9x8qxf9lnJwte98fc-5r32iGozq8-rIc10fvDOe1nXFU4U1OYDSTG8ui4J58rDP-X4vTuUH003ISzKFk9qJvkv8Q4zXVPWnScSCwe5mJPAXRH-45Z7Xdmo27bNFWRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلتنگم، دلتنگ لبخند آقای شهیدم...
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/447104" target="_blank">📅 15:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447103">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqeVvm6knHl3367DNmdxf6tFPXdX8RgBytv20_G2UhIqMCxdNvi1kUfleIJjEv8eNOUsHfMWpel2fb-416R-fuFF02TLN5TRF9BnrpbyIzeomFtOSi9TkKgtpkd9Zcd5eodVpkoohMic8cpNh72qYuFSDzbGl_G4U6T5VHfm7NAzmUUj72DOSlrqKsdf7OVJRRzdCTv2x94m3mFX1MWaFsotTvimBSX3u-7u2XMZyexmN4Jc_O2VIY1gclTsFIS6n6G3oMLbpqFMTyasUBKA4E8Ho615Ey9b5h6wb5UvcmH4aNikN2Dw-Z8so8qAgguox5SHrsIbWRVXGy3chzwmrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانهٔ حرم رضوی: در راستای طرح اسکانِ زائران تشییع رهبر شهید، تا اطلاع ثانوی تمام پارکینگ‌های حرم امام رضا(ع) تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/447103" target="_blank">📅 15:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447102">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c5a210eb4.mp4?token=Cs4Truh3rgSnSvWkf3MXMUONnWUDAiIhF6MT-BbZXru1JB2yU0E93ZiyjViOrFDGXAUFfDkqD4JHJm60UmEeT2CaUGAeeWTAqZDpQVhPQERMnJ_r7g69mbhUHXX5DfPcwZnx7xOzKnkFqU_kN4xBL76s3WZwmcAE_1CaUI3yUT8O_obS8kuMWPoyU15oVj9HbEwPDdLvpEZr_JtpOLHxHYskx8CeAKBXF_CDMIb_twXxgtyWa8b8bOKkGQ1a_N-RiucndiuyqVp__1acgvznG1G3Lk_QuzkqL-U0gA6bNGGFcpg-fydX_U8PZRlbL56Eod0jGAtkGNmVDcXcvCWo7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c5a210eb4.mp4?token=Cs4Truh3rgSnSvWkf3MXMUONnWUDAiIhF6MT-BbZXru1JB2yU0E93ZiyjViOrFDGXAUFfDkqD4JHJm60UmEeT2CaUGAeeWTAqZDpQVhPQERMnJ_r7g69mbhUHXX5DfPcwZnx7xOzKnkFqU_kN4xBL76s3WZwmcAE_1CaUI3yUT8O_obS8kuMWPoyU15oVj9HbEwPDdLvpEZr_JtpOLHxHYskx8CeAKBXF_CDMIb_twXxgtyWa8b8bOKkGQ1a_N-RiucndiuyqVp__1acgvznG1G3Lk_QuzkqL-U0gA6bNGGFcpg-fydX_U8PZRlbL56Eod0jGAtkGNmVDcXcvCWo7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حیرت تحلیلگر آمریکایی از حضور پرشور مردم ایران در مراسم تشییع رهبر شهید
🔹
کریستوفر هلالی، تحلیلگر سیاسی آمریکایی که در میان جمعیت عزادار در متروی تهران حضور یافته بود، با ابراز شگفتی از شور حاضران گفت: عشق مردم ایران به رهبر انقلاب و انقلاب اسلامی باورنکردنی است».
@Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/447102" target="_blank">📅 15:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447101">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d75d22ba7a.mp4?token=AQvbCL2wJREm368wlyebxitp8oCQ-g4qapShUIxROth27V3Z3taY0U9zR9Rxr4F_mHUVs4A3BQjA272kQxbOC6QzprR0e3WqKdyB_TXHA6CXiJrxdMbScaAzRoh2OdNaxWGDIvjzpA3ktjUzEBs51XDiZ6gJr-SBkydOsBg2oRhKt5pjWOBq060WJ13tMwyLt9ucNjNemOXCLdZENlk3DqrC_EtsrMNpUSRXmOYfpD1BRxawxrwUxpMEDPlUKsAeihthZnHhh_7X7nctCRMGMv_JFH-K5tV8CxQJiAgpo5LJcTawtNHc4sV1AaXdGmZ5Nf119hM5h4argV_yoL6hrmyGNgJiONDej84CVuE1j02B-7JemhnG3tOp-2UWlch8f3CILfYveQ66KFbO4lisLJ3sabDfH9NtX_6cLOqHrNqrr1xZaysXCkRBwi_GA0_ovT7uhoMfCfz_I6f0HI6Tm3uUyBfhDEXhUMjvtf1jNP2z_vIvGgorb7K6qxNpTTTA7DF9L0G0Pkwwtv5YqDyRmIxLHQk4Wxgw-r4yZzhus7-z7PDxfbUh-08R79McQEMZAE8DNEmmq3CxXJb-2ypUvKH7_qv7K_6RtGtWmnODavPYHOtLkSwUQiXXHsJ816sPwFkT34hPcxB1UDdDIvcuDZPDWc9oq_7usP11AOM6MY4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d75d22ba7a.mp4?token=AQvbCL2wJREm368wlyebxitp8oCQ-g4qapShUIxROth27V3Z3taY0U9zR9Rxr4F_mHUVs4A3BQjA272kQxbOC6QzprR0e3WqKdyB_TXHA6CXiJrxdMbScaAzRoh2OdNaxWGDIvjzpA3ktjUzEBs51XDiZ6gJr-SBkydOsBg2oRhKt5pjWOBq060WJ13tMwyLt9ucNjNemOXCLdZENlk3DqrC_EtsrMNpUSRXmOYfpD1BRxawxrwUxpMEDPlUKsAeihthZnHhh_7X7nctCRMGMv_JFH-K5tV8CxQJiAgpo5LJcTawtNHc4sV1AaXdGmZ5Nf119hM5h4argV_yoL6hrmyGNgJiONDej84CVuE1j02B-7JemhnG3tOp-2UWlch8f3CILfYveQ66KFbO4lisLJ3sabDfH9NtX_6cLOqHrNqrr1xZaysXCkRBwi_GA0_ovT7uhoMfCfz_I6f0HI6Tm3uUyBfhDEXhUMjvtf1jNP2z_vIvGgorb7K6qxNpTTTA7DF9L0G0Pkwwtv5YqDyRmIxLHQk4Wxgw-r4yZzhus7-z7PDxfbUh-08R79McQEMZAE8DNEmmq3CxXJb-2ypUvKH7_qv7K_6RtGtWmnODavPYHOtLkSwUQiXXHsJ816sPwFkT34hPcxB1UDdDIvcuDZPDWc9oq_7usP11AOM6MY4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماییم همه مشت گره‌‌کردۀ رهبر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/447101" target="_blank">📅 15:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447099">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/196556812c.mp4?token=Rd7RkfDiCg6IFcZYiYwR1nGjDuTMyoc_j5KKsZE9wYl6HlDxvIh9RVtwVSaJLa1WYxg7gA1YBzqfGRCoTAtHnHhJhBTvw9Q5xUpa7tdUCZUMI7hNAf_G7mNcHTRZTZIAdGZpf7iElbVFfvGNcFkHrLoTsZALi555PGKJ1tcLixjYkOCgbyrEBUvR0VheQ3Ex-70smgF0NZdR4AmGKRI-lY6zLouc5IbvLNsuNZL3Qh5CsuukvoqZae2v-gkWLPYCNwQu719Mp7TbtyGKq29tcISEo8LRYfKuo1cmn8L3kVvNl3VEeI3tsogXwluZz9IZ427jE1XmFxrxrTWr_KaSI3FiNVyjT5tPKbEWUoLbr6CNUaj1WFSehb3eFRzGiX2aXnuIuZV0Njd6IbgLw4_jNdtzNW-gn2ottra1NBI1FYa5cKNht-LZPmocdcskiT-dgG3BYhYfStJ5a2g9ULG1JXwOVoUkDjzTlwSHZ8ybXl0hcULtxx50DkX7vxRe1DP5uGHo616sKOE3UzP0mz_zz7NP5nL2QMKthJCvJeFGVmhv65QfesZTYAusqG193ciPvt8n41Zfwa-RptGkFhVvrbHZjuDIHvse-1IpJT2jkZxpUDjmPIC-LDGzy-f5wl9YWq56RpmUpn_VIl7eA4ZJ24xQw3uoKzhgVHz9LEORh4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/196556812c.mp4?token=Rd7RkfDiCg6IFcZYiYwR1nGjDuTMyoc_j5KKsZE9wYl6HlDxvIh9RVtwVSaJLa1WYxg7gA1YBzqfGRCoTAtHnHhJhBTvw9Q5xUpa7tdUCZUMI7hNAf_G7mNcHTRZTZIAdGZpf7iElbVFfvGNcFkHrLoTsZALi555PGKJ1tcLixjYkOCgbyrEBUvR0VheQ3Ex-70smgF0NZdR4AmGKRI-lY6zLouc5IbvLNsuNZL3Qh5CsuukvoqZae2v-gkWLPYCNwQu719Mp7TbtyGKq29tcISEo8LRYfKuo1cmn8L3kVvNl3VEeI3tsogXwluZz9IZ427jE1XmFxrxrTWr_KaSI3FiNVyjT5tPKbEWUoLbr6CNUaj1WFSehb3eFRzGiX2aXnuIuZV0Njd6IbgLw4_jNdtzNW-gn2ottra1NBI1FYa5cKNht-LZPmocdcskiT-dgG3BYhYfStJ5a2g9ULG1JXwOVoUkDjzTlwSHZ8ybXl0hcULtxx50DkX7vxRe1DP5uGHo616sKOE3UzP0mz_zz7NP5nL2QMKthJCvJeFGVmhv65QfesZTYAusqG193ciPvt8n41Zfwa-RptGkFhVvrbHZjuDIHvse-1IpJT2jkZxpUDjmPIC-LDGzy-f5wl9YWq56RpmUpn_VIl7eA4ZJ24xQw3uoKzhgVHz9LEORh4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بدرقۀ تاریخی امام شهید
🔹
این روزها، تصاویر، روایتگر داغ یک ملت است و هر قدم، روایت مَسافتی است که مردم از دورترین شهر‌های ایران، پیموده‌اند تا در آخرین بدرقۀ فرمانده و رهبر شهید خود، حضور داشته باشند.
@Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/447099" target="_blank">📅 15:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447098">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfe0ef585a.mp4?token=VyrLRbZ8nCAo49FUJilL5aXeAm0rO37PfQfKSqBQy1NwwmmT979w-I1DPdTM710c-OYpSj7SFT2L-e_e-vNzk5BJl4D5POkQ2CIYQTrkQymVcU48-8t1tGLxqBkERW0MmfRGHYhirf8P0XIz4rvg36aqFSmzQx9YiLuUloIMhhKyf_rsMgg5wM3isB4rO1PR8Qwj08Q6GXaQQlzJ7-yq2ssouiNfvAAWPIJ8Ae1O6sYDPzlMn3Fp0wgbiyQ7pSjeSXrWdfNLz7qmPqiGyzF3tqkz5ButI_dsUHKz46tHOU2BAae6mc6dZ1GLI40bO7K9phzOnW_V0sprM5F8Zy0lwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfe0ef585a.mp4?token=VyrLRbZ8nCAo49FUJilL5aXeAm0rO37PfQfKSqBQy1NwwmmT979w-I1DPdTM710c-OYpSj7SFT2L-e_e-vNzk5BJl4D5POkQ2CIYQTrkQymVcU48-8t1tGLxqBkERW0MmfRGHYhirf8P0XIz4rvg36aqFSmzQx9YiLuUloIMhhKyf_rsMgg5wM3isB4rO1PR8Qwj08Q6GXaQQlzJ7-yq2ssouiNfvAAWPIJ8Ae1O6sYDPzlMn3Fp0wgbiyQ7pSjeSXrWdfNLz7qmPqiGyzF3tqkz5ButI_dsUHKz46tHOU2BAae6mc6dZ1GLI40bO7K9phzOnW_V0sprM5F8Zy0lwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات مسیر تشییع رهبر شهید انقلاب و راه‌های رسیدن به مسیر
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/447098" target="_blank">📅 14:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447094">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOQr2W0fHkEyeaCEULL7Cdi4CcAMXCY21z5_2Gn1c0tqQlzDU_0SmpW9QKhrDQGuUz6Ep6HB-RdivFQE0qCFqZQgRu2Ly2d6N4YaeRds_eyxLkCuoEPPXwC3q8NOspN300JPZNTi7_fdvEKOMlZ85ycibXpkcIcNuhvg4vjL1TEXXqHmfFm3SP62oALGs2QgOqQdIWRapqOJwqgP1rormT-n8_6cxRpKfWn37NW_4H6VieWSPv1gk5QUSBmNlEkOoXeiRm7RNUyAjwkFgRkFa-HysVM1DZX4-_PTZg5XWrces21SRkrwsqfkYPZAk57YcsG-yFLPmemc54BXEp6e2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k19lyXW6Yvnp6QdCUqH0LI_oSUs9v4EnvCdtSXxHaQD-mmJKc2Mts-8i-NvmYTqcIGrEyMDhmvDHwp0NIvl29QyeeiDVmleeiXyNcv2k2Kki6DiANXPNZ0Go7GVbeWbBuaFO-1cLHgztTxf4Wx_ZFfkdVPVJgsmVbNnA27lnB4PWTRzgSsUidY9uzccBG8E-0yYk3PG33azsnD2_2gKR9QvlXHLZy5fwFj1kGpX1lytwBCcUE-WIfRgiOEUkLlr8EWbICM99DpbMvgdfV-V3L_SAiBfiXMKDmLZvaaQJXxqGA0gGExXYo4r9rpSSEoDo6asUsSbSycqeqyX74K-rmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jMzTNqq_lOLC_XRf4qPWE8yj3kV72dhDvn_cENlNCKWCUI5Squ6SYzwEmVuOtnebXBCqlY7RHRnB7v13aLt6I3_7HJJp24nMPbq2nVHXHFCVFHyKnb-lmYYrszS7bawY9BT5ouyZ76dhGzTUaWR17RWfIn6BqeKKndQgbaRy5a8inKWpFIa34E498EbDUHkVEf3XZfwCpTkF0RpCBFgMXMRh7UExkqI-ongsfizrUhWAIyeO2rpBBAvClx_4oQVA4RGD9R_prLUy8bD6Zphq13QxkRKAKPHYu1vY1a2Lvciq-iV_9EwcDwwsvGslI9yTyfpYpzz6Y6PLZVujKS0Dcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hp_xTwIqPEEW1iO75E2Hh7MMKThQB9LJYFa8Q1RUoLrkX58ifDWykyojHOWtUpssP4SriChizHoxXpZMbO2wNO7cHQHfU0s4ucMASecDG0f8cVd41MeLhqRbn5dxzrc_z9czmxTorsYcxkwG1jHiBHMecSvC_vZCfnhLmuXuxQUIzyAiRbNHe57stJTBOc5tfoQFUidzKmrv-b0IdeUMAxobTdXH2WJ_uGCCnvg_p_Wt5haaQIaIsIHDInVuPfCl8_SDiY_-E888fY1rF7QtteJteyHmjMnaPkYOcB4eD_R_TWWzCuNxr8UIBQYEHm9N7Oja7ffBvT4hdKCt_qjQHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور سردار وحیدی در صف نماز بر پیکر امام مجاهد و شهید انقلاب اسلامی  عکس: زینب حمزه‌لویی @Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/447094" target="_blank">📅 14:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447093">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cbee8f7d7.mp4?token=QV_EU1eVzNu8peJ2Je3PiH-cX1KO-zoLsVxSJHRQZz39E_gNqHRwWOTorHxBPIe3g8tqBFyaAnaPfQ_XAOKaWBp_u2Fo1HXubmJMMHKHLULe83yW4m8X3XnxvaoYpgZ6sgzlMsUzkUaLQnjVtnmwZE4V0wLOcp-KXp0bUA2ANmLOmHJweYhGWnScYa_vFUPw5NldRr9J39kAXN-WGLCkvBP3R7BWopkp0LYqrvcJpIZw-AAwV3jPAmWqHBbIkAWbkZ27VLVEkZRkLtB5BjyFkLbVm3Y5wHZgEzBHvDGDCKAXdyTF5h4MIjVVz-uohHQEfuwLi8f5HYCxpdyjHCd-Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cbee8f7d7.mp4?token=QV_EU1eVzNu8peJ2Je3PiH-cX1KO-zoLsVxSJHRQZz39E_gNqHRwWOTorHxBPIe3g8tqBFyaAnaPfQ_XAOKaWBp_u2Fo1HXubmJMMHKHLULe83yW4m8X3XnxvaoYpgZ6sgzlMsUzkUaLQnjVtnmwZE4V0wLOcp-KXp0bUA2ANmLOmHJweYhGWnScYa_vFUPw5NldRr9J39kAXN-WGLCkvBP3R7BWopkp0LYqrvcJpIZw-AAwV3jPAmWqHBbIkAWbkZ27VLVEkZRkLtB5BjyFkLbVm3Y5wHZgEzBHvDGDCKAXdyTF5h4MIjVVz-uohHQEfuwLi8f5HYCxpdyjHCd-Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قابی از لحظۀ ورود پیکر مطهر «آقای شهید ایران» به مصلای امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/447093" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447092">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7de39fe86b.mp4?token=S9MWY4VcKJNUa1QYkAqWN9Ry98DBn56s4aV6B6fU343QFdQKNMLumTHY_-ZCrdkylaAhtAOrakE81b0BvH9Ssk8_P6uE5KZeg0o2HleqxfePhTL-k3IADXurSHIGXwjxTutMM_VhR7j2tlo_LhlACynCq0Yyiuk3Vx_E-xT3WtaIS3AJDvhwKBpzJTXp-3SpL54ZqBHlIps4ZOtPSdvViC7HVfFtfVX_sxNshLrCae-Re6Mn-pysNHlQQrNJ6vqGC_wiu55JRHVFqJ9cPG6wPFnNB8VQ1qyxNK2tdJDmWWVlNPso5jetsFrjZgeYe7bzA9_M8rMo7k-6Z_aaD_Y5RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7de39fe86b.mp4?token=S9MWY4VcKJNUa1QYkAqWN9Ry98DBn56s4aV6B6fU343QFdQKNMLumTHY_-ZCrdkylaAhtAOrakE81b0BvH9Ssk8_P6uE5KZeg0o2HleqxfePhTL-k3IADXurSHIGXwjxTutMM_VhR7j2tlo_LhlACynCq0Yyiuk3Vx_E-xT3WtaIS3AJDvhwKBpzJTXp-3SpL54ZqBHlIps4ZOtPSdvViC7HVfFtfVX_sxNshLrCae-Re6Mn-pysNHlQQrNJ6vqGC_wiu55JRHVFqJ9cPG6wPFnNB8VQ1qyxNK2tdJDmWWVlNPso5jetsFrjZgeYe7bzA9_M8rMo7k-6Z_aaD_Y5RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نظر فعالان رسانه‌ای پیرامون شخصیت قائد شهید امت و حضور میلیونی مردم در مراسم وداع
@Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/447092" target="_blank">📅 14:51 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
