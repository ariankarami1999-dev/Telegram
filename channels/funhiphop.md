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
<img src="https://cdn4.telesco.pe/file/fNSKPssqGp-J022MFKOn5rqRsVxQHl1yuOtd7MXhLLqKrMZSt1y1C5rHiigsUaoh7ju0inEvlGOTLPwvkWfKTJGMw7YaKuCzQcpiFRqNQKW_58wj3b2kZ0H5vC6JkkSCsL-wHa-tvJJqxUZXuKLRhN4JQKVcwM3Nwze4HWh1I7as4e4EZFZl_oTvdZQEsMyZFEcaURr77igvhKkOg393_1d6Gf7VCHzkQsxSGuviq3Ar19EdS95pFgcexWsjAPfLCuHE-_E4ng1yPFxL0uTfIrlCqYdZX0idBW2I7PdRar2MZD5SHT-dPU2IJ889UIwJZYJucetctHuUnskSu06AZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 222K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 18:55:34</div>
<hr>

<div class="tg-post" id="msg-81483">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFnS6qHNL7hZIq_yvH-5veGK9KCb145R8OaOa7NTB3h8akqFZPBxaG_pELVkoQicikjE-vEiB_EWjNtUbsA0Sm06lld8G1GiazpbSdO6Pj5GBQk1CJgIayufBgQDZGfM9PBBsR7_ETsouG0SUvjvTNJYxK8hnXnT_R-k5RFLjmDrItqcyljP_b2hvExQM2S3kjt6fcjY8rxp1AMjWBXI4Lz-NgZU6gDMvYRyXLPFWC-5iFgIzP0kJ6CJh74P3ci5K3vwVXJPnFfJmmvhmn2-Eht-Ufz-mHaHU8e4qdp4EekYcw33657jd_2CD-T0hZzAC6RHnZ2dXqHCRcSEmXkGjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس جدید صابر‌ ابر و دوست پسرش.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/funhiphop/81483" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81482">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5tFmQrabPwRcsxQ3oHcxLJOai7MjKMHGMZhJDTc6RQbHPEJsVkMyF6hkjVHD_Yjup71YgxBbGLkQhHFJCvC1eb2n87IP51-dOzX6TVcP_CiSdOw9GdTO6aw_aEUKNj2hwBgsjuEuK8Fj7LMP8sUR5AvcvozQBHWERFEMC_oW_UDGO4_7mlFNsyAMLHPeAiXYTZbEQVWxuyGlg9xCbPsgalXzri77M0C5--VQUIWDsUEfRoTegErgy75Q6kNMr45mQfXEWjIMLEA44DY-QyqIIyQW84wXdsydmrS0j7iw3YYEjRbSL-rLWMgE-AqILpOt18oKV423XxjEka_TeZW_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/funhiphop/81482" target="_blank">📅 18:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81481">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkO-gqEBmYBqPDWSnEq5WEkf6KD14Kie9ISkIhkYzly6gM8NxW1swhQqGqgHt5Vtxqqjc8oDm5z-cxH8uln3wKosPwrkNTOXveVWQl-OcxaJ4LF0uNEJPIjZW1N9Yap5_MiCrE0OJD8frJuC-wIA36A59e7pcveQNboy9hTHChmeK3UBnnOX4LDAigaRlpR_9gAVwapp_z3BYYQ0MxfH1qlI5WKzLiK3creQvXBFMMDqq7T5oJzRwUvyl1isS5vAUoeshG4GQfIx_2DpCYGjdSugfliwUg_hVJQAmNKnzaoQTmXetdXXLUX5EyggH1kZxWpz0UjSzE3zhNHRpXHhzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش دورف:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/funhiphop/81481" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81480">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/funhiphop/81480" target="_blank">📅 17:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81479">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAzgoY4YLB0TfGhDKYaaC3iMvmfzY7dNqxr9WRsXwPq6CDTlNnmQnZwdQMK5bxSJR1wd7z_a_ZiW4kphk1QIj7erPGjp8i-LJVzpegB3S5hveGytfJ-SB_gk91JtyNxl9aT7wyGTBCvX_gSfo3-_qGNIPA-dZ0DefRk8GNp7TCwrAORXY7USlUsxck-VJS_wCo9obKRAJeauI2bmSStYiiHofG3CO05Xz3vm7HhcCVn0O0neu23zm2btlB332lnuZlLDlKnxR-888_s19O-7fA1ETeIaGeMIRskix6lCT--qLN4UNHf1so5kQKtHMmDg3sgr4GhHyS1js8CvlMsm7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/funhiphop/81479" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81478">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZk1Hb0oj8sJO_Mx-VUKTX_sXnIIKjERU12iK9mpcRmMSrd-GlOPXep8rY5ExfrBYw06wqox1rbag9BEtQZ0jkYHaOT4IU8AOqDwDGV7G77UDoel24Up1_5RyYvAr8HddwTxkGz1CKDiriVFY1h-cPd5XQmDOlwxMCXqRRSFFXxhj-eJqaoqwogGhKeUMtTLty86gJNGGiTr_bKQo4z9i2OG1mYqxfVpwnktANUe6KrrvYImGCJ_a6jFgkkZpNKAWME4l8214AP1X4z0fmCZFv8O73DTh49mUcgRHyADxWlLY87GOegWVItSXUNmNaeq1L8hyfe32ppzedR4cI4_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/funhiphop/81478" target="_blank">📅 16:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81477">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ: ضربه سختی به ایران خواهیم زد‌‌.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/funhiphop/81477" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81476">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">منابع نزدیک به سپاه میگن در نتیجه حملات دیشب عربستان و آمریکا در عراق، تا این لحظه دست کم ۵نیروی ارشد حفاظت اطلاعات سپاه کشته شدند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/81476" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81475">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/81475" target="_blank">📅 15:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81474">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/81474" target="_blank">📅 15:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81472">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDl-nxz31RY4sekxZvBCxbWLzrbPApDauf5_-2kHU-5Y0ryALsC6H8SuZbBEjqjz9tAy2cmxH0PiSb3IBobqYm4uhFFUs_Fo1D_oJhSZu4Rd0jcluHUYQLVUiUXKves3e2LwKedE8lhz6TVhMUEpXRvAV7NuL6hOozyuVEPJefXVI8fcQDVMKyvGcokkPBWRfY1DFUgTyY1pDgg-pYeICIy9tIClKdL0hBGJX6O3cdcNYTq6cdKHgbzUcUnOjMEu6OQ-ODm7p2VXJ22Sn-BlOGAT8tNJ3371MBfRY4L7Hbojwcw3mm8EvIJLEKvz8mEP3sapN0jpAWFKRa438Zoo5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/81472" target="_blank">📅 14:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81470">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kum7VWVCAZiZyyD59WjVptejfvxTt1eUqFsxcgI32qCpg9jO5FwGSCiUOCVbV_-PRe91MWX7SLaD6eY8bPdv-bjfZDG2Yho18fscw1L0ZDbdgVUoljQoU2z2JoiRllI5qh-ZT1tGkMPbdnteA3bua7-agvRqNFW_vChY6izX0yEOPhBSnV3DznblkwZkqZR-OCgWyJMoulKLIi_L8IwRr7CshrdB0i2eWImLjQT7pURApF63HxSkNNX7wdDUL-dkSGBGj6y4QGIERl8r2Qo5llggHezTfrdgu658I_WriYNOXgiv69qtnGV5h6xEH4lx65pT3FU3wQ3vQlHznuUq-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4z7cFiTeUMXLabEMA5SXt_cQotARivdn3cpeEJMOeg3S_iBmZcTwnWLTVuiwHSepa88F7yRFwc6Yel1i3cQJgrfd3LPHpBcna4gk4XaQlWpLkLUmMlA_BeNat_rf6V3lXdG2JqZuuWKdGAjladFADk4PCTxeP8j0aOmT7ZQpMwnRmsfKyRIGvSwKuLKslq0RrDNPy-SK4RNYxR-2SrOmj1wwhh__Q_CTKtRoKHzhlcl5QZwYJ0BES5hqntysehIECxbAEBH0p360XtYu8oi8ZNuY4UlMosgfQCJUMiICXNgYSREdEvl61Jpiayqz0Ck_tOANV0yJ0WiWZbK1MPE9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پینترست چرا تبدیل به کرج شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81470" target="_blank">📅 14:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81465">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اگه این با سپاه همکاری میکرد که الان همه تو صف اعدام بودیم</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81465" target="_blank">📅 13:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81464">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81464" target="_blank">📅 13:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81463">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دلار 193
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81463" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81462">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG4Pl1c0zP6QUl9OhppNoEnf6F6fdaXWgM4fW4K5dqyMw6fcpw518-vksHU9bOOEzlxeT9BshU2f5hEEUgfTOFBCV0zyD6pHWt84ux-pB4R6JCxnac2_8utIuz9SRQaaRakH4scHFWmwzgUlsVQkgy7n-zFd4loOCKICPefbymVuQugd-zisiGypf9Lstz2ateZca4R8XCDvWWik7zAZ7McX4ZBp_0u62J7icCcCffcmtc83kEoBsbDdn12bMxRx8uKS4CJK8BUjfzL9oMv_TqvPm0cHnvmRsG-glMsvTFTsOCdP-nBI9Eh8c64r5Mo3y2aN8Z2Q0eS9SNth-7fpdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پیشرو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81462" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81461">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBFaiatpi7OFEpgd7rWtvZ22aJrmCe6wbvsQjj3ctbr9U4P5Ns4vz0HpM8nQtYfHzyGAdnhCQJGvXnlBVTIf_6KnOun3r7s6Vvmkw-b5kaRPQFDQGnyR9EGbpll5FJYaZS2Q0DfEgvY0MLobCiieP_O1Yj2YwjugGGCJar5subyV5DtUu_Oo7SERHBGQqtlMa7iVK8tw7Len2k5tHd5EoNHD7XzhNxTcKuHLsmfNlCPvBlSBEvDxXnyhLsyruf8dqC-z_ui7urM6ddyTLWdtc4NiVnj2p9zZG9FW1JYddVEccNiyHTiTmzt8_5Sugw4djlZBw-XlldJIWtvAyWzqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید
🇪🇸
-
🇪🇸
ختافه
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
چهارشنبه ساعت ۱۹:۰۰
🏟
ورزشگاه سرو دل اسپینو
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اتلتیکو مادرید در ۶ بازی اخیر خود مساوی نکرده است.
✅
ختافه در ۴ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳ گل در هر بازی بوده است.
🧠
تحلیل خوب، آغاز خوش‌شانسی است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r7
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81461" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81460">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">از الان تا ۶ سال آینده هر اتفاقی بیوفته ربطش میدیم به جلد مجله اکونومیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81460" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81458">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هدف یدونه پایگاه آمریکا تو اردن بود فقط
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81458" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81457">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تروخدا اسرائیل باشه تروخدا این یهودا خیلی راحت نابود می‌‌شن بوم بوم تلاویو اسرائیلی‌ها مجبور می‌شن از دریا فرار کنن تروخدا پدافنداشون ته کشیده ۸۵۸۷۴۳۹۹۴۴ نفر ازشون مفقود می‌شه کلا اندازه یه استان ایرانن ۹ میلیون جمعیت دارن کلا تروخدا تروخدا اسرائیلو بزن سردار
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/81457" target="_blank">📅 01:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81456">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ببینیم از لپ لپ اسم کدوم کشور درمیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/81456" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81454">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1P-jHLxqAqESux3Mlgz_UUo1cRr4nJFP4JuJd6i6WQrWLYj7LktWhXub0NAbzovyePXlh9ENamE6aLR-zyR_lm1_nflHtJXVwsfuXQGbs9GMWZaxf5tq-d0eeqDoqgJkshP-9ChBNAhwV0O1VSNb6XWLUMfQn5z98kZA6yUHEpEo_w-YDUmcOmvm1FxFYcmyWzGU6OYBimaIovG-2uVP8janqurh_UxguWfZVNECWWYpZJ3TepXs4f7mUXwSgX0FeGfx6JExpbjWz6_RArRt1yZseFLlrZuztpF0cvmWCeaoxpSiTp-SbezS363meG9ujZ-A1x3YlP4is-O6ANqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/funhiphop/81454" target="_blank">📅 00:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81453">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xr9HdiBBiQ3QyktDGxVv6cpaLT4TtvT2gw_zBbStQOlcLVYc0FJSME_oMxVordOYPRJwSmju5SkUETEUh7DZMq0av0YagTzM-Y5_bHA1-yiQGbDWxZh_FRCi2vezaIQLcfRWCWfL8kni0BCbTK4K2-y6jBmyF-M64wHqep3_E7h3C9Fs2mDOwXPncpttubtVEvw9icTI1LlLnL4LIyWEGa2rjKmBlblqucNZRHfdC4WW91wiJzdYHT9Kxu9zWFjch6gwC0W6RW04z2xn3vZLP9bR5y4SWzbIttu87lIeMIt9slpPSY8xOtmiSihU5AzYyTyV0mQofn0-nvrT84aC5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم" تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81453" target="_blank">📅 00:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81452">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTriMO5_2CqCRVu1fH6Fz1bJG_FPazOmAfOGjLHVV8TjKzzelSkt42crmLCCZvsWKtYC1qB6y2nbHb6aDzKrntwhub9bTEa3ZndgHq6p9kMbE9z7f0sj5jprvlIW6BREaUIutTgpA2IOwhBpUxmdQpbJIxT_H-hFbwat_mlXtBJb7RYF3yh1pt3yXXPD_auIfDFkd-UpjsUzxPmqrt9qAvY0N0bvF-EqDRGH_xVWQ4EKus3dBTTgm13kA44rcsD2Df98LkukysTYHFVxWyg26jKyzdhb2IyyJR1FH8y3DEmL0oQjFbrbHfUhvp7HChflLqZ5060HgKdNBSW7taTNNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم"
تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/funhiphop/81452" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81451">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">#رسمی
داریوش ترک کردهههه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81451" target="_blank">📅 00:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81450">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNovlgkFqabra4MEAMsIk9-xiSWTrhDnCq6Yxh517KaweAsaxIhUjzcClzrEnK09R2ExzwumQdDaf2AqTX_maHezcE3dDL1O99xRO6BAlkbtRMJerwcw1B7h4GXztEiyfhnEUv-ZXsJE-JGp8mx_nrGOXRD4rylLt2D3k_PoOaSiMFaPOhzqNseciiV3EkGdyGBlTfEO2v_vSE4-JEqUcOUkKKwPwVQ_rICfsEzceJluREwRVrBBYCyCfb2ZswdK6Q07ijX5bbhnfcDYQ5fX8tHlCcWuv1Iqf-3_ZIdMLudZZ_UPf04YhKK1ek7J_h3o59DYyapvVV_ifIqBflaLAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم یادبود لیندزی گراهام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81450" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81449">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یعنی جدی عملکرد ترامپ رو تو اوردن نفت از ۱۲۰ دلار به ۷۵ دلار تو دوماه ببینی و باز از گرونی نفت بعنوان یه موفقیت حرف بزنی نیازمند خیلی کصخل بودنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81449" target="_blank">📅 23:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81448">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkxQtTeNRd30xKH65Ev-EU_rmbRK6kSedrFyLDYniMrY_u0WU4LgIQ_7_ve27-_eNKMi9hdkIBKMquSUoQ9EIR1v-gNeThWIXVHGtss-0mCNhyGZeAJCA4jTuNIM3mlzm1fz3KKbRjrE1AAXlwnpZ-trhmdS1Gy8IwUJwiVP_gQM0Uu_FOkzHnOFRzdwGdwPmSzN8ge4lo9kOCEZMbO31fu07ZeB22I_O5x6yYdadFR3LU4lHqaqO7w8a2kfd6xRxqTEva-MwJxIWOhhj2OdUYe7k39Lc3BPaWaEm73rbxi7Gg195nxGgV7g5t1wajZqHG_DX6kk7BE9pnEE662t5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا سکته کرده، اما اعلام کرده که حالش خوبه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81448" target="_blank">📅 23:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81447">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">قالیباف: دنبال بهتر کردن
زندگی
مردم هستیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81447" target="_blank">📅 22:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81446">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfC2stlA2MA_GYfK9mpU4es593oQqRyfowqA49EVIbXW1Y3uFeU0q1BtzWNDCEivOe6kwUa-hnJxPbiB5llwP2X5EuEXXNzJc7e9o2p2Rin-JgQwbBhO4DNzV7mvAjJUaVtQlzCMKG2RySB9OjHqI0WDPJQSJouJQB8CbUphxohUvuFBTeiwVOBjdCDuqkDco8mKF9eQQ8vKMRUq43S44BvL3ZVMuiBekQXr5SrZgJMRcqqh3JI5jq5kwp3JqxfAGCJZ1jTPcxrexvjwG4aXFpJ7VEXL1YsNuJFq0Cyfi_rZyGKorIc-AUHbeEXnuDhUMmQ_OcbAW5VaBMqWQCqpVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعفری دوباره منیجر حصین شده، هم پرایم حصین هم شایع با جعفری بود، با هر کدوم قطع همکاری کرد بگا رفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81446" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81445">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromApexNet Shop | اپکس نت شاپ</strong></div>
<div class="tg-text">🏳
سرور مولتی لوکیشن ویتوری موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر نامحدود 90 روزه - 45000 تومان
🟡
سرور 20g - کاربر نامحدود 90 روزه - 95000 تومان
🟡
سرور 30g - کاربر نامحدود 90 روزه - 135000 تومان
🟡
سرور 50g - کاربر نامحدود 90 روزه - 225000 تومان
🟡
سرور 80g - کاربر نامحدود 90 روزه - 360000 تومان
🟡
سرور 100g - کاربر نامحدود 90 روزه - 430000 تومان
🟣
همچنین سرور تست موجوده حتما قبل خرید از ربات سرور تست دریافت‌ کنید و بعد اگر راضی بودید خرید کنید
✅
🟣
برای خرید از ربات زیر استفاده کنید
⬇️
🤖
@ApexNetShop_bot
🟣
برای ارتباط با پشتیبانی و مشاوره با آیدی زیر در ارتباط باشید
✅
👨‍💻
@mehdi_splus</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81445" target="_blank">📅 22:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81443">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbSo_IuAdchC5yxQDPdkzzsWNo_bDuY3yUHJ45-orglBnWMYOSJdCsCN2tcMAl9IbI-IzAiFez3ArJd_O4k3DbogsuSg5Ncs-CInsCMZHhGAh3ikRfrv51gkoX-pAb16MiLJ7a3uv1Mv5DjTN2iAlnE9JPF4pPl2JVnLjhXT0t1o6DHnCfEGfXVo_5C544xJq07ZeXzO3ofRc88TrlMJ8k5K2b1bt0RKs0g0TbAzD4w4BIedQ66kJHvJN0wjD5EuMXkud2nSgB9VwWnxH1V3CtV3vGhBuallrtJUci8oDosf7OUDILV71uccxeNs7phceftHGnrMwhC9FLbDHKL12w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShjRTvR0SLcaZBWeNZlUguLGFDkGy5b857eSqpaXzQyewSgfbdyFeyqLW4pjksFgQmgJGLQstkASNwTsIHs9AZnSlM9smwriCjBuYE7TBu2PYztrxtApJKMa409qW3quObZ804adNHj8RDEeDEuYqwjLt1O-Iruhy8irN6Wpc_fXKAArWm8Ha_-m7YvruUT6BUA_ykuTA0RzQhumNODry2g2vQ-RpOaf6rwmD46yqDgmVWY3JenS21KZ3U3cISvd6AC64d3BHltU5u3CcSINQ_G567EUAagAkBTc4E6ZkJrU84hJ_sS8WKEsbWxcAGhDAr8ucUfdPcvXO16O1V3p2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری های نوید و بامداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81443" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81442">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=bZRlVLS6GD-StKyDaU8py0NCc7z8ctnYb3s72YYwMgxN2ZYL10w15jvpbqAo69AdwzVoPNfHjLj0u5iwC7d_4UkLL_waOn3lao1cTDLowaxy1o0keDLfBCxH5jGFNr8S5esQJbouGqkHsWPAp7P9h-zuFUuZaIZ-_-3RkjCVIn6d9h0YUJQJ_z-gUdUthsL634ETwz1WxxRh_-u_6vcKQYnd1yjLnwUYQJ0mFGr2QqHZxPg5VAM6bYMUn3cCnIX21kairTLxDw3dLzhSTAGHXEfKECQeHZAUH-_dgGHNlATFDtDboKz2NXpQVQabMWmg7LQqcuacgID7g6FOG5QGog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=bZRlVLS6GD-StKyDaU8py0NCc7z8ctnYb3s72YYwMgxN2ZYL10w15jvpbqAo69AdwzVoPNfHjLj0u5iwC7d_4UkLL_waOn3lao1cTDLowaxy1o0keDLfBCxH5jGFNr8S5esQJbouGqkHsWPAp7P9h-zuFUuZaIZ-_-3RkjCVIn6d9h0YUJQJ_z-gUdUthsL634ETwz1WxxRh_-u_6vcKQYnd1yjLnwUYQJ0mFGr2QqHZxPg5VAM6bYMUn3cCnIX21kairTLxDw3dLzhSTAGHXEfKECQeHZAUH-_dgGHNlATFDtDboKz2NXpQVQabMWmg7LQqcuacgID7g6FOG5QGog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار کودک‌کش تروریست صهیون:
آقا جلسه‌ی خیلی خفنی با ترامپ داشتیم، وقتی می‌گم خیلی خفن یعنی خیلی خفن دیگه، ما تقریبا سر همه برنامه‌ها و اهدافمون به اشتراک رسیدیم، از جمله همینکه ترامپ مارو پاره کرده که ایران سلاح هسته‌ای نخواهد داشت و یه سری چیزای دیگه که من گفتم و جاش نیست اینجا بگم زشته جلو جمع.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81442" target="_blank">📅 21:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81440">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bR7appS6KeVp20zEHy5VxcEiegY-jgvQb79G1wJVZCXy2rNDO6VFTlFtZam6eGYFPbbP7CUfGMlQLOjrqz3TvI36cDHqGnFinxKdUeNI2__nlHN9R2nEKJzV35s9p60R4d723RYFLzt686TNMDkQsSsXldJEZlnCL1udu6JX9zZ68bUvRGC7ncQtaA-a8m7DoU7v8w-qdxPiI5pz6dl9K1RZhBbvT0qFvXaasezFKBFduc1riDkFM-2VsNDBgbzFbrxshilCBt2bRM7w_zG2RQhwYYNJCQhEE2NFutcFwlYuBSl2EpQnH7QL20TNKtpNXacSnz43P2cK08FShQIBpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjxY_FOwZWGloVg8FSe0A8e4gCxuF9Tkk7dSdVeHxR36F4CC5Bdc-Dr88U0pXgPta21Hnrv5z0vUMCMx3fMCqRIfX6fXOfJPlex_GsOb2nX4nOGIVSLQh6tkN1loUIQtfq7S-AumAWnBb2tFcpGqk7oF0tcAMtN_jDli8lrghXn8lHNyXC173RbPv1rfcrYuuQxziAFLYYx9qm3ng14ZwTVPv1J5IQD4xIOXOeg1GN98Um682YXbHwNF5AhAhAtee_0u9fjuDRELJ4kM5n_FXASNmm59U8E2it0ou3Z82HN5U_0vhL3RSSHLg7k6JRVOt6w4kfIrsDSzt0nns1tTEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوکوریا قیافه دلافوئنته رو تتو کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81440" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81439">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7eOG_RqPxJw1N3g2WfTuGtLMCzKGtOhO9SlCO0T12Q_8zn28s2Aj0KsrAxPPD2sL_apqELqxNSAgubGJTSugK0Gnd8K_lbpk9XTz9QqRucdLlNdqb1blKCjs9mbw1kX8LLS_8phhG2SK5eAKs-7PQTNYgWWF-_9AzPGbzLKjl3UK0YqB-U1SchxYurDD5lGtUYlwzb_QJSWQkQw2ZQCPnl9TCJfi-aooz65PrrnBEA_H5SEviT4TU8byeDGb1nftUYYRo0dJcZLlBtiBcmhpmQD603wDW2Hp6nSG2Dn8vfgRqvwQYhk2qqauqZbOsJZOyTjv-Ks4sImdA9k0pf-tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماممممممممم
😂
🤣
🤣
با هوش مصنوعی فیلم سوپر زن رونالدو رو  درست  کردن  اصلا ببینید پشماتون‌میریزه
🔞
یجوری داره میده انگار  ۲۰ ساله توی پورن هاب داره کار میکنه دهن سرویس
😂
😂
ویدئوش رو اپلود کردیم بات برید ببینید بدردتون میخوره اخر شبی
تماشای  ویدئو کامل
https://t.me/CONFINGMeliShkn_bot?start=3126b54d70f9</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81439" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81438">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بعد از اتفاقات دیشب شماره مادر سام صابری رو گیر اوردن براش فیلم سر بریدن فرستادن گفتن سر سام رو داریم میبریم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81438" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81437">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شاهزاده قراره با بی‌بی نتانیاهو در مراسم ختم سناتور لیندسی گراهام دیدار داشته باشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81437" target="_blank">📅 20:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81436">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtDJhR85I0zteo30RepCapqyAHnATS687XOzPVOkjvced-kdnK11aszyCezPnTLeR-hLB_eIvm5YbHOVHSEApv7L2N8XayB8_xt6gUcu_MRLRmpx_BF5T9qLrHyUSH_id9QvfTxGv0uGLcr5NhjRUv-rqTTKUvYtpdBGoQOf9-YInOXNFJ13xRevzv5P-eL974_wrYGbdDOaf4E9ha1PpLC4oMJiWATun32qch5lXr8lsGhBz6lOODg1PX-X0sxcBCzul-7QO-Y2sAf9EH66R3fV1CNuvvg7GTcFZ913kIH-gtlXotJPOQOr0ZSjHbwViZGy_-7_ZdXMjhvjyNv_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه گذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81436" target="_blank">📅 20:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81435">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Numb 1 - Madoro</div>
  <div class="tg-doc-extra">numb</div>
</div>
<a href="https://t.me/funhiphop/81435" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81435" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81434">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OegALngZ8X0WWgLcMYgK9-FGTKso7WJO2YpbGghqJXjqKKRvo3rVV05-_ergJ6YtmKRrlVlDvy0oA0VwrNOJSI3uiVXSw8XwGibgoCw23zJVhMo4HGr4m66STkgxmTeA8kAQmDJYoPeYOmsvJ7aW9gFDAMQubd1DlhVTdte70_LqXgZypjiiunptamAVZr6xOuchZL8CDH-vh-cGcI_FLLvCAUv2tCPkQThbS2Oh1Xb372Y_cBsoVlZoXJGfIzNfUQDscN3venb5XRvHpsLuXpfgl_Lc5PzFvYe_kvX_DQHv2ZyMCmIXniAvDb6YqAty0vXGiY1SBWa8-qsRVVBXpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ جدید numb به نام مادورو منتشر شد
📺
Telegram</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81434" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81433">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">این که ترامپ دوساعت قبل جلسه با نتانیاهو میاد میرینه به نتانیاهو یعنی یه کاسه ای زیر نیم کاسس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81433" target="_blank">📅 20:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81432">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4f-eOlHqVs7IQUIHeoTgBCbfXxqBMYPatW4d2ASWarJUvpe3bPLgoXD9jxp1hoQ3UVlZNYq4Rrmqeo2D1n6-mSljIKclYZ2kr7fNLwMlkZmbuUzncIS7tMF0VLuZCalSm4bKjl8o8c6KbM4CUBBCgI6Rgkj4CxkYONTwXMMG6s9CTZ4ML6w9hZL3Eulw26PR3gIcnd1-eTX7MFrN6ZVANNqZn6xfFNmZ_MMRCa3nhQmwFrV-3s7CT68No8-_Ug9qn7ZGUXOufAw2BU93t39yy7f2GT7rsJXZ5DW1iKDAqBOMVX3_35Vy_9CqWvh8pvUS_QqKTLI9ocZA6ujUP4M6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو تو فصل یک عشق ابدی رفته صداسیما
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81432" target="_blank">📅 20:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81431">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEsJXdm-pFbzO317nXkiFlPauHcR8yw0feuVSTfJ7EG7c-K_whVB6kNrz7cZPHCpcpQEgUXIhHCR12Xs-ysbhiMMQ74ymsoYQfZ-zpNgemIiona4eufbJ0OaDJDhhEXEXkIrW790E_HMwZs9hZwUqQvkR4g46JezOIRw0sC-CCbIuB3ao6OejUrMnXIeC6QchZmMzggOv7znEKfaHrEM7XYqIRODanVB9gQTb5Z5bxGkjnpYCxUIdvhEkkPwtwwWID5rGqFDSIWD6bLyvyhd5JU-5JFByKbAVHxm2hAeWQcb8CtLNxSUElEZrBI0340cKq_P9lk2H2avEtmOQuJ3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو و دو تا از طرفداراش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81431" target="_blank">📅 19:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81430">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfEyjkPm1urDZKgY1_Jln6lP__iBBl6XT0mwuuD7aTcQCoYRHIoMKjWnpIGDSGJYp8L53rlW-Jcqng03pcNNkJc2c-o9rsi5Ix4aKJVCDqXKju_6xJejTzsXkf0PS-eHK5kEYhQbz32faYf-5ltcVL6S33ms9vRIpGbgK10ZbJStJk5tOuRKjZPf_UTwexxuS0QucdXuI6PkwvdWv22QFGtgNJW4pWOKDKjtabj1-VyMnD2421hr3lKZSFgiPJ1LbWt9e7yYB07X9qUchxX8UvdoDyyL1kz_Y5fkgISwXLz0_yEdqm0fETO-OFj_mI0PZwzKhASrvdJ5Fa3pxA9beQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل جدید لیگ جزیره
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81430" target="_blank">📅 19:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81429">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6Gu9xKR9loqJiEj6OClP7L198Ii-DkCvq5Sg2EbRGm70Cy8kr_MsuSirGIGbpc2p6zdcqwgGBmx8xXjAkHNP1J-aVndyJEdU_ADZalF4xRifMZhKQNt-MYRVFXl4cLMbd-FIvGPjDBx0Lzpxpj8-wYvUSjkYmFkW2zqntcVzCz3lPvxqmnHlsWIsQDlZHpewATEaLa9BbXChFc8c-XxqE7C9G9vzuy9sEkOdDHfLNWZ67mRY1FvKwTQ-j-wiMs8lsBfBGnT-e0lGEn1cVIvfL-ms5_xFGtr7JaBP5fijLwfgCSRztfsOJSB2CftoPMa5FVNcxr3SdQ1mbIYUBIPTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی بگم از طنز ماجرا کم میشه
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81429" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81428">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDTNkwhoNjSwQdOXjJlP3eC27qnx9c-xQSNF4knzz_GVNRWYuHTqWxvjY3sr6WQdGW5agl5DS3_VprzdTB4T1hQQOkk_rUASsPeYEEIMXLr0fzuHkATNgc9Mg5age09ZbEG3iBbuXSjPYKq_F-rQVxfrjpSHrtCwnZaXcJ1qQcqA99zRkV5Z98hfkeoVzL8QORPjXFXf19YBa0T3bZb7Sc9Qq1rfycZgbITrwL7rk0D3kUaGTvo07q_uxHY7U_eZqv87WU9g3u2dAaZkMrDImxKBciKtkvt84VGad6fKC4rD20PipDabNjICpfjmo6kzvZvJnMhnEGIBceJ05eQe2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید
🇪🇸
-
🇪🇸
لگانس
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
سه‌شنبه ساعت ۱۹:۳۰
🏟
کمپ تمرینی رئال مادرید
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال مادرید ۳ بازی اخیر خود را برده است.
✅
لگانس در ۳ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر رئال مادرید ۳ گل در هر بازی بوده است.
🧠
برد، همیشه عدد نیست، گاهی آرامش است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r6
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81428" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81427">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81427" target="_blank">📅 17:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81426">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">به گفته ایران اینترنشنال,
قائم حسینی ، امیرحسین ملکی
و
علی دشتی
از معترضان پرونده‌ی میدان علیخانی اصفهان، به زودی قراره اعدام بشند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81426" target="_blank">📅 17:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81425">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81425" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81424">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jo52f42UbqCVV5kMv3p-vel4xW3f7EfpeMs_maXCtF5qmb8imrs_pDCstLPc2rMitc1rerz2N5Im_PunEZHQQCCFaQEg1fxhSLYc-S2dVSW9UpTdSSSw-ObJAHclYYmUeJT4cU0b86CkiVE4au9IVu_MQsu0vrdL1j5EEWO3GppEDvw4FQnQqbbCh8Dm-gQVjaPcaIeWfvV7tH21jBJod0VPdbBzFWDFK7hDqGS_JceKBtLiPGe9po6OLjCBAjdg23OVLMZqxx3mFOlhFLbw3Ezx5kSE9GNCCH6wNOs3IMV9oKYUUmsb-85ePMV7-i8YfFbn__LAP_goGvNFWc_iZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو خود سایت کارزار، کارزار را انداختن برا بسته شدن کارزار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81424" target="_blank">📅 15:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81423">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اینطوری که روز به روز اطلاعات جدید تری نسبت به زیرساختایی که از ایران زدن و زیرساختایی که از عربا خورده میاد، فکر کنم آمریکا رو فقط در جبهه کری خونی با AI شکست دادیم که اونم ترامپ اشتراک طلایی گرفته داره همونم ازمون میگیره</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81423" target="_blank">📅 14:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81422">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سخنگوی دولت: در طول جنگ ۴۰ روزه ۲۳۰ میلیون متر مکعب از ظرفیت تولید گاز خود را از دست دادیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81422" target="_blank">📅 13:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81421">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">از سر شب تا صبح ۱۰ ها موشک میخوره تو خاک کشور
اما به اندازه ۵ دقیقه اذان صبح کشته نمیده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81421" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81419">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/itetgVlE3lVGLTlO6oUCGmjP8z0QOKIwExTOkh5kRSobTUK1KQKy506Saf9Mm5ujLHMOp4reIC5PAP5TAUKgzIWbCF-Qm76a3bQ53JSzQ_lc1CFKpQgLEvth6MXtlX899kXftL7T-Ap-IGKbZ5-R0L-VMqLY21Mx04eJ_af8MCUeXJ4ZbMsD6bapUUWzoip_hSZ1CPxVIcX-4akEHBOrTdYrAwbqstqzPiZuCGdidYCOxYY77ULHavXNcPTg0VfKbXiuDIhpa2anlx1QoHT_fOrczsHV4zJiBDpyW6FY0ebw6YYF-5v-LbjifreCSY1p6BsUwVwLfMnB_eBGwHEewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFNWCnNFR0jJXVH2sTC0MLHUIaxqSLLog049YKL8_a3S9LA3vRqOhE2dnD7LD1zYiCnQU45jmM-CZW0zyoqsuyh4vGUNFATC_ffgK4xBACsZ_Mxpdy6pNdCZTR47DPPtHwy_2KLidIZOghuAyhIHEWoeDmp1AspW6U9ehbByhMym6zF5HO5YmF6xNTNYIYInh_leTjcIOwssr0NDWYXHrMnaZDymBmsE1ZjL400MWEAwaJJ8ElJu9DfQbBsGL8hmYaqG710Wb559QNbWycJIOy9py0BhHbvxyg7tYIxTam3MbKdA9r4S1hirU22K6K1dwnQCJcIBwdeMCl6GbURURw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی دیگه از پیش بینی های اکونومیست درست از اب دراومد.
زلنسکی با دوربین کنار یک کشتی ایرانی که داره کالا حمل میکنه، و یک پهپاد هم بالاسرشه
چند روز قبل اوکراین با پهپاد یک کشتی ایرانی حمله کرد.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81419" target="_blank">📅 13:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81417">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqxW_xtaC10TrficAVDbUwlD-0e1m5RSCn24zsgqkDqagEzm6o_bW3MUOfPktwPq0qQxI9So3CzEhvpdCdtiwe6pzNRZskTeoOk-Ob-mcL_AEz3qW2V7eYcNcB-ISqC4rlvz6RItax4ygtpCulOAj8nrJYqdqtxDvBrFqxSArKcwCSkwad26tCs9x5H9S8zbRZpJ53CXPFp5DsAfKaFC_yqJESUlaAHhDnbi0znXNKHpcmft62-PZpbG0a3XRExdUjofxXkyG2HMtXy0YF0R9ls3L6MwsGbJnA5XlWbmOh8YOnnoDzbso-9K9CI_MVDuU4vodOVBB8x6QvR8S0Z8Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f171036de.mp4?token=nROc0NscewinIhTHurUgJ8Jp2NQkmkDG0GSWd97feiqjQzutfkXiiZGz5prhyuxxQihUuNRu1qCx3B261dS8pbo_uFmt7dD89bde9agBVmAzzBxqgv6Ymxbo4e7N2Nw_1PcFvayZblo86_fddi0vaGhRsltcjOTXzlCYZ2sF37DzOT4rtH_oh7SuaMv1Y2FsfiIEoE77q_xSoTuAz0J_HD5AAgngKJL5z9xfwqLn7Fbyihj3P42zS9ldl3voLsOSaWvxUYpV-HOZsPfBYpcwGTBG-spvXwNOTB5VNXX4M5SM0dPS4sSXM0sFFiw58khptytT7fAMZRsPFqDCWSAViw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f171036de.mp4?token=nROc0NscewinIhTHurUgJ8Jp2NQkmkDG0GSWd97feiqjQzutfkXiiZGz5prhyuxxQihUuNRu1qCx3B261dS8pbo_uFmt7dD89bde9agBVmAzzBxqgv6Ymxbo4e7N2Nw_1PcFvayZblo86_fddi0vaGhRsltcjOTXzlCYZ2sF37DzOT4rtH_oh7SuaMv1Y2FsfiIEoE77q_xSoTuAz0J_HD5AAgngKJL5z9xfwqLn7Fbyihj3P42zS9ldl3voLsOSaWvxUYpV-HOZsPfBYpcwGTBG-spvXwNOTB5VNXX4M5SM0dPS4sSXM0sFFiw58khptytT7fAMZRsPFqDCWSAViw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طقه پوبون رو زدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81417" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81416">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JB2Ycn7NiJQ9Y9y6VVt1yIjYz09876bZ8eF6mt4sYy-EBcU1uXxyeABoryjkQ97h0FIuQajP1t-1JE-2jjG9VIZ5SlK6mcjuPXLnk0evUE1G2nc0UG2I5Y0WoH-3IDP66r0jGmLzpyCyh6C-lxTQ5tNnd2iRDKdTZSqmnWOpGC3ZOsgG9CZlykpOrHUri2x3ebVl9xEu2QBC94_xuNQlmqanKWxdfKzqRSqJiramRZT9eEmyJcVs9lKW6KVsaElIS1c1pYB3_A9mMtU-FssWHML15GJ2RcNoF3qcZLjbt-U2sRD4KcampXoEBBcn8zQ8af1HPWa_0nOy7vwUg5OdoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید
🇪🇸
-
🇪🇸
لگانس
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
سه‌شنبه ساعت ۱۹:۳۰
🏟
کمپ تمرینی رئال مادرید
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال مادرید ۳ بازی اخیر خود را برده است.
✅
لگانس در ۳ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر رئال مادرید ۳ گل در هر بازی بوده است.
🧠
برد، همیشه عدد نیست، گاهی آرامش است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r6
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81416" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81414">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=KViZTLIZTGgfFCZsM2kZVKrIQRYjP1wFlphMBxKF5NDoSzePklTaPOFaWoYvFJv5NedLW5SL5saHP25egV0ulHFIGgthmAj3OeLJXzAxqXH2VVFEuY6tXH7ZnNLy8n4rnuoADgBoee4-kV39ZfNMr4MkeZ8EmkI8Md6Qw2eNJfYiMemHn8oIifFTwTWCFwOwIqXF8DhI6J8gL2MsMnfd2plX7puHxvF6VIt2AagrWMY8xRfXjvwDmvEwNCcLph21gyqZw7ocihT_QXGdsaQ4IZFS2OTFdHwus33DNqm8zQzE8jCzplBAl3ZdUerPwnFvezURgiSByMn9svQ8XW0jeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=KViZTLIZTGgfFCZsM2kZVKrIQRYjP1wFlphMBxKF5NDoSzePklTaPOFaWoYvFJv5NedLW5SL5saHP25egV0ulHFIGgthmAj3OeLJXzAxqXH2VVFEuY6tXH7ZnNLy8n4rnuoADgBoee4-kV39ZfNMr4MkeZ8EmkI8Md6Qw2eNJfYiMemHn8oIifFTwTWCFwOwIqXF8DhI6J8gL2MsMnfd2plX7puHxvF6VIt2AagrWMY8xRfXjvwDmvEwNCcLph21gyqZw7ocihT_QXGdsaQ4IZFS2OTFdHwus33DNqm8zQzE8jCzplBAl3ZdUerPwnFvezURgiSByMn9svQ8XW0jeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی گرامی کار قبلیت چی بوده؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81414" target="_blank">📅 11:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81413">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مگه نمیگفتن هر زمستونی یه بهاری داره هر شبی یه روزی، خارتو گاییدم چرا تموم نمیشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81413" target="_blank">📅 10:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81412">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4Emzc5hobcsPy6YuGEixBm-D04HAlPiBrqU0S_7ORAIftwVJfSLv4wrKuPjq_Etrpom0MdI3bRt-42r554s3v7C5tD3Or5Uop8wnM3MU8bBU708ftpVjPBVlFBTbAVzbqjd6IcOZBKgfU3gYJM_OcupfnywP000k0h9pYWYFcaybVN0M-lz8IINrWUkLS6mvzapGk9-vw451gGMMbWiHsePzQYKJCXB33JkV9sGGxqLoo74ELegQmmXz__qZ2M8L_wBRdNx99AqbSXFTBuACxQSQJb_bMX-UXiWF7j22yZMvq__3RV8BSBMxhPVyi883X4HFA4BrCCFRFHe2jsA8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81412" target="_blank">📅 10:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81411">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تروخدا فرزاد قدیمی رو قاطی زیرزمینیا نکنید، فرزاد اونقدرا هم کیری نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81411" target="_blank">📅 08:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81410">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خبرگزاری فارس:  هر سه نفر اعدام شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/funhiphop/81410" target="_blank">📅 05:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81409">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خبرگزاری فارس:
هر سه نفر اعدام شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/funhiphop/81409" target="_blank">📅 05:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81407">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">از میدون صدای الله اکبر میاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/funhiphop/81407" target="_blank">📅 05:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81401">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">درگیری گسترش پیدا کرده میگن با ساچمه چن نفرو زخمی کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/funhiphop/81401" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81400">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اقا یسری گزارشایی رسیده که مثکه مردم و نیروها درگیر شدن و فعلا بچه ها اعدام نشدن
تایید و تکذیب نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/funhiphop/81400" target="_blank">📅 04:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81399">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مخم کار نمیکنه نمیدونم چی بنویسم
فقط میتونم بگم تسلیت به خونواده داغدار و ایران عزیز
شبتون خوش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/81399" target="_blank">📅 03:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81398">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCT0f95aH_uofzRvyRnJ7eqlZzLcOKe21ZeagPCu-4Fbd1h40aga8hijfvJo6myRXHIXuJzcHF3vLo3Rj7bLTCPj_9ijS0uvyYplr51_jMfp9XQzj2s0wySheg1j5_zfIAbQICICpdKW6ijmWOC_Z18vu5Z4LqJii-eL3XUFHy2x3Y5nLWGF3q_Hx8nrTL-EeRG7Z8XnRkxEt7EwXwGDWB1JnbOYMKbRqJrI9CBf69H5TtK-ZZO8asTzzoL-4Ht_24amJgH5_n_xUmr2xivetCBNp0-IhjkiejK87AuSbbpgsRo63k91fk2MItB7blW1dPf5-vr7t7FoZfdLnZBn0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپشنی به ذهنم نرسید کسمادرت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/81398" target="_blank">📅 03:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81397">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اذانو زدن
🖤
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81397" target="_blank">📅 03:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81396">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfiYtiKapm5Qr83z4jaVDehtIGg4p9RJ_FhPRHryxoCv6A-uKptva4oiOxhAceozPNYp9NCzh2vuz8wSkOEkD7snivkQsIr-S4Fb6IqRQFBv4jfaaEOfAgEV0zvqS5FokmPefypyPAmLOHwy7T3N4ak2TgzEh0AyXehAL9RbMZNTtNv3ePCtZkAFED1jZVyi6fJ8eO7d9YLcAGTD2oZO1NTPoaBCcLCeuMNalgKz_pxBFHwEIYygOr2Qc3niJi6JtGCgkCOUYL9hDKWw6mVM8tY63yX3ni4WOEPEKVedEwUjwk-qxYN6YjLXs_DCyFDHO06-gxrwnnO8ItWl2HaGfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/81396" target="_blank">📅 03:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81395">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اذان صبح امروز اصفهان ساعت ۰۳:۴۲ به افق محلی است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81395" target="_blank">📅 03:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81392">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e358934688.mp4?token=Ri9TAIeQc1CHdLdSRcy0ORDJgoWgQeu6daH9kTrlHx8w95jiCzxSoloTl85b5GmRO6_yIXpWui1kSarejRDsXjsozQTXYNn6jHrvs22J0ICDg_wB7fm2pNuNU-BR9F1KKaaeKz-fx6tIesNbpwfrYLtlo14TJK20LDjNlnFZtq4FDUz54VPicHixr--O8Uzv3o4zNLQf3_SEZgf8fnYHaCz6HZVm9fo_eXKB0lAs2tkeIxMshwwpWJi0i7u7TX3IE7tE2CcfX3sKoNZbLNj26auF1Bj9snt55mrq6RBSZSb0mVtWSkVvsPdJek-E6Qu6ZZ1PRED-GZmsRqxDoHCA8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e358934688.mp4?token=Ri9TAIeQc1CHdLdSRcy0ORDJgoWgQeu6daH9kTrlHx8w95jiCzxSoloTl85b5GmRO6_yIXpWui1kSarejRDsXjsozQTXYNn6jHrvs22J0ICDg_wB7fm2pNuNU-BR9F1KKaaeKz-fx6tIesNbpwfrYLtlo14TJK20LDjNlnFZtq4FDUz54VPicHixr--O8Uzv3o4zNLQf3_SEZgf8fnYHaCz6HZVm9fo_eXKB0lAs2tkeIxMshwwpWJi0i7u7TX3IE7tE2CcfX3sKoNZbLNj26auF1Bj9snt55mrq6RBSZSb0mVtWSkVvsPdJek-E6Qu6ZZ1PRED-GZmsRqxDoHCA8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81392" target="_blank">📅 03:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81390">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">معترضین بازداشت شده با اسکورت شدید مامورین برای اجرای حکم وارد میدان علیخانی شدند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81390" target="_blank">📅 02:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81389">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64626deb37.mp4?token=alSjh3vKfmb-0IQQ3viXat9-mgQSOSpecRgGd8qRQtlbv19a0Yl16xmaM4wnCqqNs0_iNeeLMfCJkULilJA6JXWmDZ_rcCTx7R-B-Rfnrljf0crtbR-8Us6y7q3SH4p3cLKAphMBK3Q2_rc3hOPxdw_Tka96rZZ9-EdL39bojAabNrDQN-v9FUGnJSOKfg_r0UH2g0ZYyp1XEPbpfLoM1M5D6cl54XMICho_T6dQSXs5VLGfJb05gvaWhQC-Sinjd_qbo6Ivx0TuFPqYTMq-QuaECdsPfKFJLzrpCMjmnKAgur0U0nHXZ_AUosuGTcMt7fPDyk7LURR9b2_SX3tOAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64626deb37.mp4?token=alSjh3vKfmb-0IQQ3viXat9-mgQSOSpecRgGd8qRQtlbv19a0Yl16xmaM4wnCqqNs0_iNeeLMfCJkULilJA6JXWmDZ_rcCTx7R-B-Rfnrljf0crtbR-8Us6y7q3SH4p3cLKAphMBK3Q2_rc3hOPxdw_Tka96rZZ9-EdL39bojAabNrDQN-v9FUGnJSOKfg_r0UH2g0ZYyp1XEPbpfLoM1M5D6cl54XMICho_T6dQSXs5VLGfJb05gvaWhQC-Sinjd_qbo6Ivx0TuFPqYTMq-QuaECdsPfKFJLzrpCMjmnKAgur0U0nHXZ_AUosuGTcMt7fPDyk7LURR9b2_SX3tOAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس‌از اطلاع رسانی کاربران توی فضای مجازی، جمعیت میدان علیخانی اصفهان هر لحظه در حال افزایشه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81389" target="_blank">📅 02:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81388">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JT5Mb_3s4Yr_se3-aMWS4AC0BvKuJDjMjlM-m1yjFxNmxLLmj2C9kM6EDflQdYv0u1jTmaFarPyswiFxicl5DR3xPtss4KBdAtTbe3hz9rHvgxvV3FyVvVpJA26yglQPayCKvlRDh4sy9vu7jXIwYOVBtoCmaqFu8q50wQxN7a63NcBDCAMqBNvmYJAeSR3tk1O4t4HfAgzcOBGqMKYj-P33Va-d-pmpyqHvJ12NQ76ZfF9wNavYD1DQsOk9ddINU51l4XckMr_mYNbaODH188W-_HijclA_xrYS3TCXFSwLTx7swlgvFyI1m-MP8IdxCoN0qTA8fW8PnTcY2wbw5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این لیست کامل ۱۲ نفر از بچه های معترض اصفهان هست که ۳ نفرشون قراره در ملأ عام اعدام بشند
۲ نفرشون هم در تاریخ ۲۸ تیر اعدام شدند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81388" target="_blank">📅 01:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81387">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlfrdE5z-z90rSVK-Nm9QI59edIDkfHfO8_yyZDja7rBknLZfqhpuaoI-pbbStn7IcmTYCdYT1FtqWPOCPZv4DAEx_m8AR5DXPWEGL83UkRzMZhGyMvdEfkDYnJ7jYwXOWtZDmq9WJb9XTqGh--QHgtBHujdIR94HNJIjXmpHf8JUpPnVNa97Y9qiqUkKluy-EQ9U7G2WwgJTdEraDyEkPjU363TtA-BCzImvMGa-Jei6bLpaFDbAiJsJEzi3NnAa_7ypJqyBKJFPRW88OzrBqqDPxWL5fvYc_zMEeuqx9FAkbfqJqYZtXW-AhIyghptI3g1xAV91qBrwMzIU-Nwiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بنرو تو میدون گذاشتن.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81387" target="_blank">📅 01:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81386">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81386" target="_blank">📅 01:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81385">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuW6gxY4zBfQ_d20Fx0FZtrmKthLiY00ToDlMQXhEfLk7sTX4c9BaShg9WTsChWANOUNmECuuKHSOyU7HzV6fY3Db1diJfgeWsrJinMrGdF3rfpZQXs9-Vl19PbKQL6mJ9kCrXKnCOksMkyNiZ4KU4bRYk5jQU2rq8GUdD3nTC-gdTfkEcNjkVK0PxLCpxjINAv9zrk0kgD3G3wDvQU2EafWpBLyuipkg1StauMSOhLPmvMemsOjoYaZxBNg5j_fkHwGTjtpSHvy3DPsrDrbbeg4EQupE2fHPaXMyjc3gNjCWd2ENG5o_CPodGQYvYHCpnDNUWudQUgEy1oyWdlShw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81385" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81384">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">از این ادمینمون فریب که شاتای پستاش تو جنگ ۱۲ روزه تو کامنتاس از ۱۸ دی خبر نداریم  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81384" target="_blank">📅 00:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81383">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMA9wr_kg5pqm9mq6ppYgW3x1mIEGn_UWZtltySbKDIqRIlMuJGG1yanQDjly0gmpTutkKwK2EwKK4gT3oF5Hysz5c7rHhLQjDoS6W6YersTlzkcbWCQ3-MiY4griGWK-WTRJWrZFCAXSolUxHLZDYVeLPj07wFukjPRWgAihqqI_ZCz3k-d67-tR4qILMzYtwfloAisrGnLUDt1s5aaB6GAWVPtE-g_A8VqY09afMueWr-_0e44AOddiC333xZFUZ03TB_Tuv6L9cD3BsM52G5EhvvG1_ibScxc3K-0966m6L3ol2xAWKBgh5ChtQi4k_4UbkT1HGuLLznU0AtBtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی این دوس دختر علی سورناس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81383" target="_blank">📅 00:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81382">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqQQsEp897L8iJdjkGUyOb2VKoXKUqVsSPfK1aPQCbnuFnrGAY1S23MZRv6Osb1RpdpNc65PMqg1iGr2k5a7oxW63Pi-Ykm1s0f1u4JjqakiFLOuaHUH7A4Bn8rzRZnziM29octtzk2Z3b67ZNLnP5GpncP2BTHn4AjMpvhYvHJH4dDBGswgrWoT9QSXCIxEI5KuGiR-8a6DiK4oLoobuS6pUaUlAwTFPEqRU0qvutiB3RJnCrIYHxeT1EGsfMMPlA69SdjwMdjWgdNjKk5ItkFREq1RjGaCfRVBM_dzaynxgHtQq9Yrwxe6uiwFVR18qq2y_eeQLM_IoPZnyu9Fcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری، از معترضین دی ماه در اصفهان، متاسفانه فردا قراره در ملأ عام اجرا شه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81382" target="_blank">📅 00:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81381">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YN0sSvGwRKROLyyxwiKqZ6RJ3FjcAQDpCjPm_5CJd0-iZooEK85hWovXyyqeroM6930IHWBVttYNv1sKqoE2wXI4pIflvS4ccIyQMI-CaI2PbUwxAspoMd2lj3Km8ZEynfJsRhNW5PPfs953kcneMHpVF-0pmgNBmj1nH6z3rI-3fyR9vjcFmaLuLio9zDhvJQrfTlfcKPLC6WbUPIw4CWkLGd1kp_g98IvNAveOHppXTEv9pv5KOypQZFrIvx6JgMlgvk5o1yGjqa7vVBZe_q7SnRG1Lzf0avXaBLiPmalfBDCXQAYFIMHDXXaPw3E4PNKImgRq8_VoFzpnpHQKqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81381" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81380">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqNJYBBZRk5b4B9YYjaEDq3Hz5Eo8HDkfC8QlPFT6auBa7zvILW1Y5FPIUcVRosQFBvvveRTLBIopqLq0LQA5tEWvKy1QzQPJcvMdovMZ-n8PVWjUtXuEAelqAZXdB6GGGOzp7IpGKk3eladZJ3H8jllttLlJks92tY8ZO3G2gd0iAn1SlkV-lTTFwGYPuG0pT7_lqbklnaYDmbnEC73r9HTFSlUmpw6_k0jLgFfRRuBdXIUhXBPsPAfmwg7ToXIj879M6L1LsJsKXE3qXWMOfJmohWtU2PbSLWmNxshxZ5YlipZQ8QNEkJAJrHAcwiL-cLiH77T7yQYowghTB_-fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراد ویسی بالا باش داداش کلی تحلیلِ نکرده داریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81380" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81379">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kR0m7jvX5BlJm-DbbelEj4JCj3zkT2Vo49UYwknAS50ZE6lvBb3U1bQpjzobWD31RJT_iPzbVo3ti4lYiPs9tnXwzzburpLWV3Wi3WYwtSbFgRJxUMxluEZWFO7xZ7sq_Teap4PuK_9Z3ktjR5vjHPN-a_-oj9595J9R-1ooa-DlXlvCwydI8QpM3g04WuyapkZJIoPBT4L9lLnHRQaBaZ98lxv6Y_Uc-tlpTEMt0BMQM59AUkw_n2KerJ4-Sftcb8W73y7cqifvVxx_I6nvM52N9aPmJXF1uxqW06Q2aubOCgYk_rAhaIL80F0x1BpJpCLpLRcHxsaRIfwL-lszKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید فرزاد قدیمی به نام زل منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81379" target="_blank">📅 22:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81378">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81378" target="_blank">📅 21:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81377">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acIHENqKLKoI-XS7dwh_2gG4jxiI9bPjz1Mw7jl1een0foTo1T4J-HC7NeEsK_dBCzJJ1kWb2cpaTp2akvfKT4KkQsx-teaAZzdeU6nVgENoBGCVHXjIMYAf7EzMdr7eho8U06N67kkOoGMDueE3aIXKrwNtK0yyKmbK9rmmlK42RqlZ-TLbs-588Kdy5-oARCl10IwhdYswtF5FvIvxKZl23VUC4GFaRpF9psUkEqs7cqugkjz9JrlznhcPMpTxhEHJA8EDeJxzZOsXRoEI7-7meuKM7TeqrbauONqJ1QXrxzacVC3xZ59tnY7cJNI6txGnU4Ty85b4eLoMCs2jnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکا وقتی غیرتی میشن:
Gay rat
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81377" target="_blank">📅 21:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81376">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3BfemqeuIbCTcg3uvD0NTEEKk8_384JXSyYRIY6qYDtWEwxOKGgEtvwXj8YFYiE0BEtJSJIE0NL-6A7OKAHxNe9hsOBtH2ojaGiDqEa7j6RszVNtA_aEOrvAgEjO6EEb9k4MbFouDfhfUqT7WJnQzsjkslP5RhU5acLgEf_yjbp2K68DWJQTl7oR5rTcRWyvzDinE_h_hdFdyo688KtrzKgtNYciYQ63T3ieP1T9r5jy7WvMEbh1GaM9336aAHvl0_jHfGe-LBoKYz5LMmJuGn_ezUSUiLLMQyhuu8Sz0n0JWSzF5oKKwYEnlo_SuqxUb7axFbxTQW_J6764j1fiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81376" target="_blank">📅 21:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81375">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O21-IVX29MbP2hZaMkE5I0DikTKGT6I8Eu4ey4eGZ5SPBHsl4MYCfj3PjC-XE5ArpiFIxKq3x0Co4U8N3cdfFaH4sbBA91F3PazE-L9KNYS6URf98Xrm4xKPPZVEO81RgLzym-vKU-6VBG0graT9ppbDSAq6HkelwAFG8vhkHQPXBKgQigS__R_d4eJinrDx7rJeCAxoKxHelmtHRPMKsMKwcXteYH7sDas1xJMuruZSwz05wiuxMK9ENDWi9UlEP-_QO60zDHsv2ayUivRiVty0_z8MTXCSW4afWIRHHyVF-8iGLGzaUKQeXX5IGfr9ffBhLS_wj-D5Waw61-Avlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81375" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81374">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IkoiI-OijPfToL3M8w7vAvHWCEOZDHNMe2rSUe3RO2QD-dlUiJrPDO-LT2AraKLGnl2sKhjtfN6BvMi_oorkhrh4qG2cwjDjJmqPRztqqjtgsyUu72rONeeYCIuYcLHj5dk8NTzb9nsB_zxmilWcKLVKMkZMjr0YJdLknTAvmDKd9uHbtIoRooWNs5gbrcq0eJmxDYLHjJ8ZgU9VUUEKNff7FPLgjCqLnhK88JWJ_vsgrSd8aISz5llELKPOEO0UgnsIHxjJ3zOODfn-AMrd5om1uk7bmhl-UOyFgVz7Tr9EFD1MUPd00zWD7Pyp20mhUAjxPn9xbCj5JZZ2qPrzEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81374" target="_blank">📅 20:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81373">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmpXhH18mmLyJmk_W7z0NmWMBpUgppjFtLzApDZPG3XB_PJBEehDFP35v-x6yvuf5Pt3z3bZ1VuAX9yYcYvbb_gVEgdbldwfCnfhZeRGa4_8HBw_1OuFRA8OR79ZB74UPsuXxfhPINOWv6b7JwaKvWowOtkxMXLVmtOPHcWlrv-N4FsP3llFY_fSdGOQUNsBA_SesNX02H6thHVstYse4B6ZttxIjejjK7VfEf8gX_1HyZ_HztyFWuvSFOET5aGteWkubVJrmyWoYYMUMTRLz67p26BoUgrFNTf4YtjhdbfoAsfaa1ctlLAG87BTudFmLzEd8y26JLeYXZNt25m3sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام پسر
خلاصه‌ی مصاحبه‌ی جدید ترامپ تو هواپیما که همین الان پخش شده
عجب حرفایی زده کولاک کرده این بشر
👏🏿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81373" target="_blank">📅 20:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81372">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sj15EWgCR-kGBmLRyIVSfQkPllGV6XraOuIyNLK16hhRYg6SzdjGWLFrDq1jznPPBwlp60o02m1OsjdPwjoUAlfr7NSqG6cDDgzMBWcp6sz2-DolZyc5gLIcPvTnYcK5azb7qbNEpU4tuvb8INxhMedLxIadYpNf9V2bGFzHA3zdBYl-T_GeNjUk7xjHvFUMTQ1sj9WFi0I1WIOE95kf8KcfrSf480I854j-RVx0FlvxbWjtzC6b1ThxPg1PB4Xi6V5kFSxI2eBO1mLMjrk7UKh2nJ4DMpB1V5x9xhSCUjGH70ORmQS_ItKdubSUxNsKFPzImOwpqkFjp1qJhYyZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81372" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81371">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خ
دونالد ترام به شبکه‌ی ۱۲ اسرائیل گفت که آمریکا درحال حاضر «گفت‌وگوهای بسیار عمیقی» را با ایران انجام می‌دهد، اما اگر این گفتگوها موفقیت‌آمیز نباشند، ما به اقدامات نظامی بسیار قوی بازخواهیم گشت.
زمان زیادی به دیپلماسی نمی‌دهم؛ یا این روند به سرعت پیش خواهد رفت و تنگه باز خواهد شد، یا اصلاً اتفاق نخواهد افتاد.
تصمیم به توقف حملات آمریکا گرفته‌ام، زیرا همه کسانی که در مذاکرات با ایران دخیل هستند، به من گفتند: "خواهش می‌کنیم شلیک نکن."
ایرانی‌ها شدیدا می‌خواهند به یک توافق برسند و با توقف حملات موافقت کردم، زیرا هیچ چیز برای به دست آوردن و هیچ چیز برای از دست دادن وجود نداشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81371" target="_blank">📅 18:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81370">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHMtdhjkDHaQw4cNB2CdBenPLMsMO7GFgKIxDHRhb7Mrk1tvC7KdYC1SBpa09JG5Ab2Mx_yUQS74Kt4TOddoWeKTuFcwd8aLNpQu73EfTjoNP-QTRZ0hpYbtTptTcaH121w2ca1JIwgW9UWrue4vdOzRZSI9pHcvd5q5nrMhoqvsVSmH3vhRUovE4Sug7Lu92hMukyMdxDAf0o7zyxTnY5ljkfNIWuPuY2K_0H3squ0nlALrAE3acBKyMF-QZDhfs97BqQdlWqwKubqdcHiWSHnOOK3owTFLB4m7pOBZnRc_fQCyyqpDPE1h1wGGK7qtIDkvVkvaJv22LsFOm8B6Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندروتیت
دوباره به جرم تجاوز به کودکان، پورنوگرافی، قتل، قاچاق اعضای بدن در میامی
دستگیر
و راهی
زندان
شد تا بهش بگن کصمادرش چه رنگیه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81370" target="_blank">📅 18:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81368">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TR8ayWdeCBgk9_CKtSOxQQCA9PsxPvSyA_7Cfu0fpVE9uprH558OBn8KKhKac67pAFZBjMmj0rfbN4ZqA7UwY52JLYLBlvy_TEIbNQHFGPEtdiJGze5CLO_jVhY4ZhaGQXXxXYYsZFj-ji5IHa90-oGXjtIQI96ZF8Jv_HjPOpIyUgZVd1rGw4reHm5PbcHt_GQ0PYLv30qY4dCCXV8T_Q2yaYIB0sOICHt_x_HPXsvBPNPicvCRQEe5b9ULcpFt480ftLHZDUEWFBZQ-HKt7_srQmV_dX92w61SNDkj8Ll-daUpZRXu-geRp99EIjWIL-7ClvEKN4ccflWdFcTp8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u240_HFxECf8-BDqLnXE-hcAudHi_Z0pucE67eTRV20EQdNsyajMaINtH-UTbUo6zd7PZMd-OQBxJvtu7aF_xU7iaiE070_JbF4dfQfXkjHOhKspiV-oZdDHTuJwiZJIx4ar-2aQQV6Gmd0TPyORSf49sfQdxI5KaT8jkMj7zi6KC7ZVDucLIVphYhnJquo_cmdcNI8JzFgF1xwvX84iIqXRwUgPNorZ5ug3xU9HklLNVkVe_IHi5mNVRR1KOanUI5pKA3tvH1uKyCcm9H1Cj9ETE-kaR17IkwKdc166Vn0SXH2wJc3uql9Z53hkmbfNfEJkBAwkN7LqVfxeZ4fq7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رومرو درحال رقابت با صدفه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81368" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81366">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کانال ۱۲ اسرائیل :
بنیامین نتانیاهو با چندین پیام مشخص در دیدار با دونالد ترامپ حاضر شده و قصد دارد تأکید کند که جمهوری اسلامی، به‌عنوان یک هدف راهبردی در آینده، باید از میان برداشته شود؛ زیرا آن را منشأ شرارت در جهان می‌داند.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81366" target="_blank">📅 18:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81365">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=AUznxv1TJP_KGUK8D0Y86vxSeIMjc2GpwmwFdZclGU9DMXI77bBm4YKHQ02-mliSkKXNeo_SYFI1dn9qXpRzqDcsAHYsn0qT_UHys2b5Hi3xHrCgPIVEaP8AiPHrATeS305EQIYDgTq2DvV8Gaf2pUAs5p3Lt5WKAGTMPTQwm3Am6glw7Q4xq7RfPcL-d328upc7ZWLcHtVB4Kz3JA4bnjqQjf9o0RShBmbZOvYevU5Dkx32wjxvbIvLCGnyZMve0d4ZnBwf0LLa7ISljJs0uomC8NOfQRKH9RACon-AAKeQZP4hwvJBhhflk1pZV30wwNxQbBrXwLt6yJJ85WL-0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=AUznxv1TJP_KGUK8D0Y86vxSeIMjc2GpwmwFdZclGU9DMXI77bBm4YKHQ02-mliSkKXNeo_SYFI1dn9qXpRzqDcsAHYsn0qT_UHys2b5Hi3xHrCgPIVEaP8AiPHrATeS305EQIYDgTq2DvV8Gaf2pUAs5p3Lt5WKAGTMPTQwm3Am6glw7Q4xq7RfPcL-d328upc7ZWLcHtVB4Kz3JA4bnjqQjf9o0RShBmbZOvYevU5Dkx32wjxvbIvLCGnyZMve0d4ZnBwf0LLa7ISljJs0uomC8NOfQRKH9RACon-AAKeQZP4hwvJBhhflk1pZV30wwNxQbBrXwLt6yJJ85WL-0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور:
من فرزند رسانه ملی هستم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81365" target="_blank">📅 16:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81363">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jz8_V001p18sAJ85BEyoN8_ByuijSYxEjgYF-0yib5qlL5iR1cqn6CQdi68gGPBypAEIaU0XzlQXqUc50afII2ESPlw20c5Y1d4ekUbDkCBwfnk9NUCuX2UviXYYEQ1F0CsTpfR9elBwtA-9y9aVkCToCKUHFIm4kjYkmO78t7A0wHhWE6tLC-s0uN0EnXMB5p3oBALuugCONxUAbXrDi4LKkQ8vkfGY7QCgCv7H6IWKuCuiDiqvwTh6mk8HwvLOt0_mhFkbmlVQFlnXOFwoFoODtZivV0OAMvdeeZ5oU77PrzfJWma-_Yr57TzHslPZszhmR2F8585kRgq05mRvHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام از این جا سیگاریا برام بخرید لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81363" target="_blank">📅 16:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81361">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oq_9WR8z5TnxYiu3uYe8fDbooI9P6O8ii6uxzUQ-QcrCjmvk5PQ4B8hzUAnKQ4c7iNpX3vR9XBIbHxs2oX0OT3LRxR7SPKz2UqmX4Ablhj4SytF5cUHVynBnj5lIqU6WhdwBSIPCIvueHsN5bVOa5Sz8qGk0rtkZseJe38xGEfZtYEz_tMTf2vi4E8DNvOm15QRivefuVxWYHQvh_lG6gv2CSpNPzrZpYRRBE6c0BFMJsktcs2OHcvCui4bU8noKDnQXD0yhKr6Gcg_LAXkqA3mOfrUk3VEWa5LoZa2Z38ZFKi03IDNSnjVbU6AvYa1jNZRpAfJfAvLspGw85M4Kjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کاش پنج هزار تا استارز داشتم همشو روی عکس شما میزدم بانو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81361" target="_blank">📅 15:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81360">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تو 5/5/5 تنها کاری که میتونم بکنم خوابیدنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81360" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81358">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81358" target="_blank">📅 14:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81357">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R25xks3tCRF1Afu1088S0RSUGM-ON5M_JyqdLg9oix9uaACQP2m5GGuPV1y6NgiW0veAtTQUIMmvkWPbfOh7gNYN-UGZYuVVpu6vlYH_U8drB9HVZM2d31QorCg6VvQourEQxZENaMHwwvKXZDDni0s2jBtHDOUdiJtCi7iTmGKpYrswPA-ZtNQGBDv-AJTtL7eq3jo8U94wYaKNotgJ1plH0A-VQ6_SsoTp2KlQ7Wd0g6QvIxzbd7LHsEIzlIvP2f3uMwkNMu3NIZ1-HuBTDX62WNjc43QC52eTiGsfpC3Y0uUIbbNMLCyKtlwVen4hlbYez7fbekxYFi2Ss51C-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81357" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
