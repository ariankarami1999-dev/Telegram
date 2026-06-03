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
<img src="https://cdn4.telesco.pe/file/Ly8Q7R0nBATnUgJMD9geHOL1M9zUhe_qMeBnYkiaSsVII3qDMYOvYP_7oVSjW53PQBbSb04gwsuV9FMH1gqlfmGYnKEeW3RcKzcovLWZWgI-sGvMdC1VwSK51ZXzOtB7qMoLuI6JDXZZPqeiUm5HrvsQ_b2Ks2mBV1hqYgytzP0EnpaZnUY0eNGGtwgQhv5wtrc5OLQRxa7zgglBe-mPabT-SOtcUJdVphkSa9h_dO8Dv8RCdHWxu8p7Ik6MJtPobfq2YhbHWHU8-5paqDDwIN093Dt_JH7MqBwwystIYPUXZx6_8SYg6Uatvkl0AUuA6kkjhJe6wKss2QC8RvWlKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 176K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 20:54:24</div>
<hr>

<div class="tg-post" id="msg-22722">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHpLxbiXdFjiiZ8rGUB5xDAwtYn2DNy38ovyu21-X4M4vybIwFN3abbyTGxbb-XRGA7SEGZR42b-u0yAo0Ed1lXEelDhY36d7jPYJGE-Ioq2bYlfdZMM0UnwgzgQaMNgx5oOYjQHlbjyno-jxu6TMl_woHwA8re-wib4MuAjBiAROiYfGCsFcR3euec2UYWro-2mTR8iXyTUycIbxY_zL5eKe6dzonhR3_WRyZ8pTGBORYgHAN7ZDMJWSxORkUw8_K44yi0UPqVE2XM3_8uAzez2xQRVtKT9eOQ2x7imU3QpA2yDb3nNKjVjpdxoZg_1dviYsMWuO2pJIQ10XAaGzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
لوئیز فیگو اسطوره‌پرتغال:به‌جرات‌میتونم بگم که اسکواد این دوره تیم‌ملی‌پرتغال خوشبختانه‌ یکی از بهترین اسکواد های تاریخه که امیدوارم با کریس رونالدو بتونند به قهرمانی جام جهانی برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/persiana_Soccer/22722" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22721">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sI7Wh3XjkaXKnuzKdjTLbc9i6gb0Q0Xn1IDXjrNClJZ1fAbFzxE38F2karDJgVVNXbD60rRz-dqw1d82BFP0tVe9NQTaTToHGKQFFj804596Jbly34nmREBMxnDVX3qF5yLlmP2hIddhZ1HV-2X1EsgA27DwTN7pjnyUy7Ci3OiO0vsR21gM4bea4hIUOsQAFQu18xZ91GTBgWfe3iYUQRnoIBeBtzwqbj78pImU5xcCIxgO8zM0Opy2oXiyncvdkMFsMgJ5jBd_or_SXaB8NuKjbRKWebcGItJNyyKKuoievx9giZXkA2BKFk0vaRBaKkUswhRpGEgshRc-f_fO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛اتلتیک:انزو فرناندز ستاره چلسی به سران این باشگاه خبر داده که قطعی میخواهد در این تابستون از این تیم جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22721" target="_blank">📅 19:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22720">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOhJX3ieTGcVeyxFs36GmkGdVj8ZzZ1A45x5dgAAFTw_D8w5kf1HmQ6RJBRcASp0OtVQke3emu5YeL7BIvJ9cgFmDWNPpSh8Wj0Ouve80aeJbhWP5AJIPcRe5zQKCqQuU25k0svfG0V-6aRsMlIBMm-A6xiRNyCZRH333Yt4AJeF2a05tpt9LjCu0bjvLKlceXlis_RnD46U45gI4n_WVes5OlLG0JDYstaAJZvD_IEF5mN2lJdvuFCXab4zwMBzT5dzWXr-T-3PrFybm8SkuujEu32J8sZhs1hlFhgk_NJvDeI_9ZDQCiL6ePdcfs5v7vtEkNSIzybEsO3NHYrN1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌آمارمثلث‌هجومی PSG فصل 2025/26 و آمار لیونل مسی به تنهایی در فصل 2014/15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22720" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22719">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EG49v2U1XMeV3EYKWWjZ5riE89pY9yrf9U5bBQgSDrDEU0544HA_Xmtyl--bU6noISFu-Knj2k0OU8SRbMxlMnjlVyaiJjYJdLWxI_uIo2zTawGChcdL-soKktEp8TjOqBwmqXM4CVFJoRWkfpecpclIMCbrBSlW17jrR_glKjQ1fTEJPClLcwT6jJMksDejp2WoKw0MSHW8NaZfmCW3Zak5krS8I1gJyikkHKz--xRgjeKO8oHzb5uPz8yH28JXkzsDgz2pWdI8Hndl1z04FPnCqzaruswjfsHjITj39uZvar3R9NJWDoIQk5ox5fgoHrueigyB8DD2K3M05dsHpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/persiana_Soccer/22719" target="_blank">📅 18:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22718">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Im3dfVxAlrwLCZq9lgpOiocN-f5jB1AoRChOMfQe1xlbx1OrF4yhIX3OFfF0E58rYhCLgpUjXyWUIba8Qe6emX0ROG2Ja03Zs21JCAAqTIrSNvK_-2sI5Ccxng5m0mxYW6-hQsTu74ygcB_W-PS8SBldTSki7shoSwZJQ-Tgwr9N3lkcomRL6CKYjKIqhbEBDWOvxGbqJ_XrcuSUSRJxePfj61iBd64JClN8IEnzLHedQhrYvssng3MduGxkK5pmmQ-zihxlNq7orRTD8DrgVzaeAkaxjfL3OHyt3DemMfdy9ncSZJBX8pmXdfY8fgUhPSB_ogVRe-hjDQ6AzqmCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/22718" target="_blank">📅 18:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22717">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uc2nSwGpn5UO3u5-nkMCkVfN9pud9wTsuCUxdXka3ni0zZ4cS2EM8L346DuyjWwtI1FxqeMuZVIfX1GoSEdor_NDkr5e7XNrc3dq-CV89tUiWbMsPkWgc-fFJMC1QTCpLqT8-e8diTnvwMpsb3MoO-e6nCmA3GlQSD9Q2cOQR2qXFHnsElqbIdLn3xw_Me6yGzy-yxStIGbKrJY5yXYvz42bHBlJQ_vtPqCvTG7vHx16InpA9vuRJ58omuegTm4hg0QP3E_YVgqLEXusHUDQlAFy5oOYssEg-G25r2cB3Ou7lfPfRY_np1qWxZ7KxY-U7aerTlJQANwpa7l4MpoGGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپورت عراق با انتشار این پوستر؛ خبر از عقد قرارداد دو ساله یحیی گلمحمدی با دهوک عراق طی ساعات آینده داد. هنوز قرارداد رسمی امضا نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/22717" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22715">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f9TloGmb5wd2mWUP0EF5StZIwCeekigyeQi0n19xX0obvXkjSg_IBUr4-1mGM4T0roJ-0Jh5_0zbY0OBgsjos5_wR4QcVpMpbyrk4vjDos6OHLiXj-k7OALjAs1WPaXrKtnJmf8-5ECCWbi-j-r0HikHp62XF2p41C1_VHdqbwVXWCcxpYRvjYrsfcZ-yEh361_ODMSogfJr73DxHrKE_G4nWRB7a17iuUI4M5PyeQ-NMr27UykvebO534X26XErxMGzEc9xl_BtDGB9slr-LLBA3EYuMTzwVpAJniFJ2P79uo5SeMm6o17MgwolooqkTlsFsgXIwxy_bqj_52aiaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIM0x8uj7DvOws32dkrfwu0cp2apAvUU2wdrFZ_o26-5TkZPo87xTqZLDcIBbRQQyGiVKKt7AZkn-eGZfZlkk2AcJy4NcBKykLptU6PC1wEFQU9qU706YwZWJI4mXvF-KSpxmHSM-hDIwUoT_XnChkwTrFlrYwQVlr5sfy4CFjgWOxYRMaN-2vRezpK9jkz8k8jjCn3ou0vsaHSNfEOFdPz7E5bfo5BKAWtLMQyNOC_4aHNbQmKmmIdHvJpfkSvd_npdFbPGBSIA8e91QFi6HXfYE4BElxsUPHntFVumN2BZe-QBhZ_pHb2PyWDC2CF-n7PV45GNsF9jI6EDIWujNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇿
🇮🇷
ترکیب احتمالی تیم ملی ازبکستان و تیم جمهوری اسلامی برای رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/22715" target="_blank">📅 17:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22714">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=SzQvm_dw9Uc_m7N7WOTQ0XK5jHcsYaKfUZgHl9TUAkEWNZwmyIAcdCLz-tcgiccp97BWPWRGScTRdRVCA0CHlvNaPsYdoaYHHaxtrfxwl8hOBo2AvWlsbSYEU3gr5E6KDwz15Pik-sk_3bN4lvDi3Oex4oiokgjVRgK5WZne1Z8X6AsRFiT03Vx3twWJBlqvH3HjSehYJpSdU-eOspu-5HmFTNPnxC5lI80r3EVeXBZYGQdMCPJGy-yJotrxk7hjpaKsYcmrbjOunDOYwIpAl9_osRBhtayvvEPQtOZL8kUHCgOlsfeucKPZUOkm3HQUyUrVt5ECAOxnGlxBLd8bmzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=SzQvm_dw9Uc_m7N7WOTQ0XK5jHcsYaKfUZgHl9TUAkEWNZwmyIAcdCLz-tcgiccp97BWPWRGScTRdRVCA0CHlvNaPsYdoaYHHaxtrfxwl8hOBo2AvWlsbSYEU3gr5E6KDwz15Pik-sk_3bN4lvDi3Oex4oiokgjVRgK5WZne1Z8X6AsRFiT03Vx3twWJBlqvH3HjSehYJpSdU-eOspu-5HmFTNPnxC5lI80r3EVeXBZYGQdMCPJGy-yJotrxk7hjpaKsYcmrbjOunDOYwIpAl9_osRBhtayvvEPQtOZL8kUHCgOlsfeucKPZUOkm3HQUyUrVt5ECAOxnGlxBLd8bmzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازشوت‌های فوق تماشایی گرت بیل فوق ستاره سابق رئال مادرید در دوران حضور در تاتنهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/22714" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22713">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdOQkj3_8dYYytVNrPT2XLDO9wUJ9m95KsXebo_6QyPvz4F62M0IQhensheo5_HDF8S9BXiaw4FWHvcwW2GnROIPmmGJyz9-w20gqf2ioB_r2WfrwwZ3t1adLNx0qmI9Np8RB_YAu4ufZUa_rDcNEXaLabAzPuvNE41v_8889x7l7htxz7LQ_aLtMZ8HR4xo0h5CsvQbk_ZNLKNkNMuJkJuHr-R0JE2AfXoRYR8ejv9YrdOVZeR40ocW7TaZuv0wo42ipK4iaACaRP69oTFJt43IiBN8Y4h9WwZ1n01x2CK4uard38nFJxoitKrfTzHr4ilaLub_FxzjuhKR3ZgKkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ یحیی گلمحمدی در روز های گذشته مذاکرات مثبتی رو با باشگاه عراقی خواهانش‌ داشته و حتی توافقات لازم بین طرفین انجام شده اما منتظره تا تکلیف نیمکت پرسپولیس برای فصل بعد رقابت ها رسما مشخص شودتا درصورتیکی بنا به‌هردلیلی‌اوسمار از…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/22713" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22712">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3esVWe4rMY0431xtlIhY5qfau2LJWIRyRIfGxzOXTBtjC2zRZDvJcQVk4oedw3Pzc8AJy4FRyGGJeg9z0tb3mz9Yan1HVjb4Ezs0gtTBGit6AVQ-StdrI4ml_BtJUIOWOC3_R1pv5Nx5OXdZ-3KAU7LNwAgSt029DgvTrb6mCcjPSkLQLFBEH4bjxm1KlCc37pUJnunXOdP7Tdh9BZ3A0Ci0Mg6V68V3OVdwaOmIjK42qqaFMlyWTucWE8Jtcsav-v2yuB-QB9ycaPLCVayWJKZq8ffYv4sccZooHiZGMGDDrMjo3iY7TWjF2fIF810VUNEMPGlJxZB0kddSiUbvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/22712" target="_blank">📅 16:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22711">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=uRFpe3p019uoZvG0dsdi2_WsYWL60oQXjLaRlVbOxHG6DBX714b0fnjRWQNopY3cpoWKSs3YECRcx38bMxTQ_h2eFz4qsAjxoeR43M-Alq28JtZY6LaEPora8b9pmQHplk8aAx0NPrh0frFxWa5wCPxaI3iHqWLBiC4WjdgTSYN2fulM5lUUJ-0jIOWksC5cAwALnpjQh1-b2CH9uS5o_dZEA0zcTxp9U0RGoNlYsFz4cn38Trg8-Lu_9yVEYHXQm-HP1b_-QPinbouZAakF_tFZIQUH4x465x428SdcAeovm6XoUBKXv6c03wgYcmqD5n0z3H8YJUbyukUQjfDMjYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=uRFpe3p019uoZvG0dsdi2_WsYWL60oQXjLaRlVbOxHG6DBX714b0fnjRWQNopY3cpoWKSs3YECRcx38bMxTQ_h2eFz4qsAjxoeR43M-Alq28JtZY6LaEPora8b9pmQHplk8aAx0NPrh0frFxWa5wCPxaI3iHqWLBiC4WjdgTSYN2fulM5lUUJ-0jIOWksC5cAwALnpjQh1-b2CH9uS5o_dZEA0zcTxp9U0RGoNlYsFz4cn38Trg8-Lu_9yVEYHXQm-HP1b_-QPinbouZAakF_tFZIQUH4x465x428SdcAeovm6XoUBKXv6c03wgYcmqD5n0z3H8YJUbyukUQjfDMjYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
توپ فوتبالی مجهز به هوش مصنوعی که به تشخیص آفساید کمک میکند در جام جهانی استفاده خواهد شد. توپ رسمی مسابقه می‌تواند داده‌ها را با سرعت 500 بار در ثانیه ثبت کند، به این معنا که هر ضربه به توپ تحت نظارت قرار دارد.⁩
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/22711" target="_blank">📅 16:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22710">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MO9-4nf5icscnuPbA6HlhRQ4YDSPzG632jb9HuzUhFpXu9HIcRinVAlfChxg_6bnQz_Vr4gm3dfN9O5WWQ_eRbrqJBoOMUelc213oLxFPFT_uONyZPQeZcWG5WRNU-f7Yq_wghFLMVvq7U_ziGjXU5d2PvyLlbUUatuKX6Oa7kpLKtjwTll0OpK35KbF-fWVqTuDnUGU-vCjWH9NA-fxlNTD5gWFPrJAi5gpegPVvM5JYPSOFxu-Ci_FsfZaK0amvIhzAcQm2KePWbjvgy8B42hn3G6OEhXz6CO9AcS6p7plZXbVUOsJVKq8GFoqaVCXMW75n6hDia2TUj6ESdIBQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/22710" target="_blank">📅 15:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22709">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAt-u6Hkka5jF8sOWjKusL_kjLalC1FLzPPj6IsjkmDlK7ifp1Oq4ZRpVonERrMDU_ECMULI2NbJRgTZRliyP2zh2sYHDg0AqWAMhr1Tpdotq8QmxCtgDOuXaUiHxeImVh0w3MSaBaJA_xPeOK_ZgdcxzigiHPKYTxFVcXkSSweDipnXVyiMWwARPeJo3sHHWUQufmML6dj4ES0G2hg3xmCyw-S6H8Q8f0cP1hjI8PnRMGGOTVldg9p3ix4S7iEBqjnnLlCTwMj9Mxzinuyx0ARM-EzByNAaob0uyVhGwExGoZFWmVQXVaEpBOxJmAncJAkbzTdfEFJAFdTWZfwEaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باحضور دنیس‌وسامان‌از تیم جمهوری اسلامی؛
لیست کامل ۲۸۹ بازیکن در جام جهانی ۲۰۲۶ حاضرند وبرای کشوری بازی می‌کنند که در آن متولد نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/22709" target="_blank">📅 15:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22708">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuMPfBZ-nk2DaRYm0dB-DXCbQWRB06R6Px_oPk4ardGlfFmIV5iPfRXYp9DLb_uUk2sxB_Guo0QfQR-I8mVgC1DcAILxx5n_46r7X_qqVOWXWsHyRXJyG7hTujfbxzWVG2bFN2aH7eVZeTUJ4NSrkFKbLWEDDcwPJHYCKVHn_mRtTLrlum6RCIYX7N-f7QQJVRkvJC9GxAr-PRACK_kAcX9tINP9gf9mWdlTfWkN3H1kSjeMfAUPptaBbWt-98SHDgLx5x-QpTmCacxzEZ3pWz77fuvC0dEY0whga_tu_EHPyYBNS3ANwV8vTPjQwtQGqdxyUp4fOVCGIZ1fgAjgkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار هری‌کین‌مهاجم بایرن‌ و عثمان دمبله مهاجم PSG در این فصل؛ کدومشون لایق توپ‌طلاعه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/22708" target="_blank">📅 15:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22707">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYaBUpKjjnPr1CUwh9B1w-C2gPQqCa47bSSP56BND5oPd7yVfjnFX5yuXLp0yXNl4DXV9be4ZzH4wvj8yVxQUY2G2UIUe8oywE_Bc9evZZc-WBEYO6wxDSj-zHkCNWcqm-zceTskbm8AyE6T3lfxdSQ7vjA8J1skQD2Dx5bxQLdgDUQaybj_O2yQKtEKgIWqkxlQVVaZ3gjezuzJ7jcfLZGnIRUwD-CGFmDMnP8P18t7rd2A7MIz2_yx88LwprWMInaDyNSM-xWx_tsWcCrVanBZeYDOIQJ0xHT0gL1GAxNfczhM10QOrtvVtdy9klefwl7guyOYzCWx3zkrSiIFig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔵
راسمون هویلند: امیدوارم‌که باشگاه ناپولی در پایان فصل بندخریدقطعی من رو فعال کنه چون حقیقتا دیگه‌علاقه‌ای‌به‌بازگشت به اولترافورد ندارم. برای من بهترین بازیکن تاریخ کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/22707" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22706">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSu3KJcxRHAtAF73HUuUYrhOgwOypPEjNK2oQoavO2XglyJypoIb2d1mNbriimmbbCsSncCBzgJZ4y_LV80Ybpdm5L-9H3UVQdIIueWr56JHz06XpSCQDWgQoDz_6e_ntPPQQveMasyUk5YtClG_wOzKrKMLwD26YIKJV4666edwFBBfUxaOERay89n_NvpJJExGHNJpO10tYg7WGbyziRQQKxm8BXKzphEWRGS8j5DpQu0JCUnvq2zNnZjqeRWXJXS4IfIr5iD7FRvCwbIhziTRk3fpewsfTcvyY3cA9z0mSdX634AOeBtef7ONOdbgLhBKbtkTSbqb6zpUeCCTdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💣
#تکمیلی #فوری #اختصاصی_پرشیانا؛ یحیی گلمحمدی علاوه بر دوباشگاه‌عراقی؛ از باشگاه تراکتور تبریز آفر مالی بسیارسنگینی رو برای سه فصل حضور در تبریز دریافت‌کرده. مالک پرشورها قصد داره یحیی رو جانشین محمد ربیعی سرمربی فعلی این تیم کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22706" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22705">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=tEBl-E4ZJ61HpNZwumgR8dheV_DvxcHn095FAH0dv7kPQVpxw1mk3IXjojyBtn7hPSFcgTz3HYlNipZW61efMawSM3sFC9JiTPIwLyZLqyLmMMFf4uRE0HC_8DUT8dpXZeuogOak__GR_ERmcBQhUNBL4k9gnTQXBIEJfIHSL9o_ka7QLAjXD3Kkuikqh9M98Oreu1Wa8-ekZ9h5F2bj-YUV0bsOOIaTJNWxpH9iIEefADg1ijSbbz5EWkaNpJtvtXtIhKK5h6oqjuxnDEOdm1mOqT3MhQH4AyDBg-fbcyWscRNkianDR2BWg92clHXsatMwl75d6I7eeUAc52yGYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=tEBl-E4ZJ61HpNZwumgR8dheV_DvxcHn095FAH0dv7kPQVpxw1mk3IXjojyBtn7hPSFcgTz3HYlNipZW61efMawSM3sFC9JiTPIwLyZLqyLmMMFf4uRE0HC_8DUT8dpXZeuogOak__GR_ERmcBQhUNBL4k9gnTQXBIEJfIHSL9o_ka7QLAjXD3Kkuikqh9M98Oreu1Wa8-ekZ9h5F2bj-YUV0bsOOIaTJNWxpH9iIEefADg1ijSbbz5EWkaNpJtvtXtIhKK5h6oqjuxnDEOdm1mOqT3MhQH4AyDBg-fbcyWscRNkianDR2BWg92clHXsatMwl75d6I7eeUAc52yGYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تکل جسورانه تیاگو پسر بزرگ لیونل مسی؛ این چند ماه که اینترنت نبود احساس میکنم از همه چی عقب افتادیم تیاگو کی اینقدر بزرگ شد، آخرین باری که ازش ویدیو دیدمش دقیقا نصف الانش بود
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22705" target="_blank">📅 13:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22704">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXgTjAeTpQjyeWIi1HdnbInM46tXTebLiz1OdSB6x1wgYd6cItzD0-i0CzkF0bNwuj1MGO2TXl79v85vB2vc37d5DSDURi4V6smKFwgUhGTkbHsAAJwPOv6wrC_j50UN3xt0fY3A6i3GutzkiuhCB7776tYqBexWUR0OoZ5xLsNgqKUSI-qNvvQZqoZBtDf7uUpyiXidPsG3UT7UhgTAAN-dipY-3ms-qDN8OEa4A_SOf3OX39_4QDPqsJtK0QA1AuNIC-PDnHMLPB0Ou4qwaMoEsd2j1ZMjnjWwjuo8I15S4nPXYoNDpUzACbU8s--5gre0oD0qIeIedXJyVWxqVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|رسانه اسکای اسپورت: ژائو نوس، انزوفرناندز، یوشکو گواردیول، ابراهیم کوناته و باستونی‌فوق‌ستاره‌هایی هستندکه‌علاقمند به عقد قرارداد و پیوستن به باشگاه رئال‌ مادرید هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22704" target="_blank">📅 12:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22703">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWllpba6CZmYLhCKBmECvgQmutNxWh0TbWGbhjGAb9PM0jfAATT6v3dAUZDbOZP1P_9EbPpf9ipZjh_7a0z7RHhCtrqqU2xm7GEFvB2hVsZTdPp5ofCWKu3cKeuUixYVUdbz1arDpGKzQV3sx1Op_R9yGSnv9s79ifsANKIIfYA6dVxbGi6X1b3rKlLf0UjphffdGy0s8FLUdEPelBwhLViXb-8m5aXdGToWi7VytvBYiNrcyC_ReecgQPBS-Bs26SsNY_zVQSgzCgMy_AfT5KuAmdxZhk1E5h3wUQXk1wyU8IufHVJcyW_rotGlRfx_9OWxA2fA-Q_fixH1lyg16g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌پرشیانا؛علی‌تاجرنیا رئیس هیات مدیره استقلال تماس های اولیه خود را با دراگان اسکوچیچ و نماینده رسمی او برای عقد قرار داد سه ساله با آبی پوشان پایتخت بعد از جام جهانی 2026 آغاز کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22703" target="_blank">📅 12:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22702">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8Eg-VnK6zXDOTRKaPv4By0BFApAs_5dLzn3rh68zGa8YrMFccpJ0ttIDWAl58jLNBK6li7YsCCN0_thpyG1-HqLAa_TBIzY40QbJkAZtXh7hoosoeskV6NnS1cI-YQYH9qEQF9QGlbeRygGnphJmw44c1Un4hI4Mg2y7QwIE2_v0H0bETLv0XxOdi3KZba0eL4w3C4OyVhyWgdNfUHpCGqohJ0prQokO5hec4kSke-lqVnshTDtxhB8bWMTswRoEAElD9k7Slu1jszfDzHDdi01Rbn-GeqkB3b9sfUBZHNiZm6mWdTuvrsJ1CEwNiHJpnJn0dnHRlnl68fuO7M2Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
هری‌کین‌درباره‌تصاحب دوباره کفش‌طلا: ‏«این یک افتخار است، به ویژه که فکر می‌کنم فقط رونالدو و مسی بیش از دو بار این جایزه را برده‌اند.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22702" target="_blank">📅 12:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22701">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agYM0pcE_hs8pG--CK4wbBEifipBTVFutv7gUY9jgUQv77nyUBlE8i9fGgTf23hw0FErXoCJjAbRbky_PUdTyGwrvsOqqHVK3V9Jt1lvQjbMbuMuI8GZVR1q7ljgt0MRIrlHHbwujjlJSpSaQphx6Fbl4GrRpdlJMBT5lk_EG_yb9TwVucfD19uoLfBApvtNfkA5gA6J1H9C6VN9h0ZFg3vTAAVx-k9H1uxUEqAg3dDX5DQz89sszNZqGQoNf5-c3SWc0BaWbZ4O7hkYN0JOjhwOQ1wRERifiGHEdK8PL4GV95gAi-KGflsSwmxPfQaCqIM2iLL7SluxvlD__Q5SFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۳۲ باشگاه با بیشترین بازیکن دعوت‌شده به جام جهانی؛ بایرن‌مونیخ با ۱۶ بازیکن‌درصدر این فهرست قرار دارد. تیم های پاریسن‌ژرمن، آرسنال و منچستر سیتی نیز با پانزده نماینده در تعقیب صدر هستند.
‼️
نکته‌جالب‌این فهرست، حضور دو باشگاه ایرانیه:
🔵
استقلال با 8 بازیکن
🔴
پرسپولیس با 6 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/22701" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22700">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=bUuKbCkydOiZb4FWt9J9hIJZ41rBnlg2klDgMuSVs66SsWziecaBbDNYomcA5lLFE25pm7Nk8zAh2FaQz-E5c77CyNI7IHQuFOameqY9sheQQqLwrpS5MNEGNq9SHaVGKIVYpc6wuu2GonDuof8oHFA5sPs82WxlIK0D2f_9hQur-HJ3jcEkD9g4Xvh7TdaxWns02NJQa8Fotr78UvczK4_YUJ7Fp72bAev3AkdQcI0P222MGSPp1vRorXkdEZebDVN94er33uZC0PxyqRzM6hg4AvLSbpUphpDW-4eZ0erQfIC9-QWn9EAM3FKleMju_NSUS4pxWQVzuGrSXVb3VkES7pT3VW86KXHeIY0DtCln7IL4kcWm5fLiT3RP8HNHDlmekI0ErNbPxzVsnJVbYAaZOlmsLXxLwqiTNlKlIzyhuEi2zMWrQSpTHpIb8FIT8kF5YujEFXsUTAy7bU2yWxRTjqznemCJv8-LFRuOMElnApommNd-hVCszQozy8pndt__fYu_GMwq3T2XsQESb5bfwVv27kYiVdL6YGgrRDZbR-66S7hD93Y0TEbImVWAxFvvj9fSkL8JlwrjClmC6qt4oqRbB1S60rcpKzxXAXFE4q_uv2c69bVdwRaU8srmy_ol4j0HXVeXPshf7QhyFiU8ltI4ceGSU0UJErK1TbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=bUuKbCkydOiZb4FWt9J9hIJZ41rBnlg2klDgMuSVs66SsWziecaBbDNYomcA5lLFE25pm7Nk8zAh2FaQz-E5c77CyNI7IHQuFOameqY9sheQQqLwrpS5MNEGNq9SHaVGKIVYpc6wuu2GonDuof8oHFA5sPs82WxlIK0D2f_9hQur-HJ3jcEkD9g4Xvh7TdaxWns02NJQa8Fotr78UvczK4_YUJ7Fp72bAev3AkdQcI0P222MGSPp1vRorXkdEZebDVN94er33uZC0PxyqRzM6hg4AvLSbpUphpDW-4eZ0erQfIC9-QWn9EAM3FKleMju_NSUS4pxWQVzuGrSXVb3VkES7pT3VW86KXHeIY0DtCln7IL4kcWm5fLiT3RP8HNHDlmekI0ErNbPxzVsnJVbYAaZOlmsLXxLwqiTNlKlIzyhuEi2zMWrQSpTHpIb8FIT8kF5YujEFXsUTAy7bU2yWxRTjqznemCJv8-LFRuOMElnApommNd-hVCszQozy8pndt__fYu_GMwq3T2XsQESb5bfwVv27kYiVdL6YGgrRDZbR-66S7hD93Y0TEbImVWAxFvvj9fSkL8JlwrjClmC6qt4oqRbB1S60rcpKzxXAXFE4q_uv2c69bVdwRaU8srmy_ol4j0HXVeXPshf7QhyFiU8ltI4ceGSU0UJErK1TbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استفاده عجیب از گاز اشک‌آور توسط ماموران در بازی این هفته دو تیم بندرعامری و شهرآرکا البرز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22700" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22699">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22699" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22698">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzMUI4ZfWrmqS40OHnaMot2Yhf6LOXpWiuWhMum-CPV7bJmmEWp5s-GCk3u9d6OFLpg4hCX7s64TSCrLB9h--XfIcJfEcPmVE4OBu9ENVFAASVyaJRgQMBbW-5kCcWvJq275if9s0r1T1dTy0L50Igbtcavz8O_ho45WREsQOt5TPwyPddII51fmENspYyvTWXnFb0E_iGhFgv1nvTKfvX7HdfbDUeXlnTJGXL-W2x3rcjaHgjXjUfYsqZj0C7u-uBldZoAoOKTJvYju5c0YZCIWq-ICgAV1_AdzWWaXcaLjL4A5bQEIJwoMbwDbrdzGQaLxbsDp4ekojEPJJ9oX7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ دانیال ایری مدافع 22 ساله ملوان اصلی‌ترین گزینه اوسمار ویرا سرمربی پرسپولیس برای جانشینی مرتضی پورعلی گنجی مدافع 34 ساله سرخپوشان در تابستونه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22698" target="_blank">📅 11:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22697">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خلاصه بازی سوئد VS انگلیس؛ بازی‌‌ای که زلاتان یه سوپر پوکر کرد و اون گل مشهورش هم پوشکاش برد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22697" target="_blank">📅 10:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22696">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6-_mjC_aP1qcHNGN1Q9n--DWU8NWP7GWBTuqtM7vghy7DG9eUd7gaZwdihnY9BIGWYlDYvfcfVkuPIrMrrSSvm1npLOH_SSftQQsuMFVTlWH1gwgxNOxub08F4pj-xNRcO9LDvtq5GjKWo7CgUf4PkSNwuW15VLwDT-khRWQopuIztqCRtEDZh3E2mTalYwy-IRrpVC-oOWgIS4h12sJ0zDBBbCY5qamAAwQ-Va4H80wP78dc7yc0MU-bBvt8jdnj6h0QQ1cNxDju-S5sdoxULDgZE7-htY0SlBxa4GSamTKfRMebZBm12Dl2SrG3ghw_Lo0-LyXc8Cu0yN0deBlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسکالونی سرمربی آرژانتین:
مدعی اصلی جام؟ بنظرم تیم ملی اسپانیا قهرمان رقابت‌ها میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22696" target="_blank">📅 09:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22694">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViwDVVTofW-QyFaCQspQZe94UO8ZJhHbRINBLaFJxa-ppURfzzulmCi9QnyAT9G-20Y1Eo2eyTrCGrLlhL04qR6n4ogUxkrJip4KzQumUc0DSkzkhPoq_GWuPbF4aDUwi9E6SauL5Of-nqzjG9Us7u6F-d0nJ3xorfDF6h8DZDoOews08Mzjt2DKCvDxOhZqaysRcWr6B-Bk6c0_1844bwzTD9PHrB7Oky05tVvdu7r8zJC40mV_soPNvyLFgT2mIqz4sFk3Jr0qXG1HSZtv0hiAEm8PpZzjLQx573wQs1X_oempw0z-_F4EOSKRPbKD79FdtFhevdI4vq-hyoWgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اینفلوئنسر برزیلی کارولای شاوس لباسی رو که قراره درجام‌جهانی ۲۰۲۶ بپوشه به نمایش گذاشت؛ اون با پوشاندن بدن‌خود باصدها برچسب از بازیکنان فوتبال این لباس رو طراحی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22694" target="_blank">📅 01:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22693">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjmAc6LD3I30Mlh_jLjnMb91mP7fP1qs8jDkMU2YdwVZG59UMX4076pl4YEbLnyxvCh-HGwgV5fVS7ZATH2qV2c9hefveHk-_deeaXnpB0FXkvan1XIRzOABdcSPHo_40dtxzeiQ_CNJK3l1L1XjXkjyfrB91jZ41jaxI-rfZvPNEl1_bEKwpXpiGIoQ6wFu81eeh1rKkLDFgJ3wYMMXWqoRsIXsE2TffictvJcMZsjUgCbRqLjVc5zIYDbZaCJCGpfLDbfcR9ekZnANlvazIvMlPHrRrxaGAQYYCdPjkz_o6rqDET_78qXSXL9qm-6IFhuJcbR5LWBsRS9YPBprng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدار های‌ امروز؛
از تقابل یاران نازون و کریس وود تاجدال دوستانه هلندی‌ها مقابل الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22693" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22692">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJNADIzkO8QmMR51xzimY5MVo8UZO1be5G_EtoUvcQmno1j5F7XZbrzmWjZntTJ2XBe0XJ88xnHTVYhikRzXZ62C6iqPrxSB5rnzKQRZWvNg6MDY2zi2Uhy44_KKcRmYlF7EtVDjGCWauCBnAhmastK5UTMp5RZT5kLChtgaO66_hR5Gg2bFtDjJ6SXCR0gPJgycIvjIEhcRVBtlreskU_32YJONEp1y82kQtC-Rfz5rB80M2z3vDuFp0agczLvpaG6TJprrv8JqY0AWhNthQliI_pC1nSZwxVLgcdgMft8HlLsUvJfWuCdyH4ywu5UZAdxPsQyEIkhX8Abkp7HMfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست‌شاگردان کاناوارو برابر کانادا و برتری بلژیکی‌ها در جدال با کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22692" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22691">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6HEM-ixABX2xogG7uZC5VDgQXBpnSeHmgZ63N0DubowIqSfdebXYJa-VRSzMqpXG4BKWywVTkZBMQwREqywS7OPBFcZgVAEiDCUEh1cdIANPQZdS-_CG-kKDRAysJ-NAB-2KIe43oZW1e0k1LzzJEIHXetpLplei2gyidOd6zmmUEi-CJn0Lk2-itCCDD-vbjAxxg-q-r8R0QCHc9LzPmKvazU26cqJrNj8mTgREgztVA8XXIzMAXvTep_EyygXIT7PBqrJiPxpZVdOVlX9mgcmEfVX4bQPY7DEHlbH3RNDGLEjuzYsh3I888DL-Limoty-Uof6DUkaodYThAWzwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22691" target="_blank">📅 00:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22690">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0TjJvuq7U9fUDOCYOO4TmZtbXQe8QOKFfJpTXClRYqDdWwX9xwKNwYeDlAu0sv-gSstHfffqFxMX6scKBqLGIB05TC13uQtu1pO5SlBoPm-OwT0RnK2QOFkZ85b51aMPum3aONH6wn86I2FvI95-FfaK-KnKMt0pYG9QCRXhKPZUb4xJ5Vk7caSU4UBALHyHUbzIADjeWbQivsT12prfOj8VNnzHvsykggopLftbKwrJf0V0uXGindtEtaBFnfVk6yg5cZjVs5ZoV9FSpUOgRZ1C4UOLbbXkBsoSJfNDNT4zo_cfiR8_VT-LkRdl0R627Nqn9sN6ERJCSv9ZDPGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22690" target="_blank">📅 00:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22689">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=TiZ-v0iMw8rh8HUKeCkRlvEFWRQgLBdhO1Nbijm_KCF53cbNYKFNiRVK0ZK9UiaUiS78V7nf8wHxBWcPp0Os0-eBtEZ1CS4xCcTNisRq-sqIWMFJEYgCMxRcCP-lEmUPi_z45xbDn4kwBPVF9bfdXE5NIYquf50Ey2mCWjDq4SEJMUKIJofUViQeuV3hr-SzBKUZVY_lbz7-uVa5BENt6s9PqljQ6wkj50K7ffjgDtKiYTucC39dRZ0CjBHWGzwUfH5Zd-MZajix7wFoOjHFMPl0rU1onSo7_AIW8w0o6Y91F_2IVDAFecFW6ISbcMadplr7lfs3VSDl_1PDKw1ZEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=TiZ-v0iMw8rh8HUKeCkRlvEFWRQgLBdhO1Nbijm_KCF53cbNYKFNiRVK0ZK9UiaUiS78V7nf8wHxBWcPp0Os0-eBtEZ1CS4xCcTNisRq-sqIWMFJEYgCMxRcCP-lEmUPi_z45xbDn4kwBPVF9bfdXE5NIYquf50Ey2mCWjDq4SEJMUKIJofUViQeuV3hr-SzBKUZVY_lbz7-uVa5BENt6s9PqljQ6wkj50K7ffjgDtKiYTucC39dRZ0CjBHWGzwUfH5Zd-MZajix7wFoOjHFMPl0rU1onSo7_AIW8w0o6Y91F_2IVDAFecFW6ISbcMadplr7lfs3VSDl_1PDKw1ZEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه عجیب از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن به اونجا بود.
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22689" target="_blank">📅 23:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22688">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIu0lawqJqvI_3WDCdWTAJHiHYoXTOxZwhs2t0v_uUuVnso61OidN41fTkdlaHWtbKJvg9KXAZ3xLGIvZj0CBo-haNlS1L8zBNbilPPXNad68TjufiJfcJE_pWnSpEXIcRj0Nkhe_XRF6DWekMzw5MnbWDKx2FHQxZCX0bRMzDN4y0QvP9Lg1bKUmhpXhY0Mb5lBYLxsTfyefCUdnz8QLdWi8W3jZwjIknC7mQ0i5_Y12l3ZufBYFra0OQDOOPpjXCUplXEXDS4aF0CfOW-hhL8eQh4qjvbElOgtVDZs9vwh6z4_RcOyGvQBjzM58YeBqEaoF2LrdABOQh2slf-bJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رسانه‌های عربستانی:
باشگاه النصر بدرخواست کریس رونالدو پیشنهادی سالانه 85 میلیون یورو به برونو فرناندز کاپیتان منچستر یونایتد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22688" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22687">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsvDMej_ov5W7cB2Nq4u6Nq4Mg4t3gknkKn56ZDtypsSPUqeaxqKqQjvIo0pyQ2kNvnHjUNDLkYZiyGFEMa51_XlQda7wH-DK_eZEBtKK-2kyUY9lautJRCFEKGtWyISq5UKf_OjuYXJXNOyibrPKwRA5-Z3j7uYYP8Uk0VqZChfFznPpk7vnH2KKyuw5A7ZdD7yaWLcUSg-XME1bUIIbznKYTXqpfNWoN4WjeWzHUTLblg_7SS5p-mQCT-hiDBmENEnX2iIVynPHjkNvHtgU42TqylEkZjUoZ68qXErq1W2xLnJ5NTlvhIYYKdEX8hjSn7g19zCyaIvKz4tNS5y8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ملی‌بلژیک‌درفاصله 19 روز تابازی با شاگردان قلعه نویی، با نتیجه 2-0 کرواسی رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22687" target="_blank">📅 22:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22686">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsGxHBOv0EcIqPsxz-ikA_bNGdL-O3ZWfrNLlfve5I1uMDzJqBt4qskzuR2xgkNBH1kSfKew6gBgegyGr8paINYZ5J5pripq9GfXAt4Udn7UGqhIXhOOLSNIPLEJ6RlZPWiwEVPXgZztXnV3x6uButSck6_dDMYMMFgR2UizE0VN6Xdnz6Kvn7ivpUdEOIawG2qyzaOC5OzdWAk3zk46iBEeyDNLDqxxnOi7RtmPrONBNtr3bn01fh38DE0aKGguBaZOi1iqkHJ6Qtm6nW6HXTY3LvFZLLdQI5YOu4h6amMDtv8UHSX8dPICNtRWGO_9SzhSlnK--YO9MKquroG7Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22686" target="_blank">📅 21:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22684">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291786993.mp4?token=cNTXpjeIVPkiY7AczmGDWegwfNYBcb-5XPVyZlX3EwcN0L_DQkK3C-3nM1xzh6Sn3Vbeh_6fscyz-Yds1sZ1QYua-I2cA6xfm2T3rjB9yFfT4E-fxCzU8406RzKKy1ySBDDsqsh4cptBJsahndXlmYCXTrqEUlpM9pmx7m1Ag3h84tijeUVbrpu33JeAZB38Wc-hK-bGcwWiy1BzljEAjVknUlYXB23hYjcXmL9uSXvKpbUj9Fao-KB9ewe3ml7tiLUBaeK6Hpz03HwyOQvznZbe6r6_gIY1iva0PRHihpP0kS0n6v2TbBvyM1TfjnKLBBIbx3cJSUOIE1ErMFM41g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291786993.mp4?token=cNTXpjeIVPkiY7AczmGDWegwfNYBcb-5XPVyZlX3EwcN0L_DQkK3C-3nM1xzh6Sn3Vbeh_6fscyz-Yds1sZ1QYua-I2cA6xfm2T3rjB9yFfT4E-fxCzU8406RzKKy1ySBDDsqsh4cptBJsahndXlmYCXTrqEUlpM9pmx7m1Ag3h84tijeUVbrpu33JeAZB38Wc-hK-bGcwWiy1BzljEAjVknUlYXB23hYjcXmL9uSXvKpbUj9Fao-KB9ewe3ml7tiLUBaeK6Hpz03HwyOQvznZbe6r6_gIY1iva0PRHihpP0kS0n6v2TbBvyM1TfjnKLBBIbx3cJSUOIE1ErMFM41g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بدل‌های ایرانی لئو مسی و رونالدو پیش‌از WC
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22684" target="_blank">📅 21:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22683">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFSA2DN9DSnYIpsNhbs_epnlbBAUy213iQ1skdhB_GRTV_vXpivIkaFvS6n9tjzxPi5Ue5zqIOuZmiG4TiOh8XvSuiHVLVHv0hmWyfO1k5ipWkWB3DNQ_LSB2LopetPxHh6ecIzeXTA1-wSyATUuErxChPiZvbgl5VkY-s1T8YB-FIEWt8uJ9a-vMJpho02tw-6V0s4f-cFawHEBX1UqxJiLyDS78oUGcVDnk38SFPvp2bBkCgQraR_tArY4nRwF5WmykHrTjyLUNrKvXSaTZ21ugJW19IQlF_iR95yrWIVcglbzOEZ1r46QXEM6QFCFxfDGSOR-ndO6XkRFt4pmgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
فلش بک بزنیم به سال ۲۰۲۰ و شاهکار پدری درسن ۱۸ سالگی که تونست طی یک فصل ۷۳ بازی رسمی رو بازی کنه و قیافش به این شکل دربیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22683" target="_blank">📅 20:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22682">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=FYLj6lMx8sVxDA48Gcx5-4S7ZhlpiKOi_zAM73bqm0WzTm6Rqqrlw1VnurZALLZKZrLmz83eITHP1RIy8Fb2fyXUgKYHVJoh2NabAieMfSTuEFQbI7BYmu_Ult_p4_a96xdM4ijUo2i_7pPbO7ZHrc7OAXjG1qBaehIanhPWTAME4yH09ZGNalV92PSpyJ_G74yURojMT5HDA64mU1WQtyAxh3znpdzqIIn1_374G_Lwnv578hGBA-LF5boG-dR_hAYozToEnHHylEkMbcZaV0Eor6pkRKW8LxSa4ukddaIse_A_6ZjCjNTrY27M7rliOtj7d7WYZfo806b_lgh-Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739be8e1c9.mp4?token=FYLj6lMx8sVxDA48Gcx5-4S7ZhlpiKOi_zAM73bqm0WzTm6Rqqrlw1VnurZALLZKZrLmz83eITHP1RIy8Fb2fyXUgKYHVJoh2NabAieMfSTuEFQbI7BYmu_Ult_p4_a96xdM4ijUo2i_7pPbO7ZHrc7OAXjG1qBaehIanhPWTAME4yH09ZGNalV92PSpyJ_G74yURojMT5HDA64mU1WQtyAxh3znpdzqIIn1_374G_Lwnv578hGBA-LF5boG-dR_hAYozToEnHHylEkMbcZaV0Eor6pkRKW8LxSa4ukddaIse_A_6ZjCjNTrY27M7rliOtj7d7WYZfo806b_lgh-Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شادی‌جنجالی درلیگ آزادگان؛ سلمان بحرانی پس از گلزنی مقابل تیم نود ارومیه، در شادی جنجالی و بچگونه گل خود حرکت گلر حریف را تقلید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22682" target="_blank">📅 20:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22681">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqnBaMOeMzr6YvLGsMNhrzn2cRKaF8KhSu8l07vnf6HXKl1aN0zSiX9SX3F4_lx-mjkhLErfN2JlNPgZoyQ2Dl6I4qdz7gsx_vebdSCME8cPZqRTN65aLKnDADgt8fVlAWQ8blDiZauqS6tFYRUYpx_Z3vsBiROu_JMbEEI4KQaSnH1DyUpagpzjiNGoaXu4UiRYZGRCjSu4zfyUvA6BRqG1c2eabwHI2ggLQUyZV1dv9W0uK79Zp4FXNKxAUEvwojUTEorfhcTz-zz9R2YdcNH6JZtZPuF39GsAtnskp9zQLMlxskDXEzASfStdumFlX-QX5RYofftBxCvIhloUJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو 25 درصداز سهام باشگاه آلمریااسپانیا رو رسماخریداری‌کرد؛ 7 فوق ستاره‌ ای که سهام باشگاه‌های اروپایی رو خریده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22681" target="_blank">📅 19:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22680">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=gYx2E8u_4yJsh8S_x5aYvwNvQJ5W21jqrdv8TWxtuXXahzXUzPj3i0IWV53N9n8k95df7iro0FXUx4rGLhOoAdVRGPHSL0Zf8YpKEDS-9Zi3EN5znLSsdMAK_BdKEba2N1VaexVotPeA8DMT_lVkcZTWHpjYjKcJrF5mXbD2-vQ4BKkw-8TemnGexFWgylqyELsDHwtIKIyNRE8H0PPoUZ4q85xky_9QH4yaSdfk1zy2w782nI9EttxELyHCC_5mkgk1TPQTI55Lngj6D4qW5n9fYev0kn4wOQYyDRKw1MrJyuD-XJEHKllBmU-zuU0-XKh5F74BQDCmjt6JmL6B9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5549cd5855.mp4?token=gYx2E8u_4yJsh8S_x5aYvwNvQJ5W21jqrdv8TWxtuXXahzXUzPj3i0IWV53N9n8k95df7iro0FXUx4rGLhOoAdVRGPHSL0Zf8YpKEDS-9Zi3EN5znLSsdMAK_BdKEba2N1VaexVotPeA8DMT_lVkcZTWHpjYjKcJrF5mXbD2-vQ4BKkw-8TemnGexFWgylqyELsDHwtIKIyNRE8H0PPoUZ4q85xky_9QH4yaSdfk1zy2w782nI9EttxELyHCC_5mkgk1TPQTI55Lngj6D4qW5n9fYev0kn4wOQYyDRKw1MrJyuD-XJEHKllBmU-zuU0-XKh5F74BQDCmjt6JmL6B9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پست برای رفقایی که تمرین بدنسازی انجام میدهند. بهترین‌میان وعده‌های‌قبل و بعد تمرین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22680" target="_blank">📅 19:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22679">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-gBdUdJMIfVW_mmcOhWflBZ4J-9aU3tnUGEi2JNdmKX5fq5lfVYb_fNS1AaT2i4f4lEw5xqbEhOqb0k0xKGLrkWvr6dzN1a1T4ENndoyJsj7Po-sg1tgR2Ut6NbBXUf8mkBITIXAFVline5q854C0anKR_WDSCh57Pln8JrVPWN8-DKDhYnaGNDyOATgEmw0Hzj5Wdbt29cq_tZrK21Nee5YqK9SPN0pB6u3xmjemNh2muMnzKCJma3WpPTjGVqKS0b_7fRHsyGRXI6GiD51lOnZckdXTkrJXzWxj3ellzIKBUGaimh1ziXPcyynWt4_TxXArN9Xx20jp45NBfnRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام‌رسانه‌های‌معتبر بجز رومانو میگن که بعد از ابراهیم‌کوناته؛ خریدبعدی کهکشانی‌ها برای پست دفاع دنزل دامفریس مدافع راست اینترمیلانه. ممکنه بزودی خود رومانو هم هیر وی گو کار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22679" target="_blank">📅 19:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22678">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwEJXxREGjCY_s__n4tFiZ9UgP1ZtNaRDNZNgfAYbMD_B4I4TQKZHWb7B6w2iOdvoToBIPKUQ15uRsckhQZ5g1x3vdcJdkbx_E0GJ2_RjY58DjJntXfyvMVrrAKJaR_wsDqsOnDWnP652vlD6vO7fLQ4-ubb8-WQy2URsYMB2mqdZuegl-u9NmQQVTUFpwhLDc63N7PAvr3hO7zuFLy7-NMmIrTGnABUsTK1rbnB8Y5iaGx-bMqNliqxWQmwpE83l5PfZUHs-4Yhoo8hr8UwdLZ1UnHBwCZf_vBaUomB3kn3YhhDXTlPPuXNdTUD23qMnzspY_29CYMGf8Ey03BEVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22678" target="_blank">📅 19:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22677">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGC0SpSFQVOtsTD3unkf9ieuI25truksV_kfr0UYSkKqn_tQT-dNMhDsWgCZBXqtnbNqUNBUvQCaRxlrgs7bEP8ULjq9sRYvifGTlEIH12QItILh_U8UGJo5FCgN_S-7t-NSIUhSiJeLqBisq3ziOACP6i7Juj6jgRor1pZzAX73ctcP3-cdGe90DqLdHel2uUr92bWjFKAsJ6NzZKR_0aGR6N3ijQ3u8sAoeosMmf1_CCg2vHo4YfgExQs5K2lNxrh_VJXvGoiRzHBbsKlQ-AjhfysLQI11zKJdfUTOSHuQj9YwJAsKYu5k6mH0kWw0AgUKuEZPMHE0rvTGkCEThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارفوق‌العاده ویکتور اوسیمن ستاره 26 ساله تیم‌ملی نیجریه که درتلاشه در ژانویه و یا تابستون سال بعد راهی تیم بارسا شه. امشب هم عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22677" target="_blank">📅 18:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22676">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2PJQXTiNq8ikd1YFgVlDaRZymIVN126VESyNqFyUfjVGyOpaMq4NgWVo4KyiMbBThxjivEdTkIZLB3OibXgwVqRqOKCijb8xU3z0Mr98VQYPu-GdTxM8Bn1K6zjINAlauDKhldxo-SBoWk0CD4RayDNEwrOx9Y--DdLnR_C1Hplmb2OOEyOlK15l-vLBNRltEcd8J2e3qia7lb4ikUbcFyA8OvStLPq67dqApPKcOrnBxwlvqZ2EhvA4iE5g0sPIs26hx9JBx1H10yEDhof6TP3ii7XY17RikWMjs3smuwSf3i8nFYhzR89TTxv--iOLGN7OOIdaLGKyd5VYnfBCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام باشگاه فولادمبارکه سپاهان؛ انزو کریولی، مهاجم فرانسوی این تیم از باشگاه سپاهان جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22676" target="_blank">📅 18:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22675">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=ZM2-AZCy71b01AFfTNF4P2CftQlzoRKNTGQoVvYynlnf1na9WI3KGhx0kyIxgmQ6hQtaoLv7mrVU-jhuWBoZTeee2ezy-GChtZiSkYZpuAsLHr-CkIbdkxbk5f4hOupxV1AnvY-MEAYR8hCIwc6n13s-MDj6MJxt3fn86gj05oNI2mZB-uMR_oShWAP96usFkZ9nl6y7DNGNtE-JOoivff4TeZb7OFLhPRDboAYp09xGnASTWOLPo-CAmTqdmhsrdCf7tfTgPuXhXU5i8U004kFV-q_auj_kfIFgtsp5U4e1LgPyRjIoxNd0Xa3sm9w31ozWv-nKsfukbBWEl-OgPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c124dc30.mp4?token=ZM2-AZCy71b01AFfTNF4P2CftQlzoRKNTGQoVvYynlnf1na9WI3KGhx0kyIxgmQ6hQtaoLv7mrVU-jhuWBoZTeee2ezy-GChtZiSkYZpuAsLHr-CkIbdkxbk5f4hOupxV1AnvY-MEAYR8hCIwc6n13s-MDj6MJxt3fn86gj05oNI2mZB-uMR_oShWAP96usFkZ9nl6y7DNGNtE-JOoivff4TeZb7OFLhPRDboAYp09xGnASTWOLPo-CAmTqdmhsrdCf7tfTgPuXhXU5i8U004kFV-q_auj_kfIFgtsp5U4e1LgPyRjIoxNd0Xa3sm9w31ozWv-nKsfukbBWEl-OgPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی به ازای هر مهمون پنج میلیون دادی به تالار چشمت به‌پسرخاله‌ت میوفته که با لباس بارسا اومده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22675" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22674">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUzOXVjYwUSUwI_yd1NOc1LB8AAPJzJQQOcp08B6KUwPypD2MCU9u6eLQUe8YD53dbJ72_D11gndY8BeKHTC8GXcYDWNp4nkLlUgpJQj63xFE6tlN6nSrS79OOxxpAZ5-wPeWCujRoA5Qcr7NUE45OPEFGAG2r__FXWN3xHQSjULukg2Z7qpNXgHcgyxXNkeaKN6ES4RdO39bkJeZ6d8gUk6NXA6qJIVjYi2OWhd33W1SvKjfo8PGw4jnsdCop5vBkiJBQ95D3Mb8yjq1yEGyxjpkftJZnpxua3GACCZk7sXTXyy5kDPo-UWUFWTu8KRq7bsIoTaa4t82t-3m57f1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیم‌جونگ‌اون رهبر کره‌شمالی تو یه‌حرکت کاملاً منطقی اعلام کرده طبق قانون جدید خودکشی کردن  ممنوعه و هر کس خوکشی کنه زنده بمونه خودمون اعدام میکنیم. هیییچ تعارفی هم با کسی نداریم:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22674" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22673">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktpWw-bpm8FLKYmk5xDFXK6qqfKLZVi4kiB6yFlusRljsln2oXNi4P_UlV37HgmRYGWeh72P9GlZ0r0-OjGSszYL-gsubFNxpyqyZcNUZuPy_svlwTLDjOHhEUiUMWjO21pYDnfAFEjeQbVJ7Ik1PHwOstQ-rSX7D1j7WaR2UUErkJ-lyOZaRoLqgJlvDlaSJBBs5cHp80gbBwfTp6qZh55ygPMAO2yEqd9jC3aI1HY_YdKtRDoR5XAzeF4BgiMVWrVM51IVcSeen-CVjzxbPpMgEHtjEtlonNd3Fns7iyJyCpHoBmHiaHhYM9zC3NaQwsvZVNU399LnwLosBUjaMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لیست ارزش تیم‌های حاضر در جام جهانی؛ فرانسه با ارزش ترین و اردن کم ارزش‌ترین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22673" target="_blank">📅 18:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22671">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5-bvv5qtkygjxPrLKOzhDjPG4CnOWNlnQnQ-SAu-mpUC7WWiRGlqkVvSdWYVAm9LakPMI4fMTAWbk5J66GivT4e9q0I6GIDqMrW7_w3PyqonEoswXy2NrR3V0Vx0GCRO-fCpzakYgWnaNmYHIqdQQkm64bKo8_E8wV9TjBQB0iApBB8AT8Hs5kAHqK6OP2pRtranBVIJ8vWQxsmZz-JzxBK7EarqDIcLqZQBrBNJ31ZoEl5Lni0KvqTGgCdh-lgVzXGLBFEzKmmv0BSaSOBy4dzOgiORzEO7GJdzdWCZGxjP24Nn8bAuB_0c9mMNWPHsk9WqHdA86GkoVswkNcJTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت: بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22671" target="_blank">📅 17:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22670">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZbkGaZcDhHWxtJlF24bkM1RZxo8r9hP9hVY2hE5MtueZ4b8RrGpGa-2PCHiIM6XWPXYdo4bXDuVzpAAoDrfbaChkVTesKoC3hDgFlv9IRTjr8golb0hl747HXqxWtNVfmtm7u30juapYxQFkcgdoLIoXIiFQY3rZmLCgfwxI3T3gU_jzTEfo-MY0Q5Qg8PtrHHkHod5ey1PlqdRU0HGOJG9cP-ezvRbZ5hnv0kI3UuyO-NSL1vDkwLQXBogEYHV7b0n8nBzb0GJ1zsfHpSXBKIbqGVFHvphQN3Lx09aYZGkbC6old1Zvu8Ea-NBpqBctzJ8KA4nEbjzmRMsndLruQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ روزنامه آاس: ژوزه مورینیو سرمربی جدید رئال مادرید موافقت‌خود را با پیوستن ابراهیم کوناته به جمع کهکشانی ها اعلام کرده و به احتمال فراوان بزودی این انتقال بزرگ رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22670" target="_blank">📅 17:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22669">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBata-lIfF830sQRk-DPcY3_-WXlnV_Hbk1IDCB87AjoB9EvjO1YhJXZsX2ox_p99U1SvsCzZsKid12MvyR8SHTKLyHgkAsmHkVs_0dO5vIWWVyRpfaqtUFJsOKG5chQjH0GlMYxutIxK5wlFCQirgi6RGKPiOtFM7ZJCOgYSr-u0oYeo_W_t5VzPl8mR7CSnAkSh6ml5z_sESG5gy2R6-y7fZvIkEYybkilsPVxPSg8fOsViJYGBM1v8Sf5RM_dZQBHs9IR4U0k8B_4DnBkNdHHHL8rnuxMNi_KhQakIiBcymC02XBGAUqIPvWvyUPbWC_QFnHQtSqnJGIDg5qlug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلام و احوالپرسی‌رسمی بین‌بچه‌های کره شمالی وتیم ملی ژاپن، در مراسم پیش از شروع بازی مرحله یک هشتم نهایی جام جهانی زیر ۱۷ سال.
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22669" target="_blank">📅 16:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22668">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoEwrVkHX-tYJN-vAgY4F_Zmkp2Iy_6inUISW48VjRTaJ9vWdPETE5vTkbk60TC3gzg8vRDKtsU9pDgqXHmAURb6uayli67On9dpd8m9K2kWQlVEaiy9mowMCJUWMr27jXN5tkhlPJZesPrsBj599WTi61Oh4AuJWfci5tKlx2G32JGZ1iCEguqNFF-NWEJX3yzHny4zndUag9-wOqLI-Ftsdq3z9tOSIWsR4dRv2LAibPLA_IelmQBWlqNmNUbGMKDLJsCZZmNq6utpis0TptSaao8aRqlauvQaIg_IAsCB74Rdjz9uZJJbfYkFMOS2u-sO3LKfl72uayst-Sdlog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22668" target="_blank">📅 16:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22667">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-G7gF_CwMO7wDAc6K0EYBkVBWDUItlWMP7iCGSbz6n2od_cM5f7z71Riv9iXetIS_iZqZkECO_fDWBtF2QHl94Gnlv16UURt_3AZuGiBmX8I5RmT64FFArnnJLY8T6JbB6FX3CpQZD0349D7MkDhLSMDcDBOQZXet0JjIs2ie2ZxXDaH8mma9-gvafWQlJUo_wx6c9aargqozI36h5yMg9RHOjJum41tf7fjXgrs3mfQGGJuQNn3EbTET9y6vpwnG2oUe-YSm4DfqBet6Igk0YlxZuuZavm4nTuphMJFl66MqzdtiQyTaz3fW3gHypjKRFGS-OBkx7IoYdzeHa6jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇲
دراقدامی‌عجیب؛ کادر فنی کامرون؛ وینسنت ابوباکار و آندره‌ اونانا دو بازیکن با تجربه کامرونی ها رو از لیست این تیم برای جام ملت‌های افریقا 2025 کنار گذاشت. ابوباکار و اونانا در این فصل در تیم‌های نفتچی و ترابزون اسپور عملکرد درخشانی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22667" target="_blank">📅 16:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22666">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLQQIA0aJQFeEUDlBe2CrODF2jc5xB6O4aqC2EtvNTjREavocI0bbllt7TXbwyNhZmulbIduVJOOt9zLcfGGRK1kTUzn9hQMB8P7ltNzQA5NUc2mUdGZKk5uBlHZB5kKFjPJJIXGNqWW9J9uVuWMS55gIz3HauJN0CJK-aqHkfqrxYJSwJVGRJ-IYIfESMFOipGlBc-tE58p3HGMFMSgYXzxqux433qoqo7WwnQibouvnxyhtFeQ1DoCwCdz2Zs1WhAV6pcmnCOcqeFeVR0dBCQxhQaqXJW7WWhKZNU6O9oZR-lzMrjvZp_gA5GC6Qvo0Ptlf92ypsypAdPG7OVljw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22666" target="_blank">📅 16:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22665">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_Y7gass-qsg-biUdc7NK3M_J-AtxfKKfpbcVrWuwpH9a7fFQ8NmdnQRsgeesjr_Zw_--5XTMyBGRVUzSN3pUIkz8vQT34Icnw2tX7hsJlWdSv-GFxDer7WOgy04Ml03QWMa2PfjX88CwMk7VweP12jzKk5wOagxgG3ZgX9llutWzIEX25OkJJBFvdnRXS4S3ZrD4wZ5WolRQqTJJ-b6BhJrnigWU8a5S93u8BDoLkc867x97OC7CZNr7yJa6Mr8xWLKbw2LMVqbr0np220J-QOuFFHa0Ch_fi4zHcR6clJbL6CvnZ5oNTNb5zm3-d8uqGbue_ha3oeblXZy5LVWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛
سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22665" target="_blank">📅 15:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22664">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mh4mhWgCyAeuxpnCtz9ar9JyiCHry4_OWrWTb5RB6W-OAhfM2m_YrfogiPakEAMJf1o7aM9p3cSxOu3C_rw35lyblGYojifVZbRPVmc20hDTBd_2ycvJCM6gFpj01fgK6gMNbV_s4Rz8YSAnzl8oREmgfBZBlt1bkMavsBvYwYqLUovDInz4vc5NyXvGaIZBNcnjet65tUhr4s8AEY0VHRqF0WSwZQaRy1Ro63a3Tl6zjSrL2z-Hglc5jDctmpFb2b3rJhkLDNorc81BMad8W-9g-mvUv3p7viz8kd5mCvewgjOBJ1Y52veORsz0tPLZ2SNkOXlvtkqQQ7ZdbGYVRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22664" target="_blank">📅 15:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22663">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXENGPsRKJnDBbE0u5-gRp3MT6731VQFbCGD3u8ki3YZxp2Mxt9diek1QnKrjYukfbYF2ppnZKPc096WIBl9cbXqBZoKeerdWKIayYoZhMLxA_s7yL7Kg8pu6TkDFuQJ_I9EDraaK_pfCNII7IyVD7qm2qOUs6hyBq2Q0VsnhoeCBq6hoZZtdNc8p1Lu0y29HpIsAgwNWQh7BCG6TxkByJyNygVmoZg8gdqCSzF_esQbo0PkVW2RxWEXXrC3jvpS1uUI1HhtMdmdyTjpttI_qK37NWUj3Cl7OOGoPfS_AeWJXgu3kjKCBz4eYXyXaTt_2I2wNU1oxmP-vCXC0RZjdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ باشگاه بارسلونا به‌ زودی با پرداخت رقمی بین 8 الی 15 میلیون‌یورو به الهلال عربستان؛ قرارداد ژائو کانسلو مدافع راست پرتغالی خود را از قرضی‌به‌قطعی تبدیل خواهد کرد و قراردادی جدید به مدت سه فصل با این بازیکن امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22663" target="_blank">📅 15:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22662">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJAa9P6EOvQ3bvQitnbxZuo5KQkjVq-8Aue_fzNa90fyEY89cZqBndvECuntzQH1M_DSIgMeZE3ZgWw6RwIZhdm-5ZHCARs49wjzQsYV86pLYUi3pUdoEHYvYvEkkMf1WJQmc8L80UMt77cUkkNwySvtTjC20C_wWxu34JIqDAWXl7vhf8ND4TxYmfcp_ik1QMKUvM8WiIhGm6t0ZcnfkFObYyyxjc2gNMLMwtbpSm5BRYlyxyEW1NR_OR_MIoOo5SYssOhdM9AkUIQ9Y4yMWgcLwUoHmcH3_aDT1Rs5utEMnQYS6UqBuwQkzA7mdDgnwwui8iFSzpVyyjGFqiVlEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا
#فوری
؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22662" target="_blank">📅 14:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22661">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ti2B9u3i4_NzipN_UXk7kPJBq_IH9dYaWMO9p0THla6fIfOBFvuM8R2eeNyrGNErHDq2Ieg1QhPeAvTBbg8_lVKU0ROinnb4vshtAClgNFGxp_7pAg4eMWDFrqwkcD4-yFSxokTykfc4_73m_vSy6ko6DHNyzsRJI_LCmo66Op480_STdbi31OfmdngruePz0jrAR-cdUZagf-52HbSQ6KLeFK4SSr0xJwkJihf9iGs69pQA4ThqQWerBuEKeApBfLm2Gl0I89cXc1ckpsvodCr-eHrNmsWPqXg4tLAt81BaCblqHNjXyepx6LPTI5PuK1wtdWD63_TlO1Vb5ufozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22661" target="_blank">📅 14:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22660">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=gxWqJ7wtdubs27r2fET3pDxlqajgVb2b889vI3k--9_fmv17dE5AAyWG803df65OOZQ2uSwCVZC0_Y5tWEm9dmNKaIeu876Vc2nWmxd2Ziq-JgAq3MR_ZeKeXn7zc15SaMofQUWPjY3IssmbrgZxn2evDbyQSE5dlqvXo9z5HXjpnKaAzhTXKFcb4o4-QYPpEiETrOCkencGv8FErjHGG7NNNbphi4ATkIbWdDkJW5rL5MypDDQwDNZV5wDrlvv2sO4HWALIkcGnqsp5SemCrxhJ-MmoYENI3JpiWg-I1AAJOy0Z_TruXPVy-b7NQNPCboi7E6h7JdSf7ibgXHINoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5314c21b9f.mp4?token=gxWqJ7wtdubs27r2fET3pDxlqajgVb2b889vI3k--9_fmv17dE5AAyWG803df65OOZQ2uSwCVZC0_Y5tWEm9dmNKaIeu876Vc2nWmxd2Ziq-JgAq3MR_ZeKeXn7zc15SaMofQUWPjY3IssmbrgZxn2evDbyQSE5dlqvXo9z5HXjpnKaAzhTXKFcb4o4-QYPpEiETrOCkencGv8FErjHGG7NNNbphi4ATkIbWdDkJW5rL5MypDDQwDNZV5wDrlvv2sO4HWALIkcGnqsp5SemCrxhJ-MmoYENI3JpiWg-I1AAJOy0Z_TruXPVy-b7NQNPCboi7E6h7JdSf7ibgXHINoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های ایرائولا بعد از پیوستن به لیورپول:
خوشحالم‌که اینجاهستم. به هوادارانمان قول میدهم در فصل جدید یک لیورپول جدید و جنگنده خواهند دید و از دیدن بازی‌هایمان‌بی‌نهایت‌لذت خواهند برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22660" target="_blank">📅 13:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22659">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBv77w6irxOLjhCxYGJzC1NxVMMTJ5F-1_gAikbL0ZbelMi10UJmC4JtjMPJkjf7BlEp25QLU_MJhcCNFtN9VPVfL_PaxlBNBOCDV4mLoZpWHeIuWHXx3WlkkXOLClClSdN7XZPohgjVR_aaSss1DzWK_AKT7PvW1EXhV0-e2Vgf-nlahxkYVi5fuAMUoUhMk9Ettym6YW-GPPl4oVs6LM_U9z3vmkhUV7Cfvw9HdGSW2lvX5nzTYfMNm9pFAzD8zUCqf7uJECdjHaLg521TllDtf7rQWEz5vzZ2TIqAyMwW0WH4VQ5vdmyP69t1Tp7BdDI1u32rwo6EXpgRpaYXyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی تاجرنیا مدیرعامل استقلال: برای فصل بعد هم یاسر آسانی درجمع.ما باقی خواهد ماند هم مونیر الحدادی؛ یک وکیل خوب ایتالیایی استخدام کرده‌ایم و قول داده که پنجره باشگاه رو بزودی باز کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22659" target="_blank">📅 12:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22658">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_r3FFeYyov7RHkZJFeTlEq2E3ny-L4Er3Y1-5aMX3VGzMUzklGaZoz0_HdYsekjWy5wSlSMrUmQqF6hnMoNnPhjJJMR8tUj5ay-x_ttRQPeoNuzDei2D6pG9TKkSQKqtpAouU4CMxDJjgcSCXPuoWyaNdjC_fwHdxHyVnqB9YB0YYb0tDP7t1CXpmjxqYHTEl6Babc-_k-RKRP_hleL9DJjRXc4s_2d4TUJS4u2hSqORGalHZsqZsN3l_ffitHe-NRtY6uIGqKhyQp3pjNQWF_Nw0aWOpMJoxhid3LG9eZIH8-2Ti-7Pc9Z3lgXLI2U2Ii68U6MITaTTmcuVDkLuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22658" target="_blank">📅 12:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22657">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=iBO6n6Zd1NDPaB0RDpTwMIAEpuH3bHYuzrq9afOgYxTeSmVPFucr88w5yDWTcyjIUcVPwVjqzoR0L-fL8sK9wYJQ8DOTmbhIqwtYTqthMFLj3D0oZgqrlVbnDVzxo7bmG12t25orQGOabJRJ1Rf4IwQVGeDGMyvR8tiLUnMM3PGWM6JceNQKffGY7w133OM_F0eq4PeifvzNjq7C1IELisTb7iaKfdWkOrec5U00I5riSiDYAodbI-UItO_qTb8Pcqp30XLotnZ_X392Oh63aW21VJmsRPwibRYD5Ui8Zny0SL12gfRLMue4GqjF2LDxrSXL-m6rci-liBXeIfCgsDUs799ONrHirrIiUtTNlrC4iFYW_hYlGh-wqv1Cs_Yuf5QIyd6RDY-BVmVaRjzj2J9VMzyiCZLQoPgamp71kolX1fFp_nc-XT4VF4YVPbsi2lVSUOFRlwvf6gYW51XOENhEjkU6EkbiviSY1TXmzuTDjr5A0LHSNpwlIsaRyApURT7cWB8tU6ulKieLzOJ5T4p85GHLoFNIQra3gHNah4v9lUq7udh1jVkteq-TV-G2XK7EZqQR6MRjaTmOTqoE0w_BdjmZyIJ6aY2-KgIkAhAf_wDrOsH21_3zu8kH1pWHnNJpbqvbJ-QyKTjnofIE7PaneQA3cTJQre3pdf7PSEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8d6fd380.mp4?token=iBO6n6Zd1NDPaB0RDpTwMIAEpuH3bHYuzrq9afOgYxTeSmVPFucr88w5yDWTcyjIUcVPwVjqzoR0L-fL8sK9wYJQ8DOTmbhIqwtYTqthMFLj3D0oZgqrlVbnDVzxo7bmG12t25orQGOabJRJ1Rf4IwQVGeDGMyvR8tiLUnMM3PGWM6JceNQKffGY7w133OM_F0eq4PeifvzNjq7C1IELisTb7iaKfdWkOrec5U00I5riSiDYAodbI-UItO_qTb8Pcqp30XLotnZ_X392Oh63aW21VJmsRPwibRYD5Ui8Zny0SL12gfRLMue4GqjF2LDxrSXL-m6rci-liBXeIfCgsDUs799ONrHirrIiUtTNlrC4iFYW_hYlGh-wqv1Cs_Yuf5QIyd6RDY-BVmVaRjzj2J9VMzyiCZLQoPgamp71kolX1fFp_nc-XT4VF4YVPbsi2lVSUOFRlwvf6gYW51XOENhEjkU6EkbiviSY1TXmzuTDjr5A0LHSNpwlIsaRyApURT7cWB8tU6ulKieLzOJ5T4p85GHLoFNIQra3gHNah4v9lUq7udh1jVkteq-TV-G2XK7EZqQR6MRjaTmOTqoE0w_BdjmZyIJ6aY2-KgIkAhAf_wDrOsH21_3zu8kH1pWHnNJpbqvbJ-QyKTjnofIE7PaneQA3cTJQre3pdf7PSEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام‌برندگان‌جایزه بهترین بازیکن فینال چمپیونز لیگ از2020مصدوم‌شدن؛ ویتینیا طلسمو میشکنه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22657" target="_blank">📅 12:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22656">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdaKYid03z3FlNV73_8uxWL6U1fhzzjf8WM7ZxsFMZCmSaM5nOqkzH5AO5yW2cLj6gdXUU_aeO91A8fwpQ8n-2vApFP3HTNnP4cM2FdLKOqc6Iv_Cmf4pq06SSS7mUwZA75DHlAKFLO2_8XgZ5xs-H6bh-eMO80o50CGdkco3x9ufWqAhYt3sUHEcGBuzr19d4gvyucmDfkEy8-3cX0ld73aEerA-gu0em99tIi7S22SmRd6cNcNjAN8VEZd-jgicFSq7gFGXG9bB5fPXaYVMyY-0H4TVOl9-9DNeSBPEHujBTyfyAL5H-eDf8m-iEr42hLMoz6rTQuADNuqf4LDFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
شبکه الچرینگیتو در خبری #فوری؛ ابراهیم کوناته مدافع 27 ساله فرانسوی سابق لییورپول برای عقد قرارداد 4 با باشگاه رئال مادرید با پرز به توافق کامل رسیده و بزودی قرارداد منعقد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22656" target="_blank">📅 11:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22655">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=UbGNpBdN7TJdWws7W3bmsUAzRBNCXO7SM_758eqQeDqBWEgaGfPhgfeUhWpP-Ka1-GIFwLZMOb0GI-Z4Vi6fnNogmOWNDxpb9fborafERAQiEt-5XCigwsPzyFw5KS-VBfVuNzuQrG7p8Cl0iUn2y9LycboqFZYG6Vb3y1-XZWk2gQrISsDcTZGUBVAUXgEf-4DkZ4kN348H2Ce66xS2X-B2b5JnM1Q4sbluZEIwwwyzd6eYjlMANA55vimxtVT7OnaQ9XrbdDdyaKlAQMzZ7QhkXs66Sa0F78oyiaZwYtIg81A8jxqIMmiAZ6euuUBJkXn5uC4kyV-ET6DQW9Fqx04-t2S0nxI5PdTwlmhhngVbp7YIVb7f9jNEZ5SFLZDv6oM0W5iO7JOD7ngEVL-AbacS6qJihCm9uZNFcy6USdvybRrKrGqSWcYW2t6J8WFcCOVMXeOrkYvmWn3zvZNOrOlJPbtfezQihlolTo90d2CgxmcmhYTfconAT2zUKA8b8ocrQeQcvHEYFNehu7328aAwXf0iIguAsePklQuQ4VK6vFCueIiDfAn0xs2rO4ThdagEYhxRcMfujRMVI_IVOWGMp_pk7b1JSmi2IHrUTBivn5KIoxqMcD93YrfpjmoWa2DNvGfOFbqTidcF62VeA4YAuBqO2vxlwC7vbxTPz58" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c58775c3a.mp4?token=UbGNpBdN7TJdWws7W3bmsUAzRBNCXO7SM_758eqQeDqBWEgaGfPhgfeUhWpP-Ka1-GIFwLZMOb0GI-Z4Vi6fnNogmOWNDxpb9fborafERAQiEt-5XCigwsPzyFw5KS-VBfVuNzuQrG7p8Cl0iUn2y9LycboqFZYG6Vb3y1-XZWk2gQrISsDcTZGUBVAUXgEf-4DkZ4kN348H2Ce66xS2X-B2b5JnM1Q4sbluZEIwwwyzd6eYjlMANA55vimxtVT7OnaQ9XrbdDdyaKlAQMzZ7QhkXs66Sa0F78oyiaZwYtIg81A8jxqIMmiAZ6euuUBJkXn5uC4kyV-ET6DQW9Fqx04-t2S0nxI5PdTwlmhhngVbp7YIVb7f9jNEZ5SFLZDv6oM0W5iO7JOD7ngEVL-AbacS6qJihCm9uZNFcy6USdvybRrKrGqSWcYW2t6J8WFcCOVMXeOrkYvmWn3zvZNOrOlJPbtfezQihlolTo90d2CgxmcmhYTfconAT2zUKA8b8ocrQeQcvHEYFNehu7328aAwXf0iIguAsePklQuQ4VK6vFCueIiDfAn0xs2rO4ThdagEYhxRcMfujRMVI_IVOWGMp_pk7b1JSmi2IHrUTBivn5KIoxqMcD93YrfpjmoWa2DNvGfOFbqTidcF62VeA4YAuBqO2vxlwC7vbxTPz58" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بزرگترین و خفن ترین کامبک در تاریخ فوتبال؛
بنظرتون عثمان امسال هم توپ‌طلا رو میگیره یا نه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22655" target="_blank">📅 11:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22653">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=ErKWssz5TQBp0BOkbj_UWiDsHaiRGj-Ws5qsNZuIMvFM_qsT230wunm8zdq5d25KEQ1ZhrsN0qqzFRitTEUDweLsTAubeN7lfGAwsNNCKyRDFwGOfq_Io5iM22ijSfVpwse5_Ukkvafh3wkODA2oS8P0PygQDWo2K9rrTOd9UauZ0JEoTN1l6H-a0d08XLt3pr6wMbanAAQzoJ20-EqcU2RBFMj0kWmn4DyeG6WZPH1fD6KRBqA7Ldkw3NM3JkqIH1jxD-g0o7XMuG_dHZBXhavCPFFtC75B0IoRTR2pXdCJQtaNXyuOU7HE3Uf6EScL5119PUvMfTQiYrimVyWKeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65ddfd9ec7.mp4?token=ErKWssz5TQBp0BOkbj_UWiDsHaiRGj-Ws5qsNZuIMvFM_qsT230wunm8zdq5d25KEQ1ZhrsN0qqzFRitTEUDweLsTAubeN7lfGAwsNNCKyRDFwGOfq_Io5iM22ijSfVpwse5_Ukkvafh3wkODA2oS8P0PygQDWo2K9rrTOd9UauZ0JEoTN1l6H-a0d08XLt3pr6wMbanAAQzoJ20-EqcU2RBFMj0kWmn4DyeG6WZPH1fD6KRBqA7Ldkw3NM3JkqIH1jxD-g0o7XMuG_dHZBXhavCPFFtC75B0IoRTR2pXdCJQtaNXyuOU7HE3Uf6EScL5119PUvMfTQiYrimVyWKeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22653" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22652">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkpuSeOpv7yCNU18UgTnp8r5d6EMCZC-sg1FpBLoH8GW93YcjT17Ppojb-qTy7hCJWGWz77SWH9lp0Tosl4wTeTDigsBqoqzdXoNIIFuCZYdQC0FLtJW0MU_4a8DvexvYtHGExNKeVnw1qLys0NCuBHcMkMPHtUJjAO2uPGPbB4ZtIYtRXvckPqw6yiAKcjYSgl9M1SPh-uamzqGk2zCS8fmCDsZ0rkokezniPbI3qf0b-Q4e-GGj-w9_8kqgaLpG_VOAZNBRizFXYjEsz9PTAvfMdqNVSPk-hbzyo83mAexPcdx2Jjp7opaLdBF8Biycg0S_RWND3TIWZ0A-p-Y1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
آرتتا سرمربی‌آرسنال درفصل‌آینده پرمیرلیگ تنها سرمربی‌ای خواهدبودکه‌قهرمان این رقابت شده. همه سرمربیان موفق از لیگ برتر انگلیس رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22652" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22650">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxIXppqFcCMB3AZZx8kNEZEgPB0aJDaow97VuZt3dpAEZ791vKoGVKBAHO52E6UkVAWpDUlqPfBzFWC-Xb8NOTFD8YR19xPYh2w6lvaD2XbqEFp4jOG25SdoA4MdlzNkBrjs8m_HvxR2MXPtLWWou_hGj0DhVw1mnd5iowCUQvHfW1fp6Yy-v-fd-gz3G8Og1LFYyRZAGon_xJBpLkOKCD3j4M-qBP7r6lxYvQdkemA3nZBr_DY8ENp3QM8h-8baB2rF_1WNdZHYMKtyw77byrtRYJVunUZQYv4qIeqV9AnEfHX_6bmdYvAz9UpHsGWwOcTZZERxZIaPIGsJoWxNMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ویدیویی‌ازسوپرسیوهای‌داوید دخیا در مستطیل سبز در آستانه تولد ۳۵ سالگی این گلر اسپانیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22650" target="_blank">📅 10:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22649">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-3DWtFYF8Sc5zbZI7v-pl_7kGYAOnaVyXHpYy1Zck_9lC2ToHiRO6r0NDFmDuvqqUWDltQ47KG3VE1_bou5-SVvL0kA-zjO0OG5lmZ-r-ptpij36mkQM6NuvsEV1O_iuSBMuK2q-6MqqI0-Ow28Z5E44tDhVNFXOvF15JNVEapwZyw7Q_FiuvSuUKq-1EfDbaBK56IKAbqR8hEDk_kwPMHkkmrq9r4vpHc4dzoaIZKeV7auWAHDe3il76KUTj1cC_iK1cmjBf1RhBgsYHkn7zg3P-FmTnCcEk2Z9pOXCzt0PW-GStFdFkHTLDUqSNBqS1a3hC1_dEk6EpZAEdqdjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادعای رسانه‌های آلمانی: هری کین یکی از سه گزینه‌اصلی‌ونهایی‌سران باشگاه بارسلونا برای جانشینی رابرت لواندوفسکی لهستانی در خط آتش آبی‌اناری‌ها برای فصل اینده رقابت‌هاست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22649" target="_blank">📅 10:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22648">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=IuvjCdJQ7cYi8pMy6NAEnncaGRDMS90UT-9Ux5EUIkjt-ZBoZ-s9lkbc9psOm6hdSMFc7HG_TDuUBML_tLo2viCSGqv-l7XZOC7OSeYWCaFw_RCBeQuZFgX9OJqn11WVjuno0yQsQHSZdy1xjDqceqdp8L4mLDfysNR6hB8SPcRtYSSZktzfzsWIrIIkAPORQ1sNu7nPK0t6OOaBqge9msGdb4LbnbmtMCQX9xon18EDKCKqpcwjvdNYfN-ljb90b_P0QXoyfv1YFK26daY7GH9WZX0lKLRh1lUjRAnFRTpniKKTa1w9MzVPnqLWu6oSvcLBXUFYBQLbcSvToZgpRAHqS4p7xnIQbxfAH-PrVswMJcrpmkrFx5oEhrXRc1KXNVirGPmLhF_X5HdabhIt9SRCe0l6f6cOlPtvMMbQVf_jbhEG5Ov4cuNxLZNhkeXTjUe8GlZ-y2mgepZj--kD-pnqtsp63aY_jzta52Qn8Si_CcxBQGbRgoiY7ISIr5gDfs8Yd2q9PwZPEqCU6JGdjYy1jMhvJZKcmpO12SnxLB9bFw4qf6K-CqG1XiQ9IEsMvIg2dEA1rx3RcOfYR5rS-hdXFa7CVZn8XqilniF3ahdf2oj3FcgrP3GVQ63tjv-eq9BCpUCVfTYifg81-HxWaosTxR2CZrszzZxCVAz5DHo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab78a2ef5.mp4?token=IuvjCdJQ7cYi8pMy6NAEnncaGRDMS90UT-9Ux5EUIkjt-ZBoZ-s9lkbc9psOm6hdSMFc7HG_TDuUBML_tLo2viCSGqv-l7XZOC7OSeYWCaFw_RCBeQuZFgX9OJqn11WVjuno0yQsQHSZdy1xjDqceqdp8L4mLDfysNR6hB8SPcRtYSSZktzfzsWIrIIkAPORQ1sNu7nPK0t6OOaBqge9msGdb4LbnbmtMCQX9xon18EDKCKqpcwjvdNYfN-ljb90b_P0QXoyfv1YFK26daY7GH9WZX0lKLRh1lUjRAnFRTpniKKTa1w9MzVPnqLWu6oSvcLBXUFYBQLbcSvToZgpRAHqS4p7xnIQbxfAH-PrVswMJcrpmkrFx5oEhrXRc1KXNVirGPmLhF_X5HdabhIt9SRCe0l6f6cOlPtvMMbQVf_jbhEG5Ov4cuNxLZNhkeXTjUe8GlZ-y2mgepZj--kD-pnqtsp63aY_jzta52Qn8Si_CcxBQGbRgoiY7ISIr5gDfs8Yd2q9PwZPEqCU6JGdjYy1jMhvJZKcmpO12SnxLB9bFw4qf6K-CqG1XiQ9IEsMvIg2dEA1rx3RcOfYR5rS-hdXFa7CVZn8XqilniF3ahdf2oj3FcgrP3GVQ63tjv-eq9BCpUCVfTYifg81-HxWaosTxR2CZrszzZxCVAz5DHo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزیکه لوئیز فیگو پرتغالی به ورزشگاه نیوکمپ برگشت اما این بار با پیراهن باشگاه رئال مادرید که هواداران بارسا به این شکل از او استقبال کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22648" target="_blank">📅 10:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22647">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFykStjusr5WgTAKEySkNMNW1tdGhCqgCbR61j_6wtNX5faJMfXHEf7QZ1ygOyBBwXK8SQutU24MmaOVr5FRIpQqbNJT06rqoCum8TA351sqYsZoMEl_jOdfQjFiTImx3GQ8ijqrdP7A6883FGp6TDJAqUsG8FI8sJMpPr5Q3-lzYGq9WNfnYjbbyqHdDOBDnLPMBopkpgQZ3prp9UQ89u6Z9INAoRswFroCs2b4Z2MIhf98PCMJdGcaHvSCZcMgan3GsL30l3gw5q_hrA4-vIXKSXEOfVZ3AOQx2SeKWGmQOoeIk39W3bBh4TW6E6QbEjPBFwbC5gDiEh1IODXf7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از پیرفلک تا شاه کرمی؛ اسامی لایسنس نشده‌ی بازیکنان تیم‌ملی ایران در آپدیت جام جهانی EAFC 26 با نام‌های جاویدهای کشور جایگزین شد. حرکت غیر قابل انتظاری که EA آن را انجام داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22647" target="_blank">📅 09:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22646">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njZ1stJTveq9DFZns0YcIaRfo1kd5KhdLk6Ri-FdBnKrCGwNY0oEsxdLQoOo9nJhWCQR9Qn2LrJNM29mhe6Fmhh1wcaiopu5AMWddsxhqoLs0Kw35-QpTxDzWK264Of2iaOy08E9HL2wFOLQaaWz1GAdjW1PJyxj1Hz3DJqnrtkflb8yuMM06faAate7PzXLu47XVY0Kd1RZNh9AOYw-vHb5KVehn28Dpdzgyuwo9qgwzxmRug72tb1pk2nscANtNGaVr3qG4Goj_A1GGRUOQc8SKWavIyqkgKnwqYVA-N4kqzxNJV4QCTUSaFaUIaL0VsbiSxK3xHJ3gjdIYGUw0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ابراهیم کوناته مدافع تیم ملی فرانسه که‌هم اکنون بازیکن آزاد هست اولویتش پیوستن به باشگاه رئال‌مادریده و درصورتیکه آفری‌از سران این باشگاه دریافت کنه سریعا پاسخ مثبت خواهد داد.  کوناته از پاری‌سن ژرمن و الاتحاد عربستان افر مالی بسیار سنگینی رو دریافت…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22646" target="_blank">📅 03:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22645">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1m63av56l8gXndZtBb7B9hYNFsAyuEt8LmJDmk_CHCd1T8iG0cGNXFS9sQDFUQDN1l7CQOwMOmCQWxxd7pDx2LgBPBzpY3KD9D2pgJ2XHxrHBhf5UwGmIRbqHYzE22PeEC-ARK4I8AAjuOrmP1FvXQycDtvSjlfoP4N3upBMIEq-orYTMecUhm35XJD5b5fMZGm_6NXRFRiw3UBx0tfTvdJQPoEdHRNH-HGw4iHypfxohRQuQmjbdBG2xvhGj12m3mQsBL7VVPh6IJQ_-3y1u5lY7JVdxTpVQOMwCKV4Pqzi2JzcOFwh8ZLWnMwLI6DJX3OnMyX16MQRIe7H7lOsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دیمارتزیو خبرنگار اسکای اسپورت:
بعد از جدایی دنی‌کارواخال؛ سران رئال‌مادرید بشدت دنبال جذب دنزل دامفریس مدافع‌راست تیم اینترمیلانن و میخوان تو همین پنجره این بازیکن رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22645" target="_blank">📅 03:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22643">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GSBAAbaWbehuwUTLW6gPeLgcGnhYIUmYdnH8yrFth_WGH1W_mYsqxE-M67YpXnqIhgq-xDJnqdEsT0mCgHfBbESCJVuQz00u7DI43ECHX3yRLiiejAxZ9QsXi1ChhCdf6gByk_r0ZWhrwsneI63l9WT_hF-hWVJ60L5uIXamTDf2ET40ladS7UheIMG04ck-uskJDtnPdZdbZ397MOkL9jfRdHB1pIupJ6WHsnP4m2MZ9zZMnoyhhHple1CJkqwPGYWyykNs4G9BJ3TVjJZExJqPfNjq1aiElHjaGR5v9fdwVqzm2CCCvsAKnOjYtl_THEDd_1Urg2DhPD5sodm6OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bfZd8CMdav0bdCjvpqicfaS9jNxZqxUXw5YR_r8aghDfdNgFOO72iZ740E594BISNSm_WGByisiR0DMmhBsyQw2Swh2OhhbcgHSzcqQS2yRjUfV1Tsg5dM9X__ZNS5S5XTEikfx2M7jBz_pv4oe3onYBmXidYXBjg05dgOMLh4BUgQ2rClfzHiuHk4QXwdZm15Jo5Ue3HwKd_1F-kF2S-l2vlUUi0ZAZ8C6Kh-nUYV0rvSCdMy60Zfnkc5HW77WSn6aTZbMhCae-FbStEx1znT6HmXQtgrnYSBIxg53Gh9Z4AschLglTyDJxptetME_ATdP-D6eD0SsUfvNlwNT0Pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🔵
تاییدشد؛ مدیربرنامه‌های فابیو آبرئو ستاره آنگولایی‌تیم‌بیجینگ‌گوان: در ژانویه مذاکراتی با یک باشگاه ایرانی‌انجام‌دادیم‌اما بسته شدن پنجره نقل و انتقالاتی این باشگاه مانع انجام شدن این انتقال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22643" target="_blank">📅 01:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22642">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=IKKL02OgXrQnA3gt2TUdxRwRNpbWNa58EYEv80sN1rvMs4mhM2GT7NeYXV7ovhLyNUmT6mPrPhQ9GhqUm1ewVT1gNtQF5le8W4W1fAtFfRcXL4CJVWD2a7xap_BDkyQgCnjyulh0HR_p1-5KUx8vS0h-JHaNJSV_ouGuAViqfj2Dq4ERdwaCod5lkg_PVL0-4HQVzFZpuoUjT8dyy_NvrHdXzLU4q9Kuu7GWbnTNPrgmn3u_CPcM5HYFhrXzJCoqQl3jn3U-1Ks7i0Qz5Dc0uRqXtp9Yrmj5ul6HtmyH_1jN1NuvVgGvrEwA0eXHtuWXAZ9-BMZAXgk0m76y6i3Cgmnp575q3tmAJQoTQCy1m_tGPxpRpdDJgW179y1OB7fPhljvm5wN-BP_L6aZHy4Rjk0Alta487cXN6u-ZGuhIoWY44W_LIyCYKYt5iuUOdNywthAINvuiW_s7bnHIB2sOwklQ2tz4GM1-eR-9czHMeK-LblOmEtoa2UDZWWTU2PqE887ZiYq_XrazixlyeRmiSnu67fHt9VqpMeT-u5blm51oGNPG87U4tRYx1mdPNLkC4iQOk0o4J105OpoeSPmvg1isgl0z5BktPLPOgdJijj841f9QZZyazSZi1tx8SdXA91SVbUfcdIJGMCXf533PCzt_adVa1KzvKmq8U4m1ss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/282d7b4a2e.mp4?token=IKKL02OgXrQnA3gt2TUdxRwRNpbWNa58EYEv80sN1rvMs4mhM2GT7NeYXV7ovhLyNUmT6mPrPhQ9GhqUm1ewVT1gNtQF5le8W4W1fAtFfRcXL4CJVWD2a7xap_BDkyQgCnjyulh0HR_p1-5KUx8vS0h-JHaNJSV_ouGuAViqfj2Dq4ERdwaCod5lkg_PVL0-4HQVzFZpuoUjT8dyy_NvrHdXzLU4q9Kuu7GWbnTNPrgmn3u_CPcM5HYFhrXzJCoqQl3jn3U-1Ks7i0Qz5Dc0uRqXtp9Yrmj5ul6HtmyH_1jN1NuvVgGvrEwA0eXHtuWXAZ9-BMZAXgk0m76y6i3Cgmnp575q3tmAJQoTQCy1m_tGPxpRpdDJgW179y1OB7fPhljvm5wN-BP_L6aZHy4Rjk0Alta487cXN6u-ZGuhIoWY44W_LIyCYKYt5iuUOdNywthAINvuiW_s7bnHIB2sOwklQ2tz4GM1-eR-9czHMeK-LblOmEtoa2UDZWWTU2PqE887ZiYq_XrazixlyeRmiSnu67fHt9VqpMeT-u5blm51oGNPG87U4tRYx1mdPNLkC4iQOk0o4J105OpoeSPmvg1isgl0z5BktPLPOgdJijj841f9QZZyazSZi1tx8SdXA91SVbUfcdIJGMCXf533PCzt_adVa1KzvKmq8U4m1ss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری
؛ درحالی باشگاه پرسپولیس در تلاش بود که رضایت دو باشگاه گل گهر و چادرملو رو برای رفتن به آسیا جلب کنه اما دقایقی قبل زارعی رئیس کمیته صدور مجوز حرفه‌ای خبر داد: تیم پرسپولیس قطعا نماینده ایران در فصل آینده آسیا نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22642" target="_blank">📅 01:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22641">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLq8TNgGHjhlMeGSBCWhTF009bDoz0INdQbc_1E09oRGf3cjj4gfDtetILL7ZqsfQg6n5fxhNLRut1L5KCuX59Z4__YCUlKldq44gf61gEKJkAq7t1RPv6AZT8QND7mvFRdtq2QCrVDao2esdQUADilSw9zvA3p0Bm61G2R3k6p_bN-eMdSieiSoyc9_rQuej1Ip7z-_ZXaaW2cTN-X0ArFfBfLrJxTWm8XL-p3I6aWpF-jLfCD5F7rfKA8lp9h2fUDjQfETicHTAKO6dYkz-lMXzCEt-HWDBBrFHS2dIBQR56vt6Ytv9YclKay2arT0TXzPuNAT2btgHaiPLxFOYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ آخرین خبری که درباره وضعیت پنجره نقل‌وانتقالات تابستونی باشگاه استقلال گرفتیم وکیل ایتالیایی به باشگاه گفته کارهای اداری رضایت منتظر محمد انجام بشه پنجره قطعا باز خواهد شد. هر خبر درستی از هر باشگاهی بگیریم میزاریم براتون حتما.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22641" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22640">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df595076a3.mp4?token=Pt-vBwnZ8XP6-b1da2UvBgO77ZypyKeGaA8-WsWE-0a8jlFrmBXdTeXNO04zg4DvJKrpa7ei8FhAG3ed_I0M8f552RH562icjPlIt1Eg8o_A4fRcqmD1Af-5q_kzEJStYKKi70VOfI-2ZDSljnAvbAzDrRzzUzebzm7OYJTSHLcuwEg7H-sQA5EoliGY2KlMmiNlAgmP0IIlGyKevhutvR0S-mbbGGTBY6_z0WYnfbff1YocLqj9BPrYNG2Cwm4MjI57s6ce9ziFL4XIWlsd-0QHX8YYJta3oaA5dK8YP54qIF3WvWkZM3XqFABn1PDVg-ScHgfkF69KP7Bj9IiUkB1GrN9wkt9p4lZQcFCm6DL318qn-0si7T7Ig5RMdiYTywdArABRA3b23ZPFgI2iZgu_zNLNTMVdMVWs-95Bmnj1axvGCnd4aCTQ46_cqsbgW_6jyvqgs0btViEcH9mp0-AkOX6fBSdStZH7LtpCzo1pCiiK-MpIII9QvFqjZUNQdcGrllM2qWm95_Dsz_PXvXUWuPxi74JxyQQ7EC1JC8KyHyNnuvy5JORE9YlKfcZRpZYXLFn2WAbIj2Xzl2O0ua4LyfnZwm335qW9H-ME_V5GMftfG1IuaYsPkbs63TMy049INwGkjkvfIEJTk5Go80KxyRR40r9JexbrQqPI1GM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df595076a3.mp4?token=Pt-vBwnZ8XP6-b1da2UvBgO77ZypyKeGaA8-WsWE-0a8jlFrmBXdTeXNO04zg4DvJKrpa7ei8FhAG3ed_I0M8f552RH562icjPlIt1Eg8o_A4fRcqmD1Af-5q_kzEJStYKKi70VOfI-2ZDSljnAvbAzDrRzzUzebzm7OYJTSHLcuwEg7H-sQA5EoliGY2KlMmiNlAgmP0IIlGyKevhutvR0S-mbbGGTBY6_z0WYnfbff1YocLqj9BPrYNG2Cwm4MjI57s6ce9ziFL4XIWlsd-0QHX8YYJta3oaA5dK8YP54qIF3WvWkZM3XqFABn1PDVg-ScHgfkF69KP7Bj9IiUkB1GrN9wkt9p4lZQcFCm6DL318qn-0si7T7Ig5RMdiYTywdArABRA3b23ZPFgI2iZgu_zNLNTMVdMVWs-95Bmnj1axvGCnd4aCTQ46_cqsbgW_6jyvqgs0btViEcH9mp0-AkOX6fBSdStZH7LtpCzo1pCiiK-MpIII9QvFqjZUNQdcGrllM2qWm95_Dsz_PXvXUWuPxi74JxyQQ7EC1JC8KyHyNnuvy5JORE9YlKfcZRpZYXLFn2WAbIj2Xzl2O0ua4LyfnZwm335qW9H-ME_V5GMftfG1IuaYsPkbs63TMy049INwGkjkvfIEJTk5Go80KxyRR40r9JexbrQqPI1GM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی درواز‌ه‌‌بان‌ ها حوصله‌شون سر میره؛
فقط ادرسون که‌گزارشگرم گفت بی‌دلیل نیست پپ کچله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22640" target="_blank">📅 01:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22637">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unSG7CZ8eIMXNOro4Iz6MDTi-PxFK1T53FgVENTLADj6lVgyiH_j2xU8QzYaTyapodKNmYxOLqGQuy4jC_BepIbxRFTqiXssKqERF67vkzXM4bNcPGkZvW6TBq3Sfq9IJtZJlOUEgUK7xArWA4db4COSHl0UjEleRm4OwU0Wp1ulPIsIRKGMEyfgzPJ4nCzvXL0FGRdAccoYK1Z4_RxhFezCrmC1lVQT8xH_mJEYyj2sm6uGzO1ujcaLpn5_f8Zko3LL5NTlfWmAVI-VUH4u9VcF7zsFytvlc2BztyEenpP7WTxxbziw7zxl82blmrCG4wXUYlnhd5-ZVGu2xBY5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ مهم ترین دیدار های‌ امروز؛
نبرد دوستانه دوتیم کرواسی و بلژیک برای آمادگی در جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22637" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22636">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElwKkV08okGVftIkeqPdaHOtLJTm2ryrtG27ZT6xRbZfpEMWW5Au4y9uPkktE2h2udPfNtUOy5onXEi7j4KL3E3DxqJY2NXJClmaeRgj2NZ9oy3TgsRyMzgPsf_r92trrNsuAZc7j9Jajo_qWI_aKtfyDQ_BS3TB41jORKkjWjM338G7EXPco6vBh6TnsyyrienOI2XtVvMBIngwpq8Hhq3A6870uHwykH6gE-O71aDGOnrROOCOczasj1m0zfMV3zTJhLCS4peMQ18Wiy1QiF9axoxMUp6UahPp1mqVvzkaTr772URHuluh2VK_vLHFNYUMcDT5JtdMEQ8CSqf8tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد پرگل و مهم سلسائو تا برتری وایکینگ‌ها در غیاب اودگارد و ارلینگ هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22636" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22635">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31b893cce4.mp4?token=NMCoQJXDLnbWqyyS38EHTa-SgFIxUWVnJrQFSv7YvA-_GLTdoMkXK-4Ef24_cUhmw7KKxtgHeMtHzV37hOwbmeKFYsoUvfOA659JlXQyBMIMWfvHttfo92NKea0iTzGnnVbTxCcf03TuyB5X9VC7NEy_srHIn9y8lcwaVfs3DTsiySwU7iHpbelBM2Xsx7ynnh_-ykRutwNs8odK6rirR0w_rrV97lVzr5mkk2yp51oJzvn4w-3SDyR2JL5IW7MVKbd0MTKnkhVlF-yePTthSjXdrMBnwjQfy-GIlaoKbsgBrhOIz2ayf99Jhh3N80nhriKjCjrY6b2cd8e3mJiTKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31b893cce4.mp4?token=NMCoQJXDLnbWqyyS38EHTa-SgFIxUWVnJrQFSv7YvA-_GLTdoMkXK-4Ef24_cUhmw7KKxtgHeMtHzV37hOwbmeKFYsoUvfOA659JlXQyBMIMWfvHttfo92NKea0iTzGnnVbTxCcf03TuyB5X9VC7NEy_srHIn9y8lcwaVfs3DTsiySwU7iHpbelBM2Xsx7ynnh_-ykRutwNs8odK6rirR0w_rrV97lVzr5mkk2yp51oJzvn4w-3SDyR2JL5IW7MVKbd0MTKnkhVlF-yePTthSjXdrMBnwjQfy-GIlaoKbsgBrhOIz2ayf99Jhh3N80nhriKjCjrY6b2cd8e3mJiTKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دربازی‌ایسلند و ژاپن قانون‌جدید ۱۰ ثانیه تعویض اجراشد و بازیکن‌ایسلندبیشتر از ده ثانیه صبر کرد تا از زمین بازی‌خارج‌شودوطبق قانون داور اجازه ورود بازیکن تعویضی رانداد. به این ترتیب ایسلند بیش از یک‌دقیقه تازمان وقفه بازی ده نفره بازی کرد و ژاپن درهمان زمان گل پیروزی را به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22635" target="_blank">📅 00:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22634">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqODGvektpJAA4OUe0yAabVjt3hf7OCgpO4jMcvjnVW2hUk_0dgXT8j73XpRbloJ2zCupCfOfrdUZRZ8BOfJ2tHPnHGwm3GgETR2PTB1uoxTK8tMcPrqpp0K-xkqX_r1hanhV-unEMIQjm1AgOH6iF6l26I_kuGiv9O44zmpa0Ut6ga6W6CTxzSKSlhKe3ZWo-kKPLSJ1E_2NFCAfx_9gEj7-IoBCffvYgpFL3EcvZFW1SuY7dGt_34fFX7FEoF4BSAcgsTpE_O-6Oagl7MnIwDau-onxYAIo9uXxqSS1sEN8JHrGzkuzAg5xlElu9jnMnZHWe1IbdIe1858ZWb2bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22634" target="_blank">📅 00:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22632">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWh2_dwSUF2EEbuiTlGKPHbknun7hjasXQU1fTw6USEHlMyKsxzcnuC2kLtnGOrlzE8m8dHI7jLqE7QbdjSM1NKJ8JZf4AUbTYGbRlF2wF2KIfCiM2qmjq8zVwHar8MOB0j6DrNv52cvmS0j8HJbfc3BYvx577LY4nupi7A3s4BS8bp99IhTxWeVj6vkIIrxho45VxjwdLGHCU_1mH-kUwksjPqHzOhLbHslv5F2gMh-gGphTS0GLyB7DdXGfofF6AnkGJB1OV7IW_pqjMIvPQFwt1wHfyvj1Cv9ngpViTPoyDFNxgL5a7A3imAl6Gjs1uA7Muqz37fflljDXSi3LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=WyzH2BKyqMplC6VEx74E71EaDCW-_gizPBqRBXU30uZTBiJfB5_Mify5DnCsC7-nHfeaWe_SCR7OgvoCsEVMSTAu8LQ56bsLERFk8daO6nhSczaGVYMMChX_3hnX6Ml2TTulM-T49AKrcIhkCATpP88ZhgzQoQgJ_h0JwALLORKe4L3ku0-7d6YflSz2Rdg9tlseUDaLtqZuUTOj0TmgCzt4KNoHc0zVikPXjbBvNkILR6GziTUL7MJ8gCGqeUtZmkEvm3KDq5SU7b0ja5pcqg1SvkiRWElPBIESQK7BJEMok9fWQnaM-bMKYmgSIG7k8aUfhSeJYZM4J7ep01_tkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d165d6a89.mp4?token=WyzH2BKyqMplC6VEx74E71EaDCW-_gizPBqRBXU30uZTBiJfB5_Mify5DnCsC7-nHfeaWe_SCR7OgvoCsEVMSTAu8LQ56bsLERFk8daO6nhSczaGVYMMChX_3hnX6Ml2TTulM-T49AKrcIhkCATpP88ZhgzQoQgJ_h0JwALLORKe4L3ku0-7d6YflSz2Rdg9tlseUDaLtqZuUTOj0TmgCzt4KNoHc0zVikPXjbBvNkILR6GziTUL7MJ8gCGqeUtZmkEvm3KDq5SU7b0ja5pcqg1SvkiRWElPBIESQK7BJEMok9fWQnaM-bMKYmgSIG7k8aUfhSeJYZM4J7ep01_tkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اول‌برام‌سوال شد که چرا بازیکنان پاریس همسر مکرون رو اینجوری نگاه میکنند، گفتم حتما خیلی خوشگله و رفتم گوگل عکسشو واستون بذارم که با این رو به رو شدم
🥸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22632" target="_blank">📅 23:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22631">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsfvtYyXRGzkwz0usRpC5D3kzb685Srs7PTPmu4Xuym0DkbhWm-OQTNr3IrDmyu7114W6L0eMRwspiX9OI96HwfxLkQ0rWfpKeHuq90B3yjyQTSsmAAd6iAd5ilfBVVaDq3Nrsy7m12_3OsErUjQFbagzF0u5GGuJy-eZy3s6dG9OFx_R4wd5vDOyzxHSH1EtR3_zO4LiV7G570K9vg9R7pRTtXSmvfT3qT1rF3cewIt9XBVOLWhZ3VUEIkc-0JdeAXdkjols604cJWoRToci1vIi3WpfLIYaz1TwuerxT57Cr8z3OEWs48WIDn4HZLEcvCpiCsGUjhIdzLT8UkYyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇦
#تکمیلی؛رسانه‌های‌عربستانی: باشگاه الاتحاد عربستان اگه بخواد سرجیو کونسیسائو رو اخراج کنه باید 25 میلیون یورو غرامت به او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22631" target="_blank">📅 22:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22630">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYSp0E6PvHQfmLDG29KfTjCoTSoVJcYzoxiSFfEOm59BIrXnPKEWS_qqn5gmMMcckftlNwGAs7VIreIAsbaaUOCIPrVJC5tZJi5REIMbe79xx6p9zSpYkbyvy_xNaf7NiN7_PHKfumH6B1bdgYQKkaKgzpuGYbAAqD01t2ERHiw1lH8KTw5k1rd0SU_dAiuNCU8SkDdD8ywGXtZ85jDnYRgBdrcYw0kIS_c5hjs7w591rN6FgR5gYzxbWpwzlRIzhOT1JAkjFARhjN3vwlOLjl8kN9at_pt9YbGdlKe43Dg0ELUVgfrciNMkAkGwokV0eupgEEqbcLNX3idQ4WfbFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22630" target="_blank">📅 22:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22629">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=GF0jIgeRI6YEgYq0QysO4g7o5kCSNbGzqCR3r5DRbS3pXlwqj2qQD3A3zyN_-eYne5kxbgzm89B6AYnxW5zYrgruCwtj-W77flMXjD7PQMZHA1PA1VFxKXyurQCTGje_JY4FQjOReSpbKlW-0oZAi_-8isPMzZ9UlobC8D6tdb1mn7xKEuy8RJbVPWuDgZ5yehT6uO_NLI7TOm2Rmr-3epoxc_7r4xWub-t9eJ_O_HhxueKBvhMPyrLa3ptteoBZY9mld4FDstYXIjRJzeVQYkeT0Bj26l39cWLAlWDklu_JpmavDB6u15fAEdPlkjtdrDHyVavK2seuBZe1autwXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4344a08e8.mp4?token=GF0jIgeRI6YEgYq0QysO4g7o5kCSNbGzqCR3r5DRbS3pXlwqj2qQD3A3zyN_-eYne5kxbgzm89B6AYnxW5zYrgruCwtj-W77flMXjD7PQMZHA1PA1VFxKXyurQCTGje_JY4FQjOReSpbKlW-0oZAi_-8isPMzZ9UlobC8D6tdb1mn7xKEuy8RJbVPWuDgZ5yehT6uO_NLI7TOm2Rmr-3epoxc_7r4xWub-t9eJ_O_HhxueKBvhMPyrLa3ptteoBZY9mld4FDstYXIjRJzeVQYkeT0Bj26l39cWLAlWDklu_JpmavDB6u15fAEdPlkjtdrDHyVavK2seuBZe1autwXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
پرس‌ سنگین برزیلِ کارلتو در بازی با پاناما؛ حتی وینی هم داره زیر نظر کارلتو وظیفه‌شو انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22629" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22628">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=IySHWsJDJz0-keBNP-Yt0SIPp-e5FQyQLYcAm8tfSTpYGqVXnJlqZfc38FCcxFJIhryaKzGNxkyypC4OBDvgTh6BHFvZd8m8Z9fM-Ar6hUmtlfJwOSqAtG8D-d_xb6Yi7Q_HGj9-E6IjNPwkqk8JNnC8HsM_LjzJ_mDXITdfZsSbf0pGRRTrOKfxM7jLfP0L-H0Gsw00SuWCEPDy70wLsH1IA7DoTvP6tOgHNAMhrTp_zSip8m85QkxxO-Wj-PeyC6DJ0Ossb-bQxtgX7uzu6NA4AhgZ3JZG4gUpbz_rnQjoXeBP_-olnH8br4e-7Q8LFp_YEOhOQMLlS__XyDM34Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca84e9f76.mp4?token=IySHWsJDJz0-keBNP-Yt0SIPp-e5FQyQLYcAm8tfSTpYGqVXnJlqZfc38FCcxFJIhryaKzGNxkyypC4OBDvgTh6BHFvZd8m8Z9fM-Ar6hUmtlfJwOSqAtG8D-d_xb6Yi7Q_HGj9-E6IjNPwkqk8JNnC8HsM_LjzJ_mDXITdfZsSbf0pGRRTrOKfxM7jLfP0L-H0Gsw00SuWCEPDy70wLsH1IA7DoTvP6tOgHNAMhrTp_zSip8m85QkxxO-Wj-PeyC6DJ0Ossb-bQxtgX7uzu6NA4AhgZ3JZG4gUpbz_rnQjoXeBP_-olnH8br4e-7Q8LFp_YEOhOQMLlS__XyDM34Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هواداران خودِ بارسا از خریدهای خفن لاپورتا تو این پنجره‌بعدازمدت‌ها تعجب کردند. لاپورتا به فلیک قول داده 6 بازیکن تو این پنجره براش جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22628" target="_blank">📅 22:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22625">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o7yww0AeqZX1KU_QYx8Q-0c5E9MJxBxp9RcmIOWlTkO43RtJCVq9iw_GTPYupHnTupZE_lvy706ksccFRRjFooNxejRl5-TCalkICOS7zFrDayeenu_5J0ihrdLUT1fFzwtqu1tTmWB2t0Gj0Lv3jMNcfjCO5WwwSJv42J32yYlfuyk2dQhysMzROaISQ3JiUL47zCx27H7rujjfaVnYneLjia_IqpNaQ4_jnm6Wt52B1gR9ZYx9C1w2U9o-3EXf7WS9xlqUDrm_6IEfGjToWstzv9N03mMkdNl9CvcfCvP9vZnWwFpOaVGsTQ3JwZP3FowIWuAmvfJfMY5Cm5MJ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EqfOXK_tMf5B3TD1kouQs4YpNRBmRv73IFeU_zhhzDnRWNx3-DuDlD1pm3aQO_tcnLS2ezl0imRA3P2i9phbGUqbZOQ6DW7QVQgjwoDoMm0Q5KjmTJfqtZIhtLJaJm3ktDYMvEodK7Sq8GumUNzrwgKwZMyG-OTeZggH2cqywIBdDDaKMSauXGHD64_Q2k83CFrZcI8jJEIuEj_vEr4noUI6Ub5xmYrTK_kvflpOKV2Q1wop0FTBlC9_CG_gAkTZ6XLJsQRbUuYgPaYREHKmj1BotweBIht_Z2WHCYfBO9_gFLFuZYUUGdVJRaH4lSI7BXWoBypJyg1ryy9hZkAl3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22625" target="_blank">📅 21:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22624">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=IrWB2_ICMz5-Ho9ZeHEfT1n2BEV5U1eAYZlrfxXVtm_XKxTnxEyWiqRwPf3dVU8IawWwe5YIbEhKadmR7AHSYCU8C-m-OTWs1WioNsAgcTLCH7tTrn1wvoZrF0jclCSm05jx15Tm-Nrkd6qUD-Wlb3rdebzC2Dd865HwQJkVn35_zla540sG5W9xu4lxujc429wbqZTQ91a35rdG_pmvjFgK5YnNhLoXZCVZR7QOhXP9aKDFHCmGaV4hW1ytkwFCRl1dbGVtH90YqIt3nNQgHIg626EcVYiwHWWDfBnsmE_U1SrIOzWGUli4tWGwr9D3em4VWuYUoUuoPymuHX-Veg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bceaf8ef4.mp4?token=IrWB2_ICMz5-Ho9ZeHEfT1n2BEV5U1eAYZlrfxXVtm_XKxTnxEyWiqRwPf3dVU8IawWwe5YIbEhKadmR7AHSYCU8C-m-OTWs1WioNsAgcTLCH7tTrn1wvoZrF0jclCSm05jx15Tm-Nrkd6qUD-Wlb3rdebzC2Dd865HwQJkVn35_zla540sG5W9xu4lxujc429wbqZTQ91a35rdG_pmvjFgK5YnNhLoXZCVZR7QOhXP9aKDFHCmGaV4hW1ytkwFCRl1dbGVtH90YqIt3nNQgHIg626EcVYiwHWWDfBnsmE_U1SrIOzWGUli4tWGwr9D3em4VWuYUoUuoPymuHX-Veg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
همسر ایرانی سرمربی‌سابق سپاهان خواننده شد؛ همسر ایرانی خوزه مورایس که یه مدت با تیم بانوان سپاهان قرارداد بست با انتشار این ویدیو اعلام کرد بزودی اهنگ جدیدش منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22624" target="_blank">📅 21:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22623">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c62242613a.mp4?token=tg0OU_alvuVAxtNawoufo1CF0mNDihfieWBk4TOSouM_EoMOms380p-D2m_lUH5wvbdZqF1Gt33cIAk_fdzCgflOHOqDO2mcN3rJg5ZPddn5piM6XoDK8dHXmMpVrziiqDhXaGYCybTx76hpU7K9jINGOg2dYjB8dHC9_irSJC1HyrdmBJw3I4AvBkvBnA13ixXDzTDiCWoE6Ed2uAYcebQdJM3jgd1lGsvAWPDoTDDoeOW4JBJ8CVd9RNqwVwuTcAXdG3B-6r0ZwBdpuK3dOWnY8HDv8QD0jHEQnQzJGgTdGWw97fvyb48kPYL3pcEztOIiw1Sahwoh3wvlfh_N1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c62242613a.mp4?token=tg0OU_alvuVAxtNawoufo1CF0mNDihfieWBk4TOSouM_EoMOms380p-D2m_lUH5wvbdZqF1Gt33cIAk_fdzCgflOHOqDO2mcN3rJg5ZPddn5piM6XoDK8dHXmMpVrziiqDhXaGYCybTx76hpU7K9jINGOg2dYjB8dHC9_irSJC1HyrdmBJw3I4AvBkvBnA13ixXDzTDiCWoE6Ed2uAYcebQdJM3jgd1lGsvAWPDoTDDoeOW4JBJ8CVd9RNqwVwuTcAXdG3B-6r0ZwBdpuK3dOWnY8HDv8QD0jHEQnQzJGgTdGWw97fvyb48kPYL3pcEztOIiw1Sahwoh3wvlfh_N1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
بازم‌ این‌یارو با هوش مصنوعی‌ش اومد و اینبار فینال چمپیونزلیگ رو برای آرسنالیا اصلاح کرد. اونایی که روی قهرمانی آرسنالیا شرط سنگین بسته بودند دقیقا یه همچین حسی به این بازی داشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22623" target="_blank">📅 21:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22622">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crDQYaxSUUgrB4vfXm-M1pECIV4tzXn-kBzOa2YmyOGENalluLfMGjFFE02e8rwJr8gE5jns7FO_PMdeYk4Xrv_oqtK7aPcvh4VJ2OBM-TPNiYnbpjQww7aGppFeXssIForMV1yry8Kf5ke3efXOB5PoDd6vEg4MHyzK-2WjeHygDNXDJWz4Co4XL2Fm3gNMQ23xgI2xHaq_wTeBh33kOTHOpETSd4Tyi7eaKa5qsOSKS1gszyv0aQqrMVnTym1pO2Ep9MlEaWPXUzBdZ4vCjVAAWnITtBGZF4iwYaaMjaJyJSwySm_WQymdmtF-T0L5jj_yE9i0PObdWXmdAMyH1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
طبق اخبار دریافتی پرشیانا؛ چهار باشگاه فولاد، استقلال،ملوان و خیبر باارسال‌نامه‌ای‌به سازمان لیگ خواستار برگزاری رقابت‌های جام حذفی بعد از اتمام جام‌جهانی‌بصورت‌فشرده در دو هفته اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22622" target="_blank">📅 21:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22621">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfUHhjBwezvdPQ26MyyHAjpU1ahMULegf2zFCD34G_tBx-7Yo-bvrQhb8kdu3IhANYRlg1ZqlqqieM2MCqCLXZ1V2I366iQWdSo0faCky-5h5hqcKOF2qI1HmZrnYHaK8b03Td3XAZWH2ZZusVklLSPFu80FbvyG1u29MqsxnNl7OUtMAN_456fC6NCFVbW8YPBfj_kFk86wyBIZvIrXMGtUM2gOzuf3hO3c2LWVpe-k_givSGmpIMjQnoaO-iS6AwDBijdVPl0v8o1SHvRjpZMMIzoBG3DXTR_GU7KaCftRgxlQc9VclY8v5MnKQ0uqW1snuTwostKAPfxLt0-Nyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩵
‏پاول دروف مالک‌تلگرام: حکومت ایران تلگرام رو به بدترین‌شکل‌فیلترکرده صد تا پیام رسان ساخته ولی ایرانیان هنوز دارن از تلگرام استفاده میکنن و محبوب ترین پیام رسان بینشون تلگرامه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22621" target="_blank">📅 20:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22620">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrHG9J9JYQ8akQ6iZ5wT3ndQzqpFmIokImC19DTAk3vuicARTvh6Mww5mJ8gyxxryKUK5w4mWncgBqeraXGpFWfVpaybzvp9oPIc8M6O38Szeb2SFTg0k8_qAD_y8BEp5Q4q3rHJFpnYddGxWqixP1RiHUvFQvrkoBpMd-PtzO-QYNZxwU79iekgEi9bMyereaSTFqLvpK7soUG3w3jW9FbDo4hk22oTf7uDWMKI-GKmybvyrOQ7jIwnQP6xA-_UfUHQheBvKRz-1x9Ur1L51JG9NB5vtAWHnO-oOsqXOyQOT_f_1XC0I7FVmvh-i3kOAfb--vgQCR-NXKjIONOZIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ با اعلام خبرنگاران نزدیک به لاپورتا رئیس باشگاه‌بارسلونا؛ خولیان آلوارز ستاره آرژانتینی ظرف 48 ساعت آینده قرار داد 5 ساله خود را با آبی اناری ها امضا خواهد کرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22620" target="_blank">📅 20:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22619">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdjRQ1k3qkI0uP8Omrc54bxBV3h7EUFlcFIRV2NME0vAx9LqXrRHKC9Cewj9fTRnehQlfBTyp7LJRQJnQXi4ceTSgofiS0wb4BODKoSbqOmnE2_Tr1Qj3HAOiTUdJA7rFw14WlyO-5B7DLTgwzsP-yVsiS7cUs0pylqvC-BJ-GGj1FAnFb4QtIs7Z0XX7krbzdu0IEdGeAG1WQJs5DT9ZERJYm2Apg_MdD2sRjv62r5j2fZ4bZfgl1w5wDx9NwHR2d3B4KrlNSye9ewNrmBi1W7voZxjLwdsgyJMaT1bvE7l_fIps_cClbJCmO7c83x55ZSM1ciQ6N-BUWsjOtmPrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22619" target="_blank">📅 19:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22618">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1UIQPJq2Gr7eSWFNbc4gRY4KENtocx9nTD45fFPE2bSaFEmglkV_a8VP9nzrhj2o1uXnGnLytzgFJrj8iec_j_ozZuCM5nsPabGIvC8zZgbU4l5VHaPmyIkv8aPtpoTmtqzJo2TQUrKGF_gNYaSUl98s-gvxwnWRhX_53qei7R0pClTE1w-YAvm68JaopdiWcB2wdnq5SIYHd74IuvZdIyy89HxkTL3FSLMTiDAlM-aiYw9Rd_ESrHCV0xUj4E1E7pBW2TTHPWk0ZpWIQ9AG8_eCac_XjqGvkLeZAY9IUMgGCCBQxeDSWDD6eUfiTlbFO8HVVmBUEheDc1d66hlyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#نقل‌وانتقالات|مدیریت باشگاه پاری‌سن ژرمن آمادگی خود را برای تمدید قرارداد دائم العمر لوئیز انریکه سرمربی این تیم اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22618" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22617">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514074c458.mp4?token=IOTU9Q6zgisj1osjXUNsztPJ_72QeWP0SSjMrGcNOg5n5RemuRQ2Gv7tFlveMj_ZZgPGoX6mOEIGlykjM7xrkAR0AOPXpvDHM-h_5O68eFzmgVwJtn8sAaQvqEUbhq6H6UL7SqmqgmohezOs8Dd-fC4RYNZrT3Sw2XiqEhvuaccza8hX7PBOLXzYwJE6p5ip7yAV4VF8-sjZO5vII_xk54q1Gpaf30X0ATo8VrsRpgwjx4o4tbDdgfIyYn-0PHrjUuctspZ0nFFFkuPzpAG9kR4ePqm0tjI7Y10Mt96uOzOy0oLB7SOmxcsxUYlnoadZPoMKdzfGEYu_7zW9b2azhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514074c458.mp4?token=IOTU9Q6zgisj1osjXUNsztPJ_72QeWP0SSjMrGcNOg5n5RemuRQ2Gv7tFlveMj_ZZgPGoX6mOEIGlykjM7xrkAR0AOPXpvDHM-h_5O68eFzmgVwJtn8sAaQvqEUbhq6H6UL7SqmqgmohezOs8Dd-fC4RYNZrT3Sw2XiqEhvuaccza8hX7PBOLXzYwJE6p5ip7yAV4VF8-sjZO5vII_xk54q1Gpaf30X0ATo8VrsRpgwjx4o4tbDdgfIyYn-0PHrjUuctspZ0nFFFkuPzpAG9kR4ePqm0tjI7Y10Mt96uOzOy0oLB7SOmxcsxUYlnoadZPoMKdzfGEYu_7zW9b2azhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
5 گل از بهترین گل‌های فینال لیگ قهرمانان اروپا به انتخاب پیج رسمی این رقابت‌ها؛ نظرتون کدومه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22617" target="_blank">📅 19:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22615">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZG-1S7In0a9GeGtWG4BVyWwLCK364I4ZIHvJXK7LdkZhP8k411yss24Tf_k60Yb14gwihR64L1uyCnHPdGdNlCLoLwTUEN6fcT_ExKXXtOzyB3frImMScXhfezPBppnOw_XaWzM_j0tRofR5kERZGB-Ix7ZBnsJcY2cWcMwsvZJJt-tyCkD5LkWO0kYzYBzGKYD3a3neFUhc89liMkECj0YgWUtVj-DHsj81QnD7BWXvS982spVdux8Q_Zuxm8BjOt4efB2G5fCuUZfhZZ5sQ3z4afYk4LPTayzTRKmFUF5ZFVrvs513q7o1UDeG7ZfEe9dpu0nuTzPTHHf9-SeIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدمهدی رحمتی سرمربی شمس آذر: من با باشگاه شمس آذر قرارداد دارم و همچنان روی حرفم هستم که فعلا در حد و قواره سرمربی استقلال نیستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22615" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22614">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=CbNo3auYymQNOGufmQS6JH5EP09mypWsVLq_aQTkEnsGn1vM6_c7lh9fGhbKjiC89UxGrU2Upb6tArl5AD3DMkKMlmPuBQAzmFt_aBoj_Ad0n7_ErS1W9o2K6YYlNra9nTqVIUcvAhf4yVzvXq15LHnEp7gMYzJEUR_VsRlyuOwiLhCPcOdPB4qMWhFYhJWylmWFI8ee3XqzZAretE5MiKVoZjdmYrQsrf40xBRn3njV8zuonl53xltRut449uCm493ySR8ATRt4Xdlcg1QQJd0sInZAK2BkMU1JaFsynfdbcGtTdypYCDe8R98uCXpLot8pJ_SpfVGEbW_aOUa9Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d191ac7bce.mp4?token=CbNo3auYymQNOGufmQS6JH5EP09mypWsVLq_aQTkEnsGn1vM6_c7lh9fGhbKjiC89UxGrU2Upb6tArl5AD3DMkKMlmPuBQAzmFt_aBoj_Ad0n7_ErS1W9o2K6YYlNra9nTqVIUcvAhf4yVzvXq15LHnEp7gMYzJEUR_VsRlyuOwiLhCPcOdPB4qMWhFYhJWylmWFI8ee3XqzZAretE5MiKVoZjdmYrQsrf40xBRn3njV8zuonl53xltRut449uCm493ySR8ATRt4Xdlcg1QQJd0sInZAK2BkMU1JaFsynfdbcGtTdypYCDe8R98uCXpLot8pJ_SpfVGEbW_aOUa9Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدئوباشگاه‌گلف‌یونایتدحاضر دردسته ۲ امارات برای رونمایی از«آندرس‌اینیستا»سرمربی جدید تیم؛ اسطوره اسپانیایی وارد دوران سرمربیگری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22614" target="_blank">📅 18:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22612">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZtJanUS27Me00E6q9VcibbBF7aTn6HoEsW7rPxVceEIGXEy4tMmiGGp69F8eKI3dTtZDoWkNreZD61qZT8EBOdfJGfUrBQOFMZOasXx4GKqBILxD1Az1gJu44Fj3LlZJSsMLamj7sHebZ9nRq5eezT56_sAJI_yStkw4N3RdXm__JMyGc9dAaBhmezlQLEnx1wbkApapb0vPTn9nFv6tG4_EpefEFElYlcBGvapbWkxggYUawVai8POJImhc6fKFTRUTK0ge7FiffNAYvrbE74I-IXMIGMTY-_3Jvtq_ENLbDhrfE9N2VCA34hp4bW2kqz5aNjIKjsBTVhZ_UG3Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت
؛ ویلیام پاچو مدافع‌پاریسن‌ژرمن این‌فصل در اروپا هر ۱۷ تامسابقه‌روکامل‌و بدون تعویض شدن بازی کرده که‌یک‌رکورد خارق‌العاده‌حساب میشه.
🤯
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22612" target="_blank">📅 17:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22609">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=Vun7VN0uZWyKQ8IEk32tvly5zYKQSbLDKnI5pi69Ln5JuYucmXEK-pi3zFFZdndWnFB-W31RYzIqQq97XYYJ7epJi-iLuQ-7t_GDKEzfVei4PaHh4Kk5nZ9i6PywYVEEkar1969HsF_7eMkfBitk4OgehvcyIe6-pwTubKOBy9qXDc5uEuvbUZPPdXH2uvJQhfh553k9BD7APXemLLgR_IBLr85-CPN-2tiRRsFU6vufIfMRpu8XoLCokObOaeTWfLla2T9tWih6UxNWkMU-iwrXMaVMR4wCCnrHVis2QScmXW9XYSjbTd62kVFg_-KCrSQjVQM2tGSPx8Lo_2A6IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f31679a7dc.mp4?token=Vun7VN0uZWyKQ8IEk32tvly5zYKQSbLDKnI5pi69Ln5JuYucmXEK-pi3zFFZdndWnFB-W31RYzIqQq97XYYJ7epJi-iLuQ-7t_GDKEzfVei4PaHh4Kk5nZ9i6PywYVEEkar1969HsF_7eMkfBitk4OgehvcyIe6-pwTubKOBy9qXDc5uEuvbUZPPdXH2uvJQhfh553k9BD7APXemLLgR_IBLr85-CPN-2tiRRsFU6vufIfMRpu8XoLCokObOaeTWfLla2T9tWih6UxNWkMU-iwrXMaVMR4wCCnrHVis2QScmXW9XYSjbTd62kVFg_-KCrSQjVQM2tGSPx8Lo_2A6IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22609" target="_blank">📅 17:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22608">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAvKRxTmV5mcs4dKUdPRbqCg-7zGmHTrTRITzxcGy36o4UC--TyJIIh0PNeHg4BfTUVA3Owzq70Uny74LWc1F7HWrJWFfNtUyMKz9R4BqwoJYyipcMnZ4qq36LiAE7x_B435uEfm_c3gvPILIDkPAsFeqrgRKbSHsBlVQjijol-q7VlGTaPcOnP4EEeGA4PXmcC202snQz8hhC0Qh1u4ZXwXPJhRc-GGgG-O6OY8zHNew8eEZUoZm6eQiGC7FeYresGFSRwJQnOj4IwxwGg4eXyjBNyhsYOFVuJA_8SXasjI_yP5FiuVYqRYzytIgD91qf1ltmmec3m6d4YL3yD3NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22608" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22607">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nh1uWOEHEXBHRlCmh9MidhAHO4agPm7ALVF5I7dgX8AGQvC1ujBS5UnaElCfrmW9Qcw9M7ADMksQtV_x-Vdl0TpqoxTGvVHYqhzZ-KiW3_lneCJ3BWv37s0A9bFD838LDHDexba1W5_QyVDDJ06lwrHK3vxElyTpx8zdGJlzC2eKzCmgi1nYgjDo7vqHJcld3FA2iNugQWfKwvsk9UAxOGIUdD2VSl_s1eYlDS1J9KS1YjhJXtJgo9Pmw-_bJUkWBZKuw_qNEa6Z-DW7btF77Sk5Dsr3VXRhVbr34TnrsKoNYkMApmtFYZenYlUqLjcMfA0VLW06dF8woyJ4_Tcpjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی‌وقطعی تیم فوتبال جمهوری اسلامی برای جام جهانی؛ قلعه نویی همه جوانان رو خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22607" target="_blank">📅 16:30 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
