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
<img src="https://cdn4.telesco.pe/file/KTCIgV_x2mu-Q8PkexSb_7PT62D8pPPw8clpksNsW4dGuMwta6MLaUn-RMqUyyNV_CsiizrSIj1Og9XCkOHzF1es4D2U5XVBHftJypHVvtnvXOkLooDHP6KC6oq7RM2FOFvJWW2FgiBJhSiY_YPM_gk0Mb432sWvBkQC8RtVprqPAi7gf8sgm6AT9reQFu1sYBPksnaa_Fb-1oGLAjiJbAljYPdMKLAiQ9qdla-kf-LOXekAHVA5S60IgIlWIWtJ3gm0LIxlkTMo2OvAo5lmrcHNLCnKf4Fd4UCleptLYYXr0eQDef5F2WcwfFKqaqJOsXYCmrNIwPeQgU6_bdEpWw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 00:07:11</div>
<hr>

<div class="tg-post" id="msg-83083">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrCLzbm0vjfUvmGlcoPEqPgbwSDbCsE-3rSHP0L9ivHqAq5Fcw63jhY_tu2ANo9YitEhI_09NDRS3sL7P3AYBEVTCNFhNUU-zvBUI6gi2DgndYoMgOhbOOzLuoIc0p1H0x_-kAj2uC9e5LBiTuVDcwSeyZEufGW6bYxZd2JhnV2hjoI2qYevY1-ojJaK8LIiFby6ucjwc8Bk_QUbtgMdDYOTsSkerXu2Y68DsSKixxymgvZEwB9dMRAD41M0B4bvOSX-bd15ppQx5B-_Gt3DdvDN2k7FJcEes-Str7KJeDv_jJSNT4TX8f3dQGykTD5kDF2pUvKceJVUBlysIu4ExQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به ک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/funhiphop/83083" target="_blank">📅 23:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83079">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ImjA3lgJLrjW3Mm0IwlCV7E770U5U7oRztNGyIsisK6fK-L1BIvbAMU13jNSc0b7XmWarRBZaIae2agF_wdjeknoZbNEW6X-17F-RHCzgiJAVdY2emysPKXBhIj6TfJh_M8qixxFLwe3wmB4RtPyoGlFoR3y6ku1s5Jqo3W9Wusob9cPoB5j9dDZY0U9b3uvaOF4e1mKavNtNNb6ePIK0JRLh1hPJbjgkkJkl0MzbwENL5yqwSZyfBGehqTep4I4y2eBB0qKA8xBBhavysXcitZGF01Ov-oA351BNN4tJQZx1qLq26132wq-D1m5VVEpr7l88XYCsli7N31fns8PRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQjyOsBjsI0b63l3Xx6UDUs8Hdn28PLwmwf5_m2DmrzW1vu7u-gPCONZaltH-zSvp0rhvSTemD1l6xAropDKdI-9zZ1HU17UBVpmZA7tIGF1nMXEdYyiy7n1Kb-W64LS9r38UBvjiQK7mIMfrSozau94KV_A6WDu0GAXAPOL_jOg6Fs3XLCoPEqwEb7IElE3LqPPyz6Zj1WtxrpziNx1L86z1CphmJu2FucU_tTr2zLSVoP6pxDLpdDPpd1j9PGCVN8DOAX01v6yA4sSfsdeYnZ-DXsz-cXbYZBpDiIli_SVIwUj-PLPmEeQrCIpV4M_oxSA3ejSuTCwXsGlplXk1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hKJuwSXng0B1MyJyW8FsEWatMzbF2t0eLIWMvETaDOGe5-i9DTwOQB7wvYudI0Tz5AMpV87Kh8ALtMclDZAt_TLHLZG2wNncRhR4ZBfhcIsWAzRPq2nPy7CMmJDekdYIoTle3eWraA3RI7QyBAFhcNs7Q_QYuYBc12bGoQVK1hP9KvmyD7cotiycQoRPW601g6QaFEZ6eDdBX42C8XiqLWKG7TuXyOZvNfzF8XBm5g_wjaUrnZ32LC4lH84dMqaC25ZJgxVeWNwexg2wOkAX7HzhKkXfYGpXa_cItTI6UqTTs0cWL908ibcCDmGPaimImUrIU6LEx5c1faJxeE9APg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSy0SABD_jabKAxcUOVbxzZ7YPQ9PaKewCNPhSKrejY_k91mz6cxzgFBakbZz4gBktYyqf2VDPQtsPrE5PMWeAj5FWwTm8A3auk9TEPvXaFCEByn4eTuyACX3IMNLJG2Tm7PzA-1WASV5Qr7-tp_gwywoNb_57c6aRjBjHPCqUIr41v48nfkEuNqPYOqhFKdGewvymMznnGlM3a7gmQHqyx9AHNjjY8Cpl9vIFSDgsRn8bkHHFGYEEUSlvOA2HOlQ6FRBENUTD9h_inJv57Dycx6brAzFutUzuEiMMo9ElRL_yW1iWzHnFSKloqVEUktS40z10WI79AK8yymyi_Xzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صد رحمت به سلامت‌روان دوست‌دختر تلخون.  ترجمه:
ماه مال ما است
🇺🇸
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/funhiphop/83079" target="_blank">📅 22:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83078">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kke0aDMCxzfgsc4K7o_XuRPUzQ-zCvtaBwE9nhKgqY3tSY7Wyxo7Qnyk4Lx7dkALxe3YT4_HCFh31bo44Pj7wIb0EHh8zGrTT0BRBLZ2wChm2LWjEbgcEMX3rPh1k6AGZbICNsCsN79qvNK5rLDZ-ZDzIczJTEae3DwDD0CyVKuvVdIfqo6e-KBGoAv8CPUe3tWcisqvDdodbCgUIbQhIQhigjnRnVMWi0IgVogBhBoHAlY9_ACIuUa1EjE6UVu8aJLPsZwZqIJ1r3iW13Ic4dufZS-GfnMWmSuVxGajyVZP9ogn7Aaw6qvsVQ3LVAPXCwBnxse6g0Id7BD7FGPclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من حتی خایه ندارم با اکانت فیکم چنین کصشعری رو پست کنم؛ این چجوری می‌تونه به عنوان رئیس‌جمهور آمریکا چنین کصشعری رو پست کنه؟  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/funhiphop/83078" target="_blank">📅 22:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83077">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4scmUb5IDMuI1TQ20zqcxWtAmlUsXFAfGXG6mxW5IV1IpXJyd5aNWZn-rshgm1dQ1Gcjd3ngWzs251zg5M9-RvXO_rCGBz-0Tmwiy6K5B8dIwzRQU9HAih4C_i6tpF3TTiGTRCTwb18Grp8L8y0IiWv30GYIoN8TdZStPLDS3eIL7etuCzGuSrKb-DTZTXWRlwhbf01JGc9-krhtyy08MObwHvG-ZIA3BM15qLwVc3XmvCfO8R9xVuRFXztfXN0mzPCWVmKMa-x9oi2NKQnBpq9olCIHw79gTVzWRhU19F6ZOm1LAJZB_LFvbMjsmM6F4hDfwqubOrpxhJyFivXOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من حتی خایه ندارم با اکانت فیکم چنین کصشعری رو پست کنم؛
این چجوری می‌تونه به عنوان رئیس‌جمهور آمریکا چنین کصشعری رو پست کنه؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/funhiphop/83077" target="_blank">📅 22:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83076">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">از امشب نرخ سوم بنزین ۱۰ هزار تومان میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/funhiphop/83076" target="_blank">📅 20:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83075">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2ybRm8_4M50GFYNEKpLedCQVkGZZ8YFLTC8ZZzi6PMLKRGnYyFv72qKzYJtpJIwG5ygpl80WpDCQnt6ejEt9vJpCh7XI1tC52f4nI0q4iNT3LXsHhQhh84bbbB3GhezJfHnd_DdC-KUkiwknQSDCpop9QwZPsODlaiGcGJxumKttqHUbX1Fcz7EZSQ4GngXWXS5GS2jDZzukOcCtKF0GbtIlBL5tSnluTj_8-2XM7YgYlU6WS4tgnhqlxgWoZIthXV--9Q8dKu3_VFZvhx3NsUPKHd4x7oW3W83vq8cBw11QnJS-dcKY1RIusqHuNYaPPYLtgdUr4UvsXaPZpNl9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمین صبا میره براتون نونم میگیره</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/83075" target="_blank">📅 19:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83074">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYQt6n_r7meu209e4GAWZOkxnBF5u0sts05P_qJZfRb7XtvLwoeczSdaOoQUBpG_NppScbsN3UWd-JiLZVmothd-TeYiF9L1exEqgWDAmAZReXBnWsNvTMyM8hViV8RVlaZ2c49iSMdzT-59wsTrOe3ruEvO8ob-cZ5Cw_4Fi9FUZkjg3kn1Ly47OTUgzfN1XOwhrI5v8gz2wOkTQ1wJMx8yutFniCLQy-aI1jjMYxle9ZLhsMftoV6uxaKREx83A2b6nMWV2IJhBzixImqH9UruGbp3KN9gT3G7mUZaCh5VAc9KdvZoe41DP7Cq615IXf4orA3EAyQbQHuyxGCu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش به خدا یک هفته از درگیریت با بسنت گذشته،تمومش کن، به خودت بیا
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/83074" target="_blank">📅 19:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83073">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کصکش پا پرانتزی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/83073" target="_blank">📅 19:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83072">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">منچستر کصمادرت</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/83072" target="_blank">📅 18:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83071">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4_KrwsXz7jBAkVfLFDU0cDejHdSAoQVnY2kJ66Vr3ThpsFaX6NwIR-RomvtMI5mhIeDdvZBW4Z89PsDw4uasNZMaG7sEn6tWKRw5KvqEK0GL-THLlfMXgON5dao2okPDmQFR_EBpmw03h4h286FeUeVZw0Af6JVX4gGfKv_0TEemzc5L09FuupnrQR-KlFvul7PFjNQtbyvodiMxqhB1xiehKoKiI_6N1026RmXuuOgs-GrYQFj8bcRwsool6DQaPE00fsh-eofpVgTVXInrDBoUFYSKBE4u5npHjrqQMYqg3IPB1vWBkHMw8m-_2EW-mV8skdKVw6qcdv23tzPEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز خداروشکر گفت روحشون شاد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/83071" target="_blank">📅 18:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83069">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فرمین لوپز شاهکار بشریته</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/83069" target="_blank">📅 18:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83068">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUUoDcfjBC6UGI1cNzp1pgN1D316XZP7tYmVe_536w7dz_YmBxJ5TzFCBpXpwn1Ekp57gtb5K7mEYmDa8nAheUTiqe3iL9u11dh9HefS5s_QnN41z5AAUAWzOHeUxv6oWk0nPKKcMaYLeYxjTWs5ubPhtNeXu487ka_I8RgbrEqHGeY07KwfbIxYRxUlyBHlS0jb4iBAg-N_bx5LdiYCpJu2tLlIzqf7xK4CZmQHs1xG5WzFNHHzyTOp3FcbdWJ3g6WiW_n3fk37sEgOZNzbVSjXjF4s0T6T9t8Uxy-b1bkpT1FcztltezFdRzxnTFcHahQfrrEa5rKPRLjxgo2q6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداشم آلوارز نفوذی درجه یک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/83068" target="_blank">📅 18:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83067">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORB9t6jlTUIyZBB5DKiJYwWBupZX35PzfPZoloT-QvXDaC-oYCHnkivg7reJkyOIWCWyFP1RVN7DXPmQ67azOCArWEOtjrHCE5mEmZUFAVM0vS0IWdQUnK4bp1N0afFBw4WJqLGo68gCLALp6lgtuOXuM3gTVoFQDGygog5FL3QZwrPtmKkqI17Eh8iXms2T9fnr6Yx2omVUr5PPFZ0xj5OB90QFwPCPXIetfs1wd13LpeP5wnw9hHMYpE8jIb4UOlWMx3uemX-tibsYEO-CQzlbtmBdJRqKN2L1wwV_QlwVXBalBA6d_vIigt7rBzC1dByOVzjDylg9cdv4azTtpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
آرسنال
🏴
-
🏴
چلسی
🏆
لیگ برتر انگلیس
🏴
🕔
یکشنبه ساعت ۱۹:۰۰
📍
ورزشگاه امارات
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
با بالاترین ضرایب پیش‌بینی
📊
نگاهی به آمار دو تیم:
✅
آرسنال
:
۶ برد، ۲ تساوی و ۲ شکست در ۱۰ بازی اخیر.
✅
چلسی
:
۶ برد، ۱ تساوی و ۳ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر آرسنال: ۲.۹ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر چلسی: ۴.۴ گل در هر بازی.
🧠
آرامش ذهن، دقیق‌ترین ابزار تحلیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g15
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/83067" target="_blank">📅 18:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83066">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgMC4Rtk2VzQKqSdRSPylGQKlI11ukHBGpGLpgYZpTh6h5H1PyRpXWrs2Fx7e19Z5sooTWTr2MxrurXgPFU9EgprW4VzHJUCqmbr2AR50tDfBo3Leg2R6PG-5XoG55l5ljea9DHbWoPFb4YDtVJBPm9ZDYsUFb6fze-tCptJ5gIPTxpoa2m8Fz1bnPk9xoQxqiniGd_7OuX4s19Lp-AU7AE4Y-k1MetCTPaIF6mVjuulnjq9NHM2Tocybs3pHCEiR_3cwSN9P3JvoLeBWJV00tLoZB92d9X_F044yWIs6kS-tWihTZMIdF6aKx1jynvQz-gRpaWnIGi2fgmb5BKq_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بریم واس شش گانه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/83066" target="_blank">📅 17:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83065">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKV3Rc7ptvUXicNhqTehBCI1snA9ZKDNB-Ae_-YmV2olx_7gA_gaMnScWvh9wz9Ykc0nbxW6Uw02JFLv35TP4i_SVS0HN1YXU_VCfZMIz9niXLfrMuCxZMPAk1N4shWibmFzZs1mSM74vusZQGyhUO_BCdsejg1QO-Q0RIYil_PTYSCys8lsNYP_oq03yXLNRYj5Nzqf_jk1G1pVcb5u2WpaUpM6r7ROsRSYHcXrqHMVXFzYuJba6sKS3csQDhnIDEwWXucf7ZmEyYSFK0pOS-GUHopK2ryjJmzks7kq-Y5_IZKZQ6SQdC4OMdEEHykvEeA51_-TUuHV7SwZ3bCAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به هیچ عنوان برا تازه کارا ساخته نشده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/83065" target="_blank">📅 17:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83063">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuKj6t_cf6zzTC0sWNOy7hGF3UokSvitdbLxv-Jqfy-ut7xI-4oD7uohdI5Y3k4urPe2XElKSNnZKpHtgxXOJEOjgkXIR0rKr6v1UCdCOD6pk6a6utUC2GRy21hrG8R_5UBSmRZmdXSkqcMUFqzO4ZamgDpCUwE1VnRKSijBGmPT271PFwJnzu-NdiQSj_zhs3Cik4pZBfLbjNxAq0T7Us-BOk7onKJNeR4_TVr8aTe_XiFLrz4lGu4ka0-p9ljBrukeQSuLrIukF42odFuibUUzAWFquelwrRzI_99HcJahC_uuwK5iTUZb92In7oOizNbwi3uTbQNfPr8pLuyzoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ff0e768cc.mp4?token=azuuZVbtnIELwaSTpbN-7Dj3gRfBE31h68zGFOL9j5h0GYBxpoIKHLBEN_FtmBfO5vmX-JVQI5l1G74rSbo1j65M1cYRZiOEui3ukwt_kxSGv8e_QSG35jsLM_JD0Y01kaQTZwlUgkpHonNZFLZI9sS2pZmR44uGuEUV6GtVYP9t0fnFLNezNoxUPYwAmgLGMkmPJTiXVn8iQzF_rTPnz1iw8zNUcNxH_VQ5EJnM5zO2fvmldIfyjF_zZOp_qc1gyK78fe4R-OWJm8UnlWWRm1etI4qES1jxv5utfOvJCiCUvIYBcPH0HC47dYMhLElYbwpc8a1r1opTyORy_0smyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ff0e768cc.mp4?token=azuuZVbtnIELwaSTpbN-7Dj3gRfBE31h68zGFOL9j5h0GYBxpoIKHLBEN_FtmBfO5vmX-JVQI5l1G74rSbo1j65M1cYRZiOEui3ukwt_kxSGv8e_QSG35jsLM_JD0Y01kaQTZwlUgkpHonNZFLZI9sS2pZmR44uGuEUV6GtVYP9t0fnFLNezNoxUPYwAmgLGMkmPJTiXVn8iQzF_rTPnz1iw8zNUcNxH_VQ5EJnM5zO2fvmldIfyjF_zZOp_qc1gyK78fe4R-OWJm8UnlWWRm1etI4qES1jxv5utfOvJCiCUvIYBcPH0HC47dYMhLElYbwpc8a1r1opTyORy_0smyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی عشق ابدی براتون رپ خونده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/83063" target="_blank">📅 17:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83062">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ساندی‌تایمز: دو تا آپارتمان پنت‌هاوس لوکس تو پلاک 3a Palace Green لندن (منطقه کنزینگتون) که برای مجتبی خامنه‌ای هستن به فروش گذاشته شدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/83062" target="_blank">📅 16:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83061">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">با گوشیاتون تو شارژ کار نکنید که وضعیت بگاییه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/83061" target="_blank">📅 16:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83060">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b309c1c56.mp4?token=ks1qYYFZ4YAImxwe4Wv6GQciZSgs_enKOs-unbGwrqhLdAn3Pn3D5FEjky3sbXCrLL7SnlJ5boHOs5hfPFnIAd8cNUS0-wP8rSCaZXmtGstqtclyiqDUKLf_-YzqIlfLddoulKG322Q_ZUL_sgSzcGM3X0by_HSJoTyX86fQxdAUG8klgP8yjy0gXOYfkh1OcGi_qQDPfsV7C_5u-c_m38rqPI8g5wFydvoLZRVaAAoyTRpPqXjdnD35XmbD1dZjVBPrs55WBPFMP45bFUlOLmlW2QhebrQI744qiqpCpKgefMzmWziHjw8dnnGt8MOi6PUeHi7ZBCIW4nT_gnl14w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b309c1c56.mp4?token=ks1qYYFZ4YAImxwe4Wv6GQciZSgs_enKOs-unbGwrqhLdAn3Pn3D5FEjky3sbXCrLL7SnlJ5boHOs5hfPFnIAd8cNUS0-wP8rSCaZXmtGstqtclyiqDUKLf_-YzqIlfLddoulKG322Q_ZUL_sgSzcGM3X0by_HSJoTyX86fQxdAUG8klgP8yjy0gXOYfkh1OcGi_qQDPfsV7C_5u-c_m38rqPI8g5wFydvoLZRVaAAoyTRpPqXjdnD35XmbD1dZjVBPrs55WBPFMP45bFUlOLmlW2QhebrQI744qiqpCpKgefMzmWziHjw8dnnGt8MOi6PUeHi7ZBCIW4nT_gnl14w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک به قصد پاره کردن کون اوبر، تاکسی های خودران تسلا رو به بازار عرضه کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/83060" target="_blank">📅 14:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83059">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYU9vOzKIhQGObRKK41jt4QffUw56g40v26mSAfVgX8LU8nTgqXm3FbYPIpdzDnqNwLGGUa3Q_ZfCmf0lfmvDchZLorEBdb7pz1EqJYThnv1Bm32jz602ZksAgeUECPEAj_TUcabI6F628TIv8-L3OLfFtnSB3d1-8TumCKWMUJa_tDuGF5o-DkT-qyiOlxukGEF2eLJkdxNZVsAqsofybCsvJP_HiEwzO63J5LBnFAv_VcdyQVNQjgtrIijqa3YlAkoZQcQfh0Hw_btpWOEBn73jwCn5lCOBAyScwVsbAyTl-BaieX8RkmrFl5u1zK64y3fs3SULhQBLDTq9XA3GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادمینای خبرگزاری فارس واقعا سطح طنز بالایی دارن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83059" target="_blank">📅 13:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83058">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دلار شد ۲۳۰
ایرانخودرو هم اعلام کرده میخواد کصشراشو گرون کنه
عالیه وضعیت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83058" target="_blank">📅 11:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83057">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLcQHDz9EajinsXF23iED2F-M-nOxMR3e7WTR62asvvz-kKqafNp_DolLWbVquY6T_A10flEPw6W97dvgHKbdY3eTlv-qvGHYMfksw0sjJX8jhg9eJUPOcoNQHoq43HZyZNsL61eKpkKrw8_dSzUFGJ57pzMCE-4lyYfnW6ZIkLA5o4GMVojP-UZILX7vr19liZAEpTACFVN3xMugzDIbqHXKMbd_g1ykdZCxm8lHSNcqOrAJmae_1rUYlNfLfqfZv8BumxHoCd7vcN3kLL8v1hwS03yR6f-224kFG02GbFvhIgxmfwp8JC5OfavQFPHl4uO2ywTIkh53Zmmfify1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردن نگرفتن همیشه از صفات بارز کیم جونگ اون بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83057" target="_blank">📅 10:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83056">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-U7mGuz_XwvbxQoS79f9G_cuXe3pQgSaqc0K4fefmbTItNkz3H3rpy7AG9DJkDRAD4xu8zTW7VJWSFvUWVIPmcbDBFPmh99a_gvJFnTN3sSfHUlN6ezEpqn-JDt1D1ngAbd3Yb0FWpqvs9cJwr6y-bFHSbtyPGfX_jQaphOYx7NMxQFJuKTDVuhKXTzlkPj1EGBLOSCkrya8Qd1aMduxxI2LArW6zNVXYud8JsnIa2Aqx2TIYf6ambx6I0CJc0W0gS-EyuDIScWao-HmSYni5zwEwnLq0eJDmyPePlR_u5dmYnjE4oMl1dLEezaQIGkjaQXwjiXoXO0WyCvd5XC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
آرسنال
🏴
-
🏴
چلسی
🏆
لیگ برتر انگلیس
🏴
🕔
یکشنبه ساعت ۱۹:۰۰
📍
ورزشگاه امارات
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
با بالاترین ضرایب پیش‌بینی
📊
نگاهی به آمار دو تیم:
✅
آرسنال
:
۶ برد، ۲ تساوی و ۲ شکست در ۱۰ بازی اخیر.
✅
چلسی
:
۶ برد، ۱ تساوی و ۳ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر آرسنال: ۲.۹ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر چلسی: ۴.۴ گل در هر بازی.
🧠
آرامش ذهن، دقیق‌ترین ابزار تحلیل است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r15
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83056" target="_blank">📅 10:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83055">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dba858a3ad.mp4?token=F-0vOvhYVlCbEc3fjw__l6cCyHVWURqZhHXtYJ0NKxOPIQw68sgsIysZNVZVGqu4JBGOEbkTAicdi3cksZfFBWGqc0HpFrB-qZasaQwF9p-ZrDnNpAfEQhGr_vWCw4Y4ZDbOcyMCw4_31y7xaXJ3XNv1Xfxt4jkwBd-3aOfiXPnAOuR9NPu1h9lK-nzjr1kdUOIahniyZIh3ajn1NMB_DkhvMG4bK5tH-zA26RwctqiyrY0qwCfH9Zsl0qmnPWhRD1EHBTtifJbW1YO4vDImsHcz9lPoKngLziWveYoblzn6qy3Ngm8oQUGqODW0ENDALxJadv3sgm3ph7hw9_KjtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dba858a3ad.mp4?token=F-0vOvhYVlCbEc3fjw__l6cCyHVWURqZhHXtYJ0NKxOPIQw68sgsIysZNVZVGqu4JBGOEbkTAicdi3cksZfFBWGqc0HpFrB-qZasaQwF9p-ZrDnNpAfEQhGr_vWCw4Y4ZDbOcyMCw4_31y7xaXJ3XNv1Xfxt4jkwBd-3aOfiXPnAOuR9NPu1h9lK-nzjr1kdUOIahniyZIh3ajn1NMB_DkhvMG4bK5tH-zA26RwctqiyrY0qwCfH9Zsl0qmnPWhRD1EHBTtifJbW1YO4vDImsHcz9lPoKngLziWveYoblzn6qy3Ngm8oQUGqODW0ENDALxJadv3sgm3ph7hw9_KjtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بابک زنجانی یه ربات هوش مصنوعی ساخته بعد تو یه حالت مثلا ما خریم یکیو گذاشته با کنترل کنترلش میکنه، یعنی در اصل اصلا ربات نیست و اسباب بازیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83055" target="_blank">📅 10:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83054">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/funhiphop/83054" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فحشای خداداد عزیزی به امید عالیشاه.
کصکش پا پرانتزی
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83054" target="_blank">📅 00:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83053">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">قالیباف: بستن تنگه هرمز به ضرر ایران شد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83053" target="_blank">📅 00:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83052">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اگه میخواید عمق فاجعه رو بفهمید باید بهتون بگم که قیمت دلار داره دو برابر قد کاگان میشه در حالی که پارسال همین موقع کاگان ازش بلند تر بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83052" target="_blank">📅 23:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83050">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bZw6Kt63hp-pL43cAJ109jgFz7b-KqCK0w2BVnUFkqLaYADh0xiDK0YFtJtSxuDnsWSO4k5T-mGSNKPzpio0uU_W8nb3CYf32Jjt7Wpr0PEOzbXDO4bKSpJbex8I1aKzrZVXzEAm-HjIztaYsf7m1oqmuZtlawXHqFX-uDjYy-tWGYztFG68LLckrdaKS0cl0xOkm5-AcqfAdZHSV9uymHAgt2CtNIRAq8IEIl5Qr_k9Fj0ZR18YDcXr5RpBCUIWNdlSNgpxiGNX4Jw1WnA9IYOnKjt99WFBFMQngFIgpvmeZaJv7600GRvxHH1WaY9hRIYU0eNfugzRj_H9e6SqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUybRPYMc7-kvmg-Dygb_ZmVTmUgJM7eYv3KYg6WU44BNDxJg1GpQjokcE6r1xYHq9dDpZSq7iV6ypL8djSnXCTHUh-QCmge3oCxVliX7yFLY79KC35dW0mLGqFrzXe2GhxpVIgKpfMNVYDoGH2Be6q_dPTuYD4iOc3plhCukHu6o6Vi7AocaDwvleP8Vj-fn4I5Tr87PMvTY21DLud00SX3v8perySDoB7Wl3YQHNXGNdEJwbIMXtxdoRnqHB5E5o84ZFTFPhRoH1JTog8dR23hVMGU3st4QLssKx-5ZsUisn796FbPqUoCR0Ox_8rVjX0z_sLBu3c3koXj1hSkag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین تی‌ام و سجاد شاهی دقیقا تو کدوم زمینه یکن که دارن سر اون یک بودنه باهم دعوا میکنن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83050" target="_blank">📅 23:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83049">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">درگیری بین نیرو های انصارلله و نیرو های دولت یمن رخ داده از اون طرفم شبه نظامیای تحت حمایت امارات ریختن دارن حوثی هارو قیچی میکنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83049" target="_blank">📅 23:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83047">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رم عجب تیم سکسی ایه</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83047" target="_blank">📅 22:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83046">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">همین الان برق ما رفت
وزیر نیرو : خاموشی‌ های برنامه‌ ریزی شده دیگه تموم شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83046" target="_blank">📅 21:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83045">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔖
ایونت دو برابری (Double Gig) فعال شد
#⃣
با کمترین قیمت بازار، این چند روز هر چقدر حجم بخرید ۲ برابر تحویل می‌گیرید:
❤️‍🔥
10 گیگ بخرید
💎
20 گیگ تحویل می‌گیرید 20 گیگ بخرید
💎
40 گیگ تحویل می‌گیرید
❤️
سرور اختصاصی، پرسرعت و پایدار فرصت ایونت محدوده، برای دریافت…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83045" target="_blank">📅 21:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83044">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پویا رحمانی فایتر کار درست و مردمی حریفش مالیخین رو تو سازمان کشتی RAF شکست داد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83044" target="_blank">📅 20:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83043">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtXjULyp3SGsFn2EbJGa542A_itP3wFnKUitphrOjiWkA0mVK-juPzl8W3imp1WwzTEZCykEIzO-JpoDZku_ng_n1keulvBg6dnKZsWoO41s4vUwtYdNR5eK8J0jEjqaRPw3F4FYp0-G57CecG5JczgQ3-hZSwh5jhYq4cUpkIqKXhLV3GI5q93jUvMhiy_OUrs3Q9MHnADJnEr4ChCxNc0n1fAQbbtPh7o8zw6btFEd-LhsE_Bc-YZPCH65cAUTbgBiByx26z10vYeInyeUzIuIHHZNqqqJ-9bWm477dTtdtJ6E8bqXqWqjXdfxIhsAKj5mCzZQ50MFphMTeOD8oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پویا رحمانی فایتر کار درست و مردمی حریفش مالیخین رو تو سازمان کشتی RAF شکست داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83043" target="_blank">📅 20:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83042">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دلار از تعداد ممبرا بیشتر شد که
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83042" target="_blank">📅 20:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83039">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nz_VfakHICriXDLQx1jngZgYbSgTd0yqcUqT1vYMzFdZkplrkITGE7Jn5OGueURMqhwrFas3Ym8r92Nb2tvTSbc7N6HDh9xA7M0TK0jWqCyBB8wqHV5dt8bRokcVLmrYMlgcqOsvFrAqGke5pm8g-gJPFTEiCOw8WdZxOF3fnRkBsW-_wWAVTQDwsCEQ_Xy1Kte0CHGvFUrhBWR6Zz3XnY4fznmEmepiKrxQnIBJ26hzeleYNDh6taBKP-sfvLBDgDNd5-1oKtVLG_nXO2R-s1s4rlJyTSpvO_nOZjChNMfZmB9Uftgy9n2ricRucnJHcXTb44ZU9H8_s4jJNBTi8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkSs-stAyEBisIrV5NvpWJxGJ2YI8zk15JIz3trClCvFLOJiEtL9aFTJQerzA7V9SfCAYYoYKpZv-MxUJen8uFXo76I8nG51MynGvyYhcty4ls7QxE0-CkyACiboyHjZcx1tU6OImoFcGJBCcsN9iEL1kVhkjC3B0oMprhDYi6DHd3ZN9Ze2QlEjbfBqmQTpnewev2WraLc5jVe54kag85dBjF5uM8K7tloaA-jCuRIoBfNZ-ufnIvbQPq6qTNGOcHwHtEbUnDS4X4cs459CX3bJVN4PYTFBlxakLfLZneXHjR7wGZ78_whACDAJ1RrShhIfoaNkNKgYpCZkxKB0Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q-q10t5kLAoknz852aVuyIS6b4CaIWx9m8_kpo1OGGpyXJlLKMpCJ8ASIqLeHt3ljffsOAnA6kbQ3EFwBVvdfOGX4zbIwTpfz_VKbOrHUnZnAx-fqGnGf9q82c1ZJS6g853IqeuvK8Jjg5PgCT2xOn6_5JDbVErk4dgFWKcysIlbGarlXTtZuZO2NeXbaV2XLEihPwRr4pROsComfff-PrIokpXXgpeVmZY7bVjJSyu2aWuH0nK_9rptdYFMKVXRVPAhoMOgl9yJg11FlneqwwsNhOQU7vgRWK4zC81cnNqofyFPqv_eXCsKHvamlDJToOPt9QmRX57pCGHRJ9nWyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تبریک به فوت فیتیشا
ترند جدید توییتر اینه که دخترا عکس لاک پاهاشونو میزارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83039" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83037">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔖
ایونت دو برابری (Double Gig) فعال شد
#⃣
با کمترین قیمت بازار، این چند روز هر چقدر حجم بخرید ۲ برابر تحویل می‌گیرید:
❤️‍🔥
10 گیگ بخرید
💎
20 گیگ تحویل می‌گیرید
20 گیگ بخرید
💎
40 گیگ تحویل می‌گیرید
❤️
سرور اختصاصی، پرسرعت و پایدار
فرصت ایونت محدوده، برای دریافت سرور تست و خرید وارد ربات بشید
🤍
🐶
@MaMLiNeT_Bot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83037" target="_blank">📅 20:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83036">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b8b1d6558.mp4?token=XgIxKjOMDK9GqFRgyCubpVymXorwDFkd6Ca9gyO25QGx3ENPO5l0_F_JtO7z8lWe0xdmmAEG0xv8ylTENv8kRFEBT4F7RTMTEoq-qpH99oUs1W6CFmK92PYZTNK4fhyV4LA03P8ex7OdF6b4rAwioGSphOTtx3LIjfCAvq29hjYzd7rYDNaz637SVsCeJhE3lZMjtENM0CnVuhYLIGw1E1tvQVtuCvCjIm3yb-uwwDVbZUn_ftYpjLnBcUahL9ZVpPJ0JS6G0Hny0_6j-BKzVti-99cOxYrDeZjYxbmGRv56D_NUYr-WOE_Owp5udJTNw7n-vqjOf5zi9dLzIsRXOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b8b1d6558.mp4?token=XgIxKjOMDK9GqFRgyCubpVymXorwDFkd6Ca9gyO25QGx3ENPO5l0_F_JtO7z8lWe0xdmmAEG0xv8ylTENv8kRFEBT4F7RTMTEoq-qpH99oUs1W6CFmK92PYZTNK4fhyV4LA03P8ex7OdF6b4rAwioGSphOTtx3LIjfCAvq29hjYzd7rYDNaz637SVsCeJhE3lZMjtENM0CnVuhYLIGw1E1tvQVtuCvCjIm3yb-uwwDVbZUn_ftYpjLnBcUahL9ZVpPJ0JS6G0Hny0_6j-BKzVti-99cOxYrDeZjYxbmGRv56D_NUYr-WOE_Owp5udJTNw7n-vqjOf5zi9dLzIsRXOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بیناموس این بمب اتمو کی میزنی راحت شیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83036" target="_blank">📅 19:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83035">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تاتنهام کصشر ترین تیم فوتبال تاریخه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83035" target="_blank">📅 19:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83034">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حاجی یه سر داروخونه برید قیمتارو ببینید دیگه خایه نمیکنید سرما بخورید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83034" target="_blank">📅 18:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83033">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNpmv5Z3KEFGU9CxvM23SKM5xMV4Rugh5Op18SebD9QvmCERVwf0x1a6u2dWz5UGiJrF3VeXCt2XudQQApjIC98wdRlDNLdzafdqOU9W9h0lUwxD-3XeErY30KqXwyenZCHm4lK9I9r83bePOOvqf8yPGExevn4XbeJ8N0OtmT8HAhQlR0FZVl1q-uw98tT_mt-wLm9loopDVgGtMD_NtjB_fn1_v-4NQCzBEqJgThWTfsrbawYQ_WkTje3FBloJB03pofm3X3V0x4_wXVmHdwS3OdJb7nn6fOtsTyWatGZI_PplU8d87o95qeGDeQN-CusHgt60bT0rs_o-4DzoOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا منو بک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83033" target="_blank">📅 18:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83032">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaso8WEv17ZblO8OP6VAUkkBF2BMVzkvc5yyWn_ezFdMrVXkJfPU6hl5kY4lH1_jqrTWE5y9Q8HscF00ZzHk1kr8M7OIWXinmkqqfSiwFgpTZPAZ-bfAZ9FWhsBjCmmaBWJl8KunEybbQWE-UHmPZ05ZxOHNRMKfh9-U6w3DeV5TfN3sOuPvnMl-4h4rJWQFXGdkpUPMbNIvTORuUFm49G3nPYAydZ3RE0JmFnSZgHLVoXBqbHLcH5fo_DR6w0jCc4cEWteYEKEfDro8exAxrx22MhaP3KODUGhVb1SmaGNbF6A6HjGxmIeK5zR7F7beCA9KOgy1rCPFDGfCINNKLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
صد درصد بیمه ویژه پیش‌بینی لیگ برتر خلیج فارس
🇮🇷
⚽️
با ثبت حداقل ۵ میلیون ریال پیش‌بینی میکس بر روی رقابت‌‌های جذاب و تماشایی لیگ برتر خلیج فارس ایران، در صورت ناموفق شدن نتیجه، بت‌‌فوروارد در هر روز از رقابت‌های لیگ، ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PERG100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g14
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/83032" target="_blank">📅 18:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83031">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دالی  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/83031" target="_blank">📅 18:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83030">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گیمرا قراره به آرزوتون برسید، شایعاتی پخش شده که میگن تو GTA VI سیستم قطع عضو اجرا شده، مثلا با شاتگان به سر یکی شلیک کنی کلش میپاچه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83030" target="_blank">📅 18:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83029">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1d45c18d.mp4?token=ZEscLC6LcheHqYg_0rSdGjPtEW-WBr4B7QTAZu7IAyEQwuzSHI9DH5uskTXzXhFKUNecobCl3q4iQr9bLSIStsYYPwF7Mul8er0xHd_AigNyQsnOB8ll2SYK7s-uUKiQUeHHHUsvQwWkRHSg6kAgDya0850KVI6krOUMio8xj0MsSSmnc1XH55euKAD1rHkic8tzhCJc5CmYBgvvSmXa2JLgvIXCChfgaxqpcNGxpcNMc2TUeDty32Z_Y-MQvbmZ0oPFnSHDMUe0AGYUsrRvIUElNJyzGs1JyAnp9hh9uSCd_itD2dDIWnFDF1SgJDPaNliP5cLECoBSOQ8vaRHZ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1d45c18d.mp4?token=ZEscLC6LcheHqYg_0rSdGjPtEW-WBr4B7QTAZu7IAyEQwuzSHI9DH5uskTXzXhFKUNecobCl3q4iQr9bLSIStsYYPwF7Mul8er0xHd_AigNyQsnOB8ll2SYK7s-uUKiQUeHHHUsvQwWkRHSg6kAgDya0850KVI6krOUMio8xj0MsSSmnc1XH55euKAD1rHkic8tzhCJc5CmYBgvvSmXa2JLgvIXCChfgaxqpcNGxpcNMc2TUeDty32Z_Y-MQvbmZ0oPFnSHDMUe0AGYUsrRvIUElNJyzGs1JyAnp9hh9uSCd_itD2dDIWnFDF1SgJDPaNliP5cLECoBSOQ8vaRHZ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اژه‌ای به هند سفر کرده و مورد استقبال مردم هند قرار گرفته که یکیشونم رفت و دستشو بوسید‌
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83029" target="_blank">📅 17:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83028">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام "ترور"منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83028" target="_blank">📅 17:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83027">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPhOEQFgrGZ_4_r1vz6WmQO5wH5kqJ0ep_0YJWv3ICT5JsKmReNtaoThlK6A92-gblJPKKR0I82nfb2s7IN9KK2ANqmlLTggQ5uaci5C31hl8pEVX7RZHRdPxa0wWnwzZbeOZH7Bc48LprsRxOBccBwayW9pI46mSBXVUJXSC1lPqJTUV1C0rApY4abZsB9FlJtmhe3Eunvr03d9raJVvHr5jdsrGipdmbK6xtm1beCEf7Ze99htYqd7iUF8QuqHq0hwYhUVPtlIInoakDFupn8nzFnZyg5jvCeoPKBHlsy-aoDMq6zVoiQHaKdJvHjG9QkEp-ZGb7IlEaN4J1ERCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام "ترور"منتشر شد.
Youtub
e
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83027" target="_blank">📅 17:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83026">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پسر میدونی چیه مملکت از همش عجیب تره، خبرگذاری های یه کشور با فاصله هزاران کیلومتری از ایران بیشتر از آینده اقتصادیمون خبر دارن تا خبرگذاری های داخل کشور خودمون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83026" target="_blank">📅 16:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83025">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuKZ3i-lUlRd12DPpxsoH15H0GxKUsfQDBuxNE3zDOVAH96NJME120cVxNk-Kyw45XxVYGx6P3lUaoAcPMleqWSRLHf9hfqY_6VEfD-8tjosERa6p93qScwbwS4vgpg5PAl8VoJEAR7_ucyS29CNPLYsVr5TneDr0rUjiB8WKa_hIOn0Er3Dt7qRsUgSBAPpdC3r3E-NAKxVmlIytGcGORkhwnPURzYUlLuD2i38p8Ss91ch_EGtIfQjn7ugC3X5HQKiWh_n2BPQze4oV6CedddS1GR-RXUT6s052hx3TM3noUd5pxlSqc4hG1uLA80ycDDZ7xuxdVN4cF6YhOq6Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محکومیت دیدی بازهم کاهش یافته و حالا ۱۵روز زودتر و در تاریخ ۵ فوریه ۲۰۲۸ آزاد می‌شه
دیدی پارسال از حبس ابد تبرئه شده بود و به جای ۲۰ سال، به ۴ سال و ۲ ماه زندان محکوم شده بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83025" target="_blank">📅 16:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83024">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Az6sGdNmyd1cmbFjKcvks8LoHdfAqXHZF-QDNIJnIstM4oj9gUwLW0HTKGHChTCE89k5JceDF985R-Md0LDj15KFCQh6UO8Mfd8SU_5nKvE9H7yeonrV6U0fx3G5LrSGP6JaZ1lJStT5PncCiIppHHCczDS9NStoc4mg5xaqQgsPJw5X50pzGoJqepgKjqP24lm3i4qUk_WQw6OPWNYw3JcZEO8I468bY0DehP4bVncE9IXV486MThGSKDy305tyNIORGofcHsi8hVCMBF8HFrE0upGskCrA4oi3IwO3gRHSZz95opXIPp7D_JCeLArh1UgdkKVSf9CAyrT-NSAlkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83024" target="_blank">📅 15:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83023">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">به مناسبت 200k شدن دلار بهش لوح طلایی ندادن؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83023" target="_blank">📅 15:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83022">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KANTNE2CwfPMBHyP0oZlk_QEWtOfEfrnWqKYyeAEzCR-14I-Rm6tqlYxA7JVaMfNtkPhNhevlMU4xDTMDZWfS8DmZb_tIZarmxUnZjLK5pGUQS3ZtRnFItLt9kMfs26rgwzusA8UQZflCAVBuxAcHrlHgSMfpOsz2mgnyIStI_OtAp8wma8I6eKmdLU0hUuOq7DJNnnDNmnxQ2VU3AMW3cvQPVTZJ1VSu7_Op4PBhUO2qyPiwd-Gv5hopGViXdbRcOxiT7a54WMn7UrhabZkkimrlgKDda7CRfq1CXPDfq5NwI_ZsMn4P1zX50HJfatqEyfEF4hZieaEZ6o-rLMMgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83022" target="_blank">📅 15:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83021">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">البته در نهایت این دختره کفشه رو خرید و به آرزوش رسید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83021" target="_blank">📅 15:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83020">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8CUHue5CZ-fSgdMVqN4Yjv0CIQCsOT7lW2ijk82SMo6fbWJRTr08-Y_uI4hx5kIOrZ5vCc9wwX1-woVWmn8OjdP7s5M0Y2AN5r_h-ahmNEKk_TUEqjjs2XB9AfN_I2PghUjYb-GoMB3rjCeBG3SG8vYXeQcn8rDr_qKSf5C7dU2_M0CVeY2T3xb3aYZjCtl53Hu9IkSx0EDq007nE_cOBrlDhxobij7bSGG78-XMyPKW3MmcxtgwbPej_sHjnEwN4zV88bRxpCndbev2rWlbEvIDUkb2n3dGF9qRTLuymoJ7KYNSQrne3nC_w30itoCPOzwwO9P5Y_TEYEkK2JcZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو این خانم از دیروزه حسابی وایرال شده؛ داستان از این قراره که ایشون واسه خرید یه کفش به قیمت 14 میلیون حسابی برنامه‌ریزی مالی کرده بود ولی بعد افزایش قیمت‌ها، کفشه به 19 میلیون تومن رسیده!  اینم دیگه طاقت نیاورد و پشت فرمون زد زیر گریه  @FunHipHop | چمن…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83020" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83019">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd895d17e.mp4?token=qnJSdxNW3swBwyIxmqNmQqb8fp0XcGkaiyuzu1HsVdJA7Il6jBgL9DwhRh7zvDQPQgGsoHUOpKFnEdKtDIet-tyo70dHSO8jICiSTRKsh1x7JyITOnqO97DeMV8joHw9Q3MrhAha0Nua0K_Wqk3MKE77D_1S8IOQcyxRUnUbmwZ21OG2QB62yU8FBNoCN3dkSm7QU_bz5VS3G5O7aMnpDw35ZiDC4LoK-aavyonBgA6QSjCnHToBZ_sw7UL5nNqaioxyRzuVd5eJh7tDcWCqlho7q4w56nDfFfVnGN39llDO-c14e8-e0akEGxEvOfq4GwT5E6XG2qVSORWzbzv_yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd895d17e.mp4?token=qnJSdxNW3swBwyIxmqNmQqb8fp0XcGkaiyuzu1HsVdJA7Il6jBgL9DwhRh7zvDQPQgGsoHUOpKFnEdKtDIet-tyo70dHSO8jICiSTRKsh1x7JyITOnqO97DeMV8joHw9Q3MrhAha0Nua0K_Wqk3MKE77D_1S8IOQcyxRUnUbmwZ21OG2QB62yU8FBNoCN3dkSm7QU_bz5VS3G5O7aMnpDw35ZiDC4LoK-aavyonBgA6QSjCnHToBZ_sw7UL5nNqaioxyRzuVd5eJh7tDcWCqlho7q4w56nDfFfVnGN39llDO-c14e8-e0akEGxEvOfq4GwT5E6XG2qVSORWzbzv_yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو این خانم از دیروزه حسابی وایرال شده؛
داستان از این قراره که ایشون واسه خرید یه کفش به قیمت 14 میلیون حسابی برنامه‌ریزی مالی کرده بود ولی بعد افزایش قیمت‌ها، کفشه به 19 میلیون تومن رسیده!
اینم دیگه طاقت نیاورد و پشت فرمون زد زیر گریه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83019" target="_blank">📅 14:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83018">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7770ac79f.mp4?token=GjFqrgqOYS9f5c90QaSMqi0p1NiuGnhlCpBt2Kthv5SIIKYnTk8XWnHfhmsnJXmM3bFGS1CyIwInQzY_4AOmHvEVo-rSJqaEkrnj_jluhSTAt84P9DcbgnbhLk7K8QeET-d5X3q2OTEQBoX_TgBTX88bxHyep-pgrQMGScZA3Y5blcavUjvyARFHdSPQNM7-PCFLOIMX6r9r8y803x3zAv4uXmWLWdFKFyNI7pg6q65uXFVEa6LC1iUx5ZrAk_fHwshfeUgiqq8maz4Z7G4xPrs_HqEfgCq9UNo5_8t3rmI555OmVLozL2pO0bUjc4TUxmssejeQaIdOCW4mKcY-3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7770ac79f.mp4?token=GjFqrgqOYS9f5c90QaSMqi0p1NiuGnhlCpBt2Kthv5SIIKYnTk8XWnHfhmsnJXmM3bFGS1CyIwInQzY_4AOmHvEVo-rSJqaEkrnj_jluhSTAt84P9DcbgnbhLk7K8QeET-d5X3q2OTEQBoX_TgBTX88bxHyep-pgrQMGScZA3Y5blcavUjvyARFHdSPQNM7-PCFLOIMX6r9r8y803x3zAv4uXmWLWdFKFyNI7pg6q65uXFVEa6LC1iUx5ZrAk_fHwshfeUgiqq8maz4Z7G4xPrs_HqEfgCq9UNo5_8t3rmI555OmVLozL2pO0bUjc4TUxmssejeQaIdOCW4mKcY-3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوزجان بیلان یکی از میلیاردهای ترکیه‌ای و مدیرعامل شرکت موسیقی «Muzikonair» امروز وارد ارومیه شد و قرارداد همکاری خودش رو با امیرمحمد امضا کرد.
طبق قرارداد، این پسر به همراه این شرکت مسیر جدیدی از زندگیش رو شروع کرده و قراره برنامه‌های زیادی خارج از ایران انجام بده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83018" target="_blank">📅 13:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83017">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUT5PWmL0DRv12uvY7ER-ltlXh19U29tQHyHuWg4kcSSBK-7NxklAADjH9wlktaicSACa21O_GZBbnSut5U7nHYgW7pXF_8dIgt4stKeWuJx-c_CZRsBGMbSkLPRnz0ScoXjvR4fNAqLKheO3JOn8HktyYZn4mX8P-Pb7ZAc-KURFfrRw3ixiOOs4KaPpdBTRRGJX4y-rbbSSyAeT-zPoPNF5tNKhFdBYAdY96re0GLvTIPOliEfscxgQBAWNIc9PSHc3aA8Weku5SA-bjFyHKKYPLNS2R9QtEyCR-y7rcsRgk-sCSFuTB-ZOXitXBUpeZeETRC5tsSLzjLsdQKCig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
صد درصد بیمه ویژه پیش‌بینی لیگ برتر خلیج فارس
🇮🇷
⚽️
با ثبت حداقل ۵ میلیون ریال پیش‌بینی میکس بر روی رقابت‌‌های جذاب و تماشایی لیگ برتر خلیج فارس ایران، در صورت ناموفق شدن نتیجه، بت‌‌فوروارد در هر روز از رقابت‌های لیگ، ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PERG100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r14
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83017" target="_blank">📅 13:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83016">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دلار نزدیک 230.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83016" target="_blank">📅 13:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83015">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOSWsC3yqbQ7EEdxraaSzON5P9827oCN_TQMyP3dzOpZvKn2P82ezJ10hq-OIv-Ra9dNMhWEV5mSGe32wzPJSFbFX7vX0LuzilhtOqxMDyxpBDCUuttCtNjNXViPLhpVVcm63seHAWFfP1eK1O4xk8JKNgedoqKHewiC_xb8r6rDAk-RGRb8Z9obxxWohJfkfTFlmuIRS2F9lwcxr-MQ_UMN39LUNWMuXCc6dZgof9iYd88LBpG1eEyhGR_z7ZCksMVYY_ETTGmLYP_bSuuHZ1UEygRs4cwGlyt1aPihQc753FxaKDRxzltoJ7sC7J9GMz7gxTE8W2FWVbuyuQ34KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیبارو سفت بچسبید شاه‌دزدای اصلی دارن میان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83015" target="_blank">📅 09:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83014">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">چرا هر شهر کوچیکی میری اسمش پاریس کوچولو عه، بخدا دنیا شهر های دیگه ای هم داره، یکم تنوع بدید مثلا یجارو بزارید لندن کوچولو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83014" target="_blank">📅 08:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83013">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ادمین نظرت چیه هیپ هاپو برداری فقد فان رو بزاری بمونه؟</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83013" target="_blank">📅 02:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83012">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16cac9fdec.mp4?token=URwC2Ze5fXbKXgASbrkBA6km8qqNRwcZalk2Ok5jL3eorj0xMXCX8euzYi8xdU7AZCaTvA8EPTrzPIm495aGaW22uB5udji9CaM0J0z1xCBfjRdOoUF9M3kLOVBWXSqD7mwLVJECreQL09DMY6aD3oIe4AKy9nsIL0v7depJnnxxCNTdiigwvMIPbDGkLf9MsFeBpvI_H_1GG4DD_nHjr-GGgOsbPJVbojVW8JH1eNWAyCbsuPIR_tSL5dpNk3MAWZ4pjcXVFk4rY43hBLIruXYI_2yqrSW5WaOdLdv0SKa87Bqz1qohcn2Hh_AiyGgv51Ph6tF9dbmRZyvUvr1EY2gYFdycUch1tq_1Plzseh9HISa3mBom6tla60M9Oz-9anrJ2eVudTL-TYxAGMGOfDIMBu9LLBHQbUyYopVdLTLNg5sfhffw_X_hdKmuJghX5fuyZ5uNr3ANr5efK0dffm61Sn4gutzl4P6Au7n5pDz-f5Mmrq_8Ik0iOh5iBWUOUIZx1xBv7nq2QzeHE-hCAj7do2m_bZQl1QguvFXaYGHQVhCLBqBPodRoAUW6LJstQO-Zo7CBY5I6_S416Pk6GQdtZQiqTnhaXF8Wr9QNlD7x6GeLW5U4N4D7sdfITlS0c3EoVdxP9bQw66AiT7MlO0m866QoT0iNj3BvbPSmmrY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16cac9fdec.mp4?token=URwC2Ze5fXbKXgASbrkBA6km8qqNRwcZalk2Ok5jL3eorj0xMXCX8euzYi8xdU7AZCaTvA8EPTrzPIm495aGaW22uB5udji9CaM0J0z1xCBfjRdOoUF9M3kLOVBWXSqD7mwLVJECreQL09DMY6aD3oIe4AKy9nsIL0v7depJnnxxCNTdiigwvMIPbDGkLf9MsFeBpvI_H_1GG4DD_nHjr-GGgOsbPJVbojVW8JH1eNWAyCbsuPIR_tSL5dpNk3MAWZ4pjcXVFk4rY43hBLIruXYI_2yqrSW5WaOdLdv0SKa87Bqz1qohcn2Hh_AiyGgv51Ph6tF9dbmRZyvUvr1EY2gYFdycUch1tq_1Plzseh9HISa3mBom6tla60M9Oz-9anrJ2eVudTL-TYxAGMGOfDIMBu9LLBHQbUyYopVdLTLNg5sfhffw_X_hdKmuJghX5fuyZ5uNr3ANr5efK0dffm61Sn4gutzl4P6Au7n5pDz-f5Mmrq_8Ik0iOh5iBWUOUIZx1xBv7nq2QzeHE-hCAj7do2m_bZQl1QguvFXaYGHQVhCLBqBPodRoAUW6LJstQO-Zo7CBY5I6_S416Pk6GQdtZQiqTnhaXF8Wr9QNlD7x6GeLW5U4N4D7sdfITlS0c3EoVdxP9bQw66AiT7MlO0m866QoT0iNj3BvbPSmmrY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این یارو زیر یک ثانیه از ناله های پورن استارا تشخیص میده که کی ان، زن و مردم نداره همرو میشناسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83012" target="_blank">📅 02:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83010">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d117c4a49.mp4?token=oXELTR2Q10QR8IQfSmKdpcRwHiDPjPh3HsHE8NM7SAJlngfD4b0ZfFCBi_Ra1XmJgWU6Q1XLeWv_X9xa-zqDWDEeWmI2u4EYqNoy3_bcHuVXu8YEFUv0YcKeGNuExSNCu85cS6y5h5wTPgcu8vef7UsDKrquybBdC7KJOeO81XyKzt0T6DoYBaAKsvtVnKloysX_UZhw-Ue2_uT06bLrGBi082D7jlP1TfRO-XoRzzrDZCkrgxN2JmFxcVzssncR342yYX5LqQQQoZcaxIX4ojpB-CWUJx8IXNK_M4JUBdkRjHPbrb0k8vrjIqvn48W70uEP3TFhMmvIbHVyiFMdLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d117c4a49.mp4?token=oXELTR2Q10QR8IQfSmKdpcRwHiDPjPh3HsHE8NM7SAJlngfD4b0ZfFCBi_Ra1XmJgWU6Q1XLeWv_X9xa-zqDWDEeWmI2u4EYqNoy3_bcHuVXu8YEFUv0YcKeGNuExSNCu85cS6y5h5wTPgcu8vef7UsDKrquybBdC7KJOeO81XyKzt0T6DoYBaAKsvtVnKloysX_UZhw-Ue2_uT06bLrGBi082D7jlP1TfRO-XoRzzrDZCkrgxN2JmFxcVzssncR342yYX5LqQQQoZcaxIX4ojpB-CWUJx8IXNK_M4JUBdkRjHPbrb0k8vrjIqvn48W70uEP3TFhMmvIbHVyiFMdLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نگریرا وقتی میبینه ده ساله از فوتبال خداحافظی کرده ولی هربار که رئال میبازه اون مقصر میشه:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83010" target="_blank">📅 00:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83009">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دوستان رئالی نگران نباشید
از هفته دیگه که رودری به تیم اضافه شه اون موقع رئال واقعی رو میبینید
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83009" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83008">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdTs9cwhecYeq5ZEvHW-8Tr4JU7yPzO-IawHlBJFy9ZGnUuoJJwOsU0n4Bdj-9_UugJcaW7feGd0O1wON7emCH-Qa8zdbkDyKsrQslIA_5zyg4aycKbwk3FcO54CFgtw9L1TVyDUmrNTiNmXUfCm6yzsGvMiDFJTe03mGlpQPdP7PBucEveiu49NWy0HjsruSnmXV4_JmrCZbM2e6m9zL0Zs8Ltb5jX0YWgLHLYuQtx_Rqg3c_cQDtKlDIBrDFFgbXcYI2R2tGt30DM3WcrVNcNMb3W2ex98-MELJqFo4PRPd8cN-D_QfBvDRtbV78q-znxn83TsVIq_jw1oFpiUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چنلای عقب مونده ای که این شات هارو میزارید چنلتون و میگید ترب فلان شد بهمان شد، کصخلا ترب یه فروشگاه نیست صرفا یه واسطه اس که مغازه ها جنس هاشون رو میزارن توش و میفروشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83008" target="_blank">📅 00:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83007">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ولی لاشی با اون صدای بگا رفته هم بهتر خیلیاس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83007" target="_blank">📅 23:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83006">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">امیر تتلو از زندان بیاد بیرون ببینه حسن بابا چه کسشرایی ازش داده بیرون مادرشو میگاد بخدا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83006" target="_blank">📅 23:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83005">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0641a73955.mp4?token=TGkfda_xMXph8hxHPaTyQPO41CH07J6kHLzYVyrbvoBS3C0Wy14rJb3R3bdBbRGGMbeJ1w01DFbpFa97z2-ym8lR3sTb7fKnAFVwz1WsIwUYrIejqjG1FD6kVEE59oDjElz3NkCMxL-6ihL0JmatmVmpui22CG1LI3m6rO85J9he0Stzj52WNF1Hd86r5ARNmS9HQ5xaJFKRlHJs57OsLQS9OttOp58oBgT3_hQBcs6mJgIYAgEZjC0Tr21gJ8Nyrz5c7UxvLPZ0fpfveLtNsbhicz57WnC5-Il49Dm3aa4F2jOCDI0XLxx4FLJmneVmVawYxv3InKHUmdO4VFJm9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0641a73955.mp4?token=TGkfda_xMXph8hxHPaTyQPO41CH07J6kHLzYVyrbvoBS3C0Wy14rJb3R3bdBbRGGMbeJ1w01DFbpFa97z2-ym8lR3sTb7fKnAFVwz1WsIwUYrIejqjG1FD6kVEE59oDjElz3NkCMxL-6ihL0JmatmVmpui22CG1LI3m6rO85J9he0Stzj52WNF1Hd86r5ARNmS9HQ5xaJFKRlHJs57OsLQS9OttOp58oBgT3_hQBcs6mJgIYAgEZjC0Tr21gJ8Nyrz5c7UxvLPZ0fpfveLtNsbhicz57WnC5-Il49Dm3aa4F2jOCDI0XLxx4FLJmneVmVawYxv3InKHUmdO4VFJm9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترند جدید فضای مجازی دنیا چی باشه خوبه؟
شکستن گوشی و تلویزیون هایی که عکس و فیلم نتانیاهو توشه.
حالا پول اون گوشی و تلویزیونا رو کی داده؟ خودشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83005" target="_blank">📅 23:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83004">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CakXGTYwYJnFUQ6d4dpJNz9RLez-MEKc_lCC67qHLq4a6bMlIUfG9so9r5_s6V1s9RIbWmF7pDtHrETROlrbc-qhVAxbkOyPaFY7Y9Yux0hiMajEJB_x4iBF1h485rTcwzfkG0lZAVNAYX_rO9jr84uY7HmymVKyU_qMLdB12j1QEz5tIoq3qs-tPRtmLUAl3uM7jAV6GerwSjDZirerVbCQxghKFuOX3kuQo7VLt1KJIsUwZO3izJY5G51O0tNrlpp1AsM-Lied38icFFocquwTVCmYESXfgkHmdPlP64hRY-Ret56qcZq4VxJLb4NZPhPtYZPAFHLO7J-_eCGeLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا امباپه یک ماشین گلزنی ها اینو گل نکرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83004" target="_blank">📅 23:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83003">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdfYYCdIk3XWdHZKW81E2XKcx921KKd-FUfVVeKqh158DZpKCYIxxk-g5AReaNu8hf8Lo2nYtD-CDkCTz4S328OZZVy41_AmAYOErkTnPuqWvRG8MZY27YB9dOZhwUo3nxyHq59FxxYItqoEtNxWdye4LwQdEVXDbZk4nnwulIkHi0B5mP1hAp-crEd2kIBOol3zRXqqMDWWyvWkHzTeR4ZLjCSJSikkw6PMNfo-Z9y4WScCwCkHaafMVESE7lf8JkMFBecLlCC5-cmYxYKj5oFxOLQ-C281yfCPN0WxXjUA3wW7dJdVoZcHI0W_er2GTNt8CEGaq6Hu2D3j_sGDkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خستم کردید ناموسا، کیرم تو این زندگی که شما میکنید و ازش راضی اید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83003" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83000">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGePCnani-q5wri_wMZMPGuEyRFcBIee3ZsrH60-sPgDy0AizjKY3PPxE8HBZ5DTahT_Cwzw7_2ZOT_jJ0u1bnwDHZ3FlDKYfNQmay_cVn8lEZIgABE1TKd1We1LL2bFERVtSO57Jtfa6AQcwzUpDl9zlefP2CBfd9Sx_vduZxFz4parZw54MQEDFiWoX0lxTAkJKCfo3ZQfSo40C9yXMwfWwnI-YYfrFWBz3q6DZrRWl-5Svb7UnDTtJeWeIVBig-UPc8etvsw2rcLW7Zj62Hl3oRNgAxH9-bda-kRh1Wd0cgq2RBs8zN9wGZjVUTPnlEHtDxS-kxXGf7E8M3LORw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گاس فرینگ تو مراسم اکران فصل دوم سریال جنتلمن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83000" target="_blank">📅 21:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82998">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یا علی اوتیسم  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82998" target="_blank">📅 21:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82997">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cfb0d4b2c.mp4?token=P92zyG5WVaE0dwL4MlQSEOrhmdvUXQkut3Te8CEPDkB-1aRUmI-4j4r6YzFJVVJqelucEJ7tqCCOONg6SxAvg5BKYaZVa7fqTzRTKgELWFSnCKHpUuwWTDzDzwAickQ2VEMw9ePYvMfuizb6i1oaRI2hQz0AsiRKzObKFYRdmh7eG9dMEqxg-RXqaBAiLDM9_mgIjfiyxQFJEiTNvX2fcmRPO0Nl5AzonNwJa69VMNN4WwzXMAwpio-4D68cRVn_Q9WOFrJOHzF6XgREzPz1Rj3yj9pfdEg4xWbjoCOGSm_n8sCnzLUpAzagCwpRR3cpTtGv0oFudaj-nukMTHN7FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cfb0d4b2c.mp4?token=P92zyG5WVaE0dwL4MlQSEOrhmdvUXQkut3Te8CEPDkB-1aRUmI-4j4r6YzFJVVJqelucEJ7tqCCOONg6SxAvg5BKYaZVa7fqTzRTKgELWFSnCKHpUuwWTDzDzwAickQ2VEMw9ePYvMfuizb6i1oaRI2hQz0AsiRKzObKFYRdmh7eG9dMEqxg-RXqaBAiLDM9_mgIjfiyxQFJEiTNvX2fcmRPO0Nl5AzonNwJa69VMNN4WwzXMAwpio-4D68cRVn_Q9WOFrJOHzF6XgREzPz1Rj3yj9pfdEg4xWbjoCOGSm_n8sCnzLUpAzagCwpRR3cpTtGv0oFudaj-nukMTHN7FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا علی اوتیسم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82997" target="_blank">📅 21:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82995">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKCeyBnUySAZlmX08N9l0fTkgQYn2prH16k6spV9uEgsTMsTSvNJViWcP30BNC4RHUXZfAgQ5KgQqZC9_-zD0RGk4n4XJqIWFceJ_YmLiNIpws74ulf5-KoHJviO3H3K9BYepvYkcVRLXZ81xhUpBdY-E8sue1emDD5ZU8qdPbc8vyCCu13HkZIZFMEDXHFfmgMz33MBOC2tJ88iBCR1R2S6j5LNXAP5j9CD9Rl-m2NMPTwlvnSQBay5IwNlBCinNlHO4Qbe35dzeIUOgNUEPX56dMD5pLey2RhNjpg1myN2l56_5JI8Y1prQcy2FWgF68ubxjM42P8fvDTeS4iYVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FMPC9ZgUlCSnH8c5o_VzvgwpfmunfjyqKItDekPm_msKJl2YWEkoTpBGdZsgGsxup5lurr1rJROufF6Vboa2qMeO_Iaxs8v-MPuRqIcH2R5T0nVqdIwfhMinwfet-NkZk35iHu41ooV3eu8rOWqqxQCBGq_CVrzxphc1lIKM-2C-YUd5ahhSJM88KRxpd4heAqVOLJ0bMXDP6fOawWuoEhckjXVIWecQeYc49w__7yTKzXFLSHhe2ZIKsXVAY7ZHDdFb8hTRu9MJAn1VaZZoBj9PPI29C2L2rl89Y5eOCeuX9hjTFxtBOaP5d5NABkK01e50FaxvIjBjHkXXvpKLvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاگان این گیفه رو گردن گرفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82995" target="_blank">📅 21:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82994">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce693d467f.mp4?token=T_YvogKWWO67xPQy9pFWa21lqzGrn6x53Cs28lWpVsY0Yj3r3nvw-fXLJBVgSoE8Pj8naufmC6LkYVyhd7DrpUsOtO22B9aaOmHalZn-cjNOboUJ2w1Cyx5Amm59h1WLTFML1_Qkf_r_VHeHmJENHHxahQcNv-vvfWD547i1pEizqvg1eEA0zhY-FIkiWCVQWDDT_yZwFTY7EidLOJpVb8gy4J00UVNkhqdfW6HL5lFlmOrzpQchFyeaQiFsxBbztHmtXeKgDdPlj7Et-qzupusXFNwvo-lwfdQsrqFOrureBU59btHdIFqIxpPq4M63NrNY2QdLylqkgr-a-Sn2pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce693d467f.mp4?token=T_YvogKWWO67xPQy9pFWa21lqzGrn6x53Cs28lWpVsY0Yj3r3nvw-fXLJBVgSoE8Pj8naufmC6LkYVyhd7DrpUsOtO22B9aaOmHalZn-cjNOboUJ2w1Cyx5Amm59h1WLTFML1_Qkf_r_VHeHmJENHHxahQcNv-vvfWD547i1pEizqvg1eEA0zhY-FIkiWCVQWDDT_yZwFTY7EidLOJpVb8gy4J00UVNkhqdfW6HL5lFlmOrzpQchFyeaQiFsxBbztHmtXeKgDdPlj7Et-qzupusXFNwvo-lwfdQsrqFOrureBU59btHdIFqIxpPq4M63NrNY2QdLylqkgr-a-Sn2pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به لطف هموطنای عاقلی که سطح IQ مثبت هزار دارن، لبوبو ایرانیزه شده و وطنی هم وارد بازار شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82994" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82993">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">از اصفهان موشک زدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82993" target="_blank">📅 20:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82992">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">از اصفهان موشک زدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82992" target="_blank">📅 19:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82991">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">از اصفهان موشک زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82991" target="_blank">📅 19:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82990">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXNfLP2i0I1PEA9l0mOslauByTRdavHMtdrd3S6Gx2sxzuYWsK6J5Ikb1tapIzrLND2ON7BLPqVaXBvOHrEpJ_q-qKzVBh0qU0PmJx1zfgK51RXPpWuNQY41hBrdgsRU1JLjAMV4pxV5RP0RFZWVMX029PEP2LBHnGsQQXMf8LCT0tL6EaxczhohfVtS_5fHDdrhTrQCh2VnJVUonWT5Elqk7dResnq-7GjgIf_lYG__vAlG4IlwRWJE3jJ3DuyUBlLJ0qsqcEMI8Tt0IkBJ4NPJFa0QZ9QojNqsRNKfFWr0g5lD0dUVqieqUqEU_oocxLf1b9Pt2ud7BkiXNR87dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوید محمدزاده از تئاتر "آرش" به دلیل استقبال کم مردم اخراج شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82990" target="_blank">📅 19:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82989">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">برو مارکت ترکیه خب مشتی، یکی از رپرای خوبمون رفت الان یک اونجاس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82989" target="_blank">📅 19:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82988">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9sRtYtOxmOlApWs7ba8drW7hJgxgyT61DdZxI9I2BHmICx8OEdcTIpX-730qBWZxcdM61hwUlFkk8FCUf0gMtEFevFYy30dL-6_4YAeScB-3iU7LC3SrOYGU2NlLABQauICN6aRs-i2_LM8TJ1lLEtwm5mw1MOjx2VS3mxa2_sK6bLi-kxQqybyapPKwK_lhzkusIjb3e8OLrBB-j7Yop7DrHK9P9mq8SFolaPkE-UNvfW0mbk0Q9zqiyomrae0j47NLfx4GkH-pFxygzbo72Q1evAR9f72g6IaCJ-mY-s8C-Y_Z-rVYrPTS7bjvh210aniwGpVN-wFVu0tbjkgmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادمینای چنل کوروش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82988" target="_blank">📅 19:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82987">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ed68f76d.mp4?token=AnGeL-q0J6fdtJHGW1aZzmeDGLJ9cKDwajzQuITssql97jL-lAcD-KQMp7Db1L579WWaHkXZ1T4-vf88cY4MMCTEJdTa8gijr7af6B-8obt-6TSQbfhIRjhp698H_4dAR3obYmtqhCoXyqC4Wugv9tWrBpef4JJK3iKB9sY8Kl8X877PLFvTkma_2jtNH6BwTEuyT-i-ZyUq7lyVsZDWThCfJWJwWBiAomC8zhzvLVdWz9XD5RyfkVvcOpUrYnYjmY0qEL7xVX1-_p-GxVV0aFW-9tvKR8MGTzqLB3zc3DLFHHffZHE_XhEKEGuNdOqfStL5NlQQYLZNyBc4MtafOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ed68f76d.mp4?token=AnGeL-q0J6fdtJHGW1aZzmeDGLJ9cKDwajzQuITssql97jL-lAcD-KQMp7Db1L579WWaHkXZ1T4-vf88cY4MMCTEJdTa8gijr7af6B-8obt-6TSQbfhIRjhp698H_4dAR3obYmtqhCoXyqC4Wugv9tWrBpef4JJK3iKB9sY8Kl8X877PLFvTkma_2jtNH6BwTEuyT-i-ZyUq7lyVsZDWThCfJWJwWBiAomC8zhzvLVdWz9XD5RyfkVvcOpUrYnYjmY0qEL7xVX1-_p-GxVV0aFW-9tvKR8MGTzqLB3zc3DLFHHffZHE_XhEKEGuNdOqfStL5NlQQYLZNyBc4MtafOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست پاشینیان نخست وزیر ارمنستان تو اینستاش:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82987" target="_blank">📅 18:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82986">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf87a5e3b1.mp4?token=kVDCoZDuqcOCo5rVixTsqrVnak-IUXQ9_E5MQSaaTy5FXdbu3GJa00NC4xDf3bR3CD1ISbQgUMTN7f5NH1FYNdJx0T3QlBbjH8ujD9ayHawN62d6Fy5-e4DYBVgyM7xvQ3BwkM1zr1L9XNpuIoN-f6roqiy5CTjHztq6k0ov-7tc_43ekCxIx9j4i7LIT0iYUnqbgqtt8JT8BDjsRBRLpMUZiJgz3j7nmtm2J-Lmq5d-yJ6quD3tZF-7RoFCjfGLFton6_PnxmYOtQeWtN0_KRNkzrZnMlQgRP2y4VFnpBtgtdPwiY3Sge_A7LAcUnFRiWNDom-oWNxI0S1ecQjCng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf87a5e3b1.mp4?token=kVDCoZDuqcOCo5rVixTsqrVnak-IUXQ9_E5MQSaaTy5FXdbu3GJa00NC4xDf3bR3CD1ISbQgUMTN7f5NH1FYNdJx0T3QlBbjH8ujD9ayHawN62d6Fy5-e4DYBVgyM7xvQ3BwkM1zr1L9XNpuIoN-f6roqiy5CTjHztq6k0ov-7tc_43ekCxIx9j4i7LIT0iYUnqbgqtt8JT8BDjsRBRLpMUZiJgz3j7nmtm2J-Lmq5d-yJ6quD3tZF-7RoFCjfGLFton6_PnxmYOtQeWtN0_KRNkzrZnMlQgRP2y4VFnpBtgtdPwiY3Sge_A7LAcUnFRiWNDom-oWNxI0S1ecQjCng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آزش آنالیز ببین کاراتو تروخدا
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82986" target="_blank">📅 18:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82985">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ویدیو جدید پخش شده از نازنین بیاتی کف تهران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82985" target="_blank">📅 18:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82983">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gC2FF-5uDHdxEtRKWN2xerD7tSwa3LtyyzWT9P210-veutEE_WdZNR3JDCxO5wTlgiLE8sb02cmLlQ0-9mntRTsSsLz6c0NQS0oPHvdIZdrfPOGsyLV-Ftoabw86k8f-t8GU3_lmyUkrogZaVCZSrPsJAu08ILp3laQiz5WzRfTg5Ax5gKHAWp4-FQCfpw7_dqEmMVscfm5-KP2s2zVwbJiKplXEJtRINzNg3qUe4QGKycVRkRE3XadG_aiVoYzVIS64xsYTBEMs4cUBQ2likx6_xgtjJ7acWQOjxcDjqXo4-w7Ih7uu1ufKEAwY6l3yHkHOyrjtqBHcgv8Hzm5Pbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34b684e1d.mp4?token=dftYb70q8-hr7dPULEW5c9keoVHiz55wIqDS76KO8-mSzIc82ZiPnqdR8J4oh8F-1V9DinrkwXW676vc_bP4_w17lHZcwDsiydh2E7knyTKzRuiwaBQWQodv_3DQb99ST5zrZBUWJVI-B9Dt738nKcmGtwTU2lBaSocUCnwBLppelVWBXsOA6VutkUPD5IETxNFesP49ko7WqyZyvcr_rRmbwKWfPfmPXfpMNfkOv-kFabKxhtMPdaniFbmdNMAvg-HHdQ9ZWfmEzp_isLpOsDXT2soBu9TvZESmvhggK50ZHaJp-AF7_5F0g-AyJTzGllsiaCrITxI46vxMxKuSDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34b684e1d.mp4?token=dftYb70q8-hr7dPULEW5c9keoVHiz55wIqDS76KO8-mSzIc82ZiPnqdR8J4oh8F-1V9DinrkwXW676vc_bP4_w17lHZcwDsiydh2E7knyTKzRuiwaBQWQodv_3DQb99ST5zrZBUWJVI-B9Dt738nKcmGtwTU2lBaSocUCnwBLppelVWBXsOA6VutkUPD5IETxNFesP49ko7WqyZyvcr_rRmbwKWfPfmPXfpMNfkOv-kFabKxhtMPdaniFbmdNMAvg-HHdQ9ZWfmEzp_isLpOsDXT2soBu9TvZESmvhggK50ZHaJp-AF7_5F0g-AyJTzGllsiaCrITxI46vxMxKuSDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید پخش شده از نازنین بیاتی کف تهران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82983" target="_blank">📅 17:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82981">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPnkCzNBtTtlv7SDo1v24WUyAXFXihT80motV7OhDMfu_Jv3teYjWdF3GPsQOg26tl2Xvfe9D4tJqfC8r-F3eMbzmL9ih3KdqvJDgafAA7LlCa8xpzrDXeE6-kKYw5R3xR-NOBFy5LpBj_TteqhWskxkBvCLwB8F-SExf2l4hHYQxlGUatHt1i5xNWJ5LSfn1H-1tbtJs1hn14A0xLKsPOzMCMwijoxbCk7nufTZxCHWJ1HzHn5kMoLWU8yHqv5zze43_HN_7f9xR95zey_kGaUBCYnpCutttjqIkWfbLgyRcYcNdG_aNwbn7yUBix7NHhn0NT7nr-WXuVUcJ1prvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش و سیا به نام “چندتا؟” ریلیز شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82981" target="_blank">📅 16:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82980">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/575bec5ffb.mp4?token=WypdSiPb_20mgN8OnR3nIPuMgD4symSmBQSQOU8b8xIcwfbjaYNVSB0c28L5BUuPmYyAj68DR-_lhmCAfoLjGgjv0KFGBSlXUtH_Jkma_-EFYXHd3lthgOAN1VnjsU-vbNsB9T7ikfN-rDmW7iysedbgio6GwToORmJrw3jjTV7Tr9vbB9YecwZgJA5fFD8O0jyYaYz_JsHhEBO3Dqhunl-vKYj0xRGBsmiFda0C12Pep6yucrQAnDG_IBYZrye0hBXAzjc3vKrYbBeDv-Cx8TbUDyH8AI6mSyuoKUS2Qlmdl0Y51NjTjvvRM1cmA9k3BeHvNG3dNH6aWOCKi6aq-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/575bec5ffb.mp4?token=WypdSiPb_20mgN8OnR3nIPuMgD4symSmBQSQOU8b8xIcwfbjaYNVSB0c28L5BUuPmYyAj68DR-_lhmCAfoLjGgjv0KFGBSlXUtH_Jkma_-EFYXHd3lthgOAN1VnjsU-vbNsB9T7ikfN-rDmW7iysedbgio6GwToORmJrw3jjTV7Tr9vbB9YecwZgJA5fFD8O0jyYaYz_JsHhEBO3Dqhunl-vKYj0xRGBsmiFda0C12Pep6yucrQAnDG_IBYZrye0hBXAzjc3vKrYbBeDv-Cx8TbUDyH8AI6mSyuoKUS2Qlmdl0Y51NjTjvvRM1cmA9k3BeHvNG3dNH6aWOCKi6aq-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقال تانک‌ها از ایرانشهر به سمت چابهار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82980" target="_blank">📅 16:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82979">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترک جدید بهزاد داورپناه و آیسم به نام "تا بتونم" ریلیز شد. SoundCloud Spotify  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82979" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82977">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYIWgEMz5YnbEmKq9OKM8J7R1xuC0AbwE1T2smrbDcCzIKXlMDS-Q2rF8W5ocIHZqevp-ii79XutWSt6MVFjPVAcao51Q-J8edPz3PrCGd2fJmR8_l7_XEEJOJ8RuBOVqGAlDEMEGWTXQiw5KU3BZkk5ICn3qQJqS2yukPdoGhGTAIBNeYTs8_6QGUnUtMCEclkgLeMdZqumCBluaWliwdLuvTerczYcdl5rYdJVtNLvFaTZWbYEj14-2f4KouJy1ouvbthwE90fF3xbReNMeM52Q_r69BaLYBNaEWw-kH9WSPGX-CIWpu9D2ePanP9daADHZJJe0qA4rMTZxDP9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید بهزاد داورپناه و آیسم به نام "تا بتونم" ریلیز شد.
SoundCloud
Spotify
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82977" target="_blank">📅 16:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82976">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BahXJ3bW-9_HJbb6snPpzUTpjOvX8UMhueh8PnM_QyBeRuy7dvBlu-wylHOcd8_qv-Nesgkmx1g2zNMdQYD5MawmFQbyy2HtqZxDybXKTsV75PpYrb_CR5CmSl1kRioRhzJzzNFuB2pNj_XLhlhQdpBG0v_gYf0--6i_4mltDX8eZrZXHHt_IimK-3oAzJGfWzuFYMmXMrzSUjK7mTEtNKwFFtxaBwbbfzA3XNkiexrVxiZh01IAja3C0VuS91a22E6Ae9zNgf_DPU1EVvPmwS1biuCofB8DOj2DMAOjpUqXAZl0g3gpQ0HejwPSeZoz8RL3co4MY7EP5r7XhhiUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهیار و خار مادرش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82976" target="_blank">📅 15:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82975">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYGDjhzXulddD65g08_FAmwH_wD-XUr8c8TUEEIWU1VFyOVsvP6mhVjlbVLOGA2Mvcj6wWCXb8ahXloKpckEWbYwR57e9ETp2isGw4vRlxZw7coI6ewxDh_z-9pl5g0AynRy88ScWr4p2Qbx0EfhMwulABYysdBmC8ZWHVCzWWd5pL8MV2kjAWCfmMK1Qz83secgFczdx_iqZaAxG8UOaOYyDtoBDkclPqKQiewICcUZ1keTf-maRNSLtV8JSfvRZrGtA_eXgGseCjH5ZwHknGLKtQvMOKqQcVlb7hBcDH1l-hUlsfg2cOlU6tqTgPcKZqxujnT9ILwVRAUlKUrauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برا دکتر حسام خوشبختی تو کیر خلاصه میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82975" target="_blank">📅 14:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82974">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgrhAA2VWZULoP__IVoKM3eg-4rP4swLVCCdMapfWaG2JJDLIY5ZejwofTMuMduiE4oCbQevj2-j8IyzniovaneGbCeQIPcJuHCa225ZmfskWr2cPKJa1s1GIZIJfeud3oDEqlSViMJ6iq8vmcf3E2df5NbfX9j6fhQsZ1VfwiTnunuKQKL9GlVhPT7dPDPKNUf_KgXcHBMELUyhnqsi0eiL9PQt2y5NwFSmy9-5QtYUQAthpgU96bMt7XsUy5rlE0mPzn7Z-b-S07k8ZrvV3nhoAhpLZOdqUHtKAyWK3x1lr1fqCEZ1Kjhn5PtEzvYZRB928Z7Tnew5eKX4CV8XMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید عزیزان، کمبود محتوا تو سطح فضای مجازی و رپفارسی واقعا بی‌داد می‌کنه و ما چون دوست نداریم پرامپت و کصشعرای سه سال پیش رو پست کنیم، مجبوریم هر روز به پیج این اسطوره یه سر بزنیم، ممنون از صبوریتون.
🙏
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82974" target="_blank">📅 13:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82973">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خبرگزاری مهر: موج یکی از انفجارهای ناشی از حملات آمریکا به یه مراسم عروسی تو هرمزگان رسیده و باعث ۵۰ مجروح و ۴ کشته شده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82973" target="_blank">📅 12:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82971">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOory1OydaERdScBRWvDzi3oIt3ND9vDjcPetcX8vDiGtxNUxI6ldDiOC5sY1HRlUNKH8ZSpeonQRdJgprXK1BzSlTLh47B5O74GVFB0PENHv7m-N1kSCucQUI7IXBiAJJ8zWQDdOpE2e3VQUqy-4X9xhgfVViB2bqT1IPhjCZeQw-olnaCNTw3UEHAgBypoXZBOjE_jnzwblp-QuXhjEat_Hn-7LRc6mK7Q7K9zQKMznGAXfFy40slXQoVaE7rTE4K6mo6gUJ8tMZOwxTrqNftT3qAcS8T-pkWc9uF4HNouzBWyx-ipJlAba_kJIIPk6Oq-HVoHrIa0KkGI6n9SZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ad8899803.mp4?token=Lg8u3w6DpnAo8dSjNHcXCNImk_KQVMgMxbSBZp1wGpHOOQu3_-XMyq1fY1fbqzuJlVS2bw0KKQCPFW4QcBlQd_AbK_yjVAfUlfAW4BrrzZScKuxjCGqwZLo4F1nzJrWSjUOEdJ2bXTB_w5M8O5QMBUxWPGupJeCCCgaj4jhk51AUosUFjtsK7gfGPJfJogfYjZ_gKml44w8QdH-q2mi77N0r_aFf23foCqAGqC-oVrmKDi0Iq-LfVpRe-Ce91-rcarJ8bkiXW9xvjE9m6hwVlCz93eWkTWZHGrXUPFL1oQ5TmrxBeCSI7x-Vb4y8DsaxITqoZRJ7vyffuB5fGvQtZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ad8899803.mp4?token=Lg8u3w6DpnAo8dSjNHcXCNImk_KQVMgMxbSBZp1wGpHOOQu3_-XMyq1fY1fbqzuJlVS2bw0KKQCPFW4QcBlQd_AbK_yjVAfUlfAW4BrrzZScKuxjCGqwZLo4F1nzJrWSjUOEdJ2bXTB_w5M8O5QMBUxWPGupJeCCCgaj4jhk51AUosUFjtsK7gfGPJfJogfYjZ_gKml44w8QdH-q2mi77N0r_aFf23foCqAGqC-oVrmKDi0Iq-LfVpRe-Ce91-rcarJ8bkiXW9xvjE9m6hwVlCz93eWkTWZHGrXUPFL1oQ5TmrxBeCSI7x-Vb4y8DsaxITqoZRJ7vyffuB5fGvQtZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره رسمی شد بچه‌ها، آه از دل‌های شکسته و حسرت‌های ما
💔
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82971" target="_blank">📅 12:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82967">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ای یو علی هستم، ۲۸ ساله از کرج  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82967" target="_blank">📅 00:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82966">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b02f59615.mp4?token=KPtzs1IUkn79bjvISQ1ULmFigrQZB74caQm3R-FcxSRAEm2hpvCN_WMdeFphPzzIAldcDSrURf7J4v5wcUkUIttDEqXJhC9QbY0OsDARybUqA78PFcvWdA1aiBk53z_2GmDmbO2EKMko_yAqhVrJ3ebhz9x0aBLPSKKN4ex_m1zRKa4NbxeZaNkvMHU1T3WUr3zrcEO4ydoWmBuBiPolrffpGOm-X47YCcYy8FWTX32L06JNdxD_geHXuT8k4MBc6xHqzn4r7z8IkwHm76EbibzClcBPV-RngB3-yRN7uHI25swObh9-UqG7Va5WLNuvxECKztaY5bFtpWtR2Bk6bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b02f59615.mp4?token=KPtzs1IUkn79bjvISQ1ULmFigrQZB74caQm3R-FcxSRAEm2hpvCN_WMdeFphPzzIAldcDSrURf7J4v5wcUkUIttDEqXJhC9QbY0OsDARybUqA78PFcvWdA1aiBk53z_2GmDmbO2EKMko_yAqhVrJ3ebhz9x0aBLPSKKN4ex_m1zRKa4NbxeZaNkvMHU1T3WUr3zrcEO4ydoWmBuBiPolrffpGOm-X47YCcYy8FWTX32L06JNdxD_geHXuT8k4MBc6xHqzn4r7z8IkwHm76EbibzClcBPV-RngB3-yRN7uHI25swObh9-UqG7Va5WLNuvxECKztaY5bFtpWtR2Bk6bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای یو علی هستم، ۲۸ ساله از کرج
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82966" target="_blank">📅 00:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82965">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3f3bba65.mp4?token=W_znH-VNmzvLJFkRjiaEbx-OHNYCdJ7F41CfIJ-7hcBudwiU2Uf0iRk1Jbz-N3XBVxVrxqXXgYoYrvsgmzZCZyKocvLrckwZo9uOe51oDgKqSW0AYPfQ8wvTRyC-_paUgixWjHTnLTefVmAgkPQPwZLhxCUWIjCl1kVTwcB_01uGF1yqi9jKjB0ub8mWlzASM1SjmU6n5j8IoKIf1-qivG32BYEF22NDrFJBxDJxRV_eVwpy6J136SQ_QNHPnK0svV482zcQj3ODk1j15TH9Oh4w6dt5C6XcfTkYKJYswWmU2ZDOYK5YuSEeRixuIOrLgBjMWNUFwtylo78HDe6S3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3f3bba65.mp4?token=W_znH-VNmzvLJFkRjiaEbx-OHNYCdJ7F41CfIJ-7hcBudwiU2Uf0iRk1Jbz-N3XBVxVrxqXXgYoYrvsgmzZCZyKocvLrckwZo9uOe51oDgKqSW0AYPfQ8wvTRyC-_paUgixWjHTnLTefVmAgkPQPwZLhxCUWIjCl1kVTwcB_01uGF1yqi9jKjB0ub8mWlzASM1SjmU6n5j8IoKIf1-qivG32BYEF22NDrFJBxDJxRV_eVwpy6J136SQ_QNHPnK0svV482zcQj3ODk1j15TH9Oh4w6dt5C6XcfTkYKJYswWmU2ZDOYK5YuSEeRixuIOrLgBjMWNUFwtylo78HDe6S3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از صفحه رسمی فدراسیون تکواندو ایران منتشر شده به مناسبت گرندپری کره جنوبی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82965" target="_blank">📅 23:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82961">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اون قسمت از جنوب لبنان که میگفتن اسرائیل حمله کنه میزنیمش
کنترلش دست اسرائیله دیگه</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82961" target="_blank">📅 22:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82959">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evwheYFbcrIX2VsGtXX2qneUL0dyyuACTDt3hBpswRFwXuFnjqzpXzeVKcVFMd72GKBjgOHkgECA0vT0VvTzGoqfkqYmR10PnJm1t2JtYFk1-9-IKnxh8JukA668zuecT4PGsZTxowh45an1pbg-7K2R7JTbVGavLJdMh_Y4IzPh4ufIr6-AFnKa5el-iKlJpGssguUq94bShYZfmtTIoImBt_R3QSyD-Diqqv1H1KCN55KPugk5ViPqTj0GcWRPi7DMzF3J_F3V6IgNNGwMJ7Q8W_CptbT_bonr9Zxbg2bQudsmCu12AZpiOKqJuoSoRSPjluzwWjKYWAHTFQiPGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکوندی شاه عالی بودی شاه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82959" target="_blank">📅 22:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82958">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a86445b0.mp4?token=o5HsNnXEJjj_gz1T-z2aj5VFhkam1m3Yuoh3_gjByY2GEC0x7ojMKaKBLw7qfRZFMe8l3P1VMy7xigil7Pz8_lt4eG1Dw5Ttxw_R6cty9x8LQRQv2tnk0LinApL-u1AAskh-PCyf9dzBAJxl4ZrtJm2dLuzLxw18P5YD-a5Shz2HOz92sCqgmBNZ4rqznDLU4DV_ql0CMpKHk1Tel6aPLFySJWKNPoxJ9-bP2YsNQo-MHCAPUtG4Fx5TjbPK5gz190KC99r96nkyCV_zwhFtIRa4q2zUrPWIyjcQg3-Ox9UtNWbMMM1EpjcT4YhyfCvET3EwwDvdG1h6q6VHnrTyKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a86445b0.mp4?token=o5HsNnXEJjj_gz1T-z2aj5VFhkam1m3Yuoh3_gjByY2GEC0x7ojMKaKBLw7qfRZFMe8l3P1VMy7xigil7Pz8_lt4eG1Dw5Ttxw_R6cty9x8LQRQv2tnk0LinApL-u1AAskh-PCyf9dzBAJxl4ZrtJm2dLuzLxw18P5YD-a5Shz2HOz92sCqgmBNZ4rqznDLU4DV_ql0CMpKHk1Tel6aPLFySJWKNPoxJ9-bP2YsNQo-MHCAPUtG4Fx5TjbPK5gz190KC99r96nkyCV_zwhFtIRa4q2zUrPWIyjcQg3-Ox9UtNWbMMM1EpjcT4YhyfCvET3EwwDvdG1h6q6VHnrTyKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کافه ها هم مثل طلافروشی ها و صرافی ها جای منو مانیتور گذاشتن که هی بتونن قیمتو عوض کنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82958" target="_blank">📅 21:13 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
