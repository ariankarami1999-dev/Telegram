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
<img src="https://cdn4.telesco.pe/file/sY03fOO74UUqHjBwbIYUHnNakDRd_FWvEc3vMxQWpkj93fGTSGMN6vRgHYzTKCR5bZSoPIw45Dcr1iO9XknY9TmLARE62SAylc7G1tQgTTkjPsgZJ7TB9-DrkDfW8ULn3A5SsrC9cijMMOHJ8qRMiYSNOj5P0L58VX2KILWL99yM8BOqIBYqmea4WY-JnYIVUVUW8Pfsz8l1_Cgahn6nF4MRNM_eZu8GV4TvQoiCBs1cs8xGHvObU3hHGWzRDCu2HL421TSTJo16cNhU7Fl4esKuoKTM3yvphoHXKrqxsdmdsxf_H8CvYk_bkmnpMZq0D2t407-vBp2iYBMlr-pLdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 364K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 13:09:54</div>
<hr>

<div class="tg-post" id="msg-24857">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRSl7x7bo8zqZysfbyp0sHOYVG4O2JCxcopm4Y18JoTPhPyKFTR2AoCbfymcY__Fj8wSEC6u_w2XnWsrHGRX2cZ4Qhs3f8yt85WI1nl1d0Tkp3Sz8jRBjnyYVMKWHZSkIyhCtv3-CXXT3rXqVr3pt7alEKekl23Aen3PXnRUXFaMGgZujVTd5QALgBimfRnhlOSbSonqJ9sPpFgrHV8oha2aRRJ0Zy1y5EEIlFqCXSO2N2mCTeU6o5lUrLq-IhdMeoGyMQvthsIXAERvOSlGpcnzbIGs-p5I-DZmNYsWfFixchEtCBzD14ETipYRbBpp0fA65rCZnAXF89xpSoOLNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/persiana_Soccer/24857" target="_blank">📅 13:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24856">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idPbfWE2gmOO_eG2Cox_gw1eduWAEMVK7_pNJCxhKplR6AV1suyvD-Wxat4a5JBrI8k_QHEQxW8Y-zGxiAd9S1TdDACXZ6xJpLZmlzUgmFgm0g1kOjAdmx3viiCqXi3tqiTTHvXI4w0bMedob7t-_5xzyHqI5BMz7irok7fWZBWujvs4udKANfZDvCkeEJNc6UgxUfT8PJtxOO_GpLvNWtqhQQyqpZdHG07V2oNLyzvmkXupBjiKmx9qcSu_z1kGAECFimGnnvZIiWfr7SYWVvGoQtkI6bUnnvjYm4Me-OQi6sAIi1T5Pp24W5mKKi2Ndo7f2OM9fXXc83H-QDBBsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/24856" target="_blank">📅 12:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24855">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhqwdVP7f9epjtHbBWvFAFpB3aqept9TLqIwluw54_sohdRd2cxo-bqDJ6sUaI7kuvguC0Ol_OhUWdoXr7P8ZFBSLGZjCWeDZx4iJ5D_lzTlTX9zObBBSCe_PEd4V22KyV_IqbuEo4vX9jltFMymRzvlmxExGNnH0-sUShZxzMBspd3XkeOhTuMEHncFhWxOxoKb6IOC96podfB-K5w9BRrJC2iAzEPoOu8p_4__ji8LdcnBcx5U2Jp_uGItzP9pLCmV_aQsJWSBDSCfER9FA9fIN6kQWkVrRC-cagpj0BeAjj9CEDj9fd0lzhdCYXZQcfZ21j6hQnlw-mF0IWJW9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/24855" target="_blank">📅 11:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24853">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjhgvK8kvbb6JM22Y_Z_2vsexBlT29RCJndJ70dKo0i2qf-W2-dbgLMaMoyoifUk8VR-LVgLTH0UyKblvaI-XKG36gxQOnKR9R1VZi_zpoR2sgfmWmSWep547fv2lmW73M2DXCIoTNmUY6a-uDWa3N102AXMOyynAtXtsRIjoWd1ncpclzp2DFCTXQPfkRPhx8AMRT4JyxW8ZNpmYBFvi64vvt1YDEBhDZBfHonrWDjyQ5mp_tSe5cQhgkcI7Oclsk3YkMUOJB2SgB9LrkeC_0SFd3KVXXArYD1fJvg2Am2zjETIkoSHvXRA9hQIE3UgHjtOGW8fWJ1tCTh2TlS2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kJ9vVu8EoXm-GXTXCptmzcGmHc9uCCkBIGqjAHiJ3sBHyvZyThnSjx8oKxnSV-hgGAH2WN0ksVW0PRTuSYgRcQQcTcT4WAmXAUYoD4WBRNIg2mVut9JCIwnc-c-Q8rphNXR-rQT-a02SUfHZS-ZMJYh5f9fKaCQSJ5H2Sa0S9c5G3JrzhmSNFgisKKfpBiXi27X_XbnXHKz3E-i8wxWYyrvJmQKK9kPsI2v9zyDEvslI1sci9GhGqiFi_11-2hLuU2Xitd8oEUc1s9rdhlPsol-pL5Ukx_YDKypaijG3mxwSUcvXPI47qPuVNL2sRXZaIvyfF-I8Hc6erxe_Jiu_3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/24853" target="_blank">📅 11:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24852">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=W_rJYewke_RRQ8m2Gi07rgGm30Qc7CHVVIP1_1kw5Zrfi_ZzKwB0Ezhww_ZUwox-6pf_lfcdgxrA5c7HC-Bz2DePbXISARl3KxO4Ip3E6O7OBUOUWci5wzCBc2kBaEVL85NzIFIV5gHTKZ8JsBjZ8fA-qN2ZWdO9TS7pyqi-D3qRhTdwDW84JVdqzIa_vTBqNWBodABj_A5ULRT6h--qyhXJaekQ7WzaVr-a8XhtPV2Zcimc48yyoL-RCon9Z8X2rsNG52xXV0t_u6b864yqmOVZzm-5i8K9GLCddqh64quFxlBYsPb94RP7RT-gxfQMoCmTErcYtV0YlHbVsDTg0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=W_rJYewke_RRQ8m2Gi07rgGm30Qc7CHVVIP1_1kw5Zrfi_ZzKwB0Ezhww_ZUwox-6pf_lfcdgxrA5c7HC-Bz2DePbXISARl3KxO4Ip3E6O7OBUOUWci5wzCBc2kBaEVL85NzIFIV5gHTKZ8JsBjZ8fA-qN2ZWdO9TS7pyqi-D3qRhTdwDW84JVdqzIa_vTBqNWBodABj_A5ULRT6h--qyhXJaekQ7WzaVr-a8XhtPV2Zcimc48yyoL-RCon9Z8X2rsNG52xXV0t_u6b864yqmOVZzm-5i8K9GLCddqh64quFxlBYsPb94RP7RT-gxfQMoCmTErcYtV0YlHbVsDTg0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
از دو شهروند بلژیکی پرسیدن که حاضر بودین به جای زندگی در بلژیک در ایران زندگی میکردین؛ خودتون پاسخشون رو ببینید‌. چقدر تلخ بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/24852" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24851">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=v0WWt1U_w8izlAU84P8NRqHfAESVs6NoV7HwID9kMmWHEv-zc5NeWr7OuO4HVOSoWqn21mzpwECihsWnwZFTSZ-xyTw0hxPryss65AqVLWvPUozSWil-94xiJlBFwWOK486I9Ktmc9LIw1dcFFqbFaNdjNwHJQv5s59YpRy7G4RG-dXSa8LirQFd3tS7vjTvxooiNsyVatpvyD670ASAomRkwMPBwVdvfnsX9SOD_gGF1Lc4whoHwZXSx-Aq_zhs23OlT73ahkzC0lYL0FgOTbc4kMEPNa3ZAthwRxgpS1BNxcFyJcTuO3MVJzqOJwLkwXp6RzQZPb6KPo9C_f_TOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=v0WWt1U_w8izlAU84P8NRqHfAESVs6NoV7HwID9kMmWHEv-zc5NeWr7OuO4HVOSoWqn21mzpwECihsWnwZFTSZ-xyTw0hxPryss65AqVLWvPUozSWil-94xiJlBFwWOK486I9Ktmc9LIw1dcFFqbFaNdjNwHJQv5s59YpRy7G4RG-dXSa8LirQFd3tS7vjTvxooiNsyVatpvyD670ASAomRkwMPBwVdvfnsX9SOD_gGF1Lc4whoHwZXSx-Aq_zhs23OlT73ahkzC0lYL0FgOTbc4kMEPNa3ZAthwRxgpS1BNxcFyJcTuO3MVJzqOJwLkwXp6RzQZPb6KPo9C_f_TOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/24851" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24850">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B42rBsp0JGdN3eNIHIjf-4iCU0YjrLWXw8_Oh4zVW0U6mNxRU0uB2_ZjASmSA_gB9CPfaPJ15nMFe1Pqi6lG0robeF2cmCSMMYhcM2MIn0MuGNT6gY5oAMuTsxTlucBRJmcUuoh7oW4D6CcjCHd5X6caSRNk4skWGZVtlOfjKCRhfZqY41OEdSIKqESZvG8UAn8y4812_b17MlbuQSd_yLuHCd8Km2fJM7rDr6zL9Ql-ltk2MGEVBH16suyzn6U16bxaC-Obc_vTnBDb_R3lmy8XvkHnjfNGlDT0NmcXYrKudm2qFAYZojHEosXWDHaKa0ZGRTAk3uNJNc8am916NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تجربه پیشبینی مطمئن با
🅰️
🅰️
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🛍
ازاین‌لحظه‌به‌ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
🤩
🤩
درصد برگشت وجه در  صورت باخت
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r12
@betinjabet</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/24850" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24849">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C63g1KuXvvgGV83-iDi5n5V2P23NUgxW7tRFs_YCWTeWnLUFB2HItaIt0X5KB0z8-hB8h7a7QSTQ6XYAfgv21oCQLiA7wllc6iQBTsjPx7z8THaUxlubuTGQROfnxV6UzJ90rXblIEwps2bMv24RrtB4N3SqDSfYBWqGHpNjJMuWchn4DjfffvAl_MbhbhbKaot7WInvhJCWmLPbiL1zdfOsnfwLzzfYgFKpy2UPRiGKaymZ4Fz7w49WkDPbpMeLGgweO3WXc_kC657a0IxC1RsjsIwY1sK0w63K-0hDPcEuilOnfkkMc2mnt9e4ja0Nnk8ytCYiGJQslKuHNG_Wsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه سنگ اندازی های عضو هیات مدیره بانک شهر تموم‌شه باشگاه‌پرسپولیس‌از اسکوچیچ رونمایی میکنه. پیش‌پرداختی باید پرداخت شود تا اسکوچیچ وارد ایران شود. امروز پرداخت شه فردا میاد. پیش نویس امضا شده اما شرطش واریز پیش پرداختیه‌.
‼️
دلیل مخالفت اون عضو اینه که…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/24849" target="_blank">📅 09:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24848">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=LX7C0Abx0G3VvMRx5gDxIFBuCnMVPaO-VLX8WxXoI8hfeN73zTiwgP566ZnGt4cs1W65lrX9nI0xD4_-TXX3AbJi833LGFfqwFXqhuTY9NaSMnmBXXeI8ZYP-8mVn8w0ufG3EPnejt3rgvJ__GSAOU5sec1iXwvttbjE16GaQP4nOqpOvq3HZA8bEgM1nA_me2jbUOhxPzUK9wGpzClV5hWXbovA_5SImkH_8GmmDz0OpVnHh3CNFRHZfD-uXokh_4hPD84J4JMKE4UWg3be2PkQQvFsrfN8Gzo1S5orc3Zsz2q_Smhdke0xrKNeMSvHld0Lq3xEFYVbSxFzAtcEXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=LX7C0Abx0G3VvMRx5gDxIFBuCnMVPaO-VLX8WxXoI8hfeN73zTiwgP566ZnGt4cs1W65lrX9nI0xD4_-TXX3AbJi833LGFfqwFXqhuTY9NaSMnmBXXeI8ZYP-8mVn8w0ufG3EPnejt3rgvJ__GSAOU5sec1iXwvttbjE16GaQP4nOqpOvq3HZA8bEgM1nA_me2jbUOhxPzUK9wGpzClV5hWXbovA_5SImkH_8GmmDz0OpVnHh3CNFRHZfD-uXokh_4hPD84J4JMKE4UWg3be2PkQQvFsrfN8Gzo1S5orc3Zsz2q_Smhdke0xrKNeMSvHld0Lq3xEFYVbSxFzAtcEXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛
میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/24848" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24847">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wsub6-Ev98OQHQ1hrgZZbFla4PqbUui-tKBUk7fSByeqph6VFGLeITeQpN-RdbiMCpZNNe_Wa6pg4e0k37Ho9DQ4XOgzNet5SgS3xtbbdEyiqPjFYnKCjB6wEi9COKWsZpZmaNYYfV6zk4N8sEbmAc8pB13VJT7344hcWjVUbfIinx7J_8VwJiHdac1n2sOPXuHDRUby-kZe_9AuPycFP-mZfcMan_HylNglruaN1w_jXk-1RxMbiOaLbasDhUUVvBNKLmovGBGHEFF_tAUdh5kfbHUwVUyj9Ut6FiaxnffDBWTij8DpD5AJh2CZvoAQ5AR1J8XduYHmbyrYP7o7jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/24847" target="_blank">📅 09:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24846">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUSdhh3JDaeDpY7rR33BKpl-TYwME5byAhgmVP4_6toUeZLf1rJ1furMrE9DApEcO2BLFgXc0d-wJRLtjSirTxme9Z2fktPg37-n45QC-Z-26XQIVa8Qgc--Bizx5HsKseLR09WMjs3UJJJivosRAK_GH1S8xytAD1Kau2AT_RSElBqdZxL73Pf2lcilZIO1tngl42rpMs00-zNCPzT8Nqbt1KI2sQEvf87COUUREh1zRXdh1MSqywhg9NUQdAFn0XbVyyY7DSprohwmhd-pqDV3RZrpgUgvXEIU7PWSuot62LXfbJKDEuRtuErAGTywnKDBBYXIx-EUw54uf9s6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/24846" target="_blank">📅 09:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24844">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZJH_DdQV4R3BEI8f_1c4yrnsa5qB31rX1HyE7fkniEJQ6fQKlrbE_TaFIREJ30Qz0r2Y7d5dWByGLkLqJQoylJ_FgBpRQSnmI6bEhGrVT1O7mgYHJ6dz8WwIYwDfjEpqkcIPdafPfAvgRdnEoLzpypdikcT-sL6vo-mtPOrYDJ48rJtJCtrr_LHPO2iivrlvARE23qmWF7Hi4JacLowz0mnDW9_Qp1d60vRaVD1v62rFJReWKhbNqAt9R8v9yEO2ERZ1Gnx18XxJNghro0MB_V5-bbMAun74lT2_W3wFpYg5VCO2WWQeRWALRkVhL2VVTBvOHB3ZLv-9KdOI4cu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ao3XEIqoEe35wxzH6olf-SEff9Y83Vcol1-HmlR1DfGRjZYp6Dyed3nlMcqbl7ezzOM6KdB06kzxwSJsqD90PT72lH75k60UhEAt6ZpnjTOTwki_66EJA_z0hDECskDSLRXzqUjHaK5bDLt48xX8Bv8b7xCxzQoHKtfE5ejXADT48o81PnqdNlNqP5NHMli1XAozFVutV9OUWVvEAQ9xaWJHhz2C9CaNlphfjtbQLRyi0IPSD9x__HpPg4TjXOVtZmMzSAr7npERZbGUwMJ-fg8BN7NeHKeZptmL57oI1qPQEEbQdJ7892G42jhTFWQWWyjX4kXcA3QPOrnBmxe8zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/24844" target="_blank">📅 08:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24843">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fr7U3ar2gEYMgYUr2F_9mu8gby5XQlnE4KRXeS3XnOniyMt0_Hj-JIc649u7A8GgPtN_joEn1GkFkeo3EvdhD83iFSIRu3RKwajk7WI4TMNqeFfjNR8Mdm10M8K_WWbmFb4Hqdozhed1P_VA-ykY3h5SysRck9gl8Tzf0FouCImGlh7lxZUb7vOSr9HEJmP1AV_K05hxPjZMvuFio4p28eFSkUzOwgAPyTsogZQ2v76v-m7cRO_sedEwHaeLr5AuUfQphQjQjDgZzrsG_lyG2pE1RuNF4x9HuHSmfeM7S5_faskIS4x2SWSW85IRyRbWGK1oiJTdO6du_EzQUc4bCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/24843" target="_blank">📅 08:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24842">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSEYlIMXlUyVlUcmWWsHKzu9F17QuFbHIhkSTQLyoxGK3MjEXyvXINuc3VHxuOvRLQMjeYjHW4H_wIObxUIUYkXT754vpE8A08tgA1krwf0ANy25CJ93KWZmWIgiDHzhYV1y53Xa3Vl-OmbCF1gtFl22PuG2k1S_feoVECfizfO19Jo7tfqnZ4A90-9Lod4K-0ER5qCP-HeeMPvcAKYAriQC5RZu1bzoT4K5ZcB6OPOyhNHEXpDwnp5VnsBoXfeICmmq6BjOSkm5TW4hSTj-80myyC-yxLk7LnFUdkaukDhzBRjAt33FAjzzE06T_8m5yyoALHoIW90LDX59rRSI0RKY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSEYlIMXlUyVlUcmWWsHKzu9F17QuFbHIhkSTQLyoxGK3MjEXyvXINuc3VHxuOvRLQMjeYjHW4H_wIObxUIUYkXT754vpE8A08tgA1krwf0ANy25CJ93KWZmWIgiDHzhYV1y53Xa3Vl-OmbCF1gtFl22PuG2k1S_feoVECfizfO19Jo7tfqnZ4A90-9Lod4K-0ER5qCP-HeeMPvcAKYAriQC5RZu1bzoT4K5ZcB6OPOyhNHEXpDwnp5VnsBoXfeICmmq6BjOSkm5TW4hSTj-80myyC-yxLk7LnFUdkaukDhzBRjAt33FAjzzE06T_8m5yyoALHoIW90LDX59rRSI0RKY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/24842" target="_blank">📅 08:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24841">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqhZU6uHNZm2T1QY8glJbp5e2ury-RwlfvCdAebu4WroGSm_SW4FZs0HSiVdZ11fIrI4RxPN4byPr0V05_gcfIewDSN8CGAxGCN7PiLX6YTZk-SFVOvDy57wJnR2CNNfuQj9E_-2EUO_5e3FgM0KEDWlZfl3Lk8zrZpWU63vjf2NmphqwXUqzEOZFk1VaH9qtHeEpeoDaWZB0OMFlNXDiy0-qtV96dAOZafcgLJUKZWZFNKIKFlZV3cL69xwthWJq1e89pxSG3sOI3P9wF_lkEql4_pjc1tiUCg-EnCm0qO3THcJEa1J_H1Lbj47ixqvYg6ZfZWGgTJ3NpvejX4euw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/24841" target="_blank">📅 08:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24839">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anbSbDZktwwjSk6fK6Tbjpk7ZvTr25LzIuUTsMbFZVKyB_ffy6CnRn9mSOLP408mzumr1Y7-CC22VkNpZBHPbE7UQarrA5nYHNFXBc8iJL5kkynZc_HH5VCD8sLXoOX-eoc7hT0pFXBiRCib7dLY48Z3HdyKO7AzwXwlwXp-sLjAry1dnRCoI9ZLnbHJ_BF7SpWNwEuUjQukizbnO5u5tV0tYbZ2778R2yridNBLzRycgKLuMzx5hVLU-NFPXQiL6TRgRTmx4lLNWgHhCE1Wjlu-IFIgZbnhwoTUtvSBbYz9M75kgqkFhELQ-MWR9mkq9I2yVGLb7ZXsx-39NDzd7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24839" target="_blank">📅 01:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24837">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swlr9SIaCrOQF4UWOreEPwTOScGoYV4mfQplUWCmdAG6kmQY5eEdMQO6EcTpGBPtJ-LC0PbaHxOE0FFlLD6gZPaug1g_y3p6fCc3bUR8GXZZeGlYEDKyVURd60m_574EXzCtIjmzJViOTvUQTDRAN2IcQ9Cni8joMovyvkK9omDEfPa5O2ot-vLUeHbOkXIkGCLs5XRFxi1QZRPvmQOaGv-NKOnrO3jsY75pfVrJjaSHbs_VpeywgFRrd0nNI1M8r_MWo3BRBJD5UJ9iwIGxL8w8nl4b092Ac4suMa7QNAWbV3ad-oLPXb_06FOQ6uVHMCijc-v58qzAOyRJ-uJJ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSszuRasUzDwaXcd5rvbUBMJnSKuIA2bWq4gT-H1VwRo8-y-G29EYc7KrFI-6SgFg2RKNakwr4IudiMMCP2c7b5XE_9EzZ2HV0gD69655uaZX-svIZRh2fe90STIjQ39OvpjoDP5HVsjWUD94_3CyaneU-aXpSBZHw1uh4LV8EvcB8-z6Gkp3xBUsaFBVwwgaU_f_kNXBhwImluhHW2PA0ldOfPuplZRpLGhS9z6WaPJTQBHqwbTmaux5CxwlM2cB1GO2M6v71Xqg1mC-p_lcXH6zPljGQ_giumfqwkWfq8ijVpG2IoHFPJ-toZIqHx_uOsGrlDN-NtyKP1Ft3Bukg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام
‌
جهانی
؛شماتیک ترکیب دو تیم ملی پرتغال
🆚
کرواسی؛ ساعت 02:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24837" target="_blank">📅 01:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24836">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJVz-uRXOIpJQpyPxL-v8zgiX3rhUnO8_2FNBgr11YMWQzxpxD7Kq0pMMWbJRbbwflFkgVTXtouOmfQNXhb1AS_rr8eXqXsmLbzYUJWNLokmDIT7lip_MtJPOdfcFqjfqMHd0J3DDDXeo2wYdI-T-4JjTcOzyyuyBCwoKcVpTpWfSwm4zh-l8nid4h2roTa0xzQxH6DqzszDylDgdm4UvY1-zZtGawpXATBQAUpJRSKWUz4Y61brynFr00jUhjEHfsb6rcJ71qjslsxifSUHYG9FQ1WYtzowIUjxpOIK5isBZi8PyPs4FAWzah8KYiXyJJJkSHFmLe_o1cfaUsba2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسول‌خطیبی درگفتگو باعادل: قلب محمدرضا زنوزی روتیغ‌بزنن روش‌نوشته رسول خطیبی
🙄
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24836" target="_blank">📅 01:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24835">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeHRhZ_TbzB9mfo3nATNy5WYIGpTVR_NagvLv9JoYYLPbpIoq95GKiHi5dm93KDlaDhTejBBW6lZUxhs2ANvZpnfAEwCwcyerHtWlFe9xKHAzU8Fp5OQbdfk-UCAK2vauCOCthWI1bt3dFQY6A3Wy4Gv3ShGtBvIow0MumTIVe34WIoWuSvfwkYHFnzAZ9wuZp0wM6wUFUXLsrVxusSALJoQ6rXgvZNF6aaJ7Ci0dPz8XSYbWk0Fxhwyz-YQ8ooearjphbr1euJFHlpP66o7ROgqr8hmVgjDPkKr8eukPy0d-KVvLAuNvMHhoYdEuw_uFLpiLAQ72DXSsl8HrIHLNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد فوق‌العاده حساس و تماشایی یاران رونالدو
🆚
مودریچ در تورنتو
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24835" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24834">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUPl_xPmE4s3_gsTHzlprBPaDb46Hzf-90HrhnyA9Nb1NlW4biYe7bcjsH6n8xhkXP_PvNrvoydU_7mPabEXhQLObpRngJUvsOi7SRLRojj-koDUtA8qMigCjkp6MgX4MjPDFMVWGLP1RQTSOw5yBFmyz9Yri1pkvrYL-pgcs9gQ1y03Rp8om_9r1uJ-vYdc_QOaUhPRE7-pU2aLJcJmdzJYT2wzVZxLBbQ2mUtYiVSfSKWuLpdWDLRILLmE5BpARYOHsfqchSfjZm-jiBbtSvZ8dngpkHo1Q1SqjrdGCypLsw6IKz2mgvFESECZ2l4iTXTaaK-ibB1vN52UDRUU5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدارهای‌دیروز؛
صعودمورد انتظار آمریکا و اسپانیا به مرحله یک‌هشتم‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/24834" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24833">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG0CmPIJQJp6frYKO1GYKHVB0IcJ08m_-2oLZt0lcl0BCZ5IkCCxx_KiCMZh29KADo4pGvubY85OVb1OHwcea0lh7YeCxmn557GWRT6j9ftR4XDcYIbh_5066AMqAOcolWxw7rpGuLibT0eYEEGUh7-At67jx9MhYHzo8TZPZyDnFjagg8xM2rUEhHdOND00kxWRr5LEnOrCyt5rFYyGsUjcuwRDAMFhMzKlwKEJObZsssl5C0P0nAXH952V5-4BX17I4kjSm3Zm9eTfQfzIwxT2BODZgHlsMi3hD3INqbBjHkN0QsO3LLG0oKaENaK8H7Y-HrCMIOj-Ic_yK_WjXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تجربه پیشبینی مطمئن با
🅰️
🅰️
🅰️
شارژ اضافی و ریسک خیلی پایین در
#پرشیانابت
رو از دست نده
❌
🛍
ازاین‌لحظه به‌ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
🤩
🤩
درصد برگشت وجه در  صورت باخت
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a11
@betinjabet</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24833" target="_blank">📅 01:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24831">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=IveLVxIkRFWqDIHcD9BdEkyYDSRARR0MMCoHVPZhoNhlYi2rv8bdBY8PG6z0MD743krKlna4GizF9AZ7YBWMtlldR1K77Yl8tLMXo3Wu0Wyj1KehMIRfnnQzRMrD9yJq7_V-0dEnBoji5FcztB4ZeQLa6fO3dAfpZccrlI7tQgMEPsff_03AehPznD56mQ9bjdCMaWHnkNa3j4ni57YwId9o3Nt27j0LqlMJvvb_PT82sYTgYmB-HkHRduqmpaWJ6DwLUTJJUdVUC_BacjF7wRainrZ_rIiR41PtkPBP-Mvre_ZNerlquqhZyMDWqj-LUl4IPUJfotGLy5-jW-WkXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=IveLVxIkRFWqDIHcD9BdEkyYDSRARR0MMCoHVPZhoNhlYi2rv8bdBY8PG6z0MD743krKlna4GizF9AZ7YBWMtlldR1K77Yl8tLMXo3Wu0Wyj1KehMIRfnnQzRMrD9yJq7_V-0dEnBoji5FcztB4ZeQLa6fO3dAfpZccrlI7tQgMEPsff_03AehPznD56mQ9bjdCMaWHnkNa3j4ni57YwId9o3Nt27j0LqlMJvvb_PT82sYTgYmB-HkHRduqmpaWJ6DwLUTJJUdVUC_BacjF7wRainrZ_rIiR41PtkPBP-Mvre_ZNerlquqhZyMDWqj-LUl4IPUJfotGLy5-jW-WkXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌باشگاه‌تراکتور؛خدادادعزیزی همچنان به فعالیت خود به‌عنوان مدیرتیم ادامه می‌دهد. عزیزی بعداز عدم‌آسیایی شدن پرسپولیس از حضور در این تیم خودداری کرد و قید توافق با سرخ ها رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24831" target="_blank">📅 00:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24830">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrAnHaoutHVmpwJGDM0rq71j9A-m3tPPU9HzGk4D55FVGbpV5J8S_nHZ3i8Apq2QDb4lZkC5lsjF9MLSRGA_MBI7uT0BlPMORO_ApJXP01gYOLv73X8KX3_2ElQe-6Tksw9v0Q3HpXgdJbHwIDbyvNmpA6o3u2ZZ4whgM9NIBh3_BRlIOIzq6ApkMOGWXI0NpROFLBl_osqntVCbKgghUu3kYL3t2NtCKUVuZShhIPOBKJvPmsN2Q4Mbh4sadbDt4VgzLgUSH63XXjGGDNXcOXWGBG1_1r22qjsmgFLnvIGHJZ3_8HhwtyE7CwISFussRJVv7XnEFEdKiLLQIkJjOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی رقابت‌های جام جهانی بعد از پیروزی سه گله اسپانیا مقابل اتریش. بین پرتغال و کرواسی یکیشون حریف بعدی لاروخاعه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/24830" target="_blank">📅 00:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24829">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U04UyirZYpSNoUlzbEf6WZ4b6UEcGNPwhMPXyldOOHp1iAz2AqUJzt4A8_ZRGPk3sWxOrJddwHhsVcUaHPjH1xGYgdHXN9thU_JKbKfCT-QsWL1gTA-FAeUM6zs_BKTWU3WLBm_8XTzCvvSO7odWURqRchljUls4_f44LYSiwZm3WhhwD0Tp-ATXB0PB_Uc1-M6lVHy_m2fUbdLwond-bruKLscuBOly3F4r9ZDeJ1vk5IQALuZ6OBVI81kV7_IVJ6qEJ92trob_Tnbdwo5dGNljBng-R0jvV07hfxaJhrL-G3PkOJJxPQ4kHNlUPmQxgtS4wYmsG1IjCqg8pvpGSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درمراسم استقبال از کاروان تیم قلعه نویی؛ تو جمعیت و شلوغی گویا علی نعمتی یه لحظه غفلت کرده گوشی آیفون 17 پرومکسش رو دزدیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24829" target="_blank">📅 00:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24828">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7X1YSIvNKkMq0pVRarmbwPBMsfLrq8t_eDCa6OfK3cnassKdE5e9rlRAxz2o2cLGdLHVftstXN97lYJdQ_d4fH-Gm51EJr7siwpzxoYSNeLaTjlEaYz_X743WBF-a2oMIlj5VYOBko3NhcQJcdOYp6sta1yMPiDJRklq03QG8ayCC06QTk8zNRgsOuKeW7s5teJZRTpR4_-gNX3547hcLcEGcKPrZS0w6e8E8XApjsb2eYQ7Pb18tab1jRRFR7pgtOrROHf1AGubutUaY6YrCRUE0c6HNm9Q2tIZC8WRUSVr4XVLPytcklJyZ7RJf9UTvRGV669H-iTnzcQ-b4I0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24828" target="_blank">📅 00:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24827">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=iIYJCijMXqZ2llf6vtlAI-bpYf7shZ5LP813XguGTPLRqEV2KhceEbN099D9YSzMGLy8e8JDHWmNQIXpeJwPGHM66DMgX97YDIcVMrOMpW5OjRkdxz2ZokDYkogzjM5xmEHpfIucFXz07TvdDp5wNrlzDe2GHMFFXGSwP2ulzjoOt8WdBMiba3_zWk-Ep-56n0PBPE35hPXKVaApC3ZLLQgiUphk-jm8SrwyN_h8fVRI1oAWfvI7BQ0S9TDokcm2ZF05yoRTMEXspN0S9EBSFLTnD058m4ZSHZhcsqRDP9xpWcGHb7n1SmJYxTYOweFhfYi1DTiuJnv0G38_mE4YUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=iIYJCijMXqZ2llf6vtlAI-bpYf7shZ5LP813XguGTPLRqEV2KhceEbN099D9YSzMGLy8e8JDHWmNQIXpeJwPGHM66DMgX97YDIcVMrOMpW5OjRkdxz2ZokDYkogzjM5xmEHpfIucFXz07TvdDp5wNrlzDe2GHMFFXGSwP2ulzjoOt8WdBMiba3_zWk-Ep-56n0PBPE35hPXKVaApC3ZLLQgiUphk-jm8SrwyN_h8fVRI1oAWfvI7BQ0S9TDokcm2ZF05yoRTMEXspN0S9EBSFLTnD058m4ZSHZhcsqRDP9xpWcGHb7n1SmJYxTYOweFhfYi1DTiuJnv0G38_mE4YUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
رونمایی‌از قانونی‌جدید درمستطیل سبز بنام "قانون شجاع" که توسط ابوطالب تصویب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24827" target="_blank">📅 23:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24826">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLLNuIuDQuHeA9_cNVA2TU2NzWe7jGhOH997aZta73702QU3nfycN7rlQW-OQIa-N73hI8VEibjrvZqTF-qzfCggJ3N4llda_oCU9fE0li7uoQnNpGXLTTHTyFEZU3QnBNe6oT-4-rCl6zVJ1E1dV48EtK7USY590T0upZabxWSPoqwEKT6jskrepc8TGjlrZIUw4ph3crVm_8rASDak8fHx9fx5UsMTWQ4etbSreph-R8xQ4kQVzDw5bXAFvrmIY7uelY42WHytL4uFIfbvyMF4Ei87_02PI4qfGeRz-1hYluXtyEx3FI1Ak9h6GRO5lYH4CGteDJA1lcShFVM2lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
رسانه Smashi Sports مصری خیلی جدی اومده گفته ژاوی روایران‌میخوادجایگزین ژنرال کنه‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24826" target="_blank">📅 23:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24825">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=bizl5PlOMNGG2lynmSeobky986No7w85ZilC7IAypxAbU-5nGNQ3BXOjkdL5DyZELStDMxvqGUvL8BqL8n2GXqSrQOlpUjbAoqwS-UUUQ8RmqoqLrtn2FmTPJ8F-YW53Hf-f9RQAQvSLX1PR0pIrGq9_Nb9K9Fc935Zu8t_FtZl5oOY2RHEXSWlwe7ozdLdby0Fx8-mLvyzJ2XhryfhUk_aLzohqPGSHzI5jh0FTg-XE9GTGWVaQ8Ikm22XVyasxbXM_GjaWOpooDcjx2sTzsOSdXbTvcDjQX8BsjwC6XTcXYqpaUESYfDWuT0zUS5WBKRTOBlJs3r1V2ZIb0wTjvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=bizl5PlOMNGG2lynmSeobky986No7w85ZilC7IAypxAbU-5nGNQ3BXOjkdL5DyZELStDMxvqGUvL8BqL8n2GXqSrQOlpUjbAoqwS-UUUQ8RmqoqLrtn2FmTPJ8F-YW53Hf-f9RQAQvSLX1PR0pIrGq9_Nb9K9Fc935Zu8t_FtZl5oOY2RHEXSWlwe7ozdLdby0Fx8-mLvyzJ2XhryfhUk_aLzohqPGSHzI5jh0FTg-XE9GTGWVaQ8Ikm22XVyasxbXM_GjaWOpooDcjx2sTzsOSdXbTvcDjQX8BsjwC6XTcXYqpaUESYfDWuT0zUS5WBKRTOBlJs3r1V2ZIb0wTjvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره کریستیانو رونالدو در یورو 2016: از برد مقابل کرواسی خوشحالم، اما چون برادرم لوکا مودریچ گریه می‌کرد، نتوانستم جشن بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24825" target="_blank">📅 23:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24824">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic9v7ryG-wSYgI_BHdv7LznsCkMYOBQPnexzB7qk2KVcBZ6r5I554UGQyvYCb11NzafAMWlshMG-Popjg82qcI_pdk0ZrpvONVuhha94cZ8_sfcJ6-OSFa2rtz8mPCo8kXC2Ou_HYNHwOOP8Jn7jFXjV8HIPqdGSzKxEn_EaAxfCAaRoBLPwTKjGizUYh6ttkoizQeL12SL-u77UMlYKF4tR2dBz2rsBpfi1AD9aZ2qJKML-FnmaGsBph9ZpTKDDX8N3o6UYHqI1-0MAiWW8LE4SJ9HkVSg_ArdVTg2ytIJ85bLxZRS6oz9Lm4CWn_-Fs0ctYlyfQ3UmzBchziYPXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24824" target="_blank">📅 22:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24823">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvnP3TbPIKGfn55KonGhMOkYespjZj_0uirOO_oLMleKBB8jNJ3tp-Viah299LaOebIXs6Mwqnfv5s1ml9uVnlXT7u4bS2ntgAeyGKp4SilkQq8_w3lC77SJb0YZXvhWFuVgkFTu3uQPA6RRBl6wv7G0HqhSYtner5DVsE-5ecTrRD3sFBBK1R0pC0_VTj_qf25mkJ5o37t3CwRn2_bTONBWDo4TEcTc-iB4nra8xAeS4c-FUE-4IH0Ki-SoPmONb8w_3FyH1XTdlu23z8y3SU4BiGxI8d1NNBAy63gneBNyhDvVs6aUmiW58bYaviF8iB-biPhAWWFEzj5KKGfMpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24823" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24822">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdB-I0YVe5p7hQMHTM0GARecNw96Du1NRy9XVtMdYhwJeKBZX_-LAPNvcXaZSfVQxKf6i3xEaZNncowFAq-C2FCMjoHsMPDy_Tbtmb_ehwj1gML6bqjRgUyzcB5V54VrO0XiURD1faSaLqHpy8pEl4pUiiGhih7IF-hGk3lt9rRAWMzhl-ZcgXFt33krifMPdjS_uGuVZt1LrH9l2FyorNf0mgQfLM5YRW6Ki6sJVgBbGtkhQMhFW76zO2lyxQJ8h4KTB9YB1Rq4OK1nbdmoC7OYauuvTkr_DN_vyrJxBFQUMIIrMaMBSK8TZlwsMQx14G-yGngtewyQaNRLEX2oeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24822" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24821">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtDRFVBi9ijMOGpe82BCFVaihCi_UogxchFj78rB_b7oyyOlky65f7HKxt1jtQ-LWZ2V5EhrOtW3iOm5931juyUKvqksN_6GV_0IylZ5_BT09_93aL3hRPbv3DYTFbWd3YfEfq2UxpRY-Vuv025VxdShVUvV3gTNFIaxMuMMyULBb-wVkDxBU2P7rGzpBw4nx5nHDEsT_S-8TWKcm48LQBNDPsKkOvFV9I8LrcVJDqepnVBbuLMhuNdkv1myK2Xqtog7obXXWhWVCQh2RAo2CkVhqA4-G5mFkKIqdyK_RcWyvcZ8Qf7COCU7GRoy_nqdnTTuRWpkvdV3GtvxoF_tgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24821" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24820">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPzCPmochC8v_1bwATTt7uEcKU_WjHaUyV-HbDBlDupJxQgpvqtyB0ewqX8u59y6Az51Lp8_oxq0BtckTNcF3CGT7ZVDg574R0QuGTtvpL6rjYGizCnqRkf7Nc4MtEJ7pHA6G1AtBpBOhS-dRVsESk-_QI9YseSU1NhygwLe8VR0a7zfVGeDirtfyzSTe7FHva4mBSrDZv-rgpRt4DvkZ4TpcRRQv9mlOGBFRHpVRFi_F_HRFzt9YBrDBE32dJyuvvu1-mKj5v5iy-k31sOPek4myhxeLYCY2-azP1pvO0pNPKEh7ObzF6ZCyF0byidmDjLduMY78qjlDq0gZmEorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا 72 ساعت به‌باشگاه تراکتور فرصت داده تابه آفر مالی‌اوپاسخ بدهد. اگه‌پاسخ مثبت باشه ویرا بزودی بار دیگر به لیگ‌ایران بازخواهدگشت. همانطور که دیشب گفتیم قرارداد او با پرسپولیس فسخ شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24820" target="_blank">📅 22:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24819">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gar4xpOZGhJYAuX-f1Gl3-a6AmFFJ73xTSrtu5ZFCE6st3mXDEEmvTkNe-urFvmgUKcmK0NH9SRCqTm1T_5U5oDg8_gCJIdtdmfuDwUqO44e7vd1OprBDZUVFmLPYoTcWjXg7gPqkIlollKo5dCus_q9yoUhZKA-V6-eEHQMbwBoR51j3xWGV9xYaBtefK5YlHAN0o0jDSvWuUPG4a1oI9LYN1VxLaTNXqG_e3R97LbTlDe9pqBh6PGaMKAJks-azs8NxIghTiZ4cAbBdgtdUNEAnz8PdaAXmlKH86V6l03XVlfFl4PuVB8zL8dwdoIHnsAKH5jATEOjaq9igsl1oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حجت کریمی مدیرعامل سابق استقلال امروز به عنوان مدیرعامل جدید باشگاه تراکتور منصوب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24819" target="_blank">📅 22:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24817">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPfjp7-6A_XgRzfgM0M7XTqlJXkjIJEpOcjiXKuWkL1AbyS7veYp8CAd4jNxBkaLA2_E1CnjCBBpt0M1-DLaZsomikBki9te1rdKmpLbREy2sP2Q_98tBAryC_qehQWi0Vqr8ILJuhxu4bfVyNjhpxfOS8KfAyskrGXSMd5IlLacfjKbzgb172qv-jOeHnSr-cAf46puyB2G1urRbTJmoIgsPSNWQGTAjyGaKr-V9c3QI14CL6LRJkeGHhXDEE0coGMsSD2VHiVU3N7AwSUfU8w2XhKEq0n3dj07cXidxs2dqdJQ7OYkWHmCHXkTaCl30fmymvSBweDItIkRqdhn2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امشب یکی از این دو نفر آخرین بازیش تو ادوار جام جهانی و احتمالا آخرین مسابقه ملیش رو انجام میده. شب سخت‌برای‌هواداران باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24817" target="_blank">📅 21:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24816">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTy6wNAEaR9H9G1SdmqZtD_sIQAlC3uhWTwj-skRYyNrACktz2ckTwdrF1bG_S0w6iqxqSCIAvWtjg7Cema4czG2cNOI3DMHk-NjrLJU0y1oRrAxtF343oEPrF--QEls8shBp32yrgt9-1zWgZcGHMgt0imMZK3e-epIrDUfdu63DGyGYqmD4EOSlL0cWdwVLejYuRyo-gOxD4-Gv42Dg6-GApYrOdx0DHg4Ia28DdftCLSQiINPgpbNvVzSndauyiBTaepkimIRf2mGVxROeo9runVJWHPb0YRdPySB0Y13mqGoGr3N4Wb9_YhYDGmQXapyWwCLggPdPIZIhe8sAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یوفاقانون‌کارت‌قرمز برای بازیکنانی که دهانشون رو میپوشونن رو وارد UCL و لیگ اروپا نمیکنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24816" target="_blank">📅 21:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24815">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkQ9Dl2SQsI39-KChvfrx5CPMexZpTEKVq0XmJ3mGZ05I9IsTfUGkZpTwocYdvUEdVpyOqiFr5ZttV29qsqbBeH-FQFoBkg1m1rERSxqtsCMzfiU0wPnrEt1tTM8vSec5zbEF9X1X037PsiV2pl7OzutpR2nfP6-BNyOPmUhWVm9WLcgoEcOd37wzdf-qLosHlyeR1vG-lPD5MlpeWw0AxYtS1Cu9uiAAu-XTjFMRBqImgnr7nq--1IJyJRJQg0QifchFxwYRgQFOdQ07zHPnUk4ssJsg4K8BHIN1E594wkrQ3rrCaC4pSKDXUnBzPKzn3IPANf4JU715hUTa2Z1IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24815" target="_blank">📅 20:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24814">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8NiN9iYUa1derQ9tHgxPVCQVEozTv8Jcd3pZ_Dr4Yr1EI41p2WKsLkUSfYD8kpz_xWnkSg_jV6d6E94BnWrS4_82OjFilDeyHLAxrOGBEbef8WDcrWFmVDRiM36pvozBkLf7VpalphfT8VhBoYX1FAb8M29l4_HWAYhhhcz5sh33BnGWUAZT9nmFoOFvWf5p8l4KGgyWEvBYkfvd-gQ4-wSJ2B1c58pIx-g5ySuJezZRrjt65Ix-b2d_goysxFaRDsHJ1fb9lglbQ8r29m-dmwfLfBMKPzZecQ95_o3o5XYAiMGENxuoULZr829pBcmD4kwtTBOOFWnudyXTmTebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی
؛ شماتیک ترکیب اسپانیا برای دیدار امشب با اتریش؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24814" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24813">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnTPB_wMzPuJ_MQdvdGa7EpHH7CN5tOwWTDZ1gmCt5p6oz3zmuikoMKHOG-ev3fv4tUK8LXjHgyihxMXO0BlT2th5o80KTX86tWAXkC-wK3Ya3PipFxfabZFtL8sAaB2AdxIMYTIlOGlgCcw-xIeDJ7JtlsWwhjs4dBTW_N_W0sEs8WgaOE7m05KX0VNKrt_uaxVt_pa9pHJe_hsjYflSt-Xb0w58lzGz63mJRGkiox4kR0KlB7UM6w0QG_38rPYlGpqCkLhWui-Hr4veJGcPvkUKiayKhELyVn4I7puzjWHsJytoyFxFcu18KVOJyfhrml6ZKFRwhhKHDEn24Rgcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24813" target="_blank">📅 20:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24812">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTEiAlGioQIygdXPVYaXgTeo4uyy6JZuE6bkrrS8rZ_t8XT_30sBKYIrZVfmmVYECJxASz9DWdD8pcBLU-6VADV1NaJAa7O3EeGatN4CpRTmqpyIqKFPt5CxX7xbYN3sZapRgzkp_gHKpcP2I6ZxEXTNUtDF9WStmgH5ewg5IdaU9tmYOyMl-D0jJKS_2dgzbCD057YhUYBw57Umj3XBBfrCprElHCuLJVs_PZVmaf8LoyElxF3INARipBjkzbjqhkaiT0MHiIxOSQbBuVzJ8XM0MblyIeQqCk_Cm6wq52Tpx7nfMUewd1MNdtn1-EmCkWWCTSIRxenjlgu92KX9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایح مسابقات‌جام‌جهانی 2026 تا اینجای کار تا قبل از شروع رقابت‌های امشب مرحله یک شانزدهم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24812" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24811">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjQFcOffPsxRsyKQ-UHhkczAFCjpMM_UyPI5cf5wl7fM-_QLUA_JNeq5TkI1y5qK26RW01Zxi67uta2T95gP3-4n16K0Qw4jyu3RxV1tI39_ePWlghqgUjgbgYafCiaor10wM3FO0u0UwefIqT8a5ROA239xlwtMmmFZ53ULPeQRroevzp6tHnYN3pGGh533ye_XmY8plZeuX8-CjQclHLcB9Cld2fpbsMxFL2EUmk4VuXw3bN1PNs_1zncRIz-B96P0A2bU0CaNFrsK-Nj2awEq2HTofPnhp5zUkdXYpzXnAsY_bN73f8dgIkuQVPBZU_mHDBxg41xBxAZM90uPaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش: تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24811" target="_blank">📅 19:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24810">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q999psRSudkRJR1kdMvRcHNd23DfV3RCXX0eABKxOB4hVVeDfzkyThb8lGlVt-1P1_lVPuqyYCGgEj87Zb6JlRk3qWx-1kVcENR5KcffegOH9MW-jjKlyq9IBTrIlHdCD6_T80XmqLOFEfG6l4rsWqeFuWW5LJWhYKPQVuxS1uy606NG84udkCV2e4I5CI70SHOakF4pmHGLkEa9mweLyVUEw-7Om-yFiVvTtZt29P3nXbmNv1tqEsbZI7z5R2d8wsWimetRUYgeJaiSAVfW2JG_HOsQWuFYUpFiq0HJCtSisRX6N2guA4Fijcfb0ojfUMEFZQzN3GULUZ7l51nllA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24810" target="_blank">📅 19:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24809">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cONLrJiBnuaIUThq8HvYnW4ZPuCnf3TPQLYxDy9xXD9GeCqa3Qx5SbBWyZZuF9NTUQZomrWvJvRY4pj-3a7-hAyrEIH9WHH2rtImhhcWHyuXUUPWB9GhbOSVrs_5AKOLG1QYAaeNAfGUFcpm4JLyY5--UZO2kwRzWG2jdJ_Ct3I1nfwH2XDwOywkosYKtBOpvU181BKfQ6Gpy6ojGG9o6iS2Juf1-CBgwDRmFTsP3ck4qJUQAl9XLfiBNgj1zmu78vNRRrxlZkpAkbhm2C1iSUUdp9aHYG9B9oMaRNHJFNwIxPXBYRicG1U2H-8sLU-1D4jN8_OxrkOCbLT9AijMkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24809" target="_blank">📅 17:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24807">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GynqylbjLCswealFRq6ejbS1tKbsHpmt272OBtobUIlQ6qnAcIEabKO-bFaMQMt558QEgTIAcxl9UpzMCmgko-PpwDexJsGS1m4GMsNrxrtZvVtyFzQeK2m3d3a2yWEAxMRsEkn-b7vFw3oCNBFBjf06LEzOVvA0ZNVZtGMc44zevik2MZvxRXHn4my33Oy_RMPRysnxkqEBj1N4u7c61lX4RWBZaJjiHasypHvNoGOTOaxMOD409bQCgQcUyDrtqppy5Gvxve-tGL9I2KUWVZxVLHif6clbq6Ky8jdTK-0AHB13gr1SFuOoPz_PbPjWi8X8e7_Iyuu05OW7ek3ing.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QxnEhP3RiJBFfaNOuOYUVZMboWJHMiMrzm2efoSZ_Ho_4581Co8YNmRzC1YgFcX4b-hHH3pKuBWp9-iHlr93t4WahHRfKzqI7eJ8pZC3EUIfY5IZpIIRz5HUg49wDAXCqXPUpUOix45Q-iMJnrFaQKiNhtolI4-v_U3agu33MoUrcU_Yy0bqZr-erpBBedBcS7xVqWYdLPFPl-dZTX8nrf6rQv1rJw1THXCjUQQVlSTrvsNn2UqgmqTR-db8YHJ7SlXQ41U1fhwnchv5jp3gWjn6fecDJlaNP-mXQ4uihkIRYtxp8MlhoEvqKQ3ouHhPElF9bvm8R0d0d0xHzZ55NQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24807" target="_blank">📅 16:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24806">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c080f226.mp4?token=LNnmUgGif0nEq7RRPee5DOCf35A4zEF57rpeLs9H9cRJYPBOIQoJyUWmnIEgsNP3ci9uRl3HMZSGfj37AlA1KiMzpJ4Od1nAq-ezjRBTsTNW_HPF61csPKD3wjkJGBrukBTck3KAv03TvW3yGED3OGyjPRY90RU-1_AnXuzxJrDXJllXa-FOKUBqpjaVdck0SjD_2MllxoGjSIEhBV1NkjNhlkgw92HPVLq0TEYYl28b8RnBgDjGYb7_02y-keppvIq4HVaQjqN77DhlNAJu_fWKhDnstk7SWKo0-vUlO9t6iTyFJbwcLW0hbrzxSa9YkIn8cnU2jz_epo7a5C3Qmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c080f226.mp4?token=LNnmUgGif0nEq7RRPee5DOCf35A4zEF57rpeLs9H9cRJYPBOIQoJyUWmnIEgsNP3ci9uRl3HMZSGfj37AlA1KiMzpJ4Od1nAq-ezjRBTsTNW_HPF61csPKD3wjkJGBrukBTck3KAv03TvW3yGED3OGyjPRY90RU-1_AnXuzxJrDXJllXa-FOKUBqpjaVdck0SjD_2MllxoGjSIEhBV1NkjNhlkgw92HPVLq0TEYYl28b8RnBgDjGYb7_02y-keppvIq4HVaQjqN77DhlNAJu_fWKhDnstk7SWKo0-vUlO9t6iTyFJbwcLW0hbrzxSa9YkIn8cnU2jz_epo7a5C3Qmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24806" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24805">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYkj6ApdFuioBalNCfLX2bxSwIOh7V2EwxhuZiKklVgTKt4yNGCl59tOXnH2eE0eVfAxCEBbcnkd9EeUABYzNaRCqc1jLUlAgO_M4p921oWt60-l1-Rj2FdtWZsgm66CH3mUOOgeElWHQ-hIuec-qSalxya7rfRhVumJRmCXDdPFXRRxwx4JlRlWu4KeY9XclRUhtq-_iiWM0j8zpCAsZbFEdLUeE4wpKxFr724Md9TgRZTUlMyDChwsBFV-oKibbPogZZLgmmlMyD3iRIVS99SUXIntrenlBlm1kEjcOJpRCCvaWNqdtoJpB48m1SFrYTSCpC9Fr4XCU8-0KS1EMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل در یک فصل در تاریخ فوتبال:
🇦🇷
لیونل مسی فصل 2011/12: 82 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین فصل 2025/26: 72 گل
🇵🇹
کریستیانو رونالدو فصل 2011/12: 69 گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24805" target="_blank">📅 14:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=sEu8CVsYnyHsBYV_BqhCluw_7B3Kp6BrfwTcNOvxx_Wnmtu8Pb-sIXc5QYpZMWpVHZuWfvgecVK6_r3MWdPvd9BL8jJfOCIzbsdgLhqouU_7uBydKBOLpFu8fYJj1FHjj6ELb8SmC9TDaBgI0R-AsFZXLPiNq2H0AC5D5O-g32y45axD0Wa4beYRR7tUUlDKTnr2ikztZTw4IHuBq3-iyoaDhu4STdyXE2ucNQhnhDV-aDTnEOVO7wI7Sq-_VhLl3d0HYjatnRvf73xsUeIXYQbjfNT-o3YVc5biQSFlaYMas2xqgLpUiow8-RzFXrIQl1SMe1osBcQEh3tquCdfzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=sEu8CVsYnyHsBYV_BqhCluw_7B3Kp6BrfwTcNOvxx_Wnmtu8Pb-sIXc5QYpZMWpVHZuWfvgecVK6_r3MWdPvd9BL8jJfOCIzbsdgLhqouU_7uBydKBOLpFu8fYJj1FHjj6ELb8SmC9TDaBgI0R-AsFZXLPiNq2H0AC5D5O-g32y45axD0Wa4beYRR7tUUlDKTnr2ikztZTw4IHuBq3-iyoaDhu4STdyXE2ucNQhnhDV-aDTnEOVO7wI7Sq-_VhLl3d0HYjatnRvf73xsUeIXYQbjfNT-o3YVc5biQSFlaYMas2xqgLpUiow8-RzFXrIQl1SMe1osBcQEh3tquCdfzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24804" target="_blank">📅 11:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilnZEVd0-XdjuI31olFJ7_WdhYxMxfsJbLKi1r2eGxqollD5vLYDsyHUFj5-AfrhnXIMw9RXziAKEpA3EihOFb1wfKyaL__OGwZ8QZsIUQAHZvwjp4LdAWos2NKjOWyoYV-0oPFkzBc9qJTaeZQM-e0gr2JS2H9epuKmhnQmidK1EHklSqfA_Xr8OcGO9ppzBfibIv0We-XbnZK0gB5wjZDQrgX9JSAb1Pmi9-I4tx1W18Qs6ojlhOxqQfSeZFPOWqYyPDESDreYa0FCtYThOOyBbwLAIjvmFHyDpxK5fBi1XH0D61b8bwRffyAeAeQUwXFTa35Pk4xq5dzIdBHdBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
ظرف‌چهار پنج روزگذشته بارها اعلام کار انتقال دراگان‌اسکوچیچ به‌باشگاه پرسپولیس نهایی و تمام شده و فقط‌پوستر رونمایی و اعلام‌خبررسمی آن توسط باشگاه باقی مونده اما یه عده تکذیب میکنند اماامروز خبرمیزنن‌که اسکوچیچ سرمربی پرسپولیس شد. زمستون هم بعنوان اولین…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24803" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24802">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=X-APK2C--05MYV5QIvE087loGmk16eFsIGGZZIg4Jb5v58fNEvrLWc9i9kY3V7yLBcktY0zXcMeR7mfUsP9-KxuDNZhDvX00GHtHKZNseSf9ludgJApracB6MzDT18Tm8GgHYhNKXvtlzigYKDFXyk7tJ2FoPEya_4k69MPea_uOaharPpgOmOlNN1DOjDJm-YJDlBwB09-AKfOYt0VVSpMIbFQrZV1IXW9a_q7r5TT1u5zfyMOH7vq1MQQ9G80ht9qrT1KwfECx9Qo6WVPLG3s9C8nF7g7WzFKLMqe7DZBvvK0CPcLB7j-etbKkpynkTulZbzbTRaDKr1AgVS0llQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=X-APK2C--05MYV5QIvE087loGmk16eFsIGGZZIg4Jb5v58fNEvrLWc9i9kY3V7yLBcktY0zXcMeR7mfUsP9-KxuDNZhDvX00GHtHKZNseSf9ludgJApracB6MzDT18Tm8GgHYhNKXvtlzigYKDFXyk7tJ2FoPEya_4k69MPea_uOaharPpgOmOlNN1DOjDJm-YJDlBwB09-AKfOYt0VVSpMIbFQrZV1IXW9a_q7r5TT1u5zfyMOH7vq1MQQ9G80ht9qrT1KwfECx9Qo6WVPLG3s9C8nF7g7WzFKLMqe7DZBvvK0CPcLB7j-etbKkpynkTulZbzbTRaDKr1AgVS0llQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
آقای تونی‌کروس عزیز؛ مگه تو چند نفر بودی که بعداز رفتنت نه آلمان روز خوش دید نه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24802" target="_blank">📅 08:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8E5_5YgEuhJzxV5iWlMSJCePczSq0jenREZFopqKrxxo9xZWlr5sZFf7JpyjPBnfpMycTT0idNgLFs2oUd8h800aiH8-rF0JuCEDHC45EQt8IPY09TGLpD5twu7jFKBsZy55ywmbsjBZK_z46byiceceNHgMB4hb6cbc3ZuPguJHCCt5aa9wto_IrGj4eYgAUttd6yjxlJLuYGVXObVlBfxWpPkGzo-ZhPd25uotOvLWI767lTNO8Uf7H7na-uMIwWoiuHmM2lJyD2_q70xwijX-2AN8geFwX1pv1nOvK202k88PnebWIa7-9ZhxhOWhwmkIUSOHyebrTRa9zqMhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان چهارمین روز مرحله یک‌شانزدهم نهایی؛ آمریکا هم با شکست دوگله بوسنی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24801" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbyBmiIH0wnPxFRgh_xq8ar6rLV3dSZVq2oJeR1J32Ml5IIWcs_rIuCvqGwPSTUnEII--IN_vn22EEtZEW0vmsWseZyoMjoAa6-30xo5SLrBZU-lFvK6_aMl4ppzxuvKh8XD5hyGOhym-lawVkN2EqmiHBM0ts1DcVWVHiVFBeF1aPs1HohZDgg467ARgIS7yjFQY_r6kmM8SGgB1wsZ14yyUkkAHbU6WfnJ34Nxozw_NRlCl_XhvR6BToYiXPFXZeKZelfZ8zMwvd8WHw8CzplM703HSCBZ5rXbmdBS5ddWFzoZ6t3d70U3uR2Fv5wNZYqxsq1ekmoW_Xjxsz2FHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله ⅛ نهایی جام جهانی که در حال تکمیله؛ بازی‌ها داره مرحله‌به‌مرحله جذاب‌تر میشه.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24800" target="_blank">📅 08:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djzukc-u5eBQ_kkMEwmOpqYEJ-nuw5g1BpwreKmi7y9pz3oEVDTU-znyAD4sksneWk9BfA00oFiYX2Id6WraFLLd7nw6Ad25AuCQP3TgYsVDd9fwNrD7y7tsNBkpR_kc9HVoU3kO-dKzDWdTxfpNAkHl_i7UYzqOj-NNQ4H7Nn2O8iE50BigqeRzQR-e5PY45gycnFBW4CJOTMBjtMExFNSyyT0eNFXHwUDxOazwalNR0BIzvgLB0XVasQ7akl3dTyN1Zxf1NiFXdBZpUi7WpO6lITp0dPkDip5ZfZO2MO6ygry6Z4we7NYnpRorb3bsvUaMfuFX8Xml7ySZP6W9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/24799" target="_blank">📅 02:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=jQYOjfl68Ruameqf5-Okmt6z5pFhLhFclWTFLHd7YzYYL8j9xm-GfY1C1YWIDncV0_umPI88tFf88GJ_QXSP0vDrWHN6_YwE_-CbW-AcKc9uXcuBiTwaHAM3WM1F97qTzGwVMvq4MK8MQrMAHOpF2RV4acLOYsheduAimy1Z6Y2SyxUYq8Aln_kr5lj1OVqKvHo6tk5HqrBIZJnppRSDv0DrflVx61pl9eOP9_rVFNrLdtJdO4L-bscvdrQhPmUmKk6kj7exmmLE4FUzYBstsd1-tD6q1IcXtlC4lAtAGrMdOFQm_ctPFwsHg8RH01yGxaTIbZeWMIGz97e8QNe2Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=jQYOjfl68Ruameqf5-Okmt6z5pFhLhFclWTFLHd7YzYYL8j9xm-GfY1C1YWIDncV0_umPI88tFf88GJ_QXSP0vDrWHN6_YwE_-CbW-AcKc9uXcuBiTwaHAM3WM1F97qTzGwVMvq4MK8MQrMAHOpF2RV4acLOYsheduAimy1Z6Y2SyxUYq8Aln_kr5lj1OVqKvHo6tk5HqrBIZJnppRSDv0DrflVx61pl9eOP9_rVFNrLdtJdO4L-bscvdrQhPmUmKk6kj7exmmLE4FUzYBstsd1-tD6q1IcXtlC4lAtAGrMdOFQm_ctPFwsHg8RH01yGxaTIbZeWMIGz97e8QNe2Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24797" target="_blank">📅 02:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpV92z4q5GvX9C2IWF3qZ4WAp7HCfojdF4PD1Hm8t3lLnrId35a-pkkTRxF7BIQbdclOBgXs-H2bFZQ3lO4zXm7BilqV-l7vXUNsZQilJU0-_REkPZbQKs1VN6GEUAsqXRQNGk-3b5xju4m-5CF0IOu7L0xHyGozZ-EIq7-2S6JZ6phAkqo6XcAcqLQsdj3RTEJsmZtSwwDzwO7ylAC88yEKpSSiqetFzET4MutcSksSN56X8SRvo8BPNmEz8AlR4pke9yDcnd_0u8Hq7NUa8dduh9L6heS1Hqiu-_ZNp3ASA91HsJjYJfiDmT662KEA7PdPt8P6t-16BgHBTs1lNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم نهایی جام جهانی؛ صعود سخت و دراماتیک شیاطین‌سرخ‌اروپا مقابل یاران سادیو مانه در سنگال؛ بلژیک به معنای واقعی کلمه مرد تا برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24796" target="_blank">📅 02:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSWm1rLWdrfy8c5jUeFzGFr5M3EeuWypXJi0RgVMN4BqMmjnMPNFlctBs-Sa8EpZNKT4gdkYFW4LcMHtsxUmjDnEhXoJTQ4a4gHdvDOrjbDyiV8y6KWNogdN26bn8STCGkLXIH_G1W8ujaRDVI7WpGAF8yk7C3ZIwfh1URUOy6-WbdS36mTrmT6Y4T2Z8DwqXHZn_-IEPRXeDIh64ew6Sxkk6xO_r6aUqjrOcF7gycNgXrga5xpyZFrukCXUKc2zRKsSc_2RevEH3SK-RR_i3lhnxRBBo0nKrLtVRFgv4QA9AI9PCfksJR9nrU1FP1WDOBGHXyIyIPK3t6DtWVRlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24794" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyIF9AIndP6zHQ5fkqfqjg4pINva7xhBAWNWEpSvj663tkCt82rTnNEtqBBLErcNTyd7w_JslNDG6xuPd42s_ag2-KQrpIZJCjzukhWAdxp6CxhjDESCJswUfWDX1n_hPj8cu46SqFX1Yw1NArbqXomyvLeMy0rHTBqjPHKWvZZbrtgZWaS9DokvZQJ04_q-MKakg4QMsFlMSlww8b8bSYPxAiZUcfBddWYHUHxUOh6LOS_1fwDp6fv93XDx_V_GR15RSXIqlaCvsiMgo5mm8g5JNQ2gG46J6tfT-sbOXtCNWHVIngnRkfBft59yt28_jf_e1DeVd3kPozdtw4MNCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از درخشش‌ادامه‌دار امباپه درفرانسه تاصعود دشوار انگلیس و بلژیک به دور بعد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24793" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4ztWd8vCYb6MULIh89HTf5Sxu2CNEPJh5KwV6s-ncmEMEU3pxE62KuDUv0jrqw7fpd1DRipsqxltYRzN3nVFjxYMjAj_rnxbIJJ9SNweX3Cx3Nt28uZl6dJOdzSEgM1yEdsgpRuUqyZudmSATIOTSeTWtj2_235cdVBDCl2gO5-ZFg8fs8NmhHTfoN5NPpeEhsZGWE8OM-I3S2nZLEcf4mk9WxuE0q1cOL3XWXkLerSVqgHuZWU7osaKqHsfxBk_48BTvuISCpRrWACtV_IWr_jGPWcVrZ8BvrpZeerBsh0EZIPkiKHEvs1B75fNnHirdRLvgyau_BgImhD75dDmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عامل‌اصلی‌کامبک‌زدن‌بلژیک و مساوی کردن بازی برابرسنگال رو میتونید در تصویر مشاهده کنید. باید ببینیم در وقت‌های اضافه بازم به بلژبک کمک میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24791" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjfm2DO8EokWw0Qh7ryGF3wNhd6-3YTfmbokECQGYe52hJkqBpLZeihjqHhntn3zIjmaycYRkigqSSq8VCnQeBT8faAjB7-nUDP8rc8tg6kYCJJ3KiJLGPnw0tqpoPKECyF8NLCntK15zANhbUl-ykLfqItNRnDow11-aCxeVaOKIMoO-uS15_p02t-oIzplVB6Tbi-BEi0Z3q0W5x-d7K6tG7o1tP6x4zLSW8wU1pb_cH7QsCYvGQJkkYswDpklttjV0O2DOJcDx0kT2Gn-6TA08js3vU9ePuS1ESHLvXwXg53jgiE_q50bLgElY-SFijBg6l0gYwyKMNhbcN5XAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میزبانی بی‌نقص و خیره‌کننده مکزیک دررقابت های جام‌جهانی 2026؛ سال بعد همین موقع‌ها خبر میاد که جمعیت مکزیک دریک‌سال گذشته چند صد هزار نفر افزایش یافته است. اوضاع خیلی خیطه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24790" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvXCKydbyyUv_A8SnX2wfJA-J4s9t8KVqgzYouBAM-_fTvrzCoLL9cdZVFRJxYkLwOFhuKIkxwlKEgyZMZrvvoqN0gR1PzbwQxKLi8WS35ASBXunMX08u3p-59Bax20VQj9u4h57TCQUhPZZdabmJRgX1gKLco_7jCho5CYsbphdbPSLb5oL4ezANQKyke-t_lYlYQ0Cp1mdfMvMnpkvq-zl5ruqfRQI40w-R9FE_CVje794qsmABcGje2szHsh4PqOU-Ntb1GKpbuQqDeWHOwq1qDdoN7qSB0QbTxU8gDk4rPcrW0TH_adHbvzP7kbtF898SX3Xxc68vcWSWsnF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعداز این‌پستی که زدیم گویا بلافاصله به غیرت بازیکنان بلژیک برخورده و در فاصله تنها سه دقیقه کامبک زدند و حالا بازی دو بر دو در جریان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24789" target="_blank">📅 01:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRa097kii85fcUl_wZPD6zj5tAV-mRtRyyWMRNhdH-K7npkrWmSAtHIElrGSAjvx0KRrN2LxLx4yj6EFfvaWo8b07PsDguHqaRFd8ZvuiAeecUsRbiFUoX5dKyy9-qOD7snw51z082qN9puAqZlVCCHkQ54e2VTV_4U-sEfXr7T_wjCckKSBJ_qOCBALby9fDdATalRXcUOaGJ5z552smnU_M2OqsBdjxe3UTAQWsBIimFMk--PQx6zerv4rxkv-UpJNbbjEhvmFBUQzSOE-tdakSW_PE-o5XKCVDQ9KXSTTGbTxe6zyZq631WHdGj9TTEJv28PUYhLURAgf-uwbLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضع تیم‌ملی‌بلژیک رو می‌بینید؟ قلعه‌نویی داره از چی افتخار میسازه؟ از حذف‌شدن در «آسون‌ترین گروه‌ممکن». ‏سرگروهش‌هم‌درحد سید سه گروه‌های دیگه هم‌نبود.نیوزیلندیکی‌از ضعیف‌ترین تیم‌های کل جام. ‏جای مواخذه داره تقدیر می‌شه ازش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24788" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkUBeHQQfKLSAf_xLzFoM0npm2KnQAwbiJydUaadUMGXCWIklmG8LB8e3MpOGYbWkoUXr7wTNiHGbXjpzseRr0yhyZk8reVzWiEjUynVgPFTx41ibvVFSPyVddbfMOsUUegeOJZtsw1n35WsOzLhPToNh5Rzx-USBF4ptQKnfUpvnO5i2Bv0ls710gOCq4VJr6jXN31UEd9EloJqyjJWP_9UdFYdlx7474t3wq4qK2OVaZK6iGrLmiwnMv7FDqyG5wx1t3vGocnBIQpICqqsyO4kJhXic8a_qgD6Y1taC6mlkjZeNDsx9Mjx04itL_0glZrbLDydeQMxxA25XWaANg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24787" target="_blank">📅 01:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=EmlbztiqbRDAeU639CDgApIvQAtyyd8WVlekkIloQIiI7pD-9R1W7AitoSAb8yx_OZeWSVQgwaDLZhqywX6Jj6pnckc05Mf96xmUjV5UwEx-AXQJipz74ZVcXaXFsZpIVbq1ph3P29tnROO_LbfZyPiz10VBWyRJqgS4k7XHtmufnqfCLR9G9bbdnPWm0eMVV_XQL4kjC6OPuEeYZXnDKOjqjNFnT8t8vF9vUZPFDpT3aHeqTyVpeJ6lajM7nRFd1qHDHVcE0tmKuOGOz9kaR8y1JPjGk337ouekea_-abq5eENX-ntzClH2cfRlYSWOqOBxAKgBmI9hlM4_VfEZt3lVS5pjznCWwf9KT5Wjn1RfmmvjcpVCtDqx77sCQ8p8_U7mqPfPhq2uai22Y_FPqc4umzqeGH3axeC0Cp6pMX7cb6RrSkoDdn2XIKACP01FigUAgOZLi3l5phtlvOJ79scFGWNcDkyS3trE3hlLVvdi2MiG97MVcE8taHrK6rRDk-ZNTiO48WUS89UlaLX9MR7cUBDweSDn_dtrOnVYCih0ZaEHVXVOHI8B-rcsaBQPRNGU9Nx-0fYw4ZnG7f13H9m7wUP2e7ob1WOk6fnnRsw4UROihfDt7zPUr8K4PonaG_Q5hXYlTB0aSfBzq93f2DuEf69KTx7TBbHvhsT-sj4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=EmlbztiqbRDAeU639CDgApIvQAtyyd8WVlekkIloQIiI7pD-9R1W7AitoSAb8yx_OZeWSVQgwaDLZhqywX6Jj6pnckc05Mf96xmUjV5UwEx-AXQJipz74ZVcXaXFsZpIVbq1ph3P29tnROO_LbfZyPiz10VBWyRJqgS4k7XHtmufnqfCLR9G9bbdnPWm0eMVV_XQL4kjC6OPuEeYZXnDKOjqjNFnT8t8vF9vUZPFDpT3aHeqTyVpeJ6lajM7nRFd1qHDHVcE0tmKuOGOz9kaR8y1JPjGk337ouekea_-abq5eENX-ntzClH2cfRlYSWOqOBxAKgBmI9hlM4_VfEZt3lVS5pjznCWwf9KT5Wjn1RfmmvjcpVCtDqx77sCQ8p8_U7mqPfPhq2uai22Y_FPqc4umzqeGH3axeC0Cp6pMX7cb6RrSkoDdn2XIKACP01FigUAgOZLi3l5phtlvOJ79scFGWNcDkyS3trE3hlLVvdi2MiG97MVcE8taHrK6rRDk-ZNTiO48WUS89UlaLX9MR7cUBDweSDn_dtrOnVYCih0ZaEHVXVOHI8B-rcsaBQPRNGU9Nx-0fYw4ZnG7f13H9m7wUP2e7ob1WOk6fnnRsw4UROihfDt7zPUr8K4PonaG_Q5hXYlTB0aSfBzq93f2DuEf69KTx7TBbHvhsT-sj4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی:
همش فیک بود
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24786" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaauNtjpkMsd1GmAHFVbH_7IohSWdM4nMXO_Xa2NzA992uHotMqqHiDehV07Cal4QjT7GDCvEhifn1GScgSCqMBFlgwsYeOr_xIbxMIEyHv5FSyhqmIQ5hqGpo7Qlp4kAdFQIBkETdAo1Yairkg7fX2SaswDyFBArGKiEamhkqvdMXoOdyB0xUb1uwXhuZjGwzJhqxzPtlvxLpp8ZbFq-qtzLpCY8FWbmwsdgtzEaTcb-2SIwtpYNVZXYmsv722L4B97HmQmqEUy8gi4aqQimoYje0qTwbuUfou9j2KH1oGkD6G_ot05hN6N0wzDABB1hfoLZW8JL7q1hcSokAc8vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24785" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTKkuLCdOcRC2Sf6dWEpu5bnzwx1byWNoG5o2AfZ8Krr_CiTmSOLTh-x-gdO0OvFZ1BQUlgebFSgfF3m5fPvu8BIvIjs7EYiEzMUa3Q2JTw9B-d7-N-zLalb-2DmuAV6x-rx5tLXFw_S0WJDGCxwW1R0_HTCDHEPnBChr4VLfX1ZFhotvS8u72uNHt1vMAeKXN5u2HUkGsFwe8J-Vc2ov4jbLgB1FCDibzEv0mwKIHaGdciaGs3Vy-LnO6Pq4DdVi-N8smFnCsOmmGJATEcsVDxFAE7DLB2VnzynIKqac_QhoKMIr3-AhxUSPdj-f9TRYHrHNmUz3Fcu95IXEB-bJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24784" target="_blank">📅 00:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24783">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=Mv33CxrNL1iTbVmfWaM1dVTttX2hEOMN_ot5GiB6tSQELyABKsKM4SIPgpjBsR3nO2Fh-iTcCxdhH36jkHtyLjrcgS1n4RSH0tuw3GWRshs4Bp9f5syuDhSk60luW2YEcnPpGtYES3rc1rGru5Zpp1yFAqwDIm6ZH-ObC73VAolvE4-nYTMch2PLNf8IUV_WaMNqUtIkbkMEmnCGbV20P5K6_ZJp9E_ceE2QirSDAQt9cB94sSCR3qxP7v_HXzq9PWSUy7LXnzVdNlkvJFL46L25C5MTUhqVVgBWezXUV_qXzMfRt86sD-gtgjkAGK02X_gk7Z7yoA0cX1KEfnwcag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=Mv33CxrNL1iTbVmfWaM1dVTttX2hEOMN_ot5GiB6tSQELyABKsKM4SIPgpjBsR3nO2Fh-iTcCxdhH36jkHtyLjrcgS1n4RSH0tuw3GWRshs4Bp9f5syuDhSk60luW2YEcnPpGtYES3rc1rGru5Zpp1yFAqwDIm6ZH-ObC73VAolvE4-nYTMch2PLNf8IUV_WaMNqUtIkbkMEmnCGbV20P5K6_ZJp9E_ceE2QirSDAQt9cB94sSCR3qxP7v_HXzq9PWSUy7LXnzVdNlkvJFL46L25C5MTUhqVVgBWezXUV_qXzMfRt86sD-gtgjkAGK02X_gk7Z7yoA0cX1KEfnwcag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24783" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24782">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_2JU31E7rfCDwVJUXr3PJGoVY0GSYrUiDHCKPDLdW6F6Bp6_eyMZ9AadiIckxrfcwB1zqj3ZHJUyTRlGmMq7wJuKKohJlSRunSeazeNsSSJAjRXo2ghubEiJFBob2P5LRd-K-KteuvGDJZTjg8t1qkuaW3we0TIkd_lguw0c5lSaGMH3_4RP2-KVLic9HLoD3eZf9LPtgMNlp60fHaBQdUnWeS5QoBZ3pT0ukjoa0B2bHdNwoy_7M9I--qew8a96czVelzAPQs6Rfkybe7DmYqB435ZaC3EoLdilHckUt3yiISKUDubfRPLR2cbLEcZa3-KgZ13W1njdriDwSdHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24782" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24781">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUJvM1-LPP-qp6T4cLCpcuJEM3GArKRglYmqbrvQdjxhVxP9_pkKyakQChvBI8gprCSoKBEQVe_lu5zIKwQlwmTLspmRR8IXtmuH1aSoTogCAUFlvyU6FpRkrnXRFAx1oAnRFS75kHBFJcOiZsaWGfpuY16sxFJyxWDW0qdepb4RXqv9a-G_MOyB-XBDldG6jNQbCUMendXrWQOxp1KCiGwAuFz_cxE20nq_hra5dKHaHnlMfB7SYAhkldMJYqBASghCj7QjIrh2gPo0Tvn6L-31SeFLMluwl1tmfPOcTlQZLrYn06tnqxGHVaLzIVim4cTJ7_q7oMhV376Mr6jTmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛ مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24781" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24779">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32137f795e.mp4?token=p1znvaCC40xAGMVKqfEslcVha9P2bVY-MvJxEZOlwIAmbSknmFgerFClJ5p8m_DpS__knxT-hLYA5VPjR15hVSsmtjFLvsT3ku30kYAwk7_cS_7EOD4BEQhQ6LUE3t0Vs6zzmL6IZsqMeVYNtAIECknENVKyACR_lxX1GFvUJoFOHwokBg2W89b_Uem11Y0DBC10uJ4y-BtHiH0ewe0kNTiTZ5dPFM3kIe-9rk5XgsAVDPLp6j5o8HSke_fv088quCSJm1ksiPjhfLf3uX0sY7y4iok3AqbjRysVod3EE2P37sfVBzJY-OvGpQVIw6CeJvQ75nKJKsLzutSrSXlnSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32137f795e.mp4?token=p1znvaCC40xAGMVKqfEslcVha9P2bVY-MvJxEZOlwIAmbSknmFgerFClJ5p8m_DpS__knxT-hLYA5VPjR15hVSsmtjFLvsT3ku30kYAwk7_cS_7EOD4BEQhQ6LUE3t0Vs6zzmL6IZsqMeVYNtAIECknENVKyACR_lxX1GFvUJoFOHwokBg2W89b_Uem11Y0DBC10uJ4y-BtHiH0ewe0kNTiTZ5dPFM3kIe-9rk5XgsAVDPLp6j5o8HSke_fv088quCSJm1ksiPjhfLf3uX0sY7y4iok3AqbjRysVod3EE2P37sfVBzJY-OvGpQVIw6CeJvQ75nKJKsLzutSrSXlnSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شوخی جالب هوادار تیم ملی با امیر قلعه نویی و شجاع خلیل زاده سرمربی و مدافع تیم ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24779" target="_blank">📅 23:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24777">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrswJlAwTacYcHNvmQLUlgWrdWUnZWv8MOAyNWF9JSVtC5Cq0Asqo8DDUkOcZCivLrq7eEQb8B-jXVUzk7gpy56tTmVDIzi9hLHu9bQElCs2U0_X0tOQVzkmoOKLQUFYgdRd0CwfufDMD1hJBKGsFep3Eye-TU0hU4W5C6Ak1cp4BtYvh83N7H2Je5wKc9CrjaCIBJR34hG9TerGEpbEYepXEHIdXY0p0x7IMO1zx7tekoB81UtncKAN8ld7fRIfDEB_D-T501m0DYQax7POlqG90mNENcpCvtMvvA8UHoojsABscUZivnz-dFRKKuFi8gPK7idnlLswJcVH4V6aqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون: نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24777" target="_blank">📅 23:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24776">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون:
نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24776" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310289702f.mp4?token=Bn8NKFA_RwkmVlaK_MkPEVhlaqcNGp_-bo4r2nzmM2tVD98BLn9oosRND_icbmqqDSp1HI3ECPgECIpQTGEbypYXzcL75p1H_L1MzUhLN-Z2jlinso5Xd-x9md4gmBAAUnxl6kUIWE9WpiKbjcUojN3EHiv-7BB_tJ-a8yqEjMR3GUEAhdN6LZP1JwPqcHGxkVdD11nAE3rhaVfgE82EKcSz-oLjUvbMruD5Laq_RDcBEFwvLxHT6_oFGzBVt-IGYVQ50az1A0bAbXbRUhuY-Um_9fDUzDzpx0gpJRLzj7KOQLtfbXqf9xQGj506miF82d-oUZVdejraTbmXvmPzrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310289702f.mp4?token=Bn8NKFA_RwkmVlaK_MkPEVhlaqcNGp_-bo4r2nzmM2tVD98BLn9oosRND_icbmqqDSp1HI3ECPgECIpQTGEbypYXzcL75p1H_L1MzUhLN-Z2jlinso5Xd-x9md4gmBAAUnxl6kUIWE9WpiKbjcUojN3EHiv-7BB_tJ-a8yqEjMR3GUEAhdN6LZP1JwPqcHGxkVdD11nAE3rhaVfgE82EKcSz-oLjUvbMruD5Laq_RDcBEFwvLxHT6_oFGzBVt-IGYVQ50az1A0bAbXbRUhuY-Um_9fDUzDzpx0gpJRLzj7KOQLtfbXqf9xQGj506miF82d-oUZVdejraTbmXvmPzrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛
مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24774" target="_blank">📅 22:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiQ78q3eHBt6BkHBq1U985F5nKzH8mwryFua09MFGsXM63OEvLyyMrioXZk3kyuOhBxudzpzGWbShQFG7_gw9YXAo1mx3AnLWg1i10o3jd3WGHgsNfIEc07eEH79ueFhAXzb3-0hNdA08pR1Yog3BaYHqzt2ibfyt9gCdD-UCrDVqBiz0lzIej6PH6BahsqNOFlNWNSBnxpgwC34rWw-XSl1-0WE52PrRoXjth35IA9LLDZ2fHKZ85DNCmnmfWjri51PyT5iBMW25a3mORKKElG1zHcYTuHPRyFQO6TD7qXknVA86ntHLaIVGFKTWzfOItjvXpbQyJooSW7Z0RL9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
این داداشمون کل بیخیال تماشای بازی برزیل مقابل ایسلند شده و کلاهدفش‌از اومدن به استادیوم یه چیز دیگه بوده که تو عکس مشخصه دیگه:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24773" target="_blank">📅 22:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwK75UtNbbNnO2dvIybfn9TNPc_jDXixXekEd1lQ8hBv07pqCX7N6mbzBkoEMAKFT2onfc6aW9I3NBk8Y6Rb_V8YS4FRB2p47bm6TFOKrNFFf7cGE4HFTu81DvYlig8Zcpsk74GttpggxqtnOYHP0kHSoc8pYl8hfPTrZ491y0PnQgNtMtsks0obJZxpDYkM_prS_d7Wda-bz-KQ48PXVbWJ1awex1d5TTNuYhtKyR7O3hWrRVcfu9U3aN6Om3749g28czNbU7Vu9sW9tNDIe8AxC1dJuPOMi9fIRcZCKCvF74CSLllujzi7JNVxO4eR2XbUwzzG4eUsZGJ77EMcVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبراختصاصی دوهفته‌پیش پرشیانا؛ یاسر آسانی ستاره البانیایی استقلال ساعاتی قبل به تهران رسید و در تمرین امروز عصر ابی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24772" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=tBUKULaqd7Lb-77bygUHNOSj9v_TE6KFSmEfo1bKKK-x3-sEuSGU0IsA5xnwwsGQaHAjExakmqE_h1Fp3nza32dvkDtB9uuWx1FCLY2bKYjF3dgEuPTzVB4RZqLsGOIfqNI5ZCeFozB19hARdLLYsrK_vMgSJ7oCWSiqU_1lEYmouMm2QXFuC56DbAunMfj9_ZO2bn5Qw0oj-mguKEkrH37bnNmNXBHR4KQ5QCaJMLEXdf-O8BeWAMhD-NCIBLSYFS-z8t9SL58aZsK5lvRLgmogs_B9tkELSxM3rKd-phvMFzwRTIGJbmGytvrxBvulHTLVMc1F0VENbGwdvXLAvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=tBUKULaqd7Lb-77bygUHNOSj9v_TE6KFSmEfo1bKKK-x3-sEuSGU0IsA5xnwwsGQaHAjExakmqE_h1Fp3nza32dvkDtB9uuWx1FCLY2bKYjF3dgEuPTzVB4RZqLsGOIfqNI5ZCeFozB19hARdLLYsrK_vMgSJ7oCWSiqU_1lEYmouMm2QXFuC56DbAunMfj9_ZO2bn5Qw0oj-mguKEkrH37bnNmNXBHR4KQ5QCaJMLEXdf-O8BeWAMhD-NCIBLSYFS-z8t9SL58aZsK5lvRLgmogs_B9tkELSxM3rKd-phvMFzwRTIGJbmGytvrxBvulHTLVMc1F0VENbGwdvXLAvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24771" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=drOGBh4Ap4m1EF9evSy4kYIu4skppPQ3BO8bnmahDX0oAYea48XIOJ3EWv3XX_MYBM-l14kWG90UqgNFk6sAmEybwfB3M7_yXAHD6v_dk5GrIn1VwF1WEJcfaq1Sx1PmukIk-FE1PblhyDHT3VpiTgHV_FNFnvUF3pD_fyblMvxU7NfauqxyNkOfqMPMrzgqrNxSl-Z64mf_a5ccPhMouPH_eBv4sDbEZS6NGM344pw-HRs02MJib8aE67KYu5DJLuJbg95ZftOuKzEakiG_oLhBJd-KsIeFBpy_7CxIs_adwHBCPh9s2j-nVqGFpekLLhzcrc23AGuHuowviZrZ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=drOGBh4Ap4m1EF9evSy4kYIu4skppPQ3BO8bnmahDX0oAYea48XIOJ3EWv3XX_MYBM-l14kWG90UqgNFk6sAmEybwfB3M7_yXAHD6v_dk5GrIn1VwF1WEJcfaq1Sx1PmukIk-FE1PblhyDHT3VpiTgHV_FNFnvUF3pD_fyblMvxU7NfauqxyNkOfqMPMrzgqrNxSl-Z64mf_a5ccPhMouPH_eBv4sDbEZS6NGM344pw-HRs02MJib8aE67KYu5DJLuJbg95ZftOuKzEakiG_oLhBJd-KsIeFBpy_7CxIs_adwHBCPh9s2j-nVqGFpekLLhzcrc23AGuHuowviZrZ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هواداران تیم‌ملی‌آرژانتین میگن: آلمان داره تقاص این فینالو پس میده؛ جاییکه این دو صحنه به راحتی میتونستن سرنوشت قهرمان جهان در سال 2014 رو تعیین کنند اماسرنوشت جور دیگه ای پیش رفت ولی حالا آلمان بدترین روزهای تاریخش رو در جام جهانی تجربه میکنه. تیم ملی المان بعد از قهرمانی در سال 2014 در سه جام‌جهانی متوالی به ⅛ نرسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24769" target="_blank">📅 21:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8vfm1yCwY0Sosepw4TtlW1wljYFl7Pr6nBVbDjezlbMq3fKIafa_KuD2DRYbgOY6bEvjXQueLCfANe6p9BJkBojdAOWA646DLGmBaYUKXHKCxC1w5jS84TZa2Q2o5LRABFQNbAj0__04Lx4XAg0OywCEtGN2GlIclGHCWSWKAfBLEf216ksoWEB9BUCG_hZ_LYdbbY2DrULsIaBIkknLf2KDnKhEuhZobrvD0ycQOgXiFuD9T4AySXaPf6-hMg3fXfKzmKNwUCe6b3JhoxNWF5VCyXjg9qXC1DpkiTJTM3gMWTY4xwYCRE8MNg-kPKQAvID1wzBlIyd_5xK02kX0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24768" target="_blank">📅 21:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rp2_kHMzAuMHIQLRWiHbbSbNZka_0969YFOzkEXueR3010mrkE_Ix-4qkKvUa_9XBSn9MTaHEsAQhsgX6tNLdCYa1rdLo7OpXAD51XmyyYsQ7ZaaJobvmz5wmi2pVNM_cg7UYs4rrGn1GXSgSS2DalxALy-fKz68VDbDJ1h55RH8W_DLlJHYvnMgpVuCSnpuYNkrIHd7fUAuW6ocTDkiLtWji96DpdWPfpwu4_14YCpEzDU5di8el23QcyxM4y9HpBrE1kwyJVUIptdBRB7JmW3ZjL4OF9YtFtJ4s9we_dTUNiba762boF240xZjHP630HB9V8m-8OVbKWpPSrF3TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه‌بان31ساله کنگو درنیمه اول دیدار امشب باانگلیس سه‌سوپرسیودیدنی و نمره فوق العاده 8.3 دریافت کرد... باید ببینیم نیمه دوم هم میتونه مقابل فوق ستاره‌های انگلیس مقاومت کنه یا نه. بازی نیمه اول با برتری یک بر صفر کنگو به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24767" target="_blank">📅 21:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOJNOTt-yKbyGh_HSJ91GRPKmqn3wrtUV1VtvH5VOWqaTX_-9vzQOi6Ll8wZb5m5wS4n0-ssY8N0LYVMwx06nRbH3OkX8RnYnc5JwQJdq1e7UtZGEDqd3ANs1HnG1wqmAPXEwHgInF9HIDCDlBnmyKUsgrj5wCS32oAqBc6t1GI4slFciiB0ihvNzTc3uTcJZWDYx89y3mV3s_dYJ1VGgp7uFhCC6pB1alU5EIX2K2WvYd1H4l2G4mVc3hfmL-rmihV3t3UnOpet-baW4PkIZ3GmTNYV46KTQ9r2ORWznCjIINs6ESycFU1SaTpGrouwPlMTWvkmV2FPh5fW4EiX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24766" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=aUXi6UxxOkojOeKWH9qnr-_RJvtZms5O6KGK5CRQXX2qGRhi1DT6tHYK_FIuQqgf5RwEbik2LIJPCAYiNBlxjYx2hKOKPMJpC2FdIq2rLchf7zcOKz17iYcekfTUbYIssgSwCRbTcipMxdJYxXPtx2SADSGru0p64sNWWpe__P7RXuZgLdntgXxAkQG7SiQrZUH5wsBR_pNPA8lgMlXIKGUUendPCZxKcGaHvZfnvJf9ba5kVCVYlEOtcNquoZWz06CVSIh0o3Yotxwlh2NsNwl36Kn2zn5aYdm_fksEBzCGjWs5KEOl4rRg8JyD_3RB7QrRyIAV9e04ofrHRTyIhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=aUXi6UxxOkojOeKWH9qnr-_RJvtZms5O6KGK5CRQXX2qGRhi1DT6tHYK_FIuQqgf5RwEbik2LIJPCAYiNBlxjYx2hKOKPMJpC2FdIq2rLchf7zcOKz17iYcekfTUbYIssgSwCRbTcipMxdJYxXPtx2SADSGru0p64sNWWpe__P7RXuZgLdntgXxAkQG7SiQrZUH5wsBR_pNPA8lgMlXIKGUUendPCZxKcGaHvZfnvJf9ba5kVCVYlEOtcNquoZWz06CVSIh0o3Yotxwlh2NsNwl36Kn2zn5aYdm_fksEBzCGjWs5KEOl4rRg8JyD_3RB7QrRyIAV9e04ofrHRTyIhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش:
تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی می‌خواد کجاش بزاره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24765" target="_blank">📅 20:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7GqnpX2RzJ3byyh2ZQ3WSdptEFfT0RNWtwTj8-XWNjG9iHIiVHdH5fi05iyRKLjpbuKQpcSqbIqUxegADfzs3LCmhp3qWRohQxqNX-gGjxDRYbXGvRuqTXOpLLGRFSra9lQvw76QK20nl2WAn2_e9uw-HJgSHkl0PMAcQFWEY5cFpFYghN-gL6jkNIba3q2ketLH41zPpyPS73L82yTSchwExiN-qk97r72HGAhC6TvgyyVpTWsqfmKIhfcUnbD2BOfUkypQZ00CqiCfG6x5pjr6pkTX1vhMEQ6lYz4sx079lCjC_Uwje4Sx2gh3vMmsAlYGUjoEP1xEoDi0yebVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره تیم‌ملی‌مراکش در اوج روزهای سختش دوست‌دخترش او رو رها کرد چون گفته بود که اسماعیل نمیتونه یه زندگی لاکچری در اختیارم‌بزاره. بعدیمدت میگذره و سایبری‌باقراردادی نجومی به بایرن مونیخ میپونده که دوست دخترش بهش پیام میده و میگه من روببخش…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24764" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=kIZvpQdvqIHOQjuXT3tPTtAJfWUi3flyCRlCJrBKuH42XsNpCQ7cZEBNTVYhtTRxlKFDHhUBn4iUGXvS2e4EqDeqnzlaVnoFq1_y_vQkKIq2Y0T2y_HbTT7CesLdfVX04ButQ814nlmjt1feEPsmUdGRmXWBws5IW3HjFj7_gZDE7uJcr2lqBk_BjPbdGy5fWdSgoaIW3ifDTqz8VeTtQmF618SUVk0j70dImJ77Bv1u62lYbNtThHOjT6sxckjmbXzQMNU7Z6i96Ek6WkIXIYqOh-kdWm_xTuiSbULyD1BSFkMESkHkhU9H5x2_qXtSLDEXPkSHRXnkXKMsKUwF6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=kIZvpQdvqIHOQjuXT3tPTtAJfWUi3flyCRlCJrBKuH42XsNpCQ7cZEBNTVYhtTRxlKFDHhUBn4iUGXvS2e4EqDeqnzlaVnoFq1_y_vQkKIq2Y0T2y_HbTT7CesLdfVX04ButQ814nlmjt1feEPsmUdGRmXWBws5IW3HjFj7_gZDE7uJcr2lqBk_BjPbdGy5fWdSgoaIW3ifDTqz8VeTtQmF618SUVk0j70dImJ77Bv1u62lYbNtThHOjT6sxckjmbXzQMNU7Z6i96Ek6WkIXIYqOh-kdWm_xTuiSbULyD1BSFkMESkHkhU9H5x2_qXtSLDEXPkSHRXnkXKMsKUwF6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24763" target="_blank">📅 19:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrhg1XnqXfN2CNYsDOWJ_wLZn7iwR6A93HxmLdD0c4Cqe4QnRjly93bVgu_NTibORXnRchUCBcXBS6scTeYBgbkRpNd8C7tDnqxBJ0qA42K7EhmgMMLPL6QAx5dmU3VvCgFRuYky4k9NSMbmkwrsrrJteCcELAH8cYRtNIEyNRKq5AerV6Ws3bpZPVC14xiHt9o6Q23pD1iQi1WqeMeDDV9iqVkn50BZfyoRdCjSAIp9nBTsPRovwWUcUW__mGXIbeIP-CVHYCY_bWnFsmYaFxAJLrWRbytT85OgUPeJN3xiXFAez_N-xiHekFhK4ND4PIY1nO69n0akwmsZwVkkDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوستر باشگاه پرسپولیس برای اوسمار ویرا به‌مناسبت‌جدایی‌او از جمع سرخپوشان؛ همانطور که وعده داده بودیم پوستر دراگان اسکوچیچ هم آماده منتشره و بزودی توسط باشگاه منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24762" target="_blank">📅 19:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=PHmHGvXOYBq20u6XY5Lr3flU4zVxOMHDjqA12ozrlUqVpUK3JJMxMt676eDXMtvjOMMrJTXZl4Iif8eKCaR2BL0P7uaFKpoTAndQonjKSVp9XFtyWw3byaWM0qDUNWh0RQGDaQyMRYZbk_C_NwSxghP4LkV-oU1vyR2FF7iN1-QLn-3219T1Dyk0unbCCw5SqNGtk17jJ56wQHbl6VRc7tJJ8MncA5Fco_mudFeVIChFAOS2-5Uk3OHwVyzSCFxMGpaoUEb2Du6WX4TI7TmikwDVYorhyy6GbZgOQdhJQzTlI6aRuO_FdhFwzEH4Frhfd6GIaAl-Py3NQZeGdIJZRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=PHmHGvXOYBq20u6XY5Lr3flU4zVxOMHDjqA12ozrlUqVpUK3JJMxMt676eDXMtvjOMMrJTXZl4Iif8eKCaR2BL0P7uaFKpoTAndQonjKSVp9XFtyWw3byaWM0qDUNWh0RQGDaQyMRYZbk_C_NwSxghP4LkV-oU1vyR2FF7iN1-QLn-3219T1Dyk0unbCCw5SqNGtk17jJ56wQHbl6VRc7tJJ8MncA5Fco_mudFeVIChFAOS2-5Uk3OHwVyzSCFxMGpaoUEb2Du6WX4TI7TmikwDVYorhyy6GbZgOQdhJQzTlI6aRuO_FdhFwzEH4Frhfd6GIaAl-Py3NQZeGdIJZRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم ملی اسپانیا:
«من اصلاً دلم نمیخواهد که‌همه ورزشگاه‌ها تشویقم کنند! هیچ نیازی ندارم که در همه استادیوم‌ها تشویق شوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24761" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgNC44ZuGRzgkGmdYhmk8vAHFhcrpkwsXSbQurnLzdprihnIoF9ARuCj02ZbC2z5qnJhQHZLsZZyT8AupZyl5wprRrrCEftYfqGuXuXci8XnPK71XMKyUZqQxbdI3MsiDyR1p8b2d1kG9LRUHVUqpcQwbDBOWgKOrj009zN8qkChJATCkNYfZwm-QdYfWedIDKzv-FoP897h6VzYsOfHJ38-HvfzxwzfJbJE3OCqdiVt8foSo03wnYK6TjCpci4cLGUvmOhNa4PZYnfNZP-96IOZ5DC1WlTBYfz35lO7ufHB8fK0ouCRVJPxOGRVYR8C28uXBJxH-WDA7yVjPBDG9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24760" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyHjaT9nEt_61igd9_wCvQR0pP95Xhs5TqdzjrRvENLDSbWugKRjZ0lnLlqmOPk6A8dahBybUQ42OMyyoIvKYmYtz3W7jOefiRGBCSzFQyzf9hd6krk3NstpfdJY7AjuzXhwRzphjkmcHheqaudj_pbHUg9JyTN7mnjBkxNrCo6NR4olt_eVDS_KxQeKkL_9CggKE-ElAdq4sqWOB6N1JkgBlasfeeOM17P80GEd7feS99wnMs_MAkIf_NwQrr2b-3kM3axK0eTJzHMtsmwERX-VyvOVdPDizNNCMuCEiFucJO0oy8-5MzlZGbmMut-X7oYX1N-MWxQYKdOXrm0Nbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24758" target="_blank">📅 18:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24757">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9tbK8gFrS__0Y7vHOwIqru4AUaMPTZEZxkXnw_SQmhf-H6Bf8pGjG5PYzjM40hKcgyQhmqqesR1mO1odJN4mS55Kk-qBOYc4e9Of5876bsCZYFG8GoqxpwVc--df1m6fyYfIlI3pArks2RQ3kXHnfiAWm2QAmZSF-_wp43tOvPviX_7ML4Rw6GLs2evFkRFyvTqMzdRTLm5o_YHd5wXzOTJkuGKJhVKe8FTERFABS9gAkFmFl9SbYqVYzF4WYHKdmAnPJ8bz7RmtgSuwQ6WrMBer4HKtHcve7vP8XtffY0YGX8wryCQC5mvN4O_tG0PmOP2yIVP-CNlL6CsZ9a6ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی
؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24757" target="_blank">📅 18:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHkRAZ87jGnh_RUAm01264NH5TDde6KtYZdFt9gKnWkn0JUgYe8ADhajKEQPnbyvT3dPmkxlFXy9Du7Z6R13hbM3WSQVSyrECQ_U8mAtYGUhDMSwQVu0JOtmrYE4HkDzr-J-ukn49fc2Fo-YgDjB6_7UcqOR0OTnR4FqWXlY5WKq2624-q0B6BVCoIRpbhDBBlHndl1YKz3BiFv0WkQL12KbYeoh0xuNK7ZTY-DawCBwAjiyLXjHRGtnkVFoW_xGOjbTR_2BFe7BnxYC6T9mvkKKI5Q7F5l3eusNOEIqtHDdzdFLDktYKZxs5GuWJuCGOdw90TizExWIFwyJBuWGvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24756" target="_blank">📅 18:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksNbUIDduce2XhBCsAW1ugk813veh1cKh-aDHyEtJw6NDR0i6lLUlxvna4m1N5KNcyRh94DFY2XV-_gCie1gkN22b_FTC1fgSj4yTMixMEV3l3jc0hJJTcnOrFByXF2KcF7BZhpDWnuGs3vdDpaPacESdglrs6rKA76TZGpisu9Cjq8b4RO7czEubEEeeI-KhCeCtbfte0T9qHfzlFG2HGj43XAd8zK91YxPEl3i7TGRtM7BiZNnp-eLKoFxaRyrfokxzxDPd_sGw1HK-snJ9-jr5NeWTBt1d7UzSTjlnsjMKxPqGTzfLicyczYxkdo7uhMJTDPe5BbZNWYjclp78A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌رسانه‌پرشیانا؛ اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24755" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24754">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=FBvD3IW8lkDDdItAF-xdHktZ_m0_szfRBFI7T7NdTc-LGfraA8dLEHsnWD2Q5QcL7VOnqfvT0GfsC4O3YSWgUxvupyMZYxGMdtuuDuW3H52rDXPnjWAQ-hGvh4-O6CXlVwa0KOjMevXBPtsJ259qVNT-8BT72z2SRg5d54zBGBlhERc9ThHe0BJLNJCbrIX_1olgPbWqKhK0gMM6JpyBvdUJ2JCqaQbI4Wi9vSYggFRt7tPp87RzkDNXLkfllPNc6Oh_VOAz0xTWVFhTmL5lsY-ama7vf2SEEb5DKrMJB9F8XNZX9pU_QOUN-7vRS8zhYsvzyiwt1Wb8SEs-fHyPMU4Y7Sdo86r_1IRgyZwEW3ULrINcrOTmyh70CmYN__P7AI6_PPZ_NxuCmhQbgCEdQGNB0LjZoPk3-pdu4-lcg3vIlYwApU4jqqNcoD027-iukxKqcjfAdY4TR6oyzJYSpkHjBzCOBJycdxxl1icYLX-NrZqK6TvrF5UplcTiRAHB_cvZSEpzjoEBkDEzdr053szNRmLh7DH4yzih_I1PcGpGMJlYT8mxcMSITrpCsEq0NfJFCnuDmBbF-pKy1N2NfYm3qbQNfhckqwcryVxzKpZjy1PNiOV9LivTesG8QxT-r6Zz2uFfVHLwBRiQvFduoGEHHZ7QZwVFxUVui0G-n9k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=FBvD3IW8lkDDdItAF-xdHktZ_m0_szfRBFI7T7NdTc-LGfraA8dLEHsnWD2Q5QcL7VOnqfvT0GfsC4O3YSWgUxvupyMZYxGMdtuuDuW3H52rDXPnjWAQ-hGvh4-O6CXlVwa0KOjMevXBPtsJ259qVNT-8BT72z2SRg5d54zBGBlhERc9ThHe0BJLNJCbrIX_1olgPbWqKhK0gMM6JpyBvdUJ2JCqaQbI4Wi9vSYggFRt7tPp87RzkDNXLkfllPNc6Oh_VOAz0xTWVFhTmL5lsY-ama7vf2SEEb5DKrMJB9F8XNZX9pU_QOUN-7vRS8zhYsvzyiwt1Wb8SEs-fHyPMU4Y7Sdo86r_1IRgyZwEW3ULrINcrOTmyh70CmYN__P7AI6_PPZ_NxuCmhQbgCEdQGNB0LjZoPk3-pdu4-lcg3vIlYwApU4jqqNcoD027-iukxKqcjfAdY4TR6oyzJYSpkHjBzCOBJycdxxl1icYLX-NrZqK6TvrF5UplcTiRAHB_cvZSEpzjoEBkDEzdr053szNRmLh7DH4yzih_I1PcGpGMJlYT8mxcMSITrpCsEq0NfJFCnuDmBbF-pKy1N2NfYm3qbQNfhckqwcryVxzKpZjy1PNiOV9LivTesG8QxT-r6Zz2uFfVHLwBRiQvFduoGEHHZ7QZwVFxUVui0G-n9k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برسی‌کامل‌ودقیق‌شدیدترین‌مصدومیتهای مرحله گروهی جام جهانی 2026؛ عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24754" target="_blank">📅 16:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=L5p6MkwQjpHHeelgnk4Fl6fbmnrG7DT-uneOhmCeggcDGY4o3hQbHw7rnnlAIL0f5hJ9ofLfTqcuCPOFXPE28cLnLAvFkYxdszHKXWLeheZJZcOW6y1BYSVmsli9MuZDJ5Je1Y81IaYDBaHa1_7H5s1-I5-5obMHRPvGT08ADlmLClNOxKYpIOctNYKLgRxYCEJIJTeJvdk3PyFQVYPjZlUPGu59m3-qQNm3xKFa-kJOyCcagfQXLxNOjER2BavkFHOaJEbwJSOUCOqtGYnhAMIRHXT0pMGtyaEDeIsPg6hhxltw5qSQFX_gJXFsaI_2WHxvvBxzTFet2r8LKpJFHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=L5p6MkwQjpHHeelgnk4Fl6fbmnrG7DT-uneOhmCeggcDGY4o3hQbHw7rnnlAIL0f5hJ9ofLfTqcuCPOFXPE28cLnLAvFkYxdszHKXWLeheZJZcOW6y1BYSVmsli9MuZDJ5Je1Y81IaYDBaHa1_7H5s1-I5-5obMHRPvGT08ADlmLClNOxKYpIOctNYKLgRxYCEJIJTeJvdk3PyFQVYPjZlUPGu59m3-qQNm3xKFa-kJOyCcagfQXLxNOjER2BavkFHOaJEbwJSOUCOqtGYnhAMIRHXT0pMGtyaEDeIsPg6hhxltw5qSQFX_gJXFsaI_2WHxvvBxzTFet2r8LKpJFHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌فیروزکریمی‌درباره‌مراسم فدراسیون برای استقبال از شاگردان‌قلعه‌نویی: اس چه تقبالی؟ خودِ فدراسیون از این کارش خجالت نمیشکه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24753" target="_blank">📅 16:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEMljLE4JUZ48_fKHD6x1Q8_ycy6uA1Z8HznJw8zAFNBA7wUW8ZVKyXcOUhYDq2i9LUb1Zyds0AYJF70cLCO3LJddt9PiUwrtgW5rGtLGlIUsOPrQqwksXtyhvR_EvBinGmHsbg83Us1dLq-CzOXcfQr_nk0WdvICwRwZ9STUVY_V0nzvJaIBBv8UK7WrGVRG2nWvY412atGv_-e8CFKonBd0gBpYvfIkYfxFgkGZCKhdHS0isnO3DSKX9GxzMnv_bDuZrm16fBZ5SPoxrY-caegYI2HXA9bXUPFhCl2VOXbQtwKl6Q2rs58eFWfV-DYbOB2ofHn4bO07X0DVYOreg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24752" target="_blank">📅 16:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24751">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=CMz0JgIm_b6QWeeLQGELnEtieU2fWWGhouy9yRjKlIxu_slo8lSZCRZUdiRd-6k8w4bltVAWHr3w8bWSkngDfskkZQj_cdMlehxr_n4R1ZTDqaMZQJ3OYqpVTB605-loRts3-itl2pWtyasmuWvTGFa9TghWd4HPCKMakNEWruU_-wyhVUl0jcK5JhNukpE-R8te5KKG5fQtgQyT0gNImy3Qo10DbaerAcuscw-1AoUhZ5p9_rSWJmFUtsJnUW8278Q7kVvJnsZ0I3LcIHKSt8dSTZbEyObrAA1d-dcM_lxAClJwktEuHfvBdBK2O_hBgErRdN7O9cZsYubpTlk5hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=CMz0JgIm_b6QWeeLQGELnEtieU2fWWGhouy9yRjKlIxu_slo8lSZCRZUdiRd-6k8w4bltVAWHr3w8bWSkngDfskkZQj_cdMlehxr_n4R1ZTDqaMZQJ3OYqpVTB605-loRts3-itl2pWtyasmuWvTGFa9TghWd4HPCKMakNEWruU_-wyhVUl0jcK5JhNukpE-R8te5KKG5fQtgQyT0gNImy3Qo10DbaerAcuscw-1AoUhZ5p9_rSWJmFUtsJnUW8278Q7kVvJnsZ0I3LcIHKSt8dSTZbEyObrAA1d-dcM_lxAClJwktEuHfvBdBK2O_hBgErRdN7O9cZsYubpTlk5hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نقل‌انتقالات
|شهاب زاهدی مهاجم سابق آویسپا فوکوکا به تیم‌جوهوردارلتعظیم قهرمان فصل گذشته مالزی پیوست تافصل آینده در لیگ نخبگان بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24751" target="_blank">📅 15:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‼️
دیگه وقتی سرمربیت اینجوری بهت تعظیم میکنه فقط یه بازیکن ساده نیستی؛ کیلیان دیکتاتور
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24750" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=Fk8hIJPiKozH2oM1k2uky54sBnwWgFPBaGXhhESsB9j9poOne7beiK9adT8tLIGAo3b78Ub5Yw9PFuq_IwE4tl_i3vYXFoyzp2G4t0WyjGy8S1UuGupX5MKZp-9wltKZiTlb__a-Hgvi9KxulHfYFRFwvYVhiDMkeOCXzUl-U9cfcFJo2gA12_5E6MEPmiRWYwuigtPZPkl8C32TvhOcHT-s3xF_OO8HRmlOfjDC1mY20hD1oAn3ba29gC9fx-lN394bmXtYoaJrDa4NZw0uW435RnBGHArleL0QEfwGBl3sM4Acz9v-Zc0KoaLHMvLNwQ7-53ILaeuGE5efUrCxrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=Fk8hIJPiKozH2oM1k2uky54sBnwWgFPBaGXhhESsB9j9poOne7beiK9adT8tLIGAo3b78Ub5Yw9PFuq_IwE4tl_i3vYXFoyzp2G4t0WyjGy8S1UuGupX5MKZp-9wltKZiTlb__a-Hgvi9KxulHfYFRFwvYVhiDMkeOCXzUl-U9cfcFJo2gA12_5E6MEPmiRWYwuigtPZPkl8C32TvhOcHT-s3xF_OO8HRmlOfjDC1mY20hD1oAn3ba29gC9fx-lN394bmXtYoaJrDa4NZw0uW435RnBGHArleL0QEfwGBl3sM4Acz9v-Zc0KoaLHMvLNwQ7-53ILaeuGE5efUrCxrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یه‌فلش‌بک بزنیم به این صحبت‌های مهدی طارمی بعد از دیدار ایران - ازبکستان در کاپ کافا: اگه تو جام جهانی پنالتی برای‌مابگیرند من نباشم کی میتونه توپ رو گل کنه. جز من هیشکی نمیتونه پنالتی بزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24749" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JF_IyyG_58Zd1AeCab8eUtfW2xvo_jiTJhQzws_9J9q7Ogiq5vuB7XIyWY698HCsYkWBQvl_YJMm7pRfAKxN0jsKspUv6Vkfy3QW_exxUD4XrbShYl6Qu6IXuLyQuBGNg61DByMwR-W753qpHYCp9ZqsScS_BtSG2QnRr0Jg0oeDg3UsgovUpQoZyVAz69i-kAWMlgyb4CD1wsOwXJ4_nX7_plG-_1Gm66qBFWe6MvyQSmq158EP6ERJOw6jmetwUyYzocuEfEX3FBHUCEz867iuzynF9WvNouf2eqj87xVrsQh8CexfRLo6KY1yGLXoO-4TBqZxKRhiswyZHdI4PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرمربی اکوادور که خیلی عکسش از لب گرفتن از همسرش بعد برد جلوی آلمان وایرال شده بود، بعد باخت جلو مکزیک استعفا داد. اونوقت فدراسیون ما برای‌حذف‌از آسون‌ترین گروه مراسم استقبال میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24748" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpNig7ElzpaFw34Z7Lg57YZBZtWZw2kevVo7QirEFq1XGj2_tpjDhqbyq_2AVj92a17-6R9hpKCufaoP2JPYT4_WGpaS93cdeaWbtvXlM2mLywfla2eRUH7siHdcdUcpmq6vgU1ciJWDuuylQF4ScVYdOP2pPwj6QkLHbsqqbdKvrd73n0wFaHzkQwhkAlwsqPraVUYwMxE30b9YhsAtucoHMGGb1V1mzQSczVsHDD1X3O6NfJ1IPH1JWEIBA-FAwZUT8nUW70KKALYOmuIqNhEWwu2jvj7Ddf3oMKdZNyhknTMPmXrvNmLdkdCW0Y6ZYjCHrt4H65YzRbopeLk8Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24747" target="_blank">📅 14:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24746">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5HubfEiZtrbIK1jLv_7Axm5UGziP_9yKiH1QwJqbh0bkAEHcAX0slC3iEuwx2eVAhHIDV_ah2oKXV1ZwogHX2E5lHI8NE3IkEl8bWuklIjt4_2nrwnU6C3fLJw6JSBNCmL7O6iE7KZOZelqV7T4srv5qXLvsY8IhyeOQAPpzwtt7bVdS_l-MSpLM7PH95jFdlhOANF9g5S0RqwW9nK07_-zNCmKGjDxLT3jbO6TjMeUIY0XGc4qjlonyHKqJB-475b9UgvVNwUmqpcDKw6eeREZQSkupXdjmfVRi5Uf8nA9GZpYsc88bnOk0so6X_BV9Bi1a8RlBy1jcY4OUTrEmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان با باشگاه دورتموند بست.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24746" target="_blank">📅 13:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24745">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPlAgkeF1cvWvEpKXRlynOs4z4MDtFejXymXZdOOrd7j6BQis8Qh_dqVlkUgxWjA_1G3OtESlZljpEefm0Lz6bnkp5Kq3X5uQjhKitLzzHSTVvADs9PJYUZNvxVyOguHt1x3_4bv25Fx9DcAyByuLO3R9R5uwe8UqtL3HcAuQk6PFXVFqlHjasgK4RQsaYGvpw9HYpYl9EQ3DCCxB-l4QQxk9YuQ9_pcKzw_jvfRioVMi4wmMxewgSw4kYyaVylEqy1KWBbFyLDnGWQjQNukgqi4lEIf4hzxbY95LOKMuvblGzkJmhsgorxsXVlfqFu1J2HmHTnBzkm5lk-9SqUYQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه‌بان تیم تراکتور از شهریور ماه سربازه و احتمالا راهی سربازی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24745" target="_blank">📅 13:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24744">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=PNnr8FIbY2liyI1qMEgsLLIaf2WFTOErZaJm0sDosRD5sApl7iUMCwPs6J_UlGrf-ZBgbqxyxBcQ58cscXyZc3HmO_t8RzGtqakCG2aMEp2uvP_IDM4s_7q4gC2JJiZN-ciS8g-0sxIQ6xLIAd5DjkYQ8XqcrpJKLOGx0RE9oFW2SBlq6UsIwJ3YeXe8ATaSrJ4neLt6yDh3SqEuxvongIKbvOLJVrTJdoDZ_972VkhS0W0wRi6EgKTORxs0clRq9h_wF5ZyLHLN3kEEFDCAotW5Zc1x5ADOenyvBUtGaz00MDihpQARUfxc1ycfH_mYhyPPmEC92vZBn0oDrkEcwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=PNnr8FIbY2liyI1qMEgsLLIaf2WFTOErZaJm0sDosRD5sApl7iUMCwPs6J_UlGrf-ZBgbqxyxBcQ58cscXyZc3HmO_t8RzGtqakCG2aMEp2uvP_IDM4s_7q4gC2JJiZN-ciS8g-0sxIQ6xLIAd5DjkYQ8XqcrpJKLOGx0RE9oFW2SBlq6UsIwJ3YeXe8ATaSrJ4neLt6yDh3SqEuxvongIKbvOLJVrTJdoDZ_972VkhS0W0wRi6EgKTORxs0clRq9h_wF5ZyLHLN3kEEFDCAotW5Zc1x5ADOenyvBUtGaz00MDihpQARUfxc1ycfH_mYhyPPmEC92vZBn0oDrkEcwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاویر ارناندس ملقب‌به‌چیچاریتو که در تیمایی چون منچستریونایتد، رئال مادرید، بایرن لورکوزن و وستهام بود، از افتخارات میشه به دو قهرمانی لیگ جزیره، یک قهرمانی سوپر جام انگلیس، قهرمانی در جام باشگاه های جهان و قهرمانی در جام کونکاکاف اشاره کرد، وی به دلیل طلاق از همسرش به شدت از اوج خود دور ماند و دچار افسردگی بسیار شدید شد و در نهایت سن 36 سالگی از فوتبال خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24744" target="_blank">📅 13:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24743">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQCryF4y25LuSaDL8FzFeJxGJa9EqFt4UD7ktjneqsdd5mRGp5sCK8y1NGHumN7tFGpqK9gIwf3Z9CucieG--5CeP4LGk7pAZdW00Mtffqil1p_RJBESGIveUYMzXBFFF8tYJZo81OP1YAwISTOHTP3JbXYHCKjMJk2V0fq60n1dGeFwCMLHFQZow_71I6WXPISk5gEhG6cAkMuVvmPP2pKbGafos2xgWIS81A_GcTLrgp5dG1eGwjUx98kQvonNGopUljwfSDh_G0PQ4lh-EOewNy7fQMhP4IzKi5FfIO9TxXMGha-zbKZSayltD0Q1sQt7y-68zrGj5xcef2PZBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24743" target="_blank">📅 13:14 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
