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
<img src="https://cdn5.telesco.pe/file/tRDeUf4nd-Hd2dQli_4ieI5g3K2y7QIDthao4l0wpJEiRhAPgQmfqD0tQpclN2B8KMteoXTmcIFCWwQ3rYFWJX7kBPaSpOyUIuWt1xLsSkYi6DTpx1W6gLgcJbY5Y314h_tjhRgvrwLW8mdkmYD2gChVXAN0XDwEWnH7NgMQ9HeNCnwwsAw3xWG6f1jBCyCtu37CDRltWicqak5h0aLXisJdgJ-C8jLcOAaOUyd0kYAONl5x354HcM6ejViEfo-jH3w9Wz4Xi8IGvmySLS-aZobiSoomXW_wlsTVkTK8pIvarPN2p7so0LG1kkgZrnAJamWvjI8gTaRJUvlreJ7mXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 524K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 08:33:32</div>
<hr>

<div class="tg-post" id="msg-102041">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0tVyRI2F7zwr7B-U4jNYW2iCJi3xEDdNQahxrW4UVZtHFugHnsW1YS8lBW1UmeqwKm4NjfUyKR5th8BNE4Kc625GWXzXYuPkdjB1WmTjEh0AbbfyTCoUHFs7DVbwedtZ6oGZEojViBGsqNRgochDNaUAUxFFqzttocxyRzSl01XQPTPaztN5wpZj0ieolis2JYOlTtn41uwOO9u0rR_FkoWJocn79sx6f2gAca8q5Vm5Ug-6uLyZ3joETcMuS2SyegS2b_ICMTeT7_1QA86nVJW1nqsgL5JRBjbKAbFXIJv6L3r_9w7np7qtY_IzituA8E785dBiAIpSNmHXimGfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
اوه‌اوه یکی جلو فلوریان پلتنبرگ رو بگیره که ریده به سر تا پای رومانو:  حالا که ما را "دروغگو" نامیدید، شما خط قرمز را رد کردید. شما فقط یک روز پس از آن، انتقال رسمی لوزانو به آینتراخت فرانکفورت را اعلام کردید، و با این فرض که هواداران شما احمق هستند،…</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/Futball180TV/102041" target="_blank">📅 04:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102040">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpdGt5Kgy1KiunEN0iqTlPaeZEzDi0vbGfThTfFvSATC6Q2pEKs0QxgIrBG0v7WwvxvJjnAEDyTbgZ4vPklVpfR6Q23xw9OFWrATjS9mBeZqojcyN4JX68uzdRh-1lZ471T7a6L_1POAN5uN4-F0EcgU482vVLZDDGOCPImX0P3jYF7J-CMPbc7NIxgNEnt8ppLGxnfsxBw4qpQJLsiXqaDvM9g-OSgaaWWqi0lZ7nCZBs_ERXEK8aarmOX6GhjGUw83bQjIIoksk_WBehBAO5CU57SrQKSp-QWHdSGs7aUJFzaK_jIN5QU2qcv7N5sF1JXRdnoiwY2Up8w61T61Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/102040" target="_blank">📅 02:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102039">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWAvSnAt3rcVHwKgUAel5StFUy5wf1SxwGLQVYSiVTzDDCyXwlFjusCodkCe9cYeiHScBOUgGpKV1W6pKmXa808QOkJCssNOTt1ky3HeaMMS5huzSVq8HmpyivYPL5GQR7IyrjUdm53RiL7udQPKIsWWHiG4m2MlYVBuDI56f-JvY0uSemB7bg-NZtH0Ar1OEe7g4KmI6QLxspQ8QNgR1bFCllw1wxEpcfMn2O1ltFQRIeDQcSz_ROo9W_s61tfWnCXJsgWlu-KH021w-r6hCf8uyJvZu_pJXIoNUTgiFAk1QkcW6TGeI4hAhb6DaV2XaLS-6kpJK2d_i1-H2atnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری
؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102039" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102038">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWrrbqIYE468t1YJSj3UJjIkHjAGt6cc4J-wcAZqLBCpI6FiTXHn0-nh2_PTRlCpvzAUNSi_B5bBYR85zXKeK-EctyWcrcevL5g_5UV5bm-Ki1F8Vx1cCuM-EKUEo4hjdvsB_MgTrpwNevQ6AQ9B1uJN-i-d1MOw_evAHPNwtPJu4JPHDQf6ypVN1h3CHCCo56syXvBXH8fkaFlBv541rTp-F_yzfFnql9z72--mS2deWDrw9VVv8FtJz2B0mFMqIJi3fo1XhSccQWqoHy3Zsv4dIpsYHVM5Cw5RkWhzcuGCeDiRU0Qa7Ukl4WWIdmq1NkbJWfI3o6xOsqbcyhjXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ماستانتاتو بازیکن آرژانتینی رئال‌مادرید قراره به صورت قرضی راهی بنفیکا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102038" target="_blank">📅 02:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102037">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZL6-zjqfe1m7RIDVYmiolp6PzjPyucY0xcTbQvTuJjNOOWuaanCTyTScKZ1J1OpMBXoMulXfGe0z9OLHSO_xzKRXm95YdMyP3a9wbMOSPAUK3OSr2ft-twp8ERkmcCl3zTVXllCcyJtgC9JAF9O7jTVTnxtVHVOaTgEIzQ2_4YixrvhOao2LTfEAEcQzIGO5wIWrROlVOZvBiR3lUIZEqG0KOZmoNuQVOQL_z-PTIiCnfZoSpdFxQZRoj4KzDpi3Od0w-g-vn49o1nhwXjMs1lf3okR5NoP3EjjSXu-hzjteYuKZU2rfCZLCHlioeYzOPxk5K3cDO90Cx-VcA2HHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
جنگ بین خبرنگاران مطرح فوتبال اروپا بالا گرفته به طوری که دیوید اورنشتین گفته پیشنهاد رئال‌مادرید هنوز مورد موافقت لایپزیگ قرار نگرفته و نیاز به زمان داره و به نوعی گفته رومانو فعلا زر مفت زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102037" target="_blank">📅 01:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102036">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/frQ_pnVqbi2FJYon_dYsXMEhASOhR2pKWD-9-KBNFxJmqDj8w_hBHpjrtdDPYtvxbXTRRxmmbBn4AeubpX7h1u59eCGOMxSZy1U4K8wEOcJEVzR3CCTLa8nfquT5Oas85X87rTUfocB-yS53FKy3WU_7_7BlkuEJI7ej9cEDUgrliRyVSDqXfkGV_ZiF-pZ_hjtjwe3VNWjzen5jB22n2Ypb5nMf3DJH3QyQuf_D-xzsbAZV5D90QoXLIQM897o5M_vpNcOc-GMSgWnTcsdwpdJ9yRWUM7lgSdmg0AxT4ztThP0arYZY0Hy3pQmZCfKWjALfN-z3zRF5n3Nt89D6Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرخیو والنتین خبرنگار فوتبال اروپا: ژوزه مورینیو به کاماوینگا گفته که فرصت بازی زیادی در فصل‌آینده نداره و بهتره به فکر تیم دیگه‌ای باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102036" target="_blank">📅 01:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102035">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNjiOmWmadARLrE-reDA1udY3A0Y7EYxLnf271ANuu9ScwQ2pPSFJ-weLmRGES_L9E04_Fw0EfXLUOaWYzOCEGCPQqInSp1oHfl5WJi8yyFywWBh4Gw4DWhNX6jG6mjPI_cDt2yI5MEYY0XJCoKmIYaZ_KfxSh4UDmALIqEANGD4qBblJAPZmElyCcqfLeozypZqTLoj2obOm2fqGDUNBRnIDo0ENvyIFZ4dW017jLu6U9koToLV-r9A3V5r7VxE-X2LLa_OEuIuhsRo14vT24XlvXUQeZVlkIuP8ccU939eeGY1jnvk-xr5W46jd3rtBvCljfuUCjj2TLpb3esqsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102035" target="_blank">📅 01:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102034">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1wfxSpDixJNz0fbYTrnmQjgqieMonMXvEG18_i_Gwrtd0el2SGREgA8r3kj3LxnDhB4WIANch1vTSisVs1i8V3e5FLcxBJV4f5Q1oNH2NgvG0XCbEjUvLBMMYU1eCvSM12yYpK243vyGbX_Tc57_zLYBjCJw5sd5fVPgS1Bj_Dx1NR8U-XXqd_g1-k2gzWL4ZNG1T0lNEKnnqRX5i24YlDefhy502c3oT_sSgngM-8GAooSSAm01U_geD5X9xY3L8tNvLplg9dmXd7-iPIpKZEcalApo15x32rluUWYWOH_VALh-aSr-wH-rF53IavoJyIKP2FS7g5VY5OBenCCPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
تلگراف:
مدیرای آرسنال معتقدن وینیسیوس جونیور همون بازیکنیه که میتونن باهاش چمپیونزلیگ بگیرن و هرچی واسش خرج کنن ارزش داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102034" target="_blank">📅 00:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102033">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=dCZ-T5VzxtsTbZ7By1V1guxkLG12Cjqt1-bSLFK-PaGXf2rLbFPqmB4nkq01XdP1ZoXS1EH6droN2ImsEYiBU3r1ee8iCYLCX3t4iN41nCnc9PkyA4GXUWcBdQKOiyjUIWwKQLHHdgO9_Zpgw-KsJKw6iej0zVeAoKX9zGmDYK1D3LKRLHcafx0e2LGJxvGS2wi02bZkP6p_KlKPMGEfqduO98Vt-hpBZ7Q5iaFnnmzjJmwrJl5jbh5K1kr7yJYDmzyslw-dUCA8FGz-jI5twHcNbySmX9Xg_8q94qj7y_zyHAAYYr-lCBY-O9DcFP4brtOk2UFRyOySjaR1E1KXcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=dCZ-T5VzxtsTbZ7By1V1guxkLG12Cjqt1-bSLFK-PaGXf2rLbFPqmB4nkq01XdP1ZoXS1EH6droN2ImsEYiBU3r1ee8iCYLCX3t4iN41nCnc9PkyA4GXUWcBdQKOiyjUIWwKQLHHdgO9_Zpgw-KsJKw6iej0zVeAoKX9zGmDYK1D3LKRLHcafx0e2LGJxvGS2wi02bZkP6p_KlKPMGEfqduO98Vt-hpBZ7Q5iaFnnmzjJmwrJl5jbh5K1kr7yJYDmzyslw-dUCA8FGz-jI5twHcNbySmX9Xg_8q94qj7y_zyHAAYYr-lCBY-O9DcFP4brtOk2UFRyOySjaR1E1KXcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
وضعیت این‌روزهای لیونل‌مسی در تعطیلات:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102033" target="_blank">📅 23:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102032">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0SzL98f-p1xRc9J3ivfPtYtQiv53Depu0QX44KBvUb3UcsQUoN_M6s3LqXmssimPK7Mtou9mjDza-LHUHAHEEBHughAvZY0uVWeB1xiaem-wspzuJ3YmsO9W4Gkb_tIO2iYSu9zxvOLFZQ0WkG2ZO4zbhbNy20XvS6QIcX_L_MIq0rqzu5nf8bjNLO6CNvDBuI-6CwFdywjKk5__i5rTaS55dakYgI5s8rSsd82-f9jKY6NwPqp0BU2BR7uuU6AUQmGEyDpopvhNNnpFfzPDgHPnDcEte6yT_4oFHCohSvzcvb1Z6X7Hz4JMXRe5EPoqk-h6coyIOJroCuLKJyX3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📮
🇮🇹
دیس فلوریان پلتنبرگ به رومانو: بعضیا همیشه میخوان اول باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102032" target="_blank">📅 23:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102031">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUxIlRX8zuSMpcS1Ajlm6MLt3Q9Pl4QgU30JfZBLev4xpHQzTZWdcMg1x429Si6trJTywi_u-gybyO2kgICr6fexMdYVHQItv8JaXJgRp8smcKy1Y1sLj4UA1Uydvr3jMyaQ7_zhT6iXMhx6o_EMttg6Ujug_VH3kKtPqSZso5Zml1ocN965qQ1gIaHEG-tI1JLCHuR94V1ZAsVT9JNCS_QCiGDGaotTW9zYDFgidFhqx0ZhL3UmMwS6sGNniJTeWLYUzbSf0gTJA_5y9Gx3JNd0glPZK8d-3DXNO9VeYbrwQEquO3HcP8MnoA2hlQsucadjuRC3c5vEqICi70xGsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
فلوریان پلتنبرگ اصرار داره که هنوز هیچ توافقی (حتی توافقی اولیه) بین لایپزیگ و رئال مادرید حاصل نشده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102031" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102030">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102030" target="_blank">📅 23:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102029">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=FRssKzQhuxaVfBREX2ueCtI_hTuAHubwHFgsqOmU0irBXAy8GP7gC9yBuyf80exXTP4XFJbgBjxK7i-XcTtIyWsQeGRn1Kipg7f7ODtnWEQHN_7iVHq1NZOJK9quhTvciT_Nl7b6kyNAuUt7v2R3qw0B1mvHEMzuths57XbLQM_w8Df9bFPJzk2yZb-kXn6Gr3XmLLiFx-ObGM5IQC50pgfE6M2CrMZFQXL0SpwUnFKgGJmYmE3K4CSzZhshdSrJTIc8zaQOlNvnIyVU0Ca7lpVRH_u3Zi4x2_ngl6i62PtH-BPmYpctHcH5JerLnVTm0K0RdwV1w0BMxgjJ8830Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=FRssKzQhuxaVfBREX2ueCtI_hTuAHubwHFgsqOmU0irBXAy8GP7gC9yBuyf80exXTP4XFJbgBjxK7i-XcTtIyWsQeGRn1Kipg7f7ODtnWEQHN_7iVHq1NZOJK9quhTvciT_Nl7b6kyNAuUt7v2R3qw0B1mvHEMzuths57XbLQM_w8Df9bFPJzk2yZb-kXn6Gr3XmLLiFx-ObGM5IQC50pgfE6M2CrMZFQXL0SpwUnFKgGJmYmE3K4CSzZhshdSrJTIc8zaQOlNvnIyVU0Ca7lpVRH_u3Zi4x2_ngl6i62PtH-BPmYpctHcH5JerLnVTm0K0RdwV1w0BMxgjJ8830Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره فوتبال مملکت علی‌آقا دایی
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102029" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102028">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY2JFDMzsbW8L6RRvY2qUxmdkdLjQrEcu_-wjNMgoQ-H1EpXmsmMYpOvR04_WdK53Wekoo2HSiWu_IL40Ytkt14rb1zI-6uxs_z6Jcr1qtA-4y31kmE3bk2FF1ePNuBZ5-Exm7EHQ7qkSwdPHSfjqzcKpgI__5l_W4UkFLFErq_sy1ex53eaXhVoUtWFkP2BJonrzR1ZD4DZG_Rm_iAFdMOG5CfVkPLKa2kQtN15iFlqLMxk8-4I7XE8CNt0-c6_bH5EYUwhRElKHJx_BFRzz3D1Dnhn-cvYuxERj3Lx3lJ2hJwBqizJ6r3wgitJ2wJKlmTys0tNICQ8nJSx8Sv-XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👀
رومانو:
🔺
خرید دیومانده بیش از 100 میلیون یورو برای رئال مادرید آب خورد.
🔺
مدت قراردادش هم تا سال 2031 هست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102028" target="_blank">📅 22:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102027">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xt_XajTURcDUD5hbNel_ZBCYMlP-EwDCo5PRi3h1LGZ3GtIUQs76eHvaHOFfqim5DExA8NidvudbtcgSK-2r5Uz2Ys3i1XAjihA-4vdunSOZm-WtM5bO8ItpMabUim870jPYACMWDzOa441nMN7vs4fNUdSTiwaQDQsSAC1r5Wgwd0rON_CQktnqL3ntYR5zh96Go0Cx_bze5cpU9DufD33szDjIL74Bkr631d2hY2wYZXooIKcmdBz8r-jIjw8QH5k7g3wNcBKR8eqKJFXfAzWJdIR0NzjRfYYtR8ZFOcknfPansDoEAa3i6t9WPBvwinwPs6riNn05RKyNspTtHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار پرز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102027" target="_blank">📅 22:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102026">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست. 𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102026" target="_blank">📅 22:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102025">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tofSIsTrqfLcoSC9EJsV_ErDB-Niej7QCFYN197iX-b_UDhbQ_0GaEyHTfGdXmspPhuqfBVSjzXtOAcpQ3tvSgxsHV_9gmSxH4KMbEgc45Y0ORLL961rswsPb7rabGOBhU7Au8O6xiqAo2pJi42ohX8x1JHQToJwuvS0aZVooVZ1kAiQf5Ntd5bkvjXj5xC8f0Y1yZckWu-aeQTkWhTZapCe1m0a68k1kqJXRp3Gfa1RbYWQ9U3_hzaMXVz3_ePiWb7XERiMgI7NP4uEkWv0JCJd7cihRb8QIDKjB0V-DAUCcKF4-_MS0iT0aBt8DDmbp2MyTxJ3jnnXbz8k65_3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
اسپورت: خولیان الوارز گفته میخواد یه قدم دیگه برای پیوستن به بارسا برداره و بزودی انجامش میده . نهایت تا ۱۰ روز اینده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102025" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102024">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpA1myXDX3jdUpo6PspsHbMq1k-tqiJpN3mGYBmwD3XoPoJAJKQhj1XYjnnVTHMsOvMCo_oXQIJwxiLPDz1gjIFvRdUf8nJ-fjM4OjjPXlSBv3eVgK-lBBLUixBIYGrkfXYC73jihtoF73sBApDjod1oeeU9JTwrzcvFPMq9vJwkjMNb3JjaWT2VDBYFbM-Ydo-8J3xcdqdCs72GyYoPu8yrXfv72Rw0AnW4SVubAUlpcN_OFT05tIRefc_wQo27ZMC7pVrJIxPwbE0qRHH_8P5NdAoGJ-T8lJEYu7W69RQus2pIKL066_CX75Xi4AkFsGKK91VQ8NdEXZTubJGchg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
💣
💣
#فوریییییی
از رومانو:
🇨🇮
⚪️
یان دیومانده از لایپزیگ به رئال مادرید پیوست.
𝑯𝑬𝑹𝑬 𝑾𝑬 𝑮𝑶!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102024" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102023">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=BbDyRDe2uaPqO9h_XTou3bFQrZ4JUgHDPZdBDaTVkPAxalp9waXzT0xoB3CacwpV2XNSQZ9UJqS_azxz7pVDSw7z6R7PjF8EzwuJ7nFK2dUVvsaHbw0SJ7fUA62T08kmED4XHITlmySChw9bx4dVGtWbW_rn6i_jXeq0K91NQhAf6giXZrj9OJ5v-EOqJY4MSyvuqWoWYWcYm3lnE5I3S1I8hLTMqX1Z413MZhqfmSvDpLYWcsr8TBKFMHr6A3fGsWEHppFmFUnMl0FHsjjg0yDCMPyKnr--Mt8aEVVaUBRl44kdYUmoBF-tJtOlUMlQ1wtcw__jh1vk_LgnKWoWYylSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=BbDyRDe2uaPqO9h_XTou3bFQrZ4JUgHDPZdBDaTVkPAxalp9waXzT0xoB3CacwpV2XNSQZ9UJqS_azxz7pVDSw7z6R7PjF8EzwuJ7nFK2dUVvsaHbw0SJ7fUA62T08kmED4XHITlmySChw9bx4dVGtWbW_rn6i_jXeq0K91NQhAf6giXZrj9OJ5v-EOqJY4MSyvuqWoWYWcYm3lnE5I3S1I8hLTMqX1Z413MZhqfmSvDpLYWcsr8TBKFMHr6A3fGsWEHppFmFUnMl0FHsjjg0yDCMPyKnr--Mt8aEVVaUBRl44kdYUmoBF-tJtOlUMlQ1wtcw__jh1vk_LgnKWoWYylSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
آنخل دی‌ماریا: مسی نشون داد که یکی از بهترین‌های تاریخه و تا وقتی که خودش بخواد میتونه همچنان ادامه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102022">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_ita4ixEJYZOJq6yoLCs--evlJZ_dMw23E7cT2kcRVbaeC5U2EtQHUlmSIOkE57bbkwvdBn8wtEaOdkuO2C88fSJHN4AsqTQq2MElKTinqm3R5-AQyWXiwH0eEc-D7DkiX8444cB-0qBTW-PVkxE7w43-FOjgE3RNa33oxn0lAgeBib_FWyRvqp7KgFAtrqiE7VIBCNUUUJqYvTmEe0RG6jPH1kiPGr4JM0c2sDZechUq6IZ9locLS8T_TQ4TlMKQJzXAcbyJ2V0_6cEcXCVfQf5ButoCwHRXB44SGisQqvcHOJvFt2igOvtT55pRdZj4iOXaWdzEnDgn8ueVSAnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚪️
عمق اسکواد رئال مادرید برای فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102022" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102021">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=joDSwv7XweHfsH3poL_bUo1BRbFi8ysrlWRHu8nWMf8E_Sdd0TPrt_NDW-tkqUviEKd3SEzG4a3iEhaugWQid-tYm6560WMLQpUXpAp5clRHJqvQSJTTvTgShs5K3ick14nHYzYWmKp1yBYsktJZ8lZ-Zd906pgp2SpT-J6HLniqH6uuST2bouZbd73E4SQFqO9GYINZBR3aITKOV89UBMQZMIm3bDTI9_NoLjYOAQMSa-ZuWgCfrZ7SLUnGlZpa7QxjxEHvqkl43FpzOs0jItsr4hPrTqX-BL-c62Dc-f1TAQ70m9_wsfdXNwUyvd47Jl_xvIOYGzQ-BzSH57c7KC-GqpSn9n8otiyt60-JC8T44SBQrJVBimRxUpRw18xz9cV3Zt7pMy3LuzfsarNFbqJBkyK3_Z9-U0I8uawpK6xq-d2eSilQSgS_8zWeN1fRQCt_pEaPpUC19khUOEkNjB5z4Fgbchn00xu_T_Q7RiegBxW-2QNJWsnm3f1tgISlgCNt5vOVzcSDQ7z-oI2ssgunDUJkKBvwRlo_HyEhP-B5Ik_Xwt16Mbug5jZ74vRzcUE3Y4DDHcW2skb5wOv4HUy3RuETqLbV6Z7UtfsXjrz1jWX5IfqyoZVbI41zTjqLajYY4YrD4OdAk-VyjFWyQAhgDXxt3Z0XBGWIVG22F2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=joDSwv7XweHfsH3poL_bUo1BRbFi8ysrlWRHu8nWMf8E_Sdd0TPrt_NDW-tkqUviEKd3SEzG4a3iEhaugWQid-tYm6560WMLQpUXpAp5clRHJqvQSJTTvTgShs5K3ick14nHYzYWmKp1yBYsktJZ8lZ-Zd906pgp2SpT-J6HLniqH6uuST2bouZbd73E4SQFqO9GYINZBR3aITKOV89UBMQZMIm3bDTI9_NoLjYOAQMSa-ZuWgCfrZ7SLUnGlZpa7QxjxEHvqkl43FpzOs0jItsr4hPrTqX-BL-c62Dc-f1TAQ70m9_wsfdXNwUyvd47Jl_xvIOYGzQ-BzSH57c7KC-GqpSn9n8otiyt60-JC8T44SBQrJVBimRxUpRw18xz9cV3Zt7pMy3LuzfsarNFbqJBkyK3_Z9-U0I8uawpK6xq-d2eSilQSgS_8zWeN1fRQCt_pEaPpUC19khUOEkNjB5z4Fgbchn00xu_T_Q7RiegBxW-2QNJWsnm3f1tgISlgCNt5vOVzcSDQ7z-oI2ssgunDUJkKBvwRlo_HyEhP-B5Ik_Xwt16Mbug5jZ74vRzcUE3Y4DDHcW2skb5wOv4HUy3RuETqLbV6Z7UtfsXjrz1jWX5IfqyoZVbI41zTjqLajYY4YrD4OdAk-VyjFWyQAhgDXxt3Z0XBGWIVG22F2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
امیرحسین صادقی: وحید مرادی من و فرزاد را در هتل المپیک آشتی داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102021" target="_blank">📅 21:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102020">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZD3ijjJ1aTS24mY_Rygmr4WOXMKvks_TS8LiZB1HPwvMrUGGCAIRcE4dK_LydXoB9vqP9JYK0PHYDsBU-FuYI_DVyy06rQVHvkq4EQmeru2oNqjH_jm9fdWfVVKqiFMgGmiQxT7NW0HDrCBwDd7CuoK1jCHGup2wMGjpWlSMuyryOLj4WzhKrybr3oWdz-jXRD4oqH5MWvgizyh5v4JSg58CbLXZRpb-6j6tZj5ZA4wjMRrNKzuU5YLbTWedS9NUeUOtY543W6Dw5YDJrztmpnnEigaO9wFMGUOPhQEM4WRjA-eBFaqq59CTX_r0apZlS5GEPdqwq4Der2bocmcBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🚨
پژمان جمشیدی که به تجاوز متهم شده بود، در رای نهایی دادگاه از این اتهام تبرئه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102020" target="_blank">📅 20:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102019">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPw1aOMjox-UMnzZshTqh9WMW_7YcLHigq86U-jGYCeJuwmqGBzEhcB8DmhQhMQJAlOZOyRAJSDg7y-6N-zHA5fwa8hm8UVHZTsPljXGilaqkkDPCdXgAovtxUeu1Br3ZqXJqF35bVBG7OZqp7CFvVIw62JuwkvQPF9MYK9zTEQjNDvFguJ1jtVNkvbNAXu2pUrSQfB37nEaUET-TL9BDGRJeYZNsT9kfV9P3pjeseHQD4Uny-MTEcBGFKrlx5tdbWtGNl4P9CDnzNpym1mKUDLuZT9v2YcZALJV0xX1Il3cSgYidJ0PmmbDSrQO5lncA7f4ZtH32PAvVGTCFF4r1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
آرانچا رودریگز: انتظار میرود که یان دیوماندی این هفته به تمرینات رئال مادرید بپیوندد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102019" target="_blank">📅 20:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102018">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHb3DupinzCjKs9RTEj2uFaUU6B86fV0jz-5D2WGqLU7Z1rT6eoGCI-4Dpf-eiaVJeMfRKTQgguYxnZDupNMX_W1Tf9V5l4OAzQBJQbUt6bsiXsNJjAuLHogAZLIFV6vtsSTsfRZqXpGtRU7ZNgskp_u1wolQwJ8W2ly-QcvPGpzMaCVZKgi6Gc0y09BGZA6ogHmK9P9Ui2QLfKFdU7OnLG9EZ-R_JF-NYlIxThsOtPe9iQ1N0Nk103Z9FPhobfkgvtPeu8-FSsdM3IB-8AOJh6p2FgaCWX1p5A24VlDFddhGp2b1YT0Yv9cM7iGkbNkRXJgEhRHD4YBw67eoA_KgtEuY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHb3DupinzCjKs9RTEj2uFaUU6B86fV0jz-5D2WGqLU7Z1rT6eoGCI-4Dpf-eiaVJeMfRKTQgguYxnZDupNMX_W1Tf9V5l4OAzQBJQbUt6bsiXsNJjAuLHogAZLIFV6vtsSTsfRZqXpGtRU7ZNgskp_u1wolQwJ8W2ly-QcvPGpzMaCVZKgi6Gc0y09BGZA6ogHmK9P9Ui2QLfKFdU7OnLG9EZ-R_JF-NYlIxThsOtPe9iQ1N0Nk103Z9FPhobfkgvtPeu8-FSsdM3IB-8AOJh6p2FgaCWX1p5A24VlDFddhGp2b1YT0Yv9cM7iGkbNkRXJgEhRHD4YBw67eoA_KgtEuY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنتا سوپرگل قیچی‌برگردون ببینیم تا روحمون ارضا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102018" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102016">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/disIQeNdOJg7MHZUyC71gJkw-IapSdHKNQA7-rTZTOQQSKu9G_wfZGDAi6uESJvWHxH31-_4k5ZX4uba45v_N6Rhf0txg6ypDf5j6fktDinaXmnBNAFjbqOlSJpfi33GadOBQpfoUPoTVTE2C-DHW7WEJyzZ11YvejWdSCTv6xDUq0xNpVPZrny9kpIIfJ4PbEdcEJpAA17WEjRNAm3_veFOotF16FnABl6fZM4DmFjb88oTNVEF8A3b__TQ5GcuYCHRQK6FWFOr0y8tQuIG5ih7y87D-9wEqho1fOAZn6yCDl67mUZvoj-k7ZOPLrrgWSjCQEaNiA0M0oCPnRiYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZiSM61rNXzVDBm_uDKlBrFmk7_tJl0MRr2HWVR5dT2VzGk5loe0lIPOmJJ1z7q4XJ9cV-2EuzSfSmHXyH-M6B8raGmvoUrRriB3StyCPPy6KSv2DV4SV709MOwyxElcifDwqLF0OYgjRtKGyAoieZWqfeC00ulob5xp2OcFEbhD3yPZFwb7ln73iLe9BI684_DOudqAoxFspmtLAAs6qJyDT1ev6j5Ea1YcNM0nqA4RvUFCoBtHWnMLzjRITedFlV1ONshKhmIFTc5Ct_V07H40OYV7fWcr5E0DplQDf92L5FCi8L333Dbvg8EUc91s_zJKLb0RNJHk6zeIWwdg7CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
لواندوفسکی:
شاید مجبور باشیم ۱۰۰ یا ۲۰۰ سال دیگه صبر کنیم و منتظر بمونیم تا دوباره بازیکنی مثل مسی ببینیم.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102016" target="_blank">📅 19:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102015">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGaumk_K7w6fdIlq76rrHnLn9LhL-UNL70VNkEXLuO0JiK7WGNqjU3uMO07uhSXFb6viZWDVJSjwed1nhy1N_1sAthqQhZyBQjCTnHEm7jpTzLpLgN-W3VpWQEAYg1qfSCX58X1WfrpAsGhl16S_YoASvbIN2k8ngXjidAWTxySq-Sy1IK_KSY-CrBGFQNlIrJWlLqihHv2FcExslHtvcz0SsPR8nhOsrq-StYzJ5ZpcfASgDDtPT9ZjyNgrvCyCf2CSeZxa9wUhhSNYqcMmEAPlG_8LwztaSq3CqznQi7mB54V2EgzBdpfjvpumyNtsGGqBxRVzMJk8WXDZ0twAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
گران‌ترین انتقال‌های تاریخ فوتبال با در نظر گرفتن تورم:
🥇
رونالدو: ۸۰ میلیون پوند → ۲۹۲ میلیون پوند
🥈
ادن هازارد: ۱۵۰ میلیون پوند → ۲۴۵ میلیون پوند
🥉
آلن شیرر: ۱۵ میلیون پوند → ۲۳۸ میلیون پوند
نیکولا آنلکا: ۲۳.۵ میلیون پوند → ۲۲۶ میلیون پوند
فیلیپه کوتینیو: ۱۴۲ میلیون پوند → ۲۱۷ میلیون پوند
پل گاسکوئین: ۵.۵ میلیون پوند → ۱۹۷ میلیون پوند
مارک اوورمارس: ۲۵ میلیون پوند → ۱۹۶ میلیون پوند
گرت بیل: ۸۶ میلیون پوند → ۱۹۲ میلیون پوند
استن کولیمور: ۸.۵ میلیون پوند → ۱۷۹ میلیون پوند
ریو فردیناند: ۳۰ میلیون پوند → ۱۷۵ میلیون پوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102015" target="_blank">📅 19:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102014">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=qGdI5Tc5W7dCEEp78-c4_BH9LiLoqcflXId0tLsRI0mGwAKmwcKctEbmKcsj53B5svpWCxxie_PzhmRapNza5eox99AxxWyIDIUVt1GQzPevtdhRaG7a-mrDZI3d_7cuEzC7niE2LNG_MWGxWCC_ZiGU0aoEcidTCwAoMN1g0cep0ngGSJJP1PEW9-yg9pen0cgjvw2IWEIp2KA7rZO9_4F01ryLmUglevmknJ2y2M6cZKG8W9ehTeIQ0nPwI7vHLPtKEi33EjYHXFcFSPbjR6Tk3dSPv94Is32WQIiUrUvrYUhBM02hRouxT25-TD7w073jZdKM4YR3rVidj-fbAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=qGdI5Tc5W7dCEEp78-c4_BH9LiLoqcflXId0tLsRI0mGwAKmwcKctEbmKcsj53B5svpWCxxie_PzhmRapNza5eox99AxxWyIDIUVt1GQzPevtdhRaG7a-mrDZI3d_7cuEzC7niE2LNG_MWGxWCC_ZiGU0aoEcidTCwAoMN1g0cep0ngGSJJP1PEW9-yg9pen0cgjvw2IWEIp2KA7rZO9_4F01ryLmUglevmknJ2y2M6cZKG8W9ehTeIQ0nPwI7vHLPtKEi33EjYHXFcFSPbjR6Tk3dSPv94Is32WQIiUrUvrYUhBM02hRouxT25-TD7w073jZdKM4YR3rVidj-fbAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الگوت کیه؟
دیومانده: رونالدو
رونالدو یا مسی؟ مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102014" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102013">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=p2E521Q6bfDkh8ypl__vUmRRuKTmWEMPkt3ocBe9Yd9XPnzmkoUhSDwZgrd6GB2tyUSLWelMJZOqa-UKk2zAxqDuY1P61_YQAdTHDFVXpn-NY5GMDWH_6Uc1HiXDMR6NFxejrScEK5UKBGXDqkrSzPduONfS5t2NeUCR7qBcKuoT6RJ1YxiPQgCP6xJzdF8JIyFf6ap2krprvByL8th53QunbVBuFRzr-M46il-FIYhYBuhNqo_-OgwO0h5eFgBC2w-Z2S76EgqBru9a5fhIHLBEAg6Yuyrh-dBnd5xReUIY0R4BzJswD538jqmuyhye_8cWQJCcf5VgPelBAaNPAVtb4iE2nBpKm5jVNye_8DkS00RhyWREM_NrhSMi8hh-Tg6IWx27BcFZSyg5fc6nkK7y8HDuF3xgiS_emn-MIG08eAn0Mk1EASNKYcEgD8RQWtDBbtaqsSRBVX6Oh_efL7mIIRZ-NMKlflzwPuA4-TZ7LBIo0b4EzP_EigRrFpMaJuU9OrC2q05LXeyelR3C9zUhGe8ndce-9HTNVLv4d8jIumqiPbvF6MxE5QCPsJxqnCbDsDB1mPu_XQO5V7CZ3LL_tvSLL4e7TYuhIEzxP8fNMk58TJXx80sLG89xWFrD93oBwnDZpwnhYy9OwKCsMb3IGQBL5nX6IKtqZAAhLmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=p2E521Q6bfDkh8ypl__vUmRRuKTmWEMPkt3ocBe9Yd9XPnzmkoUhSDwZgrd6GB2tyUSLWelMJZOqa-UKk2zAxqDuY1P61_YQAdTHDFVXpn-NY5GMDWH_6Uc1HiXDMR6NFxejrScEK5UKBGXDqkrSzPduONfS5t2NeUCR7qBcKuoT6RJ1YxiPQgCP6xJzdF8JIyFf6ap2krprvByL8th53QunbVBuFRzr-M46il-FIYhYBuhNqo_-OgwO0h5eFgBC2w-Z2S76EgqBru9a5fhIHLBEAg6Yuyrh-dBnd5xReUIY0R4BzJswD538jqmuyhye_8cWQJCcf5VgPelBAaNPAVtb4iE2nBpKm5jVNye_8DkS00RhyWREM_NrhSMi8hh-Tg6IWx27BcFZSyg5fc6nkK7y8HDuF3xgiS_emn-MIG08eAn0Mk1EASNKYcEgD8RQWtDBbtaqsSRBVX6Oh_efL7mIIRZ-NMKlflzwPuA4-TZ7LBIo0b4EzP_EigRrFpMaJuU9OrC2q05LXeyelR3C9zUhGe8ndce-9HTNVLv4d8jIumqiPbvF6MxE5QCPsJxqnCbDsDB1mPu_XQO5V7CZ3LL_tvSLL4e7TYuhIEzxP8fNMk58TJXx80sLG89xWFrD93oBwnDZpwnhYy9OwKCsMb3IGQBL5nX6IKtqZAAhLmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگر قصد دارید سفر اربعین را با اتوبوس راهی مرز شوید، پیدا کردن بلیت را به سپاس بسپارید
🔹
سامانه پایش آنلاین سفر (سپاس) با اتصال به همه درگاه‌های رسمی فروش اینترنتی بلیت اتوبوس امکان مشاهده و مقایسه ظرفیت‌ها را در یک سامانه فراهم کرده است تا سریع‌تر و آسان‌تر بلیت مناسب سفر خود را پیدا کنید.
🔹
از ۲۷ تیر پیش‌فروش بلیت سفرهای اربعین آغاز شده است. برای برنامه‌ریزی آسان‌تر سفر به سامانه سپاس مراجعه کنید:
🔗
sepas.rmto.ir
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102013" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102012">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102012" target="_blank">📅 19:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102011">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCUjXKE_6QSCWDkO5tZ_u1_scJEimc7zdcjulMuLpXlFqhUvxaxyoNiJfFCZob7uJg7qK4LGYIBCAVmpSa3GwpuHnwhzBVCdnHFVYv6F_A5_uiN5ZOG8VrCscwq-QEX330_UiBPKJanuO8AobDNUlSIkVvPDdxakwGYKBRKzIH4rCvL-4KlFvGDxBhpylUJusIfiXacSjiQuskwOmxJExlZmZI_z3bp1iSTpfU6ZMt0WZ6lRYU4KBWXNMKPmn-eQHaYSR-q7u3AUnDAA-akMQfL1ThJyjGMAJbEfqx44FpWYLecCIRXYD8E9rDg1alqiZFN10zrI-U-Xa6t5F1rgog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102011" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102010">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/746abba13b.mp4?token=mqYdcIYIzVyM9bDqsdKHcKy_xjiGNA7B_L5y_PpEEshQsO6F2aB_Gy7aLImwU0QDoXJy00e8DPqtXuLIF9ZgLcjWojmAMebyEWKrp4lN3UdNP33b3i1Ky-tEFBP0tl5DSVJZKdrl5nXxrIIm-Yr6JrTX_oal_YOji5Bn3m1b_U3Ov8iJ9oj0hY40NiS3nL7ZY8922BnY4k2HRnKlZz1eJbx2koxerZ9hYF2w7YGakhhk6MKWvH7bSTt6fwrldsVnfao0lDmARpmLRLvOJqOa8RhXKrrNdBWEJq1NWalGar5YsSeYTCnJ7OfbRcSUhsnWFtsroakwfH1f-TeAlGXY0kGiVdNHGYr_uHyUkfN0VmJtZSa-3ZdZ2bcvNilky1kx-pWIPxMjkan_Zd_KI3A58bBcwZxWZ9P8oK7QjcDp82-s5b_j1mnd4MOrGtnaXbzYV6FCZOj-E3eavlnkovqOV0apEquP-2t5XAmBErCB2VzeV2eH8lGCeWym3oGjVpb2d0X02sspiA_1xwaypu50f_s66BAb2cuEHWqcI-1v9ra1qqv310j8DJfwdfDdMGS0IEXX0S5KrXjGCzJve3xa31LPKajVab5wNtFXdYJ0sCJL9zzEAcnyETcWMrxw6LyMs6X5OHhhnWJmJ-OisZy1M73sWzMMO78T7FLdFA50Z5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/746abba13b.mp4?token=mqYdcIYIzVyM9bDqsdKHcKy_xjiGNA7B_L5y_PpEEshQsO6F2aB_Gy7aLImwU0QDoXJy00e8DPqtXuLIF9ZgLcjWojmAMebyEWKrp4lN3UdNP33b3i1Ky-tEFBP0tl5DSVJZKdrl5nXxrIIm-Yr6JrTX_oal_YOji5Bn3m1b_U3Ov8iJ9oj0hY40NiS3nL7ZY8922BnY4k2HRnKlZz1eJbx2koxerZ9hYF2w7YGakhhk6MKWvH7bSTt6fwrldsVnfao0lDmARpmLRLvOJqOa8RhXKrrNdBWEJq1NWalGar5YsSeYTCnJ7OfbRcSUhsnWFtsroakwfH1f-TeAlGXY0kGiVdNHGYr_uHyUkfN0VmJtZSa-3ZdZ2bcvNilky1kx-pWIPxMjkan_Zd_KI3A58bBcwZxWZ9P8oK7QjcDp82-s5b_j1mnd4MOrGtnaXbzYV6FCZOj-E3eavlnkovqOV0apEquP-2t5XAmBErCB2VzeV2eH8lGCeWym3oGjVpb2d0X02sspiA_1xwaypu50f_s66BAb2cuEHWqcI-1v9ra1qqv310j8DJfwdfDdMGS0IEXX0S5KrXjGCzJve3xa31LPKajVab5wNtFXdYJ0sCJL9zzEAcnyETcWMrxw6LyMs6X5OHhhnWJmJ-OisZy1M73sWzMMO78T7FLdFA50Z5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی فوتبال تبدیل به یک فیلم و اثر هنری میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102010" target="_blank">📅 19:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102009">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIJgcZvLa0gMwKEiZAkvr1tMRnw1Ltcr_u4hwmDGtYL65hCHatdAshi1vS5X4ttHwW4I7nkuPZ2wMR6VDipfn3x-S4F-Ynv3Sp4O3WJbHCclm_7_VFXuCa8AQENUmSOSHqH8IILfBh5bGveaa1E6ItjE1iNhRQo-9M-9k-fKjsqEC7qO0UlPEKn1gihBHdOq7X91s-LJ77QEw68WvWfdjTui3aZw3XVMcz0YIdoIgDC7bKddCXUX_OAxvGoOBdNLlupsQD2Ervj9FScK4eBO2UDJZJId9lxTB1xndfXX5sOvS0gr0L0QGFKbMn-HGV_YDcEu1F83iZPXCTaMvRhCyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
اشرف بن عیاد:
کار تمامه، مدیرای بارسا متوجه شدن که موضع اتلتیکو برای فروش آلوارز تغییر نمیکنه و نمیفروشنش، حالا بارسا منتظر واکنش آلوارزه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102009" target="_blank">📅 18:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102007">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZY2DMqis11xS3DKmeVF67eeAO8YO0jaYLXa2MdWVaGfL0bF10-KOV2zFWnKBlKZ4CzWCLWyMSR9ex2uU2jh8_7n1gibvkzqNBo5wc0cwmLwiPuTduPeaX2MmM-y-F5Eecv32RvZV_TJpVf4dIECdEgiw3dZGg2_H3hYh8eHq7XS58pHUcv2WhN4krxIi51RuM73TUe-fI8olG10VypwrmIlbX3xQHT0Ls8GRFMeL83XGQI6LuTzP-FeT5JE4JnhNObmUj22X2H45h67dI-unhuc5fKvTE8nDKNVCTnb_Z3pXpeTbhK4awVJMnvqhqoyXwUGeAqca86u8abDcSKx1fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EmLDLWxdx3JUdOAHxkMkVAzYi699Q-Gsvi2-FAIaL9Bmc5dsNj5-RlSG5Rim8cAO5kKO4UzOQ-EcgW3auMuuW8O_P76f8QyFyU18u7CXdeyqOQHiciCtlrNpw5kip88Fnc0_Sa9vxwryd2pmluw146fLZDIcVVDrbBUa_eKa76nSi6ZkuB2QOowfIc0x3mQPJm5pF6QP54FOWejghV1loT5ll2CPhG7e7nmtkNCLaySSjD2tiodMhCdZNnmNxyOi10s4LHGg-zmL-rxFH8R3_ql-nf_mR3G7tVTpVFMwAZYQHLLy0spljlKl0hSlAcr6HGJhC9WggLBUwvKQGPBCGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تاریخچه رابطه‌‌های وینیسیوس جونیور:
• 2021 —
🇧🇷
ماریا جولیا مازالی
• 2022 —
🇪🇸
اِستر اکسپوزیتو
• 2023 —
🇧🇷
لورنا ماریا
• 2024 —
🇧🇷
جولیا رودریگز
• 2025 —
🇧🇷
ویرجینیا فونسکا
• 2026 —
🇧🇷
ویرجینیا فونسکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102007" target="_blank">📅 18:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102006">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=Jo6T3pe_RQQjMtQ7JzYwwhHuJH6cpbJd97DHtsrXu8q6ADjkdI6sZLrFDyZv9CnKsXCDyKosXrYDjqSM1s4wYgcpIuu2iVi37pRbR58638_OhRMT-sQZiSTZ6fCZ597iNQs6xmaaO3A7e2vfXsrXDy8P1p_NFkXOOEPMXvLvrAykiN8vVbT4L5dxm2kZQTNDv8n9At6oEwD9ZKEV-Wqj2WCTUMs0dT_ApYG1I3ZO1yFHa6nXjQ3HCrqzUtyyxiFUGWyT1gHqWHfuHvSrqr4VEEncpOV0K4hlOncdvTjMarlxjhozjEoiW8YYUhU5LLw6tOoviFdielOJSgNjF_Ha2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=Jo6T3pe_RQQjMtQ7JzYwwhHuJH6cpbJd97DHtsrXu8q6ADjkdI6sZLrFDyZv9CnKsXCDyKosXrYDjqSM1s4wYgcpIuu2iVi37pRbR58638_OhRMT-sQZiSTZ6fCZ597iNQs6xmaaO3A7e2vfXsrXDy8P1p_NFkXOOEPMXvLvrAykiN8vVbT4L5dxm2kZQTNDv8n9At6oEwD9ZKEV-Wqj2WCTUMs0dT_ApYG1I3ZO1yFHa6nXjQ3HCrqzUtyyxiFUGWyT1gHqWHfuHvSrqr4VEEncpOV0K4hlOncdvTjMarlxjhozjEoiW8YYUhU5LLw6tOoviFdielOJSgNjF_Ha2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خشونت بی‌سابقه در لیگ‌فوتسال بانوان برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102006" target="_blank">📅 18:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102005">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLZEjrbjYXDs65sHL-Vq5gNHATZwsOorviY5zUBz621DL_sFspkemVCl87P2RBGP0kdSzr-izNSfUsrINA_NV81LaLLwDVVRugT2_SCpBhjPmSF6Zzsqh3GkbjxAR3O2QRoLIL_xMfCpCsCUFMyA-kyoobPgxBmuoPVAy70U7Z2VMo8PKVm8Rk448Tw2Q1LQWkXBsKRRnxLnJHqGTpZCJsOfx76g9Ap_4foUj4qBn8KjaQu0-PULisEWOyJ8u4yy2QsRARsgBjRs7h9Is-hpjUTAU4tygVCdwbDn9RJHwaLNfy5JuOisAbLtqIwQ5y0HonT6FH19Y6aiJbl0tUjsOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🇪🇸
رقبای احتمالی رئال‌مادرید در سید یک UCL که با دو تیم از این تیم‌های در تصویر بازی میکنه
🇮🇹
اینتر
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🇩🇪
بایرن‌مونیخ
🇫🇷
پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102005" target="_blank">📅 17:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102004">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iw6A3W5ftWWNPz0w47eaJqUR05u71KxD8-FJSyOcxOzK-K_uq-aEtica3m_vclMXzJ7USRv5cS-71n27pWdAACFajSDh_8FIHgt0r655zFjZhs1iAlb_NBHKffFfzIE19Zc7N3Smk05vVQ-bszcQSs3qOGf3OcMt3U9NbTSZGHN-epDpYMFJiE0tPU082ygwkGnhdZq7DPIn5eHV431GljCc3AlilyU9cj0MaBJFOfCTx-fjA90z0U_1wHr4jjlU9Jn8NyhkYtvgBUNe105X-Oax273MEC-zWOU94x7j126PYvxKXk7UGwF68KJn_LCkuewcyk9GD7SYLmn2aPmNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
متئو مورتو:
فولام قصد دارد یک پیشنهاد بزرگ به رئال مادرید برای جذب گونزالو گارسیا ارائه دهد. آربلوا می‌خواهد او را به تیم خود بیاورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102004" target="_blank">📅 17:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102003">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmNT9Hn7o_yCZrqnFxvXqhteA92zCHf5r13mndhaBkC_y-xqbuuKVbkrVWSzd4K-ivt2Tl9IvqjxNXJbmpX4C14yrQdxPley-9hp7xZ0Ps0BUy-XkP0Y-gqdguuhtyHSX5vq1LvG4cX13x3pDBcfXnBZGZZ4YGQ-cmP5P4gjmJ1SuF6Le45XUeX2QZXgCfjmj6qYZobw5G3YND4XUFaWONHoWGXeH1cylAiUQCH4uWYJhXZo6kCnzZ9hdFNBiYNm7i1GfQhPtgVxFC5YYQaGASF0ozNwr9ttCj0m6qsRvpApFKBYsk_GzXeptE1uJn7RLMNXXgv_WVdxnYD4jo_WYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سانتی اونا:
باشگاه الریان قطر پیشنهاد خود برای جذب جیدون سانچو ارائه کرد
باشگاه قطری در تلاش است تا وینگر انگلیسی را متقاعد کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102003" target="_blank">📅 17:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102001">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🏅
فوری؛ لینک پخش زنده بازی پرسپولیس و پیرامیدز مصر گذاشته شد
💬
@squadify_ir</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102001" target="_blank">📅 17:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102000">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=PwvMlyTbG4qQObJus6uOcEQEvAOlOSmpPSQejVr6MF6j5YMDbyakY6_KAacFBUEoFTp495UfFOqe6u0Y2Za6_zj4z0OB-tugPiNfipKlqzPAmenPLHBoplHiLa9VeGP6phPQnGOd_Bxwl9uqPCh57vxURR-W9XUY4QMV-kBxanL-aczNzmlbQDRu-ZTI6wlKW15rbJbJOMXfH0Eam5uVygDkQfbHjIWIaSXThzYq7p3_fviRCEPeWfNgbDqYGHDKUO3k8_Sc0tsoaPWK3DwT7v7FRDG39TxCB1MFmd1xtOrgxCWWkXIeJEE4zOcJw-mebo9UHCcIHP17OYWtV2UZ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=PwvMlyTbG4qQObJus6uOcEQEvAOlOSmpPSQejVr6MF6j5YMDbyakY6_KAacFBUEoFTp495UfFOqe6u0Y2Za6_zj4z0OB-tugPiNfipKlqzPAmenPLHBoplHiLa9VeGP6phPQnGOd_Bxwl9uqPCh57vxURR-W9XUY4QMV-kBxanL-aczNzmlbQDRu-ZTI6wlKW15rbJbJOMXfH0Eam5uVygDkQfbHjIWIaSXThzYq7p3_fviRCEPeWfNgbDqYGHDKUO3k8_Sc0tsoaPWK3DwT7v7FRDG39TxCB1MFmd1xtOrgxCWWkXIeJEE4zOcJw-mebo9UHCcIHP17OYWtV2UZ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
آنتونی جاشوا، قهرمان سابق بوکس سنگین وزن جهان، از آهنگ سیاوش قمیشی برای آهنگ ورود خودش استفاده کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102000" target="_blank">📅 17:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101999">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=ZLZO28Dh3zeU9draEWyYp1uZJPykZJrJVRu045gh6ghKeErjQHmNf4f0dvLJS2kbHBXR9Pj7i_FuFZ7LLnWkdGXQzz7WY-FUF8II6GxVEI4afFhBhjk5qWkbT-LrXVz7G-s5e0M_e5VyATrnqz31jy-yb1jPNS-Xkfx9UX1UQfZ8LKPzGN4GxR-8fZGm_YLJcF_-Cv3M-1QR6_790x0Tm40wiP3-F4_9U2vhtY3UjPcSG5DbeDAdl6Y6-zw54uPgcj5-7n6_f12ep_5FO1cluierFyWs2ojUaWw_FFdFlj5RxjlTNmS9YtDb0YxXKLiK9PSW76LlWL6LzwIv2qa5kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=ZLZO28Dh3zeU9draEWyYp1uZJPykZJrJVRu045gh6ghKeErjQHmNf4f0dvLJS2kbHBXR9Pj7i_FuFZ7LLnWkdGXQzz7WY-FUF8II6GxVEI4afFhBhjk5qWkbT-LrXVz7G-s5e0M_e5VyATrnqz31jy-yb1jPNS-Xkfx9UX1UQfZ8LKPzGN4GxR-8fZGm_YLJcF_-Cv3M-1QR6_790x0Tm40wiP3-F4_9U2vhtY3UjPcSG5DbeDAdl6Y6-zw54uPgcj5-7n6_f12ep_5FO1cluierFyWs2ojUaWw_FFdFlj5RxjlTNmS9YtDb0YxXKLiK9PSW76LlWL6LzwIv2qa5kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
قلنج‌گیر معروف ایرانی که با درودافای مملکت ویدیو میگرفت توسط پلیس بازداشت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101999" target="_blank">📅 16:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101998">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=a5vx3SOS8krd1wca2a6p6iqRz_orx78s99w_4V-XMxypEiul96mkv4hkteMFze2IEZyM5LwnMR70kJjyCE8uyMf_uW_lVoCsMqUfYcYELHq4XMrWnX8UYA7pGmk-mXmevYCftIZt_4B-rkrVquBFsvfSxpChGMy7tm9IiDa6R6FrAkFwj3lqbCA31wAgI32mDi4y6pwVQ3HoOzR-LSqu8x1M5OJPQvXjCQEJcZ01pRx-tOigaSIMpP6lMDUmD7dv9NyZ7tn3LoKtQpcnkApGmWUfiqdbOPFDKGpn57xMuuIiPcH-dGyW5eEr1uTHOjDyofsp7Zj8d6fgYfEPVA5ZlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=a5vx3SOS8krd1wca2a6p6iqRz_orx78s99w_4V-XMxypEiul96mkv4hkteMFze2IEZyM5LwnMR70kJjyCE8uyMf_uW_lVoCsMqUfYcYELHq4XMrWnX8UYA7pGmk-mXmevYCftIZt_4B-rkrVquBFsvfSxpChGMy7tm9IiDa6R6FrAkFwj3lqbCA31wAgI32mDi4y6pwVQ3HoOzR-LSqu8x1M5OJPQvXjCQEJcZ01pRx-tOigaSIMpP6lMDUmD7dv9NyZ7tn3LoKtQpcnkApGmWUfiqdbOPFDKGpn57xMuuIiPcH-dGyW5eEr1uTHOjDyofsp7Zj8d6fgYfEPVA5ZlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
اسلحه به دست منتظر آمریکایی‌ها
صداوسیما: مردم بندر جاسک به صورت خودش با اسلحه در ساحل قدم میزنند و در انتظار ورود نیروهای آمریکایی هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101998" target="_blank">📅 16:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101997">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5IIOOZMqGArxmlyddT8b9KFJWSfSMotBFQ4ZyvOzEkC7KZ8a0J6cgjwNJz0dAKftJimRL05lIkroCWDr7FL2WthtyVt9yqGAonA9vPI5l3y5jmQnGQJ_EBOVqIiyJ85RX166CBkuuNrj1U0QwzJuopYLylVs29qHhFmyQU6EtsYNnH0A-XuFQf1uSXIP-cAFD4vyYYfsQTrEZVJFzvPw7TNgJ8PLMndL8jjghiDAgYBU1LQj4frXZY01Etj28hKjMQT09rUChtNiDPrZfKF1a2i8S6ESuWnJyY1n1jTldxeY3i97bcJGcbaYXS_OWW7wYoZaX9kIGa8xzZYtAaruQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنانی که با همسر یا پارتنر هم‌تیمی‌هاشون وارد رابطه شدن:
🇦🇷
مائورو ایکاردی و همسر مکسی لوپز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری و دوست‌دختر وین بریج
🇩🇪
مسوت اوزیل و دوست‌دختر کریستیان لِل
😀
تیبو کورتوا و دوست‌دختر کوین دی‌بروینه
👀
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101997" target="_blank">📅 16:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101996">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=j84v1O1-5UDA9SmmLlr2ESJgYR8G0Gj27Jp60Qd8P2vz7iUm6SvvWnsG1vLHR2Zj2LIWcWvw5pWWpjh_cS8ZygSeLZlwUwC16ocSqpv01f74RxdIEBb6Xpht88O_AsDH6G9HzV7Vm3F_W4PRCkvH0dfcGsOocTSSjs6XTBXcRK9vnzDR4T_hIpvtx5WEv8KeCq1l5Fpa33NsC7OZQ7zZIgw2wDFtAONXareylLAMB2WxSEnPfNvZ_QeZ99RlDkpbA6OQfIm5Nk5f0xT1Ku0s1b4uU-HmuAciPEAYpm56CeXqpZbsxSpGnbODLUo3rwUjPVCx9MXEp6p6SFFBb5_Ukg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=j84v1O1-5UDA9SmmLlr2ESJgYR8G0Gj27Jp60Qd8P2vz7iUm6SvvWnsG1vLHR2Zj2LIWcWvw5pWWpjh_cS8ZygSeLZlwUwC16ocSqpv01f74RxdIEBb6Xpht88O_AsDH6G9HzV7Vm3F_W4PRCkvH0dfcGsOocTSSjs6XTBXcRK9vnzDR4T_hIpvtx5WEv8KeCq1l5Fpa33NsC7OZQ7zZIgw2wDFtAONXareylLAMB2WxSEnPfNvZ_QeZ99RlDkpbA6OQfIm5Nk5f0xT1Ku0s1b4uU-HmuAciPEAYpm56CeXqpZbsxSpGnbODLUo3rwUjPVCx9MXEp6p6SFFBb5_Ukg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
علی علیپور: حتی خود پرتغالی‌ها هم کیروش رو گردن نمی‌گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101996" target="_blank">📅 15:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101995">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4Qi7qBDCosFh9mQDSgLEVG46ZPfLyniBSxV65GvYdqKrYVlZodmwuGgBeTPXiJVCn0ri9EOoi5K-k--esPw92VlU9sc2CiuV_3GDSW5AkPhapy6lUHDnjiASwz54vi72m3gfyjQmt90JLF11ZCpcFBjjkiUtIIJo-VpqohctZjzUzq-apegTfuZ-9YuDYDfscbX4BFPx0b5-6kXtQuKx8y4oJiCyrP0eG7svtAHx1ffWXJ3iXDOZPm60_zlHElIj-n8PlnP3XW6jdjSj2DKzOcojZ3wMN0tUfwPa5RvoMg_kU4jGiPNHlYdE_6goDRFC994heCZnff43_0wB6ItGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📉
می‌دونستید؟ فقط چند هفته قبل از جام جهانی، اینس گارسیا، دوست‌دختر لامین یامال، حدود
۲۵ هزار
فالوور در اینستاگرام داشت. از زمانی که با لامین وارد رابطه شده، تعداد دنبال‌کننده‌هایش به
۴ میلیون نفر
رسیده است. فقط در روز فینال جام جهانی هم حدود
۱.۵ میلیون
فالوور به دست آورد. همین رشد انفجاری باعث شده چندین برند بزرگ برای همکاری تبلیغاتی سراغش بروند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101995" target="_blank">📅 15:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101994">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🔴
فوری از رومانو: لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101994" target="_blank">📅 15:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101993">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZnE2pk8xWfK8kaX1EUhJxXjaFdzzCvaXZhWlo7UrULxUEoPd3XMxlMYXw7DPjqH0yryv1HPIsJY8DTbzJ4eH4VLz8tSZVjIbcFFswFIEW5ngY_44KuS45pz9qkPCPjfiU-V292VaxQL_qqT5yP7WnjONzyJWtqlaH0o_Emtf5Hk-wXGYj__oTVbdq3ufOzBm8r_mFsOvEtSvgsexVmoRFEBi2EW-f-NNIzQqRSwRkV751EQsDG_cZK9aIWD2sY-jI_BQNmxzqxmmEMmV4qoFnRK_Mo8IOiLS-TaHV9-BnqlGWa2PmShTBULP-ruFNiGkBE-dSesgKnLQ3I6k7jLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فوری از رومانو:
لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101993" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101992">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=nOt9HE8_j-dCfA7-t6XFGNN3YqhfReK_0uYWCuGShgrnRSblzaWRlrA0Jb9l_bvyKBJ5i-ssyN14m48gLPjV39O6nCmzW-k5jFcTGGNYFVcR2Zx7qpREGpz-kWE4nh_BdBXpAkdZzhgEzgzrHxcaOg4JwD9fUzLwZ0e4Mew9Ytw1k3nKWKXBbrgVtAGTiizO91b6za0ikzTkL00NRrlJftHn6DsrCt3DaPhfJP6ZDUfSrAjYQ5Oi-KFScQ-X4sb7HZjIMuRE8PxXOhlDKpGkw1XzgCN7C0v2IUJ3UdG-RFjsdfnA3GRJcZMAUUV4mGi5-W7agGLV9RMuyU_LhDjs57aPEVqATYOzz0rFZm4eQV7Viw9fNA8rBCPou3bfTpYDlJu8OaKACQ_O8eUKiY4ptik_Glq2ZcwloTPcDIGJ-cgvimUZDXAarKb3664XR3u5UX2__eeBEFMLwcdTEHM6lYi8JB_tBw0FpC7tBDnefcCGQQ6rX47V1m4e0Ybkk-irXzKzorB76Zk7h4p-R7F3j8T8JMPbC6dmfOMhXVMnQYXE5PO9tAVJWpBgbQkkBSeqDdbaaWa2CpN10NJNOfskIb7ayW5_DPxgyKAypxcsreI0EHeXbsG9G6eG8It2Lg28-xH-MTbQFJye3Wv6buSHGhuBkJ2R064u_qnPUPkP0ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=nOt9HE8_j-dCfA7-t6XFGNN3YqhfReK_0uYWCuGShgrnRSblzaWRlrA0Jb9l_bvyKBJ5i-ssyN14m48gLPjV39O6nCmzW-k5jFcTGGNYFVcR2Zx7qpREGpz-kWE4nh_BdBXpAkdZzhgEzgzrHxcaOg4JwD9fUzLwZ0e4Mew9Ytw1k3nKWKXBbrgVtAGTiizO91b6za0ikzTkL00NRrlJftHn6DsrCt3DaPhfJP6ZDUfSrAjYQ5Oi-KFScQ-X4sb7HZjIMuRE8PxXOhlDKpGkw1XzgCN7C0v2IUJ3UdG-RFjsdfnA3GRJcZMAUUV4mGi5-W7agGLV9RMuyU_LhDjs57aPEVqATYOzz0rFZm4eQV7Viw9fNA8rBCPou3bfTpYDlJu8OaKACQ_O8eUKiY4ptik_Glq2ZcwloTPcDIGJ-cgvimUZDXAarKb3664XR3u5UX2__eeBEFMLwcdTEHM6lYi8JB_tBw0FpC7tBDnefcCGQQ6rX47V1m4e0Ybkk-irXzKzorB76Zk7h4p-R7F3j8T8JMPbC6dmfOMhXVMnQYXE5PO9tAVJWpBgbQkkBSeqDdbaaWa2CpN10NJNOfskIb7ayW5_DPxgyKAypxcsreI0EHeXbsG9G6eG8It2Lg28-xH-MTbQFJye3Wv6buSHGhuBkJ2R064u_qnPUPkP0ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظات خنده‌دار از زنده‌یاد اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101992" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101991">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=dhDF_AZjMEkmJBF61Sl4a2mmCXsIDNSRFoYqWOsqo_MzGAC6jGn4rBeRLfvT-2ko51x96-2-3yamtFk_gR9zZSnz2GRxoQyEnEXuGLZAVB2sKnLeDchdySr6i3dR3eTmZrPlAh6XHOUyp2OctubjF0E0qwmaOvxBcaxNXq2WytJKhTtp3LD6fBbHTNE7tlTFR2B_k5aBzU80t-b_U9CwPgxxIwjlfzpGL58BGdHWhEmqDH4hnO0tDAYBT7B_3M-PhcLgXqn_wzpRxmb-vj6UjQfaHUDV8dzPRbZLqoe9ESjlf1wcOGuoRt42-5wtZmX_9now__7uFkiNMCO10pu0fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=dhDF_AZjMEkmJBF61Sl4a2mmCXsIDNSRFoYqWOsqo_MzGAC6jGn4rBeRLfvT-2ko51x96-2-3yamtFk_gR9zZSnz2GRxoQyEnEXuGLZAVB2sKnLeDchdySr6i3dR3eTmZrPlAh6XHOUyp2OctubjF0E0qwmaOvxBcaxNXq2WytJKhTtp3LD6fBbHTNE7tlTFR2B_k5aBzU80t-b_U9CwPgxxIwjlfzpGL58BGdHWhEmqDH4hnO0tDAYBT7B_3M-PhcLgXqn_wzpRxmb-vj6UjQfaHUDV8dzPRbZLqoe9ESjlf1wcOGuoRt42-5wtZmX_9now__7uFkiNMCO10pu0fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
دستاورد دیگه تیم‌ملی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101991" target="_blank">📅 14:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101989">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BYPsTzv9pUspq4uDdlX-E8GxCDbzLGA8mwUHQLnQ1XsjKSNaReAJoGA3luUtY3d2Q87j7C5qgJARBLnC1ikBka9MEVtr4bcedTI-ckmquimZuBDJIFNQM-jnDSqdT0QqqIaHjVtR30GYcxK5zEoqfkbOZmrc3FM1Jo59dMg7y8CKJIeDOR_n6LTwWi4P20FyB18MP2DciTlRh1YRDAY-pUsErWYFt85unPQvPmO32LJ_zHB8Lp-2LQ7DrRk8UicUluOc_4qzTiopys2QQGrb3eZaFRujIbheQgpF1DiAXTccVFSDrUCYbG_PyynYpKEPereQLAiarHWJaaObAnLE1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGA_jezv4vipmckUzCKPoZPRMIlaggerESym9tsewcirkp-pxL4-YIkkcD2aFl2vNDFniF_owAa9IjRMXSr6NTQlDc5T2tXc7-9tDTcn6cmoy3QRnWBUmsVJ1fKnCjUsm7xUIY5rBboN6UFhoLrRT5FUD3QjnGb7rvBRHwU2zg5A6_njwO0vWdX7QQ-ut9-TMMKGNOmWvIW5hyRXF_pxRpmNz6PWaV5k-j94i382AKiHq4N8Le9JdHPe728ZC4MgGISEMSJKYlN46-nxXTy_oka208JhUzitHbGoiJAJY1nukIcEAOn1h6j8SMWp7ne8-KUdW61kfc2wixO_VfpUBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اینس گارسیا، دوست‌دختر جدید لامین یامال به این موضوع که گفته میشد باعث جدایی او و نیکی نیکول شده، واکنش نشون داد:
من به کسی آسیب نمیزنم، چیزی رو از دست کسی نگرفته‌ام؛ فقط دارم زندگی خودمو میکنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101989" target="_blank">📅 14:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101988">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=Vk-TURdFlcyT6xBa2KWea3FS61zN46UnqoWUCjsHGcxklx605MfFOe3gYUDmYUofdMM6iUnwMRGpTWHhofNrR-Jq4wgmJDgqQO3NeMVMS_XGTiCfWJpwoL83mLulZc9tt1kIY9JP47DR7jUEVo7NTJnrgYu2WeBBfcJnHVUclXoJLTi7g5yqrUW8YJNEjsTOtBUqt6LwjrnVJadICO58TQTe8ty533ZAWlrSZsl3d4Y5wX5AgiEbL_brkKW9hrz8JOlD0Um6hrxI4FGRUHR9NTRP1Dj7L2rXDJNeaJEyB1R9urO3C2e6a7Kcl7ZPiCu0Ik9wfTzZcowdfsmn_YFs_iXSsh34EhL1tXbBhbrnNurC-HYKYisSHp74gWZrx61ownx1q2iuFkA6bCmyFhpZLVtG8WwzUOUEK2pJybQckNuWvFpLnXCQDjsiaEvOYGnwdKXfEzdVpBW4myys7n9zWGiQI9B8BMO4M-xY5OoqCV7f-PGiuVbfmpZNdGSd2M-GHjGKtVE0irvpJcwUPhWnVFNiUypShy5rRvjll7K3hAelVL5HB5PcOK2VVrZH7w4fdaQqgUGztM8HdILr19mkGKpXIT37M7M1IuciDzD0nO2unX8tPy4R_VTLuFMUDu0mHLs_RG7s1dZXqNYpkNUe9J3ipcNVv98nmMahuLJmkUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=Vk-TURdFlcyT6xBa2KWea3FS61zN46UnqoWUCjsHGcxklx605MfFOe3gYUDmYUofdMM6iUnwMRGpTWHhofNrR-Jq4wgmJDgqQO3NeMVMS_XGTiCfWJpwoL83mLulZc9tt1kIY9JP47DR7jUEVo7NTJnrgYu2WeBBfcJnHVUclXoJLTi7g5yqrUW8YJNEjsTOtBUqt6LwjrnVJadICO58TQTe8ty533ZAWlrSZsl3d4Y5wX5AgiEbL_brkKW9hrz8JOlD0Um6hrxI4FGRUHR9NTRP1Dj7L2rXDJNeaJEyB1R9urO3C2e6a7Kcl7ZPiCu0Ik9wfTzZcowdfsmn_YFs_iXSsh34EhL1tXbBhbrnNurC-HYKYisSHp74gWZrx61ownx1q2iuFkA6bCmyFhpZLVtG8WwzUOUEK2pJybQckNuWvFpLnXCQDjsiaEvOYGnwdKXfEzdVpBW4myys7n9zWGiQI9B8BMO4M-xY5OoqCV7f-PGiuVbfmpZNdGSd2M-GHjGKtVE0irvpJcwUPhWnVFNiUypShy5rRvjll7K3hAelVL5HB5PcOK2VVrZH7w4fdaQqgUGztM8HdILr19mkGKpXIT37M7M1IuciDzD0nO2unX8tPy4R_VTLuFMUDu0mHLs_RG7s1dZXqNYpkNUe9J3ipcNVv98nmMahuLJmkUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
چنتا سوپرگل نامزد پوشکاش ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101988" target="_blank">📅 14:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101986">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KrHqV0Tg68Un3shsf_WJkWdaM9zgKeJrcGgWQggleuV6pSWHZc4yFHBnSSEIlVAuNawgRCXCRxjb89MkcJhf0qdqdQxDtJ-gLZLNK4E0GISkD-yMmwYgYRxQiwabAPAEOc3kO99VFfa-A76XenDHTfIUGHBf5ZjOtJWAYUXvNrFaSi8ToPOwHMq3uz9fBkprwoGGeM4SQZluWMe03pLWfmsEgJCwsiggBnjYV1gG11W5GznhRnmRJ6JmBEgVu5HgtHHUvaxoUg2F27TpdI8BIZNSbp13Lm_Y1p6MSwUm67urw9ddU5hGJpMkekm466aNl_GFzv1Ytv3F5mgaCfH5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxwVUGi92MftRROd05VyLIuPgGt68TBypncOMKs4DXtoTFIMB7upKD7KfUrpdtisRHmB9J7577LZ1CBpyfKc8glePm3RHCp5F7wu1JGkR08YJx7rHw8MAmrut7q3vcHwnHNpCqIGxPXJlnXvkFSAJ6ysPhlJU_vEnUtM_0sOm4VfehOrXeqmzJ0JLWbqEomNcuAe-JpHl61gwBDvDx3-DftkHvqBX2i0_ABIOr9jw8jfwHM9pk3jz4UEmXltKJGnf5Ewhx-JpimeguXft6VIJesoGd-8jVvCW4uj7AKYcsVFJIYTGV9gJkvRsFEf-Ym2UlkGqGEoUH1PnAD9CawxLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تاریخچه رابطه‌‌های لامین یامال:
• 2022 — سینگل
• 2023 — آلیسا
🇷🇺
• 2024 — الکس پادیلا
🇪🇸
• 2025 — فاطی واسکز
🇪🇸
• 2025 — کلاودیا باول
🇪🇸
• 2025 — نیکی نیکول
🇦🇷
• 2026 — اینس گارسیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101986" target="_blank">📅 13:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101984">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjzplorUJdOOeL3o-seugnWW1WsTP83233W5YuDO2P43MSRE_n1r_r-0tAou42RE2m0KRLtX4N1HPeGF-vMls6RBP_qETS_nrpJ0lTqbtTdQOlEjYNE086Gbsfs5zzmd_ylaG3MqPIvSR9hXC6xoD7XDf9a4d6QgvRYNb5vqIENEJV3BQzg9gx2QoO5GyoeRgr2CXyToIWy5kWZqG5wFyyiVgCv_qrEUbrBwFQdPPhLqBJRFgfl0eZ6YLhybA5PM8hh2eR0D1a6VnDTRcyPKqkta7wniK1zx-dhqIyzSKZmtWrs3xN8daN_YARHyq7JQYk5M4eTNnKKfjBZTkgGFGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bc7wSSPBA84s58pP7DzXuRP8I3Sz2ZxDT2MHkIJOKZ86iz-w-ehvrGafZkzBnh9blPgNkiP1R7sZl19pslTnm7gJ6HbiqCPtrzWjaGmWYBjpj-HVMZ7utOJhTv40jEv56ha-XRSz6itG_6X7vGrd8CBEOH2cmA2Y8JFpPe87aHqICNd7mTArJN19fRH3ieUAKwdWLjnhQdcQ-9mAMz0GBc1M-WYcX5vuS4FPfrMB0ZftxYbYfbKfP_3kWQkWZuuIIPgNzVsgKwGMMETCf7kW6Yz0YvG989yG4-0COKlE3MKlItIites_USMgxo_ownuK1zmn3OCvzldgXQ5h4d1RKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
جسیکا توگا دوست‌دختر سابق وینیسیوس جونیور:
این فوتبالیست‌های سیاه‌پوست فقط از نژادپرستی شکایت میکنن ولی همیشه با زنان سفیدپوست و بلوند وارد رابطه میشن. اونا هیچ‌وقت با یک زن سیاه‌پوست وارد رابطه نمیشن یا چنین رابطه‌ای رو علنی نمیکنن دلیلش چیه؟ جوابش واضح و مشخصه! خواهشا این سیاه‌پوستا فاز آدمای اخلاق‌مدار رو برندارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101984" target="_blank">📅 13:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101983">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101983" target="_blank">📅 13:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101982">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAOuHZltIMtVA6DTPkt-8ZD2tRRQoFLiBaKtGCRBLw-_uCZb7OYhaGgTV9Ujprgvm3nWx5XCSLs3crL8Jmbn1GNK3Bz8kpnNz906P6ZK7Is9gekkpsBRfwpx3n5damlz0Eg4BOMYI1PZrV3STx2SkxDpvhAOTwrlofmviVaaVE7lnVbricJG5P1Vn4K-M2fZje2pG7jA5gmabCbaJJ_FVXPNpudeunFqWN2YxMoLvSgfva97DnQdbZ0kTaAWP4IHXEAs9h-6TEvH10-DVYfBmjZ3ITX0-qdRnoImR_24PMzRvpHpSF7sB7J061u8m67kGJO6fmSv4X6JGpAh_HXIwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
په‌په‌آلوارز: دیومانده به رئال‌مادرید تا 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101982" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101980">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBQM_RB5nafEv0I2pJAPXoOPL8dVxJk1nifr7vTP5G7FaEOVkBsiQpGKu-_JjAKZOawdPGDyUjLTSuFYM8W5ByNIaTSkoWCi4FrXq7tqhZSnA93i7qd8oElu7th3X0gHf1C-6ZTfh7DYcfZWGJ_5dldTl008WhqN5ZSFqeUYnyGRgurKrfnS33e7bnqL0yD7vSlYx2eVeRFxulRsQzUIQ8jhFXAvsrHu85kLluz_K8PI-utsoEoVdHo_bZBS_OeUp8GLUNoUPbT1AI9BsMnRwyrNygBm6iNSVkQVJ4ZVHiKJnNeiyKl-92Zc0u5dF5s-8bEofXWMwWGfw-TugS3eHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNdTpot5dGu1FiNNte5DExtkKbo42g5dYqaJFf4C7Zt_qYgUkPsh-EEvXn4GsKJDQsyXGam6kRznJXereuf5plsLvDYxOXHj4D9fbWiQzPedw6ZiAY1yuW8RB0vewjzFjXrEjenVx9RWCRjq8cb_G5LLh5wDmneP6BVRtl4y9mqCnfVY53Aix2hWpmXncWNa8aMt9Jr7ZusceugIEC4nd-jMqlVrNHbrg_4so6MMvXab3Ju3UDpYmKaKyB5BKiKYhpYv4KK5sB6hQXH4hsOg6EchIE1G1c9bZwfaq9CKU58ECrQi4CqGe0t6lAjJ4rHLMvBBk3E6mFrcAsbua96uOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📅
🔵
17 سال پیش توی همچین روزی بارسلونا 46 میلیون یورو + اتوئو رو به اینتر داد تا زلاتان رو از اینتر جذب کنه.
🔵
🔺
فصل بعد اینتر تونست با حضور اتوئو یکی از موفق ترین فصلای فوتبالی تاریخشو رقم بزنه:
🏆
سری‌آ
🏆
لیگ قهرمانان اروپا
🏆
کوپا ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101980" target="_blank">📅 13:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101978">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kSkq9zQX0ZyxzLCuhksDYRDMFDBU757KPe2yyDx5pzFhGHJWY7ccHTxkUvoSMtVz4iijCd_LkglsS9nTWn5ctsnC4wWEa6Fx07bMRzA5GfQ55KGpj558P2Bss__qFPD3IQeGIHfXhufvhn31V83iw-UpLubZ6wwxlyUOjOlP3TstoJEWyrKuKByYJKOf5Mi5lMuodLxjysRCmazLixiGIOF7oecTVohJlFo6HPWqzVohpWuqiZVcCOiKxaOSjh-HhWe3EOpgiiwTsCR0cqg_Eq_DOxUdveJrWQVp4AGbP8IkvuHpCWLuiVmExjIvc0wQOnvMNh3abWjWC9DDW3e3QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jgHkD96SGCq1GmoII89hjnU3PgJ8R0d8HLcZuEolXH89bTBDuH30dsOPp_fF0vqqhfT6zNb0D_iYTFA6M0Bv0qJkjGNaItkwP2tHEr68Fgqnq4YUfvmZhVWMY-nnEhHhfihEz3pJERkg9NfepItfAsrnsf2nTCpJHi4RfvYY6OIUOa1zQqgT87SzY4dlpNeRJ0sQZ-sclcK67zm-ERMIEui4PGMcwLzajo3-W6co_1ps9zSLvqJ6HkQ5jWz7oxyAU0F6FzNd6fEIHTSQzaoc0FBTvxv0K0XiqL__v2Cwt8V3nI2veLP9YXm6HJcm6HVUCFITGxLhjK8UiUjVQx_piw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
الساندرو نستا درباره غیبت ایتالیا در سه جام جهانی متوالی:
باورنکردنیه! پسرم تقریبا ۱۸ سالشه و هیچ‌وقت ندیده ایتالیا توی جام جهانی بازی کنه. وقتی بهش میگم ما واقعا جام جهانی رو بردیم، تقریبا باورش نمیشه. میگه: واقعا؟ برای نسل بچه‌های امروز، دیدن ایتالیا در جام جهانی انگار داستانی از یک دوران خیلی دور و گذشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101978" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101977">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkGKseUSxhFqmYNQA01vJ9mcQJ1kk3ZfnwreeXbCaH97IPhumm4iZVSTuIOMCHbgwhl1Dfl_84abE1514VPIb6MXagXLz7H2kH_Y5fKjPydhXIIELpl9o34dZH521TiPQaBJyJb6HXNP7bUALlaO4kxtX-Q1JxpkukJu5_VvFWE-SFE5SpfbE4pnycSUmrU3KGjS6FgzLFJB0iKBJbwxFIxL6EFOBjl9ts8rLvqpxoATaOxTqdzHlqRGio-MFJyEYIrjugUI0ZilWCJZ1RudvKN5QcHeVal839iRskiIHJILsl0jbV9mvrsEI4qbkyHsJAdrySTyLJZW_BPoW8yudA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
ترکیب آرسنال اگه همه شایعات نقل و انتقالاتی به واقعیت تبدیل بشن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101977" target="_blank">📅 12:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101976">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKgkDaKvEYeRHrCTmvFXpUUakjUge5VkcxevSTvVoZmvYJTgCb9Bu7Hs2XpN3UKldu5TTYfHRuhM4bjpmVl4hZ_zwpHKmGMm6JHNw8pjmb60iMdQU2WrNkFFgvOuNFHNLmlUceuPxiiOJ6S8bc-8yNDqCGbS_qD51uFRvRPWRLIEIJkVv_qFSw9JbksFDCg5jIgz8h6viISWVgoW-vkt8rz1kbBidI1vY3VE1SAWXwPMaoStR9NnI6yOz68ulG8xTQbJT4s-Q4kQ0UJXHg9G49HVLEGQdK2R6WI4vs92pMaR4smSpwsnqk1Rn0c-fAki2m0M8AQf_g6S8WlxsGKp7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
طبق گزارش‌ها، بدهی‌های النصر عربستان به حدود ۱ میلیارد دلار نزدیک شده و همین موضوع توانایی این باشگاه برای جذب بازیکنان جدید را محدود کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101976" target="_blank">📅 12:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101975">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=Y5KRVWIc7WuvC9m4Ntx2ZvRxiHH_mn64FL1f4e97ABtsplSTDgFeFhvsCmbkn15jQWILfBo3ev-udInUyzO8Wumnd5eEKH98SMu_S_AWAF2WU2iS4xuEQo8JfDbtxMf8jsvZod3rmJP0hbL2pIbIcREzXnboEzdLEpYBQ5lfmMywfdEXtfaKuK7YWyGfSn6Qkk3PsnCaOmd8F5ItOwTJNPC9Edv7t_HkdfKC2raCn04uATfW-jFqcxiItkD8iHFrY5X7UqCmt25LNlsDTRwl_Zn9FmFFULiYgrXpXTuwAAYT8mT0Jkz6jiTcWuHSVoDOYBwca0guHBOguEtr0zRAGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ddfc2f853.mp4?token=Y5KRVWIc7WuvC9m4Ntx2ZvRxiHH_mn64FL1f4e97ABtsplSTDgFeFhvsCmbkn15jQWILfBo3ev-udInUyzO8Wumnd5eEKH98SMu_S_AWAF2WU2iS4xuEQo8JfDbtxMf8jsvZod3rmJP0hbL2pIbIcREzXnboEzdLEpYBQ5lfmMywfdEXtfaKuK7YWyGfSn6Qkk3PsnCaOmd8F5ItOwTJNPC9Edv7t_HkdfKC2raCn04uATfW-jFqcxiItkD8iHFrY5X7UqCmt25LNlsDTRwl_Zn9FmFFULiYgrXpXTuwAAYT8mT0Jkz6jiTcWuHSVoDOYBwca0guHBOguEtr0zRAGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خارکسده جزیره برا ایرانه
✔️
خارک و سه‌جزیره برا ایرانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/101975" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101974">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2mV_9QhXFdwEIgJfAzZioqbZuKQnR7Toukn0PHXzEEtc2HivFbLh8acj7BMYkpfWMf9Ttuv1tLUxIKGlnw2EmXlP3jEXs8AE27gouimJ-rC0b5v-W3HScL4NGSRumcrG4YVvolKG2YOZ_xNhadMwXCSBHjbki6cC-Ly2rSh7cUUPusLA0HMLNZa5U-QJC86Ui092hAgbCBz7OA5_3jnhKi4UF-C7iTwYLoII7CgJiUXtMvjwkZIOCBT8hNz5Fcbf8nDOt7f38uJPAmtI8cjUv2FHyirlIUsve8LkAhfKkMShJSVZqDIxfsGREFvqfr7vpXcf47QqeJluDPXEZGj-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انزو و خانواده تو تعطیلات
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101974" target="_blank">📅 11:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101973">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5mFhazAFIoAaRIKDZmpZO7Dx67wfOHZuzSBsjRik35SukiUiaQPdReb5qattFc1QrCdtLj6XGJAzdfWwEpql08VGmd4jRVo4vVjCUnHuEgltEvaRLRRjOlDfqYNHar3_GQcgwujOsMzdNJm918wpQRvAxTbvDYnZczwOFOE5oN35o22s_dqqsXAb1fIGr0ruhjOiyGahrBwti8tYz27kURk-K_5C7QQFK8q8ojtTpd8C4B_zbJJrlIYdxCtQLMluf68_sLnYaK7Abhbv3IXt2qZtLhuRzS1pq-5ww25EIR3nmds7BJ3n8zgoWl-_qoT0zIzFrbR_GbCiD4rS3aNSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
‼️
مانوئل نویر:
🔺
هرگز آن لحظه را فراموش نمی‌کنم. مسی بواتنگ رو رد کرد و درست جلوی من گل زد.
🔺
بعد از مسابقه، بواتنگ شوکه شده بود و گواردیولا به او گفت: «احساس گناه نکن، این کاری است که مسی با همه می‌کند.» سپس به ما گفت: «حتی اگر صد سال هم مربیگری کنم، دیگر هرگز مربی بازیکنی مثل او نخواهم شد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101973" target="_blank">📅 11:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101972">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=cU4tjWjEOP9nYHhadH_GC-t639k9cW2i3v-6l-lefo6elj9vewCguaiiDaKINji4IHPJgintsCwDLM7sY8Hl1NmIuiZe-njSqFbIdvgx-BmuMctE46D4YE80Gicf8zy_DfY6di60cgLI5-JfCWAPxnW65o90pHB_YMCpsKScSfEPz5XZfyxtU6IKL_VZuIYBaY9IK47O6ZzYLK4rf_g8NYQNTy5W3JU43hAKEo01td-UWG8HwGk9Z0SKfV_1W4kvimPMU_4ian0z0M_msAe4bZHmU5osBu2onqAYpWVLJ47oF5CGkK4ou7xBvpP5RrwRuT62WRDQy2mZxRhDX_iVng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c941f7e49.mp4?token=cU4tjWjEOP9nYHhadH_GC-t639k9cW2i3v-6l-lefo6elj9vewCguaiiDaKINji4IHPJgintsCwDLM7sY8Hl1NmIuiZe-njSqFbIdvgx-BmuMctE46D4YE80Gicf8zy_DfY6di60cgLI5-JfCWAPxnW65o90pHB_YMCpsKScSfEPz5XZfyxtU6IKL_VZuIYBaY9IK47O6ZzYLK4rf_g8NYQNTy5W3JU43hAKEo01td-UWG8HwGk9Z0SKfV_1W4kvimPMU_4ian0z0M_msAe4bZHmU5osBu2onqAYpWVLJ47oF5CGkK4ou7xBvpP5RrwRuT62WRDQy2mZxRhDX_iVng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیوزلندیا اینطوری از بازیکنای تاتنهام استقبال کردن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101972" target="_blank">📅 10:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101970">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1zsV6dOA0_1q27bgTyJpKx28ZEnhtfXsuPwi6eaM7FNox1jlRMQBcTStkrYDXyytHD8GRIo0sZf7barOWvFn2HhgDamhhvfcPo4vj3zTqO9BBYBpUNfy4oE8-fZ0suhe3pSlwjuNbv-X37-fefh9WSesQjVa2ivTSg_Sz169tF1p9RM4-Qw3rUq3O8buxND0wmDDyEfpYA_04YL4xljdCjQ6T2ItZY0IyvlXprz2SDLjYvRaAlfGae3YVQRLChPD82BOscKS0rNroFSChT0mXBsX53f5u0U5LaDnzEMU_BINFuWDJfUNGgEifXU-q2llzHjty_Zu5wYXwDEcQDczA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOGjvGu2-HeAYqz0epZ2oNoDYiugMLGodJA5DPqWQJZGyKx0KJjPb_kFvv6Exz9n_uvCeRM0_AjikataL7Vbw84QuBg8ysfRELJkpTIGiPmk3ED0eknp6xsOVgxQ9-fKSJx7XZ4VcCCfFCgt8fmZib8SsoxCxAK2eWEDSpRQI5C60WuRILbNXqJnSHVfGwKRyYFakdSOE-aImjB54tnwV0MTMg9WTVaqcgQyvaFK_Oxu5mW_oCCk8CzI7qG98Gdnqya8wOQjM5Rxt5MvcTrM7DYhyobRTenLt7aa9MBfnox-c-xWQ5OQx4Bp-sFVaqvq4Ps54rECm1oQ5nND93gvqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پدری داره تعطیلاتش رو اینجوری تو اسنپ چت میگذرونه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101970" target="_blank">📅 10:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101968">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2E-SUnUpUfXg4RuO0M__P1j8bp50oJ7urBkqwBdoZwrqiEXfGHUWdIQPK6lbCpFMKni6GSnJcu1Htz1cBZ67AgY8RJgw5DWDpUSXCQJpvAeEtz481KYsa2eIzmp9X95Bx53DOWuKtLDp-5egGkI5xZGekJU3VPrtShvjSa5g-qgLv1V89O0JvLDxx0UX5F33h5gVLkbWgLYTTzhys8imyMiPv0OyeJvZIz40Tc2ESxrN0IXLubd7utV1Zl5hVCBAJQcnqrjQys3tZ9KcCchDPoMo4qNNBsYxT3wdI6wH3tqzcOk7-g97Nek6pt3kxMCwODt2o8faSaA3kseEApbdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Aw3ddObFwt4FBsTEmuTpCQaCROZETRM0rrlf7BOFMUmwmE_cNRyXW3AK_nxQofJOMp5UHeCNgYEvsGUVnScdwVHP4Lpe5gftXySZ1cmllQJ2CPi4dtrCH6a7SeAeoWQwpmOYliIIzj732KoSooBtf1XRFuXFybWMGAm3oxnlSIbMsKC5ILj8bel2_xvcfJDmAugBjyeLyjuI85ZahOs98eOh7nJkibMeBXdqKhh-KJFtoJQ0mKe39570u9BOs0yYeEOnvugABbIVHJEMSfiSCj3uNCdV9DSoEh8lkJaInJzlZ-HMK6PY4ZHtP_MJTeJ150wq_V50SrkVtH35rno6Jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
😞
میگن نیکولاس پپه بعد کات کردن با اکسش تیانا ترامپ ( پ.ورن استار ) الانم داره با لانا رودز وارد رابطه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101968" target="_blank">📅 10:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101967">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipSD8WOh1qpQRvbaUYAzXtvnM-E_hfuNBbbl2UbNVtYe8voixKzlUNbSaAlwQKWE-9jM7QUgTAnJXWkcUIPbwfzTF40GB4_itcfUyT65hgZKkZzwLklz6H6hnI5DmucfT0SIPErwKiJ2_y2akOwua2SNExL8KjfcLz7eu4GWil3eMD5RS-cV5NJIpyYhX9ZWhCfhru586NZjQu-BhwdvFsOjKiQHkQWzmi55NZyBYfIVyM8tkBt5FYyz_VkdWBVIrFBzOR4RJb6_M7fKtpljytf9s5bgmnKyP7ktaEPrCip7bl6se5uQZ62cJpGS5aU4-2r4hWhMwKciBPlfWkAVdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
موندودپورتیوو:
اگر بارسلونا نتواند خولیان آلوارز را جذب کند، دیگر هیچ مهاجم نوکی هم نخواهد خرید. بعد از جذب آنتونی گوردون و کریم آدیمی، مدیران باشگاه احساس نمیکنند نیازی فوری به خرید مهاجم داشته باشند و معتقدند فصل آینده فران تورس، دنی اولمو و رافینیا هم می‌توانند در نوک خط حمله بازی کنند.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101967" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101966">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdYq9OxUOcDyVwAoBiaeDlrLpq_A8TL5C9JM9xvmyn5juVq6w6XpRvm-mpbG7MS5H0vcZRfbyeRf8oYjTwbNcgPS6tDk975ZlZ-xw2XbJWOOO9dSbF4pZa0b48-Zh-tspjfvhiuHpnQQ4WWgn5xtKb0anmi6UAp-09AtOojh7WFWJKgBbVSHhSKiKRAu873kQoc81VQBj8rGJYGMnxW_uDiqQY_9CcC9z08lQEo0fdWw3CM3ZS950s2e2kGzxmZdkKvFKyKQ6GLxP3fUg5jDMxi-2cMzD2BNzuFFi6pyR68YPjNbKVAfvS-3Z4u6jsJ-XpPzXswZ4gFVyppkyXJRBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
–
فابریزو رومانو:
⚪️
در ساعات آینده، باشگاه رئال مادرید یک پیشنهاد جدید به باشگاه لایپزیگ برای جذب دیومانده ارسال خواهد کرد.
🔻
این پیشنهاد از 100 میلیون یورو بیشتر خواهد بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101966" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101964">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u8kQf9jCRNP6-maJ-R4_GDZyIUkpis6VNmBhAGWLsEfo6tKYIWROnWmzDlkNbJ7ftDiXTT6D6HvjBmf4YNLYLQb8IySmUK2Mcr3fOpg_x-PTj0BI-IAwimDXD26jau-DAwuQ26nhfNa54dWSQIInW5IuYZiGj7KI1mBkReQ9YNoI6bxlC8o82t7CJ-7bGXuPwqjSMxL81OeIwyOFyh5XkDoB_SaAotZT1OIB9Jr1fDncHt4V6m5F3JZkxkyHwMnXM18LP4hygJFhjnTGmI8paDm5bGXPQ6UHLfncddOb1XY_zYF0DHeODpg-A-lHrru4v53-l5gHHhDowA3eGU3WuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fd5IfqUgawF88O55EfPiyVB7zTjlfEUZONn7Dq3U0LcW_RvobXNfPY-R3JbRja70BDWYKv-H8bfw0wLsH76kM1gyMML1_lgtTnQ26jhFWggR10ENbvvfShesjVbcdz6T4Xhf4OFfTcmQ2xE_rMmOSVLP0b3QX-VXjIxTrX-0qQUFGqIb28IzB-QRHvX7BhbczGtZ-jbxa_hiT-43z2rRHaGyUUyjfBXLl7QvcRAX4G3VCcBsrpk2a0-brsU8Rhv1KfO7IGjsz7ZOhjxlgQ0EkjHzgWLMOPXWkwMXMpXa3NVo2PgVj8wXSMuxkSn8qyaDcxRogusuXu4ZtHTx7XDyAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سوفیا رین شایعه‌ای مبنی بر اینکه حاضره شبی رو با کیلیان امباپه، آقای گل جام جهانی، بگذرونه رد کرد: من هیچ‌وقت با امباپه شب رو نمی‌گذرونم. هنوز باکره‌ام و خودم رو برای همسر آینده‌ام نگه داشته‌ام!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101964" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101963">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hW5KO4HHlm4B7GnFYUHPyo3IMjSwOYktzPiFr8un4CC6QUq-J8RypCLI0lIY7BRFccMXCRuQ48SAFVu4QzKRFzG7mm3BqhfjM_Tg0W2pTojOQKDGBBXB9y908nJh9UaCVL8PdMZPfiKONfpHd8n6qLvctg0IfDWUwWykpbAebxS_HI4wQ1H4aEatYZlkNUs7r-H5L2oBb8svW8nTfimacPsOUnNzdXnYU1JzO9aCRlbsy4KA13O0eLLIlUsc1iCBApEAc1Er7Zm3J_RUSOxvubOGgMwd3OMxjYzxWjkGWCCfJVKS6arN4xDD2kXt3jcW-sTUuAilrZtnA0vr3cXt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رونالدوی برزیلی درباره کریستیانو رونالدو:
فکر میکنم بازیکن‌های خیلی کمی مثل او از بدنشان مراقبت می‌کنند و این‌قدر اشتیاق پیشرفت دارند. من تمرین میکردم چون مجبور بودم، اما او تمرین میکند چون عاشقش است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101963" target="_blank">📅 09:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101962">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0d0985c7.mp4?token=ZTEGsYhh8L3n9iKrodwFHieXql0JwKqLT3bNS2iPMNOQiBGQhu0xuF6WwF7IOqm6o2kG4e7lRw3-MvILfN9SFf3qzJYXP2B05bfcZXWmn3uPPhkxDuVFmr5cHWVBWA2yR1c_6L7fwB4pZUT4lnA8viqA5AGPIlgT5VUu14WuV-e9kX9wu8Hd5QEXTG8Zvz5iTRVLE3kSEoSkjNZ6ExY5vC2CZydfhKo8kGh0QdvmPNKZwEmQqoUEy1tlRwLrsfX_yoBju6N8w0g5FfPMWBSzJpX3IKHNVv78U027L64cfRcWlxWEt-7C4Q1xCG2DveyRRz2gp5qhdXHnkwPXSxmNfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0d0985c7.mp4?token=ZTEGsYhh8L3n9iKrodwFHieXql0JwKqLT3bNS2iPMNOQiBGQhu0xuF6WwF7IOqm6o2kG4e7lRw3-MvILfN9SFf3qzJYXP2B05bfcZXWmn3uPPhkxDuVFmr5cHWVBWA2yR1c_6L7fwB4pZUT4lnA8viqA5AGPIlgT5VUu14WuV-e9kX9wu8Hd5QEXTG8Zvz5iTRVLE3kSEoSkjNZ6ExY5vC2CZydfhKo8kGh0QdvmPNKZwEmQqoUEy1tlRwLrsfX_yoBju6N8w0g5FfPMWBSzJpX3IKHNVv78U027L64cfRcWlxWEt-7C4Q1xCG2DveyRRz2gp5qhdXHnkwPXSxmNfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚡️
بخشی از گفتگوی جذاب بکهام، زیدان و زلاتان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101962" target="_blank">📅 09:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101960">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oTEZhUm36o4sOWnYBQvdu5BtXiXEWsKfIf3aj9kpds7kc0Sqx_IThJHnJCvQTFqWusZgkWEjL7DycTMNwh9btjvSmuO3V8_VU3S0NhGzFDsXHvJ2UqJUhGXHUbotn5p_MisgFtZEO2DFr0C3seQyQ7aG3fMH0LgNcKeOxSoSC03VV1NihYZ7rTwkPXFm9miP64fujc_uM8hdmCYR8NzgUBl88ef0UQFs5-U4GbE48QKCg6N-e4Ny0Lq09w-d_hIzqzaXPHr_kK7B4YEvFjpDFql2WNI6sC-exW6UrEUqw3wM5wXkWtL0nag5FNUD0XsN7iJSpYZto8eNxGlfB4c1qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vr-lZpj_6cEJz9yi8SRFKLQ0grzYeOT0OuE838H4K5LKmcEzk00VZg11GObP5IRDCMor_WXaHT_6oxNBxCb_fDGS18R9vJx70cPJ5vokrum0hCXcFhU4soloahvROAlb5ly9rBHiQnbu7CCaV2R-N45Y-3hsUVsmRs0Sy4-KqqO7Nszya-zRN4xdo7DNeNSLaHK08B9kJD72-DiI_DcHSWAsBjAqjtJMUHxmYf5Y02cVb7il0bTS4lpyIfOuxGxrqQrVf9tJuDPxsjhuac4UH0dT5D4MyNDAPTcgKhUfRPy-uWo66SaYF_TliaNeW80iqTrcJ8qCwhnSUT9m9b28Bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریستیانو و جورجینا قراره ۱ آگوست با هم ازدواج کنن بالاخره. تبریک به این دو نوگل دیرشکفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101960" target="_blank">📅 07:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101959">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hf2VGkCxO7zVEX4vULwoPfEaVv3FRUnuaKmivTTzjrFa2r3lOPrS2rbiJxavZq-9nRuywUud8hBLN3aCJFVf6vUWe9oWgKovLR9uiJ45VTBB5SPh3ZkmyVTEJ_tU0NdK_4ACLhCIfbjSGHqdgfrB7Y538-F0OF2VMmFUUoHqZ7d-xv7SvIQySJRJ_AtyFF3Mqun1Z2qI4ITYduIg4HLBX3VzAeI0b6biPhHBY1IFJXL-WWXWqSqXNd8SX4MowCzEX4Zhvbsc2xTSIyYS1Tv4Jj65BiR3ux0WCSyW3G6zYpIESO9vkfl3bCEHKHmWa5jF_0d_Y2tV2q1sN2OlM0-6kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👑
موندو:
تعجب نکنید ولی احتمالش زیاده که لاپورتا پرونده نقل و انتقالات بارسلونا رو بدون جذب مهاجم ببنده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101959" target="_blank">📅 06:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101958">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85d2fa751b.mp4?token=Bo44AWuj0ehFtLp9lQNc5NkoXgGxtgOhiDOcRhjL0WcrtGtKsOHbgoX9MboPVr7ZnGpZlu5Bw_wWKQKimyhvnS7CM6QM_eFXvi0ZGdOyqzg-wuCKu1ViUP38bQyRLpJkiNztvZckHW1W1hRwlywZIXHKLhI5DTIeOjZaDZYRAWx8dCikNNrq7vrbhNNMTeDDXaUdQwhoHdz3s6mvm15OAsgjhw2TL5xX0Uh8Ag15rLcMGSjsBUZJZxhoEU8r_d4VCMFX2_GIj8pcUM4_JEP6eW5wGaMNmmehZN0fJUOM_OVMZzsR4fIj1HlzUEsnKNIAq_1ghEcjS-kEET8P29DocQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85d2fa751b.mp4?token=Bo44AWuj0ehFtLp9lQNc5NkoXgGxtgOhiDOcRhjL0WcrtGtKsOHbgoX9MboPVr7ZnGpZlu5Bw_wWKQKimyhvnS7CM6QM_eFXvi0ZGdOyqzg-wuCKu1ViUP38bQyRLpJkiNztvZckHW1W1hRwlywZIXHKLhI5DTIeOjZaDZYRAWx8dCikNNrq7vrbhNNMTeDDXaUdQwhoHdz3s6mvm15OAsgjhw2TL5xX0Uh8Ag15rLcMGSjsBUZJZxhoEU8r_d4VCMFX2_GIj8pcUM4_JEP6eW5wGaMNmmehZN0fJUOM_OVMZzsR4fIj1HlzUEsnKNIAq_1ghEcjS-kEET8P29DocQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
نیمار تو اولین بازیش بعد از جام‌جهانی با دبلش کون سانتوس رو مجددا نجات داد و با نمره 9.4 بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/101958" target="_blank">📅 06:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101955">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eVslrFQPIVGQvB6zqUZ2aWQfmA3RqjpS_mBfylTnp_Co2FnaTMFrB4u7UHeGk9KQF1uKmYbY9L5lI28ZE4iFxHZVCuIKupVt1c_9GnbXOfk_x20QOumY-5s0ui9sq6yUhB-xYwKT0ipfrfU6jgYN1WcvMFciacwBmII_u-FGoXN-TxTcrgf1wt2q162cK5t1NGonlJ90_48uQX1o2v3Jr54g_8eZmogASIhW7Vec1A9DwoTGAsyPl2iMnWRu2MBnUWF-WgBB93jbZexbWD-RBQ5B_Rl0EhYpRix4BLN-NmM14A_KFDD-R-_DteunhDd9TmccCX4Usbq0HUekluZNkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpRmzGmSnshE8_rnzo4wt7Vot--ZWX5b0xmhSBtgMJx0OSS4dklLVUrcHZBsDbIwjJSk6Hdriv_berNJfUbckCGcoGkwdIRUCT3WeMnsCH4A1w8oLCFCh1tcu5G9xD0oQI-_OuefD1-feICL0PYNMzCq7N2Ev_Umc3DeF3ov_eDaUJGe0NRsKSgY20gIPG8DCSthXWOy2QSxKvarNb4MPBp_6j3v10y_2qBvR3yJ9nq_tvwp5BidzKC25bc7gZ-3L52S4D6HPyIvAH7K-_2cGUlzb0KyrDtMGa3pE4S1laYP9ERuSyFmsU3Cri2jO3dODNat5lYse9ziA3dOWbtRYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953a60dfac.mp4?token=FbldGnMapol4nZTzGM2mnigkLIe6_JX0lnI51zLr8-N8_habHvOx4SymXhcVTCROS8-H_h7Y3jFgoeOu2StXmURfoutj0gOZfQvhiB6uyr-TUkP7vzByx1Nbxpzp9ihIgNNhyrOyB0486uu2MsbW9exu1bV8Hy5KenWV9OtCIZGd3xjSsrIn5c4_SRDqpl2FgNx5ZXqQh4yQ--XiH3LUUYlGamyfm96aofhj2CCM0_uQVhyR_L3E_C0gKFxBwkw21FF9p4lZd3xIli32FSQDY_-EN7EDGD3RBJCwHBYshHelPh_UeaKkrA53FPU3xzswMHy4pMXF4vur1TllXKh8zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953a60dfac.mp4?token=FbldGnMapol4nZTzGM2mnigkLIe6_JX0lnI51zLr8-N8_habHvOx4SymXhcVTCROS8-H_h7Y3jFgoeOu2StXmURfoutj0gOZfQvhiB6uyr-TUkP7vzByx1Nbxpzp9ihIgNNhyrOyB0486uu2MsbW9exu1bV8Hy5KenWV9OtCIZGd3xjSsrIn5c4_SRDqpl2FgNx5ZXqQh4yQ--XiH3LUUYlGamyfm96aofhj2CCM0_uQVhyR_L3E_C0gKFxBwkw21FF9p4lZd3xIli32FSQDY_-EN7EDGD3RBJCwHBYshHelPh_UeaKkrA53FPU3xzswMHy4pMXF4vur1TllXKh8zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🔥
نیمار تو اولین بازیش بعد از جام‌جهانی با دبلش کون سانتوس رو مجددا نجات داد و با نمره 9.4 بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/101955" target="_blank">📅 06:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101954">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAG_yOqwNaKcP3BptukJfDIVNBkqztjVZZjBUTVzvjHHwsAVimYUVr3zH-b3to-xZtpjeY-N2iJ0YId1RO49FDfR197Y-BwR6MJnV19BLu6o0PWKArjArwbWXTnrIOZEOi2b6Qg8VPf47JS6dFXHMpWr3xgNXD23-OcQnVCwoFzCaB5Z3V4FdykaGliclDUcYRHCrlXdwexmVF4hwSNSxRjJ2joIC7MFzIppbHEnoTSsjv5rFjhkvirxmosArsdQjsELYNbr0U5W0jBvSi4S8l0iJffXkdtbFE2MSvtjK0DKwegTkUzYbh-rH2tSd3eewlU52Bzmyr74eZIqbm-Ghw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
مسی امروز اینجوری تو روزاریو شکار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/101954" target="_blank">📅 01:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101953">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44643cb150.mp4?token=SpQoi2w9TpKb-pSuqkyb9CEJ-3LpC2dZg6-sH11m6vwW6IvXKp2YmC3jo_2RmioeMyndh9dLxJleaGj2Sn90KRF8UTDbjmicXRuinFDl6xtyRh9ydpo9r8uc2TpH04H5unqBzGbfkI5TWO_LdJaCoyw_M-wGYP39cun4sfq_KHnQjmF3lnqrwdV86B-diC9BsBAe_Iwjf6M7Wj54Lwm-e1hmoKBDI2gYaADtJaI1qy1xWws6OIeTF4wmt7o18bRzz0BsPU_QlES9rNbSSvK8Nw9QG67RBxLVc1HdwwdLsOmW_GVwySv9UV_AbGS8tCeibe_eyXT7VUARGse78zyu34ISNjxp8BKicTHnGoRKmlDEBHGbEHBKzRfRO5Wbaq4Ye5vZet3d8DYjU8mTUg8ztsZCSLp9Xut-4uEx9d50Y8G3z_cKuQicmUGzGH7CUSHo61-sERjkLBuSajhk1rBD3Sms6kBocgLyJ5EKzB0D8Aov18k_J_niuvLO0PV_boW8jiKl6ermUD0TE3wEgeSmrrJRjXxYwEqMYTJpZIcrizc8M6aLZi_6oEkNeIz1y7HxjqcTfusSB4qbezuFjDZT0tb0IS57UtHo_wbnumbwqJwK2ffy9UhK9gBuHoFO3hlxlOXM5oZ8Iq863rRtejzf5IVMvB2-hfMqr3knhNvLG3Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44643cb150.mp4?token=SpQoi2w9TpKb-pSuqkyb9CEJ-3LpC2dZg6-sH11m6vwW6IvXKp2YmC3jo_2RmioeMyndh9dLxJleaGj2Sn90KRF8UTDbjmicXRuinFDl6xtyRh9ydpo9r8uc2TpH04H5unqBzGbfkI5TWO_LdJaCoyw_M-wGYP39cun4sfq_KHnQjmF3lnqrwdV86B-diC9BsBAe_Iwjf6M7Wj54Lwm-e1hmoKBDI2gYaADtJaI1qy1xWws6OIeTF4wmt7o18bRzz0BsPU_QlES9rNbSSvK8Nw9QG67RBxLVc1HdwwdLsOmW_GVwySv9UV_AbGS8tCeibe_eyXT7VUARGse78zyu34ISNjxp8BKicTHnGoRKmlDEBHGbEHBKzRfRO5Wbaq4Ye5vZet3d8DYjU8mTUg8ztsZCSLp9Xut-4uEx9d50Y8G3z_cKuQicmUGzGH7CUSHo61-sERjkLBuSajhk1rBD3Sms6kBocgLyJ5EKzB0D8Aov18k_J_niuvLO0PV_boW8jiKl6ermUD0TE3wEgeSmrrJRjXxYwEqMYTJpZIcrizc8M6aLZi_6oEkNeIz1y7HxjqcTfusSB4qbezuFjDZT0tb0IS57UtHo_wbnumbwqJwK2ffy9UhK9gBuHoFO3hlxlOXM5oZ8Iq863rRtejzf5IVMvB2-hfMqr3knhNvLG3Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوکاس هرناندز: «کیلیان، اگه قرار بود یه تتو بزنی، چی انتخاب می‌کردی؟
🔺
کیلیان امباپه:
فکر نمیکنم هیچ‌وقت تتو بزنم. دوست دارم مردم من رو به خاطر کاری که توی زمین انجام دادم به یاد بیارن، نه به خاطر تتوهایی که روی بدنم دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/101953" target="_blank">📅 01:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101952">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3rnSNUbAPnQSPu8aPRJVCdD2GOUiIgTMinrBAlwTxxhbUOJdn8zoUnfvnI6-0RdF27pis27pmc6Ry0jb8MdjF3raLPv8W3piloaN8cdpVK3gmVhs2RcX6MJv11BsOj9wk4u3ZMrdZGCCEgSufnpzkKKKjHpX9Yi4Ve9IKP5M7LESX5HCMc00tBXlli9ZDbBs_FWulM-bRxRKqKxU4cuG-5y8gZDIcZLBJaXUukLh2VQWCIu9UcmczAU4EqrjngFrSLVUoPYktyxd1Yb0a1-2fzpjZ3rVvMnzAjfnOYydsTOE4OJVjNE7-CjRcPYOECNYGREW1If3tSx4Eb59mG8Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
امباپه و پارتنرش بانو اکسپوزیتو‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/101952" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101951">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNZtEvEG67y_r61Eu11l5JXWmhRuEhOeZ60gKO8SuHwqpnGpYPQlNVw2A2pRcXCO0vmNvjHREMsfX3dd3cVWdYvExfvtLE_8fKm0q19T9c_YoTGWx2YpT2sz4fO4IBEbOCQdxWfz3CwC2-1op9fyxaoJPOHjvZj3OFaYzwgUZ8OWPZXo8UrVryyHEvDMFLMP0brXLS71_0dGxRNP3p99UUQEd2N_FkOeQoIuYi2Z5vPTfs6GJePrYdFkc0QXxi-U-p6wz1U70bSt4H11tiSTX8arJkNfIz3x6zFwM3ev9yheeU2TXabAbZzZYlU8f1oochQ-5nbtRpGKtiSz0UWSfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی خوشتیپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/101951" target="_blank">📅 00:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101950">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63dd42dc4d.mp4?token=uVE9y7V1a8LqnwMuS2R0ov9ytSDawaA_QgVE0R8ksXjFV_JrCC0Zc3ow4F8W4CkoMXojztxIubdXW6OcULvnsZcHa4xf31UmZdSz3qt8dF3tnBhCzq_UQzmnWxJb-3KQuCXea8kMrYw2q1Tj-PSi-11DBY6CRyS9xAYuHjQeGZlntsLciw664aVJT0HFTuCAX9aoP2qly_qZVLVeDnJ4JdjhDHKhwO_y_T1mxYJsmF0-fdINBorkTJslbl4OFsfPfqJaSk94B-XzIOZR4tfVWLNOqBlq-jm7nU7_c58KxzP1NU4hPhQf5oRPSzlM49wXEWKA9YvdzcdXsN0AExGG4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63dd42dc4d.mp4?token=uVE9y7V1a8LqnwMuS2R0ov9ytSDawaA_QgVE0R8ksXjFV_JrCC0Zc3ow4F8W4CkoMXojztxIubdXW6OcULvnsZcHa4xf31UmZdSz3qt8dF3tnBhCzq_UQzmnWxJb-3KQuCXea8kMrYw2q1Tj-PSi-11DBY6CRyS9xAYuHjQeGZlntsLciw664aVJT0HFTuCAX9aoP2qly_qZVLVeDnJ4JdjhDHKhwO_y_T1mxYJsmF0-fdINBorkTJslbl4OFsfPfqJaSk94B-XzIOZR4tfVWLNOqBlq-jm7nU7_c58KxzP1NU4hPhQf5oRPSzlM49wXEWKA9YvdzcdXsN0AExGG4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ری‌اکشن هالند به میم هایی که ازش ساختن.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/101950" target="_blank">📅 00:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101949">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHQFUN5-EIu4gHvNA7Wrl0I_kscR9sMhpD7mvNExC-zJNU0ySQQpF3ie1fGZJz0e4Wu18LYvLg1Ch70EUqqE0m1IfU2SIJ53VwnQDgSpfHSE2Cg48TlmxB_c_2Zgsrf6Se_KlzeQbSP6OyLJm1amXZ5mr0FBiZu0UWdp_BjOryHnRXrEukXolpVrGda78-snncr8SnnzFU5bWpiUyXIz_cwBoTJJc5Mp49hTfFthogRLR0JEg1ucHVV8ZQI4ggJrUdEYPTnBvtUPCfxLdrdss_kFmm82Wtk_syfvU-uy3iaYwXKeCus1bQgU5c56F6Fjmt1fTk9Fz_yDqBmtKnEExQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/101949" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101948">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1g4yGawof9j3QGozj_aii6t4zsm0ckDey5zCWoItFg3hbohOolYzRVOXwUW_7Xk9Oaq9HbhMehmhwm-ntxf7ZHXRB_WI7cdzKeHcOfuhIClLJ_M18Vew7LN8iKIdCtAt62LrEYSe9f2DU5AsK0EjrLC7sGFfzOi1dkfYSaEK2_Cz8VyfgrGxlR_7jUd2YvqnOvuwd3N-7ikbB5tvlh3jDinPm94YzsL6ntlm3xU25mRS04ffeYZZpI9DxpRbn57skraqZC7Ht9Ld3Q4KG8nBR-bUW20VGedW2XB5NxaSlRP2L-wHmDlEqF7K_U6-AYLUQoK20mIAOyAWteyJfX5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔹
ساشا تاوليری: باشگاه الهلال میخواد مبلغی در حدود 120 الی 150 میلیون دلار برای جذب لوئیز دیاز هزینه کنه! اونا بودجه 350 میلیون دلاری برای نقل و انتقالات کنار گذاشتن و این تازه آغاز کار اوناست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/101948" target="_blank">📅 23:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101946">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NnZF6K8LEqBsg_yRU_MNpvjnQZVuS47zKpiJHHbzDPrf8Q0TYuZSy6HbY-CT_6m6zVqsIKtiyForxwzBYV1z8sDw7mL2EQ5X_4aPFJgnxlozpuiDxGulU-ccWror07ebwewaDs47v6hPzH-hn9ftK4ZYAFo-FvTrCzI4VHW8s25P4hYovAY2Z4LXVwQ5IvXD7HFGm3hLUjKDpeUXnbVWUvXurDp43CnfK0u-EHhPAdjJTdzZg9cVNJXjaSY7HcthBtwjHMPWyb-DvvUr3Ylx19z4fDIQDiZJ759k_RAP3TGnpmuUM9ob7GPLQSdCUXkZxgefcg33DIM5PlR4ThSDHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/adHtR5WrvbZkcCGLOlAMhLZS2UDwZAC8Tnr1Iq4xkMAZOp4KNRjjHgG_odctBMXYbqFRm6wO0c94KfNy1WfzetyiS2KgoVh8Z1SuoysREDuwvjx8kRWJYuCtc5bvr8BGxiznUxNbag20U6ElvWuHf2QTYwzbUnYYw8AwZY6rDckQTBSFJnQEprK5HM0qpKbGmdkDc0oi9zrdvCZbwEaNsrIe5StaoFIiuH6Ow6GgqZycUnwp8g0CxE5ACj_o18kivLQmWZwLoIftahehNVqMJQMNeyFG_dhE90MWIUU7HMLjDwQhBSbYHXvsCzOk39u8xI9PI7J2pwqkJ75Qol50Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سرخیو راموس درباره اینکه بین کریستیانو رونالدو و لیونل مسی کدام را انتخاب میکند:
برای من جواب این بحث خیلی ساده است؛ اگر فردا فینال داشته باشم و فقط بتوانم یکی را انتخاب کنم، کریستیانو رونالدو را برمی‌دارم. مسی لحظات جادویی خلق میکند که کمتر کسی قادر به انجامش است، اما کریستیانو این حس را به تو می‌دهد که فرقی نمیکند بازی چطور پیش برود، بالاخره راهی برای بردن پیدا میکند. چیزی که بیشتر از همه تحسینش می‌کنم همین است. استعداد یک چیز است، اما در اوج فشار درخشیدن چیز دیگری. وقتی کریستیانو در تیم تو باشد، همه تا سوت آخر به برد ایمان دارند، چون او بارها این را ثابت کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/101946" target="_blank">📅 23:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101945">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8jf5Zz0hfdo_JtN5rhlMdm-tpx5XoJKqG6o5c9GbhRiJJe4wkDydIzsWFqtJ8kDG9QWRSMY7GS6cgBdk3t-DISRPzgGx4NIaNxetQdj2X_6AJDrop_654fSJVf7Y6kxBU6aJDdz5TSoKsKveEDt19IVz0Xv7e80PNe-KGwye6mzQj362ZY-h7qjCrcscjwNfaDCUITFERy2MUy-Fc-3S0sUEHykWiY2RUFc59TyJuRKEhOJuM4RIJTiAwdz8Qd_RnEcLrVE_RUAMnN-1l3i634KiC_m16RNGid_xKgbpFRt13A0T4IE-uz2TDRh3N3jQwJyUv1zYSj4iMxXDrFVnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
به نقل از فابریس هاوکینز:
مایکل اولیسه تمایل دارد به رئال مادرید بپیوندد، اما بایرن مونیخ درخواست او را رد کرده است. رئال مادرید تمایلی به درگیری با بایرن ندارد، زیرا رابطه بسیار خوبی بین این دو باشگاه وجود دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/101945" target="_blank">📅 23:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101944">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhCZTMwhxfQZ3r_6Fz-0H8hSeh0AOz37x2icYgWW5a5OT3kba6HM7Rc-ZeAnzSYD8D84dgU1Zun3qpG9RdTlI_6nJ4bquQzTVojSjtXD9_iny4pMDuDs8H4PGhneerku6lECQEf5hgVHaw_JzG-vt_NWHYAiS8S6Hcw0mrA5g9GfLYlzn-VFnlA9IrmQmyCDgfWVICnHG6H618ORRqXOXzFe5Q7n8l2XMvMUAUVFKxkRLJOgCfuQTNEjEUZbaU8wJfxX-RZ1b2mF17DLMSG8xA46cZxSDJFG-mk10JiP1qxpp7MD4gbYayHTljv5zHtoAsAca3rXMiXLQgmVrats3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/101944" target="_blank">📅 22:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101943">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZrN7jvD_40C4wa2OLdc-qwfa-9f1uFpsy1kr2m30T-SWZ2QOIYIlecaNoMfBKGExkmJ3v8J2z8zoIosz0c2tgzVEOWnU8rRhijikNU-XgzayrOQ5SHPSYp7xgMVId6ixi1lldqogV0Y0XHgW_nbLjJ_mSvwLTw5XuVOWiCo6nC3VswMTEc4kcMvcqGeh6ZCQzHnhOIKDhea11tJpYEkAv09ZIE7sk5_uSvDxhMNr_ttI4pzbydbtYzFTAOI3K1uTiGsCmEFM1PH0qebE4Laor2WPZAE7hQi6H3uXERpVxth8EjihByRqkzdhkPg_al4_5oJ1SAb0LBL70dV9DRfvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
رئال مادرید و یان دیومانده به‌ صورت رسمی بر سر شرایط شخصی قرارداد به توافق رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101943" target="_blank">📅 22:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101942">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOQB9Cs7gZho6q3JowifE1uJOBb5PnF66Sx9UgMACp-Vi0Mo9SKqh7dEQzIuVajz_sCcqYpU9qb0Zdi7N6AJSQe-1dxce0LcYdVfLdYpFPzDjlVBc1P_tCvbIOME69OoKq-qLBpbitVT8iCWJ08sQHZAUl91q7YTA_CO0lafY5xHeOV-MtKAx6yedKexemikKJcHNvUUrC1xncOH8UMMOJm8nsAcnwFBSJ47RtEx2sG1j_VTu9o4t9qsGLnwhHmMYF03BRORIeCy06Ly6ha8Iv2H0i_fjvCS848wqamQNMB1yeYj11yof0o1OzAB7Xmf4I9XBb-lhAUOOY2B-6QyFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
ترکیب احتمالی رئال مادرید برای فصل بعد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101942" target="_blank">📅 22:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101941">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcmWwW-G_jUHIL7Bk3hegNSBVk-iObBJ1zIrgGd4jUCz3WmWELUrKwxNF7SLCV15YfMQxTxM75OBHaowKcxDjQKLg33RdzkF9jX5CDBLJfmU7bHoSTI4R4pNCqBTsGEsS__4HJywvxetNu3HO4LwPXtrqPMkDr4iKgd5xkpqmkpJtvuRZFtQuSM_yroFNW-bER36IK8ITRw9q_60XgZPxTVPyzObhEUP6ItSWgVs3rnSDZJcoW1Oy2rs9sEyYSSYdK8orFGrtmmoLTSB-kzyTy7Gp2ey7-f4auT_u2ZlI0xozD25k-mnFs_BHJaGRt54_fdpig-aMXyM-MF-44SWfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از قشنگترین تصاویر جام جهانی؛ مارک کوکوریا قهرمانی رو در کنار پسرش متئو که مبتلا به اوتیسمه جشن میگیره.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101941" target="_blank">📅 22:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101938">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lg4hu-t1o41dL8ZeE1AZZiEEPLPkpuZBBmFpJXwxJ1jR-rjWeYtsz7_cdw3euCCZst2WY3St7XVo8iR2NBklPt6XUBPyrWggSKTg22c_b_dxReawPyZUFYYIrwGphrOO4U6L9NzO8Mfjuk-iqXn4RRGIVMt2-96a2vD7b_VB2_5lX6Weq9gteHVQJ6VSlxrpqycomG6Hro1OZWxhE5LLaj88xqbE5tSY2J9sr4mYEDcE-E-H0LRMd9E-kHwtvAbFSD0wUi1M5nnWo-pBixHTj774GekZpn6lRI7C0yKCMw4f-by76r34M_9EGeU58APvUoZ8EG9PeyWE9nu6dDFBGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aKausD1esmNcMhWqsoXNsg5oNeJqNIUBeUwNSXdSIg1oSUR5ZwUvVXGPqJ3H8Z2iDuHPIeswjAUACMKvCDDENMFbxJ9DQk4S6S6RWd8UbVtYVYHGOmXlth67ytED4N_3UxYbzqI2kzsgrIwV2RtYQ3nZnLkv5b_6ohWWfYJ3_noPPRwnEg0F9__rWu8tnR1Cfp01x4wF_0zImQl-alxVVRidNpovtIy0K2qRwb-1-6VBCgz_cQvp1QEgBwv7H35P3as7jrpZx3NMMI1xl5UKu7JRBaJe_mQTAQtGV03PbPcm_IIxMTs34B8d-LIgRvl76WjwqFIflejxPfd4lirP9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gh4rxXTQtgEDHMIv3mAs3VRkQPeSgod1rx1TZWhvgzLEc2NyZZTVa1rJozkf2zLPg9YScDlPx_vYDhjIU8WlaBpCl7T_0Jk__OHnP2uhTAhSslGMAbLmqEavGTuuHuL3RLnFz4gjShpuVbXFKJwqIaZDuBTxtwwZyAq2_cK5WLfvqZc3B8AEpIiOXmTzO9J4kbpGOwzuwGqzmcXH8chRgjpixIralEsvGPVbr4GGQJecOtv0b7wYnVKvfb69dLWIbcAU5dZ2BqlIK86QhngMJzddjHq4C203L1FfMaRxNOYh1lgwIKmuR9GaeeNTlFdNUcBrtyf9lXrwecnqWre0sA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇳
😆
امروز تو یه حرکت پشم‌ریزون دانشجوهای هندی تو اعتراضاتشون ضد نخست‌وزیر هند، عکس امباپه رو هم آوردن و محتوای بنراشون هم اینا بوده:
«دیکتاتور امباپه شکستِ سیستماتیک را تحمل نمی‌کند. همین حالا استعفا بده!»
«۱۲ سال در قدرت، و تمام چیزی که از مودی(نخست‌وزیر هند) نصیبمان شد، نسخهٔ پرمیوم امباپه بود.»
«دیکتاتور را پیدا کن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/101938" target="_blank">📅 21:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101937">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vF3lANEr2yV9TH-8pQEwaKqgXQrU5BPmz1GWG_vhHQ2-FqMjZyKfKeJ2viJBNHntmLNtLX80XSH4lquGCQODvOvEEYzS7NkEuYxOv2gNuwE31ozA6UD1bxdU_9t6_WXS4TIADvAiQnn4VPZxSAtSA3Dqy-NtCLgdd1PMNJDGs_glHiN4wqjmzykpxcZ_7lk9shJzVDjfRcduy-1GAkeYVlTluFJObO1gh7__ZV71nPbNzhVnwvQHhukQz4KbZbENLp1MWWw-uBwgEjLUX_yXamkofyhmrkyVATR1cvXIMsW95N_jONU7iC22ZwzcCoI8ZCZqDf3bv2yjgiB_LdNzbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلاتان ابراهیموویچ: "بین این دو باشگاه، این سوال پیش میاد که کدوم یکی احمق‌تره؟ لایپزیگ که پیشنهاد 100 میلیون پوندی رو رد کرد، یا رئال مادرید که 100 میلیون پوند برای این بازیکن معمولی پیشنهاد داد؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101937" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101936">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lc0SpYr5GZSuWZ7OBQnkmKtAF5t8BGy6SSYE6HOYGToyxaUrJIMN3rGUXaZ53Tm6jqb-N36sOUV5GZFIs0TDi2OTFUCKPCkrJGScQrjzOlYA7Tf1IC6hns0h84ZRv-NEa1wsZ8lupJHJ4_trPdJ_R2Ts0OSGlCYASGe4Q6hh-jCj_Fjtpb5N94CRWC9KPhkBx_myygiy37Rp10pEEw89IgGwJsqrW4djUOClJQipt5fQTePRQy76htgUlS0oLYobdNkFqx7629OKiY9WVzIZAGvXdhiu_mxm2bedVzR95dYj_8YmwuQyGfnQ131FEqaIQtHuJ0dJ_SvZc48qls7DDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
محمد خلیفه، گلر جوان و ملی‌پوش آلومینیوم به استقلال
پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101936" target="_blank">📅 21:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101935">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVLNh9Y4vjCgOICL_gQtTBjnKS7E1pMW-iN2oY7D65Rg2goR_Ba6VSd657iA8AbjcM8BtWRk2ZyNMegynFbFGSMQw_LLpL33caJrBEyQi-pjwbG1Y274-Y_45JbQN7eHh9yGJCDZpDsVjjgIZS5khXI4mkEPpp_Yy_1uMdG0p2QqUc4_7PNlNliJZS9Y0QBsg96ZldS0W-cQHbYFXNRBQ7RlE8VDrPLRgo6gG1eIgaWTKsSLG-ImKOO-EEZrt3si7PI5gTPZe_GIxErEvFuNDMU2e76_CSvAkogyi5CJ_obp7fhQzbOis-q1lLM6-TsCw-3P_o0xRhCzXDcup-NIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ماریو بالوتلی:
یه بار زلاتان ابراهیموویچ منو با رافائل لیائو مقایسه کرد، ولی جوری حرف زد که انگار می‌خواست بگه بالوتلی بازیکن خوبی نیست.! منم فقط یه عکس از جام قهرمانی لیگ قهرمانان اروپا استوری کردم و زلاتان رو تگ کردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101935" target="_blank">📅 21:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101934">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_q08q7WgwRk9UsIN98hyGa3lkg3W64H3um8cJrdSfU-T4LJEnbk6L71rz_qOjxH-ogmU_3cnRFET6UxPH_-7UsT5TCgYMcTtU79tD6J2qN_amRCDCiSrrhRV1OWncTZ0VxLJxz7F1Ub00IevK0i6ctCbpPtUkFrJpYY33rwVwcMx7A-GCKJQvtjnoJDcj2rMNerXCPtjgEKPVk5O6G7Q1X6BB3Mn8WbYjp71sGZqA5cLSGBZfahbDSv5EAyPe6II7q9vxJK-_hhLh836n_m44voGN-6m7tk7K8otYnVtonMgUqiy0FJmxeQncN0nH8rVO277u3K7UMKUbsWm6s7ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
کریستوف فرویند مدیر ورزشی بایرن مونیخ:
اولیسه به رئال مادرید؟ این موضوع اصلا برای ما مطرح نیست. او این فصل هم نقش مهمی در بایرن مونیخ ایفا خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101934" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101932">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FlxwnkqtUSgfqP6kmZLJ9-I0HZOQ_mZ2ayYpQ2xJth_FRBcvowVWOYaimTiEOdRSdRpUo2S5iL2lKS0zE-OKCPPyQgiWYFPgmMUDD2mTtMUPkyz7hKzBvXF494CZkoszKt42ykEW_jdWz0KKcU0d9ArfIXloo6wBm1Atc8lhtf9XOgApR_ZD9Gpmcvv4Hd9uyx6lC1wwRAIMRCntq_uZOphSEC0blnszg3LnfEX62K6n0crQ8x6NIInUOCiaNM_N9PL9-ZF7QTIiduT_JeYehJuQQU9o5HmcjOrHb5bqaUDxjjftO0X915aHJeqVqOu312FqzELDGrE0zcE-RAUKXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AtwyrN8qMbsGMJd1bCNLNZO0kqCAghkJF4QCfnlrjqDdH-ge5yvkAwMzFkZzZORf6U-WCaa6TUB769dKn9UeyIXblI_4Q61YoiN5nkDI9yH9l-TuXZ_OaFE2lgjccvjfjQB71KTBfWTnieXgQeLIJkIyDLcOjQjgdt8Byk8fnB58Vqsqyqe2jNw448rxpahpV10CA0xYzfyCXY58GCVFjiNWGE0cfMrwwhWTeC2aW0354JQZgAXWmNOeakwuXabxdMByu4A6vkz60ayncKsheurCuq9uvZq9nLgNRYJHJ-bKHTCwfkIaSVDuXm11vI9jPnoN2L0s1_JZov7vXb2Y8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
براهیم دیاز هم از پارتنرش لوز مندز خواستگاری کرد و رفت قاطی مرغا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101932" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101930">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXYzlmn_IhwU4Hwjo1eBOcxHx9LeWwCBPkE3N8lletr9wCvwoMs8xnfLBZGX7lnN8v9Rd49RiYLS65b58acCgbzBrAXCc6Rmg6fMqjzZhxCqPgHyPBsZbhCyrB-q5XaSgndRxkv9WCaOHww36hn1u5WNS2SBOXp5oYkrkhqNNpV9C5HQgNGthoiMJokrzP_dt4AAGKSHRGGJ3oPH_7U57f31D_9rEhff7of8W3bgwB5rys5VDgv3utSqTmnFkzQ_g8vtDYDURhw4hy1gwCy5rPIBw2jrg0NWt5dTnyk8cgUOmzS21WE7mvOACoHv6BDjiAMwqJI4K-bDokZk8F-Ohw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2c2dac8e5.mp4?token=Sti-Io_mUCC8wpeDQCVi1kvL4gKfNmPEeIDFOZ8Wxy6cikPYVf3xj8RV6Q_u94zldyPRVisQNzMepHLdzpPGbQnk8DrKA8lUAzLD0PFK1fmjdQVdKlJB8JmIPGStSbZtoMqDsgwH6inbuZHlvGJU3Daw4JqsRYuH-HX-d6YyW8ov34V_i3reW-cjb0Pgh2IW7vv_gbx8tM3gkwXPBNeXtK_k6fnH5FHYMXy9MY4fjE16NRaAM8MKGqo2XAdVdibqeFrgEDUrDJMw8UyYR5JDiF6AB8QpQeZUbfEZsodlz1y7d2n-IF_iQK25SuOF5Ros74jMKEXXVZjuJgRBoVkcBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2c2dac8e5.mp4?token=Sti-Io_mUCC8wpeDQCVi1kvL4gKfNmPEeIDFOZ8Wxy6cikPYVf3xj8RV6Q_u94zldyPRVisQNzMepHLdzpPGbQnk8DrKA8lUAzLD0PFK1fmjdQVdKlJB8JmIPGStSbZtoMqDsgwH6inbuZHlvGJU3Daw4JqsRYuH-HX-d6YyW8ov34V_i3reW-cjb0Pgh2IW7vv_gbx8tM3gkwXPBNeXtK_k6fnH5FHYMXy9MY4fjE16NRaAM8MKGqo2XAdVdibqeFrgEDUrDJMw8UyYR5JDiF6AB8QpQeZUbfEZsodlz1y7d2n-IF_iQK25SuOF5Ros74jMKEXXVZjuJgRBoVkcBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
برگام عجب سلیطه‌ایه این! اینس گارسیا دوست‌دختر یامال، بعد از موج انتقادهایی که به خاطر جدایی از دوست‌پسر سابقش گرفت، یه ویدیو منتشر کرد و گفت:
من به خاطر پول یا شهرت لامین باهاش وارد رابطه نشدم. خودم درآمد دارم. از وقتی با لامین وارد رابطه شدم، بیشتر از چیزی که اون برای من خریده، براش هدیه گرفتم. کلی وسیله گرون‌قیمت براش خریدم، ولی اون فقط یه جفت دمپایی برام گرفته که حتی ۷۵ دلار هم ارزش نداره! بعد هم برای اثبات حرفش، کتونی‌های گرونی که برای لامین خریده بود رو نشون داد و در کنارش دمپایی‌ای که لامین براش خریده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101930" target="_blank">📅 20:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101929">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8-Kxh1L-419KVL4R5IaTIbROP8rDrRP-4cD5vlv99Ur9dxw_ycQ76L8tCNhDaBlseSy78rs3F5qskaGW12ztS0ymPiucULSJTkGUcv7BesBOzeI67kDX7l98h5R8b9Pn50oT5LVf9KjIK2D2Bz5cXr8CYnjfzGFbKHpzwEYbKKI-p6Cqf0uDw33E8UDGG7ZyUMeSG1XbMpsBrtkSH6Pv5esOi8ylizs93xmag0aFC_Na1Fcazi_EbnAB2ZlXgGjeIm6ozTE5bI6H-vFPZ2Deb_smnolGZzTW-cuWvnfl8y--90ALb5sSgk6Un9_MNbUnFsOAg82bFsKRW_0yvVB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پوریا لطیفی‌فر هافبک گل‌گهر با قراردادی ۴ ساله به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101929" target="_blank">📅 20:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101928">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62941770b7.mp4?token=ZtuihivuuG-mg6GB3nQLR6rdEOP_nvQgvtSOBCiWu8dH_lFah_c6oSSPkGWm4AZcUhbPlecHSJ2u_gnHgh46-ThasedVTOwJxsmTS0zmV_OYboxGZe37VAJJNZ5VGZsSj44Sf5077LIOKX_oR-5vRS6euqbI-PJASLQMAe6A32R_eJu9wfgSCD96Xpi94YM2UFdN0ADgNK9I9OMykUWcRAxa_sWaftMaqBwhCRiWiSJaG_WGSy7feg_kfk9wGJvTI1w5m68-LfljjlZ_7cDisLrDRHoP_Wfh_j3P1Nt3_0NuLfRFJwe0h8TPEhNnQqXUUgE9hUSBigY9XDmxQLY-AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62941770b7.mp4?token=ZtuihivuuG-mg6GB3nQLR6rdEOP_nvQgvtSOBCiWu8dH_lFah_c6oSSPkGWm4AZcUhbPlecHSJ2u_gnHgh46-ThasedVTOwJxsmTS0zmV_OYboxGZe37VAJJNZ5VGZsSj44Sf5077LIOKX_oR-5vRS6euqbI-PJASLQMAe6A32R_eJu9wfgSCD96Xpi94YM2UFdN0ADgNK9I9OMykUWcRAxa_sWaftMaqBwhCRiWiSJaG_WGSy7feg_kfk9wGJvTI1w5m68-LfljjlZ_7cDisLrDRHoP_Wfh_j3P1Nt3_0NuLfRFJwe0h8TPEhNnQqXUUgE9hUSBigY9XDmxQLY-AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
استمرار، استمرار، استمرار تا رسیدن به هدف
این ذهنیت منحصربفرد ترین بازیکنیه که دنیای فوتبال به خودش دیده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101928" target="_blank">📅 20:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101923">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzhA_FifHgpBdLbanblqjNuuf7NRx6oXyxmGIVggZEzaoLBO_miJWAKLp4Ji5KDpvKXzmyN9pESfF58t9Exb1H7npXF5v9uNEMUI8tvPEiUZe8x42PHvJGv7HoGI0q6DdOAAQdXdlawgORWmaOVKp39pCZ3WuYR2l50Cxtfil2Q4klhbs5koHLThkgE27YNgB0G8s2ZlQNPO-3nCr6TIg6UwcL3UPSezOWSHJlsGJvuYoL5tk_UK59aAymMAmV03dMKI6MSdnOLS1wC5opOxd17V5VgCDAf8gSYhZXGQK5hhG1DHLBRBNTMvN1H7UtXBw-uMk99eRm5SaoUSwa69lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHVfU0ceadJQhbDrPaoegT4sYZQtRIkN--nZPABwbZvIeiXDM95Avi2zBpZqUz3XZ87vTsLbZ3zceNBtGpDOuu67pnAF72S7EMinJcmdIUtpzRSaSnWmcKyxazH1xr6AERqzDlJjy2bBYk7DQQXVhNjQYJwxuaqkb6SSVenI9jVVOwP-mkS44i7QGHzpV_FvcKzeMqN4_jDZtcAKvEmdWpChjD8EnMYjtEn-ASHR0lnxevow_UWmGJHo2loIkezNsj8jXBu7w3OjW3F66jgQ-3R_Pxh75D4-sszLf82cY7tzOEoDCq6fEJyZaX8PU4XzSL5cBKjebUGRnOxrKTLwsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sZq8z_6JPSn5O2OqY0h371ISG-CjTxOkcZlYOk9luwGNRGn4k4CRT4C2TtF2VlhLeswML8t5yyaLSZ9EJQbrfruY2JvEA3C2DXtrhlf0-CSU7nTbGz_-c7pWEPuDVzLOT0oG_jRm5eonVxXi-eLatYxIIGrPnT94puODoBPnEY5Jc_tEsjaDew-lJbspzUFssqCUouYKBgIRI1c0eHJ0IuASTjZ2Nm4YbeS3pu458YHdPloNVOrMzozeiKrY85yHJFeccyUztsU_gP3PdTU2UOg6U96Jq8-9YCUyT1CxtHEORjAp0Bntl4p_LRRijmiTBYhcGvam_mSvXgCQzxSrjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91c7199c9e.mp4?token=EI2dfS25vmNDT-GN8182J2tzKQK9brkpdNmLiJGO7ESltkrQyHTa2XlV0SBjbTJeN43Tv16C-ldOgyslA8btZauI_2SlNPQ7v1uJ_rhHsxyxxdB3DxT_TDvBtR0pdI7zs0T16NJ0ZWZEGFp-RiDcciEhBQjotqe0YZfv1gDjRdGbYdixLaZeRoTuMru5xy3XcJSztq0AR_g31lEBnN5XQpDC5Tht4uwkiInoKyBLqC4mxpOk6nEedwuaLqdSnzYntoLrTTSOZi9T_pqQBdzyEkqyxC-02So_o6jkU7Aq4n2POXrr18fcLmKm0tdgOljE4jxcYPDKNwOQ_3Lemrqt5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91c7199c9e.mp4?token=EI2dfS25vmNDT-GN8182J2tzKQK9brkpdNmLiJGO7ESltkrQyHTa2XlV0SBjbTJeN43Tv16C-ldOgyslA8btZauI_2SlNPQ7v1uJ_rhHsxyxxdB3DxT_TDvBtR0pdI7zs0T16NJ0ZWZEGFp-RiDcciEhBQjotqe0YZfv1gDjRdGbYdixLaZeRoTuMru5xy3XcJSztq0AR_g31lEBnN5XQpDC5Tht4uwkiInoKyBLqC4mxpOk6nEedwuaLqdSnzYntoLrTTSOZi9T_pqQBdzyEkqyxC-02So_o6jkU7Aq4n2POXrr18fcLmKm0tdgOljE4jxcYPDKNwOQ_3Lemrqt5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدری تو تعطیلات در چین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101923" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101922">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNXZLZMdD62QiHahnAIKAAklcLk2FyU_0PtKVdJb1H8gvTh61ORd7xknSdDR7cNFHbbZtXcfBkMvnZ-csRCPy0WLogvotw3I4pPlTwVDxy_hPD55yvhnmBjr4cX8W17afsuUYKMeH1dGK-1W3RIYWiJU2MUMFu6_VlUqdSFHBUr9mguerQrTzpmrxLh9PJTBGcETmgaVymNdX1aGqnMTU61vrmOLPXyO716HC5xbfejS6uxH1dWwViNiSCTbVUZWIBdrlJ4hsN4ioaxVaSgDmf3it5lG9FxKmjAMdlQCtVsMQIw6SEyMp17dUQEtW44vg-6tanffOL0kx8tpZTONUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔥
همه مدل کیت فوتبالی فقط 570 تومن!
🔥
⚽️
از کلاسیک‌ترین کیت‌های نوستالژی تا جدیدترین کیت‌های باشگاهی و ملی دنیا با قیمتی که هیچ جا پیدا نمی‌کنی!
😮‍💨
❤️‍🔥
👕
کیفیت بالا
💰
قیمت مستقیم از تولیدکننده
🔥
تنوع فوق‌العاده از تیم‌های محبوب دنیا
✅
دارای نماد الکترونیک
✅
امکان خرید حضوری
🚚
ارسال سریع به سراسر کشور با کمترین هزینه
اگر عاشق فوتبال و استایل فوتبالی هستی، این فرصت رو از دست نده
👊
⚽️
💚
کانال تلگرام برای دیدن مدل‌ها و سفارش:
تخفیف  ویژه  برای سفارش از طرف ما
👇
👇
👇
عضورت در کانال
https://t.me/esportsofficiall</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101922" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101921">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fac07199b.mp4?token=YcXJFDANFzkgnf5v2BZhA1Kh004xQN4LRhoG1ZcfgYsiMlaDnAyh45O7gZSeyybsTefQiGuAssL9iMgUCSds6B_v8mcB0ZEbWVoE6diQF6QwuGbd2jN3zgztGqwWfY-7Td7-b7Ga6OL25nd2StLBv5uT_nsW1VB8pz4JkCQtLryu8PHq_sAjPNWY7s1KEl4HULdOlSFR24o30XE5FfecdzCPFRMuvEo8-WQmDGSniVAi8SOR0-rYu_hEGzG3rDt2OlcQQpkUvuDN8kzZxip9ZQtufpd27H4rcL2hkXQj-84gUhNbOiTyZjDYasZQ7t5T1YRZ6LK6xp4aj8mecQiLPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fac07199b.mp4?token=YcXJFDANFzkgnf5v2BZhA1Kh004xQN4LRhoG1ZcfgYsiMlaDnAyh45O7gZSeyybsTefQiGuAssL9iMgUCSds6B_v8mcB0ZEbWVoE6diQF6QwuGbd2jN3zgztGqwWfY-7Td7-b7Ga6OL25nd2StLBv5uT_nsW1VB8pz4JkCQtLryu8PHq_sAjPNWY7s1KEl4HULdOlSFR24o30XE5FfecdzCPFRMuvEo8-WQmDGSniVAi8SOR0-rYu_hEGzG3rDt2OlcQQpkUvuDN8kzZxip9ZQtufpd27H4rcL2hkXQj-84gUhNbOiTyZjDYasZQ7t5T1YRZ6LK6xp4aj8mecQiLPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
تو شیراز یه ایونت ورزشی برگزار کرده بودن که چهارتا کم عقل سر دختر دعواشون میشه و طوری همو میزننن که کم مونده بود بمیرن‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101921" target="_blank">📅 20:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101919">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQFa9wLOkfs8wq37dKxNmF_Aien_ak2jNQi4c5_e8zAgZAl__-fd8njjLwbdfMNqcoQyF8C3wylx9KlwvlrVUmnq3kotrV_Y0ljtQbAvJqFEd2tFujm058JkpKKWoKPR6UL3NL33xHjxFlK9lfajFtUGfolqTXIZ1xIyfrEBd5xceP3d6V9Ghp4uNs0Q4hnGSRQNH7mc8UjUItifTNLb7mJlTmduCtjMoLGjBVX8Za-ma6YO4tZRJsM0L89HBlLoG6nzNgXhvYKsoH62WyPDkEvJIWP_rt5APeTsh6emvBQm_xFNZTfxNsjc7XflWkGQFs6gdYEYzzUmqlJwQCklYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I5waFwUG6kLeaJsBKgWmPh2zwjMCMJ2wgIV9pmSK5nmw7aotXJsaD7vh7RnExfhRC4MKD8SSJkEX6dr-QJ7pdUVz5X2RM-22f4ZueHvOtHW9lDFOVxGBGFq54HE4t2e-dnPAD1ih7zVSE5u4cWySnvZUhMJqAq9zfGlZFW-N8JaTFYuhg7-TxunuDqOsYqlXmxEM4EpzD2w53-M9DjNPIUSwjRhXb5yr01YVANNTPiT5Vjwmi1bhPhOSasSMFbS0SAx1ZWeQ7JC6-E_B5d92teH-RKfnsLUei44J2SdQILoA948kVZgOCZVEf2FfIFU-LGRZl3fL6uL8vTRa8_DhGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇪🇸
فرناندو تورس یکی از آندرریتدترین فوتبالیست‌های تاریخه.
افتخاراتش شامل:
🏆
جام جهانی ۲۰۱۰
🇪🇺
یورو ۲۰۰۸
🇪🇺
یورو ۲۰۱۲
🇪🇺
لیگ قهرمانان اروپا ۲۰۱۲
🇪🇺
لیگ اروپا ۲۰۱۳
🇪🇺
لیگ اروپا ۲۰۱۸
🇬🇧
جام حذفی انگلیس ۲۰۱۲
خیلی‌ها دوران سخت اواخر دوران حرفه‌ای تورس رو به یاد میارن و تمام چیزهایی که به دست آورده بود رو فراموش می‌کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101919" target="_blank">📅 20:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101918">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKBCGts0xXYnq2rcELy1xaAd7hKPmaXFRCVUtyflZQrBz2tgYqEktJOAsvo4jiN29nUQxbBLkxUEEHccnnl1hkSqmgcu7_GrJySKcTDiJw_OAf8n3KLyourtSwFtAAcd5BYCyJ9VjA1tacDRjx7AWWDpPcRQehzFc7STrQ5HzAj5ULYOqw_lZ2kN2HmD0_mR-n13LDRzApppMRzE8xsS0KSE7I0S_o0oeCuxaem0JIlNqHJAo8sPtKPyvR8INHrPMd2FWe8GXFonNh4q1f2AtQrMirWsf6FeveMIv50_D_NaG_Ql66UNNH-DGgZaev9lRRqNGAThlqzNbb5214jpSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اسکای اسپورت:
هری کین بلافاصله پس از پایان تعطیلات تابستانی خود مذاکرات را برای تمدید قرارداد با بایرن مونیخ آغاز خواهد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101918" target="_blank">📅 19:48 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
