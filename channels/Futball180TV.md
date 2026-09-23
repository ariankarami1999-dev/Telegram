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
<img src="https://cdn5.telesco.pe/file/ltCLOSapohYYquOOO_HoIOPwWLYhGDPIJkU9KVOJ_nUgbkvypsXTMXAVTcDBm_4eIBoPQ9xvEHtuXAeAfqDsy2399ELCkVOD1KfKa1ZnpV0BEj_DlMugJ-MNHKfiVFK6OqtFb5ppDge7h0QM3KT6s7HjopPZe_-AVHszvD5sOfqwxU7VglJmnoYZOwxmyvrH_uKW5n5K-YyJVpHuQUyUlzea-x-vdh9MA9LJCzAyzDqDJvzFm319tp6qSN5CiOtDffwlwm0356ILyjmvzNGvCBKBaWSQvvaQZ0NsXVOQwUkEv24_OVmsV3Saa6NY9GssSZyNzvQAP1ajPrBKq7ac5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 403K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-01 13:40:22</div>
<hr>

<div class="tg-post" id="msg-107119">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2053a9052c.mp4?token=QgiaEfwa4DMfPiPN00JsUCt69yVSnj37vqb-Dfy-66p-DPGx18zjNX_60WOJIGG3d_umohRXnCF6-kvFWjbwMRPD_YfXITLzuQ7Me1m7T84DLWt38bJcGLxgVJVjZzXsBC2xTY4dM2nQVhZCg8At2sfODzjqRMhTBM4PJCom17milpj7Zp96K-j9Q-YILZcy-Z0jaKjPSO3bZhBtSg3oOvCppY5IY03w2wxJho4OkFxgSpSIk46YfJU02ohVYPfX569R1G1R7jOssN6QMoRCOO9SYuByEhYs_Hz6NEi8eEV_uOGVqvwcWVV49ZA_y5w8dUPkzf8RSoK_hEER1E-ENg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2053a9052c.mp4?token=QgiaEfwa4DMfPiPN00JsUCt69yVSnj37vqb-Dfy-66p-DPGx18zjNX_60WOJIGG3d_umohRXnCF6-kvFWjbwMRPD_YfXITLzuQ7Me1m7T84DLWt38bJcGLxgVJVjZzXsBC2xTY4dM2nQVhZCg8At2sfODzjqRMhTBM4PJCom17milpj7Zp96K-j9Q-YILZcy-Z0jaKjPSO3bZhBtSg3oOvCppY5IY03w2wxJho4OkFxgSpSIk46YfJU02ohVYPfX569R1G1R7jOssN6QMoRCOO9SYuByEhYs_Hz6NEi8eEV_uOGVqvwcWVV49ZA_y5w8dUPkzf8RSoK_hEER1E-ENg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه دردناک سرقت تلفن‌همراه پاکبان در مشهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/Futball180TV/107119" target="_blank">📅 13:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107118">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOKCXLmGNxq_5Vdnw_2hqlstWOS9Zju9xSJ1_hc2w3MdIUpGmCDoooCaFTTbgX54giNfFSi5f0B9TK9aYZ8u8IF7XUPGhJGLLAnVV9WD_gJTQaQS3tKoH4NFdebVB3PRLKDXThRKzv-7keDoRapJleqao06hcYkDAX05tS2XH9_7MI-xIcwnaowb9nyaq4b5aZyaaCvxnPx3oaYCNQH5u_nuzm4P7ffFHdhRorl2G4Onvar9xDDCMHZ2Rzr_irF6VkYJyjtx37X8FAYB7EcsXqp-y5NiFhjXPejucLodHH2uUsges59-n9bbPIuriJ65h7Xep0bm4nOQTn7-GrSnTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
📊
5 بازیکن برتر در زمینه خلق موقعیت گلزنی در لیگ‌های معتبر اروپایی تا به امروز:
🇪🇸
لامین یامال – 6 پاس گل.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مورگان راجرز – 5 پاس گل.
🇫🇷
خاویر هرناندز – 4 پاس گل.
🇮🇹
پائولو دیبالا – 4 پاس گل.
🇪🇸
آنتونی گوردون – 4 پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/Futball180TV/107118" target="_blank">📅 13:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107117">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiB3scoQjTeAmWB8NrYqm-h5qBSdR9iohkXA6EazK70OXokUJQqB9yA-P9Z1O1QXec0DQEVJEknR6PXu0inqvPPDq9_nE16fVxF4R2w_gN02DGxUEnkHDnYcFitLiB4jWAQE8aH4HFE26st0JJeVdxLh_S70E5rNwgWq0nwaj7rq2OnC73vOgD6ibsL_9n1ciIl0KJf_ds99l4EFiV5p0196lLstxABNEMVFXpaijEFvOyUiDrR_XA4RTo_28P57l56h7BfivasepeIV8Fr-Mx2DJF0em5xaaHsV2FzvuysiIVJjRgr2H9v8YJLbCw4K5l5LQAqF7HCNkRBdQzOJBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خاویر آگیره سرمربی تیم والنسیا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/Futball180TV/107117" target="_blank">📅 12:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107116">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocGTV_2zloGhXjzXmBgA1RFQtYsVsydXJsG_P8Wt_bk7BqNtrHvvuw2tGcJLu6Gc2OSAd3rubyBY2qjl4GBBsYE7BRnYFOQSDmwgYf_y8jh_SN7WEGeBeeFTs28V-qcMUhEKmS9yVp2n890IiGQkZMu8uAbVlIkR6A4Mwg5S7S_e3C8iG9AX0LSxp3929xH31TSbg-Z_uWNiSSGczDoSUKSYmj7-BGHQZw0wDEQoOELwcoPqiCTLNKJK0gyv89MVy6plPrglSHIzq1YbER9LesrASdhTTVCXUQEVaua_JgxIJ8o3AXCpaWcx6QJZ3hhIYyBqA-1ifwgWHLmNjWRX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⭕️
#اختصاصی_فوتبال‌180
🔹
با تصمیم اعضای فدراسیون فوتبال، حسین‌عبدی پس از رقم زدن فاجعه در ناگویا، طی روزهای آینده از هدایت تیم‌ملی امید برکنار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/Futball180TV/107116" target="_blank">📅 12:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107115">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pvin1MBSNjselkuQy0SvJvMxzYZ26QCj__o_Szov0HRjb3vODi4Rgr4fGIqm3TBchNLx2QGfEc9NxZIzLtoKp3N-sfjzAL0TPEuwFtV6umhvHXmv779oTp44C0NuTwzGRyqDFoV__FnWMTD_dpdY60bbXFne1rldrwCz10gBS4bHbLj_vk_2lqxNzXWtc5V260GKJ0OPRtwVZtr2UIrRawizlXrod2Wk8aBkHW_anui2cmYigL1oZQfRJULqyH77YQuuhOk1ARp9I1rOt5mJmkz9PJliHr5vr172Tr_iXC9oKup491P_TCqtvUVb0uXGgW1vfx9LsWW1vNRCRMhapQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خداداد عزیزی از اونجایی که خیلی الگوی خوبی برای بچه‌هاست بردنش یه مدرسه تو مشهد تا زنگ آغاز سال تحصیلی هم بزنه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/Futball180TV/107115" target="_blank">📅 12:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107114">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a29oajhSbkSrelgw66WvRT3LOXbf-lHoBNNagwcLO01UlC7zaHpG18zl2csd8n6mLM5olPbjdp4wLlIzkwwinAXAjKWAjO3otpGZw1QOZh8LzPVN0D_QQcfs32_5EhfxoyzjO_jk0c8HJeT01dAQD4TgPDofS0eyjEldWMJJP-DG4x1TCRI_j4vTvyF3y_Xv4vDrLkSw8X7RoDIAZVxUbg7T20jr_OWNeg-yFXPsCIlUhcz3xyE26YruwxpE14zspJGw743hPmYk6XmfO5DYHPP_shpu4Q44zAV54kK-eSfUOlUQvNjLN9hdFG5KiRca0spThXWxE-fbdbTYuVLfdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
کیلیان امباپه:
🔹
"من نظر شخصی، سال فوق‌العاده‌ای را سپری کردم و این مهم‌ترین معیار برای جایزه توپ طلایی است.
🔹
من نسبت به توپ طلایی امسال خوش‌بین هستم ولی اگر برنده نشوم، ناامید خواهم شد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/Futball180TV/107114" target="_blank">📅 11:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107113">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53478857b1.mp4?token=c9GtfbSUMc-nvPkwnl7sTDsFcVaJqEsXk-wf40mHjeREi-mk06xuqx-eYaLBQVMGPMabn2Jj0MK3tvmFXQgfTajqZJAa9ugGWEb_s7ppxfjwZnANNKQiWEEusTSYcxGIcQ1OgNPVG4fniklOZAusGPJyNtFpjZ9_Dmt_b0rhtQH5Afp_OhiBC_tEAN5gw2e00cY5eiRSl-mKtSb9zNT4eNGr_GPjDVILHJ-qp6RpgzR4IKa9N9uXyrrVe8FhFuUg6CN5mfNv3UXibcp4bK3X0wS1yFNjciv2c9UVIiSbaQejl2zFBaSNhtC6k1BzMLrQog8XfbrZkfkoix0j3C5fwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53478857b1.mp4?token=c9GtfbSUMc-nvPkwnl7sTDsFcVaJqEsXk-wf40mHjeREi-mk06xuqx-eYaLBQVMGPMabn2Jj0MK3tvmFXQgfTajqZJAa9ugGWEb_s7ppxfjwZnANNKQiWEEusTSYcxGIcQ1OgNPVG4fniklOZAusGPJyNtFpjZ9_Dmt_b0rhtQH5Afp_OhiBC_tEAN5gw2e00cY5eiRSl-mKtSb9zNT4eNGr_GPjDVILHJ-qp6RpgzR4IKa9N9uXyrrVe8FhFuUg6CN5mfNv3UXibcp4bK3X0wS1yFNjciv2c9UVIiSbaQejl2zFBaSNhtC6k1BzMLrQog8XfbrZkfkoix0j3C5fwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه گزارشگر صداوسیما به قلعه‌نویی و عبدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/Futball180TV/107113" target="_blank">📅 11:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107112">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1yn0lD3Vb145FN8xomL3DA_cC7pYFuGsVwjytvpwwzD0JsZS04BF9lFpQRYIntLcEIfHwySchpbD3shaXD-FoVD66g-CI7xmXbyYVXTRcUzfm4lJLpv9Gi8P6PLquPRe0Arx2lvomOgNRl6MmX5TxW_RS9kdqHpRJvD6kowtQeHatJJgqFsadD2A0LFzsCDLjsw0LsF4DA0-DnHxnmCi_3VVAsyvTr-rw3fNrp4rQrchX8EH71DZjn5hLDJht1y-YqlpQtLNbp3m47n4OkktloHsfIbg_JCJRgcVm2D34XDQh1Bqsvg4Bqxz5o1ZbuElEJlqEIGCRvvhW6-3qaS5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
رافینیا:
🔻
"به نظر من، لامین یامال باید بدون شک برنده توپ طلایی شود. او آمار فوق‌العاده، افتخارات، جذابیت و کاریزمایی را دارد که او را برای این جایزه واجد شرایط می‌کند.
🔻
به نظر من، عملکردی که او با بارسلونا و تیم ملی اسپانیا داشته، این موضوع را کاملاً واضح می‌کند و او شایسته این جایزه است."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/Futball180TV/107112" target="_blank">📅 11:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107111">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107111" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/Futball180TV/107111" target="_blank">📅 11:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107110">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8ulsxGLTf-i73_7HduF4Dixj8O0ivyKh_TY_8fj2NSyCJxCIZX-0izbc00MOR-RsbrOJ3jkWT-x9F1WUEUsgT_Qz5A2zk6f8rKV88_Vn-kYG4Q9uSP1qulgDWuYzv_DJcSnbnXmAzllWncjguQcwinWqqw111S6YXHOShL51794kyyb-8Wvj4QYupDktmSnZ6_NRzwuZn6SDze9xtd9kfUgsiq8lVfWphDvkW3qOmrHh56eX79OuesyqQ-G2TEffqi5PWnSC6cJYLSnQpJpahKrY3EuNZTxCIMm13ALOzvePsPIEHchPgsxcMt_G6fOKZdbCr5EWip1G_KxnD5jIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
هیجان مسابقات DOTA 2 را زنده در
TrexBet
دنبال کنید و با پیش‌بینی دقیق نتایج برنده شوید!
🦖
پوشش کامل تمام بازی‌های محبوب Esports:
‏CS2, DOTA 2, Valorant و ده‌ها گیم جذاب دیگر...
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/Futball180TV/107110" target="_blank">📅 11:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107108">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9548a0e3ec.mp4?token=TM5kRr5Dd8BHdNjihYaBhvU4cUPg9ytI3BZEFa14b-gs_bCay6hfyHjOtCk7npJo69YXWpxInip5Ymh2lIkJLW4yS54ZFI6A-AHaA9toEZ_s5BSE_FeanPeohl1WUEtb0zh1-WK5t6qi4SET6dxJodf3csXxWk4hsqy-o-KwxtkDTCYLTp4b9RMfWFQqKXS0scYssnQNZV5bgkuj4dgQxZ00WN6hsjR1F52XII9HXe5YcbIhQETlR_iPazf5jNPxr3NoxIxTrYj2OxA1nY68fiYyGvYWKwv_V1-gjqApusUGR8Q7IGQ5UkDdnsa28v7Ufq0-LUNp3eoAQB2OQ7R3LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9548a0e3ec.mp4?token=TM5kRr5Dd8BHdNjihYaBhvU4cUPg9ytI3BZEFa14b-gs_bCay6hfyHjOtCk7npJo69YXWpxInip5Ymh2lIkJLW4yS54ZFI6A-AHaA9toEZ_s5BSE_FeanPeohl1WUEtb0zh1-WK5t6qi4SET6dxJodf3csXxWk4hsqy-o-KwxtkDTCYLTp4b9RMfWFQqKXS0scYssnQNZV5bgkuj4dgQxZ00WN6hsjR1F52XII9HXe5YcbIhQETlR_iPazf5jNPxr3NoxIxTrYj2OxA1nY68fiYyGvYWKwv_V1-gjqApusUGR8Q7IGQ5UkDdnsa28v7Ufq0-LUNp3eoAQB2OQ7R3LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دیدنی تیم فوتبال الکترونیک ایران به حریف ژاپنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/Futball180TV/107108" target="_blank">📅 11:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107107">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcZwqwg4VzZvmK_5z1WitwS-ncBnM8ayg-83iBcF-iJWAtMlN5q4M048u6PMnMsc6qmP3Etv5gSEJwKgQInK58F82zCR1V1nKFN-g-onBUWl76uK3VeG4g25-vDvsh4Y8Rn9Y9mx735UzJ52IOo-Xy6sG5nsWlWtYIhkHiIUZqYWaqeqTl7QKsDCm9MgvQirn_-F2vn6U22pWFvuKZDNR8jStM_Uzb4TKqcl-MC2T7qwksW_fW6K7PnEr0EewsNXbZlxSRSavKCMjKeYfomItnLmotlQEQSu3c80CeS0veuHGaYgw83rYayBs5q0izmz53R2AiAggSjhtDbK2umQDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⭕️
#اختصاصی_فوتبال‌180
🔹
با تصمیم اعضای فدراسیون فوتبال، حسین‌عبدی پس از رقم زدن فاجعه در ناگویا، طی روزهای آینده از هدایت تیم‌ملی امید برکنار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/107107" target="_blank">📅 10:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107106">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWFFjfiEqb5NToyvnk3MC-qMlQtn6f_YWipnD2leyLO8-eNXUzt82UtZUadp6rvMk6KkK7C4Plgk9hkc-y4psMCfJ2y1yw0T88dbPgv-wJ2eatB158ZWUZvGD-qPFkpS3tsobD4YYrgGUKo3uTPVoJgeTQl2rn5bo3aTTfWn7SR8Yuw0UOud4v9ODtVh_ug2W_uwcPQ1Tsa2viC6XM42ddx1nIeqIYWvo0Bu34pITB76j24I3gEAQ0gP7-s3VdfuiEfXRI51QJwbDc_0jyUnlR0BAI-rL5HXdBlNw9LWBfwbnZKoOBLssGgfviQiDg-oJ2w-rBhhrWeiNOc3uemdBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان‌بازی|شاهکار حسین‌عبدی پرادعا در ناگویا؛ ایران با شکست سنگین مقابل پسران کیم‌جونگ‌اون از صعود به مرحله حذفی بازماند
🇮🇷
ایران
😃
-
😀
کره‌شمالی
🇰🇵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/107106" target="_blank">📅 10:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107105">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnHmLD2dAyaFH8NGYyPPoiAIMslHKpvYRNkEWPU2p6qSpwL-UDGjqqRDUu6Xg_TmezTC3VqI4taAKak-0ZREO1ngrbP8vXyEe2XfqfeZ8Q4cPH-flyfVEMiWeNfcgC3jK3C8Dl1oPE9NQXfPjSanBBWi1jf4KLmm3aWaHtcZ6gyKS1AWtBO9qqldwffszZDLpR9UgsR93ynGmvB_6baOtTVwLZ1UjCFRTgm6GjaEbBWUv0cXc332CpZWnJkANJrOPeXz3levE2vEsxXhWk3AIcl-6v3Z4e3FsSKpiDceFEUqYzSu6BJRLjKRgRkyU12WxPVP1iV8XqAOhqbxiXS4JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان‌بازی|شاهکار حسین‌عبدی پرادعا در ناگویا؛ ایران با شکست سنگین مقابل پسران کیم‌جونگ‌اون از صعود به مرحله حذفی بازماند
🇮🇷
ایران
😃
-
😀
کره‌شمالی
🇰🇵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/107105" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107104">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65dff3514a.mp4?token=WgC9GBTlk0CiJ7H1ttle8GUyGYc21nGo07rsD2-0epvA0gqqsFk2Iji0rAMHpUu5YnGa9aZ9EDS76nMDhtS4Svyci1kDTiMw6Mv04XQLu7aGd68EMfVFQJkb5brbECOJB6Qg2wHBsiBCegv35xQRwCx-N3dM6cnkQpw_AMOsP-E3J05svzFx8Q4nYwdISv3gAxq4k7tSexTnWWl2F5NbqxzzqkHx4vCw18Yq_8CR2H9j_Gsj3EdMN9d6PT0X_Sphg1vHpqA9W4T5vnJXeElLer78hCVzUIv9XLfEFuJdgSxU9POGycinMgKV_K9C7VCH4Hl59Oiul8JrjAnJNwigKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65dff3514a.mp4?token=WgC9GBTlk0CiJ7H1ttle8GUyGYc21nGo07rsD2-0epvA0gqqsFk2Iji0rAMHpUu5YnGa9aZ9EDS76nMDhtS4Svyci1kDTiMw6Mv04XQLu7aGd68EMfVFQJkb5brbECOJB6Qg2wHBsiBCegv35xQRwCx-N3dM6cnkQpw_AMOsP-E3J05svzFx8Q4nYwdISv3gAxq4k7tSexTnWWl2F5NbqxzzqkHx4vCw18Yq_8CR2H9j_Gsj3EdMN9d6PT0X_Sphg1vHpqA9W4T5vnJXeElLer78hCVzUIv9XLfEFuJdgSxU9POGycinMgKV_K9C7VCH4Hl59Oiul8JrjAnJNwigKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل چهارم کره شمالی به ایران توسط چونگ سونگ(68)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/107104" target="_blank">📅 10:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107103">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گلگگلگل چهارم کره‌شمالی
😐
😐
😐
😐
🚨</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/107103" target="_blank">📅 10:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107102">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c68b593c8.mp4?token=tlTaT7cSgx-MZ2Xmb2h7bYzkOrKyjowvLdJeYknMHrUJOPujHmOZTWLOkv7IbYrnkuHhk7e6DkKp45_tM5Nqei7IkYBhPxgs2eCgygd-tGBbnEAlBIiYdCtJz9HewwfKnG2qR-5GwCPNZjHQmqEou7GfjI3NJQs5Vp7HHdxLmgsK7ccePcZGdobZXycVLzGUTFLlO8mt0DACVOzKp-7KAxbzLBTeJOjYhg28pYYWXQCDGGdgi8Wd5EyW4hc6P9scrDQdPkNrJkgb4CLGA-3kh8TcUBXTE_xliZ_V9kBpNms8s9KNSbUYEuNkqUUOw3Nve47-d7VCp6ROlTSw68YSmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c68b593c8.mp4?token=tlTaT7cSgx-MZ2Xmb2h7bYzkOrKyjowvLdJeYknMHrUJOPujHmOZTWLOkv7IbYrnkuHhk7e6DkKp45_tM5Nqei7IkYBhPxgs2eCgygd-tGBbnEAlBIiYdCtJz9HewwfKnG2qR-5GwCPNZjHQmqEou7GfjI3NJQs5Vp7HHdxLmgsK7ccePcZGdobZXycVLzGUTFLlO8mt0DACVOzKp-7KAxbzLBTeJOjYhg28pYYWXQCDGGdgi8Wd5EyW4hc6P9scrDQdPkNrJkgb4CLGA-3kh8TcUBXTE_xliZ_V9kBpNms8s9KNSbUYEuNkqUUOw3Nve47-d7VCp6ROlTSw68YSmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇰🇵
گل دوم امید کره شمالی | را میونگ سونگ '44 امید ایران 1 - امید کره شمالی 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/107102" target="_blank">📅 10:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107101">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23009325d2.mp4?token=XjpMapAwKcmcIi7Q2rUEp76tVCYwiqh4QSIuQD6RaUCIxwfIjv_wTlzRiOKnHM7GZulLDRVMrbhb6dyP-SOxV_YKeAXwRckO5HDApBolE9Fcy1fH7e3sbE6DwA7VdOcjH8PRgOwgervb1riRGTmSF--mi_xihJCDF6u17BeeRJrEOuOjKk_U_ulufCQm1b7vUcJDG4DZ26KmCDpJhnZ2bbHbBFlTWn99e-tPilsw_dDsAv10GuLoF19Td4A50df2uh2x9dzbCKbderH4jmUfgz6D-JjE7p9mN2bC6G_FCrWA1A_pRbIaf_ConJXvzbVdRJcT5zMYnHCgPY2_0ohjBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23009325d2.mp4?token=XjpMapAwKcmcIi7Q2rUEp76tVCYwiqh4QSIuQD6RaUCIxwfIjv_wTlzRiOKnHM7GZulLDRVMrbhb6dyP-SOxV_YKeAXwRckO5HDApBolE9Fcy1fH7e3sbE6DwA7VdOcjH8PRgOwgervb1riRGTmSF--mi_xihJCDF6u17BeeRJrEOuOjKk_U_ulufCQm1b7vUcJDG4DZ26KmCDpJhnZ2bbHbBFlTWn99e-tPilsw_dDsAv10GuLoF19Td4A50df2uh2x9dzbCKbderH4jmUfgz6D-JjE7p9mN2bC6G_FCrWA1A_pRbIaf_ConJXvzbVdRJcT5zMYnHCgPY2_0ohjBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇰🇵
گل اول امید کره شمالی | چو کوک '41 امید ایران 1 - امید کره شمالی 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/107101" target="_blank">📅 10:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107100">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/663cefc9c1.mp4?token=G41pLqkkifQ9F0-0plze3i5I27fGP4uwLWJt1QmO-tf11k98eZe8MRdaX1gWnvOOKFFJ8iCeBGKXP5eOvQB9VgYffsUJPJuCFOn5wX82IEVOK3ONDvBsts6q5lcHZE4mIzAZiZjm8Ya4Xfa8YGmkeVKEjt3QZHzBQeLyKo_N_qbVjLT0wJ520cjf4KIRwXhkarZzCHbYO4YCQMC5I4h3UY5ZWzNQPaV2Kv30XeZEn5rz4snEekABgs9fr4ysJTHj2S_sfQyCxC1PHsYWKHMAqGXRa5H9l831MuRB_D3NK_EQAsfQW1k-pR7KBRJqEmtol2UNFSox76VaZIGNqEnb7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/663cefc9c1.mp4?token=G41pLqkkifQ9F0-0plze3i5I27fGP4uwLWJt1QmO-tf11k98eZe8MRdaX1gWnvOOKFFJ8iCeBGKXP5eOvQB9VgYffsUJPJuCFOn5wX82IEVOK3ONDvBsts6q5lcHZE4mIzAZiZjm8Ya4Xfa8YGmkeVKEjt3QZHzBQeLyKo_N_qbVjLT0wJ520cjf4KIRwXhkarZzCHbYO4YCQMC5I4h3UY5ZWzNQPaV2Kv30XeZEn5rz4snEekABgs9fr4ysJTHj2S_sfQyCxC1PHsYWKHMAqGXRa5H9l831MuRB_D3NK_EQAsfQW1k-pR7KBRJqEmtol2UNFSox76VaZIGNqEnb7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇰🇵
گل اول امید کره شمالی | چو کوک '41
امید ایران 1 - امید کره شمالی 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/107100" target="_blank">📅 10:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107098">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b315f04dc.mp4?token=MqwGaflYArnK3Q5CqjDffV-kqqkjsJADJxLqH-v9i0OR2uBWHiAlvTGweXzONKK88n9yes8apLBt9n2dCKracB14jM-X30q8AcQ5x9ETMJ-D7TTOJaAdOV-fiAs6kl_49ga8DxkcjCTMY4mbxqMBXapruGIT91lxUDliLlu9eE6Rd1BQ_tlkv2xtQJdsURWAayILKAfuaI3R_kmSqYYkiJhJbMmn8IbrEudT3JegaWZ-2SfbIdcmRN_eHVN0eCMo1P4_r3Ol97tVg4xWcmMt82B5C-7WkAW6z4GWUE2yF7tgvGGI_I6qXolmVZ0jwzSxBkg0D5WSrbBIr_cC-NJD4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b315f04dc.mp4?token=MqwGaflYArnK3Q5CqjDffV-kqqkjsJADJxLqH-v9i0OR2uBWHiAlvTGweXzONKK88n9yes8apLBt9n2dCKracB14jM-X30q8AcQ5x9ETMJ-D7TTOJaAdOV-fiAs6kl_49ga8DxkcjCTMY4mbxqMBXapruGIT91lxUDliLlu9eE6Rd1BQ_tlkv2xtQJdsURWAayILKAfuaI3R_kmSqYYkiJhJbMmn8IbrEudT3JegaWZ-2SfbIdcmRN_eHVN0eCMo1P4_r3Ol97tVg4xWcmMt82B5C-7WkAW6z4GWUE2yF7tgvGGI_I6qXolmVZ0jwzSxBkg0D5WSrbBIr_cC-NJD4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل‌اول ایران به کره‌شمالی توسط حسین‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/107098" target="_blank">📅 09:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107097">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1971f21e3.mp4?token=KOQ_J_1JEj_Dp4lVFk9bw5po-Hr1JejPVDP7-eaVR28Vs1YtiMtaDDajBnEzuM3Y0dzXkoLMQsSzIZRhRvaIHRkJmx2F0DUXloXzRe2qHeFDh0oS9pHlo6BQMlouQf-Uiai2q-9HLvi9OcjcmFnZTrNXeYHxaH3RclNIfIQSbF1n9xJsdDoSqFttRIdv0wnUhAZTuA185QIQ8X9eXmZz-xNKKo2tqOIIb1sYw2FFGci-0R4JPYoN3W1K-hoDz_uRpKO5QMyXvgLq0r_DmEVJXfhWcNaxgt5kvtczF_t9Qq2kmSUmbLTYikUoWZQRfshZK9BGlx91xGnUGycVVk5DVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1971f21e3.mp4?token=KOQ_J_1JEj_Dp4lVFk9bw5po-Hr1JejPVDP7-eaVR28Vs1YtiMtaDDajBnEzuM3Y0dzXkoLMQsSzIZRhRvaIHRkJmx2F0DUXloXzRe2qHeFDh0oS9pHlo6BQMlouQf-Uiai2q-9HLvi9OcjcmFnZTrNXeYHxaH3RclNIfIQSbF1n9xJsdDoSqFttRIdv0wnUhAZTuA185QIQ8X9eXmZz-xNKKo2tqOIIb1sYw2FFGci-0R4JPYoN3W1K-hoDz_uRpKO5QMyXvgLq0r_DmEVJXfhWcNaxgt5kvtczF_t9Qq2kmSUmbLTYikUoWZQRfshZK9BGlx91xGnUGycVVk5DVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
دلقک‌ترین استاد کسخل در تاریخ سرزمین ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107097" target="_blank">📅 09:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107096">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/625edd4ac9.mp4?token=nNUOs3ksXEuToY79NX0_5c8OjkUvMhMbfO1Frh0TrbwBtZg_T2dQvMsBwQL2ySqBqR72GFso9FQy6-XmSMTVLnJAeld1YXiqnNScJ0BfzkClfkBJGdtPtnKbKKOscA4vHFo0OxfYEi1-iNQ2Fy_f4CmXASnov9Lixq4-NyEgp7rYVwjJ3NcZOcgcVj4qVWKNy_CJFEo-96Sw5XyMstzvo3WIVArYiZv0Nmc11hgpfKebDO58lb9DodRoeb7wRPZ-D9anTvQQ6tRw2ItrHyL-8QkGExJ2KrF2H-mBy1wNWR6XM_ZXGk6OSPtg3sRdiFu_mqVrljwsfZL5BZHhsBZ29A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/625edd4ac9.mp4?token=nNUOs3ksXEuToY79NX0_5c8OjkUvMhMbfO1Frh0TrbwBtZg_T2dQvMsBwQL2ySqBqR72GFso9FQy6-XmSMTVLnJAeld1YXiqnNScJ0BfzkClfkBJGdtPtnKbKKOscA4vHFo0OxfYEi1-iNQ2Fy_f4CmXASnov9Lixq4-NyEgp7rYVwjJ3NcZOcgcVj4qVWKNy_CJFEo-96Sw5XyMstzvo3WIVArYiZv0Nmc11hgpfKebDO58lb9DodRoeb7wRPZ-D9anTvQQ6tRw2ItrHyL-8QkGExJ2KrF2H-mBy1wNWR6XM_ZXGk6OSPtg3sRdiFu_mqVrljwsfZL5BZHhsBZ29A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
هیچکس نباید قهرمان شود؛ خیابانی: فصل گذشته باید از تاریخچه حذف شود
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/107096" target="_blank">📅 09:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107095">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107095" target="_blank">📅 01:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107094">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+hgTgtcXHw1k4ODA8</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107094" target="_blank">📅 01:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107093">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfrFY9Hk4MCifHyW2Bpa2woSRg4NsAejrl_kSizv8Wcz3pUnP0Ht9Px_uwZ8vE8S5nGZh1zRoXY0wNxAiLffaZ4p5eM5af28XJ_fChsDedOiX--_SoDvvRdY5qNFFcjcBo13tsTisFvmKST2JM7Hz_EepwV2U8whGGsT-tHwe63z3SedhAt6J9ymArbl6XHWSlXgksxTtgzOonKMaaQo1CDQiBBNdbB9F2NpnzxAimQKYuJhb9njoPw8pd0nqd9-e_3Ph8jbO3ia2HzIiR_jBvzGA8FhqHxHm3vBINKoozG0CCipmsKktrTtHczg9LA9-1sLUtWU3uG7yg3mC_I_YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو اعلام کرد: قرارداد آرتتا با آرسنال به مدت ۴ فصل تمدید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107093" target="_blank">📅 01:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107092">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Siukmh3VqTiRt5AShb8VfjrYz6HWahS1bqso6DEyolfhNnNBJn5nrGL5NT1nC260AZ3skuOOVsF2MFU3V2l223pz_EqNS22wzNOAv4viaz5eVyZbo4ybC7UaGj0xJfABuJ-g5HeGv6OcVOSFA-qQByJgdixOOUlTTtprHAJZGShmDN-dKcIKgAASIdfmLSlq5tFuDKaYCCe-l9CxTBkDQdaKheqG30h8ohaTMC-onlEJnuzwwPjHtMXKcIdYgTaRpQk5vqJ_tWS6qEUfRrS0pvGB34z4gwejp5asWMqlWN-V1M1irNIggilQ4uifglAbWq1hNKnHoCg0p_S2Ak8CIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🔥
بعد فیفا دی عجب روزایی داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107092" target="_blank">📅 01:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107091">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rujAL8pUzTaMuNt73fA6KNH-1s8iEiEuyjbCZEB8QwQi6sZa2dHfocCRozuC4uy3BZ_l2kxSweznU8Gc7EBcHqAESATz4Q16KmU0CKSDFfSywVcx3GJtNnUG14q20gvznASWQkPFFrOKEsRkzAk1tKDEy_q5U8schaK32kbQ6vq6mr-INkMXUCFCnCPu81WX4O4BbHGB0d02qHikh4UKGtWOr6Blgaq9HpeKoCdYO0iAzvfCSRij890xLFQQSHz8PcNVUb6qYRDhwk51IPN2AT3vb2tbUK99t88UEiqc9Ia_j6nF1Eei7KazQT4xaO6WftZQd38QIe4CBqKPaRdniA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیفو سکسی عربستانی‌ها برای بازی فرداشب با کویت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107091" target="_blank">📅 00:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107090">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhVI5qpphDMjBHsxQZOoqoncY1ApjLCkfqBMPWCGaEZnX6meX0Jb3W68V1tkC2YpN8b_4fBmyNf4Ej-FHrQscyR_lnoA_6FERbjp1pR4thUCiMS0I6Noyu6Pp9pTqmsfF13jo0P5x1fqRRgwGTPAVTRBOLzPG1zGRSTYYUoYVwgq_oQ4oA54G-HF9ZX_PeYz4uI_rPsV3v0llMDJF3nQUu67KSJO8hggYNzuVMFCaahKkUiDbcqvAtThc2nM7f0cqFPmQo8YsO_2pJbCjXuZgrdsdy1TskC4B3mZ8D8Wq2pKTkmFKmkFK2SNU48NKzoTZVTJIRGBVie9RHaW_30qpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
عراقچی و ویتکاف در حاشیه نشست امروز سازمان‌ملل با هم دیدار کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107090" target="_blank">📅 23:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107089">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eec872952d.mp4?token=bL-W7lkCpgHUOvYzfADqM3TR5JimlhwC-zH7m5XuovqSfGI5JBtNtc8rT8kJ24RmrAt4y3BLchRTbj40ja9ydqgzk5mFNe5pEQwQocEgpZ_ts2KzsSXlZyEr8x-4fz65KwP7CVUmYhazYQ_00rVBOJnVZEL3bavuPfPc3XuaIBEJUckX_FgBcw2m9JpVjQJYppq5D8trDzs7fsg0h1u0h5t4QA5hkvBGqFURBp7mScwGWYkAElVEHihAMe291J4wogomtIxA73ldPO8PRna9Ia1HjY27607aLFomJXBJU0Hy-Lj7fLtXS5PLLhfpgL414Bhv7aArsCt1AgaRqLdhP29YibrqYGmJev5WK4g_IkVvlLoMHjF2IJNQd79gIQBl7M5JY11cWFij_b4Tkm6prThyploWd2rOj5sT4AdzSXwKwZcNckaJtt019wWEh-_dxgMD_NzENJWcxTotk8OD1r86V1VRbXVM30YXt0IZZJqS9Cdn2uBJ814XIGvT5srrSsTzfwnpqF_Obr4FF5gWsgzjpJMeav9Z89q13OLFsbwxmMOT6A5XhZa_cyXRm2OQxADtA14aeAsZ3RnfWbI7pxGjARZ6G2mai2jsC2GsgVrInhxXHipHKJvbg24oG2mbOwVt9ttjw8XEdBxQS5f1ZtVhlCT2no2T3cCdeYfgCnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eec872952d.mp4?token=bL-W7lkCpgHUOvYzfADqM3TR5JimlhwC-zH7m5XuovqSfGI5JBtNtc8rT8kJ24RmrAt4y3BLchRTbj40ja9ydqgzk5mFNe5pEQwQocEgpZ_ts2KzsSXlZyEr8x-4fz65KwP7CVUmYhazYQ_00rVBOJnVZEL3bavuPfPc3XuaIBEJUckX_FgBcw2m9JpVjQJYppq5D8trDzs7fsg0h1u0h5t4QA5hkvBGqFURBp7mScwGWYkAElVEHihAMe291J4wogomtIxA73ldPO8PRna9Ia1HjY27607aLFomJXBJU0Hy-Lj7fLtXS5PLLhfpgL414Bhv7aArsCt1AgaRqLdhP29YibrqYGmJev5WK4g_IkVvlLoMHjF2IJNQd79gIQBl7M5JY11cWFij_b4Tkm6prThyploWd2rOj5sT4AdzSXwKwZcNckaJtt019wWEh-_dxgMD_NzENJWcxTotk8OD1r86V1VRbXVM30YXt0IZZJqS9Cdn2uBJ814XIGvT5srrSsTzfwnpqF_Obr4FF5gWsgzjpJMeav9Z89q13OLFsbwxmMOT6A5XhZa_cyXRm2OQxADtA14aeAsZ3RnfWbI7pxGjARZ6G2mai2jsC2GsgVrInhxXHipHKJvbg24oG2mbOwVt9ttjw8XEdBxQS5f1ZtVhlCT2no2T3cCdeYfgCnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇫🇷
اولین تمرین خروس‌ها زیر نظر زیدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107089" target="_blank">📅 22:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107088">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53976f40f7.mp4?token=F8FmfRg7U6E20BO-MYrupZwOVD8QN4LFWy43FXWUB60oB-1V1R2QNsoc3VKdYt4TEU-TvopO-eJv5UWu1-aDyP7uUYsMngDx1v_fxm74gLZIbucx8Fp7gE1QVv8X2lClGi508ev0WJemfFzU-UZ2IAMLx27A8e2EMETelY3yJzAOYhc2b7ubanpk4lSHYJYWNAEACyrN7GpbagH8fYmoVUAAvDzpLB_SJxVLDmNmv85ucZNjE9zekDWe7keXVvIkVkdQcUT856cMKZrjRPoZFwAJPCCbgxYP6nwo4KowYZ9MYCu-r6Ym3zVJniRnCcHkOqaCINCP_J99QTr6gdB59TuDJKnQ_DhFHVvohmIgOcbXKLb3NTCxjR0VD7ZlaB2TP7l5yxb9fxox6FiZB1DM-kMCf2npf4pmAZuABSGcov2KNuad1iGaiUaNRdu28-s6Z1rCqS8mm7nbpmG4ERfmII7Y-dhOOJlXO4PGmVgn5lNg28Jd3pW7A1jW7vxJUTtkYh-SEUPuTfWKqEuZGRYtJvREHL97Hi9hswLh9tO5BaGa7Ad3WGGh2nnDf-L-y-5jx_xzVx1OGinjTDtWLEhSAubzaknmndJ0o49_lHfE2_dNb-GP8cn2giUZh-HAdI9sexzmrGUSIdS_tzkBOq-t56Ja_yxert2jUkjfKG8QSa0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53976f40f7.mp4?token=F8FmfRg7U6E20BO-MYrupZwOVD8QN4LFWy43FXWUB60oB-1V1R2QNsoc3VKdYt4TEU-TvopO-eJv5UWu1-aDyP7uUYsMngDx1v_fxm74gLZIbucx8Fp7gE1QVv8X2lClGi508ev0WJemfFzU-UZ2IAMLx27A8e2EMETelY3yJzAOYhc2b7ubanpk4lSHYJYWNAEACyrN7GpbagH8fYmoVUAAvDzpLB_SJxVLDmNmv85ucZNjE9zekDWe7keXVvIkVkdQcUT856cMKZrjRPoZFwAJPCCbgxYP6nwo4KowYZ9MYCu-r6Ym3zVJniRnCcHkOqaCINCP_J99QTr6gdB59TuDJKnQ_DhFHVvohmIgOcbXKLb3NTCxjR0VD7ZlaB2TP7l5yxb9fxox6FiZB1DM-kMCf2npf4pmAZuABSGcov2KNuad1iGaiUaNRdu28-s6Z1rCqS8mm7nbpmG4ERfmII7Y-dhOOJlXO4PGmVgn5lNg28Jd3pW7A1jW7vxJUTtkYh-SEUPuTfWKqEuZGRYtJvREHL97Hi9hswLh9tO5BaGa7Ad3WGGh2nnDf-L-y-5jx_xzVx1OGinjTDtWLEhSAubzaknmndJ0o49_lHfE2_dNb-GP8cn2giUZh-HAdI9sexzmrGUSIdS_tzkBOq-t56Ja_yxert2jUkjfKG8QSa0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
توضیحات بازگشا سخنگوی پرسپولیس درباره شکایت از آسانی به کمیته استیناف
🔻
فردا به آقای تاج و فدراسیون فوتبال نامه می‌زنیم و سه درخواست داریم. حضور وکلای پرسپولیس، ضبط جلسه و پخش آنلاین جلسه رسیدگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107088" target="_blank">📅 22:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107087">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvrJb56T6Q2UV67fYclxjWB1qHfL_jZ9A6MP5pglerxx7wjvvlIfsJoGVB6eZjtF15h5owESIFaHGjLWcAYSyNj4xX79qRWq7JTmUQQNsHZnC8974dJYm2BGqSmb9PboeOljix5QeqEq0SdLpnnxAgekY6LPidYWnKN7uJ5T9CqHDkUH8ib2DdnqYJ-nWd_utSoi1zOZxVak4H87cVef-Zzt_nix6QPrf6k9JaFPXp8JMfKeKRNF2WFAbaX66DCn4UhLmXriDkb2poyJRNsV690U6e3NB2V_Ezz0joKyrc0_vwTsYb4e92ducN9CIXZo1TyoQYxWmcHMwrhd2ZoBJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
جمهوری آذربایجان رسماً پروازها به ایران را تا اطلاع ثانوی متوقف کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107087" target="_blank">📅 21:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107086">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91400e175a.mp4?token=GPgHgjjEi_3QrZWZdF96eKuBDL2bdqY2dWJmLK0IKbyj88qRWSrKoEnzcLknDfggnj2PYnrMVew6Czh6XDKUCDWwIcnegh8jQpTqyH0XghxsVGEuJArz1aj3SE91nrz6vs3AcvqqpMEqrlIzWjJCQ5RmU8-ZQ2OYdtzRW0xrRut-sLKdPQlDZmgZU-tET84MD7glIlBr9AZFxpEUinFM-DH5jNKVoRRRwVyqZGAcqjlTFyoVBEfwyV5Ho4HpM0zbunpUaqNQ6jY5BLIjEWihcTKKjwOmQIR272nON6wY1YvBKogTC_ghHS2HrZh5mmvGhXnoVZIiVbyyp09De9uwVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91400e175a.mp4?token=GPgHgjjEi_3QrZWZdF96eKuBDL2bdqY2dWJmLK0IKbyj88qRWSrKoEnzcLknDfggnj2PYnrMVew6Czh6XDKUCDWwIcnegh8jQpTqyH0XghxsVGEuJArz1aj3SE91nrz6vs3AcvqqpMEqrlIzWjJCQ5RmU8-ZQ2OYdtzRW0xrRut-sLKdPQlDZmgZU-tET84MD7glIlBr9AZFxpEUinFM-DH5jNKVoRRRwVyqZGAcqjlTFyoVBEfwyV5Ho4HpM0zbunpUaqNQ6jY5BLIjEWihcTKKjwOmQIR272nON6wY1YvBKogTC_ghHS2HrZh5mmvGhXnoVZIiVbyyp09De9uwVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد چلغوز گودرزی رو داشته باشید که دوباره تصمیم گرفته بره مقبره کوروش
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107086" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107085">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
تمرین تیم‌ملی فرانسه
✔️
کلاس آموزشی تیپ زدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107085" target="_blank">📅 21:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107084">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🙂
💥
مسکات حلال‌خور اتلتیکو مینیرو برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107084" target="_blank">📅 20:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107083">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8c040c455.mp4?token=CCnwhkUubhuErj1LyQqqfSZfNzghWDsYj4_aUv4QzwqNYdg6UCYqH7pUR5UZKnZzfRkhyunXOuaz3khAgf68VM2bHLi4HMbE-tTreALdARNKURLONFMqR6QmRCUUebxwySIApPrvIABEwzuHp_pW_bpytSUec420NqF18YtXI89mrNsVz6rT0ZKn97T3OR2SRxo8qmI1DfvkbdOshE_qH6VD3HogVo9j3ugvVzxs7I66ygumCd8hMYYwSMCt1ygXeK77Wd6e08e5jmpPLqzI3IfZ8K1JZRC8g2teqCJZ5YCHKnewcso5SptxqrtUT7N1jNHu8_2ZWRSbNmmyzkhbpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8c040c455.mp4?token=CCnwhkUubhuErj1LyQqqfSZfNzghWDsYj4_aUv4QzwqNYdg6UCYqH7pUR5UZKnZzfRkhyunXOuaz3khAgf68VM2bHLi4HMbE-tTreALdARNKURLONFMqR6QmRCUUebxwySIApPrvIABEwzuHp_pW_bpytSUec420NqF18YtXI89mrNsVz6rT0ZKn97T3OR2SRxo8qmI1DfvkbdOshE_qH6VD3HogVo9j3ugvVzxs7I66ygumCd8hMYYwSMCt1ygXeK77Wd6e08e5jmpPLqzI3IfZ8K1JZRC8g2teqCJZ5YCHKnewcso5SptxqrtUT7N1jNHu8_2ZWRSbNmmyzkhbpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
🇮🇷
پیش بینی چند هوش مصنوعی مختلف از قهرمان فصل گذشته لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107083" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107082">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=fDbswZjmKyf0a6c4ngKyYoQFm-38xtRH_8fMAyElQxdKk3isO_BJkcsYSibQhIo5rXM1M4QqNgjf-fd3j2wT6u3h9eS8RpZ4Po_J2PQZfFnq7zQ0Bk2GivnO2-8ENvX-avW25oWdrJW6yME9Abhzx17X4ctbp4IiVhGg37FvrEOXGBhjSkkDqLoZBOTys4sibPpho3K94ngeRDAWL06vfOA7fAGo0E4zN3W-b6u5K500jCnm9dfDQ8YjcHIWlnrKZakVIIBrPIpDUviAs1Bjr8b6gB4iRemt4tfqpwXoVkt7gi0xuTUfYZbCHB4ruhz3uGWzKZisFGFfki7GxycT5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2433cb0d35.mp4?token=fDbswZjmKyf0a6c4ngKyYoQFm-38xtRH_8fMAyElQxdKk3isO_BJkcsYSibQhIo5rXM1M4QqNgjf-fd3j2wT6u3h9eS8RpZ4Po_J2PQZfFnq7zQ0Bk2GivnO2-8ENvX-avW25oWdrJW6yME9Abhzx17X4ctbp4IiVhGg37FvrEOXGBhjSkkDqLoZBOTys4sibPpho3K94ngeRDAWL06vfOA7fAGo0E4zN3W-b6u5K500jCnm9dfDQ8YjcHIWlnrKZakVIIBrPIpDUviAs1Bjr8b6gB4iRemt4tfqpwXoVkt7gi0xuTUfYZbCHB4ruhz3uGWzKZisFGFfki7GxycT5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
ترامپ: آمریکا و ایران قطعاً به نتیجه خواهند رسید؛ به هر طریقی که باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107082" target="_blank">📅 18:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107081">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=INNuUvfiafSKiWbIw0vngbqI_K5XbQDC-Sq6PuWbKODhUipACbdkXor0K-EBsmOpXYZDlRozfUQzp9mt6GDtDX9weMegBwK205SGEHIJSOEulATvPqQWuP-Kb20rDMVjZqtFoveq550WHc9kUE0GFUp_ET86Ngzhyj7l14z5gp86fYyEh1RCbQcOjFWxDHdlFkHdmVmEJ7P4gpmeCvyGgOTu11fXMferCasJUVnKfWQc_ff1yQi68zpdrlIazlPnWtv0UNOuj5R7fcJnyS98I1jmj8HCJI1UDvgCdEX9AL6546g_nAcbIHidVJ1VKW-Mm255q7TNx3SZrOt6hEkf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cae4c2a3d.mp4?token=INNuUvfiafSKiWbIw0vngbqI_K5XbQDC-Sq6PuWbKODhUipACbdkXor0K-EBsmOpXYZDlRozfUQzp9mt6GDtDX9weMegBwK205SGEHIJSOEulATvPqQWuP-Kb20rDMVjZqtFoveq550WHc9kUE0GFUp_ET86Ngzhyj7l14z5gp86fYyEh1RCbQcOjFWxDHdlFkHdmVmEJ7P4gpmeCvyGgOTu11fXMferCasJUVnKfWQc_ff1yQi68zpdrlIazlPnWtv0UNOuj5R7fcJnyS98I1jmj8HCJI1UDvgCdEX9AL6546g_nAcbIHidVJ1VKW-Mm255q7TNx3SZrOt6hEkf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
ترامپ: انتخابات هیچ تأثیری بر تصمیم من درباره ایران ندارد و تنها تمرکز من بر عدم دستیابی این کشور به سلاح هسته‌ای است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107081" target="_blank">📅 18:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107080">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
⭕️
⭕️
ترامپ: باید تصمیم بزرگی بگیرم درباره اینکه آیا می‌خواهم ایران را نابود کنم یا اجازه دهم به حیات و شکوفایی خود ادامه دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107080" target="_blank">📅 18:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107079">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e271237b80.mp4?token=DmCkZtTyAdTRuQT--ms66eXgWooxIRg4MivA4olEXN_MFywlrofUbFkgxolW8LXdn2TG5tJquLslCR3e7SXzkeFfFQoq2eARJ-or61bL5RNVmNJQ-HYg7_mOBWLQbBaS2JtTPsV5VdTJb5wnYpbNKXTMtl15itjjLyU5EpOwybFkBb8DDc1woLPKYbtgvtL_tidlkhTC9CgsfuxpPnxjYliaNEyxmzFgjCdlUzWVTXvOrOfZPRuB68EWuAEeAWUQJmIdL640a1x7F6lP3ZXtkfQUSVk6O3BneAEEFdBZfJcRUS5qPh9NrIo6fjCfijIhmoK6KQK14SGWypsVpZlrNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e271237b80.mp4?token=DmCkZtTyAdTRuQT--ms66eXgWooxIRg4MivA4olEXN_MFywlrofUbFkgxolW8LXdn2TG5tJquLslCR3e7SXzkeFfFQoq2eARJ-or61bL5RNVmNJQ-HYg7_mOBWLQbBaS2JtTPsV5VdTJb5wnYpbNKXTMtl15itjjLyU5EpOwybFkBb8DDc1woLPKYbtgvtL_tidlkhTC9CgsfuxpPnxjYliaNEyxmzFgjCdlUzWVTXvOrOfZPRuB68EWuAEeAWUQJmIdL640a1x7F6lP3ZXtkfQUSVk6O3BneAEEFdBZfJcRUS5qPh9NrIo6fjCfijIhmoK6KQK14SGWypsVpZlrNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
ترامپ: ایران موشکی با قابلیت هدف قرار دادن اروپا ساخته بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107079" target="_blank">📅 18:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107078">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=SCXsAgoaDI2e3qdcUkT4zANZxMPlkwCFtzS_QLqnAeqmLyZpX38e8SQVMYAsoch6fsQwZk5AIF3roUvl5nEEw2Osn9kLMqq48B42F9THLjGeHqKvuEM5HsFZNmBC62WFsZCYrgULyvFgpK-I98YNxiH6sGN43RlmdWMuy9UVK0FsMA8Hu-Cd9rxZvWq04lKSORp4ZowSD3LJpCgDTdhm4-E4bXNAYDMKcgM9ZctBxo0uu3tH1QzKbE_PXM4sFKDRZU_QdgwhC6rbHCDQ2_Y7KTwxz_FKH7vr9XgLHjb1pE4ny3-Y8rzFKKsVKf3nlASyFDkO-p6fqchVBJndpOiwWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/380ee199f8.mp4?token=SCXsAgoaDI2e3qdcUkT4zANZxMPlkwCFtzS_QLqnAeqmLyZpX38e8SQVMYAsoch6fsQwZk5AIF3roUvl5nEEw2Osn9kLMqq48B42F9THLjGeHqKvuEM5HsFZNmBC62WFsZCYrgULyvFgpK-I98YNxiH6sGN43RlmdWMuy9UVK0FsMA8Hu-Cd9rxZvWq04lKSORp4ZowSD3LJpCgDTdhm4-E4bXNAYDMKcgM9ZctBxo0uu3tH1QzKbE_PXM4sFKDRZU_QdgwhC6rbHCDQ2_Y7KTwxz_FKH7vr9XgLHjb1pE4ny3-Y8rzFKKsVKf3nlASyFDkO-p6fqchVBJndpOiwWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
ترامپ در سازمان ملل: به ایران در ازای پایان برنامه هسته‌ای و حمایت از تروریسم، همکاری کامل اقتصادی پیشنهاد دادم؛ اما نپذیرفتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107078" target="_blank">📅 18:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107077">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4439db1dc.mp4?token=BK0fSH-g1Jt-Pw40hy3XKsYiguYgTzbdPBdL_jyn3SN_tHUentSTkju_lsJdpf26bITqzY3E5UMyrvjDU-AWrUuRjZzObJxjEMQIqeU3hJadwTxikFY4oIiF9l0XP64c34mI8Ih6JMI0SXZlrJdKj5WES7n6VXrE_QFlD7UoyJfaXL1BAsDPLxil8QFqkeRIdv1aPGDCXFC2m1VKBJOngrE1KiWaHnygU6IJLqNACKWtdxl8nJOMEKWIBKuBKLw7KkAVOmOaa6ZqHbBwB-hdA71YWXcPacx1f_g3fqr3iv4VGd719eWM1EbhpWd0zyHPcfgYiq9zKQFDJ8aguh_vqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4439db1dc.mp4?token=BK0fSH-g1Jt-Pw40hy3XKsYiguYgTzbdPBdL_jyn3SN_tHUentSTkju_lsJdpf26bITqzY3E5UMyrvjDU-AWrUuRjZzObJxjEMQIqeU3hJadwTxikFY4oIiF9l0XP64c34mI8Ih6JMI0SXZlrJdKj5WES7n6VXrE_QFlD7UoyJfaXL1BAsDPLxil8QFqkeRIdv1aPGDCXFC2m1VKBJOngrE1KiWaHnygU6IJLqNACKWtdxl8nJOMEKWIBKuBKLw7KkAVOmOaa6ZqHbBwB-hdA71YWXcPacx1f_g3fqr3iv4VGd719eWM1EbhpWd0zyHPcfgYiq9zKQFDJ8aguh_vqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
تعریف عجیب علیرضا علیزاده از نوید عاشوری که موجب پاره شدن دوباره عادل شد: گفتم ازدواج نکرده بودی، با هم زندگی می‌کردیم!
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107077" target="_blank">📅 18:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107076">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e179f3429.mp4?token=FsPVF0DODLQhfUuUk3SWSyLyYnips3_X-Hr1QKk3vD3XmOe9K8BBHp2YPG9XpVheGRODUquH3mGjabYHfzL-zl_9ZsbMxbyMkXLOmtNCfZNV6kSrvhdfzs7dQv_c4P1JNE30coHLzJ6khhlQJlH7PWFOYDGqhMt9_wxuNmdDw1Ccetc4nCxM76jq_Ejtz-gxDbtjHLyHBW0SzG24mKpr96V3G4WbV-nO1XCCT0iDYHaahKbxx5JJ4uShS72q79gDpLJBOlIlIBQyFLNKIS--oUVXnSji6RwY0b7dF9O_uZqTNGTsrfy2Z3PQTiHaioRIO41Oq-htuVpPXSoNsagT-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e179f3429.mp4?token=FsPVF0DODLQhfUuUk3SWSyLyYnips3_X-Hr1QKk3vD3XmOe9K8BBHp2YPG9XpVheGRODUquH3mGjabYHfzL-zl_9ZsbMxbyMkXLOmtNCfZNV6kSrvhdfzs7dQv_c4P1JNE30coHLzJ6khhlQJlH7PWFOYDGqhMt9_wxuNmdDw1Ccetc4nCxM76jq_Ejtz-gxDbtjHLyHBW0SzG24mKpr96V3G4WbV-nO1XCCT0iDYHaahKbxx5JJ4uShS72q79gDpLJBOlIlIBQyFLNKIS--oUVXnSji6RwY0b7dF9O_uZqTNGTsrfy2Z3PQTiHaioRIO41Oq-htuVpPXSoNsagT-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعضی‌وقتا آدم فکر میکنه لیونل‌مسی تو زمین فوتبال بیشتر از دوتا چشم داره
😐
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107076" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107075">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107075" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107075" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107074">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbXdsNWAYzs41p9iduL7ZmBlkLm4UGFx2s8VK0AYO0gqNJ-n67jfEXn34NeU6aumiqwRBb5D_-TOtBQcQ2MzixV7D0lfGZOkHxQiOff1mOkadmFGl_mgn_2k5k2m82eL834Fs6ZmMUbriqbNhItSG3ymxWswey-XPRszcaSHzD9qygsjSBgMNnHYUA-ngajxm9aJ8bdrJMR8FYiKS9s1eBICCH904FX9Vo3lo1iatqD54iavgKUFtucTgNYsGMnnwFhhDC30SvOW2fd-OBVTTJsfQAh8AWB9rp9vHHrEMpBueeBr4eQNnbZPnDz9xo8vZeeAj3PFES5hdz0vbl2Uqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مسابقات
UFC Fight Night
شروع شد!
🦖
یک شب پر از مبارزات هیجان‌انگیز، رقابت‌های نزدیک و لحظه‌هایی که نتیجه می‌تونه در چند ثانیه تغییر کنه.
مبارزات رو زنده دنبال کن، عملکرد فایترها رو بررسی کن و پیش‌بینی خودت رو در
TrexBet
ثبت کن.
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107074" target="_blank">📅 17:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107073">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvQTvCy-UGXTdYtVYWQCeh6EnyZOr7KUtYTZ2ntth0nSXh9Ktwi5ajMMiqMndLAS_bqzgt7wR4X_eDcS6uBUk8s_uAgnqzZcjGJhB4P1yDPtpiUzStMJEEqbCfpt6Y2cjdD0vKW-1A0GyyeRjfPk1QXfdcknf8AlKTGrQM2K2tNZdmZoW-rRIJcBJOwk3FL3qsTyuyfNP6ujV5KbGd3wr4KeHYW_i4veVbJOVromlBD-TdOKViGFms5lUPDGYAZal8IgXfaZU_KWpGnxypaon7T1viVa8tE3OaboDQZGVN7-Sei9PLTx-pM1k92aHNRtkUXTl9B7pnAFfRPhHUPCtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇪🇸
لامین یامال :
🔻
به نظرم همون‌طور که می‌گن، توپ طلا جایزه بهترین بازیکن ساله؛ برای بازیکنی که متفاوته، از تماشای بازی کردنش لذت می‌بری و حتی فقط برای دیدن اون بازیکن حاضر می‌شی بری استادیوم. فکر می‌کنم توپ طلا برای همون بازیکن متفاوته؛ ربطی به تعداد گل‌هایی که می‌زنه یا چیزای دیگه نداره.
🔻
وقتی به توپ طلا فکر می‌کنم، یاد مسی، رونالدینیو و بازیکنایی از این دست می‌افتم. اونا متفاوتن و وقتی بازیشون رو می‌بینی، باعث می‌شن لبخند بزنی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107073" target="_blank">📅 17:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107072">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjjS0dshSJIOo3ewQoIK3lTSm0k9dvoKWFPbuIkj5m5HOjqywqTlOu0ZxnaxlFz6nS2g9TICRJmVucgJ6Fh6WDClm5Rx49HPD_T-IDH_fnaIbWvB4dG0_e4u84Mn4o9TAh514NwONk30N_Mo3cuypOJYEAePeIemkO_iTT6hiBJhMCBlcpUJnOQPEDpoXD__sUZ4Gt9laZ4oETcaS8WI6gKrFUJ4zh0_TmpOkRRFlNNnSXPmWgJ3wQvIWcD8bxhTyH3eUb1phV_igbD0VsY4B08gvXl0THt8nvCsG1N2CZRXbk9ln2y1a5KgCG_gJunqOohAyScIBYWJDFETMSsPog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
قرارداد جدید آرسنال با آرتتا بزودی امضا میشه و این سرمربی به مدت طولانی قراردادش رو تمدید میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107072" target="_blank">📅 17:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107071">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ec90abeb5.mp4?token=GZ58PbUlv6UOPBqhEPuUd9msx_MLIdG7vRnD057r_1Tr0gdsfwsd0v02bmJ-Ou-Bf1xdgXR9Do88LW6OahqU05d9Q83PnlOpd1yuy64u3WQc9L5IiifVTmGXDFlWbsIkuoTKz_YU8RODoICGrv_luYRUcCpFIWRv6WI24F0oJ--RHnBZzixIlS2mHsK7HP0bIs7YWb79LbtRu_PJmd7_bdAbXIILklsRtwKcS8spr93Zbg-d41kKVpE3xKjF992Dg9tO0VYsZ5O9HyP6-K4oVzIugwDptYoTrLGqSgVIhsmDyBgX6XBIaDlwDlQSoZTt77HlVFSlX7zIPlOMQyFPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ec90abeb5.mp4?token=GZ58PbUlv6UOPBqhEPuUd9msx_MLIdG7vRnD057r_1Tr0gdsfwsd0v02bmJ-Ou-Bf1xdgXR9Do88LW6OahqU05d9Q83PnlOpd1yuy64u3WQc9L5IiifVTmGXDFlWbsIkuoTKz_YU8RODoICGrv_luYRUcCpFIWRv6WI24F0oJ--RHnBZzixIlS2mHsK7HP0bIs7YWb79LbtRu_PJmd7_bdAbXIILklsRtwKcS8spr93Zbg-d41kKVpE3xKjF992Dg9tO0VYsZ5O9HyP6-K4oVzIugwDptYoTrLGqSgVIhsmDyBgX6XBIaDlwDlQSoZTt77HlVFSlX7zIPlOMQyFPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارلتو، نشون بده یه مادریدیستای واقعی هستی.
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107071" target="_blank">📅 16:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107070">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9DIUVW5ZAcJe4nctCdvkT2ikBH20rz0WkkTbmi37YDi_ESPpl5kbAP1DuHsJlDYm6Jy7bsI2h5hJazrjdx01SO0xMhdAmGq6YzPNDz7XRFng-WY0UBXPQpkhmoSI571vIhCJ4IUTtcCh5SBGfXEwYdEdaoBt3Vu_wjMeqfhO2wU2bPqqstcOmzYY4t7cyWfMmd5Z397-YNZKeWKAUQ7a8ZejiObUCAUm1gNYiLkO6yrcLTK8W3CH5nQ8SwnjnNyM76-io90k-W1g-YSXQw_wdqSgt6WTHzTiP_lCjHob--qjnd4eAH2H3UK40l-cl0KSbW3VT6dFPWo9lCmKIfI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
سهراب بختیاری‌زاده برای نیم‌فصل خواهان جذب یک‌مهاجم خارجی، یک وینگر چپ خارجی و تلاش برای جذب محمد جواد حسین‌نژاد شده است. از سویی بازگشت خلیفه و گودرزی نیز جزو برنامه‌های بختیاری‌زاده در اعلام به تاجرنیا بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107070" target="_blank">📅 16:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107068">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsRslc9RyYkUCsyVjAGgRXDeTIYNqIcrEUA_O4s_geJLX2DFga3oucjt70xJgDbbkqNukWzr7xW42eZVXj_TW0F8AjD3QJQI81-IQ8yfSVFVSnvvpFuS-HiRbFh9L0tZO1eUNXlTcQGLr7gkNk-d9kHMGLbaNtzO8ZfihDZHA4H1trFFsHn_6rdGq79inC5rYKOouxvF6tEFH14dWHV2S9skiNOBm2LcV9tSSMjXyzh1x9TIJGBCU8VwGQX1hjZCrz5pTrhEcyUwEH1_pl_Cf0vVbv1rk2m75RWvj5RT6v9KGCTIB3Y72XOoO33JeAwxwmQFdABJrc-DOvMSa3J4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
اوج تلاش خداداد عزیزی برای درخواست بخشش از مردم بابت وویس زشتش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107068" target="_blank">📅 16:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107067">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGA50mKYhyLCrUrmveJO80v0JF94NS4pN8R5gzCDlIQe2FT5lPlwDr3HgVMcSrGQE46jIySSR02N2wfatXo9ae8WfaO1h1Ex2D7jrBNTm-mRz5dzaiO5iRO-CVjV6AkTEl6V-CVEhYlRb7xX1w_-7W62nIVtLofhSmPautmZZaw-ytYjT2rOxtyXT7rreqj1jivKL1zBKm0cQ0ewo1WAL0uPJjavgCUQayoEFM1Aqisq9HV9BLnCqViuHN4JPyPxMYG2rgBLePHqwvNGFde0reifu8oXgOTre_motEy2P3oNXpQkVdzKO7oI352007lNR6qDGzEr6Oq52QUiJ_z4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عملکرد فوق‌العاده موناکو زیر دست فلیپه‌لوئیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107067" target="_blank">📅 16:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107066">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejWLkTb-fSAaBlH-QCuB9CVrIdKlJSZSlYLl7xF7qAiz51YfXL4iCnyDSThT4VWz0ujofc0hRbPo-Pj3ATJsXC4lFa1sPAsyl_QL0mpf3JPaWVm3yxREH33bryE5O6i6uelWGPyxhFw-YGfUePFsnU9-fLHN-4-Rx8_Ue1SyqoBsoMGCi9bxSWh6dwrJXkWd-Bq8_pVlFgKpnfA6IadVrGs7rhYv067vCgKERzHyKgjiZg1H_17Ng_2sPkbXMG8w3-ZgKprfbpG3WhIINZZRhXW72QnH_c8K_bo_JbCuorv_G1DoVCNf4emuuufF21sMXPwMaO1PKeYwjQ6Qkk5zKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهار
تیم با ۱۰۰ درصد برد اروپا تا پیش‌از فیفادی جاری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107066" target="_blank">📅 15:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107065">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_xtuGzSphCfLRbP4QuyWRhjObdm43cMVPcG7zk2pDbARgDySrf-I7m6D1vGHkKTw7KkrHgshCbB04pzPkFfMPD9m5_J-3BuWMELNsDLZj_QAyHOxNSqfmPfUr_ew_9vwqgKOGUEjabIMekRfoMZihnXsKbzOX9PmSaoKt5S5rQO9hz9ylzseYvk74n0-6PLv62RSIB7kAMGFh79cYTZ17gYhL6KsgjqWdLD8AC0otyLxHZwR9UNazMH49q5r9APl2_89rDwjx-N2ny335HO9zJEiz3PTd0m_SZkl13SBuhZX_GgZJGsQeOHKhb9DABDgKYQI_2BmZ8w6PizuWNWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⭕️
عربستان و چند کشور خاورمیانه در آستانه جام ملتهای آسیا با فشار به فیفا به دنبال تعلیق فوتبال ایران هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107065" target="_blank">📅 15:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107064">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74cce70e5a.mp4?token=itsRfMWXP9X8O8HnDzXobvtWUdlKSTgS6LErx1XigfU0TBH6-uyo_90kTnSJDw8GPfJL_nB3p4yUJqkILgUBUwd4Ge_iZqs8CAFtK0BPVkEx4c09F9qO9CiptgIaavNDMZHBTXbDPydsWGwZHRD5ZGrKQPraBuX44BEu5k2Nl4a-1Rk3oEQ9FxkxHhqbOIzviwbxxFXWEMnMXz7M84NGdBxacrDlUZRqxFZgEXxMSY9RDTs-6sL1D9_l6xs9FNSDwKnCFHM_-thk5Akr4VmU2h-7XElaFarFzcHmiNX3Kn3yjVP0P1SqRpeb8KpG8hjY15AsJw4MZfPbJiky0343Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74cce70e5a.mp4?token=itsRfMWXP9X8O8HnDzXobvtWUdlKSTgS6LErx1XigfU0TBH6-uyo_90kTnSJDw8GPfJL_nB3p4yUJqkILgUBUwd4Ge_iZqs8CAFtK0BPVkEx4c09F9qO9CiptgIaavNDMZHBTXbDPydsWGwZHRD5ZGrKQPraBuX44BEu5k2Nl4a-1Rk3oEQ9FxkxHhqbOIzviwbxxFXWEMnMXz7M84NGdBxacrDlUZRqxFZgEXxMSY9RDTs-6sL1D9_l6xs9FNSDwKnCFHM_-thk5Akr4VmU2h-7XElaFarFzcHmiNX3Kn3yjVP0P1SqRpeb8KpG8hjY15AsJw4MZfPbJiky0343Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
مرور هفته‌عجیب فوتبال در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107064" target="_blank">📅 14:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107063">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1af88a540.mp4?token=TTph6eWjpYjAT43dPx04vTfHA0hIYEi4w0eUU3qKsRjxdiDGyBFI6djDYUUleEFtsozt3cXdZChhS1YgGZqoxNpoeiuD-bUoC2_ud1oOIjeAi9VKGfYIQ1dZe9qzD124X40mybIl0wT1_PaaxKRLwyleQ0WcXNma9_4UjOtstYHAbXRicPWTfIR5RNn4FJ-82-pV1cabX2hNJTEhGbFP4oRBGl2KcNcFKrIW-oeTsTwaT-gTMux-pCfpCZPaAN_XNq9nDUWZiVkJ-VyJT55WGtLFNi37nTrZ2pVgsT41nYla3dbYYPHbAQD-T3FpsFdJFSt9_8BSDzGXRY7ELVVbTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1af88a540.mp4?token=TTph6eWjpYjAT43dPx04vTfHA0hIYEi4w0eUU3qKsRjxdiDGyBFI6djDYUUleEFtsozt3cXdZChhS1YgGZqoxNpoeiuD-bUoC2_ud1oOIjeAi9VKGfYIQ1dZe9qzD124X40mybIl0wT1_PaaxKRLwyleQ0WcXNma9_4UjOtstYHAbXRicPWTfIR5RNn4FJ-82-pV1cabX2hNJTEhGbFP4oRBGl2KcNcFKrIW-oeTsTwaT-gTMux-pCfpCZPaAN_XNq9nDUWZiVkJ-VyJT55WGtLFNi37nTrZ2pVgsT41nYla3dbYYPHbAQD-T3FpsFdJFSt9_8BSDzGXRY7ELVVbTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😏
🇪🇸
پست‌سمی تیم رئال‌بتیس از جدول لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107063" target="_blank">📅 14:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107062">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/068efa824d.mp4?token=GwPuKiL2pwf0EcasZo-5GxNGfJTLwZv-ehXnCrx28czI8AFpq4och-NXbMcTRQ2KW0fc3BM7Lp37h4u5P7rc6CKT9J7jhvsbXbx8lwtqlbVvwXXuEFlZ4LLGRAfR4SRxjjVPa2K_MHhs9cQy81nHE3xxbgJqG_7CfYOEu4sPekD-N7F9wpDqFYwfTPluvHL5CbW-5JxJEblYHwKWca0fB_D4C1NDWurXX1YqrDM6AeWovHklcZV1icPh5KPKMRd0QekSzw9a3jJAVXP5RAZW1LbQ1VWbnL7kwrAxIY-eZf72hnr82nh7GGXW3mgw1kHk88Bggwb-gfn5qwVGF-Yn1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/068efa824d.mp4?token=GwPuKiL2pwf0EcasZo-5GxNGfJTLwZv-ehXnCrx28czI8AFpq4och-NXbMcTRQ2KW0fc3BM7Lp37h4u5P7rc6CKT9J7jhvsbXbx8lwtqlbVvwXXuEFlZ4LLGRAfR4SRxjjVPa2K_MHhs9cQy81nHE3xxbgJqG_7CfYOEu4sPekD-N7F9wpDqFYwfTPluvHL5CbW-5JxJEblYHwKWca0fB_D4C1NDWurXX1YqrDM6AeWovHklcZV1icPh5KPKMRd0QekSzw9a3jJAVXP5RAZW1LbQ1VWbnL7kwrAxIY-eZf72hnr82nh7GGXW3mgw1kHk88Bggwb-gfn5qwVGF-Yn1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇮🇷
🇮🇷
شوخی ابوطالب‌حسینی با عدم قهرمانی پرسپولیس در آسیا و ناکامی‌های استقلال در دربی به سبک هوادار مشهور منچستریونایتد
😆
😆
😆
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107062" target="_blank">📅 14:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107061">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/709cbff54e.mp4?token=GAQUvtrGGTCsrJFUXyakzZhU9L2qcpGdlU6tZiGRu9k5EA0cQXHPGiMKWJs2Pm3h--BkzlDMHIdJiGWB6f8VlCKRZp4SDajZwJ4yS-2Tgd8JFrpbwKmrixhjgNBPC9K9DiV4Ox40fTwlV4B9TThglqBfLXFk8CGyZS_0-Om6NxPuAIlmUqHgIvVgqPhJUX1ei4vqiP8iewq2L2b7sAWyy_CBsscwrRDy0oRWfphoGG6MZWXoUdZ3dcMGRESRfKqO0R2WE67QRjDQ0t8W2sB68pyA5I33sCQRvz6BMA-Fr-KHRyuBXUvqEBmkvbV8BkG6_Pohvb-4py_Kwf9w3nKP-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/709cbff54e.mp4?token=GAQUvtrGGTCsrJFUXyakzZhU9L2qcpGdlU6tZiGRu9k5EA0cQXHPGiMKWJs2Pm3h--BkzlDMHIdJiGWB6f8VlCKRZp4SDajZwJ4yS-2Tgd8JFrpbwKmrixhjgNBPC9K9DiV4Ox40fTwlV4B9TThglqBfLXFk8CGyZS_0-Om6NxPuAIlmUqHgIvVgqPhJUX1ei4vqiP8iewq2L2b7sAWyy_CBsscwrRDy0oRWfphoGG6MZWXoUdZ3dcMGRESRfKqO0R2WE67QRjDQ0t8W2sB68pyA5I33sCQRvz6BMA-Fr-KHRyuBXUvqEBmkvbV8BkG6_Pohvb-4py_Kwf9w3nKP-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇳
🇸🇳
سادیو مانه با حضور در زادگاهش در کشور سنگال، مبلغ ۲۰ میلیون دلار را برای احداث یک پروژه با اشتغال‌زایی بیش از هزار نفر، سرمایه‌گذاری خواهد کرد. مانه اعلام کرده که بیشتر دستمزدش در دوران فوتبال را صرف رشد منطقه محروم خودش در سنگال خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107061" target="_blank">📅 13:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107060">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548065ddaf.mp4?token=uAZtXj1j8OFep7NnPWp7KFXu21NEsZHhhfsYG9r6MiRSb-5naH21ten-ilGCjEGNW4k-_gbE-PvUPuBwoSdpl7ORs8GGqi5SHTm74qkjSRyBONtseW8muW6ldpmXDOHC57YSOoSVm8J3j6aY8_Ou3ahNczTMSiNdycwHYuqNRi0BTxMYzYHz84GqTQRmWgq5afmYsdgScIbDVSVf6uV0XaR6aU3JARe2x-Pd33LJ3B8I9eqALa_nQK8vjBK6IspSbEl7hyECKb-99ny8-zn7dV15rIKvHUGui-__wJFL7ok8L3efHrIuARN7S3BKO0Rru4o6IoWzexMvsTNVF2QWow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548065ddaf.mp4?token=uAZtXj1j8OFep7NnPWp7KFXu21NEsZHhhfsYG9r6MiRSb-5naH21ten-ilGCjEGNW4k-_gbE-PvUPuBwoSdpl7ORs8GGqi5SHTm74qkjSRyBONtseW8muW6ldpmXDOHC57YSOoSVm8J3j6aY8_Ou3ahNczTMSiNdycwHYuqNRi0BTxMYzYHz84GqTQRmWgq5afmYsdgScIbDVSVf6uV0XaR6aU3JARe2x-Pd33LJ3B8I9eqALa_nQK8vjBK6IspSbEl7hyECKb-99ny8-zn7dV15rIKvHUGui-__wJFL7ok8L3efHrIuARN7S3BKO0Rru4o6IoWzexMvsTNVF2QWow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
علت جدایی ابوطالب از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107060" target="_blank">📅 13:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107059">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38289f78f.mp4?token=geuVu5Hp5hu08gf0wWmGyFSuGwvxvxj6oLjOoC83QSLEyChoE6w8tgddIeQ7vt6UYD0lAxZnoohQIYKqrw7QfLKLZGF-VKlGsp2RXfRkFe8SL5Lv_XOqThhQTmWZ3xhAg-QIohxaVyBUA_u8b8ZBO_pWxgOSa8t1dk85ibFyIDaI2x4-B1NfKaBeEI8bXlLjgMozvv2yt32aY19DjkDLYscioZre0ivqkUkqqXRBvkl3Zmzf0n_SDhxfr2x6CGVFtdAS7HAbdx2bTv0t8B5lSRf-iTvTxmybwQ9pw1yTMj5oCkkAPdM3vF1cg-9FXK-ZIuFk3FwQtituJANC-1lxKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38289f78f.mp4?token=geuVu5Hp5hu08gf0wWmGyFSuGwvxvxj6oLjOoC83QSLEyChoE6w8tgddIeQ7vt6UYD0lAxZnoohQIYKqrw7QfLKLZGF-VKlGsp2RXfRkFe8SL5Lv_XOqThhQTmWZ3xhAg-QIohxaVyBUA_u8b8ZBO_pWxgOSa8t1dk85ibFyIDaI2x4-B1NfKaBeEI8bXlLjgMozvv2yt32aY19DjkDLYscioZre0ivqkUkqqXRBvkl3Zmzf0n_SDhxfr2x6CGVFtdAS7HAbdx2bTv0t8B5lSRf-iTvTxmybwQ9pw1yTMj5oCkkAPdM3vF1cg-9FXK-ZIuFk3FwQtituJANC-1lxKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
‼️
دیس سنگین ابوطالب به خداداد عزیزی: قلب آدم صاف باشه نه پاهاش، شما قلبت پرانتزیه آقای خداداد عزیزی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107059" target="_blank">📅 13:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107058">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19fc9edd61.mp4?token=ISpFFIMYbViJLYWw2VHLJ7Y3rBms54dkCFMqJEbZbZ8VyVx9IH2iym8nX6E1JjuoXvpcLA-iHl7ImUM_ff0yYYEUKxdBWYPEmAp5Zb7Dolz0hNB4JwDzd_KnKwiwnHQhGm21J_jD5aLD40D1iyUte_dtXczRR_aNY5yVxZQ_mHeRv8vyPWiRpnNF9EeuBbewIBEBNJZsW2NH5jr-Dbb-wacJw9ECqAXlrTu_1vtLBtkftYwo6I_fNOiHMFAx8dFZo_lePe7V3YzB6JKokYo0AgVfrvd1yTJ3yFLI0HdWjCB3I1XhliQXU3LyTW6k6ILrW4R1IK_XcP6pzzMD1Su45A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19fc9edd61.mp4?token=ISpFFIMYbViJLYWw2VHLJ7Y3rBms54dkCFMqJEbZbZ8VyVx9IH2iym8nX6E1JjuoXvpcLA-iHl7ImUM_ff0yYYEUKxdBWYPEmAp5Zb7Dolz0hNB4JwDzd_KnKwiwnHQhGm21J_jD5aLD40D1iyUte_dtXczRR_aNY5yVxZQ_mHeRv8vyPWiRpnNF9EeuBbewIBEBNJZsW2NH5jr-Dbb-wacJw9ECqAXlrTu_1vtLBtkftYwo6I_fNOiHMFAx8dFZo_lePe7V3YzB6JKokYo0AgVfrvd1yTJ3yFLI0HdWjCB3I1XhliQXU3LyTW6k6ILrW4R1IK_XcP6pzzMD1Su45A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
‼️
ابوطالب حسینی ویس لو رفته خداداد عزیزی رو مودبانه ترجمه کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107058" target="_blank">📅 12:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107057">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSfqR-qm1TCD3Za_xF1CSr-tmPVxNubDaYl6q4Ma1oe7ynbYK23O864WVL2CJR7STrjDoz3RF4oxJ_KrP5AwpBxGFS9EAgNBSiUkHlvYU2muvpdj1rvRt6QpyAzai7pRRVMpaTOXRjNBL3lYljwcueq2p2TsqwXd1WTuxkrAXgEk6S-5qWudTk2oVojFcmM7gKk8P46kLmsb_Q6JC5qfPtVRT7UnsX5_ez1bQ1Ih44dqZkaIN05mcjuiXjJdwK6Q6MYZFW0qCbKAoJKu4O7x32j9rLRAVJgu5PbgdhvfBejhocSq9FxsGVYLmJdTAuF__pgICFHeQmVpuOxKDaoxJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای ابوالفضل جلالی فکر کرده در عصر قاجاریه داریم زندگی می‌کنیم. چطور اینقدر راحت دروغ میگن
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107057" target="_blank">📅 12:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107056">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaugvFhmfhBNAln79dcsDDCHjOHAgEPflqcNXWnDyYcDIjtY8IWSSWDFrwfGk8gp2fmy4mG6bNMF_8ZFnJ-jQD9GkRCEPNFWc5yo5EqjAMXO_V140e6njqSwpM3TW33gPstW4sKJ3rFOWW3EdyDqNj57dWXJqsAPYUbnUFRUOX7J_Wp51qt1pOx2qS5E8VgCiQlDP77bbgFvjnzv5dmijM8A0wRkAiag65AtSkI5rUS-U7lRKz1e8eynH3L-kiceVkdKIgMDTOdRt6Mmm84qoYLznu4ENp-CSRSx_iBZPgDhLEf4W0PxtFSyzwhDrCqYE3x8eLtQHSkLsuQlJmZvvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جمع سن سه نفر جلو: 110 سال
احتمال فیکس شدن هر سه بازیکن تو جام ملتهای آسیا هم زیاده. جوان‌گرایی بی‌نظیر امیر قلعه نویی بعد از سال چهارم مربیگریش در تیم ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107056" target="_blank">📅 12:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107055">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa420985a.mp4?token=ludgA6wa7evU6ryCvqefFdy5flYSaVYPqx41xe_yS1t68khj_m6zeIlTDdORegHMpDezsq5DB8sdrVl_VZkZr1e_Lg3i3onWxDmWFNOqm_06FJeP2Tu1oPs9qPVFIDjrTXmGrrrjRs8aFsUC9DGbN_DotAuFOW_KyeYKVtCTW-Aeg6pWDXrErOcoJlrrg-saYSxHJn5hm3rjH3_X4EJqgYpyej_2tlisEc1yERTZojlkFxKvBltR2rQMDzOtkMvuIG3SVtSGpBLXXAjwkjfC92rHQTB3oItjB4-MWQx7CtxaqwV2rFSYbk0zDxGTScmoHa0X9yQqB4qiUBz5fA2UWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa420985a.mp4?token=ludgA6wa7evU6ryCvqefFdy5flYSaVYPqx41xe_yS1t68khj_m6zeIlTDdORegHMpDezsq5DB8sdrVl_VZkZr1e_Lg3i3onWxDmWFNOqm_06FJeP2Tu1oPs9qPVFIDjrTXmGrrrjRs8aFsUC9DGbN_DotAuFOW_KyeYKVtCTW-Aeg6pWDXrErOcoJlrrg-saYSxHJn5hm3rjH3_X4EJqgYpyej_2tlisEc1yERTZojlkFxKvBltR2rQMDzOtkMvuIG3SVtSGpBLXXAjwkjfC92rHQTB3oItjB4-MWQx7CtxaqwV2rFSYbk0zDxGTScmoHa0X9yQqB4qiUBz5fA2UWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما هم از فیفادی بدتون میاد
🙄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107055" target="_blank">📅 11:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107054">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c092ad06d.mp4?token=vy-GtTvJ_WQ-V4AdVZScKywFreCW8m24x-mB_19F_Agnkwnxrw5IClNHOzoWMgEJyk1LLIGYzIc20YBSV6XQYj4_5dnWMXEUZ07i5o0ZM5TKhNYgy9XJRlMXFy95GGV0ib-GX8XLNKplTgM5fg1V_oFpQMW6DnIhw7eEbc5Mv_K6SSW2cvIVjuJjC5ktA1Hs2KM2SCqHhN68pc3geRS2-FlwqSblW0bsfpCeYahT8avMSwUdiR-DN8ST_cTa6QM5FyoX9XJKUIqm1vGlcpvGj3jccVarxjuIwbjy5IkgeGB27t17awCyAlBxVOgxJQVW8C69Av3vFxYgtjuRFkcsMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c092ad06d.mp4?token=vy-GtTvJ_WQ-V4AdVZScKywFreCW8m24x-mB_19F_Agnkwnxrw5IClNHOzoWMgEJyk1LLIGYzIc20YBSV6XQYj4_5dnWMXEUZ07i5o0ZM5TKhNYgy9XJRlMXFy95GGV0ib-GX8XLNKplTgM5fg1V_oFpQMW6DnIhw7eEbc5Mv_K6SSW2cvIVjuJjC5ktA1Hs2KM2SCqHhN68pc3geRS2-FlwqSblW0bsfpCeYahT8avMSwUdiR-DN8ST_cTa6QM5FyoX9XJKUIqm1vGlcpvGj3jccVarxjuIwbjy5IkgeGB27t17awCyAlBxVOgxJQVW8C69Av3vFxYgtjuRFkcsMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇳🇱
اولین تمرین لاله‌های نارنجی زیر نظر ژاوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107054" target="_blank">📅 11:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107053">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107053" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107053" target="_blank">📅 11:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107052">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDpG3LyvPiMS8BTmYPzLSCWMW5OmTcRuR-HzgQgI9Jf1VtSBaqWH99-4Fj2xEfMidMfYqWOHP4qpIpq4JWiV7O-VADpgoTPF9waPbWFqrI11j0mdi0uwkjtVvxK4ili7m6NdyEyl6aPxBKqRPz1nNJkljCeifqSiRSsbUeYOiQm-NnrmVZH8ODvsVZ0PRQfSLXhvcprjDgJWzy84kWzeeV9uOUcF9mUslh-9nTEQtSuGZAnuMmJOK5yCYEnZz00B7LLmFgocCamYW0x8p0uTiy6JSwu_gC3g_fanLK8s_NefrteUQq6azsU0GwzCKMtmDCmZpbfliW5Y-t4m7fPqCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107052" target="_blank">📅 11:39 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107051">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGWlmN4nsdkSp7OBmvgaMosfzB78rncxGrV2JZ3m8rCoFT7Oj5EaVJznRZDzzdvVTTVoyF7DN-G2LYogp-NMbyldqtCWwf2zjRgC5Q9rz7jn5G6P9xfGE5vnmfkV0RWR6kkjGpQ2eI7WBqqfYu9bANSoh4HuC-FuPxm05dncqG-snDY4BGIihwTzCrhzh18tAueb6KZkfgwZhl-AfVZN9iwwU5Y29x49SDmrnxkBBxAQv7X8notkV6TVLSESHha3qFDCNHbYoZl9UpiNMbyj2J6av-5nUyjKNsYi6tO5LAkcBkTe-x32OLltdkdd5CYcIX2z4L2ZAmxSlFoJ8BX7yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
لیونل مسی ۲.۶ میلیون یورو برای کمک به ساخت مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
✅
این مرکز تخصصی سرطان کودکان در بیمارستان سنت خوآن دِ دئو بارسلونا قرار دارد و ظرفیت رسیدگی به حدود ۴۰۰ بیمار در سال را دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107051" target="_blank">📅 11:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107050">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26eae7147.mp4?token=SITUfPk-hHHmKmst3cCn8F5ZbIhtlIKxTfUPJyV2EZFuOdP6rJFHsPM60_R1E-F6LPJYHuh2xDxH6RL59sh-Dk0SscbH7nkX9LeroisvDMpbEniMXXNJ0o4B3B7aXzCAnD8KyiWZIEcJAlFiBBChAEU37eAMjg47ePN6jNX-d6m8OZ7MAMERVI8TwN98UQx41PAHDpOf0PHJbNqy4mcnG85c81pHzVuWhyFr2gI3SZtKh-lKz_Pqqe3i2fajzAUgFXXFSQucR7sksMshCjy8W0OuKU8Gnff-zCqzNWBJOgIRnBhf-hMMf7COJhzUP3M_uZqkss8iXVQUoRFyWIu1bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26eae7147.mp4?token=SITUfPk-hHHmKmst3cCn8F5ZbIhtlIKxTfUPJyV2EZFuOdP6rJFHsPM60_R1E-F6LPJYHuh2xDxH6RL59sh-Dk0SscbH7nkX9LeroisvDMpbEniMXXNJ0o4B3B7aXzCAnD8KyiWZIEcJAlFiBBChAEU37eAMjg47ePN6jNX-d6m8OZ7MAMERVI8TwN98UQx41PAHDpOf0PHJbNqy4mcnG85c81pHzVuWhyFr2gI3SZtKh-lKz_Pqqe3i2fajzAUgFXXFSQucR7sksMshCjy8W0OuKU8Gnff-zCqzNWBJOgIRnBhf-hMMf7COJhzUP3M_uZqkss8iXVQUoRFyWIu1bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
در این ویدیو پیرترین موجود زنده دنیا را مشاهده ‌می‌کنید، کوسه گرینلند که بیش از 390 ساله که در اعماق اقیانوس زندگی میکنه؛ این کوسه زمانی متولد شد که آیزاک نیوتون، موتسارت و چارلز داروین هنوز متولد نشده بودن؛ البته که گالیله 70 ساله و شکسپیر چندین سال قبل از دنیا رفته بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107050" target="_blank">📅 11:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107049">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b6b29a98b.mp4?token=tsRm7S_LwhJLZzWof6zgZJKzrPlC91AKhPfPpnuEmn5d05b1Y1J0YW3VPph31_QshSNfp_m8cU9KbW7qQBadIb3tuUcuos3Q41nCQhWDonRGe0N3xZXIwPAVjcNVn5v9iWxi-gcTyF62ws3ZwPfokQL86i5P71tGkdZmOik5cy4eP7LMM2SvbOwxy1o1ubnZ60SnEZahhl7FJcVtGyp3eMKOsNA6chmPUpr3RK5Eik7l_byq09L27RMNNRO8oiQU5MDdeoYytT--ajofDk99WUCmUoVFhqKtebJEgw_We5DzTg3ctLYcuYTIejEZyWDvas1FpUtS85N5uhIX05PHWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b6b29a98b.mp4?token=tsRm7S_LwhJLZzWof6zgZJKzrPlC91AKhPfPpnuEmn5d05b1Y1J0YW3VPph31_QshSNfp_m8cU9KbW7qQBadIb3tuUcuos3Q41nCQhWDonRGe0N3xZXIwPAVjcNVn5v9iWxi-gcTyF62ws3ZwPfokQL86i5P71tGkdZmOik5cy4eP7LMM2SvbOwxy1o1ubnZ60SnEZahhl7FJcVtGyp3eMKOsNA6chmPUpr3RK5Eik7l_byq09L27RMNNRO8oiQU5MDdeoYytT--ajofDk99WUCmUoVFhqKtebJEgw_We5DzTg3ctLYcuYTIejEZyWDvas1FpUtS85N5uhIX05PHWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاییز با بوی نو کتاب فارسی شروع می‌شه
🍁
✏️
حتی زمان ما، شروع مدرسه ها صفای دیگه ای داشت ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107049" target="_blank">📅 10:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107048">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6ef37fb80.mp4?token=TE6u4M3P3crEEkeFvqBYuFQr0W3oy7IwG0J91wJHAAb5SShBaDJLpa2_ndy5R87uJa_MBSx-ss5jyo09l5VNswYEUsANTRhyIJs4G-3VPhNXLjzoYZCEcqRJLOojAD1wyogti9vyz-jKYCUcvj0eo1690PS7DcJ7_JQogVpHPx3QCfH87y8Q-vwfFMSnifo_qjNTNLcNSMBHAunWWHwYU_0HH7UchQdTiVqYk3VMur6kIXv3kXbzoawnTLOtk4c2c7lgTTSYM-fIJSoNN3OQWjcnDFNWbobYmP4S_gtIqrHIyI2cxCax99MVIugLOIfvskMn-BFD-uamREi-i2gDVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6ef37fb80.mp4?token=TE6u4M3P3crEEkeFvqBYuFQr0W3oy7IwG0J91wJHAAb5SShBaDJLpa2_ndy5R87uJa_MBSx-ss5jyo09l5VNswYEUsANTRhyIJs4G-3VPhNXLjzoYZCEcqRJLOojAD1wyogti9vyz-jKYCUcvj0eo1690PS7DcJ7_JQogVpHPx3QCfH87y8Q-vwfFMSnifo_qjNTNLcNSMBHAunWWHwYU_0HH7UchQdTiVqYk3VMur6kIXv3kXbzoawnTLOtk4c2c7lgTTSYM-fIJSoNN3OQWjcnDFNWbobYmP4S_gtIqrHIyI2cxCax99MVIugLOIfvskMn-BFD-uamREi-i2gDVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای ابوالفضل جلالی فکر کرده در عصر قاجاریه داریم زندگی می‌کنیم. چطور اینقدر راحت دروغ میگن
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107048" target="_blank">📅 10:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107047">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/090ef42156.mp4?token=b28bj7du25_PbKpZHhhN9Fn5yDr326zniOnJMmNMqESyDo_hu4ksI9R3dW6GVXWCAesi2YPbEwEt_WaEPK0sT_8RXSrUU0SxMwDcF28g5IC6tNcODq7e4dkF_NFBYb9-YersFyEZJnlryxIQwGR0y029KhP5359AN5qBnIgoZ3A5aS2rN46Xfwsny4wQRWBi5u5i890cgiuj1dgst-sBx3resdJEQY-lWQ5OaUHEbYaEpIj_JSDATiDGiwYRqCi7ABNUsgI06MERzlB_xUcxJnAUWKlkeUiFXxDCCrrZQgAbnj1gI_1YVrrnYMLhaSfd2Yl53hZFJZaICdFMT2ektg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/090ef42156.mp4?token=b28bj7du25_PbKpZHhhN9Fn5yDr326zniOnJMmNMqESyDo_hu4ksI9R3dW6GVXWCAesi2YPbEwEt_WaEPK0sT_8RXSrUU0SxMwDcF28g5IC6tNcODq7e4dkF_NFBYb9-YersFyEZJnlryxIQwGR0y029KhP5359AN5qBnIgoZ3A5aS2rN46Xfwsny4wQRWBi5u5i890cgiuj1dgst-sBx3resdJEQY-lWQ5OaUHEbYaEpIj_JSDATiDGiwYRqCi7ABNUsgI06MERzlB_xUcxJnAUWKlkeUiFXxDCCrrZQgAbnj1gI_1YVrrnYMLhaSfd2Yl53hZFJZaICdFMT2ektg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
بابک مرادی: مربی داشتیم (کمک فرهاد مجیدی) که آدم بسیار فاسدی بود. همه فوتبالی‌ها میدونن فاسده اما هنوز داره مربیگری می‌کنه
+احتمالا این شخص فراز کمالوند هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107047" target="_blank">📅 09:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107046">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d781ba027e.mp4?token=vkM6Nln1XY7vVln5UJ5RKRsJyj80QT99RXia-Lz8UmAjQWJR2n63R2IEDcNqaOwBqBZJ-RfkBJAi2eC4Ij0YwxkQY3IIeQhaLovV4uP_LB467jLX03IGT__l-2MZ_NiH0_obxtEaAR6o4f63mkPJbBFZmntufbNICn0Ss1zBZim974FMj50RWyXfm9lbvhB2DlV3CVyIZu-vPJ8TqH2_g_tdLIi0ZWY5ZYuhNXFmoqvIe89OSlnExjIfJEssTPV52WOK9QWsJp6SwC-A5qy_4CbZsubGN45LOAcG1wTGG1yWkFoOHR-Xcyd9fpFILnJOM7mJMv14bBclxLa7kmx5Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d781ba027e.mp4?token=vkM6Nln1XY7vVln5UJ5RKRsJyj80QT99RXia-Lz8UmAjQWJR2n63R2IEDcNqaOwBqBZJ-RfkBJAi2eC4Ij0YwxkQY3IIeQhaLovV4uP_LB467jLX03IGT__l-2MZ_NiH0_obxtEaAR6o4f63mkPJbBFZmntufbNICn0Ss1zBZim974FMj50RWyXfm9lbvhB2DlV3CVyIZu-vPJ8TqH2_g_tdLIi0ZWY5ZYuhNXFmoqvIe89OSlnExjIfJEssTPV52WOK9QWsJp6SwC-A5qy_4CbZsubGN45LOAcG1wTGG1yWkFoOHR-Xcyd9fpFILnJOM7mJMv14bBclxLa7kmx5Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
🇮🇷
تعریف و تمجید حمید مطهری سرمربی فولاد خوزستان از سهراب بختیاری زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107046" target="_blank">📅 09:25 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107045">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed15f390e.mp4?token=pcROdTK3S9cEw-It98ylNHzdlHYLoSP611VVycBUdgzj_e59lN4-Q2Ouk_jPZXknl2C5UmPftx9ib60ZQEaOqnfmDI-ee_WqCDn2TIC_Kmt3uq73rmnyczgsK1KsXQIGKNatDgftOIXywr-UQkI4eJZ5h0MvCFEVKi4VY4EspCwJMHV1Fa5kw2bmc00ab_Hgtd4NP4BkpVJ8Qyqfcd4NfQq9toIxSRBW_86pK_hT1dTlMHY_UjsqjYZ2YTjvjmF_WuTt0WxnTtoUxxeTsfY9dj3oOZcXncMPo8JCMKJTfJ_KxRpzjp6MeaFekxo0sX-legFS2HiedGiVjBhvuE3Heg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed15f390e.mp4?token=pcROdTK3S9cEw-It98ylNHzdlHYLoSP611VVycBUdgzj_e59lN4-Q2Ouk_jPZXknl2C5UmPftx9ib60ZQEaOqnfmDI-ee_WqCDn2TIC_Kmt3uq73rmnyczgsK1KsXQIGKNatDgftOIXywr-UQkI4eJZ5h0MvCFEVKi4VY4EspCwJMHV1Fa5kw2bmc00ab_Hgtd4NP4BkpVJ8Qyqfcd4NfQq9toIxSRBW_86pK_hT1dTlMHY_UjsqjYZ2YTjvjmF_WuTt0WxnTtoUxxeTsfY9dj3oOZcXncMPo8JCMKJTfJ_KxRpzjp6MeaFekxo0sX-legFS2HiedGiVjBhvuE3Heg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
فوش ناموسی بلینگهام به مادر داور بازی با اتلتیکو که شکار رسانه‌ها شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107045" target="_blank">📅 09:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107044">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a69b72fb04.mp4?token=bhoO8ccwhcRKdRd8uCfWwejSOKW8K1n4nIAskjy0WeQ6UnBcWVzx7VQX5JYFvF61V0sw339wOoWaFjX3_qTiPNa2BDLJnNAPhqxeOFX68smtRuxY6ptNYm3td5nUbyakQjEdccC-gxyuGTo1-HznoYhgARlVJpDd93y2htwej9VaSP_aYB44XI4Tp2k7jamvRnyoI2Zo6zjIFSuvlXaJH7xUII5TedioEKeYiFr-MtbU2AZPAQ_AH59aWDEUtS4oXrlWaah29u2QA7El7Cxc4Nvmc1Y5OtcfWd6pjp8EWpYmjMRdQfn9B59mdidJRj3aDNOJXh1Dh-t1ooH2rWYrLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a69b72fb04.mp4?token=bhoO8ccwhcRKdRd8uCfWwejSOKW8K1n4nIAskjy0WeQ6UnBcWVzx7VQX5JYFvF61V0sw339wOoWaFjX3_qTiPNa2BDLJnNAPhqxeOFX68smtRuxY6ptNYm3td5nUbyakQjEdccC-gxyuGTo1-HznoYhgARlVJpDd93y2htwej9VaSP_aYB44XI4Tp2k7jamvRnyoI2Zo6zjIFSuvlXaJH7xUII5TedioEKeYiFr-MtbU2AZPAQ_AH59aWDEUtS4oXrlWaah29u2QA7El7Cxc4Nvmc1Y5OtcfWd6pjp8EWpYmjMRdQfn9B59mdidJRj3aDNOJXh1Dh-t1ooH2rWYrLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
شعر خوانی جالب قیاسی:
«مثل رابطه سهراب بختیاری‌زاده و صالح حردانی
مثل حال دروازه‌بان بعد از تک به تک شدن با یاسر آسانی
یا مثل حال اتوبوس تیم ملی بعد از جریان کنعانی»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107044" target="_blank">📅 08:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107041">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32c5c8c60.mp4?token=VISJEiZUfErVXqKRzQk05BCL94UEo8N2TGAej3GkyFtjd5f-FuW7y8pVTbnIQAd-uZAZCvKFhaiUJRjqrk6QydJoBdM6yNe6Uj1pQE6sZtkabyvkuwH_YvztNEqHPO5uZvWBqmRkIIayzqNxKbUUe6c_2NW7RW6l5OodYm1AgzhzDtwZlwie0KAQTm7BOTLna7J04VH_532JAzSujjMM3j_gScw4Ty9cNCiO43mSxFCMh4wa_B0D27O9Wp5czrL2GB3GojYU64I_XxwcF5-qPvEhR4XSzrIA4O-lopg47ekTr_oaF24LSRutjZvTe08G-xC90IQOj2yl5S2o2TbrnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32c5c8c60.mp4?token=VISJEiZUfErVXqKRzQk05BCL94UEo8N2TGAej3GkyFtjd5f-FuW7y8pVTbnIQAd-uZAZCvKFhaiUJRjqrk6QydJoBdM6yNe6Uj1pQE6sZtkabyvkuwH_YvztNEqHPO5uZvWBqmRkIIayzqNxKbUUe6c_2NW7RW6l5OodYm1AgzhzDtwZlwie0KAQTm7BOTLna7J04VH_532JAzSujjMM3j_gScw4Ty9cNCiO43mSxFCMh4wa_B0D27O9Wp5czrL2GB3GojYU64I_XxwcF5-qPvEhR4XSzrIA4O-lopg47ekTr_oaF24LSRutjZvTe08G-xC90IQOj2yl5S2o2TbrnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🐐
🇦🇷
رونمایی‌رسمی لیونل‌مسی از پیراهن ویژه خودش در آخرین بازی ملی با آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107041" target="_blank">📅 00:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107040">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b37185041.mp4?token=ZR6T5feNYyvKysqDa4XkVfKd1Z-UsX4HIbx927fKut_5UVuFDXFt8VXJ5kEZDuMSygZ42i03_8_CZjb9WOBvs2PmGecF4lkUWYSRL2PGNZYQWUnQ-i-eRCZhpacF-E4qD6Ff2fkM-KF7LUDzT2AOwYmfMLWFsTydOV8gjr5ZGcsFFEYi9wRUESc8sarDe2YksXH33O4oIZhUpf7HEQvO1WEO9V_Wo9SaD8eGwBPAEeYX_k0Nvt3l8dZnvct0dVO4lhmMgQHTJHZb_HRC9npixME4tDLZj_ta2XOvGDTt5ymKfKRxpTJBf8BT16ffIWCa7jvdGz9PARCl0F7GdyC-ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b37185041.mp4?token=ZR6T5feNYyvKysqDa4XkVfKd1Z-UsX4HIbx927fKut_5UVuFDXFt8VXJ5kEZDuMSygZ42i03_8_CZjb9WOBvs2PmGecF4lkUWYSRL2PGNZYQWUnQ-i-eRCZhpacF-E4qD6Ff2fkM-KF7LUDzT2AOwYmfMLWFsTydOV8gjr5ZGcsFFEYi9wRUESc8sarDe2YksXH33O4oIZhUpf7HEQvO1WEO9V_Wo9SaD8eGwBPAEeYX_k0Nvt3l8dZnvct0dVO4lhmMgQHTJHZb_HRC9npixME4tDLZj_ta2XOvGDTt5ymKfKRxpTJBf8BT16ffIWCa7jvdGz9PARCl0F7GdyC-ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام علیرضا بیرانوند به میثاقی روی آنتن زنده: اگر نظام وظیفه اعلام کند من چه زمانی باید به سربازی بروم به جان 2 تا بچه ام فردا می روم سربازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/107040" target="_blank">📅 00:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107038">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EXWENM7ZhtgeuMXpyV0qF5xaJU8hRPZ6aonO4nxtd-dtlzMS9rAwtW-GxRyv13kaRfOuglTvtVs7-7wcWMdLNDUPN0XCY6-_VlqVPi4x5fsp5UXOg1J-N3AANlkHWEQwKKoUSW9o3HZYA8S4m_3J3L4wXpngQyIoFxNQespvJxMBxj8QlWmBMrXVCRP-EXU1hoaWDi4KT6QwnCFP-E_NxMQVKeg8RFFz0RYCLo3YQXO7i-1KEZNtM4Ab-9XyQrDV7jnF6AN6I4FgTdBv70yifOYUzn4HH0Quiw9nqkh9ZKbC6YCkao9jFMSh2NwAIfXlIv-wH9uPEXIciSeyNS9GCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GBeRAsHZ7jmnNZ9mVG2gBAoplGNis2XvXkcBduPoqDrM4uBNPIMY_5sLCm8BYu8qnm7YURsSnabdJrSPE4m--OOMdZu7I5kO7P86j54aS5reuBBLfOUclNiyEFB8nxj5TuIChR0aJXR8S-VlWFKjzNeEDOZii9DI3Ujr34Wib0FVGkCzl0lfl2zjg2Y_xiCtzQxgHBO-72AcT3-jRqCpleD2org7Exf7lBm3dood_HqcyKlCeRJUEH9u4OBsC_k0R54rahwdgs1QjMcuHU1RZh_60cKMafUZ0eUH5ld_SyJ2aMA3CQEQ9SMcFkl6Wc9tbtH3sHxKC0H54aZxAI8WAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
❌
دلیل عدم دعوت اللهیار صیادمنش انتشار این استوری در ایام اعتراضات سراسری دی‌ماه ۱۴۰۴ است که باعث شده حداقل تا چند سال قید حضور در تیم‌ملی را بزند مگر اینکه به مانند سردار آزمون دست به پاچه‌خواری بزند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/107038" target="_blank">📅 00:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107037">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
⭕️
‼️
اللهیار صیادمنش: در اردوها به بازیکن احترام نمی‌گذاشتند. حرف‌هایی که جوان‌ها نمی‌توانند بزنند را می‌گویم. در این چهار سال ۱۰ بازی دوستانه روی نیمکت بودم، ۲۰ دقیقه هم بازی نکردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/107037" target="_blank">📅 00:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107036">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
⭕️
🎙
اللهیار صیادمنش: تا این افراد در تیم‌ملی باشند حتی اگر بخواهند هم دیگر برایشان بازی نمی‌کنم. در اردوهایی که زیر دست این آقا(قلعه‌نویی) دعوت شدم هم چیزی به من اضافه نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/107036" target="_blank">📅 00:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107035">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
⭕️
‼️
🎙
گلایه تند اللهیار صیادمنش بابت ربط‌دادن عدم دعوت به تیم ملی، به مسائل اخلاقی: می‌دانستم قلعه‌نویی هیچ اعتقادی به من ندارد چون اصلا هیچ مسابقه‌ای را از لژیونرها نمی‌بیند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/107035" target="_blank">📅 00:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107034">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcYN6ZMIzcHwkmoe79VoZH820j3AubNIGfttKIwK2eJSG9NtbSnvX6JB1XDkgkohtVh_QQ3M9GOp3rcidBfrYCX2Yx9Lm96-oMTyGaHwxJdCue7O-f4aVZOhOhPliXnb8DZelGtFVf79Qkosm4pvW2Ic9SPZi_XBxoP1ss_qhgoyKU6tmInfs1J88BlVy2bvFAOY3h8gnWbmuKZyPUDJvtw-zJNi9K0GECfCkRR1wCAezLr0IMLJ2z1jPZK6D_m3u73T_MGO9UGXj-UnLmyG1DhUBXuPGPkZHln3M1pEYMCikcVekD0EPFbzuZUlPYnd4ghGKZ8OcAkyIXE7Dw2MZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
خاویر‌تباس رئیس لالیگا:
🔹
باخت دیروز رئال مقابل اتلتیکو صرفا جنبه فنی داشت. درست است که اخراج یک بازیکن حریف نادیده گرفته شد اما اینها بهانه خوبی برای باختن نیست. امیدواریم رئال‌مادرید واقعیت تیمش را ببیند و دست از جنجال بردارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107034" target="_blank">📅 00:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107033">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8238d2e025.mp4?token=M9cSLq3iAqB-wwMjLSgXNpgQI1yYy6VskKxelyIjutkJ_e_VYPmEI2VSXnGMDlC91E7vOwzzLmfa_GlPqFUNuAD5J0qJjQS02uxQRHUyVRFtoSjlPelHjshcTtWiD2J7D-kkjym1OSiu0bqW3RAvLMAh63sPIEvwnN2WlruyzHWJ2zA4FnpyC5B_KzOArvEX4wNa_hfSwUFCvFmN3RHen1KRowGPgSLHsP41KMDu53XaIXP3puV4jM46J_84N3UOl1TawT0sdf27xIzpJCVrLUX33A9VsgbxZ51BoWE9t6_7Ovob_iUM5kHsXnhcVWLShc_qCahRaRz2LeWijSqIOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8238d2e025.mp4?token=M9cSLq3iAqB-wwMjLSgXNpgQI1yYy6VskKxelyIjutkJ_e_VYPmEI2VSXnGMDlC91E7vOwzzLmfa_GlPqFUNuAD5J0qJjQS02uxQRHUyVRFtoSjlPelHjshcTtWiD2J7D-kkjym1OSiu0bqW3RAvLMAh63sPIEvwnN2WlruyzHWJ2zA4FnpyC5B_KzOArvEX4wNa_hfSwUFCvFmN3RHen1KRowGPgSLHsP41KMDu53XaIXP3puV4jM46J_84N3UOl1TawT0sdf27xIzpJCVrLUX33A9VsgbxZ51BoWE9t6_7Ovob_iUM5kHsXnhcVWLShc_qCahRaRz2LeWijSqIOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
میثاقی: اردوی تیم ملی تمام شود سربازی علیرضا بیرانوند تعین تکلیف می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107033" target="_blank">📅 23:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107032">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e4355f95.mp4?token=WLzDifixhaU59MWeca6OIr1wSfC_Bd6SjRu2YdCHkbk0pF8hqiUs4jSWU4BxwjtRX88uwD_F--HNmHnVkN_ZWm7wCnw5ZCiRIDB_wTeQjGasvTt9tr3HrmFkUMlLl5qtSyNUH4EXprYUAYCJxP5RCl2wAWGRnPw9NXtMq-XO3SKTlwSkuToq_5mnLbqa3yjByj8LPURXS71K31ZHJpElXh9BSK3DisRoiSKEtDV9EFkBGG1UudURBLUurUkKxKJ25vcqmQk4An6BUSkUhJg72uJiv6kfFqajSdnZaExLG6D-YSiFN2psQhSP6ddS8Rq2xXzg7ngIsz4rgYz4U_8vWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e4355f95.mp4?token=WLzDifixhaU59MWeca6OIr1wSfC_Bd6SjRu2YdCHkbk0pF8hqiUs4jSWU4BxwjtRX88uwD_F--HNmHnVkN_ZWm7wCnw5ZCiRIDB_wTeQjGasvTt9tr3HrmFkUMlLl5qtSyNUH4EXprYUAYCJxP5RCl2wAWGRnPw9NXtMq-XO3SKTlwSkuToq_5mnLbqa3yjByj8LPURXS71K31ZHJpElXh9BSK3DisRoiSKEtDV9EFkBGG1UudURBLUurUkKxKJ25vcqmQk4An6BUSkUhJg72uJiv6kfFqajSdnZaExLG6D-YSiFN2psQhSP6ddS8Rq2xXzg7ngIsz4rgYz4U_8vWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ابوالفضل جلالی بازیکن پرسپولیس: برای هواداران استقلال احترام قائل هستم. آنها زمانی که در تیمشان بودم به من انرژی دادند. در استقلال بهترین عملکرد را داشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/107032" target="_blank">📅 23:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107031">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19a96e43d.mp4?token=MVb8Q8DsZEvHXa9cGxA6FPweTFYaMMVYjCEEcLLz7rO3InwIg8Nd4qkrbx62s4qxKAu8DFMeTAOva2EvgscafiPanY1HyK6X7P3vd36WeXgWIbWxCbika2AYPnmxQPFzChbfslWYPChutIygjXsaaxAiTHq937-wfDDFAVHtQ-TEwkYMC7oJDyVZ_hwZGCyJ8VS3lQVE5I2lSbrxB5AhMO7Y_okRwrHypq2f6Pw4sCoMhQT9Vmech_cWzJZqJMAlENm_4zvWtPHe-_m4_qCKiUst_ZgmCFWl5ohJ5lv8Kr8FvjskpbV-26dYS55Sbl3ezxmByKidO26bW2dKjZojNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19a96e43d.mp4?token=MVb8Q8DsZEvHXa9cGxA6FPweTFYaMMVYjCEEcLLz7rO3InwIg8Nd4qkrbx62s4qxKAu8DFMeTAOva2EvgscafiPanY1HyK6X7P3vd36WeXgWIbWxCbika2AYPnmxQPFzChbfslWYPChutIygjXsaaxAiTHq937-wfDDFAVHtQ-TEwkYMC7oJDyVZ_hwZGCyJ8VS3lQVE5I2lSbrxB5AhMO7Y_okRwrHypq2f6Pw4sCoMhQT9Vmech_cWzJZqJMAlENm_4zvWtPHe-_m4_qCKiUst_ZgmCFWl5ohJ5lv8Kr8FvjskpbV-26dYS55Sbl3ezxmByKidO26bW2dKjZojNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
ابوالفضل جلالی مدافع پرسپولیس: الان طرفدار پرسپولیس هستم، عاشق پرسپولیس هستم و سرباز این تیم هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/107031" target="_blank">📅 23:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107030">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6fa04dad9.mp4?token=EX_eP2UihTmf0CQt-QkMYe_6oIrF6xMJpr3K2tY7CfS6F02vFJgW8vjJ0k5k6Z50Nuu2FaOpQElWtU_QxrgdNGrCeNc8lvktz98YeMXhgLAELGgrATpmHtY1jQc9p_q0J0tOJYsn4npYT6hsEL07DjBQgTKgkdVYjsR3lpQhLHiGxIXEOqG_8aIii8rmgCjfvIDL2sD95ElZ7XTGIs1jwqseqlAKuA8iFGgTi1QUYT6I_qTWuLXeyok_oZ6ZgH_lp3MDcvAq1DQwbfouwY1v1LnE8kteny1Dugs4TKbxwqdBnoFWZU39Vlj9MY2qhjX1SXQ5Hs05sE_SeeEQCsoq2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6fa04dad9.mp4?token=EX_eP2UihTmf0CQt-QkMYe_6oIrF6xMJpr3K2tY7CfS6F02vFJgW8vjJ0k5k6Z50Nuu2FaOpQElWtU_QxrgdNGrCeNc8lvktz98YeMXhgLAELGgrATpmHtY1jQc9p_q0J0tOJYsn4npYT6hsEL07DjBQgTKgkdVYjsR3lpQhLHiGxIXEOqG_8aIii8rmgCjfvIDL2sD95ElZ7XTGIs1jwqseqlAKuA8iFGgTi1QUYT6I_qTWuLXeyok_oZ6ZgH_lp3MDcvAq1DQwbfouwY1v1LnE8kteny1Dugs4TKbxwqdBnoFWZU39Vlj9MY2qhjX1SXQ5Hs05sE_SeeEQCsoq2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
💙
ابوالفضل جلالی: ساپینتو شاید از قیافه من خوشش نمی آمد که به من بازی نمی داد چون از نظر فنی مورد تایید او بودم/ جالب است رامین رضاییان هم همین مشکل را با ساپینتو داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/107030" target="_blank">📅 23:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107029">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11cbab4a72.mp4?token=G-CL6AxnmiA-gbiHk4dHzAeNu0WjPUNRW0up0H-ITT2thvv9dGsb3LmAAK1taRrPRK8KKHeW-sANJ442dgPhR94G0r1p4yrCNc6RdRrEa1V_Y_MygsZuzSHcTTGhKSq5NTPw5c-LngrYrBsaDB9v8_S8T4YgsORrOs4RO4LzgJbNQmMzYKD0dSTZitfJZoS_NghiTgVlPS4IUBkWpuH-haUWZjleNeozW7BVSpyniRyGPzBRNmHVfhbvnsgzXyEMPsZ6pcFPJEoAPhFhL_d0iOll-Jb-L28G1ysYMXRNl_PeVmY8y3IPl-Cn_oH7vFwTBabZAagUVJX-8I6VN9PDWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11cbab4a72.mp4?token=G-CL6AxnmiA-gbiHk4dHzAeNu0WjPUNRW0up0H-ITT2thvv9dGsb3LmAAK1taRrPRK8KKHeW-sANJ442dgPhR94G0r1p4yrCNc6RdRrEa1V_Y_MygsZuzSHcTTGhKSq5NTPw5c-LngrYrBsaDB9v8_S8T4YgsORrOs4RO4LzgJbNQmMzYKD0dSTZitfJZoS_NghiTgVlPS4IUBkWpuH-haUWZjleNeozW7BVSpyniRyGPzBRNmHVfhbvnsgzXyEMPsZ6pcFPJEoAPhFhL_d0iOll-Jb-L28G1ysYMXRNl_PeVmY8y3IPl-Cn_oH7vFwTBabZAagUVJX-8I6VN9PDWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید الهویی مربی تیم ملی: درخواست کرده ایم که از اول دی ماه اردوی آماده سازی تیم ملی جهت حضور در جام ملتهای آسیا را برگزار کنیم
🔴
میثاقی: با این وضعیت بعید می دانم تیم های لیگ برتری بازیکن به تیم ملی بدهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/107029" target="_blank">📅 23:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107028">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12081ba765.mp4?token=W5i0Rznr6zRO5i_oxsJEERaVkolQJP4pnpdMCNLJadPkR4dVh_AVDWK93XVAmkrs_lKGbj9RVgxc-l-kE3ewW7hkEYjJSwuyWBBq1lBGTTvlVTcJFwpygkA2wxdv0s8RZ2I0XJ0LFNOx-FY16bbsp6OQt9bcs09ztcMZG_KdoThlo38Oc2TwQw6QaX75TqJw6Za8D7nSkfmjR62rS-jBhltpl24lkYRB72YCYrro9ydFPMjf4dfwqJnKmvKCkNREdiJuxi6LuLQD7BYMVgWnVA9PYgSAwSr062GCeFNUzJxeGJj_6hh2_zW1EQnW0KTr4ULEZNbBR5IQWiCKrX9fvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12081ba765.mp4?token=W5i0Rznr6zRO5i_oxsJEERaVkolQJP4pnpdMCNLJadPkR4dVh_AVDWK93XVAmkrs_lKGbj9RVgxc-l-kE3ewW7hkEYjJSwuyWBBq1lBGTTvlVTcJFwpygkA2wxdv0s8RZ2I0XJ0LFNOx-FY16bbsp6OQt9bcs09ztcMZG_KdoThlo38Oc2TwQw6QaX75TqJw6Za8D7nSkfmjR62rS-jBhltpl24lkYRB72YCYrro9ydFPMjf4dfwqJnKmvKCkNREdiJuxi6LuLQD7BYMVgWnVA9PYgSAwSr062GCeFNUzJxeGJj_6hh2_zW1EQnW0KTr4ULEZNbBR5IQWiCKrX9fvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
سعید الهویی: پرونده حضور احمد نوراللهی در تیم ملی کلا بسته شده است و این بازیکن خواب و خیال تیم‌ملی با حضور قلعه‌نویی را از سر خود بیرون کند
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/107028" target="_blank">📅 23:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107027">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNtwOrXLI6PZF9VTCzIfOOjM0_r_cdYK0olQybbohyyZ6DuoKxgnbX7pksVzooo2Qy6h6eqw3ZwN8LirsfCh1qW074p7EFdQWArdQCZNI86CUOUDKtRDjwNHT814WFkwty4Q08CAF1zKILfT0WVW-fyv4ujLvIy_wmhx34WjzpVp395wIY1ZCHNF2Isgt35Olaij25uAUOR2bUaTLV5disvX0Oc_pIyhMWfwiM5ebdm61H0wMF9muyXoAJxeLhXavn6h4zGLjK9Mley2R_vurkKXW48t0Ahl6HaX1LOPQepCoauueebbLGsXPQBonScRubeOirS5CFPSyi1pMt3aWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
سعید الهویی: الهیار صیادمنش به دلیل یک سری رفتارهایش به تیم ملی فوتبال ایران دعوت نشده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/107027" target="_blank">📅 23:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107026">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c45095faec.mp4?token=EgMtRFdgcgsDfjAFA4WD_cCvl8u5VQqEbh_moU8_fpP0iSBlN0vfEnTB5cG8mXhvVdw3I6HAY3BVr2eOQjFIvIZ8ci0tHmiaDMqx_HHhfMIEaR6qW_yo-aCX5jZSZIWbqEu8m7cmL4W4QXjqsxpH-wHoUCl51g1tTFPWwIKh6cOcgMOWz1ep1BASuzSL2R8aypsjzp2Fg_pBBSYO4o2SX1y-HqCVGQd0rv92zEj3aJerT8GqGtJaolheHthT3CCC_W_PEKCOKxYCQuXUVyyJ3825TxJLyakADil0W_tXAB2n_Zl9gyjHrBx9p8SAy-L0tVPE73l-F_0ibe1MGe2gAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c45095faec.mp4?token=EgMtRFdgcgsDfjAFA4WD_cCvl8u5VQqEbh_moU8_fpP0iSBlN0vfEnTB5cG8mXhvVdw3I6HAY3BVr2eOQjFIvIZ8ci0tHmiaDMqx_HHhfMIEaR6qW_yo-aCX5jZSZIWbqEu8m7cmL4W4QXjqsxpH-wHoUCl51g1tTFPWwIKh6cOcgMOWz1ep1BASuzSL2R8aypsjzp2Fg_pBBSYO4o2SX1y-HqCVGQd0rv92zEj3aJerT8GqGtJaolheHthT3CCC_W_PEKCOKxYCQuXUVyyJ3825TxJLyakADil0W_tXAB2n_Zl9gyjHrBx9p8SAy-L0tVPE73l-F_0ibe1MGe2gAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
سعید الهویی: الهیار صیادمنش به دلیل یک سری رفتارهایش به تیم ملی فوتبال ایران دعوت نشده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/107026" target="_blank">📅 22:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107025">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‼️
🙂
🎙
به مالکوم گفتم Bro, Easy Football!
کلماتی که از درگیری شدید علیرضا علیزاده با بازیکن سابق بارسا جلوگیری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/107025" target="_blank">📅 22:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107024">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
‼️
انتقاد تند عادل فردوسی‌پور: پدرمون در اومد این‌قدر با ازبکستان بازی کردیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/107024" target="_blank">📅 22:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107023">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee3019bfd.mp4?token=uFzdgiklcI6C1yM8vc9Ra9t60VX4a5SBwdocpLy12jk2wjerd_Pfurq7L9kHBdVjDccCDaoPG3kZAe4mht7LLjQUh1lIoLTPSNE2QVolF-9fn9KYY_tYB4KpMd8g6lX_QiJLLF-W2LMVcjL4qgCeIPVWFSpemRI3FceAUnY-gkbuuTAGXXXoWKlifN9mSYf4GB8Hio81N3CpZPmTI43tE5a_yAzEQ_j7YR3dSvBWE5TusJ5DgZ5PIdwlFlSzqbfqDQdljYK701icPrLEOzpj2Icvy2TwWZw1VlQ_4K8SqFPxKotugChkWGEeWX93Y4lsrQzEXSYTcwbI0NTvAMR1Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee3019bfd.mp4?token=uFzdgiklcI6C1yM8vc9Ra9t60VX4a5SBwdocpLy12jk2wjerd_Pfurq7L9kHBdVjDccCDaoPG3kZAe4mht7LLjQUh1lIoLTPSNE2QVolF-9fn9KYY_tYB4KpMd8g6lX_QiJLLF-W2LMVcjL4qgCeIPVWFSpemRI3FceAUnY-gkbuuTAGXXXoWKlifN9mSYf4GB8Hio81N3CpZPmTI43tE5a_yAzEQ_j7YR3dSvBWE5TusJ5DgZ5PIdwlFlSzqbfqDQdljYK701icPrLEOzpj2Icvy2TwWZw1VlQ_4K8SqFPxKotugChkWGEeWX93Y4lsrQzEXSYTcwbI0NTvAMR1Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ادامه شاهکارهای داورای لالیگا این صحنه رو هم دیروز داور بازی دپورتیوو و بتیس کارت قرمز تشخیص نداد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/107023" target="_blank">📅 21:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107022">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه تراکتور با تهیه مستنداتی درحال رایزنی با نظام‌وظیفه برای کسری یا معافیت علیرضا بیرانوند است. تبریزی‌ها مدعی شدند که بیرانوند دچار مشکلات روانی است و به همین دلیل خالکوبی کرده و باید از ادامه خدمت معاف شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/107022" target="_blank">📅 20:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107021">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abz0BF1cBAV_RPBPFRFbhlNtWBDduZS9ALjPYvF6c8Ui-u1_san61z6HGHmVcUtqN4d612PbYGDB7EtihMvB56zlfWoEukIxGZ68wjU1kce8ZPnA1DlxnQh4Rc5jZ424_ANOaJdULghCpcdnh9-ORHzwEpaobWUB9VCgNGD4E9-1xXYPxEIm_8_0-TxOmxogBk1bSU3Uvf1smVl7bqrTiER4co5gP1Xjn9JO2rLurjTcE2WApZPnCuje_GwwrHSOeI2r907KUwKyjopkT9EdNHi6wiokZiaWmEB1i5QNZoAMYwIn00xGzzcGN4qnSl3i__zxM5AGLSl23_soMXG48Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
مقایسه آمار نیمار و رافینیا در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/107021" target="_blank">📅 20:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107020">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/690c7befaf.mp4?token=UtkXF4Y1RbUGJHJRvtGio2Ln0mLOE-BS-6xi_YPuMJ6mZPVQqi4absllW7YzTfls0P75quARYquEGAQYh0EwRjoql0sKQqdyqsT6dRTfTCKyZjKRMxF5N6pfy25Ji9E1SuB7O7imSAd-9aHMTHtol4SePSc4kZenybkKhrFYCNsftAcUcGSWNf4tmXXw8daFSOVmGughMO5fNoVB-pCBZnKf9s24CaXChoUSyKwyKxhQNOcTUnt3q2rLt01uQNeUyTGKUIMr0fIpG8RwRyJpelULmsO-qEnK0QVNJhuu4B2bYnd_HXxrdaXuaVFwiie44-mhBx966s8WQyOsJthWpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/690c7befaf.mp4?token=UtkXF4Y1RbUGJHJRvtGio2Ln0mLOE-BS-6xi_YPuMJ6mZPVQqi4absllW7YzTfls0P75quARYquEGAQYh0EwRjoql0sKQqdyqsT6dRTfTCKyZjKRMxF5N6pfy25Ji9E1SuB7O7imSAd-9aHMTHtol4SePSc4kZenybkKhrFYCNsftAcUcGSWNf4tmXXw8daFSOVmGughMO5fNoVB-pCBZnKf9s24CaXChoUSyKwyKxhQNOcTUnt3q2rLt01uQNeUyTGKUIMr0fIpG8RwRyJpelULmsO-qEnK0QVNJhuu4B2bYnd_HXxrdaXuaVFwiie44-mhBx966s8WQyOsJthWpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
واکنش اتلتیکو مادرید به عکس‌های پرینت شده مورینیو در کنفرانس خبری
: «همین حالا به آزار و اذیت داوران پایان دهید!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/107020" target="_blank">📅 20:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107019">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0863a4f870.mp4?token=DQsxHAyROU7DWhUqfdsyvrJfyCimSo6jlLAHtKbp41QL8FRPfjRvN8RnFI6P8iJR7KC2jT4ldEv6xv8TPxRsuDLHRszt4Djo8y75pwM5o5jDdUe8PQ-NpnUAimsSk4yyFvRb_VVEmIoEAi6jn20akTdNCFSSBnEDfUCjvSlKLqYNsFnIRnRaxVM0S0kridBRUL74sfS5cxuBxeo6rM1Qoa9W_w5X04aruNGlDrc-lPE7GszjQLUzZGLWJgQk18yKAljURhhmjOzM-dZigCpcBmYDowUGNXJywZ6CJyD_DQAs7KNxCIlGIl9dbXjrwj_Jd4bwmjcuOrc8mgegnag4Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0863a4f870.mp4?token=DQsxHAyROU7DWhUqfdsyvrJfyCimSo6jlLAHtKbp41QL8FRPfjRvN8RnFI6P8iJR7KC2jT4ldEv6xv8TPxRsuDLHRszt4Djo8y75pwM5o5jDdUe8PQ-NpnUAimsSk4yyFvRb_VVEmIoEAi6jn20akTdNCFSSBnEDfUCjvSlKLqYNsFnIRnRaxVM0S0kridBRUL74sfS5cxuBxeo6rM1Qoa9W_w5X04aruNGlDrc-lPE7GszjQLUzZGLWJgQk18yKAljURhhmjOzM-dZigCpcBmYDowUGNXJywZ6CJyD_DQAs7KNxCIlGIl9dbXjrwj_Jd4bwmjcuOrc8mgegnag4Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
وضعیت رختکن تیم‌فوتبال رئال‌مادرید بعد از شکست دیشب جلو اتلتیکو!
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/107019" target="_blank">📅 19:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107018">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beecf6e577.mp4?token=srO8zwcuvOVW4_fPP3Sy6Us5iyFv0o1XVUp-q9e_0E8U65UxiRJTpa0k5YiAvn6KyJ-uHY_1xB5KgSdkjMq0bKap_N3abK5tdLwP1RvWR_sSNNd5ALRgfsOfcfKR00kLBDibKoaUxXZxSH_2LYb-D8zXe-c1iLU4tiXtdgh07n8VR2rwtc9G7pWCHlZRvSjqSStxvbpxu6TvRDSFu2yys1I7-jqdfqiVMJfdaa2PlJcbL7b4y83DLq4hOwQDSVpRIU6KA3fZI5pdEpAEI3nkrAHLDAxV4NSXnkCRU1Qno-ElYGIFR0h0M2ZjC4PjVRu1-CsnDW_AzNvXktiqnzlB8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beecf6e577.mp4?token=srO8zwcuvOVW4_fPP3Sy6Us5iyFv0o1XVUp-q9e_0E8U65UxiRJTpa0k5YiAvn6KyJ-uHY_1xB5KgSdkjMq0bKap_N3abK5tdLwP1RvWR_sSNNd5ALRgfsOfcfKR00kLBDibKoaUxXZxSH_2LYb-D8zXe-c1iLU4tiXtdgh07n8VR2rwtc9G7pWCHlZRvSjqSStxvbpxu6TvRDSFu2yys1I7-jqdfqiVMJfdaa2PlJcbL7b4y83DLq4hOwQDSVpRIU6KA3fZI5pdEpAEI3nkrAHLDAxV4NSXnkCRU1Qno-ElYGIFR0h0M2ZjC4PjVRu1-CsnDW_AzNvXktiqnzlB8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
دیشب «محسن نامجو» که به تازگی برگشته ایران، شروع کرد وسط خیابون با صدای بلند آواز خوندن که یه هموطن با دو کلمه «ک…، خفه‌شو» دهنشو بست و این شاهکار رو خلق کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/107018" target="_blank">📅 19:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107017">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34f1b0314.mp4?token=QnHM4mRrSOkQJigEmqktBSUXevIdl2HqUN1k8zWdWeLmrV_UyOmiNdo1LM2aQ8Joyd9LZya_u3Z3E96LkGsI2lh6uUkdGeAgEN_jKH9Ci5l3FLwkZ89cYaTGt6Gehaoa0AqxVy-sdW5DYzTN3LRVhuflt3IYe-3hWTKCUXnzBV5LXpQEvigbb8ahUUF5Bh5OencWIHy89S9NuItIc9WahK2RudtEoLQDIMuw_MJc4J3r0_fpbkCOa_PC37d_Fwcln0Wl8ZpPVoSr-ay0BN8dkT5vEp5AMAnQcbZNcaBu5LLvdbVnEmju8QMsz-J6AJsWQBy9Y6Fw63mG9ojj3X3o6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34f1b0314.mp4?token=QnHM4mRrSOkQJigEmqktBSUXevIdl2HqUN1k8zWdWeLmrV_UyOmiNdo1LM2aQ8Joyd9LZya_u3Z3E96LkGsI2lh6uUkdGeAgEN_jKH9Ci5l3FLwkZ89cYaTGt6Gehaoa0AqxVy-sdW5DYzTN3LRVhuflt3IYe-3hWTKCUXnzBV5LXpQEvigbb8ahUUF5Bh5OencWIHy89S9NuItIc9WahK2RudtEoLQDIMuw_MJc4J3r0_fpbkCOa_PC37d_Fwcln0Wl8ZpPVoSr-ay0BN8dkT5vEp5AMAnQcbZNcaBu5LLvdbVnEmju8QMsz-J6AJsWQBy9Y6Fw63mG9ojj3X3o6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت هاشم‌بیک‌زاده از استخدام مربی خصوصی رونالدو برای رساندن مدافع تیم‌ملی به جام‌جهانی ۲۰۱۴ برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107017" target="_blank">📅 18:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107016">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beeb6137f6.mp4?token=KUwTPisDnV2axUgpzDWe4ggOLc4hkwXsXEkNNmJDxJdnQ28RSzL1JUnF1ydyTjVVwiwianSiPx_ONrZUxWEOuvJnCLn6Nb2EO9IJ0JwfZ5fThbHVW5hhO2lTCyXgvW6HPqOT2b-ZPwtbOFr9JiNV5Y2Ki6sxkDFUICihRdrWLYZv9ijbGBV9e06uh2_7OAHFQFX9qcOLSx7yifIYVOvMXLik1kkTfiqNRFjOAJ6Ne-V7aR0vxT5bWX55NK1emDxVLbkhfLVu2FvMW2-Ry5Vq5lKE-FVlWGOmvcv_Hlz-AwCJWtm6L9Qzldb3HsVoLLzImlqV3tqtilr6wHgYdluY6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beeb6137f6.mp4?token=KUwTPisDnV2axUgpzDWe4ggOLc4hkwXsXEkNNmJDxJdnQ28RSzL1JUnF1ydyTjVVwiwianSiPx_ONrZUxWEOuvJnCLn6Nb2EO9IJ0JwfZ5fThbHVW5hhO2lTCyXgvW6HPqOT2b-ZPwtbOFr9JiNV5Y2Ki6sxkDFUICihRdrWLYZv9ijbGBV9e06uh2_7OAHFQFX9qcOLSx7yifIYVOvMXLik1kkTfiqNRFjOAJ6Ne-V7aR0vxT5bWX55NK1emDxVLbkhfLVu2FvMW2-Ry5Vq5lKE-FVlWGOmvcv_Hlz-AwCJWtm6L9Qzldb3HsVoLLzImlqV3tqtilr6wHgYdluY6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرحسین قیاسی: مهران مدیری برای حضور در برنامه من اصلا هیچ پول نگرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107016" target="_blank">📅 18:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107013">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/037abe05f9.mp4?token=EtAs_YPybGGAoUMMb6LFFta4fUQfJzUEUWs6yb7dOt7rz9oKyUGD8HY1YU7fERLJCm8KlXjKsv_yX2Zx86x7ennSqsXd3vZQCGU0_fYFmGirioHxscmoc5FwTpfzTOdbcVXwoWF12d2y628Ci-H2lgSnTE_gJhhp5D-9Pr38Q5frC8njt4hichGKp1ZYhREe7TSxWL_vBlHM44pgtJa8OxJAPzZf5P50CAMtG4eKAOx0cVlR3Ekfy7LU4i2sThjhMzBw2-7aA7z8LavMvm46k0Q3j4sz5BGtkWEkgutvyPrtKaM9GLvWzoUcWbxUk8T__Z6h2-UM8tSDGEaQBAAyPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/037abe05f9.mp4?token=EtAs_YPybGGAoUMMb6LFFta4fUQfJzUEUWs6yb7dOt7rz9oKyUGD8HY1YU7fERLJCm8KlXjKsv_yX2Zx86x7ennSqsXd3vZQCGU0_fYFmGirioHxscmoc5FwTpfzTOdbcVXwoWF12d2y628Ci-H2lgSnTE_gJhhp5D-9Pr38Q5frC8njt4hichGKp1ZYhREe7TSxWL_vBlHM44pgtJa8OxJAPzZf5P50CAMtG4eKAOx0cVlR3Ekfy7LU4i2sThjhMzBw2-7aA7z8LavMvm46k0Q3j4sz5BGtkWEkgutvyPrtKaM9GLvWzoUcWbxUk8T__Z6h2-UM8tSDGEaQBAAyPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🎙
بهترین گل‌ دوران فرشید اسماعیلی کدام است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107013" target="_blank">📅 17:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-107012">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvuJZai3Rv3RO0LNYPWvjnZa34jJhb5WLZFEs57_nTzGluax0nfykADLmiC4LO39TohtLlIliFZLvx9DqVIjTc5Pv5nbDeb8aUInmwqiNLimH6bIGrmpDY3pnOSR_hHATaf5ranij6eQi1Va352_eFWPHlomOdty-K-ymaFV0I7EL72oXttnNRzKMd_1_f-Yp4IGIP5yDe6Kf3i_bgQB4gzIHwCOhjIKrncNZ4Gf2Gxe9IUmUFXXcF3R0MMjLvzGIPVr1NMvJpL7m7wJ0zLjVqZnlx0P2T4qSkO8Co2Ouh3iDwWgaGVA0tnGKf_5tF5LqdtcCyWRcGMIL_aIy_nwOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سه سرمربی آخر منچسترسیتی همشون پنج بازی اولشون تو PL رو بردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107012" target="_blank">📅 17:20 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
