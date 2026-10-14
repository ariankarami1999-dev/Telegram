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
<img src="https://cdn4.telesco.pe/file/AJ2XhDDThWmJuBJd-frbLfzyTFzGQY7w06R3rlkrgt5o1HFceCdeHzk_t1WEqU7VDYhMvDg2dk6iaq5McxQd0_fnWm-XpnLFLznzm6Ctlo9t3-FGUxNlFvdxHBaQ-IV_GZHvK27W0W7OLQ7bnyp3lY0W7HF5aRbNcbOD5YQNAv1gwq5jY5yjg1v5hjvf5HbmVRHiiJrGXh9E7T3Zp5KfINkFnez_J1zAz5CqaSQamhJ-dqFaOro5U9Q7vjwavNJAzF2isDttZemMgjaUJxndVByGkVVmyAS3Gvp5kKbd-3RbvaG27KXTJj69AllDNcnhigZGDf5Fip1021vRq7CSIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 270K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-23 01:19:55</div>
<hr>

<div class="tg-post" id="msg-84859">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f8d513a2d.mp4?token=ATd5Fr6f7SS7hqCS4PIBiKp2M5jS5zxo_tK_D62ZVTixbGfbevwLmunnblD09Q_lU2_IaYLplf-hn3JlUOIBknBROJwa2SKpY_0Y7zTExcCzJPQvx7XQUwEYByrP7aFXrfNrys_HkH_q_jw6S5IZoIHg0Hk_u_p_VHq_7f4KOShIxyZiNxqDtVcbxMZ7R5_PIFC3MtF7CWtJg6byqgeZIG4aMGk_WcndJxzGNaiD-ts5bYm8FcEV5iAqKSz2iVks_FOXaEKEba3UL8y2rvve6-_aRQX27vejLykjwI-lg-s_GahRtHzfFOg5CNUjiSdMRVTsUdr-A1flNUt2uI6G_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f8d513a2d.mp4?token=ATd5Fr6f7SS7hqCS4PIBiKp2M5jS5zxo_tK_D62ZVTixbGfbevwLmunnblD09Q_lU2_IaYLplf-hn3JlUOIBknBROJwa2SKpY_0Y7zTExcCzJPQvx7XQUwEYByrP7aFXrfNrys_HkH_q_jw6S5IZoIHg0Hk_u_p_VHq_7f4KOShIxyZiNxqDtVcbxMZ7R5_PIFC3MtF7CWtJg6byqgeZIG4aMGk_WcndJxzGNaiD-ts5bYm8FcEV5iAqKSz2iVks_FOXaEKEba3UL8y2rvve6-_aRQX27vejLykjwI-lg-s_GahRtHzfFOg5CNUjiSdMRVTsUdr-A1flNUt2uI6G_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا شبتون بخیر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/funhiphop/84859" target="_blank">📅 00:59 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84858">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ:
اونا از من قول گرفتن که دیگه هیچکدوم از رهبران ایران رو ترور نکنم. منم به اونا قول دادم.
احتمالاً کمی زیاده‌روی کردم. متأسفم، چون دیگر نمی‌دانم با چه کسی طرفیم.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/funhiphop/84858" target="_blank">📅 00:46 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84857">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrT_Js3HFgtiiNkqgKSS6YdjeZt2oj7cSUZmP0lOy3tCEMD6onVZYmh5t2hzEII3uXSaQM18Bo-zzDow17gNClx6YMvHx7IYBO5aPEEUZ5CqHGXIi0zwbSOPxF0EIovJUgjHCi_1L40QZhAdzOv7HE_dvreUUGkOP4Zm3d93eI-rDg1SQSL5P-xI1GcnFcvfcnELj4UWq_CoNY_u2MiwTDIAEJavCuvBrMawBVfYekrt7kOTE94VzCl0JrLprNoDwTOTVApm_X6rk5hYrSCwxEHSZ5N7Z7DXbkCV94maE9aHAz1Pahlegam8708GBuYjgE7ry4bsIXk0z7jE5kg1hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضریب برد رئال بعد ۳.۱ چند بود؟</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/84857" target="_blank">📅 00:37 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84856">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ضریب برد رئال بعد ۳.۱ چند بود؟</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/funhiphop/84856" target="_blank">📅 00:35 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84855">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستان ولی از بارسا عقب بیفتید رودری توپ نمیده کامبک بزنیدا، حواستون باشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/funhiphop/84855" target="_blank">📅 00:30 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84854">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تاثیرات نبود وینی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/funhiphop/84854" target="_blank">📅 00:29 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84853">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پشماممممم</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/funhiphop/84853" target="_blank">📅 00:19 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84851">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کامبکو واااای</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/funhiphop/84851" target="_blank">📅 00:15 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84850">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پرز باید یاسر اسانیو بخره اینطوری نمیشه</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/funhiphop/84850" target="_blank">📅 23:47 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84849">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نمره فوق العاده قوی وینیسیوس شامپانجونیور تو نیمه اول  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/funhiphop/84849" target="_blank">📅 23:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84848">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7TD88HpGDz2CkVYboPZibtkyq0kXAThPnfS3LyLp0kcjEVmKdro6CQyUCcAr46F0ftI2C0xL4eIAm49tL-hXG_ZsLyFUoJSMDkS3IylbJ9mf_Q7kjjYSZ2psDFfkvZusZfxjxxXULhX11MWOymnodqWt2Kj9tL3TEKh74YEtVboF2ZJuqkV1bO-aPParMmhDmLZXiFgFPscu1bh-SpzpdGssOnDBfb6ryxsp-kFQW7pPV7Ch25CSlR_iY020VaRUiUs3JYc6m1d54JjC90xZVdZlgk8laq0aS_XjgHfdYdJJ5rQLTseslBVRPC-HIQ5_e6FrXJUoBqUAiS4bBGUIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمره فوق العاده قوی وینیسیوس شامپانجونیور تو نیمه اول
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/84848" target="_blank">📅 23:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84847">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تا دو هفته دیگ ایران به فلسطین اشغالی حمله میکنه
بماند به یادگار
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/84847" target="_blank">📅 23:24 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84846">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بیانیه اپراتورهای ایرانسل، همراه‌اول و رایتل:
خبر افزایش ۴۰ درصدی قیمت اینترنت دروغه، بلکه درخواست افزایش ۱۰۰ درصدی قیمت اینترنت رو دادیم!
هزینه‌های ما بخاطر جنگ و آسیب دیدن دکل و زیرساخت‌ها، تحریم‌ها و... به شدت افزایش یافته.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/84846" target="_blank">📅 22:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84845">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f18ea1acb.mp4?token=XRbM5H4dZ5Iq5uHBtSQUsJQvh4O7kFs27nXA6aQL3Da-AsrI4o1n5r9kh5xvyTLmA78YGi_nD9pyAy9oxwqZR7Hxq_dHC9AnuXCABROEd00KdEVoHccxKjRIfhqIOB3qvS_EZCOn8pjVt94NBjefHiQ7YY1gHBkKOY-TgxFjeCkIVm7z3WQpJB_NeqIkwg2o9z_-QTksPfUVSq1QjX8B2Gv6k-7hJ_Cp78L0tjqQRuOxkGjGsUNs0tf8DLJ0YJDE02XA4jp9L7_N0jf_NFPJhtxCIEfj_iuJLCGCgEsqlaiePIIYR3t6xYet83_wfz2UIDyE4b0xJ_GDKZTgYIKTLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f18ea1acb.mp4?token=XRbM5H4dZ5Iq5uHBtSQUsJQvh4O7kFs27nXA6aQL3Da-AsrI4o1n5r9kh5xvyTLmA78YGi_nD9pyAy9oxwqZR7Hxq_dHC9AnuXCABROEd00KdEVoHccxKjRIfhqIOB3qvS_EZCOn8pjVt94NBjefHiQ7YY1gHBkKOY-TgxFjeCkIVm7z3WQpJB_NeqIkwg2o9z_-QTksPfUVSq1QjX8B2Gv6k-7hJ_Cp78L0tjqQRuOxkGjGsUNs0tf8DLJ0YJDE02XA4jp9L7_N0jf_NFPJhtxCIEfj_iuJLCGCgEsqlaiePIIYR3t6xYet83_wfz2UIDyE4b0xJ_GDKZTgYIKTLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مرد ایرانی به اسم رستم با تیپ و قیافه لوطی گری و سبیل دسته موتوری رفته خارج از کشور، کل دخترای خارجی روش کراش زدن و همه دارن باهاش عکس میندازن. البته میگن ai عه
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/84845" target="_blank">📅 22:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84844">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رئال داره درست میشه
وینیسیوس 4 بازی لالیگا رو محروم شد و به این ترتیب الکلاسیکو رو از دست داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/84844" target="_blank">📅 22:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84843">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فردا بهترین شو کمدی تاریخ ایران میاد
مهمون قسمت جدید برنامه قیاسی پیمان قاسم‌خانیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/84843" target="_blank">📅 21:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84842">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86350e52fe.mp4?token=sP15uNYRc0x0Dy_ROJFTVY20JZGLlRCDxZw-j-0Hpz46Gckm09vEj6_H8idCep-a6a_nIzHedbNcNja0HDShCDvn8fs5-pD-ubLxmESfa9pM5kCtN3oi3-SGomN_FiT7hozIGJKg__EE2R4kkTHpB-xGGqfiOJEKOb1nTO-B70NK7_sVUVSP_lVFSBYeYtAAo9ExqYwng_hPr0iU60DqNjwnVAxS717jH1NK4qpHXMVjRuhVAAmbqiRCVpcGHspAGAgiZg4lBFWoP5U4Ccm-eF1jdBamtAkFhOadFp7d7ZcpNGuSDLmRzr6H7CIrQDo2a_jQ1djXUB00jknO-_wxBwqqasFowoGTEpAa5DnU5R3mqsURa-AhfCW0d7eaZhoxq4ExP7WdvpeU7uU4RXmA9qKZxRIsOXVqdxdlb0ve_xOPr77QSGufoCjvMUMdzl3PHXYwr_YAt5HByjIHhhNGJAF_GIKDersm70b7AI3VIbu6CgyS6svvSTVfT7rrKLhiR0FNwMH3PnKegJz3tn0-doSi2nwfBaaa2zVjbF39aiZOPA0CUCT48GlqbJoFV9pXIVSfTE_y2Wa55b1shOX9TZxP_mqNPMzL0iMiIZqIygpsJHH0fA1V_c-VVNNWml09BavqbGRd5bBZk7UHl4E0fiPAggVvkhzkgvy0Rnz3Hz4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86350e52fe.mp4?token=sP15uNYRc0x0Dy_ROJFTVY20JZGLlRCDxZw-j-0Hpz46Gckm09vEj6_H8idCep-a6a_nIzHedbNcNja0HDShCDvn8fs5-pD-ubLxmESfa9pM5kCtN3oi3-SGomN_FiT7hozIGJKg__EE2R4kkTHpB-xGGqfiOJEKOb1nTO-B70NK7_sVUVSP_lVFSBYeYtAAo9ExqYwng_hPr0iU60DqNjwnVAxS717jH1NK4qpHXMVjRuhVAAmbqiRCVpcGHspAGAgiZg4lBFWoP5U4Ccm-eF1jdBamtAkFhOadFp7d7ZcpNGuSDLmRzr6H7CIrQDo2a_jQ1djXUB00jknO-_wxBwqqasFowoGTEpAa5DnU5R3mqsURa-AhfCW0d7eaZhoxq4ExP7WdvpeU7uU4RXmA9qKZxRIsOXVqdxdlb0ve_xOPr77QSGufoCjvMUMdzl3PHXYwr_YAt5HByjIHhhNGJAF_GIKDersm70b7AI3VIbu6CgyS6svvSTVfT7rrKLhiR0FNwMH3PnKegJz3tn0-doSi2nwfBaaa2zVjbF39aiZOPA0CUCT48GlqbJoFV9pXIVSfTE_y2Wa55b1shOX9TZxP_mqNPMzL0iMiIZqIygpsJHH0fA1V_c-VVNNWml09BavqbGRd5bBZk7UHl4E0fiPAggVvkhzkgvy0Rnz3Hz4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان های بیرانوند به زبان ژوله.
پ‌ن: به شدت چندش بی مزه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/84842" target="_blank">📅 20:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84841">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325e9a098a.mp4?token=kz6jJd7iAv5sWihPmEnX4lLHXIKLBN0zNInK1FRhOSdMcV6J7rRv04eWBxGEDItDxKKQXG2y--nfHmfY9yGNBEHF6OT9ZPmRcuoHV1wFfpIDi2HFkMZBAPcj_ov4GN55hD-wFOsXslXWv_B8x39DXhmVgr24TWF-IuLe9BoK6UCII9C7m5Pii0dYaAV-sXM-NvssXX_8RNjIl5FTF2FR3xsbb190IV3Y7EKe_jmFOOkkFaVhIQkN0Mk0n6O4dDLROaPPpXFlvAsiHBaNxKWBCgmN11huKh9tqvI3NJ_EvFJKFOG5ZhhP79_ZaVZFys-uvg9RkF-LUS7Vjmu4DQPUMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325e9a098a.mp4?token=kz6jJd7iAv5sWihPmEnX4lLHXIKLBN0zNInK1FRhOSdMcV6J7rRv04eWBxGEDItDxKKQXG2y--nfHmfY9yGNBEHF6OT9ZPmRcuoHV1wFfpIDi2HFkMZBAPcj_ov4GN55hD-wFOsXslXWv_B8x39DXhmVgr24TWF-IuLe9BoK6UCII9C7m5Pii0dYaAV-sXM-NvssXX_8RNjIl5FTF2FR3xsbb190IV3Y7EKe_jmFOOkkFaVhIQkN0Mk0n6O4dDLROaPPpXFlvAsiHBaNxKWBCgmN11huKh9tqvI3NJ_EvFJKFOG5ZhhP79_ZaVZFys-uvg9RkF-LUS7Vjmu4DQPUMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میا خانوم انگار تو کنسرتش خراب کاری کرده و خوب نخونده، ولی خب به کسی مربوط نیست ایشون هرکاری کنه درسته.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/84841" target="_blank">📅 20:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84840">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8f9205840.mp4?token=MsPiEuCvuI5VlElrsEpbVNCMI6JquDt6_STLHga8iOhuKpa1zmN4mG3DKOyVMXQGKuKNR6TAPeD5JpRfkPcfY-OrlIdcSZlHQ4DIjUVFThgvGlhi65djwIx3asN43PO-hNRDs4j5Waz2oe-HM-NZhm3fJrvp2fjrB_1-ZQYYjAWF_jfsTxcXXaAOJtOcrc_gyAPhe8lZah9msP-5R-cj8xO3xKdggX6NBC_0sICEO40-M1PRHiZcO68CAO-nA2gwIugmaOMCpkx2YuQ4B6BcHtICc2t7AYmrJcJkTbA27xUeCtxh86t1Vz_Cx4twDSa5N0fif9ZOJQzFQdutE5nGyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8f9205840.mp4?token=MsPiEuCvuI5VlElrsEpbVNCMI6JquDt6_STLHga8iOhuKpa1zmN4mG3DKOyVMXQGKuKNR6TAPeD5JpRfkPcfY-OrlIdcSZlHQ4DIjUVFThgvGlhi65djwIx3asN43PO-hNRDs4j5Waz2oe-HM-NZhm3fJrvp2fjrB_1-ZQYYjAWF_jfsTxcXXaAOJtOcrc_gyAPhe8lZah9msP-5R-cj8xO3xKdggX6NBC_0sICEO40-M1PRHiZcO68CAO-nA2gwIugmaOMCpkx2YuQ4B6BcHtICc2t7AYmrJcJkTbA27xUeCtxh86t1Vz_Cx4twDSa5N0fif9ZOJQzFQdutE5nGyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی انگلیس هم باشه کصخله پسر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/84840" target="_blank">📅 19:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84837">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WYEzmzp9OcP7hqFFPB8hnEZVKbsu9SoqlOzgt9QvQgAFADOxs1AgBUfrFHXOnraD4ZaZ7wPUOti-2ReOvaEoLMBxE-prUuDu4ptcr53SZJuXWf-6YX86WZhjKkKMH13j6vTE-xXuBKfFzS2osqw9GMmBYIeeUgafZjBXdsJVNr7IfVrzQK1sjSl0jAIc2QovytmynXiVZEwv5aLLUYcqD2AzqgFjRfSrnzBYxMHBW_iO5VLe8-eXV806_sOaG_6TVN7pbGarErxiAh1XboHQkU2K6PhByiBjGi9Wm1HHgQkFDb7krOxig5J7B7oq1NHuEuOA3aPuI83rjJpos1YxYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m4lEVkSJG8-_O7y5eJt7EpQLUv_NxvT-ue4vVqHUSC9nTcSmXCeK9dtlgMwNI1sDdJRWviIRqfu6xYMln3he2sUo13QsNOGeJcjnfodXTIrttWXF-ZjfL6Syk7LOeREudnQpDoYLuwkt14OgXK9Uv57V-UIpxfn4cKOWXDNeEHDdDzvuEDsM9kpVpyFiRLiXkTgfPTPRxn4QHnOWlfTH9-tnwo7xfIjHzh-sYiFxP4yfVAMxP1dt1u0sCQKeEH8LWPxNHnX8SYmfSGhvonmfo6Aoaqn5h6bV-0ZdwyPZ9JYWMEUidAbQ6gMrVgN0iEH_8g-rZA-2EeXfLlIRgOPHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_XUoypWGwrLPWKTS8pJUhB1XTGeKhmzulhnfZzmOwHAB9OSM-UBxdL9nXXckjojW4KBGtyLCeA6WyZxSpkooDNq0NIuSfJfDv4kXwEg60okNCphQDxJoSu5px5ODUaLtFmJDMFBRVimWicm1MQaPNoLiZ7Z0jqDtrEgcT1dJRJ8-QjtluP3jajMu2RXh_oAwOUD0O1PNG48L78XKNivX2KOVfQc_PK_OTp-yn4Rmna4AzZZULDCAr0cCh0WYfVNQSVA1FDLkHkAUu2uSuSbIlxIdZY-QYPnRD7-yrd_pVrTB2v5CihufD_oYwcCCVT9DfgBjfwUQax1omMQEft9fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاتای جدید کایلی جنرو ببینید تا ببینم چه خاکی تو سرم میکنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/84837" target="_blank">📅 19:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84836">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oiq5NQRGgoq6ENYn5oO2xk_uV4tX9wJgQMZoFzTJAJWt65m8nB7CCfWKZliYMBIC_VhLJNpvhwQyUzy1feB-R9k2RTKjrWlUFKuHbkjndjR6I8i5elMOEw8yqt8Ccey_GUy3oTixIw1nMAl5c5dPyuJkjqYhgkI-3MbpDmdbVSFsbxBe3Zta1BTGLqxzQ44aIVCZBfk3VN_6tStkrj3QpyApxkY6CJPJcPu1IXvBH0h2n3va1RgdyYPhHZe8Dpn82kdupyK9dkjc1Wc7DkgMUbKXYuWIYZh6SOWW14mnhydr0pdfyOn4UyEbrM1uSwJTRmWeQ83jc1RHPswyQoxWkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
10٪ شارژ اضافه بر روی واریزی‌های ارز دیجیتال برای کاربران بری بت
⭐️
🌟
📢
در سایت بری بت وارد حساب کاربری خود شوید.
💸
از روش ارز دیجیتال اقدام به شارژ نمایید.
🔋
🪩
بر روی واریزی‌های ارز دیجیتال تا
0️⃣
1️⃣
🔣
شارژ اضافه دریافت نمایید.
💰
✅
ورود به سایت:
👇
🅰
g22
⭐
https://leworkcihsa.shop/fa/affiliates/?btag=914641_l303106
🌟
کانال رسمی ما در تلگرام:
👇
🔗
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/84836" target="_blank">📅 19:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84833">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c264e282e3.mp4?token=E16lpTLfyG3BKwcL0YJ_NxEhtojrtJuTC2U4hrM7322tplZ1Uvq1WlMtcDZKHMMeOZPt_cxmeqFKAb1fNgVCyANxqfQyKv-dk4hnyG1509vm-Hr0D6Bz383P3X3Ivq59IMxRCMitGYQasrGlrYU7DaYqSNArzYBZNzDI8XuX_-78zFynALHw4PdSwgpZQZbcI6M6Pl57u9D7lXHHflx1upPrHLnBv_ABLqAZKdKBgxUumBUstdh6I6b6BOHnq8ITbynoloFeRP6sibhz8eIjwoy2pSBBq5mdgQqpivU3B7xxrMX-RjNneGUz1WejdzTqlDMPZzY3BERXyrPBbLYPDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c264e282e3.mp4?token=E16lpTLfyG3BKwcL0YJ_NxEhtojrtJuTC2U4hrM7322tplZ1Uvq1WlMtcDZKHMMeOZPt_cxmeqFKAb1fNgVCyANxqfQyKv-dk4hnyG1509vm-Hr0D6Bz383P3X3Ivq59IMxRCMitGYQasrGlrYU7DaYqSNArzYBZNzDI8XuX_-78zFynALHw4PdSwgpZQZbcI6M6Pl57u9D7lXHHflx1upPrHLnBv_ABLqAZKdKBgxUumBUstdh6I6b6BOHnq8ITbynoloFeRP6sibhz8eIjwoy2pSBBq5mdgQqpivU3B7xxrMX-RjNneGUz1WejdzTqlDMPZzY3BERXyrPBbLYPDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو انگلیس، یه مرد جوون وارد محوطه ببرهاتو پارک حیات وحش میشه و اونجا یکی از ببر ها بهش حمله می‌کنه و نهایتا میکشتش!
مسئولین حیات وحش اعلام کردن که خوشبختانه ببر سالمه و داریم بررسی می‌کنیم بفهمیم اون کسخل چرا رفته داخل...
یه ویدئو از قبل ورود این مرحوم اومده که داره به یه زوج بریتانیایی میگه "من میرم بین ببرها، ازم یه عکس بگیرید"
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/84833" target="_blank">📅 18:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84832">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این رپر جدیده سمی‌لون، بالای ۲۰ تا ترک داده تو این چندماه، هیچکدوم هیچ فرقی با قبلیا ندارن، اونور قدیمی مارکت شایان یو ده ساله داره رو یه فلو ترک میده و همش ترند میشه.
بعد میگن چرا مارکت پیشرفت نمیکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/84832" target="_blank">📅 18:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84831">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfb34762f.mp4?token=oQs6uBXi1oEJAoZF4ln2Z4_74KlPa-L4pvDjJ0grJ5CFiQ1Z-zgHDlP43_BmZPBcyMTSVWZZ9A4BKGXhAklrdkF-TGCbTIV9MJbeDBaB9TSM4_2bwy7fIcatYd8alLl3n9tRNfRypSx0xB2EdsNLAD4xiiLjhBtOJnFB0HyDk5sPZVq43-QaKzi5sJgWEKZwPNHeeqGHkF_ZZUjK08rT6jNKu6bgMvnSs041kDLyBxuOz3nghS9KIzzzAw6rQkfRBh_Awmo-Xc_lWE_DIEdX0OV_7uY8Z_F2pyNVfqNUhrJ6O_CC0W9vCBwhQeNEay4GXAWEvJyhuemnL4QlpShZ4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfb34762f.mp4?token=oQs6uBXi1oEJAoZF4ln2Z4_74KlPa-L4pvDjJ0grJ5CFiQ1Z-zgHDlP43_BmZPBcyMTSVWZZ9A4BKGXhAklrdkF-TGCbTIV9MJbeDBaB9TSM4_2bwy7fIcatYd8alLl3n9tRNfRypSx0xB2EdsNLAD4xiiLjhBtOJnFB0HyDk5sPZVq43-QaKzi5sJgWEKZwPNHeeqGHkF_ZZUjK08rT6jNKu6bgMvnSs041kDLyBxuOz3nghS9KIzzzAw6rQkfRBh_Awmo-Xc_lWE_DIEdX0OV_7uY8Z_F2pyNVfqNUhrJ6O_CC0W9vCBwhQeNEay4GXAWEvJyhuemnL4QlpShZ4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تتلو قبل کسخل شدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/84831" target="_blank">📅 17:36 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84829">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اینترنت پر سرعت اپراتور های مملکت قراره افزایش ۴۰ درصدی بخورن
تعرفه های اینترنت فیبر مخابرات هم کم کم دارن افزایش میخورن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/84829" target="_blank">📅 16:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84828">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c83uYHETy_ssVXkDj0IqxnoRA660ZfvwXRZ7aqfNxBmzOhvk2WWWWKmQWUfaxIl-IaSDx5CbKgaaySNngJ1oMnpm9f2TUbqTCjUpDDrqeGiYIf41_ScVWfKW2tW9pBT5EScmKkfGgMuOIDQIP1VhZPu7nwlx-SiFvdzEEl09qG3C95EIdQ9FPNMqv2XDu7B51j7_FY2Qcb0Bt4o-91ncZicRsKXh9pwNR8oZmEncrwzvFLfz2k9-KOJAeUFkTm6299pJPPqC-R7qnfpPa5DXlwhwwqwVTg7tTNX7CT11FCaXtysoiIJe8RLToyL2qz-5GWscpF-KQ_Q1YIVIi3qNyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال یه پست گذاشته خطاب به لمینا بازیکن گالاتاسرای و گفته، یعنی الان دیگه منو می‌شناسه؟  رافینیا و فرمین کامنت گذاشتن فکر کنم دیگه شناخته   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84828" target="_blank">📅 16:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84827">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujFGuAFn80bzjMLB-HnNNG9Tsn-V7j-Zzfjhsi6k1Ch4ZxsObv9IKxGrjmG3-jQGyJ7zt4eHYRdAfprDw7FjP0MMyYa0zospWAPy2hYTN5NQrF4Te-kAsQxhLSof9u2iFNQaWm7-t7B1JimFIdjuCl6Rt4aNzXk_2DwE9LiiA45iiam_xfhrBwhY-Zmp_RTcUiMWToAH2WHgY7k0o4xJ7UALo5gleQtIC8dDOI7ghkePSBXmuR1YaAUHB18wNVQ8RNvhfswEr_A26GW9MW2wGc2-gCcenD5jPDOnJ9hO6NeIJWIxMrU_LbI-T1R5Deu28bbIBq_QY5729xffaV3w5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال یه پست گذاشته خطاب به لمینا بازیکن گالاتاسرای و گفته، یعنی الان دیگه منو می‌شناسه؟
رافینیا و فرمین کامنت گذاشتن فکر کنم دیگه شناخته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84827" target="_blank">📅 16:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84826">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کیم جونگ اون رهبر کره شمالی خودکشی کردن رو ممنوع کرده و گفته هرکی تلاش کنه خودشو بکشه و زنده بمونه، اعدام می‌شه.
ممنون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84826" target="_blank">📅 15:54 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84825">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">عمان:
مذاکرات با ایران درباره تنگه هرمز به پایان رسیده است
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84825" target="_blank">📅 15:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84824">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kj3BCb-r2FDVZQij0LDu5qP0tJ2nXzYxggLeJZGoO2_kk1uidOnk2vHwI_ySujYC9LKL-7egu2XaWkCzLbYsFbQonLHWqCDoOLWe73AsvnY1okammx_SRzNI1rd3_g5UxyGAZMJHt4TrsKkEoXI3vwpsnzvbwPr7YjzGiqajDEUFYsJNREoR1cmeipZsyErg0RFkDr94fT6exbRd_VUI4TANSqSTaCwTczUBBvwUoLsByPJUq_lHhUix7S-Ti1rEi5cCGVgekf5zWfFzdw-S959daLOozkyhJ-okAW-KmHyPYvvcQU5D8E-O_q5e6_aLp4GDfnGv2ppAqMKHtY3SkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسه دیگه اشباع شدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84824" target="_blank">📅 13:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84823">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سلام فریب جان خوبی چخبرا  ذخیره کردی؟
سیریک صدای انفجار اومد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84823" target="_blank">📅 11:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84822">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(ChamanDarKhak)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVC939q44sB0DOGT1p1QzAEFlT3eoQqRR9pL1vCudDaXjgecDaHGQzkh8MtaDieKjMn4oral2NjyZEHnibYzuI009uf8PJizeU6wIyagLAlaSkWWmbvG_ttv1OMKYE5mLctsipr8yEyjTX3F0JVjlrzH2oz1TeKFqzWGnlwfD-oiztzgO4LD3lecLzsmUJyx2OP_WcjIGjNfsbggvwRG6qzUGFLyYHJ9WHpP2Wv9L0cP1em2XSrXt9876db7erciE8ItlY9oe7GjyCQobpzo2JCaaWNY_fz-wyoDdprGUp6pObWF47mxiXFLCUcpd4hj7AZBjnyQSNpzI_Mv1NX0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NEWS
🗞
🔴
فیفتی سنت
به یک خبرنگار گفته که
Eminem
به دلیل اینکه داره رو آلبوم جدیدش کار میکنه نتونسته در ساندترک فیلم جدیدش حضور پیدا کنه، حضور خود
50Cent
در آلبوم
Eminem
هم قطعیه
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84822" target="_blank">📅 10:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84821">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKaUxE3vsIKTfgC1wuxRN_lB7rveXkIEDB8_NTX5jw9byC_zs-JnAKQXFmwZqAfRuEEMcvS-lWRi-MLiPccgxiCWggw78qX3KFtMFPBC0FHkeqCyJ5HLaxtI2v2fZyv3vX_rG7m8UNnu9TS2ndJQADvtmG_ewuOLebA3GOWbwGFUfj2ItMth_V2OfBILkT8b9wTH8jG_pPy2xB8gEipQGB1xSOQWBSPHz_eRh40HZU97YRK8P69Tq7u3q2Dg4o13ItvpPvrB4Um-IvXrF8m84dVK_wuwqZCNaaBhXUMdA21rzHTQZ4t0a0AqDZ9zfnOZyTu6llNRCwYlVOAVLabT9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرونده قتل توپاک بعد از ۳۰ سال بالاخره حل شد و قاتلش به ۴۰سال حبس محکوم شد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84821" target="_blank">📅 10:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84820">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTi0eatiaaPRHNW0v5mGJER76OwODe9lCI6hNk_mky6Pxv2zbjBcAQforAgYSbFyZtL_eneuDoUr02KRP6CePuJK5WUSDP2QeORpqA_-1EhtL-NZFZ43PrYcsTAN8AcZbLImm2mfzoEyYvAP9oIgj5oS3J_wmfWVlAT4wU8ZbhQdyBsaEDzURMuf8USAPmQAjMoXujTLxo236zko2mH6Q1pHWI0vGmMvV2Y7JEoxtkFqXl2Ju6oFU9e0X5cYjGD2tWlCLKHI7ymY8GY8bK_flh_lZdPWBWfKcz7afCKPQUrnXSIZY9LeX222m7MHsfkvAxyUkgI4nl2glLn5oROlNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
منچستر سیتی  - پاری سن ژرمن
🌎
ساعت ۲۲:۳۰
⚽️
آ اس رم  - رئال مادرید
🌎
ساعت ۲۲:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r22
🔗
https://leworkcihsa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84820" target="_blank">📅 10:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84819">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScnyN7-CaYVYwUucDFX0Rz3NT1Z3Z5b1csBiV44NnViG2A_fWh_3wTwMkM6IF-GyVqol8kXkAqmaoVRni57qP3dP52O3tC9fVWl_l87P06QxhtIAjz7Iz6jIYfedgBzHUDZJ6hnY6S6J1lV4lru01-l2S-BlDieQDLJfMSIBrYNrSn4O5ezPPih3z-Vf7bybKaN-PhBIV565rNk1SmFrb7E1VqEikTl9r4JDc9pfwUTpL8e610oCUhCI6YtXJbAKXJdZJ7yLWYCjx2Bey1BRbZAByDVYVG-KtrAKe5KhPhYo8dKBaq436XHAeDNb9vDc17RFZqy2u3vebkIAVRSgpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب تو استرالیا یه دختر مسلمون برای ترویج دین اسلام رفته بوده توی خیابون نماز میخونده که یه راننده ندیدتش و از روش رد شد و دخترو کشت.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84819" target="_blank">📅 09:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84818">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc5f754c70.mp4?token=hYSvOUPiZdC6psz7X26Djlc2CjA-Wxzoaa76yl6wLMG_kEg2J7CUbx74C0CSLJtXyMoUpG2qjhe9Pgqud-VojdocHK3IvU3yt5UhQR2NdZtH-a72g1e4ImuMuEFx8ofaCaa17Wf5gGyhjdX4Fh6ilicChgdiVYDxZ2wC40gOENRTsyzm3-CNm0nNdq5TrQG3EKvC0vGi574W4fhcoTTuy5Xec7LCZaYzVxk57_DTRYZm5sJVSpA208a-9qnUz_yC0DJ0_7NOl4IjI19TI44gCx1X1XLhMNHPV9nATnrXTnbS-7Onb6h6yzbJ1qWUdvrNLLaCEJ4Wpmov0vfpy3-U_S-38dV2z93hLqnPQB8BxGRAzOJ32lEtEx2FLSU06dPf5PwjQGgGycz-c3ycEmyJrO8hSAPAx0Iat3T1Spv8qyeJecA7Ls8DEbwLoJ3NoizKKJbgi4_2vX9Fvv9m4Hlw6hce9FwjwM8lQ8PElxo3vRDTQ8Hrou1BxPIXidegLPWyktbR7zDby76yPMI6Sa4c7IzeUmglCIWfzo_zhjMOgCvZvieFa4gxDYW4KGjgufSWDUCZbolugFxOqkI7H1YuK2aFgYV8rXfCTdDWvZNfD8vvMB05YqHVZI50KQ6fy1XSWmjrqjIJQ6HIa97S3621lDVZiI-qi3Lvo_t0IhFHd0Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc5f754c70.mp4?token=hYSvOUPiZdC6psz7X26Djlc2CjA-Wxzoaa76yl6wLMG_kEg2J7CUbx74C0CSLJtXyMoUpG2qjhe9Pgqud-VojdocHK3IvU3yt5UhQR2NdZtH-a72g1e4ImuMuEFx8ofaCaa17Wf5gGyhjdX4Fh6ilicChgdiVYDxZ2wC40gOENRTsyzm3-CNm0nNdq5TrQG3EKvC0vGi574W4fhcoTTuy5Xec7LCZaYzVxk57_DTRYZm5sJVSpA208a-9qnUz_yC0DJ0_7NOl4IjI19TI44gCx1X1XLhMNHPV9nATnrXTnbS-7Onb6h6yzbJ1qWUdvrNLLaCEJ4Wpmov0vfpy3-U_S-38dV2z93hLqnPQB8BxGRAzOJ32lEtEx2FLSU06dPf5PwjQGgGycz-c3ycEmyJrO8hSAPAx0Iat3T1Spv8qyeJecA7Ls8DEbwLoJ3NoizKKJbgi4_2vX9Fvv9m4Hlw6hce9FwjwM8lQ8PElxo3vRDTQ8Hrou1BxPIXidegLPWyktbR7zDby76yPMI6Sa4c7IzeUmglCIWfzo_zhjMOgCvZvieFa4gxDYW4KGjgufSWDUCZbolugFxOqkI7H1YuK2aFgYV8rXfCTdDWvZNfD8vvMB05YqHVZI50KQ6fy1XSWmjrqjIJQ6HIa97S3621lDVZiI-qi3Lvo_t0IhFHd0Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به روح پاک پسر طبیعت قسم این دیگه صددر‌صد یعنی تعویق
ترامپ:
صبر کنید تا ببینید ما با ایران چه خواهیم کرد. ما کارهای بزرگی انجام خواهیم داد. صبر کنید تا ببینید. آنها فقط منتظر هستند.
صبر کنید تا ببینید ما با ایران چه خواهیم کرد، زیرا ما تا حدودی از این موضوع خسته شده‌ایم. می‌دانید، ما خسته شده‌ایم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84818" target="_blank">📅 05:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84817">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترک جدید سلطان بالاخره ریلیز شد و سلطان بالاخره رکورد گینس تعداد ترک ضبط شده با تلفن ثابت رو زد
🔥
🔥
🔥
🔥
YouTube  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84817" target="_blank">📅 05:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84815">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzKdW08Qg0StFxpcFuXRuidb-B5sJyaFvSM9Kqv9fsgapCWUEbkwkBYe2wZ2H8IPgKk8axlF7juq6Se0n1CUyMT3xEcFo4YrF4bsvtF-VZpoMRb5nrCPnQ2IFJfs6ZB2kVfpv4x0jY24kdW6Ul0kvEZcQD9V51OfUBhjPnM66RTpzASECVw9Xdv_lSkfkK9XXBRB8bHhOWtFGG6Z5QWqe2rfDf9cGZx38DNt6TLXWMGiSkyQE5nCSOgJRvw3Deiffq6D1vyFWYp034wqxRaXpaj0mL34RvAKG8fxxgixWBrz-Q6jTedvQ5CIDDquXo_BxQ6pBaKTrh-lrkmKm5E5LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید سلطان بالاخره ریلیز شد و سلطان بالاخره رکورد گینس تعداد ترک ضبط شده با تلفن ثابت رو زد
🔥
🔥
🔥
🔥
YouTube
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84815" target="_blank">📅 05:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84814">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08b06e11a2.mp4?token=qT6rJAgx1ACZ-OPjF6pTIubgZgVvDJ0iPsIWq1-Hmdmq1Ir7CWjfLR4aMygiivJe5pQruqC4URsOw-wB-GADLKAit-7utg2MoZXR-V2AQQeMG0S-1XzQwu3aTGG3CXAPIG5NgjZkp_spai_hHhKvLY0__zQZB7HrkXY6K0aZB-C7tJnSJRZwUsX1nL3J69ICQZ9hl6JdA7-VapVBOZ0Mu_P1MyOgdhls-whpog5DlEuXbbCcy-6AVV2R0Y-Ycxe8MEnua5UlNxf6H-Gbsj2mhwFMcHlVZgVghFX0cCbJLnAVFs7E3i93ET6Iu-bi_7SHa2yvoThR4w4B-6qOqxre-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08b06e11a2.mp4?token=qT6rJAgx1ACZ-OPjF6pTIubgZgVvDJ0iPsIWq1-Hmdmq1Ir7CWjfLR4aMygiivJe5pQruqC4URsOw-wB-GADLKAit-7utg2MoZXR-V2AQQeMG0S-1XzQwu3aTGG3CXAPIG5NgjZkp_spai_hHhKvLY0__zQZB7HrkXY6K0aZB-C7tJnSJRZwUsX1nL3J69ICQZ9hl6JdA7-VapVBOZ0Mu_P1MyOgdhls-whpog5DlEuXbbCcy-6AVV2R0Y-Ycxe8MEnua5UlNxf6H-Gbsj2mhwFMcHlVZgVghFX0cCbJLnAVFs7E3i93ET6Iu-bi_7SHa2yvoThR4w4B-6qOqxre-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قهرمان فیزیک بن‌بست دسته‌ی مثبت 35 کیلوگرم، بعد از یه بحث بسیار پرتنش بین سه تا نورون باقی مونده‌ی مغزش، یه همچین تصمیمی گرفت.
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84814" target="_blank">📅 03:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84812">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شمام خوان گارسیا رو میبینید یاد نویر میفتید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84812" target="_blank">📅 01:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84811">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDM34QxJDbjB4JKAi4PgWV_peVM8FSgaue5Bf_Xpu9Kox1VpaxAYWIevPKmPGEo2eib_E-rtNmgY_bt9rePwNBPAnj_4O0ceSVYMVv-aOzuDsRixEVO8KItJ2OsqKNmg8T5kF_SPRHUNSl2asXPvTMIIUIpVlDF_rTQ5apWzK1Z180IXhUIfzKkT9XT3LbKWP1tiYkkDry-4ybcLXTypuF9QhDuDVL_k0qQ9DNMblEyVL6hrQ5MY5fds4HMotQAGisUvXhp6RkxYVwq6nncm8JcrJuoFjrGYc6SyMHzwU1Z6lODoUEhR0qCXjg7WxwMJX48YIF-7TGCv46Y_v1aycQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هی بگید منچستر قرمز نیست و آبیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84811" target="_blank">📅 01:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84810">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آمریکا اسرائیل و ایران، هر سه تاشون براوردشون اینه که میخوان غافلگیر شن و هر سه تاشون منتظرن اون یکی اول بزنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84810" target="_blank">📅 01:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84809">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65b19bec2.mp4?token=J26JHbmsvDi8oemBbOpTHy5b5NVuzi3XFuaalMs32e9UdSb6VYWmna9NVEvD5Jho1K2rCGqsdcaHR6V4Sdf1uisvsd98TfCl2O9OBmCvImortkgwiI4elHJAoqBkp6iHr9SA_0xTn8r-S3xW3NeIm_h7pt1x_yLFbiPgE-MbPF6xD-N4yB9FvyBeXutZm8aGk9w754zh5bKcdx1RVLl41bVxS70jz4Yu6fOGPSaUe0IsUDvEhpl4JGejQeVfm0zI9L67gWNnbH-J3qfM4CeNSVROavIS4T396SNCfXSxZ_a-IX2oKPX4Ly9KIYf0VWstq-UIiMMqUgLlpve968sqOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65b19bec2.mp4?token=J26JHbmsvDi8oemBbOpTHy5b5NVuzi3XFuaalMs32e9UdSb6VYWmna9NVEvD5Jho1K2rCGqsdcaHR6V4Sdf1uisvsd98TfCl2O9OBmCvImortkgwiI4elHJAoqBkp6iHr9SA_0xTn8r-S3xW3NeIm_h7pt1x_yLFbiPgE-MbPF6xD-N4yB9FvyBeXutZm8aGk9w754zh5bKcdx1RVLl41bVxS70jz4Yu6fOGPSaUe0IsUDvEhpl4JGejQeVfm0zI9L67gWNnbH-J3qfM4CeNSVROavIS4T396SNCfXSxZ_a-IX2oKPX4Ly9KIYf0VWstq-UIiMMqUgLlpve968sqOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا پر تناقضه این ویدیو، شاهی و بیگ شگی و محسن ای‌وی‌ایکس انگار از سه تا دنیای متفاوت ان.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84809" target="_blank">📅 00:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84808">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بارسای هانسی فلیک واقعا بهترین تیم تاریخه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84808" target="_blank">📅 00:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84807">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یامال یه سانتر کرد توپ رفت جایی که غم نباشه</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84807" target="_blank">📅 23:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84806">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDx56NlJOUQ6ad_1r-dUTreljTo5WoJEiS1c1Povz1yn-r40Syus4lRfeXgnpEJ_p6EPgr1wuY2HTeevcMvRSDklc5gkB0Da9zfzSy7lNl4-dApKzW2q9PT9jkvVG5Gd8b4PsAlFczFoNpgaMLUdK2Eoo_etwjxXvePzI9k9HnmDRz1FHhdVrerHWvCsdfUk0BVxNgNxkrDQh0Ih6D18R3SIn9U6Bp5eS1eRoTjPQN2mdZiYSEaFA6RyyVcSNyN0dOMEauWM4w_kBa0H5W3g_yckFdYgXyVibobagD137jDqDaBapDJFU7CzRVpn7RWMV5UJiCASoasWlt_bV2viWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپویل نکن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84806" target="_blank">📅 23:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84798">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYmi6rdNUbmI2bDMpxEBLaV60Fac2e4l-DuAJNTt6UU0DNJ2xgxrfpG1Z1vybzCDFLh2xgkouEm-8BBvul_eC8vhr1kuZMVPx-kIZywpuFlMlo2gXyEv8svYsQQa61kl2ai6WAW9awxgdIE5Ola0PUppiNSmzPVW0n5GRt9eMbrt3BwZ7LKf-sMZXbkhnUHn89l4fl60nnRh08lxDExOStsHqoiNaV0AT6rA7EptLhaV4vckzGNeqlHfceAw3fHmnkCdPkIfSV-wHV3XjWt5VOBgTA7L0NfLlkabUGh1n8N3AeIEKJkf6up-c6d4osrT8pgqAaJzUfZXcAcHxk9LNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m819OGjybuGg2rA6OZOp4qEdPMo4TQGU7zNChcvxW9b6IjzELL6cCOpElaCQsYVGCgYR9FuyNPRHGxoO9dAKJfwbUQaXgtrsOAxEIn8rB3ZGsbLuhCCP_GOFpk6SF9-JsQz5RHozAGTi7QlLiRmFF7yUHjvouEzPheLo0Ab9tvfJmRkzWegKJIFfR1p40ngMY0CPbuyL5-yvIdCetrFMDIYLPUY0GDHx_i18KkgHvuEHXhXhBQHnHZiZRyvKJpWLYA2uEZgWPjonEosC29NUMO40sz04Vwca9ncWhIqPCypzrHev9mB1P3vk0_UWfXh7W-uKXImel0H5DhXeO7xDAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توی ترب دارن دم و دستگاه لوازمات جنسی مثل دیلدو و واژن مصنوعی و بات پلاگ رو میفروشن.
حتی صندلی و ابزار شکنجه ام موجوده.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84798" target="_blank">📅 22:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84797">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/941b0ce75a.mp4?token=owb1B9VDWyLXoMxZ4R29Ud7oYElUUzhkMTngnkDhNYNYAyuNDL_5V6jtd_Bs5w5NmsyUJqBryYTiWb8HYe3_x6kGP8bZncWRmSuZv7MYQIKjxbKZ9XxRYX_CbmeJi9MzzoKHugpP4JV8GPlNwy7-Q2RJSMa38M4r4pTnoeyrqcAQogdJy9QLgjPlH6CiYima9O8uVR2yrXuaTU2ExwBs2-pj2zUwANgIFPk2LVYSjo2dtyKvLN1t8qQUInuu4gIg0r6_W2KnXaSNAM3lBaWP5mflEqeWQD-xOuD1VhR2Aqh9fM_7mFWgmnFZ_pT7_y2_tq74v48PXKS-Dmah29ZjPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/941b0ce75a.mp4?token=owb1B9VDWyLXoMxZ4R29Ud7oYElUUzhkMTngnkDhNYNYAyuNDL_5V6jtd_Bs5w5NmsyUJqBryYTiWb8HYe3_x6kGP8bZncWRmSuZv7MYQIKjxbKZ9XxRYX_CbmeJi9MzzoKHugpP4JV8GPlNwy7-Q2RJSMa38M4r4pTnoeyrqcAQogdJy9QLgjPlH6CiYima9O8uVR2yrXuaTU2ExwBs2-pj2zUwANgIFPk2LVYSjo2dtyKvLN1t8qQUInuu4gIg0r6_W2KnXaSNAM3lBaWP5mflEqeWQD-xOuD1VhR2Aqh9fM_7mFWgmnFZ_pT7_y2_tq74v48PXKS-Dmah29ZjPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین تی ام واسه خودش و دوست دخترش ۱۸ پرومکس خریده
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84797" target="_blank">📅 22:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84796">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OmifyZpenyJSM8qgYaTTLIE40aK-o5qe5nMI-l0VOicpUlVDIJXNxxn1x7_I3bCXxxjZFop6w5Z9PnhhJ_Ifxu7WAM8DFXoItZJEiAjD2P91wdaVMtzGMWMwlUGuEd23VHc1jgxBmiN31qQU0YcrcZp7Rpg3h_sn9JOx7zDedDnSi5mVmn10ZpyKGgeMEx9fE4Nj9wNw1kiiZPTWeywqFt29OFOyS87E6GX71BZlSr4oPUkTM573gUtXbKoDzxNZQoBF6PoYJz8I_QRRdDE4Kd4OO9ZdcF5G0R3TP6D0yv1vLOhxjxDtN2LuqXMPTANZr8jux4tG2UeYqFwDUvc4tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهردار همجنسگرای شهر مونشن‌گلادباخ المان با یک مرد ایرانی به اسم سیروس دبیر
ازدواج کرد
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84796" target="_blank">📅 21:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84795">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">The Memory</div>
  <div class="tg-doc-extra">Creator (ft Alidanesh & Sahar)</div>
</div>
<a href="https://t.me/funhiphop/84795" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید Creator ( Alidanesh و sahar ) بنام The Memory منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84795" target="_blank">📅 21:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84794">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atRfKiT7923RPIHAo-3e1itiEDEchuR1p3bUyO3GkarCdBQs4QjEq3oG3C03qRDJEu0-rHswXXjhyROKEY8StJSS9omo3mVo9cOI2La1XkLA6kmqag5Y_gaBXvP84x3gjFGkq_L0FL71ENH-u92-CrDF_6GQfckyjhFGVdfqtoGFO8ZOB454l_ZLr6dejC-aydDOuZy2VB7QDvylKQ34lECu10xgd-gBeD7LFYmph_BAlwxkKLPsOiC_CihFLaaNfuvmqQKCTRpI8w7nbu3jLa4vP8VP8XBqXn9br6D7eNga3NmkFOd3usSNyZ1Q4FeT55_kN1CrirwWRbHpK24M-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید Creator ( Alidanesh و sahar ) بنام The Memory منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84794" target="_blank">📅 21:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84793">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f013a68a.mp4?token=dM8AvWtVzu9QQ-H3RXr7YDMDTP3l622pe9At7R48XuNT-0g7RdcBONyt468IaMnLNsz-nKEGzomQbZl4JLGgTRQQMy8GGhRIeI6V-TZyGDETk2dYEJ7XCg1exPbD7LtBJ5Wf4a1-MYViuSrKVLyD_JKoiyEyuQeqoajIpI4d8d1xXY-eHkrgUJ627nTEMjF17iIfXXa4CEoAkFqa_Rm5Ny1a3SRSXHR28B8Yr91nNPCnBbPZ4qLpsEYPWlhWccE8FRdsaEd2a9oZbdJAvsbnHX6FZGXkk-STo6NrszcRYitt4Dyn76ihKXSxrWui7lQHygCcXO_2XB8UKQWKYCUG9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f013a68a.mp4?token=dM8AvWtVzu9QQ-H3RXr7YDMDTP3l622pe9At7R48XuNT-0g7RdcBONyt468IaMnLNsz-nKEGzomQbZl4JLGgTRQQMy8GGhRIeI6V-TZyGDETk2dYEJ7XCg1exPbD7LtBJ5Wf4a1-MYViuSrKVLyD_JKoiyEyuQeqoajIpI4d8d1xXY-eHkrgUJ627nTEMjF17iIfXXa4CEoAkFqa_Rm5Ny1a3SRSXHR28B8Yr91nNPCnBbPZ4qLpsEYPWlhWccE8FRdsaEd2a9oZbdJAvsbnHX6FZGXkk-STo6NrszcRYitt4Dyn76ihKXSxrWui7lQHygCcXO_2XB8UKQWKYCUG9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادستان کرمانشاه: در بازرسی از یک تریلی در مرز پرویزخان، ۹۹ سلاح کمری، ۱۰ کلاشینکف، ۱۷۰۰ فشنگ و ۱۹۸ خشاب کمری کشف شد که در بخش‌های مختلف خودرو جاسازی شده بودند.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84793" target="_blank">📅 20:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84791">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SaGjWX9ujlFcOO9XeBh_X_dhHszMYQ80F0UenGqaCC0FJpLtkKZ3hJINibxwr1KpaCyQOxvRUNEnN8H3hK843qmY7YQJglsr2vnY5BWlz8d0xngTYIA6c2Vzrz8BPKMRwrRwcdycV1kcYRcN_pGr0HlXEOzHglJKup1VHlcFbu8Htx4ePFPYLGRtGkARum-eppGT9cfNtMw-xEz0RmR36nI816QzAd6kDnMMX41GjAovdCOmUzhCdXwKsghE8iV6dtsR0j5baP3OziDT099OMyupyztjBWqAM9aEvvnHsPqYsVHZzUA-s043DcEiXUWp6pFf3gdp70WJSfq43yJhOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SDHDF5JQxxTF177peqX-yh1DSGnj0xqoUkzcE8wD0tXzBbz8DwhLUP9bQ7samvZ4wie6FS4E_EqvllvFV_AhmN6vFhd9PJTnkclco4FjoIDWPE7YI1DWWKxHRS8aBlKKs_TwvbqpLU854WBOOoWhQnDmsB4Ih1xijiQnL7cdsO-AKhtLFRpU3PzUJzCkkL_P8gj_7l-2lSnfTCArERZxC3nW18GFoEj5_98wO612HI2jqrOAZSH_dzltKg_AGvMLoZeUfFqHUXX5X84iZ7sSKJZagczauNc-1I4_8gQQ1PWu3VqFDQP1uyq23SbVmyt7BpGTcoOFChVc1nqrdYqPZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بررسی تخصصی و کامل معنی “سیکتیر”
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84791" target="_blank">📅 20:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84789">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFsaBNQwsr-uIKrH7v0IXMJHSKhOdbpLTUZgNB6uaY-hkhQIPWgtjo1II3BwlulCYQ-UN8up1Mg_s1iT7bTw7_9QRvh2ZVqXlLuVkrpd2-m7dkKTaNrO_aMYqjdFYgSKq-eEzutql5ZnPA2QmsVzo6UOshk6X2tx8cZe58F4NU2I5788PMHsHS1srjeL2UKPgVu0ruLjF7RhfdGo8sN1qUt2HnbvVHS5WmuKyezl-qHV9uZgqDYrCVoahpUe2qcLCXDDgriUrvL3MfDb_yNouXyocfMaZAGAwJ4wzVJau5YR27UngJ_sJ07JprGOUcKZ53SUT9tjdIwhuaS6diIQgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11bb640d1.mp4?token=prWA2hFT81EGjf_JCvdIc7QTUQ_UgojV5RlJq9ESIHYnuKgT2JUb4KUES7V4u8rEvjy8clF40uFoXbbHVXq-knUiSED3o-iHYIGV0b7ijxj0m3SeqCUWbME_SHWoLujyAuyuGyZeSLfCWs6j0X4GQy7a3RE3eDC2vxF7K1ao0yjjIlg2FmdlljKy2zSRJnFektZhI-ZnUd_lCImP8qeoOJTB_jh1Q4TVQv3AsvseJL-yNUwtFQ15FB7ZSQWdJOMeCvBUIx-JXOEnTxmZTNt1IeBMICZWbATF8X1Wza3k2-osUFG4O-LaEKrfBl5Mw7yZcZbYIe8xSptaBhNK-dVv7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11bb640d1.mp4?token=prWA2hFT81EGjf_JCvdIc7QTUQ_UgojV5RlJq9ESIHYnuKgT2JUb4KUES7V4u8rEvjy8clF40uFoXbbHVXq-knUiSED3o-iHYIGV0b7ijxj0m3SeqCUWbME_SHWoLujyAuyuGyZeSLfCWs6j0X4GQy7a3RE3eDC2vxF7K1ao0yjjIlg2FmdlljKy2zSRJnFektZhI-ZnUd_lCImP8qeoOJTB_jh1Q4TVQv3AsvseJL-yNUwtFQ15FB7ZSQWdJOMeCvBUIx-JXOEnTxmZTNt1IeBMICZWbATF8X1Wza3k2-osUFG4O-LaEKrfBl5Mw7yZcZbYIe8xSptaBhNK-dVv7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بعد از اینکه «محمدرضا گلزار» به «رضا عطاران» تیکه انداخت که به خودش نمیرسه تا مردمی جلوه کنه؛ دیشب عطاران با این تیپ توی‌ جشنواره فیلم بوسان کره جنوبی ظاهر شد.
@FunHipHop
| Temsah</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84789" target="_blank">📅 19:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84788">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84788" target="_blank">📅 19:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84787">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELvGFah0tBkUJ30_sPkMpFXKR8A6dwpzIdlGDEkAJnTVo18nMUAcnytLdioA1ON29bZYd54dMwbR6B6FNnXHQCET1GrhjFu2IRlQsr5pnO9dV_yxV150qOwLJ3_tQzNcGsOUldvHZ7vsZ5gfblt_vWFeXIjgwu0zVJXCCOLAPTXh4fmbvPMFlUTS6QCcQF4Dqtnz0AaPSxp6rSrYctDFW_OPtYeWzVu0gbkn-6-esAchhywHO8mEsLs4JULRq5li1b0u4PTYYQf2DSd3LWzCocQMpyfM3EpESm3OkyCflM1tx55Pg9Mfd1Fp2RJ9EjK2Cx4AwDQHoMdGRDGMeBmHCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G21
🅰
🛒
ورود به سایت
👇
✅
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84787" target="_blank">📅 19:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84786">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ:
بزودی درباره ایران تصمیم بزرگی‌ خواهم گرفت.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84786" target="_blank">📅 19:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84785">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d183db41bd.mp4?token=S6k1WMx5oDtyEEWAtIKmVEcKzrBva4Kar2UTM-weNTyYF-xp6x4DyS-gRJTfR3J2yoNpafqwspWdwvLrAy70OjyeMpQZjbmKDaGz3Z1k_IexsIJNNkBKMgQKlnoksg9cJnForGymoYxZIxhYnsioIvNH4Zg0OaEC9sKEG0c10Wgh7-6dGdKeTG0EaIhLHSLZ_N1h56FkJ5xzCr0ApNierabraZkREtoLMqSkjLl4EzqIo2VLA4zV70jHVcDG26j9vc9HN0zktSzTxVYL3ZT-QD-jdC76M9RJ6HURrEaEw-PRnahfaI2CMzTG-Tt24ZNZ1hdONAgwVKrx7zJgLMlPTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d183db41bd.mp4?token=S6k1WMx5oDtyEEWAtIKmVEcKzrBva4Kar2UTM-weNTyYF-xp6x4DyS-gRJTfR3J2yoNpafqwspWdwvLrAy70OjyeMpQZjbmKDaGz3Z1k_IexsIJNNkBKMgQKlnoksg9cJnForGymoYxZIxhYnsioIvNH4Zg0OaEC9sKEG0c10Wgh7-6dGdKeTG0EaIhLHSLZ_N1h56FkJ5xzCr0ApNierabraZkREtoLMqSkjLl4EzqIo2VLA4zV70jHVcDG26j9vc9HN0zktSzTxVYL3ZT-QD-jdC76M9RJ6HURrEaEw-PRnahfaI2CMzTG-Tt24ZNZ1hdONAgwVKrx7zJgLMlPTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهردار کرج:
همه ایرانی‌ها، کرجی هستن ولی خودشون خبر ندارن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84785" target="_blank">📅 18:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84784">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d0c459f41.mp4?token=XhR4PIjHPxiiPtLdTS9-9mMubiEJEEmVbMYZz66aV5y8PBG7z-SxOHdZIgUbx1k2fByBXYZzo8u95rD2fUuCZ7oSIVPUI8ZMoIVhS-HGMBSK8vEEFBe_6iJanwpVg6Wo39em4PWmNMESvsWVKzHw61U-JQqb99u-vwhpWGRGqKGRHuv_uUMfD1NhE_-SOgcY2x59vnniwVS79HX5tPldUUefZhPWOvgeganE6ZckQmqyFXj81KyYHrxQ2lfdOQiaqDKuZ1heXcS_F9HeYv-EfDLAetOMH2KaTDnahad6qlp-Z2XUIiFusv1T2fbQki6-RHTciu6iOFTZaFa8SRnv0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d0c459f41.mp4?token=XhR4PIjHPxiiPtLdTS9-9mMubiEJEEmVbMYZz66aV5y8PBG7z-SxOHdZIgUbx1k2fByBXYZzo8u95rD2fUuCZ7oSIVPUI8ZMoIVhS-HGMBSK8vEEFBe_6iJanwpVg6Wo39em4PWmNMESvsWVKzHw61U-JQqb99u-vwhpWGRGqKGRHuv_uUMfD1NhE_-SOgcY2x59vnniwVS79HX5tPldUUefZhPWOvgeganE6ZckQmqyFXj81KyYHrxQ2lfdOQiaqDKuZ1heXcS_F9HeYv-EfDLAetOMH2KaTDnahad6qlp-Z2XUIiFusv1T2fbQki6-RHTciu6iOFTZaFa8SRnv0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمید سحری برا استقلال و یاسر آسانی کار زده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84784" target="_blank">📅 17:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84780">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O6znJE9ghXi1LhAkI8__MXl53gPkAIoFe4V1Y1AfKXOWd3N93EzJXUBN9Pe4gsVvuDy2pH5K5ZogcEiBDqF95kRvI7Y5C40m0J5P79loTNgZDISFkYTcurf7m3DEGc7Vd3rC-n6n3ycWBpArjB4vHs7iDfHquox2r-4oDhI7bCschwzfyJWvmLVX45ulvycD1IR_1_scDby4H5ZMXiCX9iat4Ge1166GTqHKNr6jsbFdlUs0cpRDGMzeDt0lydzTRFVi1vblxghWvReIT0E3oXTJcS2gVfkAb0CDVmYMWHRsNS4G9_2ewPbycKSMUTd3zmOVayv6i1FPA5zYek9EEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/thHg8IJWMAZ6EFYBYgVyfps33hvl4lvjLQcFtX7_tsErqoSLAMMpYATh_TZv2e_XfcDu-HZBCGONVhhV_bPFdEfXz55gH3ScHYvokWAoc7jan1pBGPGIObz5Z-kHpM7BcaCBoaagqYj2MrYiN90pDUThc9ibNSvwW58FEbgygJf6KCwso0RZa4B0qFZck8OMeWZNBF_zzHwYywFscf3QGzmRhrl3m83xh-hRJsaFzOpCRZ7XKDFm5WAZbe7eb94DAEJo68vayQMm7MC2mPzhbzDkYgZzCK0L-pmQ-JAojEb4aOZOkuDpdH-dFE-ZzZriBSkho1z-NRcjjImJUat6aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrOzCXnWtxxy55nA3zefT3_GKJB4W2MwhgjK7JMfLOZEL7hTpSK3ueqik4xEYGe5AjPOIfYKqLtYnjRczIySXEOCUV2Xxrk1CdqM1Wwnj4YIHjBd4a2yobHcn5IF6x6ZKxy713ZmOrVoKgsM8ek02z5RI0YZOjVybLUVW4SUZIqI0fVIE_6poeRKv9f-VfsmwApw8YQJPGklMu77IkCuoitrK7MWJwqA0sbYSA7s8wF-S-oHi7d4ZF9UIiNXjghB2lW1EXf7L2dqvh8T2O2rav_oJZ2VH_u8zsP2wuROnEh0iANQYvWzdl-OoczJNEuqe858aLk-0AKW-7B-Hwyvzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sy1Wds4HKpXxWNNGOdiiYk4b-5sOT5U3FoNPIZkBnV34VTPh6U5tVOUqN3M34GzW7DpeRf15MZAU8VPH9N6OJdsGwV4sEpWFgq-E0KQvouie3MZGgquwEczCO-XeZfhscGuK-Fez9iSAfqlzDD-xFloz7fw1ixADAUq9TK9U0b2yrBDreC6biN87aMD8P0fs2kwQ6-_exPqXfpI5xKPcfvCzVZtvFctVcmwo_POoglddti6Kczk9ZUWJ0DG-0F6H6_wfTabZsOcrxEMdchf6Pu2YXXFrnR8YAeV8SbZWphsoCRV6uqjH9h7kJyqfaJEootHTHLbDsaRXZlIhofNkvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز یه عکاس فرانسوی تونست از پدیده‌ی زیبای red sprite | رِد اسپرایت ، عکاسی کنه؛
رد اسپریت‌ها نورهای قرمز کوتاه‌مدتی هستن که گاهی بالای ابرهای تندری، تو آسمون دیده میشن.
اونا فقط چند لحظه (هزارم ثانیه) می‌درخشن و معمولاً بعد از رعدوبرق‌های خیلی قوی ظاهر میشن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84780" target="_blank">📅 16:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84779">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd7b86e14.mp4?token=qqyy_SgWjTWd2nXNOrh4O_aBJ85BsS5YzyisK3s1yQSk04Hayxq9sTNGzyMmBX_qML0eRh-Edp01pUBC8ymYFbUsjEhgQPcLS-XHmBSJk9niccI5e8DWeLAztkQe_56a1Dxjdwq2JSearDOokKa7SAeY4jMUr5AXPfLJpnp923K-OJiL9Y5q2mHa8BWE8H9gxU38cZl9NOp3-gdkAFZMqorBlRauxcLRz5zg7gUiwBe-v-N641klDAALObFwVvRFkmpYIYg3N2wqUa804y_pWGRBHElJB0lMBrIn_jxtTHCKqXmLhBedPg4HdxP7RakqDBNO0wIjDkMGzDO--iPmZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd7b86e14.mp4?token=qqyy_SgWjTWd2nXNOrh4O_aBJ85BsS5YzyisK3s1yQSk04Hayxq9sTNGzyMmBX_qML0eRh-Edp01pUBC8ymYFbUsjEhgQPcLS-XHmBSJk9niccI5e8DWeLAztkQe_56a1Dxjdwq2JSearDOokKa7SAeY4jMUr5AXPfLJpnp923K-OJiL9Y5q2mHa8BWE8H9gxU38cZl9NOp3-gdkAFZMqorBlRauxcLRz5zg7gUiwBe-v-N641klDAALObFwVvRFkmpYIYg3N2wqUa804y_pWGRBHElJB0lMBrIn_jxtTHCKqXmLhBedPg4HdxP7RakqDBNO0wIjDkMGzDO--iPmZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست یه خانوم از اثار کتک خوردنش و 10 هزار کامنت این شکلی...
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84779" target="_blank">📅 15:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84778">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMehdi</strong></div>
<div class="tg-text">بنظرت لیگ دانش آموزان بلاروس پخش زنده داره؟</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84778" target="_blank">📅 15:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84777">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مرگ دختر جوان در ژاپن بر اثر سقوط یک زن از طبقه یازدهم
زنی ۲۹ ساله که قصد خودکشی داشت، از طبقه یازدهم یک ساختمان به پایین پرید و روی دختری رهگذر سقوط کرد دختر جوان جان باخت، اما این زن زنده ماند؛ گفته می‌شود این زن به اعدام محکوم خواهد شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84777" target="_blank">📅 14:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84776">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کل مصاحبه گلزار فقط اونجاش که گفت اینایی که پولدارن ولی مثلا برا مردمی بودن به خودشون نمیرسن و درویشی زندگی میکنن کسخلن
تا خود صبح باهاش موافقم، کصکش پول زندگی خوب داری چته مثل کیرخر زندگی میکنی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84776" target="_blank">📅 12:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84775">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a93f041f2c.mp4?token=H3CKOHytNKRypgY2-Ln9ep6npVBi9DMe9czzplRnivuPwE3kiJxMCUSCWEan4gJ7uWRWAVA6xA2OgTY-nNlAmgGOeRDbUxW1hfU3irB-B4_q-_5Fojrxs-abrOItwGcjEho9nZ4yE9GAKVWUr9rTX2-M7tqIE6tbtVARrIEEcsRAoANKmzKy_drLGpk7vC9TPEY_SHhldAvUJKjWRSysbQPXaPfhSok_rgbs3qLH_wTXPh9M2QOVfiyroLPyp1Ci9hGEdKMw2RzpZ2k29EAheaIouc_gqgYlQUATUfcMJYUINoZ9bRKTWDom2m-NeekV7mcvnbShQcg1wTo-glTPZazSjvie0k6TmOahlX_fzUmie1PmoT4ov8PUMLy8G0QyQuzcFfRIhTjT6KFSLhr5FQyR8cc2CxJbavL9BD_JbNB5VkDNxiZ-yHaJjByVXp2u3zYCcGTbAw0uohDdpZCrI3wyLiuG7u0fJa-RocP0ZINVHl5rrUBU59meiKiTU1ERidzroGPIaYtFk4pSi_bwlc1QKTdlb9t6cJ2nXW_RGrVt-x2RAq6b6Uzlg8aSVZCHuNZml1fZ-zRgFmk9IUiroIOYi6Nvy2tIPHhgKV03fuKEcZu96PBqLP7lnZ-wlyyf_l5ibyldYyKRV937Pkdgc7kjdLEQ6IR1ClEMR6vMCs0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a93f041f2c.mp4?token=H3CKOHytNKRypgY2-Ln9ep6npVBi9DMe9czzplRnivuPwE3kiJxMCUSCWEan4gJ7uWRWAVA6xA2OgTY-nNlAmgGOeRDbUxW1hfU3irB-B4_q-_5Fojrxs-abrOItwGcjEho9nZ4yE9GAKVWUr9rTX2-M7tqIE6tbtVARrIEEcsRAoANKmzKy_drLGpk7vC9TPEY_SHhldAvUJKjWRSysbQPXaPfhSok_rgbs3qLH_wTXPh9M2QOVfiyroLPyp1Ci9hGEdKMw2RzpZ2k29EAheaIouc_gqgYlQUATUfcMJYUINoZ9bRKTWDom2m-NeekV7mcvnbShQcg1wTo-glTPZazSjvie0k6TmOahlX_fzUmie1PmoT4ov8PUMLy8G0QyQuzcFfRIhTjT6KFSLhr5FQyR8cc2CxJbavL9BD_JbNB5VkDNxiZ-yHaJjByVXp2u3zYCcGTbAw0uohDdpZCrI3wyLiuG7u0fJa-RocP0ZINVHl5rrUBU59meiKiTU1ERidzroGPIaYtFk4pSi_bwlc1QKTdlb9t6cJ2nXW_RGrVt-x2RAq6b6Uzlg8aSVZCHuNZml1fZ-zRgFmk9IUiroIOYi6Nvy2tIPHhgKV03fuKEcZu96PBqLP7lnZ-wlyyf_l5ibyldYyKRV937Pkdgc7kjdLEQ6IR1ClEMR6vMCs0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فنای گالاتاسرای دیشب جلو هتل بارسا:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84775" target="_blank">📅 11:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84774">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یعنی هنوز ایرانی ای وجود داره که فیسبوک استفاده کنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84774" target="_blank">📅 11:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84773">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗺𝗶𝗻</strong></div>
<div class="tg-text">ما سیاه پوستیم((((؛
همونایی که…
بغض نمیذاره حرف بزنم
حرف دلته؟
خب حمایت کن سیاه پوستا به حمایت نیاز دارن((((؛</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84773" target="_blank">📅 11:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84772">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">من دقت کردم از وقتی فوتبالیست های خوب دنیا سیاه پوستا شدن برکت از این ورزش رفته، چرا انقدر عمر حرفه ای ورزشتون تو فوتبال کوتاهه شما سیه چرده ها، ملت هنوز با مسی و رونالدویی که تو لیگای پرت دنیا بازی میکنن کری میخونن واسه هم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84772" target="_blank">📅 11:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84771">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f888102f5.mp4?token=SSikO4_C0lIwxM6JCuKLjmGG015Hf4tJ3f0DPfQOE2FzFC2V4d7FOg2NQMmQKB3G58bDhEuEoZlEJ_7ZRwCxLrkuZ6FjwxeCzbTEBmOM5DplW-B6jQ5tYaVmw0LBP5RJ2IoB9yzmfhj8Jg0XQCrb1Qun-w7BbcEUcpCftWj6G-L2kgNom6EflfHeVqdCBlK8v_LhLTYe1_eXjWSUIn7jA90iSoXXFQvVlJ75lklxvAEPgFHSy7vfCIN-L0RP7HYpsS_bjrHjLUy_7COcEA66a_cDT2ay4L_ag6koB2BrBGb275e0VetGUtmpfNtqa6FvXJBnlIVwiSu7a4bOKzF3Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f888102f5.mp4?token=SSikO4_C0lIwxM6JCuKLjmGG015Hf4tJ3f0DPfQOE2FzFC2V4d7FOg2NQMmQKB3G58bDhEuEoZlEJ_7ZRwCxLrkuZ6FjwxeCzbTEBmOM5DplW-B6jQ5tYaVmw0LBP5RJ2IoB9yzmfhj8Jg0XQCrb1Qun-w7BbcEUcpCftWj6G-L2kgNom6EflfHeVqdCBlK8v_LhLTYe1_eXjWSUIn7jA90iSoXXFQvVlJ75lklxvAEPgFHSy7vfCIN-L0RP7HYpsS_bjrHjLUy_7COcEA66a_cDT2ay4L_ag6koB2BrBGb275e0VetGUtmpfNtqa6FvXJBnlIVwiSu7a4bOKzF3Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: شعار موردعلاقه‌ ام «گی‌ها حامی فلسطین هستند!» می‌دانید اگر گی باشید، تو فلسطین چه بلایی سرتان می‌آورند؟ شما را از بالای ساختمان به پایین پرت می‌کنند. شما را به بالای بلندترین ساختمانی که دارند می‌برند . البته ساختمان چندان بلندی هم ندارند ولی از آنجا به پایین پرتتان می‌کنند. با این‌ حال، مدام می‌بینم گی‌ها از فلسطین حمایت می‌کنند!»
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84771" target="_blank">📅 11:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84770">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qo_p6ADxdbwY11wxqazD9mq8siCR3NYTgMepx3YyelMJ2UR3Js4cqFJtPpvWAF7Di9V9mAd97gJGeC13JQUmZvH1p-1yX30q36QT1ETl6fmw9dRM4VOqYvymg1AH82yebPboLkXhYsMkAC8XAaRotkZMQk-83vp9dsac-h55-IOlwMr0jAD94Fcp1MDEm1zPjZiho_tzlVSoxGr1oAu9fJcTQ9xGe6enK_r6F-EaB72ypbbUvF4B2SRb6f3KDvkwm9bGtJMZ_jqZNkmeDKFQVzUNb_jay1IPw4Wc5hJZPeR5I_BQWla9JJTBEfUVnkMkn8JYO-gupNDoT5cTpbS05w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت دیوار پر شده از آگهی فروش سبدهای گل دخترهایی که به مناسبت روز دختر، جعبه گل هدیه گرفته‌اند.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84770" target="_blank">📅 10:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84769">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بازیگر نقش پسر والتر وایت در سریال بریکینگ بد، بر اثر خودکشی در ۳۴ سالگی درگذشت.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84769" target="_blank">📅 10:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84768">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9441c5ec98.mp4?token=S7jEpkKmnJx1C5aF_B4z6YeWjnPtLJteDKzrS0UdlAnA7-BwbfzMb2fH1_HFBCwhJLXIjoPYOuKwHek0DiVlPe1YYrqDtWnZEflBffIgVxrQ-DrF1QSR6490a07MLwOSoby9_4fJGBg8jBVPbpOkA1HXuR3aiuMJVxl8so9xEflXfGk0eq2-k4zyelmyNQFbsw_2HGzKqJEHtauEloxWiJnvXzKFw6xz1extNzHfWxfdLxKkPR0sY-o_NKHgWqAYsTKFfKgVPCsJb9f93Z7ZYBNADQHOfGmUPfnn6YJrkLtfxGGrehUGwlpxO5WhzJ5aRK9NoHmrrE90KYVkKZ84pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9441c5ec98.mp4?token=S7jEpkKmnJx1C5aF_B4z6YeWjnPtLJteDKzrS0UdlAnA7-BwbfzMb2fH1_HFBCwhJLXIjoPYOuKwHek0DiVlPe1YYrqDtWnZEflBffIgVxrQ-DrF1QSR6490a07MLwOSoby9_4fJGBg8jBVPbpOkA1HXuR3aiuMJVxl8so9xEflXfGk0eq2-k4zyelmyNQFbsw_2HGzKqJEHtauEloxWiJnvXzKFw6xz1extNzHfWxfdLxKkPR0sY-o_NKHgWqAYsTKFfKgVPCsJb9f93Z7ZYBNADQHOfGmUPfnn6YJrkLtfxGGrehUGwlpxO5WhzJ5aRK9NoHmrrE90KYVkKZ84pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل مسی اسرائیلی نباشیم
☝️
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84768" target="_blank">📅 10:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84767">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ix1BU2tjXuZK8dfUTnyygLAA1Unfktj5qDLFluM0QMIean853S1iz8sAa89ULXpPrBzrSBz3U7aYCf6QxaLa-pVEvYJ7VoxAGmXkTF5JDGMcWdCN5fRmYfYWn0uqejpgP1vOriaR2nwPU8hA1GbRoSfjqXcDVoYYFaa_KgZdejLr51vk5tTYyg6Tg2KET3YGShnd7yNitDD_a2oD5eGk31hsLt81jdKJBaMv0GrMEVfN_u1LwpdK3hWfeEOrB6EHzbwu5Vqsq6w8KZalYzxUL8Wo6JbUJ2aO16N_NuajhTnUWnUccq7AzDZYN0PAQYk0NPOzze4_FRrRUWlgqX1-dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
الغرافه  - استقلال
🌎
ساعت ۲۱:۴۵
⚽️
تراکتور  - الشمال
🌎
ساعت ۱۹:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r21
🔗
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84767" target="_blank">📅 10:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84766">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7babb9a577.mp4?token=HOwTZcIPnUUGfKuXq1qr93sT1tR9eiJSsL_9j_jUWS6H9k2m0Jmf5lBuB4ZnJXcGFL2m83Q2RbPZqhW4PB9zxRwRJE3g5mhLD9SiFxQwkWVtBDmto4uKFFdyMosWN-FOi7a9qCBqh2q1kyyDV9Ldy6S9E3pzJPH9YEgxul2cm7gvyXstvg90boL6ASNCrQaeZDGgX10YIYQtW_8ib49e-l3Uno5lJcCDO7q2kKQSQoQrzfHT7BCU0BWedG9lQ0KQdITzDg2j-59LadSk2tY7VZZOECaF0eBieaSKv9xHMLzJbsu1HMWTqxgLTdczrwn0QkimdTe2TT0E4mnEY0ATcg1FH-PvyZbnmCuHdCctJhWAAU2yTnLlUMY5iCTkzjfAx3yM1Fi6iEwHZs_X1Bs7SXPn8FX3ETKq4g_qsmcQ_dtJ2QJHLaThuYhkwT27FqInPJ8fO-uy_mMZHYgE95RxIdrdzLXwNpVLbEu3k3O3bFCazmOsOOLJnanvrh6ohPSUR1Fk7dzS_RKVA4wsqdPyrLPnQ1Jv-mJMQeIXP-W9LuuBoz70BbfySaqdYi8pRDVaSrsruoWORwCZlTtK7n5k8njMLrwUZqhlwZhucLnt5fndttdcbDuk1LdWXUyCakHdEuS-Q5PWifnRS4OY7QiHgDUq4c3fE3rW_8Bdl3Sw4bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7babb9a577.mp4?token=HOwTZcIPnUUGfKuXq1qr93sT1tR9eiJSsL_9j_jUWS6H9k2m0Jmf5lBuB4ZnJXcGFL2m83Q2RbPZqhW4PB9zxRwRJE3g5mhLD9SiFxQwkWVtBDmto4uKFFdyMosWN-FOi7a9qCBqh2q1kyyDV9Ldy6S9E3pzJPH9YEgxul2cm7gvyXstvg90boL6ASNCrQaeZDGgX10YIYQtW_8ib49e-l3Uno5lJcCDO7q2kKQSQoQrzfHT7BCU0BWedG9lQ0KQdITzDg2j-59LadSk2tY7VZZOECaF0eBieaSKv9xHMLzJbsu1HMWTqxgLTdczrwn0QkimdTe2TT0E4mnEY0ATcg1FH-PvyZbnmCuHdCctJhWAAU2yTnLlUMY5iCTkzjfAx3yM1Fi6iEwHZs_X1Bs7SXPn8FX3ETKq4g_qsmcQ_dtJ2QJHLaThuYhkwT27FqInPJ8fO-uy_mMZHYgE95RxIdrdzLXwNpVLbEu3k3O3bFCazmOsOOLJnanvrh6ohPSUR1Fk7dzS_RKVA4wsqdPyrLPnQ1Jv-mJMQeIXP-W9LuuBoz70BbfySaqdYi8pRDVaSrsruoWORwCZlTtK7n5k8njMLrwUZqhlwZhucLnt5fndttdcbDuk1LdWXUyCakHdEuS-Q5PWifnRS4OY7QiHgDUq4c3fE3rW_8Bdl3Sw4bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه بادیگاردا این یارو رپره میگفتن خلوت کنید آقای بولینه و نمیذاشتن طرف نزدیک بشه، دو هفته مغزمون گاییده نمیشد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84766" target="_blank">📅 08:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84764">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f656ec5109.mp4?token=gxsLy9vEe5yq88ZEkkh5I0UE9di3hJ59Ha1qVIDe9WLTw7EzQIAqghWYiXGXFyCbZLrEgDR2oSUPnFK4QlQ1Ky9zP5QItDfpm46oDm1_q8HZJQNT6FJJHV9GmQKds0Fsnt7mdr3MwrcwkvZ7fRPp5ve9z4_XRngi3Vdup0W3J-cTnAuAHUMKxiyE5l-RZRNMktQS_xUZR9aGDWKIACv5JZpd9GZXyPt_Jdgw1MRUQd7pUGtaG4yBDp4-s2gKQbV7ESW3p7X0IFRVwO3H39Ea6q9BfQyKbvIDvEm1yaPmruqDJkMyDd88EFU-1w8EYNJUfqXXmJKKmn-c3-SBvlstng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f656ec5109.mp4?token=gxsLy9vEe5yq88ZEkkh5I0UE9di3hJ59Ha1qVIDe9WLTw7EzQIAqghWYiXGXFyCbZLrEgDR2oSUPnFK4QlQ1Ky9zP5QItDfpm46oDm1_q8HZJQNT6FJJHV9GmQKds0Fsnt7mdr3MwrcwkvZ7fRPp5ve9z4_XRngi3Vdup0W3J-cTnAuAHUMKxiyE5l-RZRNMktQS_xUZR9aGDWKIACv5JZpd9GZXyPt_Jdgw1MRUQd7pUGtaG4yBDp4-s2gKQbV7ESW3p7X0IFRVwO3H39Ea6q9BfQyKbvIDvEm1yaPmruqDJkMyDd88EFU-1w8EYNJUfqXXmJKKmn-c3-SBvlstng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تورکا حسابی خایه کردن از بارسلونا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84764" target="_blank">📅 07:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84763">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aae0b77801.mp4?token=keV2gOOAwKpiltBc_-4d5R-RRiUtQrgaCwqRTGOG2fXYzOyqQj8ICxfhbLNYjE6qmvdojG89PHGDrvQnLRgoLQa-iiZLQZOgjK80ZBzVUqxUPqru8xHg0qvDznZ-kEmt2jWeQM-Wvp7dvctqqOQKFlUOLsEuSvOzwiqkmOiZOBTugOjsd3TPlPSWETjZ_NCJi9Ia1M5z44M-GHf5A_dMkxxG4g6voiaGEbF_IYME-bvd28gmJwjCALigM5owVz0xkStj8CwogKXr23qSTXuOgZhShnL2EuFrPnwCcw_kbJL-4zbM6xxnIrNJ5rDCHQ_eMWLM2Ey1QOKq97HLMIjMjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aae0b77801.mp4?token=keV2gOOAwKpiltBc_-4d5R-RRiUtQrgaCwqRTGOG2fXYzOyqQj8ICxfhbLNYjE6qmvdojG89PHGDrvQnLRgoLQa-iiZLQZOgjK80ZBzVUqxUPqru8xHg0qvDznZ-kEmt2jWeQM-Wvp7dvctqqOQKFlUOLsEuSvOzwiqkmOiZOBTugOjsd3TPlPSWETjZ_NCJi9Ia1M5z44M-GHf5A_dMkxxG4g6voiaGEbF_IYME-bvd28gmJwjCALigM5owVz0xkStj8CwogKXr23qSTXuOgZhShnL2EuFrPnwCcw_kbJL-4zbM6xxnIrNJ5rDCHQ_eMWLM2Ey1QOKq97HLMIjMjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثال عملی سخت کار نکن هوشمندانه کار کن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84763" target="_blank">📅 01:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84762">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXgVRQa7a9GyvGr_eMO8qFM1-V_GoUMaAuCX_s-OTIX0X6n1TI2Hk1z_SFWtbYXEbOspO6AUGyr5hvUMJqwONJcWSLLLMueMvSF6rYkxUD1PYfylFJ1O52fcYuPMs-i4hEkY8QSLVOgc3QRWMIwZKEvJZENm3Ki6T_4eYwe0yWTeZuAVAGsw01Ypa4A6jWIL-l7avwTVyC8F61OLAGNPffYbxvEA10zQ47Cea2aM0D9l0dEx9kF3D7bVz_GQqdcORYLrFo5W_omrOxTEqCrf4cpf_BdrNZZdNkss_BFBlQ40cL_JO2a0zWgTJ08SXntJYpqYGL5elA8x4sh-ITsNEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84762" target="_blank">📅 00:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84761">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خدابیامرز نقشش تو سریال اینطوری بود که اگه اون لحظه جلو آدم سبز میشد تیکه تیکه اش میکردی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84761" target="_blank">📅 00:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84760">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snpQy_DsH2PjNH1fEo4tPDsoir17Mm6NAhiH9-YAbpm7yuxcnZQUNVH0JvO8ZKfPm8zWjy9rLppzF4ob66DO8YEEsdHAQtNGlG5ItbLpB2ZrvJ1a03CmkC0vbtWvzuhcV1eUIzk7LjETrraL-bZRnESRgaFiIXw1CJKxqoTIJoMOoitqBFEt0xFQHzvbaGGCve9rWy1VPIzUysIby9Dym5vls8qFu4tqoPEngMI5eoZlcAJCbAK5-aJXPFYfGz8NLYV-pxIKFjVLso_yswzzPdqfKiTlhkMe15_CmvTSRV3g_b60DApbsn3KUF9OvFQMcL_uijcuMUkG3NKlLgqumw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیگر نقش پسر والتر وایت در سریال بریکینگ بد، بر اثر خودکشی در ۳۴ سالگی درگذشت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/84760" target="_blank">📅 00:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84757">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEWh2Praz7b0-6oHI9BPnyp4zzX1Ih5-2Ql20BsTL3WBYAxjRgQG6-aNaGbRvQocTiUE82OWrQmBA5RLmwC7BgwQlEw1D5jbDkr2DA4kLSJlPR4Fw9D7C-W6UIyiejKLF3jvSe_CoL4d-g_mEq0Bw3zDUKlv-We4tiRUvXTW2nFY-QRt1SBn67O-74w175tJ3IDmENdHZdSRBiHsR_acto_zMPNXV-PYlw6muBit7cjUAJMjL2jVESL4oQ9VtSgWPcuJVP55G8gWZS09qn58RolEZh245j1HBki7sbg-tCr3V0zrYtKZbdAUypr2BjOTiDrlzutusLnFs--o8l0tgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داشتم زیر استرس جون میدادم حاجی</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84757" target="_blank">📅 23:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84756">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1lc2YXOce293jtpKfwrcd7gRkAXHHJ4kK9wQ3LPUfLykxv5I-QSGYGDSq_sZU1XokUpSjentVaAwbUKJkmQ4AQ6cEhBFUTmzYjcOy0LPbZoz_1DRr4A0sA2VC4_RHMKGsSdzLLmi3xWCqfqnkVU45eDFy40hG7SNRjO8cj10W1McQStAIP2ifPXnHzp8spwXz8b8Y4a4DvFJk5CrfbRiVos4wAcJR9lRwhSzS2ny6Rawp6aL4vOLzsmkNRb0s2f-MnUqtfQCHkQIqmzJoDMXuxg743teVYixQhm04RYc455059UFTsDnrMfow2nsj6-08hHXPNcbx3jQEe3Wsxd_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید فدایی و شاپور و رفیقشون ارین بختیاری
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84756" target="_blank">📅 23:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84755">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حبیب کیرتو بخورم</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84755" target="_blank">📅 23:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84754">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amjloHpR5BMOnUPwtzp9Etq8ljh7vJtxnIrh20sbSUKqLRYzFW2ICs_73okAQkcBDizeihfKhtAXdOOeCXz_CXhLSvS8A-W2ZWKC4gPzmwk_DuMPNNzJwVRHb0fHry_l2_jDQCty0SeXur_8cIzNaPng4cK0onH6wbwOl6D6NYqoPezqhoPC9zO0i34_lEnbI8LtrFELeMk3IUZKqfu29ySLcpzbL6s8OZMUIY2kjQOdW7ogQaodok8QU4lfrhHfd8UDfWX6sVMbAbiJU1zLvIoY9p40dtvZFFBiuC--Z35nXQjYzoSrMmd11KAeVuD7sRsNGYNCuGviOxGAdHCoqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیافه رو
😂
😂</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84754" target="_blank">📅 23:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84751">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هنوزم نمیتونم درک کنم چرا هلدینگ دو میلیون دلار داد این سعید دالگخیزان رو بخره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84751" target="_blank">📅 23:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84750">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1K8dKHMWamk6CNLd_FqiO9s5qQ783XVqvu21t9q3pc61KMn0Fxb6QI7vZ6DonHjpjBKFUrEoN2w_DnhJjNzeiuTlIwc24gtsm_BF2JxR-8TWP0r8ZchQ7H0bq5OGLNpp2lTlGPE_gJ8eZAmwXbGOAqX6zfUi1F7n2N6bE_vVGKFzFiex0KWK799P1hkjwb6jSqjvBIJ4xDVyWNFMfFOvso1LkId-U_MGWSoWw4MIPzf569tMyh8B-UUBRGky3LoYC8cFKNkqT8Fdk62puIXmFgCdk0l4229DmSacYZoozjnhH6W46WkVLOPmg5wrX6u71Dl9QerakoHTMUo2Br_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین روزاس اسرائیل فک کنه یاسر آسانی لانچره بزنتش.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/84750" target="_blank">📅 22:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84749">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">همین روزاس اسرائیل فک کنه یاسر آسانی لانچره بزنتش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84749" target="_blank">📅 22:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84746">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940390f975.mp4?token=RFDLTL4ybvavoVJl-pXJrdTKAdnymSz2TNcmqWGBeiIz4qLKBFVSUGENfHMslfOSPpvgQJMjfeiYtz9bvDVcSMZqV033YpR29dMz_J0_0B3nRiU_HLR9X5jEDwqY9bh8k3gSM7WGa--X_wd48brqeeEPiHTuny3DlZC5TpfqTfyZs_s0GxyPqaA9dPaExO2RrxttMwf6rjO8c9O-EjI-UkGHCWarglg2OM0yXT7IF6LUZSwqUElvYFD3NQi3SdQO9OFVd_m0EZmH371TcWcgFdT0m4gPRCLENBgCwfgCjm2xjGuH4OdFH4ylbBvFsffys8J5NTNdLK3fsKfM7BYosQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940390f975.mp4?token=RFDLTL4ybvavoVJl-pXJrdTKAdnymSz2TNcmqWGBeiIz4qLKBFVSUGENfHMslfOSPpvgQJMjfeiYtz9bvDVcSMZqV033YpR29dMz_J0_0B3nRiU_HLR9X5jEDwqY9bh8k3gSM7WGa--X_wd48brqeeEPiHTuny3DlZC5TpfqTfyZs_s0GxyPqaA9dPaExO2RrxttMwf6rjO8c9O-EjI-UkGHCWarglg2OM0yXT7IF6LUZSwqUElvYFD3NQi3SdQO9OFVd_m0EZmH371TcWcgFdT0m4gPRCLENBgCwfgCjm2xjGuH4OdFH4ylbBvFsffys8J5NTNdLK3fsKfM7BYosQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84746" target="_blank">📅 22:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84745">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c170193b1b.mp4?token=iybc-3sSpHiMVlJ4uL_FLP8qgIivMXKCJI9qUrHrsWWAAxxfTnWHOvlmIs9JAWG0QxGH2jPiaFblGVVOoV6zX80ujTyrNX36rnzCMRe2EF77I2u0O6dZt9IV-LKzuKQ2b3EBro8QhrXoMdmYZOe5owvJeMFxGA1nLCdoRl_4Vt-wXQ0qPQfaLS-FAdGG0TvkCMuiTVOikPiAremVRL0oBoGuJ_U0fcyVY6pStjFeYB7CtfgESV2uEPwsNpC5R-v5zmjM3O3vXH_SNi7cT4FRkURT-CIpqpKTiiFFLqfbUzDvBVjx6xul1kGhC5XcBsofZ3zLPMZFap0n3Ug73zJwjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c170193b1b.mp4?token=iybc-3sSpHiMVlJ4uL_FLP8qgIivMXKCJI9qUrHrsWWAAxxfTnWHOvlmIs9JAWG0QxGH2jPiaFblGVVOoV6zX80ujTyrNX36rnzCMRe2EF77I2u0O6dZt9IV-LKzuKQ2b3EBro8QhrXoMdmYZOe5owvJeMFxGA1nLCdoRl_4Vt-wXQ0qPQfaLS-FAdGG0TvkCMuiTVOikPiAremVRL0oBoGuJ_U0fcyVY6pStjFeYB7CtfgESV2uEPwsNpC5R-v5zmjM3O3vXH_SNi7cT4FRkURT-CIpqpKTiiFFLqfbUzDvBVjx6xul1kGhC5XcBsofZ3zLPMZFap0n3Ug73zJwjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی النصر بخاطر آژیر خط امنیتی (احتمال حمله حوثی ها به ریاض) به تعویق افتاد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84745" target="_blank">📅 22:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84744">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بازی پرسپولیس الهلال بخاطر حملات موشکی حوثی های یمن به عربستان لغو شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84744" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84743">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ناموسا آسانی حقش لیگ ایران نیست</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84743" target="_blank">📅 22:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84740">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">استقلال یه بازیکن داره اسمش احمدی عه، یه بازی قبل دربی رفت سال پیش مصدوم شد، ساپینتو میگفت به دربی میرسه، یسال گذشته هنوز مصدومه</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84740" target="_blank">📅 22:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84737">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آسانی نیست استقلال در سطح تیم سالن بچه محلای ما بازی میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84737" target="_blank">📅 22:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84735">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بازی استقلال تو آسیا شروع شد...
گزارش لایو با چاقال اسپورت
🤣
🤣
👇
@Chaghalsport</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84735" target="_blank">📅 21:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84734">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrLlkanB7yxnU7KS5JKNGMzuV9QGAB2BA9jtQCa7n7gL0L31t2rT-EbExhzPeuACJc77E8TqJsUqIXb5NZRAV6T_lgySkdN5dr26-ulBD7Pm_tt0nuvZaFj4r4vFERgmheYnr2Qz7BYKBkdR1yF4dMF2gL7n91r-o-oCUprT4Yq1VbDmHeDT0c6IRn9wUze-mOoplp9eva-Z4fIbwPcmVTlTQcya_1OaF24vwc1IxE6tFsRSkJN09A2c_a8pM8nnBQ7Fo0pNRjoLgGkkpirbF5LkCW_UwiYR9lbS5EGhgdT0kfNFuF_hXluDiwtEMv0r6C8PvmnoEOZ6RGCScGfRWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب پرسپولیس برای بازی امشبش جلو النصر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84734" target="_blank">📅 21:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84733">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bff24e8c4.mp4?token=YiBmcyve4if7Dtsz00uXhaKD_ytny-3LWCn2pC6dMKqrrHqciN0COwhyPHIprw_Z0-sz2Ii-Pqy4JK3kk9PnK6rMFjilszHb48mkOcNaJEej0Rig2x0pM7jmwmaywmj9SlTwjosJmLxsM99iQMtuhVLLwli3qOX-fXP869C5z6NrCHZ7OlsofNyIUjpHrl-7UZpLjLv4ZJjNUsSpnVXW3at7hp69YN9ymeZyhmHht-e66M_gsTMyYH5IkhbSeFAwhrpPHiPeTJN07J4N6KI-4rRqqtyk1XX5Xgtpv08KWpBmNg8RRvC7maGH13h1KLLVxCBaYXV0zC2Ax1xUuMWDfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bff24e8c4.mp4?token=YiBmcyve4if7Dtsz00uXhaKD_ytny-3LWCn2pC6dMKqrrHqciN0COwhyPHIprw_Z0-sz2Ii-Pqy4JK3kk9PnK6rMFjilszHb48mkOcNaJEej0Rig2x0pM7jmwmaywmj9SlTwjosJmLxsM99iQMtuhVLLwli3qOX-fXP869C5z6NrCHZ7OlsofNyIUjpHrl-7UZpLjLv4ZJjNUsSpnVXW3at7hp69YN9ymeZyhmHht-e66M_gsTMyYH5IkhbSeFAwhrpPHiPeTJN07J4N6KI-4rRqqtyk1XX5Xgtpv08KWpBmNg8RRvC7maGH13h1KLLVxCBaYXV0zC2Ax1xUuMWDfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا چیکارش دارید خودش دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84733" target="_blank">📅 21:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84732">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">هالند راجب شایعات سقوط منچسترسیتی و جدا شدنش از سیتی: خب اگه سیتی سقوط کنه مسی باید نگران بشه، چون من برم چمپیونشیپ رکورد ۹۲ گل تو یسالش تو خطر میفته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84732" target="_blank">📅 20:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84731">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxJlRk7r5qSz-_oB5W4x6p-1OcCYLw6Meg-Fp0NN9TswN_ljlrSpTl1MEGe3gAklwCpXbg_IQQ_32o8ZvIMAIzYJ0Tf-Zgk4aQcYNmsigBhSPcxKcZxAIWjxz6dYkQVlERxsbiEsr9m_hByzifTTW5JxlltNdmmhxrKYWpXzZAcZCnpfvDEEG4PhImxSX1VyBEd5EPDb0LMwXyI7b3yCh_Umn7kuqcQNxLdHzW5LsjdOHexC6e29dLykt3i19WeCIEWfNwPyq03sgOaHUPl8xDyuQ5H_GNnfYPB1xstFh6rzc3qQe0TImbfrJ-8BfSFKHLKOGo19n6fCEXAxSdqwKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران رتبه ۴۵۹ بهترین شهرای جهان رو با کمال شایستگی کسب کرد‌
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84731" target="_blank">📅 20:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84730">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eecaea14fc.mp4?token=CVydXtFXDjlc8M2_NC54C7lDwEL3nBWEwml2FAKVtt6LS25m82MM30wHJunyqK5MgvhYgmZQ4Sm3zKGWlefPfn99kheyhnl0CMEhprOebQnUvHFfKggMczcPxG9lxsqpcB6pSE84jojGKVmHDPoY5YSombfMaMFiZ1Y9WyDICA3z6QMaBdGvaT0oEEFp-1FQZlGoC5VVnzJ8ceARlCid9f_9lsokW0cTkbIQgjXXQXTDpsEGeGwRyhH99HzilJ41M6V653FxFzNXOKBUeR1X7CJC4iycAKDODubLOJ8XV3oltiTFc4eu8l3T4au3_D2oAwTxriPjgrPTA_MuZF1Bew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eecaea14fc.mp4?token=CVydXtFXDjlc8M2_NC54C7lDwEL3nBWEwml2FAKVtt6LS25m82MM30wHJunyqK5MgvhYgmZQ4Sm3zKGWlefPfn99kheyhnl0CMEhprOebQnUvHFfKggMczcPxG9lxsqpcB6pSE84jojGKVmHDPoY5YSombfMaMFiZ1Y9WyDICA3z6QMaBdGvaT0oEEFp-1FQZlGoC5VVnzJ8ceARlCid9f_9lsokW0cTkbIQgjXXQXTDpsEGeGwRyhH99HzilJ41M6V653FxFzNXOKBUeR1X7CJC4iycAKDODubLOJ8XV3oltiTFc4eu8l3T4au3_D2oAwTxriPjgrPTA_MuZF1Bew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فک کن برا ۲۵ تومن حقوق مجبور باشی بری تو باغ وحش درس بدی، معلما واقعا بدبختن حاجی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84730" target="_blank">📅 19:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84729">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNaIZ53bCyb71ydyqjAzqHsb6xg6bJEXRLQ8v99TXQaRv3nMUBWUphVKMStWBgMA7-DJJIPry-idqp6C-PXV-I_AjinqEThcK-w8JQSprEoQo_8V-aJ8lXF8May3XYdxeSJHmNCxT6QiQG7ude9Ar1lWf-0hfsvZ9B3jbI_3tk8L2gZp7Zcoai9potIz4tTH4hkoJqrR87wu3rOyE7xxLzNZ0sqLhNTrbgyM4nx-RssxBkHHfNpp_VAv8zE-6XhhX4Ie3SBUCFxRGRbD1HzrHAXYtbt1BD4WUNiVCaQJlyP3QKpxPIr0vYOkzwOfkwkGMxadFmgi2fy68gBxI6XlfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G20
🅰
🛒
ورود به سایت
👇
✅
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84729" target="_blank">📅 19:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84728">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شاهین نجفی میخواد بیاد استانبول، دسترسی بهش راحت تره لطفا با راکت بزنیدش</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84728" target="_blank">📅 19:10 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
