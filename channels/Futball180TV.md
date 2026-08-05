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
<img src="https://cdn5.telesco.pe/file/iTBzodE_UCx794G3vGbEbUCKZIZSVFLA0j0AHhZq8l4mOts-zDCa-Qq1pMB_hKWwAmIswISzzkha4X57htRvf3lyytkH4UgnZQDXkDEml35A9JrfHtem5bM5vIX33sAw67DSHSO1CHlXCxC0Y-JSTVmThfvC5O8G5gjRgc__W_iDL1irWry24y7L6va47caScFBjUnoX4sGnsP228kTK7P5AlCrbT5uqgF7MNgiZR9AHdMLtzo1F4U5ByUG1hSZVHJMRMy8kdv0QFy7l6NzxLuKkIOhIkVFbQHO-r_QvZs321DES5hX0dxPSfrpUHT1kcOvPTYBMr0m_67uD13Tq1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 493K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 23:32:41</div>
<hr>

<div class="tg-post" id="msg-102812">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7IA22RfNJOdhtpFD2zNaO8eeS8dUSaWzZxwGB2IsEcrk0WAVocj88pdybalg5RNNqNaygjG-Yg9qEWYrtQ47bUfj4nZumJmJKB9s5f74RUp2l4UoghrnihU82xXYW0lyCIxuUz9fuaik9EzkfQdCfTdUiASA391nGDnpkMYWo9pSVikcFRi59ogOiIUEPCwG850gJRBznwtPtpLRJNlZhI8g6ZSGhPGF1fDLhd_0hOJw-i7q753BCJh3u4TVin0ck9YUz4Ms1PLVdRtFNjHruIYVytpvAwNaA1Qpvc5CBWzbKXzfMHXxg4NpJ7w_gcRECoLTR2fDRTzKrovcQE86A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتیجه تلاش و پشتکار:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/102812" target="_blank">📅 23:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102811">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv_EMleGhaJ2Zv9h_eVbxIYkd8XjiZaNp2BWzkpbGJvHWWy4RkpF7BKI5rbe31EMNj2m91KHXMKEk6kC8I1GhqWuD1WTrPW6Guoj-VqRWlcQwzQjvPJ6mp7PsAmJ224VmN6A6-2RsW7nwM4SD29TKHMgWaoJHgyPehoLBmEg6S_wb7-66kPmERnhDma15eqL3l7Y25oWk73zDTtsgP4P35X4nYx8yp3306vbwUm0C00Em8VjD0XOIjIT6un_ISS8YAjIcAPQ2AsYXyKWbjnd_pJBBX9fjXfvpObXv7NSs8dQTo_gXAZRPHiOjl9SZ2IeGJMtZqh43-OgJb5L7sAXAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد صلاح:
من سخت تلاش میکنم تا در لیگ و در اروپا به موفقیت برسیم، چون من تو هر تیمی که بازی کردم، موفق بودم و همیشه یک بازیکن فوق العاده بودم، و این چیزیه که باید اینجا انجام بدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/Futball180TV/102811" target="_blank">📅 23:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102810">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Esgard-VPN.apk</div>
  <div class="tg-doc-extra">42.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/102810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پیشنهاد_ویژه
فیلترشکن محبوب اسگارد ‌وی‌پی‌ان
تقریبا با همه‌ی اینترنت‌ها کیفیت اتصال و سرعت خوبی داره. حتما امتحانش کنید
لینک گوگل پلی:
https://play.google.com/store/apps/details?id=com.vpn.esgard&referrer=628035</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/Futball180TV/102810" target="_blank">📅 23:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102807">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBjFr2_xlhuzRNGSgSgr3Zrw1PDrC_VXjRQTDUUzgdPmeWxvpqIDqhV87ghuWaLGAYzGeGl9lh665cdBZHvf4OVbaVJJui1R56gSY19UPCZNtvwqJVil2Yy_91RjrytO7vPSnicUppHqT6nn-Q6JMaWM8ntLr5_AoJYIgWbG2vcY9I0mNw_HPqu317tKYrCCUaDBROwGPCBfmVhIRZ71lqGL6er3UAfG4wgYHW04o9o9xLwem2Ig9Cap3z4L937ASukOKJbfT0IF9rDkYR8tBDkt4bF2OwGFHhHffbltbrThjt_rjmr_TtnuYjPdnIL0JkL4nHFPBgdJc6byYemE4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TyqG0Ck4kebPut_1y8BvvxNZHucv93uJZS-Tlm1vO1b5UBmnHHnE6o_pXORQnabEYBKTnDtYtu3Qm4GxNrZskAbcLDeWjqC9nDL3D5xj1xzEELJ9XRqpwMvsxUlnnoZvCCSHR70tgyg5Xn8aKtEmAAXQ2McXThHQWCPd9JdikAbjIEBsCt7Tr6De0QCuxP1fXjOuXGY3flyQ5Wlr247-KlGpsFrgGSq8oja0764uNSeMKV57v0eJyHeCgNv_WDKQR6yLn6TE-Jhygp6gYuMhLLu0vH1JXQie6yoLTMEOi4qoYGqfNV_ebpyc6jkzfOQWIfSN02agTp_JSoRckOXRbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1r5df2mFjtcu21w5na4Pail4dL-zjaAMPn7-1KMgMLpJ_-ocju-WGhhB6rznZRA6cErFTrWrHoNKOuAugbQ7jbDcI75QhejzOWmFUM8wpAhWy1CbvKUv711siHjDRM3dv9igbmSYif66sRXTD2mY_3BxYAweP1Bbql3jy92FxEOY-B5CdWKDwNvBevHemIebN1NKR7AhR9i5Mq27NSGsF9ZIV5-MJgZYBcMpZGbBiXAPzjMcDv8sTbjLQNbohjL0l1Il8j-462pfx8AZ_AS5fS2DH5iQqclnr6ZTI50PJKtdZznN0dsHaGIZADKG9OyJ95QrzKTuWdJPkamnudq9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استقبال برگ ریزون هوادارای ترابزون از صلاح رو ببیند و کیف کنید.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/Futball180TV/102807" target="_blank">📅 22:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102806">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8Bhwn9TnJAekqhs3KIyD8P1DNe7X22UcQDbgtC-JiwsaMsXADYzDA9rUwqy3VlT1MrPGbtULr1Wr_YHW4LyUq-ZRiBcaxv1_GGadQI9-C5kQzMPMNCfWUcrHsuThPMwr4OqyoShxczAn4cU9H3PXsrhxXHJXV2t87MXiv47cdxIvKgL4WyhwLLy0kgOTu0vnscrStpznTeULU-9BdBrh4WQ3l_rHIgNz1xTlP7jANEddIzVeoAVkCBAdB3xaLw_LQ3xywGzPcTtuWlBsv0N1_4OXAIQtsyHb0mv3UxaIdo_BAh2iNidZIGACN5bmGDbBh5kMuIGO8z93oroidcfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
‼️
وینیسیوس در اقدامی ایرانی طور تمامی پست‌های صفحه اینستاگرام خودش رو حذف کرد و عکس پروفایلش رو هم برداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/102806" target="_blank">📅 22:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102805">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvHirn6fUa7Y_wJyv1gGcRh8av2JKBn_MIsnUlQtU8oxncF8s2U4O8yV4PHEqt0sUkYk13U46BG5j4TAXCtFi602dkiEgeiz2vuE88dm4-vo7LZSGYLbEtWdUmHwrJhvIfitr8VR3AxPj8UHMp-pTCzsCHiq3_Ea4N7G4zZnDatQ77I6H7Cj1WuNQKjffO06E3Z6sSDs3A5IEoHbNGfn651q_hbAmtr-wMJ3MnNBm23R3ZbRDfLuhN0Nn0MqS6kTjrHogDgJ-OK2Mn1Ef4KXaPvA2BojUJ9vERxbAvIeHE49yG5SUF4J7B3k8K-n8qxHKWmxxHgLi96gmSClJmVfzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
رومانو: ژوزه‌مورینیو شخصا در پرونده تمدید قرارداد وینیسیوس جونیور وارد عمل شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/102805" target="_blank">📅 21:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102804">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETCNBPUc-WD5DG1hU8mdFnqqFss5MzjbSxibxWVMbiZTDA_A9i9tJJ0p1mLGD_bOy1IHDd4qknEK9WeYfO8t1EHJIQS4WWu-tku2oBcUQrGbY9hWYWno_REAueYSDp0i8R6tNaxjXkxPBQOWrz_JSLkrtNnwJZs3UpbUYWWGwYHW7jqjhTXB8HkLxnHFvGBdavJ31WsQnbvjDPSd9UXtjdNg1T9w_8xH2a_rEZA8ho1_4wJJ_1q3X8dXd8_MZWfX1FLRUFKrvlwUPrELSE3kIwltwQ_b8F3azhg-abBBLQgI5YHwJpzKaN-fl9lMJeAwVxUbDNhFwi56Rpe1t-Unmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
کوکوریا و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/102804" target="_blank">📅 20:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102803">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCduLpiQbvJRhW2eTS1-mxX2MzKQ73X6ZBEY2ZGQXJ0CkQsd4f5IRJBZnnzZSBU_Ae2NjDNfvibqR4Z_WT8ngmjw_Ju72PjXwf0dlDDDU23siGsr_q9dp9ChTFmiC8pa77jXt7wJoGQmzXnOD9rDzSo0Rx9mN6xfr6tixhVjnHlOimzXaWksJjy6HrYYZVayMcHarnFo3qM7tA4RQvNXw1tii18I4nSQI6PeXuLXMglI7_oj8AsIjuqbvQSsrDcdjePv37ILkwJh7AmHmNx9_Rcop_cUhKXgVdQZ1-P4k4LeK6w80_7Pk_xtTXPjwU_avA2KOTffG7SGEuWwhM9uwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
تاریخ
مرحله گروهی لیگ قهرمانان اروپا:
هفته اول: 8 تا 10 سپتامبر 2026
هفته دوم: 13/14 اکتبر 2026
هفته سوم: 20/21 اکتبر 2026
هفته چهارم: 3/4 نوامبر 2026
هفته پنجم: 24/25 نوامبر 2026
هفته ششم: 8/9 دسامبر 2026
هفته هفتم: 19/20 ژانویه 2027
هفته هشتم: 27 ژانویه 2027
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102803" target="_blank">📅 20:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102802">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/My7Tae5s9W3MhluxVUAra9BGYJC5m2g4hR1oUeHRQLTQ93MA7YqfFk0QAgpmduRDJuk89U1AaBVzmYeSKRysJ2yBkA0p4fcwM4Y-6WyeCRn1RdTFFzhFnY2WLH3jSuAGVptGYoYYzTYz1a1-9BXmD-fA9uhcTWZqHOMEUilHO9a0xJBwwJ45hjq8dBpnD2b8SdOjcwQm6cr0K6CLLpbRQjco98Kzh0U-zUxkFwJ2yo9KSTs5CAr9PzfD53M__2ySHqoV0Xa2DAW6kmxdCXF6CMvIgkIziVmprkOOYx7MCsC6DVD-Rk43srHxn8b0NRsJK-IKrX-fj5qY29u-_FgMjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🇲🇦
جیانی اینفانتینو به مراکش پیشنهاد داد که در صورت حمایت این کشور برای ابقای او به عنوان رئیس فدراسیون بین‌المللی فوتبال (فیفا)، میزبان فینال جام جهانی 2030 باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102802" target="_blank">📅 20:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102801">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e865a76e80.mp4?token=abFWD9rULuGBgl3KHQGvUR-aHwMagot2IbrsPKMI2fSRadO0Cj4n7SNBr0Kqx8kgmhnpxvUz9uHLq3Enrrf1CeinNTPr_n3ygEmZiKTGFeqqxeEtpHNIgeCvMY8bbfmkOTUEM6BaNdgPgRatfpEKQJQPG4QG3z53-pBvV3Ct2IgRES-ST7o37dkAGUTZZ8cXlBDZQxtv_eAxIkzqVi-Z3FyDJjtCK1S64Dvxn7HR1gwJVFQ18TZLU0nc2YpUGRypyJHN27mV9a9K1uSeQKbrpMJd_2ZXJEUwoggqr6TJRtjLRnyUO2iIuUcbyQW_1QYp6UmobAF-VBNBK1nDod7JYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e865a76e80.mp4?token=abFWD9rULuGBgl3KHQGvUR-aHwMagot2IbrsPKMI2fSRadO0Cj4n7SNBr0Kqx8kgmhnpxvUz9uHLq3Enrrf1CeinNTPr_n3ygEmZiKTGFeqqxeEtpHNIgeCvMY8bbfmkOTUEM6BaNdgPgRatfpEKQJQPG4QG3z53-pBvV3Ct2IgRES-ST7o37dkAGUTZZ8cXlBDZQxtv_eAxIkzqVi-Z3FyDJjtCK1S64Dvxn7HR1gwJVFQ18TZLU0nc2YpUGRypyJHN27mV9a9K1uSeQKbrpMJd_2ZXJEUwoggqr6TJRtjLRnyUO2iIuUcbyQW_1QYp6UmobAF-VBNBK1nDod7JYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">8/5/2021
💔
🇪🇸
🗓
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102801" target="_blank">📅 20:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102800">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn4MYVcUer6hFSA_1APDFjTYj_8Co2gpgkxmtLast69jAO7vYPTQ5EEDA8eoQ1b0cva6innlF6d4QH-M160-_idYf1GVuNOpNaKl0UBl175HCjgYl7jk2nCh2RQ0bl1-RnA48s7G1L3q0NuiFxqRV9dlQjKENplPfHc4j8VctFrsemEFGhk771YSvcAE9mtQ2ltKtcXqXO0nAdpg-p0VGrAjKnfgjTuFj42AKdPU_liG_GF5RXTrUSPSs_NjIoSGNPhtD04jOxQb0KQMwFZbqioS-0XL2Oab667foX5FIhcNrLvWu0UgIWf0ejc8JHu2H1cf4Bd-vCtwCZJkxl2hJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
استوری جدید رونالدو در حال صفا و آرامش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/102800" target="_blank">📅 19:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102799">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b7936557.mp4?token=d0tXlzlg626kMjmQr6NNks0AwX8mKn78H0XJJiRskiadlBcVh83LVQiYMrqa_sozVFKdS_hqZyUOPG4APlFwdM2GVzbE2EuAZtMZSAb3BFzKhFpkD7QiCY8CsEMnIAnHOlmVH8k6WIEHXnkQUQIirNk0JbDIGH59LCsVBCZumz7--K3-WPgMN9A0IaxESboz6BZYXC8me21EtrfDeOXUQSjLFFDEsk_jvy3fWem-IwHrjzqulpeTqly47Gt6zr6RCmEBQnVNuDdHrUtN03_AdVRYa9XyBDLTod6fFOzvY9ahMp0jhp9Dn3B8aID66bb1ZOLfAb1YeD45X4QAtxMNZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b7936557.mp4?token=d0tXlzlg626kMjmQr6NNks0AwX8mKn78H0XJJiRskiadlBcVh83LVQiYMrqa_sozVFKdS_hqZyUOPG4APlFwdM2GVzbE2EuAZtMZSAb3BFzKhFpkD7QiCY8CsEMnIAnHOlmVH8k6WIEHXnkQUQIirNk0JbDIGH59LCsVBCZumz7--K3-WPgMN9A0IaxESboz6BZYXC8me21EtrfDeOXUQSjLFFDEsk_jvy3fWem-IwHrjzqulpeTqly47Gt6zr6RCmEBQnVNuDdHrUtN03_AdVRYa9XyBDLTod6fFOzvY9ahMp0jhp9Dn3B8aID66bb1ZOLfAb1YeD45X4QAtxMNZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادمین صفحه رئال‌مادرید بازیکناشو اسکل کرده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102799" target="_blank">📅 19:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102798">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKLs9OnZx1-hGG0Gi9cWge_F7mLqLhDSH34ra37a0_6sc5jbz3U18ZzkxMHhROW3teYDg4ZlyDvydga-omGAMVN1_QIOCMCchrVNGlJRoeYsaF81G5aiYL0M-6dGG3IG95R-mOJL54yCNJYFAPZt8E11uATQMAdjtd83-yL3E-mFPg12gqgJfEP2_Nh_ACsxmeyL5OXg42OV7MYuwhkZ3iBnkUaMcS8BXYpt_4PZgo0c-a1B6RoxNxduRAEj2TnSfpp7VhvREVvCO4DiWmXTh-ZPLpOhmaZDvqR_J756q7pO7811mmcdAHzFwTKULLkjJlJvsPealLD8bIguhJSPUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🗞
با اعلام رومانو، مولینا مدافع راست اتلتیکومادرید راهی آا‌س‌رم شد
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102798" target="_blank">📅 19:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102797">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a21bec45c.mp4?token=I-c9M_mbZiz4l5ZXmATRig-FucPPXPxXK3xrcRXjeQBQwKa5sz09UWuXI2cyvgGJjI6T_wBrVh5Ya_C8S4QxzPmL9l0aPtT9AEYwpymfZ8cBoKs4_TpJuorTpqHUkSmvbajQpgPZ1mrEwWirS55Xj3bPE-_zUDQt6BlV1iaVlIX-vJ7l2OEjbg_N2QjSo4_puQU-qA-810Ri5txXivGphI2R2D18vwCumtKW4DSwTneBcHhuVgUEkpvVScK8iuXa2tkgZVAgMYXIvNtRw-UORGjorKWGbp7zDIRxXdQk_qA697Y6NmNkv2eAkQaIpeahMosjfxPzzRPtaySGEnDkAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a21bec45c.mp4?token=I-c9M_mbZiz4l5ZXmATRig-FucPPXPxXK3xrcRXjeQBQwKa5sz09UWuXI2cyvgGJjI6T_wBrVh5Ya_C8S4QxzPmL9l0aPtT9AEYwpymfZ8cBoKs4_TpJuorTpqHUkSmvbajQpgPZ1mrEwWirS55Xj3bPE-_zUDQt6BlV1iaVlIX-vJ7l2OEjbg_N2QjSo4_puQU-qA-810Ri5txXivGphI2R2D18vwCumtKW4DSwTneBcHhuVgUEkpvVScK8iuXa2tkgZVAgMYXIvNtRw-UORGjorKWGbp7zDIRxXdQk_qA697Y6NmNkv2eAkQaIpeahMosjfxPzzRPtaySGEnDkAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚠️
هشدار، ویدیو حاوی صحنه دلخراش می باشد: صاعقه یک بازیکن فوتبال را در حین مسابقه در تایلند کشت
❌
تلاش‌ها برای احیای او در زمین بی‌نتیجه ماند. به گزارش رسانه‌های محلی، ۱۲ نفر دیگر نیز مجروح شدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102797" target="_blank">📅 19:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102796">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sq00Y6IF7KhBN2VSulcgs4wYTapBmIo7CqNG6K-gYBNNfWTAjfQ5jEgRNbcHudWa6mdZvnZemrEa5QHU8MZXpw9wm-GtzculHX8eB6NLwqtrhIaeDPDLaG-PJyRg08HhxeYa2j2NvQB797GtO2R2XI8gXlMqG4mAQRw6b8C6z3JBi6Q2sMD1QWPGc9dY0l3ZFP8borr1RiwmKJ56dmJ0iQlEufdfprR5r3gz28bxzJ3HBOcv24no9cLKOgQFzesMvgrov36TlEWpMPLPhN5WWpV33rk7vnhPW9PoR_DZnjClB-rCoavz87VhXJQdzkv2J2xkmgoTHRVxlGCOcJp0ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
💥
جزئیات انتقال دیومانده از لایپزیگ به رئال‌مادرید به نقل از فلوریان پلتنبرگ:
🥶
مبلغ اصلی ۱۲۵ میلیون یورو
🫣
مبلغ اصلی با آپشن حدود ۱۳۵ میلیون یورو
✅
۵ درصد از حق فروش به لگانس‌اسپانیا تعلق داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102796" target="_blank">📅 19:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102795">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFYs7hntxT2LOPMUDH7MTtMnW-XjzmGtIx3v3p6Ql7VTx3QZMAkghtaNjGpGcXIWe2uM_HsIRmTXPOziq-J0NjRKoPWNFAf4SN7NzmWIkRC2sqgQsej_Adi3nVysntEPhdAtTHpkxI7iNMuZDRYxxdt_zKLWi0VPWcrYi30T0mdSzYZSDE38csxaArFcVZk4ghB4QNI4Np6qy5SVJvY0ZEvAWyy16fFnBlVdmX9sPLwRiAHJY-D6lIRfivqd78LQC__5Ro0uLZahAAVvju_u2KagYbmVSYYz_Lc5CvI-pX0hDFn71JafPeV_FaV4wYsAtEdWtkBI5SnR3Id3DW0RZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
#فوووووری
از اسکای‌اسپورت: وینیسیوس جونیور پس از مذاکرات امروز با رئال‌مادرید شانس بسیار زیادی برای تمدید قراردادش دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102795" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102794">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/833c1a2554.mp4?token=CVGPqgRGiz66P2WQcD6g8I9CyGBB1o0rXQ5dVn0sC_8x55BtfLCyicDdRM_jypx8tlLyTYzM9Ck6-aIg_urFzjMv86XKqot-7EOGyPHdGVcXoFLIZmu3GBRWd5BUeb3x5xMcDjr4Y24ublMTRv8Am6jXTIF-UmU0O10YpgVnFOikqOr2Ubs5bNWaPFFA166onUTcCK16xfj2D734SytKiiCG_jf1cjT0vZ-XAinPFso0drECoWNiyye1G33Lw5N6VbHX2p1iStqIZqRGT0qA8UPm7DW9-_aht_K4BxvPuoItD68AGeHXFfEc_Zztka9fBnpIWLZy1XYJrW4k9c1idQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/833c1a2554.mp4?token=CVGPqgRGiz66P2WQcD6g8I9CyGBB1o0rXQ5dVn0sC_8x55BtfLCyicDdRM_jypx8tlLyTYzM9Ck6-aIg_urFzjMv86XKqot-7EOGyPHdGVcXoFLIZmu3GBRWd5BUeb3x5xMcDjr4Y24ublMTRv8Am6jXTIF-UmU0O10YpgVnFOikqOr2Ubs5bNWaPFFA166onUTcCK16xfj2D734SytKiiCG_jf1cjT0vZ-XAinPFso0drECoWNiyye1G33Lw5N6VbHX2p1iStqIZqRGT0qA8UPm7DW9-_aht_K4BxvPuoItD68AGeHXFfEc_Zztka9fBnpIWLZy1XYJrW4k9c1idQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
وینیسیوس گذشته خودشو فراموش کرده؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/102794" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102793">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خفن ترین تیپستر های ایران با هم جمع شدن و TRUST BET رو تشکیل دادن
👍
هیچ سایت بتی دوست نداره شما این کانال رو پیدا کنین
رایگان بهترین شرط هارو براتون میذاره
حتی هزار تومن هم دریافت نمیکنه
سریع از این لینک جوین بدین کانالشون
👇
(این پست پاک میشه)
g14
https://t.me/+cBQ8n7zLQiUzN2U0
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/102793" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102792">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX450VxPkNwhbNqhA9xvNBzkJQ9Epz1hfFQfmgKbhuXgsIuIMaUe_r7VT3rvKWQmtG1UXQEuafS6JJlwys6ZdN4Gg3OhIBc7ZS9Xh3i9o3IiUKbvZJZKkGm-bAnP-mbVUPl9-u39jgowWUoKwNiPnlw6wZnoQwrjyN8rUSCuuzlWdps_y-qH5i9sGeYIpQMhOe6S5E2PFQK73tqL3ZWYIVrCY0EGpTpOtGmD0z240AvsIs9lxp33AnLmi4ucBS6LDy_jpcwTbfTotiVdJNwKPYgOz5kP2WAxaCJ6mvMQj_-zRCnW6vdad72_4EI9qtr2MT4U3h-3niY7hyg9PLufIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">40 میلیون تومن برداشت روزانه ی کانال تراست بت
🎁
پول دراوردن از بت تجربه و استراتژی میخواد نه ادعا
برایند ماه تیر توی کانال تراست بت: 78 درصد رشد سرمایه بود
✅
40 بازی اخیر 34 برد
📊
💠
https://t.me/+cBQ8n7zLQiUzN2U0
g14
💠
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/102792" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102791">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a91c5460c.mp4?token=qbGiWhw6uI9k3D6bdFzvJWJinWBVydL7uyDCsoXvP8HjIWRkvd0MuXE3ekGIJQyJnxFYd964rKgRdSqwB0dHsf0BQV9WIRBujmKD3gw_cHG1vWmXxjVBXlLRg1-EkgM0M-MfXNRh6JSVCR3b1WWdo1UIQ36_JfY8cd0yORAjJ26TjkIbC_06hmFQkLAfj-62l2JNsoqnC4zgmaku3URFbJM8HlGf4xFbsrvC6frcyyJB3MomLNCQAEiaESIW36_9HbNBaEgW98kpsVe_0vO2Tu2ByRxnB2zxfiJUcEnAKH6WAvjXP9PxmsEpmyaSXHeALfobP3ooW9kddj83hSIAPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a91c5460c.mp4?token=qbGiWhw6uI9k3D6bdFzvJWJinWBVydL7uyDCsoXvP8HjIWRkvd0MuXE3ekGIJQyJnxFYd964rKgRdSqwB0dHsf0BQV9WIRBujmKD3gw_cHG1vWmXxjVBXlLRg1-EkgM0M-MfXNRh6JSVCR3b1WWdo1UIQ36_JfY8cd0yORAjJ26TjkIbC_06hmFQkLAfj-62l2JNsoqnC4zgmaku3URFbJM8HlGf4xFbsrvC6frcyyJB3MomLNCQAEiaESIW36_9HbNBaEgW98kpsVe_0vO2Tu2ByRxnB2zxfiJUcEnAKH6WAvjXP9PxmsEpmyaSXHeALfobP3ooW9kddj83hSIAPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚽️
برادر گارناچو که فوتبال‌بازی‌کردن یادش رفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/102791" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102790">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59768147dc.mp4?token=P6ueERHNiFolUajE3UxcKd4UA8neDCB5TpMmikuFVUuQVGgwEPNlWoKLrWds4DrroZcgisR4otA06pbEMtd7X4WjtGRz2kfLo01k5EDQXQZJQo0E9yMa5I0R9vWnoA275VNn6tUBhhFPGtSbd7aO5DcdDGQBu7Wgex1MK6b4Llr1Zn3GR3IwOZis9bFNgk2flipyhKngehuUoKttr63Qp85aKV2UEv0LYiANJdKpHWmJ2wpouuFSSlxCgJ0kdFTFpeUjGUlqZJzr2SdVslOtAvwhBZmGO8jawGsEf79AVRrQeCQKoYiyPxmegdLQZyGUCJbmnjqlkLVdZCWhRQyvZyoTau1Eli_F5i0uqQlSui9DDZ_tRvGMRdqTQU05wQLZuqxxlaiBxw-X2Bk6GvDjtIlj7jCthUVZBJ8JNcjDMNa4dKi8IuzGKuvMm6PSwnRilmKTCszmkp8ZAZvX6lkVaz1xZa-3TJiFP_ZdksuAHQ2ZckMktPorXLx7PTodBm6YANZ09XrwE1Pn_Pnqvm1IC4wyOqfI2uhrufB49BWxpsSQw_ps7QbdnpJ92WR_v0wlW9x-nbKlHlCs33jjPADo7cBUU7HwzJUPFp3sXfoaGwJsOl6ktqLWLMGf1RVDU6PIs3GONysXA5Tk_edU_HJXyZ6RiAn57ycyGQTpdm7pq8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59768147dc.mp4?token=P6ueERHNiFolUajE3UxcKd4UA8neDCB5TpMmikuFVUuQVGgwEPNlWoKLrWds4DrroZcgisR4otA06pbEMtd7X4WjtGRz2kfLo01k5EDQXQZJQo0E9yMa5I0R9vWnoA275VNn6tUBhhFPGtSbd7aO5DcdDGQBu7Wgex1MK6b4Llr1Zn3GR3IwOZis9bFNgk2flipyhKngehuUoKttr63Qp85aKV2UEv0LYiANJdKpHWmJ2wpouuFSSlxCgJ0kdFTFpeUjGUlqZJzr2SdVslOtAvwhBZmGO8jawGsEf79AVRrQeCQKoYiyPxmegdLQZyGUCJbmnjqlkLVdZCWhRQyvZyoTau1Eli_F5i0uqQlSui9DDZ_tRvGMRdqTQU05wQLZuqxxlaiBxw-X2Bk6GvDjtIlj7jCthUVZBJ8JNcjDMNa4dKi8IuzGKuvMm6PSwnRilmKTCszmkp8ZAZvX6lkVaz1xZa-3TJiFP_ZdksuAHQ2ZckMktPorXLx7PTodBm6YANZ09XrwE1Pn_Pnqvm1IC4wyOqfI2uhrufB49BWxpsSQw_ps7QbdnpJ92WR_v0wlW9x-nbKlHlCs33jjPADo7cBUU7HwzJUPFp3sXfoaGwJsOl6ktqLWLMGf1RVDU6PIs3GONysXA5Tk_edU_HJXyZ6RiAn57ycyGQTpdm7pq8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
روایتی شنیدنی و جذاب از لوکا مودریچ افسانه‌ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/102790" target="_blank">📅 18:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102789">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
⚪️
دیوید اورنشتین:
🔹
وینیسیوس جونیور برای موندن تو رئال مادرید 28 میلیون یورو درخواست کرده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/102789" target="_blank">📅 18:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102788">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bL0D1clbb_8mHOrPH0a8ohuknTdJNyHGJc5WAoZd7Gl_sF8i0fVRtKDLPqppK-qSyt85z4EGXmcWJRT9VYH1SdQVdrRJ_HRgJDWZJkT9I8nYNvFkMytaejOub25eScTrIAg2cobSW2ezmd39DFGveZ1X1A9Y1RwWhfddxRnmEaZuUox2rAfzFxfawapNz8vpjdi3T_FQhIpv8XlQHbgb_VGmU_VUxu45m2BDumwyMl2nywTmOWnOgzdMoASv7AghCnLAqQSHibuPJ6YNGUACdmM1cfub-cYzBYa04Mht3xciCPzF6Y3i-I2IJ0U4plDYKpRfLZrJ13X2Vo2Nr-Jn8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚪️
دیوید اورنشتین:
🔹
وینیسیوس جونیور برای موندن تو رئال مادرید 28 میلیون یورو درخواست کرده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102788" target="_blank">📅 18:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102787">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UehO3pRaWzYnUFLetJs0EJu1aaDR1q-tIV_DcmKw-vT1wwl259uDXM1yVa3oKs_VSi94wPWj9alBJkfaT8EUulLFeRVMNvJGYEnX5VeX5SCPBYnMN_bMoxlKDnqhsIq8hlQy39kDWTE6vB6YG_no4dj1eJISU_8HdkhL0Nf-d70w2y7jWCArCSHVr0NraH2EQigkHgMdXbDuIip2GkZgGflFYWoKzuxO98dAhcFqe5IjN-D0iHaM0ocay9t8M2m62gSUL5SmyLNjqhQMCZ642QIlHavr2MJMT13kOmCXq1Hi8XbUBKv5bl3ZD7YseDRKE8s9_zsiKILlNn871_RCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیس فیگو:
اینفانتینو همین الان باید کنار بره! رفتار او پست‌ترین، فریبکارانه‌ترین و خودخواهانه‌ترین رفتاریه که تا بحال دیدم، او برای خوشحال کردن رفقاش از هیچ کاری دریغ نمیکنه. ما باید شرافتمندانه زندگی کنیم و به یک قانون متعهد باشیم، فیفا هزاران مشکل داره، اما فقط یه راه‌ برای حلش وجود داره اونم رفتن اینفانتینوعه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/102787" target="_blank">📅 18:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102786">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d841566422.mp4?token=dcEgxIzsYM39LHvINabosAk2x3UYAHY07mL03X46zuflDm8bdNokBb2Gc5znRuNuWDsKBXEzVluDKFkMAQWKzpZ_3cTPSRZ_-4R5m3kJ3Uam4A8DctE0oaEjFm1RG9_qe7deRAjCG3VYHn5qfG6MdiNfNFHGTtTDizANe3kN3JnfHETCVVOLmJD8ixS9RBPPUs_V8IT3u-DdrqZMmL8ksYSBy18OlTw1HRNtu_H_hlK06wg2xSP49TURGZH6ucFMsYd5nfp-ctzO5DVE5W3A5SZ5T_ndCYR8e5SI1yQgmJ_8gkGrqoeJMAmQkYrKXhu3Lf6tKwtd8RD7mRK-SFhz-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d841566422.mp4?token=dcEgxIzsYM39LHvINabosAk2x3UYAHY07mL03X46zuflDm8bdNokBb2Gc5znRuNuWDsKBXEzVluDKFkMAQWKzpZ_3cTPSRZ_-4R5m3kJ3Uam4A8DctE0oaEjFm1RG9_qe7deRAjCG3VYHn5qfG6MdiNfNFHGTtTDizANe3kN3JnfHETCVVOLmJD8ixS9RBPPUs_V8IT3u-DdrqZMmL8ksYSBy18OlTw1HRNtu_H_hlK06wg2xSP49TURGZH6ucFMsYd5nfp-ctzO5DVE5W3A5SZ5T_ndCYR8e5SI1yQgmJ_8gkGrqoeJMAmQkYrKXhu3Lf6tKwtd8RD7mRK-SFhz-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
سکانس‌های تاریخی ورزش ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/102786" target="_blank">📅 18:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102785">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1Nq2JxWHixCXK2aNhfB92lLbGvy9kW2euu1pt0Lhb-0qCzTJ0UID_yqVLazE8GHumyqeMCm_Ff1fH0OFLTPgoIOX6YKY6TwhpeD_rTonyc0Ji_JPvfXFlimzBu0glq3eMcJiIW8Mn19GrLsCe3LfqctWymCxTNg10Hy-zOx2JPbEfZovk4mSZeKv86T_q-tsdbCPkd0Io5q61d8qWa3d0V5M9kKRPRLWjGqTcFdZCTTbasLV0hODontadOQZNsFhKJxzIXR-EWZtcflWq7DxpHBupfz8NzZ0xwrcjblqlPByF42e-nYzy9IcyyXyZyuEk45Q_PnndQhmlmyWy5bBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرسنالی اینو داشته باش فعلا تا ببینیم چی پیش میاد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/102785" target="_blank">📅 18:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102784">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
وزارت خزانه‌داری آمریکا: تحریم‌های ۳ نهاد مرتبط با ایران لغو شد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/102784" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102783">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa7464e72.mp4?token=D5a5cgqBko1V6mi-T3Lq3kJwBqfLyx-6U006DlA-MKLkWljQGFggpED-dl2FPvpoEjilPEH_JrG8w5O_v4uzVpMobH1rug1Z3VlwILJe1g8eFpBwiiquNheb482yOzd7fHmzo4YPFBVLMEhekuwgz3KAX7L_L7pQ3PT_y7E4TAApR8zEfw_5TAIFDmG19V7phqIKN80KRXOahvx6H3Ms-FTF6wPZfVgmjX-Xw9DumCFTz953QbyAE9-4_bFJtnzU28yBSqP9DHu62E8WmXQzqvJVQZI0BPsc8teO9193mJiMSRUY3Q5CvFeCOO6hPcclbRSphGA_qwTYmcqBfOGQmwBNyWPG0gdZfEX9k8iGHFL44QkNWfPOWcZLBOdGncs8b1aXogAOGtB9SgT0WEjonpTjkptUTyIOuXAuL5bM8M6BEy_nvtIN09IT5Hj_Oocb3TkejLuOS-c4bBuXqc-EycUrwMMaHgRgn_Wl8h6JSr86NgujY1roimrkghq3emy5m7JvZLJwQuWLj4IPNaneqb3xDmgYVRo_aYy6h1mRwXIPKPBqjeQChBnow8H7ROeZXb9FQAEruxIuXO3SiwgXjvzq6zhq-0bD_GUaHONUyu3isO78SEDWEJFDdwbOVohEVXLdqF7hb1YaOaqWKyOV1A_eXFbVv6fZcVwFUKU6blI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa7464e72.mp4?token=D5a5cgqBko1V6mi-T3Lq3kJwBqfLyx-6U006DlA-MKLkWljQGFggpED-dl2FPvpoEjilPEH_JrG8w5O_v4uzVpMobH1rug1Z3VlwILJe1g8eFpBwiiquNheb482yOzd7fHmzo4YPFBVLMEhekuwgz3KAX7L_L7pQ3PT_y7E4TAApR8zEfw_5TAIFDmG19V7phqIKN80KRXOahvx6H3Ms-FTF6wPZfVgmjX-Xw9DumCFTz953QbyAE9-4_bFJtnzU28yBSqP9DHu62E8WmXQzqvJVQZI0BPsc8teO9193mJiMSRUY3Q5CvFeCOO6hPcclbRSphGA_qwTYmcqBfOGQmwBNyWPG0gdZfEX9k8iGHFL44QkNWfPOWcZLBOdGncs8b1aXogAOGtB9SgT0WEjonpTjkptUTyIOuXAuL5bM8M6BEy_nvtIN09IT5Hj_Oocb3TkejLuOS-c4bBuXqc-EycUrwMMaHgRgn_Wl8h6JSr86NgujY1roimrkghq3emy5m7JvZLJwQuWLj4IPNaneqb3xDmgYVRo_aYy6h1mRwXIPKPBqjeQChBnow8H7ROeZXb9FQAEruxIuXO3SiwgXjvzq6zhq-0bD_GUaHONUyu3isO78SEDWEJFDdwbOVohEVXLdqF7hb1YaOaqWKyOV1A_eXFbVv6fZcVwFUKU6blI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکات فری استایل یه دختر خانوم با توپ فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102783" target="_blank">📅 17:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102782">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDYuZCrUU4iVRNhEVRVUiL2_LNpsjScPb2HM_8Lsc2EJliZYQvaqzxAkS-w2uQbPNigajFk_nPJloAT0YWZfF5du1qZuDgC87FcXKja3AQPKpNwgNfuzUFtHGFAfNdlQBP-PgL8ln4Dl9Nkzj4hry5P7lEBp9RIfJfR-GD0mh5zWbRJDeQjwg_EkWKPl--NMAoX_GXeN_ckOg6prkLjNXzv3ESVf38IDr3EmY_U-nwIP9H6H3hFuHR62BA-OJB-W3HO1UsmS1WTzzkWtqncgf15zuUi4FzKzVMDmGT_fSWY5H13XYHb0XGPgWFb-MN-KDwI-iPAW_yFRQ8A1t3HsMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وندا جان دیگه کار از کار گذشته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102782" target="_blank">📅 17:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102781">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB_7hsfd60WLtcePNY16yOa5vnMSGMHQJ1xUmz-kLd3JUwQ5t98xbAXaNcESatnRRCmIOIpjGQMMlCWqt2y4PRUTphpYJE6U5Ejt0X4PnA_4vCm_pff9LZz2PsQ8ZZVwLKFvueCm7qGs540DJn5nyw-eEIYR4T39Ugz6JqqT01qWqXD8htnvZL_I2zlRRXO_GYLwU7PZcp5pqPYDoyD-izz6FgP48fVVS97e-EcPyEbjhYlGwkB2cGKdWY67TGrwPP4bUvZnphSjMMnUlfCZntCAFThB8AuNbu0VcQZQMqNODM1htq7a7BwFNlkhe9HXXczrsp6DZ7TPmF-tVrTKMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیمار در بارسا
🆚
پاری‌سن ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/102781" target="_blank">📅 17:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102780">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvaHtjwurhXGqWimkoaxscL5dWTNHbJpPgIO654ErvthSZrq3CmkDBYDekg5an7uux4WUjTY-gOJIFcqdQ8kg2UYQ7GrP8VW899UBobJqORC_tMAcWMl6mKHcVxHKaBzB4UgV8SPO3SS7NQ0S_l-I1z5gti1o5zRCYaFdhqPMUtUNjk-FtCLEQrelXnwofqMpk8UK1Gzqdk6R_UTQXyUW-cFfW2ATkvyiwgeqIHsT5cfh-yRrXlRXHTC-eOF7KtGGaRVOcSF1muMHf0EVpv17LunOVTzjN9AReYDuwlOmwI8S0ctdrczXZ207uqK01cqeKSPo8jtLSlXa7D7sxp2CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
بازیکنای مطرح حاضر در این فصل سوپرلیگ ترکیه:
🇹🇷
ترابزون اسپور: صلاح و اونانا
🇹🇷
بشیکتاش: تروسارد و نوبل
🇹🇷
گالاتاسرای: اوسیمن، گوندوغان و سانه
🇹🇷
فنرباغچه: گرینوود، کانته، آسنسیو، تالیسکا، آکه، اشکرینیار، سمدو، ادرسون و لیواکوویچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/102780" target="_blank">📅 17:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102779">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtSsVisNQdef9zeXkWJa60MBEXmd2XZijj4nIaL4Ewca3XLxC1uydieRVfOtEE9TcnkgrDkhWB4x9ikdlAhegiVctcvAT8A4GeAcnMjAtn6IeIPtnTrDdu8cKD-yIz-VkW8mXDm6pxn6m45TFCADTKxUgVUblvuqtyOP7LmZ0mOjtiWwhmqFfiIZQq7j7po0qwOaHcqnbV5KqYG_VND-Y6h8DN6xogDHBT_XX57RbD4wXgzKV8I0z4Ge3b9FDcG1kXKTW1wi5fS3xtpDR4USg5vyW2hRmX_rxI5pO4AYgt7bjFA_dl3pcm-X9ZoHX-l-zKkKMN1ypgzSGrsuGL338w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
چلسی بازم تو بازی دوستانه باخت؛ این بار مقابل یوونتوس.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102779" target="_blank">📅 17:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102778">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHjNRJwm8wCM4a1SFwjRK-XmEMTTgwaVwff-JAnb_zQ_zj4bwvK5OnG-wgWuJbMquJZtCWZiRU81tL84elnKLQt45ZGq_Jp79JILnpa7Vy7D-MJ1InlImCtUY04o0_tpW0N9A2pnnq2pgXHmZaRsw1Xb9yqGWBX7U4fB6HOrZIaWFKorP5D35d4mIv9eA7CX3TCNusz2ch15kImIxj-KAs7_zoU-vhO3b0XzBeilcUe7wCXGb7e_3vgnfzrbtdahnuTXnM-gdljoHnvvzM52USghUFav-6f9KueMyzxJYB1lQJbz6xZrSfnTg0GxA6xJXt5mydsODPw6NXXc3Zmwcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
چهار خرید رویایی رئال مادرید در سال 2009
:
🇵🇹
کریستیانو رونالدو (94 میلیون یورو)
🇧🇷
ریکاردو کاکا (67 میلیون یورو)
🇪🇸
ژابی آلونسو (40 میلیون یورو)
🇫🇷
کریم بنزما (35 میلیون یورو)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/102778" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102777">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyVN60snFb_QYS57y-66RMqaoVe1BOOBg9MKvbyOhGZd7lLbZUXNzw2gVuoPgKeryjpqCZlHMmND5B2O9agNhb0S06kiQwDTGE3WIk3_Ey9r6Q48o_aQQighTAkg6pFn2VccYE2VydAuF6o4zAy2KK_KWiaBXk2tYh3zHAkORjjLbRACViaIzLM4UZzZIHAlY9L_vn4DMdUj-peX0zcFWUHdYTznT1kjPM-VWJkfN1ur0BhGEMYKsxGfH4ol4TcyspK2mt0k0YETM-EeA1Rv0QKnbi1mql0XX3eSjFclxwdnbA_uYb_y4lpLo0_Lo1PmZLQ2UAp7Erl2NUlzwuhsbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
بارسلونا قرار است بزودی رقم ۱۳۰ میلیون یورو برای آلوارز به اتلتیکو پیشنهاد دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102777" target="_blank">📅 16:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102776">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb91a96282.mp4?token=rhGFTFNDxI0Li3XU6aaZ3zriq6nzLuXZ5bgw01f6dJwZuVdtBSg9i2lZoiXPp-a87O6TX20oN-3F9RoUj6SBtGNBzTNV4RrbHdwj2AyAoqvZUuQ3Mu4v6jJ8H0h5nz_iq23SR0CtmjMPa8D-A6D0sCGQysh-aWjH43Eye5EL6WX7lR3OQPzFXTUhh4HWKuYZFJlectlbwzDzxb5di0j3B-pmCdP0xqROY3u-S_f8MIUZh2wI6Sg9QY1zdCJMuVh9rAnF2ibcW1ExQNIFRxLklz1BU5trUuUvf5httBQTX7zoRKyv68g5lBEYz9Pr6GFjanP4VysiLiR_frlxj7Tg_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb91a96282.mp4?token=rhGFTFNDxI0Li3XU6aaZ3zriq6nzLuXZ5bgw01f6dJwZuVdtBSg9i2lZoiXPp-a87O6TX20oN-3F9RoUj6SBtGNBzTNV4RrbHdwj2AyAoqvZUuQ3Mu4v6jJ8H0h5nz_iq23SR0CtmjMPa8D-A6D0sCGQysh-aWjH43Eye5EL6WX7lR3OQPzFXTUhh4HWKuYZFJlectlbwzDzxb5di0j3B-pmCdP0xqROY3u-S_f8MIUZh2wI6Sg9QY1zdCJMuVh9rAnF2ibcW1ExQNIFRxLklz1BU5trUuUvf5httBQTX7zoRKyv68g5lBEYz9Pr6GFjanP4VysiLiR_frlxj7Tg_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🔥
🔥
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102776" target="_blank">📅 16:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102773">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stidUZnm1IMoLxbxrGUf3hUlGi8RcJlyl5bTWHoc5w1iWbS1tkASh_QYXzybCiT9j-vZcAEW2frK6Zjv3Ed_spsyEHERlpD2HVb3JObySvXKbSDz2xYgWCAAz-54HfNKI9VKTtX-GlG4A5l23EH-vJMqzqOVq9RjMuf2JE8h1kqx3qMKDaqICC-nl4GRX074XVexX0g5X5Zlgk8hfQkEGufap116PViTIsTFRXIoPu1d85xVUuWeKDZ6aglEzMuBN-ek9WMC5ipvoH3yVWlMJK7ntaTJG0AC80kNWsGDzfUNNottTq3o-OT6DR2Jb0QG6YJ_V0u3zmtYu9ZS9BtoWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VmycOOThZA7XZUqjvHPknI_fZPpgixbF3QuSWBz_98fkh0As54ouXauAtyE8U8RCHjaNHIQ25JFUkE1gIC5ONK1hj7Zec0SClTGt2e1aCqFmQFmXD-TAdjwJz81j1gRyX-xiaafvmQT5_YsjU2reC-Btx4iUNSi-YX9uGeu_TlMgMtyRR_BhV1ajumk71oED6QWNRo0SjCGXDXxsd5hYEMLufs-B2TmHrqeKvmqAPiP01NlcOEC58i5TFpqkkoDZD9taBGG5XuPFF0ZP5SoVNmTvBGfhrGCs-8yZBnJuGf2vWkHlFM7q6MBY_LwnA8e6QTQKee7kEwphn4myg0pLHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqIggQhirsAcpT-oJ_IEsxm0ZVrGczqN7kCylhi1RaUXVF2Lesbvr5d9yJZKgwky_umOPbab7mHSgCu_0p0jejH8k4YcgXAixbqggHRQeXz1qVrfl4ZKsQSzzE41HFeHjFd17dpBZUq6QVF71LN1jh8RrrzlqwgPksM5nnIx6vwkzE9W6EYW09HloMn1pziM3x3p6YzeeMiZBfLcObcPYdyFQ2c5jv4mMzpACYhV86UAS92qi38RlgMpwCmomwLEC8wZq0Rja8pF97mto6McZGSz6bzPRWp-R_OiXrIVpDPproEQJei0VEnoLc_bH2a2xCUhGBxjCJ9sGlgJmHhUAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم «کومو» یکی از قشنگ‌ترین تیم‌های دنیاست.
لباسشون، شهرشون، استادیومشون و جوری که مرحله به مرحله و از سطح پایین‌تر ایتالیا رسیدن به سری آ و گرفتن سهمیه اروپا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102773" target="_blank">📅 16:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102772">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba5d6f365.mp4?token=uxVuwyiSgmVNKw67AtNNLmCtgYKmk1S2-OrhrWbcfBBP9DG6fqvPZus4dc5oqGyD2M0eps3BL_KxQiZqQxHFWhd0WoLSyj-Wd2iagkaP27C7hmZDwZmWrJwevFl60IFbiKPnmUcUXcuYO8GfABJS1mTlD6ILpBb-hWmY7I15YSFBtG0ve9QMZUkPvkAFG0cZNodls0wnc9Mp7kxU5KLmcIUas8wkn44J70hxiN7ufOuWI9nyJW1ZF7idkFnsb8zDlrY4QFksLVVvTeIDvlL4gj-vrGo8_SvDC4bkLxROpNNTOOXRukS3QSEFBNN6tbB4A0sMAg80mY1EbsFig08Qsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba5d6f365.mp4?token=uxVuwyiSgmVNKw67AtNNLmCtgYKmk1S2-OrhrWbcfBBP9DG6fqvPZus4dc5oqGyD2M0eps3BL_KxQiZqQxHFWhd0WoLSyj-Wd2iagkaP27C7hmZDwZmWrJwevFl60IFbiKPnmUcUXcuYO8GfABJS1mTlD6ILpBb-hWmY7I15YSFBtG0ve9QMZUkPvkAFG0cZNodls0wnc9Mp7kxU5KLmcIUas8wkn44J70hxiN7ufOuWI9nyJW1ZF7idkFnsb8zDlrY4QFksLVVvTeIDvlL4gj-vrGo8_SvDC4bkLxROpNNTOOXRukS3QSEFBNN6tbB4A0sMAg80mY1EbsFig08Qsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
روزی روزگاری رئال مادرید در بازیای پیش فصل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102772" target="_blank">📅 16:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102771">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk0Ht8wM6WfATOrXKeCpJZgllY0nKBsd_p4-UvAjZfaIioq1II1DrQQvvJGN2ZACVcLdSGX3bi3z_O_9Wnrho2S6OiEasAuNzgIGLVRTCQH4xyAir9u5LVQ383PwEy6IkTXn3lqJMy79QQ7JVNydMWbY6f0WnbK4tSCS67KZzJmLVu9Sfd1ZJw5vJD-2aFlXlLsYCvOV7KG6lcJb7vpgEqhWvL4o9dBXOZDad72mkmeVDgrpd1dKMZb2FVnISe1BJ3T5Ksqe85fHO_NpYzaTf5za-6yDzYjMEXeBoNtVySz8AUxU7yTtdmUCkz6PM88-GMx5BLfDeIxCc3HqaN6tsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس در واکنش به هوادارای رئال که فریاد می‌زدن: "وینی، بمون"، با علامت
👍
بهشون پاسخ داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102771" target="_blank">📅 15:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102770">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0143fadc66.mp4?token=kA4ArFnMQ1xjcTINk57J1f6I8-1ruL9vGicxBNXSwQppyemjlQCEs0noT6zTY13s9bApnC5U0xl9FrlQgMqjg1HKdGAjaQJK7RSXwuZQ-TLtsNQAub_pTBDpXy8N1aHXqRVEXx6dvaofGiNSfGfMt2SyNG7GBYTmvm0iy1tOcIJj3yh0yBFKfD2KjHHoBjfMolXfwaqMZzgoX4j9XEWdnLyEBFzndTiMgPWRWUw3A-BcDZ_yQYS47RTfC4ea2ss6Bvb4yss3D45rsCQkyWxLMc6OszOuK-1JigNnzf1mqylGyP7T6-YQH_G0pF8sIBsBFNNEDOq1Jc5C34XKg8QL8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0143fadc66.mp4?token=kA4ArFnMQ1xjcTINk57J1f6I8-1ruL9vGicxBNXSwQppyemjlQCEs0noT6zTY13s9bApnC5U0xl9FrlQgMqjg1HKdGAjaQJK7RSXwuZQ-TLtsNQAub_pTBDpXy8N1aHXqRVEXx6dvaofGiNSfGfMt2SyNG7GBYTmvm0iy1tOcIJj3yh0yBFKfD2KjHHoBjfMolXfwaqMZzgoX4j9XEWdnLyEBFzndTiMgPWRWUw3A-BcDZ_yQYS47RTfC4ea2ss6Bvb4yss3D45rsCQkyWxLMc6OszOuK-1JigNnzf1mqylGyP7T6-YQH_G0pF8sIBsBFNNEDOq1Jc5C34XKg8QL8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی نیازی به تست دی‌ان‌ای نیست:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102770" target="_blank">📅 15:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102769">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f7f8280c0.mp4?token=ecpluie9P2qKaIjbPJUJiMeq9WLsJay04m7qlMZUHNAmJyfnJ10LkkjsFzuoNc5DstvYducJXVnOAMe2hAUu3c6pctm3OLLJSzMLX6EOYD23kq6oBI6da4cDsoFPq8wQd_Qr9Lw8hwx96c6avyA0ojB5iGoixKcwwb3qAs9APp9XYaUPLWIyrhNek6fwuT6aw2IDy1E01YFM5D4gumk6L5foJCxeNg8At2Z5kR7Kfn2ozdPnBx0lCc0SX8d4sTsi3Fgy7r-TNyBmkjWNeZHBdnMYIYD4W2-Sm23mHBMfwEjvAPiwiykL2FXbq5EJD1XK8Tljn2pnFF-FEd-5ilYsrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f7f8280c0.mp4?token=ecpluie9P2qKaIjbPJUJiMeq9WLsJay04m7qlMZUHNAmJyfnJ10LkkjsFzuoNc5DstvYducJXVnOAMe2hAUu3c6pctm3OLLJSzMLX6EOYD23kq6oBI6da4cDsoFPq8wQd_Qr9Lw8hwx96c6avyA0ojB5iGoixKcwwb3qAs9APp9XYaUPLWIyrhNek6fwuT6aw2IDy1E01YFM5D4gumk6L5foJCxeNg8At2Z5kR7Kfn2ozdPnBx0lCc0SX8d4sTsi3Fgy7r-TNyBmkjWNeZHBdnMYIYD4W2-Sm23mHBMfwEjvAPiwiykL2FXbq5EJD1XK8Tljn2pnFF-FEd-5ilYsrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
ياسين‌چوکو بادیگارد لیونل‌مسی این‌روزها علاوه بر بدنسازی به تمرینات دروازه‌بانی مشغوله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102769" target="_blank">📅 15:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102768">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8597e812.mp4?token=k3CGNPUeck5vDil5gIQkr29ypV5JJsN33jfbFYsvaezIxORGUYVZucYhitGLe9mhW9uDcVbQcFtgiWKvnyBP6f6aS3ymX2O4DlYKPlklqjnGsyaK9XqKi5XFZZMLcbE0fGbBQErKojtVb-WKJLnnLrS4KPMXDV1QzJf2WrQUoOe6y7mgFE5xOnPT6CWI5AH-NMo2GtEpCHdh11rzHTxQK0chRPfQll3YTyF4B-b1J47HoE7Ns0GtxUju5JASi0qLri7KZDu4ic8JzdPrYirprh6Wz2kXdwB6YB8pZZKh64NOZ8oDdm01CfKanBgjaU0nMZ9eiwOUI8yZc_fqEwW-wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8597e812.mp4?token=k3CGNPUeck5vDil5gIQkr29ypV5JJsN33jfbFYsvaezIxORGUYVZucYhitGLe9mhW9uDcVbQcFtgiWKvnyBP6f6aS3ymX2O4DlYKPlklqjnGsyaK9XqKi5XFZZMLcbE0fGbBQErKojtVb-WKJLnnLrS4KPMXDV1QzJf2WrQUoOe6y7mgFE5xOnPT6CWI5AH-NMo2GtEpCHdh11rzHTxQK0chRPfQll3YTyF4B-b1J47HoE7Ns0GtxUju5JASi0qLri7KZDu4ic8JzdPrYirprh6Wz2kXdwB6YB8pZZKh64NOZ8oDdm01CfKanBgjaU0nMZ9eiwOUI8yZc_fqEwW-wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
▶️
#نوستالژی
؛ مروری بر آخرین تیم قهرمان پریمیرلیگ انگلیس لسترسیتی دوست‌داشتنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102768" target="_blank">📅 14:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102767">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e70775585.mp4?token=WZVXZHT_eKpg6G_BIa1-75MwQbAaqj01ftioMIsXCXLNL5JKWQv2b9RMfUjXEbkQIhm8yP-hjLekigUdjf8Nc58iZt7-rDazq-YQBJ714yTeqHNKzMOAMM8yhJG31Djrc302fhGmaOheZzAqj34r0hBRbTj-xZbJ36L_jKJdImZaYDLNvo-cg1BYyIr3o9LgQf452gnFj8j-0BHwirHOgxLDtY7KyzNYA0tl5I3eENa00tFWKUgU5GGlVofgFYRljMYHAKhXiYb43VfTpUEyV1KQCE4TV2mok0Nye6ogRFr50iXeHpZdc_VWY4JAeSzC764laSQLW7bYDcOyTBu3oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e70775585.mp4?token=WZVXZHT_eKpg6G_BIa1-75MwQbAaqj01ftioMIsXCXLNL5JKWQv2b9RMfUjXEbkQIhm8yP-hjLekigUdjf8Nc58iZt7-rDazq-YQBJ714yTeqHNKzMOAMM8yhJG31Djrc302fhGmaOheZzAqj34r0hBRbTj-xZbJ36L_jKJdImZaYDLNvo-cg1BYyIr3o9LgQf452gnFj8j-0BHwirHOgxLDtY7KyzNYA0tl5I3eENa00tFWKUgU5GGlVofgFYRljMYHAKhXiYb43VfTpUEyV1KQCE4TV2mok0Nye6ogRFr50iXeHpZdc_VWY4JAeSzC764laSQLW7bYDcOyTBu3oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
خیلی از بازیکنای جوون دنبال اینن که سریع‌تر بدَوَن یا تکنیک بیشتری داشته باشن، ولی فوتبال سطح بالا بیشتر از هر چیزی به فکر کردن و تصمیم درست گرفتن توی زمان درست وابسته‌ست.⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102767" target="_blank">📅 14:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102766">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ddc5f55ee.mp4?token=mhbbmVJ3yaiT2mbPoUa_Sp8Vf4tGmZHxvm6AxLonaqD_2geVFycbqs248xdQZoxujCuLoJwnSsyQucIlZBbeNWJ0OXBfakdTMNCHYETh4cQuhJxgkIDOL-QrcN2MmZuNieNVJ5v3uaRkkEvXAMp38D2yW4r6BOUR-KfaIMIFBz7nDO5EJY8dxx2TE3a4bwGVDHtRbX_y2mJl4FWLK4mIE1KxWkdAYLoC8I_sq6HaAeavHQLsahZflHYA_7W5VXQF_1Op8q8-iaZy6ZSqo152s3kvIaFdwifAdxDWhqZVVSHnrCes4M3sX41PyWTF-zDMNT9NKgV_h3UkN7cgX2k5Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ddc5f55ee.mp4?token=mhbbmVJ3yaiT2mbPoUa_Sp8Vf4tGmZHxvm6AxLonaqD_2geVFycbqs248xdQZoxujCuLoJwnSsyQucIlZBbeNWJ0OXBfakdTMNCHYETh4cQuhJxgkIDOL-QrcN2MmZuNieNVJ5v3uaRkkEvXAMp38D2yW4r6BOUR-KfaIMIFBz7nDO5EJY8dxx2TE3a4bwGVDHtRbX_y2mJl4FWLK4mIE1KxWkdAYLoC8I_sq6HaAeavHQLsahZflHYA_7W5VXQF_1Op8q8-iaZy6ZSqo152s3kvIaFdwifAdxDWhqZVVSHnrCes4M3sX41PyWTF-zDMNT9NKgV_h3UkN7cgX2k5Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
وقتی میراث فرگوسن نابود می‌شود :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102766" target="_blank">📅 14:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102765">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCuIT7AG6-SywrzOeq00KO5L7zrlaurlvtv9USBHqLoYfr0qR85Vo1ns1w-6p8E2qe7I8qjtsswhvYlZRa_CIJsCD_UjvBmnSYldHc062Hh21ZnYTNyotJIrIlfV28iwjbfPgzQ2-A86rWg8HHv_7qhxijLUuqt0LczL7XKRiMn1ec04WTzOX0l9_ySgp5yb4cUbFN9u6F1nJA9oqRSPqeW5JQiOVn3p8xM4Jqmoq-MUp5HKTVtN4FI1yhELnJiQZrrC-Br1o9oi9DjtK1M0oTZ0w3kz5d_yIgv6cvylHQWL4OQf_ngr2SqhmqMoN3prTaCS9OkS4XLDSTXAxtxfOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔴
7 سال پیش تو چنین روزی کینگ هری مگوایر اسطوره فوتبال انگلیس با 80 میلیون پوند به منچستریونایتد پیوست و تبدیل به گرون قیمت ترین مدافع تاریخ شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102765" target="_blank">📅 13:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102764">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctDVQIuEVBf9PpBHSqIwcXZzfdnb5XndiO59QEDaryP165XTkxldn7AlccIjhYiittBsVGpkybOWV6FI2RaswmlSLLaaHVISCRG8eOmf9hnQJtSLLtoM0BwJ9rPiEnJExbzOGAj7vkqhQnVk8qmmIoQvbnmCSkK0Ed9BLOlL9uPWzVWyaC9xu9hDGNnC6_hW51twvfTtaNRKqn8vZPSqXuZgcpJrccjrIk3t46DL_Lis_zuctiVnFayXMQnfqZlfx6Svv13PNSoti_8B52Pi8bzUq97SSX-KkZoQneenbfjk_jT6b5sfhYnmyYJHfURKqAOZBHOpUWepRWWsqllxHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
بازی‌دوستانه؛ ترکیب اینتر مقابل میلان
⏰
✅
ساعت ۱۴:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102764" target="_blank">📅 13:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102762">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLBbDfiDqRDLrRTU4qeDpHPaGVoPt26js3CO4ueT9v1TklD1JZUZvvAjb3_E3Gfm-i6iA2LJiVMTXa8KiKlRxNA08yTGUw07yNsqVDZdm8QUf-4EvyOFgCOIMo2eZfJ0Jm0MP1O0DPObV_XW0vM_kmHKAz-j4NTzOj-9ShHZUGn7kmM8QJj9cg8TeT4zycx-FsrezWxsqBytKzPg0HdA8f8vtAffGVjP7bVWdaRiT7p0fUfGy2YtqgFIkMX6bAflsWdYF40MOzzQbfGJgn8vhJIMyFKjdGLDuLm_bRZPaem_f7ZGxnZom0KuSKUmZRAEbCygEKttwoRk7bVIrwyjMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه که بدونید فصل گذشته
فران تورس لورد بزرگ ۱۵ بازی پیاپی رو بدون گلزنی پشت سر گذاشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102762" target="_blank">📅 13:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102761">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a97462a8e8.mp4?token=P2_p7GJ3lGd8e2lEnvwn6lCx9HByrCqrCdtqSsjZLaDCbPCDwmrGXy7DiNrVOB8yTFelr1qgHqq83t4wEwDGnpke_MIGMXk7JCNteJ4ZKwIoanAL0V-_wlYkrgsfB_RwDlIqQIRPwJcwY64n_E1XSzWCYbSbvBAdJNQY_tg-CnQ3w_g27svS_SbVItKEjZk4WYx0XNQ_QE1SA1OgNQfWWJtNh3xgTjMZ0nXhmutqMaL6bZgcOfPh-N3PmrQjVJzn7_PhJuY98plesZrET-Refv-lwBmBOFVY-8fQzwOsKdBS-2Mj9JkMllgF41sSf5KNoyuigP5u5uwfHWUtzZ4I3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a97462a8e8.mp4?token=P2_p7GJ3lGd8e2lEnvwn6lCx9HByrCqrCdtqSsjZLaDCbPCDwmrGXy7DiNrVOB8yTFelr1qgHqq83t4wEwDGnpke_MIGMXk7JCNteJ4ZKwIoanAL0V-_wlYkrgsfB_RwDlIqQIRPwJcwY64n_E1XSzWCYbSbvBAdJNQY_tg-CnQ3w_g27svS_SbVItKEjZk4WYx0XNQ_QE1SA1OgNQfWWJtNh3xgTjMZ0nXhmutqMaL6bZgcOfPh-N3PmrQjVJzn7_PhJuY98plesZrET-Refv-lwBmBOFVY-8fQzwOsKdBS-2Mj9JkMllgF41sSf5KNoyuigP5u5uwfHWUtzZ4I3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😐
😐
⚠️
ارتش‌روسیه دیروز با پهپاد یه سبزی‌فروش اوکراینی‌رو تار و مار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102761" target="_blank">📅 13:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102760">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJRPAU-A5vnuwZ7XoqNEO5-xB_jAcvPjEBS7DRRbBSHUVBi9f-L7_q2O6FKDJNlIl-wFo8G_sykjmVAZAM7l-zV3qiGvWpew7klcg6xfM4rjve2ELPgMKDH5pocAobrumM70ZltqfgPce4ws8k4FzljWdA6QNgVQerp36r1nHWwQseU6wpG9Z-vdDISLh9ZLuTB2XmI4QXXJuKfHxAx5Xb2Hf_Ib8hzx5b0a6QkjepEboDfHyFKj8_OBbWaAMAbySEXC_zF534orKJy4ZFzyhADpOwaX_C36N1cwZU0jPpiYq1JIHZ7yqrYzdmfEohHP454QExpRlFZkZRMhSUkI7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
بازی‌دوستانه؛ ترکیب اینتر مقابل میلان
⏰
✅
ساعت ۱۴:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102760" target="_blank">📅 13:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102759">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPujSNbe-ZyZYG-4f6FMpP9RbMWS4xCOXtY_-_pOr6OTJ4iFLyUFPb7vBF1alcX6plDOzA6XfRuAH8qIfrKFgNyEBhrObeCpytarQZOg7y5yKgYS4Svu1OqflenYGLRpqGPQeEMxW1XIq5PUt9YFjgLNtPBqwamVw207kepcWsvS8kXk5H10KHJqVGKG5k3xu82L-LFOIhAjYfFNfDEngWh3QIswAAnsGLnmz1W7kmZVxavxXo0QkTi2dnO_wpvnkXc4ge7bjuZRzoR351SU_8Mc4QVUMULTXCXX3BmLB_nT4zQSGjSeyF20bTy-5ekvk_UUKDPzXZhWXWWesqv_Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
بازی‌دوستانه؛ ترکیب منچسترسیتی مقابل منتخب ستارگان لیگ‌کره‌جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102759" target="_blank">📅 13:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102758">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfQTDFqT15Iab5cY22cCWv8Rqz39gGqEniLvnsQwiTH5ZJlV4jEpnlfBxaL8lKrrYVOu7gEc-5h6y71mHYYSGOe3yC6KhtSL7rugBm1oylQ4MdsLglMjjhyco3V5Y5sGYE_F3a1gWA3lwu9mnw69WPWjUb20gN0lQi6Ideinl1cYiJNR2tURQj5Lu6yM9OXfIyeRa5m8HhM9EJqVt4d2mp8iyhSmP8d-HVuo3CWvZikqNwSNNvdDEdl56wa01VNtMEL4pznMpVuGpNKePEjIs6I3twpTSAOo6VbN9h8zjJKro8A9iy5IIPSboLSKOfaNbEX-O5nLm8JFILVvNAGcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
متئو مورتو: جاشوآ زیرکزی بازیکن شیاطین‌سرخ در آستانه انتقال به یوونتوس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102758" target="_blank">📅 13:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102757">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fed5c521c.mp4?token=jiM9kaKS-SbMZj-YuhZDE-qu1qWRANrkYKDgDqOmNWZXleGVTB33ClS8zR0RwnSHyTamMt2QXHH7lz__ZXYOCO2tCQaX2Umg11i8aG3631cI3M7BJndotBUNs-UbAxxAyTXnUehaHqWZ4mIspAfaJzwvQRR0tFmtuoqXfZK_pxGVJq6b8sCCEsQOyh1HDDFFGy04ORozAPnWbCI3epQ3wzkaJLZ_5v1aRXg8Z-WNxZ-8xEeSdDok8uy3L9U0Pstp9Q1N-jB7gWSepR9VwjsrAgKmXDydaDry5PsOjRl3-BflDzZ7NNGl76TKR4F8GnzH06qw7HSAwYIOusZG3nQcEZyGm3TrQ8cxylB72ir_FiaN7AzNAEG9CiwtgR2MELUNLPPS6xdeki3EHM2vZ759-I7s1KFFHmv5bLxa8QbzO53KZ3br5QbS-KxOZ5yk3mRIjJvMCeDxeuuR11m7EMpwujwxvvfxseUhJE_2SzS8hLUEb8xxVDBTM_mcrXLr4pe44OFjsU-fvleoO2U7JMz3geUT6X0Y_EsiD7UR8j0fD0yYh867E2eNxdYJGkLy5Gz15a-ZfPdlWW9cMKJ-dm6ccwUBY0ArJ9ecJIA-eM6FrEnA9R4c72W3XDx9VnUTsWl097DHxAWJ8rfk7AUmOKFo9alE_e0jxD7TQbAapgQeLic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fed5c521c.mp4?token=jiM9kaKS-SbMZj-YuhZDE-qu1qWRANrkYKDgDqOmNWZXleGVTB33ClS8zR0RwnSHyTamMt2QXHH7lz__ZXYOCO2tCQaX2Umg11i8aG3631cI3M7BJndotBUNs-UbAxxAyTXnUehaHqWZ4mIspAfaJzwvQRR0tFmtuoqXfZK_pxGVJq6b8sCCEsQOyh1HDDFFGy04ORozAPnWbCI3epQ3wzkaJLZ_5v1aRXg8Z-WNxZ-8xEeSdDok8uy3L9U0Pstp9Q1N-jB7gWSepR9VwjsrAgKmXDydaDry5PsOjRl3-BflDzZ7NNGl76TKR4F8GnzH06qw7HSAwYIOusZG3nQcEZyGm3TrQ8cxylB72ir_FiaN7AzNAEG9CiwtgR2MELUNLPPS6xdeki3EHM2vZ759-I7s1KFFHmv5bLxa8QbzO53KZ3br5QbS-KxOZ5yk3mRIjJvMCeDxeuuR11m7EMpwujwxvvfxseUhJE_2SzS8hLUEb8xxVDBTM_mcrXLr4pe44OFjsU-fvleoO2U7JMz3geUT6X0Y_EsiD7UR8j0fD0yYh867E2eNxdYJGkLy5Gz15a-ZfPdlWW9cMKJ-dm6ccwUBY0ArJ9ecJIA-eM6FrEnA9R4c72W3XDx9VnUTsWl097DHxAWJ8rfk7AUmOKFo9alE_e0jxD7TQbAapgQeLic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚽️
روایتی از تحقیرآمیز‌ترین گل‌تاریخ‌فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102757" target="_blank">📅 13:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102756">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7cbff6ad.mp4?token=m5zSDpxKzYmLkctLkCMMc1gz5fFEfN0LC_c_jqoaDndr4WoYkT8MdNcoIcs-Ns-7JaevhAMBIs0NaRWwsb8S6FathcxklLTzY4TKcfOgUZn4fGFXUCjFJjM8txYZDayRjBNMfOa2z3_a3nE_Qs6Uh2ldysJXA4KbkLI6MUWgeXQhIhQu-0Pz4lAgk7wDmP4wWjaV79-ww6nHeEaGrTSzhCU75EGcvzpmAlsurBrsZ7Kl7FrPCGYheZoe_d90B_Fcn11oacOq7DkU0y-hUlDfVBnm4Oz-rFlmA44-Yx5xmpSkClVUzhLYEzhjD41MtuOGFbHgi_b5WYytOuZG_xO7kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7cbff6ad.mp4?token=m5zSDpxKzYmLkctLkCMMc1gz5fFEfN0LC_c_jqoaDndr4WoYkT8MdNcoIcs-Ns-7JaevhAMBIs0NaRWwsb8S6FathcxklLTzY4TKcfOgUZn4fGFXUCjFJjM8txYZDayRjBNMfOa2z3_a3nE_Qs6Uh2ldysJXA4KbkLI6MUWgeXQhIhQu-0Pz4lAgk7wDmP4wWjaV79-ww6nHeEaGrTSzhCU75EGcvzpmAlsurBrsZ7Kl7FrPCGYheZoe_d90B_Fcn11oacOq7DkU0y-hUlDfVBnm4Oz-rFlmA44-Yx5xmpSkClVUzhLYEzhjD41MtuOGFbHgi_b5WYytOuZG_xO7kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
تحول تاکتیکی تماشایی انریکه در پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102756" target="_blank">📅 12:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102755">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1773cb48.mp4?token=IXhTjpL7yQhDIZI7tkgvpYM_DbKkwKOWYXWPO0-y2pkwruWf9oDlKSmC5ztB48c7NQouqPpPBmFPb_3SQy5ax-E9Us213SCiqxlivYpT1_KypTN9k7l1awwmUHVZg6nx63wjqiFGhYc68UQrozlDp5Bz5M_Zzkoxpop_A9qvrd7SUyW79nKOtP33fFxhTb0sNLrPZqq72oI2Yy4314H9yTXrV2AJBeiNOQuvuTJ-Dvzs3bxYKNbYoGiVR30MA1g52WmD6x_I2-x3Dr7dnmGUJbCJaMjIbMFhJDEmKLQNQHC1rvSsGczV8Uyh6wM_6nO3AndQOCyRs6B4Ccm7Mt0-vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1773cb48.mp4?token=IXhTjpL7yQhDIZI7tkgvpYM_DbKkwKOWYXWPO0-y2pkwruWf9oDlKSmC5ztB48c7NQouqPpPBmFPb_3SQy5ax-E9Us213SCiqxlivYpT1_KypTN9k7l1awwmUHVZg6nx63wjqiFGhYc68UQrozlDp5Bz5M_Zzkoxpop_A9qvrd7SUyW79nKOtP33fFxhTb0sNLrPZqq72oI2Yy4314H9yTXrV2AJBeiNOQuvuTJ-Dvzs3bxYKNbYoGiVR30MA1g52WmD6x_I2-x3Dr7dnmGUJbCJaMjIbMFhJDEmKLQNQHC1rvSsGczV8Uyh6wM_6nO3AndQOCyRs6B4Ccm7Mt0-vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇺🇦
آردا توران در تمرینات شاختار اوکراین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/102755" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102754">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/960818b54d.mp4?token=Ga2dyxsuxAyE54hbmcMk_dlaCCAEp-VnzsHDb-HocbIyDr2pyDAjz_uorzGA2hgbLtz3vTXy68gFbx3GwvHw_Bg_GSrohwyT27pMt4GOBA1Q9xxc7SuZJsDBehV7rgDNZt11mtMYUhcTgvtHHfwNMuLNNiMTY7J7B1oCgEbY83Xa3UwZmRdPtaCYdMFcBJfNv_TMcVCNORhi8uesurcOBF1DHFhg9NgGRpKF4-RRq-5UfOJxcGmKYSG31kGusl4TGY-08ZY-YT7XBkBJ3CqvH9bWo7iSM2Dev_rKW6padghikJHeBYlnMO2r98ZlOVIBr5BPFsuAZnAPP9lpskiRTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/960818b54d.mp4?token=Ga2dyxsuxAyE54hbmcMk_dlaCCAEp-VnzsHDb-HocbIyDr2pyDAjz_uorzGA2hgbLtz3vTXy68gFbx3GwvHw_Bg_GSrohwyT27pMt4GOBA1Q9xxc7SuZJsDBehV7rgDNZt11mtMYUhcTgvtHHfwNMuLNNiMTY7J7B1oCgEbY83Xa3UwZmRdPtaCYdMFcBJfNv_TMcVCNORhi8uesurcOBF1DHFhg9NgGRpKF4-RRq-5UfOJxcGmKYSG31kGusl4TGY-08ZY-YT7XBkBJ3CqvH9bWo7iSM2Dev_rKW6padghikJHeBYlnMO2r98ZlOVIBr5BPFsuAZnAPP9lpskiRTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بنده خدا احسان علیخانی خوب مچ میثاقی رو گرفت قبل اینکه بخواد علیه عادل کودتا کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102754" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102753">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5HWCQt-sRTcEasNYlxUSxxzgH8WTqfyc6tMpx6NEAh4lPjPLfyRO3yat6UV6JBMLstSYr7MyjRXSQ65hABvem9MQiz0tNaOkDUqjyBQv7ElXyF---QaCd6JlrBSsAlaaFw6aejTx7vmr7Zt_ECq8F-lpmhkZ50hzHsbzrIqsUKPdWWC99Qvzk_spHYmbvromX_ze2FRTC-om0yVoIIGwcxI6kKDdCZyDsawAMAIAbsvnz97bckZrusT4ZmoxRMhuW0t9G2oCMkPhA5mKq7YitWNBeWl0BLYrRzilFBySgsCYBFm0aAD8r-QiMMXs_0yT5QUT9gV3ZkTXpGrL-WMJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
بازگشت دیومانده به کمپ‌تمرینی لایپزیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102753" target="_blank">📅 12:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102752">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF7jA_Dri-rABMwaaREtZH4-i-TRJsArb1LcAyrVemQi4VgQ4KDS50D7w2j9gx7DY7avEUd2MRpE-c3Hway-S5ze4O6fydr1pxP4wB-JrM43KXzPiR1E-QvIHlAQD3yx913LLzNlnUURN5NVIi5nl7DQKNvLYwl0xmapMb8SP-GMn1tbUvp3IebrX_oqyQPBwbM92MXihY_VDK6-IhlQ7L8HkGIOFWvNeMpzLsMx3_LBUigR6qLUzCIFhdJme1Y6wFXcnanrZTH6fLZARbuoP5FHvlmHXH86iC2UASshp36_ZXIFbUjEyD3MHVVbL0DJf8dFA_tPtHP7VJddOukMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🗞
با اعلام رومانو، ماستانتانو بازیکن رئال‌مادرید با قراردادی قرضی راهی فیورنتینا شد
Here We Go
✅
✅
✅
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102752" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102751">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6hUVGSeZ_NCTYBISYYKvBefuYo0iBj1opTrDray-NUr-PkvUTt7SZlx4x2FPF_s6bPtgtgSVbwc2rRkOOVAWNHjLdWvRDytLJNWloaynNDdL9ACQBAmNdMMt7FblPOMSmJNMDYhmzjPkBoIGE2A99XC6czWcWBVkzHhmApFbNiK_07Wjk09BlpJ3DgRDDLGGt-JWLuwmJVNxEaipEGMyjiQ2KSA59tWFjNm9uOjIdv4oTccKh7HkXYiQCgWtYvAcvcO4iDKok4tZlB-tBuYEB0Dm1-evZ7LFsBflVS1FDF3Mqk08ShKjMnzvq1F4RXmgKd5OU38pfYMAX8YuK2Pcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامین رضاییان رسما از استقلال جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102751" target="_blank">📅 12:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102747">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gQtleVrmcsyYRMHmX85Wa1Rgs1NuJP39bJ7b4fimX85wpKcCajbhYOisaE6odXtO2rDmtp4CohZzh0qZ_wgBnnUAfBP4uJcRq480hvgetvK6QHEIe5qDVhRQcQygZ6aFfWm85swOIm2Gk4cB1eLDo1LDkpY8fhPUt4rMNrYYMIfXrAcKvyuX3VPY1i7Ukj1-B-cSA9t-Hw6tF87Xot8io6h7BpyvZTTdlO-EmFmFdDzpxSfO0WbcwsUCdEke2ARoKDFexmG4caYFC6C_htd4Geh_KO_yGbZIpFUdUZ_OBc2VZsQG6dFWGIvO8wiR7pvk8Hq5J3vZM-Xm-hFXaaccTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ES157w5Zo7foy1Az5NGfDIOTu-Iy7NtkFsdd1FknTneEqO1XLcke2Ph_5FZNE3T2fNnElBRuYFPBsw4CV-gqNAhE4tHee8lv-_YUkpxOW4lvJ-hTn-JVnPgIV6h8Gwkl26aax0uTLz4kk1gI4xxgSJCgDEbI9j4iN_8Y1aJHXskY5CcI76rGK_HF7nweZ2e3T95fc292YssOXvLuBTRRp941UvyEeo0w8Bbv4-TxbJ-ZKxR1S9ST-q4txor729qYa4UMnsRS0FgDpiYw_yhjGqMHJZnqDiuSJykR2txK6ejxl2wseg0lL35S08My0cIaLcinQNOaAyPppbf08h5Nkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F9xyWBpcNiX1dwUOSUpdc4y67hrxM4mmer2b3mPhfmTY0Q4Y_hxT8u1pC_HkF5umyEt8dFcGHttwTKWUIpVI-b4Rq6-sOOvOKXbFKuMyty9wRV2qM7rsatQ8M_BBCWtaOPA_cyq8KW9d6iY57CLuZCEFEwtG2T8C0WqxYbmax9ysOBl2LMDYh3LTRm1zB4WD8sq6dAV5QzhnV7ucrZo0yxtRFBoXVbMMcebxQNzuRdl-CTPs8hlRVrufnPR0-HLtcuwkPE939I2YtrJAMkqh9AXD30UNED2hJQEkq31msOCVh20etXWMsvU6Y0T6DHqjOdBs9fsoBKna0YdcrQZLUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZ811GmA4PgNnlBJevIB5yeuN6VM_idViRgJEyO-iRB72Lw1dYzN3F5939xonlCb_saPOb-vKOCT13fT7RGWMTPwLAMFfZahTkUYV9AJZBjeXudd8hw7GEqHwI0d9C-MARyuMaiCrDP-qviXVyQRCNPBA5RHQoB3l6CL9A6N20yuQ2ImalWS_ibTGXEwhUqPqe6oY1EQ-uWtXB2buzOT8Rj22vSiUlAHqDJz6UocPkO74phQeNVhseiVk5sMfjjZqjMrGBCwGE8ak-j9gPypMcx8mFCIsYRpswk7MGf_y4TM8KRZT_9L3au_i44GD0DBRyqTfC5muGTvHgovTuunsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🔺
تیم کومو 7 سال پیش تو دسته چهارم فوتبال ایتالیا بازی میکرد و حالا به لطف نتایج درخشان با سرمربیگری سسک فابرگاس اونا فصل آینده یکی از تیم‌های حاضر تو چمپیونزلیگ هستن.
🔺
جالبه بدونید مجموع ارزش کومو تو ترانسفر مارکت تو فصل 2019/2020، 2.4 میلیون یورو بود و الان به 489 میلیون یورو افزایش یافته
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102747" target="_blank">📅 12:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102746">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c832d40c29.mp4?token=NGO07DPwcpqdL97Y5qMXVsBdOeEv33jelG9Vd0BrVdIryUz-NvMIPz8k4tHxeUp3lJm4HBeKA4x4Y1EUofsGLspaiTk2KO5xkKJY0kodVoiYZHxub0yDBjKIdhXlU280td4c-r3fuzD4Kx1V5wHe3uPwyAT2BXO0CitzJKBn-4YeayLF9mQx-yPQ_Zur0WSl4qhjMymscFqgcor7XufGafQI-qkoq_OJNlW9N_KcgKjhr1Bi1NrO2u-OYhJLmE45FUKhRhDex-xJX9QwX66HBoeO1p_r8vXu5jJwgFS2o5yRPxRaTlmkG7c9FQyHgLYc-Sf4aklxDd2GYkARCjtfWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c832d40c29.mp4?token=NGO07DPwcpqdL97Y5qMXVsBdOeEv33jelG9Vd0BrVdIryUz-NvMIPz8k4tHxeUp3lJm4HBeKA4x4Y1EUofsGLspaiTk2KO5xkKJY0kodVoiYZHxub0yDBjKIdhXlU280td4c-r3fuzD4Kx1V5wHe3uPwyAT2BXO0CitzJKBn-4YeayLF9mQx-yPQ_Zur0WSl4qhjMymscFqgcor7XufGafQI-qkoq_OJNlW9N_KcgKjhr1Bi1NrO2u-OYhJLmE45FUKhRhDex-xJX9QwX66HBoeO1p_r8vXu5jJwgFS2o5yRPxRaTlmkG7c9FQyHgLYc-Sf4aklxDd2GYkARCjtfWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
✅
رونمایی رسمی باشگاه ترابزون‌اسپور از صلاح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102746" target="_blank">📅 11:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102745">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ace4b7d7.mp4?token=Ei-wZwnfWcx7sUiwfxRNkjdJeYoB0Cd16chwF7qeRLlAAJ9XkjY3r6H4mEwKmX6Ev_6BlmFaIwYQjsYb3QyVg82_o97T0fAeFROtQO6JSGIe9Ar8zJS2ai2PzI-UbOCZwRqstsfnG_gP12OeiD_vC9SL8Lwprm-AFhJcAqpHHnO2ntzu43b2t-GPv4S8iiyuKwRukYI1YUc-Z2I33AUwiGqvKaKvW3P4slTGaEmfZYWayBEN0ReFYF8SgFRtKn62oK8KEv9NsoMK2tBr1KNX0vHuHQHO7Vix424DVWrSL7PiikJT13yD57FynbVTpHYh_fQ8Kpf0NZOhIKEGQZ0lPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ace4b7d7.mp4?token=Ei-wZwnfWcx7sUiwfxRNkjdJeYoB0Cd16chwF7qeRLlAAJ9XkjY3r6H4mEwKmX6Ev_6BlmFaIwYQjsYb3QyVg82_o97T0fAeFROtQO6JSGIe9Ar8zJS2ai2PzI-UbOCZwRqstsfnG_gP12OeiD_vC9SL8Lwprm-AFhJcAqpHHnO2ntzu43b2t-GPv4S8iiyuKwRukYI1YUc-Z2I33AUwiGqvKaKvW3P4slTGaEmfZYWayBEN0ReFYF8SgFRtKn62oK8KEv9NsoMK2tBr1KNX0vHuHQHO7Vix424DVWrSL7PiikJT13yD57FynbVTpHYh_fQ8Kpf0NZOhIKEGQZ0lPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با این وزن و هیکلش یه حرکتی کرد که واسه نصف بازیکنای لیگ مملکت قفله:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102745" target="_blank">📅 11:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102744">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c80f4ab4.mp4?token=rLtkbUrakU4AZKNshZ5f3RpnB6nArGXUM6FvnzKywDPEctWZXRCRrxBonM_oUCe6GVoqIShNL_2MSYyw7Gdeu8e4sfRmjlMQ6LNXcXHgmYddcwFTN1fe1_a4UT1ProB3-08ej8V-aVCkkw6NDi81WpjdI_kj2uPrScOvEXn_wHvwSoimB83_m1RhMtqeZ9VLqN15L5vIhWbh_d0KiuQIHev83CxN4C85e9HjlrGDMPIsZEApiIyAE7lxN-HCvNDyWfrm6zcrTUNuAYTAfWsouYuzt61PP0rk5nlYG8XqbR54YLHyjfpQZD0TDn8408JKsR4Si1eBucwHe0rhAocWcmZG7_nOJhyWitjtew-RVUh9lA0CeUnlZHsunmLcNp0bwGqaPLmCyBdr5GMb-UhF4oazuUQ-swWw7kw-cZ2bNDqWKeCb_tIUUzS83U9rNO1s2iVcoQaYX6WpCT3kfjxdQEIQFyql3N2bo5MkYGbAJy_1v0tEow6-3UxzqexXGOONBxGPdLVciIfKkj2rjyYKagybSUrWsuBxmq_dKDIVVRrxUQBQXsqUvQVTsxoH0QpDh3uPJfxpghWjURAVfWVD7Y8c_OBUkrW5jOPEMH7Xn3pq6Al3XkzmAFA412Pq9AxHBsoJyyNhuPiqOjZDGchPO5-RBjtwqiwMFVLF7sl4y1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c80f4ab4.mp4?token=rLtkbUrakU4AZKNshZ5f3RpnB6nArGXUM6FvnzKywDPEctWZXRCRrxBonM_oUCe6GVoqIShNL_2MSYyw7Gdeu8e4sfRmjlMQ6LNXcXHgmYddcwFTN1fe1_a4UT1ProB3-08ej8V-aVCkkw6NDi81WpjdI_kj2uPrScOvEXn_wHvwSoimB83_m1RhMtqeZ9VLqN15L5vIhWbh_d0KiuQIHev83CxN4C85e9HjlrGDMPIsZEApiIyAE7lxN-HCvNDyWfrm6zcrTUNuAYTAfWsouYuzt61PP0rk5nlYG8XqbR54YLHyjfpQZD0TDn8408JKsR4Si1eBucwHe0rhAocWcmZG7_nOJhyWitjtew-RVUh9lA0CeUnlZHsunmLcNp0bwGqaPLmCyBdr5GMb-UhF4oazuUQ-swWw7kw-cZ2bNDqWKeCb_tIUUzS83U9rNO1s2iVcoQaYX6WpCT3kfjxdQEIQFyql3N2bo5MkYGbAJy_1v0tEow6-3UxzqexXGOONBxGPdLVciIfKkj2rjyYKagybSUrWsuBxmq_dKDIVVRrxUQBQXsqUvQVTsxoH0QpDh3uPJfxpghWjURAVfWVD7Y8c_OBUkrW5jOPEMH7Xn3pq6Al3XkzmAFA412Pq9AxHBsoJyyNhuPiqOjZDGchPO5-RBjtwqiwMFVLF7sl4y1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⚽️
⚽️
روزی که لیونل‌مسی به مورینیو در الکلاسیکو درس فوتبال یاد داد و پاسخ تمسخر سرمربی رئال‌مادرید رو با درخشش فوق‌العاده‌ داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102744" target="_blank">📅 11:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102743">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از رومانو: برونو گیمارش با عقد قراردادی راهی آرسنال شد   HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102743" target="_blank">📅 10:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102742">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYblIEoCTMRUflRqzYk1kMAhmejsiWaedgJxMuX3KlTrh6TWYrMNRJ_HIZOaMt_GUJHG8jqbziGuFK-xFLu1zCZJA6nYVYj4cqfZWt6SX8uRuFXw_xDykdNGzErEWs7Adckaz0jABoZk9QjlH8DVWaFnM0JaBGPZQdUu32hWv79eR876mv7Qs1hcym0S8h4RzYqBPbgn7ZDEQHO1RjM84ykRToBF5s8vBYkWMHgLUfqrvX_DxJEkpG6ANfI3KdP1oFt_mYpfcNITMvM7wRfY-dVDcbdEPUwG8oBNszO_J8lqel155KFaDRAAExpj6ktYhi4FVRg9o8a0CU8EQazrYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: برونو گیمارش با عقد قراردادی راهی آرسنال شد
HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102742" target="_blank">📅 10:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102741">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f2e64a450.mp4?token=vRsLcQ7cgCsG3kAPLMLgyXvzMOCjL7vIwMIIfM3YT5YmAAn47RovC-o15dyeYZ5fgyFzOSm6-1AsE0Ni4ug9Ovo0LEurZ_1gKH_k62H0PC409kdp8B4dG_S6x2lL4uREjYoQyX82SWYZRtltCXT76If65nJewsK0GuDM5xHzhXCxCuBP2M56uAVjI0O-TElfMY4XHKctPbCdjk8dq5HgNRDWMTSG7ppA6GmDuEWluaLy1v0qqRkJj-6ee9L095GYwTlJ_h3nmkKHXqMvkhvHA249OuBakH8A8mOLrHANSuDFhDqM8aWmxOb5xqShdklgEDcpcpa4a_G2Q_QDqzlO-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f2e64a450.mp4?token=vRsLcQ7cgCsG3kAPLMLgyXvzMOCjL7vIwMIIfM3YT5YmAAn47RovC-o15dyeYZ5fgyFzOSm6-1AsE0Ni4ug9Ovo0LEurZ_1gKH_k62H0PC409kdp8B4dG_S6x2lL4uREjYoQyX82SWYZRtltCXT76If65nJewsK0GuDM5xHzhXCxCuBP2M56uAVjI0O-TElfMY4XHKctPbCdjk8dq5HgNRDWMTSG7ppA6GmDuEWluaLy1v0qqRkJj-6ee9L095GYwTlJ_h3nmkKHXqMvkhvHA249OuBakH8A8mOLrHANSuDFhDqM8aWmxOb5xqShdklgEDcpcpa4a_G2Q_QDqzlO-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
▶️
تیزر دیدنی ترابوزان‌اسپور برای محمدصلاح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102741" target="_blank">📅 10:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102740">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_4_-Ak5jKS27eNHNe4iIxz0WJRy6cqkV5ohAvYAn3iTQlRrvM6NyFZPYN0mYQEYdCJxDtP6_tzcL5VGNgN9YjpHjnB8Nd1aPdCf82M-ma2N8BAuZWNS1WHSES8S-Hv23ABDFyzqsy6eNM3zemqWj6akim_5rev2Aeg2KUOWzSdp5o42km3s-0sI3LsNdlfj9GF2HQFycCjtBTGYVOHWRTRCDb_gASfCM6Bz6zbm--bhAGRyNCzUloHVNQakrYt3z6ZlF2-Rs2_CpfgOn3neqaL4shRNbWe6nUbR9ZfviHPQqeKl45r32G5oeOnFnRPbUBsJflqHQOTkpJ-XdZ0ThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ وینیسیوس و وکلاش برای مذاکره با رئال‌مادرید وارد کمپ این تیم شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102740" target="_blank">📅 10:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102739">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d431d3ca7.mp4?token=aCfLrvb80IjMyIjofktXdZQd37ujzeMvWOFECCBewsvaL8uF33nb8U5Rg9kJLyE4t4Wua7IL393a7ZGdLsRFiOGMzmMuGyOI4WT_JPIin4PRs3sBD-PwYnhYLwwIkWpdNFIYE6r5DGEFb5bN0OX90HdAsHJBnr_lkLvL-i7cTKzeqiDOVfBC9-eVmszA5p6KXmQeRkjBQkKa3mcZTUtVMJHKoP7zsfuCU6sUOXMhZQed6co2jQYOmy6YY1AGoWkg3hHfrVOvBVQh4r184KpRSV-mGFXFtsoBqRKf3vcnARDHjtVw1Jo3ozoPAXhqLgbH4NNwGFWbItbf8_RrGLiIbbIKiR0kUWw5s8LLQUFY-M7noof5cXp6sD4uA0WQD29NlVIfSNi7CmJohNcdhsMIUPIcPfzKvazXgF8N5eBfJpwdR0JzI63lSvhLRv8tJrLXuMTcTMt0LdA9OHjpSyZmZDRRkUOFLIXE3aEHW3XE2dVzcrCboFeJMc5NnHsnKKaijoQC282clEIur34hROx1kzwZzvl3zg4xQMfx7cfYhkaq9Fl7fg-dKiliiMI_sy0SU6gJiLLpBPyj1zvFnwsy2iiEgeugxJvJcnD0UsCHm_1z6arYY77WNPhONj0G_FJsJAyWMAQNh5GGdsfCV9Ro93gKMkrureU_f18qE0JLano" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d431d3ca7.mp4?token=aCfLrvb80IjMyIjofktXdZQd37ujzeMvWOFECCBewsvaL8uF33nb8U5Rg9kJLyE4t4Wua7IL393a7ZGdLsRFiOGMzmMuGyOI4WT_JPIin4PRs3sBD-PwYnhYLwwIkWpdNFIYE6r5DGEFb5bN0OX90HdAsHJBnr_lkLvL-i7cTKzeqiDOVfBC9-eVmszA5p6KXmQeRkjBQkKa3mcZTUtVMJHKoP7zsfuCU6sUOXMhZQed6co2jQYOmy6YY1AGoWkg3hHfrVOvBVQh4r184KpRSV-mGFXFtsoBqRKf3vcnARDHjtVw1Jo3ozoPAXhqLgbH4NNwGFWbItbf8_RrGLiIbbIKiR0kUWw5s8LLQUFY-M7noof5cXp6sD4uA0WQD29NlVIfSNi7CmJohNcdhsMIUPIcPfzKvazXgF8N5eBfJpwdR0JzI63lSvhLRv8tJrLXuMTcTMt0LdA9OHjpSyZmZDRRkUOFLIXE3aEHW3XE2dVzcrCboFeJMc5NnHsnKKaijoQC282clEIur34hROx1kzwZzvl3zg4xQMfx7cfYhkaq9Fl7fg-dKiliiMI_sy0SU6gJiLLpBPyj1zvFnwsy2iiEgeugxJvJcnD0UsCHm_1z6arYY77WNPhONj0G_FJsJAyWMAQNh5GGdsfCV9Ro93gKMkrureU_f18qE0JLano" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
نیمار دیشب اینجوری بعد برد تیمش برای هواداران رقیب کری خوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102739" target="_blank">📅 10:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102738">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/102738" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
R14
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/102738" target="_blank">📅 10:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102737">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WF4L5pLsnTdqjERdzC7of-RjdJiIoFtQdIFFFuNRG1ef4iTtlfR-VDVCk6nLp7stP4-2qcNyOSBTZjrlhtQbBLV8jtZ0XnxM-f3bXODwfFo_QMNUTdDQ8bfbf-6EV3Mh7l5vsgoBg3hIKiOSEQbNtBGT4Dnu02R1dqOL9mSPWmxsA7oMAZGIf0iEpe8K3Mrb9fNyophROcnLQ_n539N00ILTYph_h_PKABAsqi3SRdReCl1pUFIUVjmQXl9Yxjm_UZNsQanV1YBy1WXtdwGV_mL49KyToSEcnmgi41jV8NblpNnqIz4R9Un8U7aHyMKO3oTrzc5mK5sx9rIBpNwSgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r14
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/102737" target="_blank">📅 10:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102736">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d6bf58ac0.mp4?token=hd4FX_-76Sq3vooGSGZbhcOdAlwz_AdTyETyxGkpr-792AmII8G8aFDnbY5XhaP9_eTeF7hfAzIIhh1Mk8I2DsYvU3Vakor7kxlzQtTGt3YG-sg3mQE7ziz72rq-w-tJIDZFEh7ppTHQGEWm2r_8sd5uPejCHXLaZEFjImdSQljjPRlXDFMiAE9KYoQGcLT1mXftbuZf33OFNgYJjeXfKuJJsa1QvdkCPA4FsO4tpkm2WzsJt4JEoYsMnFKVPZPUvfL35O9uSicoiqjWYahXkfolfVxKgx32MWn-jWJVgbvRWUy5GuistT6w3swaoqu_CcNhVrTfmTTuf2HkK4Efgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d6bf58ac0.mp4?token=hd4FX_-76Sq3vooGSGZbhcOdAlwz_AdTyETyxGkpr-792AmII8G8aFDnbY5XhaP9_eTeF7hfAzIIhh1Mk8I2DsYvU3Vakor7kxlzQtTGt3YG-sg3mQE7ziz72rq-w-tJIDZFEh7ppTHQGEWm2r_8sd5uPejCHXLaZEFjImdSQljjPRlXDFMiAE9KYoQGcLT1mXftbuZf33OFNgYJjeXfKuJJsa1QvdkCPA4FsO4tpkm2WzsJt4JEoYsMnFKVPZPUvfL35O9uSicoiqjWYahXkfolfVxKgx32MWn-jWJVgbvRWUy5GuistT6w3swaoqu_CcNhVrTfmTTuf2HkK4Efgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🪄
🔥
نیمار در بازی دیشب سانتوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102736" target="_blank">📅 10:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102735">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a45508d652.mp4?token=uwj_H8r58MvUUMueiNyZ6jqM0Y82GL7X201_Vt0xAYDiqdnb3wpOUrdHjVBgTtw9Z1ZkU-vUMILHqDljuOr_ekkM-j_9AuP73V886kO8Cbnc9fU5BvV6Vz6tLOs0yzX4skXh-2GcVj2mDX7QRd0oMw24LI3Tqs5QJdLP1j7Axidx0Pf38-15HMOQFOrg-y7N6N1tph-gHP8TYwNK38DUkJ0LYgtnr7Su9KgWH-o7DLADB8l9lTpZJ3zUUaiuyOnf18tTu45sngx_pDvnW2ohZCtjqs-Iq3AEp8Vl7seb4aofsHz1AIft7HUgzIsIpBIKR1xT6gNvb5P976RAVpBQrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a45508d652.mp4?token=uwj_H8r58MvUUMueiNyZ6jqM0Y82GL7X201_Vt0xAYDiqdnb3wpOUrdHjVBgTtw9Z1ZkU-vUMILHqDljuOr_ekkM-j_9AuP73V886kO8Cbnc9fU5BvV6Vz6tLOs0yzX4skXh-2GcVj2mDX7QRd0oMw24LI3Tqs5QJdLP1j7Axidx0Pf38-15HMOQFOrg-y7N6N1tph-gHP8TYwNK38DUkJ0LYgtnr7Su9KgWH-o7DLADB8l9lTpZJ3zUUaiuyOnf18tTu45sngx_pDvnW2ohZCtjqs-Iq3AEp8Vl7seb4aofsHz1AIft7HUgzIsIpBIKR1xT6gNvb5P976RAVpBQrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین گل مدنظر شما چیه؟
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102735" target="_blank">📅 09:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102734">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbFfwQtElSIcC-2tTTGTyghBCFPfqU00CNe_S10t6ZyfMALk6nDhtPCRRDr8_IwlPJWCS5tFsEB_H_iC5CM0iPhF5RQr_WHtEboQ0rrUMSgGhOG5h6i9gd5CVSHia08QSg6HdBRQoLHCVOAGWl2uGC0D-d5OS_9OJhMAylmIOw6ZNIPgytDC161oBuLBjMrxQDIHpj5rLUcOXp9W539Zj2YbDZmLYp9C28CtqEK7K3b9kkQRgMySQpdf0LTYERmpRAB9HEMDVhvE3Uk27gfojJgA-iTaNfpu05YRXuz2wrS_hWDK-UjO4dFj-BXsnj0MHl0mMpwiAVxRT91GhWZ3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🗓
روزشمار آغاز رقابت‌های فوتبال اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102734" target="_blank">📅 09:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102733">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqQHS8CJiDq8PS9_vx7UgTPVCXGjMCcGsgHv40f0Ps_KrPW_G_WKa_No5xRaY7NJfMQYjbUrsTK_fLhkaHtScmwk5JfAXDOpc7Vrc9-NxKmaLEjYnPZfg-YtElbDBhrvdAhLZxzvJmhfPpvkkHEURCwwzyPXBW5wB_a2wLAx3e2bc3UehuehFnclZr9bCfH39wLpq2p22n_06r258AJCUlPQacXNjKVnpfwaqp5TwlTpPNYvNXNQCI5KEGiAtwvp-Y-dtEGMggBDYhSCr_b3X-3HiX9npVpmrasNwfXrXwFByfuphvSnx1rDEgC3VZ5nRdGdrXhgV-7pRmLLvjibuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تیم اگه تا الان مونده بود کنار هم شاید یه لسترسیتی پرومکس میشد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102733" target="_blank">📅 09:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102732">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/663702a362.mp4?token=dldqq-_Jb8w8PSFBfT04a1eoLm4JdconjbQXvQnZQSGSLntOVBejOA6i9lX3EzcSbpQxi_EGWE-e8pV2slRS52GrOxPwBdXUMvDAXcVow97Dy_UwUCqPh6Spmnp8-5wvTWbWis0E83QHCuUhqx5EfOeCGrNYdEXAH_WmmuqMCh4u4XduajMrflkVfb0MizduEXHvlH7jNw4UKu7A92KdZv2IFCna2ZxKpzHXGydQE74kDLR3FcGDpWp2MoDK-njNa-ZuBpv4JKV7JSj44ZPk-4lCmp5OmnIiuBXB4PiAgJtrhQI4PuDpDGz4c6KjfcwZJM77AzyFS3cT1urB8slxHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/663702a362.mp4?token=dldqq-_Jb8w8PSFBfT04a1eoLm4JdconjbQXvQnZQSGSLntOVBejOA6i9lX3EzcSbpQxi_EGWE-e8pV2slRS52GrOxPwBdXUMvDAXcVow97Dy_UwUCqPh6Spmnp8-5wvTWbWis0E83QHCuUhqx5EfOeCGrNYdEXAH_WmmuqMCh4u4XduajMrflkVfb0MizduEXHvlH7jNw4UKu7A92KdZv2IFCna2ZxKpzHXGydQE74kDLR3FcGDpWp2MoDK-njNa-ZuBpv4JKV7JSj44ZPk-4lCmp5OmnIiuBXB4PiAgJtrhQI4PuDpDGz4c6KjfcwZJM77AzyFS3cT1urB8slxHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
دیماریا: دربی روساریو با حضور مسی خیلی سخت میشه، چون ما همه آدمیم اما اون از یه سیاره دیگه است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102732" target="_blank">📅 09:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102731">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZWL_Jy1tAFP1Lh2r5bDLEdHOVUcmSClK4jaZGcc5elE9UJsm7Fpf-u5LMl80CsVsnvBvz8yWM5d_H_7AeoLLf3cz7RBY2F4u6E9_HxRh-DgoiMP_wrF0_fElB3tY6dXm7mbdTD79ux9mJyCjIHVww0XWz0HI82Atj3dadBmoAYjKNgnYbFzAdvToIw36de0MWsrPWA5CtiPaX-v6fZz0VufThsg8FId5fuCs8q6EKxJFeYGrkNbXzLrvFczDWqB1KAIuhAAXMi6L5WRKhyd-uA_aWqO1DUkIFM7YDHMNH5x1T6J4ZE24t0f-zL1MV2MjpIlcVTIhHyQzoEcCwUTVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
✅
💔
#رسمیییییی
؛ اتحادیه فوتبال اروپا، تعداد کارت‌های زردی که منجر به محرومیت می‌شود را در لیگ قهرمانان اروپا از 3 به 4 افزایش داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102731" target="_blank">📅 01:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102730">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvtoEp_cG1WIadYrWOMKreCC_8w-h5ZPALjaGyRF-TOyf10rOhxUo55LwcCxlghbxGBehEXEYJRtdDTLSnhgqJRM37pm7RsNiDYkHP0Ur_Rox3emQGHBBZPb0VDCqVQ5BtnAZSMndMvXqrvzc3FNout1lffb9HEsE8cX-OHJ1Wa4VIIkqMq7wx6-PTDywlKVy3KWSIPYAD_MSNou15RbaKP3w7yPxyRWwBPmUEvvq3X2hHhxw8RlsCkdGcWfZA2G3J5mEMRMyzS0avwjcGXbpF7Q-393PwoD8Vmcz3hxHAifDoA-X6FQ7wV47GgSN7RCsUB24kc08Uyf_t55oyZiFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
؛ به نقل از روزنامه SER، جلسه سرنوشت‌ساز رئال‌مادرید با نمایندگان وینیسیوس جونیور فردا چهارشنبه برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102730" target="_blank">📅 01:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102729">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIduxAMLLer1pFw-iYn_IuSXjme_9NizbwZG7Ucmt39pYiT7oI5R7AK-eK8Vks8NqQq2ggukVp6fq7z8crqbLpqPVGFv2QfrLXmt6OC9cMSKsYfwmYiIxRvPuAfNiypBda5WtXowy5306DXiJvSddZV4cq0b9P4kwgMbLwQT27a4iX96t0iKRyoVp-jAOIFFAuOkQJDmO7kKfVIJBqJ3WQDqsAw8-xpf54uWU_ez8w7e8yL2LcMbkXzoe2uOAb6UFKOg3-r0wWkV1vXtisXzoSyAux5L0gnhhgXQPBM9VAVVCX0IXqykWBmXQD00siJ9cAuCPLghNSEUS5D1ujq1VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
👤
جوادحسین‌نژاد در مراسم رونمایی از کیت‌جدید تیم ماخاچ‌قلعه روسیه حضور یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102729" target="_blank">📅 01:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102728">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkWwG8hZBhS0T0xr6zb2lEpWBhJ1r7m9U8rr8wS3R4gxMjeY8_EEgwhzsB5XvlNRzp9dTRZnBKHqyGS9Cj0yahe4zgjmfbvwBelkyaUdkelmg_uxQF-8r1LNxjdkegj-6LRvmxiMP7NH5KntR046y_ZSBW06PXm0sSVux1mkq-lSX6jjumRE1c_lferNnfXefoCTKOEMoV1Cmw6NirZhidEj_1WKgXkFLrWJRa-z0p9jmp198S3OP2zCFyoXC2lhpz8ycE76Bscsu77WdFNOy_cWlzpJuCsEmpGAguJOX3GByqEZ7FAPcRq-GYVtaawOw8bneehXYFRQmKt_W3lyHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت انگشتهای دیدا در مراسم تشییع بارزی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102728" target="_blank">📅 01:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102726">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c707c5bf8.mp4?token=qDVCVAvLIgz7wMiO-vDms4s8talzLy6olt-ndeFmLBwZBS9POYIJofYBGMUMf6ZeBrDTKLbGNEO0M8XSLT2F6chJvzGPt0vXhIaT7CiGL7nvr5sTgsG5l_q_jG2uEt-R0TJy80zCQtGX7S516_z7w62lQLKSNC1F6oxZo4F9KCmDKoiacIVAcQagdDON6u8KeQeQo2I02V1TwT9y88zoUUkhiRnP4RMCSAZ34HUG9qNqzPYqM7VVnaDDeIedbFSCH3CjSzPXEuNZ2f7V2efA-YPoboBWxDUkPYI_0podlHUNSNA2MMc0Z7jEBxmoJ6FpuRRZZgtLr3QPrTo76GZXYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c707c5bf8.mp4?token=qDVCVAvLIgz7wMiO-vDms4s8talzLy6olt-ndeFmLBwZBS9POYIJofYBGMUMf6ZeBrDTKLbGNEO0M8XSLT2F6chJvzGPt0vXhIaT7CiGL7nvr5sTgsG5l_q_jG2uEt-R0TJy80zCQtGX7S516_z7w62lQLKSNC1F6oxZo4F9KCmDKoiacIVAcQagdDON6u8KeQeQo2I02V1TwT9y88zoUUkhiRnP4RMCSAZ34HUG9qNqzPYqM7VVnaDDeIedbFSCH3CjSzPXEuNZ2f7V2efA-YPoboBWxDUkPYI_0podlHUNSNA2MMc0Z7jEBxmoJ6FpuRRZZgtLr3QPrTo76GZXYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
فریادهای مجری کشمیری تلویزیون جمهوری اسلامی درباره تنگه هرمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102726" target="_blank">📅 01:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102725">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNpJZqh-71Y_RNELI7-oLWqZkbIg4-ORp3lDRrCWyn95h5TH7IwU1eTubl6Xie0N-858o10YTm9Lo57juTAAdHsBTjTl2ki7nEL0rHTe9QTBrBRN6YMWmLQnov-lIL7xqMLZ7Zi8BvIHhCz17zsOxqS_3CvHaTJRr0A4nihPFUsyMJ3THrvjsT_O7s41LXE2_yrPo8TGXHyG5nyex5_avt9Klsp7VY8918_czMBt4UKLu1LOVF9A8ZfJTBRAucP9SWviwsl6pkH7yOq8FiRXIh4O5-dq13GS_PcFt89nnWL4DAsNjSVNXnJ09RnnwJKZ2JS8e7TX-eQfM9VB0ZFT2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
باشگاه لیورپول درحال تلاش برای جذب ابراهیم امبایه‌ بازیکن PSG است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102725" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102724">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
بازگشت ستاره سابق استقلال در آستانه بازگشت دوباره قرار گرررررررفت
💣
💣
💣
💣
https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102724" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102723">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AGYJp6X8tQOr2oN0i34tPtKIF8jNqy7WnPXTwhmjyDXF7RM-sdiqYHNsgrR4U8vAgwxL78JoMYtHymc-WLDGxAzKjVON7f2DN9Jfgr9626QV5nSG1R0IXuEclTJdEVMosBqkPRu8cmiyuVhTJD1RqWLnRrePMk3M2Vy_gwef8WX-umuRM1OEtojdhuqum4rOlN0A0VgM6gzG8iGDWB-24ctV756YkpRez7VvT4mrQn03PfIAQLi37TaR7-VMib9i5r6PSOQi3fl1mPyy7YJmjqR747HOddvwZ3M2JCZJQXWXI5M5oHL3uCO-hdoZqdvmVeSn1mc_08cqhU-RhRSsSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازیکن را به استقلال پیشنهاد داده است</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102723" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102720">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PjJlm0b3mfvx2jfqDzGjx--9LjMhHE1gQtC-pL4SBJPZ-VB2Ke5CFw8MhCnVyOsyr5rnB_xamL5TgAJmtbRtRKmAnz1EL1bInW9cY56LjcIX7B-s8qamC4Om8T4gSLrxyWqXnk5gIBWH0YATE4uV1xqDWMO_Got3MJxewncCKNGRAXvg6q4W9VcmzaRC3zqMseWCZmu032o2MY-Wh6kGD7xOWserJR1h2pCVOb5OJpBEEZmcpfwnzVm26O5JdiNLCy8maFVWy2cvCSVGUBlPFBG13D8fn0LcP6ZwtfqAIr_L-T13SBllpGvoi-qVQUdJ1GSUeqfrv6IybVs49IcRqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WCKm-SV_fTUuKbgmXEh2i4JPRNGl8T3FRYY5OQzQGUbdjPEcBCiUexAE72OEeLKI-kccHCRQhtYxK6tM0TonNNQrSUwYbEleSSYSeNMlOeoSYTwDeKd-stNIEw7QapAHhQyzP7nIOmoiaihg-2mEhNiDks2twEUmm1cPouYTzpbgm-jtvitx05QdF-A96v9S09iBBR8aSq-0vpA8B82OwSjNzpDXqwwlX3_Pz-g6eo2mL1a2qpBbD_PmFKyIa98D_iBcaiRU2dUTD5FOfQFHDdEuUxMwKyHTmSDrE09Y_MsZIe7WUQOvR9IC0s5YU0ycKRdeVqRZedQU2FxLLw5qhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t5yfs07bj2EY0VeUsjHaAiLhb-8fgU4i0apb48gMT6AVD5Y6bMhtNFiDg7ePXS0iEjgiSdrc_T9WBG8q_1TqmPeF52Iw2Dax4S6qaVgbEqPWOoz_dUY7n8-AV1YUWrJKJSESZROy9PpfHnOL7OyhD7BMMi4stnxdbjh1lckhGhYfMKJW2qYJgpvUlRCLwqV376wudcNM70TJOXJwY_C4E9YwrFXqqZw0cnQzXpuzRVzByNfDJ5TRjYG6sK-5X4HGNZqdcsHeLZVNamsdLefmWB3hF8hAEFSWDeXbLkTjmW3E_uMqMS6lDNy7KMwXhWtcufSNLZVAzanxSft2474VnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو اینا رو با کپشن: « اسباب بازی های من » پست کرده
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102720" target="_blank">📅 00:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102719">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZR_p_Sp7boerfStiVUIp7Q7RnHf6jm8oktweZogMySCRai6hgtlxoJ58oOG4NU3h5Q_LesCxjL5b7E3RhuOU7H3GMwxKZ4CFj3dpu2MYNJOZDoho8lxSgelpwjSU6yxbznSwCXiCwM7x1bMMdOxrC0Kh4f7bwfTmtI7K1aJ2emIH1bg2N1iDL4Fk7gTyif0f5mlX9O3jNWegLCmKs-yZE19qSdi2jM-OLJYU2bYV6NSjnjf_A8zo66YfgUu3YAova-dd6QUiF2INp5crvMJBxJ9s6leHJpSA9qlbuAOrS5-r2YyZhjA7diDOMnwrpbfYmqe0M-b8F_AGFEFmb1yvSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🔵
۵ سال پیش در چنین روزی؛ لیونل‌مسی اسطوره بارسلونا پس از سال‌ها درخشش بدلیل مشکلات مالی کاتالان‌ها از این تیم جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102719" target="_blank">📅 00:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102718">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Shlb4VcMJdEmWqB4Qxr35eBPMLMRgVz1HhPKVl4ZeqHoiytzxz6v7RUylLW9n3sh9TxXYNBKFw4kONdtmvhP1xfAUN8_IPwXgunJIGrzFGu1T6GzzH5NQzSX5bG0jjyCEH3eKApdgEryh_MLNsHS13qEtCGpjF2_4-Vc1NmBMyEq2AwrUsOklKLveAG0diRsXaTlsFWh9nTmIcKYLSGFHZj0_KNCJbD6PynuLI7tDD14h40GNRZdGsg7UUEJO5W3lR9_LwDJEJUJRJNYcPKqEuIOFrIDZq2ZPFMGSEqJtzEGtrPLGx4L-oUvV1dV-Zizw0g9X5m6pNfslv45aBnmNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇹🇷
فنرباغچه ترکیه بدنبال جذب پاولیدیس مهاجم بنفیکا هست و برای این انتقال باید رقمی بیش از ۵۰ میلیون یورو پیشنهاد بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102718" target="_blank">📅 00:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102717">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aa0swhkGZ36FrnDCek0i3Vo1lWyLDV_ZJ76w3mjnS5KJ_cTtOA_aIcztcpywGp_CpKhJPPS579WMg_K7ro9t3oNnUkmkQQfxFoysajEeVfTGE4kYDcek_Pz7jxkNBUSJIjwWAi8okgj0MqqqeueglbSuyRSPG_RzCnVAo-nUjgwW2rx6duF6gFUq62ICNjpwxsyayBPveF83FhZhGQlrdQE2gtVwOQvGK81T05PcDjx9Wiec8qXDkFqrPIrh8sUzCzQ-O10qeH4-9g_YS-YBvW7UBZnM_FSkJ0nht2iBAuMDnDOFWoG4wpiTkasBys_cLQp4Mn5rvLYvoINAlNqSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102717" target="_blank">📅 00:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102716">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jBcU4h5NbcFU2_4PU_zQNQKFWLnmjpox3OwbMbb2xoU6JwcaNyHMJJcxemS_F1OGQSpXCizF_jZpEvZS76wKfxw3xTI2NUkRxLhNzZeHm56epwWZOomKZwtfkI40MYNdaGI06dFMDVj7QhMRXr-1bS3zwWF3Bb3R2Kdnic4IBWo5f3sOykM45B488-LmTmFu0FhA9tKV0yhsPmwrRA5iYH7GESmbmjj1DhxQzzC0AUt8CJgvwb6koQpJwDZyvkTHiy3qQ36gTpOWbgqWUn35cz9tTZigrA3aDVptqGdd4nDFgH1Q6lAccloQSBo8qeYrHSFjXKBUXp9Yj2Wi6DbH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
جرارد رومرو خبرنگار نزدیک به بارسلونا: امروز تو مادرید دکو با ایجنت آلوارز دیدار داشته. طرفین میخوان هرکاری برای نهایی شدن این قرارداد انجام بدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102716" target="_blank">📅 23:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102715">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqLUoZMWeoodAKZq9Wllj-KfrKp5ietFFMxfx_d6fTptvHa-re58hUOFkF69Wnm_7fU1ZqP75r7DHy2EPoY9_rK-xgjQMvfNeBt9suhFcU1sBWq79xMFF9w410_SqJxwGCM0VQU1loMepFalP1m_JW6kbXGv4sg5IUJF5qq1JkIXCUJjWLUL9QezomY18MMrn2xMKYg717kFYI3HAyXTw-2stYRlAN7g7mN3H7mzBVwolR1ymasEPJDrfinZPjM0903XQbMu28F1KfWqlhFU5CNGlDFY9JgGJNBFfkffWCQ2AchHuuRZDvNg99GEVj3xwXyXSgXILfM_pbS7VB5kZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رونالدو و پوستکوگلو تو تمرینات النصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102715" target="_blank">📅 22:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102714">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_0GcMdLOL_kohPy_srjjUVN_XzzILUm4zrnXfRutEmsTU5FHm7-0E0OLBJT4PdyZY091d2d65xKmEX7ay8b4rgJlQ8o3-V7XcI3ZrxwD11sBwvphBihVgz4KAU1h0plLdL0UEv7vScrOX8IKcBfxCzhmdUwuf_RuksDsJzrpNVdD1xviiBnPBUgHv55Q5WBhTJi03VI3EUca6MPB1KKi_SHBewv-MTavltwT0rEYft2_WYEAjiTfrIXFJszSXtRtbPC4lgKCxEKbsVvahG0A28tGW7o5bS7LQ05OSKcC17UI11AgODUXIg5rz2dzY5aIzBpuwObV6MgRrTryrT19A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102714" target="_blank">📅 22:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102713">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3689824738.mp4?token=YWM-3aGhttVM-1FRaFn_WbZSekjMaMn28WlKJbWPjKw8ZTtxwk1_mDyQn7f_cLBPhrFjVMJXpwO9gVnRYjxK_eUuhUH5oEr17Xnkoi5Q8AhvUXIZXUvpgNcaN2TXJcQbIzDHNEYj9D_mkSeVb__f0PM7urkU0zplcu_20v1PK48en20V-ZsmfqaJZlDWP7qz5zbMIznHD8f4GJZzcYD9mqvnlkwmecnzY54KOKAbHk9qjhTWnG4cXjHA-sIAF-arK3w3KM3UQOPGiiHEKiT1y4xQZRtQU5nwIWc4RXXOYdkHnq2LSaTxMfGxhbS58JKdvkrj5wL5LR13ykzGDvs1iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3689824738.mp4?token=YWM-3aGhttVM-1FRaFn_WbZSekjMaMn28WlKJbWPjKw8ZTtxwk1_mDyQn7f_cLBPhrFjVMJXpwO9gVnRYjxK_eUuhUH5oEr17Xnkoi5Q8AhvUXIZXUvpgNcaN2TXJcQbIzDHNEYj9D_mkSeVb__f0PM7urkU0zplcu_20v1PK48en20V-ZsmfqaJZlDWP7qz5zbMIznHD8f4GJZzcYD9mqvnlkwmecnzY54KOKAbHk9qjhTWnG4cXjHA-sIAF-arK3w3KM3UQOPGiiHEKiT1y4xQZRtQU5nwIWc4RXXOYdkHnq2LSaTxMfGxhbS58JKdvkrj5wL5LR13ykzGDvs1iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
یه سرباز روسی توی دونتسک اوکراین لخت خوابیده بود و داشت افتاب میگرفت که يهو…..
❌
تصاویر مناسب دیدن برای همه نیست.....
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102713" target="_blank">📅 21:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102712">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVgp0G2iaF7VsltEvQMvUE_N8D4ID1r0PK9C5EsEG-AJpkr4mgAriC_Lk13ep-OGmFNiuMMVsFUa9FSzZ6mpj_RiG1ccUB2h8uQcNqeLE-LzKlmGqlJcPqoEPqHrJLizNB645KooEZEH2I6HnEzcSnTHv4OjovCo1-JPDuoniRY9XHlZRq7FtVnG3ri9u3k_tiBOwyaUJQo5qdfKrbmtPj6QyPvaklngdB2vyr2K-QrDjV_INflWbC5yRzmq3zyKZcWDwy6UNBF00T5EpTFKOmKRWpx7dDp1RbUskIeFJ_u1WbFnV70LwYT6-z3acM4GGRDFt3gJ-2BJHGoxA0LPGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدری از پسر تبدیل به مرد شد
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102712" target="_blank">📅 21:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102711">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qm1T9OlQ1qLcExXzV7_H8ir5bI3HaELiNqywnx-2-WaARVyF0l99CZoSofR5BA6HmYzMqwG2PnyatkUVfU8FfTDvyswDoRlWRYoeuaj3c6NBnQ13QwY1cAvZNtagTRaYloRPCjTO_o-Bt4_bwDAUsgxKlZl73Ihk6oqueFobPz-wWyOnU3lc-eEWCUrd7jjsg-c9HPixyPpgJjxKmw8b3r0lkcJqMsY2ATSc-cI6OkeiR-LIPprnzJhxjCmKItls0hxA3fZSF7o8bQsx2LsZ0xqBSsHhETRbnF_W9I5y-EijIeziTMEgb-o41namFI9ACrE2lbcTki2nhZr1oTSiAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل زده در 10 فصل اخیر 5 لیگ معتبر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102711" target="_blank">📅 21:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102710">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGbss22HQIO-NfJbAj_o2N02pz6oZ8MOPM2x3ZKrtdaJ4pI8bFNmWAnNV3T0agunFLHyThk0SNFIoYQKvMnsaCcxrEShO_XcnMffMQvoEyTi5DLDH7HAu6OC5ShSdKZQ92z5JXr_p0SBH4gIcmsRM6J05wHOxfsiAEkett0IZ7bycn7GhE9bppP7ogPAK_XN0sRP8m8TPoAeNhSSax6k8h51Dl4XiZq67fyfrW6JBFktXhTjLCjnaKIjaDAZGi2xMk3SA2959t1mEe8J-wTyTBRxhHYhmpiXa2hrUbuTTltZJE5BcGOIeGXXVKOvqAzDK7HYy1fFr2imnOgyYuqKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
رامین‌رضاییان خطاب به مدیران استقلال: دست از اینکه منو بذارید جلو هوادار بردارید. من حرفامو تو زمین میزنم نه فضای مجازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/102710" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102709">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVHn_OBEXG-00MjWTapJMIdAd-8snc0jFnOtJN6CkCgQAzwNIZ9G_FelhrFVekk6f9zDpn3UBjmuTnXo-7JloaIB9LDYNuN5bhCkS74nQcERRvawwNYDvbh8M3X7Kx8dhV6xs9dLbOapVyvC0CZFmau42O-hw7KCGn8ouldmPLWs9xIpHTbHaJ1LXL_jKe8Vmm7q-6wBNpwGEUK-BGtoZ7nGe0r-LpfGojbNANy2t6bRMuvCzYhw2qELOzgwohhFMlruLJuup-Jn1mQz-GSgQcPKmLzM09tztJ9UNWc7qiGU1XJYFha5m9S-QlgB8_ND0aTF6E5MU2Qsuqg2J67uxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری
؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/102709" target="_blank">📅 20:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102707">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFu7Gxg0rD8KmL011Ho1qsIU3UZ0EH_UhgsnsvisCjFCaNlloigy6xfnBWgvCJXDKfqxh_T1wwDbg1F5PU1Ut7BKhycscod9mj6c12_fXtuYrgmPIzHG1EWGe7lQsk-uEov8fFKJ3QJe8puUPah6RAKEvEUThR37jcx1OxEVsDPHFXnrdjwOfCU0S1fMcL53TS8SYsoyKEtRUCKigftKWUcliTiyRrzzNT0gWbhhQjFzFe25t3p7hb2Urgwo3n0wjZ5n1Ngzu7lJF6Jvoit5ohcs4UmaElsXTz5v6XdNhNbMK_OG1ugu9OPaQmXS9atTf9lL3_6rtzlnUK5IyauFAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a_AtpXrDGW-_DEYHj8t56kCnQyOzgU5bYU6auUBWjO7sL9g1i4TGuaun0hJXduLQZHTKffV-xZIW4cbb1EEUwJp45PRm1YixDcxqii8InbH0di2nzxcyi4CkNY2TI5OciH10NNehtqdmhMq8kViRWOrCMKKnD-7k2-f9z2oBhWUWJi9pyR8r-hPjRuiwUFqdsDNVmQLJ6-HACHBw0NgZEKrDiTIVK7nMsRBt10OsP0YFMo1hn_FmQhv6OVBG7U8eCPWPgv6H8YsjghhVWt7ktGSbctVO0b_kyFDrrVymNwbzch8kgNk3I3Z4x98P1H8sTO6IVU1mvBm9YstQXp50zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
ویریجینیا:
من اصلا حسودی نمی‌کنم. به نظرم وینی جونیور خیلی هات و سکسیه؛ اتفاقا باید همین‌جوری عکسای بدون پیرهنش رو بذاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102707" target="_blank">📅 20:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102706">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSkMqGakTZTRPlApPIw9HLvuGCwp6Qqsh61sI-wmgZmgudl4MKFizrXsvO6aenTzXqQ27khbP3O5XD3yZu2y-8eKo8FZlN1wZsauVuEU3A9NFzBLYIUVQbKQ6rO8a25Pb3VY9IEsUcY6Hcz3FcMJ1v2zLTYPAy_wgtOl5vrCyX4UFc92n1YQb228jvYEBnb2Y3nWDtHwfss-VOFAUP5Qv1nDL72Wv4qLrNrXVIbA900ffAKOL2SZ2KYuscTabS7_NYV30tfVaNcMR5ZKa8MqMzVoMWGRA7FOy-tgrUONvWy4gKVKwEefQKoKHWjS_v-G0nFZY1WvyZfTHnf3PfQVyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
فووووری از فابریزیو رومانو؛ سیتی به دنبال جذب پدرو نتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102706" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102705">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b139a17c.mp4?token=TNFG6kH10kKqb4pzEVwDYy50dynrK9YCFpIKdGP9WEBzgZP1Qfmyual8W7cxklTztVre8iYMRNd-rxPuOqQtWoNPrFXACWRQgqIG6lVwF0E6-QgHBMCtpPNe64Repcf9D97GIp6GV2dMPblsjzcWw1biZrTmiUK6MRujOHPWK3D5jR1JTuct0gfKGUtZ_4VMEOCZCIMtPX1oMeEIVlNiDRjWzgoJbTCAFenvQilbSial21n1LMO3q_WVINwPb9dCUIvhNoz-LUcimBtIy9Xjrdv6lGTmpk4zm_prcGnN0TZ1ZOVrG4-_rjLjDHxO3DQRMgBR54W-Ij102nCOAKzKoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b139a17c.mp4?token=TNFG6kH10kKqb4pzEVwDYy50dynrK9YCFpIKdGP9WEBzgZP1Qfmyual8W7cxklTztVre8iYMRNd-rxPuOqQtWoNPrFXACWRQgqIG6lVwF0E6-QgHBMCtpPNe64Repcf9D97GIp6GV2dMPblsjzcWw1biZrTmiUK6MRujOHPWK3D5jR1JTuct0gfKGUtZ_4VMEOCZCIMtPX1oMeEIVlNiDRjWzgoJbTCAFenvQilbSial21n1LMO3q_WVINwPb9dCUIvhNoz-LUcimBtIy9Xjrdv6lGTmpk4zm_prcGnN0TZ1ZOVrG4-_rjLjDHxO3DQRMgBR54W-Ij102nCOAKzKoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⚽️
#فوووووری
و
#رسمیییییی
: تریلر جهانباز FC 27 منتشششششر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102705" target="_blank">📅 19:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102704">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OC4R3alSbwytMcRzy0D5HA_aNz7fOkLh5JHGTYSS7AG15mplPCvxEJTBkhIkQASaQwMHg_d5HfGKl3iQUCxLLrs30HXpPdSSBw3T7S0tFcE70639fd-aecJ8RO422gZLZCaFp7KWB_HG0ZmkGwy-zRefqQFNs7NFYnRUYqrBZlVgPu41rEMLIC5u3LJxftigSfVBSBi1cLLvpF8Uq4WIZHeGkl4pdTR8XG3zSuGqlfN1hk0QHK4h8zeZqdFU7PyuH6nW0eYL_v2MJx3YMqtWOiYPT5tioTxUM4QapmrdGvNcfXIsh9wVJxW5Rdk_7Ocg9-S3jy-woRYM9yNoX8ZwGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
👤
پست جدید خاله جورجینا در تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102704" target="_blank">📅 19:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102702">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sDWQ7UwvSoNhahrHAwko9Kq3IvctCHsPdUZMmkwceyGPE-sfIs5e7E4cdGban-RXNaortKJG7lUBRmNyaNMoR5phzaQdtu-N107jrJ6XHnqcXEYoupYfuMVkaDCJQ31FZI1OwEg5ERSgDVWAnMqATbZpjbMvJJWghcP6fLwujdlqjQr8qcsEfdZVibeFoA7qof44BGZu64GBE2MeOPKiXwdAE0LJByXXsY7XokNr286DJ0VNbBn6wAASX6xYeHoMQZHphkJLe0l0G_CgFSFc7UrGm73hEMO9MhRBBLnHIXAQJJIPSrSPcHGf1CXtwfcd5Nc1Q_LDaO4NptqZU2ZDRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pqEBdt2oF6GRyG7HhVTI8VEa-Gq_1kGRjM4J81jUR9JIfEHL0e_YgKR0oQAoUCHu_pqe4waUOb2HcbV0kVsdkgjoTPqRbYh3V-juj0N5xvodwv_pTq0MVJ14gUYpwVe-IW4TLaPG1W-Wb54eMoiuzpXIpIgsqZs-YAcwcTa6KSrpAbghZJZn4LHOkb39uGwdd2Px7ChuIZqoY7adAVkiDtdI1uvFDPNa0alBWChhyFxmxpydrGeP8mG84q_sv97_jz2FKpla29A6-BQyuk9OseiJHEr_1J-IrjmGmHcwB2Rfk87xhqraGrbMEalbkz-rvmkTeJMf1azpHZLJ2oilfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
رونمایی موناکو از کیت سوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102702" target="_blank">📅 19:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102700">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94b7db1a6b.mp4?token=Q-T3Jb_zo5O6pQTyRw6HJ7k6-lP6buPYbWY3hdfVF-f3sm8KaAnbbQwTdz_pD5rhPOyRXgoilPTGTnsHpJJb115EQ1hlB-6AKDm_paqBJvSc--ct3JvZcFxE9DBNZUsj_2rXmD557ktUgFAjhJIM8sjbPTuG51dKM9Xnllxij7JTEU-FRXXl_-uazgXsmzbOaTey_zJuXBaljucowecixn1E76pzidRccbjO3iyDk5A4om-1uFH5yd1rP2C596ofTSyHEJD02K3EjPHwgF9eWTj3kJfkBi0T4IysuHo6KZkH_-sfcbUNPB60zqez3UxQUyKnSdmVapl0olsqFgGq_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94b7db1a6b.mp4?token=Q-T3Jb_zo5O6pQTyRw6HJ7k6-lP6buPYbWY3hdfVF-f3sm8KaAnbbQwTdz_pD5rhPOyRXgoilPTGTnsHpJJb115EQ1hlB-6AKDm_paqBJvSc--ct3JvZcFxE9DBNZUsj_2rXmD557ktUgFAjhJIM8sjbPTuG51dKM9Xnllxij7JTEU-FRXXl_-uazgXsmzbOaTey_zJuXBaljucowecixn1E76pzidRccbjO3iyDk5A4om-1uFH5yd1rP2C596ofTSyHEJD02K3EjPHwgF9eWTj3kJfkBi0T4IysuHo6KZkH_-sfcbUNPB60zqez3UxQUyKnSdmVapl0olsqFgGq_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
مطمئنم شکیرا ومپایره مگه میشه آخه تو 50 سالگی اینجوری باشی و با 30 سالگیت فرقی نکنی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102700" target="_blank">📅 19:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102699">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd0cef8d4.mp4?token=nY6z6bIMMCCwBR1WQags3jLc1f4kwlq22OqTYcekkMXR2YH0UxGYr2GkMHsdesAqEsmkzeZ1LgmjomQ5-xkK-eGNclI5otq9lAJjGAehgIeQJbKsHHGj6Y8t6dJdJnADvpqaDBjx9Gq_q1I16sMdWqa667uWsquEk0ZCw24sZrM4BPBDwck-4TDQIr0-3MXpIHzf46pcPsp5XBmdVvwugiduSwhjOhlKujNAC3WC-D6T-PgfkTK48kLJDj6xxdGdtx-FDq98uIovyxmubwLR5KgQ4AWNyaWlDDyzOXVqviiY-x_YshjdCM26qxa-7M93AUqTPKthA4BuPc-PURLYlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd0cef8d4.mp4?token=nY6z6bIMMCCwBR1WQags3jLc1f4kwlq22OqTYcekkMXR2YH0UxGYr2GkMHsdesAqEsmkzeZ1LgmjomQ5-xkK-eGNclI5otq9lAJjGAehgIeQJbKsHHGj6Y8t6dJdJnADvpqaDBjx9Gq_q1I16sMdWqa667uWsquEk0ZCw24sZrM4BPBDwck-4TDQIr0-3MXpIHzf46pcPsp5XBmdVvwugiduSwhjOhlKujNAC3WC-D6T-PgfkTK48kLJDj6xxdGdtx-FDq98uIovyxmubwLR5KgQ4AWNyaWlDDyzOXVqviiY-x_YshjdCM26qxa-7M93AUqTPKthA4BuPc-PURLYlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره خنده دار پیمان حسینی از عکس گرفتن با دخترهای بلاروسی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102699" target="_blank">📅 19:31 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
