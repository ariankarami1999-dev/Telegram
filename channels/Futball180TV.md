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
<img src="https://cdn5.telesco.pe/file/DBUGyP9XCfgTskyw8EO2l4-RpnBK0_ZTVJWRtCI5E91WaIR6xpo2WHurdDurbgmH6xqcmllNw-UjnxmcpsO0d1oe-1Uv_yAmQrWuBOdtwPYAJWXva-WTUxitvYs0kQIZINNLH44h-RgFA8sccEI-2Ny-1zNJW6tXAbmlcBXP4gcDJqHGpolqv1_Yg051_vs4Jk95oaTlPCPveQkVazjw6hv1rsWx2bZXGe8TVociXohw8qF4np_vMxbtuyb8oyEO4EgAY87W5l98c6uyVxzLceXbO2eltfrEWo9rT9-s1wI87MTfZAZr42z_vwEj994isPXn70fnvwK6ZJIIXmt-Fg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 625K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 23:49:58</div>
<hr>

<div class="tg-post" id="msg-98644">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مندز تعویض شد سمدو اومد</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/Futball180TV/98644" target="_blank">📅 23:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98643">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نونومندزو گایییییید یامال
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/Futball180TV/98643" target="_blank">📅 23:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98642">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/MAhubVCTQtFylU83HKjZ24kFQPF6iq0ob3ddBgGHXLBVUkwYgcT56NJEVr8WQ2a-xOKU5rAMQBVUkKzk9wrkekQvULtUtHrMGW4f3nFUWuR-t-oLqNfyHF30-xv5rUgAc7rzE9uwyKbG40aNOUngDMy5cu0iKTr2RsoviIk9AAYhMdKQMmSAdPPThTfvAiikQJAh94H-j97aJKCzJHsq_PFn8Hv_sJaPh0ZgymoIONfw_bLN4RmMD0fhwfvb7YwzNAjl0pONbEb3Lx58LER2mbqRxAI5GgKh4G55fOwc9YvD-pzzGVEAgsk4cip6szXyYItWf2FY6yfdQnyxFEKGSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقا سطح اینارو نگاه
سه تا از بهترین هافبک های دنیا توی ترکیبشونه ولی دوتا مهاجم درست حسابی ندارن باهاشون بازی کنن بعد بجای انتقاد از مهاجما از هافبک ها انتقاد میکنن در حالیکه دوتاشون چمپیونز زدن و یکیشون توی این فصل رکورد بیشترین پاسگل تاریخ انگلیس رو شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/98642" target="_blank">📅 23:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98641">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🇵🇹
🇪🇸
آغاز نیمه‌دوم بازی اسپانیا و پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/98641" target="_blank">📅 23:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98640">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7cYEInv0bzu5hGNauXqY_EscsH16pw6geL2_STwMUSnY1VuRHR8uaL-S9CnOF8Rp1meEE2qTidm0QV6yW6LEk_evALr8hNECGDlskua5CpbmX07a4mbd9mlxrUiNF-9QPhFFfx8GEpX_Hm_-tNjQ1Yqgq3kx2t8jCuG9-Mo5d8Q5sp3Iewt0DlDY1UnooHvJERxZRL3TsLQSnUjLk6aoU3tV03ogeIDm4itf5Mk66YHaiUtJHUwMniS5niF44e9tHWUuMxl2nFG3XYoMSe_4UshYhAks0aGCdEhzBosvuxy5IkzLQzlzK26_Iesn65tYcAsSNXREscFpmw-YRRHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
| تا پایان نیمه اول، اونای سیمون دروازه خود را به مدت 564 دقیقه متوالی در جام‌جهانی بدون گل‌خورده بسته نگه داشته است
🔐
🔐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/98640" target="_blank">📅 23:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98639">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaW9KeS9h6OIuroqKfzkdps1PX1fjx9L4H7j9K-tUYLdEJPdKeJzYxZP2s43kWBIkfrniFImzKZWVmhAxYgZhwZrQFZnSgH0v7LiWqmrJ9UlsyIdbPNh4yIBX328Iv8Yjs78ajRFl5esuWBEu0A778utWjQUyXVqsPB3YZOviqC5qw5mv7STOyQmrvZYER9b43iu_6Rre7fmxprxe-Etn2CHtdUwQKXRDU4rPf0Qs7ZLUDdbJpWZFbjC-7DDna2A4k9t4hRIPqXXTFl7pplsrNw30nlqPV0KK1zLUVub2cK4lD30R-tTXCr7uWNDaf8DjutX-bTpDRqdq0-OA620RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گاهی وقتا هم کلا دو نفر هستن که عکسو خراب نمیکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/Futball180TV/98639" target="_blank">📅 23:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98638">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mei5dt0BqZgSIeVUUdAdI2Lru3x43n-UfqcTHsNGI4LVW4TmUsqimqxSMMButw0kU95UxYklpco842GO1_0nNdvXFZXszsknpZ5SPvB2eI8WouNmqmq_cdTpMfHspGvTIRJQTxPzpHljtYGJeX0fuvToZ9GgQOJTE_W9V5tvMF1SVKQZ85muTmSP5uOJznyrFgj4nQckEfdIw64m9jKLjqwY3tF_LtqtKPI6qrKL_AOudGzilH56xmTNjOXheui-W6U-GEja8ncf9SH6_c2NRjZNfagrVUAeJD1sR89mAerz6O17_P0L0iHT8ToP6nhOrMGWZ_8Ox3yTdmbk2lcCWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/Futball180TV/98638" target="_blank">📅 23:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98637">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgZliLKuN6mPtJZQoXABlgvWlop3Tn89fvLjxhjtm8hNbp1gwajBy7HotHTnO8D4ltMRDUTT7-SeDHIP_bgDWV_BG1hxN0ThAp3j7FCKLDxZ57xYz3bQHUyOKlXtsBfAjj78jayeRmObKFeqh_EoflHWlJjRflRtL35QbOT3yBkom52bek9X9fUH4vOdTtSZMOSAxWMTMfR_r1_ALjy9qh5D3_QShzTxAYwKaqlN6G0PWptk0wVR3N58jxA04uhpd129T8ou6bPA_emce-MPfzsjbdx0YXhmpU4b1zf54EexOOIMamASXn2cTK1_lhWWacNS1bjYnnw1n1uTY3rSsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
آمار نیمه‌اول بازی اسپانیا و پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/Futball180TV/98637" target="_blank">📅 23:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98635">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
پایان نیمه‌اول با تساوی بدون‌گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/Futball180TV/98635" target="_blank">📅 23:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98634">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/257e1f3178.mp4?token=r_wX9-gdvCDiiYTx6XAQujjOrJnLycGD80kcw7fiGaol7aPNmIr1CEA49Q2t80aT8iv2xFxpuiCA-0nKQ0WlU0lW0DWYR4C6tqOGt1LqmzhMiK0l1nPUpTcX2rBAjQQjtNTef5ObAAnyzW8nkwMnRwnPB6YYCV1kykI0iQb7z6bYn8IiQaIGDaLKSXRpKYMBNxJ9JZdOD8f-618oDoVhg6zwvjfgaPEHraGupKSIKCcSnntuXVSbrnILC2c1rg8Q20OGT7e-3aIa2WF2l1xu5j253FpUcc687aCAJKZB7uShPaG0u9NsSiIva8iIvl4A_OiMKCPAt8bYgEGyTrQqdIuk3tdD1M5OvZ1zeoEBWnmC6zkbQezY1IfHidop5lxWrZUXnLmWjDUo-Caxw8XxrUIW7dhQBXdRWqVDSA_jp618MUeVpLmXmAbA_QeH8zyBG4v_l_A_j_Yh8WwGe_G0WWXTmnfgyt5JQKTeBaJxD90WzGkFAH56y6SqVClWqWAmNyNXpp04FNTJZDp3KOkrRG_BTOAGmidsJHYWvlOiPzRceh9IMEdpTeFK4zVQzrzn21gzdPo9G2fIeIDS_yXhu_qpUv8pJoejXSKkZhV7Up8P6zvA5L7WujkohFL9aJDAXhROTB5G5mmaYB-x8lZtzufzq5yONuT1r7J5eabcVQI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/257e1f3178.mp4?token=r_wX9-gdvCDiiYTx6XAQujjOrJnLycGD80kcw7fiGaol7aPNmIr1CEA49Q2t80aT8iv2xFxpuiCA-0nKQ0WlU0lW0DWYR4C6tqOGt1LqmzhMiK0l1nPUpTcX2rBAjQQjtNTef5ObAAnyzW8nkwMnRwnPB6YYCV1kykI0iQb7z6bYn8IiQaIGDaLKSXRpKYMBNxJ9JZdOD8f-618oDoVhg6zwvjfgaPEHraGupKSIKCcSnntuXVSbrnILC2c1rg8Q20OGT7e-3aIa2WF2l1xu5j253FpUcc687aCAJKZB7uShPaG0u9NsSiIva8iIvl4A_OiMKCPAt8bYgEGyTrQqdIuk3tdD1M5OvZ1zeoEBWnmC6zkbQezY1IfHidop5lxWrZUXnLmWjDUo-Caxw8XxrUIW7dhQBXdRWqVDSA_jp618MUeVpLmXmAbA_QeH8zyBG4v_l_A_j_Yh8WwGe_G0WWXTmnfgyt5JQKTeBaJxD90WzGkFAH56y6SqVClWqWAmNyNXpp04FNTJZDp3KOkrRG_BTOAGmidsJHYWvlOiPzRceh9IMEdpTeFK4zVQzrzn21gzdPo9G2fIeIDS_yXhu_qpUv8pJoejXSKkZhV7Up8P6zvA5L7WujkohFL9aJDAXhROTB5G5mmaYB-x8lZtzufzq5yONuT1r7J5eabcVQI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
😆
😆
سطح یامال عالیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/98634" target="_blank">📅 23:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98633">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رودری به آسمون کوبید</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/98633" target="_blank">📅 23:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98632">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پرتغال خوب موقعیت ساختههههه</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/98632" target="_blank">📅 23:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98631">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/98631" target="_blank">📅 23:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98630">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">واااااای تیییییرک</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/98630" target="_blank">📅 23:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98629">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چیووووووو نزد پرتغال</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/98629" target="_blank">📅 23:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98628">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">واااااااای</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/98628" target="_blank">📅 23:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98627">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اسپانیا خیلی موقعیت خراب کرده</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98627" target="_blank">📅 23:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98626">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">چیوووو نزد اسپانیا</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/98626" target="_blank">📅 23:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98625">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SW5IpSpB6c_FTy6UP1ZhKKMIEuTLN-3sn970B0XCVYouSjlrWzVXg2aC3iI0XszTS47Rq5Yk4PeYH-7HL74zQDy60DIh7ePpwJCL9We79BxGFBQNA6vUKvebpQ8YonFqRfZRaGxiGoJf3cx6lgLCs6dFCxXinS8rM-hnsDu1xMAhggaT6HoDiSeQ6HQKkHA_PpM0MZXPLPNz_hpDLLJ1nZeOXfFGSccASPKGcLtfwHE9cQ9ibdc4D9wIZ8bHamuSuCk6ZZGmo4r8X1w0UlxTTPpnOW_giWK_-jJ6GpWnKoaOHrknpD2i0x5KTlyB5GV463le1PX6iKk8VzxuvkLuqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدین شکل
🤝
🤝
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/98625" target="_blank">📅 22:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98624">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اسپانیا خیلییی خوبه</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/98624" target="_blank">📅 22:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98623">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کاستا چه سیووووی کرد</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/98623" target="_blank">📅 22:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98622">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ci3ezZmUBj8rL5B3-BA8QhftaTCH6BR8TssvfjawfbzJopLePNiNAGAKF5vaHMAoL3qnPQwBUdzSZ_g9xx0iz2pFZ893ZtvmNrDotXtbmtqUC3N4aoFcKTLAFfsAaDrWxv0rt8DmUCYEPxS57SCFOv8Ded8wAd1aODyCvJh-7aCplC8UgBhSniJweqNb4tcCY8jBtrEojbMAQ4ND0VmFWh4PEm9s05W1fUdVC3Lqb1Zb_EtImvfHd4Q0gVgzw8dMcmTn02EVoy6cKmMmyE49H0e9J46fDCioVQiSttq0PuEZEV9m4Q99hSQATrEyTgi_R7ltcGl-7sYX5MiciB2oHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اویارزابال اینووو نزد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/98622" target="_blank">📅 22:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98621">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">چه تک به تکیییی</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/98621" target="_blank">📅 22:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98620">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وااااای چیو نزد اویارزابال</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/98620" target="_blank">📅 22:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98618">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بریممممم سراغ بازی جذاااااب پرتغال و اسپانیا
🔥</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98618" target="_blank">📅 22:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98617">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYLtSzlFbRbpcB9t4v0W-YKpI-i93dIH-Mj47qwg0L9VgT4xceyHuuZHghMnVqT8O7pRAVwIBiSfE_6gsn9NhzkB_UC3zgmAsy0V40X1CwQ0cyKAiZUeGtIBfW8WkjOgvFDKGUbfqd7-jxahmV_4lpCwaBbO0sfuR4cxs_IQXGvYV6-4qNF8dYlhi3jmtD0bK5irPUkpb8vCgYcb6L_dfO1LD2Q7T6RmDqkJJCjl-T2eoNm6ONdumyXutksz1F9FBrzzV20Maw2c907hBA9sl21iaaeSjvFGv_tpl-ztDNTVGHhtEiyaq8-RU1w78mkTzjf0p4C0NaEvkrYjM7Q0gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنرایی که امشب تو استادیوم دیده شده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/98617" target="_blank">📅 22:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98616">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLhvdQhUgDhrE_3YTjPaPl1rX9FrJ-1di9mKI5-Alw0pZ3B3plXlvyisHXOXVuBUKfuawt56me72ww5p-ylF8RIHd9e_m9SNkmv_VbdFoq_gjHfLNw-PmbyYzbkHG40fk9WNjPyjnx070M1kaayju3XP8u-SwiYadfJRejWbdy_Vl3NRcrPeYXn4vAr6izZxsMjNr6ybYMR0LzWd4q2-jYQ6b9hksTt36ieTnffddbyGePnteAWOEEyOEsN1xRTWxaY8Wv2qZpEQhEF6ns-hFJw8SdCLjZm9uP2T77gmfSujmqLF1EZkptUehO6ZEETyJZcKFX4bncG4Mg9ytYWNXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریس آماده درخشش تو بازی امشب.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/98616" target="_blank">📅 22:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98615">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5jwArckw-f1IeJTCr3ucGyLH1AN3WMwN7pYZvLaeKCksWBFeZ9KB2F6L93YAgzEkB1dYgcEVRTW0wDKM4nn02qYSYIXW5Ed12cjqnFfNxg6QKW796ZWxVGRkt6CNiyfXG6_Fuj_YnoYmk_VbELRQs5TCiBwdluRydbcpEVxJyphikagjP465eemws8dwvmliPxMt7QTxKr-3p6eDLQwYrf3aFGK77Sftwu6gr1B65VNVmADJ0WXcwGYd3jyqpAjzfe2okJFZ4sVx4eDPravWcdKV8jIaDgIcTyjHDRXoJinAhLiR07MU9jOzp73Y0waj1lY7J8z8MA4sBZySrfpYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
😐
اظهارات سلیستی آماریا (نماینده پاراگوئه) که لحنی نژادپرستانه و بسیار زننده علیه کیلیان امباپه داشته است:  ‏این موجود وحشی حتی بلد نیست بنویسد. به جای شیر مادر، با آب نارگیل بزرگ شد، و باهوش‌ترین موجوداتی که شنیده، میمون‌ها بوده‌اند.  ‏باید به او انگشت…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/98615" target="_blank">📅 21:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98614">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😐
اظهارات سلیستی آماریا (نماینده پاراگوئه) که لحنی نژادپرستانه و بسیار زننده علیه کیلیان امباپه داشته است:
‏این موجود وحشی حتی بلد نیست بنویسد. به جای شیر مادر، با آب نارگیل بزرگ شد، و باهوش‌ترین موجوداتی که شنیده، میمون‌ها بوده‌اند.
‏باید به او انگشت میانی نشان می‌دادید، اورلاندو خیل (دروازه‌بان پاراگوئه).
‏یک کامرونی استعماری‌شده، که وانمود می‌کند فرانسوی است، بدجنس، ثروتمندِ تازه‌وارد، مغرور و زشت.
‏او در طول بازی، تا سرحد مرگ مضطرب و ترسیده بود، درست مثل کل تیمش.
‏حتی نتوانستند یک گل به ثمر برسانند، تا اینکه خوش‌شانس بودند و یک پنالتی گرفتند.
‏تنها چیزی که بسیاری از ما او را به خاطر آن سرزنش می‌کنیم، این است که بعد از بازی به او یک سیلی نزدند.
‏من حتی طرفدار فوتبال هم نیستم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/98614" target="_blank">📅 21:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98613">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuSoGlYiQnk90JvvUxufp1Uhevu9DII549mAm-seFAHioxlcuF_HzVF8kyLFPZ9PN6BrnljSvJ9Rap8yC3cCk0vnMeKiVD45G72OOV3GoLej09Ok6QyQxE5Y1CI-Y0VHFpuTEG80PQG_6dYN7kLRnuu0oE_qvk11-TCR-vU4M3BAlXaQ7YQlb-Jn2PdbnbghnZ3gVe1tzyzeijTV55hPESPQgavNQv5-dOUC3X7XEg_ttOHG9dJ1VvaAiLcBbalBkOaLCl1caPSLCJO_GmJ0nnTCAeQe7QEyfEIMt74yc35IhabzNvx8uU3kIFkGOW3xOq745e8KG3-mzmeWCR1-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دنی اولمو:
استرس؟ ابدا نداریم
اومدیم کارو تمومش کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/98613" target="_blank">📅 21:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98612">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWBceusFIvGtz7JqeXsjkdeKUKbt9MU-iVFPRdnvqVe4sGYUfdo_8DmDTwo2_vIoeFConywqZo2UR7p3WDyfSPG9ERzWSRQurFpcWxY2t9wgy9zhFZBB0uhdcUO2atgwl68__SeTAxY5FD-sUDk6ANpnmFi4qP4ESXhJgqKGXIikqMzx1I8jGz1SJRYa6qyn2lBVf6W_F_4K1MD6e_4TgjOzNKuNkQ36j9vyOdhVbUWzhF0BknHQrWzwzdL9mEfaCc41Ad5o8PGsfz0xo9BaYTnH3DoAxWu10y5fcN9p-hfBMswTvrbVebEYYzdR-OE6V_YsJOOdx55CXmXhY2jO6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
آماده برای تاریخ‌سازی مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/98612" target="_blank">📅 21:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98611">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feee130828.mp4?token=DWaqxxU6AbVMd6DPHp8O0BUjHYJl_cGIq1tzPw7H0sJ3kS2nhht_OWlAW3YX0UjbfX1HBKRgfE1jQY1dlIbQm3JgKdcDFrkUAr8loU-w6Fpaj40RZpAAybGPRRYMkhOWea6vdkj1zMBEdeQFdjY9QPsqJWdGtk3oNhdjIhi7ROyYQEao0E5q83B3lxCqI76oqdAPFsEeoGjSvcgypljXUVGhIGCHYZlZoQ1bdXImkksdjC6GVL5PunaW33NmhZRlmPWaRy6cvryoT3oFH2jqwPUev_lqSvmYNFeOTH90rxBpH90DWA9b6SXb0v9_jkOs_JAQv3Q0WxvAKV5Ca378DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feee130828.mp4?token=DWaqxxU6AbVMd6DPHp8O0BUjHYJl_cGIq1tzPw7H0sJ3kS2nhht_OWlAW3YX0UjbfX1HBKRgfE1jQY1dlIbQm3JgKdcDFrkUAr8loU-w6Fpaj40RZpAAybGPRRYMkhOWea6vdkj1zMBEdeQFdjY9QPsqJWdGtk3oNhdjIhi7ROyYQEao0E5q83B3lxCqI76oqdAPFsEeoGjSvcgypljXUVGhIGCHYZlZoQ1bdXImkksdjC6GVL5PunaW33NmhZRlmPWaRy6cvryoT3oFH2jqwPUev_lqSvmYNFeOTH90rxBpH90DWA9b6SXb0v9_jkOs_JAQv3Q0WxvAKV5Ca378DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇸
هواداران اسپانیا در اطراف استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/98611" target="_blank">📅 20:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98609">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E_wJpjH35gWad0HseHEEUBvIsZpBXag7HYx2GuQxbs53yib9GXEIsx36tWy7OD8ZKhI6igsjzhbLDgItkDVtTCJRn8j1tF8EK7eksa1sDRROiAVmybIOGBYNPZ8R8EseA-jXXFT_cNZvsaT-yiNgVsCbh9gAP_koPitak4SjIyPB_HbfdVv7OhCNvBt6N-5VzHixJ34wQRfwms-awZhH7dHPVI8_hfzRsr71-BhHfX2nt999dzjRX40-vu47vRcs1IMHFoGwBdXNgss0RWgI3xjS-eQp3PXRwiKA8Ox85DcupmCiHblbmHFo2Avve1Ef3Ba8RZCW0dgS0g4pLDgPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rk0xNCOXgWykxXZQXlYZ8UGMYBUOF8R9vAcUk7iM38T2DPMtocAyGNC8CCaJZmLhIVJluNZBDWj7NETZeFRjAUKiSNijmcq_o7k9Fp8hqb8zIWgY8PX7EH__NIgkQ0jJjv84ji1OOehxpxUNXxr_Br8hoesVSHlkdhJ98iddcYX3-nupY2Ev0kWyLSAIFbeZqVCcN2dOtOBEluWiopBtkZa3LwlzDXJUjTRPLVPZkceONO5jxW09y91HhycG-8zHCNi5C_xqGPzCVk62aeMMsx9qz_f0B6Qso-kfSB7BDqid5jER18uFdXVtr_P0133nKNdrDKEzTG8cTyIySo_MMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
استادیوم جذاب دالاس آماده بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/98609" target="_blank">📅 20:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98608">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOAY7W7eY9w5xYhF1TuSO6776G8eaGp1Hq6--bHHgoSO77sEW-4iGBLw21XCBY3KGbYFZ2m7zxgs8Zb4QSp6DvhshNw9qmKu9QA1Qx-jV-Fx2EUwi-BQuYRDIqm4VrV8nFrH5CL3ilJ7CdAGEPFrAqzeOMVGvvFN3QTtvEKmD7ZpiHvMI-kHqS4b5zkzIKL7Lq8NfrFlEkK7t88xBLWLRsCyZ5Z1pLAgPRwaChoI5M1_cVa3ubCUv8SFRtpqvRW8ckzc7tf8SlCdpLMp_WyjqW1CItLzx8Rkdgdcs6DqFqYm-QGWvybGmOtO3CJ5uYrr8wsjExPMHlTDalp7MPj2Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رسمی اسپانیا مقابل پرتغال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/98608" target="_blank">📅 20:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98607">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeH6l2HhR509wBOM013gYrag1s6lnzps9KamBI7I1otmiI-eGpYuM-zlBrwVq0kjoLHzxCQFGxADeyolqbHNQIXxiD3akIHfMYQ35nHjUu2OqiSVJvUhu_XbtnA1ifZfYxtvGyxdxhKoKggxdxXWkhYXqCdFsZrIHLByrW3hCrwF7fCSZdA7qYKHXHr0w_RUR8V8VEWtC2QojsvwlQyEKESaXaXje4ltHxlAiShtI8mID2avB55W0C8Qq91KCi6jqPmNr139A7DGY6MR8_8F4EdVukh1aSvLJfzEpVLsdJZsP25IsZCOUziDZygm6Bt7RZwVC5CJZhikHgTY1PinSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
• بهترین ترکیب منتخب بین پرتغال و اسپانیا، بر اساس وب‌سایت Whoscored
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/98607" target="_blank">📅 20:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98606">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6kDjyflAAI3tqnpzwchdu1ZIBDumgXipl0UUzVR-gc1qWBpvqT3FQd5U2eGTWHCo_npkeZCmv1z5E5x6SMz3c87ZWV_UYVZ24M4YsIZ023g4wN2AF21OHFhZYu0ph-J1xRUqwEjOlzvniqxNZxX6o8jp9nHhZ_UqkQwgjqEYbMNMVkza-Ashetxs_isne45-QroSh8AKEcdhXvpY-S9y3v7MDODQ8qWTaE64P9cVPfhk5IzWfZKN5KycI1xkGzmApLYcPN4gXs40H6lHFf-XbsPJEIGGhh_SJEvjQnAbhuqB0fSi8JFIH9__oUKtI42Y0nomNNzxOnRcjDo-U5Ixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رسمی اسپانیا مقابل پرتغال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/98606" target="_blank">📅 20:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98605">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4XqZ1rP5iNTgCvtdd5iTQAaii0DaohqGTGC7ve3BD_P7OlJR4z72X-dDQGW_94sEwXZvs6TzjA5WEmqkzPK2N3IhE3Oi_OnEKKqp3Db5O9xQ3S30SKRBMZ9tGgjpgBSlZt7t-a9wwzj4XB0rkoXp1NdLtVzmazHNlrewsIpT3cXo50dSgD3wZ5wQwHjuYS7D4qlSi8hLUTg7txBXyWYOh14MwD3Syawa50HO-fRefccOFyLU-Sa2JjHL2kqI_su_Qx8N8FfidE4mEmcS_yTjp2wh7Wt570M__aMo8u1Meclx-P5XWTQZxNXbRnv3lT2WsuZHMbxmmie2MH8cgFODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
🇧🇪
فدراسیون فوتبال بلژیک: اگه امشب بالوگون بازی کنه، درخواست نتیجه سه بر صفر میدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/98605" target="_blank">📅 20:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98604">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqJAaS6qdsSafbN-L6ZMncrnbPxhpTLU6LLxHmnLO1qQb5BhzBrNJ-JxcvZf3oBvG66BKXRH8zQsUZobWK54j6OAoivEozVzH1-Dyit-9nrW13QiN8Pwd1ehixqkaWpJ5ha6kQ0D3UxJpJn2lrJpYk31ycUaz4odQMT5aAJPGBZjZ7EmDmcJM7fypgxcF7BbxdUQuHYrq7WB90lQyqnFOn0vZ5Eie_iMOkIyEPSrS_R2SZLgRmFDjnD--pNLyUP6wYKMlKGpRKnWavmh_3iAzGyWKXf4cl9USJeSm8A3pV2LDNFb5whjXvRRVuw1OE2DmTJuH_l-dTc_GtL0sZqiyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
😐
رسول خطیبی خطاب به محمدرضا زنوزی در استوریش از کلمه حرومزاده استفاده کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/98604" target="_blank">📅 20:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98603">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
😏
😁
دونالد ترامپ: فکر می‌کنم کاری که در بخشش بازیکن آمریکا کردم یک حرکت تاریخی بود که اگر بایدن احمق بجای من قرار داشت، اینکارو نمیکرد
😐
😐
😐
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/98603" target="_blank">📅 20:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98602">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👀
🔥
🇵🇹
🇪🇸
خلاصه‌بازی آخرین تقابل پرتغال و اسپانیا در فینال لیگ‌ملت‌های اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/98602" target="_blank">📅 20:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98601">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbSa___omsMLv1vO6VAJcwgXRXfOVu7GYoFQ_e-oOjXYvJJtdbRPAphVT_-9hOAjTl03qVdXmrC0L8uoXx7WXZCyU1XO7_TqWDHXR4NOT9vuwEdK8pTG5IqgPyVpMmk9GjyXfuORMX4Qq6e2cdEfA_sQxFEHtgiucudxhwNDX1b1UhIFBb_NHHiV5SVVZrbd3Zp3yzhtNvFYAHqVKvO5GWdKJlXP3fSa4iMtb7AZJ894HUa9lArMBD2ucywpbZHq7hqMxQh5a2rFR-7C_jmiYvXXqmhRkwbA0_ODem25rThecDHrRDNMinOZOQCvfz56Nwhva6EimVXZZvTzBSDfuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🟡
#رسمیییییی
؛ مارسلو بروزوویچ ستاره النصر از این باشگاه جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/98601" target="_blank">📅 19:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98600">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb28cb71f5.mp4?token=fJD0dvDRA0EBDXiGzA2y71M0dUla_Qh51DbzPkwzPd48ftyueAEw9CZO9OE3d9PfvkdOyU_WekyDmLeI02Ej1m9yKXwvUobmH6QYMA9_Ztql613sNuJDOy8MdFIdBQHeh3ojzECVdtva0dnlbUVuv83KLqV_44A-eVp5RWhrCprIutQiAhws4BxpLoVr45MZr5IS29_omEqJ4zpD4i7WL-fbd0_fWnAi16JVwnY1-U3pnQ75QiQFtLjn93MOyKtIimjto__rD_co7seUduLo7IileQa5fxVN9-myMmOkdN6Oj-AOvrKPMjsPd_aLdjVrywPcLDGssKFUPHLjDdhxDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb28cb71f5.mp4?token=fJD0dvDRA0EBDXiGzA2y71M0dUla_Qh51DbzPkwzPd48ftyueAEw9CZO9OE3d9PfvkdOyU_WekyDmLeI02Ej1m9yKXwvUobmH6QYMA9_Ztql613sNuJDOy8MdFIdBQHeh3ojzECVdtva0dnlbUVuv83KLqV_44A-eVp5RWhrCprIutQiAhws4BxpLoVr45MZr5IS29_omEqJ4zpD4i7WL-fbd0_fWnAi16JVwnY1-U3pnQ75QiQFtLjn93MOyKtIimjto__rD_co7seUduLo7IileQa5fxVN9-myMmOkdN6Oj-AOvrKPMjsPd_aLdjVrywPcLDGssKFUPHLjDdhxDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای پرتغال واسه بازی امشب آماده ان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/98600" target="_blank">📅 19:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98599">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8c30bead.mp4?token=U7694CqSXs1oYkMNm4_JnGrWbfH7StqackGtvDePyGBWPhVcEFDaSGLWBeRHd7dZ4qMSwGBhKDDDuX8CDXV4M_KJVBAeh26xDyMK9wOxp27zVpeSDD4Kc1Df4NmQL1cwPgX6sENYAH3-WcIouh-DBsyo41PMLohtKE7_9EtPelMMuochQFhoRU63ym5nfgHe7XvsJ1R75arJ51Ea5mTsQpuXtZBOWlKQSMAZn1mVOTLr5AukdAE96OGGlUVUwYgw2MqP-Ufw0MP81cIFvzy0l-Orql9CeDlPlbxHJ1sYztQinka4xjpvqCJv0Kfd96lVxhzK6aQNux7fKizXeO5I_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8c30bead.mp4?token=U7694CqSXs1oYkMNm4_JnGrWbfH7StqackGtvDePyGBWPhVcEFDaSGLWBeRHd7dZ4qMSwGBhKDDDuX8CDXV4M_KJVBAeh26xDyMK9wOxp27zVpeSDD4Kc1Df4NmQL1cwPgX6sENYAH3-WcIouh-DBsyo41PMLohtKE7_9EtPelMMuochQFhoRU63ym5nfgHe7XvsJ1R75arJ51Ea5mTsQpuXtZBOWlKQSMAZn1mVOTLr5AukdAE96OGGlUVUwYgw2MqP-Ufw0MP81cIFvzy0l-Orql9CeDlPlbxHJ1sYztQinka4xjpvqCJv0Kfd96lVxhzK6aQNux7fKizXeO5I_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت امشب هوادارای رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/98599" target="_blank">📅 19:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98598">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH22T7p3wXumLsTYCY4ob5u9qjSDm2LWOWfpg1z9yXqYRzMgV9vheToFuULUNvat259A2Ec6iq39Ri652Nks5lWeE2bt4DKp7GMCD2hJFGTVeGPS1qthMjiZ3X5skWkKjYVPJ833hrv3rdZ5G4bxhIzZiqtgMHxtOvJ2yIVJGKvfSXwGz517Q2Xa0A5DwdqlO1b7fNvEw-Swu1C7z5BiJIaFLjH9YGLMLn_Lrn26o9kIzB6_MdTbbNfXOZSnER2BizDMFwTt0idlARcfrtaRJPaelfIB1Tk5LJGuasbFhGfV0Hdvb-qrNpSWJ9NWWnGinIe4S94KVr-xVGigfl69fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پیش‌بینی خودت رو ثبت کن!
🇵🇹
پرتغال
🆚
🇪🇸
اسپانیا
🎁
جایزه ۱۰۰۰ دلاری بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه
👇
انتخاب شما کدام است؟
🇵🇹
پرتغال
یا
🇪🇸
اسپانیا؟
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود.
https://t.me/betegram_bot?start=p2_r4EF37DCE</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/98598" target="_blank">📅 19:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98597">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔥
🇵🇹
🇪🇸
انیمیشن فوق‌العاده از تقابل امشب اسپانیا و پرتغال در مرحله ⅛نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/98597" target="_blank">📅 19:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98596">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujKy0pVC0HJIcqaxGCMsK4az5ulKlCXBSUZeK1yXga-QkP39mIeCW-1mIYUmoCngrzGOQCCSmJKjPb0F4iy2E9EGxGmH4l4VXimvOv2jkno8V3NB1_WFE4vtGTwWQP9EPVnjwFWosUCvq_lXB2IwUX1rFctKnab_V9zT7Ruytvii6FYr-muJi8qsYWnmPIZlb3DfJpolD5GXCJXFxvYhWk0Igv6aZMOa1uowXk0ercbE6YZns7MxozuMC_zFy4DIbhgtWTsahb2lYEzWH_I455-vjsLZfEfTnzEo9-9QALSWAOrRz5dYmaU_AGFCaBthsScVJ9cho68AHttZJn_gKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنان با گلزنی در بیشترین ادوار جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/98596" target="_blank">📅 19:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98595">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49227f7ce7.mp4?token=TrlofMU4whT2OzimWPaEexA-yiHxyPuucAQq6R0UvPYQWOf3TJ-u3Cd7W8vwZ1PNdiGYpvAIqOUR1ZaD7jSk2n3oVbGv_xvtKhw1zSHmMktacs7Bg0yIV4G5ZDgOjToY14iMO-FICoCPRdXozggJLguvmhPyZtnhrdyfqt9HB0X-UlBYNO3os34o2CB09DhdXMP_JB_WDK6isdkxKpQWhGeeSV2E_jnYgMANbTgo__eDdVbnB8S1e58CIQ3KlmfqxbaS0XX-V1iqZt0chkBrVzjUnugygOkoFGWYx4hYm-niV7bwh2fPe8sI_NcVn605-_6ztDzApLmD0CEtJk1Q_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49227f7ce7.mp4?token=TrlofMU4whT2OzimWPaEexA-yiHxyPuucAQq6R0UvPYQWOf3TJ-u3Cd7W8vwZ1PNdiGYpvAIqOUR1ZaD7jSk2n3oVbGv_xvtKhw1zSHmMktacs7Bg0yIV4G5ZDgOjToY14iMO-FICoCPRdXozggJLguvmhPyZtnhrdyfqt9HB0X-UlBYNO3os34o2CB09DhdXMP_JB_WDK6isdkxKpQWhGeeSV2E_jnYgMANbTgo__eDdVbnB8S1e58CIQ3KlmfqxbaS0XX-V1iqZt0chkBrVzjUnugygOkoFGWYx4hYm-niV7bwh2fPe8sI_NcVn605-_6ztDzApLmD0CEtJk1Q_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجم نوک های برزیل طی 20 سال اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/98595" target="_blank">📅 19:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98594">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/98594" target="_blank">📅 19:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98593">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PNGGUplsz3cryAcFoVydw3RUJfw-UiMITo9AAZpJMtxvVtNAXaB1zAjF--S2dbCuX2XCsfGDG1MU7w2x7MR8FDQaMn6QVBBJjfbW1Eylj8Kr4s7jZ8OPNYST_rWRctQbJjvXyQ9MXgMMD4y_rnFWvEfF_BGohoFZgn737fkhGB8MbUzUrP52p7pKkmTpMCnOfZZ3f4RnlQ5IIpvS3wbHnGKO5LvsQo5BvCnMjAhrbVcl-6-Dzcn_GJZd2xTCA7FM33a6G_0g7YOjS622nIe-mxH2GvCOdmWuUNEzg9OWOBiZli0D94TgWUP_utKECxAjK-Unxa1maSmJYMO_tbnC0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/98593" target="_blank">📅 19:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98592">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D86FwsaPNqQXNrIYgQFNETSxsfgj9-vQFx67wIFf1aPS4me6Hv4Sa7-_YbACcjvI4V3pUx-YKyKx-g3vcRfKoh7LWwdCiehhBdLN0T3zMNSEmOSOjp6RxWRGIdtxw0zl0EdH-JWgOTbz8ktbEbXzo_shtQcSs7gqJxMh3pWhjlYV5SehZ3pgkJWuP2Fc6ca2CkbTocBIYPhT7_2aTmBTtGkVGq5wLcEJsxmVMTtumi6dikktv5W8H6bSIEpDx-NgfKpb7mqXBtJqpHmP4D852NcaidPLtMubkJ3mFSCrkmRVfJW-HHxsGWEW44By-ESRfPnlu_xOC1IZlmRTrmgFUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یامال قبل بازی حساس با پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/98592" target="_blank">📅 19:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98591">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
‼️
🇺🇸
#فووووووری ترامپ:
😂
با اینفانتینو، رئیس فیفا، در مورد کارت قرمز بازیکن کشورم صحبت کردم. این غیرمنصفانه است که فدراسیون بین‌المللی فوتبال یکی از بهترین بازیکنان ایالات متحده را از مسابقات محروم کند و خوشحالم که دستور من را به خوبی اجرا کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/98591" target="_blank">📅 19:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98590">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZ9Xk3RKDxpXbCCCkeOQNaLRRwJCEpdgqCjtbpbWX3YMZMnusSvCxT4thNGYmnCHo-tYB5cGUtNODE1R-b17wkJB1FdAnUVqORPXqZVAeINeEcbiluh-yLE1aZcNavsxxBfs7-oVEq18sHC7_cdjd2d-rc_ALM6TRUIYqwcq2qZ1V89vJRIVMdUb451SJtlSF3B9h7J2KyMHOHH9A_UNn5Yp9vq_pPXZC6QG_rIIcG94IicJEnlDg1daAO98VFaftcBOlV8A6u5PV2GHME7oyh4TjA3wyW0kFtnJuoIHJfU9R2J95Q-PfPAAZOlQkoraUQ_gCGsnmUpxPfP9IKLEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یامال قبل بازی حساس با پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/98590" target="_blank">📅 19:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98588">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jvnkWGkvVIXUwSSeQ12VorPoi5-ZjI3b41KvJbuaBzK1Pt5RogmT6lx-p-AiNzh5CoHNpiFRlhykRtdPhHbuaFlCE26WuAbkMkiz8IE8gqNPLcBTKq5VSpQq0GdLvNmc8xY0AOKd08e7GCi_upqmcBc58HoBE_t6C83o_EvLZ7ochOjvBRvm393VIxZdI2SW33YKjathkY_BS097XMuiHEc2460Fs-0m2_5oiJLkvmRYzpD3mBn-W4QqUdfwo0SG0whlQTVIzuzftwaxyr-M_Lv5BXhd7tq1vR2Bl-OudEbZzys3iafJoo6ZXBkyfEmJDoGw1wFxVd1KNR2iim3Nng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pRYurzXpV4xFPA8qAPvuykRvcy0gRWKNXRMrN9xa5O1Vysa66pAqcNAcbPtrWRb89pYma0pvQhV-YXIMkLCIbUCH1czirqCBycWS1cTKjX2eP2x1QO1mJN7kfJDa7QCVF4v76Gu38kwkZ3K4F72fqHyIwh_kufObGF0SpgMYFHX_5i91a1DFxvZFGGZLVLQpRIg2ZCiiq6CAoNO_lm1cn0Bhl0Zs7uhqGXsdmsh2G3VkjDgbHC8OvDkUcqJEb0LDs3A7egdzStT-9x5UpnDlrH17_dqYRwNncF35Y7qDv9mYCD_BaVNzermcnJcIDRBmXeXP_6CBJNEsJEjyAjq0TQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
🚨
میگل سرانو:
مورینیو ترجیح میدهد وینیسیوس در رئال مادرید بماند، اما معتقد است با توجه به ترکیب فعلی، تیم بدون او از نظر تاکتیکی منسجم‌تر و مستحکم‌تر خواهد بود. با این حال، او تأکید کرده هر تصمیمی که باشگاه درباره آینده وینیسیوس بگیرد را می‌پذیرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/98588" target="_blank">📅 19:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98584">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j0TiQkSNXZSXFR2Z2gjaaAwPvWYL4bYkwW6NCEzX82qsbX3CIoywHC5vHFz-EGI3kS4zcGD2BCqo3O2M7E1Nv0EvS3_E6yWQv73w-cMXy6_g4Hu1dIq1noTLo82ZTzdfzjkaXsTRYVgHkO7qgztfsElP0Eg4WRjDeBmx9ag47lLbgaYnNB9gVEZRwoDhpaczWJlb6YqN3F0UQ27tkPI4Kl-JXZEZOYYT0hzLx3EgUkU2a0TSg5pKDDPrq56xvkYUSFoGdSNXlv7rAIE37I55zpAZftxDczdbyscxKhxJ6temdDB9yj-GVbPU8t30fc_jYDlynop5ziEZ6MsnMTWieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PMvNphVOj1EmQpg7wKScKaBRQvyUEEdjIT2rekvIL-SOwczY6bmbp8oPvaGxWOZ-qYkba6pFKe_X37oGdDxVf5desccZgNPbXlusB2EC8VdPj52qM7pZqCTeeNa2qQSnLdomiC2uxs39QaZHX_Gyfc9k41nTLQZu37MFTQLNHilozLvhTO2lPD7GUjsOHA4NFIVwuEIwvfT7iFaSsEg6f1TiamsfoHB-N2IuP2a-X8lsgPSgOQC97hmPzi3uh_iHlU7UPRIj8eSu9wwD0ICvTKvJ1UChBBa_o1O29bZaZycSVphb1QWox_a6p_h9hmkW_6e2aKUAoaW2UQstOuhq2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JW38f1KPkGBLqmNfOVxg3r0kB8hXsMQ_nnsJpyhqOAvj0FNn7Vv8HGfxzDavQiBS0i6g6_kKY5y5XaecP6KeD_1TrXpE_f2QcW49Q4y5DMZszVqg4qhysEcD-v9G0UqMv1EcPeH8gO_ctBigKr6NQCiTbYakUizOlaG-i_iRleMSoSK1-okFV1OUl42PqXWuCFOBBzerNdVM9bt_y9aHN1hpkNZpx911oWLhIMUv4smsGqwPZ7Gs0hirSsW_dojQKAmhwuoUAEOMifqV3nV759VRL16GIDTdIzfqwe91sxdzLv_bxl7UQdS773rGxHqytgQZhYwu-r5x9WhzJxNxOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tMlWgMOQFSjT5JNWjPpLTglx3ePZq3g_ZVLBgMTlxES1bfCzoua8wFuHBHQtkddfgxn0f5ETukLed0HE4glf6vphaZlbOrQZlQU0Q6EkgItFwEl_60BDnMsLRhnnpsp8VLw-slNu1qUmCIrMBWuaW0_OFiH0WasJGOuwHcLG6EPz7AOfuNGu9FrJC2N_Qmrt5t4nXw8dsjmq4WWS1Fww4S34kEVZCnpl44DEMR46t9lw9XPZxhxx_YjgKZMfdlSbAijCMdqNE_shVGY_bB5iS4NshoAbS2KlGJelqljd1IKixzrqqh0jlIfzVTmdJlpXgdqStbBBYx07ow9Nelbe_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
🚨
توپ رسمی فینال جام جهانی با نام آدیداس تریوندا (adidas Trionda) که قرار است در دیدار نهایی ۱۹ جولای مورد استفاده قرار بگیرد، به‌صورت رسمی رونمایی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/98584" target="_blank">📅 18:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98583">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
‼️
🇺🇸
#فووووووری ترامپ:
😂
با اینفانتینو، رئیس فیفا، در مورد کارت قرمز بازیکن کشورم صحبت کردم. این غیرمنصفانه است که فدراسیون بین‌المللی فوتبال یکی از بهترین بازیکنان ایالات متحده را از مسابقات محروم کند و خوشحالم که دستور من را به خوبی اجرا کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98583" target="_blank">📅 18:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98582">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00267e7cbb.mp4?token=DBT6dW23owmKRmBPDhfCTpN3OXr2h4YDOG_8oUdbCuLhebI_J9a9BEygv74Jli2CFRxNHyknNAbIbh-NiVVLMrLFQQxb0mV6YN50xh7JPzaQ9AY01ztWohI7KBbHKRdk2w0BsCo7nFVLTT2GeEZ4CS99TBZygc9vq9fTPtK30S8H0sVLOr0IjIIM5fMx0l6A-wDw80nfB5xCy3m_hIDHtkbIIgcnnAURTHBOqx6I8Ba7V9luijAqX5F0jzSgOi4iRcjjVl-3GJHpkuIC2zjRJitaZSKc3Td_Nf_dtFyx03oylTVXvW0uQEz8NNjiGf0ava890IvOCpn7j9AEIgsqWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00267e7cbb.mp4?token=DBT6dW23owmKRmBPDhfCTpN3OXr2h4YDOG_8oUdbCuLhebI_J9a9BEygv74Jli2CFRxNHyknNAbIbh-NiVVLMrLFQQxb0mV6YN50xh7JPzaQ9AY01ztWohI7KBbHKRdk2w0BsCo7nFVLTT2GeEZ4CS99TBZygc9vq9fTPtK30S8H0sVLOr0IjIIM5fMx0l6A-wDw80nfB5xCy3m_hIDHtkbIIgcnnAURTHBOqx6I8Ba7V9luijAqX5F0jzSgOi4iRcjjVl-3GJHpkuIC2zjRJitaZSKc3Td_Nf_dtFyx03oylTVXvW0uQEz8NNjiGf0ava890IvOCpn7j9AEIgsqWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇳🇴
نیمار و همسرش بعد از حذف مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98582" target="_blank">📅 18:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98581">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3386b27428.mp4?token=K7aa2OkNiWYqAIo8uxZdVJgsN2j80yLaUjyQWZAdVs17XRduWHRuPp-zok6uW5flzI6GbyOv-SXh9bQPN2_dh71y0QH4jRpLbNXou7ZnakN0K55TkwNUg6ASvmt-Hb1cdTAcPhcJtbV1ip1knFJOeYBYlrcNJLMk2Eh0rlR_uwwiGpceriA2Q6EXCdgq-aLoo7dZBQQwV2A6q8-zZZbXd1BoI9ZJ8JeLTHLk6nYLqnVVXbU_dnPrlfoJPC5dhPJ_3ZA2wIm0kG7WB2PF5XsWABh-fgOGxiHZYdQB0J0jUkMplxS_jIeBu68z0mFVmJsFMpckalJY2ZF7Qb0RNti19Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3386b27428.mp4?token=K7aa2OkNiWYqAIo8uxZdVJgsN2j80yLaUjyQWZAdVs17XRduWHRuPp-zok6uW5flzI6GbyOv-SXh9bQPN2_dh71y0QH4jRpLbNXou7ZnakN0K55TkwNUg6ASvmt-Hb1cdTAcPhcJtbV1ip1knFJOeYBYlrcNJLMk2Eh0rlR_uwwiGpceriA2Q6EXCdgq-aLoo7dZBQQwV2A6q8-zZZbXd1BoI9ZJ8JeLTHLk6nYLqnVVXbU_dnPrlfoJPC5dhPJ_3ZA2wIm0kG7WB2PF5XsWABh-fgOGxiHZYdQB0J0jUkMplxS_jIeBu68z0mFVmJsFMpckalJY2ZF7Qb0RNti19Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
طبیعیه ‌مردم نروژ با این طبیعیت و کشور عجیب و غریب همیشه خوشحال باشن
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98581" target="_blank">📅 18:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98580">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏
🚨
🎙
🇺🇸
مائوریسیو پوچتینو سرمربی آمریکا درباره بخشش کارت قرمز بالوگون:
⚽️
-این تصمیم از سوی فدراسیون بین‌المللی فوتبال (فیفا) اتخاذ شده و بر اساس مدارک و سوابق قبلی است. و این تمام ماجراست. به نظر من، این تصمیم برای فوتبال بسیار خوب است و چیزی است که شایسته…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/98580" target="_blank">📅 17:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98579">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrVs49rC1vdaoioBbhgww6kJ8vb5zIXrGCnqSoDo6ukLS_SLW-6EV0jV9-j5sjHO1BPSfIyGOV5NhvxonW13_POcLYvGGVl4XvaBV5Q_P5S0TWDFSpAZUiPVC8pRe-09PMV0o2Ufp08EYPI3ha5EV9VoC9W_0tqreAxpud8Ux-_nNNqvX0hjDvHu4NsQRyV0Z37a3oOehLrZhiI_xokZ5Mhn31vSR5zZdqL50b4J5RkYjMyp3Xib1DJUb2mvBY-RXNW_h3zACRmKkt2q9MY2hnq0e56ssYtyYk_4mFyNPAERwisdVd42zm01T1vtLcraJ36KSy9ecstiqrbrSthMgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🎙
🇺🇸
مائوریسیو پوچتینو سرمربی آمریکا درباره بخشش کارت قرمز بالوگون:
⚽️
-این تصمیم از سوی فدراسیون بین‌المللی فوتبال (فیفا) اتخاذ شده و بر اساس مدارک و سوابق قبلی است. و این تمام ماجراست. به نظر من، این تصمیم برای فوتبال بسیار خوب است و چیزی است که شایسته جشن گرفتن است
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98579" target="_blank">📅 17:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98578">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvuu5-xdHwzpPD3kDTyBZy0FB4dZQsaJ4mICsPS2tR4xoqHHJpea7kGrhOD3ls_cJVeyML8Bt3ph-ptasVPyeFKB9U91r4ua-TL4cDRYmh33Li3npz_27wWftihEUbi2KcDGs8SUpsoE36628Vo_bPpS7zDmraHh-vPtS7t8CDFI6V7Wsj18iRhOFQnGA4aPWMbSXAntEzRV5Ag0eyQTfdKCytC9eDkFZ10-Adg-XBb1esmFeeGe3PtVjOl3vOX6j1kO9BdDbDBle-eW6g_Ut47T57zxQkpjgw6iA_0TgT54C5CvmdWHIE3rqb82C5H2-FDr18jWksw5oSRTUaUAQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇪🇸
🏆
ترکیب آخرین تقابل پرتغال و اسپانیا در جام‌جهانی که در سال ۲۰۱۸ برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98578" target="_blank">📅 17:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98577">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
صحنه مصدومیت دیشب هندرسون از این زاویه که احتمالا ادامه جام‌جهانی غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98577" target="_blank">📅 17:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98576">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef353a211f.mp4?token=JTlmb_2mG7wJjK18kQQNxEXOuWaid_7WY2bxdPOtP0FAIOuMP65b_zlj7C1SJ-XkIloH7y0COX1CWrwugI-BS1mbzsibHU_L68cYJBJXzOnjd5SHXYHCcOIB0M6ZVxSQKKOrPFzbiwafzN5S_TuJ6wheti_4j3UqhaL4FRa5mkbMdrbD1IVUXr65AFi-IWHXsYlWRcLZUkzRKvdehFduxcl0xJQmH0XN73G_BG8D1xa-ZbweKfSeK8fsj0aNpBQSg2vWwwaN_UfLJgWBv6JlAn31AM6cU-SHHSWIfRw2k9M47rLEieEcPuTNJMhWOg6xglrnGViP4wVnMG64DcwMpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef353a211f.mp4?token=JTlmb_2mG7wJjK18kQQNxEXOuWaid_7WY2bxdPOtP0FAIOuMP65b_zlj7C1SJ-XkIloH7y0COX1CWrwugI-BS1mbzsibHU_L68cYJBJXzOnjd5SHXYHCcOIB0M6ZVxSQKKOrPFzbiwafzN5S_TuJ6wheti_4j3UqhaL4FRa5mkbMdrbD1IVUXr65AFi-IWHXsYlWRcLZUkzRKvdehFduxcl0xJQmH0XN73G_BG8D1xa-ZbweKfSeK8fsj0aNpBQSg2vWwwaN_UfLJgWBv6JlAn31AM6cU-SHHSWIfRw2k9M47rLEieEcPuTNJMhWOg6xglrnGViP4wVnMG64DcwMpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
🇲🇽
آشوب‌خیابانی در مکزیک بعد حذف مقابل انگلیس؛ ظاهرا بیش از صد نفر دستگیر شدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98576" target="_blank">📅 17:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98575">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq8B5FmbtsRz-3Sspmplm6B4uye8ytV30Jx4dJ3Cz87k9ijZUcneBALXJdU1_wueK47Ek7eqlejfDjsqcPgIv7XnHnjpkKosUhON3V1Is53wo57z47lMLEa0R2hnhridwHceuk3-FQwWQ6bt1lyPDGZOJ4cgW31ssBiCSt-hF-r0AulJXOXZt9WnDRr1qfz5_uEe8h4I__1Q9uwsgigbPZt6hYdH2zAm-1SoLCGNvd-AEajRlFqToOY550bCZTG71li1jpT-ZZq8fDg28vTNRJhg5zgG7M3KQcbMQWAfaSFt8JuTi9_bgQMMcYLiz2-OLXzJsszk79JdEa7x6sPNlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان ابراهیموویچ درباره ارلینگ هالند:
- "من یک بازیکن کامل‌تر از او بودم. اگر هالند دو فرصت داشته باشد، دو گل می‌زند."
- "اما اگر من دو فرصت داشته باشم، سه گل می‌زنم."
- "هالند باید خیلی بیشتر تلاش کند تا به آن سطح استثنایی که من داشتم، برسد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98575" target="_blank">📅 17:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98574">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b9f4e618.mp4?token=REr9IKgt-O6Vl41-vCbumdz76FaQyhAbRKv3T_zL8ZzW4zzzfZwRtWmRHbshkgQo2I_WKJuleyM7nEh_2bv1VgL0Iq8czHsVP1z34ktSdNmhk8cYWryBCz4gmT67WTTHJ65jPaY7a7EoDnhgPO7g-toeXQElIhWD9V6DHAScbHzE16FnGq09Pq6BIXS5iy-pcob-0ia_SjCTT5DcloGeGW5wxEsr51nyedkuhLgAoz4AMN8aT7dKRoTx7kL9k6NBYa-DAEWTmEXlNZexCpVeD4dO_zbftjTP7iIfYVr5ssH5l9_Lx8jJsmNogmniyGCwLVxwhHgVRQ-bs50TXvYzcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b9f4e618.mp4?token=REr9IKgt-O6Vl41-vCbumdz76FaQyhAbRKv3T_zL8ZzW4zzzfZwRtWmRHbshkgQo2I_WKJuleyM7nEh_2bv1VgL0Iq8czHsVP1z34ktSdNmhk8cYWryBCz4gmT67WTTHJ65jPaY7a7EoDnhgPO7g-toeXQElIhWD9V6DHAScbHzE16FnGq09Pq6BIXS5iy-pcob-0ia_SjCTT5DcloGeGW5wxEsr51nyedkuhLgAoz4AMN8aT7dKRoTx7kL9k6NBYa-DAEWTmEXlNZexCpVeD4dO_zbftjTP7iIfYVr5ssH5l9_Lx8jJsmNogmniyGCwLVxwhHgVRQ-bs50TXvYzcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
تنها جامی که آنجلوتی از جام‌جهانی برد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98574" target="_blank">📅 17:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98573">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7e9c60132.mp4?token=WRCGJ7VYIjGoXrdfDsceKXFFTTXG0YY19MoYQNWMcK2NjJHLbV_sdCKIettilR12XYQawcWDjqRxKigRsPAqiCVyfXtGdjO2tMSSDcS7RmxIpkoTlREYGAxJNHojyVzXEbCFFHLRVQqFUO97M3JJn0AtXmheoKdRrM2ykfAPO_bZ-J0UgH3WHGiT0NDzn5b0K0SNBOnU-7s1e6QM99K9i0QMcwgxH0f_dMWqu_SbShPgLBcvddoDNz3ZLbTjWBsBhKcbpa_o-UunfZo5FKEa4TAaI3RmMvG0JWyd-aVL-p2iCMo179NHV0_rg8ojyk-clNcbBfeSvoZojC9GWgCJTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7e9c60132.mp4?token=WRCGJ7VYIjGoXrdfDsceKXFFTTXG0YY19MoYQNWMcK2NjJHLbV_sdCKIettilR12XYQawcWDjqRxKigRsPAqiCVyfXtGdjO2tMSSDcS7RmxIpkoTlREYGAxJNHojyVzXEbCFFHLRVQqFUO97M3JJn0AtXmheoKdRrM2ykfAPO_bZ-J0UgH3WHGiT0NDzn5b0K0SNBOnU-7s1e6QM99K9i0QMcwgxH0f_dMWqu_SbShPgLBcvddoDNz3ZLbTjWBsBhKcbpa_o-UunfZo5FKEa4TAaI3RmMvG0JWyd-aVL-p2iCMo179NHV0_rg8ojyk-clNcbBfeSvoZojC9GWgCJTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
🇲🇽
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تفاوت گزارشگر عربی و فارسی در بازی دیشب بین مکزیک و انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98573" target="_blank">📅 16:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98572">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029dc7290d.mp4?token=e4Q7nv0eKbQfuyks0vqLiIgFcL1pYJwajJD0l1BNUDzaf56WZwx9VugiZYaYtFLTgLL2K-gm1CM5WDzk-AJBO6iB3tTQzHO8ilNUH-rcxrFh0ij5fkT8lx6SnVW3zraCZ_f1HgvgjIqJ2Ln5ZVMvifqygWK6WNztaj9jS2GtONNeuqYoClb5EBhqeqnjwJIDhtCDl-tQngN7vHt4iGEgSgNeYFYBEIfccy23gBIyRLAkdLeHI-GRiOCe_BYkiRDlmw57NFaaLe2upeVt_WhrOPpqYxelaIepjZXPO_VOP871ordqILSfA73GcNJSzVoTsfaLKEDB6-OyIHX1BTfdLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029dc7290d.mp4?token=e4Q7nv0eKbQfuyks0vqLiIgFcL1pYJwajJD0l1BNUDzaf56WZwx9VugiZYaYtFLTgLL2K-gm1CM5WDzk-AJBO6iB3tTQzHO8ilNUH-rcxrFh0ij5fkT8lx6SnVW3zraCZ_f1HgvgjIqJ2Ln5ZVMvifqygWK6WNztaj9jS2GtONNeuqYoClb5EBhqeqnjwJIDhtCDl-tQngN7vHt4iGEgSgNeYFYBEIfccy23gBIyRLAkdLeHI-GRiOCe_BYkiRDlmw57NFaaLe2upeVt_WhrOPpqYxelaIepjZXPO_VOP871ordqILSfA73GcNJSzVoTsfaLKEDB6-OyIHX1BTfdLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇫🇷
زرنگی بازیکنان فرانسه در صحنه پنالتی جلو تیم اروگوئه با همکاری دمبله و امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98572" target="_blank">📅 16:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98569">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21007d5c7.mp4?token=EeL4d3W_pkgc94AesRJEs6rCka5DIM_OMZrp4jw6Xrk6HUTNsPbdwfHyurIOPf5ASm57T0pGdGa98TCH8A3aYxqGroeSsTSjIms0M7jJ5DwJ_coeyGidBwtxdUCIuRrHqV0zs4J7wmP5VG0uUgQsih8x_qVB_4T2XkOH_gFMU6kmyZxws1RsLrJma-hJ1X2iB7cGJaFq8rvdHQEleYpDqz3QmJvbdZQ4wpUPfDUW5OZEWkOTSgTS9XNgpQbtwsiu4Ae2ypcxXz7e5oYgzI_ZjSKAGget4sFfoGIzhTIOJ0kyjAslK2FFbSd-TcnC5dv4-necnXQICxahWIA8J2XHcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21007d5c7.mp4?token=EeL4d3W_pkgc94AesRJEs6rCka5DIM_OMZrp4jw6Xrk6HUTNsPbdwfHyurIOPf5ASm57T0pGdGa98TCH8A3aYxqGroeSsTSjIms0M7jJ5DwJ_coeyGidBwtxdUCIuRrHqV0zs4J7wmP5VG0uUgQsih8x_qVB_4T2XkOH_gFMU6kmyZxws1RsLrJma-hJ1X2iB7cGJaFq8rvdHQEleYpDqz3QmJvbdZQ4wpUPfDUW5OZEWkOTSgTS9XNgpQbtwsiu4Ae2ypcxXz7e5oYgzI_ZjSKAGget4sFfoGIzhTIOJ0kyjAslK2FFbSd-TcnC5dv4-necnXQICxahWIA8J2XHcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇨🇴
تو پایتخت کلمبیا بعد جشن صعود به مرحله بعدی یه خانمی این‌شکلی سگ مست میاد وسط خیابون بالا تنه رو‌ لخت میکنه و تو حالت مستی با سر میره کف آسفالت
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/98569" target="_blank">📅 16:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98568">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0p9hEFhH0NDpQEG02yjdnW0d7ekIBu5Er4fllFQ9xBaYjNOV3oAMF81m7f274QIeuiFCWU-XNcvuXRSVdO8P20sTZ3mDwuhdsrDZRRAmZI8YDhajKEMnEDRwYwY4xyggSWQhQpCdTATJaJfjXFFyOmBFPHOHzxVnRIucMAjsTshAEuQD_hCG-F5bBFQKomHO8s3DmwTd3zfMbXDJpDTmrlF2jc1Gi_d0KwgEx-90psFP7hJGgEmJqxsz4guUNtEVOczxkhhf9V1JrXG0rDe2Zdtn7wC9vMygfhnCr5RJtfJ_9PfBCDLyBT0dRFPfsiculRGmHXmcsZqVvLcUiDTng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیلیپه لوئیس رسما به عنوان سرمربی موناکو انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98568" target="_blank">📅 15:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98567">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae451d7e1.mp4?token=T5m5P5gfPTDnJ_9zzKJRvNlT3wyD1xDksdC57sMJfOGyJWfC5hZujPtfvM7Ook83-faapEiFNbR-_DcBWTmwITGPUlUn75xQkeRhmYOaUCqgewh6XxGIV1UbYCwkOX9tzR3ykOPEVWdPZwKpecOsMUrsbmIiFlYpN2PYJJS0AJxSt1lPaPh00698rS512RC10pYxwaAmTsg71Zj1G7TvEbWtNnQzNhACCm7T4WYwuTrcNvTBp1hUeVZmPJwsHFLCo158q2aDoYzu9AuLbkYTO0P4Pfgml24dK7vhpLilKdtta8QjPeTR38MyB7C6ddTyKjkOTR0CmC7CC3ee37C-yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae451d7e1.mp4?token=T5m5P5gfPTDnJ_9zzKJRvNlT3wyD1xDksdC57sMJfOGyJWfC5hZujPtfvM7Ook83-faapEiFNbR-_DcBWTmwITGPUlUn75xQkeRhmYOaUCqgewh6XxGIV1UbYCwkOX9tzR3ykOPEVWdPZwKpecOsMUrsbmIiFlYpN2PYJJS0AJxSt1lPaPh00698rS512RC10pYxwaAmTsg71Zj1G7TvEbWtNnQzNhACCm7T4WYwuTrcNvTBp1hUeVZmPJwsHFLCo158q2aDoYzu9AuLbkYTO0P4Pfgml24dK7vhpLilKdtta8QjPeTR38MyB7C6ddTyKjkOTR0CmC7CC3ee37C-yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
ناراحتی برزیلی‌ها بعد شکست دیشب
😂
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98567" target="_blank">📅 15:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98566">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rz_8O85IVsxll_7kjJkoR0dkTNR905VQZqwMuts0Brr1S_EswPdhi7rrU7ydp0IChN8NjbNLi9IEAwSawzXIW-mFmg-zkhvS-PwkugNu0DqM3F9BAyC8coHDDlX8uxOns-Z-p2HFk6l7TNPUqYmtXRjbI1Pumk5UdR2N3LlK-tVsRPTYQ36_gAane9zzaAKKYWdgbj-hfrc4nogY7UHZls4U1wWwxs6gw59M9Bs6CBZLlradm8OxiC47BvcJO2TM8r5Sm6OKd_NNiSI5bgLVn3sgGJefZCQ1MmmzXVABG80B0J728fieAGe0bwst634vvBYrRFqaOzYVF5_r_94CZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فابریزیو رومانو:
کانگ این لی از پاریس سن ژرمن به اتلتیکو مادرید پیوست؛
HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98566" target="_blank">📅 15:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98565">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/033eeb4eb3.mp4?token=YQ8gdFWT_LtNUrmFq-TcHB1qVHRCxRQkedks_P6c2hywJprdIgES4K8xwTgzz1sQ_oL2DRerhL7vMUNyfm6ipiAIY7D9kHiZ7OIckzKShz77fFXarR8IGsjy3rdLYV5wB1y9TJt_LKQ9HaXI9fyS9EFBe9gIrG8UJ6EN9c4i-MrBwLo2XPkCEf_ZcIkFqZOeIexkjswyAtX7T14rmhxcHisl_uW9brLFQoI0Rgz-iRGbaXcmB_ZY_K5tUpqrz48XMQPptzkFxcS4ibHum2GWAXu3BaReqg-0TPakd-qa38XhBWH7J6xNhrBs9GWB4jgej3PtmOnp1BW9PODZajuNfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/033eeb4eb3.mp4?token=YQ8gdFWT_LtNUrmFq-TcHB1qVHRCxRQkedks_P6c2hywJprdIgES4K8xwTgzz1sQ_oL2DRerhL7vMUNyfm6ipiAIY7D9kHiZ7OIckzKShz77fFXarR8IGsjy3rdLYV5wB1y9TJt_LKQ9HaXI9fyS9EFBe9gIrG8UJ6EN9c4i-MrBwLo2XPkCEf_ZcIkFqZOeIexkjswyAtX7T14rmhxcHisl_uW9brLFQoI0Rgz-iRGbaXcmB_ZY_K5tUpqrz48XMQPptzkFxcS4ibHum2GWAXu3BaReqg-0TPakd-qa38XhBWH7J6xNhrBs9GWB4jgej3PtmOnp1BW9PODZajuNfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇧🇷
دلیل انتخاب گیمارش بجای وینیسیوس برای زدن پنالتی از زبان کارلو آنچلوتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/98565" target="_blank">📅 15:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98563">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0HKjNZrxuKWvabF_i9OBfQXw7qeibYxfgh7xzyOZamKEaEcmNmRs-mr20o-4QgQ95wBLv3VInT-HgNKm9JquwxLJHuPriloNMHHhdxPpd28HIZGQ_wHDrOhVPyjYbvVBYdY1EZfoWxVKwPhCvTDuMMVhpdaNSf4c8WT-Yp17YB6OXZ2x41db7-_glCjmC53E_7Z7b4WyyahIsJw4eZoYfxqTzF0aCVOZbzYIL-y7WxSo17D1JgRyFKAMfv6IfKpO9RUeFFxRqyxxOM17hGsQeaz-xeGLv6z8HoxtVJoYvPYXk280RwLpICLhVjhGanw1i6Ictd0IyCx7Wzl6_a38g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KLbOEaSiI2iBIR95B6w8fQfK-KSROkL2cOLlYscaMwkglkaqr-tOxKAZ0ie9BVgZN8L3ya3jqXjEUfg45HMA-BsVRJFWtEFP5JzPFxqjX1mx1WrCCcGZDP869G6hFQxZhpFUR_qrzNeulwkMbJ5yIlRNtT9Og_s-t7GAmtzkRc-PDlOyW-xR30n0MTHrl1UJanpsBdTCW3qYE9sKgqfLrqTk5Z9S8LM_JslbiAHp074czmstuxhHXjJZoeXKd9BZfMBUY8u2if_MC4yi1r0akBFQqy__WDurW9yDOe58wNen9ddZoSb4l84Tq78UvAqNO84hBPrQLsBSoctA2xXALw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
لوگو ناپولی برای فصل بعد به مناسبت 100 سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98563" target="_blank">📅 15:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98562">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/98562" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98562" target="_blank">📅 15:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98561">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98561" target="_blank">📅 15:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98560">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213c8e29be.mp4?token=K1EvPmBoBxnw6eq7bhCLmGPwxY7TXCXUc4MFOlqIlb9Vv-bmT-r5byiUlqbLyy9xOr7pYp3mckLzG-Flx2ALkomdQm13ukB17iKMcz72qn6hVsz8p8ZJsHjZph7XHsX2lAA-Lj2nALJDZ4GuEk4RALRJi8-Ht9bkdlAHXmhSCEqhurqgJgRogZRtXJ-x7-ZCsgJvJCT53Cje3Ql3Odt7lCpdSQ29_nF38KUHGGw_uDewlnGLQU7TkSTYSgeQLuZYdN4RttO2osaTe2fzuiuuIPloXvfb-KTUUuS3kMIVysstT9aTwPmcl0gKX5fhWb043u6qiQHChDLl0aEZuIOH3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213c8e29be.mp4?token=K1EvPmBoBxnw6eq7bhCLmGPwxY7TXCXUc4MFOlqIlb9Vv-bmT-r5byiUlqbLyy9xOr7pYp3mckLzG-Flx2ALkomdQm13ukB17iKMcz72qn6hVsz8p8ZJsHjZph7XHsX2lAA-Lj2nALJDZ4GuEk4RALRJi8-Ht9bkdlAHXmhSCEqhurqgJgRogZRtXJ-x7-ZCsgJvJCT53Cje3Ql3Odt7lCpdSQ29_nF38KUHGGw_uDewlnGLQU7TkSTYSgeQLuZYdN4RttO2osaTe2fzuiuuIPloXvfb-KTUUuS3kMIVysstT9aTwPmcl0gKX5fhWb043u6qiQHChDLl0aEZuIOH3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇪🇸
کثافت‌کاری رودری تو تمرین اسپانیا که یامال حالش بهم خورد نزدیک بود کونش بذاره
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/98560" target="_blank">📅 14:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98559">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6958da4a5.mp4?token=uToxp0jJSZL6NmRSrLcQ2_cXm6BDJmrCTPcoVD9zX61TwAyegQeXPyZ6MulSgC5czxkVjlXLJumPPIOUM-rYfTvcEWK_QhPbzCf7o7eIQYycnJzvhm1QcYsFqWHg9_fXKG0U_Q3TZuwIpx1Dm9my6yeFxhlcdya1g-CKT4Mg7eq_cwBzM5n-1JT_wTh0bh8E5ZIOu7fBt8LIP2g-1ak50dnAosaplU8v9uclC2qM-3_MCjb3dNqxTfPPWCqWI81AcxRT8dV8rVf-pkbgBdmqS3yxan4Xe-9DmgjbVzu0-wykce2uTP8hkMOMqWb5LTNvheIETqeAWqblUq2wkxHleQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6958da4a5.mp4?token=uToxp0jJSZL6NmRSrLcQ2_cXm6BDJmrCTPcoVD9zX61TwAyegQeXPyZ6MulSgC5czxkVjlXLJumPPIOUM-rYfTvcEWK_QhPbzCf7o7eIQYycnJzvhm1QcYsFqWHg9_fXKG0U_Q3TZuwIpx1Dm9my6yeFxhlcdya1g-CKT4Mg7eq_cwBzM5n-1JT_wTh0bh8E5ZIOu7fBt8LIP2g-1ak50dnAosaplU8v9uclC2qM-3_MCjb3dNqxTfPPWCqWI81AcxRT8dV8rVf-pkbgBdmqS3yxan4Xe-9DmgjbVzu0-wykce2uTP8hkMOMqWb5LTNvheIETqeAWqblUq2wkxHleQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇦🇷
ابتدا، او به عنوان داوطلب وارد زمین بازی شد تا پرچم آرژانتین را برافراشته کند. چند دقیقه بعد، در حین پخش سرود ملی، دوربین‌ها او را در حال خواندن هر بخش از سرود با احساسی که همه را تحت تاثیر قرار داد، نشان داد. و در پایان، او مانند یک هوادار دیگر، تیم ملی را تشویق و دلگرم کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/98559" target="_blank">📅 14:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98558">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AF-15z69J9qaS05MWiFZeB71rxxgb5voB1ULqA8zfEKlay0OoYviZrbCzaJyZBjtqOHH6wny90VjR25JkZpMq6WT2q4HADfWX7cNd7DUp9SOuk5bqNMYOpM57kLIrm9ywMSHRnC2dUc6rDL2sGklMeMXVWhxj4TxGA3-HIJmj625T5j8QAj6X7ea6__a95NfHPSb9TKLyjgTfr65vFTYniBxu82kErTWnwSPc1kFC7t7i_Xfeeikz1z7EgQEetracEvI7NzXc_cVqurqHTl3B0cFOpz8xgBYFrCFnHB6hF2VBG_Kbm20SV46wm7pkgWI4MHYD3NRuFBIqZhMMmz2Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
فلوریان پلتنبرگ: آرنه‌اسلوت گزینه جدی سرمربیگری تیم‌ملی هلند است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98558" target="_blank">📅 14:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98557">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/457acbc22b.mp4?token=LcLuLXv1AmyHtkM_wdRzlYJQJTze8BFIXFwWraAkRXv8Qy7bzOiuaUtAOMbjptsBev4T2HF-ATDPFEEb9YZiwZDhViye3KCQESm9Fr2mvTaRf5P-35CuEb-BDtXf1MKmgb_XZ_FgvokvyXxRKmxR5R9pqKdqmkl8v546mPw6h_i1AnCJX2sdbwj-yHee8TohLHqQsP7kKr8gr9qqnBUJfb6eB9hd71a_RpSvP3FHjpz7dhQ1n30O09gKPwPgjFMTs8QuGiU6XmVNM5Y6Q-n0vD_H2EHwGqL5NujiMg0zxv4xfDXT6hc_WpHK_5DJsDZbpPZEoio95dKZ2sZ11RbG0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/457acbc22b.mp4?token=LcLuLXv1AmyHtkM_wdRzlYJQJTze8BFIXFwWraAkRXv8Qy7bzOiuaUtAOMbjptsBev4T2HF-ATDPFEEb9YZiwZDhViye3KCQESm9Fr2mvTaRf5P-35CuEb-BDtXf1MKmgb_XZ_FgvokvyXxRKmxR5R9pqKdqmkl8v546mPw6h_i1AnCJX2sdbwj-yHee8TohLHqQsP7kKr8gr9qqnBUJfb6eB9hd71a_RpSvP3FHjpz7dhQ1n30O09gKPwPgjFMTs8QuGiU6XmVNM5Y6Q-n0vD_H2EHwGqL5NujiMg0zxv4xfDXT6hc_WpHK_5DJsDZbpPZEoio95dKZ2sZ11RbG0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
فیفا تصمیم دارد تیم‌ملی پاراگوئه بدلیل نقض بازی جوانمردانه در بازی با فرانسه، جریمه مالی سنگینی کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98557" target="_blank">📅 14:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98556">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f70b02a0d6.mp4?token=TAoyjlQ2zGORwW28M_1i_oQQ8fAyJNUdGbqpkyMDSoT3f97wIdqxR3gQcF7GKlPhPL-ftypIh3iBrpScPqGrzs4SU0bSZRWiZKI23IObzULLOdsUvwMxEnQjIHRUKOXEpTfTpUxevsSo35Tc-zzVtMlIPxIC5Z_1G1gyXZqcfF0elyz5LOMloLUfM-5-CCgfdmsP4GHIN0E2pyngqS5odZA3WDe8VeUvM3SpUPtS2WD_0a3RodeU0VhuIBkzydu2A493NhF78ibUO4E7quvIx9-ajuHe3BcRjshdLQlub1EqS-nRjvngyDNTe92Rqc0OcNSt1HTA1Xj5SylVHBWxAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f70b02a0d6.mp4?token=TAoyjlQ2zGORwW28M_1i_oQQ8fAyJNUdGbqpkyMDSoT3f97wIdqxR3gQcF7GKlPhPL-ftypIh3iBrpScPqGrzs4SU0bSZRWiZKI23IObzULLOdsUvwMxEnQjIHRUKOXEpTfTpUxevsSo35Tc-zzVtMlIPxIC5Z_1G1gyXZqcfF0elyz5LOMloLUfM-5-CCgfdmsP4GHIN0E2pyngqS5odZA3WDe8VeUvM3SpUPtS2WD_0a3RodeU0VhuIBkzydu2A493NhF78ibUO4E7quvIx9-ajuHe3BcRjshdLQlub1EqS-nRjvngyDNTe92Rqc0OcNSt1HTA1Xj5SylVHBWxAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثرات دیدن فوتبال با گزارش عربی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/98556" target="_blank">📅 14:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98555">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GC4VaOi0NSZdUaeFDr_drrf_81NGSHx3t52ZAxXn1R-gEf9JUNCVVeWoctlrevFp91_5xfwZIZtNaOEQN0hI1a8CWabQQvYFdpvhg8ht0VwAxiCeozt8WfBp5L3s1ZBXRbLC6vEBhYxwY8mUU5jVq_YpHSnHoI-UVcwabxI3GSm4YbnTZnd-Vi14GnwZ2zkAl2gy3n4ByU7VbRV4Z6EXnqvFzqa-tC4UvzgKdr0INKBDxTQOxdsBAatBcp3DykMBTbp0a1g0vnQTwLHC89M-vBODwCAUI5LZbGNZtpsUoAtTmVGEQFP-kd_YskvFh7pJgTgoRvKTmeq4bCVuI9jFtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس‌توخل درباره قضاوت علیرضا فغانی: فکر می‌کنم قضاوت داور بسیار ضعیف بود و همه سوت‌هایی که زد علیه انگلیس بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98555" target="_blank">📅 13:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98554">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3428ac45ff.mp4?token=JlSls3PSKc8dYodfBtmKVic_ZpsQZzDtXyKM4VtP82xAT2yt39hsU7W0L1atYXFWnYGLatblxk0BtG6YfanhyEXEoBOsKMv_YHZfsnNlvd-nGBbnD_opEzBiMH-sXB46dOjOh2T-7mAvMoCEi6ECPjieICo_I_LcOVdwPpbeeThFupy4Dt0SbHODdE4TJGiTcBEc6ZTo3JyhaokuZLyv9rkDm-BZ-nJfb7bKp3xYxP1GfFJ9RPrfvhJVIPqi5lp3I6n_cwMCa7UMn4NwBD5svCfx5MaWT1v0J4MQIG_1ALIMnBe6V9Oy-cqN42xwSO64KNnMuhJkllrLmSc-ys5jCXkdtFSUweXnakmHdkiVTgT8AyrlebOA5ayGLUp41zxIO6bekYml_9hOhKPsEXOua_qFN6M_b0pkvsv8i00k5aSHQyhdGfyROvqy6Hu2ZMc8bc5Hy94SeIsmnj_NUJbKCac2G4iKJUW2MFYsWnngBOyiTN8Ij22fujmMYMLJ3Na0PfShQwwf3ZPWrJukgLc1d6nYVpEgg8Pz2v4daiIfa50Rlb4dR81fXCQMmGqVOcqxfIffHvFRw9QjTIOfcvxME90rvmGoCp-sOqpOskQX9pDJpSEQTsCiqGZ7RoOz1I0G2HyFU7miLkiqa8Jw25PDFZC0Z6mg2zeO43PGJ1Aq20U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3428ac45ff.mp4?token=JlSls3PSKc8dYodfBtmKVic_ZpsQZzDtXyKM4VtP82xAT2yt39hsU7W0L1atYXFWnYGLatblxk0BtG6YfanhyEXEoBOsKMv_YHZfsnNlvd-nGBbnD_opEzBiMH-sXB46dOjOh2T-7mAvMoCEi6ECPjieICo_I_LcOVdwPpbeeThFupy4Dt0SbHODdE4TJGiTcBEc6ZTo3JyhaokuZLyv9rkDm-BZ-nJfb7bKp3xYxP1GfFJ9RPrfvhJVIPqi5lp3I6n_cwMCa7UMn4NwBD5svCfx5MaWT1v0J4MQIG_1ALIMnBe6V9Oy-cqN42xwSO64KNnMuhJkllrLmSc-ys5jCXkdtFSUweXnakmHdkiVTgT8AyrlebOA5ayGLUp41zxIO6bekYml_9hOhKPsEXOua_qFN6M_b0pkvsv8i00k5aSHQyhdGfyROvqy6Hu2ZMc8bc5Hy94SeIsmnj_NUJbKCac2G4iKJUW2MFYsWnngBOyiTN8Ij22fujmMYMLJ3Na0PfShQwwf3ZPWrJukgLc1d6nYVpEgg8Pz2v4daiIfa50Rlb4dR81fXCQMmGqVOcqxfIffHvFRw9QjTIOfcvxME90rvmGoCp-sOqpOskQX9pDJpSEQTsCiqGZ7RoOz1I0G2HyFU7miLkiqa8Jw25PDFZC0Z6mg2zeO43PGJ1Aq20U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
گوستاوو آلفارو سرمربی تیم‌ملی پاراگوئه: با انجام بازی خشن جلو فرانسه، میخواستم یک انقلاب را در مردم‌ پاراگوئه امتحان کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/98554" target="_blank">📅 13:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98553">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvi_gAWx9OQNKn0Qkn2do7t9vaA8ahudUrjZ_ATtHAV8r6mKRFMA1YXzhbD6D5nK5dk5yPC1svwD9iO7BwXIy6ZZjOvlsJG-L9_4wOc42CW6rkhSVk98F1ChDjagjJf57zlRwiZcTeoSpCARXl6Nr9oGBkXh3-0_nuec2joiSrHyHiZFJHIGWZ0MhQe_A1UT4IGowHDxCC4u-J9XuDtPBm9yl5xO7nY_9YPkagkFvcUfGn-WlUxsJVAyylxOXvxOTKUAUFNgUBOuAT44uFvP94jqtvlbUEt-bp9tf_wc0RDjookoF3Put90CeV6izKv_t8KZu_gCKND41l4VAPT6Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تاتنهام از جذب ساندرو تونالی از نیوکاسل به مبلغ 100 میلیون پوند با بند تمدید قرارداد تا سال 2032 خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/98553" target="_blank">📅 13:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98552">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🔴
⚪️
#اختصاصی_فوتبال‌180 #فوری؛ حداقل دو بازیکن گل‌گهر سیرجان در فصل‌گذشته بزودی با پرسپولیس قرارداد امضا خواهند کرد. یکی از این بازیکنان مهدی تیکدری است که قرار است جانشین دنیل گرا شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/98552" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98551">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ac9255a0.mp4?token=QlMNNNvz4Xe9iaMtmKZT_t6k4TJ9ga0o57Es01pIkESe4-DMZ_MA_dhXPM2cRpx_RQL3oqYZvrmgPmUIDpNri-Bp089aM4SArjJgzlP2Ea3EbyDRTyek4b4xOS5LXf9B8ssLDzYqxEblnIgP9ToMec5vbYK0WsW-XPGh0qsquCPgP67fMcU-pronBEUTzfjYPhotYuNT6TJScp8MXmK8nh9M5kVrV2GWPnOaa6g-5kKOnqoIRvD8k-HxEqbLpgQGRrKzIiqrghCchphGkNX_-2k53tnmp_jti1Px614J6OPeq11liMgPrlsRNEin3mSCc9XtzoNbsBqY5SONjkOw6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ac9255a0.mp4?token=QlMNNNvz4Xe9iaMtmKZT_t6k4TJ9ga0o57Es01pIkESe4-DMZ_MA_dhXPM2cRpx_RQL3oqYZvrmgPmUIDpNri-Bp089aM4SArjJgzlP2Ea3EbyDRTyek4b4xOS5LXf9B8ssLDzYqxEblnIgP9ToMec5vbYK0WsW-XPGh0qsquCPgP67fMcU-pronBEUTzfjYPhotYuNT6TJScp8MXmK8nh9M5kVrV2GWPnOaa6g-5kKOnqoIRvD8k-HxEqbLpgQGRrKzIiqrghCchphGkNX_-2k53tnmp_jti1Px614J6OPeq11liMgPrlsRNEin3mSCc9XtzoNbsBqY5SONjkOw6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
صحنه مصدومیت دیشب هندرسون از این زاویه که احتمالا ادامه جام‌جهانی غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/98551" target="_blank">📅 13:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98550">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fe4c5d7b.mp4?token=Mem-uPYxcS4f_yXt-yJwALVPXPGF4wjiw6ab-CufX4RENUJHzcEyp2_4evfCsLqhMkc3MN3TCKvOQOegXwOK-oTQNd25XYAM2__bFcNZ1x9jKLAth40WoS7L6m4UCV8WZ3o3ZOdWt0Oh2qGUvEy2J_ELoG6RIeA9z0YdhzZntz_QeF_bjKVbz0g3_-gk3C0sSwNAyGX3xWa3KaiIvAU9NXaa_KMpyyjJEk7h3FI62PwJqwvhguDAP718l-lkIxnM_6A4xhbZdLry93nhVnpdNiNNpjm9Y40prGBMHl-5fm1tO2ZvKRki11yNB0gMFqFbdjpUU0zhWAqkPmzfCTkPrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fe4c5d7b.mp4?token=Mem-uPYxcS4f_yXt-yJwALVPXPGF4wjiw6ab-CufX4RENUJHzcEyp2_4evfCsLqhMkc3MN3TCKvOQOegXwOK-oTQNd25XYAM2__bFcNZ1x9jKLAth40WoS7L6m4UCV8WZ3o3ZOdWt0Oh2qGUvEy2J_ELoG6RIeA9z0YdhzZntz_QeF_bjKVbz0g3_-gk3C0sSwNAyGX3xWa3KaiIvAU9NXaa_KMpyyjJEk7h3FI62PwJqwvhguDAP718l-lkIxnM_6A4xhbZdLry93nhVnpdNiNNpjm9Y40prGBMHl-5fm1tO2ZvKRki11yNB0gMFqFbdjpUU0zhWAqkPmzfCTkPrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نظر ابوطالب درباره حضور احتمالی ژاوی روی نیمکت ایران بجای امیر قلعه‌نویی
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/98550" target="_blank">📅 13:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98549">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4977d72c1.mp4?token=CqDT8ZxDU1ZMoA-3i9dE_4r_9aF2n-owTTQO-j9n6fzv9u_wsX-Hw6l4J8m4l7TXeCLrX3zSjWgwqtZDmhDp8PUphs01HzvgjD1WaNsJ0VbPViq6UZjYtepigWbhCYLdKFdnSta9jk3S4CNkJOKdTd6IFSaN-8JC0Olo2P5TYqbIflt7aW4kC51x1mZLdRxgcU_twlDd-1WTy-4goQQo8jecO75ShKbcckYnJz3zURU8QolfK5IdkIDPH-HN_R9A4e3lTsQeXPIKaXDL09KXAoVGVFTLm2n3MQJzsfmBw5xNGpubjguu50_5eDGO1HYkq52vK_x13mQFMsHRZfr69g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4977d72c1.mp4?token=CqDT8ZxDU1ZMoA-3i9dE_4r_9aF2n-owTTQO-j9n6fzv9u_wsX-Hw6l4J8m4l7TXeCLrX3zSjWgwqtZDmhDp8PUphs01HzvgjD1WaNsJ0VbPViq6UZjYtepigWbhCYLdKFdnSta9jk3S4CNkJOKdTd6IFSaN-8JC0Olo2P5TYqbIflt7aW4kC51x1mZLdRxgcU_twlDd-1WTy-4goQQo8jecO75ShKbcckYnJz3zURU8QolfK5IdkIDPH-HN_R9A4e3lTsQeXPIKaXDL09KXAoVGVFTLm2n3MQJzsfmBw5xNGpubjguu50_5eDGO1HYkq52vK_x13mQFMsHRZfr69g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇫🇷
🇲🇦
بازهم تقابل دیدنی فرانسه و مراکش در جام‌جهانی اینبار مرحله ¼نهایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/98549" target="_blank">📅 12:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98548">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDL1MPsYf8aL5yAiMVzFRbf-yDHVDiQOclylk7wlitaPo21kqIPRkhXlAxmE9y4w2Ob9Iv6SgfFA5esxVMsyOlW_YRodq-1qV57J_fxyXRpHb6k43BsVTdT6uDcPJtAXYwa9vp26FnGiW9nFuRSqwq0qGbtaVW4nV09hUGA2OHn4FGtxHhl9VKjr1fBWpWHboZmMeedGt6mC-fPGvcZAUPYRgSKCwZOIU2PR6MZvV5keN6A3ClIQZNq2uHfUbA01p0FcC7QNcQ2-yasj2QU10sAEzUd1xtMFiiGUwUWC3_uOipcw0VXnaaZDSRe1OEakyHW8Cis0qbUAQG-adNRU1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گلاسنر سرمربی فصل‌گذشته کریستال‌پالاس هدایت ناتینگهام فارست را برعهده گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/98548" target="_blank">📅 12:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98547">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0f247243d.mp4?token=YsNA3DujVjsdnaPpGohkD9wBxN6W-DDFdJOWMHI91SRSjrGx_VCou64mufnZKmpfUAIZZ2O85uKQuBZSX8MQmipUVHjU_bsmg4_U9OghZlno5mPElvNpu494L1xzCXYghqQJQtptU9Ur3H18jUZYLJ7xQ3PWlPWebZmbL5stvU0W1FKGRUo0JyeW_-cfwDJPpxmLRJKuw37K27vLwoLBdHlmT2ynqX13F3vWkKzOsN_iinNar1-QlmTnZcf_NYiTHoGgY_7uiyvMgojgP4eq8YwNQyWyQZiP72_obFP0WoSlfEqfFa7lW7MjA_-aw-IpeWI4rV0M4NfK4VXWNtLMiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0f247243d.mp4?token=YsNA3DujVjsdnaPpGohkD9wBxN6W-DDFdJOWMHI91SRSjrGx_VCou64mufnZKmpfUAIZZ2O85uKQuBZSX8MQmipUVHjU_bsmg4_U9OghZlno5mPElvNpu494L1xzCXYghqQJQtptU9Ur3H18jUZYLJ7xQ3PWlPWebZmbL5stvU0W1FKGRUo0JyeW_-cfwDJPpxmLRJKuw37K27vLwoLBdHlmT2ynqX13F3vWkKzOsN_iinNar1-QlmTnZcf_NYiTHoGgY_7uiyvMgojgP4eq8YwNQyWyQZiP72_obFP0WoSlfEqfFa7lW7MjA_-aw-IpeWI4rV0M4NfK4VXWNtLMiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇳🇴
شادی مردم نروژ پس از صعود به مرحله ¼ نهایی جام‌جهانی؛ آدم واقعا حسرت میخوره...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/98547" target="_blank">📅 12:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98546">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effa95670e.mp4?token=OeYAF4aNQveb7mgTZa7Cuyypzec29f-bKkuEI_gc7Wm2cgaVR3zAMvbU3TUh7WZ4a-HDvwGuV0tG3BjtGjJwLAR77EmpFOAIzrh3igEpNDLg-XoJMFGBCgSsB7mgzRpc4n5abNfK9BebDU1_NIoguWEF0YPmYtoRyK4U9XYZMnrdbKNW2fcI0wfZ9S1ZcqoE4gdYADgCojtZYgSrAV3YbPrSF1zRN3EXepJDq8FAzD-eavAszUDIvvdt6aexMCIHMzhN7lpf0BUzo86_JtdXaZEw4cfQrE-C1AKncRP_JXJJMILXqK9IrA-gJcCEZAOjIwvun5Lqss4IV1lfsFB6wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effa95670e.mp4?token=OeYAF4aNQveb7mgTZa7Cuyypzec29f-bKkuEI_gc7Wm2cgaVR3zAMvbU3TUh7WZ4a-HDvwGuV0tG3BjtGjJwLAR77EmpFOAIzrh3igEpNDLg-XoJMFGBCgSsB7mgzRpc4n5abNfK9BebDU1_NIoguWEF0YPmYtoRyK4U9XYZMnrdbKNW2fcI0wfZ9S1ZcqoE4gdYADgCojtZYgSrAV3YbPrSF1zRN3EXepJDq8FAzD-eavAszUDIvvdt6aexMCIHMzhN7lpf0BUzo86_JtdXaZEw4cfQrE-C1AKncRP_JXJJMILXqK9IrA-gJcCEZAOjIwvun5Lqss4IV1lfsFB6wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نروژ رقیب خودش در یک چهارم نهایی رو شناخت: انگلیس!
👀
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/98546" target="_blank">📅 12:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98545">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f623fc21.mp4?token=NY8Tg7CniAMM3FM6FMLY-YqfeJBgsPGCbk8CYWoS-kUoVe48Iu2VTEv5dDxl--9PJ9Owh2gKzk43pAOgCmxC4yKJPMuWvviW9_Qr05ph6R0JtCQ9mtRXPtM7K8AjhoulVyp8SmIbaEcs-VZiA9sotbxwXulsYkmChPMMN9cPm9y9pjVgQSEa7l4VAp2-R1iAmB7t7N9oKt0drqkm_3bgTrDYW3ra-lfDJmm9AWg07USMjEs_eFW7UliYcosPq7XVVSNLNc83gJ_wMOQKTObvR5XyO5nxKG46z8FQHnxtFlx5jZ89yyDlu38ix-5wuq0khHlTNDQHdnJvD5Ut3slTmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f623fc21.mp4?token=NY8Tg7CniAMM3FM6FMLY-YqfeJBgsPGCbk8CYWoS-kUoVe48Iu2VTEv5dDxl--9PJ9Owh2gKzk43pAOgCmxC4yKJPMuWvviW9_Qr05ph6R0JtCQ9mtRXPtM7K8AjhoulVyp8SmIbaEcs-VZiA9sotbxwXulsYkmChPMMN9cPm9y9pjVgQSEa7l4VAp2-R1iAmB7t7N9oKt0drqkm_3bgTrDYW3ra-lfDJmm9AWg07USMjEs_eFW7UliYcosPq7XVVSNLNc83gJ_wMOQKTObvR5XyO5nxKG46z8FQHnxtFlx5jZ89yyDlu38ix-5wuq0khHlTNDQHdnJvD5Ut3slTmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇧🇷
خلاصه که هیچ‌مهاجمی نمیتونه مثل رونالدو اورجینال باشه و گلر رو دریبل بزنه. اندریک و بقیه تازه انگشت کوچیکه اسطوره برزیل هم نمیشن...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/98545" target="_blank">📅 11:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98544">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaB_lHVP4S3k6O2bEkvlms9Ebc8u0X70vKO5iHKgmTrScV8QLrSZV_T8MsbJEJ18Sz4pavJa2CtiHrrkYQQvW1TccKLPY3Q71WcJzWzORlDK9HBTz11n3N1iwjCsi3Ar_O7OBj97rFzMcQjTjup7bIM4Rj6hwXLQogN28FxgAsJvY1Ca3X44ZB5AIjR7ms136o4VzE02T8PuLA8KEO0eyIgBJlEOJs0iWPf9IN_qvbiq262WCP0g_NkGtJemQWKWeLb2KIhOLY1o8eHxR8kHGzGiZY-nQmwcJ3YgeU1Lj_F2Xr-Oi4Ju75-lufq02yk4LX1qnigvbc0lRdqP9EVbPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇧🇪
بیانیه فدراسیون فوتبال بلژیک: لغو کارت قرمز بازیکن تیم‌ملی آمریکا در آستانه بازی امشب نمونه واضح از نقض آشکار بازی جوانمردانه و دخالت قدرت‌های سیاسی و نفوذ در فیفا است. شدیدا این تصمیم را محکوم کرده و پیگیری این مسئله را ادامه می‌دهیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/98544" target="_blank">📅 11:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98543">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f91878075.mp4?token=bHViyepDsFa9i_gkI9xKfCD0J-tV-IWF0q3a7FZn68Ni-VNnwGawpWv6ml0GqoJOf9w3d393ZIhOmAQJD-eh8yLba7ADDyyb8OktqEIHIkG52Q84mLEQ_9tSQmvqCS7fXC2FfTjcn-UcO9LqibDjXdBHu4AEenFfaQSbZ-WvOXKHtyw2-UN6Di2pngY5SnlLjw4aO4ozA27hyVZnNPmvAptJIxXt5UNiDxT2AyIRcpRiqNnEDP5PYDH7tDXs5GrvHeY0EugQsZCEAS87iIm3myFaLLSvw5O4blBzbDmrHwsnGHbJCT87DuVrvbt6xomG8p5YXwyoBGWoPiy_172tRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f91878075.mp4?token=bHViyepDsFa9i_gkI9xKfCD0J-tV-IWF0q3a7FZn68Ni-VNnwGawpWv6ml0GqoJOf9w3d393ZIhOmAQJD-eh8yLba7ADDyyb8OktqEIHIkG52Q84mLEQ_9tSQmvqCS7fXC2FfTjcn-UcO9LqibDjXdBHu4AEenFfaQSbZ-WvOXKHtyw2-UN6Di2pngY5SnlLjw4aO4ozA27hyVZnNPmvAptJIxXt5UNiDxT2AyIRcpRiqNnEDP5PYDH7tDXs5GrvHeY0EugQsZCEAS87iIm3myFaLLSvw5O4blBzbDmrHwsnGHbJCT87DuVrvbt6xomG8p5YXwyoBGWoPiy_172tRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🙂
خلاصه اتفاقات دو روز اخیر جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/98543" target="_blank">📅 11:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98542">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e3eeffa12.mp4?token=YduHTS7oN1tZ11_kf__K0tSq0O3rJEb3bhDUDB8r75WJki9IT3hsklmyJYCrhBD63q3NNif1s2-XdKbT7cjJWqw2in25ErWFq1-fcRc2alUSbqpSbVNV7TROJCTYnSf5BQTJKBmQYoJw3bPLBcUswW_RZVI-4kIX5lXLgwIa4LmH1a-rf35RFhpUFzKBLvWGYZWaPHK1tC37e9m2_4JtVXuXa6AVjcaTBK55OfIpb7dOstK6viUqHZcnFBPhU-xDVixcEEtrj7itHE58XKd4IraBMJSmr1dAMjpyb7YwSDOAf0kPrTQhvJKNxd7moMP2WnIKYQtedflbX1TfzGHdPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e3eeffa12.mp4?token=YduHTS7oN1tZ11_kf__K0tSq0O3rJEb3bhDUDB8r75WJki9IT3hsklmyJYCrhBD63q3NNif1s2-XdKbT7cjJWqw2in25ErWFq1-fcRc2alUSbqpSbVNV7TROJCTYnSf5BQTJKBmQYoJw3bPLBcUswW_RZVI-4kIX5lXLgwIa4LmH1a-rf35RFhpUFzKBLvWGYZWaPHK1tC37e9m2_4JtVXuXa6AVjcaTBK55OfIpb7dOstK6viUqHZcnFBPhU-xDVixcEEtrj7itHE58XKd4IraBMJSmr1dAMjpyb7YwSDOAf0kPrTQhvJKNxd7moMP2WnIKYQtedflbX1TfzGHdPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇺🇸
پشت صحنه‌ حماسه‌ای که دیشب اساتید فیفا در بخشش بازیکن آمریکا رقم زدن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/98542" target="_blank">📅 11:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98541">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86d99c29d9.mp4?token=pT5gx2pyUYe_cFDuqrpCKD5JN21n6igxdf0ZC7Cq69s50fx5DL_ehtNQzPDX-_R8l9A-wKPz_KLaWjTVkxxofSOKUibW1BfJT_VucTnfHnXiNax2zmqkkJtvmPr1IBTHCRJ-uPdGDUJvp37oZIdSpO_e7H8rdi3dGxIJc4x0xMz2ovq9mLlVy3c-hHTx_lffiHN-oXDOOL1VDW38eheUBgNbQx-3Wunaw08ZkathZc1SbeldEGfgVaUYne6MFJKI8AcV1Wlf4LncYDGI-B_DBRDJeS3wehTAWk3jsIyEuxzCfCho-IAjvWYfvLGZrvV4RMZNDvHZ10dBdRoArfulMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86d99c29d9.mp4?token=pT5gx2pyUYe_cFDuqrpCKD5JN21n6igxdf0ZC7Cq69s50fx5DL_ehtNQzPDX-_R8l9A-wKPz_KLaWjTVkxxofSOKUibW1BfJT_VucTnfHnXiNax2zmqkkJtvmPr1IBTHCRJ-uPdGDUJvp37oZIdSpO_e7H8rdi3dGxIJc4x0xMz2ovq9mLlVy3c-hHTx_lffiHN-oXDOOL1VDW38eheUBgNbQx-3Wunaw08ZkathZc1SbeldEGfgVaUYne6MFJKI8AcV1Wlf4LncYDGI-B_DBRDJeS3wehTAWk3jsIyEuxzCfCho-IAjvWYfvLGZrvV4RMZNDvHZ10dBdRoArfulMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇧🇷
توصیف‌های عادل‌فردوسی‌پور از نیمار...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/98541" target="_blank">📅 10:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98540">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f587817b79.mp4?token=k4EU10y6RUOWlkoIkzcroq513WHUtJW6nPenzOCEPgP1TvO-L4HllHY_GO6rXE0p8gHkQ-7qbhy0Rn9e25mcD1oaOFalnvOnjsV21hi5mtLkIl__Gd0PM5oLNLudiE8VwYDZQgGuKYuuw6kyXowADwXddYzOLMfDb-IuPFWOMKImDrZNd1m52AgMb01b_NgnacKoswH6FdkJXolQZtnnhTmD5ScNCUfmcHuzhtUIV95nxy_L0y_u5OPc0C4qoJHM7sMnErgN5wpuyE1j9xWWPpbmlD1lyzbWZKlFdhUIyRY8JbK_Gz5vbXmXeOfc9q3275S3ftGKwfWGDdo6avYpRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f587817b79.mp4?token=k4EU10y6RUOWlkoIkzcroq513WHUtJW6nPenzOCEPgP1TvO-L4HllHY_GO6rXE0p8gHkQ-7qbhy0Rn9e25mcD1oaOFalnvOnjsV21hi5mtLkIl__Gd0PM5oLNLudiE8VwYDZQgGuKYuuw6kyXowADwXddYzOLMfDb-IuPFWOMKImDrZNd1m52AgMb01b_NgnacKoswH6FdkJXolQZtnnhTmD5ScNCUfmcHuzhtUIV95nxy_L0y_u5OPc0C4qoJHM7sMnErgN5wpuyE1j9xWWPpbmlD1lyzbWZKlFdhUIyRY8JbK_Gz5vbXmXeOfc9q3275S3ftGKwfWGDdo6avYpRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇳🇴
خانواده سلطنتی نروژ دیشب بعد بازی با برزیل برای تقدیر از بازیکنان کشورشون وارد رختکن شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/98540" target="_blank">📅 10:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98539">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225328e9fd.mp4?token=rJRNqULw8G8YLhCQPnatWL5s6KIpjTvK-22ZMfECxTslekmlv-3ohEM8U98ko174A4syVwRzwz3lcML-odTbebLu8NKzbnVBFf-ljOy1YmsHxUWvSCtL9izSPjS0PrO3E-5BdtKbHqjI7nKaRBdtjZ6PvTmXXqN0hLap2yoFK1e6yfONXg9Z6RVrj7_x8HpqDWCya-VeRurt4f-5DpxzVeuNMZHGFUpurti9srz6OFWAhdKgpFbFHGmLdTmBUUNXy-0ntc3UCLu7yAzsBR77VsNRPBmuIl6EjT1rK7_ENaZQ7-xSw7B9b05Dx0_71N9lvGj6dGQ8Sa5i5kxUAz5Peg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225328e9fd.mp4?token=rJRNqULw8G8YLhCQPnatWL5s6KIpjTvK-22ZMfECxTslekmlv-3ohEM8U98ko174A4syVwRzwz3lcML-odTbebLu8NKzbnVBFf-ljOy1YmsHxUWvSCtL9izSPjS0PrO3E-5BdtKbHqjI7nKaRBdtjZ6PvTmXXqN0hLap2yoFK1e6yfONXg9Z6RVrj7_x8HpqDWCya-VeRurt4f-5DpxzVeuNMZHGFUpurti9srz6OFWAhdKgpFbFHGmLdTmBUUNXy-0ntc3UCLu7yAzsBR77VsNRPBmuIl6EjT1rK7_ENaZQ7-xSw7B9b05Dx0_71N9lvGj6dGQ8Sa5i5kxUAz5Peg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حذف برزیل از جام جهانی به دست نروژ.
🇳🇴
☠️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/98539" target="_blank">📅 10:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98538">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5bedcc290.mp4?token=k8JDhLLmKywlzH6ADxVcuVlQvAP1RhWczIJR8n5c4j_SnUx96_MczP2vnSCQbhUYPp5fmoi7fc0u1WWRyVNTyQOZqYR-YGb6KUoRLHYeM3biJdgWX6KLUexLgBXS0EXdAJOtscBW0RlC3T3L6tXUd5uooPhYpt8tsMhMurdh6kvsc8uSKFDI-LmdDQZhJxmtFMb0_Lo-0pHs7uItJhM9KneanpgGXNNamo0t44JFmUzvQwjCl-azhIoYTQZ0jcgZ-NzWbhvaKSTr9O-WFpPBAE50rWKzwXf-F7pAZ-B-FdlI69WjfHiXt3FW6LPCsSY3CU5sV19QvVzbBWBSjsSkBbSjAaGA9VwhTXztNKYSGlERYI4bz_hOXqPE_Y3SZE8INh_DCtCmhZSfGsglnRTaVa_tjeAeoZik-X_jtERTNstnc4SMq0_58y26nVi41V53llJ62DnUev0QceRc0ZB9RDup7hkYvJOfotGzlotYzHQ1-U_CTV15eD2BXwCe1PAVsLpE5A4Xb8PwOxXHhFJxim7COu4ZUT15JhetR5Me88BtPdKlPwf1bHnn9MOYJsX7ANeOwoaQNGfAIum4XW3lnDboH-L89jKWPBLgicZHvJS8ODRQjZ15vxpq5X5-uBDunxQNYl59T-2Elz2i_wTM7TJAdGjK0mBzldFAIbYavrs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5bedcc290.mp4?token=k8JDhLLmKywlzH6ADxVcuVlQvAP1RhWczIJR8n5c4j_SnUx96_MczP2vnSCQbhUYPp5fmoi7fc0u1WWRyVNTyQOZqYR-YGb6KUoRLHYeM3biJdgWX6KLUexLgBXS0EXdAJOtscBW0RlC3T3L6tXUd5uooPhYpt8tsMhMurdh6kvsc8uSKFDI-LmdDQZhJxmtFMb0_Lo-0pHs7uItJhM9KneanpgGXNNamo0t44JFmUzvQwjCl-azhIoYTQZ0jcgZ-NzWbhvaKSTr9O-WFpPBAE50rWKzwXf-F7pAZ-B-FdlI69WjfHiXt3FW6LPCsSY3CU5sV19QvVzbBWBSjsSkBbSjAaGA9VwhTXztNKYSGlERYI4bz_hOXqPE_Y3SZE8INh_DCtCmhZSfGsglnRTaVa_tjeAeoZik-X_jtERTNstnc4SMq0_58y26nVi41V53llJ62DnUev0QceRc0ZB9RDup7hkYvJOfotGzlotYzHQ1-U_CTV15eD2BXwCe1PAVsLpE5A4Xb8PwOxXHhFJxim7COu4ZUT15JhetR5Me88BtPdKlPwf1bHnn9MOYJsX7ANeOwoaQNGfAIum4XW3lnDboH-L89jKWPBLgicZHvJS8ODRQjZ15vxpq5X5-uBDunxQNYl59T-2Elz2i_wTM7TJAdGjK0mBzldFAIbYavrs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇧🇷
هوادار برزیلی بعد باخت از شدت عصبانیت هیچکی نتونست جلوشو بگیره و تلویزیون رو شکست
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/98538" target="_blank">📅 09:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98537">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe89e97eff.mp4?token=Mo1WSBVwBP-Zi4ICQVF2juK5jkh_Dy21qeSutWqHddGfuXF0805cndQZ7MdgosC26wC38pHxI0_JjJd9_O_M72Htohea7BNoeVs8zWSlyCD1jGnav737K9uCsc6nqd5CwyohJWM_tP82dzaweASQu2GC8tPqwZQJ-V4SbCozT41t9w-qHyDdLq33ATzE6VPMhE6NKlNRRUczffSQVXt0GWKXAm7GONmmxsAhSGHkJPhm0tIJrOnFQzPs7dWSfTL5x4LmGDak0babAsk-TpXxIwjwnay5rtYCDiRB7zcLnOXgGtN11_MQPTZOUru56xVjSIcoW5Ij3FDHWeAV39q0LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe89e97eff.mp4?token=Mo1WSBVwBP-Zi4ICQVF2juK5jkh_Dy21qeSutWqHddGfuXF0805cndQZ7MdgosC26wC38pHxI0_JjJd9_O_M72Htohea7BNoeVs8zWSlyCD1jGnav737K9uCsc6nqd5CwyohJWM_tP82dzaweASQu2GC8tPqwZQJ-V4SbCozT41t9w-qHyDdLq33ATzE6VPMhE6NKlNRRUczffSQVXt0GWKXAm7GONmmxsAhSGHkJPhm0tIJrOnFQzPs7dWSfTL5x4LmGDak0babAsk-TpXxIwjwnay5rtYCDiRB7zcLnOXgGtN11_MQPTZOUru56xVjSIcoW5Ij3FDHWeAV39q0LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
گریه‌های شدید این خانوم برزیلی بعد بازی دیشب و حذف از جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/98537" target="_blank">📅 09:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98536">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce65688fa.mp4?token=OBJE02V1ICCDCnd7WEnV28hJ6nWxyc9Sm0zQ6aEKLutJYwvy1n6cv_4AAr4XysCH9uCok6knn2mn1ERi0-9e-QHDC6D_DWvIo-bWEzkbluayAU8RZ0ojJp-4wiUAFweEvVFtJni2miYHNq_m0f3sGqnTl2dpCR4WOsoqBBnvO4mmgsqmmY9xjokQznEEd7rT4f-b50xPITkfwn3R7v4c4HHA1aDVpzUTN8uizG0X0_9c0RO7UmkBTO2jjd5N2DkRrMZiJx-Lco43Jzg-HuIfTmtMNmH6P76BNcSS5MRcEzDojbaxMGxif9m1bLKxcd-2LsrMdSGUKpZIK4nV16j6FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce65688fa.mp4?token=OBJE02V1ICCDCnd7WEnV28hJ6nWxyc9Sm0zQ6aEKLutJYwvy1n6cv_4AAr4XysCH9uCok6knn2mn1ERi0-9e-QHDC6D_DWvIo-bWEzkbluayAU8RZ0ojJp-4wiUAFweEvVFtJni2miYHNq_m0f3sGqnTl2dpCR4WOsoqBBnvO4mmgsqmmY9xjokQznEEd7rT4f-b50xPITkfwn3R7v4c4HHA1aDVpzUTN8uizG0X0_9c0RO7UmkBTO2jjd5N2DkRrMZiJx-Lco43Jzg-HuIfTmtMNmH6P76BNcSS5MRcEzDojbaxMGxif9m1bLKxcd-2LsrMdSGUKpZIK4nV16j6FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇳🇴
حسادت عادل فردوسی‌پور از وضعیت مردم کشور نروژ که در رفاه کامل هستند...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/98536" target="_blank">📅 09:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98535">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rg9QnyfXIFV5bGAweUaX5dPJzvUD-X55UUsb41qy3igjDQKzcoAsUIuyoByict0L4Rdg2TgIcUj9csR6RWlpiGabMnzscExnGJRhMaA7BhLDCDo6u0llsXlWgRud3A333AhVfg19ZTBcgf9yRo8YbXA1XBR4xI-t6ltF4sKC83O08FnQPeXRry8bmPB4LQoE_Rzfo1Ga3Bu_NKApkzpheBLILkNLudmozqDqPPYNZSJy3q2q9fFhXRz8m5pP-VM84faAkU9jp3xV_tksnDDrUUasl_1OqtJhi5LeeDZOdFNH3XfbUHkq4GiKK-dWpETke7lCl0oJ3OefxTFj1eoj9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون پخت و پز همیشگی
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/98535" target="_blank">📅 07:37 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
