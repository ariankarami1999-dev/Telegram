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
<img src="https://cdn4.telesco.pe/file/aDRmO3NZzgxaVfRk9jagTLRmv0MpmbkQFhixgaqJx4_wnCwABufaAnZ47PZmD3PreB3qJZpA92ARjyUebxDUZa3J46iwOSO8Zqg-_Sr_VnqxRUoNXPl8BGXYdLmUEXwyDiDAON6ncqwu5dHwTxz5nCbDLnm6_hxqiSyO1mkYq-0Cny2OOqavDcOaegwjZsa8CPtJQaF9vAfeypOJHH08ln4Rg2md-vYTVsLcl5rcrFzdjdKxkm-0VdJKaVB_xozIoeY39GGZS6fXaj-Hm3p69do-YiWm4pE8rJ0GSQdIMeDiBZrtLEFITnai5MyfequVW7ingUYPYuMvLypysAkO_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 16:40:45</div>
<hr>

<div class="tg-post" id="msg-152129">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
صداوسیما:
درود به شرف اعتراض کننده های فرانسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/alonews/152129" target="_blank">📅 16:35 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152128">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: با پاکستان و ترکیه همکاری می‌کنیم تا همه مسیرهای زمینی ایران را قطع کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/152128" target="_blank">📅 16:21 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152127">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
حسام الدین اشنا:
راننده تاکسی بازنشسته سپاه بهم گفت شما اینقدر نامردید و لج منو در اوردید، که از لج شما می گویم رضا پهلوی
تا بسوزید و این بلارو شما به سر من اوردید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/152127" target="_blank">📅 16:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152124">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sC_PUqHDvbKuvinN1OJNyioOSrhLq14IG0hZpGsMeuBBO-Pcx3G4mchvPCrU7UuzV7c9ZwSgebVRe_2Hloa3aGwGHkeeN_vbKVJzrnu2osekLEGvWFNre9ep5T56Ui3z-CLymJjCqeKETIf0QcwXPUyue5VVXH6HviWAh3yFUow3bJeh49CEKTqkqPT7f0g5V5IQAq_qHiSpgDVtcs-NBPOYVNdVN8_yIyiq5M5Qo9H6kv8pnSUNOACS2OBk1Rc0KG1j0HRaR-NKYCyFFmJgXBDQDCfVUqVFPAkqWGpUZdj-_YkztIYzN_FAJO0C9sLadsuQQoZN3DQXlqfw9gt36g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9MI13mPAepaPrtMwkhGqHv25myT87xTZkNOgzvtKBtMGN2RgTzbOUG7gn9nlaWTa-f7F1oX2bj__mB8S52SG-gxR7jkkXte5mwhkdIc0G-WWbAD1teIiJkjNuSym3mrKQCwSM2hdz_Vr5Pt9Fu65fyTITlzxQ9CkKIThSFC6GGviFcuD0Amwgf9e8Sx_H3lr1W9EOnP130EkkV7mocfGMyFORbX_dAHBj85WUCQ_4VU1m56YC1qSSiI1BEyRV3TEEG_yOdPUbM_qbDkDGKUzbd-KIcFRPgCRXJ4EKte5I-ep-BAgiVbI8kl4go-eIgMxtu4GmTG2j-vcbUJRdm95w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKDcvqk6XS1IJXNAcoKPDt58OfV__OdyEpnfHIJ028zBgVyNCGRevZAyNPdy9A1Bvpg_F46coYxxaBx4zkJWjEk65QBm_cmRGo2nllNI7AFLPJPC8V2iJTrdPh9FZeKMRM63iC4UOjPpmYvGcWxwXcs49gv30hXUvXV3QwYQwr6zRBjZli_Dp8A9s_a5DSAod5p19atLXqS0WH3tLYx-oJgnJqLFYNLbEk6mZXW9UtKHquy-lXEmeOhKHTvj7PoPZmNdc8BKiWOmJmKRJzDPc3GDh1Xe9OL4NPRtybgi5tAUiq4xc-wWdrqs3BVu91ozGMK--8E6vM7iaOvmYSm_PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هوای تهران امروز خیلی تمیز شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/152124" target="_blank">📅 16:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152123">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
فلای‌دبی به‌ دلیل تداوم شرایط ناپایدار امنیتی، لغو پروازهای خود به مقصد و از مبدأ تل‌آویو را تا پایان اکتبر تمدید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/152123" target="_blank">📅 15:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152122">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cf041a409.mp4?token=gWKjZFiRKOn55CrOyEANtfl8yw-IpXCeIS797HgIpxBSIr-d2bZNvjdQXURkPcvL8pz91pQURAOSmOea6v5col80QJnUo-zMrQ1GE4KSIljt3xAS4v2yF4DPAMIWhtQSfkSpTzVqUSa8jkl3OzAz11vrdVDWFOZTZV2McRLzi2hRpF_cxuxUR9dOhe5C2GzapyVCnOMXfcCRHfww7DqwC-8SGuNt0lZN2stLhxtf7XbBxdUDf3kmozls1V9t_hIBiITQevYjjIra8ybMssUx0bvmAWWFpb6sZy1Oo1Gc-Gxa8MRPT2QN12-BI5tkOsdTvOl7p23u9n-Le_pP4CWKtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cf041a409.mp4?token=gWKjZFiRKOn55CrOyEANtfl8yw-IpXCeIS797HgIpxBSIr-d2bZNvjdQXURkPcvL8pz91pQURAOSmOea6v5col80QJnUo-zMrQ1GE4KSIljt3xAS4v2yF4DPAMIWhtQSfkSpTzVqUSa8jkl3OzAz11vrdVDWFOZTZV2McRLzi2hRpF_cxuxUR9dOhe5C2GzapyVCnOMXfcCRHfww7DqwC-8SGuNt0lZN2stLhxtf7XbBxdUDf3kmozls1V9t_hIBiITQevYjjIra8ybMssUx0bvmAWWFpb6sZy1Oo1Gc-Gxa8MRPT2QN12-BI5tkOsdTvOl7p23u9n-Le_pP4CWKtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر جدید از حمله به فرودگاه ریاض که دیروز رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/152122" target="_blank">📅 15:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152121">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
گفته می‌شه آمریکا پیش از شروع جنگ، نیروهای نخبه‌اش رو برای عملیات‌های خاص تو ایران مستقر کرده. هنوز هیچ مقامی این ادعا رو تایید نکرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/152121" target="_blank">📅 15:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152120">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
مرکز آمار: جمعیت فعلی ۸۷میلیون نفر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/152120" target="_blank">📅 15:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152118">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQRVaSirYta2EHyg6vjoKy4Iva_2kcKqVLf0Qu3rKZzDEZZDsVlAfqrUgi9poqXM7pfvReUt1wzK74tFae55kpShr-9rbybe4I1kXHhpivlEZEbM2xmQVACeC5yAawWUkqrDkNbYX6xZ0TF7wVxsRMZVaUryHhsPlWxRvJ0Zpw1FlODqr9l-hqLErHbF5p1vwfoOcBufcTiDxzJkvLVWGyJOYe3YVTYGnE8RiBPXa-Pdb-mi8jmfE9uDZL_xAocIAwQkbQCl3Bc5i0jIl_vEXcuhcpGSLxFupipPzUKoQKhzrYe82TuwJp18EKd11fQybHSzv58NHvTCv4U7-OxoZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U29ugYadJ62psep8NeGpIPTPerDFcib02TxYC0JxM263_rmPKM-8yD1t3lhREOcfMuiTY7BvIg0u8_LZieo75YWqD-Picj2T1HQR0JUu-PTqZTiESIG4mfDAOA14V13gPtjxtQPjSksQxzvtf1u-MyWidjzBbkpIdNjZeECON39bQpJQflfRCyBpkb4-QrWfVkUCZSXvSOKSE7hYU462bhNyTCUGhQKYFpepL82hu7X1pco_tNvJFIz4gP5bckAY1qGprZnFDsE2-vCxGjg_QScmOd216EqXF1j6bvVKQ23tamQXzlwpyAJsO-JQma-ivHvNsWrynLNAiuOeUxOIpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر وایرال شده از رزمایش امروز جانفداها تو خراسان جنوبی و استفاده از کودکان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/152118" target="_blank">📅 15:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152117">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
شرکت فلای‌دبی لغو پروازهای خود به تل‌آویو و از تل‌آویو را تا پایان ماه جاری تمدید می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/152117" target="_blank">📅 15:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152116">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
خبرنگار رویترز: آمریکا ممکن است نیروهای نخبه را برای عملیات های خاص قبل از شروع جنگ در ایران مستقر کرده باشد.‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/152116" target="_blank">📅 15:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152115">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aea388dc62.mp4?token=MDJGKdbWxXZRT5KX2JPC4LOSklG0XqfP8LDaAIlasUjX6rOzkqnBbjfIBWwEJD-Fa2RlxTn4dyC5VMDlYfnNdgnGsR7h3qKDGA4P245vvi5aXYwV5kjeR9P4TRZBKTL5R2HweI5UxdmDBEq7wEqWoAmb48DjpiqeekWtw8hrV2OwVJtXi8dzs7RyYArypTa3qE5cR_QnNWIGBHv7FwHYz6cmjDs-SV3s3ZltUSfbQH30A5lg5oFHkaI_7f7CacDQA9YkUiGAVqr9jklYszw2GvCVhihO4xdo4d50s20d0Rd0sWm1xnF4j-E173zgipHG8FoiqMDTb2rE0N6XUFPMIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aea388dc62.mp4?token=MDJGKdbWxXZRT5KX2JPC4LOSklG0XqfP8LDaAIlasUjX6rOzkqnBbjfIBWwEJD-Fa2RlxTn4dyC5VMDlYfnNdgnGsR7h3qKDGA4P245vvi5aXYwV5kjeR9P4TRZBKTL5R2HweI5UxdmDBEq7wEqWoAmb48DjpiqeekWtw8hrV2OwVJtXi8dzs7RyYArypTa3qE5cR_QnNWIGBHv7FwHYz6cmjDs-SV3s3ZltUSfbQH30A5lg5oFHkaI_7f7CacDQA9YkUiGAVqr9jklYszw2GvCVhihO4xdo4d50s20d0Rd0sWm1xnF4j-E173zgipHG8FoiqMDTb2rE0N6XUFPMIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای آتش‌سوزی‌ای را در سواحل عمان در پی هدف قرار گرفتن یک کشتی ثبت کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/152115" target="_blank">📅 15:21 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152114">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
لبنان بزودی به پیمان ابراهیم خواهد پیوست
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/152114" target="_blank">📅 15:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152113">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
احتمال تماس تلفنی اعلام‌نشده پوتین و ترامپ
🔴
دیمیتری پسکوف، سخنگوی کرملین، اعلام کرد که ولادیمیر پوتین، رئیس‌جمهور روسیه و دونالد ترامپ، رئیس‌جمهور آمریکا، ممکن است تماس تلفنی دیگری داشته‌اند که به‌صورت عمومی اعلام نشده است.
🔴
پیش‌تر، یوری اوشاکوف، دستیار پوتین، درباره تماس اخیر دو رئیس‌جمهور گفته بود که هیچ‌کس نمی‌خواست اولین نفری باشد که تماس را قطع می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/152113" target="_blank">📅 15:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152112">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMXuJwL4MPK-MYPS05Uk53Joctqt_Hr6mwWdsSIuDcGZ30fzpAVSstMOU-kwXaLdau8eXT0JKKOAj5syts2V1IdHgSS6ziTpkHqI8pWQ0P2gUEXpXAUuqmb4dcjDGQBitFzkmU09JgQUNYBsp7UMfTf2_w_tZdWilqL3NAWICPD_SkGUz8AwuyTBGluo36aP7xExhc3xZ1K0NOYMXKHB2MAZMT1rW6wt_EaVnrXBX7SprI7yslrLFhDITF8oa531FlDHWNGDtUms_3Sv6qE1AUuEuZVEfyXGxI_LINGoD0LcrMDNyRjGrow3e_WZe2vr6KBvRl0SRhPctFLDcCzwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جروزالم پست: در میان 8 کشور، کویت، لبنان و سوریه در صدر گزینه‌ها برای گسترش توافق‌نامه‌های ابراهیم (عادی‌سازی روابط) قرار دارند؛ طبق گزارشی از شورای امنیت ملی آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/152112" target="_blank">📅 15:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152111">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUlo84umKfmQchJ35Mnueidmc79lWLlzoSpByNOIy2S1vuPuUCjzwgkgsuFSLX8q66ow2T0e5yeenSkzoSxWh2XdNSdKwpf1pCOWxEfyejiX3xzq3fdYd6m2QRPuF8MvxA8ay4uwfExHyHhOYxHH5lCRAXGJ1KXIw4d03WaLmTs67c8B7UNr7H1zt-h_nsq6AvAt-UASlGLj6Qu4rDZZV_UocvXTHIjd0c6vc1kbf4VUQjZJDdJz_q8g0qt-L13qhO6b2USzRPf0FRZE0ktBXClRTidQZe01eTtgcBjzo2mU8qJcZCV5sUpp7h9donBhtBS-HMKSzkymQFGd_YeylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم‌زمان با هدف قرار گرفتن یک کشتی در تنگه هرمز، آتش‌سوزی در این تنگه در فاصله 25 کیلومتری از سواحل عمان مشاهده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/152111" target="_blank">📅 15:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152110">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
رئیس مرکز آمار ایران: برآورد فعلی جمعیت کشور، مطابق برآوردهای پیش‌تر اعلام‌شده، حدود ۸۷ میلیون نفر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/152110" target="_blank">📅 14:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152109">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
گزارش انفجار در تنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/152109" target="_blank">📅 14:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152108">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
پزشکیان: در همه برنامه‌‌های آموزش و پرورش دنبال عدالت هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/152108" target="_blank">📅 14:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152107">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
سخنگوی سازمان مدیریت بحران کشور: تا این لحظه ۴ نفر در اثر سیلاب و ۳ نفر بر اثر رعد و برق جان خود را از دست داده‌اند و دو نفر دیگر نیز در استان گلستان مفقود هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/152107" target="_blank">📅 14:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152106">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
صداسیما خیلی جدی معترضان فرانسوی رو دعوت کرد بیان ایران تا همونجوری که میخوان زندگی کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/152106" target="_blank">📅 14:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152105">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
شهباز شریف: مصمم به تقویت روابط با ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/152105" target="_blank">📅 14:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152104">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
دنبال یه کانفیگ ارزون با سرعت بالایی؟
🔥
با ووکس حتی تو قطعی اینترنت هم وصلی
💢
@VOXNET_BOT
💢
@VOXNET_BOT
✔️
میتونید با خیال راحت تهیه کنید</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/152104" target="_blank">📅 14:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152103">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67683d5f7d.mp4?token=XtHsXYpyDWTdTYu1hZEQVk2AxAwWWSYuteKewqKgMuBQPjVFiiQZ4mEI4MGPGG2Rvfunu_wajp_QpHqkfgDQKaIiVHYJXfTFRGXPrvRNppG1p200hav40EZVRDNa4GQHF2UQB2USvqeJj7Sc_6ZokPuRzU8Bm1VrbuTg1bDK1OMC3_YOp1zE9EFV2qx2qHyoTJ1G6L1f2uLxoVpde4UIbwLW8HglMPr8m6Z8NsXCSxUhyhOcm1OK0qZfjFsWRherpBDGG6K15IlnkXCgrjFiKhoJa4jICI9mDjvqP_MCCrZUf4Xy5arVtyM-G3TfOY3JWQY_dI0INe85lbf3AAuxog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67683d5f7d.mp4?token=XtHsXYpyDWTdTYu1hZEQVk2AxAwWWSYuteKewqKgMuBQPjVFiiQZ4mEI4MGPGG2Rvfunu_wajp_QpHqkfgDQKaIiVHYJXfTFRGXPrvRNppG1p200hav40EZVRDNa4GQHF2UQB2USvqeJj7Sc_6ZokPuRzU8Bm1VrbuTg1bDK1OMC3_YOp1zE9EFV2qx2qHyoTJ1G6L1f2uLxoVpde4UIbwLW8HglMPr8m6Z8NsXCSxUhyhOcm1OK0qZfjFsWRherpBDGG6K15IlnkXCgrjFiKhoJa4jICI9mDjvqP_MCCrZUf4Xy5arVtyM-G3TfOY3JWQY_dI0INe85lbf3AAuxog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از سیل وحشتناک در نپال
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/152103" target="_blank">📅 14:13 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152102">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
شرکت آب: قبض آب یه برج تهرانی شده ۳۰ میلیارد، مردم رعایت کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/152102" target="_blank">📅 14:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152100">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r-k6Nrd2D6o-VGgAXfZlJLI2CdsP3LfTCngN5BQbr5uRkT2YQPrrD-KWJKMIuXO3BwArzu1ImnA8lsIhs8rakMDv-UO3HWW9WfArOal-czAZJPutA2M5PBmNcRDbxI9X7N0VcyecDltLiC-oFqUEMuSZ7WHeq2-o-tLT4UYblbZ3J6WijuL73k7b3GCbhJAWDU0eYcEbSF8PSBJyzVIAa_fedXp_FwGVat8Mgji-d0GmOm-mrPJJchn9wpwUX074WnNwyyb1QhsmVPw6UGaS-BgX4W9euOTRmnsvxBia1pwXlj5ZIlIX6_Nl10kMwJlrMlsWXtPc_bzch1yhUuXTWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mo83coDloXJCQleUQTR9hd2omMBBsTWyOOPGlMcE-VEdcEwvSneGQN_Rz1XDogPhak6ztenY4lmO2SYWF5w9pJOToCKcen4QBRegADhduwVW9kfkjzej8sF6l2HrYh9d1OXFJn9iUIR7uiqqfATG5FiRo3hLNPyGUbPBVmrX6WhkjzEHYMOpLT2UHwsYPtPpIk3U2_V35OMC5NUF8n4y6M32AzqiNHoSDlk1Qc42dacl57U7XA-DR38K0USACIMFytxGaLDv7X0ws91AY2wX59oLk7w4E7H8Ce9nbahnCUmbOwb2qVbXQvu4FC8uDKl-9KppsG5Zb0QLWAo0NnFmug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر وایرال شده از رزمایش امروز جانفداها تو خراسان جنوبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/152100" target="_blank">📅 13:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152099">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
روایت المانیتور از سردرگمی در تل‌آویو در مورد قدم بعدی ترامپ: منابع سیاسی در اسرائیل می‌گویند نگرانیم ترامپ با پایان جنگ موافقت کند و درباره برنامه هسته‌ای تهران امتیاز‌هایی بدهد
🔴
در تلاشیم بر آنچه در حال رخ دادن است، تأثیر بگذاریم
🔴
آمریکایی‌ها به تدریج از ادبیات برچیدن کامل ظرفیت غنی‌سازی و خارج کردن ذخایر از ایران، به سمت کاهش چشم‌گیر ظرفیت غنی‌سازی و رقیق کردن ذخایر حرکت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/152099" target="_blank">📅 13:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152098">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سخنگوی سازمان انرژی اتمی: اگر منافع ما در دیپلماسی به دست آید، چه بهتر
🔴
صنعت هسته‌ای ریشه در ایران دارد و نمی‌تواند با ضربه از بین برود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/152098" target="_blank">📅 13:38 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152097">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
زلنسکی: اوکراین آماده است تا حملات خود به پالایشگاه‌های نفت روسیه را متوقف کند، اگر روسیه نیز حملات خود به زیرساخت‌های انرژی ما را متوقف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/152097" target="_blank">📅 13:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152096">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
سازمان ملل: در پی غرق شدن یک قایق در سواحل جیبوتی، 109 نفر جان باختند و 116 نفر مفقود شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152096" target="_blank">📅 13:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152095">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
دادگستری استان اصفهان: شناسایی افراد «تن‌نما و ولنگار» در بحث حجاب و عفاف آغاز شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152095" target="_blank">📅 13:20 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152094">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
خبرگزاری رویترز گزارش داد که پلیس لهستان اطلاعاتی درباره حمله احتمالی به نخست وزیر و وزیر دفاع دریافت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152094" target="_blank">📅 13:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152093">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d64a23e4e.mp4?token=QogJURzoTNmg2bv7pKssPemc6qoahtULW_i6ZV0ZAXN4MNvTHH_hbaRyfBg2qUyz64beMjUb5Ve4Jo4xXX-S8eLk_d84cfUgHsx4MwKHBv59zDnKaPqo-OAqvSa7MGLuzzwDIaaQ7q_0CXQWi4LdTwXAxurb35s6BzLC4bsYT38vhbLE4FsqEH03FvAzOBUwkI0p-lDPpz7INgCCDr0_NGLMnKvRBIh3mHNI8aonq1sfwI4VApK1WT81dQ_0DKWulPed0jENEvhgKRohQ-Eg44-z5jjN3KMAqNDg8znRcWNO6FMQWMe5VY2Bkva-Ta7OFxWkX1dcSMk7NbhttUc43A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d64a23e4e.mp4?token=QogJURzoTNmg2bv7pKssPemc6qoahtULW_i6ZV0ZAXN4MNvTHH_hbaRyfBg2qUyz64beMjUb5Ve4Jo4xXX-S8eLk_d84cfUgHsx4MwKHBv59zDnKaPqo-OAqvSa7MGLuzzwDIaaQ7q_0CXQWi4LdTwXAxurb35s6BzLC4bsYT38vhbLE4FsqEH03FvAzOBUwkI0p-lDPpz7INgCCDr0_NGLMnKvRBIh3mHNI8aonq1sfwI4VApK1WT81dQ_0DKWulPed0jENEvhgKRohQ-Eg44-z5jjN3KMAqNDg8znRcWNO6FMQWMe5VY2Bkva-Ta7OFxWkX1dcSMk7NbhttUc43A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیش‌بینی جدید قاسمیان:ورود عربستان به جنگ بوی آخرالزمان می‌دهد
🔴
قاسمیان سال ۱۴۰۲ گفته بود ‌اسرائیل ۳ سال دیگر نابود خواهد شد؛ بعد هم مکه را فتح می‌کنیم؛ حضرت در آنجا ظهور می کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/152093" target="_blank">📅 12:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152092">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af1c43edbe.mp4?token=j_QfmZVtLungIMDhyFv6a-ohedkFqUhW4uLfALkayvcWxWhV1R0SQZzJmCI2SjjKViSzUm-wY5pDhtzvWSWte_0asvTi-UZjrxCO4Hfk8oLV57EkOAPP3ZGFQquKXWwyCJBsH2gs0A2wyvdCWS4vS5a_UrRJplJaag2Rd0sVHkZ1bdqEmRw2OYkOU2IQVCrQEW915dAIPLAl0rkdcWE7Ysev0G05NAXZEGLBeJ0R-cH7Yyporl3ShBr2J_R7UwONcSemg3ok0kZO84IoBoIwmaDfnFsX2CaKOSEaujxL42McT-YfRNaL-o91enFqA6QfxM-QYtCJXpG1IiqAvrbhRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af1c43edbe.mp4?token=j_QfmZVtLungIMDhyFv6a-ohedkFqUhW4uLfALkayvcWxWhV1R0SQZzJmCI2SjjKViSzUm-wY5pDhtzvWSWte_0asvTi-UZjrxCO4Hfk8oLV57EkOAPP3ZGFQquKXWwyCJBsH2gs0A2wyvdCWS4vS5a_UrRJplJaag2Rd0sVHkZ1bdqEmRw2OYkOU2IQVCrQEW915dAIPLAl0rkdcWE7Ysev0G05NAXZEGLBeJ0R-cH7Yyporl3ShBr2J_R7UwONcSemg3ok0kZO84IoBoIwmaDfnFsX2CaKOSEaujxL42McT-YfRNaL-o91enFqA6QfxM-QYtCJXpG1IiqAvrbhRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه آخوند: بعضی از پایگاه های آمریکا تا ۵۰ سال آینده قابل بازسازی نیستند؛به نقطه رهایی رسیدیم/سپر دفاعی اسرائیل از بین رفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152092" target="_blank">📅 12:49 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152091">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزیر دفاع بریتانیا: حمله به فرودگاه ریاض، تشدید تنش خطرناک و اقدامی بزدلانه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152091" target="_blank">📅 12:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152090">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5u9-2jW4DedwbuDQPbIW-ES1wIGXgfAEiutbY5vj7_tjcVpk4CG9hBINWDp1gbxj7NK6a1yZKa0VbCo5_KSsf1-Ae6Q5_rnFwSc_QT1o2sBVETzzTUdOCW0YoizCxW0WyrbgkaTq-fWtp_O2owdfN6-_rK9sFNEGaYXKG4HCGoE0khEHb3ampHxj0iBQFC057a3b_lJ4OrY91rkJ4gBhLWreDAbNj8KZihJ1c63CmVFNo7L4sXpSie0xJTSpVXiAQQvN9Ueo3NgmTy0ybm_TVwcWZKiu-bC4u2UmNjwEPfxHlX_V9cP3df0D3qWoCZoW6vF7ZPqtoge-y2v4w12QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش شلیک موشک از بیدگنه تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152090" target="_blank">📅 12:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152089">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
گزارش شلیک موشک از بیدگنه تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/152089" target="_blank">📅 12:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152088">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bc3bacae2.mp4?token=lsCnf-bEId1rMoukVg7oaf7CtYtRFT-NYOY0IiJnUeZbTMvMW4MRPpa74w5YpthMS6-6ZtY5I1ZyxR7tinpEouzKqQteJFUQgvO6eMUrzsn4tN65msFP80k1vdMfsNOOqTESCgInW48e9y8S-gNvTcUP6sx13tvF-toC5526eZ4DIWKBs5QmXi9mzRCURwTOVRplVf1-SI_puWCHAF4P9JlHTYTo1tcGfMXRcrRJUk52zpJZBelsKcaL47cmKfV23yZPnhSTB7j5ARjOXDY19OiLwS7VD8Kbhymd3oMtlCCqRB9TTScXlM7mx6mTo1Vz4Wy9s4aGTC6x7z6DYQvCAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bc3bacae2.mp4?token=lsCnf-bEId1rMoukVg7oaf7CtYtRFT-NYOY0IiJnUeZbTMvMW4MRPpa74w5YpthMS6-6ZtY5I1ZyxR7tinpEouzKqQteJFUQgvO6eMUrzsn4tN65msFP80k1vdMfsNOOqTESCgInW48e9y8S-gNvTcUP6sx13tvF-toC5526eZ4DIWKBs5QmXi9mzRCURwTOVRplVf1-SI_puWCHAF4P9JlHTYTo1tcGfMXRcrRJUk52zpJZBelsKcaL47cmKfV23yZPnhSTB7j5ARjOXDY19OiLwS7VD8Kbhymd3oMtlCCqRB9TTScXlM7mx6mTo1Vz4Wy9s4aGTC6x7z6DYQvCAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویر هوایی برخورد یک ابرنفتکش عربستانی حامل ۲ میلیون بشکه نفت خام با دو مین دریایی ایران در تنگهٔ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152088" target="_blank">📅 12:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152087">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
رسانه های وابسته به انصارالله حوثی ها از دو حمله هوایی عربستان به منطقه نهم در استان صنعا خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152087" target="_blank">📅 12:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152086">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFHoQwAP179kvW79-iKGtLKALY3S1vrVxFX-Gwyq4JHz-t6SOtkxRgoD4k81mMd5tvK8IzqakhwC4l5U_VrCgRXtU7Ovl_Av339H3qpfJoMb_XmYwP8zjTBCLcQ7K1p4Wq6tP1dQF0UYdOLIIgM9rhxwQekT0wbV1ihqccBf7HNUjFpWqph1mc0NZXDDgmeI9uFud6iK4UdZYxviIP7yHFYCgXu_aKku84mi6DihK9Ni7z-d3xausy9_k8wXUIs-ps72dAgnia6ZVTu-ZS9ldf_XOowooRVyzU1gGwOCTbRKqCZJYDxhdhfDmU1NZMfNSaDtx3FllU5Ad9nrfqy6Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ظریف: باید با آمریکا توافق کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/152086" target="_blank">📅 12:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152085">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
عراقچی: حملات اخیر به تأسیسات نفتی، پالایشگاهی، انرژی و هسته‌ای ایران، خطرات جدی زیست‌محیطی ایجاد کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/152085" target="_blank">📅 12:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152084">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
روزنامه خراسان نزدیک به قالیباف: واشنگتن و تل آویو تصمیم برای شروع جنگ بعدی را گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/152084" target="_blank">📅 12:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152083">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
مسئول سیاست خارجی اتحادیه اروپا: وزرای امور خارجه اتحادیه فردا، دوشنبه، درباره افزایش تنش‌ها در خاورمیانه بحث و گفتگو خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/152083" target="_blank">📅 11:56 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152082">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
معاریو به نقل از منبع نظامی اسرائیلی:
نتانیاهو احتمال حمله به ایران را رد نمی‌کند
🔴
آمریکایی‌ها سردرگم هستند؛ یک روز چنان به نظر می‌رسند که گویی در آستانه حمله هستند، اما روز بعد ترامپ اعلام می‌کند پیش از انتخابات میان دوره‌ای حمله نخواهد کرد
🔴
تل‌آویو آمادگی گسترده‌ای برای احتمال تشدید تنش‌ها پیدا کرده
🔴
ارتش اسرائیل برای حمله پیش‌دستانه علیه ایران، آماده نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152082" target="_blank">📅 11:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152081">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3XPzKYxD5kxTca9pJd5sMqvN2C0BMUm0pNI8WjSS2THoqDWveas6B1x6Riyb43ExPZ26IyJ0JGciczZHDZi1JL2sxDvkC8jV3r6_FQCIve0sK-4kppSLKAbR-nydB_A-KZT0GRO7r2uIzLb4eVYa06Q7iY_yM2KWlPkM8-_RXIMkDh0whm3XeGlYfdpuUlikcDQjVqfdbCk5k3Xh1SV4xNTkYJd5VgMpKMkygT4y7zLg_ITaLop6JvQ8-kB9GbGXVKF0QUHO6Li40aqmITWE-KiANQqDY9NmolkEi3XIpwLW42tjm3_LBxqmGpHafdF5OsCxvmeRVsq_BWwfAx5UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای ترابری نظامی C-17 نیروی هوایی آمریکا، دقایقی پیش پایگاه هوایی الخرج در جنوب ریاض، پایتخت عربستان سعودی، را ترک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152081" target="_blank">📅 11:42 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152080">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b97936751.mp4?token=gCcJoAuwW3tPYCzj9DLws75MvsSM5WZiwJmdmivNNPM0pKWh9xMm5cx038d9ElTLu7XyFDzxv5DWdswFdgnilY7uigsPyl6-b_DPFl5YXI-mMswt7V2ZkusupkErfNLTg0SME8tB4B2wPiIHbQ-0lgJorCD75oCFm2bpigty09OT-VHnwazhOtdytFc7YlzfNLUOqg0DG8IxcbzDi7KrDCHBKVf2xhJaLiOmCumTP9V-i0S-c8esBFuXLVYv4CGTjvCirAP7D-6im0ve2eVlWyfOkYmAcU8gVeNiJ7cnApvaLCY8Ja9nD_pXKyTT-espetpLvow2-th1xcra18MYYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b97936751.mp4?token=gCcJoAuwW3tPYCzj9DLws75MvsSM5WZiwJmdmivNNPM0pKWh9xMm5cx038d9ElTLu7XyFDzxv5DWdswFdgnilY7uigsPyl6-b_DPFl5YXI-mMswt7V2ZkusupkErfNLTg0SME8tB4B2wPiIHbQ-0lgJorCD75oCFm2bpigty09OT-VHnwazhOtdytFc7YlzfNLUOqg0DG8IxcbzDi7KrDCHBKVf2xhJaLiOmCumTP9V-i0S-c8esBFuXLVYv4CGTjvCirAP7D-6im0ve2eVlWyfOkYmAcU8gVeNiJ7cnApvaLCY8Ja9nD_pXKyTT-espetpLvow2-th1xcra18MYYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طغیان رودخانه و سیل ناگهانی در شمال نپال
‏
🔴
ساکنان حاشیه رودخانه «بودی گانداکی» در شمال مرکزی نپال امروز (یکشنبه) به دلیل تخریب خانه‌ها و سایر سازه‌های منطقه بر اثر سیل ناگهانی، تخلیه شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152080" target="_blank">📅 11:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152079">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFoDaLzhDPWvfvTVb70ajAXjlNWLYdPYnX7kaUUGPwr_ioXa8Mm4L8F80RkwBnjjS7BgFcrEfBFMOuyN2psg0C67FyadtH5WhRloGs2ZKiziymXdYLhuzQ3gwFpt37tMfV6YZr4M7z5R95dJBp5S_Dhs4NP28An9_5lrRFCLCqGW1PyUd4cm9_kvB3Ogxx5PAnwkByClaEAtUmUlAzbn5NM4PWubAe_6Bj9SzdZYCuKb0N9JtFgVN493VS5ZRHW3o64faj7cu9mXz4mbgbZSsQ-Gr4t3naN5ouyme85yHGHXh2xS2mq3u_idPHe1Fy9ASeapiGiqYmVIICQr7-q5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هفته ملی کودک مبارک
❤️
[تصویر تزئینی]
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152079" target="_blank">📅 11:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152078">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
یک هواپیمای سوخت‌گیری هوایی KC-46 پگاسوس آمریکایی وارد العدید قطر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/152078" target="_blank">📅 11:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152077">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001aba2a7b.mp4?token=Tuno61f_XQD2W9dREqbKXa9uWdUBulPflmdOs3YPNHUat7badwiL8oXs-5kdHuO0Y2Xj5GXsJq8vFgRXSqAdsZCRleJFNWwxiYcotdrDonkpZ7oNkxSmN1xRCtAV2VoXf0daq60HhogRw9pT8x9eAKS1gvmj-OMJWVS0vYaz0ZOh9BExG2ZuKMOZgMjwLoQ9AvG21K2dpr23hfvE1RHpb22hRxKoiwFhCWTqgRogHtbFw7X2Jnp6O0NBVrYOZ2TPPVl1Scr5xisRuHX1WrD8cbj-U3k__g6Xk71pDejDWtWYtcu_hC1wwM5LmCB_hEztzrv5jzSGtAI-4fIoSbavWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001aba2a7b.mp4?token=Tuno61f_XQD2W9dREqbKXa9uWdUBulPflmdOs3YPNHUat7badwiL8oXs-5kdHuO0Y2Xj5GXsJq8vFgRXSqAdsZCRleJFNWwxiYcotdrDonkpZ7oNkxSmN1xRCtAV2VoXf0daq60HhogRw9pT8x9eAKS1gvmj-OMJWVS0vYaz0ZOh9BExG2ZuKMOZgMjwLoQ9AvG21K2dpr23hfvE1RHpb22hRxKoiwFhCWTqgRogHtbFw7X2Jnp6O0NBVrYOZ2TPPVl1Scr5xisRuHX1WrD8cbj-U3k__g6Xk71pDejDWtWYtcu_hC1wwM5LmCB_hEztzrv5jzSGtAI-4fIoSbavWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ذوق‌زدگی و اشک یک دانش‌آموز از دیدن پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152077" target="_blank">📅 11:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152076">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1585d3f8.mp4?token=eHFsFMqns-MEbO_50ag_vMKhpTp57amSaitUtuC3v7maGJHACsg2pV5ZPUD92XHZxXACqv2gStwguuNSIgjovenr9_3B8vJ0yKq16EyL43MirVjC7aAgr7UO1WmK3SziUYxyKSBoQC-LqxdFj2ppMFZ-VJTEzeGzC_Bpm4o2fhbe8l8Fj5_9NeT5QyihecZJJgno1Iz8_Wf3sYjpNBAZbTB2yHtGSNvfBHkdj8PhCd58kZnkT5NXu1iqkKUxVyqhtzFmfcN5WwC0Hn7FQnIZwkKR41g5EW8CCbCbZtgVsF2jZEBrMlwiq2zpef8laIODVjbEr3ZJcC_GsxuwIT2B4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1585d3f8.mp4?token=eHFsFMqns-MEbO_50ag_vMKhpTp57amSaitUtuC3v7maGJHACsg2pV5ZPUD92XHZxXACqv2gStwguuNSIgjovenr9_3B8vJ0yKq16EyL43MirVjC7aAgr7UO1WmK3SziUYxyKSBoQC-LqxdFj2ppMFZ-VJTEzeGzC_Bpm4o2fhbe8l8Fj5_9NeT5QyihecZJJgno1Iz8_Wf3sYjpNBAZbTB2yHtGSNvfBHkdj8PhCd58kZnkT5NXu1iqkKUxVyqhtzFmfcN5WwC0Hn7FQnIZwkKR41g5EW8CCbCbZtgVsF2jZEBrMlwiq2zpef8laIODVjbEr3ZJcC_GsxuwIT2B4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقتی پوتین، عوستاد و تحلیل پا منقلیش رو ک... کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152076" target="_blank">📅 11:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152075">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
بچه‌ها هر لحظه احتمال جنگ وجود داره و پشتش هم قطعی اینترنت
🔴
این ربات vpn داشته باشید و سرویساش قطعی نداره
💢
@VOXNET_BOT
💢
@VOXNET_BOT
✔️
میتونید با خیال راحت تهیه کنید و تو قطعی اینترنت هم متصل باشید</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152075" target="_blank">📅 11:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152074">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
لحظه فرار سارقان موتورسوار که گوشی و طلای مردم رو میدزدیدن از دست ماموران پلیس که اخرشم با شلیک گلوله متوقف شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152074" target="_blank">📅 11:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152072">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c374bd2b.mp4?token=nH1qLkNZuQGXYUGSvArrbHfKbQHmGXghYREasJWFhz71vQ6ztKye5SNUFaNHuv9PBBLJfinaK-qMnmarBnVKVNha6j4jYN3fm2vJ9sQtizlWVelZVQ75pyQafLsrdY6ko05ryq0RyDlf8xDnveQSfcQPFq1VzSqkDyC7iv6Jzny69O7ckFr13e059Wgchm0YkcFNMFVLwVrhQlTo834KWxtH47WKXy4W_5yrWku_dJmaK0uKp6qgruERq2_dgbRDph_fHNPfEWGbGQOQ1wcCri7e0y-O4wZLuBKtunte000bu2a3kTLsDuVtGRRE1DQV4NciRTVDZ9BlgX8JanNkLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c374bd2b.mp4?token=nH1qLkNZuQGXYUGSvArrbHfKbQHmGXghYREasJWFhz71vQ6ztKye5SNUFaNHuv9PBBLJfinaK-qMnmarBnVKVNha6j4jYN3fm2vJ9sQtizlWVelZVQ75pyQafLsrdY6ko05ryq0RyDlf8xDnveQSfcQPFq1VzSqkDyC7iv6Jzny69O7ckFr13e059Wgchm0YkcFNMFVLwVrhQlTo834KWxtH47WKXy4W_5yrWku_dJmaK0uKp6qgruERq2_dgbRDph_fHNPfEWGbGQOQ1wcCri7e0y-O4wZLuBKtunte000bu2a3kTLsDuVtGRRE1DQV4NciRTVDZ9BlgX8JanNkLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراین لحظاتی پیش در واکنش به پیشنهاد ترامپ مبنی بر مذاکره، مرکز داده یاندکس در منطقه ولادیمیر روسیه را هدف قرار داد و باعث از دسترس خارج شدن و اختلال در خدمات سراسری روسیه شد، خدماتی که شرکت‌هایی در سراسر روسیه به آن وابسته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152072" target="_blank">📅 11:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152071">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
تسنیم: طبق گفته بسنت اقتصاد ایران باید امروز فرو می پاشید اما باز هم این آمریکا بود که شکست خورد و اقتصاد ما کاملا سر حال ایستاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152071" target="_blank">📅 10:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152070">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8625d06a.mp4?token=ELgl3sYPd3Ta-7PTt0hQjGiBPkewLoGbRkhaFj8Qoa6kXpi2f6qcm-n0qT3T1sf4pJ4dz6xv15Nm4AFhSd6E1F_kze8UzBOJl1OSOO3AWP2D5yqyJE5toXsuGjW8pU22i6pACBTeTcU5jh883aux_Pc7wjEjNZORoT9RHWfRrU-FOEZFNN_8ijhlXFkrsfBxDK8517U2kAxofG9oWm4tekwo-6uMc1sZDE5qB2tQfGmkVCLI-RCbR7FR7j9n2a37TH6NUtApwEJkMg_dWzXBJpj0C0Hyq4eYhGMrNoHauiqKQ5vaxS6_DLQ4VyRm_31Ot3Wh1BlnKvQejSi9PBgLoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8625d06a.mp4?token=ELgl3sYPd3Ta-7PTt0hQjGiBPkewLoGbRkhaFj8Qoa6kXpi2f6qcm-n0qT3T1sf4pJ4dz6xv15Nm4AFhSd6E1F_kze8UzBOJl1OSOO3AWP2D5yqyJE5toXsuGjW8pU22i6pACBTeTcU5jh883aux_Pc7wjEjNZORoT9RHWfRrU-FOEZFNN_8ijhlXFkrsfBxDK8517U2kAxofG9oWm4tekwo-6uMc1sZDE5qB2tQfGmkVCLI-RCbR7FR7j9n2a37TH6NUtApwEJkMg_dWzXBJpj0C0Hyq4eYhGMrNoHauiqKQ5vaxS6_DLQ4VyRm_31Ot3Wh1BlnKvQejSi9PBgLoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای هوایی عربستان سعودی حملاتی را علیه کوه حبشی در شهر تعز انجام دادند، پس از اینکه نیروهای مسلح یمن کنترل این کوه را به دست گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/152070" target="_blank">📅 10:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152069">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325761006f.mp4?token=TrVtj5J9WjXW0yDEvTjelFqNgsoOhuzNb7BZ8445E_CdsdF5MpIeIxve288WXRz2heku7cTY-nHd8-ktFmKfJZQ6_PbEvstK9qouCj6-_Lut0njrYXkyk-VoRGDnSx_uQ5SDmo815cSpNoeE7bEMjQ6yqMGHAraij_wSaUcubmzUyxvDCW7_h-g9lfGn-Lk7EWKOEl3JGTux8sN0Zf96oMwO6v6N2DfUhQOVO88rS8gWBGkVbXAe0z13KWDkn_iOz3EYeZKnxCyipVP8cBjhN8Mrkg1eKWQ6dqQOk4aOZFPWfvUTj8a8Ayg9_8S2gHZiZQXRauz36-pMRbrCK-DDfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325761006f.mp4?token=TrVtj5J9WjXW0yDEvTjelFqNgsoOhuzNb7BZ8445E_CdsdF5MpIeIxve288WXRz2heku7cTY-nHd8-ktFmKfJZQ6_PbEvstK9qouCj6-_Lut0njrYXkyk-VoRGDnSx_uQ5SDmo815cSpNoeE7bEMjQ6yqMGHAraij_wSaUcubmzUyxvDCW7_h-g9lfGn-Lk7EWKOEl3JGTux8sN0Zf96oMwO6v6N2DfUhQOVO88rS8gWBGkVbXAe0z13KWDkn_iOz3EYeZKnxCyipVP8cBjhN8Mrkg1eKWQ6dqQOk4aOZFPWfvUTj8a8Ayg9_8S2gHZiZQXRauz36-pMRbrCK-DDfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خارجه سابق ترامپ: باید ایران را از درون درگیر کنیم
🔴
مایک پمپئو: در نهایت، فروپاشی حکومت نیز به کاهش قیمت انرژی و افزایش امنیت منجر خواهد شد و اتفاق بسیار خوبی برای آمریکا خواهد بود. این اتفاق باید از داخل رخ دهد
🔴
چه از طریق عملیات مخفی و چه از طریق حمایت از جنبش‌های مقاومت ایران، اینها ابزارهای مناسبی برای تحقق این هدف هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152069" target="_blank">📅 10:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152068">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ترامپ : زلنسکی بارها می‌توانست به این ماجرا پایان دهد و به توافق برسد. او همچنین باید انتخابات برگزار کند
🔴
جنگ روسیه و اوکراین اصلاً نباید اتفاق می‌افتاد. اگر من رئیس‌جمهور بودم، این جنگ هرگز رخ نمی‌داد.
🔴
زلنسکی می‌توانست به این جنگ پایان دهد یا بارها به توافق برسد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152068" target="_blank">📅 10:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152067">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ، درباره جنگ روسیه و اوکراین:
«روسیه می‌خواهد به توافق برسد، اما به هر دلیلی، زلنسکی تمایلی به توافق ندارد.
🔴
اگر به موازنه نگاه کنید، می‌بینید که از نظر تعداد نیروها، یک طرف میلیون‌ها سرباز بیشتر از طرف دیگر دارد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/152067" target="_blank">📅 10:37 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152066">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e14036ad9.mp4?token=tj8vVG-1PiprQnLXaus6YYK9JVqlkON02l4JcCFbY44PIpuAIEgGaBL7-l9gH31Is5UN8O3jKooY68rs8oPhUUHC2CZ8Nia4hQLgSsA6v8kL1yopJjrhkUn8yojKFGcCmClMm0M36XQ70WzaJM3x_kpcpqJ1dgZgIDrqBAS7xMAMsRvZceyTlY9Vrmje5Nw7BLBxYNChMWfBOq5MA7iPukJ-mC2i4pS5yQMJZWhyvM7vs9zm6xXXz55d7uixLyo8aqRpFIbTQXh5iNVmABNCbzuWqmgGyoMrHgjCKITvNaltgvF-ZkyvBDGMUVCmisKB4sHC7mJ7YLkCYCXgefFttA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e14036ad9.mp4?token=tj8vVG-1PiprQnLXaus6YYK9JVqlkON02l4JcCFbY44PIpuAIEgGaBL7-l9gH31Is5UN8O3jKooY68rs8oPhUUHC2CZ8Nia4hQLgSsA6v8kL1yopJjrhkUn8yojKFGcCmClMm0M36XQ70WzaJM3x_kpcpqJ1dgZgIDrqBAS7xMAMsRvZceyTlY9Vrmje5Nw7BLBxYNChMWfBOq5MA7iPukJ-mC2i4pS5yQMJZWhyvM7vs9zm6xXXz55d7uixLyo8aqRpFIbTQXh5iNVmABNCbzuWqmgGyoMrHgjCKITvNaltgvF-ZkyvBDGMUVCmisKB4sHC7mJ7YLkCYCXgefFttA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، درباره جنگ اوکراین: «ولادیمیر پوتین به‌شدت خواهان دستیابی به توافقی برای پایان دادن به جنگ است.
🔴
ببینید، پوتین مقدار زیادی نفت را برای عرضه به بازارهای جهانی آزاد می‌کند؛ خب، این اتفاق خوبی است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/152066" target="_blank">📅 10:36 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152065">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ: شما نباید اجازه دهید یک فرد کاملاً دیوانه به سلاح‌های هسته‌ای دسترسی پیدا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/152065" target="_blank">📅 10:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152064">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
منابع  یمنی: عربستان سعودی از دولت چین خواسته است تا رسماً با صنعا برای اعلام آتش‌بس بین دو طرف میانجیگری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152064" target="_blank">📅 10:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152063">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1db8057bec.mp4?token=sdQDbXoYUMHlCqjGxlDnu6OWuNDT7XFbWwxbnki0CD47ZXVLZAb2v12O6dCurIgb20u_zVL-I3yrgX_a29T2jm-M67aep5pz0gf9qMuqu3F17S0uoYqe1bVmSEcJL49TvD3bBeVZGQMnRkrTXCvYaOvv-_KBwJnim3dS0XuYUXLv9Eghx3aLTnlJW-P1fyrVzqnLUdZAF2-32oZLfXn4NCWhI66K2v4NRZ2nMoMbVOwQ25dRMSQMqQzvJJb7OCZk1rhsmv0RMKmCntncFNGbBk0CAMfzCsK-CtKNttWvDVeaksBVGny0oh0QGfjRXJLFguODJQx6ygKj8ahuseWQIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1db8057bec.mp4?token=sdQDbXoYUMHlCqjGxlDnu6OWuNDT7XFbWwxbnki0CD47ZXVLZAb2v12O6dCurIgb20u_zVL-I3yrgX_a29T2jm-M67aep5pz0gf9qMuqu3F17S0uoYqe1bVmSEcJL49TvD3bBeVZGQMnRkrTXCvYaOvv-_KBwJnim3dS0XuYUXLv9Eghx3aLTnlJW-P1fyrVzqnLUdZAF2-32oZLfXn4NCWhI66K2v4NRZ2nMoMbVOwQ25dRMSQMqQzvJJb7OCZk1rhsmv0RMKmCntncFNGbBk0CAMfzCsK-CtKNttWvDVeaksBVGny0oh0QGfjRXJLFguODJQx6ygKj8ahuseWQIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : «فکر می‌کنم تقریباً تمام اعضای حزب جمهوری‌خواه، طرفدار جنبش ماگا (MAGA) هستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/152063" target="_blank">📅 10:22 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152062">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c93a9235c.mp4?token=qp3ao2mILdY9OzqQkkGWpHzRwQ337wMU_t_0RR3uAc9lQXvWwRCzcwU3WukrGxY8dPtNoDDbqY2VM3THCgn8g9bp_z14oKphBdgF0EjxIgV3JSN9JrvWuKa6N3YI0YJUSGXd7msETJgItC0Uoi7xNhRvOPi7B1MoUlF8bzWqfwh2NxKo4yTBoTPcSbqPm6W9O0VlQe9496uDHanBH85QoBKbBFVxF1OdAzlMeCvC0Zx-87giOyNk7IX4dfxYzdK9Jez2K52w-1bMKLAwB1sYRs--J4X7uYELkR7nMZnGmb-bT1RPeienFGrUuCdH4gyLrpSMbhwQxqNmHXpgnMwVbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c93a9235c.mp4?token=qp3ao2mILdY9OzqQkkGWpHzRwQ337wMU_t_0RR3uAc9lQXvWwRCzcwU3WukrGxY8dPtNoDDbqY2VM3THCgn8g9bp_z14oKphBdgF0EjxIgV3JSN9JrvWuKa6N3YI0YJUSGXd7msETJgItC0Uoi7xNhRvOPi7B1MoUlF8bzWqfwh2NxKo4yTBoTPcSbqPm6W9O0VlQe9496uDHanBH85QoBKbBFVxF1OdAzlMeCvC0Zx-87giOyNk7IX4dfxYzdK9Jez2K52w-1bMKLAwB1sYRs--J4X7uYELkR7nMZnGmb-bT1RPeienFGrUuCdH4gyLrpSMbhwQxqNmHXpgnMwVbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، درباره حمله حوثی‌ها به فرودگاه ریاض: «با محمد بن سلمان صحبت خواهم کرد.
🔴
آنچه در عربستان سعودی اتفاق افتاده، قابل‌قبول نیست.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/152062" target="_blank">📅 10:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152061">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7603ad8bf8.mp4?token=QSPZFGl5bnp9mxfUouMMazcP7sxZfnPnxic0sE8KVoKlmKnwwLPc8Z137DPAwqkiZDZxxMmvL76517Y4ZN-UO5Hw3XKl7BHj2yBqb9AtX0b5gYRncbrUvlgAvVS6dh5qwiG3WZ5TaFDSQvJKpx4RBsP8ETnqtuLl09zC9_r4mSFhykJXXv0zAdO7LNJP7YeJR2xL7HUc05TWCyLRxUjnFVaVyCqPGxix9D5rSTyUH_3sZUEaVmLoeygYE7kFOXrzBUsJEuYHrCZBECUjMgxdHgXt2RJyjFZM1ExUdorGBYyERvnNxhjp5OWDZ5wEsjVPZLYzeoPobiiNZ6wfFrXNUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7603ad8bf8.mp4?token=QSPZFGl5bnp9mxfUouMMazcP7sxZfnPnxic0sE8KVoKlmKnwwLPc8Z137DPAwqkiZDZxxMmvL76517Y4ZN-UO5Hw3XKl7BHj2yBqb9AtX0b5gYRncbrUvlgAvVS6dh5qwiG3WZ5TaFDSQvJKpx4RBsP8ETnqtuLl09zC9_r4mSFhykJXXv0zAdO7LNJP7YeJR2xL7HUc05TWCyLRxUjnFVaVyCqPGxix9D5rSTyUH_3sZUEaVmLoeygYE7kFOXrzBUsJEuYHrCZBECUjMgxdHgXt2RJyjFZM1ExUdorGBYyERvnNxhjp5OWDZ5wEsjVPZLYzeoPobiiNZ6wfFrXNUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : «ما با حوثی‌ها در ارتباط هستیم. باید ببینیم چه اتفاقی می‌افتد.
🔴
کاری که آن‌ها انجام دادند، بسیار بد بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/152061" target="_blank">📅 10:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152060">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5fdbe62eb.mp4?token=rak8FTdWHAz8Uz_9ycoihJpc2MDLLBgMpwCjBlFvFTqAr4nrU4czPA8e4Tv_FyePgPz1DyDZ3AUSSMfQTs7RS05Toph6VO8EnFuDqRrZKHYzATkq_wBRmFB-kkAU8xv-e3qMXs87sjhq563ULONogRxo_Gx3cDI4J5tovcJLwv_dzMWAnwqxpIUgKxuU_NVucBbW78bonQ_KTLhc1aIm9VU3ty8yNp787U4-gGHJszuCaGEOyBtV09liDQwxPVQAWxoUOHqS6tUH1H7UqvyqW7O0WcAsuqyzRlCf7xsjGRZty1jKMpCG0FPJ5QiQ2bXQhHPOpFZkzJmUlzRdYqaqyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5fdbe62eb.mp4?token=rak8FTdWHAz8Uz_9ycoihJpc2MDLLBgMpwCjBlFvFTqAr4nrU4czPA8e4Tv_FyePgPz1DyDZ3AUSSMfQTs7RS05Toph6VO8EnFuDqRrZKHYzATkq_wBRmFB-kkAU8xv-e3qMXs87sjhq563ULONogRxo_Gx3cDI4J5tovcJLwv_dzMWAnwqxpIUgKxuU_NVucBbW78bonQ_KTLhc1aIm9VU3ty8yNp787U4-gGHJszuCaGEOyBtV09liDQwxPVQAWxoUOHqS6tUH1H7UqvyqW7O0WcAsuqyzRlCf7xsjGRZty1jKMpCG0FPJ5QiQ2bXQhHPOpFZkzJmUlzRdYqaqyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، درباره حمله حوثی‌ها به فرودگاه ریاض: «آن‌ها توانایی دفاع از خودشان را دارند.
🔴
ببینید، سعودی‌ها جنگجویان خوبی هستند؛ اما به‌نظر من، این حمله اقدام وحشتناکی بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/152060" target="_blank">📅 10:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152059">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7caec3f32c.mp4?token=gxHN5NlHV2rhkel8nSdjxtqYGIHEXiiRUsv3MErylIdnTVq3ll6UlHMmI-JvvL8iwFx48OiwhxXljM_eWcBisdBr64xF-V1KNm2hFV4n7k_rwiBJJqdMfYQxTj6PtZYWs4uhG2ZV65-clOfd0C8N5yt4WzImFy6WHjVw9f8rdvd1d6iq0SCdkkrm2R8oD8gtimMGbakaujXGR0O7gTffIVv4_sm9WmG6gEONiQTO30Lg90Kv3uOms2a_j7ugataGWz3jXSzgGxzrRQrA7vwrq4nv703unIkDwAxVak7J8IS18zVgbZGJeq9hnUySAkOz94huJktT-dyDZyM7k8hRCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7caec3f32c.mp4?token=gxHN5NlHV2rhkel8nSdjxtqYGIHEXiiRUsv3MErylIdnTVq3ll6UlHMmI-JvvL8iwFx48OiwhxXljM_eWcBisdBr64xF-V1KNm2hFV4n7k_rwiBJJqdMfYQxTj6PtZYWs4uhG2ZV65-clOfd0C8N5yt4WzImFy6WHjVw9f8rdvd1d6iq0SCdkkrm2R8oD8gtimMGbakaujXGR0O7gTffIVv4_sm9WmG6gEONiQTO30Lg90Kv3uOms2a_j7ugataGWz3jXSzgGxzrRQrA7vwrq4nv703unIkDwAxVak7J8IS18zVgbZGJeq9hnUySAkOz94huJktT-dyDZyM7k8hRCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گفت‌وگوی خبرنگار با دونالد ترامپ، رئیس‌جمهور آمریکا: خبرنگار: درباره حمله مرگبار حوثی‌ها به فرودگاه ریاض چه نظری دارید؟
🔴
ترامپ: به‌نظرم وحشتناک است
🔴
خبرنگار: آیا آمریکا را وارد این درگیری خواهید کرد؟
🔴
ترامپ: خب، به‌زودی متوجه خواهید شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/152059" target="_blank">📅 09:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152058">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuA2Kt2pPPFugdyrEFeDHUHaOvMD0aJZGiqtn5fnEE7HuFNh1O4Lu6xQ0a9ZDZrCt99hWS44CjAodN-tTaFAH19nYGISnTE-6uETBQl4lfUsI9PM1T7dcwzu_uVAWIZx7OZhspqazuh7J3xHSmBd44YxQf3iwgAiPDCpK4UsopHJEa5D-_lZ3LRqBL2rernxItgM-Lmc_r669KDZcuM5cJimkKsvlKFhHl9dixm_hyy4ry2uKIlflZ1k918UJQxI0huVYDdD7D5pqf-9jeU5uSzylkvdgnBTlS9p0Zqw__-c-7eBxoJxJGVXUqcQ1fFwGL27bZ6s689J2bwTcHjeWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / روبیو: یک آمریکایی در حملهٔ یمن به فرودگاه ریاض کشته شد
‏
🔴
وزیر خارجهٔ آمریکا اعلام کرد که در حملهٔ دیروز یمن به فرودگاه بین‌المللی ملک خالد در ریاض، یک آمریکایی کشته شده است.
‏
🔴
پیش‌تر سازمان هواپیمایی عربستان اعلام کرده بود که «در حمله به فرودگاه ملک خالد، ۱۲ نفر کشته و ۳۰۹ نفر دیگر زخمی شده‌اند».
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/152058" target="_blank">📅 09:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152057">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
کان نیوز: نیروهای تفنگداران دریایی ایالات متحده طی ۲۴ تا ۴۸ ساعت گذشته، مشغول انجام تمرینات نظامی با شدت غیرمعمول بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/152057" target="_blank">📅 09:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152056">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
مدارس ریاض غیرحضوری شد
✅
@AloNewd</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152056" target="_blank">📅 09:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152055">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/biWWLcf96hbFcPyHQxv-poequs89G3hwslXqGnIHbeAGSt1D5mBW46DLiyNWtte4ozvEXYkiDnIOaVte3CsQUuRObUDGIPfqXh9OKfAqwSlbdAcnAXQuAxZYL50e7fKofXQaDBsuVBMvytIfrWGdeUFk9zyfcSAjRxcEfn6LzYB-DcdZz30RDtPaizBx6z2lhNbaRRnswoI9zGvQ6pHmAVYqZC3xTznWmKBU8haDw1XFZfQEbG7NM5zwd9BYMgMkyy2XasS1AxVMuUvUmt_DTHhq1VsX7fw5HbxNiOHVNq-IeROjtgl0W6uLn4qJuMnG8lfDrd2kuqAixr0IVDr1aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فروند هواپیمای سوخت‌رسان KC-135R/T متعلق به نیروی هوایی ایالات متحده، از مناطق مرکزی آمریکا درحال عازم به خاورمیانه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152055" target="_blank">📅 09:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152054">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-JabDyOBUHpdSuU2k1GwRe33aOupumgkK7opAq4E4ECkD0MtUwh8KNWTw5WDl0XZC1JKnjxWLAU0N5BTwyAm1B_925plv7Hr6ljS4ReQkcfgNi1El2ZAhhy_V3FLv_ey-0WYmwtfxUnl-Tmfeoaoljqz67PcRrGmxASXSAM5F5xt29_DuvVoDtQr_xTzXoVFtvPNB1_98mhz-T5PyYh0mG-VBmql36wfS2wW8sQo72BtgXB6byRuw__JO6gVby2kj0efH0fsaT4AxAO_6JAqhpk1UyJrzoZ4wzyxPKYnYVyHce9FxkcCIRGTzpthMoEoBzgyWD8tM2iW6Pbp3j4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان سعودی کشته شدن ۱۲ نفر و زخمی شدن ۳۰۹ نفر در حمله به فرودگاه ملک خالد را تایید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152054" target="_blank">📅 09:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152053">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
به گزارش میدل ایست نیوز، دو هواپیمای عازم ایران پس از دریافت‌نکردن مجوز ورود به حریم هوایی کشور به دلایل امنیتی، به فرودگاه نجف عراق بازگشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152053" target="_blank">📅 09:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152052">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0528822587.mp4?token=sj0ePd6ejEhfs9X1W93MO0JkuHIriExoV1bYCnRGVm9BhgsqzufrIFHPofF53Kdz4_NHhLuaXwMFX0RpGaUcofqkDxzmWnFYThZxa6Rw70D9EqzOnH1cI5dXdpTa4I7kud4eR9-qJxrXdAnugMRzvykllsYus2SjeZcTnxHex7HbwaE7zgv_VpQuvo5KvfsVB0UkNXwi_wUrB_WWVPjm2Fe3kMF_T6FH5FeohE_4ph0yPI8vqdrrlwqXC-WD-4LCSAeP3Yvho8kF65LFBrge9-vX57tV3xzcBHzKbQ7OZgn-uYzjED62o41-w43qFGEfBoNZd51s-n4VY1Y3JBeg7Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0528822587.mp4?token=sj0ePd6ejEhfs9X1W93MO0JkuHIriExoV1bYCnRGVm9BhgsqzufrIFHPofF53Kdz4_NHhLuaXwMFX0RpGaUcofqkDxzmWnFYThZxa6Rw70D9EqzOnH1cI5dXdpTa4I7kud4eR9-qJxrXdAnugMRzvykllsYus2SjeZcTnxHex7HbwaE7zgv_VpQuvo5KvfsVB0UkNXwi_wUrB_WWVPjm2Fe3kMF_T6FH5FeohE_4ph0yPI8vqdrrlwqXC-WD-4LCSAeP3Yvho8kF65LFBrge9-vX57tV3xzcBHzKbQ7OZgn-uYzjED62o41-w43qFGEfBoNZd51s-n4VY1Y3JBeg7Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی: بارندگی‌های امسال سدها را پر خواهد کرد
🔴
پاییز و زمستان امسال گرم‌تر از حد نرمال است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/152052" target="_blank">📅 08:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152051">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا اعلام کرد که گزارشی را از سوی منابع نظامی نامشخص درباره وقوع حادثه‌ای مربوط به یک نفتکش و نیروهای نظامی در دریای عمان دریافت کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152051" target="_blank">📅 08:53 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152050">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f1bb1bad.mp4?token=a4OMrEPQ_GDdZEahdNeo4nmZPto8sZVH6SULuN24g8YHIhBhZAPrXPkQzEeymv3YfXW467KOKoCHtNAeEE7eMHPyCWv_1fFbiaSBmIYMRpGE45U9-Q8VbKU1HgwJ9npHHuPqwtPur2K083il3UZdMB3UgXZVCkYNnpCjXIpAKJLlB8EujdAGw8G_-fLI3x_c29M4P8XFh4zBioVaoCUoXkxJOZty7vzeIEwAadSWnPPc30za2BilvvxpQj2Oz9OTjcRzbuBmlw3OEE9cIh1zPupp7ZAVM9uhxh49Fy8F-RhqEyS3VMFktTi5BiHkr3mByzQcLm6WUke78MNNaDKP-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f1bb1bad.mp4?token=a4OMrEPQ_GDdZEahdNeo4nmZPto8sZVH6SULuN24g8YHIhBhZAPrXPkQzEeymv3YfXW467KOKoCHtNAeEE7eMHPyCWv_1fFbiaSBmIYMRpGE45U9-Q8VbKU1HgwJ9npHHuPqwtPur2K083il3UZdMB3UgXZVCkYNnpCjXIpAKJLlB8EujdAGw8G_-fLI3x_c29M4P8XFh4zBioVaoCUoXkxJOZty7vzeIEwAadSWnPPc30za2BilvvxpQj2Oz9OTjcRzbuBmlw3OEE9cIh1zPupp7ZAVM9uhxh49Fy8F-RhqEyS3VMFktTi5BiHkr3mByzQcLm6WUke78MNNaDKP-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام: یک کشتی باری را در تلاش برای عبور از محاصره دریایی ایران از کار انداختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/152050" target="_blank">📅 08:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152048">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
تانکر ترکرز: صادرات نفت کویت دوباره در حال کاهش است
🔴
تانکر ترکرز می‌گوید افت دوباره صادرات نفت خام کویت احتمالاً به کمبود نفتکش‌های عملیاتی مرتبط است؛ چند ابرنفتکش شرکت KOTC در حال تعمیر هستند و حملات اخیر در هرمز نیز به ناوگان این شرکت آسیب زده است
🔴
به ارزیابی این مؤسسه، کویت برای بازگرداندن صادرات به سطوح بالاتر ممکن است ناچار شود از نفتکش‌های شرکت‌های خارجی استفاده کند؛ آن هم در شرایطی که هزینه حمل و بیمه نفتکش‌ها در منطقه به‌شدت افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/152048" target="_blank">📅 08:43 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152047">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbzXWKijO82krF2YFD_CTGIQ378IBM1gqO4cohL7wXfagcd2TZFjdmy2eqa668-1VTwbof69pzum8UOAgRS6_7b6B4fSJNVLQUKozuzsf7jlaRJ5x5r3dCfFQGlJlrXiDvjIK_tuSxYBLRMhyTW_z1Uv1fFkDastl7DtpN8_fMl3EefAIgf-SRC2G2rfwOUv2Ebwz__LnmhUsbraiqLWbx_6YrIsJuRzNVTokhVrpNL5iU1Htbb1OfiQVaHAtlYBQbK7p7Def7Tam1_j2MetBP7LZRIqumHJRzzJBuS8b4erE3l56eU66zYHOLLQrWrheE3g_ZfBGuDxbGtbm7Gu_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ائتلاف پیمان مکه:
ما با قاطعیت پاسخ خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/alonews/152047" target="_blank">📅 02:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152046">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04243f9871.mp4?token=HSs2zPsMLbqJbBSYv2jFtdrQS8cAr7JT2WX1vn8fQBK0nQmYRCbklB0msjmxSfwLFhcvfr6nwTt3-6Itv5-jlh28nN6JAeWKk1ZwKIjKCBchAqsKrQRO1_Dsm-ewu-SkUfUCLZR1yyU-sgOfeXoNTV1TR7aV7b-mBE-7ODFPCWz61x4M-AzLggqsAaxKCWhKuxCO1G54Sj5Ow5X2fQadZ003dpaZh2Vg6i8ugNmNWcM8JGqPi417S1-wKm31cjct88I-Q_cM9upngwotKOK75Ggv_sqUBq9NHN1Iqea07tXjnxhwgG-tXxNGG-q2BMhNywRzsVEkLYqcR39HSzhfSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04243f9871.mp4?token=HSs2zPsMLbqJbBSYv2jFtdrQS8cAr7JT2WX1vn8fQBK0nQmYRCbklB0msjmxSfwLFhcvfr6nwTt3-6Itv5-jlh28nN6JAeWKk1ZwKIjKCBchAqsKrQRO1_Dsm-ewu-SkUfUCLZR1yyU-sgOfeXoNTV1TR7aV7b-mBE-7ODFPCWz61x4M-AzLggqsAaxKCWhKuxCO1G54Sj5Ow5X2fQadZ003dpaZh2Vg6i8ugNmNWcM8JGqPi417S1-wKm31cjct88I-Q_cM9upngwotKOK75Ggv_sqUBq9NHN1Iqea07tXjnxhwgG-tXxNGG-q2BMhNywRzsVEkLYqcR39HSzhfSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت جنگنده های ارتش اسرائیل بر فراز سوریه
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/152046" target="_blank">📅 02:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152044">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/py_JITd7UoKEmoBIBTdM5flaUExiA50N5fZHGmHRlHV10eR20XbtrEFz3t7sx1L452yldiFv_3oYVVdwll-gHmEn19X4ZzX3vE_7vWEqdBpdBIibJ3TXE7VAgyQWPGtpV8fzm4S3d9Y_2nrPYV4K5uYzx7swsmOJdQryzp6kyzToVvwp8Tsfci3O-ABwAq0X4oF2vjcaRwecMFe3wFY5AygRi5PPd8Q5dCe6gqxuGAyks6J3Jx5Re8wbZBgmMF3Hy9Q5GDrS5noPf9JilohueOWHSNiRbSwZ6QUfWWnNmV_LXOi2fgmPOur2WP7KW_vdi0t812G14hgJ_K4kzs7jwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l0ACZqBF_ZkfwUN55u7zyCnxfAU6_1u0fqdMaErImj3AfxEZc7ttna1HZD-CZdLWRIm0beMhN3zqcGQ-ghGxNoRHB_X32IPVBb_BPKvV-KVOE4vB_msRKt_OQMPRZG5_BlogkR7uljoQpan30XlUTJEp-A8acTTLufCvEN1-pxu4Nn1FZOh9yBkpRcFCgHAN7jg0nKISio45N5WdSCdkcRhqa7Lw6hZQQALzpQK89fyO_MADBA35kHLAGWW-N_vCE8KtmTBZ-sbgjPuX3wZ2AujRdFUOX8CnM5ZT81nVLuhMiqnJQbiyDG2_MZ83UMnxXtGS7XYgkBzqbAyTvXoTXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
تو سایت آدم و حوا منتسب به حسین یکتا از فرماندهان سپاه، برای دختر بچه های 13و 14 ساله برای همسر پیدا کردن پروفایل باز کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/alonews/152044" target="_blank">📅 02:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152043">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q89us4JNb7oP7WM87klg43aGrP3i1EnVbNjL1o982kkq_lH9fLOeB99illFVzvcPyrkq23RI_ttplcHdld4grYMv6eBfPyFf3j3rJcLIjI90dJXVEPd_o5KcxXpnSuDvy8TyapRyp7FxJc9vxya20HFpjSRi-LHWMleFSMhpQ4YsH4shoJQt2O7LEiFkrlorDZPLG2m0Qk268oF1uvoi9jxYJ1McdiETOLTYvC4_FvjNPRH8bS_yNoZIWPKTv0OhuKIV1XJOqnKDVtPLXUW0kwkCIBHF0xTWJkYKyVLs8-UYCUb2sUkAgoYqYo9OJNA9VZf8eJG2EG_gFUGC44MInw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: ج.ا حداقل ۶۰میلیون طرفدار داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/152043" target="_blank">📅 02:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152042">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZGAoJPH0NVET9jBK0LrmsVXj2WhTdJeG61lAv2xbM8nlXDOCNWzrI46xM-aya2ED335_J7NrbPQot3a4tOEKo3sf9ehSsPigw4L9mAONgI5rxFpL-NfG38d6GYRR89hnVtz09j0msYjD10NP8KhRiYar8V5oz2fbidRdxhU7WLDKiW9I2H-cdibSyOsQBXjrAoK0-ZkFrdWTJU599cuSZHpoo15dtTlo_5nvjxxgUpz5WOwSY_BE08YM6ZSnSeZpdrBbAwrWTMeRtMSx8AkGhK9Z0P8J6yUdf2jWKdWm2oTcFtrdAESHVRj-ARJCm_m2bWL8riZNnLaijLW9QOoIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این تصویر عجیب در ایتا و روبیکا وایرال شده و نکته جالب اینجاست که در طول ۴۷سال حتی یک فیلم از تاریخ ایران قبل اسلام ساخته نشده اما اکنون از همان تاریخ غنی درحال سواستفاده هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/alonews/152042" target="_blank">📅 01:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152041">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
بچه‌ها هر لحظه احتمال جنگ وجود داره و پشتش هم قطعی اینترنت
🔴
این ربات vpn داشته باشید و سرویساش قطعی نداره
💢
@VOXNET_BOT
💢
@VOXNET_BOT
✔️
میتونید با خیال راحت تهیه کنید و تو قطعی اینترنت هم متصل باشید</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/152041" target="_blank">📅 01:51 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152040">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h81OX7BiQXbOfWtRXj4Hw-g1tvELX_Cbw4hXhNqY75I7cC9HddBNdp9A_K0lp3OUt783tVAdmyKRJdTmWBUunUpX2zQ0z2w5Z0Nr4CTz2_KWsB1Opo6LU3P15TrRw8gVKccopDwBpzDxProw4-PAYl6DjM_-Q3juE-SVqFr8CJ5cRgMLrdTAHGUMuqpZHEE8wH05WS6NaAxjHAk9ivlkIGsziDs_1ITIGG939ONC2LGtoj7S8y47hfL2d69SbCCbN_LkODPQHEWmanCrSKiHZ31zF2DcysgH_Jo4DtgQx2zxXbsD-JOMFMpAf4K0cHSlHzbNBsCl5y9cg9hAAZyFmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور: روس ها به دنبال این هستند که ترامپ دوباره رای بیاورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/152040" target="_blank">📅 01:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152039">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EP-2bqlmveIxmTqIjNUQY-PbA5GwYM6IGOBZKign75rVbeKPLW32XbLDBem1eENuehSDVb78inE77zFPyLx51bTpGDwUWlX-fYXDIbApI7zwwLlYhr6XZ4rG0vJ6x4Dmvoa5AqNAjop4Mr5PMm9XaMVRqE0ucuyT-aChFE0M3nvg0JU6L5jQU8ocmHhP_y8eWz-1-yx5_auXY0RMJDYJBX3bTI0YLlvUsQEEqp8UxCqeVU8fC6xOO3wk8ZMPR7n_Wwy7HKAe2Boo-2BeL0XOu72iscTv4rwml3JYOouKwzOdWhLvQYaNqkpmqBzqArwFkb2y7jc5kYK0wCjksDthRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: ایران نمیتواند سلاح اتمی داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/152039" target="_blank">📅 01:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152038">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
فوری/طبق گزارش مردم محلی، در بیست دقیقه گذشته، جت‌های جنگنده نیروی هوایی اسرائیل از پایگاه هوایی تل نف در مرکز اسرائیل و همچنین از یک پایگاه هوایی دیگر در شمال اسرائیل، پرواز کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/alonews/152038" target="_blank">📅 01:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152037">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
اگه یه کانفیگ میخوای که تو قطعی اینترنت وصلت کنه حتما ووکس رو داشته باش
👇
👑
@VOXNET_BOT
👑
@VOXNET_BOT
✔️
با خیال راحت تهیه کنید
✔️</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/alonews/152037" target="_blank">📅 00:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152036">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6hm2-l7QIvkb-AIfwcO_XJwDvSdHgJa9hLpfxmoytpo1c29Mkz7UbnNrZFC9FA1MmOdngcjcOMbKjyC2LaLK93HSo3FKi9FI7ygTGxfadKivUAje2ai06CYcTuOkI1eq6zkNg2noAj4GblR1Jxoh5kYh-Myl2FXuRwOmBUn4Yxc20WLhtjfXMbC1lbb6JNOFmUWfKry0tfquGIKLu7VinVdzVyR8bpPLs7VzzwczvGrktuuykRifJbdaFzeMkiPWaHLVCs4vca6tFzUw_ciruymYqs0YfQA5QpjkORh0GbHlKnubIsuZkdaeQ_C4_HZjAR5_1nK-0rk8Ws1tog4fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: باید به پوتین حق داد؛ او هم بر اساس منافعِ کشورش عمل می‌کند!/ اشتباه از ماست که «روسیه» را شریک راهبردی می‌دانیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/152036" target="_blank">📅 00:41 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152035">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/595730e6c3.mp4?token=vsi4t-0AY4fqFvKwVis53u94t6L2M-L9Rkc1nUzeNEU3qqcrzRfMsKebjpjwwOY5BHHVcRcdKMtymkqlqGIvJlUQpS-TbAJP_p_elVNCFaB0yCZCSVvrI_XE7UeaGVz8TYyjEPfqSuNps9o308kdTCRGcIk2Ac-bK6IYtq_7Eon5082bVgJ7SSmFEOiKJTZxz4bBKGlVh3lY7hbkR5CNJl9InR-D-Z2ci2dOURYQR8rI77w8oy03mND2ChNjNW4QfQv5vCIzvPptUryPkXGF_TxbflD0RJVsZtUVjsNtXiYjZ4XtLUQ00aL5HO_BIeL62gtKSM7f5TeimPug-H-HXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/595730e6c3.mp4?token=vsi4t-0AY4fqFvKwVis53u94t6L2M-L9Rkc1nUzeNEU3qqcrzRfMsKebjpjwwOY5BHHVcRcdKMtymkqlqGIvJlUQpS-TbAJP_p_elVNCFaB0yCZCSVvrI_XE7UeaGVz8TYyjEPfqSuNps9o308kdTCRGcIk2Ac-bK6IYtq_7Eon5082bVgJ7SSmFEOiKJTZxz4bBKGlVh3lY7hbkR5CNJl9InR-D-Z2ci2dOURYQR8rI77w8oy03mND2ChNjNW4QfQv5vCIzvPptUryPkXGF_TxbflD0RJVsZtUVjsNtXiYjZ4XtLUQ00aL5HO_BIeL62gtKSM7f5TeimPug-H-HXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
حرکات عجیب ترامپ در سخنرانی امشبش
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/152035" target="_blank">📅 00:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152034">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d7a290694.mp4?token=I2rDGTYBCwKQEVyZuWZzhVe9Qaem8PL8Lt2B6ZN-V7VDYu_3CVXxcTAPeZkIqqMKF3lg1squqhF157MLgrerrqMCGhoX_lZvT2FqpTJhN55Yq_Wmj7NzO2e9HxZSAby33MXYUi5y4b6QG5C7QhuUYk3PljaLMbyaLy3ZthYTV0v7HZpFlEpcWLhRP3yGPlFTe2kiYssH8JwkZZJcZe0ECJwsehad2ARQdvERFjL1MaYm_45yxNFhaBt1NICjkB7I8A7JzXMYRB3zSwXvhhqLtPTQsFynnBnbWMBqLnIqfuB7vmdu6AmHhaBwn3w_Jl5FZUDJX-eXRKfNQbydBHSn5Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d7a290694.mp4?token=I2rDGTYBCwKQEVyZuWZzhVe9Qaem8PL8Lt2B6ZN-V7VDYu_3CVXxcTAPeZkIqqMKF3lg1squqhF157MLgrerrqMCGhoX_lZvT2FqpTJhN55Yq_Wmj7NzO2e9HxZSAby33MXYUi5y4b6QG5C7QhuUYk3PljaLMbyaLy3ZthYTV0v7HZpFlEpcWLhRP3yGPlFTe2kiYssH8JwkZZJcZe0ECJwsehad2ARQdvERFjL1MaYm_45yxNFhaBt1NICjkB7I8A7JzXMYRB3zSwXvhhqLtPTQsFynnBnbWMBqLnIqfuB7vmdu6AmHhaBwn3w_Jl5FZUDJX-eXRKfNQbydBHSn5Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به هواداراش: این فوق‌العاده است. من می‌توانم احمق‌ترین حرف‌ها را بزنم، و شما تشویق می‌کنید.
#میدان_انقلاب
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/152034" target="_blank">📅 00:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152033">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ترامپ: شاید نام یکی از اقیانوس‌ها رو هم عوض کنم. ببینم چی میشه
به این فکر می‌کردم که یا اقیانوس اطلس باشد یا اقیانوس آرام. اسمش را بگذاریم اقیانوس ترامپ یا اقیانوس آمریکایی‌ها.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/152033" target="_blank">📅 00:19 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152032">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93cc318ec.mp4?token=UN7S3KTTmsHagP-ulyNaAmI2GU60YSe9bFKwSn2CORtqVOmQzoLm8x14hojw_R8Oyfsf3sAnwGZuOnqf4NqVcAb6hQku2U6Xqn1roF_0QoTN0iSHRZm1ID5N3Xe4fxfeo9Rizva4mEw573G7JAcVcCBgdu0vqS1wLP_CwvOFkCn8FZD8pJWuULkNKGxBuXpepauTsuvN-1UIpBzZNai58jHnycsGIQk_vUjK80YiNeBINuXhokY6ziDGMJD2x3K089kfAz93S-o-WVRpiCtm3fHDboF8g1k1y2_GI3k88MNmYOkGyVkBMypREh98s-1xbCNzIzpzYnjIkUaD4PrP-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93cc318ec.mp4?token=UN7S3KTTmsHagP-ulyNaAmI2GU60YSe9bFKwSn2CORtqVOmQzoLm8x14hojw_R8Oyfsf3sAnwGZuOnqf4NqVcAb6hQku2U6Xqn1roF_0QoTN0iSHRZm1ID5N3Xe4fxfeo9Rizva4mEw573G7JAcVcCBgdu0vqS1wLP_CwvOFkCn8FZD8pJWuULkNKGxBuXpepauTsuvN-1UIpBzZNai58jHnycsGIQk_vUjK80YiNeBINuXhokY6ziDGMJD2x3K089kfAz93S-o-WVRpiCtm3fHDboF8g1k1y2_GI3k88MNmYOkGyVkBMypREh98s-1xbCNzIzpzYnjIkUaD4PrP-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره ایران:
میتونیم خیلی سریع به این ماجرا پایان بدیم. اونا هنوز نمیدونن چقدر باهاشون مدارا کردم و مهربون بودم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/alonews/152032" target="_blank">📅 00:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152031">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ: ایرانیا میگن همه رو می‌کشیم، اونا میگن الحمدلله الحمدلله! بچه‌ها شما دیوانه هستید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/152031" target="_blank">📅 00:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152030">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988c9468b6.mp4?token=ZmXCEjBHNzzV22fHM1VTzIG-uBWOFbibD1jSipIzB3v2C51Uo1SshqlJun8ECyi9WvvDOJtsk5kKm36ObUuudCWPaFjYAlnyLvZhkz9sLXB_9ebijTo1HXMOkrvSNvDLBHg3X8dBe8PdLdC6rJBH-sn7PkHTmV93_HjgtesaOik13H-7xJWQa_eiCbddCP4o2MaJfAhGhtK73PjJtfnxztTOIFD3CmeG4pqGTn3QtL-scwQyc50EMWB2whbNq0-bnqpf1vJhX012HUnCyl35wtRaZScU_kAiLONS-PpKwfZqCM7NmUz8nhFt1BHJX28Qe6mVCvz9xur9B768m6mu_68_yXS4yXzBJalwVZAdpp2PIVgNrN8FWMhBx3ZLEN0peGBnxhU4RCfLzyACmMyDIHJgovfOxFRMVDbLu8CH5ZCjEWpwTY5J8WRKRzJmRM7ZSKErO79F5HMnPpGUUW7uz_2EX9yE8RA52zVXwZj7hj8q5B4kXyL690opwy5oeiEjV3VBR7xXbJx7y8KHCezYp18h_iVpf8Nxs7HPXQrpQHiWedl8Y7LhdaH1abqUFiyhMJBASWp_vlmU8Kc8ztFj__Wv68GW_1AUjyuEbamLsXCbnAC3j8uBZsmBKeMiBZQFGiytbqQnhOg8ey2i9h_kbCwKtoVo5c7V-_LgrmuHUko" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988c9468b6.mp4?token=ZmXCEjBHNzzV22fHM1VTzIG-uBWOFbibD1jSipIzB3v2C51Uo1SshqlJun8ECyi9WvvDOJtsk5kKm36ObUuudCWPaFjYAlnyLvZhkz9sLXB_9ebijTo1HXMOkrvSNvDLBHg3X8dBe8PdLdC6rJBH-sn7PkHTmV93_HjgtesaOik13H-7xJWQa_eiCbddCP4o2MaJfAhGhtK73PjJtfnxztTOIFD3CmeG4pqGTn3QtL-scwQyc50EMWB2whbNq0-bnqpf1vJhX012HUnCyl35wtRaZScU_kAiLONS-PpKwfZqCM7NmUz8nhFt1BHJX28Qe6mVCvz9xur9B768m6mu_68_yXS4yXzBJalwVZAdpp2PIVgNrN8FWMhBx3ZLEN0peGBnxhU4RCfLzyACmMyDIHJgovfOxFRMVDbLu8CH5ZCjEWpwTY5J8WRKRzJmRM7ZSKErO79F5HMnPpGUUW7uz_2EX9yE8RA52zVXwZj7hj8q5B4kXyL690opwy5oeiEjV3VBR7xXbJx7y8KHCezYp18h_iVpf8Nxs7HPXQrpQHiWedl8Y7LhdaH1abqUFiyhMJBASWp_vlmU8Kc8ztFj__Wv68GW_1AUjyuEbamLsXCbnAC3j8uBZsmBKeMiBZQFGiytbqQnhOg8ey2i9h_kbCwKtoVo5c7V-_LgrmuHUko" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایرانیا میگن همه رو می‌کشیم، اونا میگن الحمدلله الحمدلله! بچه‌ها شما دیوانه هستید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/152030" target="_blank">📅 00:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152029">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
بچه‌ها هر لحظه احتمال جنگ وجود داره و پشتش هم قطعی اینترنت
🔴
این ربات vpn داشته باشید و سرویساش قطعی نداره
💢
@VOXNET_BOT
💢
@VOXNET_BOT
✔️
میتونید با خیال راحت تهیه کنید و تو قطعی اینترنت هم متصل باشید</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/152029" target="_blank">📅 00:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152028">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزارت انرژی آمریکا: ۴ میلیون بشکه نفت از ذخایر استراتژیک برای مقابله با اختلال در عرضه ناشی از شرایط جوی، خارج خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/152028" target="_blank">📅 23:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152027">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c86374dcf2.mp4?token=AvNOx8BFkzwCuOJu0UZj1qYTyUpHuJgILIOfvej7L-r6iq_VbVEdgp3aI8wkvglgQErYrswAqjDEo3H39Vo7FAW3EMmq_B2mjuU4hNVj1M9B7UyY6ys49sjQkI_Y6N5JAMMhObiN6KZ9apjCAMy1TPYy8ivSo5RuVDOAQtmsqN0mzHPNE-L0GVT1a6T2o1QzlNFg3GWdJVobPwuP_XZYjTJCD8qM3zt8KUAz1qktgOOcsUELVBHbLMvpkRg93o7geS2x6PfVMrd5jwY5dE-N3rnnDfLHK7X5_FvZMklH68HzM4StSmJxBiiiPazdvaBMFrGtnvOdHa5q99waJ4js3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c86374dcf2.mp4?token=AvNOx8BFkzwCuOJu0UZj1qYTyUpHuJgILIOfvej7L-r6iq_VbVEdgp3aI8wkvglgQErYrswAqjDEo3H39Vo7FAW3EMmq_B2mjuU4hNVj1M9B7UyY6ys49sjQkI_Y6N5JAMMhObiN6KZ9apjCAMy1TPYy8ivSo5RuVDOAQtmsqN0mzHPNE-L0GVT1a6T2o1QzlNFg3GWdJVobPwuP_XZYjTJCD8qM3zt8KUAz1qktgOOcsUELVBHbLMvpkRg93o7geS2x6PfVMrd5jwY5dE-N3rnnDfLHK7X5_FvZMklH68HzM4StSmJxBiiiPazdvaBMFrGtnvOdHa5q99waJ4js3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آنها دموکرات‌ها هستند. احمق، احمق، احمق، احمق
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/152027" target="_blank">📅 23:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152026">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
یک منبع یمنی به المیادین: برخی سرمایه‌گذاران و شرکت‌ها با ترس از طولانی شدن جنگ، خروج از عربستان را بررسی می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/152026" target="_blank">📅 23:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152025">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
روزنامه فایننشال تایمز به نقل از منابع سعودی گزارش داد که در فرودگاه ریاض، ۵۰ نفر مجروح شده‌اند که برخی از آن‌ها در وضعیت وخیمی به سر می‌برند
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/152025" target="_blank">📅 23:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152024">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
هم اکنون شلیک موشک و پهپاد به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/152024" target="_blank">📅 23:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152023">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رئیس اتحادیه صنف طلا مشهد: فروش آنلاین طلا بدون داشتن فروشگاه فیزیکی و تاییدیه این اتحادیه، مصداق کلاهبرداری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/152023" target="_blank">📅 23:45 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
