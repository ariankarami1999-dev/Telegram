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
<img src="https://cdn5.telesco.pe/file/lKncEe7zBz7hl2UtJeuPpgnKfuCPXOwvPTzoD0p5IjFq_XCbCXF3ItbfU-zhpyNq1VYevMMacTHrKPV-IBEasGUU9c7oPmmEN5c8vlECoEuB6Xi59ViWFUrTMnXAb7RdruTqKGleeFoMlIHUSOyjv4MO_ffBvFJtxmsUq_yZXD9SoTs3kqLxi9mYM1VK15cd3GMddzAx0yG_B35h0QgFOd0zcucmXMJlfBF81guHVdob8vnnbZL-mGNV6HTpXe2LkXo0zdp-MbJpkc3SkCcCJ8mdu-hKTAob4OZGjS_OfiL4IEiVZNx3lpPJvl1azLkBEWAaSG2pefYKXa6n3EP-aQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 522K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 23:44:36</div>
<hr>

<div class="tg-post" id="msg-102100">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f39b79d0a.mp4?token=J7qlKtS6GAwiirgo-nMbE8PIO2VszLFWNyIHRc1kML4-X3qCEd2zMD_c6YLnqz0oWZVSq3ugEGQFD4p-8dzjOGFLYX9by8s6bbrU4FTQrK0TlIuAyS8aiEgcpjrOXoaFVCkgdCu62dbTwedZ32Pwk_3sB25YddAJZu-JRucrIImzvs_nWJTRYDSnPv9OY6Use6Mvu9wkZtQKgB8G2sEDIJXzLPTJT4rm-o3DiqC5GcUGVJ_dJz79AREa3FEgTmpozUYMyNutKfH5I9ppWB8JOVSo6T49ZIZEIhISpgU3RVYqPIQ2D3kkAVK5xZsLMLh17NIiMYA9lC27z0fZNEE_rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f39b79d0a.mp4?token=J7qlKtS6GAwiirgo-nMbE8PIO2VszLFWNyIHRc1kML4-X3qCEd2zMD_c6YLnqz0oWZVSq3ugEGQFD4p-8dzjOGFLYX9by8s6bbrU4FTQrK0TlIuAyS8aiEgcpjrOXoaFVCkgdCu62dbTwedZ32Pwk_3sB25YddAJZu-JRucrIImzvs_nWJTRYDSnPv9OY6Use6Mvu9wkZtQKgB8G2sEDIJXzLPTJT4rm-o3DiqC5GcUGVJ_dJz79AREa3FEgTmpozUYMyNutKfH5I9ppWB8JOVSo6T49ZIZEIhISpgU3RVYqPIQ2D3kkAVK5xZsLMLh17NIiMYA9lC27z0fZNEE_rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل سیدنی لوپز به آرژانتین به عنوان بهترین گل جام جهانی انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/102100" target="_blank">📅 23:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102099">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RihQhs__3R7GtCRLZ3b7oMPC9lINxhNQhMF9mJMnLABW0L8mfatevxnZdMIKlvDk17YvIWyR2K9DaVerkxnkmynesqvuwL9j-_UF1Qg4AFgfDyPLxYG921XZ3ncMaYYqCYEQI1P78JXATLTz_I2dLCJGptwez5MK_upgy2Jr-a8z46pXRYlk2T6UcMNyQq2Ef6M_kdHrBWZGr9WJ5lnXVpvJraM4u_YVi1C9O-1xLcSIo9v0o8Jw3E2ycmFxS_JliIIuPDJmGotmF24QXWDISkCtnVI5Ub-A-wIoe9RNq_pZb0wXE-lysb0V-XQTgpY1Qc678CXCvwr4vCZcyGvpFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو:
جان استونز به اینترمیلان
HERE WE Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/102099" target="_blank">📅 23:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102098">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLyqK6id4V-t-IWovRQDl42kjBRwU1XpkhRMwZ1K3lbuAOyUvdMLPd98yL0yCGr_DaC-vsbuEn_asR-HsBBBk38C35sRlvjz5Sn0KOgLXrdcdxotBJZBloUhFZscDGY4dSyHglg2VRBbJovTwJx7h7RthOKljyurVw9phyCMD-NW05Su9-TCcQ3d20Z-dR-SLGy8fG7lZ67yN51OP61OByyG5IhRijqLXwtclV2i-1QjN_1D-wkXyA3hcpV09Zv0mopNHlV2T_kTt9wIRTfBf2EFrRnepQM01Ho5wWM5yJX_qOQaKaajwiCZLL_ArBqOK6By6jKPjK8UDqyaUwJtEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندریک و خانومی و بچه‌شون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/Futball180TV/102098" target="_blank">📅 22:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102097">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js9Ad0nTl9roSsP8ycnHHdeTI7xD30XLyHaElqGG_qosd-NuAezsmIBlxmzJBld3u9dwzb7SEPOyGAREylwsU2EFumvVWZ9S2tssDeDxUwdns89eOr-cJU-IzSBxBUVGsOYzTif7djIrSg-cbqS9bivho54B8NCAjcTIi_IXah2l2C8JQ5BTKnkwYGes7kgMmv1UBUDyKPbtPWY9EWqY1oNCTZIHLfvggi5T5HvpZBIerZiLm7sagS2lKjYAiOD96jDHLh-xJYQw7JnRtE4-Pjio7biBORvmPeIYihlrHPeGvqRu3CBfGc2PucZSN9ktrQ2arsyegj7WKLkrUKmDEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
جیمز ترافورد از منچسترسیتی به لیدز یونایتد پیوست. جقی 3 بار ادیت زد تا تونست درست بنویسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/Futball180TV/102097" target="_blank">📅 22:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102096">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wA0yZU_bjYgQrcImRTOsVWQ48FvZ-2SGuTpGQHiBWo5QjXX706EhhPAhjAFi8IxpcKEZ-_ajRXxA_bgnO4yfGhrpXUfR3eRXbjEn-iAFesmsqAPrilRjH09DvhD991E_NnGvOl2vYHmSWDAdaSB3gt9GdCQXJFafjv7XHlOo20A8vdzZrTL5tTrNWKiHJLZw8VQ-w9e7Fz-K_qqoefJC7BKSFT1ur9k1FmM4IwD0aB3mjDYtOHIGY-JlqwpWV7BEe8C1Me25Wcjw-Bs26HNBWy2_gMPXEPlprzef8u6onNKowK_DTGkS9qyJTxLb9WvjBczO_wVEE6VaFZVkDFvL4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
تیم منتخب بازیکنان آزاد در تابستان 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/Futball180TV/102096" target="_blank">📅 22:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102095">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🔵
متئو مورتو: جان استونز در آستانه پیوستن به اینترمیلان است. دو باشگاه در حال نهایی کردن جزئیات این انتقال هستند تا آن را به طور رسمی اعلام کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/102095" target="_blank">📅 21:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102094">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qW_cJnSrzYqdDbtD-fWJ-snZhQyYvQ7aYhm3IrigwJdcJg8O9pSK_x3UbXdLhxPbt9g90EMujuXWrPiWC5-BKigjPxpb9pfGePUyPCi-OJVgjxttWgsWtNID_M6l7m8NBkgkcij5bcZqdQk2gvTD8mJbuPEhvbUb47NCXBjuCvCtf4RaDq5B2vGLGUgxHY0Z5467vo_DY07Nbc2WIdLZhEOUbb_UEyZ4rpIEr4sJo7si_FafT-FELyLTKcHrs0tY1p0he9IJezkAoAamUJPJwYwtknQY1_fOO4LphkM2AHWzZcnoFyE5mOvcZSneLC1u_K_p88m8KFSmB0QsUHpgdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فلوریان پلتنبرگ:
لیورپول گفتگوهایی را با مدیر برنامه‌های برادلی بارکولا و باشگاه پاری سن ژرمن آغاز کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/102094" target="_blank">📅 21:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102093">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQjs40IEYNXOK3vqVKyY0z3wsF8XCgxcxR2q0v0k-L-E5bVLa4J222RZJb30DyWo2fm8LaT9khDp93gAMl9IM2OWJV1OVyM95gUUeY0uqu7Z4_Tb0MR2sspmjkhDvmbrPTpIRifNKe1xahExr3eXyIwbdNGXeIcLQwhX90YMBHZfbkkB7WbjPk6pM3IjuIUAWFnk_uJM2xQOeDYFYfXNDf4TwfXIBj9CNVk7Ctd9zqFKqwu2y21RuU7X3by06BBycdE2gAbqswbKccUzKPAdQPY7-PjPwtFG7WwsW6AO43McBFm79eyio8fWNsiTBa7yTauRLAmeMiEPMWUWdmB7EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو: چلسی قصد داره جردن هندرسون 36 ساله رو به صورت آزاد جذب کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102093" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102091">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZhcB9WE-W_-6ybd_nOwmeBA4C2JqGv8tzmRoHY1UkgZPRGRwYG8PmV7v1o3ElAqEGRW9hLLTYyPv9z7dJj7Qjt2d6Qea7zBQP4pus8imlGx6EtBzH65jdS10PxerdKlMQgLvuwD7vWFxLXrQMu_Vnz2VLF-3wt_HqqZVpof_OjHGtgpKzwC_Mw_G7heWjESKv3hggi1XtMRwnKBeliFidULWPSwPqwNpI_TgHCZFu3P7OEI_yajU31KLxry1diM4UHdKOjpcwKmHrgnSFG_e_xo7Ueno0iGfQojGDyuf8xvwH2Cp7qC2cGyYPVXucJ-iU_Ru4b-eEVE0jvyW6idLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇮🇹
فابریزیو رومانو: پائولو مالدینی و لئوناردو از سمت‌های خود به عنوان مدیر فنی و مشاور در فدراسیون فوتبال ایتالیا استعفا دادند.
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102091" target="_blank">📅 20:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102087">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BEWTo3NM6WoKMVaB7-V02yR4uYUmmA83gSaZbx3nnbb5sXWskAL_QHouS61sg7krnybGkRdQrdcLLQHku7Bd1RKZGI_qx_LI1iGVZNOl46830Rf8CGZhiVwToZaPokA6NlBC7CjuaUQtsr3HuciyyX8Pkle3HlACjc2wcSsl5J1yyYKveduXLsWHvO5PMHMPt55qg2rW09I5t2EtZuV-sBFcOarBaXrBLQSgeqPI-MzXnNd2p7dvO0XxAZfC6Tw8GFrqpGfSJ7Mwh-hHhTq8bjqXD5rbje1g21AJw1kizhrPaIEU8_woTh3XVpRDuTA6rj5ODJbbMjSZ_0wPMsmGaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dnu-JOERf7PjaUTIG0kaE5tfHOOAyFEiIKI3m2egDRWSqDnm8VFTKMJVRODTmbkNHUFV7qBDLwF10c2mf90K3iUk2gQq94DnMyCaQr6SCDMN6rVwyNFKkzukTogZZyMReALRk8GcIYHbrTm9kcsVO7spW9esfp-TVh3rQnv2O9zXDg5ExdB2_g4C9XmCjdCujkIJWQ8fJYhMT6Rb-UX5MmZycJ69ACeKMcSgRTNkWufedpu1Hr2VGmDYkKEUJouj_SDPgoEnRglwTb-ECxJjlcIWdIoUyV7OVn0615faUs9HzYUvK9IDgLrPayhfoeb0nxKTRYsfgnV-E213DaODiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbB8yRwn7hytYAYdczDSMLH4o26_b2obI01nd1CH8fSPFN7oBCDvMCezK3rVbXeApfcl_g-2Dyg43YuXkilhobHX3aPPo0Ytm8WmG4hkEhtkDNG1rJ4yQxbHgago3P7x9Bin49Yx_cnqSxQkwCB8kz99GNe5aTP4Ut1zRi51MPEmHE1JIP1jocPm5VIREYb9-un9cgTvvWusQFD9ZZhUAGuyy1flJzxJSlEjosTvCWqlckEcT7gvDlp09DhRcvpSx3y016VLR0FYXeSHPcojkUiIsPF2fMgR6_mTQYgR1pEo1HIJZv0Yb6D_vJ-ARifjkxtzudPqTOzKEgU9f2CTng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjbNAPQeFj--i2Y5rCXYf0uihH2yGe_Qpn7ANUjDcRT0AgpVhqLFFxZFRf4aFlOSXvTvDz0_Yu7PTwWaMU0Zpa3Zml9TO9Z5rQrArhGxwsoLdwRPAPYW5UwwE3hB4YuraJehBXBbaNptGC_IrPbxwm_fHHfolIkvAr_cciw9D__KDijeZSf4gv2fES-KeIM0igK-e9YFnBdw0hjwsw-xTgfI5eC_ry1l54vnulyPtwibHFd-HYMC4S7kQg2hTSEvQNhu3AjuYhCfqGiYKF9YIrtub75_gkj-a10nl-edYk4RHsiczDSxfirQpjuTRu5-I8cp08EsJRnRlKxPt_6kTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عشق و‌ حال وینیسیوس تو‌ جامائیکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102087" target="_blank">📅 20:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102086">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVrJ8-aq1pyQFk_g7_eEVU9rQ4Nzt1kQkMz1TR8n6grFFIt068Ig02rD2UbXEUwWwdYr7OFSHe-lgDtYvVHm7PljbS4Qk5sXJfQeiJMEr1AdzjAkZuJabNLwZIOoPn-ZgL46ki4j3Dp1Z4jhPqIGrAgVPa6bbZmdeMY4C3NmkZrZm8GPdb5MigvGbQmYh01p3CyuIuEInOMRjKvhmy8gDU6ye1GVPtChM921n_wJvGcB4blBBDlpEms0OtcYHL-4y5iEc5_fraH7jGdGL802GTxyhAV6eedNppzZc-zif0tpNdT1OmTbtPIlJ8G6IYNFhSfdWgbXkcYLlWn1GZTHAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
گلوبو برزیل:
سانتوس قصدی برای تمدید قرارداد با نیمار نداره و این بازیکن در دسامبر جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/102086" target="_blank">📅 20:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102084">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oWHam_NetwC-s1mGyBF2DzN-NLqZgmBoO_yCoRUcGiwkcAq69vNj7O0q_z6KERzCc3pfwoRyneassThyjjXvJmxnPbsGn_zh6ffb3xZIniVO9ljRTUFNAL_QC4CiwzpBdc9Ead4zjwIrjl-Ten3oG17oddLMtzw9MBRv8t7u691xSaKy1doKIFP4Lpp3AEn0Tkaa2KI61hFgCfQimDrB1LsYwxyKZFkJ8P-wpvEpVXSZT38Z5dxdBnmoiueVjuooA_hrq68rzt24kKOSuxPMV3GPjawfVMnVyk21kYABVGeGVreVOTREZQ28nfp3MTSzZxLPDJSTtX9mmj1RbBup9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBL75KG8JpU6hE0f1JJxiJjb1kdc5pvWRgnb4ViIP9k5P44oSqsZUDkIdyFm4VcELMUY4FV3VcIel_4VxHB1RR8u2wVOlYGfsIWT9cpiPXjuyJF1xCB4CHMkWCESeeu1Ks1go526cfgnqqZZSAdV-M1EUrd16aQhlms2koMt9HZSbOM6g7jI_45AKlk1guvOnxU9JMEa0V897doZRylJwXLjlk6W8noYZbQbypCiGrMWapZBSqmPn5vBotpVISZij5v4vkV_8SU7TlXPXsWQyM_NX8NJBhCzHKsF_0i_--IzuZtjTDN4AdwZq5KhPB8r_0k7QCWgwj1f0D1gdRQGJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره شایعه معروف طلاقش گفت:
اینکه همه اموالم به اسم مادرم بود، هیچ ربطی به ازدواجم نداشت. از ۱۸ سالگی که فوتبالیست شدم، مادرم همیشه مسئول مدیریت پول‌ها و دارایی‌هایم بوده، چون کاملاً به او اعتماد داشتم. حتی الان هم قبل از هر خرید یا تصمیم مالی مهم با او مشورت می‌کنم و این روند از همان اول همین‌طور بوده، نه اینکه بعد از ازدواج یا برای فرار از تقسیم اموال اتفاق افتاده باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/102084" target="_blank">📅 20:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102083">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgtSL0WLvMQSg0lxmyyuLbQifxL9SXDjROYRyBrARLeZNpz8Twte4wJBzSRU6Zm7b8IyEZrCKp4_KaUTHm4lEmtzs2WKEoAKkuE066KfNH8wzdo_OUqgbTPCEn-L5RRoFJa8OhAw8QHMIyn9wrAyA20iCeQmk1QAgcOZ9rb3cMc9fLEBKCtYq6l9ZldjXDx4f6y-woqWQdQVVzBMIkVyVt4djRGkT3tMaQjV9gAk5io6SU8jPnjVG8iNk3JlyARD_wCapfK2KWmSQry32NSd7-FRHmmjnr-UGsyIeNYJ-Z8xZW1IPfqUQwG7lAyoRsB1V0O1UF3DYNv0OFbQv3hgKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
⚽️
امار سه فصل اخیر جونیور کروپی که ظاهرا گزینه دوم بارسلونا در پست مهاجمه
جونیور کروپی ۲۰ ساله متولد فرانسه ، پا راست . پست اصلی پشت مهاجم ، مهاجم نوک هم میتونه بازی کنه.
💸
ارزش ترنسفرمارکت ۵۰ میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/102083" target="_blank">📅 19:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102082">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdHG2lJTESeRDGSnFr0Fghgst4M0yjENYMN-NwMnPY59nuBQY-mP1XXCtdwYoYLCbaluSTH0P4yspzeyeC_jEA9v0kNVMiGem-YbawMHkuLHPDB3xZTg5xdUW9hnPz8LNx6Um1nfuz1g9dw3nOxyegJSOvnMUcGjDJcsfWDsGp0fDd3xrOMvoyayqVApJSLji-O7CuzpTUaPBpgSJhPJ5UAKttHiLhv9nmXf0Rrbcv0NxTf1MvzVIiaEe1MIS3OLr0xQkacz80otnqSq28hRGXlMmHMAkfUOCVDrGI1Xa0P44KqEsBcO6IaLDlRLvgIsWB1GncogBRG4Rofca2YIgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدرتمندترین باشگاه های جهان از نگاه اوپتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/102082" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102081">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e948c535d5.mp4?token=PQYBlOVv5FVbRxT4VK9cbvr8mL22fodY4Qs5cuic0X-yCcvJNn5RilOCFUmlqwg-USnqvnEmpG4gyUE3OD61KXtKYQO-RkrPTtO7_CyvYmaLwy-qrcGOvRX71Fo-nnZYjXK5hzlSRAnKcM-3usKx8qVfsYJBKy70Em9BHubBXQrSSFL9Z17q4CsPepBx7s3vQ7mCT-zkBAKy3zupshg-1PDxnpkaXT3xM1ykaW5TmapshEhxYLgk_8sWIHwCuOHowY5svB9SEimEpSL5qzavZDLl5jOs7mda35_8DbnE_hqtl58QX5eW-S5fN2wi2BJUjtWQZch-tkIPP-l7LCKm9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e948c535d5.mp4?token=PQYBlOVv5FVbRxT4VK9cbvr8mL22fodY4Qs5cuic0X-yCcvJNn5RilOCFUmlqwg-USnqvnEmpG4gyUE3OD61KXtKYQO-RkrPTtO7_CyvYmaLwy-qrcGOvRX71Fo-nnZYjXK5hzlSRAnKcM-3usKx8qVfsYJBKy70Em9BHubBXQrSSFL9Z17q4CsPepBx7s3vQ7mCT-zkBAKy3zupshg-1PDxnpkaXT3xM1ykaW5TmapshEhxYLgk_8sWIHwCuOHowY5svB9SEimEpSL5qzavZDLl5jOs7mda35_8DbnE_hqtl58QX5eW-S5fN2wi2BJUjtWQZch-tkIPP-l7LCKm9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان کریر سرمربیگری دلافوئنته
از اخراج تو تیم دسته سومی‌ تا قهرمانی جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102081" target="_blank">📅 19:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102080">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
فوری ترامپ: به درخواست واسطه‌ها ما در حال انجام مذاکرات فشرده‌ای هستیم. اگر این مذاکرات موفقیت‌آمیز نباشند، به اقدامات نظامی قوی بازخواهیم گشت. ایران فرصت کمی برای توافق دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102080" target="_blank">📅 18:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102079">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7ooaVI_DvXbplMBM_mWIcSUaU5gp70ZrlGnwfejtpS3aK7AXhdlkoqIjZA5G6EpWHLT87iTRchVuHWurSY5KS-zAHwkynxPDzQsTT50lxCFUhzciut0Lu5135VCbMqFtNnDjX7h87VKefvmutT325_oJAeKgOUJd0UQImuNLZN_emiLSuYRVq1zc5bTt1VsiizA4ITp7lPzJB068tvnKqzmdOic4hZL1BaMvFSqfBP1_9jV0JKvzM_mfLu4uEINk6WYofq0L3lMIGvT-Z0Ust71L8k55HdCBU7MF9Hj5k1YNbKJdOSgzVyD_vgdxXdg9bPvjG6-ZH4g2SLrCsVjkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
چند ماه پیش الچیرینگیتو توییت زده بود بارسا به بازیکن های بالا نیاز داره، و حالا همه این بازیکنا رفتن رئال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102079" target="_blank">📅 18:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102078">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru09_HfwE2SPkORjfDJSIa6ce_MJooCx5CijpBlTU0ZHmOCjLcYmEYnOkI_kZZQHvUdI7SFWTDoJCQo3VE08ae-UU8t0ADsHcYp3K_G2aO44KECshjiJSgTFm396yIukUVv1o2KDqRUu-iSGt1paqiri-Z_sUm5-ockCsHsEABPRXh04GtsdiJV85LNcJ2JdezcTaj2T-QbvKwvVYcd1CHM3tgh8DMLaFaKjaiFLJdt6POkNPGDO15SQShh6EJAEj_SfIzwAg1KDrG8emK9N2l4_J0nCa5vRAx5DWCsNFIe-q0b1gyfPFlfx296hza_hlmlk1t1TsuqbfvxWSmO3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
امباپه:
ازم میپرسن ممکنه یه روز سرمربی شم؟ نه فکر نکنم، من تو تجارت مهارت بالایی دارم و میخوام که تاجر بشم البته بچه‌های تیم میگن تو میتونی برای ریاست جمهوری کاندید بشی ولی باید بهش فکر کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102078" target="_blank">📅 18:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102077">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-kaq3X8DHKyHrA40cN3pXJsY5ko5nSUGUi9gCNpWgOSY-VL6A5nKjPCm9jcO_f6hq14bgKIUAt8PdZ1nsKUranF5Hr720D-8dg8GtBogKM0mqtWhX9oqAEsTOM3hqhU3ObtaxoI69wDapLLlJcRtmE6zaw6Qdvdcbqen43ysxkw-q-XvARaLSA7jKMSYpCb2A2X0lGxXUT8uSh6yIKOeGsTanaKlC8sP7mR_H8J-MRZKi6yVLlIGsqPm_Ad-9V9PBdv4I-7tagLf1GsW_cdeaNb0IWUh_z025yLsKJQp-wVi4N5U3FHkTlTUb3S9QVMPqte-M2luEeg03DD8cN9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بی‌بی‌سی اسپورت
:
یک قانون جدید در فوتبال انگلیس در مورد مصدومیت‌های دروازه‌بان‌ها اعمال خواهد شد.
اگر داور اجازه دهد که کادر پزشکی وارد زمین بازی شود تا به دروازه‌بان مصدوم رسیدگی کند، مربی تیم 10 ثانیه فرصت خواهد داشت تا یک بازیکن از بازیکنان حاضر در زمین را انتخاب کند تا به مدت یک دقیقه از زمین خارج شود.
در صورتی که هیچ بازیکنی در طول 10 ثانیه انتخاب نشود، به طور خودکار کاپیتان تیم به مدت یک دقیقه (خروج موقت از زمین) انتخاب خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102077" target="_blank">📅 18:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102076">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLE5THPEjNFzyS6MBdKuXMoI0IFxLaDkEBYUnVobhk0DaUKXD_OPLlUUnYHEII95mMPEuZG7ulQP9rks7s3oQCs8QJpyEb9_jHEF72_z8-eirWjHDPJ5UGKYRqFBIwEiKDAlpSrAUPHAfQ0g0izkt6tbAGqZwHY_PdIZAN29QtZ-B1OWOFQh1dLFnRJmkJCgj_Z5VPdoTI7JdsgYXKGckvAYUtLgl0paYSg3JjU4QNJpJfq4VEmne9J1g5c2YZ_rPPxdymQs6cEceE4G-v1px-0-i_Q8LCN7804MusPbsBdlT_Nf8Ib3hgLBLwQDnbTyKOlLX0DLJ8mKN3M4Sbhnaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
فابریزیو رومانو:
‼️
بارسلونا با افراد نزدیک به کروپی وارد مذاکره شده.
⚠️
بارسلونا با بورنموث تماس گرفته تا درباره امکان جذب کروپی پرس‌وجو کنه. بارسا یه سری اطلاعات درباره شرایط بازیکن جمع کرده و چند تماس هم داشته تا وضعیتش رو بهتر بررسی کنه. کروپی بازیکنیه که داخل باشگاه بارسلونا خیلی مورد توجه قرار گرفته.
❌
البته این انتقال خیلی پیچیده‌ست؛ چون بورنموث نمی‌خواد تابستون امسال بازیکن رو بفروشه و منچسترسیتی هم بهش علاقه نشون داده. بنابراین، این معامله اصلا آسون نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102076" target="_blank">📅 17:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102075">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7hT0ZAEGd1c_n6nEFg8KbNNdbX8FQOX6mEO3aMRH9PnZ0qybs1GOk15C3s5-BHW9FO_5evC8hAoyVtkamftKJkK6tXdJs-O-Uev_FVsRHo_DPZVVWZVYI7GxxMSkanf5Vw8uTQcSBcIYopvQF1nB-BJU7gv1mqLIbms3ZTC49mHKJkc3OSZ9sTHIyHtyNP943FnL3VbXzNFtg9osSclqNN_UH0WqM0tFBQA2cgjWrJo73pjc5_wLlgHyyu0noXoldD99NItxI_31XwVlvuXctpiUhJpbs-GWL_DYJk4N3lmNyuPWdacFgGBo32LlG3d7Sq88CccluDBGyAZDn1zLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فرانس فوتبال اعلام کرده که بردن توپ طلا حتی بدون کسب یک جام بزرگ تیمی هم امکان‌پذیره.
📊
این اتفاق برای این بازیکنان افتاده:
🔺
جورج وه‌آ در سال ۱۹۹۵
🔥
🔺
لوئیس فیگو در سال ۲۰۰۰
🔥
🔺
کریستیانو رونالدو در سال ۲۰۱۳
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102075" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102074">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czCXJ5f93YtMacoNjSm-GhMLzXLbzFewc8I0jdf4mkFTQxxgFycrXrj6KoqnqRYBE7SPsOQAECgY5-wEI39DY4iwMIhYCWPqrCK8TNqbx5QtJnvdZ1tCH6jF95p2xEwn6W17-PM8S-z7ZZd6RbUaMJepjdLqodPx8pygbz-WHhGTpttLNZaffrc-OvsMtY6VuZSLL_U53CGJ6VAYpapbkdWXDKlw9cZkL549WEjz7tOcZeOcmP0BzE6cG8khjnVTrI_T0PdOu4sCoJWN98j5zPJWWexiB5a3gBf5QR0ZDe1Ph9aN9by37kvRqZg_dgzWXCm3JeCmUXWDm9VTMK6moA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
یوونتوس و پاری سن ژرمن در حال مذاکره با سوزوکی دروازه بان ژاپن هستند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102074" target="_blank">📅 17:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102072">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nm6Igoe33qI_V3q03ogwEOWM5hwbKN6mSFLe4pvbYhYf4aiCEuJ9GzB6sAHojQ3U-QHy0ZuVfiGjLY-C1izF6AUuui6DIFjkNtjODxHZO0R9RC-eyR6m2alrUJ26mON6pRYdc8ytsJ4kK_jQd5wvAP17CcExk_MaW434dsWEMxAmPG_HxkJjlVqnKr90UlyL_A_7NBZZ86v-HR9SxJuSEyfKiXxvPDNxnf-KRPvK4niviJBGM85Hg6ZqgvSHdxifUiPQqD_lOYw-oAIql0P18_dbRu0RogJKW81Hf4-o1FRa0GPhH6ODAKyVuSiL3u3DKhUM-7LwzGSH3mlCqtqR2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdANBG0UT5YHhq_refDmi7hg_DbiNfRTqZPssIOELD5rlsSlJPFdoIw4gSvmgWsRnopNEAWNrpgJQ8T3eLkfN9ys6OsfWWNemJTd2GPUkCRbPqxZcPO3xFMtyc10xVSxv-8hxdLwa5h27j4yq417K4oVlF8tLk9wJ6IZ8LJwVUm6pJafufmA5TGevCA4-MPEg5j2wJuFRJhuCsHBjK3VjAquHQiayRiBtM7rAwIbf8BhNKDSpGq_eX13oxPUELAgo-bs8VbhaEzhO9HHWyhpdZpaPCibeWhacC-hzso3qnGQ3P6iP2RNKLsExK0XHJ07zgkVmiIpWsPtDjgdoDAExQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره بهترین خاطره دوران کودکی‌اش:
روزی که رئال مادرید با من تماس گرفت و من را برای تست دعوت کرد. آن روز بهترین خاطره دوران کودکی‌ام بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102072" target="_blank">📅 17:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102071">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vy2JL5U7tDdGJ429KDWQN6otYVponUOQsSSt4YFQDa3WMOjQesB6O3QFKo75Pl81T2Vy4stjr6wtQLcCqmMfsibqIRNQiL2e41glUtvyL4y4VbYP58weK_Mbtp0oITBmBrnjqPcBzfNKeCmTWoP-l1xxDPuY8Gnhz11Obti-CFeznb2eBylt5RHERAeINU8C5tegaouWMCIi0uUGzPsl78DkfZefC5SVfF2WmAn1E8pqqA2a8dSz-aqUCsY_f-TIrxHLOVLqzBaEJByk8NoyEz0oShxeSkySE4vqR-L7RH__WNgnjj2D5aFF6f8DGSQAPaakwicVMoFxr3BkheWGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حضور دیومانده در تمرینات لایپزیش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102071" target="_blank">📅 16:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102070">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3120e668b.mp4?token=pn1QmsvtjTrok7mgIEovbSmLeX9yyJ_0JQTsxAtVWn9Zv-M3pZKEOHR7P4jqK7DvquMxQ3WY2JS16PtLIekMOF4fACjhapsf7XQ7YK-HX0CFf-Z7Y8HBtUQjj1iXd_bpTuh4kOYoMW0cHLgNxYOGVr-9ZjuOl4SVcTo_QqPQKs2rvo6wWTjnv7pWmR0uI8p-ZsOGvOPFfO9poXeYh_pW5R-61P1XkVdP04fssYWKAYRCgI60IF_cHNf9_gjZUShf-kdM4trwBScWSGO1XxPAVxh3lWmoCMGqvQaQJ549eR9eOKXhaMygYuTFc0FyzDvhbzOtofXXNPXzmvyWJNpRtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3120e668b.mp4?token=pn1QmsvtjTrok7mgIEovbSmLeX9yyJ_0JQTsxAtVWn9Zv-M3pZKEOHR7P4jqK7DvquMxQ3WY2JS16PtLIekMOF4fACjhapsf7XQ7YK-HX0CFf-Z7Y8HBtUQjj1iXd_bpTuh4kOYoMW0cHLgNxYOGVr-9ZjuOl4SVcTo_QqPQKs2rvo6wWTjnv7pWmR0uI8p-ZsOGvOPFfO9poXeYh_pW5R-61P1XkVdP04fssYWKAYRCgI60IF_cHNf9_gjZUShf-kdM4trwBScWSGO1XxPAVxh3lWmoCMGqvQaQJ549eR9eOKXhaMygYuTFc0FyzDvhbzOtofXXNPXzmvyWJNpRtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
عاشقانه‌های رونالدو و زیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102070" target="_blank">📅 16:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102067">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/orUoyUrhagI10YDYWkyYeyQMy0kGQj3JrY7QTNQcyFVnEdRXezLAoe-Qlxr3KNqhjG4OBO9U5jl80Q0arc3_7CB06Eswpr0FZqeGRnjdcw_avDn1p_a1TEQoio0yq0yVeed068kW4oZYmJKj7Um4U2Oq0hBmMSmTWjkAgckyCsLpvm0RLZ8zXY5GgkmSjPkywXSnQ3QlcdZEihnYq0H_tDuwaSmnAA7-F5Ry1rprmFu0Ro6IHkQLz7lM0_p-Dxo1q0qVHPkwtYUxpLbtK1DFMspu44SSZNvL1eNS_Cm3xQBBZ124VLWsyHYWILx9qTmUB2SXrSys3X0i_pDiV2QsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hz0DKsiVEbL-yb0JqYu3W4rWGK5xEjTRd5cyhUGbvHDXivqXiaFYxgZ3BXDKE_WKWZd_44ugE-aHwK3kpt9IlI2JuvexxCpnBFhz9NpQsFFci__hn1pSLcHtbvLqndhS_tWumEigkJM785xzz7eZni0uFB36vihBTPs8Mjq8p_NPN8M2q-_5lLy1ttjeZ2LJ1AOJRccTrQi0TrY90Uq5XhLFIi1QK00Z0vTxAyCq3aWlgLn_hLHhqbp3lg42_CHA6V3AgkQw7JD0L95qOMgiJR2QMa3bErIW_DgTBNts4vQqORYVFVBfd36deefieQkf6cUgCtVyl33fyw6XScEyhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A4D4XFOCDkFaGoVzJOqYAKtBUsi4pFNlCASqCmqlUqtZvFOngq5M33H7ZWE-Uu6wGnBtJB8aevnQYIcbYPzYKXDTghTMccZkEEuo9SZBKoaEazaVvEwE1pt-5afNaLGwIRdQnytryqka0WJFidRF21qZQrGYgp6_-JJjOR6YMyj18e-1uFBCo4sbKrbmuIetiG9s4TFpPDdv_eYJrBYb5JTesIheLMmv41cZEAgICGrxJes6OI9dDpKmPk_tfeRhKXmLSVG5qNj88kcVpKi5eUa2w8j7IOvuqyxmtU3aavJjHQRen5Kav049cV_E5n4Y7Kh5irTiPNVzJL5IIOYIRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایشون که تو تصویر میبینید مارتینا گونزالس دفاع 18 ساله بارسلونا هستن؛ حالا هی برید پیگیر یامال و رافینیا باشید درحالیکه اصل داستان جای دیگست..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102067" target="_blank">📅 15:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102066">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
‼️
انتقاد شدید امیرحسین صادقی از مجری خانم شبکه دو سیما بابت انتقاد از قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102066" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102065">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f32263398.mp4?token=H2_Q_-EuvdZbJwsLT8pf8Ag-5pgq3jNQs3stmOK0Bb9iYsJ8x6gRzyukvbOrakh3fyYll7SDZGpUwqVYPX_S6nJDPM-CSDiEAmu6XT_8HDhLC86AOcLeLGk_ZB1evlFoYFTbFWEINsMw6fOpaoBsfm0KIRBJHl59mbidcMLjLCxx5lIgJ0JEEAj4Lceqki1NT-qdrdOeu6OojUp9vVsg1Mu4C5iKMJGGgToSl84dGBNBgmKl-hCPqHlI12SMUyGzgFqWizYzJ6e6DdeRvu1or1L6DT3Y4tgCr4Ya9Y9qHltE7ahhNf4Lx8v2xHh6NMM3qZfg6khB2NymEKkZiIbFJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f32263398.mp4?token=H2_Q_-EuvdZbJwsLT8pf8Ag-5pgq3jNQs3stmOK0Bb9iYsJ8x6gRzyukvbOrakh3fyYll7SDZGpUwqVYPX_S6nJDPM-CSDiEAmu6XT_8HDhLC86AOcLeLGk_ZB1evlFoYFTbFWEINsMw6fOpaoBsfm0KIRBJHl59mbidcMLjLCxx5lIgJ0JEEAj4Lceqki1NT-qdrdOeu6OojUp9vVsg1Mu4C5iKMJGGgToSl84dGBNBgmKl-hCPqHlI12SMUyGzgFqWizYzJ6e6DdeRvu1or1L6DT3Y4tgCr4Ya9Y9qHltE7ahhNf4Lx8v2xHh6NMM3qZfg6khB2NymEKkZiIbFJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزاله اکرمی بازیگر: رضا عنایتی کراش دوران نوجوانی‌ام بود
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102065" target="_blank">📅 14:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102064">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lwl5GwU2_WPSyeLM1apW0RGYIAmjIzoaG4Y9cZECh5E8YhcZu2p_QJAwTHIefPEpGo93op2Y7ttC3Hjm7PJvTlo8PTEFT6fa7XkTXkBYkROryu5e7EHHSnrHA2G0XykKfv5iqQv-5_5s9rZ56B-aU7xvHiTWfU1vUte6m3ODBacuijZlYY1raeMXkU_Xy3kUcJ5GjEimO7KwJXH0Yzfh3Xqm62odUxpbX1GAhniR385L6ngj6a_KZpqEfOzthSCSzjoh5PvtUpzxoLM2FFt4vWL1l8nUA67zsgjgST0XmoCq3liUepDph3WatTu6QqW5qYxmPEqAmhHaBXioEP0i-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری از رودرا (ESPN): رئال مادرید نسبت به احتمال جذب رودری خوش‌بین‌تر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102064" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102063">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQUrjA11MZubmEyqcAn4iqMlwLNQvajPRbX9M_V7uKDvWYXrwECak709F4RRs0vntqirshjMv3V2OcMjQa2cvJGxJeKipBYXEdNA6dJSkmy0RP6-iIYJXmV2uCzrNEKCB189WM7_-FcS5w0NeUeo9tQ8zQebRmlq90c4KcvkdzVCnT5CgiGp15Uryn3uhGJMhbs76AJA4tw4FvJwCicuZCzjiwyEYO3H7aF034MWpsT8vdfdNR7UAuhSLXl2qutA96yT5SgUe_lXxo9ZOW2KzgglrDMrtZ_TmMw9VtdZCe9_MQsn1VDQQR5Ougj6OrBi-S55pM4nQYcmEjruynG2jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
اسم کوکوریا تو لیست رئال  برای لالیگا ثبت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102063" target="_blank">📅 14:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102062">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sChJWF5oIqWhzwWNzfmoEAPh0zNCaca8H2dbM9QBESmABJVxkZlWLKFD-FtaWuTvmUeoNUG4zRx4oOlVMmUpX49nhFcTk3DqAR0SvAnJxmdZUCWb20-rhQTf-V8oft7SFWCL2_AZjGjqLp-_XZAkEQj6iGdg7A8v_-mmyCoIJsbKM2_IjZSTBRQm_yNpRMus1qnrlIjCX6FfdYatryUaWDSWwyxvMV9rIfftolJKGtke87OvNdR7CE54OlPNmizb76Pz5SnSK9G5A1SCyNqnPOSeGEhVX29zcZM5UMXXr39km8oSvZ0IPIbVjEaZfCSXoqByPKu19NKUdBV1qaxpYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
مقایسه عملکرد نیمار و امباپه و هری‌کین در بازی‌های ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102062" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102061">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2084d796e5.mp4?token=Ppuw877SF89XUEkTsp5yrY81aPaMBifrt8rHcuxvTZp3r0UXwvxpiMfSZ6GMHhKGbM-95C1ekuse2FkHvBSbLe-NmQg8zV15Q1dgPtzIMvDDETN1zKhRPSBoWu9MePSRSbA8LmP2ciIe_H8BWEPql_PHNcj9jrc5tolXgHoeoDCmdY6st-TDGaOabJ8CcbSk-ubkecZhkLbBKCKMn0IRCdwmL8R8QXSFSWuyQyW2n8go1wu4IX6nV2Ux2oJZ8QMQKG0jsh5tD5ODYKvqaSInrELeEUdzKYYSCZTAuhX4PLuTyigECPVRsY5kSA0yBzR9LCuloNgDotolULFo3_RIzr1iVg1LCexEeKwlQx75jeezp0PgLPyVJDchwNJpR1sxYPmBe1_ZXTMZL9MRx9UH2D_AyLD4zYYrBDZTkNH2-b2MO6hJmngRZfMBL-9NIMHmqJ9mk08VaUoO0Opr5JkJE0fBxrnWYfgw-_NRTQqxC_gDHxV4a2-Afzlo6RAOjAyP0vKa21rdQRtZVmhk1O7ZvT7kf6DZqNGVbUQf6kta0nBlIUzlCN7luIX1ZB0I0aS-3T_dvHaTfGhxDtWLz56MpMhg65_77SOayEK8tYK7kBnRT0FWpary8MBBqjv1XdI5hIffOZXdnmSTUNRQQ0BL-_M11XHMkEttMYyqPsfMEYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2084d796e5.mp4?token=Ppuw877SF89XUEkTsp5yrY81aPaMBifrt8rHcuxvTZp3r0UXwvxpiMfSZ6GMHhKGbM-95C1ekuse2FkHvBSbLe-NmQg8zV15Q1dgPtzIMvDDETN1zKhRPSBoWu9MePSRSbA8LmP2ciIe_H8BWEPql_PHNcj9jrc5tolXgHoeoDCmdY6st-TDGaOabJ8CcbSk-ubkecZhkLbBKCKMn0IRCdwmL8R8QXSFSWuyQyW2n8go1wu4IX6nV2Ux2oJZ8QMQKG0jsh5tD5ODYKvqaSInrELeEUdzKYYSCZTAuhX4PLuTyigECPVRsY5kSA0yBzR9LCuloNgDotolULFo3_RIzr1iVg1LCexEeKwlQx75jeezp0PgLPyVJDchwNJpR1sxYPmBe1_ZXTMZL9MRx9UH2D_AyLD4zYYrBDZTkNH2-b2MO6hJmngRZfMBL-9NIMHmqJ9mk08VaUoO0Opr5JkJE0fBxrnWYfgw-_NRTQqxC_gDHxV4a2-Afzlo6RAOjAyP0vKa21rdQRtZVmhk1O7ZvT7kf6DZqNGVbUQf6kta0nBlIUzlCN7luIX1ZB0I0aS-3T_dvHaTfGhxDtWLz56MpMhg65_77SOayEK8tYK7kBnRT0FWpary8MBBqjv1XdI5hIffOZXdnmSTUNRQQ0BL-_M11XHMkEttMYyqPsfMEYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
درخشش‌های فصل‌گذشته لامین‌یامال در بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102061" target="_blank">📅 14:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102060">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap50rvTiVleX_PK6zusjXmdq49VexkkU5OWO2dnuv22MO0cBJ3Ka8ylrKSOytsrgmyxFTAIp12qZmQZMB9An6q5Ul9Dh2TV6F151hmdgHOIhTZuqR-EvcJ6SxiT4LKPDv3iPFwhz5GV9LZIBpcXrmTXwXAviJN6At4KBmv0hZocs9zHZg6kr68JislmNj_j8hsk545cLGuCu8bnUwvJILihN5oDddnW57UkThFIs1BCLsdVMwlzGPAY-01i2dz8wwPWa5MMVJo08mAmWgwlbtmKAUy5zhF8Ybel3gtYFoolnRG7WFJLQzF8AGSm1KTN-f7nZth_fw5TsS5Is4SJyIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽
لیست بارسلونا برای سفر به انگلیس برای پیش فصل با حضور ترشتگن و دیونگ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102060" target="_blank">📅 13:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102058">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLipo37XpQRJjMrnscnAYXoqEfri71pujDL5k7G6bl76kaqnvqlgACOqEYvfRbwBVHteqZirmXB053r1AaW2MPROLO9F60BSBzP677rU1X2kdbqyfqswCMFSSjDmLTjE3ONt4kQQIe_fWsBqNZ7XIoBLe9pqV2ld_i9ULo12ECr7lOGT3WgmY66ntFrxJ5glanmx3z1tebaAK4srROS9HRc060ropQRHNUQm2nPkseHBq5cWIA5T_P6kNCTrbewPlrwZ3fBrhXw30H4H9TccqgNyZnxW5DBrZRfrK04AYCnaXYy45pp01qDYwCSH-HhQ6EubzqrGhtWa3CwUgzcu3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/olfgU8RdiVcLsHfeiGMsAO7ClXoANC8-2Xranav4Wgk18KM5UfNlFBHX7Habs8zabT2ETZpab2eQIwVWKO2W1YOwl9-LJslyRgpp3PCUB5wINz0S4WirdASasMNUWnxBr-BmQ4raXwgxlerM_mrUsnFC2ZaKcJhYWBMgqBgG6RGtnxeHnwMCfIzYI_xxmkTlAkoaPLwLLLz8CksXCGEgfWEnnjTXnVyLN8tt_V8EueOCJxdbFt5xj6wMzbKs6f2at1jcUszFw1cfB9053c1LXatw3tz4kEslnAIxyPzxhptFQ9BnwPtfw9HBC_CxOWUcMGRK4ocYZ6EcTITxlavl9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
نیمار:
وقتی در پاری‌سن‌ژرمن بودیم، از مسی خواستم پنالتی‌ها را بزند، اما او گفت: "نه، من برای این کار اینجا نیستم. یا خودت بزن یا بده به امباپه." او حتی برای هیچ‌چیز هم بحث و جدل نمی‌کند. آدمی فوق‌العاده آرام و صلح‌طلب است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102058" target="_blank">📅 13:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102057">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/772e430691.mp4?token=fcPgqUSZhspYBM3vl2Eil4EdKa-vFUhMbuyOmtsBPiyHNf0B-jWzAgty0Rd-o0uLsBogTXhtOSx8I-tyZdBojAx5vSUs6DdU_H9ZS0vmfhtb-dTaqwvU2x_ZIw50E7FjAikErMngnzhL-5KhyuNnZX2b1vUC4bUC13m8SUkpgElCbtkT-ts2CZSQP7Pr3q5pIx1dHDIbuVoOrTCaydSbc6Eb3G0010BEb6NLF7cGFBDTQXatPzq-4itIiXKfj_KUkMSr9YhEBC1fWM9ZL32k6XkTRgToAVvqC95G0K4E9cj1dFjbGd2_5HmLG6iJUESLuuR_33kHhkdYvSGjuqWL_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/772e430691.mp4?token=fcPgqUSZhspYBM3vl2Eil4EdKa-vFUhMbuyOmtsBPiyHNf0B-jWzAgty0Rd-o0uLsBogTXhtOSx8I-tyZdBojAx5vSUs6DdU_H9ZS0vmfhtb-dTaqwvU2x_ZIw50E7FjAikErMngnzhL-5KhyuNnZX2b1vUC4bUC13m8SUkpgElCbtkT-ts2CZSQP7Pr3q5pIx1dHDIbuVoOrTCaydSbc6Eb3G0010BEb6NLF7cGFBDTQXatPzq-4itIiXKfj_KUkMSr9YhEBC1fWM9ZL32k6XkTRgToAVvqC95G0K4E9cj1dFjbGd2_5HmLG6iJUESLuuR_33kHhkdYvSGjuqWL_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این جامی که داری میرینی توش آرزوی خیلیاس پسر جان نکن
🌟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102057" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102056">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF-DoKQ1xjCfLvjdn6kaPyDiAXRmb3Wdo04SJxLadjs3YSGk5plLcSF98NFyCPA_z6HAEriegSrfCEwHnyr4-tfBClyxU-gmcqCr7xBGuYvfxlZTQm2eLEZ-5WYweR8dUC8auW9k2UvHDTTou041g_cqrUunqydzgXLaJ33Egff2EZ5i2IVl5_oCa0_xFTUDoo26Vn2WRJe7fTFlMKL30KdPIkaSdQPnuJN31enBGfDeaU4q79lvBh1w08Uz84H0ao4SQ0kzfPgAHoTfD5d_lwyuNhDSSg7H67cLQfqULLtOpAUmune8wfmfgY3HHN83dtt-cAbeHvBTMffhxdL4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇦🇷
بنر هوادارای بوکاجونیورز برای تیم ملی آرژانتین:
ممنون بابت تمام این شادی‌ ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102056" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102055">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
🇮🇹
✅
پائولو مالدینی، به عنوان مدیر فنی جدید تیم ملی ایتالیا انتخاب شد.  HEREEE WEEE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102055" target="_blank">📅 12:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102054">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vvobh6ZwsIbcCtaZ_JuWE3z5Lc631h9_nv1vmawpLIDD62GPJHQtyJTTDdy8srPyVnoktifX6FEo00EeTyZLMGlajghm3-RdomOOsf4WVwjGx2UKjXhthvH-0z-DWSLCQGGezC5iKFSZf6XvFJi35O9W-Jr08la_B9mkAXsa8OWcYnvIRUXc8kNlOR3aDxP32LZgMKd4ddp4ud5FQlHX5ANIxcLPAxN9oM0DTuWEgyoYVZc9MJKmXto1gmKvubQHLJYhQ5UMj5tS0MisSx5k92bhPxjhUWwv-vwr0WpqLL0dQEioKsddVK3U1M0Ku8hdnFoH0EH-6rhv9MTcQel0Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
الهلال به کریم بنزما پیشنهاد داده بود که به هر باشگاهی در لیگ عربستان که میخواهد برود. اما بنزما این پیشنهاد را رد کرد. این مهاجم کاملا روشن کرده که هیچ قصدی برای ترک باشگاه ندارد و این خود الهلال است که می‌خواهد او را کنار بگذارد. در واکنش به این شرایط، بنزما خواستار نامه فسخ قراردادش و همچنین پرداخت کامل ۱۰۰٪ حقوق باقی‌مانده‌اش طبق قرارداد شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102054" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102053">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8d8lriUFp1rWss4R0zSynVZg4vinY6WX1NpevjKlvtIHWNBLD38UQC5Ck-PkPz88jjVlFv7Vds-dS_ejmH75rhvnzmQ_qwQJhRmRtRijCaScunUw7e-2KqX9LXzXWlhUin7qcL5a4yIdw4qNa1-YEkCduJIFzl2xUjfN6qDDErGcH72zrwvTdWwpYAX_bUa2K2_qBQqvC6gYtvjWwm1wcIvWAnfGF2I-50pyEGPW7uWWUoi2JgYIMe_deWcWrS8CWKzvpTsIQ4OhFh13_bsBU1dQys_Mh6lvuXe0IXnFQ2Ty1mt7-J6Urn-mcgTo41zT1Dn52Z1WNWvG_ooQLhOWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا رودریگز درباره اولین دیدارش با کریستیانو رونالدو:
قد بلندش، بدنش و زیبایی‌اش توجه من را جلب کرد. جلوی او می‌لرزیدم، اما یک جرقه بین ما شکل گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102053" target="_blank">📅 11:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102052">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PE8iDWG-zbctYs5ZxyvxCDy7XJbUtmLTzSWn1niH0pPEAPLTe83HdI8RIVqpeqx-P2FSoS2ilddlUwaI_IDwHJnC1dIl8wd44qc_XtHWqc53BuRlhGVIpHXNbFSwW014NerwfmuFJXo-v06NZLE3SDZ9u970PjIugHPPWbxT4i9PS5iZaVvdUS6omFM4P9dFwem2U4RRJ-lLanTUpxNv3hDZbaEYvGYHg4iNGo88kh8FC8ZWvzqVYZxIoVCoXXqwKm-cQetTlatfSYBJsPAd3kS1Y3uQXZ13QWSvxo3Vzdvl7jBFYJGP8D6yaoEC3KAb-D8EoWq8pEobiZ3bB7Ifeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برناردو سیلوا و ژائو نوس به همراه زیدیاشون تو مراسم عروسی گونزالو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102052" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102051">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/809e9f523f.mp4?token=CDO_NVhfQOpzqKpnLFJW_iF_eNeCJa9bXzcu6JUbG9rnoOFbyG4VSeXF6iZhWza5CNiRBM9N96u5UhGtMYbjwa6FDF7CkDEzVvZAlL9XeNS_BtqielsPxZDfDRACe4_wEUqbpkFjX1ucgJey0_naH-bKB7wWj1KWApo1CsKkGKPnNpRReXIyIjaM1JlFLeWUxxddKLHdCBR7mJ7A_rLfHWYUYBzw68aeOIEBKIfU800ED9pN3T4uJqYvgEY_T__meoiEQvJ0ZcYhqlt9wtvuuaP17meM0BWKZoKQBpSupz2RDM16Y-pqzIAG9AvDQovb2-kYssm3fnHp3IdDhrTvMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/809e9f523f.mp4?token=CDO_NVhfQOpzqKpnLFJW_iF_eNeCJa9bXzcu6JUbG9rnoOFbyG4VSeXF6iZhWza5CNiRBM9N96u5UhGtMYbjwa6FDF7CkDEzVvZAlL9XeNS_BtqielsPxZDfDRACe4_wEUqbpkFjX1ucgJey0_naH-bKB7wWj1KWApo1CsKkGKPnNpRReXIyIjaM1JlFLeWUxxddKLHdCBR7mJ7A_rLfHWYUYBzw68aeOIEBKIfU800ED9pN3T4uJqYvgEY_T__meoiEQvJ0ZcYhqlt9wtvuuaP17meM0BWKZoKQBpSupz2RDM16Y-pqzIAG9AvDQovb2-kYssm3fnHp3IdDhrTvMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📆
🇧🇷
۱۵ سال از روزی که نیمار این گلو زد و پوشکاش گرفت گذشت:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102051" target="_blank">📅 11:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102050">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXBzkahTACktfDmbaMREq_c2mx24Q7UcbKhoJNN3yg5MAikI1_UNru1hv16C7KYgpqpOQNTApnpTObZwFCEniQ7B0qHRzTbM8I9_5IkX5Zia_kKG7GlVrmhgp46D5e5gskTwQeDQI2HacDZBJfxtbpq8A-iT0zIUeGIjCd5Bzmqv2y1F8F7UzI-kxY-_autI9QQJOqtT-kqi7Txt4687TNvBXGtoDoRX_VVdl6msd_SZcC7AodOHG8yCdRXLU09yduix7j-LFqGmSj6tQhvzH1ku6grAKKD4hq168OSPpidRxfqWuCHYJxzaWMSRq674iyPXhTyK-NvRjN-xKpXW2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
منچسترسیتی مذاکراتشو با باشگاه لیل برای جذب ایوب بوعدی ادامه میده. مذاکرات با باشگاه و بازیکن همچنان ادامه داره و تصمیم‌گیری در مورد انتقال او، یا در حال حاضر یا در تابستان سال 2027 انجام میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102050" target="_blank">📅 10:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102048">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q8QBgXraqA5lLO40ClZ5acf4MKhr40cK-2grPh9qvCJXGM1NQDHxuP2eYkxHvnKJXx3mBshUjp7fVQV5WUZnVpjVi6AQuDHmtoFvdkuTlpvuBfBRkBTHbeXaP0-ozVO0fseB8k-cyHKpfQ7n7kmP1Fj9yVoO34sC8kivTIhrDNc6hRt-mdUfF7TfdHkhi6fz0_C0NZ0JqWF0smGbCaefdrWqywpHZQLi_FJZA4uh-5WOPr5PfQe5E5R1rwYKA4NBVNQlGeN8BA2l8jkCjh6IC-z66gh-pLOHBSbiv00DWVG9kqK1Oyfp9x0jTX4MLaq2bZ6zwCtfs2CWlMql0_6DGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7slX5aeaXQKWwvk8DsAaMFuM1MIdBZ-ZRC3F5yoHlCaC-hrvtKjI9zxTU1hY74gYsTtVVSqdg62-OX9cKOd1sSAetx2Xt4cYF5KrC_Z6LI1Dzl4Z9TJToMJch4Dxz6qfzatM6XLMwW5LUBEB4EjdY_gXRB5CDVU72wrd2_sr83umEQmHmWrSErmDi-TZw2PmzuvnKLwatKPiYhdpOyjt89wi9AdOHtbKwdauWz7_PyN5wpB6NSpv543yttTs_N295l5v81eCvSZGuvx093d5jBDBxoAaynupeWnc4XXaxnQeJ67nD4un4llCZ_afOmOtx4jYoxVetZG82mr3emJMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جورجینا و پسرخونده‌ش که حسابی باهم گلف بازی میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102048" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102047">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxhVkqOK5a6TYklFx0wF8P_SS86z-F1Y3hQOcNXMIdtD8xRXGPpcZm4KZOhMICergzU6HQs30tEzKAf7ZsSlptUzhfLsScF-H9xiyCnUfHQ0qkOQAp4bfXFuBXjC95YcHHzUgp8VvnjnHAdsquEu0BrxgZhsFIqf2jzNVZ6WX2dK9vWSeMI85PMLb3cidYx4wXdQYc5FVt6R4Da50m0L00DFSwceBYWhJ_VPN_d3w0gwLe_RnZu2MDg92Z6HD_bUqlFi7I7u14AdyW5-N74N5mP2s6qHdpvZeOGyntG5L_LDbC9R4XC-RLD-LDycTMeJh9WcVcjBD9ZBqUKQtsxEuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
الیور کان در مورد کلوپ و تیم ملی آلمان:
شخصا فکر نمیکنم کار در تیم ملی به آن سادگی که خیلی‌ها تصور می‌کنند باشد. من معتقدم مشکلات خیلی عمیق‌تر هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102047" target="_blank">📅 10:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102046">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NURNRsT6yszKkAxPVKnMXd7VA2CsUSUmxLXQ_Rc_U8vqLmP5lqJ9WVPoVH6BcQR4QpfK9r80jNLHDhLMSHx-UuTOuG58ALgxzPJqvMTRH2-uMLj-4yVrl6xwjGGdbl9IyR-Dwxri73aBC4rpRP5LAiRyixaDxEvqVhrAUyG7NKEcT_5ORPQ1TMJiq-SxiMzm9IjSfMxZdFtWI20ixDFima_bIJbOi59VKES7F2i2LouZ7JDPfRNx_09YQ5UL68e-bDl5K_8r9p-_iDdBlu9-so92E2VIZnzPc0wfl-M68sHEviUYqTubupmXBeGk52EX6nRgzvimD8sQWaJdvPhhZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
وینیسیوس جونیور فصل گذشته ۱۴ گل و پاس گل بیشتر از هر مهاجم آرسنال ثبت کرد. او می‌تواند خط حمله قهرمان پریمیرلیگ را فورا یک سطح بالاتر ببرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102046" target="_blank">📅 10:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102045">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7WOLEUlVVpcj9MBRSa6hfLuTI7yg2J7FdredtZsCw2aECk91cVqTpNkxMKyR7_0VuzwDCXOo9VG7UPEROsWjNvA0ZfGaQZC-HZ8p20IufsdByl8n1y9TPnqd__0hfHIOKlbFc5rE3FFH-3Uk0JyKOoBnfztD01g5CbKQbEo6CJnI8u1HoLNVxZVYNucCnmLCbZ_gDzHlLE7FCZvKvAwUDrsuVFM95a8Ruii0lQPG-BB3397M9RAFX3heTGjRA8S7LgTQWTSr-PX9MQAkH8oDREyxhZwcH_izu7mNF1yGZth0ZlX11VCPLs7f6HgZNJBjJRb7ymytESqj2SI5RAUqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو: پاریسن ژرمن تلاش میکنه بین رودری و رئال مادرید مشکل به وجود بیاره
‼️
🔺
🔻
پاریس از هایجک شدن دیومانده بسیار عصبانیه برا همین با رودری تماس گرفته تا اوضاع رو برای رئال مادرید سخت تر کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102045" target="_blank">📅 09:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102043">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MHm0LvAzCDGaLqLu-lrKWY4ZPHT-yhgonYcZywk0IOfpFou7uyhgsiQwPHymcOWla6bCT2am3npyckDa3z1NkpqdzBMAjXFcfr18locFu5tnSf8MbRu0D1wAi3OtLaRixSgcX0FCZy5U8rtPTR1Yg5lV1rm6IXHREKBTfumuTaq4DopzPAiox5Z2SFqaAMPsx_OK6FLmLa_HKZdhAp2klwWLWW0agpr8Nzym9uBvjO111IxGjI1AWogwVBQGoX-EbURP3R1RBZZqA9PCQEwvc-z2aDkc4f1XuIcAXoafGQvEyFBsjqEu6SOfPKSHe3PokWlOyMBMkxdv3YoJxkm_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nupzd1iYnQp0TrZ7LkYBVE-o9yWJrAG-gTiX9Idq3JRdYskMW8f1EV0-kXK_NPeT8ANhU8ngBjxVC1xJEKj-n0EqTA8n7zx4JHRubLiB7SEF7hgo_TTz6CJAn1fqGtwK19ymsED3a9Rg70gcCbC91LBnMc3r9p7IoObBHZmBerlDU3BAu-NwC5EcXQlnX-hS3Ky-IqqglML6hW-tzpkESUspxc74N4_2eGSP9y-DjJ-9jO9WssDkHjLn0_bTjWrTCv3acW8bsx0v_-M7_GP2-6NmJvdmD3ZGTtFPpMqBRo_a7HY_2ZPgboXJXv2XpoZQUaz_3QrzH6xFKQ9OENfwUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
طبق گزارش رسانه‌های برزیلی؛ نیمار بدون اجازه، کمپ تمرینی سانتوس را ترک کرد و بعد از برگشت هم در تمرینات تیم شرکت نکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102043" target="_blank">📅 09:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102042">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTQKU5I-GgOAvd-2dLGqNFO0gJiTnhoJTw_PZ-viYd8tWr3-ZrQigiqX33vQO372Fcln0UKCZY94-yPgbRD67OaVZKx0_kMR829KJ3K5rUqZ0O8QBN9DnEIqcF5A85vdOg2k66TMLpuA-geAopfzEUhrjRjiNHttUZqJ7OngoFC6bkghEbnId44qjDe2BVcvoN6y7_4vTGl4uls0Z2fRWzutKgT7zmJODuIG7Ee0Opoj5m6euV_XZYf-EOfa57HKmmtb5vHmymikzbjb83-CTwG8AJuUlSEd_MOFe43XmaqpIp4HraBef6hGzbtLMG55HtPGCCfp9QDKcvne98Nfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولا شیرا:
رئال مادرید آماده ارائه اولین پیشنهاد به منچسترسیتی برای جذب رودری است.  ارزش اولیه پیشنهاد بین ۵۰ تا ۶۰ میلیون یورو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102042" target="_blank">📅 09:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102041">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fecTwxsOjSYhyz8xSp28Q0VFdHZjfRWZ_S4kp3hHkJcyF_Dv_naoLQy588RnGqURVYTvIbPKqeoriro0X6ta-UrP2pRriyF2haQZ78wFI3Dd2kMmuG7DLml3KP9v0oj3nspPe23d7ggD6IrJ23gn6WLX3DoD9SQEckHq83nPkyeCFt9Eyr01RbcQbTHxwy738pMVeYTnhzkyWA0msJ29tN4tVai1q4T25S2OwY0ZObWAFBOQ6tpdn4V8MPlTwgU34urG8C6zVIhEy9xwjTiyo3dzsDKLsqaZTFcmwJ_LA5vW8lGcjzhYow-7ICGp6YaIfDQXe5XcwCVM50KHNHY54w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
اوه‌اوه یکی جلو فلوریان پلتنبرگ رو بگیره که ریده به سر تا پای رومانو:  حالا که ما را "دروغگو" نامیدید، شما خط قرمز را رد کردید. شما فقط یک روز پس از آن، انتقال رسمی لوزانو به آینتراخت فرانکفورت را اعلام کردید، و با این فرض که هواداران شما احمق هستند،…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/102041" target="_blank">📅 04:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102040">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdWOK_7dJuhw3MIJsQEnD81zpKAcB41K4YqtCIwgnNuP1Z94H_KrC2Mu1eRJIt_H-bxg7RqxLM510pKAe3oJpgp-Sw2QCbRkNuGZqDeXev4leNyc05mYWmKEBkFHPmnBANNmX-adgxFWK8SsSg01FP9hX_t_ERl6KtZzJkEavET247oDafm2aMw9n9AWNps1SOwBeZWAzEqyLEzSnoGEocJ0bq5A9nO7d6HbXoC7MVk9HOyizp8ZKnapgjPzlumOlplB7XLafh0GuGes3BCBfNWmKUaQl-47Q96RYzCpPsR0-4fGh-xtNF1MAh2pUAyejbMwZId3p-cw7qCeVeRmig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/102040" target="_blank">📅 02:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102039">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMKyxnnsjhEksEetEkStRhQS1HP3afHnDCK2D0Pu5VaqQOCoDNgw7hz9mF1N89apbT5i4kYullgwCmYztZxXdXYQ9bQkrfU_PygutpLiHwINHWF3z8cvi5-4sIxX18ynmoypksaIkSR9dG6YxgzMwwawjHlZoKN7PVdfh0_be8HLXrOJE8hXEvx-NH1wI23814xKT41Yd2-CnA9JwYEW1gZMSyL98tvsvA1YHBciGM9r4mL2_NxWAr6eADxlB4y6kpp4l3fLv1qzW7Mlsa4xchr8-5e1TwmSRzYZfUoApBC7myfgVpbTP_Ez2GURmryztOhzbh23i6obhf1ulkMJ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
❌
🇮🇹
#فوووووری
؛ حضور پیرلو به عنوان سرمربی تیم‌ملی ایتالیا بدلیل فعالیت‌های شرط‌بندی وی منتفی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/102039" target="_blank">📅 02:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102038">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4ZcdM3PGuvRmVkp3OhNDtU6xKiV60zNLd1WOEx5fzj9YKecEOZ7DdK1xLM7TYcvTLrp2Mgv_sPxP1dFhyDH3M5PZeF_zE3XwMHGwtx9jXl_4hYmMpAjrNw0Z-CEcSxOs6QSgIye1SQqk8-YWvR3G24cqKgDp7YHyLGCkJkhxPkIkdiAJDYHP4nGBU28L26_nkCVOO0rqs043vhF_816LyyETnG4kfcKPZTY-lgg-YXgJMhC2LKQdTjeO0ameJwTkmuH61oKmkEYiBzC91qqOAstWtj97bpccowy0UqWZ_O7BcppkC8DvguFeqKSxPIQRoWL1SRMyUQMBBrfJXtXbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ماستانتاتو بازیکن آرژانتینی رئال‌مادرید قراره به صورت قرضی راهی بنفیکا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/102038" target="_blank">📅 02:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102037">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrEk8u9xKs6I71N0Blh1q9Nh1KKy0MncdPxZttGt-BI0ThzWqC7eC7DXqByzHwFbuyG7CY87e4c46bEV6pvx_ThBMjQIjuuUR2FB4FlfJel9KEFWfvjn9hN3xG95RZ8AdsfWd8ma1b63igegjHiApkUY3p8uA__uuxdS---fl0GMsusTaY8-PRvwh6DWLLxoMhFYSPeBOSTOCWmKv2RI91PuBMjHw2TuRXelG_0DELusZl0rijUCoLlQse9eeyl9bpXZ28C2OdNGnpa-JXfZjL-i0xT82EVg1qmfdHb11rsCqeQqpedeQDG5Z8JzdJ4puYQJcxvwRfkM4203tKcLEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
جنگ بین خبرنگاران مطرح فوتبال اروپا بالا گرفته به طوری که دیوید اورنشتین گفته پیشنهاد رئال‌مادرید هنوز مورد موافقت لایپزیگ قرار نگرفته و نیاز به زمان داره و به نوعی گفته رومانو فعلا زر مفت زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/102037" target="_blank">📅 01:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102036">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HiWuy0bM9eY0dUQ1k_UJw6nMAlnGjZjkRaZNaYNLvNmmB9_t16C2eCKrVj3rt6wDJAiMT8eC2TVzTGRkSnPJ3xRcSAs3TAp4Vh1TqJhZ5MSYFkKouCfs4lkBUb9EaNevvVj94G6FdGej0PIcjUk8tfXHrjCIBG48EH1kF646-HFtqIvYT97LepA8nVw63VssZqFXSgvnlrloXCATDZ2NvpDE79O-7Pme6LB4vgYFLcfeGU2mHV_18Ig5CF06Pa6cxu3TTC3Pou7vy6iPoGIGiP55MEljF-Zoo_IYNUBrcuTt5eccotKRtsV8uSOriXVom9Y-1HfFrLW-32Q_RD4AGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرخیو والنتین خبرنگار فوتبال اروپا: ژوزه مورینیو به کاماوینگا گفته که فرصت بازی زیادی در فصل‌آینده نداره و بهتره به فکر تیم دیگه‌ای باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/102036" target="_blank">📅 01:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102035">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jo94PEhKExSN4gQUSSwueHrdvUN8B22BlTkK7G_3Mc9DAC0yCVX6fCPsWkpx2rcAMe4RY0i61urzi9ezfEk6Bqtyhr_vTeHL1cUYJF9txELDZ9pzAByXMwAIEHSz8mbaXtSLG-0bTrhVyaxF6spE69-iPGBZgf2WidFEZY3ndpO3CRJUPfFQ_BDe8acZTjMjz0NmmVwTNV-XGatr5ZlR9Ba3OLf_UolhNK368SaAPXFnrciT6PKJ4wAW4CAe1bRs8xBB2sqoCKOmGG9aodZ2kjkUlm1Ic9qlVbItW_rKlSA-sZ7HTq-8iyYN567uIdol69X-w-6vaWBMZYO54Q6Wrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/102035" target="_blank">📅 01:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102034">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeQbeQ6tIXPCdr06T2LkW0wbQ7PUOpXwgXaJy5eiCWx5S_tXZD3WkznAANczM32RO7WbNGGzs4c8PsHk41Mx9WKqcsnBmi4R1v-JaO6JWcAG-jj9COE_VIo0xECLZpi0V_BW5IMYu6KeqPgiORrjaBuw0-OHuz-fv1k6Kj1KRq6SmjjNifnxMe0HWyXlKZcNec82vpFDllljnoNgJgUDSX4UxEkaSbgYD73IRpajkgAvKl0DutVCh0TqAh8Xo0cx2D0P8tCMxkAT9Anqc4LG6qXdjf0X7nhTi3Ye7n9Qx4qjDyTlYwT61JeDkWQRLhADRyG-zBocwLiV4AmdKt1esg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
تلگراف:
مدیرای آرسنال معتقدن وینیسیوس جونیور همون بازیکنیه که میتونن باهاش چمپیونزلیگ بگیرن و هرچی واسش خرج کنن ارزش داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/102034" target="_blank">📅 00:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102033">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=EOFrwC0VYMv5FkTqu_giTCko8YLR02Q87xPI37XUMq8IBJfElpih0V3m9zvvc0C_bj9pq6jn2sWGJw6sZST92aZ05sw_waMYLcItTVQdg61MjiEEnjLgCEC5pfeDmdWUI-_93095orpQLQv8bQyfyY9UnHATMkRkhpWQXpQNrvpsXJ4M1i0W2C8s26EoU4yW-66kkTnfi649P_rY8XB-5HZyvXuo01MkNWdSl3N_FSqoCYq4vTBlx0Z3d-ZtPmmClVOxJTuvE1k4ZNquctEX-OxUM0r9hAvZpLp2TlkwNBU1iTRj6G80RDYDiG2Un2CmxPov0THWDcv9C964rLRKkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda4a57b7.mp4?token=EOFrwC0VYMv5FkTqu_giTCko8YLR02Q87xPI37XUMq8IBJfElpih0V3m9zvvc0C_bj9pq6jn2sWGJw6sZST92aZ05sw_waMYLcItTVQdg61MjiEEnjLgCEC5pfeDmdWUI-_93095orpQLQv8bQyfyY9UnHATMkRkhpWQXpQNrvpsXJ4M1i0W2C8s26EoU4yW-66kkTnfi649P_rY8XB-5HZyvXuo01MkNWdSl3N_FSqoCYq4vTBlx0Z3d-ZtPmmClVOxJTuvE1k4ZNquctEX-OxUM0r9hAvZpLp2TlkwNBU1iTRj6G80RDYDiG2Un2CmxPov0THWDcv9C964rLRKkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
وضعیت این‌روزهای لیونل‌مسی در تعطیلات:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/102033" target="_blank">📅 23:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102032">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN2kRSiOgx7OhhevbJjQCn7Pzx1YMlXdXxnMlVP33XtCUcD-CUtH_YX775GfFRSqKwwYzuIIwnbEtbVlzBw0rcBZMukC81hKCfGYv3xxjSz8Q3NEkqFzeFYQO405SHMxuVnd8d2G3UMNMModiBqKTf_SxJ0EOT5VCNVsJ-O_f_5yOmscEUJZmSzE8OmEX2frCje_LYb3PGqOmg8Sm6Z9tK-LYExjc8mtk5OsvWCwxDCK1VG8EEDIm4PIQoOo8hgjzL1hGkgYHPj7iu4lyaszwBVjknLcYnefZQ2FGixUTTSCcW9N_Li4SuskSLGLpolsLj4m0fmPrOUtZi5WN0DPmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📮
🇮🇹
دیس فلوریان پلتنبرگ به رومانو: بعضیا همیشه میخوان اول باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102032" target="_blank">📅 23:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102031">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXHYDu9Ptqous0B9KrTXkX6-OBYhth9N6EMG0Dw356QNmAIJ5cbuqLSDAn74kmCvm8ZT5SIoplu-FgdDPpWuKbwkcREFuF6yudc6mWV8xz5qvIOQnCtP_sMB8vL_r6vWOLmaMhhK3-NQXuOt1Qbt83_NVfhRsP9zPJyZ6OnRrlTAHSpndPG7rTOwpVNaSunWiwEByq6RtT9VRRdrBs0EON9zJLTYLQ8WFAF8HT16YD9pbDPDBHX6_QjSZtmo5G3UhegE6q2COVfuXMRiUkYq1hEHorXG9qBAgVkdVNpoRN3xH3HKAuQxtEDVbOsM4ZZmxzGx3laHP-EU0F9uO2nL5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
فلوریان پلتنبرگ اصرار داره که هنوز هیچ توافقی (حتی توافقی اولیه) بین لایپزیگ و رئال مادرید حاصل نشده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102031" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102030">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102030" target="_blank">📅 23:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102029">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=jXz3kmvmhg4vOsMxRNdX5gzx9R4STLharYP7swh8jJ1djIf1O8DliHvkyYtQX9pGV1ZpOYmXPge3XI3saIvNw39f1gCG7naJ97uIFZDMnaywiOkBmHQ2VYiQOQRTpD_onOgHKAPOdk0mRnauBzWaGXj0KEPyQZ9O5lt_URCmXHNm1w0RHp8WX04B3oeFA6umKb5Vuk-nUabytxJDCzdqk2jJL-rDVg4n8B5HEUH0dATVLxFiHImcWTG7Pl8pwn_44NCGWJrDsYlwCwxjlAqEJfpdIw-2PswYYQ-fKYoSKa3Iced2jf37ScqyoJtDxkHKUdXA-D15h2mTViw5wTH38A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e020f6fb8a.mp4?token=jXz3kmvmhg4vOsMxRNdX5gzx9R4STLharYP7swh8jJ1djIf1O8DliHvkyYtQX9pGV1ZpOYmXPge3XI3saIvNw39f1gCG7naJ97uIFZDMnaywiOkBmHQ2VYiQOQRTpD_onOgHKAPOdk0mRnauBzWaGXj0KEPyQZ9O5lt_URCmXHNm1w0RHp8WX04B3oeFA6umKb5Vuk-nUabytxJDCzdqk2jJL-rDVg4n8B5HEUH0dATVLxFiHImcWTG7Pl8pwn_44NCGWJrDsYlwCwxjlAqEJfpdIw-2PswYYQ-fKYoSKa3Iced2jf37ScqyoJtDxkHKUdXA-D15h2mTViw5wTH38A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره فوتبال مملکت علی‌آقا دایی
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102029" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102028">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5puorkWbI5lhyo8fTb5R_vldmQ6fLa2pHfIZd8jgESCx2bp1PQoetMIiTqFVnaCn-h4AykvdaNaWgNizrPeuh0JR9cszZkg9QyRVR98Km2jxkBOqOcMz-q_ZYCb3fIky5rMnUTPmfdSj40xv2CzBClE6H3pX10g_KtIjSItugxJp2YP2RV148Hqo9oMh-ZCLEQAdQUm4bOk8q8FbE_khyWQ02JWgBCZp4yLwOBKzoUJAiVYWWjInSqfnY-uLB3htHTG6FxX4_e8vv2r1gq8J9vkBj-VKkWSaluFf3f8HYtoDZr8d6D1fegEz07xwAvtqiacESYiGZ5GYUsuEce6FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👀
رومانو:
🔺
خرید دیومانده بیش از 100 میلیون یورو برای رئال مادرید آب خورد.
🔺
مدت قراردادش هم تا سال 2031 هست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102028" target="_blank">📅 22:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102027">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uza2nMEAmB6J9gmFUfWmXoc65EDUrPHDjGeOC_6NeUe9U_Q7Gn2A2bakoPkUx8fG8wKDnFWn9Q_lpPsYJmDvoAVWwpBkCOc7lkCriVjjEPYyFs8XTWySurziZ4z2i9xY7akbpJhqeWQIJNBAgJUeU1aCcRhHobOHdPPmWfwy8Fzn9LEWhtrvD4wEJq5Q75PvTVnUBVjO_1h9k6gek56sFH5V7PXSyUDdYhJ02o_YFtwR1W_rNlXWDMcMR7Kgi3UFW-pyWQqOn-TGlAfRSGv__pyawoEYccwctsToAtCinEK1Y-yio9PawrIuebWEcl5ZaGF1BUMCnqhan0hpdg6P4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار پرز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102027" target="_blank">📅 22:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102026">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102026" target="_blank">📅 22:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102025">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NG4Zz2aeTT_YBRuvH4GddFydf_1Y1OGhUVNDHjgtQ-Rx_-ScR0sgfDenBQtXVyXu9kudUj5GBeM-abednLhs2_Z4ihIQSbvkFKxdRG26bWPiYgGlyJ1drRTq1i2bgDxOJ2nOMcUDLWMvXA0UwTOh8w2AKvsqpdrXB3NLcRqzQEW9iRBAD-i3hqCddHS-aFdAV5oUkdfUGUbRvyOri5HByXGoAAPQs7E0J5xs1eZX3vvRIF901GpgWJA0bx5iijrcUvOvSR4YjiEnMkxbN8sQYaHs7OafT-RXlFrWi-RCKFmYBx_2mpnpmG9DWfnbnZUBHPCvILgYCUdFwpDqWxApGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
اسپورت: خولیان الوارز گفته میخواد یه قدم دیگه برای پیوستن به بارسا برداره و بزودی انجامش میده . نهایت تا ۱۰ روز اینده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102025" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102024">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2RazwiBqzovkw-GpvSxRP7RaB72IWKKL4oPOzJ06rPmSm7HHQs-udJDH9kyLKjbVwkPYHGRwAjmkX2u_Y-CH69lAn38z2-aQFt1CZiNaolx0Wf8TI6ryNDWEzOWCSwkiR6j9eRwb-Dx_DapyEr2GlumTA22V5Zd592dS_ooO5Tw286IG_ChL-pZt7h8nN6gKuhXc8T99Vt2UID2FS5atwBLBd5pzS6FXu5Op8LDLreyUYxDAwW0_goCK86VnUO4RJGr3IIKJPJ6N1uSqAA9GJ_vUbMKBxnruoef46jAT__lSUy4KnnJHF27e-JkiSEh2COdTp46mMVq3ADMSwnJDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102024" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102023">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=Tj_qe6BQaDRdD5n-gZZxujiUMT8d4-COZZWoqbHOylTrH4CRkEiOArQvzwqTEaiOn6ts2y4HyKC0GBFjfeeCZ9S-K9HaaVCQThoXldCWPs__PvGHLjGLD59rzj5fg1cjWAE7TQHoUgRCG5y7V8jOfmJqt5qQhn7FZWLGYrXFyFpstl9rX6VA1s5mMhkhxAIc14O9W6-rleM9On0adxGcRFazpmPZrYsP1haScz1P5d1hmU5qlFhh7eYIhzD-ww9wb5jimRPb18rEI6Cz3mJUx6AmFiXCQH9Q7zitgb2fNpR4GTowU285ypZqMUVEGJFWSGkbYnfLOHMJuDvtUpqoo4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9274ecf947.mp4?token=Tj_qe6BQaDRdD5n-gZZxujiUMT8d4-COZZWoqbHOylTrH4CRkEiOArQvzwqTEaiOn6ts2y4HyKC0GBFjfeeCZ9S-K9HaaVCQThoXldCWPs__PvGHLjGLD59rzj5fg1cjWAE7TQHoUgRCG5y7V8jOfmJqt5qQhn7FZWLGYrXFyFpstl9rX6VA1s5mMhkhxAIc14O9W6-rleM9On0adxGcRFazpmPZrYsP1haScz1P5d1hmU5qlFhh7eYIhzD-ww9wb5jimRPb18rEI6Cz3mJUx6AmFiXCQH9Q7zitgb2fNpR4GTowU285ypZqMUVEGJFWSGkbYnfLOHMJuDvtUpqoo4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
آنخل دی‌ماریا: مسی نشون داد که یکی از بهترین‌های تاریخه و تا وقتی که خودش بخواد میتونه همچنان ادامه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102022">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLVmfO--JQdScSngKYAfAuO-8jfN--bpvArJoh8wP-Mbjo2YZGvFn6nNoE7c1OAxkNKziWMKp8ykbk5QMfafPqB3lcgQg44MGUIUr5rV1L6Knoloy46aCmvU6TwBgTTJuCShC7GO26EJ94PBWPx0KlAiCqMd1KHtYPcKBToNEglFgZdc-ptz4BXFE4McqkxgBHZJqddfDnl814Is25mmv901-yfkWD1kS8ASXWxq1QipCy1CD2Q88vJzLExZP7wCElKQHKn926JxiOUUAbqYQjMzE0m7RduAVH_Pg40QyhH_TcJbpRcf2tBDaNcg0JObyG3rHNNxwBHZ4ek40LJOpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚪️
عمق اسکواد رئال مادرید برای فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102022" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102021">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=joDSwv7XweHfsH3poL_bUo1BRbFi8ysrlWRHu8nWMf8E_Sdd0TPrt_NDW-tkqUviEKd3SEzG4a3iEhaugWQid-tYm6560WMLQpUXpAp5clRHJqvQSJTTvTgShs5K3ick14nHYzYWmKp1yBYsktJZ8lZ-Zd906pgp2SpT-J6HLniqH6uuST2bouZbd73E4SQFqO9GYINZBR3aITKOV89UBMQZMIm3bDTI9_NoLjYOAQMSa-ZuWgCfrZ7SLUnGlZpa7QxjxEHvqkl43FpzOs0jItsr4hPrTqX-BL-c62Dc-f1TAQ70m9_wsfdXNwUyvd47Jl_xvIOYGzQ-BzSH57c7KKLcCsb9zTGisv6Pk4SaLGXB6Lvcx-1wzlA7Lm9oLBBtPLSHoVO_InBVA61QqeLOGncc-KEvd8r4TCg5qq0OBKnQgEQJhZuG5tYtQ30GEiIXFVDeGAtM4bpep2WXTCpcdlqsX7cHHeWvLzmrW1xAgq7qzL12ovY-m5uSZNU3WRw7Lq-ceFpD0IIg3AwJ6Zxv5JLO10tPhFWMBr5-Wvld77eA-XAKqcv5M1Xgt-nSHpt3mNi3RHOhXrrjhLkCGzF25fJFPpQ9YH7ylkYQi1SAmEKfc1UshcQ1MiLWCLrjz5xhOEfdafZk0sxdJsur4PNYE2SZFu38EUdQ5r4hwgxwA38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e76692a40.mp4?token=joDSwv7XweHfsH3poL_bUo1BRbFi8ysrlWRHu8nWMf8E_Sdd0TPrt_NDW-tkqUviEKd3SEzG4a3iEhaugWQid-tYm6560WMLQpUXpAp5clRHJqvQSJTTvTgShs5K3ick14nHYzYWmKp1yBYsktJZ8lZ-Zd906pgp2SpT-J6HLniqH6uuST2bouZbd73E4SQFqO9GYINZBR3aITKOV89UBMQZMIm3bDTI9_NoLjYOAQMSa-ZuWgCfrZ7SLUnGlZpa7QxjxEHvqkl43FpzOs0jItsr4hPrTqX-BL-c62Dc-f1TAQ70m9_wsfdXNwUyvd47Jl_xvIOYGzQ-BzSH57c7KKLcCsb9zTGisv6Pk4SaLGXB6Lvcx-1wzlA7Lm9oLBBtPLSHoVO_InBVA61QqeLOGncc-KEvd8r4TCg5qq0OBKnQgEQJhZuG5tYtQ30GEiIXFVDeGAtM4bpep2WXTCpcdlqsX7cHHeWvLzmrW1xAgq7qzL12ovY-m5uSZNU3WRw7Lq-ceFpD0IIg3AwJ6Zxv5JLO10tPhFWMBr5-Wvld77eA-XAKqcv5M1Xgt-nSHpt3mNi3RHOhXrrjhLkCGzF25fJFPpQ9YH7ylkYQi1SAmEKfc1UshcQ1MiLWCLrjz5xhOEfdafZk0sxdJsur4PNYE2SZFu38EUdQ5r4hwgxwA38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
امیرحسین صادقی: وحید مرادی من و فرزاد را در هتل المپیک آشتی داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102021" target="_blank">📅 21:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102020">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6ZHsO9fzJemCSrRVISJcpkfxGdx9txt2dyc32vcvajiPh_A3H4gMcMBE_prsJoL4knKlR_3rHlXnSUyPqo3OJH-9pROoXC7TtlWPM4E7NJyM8_bYnB7ubY_lwkYp5mlrz-aoLUx54wvALAs4002IEBPgcvK83gz1oGcyMOzkfTs5JLEFQAk9erNxK67Q-lCK2ZfYElvLr0mR3_LHsfugY_BAmVCPlJR4I_-oZ-s_Su4lSF4WWr3QuerrMrNitorMAKad9zcQL85iLJIX4xZdCKwOzYNWbxZCoST7_Fj5BuTvOLXyMEQwqOLHy69NxCaOLhML26yukbVGVZDPTKxhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🚨
پژمان جمشیدی که به تجاوز متهم شده بود، در رای نهایی دادگاه از این اتهام تبرئه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102020" target="_blank">📅 20:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102019">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q49rviogYCUxVwA2Yu4mfWLG2fYQ8HLFDLq-_zpuQp1LPRR5-3eAPBe5g81LJ2wRuC5YzBKqA1cunOYvwBQ_IsANaIq2r3GpWN7On4TXuOcGNXhwYcUICphRInPaoEXHbcjJJQka5q77pELSjifjFnt4DpEE-DO0G6VZBJV4_uo0rmfp7vaxQtFT8r8QvzU2M7uA3VqtaZ22XhKmIBJWiHtf6tfncrTnFjHn8nJcxEnDE3PNV8TG0SFh5c4-z3QdUxe5-7PSOhhJKH7acr7nVbM4rY0egqd6RY4CZbKiEMY-LW34MmRCOAZOPFPBbIUyQPrpFMGhU08DwVdeYZvq8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
آرانچا رودریگز: انتظار میرود که یان دیوماندی این هفته به تمرینات رئال مادرید بپیوندد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102019" target="_blank">📅 20:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102018">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHb7-d08MPGSVdW0qoJETm3Ofk3vr7OAom0SbfBewLbwjHAb_ZLeS_CfDKDwtkD6C7Zqqrcn5xrLNw9JSq_XjnD39yBxgjfWxVNZ7ioTVrIBquM2xjwNP09FqtHBcwnuimg1VN55n8DsjagzikKiWCM6M_6JeQBTLbZCv_GTfdXv6FLfOMaB7NuI8XvPKzX1q_EoDUBNJnjK8YikMZ39n3d0nEjZ8Mz62Szr9QjlcriY_uTPrVsNdtha1S-oK6GPdBxUhCgr75JbVLQP0AYu6iUbtlxe5u8QTqVxgaiuKMQRhGP-vX_nJ-wRPbRJmdJupq1tFmVisGXqw4Qh9q9-E3Jb0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53f1d3.mp4?token=O72gAn2RjfWYhG2M3dj7t2ecKmlz7nBypTsvLfzPmyB7-wZLda1x-_zjJksLc5otzl8FLbXLYV5vZ-1eslf6Xb7Egw-yI1aFOjg4YmZE5EBiyR2v1momHunw4ZsTMiVvcLcufZexvrnWM_hzo_KJIz-46F97INcUBn5QVeOLiMRblr_fGAD0M0OoArlDPNj2Ufd9pLAEOac2TOhOgNXZ054mI-MnjqFamXNz96ORCp78U09ONnCyWk3nCblpeDhtrNhuHizNn1r1hco1gm2LpOYIxg7ZK_WbFNDNSM4NkGI-CJkoEjj7Gchr5jyFn-cb9SOgizJcQ3Ab4CewacaHb7-d08MPGSVdW0qoJETm3Ofk3vr7OAom0SbfBewLbwjHAb_ZLeS_CfDKDwtkD6C7Zqqrcn5xrLNw9JSq_XjnD39yBxgjfWxVNZ7ioTVrIBquM2xjwNP09FqtHBcwnuimg1VN55n8DsjagzikKiWCM6M_6JeQBTLbZCv_GTfdXv6FLfOMaB7NuI8XvPKzX1q_EoDUBNJnjK8YikMZ39n3d0nEjZ8Mz62Szr9QjlcriY_uTPrVsNdtha1S-oK6GPdBxUhCgr75JbVLQP0AYu6iUbtlxe5u8QTqVxgaiuKMQRhGP-vX_nJ-wRPbRJmdJupq1tFmVisGXqw4Qh9q9-E3Jb0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنتا سوپرگل قیچی‌برگردون ببینیم تا روحمون ارضا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102018" target="_blank">📅 20:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102016">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oIaI-WHxbk34vYiZDkfM4lDNbEj3Sla80LTiAUI8Jkyvcvnj-X5efkoMITVK0vU7FH9o_jNKsK2u7ARtkrdRBVMcoeLQTIAgoxxJ1aARAdqg0muRE1WbXEs8L9-1sI3-oBrnXRkkdC1X7B6e5lcBk8MwcXKT6VeSvVPeFRLcvzOmp-n8cexaIS9Jl652TJQ_YkqSaufV1TJryb2T_l6XdKFV5NP-QPLiH7OMyoEZM9Ea5XW8QGPye74UzCZ11xYIs1BjDpflq3CFZXtcmpqte1hJ2V-xOzl5hXZsdb7e28Uqg7xTufIcimlFbETS2ueVAi2NFv0jvbsXMzffewgDLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZ6YIYQMbeqYT3jtq7Zau5eZLrCfgvAaXO4cTszYt4wgv-bcxQjd4XoNRNEeQIM3ePRvueJih57pMpgWZDJJiiuplJcb-AOHulVamUA5igIm4cWBDpKnGLd22yDTVrVqgg1oKyL2AVLf4fsx4-TIwMN-iqKLdkx7WVYSJb9_VsZiKqUYXglGk4fmsu3fqPkki67jX-DdUV0dzlALqQxtwekeuzEgvCiuupYLGVBsfLOCXnYOoEYEEu-XnAm-cWMKAc8oCI7inxfhd5-4veaJIBHgI7eOBpppcy8Jz0fFtFCkmLzkAQanlAmJ0AxmgcDgBSQjsJdvrCv-63GkPQFEEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
لواندوفسکی:
شاید مجبور باشیم ۱۰۰ یا ۲۰۰ سال دیگه صبر کنیم و منتظر بمونیم تا دوباره بازیکنی مثل مسی ببینیم.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102016" target="_blank">📅 19:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102015">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csMJmP-FBoRgBnEhBapBHIOOr-M9MfQObJAAIluzT46qnhji8eaiKUXyaad2jeomhPgcuoBrxoFX4Oys-d4WzK9ijSWYB1uAxnjjkRdANk6168T8xtfzO3QPANirHQ5XMPxvQyQMv_rDu91ngeB8FYOM4zT3Oo9wToj3XgcEkZFlEpS_mRKZSmoVN-hUsdc4u7HUtFzkxmggxRF3bUiwl2yy7CrYe6gS9mmJuG4Gays_t7Kcw7LQt4nSbndvAmfojBAp7ITTk5bQKI0PnuEWPNkTM9bHOliKar05_337nimULiZxakCV-ZsBsOU2VmAWxV6Rj8tvcefhwLlfzoi1Ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102015" target="_blank">📅 19:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102014">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=Zxgvdx5t0v50wJDTxz9zjZ5muykcrUqX9nqBwgh5njsEhWu626JSrm2bWlU07vRJhSpBIx5P_e9tktCZYr-N64Yzbc-f-Llrx4hno1fstZh-AUp_Iu0LROQhBoYDOVc3eknMSi0JSd07hQFKW63bb8O0jc9-7AzsDJgCYzCjpm2w4Eyfk8F3ezenUsqZXE77D5enfFw0i6I78_QjZrL_c9x0vrOMP9n4GFKe9cvTsP2U2cjgf6h340NdCQDx4RJUnWVXaUNlnrXnl6wPVAzBLgM435DYJZd9pSM5vwj7AaIXkQTXesaVVd09qsuiXvZ8XwPv_9xDxSH0O-6fAcl64A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3e14eaaf.mp4?token=Zxgvdx5t0v50wJDTxz9zjZ5muykcrUqX9nqBwgh5njsEhWu626JSrm2bWlU07vRJhSpBIx5P_e9tktCZYr-N64Yzbc-f-Llrx4hno1fstZh-AUp_Iu0LROQhBoYDOVc3eknMSi0JSd07hQFKW63bb8O0jc9-7AzsDJgCYzCjpm2w4Eyfk8F3ezenUsqZXE77D5enfFw0i6I78_QjZrL_c9x0vrOMP9n4GFKe9cvTsP2U2cjgf6h340NdCQDx4RJUnWVXaUNlnrXnl6wPVAzBLgM435DYJZd9pSM5vwj7AaIXkQTXesaVVd09qsuiXvZ8XwPv_9xDxSH0O-6fAcl64A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الگوت کیه؟
دیومانده: رونالدو
رونالدو یا مسی؟ مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102014" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102013">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=kgUnmBiMqHpTW1Zq9j3s9H0gYjvI5hve0AZFsXG32A_yTMSzaPKFv7dnJ56tjNsyFjB8jFq8kqz-jy2rAJ6alq1dXDbwluQfbUWFQO9ngs08owgUCesKW9WwiJuYScO-UWdd1THzMN_M6vZkd5T4cRryAzuaygVcpwz8DFXtMARYvsnpVuTiNYQinZKB5P7-JnwzmJPQQlcttbGvsInjZBjwxxvW8rLEEde3CtcP33AEVeZX_Ya8h5qEZPH7EXWesuOey3YUto4Ek5GncL4mAt85QJ1Kl42FBkP_JPr5qVW7l6y16TzSHq0G6e2imc996jOvTrNFIU0I6h3w6lqe6qu10pDbou5Gp1-durqfVVJ0-xFUKOuDUVvJGI6nEOrGpsVAXZ25LIhfkpJhKgenDRVz_TnZLAc7rnDpt8xe6Nu48euKKEjTrVTOo294jjwApMlr5U2-sRs0Sk4I3pus1kFOA-YOg6ZHOZFFvVmXLuNcK-Vi16twErjNxl4NJxXd7XlmEs0BifGZYMz9i0E5giRYMNQtoM6IjaUSANeRX8gQsSmkkxlanwfWSq6D0UszTGkwQ81rBVG14AqVaM1gQ9txfM22Ee-E9f1RzyNvUoXIsAkupm70KFr5hFxQOlg63erfLxMtskg9SNYt6ajidO345NH8JCz6JmwRS6LDx00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1d6e560e.mp4?token=kgUnmBiMqHpTW1Zq9j3s9H0gYjvI5hve0AZFsXG32A_yTMSzaPKFv7dnJ56tjNsyFjB8jFq8kqz-jy2rAJ6alq1dXDbwluQfbUWFQO9ngs08owgUCesKW9WwiJuYScO-UWdd1THzMN_M6vZkd5T4cRryAzuaygVcpwz8DFXtMARYvsnpVuTiNYQinZKB5P7-JnwzmJPQQlcttbGvsInjZBjwxxvW8rLEEde3CtcP33AEVeZX_Ya8h5qEZPH7EXWesuOey3YUto4Ek5GncL4mAt85QJ1Kl42FBkP_JPr5qVW7l6y16TzSHq0G6e2imc996jOvTrNFIU0I6h3w6lqe6qu10pDbou5Gp1-durqfVVJ0-xFUKOuDUVvJGI6nEOrGpsVAXZ25LIhfkpJhKgenDRVz_TnZLAc7rnDpt8xe6Nu48euKKEjTrVTOo294jjwApMlr5U2-sRs0Sk4I3pus1kFOA-YOg6ZHOZFFvVmXLuNcK-Vi16twErjNxl4NJxXd7XlmEs0BifGZYMz9i0E5giRYMNQtoM6IjaUSANeRX8gQsSmkkxlanwfWSq6D0UszTGkwQ81rBVG14AqVaM1gQ9txfM22Ee-E9f1RzyNvUoXIsAkupm70KFr5hFxQOlg63erfLxMtskg9SNYt6ajidO345NH8JCz6JmwRS6LDx00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102013" target="_blank">📅 19:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102012">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102012" target="_blank">📅 19:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102011">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5Cw8QGrsCrRjxnwL4qJLa_b2Aaey1FIbCuEaZkb2_vyfJEroMDjwmt_OoV3ANRgR7HrLem6kKxKKRQ0CIBa4-YBpoQiwdFn8MN4KRPrmNNWTMCJWLUlqs6QA_vqwrnmezIIPDBxAOMO3RKA46G_mW1hny0UPYsAIo-fjR50DOx8w42pDGvVpaZSVa3uFn-0JjkJR1epENs7zhDQ_AdP0WIuutu78ssDI-_3xSgzwAY7LX2xdorB4uXluOqK1TBMAJRyFuFOMk5jZLQKXemKMvARrf4hxafPbh-tn6WlmEQZ-Jna9mtI64FRmb06Vv3nIevPkkVGv-ZJaqeLTFvCmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از خوزه فلیکس دیاز: انتقال دیومانده به رئال مادرید نهایی شده و بیانیه رسمی فردا منتشر میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102011" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102010">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/746abba13b.mp4?token=pIeJkocilKAEsbRbc97rfF_bbUxKEUZX8hqtU0HZyiv-UWvpl_pUdWaH1yXBSsn_n3I4QNT3si6729w3WJ6OCnA8Forj9qk9pj6QuaUVEh1r54I5dH7EgIqgAgEbRIyN1y8Y5SeURcD0gC_YaM62NXnS7KRyDsbbPALEtYvSsQQUMZjeq0hDYvHRyG3XyncU4xoREPHb0C806IzvegPUR17JL99sNZqIUA9MkMWYrrsA0nKDTFv302oM5Twqo9lRqPGsLWnHD5HYossl8aDfI1Hg5_WUHc0sTrSKW7MFxLP6-apfaWwPJMK7OySps2DDDSu5rTSUao8YBxE27_jM3ExstU8vbKcAyE8pID6SOZ02CfZO-zt_3B8ixQV9D4MAeX165W6Mta18ytQS6Sn8jqYN_QIaeVCeGjO70tQpo5gq28fPDX85BDyRf2SULsRy2vFZUN2gJdpxfcsBGTmq80KeOLlKSTvfe7gun-1oRCpxxvi8QDW2iF0gK0fKhkOhj2H_NBUBYB2TWBOj0-LYO4khqeQqa_t3IwBli7yO4fjozNk9M2Oiz2IHAezkMmUZcr93O3WTdWAtzpHTCRqg4RIa0i6wEgyRi9KyFNFz_JURQG-HCwycckNmaCuMG_uOuK7jzZdEVdzrg9HN-915c_yATn2leI3rL6utoOLKxlY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/746abba13b.mp4?token=pIeJkocilKAEsbRbc97rfF_bbUxKEUZX8hqtU0HZyiv-UWvpl_pUdWaH1yXBSsn_n3I4QNT3si6729w3WJ6OCnA8Forj9qk9pj6QuaUVEh1r54I5dH7EgIqgAgEbRIyN1y8Y5SeURcD0gC_YaM62NXnS7KRyDsbbPALEtYvSsQQUMZjeq0hDYvHRyG3XyncU4xoREPHb0C806IzvegPUR17JL99sNZqIUA9MkMWYrrsA0nKDTFv302oM5Twqo9lRqPGsLWnHD5HYossl8aDfI1Hg5_WUHc0sTrSKW7MFxLP6-apfaWwPJMK7OySps2DDDSu5rTSUao8YBxE27_jM3ExstU8vbKcAyE8pID6SOZ02CfZO-zt_3B8ixQV9D4MAeX165W6Mta18ytQS6Sn8jqYN_QIaeVCeGjO70tQpo5gq28fPDX85BDyRf2SULsRy2vFZUN2gJdpxfcsBGTmq80KeOLlKSTvfe7gun-1oRCpxxvi8QDW2iF0gK0fKhkOhj2H_NBUBYB2TWBOj0-LYO4khqeQqa_t3IwBli7yO4fjozNk9M2Oiz2IHAezkMmUZcr93O3WTdWAtzpHTCRqg4RIa0i6wEgyRi9KyFNFz_JURQG-HCwycckNmaCuMG_uOuK7jzZdEVdzrg9HN-915c_yATn2leI3rL6utoOLKxlY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی فوتبال تبدیل به یک فیلم و اثر هنری میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102010" target="_blank">📅 19:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102009">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EI6Ca6qHWvqUtm65tltE9SreWM90mfJkf3INl_rPONeHaOxQxFzzpmnY95C3yzE2gPM_iQFPnoAGB-yHeyKEqLhKA8sVG3vjmhsQjbvg62mXpW98tXMpo4-t-YvGYtV78cgYlyfGwd-ZhHSx1L57o6mXziX_hVtMja5kDyp4DPxInrmlPblnrG0nNzb6bqW6Twr9iBcvxstkW5Z-ESzSqBV2RyJkpsaypBeMPi1qyeTa_UinrORD-avCHfQN1ShP7eNFFNzI2UdFI61siKb-Dnz2c9dkYI2eQusJ2Lj31PdPha_33_VipE5y_JHgQUYi686vyKryEv7swc75pAQ2nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
اشرف بن عیاد:
کار تمامه، مدیرای بارسا متوجه شدن که موضع اتلتیکو برای فروش آلوارز تغییر نمیکنه و نمیفروشنش، حالا بارسا منتظر واکنش آلوارزه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102009" target="_blank">📅 18:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102007">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XloxqKK5j64eq2MLP6pxF8bXBPwUrmAk5Ear5SGWJ4WenqWtjgzcMAlAz6MSX_6wzjzu-03-tx6HSMVLyLBQ_ZpErx-3oJ07h248y-2lIDib4VYmH27Bfnu6tFQsK_NBY3ekIDvYBz_bpAtMbYCa2EYgHJsuYrurS5d0Xs5NV93Gd8nDv04WxcouhgyNDtgGOjmWSbhU28b34zWDvSq_0YC6knWpdir6xVNnwDI0fcAJ6n6jKRLbDiS6uV3MJeNAWlLg1gGXHsdRSiMmnW_6xGEJ-Om5My7SmYjbarfHd-a5oep6KRN8zrxyIEWdUPkbG07cbB440zZ6ydcWD36XHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLPSnVyguJXLa1lQhcvvDNCiX00TXmaaAIjWISM_8IfECnp3mHvlV6A7Bz_OKk1vpv7Ptib9XcaG1TtkkBODfa2FMZA2RhP7yW1dLwh3WteYyBbY4E4Ynws-GP1GE1XYBTRfB_PLUDegKU2KGPHBhL7EUXylzStepnwK6sOplO9893mpeMqsHXfW-OfNODz0X9IMNEoga1qy7nReJNs83RID1A3KUfmBnJqujFCrHPVYuCgHbsFFZfOZ4TfmbVxl0wO3WFtpGMvl0vMQrbDcxKCjNZuM5Z_bBRy3AUeWJz_vnbWb2YC--wDVhvFDm2fTXfdtJtUhE9g78mYTw20XEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102007" target="_blank">📅 18:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102006">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=v-C3L2Wb6x31YfBFh8jN731QPOFhkzPHb5BBUlNRlcCX0FE23CrdBhSICUKGmSCP9B0dRyQoopeoe_ndxiAjTZalMOGgpMShOtuKSCZKmlGch8gXe9HwZeQG6Q90OZnJzcu8oOp51Q4QHTP3fdhUcAYiOmj3Zbmm7f7zepe0Qj2rgiE4889ArjZ-wJUIqc6bAUpvNaKMcA7H5Dqora0vBaI1FpdnJ47qU3qzaX-WI80HCLheZWx3HLPABCOlGdi47--yURDmUI6VkywpT3H4a8bLlM0G_vTH68jw3AbrzPrTU5XVl_1uNBhS-oAFuCOtFQtLsf7FPdsCLKS__vD-Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac77f90860.mp4?token=v-C3L2Wb6x31YfBFh8jN731QPOFhkzPHb5BBUlNRlcCX0FE23CrdBhSICUKGmSCP9B0dRyQoopeoe_ndxiAjTZalMOGgpMShOtuKSCZKmlGch8gXe9HwZeQG6Q90OZnJzcu8oOp51Q4QHTP3fdhUcAYiOmj3Zbmm7f7zepe0Qj2rgiE4889ArjZ-wJUIqc6bAUpvNaKMcA7H5Dqora0vBaI1FpdnJ47qU3qzaX-WI80HCLheZWx3HLPABCOlGdi47--yURDmUI6VkywpT3H4a8bLlM0G_vTH68jw3AbrzPrTU5XVl_1uNBhS-oAFuCOtFQtLsf7FPdsCLKS__vD-Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خشونت بی‌سابقه در لیگ‌فوتسال بانوان برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102006" target="_blank">📅 18:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102005">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snfwb_1tjQvuVVwNDo3kDD1EQcbsFSoh2Y0eq8gYBCpd9Ix2bWegJ85qG5gxeIBuSpBjqEwNEIO3AJM3hYz0qkx2AE-Fetn2NlhnEz-tMVU5uizwAd_mgwHLRXFzOAiEfJ8MOPU5rjYBEXtupC0xXZ7dXOblhJr1KKcXx5kXCqMCSxSdWTKn2fCFnHAaXV4ukFStvkRFcOAhnMw48oi-CFfkk3IBpwiBSN6CIXN2NZeP2MAoCQNjJ3837muFkWqrAqdFn7Ztcfnmo8BEVmgdkeDb4C2EriHcFrW21YvXvqqDuiUrf6BiILb-MMmXXF8nkTpzGPmZ1R_qa94XzlIXeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102005" target="_blank">📅 17:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102004">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBvdwEJg9j_yXdttKscgimmE47NtMU8rvHBiLPITkzfjwtwOtE-xNdCh8oMxFLzkPfzoB3cWp3Ok1Ix9lSXvbRLcK8Z1yT892ZjPdMfm3U2vl9pFex0VAXnow7ULrw_x4LNtircpgwtDthDL9qc1L61m_fPnugjTpegAqA3DWlQpcXSWijiqzChR81dwb-Hbep5uVYycSlWDw9ILSEqbUWWn1P6i2lbhZF7uGGZWF7zrBQoW8-gGQQHIuSztQ5UkMFOE4ntpW_9ZKx8B9cEAy5LzXPy4AOX0oMF9cl3ka5UEpy0eFemn17_qH4TEFW9VM3fTibkR2C0_LRmjenNX8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
متئو مورتو:
فولام قصد دارد یک پیشنهاد بزرگ به رئال مادرید برای جذب گونزالو گارسیا ارائه دهد. آربلوا می‌خواهد او را به تیم خود بیاورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102004" target="_blank">📅 17:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102003">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQoClJpt34fKcex7j-vsB61tKa6Kc6Gj2uakT1roPmK1AeUfhW-MOMM1tPAf3lDwJvoCR51uoj9lkxnSvQMpvnzoaTeIFodvrXTBjSMdbq_wZ3KDoGZN1HZ9_1l262WCnCWSiac6Ucbv4MGRy4tvnLrb5Et1ZO7ZlMgkEzJToboK0XPvntyXRWBV13DrXTJvQ-PAkjSJRoNQRcfyFZKPt_TrwwDXCDmgkm0kkql82gSNdTzUZUai2a8SUYdiHgWvmCyyd0CMLgleEw9tZUBFo2NVcK0GBRBDwLzpgjyjF2gSWFXaw0b13R-9Y8CRYbJEmWci6cCTLDNgytrIiGOUSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سانتی اونا:
باشگاه الریان قطر پیشنهاد خود برای جذب جیدون سانچو ارائه کرد
باشگاه قطری در تلاش است تا وینگر انگلیسی را متقاعد کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102003" target="_blank">📅 17:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102001">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🏅
فوری؛ لینک پخش زنده بازی پرسپولیس و پیرامیدز مصر گذاشته شد
💬
@squadify_ir</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102001" target="_blank">📅 17:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102000">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=loVnze7RSvmSGa9XyxvTsPtua_olyMhUM-lJEZhyD1z4B0-qls7oxAOb8Tz_sPCaiLmrmlr6VPzRYLwiPDJpYo2gA-vUlswsNroALR-8fxvcidf1hbxuMCEPNyGz12WZomT4K71ZI3hVwhu5OOd256blADWNB7Jeezq3J000iilgMyOnPWmpK_10acB7NdahFhjpIj36OQ5ay8zRFJ7PiBHC_egUeluCnnDi5CTIdTrHUZ6r5tbucxTeEOG64yOjUbTMc3nkvlg0_lKBxJgESCBYBXrL7dB6UvIT7Wpw6PSs3_ys_DPaP6GeZot7UQHj-D9mg_5YIEMTV969LQJg7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9608d1c2fe.mp4?token=loVnze7RSvmSGa9XyxvTsPtua_olyMhUM-lJEZhyD1z4B0-qls7oxAOb8Tz_sPCaiLmrmlr6VPzRYLwiPDJpYo2gA-vUlswsNroALR-8fxvcidf1hbxuMCEPNyGz12WZomT4K71ZI3hVwhu5OOd256blADWNB7Jeezq3J000iilgMyOnPWmpK_10acB7NdahFhjpIj36OQ5ay8zRFJ7PiBHC_egUeluCnnDi5CTIdTrHUZ6r5tbucxTeEOG64yOjUbTMc3nkvlg0_lKBxJgESCBYBXrL7dB6UvIT7Wpw6PSs3_ys_DPaP6GeZot7UQHj-D9mg_5YIEMTV969LQJg7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
آنتونی جاشوا، قهرمان سابق بوکس سنگین وزن جهان، از آهنگ سیاوش قمیشی برای آهنگ ورود خودش استفاده کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102000" target="_blank">📅 17:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101999">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=FvmC7lega4xtADilflotiPcDdhYEIOeYosEHmz8cvDu-S7JWtqceD-49UaXPXDV1gygNgMcyrgcOydN-gih77szINW_qnVFVqawbdZr-_xbg36jG5hdO2xrIiUM4rPwRJp_OfV93mFb4dqzlJJjsDVl_8i-V9S4rA_8S9PTc_i50eaIDSQf9Cc98tOC4EAKBPwlv5rmwRI3mZFSmSIKNA0-PGCgSj8d3CrIxwK1D4_p3CgSXGhgOlSXhrU0Y_qKTtfYp8ZLO4WRQfgBRDU1x9gHWIinqrVTCD7y3ZG1iN7bN11pKtij6FfQpyOgcZQ3E9IU3vF6GiDSKo1rSVIzV3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f6f418b4.mp4?token=FvmC7lega4xtADilflotiPcDdhYEIOeYosEHmz8cvDu-S7JWtqceD-49UaXPXDV1gygNgMcyrgcOydN-gih77szINW_qnVFVqawbdZr-_xbg36jG5hdO2xrIiUM4rPwRJp_OfV93mFb4dqzlJJjsDVl_8i-V9S4rA_8S9PTc_i50eaIDSQf9Cc98tOC4EAKBPwlv5rmwRI3mZFSmSIKNA0-PGCgSj8d3CrIxwK1D4_p3CgSXGhgOlSXhrU0Y_qKTtfYp8ZLO4WRQfgBRDU1x9gHWIinqrVTCD7y3ZG1iN7bN11pKtij6FfQpyOgcZQ3E9IU3vF6GiDSKo1rSVIzV3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
قلنج‌گیر معروف ایرانی که با درودافای مملکت ویدیو میگرفت توسط پلیس بازداشت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101999" target="_blank">📅 16:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101998">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=hO2EIENqEP8H2z6Giw_aLyHIqjctIatf1g6ce4-puI0Ywb5EaT9h2ls-ac2VzC7nSXfAHzek51mk3JrJ8xVh92MG61CCv9PKZpFT5hC0GnGgfvWS1FHXX5F1x8dTk8IHmnLr7PsD9ya4bTMNq8V60NFY-le-H_Fa26h6h0M001IRLGChJnckmzXtte-HMLUruabddMw-q-I-BDNmFw4BVNXFKBi4dP9xKdXOxik56H0SEoaCzmF18Z-pCJbiNiPMQ0GalAn-MJDrMIu8su-W2bLcqoCZIZQt_sTcFFuOK84cGEJrl6VmNDR60RBGr-3VcWcYT3M7k0ttXonZOwX9rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a860d22dd.mp4?token=hO2EIENqEP8H2z6Giw_aLyHIqjctIatf1g6ce4-puI0Ywb5EaT9h2ls-ac2VzC7nSXfAHzek51mk3JrJ8xVh92MG61CCv9PKZpFT5hC0GnGgfvWS1FHXX5F1x8dTk8IHmnLr7PsD9ya4bTMNq8V60NFY-le-H_Fa26h6h0M001IRLGChJnckmzXtte-HMLUruabddMw-q-I-BDNmFw4BVNXFKBi4dP9xKdXOxik56H0SEoaCzmF18Z-pCJbiNiPMQ0GalAn-MJDrMIu8su-W2bLcqoCZIZQt_sTcFFuOK84cGEJrl6VmNDR60RBGr-3VcWcYT3M7k0ttXonZOwX9rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
اسلحه به دست منتظر آمریکایی‌ها
صداوسیما: مردم بندر جاسک به صورت خودش با اسلحه در ساحل قدم میزنند و در انتظار ورود نیروهای آمریکایی هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101998" target="_blank">📅 16:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101997">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0JrZhAZxh8i0ZbERnmaA5jRH_4pCefFouYvekXuf6cwtu1IFeyfNB8ai9PQorMHw_PZgJC5a2sLDXN53k38RHFap1FamXRaIBvNaJSCYX2SPBR482V3tODc9iQOH9cWnpKP009NiTFfHZeX0s4mDaPKKVpijtUEJs_PpVsMi9cRlm1kNwd7_aw26jBXm3-3qnHJRT-M35XrYLstxj-pJE6PM2yLLiCfr01Q-FNYYiSOXIfnsjBPJxG0YTafs5RAzRxZafbVs8K7VNj2NFxf5O-Jv4IIblFxxGCFc3wLozzxGXrmMvEt5dggStdH2n8d5l5ZmK0052pNurjCVuNsBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101997" target="_blank">📅 16:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101996">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=gMWSUzl84dafNrptPBYtdWT7Hsoq_MWRZqfywCFTwOBKtzVwIJi5bX0WMRBLxK9I1FthvjzMudOd24qawRYDFAokglJeW8o9H14MBl97s2Ih2Xn3AcCkSa2pw2whc3M8UKdUp_XhdLjIMKvym6mqgEVABnixVlBe3htjeI2JDAqH2YWnQ_n-INXxmSBaLDBcFYfadzFMLEU-mingEA5fce7Eqb50lhnufYBg2JYhvAfuUObAtKTVTpl_O40Eqq4DBDRY_NJpRNXfLJa6W6ywPlShATfk7IJuWUa72dofS4QP1IGoKCR5L7WRP8Ny4yb2cnlfHDHnyhpce3_Lo7rKsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58250e2a71.mp4?token=gMWSUzl84dafNrptPBYtdWT7Hsoq_MWRZqfywCFTwOBKtzVwIJi5bX0WMRBLxK9I1FthvjzMudOd24qawRYDFAokglJeW8o9H14MBl97s2Ih2Xn3AcCkSa2pw2whc3M8UKdUp_XhdLjIMKvym6mqgEVABnixVlBe3htjeI2JDAqH2YWnQ_n-INXxmSBaLDBcFYfadzFMLEU-mingEA5fce7Eqb50lhnufYBg2JYhvAfuUObAtKTVTpl_O40Eqq4DBDRY_NJpRNXfLJa6W6ywPlShATfk7IJuWUa72dofS4QP1IGoKCR5L7WRP8Ny4yb2cnlfHDHnyhpce3_Lo7rKsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
علی علیپور: حتی خود پرتغالی‌ها هم کیروش رو گردن نمی‌گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101996" target="_blank">📅 15:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101995">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKbA6kfNHI3jS_qc0ioS4k8hSFyAsvXc0ftW0snqz0KbUOHE1Pjo40oOoGlOTRffFuCX3BaiihMrSlu71SMtL-ou5m-ICgZiQLy4OYcgbXCmvVRZPRsgOhnj7JNXk9IRg8OtYZ5tljZs1s4fOTVsddMs1y6XNPCsrKOAxwgKp3oinDvPnPkCAWt8HDkusHEtyLP1gXuKPIhOVT-96XO659PxYMmqcUh2SWNH2lxqnfXeKXTqgxUS-qc0_w9l9yngRJnlhpP_06AcvZhLx2BlvBgG_J9VImJU3GPvPTcSnstryRC3qvwngMcBvMlQ7sQDU2DUavU1FuYGix9ZcoGKTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101995" target="_blank">📅 15:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101994">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🔴
فوری از رومانو: لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101994" target="_blank">📅 15:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101993">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7AmLYWVyucDwMHXb7wRhJdKSVzRB3MMyOpYsfw2VXX_lAmet7wBrO2_NQUkCNlg8dAQYWjd9NVBcxNgYHTF90kDPbmNvsSvkLA07T89CkPjGTHexpaNqZm9zfEEoDx00TgbWIvhHzvFWN_7xwpIgB2gzd3t1ttlAW28u0YoJr1lpCYbg8U6bT0kqEXw7UiE4xJISQZCp2AMOaujytEoS6Se6Ejt79C7wATUVX4fW2BHtqvf6l-UxgeozUNP2H2mH0hyhAOpoYCU5S8cZwKPTaA7lsrfm5qkN5vvAzIAGSyVOH4ejN1jCAPQJBVF3SWrQ50ZLqGVs9pokJx7rRUFXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فوری از رومانو:
لیورپول در حال تلاش برای تکمیل انتقال بارکولا است. این بازیکن تمایل به انتقال دارد و اولویت خود را به لیورپول داده است. لیورپول منتظر اعلام قیمت مورد نظر از سوی پاریس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101993" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101992">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=ZnaKH9FnlB6fXAtmGRHuwlaGa4JmRMNQ36wijynnX4yBxtxkUtYto1aNl3Tf2IwjdeLKe6xiTIlU62QenK3DpXihlfoffOQo2iFiR3Y4-Q9y_UWr5s3QzIJAvbQmrNzmKLxjZHf8R9UCcLqJOIL5kGljPiGkYTWDvm2wLkxLfQeuyQ7yBqKeaLX4krCgunXz_0ypIGki2EwUQaoiO8yDcWKY1bG2sDeBhyamfZqzc74s2eMEvcX_ZC822UYnpKOse5pFpn4Xi2WJik-bbrDsLc_Q8c6cj6fCO8pZOXYa70-271nO-0f-aCh7aToof0-aoTwj535fU0C4p5bpCZtUvW5MUpd0PNmmpTwCYxZTeOnAmRfn6ged8IpHoKnmAWk3J86Gjmonb4GVn05N-VU_rVAaI8Q1SkGYxvH9vNatmCstwRUNWd_s_PNETMDsZArMhoqVmnJDntuEZ2CE6oXGIaPXuOZKS6-Kn6YA0DMuiG0nd-A8V9kSLsyPzBPrBNk6dyixvGJQES1ydDw6rckB1yCSJ6JEbXXg8dnjlQYN_NAi9H8W8-7-njXE2Oivn1muWEygjYw-T85nPzcOdydMasQq74pE__ggOwrA-mTNuJXS-_jJ4u8Fx49QLywK5_W4O68lQrF1ySONYgJQ4q57fhqANdNsaRqLY94fc3pYHEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45e9d378eb.mp4?token=ZnaKH9FnlB6fXAtmGRHuwlaGa4JmRMNQ36wijynnX4yBxtxkUtYto1aNl3Tf2IwjdeLKe6xiTIlU62QenK3DpXihlfoffOQo2iFiR3Y4-Q9y_UWr5s3QzIJAvbQmrNzmKLxjZHf8R9UCcLqJOIL5kGljPiGkYTWDvm2wLkxLfQeuyQ7yBqKeaLX4krCgunXz_0ypIGki2EwUQaoiO8yDcWKY1bG2sDeBhyamfZqzc74s2eMEvcX_ZC822UYnpKOse5pFpn4Xi2WJik-bbrDsLc_Q8c6cj6fCO8pZOXYa70-271nO-0f-aCh7aToof0-aoTwj535fU0C4p5bpCZtUvW5MUpd0PNmmpTwCYxZTeOnAmRfn6ged8IpHoKnmAWk3J86Gjmonb4GVn05N-VU_rVAaI8Q1SkGYxvH9vNatmCstwRUNWd_s_PNETMDsZArMhoqVmnJDntuEZ2CE6oXGIaPXuOZKS6-Kn6YA0DMuiG0nd-A8V9kSLsyPzBPrBNk6dyixvGJQES1ydDw6rckB1yCSJ6JEbXXg8dnjlQYN_NAi9H8W8-7-njXE2Oivn1muWEygjYw-T85nPzcOdydMasQq74pE__ggOwrA-mTNuJXS-_jJ4u8Fx49QLywK5_W4O68lQrF1ySONYgJQ4q57fhqANdNsaRqLY94fc3pYHEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظات خنده‌دار از زنده‌یاد اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101992" target="_blank">📅 15:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101991">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=qTuvwES8_D9fF-1HOKCCP0ZDTf721mhJ_6xMIrNPoI3KsKuf6KgCYZFt6labpd10mjfYPIxoxyZgL7zrcIcAMX3x4tswKPMOELaUbN703z-SkJxXUFo4VjrdO29b3HFmECoUMx8erGbToG_RUMkPz1tKVaJt5efCXHw1rNS4AfDDxaDHzD_B4CfpPS-bgYYSHFmvVa16dvyYV7SG7kUKSwwDMM7eyHr7IW2LPaejQsXfBbfTClxE5ZSEQ3Tlcucb8qMUJzF831aRCTxygeY02KsUiuwGl0lvrpez5gmoM_GKP9TLrI_cyQo9ziqfu9CFflEy1LGxLp0MEih-c6__iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63baf35c4.mp4?token=qTuvwES8_D9fF-1HOKCCP0ZDTf721mhJ_6xMIrNPoI3KsKuf6KgCYZFt6labpd10mjfYPIxoxyZgL7zrcIcAMX3x4tswKPMOELaUbN703z-SkJxXUFo4VjrdO29b3HFmECoUMx8erGbToG_RUMkPz1tKVaJt5efCXHw1rNS4AfDDxaDHzD_B4CfpPS-bgYYSHFmvVa16dvyYV7SG7kUKSwwDMM7eyHr7IW2LPaejQsXfBbfTClxE5ZSEQ3Tlcucb8qMUJzF831aRCTxygeY02KsUiuwGl0lvrpez5gmoM_GKP9TLrI_cyQo9ziqfu9CFflEy1LGxLp0MEih-c6__iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
دستاورد دیگه تیم‌ملی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101991" target="_blank">📅 14:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101989">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cdfUVe1DCOdzlVQpriJxqxkamHQvnYglfRyq1-BFLIcgkNVnGl9MV1L8ilIcUWjpgH813v75MWxyyZMjJwjVP7P4KW5Wra9oSK1s3ouIie3sYoNlFiCZlhsBsONPhvExhx2lk_kceQLfhUzRhPviHcDqHrn-gu7bmVBc9n8iHYgNsx6hzs6RZBTsnHHWK9PX2v6LRD3BWe2FIX6aYMdwQlL9nNKq47pHk1plfYZDx_pXUWlj9eBfAwyQdsb7TPjAv5yFgoY3gfjjclpgfKRDze0kI5x2PvUSWykQ7JgL6d5SYnziGJvm0XSGnQhWMLypYmdU6YMm6kiJow8zzBSKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EjE05M0j2lyuXk12voG7QDaH24ka9fmLjB39TCVJGFPc0VIwgd3xJutuoXfIlHeAgs5xuKMW3mlZ6gPfdVW0rczIvVWmzgcyQ3brEZDZzi3-l9LLx-puH6kdt4MV_fbMTALtekCME4XsdAo6njbcMn27L3vA7DQrrr6CkywQkkKe-MZE6i6YECtkBre62xln_t5Y_Oic2WhUB3tiGX5RVUFcKcDqh25ZuHlkGTPGjZsO6gjF_T6_zgnISnjCZw8z7PC8xj90PSWxE1ksorkL_E4iEK42pFUAO0e0azs6odM6sJmy8jnQDdxHdQ-NsYBvGquO-dxMXbrJmz7NARpz9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اینس گارسیا، دوست‌دختر جدید لامین یامال به این موضوع که گفته میشد باعث جدایی او و نیکی نیکول شده، واکنش نشون داد:
من به کسی آسیب نمیزنم، چیزی رو از دست کسی نگرفته‌ام؛ فقط دارم زندگی خودمو میکنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101989" target="_blank">📅 14:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101988">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=RbU5WTiuumhNGLtyt4-VIt3aZRMcCSzSxnIvWHvuZJtr3mpprawoyY14_4hfCrQHlB9bPyVMQ7fDeE_P9cN0qe6ZsiaK-Tfquf-Wd4QX1ayAaDgfH3JeMd3kBuRYaFTzqHzvOBrYdqRZxYil28SBxp9LmViXIafBZG7OveV0NYPFv93jIvssCKwRjQa2MOJrWPAzzuKbjMNjH9dG3KPV5oursjLo6d_t_ke7RMVE-atrcKSyUYCvwwlaXVfxyNAkf6a1NM22pH61W7JsTAUQys8-cvUfAtAdYPiWF6Su1nPBZfKRfDfVC_lDNzu1S37O5bm7fSv_9Moo_06OJuF8GiRBgyrDWRiaaiS9DAtEE_FIEL6lqsfLydFENJb2W_t9bOjm-ibVW1rZQECttRNK4Njsz3OPU4QEQF8891oPaUlW_YhzdFbU6edMy0cb1UGhd0i0qnSV9i5TuelLGdeK7TK88iK6g5doQsQUzRvUxXjd5vcl9aQ6IJUw5Kb2SL_UMSPOMfq_4nIudC1f0oEjraqZulfm8Ju1GzGNX1ObG-QHZ6_4RKiz5VTR6iWbz6atYAtsEfcZP8fYFMc-mwqM4nZoxew7-5JiF-QeomcbKWWkcktCooVR7U7jYN8bjEZa2zEKAT3JIIqzv7bSVhcmHt75epDNjU1qqcd21RwVm_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310ebc00ec.mp4?token=RbU5WTiuumhNGLtyt4-VIt3aZRMcCSzSxnIvWHvuZJtr3mpprawoyY14_4hfCrQHlB9bPyVMQ7fDeE_P9cN0qe6ZsiaK-Tfquf-Wd4QX1ayAaDgfH3JeMd3kBuRYaFTzqHzvOBrYdqRZxYil28SBxp9LmViXIafBZG7OveV0NYPFv93jIvssCKwRjQa2MOJrWPAzzuKbjMNjH9dG3KPV5oursjLo6d_t_ke7RMVE-atrcKSyUYCvwwlaXVfxyNAkf6a1NM22pH61W7JsTAUQys8-cvUfAtAdYPiWF6Su1nPBZfKRfDfVC_lDNzu1S37O5bm7fSv_9Moo_06OJuF8GiRBgyrDWRiaaiS9DAtEE_FIEL6lqsfLydFENJb2W_t9bOjm-ibVW1rZQECttRNK4Njsz3OPU4QEQF8891oPaUlW_YhzdFbU6edMy0cb1UGhd0i0qnSV9i5TuelLGdeK7TK88iK6g5doQsQUzRvUxXjd5vcl9aQ6IJUw5Kb2SL_UMSPOMfq_4nIudC1f0oEjraqZulfm8Ju1GzGNX1ObG-QHZ6_4RKiz5VTR6iWbz6atYAtsEfcZP8fYFMc-mwqM4nZoxew7-5JiF-QeomcbKWWkcktCooVR7U7jYN8bjEZa2zEKAT3JIIqzv7bSVhcmHt75epDNjU1qqcd21RwVm_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
چنتا سوپرگل نامزد پوشکاش ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101988" target="_blank">📅 14:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101986">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SHnhLcZkeakFj9rA1339_Ni3c7AbUmtMR_bQy3VrxshdnAT7TDJuosHsRWloq0kVMnrgMplAUW49oOWb0o6DoD5CdXeBkN5e9j97Dc-Iio-lUCARSJ5LTOls3BzpVzY60OcfeTbgOWkMI8rloiNgjntE1Gq_aMwF0sFjx8fedQFVQ0RExAW8kvHXZ-fxExAtg39FPzbX8p75aVkwc2u0Zx6c0Zp2ZMQi1IKPoQAMfGNG6qigJvIU550mljRSDwu8vQE4a7UxIjFqsrj64TiAeR0VFWS15e6zeJUWb1A-qnibDMPw6_U7FrVx9RJghH7F2u3jKe41mhUkQG6kvopFPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CEv9n6p5BCYTfq9jOfO6L-2V1UIsbgOiU8L9fNI519pIHfgcsfDv8O153uyQLCrAhvJa3tCqYYAAi3r6kbc5rNpjOaQheZrsYHpU-Vlux66MukoovAvBCP0AmIBf0I0QnUsxvq1j91JYl0XISnBE88HnrUZseuqT9xo4BrBIZEfGfnOWJS1-7Fh3Cb4Jo9YHlzvechQRl_4ns8pyjs87HyhDdcB5aWJ16MZkU2PsXhfyDB57dIQYXOwOMTBQafkVoZ1dl8_XnWGqlnp36qyhWfYY5FuPpjv1yrtC5HgBmnQ0t-TYnsg5kNuXKsFEDdc_E-wM37HZPQgzPcTI53FoWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101986" target="_blank">📅 13:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101984">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ayWKF1WwyRXHExQH__kIZMNpYesGESDpMXm4lI5Ck6Nmn19TbW28MVwiWKwdxrg4GAPWi8qm2pQNSeoQQzCDjQrKkS9tXYd8c7DTcq1SPXUEvSOcuU6LmmOAekvmvpOFhzrWoKqavM3wCTB9OYqw1AyY5Dy7ikn86oCp-BtAu7Vk0k85lWQaJ6jZl3SbXfeoaoqzOOgkCErfYnB_QorHoIHDAB2-PyzsoLJDOT-XZ2e5r1Op-cJ-XOxMCZXIFdhOi7WJ8Saspd6rF9vhOAq5cwOxGsAJt7JEx2V1VAOVHNP3N9CD08lx8KiCVaapKMPRvuesgE-Gq-xRWsnwzsWnXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o50AcrqDnik7CLRh6XtJqDvacjc1Q7wRH4kM5xtXcI6PZq4vzwz9XfSlyy2Ia_T6R-6XX41qLkDXnIDyr7Vfb4cBXgi5olKuWB9krq-AP8HiMlHDy01cDKjRxG5PY7FG0KLg1Zah5lXc-yL-gPezYL-Kg2IqR5a1mQObOcnMI8UCrNR8ZA2qVhkL6zw0dchLMlGWRx5tPk19yjZq45jNeuR64KwflsCtIiRexrunkstEQWnHqKITh0SZ8SUbcmi_3iJyvAENQpicVxSRzaLSUExXZETxT_Jg2AAdOnyzeSUPXh8zJo98D65XNKng_VxwcUqQOSOK8J1pfKMcdlv-qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
جسیکا توگا دوست‌دختر سابق وینیسیوس جونیور:
این فوتبالیست‌های سیاه‌پوست فقط از نژادپرستی شکایت میکنن ولی همیشه با زنان سفیدپوست و بلوند وارد رابطه میشن. اونا هیچ‌وقت با یک زن سیاه‌پوست وارد رابطه نمیشن یا چنین رابطه‌ای رو علنی نمیکنن دلیلش چیه؟ جوابش واضح و مشخصه! خواهشا این سیاه‌پوستا فاز آدمای اخلاق‌مدار رو برندارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101984" target="_blank">📅 13:20 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
