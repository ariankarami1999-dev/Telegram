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
<img src="https://cdn4.telesco.pe/file/KU2x9gC7cdFQxRf6VfrnFb0Qeq4CCntXZpQ00NfSsBA9tWbcID7wZCjw9ocSnocU7VmZkWEh1Uxf23kR2P_A50y_P-4MRML0zDAsUsYFK36EiRd5bjKIq3ycJa2D4ehHP--0H0lFjTVtReNg5KT9TrJ9Upo5Ja7l6LA394GE7dVDGZdVupLk5y02UJxLz4YXIqTuqcb26zwqdG2975RfvPQPUT8LCg1mCJ4fHFxJXJwfQVf-5ywEgqypi3wZW_1g0c7gA7c1HrBXdz7z36y0yxs7DDjXtEvhnXhb3x5tU1oGLcOecP5R3n6GQT7-rOGQNHDKnoSDAyaiwD237M2foQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 197K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 01:44:06</div>
<hr>

<div class="tg-post" id="msg-80840">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nw-d04Lp8O-Xieh-x98RylahWIojWsrk8-M8geIH1BT9hU3HVxkBTlv90ueg8xTnxnteQYCNPJguXErtBXGdMA-qzGXwIu1sJoLPFQtHxnlgmBze477PCz6-kfW9MjNh_oih8s4tvrRUOPVrjipPFI-sNjkEwpUrio2lLtVxgaixMaiQt2GQyylsxLJaHff6XArOnLXAcY24HU2wt8EK4WdxgIPTD8wpUmCEBTWuQJD95w8EEW_z5pOs9vGPirjqnIydtpk2Dnx7XNhGEAL3HEAKqaI7qkBM16AofxaqCgMf2Qjep6vh0za4dTev5W3E6TvwbXIgxOH5Zw6sGkfCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا اجازه؟
این دستشو گذاشت جلو دهنش به ما فحش داد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7 · <a href="https://t.me/funhiphop/80840" target="_blank">📅 01:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80839">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دریک جان کیرم تو ناموست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/funhiphop/80839" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80838">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">لامین یه جام جهانی
مسی یه جام جهانی
رونالدو : I'm back
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/funhiphop/80838" target="_blank">📅 01:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80836">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txmTTrWpGOXIwr9dsN9OxwSSJ09B_qbKZMtMbNFlXoWEdtBAUaEgu92m7CpNussxSZ_pevOz7h8SOvkaRzAH63n757X_pc7s8W15smMD8dInFuDsqKZA98snomvn5pxT3SObOdsz0InsMigXOsj502UUq18H96e__q56Zbu1eQJdkaVtZ5bxNomHsKnR9dkPhL3v_8rZbqh5agGOghaL8LnJy6RipT8IcBmi81u7gvHgsJHSKqKendIRV4upf2F5Vxd7YsbmtfyY2hY8F7EaYFNgH8PIzL26tVYJSaJGWMUrEUTVtPTm_rz4tUDJLi_39ScR1bHGBc7BvfE8-5_c-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غروب یک سلطنت همراه شد با طلوع یک سلطنت دیگه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/funhiphop/80836" target="_blank">📅 01:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80835">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f37b90c753.mp4?token=uX-cWMMMqWZpVGRiGdT67pBx4atbs3ArvrIAA4VZMcfJiO6n803Q57lhDRdsFAX0dnJy6TxlAdWtKxgiK-urUIQIy5m_SEc9HeNENukCzL3aRTXI-mT74y-X_KPaBaUOY52D5W4MuOlEv3f3CRhxdEzqnnwtNZ6__YXHamR3eTYwR7OReiEE3A9apiaTk4rMsgTcvzF6fG8pLgseLNgENU_uEPjWMS3CzfKoCxYDU_slBLN7rtZw9E4Bqmfex-u3wx-SO4OHsrp8kwlG6qzFfew9dysmgvPJyRFaEne7pbH6s1SRM_UG37BBcEuqx8_lMeP0-edmAxkYH5QEE7Q0lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f37b90c753.mp4?token=uX-cWMMMqWZpVGRiGdT67pBx4atbs3ArvrIAA4VZMcfJiO6n803Q57lhDRdsFAX0dnJy6TxlAdWtKxgiK-urUIQIy5m_SEc9HeNENukCzL3aRTXI-mT74y-X_KPaBaUOY52D5W4MuOlEv3f3CRhxdEzqnnwtNZ6__YXHamR3eTYwR7OReiEE3A9apiaTk4rMsgTcvzF6fG8pLgseLNgENU_uEPjWMS3CzfKoCxYDU_slBLN7rtZw9E4Bqmfex-u3wx-SO4OHsrp8kwlG6qzFfew9dysmgvPJyRFaEne7pbH6s1SRM_UG37BBcEuqx8_lMeP0-edmAxkYH5QEE7Q0lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/funhiphop/80835" target="_blank">📅 01:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80834">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJhFgsGPUJ5OtQhtwARQht0XGao1VIqFesB71jC-Puv3pYj4HOlCsucYxCGL-z8aaTxFS_EfbnuJbGYyC3J2Kgt1wZrwB4WdFFp5cAJalaZKb8TK_RbcVqOTAE8osAmZl4OVLtyA7ZOJBgtKmKL5565TynIz3PjJDanq7kikPDXeZl2HezLlFs1udFgHzVI-TY6ccy3DzInLFo2YjwD1UCvnjtN_9nB3SJZa3w2U0Kd9-AVgjbO1vo_EYptcOxKWP62lme01fIZRfuAxWuAiyOHUwBaA0bR9EmZMmO8eBiZVgYte49tP2r3JQWNCECruc_1BAVZa6sfo6r8M45prbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی فنا شما بدتر از ایناشو گذروندید اشکال نداره این چیزا
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/funhiphop/80834" target="_blank">📅 01:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80833">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umrQAe1vZfvQfO4HB91GoNBmnrSvjG5P3DHQlKofpulp66dwSlNz_yz0Y-4gaa0JTi77egWmMGna9YkhLY4H4Bfv7-nGRCeOQSJf5Na4DFGaKF6Ic-MSzstDAHjLQF-tjYZcZVmKX2ZnAqlfq7Dfz8fbhDSH3NvSsJSdyaJKWG_Oj2gtEG0-rPfN4An516AvpPElAdmiJ7H5EtUHxLX6Q6jZ_JnfRq_sJk1N5ukqlHv1ESo2C2IHGcWxGmlupW8quE6N7MFShYE-yqn-o9bgdkyfnpzrjqxl-6i0uW5KyU2zxZ85StsLfYIFu2zuHcbP9o8-J7DvDcXFb8qnx32t_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عکس دیگه</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/funhiphop/80833" target="_blank">📅 01:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80832">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اون وسط یکی زد ناموس گاوی رو گایید</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/funhiphop/80832" target="_blank">📅 01:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80831">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ریدم گاویو کشت پارادس</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/funhiphop/80831" target="_blank">📅 01:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80830">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0ADuK2cpV__myRiHFO956BAcT2TGx9ogTB0HoH3WLxMACUUx5lLKmG0yWPqxn1pADduAtx4pnvMvZXv0-yIa00HY3CGPipBt-INhwEzDkOfP6ZCdfNhikV26SkEksOyLfV1QZCCfX-STJV8PsOPgVEmpKHHyQRBQEEiWjuGLCpspo-jVU7waMAyFLFmnxXDuwditEpqJ4Nur3hTD5jyxIx1USvgWu_4CAYb8hl4wNhB7qFGg00yPnxSDzjygQmhG9aLQYAmEwX-AE_MVvGViv2xcmQxMRwXunPXXWwQYZJHs3UjXqEua1cfEscjprGUGH3DRs3qIswIYCtz3m81Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/funhiphop/80830" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80829">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">داداش یامال هم از باخت مسی ناراحته</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/funhiphop/80829" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80828">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مسی چرا اینطوریه، وقتی میبرد گریه میکرد، الان باخته داره میخنده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/funhiphop/80828" target="_blank">📅 01:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80827">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اسپانیا قهرمان شه پرتغال میره جدول شانس مجدد که انقد خوشحالن رونالدو فنا؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/funhiphop/80827" target="_blank">📅 01:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80825">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/funhiphop/80825" target="_blank">📅 01:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80824">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/funhiphop/80824" target="_blank">📅 01:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80819">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/907a6900e9.mp4?token=OnCe2h4iIm1WQh5PZ2absC0NktFs-xDUVYkWWB2v45Z2eYbHJRGbl0ux88H8OFMdGlMmfoc5meZobZupHWEQUAuOAZrKzpysiBXGG_ABvqilkbRCP2DRg3Ycdc3nVrWLgICboZJJLrloMp19RJaUJkI6oxHYCUTyfhyFaHZuQ1p4mhNGDMIEvzODf0-8Ttn3DlP_90dLcWMEh3rCpLV-Bm-fbLrv9VAc-muahJ5Zuw7FyN_C84Ww4uJa3K0Lq-3UZpLGT-Pt7YJeWiVZwvCyabBiFr0P9ukpL6Xrl5IpWk4N_DV02R2_V_aYOnDmMef_NbrBRYA9TjE76qkY3ZUAFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/907a6900e9.mp4?token=OnCe2h4iIm1WQh5PZ2absC0NktFs-xDUVYkWWB2v45Z2eYbHJRGbl0ux88H8OFMdGlMmfoc5meZobZupHWEQUAuOAZrKzpysiBXGG_ABvqilkbRCP2DRg3Ycdc3nVrWLgICboZJJLrloMp19RJaUJkI6oxHYCUTyfhyFaHZuQ1p4mhNGDMIEvzODf0-8Ttn3DlP_90dLcWMEh3rCpLV-Bm-fbLrv9VAc-muahJ5Zuw7FyN_C84Ww4uJa3K0Lq-3UZpLGT-Pt7YJeWiVZwvCyabBiFr0P9ukpL6Xrl5IpWk4N_DV02R2_V_aYOnDmMef_NbrBRYA9TjE76qkY3ZUAFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/funhiphop/80819" target="_blank">📅 01:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80815">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الان رونالدو فنا با مسی فنا رفیق میشن بر علیه یامال فنا
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/funhiphop/80815" target="_blank">📅 01:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80813">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">لاپورتا تمدیدش کن</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/funhiphop/80813" target="_blank">📅 01:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80811">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/funhiphop/80811" target="_blank">📅 01:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80810">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بابا یسال گذشته از شروع بازی، چرا تموم نمیشه</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/funhiphop/80810" target="_blank">📅 01:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80802">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQPnm3DNUvhAphIk15MN6Zty112N6MGEDi9ueOCioR9FDepqgxI1zJmI3fHBE2ry5u3LwazwVOctGMqbAoTM2_AXNenv4slSZJzEHkyN6bEh1u4KtyOpXLpFxKyhbAK-8iVqNB2DSQmqmV90biHhv5VAxaSXBQeJw_gDQY-9THgHFkBrOH88veAOZZmcl9b_06UCAy6VeR2AwFxKkLXWi6ENxubyeCr_A-yuWKpIqzXp3BOSnfMxs56_YCYim-Uf7EeSEU-HPCVmEfiJJ8O4oIxIQ-xXRI8j8TAH12mtzZaUyethYuOEo0OGA3AD2vX_atIIkpG4Vax18r87DaovzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یا حضرت سیمئونه و امام مورینیو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/funhiphop/80802" target="_blank">📅 00:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80801">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">این تاکتیک آرژانتین بود ک بازی بره وقت های اضافه
حالا باید ببینیم چه نقشه ای داشتن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/funhiphop/80801" target="_blank">📅 00:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80800">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbz0zdIa822iED1AyRx7vG5_5ig3RJ7c3B-hjpIcS7lYmLy9sZxJWcq9WtgXQGrVrWPFGzp5Ck4hwhrZ5KOV86-x8gn3fI2t3bFPzEUHGQGAk4fLpb3-y4DELqHWPxoE2LPYirEY8G3gzrcHge3urfC5dcT2u6Ju3-lTrz1mEQmUqG2GWxEpm4wuRG_iqdZxrN2EMUO_U2QXjowiD0Aiqj3Ahf_OyQ9_QKaquws4LaRv_o0nFD7MI2bP4CP182-1GEA1TByGKERKgdECFqQPkYIBcAqfdrFjF669RCNpjhmRzyzrkbYMa8vhAa2gwe1UCjFS49ZWLrDIdQS0QdeyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش یه خطا ساده بود، نباید کارت میداد واقعا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/80800" target="_blank">📅 00:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80798">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مسی
😂
😂
😂</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/funhiphop/80798" target="_blank">📅 00:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80790">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">چرا اسکالونی مسی رو نمیاره تو</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/80790" target="_blank">📅 00:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80787">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اولمو اژدهاتو صدا کن پارادسو بخوره</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/80787" target="_blank">📅 23:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80784">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-yX845oV98S9VZYWZhM20_bEpTOk4DGutqxfxa3L9W_Wr6fA7nWXl2VXId363hyxfADaiGSUg1fgt8LPa_6LdZR_xxrntiNEXbS7VhZW7iUbuySrnHlpC8y0ChaidCmOm-D3YVS-NPfkqN2LWr40n1jN7yC-yqXv8ke4z0P48frDHcTKSWH605sgGYurXoU-bBndZIJvTIawDWEbwTSSOnO2VVBON4wbi2QX2GFkcYEcYBy_vVji55YGPNESPp0BThNTIIC1tnRqkL5DpRX80JArVAWXgiJ5dDCNSkiexGcedODerwoFbtykoypjuIDQKXshLJevvjPwHf71VPAAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هایلایت عمو بیژن تو فینال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80784" target="_blank">📅 23:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80783">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پشمام رونالدو پاس گل داد</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/80783" target="_blank">📅 23:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80782">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پشمام رونالدو پاس گل داد</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/80782" target="_blank">📅 23:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80781">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نقش فروهر رو سینه اسپید از عمو بیژن بیشتر بود</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/80781" target="_blank">📅 23:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80777">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">عمو بیژن سیاهی لشکره که
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80777" target="_blank">📅 23:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80775">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بیژن ای ایران بخوان</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80775" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80774">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نیمه اول رو بیژن مرتضوی برد
#خلیج_فارس
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80774" target="_blank">📅 23:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80773">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">عمو بیژن بیا بنواز بشوره ببره این بازی رو
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80773" target="_blank">📅 23:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80772">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فن کدوم تیمید؟
اسپانیا
❤️‍🔥
آرژانتین
❤️
سایر
🔥
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80772" target="_blank">📅 23:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80771">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">من فقط منتظر اجرای بیژن و شکیرام.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80771" target="_blank">📅 23:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80769">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تازه دارم میفهمم وقتی یامال تو تیم حریف باشه چقد زجر اوره، بمیرم براتون رئالیا</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/80769" target="_blank">📅 23:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80768">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljbHOEqvvcI7BBMO5inUCLsMm108YemZBxcLWrGokQiP7MU_y9ub3QKmJ54sf3ZOCbwzS3_g-OxlrsxGNf4eJ3Q8fvPtn5WDkXyX9uCaEJ8wZGPyxY9wj5XZ4unScAC6F4InYZfBfX22aBD34nh-pwnHswglW7qljMhMHBcwBK7V6KKZt0tfrIV9aSASUMuVQ7Yd5CgOvC-76PQU7xiIBzGmr_Lvo0QIFl95_t9m8xdV1q1Lp0GGCf2K6C-opmTwdONZNcdt5cgd5E1za6WElOOp--BSpx8pG3R0hXZmsvQtq1skxz_rAAiKWvLYvUVRIwlCPuK-Hdph34OnJFXbOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو ببخشید به من گفتن امروز نزارم تکون بخوری</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80768" target="_blank">📅 22:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80766">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-8KMciZ7sUh8Hv0FF6KZCE8vWzeeYN_Jl25LOfDaGEN0Oxd4ZjtEIWljCW3yGpw4kkmj9ubXZDlrcMDALYpvt2DTqrfvFlQxJGEkgFHxpkyP5v5qoauADa5cb1i3PzcWSPv3CCY3C_Vsc3vvOLJXZ3cNyNVGwsXLdLD6uvHn8ccJtdYnQcr71FOdZhen8tuejSkDpebe6leTi8nZV4sPipSgXbYC2TRtXIC4TxYESQc80YlQ0-TBZ3cNvO8Doo_qqMJsTWSsK0A6wP9R-6ch9drSyiVCxK5bBEgIyP3RuaUsUBBX0VJbnCvVKx_jPU8wDf32OBRTDCzRNKuq4c_eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم بروس بافر(گوینده یو اف سی) تیما رو معرفی کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/80766" target="_blank">📅 22:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80764">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آرژانتینیا هم مثل ایتالیاییا با تمام وجودشون سرود ملی رو میخونن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/funhiphop/80764" target="_blank">📅 22:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80762">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هرچقدر میخوام خودمو قانع کنم اسپانیا قهرمان شه برا بارسا خوبه بازم نمیتونم قبول کنم برد اسپانیا رو بخوام</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/80762" target="_blank">📅 22:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80761">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دوستان شما نمیتونید کاری کنید کسی که بچگیش مسی یا رونالدو رو دیده و عاشقش شده بفهمه اون یکی بهتر از این یکیه، حالا هی مثل کصخلا فکت و آمار از جام ها و موفقیت های فردی بیارید و روان خودتونو بگایید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80761" target="_blank">📅 22:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80760">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBWQpBwE9fB-s_7iVLTW128uuKcYmWQFuexxhI0D00KszzO6Dd5xBigJZjnuVyCd2EVIHOyHgJ7Wrzkhd3nUF7TymMZDcoM2IVrs2eYvPC9EBBSGJXDzuT5j4FHdL8VFTH6vAFrpMoTN6mJQ8eq9m6_E58yubHurDhY-TOmsrmJrZ3BIZ8uPwjVTzb7owy9Bm7psMqIzBov_DcCaRGq6NKhJv7MfMBU-D21-yM_JEh08Ww-SZK5BO-Zz9esno9sZTPnzMoY9pa29Xni2ROGg37ItkTLEMOn-9lsHwlMucqoUMxuqfqx1rsZMFU8nn8p8YZjgBDNwayEtRC6udK7qGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80760" target="_blank">📅 22:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80758">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSRNf0z4KwzF9oUuiXLKnVNQKze1QW0k4z3yWkpv39whNtmcMVL9hsozEVnA0vR1zK9-wimkZxlsKhjBpAJtP2KqYGU0VKisjavBcMDqcpaczl10IujT6jUt7Nss81C7RH9nWDHPlMGs6DuUO4Zw-z1v_gMKRvs1XVsE6KJPFGk9lrCP4AWo95ErUS_OQ7G6SgbklreYxRHqqNO2MKDYfiGJQx8hbENvclvBnr5x31KzN4PWmZthVj4aJOOOlsN6djRUeZvNCtXXIwfmQhVpCQYOMSfrCaBK2cyt8h_DIHOrnij3D4jAwBS_fHeD3P2T9H899jzt3MScvrLJOJOA3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sKRytczgFrJeR4Wj3ZkGxOY5vIPd8gGRobHBMjUAxSvLwSmHRNwk31RRqFiUg3U0IOdFObZNjODRs-iE3yjXkc0CTdIlPoWHCBRo4oDOyyxtGj_8yaMKpZgKp807ZdG2xZ4ryfxL9zMwwsv4-Ih9Z3kHr-JCC0p0WUBlUe96v6tBBaqJ02iqsid7FZcFTBirq665c3mWcDx1D0ggMTiM35cWCLs-LAPOgTNDY_KYgWWf9kCDvkBHH6G8jVYr0iNECwO_NiwAWHh6UkxfCQk1LyetK_hm5hxeSFQ-gV1y0wmg84KFs1rvLvA1oFMYVlC7olhW2Bk0f5ziqUmiNmH6dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسپید امشب با فروهر رفته تو استیج
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/80758" target="_blank">📅 21:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80756">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jF_J2_T4AwPro-TUJkDi0op1HOFZfgktThso2Z52_evyH_SI2mjrBXf8OFg6hyts8RQQDvppP37P5N2n5Ej1K17i9CxuB-RCOl8B-nrwhVy9dFWF7FxBsqGej_pCcJqkrJAz-warWjQBgI90T0la3jS3sY6ImMGtAZISqXxEQ6V9B6uABJfnUFWRrlwcAOZ4oqdHZMDAyz2SvRKGPPGq-Szdd6jcnzFe6Nm83TQVmXy6HNNEEICOLvbXFH2pbVIpc-rBf1_BVBwvG6jT2eIUwhf_bwbL9GjFd1vz90L4j9nws0OnuyM4-hA84wQfL-KiuLzvuZKgVfPVuzSYOWIn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FjRifUW7Uch6qTDt2jYGNeECml60ZqfSPS1OI4WXoGu_eKyczMyjWBlPE1ibyYEB1rR7O32bPxN8g6bvjb6e_Fm4MbpG59smQ95QqO_rBEo5ooAuy16-P0FOlLDziNXpJe7qWbhxakts_3ValLuxEs-IWicZOFaZla77FcTiTTBuyTKjkgq6v4spK8h9svH8n6ahGFyuvuOJ47Drx8vRQZdhy2kT2WLkXTiaWXXLEUcez269pUhTCCavc6_mBRWeIlclhqDs_mFGW6ig8wXz0eDuoeoRedlCwO9BM-FL-v4QnxmW18hmhD0XibJgCkF4KO3QzNyznvGXKMamO6xgoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برنده توپ طلارو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/funhiphop/80756" target="_blank">📅 21:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80755">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4-NT6w2hNB6OHfTKorxGOxjP1gHgYjk4ih5Dm8Wa3HqGsMLB91yxD9zSoqvZGWhtPK1owf-rq3MZPyoiIYrg2V6JLYkzsWNLsmyMGfG-UCqCHdfXJCScW4OdFUUFP1C7TeU0eK_shLzCR9Su9CTQ2Gv03lXLf3p3imd3PJs2zZsrCq6kYgFsEKVLbI6vndnggCg2q5ZOfFL8dXruKg8-u7225OOh0WNMAV4t-VMa-z-QYEVmIWmunnEUvGVzP4Cr4R9sZtEIbbtZAGaBzoL-spxRxLNkDdkDhpiIQuHi3ErV8e6_eHzu4_jddLkxQEmkYScrUUdeg2EWY7nVgmBmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
🏆
فینال جام جهانی ۲۰۲۶
🏆
🕔
یکشنبه ساعت ۲۲:۳۰
📍
ورزشگاه نیوجرسی (متلایف)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- اسپانیا در مرحله نیمه‌نهایی با یک نمایش مقتدرانه، با نتیجه دو بر صفر فرانسه را شکست داد.
- آرژانتین نیز در مرحله نیمه‌نهایی، در دیداری دراماتیک، شکست را با پیروزی ۲ بر ۱ مقابل انگلیس عوض کرد.
- برنده این دیدار، جام جهانی را بالای سر خواهد برد.
- آرژانتین در مسیر رسیدن به فینال نمایش‌های درخشانی ارائه کرده است، اما با توجه به ثبات و قدرت لاروخا، قهرمانی اسپانیا منطقی‌ترین گزینه است.
🧠
تحلیل بدون داده، خیال است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g28
💻
@BetForward</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/funhiphop/80755" target="_blank">📅 21:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80754">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtYRnyXHwi4v8ZsQEJsCb7J5KTn6tY4cGmj0BEuCjQyswJ9ptsnM_iRf8Bz2O5WDxjhtNgc6wwPRTtFe9qwSFyVXjESRU-Bl6R6xM-aJ8OeQf3OXzl1nmr4HGps6kB-SN4ulxrFxdU6y2HG0j4J0mfFhuEqfbFP81lVQU_pBz1leS5PcJFfYH5dr2lUwK-CXFNJMLyWwYAsmA2iAqe3Hqo_taMyqi9fiXmWQsTvO3Oy6vDVotl-8QcDwPnGl0xeOiuD7A8DF198NljrdB0Y24e7-b73gXGfK5UgHos9uIyHLaGXhUe-RA64MObJ_jQs0eLpa4gYl0IYWymcl1XsHdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مامان کریس جنر فوت شده بعد کیم کارداشیان اومده عکس پاهاشون رو گذاشته و میگه مامان بزرگم دوست داشت همه‌ی دنیا بدونن که پوست پاهاش جوون مونده.
پای مامان بزرگه MJ
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/funhiphop/80754" target="_blank">📅 21:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80753">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JP9qWN0wD9ZKGLBVRPdYtHdzd1eWbsrVnGPPop9XoQo2eXrK_GsoQI84TMrILSdvg_5FLo7GdRJz24yRfbzrg0FJ5ozpsV2p6tOqBMAxxTrPpbTbf0ZnM4T-fdy_VtVfHxfCqvlI4k9bcg2DzX_k1m3nxYp-QZnQB6U4AYVkWiklEa8M_GgpooSqRCJmxJfYa0h-y4FGpFzogQMS6jZlcH2oAjNw09TLijMEaCJEBflY-41R6zUugx2AqapTu9oHycPCf5JxlcyDodeiPl0a5wPfev2srHW9Wjtsch4nf3-f0mTSyw6hdWMFZI6hm4Cr3zM8OGlfN2Ch6emzF5CNPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمت گرم این فینال رو هم برامون در بیار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/funhiphop/80753" target="_blank">📅 21:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80751">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-poll">
<h4>📊 کی میبره؟</h4>
<ul>
<li>✓ پرتغال</li>
<li>✓ مکزیک</li>
</ul>
</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/funhiphop/80751" target="_blank">📅 21:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80750">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXkJ2r09Z59BLBwDCJHOgI_eiE2c4F0c-3RbcNl8V1EFiNRPSyLZEueK5NmjnhKocu9nZmUfCY6F_xhiqq71O2iitziRFzh-LXMaH0AqY0vjZr1ZHtMI6Q9Y33egFwjozWIwHbqfYXpEBkg-lw0vznJ72bNCM875WxJ41fT793qiw3QOY6G9WeclMN23cBpC9X8MQu89jHLLHeeTJW1CukJ7k9VGENybrCk11xpBM_RB5aGud3ES5ZCYk4BYqsEHFBwnyL7kzO5nbECMw8qU9ffE1SSHZ9S_14pE_G2WLUFfdurq-z0AbfZjzeC7KdgMOmekF5WYWpFduTxBRo2cfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست رونالدینیو
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/funhiphop/80750" target="_blank">📅 21:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80749">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مسی فن بودن هم دردسر های خودش رو داره  تا آخرین روز جام نگرانی و استرس داری  ولی‌ بازیکن های دیگه خیلی زود خیال طرفداراشون رو با حذف راحت میکنند   @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/funhiphop/80749" target="_blank">📅 21:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80748">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مسی فن بودن هم دردسر های خودش رو داره
تا آخرین روز جام نگرانی و استرس داری
ولی‌ بازیکن های دیگه خیلی زود خیال طرفداراشون رو با حذف راحت میکنند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/funhiphop/80748" target="_blank">📅 20:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80746">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">و رسیدیم به آخرین بازی مسی تو جام جهانی  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/funhiphop/80746" target="_blank">📅 20:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80745">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnvmqqfh_v7Dt43hkVS4OYoxgk0-TnbudWGO0E_CcuohkY9u5dl6U0k2bMJTqoc7r3evJhiHPg5Sqv2ve1raQjXBFdTPQ6oHkShkiP0z7GY0UzwFUcGlqf_uWCf8uHBvw2KuV2XsqNool9D45XqSF83EH3QtJPYqZCVqiAd-83nBL7WEPb879U5uFrPA25jVBaz436iylTAtuNUoAby9achfOcSVbyb1ey-prz7hAeQuFRdewU-TeyxqijfmHi4Dd9YSRSwNhH2XvYIKg-nx5SNjYPCpsWl4v2deY0GUdecL0GEXf0ZUOffeCB38r-5C_UWU50N28ZFcyk2sSnMsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری فران از فناشون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/80745" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80744">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترکیب دو تیم   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/funhiphop/80744" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80742">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kZAOXrzQAj5em_84TlclNJjaRnKE6vdqEnRCe-RYea7er6AwtqFjVc6lZHYL1dR8PGAZ9GGCCRp6R8dKuvBuaUejbpmuv0sIzvwda_XSSvfxsOoaya77Je5Jss82f8j36kU3F-bnt_igcbKlAbI0_4j90vr8VbuPny7hpBaRq96ajAbaj3zK_tRTdpaR6b1FT9J7UX7xxtDZLBR3m4snyVzvDXxzSdaYOMVCDBz_ddEkK4CQnbsGYxqyAMP2OsbSSVfDPE2mNYOHcOrBOV9tw-7BHWW3vmyYBmmRPpWB1dgVpQvdpUfHSHulutjSU_dWEMGW5PuG-_cB_-9zcl395Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EkusIygnubGxCaWwEju03pvw9yI58gIBj7VcZfMxpS09ZN8d8OCRvaIQj715lml7tnKpjqeVuX-I3wsTLh7OOl6HcpYkuPCUDJi9h-1AiJBg89ZUI0o9ID-GSdZqP9iIsmcovEuLPiOLTp7u5a_l7kaBwMZ6GS4uy_Gl5KazknBnmeoSspIPxqJ6XEOzh7cu-w_j0bwazYcmAKOtjL_jQQKLn0muCHwYWDeJHSRjHg1W4xDNlBlyPmRIePCVd0McyR8HqbrcTSk5tL_-iBNkHGVIIdXwcybR9JtwaixyutItvaU7bs7URPbr0taqnFu9TQoE5HFOQwIy-TcGfm2t5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب دو تیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/funhiphop/80742" target="_blank">📅 20:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80741">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwDgLPawcwLRhuUow0EyPqDqW26rsT6mkKIZWcjNUJn8eHRogcf9mTVc0Hk6LeOHslysWbk4zA8QS6wZsf51wHxieXT9BQoIfWRZ4JoTyAuI27xy2qXkA0toQ872hv3II-Aj3XopwnDd-w4Iz4MVVkWdipZKuRhz9e_D8oJsqWuwU7UrWkqNnB0zTZ5zsFY52ZIC0i_N5SQ_2qFPmoIoPt6eqTYnUg23QK79UfLBgLsI4rUvAJkvJ3zjo9vZtFu-JU8pQdjDol0oyczQ7XD3Gv0KpSeDu9UIbXfWljld3Q6gRRZEqNJN3A04kZWkWEtvSnrGGuiBxmFNVjS40AZwhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا باید یکی برا خیابون فینال جام‌جهانی ببره کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/80741" target="_blank">📅 20:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80740">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b6ad923b.mp4?token=Fb7IIBjgHRtSF99jUn7IMRgrARxf0TXD9RXwKdYtXYqYX6eBs7YC0dyrCfdRmLI3IHrljyOm36HApqzsmuldpEPT-rLqLMiBGyUtmlMV1s-lKF-sQgD5bVyFq1oYnniw6A2DFJNR4agdEULdMSnRow5_zjI94XyoAoE-tBC09QngMVqu4ZZtAdlNc8so2KHxf9C6SI0l_H7iIRNBZbpUQSdbdxwF1PYu2krZILlsrpmBwnmRziTu1--OWnRIZvcdVIgcbrQ6gB0fpKrw9fG1GLXUMffDHnGj-FHYiU6N4re5Q4HRi4-KqwqwpTMOoA3l_X0N4i4kwnjXLuyji7nmtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b6ad923b.mp4?token=Fb7IIBjgHRtSF99jUn7IMRgrARxf0TXD9RXwKdYtXYqYX6eBs7YC0dyrCfdRmLI3IHrljyOm36HApqzsmuldpEPT-rLqLMiBGyUtmlMV1s-lKF-sQgD5bVyFq1oYnniw6A2DFJNR4agdEULdMSnRow5_zjI94XyoAoE-tBC09QngMVqu4ZZtAdlNc8so2KHxf9C6SI0l_H7iIRNBZbpUQSdbdxwF1PYu2krZILlsrpmBwnmRziTu1--OWnRIZvcdVIgcbrQ6gB0fpKrw9fG1GLXUMffDHnGj-FHYiU6N4re5Q4HRi4-KqwqwpTMOoA3l_X0N4i4kwnjXLuyji7nmtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت خونه ها امشب
پدر: نگاه به سن یامال بکن
من: نگاه به سن مسی بکن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/80740" target="_blank">📅 20:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80739">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">امشب فینال جام جهانیه؟
بازی ساعت چنده؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/80739" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80738">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اسرائیل تو ارتباطات رادیویی جمهوری اسلامی نفوذ کرده و ۱۰۰ دقیقه قبل شلیک موشک ها از هدف همشون خبردار میشه، این موشکی هم امروز تو اردن زدن همینطوری بوده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/80738" target="_blank">📅 19:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80737">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f776ec876.mp4?token=YOC2vRW3-5E1MolYcnQkQb8qY7hjVw98FBL4xT5ZpNmatSKIM2W1Ot0hAhvYgeosnU2pYIEbXXC9BpnsbimJ3o3B99k9uzOcwO3oRnTCojIYr4siT5vP7moCtqFpvOfz9Xzfmr8DLyWFMnazZ1EAvCJ0FyUyojly5DesF3Rw_SnIE4OdauS0vHbsc45YprCNXv0e8qBXbeaeaO1IrXpLxbvdGivCNaYeGLaKRxnuI2rQS0RnQ6ZXced1Tv01IMKQwh0sQpRHR8fzvU1IlXL1wUHqnuoQXMTmhmVKOpBt2aaS45QpLcI8ZYRPhPmsqkevRJQyLIEv3YJs19HLwPcK8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f776ec876.mp4?token=YOC2vRW3-5E1MolYcnQkQb8qY7hjVw98FBL4xT5ZpNmatSKIM2W1Ot0hAhvYgeosnU2pYIEbXXC9BpnsbimJ3o3B99k9uzOcwO3oRnTCojIYr4siT5vP7moCtqFpvOfz9Xzfmr8DLyWFMnazZ1EAvCJ0FyUyojly5DesF3Rw_SnIE4OdauS0vHbsc45YprCNXv0e8qBXbeaeaO1IrXpLxbvdGivCNaYeGLaKRxnuI2rQS0RnQ6ZXced1Tv01IMKQwh0sQpRHR8fzvU1IlXL1wUHqnuoQXMTmhmVKOpBt2aaS45QpLcI8ZYRPhPmsqkevRJQyLIEv3YJs19HLwPcK8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این قسمت مصاحبه جدید عراقچی خیلی وایرال شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80737" target="_blank">📅 19:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80736">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سپاه یه نیروگاه برق تو کویتو زده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/80736" target="_blank">📅 19:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80734">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آلبوم راکستار از گوچی فلیم و اشکان کاگان ریلیز شد   YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80734" target="_blank">📅 19:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80733">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB1rYcczZLwjHlw-RPOJ9_2MgJzjVrZH26Vf-bgBbh7jWchdifpx70Ap1RpyAWAle8gkAvbaSjJQJVNUXHrbQ3aeaTyWX1z0WbVT1-LLkC0XZaduqP4dRk5VKll0oN03zmLlIw_jR0HG2LiwRluQhNHEbydENtrLqlcj37c5Ld_4On3YNyx8EbPVm5DuN4MwS8BGDE2QHPET7K-PIf6nTX4vlLq4fmFZ6rVIDZrWxipYgPlqE8-o4rfZaiRy54FaYHPbVA2GN-0k4NRm-gPby08r3wFpgwIhXrPeHIlfEdnFp5bQloTS7Se1XzHhpZN4u2vDMK8sh8C6jcWsubTXHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم راکستار از گوچی فلیم و اشکان کاگان ریلیز شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/80733" target="_blank">📅 19:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80732">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fY7ALum3EWD9q2lqaZ1APWPRYorJHl5n72FAlsE4PbdOvkv1sKPm7OvcYN7wb1_r-zCBvEGBkOEtd7sTjruCWW-mrsAFdwTPsW2eAZ5UgIIMQA5Gk_lZs2PnpENMuWuLuAcrrIS6nFXo_S4O-4L_lO2Tq6mYvS7OQozupDBfOYhkF8dfkDpgCTq3PUojNT0LURxCfE_kM0w1CVKdz1_91luDa7zFqNZDBb8qGy1nuxpt03vabMFGnZoiP3FN27bUa-CEd9exqJ3RKEwYXzsj34XS2wTMGmximuL-2beB1vLd7EkUM4xSMlvj7_2JeT5_BVppHP_OFOQEhNMiZYa_fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا وریا یک اصلاح طلبا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80732" target="_blank">📅 18:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80731">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خیلی وقته چنلای رپی پست نزدن داریوش ترک‌کرده، حس‌میکنم یه کمبودی تو‌ وجودم دارم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/80731" target="_blank">📅 18:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80730">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تنها دکل باقی مونده نرخ ارزون بنزین بود که اونم اینطور که معلومه قراره بگا بره و تا خایه گرون شه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80730" target="_blank">📅 17:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80727">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VUr1sD4yAZHU4HTF17Y7LzEiV4lPV7WAnYcfGgt4edri8nBV2PsL6pVueTtDdpSqJzLyFyKgsLDiKKzwfPWt9QERk6hXRAOa_8gp7IcJonpZ7G9G0W9YxV7DPryjwFs92jifYJjA9JDL22NvRliuI3NOPmF12SQhpXXa_-hWhv604Uo5OHhCbKPGZOxDk09zIxTJV-AkuQLtY4t8fxtg-gqKXQLeovDRB1uXQrJgz3smDc5xE9DFOTtssr5k9okG7k-6hzO7XObWOtkHwe3bYB6cyzOWSY4rOTghIEYbtEKZd4fz3vX4AhvrujlMzRV4POV7eahckFrgqnzkqMolqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OzuG5Gn-Y-4CDXqgQNjRICCS8R-Go9YnyVF5hs7VAdzpaNm1Y24Ug9iO4tU5C1xtROcG5vy2GHKS5X7svJ3-IPHOkOqsKlCtlRFbuRSWCzBR6gh9q4RMDgCZVhXkIJU-ciy8-L0ZkJrAHzEpc_PvvGVfTEbOG1dyjWi8YkOlgG-_TjOcJ3XlOKlc4hZk3V5YvTbUMIUCQRDJ_aYhr-f6wNXKEnldb1l0NBC9CpQu69lrxX5oQCgXJeB2LDelkf-_1IWacrMFweYx959_e_ZeeclR1EgxFz2aqPn-zwdMRp9Lp-w9_szLqeVn1vzuAKzyqcOq7Aw4Dga1dgss_2W6TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PkZ_Slx1kPeeYxSSi67hLkPaYEjwUYtTLY5ezsruYgbYN6xEQvJSVCKRbewzJYMkwOV0oM3Cw9vVrrQwOz9JUCha-mA4SWBUL_l9JsaQFofWkBxtwOMjn7ouCBqlotfYD0zoy9Y7cItrjWbr77-7aQPY-iRSrojfZi4slzuBWfiPl2OkE6oI39XmpYC9UBYft7yP_KEtjewA3JRegL1aQKQTpCFOzDVg5xbvxru-LBipDHkI3j7atOVdrU71lwqNoaTviQ4FWq2JaSiweITPQwhG2kk39dn9AnXFjbIQ9dYRPfv72_veraihPmOOaFNG7nnsKi17SoADVOpNM5CHtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیس ال قلعه‌نویی:
وقتی میام ساعت میندازم و کت‌شلوار می‌پوشم، شما باید بگی به به چه مربی خوش‌تیپی ولی شروع کردید به مسخره کردن!
حتما باید یقه باز بذارم و زنجیر طلا بندازم؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80727" target="_blank">📅 17:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80726">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAvalNetwork - اول نتورک</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtXpuWkxlxaNXugGF-Wieq2Llux2iRrQ6sukbuVNUAcD64HcrXxAkU7XfNNiyAHBDkCrCmIYw0ZisehunO_a-mMgdFe8icAF3k0EjPWIdjWLG0U0fM2TM7xgza7qeBR8Wv6WCR1GC526DCYE3C1QmQbQnKwduk1m7xdfcIoWg_a1k61Xz5qB4-Fq4BY72mWgVMemdZzq5JaY3lyZ9JkioQWmVt4nhWHxkXYansHUfhghTa8EHgeb4hz-YtEH1ZEdw990hYoh6F2oJDLEkZtAiE_c0oKZ3KYdkLEUZezuJT01el0c3PiUeYGjcGRfVSGxmu6e_jA9cn9R4ZmWwD6yyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🤩
🤩
فینال جام‌جهانی 2026 رو
رایگان پیش بینی کن و جایزه ببر .!
⚽️
فقط کافیه روی دکمه زیر کلیک کنی، پیش بینیتو راحت ثبت کنی و منتظر بازی باشی.
🔜
زمان بازی: ۲۲:۳۰ دقیقه امشب
کلیک کن روی دکمه زیر و بگو کی میبره!
👇</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80726" target="_blank">📅 17:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80725">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فرهاد مجیدی اگه سرمربی آرژانتین بود خطاب به امباپه و اولیسه میگفت ما جامو میبریم اونا میتونن توپی که باهاش گل زدن و پاس گل دادنو ببرن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/80725" target="_blank">📅 16:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80724">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5BP00bQkFEObZH_lKRPgGJz5fdClxc9rC-Ai0ZRpANZZMlqXMSoYkCRtNt41nh6Jvv8IF8pQmDN8bKRQ6l_jp0MR_GfVAMSVKF7cYxiOWNKEhEVwJkqeYFhAwuCj6YfW7_msJEnWGqLfwn-G0LG2_1CmPMzPPcuDQr-Y8ZinqLZaUXMtsyND2IMM99mXfye44C3-xSj3Ar8534vYgw6cbK0l2YlHg95psyW0kk6JAht8K5ouQag-ZM6QFFBb7dXZ8P3fQAKOCGAR-FvtO8ee-tukq_2da0DDlU0iWmU0_-HWz67aAbBaQaWI535fPG3oensUQDlImxEuNx4yG7K3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۴  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80724" target="_blank">📅 16:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80723">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">چند تا موشک زدن سمت اردن که یدونه اش بدنه اش افتاده تو اسرائیل و ممکنه سر همین اسرائیل وارد جنگ بشه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80723" target="_blank">📅 16:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80722">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">چند تا موشک زدن سمت اردن که یدونه اش بدنه اش افتاده تو اسرائیل و ممکنه سر همین اسرائیل وارد جنگ بشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80722" target="_blank">📅 16:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80721">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhnzxWPqZEdxSJBGv3Ea1B_5Ts8qJFHm35tbWUBIWtFQZ0N9IqDdgCIPSdHtC9A4MGTXacgnarZVWHQx5acChau7KI8kSj7zK4JcWAQy4eUFGP6FWM54yfjhT2HVivuXQrh57r0iixCswrlNo7pckBMNzswr9RiWcIsngevGvl8yUmSiBZ3glf7O58n8H3QUuyRGZain9-FWMREt8Hs-wGHh72AXkOlrKWZ0b4e2ReFrtcPBuTUUQFSO_No72T64fvxuDRX56giykmFYSzNcwI46l185UXY1lmlFFUrkDur4R1ZQ7mhJ4Lbkb7sFpG8ByjqY_gosWv2f56ifp_iT4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا یکی دوسال پیش هم همین قیمت بود ولی جلوش بجای تومن نوشته بود ریال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80721" target="_blank">📅 15:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80720">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biXeEm2xa8vEGQtgkF7TuTt2LKHtshxo06JrHn7t0l0rnmclh7voJ7eoHeFpCGwLBI_iBu2SFM3zmcnDC9iJ3tYpdWZGpC4_A1tMJswMcHrY8qUMc35zCYZHdC4QvAa4l_3TlIHdETxTOXkoJiwMP-bydjWJY5nMMWzgTvOI3vErOvK0uSw-W4XZm8bujmPQ2e6SjZ6_xEntWNVJ9Zx6Azy4V0K2wziUGfXvpauOJVgcSLcBk-8Maf6V9GhS0PlTxPtBPGzkPrXrN189RWViKbUh0tHffERib5hICxr_Crc82-nkVczZUk_7VEkMpPgi4YjWMeuf6wuIAU3-TL34ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسی که دیشب باخت ما بودیم نه امباپه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80720" target="_blank">📅 15:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80718">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSM6chEFp2CM7jaZYmAc0YOIG8wJqhAIhV7HY7wcmUNhTIx8gHXfgmHJljPbtXOYDfgu1k7_ym286lWvrRrObAESmLdlztsTnEiOwpH7FfnJOHoAmSHUmY15aQaQ5UpKpB7fE43qvsbr5DHWt0gybUQ0f11KIQefEujDejYJU83G4Ufudjr0RDwnGlUbblzSc79WQ4p7Sb74inY5G8KUmBKtj55vSvX7OzoqjaNBVcNSapThkjMXc6DGgp1Oe0ViewTjzj5B2jOzR8hLDRSaUUYbVIMDqR_qyfzkQxEMTV3XowPkZbmcfIlnGWs6HBKZLvdKC-p1WuEMe6ZD56qFAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
🏆
فینال جام جهانی ۲۰۲۶
🏆
🕔
یکشنبه ساعت ۲۲:۳۰
📍
ورزشگاه نیوجرسی (متلایف)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- اسپانیا در مرحله نیمه‌نهایی با یک نمایش مقتدرانه، با نتیجه دو بر صفر فرانسه را شکست داد.
- آرژانتین نیز در مرحله نیمه‌نهایی، در دیداری دراماتیک، شکست را با پیروزی ۲ بر ۱ مقابل انگلیس عوض کرد.
- برنده این دیدار، جام جهانی را بالای سر خواهد برد.
- آرژانتین در مسیر رسیدن به فینال نمایش‌های درخشانی ارائه کرده است، اما با توجه به ثبات و قدرت لاروخا، قهرمانی اسپانیا منطقی‌ترین گزینه است.
🧠
تحلیل بدون داده، خیال است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r28
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80718" target="_blank">📅 15:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80716">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">امروز صبح گل محمد محمدی جوان افغان بازداشت شده در دی ماه اعدام شد و جانش رو فدای آزادی و آبادی ایران کرد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80716" target="_blank">📅 14:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80715">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">امروز صبح گل محمد محمدی جوان افغان بازداشت شده در دی ماه اعدام شد و جانش رو فدای آزادی و آبادی ایران کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80715" target="_blank">📅 14:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80714">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دوستان قضاوت نکنید منظورش کشور کردستانه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80714" target="_blank">📅 14:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80713">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huPp9rm0dVv-FEZZb8In1Gs3nqa8svlBjrLwMDjHktFXXOfe4Swu7WlgPloWXWTE4VmQ2JY30lD2aMn75kQkhNJ0ayHCrhPV5Wu1iscG3UagOahgNnCd_08Q7TJli8JSlULxY_kqN8bSCRA9xxT1s2NKtqaiFNy6Z6Y5piurK9l20yObjyA0gerly-uesfa2VtKo61mkPMKw1whJYw3apYAVhC00gGwAuaq0yMUdk_N4ZCMm8KfF4U90Ed1QDRn6iZrNHQGY-LNSwhTTcer9m1Ro2v3HNnQQzs9xcJQuZfEaxF-Dd5cH-QDUGglId_u7drQKzF2qHNy_lhurrB_SbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وریا غفوری:
مشکلات داخلی یک کشور با دخالت بیگانگان حل نخواهد شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80713" target="_blank">📅 14:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80712">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عجب امتحان نقاشی سختی بود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80712" target="_blank">📅 14:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80711">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دلار 200</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80711" target="_blank">📅 12:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80710">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دلار 200</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80710" target="_blank">📅 12:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80709">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">واقعا وضعیت خنده داریه چطور ممکنه یهو کلی بلا سر یه بخشی از یه مملکت بیاد، چرا انقدر ما کیر شانسیم ناموسا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/80709" target="_blank">📅 06:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80708">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یه شبم آمریکا رحم کرد خدا رحم نکرد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/80708" target="_blank">📅 06:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80707">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یه شبم آمریکا رحم کرد خدا رحم نکرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/80707" target="_blank">📅 06:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80706">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اهواز زلزله شدید اومده   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/80706" target="_blank">📅 06:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80705">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اهواز زلزله شدید اومده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/80705" target="_blank">📅 06:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80704">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ خوش غیرت 2 تا از سربازای مملکتش کشته شد شدت حملاتشو کمتر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/80704" target="_blank">📅 05:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80703">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6gmbAYf0r_t93NVbqDSmOukl_qEfK2NzVFMg-U5_U7VWFu5JTzkRNQFZFX-5VPiuVTQCTx9jiXlOoRznbCIfrdcAP1SKVQc0o1JScpKJ09X82OkG5MdaID_Ovn2j2bUcrV5k-XZgpTAYYA9hlki-C_-OVbMB9XzZiw5allrktVxLSVjZPkRX4bDkMX7wFkUM4s6T2DmHEk_PHlGX9dXrURMR1LsC3NxACMCA_jBCv4KCB6i1gtJHaH1UGjRael-vIh8AJ2AhoKocs9qo52W_nXTJyEHvFqt1iwNOtCBL64xyLNyQo5VX5nNcw0bJ8QNYkLXgrGSHuFXfQtaUCUGng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام بهونه قشنگ من برای زندگی.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/80703" target="_blank">📅 05:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80702">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">حالتون چطوره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80702" target="_blank">📅 03:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80701">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خب بریم سراغ جنگ فوتبال بسه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80701" target="_blank">📅 02:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80700">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یاد گل اوزیل افتادم</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/80700" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80699">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">عجب گلی زد جواد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80699" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80698">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فرانسه چهارمی رو زد انگلیس هم شیشمی رو</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/80698" target="_blank">📅 02:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80697">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80697" target="_blank">📅 02:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80696">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ولی عجب فودبالیه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80696" target="_blank">📅 02:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80695">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حملات دوباره به جنوب کشور
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80695" target="_blank">📅 02:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80689">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آمریکا حملاتش به جنوب رو شروع کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80689" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80687">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1zvdZUfjwjfcJL778iU3mRiWZ56gA5zS0EdVRGhyOezNhT1y5GHXSpRUCXEJ7SjYWdopzoOlTL0-sBdqDVOfJDsBP5oxdhWXcpt5gZBZdPZQlRE8i6rMDXjIP2rKRq3V0sm_KIyHVGLk1B--ZXJAB2c1qeUF19JiJJwaj2JDHgXZZcvAXELKqzrGkT9YEttTjiNwuMUE2CuLguXG653zd7yPYDlSnOh77Bo-st-gD9QJlM2KpF4G40VDJoN7yAHau5XI7Lgbf3lB7T-WmQSth2ASbmZYRNojkyhMBbtcX4kTgGwTIjF5UL8lHOxEX0QPl_tNodAy3AOZIcK99ISVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7Bs5TGHFf0EBugo0SRBJlZwqdp_wVAToiefJFNJAelNhNASmnZL5IBuDh7zo0ULa4HAa8ZZWYv11hG5KBsH10MYPZciII85TaduStHk3r3z_Ffmv2nudu2oywEUn2EXqxW4Kho167BiJWOWZ1j1sbEsd8iq7RdmgKdy6fdI3wzdDDXQm5BRk3g6Ni-dZRoss2HTXgkc7Q52t8DQT-cs13KO1D3SY4UBHaJzW0UHDO7jzXuEThZAu2yWW8w3Y3FpFnDXSNMied9eBDQadVjGcLwLWKydH13YivaLrnRpYowEnkd06sFJ54aL5hqbtLD5lrbg-PfwVTAb5V8g-ii1NQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">میخواستم پست بزنم بگم لاکپشت کثیف کیرم دهنت چطوری تونستی بانو رو ناراحت کنی که جبران کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80687" target="_blank">📅 01:54 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
