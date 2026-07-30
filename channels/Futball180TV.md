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
<img src="https://cdn5.telesco.pe/file/XWdUxjxwYKIg4RFVkyYlUj3sCnNrEcsn58GmpP-kbe8jqG5snBCmsJHIHLsK9c3i8c4EPYE_a_aJpwzOU-MkdAkYoxCy-jWwa98Gj62waDPXNZwUJ_xhhSlLTgSEQoIRYjfIUEvCaokvMVUZ8w83gFqgpXiBBFZ865sY88d7CA0dL9c_jctT9y0n_bHRWn4j9iruK_ib3gnZxMXYha8BNEbZacwDo1IwcS4fG20gBWo5ZFWSpYHgRzPYifEsV41R6xWKBkHmxAQ1yw8ueMQ01dQjk3N_zTiNq266KgjtFSpoAc33vHeAZeJeDG1tzv9_e7ZBIpB2VOge9spQTdXANw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 513K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 10:58:31</div>
<hr>

<div class="tg-post" id="msg-102315">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEJWuDtemdI1MmV-arsWxdozGKeT7mLFcGUzvGA_Cfi04wvRd6NB2H2-r5jwcgrVttMFdSzICR2Crxfv6A2ileQ8NU-1lLZsbIRerUV4kDJB7m_UB0JtNrdqTWVCnaqCIF9MCwTDqPM0tFRwnmsIvmlnxGGHR5DIMyx7X0hzVJrZJY6TbjMtHpOUgeN5HWfthkR_YlpcGRWNKr5miSU919CP2NMmU42BaqXO0MgVLbEqovfcYQ92GqvZ1B8aM0DUV_sHbfI1AJ51JX9Am1k9i7BExl4Z3jBK9q2ifEqfmo3pj5ujCDoJYxeS-8TT_7Fqr_nhY7rB7mzCjalCP6ar_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
🔵
با اعلام رسمی AFC، مراحل حذفی سه فصل‌آینده لیگ‌نخبگان آسیا به صورت متمرکز در کشور عربستان‌سعودی برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/Futball180TV/102315" target="_blank">📅 10:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102313">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB8VFnNrszajPacXstSh9A8UjUVhBQMMvodOfpFvsY9cBOhLDWn5ASKGkqIImmd-sixWcYzcaKoZANgKW7EXhMmU8OcsnXRwH8qn_HLZp-f_dk4WtFNGpCZiO6IPqd1ENcvUbKbqGIAmg_GoVeUwmJTxitZY1h_NGHfq4fXLo4P9jVffm6mb1xM_3B1olF6xP18KVs_zH2SAGkDdh7e1n4Xh0H7N7w-3mT3GYLhnuZacoGmgTxRliKeV5srPgHM-3iR7gHAlzNzfaEjTXsQKFUUv5U0lauayWiJgiJFrTbE8j1s70RtW7FrR9yjuXdEFgClSeBTtgHNgsVkvuPd6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ایوب‌بوعدی ستاره جوان و مراکشی باشگاه لیل در آستانه عقد قرارداد با منچسترسیتی قرار داره و بزودی جانشین رودری میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/Futball180TV/102313" target="_blank">📅 10:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102312">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac4341594.mp4?token=qBVBxdS3BWZ-5yNFsrCw7AB9GA2hyRnzsknf20OwLusZpmtI2ReEjM2kFmzrA7IVykJSguJmtg4c0ygMbQVMf1rzO3ULNBwdxf-JAqoSczuBdQNH5s-bZZZO9iipZnIuPslANDiDx1HUE3xdWOIF2R01-yVKpoNVuGOLMkAPVuWmKBxNHJd3NXtIFAlG5bt1RL81P6qd9ouMQTYvwgFbKQCN0JgE5oHtDWFthV07MeuoWgOGb1qhyLyH9Y_gkNefYU5sVi9lo42gK9uw3q4URZJVnCD1IlUMooUmCinn4n5o1ZhpNQa0tVWe0oyHo9KIjlugkYNG8IjWbv6cJKSQVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac4341594.mp4?token=qBVBxdS3BWZ-5yNFsrCw7AB9GA2hyRnzsknf20OwLusZpmtI2ReEjM2kFmzrA7IVykJSguJmtg4c0ygMbQVMf1rzO3ULNBwdxf-JAqoSczuBdQNH5s-bZZZO9iipZnIuPslANDiDx1HUE3xdWOIF2R01-yVKpoNVuGOLMkAPVuWmKBxNHJd3NXtIFAlG5bt1RL81P6qd9ouMQTYvwgFbKQCN0JgE5oHtDWFthV07MeuoWgOGb1qhyLyH9Y_gkNefYU5sVi9lo42gK9uw3q4URZJVnCD1IlUMooUmCinn4n5o1ZhpNQa0tVWe0oyHo9KIjlugkYNG8IjWbv6cJKSQVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Auraboat kids
💀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/Futball180TV/102312" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102311">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVo-pF9M_5gOhI05D87eEXnaw44hjTWPBJqsljtQ3a_2yoqKcy-pw98jpeUgbEN-jprEAHH7qGSjuSQnxsHnixApYl9WbIXsXzb5P5dvl0qf3YUNLvPG8DWIhZPyeH1V2ZrcVFndAanU_ZftWYT5vS_XPy5HHh4mgNC2_JGNV7FB8COa1j4Thzcs8LpQ9p6uO7EcQpkLvmkYIZvswHD2e4wQy6s9OEAZdI111vi6LY_aELA7vyutZwiMzdiHMRQ5JVY0qATR_A85zrtOO4V6cTnnZvLIRgTTdt2YAJsqS0-hquOyCCDYYBBga7YWgwN8yPAQXv5j6k9t-Fu-S0bqqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
تمام‌نیازمندی پسران فوتبالی سرزمینم :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/Futball180TV/102311" target="_blank">📅 10:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102310">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EB1r4dVN7ocAReIXKuzMolPHY8TmkZlmYWoo2L_Ys0Hv1rfu4m51AN3P9M_6aJxunY6mcp5BRicKQSqFBmpX5LZAOfW3WkVDh-T4WDcO5ODClD-IiQg4ZxWA7puE7dgLRtfqKithhR61381PNYKHZpvdQU4mJ4e2umuyfNBlGzZvR3BOf_VUFipDTpPZBNqSz1V_-ohwJ2593sOmC1V8MKuVLaYnfLNNeyKHq9H7rO3T1bXBky4TF243wpMdg6Yc6QxduVBDFuVaYpa4YnVXLUzeaDtD2USSRLfk0YwBT2k2or3Bs8w1DiFFgcHFcao0BY2-ztrtLXkAqsQYJuuU5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🔵
فابریزیو رومانو:
پاریسن ژرمن و موناکو برای انتقال مگنس آکلیوش پیشرفت زیادی داشتن و معامله در قسنت نهایی خودش قرار داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/Futball180TV/102310" target="_blank">📅 09:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102309">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mc3rKHmEU9oGz-PmCOUBes-fpd9cv79OoEg1kHp8SoyUs7ct2zogIJ2cRFSnr_VpDOM4hDU9FPAk13Yi6Ua2tYlO8evgIBARSg3rPMThnwzoopum0_Nk1HZJdJtPn7hafl6rPFTx1r0MGuGgi-bUcXmkrTIKpqTyQ-m86XGtWxJ79U7t9dx3RV_EC7K30QA3Qyuol2nTY-bgFQ0D69HsgT5KKossLuXtaM7KzlAd-t8yyMhujc90rDPN1cm3pp-fPoN7Kawo7Q7gikhqzQ6q1yp6zx0L_WsqZ5IJra495f89HilUW0rCZhxpyOftTdzP79AmTm_tpJjvYKNwQJ8V5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بلینگهام برا زیدش تو تعطیلات عجب پایی میخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/Futball180TV/102309" target="_blank">📅 09:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102308">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTsGDQfnwY95eoS68iG4owh0p-M0Vr8pjXg7NZm4UUYmgDr_k2fHftzCzqu_tCL4GcuSUbuvfquN4IEzkA-M5LNRtUIVoTOw7SDxhrjjKD5F29V9pDuDb_tNrqC3JPySsmBcZaJTs_zVVQTgQHYtYBUzVsZ74lPaUdmvMhvegCYlCeuZBHGIIX_g4jBcjOP0wiNn98qTpT-0MGqgqx9hxwjma1mfuxO5SlBpPPYqzP85OfBkzb-R7uElDvXv_tBnNiCzRxSa1CZBnJ0KuQ7rw0iavIauWr27n5FlmMU_6rBnWGdLiFFODQjaWR5OJnpbDQx2jbFK7_hebH2Fspqt4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
عکس پروفایل فرمین لوپز، در حالی که تمام هم‌تیمی‌هایش در تیم ملی اسپانیا عکس‌هایی با جام جهانی دارند.
😭
🇪🇸
لوپز در بازی آخر بارسلونا قبل از مسابقات جام‌جهانی، دچار آسیب‌دیدگی در پا شد، که عملاً شانس او را برای حضور در جام جهانی از بین برد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/Futball180TV/102308" target="_blank">📅 09:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102307">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31f0971b6a.mp4?token=L4oR3A3-0t5E1D8qHdGHEnEarYhu5QoZXM9v5RjPe4EjGBiQTUEXduUr8L_qRQNL5aJeUe08RJ7RiEDjMKVyiKkWoERAfrbWHdpKFROgVntpn5TsS_5z2cJTr5vb3LIquZdWd56zKyGEY32wIf61kQEMnslEPwH7LZe9sIsV9nfSaU7QECsvXmOM8SI0C8QyABaWTnywXmY8j0gxcLYGU5MxGA55dDGNotYjVMaXrWaRY0d9N932nUkLjCRQePlIOIs0aBWlrI5eb9pe2nmtKLrPuqvUtTLZ3ZLmpL45kbTIgWFm9AKs-e-iNrRQ2g4VTbaTs_vH6G5tQvk-RvSTVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31f0971b6a.mp4?token=L4oR3A3-0t5E1D8qHdGHEnEarYhu5QoZXM9v5RjPe4EjGBiQTUEXduUr8L_qRQNL5aJeUe08RJ7RiEDjMKVyiKkWoERAfrbWHdpKFROgVntpn5TsS_5z2cJTr5vb3LIquZdWd56zKyGEY32wIf61kQEMnslEPwH7LZe9sIsV9nfSaU7QECsvXmOM8SI0C8QyABaWTnywXmY8j0gxcLYGU5MxGA55dDGNotYjVMaXrWaRY0d9N932nUkLjCRQePlIOIs0aBWlrI5eb9pe2nmtKLrPuqvUtTLZ3ZLmpL45kbTIgWFm9AKs-e-iNrRQ2g4VTbaTs_vH6G5tQvk-RvSTVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیوی سنتکام از حملات بامداد به ایران
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/102307" target="_blank">📅 08:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102306">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‼️
👀
اسطوره‌علی‌دایی امروز رفته بود مراسم ختم اکبر عبدی که مردم این‌شکلی ولش نمیدادن و دنبال سلفی گرفتن بودن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102306" target="_blank">📅 02:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102305">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiGRLnGkH-vYsSQstItgbbnMIRJoQ7CFVGTKYotSWtUiz9wRma-4drwdSS0FsPShE5HSRm2oa_3zNQP2AJTKAdRMpwpetixjMR-99YuNHYnOzGpLAFIBn8QTBMYQbhoI-qFZBNW3K2O_n50QbFhTzhtzEewK33d7WgaOkvQ1k-F2IGYUGyoSAgkCaCAUudX5Z4zgEiAizrm3eTPBfLH7rnyYN69CNATC-BxojAuNSZhaC3IvrBqWKA8NE8-669koQv4A-sRoTFNTZHbEMWeuBvKog_KoqkWEzwwFGtni8hou3jgaY1Tz3_IOsz9O2lDrVPU2MRf8m4H0Y3W0R5gG4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از Cope: اولین پیشنهاد رئال‌مادرید برای جذب رودری به ارزش ۵۰ میلیون یورو تقدیم منچسترسیتی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102305" target="_blank">📅 02:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102304">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9kjejOc8yYSY0z2G3b3_Cd1aAZS64_YkrN7hBT2ExGvGf2-ff-FnBegpCy6r9a5Yhn8ewpkUV0Ipnq6AGfnugV6MhCD1B3ToQfmtgyXRLSuZniErvpfaA65NX2FENTZWIFIzzj2MmuRRcv9Dv4Y2W9EgD1zkHLsZ0kJjnyLgKWAxP7j2C8UWjxT50XZrkJ93lh2DqDrmgGn4ZOGC_iihj-yM5Hp6K1hT8aq7nlSRx9_skRoHN4_OgwP8NQbwHYwEPcQPSbkJy6EYNQLwUxDUlTKm9fwzvQqr_Uqu7tNEPDuZseGWT1cU_F-SqNYMPtlhAZDUanUvQa3moH2J6YVfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
🇮🇷
وال استریت ژورنال گزارش می‌دهد که دریاسالار برد کوپر، فرمانده سنتکام، طرح‌هایی را برای یک کمپین هوایی ۱۰ تا ۱۴ روزه با هدف قرار دادن زرادخانه موشکی ایران به ترامپ ارائه کرده است. ترامپ هنوز تصمیم نگرفته است که آیا مجوز عملیات کامل را صادر کند یا حمله محدودتری را انتخاب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102304" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102303">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6afbb43876.mp4?token=pYEud3Ay4wrCoLu_OqrKY7pLUjCW64BfaQ3UCpFpK50NpJiOI8Q7V9jJKxDFatYdJnT9n0VYiZle_xh1-aeKdAWHzja4icCXJtWM74KtWXDbtcMUXH8GdCWkAwXLCsDsukcoIxBesJ_AvaxT2N_3oH_tVftNRUTEoeVkEmfaYqelt46FnI0r2ohmDK_w8K2upkr-ZLJNMlI5mhG7bswC3BAyAMzUK9ORPB6qjmiqfiik8Mek6rjMMUcJV-QPd6e0JyyyI1VuZDoMB2EERyLkzLvx6HIvB5yHRwHyBMxKeqpxZM0KQ_-wmQtUfc5p8gocAo7mfrj4bXcuFRlawHY0jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6afbb43876.mp4?token=pYEud3Ay4wrCoLu_OqrKY7pLUjCW64BfaQ3UCpFpK50NpJiOI8Q7V9jJKxDFatYdJnT9n0VYiZle_xh1-aeKdAWHzja4icCXJtWM74KtWXDbtcMUXH8GdCWkAwXLCsDsukcoIxBesJ_AvaxT2N_3oH_tVftNRUTEoeVkEmfaYqelt46FnI0r2ohmDK_w8K2upkr-ZLJNMlI5mhG7bswC3BAyAMzUK9ORPB6qjmiqfiik8Mek6rjMMUcJV-QPd6e0JyyyI1VuZDoMB2EERyLkzLvx6HIvB5yHRwHyBMxKeqpxZM0KQ_-wmQtUfc5p8gocAo7mfrj4bXcuFRlawHY0jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
عصبانیت شدید آزیتا حاجیان خطاب به مردم در حاشیه مراسم ختم اکبر عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102303" target="_blank">📅 01:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102302">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-ULDr2bO23KF1n2QecL3EVvh6rn4e0jSxb_2FX6W73GJvkY9e_zl7-Ff6NNyjYzUfKc05t-9JKkWQ-1F8QGmYtgJk5r0B8mJjNp1QSkOgcGp0_rOpYJ86KMneOWp361DzzH7eKCqCknEg3XxDGm4hOkvvYjBsNT3L-fnZ1z5rPCvzc6p-xpRvhzhmWDElC60IM5cvV8ZRFanN9FvJ2ShAnsvisvLO9VrFrffQxXsL0BV8w1EoAGWKZ136ua399U58jgShsB2DCvcl0L1z4x5N-p-ycYs4pm6_v_6tnreG-bfT_n3bI1BXfPL7kZD1E76jg8SfpbAhRxALZ43iFQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🟣
بازگشت لیونل‌مسی به تمرینات اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102302" target="_blank">📅 01:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102301">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4e2122bef.mp4?token=HgvShlLPDCGku7wXfOI72StERNE4stu8pjsUfG5Bb9en3qSvZXF1CShP5l-jSKdjKfQxKUxbqox2PVY5bCoRN-zkCTaFQ0GB-juuGWFQkt7X6Ah-UlST0SMdnWjyjSE21ciGwV9Jiw9fIswK-aGWFu_B9Wg3id2cZQumPvHPUvPYxfocDek4icDWGdla6PwQ9Uai8GIhLYLXbbOHAm4vbEBIvuq9Mu8_47l5b8vRjT4G8iTcKN5_n-C6gATgWASpcrH_gL1xhE0_iEwQMyGI2vUjTv4NLLW-5sfeOrIi4hyjSH-cnzQaznvSuKuHNepWqFrtdFHH9piIJu52fnpA1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4e2122bef.mp4?token=HgvShlLPDCGku7wXfOI72StERNE4stu8pjsUfG5Bb9en3qSvZXF1CShP5l-jSKdjKfQxKUxbqox2PVY5bCoRN-zkCTaFQ0GB-juuGWFQkt7X6Ah-UlST0SMdnWjyjSE21ciGwV9Jiw9fIswK-aGWFu_B9Wg3id2cZQumPvHPUvPYxfocDek4icDWGdla6PwQ9Uai8GIhLYLXbbOHAm4vbEBIvuq9Mu8_47l5b8vRjT4G8iTcKN5_n-C6gATgWASpcrH_gL1xhE0_iEwQMyGI2vUjTv4NLLW-5sfeOrIi4hyjSH-cnzQaznvSuKuHNepWqFrtdFHH9piIJu52fnpA1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🟡
افشاگری مدیرعامل کارخانه فولاد مبارکه: دشمن با بیش از ۵۰ موشک مارا هدف قرار دارد و بزرگترین دستاوردش در جنگ همین بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102301" target="_blank">📅 01:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102300">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDY9e4LlpCO-exEFsAgtv2zINiYALr8NnRhuhSyCVc3qUrqz7mJmk9xY-DKwL6a67zk30PKUKCM0aRP4ecFe5bF4uG7fR0MX0M4qOAnZrC69BmbFIzi1RJNd1EESAmhB5r95RLxpddAXd4Y6J92MjogtPO-avcOixFe_iaHeNzyYKgLFzMemS5WY_8N43WWj_gI8wHNAu78rCkCjFJ8JSR5pzyxvwF0vLsNBSE1jOrDo_VbwhF4L7nM4Zl272Fn8OwBAVYeOKf9ikGg5KCIwsfHhXHfXkkHzevUXihLXwRIayNJ0v-Cv9ckG1sLZw8jJwgktPcK5zCx4lZviCX_GMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
📰
به دستور ایلان‌ماسک، صفحه خبرگزاری تسنیم در اپلیکیشن ایکس(توییتر) مسدود شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102300" target="_blank">📅 00:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102299">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07fe21feda.mp4?token=nXt69RZaFTN5rRiO61Q6F6PvyzUsdh7YpDRc4GlOlpHxZq-pkzn5aFlP7o_oA34IL5lZaYswNm5Ryhz3wCU78Hqa3HlJZS6RLurTcrUnnzz3z_20b8aXdgWjh8ltf-dCSgP86GicL8IQu_9_LeVH3ImVyDizISLhyyft-Y9YyE4mdfghi-ZmZLEur-mP-xZf4zwvbs3WDBfRQSanOh6Qc7VFilc9xLiz9cv2adCm1zuhwU1fb39Ppt7eSjSzV28Pd7HTuZ0V1pm4-_nG7o4l8QacTvxphQKELHh8r76NIg0gC8tRpcHkVbtqBHxDKwFMEKy-RpuayqsH2hXu5Y_huQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07fe21feda.mp4?token=nXt69RZaFTN5rRiO61Q6F6PvyzUsdh7YpDRc4GlOlpHxZq-pkzn5aFlP7o_oA34IL5lZaYswNm5Ryhz3wCU78Hqa3HlJZS6RLurTcrUnnzz3z_20b8aXdgWjh8ltf-dCSgP86GicL8IQu_9_LeVH3ImVyDizISLhyyft-Y9YyE4mdfghi-ZmZLEur-mP-xZf4zwvbs3WDBfRQSanOh6Qc7VFilc9xLiz9cv2adCm1zuhwU1fb39Ppt7eSjSzV28Pd7HTuZ0V1pm4-_nG7o4l8QacTvxphQKELHh8r76NIg0gC8tRpcHkVbtqBHxDKwFMEKy-RpuayqsH2hXu5Y_huQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
پلن آخر بارسا استفاده از ترشتگن تو خط حمله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102299" target="_blank">📅 00:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102298">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRp0M0fHlwhLVz3iEd5MrgXnb6VfdNVEdn1z-bODn5rDr_olgf2YXQzLR3p-GW4j3yo2HUawZl22mgV9Nr0HJVLgoc9t-06BDRVrJIlpIhjQClFtTn0tjU4YcW3rmLfbXatnR3-pMnGUH4xni0dSZ8H_jQxZ5AtRgbR62sdDHdsTaoan8utitydKYE3do0I2Iz3CAEZZLVIr9PqbmJj-QFlNx75HJ9HmcB56rS3_XWj4V0j2eD2NyGmrDxqprcYiBbXzc3J0MDuMbZpI6lzkcCcQY6yF1Vat03WD9J27bnpINd17kfa3SwZNPVZOnzNp8sQ4AMtWaEt-H0F2Goo2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز
:
🔻
مورینیو، وینیسیوس را به عنوان یک عنصر ضروری در رئال مادرید نمی‌داند.
🔻
باشگاه، این بازیکن را مجبور به ترک نخواهد کرد، اما در عین حال، درهای خود را به روی یک پیشنهاد "مناسب" بسته نخواهد کرد.
🔻
همچنین، باشگاه قادر به پرداخت پاداش قرارداد به مبلغ 80 میلیون یورو یا اعطای 80 درصد از حقوق تصویر (حقوق بهره‌برداری تجاری از تصویر) به او نیست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
از طرفی نمایندگان آرسنال پیشنهاد خود را به‌وکیل وینیسیوس ارائه کرده‌اند و حالا همه‌چیز تحت نظر وینیسیوس برای پذیرش یا رد قرارداد با تیم لندنی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102298" target="_blank">📅 00:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102297">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOh7TKKAdpYcsHC11BjZy1TVaekyqeMBeT_XIzjGzX1h1YiY2xGK8aTpAXusztt6AM5TTcx9D38aio_54DmWTYmNEkl35NkfBCg217vx8FB1ivu9f-foK4JmUWrYsz796hyBdysL5LZhtSvMQKUL5zQKu2i1D8cb9MO9t0uOJ6-hUlendT32aOPTy7m6RRmWVhdCoiTlNire276wdJv3ZfNumvo9nvx5xtMhDcvX4mJjlBGo2QPiYlelz7K_EiDH9Djjh8H7rjDYOC_MfY4VDduWAvc1dfnZPXz0a7HgJxAfubN7lEdyi_smwgqeoaZgGMl6PPpPfGfD6SeBF95szw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇪🇸
🇩🇪
فلوریان پلتنبرگ: امروز هم توافق میان رئال‌مادرید و لایپزیگ بر سر دیومانده حاصل نشد و مذاکرات به فردا موکول شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102297" target="_blank">📅 00:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102296">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a93d51cbc.mp4?token=qMMjDPYjycDNjCoBQ6N6m0bdqMVjJuEuKgHWFqv9ZWFYA-hAktaTlqM-cvE29EJ-fzPYM1l79lZotPnXLOxeja-zWMb7zMW10gSZmkIaNA6hZgGbOOC33bAl-pG0wIU_Y3MgU41Dx-ZxnbjBEP9if5zubn1VOrHk16Prq4Objj_xpePz5Z_BdYyrKoBAttEZ3HdceRizBx0-8GtTBvIjVjGmNHAjBvMNoBvKyc3PzkbBGHixr1igX-GWplONRUp1YYLNfUWkj3snhoG5aNo2ZtpDh_u-1TO7uWgLFqxZjbW8VxPJ1T9IreevoqB4WukHe8tGFhIW9WdGgOMVAWym-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a93d51cbc.mp4?token=qMMjDPYjycDNjCoBQ6N6m0bdqMVjJuEuKgHWFqv9ZWFYA-hAktaTlqM-cvE29EJ-fzPYM1l79lZotPnXLOxeja-zWMb7zMW10gSZmkIaNA6hZgGbOOC33bAl-pG0wIU_Y3MgU41Dx-ZxnbjBEP9if5zubn1VOrHk16Prq4Objj_xpePz5Z_BdYyrKoBAttEZ3HdceRizBx0-8GtTBvIjVjGmNHAjBvMNoBvKyc3PzkbBGHixr1igX-GWplONRUp1YYLNfUWkj3snhoG5aNo2ZtpDh_u-1TO7uWgLFqxZjbW8VxPJ1T9IreevoqB4WukHe8tGFhIW9WdGgOMVAWym-DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمای اورانگوتان از بدن کوارشما ریخته
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102296" target="_blank">📅 00:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102295">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4b353d1e.mp4?token=sjTBMh0llkLePIYT9NIymQTuB7dXv3sNug3or2M369PhP1ON32GXQZds1qxJnIfffJ4EN44hjk7FpZr1Uj-oHK6UYb0sb8Pk7Hd2yyWMO2ipN_W9seFrzgPpffTOTrAbRv2Ao5uYLmOPhIZF7HpcBZ333vDbZnoH2U6CRMf4_bD6rAbp-xLvuDfoyVPv9KHA7opwllHfxe4_JCHxvFAUhc_H0POiJcZFbXwEYnZBo6YybQP3hKdvxLietoS3ub4yfqdLiYQNQDSxR7_JPTyRF_bd83dSJvH2VEGosskwrKqJvaAGEUGm7gGnn19Kaav3FvAdc_8qQwvVicY9P3UNmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4b353d1e.mp4?token=sjTBMh0llkLePIYT9NIymQTuB7dXv3sNug3or2M369PhP1ON32GXQZds1qxJnIfffJ4EN44hjk7FpZr1Uj-oHK6UYb0sb8Pk7Hd2yyWMO2ipN_W9seFrzgPpffTOTrAbRv2Ao5uYLmOPhIZF7HpcBZ333vDbZnoH2U6CRMf4_bD6rAbp-xLvuDfoyVPv9KHA7opwllHfxe4_JCHxvFAUhc_H0POiJcZFbXwEYnZBo6YybQP3hKdvxLietoS3ub4yfqdLiYQNQDSxR7_JPTyRF_bd83dSJvH2VEGosskwrKqJvaAGEUGm7gGnn19Kaav3FvAdc_8qQwvVicY9P3UNmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال تو تیک تاک : دوست دخترم خوشگل ترین دختر دنیا با من آماده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102295" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102294">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!  ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102294" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102293">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=L-P6u7LZEOVNpvkswGKDM9vHHMi03plrkErfVfoB34HyfhGwxS7NyFL64gFMqeHXk8Hm7Giqdlm67C2QORj_ALkSWkjRj_PA5bbot7llvW_gEpTg8MWJ1r8cuMpCvEluH2Sqd67PGmEnd63I8HeRcrE9gV-7QwinPqx4-YYB9duRd1cwfx02NENxWIEbYDnSMZFduW6Lw6CLwXk7Oglzp0z5nou7Cx8b48c6QzSbF4cnKN2b-PXjariiNdE7kTt_pVyOXlSMBeKFC0y6snMIjnR98FrItK9guOIA2eYUEf-LvJNVCwn3tlSSdqFSx9_IJyZPfbLgqZ2u918nEqj8wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=L-P6u7LZEOVNpvkswGKDM9vHHMi03plrkErfVfoB34HyfhGwxS7NyFL64gFMqeHXk8Hm7Giqdlm67C2QORj_ALkSWkjRj_PA5bbot7llvW_gEpTg8MWJ1r8cuMpCvEluH2Sqd67PGmEnd63I8HeRcrE9gV-7QwinPqx4-YYB9duRd1cwfx02NENxWIEbYDnSMZFduW6Lw6CLwXk7Oglzp0z5nou7Cx8b48c6QzSbF4cnKN2b-PXjariiNdE7kTt_pVyOXlSMBeKFC0y6snMIjnR98FrItK9guOIA2eYUEf-LvJNVCwn3tlSSdqFSx9_IJyZPfbLgqZ2u918nEqj8wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چالش ۳۰ روزه: از صفر تا سود مستمر با فوتبال!
ما یک چالش ۳۰ روزه رو شروع کردیم که توش با تحلیل‌های روزانه و مدیریت ریسک، موجودی حسابمون رو چند برابر کنیم. تمام تحلیل‌ها و فرم‌ها کاملاً رایگان در کانال قرار می‌گیره تا خودت روند سوددهی رو ببینی.
➕
پیش‌بینی تخصصی بازی‌های دوستانه باشگاهی و تورنمنت‌های معتبر
➕
فرم‌های گلزنی (بله/خیر) و گل بالا/پایین با تحلیل آماری
اگر می‌خوای از روز اول چالش همراه ما باشی، همین الان وارد شو:
🔗
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102293" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102292">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRoQUekpev5A2rNCB0epsMpBhrIGzke-kvppxDhLL8XV1ObfYuvUYdFy_HsfztU9ox8B60sj6p3vk3U9pKbho0sMcCUFQtwWcDmM3qadaxXMl-nz8mXFTiQXJkMYhGn1JcybhEFO57hxyLHvz_neOBZhQMD1tT8YsbxAwZPMuqP2tKmtU0dxo2zpa_l933XDXjTZfR7kdvRyFnFCttMyrnkJl9L9Y5_hM9QmAHDEOZ70cq7Spim4g4-82TTrszr9JOXk9XZSMo7mL_7fYWvSI7unoh6IGAYcDGijU6gevuFyfgRKHtM3WHpvCZqmunNjrzPBGtfq8skol1bOLG3t0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از پپه آلوارز: مارک بلینگهام (پدر جود بلینگهام) در پایان فصل گذشته با باشگاه رئال مادرید در مورد جدایی پسرش صحبت کرد او دلیل این صحبت رو اختلاف نظر در مسائل ورزشی اعلام کرده بود.
باشگاه اعلام کرده است که جدایی او امکان‌پذیر نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102292" target="_blank">📅 00:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102291">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtrqpHQs9GHXLuhN19y53ogbx2SEID1iTtQ89mmaNPy2a6z8vNBSnlEbSSe4SW8rm8qfCIfsKsELqJzvYtE7cH4LqpCc-VVo_1q_hy-3c8pD51dB29JW5ZSJHhS6eMFs1cKEa4q5LdSQKBAttGnJV3egq5vy0YUFh9-3vY7cjfPTK_Lb1YcOLfMphr420M-Rv8MM-i1k2K6nIyKWSH_90E4AVVOl4mQ5uSXRV4HyuYEEpyBjPfjxluCUAOPpUqSNVwsdU-grqxqZAVzebxu4m-9gNUNBmsk8eZs6P9Fu5s8nb3jStHVxjT7uvf-RNFVRHxRFcF2aOLd_mDuJT3Nv_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇹
فوری از شبکه DAZN ایتالیا:
استراماچونی از ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی ۲۰۳۰ پیشنهاد رسمی دریافت کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102291" target="_blank">📅 23:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102290">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqq8Xro5QuI2OwgGP8NndRb-XitoknX7Pqdm_IzfyV26BlLRRIb2O6qI7itNRs9xSxDB0oJm5j3Ptr2yKO7nczh0R3tCltFoIT7AEagKgi_hF28ilTuktmkJTNi7fTQXQv5vLk6TPDDWe5lzprO3PF5unj5QF5IO2OOvScxtoBrBJnU3EnfChs2U7zbjk8L-Y-x0epw4lKRQN0_8kppH1o_p1eLyHBFhH36QX8kxSO08qlrqxcwl3Efdl60pg6TX8ScejpEh-wrVzzJJLABlh6YpBFhERcy1rW4pBJsPsDXhRQWymwRfnx5VMMQaNA7D38McW2epcbQFRVpy-xW6jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فرمین:
این بدترین تابستون زندگیم بود! همه چیز داشت خوب پیش میرفت که مصدوم شدم، اوایل جام جهانی نمیتونستم بازی هارو ببینم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102290" target="_blank">📅 23:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102289">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV4AhkDlgPiOXGh0RpyFFn4TYJU3GRa310afhTpKgDtVHovi4P6rtL_vXKxJr3Wr-6auLugwyLSz5BNMIIXOADqzXTnwOo7aulEOeJ8klXsOOpVMCVoIt9nrPTQaYrpkGvJV1_oJkqFz4vY_wtMdy4l55a9O9Gb4veZ3uenprnnn3zsg-kxsBh7XZ2rmI__71bu5JNURnC0ja5oNpy488MtXVLEC6pcwVnu8Qj_h1peEk08ZlFbcThMLFeOzmS0oV4IQj8ewN6AemPFYjlPH1JXX6fOSzbhFOZEBT9imRLUHBrMpWMdppWltTVOqp7G6NSJU5WmC0t8V702uN2P9HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
کیت سوم دورتموند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102289" target="_blank">📅 22:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102288">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHtT-y_X_cX6PRzTV646UW_0Qwt1t4pnt6_3gqtHwIQ3cqV-WJ2RvSDZfJmm5x79d5_X0l4LxDsHqTpBVpB75-2aVtpXeiIKU0Hxljrkpc67QExG7B035_zHjjyHi-0Hm-PS06xfXnKYUaZcQqd47alAVw9ELnWhOJLhyWn2j_wipNTpZ3hAgE7YLn7laKTEFuo9ngN9djxGtvXrXOwujNVxbJDbVe2gX_K9uDKp-jTbEIQn8jc7sX6PkuOrr9lM76ya4MRN6LoVBkgZVxf5-YiC8Bf-0-u4rqPcdE_YFSJ2xtHmDrVK3JOohaPkFHD-RY30HNCdLbv1GB6IKX_tIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید رونالدو چه سیسی گرفته
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102288" target="_blank">📅 22:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102287">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b210f5e9.mp4?token=BSrstAeX9_OxuEpt3GtVAbYVh0AScp_pq-C3X8tjLMMz7x_aQt2lyeqY1rP3vtKfbbxkXGD5b7VzPoHI023A9UVMeeuAdTccjvbHQtqOsFrdxNX8DrE76SgEeT2Y0_1TSNkox21fEfuIkVUZtt_O19Lk7kVcs_WZctskiWJP0ZDtjZWpJjGSQjzVj3ccup5NDNVLs0tfl68Fk5KmVthEZATrSPDRPpyl75Dfpc64c-msGa6UUouX9x5yzSaM3Bm93YWlwyI7_0PPKfB-r_FRDBU8qlkOodxh9_oHW7PMM81DecHjUfnd42rN_Ch_K9EUOwtO-v3C-RaRTfOtBsAljg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b210f5e9.mp4?token=BSrstAeX9_OxuEpt3GtVAbYVh0AScp_pq-C3X8tjLMMz7x_aQt2lyeqY1rP3vtKfbbxkXGD5b7VzPoHI023A9UVMeeuAdTccjvbHQtqOsFrdxNX8DrE76SgEeT2Y0_1TSNkox21fEfuIkVUZtt_O19Lk7kVcs_WZctskiWJP0ZDtjZWpJjGSQjzVj3ccup5NDNVLs0tfl68Fk5KmVthEZATrSPDRPpyl75Dfpc64c-msGa6UUouX9x5yzSaM3Bm93YWlwyI7_0PPKfB-r_FRDBU8qlkOodxh9_oHW7PMM81DecHjUfnd42rN_Ch_K9EUOwtO-v3C-RaRTfOtBsAljg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ادعای نادر فریادشیران درباره بیرانوند:
اگر بیرانوند همان متنی را که علیه علی دایی نوشته بود، جلوی من نوشت. نامرد باشم، یک ماشین به او ندهم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102287" target="_blank">📅 22:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102286">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaU59IX1nwOdmzjysRtNLV8HW7yc09R04xuAC0tl7FqXKNVL4E4wx5JxfB1vn1f2HdGcdk2w1RDLdB3GsXjjjT19lnmy-tiL4VIPrppiwSL5Oxu4Fd9I_f17SsWXFdpcAysbJKXI7aKttLNPfhMycL9HuXOgdVnbqE_cVYUfjgPwyBMaUQARiBg19x8hxx6ExwHGCdXvNrd0J2ApYhgcxanxKugKr8bSUzKX2weeFFUCVlVlMX04fTs1hwCNJi-0Deq4RelAmIvxmsRbFOXnDman9OOrzpIOHMtRZCsJnFEGqSge2Ht4v6tGJy6zVs3fbhle1ejG4GmXnVnlFbcKvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
فیفا بدلیل نمایش بنر فالکلند در جام جهانی 2026، پرونده انضباطی علیه آرژانتین باز کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102286" target="_blank">📅 21:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102285">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb35f99ea4.mp4?token=NLyx2B6TyhuZz6iYK1Evm3j_pczjddA2sWckVRuPe5OFhotMAUv3G4kfmgzQKRvMl_SeRoit9iMgAlGsqyHHcjTVdyL711FBTd2XrD2zqhs5Pnncofidv-5ZcYhevzDsQ69wyUuuJld2C_a54GuJmwNmQdLPhMPNu_V2xugHgT4ribnfgndDOV7UOoevBA35vGJX7VQzF-sIDrXJonrZX8W_HwfTj1PavC9wYC4jD1Cfp70Kz1TRboS64svPZA8mmZGTMipt8nWx00-OlRQIhnTpX_gw3FzXDSNzpl-kqbQ70wb9AcNmOWaA7F3S5m_hvzIJviVT780B7rFS8e59dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb35f99ea4.mp4?token=NLyx2B6TyhuZz6iYK1Evm3j_pczjddA2sWckVRuPe5OFhotMAUv3G4kfmgzQKRvMl_SeRoit9iMgAlGsqyHHcjTVdyL711FBTd2XrD2zqhs5Pnncofidv-5ZcYhevzDsQ69wyUuuJld2C_a54GuJmwNmQdLPhMPNu_V2xugHgT4ribnfgndDOV7UOoevBA35vGJX7VQzF-sIDrXJonrZX8W_HwfTj1PavC9wYC4jD1Cfp70Kz1TRboS64svPZA8mmZGTMipt8nWx00-OlRQIhnTpX_gw3FzXDSNzpl-kqbQ70wb9AcNmOWaA7F3S5m_hvzIJviVT780B7rFS8e59dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از روزی که نیمار باعث شد کرک و پر امباپه بریزه:) خودش هم اصلا براش مهم نبود ضربه رو زد بیخیال رفت. امباپه اون پشت داشت جون میداد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102285" target="_blank">📅 21:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102284">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8732bd386a.mp4?token=kI3q8jT79zTzEdaALdaVVYlhVESevH2eZ3Z-uoAGMnaIVYslln3AzBoJJNJVqk4BsOt2XBcKxLroqf3tlHAsbL4HxFRtIiYjN-khrI-64DzLMDwS93Eu3FJGMBwgC5od3gM9GuZ3XD6Zz2TUXxWNBps7C7UATiRRldw7qytvtV75tvXtBaJKIcjxzQW923iWF04VtQ18eiNY-DgPwt-G7cHdcP3T-cK-iFWcPQisMsJh5vEXT_-bhfyckIpM2WXJ4L5aIZeeMpZNDgytQB0ZtNpLcbRKSiaIWws3z5sjkEmnM59fvVSJydXI73sgNx8qtQyWpBYJwrlFLvhqBCvhqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8732bd386a.mp4?token=kI3q8jT79zTzEdaALdaVVYlhVESevH2eZ3Z-uoAGMnaIVYslln3AzBoJJNJVqk4BsOt2XBcKxLroqf3tlHAsbL4HxFRtIiYjN-khrI-64DzLMDwS93Eu3FJGMBwgC5od3gM9GuZ3XD6Zz2TUXxWNBps7C7UATiRRldw7qytvtV75tvXtBaJKIcjxzQW923iWF04VtQ18eiNY-DgPwt-G7cHdcP3T-cK-iFWcPQisMsJh5vEXT_-bhfyckIpM2WXJ4L5aIZeeMpZNDgytQB0ZtNpLcbRKSiaIWws3z5sjkEmnM59fvVSJydXI73sgNx8qtQyWpBYJwrlFLvhqBCvhqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
نذر سفر؛ سهمی کوچک، اثری بزرگ
🔹
در سفر اربعین، اگر صندلی خالی در خودروی شما هست، آن را نذر یک همسفر کنید.
🔹
هم‌سفر شدن با خانواده، دوستان یا هم‌مسیرها، علاوه بر کاهش هزینه‌ها، به روان‌تر شدن تردد و کاهش تعداد خودروها در جاده‌ها کمک می‌کند.
🔹
اربعین، سفر همدلی است؛ و همدلی از همین انتخاب‌های ساده آغاز می‌شود.
#چشم_به_راهیم
#اربعین
#نذر_سفر
#هم_سفری
#سفر_ایمن
#فرهنگ_رانندگی
#سازمان_راهداری_و_حمل_ونقل_جاده_ای
#حمل_ونقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102284" target="_blank">📅 21:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102283">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuYoRbeKAGV_KWH20t-IQ67KYSWGqsPQq9FHxgg2EJJic1mqD8VywvMr32cqbiE8eV-ldE1AY4jVwoCyJagoBPUVqa24qZ1XXXEu71m7tU6qIH9XdfZHD7CoyJSuHMSyzaytfqGZjFp84TK_-l2MsCX3eftDsuauxXOQ61EQu88XcVcxLltQejU-KrhtLe5Z2aH-Sh8RiOVXzc4W9kPGQkGna4l6UGS8Y9-j-iaiphFprctcSGx2xHbbyhFLD7D23-upfhlxm_11ex9eLhUiTwXoLPfwrWxQ0SlDUzR7INnHHsc4YaI4CHDD6xazNIPZ8B3oo-r1V7FE1KWNBfMaUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید جورجینا که بسیار هم پرمحتواست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102283" target="_blank">📅 21:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102282">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGaMKz92BnP4hYh6pErfXqIjhIf7z3K4mMaxgzhBW1T_0CrHC0JrnlKLMxjMKpyyUvdOROq4r6spZ0XjJfoBxpSpaG5Cm8GRIQva-52a4OE3TKtuaynQXZumT7mVAi5EUcfmYer3krFxu3dZYtiXJ614Yb5GhTZvd3HaqJvcLLIG4tXfhNEICPDjSHH9nRm6LbKeuO4iAxlxGJME3uBTfc2ZN8xLsJ8xjnx8setKv7c6KEymCqReWDgu5SUexHncwXEwFnCDyPA7ejEubcGiuhYbRTOSRL6k-uCtG4PDa_CWXAdgQJlRryGnmQLIJusgt3D__efV0LNq2gYl4Egpyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔹
کریستیانو رونالدو از زمان پیوستن به النصر تا الان حدود ۶۲۵ میلیون یورو دستمزد و پاداش گرفته!
❗️
در کمتر از ۴ سال، قرارداد رونالدو به یکی از بزرگ‌ترین قراردادهای تاریخ فوتبال تبدیل شده:
✅
حقوق پایه (۳.۵ سال): ۵۹۵ میلیون یورو
✅
پاداش ۱۲۹ گل: ۱۱ میلیون یورو
✅
پاداش ۲۳ پاس گل: ۱ میلیون یورو
✅
دو کفش طلا: ۸.۵ میلیون یورو
✅
پاداش قهرمانی لیگ عربستان: ۸.۵ میلیون یورو
💰
مجموع درآمد:
حدود ۶۲۵ میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102282" target="_blank">📅 21:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102281">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1795b5f8ad.mp4?token=JXqU0bs6vA6hh4vlVoe1j2yk1a4TH4QNyKtIgw0s45YFRKunRCDnlVX_rSsoletil61PkV336LypsFiP1jnyTsJplVvkVpIsUKMeCSz7GCDzR9baPRdeQmIpbdmq4hAYZyEFNAShjtuUxx3ZCkWH0xxf725unPp7YhkZRpmFBxB7MCyqT3IVltgfeAcTtTn8wNlXZOkLhv0kFVHrOCt36SdQpcoLQWBm5ZHVcLhxSxIlLeBtw3YgmFdP6bQJ2Y8Dl2XveSnzdOUqC8xrNK8pqbmaSJGxs7XaORX2AWU4eKVHa68Z6797Yke6B6a6-ei7BE3KOwIj_-jlgIR0BKs-iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1795b5f8ad.mp4?token=JXqU0bs6vA6hh4vlVoe1j2yk1a4TH4QNyKtIgw0s45YFRKunRCDnlVX_rSsoletil61PkV336LypsFiP1jnyTsJplVvkVpIsUKMeCSz7GCDzR9baPRdeQmIpbdmq4hAYZyEFNAShjtuUxx3ZCkWH0xxf725unPp7YhkZRpmFBxB7MCyqT3IVltgfeAcTtTn8wNlXZOkLhv0kFVHrOCt36SdQpcoLQWBm5ZHVcLhxSxIlLeBtw3YgmFdP6bQJ2Y8Dl2XveSnzdOUqC8xrNK8pqbmaSJGxs7XaORX2AWU4eKVHa68Z6797Yke6B6a6-ei7BE3KOwIj_-jlgIR0BKs-iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریوالدو، نابغه‌ی تمام‌عیار
🇧🇷
🔺
پای چپش چوب جادو بود
• هت‌تریک تاریخی به والنسیا؛ قیچی از بیرون محوطه
🔺
جام‌جهانی ۲۰۰۲: معمار خاموشِ قهرمانی برزیل
🔺
وقتی رونالدو و رونالدینیو تیتر می‌شدن، اون بازی رو می‌چرخوند
🔺
توپ طلا، قهرمان اروپا و جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102281" target="_blank">📅 21:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102280">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnnuawTSmKR1Vg6XsFj95d_yJW5ytBqiq68Sb7j6HrRl1ZQzu9Iwf-42ngBZcszpRfm8AOMaWbZSj3_SXRPqrrmxdT8bgsUEfZsP8ymxpEyK3jE1CGiz98kyc8sdUc6N8bCKlq_wcDQH4ja8tWL_qOmfLKH6xclOFafJrd0ZF_1qh5aKp-9oOODEnILFwfOodQ3Yly-iX-_MJHETwDIOtSyBFrQL3pErmfYq1fDOxBYC8TQrIQYQ7tmhahm5002dmoNsDbuTs4eSDXBqTR9M5WtHuWg9nNrNcUBzQ4ZyxhBvVJlREH8r4fCLwqLo25CZdPKv2clh66ECyjY7FrBQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اووووووف کیت‌جدید منچسترسیتی رو ببینید که قراره دو سه روز دیگه رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102280" target="_blank">📅 21:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102279">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tD5T5uYx6XUJjL6CWx0aKiX8Q3z4UszT5Qz4iODY1r45kG1GD0ezcjtWo1VQ5uqJ9Qoc9tZh3V89rnj-YsorOLD3B9SDpdojabEK3XLMgzgiz2xb1jj8cJwd2wY8t059sD7nvsg1sOeEMjWnigwQwQJ7ExPPfGcTtuFjKAA6LaYUz70co-qAFNm2Y8qvOahD_YMdGbJ4CtmUNjCmm9Zm3nX-r82sRF0w1JYAB8n16K013Q0zbkXmKf_BEZ4Bl7xWkF6aB97vvkMXXF0DpuBGJVx9NCCqxnMDfsyIxV6ZHKp2EQOCLAUm8N5bywm9mWYWzk4DpA8Vvs3trUbqFBYdqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚠️
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#
فوووری
: رسمی: الی جونیور کروپی گزینه خط حمله بارسا پس از شکستگی استخوان متاتارس پنجم پا تحت عمل جراحی قرار گرفت. مهاجم بورنموث طبق برنامه زمان‌بندی ریکاوری، انتظار میره ۳ تا ۴ ماه از میادین دور باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102279" target="_blank">📅 20:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102277">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JsoUfgiAF75vElDYJNd8KWBiSOfEd5p0Cvokgi8PozQo0yU-Q7CB2cWcEr_LmDQMIQTP3W4M1-wDOM3NDqjs2SdV2Ia8tYFC6VCbZ_5iTrt9tnhvJkjB3ue0pHsiI3QlAipU9i9lejGIEduV97gKjPE8TrtYXSKqSE2wXQU9JH_XCDmLk1OxWm6hxyQlVBl7JMDnXp40nn3Qj9IIblaxSIw4-ksnyv8S9Hvgtps00fFTaatBeUxvvPMxhx2IyOCgDNEt1rPp60854tIAiU8xoF0Su0H_Y2_hf_BN1gQghRwass6yqHWLN_vWaYcGfX6tsqEyHai2ZKwqYFcH9rmYKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UskKSOZG_KPtQwf9H3YyWdYzJpDK0qmZZueZlbpuJrQ_u6VHKN0PZ278LeUmwRcmUU7YzQIKpgmMIlUlcsDfgkXcs0iLa_QcR0eCpdLKGJod7OxxoAoQCmVP8hiSYrit-ENq0IfhAUG51FP5DPKjRorCfKCzIb81BLm4rJU8L4-Rgeg5_Fhl2soUT0gccdM4XD4T_av5WvbxEb_HBboQe5xrsWe9BpKqkzxVNRBOxpgGbGbKFaiGefShalUYmsaaKY-qZOLbXtdALX1EtB710m8F2uq6jibQ8o3Y_Pd7lVzpH1-NyKsda2lw-KARRJ2pT_XF-8bUnzLQZoYl5q6EDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
طبق گزارش‌ها، ویکتور گیوکرش، مهاجم آرسنال، ظاهرا سر یک ماجرای ۳۰ هزار دلاری گول خورده؛ گفته میشه به یه مدل اینستاگرامی پول داده بود تا برای دیدنش به لندن بیاد، اما اون به‌جای انگلیس با پول رفته یونان و حتی یه عکس فیک فرستاده تا نشون بده تو راهه. گیوکرش میخواسته این قضیه بی‌سروصدا بمونه، ولی ظاهرا اون مدل برای دوستاش تعریف کرده و ماجرا لو رفته. این اولین بار نیست که زندگی شخصی گیوکرش حاشیه‌ساز میشه؛ قبل‌تر هم شایعاتی درباره ارتباطش با اینفلوئنسر سوفی رین مطرح شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102277" target="_blank">📅 20:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102275">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tb4pB8G69ARjLW3PP1Vahk4PAKNUDAJlgu1F-JjRVJRsvJEYevRKYkHvKwX-nj4ukV-3ZNmzS2ufsxk8uflm8XaB8nIasJ2Y-Se9kayiFbJ5u4DRBjOInwjAp9B0H_CBGSaUKGsiCevUzrWxMH5TkDpo3HayiyxZlOlU1IcXESc6zLevsEJeCT3xk4WiSTrSz7dklNMnyILVr1HmH278iTP5_DJfxdRE8scFfqXpEQvHcZy6r7eI4l9tGCzhns1QwBra4WiB3_jEY9K4Rcwgqwl0OWwJeIF9WGNUalBO7KTlls3f7OqcuwTyR7zSUS5yC7YJmS8YJ6FjgPaea7f29w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3v777_Jso9xRh8er61uLvpzUhKqKeGXcQ8rgD89w8nkUtOG5iK2eNDT00-uoOFMnEFelbb6RoHcMgwUzX9A0A4SIn69pOBaYy2qa0wE-3kEh7T6Nn-FCXkwPjBPqRuIA_d_rOCVyJli3rYs_r7bogchYNW-r_vccYweZlpixqwZ0_ad4dphQUfZJNfBDcm0OF5JTmYnfwCe5SdT1699Q2FU3R0i40yFGfKbdmXRAMVbh783n9BJ4Vj3ThXf0Wtaoeq2dmVRiUs05SqihSfGSUFxq2hBWQ3-siqIsjOzqXQluS1mSK2X_5dZuSt-ETYPbq7JGW08VP2sI3yaA2jsug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
پپ گواردیولا درباره لیونل مسی:
من جام‌ها، رکوردها و جوایز زیادی بردم، اما شگفت‌انگیزترین چیزی که تا حالا در زمین فوتبال دیدم، لیونل مسی با توپ زیر پاش بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102275" target="_blank">📅 20:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102274">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ui0yjMm3Zu_G7dypiiDJsg8_6GQ75FHzuwTHQMMhomacq8FgKZY3FvZpqAdLZRVzYGxMJzVktfYWcYXGp3imXZjNMUF-Sx7ICIVWk06MuNAIHeM4SPzySDmuMmcwWlxiurlkZbpZMUG2HpHCy__Pyo972dvVv0PUp6OEk6dsSjD3lCkay-d5Whjeq-R8LtgFl80IaAEl8PH0msZ7wiQg2hbVmEZIrln2WzHqpGdFmMFYcW1Gd4_63HG7LBHeVfZtLJo7_LtxIkwmBUIAF2wtZaDHH09FJsxg1aprS6pL6ehg2fuaUr7xdILIuGNmF0TwMjD1JEA6_OyQIEh_-S4abw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
#فوووووری
از رومانو: بارسلونا به طور قطع نظرش راجب فران‌تورس تغییر کرده و هرجور شده میخوان نگهش دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102274" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102273">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faE1UTWfzVRT-YUIB8NhxDVHpFO7zzfMMRg2D2hhioWxfsSg9if5MFl0jeXrGV3D-WGQTaFYZ5qFMO1EEHqFCp4zcemOUaAwexSe_srmLfwiE5xH_U-NjlGMEsnjbjgLp22x1SVKw4kaphVIkiKhl56V3nA2i6wP6UVuuQa_IizjieDjuZcAvVWqFzC4yYTN-s4GJEfdOYWsje46DlmQEPknzwTbVKPfTzmxesHgqVTPfx1y7Hs7hxFILoaOxAmE3S4vSScAkednbp0TmAyLbK1IXzcbTWde2DKi1IbJObs9qfMyWZE2u20xeKIDEVhSEG-TN_EgtD1cbqO7i63anw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس کوکوریا مدافع رئال‌مادرید
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102273" target="_blank">📅 20:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102272">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ff90fced.mp4?token=syCj6vFIwD2M9VOS4trrTcZ4aFGWZnHJ12VGCXUUUQk188AwN3KhQW9JtfqjUruhof7w_hVuLnyX0uYqbHpSUlszUXdDsw4DNeYrbiG4dlJkLev-He3OfuzGSH7kueBbS90CLGvWxS_MT_XrIWOEXhkMv0J-WTTUkO_VynR9vtLUqnVU6MHIhIXJU1SyjI6ZqS36a1W2TPxkYwyVQLCbKLUe_em1vHYYEHpIlw1yqY3BzhZ9TyWD3T8oUrRN_afShqp43xfjWb2eha3vL1jNXvEBDjXK8TJlw_b0BYwKHJWeRwu36Qj2ziqDQS81eQHSC2qDnO6T6zeTVQsu9KajQIYPtb_6F0eLP2uKnyUuOQ0YOVlNne30RZBHZYw2TbGQJ2rNdcNV9xL4e6IiS5yvPTJ-7AEZV3yX69zXocGnMovB5nuTQrkW9mNEh1jPikr6M4NN60d3YiSepuGn77PzkmfA00dh21KI1OBEKSHMkhrhQSjLq5tP4zXgcqpG_8gVd8MlV8VDk8TW4flG6TsVOzk55bYKbv2DXJT4N1vfdm7ABrYC3NPMbXyWIC0HL2VlDSRHYcItNWBNfDqPGRoJeih5IARyuGxIKuGGjFtATh81UsbHR8Ids21E-wIgiZEPeNxfAxM-tCzlvpctLqxOMh3Xahs0hFZbEjVGYEoVrFk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ff90fced.mp4?token=syCj6vFIwD2M9VOS4trrTcZ4aFGWZnHJ12VGCXUUUQk188AwN3KhQW9JtfqjUruhof7w_hVuLnyX0uYqbHpSUlszUXdDsw4DNeYrbiG4dlJkLev-He3OfuzGSH7kueBbS90CLGvWxS_MT_XrIWOEXhkMv0J-WTTUkO_VynR9vtLUqnVU6MHIhIXJU1SyjI6ZqS36a1W2TPxkYwyVQLCbKLUe_em1vHYYEHpIlw1yqY3BzhZ9TyWD3T8oUrRN_afShqp43xfjWb2eha3vL1jNXvEBDjXK8TJlw_b0BYwKHJWeRwu36Qj2ziqDQS81eQHSC2qDnO6T6zeTVQsu9KajQIYPtb_6F0eLP2uKnyUuOQ0YOVlNne30RZBHZYw2TbGQJ2rNdcNV9xL4e6IiS5yvPTJ-7AEZV3yX69zXocGnMovB5nuTQrkW9mNEh1jPikr6M4NN60d3YiSepuGn77PzkmfA00dh21KI1OBEKSHMkhrhQSjLq5tP4zXgcqpG_8gVd8MlV8VDk8TW4flG6TsVOzk55bYKbv2DXJT4N1vfdm7ABrYC3NPMbXyWIC0HL2VlDSRHYcItNWBNfDqPGRoJeih5IARyuGxIKuGGjFtATh81UsbHR8Ids21E-wIgiZEPeNxfAxM-tCzlvpctLqxOMh3Xahs0hFZbEjVGYEoVrFk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لیونل مسی:
آنتونلا اجازه نمیده داخل خونه با پسرام با توپ بازی کنم. تناقض‌های زندگی همینه دیگه! من از فوتبال پول درمیارم، ولی حتی نمیتونم داخل خونه فوتبال بازی کنم.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102272" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102271">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbqTszGhruKTcBZz6spydkSXn1EGrT2HrBnYAp4ZXlIzK7RWZYh63qZGypaJUCXcQS2dF_csmkj9grrTWUOYepiaJCjEW4jJfOBGo2QjkQJvn63pQAkJngFjscd_1u-bBAdqEGmwsw41omzgXHf7optN-F3KLZlfVNiPKlxIAbyYd00eHAk5dF__X4ZvLjudSyKz5wnwx6ZHWvxpitj7X6bLcJUAF2eyEY0IgH1CeIB_mLHLxfAZtmRDcM0aWUK085gvVRxwBkKQu7UeEGV4oO1q1ICGwX_H0omMbuSl1zG6T2iZOSmtbYRwzNeGUhCYgQTOc-XP0urG_vZ8uumJBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
⚽️
نگاهی به اسکوربوردها
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102271" target="_blank">📅 19:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102270">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57a7d2d3f.mp4?token=IwvrebevZviU_2hwSbIb945foH_NEzYJWbjjQtq1m-mFQ1O4xVTVqvjxA8rGbSeHxPhdN3F_-1O9XXn6mrrocogJosl0-9j30W-_Xs59BNZtPYrK76WjCgL3dX0FnK5gkZ5eluYlX60rVXXvFiTQUwnIbzGLqwJEgdCHrG3CWtk0XuppnmN3sQvhpP4hJLavpFhNyK130ulF8d0lqBKB6uRWTvM5TBV2oo4Rqz8SLdLXsxe0Mz9xseyZDXdlTOHqoXkMRQYzgqeVl3yRm7L94I7wj3VkDgrJrZepkp53cp4OOydJCf3DVvZ9OuA_6D6gyaDTQrDu2G73TAr4rc38hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57a7d2d3f.mp4?token=IwvrebevZviU_2hwSbIb945foH_NEzYJWbjjQtq1m-mFQ1O4xVTVqvjxA8rGbSeHxPhdN3F_-1O9XXn6mrrocogJosl0-9j30W-_Xs59BNZtPYrK76WjCgL3dX0FnK5gkZ5eluYlX60rVXXvFiTQUwnIbzGLqwJEgdCHrG3CWtk0XuppnmN3sQvhpP4hJLavpFhNyK130ulF8d0lqBKB6uRWTvM5TBV2oo4Rqz8SLdLXsxe0Mz9xseyZDXdlTOHqoXkMRQYzgqeVl3yRm7L94I7wj3VkDgrJrZepkp53cp4OOydJCf3DVvZ9OuA_6D6gyaDTQrDu2G73TAr4rc38hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
دریبل‌زنی در حالت عدم تعادل (Off-Balance Dribbling) در FC 27
.
این ویژگی آن‌قدر اعصاب‌خردکن خواهد بود که ممکن است وادارتان کند بازی را وسط مسابقه ترک کنید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102270" target="_blank">📅 19:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102269">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7495121486.mp4?token=pOVTyMjPRrDfRxlgTyAbtHWZn4wJiuKECfUl3KDWnA5VyXWhToKCSXAaBwFAnddaLLFGbntyXtADcND8C5ZBwAWovOd9dorCXX1OnQrCnwxSx6EGbBqaJ59uLWtx5hBYTQUJ4UXEJS68VutkU5_E3UU2qsGaC9xizPI_w7QFPTfd9Qct13puR6gTLjrORkyUJwfymb_LqHBuRQ2k8noWUNXC1GMg1gf3HEQoaIS6yF1lFPVjp-mSWJp2Xw3Cw-PSxHeqTmDiMhNWyTsRjhL6PhBfQWU085MGor15HeXqLRRK6UyHKQJG_0DMl_dM5cT2hKZQtZMFltXZS1Ntk4ryTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7495121486.mp4?token=pOVTyMjPRrDfRxlgTyAbtHWZn4wJiuKECfUl3KDWnA5VyXWhToKCSXAaBwFAnddaLLFGbntyXtADcND8C5ZBwAWovOd9dorCXX1OnQrCnwxSx6EGbBqaJ59uLWtx5hBYTQUJ4UXEJS68VutkU5_E3UU2qsGaC9xizPI_w7QFPTfd9Qct13puR6gTLjrORkyUJwfymb_LqHBuRQ2k8noWUNXC1GMg1gf3HEQoaIS6yF1lFPVjp-mSWJp2Xw3Cw-PSxHeqTmDiMhNWyTsRjhL6PhBfQWU085MGor15HeXqLRRK6UyHKQJG_0DMl_dM5cT2hKZQtZMFltXZS1Ntk4ryTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
کرنر ها در FC 27
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102269" target="_blank">📅 19:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102268">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a87aed54.mp4?token=EniDyCjRTXaEjbweL64cza5PKlBqsiQbnI0tXBXy9mb3Vlqo2F6sRPB72nYPg7aLswPbCJ2-nRcMdenKzbL3_hD2apGG7S1ciXxYW4QJ6v-5UxK4XA8vmrQJAm0uIZUCp934eE4OffRQZw4QKTDSKuD4X3FupndNnR4_zzI1Lnk1kwcNMzSuh2mZPBrL9rkOQsqQbiNIGpt5tz5aAN5qgniHeUbaiQ1q3bNbIqstMa8Kyuc7tSegLJ-4EISevQT2C3jin_6OKVPDLJWUugvqdgEvpibYloQVpccJUZ2LdVmV_vYjFaznMjquiiiQ5C-qebFFvg9cjzsPEkFqRtRmMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a87aed54.mp4?token=EniDyCjRTXaEjbweL64cza5PKlBqsiQbnI0tXBXy9mb3Vlqo2F6sRPB72nYPg7aLswPbCJ2-nRcMdenKzbL3_hD2apGG7S1ciXxYW4QJ6v-5UxK4XA8vmrQJAm0uIZUCp934eE4OffRQZw4QKTDSKuD4X3FupndNnR4_zzI1Lnk1kwcNMzSuh2mZPBrL9rkOQsqQbiNIGpt5tz5aAN5qgniHeUbaiQ1q3bNbIqstMa8Kyuc7tSegLJ-4EISevQT2C3jin_6OKVPDLJWUugvqdgEvpibYloQVpccJUZ2LdVmV_vYjFaznMjquiiiQ5C-qebFFvg9cjzsPEkFqRtRmMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚽️
دفاع دستی در FC 27 دوباره به اوج برگشته است!
✅
‌   رهگیری‌های دستی (Manual Interceptions) بهبود یافته‌اند.
✅
‌   دفاع سایه‌ای دستی (Manual Jockey) بهبود یافته است.
✅
‌ در مقابل، قدرت تکل‌های خودکار (Auto Tackles) کاهش یافته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102268" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102267">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5128380014.mp4?token=c4JEk3q7Uj5KyS4xGPIzQX0aZOhbjqgEaTdYOnuWK_Jd8vgbeHAplfpucpA2Bfm_DV-AcRlofQ7LuJhucs5d9C0ZNYsKDTfdt5Z2WcFduyOrV4YVg1hpNPhHVUIgPgJKfzqqZYQcDxVyQFXqKgvECcyME9YW_bh3jEGNbfQs3OhH8kA-BK5PLSWuWHEqNdJDID0Bj8pN9eLNZwQVb8oNJrPEBPZyAGxYrfKoS25iVwsTQXownkwn7nQEnBq5vyAE8sxbI7ylkQ86zQx1OIvfpGLfWUDx2HV25eogUX2DEp0h_9zeh_7t-fzK_N89xhQvnQHboN4d_6zwC-D3c3YIsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5128380014.mp4?token=c4JEk3q7Uj5KyS4xGPIzQX0aZOhbjqgEaTdYOnuWK_Jd8vgbeHAplfpucpA2Bfm_DV-AcRlofQ7LuJhucs5d9C0ZNYsKDTfdt5Z2WcFduyOrV4YVg1hpNPhHVUIgPgJKfzqqZYQcDxVyQFXqKgvECcyME9YW_bh3jEGNbfQs3OhH8kA-BK5PLSWuWHEqNdJDID0Bj8pN9eLNZwQVb8oNJrPEBPZyAGxYrfKoS25iVwsTQXownkwn7nQEnBq5vyAE8sxbI7ylkQ86zQx1OIvfpGLfWUDx2HV25eogUX2DEp0h_9zeh_7t-fzK_N89xhQvnQHboN4d_6zwC-D3c3YIsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🔥
⚽️
#
فوووووووووری
و
#رسسسسسمی
: تررریلرررر گیم پلی FC 27 منتششششر شدددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102267" target="_blank">📅 19:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102266">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a8d0459b3.mp4?token=EvQUHJovoEeVt9s_YhP14hNWM7olpxTOyDqeLEvQZHzVAUdvlwtxQbKLr0h8EAqpI4j1k1cOzHdYwAWONTcwL533u8sDsa5l-jfa9-e8nVrOdAsUhPSSwPJ7FKsr5rdt_gLE5c6jTB5sRH08CHgoBNHcnoLs4KeivEKv_A-NS29IKV_GLNPZEcmTeI36e1ibYGSYAcKpDMJtOwv2slBLEalbkwB2FatScD3V4kwpw7SNZmDpagnm0bAZzr2x4oTHKIQQSF5Iix45szyll29-eN9QD8cE94-6JIUdSXblM-zvqRNCHk4EAAizZ25LtUmSdzctg1zrLvoPlvAe-7Khi4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a8d0459b3.mp4?token=EvQUHJovoEeVt9s_YhP14hNWM7olpxTOyDqeLEvQZHzVAUdvlwtxQbKLr0h8EAqpI4j1k1cOzHdYwAWONTcwL533u8sDsa5l-jfa9-e8nVrOdAsUhPSSwPJ7FKsr5rdt_gLE5c6jTB5sRH08CHgoBNHcnoLs4KeivEKv_A-NS29IKV_GLNPZEcmTeI36e1ibYGSYAcKpDMJtOwv2slBLEalbkwB2FatScD3V4kwpw7SNZmDpagnm0bAZzr2x4oTHKIQQSF5Iix45szyll29-eN9QD8cE94-6JIUdSXblM-zvqRNCHk4EAAizZ25LtUmSdzctg1zrLvoPlvAe-7Khi4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت جالب مجید «قصه‌های مجید»:
وقتی ۱۵ ساله که بودم، تنها از اصفهان به تهران می‌رفتم تا بازی‌های آسیایی تنها تیم دو ستاره فوتبال ایران (استقلال) را ببینم. در ورزشگاه یک سرود می‌خواندیم که آن زمان غیرمجاز بود و البته خیلی کیف می‌داد؛ آهنگ تنگ غروب سیاوش قمیشی…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102266" target="_blank">📅 19:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102265">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALFpusfkqhS16RHYdF-9BX5WjbXwe2FopnxYuKyfbnE-aSh8RIxa1e_IYpPmFgmiSAimEXWW0xq46Lf-CZRLNnenyLisPH_YPqEDiZv4ZGWxsNwjo0quTtz7xmRBHd9yFp1x-ngyyVpCVHkWHA1UtnlAnfn6dBCpAxglA1p5GjTJazvluNbuEGuODsLpwugDRDDSbIjKcOp4FnkuIssvGj0bgRP1mqpYO4JTehiIW_8PYbI6tLAv98E5_MnLSLTR8apWYHOuFgdGZ8zTJDEBlZ9ixO4cquLKPlZO5qjyNJhR68bfA4EBHoYuQBWTRLrRvqZddUxwzYiEJtFsaV6ktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🟢
تلاش‌های علیرضا دبیر برای حضور نکونام در پیکان هم جواب نداد و ساکت‌الهامی سرمربی این تیم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102265" target="_blank">📅 19:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102264">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bcb41b861.mp4?token=cEuv9crRk7QwiYWOyqdux6KeO7eKSZGND2AvAi1ESq6n4yiS2fgfUWobgUJ0YiE51KYP0eN8eSZyfFid-iTqGvy9Cp84UjVcNeTd0PCdFpN9XhYR9UfHYbWzxKUzYEh9H1EUeHmOTT7gFdXcj94eZdWk_g-tVbLzR22ZqQN4mVI_6yaqwgYp9X4Rr770iX8PFSplC5SQLv1iZE5hWJZFWIAyq_PTerSaAX__L74AQUoPvhPsXO44UX80eGKdyCZqm-twzExgg9ngc8DLiSCyk0R49SPF-HyYbRJsylu1ClwdzO-LTNl3W0U8rlzqFJ6948yIZlfQzVMW1K5EBu6lkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bcb41b861.mp4?token=cEuv9crRk7QwiYWOyqdux6KeO7eKSZGND2AvAi1ESq6n4yiS2fgfUWobgUJ0YiE51KYP0eN8eSZyfFid-iTqGvy9Cp84UjVcNeTd0PCdFpN9XhYR9UfHYbWzxKUzYEh9H1EUeHmOTT7gFdXcj94eZdWk_g-tVbLzR22ZqQN4mVI_6yaqwgYp9X4Rr770iX8PFSplC5SQLv1iZE5hWJZFWIAyq_PTerSaAX__L74AQUoPvhPsXO44UX80eGKdyCZqm-twzExgg9ngc8DLiSCyk0R49SPF-HyYbRJsylu1ClwdzO-LTNl3W0U8rlzqFJ6948yIZlfQzVMW1K5EBu6lkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔻
داستان پسری که دنیا او را به حال خود رها کرد، تراژدی تلخ زندگی ماریو بالوتلی
🔺
ماریو بالوتلی در ۳ سالگی به دلیل مشکلات مالی از خانواده بیولوژیکی‌اش جدا شد و توسط یک خانواده ایتالیایی بزرگ شد. اما کودکی سختی داشت و به خاطر رنگ پوستش در مدرسه مورد تمسخر قرار می‌گرفت؛ حتی مدتی فکر می‌کرد با شستن دست‌هایش می‌تواند رنگ پوستش را تغییر دهد.
🔺
سال‌ها بعد همان کودک تبدیل به ستاره‌ای بزرگ شد و به اینتر میلان رسید. اما وقتی مشهور شد، خانواده بیولوژیکی‌اش دوباره سراغش آمدند و ادعا کردند می‌خواهند رابطه‌شان را شروع کنند.
🔺
بالوتلی با ناراحتی گفت: «وقتی هیچ‌کس نبودم، کجا بودید؟ حالا که معروف شده‌ام، همه یادشان افتاده من پسرشان هستم.» داستان او، روایت پسری است که با طرد شدن و تبعیض جنگید و دردهایش را به انگیزه‌ای برای موفقیت تبدیل کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102264" target="_blank">📅 19:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102259">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9pEDN9Zi9HRiIZM2gElDM0ECUpu59RGwwr5IBS6un-ACM6Fxy6F2FQu0uDltJtWBLI4MBCKBb5GZQFB59t-Uoq_AIYmrTnpYEh3edoTIA9SI_Ztv3CzXNgbpVMPR_c91oy_zWxcLUbArhIKeQCgvh6nMvOBBG3UJBt7h3pdRL5E73pNgzlJ-elK2__hSp9amrn5R9es9EGD1tzsEWnwpcRx5u79jGGUf0axMegfGAOP0y9P95CyehxyJD__7LvjHq_CO94Bzr3m2XfxCZUGxSJmSRzNoB0NcsTCrpMJ4UOqgznzHswMMPpaSI6RklXx56AYMZvLxWyChoWTlUCVrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
می‌دونستید؟
چلسی در سال ۲۰۱۴ با ژوزه مورینیو به جذب لیونل مسی نزدیک شده بود. گفته میشه آبی‌ها آماده پرداخت ۲۵۰ میلیون یورو بودن و حتی با اطرافیان و وکلای مسی مذاکره کردن تا او رو به لیگ برتر بیارن.
اما مسی و خانواده‌اش تصمیم گرفتن در بارسلونا بمونن، چون این باشگاه برای او چیزی فراتر از فوتبال بود. تلاش رومن آبراموویچ هم در نهایت بی‌نتیجه موند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102259" target="_blank">📅 18:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102258">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b74b82c7.mp4?token=CUhNsuZPBSAIoP5RDLbCVfGHGse8a8lA6-STNq9ZaryTjmIAKabw3ZEV-CjoiBJiO0Qz1obQLwA8j6PLaD-Oqq7oaCiZkmRg053k3cccO1Yz1dbhqOx1N8pMZVyd2wiQusNc-A020GaJCSQcMgWyvseIJoyrWBRpke_d5t84SQAsIjA2PFcx1evqD-fYQC3M_BkmAW8z1vaz6YyANA7cZROLvje-a7-5fA3j4KxI6baxNekuMWJxecJ9UbKNeYkiDd_VtfIBZxMXGD_WXFq04QJKnNnsU-VvpYHJyqD1mMa4gh-iNN9N-Uvj80fnYQg73aRU9mFAhKQYNwErDS0CRlgIG8ktH9YsYJGA7b3tNZ3DprUvu41IXcvwWWzr6LoXOKizhHMEjtK5yrMtAEDsxRAH8uMCdnC4i1x14XItMoyQV4ZyjODt2PrkUieSQO_CnLlh-Hi_doGSKhELebVTgLyJd3sDyf-BpufuxdeY3zcd7Du6x7xV4FzHpUFjo7KNv-2Kf_yqiCyl1U0Kv8ipks6mL3ofUujuPpxqjxd2sTtfs39XTN7EfMCEu9QlWPGW9St2yLWJbyD3AUhn55A6AtVQFdeoHe38gJG4YpE_riBHTiTR_XOZykMqMO2ooc846tOckY7NarHyUv1MmmwoZTidd5vaHRzC5Q-O0dpD2EU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b74b82c7.mp4?token=CUhNsuZPBSAIoP5RDLbCVfGHGse8a8lA6-STNq9ZaryTjmIAKabw3ZEV-CjoiBJiO0Qz1obQLwA8j6PLaD-Oqq7oaCiZkmRg053k3cccO1Yz1dbhqOx1N8pMZVyd2wiQusNc-A020GaJCSQcMgWyvseIJoyrWBRpke_d5t84SQAsIjA2PFcx1evqD-fYQC3M_BkmAW8z1vaz6YyANA7cZROLvje-a7-5fA3j4KxI6baxNekuMWJxecJ9UbKNeYkiDd_VtfIBZxMXGD_WXFq04QJKnNnsU-VvpYHJyqD1mMa4gh-iNN9N-Uvj80fnYQg73aRU9mFAhKQYNwErDS0CRlgIG8ktH9YsYJGA7b3tNZ3DprUvu41IXcvwWWzr6LoXOKizhHMEjtK5yrMtAEDsxRAH8uMCdnC4i1x14XItMoyQV4ZyjODt2PrkUieSQO_CnLlh-Hi_doGSKhELebVTgLyJd3sDyf-BpufuxdeY3zcd7Du6x7xV4FzHpUFjo7KNv-2Kf_yqiCyl1U0Kv8ipks6mL3ofUujuPpxqjxd2sTtfs39XTN7EfMCEu9QlWPGW9St2yLWJbyD3AUhn55A6AtVQFdeoHe38gJG4YpE_riBHTiTR_XOZykMqMO2ooc846tOckY7NarHyUv1MmmwoZTidd5vaHRzC5Q-O0dpD2EU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔴
۱۰ گل منتخب تاریخ تیم منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102258" target="_blank">📅 18:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102257">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLH0vlTCtt74XZlVDittRdo8jrrHlQrXzovUKWKPWjBfLLuNtz1dzp7G6FvIj-eb4mzm8goPZxXMJQKAazHrl4iL9wrducLyG-7YFzoFLf0BY7kzWlXyIKDN_I4ravn38yanfoeDtmWVACDLk97E6DkTZRpRiLnUEkgfUS5TSnYhvhQGk6PZAW6egTB4Bsg7xhvPi4tgReSiZP6VEVVz_l3N8knvUZgFUK0VGejJYf8UZdfDJGqO9RVKreEdUjJQ1ApYJp_JxiLymqQ5VvLuBLq53i63GmVY3vcjmHjnRwbFpLC4tOFSRO6SB4NuaYnxydHVRq7LohOVm_1Na2dziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⚫️
#فوووووری
؛ فلوریان پلتنبرگ: کریم آلبگوویچ ستاره تیم بایرلورکوزن با عقد قراردادی به ارزش ۳۳ میلیون یورو راهی یوونتوس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102257" target="_blank">📅 17:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102256">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaXOkvTu63fngdcMM_xTQMzbwcsF8ZoF4ivj8Lu9AmKqJ-SVph5PY9bnWtzmccZT7UTMHITnvjTdUB2BFXK3uGdPsTpxnIGAGqqxxCcJ1Dvwsw_zI-QwoziFeBmDhFkVQxkkcKZVTBu6qgNjKI6WvRlaJWydLJT6G0HE4pZGNux7HNz-a7ewKuo9US95NRaml6WoR0hiTRIz3WEpNqwSxNW0K_PCHbW-mP7JfYlAODa-NMzB9RqHRJXwfGVgHrV1yIJJhMob1HrnkXbaHPfCSyi9kfnXhBWlsiQVITe4dFPDLicJ3hZeBH2RQlZjgEuVH9GnDpaMJU7U8QpxQJvEmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
رونمایی‌رسمی از لوگوی جدید فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102256" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102255">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qErXcoTLANmqxBBWHQpuV3P028prtp6qLYy8zvrSKB7xVgNJwBtFl9el15ny2Agv0HO-e4U2WahZWAQRBxiU810naDWOw6bvLm4TdlcwB-R5uiuewox_J2jVvnP8oyat2FcFq_zWSWeYKMcyyFM72Kg1_SgHQcbskndtz4MSJf7SAigy-CA0IM9VfEqnJMz6cADJE5opsWHZhfldpWI_XVYVC44u_QdSJdBr5Ze_ic3uEupKcXfSRz6fMVU8BtLW56SDK7kTImYDEQpt-V_2JnRtXDCk4_pSTGTBhXfEErx-DFMaVn2CLysdzUWvKdtnVdF9TBGwz7hU9gdf1ZyZCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚽️
مارتن زیگلر - تایمز اسپورت
🔻
جیانی اینفانتینو، رئیس فدراسیون بین‌المللی فوتبال (فیفا)، قصد دارد بخشی از حقوق مسابقات جام جهانی را به سرمایه‌گذاران بخش خصوصی بفروشد.
🔻
مذاکرات با سرمایه‌گذاران و چهره‌های نزدیک به دولت رئیس‌جمهور آمریکا، دونالد ترامپ،…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102255" target="_blank">📅 17:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102254">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d715de39.mp4?token=u09rJruljSEHI2rsRrUPsCfLxHW-59mhrG9nLL4dwhBSs47fx9X0Z3sil2QhjFoq6TwipJjgJdlDSbQ993fzoQQtQuvgaDtOyqVx1KSjzWZZ5Ay8ZErwLosYruLb1iR7Detdl0oz7pWDMDcyHvRaGt88eXpO-HOl4Im4b1A2iZap2XYcxCoN3l-8B24mb7sf9VmySHQIzKnpAVFZub5fP4s7FrIvLMoOtMpTzmG51Y04gY0CeXDFOe_u-Y8x3CkuOB44kKJ-ZfKrFqc4bMDNBr24uC6hceDjVQ6KoBfqbnM-rzS-itjKva2xIUwZ3P4oVqZqWwQKVMHjSDfFvKStkoLnhkAID5pMS9v5iZ5uYf1ITPjPGoGnxbwqMw68ZO3Y6cEKaAR_CytiaGptPO0m6GUaP-LoxxF-RBaukNWpab997LBWHMNaNSLZElN0ZLR4qxroWoOECn-uK5Rvx_6OaDJnZ-rXh6BlojqyWHH_Jo9NH9jeuf1QROp0Mz1918UiD2PvcA7O9UCkerMs34Bc4MX3wIBa6NlcRqI83zmk0iwRVwei51HG3_B_RYncsKsMkKKfIMiFeYLKfyJOmPrMT3SmmfM2TaFY4G5B9_CYwF_1EcFfI8g4EeRobJqbP_BiUqCWlkG-lqSP14NNejBLqfG8oEtd1KPS6JPFS4MJWeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d715de39.mp4?token=u09rJruljSEHI2rsRrUPsCfLxHW-59mhrG9nLL4dwhBSs47fx9X0Z3sil2QhjFoq6TwipJjgJdlDSbQ993fzoQQtQuvgaDtOyqVx1KSjzWZZ5Ay8ZErwLosYruLb1iR7Detdl0oz7pWDMDcyHvRaGt88eXpO-HOl4Im4b1A2iZap2XYcxCoN3l-8B24mb7sf9VmySHQIzKnpAVFZub5fP4s7FrIvLMoOtMpTzmG51Y04gY0CeXDFOe_u-Y8x3CkuOB44kKJ-ZfKrFqc4bMDNBr24uC6hceDjVQ6KoBfqbnM-rzS-itjKva2xIUwZ3P4oVqZqWwQKVMHjSDfFvKStkoLnhkAID5pMS9v5iZ5uYf1ITPjPGoGnxbwqMw68ZO3Y6cEKaAR_CytiaGptPO0m6GUaP-LoxxF-RBaukNWpab997LBWHMNaNSLZElN0ZLR4qxroWoOECn-uK5Rvx_6OaDJnZ-rXh6BlojqyWHH_Jo9NH9jeuf1QROp0Mz1918UiD2PvcA7O9UCkerMs34Bc4MX3wIBa6NlcRqI83zmk0iwRVwei51HG3_B_RYncsKsMkKKfIMiFeYLKfyJOmPrMT3SmmfM2TaFY4G5B9_CYwF_1EcFfI8g4EeRobJqbP_BiUqCWlkG-lqSP14NNejBLqfG8oEtd1KPS6JPFS4MJWeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
تعریف ژیلا صادقی مجری صداوسیما از بازی پژمان در عشق ابدی !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102254" target="_blank">📅 17:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102253">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkwZHE4IK-tosQtkmuXrA60s1FoxjccGyT25oTN6VLiGVbvIrs9J3jiHepZ1AyT8rgM3ow3kWKO92XYTqq9D31O9bExB9m_mRYzPjiP1FOi_gdOtTym6r_DQG5Ygg0bYzUalPDpWH5p7gG2xMFUorAXVPQFeEg6GZN-Mbi_jNiR9JdKghwSmzHbgC_f1K0pZtQWLtqpE4pLVAUyiNzTZ-TQQxZ6umv8IBSHvifaP_L1WhlWbOS2GwAF1UEKTHP8dmC_jS9YEqTy4mJjK0U7Lhf33IOhu9JjGbVxwJloWoju1qsPEr6YKFqmojvmQ4K494mdjtpQrcG_s731Ww4HHoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از فلیکس‌دیاز: رئال‌مادرید به احتمال فراوان معامله رودری رو فردا نهایی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102253" target="_blank">📅 17:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102252">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRjIJ1jphL5cj83AGn2TSXn9blCWyQtRH5ERWFkELLoxXklkZrdbpYYPSF8EAD-Rfr9LeWp1dSv4IDo3uf6D0pFp2DaKgqJQ2Hh3u_IcfUrF_Sp0-bla9c8xp2GIrTYHMVvSvwzOliZpw-fNQrpbP2_eBbcFwNKFYnxNmfE6Z9KKnc0RF-OG7_bYTs2G99hToq5OY2vcyL7LxqyPeLGMQ5rZbU3L3U6T-97fPLd7uukwZp3QQBeYAVSTk97DTUaFM8RR4kwXtcLJt8nzjnEv82AlzDm7EtnPi0uOnzEZJCrWhkQRYprcLkyGdvJu99hTQ9JtHobi5tEpdV2N-BnT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
ساسا تافولیری:
بوعدی با منچستر سیتی به توافق رسیده است و قراردادی تا سال 2031 امضا خواهد کرد.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
🇫🇷
لیل امیدوار است که 100 میلیون یورو از این انتقال به دست آورد، در حالی که منچستر سیتی می‌خواهد این انتقال را با 90 میلیون یورو به پایان برساند.
💰
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102252" target="_blank">📅 17:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102251">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTPdY2MZZtpZL9mt6iY7NYc2GA5RIkhGG5DRwgRrXBCdnwvqgFFPtI_2dINaAh7S3MFwygjex9Wz4vKdkvBM1qizkKEY1roKata5Yt7vR9CtZTtLyiQI6B5Qw9SH4ewBpDXlzIdc-f2Ltcy3zHpXPbVS0kLpY0N0hvBMGbBB715pENz4PrfOhGlomBMs4XnuCo5IZDUjAY4Eieo1VmflPMeKovfmKeq4nWV9Neaa3nRiNiwZrppTxo7EJDzl-fEoOUPCyyHCIISKRLPsJd4xRE4RvJPy1oQTyeMcUE-IQWXmp2GUli09tWVUsuhckO3PIEj7v82w1tXPz2xAxTOa-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: جردن هندرسون با عقد قراردادی به مدت دو فصل راهی چلسی میشه
HERE WE GO
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102251" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102250">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb71ce498.mp4?token=TVazMfXwRi1BWinO-YTPE-rDK8ZnrmiBIJ_yduFWhSQNyK7yAMhSXqorhuobqyHObPb7ZD8VpxDD_NcAvYSRlO4eYuysoCG9MjGOPYVHc8N7wnRKy9PtRPzGFPunweedBt1zdq31xmutmOgKimjmhmIxBpdNmY8Bki1xYwkUFv7DBXg50tjPWL3vGZvS9NkrRidR7kgzFYKf1WIf7Hy7PfxZAGIJuId2OWVXqeFc1Ig9aP33h52Cupc-MgwtyeGXCh3ezeXFtzGyAxL0DE_51n_T9I4RBRroD3Qhg3_qINR8ljszyazlSXoFJBRWkE7H7ghoan7RsB4F4MJx_I4UUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb71ce498.mp4?token=TVazMfXwRi1BWinO-YTPE-rDK8ZnrmiBIJ_yduFWhSQNyK7yAMhSXqorhuobqyHObPb7ZD8VpxDD_NcAvYSRlO4eYuysoCG9MjGOPYVHc8N7wnRKy9PtRPzGFPunweedBt1zdq31xmutmOgKimjmhmIxBpdNmY8Bki1xYwkUFv7DBXg50tjPWL3vGZvS9NkrRidR7kgzFYKf1WIf7Hy7PfxZAGIJuId2OWVXqeFc1Ig9aP33h52Cupc-MgwtyeGXCh3ezeXFtzGyAxL0DE_51n_T9I4RBRroD3Qhg3_qINR8ljszyazlSXoFJBRWkE7H7ghoan7RsB4F4MJx_I4UUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
لامین‌یامال و زیدش در تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102250" target="_blank">📅 16:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102249">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ebe18939.mp4?token=PBFw6_dS23xRS5SL0bd_3A54vGe-F7jta12zClUg_pbJbwjGoe5Kk_Am70mH2_iocV_-fbUCVXsEWXNxKjMx2N82FwyRhnF-An8ZlnLoYOTP4M5nX8sPRxUNLSuc5-9UZytAC9g_WiALUzBdEO62nyjObWLaGC359QPdspkE2ySrHgtVkyHufbNj6Aebsi-h19pxF5ievdk7eZNZ26pmbA5XA3xmw38jkl-RPw97Tn1FbPq4Pm7xIsT1V2VGyekYmHkWh3ikAloGoVwfubp29Ejg4yfZNW8DqIQ0zgkIF_xdjUM4iPPgamYFNb35Q6_oAtQ5JzmhzbyQAGLqwjms_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ebe18939.mp4?token=PBFw6_dS23xRS5SL0bd_3A54vGe-F7jta12zClUg_pbJbwjGoe5Kk_Am70mH2_iocV_-fbUCVXsEWXNxKjMx2N82FwyRhnF-An8ZlnLoYOTP4M5nX8sPRxUNLSuc5-9UZytAC9g_WiALUzBdEO62nyjObWLaGC359QPdspkE2ySrHgtVkyHufbNj6Aebsi-h19pxF5ievdk7eZNZ26pmbA5XA3xmw38jkl-RPw97Tn1FbPq4Pm7xIsT1V2VGyekYmHkWh3ikAloGoVwfubp29Ejg4yfZNW8DqIQ0zgkIF_xdjUM4iPPgamYFNb35Q6_oAtQ5JzmhzbyQAGLqwjms_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ نادان وسط مراسم ختم گراهام آدامس در میاره به بغل دستیاش تعارف میزنه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102249" target="_blank">📅 16:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102248">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2CJHMFO5SnTNTjJJdpbOu6lfh6VvIrpq71LeGQLYhdEyMsHayErcnDeECfLYJ8lbx2j1yNKpDIu2xJaha42N9EsPWVRinl6qiP1GUYmoPZA5adNVobNn_RuBNJ3Kpyko1wdbbLye3jYRgkfXaWkpgZhwBepVHbZASCtadIKPmSfLAFSvLucRF2zDUnYoxPrzTZVu_MI3xvY2rh6nkP6DG-Lm0RoagKePe6-jbTYGoxrDivXZEZ3tr7fM4eKmbWzK3YGAWygZXtY0WFroDk3ZJCHC_k9vogpWmh9H3WfjVNitnRjXTrna3e95k0wE3reZgPRh_Ed0XsCOdd14BR8wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔹
رئیس باشگاه الاتحاد فاش کرد که بعد از جدایی لیونل مسی از پاری‌سن‌ژرمن، این باشگاه یک پیشنهاد تاریخی به او داده بود:
ما ۱.۵ میلیارد یورو به مسی پیشنهاد دادیم، اما او این پیشنهاد را رد کرد چون خانواده‌اش می‌خواستند در میامی زندگی کنند.
چیزی که بیشتر از همه ما را غافلگیر کرد این بود که حتی یک لحظه هم برای تصمیمش تردید نکرد. میتوانست خانواده‌اش را راضی کند، اما خانواده‌اش را به پول ترجیح داد. ما کاملا به تصمیمش احترام می‌گذاریم. خانواده همیشه از هر مبلغی مهم‌تر است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102248" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102247">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
ترامپ در مورد حمله ایران به اردن: حملات شدیدی به ایران انجام خواهد شد، آنها شکست خواهند خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102247" target="_blank">📅 15:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102246">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2de7978a2.mp4?token=O80otsf02JwnK62JiLwLYCyrxnylkArnx7ASckxkBpIUsfBFsAjsoJveDVidIvAOQWhLVCI6-2dH67u6qFGj0oOLnt1JsBWep6y3bXG8l9TWBy3ubGXrG0D9lJYNWwNHay1wOdSbaTEscFvkq43FS7ns_QMkNYjPZzT38kl3LXWQ0cJYuikAKrp8uDVIKkF5Q2k7tKhvo7j4VnHpQCMtn1UNvFyiVy-mIfdIl8R8vlpCWFG8lpPBK-ENn4EqXfoXpfanBeiCQc3liKkeoWh6t9zw9b4qgKPyswCon0jwndxLg1zfjmPwxfTnTWLZGmcvvcviMw1WFHeImAChN2vj_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2de7978a2.mp4?token=O80otsf02JwnK62JiLwLYCyrxnylkArnx7ASckxkBpIUsfBFsAjsoJveDVidIvAOQWhLVCI6-2dH67u6qFGj0oOLnt1JsBWep6y3bXG8l9TWBy3ubGXrG0D9lJYNWwNHay1wOdSbaTEscFvkq43FS7ns_QMkNYjPZzT38kl3LXWQ0cJYuikAKrp8uDVIKkF5Q2k7tKhvo7j4VnHpQCMtn1UNvFyiVy-mIfdIl8R8vlpCWFG8lpPBK-ENn4EqXfoXpfanBeiCQc3liKkeoWh6t9zw9b4qgKPyswCon0jwndxLg1zfjmPwxfTnTWLZGmcvvcviMw1WFHeImAChN2vj_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✔️
🔥
هادی ساعی در المپیک 2004
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102246" target="_blank">📅 15:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102245">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33130fd550.mp4?token=QPG19AOf23FWaq3QuEd0JfzdtiDhcDzl3FsjQrhSynBhl0TJYoQTRe6Cg98bq9SyXgaac1NzjXIl-KYO2YmhCbzogXn9rDDyQ5htetEfmVqxBojTMENc1bGWvtghrUb8cfkn1fRUsYGyoiOvqB4CCbuILbGdUwJBx6DEOguyNbqwrCDhOTo0H91QpVvDh57d0B0J9FJ2u9Mot2rxZ2eBW-xMC2VtTk5geFGEbiRd4PCas2FjeMrD6g66z1qbSEg7Pp5hLKIuas6wMmDhvmGv378gR4KIiEuE1BPaxGPUfVxxcc0nx6woy5p9HN1En13YsvZKUltDBp97rzz8xjToF5lDlFuGn0QmIGyMWGcBh2VBSn7dIJaX0BWyqKGibbH8-lM_nbHUhLSoytQkTsT7Ih5VQK8Gst8Nl9fsKHw6Dxa9qMORfeHrSdKm3k0zsjlvnnGAnqDTEGzkoOnqXuoqfLpRRRfUM6BAKrR9SAZat_8A9WmowKYfubr-cx4ZUD6Xs4m6gUxuJzvwQBUxcZfiJqdkM1mVkpqy7tVUEG87BDzsgaNBdKjrF8_73wkqcwDv-bWM5l_jMDWF25g0aKx91Qykv5OVfZjJqy7GvAemyNxeM4pC-A-WU4eWxAEWx1uYv-o0Wo1WV4CsBe6sPLWBiVLAeYjQsjMwVTQ6EO5XBjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33130fd550.mp4?token=QPG19AOf23FWaq3QuEd0JfzdtiDhcDzl3FsjQrhSynBhl0TJYoQTRe6Cg98bq9SyXgaac1NzjXIl-KYO2YmhCbzogXn9rDDyQ5htetEfmVqxBojTMENc1bGWvtghrUb8cfkn1fRUsYGyoiOvqB4CCbuILbGdUwJBx6DEOguyNbqwrCDhOTo0H91QpVvDh57d0B0J9FJ2u9Mot2rxZ2eBW-xMC2VtTk5geFGEbiRd4PCas2FjeMrD6g66z1qbSEg7Pp5hLKIuas6wMmDhvmGv378gR4KIiEuE1BPaxGPUfVxxcc0nx6woy5p9HN1En13YsvZKUltDBp97rzz8xjToF5lDlFuGn0QmIGyMWGcBh2VBSn7dIJaX0BWyqKGibbH8-lM_nbHUhLSoytQkTsT7Ih5VQK8Gst8Nl9fsKHw6Dxa9qMORfeHrSdKm3k0zsjlvnnGAnqDTEGzkoOnqXuoqfLpRRRfUM6BAKrR9SAZat_8A9WmowKYfubr-cx4ZUD6Xs4m6gUxuJzvwQBUxcZfiJqdkM1mVkpqy7tVUEG87BDzsgaNBdKjrF8_73wkqcwDv-bWM5l_jMDWF25g0aKx91Qykv5OVfZjJqy7GvAemyNxeM4pC-A-WU4eWxAEWx1uYv-o0Wo1WV4CsBe6sPLWBiVLAeYjQsjMwVTQ6EO5XBjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
احترام به هواداران به سبک لبرون جیمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102245" target="_blank">📅 15:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102244">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34dd03fd29.mp4?token=cmIDKzMzDhGiiwuaU9XSfvRpMcf8kpQnEFHolg2i7WMkDRUHiHuQiiVUVxV-GsM4Ib2MX0zj3bQj5MuNCXv-5NURjY8lOPYojjSN6QGU9KjSj5j_apbb-BfTR_ZrNAw8cIwPms4YVrR-d7hNWBXJtRHVbZVMmd9FYfJ2uSZ-gqmBFYVV0ofNr5FKKYG-U4_f3OudVy6ryhPMR3cAB4km01EPF13Sf-G5AwcQl4qLzraxZ-7VtjyECyJ7ALrhktXacbsT5lBUgk6s_Uj9Iqarnxrez2p35xKOoFCLYyQF0hSG6pGwgAXz88fVEjn9GHVoc9GWUvhQeSs0bzS9AuRgDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34dd03fd29.mp4?token=cmIDKzMzDhGiiwuaU9XSfvRpMcf8kpQnEFHolg2i7WMkDRUHiHuQiiVUVxV-GsM4Ib2MX0zj3bQj5MuNCXv-5NURjY8lOPYojjSN6QGU9KjSj5j_apbb-BfTR_ZrNAw8cIwPms4YVrR-d7hNWBXJtRHVbZVMmd9FYfJ2uSZ-gqmBFYVV0ofNr5FKKYG-U4_f3OudVy6ryhPMR3cAB4km01EPF13Sf-G5AwcQl4qLzraxZ-7VtjyECyJ7ALrhktXacbsT5lBUgk6s_Uj9Iqarnxrez2p35xKOoFCLYyQF0hSG6pGwgAXz88fVEjn9GHVoc9GWUvhQeSs0bzS9AuRgDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
یادی‌کنیم از تیزر تبلیغاتی با مسابقه رونالدو و‌ بوگاتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102244" target="_blank">📅 15:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102243">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a4c493f3d.mp4?token=tWpy69RBjWbXom7dsOGoEYDmO7tIlPKTFAW88gIdYH2gpDkWfJovoJe3VOp2iBWo-JViu1xoyDEYQom-tBIloApdWdeFYgwfs-24bXO-lUcWktgKV1dg60HydQNzUsUexGa1jhP284wgjoYSi6vyS535nOnJLBL8eVZKfe_6CQ1Qv5hK5vb_cYgZF_KH1Kyd77Q5Zari8G3ykOV_tGjXD1H9ggCPp0Z1-XL4WBYqYoYqhoBYkD96aKmay5JHQr4brDychxPzqQ1FlfyTQUQaXxUXnd6nzquB2nZQuKIuBPAiVLuz37vv08wuvU3BcZnErG37iVeXAA-IqZYCBAvj3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a4c493f3d.mp4?token=tWpy69RBjWbXom7dsOGoEYDmO7tIlPKTFAW88gIdYH2gpDkWfJovoJe3VOp2iBWo-JViu1xoyDEYQom-tBIloApdWdeFYgwfs-24bXO-lUcWktgKV1dg60HydQNzUsUexGa1jhP284wgjoYSi6vyS535nOnJLBL8eVZKfe_6CQ1Qv5hK5vb_cYgZF_KH1Kyd77Q5Zari8G3ykOV_tGjXD1H9ggCPp0Z1-XL4WBYqYoYqhoBYkD96aKmay5JHQr4brDychxPzqQ1FlfyTQUQaXxUXnd6nzquB2nZQuKIuBPAiVLuz37vv08wuvU3BcZnErG37iVeXAA-IqZYCBAvj3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
▶️
یادی‌کنیم از مصاحبه سمی محمود فکری
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102243" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102242">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ed8d40d9.mp4?token=G4xpAILS_4O-PeaEnMpH1oWU1-ge9xBOqkmhkJsi4eDtPsu2K4BEV8q5PAJxAWZuYhCH7gerLq1MC_n47o7wbHZdYvTPofzFOWS7y7_BwlHxorajG74mNSpqhbPSVXn5-66pnI6erxxW9bnrQEht-0Pf1yuKQHyTvw809wKiw8sgaeibKQLHhp-SVezuh5W76VOsAjS_SC-uxQp8Vq1f8hezpGVJ8mkKphIjJhSKJTocBbp4DectrinF4Bb2QRvo9Gy8fUihzcj-izqPX-6seMbYd47snKM5puMD1EYo-bhwePdluBvsI-x8Qu_2K9aw8gsgZc-6n9qG-gGSc1d5N4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ed8d40d9.mp4?token=G4xpAILS_4O-PeaEnMpH1oWU1-ge9xBOqkmhkJsi4eDtPsu2K4BEV8q5PAJxAWZuYhCH7gerLq1MC_n47o7wbHZdYvTPofzFOWS7y7_BwlHxorajG74mNSpqhbPSVXn5-66pnI6erxxW9bnrQEht-0Pf1yuKQHyTvw809wKiw8sgaeibKQLHhp-SVezuh5W76VOsAjS_SC-uxQp8Vq1f8hezpGVJ8mkKphIjJhSKJTocBbp4DectrinF4Bb2QRvo9Gy8fUihzcj-izqPX-6seMbYd47snKM5puMD1EYo-bhwePdluBvsI-x8Qu_2K9aw8gsgZc-6n9qG-gGSc1d5N4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوازده‌سال پیش در چنین روزی اوریگی زننده گل تاریخی لیورپول به بارسلونا، به جمع لک‌لک ها پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102242" target="_blank">📅 14:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102241">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9073a1aea.mp4?token=hKtmWR0wHyAshsQdFGtDTzm06a5txOUn88b2oqRfIrDVPRxcgykxRu5frxzv9c67GTzKxeTn5W1DKmBDEsfIabP4pspsh3RE7aJ4Nmv-rJXgvJo8ZgVnWrmfbggCHjhwgJXaUgbaEtVCpNzeWTFmZI7XBkEJUZTH_IZag0XbAFuoIyvX7Uihf7U7k8rS6LJ_l-1v7LJAhQ-zAOa85Wib2UD0ElXIohwLFxVOqWJWL9sUqyq_6tAvOZKYFEK26fW6JACQyg_iks07ApdQxNWp-xlMQ0tUy2WDwHn8leFtwj3IZxYeWzzOjDB4_dzsH7ZZ9gu--gNDSPWkAAxQcpjpHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9073a1aea.mp4?token=hKtmWR0wHyAshsQdFGtDTzm06a5txOUn88b2oqRfIrDVPRxcgykxRu5frxzv9c67GTzKxeTn5W1DKmBDEsfIabP4pspsh3RE7aJ4Nmv-rJXgvJo8ZgVnWrmfbggCHjhwgJXaUgbaEtVCpNzeWTFmZI7XBkEJUZTH_IZag0XbAFuoIyvX7Uihf7U7k8rS6LJ_l-1v7LJAhQ-zAOa85Wib2UD0ElXIohwLFxVOqWJWL9sUqyq_6tAvOZKYFEK26fW6JACQyg_iks07ApdQxNWp-xlMQ0tUy2WDwHn8leFtwj3IZxYeWzzOjDB4_dzsH7ZZ9gu--gNDSPWkAAxQcpjpHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو انگیزشی با روایتی‌از زندگی مایکل جردن
💚
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102241" target="_blank">📅 14:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102240">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2AdH9ojHTaNrMBckq5WI3UZYVfOtcYAMJ2f8cDwJsb2CV3H_L4qxzPHTu23Q3eLNsI-qOqjXPBS1dVFkI7vu5Fw5TLe-wZw_nhd0wVDFkuZdanfUX3BWghnukJAvI3WCLh9qfklUdxIYmFC-VhrXmupX0AXRLan1ESBJOM4c1qNUpf4smGwITlAR5pSgGS2u8WhyyRXveRhNjxcNKF_sV66NyKqNVl1lX_geS66BjrE0TtjifSkYsRNzNGhJ0JygegbAvXxq5lBzSLEY4WupXrLXnJtdYWPTwirep8f5kChQjGNi4dPIN9M3pCLj1qNCNhvLs7eWKyt-jmXq2W5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🚨
‼️
پاول دورف مدیر تلگرام، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفت!
و اما واکنش اکانت رسمی تلگرام توی توییتر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102240" target="_blank">📅 13:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102239">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🏴󠁧󠁢󠁷󠁬󠁳󠁿
همراه باشیم با بهترین نسخه گرت‌بیل در رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102239" target="_blank">📅 13:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102237">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FntN0KO8Croh2yc4c6JOZhJu5RZqOtHwv_o3MGexT7ZQoCag0KHh_LjjAaVJeLYs-JvbGzyA_DJHqJlULdUUiUOZlcmnD5htTrdv1GM5OrP98PJPbI4hM4DQSV8-oVDAzw3VG4YwDAm_RD7Ofy4G29nPSn8Q0tSYOzcLgu6W0k1sgt7UXQEMVNPdwSmJZmiht4WrpFJ1b0iilS4b7KoUUXY4paTG0ClGeLLq--c9biO2va9WF_P0exV440tYQ7qFrtsMPQToh91mXVl-pmvVR90nsQu9YeGsbGz00lcXFNEx_kIWlE9MRyMRVlgz7-lJjxnh83J9-BKPNq8-wFbbdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I0VR3dYPBVcZApdOcH3nrXcUBEKmwP88YnCdzmQg78myBD5DrTZ6hmyvECpt2xqB8HFrCfGtc4ZGYLO1GINZAvRX-95M4bFrEDu_jYGZUvC2aXS6xqccFyTkZ1d7zhPAHGAGWavWNXdYdIpsrzPppIpokR0kwM_AocCFtzd7itfr5yP4MHav3oUdPyi2B9vRmvd-nA9vVD_sQ3j2Ai3T3El-8dL-Ef_boX_LciBpEzn2CvyJxgvtSJ3b5OlAn5KwT3rb5UDDOKVztVd7V8m6c32DL7-ibl1pGluhlhr0Bt08QTKa01t3I0Ah3MYxpwC6t7HlDYSlYcEfWWc5IZ3ctg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گابریل مارتینلی هم ازدواج کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102237" target="_blank">📅 13:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102236">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrC55w-IDbN3vZkcjC3_bNza-uvzHW78f-m4B3qM4a5d6DN3dChN4tn2sQMLJVhRXIKO8VzmuNqFMQDSbF18kMWtyJ0OBAP7nZTCHQqkrorrGY6hyRat8yOM4wKENUKDOr07LgUA7ZK9cmRLav7Cy5WPKKppP_luGqX79Erydp9kzEQY-Hpk1vrIL_DHjY3X2_uWqLXHuP3pMNw0wBRzq1WrbtYTeoRNXnHZgVa6577UyBlvrbOgl6ICYcGuhQh529yl1yGNHSxiVB9PRtrd2PXmZa6iO_HPp2Iuco7_AH4bNiQOCB1qQdPtIKKpYq48E27cheIEkXoZIohbQQkmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚽️
#فوووووری
🔺
اینفانتینو به فدراسیون‌های فوتبال اعلام کرده است که در صورت موافقت آن‌ها با فروش سهام جام جهانی، هر فدراسیون 40 میلیون دلار دریافت خواهد کرد.
🔺
در صورتی که فروش سهام رد شود، هر فدراسیون 10 میلیون دلار دریافت خواهد کرد. یکی از منابع گفت که…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102236" target="_blank">📅 13:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102235">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JO_i2UhfVBHc87qGNRx2KyJKXQspRK0C6NezlQ1b6bsL8-QuRej7onnpM4sh9YavGq5nvCw2DZqkxaS0JLYwU3UUUBKXnVafLvNGun0KEozWFiSQ6gyxvbSqFvCgVpyElfIWelFddumtYEg3upFVfEhFE4-FcLfgS2Sfko7rqRIeABzepKWMuxKvb_y9n0bd88i_jxuTv7-Y2aNAkis_cxUjvAGEomlhg2Ac75STUuBkonFhen5-Shw5NYKsczvSfV2ID5DxVoONVP0xvFZnob0ebJLfSVkyizBXgYgdxCi5-mZCr-7sS4raKAuNOPpbnCaC0G2d2O7Kv1FxWdmsJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
موندو: باشگاه تاتنهام انگلیس رویای جذب کونده مدافع بارسلونا رو داره اما کاتالان‌ها فقط با پیشنهاد بالای ۵۰ میلیون یورو امکان فروش این بازیکن رو بررسی می‌کنند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102235" target="_blank">📅 13:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102234">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlLMunSbLmeQphuy_P9AgBN9OK-Rj59RahO-HixJfxDD9Xjd_kjX0DPPdzcfAqiR6U1DLWKNd44BXxSaHNuDUVkeQg1h-AV_Sk49Zm0i6DE4JrqC3-BSGh-7VCjwZZr7ok_BpZ5iyR3-sTHSFJ73QeDRfiYvjuFfzg-fi51VuFxyDLBkwJwljTfeIGHkVyJsoCweqFf1v-Gb12citGTLBpG6iP6HstEJNqiWEl1I5wcfqJg7_lD8Db7NxoIRDqRtePtojC8PfGaheLBeSl5nUT9I5ddzAGVKPKqUjuNfWOL4JpqjQGTRb0zhNiUFuh6olZCWj-i1XSWLuiPdPWe1HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
#فوووووری از اسکای اسپورت:
🔺
🇪🇺
یوفا به کشورهای عضو این اتحادیه در اروپا اعلام آماده‌باش کرده که اگر اینفانتینو بخواهد جام‌جهانی را به سرمایه‌گذاران خصوصی بفروشد، از حضور در دوره‌های آتی این‌رقابت‌ها انصراف دهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102234" target="_blank">📅 13:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102233">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad75895bc.mp4?token=swUOJAhVQsc8UjwWjmvcikBdw4oBgBC6pOIZcRjPwBS1YKlqgY6sY0rmIeeW8tXCqtf1V-yG1t7sFlhkDvREHA5I14aBT9fn9Dw1e9bjFwCPzuxIMhekp7wedWUSxHVeISODGo6b2_dsVmnocqjb_8KZCKWuwxbj4UlDUclZdRJDrp1Kw30epydloI0hDsGghh4aLU9XrNNs5TgLBi6SF6nSfLfzcZVi4Yt4-dmxJghwwSRG03CPBrU-W6GWbZ5eU8M_dY4uhLkpvrtWpNfcvidS24h3WzWxA3kz0OQNep3b9xRizbeu8LGSockeqNcf3bgHzZPsDrZ5LLV030dhaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad75895bc.mp4?token=swUOJAhVQsc8UjwWjmvcikBdw4oBgBC6pOIZcRjPwBS1YKlqgY6sY0rmIeeW8tXCqtf1V-yG1t7sFlhkDvREHA5I14aBT9fn9Dw1e9bjFwCPzuxIMhekp7wedWUSxHVeISODGo6b2_dsVmnocqjb_8KZCKWuwxbj4UlDUclZdRJDrp1Kw30epydloI0hDsGghh4aLU9XrNNs5TgLBi6SF6nSfLfzcZVi4Yt4-dmxJghwwSRG03CPBrU-W6GWbZ5eU8M_dY4uhLkpvrtWpNfcvidS24h3WzWxA3kz0OQNep3b9xRizbeu8LGSockeqNcf3bgHzZPsDrZ5LLV030dhaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
دوران prime مردم ایران:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102233" target="_blank">📅 13:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102232">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ae46afa1.mp4?token=t-jJubw2zk2tECkaLDRdgZEjps9mHgPWneK9xAr-Lx8asDhCzI5Wzqmgbvf-a1NGO5XcWs7MSVNf92h96nU9qU0u9lVY9Bk4MkVESxRJ8Uah65TuZGLP65NxraRfuSAqIDC4wSrdCzYN_JQMTXq5sfrz_qJBGvz15yxNpYQbbXxaHhuUYVn72Rq_pQNUROOoskmvQAJ3WekHo_STROonXnyA4V1JZ4taPV3QQbVC6suc0T-yPNiClXd0B_l3xKfDFoueXJFztun_8nfOLwILHx2zK5Si83mq_Klk-ruAR_CyO-682bCiZKASTRQO3EcNeTIHL0FQbN3jArmYZ2bqEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ae46afa1.mp4?token=t-jJubw2zk2tECkaLDRdgZEjps9mHgPWneK9xAr-Lx8asDhCzI5Wzqmgbvf-a1NGO5XcWs7MSVNf92h96nU9qU0u9lVY9Bk4MkVESxRJ8Uah65TuZGLP65NxraRfuSAqIDC4wSrdCzYN_JQMTXq5sfrz_qJBGvz15yxNpYQbbXxaHhuUYVn72Rq_pQNUROOoskmvQAJ3WekHo_STROonXnyA4V1JZ4taPV3QQbVC6suc0T-yPNiClXd0B_l3xKfDFoueXJFztun_8nfOLwILHx2zK5Si83mq_Klk-ruAR_CyO-682bCiZKASTRQO3EcNeTIHL0FQbN3jArmYZ2bqEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
دنی آلوز به روایت عادل فردوسی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102232" target="_blank">📅 12:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102231">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa9208342.mp4?token=Icw9pmqEoEkytWKjA8BWEuBC8nt8jfJ_Z0ZiirM1UDnJTZLzgoFT9z8XQ2TtKcBp3GZeQlnvKjzThgJQdQPksxveOi5Eo02A2tWoRfL-nZ-iJDPsrJBBhSxNqJYLAbw2q4LkJIPohOlWaflwT5tJD-uxkTrYR3ZcNaZZ98W_u2m6ZIajJrMpMBBDPJzttGT7tMrdhE4L3T3dTKwrNK2Hk3RE7Cx6ay3EtplbrSZOYT6HIv8eU0DEu6lH8ZqtJGCCjkFCgKwnzXkFxiSxxMKpT5cpE7j9sxyhFOvZoUrpJrU0SIIYL9Jjyi6y5rujTie_kMmH8yaWHTYUD0i70iByoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa9208342.mp4?token=Icw9pmqEoEkytWKjA8BWEuBC8nt8jfJ_Z0ZiirM1UDnJTZLzgoFT9z8XQ2TtKcBp3GZeQlnvKjzThgJQdQPksxveOi5Eo02A2tWoRfL-nZ-iJDPsrJBBhSxNqJYLAbw2q4LkJIPohOlWaflwT5tJD-uxkTrYR3ZcNaZZ98W_u2m6ZIajJrMpMBBDPJzttGT7tMrdhE4L3T3dTKwrNK2Hk3RE7Cx6ay3EtplbrSZOYT6HIv8eU0DEu6lH8ZqtJGCCjkFCgKwnzXkFxiSxxMKpT5cpE7j9sxyhFOvZoUrpJrU0SIIYL9Jjyi6y5rujTie_kMmH8yaWHTYUD0i70iByoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانسور کردن در صداوسیما این‌شکلیه :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102231" target="_blank">📅 12:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102230">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xc15zfBIkepBcRrLWMitIt1wZMeI_bDfA5T8vXOoAUzX8YAu7APINJWf7muwSFJaO9TnB0zbFtZekZq4Ri_BGSYnt6gSZGx5K9bjuBia1xtP5zLqJJ5Fk9s9CHo4hHnjeth-AfTdLB13mrz1eiaeGmwKKtyNKJjOz4kIT9Og3HweFJhXZlPcFHnfoyJmHGZlHC7XLs8_o036O4c_AxNx0j3Yps-9z-aGd6rFI593EIdd7fFPGhT4wOi-C_FkjQ8Kbh2BzKruXmRLqU3V60Zzkvlyxn2ht8qbUmuIPywtceypn4zIk5-eOgaiCYTeiMJkvFY5SxFeIsO-kJy2PLSqQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی با مالکیت تادبولی تصمیم‌گرفته که برای چهارمین‌فصل متوالی نام هیچ اسپانسری روی پیراهنش قرار نده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102230" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102229">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبر فوری از فابریزیو رومانو: برای اولین بار و با موافقت فلورنتینو پرز، مذاکراتی بین رئال مادرید و منچسترسیتی برای جذب رودری در جریان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102229" target="_blank">📅 11:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102226">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hq1tNom3EmPl-mTuzF4OeM986Ql0SurBvC5svmIdpElBHn5WFXAsuPwiDQR6IOlz-4zeu71fmSfGvccu1kI6uqlFBYpSdoysgg79-LSPUa9fuGTZqrdl231MYEhT-OixqmWn9590og5V8Jiw0TNVpL0DsiKALNtNUI8EGji3wyA1gc_iu3FsL5sm9INftTFci6_RV1DorJYqTB-nW6rYE1YK1xEdPGnqqC3teiXFB8lTzUG3HMhLB6pJ8L3m3zfr9ytP_e50OcBTp7Sc77C8tdy1R5os_7bSYeKJ_IPhU6AC6IiBimd3Ul4N3-lbd6pZYZeysZnrqsNFWAeM5x_iNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p198ms6ZRDtVmr5ZTQZfM75a19F8QrJxh0Vw_bYWxJi5n61JvSMI2Eb44dYp6GLd2swImmmr2g8fTb0d1qxQ5J66T3xgYjyr4hBzDF8aW33EkFLgZ152QFc0PJ5zNt8rMuo8jRA5tw4SGd1lvv9f3JWS0R2Xjp0skNP0eap3QuiStHKtu7nEu578xmR9gp9RLQcfZubsJf6wJFgSefBReg3h1NG0PZItjMS9ISVrit9y4zz96K4_yNB-sEe8Fx3_Qzjnfj7gSLnJBH8OB844-AJAJAkjZ4L5cwu5UXPXwjiHgahsP9ILM640f8-AqghTrlUbH-bBLU-MYQ-FfMrGEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ozA8j693jF-IQuV5jBOYzyG8O8HeMkDvuCVZByw_AQb_Cn2lJLG8xQhq39eFlc4h1hF53JgHiyxrdmORxA3zbYyZ5Uai5mkpjfOuqQWyTdWFPMrAQdnk_h8AOljJLrma2b2aYvhDJ_FKiAUfka6H_MA_ipQS9rzmP09o8kQPeUFxu_mSQjlpIOS5Cf_KArFGNQSPD5OtlEEZmvGA3LDrMJMVXwtgpJWldSwx9DkKRbLXPu5CUhVAH2PDuXyfRVvzNlu8KlHzcT0Zr69lUNR9IskVxNgF05nqeWy8g7N7XBDVNZZrA8IMWPpGskXSr3vo8G6yMT7J1z0NX0e8PIdV6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
⁉️
وضعیت سرمربیان تیم‌های حاضر در جام‌جهانی بعد از پایان مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102226" target="_blank">📅 11:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102225">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jI4CpTCZ7IZjXmljqplPFpyktVz7MV2aQqcojwniLb70IEjh2zMlS_QCMck80QuFtJujZVCV2Te_TrhaSnbDrs_4AFVkuFp1GmBC26JNCmf9qBl6jl7jWd8lwUgALw1oGbPTfelIZgk2132cDJmmoFhcJVmMfJ6FdNPBgS4xIrzjsy22SH4vBkahbiWd91ZXuHz4xttdB-1Gxdrm_Gc_Ij8DiyD0WnLpxAZ5vMYY3QmHXDAnlm_dhe9f5Uzp_KaSxQx7EOeEy7mj7ohUP0_C1HtCBlCdFJnxq8eKkFq1NakWXFUR2fA7pl3JpPU01ewjO5BtSXeIpz5ViwdUODtmhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
▶️
رونالدو داره یه سریال به اسم "Day 1s" درباره پشت‌پرده زندگی و کار ایجنت‌های فوتبال می‌سازه.
غیر از خود رونالدو، چهره‌های معروفی مثل تیری آنری، دیمین لوئیس و یه رپر به اسم دیو تو این سریال بازی می‌کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102225" target="_blank">📅 11:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102224">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIa6b2o4WOL4Gg-SV8gcbDwIHyqdtKPl0aO5wn7SW-gw0i9Y7T1a-NB7ICKG46wtsDniVU3sOMrF7DDtpXN_f28AAMTIhsdlKhs8HmS-u8KbH-SCt4GiUC9UOzlR5yPHMaReM50KUirjKXrIQ0dAC8sfCxflx2AK3ySsStZ28ad7GKjb2AP4IyurAiBSelXTN0Sv4MY0nLN0aqZVLEAX7qGfgW9LVJ6La3bwUxmB15XxfZoltzDimWGqYT17DtwHtrgJ4S7ds-5wlLVJPYjTAPJNjhZXECuP2GS6siV1ds058jzKnqggpVTT_qiqo7sLyaO367_M1fCf2MQnAzSqWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب احتمالی فصل‌آینده لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102224" target="_blank">📅 11:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102223">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxqJuod7CU1d6sVWx1JxugUYZkpMbtskPg3NRShtd51wDQOe8zCSmBA3f-GrUoXSqzLirtqPu2usFe9Ra_xm7KY4x8EpxJGGYKeZs-jrtMxZGl0ybasDTBnyYeOLZmU9Gec_KRo51LhbLj0oTK5w-hmEpTYlAdgYqwKJG6E8C8HnGTsOy3RD7MvUZHqI3B6l8Ojjpqb4WmJcbGVRu-AnX2LshjJGdqcdBtWKXbO06afChOgoYsoaMP44Q1kSepxFk7Xno-3cwA4B6chUq0CBq5CB6MtgERhpoJHo-e9Rn_pbmqdxdILltQjQddJeQVBGfQ_DOmrAhDkofIPtrGMqig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبر فوری از فابریزیو رومانو: برای اولین بار و با موافقت فلورنتینو پرز، مذاکراتی بین رئال مادرید و منچسترسیتی برای جذب رودری در جریان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102223" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102222">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fW7VWSEoMiUr-xMQd-EzevpHs-dIYq9Sd3XlG3rmfnKQ3b15onw2rSjPhp8YPrt0ggKHf4trqltBVjWejsvoXQSDcDzvmCTTbDiBYennJHmOmU0h0FgnkmiYhs-wTZQFm9QGGoziEp4WIPIeWC5eq_7QvpacEBX1bCb3uw76_7HhH3LGV0cxfoTovA7N9U2-1NjId3Z4YyuGXgtOFbxAkJTtNjdENs6Fz7AYQ8J2g8KZlkD4C_yD9U9WWMpcr_iXfe51tfOimd7UxVrVNDMuKpv1_idlfoxyEqtpDNWCskTuqhRN9dFQ9AXU5XQAvbSmmVML2FN0OICa-HPtMkhuxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
💥
تعطیلات امباپه در کنار اکسپوزیتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102222" target="_blank">📅 10:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102221">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAD-zFOBXykdZj1UnS40jU0NwrtVQK2w-9Oa9-RaaCWAMKcs2-_Iy4peRiwB3Tjg31PebJRk7QYZaRO_KitDoBO84GLiUGlbIiW7WQZ1XfNSxk9Siz9G8xriq2JyGnrbvjAKXjFQ0KiUfAjl2r2FqZX2glfIcz3ROPYLHMDB3DRcb5iiHsrPSHH_u8_reUrULp-jxlgZBFsQn3NgFO8geYAZJ449dOuo4217fEVtOcvMhm6UCMjMvYMWvBlhvGcOx5zElXFvOlQxnWcbC8bHcSCT2tkT18eZDL2SIX5_2UQ7wYgdf6joaTueusvijURJhj5Vq5nIAXycKs5UZ7AzCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
6 سال پیش، هالند 20 ساله تنها 71 گل به ثمر رسانده بود، در حالی که در مقابل نیمار افسانه‌ای قرار می‌گرفت که در آن زمان 375 گل زده بود. این اختلاف 304 گلی، مانند یک پرتگاه غیرقابل عبور به نظر می‌رسید.
🤦
🗓
6 سال بعد، هالند 290 گل دیگر به ثمر رسانده و به رکورد 361 گل رسیده است. در همین مدت، نیمار تنها 84 گل دیگر به مجموع خود اضافه کرده است.
😳
یک ماشین گلزنی که به طور متوسط بیش از 48 گل در سال به ثمر می‌رساند، در مقایسه با یک نابغه که به نظر می‌رسد سرعت گلزنی‌اش به طور قابل توجهی کاهش یافته و دقیقاً 14 گل در سال است...
😭
و اکنون، در سن 26 سالگی، هالند کمتر از 100 گل با مجموع گل‌های دوران حرفه‌ای نیمار جونیور فاصله دارد – یکی از نمادهای بزرگ فوتبال.
🤯
واقعاً باورنکردنی است که هالند با چه سرعتی و ثبات فوق‌العاده‌ای گل به ثمر می‌رساند.
⚠️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102221" target="_blank">📅 10:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102220">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f225d20c69.mp4?token=SLW8mz77sES42O6YV_eCQMelikLq9cbM7nWDuW3Bj7TYzrZ8CeQ6j2EQ_tEY553aSSMHjwCbgX3W5IKlGCSxrJF73BKtH7yMfbOUtdOHXRalUZt9WIGSWrsEzZaSLuuqJVQUcsg0R8X8id0yQKnFIqxcAcDlY1FvGe506sjykeewJYBWYXZJoVs8juYn6cpxfuYhpJIkx36cfsigQZPvtyW9dxPT4XbnEJGWzTM-csRSnYKz4VPOkgwCx5kyN43bmRdHhP6B1-mJu6d9BfJtToIgIl6UuL8MibPuA6xQl03RnoZ4g-X7J3URTbaPTFGirywlNEHZxKGYDoTFNmevhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f225d20c69.mp4?token=SLW8mz77sES42O6YV_eCQMelikLq9cbM7nWDuW3Bj7TYzrZ8CeQ6j2EQ_tEY553aSSMHjwCbgX3W5IKlGCSxrJF73BKtH7yMfbOUtdOHXRalUZt9WIGSWrsEzZaSLuuqJVQUcsg0R8X8id0yQKnFIqxcAcDlY1FvGe506sjykeewJYBWYXZJoVs8juYn6cpxfuYhpJIkx36cfsigQZPvtyW9dxPT4XbnEJGWzTM-csRSnYKz4VPOkgwCx5kyN43bmRdHhP6B1-mJu6d9BfJtToIgIl6UuL8MibPuA6xQl03RnoZ4g-X7J3URTbaPTFGirywlNEHZxKGYDoTFNmevhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مروری بر برخی گل‌های اسطوره کون برای سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102220" target="_blank">📅 10:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102219">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ef87c459.mp4?token=lHYNZf0j5PW9ILtlYKNyc63ffAvHtmReNKK3tFKnXSMGb57R1jlUbLBtAZ-F3JP4N-fBKSh5n936vGBM2d5KYUT5EN_fBDBhbyb5WUnaJoh6WtufxMDQ_-GmXBVD_l3xEa87-Bo-nMtqwf7o2dRKYVpE-ePvUFRkMO7aAIaJbVATfM5dkI2QVbqM_R57v-ePn6sIv_yrT4GQCx8mnX4jdEH0PYeSYLyKwhRRME7kxHhMNxug-wPYMzdEmTOhki0okckHQLEBX0MLTvn4pTS3D-UTHyRkfMgKPMuOQ_jo4w_9aYYMzEf-_RTq9HB8WALKV-I5Fljlp4tjc8nIIDPopQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ef87c459.mp4?token=lHYNZf0j5PW9ILtlYKNyc63ffAvHtmReNKK3tFKnXSMGb57R1jlUbLBtAZ-F3JP4N-fBKSh5n936vGBM2d5KYUT5EN_fBDBhbyb5WUnaJoh6WtufxMDQ_-GmXBVD_l3xEa87-Bo-nMtqwf7o2dRKYVpE-ePvUFRkMO7aAIaJbVATfM5dkI2QVbqM_R57v-ePn6sIv_yrT4GQCx8mnX4jdEH0PYeSYLyKwhRRME7kxHhMNxug-wPYMzdEmTOhki0okckHQLEBX0MLTvn4pTS3D-UTHyRkfMgKPMuOQ_jo4w_9aYYMzEf-_RTq9HB8WALKV-I5Fljlp4tjc8nIIDPopQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا همه رو شکست داد جز ...
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102219" target="_blank">📅 10:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102218">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvuSpTFIhOtkjd3hXFMi9eqy5TCru_OU08d5g8L8Z90MmYfKgeQ5aJFII02hlIV4YwAqyN-7i--paB4e4aSOyH0kmM1EpPmbkm2LSvIXNM6tkZWJ58gmQHsIHpU4eiOZF9Y07yyEmjJY9xW_puY-ixmfw9oSDIBSPWlOvC_H3HVu3cc3iGFI1DYtrxGrrYQxI-sdz88M3XQrYf9KGzUbW4wZY-kMO3FmOg5W20jzn0uYJ0QTwlw__lHT3mrKmyx6ZyPGfCbYJ2WA7V9VOR81g4IhZs_LvdbSjawW6t0Kz5WAhvfxeryFf05nbMYdafrZkK3qP5FEar21xehN4NW07A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
✍️
فابریزیو رومانو:
بایرن مونیخ در حال بررسی تمدید قرارداد با هری کین است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102218" target="_blank">📅 09:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102217">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5802c51b8.mp4?token=iNBGHgZavI5KjZBjymJzHZykHCeahdmhaeYNPk--LvAhFHFRJlq6EsmnEb18zPX-Q9sAyUApzmYqTcH9JCGlrrWohjdS6PboJ9xX8g_JMegGx8CLTGG7mmXmC7jQkzn7iECRc0BZnVI5lIwGgFtFUtrHm60-mwDQb3YWcx-THbm8QVqfOw_h2vTIKgNh_BQaG34ipO-6S_LVGg8O2UanfCUDnmBu8KOqMK0fy32E3thFkL1YPQev2eXmNQ7ubnNC8fhFid29MRY1FgODlDzGInRcak5kQP-nprhaRfjjvmlaQsTdPQt1etQkHtevas3g6W4OLP-FxKEKbkZr7NQ0LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5802c51b8.mp4?token=iNBGHgZavI5KjZBjymJzHZykHCeahdmhaeYNPk--LvAhFHFRJlq6EsmnEb18zPX-Q9sAyUApzmYqTcH9JCGlrrWohjdS6PboJ9xX8g_JMegGx8CLTGG7mmXmC7jQkzn7iECRc0BZnVI5lIwGgFtFUtrHm60-mwDQb3YWcx-THbm8QVqfOw_h2vTIKgNh_BQaG34ipO-6S_LVGg8O2UanfCUDnmBu8KOqMK0fy32E3thFkL1YPQev2eXmNQ7ubnNC8fhFid29MRY1FgODlDzGInRcak5kQP-nprhaRfjjvmlaQsTdPQt1etQkHtevas3g6W4OLP-FxKEKbkZr7NQ0LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
کاماوینگا بخاطر همین سطح عقلیشه که مورینیو میخواد دکمشو بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102217" target="_blank">📅 09:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102216">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTIyRAlKf1NRd5F3jQFv2GiD2P6zMCadCC72uMwpNj9gtaEizPvpLChxBe-QoHbUOmE82I0DMsnYORKfNF2dZJgYfEtt7bjIgj_tkOeUY2NEAmKhaG92i6-VW-Rqfsi1m4SPZ9cTaSxhU2ZW3irbxMJ09w28or53KZbIjpYMXawRJuCK2FojEvSfBzlblisjeu3i1kpC8WBjHCmiPGoIEVn9hpPTue9NmjcJG0hecq-tmgqETi6P8HmTKv8MJrosKyFVi6DE8Q8RI3dXGngNWGHaFo-jzjh5XYTbmV__3w6AG7HCu9iWrTqJs9AfbSkCh0bxfOWp51igVD4fx3p9sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرف رفته زیر پست ویتینیا کامنت گذاشته که ناموسا تو جام‌جهانی 2030 به رونالدو جونیور (پسر رونالدو) پاس بده
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102216" target="_blank">📅 09:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102215">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4792b1fc1.mp4?token=LXyJgH-RJc709GxwOkhYRizJVGoVMsZhpopkBuV9cGri-uoXrI_kATfD52I5z513zDoCAX66wUUkKSelJxeK6GsGgvWozA_GtBFUNyEL-ZVCaDN0UBSmnS8ipVtpQAWsDS_LBY-lfIUnHSAaezGXPgV4VbAe29fqfgYZd_wWPnvrSHph_f2Yhrm1lIgoLkzzi5pd4TTQuZOw5d06K2aN3zYipsDrbu7kF_ndV4xjZl53wKzeiJntuKz57g3qMkCaq_DSe905vuSe57vNnEtncBca2kZx7izerRI_J_Rmrk24kdWcy8RbP3YZYQljpjF3W6a_C3xLroDjbsQGYtiR5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4792b1fc1.mp4?token=LXyJgH-RJc709GxwOkhYRizJVGoVMsZhpopkBuV9cGri-uoXrI_kATfD52I5z513zDoCAX66wUUkKSelJxeK6GsGgvWozA_GtBFUNyEL-ZVCaDN0UBSmnS8ipVtpQAWsDS_LBY-lfIUnHSAaezGXPgV4VbAe29fqfgYZd_wWPnvrSHph_f2Yhrm1lIgoLkzzi5pd4TTQuZOw5d06K2aN3zYipsDrbu7kF_ndV4xjZl53wKzeiJntuKz57g3qMkCaq_DSe905vuSe57vNnEtncBca2kZx7izerRI_J_Rmrk24kdWcy8RbP3YZYQljpjF3W6a_C3xLroDjbsQGYtiR5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
جانفداهای عزیز درحال حرکت به سمت مرز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102215" target="_blank">📅 09:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102214">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8836d3c9.mp4?token=fo3q4eUJAyJDmPDMbDi-jh2cjyMmtZZybbUWip2_EnnJL_jJ8Tnl7nZrQ33ZxwGSBtib5jw2qfZ9cT9ligVAXDvrw4kJuswcQ1kzmKoxhBd-aVBc7_sii05EaPdIRU5Q5DPJCnUJza773P4g2-Pc4kWQsLkzclBuXxiLlEd_gUL2FuahKFHkJ1bwtg8dg4z3U9BXeIPGf2MdkPmqbdffHmuX961tS4vbSlvHqW4kOeFdJVD1wKxmP1bGb10z7OjCXyosYoC1uWfk7kxG9H8aGu_MHI1X0Y-vWukcxeC9EzHfrV4da2KZJwxJooCn0cm1Sr-JA1ryDfa17omUOgoJjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8836d3c9.mp4?token=fo3q4eUJAyJDmPDMbDi-jh2cjyMmtZZybbUWip2_EnnJL_jJ8Tnl7nZrQ33ZxwGSBtib5jw2qfZ9cT9ligVAXDvrw4kJuswcQ1kzmKoxhBd-aVBc7_sii05EaPdIRU5Q5DPJCnUJza773P4g2-Pc4kWQsLkzclBuXxiLlEd_gUL2FuahKFHkJ1bwtg8dg4z3U9BXeIPGf2MdkPmqbdffHmuX961tS4vbSlvHqW4kOeFdJVD1wKxmP1bGb10z7OjCXyosYoC1uWfk7kxG9H8aGu_MHI1X0Y-vWukcxeC9EzHfrV4da2KZJwxJooCn0cm1Sr-JA1ryDfa17omUOgoJjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇪🇸
پپ گواردیولا: "وقتی به بارسلونا رفتم، یه نظرسنجی گذاشته بودن که حدود ۸۶ یا ۸۷ درصد اصلاً منو نمیخواستن! نه هوادارا، نه رسانه‌ها... چون اون موقع از دسته چهارم اومده بودم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102214" target="_blank">📅 09:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102213">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGLpJulFpMa0HTdQauIBajV1zTpgIw4YXPgi9ZGcFla0wQfr9y6pKNC023510S_Av2cTVug2NK0wTAlBbksH7HcLeD4LEdGqh-I2tOE-rjQCml2Gi-EAW3dMxKhGrynWNjr711CxTue8CXhbi60eZiud7Dh94Hh6uj2EBwCe-GSbhdivyF-tT4eI7g3rLSuRs2F8sFHSLUr2bkntoI1WR0zReb-PEoNpMRqDXCWnYFmWTE43dXZnrXjZPlWBlU0g7BtSERX_Ydp7rTj8DrVhBEr8tEojh_mY-dDjO77SNXzjqsc0-Md4liK-j74iIPM1XRSYRFapz6JffW9BYCWg1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی‌ولبک از برایتون به چلسی
Here We Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/102213" target="_blank">📅 08:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102210">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R8B8H8xkXYoEpKNAUeCItqHeywSAAgIp5ZWPzG5tOu5keBk6-DEf8ZOQGxoDiDulW1xT4gPevQfkrjuqswNd6o1W6RQnPBfEppEU3kd29NRxfpkXt-CrPbdEmtg2eNqg6ab0lEwTLZErQhDJTHB4cKJ733RGwqYvAf8UnpcRmZnADd2wICRHJbEeM36c0p8bFoCJlpr-cK74C8fjlnHslWGepeRKmE7cS2G6cQepEBQaHDR6GWKaMre-pYYouwP_T2kNpzCc9-qgR2ZJ2aNP3DDuHl7Ix2gxqcBAWpbu0NRUGaYzPgGM9ts3-5lFQLo2x_Bgo-0kO0psB5LUr8IKgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SqjSZfC2c8II7NIyZ9Nwm0WhDqT6LU3DexQkK18kZi-yW8B1YmoNl-lrS6IMmreXTB9KP8oxYIpsdGu71pelNTFO4QzCuAJMuvZ7g1xYq2heShf0XE3g2d1R3OgQWahJhQX-i-165MwvDSfT0LA_WgFW6EdiACt8LnxjQq9ZWnjpvigq3s67Gghpq_c45J4F0CeqUHSAABb1gL-iHpnRT7mTQ2Qh6IkO65PWEG6-7mgyc7Ve8olrcY72Z2VtMi67INJwhHViSWKD-CQ9xDIvmZe0-pD7tL4EXsI6qhZm6uzRmUOjPqyvZNBWZSsfZKK0K7opDnlU1WACt9mwyLQ19g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P_lpuGYvJdXlVfIDJWm3ZsRg43LA4M7ZYjwHSMtY4VEfzYoh5hBIdQvusZXw_I7lYbxrvu5kvrfKjYcrWx23dl99lOVtkoWo67jT4bnqfv6RLL-94M-ldMbgqCzVwWrz7ZF2EY01FMHVQVGqKXFDPS9or5NZEZdxH7v8te7-IKZOq56T7guWvB10tPQOV0GLJPFwEtjnyBAtrjIUzEVjhlZORCPCztUbFsXKFGzmWQ_4hzwdAks_lTxc9ZAd4rrD3f3XrYgKJey3OswwQDcEosrH5AvcuQJxRKeHo14tbc9Mpco2STdehLtgbhnXtkBWOToNdwNEdpRGT4yOO2BE2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
- کیت دوم فصل 2026/2027 باشگاه لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/102210" target="_blank">📅 03:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102209">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gihc2jbWJoYAMUe_f5wWWJ08FX_qv8-tCJEu_epETGeJtxnXmx8OUB2_444mrC24FOLm3nAkFs5xvV9ECgC653HcFP9PUFGRJj-y73Tb4sV6nByVk_40GsE8IDVruEd1cnL04Q9r1vMCOj0_vYRnZtG4xeX71VHsTN_9FWEv2GhIubpT5hvZGAkxObOruaJozQ8JtYeRNuFdfDoOaY_idjrUakxU43X8kdcpuNp2S0YDgQauI8RdxCEFMMeErN9aFiHSm-eXQ9yPY_V8lgkMTCWPh-lLKJz8ITdHzgK9CPhXpHiP4qBF0_ouOtose9DRIRcp67D7eZ65pC8_XEpBpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ سنتکام: سپاه قصد انجام عملیات غافلگیرکننده رو داشت که همه‌ی موشک هاشون رو رهگیری کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/102209" target="_blank">📅 02:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102208">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oY1wQLCBnrHWKfoVYIQPBWuvZUloPKpTO8yL2MXBeL9PptF5rjBhh7kMGmpZ-SDzQIwdn8YOcKSPwp7YKm3L91cSltCK1ymEFMAG32Pt-ZncVI8wOpImZgWg5Vb2RfDseRvj-wleIW_L5KKjjZ1p5gesaiajYigvyzmlrm90EY-bky2vAG_qdgyJgtUvVvqL2rqYujaZPYWKmEiOF1gjlPZh-SDmwdThswBwDx6y8JxlaJZP-hDl1zWHsuwx2Oq4aPitwSihrh0tnE2tSi7XSh_H6ZwryORbmiJtSvoEReJ0RmB5iuKQr87n48w7ZG8e3G3Ih2pgjgjYGYXijMm4SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: هواداران رئال‌مادرید آروم باشید. روند تکمیل قرارداد دیومانده با سرعت داره جلو میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/102208" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102207">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95f6f50330.mp4?token=WVK7qX3Ye2srfbWJt-rD4YEP-4jTkh5Vu91keiatsb6sRf-F_kIuGkgRs3_vtN49hefHdL1UP-33hmtxhIivoMzob_OcLhZh_64IzS7VBFA4w9mQSF_iUjEkGxp7BKBhUQlgPUdQU4X635WmH9WGZ8jMkktFnbq8br2oas30JEHLwvAM_21G4h1SaM40bjuc9AHi1sjiFK6uLNp1n6jaWk6sbvKKVcoPcmCKTIA-aPJn6QVCXz-Xrh8AiLZGcalOTIlNKpjTuzfhyhnmZ_i52cfrO-aqISyIn_un5spc4gcE_i7qPkLSHlx6ZtCBrKWz7DBYWduCcJq3iiyPpMm0uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95f6f50330.mp4?token=WVK7qX3Ye2srfbWJt-rD4YEP-4jTkh5Vu91keiatsb6sRf-F_kIuGkgRs3_vtN49hefHdL1UP-33hmtxhIivoMzob_OcLhZh_64IzS7VBFA4w9mQSF_iUjEkGxp7BKBhUQlgPUdQU4X635WmH9WGZ8jMkktFnbq8br2oas30JEHLwvAM_21G4h1SaM40bjuc9AHi1sjiFK6uLNp1n6jaWk6sbvKKVcoPcmCKTIA-aPJn6QVCXz-Xrh8AiLZGcalOTIlNKpjTuzfhyhnmZ_i52cfrO-aqISyIn_un5spc4gcE_i7qPkLSHlx6ZtCBrKWz7DBYWduCcJq3iiyPpMm0uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
انفجارهای شدید در اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/102207" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102206">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxGkXGvELZjJa-Tj4mGYBGvnHrjkscCC6DCSeHQLcGaaBCrhAffX9vj-8A1VovlO2x5C348U7nZnXy9QSvXTmMjC2eCXwKw7MOXjDteXHLOdlsrM7a6spoEAao6qR2BAjvm5Bv5HwhHbB98w0OuN-8zTq3A2dQvJ4Ob57AkAL4nMuXgLN2L2PWe7OWrSuyJ0eji3UI-UFHhRAnAzuFD8hM3ucU7ko2T-7ndt10SVYOPoj0kNYqENBRBpCmcr0AOtJ3yrVMlPF7Er1EokVcyD_HVLUf2TTaavqC-1BGNou8qftY_r7vLGu7mK4Jgr_cCizD0-vS45yjVut_JsuXdW4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گویا ایران از چنتا شهر مختلف موشک ول داده سمت اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/102206" target="_blank">📅 01:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102205">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuU_c4mhm-ppPLhuj87hmJXwoJSFW8TuXCyriIR51Qya3OOsTd85D7WrcNHhURP8U_YPaUiTQMZjeI7qJy5pY9vTE5yd4uzPivZvq18YeJPi2jMijfHqtnve6G5CuGKUl5EDNwuhY5SzG4OB27sdtAQWbFI6kdwRaFNpNaAmjJVV0T01KdybXYafY30fQLTWf5e-_Pf89UGmMNejSKvK3wX0MeAKra-qM0kDcdFU3YA-TLdEw_R-fbbdCFhK7baN8YzS8N20ZTyUk8PowVaywNTJnYokk4_FCw9AcyPbNZ1CBJe57Y_5_AKGs9dSVtfJr8xboLaXJl1YBCDl0jL7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گویا ایران از چنتا شهر مختلف موشک ول داده سمت اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/102205" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102204">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYHiF4lMpYIvAb0dy3EcjEE32MFQKCoPwfvI0eU1Hld0p1TxNIl1vYYrWWt36sUJLezxWc9sWuGyyITPjc6eZKCXsvuYVgS7cCHViGeogpn9PvDYXTNsI1zGdKUmduAp0FKlAOBm8nhxuqYIRyWUklVUMDvinTLOjbENO3ZQW1wZ0-kYGxgIdt2fLvBu7px0bk1qm7qfsoFpwAn5MNt0jbtkzHDUP7ObPMUJWMgNpVpaA8RoQur4LCxXccUIb2beEyQawSdy2K1Mg6Ud-ChtPSb28mXWy3swUhldiZP6YbNefbCw3E16Ru5hu8JbrCSDDM035Zhz_CQTiGH8ZY22vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🙂
👤
تعطیلات علیرضا فغانی بعد WC
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/102204" target="_blank">📅 01:11 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
