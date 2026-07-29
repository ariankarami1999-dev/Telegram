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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 20:16:35</div>
<hr>

<div class="tg-post" id="msg-81493">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پرایم هیچ بازیکنی اندازه رافینیا ۲۰۲۴ بهم نچسبید</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/funhiphop/81493" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81491">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">از وقتی تلاش نکردم برا باز کردن پیچ خوردگیا هندزفری سیمی کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/funhiphop/81491" target="_blank">📅 20:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81490">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پول ایرپاد نداره؟</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/funhiphop/81490" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81488">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjLtVA0r1YvS8V3ZyUFmguDUvpmqvl5mZRdyJA_mc42cdIabliE9xl5jEN7QOP-AG1yiFyc2eky0-ZXm19dgesVid04hwJDGBes35HCt-SkhYyVrN3KRf113tjA5nmWyzWIjx-83afN6HaDcP7eyAOXo2hFMn4rZAa9inETAtxAZ9RqqpBMqRw7Kp24icM1rvfrRN_s9DcSFp7cyyJIEwwSg-NDv_9kyk3doxdiKOArTp254zLTm2d1PApgRS4EbPG7WdIf2WiSaxAdUhaS0npdQqs2NzmSDsC_4pBzu8DJcAMm2lWYU4k9TN9_MQSIdYEU9w3nr00ehcVkL-tY_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuedw_L47y4-XQaAia1f0zUJ6E7913LDV1uZOjE_hg3PqrMIjQW0WIkSt9Sa9CDTewbOa_B6vsY6sPfIxtoUCCOpyqZ0coFnzXiJrGc6y6uZ3MasVDaP1P3ZNsit5DeBK4xbbGA6NbPDBk8-LLG4PZOzjwkbQDjAfkzH1vI53MAMmmIRT7nABg5zjCr-08Uso8orBbZzhYBXO0uKQZx38MMn27ldNditvHCwk4KlgHjcL6dbkIhQd9VxWtLqg2y2D1lkHTm8IW9qzyZq-eTdpMK8B4XHiFIc06UbFYaLlqpxy4mmj1Tj5l__YRECofUCvzlUpx_xWaprYE6pEsESOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رافینیا شبیه زن جنده ها شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/funhiphop/81488" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81486">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1srxx4ZJ12yyKMgTUBbXk9h9KZkh_XekLH9Zubj2C2pUOlRR_tI70XvwPE8zl6LGoASR9InUM_WGV4lkk-q7rgwgT7C3RFn8pX1NJE9sSIQYKakXE7Fbd_UqUD5AuK8rwWbrqq-8MgkTRqjYvOwZhMS7hQriNSSyXIMi6dQ7vgsI-zPvPXzncHcVIxvfimzEjtkaI6Gza-IBIVZ4MsnZrubkvVzgr5Kk5mrQL42VItAlV8EMoeR6BpZS-erkdlkips1cMii6wdy3oDkgVFO5foBip0tvKgRsavU6wTha_FOz9MzYlGfEnW_dY4cFV3f1fgSubQQuC2ZfxVDTDHqfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJnWTgqBWQ9HXtxO6I-A1JwZXT6THjb8nDpVPxhDn7S30jfIjDyTTZ6b0hctusVpiQGpeaxyeRjAHtXSoxKmrXyEgi3Vc7_HBpQ3B3luOg0sACOeC5pLa9LLCNbid2QeZM-4V-x4DypRcOAd_6kcfy-bGdTDanoDSdbiG5It-tJJbk0r510OCLaF2fNwWeZ_pICpDw3wqnfDIqCqMM0aX3fbhI2623B2DQFlcdGZHQkoM7djzczK2km3EnVTFOiHmMnuUck3XbPNX9p013HS1RkYtJGCF3NLeHDOnm_47Eg-4zY0tiBuOsJmwLfZSmrnpeBKzpnRXvStqF18R8uuHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرکاری میکنم نمیتونم با قیافه جدید وینیسیوس کنار بیام.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/funhiphop/81486" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81485">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EK4eACXRJAuLMqR99FVjuiS6Tr55HySDU3PsyOi_UNdc8AZCPGsLwQV7K1znszGiv5VUX0aFuFJT-mCy-d_vUSnvmeAq5ebiAPmCqHx89_GgQS3n39jKgysz6mwPOcNwWdAG35SJa-QjqBY2E9DVhpNYlntWjyqTVqr0CVV3dFy3lmVKH0EEiO68RCTrr7pvM_6Oqn0mJStVe0PU3yQVfLxdtjaC4sXt6XWzfOyU-_W7Q3kRprfk6msVRe41z1dXLxlDgZtsJmduDA3qvYO7yZa3Ce6xbIQkZw6J1U8XAfaFnZLAHRDkcA5Bot4HvObvCbGhkTAmvRRH8TxtszC4Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/funhiphop/81485" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81484">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVA8E51gftDj28A6TFo4Bfl17FCXzM94PDw_xBAf3tMMb7CbiBpIJUCMUQafj_bARr69TcluzJ_1Je2wZ-Sl8C0oUFm9DdXQ5-0XyV10h9ItIr41LVj7FF1BybTfovkyoXclBKDyvZq6bM-I70yup9Axponlsxm1yqlVIZo2kKb1arsFpCt69aalXRq4UD6mF2Whp2AYkCtRSKQcyvR3MH4WcLy3q3lf_hz1k3wMJW1DOEnMcJfC_2rfPx7JYSZE52COyvZzbtSUzCRsGZ4YNkOJC8gr93GVV0R0nSXRGvpNLinXOSSdMtdcnHshknQD2lo80S6DiOQsKnJoTc_kGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6K · <a href="https://t.me/funhiphop/81484" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81483">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFnS6qHNL7hZIq_yvH-5veGK9KCb145R8OaOa7NTB3h8akqFZPBxaG_pELVkoQicikjE-vEiB_EWjNtUbsA0Sm06lld8G1GiazpbSdO6Pj5GBQk1CJgIayufBgQDZGfM9PBBsR7_ETsouG0SUvjvTNJYxK8hnXnT_R-k5RFLjmDrItqcyljP_b2hvExQM2S3kjt6fcjY8rxp1AMjWBXI4Lz-NgZU6gDMvYRyXLPFWC-5iFgIzP0kJ6CJh74P3ci5K3vwVXJPnFfJmmvhmn2-Eht-Ufz-mHaHU8e4qdp4EekYcw33657jd_2CD-T0hZzAC6RHnZ2dXqHCRcSEmXkGjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس جدید صابر‌ ابر و دوست پسرش.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/funhiphop/81483" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81482">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5tFmQrabPwRcsxQ3oHcxLJOai7MjKMHGMZhJDTc6RQbHPEJsVkMyF6hkjVHD_Yjup71YgxBbGLkQhHFJCvC1eb2n87IP51-dOzX6TVcP_CiSdOw9GdTO6aw_aEUKNj2hwBgsjuEuK8Fj7LMP8sUR5AvcvozQBHWERFEMC_oW_UDGO4_7mlFNsyAMLHPeAiXYTZbEQVWxuyGlg9xCbPsgalXzri77M0C5--VQUIWDsUEfRoTegErgy75Q6kNMr45mQfXEWjIMLEA44DY-QyqIIyQW84wXdsydmrS0j7iw3YYEjRbSL-rLWMgE-AqILpOt18oKV423XxjEka_TeZW_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/funhiphop/81482" target="_blank">📅 18:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81481">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkO-gqEBmYBqPDWSnEq5WEkf6KD14Kie9ISkIhkYzly6gM8NxW1swhQqGqgHt5Vtxqqjc8oDm5z-cxH8uln3wKosPwrkNTOXveVWQl-OcxaJ4LF0uNEJPIjZW1N9Yap5_MiCrE0OJD8frJuC-wIA36A59e7pcveQNboy9hTHChmeK3UBnnOX4LDAigaRlpR_9gAVwapp_z3BYYQ0MxfH1qlI5WKzLiK3creQvXBFMMDqq7T5oJzRwUvyl1isS5vAUoeshG4GQfIx_2DpCYGjdSugfliwUg_hVJQAmNKnzaoQTmXetdXXLUX5EyggH1kZxWpz0UjSzE3zhNHRpXHhzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش دورف:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/funhiphop/81481" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81480">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/81480" target="_blank">📅 17:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81479">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAzgoY4YLB0TfGhDKYaaC3iMvmfzY7dNqxr9WRsXwPq6CDTlNnmQnZwdQMK5bxSJR1wd7z_a_ZiW4kphk1QIj7erPGjp8i-LJVzpegB3S5hveGytfJ-SB_gk91JtyNxl9aT7wyGTBCvX_gSfo3-_qGNIPA-dZ0DefRk8GNp7TCwrAORXY7USlUsxck-VJS_wCo9obKRAJeauI2bmSStYiiHofG3CO05Xz3vm7HhcCVn0O0neu23zm2btlB332lnuZlLDlKnxR-888_s19O-7fA1ETeIaGeMIRskix6lCT--qLN4UNHf1so5kQKtHMmDg3sgr4GhHyS1js8CvlMsm7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/81479" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81478">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZk1Hb0oj8sJO_Mx-VUKTX_sXnIIKjERU12iK9mpcRmMSrd-GlOPXep8rY5ExfrBYw06wqox1rbag9BEtQZ0jkYHaOT4IU8AOqDwDGV7G77UDoel24Up1_5RyYvAr8HddwTxkGz1CKDiriVFY1h-cPd5XQmDOlwxMCXqRRSFFXxhj-eJqaoqwogGhKeUMtTLty86gJNGGiTr_bKQo4z9i2OG1mYqxfVpwnktANUe6KrrvYImGCJ_a6jFgkkZpNKAWME4l8214AP1X4z0fmCZFv8O73DTh49mUcgRHyADxWlLY87GOegWVItSXUNmNaeq1L8hyfe32ppzedR4cI4_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/81478" target="_blank">📅 16:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81477">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ: ضربه سختی به ایران خواهیم زد‌‌.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/81477" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81476">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">منابع نزدیک به سپاه میگن در نتیجه حملات دیشب عربستان و آمریکا در عراق، تا این لحظه دست کم ۵نیروی ارشد حفاظت اطلاعات سپاه کشته شدند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81476" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81475">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81475" target="_blank">📅 15:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81474">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81474" target="_blank">📅 15:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81472">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDl-nxz31RY4sekxZvBCxbWLzrbPApDauf5_-2kHU-5Y0ryALsC6H8SuZbBEjqjz9tAy2cmxH0PiSb3IBobqYm4uhFFUs_Fo1D_oJhSZu4Rd0jcluHUYQLVUiUXKves3e2LwKedE8lhz6TVhMUEpXRvAV7NuL6hOozyuVEPJefXVI8fcQDVMKyvGcokkPBWRfY1DFUgTyY1pDgg-pYeICIy9tIClKdL0hBGJX6O3cdcNYTq6cdKHgbzUcUnOjMEu6OQ-ODm7p2VXJ22Sn-BlOGAT8tNJ3371MBfRY4L7Hbojwcw3mm8EvIJLEKvz8mEP3sapN0jpAWFKRa438Zoo5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81472" target="_blank">📅 14:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81470">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kum7VWVCAZiZyyD59WjVptejfvxTt1eUqFsxcgI32qCpg9jO5FwGSCiUOCVbV_-PRe91MWX7SLaD6eY8bPdv-bjfZDG2Yho18fscw1L0ZDbdgVUoljQoU2z2JoiRllI5qh-ZT1tGkMPbdnteA3bua7-agvRqNFW_vChY6izX0yEOPhBSnV3DznblkwZkqZR-OCgWyJMoulKLIi_L8IwRr7CshrdB0i2eWImLjQT7pURApF63HxSkNNX7wdDUL-dkSGBGj6y4QGIERl8r2Qo5llggHezTfrdgu658I_WriYNOXgiv69qtnGV5h6xEH4lx65pT3FU3wQ3vQlHznuUq-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4z7cFiTeUMXLabEMA5SXt_cQotARivdn3cpeEJMOeg3S_iBmZcTwnWLTVuiwHSepa88F7yRFwc6Yel1i3cQJgrfd3LPHpBcna4gk4XaQlWpLkLUmMlA_BeNat_rf6V3lXdG2JqZuuWKdGAjladFADk4PCTxeP8j0aOmT7ZQpMwnRmsfKyRIGvSwKuLKslq0RrDNPy-SK4RNYxR-2SrOmj1wwhh__Q_CTKtRoKHzhlcl5QZwYJ0BES5hqntysehIECxbAEBH0p360XtYu8oi8ZNuY4UlMosgfQCJUMiICXNgYSREdEvl61Jpiayqz0Ck_tOANV0yJ0WiWZbK1MPE9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پینترست چرا تبدیل به کرج شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81470" target="_blank">📅 14:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81465">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اگه این با سپاه همکاری میکرد که الان همه تو صف اعدام بودیم</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81465" target="_blank">📅 13:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81464">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81464" target="_blank">📅 13:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81463">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دلار 193
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81463" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81462">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG4Pl1c0zP6QUl9OhppNoEnf6F6fdaXWgM4fW4K5dqyMw6fcpw518-vksHU9bOOEzlxeT9BshU2f5hEEUgfTOFBCV0zyD6pHWt84ux-pB4R6JCxnac2_8utIuz9SRQaaRakH4scHFWmwzgUlsVQkgy7n-zFd4loOCKICPefbymVuQugd-zisiGypf9Lstz2ateZca4R8XCDvWWik7zAZ7McX4ZBp_0u62J7icCcCffcmtc83kEoBsbDdn12bMxRx8uKS4CJK8BUjfzL9oMv_TqvPm0cHnvmRsG-glMsvTFTsOCdP-nBI9Eh8c64r5Mo3y2aN8Z2Q0eS9SNth-7fpdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پیشرو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81462" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81461">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81461" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81460">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">از الان تا ۶ سال آینده هر اتفاقی بیوفته ربطش میدیم به جلد مجله اکونومیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81460" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81458">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هدف یدونه پایگاه آمریکا تو اردن بود فقط
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81458" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81457">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تروخدا اسرائیل باشه تروخدا این یهودا خیلی راحت نابود می‌‌شن بوم بوم تلاویو اسرائیلی‌ها مجبور می‌شن از دریا فرار کنن تروخدا پدافنداشون ته کشیده ۸۵۸۷۴۳۹۹۴۴ نفر ازشون مفقود می‌شه کلا اندازه یه استان ایرانن ۹ میلیون جمعیت دارن کلا تروخدا تروخدا اسرائیلو بزن سردار
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/81457" target="_blank">📅 01:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81456">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ببینیم از لپ لپ اسم کدوم کشور درمیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/81456" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81454">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1P-jHLxqAqESux3Mlgz_UUo1cRr4nJFP4JuJd6i6WQrWLYj7LktWhXub0NAbzovyePXlh9ENamE6aLR-zyR_lm1_nflHtJXVwsfuXQGbs9GMWZaxf5tq-d0eeqDoqgJkshP-9ChBNAhwV0O1VSNb6XWLUMfQn5z98kZA6yUHEpEo_w-YDUmcOmvm1FxFYcmyWzGU6OYBimaIovG-2uVP8janqurh_UxguWfZVNECWWYpZJ3TepXs4f7mUXwSgX0FeGfx6JExpbjWz6_RArRt1yZseFLlrZuztpF0cvmWCeaoxpSiTp-SbezS363meG9ujZ-A1x3YlP4is-O6ANqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/funhiphop/81454" target="_blank">📅 00:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81453">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xr9HdiBBiQ3QyktDGxVv6cpaLT4TtvT2gw_zBbStQOlcLVYc0FJSME_oMxVordOYPRJwSmju5SkUETEUh7DZMq0av0YagTzM-Y5_bHA1-yiQGbDWxZh_FRCi2vezaIQLcfRWCWfL8kni0BCbTK4K2-y6jBmyF-M64wHqep3_E7h3C9Fs2mDOwXPncpttubtVEvw9icTI1LlLnL4LIyWEGa2rjKmBlblqucNZRHfdC4WW91wiJzdYHT9Kxu9zWFjch6gwC0W6RW04z2xn3vZLP9bR5y4SWzbIttu87lIeMIt9slpPSY8xOtmiSihU5AzYyTyV0mQofn0-nvrT84aC5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم" تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81453" target="_blank">📅 00:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81452">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTriMO5_2CqCRVu1fH6Fz1bJG_FPazOmAfOGjLHVV8TjKzzelSkt42crmLCCZvsWKtYC1qB6y2nbHb6aDzKrntwhub9bTEa3ZndgHq6p9kMbE9z7f0sj5jprvlIW6BREaUIutTgpA2IOwhBpUxmdQpbJIxT_H-hFbwat_mlXtBJb7RYF3yh1pt3yXXPD_auIfDFkd-UpjsUzxPmqrt9qAvY0N0bvF-EqDRGH_xVWQ4EKus3dBTTgm13kA44rcsD2Df98LkukysTYHFVxWyg26jKyzdhb2IyyJR1FH8y3DEmL0oQjFbrbHfUhvp7HChflLqZ5060HgKdNBSW7taTNNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم"
تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/funhiphop/81452" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81451">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">#رسمی
داریوش ترک کردهههه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81451" target="_blank">📅 00:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81450">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNovlgkFqabra4MEAMsIk9-xiSWTrhDnCq6Yxh517KaweAsaxIhUjzcClzrEnK09R2ExzwumQdDaf2AqTX_maHezcE3dDL1O99xRO6BAlkbtRMJerwcw1B7h4GXztEiyfhnEUv-ZXsJE-JGp8mx_nrGOXRD4rylLt2D3k_PoOaSiMFaPOhzqNseciiV3EkGdyGBlTfEO2v_vSE4-JEqUcOUkKKwPwVQ_rICfsEzceJluREwRVrBBYCyCfb2ZswdK6Q07ijX5bbhnfcDYQ5fX8tHlCcWuv1Iqf-3_ZIdMLudZZ_UPf04YhKK1ek7J_h3o59DYyapvVV_ifIqBflaLAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم یادبود لیندزی گراهام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81450" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81449">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یعنی جدی عملکرد ترامپ رو تو اوردن نفت از ۱۲۰ دلار به ۷۵ دلار تو دوماه ببینی و باز از گرونی نفت بعنوان یه موفقیت حرف بزنی نیازمند خیلی کصخل بودنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81449" target="_blank">📅 23:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81448">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkxQtTeNRd30xKH65Ev-EU_rmbRK6kSedrFyLDYniMrY_u0WU4LgIQ_7_ve27-_eNKMi9hdkIBKMquSUoQ9EIR1v-gNeThWIXVHGtss-0mCNhyGZeAJCA4jTuNIM3mlzm1fz3KKbRjrE1AAXlwnpZ-trhmdS1Gy8IwUJwiVP_gQM0Uu_FOkzHnOFRzdwGdwPmSzN8ge4lo9kOCEZMbO31fu07ZeB22I_O5x6yYdadFR3LU4lHqaqO7w8a2kfd6xRxqTEva-MwJxIWOhhj2OdUYe7k39Lc3BPaWaEm73rbxi7Gg195nxGgV7g5t1wajZqHG_DX6kk7BE9pnEE662t5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا سکته کرده، اما اعلام کرده که حالش خوبه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81448" target="_blank">📅 23:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81447">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">قالیباف: دنبال بهتر کردن
زندگی
مردم هستیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81447" target="_blank">📅 22:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81446">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfC2stlA2MA_GYfK9mpU4es593oQqRyfowqA49EVIbXW1Y3uFeU0q1BtzWNDCEivOe6kwUa-hnJxPbiB5llwP2X5EuEXXNzJc7e9o2p2Rin-JgQwbBhO4DNzV7mvAjJUaVtQlzCMKG2RySB9OjHqI0WDPJQSJouJQB8CbUphxohUvuFBTeiwVOBjdCDuqkDco8mKF9eQQ8vKMRUq43S44BvL3ZVMuiBekQXr5SrZgJMRcqqh3JI5jq5kwp3JqxfAGCJZ1jTPcxrexvjwG4aXFpJ7VEXL1YsNuJFq0Cyfi_rZyGKorIc-AUHbeEXnuDhUMmQ_OcbAW5VaBMqWQCqpVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعفری دوباره منیجر حصین شده، هم پرایم حصین هم شایع با جعفری بود، با هر کدوم قطع همکاری کرد بگا رفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81446" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81445">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81445" target="_blank">📅 22:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81443">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbSo_IuAdchC5yxQDPdkzzsWNo_bDuY3yUHJ45-orglBnWMYOSJdCsCN2tcMAl9IbI-IzAiFez3ArJd_O4k3DbogsuSg5Ncs-CInsCMZHhGAh3ikRfrv51gkoX-pAb16MiLJ7a3uv1Mv5DjTN2iAlnE9JPF4pPl2JVnLjhXT0t1o6DHnCfEGfXVo_5C544xJq07ZeXzO3ofRc88TrlMJ8k5K2b1bt0RKs0g0TbAzD4w4BIedQ66kJHvJN0wjD5EuMXkud2nSgB9VwWnxH1V3CtV3vGhBuallrtJUci8oDosf7OUDILV71uccxeNs7phceftHGnrMwhC9FLbDHKL12w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShjRTvR0SLcaZBWeNZlUguLGFDkGy5b857eSqpaXzQyewSgfbdyFeyqLW4pjksFgQmgJGLQstkASNwTsIHs9AZnSlM9smwriCjBuYE7TBu2PYztrxtApJKMa409qW3quObZ804adNHj8RDEeDEuYqwjLt1O-Iruhy8irN6Wpc_fXKAArWm8Ha_-m7YvruUT6BUA_ykuTA0RzQhumNODry2g2vQ-RpOaf6rwmD46yqDgmVWY3JenS21KZ3U3cISvd6AC64d3BHltU5u3CcSINQ_G567EUAagAkBTc4E6ZkJrU84hJ_sS8WKEsbWxcAGhDAr8ucUfdPcvXO16O1V3p2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری های نوید و بامداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81443" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81442">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81442" target="_blank">📅 21:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81440">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bR7appS6KeVp20zEHy5VxcEiegY-jgvQb79G1wJVZCXy2rNDO6VFTlFtZam6eGYFPbbP7CUfGMlQLOjrqz3TvI36cDHqGnFinxKdUeNI2__nlHN9R2nEKJzV35s9p60R4d723RYFLzt686TNMDkQsSsXldJEZlnCL1udu6JX9zZ68bUvRGC7ncQtaA-a8m7DoU7v8w-qdxPiI5pz6dl9K1RZhBbvT0qFvXaasezFKBFduc1riDkFM-2VsNDBgbzFbrxshilCBt2bRM7w_zG2RQhwYYNJCQhEE2NFutcFwlYuBSl2EpQnH7QL20TNKtpNXacSnz43P2cK08FShQIBpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjxY_FOwZWGloVg8FSe0A8e4gCxuF9Tkk7dSdVeHxR36F4CC5Bdc-Dr88U0pXgPta21Hnrv5z0vUMCMx3fMCqRIfX6fXOfJPlex_GsOb2nX4nOGIVSLQh6tkN1loUIQtfq7S-AumAWnBb2tFcpGqk7oF0tcAMtN_jDli8lrghXn8lHNyXC173RbPv1rfcrYuuQxziAFLYYx9qm3ng14ZwTVPv1J5IQD4xIOXOeg1GN98Um682YXbHwNF5AhAhAtee_0u9fjuDRELJ4kM5n_FXASNmm59U8E2it0ou3Z82HN5U_0vhL3RSSHLg7k6JRVOt6w4kfIrsDSzt0nns1tTEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوکوریا قیافه دلافوئنته رو تتو کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81440" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81439">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81439" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81438">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بعد از اتفاقات دیشب شماره مادر سام صابری رو گیر اوردن براش فیلم سر بریدن فرستادن گفتن سر سام رو داریم میبریم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81438" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81437">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شاهزاده قراره با بی‌بی نتانیاهو در مراسم ختم سناتور لیندسی گراهام دیدار داشته باشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81437" target="_blank">📅 20:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81436">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtDJhR85I0zteo30RepCapqyAHnATS687XOzPVOkjvced-kdnK11aszyCezPnTLeR-hLB_eIvm5YbHOVHSEApv7L2N8XayB8_xt6gUcu_MRLRmpx_BF5T9qLrHyUSH_id9QvfTxGv0uGLcr5NhjRUv-rqTTKUvYtpdBGoQOf9-YInOXNFJ13xRevzv5P-eL974_wrYGbdDOaf4E9ha1PpLC4oMJiWATun32qch5lXr8lsGhBz6lOODg1PX-X0sxcBCzul-7QO-Y2sAf9EH66R3fV1CNuvvg7GTcFZ913kIH-gtlXotJPOQOr0ZSjHbwViZGy_-7_ZdXMjhvjyNv_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه گذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81436" target="_blank">📅 20:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81435">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Numb 1 - Madoro</div>
  <div class="tg-doc-extra">numb</div>
</div>
<a href="https://t.me/funhiphop/81435" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81435" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81434">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OegALngZ8X0WWgLcMYgK9-FGTKso7WJO2YpbGghqJXjqKKRvo3rVV05-_ergJ6YtmKRrlVlDvy0oA0VwrNOJSI3uiVXSw8XwGibgoCw23zJVhMo4HGr4m66STkgxmTeA8kAQmDJYoPeYOmsvJ7aW9gFDAMQubd1DlhVTdte70_LqXgZypjiiunptamAVZr6xOuchZL8CDH-vh-cGcI_FLLvCAUv2tCPkQThbS2Oh1Xb372Y_cBsoVlZoXJGfIzNfUQDscN3venb5XRvHpsLuXpfgl_Lc5PzFvYe_kvX_DQHv2ZyMCmIXniAvDb6YqAty0vXGiY1SBWa8-qsRVVBXpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ جدید numb به نام مادورو منتشر شد
📺
Telegram</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81434" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81433">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">این که ترامپ دوساعت قبل جلسه با نتانیاهو میاد میرینه به نتانیاهو یعنی یه کاسه ای زیر نیم کاسس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81433" target="_blank">📅 20:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81432">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4f-eOlHqVs7IQUIHeoTgBCbfXxqBMYPatW4d2ASWarJUvpe3bPLgoXD9jxp1hoQ3UVlZNYq4Rrmqeo2D1n6-mSljIKclYZ2kr7fNLwMlkZmbuUzncIS7tMF0VLuZCalSm4bKjl8o8c6KbM4CUBBCgI6Rgkj4CxkYONTwXMMG6s9CTZ4ML6w9hZL3Eulw26PR3gIcnd1-eTX7MFrN6ZVANNqZn6xfFNmZ_MMRCa3nhQmwFrV-3s7CT68No8-_Ug9qn7ZGUXOufAw2BU93t39yy7f2GT7rsJXZ5DW1iKDAqBOMVX3_35Vy_9CqWvh8pvUS_QqKTLI9ocZA6ujUP4M6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو تو فصل یک عشق ابدی رفته صداسیما
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81432" target="_blank">📅 20:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81431">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEsJXdm-pFbzO317nXkiFlPauHcR8yw0feuVSTfJ7EG7c-K_whVB6kNrz7cZPHCpcpQEgUXIhHCR12Xs-ysbhiMMQ74ymsoYQfZ-zpNgemIiona4eufbJ0OaDJDhhEXEXkIrW790E_HMwZs9hZwUqQvkR4g46JezOIRw0sC-CCbIuB3ao6OejUrMnXIeC6QchZmMzggOv7znEKfaHrEM7XYqIRODanVB9gQTb5Z5bxGkjnpYCxUIdvhEkkPwtwwWID5rGqFDSIWD6bLyvyhd5JU-5JFByKbAVHxm2hAeWQcb8CtLNxSUElEZrBI0340cKq_P9lk2H2avEtmOQuJ3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو و دو تا از طرفداراش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81431" target="_blank">📅 19:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81430">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfEyjkPm1urDZKgY1_Jln6lP__iBBl6XT0mwuuD7aTcQCoYRHIoMKjWnpIGDSGJYp8L53rlW-Jcqng03pcNNkJc2c-o9rsi5Ix4aKJVCDqXKju_6xJejTzsXkf0PS-eHK5kEYhQbz32faYf-5ltcVL6S33ms9vRIpGbgK10ZbJStJk5tOuRKjZPf_UTwexxuS0QucdXuI6PkwvdWv22QFGtgNJW4pWOKDKjtabj1-VyMnD2421hr3lKZSFgiPJ1LbWt9e7yYB07X9qUchxX8UvdoDyyL1kz_Y5fkgISwXLz0_yEdqm0fETO-OFj_mI0PZwzKhASrvdJ5Fa3pxA9beQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل جدید لیگ جزیره
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81430" target="_blank">📅 19:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81429">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6Gu9xKR9loqJiEj6OClP7L198Ii-DkCvq5Sg2EbRGm70Cy8kr_MsuSirGIGbpc2p6zdcqwgGBmx8xXjAkHNP1J-aVndyJEdU_ADZalF4xRifMZhKQNt-MYRVFXl4cLMbd-FIvGPjDBx0Lzpxpj8-wYvUSjkYmFkW2zqntcVzCz3lPvxqmnHlsWIsQDlZHpewATEaLa9BbXChFc8c-XxqE7C9G9vzuy9sEkOdDHfLNWZ67mRY1FvKwTQ-j-wiMs8lsBfBGnT-e0lGEn1cVIvfL-ms5_xFGtr7JaBP5fijLwfgCSRztfsOJSB2CftoPMa5FVNcxr3SdQ1mbIYUBIPTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی بگم از طنز ماجرا کم میشه
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81429" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81428">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81428" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81427">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81427" target="_blank">📅 17:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81426">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">به گفته ایران اینترنشنال,
قائم حسینی ، امیرحسین ملکی
و
علی دشتی
از معترضان پرونده‌ی میدان علیخانی اصفهان، به زودی قراره اعدام بشند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81426" target="_blank">📅 17:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81425">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81425" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81424">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jo52f42UbqCVV5kMv3p-vel4xW3f7EfpeMs_maXCtF5qmb8imrs_pDCstLPc2rMitc1rerz2N5Im_PunEZHQQCCFaQEg1fxhSLYc-S2dVSW9UpTdSSSw-ObJAHclYYmUeJT4cU0b86CkiVE4au9IVu_MQsu0vrdL1j5EEWO3GppEDvw4FQnQqbbCh8Dm-gQVjaPcaIeWfvV7tH21jBJod0VPdbBzFWDFK7hDqGS_JceKBtLiPGe9po6OLjCBAjdg23OVLMZqxx3mFOlhFLbw3Ezx5kSE9GNCCH6wNOs3IMV9oKYUUmsb-85ePMV7-i8YfFbn__LAP_goGvNFWc_iZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو خود سایت کارزار، کارزار را انداختن برا بسته شدن کارزار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81424" target="_blank">📅 15:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81423">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اینطوری که روز به روز اطلاعات جدید تری نسبت به زیرساختایی که از ایران زدن و زیرساختایی که از عربا خورده میاد، فکر کنم آمریکا رو فقط در جبهه کری خونی با AI شکست دادیم که اونم ترامپ اشتراک طلایی گرفته داره همونم ازمون میگیره</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81423" target="_blank">📅 14:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81422">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سخنگوی دولت: در طول جنگ ۴۰ روزه ۲۳۰ میلیون متر مکعب از ظرفیت تولید گاز خود را از دست دادیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81422" target="_blank">📅 13:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81421">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">از سر شب تا صبح ۱۰ ها موشک میخوره تو خاک کشور
اما به اندازه ۵ دقیقه اذان صبح کشته نمیده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81421" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81419">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/itetgVlE3lVGLTlO6oUCGmjP8z0QOKIwExTOkh5kRSobTUK1KQKy506Saf9Mm5ujLHMOp4reIC5PAP5TAUKgzIWbCF-Qm76a3bQ53JSzQ_lc1CFKpQgLEvth6MXtlX899kXftL7T-Ap-IGKbZ5-R0L-VMqLY21Mx04eJ_af8MCUeXJ4ZbMsD6bapUUWzoip_hSZ1CPxVIcX-4akEHBOrTdYrAwbqstqzPiZuCGdidYCOxYY77ULHavXNcPTg0VfKbXiuDIhpa2anlx1QoHT_fOrczsHV4zJiBDpyW6FY0ebw6YYF-5v-LbjifreCSY1p6BsUwVwLfMnB_eBGwHEewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFNWCnNFR0jJXVH2sTC0MLHUIaxqSLLog049YKL8_a3S9LA3vRqOhE2dnD7LD1zYiCnQU45jmM-CZW0zyoqsuyh4vGUNFATC_ffgK4xBACsZ_Mxpdy6pNdCZTR47DPPtHwy_2KLidIZOghuAyhIHEWoeDmp1AspW6U9ehbByhMym6zF5HO5YmF6xNTNYIYInh_leTjcIOwssr0NDWYXHrMnaZDymBmsE1ZjL400MWEAwaJJ8ElJu9DfQbBsGL8hmYaqG710Wb559QNbWycJIOy9py0BhHbvxyg7tYIxTam3MbKdA9r4S1hirU22K6K1dwnQCJcIBwdeMCl6GbURURw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی دیگه از پیش بینی های اکونومیست درست از اب دراومد.
زلنسکی با دوربین کنار یک کشتی ایرانی که داره کالا حمل میکنه، و یک پهپاد هم بالاسرشه
چند روز قبل اوکراین با پهپاد یک کشتی ایرانی حمله کرد.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81419" target="_blank">📅 13:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81417">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMTCR_fpghfr963kuCDR9YxWRgT4Ci-Hhd4uH-EcrN6_5cOVtJbHpXtboxC_ORIvMGKbtv9PRPpu89UBRIxrWFH2n9P8iQFw3L80XdqxL79HgmTOq3i6TAQACAePV3i_ibIRRnjO1HprpgiRsuwRAnZ_fIvOLEuvO2tqls9pQRIkmZ1pOBGzMjLWrwG31ijBQn9TTNWCcWTNgqXZ0IC0hYfB1kEq5ZNPUug7sGHrKqPRfmrklogSB26lSaYWFi5AOt0jvuLD3bU6QcDcnPvigiYbgtBQjn0DciAqyKZJu7GzEj9nPb81jlOadzMb780Sa0LWKUoRj2uBZC3koXt9xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f171036de.mp4?token=rQM3Ionhox7KF_SiPT5EmIQXxnZUBCSkKcz_LTdhvdPjmbMP7CpKWvMvWhMYhjZLXrZsuvFtsNh24UCBBCC-c2IT9za0DpYJkUV5TYzJd4NJrP0nqbLryXbEwr9ZXH1XHqe98ZqMX4oV2358Fh_Ns_4x-rTeK_mNdW_H3JFoaKSMdkvYi9uredO_FXimvN3gmYuNNhAAPOMn642wiAChVJ_xfWJOtmjviUcUn8tcUQoM36d4Y9mCiMPqa0beTL0xrKVHeX3jhcUd35keb5nOgCUwKBIepHxTR3hR3iQ3NMj4z-KD8_37lAY5z8CT3896U_sq6sDJTGd76vJiYBU9tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f171036de.mp4?token=rQM3Ionhox7KF_SiPT5EmIQXxnZUBCSkKcz_LTdhvdPjmbMP7CpKWvMvWhMYhjZLXrZsuvFtsNh24UCBBCC-c2IT9za0DpYJkUV5TYzJd4NJrP0nqbLryXbEwr9ZXH1XHqe98ZqMX4oV2358Fh_Ns_4x-rTeK_mNdW_H3JFoaKSMdkvYi9uredO_FXimvN3gmYuNNhAAPOMn642wiAChVJ_xfWJOtmjviUcUn8tcUQoM36d4Y9mCiMPqa0beTL0xrKVHeX3jhcUd35keb5nOgCUwKBIepHxTR3hR3iQ3NMj4z-KD8_37lAY5z8CT3896U_sq6sDJTGd76vJiYBU9tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طقه پوبون رو زدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81417" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81416">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXufi8wlRxYOFom9UsBxH7NH-uzarVhXr48x1ksrxK3gQX2UEQvv7X2U-oe84FMRsOy6p6PvkE4GR8REWjKmff38Y87oA-xoIFoRDR6CzgX9xZXxnNUZg-TEZ16s9FynXVm7sNLlqSfdD21K52w2zMmfCMfhSyVLvfzLFg5yNCQNG83tbKI74DghSZZg1Sa8kNKH-Q1N9spKkD48iWRHhZHkQSYv_yJlZmPrsxVM7XL7saoy2_p-gZgvuMtkosVqdSOhAi53PLyjA-HaLDQVsSlB4XbU8J1kVcdKBtWaqJqdsXseZS1wlEEGJ7bv3eaV8O0zWHvJ0guw0A3x6uQQYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81416" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81414">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=BZF6QYoDKXxy5zVfzaD0bF2bzw-oxVoQNehmOefdY5dO5z6BMNpuRkgPKh1pIkqTpCpdhWDfy5XpE4lQKyGbEao-aL0ka3IEFf77pq-b4zFOKkntxTrdRUxjs1FDmdZjpOiKuorC5X9W6NScGPU6ypefcviLHG3zNskC3BzAzeCYwNlubvwG-XjrktCwraVO5NacKE6Y8cuUiybB40IV579w2F4sfeSp9RGyW_jXJkGpXa587qXBifG9ZZ23W-jL9EHNh8xeBQvZEy0c_GtBb2qAqXCrMWR5tEY53gIDEAozWnpKzHsXQjIme2Ryebgr_A3j0Wv-ppDmkytcFTcsbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=BZF6QYoDKXxy5zVfzaD0bF2bzw-oxVoQNehmOefdY5dO5z6BMNpuRkgPKh1pIkqTpCpdhWDfy5XpE4lQKyGbEao-aL0ka3IEFf77pq-b4zFOKkntxTrdRUxjs1FDmdZjpOiKuorC5X9W6NScGPU6ypefcviLHG3zNskC3BzAzeCYwNlubvwG-XjrktCwraVO5NacKE6Y8cuUiybB40IV579w2F4sfeSp9RGyW_jXJkGpXa587qXBifG9ZZ23W-jL9EHNh8xeBQvZEy0c_GtBb2qAqXCrMWR5tEY53gIDEAozWnpKzHsXQjIme2Ryebgr_A3j0Wv-ppDmkytcFTcsbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی گرامی کار قبلیت چی بوده؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81414" target="_blank">📅 11:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81413">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مگه نمیگفتن هر زمستونی یه بهاری داره هر شبی یه روزی، خارتو گاییدم چرا تموم نمیشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81413" target="_blank">📅 10:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81412">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLblMf6lmOWv_QsKz3C0dunsh31UlYgmIROiTHFUfDAnhvE8hUWlnxu_YWircgPni0CZSPHEVa8q66bFmAFiOtY5dK9Vb6fvHtq39fXccuebUpLsY0TUiqWtjlqVREt5omZTf1cC-WRQKpe66tLUm2fhjSJcfqJzN8rE1SeeQI8emclyYsTUQmj2en8_LWeq4DOXjshBvBPaQt6vHwjopeT0KANtQRgE44FMWL_D1wlgsZMdQfbe98Rmi_ongwS7z9OglTrdxPchsHh6Mwitru3d6cv0Lhm7xo8yHER4wMI9dSUUW4eyfYzSP0--12dcPIW1oWMdfNiY04soOc7eHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81412" target="_blank">📅 10:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81411">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تروخدا فرزاد قدیمی رو قاطی زیرزمینیا نکنید، فرزاد اونقدرا هم کیری نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81411" target="_blank">📅 08:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81410">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خبرگزاری فارس:  هر سه نفر اعدام شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/funhiphop/81410" target="_blank">📅 05:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81409">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خبرگزاری فارس:
هر سه نفر اعدام شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/funhiphop/81409" target="_blank">📅 05:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81407">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">از میدون صدای الله اکبر میاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/funhiphop/81407" target="_blank">📅 05:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81401">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">درگیری گسترش پیدا کرده میگن با ساچمه چن نفرو زخمی کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/funhiphop/81401" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81400">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اقا یسری گزارشایی رسیده که مثکه مردم و نیروها درگیر شدن و فعلا بچه ها اعدام نشدن
تایید و تکذیب نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/funhiphop/81400" target="_blank">📅 04:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81399">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مخم کار نمیکنه نمیدونم چی بنویسم
فقط میتونم بگم تسلیت به خونواده داغدار و ایران عزیز
شبتون خوش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/81399" target="_blank">📅 03:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81398">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AssCTGld9PlhwKFRmgAbyaZeM6qrV6mKw9ajJDY7wpq6YAWUe4S4NYMi0zOKalTjIx8bevVMgYzji9xJl3sUIaU4HM6XnoRsZ-bJmT9efpompmIkvj2xe8miMfzvRXMvi2uHW-Ok6zgT8-hrg1R0sx_hhmo_qnUE-T0eaXEO-Ij4WOjMDAKfhXKWmuGeOPsZkTdz92sXmWUWI5EzLs9NCPyWUCeVA9KuoqAXRlM4-tmLEmZ7aFrHrlDax7TsMwprld8BApNL6mLLKBQHJr6uiNC9bemBTHXspACln0jcHawa_wc23QjhZS6XrPNcy-xTdEfWHcSRW7k6RV0E_24T4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپشنی به ذهنم نرسید کسمادرت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/81398" target="_blank">📅 03:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81397">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اذانو زدن
🖤
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81397" target="_blank">📅 03:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81396">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlS9xqErw8gFaO1VSBSesPedHK4WBxlIpmdTc5Fb4APDpi25QmdUgVIm2i3k9b0VXbVaKnbIef3mKsntw3lRYkyrPTQs9C0F_KftOBC2PkqPxxmyX7gDQdQu2rige1djTmL9Y0cjdqUeqm4QWOXrt7Vevfdu0q7ujjOiAVVtUvKvC3OsZs4lxAZ9cMK1lprW_wegBw9rpFHmGhVJiuNZmL7dQLD2wGsDkM_Ryw7CZmthGJLg-cO3g4fwTyqAnhopC80Nkyzb28OwAcWU_zlv5IaD92QH7BgjmGevEFGJc0Nofe3mrBwQgVYCko17yai8u6-qc7P_7WoYp2jMZ0s3Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/81396" target="_blank">📅 03:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81395">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اذان صبح امروز اصفهان ساعت ۰۳:۴۲ به افق محلی است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81395" target="_blank">📅 03:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81392">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e358934688.mp4?token=tWf-vtXyiWFov3LQu6EuSF5341CXJsFS1cu44HKC0kOUCqupeQ-QEhvojz8NPRuUd88rMUul83_65lSebrg8oHIUGE33c_ua7SJgnAIigUvbiwQg9hKtUJcJ5td-5qvSb7IdJRtH9KEhEXB29I3w3VM12jsweIkIz16fxAQjYuE8wI1R9TIOwkCLfMCBe36cgsMmdNoZN2xidOKZjGNSVjNDcBsXCTIXaLWLLCqOE8bzifk9qpvA0ndkrWH0WAS9Xpp0dY08XAfkcEn8PLW9o4j4s4l9FEdGQFQeYRZd4x0cBeQEtQY4P7_m00WPrf07zLrm5OPaQu4sQSNF-ooPTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e358934688.mp4?token=tWf-vtXyiWFov3LQu6EuSF5341CXJsFS1cu44HKC0kOUCqupeQ-QEhvojz8NPRuUd88rMUul83_65lSebrg8oHIUGE33c_ua7SJgnAIigUvbiwQg9hKtUJcJ5td-5qvSb7IdJRtH9KEhEXB29I3w3VM12jsweIkIz16fxAQjYuE8wI1R9TIOwkCLfMCBe36cgsMmdNoZN2xidOKZjGNSVjNDcBsXCTIXaLWLLCqOE8bzifk9qpvA0ndkrWH0WAS9Xpp0dY08XAfkcEn8PLW9o4j4s4l9FEdGQFQeYRZd4x0cBeQEtQY4P7_m00WPrf07zLrm5OPaQu4sQSNF-ooPTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81392" target="_blank">📅 03:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81390">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">معترضین بازداشت شده با اسکورت شدید مامورین برای اجرای حکم وارد میدان علیخانی شدند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81390" target="_blank">📅 02:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81389">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81389" target="_blank">📅 02:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81388">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biCXRu9M7SvQaCUlKwp8a_Ghpga7PFzMt0B2m3xgWbsYFfTKlOjj_Wh63PTnsNheok_k0xHx2TkA8Prq-f73N8PuAzw5uH3MHT2-WpdHwUBPdNkX-6KPhPMjsNpluF9mjCbjsUWR3e3iWES-LKRy7OiHsInvIxiWfD1yHA56egHOEV1FXBbJc8aupXndFx6NL8yEmS-hISbPmJ3oqMmJPSll4Enld7HYutn-KFhPIo1ckSmCg01cFxUedZE0HctADxS5unHrey4FwEnGaGprr9GP4qM6HjRaGHKpR7Xe6pFTIqnZBvNJpIadpUHyg6baJEd6dL-xbw_h6CL02jjGKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این لیست کامل ۱۲ نفر از بچه های معترض اصفهان هست که ۳ نفرشون قراره در ملأ عام اعدام بشند
۲ نفرشون هم در تاریخ ۲۸ تیر اعدام شدند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81388" target="_blank">📅 01:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81387">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5qYlgpYivUZq2ZvuOR53UmbYTSn0WMOn5AM4N3XzXpc0DNwWQ_ekxUtEQxVIv4UJX-qN-JMuyAzywNrgO0GzyvpJwkg-Akc6puZmNOHmSTupipEeotMr2zExmamoktK9goGqgWLtwoSR_Ynk7EVIyOftnUljkNJ5XKGSbMSw35F4gr04EK4rDLri7Cm9Kdj746kd7felGqlhnx1rlZrYTh1QYJIDKXtAoi2EwMFOW5CYFdwbvl-JtPD_2L-inswDFbfClrLV9AON9ja8a3hhvlut3CHEMy8rbOikiLsJJQ_obd17JsPDuw_hngZFSzrMx7hB4uIWO9rZAlUvzD_AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بنرو تو میدون گذاشتن.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81387" target="_blank">📅 01:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81386">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81386" target="_blank">📅 01:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81385">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ps72fOtWY7qPtsh5Dm4VWqaFEp1ohN7POqcapciWrm3V_k2aNuAV3F-9V57rdBGJ2FVqroEEDDnRsfZrx49wq9ltZkqhdWJX2N1HJ8lYbXWtGhSroI_EWtdMJQzoyDIZaaaDX3prfq-caykuByssa_g_D76I_-PSowipGhMwU2Ld_eUevcwGjdr-paQtsvxusvCOb9NFRrJYlkR-NlozxcqhUNcOXf0zOt6avF1dimMJ_J3GJspzjlgQ-I0Tq4qdQMowFiHZfY8OWsgpF0oPolBjfrPHPDVqisSYrW1b93_MPqoJqajtNKAwCyDJ141kpaUjKQTKuxevqMipHk-06Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81385" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81384">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">از این ادمینمون فریب که شاتای پستاش تو جنگ ۱۲ روزه تو کامنتاس از ۱۸ دی خبر نداریم  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81384" target="_blank">📅 00:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81383">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dhf_PM4ur3DHBCDKcFkofPQaVB9FMzMU2pwc21tS6D-QtskDbI8ZjYGQx2kPzgXOpXM5mhbuWXmCfSMi4OAvP5ywS15sz8rsaI3h0nas9PbvUFgHb-F1AMmV6kyfMkanBi8GnyLHlT_R7vCuIWJeNLvoLyF4GvW7JW3-u6RIukyG3YoxhJQPPVWZeQyRQ7J4KvVHPhSWPkRWJUoj7V-kY_0kRUYj5BIho-HBoHg7o6H9ksaw6p9SdnYSX2F-zFMkSpMiUPVSG-qWR0ALwXgxARZAdSbyNp--HTungd06dXhoJVfyrJ7q_wTiDaL-oIdmdmB7JNi9YBD4T_iajt_a-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی این دوس دختر علی سورناس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81383" target="_blank">📅 00:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81382">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-f_ElZdKLObg81tLeEQVYHsF_km_PcYY3Xo7uBvjoZFA1Z5B8pL8lFzXPjFuuaJevWLxNopOT97rQO2GwsLSfWmMbevNeXEF4znrR26ENAfVAWdofsF_iqt9yEyk6dixLmO6PymVNAOu__lc8EH3FC_ACtGAJQ3CpVipCPlz0GHwHw4DASRiSdfzNOIoSqf8L8gJq2rxiKkFtfZxaMr9AB3NfLTowjrU89oO7RLrnwJIBByf4uZlvmHNirkos2dkhsYcadPvVpduB7Gev3oTwo_g3T802GqpFIe0qy-F7-AxmK91NuQOq2Nkip02VrH_vvknC1f8-APjyOggUg5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری، از معترضین دی ماه در اصفهان، متاسفانه فردا قراره در ملأ عام اجرا شه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81382" target="_blank">📅 00:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81381">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRbxVUzcJO38eQ4o4Xjx-pGfZjRV7nECnSRA53m0JBAPxcM_d2E7S1d7AZoGG6wWSwM__LF-M0eeAWT5PIQIjUJuKBIZWjX2CRw7sVy-btteTevsJ8UIvFsInqTT85i8I_QH6R9nU6QijjKZBqQVi1Cw-fU7A4pgSi8k-gbKvA9oWX8jjEk58iDibMfi5oerCXDDZMN4wgTTbEb95TDRR24mGzeR1fHwMlbbhggQWuOp_yRhCYyQCamqJG6N-KhgZjWLGzowd8aRgdDuu7dW2XT9eoL429UoCwGKn6jBFjs6nfbqUdhfrf_ar0ce33IHh5FY1p6P8QtVHPoBWUR1fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81381" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81380">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoBd4yfP-elQf7AOV-g8vguZ9WNz8qsEfa8Hd_tx9bWLw8hyC-Xg2Zw6Uh5wskmfeCWgX1aKTSvV8vn9AmS51fTljx7yNgegqvPfNniyYCQdCFkpTYmPTIpr2YCcaKsdfBCeOD66oGS8owmkd-nRyc1EBYS2eA9XFNaupwxRqZBlZVueagzyTRXpAAPNWi624pfsghI2cHCf8NZRNm3YyYi_1inOCUX3Ym1XEL3V67-9ir4SUcxzNiNDy-THY5d2blF7_Qd-oAkw0mvSIbPbaZcc4AkQArff0CNiTlZitdPGOiyZXRRommZUytIoPsvrMxjmnhrpjWvEPCHyiN4P0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراد ویسی بالا باش داداش کلی تحلیلِ نکرده داریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81380" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81379">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJj-uBieJI_8v1xfxuMp_ZxtyTUf6rVC2tBE2pduSFSySCt6R9EpZMThZFeSpkcZCalDGLlzFS8ePXC2PWv7rw8AF0Dbrw_VBVcnyoHeMd8AjtV5qaaDvWwyXxy6WNam02oDPwYhLyqR6y-Qk63gy7urZli9fAFkwBf2HKBpzO0o9wDTtWirThut93MexbQQ9FVi89Osfv9G9KSmSvA_-4eGPqUhv0FwM2Mv0gnhfqqqjOHNFYHYQWLgw6bT-Cz8E9NGQeASj58eZ-KZvhxxGlIvcvRPMikRFpZCAXG2lglkJ_8-4QF-ZE7v5yMmI0WaM0eOSKajVvweUApBalDwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید فرزاد قدیمی به نام زل منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81379" target="_blank">📅 22:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81378">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81378" target="_blank">📅 21:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81377">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsnADoZ0SXupj6-MRwhSqROjRLmrGn5dX9ParqU0MpPlwX3I4lNna__FbpMGdYfn6r5RvqBY5ZK1HBdh_SJF-3Uh1HLaWCf8zadXgfnfJtVAsecD3c_NezO5tIwircSEVyqb5GNG2gQSfnP8JepgbeaJzw6sewIZ4egtUrps96kj2Qh_GcqFndiYqGj7UpFuHbFVVADCF40ugwPHsptapFjV1nmrlompceGh7dUA7hGqB6RzE-GmkB-8O0cv8Nhw7pSB-ULq7jQJdVBRkuczyLS8MLdzLq6SZ42fgaaY1rE_NTLxRcLvs1qpT252g-VTvUI0CLj51MWGMMKgS91tZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکا وقتی غیرتی میشن:
Gay rat
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81377" target="_blank">📅 21:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81376">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9IU3AxJQ6ZYEeX7u2-LWwKeCAb7U6SKCmml1ZXwog7DWa-aw_MnqQrecSOKq2JSVEiE0LElncEENPVQc0vUM6grn5SwfsY4M6Uh5Hnbj5sLq0hwXwr3YjUHFxmd3rhjHeMx4L0pDSKxehN5o1ArBUyTxHStdgLhRKw_IMk_Wp2s6GM1J2p8XBSrjeUsg2sC0IkKGrTEcxfZn_2xTppH9HTdNIlWc_IMPac1ZEz8wTyLQL6VCueM9ACv0JvvsMiWzKcsNVrxBy2hGn-Ya7u0CsL2SYtNfm2HJwoPi7Fttz_qtVDSXiUSquLz3UBqb_GTFfdQ-KwXx5CZQIKwU0_wAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81376" target="_blank">📅 21:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81375">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MS82rqpHASfxB6l94xCubBDvsp4bMZ53NS-fFIDkJMUDLWJL2WJ97DVcxROghKGn2pEl1Rso0nM077d0DMihgE3qIveRX3EwI7JRzgqRC5RFhr5eZMTetZmcleCp2I3TxFwKLhFXLAFWf2cyrLCSHrf3SexhTRYVr2FKNPr6IeDJKRZ3w9rozFjU8ftCn36aJbQ643GS8rMfbzJUz0uem6AZzHqOlIvd9n0iJ2Fqnyr5JPoaeLLHq0nkEPAn9QxSruhROw46Rg0HuRyNL1zmf2xde7tbhukj3UL6psNDPjn1kMq7b0UTGO5mFZPtq9qcwBMoEJI4ciCgdFDqB9mS2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81375" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81374">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KoHFhOer8MtNEsEtiZecOh5EHKc6qqMg9PsI5yXG30l5xZReuKtU-r78BZa1zVTAsLp6L62AqSXqby2q0X-nfv4SDJaD2Nhojm8SeJ8eIB-wVsfIO8FjVH6DGQYh_XTvbg-RgU90r3HKHCu4y5tEBTPS8vm6W9uQk5zAfVUH41_NLfoHCuj_FkhpO-sRZIdZPvcOG8sE8PF2FrUldiQ94byGhPzCXbIju6yn1aAotr_xE1KgixNKsmOfSbCdBYDVzNkm8ZfjT72IScGciGw6FmdmjxEjHg6VITb_Zk_zi8hHAcoLDtX__X0Nekv8RRZnjGoqwYHGJPwJKtS5Ywd3iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81374" target="_blank">📅 20:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81373">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2mPWmmhYz7zXMePFhzFmQ-d-1QBqsaX5a5pu-TzDsfr7dTaiuf9J8TCJ00FOOG0e8MrcOqntt0qNHK6vaTlQQUmu2ZgI9AtwkLL-ZnqfLU_EOBbul3X7GMxVMkDWTDQXfVcpYtYGAa6yBozJn-UL39mvsC6gCltc9dzufXQZB8UujyBb0MCQHwABS9PswthwobxPlT8hqNv8NFJOTxnTcu8WPQFgfyPV7NAGC2t3JOvLrij06ma211-RCiLfe8QWGFYbTGbamUCdKJCnaiP5CU65vKwMuQdqmdJ8T6PaokmnbRLjn4-jvk0mBL8DyqIRHj0QxvV4Vb7ht6ZqYAxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام پسر
خلاصه‌ی مصاحبه‌ی جدید ترامپ تو هواپیما که همین الان پخش شده
عجب حرفایی زده کولاک کرده این بشر
👏🏿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81373" target="_blank">📅 20:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81372">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DN7Tqg5pRfdKM4wh3BakhbI0179uq8EhHnAfD96_TlTGnCgmBLfxNhmrtMy_AVukQElhQObNE6Mft111I3kUmbIjek_8lAvbEWJXETiziVXZFZua2gZalOvN5AeSARgcenHedTyFNrT-ipuRt2sSEf2TcO6qpy7-aZVRLnMdeSobtRjvo6sSK4q_B1SDDKmiEnGbShql_w1M87LEJymrpO8hm9uBaqtgGTdYQFmhRqLGZLMxksnDwBFROSSlmzlkLMnJzxdfLpWhOaQQ30_1FnQf5fosRr0mqJrxwLEuyTNFDfyUFhxZ29oT_n9jQsvh-Pvj5O66KR7R3oDOHau3DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81372" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81371">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN2plMLqRuj0zJ0WKcv7Ay-pl6d81VMfsi-SvclVxvBx_ooq3PJfQyvPn4aDfxDnc6uWAdoHVRSzVRO4oOcTTiJIw9f9esT_y3IX60ZViprT-ylymPCO-Y7vdxoQ7WGGoCoRlEPCyYQH8F9cwJSRmW2iBVcWaXddGDXv1VrSGuNA5WeQzyk1gCcWQsCC9EZGYJ6HhJMHw-5bNCz1H-Mk8ywIIwOx1JudFzzTebo7isQBrM9yEecRp4wTgKeplyndqFUCYwu33zIFECj21rgIr1pwezJOFzYQFuTDXmekHK48PQ4TbjVeppYydcg60dCEJtxv8zvnFkb7HjVWPlrNEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROfywAcTVRGoTsMhBbqk5MXAjuq7OPOcfni3Uu3uwB5wDxt_GDpjs0wYg511d_e7XYZEaYsZClVYzLOkkHqf6qXWMLzHNSQqncP74Y74WCmtatVh-PaoQrsMBR7wkwKthjMe5RtIxcJCyn7BQS3xQ40KPZMj6uK2gR-_wbLBpskKY-8vs8qtKU3W-RRlWEUg37sj2tOVLZpx7tYq6h10UfQD5jg48KmqlGSqImMRBDnebhLg9deb28TFrjPHKau6nDfUFL0YkXLjXx47fnF0W9zhWf1XV4PZEKDukBHy3AgBcxse1j0UqCKH-Sx8S9WogY4-6Q7___DxlWPZamZZAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oYg6RhKgBiyOtnWan_Sdy-O6xx_YvXykeVXflQ7R5VkOwZlvHj0CJ2OcvMfoWx_5FV1vOUglaFb9vew9iLMrNEEzIfvxOO0kWGk7StSyaGi8HlN00_cGfDcTu9vhehmqnQtYF4YfDBG33qMCVKUrRSjrRl5HU-eocMrKw8mPREBWL7XgKJ6kChn2zsJnRddH12v9OeYudUArwQjfrwlqE1U_8o2Sz8Vvgb_fpoNUFpUZcRsYeHuBGiTKsGEWN-uJgcYyk1xDan1p4SLi_YaLnYAm4xW89gT6Xw416z2KW-p-aRQVlXASyWcT8JiNrqFjsPaRE3OXi29GGrVeYvfEGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رومرو درحال رقابت با صدفه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81368" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
