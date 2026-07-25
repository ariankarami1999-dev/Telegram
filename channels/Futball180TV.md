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
<img src="https://cdn5.telesco.pe/file/lPPj3Uz1NJAeVo7XfA9_dQ324LgY4skblKOo0iZHnkptENAGm9d90488XHip2pe6ZYtTSYVwO3IDZ4V_DwuR8NqrokR_Aug7WD-9lItvseMj42ahsSfhmQDEFnu7n8YIpxBJ-U7_GQj66FmBXMsrEgBPGqLQyuv1V3JxzmGZA6WHuGDYh3AcJW6gRnzzdToXnx0XOh3xk0EvDqOWlpgqDoTSG3SlTyLCn6GK32w53xBxdUzG42aPmEjIdIdD2TeALBOcRYKzBIN_tnS92CQirfuThXcZy9QZ2xULJjaZx-ILIkpY2jNMz0VK1HJ-Ff980GBezI7WabqgB0TXm-tJEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 529K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 23:36:33</div>
<hr>

<div class="tg-post" id="msg-101948">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iase3SUsnKF9pZK9CAR4mKw_WjXGXUqZfqs4NgEtpIga0eNdR-E7hRC2icmNbIhijB0sOZ6owOb1J9tkdSse_fQeIpIMIhAxCnS-nAAvVUSVAJCPoUmUtFmC-hVP78U9TanAMoFFzRHL5STJH5KzQX-QiWJeNww-M8yTyaJUP84DcFbR7bbwu9-KPfCx1OmQhu2KJK1oMtdjahrBRmLf5iuVfIiSVBRjTxlnjMngd73Ly89VTkQWdRhhy52Q8o1m1sHANTUK-Muf4Av9ONVtRNaVmwz7LkHsmPi-exwU5QeQGACMyuLUBrmKd9lXp7HrrOqRD_PZUI4_7Au03taVWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔹
ساشا تاوليری:
باشگاه الهلال میخواد مبلغی در حدود 120 الی 150 میلیون دلار برای جذب لوئیز دیاز هزینه کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 303 · <a href="https://t.me/Futball180TV/101948" target="_blank">📅 23:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101946">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fj2jLjQTB8BAbMknf3BnvQ1HwnN4wFmcVTz7FQHvfszlArE0fE0O4MyETzoRCRbFoyV7lS4ScDv2XezmAXNYkByTmjo_OxCmpN6R8WxWV1VnCwG8IW9m_A8B0Zp3wvVld_btEpE8ovtbznRErSvLXZUzCoor0BQJvec1ytAs1_pH71ZMGakOnydz7YPNtpsjuyqkpp_9PDclBYiTRp_yiG_LEcgAiXfGXuMCm0M_MyHmVEQacrKheFD3VW3LKp9TQfEJmNMaRifISpZxcdA2HtbL13W2U-Cq72pVERMVqd2-jemfx3Q_xtj1j-WWxSaRrVusNBTE5GKEAuLvvjnBjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GIKUiVkg-nBAtrOrl-xkkim1iYVli_jEg1CDqO4P2cFe8ion9jZJPGK0xCUYE_q94EgWMvlsBY6TBVv1mefWDVetYhK2OI8EnflmyrM2bAlSPZBzeCWI6uirS5xSD64vefwA68u-SIApCg_FBcc6oxA2skDAwJuWCnCZ8N6hfEP53Ewp0WHz61MioOE6gRA3puQ9hTWt-gD3rlMOHoe7z9sPJiL18uPjIYoMFEriaxPLsmW9lZc4TuUen9RnnMfQEx4RPWdoSOr9-98uGBLiuu_M2m6PPfDfiLByLz9o73AbToGAC4djfrlWsi77K4FEcStz0UYL2UF2GgE5jfXsHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
سرخیو راموس درباره اینکه بین کریستیانو رونالدو و لیونل مسی کدام را انتخاب میکند:
برای من جواب این بحث خیلی ساده است؛ اگر فردا فینال داشته باشم و فقط بتوانم یکی را انتخاب کنم، کریستیانو رونالدو را برمی‌دارم. مسی لحظات جادویی خلق میکند که کمتر کسی قادر به انجامش است، اما کریستیانو این حس را به تو می‌دهد که فرقی نمیکند بازی چطور پیش برود، بالاخره راهی برای بردن پیدا میکند. چیزی که بیشتر از همه تحسینش می‌کنم همین است. استعداد یک چیز است، اما در اوج فشار درخشیدن چیز دیگری. وقتی کریستیانو در تیم تو باشد، همه تا سوت آخر به برد ایمان دارند، چون او بارها این را ثابت کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/Futball180TV/101946" target="_blank">📅 23:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101945">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdSRXUeHFLHfSm42UAeEfXi_pixIRQz_HiVBja2x4g5QIpCTZsGNKPTQteS92dn3M8-ijQVKOS5GUj3Ov--X6lmzxCaInOmQzyVqMvcgoG1KjN75iXjyP556qlIVZl-p8IHKionGTX4mr-V2wu-IvOPtZSyCWwu0-NXnhW4Wf1Cjaejb4aTfeO-IXoaAy8iWUKJNg-mmn93hspcb-8RSGl_gBFMc0s-u8Nj5xLwvXYoHJA9uRgdcrVRav2R9VZBIaRlC5_IaHUE1eEMrmytSnU9sqPyMg9PMZjk4UrZAJb7WpzMKrqyhGlN49maj0vY9gin2fQqjy77oQMmK0C3I7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
به نقل از فابریس هاوکینز:
مایکل اولیسه تمایل دارد به رئال مادرید بپیوندد، اما بایرن مونیخ درخواست او را رد کرده است. رئال مادرید تمایلی به درگیری با بایرن ندارد، زیرا رابطه بسیار خوبی بین این دو باشگاه وجود دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/101945" target="_blank">📅 23:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101944">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMEzxtJKITcaoaUwMjtBOl91qyEV_w_RPAnZacKMQcpQa0pyq2-021JnB9iu3c0p8HWLp_nZ0hzwleGY2GsfEF8gU91BufcG2MOT6PiwEElVLFrQ0Ta5OrFWD6Iol2w7fa5l0sMRS0OFqlIOsOh2qHCHtsxSB2FV8A8_6X_wwX8wbhyYlbnztcH5rbKghDJfIn_R5B4BvjN_hyo3MH29MncWYSae8cBLExORG2tgs6axQIaYxpQih12x8FAUBSMQUgMLwyxUiG7xFHviQF92g16Z3GLwdFBlSB5tU3gohpyL4k9GZXLYTJ9I0bMo7R9-EVKmeOdXfXxV6NQIL0b8QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو: رئال مادرید و دیومانده بر سر قرارداد 5 ساله تا سال 2031 به توافق رسیدن
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/Futball180TV/101944" target="_blank">📅 22:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101943">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFLvfnMp_ZzSb-ksco28JdTzobhN1Qm_Uw2qBUCO1u9LqwvTYMRjRGClGHZW1hw4LrxJFZcoE_pv0TV7D9y3vuI6ZAQIGt9yjmt3qBWVWrEy1TeOPF_IoGk2-vQk2bqmVnYdya1PWTVo10EaBTjVKgKN1ObpZvEfzFHBPmVAtnFqCD5PM8_GswFfkColsx56ZWtqs8QvurnHF7XoqydNcPk4MiRGtltFFLFGNXOoW8_zyJwpLBDMKyDS2j_ti1pB2V9giVlV713Le7KmYKM60lVhnEyIdJILSAJ1qOTjXLtusMF5hPiTE4O3p1qPFY_pGwB3UtSvpleJVswW18dcbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
رئال مادرید و یان دیومانده به‌ صورت رسمی بر سر شرایط شخصی قرارداد به توافق رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/101943" target="_blank">📅 22:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101942">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qxl-Nd2vb8Ya9fphejAUbJIRRWnlcyemCHtQ1mvAsvvo55Mj_gIMvouIortVMLuDh5V8Ui4aOVjeD7YAOJEJYvBRU7TJe1UdKQW6LPxmOBZ0MsMjw3oCJhcf-DujOaxWO7MZ1NT6VbJyuW-GWpzSMuyUqpDVFgC7-iy2TUqN2aeQhwZzCJuAG57wnvy-E46oB2cDN270z-OPQ2it3AoY7Tuorbp17nAvJZ4OdOdZSbFvLv9CqNFAHtTuqfLtHR_SnFC6fgBtWjCTJmoGyKTi11G2P5Gfh6KXWjpW46173K6hegdyeCCWnFNaTyDnjL4coNwM6XObjT2Zq74Q5-_clw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
ترکیب احتمالی رئال مادرید برای فصل بعد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/101942" target="_blank">📅 22:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101941">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBn0SEq9Ptw84nduwkMrmcuqjfw8nOtcsxM_O3k6qMRzBkzt2q1ffntA1ahxVuUTFRCoANdEz0yw2FURDdRQppDzi-LiRlMg6k3NCYFau5FPIUvd7Zn-C71fT9sgCrExnv7rO-XFzoeL2XHc1JxytWh3mga9OLXSz2-x0reuJuSMW55ar_r0PyVH7fCtc3nOlasHIKfF7MZGQaNGrTgQdGzFxt5V7CifiVf6k5HVvWitSiNupIobtNN4JjjNQOOly8YXGEh6Fj4B85e4TBX-GyJhzNFIPSVREi0YKaoUqpYy6QTEdNFTWMYy7wv7rX_ooZCgG02HXf4NEXOk7IAlmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از قشنگترین تصاویر جام جهانی؛ مارک کوکوریا قهرمانی رو در کنار پسرش متئو که مبتلا به اوتیسمه جشن میگیره.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/101941" target="_blank">📅 22:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101938">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cn2J9k4jI3P2DiRZ_pBfTxHEbarS7XX6jaMiyTok9RWI3LNyccvCwUIxRuPGo7Gy1DOme9SdcOJTccpxMI4Q7HGfRIOmksEWlfLkk5DLUi3Jd958GfFOxeCnhTiE9dimSk0iG1iiYLpPbmAFkSLXhbMi7xICKttgJTJ28QJ5UwuYgIJMhLjIz9ugYS4HdwMZZAlc8CnBjTD8wHNlRjUbmfYfA0wcvoxunauQimCh-GGmBRqs8eRp4jvKe4wPSRca-fYwLkZYg9JUXY2ImtxZy_dUhInXckXil2UX1BR9aQFqoUEDedi1Ueih_mF_qrdHTfig9Xx6cZlw8M6BkHNxHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoFhAUEAdkGEwJHpsk2Yq1ZxcsR_-BuGe7TA3mSz6oMsaG6AcSVjPjRbCGhAWGxfWXylj9J_U6x-ZkJztCU5KSrDcYq_No4bijBRQY-dnD-_CvkRateLMG21-eEbXbnsaIxJ4kRIZf-xTV6bvE5BmxwG7noX3XeoQIFrr2c5cT2yO8LQeAerwTsZqsggrPQoYeKIecS1fU1aqzgIHpPuyR51rb1xJwDSexytFOGUPn5UdQWRJuih3q-WNN8Q3OzIisVaxRYQ77rB89PxNBtttfM6W_D0t7QrHVnVAMmleJHY0tgCGkefaOF7mhXZhXqntrSluNIyhURYxubY_WcgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TML8hGT-zVAnuZlZuC-KgH3hHOMrrSZM8VMG-18lm9v9hS-XaFz73F18umG92bRvrMox7tP8i4HJGdP3ARrX2HsHpH_zL6YfcDzXIu1NR1zkJO39DgYuIvSURpTzsTfwJLQjbtzJcGGM01NRLALoLqgsfsiAlAmeIFmZtPfs3ti38QTKeVKljCRbty2LHXY8BVjnS_sK-9U49R_u3brLAXgghIkz6vcSJJaIkb7NddobME3eSYeNYoqaiudgXG4xvOoto9VGV17FUoBnN7mzd3R9bbfIiPMafPRELLpOMM9F671yHQycxGN8vFxvCsvjNr7RCtOj8YEPeN27Rgzcqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇳
😆
امروز تو یه حرکت پشم‌ریزون دانشجوهای هندی تو اعتراضاتشون ضد نخست‌وزیر هند، عکس امباپه رو هم آوردن و محتوای بنراشون هم اینا بوده:
«دیکتاتور امباپه شکستِ سیستماتیک را تحمل نمی‌کند. همین حالا استعفا بده!»
«۱۲ سال در قدرت، و تمام چیزی که از مودی(نخست‌وزیر هند) نصیبمان شد، نسخهٔ پرمیوم امباپه بود.»
«دیکتاتور را پیدا کن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101938" target="_blank">📅 21:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101937">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4HstE1qMe-ptgh1q4IL-n2xHl5Yb4VSJ7oAzzGeFw5NDfk4EnKnLBMJn2CP5IDVKG6bEJzOjclEuxojiXw7JMiaamDHgjItp4XMU-9HvkJrtQvM4N7VNAa65N8ctQ8uENJt1AgMrvyJI0IT53Z-kdd01n--OD5SQXT2FkeMvPHb9b5LyNFu_rxZsyv_lSAU24dCPZjLhrD5MKGNe_GRhooegtyehtR-RA1bcdV0V_-L8jZtdDkAFMgvqbPkNelzY5Bn6Fv_eKD5zpR8YeYN_NSqC56sHqwyK8fJMmKKW76EqwSvsnAcO4-eyQjwrryRCtikDisRFzrIfmN0O81kkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلاتان ابراهیموویچ: "بین این دو باشگاه، این سوال پیش میاد که کدوم یکی احمق‌تره؟ لایپزیگ که پیشنهاد 100 میلیون پوندی رو رد کرد، یا رئال مادرید که 100 میلیون پوند برای این بازیکن معمولی پیشنهاد داد؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/101937" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101936">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFi9fi27CU7rxX3BN2Q2ycek2OQNVAiPSO32yU27aoCacVklg8Sy7NcEwFr7CAxwOFmpUwBV1AEIYWHm9yTbRHPpBO4mgDQofCAzM6999y4RzJvIke2_o80vGs9uXYMBPAboiXKQy2lb3j90kar4ommE2cX-VTfjBvoCGxV7rjvM5c5F-L-FDcb5CoEq84ao-xDrIsFGABG9-CJVGWkcgII-woWzUc0AAdAfg-OnQNZVj2VhFVKbQ_N9OVitT1cMWfPKPLDFestn3R5es5UwawxWS79q79X2xsi9dLZYgOQ4zGFnB4VQXz1PbofDvsWFH6f9Lx-o90rpez4GBcbJXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
محمد خلیفه، گلر جوان و ملی‌پوش آلومینیوم به استقلال
پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/101936" target="_blank">📅 21:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101935">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUIG_lnhWsbFQbjy0CT7R8ps6irJ_61Cl5a8gGsM5Dgjsbowa3DSPqHLaXwvSnZ67zRwDZgDftX3nS_RnxNawuoJl5amiJV0x3N-SZMjQKl4uqr6-oc5inYR6l5Rg6ci88xa4hxrPvKHzFk3TUtPfS7k1MWG_ZgBQOv_zc1NUfcQivlvI6gi14zvm1Qmxdv0NnlIj7tj6qNtGA34YXWGIJkgewzmJye9l7eRex9_KvqXDsOz7sJek-628NFxCMWLY01R2mQ7t5W6DuhyC-ksRga8kwcUcYgkC75oDpw72uOuG3nI7L9unoNEcXgfmAuvzyM5EmmD0sOfmAtZzFs1yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ماریو بالوتلی:
یه بار زلاتان ابراهیموویچ منو با رافائل لیائو مقایسه کرد، ولی جوری حرف زد که انگار می‌خواست بگه بالوتلی بازیکن خوبی نیست.! منم فقط یه عکس از جام قهرمانی لیگ قهرمانان اروپا استوری کردم و زلاتان رو تگ کردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101935" target="_blank">📅 21:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101934">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvwBT41ihk7qChGWBU7-py6l0CluTN0AwpqbhQHjRYqu396odHvO_yB2meowFAWhSSAGnKrvKIC0oEYtWKQXzcTDNJdIi94IJVGr0PdrHL3rmZapFx9AFRPmZunzs49NA1FAHHru-HFDr4i13TwUEv8yPrWyAqjlzKcs_44WGDRpz9R7idjUF2u9oXgdF-kg_WpND8wOic9YZjgMZkn2yQQ665_1zXSRCT6vhHyDiercLsHL1I567HK0UuePLuqiizf4MvKnHyYtguyi_abljnqxbaW0jpLvIBMjBDuCVJpC992dnlt66xxvvt988EXD_o8RFBiLNalFsUswTLF6lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
کریستوف فرویند مدیر ورزشی بایرن مونیخ:
اولیسه به رئال مادرید؟ این موضوع اصلا برای ما مطرح نیست. او این فصل هم نقش مهمی در بایرن مونیخ ایفا خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/101934" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101932">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQn5CY9z63GkhJZyvs9NwuWnKgD83Abmqxb9S9WEKfpLDodLQN66SrcnsvenheOf50PGl7IwVtnkFloNLuaurK9fAfqTF9eu_OGr5jqicQWvbUPhgqjql0f4EE7epq0XhUBHg-4evvYF9bQHFsh_wgL1g4hBxanl1yCEYYAZ4mQKV8c2ciMylTQw2fOhMSO8T3Wn66xn_lAAyEUnh2DBVeQEtKBTZyV08YiLmBNdGUdHbkebJ8IyvC-D-U46ZEkxhloLa4ZdyPm-X2L35y7eMFQtE2BH9eWRYccyHS55Dhj9fTW35Z-RiAg-ODYIGy6iZMQiSSdDLwyjG-_nPmuPhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkSQHHOyIPxM3ZdWPE4dcOhPAFNQY1eDHxNBu3oUXVsTe9z5t1_7itga7bEdcT-om28cQdvpwLvt3JOPdvJwhr5e-a1SFiZuQ_qVy94bplKmWAKZcRo8bPYOl37c0MxxI6zWumODSfKZvOiTIOYo9_USUnGlp3yhP2dXJmzRQ2XuNnuXmKy1PjO7ro-7YTORQ05pjkZbYUxC_a3YpV7AzNUZIReeF_15HhWq9FMsY9sYnRsHGYIzrL72yETewa18RcOMxelmxAtmrjy_QQhduqX9n5Gw0KidZ4A_X4rN7TrHFB6svYE12124uox79FSRbM0Yc-FkoVsxne9zqFhXRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
براهیم دیاز هم از پارتنرش لوز مندز خواستگاری کرد و رفت قاطی مرغا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101932" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101930">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcpiRRyF-9D607XaBEjMxecDH8HJMR0yvxh5--6YrEcrfPasOth880aZ_j4PEOSNjlpfHn5K9wKI60HdmpVYwrLUM_9zOABZos0SgS83FYGGY4gTUjG30b-GDhsYv6xm_Z1Y14Exgs7XDA2cmNZkJWHJxzyI7fxzlaac84mKfI5f_B_OgWeg4izQqBSWqfNwOtyQjcVDq1TzElnhMLt6UR1kl6lcOVngWNMgIkN_sUOS5UrvT7g0UXX95tMzRcrdqeivurgWSjZVf9sBe3rNFKWJ6L87Hva5z482qh0UsG0htYwPPh0ngcMoKmUTimTjND-6yYwIaBUPsbAu9C4Oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2c2dac8e5.mp4?token=kjHJXSCz1GxNehkBFUkNlGxuznrmcB5gHemV6ttyuEv002CrD6EehbzMuZuiwq5AzAEFYFCBIsitP1RWSHk4AUJSt8v3lle5mnqHKakSHYoChTpuRQhW9hoK6PTLZUEBatPV97HUQitHWgUAWK2tvOWYiFoe2yzCxFz7Jjx2IYfDrfSk6_iA6nW82cfRlB52pBV4RuE4Y1XbwDqPnEMqKVjlHDLKGEa46EaryKG375TwIqP8ejiHgaDP7MeOvZ5DX1RBIQlK0F9YU6Vm5RRVjye4tbXEoi_9IXeiYe6dQu9X8hm8wP-aRqw0XkmWuW3ZAaGsohcKHcMuSIN4IgOZLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2c2dac8e5.mp4?token=kjHJXSCz1GxNehkBFUkNlGxuznrmcB5gHemV6ttyuEv002CrD6EehbzMuZuiwq5AzAEFYFCBIsitP1RWSHk4AUJSt8v3lle5mnqHKakSHYoChTpuRQhW9hoK6PTLZUEBatPV97HUQitHWgUAWK2tvOWYiFoe2yzCxFz7Jjx2IYfDrfSk6_iA6nW82cfRlB52pBV4RuE4Y1XbwDqPnEMqKVjlHDLKGEa46EaryKG375TwIqP8ejiHgaDP7MeOvZ5DX1RBIQlK0F9YU6Vm5RRVjye4tbXEoi_9IXeiYe6dQu9X8hm8wP-aRqw0XkmWuW3ZAaGsohcKHcMuSIN4IgOZLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
برگام عجب سلیطه‌ایه این! اینس گارسیا دوست‌دختر یامال، بعد از موج انتقادهایی که به خاطر جدایی از دوست‌پسر سابقش گرفت، یه ویدیو منتشر کرد و گفت:
من به خاطر پول یا شهرت لامین باهاش وارد رابطه نشدم. خودم درآمد دارم. از وقتی با لامین وارد رابطه شدم، بیشتر از چیزی که اون برای من خریده، براش هدیه گرفتم. کلی وسیله گرون‌قیمت براش خریدم، ولی اون فقط یه جفت دمپایی برام گرفته که حتی ۷۵ دلار هم ارزش نداره! بعد هم برای اثبات حرفش، کتونی‌های گرونی که برای لامین خریده بود رو نشون داد و در کنارش دمپایی‌ای که لامین براش خریده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101930" target="_blank">📅 20:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101929">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7ijrOIIB0qSUL-tnoZ4OZQKlEvtp1Ai8izcgCkaTlMwZJePRx2xDcVvHTl9U-wRPUp5vNext_ck7D-q1Pt9ctPUsiS6Ug2AkizylstoLXK3w0xbypL8hxsSGCXjnpugLOE_KOKYsvjxW-xdNCSl3P098dM92c-pNbeNjItMpkZRbC-uTkIU_m9SoZNKQaARc8R3QcEO3m2Horo4tJmzN4CgE0OwZPhpwWffmBTmUJ11ci4lKNcBZ91m6pN-fBkyKPekvzUEGjDaa3_CBmvRfpW9N3jMaXiwAlzA1tITtZQ0E5mFA89_jStGgBI0nifENOCtXkIO15Dp4KL1skhxnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پوریا لطیفی‌فر هافبک گل‌گهر با قراردادی ۴ ساله به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101929" target="_blank">📅 20:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101928">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62941770b7.mp4?token=SrrVR2fiWe0A5B6-5CczB29RafVNeTkFOrjokdoqqPG2xR3rEguxzZJnhdMQVz6PDuLwmAozLGLt6HVlFEMt3wt4aesniQcqrQ3N3ZDitLyWNWfgEwDC0_pKpXGEBsmJjXXJYVvQvcGZBmSxzinWBGLEWUUumv7DR_PP-PmMe8xsmqYebFWfFshhKg09nqd2LuXT5q3ToB7TdblLnvGixPdWoAjgRnHkpFwsaGvLNas32Ga1dRfHtw_Y4otdDbynFa8WTQa6Nh2IPfPgKzrgDQi7BOI8oE7wUC3JpsIO6VVA2Raacsl89O5LTBkQfgc1XM9EZslhzrM_vv4u9Pvg6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62941770b7.mp4?token=SrrVR2fiWe0A5B6-5CczB29RafVNeTkFOrjokdoqqPG2xR3rEguxzZJnhdMQVz6PDuLwmAozLGLt6HVlFEMt3wt4aesniQcqrQ3N3ZDitLyWNWfgEwDC0_pKpXGEBsmJjXXJYVvQvcGZBmSxzinWBGLEWUUumv7DR_PP-PmMe8xsmqYebFWfFshhKg09nqd2LuXT5q3ToB7TdblLnvGixPdWoAjgRnHkpFwsaGvLNas32Ga1dRfHtw_Y4otdDbynFa8WTQa6Nh2IPfPgKzrgDQi7BOI8oE7wUC3JpsIO6VVA2Raacsl89O5LTBkQfgc1XM9EZslhzrM_vv4u9Pvg6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
استمرار، استمرار، استمرار تا رسیدن به هدف
این ذهنیت منحصربفرد ترین بازیکنیه که دنیای فوتبال به خودش دیده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101928" target="_blank">📅 20:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101923">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9DXPPsX9-nhFiq_tuTISngjEMm1xB0qwdtJnQpojX9gU_5pJGc4aW9ZVzaMxss55ryz-leyiebfN2_xPrWWSxL5d5ctFnniBK_9Kq2cbTTMsEluldfOTGp6myIAhUzq7adYNOGCDx92EBWlVmcEiU-tQS2GF7kC7vt-Ziepi9kuTsa5PcvaktkBbXS7h7If1ww7noogf0MBBn9TeSmQhp6FGH9-zAbAbEmXALqLYEPk7TKbYmIMPvIo96XQAotSqESE1Ig71HF6iyNf3cpkNecTLaPys9n1u1QzurWn1yUT3qSNmgU32LBcgfWPNE9-etyX31CW_OisISmXaA9ncw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q57m_-JKndkh2Yt0iivERluGF-t9KC661REe9iSbOqhrTfBy1TWxTdBNLb1Xhc7gzueCLppwa_jN7fv4JuBQSiMb9ybaS9oOHZSbsErnTdAtSDNIGbiqwpJBewyKRGT5aInhE31Yx5_OiByz0wNzZiIHOPANeLA4jsjns1psErsCdx8FxyINGibei7tmXPiQNxL3EfLxAthwSUhfBYVtQpiU05dgByV40suPSqXhgh-GoWOPg0NvHHj9HYSqUtophu6P29NBDrGfmy0_v3D3l4Xw1KBmBLCQ8-uxJq4bQciyKPfuIfN9ZC5PQiZWiXTII30OkfJkUbH-Tv0tlQ31Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8N-3yq6njXoPloKlKkxbAI7kH20VN5gRqn3VH5UpegweTQyh7eWURXp51Ff-hHE5FTYGzdyMJRHOjAFQq_cOmV8Ub2t8q7qUl9H0JJ3v8slrvzyz7rFwiSMRBVpRFzDPCdDCEXGxkwnyva4L1JntIY40W3b8t4d3PHmehuOej51BNfEEu0_L2xnnvZ39kP9p3k5X8pSP0pL2L3HgD3RI9BXmerb4d6kXMxjBzi0oY0xQNxiZxgQpJR4L8PmjYSNqcOZJ9_FIEWUPd9tanX3VgQQw3aKY40sv2pKa0pAv3sN_DwPgpqoEA7Bte0Wr4qGNkk5tlFmDlqY9eTcM7dJVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91c7199c9e.mp4?token=vC7kjgsefKn3UwQd4kOaPYpRbwwwEolj-hdBMrgo7ZcT_PrSFiiBxRw0DNxGO4lWqEfljp1iBrLM1HTjwgXoem4QmEGB2TDIlKqMCdvAJXdLYDir9I-5vO-koN5gdnUJtyrJTk8cftPI9klC6JRPM0yC6X9uIo6MBPze-4iLqrAkPBgCktoEAIGoaG7gXm-ejr-1TVzvgcBAUt7pNTA2GV5BkdS-iNDm2AnUQFSYheOFXIvnfasdbNxhjxvpW2XXXY8UK49X2BC5U4GqN8-J6PfRKOYYisepD-gXQNLbwxDcDn9WtULaw1LaKU9p9ViOrof6IeVS-m79DYQAzlIReQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91c7199c9e.mp4?token=vC7kjgsefKn3UwQd4kOaPYpRbwwwEolj-hdBMrgo7ZcT_PrSFiiBxRw0DNxGO4lWqEfljp1iBrLM1HTjwgXoem4QmEGB2TDIlKqMCdvAJXdLYDir9I-5vO-koN5gdnUJtyrJTk8cftPI9klC6JRPM0yC6X9uIo6MBPze-4iLqrAkPBgCktoEAIGoaG7gXm-ejr-1TVzvgcBAUt7pNTA2GV5BkdS-iNDm2AnUQFSYheOFXIvnfasdbNxhjxvpW2XXXY8UK49X2BC5U4GqN8-J6PfRKOYYisepD-gXQNLbwxDcDn9WtULaw1LaKU9p9ViOrof6IeVS-m79DYQAzlIReQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدری تو تعطیلات در چین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/101923" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101922">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwIKZZfQw6ZlxcqvU-vWh7J1vdlYbweOy9ne0t06mja-yuObonJQ9VFlQfSxDl5ZmJwPuR91foCr0uEgLlZMBjys83p4b2xV9BaISoCUfvaRk7QtkAX0fMcvUxXZG5wmmm2xPxezeaoWhm5BHSNvGNQ-IsLwB_hSentmj-DcWDVJ-1Q4bdOIgwvJN-bcwcOctuJlgHkS8L8Z7WCn_oLhzuhfK_3tPrIPokUGm7Q82_o8kaOCTa64sxa6g-2qlNfjrePv8u_1Oyh7vFcV_0RxF2AY78EpfGc05nmgyr6Fx3ALbhH7duXugRRCs-CzyYhqg2yoQrCDnNiavvTmPoyW7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔥
همه مدل کیت فوتبالی فقط 570 تومن!
🔥
⚽️
از کلاسیک‌ترین کیت‌های نوستالژی تا جدیدترین کیت‌های باشگاهی و ملی دنیا با قیمتی که هیچ جا پیدا نمی‌کنی!
😮‍💨
❤️‍🔥
👕
کیفیت بالا
💰
قیمت مستقیم از تولیدکننده
🔥
تنوع فوق‌العاده از تیم‌های محبوب دنیا
✅
دارای نماد الکترونیک
✅
امکان خرید حضوری
🚚
ارسال سریع به سراسر کشور با کمترین هزینه
اگر عاشق فوتبال و استایل فوتبالی هستی، این فرصت رو از دست نده
👊
⚽️
💚
کانال تلگرام برای دیدن مدل‌ها و سفارش:
تخفیف  ویژه  برای سفارش از طرف ما
👇
👇
👇
عضورت در کانال
https://t.me/esportsofficiall</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/101922" target="_blank">📅 20:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101921">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fac07199b.mp4?token=pKJZqjoovQnoHazJfoSlKmKAjHf6vlrerfXLwaM93Twv07VBKwvgmzYRlMvr8iWzvVSSlI_IwqqvVo7nmCWLLYO3AxB3Wj_AseyituTulp7qQfQEJdMVJUBJeteu2v9gg81JLVMta83TtvlXfVWAdcVXKk8Qre2kzbLpBX2W1QWGA9Un2GfGmckvvKMVOQ-avP8IpSX24kTJEAYM2bd8QtT25TDTpXCWSepUf7Kt781mV1ep4XXOK3omqgBdtxubNiIgtHeko772SBonBIte5vtse3qmafJrFzPq7DQfXNioz2TZsD1PqekYme89tl4_5CyKkKL1tJ-4wWHvpTq7yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fac07199b.mp4?token=pKJZqjoovQnoHazJfoSlKmKAjHf6vlrerfXLwaM93Twv07VBKwvgmzYRlMvr8iWzvVSSlI_IwqqvVo7nmCWLLYO3AxB3Wj_AseyituTulp7qQfQEJdMVJUBJeteu2v9gg81JLVMta83TtvlXfVWAdcVXKk8Qre2kzbLpBX2W1QWGA9Un2GfGmckvvKMVOQ-avP8IpSX24kTJEAYM2bd8QtT25TDTpXCWSepUf7Kt781mV1ep4XXOK3omqgBdtxubNiIgtHeko772SBonBIte5vtse3qmafJrFzPq7DQfXNioz2TZsD1PqekYme89tl4_5CyKkKL1tJ-4wWHvpTq7yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
تو شیراز یه ایونت ورزشی برگزار کرده بودن که چهارتا کم عقل سر دختر دعواشون میشه و طوری همو میزننن که کم مونده بود بمیرن‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/101921" target="_blank">📅 20:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101919">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KFAWKlwoJxSnnSXqYpR9MVEh23_Va7uGWioCY36lmy68BhXLCYfltIs5nbKYTinfKbL9PL0LI-sW2iOUYsU5MXYYr5Xvqos6B3IQhl0wyFed5F8MWjUPQPdZuJBbUR3us-YTcDNJJuj1OZEPGx4_C2yDIYJ1a0s-1i93EkBr6RV6eUiQvLgnkXPPw81gkUn98r4k_uEQ1HFz0mspeGWj-Ni_IIvPmvUY5qxvm9pL5B6EVd2t65gLw5f1wyI_zQo11fMNmu9Nwfv3R14PbyP-mtNNR_DuCx1FqcrffQur3um9JxoThFoyEqbcFCeksL-wSLB2ZaEmJ3Aa54p9Zz8VwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2HWZSqxZbB2Ib7hbblAs-fkVE61DPvkAAGz3zSney1VJ6Ejw8MCAF-ysJc44Vf7sdSGzLeROTiZqTIZgw1DGCcFkrneF0H6vL94jlRgH3cd8r8ZnMlPReZ7yu6OXsYZCgKNtW4MTcNGcC3fX1t8MRkIGNvoDDPZPInM2DUCnzVWhNihMrJV-ImERfRqRlYopf29Z3oGwqmuriMrsH0-OSmkFdzGKh3sX-qS_eu9LjfrxpH8qGyiBOlLMLciumlwwZ1JpppJXpX734-BpHkMfpZjTEF4ie-wKOd71c2v4ZEeNwVdX-nbcbQn-emsOSpegTO6X8o8limq6PiJmr-d1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇪🇸
فرناندو تورس یکی از آندرریتدترین فوتبالیست‌های تاریخه.
افتخاراتش شامل:
🏆
جام جهانی ۲۰۱۰
🇪🇺
یورو ۲۰۰۸
🇪🇺
یورو ۲۰۱۲
🇪🇺
لیگ قهرمانان اروپا ۲۰۱۲
🇪🇺
لیگ اروپا ۲۰۱۳
🇪🇺
لیگ اروپا ۲۰۱۸
🇬🇧
جام حذفی انگلیس ۲۰۱۲
خیلی‌ها دوران سخت اواخر دوران حرفه‌ای تورس رو به یاد میارن و تمام چیزهایی که به دست آورده بود رو فراموش می‌کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101919" target="_blank">📅 20:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101918">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeK5uHH6bN_pAFg5TH5iTj0huK1LQEGUOgiz_fMORhpnPhkWwcvuZ93pfz_O-hlSZqx5onYnFQ_v7M03xS5FjJhZfbZkfRQkRjTpQwlpKJ9mHIASt3ZNCnr0oG6c6nOthhftuUnUZpbs4YnexrhqEw6agxmtc5pbygeNZSHoSFp3DaRHIMB9lTxRLDtLNv4BdJVSQtLuksiqN27qgYXkWYoV666522R1zfTT9i7sUvP7zo3LjaVAmE5pxv9od7o-l6ySKgqNB4oGyEUwBZq-CGTBrw8WNY6uXArm2x0j3pWo_lDv9JclR-Cv0TVWVlRXgV7PffboARuXKF1Vh6ZnPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اسکای اسپورت:
هری کین بلافاصله پس از پایان تعطیلات تابستانی خود مذاکرات را برای تمدید قرارداد با بایرن مونیخ آغاز خواهد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101918" target="_blank">📅 19:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101917">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/779a683584.mp4?token=ovi-nWRYCBil-Rm3eFO2d8P4GkICLkV4V0-sx3g_cXMXWo659JzkevhiL1O0JAD7rORsofhQ8zvhhou0VZX9yVXnsUlw8GZBif70z5j9Cy159RzSqK-mIwn7ENAjL60HJ5uggcaTCDZjl_o-xL0iTxzbHljJhXuBUejoT_dlKf2dDtVVQC5ih_GZ0-Q715imTU-limu4T9b0If8NtSexJsIoHju1zZhbO51nnIOI-MuRSqpZDds7l1bBwKVTaPeJGqPjE0EL1bodiTMM5gVskPsPCkMk4fQwwFEjsEfO0eYWn4UaD54dkRmF7dpyAltbhI5tZ1TKhCpzipWZWeEghA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/779a683584.mp4?token=ovi-nWRYCBil-Rm3eFO2d8P4GkICLkV4V0-sx3g_cXMXWo659JzkevhiL1O0JAD7rORsofhQ8zvhhou0VZX9yVXnsUlw8GZBif70z5j9Cy159RzSqK-mIwn7ENAjL60HJ5uggcaTCDZjl_o-xL0iTxzbHljJhXuBUejoT_dlKf2dDtVVQC5ih_GZ0-Q715imTU-limu4T9b0If8NtSexJsIoHju1zZhbO51nnIOI-MuRSqpZDds7l1bBwKVTaPeJGqPjE0EL1bodiTMM5gVskPsPCkMk4fQwwFEjsEfO0eYWn4UaD54dkRmF7dpyAltbhI5tZ1TKhCpzipWZWeEghA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
رونالدوی برزیلی سرعت یک وینگر، قدرت یک شماره ۹ و تکنیک یک بازی‌ساز رو همزمان داشت.
🇧🇷
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101917" target="_blank">📅 19:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101916">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3ffe3c02.mp4?token=q31bdelCkmipcWHnqeziPbrUZHcjaN7g_2rgGTuNzyZx_abOWkpXH7Etg328L14neOgCw6I2aTHdJo0PCaZsg-upjZYsM7i9Sa5l-xJu4_Uxol5O1DgaDL7PfVakQey2atwBqBdebmy6S-SikkVekvPOQqau495L2lVfAkZyfP_uzTHAIGsqIhWwFIt93r_ht5n0MKmekhLU10yWSy2yd9veKckw30JO68S5TsM3vwPG6aTBP7lzbXSLUe5aISLuqI5JM1jcj4-AbSIaqxHJRj4xV4TxKGui_wirBh3GgJ6HDB4ErmH_BPys-C8LSurRds2aXcjuvBsO2nE7Qrs51S6UwaLXSFXAW-qlC3cGOx-0tSTTMaxWpO1EjOaKAUljQWR6P6Y6oeYlSNsO-TuxQzoACRsY4oesxtMmohBhnjX3ZIzjcMrds0Cxf3BzN7pui9tTmZ_lf99P9CwO13pLv4gTYC-PttNR_4u2q4Dv0TyCiQTxOgDTVw4D_mgbg7QDIfLnvnNlvK-XWVmqCQ5RD8IjTwfXqsuX1Njje64XZ0Wap9s2Cb3bRezq4EM9ef8IfNNxs6s3SFLM0JJQey2HcN-irOEcj3qy_JGc5bjem4CyAusxTGidAprFpWd1eTv_usbQ4FpRSJ9-FzOW2VnPxMfzUb-MmovcSKpkcz4WGeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3ffe3c02.mp4?token=q31bdelCkmipcWHnqeziPbrUZHcjaN7g_2rgGTuNzyZx_abOWkpXH7Etg328L14neOgCw6I2aTHdJo0PCaZsg-upjZYsM7i9Sa5l-xJu4_Uxol5O1DgaDL7PfVakQey2atwBqBdebmy6S-SikkVekvPOQqau495L2lVfAkZyfP_uzTHAIGsqIhWwFIt93r_ht5n0MKmekhLU10yWSy2yd9veKckw30JO68S5TsM3vwPG6aTBP7lzbXSLUe5aISLuqI5JM1jcj4-AbSIaqxHJRj4xV4TxKGui_wirBh3GgJ6HDB4ErmH_BPys-C8LSurRds2aXcjuvBsO2nE7Qrs51S6UwaLXSFXAW-qlC3cGOx-0tSTTMaxWpO1EjOaKAUljQWR6P6Y6oeYlSNsO-TuxQzoACRsY4oesxtMmohBhnjX3ZIzjcMrds0Cxf3BzN7pui9tTmZ_lf99P9CwO13pLv4gTYC-PttNR_4u2q4Dv0TyCiQTxOgDTVw4D_mgbg7QDIfLnvnNlvK-XWVmqCQ5RD8IjTwfXqsuX1Njje64XZ0Wap9s2Cb3bRezq4EM9ef8IfNNxs6s3SFLM0JJQey2HcN-irOEcj3qy_JGc5bjem4CyAusxTGidAprFpWd1eTv_usbQ4FpRSJ9-FzOW2VnPxMfzUb-MmovcSKpkcz4WGeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یکی از مصاحبه‌های چندوقت پیش کریستیانو رونالدو که اون گفت او قصد نداره یک‌ روزی مربی بشه و بیشتر به مالکیت یک باشگاه فکر میکنه. او همچنین درباره اهمیت مراقبت از ستاره‌های جوانی مثل جود بلینگام و لامین یامال صحبت کرد و گفت باشگاه‌ها باید به رشد و آینده این بازیکنان توجه ویژه‌ای داشته باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101916" target="_blank">📅 19:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101914">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ew8LRBdjDJRBih0YLMrSM0PPVxYhN97h3GHPufx-CEZxITPN4KP2uCS9vY-dxeNiE2I05i18bN0ayZ0HHK4-rLBac3T7L8jcAulcv1FCRQI_BzHipVNtdZuKp4fDkHYJP6okMM1r_x1Lycy-PTjjonwO6z-gWFVsWG9FbUYe8Cxy0TV4ofRLORb4R5k_-M3gJMK0r5FJd_gRADZq8Gi3CtM_9MEwDKiH0pBsJu90vfcDX9XgSZWWQuZ9BgVUKnq_zmLnzfnaqL5Nj05LL0meEm3pVEvMNRBfhjCV6m7VU_Za_OnWg9eSgsdOY1LTk7uhALW6hNUwFE7cjrPQvr5Mzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9c742e9e0.mp4?token=IfQPdoMMSTIMq_228jG9pJ9OEwJ-7-Upixz8wIjW98KYmjE8Bjvf7EHSUEfNEHH-hSYS9UpB4OpnF3214p7OWZiV1avpPfrpnlMo9UseGckE-32qKCD4Hv8SyuqTRPGqIrGbo93yMXjo9Ddi-S2yZp0qfjdztTSoRWXQ5--QJZ_gZdqUnJqPZvQAIj75Tgzdl0xBpoqbzdjQmFcDep_q_2yM3G07xqe5m3muJ-pKXjYSNlmLvxkD4nlINXrQbidVYS5RE-lJdFFUTbEgUJ89LaEwZfDjbKv7ljdsTKBV4HwSL9VuSRwX1A-Xo46Gz6pHM8tBJFYkr3Rdk6I1VybP0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9c742e9e0.mp4?token=IfQPdoMMSTIMq_228jG9pJ9OEwJ-7-Upixz8wIjW98KYmjE8Bjvf7EHSUEfNEHH-hSYS9UpB4OpnF3214p7OWZiV1avpPfrpnlMo9UseGckE-32qKCD4Hv8SyuqTRPGqIrGbo93yMXjo9Ddi-S2yZp0qfjdztTSoRWXQ5--QJZ_gZdqUnJqPZvQAIj75Tgzdl0xBpoqbzdjQmFcDep_q_2yM3G07xqe5m3muJ-pKXjYSNlmLvxkD4nlINXrQbidVYS5RE-lJdFFUTbEgUJ89LaEwZfDjbKv7ljdsTKBV4HwSL9VuSRwX1A-Xo46Gz6pHM8tBJFYkr3Rdk6I1VybP0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
طبق گزارش‌ها، لائورا ایگلسیاس، دوست‌دختر رودریگو دی‌پائول، گفته او حتی ۱۰ درصد توجهی که به لیونل مسی دارد را به او نمیدهد. او مدعی شده بعد از شکست در فینال جام جهانی، دی‌پائول دیگر حتی کنار او نخوابیده و رابطه‌شان به جایی رسیده که به فکر پایان دادن به آن است. گفته می‌شود او معتقد است دیگر بازگشتی در کار نخواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101914" target="_blank">📅 19:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101913">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnmaMsfau34NSLn5E_Lp_j8ytqXOHGDe2AWV7X4SeLfJ4VQ3FM1aeOgfhi8PW9t6jSzVb8iiC1CxWPS3xcRTfoc0S6DC7FDgBq7_2tYT5fOOuGnFEMRXzyDMMKNyGDHonib0tcreHqUzDNn8WLLcqsw9GrswMbx3ZngerxC3DjKLYn1aU54JY9VUiqMjC15QsIrC80jdBcpY5iKcp9hPiZ4YS4cvn93xpsUH1HcaMuicx7tsU2RLID1iMde1BzXn8mULrr5073nJF8aj9MvdHncYz0Wj7IpkrCwzGeXc3ro2wKFv_w1up4Bk09aFXopnS4SSV-NY_WxP7AAxf3kL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
تلگراف: ژوزه مورینیو با انتقال وینیسیوس جونیور به آرسنال در این تابستون مخالفه.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/101913" target="_blank">📅 18:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101911">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CFdA8b3Hefx738vdL1zKfztwqC2xCOPNM-0sJm3Rnpi44ehXhD-l-UJVMc1ZAdTQP6roznOZb24E7Q3lh8gm6_yAF45kiWfxhaR8u7VsmNZM4_YpdWvGLz3eWOc1Zr_5EEeYlgl4viLVMAKauLcWZ7izGRANYYqOD6ZBC5pLpMFuLjGfNGJ_KKAea24c01526PHzZ7-T0_bat8_BjyTSh7vFQu6wXc73A5nvKMAXr-iw4ZrB8h3aLWQY2PY28q3ZLSUWtyCAGrrLqhnOwcqtEG_8MWtwttiMd6OY6YPP83U1Izmugyvug78tr3FgreY7MJ7l1wSFD4a5TGAo3bSosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4XM3UbR8c3rOT9CvPn7QtfiMzdMuxCe_i_ABB3tas-SEyimWjw8zXY5eCaPTXMzGkafNLudV1bowTZOjiVxtJjjoPQr9rF7z-uO6vVJbfT6ps6ALO8VNL2jE3Ybfm0YojCZK7eALuUZSf-3scETAX-R4y7mKy2N07UvXeJbbEhaz0X-lIYuf8C5kzUcr9IVVOSInAH4D2KfoUdT7nvyvz-MUo8YSCmo9DLbmld0-cvCogTRqxEkeyiIV4zPhE8pR_Zecw8x_PfjF_0NIfybIH7VHD1f5OI611sfxdg03avqxTJUCki-FWnMGMtgJc94_AAQjRLNx1ExC0TaPs61LA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
رامون آلوارز:
اگر انتقال رودری و دیومانده نهایی شود، رئال مادرید ۲۶ بازیکن در فهرست خود خواهد داشت. در این صورت، باشگاه مجبور خواهد شد حداقل یک بازیکن را از فهرست خود حذف کند تا با محدودیت تعداد بازیکنان مطابقت داشته باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101911" target="_blank">📅 18:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101910">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DA8VGmVo04FkIskYstZSSnCWD0--kN6ZmJ8aVDz7z-Zi27f5m3XUgpmqzNjVoQyiyPGLSvbKB2_Jd41dsV7MbjTbFgDETBCzqD4_zwkq1grtckJ01txno0iYKpic59S7SdW1bTo3GiTcrUA2wL6ZDPtc_yjPe6sKskxwIzoL5nXYiJTiK0vqiaRC8PCOB92JVsONOGsXn9BaKiln5_mvtvsYG9C-OQl47S8Q_hxW4cKergzoeNjnAXy_4HCWsA1STxt8it9v3M9ON99jPOZz3ZWba3xiC-SRRe_PnSpwMvMORPF7sMmBpzD_eKw5X60mdDP6QFw41vDcyhBdzyK4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ربات هوشمند تهران پی تو ۳۰ ثانیه خرید کن
😍
فروش یووچر، استارز و تلگرام پریمیوم بدون احراز هویت و ثبت نام.
تحویل فوری زیر ۳۰ ثانیه.
درگاه رسمی بانکی و مجوز فعالیت
✅
@Tehranpay_bot
@Tehranpay_bot
همین الان استارت بزن و راحت خرید کن
تلگرام استارز با ۴۰ درصد تخفیف
😍
یا داخل سایت رسمی بخر
🔽
https://tehranpay.net/utopia/</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101910" target="_blank">📅 18:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101907">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2UMPqzQcX9G0WxnsKTvxWSpAD3YeBG3hFBrD-wCDRPbd1ovBYiOgP2Uwnzjpi5rkM5qQzIzwUsjogdVITem4zSkK0nk0fQqLzs3QyaufXpxiQ52qMzXmHwh2neTWYzPFeGPzFRN-cqH1pHEvY1iwUBv9tqkz4j3LII_GMhLfdm0NQDa5-phfJ9UAgD2yC3nVmAY8LQtVhKtyEqISZ7kF9sKelaRm1liWpB8ntoUPy9DqjLtsiztoJDan55r5RPbfB_kRmje4UITyEE5LTC7KkolCR1blag6j1_KjLci53kR9JPcw9mayRIEPieOrjLc4pzjAIZA4ZLAU0vwMuMgSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e5ZuhN5DYHWv1HZfrC6621cLuMe6tKZDlc5fR8gyTZuEXuDJWm22FJuXJhwS__zykYjT7Ta2TpPKg-YgiDiL6uGgctNN5OjIUfIMoHfhCdRJLVQf5tzihHPbffZVdZMp-fFhQIkJPZziN26MyQJ8krOUi-xD4fDF57-lHXlzYMJP6Ma8lxIk28oMC9lMVHGRvlMd-zY9D3Uj8U_uXN6KoJ7-W6vR_i9Nerkzmu0DkPaXA5YOMZ6ZK5rqn3XMfd8ARUjj41qTVUA3sjvqTAUSxGP6PKFaOQmPOQbgkZXDPgPOYrtu1jUedsK4OerCrk66o8f8CAsh1uoLm2QCG75qDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d05827d11.mp4?token=YeMLdfS92PUgueiTem9RwtY3tzOWje4r0QxVZppBmBLERzEIPPf3ef0rReXMZedwDl5G8W4rpuJTfjAvNvzjUBlJ1HaO0TbY-TtZ6QYWHFrgse_1buKYv6yXJ1oUAcQ5BLCvybo-TrFzXNTvRs0zwB_1ypKWFbs3WIC35lTaim4BrRNZAiVPFxnJLjFd0T2hF80k2bkqMWH1flcwC8peyGUE4k01iKDNb6i3iax84Xai0TOxcAKBZPvNXYZjsMd-uCqgV5DUy7QKxOc146T2Ov010tik4j3bT60em96mBSTzwa38mY_pspjY-pWnCGjAsx1rN3E4HttMFvqXmUbJOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d05827d11.mp4?token=YeMLdfS92PUgueiTem9RwtY3tzOWje4r0QxVZppBmBLERzEIPPf3ef0rReXMZedwDl5G8W4rpuJTfjAvNvzjUBlJ1HaO0TbY-TtZ6QYWHFrgse_1buKYv6yXJ1oUAcQ5BLCvybo-TrFzXNTvRs0zwB_1ypKWFbs3WIC35lTaim4BrRNZAiVPFxnJLjFd0T2hF80k2bkqMWH1flcwC8peyGUE4k01iKDNb6i3iax84Xai0TOxcAKBZPvNXYZjsMd-uCqgV5DUy7QKxOc146T2Ov010tik4j3bT60em96mBSTzwa38mY_pspjY-pWnCGjAsx1rN3E4HttMFvqXmUbJOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
رودری درباره جنجال‌های جوایز فردی‌اش:
فهمیدم مهم نیست چه چیزی به دست بیارم، همیشه یه عده هستن که میگن بازیکن دیگه‌ای شایسته‌تر بوده. وقتی توپ طلا رو بردم گفتن وینیسیوس باید می‌برد، حالا که توپ طلای جام جهانی رو گرفتم میگن باید به مسی می‌رسید. این بخشی از فوتباله. به نظرات مردم احترام میذارم؛ مسی و وینیسیوس بازیکنان بزرگی هستن و مقایسه شدن با اون‌ها خودش افتخاره. اما بابت جوایزی که با سال‌ها تلاش، فداکاری و ثبات به دست آوردم عذرخواهی نمیکنم. هیچ‌کس نمیتونه ارزش زحماتی که کشیدم رو زیر سوال ببره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101907" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101906">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbd3d9241.mp4?token=XGtpMnsMXpdxPC-pKHRh-FQfzGPP-Sj0VXmx8uFnCGcb0hkNgbmoMmkxvXSxsADl259x0KDCDc2xESZZSrPJp8JkeU5wuRKa4qu264MAM1RyMRzeL6p9ryuxQgoRNnUJ6Oz1kXeTri9i5_0MKDAMsPMrlVAcORCs2paMcsr7nDYXWQvMhEBa6QgpZLAJjbOGaO8uy34cw_q3uqnKVl_MYLVpx8R20cCfQyeKFHYi0Ra1wQTk6OhtbAAF529VfTCM5PzyRej85o6VpcWqtK9WXYB2B-d0RF4OGZsK4sdOQM_oXjt86ooaS5MfgaJs7KOpZv-ccrZNRoEf8-0uVmygrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbd3d9241.mp4?token=XGtpMnsMXpdxPC-pKHRh-FQfzGPP-Sj0VXmx8uFnCGcb0hkNgbmoMmkxvXSxsADl259x0KDCDc2xESZZSrPJp8JkeU5wuRKa4qu264MAM1RyMRzeL6p9ryuxQgoRNnUJ6Oz1kXeTri9i5_0MKDAMsPMrlVAcORCs2paMcsr7nDYXWQvMhEBa6QgpZLAJjbOGaO8uy34cw_q3uqnKVl_MYLVpx8R20cCfQyeKFHYi0Ra1wQTk6OhtbAAF529VfTCM5PzyRej85o6VpcWqtK9WXYB2B-d0RF4OGZsK4sdOQM_oXjt86ooaS5MfgaJs7KOpZv-ccrZNRoEf8-0uVmygrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
حالا که اینقدر امروز دربارش صحبت شده یه کم یان دیومانده ببینیم.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/101906" target="_blank">📅 18:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101905">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6a2da2fb.mp4?token=QGlSOhBb_n-nz-gvjfIk_PtWR4iXL-FSz2xlmABOXUnMNwsxYa3UOyZV0T6PalH9iBSvfLMH_nhe0Hu6wummB6vxOfwgP8EubH-Czf1creU4FL_x6v-UtBkO2zjhdhaJRYR_kGFKtjYorPGj9Vb3a5HioiazStlhnS2MyKyFdcx0TR6xX1ZJ0l65maALcusptiOBzGU3X7tAXfVqktwJNzMQ2lthJg4VRbQRedbWzs-_OoCr_7976nxYR1thMWTyK45Fihc_M1hc24yv27u2YnCP0oR3zSkl4qJHuCF1zA6UkWvPLAIqP6QCEA6kwn4RSg7YmhcGUe8lzoTUmarDFZbN37aPuznI4DHUDOBf8gxfeFCFpItLJawdW-_pE1m574-lRaQD0BPbRVhXQb2n3CNBxOZp-eF21FGI54sWvORFTG_RBm0KLHwq3iWMWjE8a1na3MPDtrXC9IzIByQplCqk9eRcS5kBdn_2HW_Vzme63EFMrTricjMVtmMfvZp_1Wt6pMoFYjr2zVK1GcOrEdl77SeMgCA0j4PcM2hae3XBpSZhOzNj08htJ0i1v8QV7rU37jEm79zddcNOzd53kj_Trgb-9RHfLpn4IQ4CAjeEI_pHBiG2xc-xCAdeOcpEVQ0PSWhVHGonfb91ZUttRxTAvY8wZO4DWOueR-E6Ooc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6a2da2fb.mp4?token=QGlSOhBb_n-nz-gvjfIk_PtWR4iXL-FSz2xlmABOXUnMNwsxYa3UOyZV0T6PalH9iBSvfLMH_nhe0Hu6wummB6vxOfwgP8EubH-Czf1creU4FL_x6v-UtBkO2zjhdhaJRYR_kGFKtjYorPGj9Vb3a5HioiazStlhnS2MyKyFdcx0TR6xX1ZJ0l65maALcusptiOBzGU3X7tAXfVqktwJNzMQ2lthJg4VRbQRedbWzs-_OoCr_7976nxYR1thMWTyK45Fihc_M1hc24yv27u2YnCP0oR3zSkl4qJHuCF1zA6UkWvPLAIqP6QCEA6kwn4RSg7YmhcGUe8lzoTUmarDFZbN37aPuznI4DHUDOBf8gxfeFCFpItLJawdW-_pE1m574-lRaQD0BPbRVhXQb2n3CNBxOZp-eF21FGI54sWvORFTG_RBm0KLHwq3iWMWjE8a1na3MPDtrXC9IzIByQplCqk9eRcS5kBdn_2HW_Vzme63EFMrTricjMVtmMfvZp_1Wt6pMoFYjr2zVK1GcOrEdl77SeMgCA0j4PcM2hae3XBpSZhOzNj08htJ0i1v8QV7rU37jEm79zddcNOzd53kj_Trgb-9RHfLpn4IQ4CAjeEI_pHBiG2xc-xCAdeOcpEVQ0PSWhVHGonfb91ZUttRxTAvY8wZO4DWOueR-E6Ooc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
تیم رئال مادرید در دوران پرایم خودش یه شاهکار واقعی بود؛ به طوری که تقریبا هر بازیکنی، کاپیتان تیم ملی خود بود.
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101905" target="_blank">📅 18:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101903">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmhixIgUbvEB9bal8kpqitC-hPgD-QJqhnESAB27p7c0HE69mfIeZVDVd50Hw5Jrs5gWL1_urF42HyL4TmcdQh_4wOob8_kSPWnaWCG8ddi5PeAO66A-YhOhgScq_h2JeVF2phG6Xppannu5l_m37cKSLf_U0Y69_YOxQtWIk8pHxd19gcueI8s0ifK1By2HXc0L3CAV2K4xn6dLO8BqQX7sKgOvQdIvl5ZBlceQbGGpBGn9POWbnGcmDnVDfNFjxyJVAZzjrWoaNGyLq9RfhQo6MFeNldYQEA8egXOAlJKOtLWDJCKmWNGV36IcljlDajwEF4AvimQ0-PImNvkF2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
کاکا درباره دوران سختش در رئال مادرید:
من از میلان آمدم تا بهترین بازیکن جهان شوم، اما مصدومیت‌ها و رقابت با بازیکنانی مثل کریستیانو، بنزما، اوزیل و دی‌ماریا باعث شد کمتر بازی کنم. حتی امروز بعضی‌ها من را یکی از بدترین خریدهای رئال می‌دانند. اما آن دوران باعث شد خود واقعی‌ام را بشناسم. کاکا می‌گوید نه بهترین بازیکن جهان است و نه بدترین خرید؛ بلکه همان سختی‌ها او را به انسانی که امروز هست تبدیل کرد. فلورنتینو پرز هم هنگام جدایی از حرفه‌ای‌گری و شخصیت او تمجید کرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/101903" target="_blank">📅 18:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101901">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FZ_r1e4JDWPBZIzZH_6BrIqlfDfUS0gSH1gW1awSgpX8QVgK5GPXcJkF1fGqXFfQ1MKItn75kPwEVE4YsuCmW50yrlrY3AYBiVv5SZ5iwFAJh-FTjg2qOHifT8gfDmNWGVj3qHd4qgz4KqRBwS9DglNDIhC9rgzBIH2K5jMv5bC-cjYkMdyYklowwazKHHCjQP5zW-NUdhEbqgEWvqZ7QCOMKp-4jLiTrs6o_5AbsT-s1PPE0vsK5EM5pQyeGnLxWhhpk2oBaKKq8zkmOdbc_dtoS52_KKD0YTnYBKU6qlD5JpE1K485117YFtEBgSOk1ppZhFiyEndd5G97P1MsWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugzRPteq4SQlO56DrfnAP2GLm72rIDbqE1gq44hS7IGdWSv02CahhtwEZfJ2T6IOfMglJjgpn1ebZxYsYS86cGDszMT0gy687UD1X8-TPoK_vNpb2Q-c0x3Vjtw-NGrIbjtIRz7wVwDObxQnNEPvI7l49O0Bk84GQ9nrO6NADE806e15DPd_5NuS6Ftzl18QEIdiDWQCp0lECR4w5PKsb2sbHMiqG0OyX7RmuuXbRgKcNtm6xNtQstsORRjaO5vumwW46Tpes9MpBQ4_U96IsFw0Q5Vcp7Sk751cto-KB-iHgNClv4zeeOSFN76APhischQzd_9BHQmT9pmhQOW8xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
یان دیومانده درباره گرفتن یک پیراهن تقلبی کریستیانو رونالدو در منچستریونایتد به عنوان اولین هدیه تولدش:
اولین هدیه تولدم یک پیراهن منچستریونایتد بود. توان خرید پیراهنی با اسم بازیکن را نداشتیم، برای همین کاملا ساده بود. خودم با ماژیک مشکی پشتش نوشتم "کریستیانو رونالدو" و شماره ۷ را هم اضافه کردم، چون می‌خواستم به خودم انگیزه بدهم. هر بار آن پیراهن را می‌پوشیدم، تصور می‌کردم خود رونالدو هستم. فقط می‌خواستم از همه بازیکنان دریبل بزنم و تا جای ممکن گل بزنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101901" target="_blank">📅 17:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101900">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b492c31a81.mp4?token=ChFzIt3aNuAwUwSeoD8BNBMvJqonQHmP5YtcQjMyfLknz1a2sxiJjUIqyTchnLOw1z7QZwIRo1G2u7b-VTmgYT2XvgirZ2d8MQls79Ln8n-aMLtozJgDPBwfgSCYZctHKVIXflQugC4ZhxSrgUt7nZqUzbCjieNJcnmcsVpJvOF8PZSnitVrpoItqXuhtxRnHGd9pZaN-ubQ95_Unnrr8sRwtKNU5Bj4uGkOp2DUXia2pHRQ3YTJeXldgIgt1nCecYIb1KmJx7Wx6XoWQxl1IdoEYSvYtOYP-Yi9-KuWDexw5gtPUduqSzJuu65o7ePrK_S6YQ0bvNo3djzJaf78-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b492c31a81.mp4?token=ChFzIt3aNuAwUwSeoD8BNBMvJqonQHmP5YtcQjMyfLknz1a2sxiJjUIqyTchnLOw1z7QZwIRo1G2u7b-VTmgYT2XvgirZ2d8MQls79Ln8n-aMLtozJgDPBwfgSCYZctHKVIXflQugC4ZhxSrgUt7nZqUzbCjieNJcnmcsVpJvOF8PZSnitVrpoItqXuhtxRnHGd9pZaN-ubQ95_Unnrr8sRwtKNU5Bj4uGkOp2DUXia2pHRQ3YTJeXldgIgt1nCecYIb1KmJx7Wx6XoWQxl1IdoEYSvYtOYP-Yi9-KuWDexw5gtPUduqSzJuu65o7ePrK_S6YQ0bvNo3djzJaf78-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فران تورس تو تعطیلات در کنار بکهام و مایکل جردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101900" target="_blank">📅 17:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101899">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51f2886d75.mp4?token=PeitIeHkfxIMPgaOQ2_PMH8PEYMR6VBmvGgR9UNO9tPBDkVZmWXwM4ZTbwjwLZB8y30mvsbPezD4a6t5wTfZi9BhiqiQTtex2O-Z3Q4o9Nn1eBgHX9xA4wE8VKwBSy099GJvjQnKKm2hpBg4lxyeqS9TY8j-G_4NE0O1_VKDHpucy1hmzdHaK8wJik6mYjNewa3KDY6rgi-oQYol3hI5zMc9um1rwp_Wk_mcYnOlghOLF2CuVI03nF5Et0RqRar-z_VCPQwCML9suGrqAchj3mCedNhNogYA7CXT0ZTyFcms_u5hq6VXicCcvDgdj708zfHMke8IVBs6rFzryMNGQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51f2886d75.mp4?token=PeitIeHkfxIMPgaOQ2_PMH8PEYMR6VBmvGgR9UNO9tPBDkVZmWXwM4ZTbwjwLZB8y30mvsbPezD4a6t5wTfZi9BhiqiQTtex2O-Z3Q4o9Nn1eBgHX9xA4wE8VKwBSy099GJvjQnKKm2hpBg4lxyeqS9TY8j-G_4NE0O1_VKDHpucy1hmzdHaK8wJik6mYjNewa3KDY6rgi-oQYol3hI5zMc9um1rwp_Wk_mcYnOlghOLF2CuVI03nF5Et0RqRar-z_VCPQwCML9suGrqAchj3mCedNhNogYA7CXT0ZTyFcms_u5hq6VXicCcvDgdj708zfHMke8IVBs6rFzryMNGQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر شاهکاری یه کپی بی ارزش داره
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101899" target="_blank">📅 17:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101898">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe82274ba.mp4?token=eKooOKnzIf1Q0bzwhh05iVtoPztnbj0ATtnFb6-Mes2y6G_wFiFuEiJAPmHlmYaxUofbKVXl54W3nNcE7HitQFXkSZLx8tG8ltRMjzKISg1wLDOW-nk-3uO5SivmKlNS2V9MmqLXMt_GM99KoV8TkIKCT5fec1PzvDQLS4BQ86b35K98M0a3oZ6kCBFO90v6tPV-FhVJynqZhmiQX_2iVUlgVi3m4Tro9jUvAXZ8ygxLM3rvUIqVvCIScZ3jy0ATjAFpR2FF7RFPLUMURqSLioCNMsbaAoLpdYsPd0WZcFFqBbTasrZyOS0PtpLbE61V0auD5qPmvo-dcnxu6LxZ8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe82274ba.mp4?token=eKooOKnzIf1Q0bzwhh05iVtoPztnbj0ATtnFb6-Mes2y6G_wFiFuEiJAPmHlmYaxUofbKVXl54W3nNcE7HitQFXkSZLx8tG8ltRMjzKISg1wLDOW-nk-3uO5SivmKlNS2V9MmqLXMt_GM99KoV8TkIKCT5fec1PzvDQLS4BQ86b35K98M0a3oZ6kCBFO90v6tPV-FhVJynqZhmiQX_2iVUlgVi3m4Tro9jUvAXZ8ygxLM3rvUIqVvCIScZ3jy0ATjAFpR2FF7RFPLUMURqSLioCNMsbaAoLpdYsPd0WZcFFqBbTasrZyOS0PtpLbE61V0auD5qPmvo-dcnxu6LxZ8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زیر ۲۹۹ هزار تومان با ارسال رایگان!
🥳
با سرویس سفارش
یک نفره اسنپ‌فود
غذای مورد علاقه‌ات رو با
همون کیفیت
ولی ارزون و به
صرفه‌تر
نوش جان کن.
😋
🔥
از اینجا سفارش بده
👇
👇
https://i.snpf.ir/wopv1
https://i.snpf.ir/wopv1
https://i.snpf.ir/wopv1</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101898" target="_blank">📅 17:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101897">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5e82a980.mp4?token=JhDGablVc0RQ3GEu9Vdf-7tot7IzlqoDKAumY-z2gWAPBGT_C9eN8Nq9lPd36XEBtWOUAcvOuMzHXNnBB1Q5XwUbpm0MvGTOTPyPXQqOxENKqRNkHwEX8cgiEN-BGj-6ZBn3unk6WmPFdIa57-oy8WE8UiEnPZe2LrU3mCcFsj3P9YGRrSYvr40A8nuzsLqVM09_nuDD999NCVAanB2tmZg5EjCzsLhWsSpBNep8ErQ3TIu7tlb84jFLkDvXvPcGfk2w7w8bDxSjtAtFBHqciDS2FSuZBFo4itdMb6cDLXe8PSjBtbLUN-7mj02LLx60rhH95jofnZsLGFAYUxvQ9oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5e82a980.mp4?token=JhDGablVc0RQ3GEu9Vdf-7tot7IzlqoDKAumY-z2gWAPBGT_C9eN8Nq9lPd36XEBtWOUAcvOuMzHXNnBB1Q5XwUbpm0MvGTOTPyPXQqOxENKqRNkHwEX8cgiEN-BGj-6ZBn3unk6WmPFdIa57-oy8WE8UiEnPZe2LrU3mCcFsj3P9YGRrSYvr40A8nuzsLqVM09_nuDD999NCVAanB2tmZg5EjCzsLhWsSpBNep8ErQ3TIu7tlb84jFLkDvXvPcGfk2w7w8bDxSjtAtFBHqciDS2FSuZBFo4itdMb6cDLXe8PSjBtbLUN-7mj02LLx60rhH95jofnZsLGFAYUxvQ9oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارلینگ هالند از مزرعه یه پیرزن استیک، عسل و شیر تازه خرید و بعد رفت خونه تا خودش دست‌به‌کار بشه و غذاشو درست کنه. فک کنم هالند بعضی وقتا یادش میره که یه فوتبالیسته با میلیون‌ها دلار ثروت.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/101897" target="_blank">📅 17:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101896">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kg3DhnmtOE5u4ZKBF_VQ43HD-82JZBFJl5GSm7U08lo9gqTb3kxGGqR5PNkQzWgBy82cu1QooDwfbZY_s3XFflWIOTuc_A-E2KlTvg5OxUOSxxBeusIHTmo7F5RnjX92f7lIijaSYKbaJzODUbVp3_kQCXutXQCxz7wslQsdyRjt0wHP6SJ_bIWcIpit7bbE3cvXdBxAEnRop_itC-xhNdSY9hbkzSg0_BjLd4gGatAdARPEmldAbIjhyBiQ05ndvVD8zdc9-SvFurudf7T2p_I3fk_dHaXDrQ7aYLQ7Wuo659PwarRJpxA11NupBSVhvqMrTqLEPHf1yG0pQdJhMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دیوید اورنشتاین: آرسنال در حال بررسی احتمال جذب وینیسیوس جونیور است!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/101896" target="_blank">📅 17:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101895">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ql3qiL9tugI9V_YHRphETtwCR6svsrP25wsAhrCT3OZGU4_5SoiK4EhyqGTaGIFvM587N2AYgqunhoDRBXZ5vFfAM14oi5TorgG9r8-usI1Slva7rUCMGXdo6OmHPrvX_iGImhWtbIYYMmCJWPkdWeewAajCHX5xUauiztJ37jcqutnHbHlQ9i99TIJfM60bb_5yTTa4TjZVWomScm_qd_WuPs3PFK3khTtwkhSZ-kDvNRAnqawVIvPyP1ijGOFjY52k4c62KkT2zGo2ZmkmLjmCbufXjgkh0j4gNWmVxC5U3T76XIb4NE6yxs1LwfTpWsHzVntrRbH5fah0YPVxow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
بن جیکوبز:
نمایندگان وینیسیوس جونیور، این بازیکن را به لیورپول پیشنهاد دادند، اما باشگاه به این پیشنهاد توجهی نکرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101895" target="_blank">📅 17:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101894">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c582a64e.mp4?token=gClpTm9CQO7ewkTQw4h7eyEg0s3eAxGjz4TRfpaqY1G0oOWMFTR64OmAeSIi8DH57IBSPr4zbGLTA49WP6bV279I3ltNpgRaSYGE12-sBzHCLkv-aeIhzXAi8W_xWpcwmHiX6XV5AXXnAXZAdBI9kI5pd37v1flyegTVEo7ayjghUj_6vqDoGfMWLWEsZchRcdJiokSRpzRtLqB59-N9n_qmc8vWdnzOew_iZ4pu2GuiSKUiWoWUw34SDDCoM-G9EzktWnZ4oJ1i1zX-z_qeO9hr8g9QRFJXnZwdPqqHZj_cWu8Gjo-SqpyKRY_WMXPLZwqm8w8xMCK2va3jUnNKZbp74oHVedabAUbL-W1tLplwmkQNhpWFI457tw_8Tm4sD-VsOsFGytm6plOppdhipHL76XM1J7owi8VZMQ0aKQRCo15lwW1dY4QiTD8J--z8QUwZiKAaxCdiJQBhYPh4ajhL25kCXEjh1LJLJHP4_4yIbPrkCT7kL_4FeMru5iZ18cDl1wif3etwNsBSYTwN8GM0AdYP7STQeZAFBYrZQxFmpkigqwKSk7dg8cS56T5x5avWmrbFgR-AzlOqs1namtnnnT4mjEPeGGBgCpKuGnO_1IaCn-A7XPY33PL0qbiTmg49QuXBTG3AfEQ5XcuNQYWZTMGWAhP_oCtrSim4YPo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c582a64e.mp4?token=gClpTm9CQO7ewkTQw4h7eyEg0s3eAxGjz4TRfpaqY1G0oOWMFTR64OmAeSIi8DH57IBSPr4zbGLTA49WP6bV279I3ltNpgRaSYGE12-sBzHCLkv-aeIhzXAi8W_xWpcwmHiX6XV5AXXnAXZAdBI9kI5pd37v1flyegTVEo7ayjghUj_6vqDoGfMWLWEsZchRcdJiokSRpzRtLqB59-N9n_qmc8vWdnzOew_iZ4pu2GuiSKUiWoWUw34SDDCoM-G9EzktWnZ4oJ1i1zX-z_qeO9hr8g9QRFJXnZwdPqqHZj_cWu8Gjo-SqpyKRY_WMXPLZwqm8w8xMCK2va3jUnNKZbp74oHVedabAUbL-W1tLplwmkQNhpWFI457tw_8Tm4sD-VsOsFGytm6plOppdhipHL76XM1J7owi8VZMQ0aKQRCo15lwW1dY4QiTD8J--z8QUwZiKAaxCdiJQBhYPh4ajhL25kCXEjh1LJLJHP4_4yIbPrkCT7kL_4FeMru5iZ18cDl1wif3etwNsBSYTwN8GM0AdYP7STQeZAFBYrZQxFmpkigqwKSk7dg8cS56T5x5avWmrbFgR-AzlOqs1namtnnnT4mjEPeGGBgCpKuGnO_1IaCn-A7XPY33PL0qbiTmg49QuXBTG3AfEQ5XcuNQYWZTMGWAhP_oCtrSim4YPo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔙
🔵
۱۲ سال پیش در چنین روزی، دیدیه دروگبا برای دومین بار به چلسی بازگشت؛ اسطوره‌ای که نامش برای همیشه با آبی‌های لندن گره خورد.
👑
📊
آمار دروگبا با چلسی:
🏟️
۳۸۱ بازی
⚽
۱۶۴ گل
🎯
حدود ۸۶ پاس گل
🔥
۱۰۴ گل در لیگ برتر انگلیس
🏆
افتخارات با چلسی:
🇬🇧
۴ قهرمانی لیگ برتر انگلیس
🇪🇺
۱ قهرمانی لیگ قهرمانان اروپا (۲۰۱۲)
🇬🇧
۴ جام حذفی انگلیس (FA Cup)
🇬🇧
۳ جام اتحادیه انگلیس
🇬🇧
۲ سوپرجام انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101894" target="_blank">📅 16:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101893">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBl3l_Q5jBx14REI-1SAUCq9_r_blW4obEyrKJG8UrAYbtxQimb8MW00oEBVKtH9WsquuzPbCp16_8MNeU-5ypJQQWN4gTJTUlN0X4kFWrSnTyeV1z-boJJDrLfslVCMmd1oKXdb_RnNr4AIVmyGccI1wHdqgIS3yVQJeynMBUeygAuVQmqvyjixvZR5Q0O_RLaCG76EdJtkHYWbRL8DngAPyUXRVlIeNZ-p84TQqYxlwujoVnndi5TDaVFAiwlzbHTjkM625VqXTNMb8uFWcfB-DBOlHf2WAA_X-GoLZzDLQWvvoZt059fNM9iwseN4Wnbg9F_jD8YIao1-mny6jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش مالی جام های مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/101893" target="_blank">📅 16:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101892">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
دیوید اورنشتاین:
آرسنال در حال بررسی احتمال جذب وینیسیوس جونیور است!‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101892" target="_blank">📅 16:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101891">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a105d81352.mp4?token=DC2DVZ4xHQ_VKQYS6IcdVJGOhVN3RHO-98bsSFK2q2VxggprJrbv1bqBSjlMtV0C_i_OK6-nDoebOi_lH4MrY3jogNIMxN3U_bxk4XTdpFWxBztmbCUpsP-r-b1iKOYU79eg-sz6KNCQmt4wSTOwIOZGlgFqoEJsMzLg2zbdIo6d3Ov0XdIeT3TcKJff8lOJSUTPkHd_uA-F06vWKN9Nq1AiDN6xOfWPhpixKU_PMxK9BUJcApFBApYzfjxvXtTlVadcjK4Z3EHweenBPqND9uhqra_GECu_lOcfYrhrXVyMa_y4tl4mVc-weBbCA45sgcqTMnZF6AlwQ7JsDU3_5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a105d81352.mp4?token=DC2DVZ4xHQ_VKQYS6IcdVJGOhVN3RHO-98bsSFK2q2VxggprJrbv1bqBSjlMtV0C_i_OK6-nDoebOi_lH4MrY3jogNIMxN3U_bxk4XTdpFWxBztmbCUpsP-r-b1iKOYU79eg-sz6KNCQmt4wSTOwIOZGlgFqoEJsMzLg2zbdIo6d3Ov0XdIeT3TcKJff8lOJSUTPkHd_uA-F06vWKN9Nq1AiDN6xOfWPhpixKU_PMxK9BUJcApFBApYzfjxvXtTlVadcjK4Z3EHweenBPqND9uhqra_GECu_lOcfYrhrXVyMa_y4tl4mVc-weBbCA45sgcqTMnZF6AlwQ7JsDU3_5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین مدافع جوان، دوست‌دخترش خوشگل
پسری خوش‌چهره و بی‌حاشیه، قهرمان جهان
یه مرد دیگه چی از این دنیا میخواد؟
😍
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101891" target="_blank">📅 15:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101889">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6wL0fdiET0aXrzsJ3n3NyZgsPZiDmLmg8S0pnW_N05Q1qgh9RfTWIDoD_-BMaHy_uQd6Fjt0jwbf5tF-hnpat8OqIocrYANAHvUo0EraeembcC_NIrYVAb1XoX2YCp-XhZA2tAo8YWSHcIYFIuzuNDhtV8SUFQfcPQlLHtNrDGW8M_f_q6U1pzW8aJjLqWgHMphTZmXjEapuOp03iZ_hb-mcQhWZyY9KQqXOov0jWtPTQk5K33seb7n28fez2STfXeacXYX9s-4M_V-YXGo7_zWT_lEW2x7XtsuUAsLK0cCfBMKJ309Qt38euU6uEPLh2qVId3vQnR--Zutpkfi3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmu810jdH5FHVaNcqgePD1muvVSt0piRfX1hNfcvHQpVm69crYegC95FNL2_xHSfkqoTXvZJqPpgDEgAvCewP3gZw2DI9RsyzqbQPnuZgBTS3eSCxePsn1mBxcOxSP9v1YO7xufLUsJpDbl6m5gHjjNrRqWKX-XRO_tGV2F69mMipbYOv0S677OiNNIC3V8D8dJwnRZL7ERJSbPQGlmFoYVxA5XRPaiFueQljgBvR-vqZjGbLzzs7TG_rx8LqmTjLIIolQIEzUJGC5hm-cr-2hX2xCRnU1BJFh5VWlFZ3Gpe1mUsA1kY1B3tBEwx4f85r8RZCIBe8IKkeJLTywFeaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚪️
رئال مادرید و ژوزه مورینیو این بازیکنان را به عنوان بازیکنان "غیرقابل فروش" در نظر می‌گیرند:
🔺
کیلیان امباپه
🔺
جود بلینگام
🔺
فدریکو والورده
🔺
آردا گولر
🔺
برناردو سیلوا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101889" target="_blank">📅 15:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101888">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHAVGAMBIgc93nwh-kWYeujH0cvTakmCV6bt5H5c81H_0gKOLFwYQiNLq_Cnz8AQ_BaLujh6q4bCv-A7VbVdhx8xKCu8hApWR3wNF5t0w-2JuBb7j8cboenLpHry_8Na10r3ZqsDTxekkAM9kGll6EjeiUq4A86iHjUS5hLE2WECBS2Uw2QxkgV54aS0Pe9UTd9DCWKO-bb3H5xdmfVAgoYr5Nszf14vGcJCfr3BGKLiiC3l9ekcKBtFclLoAHrvfYPGVeFopKU3q7VsxRaW57SPUZDbMzKrkz7DNLldg8NGUxK7qeI8peIT3ngLy8bQZsy9PRi89GSRlD4CdE8Amg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوری از فلوریان بلاتنبرگ: منچسترسیتی به صورت شفاهی اعلام آمادگی کرده که پیشنهادی به ارزش 100 میلیون یورو برای جذب یان دیومانده ارائه دهد. اما تا کنون هیچ پیشنهادی به صورت رسمی ارائه نشده است. و مذاکرات با لایپزیگ همچنان ادامه دارد. منچسترسیتی به دقت وضعیت را زیر نظر دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101888" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101887">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUmExjodjZArei_dEAFZoMPahGXuiCRl4R-lZyFrRyyPChyuKU-9JeEoFn2tUUef4UgCMDdCJ_hp8kYBw4NX57BX73oTav7QfLp-ksfdku_l5PIVBS1uM-xUV2uB7HZo_EE4IToEYOB3MXE1IG75tfKFsffkSYk4yAXx1yDFP9ukThC2xO8kty5-y25Kz698i2IqD0fxTvQW0e0hN9A1jhIncuovboXQPIcZjImBQ_uOwX6lhycDDDy0khSyfEF7bORe973xCmkT9elGsORvBfHs59DqWsq2mCGU_I0I416cfxr5GZTa7TMKgnRqyWjDzmDvEKkCF6CGkgdhAfSAiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
هزینه تیم‌های پرمیرلیگ تا اینجای نقل‌وانتقالات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101887" target="_blank">📅 15:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101886">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRYN4_4cFFt_7QzhlVtfOf2Hz0G2qfeJHez6hWsJQExyi9TGQf4W14u_l62J41IjFfdXe1d_905D1dCTfFxv84sDRce-mdbJ20B0zeRV-WwXCBl7_kqL-aEyDsZayUSLqJZCM0rHGEcMPMGNCTr060HSb7WlkIcFE1DiERxcetWWMbmftppr9C5_Ifl4sS8x-epFXplOH3R15iM28-UcXpdngZDpthA6BTtPwu_f5-PGrl1TIFcxrYFl7fNoxTOv_IyJuqlW14y7mjD0-YyapFXNKtoI8k-zAuiUHvecuFQ2etcvSbqxR1o_2vOiRD2OiU42crOcToDfR_48-BNAcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رودرا: اصلا بعید نیست که اندریک این تابستون رئال رو ترک کنه، این احتمال حالا جدیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101886" target="_blank">📅 15:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101885">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q72949ddhcmBpAlUcqJ_WGyyRvRWfMdKJGFzz_XFVUqo4jn6C45Xzu06gJI4fadC3EoLTOHE5sZzEMOAL7URsLXRRDlpDsa1N6NybV5L129_1YkA9x69lhX7uxoBqlHMrY-JWDVcrXzmf7XAy4WefIqChtuOGl9nsGWboJ9ytnahsHyUX5gJz-ABkijLqu5LCVj5cPLXOYOebwhWM45GrkjaPbCPuPgrajePa8-jfPkSaX0cd15_w2ze-5gkd4qnC_K6v5m0pyJVHjJTfJ9HdfHJwSVHN_JUvH0DZ1Dw-dxviJtn4UPwZd_8KT18oV9uxhPsIrBjcPTLv8cssk2a4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
سانتی اونا: رئال مادرید از شایعات مربوط به انتقال مایکل اولیسه در رسانه‌ها استفاده کرد، در حالی که به طور مخفیانه در حال مذاکره برای جذب یان دیومانده بود. حتی آن‌ها به طور پنهانی به مقر باشگاه لایپزیگ سفر کردند تا این انتقال را نهایی کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101885" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101884">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f29886b9b.mp4?token=dDFKXCt5EOxt5r-3dlzpzPxuMozcCtND-Yjk0QjN_6F9dERYWucaP4YPN1nz4tZGq6HWcpolkOulgDki3DDCGTTkjdMz5Myx-TzR73vFzX9uiw0xHMPkavWOTh_e5-ysE0a5qIor9d8fs1qOUkc8saU0k5D26DC7ORp84oEhMIZz6P6mg1NDVhLXc3-QMnaQsEBYWq6lKHfvsqNK362xmQPKnyKVl-JbUU-l9WSfyUGvyaIxsT2KQkePdMPOLUuxO7m-AkNWRWnibQvL7Y5UBzw1S-vw3sUEGeq0hS2-_tV26_8VeJk7wVr7d_U9bKP0oDVs6u-XCSAdU6cdchGE94K1pWzeNWlLzyIlEd9nVjFmIfaAMQxFP6KBGivAlVZRO-m8ABccoPnKpGSer170NVemANDFIeRWh8NxNTVWXuvsrm7F3NxF7CXLN4ohCF9YUL6l4oD4-_qKpEZNO7hoaTrEQRtqzNYEoCKEtLhWW4OXndcCqud7qAaRRqiVN3QxSKLldQ-zQQnmgrNZN7_K3BgBb9XyNqnafgUQ6gCAnQnLDq2G46t9wEOVnzXydXZsRtrHokAu9pg-Mbya9a-RosJNTqWcHbB23sbFH71aFJQ55JLy1hQgR9FmP4V4uwXfeAO2jolNa_Sqzhw4zNdHJ7ixt4102X4dbZ2n_Y_nJ4c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f29886b9b.mp4?token=dDFKXCt5EOxt5r-3dlzpzPxuMozcCtND-Yjk0QjN_6F9dERYWucaP4YPN1nz4tZGq6HWcpolkOulgDki3DDCGTTkjdMz5Myx-TzR73vFzX9uiw0xHMPkavWOTh_e5-ysE0a5qIor9d8fs1qOUkc8saU0k5D26DC7ORp84oEhMIZz6P6mg1NDVhLXc3-QMnaQsEBYWq6lKHfvsqNK362xmQPKnyKVl-JbUU-l9WSfyUGvyaIxsT2KQkePdMPOLUuxO7m-AkNWRWnibQvL7Y5UBzw1S-vw3sUEGeq0hS2-_tV26_8VeJk7wVr7d_U9bKP0oDVs6u-XCSAdU6cdchGE94K1pWzeNWlLzyIlEd9nVjFmIfaAMQxFP6KBGivAlVZRO-m8ABccoPnKpGSer170NVemANDFIeRWh8NxNTVWXuvsrm7F3NxF7CXLN4ohCF9YUL6l4oD4-_qKpEZNO7hoaTrEQRtqzNYEoCKEtLhWW4OXndcCqud7qAaRRqiVN3QxSKLldQ-zQQnmgrNZN7_K3BgBb9XyNqnafgUQ6gCAnQnLDq2G46t9wEOVnzXydXZsRtrHokAu9pg-Mbya9a-RosJNTqWcHbB23sbFH71aFJQ55JLy1hQgR9FmP4V4uwXfeAO2jolNa_Sqzhw4zNdHJ7ixt4102X4dbZ2n_Y_nJ4c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
امروز تولد هالکه و به همین مناسبت یادی کنیم از یکی از ضربات سنگین و پشم ریزونش.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101884" target="_blank">📅 14:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101882">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrA48L3vMpr3sQok6IgPvj1_Kca6NhnHl7cwywDr54aBVC7XJGmYu8FNWqYkiRYQUXueXQhgZ9-sFOOoycwtgb7ace5CJUIh733bSboucBoPRhqqFL8ZKh7vBDcFPKUvh2Qr1Hyd3KfnD2g8anzwo4CtIYY2fR9GAaKvYLoIkhyfijon4yCH9gVXug-OD0AQgwEf9rEjCOccFxvv7xBp9T-ZG_74I2ON2HYscIqpx5tbdr-1yO6uf6l29ljAbH_8KpPgy98iHeGLdO14lrw92DglS8HrwDLUISUP5ZqG81eeYe614js3qJzRWTXlLKa1Zs2CFtmXSCZVOSNRFWQsmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6342fd750.mp4?token=KVBJOiYnNC0hW5DRDwf4zB_kd6wo8mOP7EVBgvdRJE0zybaQiM7xAZ_GP_qLRuupU5XnaS-uIfG7NZc-gW22zUBK3R9AkwO27maxboXfN1ZFJsnGk237CHjUWHW7glC40WAcUkVyISvvMz_D-111NYIIXd6VZ4bWZCas0DCV34aZyDYwJIuhC-y5WWc5aQ6Mk0a5a8IuLKyKrtsyQT7jrmoftRZ4jEh9dPdUHBFVI5tjQcaIuDkKmif8DD2lj52TpCvdConHXOGYUGwqUZoqaXBozI1PuCnyhDnbqYYJU9Ihe4rAGgghH63jFT9uR-eDJLDRHsW4bQyk0IQS52GKGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6342fd750.mp4?token=KVBJOiYnNC0hW5DRDwf4zB_kd6wo8mOP7EVBgvdRJE0zybaQiM7xAZ_GP_qLRuupU5XnaS-uIfG7NZc-gW22zUBK3R9AkwO27maxboXfN1ZFJsnGk237CHjUWHW7glC40WAcUkVyISvvMz_D-111NYIIXd6VZ4bWZCas0DCV34aZyDYwJIuhC-y5WWc5aQ6Mk0a5a8IuLKyKrtsyQT7jrmoftRZ4jEh9dPdUHBFVI5tjQcaIuDkKmif8DD2lj52TpCvdConHXOGYUGwqUZoqaXBozI1PuCnyhDnbqYYJU9Ihe4rAGgghH63jFT9uR-eDJLDRHsW4bQyk0IQS52GKGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
هِیبا ابوک همسر سابق شرف حکیمی:
وقتی سال ۲۰۲۰ با اشرف ازدواج کردم، عاشقش بودم اما او انگار به من شک داشت و فکر میکرد دارم به او خیانت میکنم. وقتی دیدم نمیشه رابطه رو نجات داد درخواست طلاق دادم اما اشرف اصلا ناراحت به نظر نمی‌رسید! بعدا فهمیدم چرا؛ او تمام دارایی‌هاش رو به نام مادرش کرده بود و چیزی به نام خودش نداشت. این یه حرکت حساب شده بود و واقعا شوکه شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101882" target="_blank">📅 14:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101881">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/356f27159c.mp4?token=YwWrlExnDtYgSoDq2yAx9sleVhhG_6uCIJNMH9-XjJ6WhNuYQeokBvjnuD97KHMXxoYcAANZLbl4G_9_9vY_fhSMOAP7zfjfyNwPFUX7ZreQrSjWXPRNEP4KorKy44QOf4cgtOhUnx4FDT5uagYAsfnRD9k3Wpt5oJP0QsCXuZsxEarR7_EYlnjlxWbv1_hH-BfNO4u6yEcfPKQXtqwBqPZId1nplYIyM-KLOlBhwoOoLhsjeGv67HmkGDZxCcVvV3qQ1HjEA9o0puXCrWpWPAQxXp5jNZqCT5HndRVLZiX5f3ozT30OoHBn4wAfFVPRDQBrfCHW77YcvKDZO9nnxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/356f27159c.mp4?token=YwWrlExnDtYgSoDq2yAx9sleVhhG_6uCIJNMH9-XjJ6WhNuYQeokBvjnuD97KHMXxoYcAANZLbl4G_9_9vY_fhSMOAP7zfjfyNwPFUX7ZreQrSjWXPRNEP4KorKy44QOf4cgtOhUnx4FDT5uagYAsfnRD9k3Wpt5oJP0QsCXuZsxEarR7_EYlnjlxWbv1_hH-BfNO4u6yEcfPKQXtqwBqPZId1nplYIyM-KLOlBhwoOoLhsjeGv67HmkGDZxCcVvV3qQ1HjEA9o0puXCrWpWPAQxXp5jNZqCT5HndRVLZiX5f3ozT30OoHBn4wAfFVPRDQBrfCHW77YcvKDZO9nnxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هالند لاشی تو مراسم عروسی دوناروما هم نتونست جلوی خودشو بگیره و مهمان‌ها رو وادار کرد «حرکت پاروی وایکینگی» رو انجام بدن.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101881" target="_blank">📅 14:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101880">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_YO3CjWflA9x9MprGiOlyKs-zBozaLHVpKKtARIMAqLxUTA0lzYxf3lbNaWzEuti8nz9FpM7nSpuXHwOYZh_CVfo8nSJvLeo4OIlNhBpsckqEE5lL22zBseaUZOEeQhKPvhm_sJJzv0Zl6xGZCNfA_ffRrwRZrtwmWoIOBPgpyLCZv9Ea7K9eVy3XEB1dsLlyviGtJ6gV5FQaGq_UHBFs7lpugiOAA9lnTIkhSEQLpwtGwKgyCu44qoi9Um2Ft1NGeXpS_9zu93NmeggZhzbXwCVT686ZMjiFSohb0JVIgsrkAau7E9B4vMT-xXnx7mbOFf1_ShPXgqDfHPsBzLCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خط‌حمله نیست که ماشالا فلیک رفته تیم دوومیدانی برا خط‌حمله ش جمع کرده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101880" target="_blank">📅 14:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101879">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff0c27865.mp4?token=p2Q1fDg_nRqSNprOZUtYD8mMDGpVUxhVLFHOeIYvNKs7WdOM04v6WWKvtbk6aao9TCA5Mu6YvI0F3HiXEoIRc9dW7BvF1D1u12TyLJqqSNIwgYnCjB4giNfn0OnQ5H0_e4D4oU4M2lP7Qejeys2sW0eVqu9JXeDuXcJvn1mezEf5khkPohrkUz1KPtaR-4bLBZ3_RvD10-qDS8m2PscScI3yAju6a0ZwEC4EQbEMLpmf6SnlbyJkeFaN9C3qGrGWUfCRHycRPkLqLiYRZRmqCGObVif4P867wtNNNJZXW9TNKUHSrF-MRMsV1t_ERFYEI9K_E22Sho7UYA4RSLVdBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff0c27865.mp4?token=p2Q1fDg_nRqSNprOZUtYD8mMDGpVUxhVLFHOeIYvNKs7WdOM04v6WWKvtbk6aao9TCA5Mu6YvI0F3HiXEoIRc9dW7BvF1D1u12TyLJqqSNIwgYnCjB4giNfn0OnQ5H0_e4D4oU4M2lP7Qejeys2sW0eVqu9JXeDuXcJvn1mezEf5khkPohrkUz1KPtaR-4bLBZ3_RvD10-qDS8m2PscScI3yAju6a0ZwEC4EQbEMLpmf6SnlbyJkeFaN9C3qGrGWUfCRHycRPkLqLiYRZRmqCGObVif4P867wtNNNJZXW9TNKUHSrF-MRMsV1t_ERFYEI9K_E22Sho7UYA4RSLVdBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
صدایی که این چند روز تو ذهنمون پلی میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101879" target="_blank">📅 13:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101878">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uj8sCtsZPOF4pQv8IQU9LQZHp7S95JV-ca3-fLIqCizoQh2Rln0FfV32jB5RL_bi5OI0vOrUtO3Zfhatgyw5MC3jKCqiRrEuQ9pHfRUGM1wQTIaH20VlewwxQ5zt1V72JvfRQjYgwHVr9PIZ74yFv-sl340_McGVI32H0bgsJTHiQWm3mFFa7pRri_6aEdeoaTkpEkuadlT62ie74cysR8KV2tWkNvfmG6T9DsDqFJvxtGmZ6CPyn8oilxvkwOrN95uQlDniVYdOgKGVHPfdqgxAC8hmc2NW7en4RBeXsQRs34WIx7jdwBPJZCeqc2_gQ26tTTv-DT2NUaz__ePfkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇪🇸
ترکیب‌احتمالی فصل‌آینده بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101878" target="_blank">📅 13:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101877">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2d82d4a6.mp4?token=KGVaEsEPVF3viEc5wt9UipOJ6WqD_jPuV5sKIPpJoM_XjmiEEFhZakTDAgJFUy4LmOR8F3dEReNdqUw3DtWs5UcMP_PEeAIEJ-x_xc0bYR6gyUmY8Y4t-j2x3NupQADXrDHAug7CSijruM7_kBjpG019pX4vd3G9_i4ArrSMhMp0JITv_Gbvht3beTpHr2cWVRx_mP6yBcM0LHApzrafu4kojPSDU2xYLE7fFTjsgIjU569BULG4-BFmGjk3u9JkTXZJXF6f4a96bszBkMUdLxsaW4gLsRye166bzBB9sIMARKrlPQkLh_akKXJDL5S0CkL2Ivjn34I2KsGPbmp2zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2d82d4a6.mp4?token=KGVaEsEPVF3viEc5wt9UipOJ6WqD_jPuV5sKIPpJoM_XjmiEEFhZakTDAgJFUy4LmOR8F3dEReNdqUw3DtWs5UcMP_PEeAIEJ-x_xc0bYR6gyUmY8Y4t-j2x3NupQADXrDHAug7CSijruM7_kBjpG019pX4vd3G9_i4ArrSMhMp0JITv_Gbvht3beTpHr2cWVRx_mP6yBcM0LHApzrafu4kojPSDU2xYLE7fFTjsgIjU569BULG4-BFmGjk3u9JkTXZJXF6f4a96bszBkMUdLxsaW4gLsRye166bzBB9sIMARKrlPQkLh_akKXJDL5S0CkL2Ivjn34I2KsGPbmp2zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
مرور دودهه تاریخی برای فوتبال اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101877" target="_blank">📅 13:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101876">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705177dcef.mp4?token=qHvNRCVa79mxKkDrTZMWvePZ38mu2Ok-Ggem20Lw9NJpdq_YB01NOGAN-i1-CdzHaHabxieh64Zgu0mufZEkqCkLiO1dMv9zjA_JtzGdWkQgET1gpVnCtgcHhIjNeNe67kTHqMMrcBJSbGwdBt3ZvUUJI1CKnjUP6gMUk7I95GabFovHIAnDSJUP-Xcn709L6XZuF2qmzdD8wRtQjYRBbicgqQBEPy3ZG89r9fxhMccxzX0OHvuFdcdOFJcaP1FygRdM6O9EnvpwvrrxExK3eY4VOi0V9PdJ08RsRUNMo8_Ha0GV_KHio1Rr56_oObslLWvv24sFgDZuig3GuQwZCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705177dcef.mp4?token=qHvNRCVa79mxKkDrTZMWvePZ38mu2Ok-Ggem20Lw9NJpdq_YB01NOGAN-i1-CdzHaHabxieh64Zgu0mufZEkqCkLiO1dMv9zjA_JtzGdWkQgET1gpVnCtgcHhIjNeNe67kTHqMMrcBJSbGwdBt3ZvUUJI1CKnjUP6gMUk7I95GabFovHIAnDSJUP-Xcn709L6XZuF2qmzdD8wRtQjYRBbicgqQBEPy3ZG89r9fxhMccxzX0OHvuFdcdOFJcaP1FygRdM6O9EnvpwvrrxExK3eY4VOi0V9PdJ08RsRUNMo8_Ha0GV_KHio1Rr56_oObslLWvv24sFgDZuig3GuQwZCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
عشوه‌های مجری صداوسیما روی آنتن زنده که در فضای مجازی حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101876" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101875">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKwTlKEvSw6E-YA5_TDl7I2kOyJYViUG0Hmx8iLbxFSOOyMl11GB9WHo9pVlqwxY8C98jKOzPojXBPrDjlIXVLJkdH3WKoJbqQhqXoTawZRyTDpgpUHgWpgD9eNoTcVL_Kwi3-L8dmwcgy0heBAnRLcmbCompHowZP3Z87a6uhv21456Ayb_C-tQe2H9gH-m-IkK_ha-0ubnhDQFqzOvqzfpAGziZgmjSuQThvszcBJh_ezCzULBzFkkwl4B-c5GGeBTy5J7s-iiNvu-nzFJIDiXZwaFMZRFk9tPTlJBVDLHnk2Ym_ZTT4hchetmer7yA2hC78xGL0NWKIMlcQ0_5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
متئو مورتو:
رئال مادرید و رودری به توافق رسیدن
حالا رودری فقط منتظر توافق رئال مادرید با سیتیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101875" target="_blank">📅 12:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101874">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d9c9fae5.mp4?token=cT9-F8n9M8zwqZGZemwGFbULA5oAivgKJkoJCxFv0GAy3794o6eez5oJA6rTSD9xI506_RbuosFO0w6aS475mpEvlZj_mKUMqN0mhCI9crvy_cO6TIcSp6WDpu1ToGrHUzCN3va9lFkC1GyA1szbEG5ZX37Eoy8GhxdSKPijcqwdRzx1WCdfUfjq8y4CcuxOIEKMQRTgKa-qtsoD4y8UCROrfJy6PH1DPmAlgDNGO1yKp2AhTSmtYV3sr3pSUgyGjr0f9RyqFJoa95uSs8CrsD8LEj1Mwy_SDUTQsYQscJ33SIfE0jqkgbQEl20CppABkTC-43qnidn_ejxd1FG8nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d9c9fae5.mp4?token=cT9-F8n9M8zwqZGZemwGFbULA5oAivgKJkoJCxFv0GAy3794o6eez5oJA6rTSD9xI506_RbuosFO0w6aS475mpEvlZj_mKUMqN0mhCI9crvy_cO6TIcSp6WDpu1ToGrHUzCN3va9lFkC1GyA1szbEG5ZX37Eoy8GhxdSKPijcqwdRzx1WCdfUfjq8y4CcuxOIEKMQRTgKa-qtsoD4y8UCROrfJy6PH1DPmAlgDNGO1yKp2AhTSmtYV3sr3pSUgyGjr0f9RyqFJoa95uSs8CrsD8LEj1Mwy_SDUTQsYQscJ33SIfE0jqkgbQEl20CppABkTC-43qnidn_ejxd1FG8nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
🇪🇸
وضعیت رختکن فصل‌آینده رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101874" target="_blank">📅 12:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101873">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd5ea884d.mp4?token=TgioI9MzEHNCZGOLVSlmyhUG_q_JJrTJPnFQfCIEUOJZY5VRnBjdfak9Jxnr1GrA-jFgVb2xa-CNqlez_1DZeyzM_XtVoqDuqcWNNwiXjeAt9KZntLovrMhWxFFzQ2CG7v1zljDvX20PpuS5mRfierfxDsYSZXBFjXS8T6_30jFAD2x7KxPH-S7nxGo19Ym9yuoHwDgK1VEY95UNpWMz3ys9cI8ers4CJWLzGtmeT8d2zxgqHx4slP0fgAA9F6xyfnwr7-2agwwh86eFObT40jTf5Kn008GTO6YeopZfNvZDSIMj55tqAt2EBG04v-2VwCRA5tygL9Mo5PvnqxjBmoQILZ8dFITCxnzqCxVraVvXGKP2Kj7q7UoRJ4cvpcG6hT-ISArAiDNDVeZvALCBPb9LGKU_rphp2AEa07XB_-quy9ZwkwksfU77q2JEF4Kr0HOTX2uQi39JhbPiqpx85TxzV_cSJw_dPEPd7iSioSD9hu_dFdiY4NDe4uUvObqa3d78ONE5vWTPeYNocoisrTTRipF-DFEqS5z5d_efLqObG_4uQGkqiluiWdXdKGbg9nbWJpTyWfFULAHgDDpCBcRYxAon9igbD5fmJ98NHGUTnd5OCb9Y7XdNVMoQaUF9zw4cV4cWMPYrc_yuzTz98RdbGps1Kp-9n0P6urd6fK8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd5ea884d.mp4?token=TgioI9MzEHNCZGOLVSlmyhUG_q_JJrTJPnFQfCIEUOJZY5VRnBjdfak9Jxnr1GrA-jFgVb2xa-CNqlez_1DZeyzM_XtVoqDuqcWNNwiXjeAt9KZntLovrMhWxFFzQ2CG7v1zljDvX20PpuS5mRfierfxDsYSZXBFjXS8T6_30jFAD2x7KxPH-S7nxGo19Ym9yuoHwDgK1VEY95UNpWMz3ys9cI8ers4CJWLzGtmeT8d2zxgqHx4slP0fgAA9F6xyfnwr7-2agwwh86eFObT40jTf5Kn008GTO6YeopZfNvZDSIMj55tqAt2EBG04v-2VwCRA5tygL9Mo5PvnqxjBmoQILZ8dFITCxnzqCxVraVvXGKP2Kj7q7UoRJ4cvpcG6hT-ISArAiDNDVeZvALCBPb9LGKU_rphp2AEa07XB_-quy9ZwkwksfU77q2JEF4Kr0HOTX2uQi39JhbPiqpx85TxzV_cSJw_dPEPd7iSioSD9hu_dFdiY4NDe4uUvObqa3d78ONE5vWTPeYNocoisrTTRipF-DFEqS5z5d_efLqObG_4uQGkqiluiWdXdKGbg9nbWJpTyWfFULAHgDDpCBcRYxAon9igbD5fmJ98NHGUTnd5OCb9Y7XdNVMoQaUF9zw4cV4cWMPYrc_yuzTz98RdbGps1Kp-9n0P6urd6fK8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
اتمام حجت یورگن کلوپ با هواداران و مردم آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101873" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101872">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05d40892a3.mp4?token=YjCkhLEyMHDZzFeVnUR5-PSmkLrleZbS-a1KfX5Yjg2FYSvWM_hxeNHDZ3xkjjDOAQXs-GJyGkuOSDtbMQUrhZVAbzC9ysWxEbe4GMA8-EZgyrdKMz8j9WHZpIEDEAtPEsx7TR822t4tdIAa51J28My1LZtq4L5WwZzpiE4noPX5Oy8BX2tJoY7DWtadxgqzDT4Syol1QwwDC3zUtSkGauaFoNvYHNDkD5lakDKIk4C57G2102KvA9A62S98ih7NxPgNrcoqfz3QlekTSDLKPbUdxdr0MF19rLGEAwEc9ZO_2RfWxSHYf99MHWAeG26fwAfAEHPimK3NhzMpty82zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05d40892a3.mp4?token=YjCkhLEyMHDZzFeVnUR5-PSmkLrleZbS-a1KfX5Yjg2FYSvWM_hxeNHDZ3xkjjDOAQXs-GJyGkuOSDtbMQUrhZVAbzC9ysWxEbe4GMA8-EZgyrdKMz8j9WHZpIEDEAtPEsx7TR822t4tdIAa51J28My1LZtq4L5WwZzpiE4noPX5Oy8BX2tJoY7DWtadxgqzDT4Syol1QwwDC3zUtSkGauaFoNvYHNDkD5lakDKIk4C57G2102KvA9A62S98ih7NxPgNrcoqfz3QlekTSDLKPbUdxdr0MF19rLGEAwEc9ZO_2RfWxSHYf99MHWAeG26fwAfAEHPimK3NhzMpty82zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇩🇪
خاطره جالب مولر از بازی مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101872" target="_blank">📅 11:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101871">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOJf8g9oV0ovpw7RRH9s6Qy3ReeDJzxSDiuXyeZVfsWYToq9MKAwTFAoApuMWSPfa5NJuvlqNPlE_D1tEDy9hOx2D4ioFu8bZDN-Zyekci-9etVGpQMC1HS6JhBnHHVqHVobwYE0EHoteMTsv4uemVCjMne3IE-XfhINNp0ZWtmXM1L9UELd4WffOOX9WvD1qo06D0IYvfnOOEsig1viGXJkUfdwPSG39vC6_EqeY1TNE2VbRPWFT3xT56v41nvtIAGcPQf8Ne2DY482d_GqJOPKuRpKXfjVapqVjlUC23RDU8OHMN1T00YtJoAA3dh9WQIC4DVvlPhHo3ZmwreBCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لی کانگ این رسما با قراردادی به ارزش 40 میلیون یورو از پاری سن ژرمن به اتلتیکو مادرید پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101871" target="_blank">📅 11:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101870">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjC_de5SDrpE1aWrGnadUw7oVkst7FTi6BAXd_Ul5X6oCokzUm1AdzuYarojfOE2U81DNN2Q3eujVPC4FmjY5WYCpga8gzckTkr7m5Cqg1D7e_-eQfo2Cc9tHsFUyZoBYOj4bTfK5Vmgcwcuni9tBtE5NGhYIQ39E9hNJ32sK4u-15M6VR3FSIncXs7WeRl1KnCu5ZmTfopoP1wv5HG_6FA54brEuBfckb0IsZCSFaA1iwZGxGPCkQCClL0sOsds5cvYXAKKCA6TkusknMfhiDTp8bBt8yITFjQXxS0pnOh0d67w9YcuiXzJSsL6Nypl2bDxmFzA287s4Vyyr6rFCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
تحقیقات سه‌ساله فیورنتسو سانتینی، تاریخ‌دان ایتالیایی، نشان می‌دهد که لیونل مسی ریشه‌های برزیلی دارد!
بر اساس این گزارش، جدِ پدربزرگِ مادری مسی در سال ۱۸۹۹ از ایتالیا به برزیل مهاجرت کرده و پس از مدتی خانواده به روساریوِ آرژانتین نقل‌مکان کرده‌اند. همچنین در دوران اقامت در برزیل، نام خانوادگی و برخی از نام‌های کوچک اعضای خانواده تغییر کرده است. این گزارش تأکید می‌کند که پس از مهاجرت خانواده به آرژانتین، دیگر هیچ سندی از حضور آن‌ها در برزیل وجود ندارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101870" target="_blank">📅 11:32 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101869">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917b2cd572.mp4?token=hcla_6_j2BQVPKqpO-7bOvnbbMyFgc6ha6W9UC10tiQBQXNHiTRJDFU1Xq_Oc0F9aM3QEuSdQ_lBx5ndUH1ANZYb_jT9W2HC3GRYhixZF6p2MulIP4mXbFItiV8uF2XGlWnPzutGOvAw3bCmPfYiKNUrGunqN0TA8ygCPplIbZvWkmg-hzwp6NK00SohloIEKJ1D1E4HfxRrquQAS0WqBsnSeNN8delbn3XHWtT0oSq0sE4tgX2jk3U38cjv8qqk6T0uAdVsAs_Axtk_1t3gKIexniLoYMw3u_GGipEIVKYMVNYp215Haqi40o-szJnMM1bEA8mDvxbPTz-Tb3vAkQVWV2iK5pbbc9gDvnhmFzk7mio-0gbqVlG3DekMR6kzRMIyLnE_mFAAzs9eyMpzueX3v7TOhgz4NKgTfWXlJJT-mkBmcw28bptP5PlsboCN0N5dt5yEOhWKgcwnF5ff2hx-dTMIromnHmv_JLkOInI9Jkl8hkKdTyhQlp7qCn3VR6qR_ez9YEvD8Yb26tmJ2ionGFVjg5JyzaPmoOP9cOWyMEoheG4aAjwpejtyhzAuPJu-edMysSBQMnWTpHI3_PcgIJ4mfVCwfAqXakFXPqDYXPcmset0o1gYNyMJutJMPFpx0aADKubwu_RVnLTp_h3_rdfH-Z47kE9OeiqNRrc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917b2cd572.mp4?token=hcla_6_j2BQVPKqpO-7bOvnbbMyFgc6ha6W9UC10tiQBQXNHiTRJDFU1Xq_Oc0F9aM3QEuSdQ_lBx5ndUH1ANZYb_jT9W2HC3GRYhixZF6p2MulIP4mXbFItiV8uF2XGlWnPzutGOvAw3bCmPfYiKNUrGunqN0TA8ygCPplIbZvWkmg-hzwp6NK00SohloIEKJ1D1E4HfxRrquQAS0WqBsnSeNN8delbn3XHWtT0oSq0sE4tgX2jk3U38cjv8qqk6T0uAdVsAs_Axtk_1t3gKIexniLoYMw3u_GGipEIVKYMVNYp215Haqi40o-szJnMM1bEA8mDvxbPTz-Tb3vAkQVWV2iK5pbbc9gDvnhmFzk7mio-0gbqVlG3DekMR6kzRMIyLnE_mFAAzs9eyMpzueX3v7TOhgz4NKgTfWXlJJT-mkBmcw28bptP5PlsboCN0N5dt5yEOhWKgcwnF5ff2hx-dTMIromnHmv_JLkOInI9Jkl8hkKdTyhQlp7qCn3VR6qR_ez9YEvD8Yb26tmJ2ionGFVjg5JyzaPmoOP9cOWyMEoheG4aAjwpejtyhzAuPJu-edMysSBQMnWTpHI3_PcgIJ4mfVCwfAqXakFXPqDYXPcmset0o1gYNyMJutJMPFpx0aADKubwu_RVnLTp_h3_rdfH-Z47kE9OeiqNRrc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
درگیری خونین و فوق‌العاده شدید در لیگ امیدهای فوتبال کرج؛ مملکت بی‌صاحب همینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101869" target="_blank">📅 11:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101868">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KilJuhNOH3Q5oq1MfDqsTAD62C036RcGRoH5pzAuU8f1GxO4_qQ2Fe4vTpyxbrKBYuCcPg7o7OhF-h-FBoXR1Py1TU3Eqoqi_YFn6s6IXgRSw0x1ufcEWJrfNGkFmSAqCHYDgpgIOfgl4zIxwnQD0zcuZeFcTzQTId5k7foapBvO9yxOqpt3kcHLrLgCvSgUaPoJm3Ag6kkuLqZog_wsedoIB-sGRHvaD-HtNN-eLJElzytDgzgKW-7OQ_WFhMbpTNWajJIMyv2r1HL5XQS-vWUYEU1HJNuHg6OML9wuogvPh-HmpJ1tglVMf59NqKS-8S6GuRNhXqpq30lb9EAV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
👀
شاهکار سرمربیان اسپانیایی در فصل‌گذشته
🇪🇸
🏆
دلافوئنته قهرمان جام‌جهانی
🇫🇷
🏆
لوئیز انریکه قهرمان لیگ‌قهرمانان
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
میکل آرتتا قهرمان پریمیرلیگ انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
اونای امری قهرمان مسابقات لیگ‌اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101868" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101867">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f4c9480c3.mp4?token=F45zQFbe0Qtvn9zL8AhIqcJIHezhT3GXldsWa1FA7oqY3buxAy8Pka65FGrPkhQR4KZ-HGFiZGwHIOoGhdr8If_N8h5Dik1KHJbKHfQ1g1Ui658zSqoBbE_CWVpcBfs7Urn53Yk8Uz9whBJl-LgUzFEbWqI5k7Yq1M0izqSIClyEEuF9x-mYqP_9oaPvR2CWIEzBoilsNR6eVfJEc1VSkUE1bTEChEUocR-myKMbTFvegrUQVAAXzZ-cwSqGK-p7xQkt03MQTpqponiG2TtIb9uaiAStDmvjvWmnvL0F6KoQxELU8kclRhyiMUfXFxsHn7gcapfJdYE66rq8zNz_Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f4c9480c3.mp4?token=F45zQFbe0Qtvn9zL8AhIqcJIHezhT3GXldsWa1FA7oqY3buxAy8Pka65FGrPkhQR4KZ-HGFiZGwHIOoGhdr8If_N8h5Dik1KHJbKHfQ1g1Ui658zSqoBbE_CWVpcBfs7Urn53Yk8Uz9whBJl-LgUzFEbWqI5k7Yq1M0izqSIClyEEuF9x-mYqP_9oaPvR2CWIEzBoilsNR6eVfJEc1VSkUE1bTEChEUocR-myKMbTFvegrUQVAAXzZ-cwSqGK-p7xQkt03MQTpqponiG2TtIb9uaiAStDmvjvWmnvL0F6KoQxELU8kclRhyiMUfXFxsHn7gcapfJdYE66rq8zNz_Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
🏆
رقابت‌نفس‌گیر توپ‌طلا ۲۰۲۶ در یک‌نگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101867" target="_blank">📅 10:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101862">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vy2ELbnR650JJ1UdQLVkSS8oIAPnWcK-wKI6dgi1MRGfn3ESibVEilrA6DMZYoL6ZChmIVVDgJ5rLYLLG6a2jxgi1q2ifoWcKOxLluzaOLSn9B5ubLobntkD0Uk_RUaj4rPhfkm1DtbL3A6ID8QI1HpbTdQDLzlWqThgk14-MH9MDeIp1daKrq_C574MgCjcTCVW7laS2vIUi78m_4CZMWD-0txuAqs8HwdCjrXQmvCruFKwhvd0Q4n8VED6VZonnGANa9cbydze2DlZVOyoHjp3UIWJWDZpQ_hnv9doHRliCdbYxjSp8EOL8aC0rYQmwvcw7v8LiflcmbI9toMusQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIjIZo8tWd3hN1RskHtp5jUawjDLPOoU7zmAWflN1UN0yua34ek5Q87Xt1t57UMhGIOoIcypuSAJr92dObunJldTJT8KedUsNJebM0jF33IvoaI34a2k3HxGvb-TJ59-9uwEk3Aekux_dlZVbdJeKcJK6iPVEyug4iRtaOjTrn9dHePiHU-j9oNnc75XLqhkvjvV41lV-KDixSAgym9AFm7e23KOPC8EdgWu6KZGzR4u7bgjMMBOqNFhy0yZfRV2gAheapC-tuT71iE7FYBZIUwoqpiWlxIs9TTdY3wC7-ct6xdEBgTe9jEqsXUZPh-fc1-jZNBgYY5evzNnn-njDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WySnz6wrnk-ZHMVHGoEbufsN92uPhbmeBqElkVH8fqYI0E1QgU3R_knyyQyiik9YgydLT9_8X8PDjj_JniZ2L_JpiDtM0Kqv69ZG4CvdU-E53kRJcJb8n-ojs6gjWDHSMPtWjf7LXXpQimE4RtjDADkeGj00CpqxOMohF6MWz22l88puUt0AjzU2tO8pP9iZPre-_DX6T_dO2AfzYVv6blbvAjfMI6cgAujYgPvzXQLKiy4iq8KUe80XnNLK_hSw1BiAO30Vy1Lfxpl_b1w23EMP5OAmHmP3SNEA8OMHEICjjrq1WvQS29UlGv1e87dwEDXnvwbZJ6s4Rb-LQxr8bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cGnaOMa5Q7E0_wz_mz6nh2kAwXgWSdGAHzXSal9PkhBPrLu00gIk3X17YUpOH1BTAh5TYIURqk6zO1vDwe8dQ2UL_e5oBi7vfhSKsBMtM0BT6lzcCvXUbl4gAlPSS9HRSgDpMaKJMDhnEKIt_3UKMt5Z5hRgaGoSiIZYvLx0J55QrijHHTdksFm2whML6VDXpAbyT7GubuJSogfq2tS0zs6Ebxm-yFcMiaio2Q7HMDXevrUU2jWRrF-F85I48qsUeWlUSVZ0FO_bB4I3lrEjihjThEzo931J2qwomY6yfJB66_jayrae55qZw5lPt0-orgDkYqQZ2EUlWnJh4KUpKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPHl-3hOxt6JZxSaxy-sc5LCZERXI-VjrGKT_Lv1v__uyDHrUJjCZD0cYwbOnFyklK6pE1RUQRfhpVeZpJuy_NOygTZO2GWlzsuXRg4MixVlV2Q91O9CunSa3euhl8Xbo3JAqiUmGAs7zTLRGNmbehd3OljBini2guT4pLcJZ4w8EciQ4kLMe4wOE6A7FE4YN7HwsSCpunB7m1EfMMVBPmMdk3YTjKGj2JHOAeGu_sQcBMuqScAOOU-opVDd4xxl_SYpA3bezvOQ7uyDhUqn5mfaPqtw8fnfdH1yxVdGvPR29LZ4jxYFdLgO4A4VhuJaSII1LEy0DakKkIN4I83Hmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">+ قدرت تورم :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101862" target="_blank">📅 10:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101861">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d7ccd208.mp4?token=qPJCQfXkYLYSn6kx2IDt7EFPl0p42wXAi_Qo8mUsXVpQj4eX5yWRi_aAP_aqARpVezSEhQKgUnzuT-vx4mu2t6fM6aK0hmIE6Qd2zVQawVyrDxIdkHfYlyKWlVDomjlNv6xq1PGjepTX4kjrsq6rmZIqfz3lkDLrVdBySeww0s91Tzanxx3nPOqYqpfjTnjCQ90QybuURqOShMrdNBR4Vde16tzvH7Bf9Pmd7IQTfmPjTasrT30mNEVtPJgR0Vkym0EoOsmIQIVu7CXP7x5VEgoucMVznyRXyq4tfwxupK13cHT-RQIxgQj8QDVGZIdE5hNJaaQi3jPcew5K1d_PRAr7cWSavRBO91hcyxcp2-anhyKgVmHEN-hD9YtyjU8U8AOn-nQRdYnGQnDBrB5cCPLK0t6epSoAUFhjv6XGSZinbRAnMSnIGVuvHuskc_xy06wr5HrIPaWXt9J_xExKTZKev9p10-P_MuOmufAPh1kjsNBX_Vj4PR9Oi05jsmfawqa8crKgoNjGI3J20pXmkGPDYz-_ZR5xJqiuRUT1qOZ8R6v3_pmO54-LegpH7yXFII3dkHR-YLUzUJpkfno_AfgBgOOe6Im9-EHRNCVHFTkDTaCxIXM1K8zP2rigFTWogspYamzZmroXsO61qtZ_Lw8d5UcmGbvWf3fNR8QdpeI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d7ccd208.mp4?token=qPJCQfXkYLYSn6kx2IDt7EFPl0p42wXAi_Qo8mUsXVpQj4eX5yWRi_aAP_aqARpVezSEhQKgUnzuT-vx4mu2t6fM6aK0hmIE6Qd2zVQawVyrDxIdkHfYlyKWlVDomjlNv6xq1PGjepTX4kjrsq6rmZIqfz3lkDLrVdBySeww0s91Tzanxx3nPOqYqpfjTnjCQ90QybuURqOShMrdNBR4Vde16tzvH7Bf9Pmd7IQTfmPjTasrT30mNEVtPJgR0Vkym0EoOsmIQIVu7CXP7x5VEgoucMVznyRXyq4tfwxupK13cHT-RQIxgQj8QDVGZIdE5hNJaaQi3jPcew5K1d_PRAr7cWSavRBO91hcyxcp2-anhyKgVmHEN-hD9YtyjU8U8AOn-nQRdYnGQnDBrB5cCPLK0t6epSoAUFhjv6XGSZinbRAnMSnIGVuvHuskc_xy06wr5HrIPaWXt9J_xExKTZKev9p10-P_MuOmufAPh1kjsNBX_Vj4PR9Oi05jsmfawqa8crKgoNjGI3J20pXmkGPDYz-_ZR5xJqiuRUT1qOZ8R6v3_pmO54-LegpH7yXFII3dkHR-YLUzUJpkfno_AfgBgOOe6Im9-EHRNCVHFTkDTaCxIXM1K8zP2rigFTWogspYamzZmroXsO61qtZ_Lw8d5UcmGbvWf3fNR8QdpeI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
روتین تمرینی لوئیس دلافوئنته‌ی ۶۵ ساله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101861" target="_blank">📅 10:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101860">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025979a7c1.mp4?token=SS-q_oUQj3BcJSw0aV4eEguRyzTFDgVQawZqLZTWPPJn9M3sUoTNE5eT1DGQ2hl3NZ8ehKfRUhsycj-eosflVoBBg8A-DnRHAo9z6pNX8ULq3knN5_oxt8EXnACqOju2T76fUJjRJ9cqNTUZ4YtTdxl00VN_tj6hyHisKnJrSsexd_vj8pEElYx0Mhsccbm10hIQuQxgcm96uSGulyF8JVU-qYDh-20ECdDKvYCtAcjdhytQnijaRt_i-mWbxMgA8tE92A0-CBkVhCp1ffvovF22NaO1SM5UU6dYTm4jqvkshaewg_4uDRQcv3Pg0We6IzDJYdE1tLVVFF3FgwI2jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025979a7c1.mp4?token=SS-q_oUQj3BcJSw0aV4eEguRyzTFDgVQawZqLZTWPPJn9M3sUoTNE5eT1DGQ2hl3NZ8ehKfRUhsycj-eosflVoBBg8A-DnRHAo9z6pNX8ULq3knN5_oxt8EXnACqOju2T76fUJjRJ9cqNTUZ4YtTdxl00VN_tj6hyHisKnJrSsexd_vj8pEElYx0Mhsccbm10hIQuQxgcm96uSGulyF8JVU-qYDh-20ECdDKvYCtAcjdhytQnijaRt_i-mWbxMgA8tE92A0-CBkVhCp1ffvovF22NaO1SM5UU6dYTm4jqvkshaewg_4uDRQcv3Pg0We6IzDJYdE1tLVVFF3FgwI2jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
دلبری‌های لامین‌یامال و‌ زیدش بعد جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101860" target="_blank">📅 10:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101859">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/552820f16b.mp4?token=SV42dtvxcbK3i5WyJZ5XMWWhbjF9yoZFSI3Rv37iQULjeUJuZpOknb5zmba3D49-d14KWR6C25-3JrPnybGYM8ufuXypVfr2Gc8vgnxpOy9oGJsD-EsOxRg8pnliR4oVMzoRcscd9UF4H0FT1sUm0WAop7WhDdC7aB511Z0mmazIOXHsUH63VP_F8SB3wcAdsGDWwYh-7xAIeK63JC6yN0scbOWHMi4xxrkkK1TGBZ-5rHGXdGFHo4ehN1LUNa7npDJC5zvd6K6GMU2gDU-8ZhD16Q3bG-xAh3lbDJGGtDpA1lnBNtrZxIdCC-FzZPEPzQ13UW0rCXq9uLtQ6j4MWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/552820f16b.mp4?token=SV42dtvxcbK3i5WyJZ5XMWWhbjF9yoZFSI3Rv37iQULjeUJuZpOknb5zmba3D49-d14KWR6C25-3JrPnybGYM8ufuXypVfr2Gc8vgnxpOy9oGJsD-EsOxRg8pnliR4oVMzoRcscd9UF4H0FT1sUm0WAop7WhDdC7aB511Z0mmazIOXHsUH63VP_F8SB3wcAdsGDWwYh-7xAIeK63JC6yN0scbOWHMi4xxrkkK1TGBZ-5rHGXdGFHo4ehN1LUNa7npDJC5zvd6K6GMU2gDU-8ZhD16Q3bG-xAh3lbDJGGtDpA1lnBNtrZxIdCC-FzZPEPzQ13UW0rCXq9uLtQ6j4MWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
⚠️
بی‌توجهی یامال به دختر پادشاه اسپانیا که در فضای مجازی حسابی وایرال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101859" target="_blank">📅 09:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101858">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5533cc045.mp4?token=HImBatxNsTqaYawUIcd8TPdHYPdoTZCjGc1m5QNy-4eyzDvjGr6KkAneYYQLj_MpHzWxgiCES3oOI7XbyV2DNgGupdmoDsbOz8K-PuEi99rjigLMtshdlAOrcERT-C3Vy_B4c33Z2PhUhl7iN4sHmOiPLdScPnTFxEdOa58ymfJFTCPT_5Y5Auqm1Eba3uqAPhtx_ser9qOU78XA06MIxJ8Cz5Wt_yoUHrcNCqsVFj6gRh4OFYwW9W2o2y9kZKZS0FCJEYuHsUu9KQYa7CipmzGiNnjZwzp9J3N7HHb32aXtgSCF6ykxAI18EH-DhzZAtNqpo83Pn6Kz0kqIvXAlAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5533cc045.mp4?token=HImBatxNsTqaYawUIcd8TPdHYPdoTZCjGc1m5QNy-4eyzDvjGr6KkAneYYQLj_MpHzWxgiCES3oOI7XbyV2DNgGupdmoDsbOz8K-PuEi99rjigLMtshdlAOrcERT-C3Vy_B4c33Z2PhUhl7iN4sHmOiPLdScPnTFxEdOa58ymfJFTCPT_5Y5Auqm1Eba3uqAPhtx_ser9qOU78XA06MIxJ8Cz5Wt_yoUHrcNCqsVFj6gRh4OFYwW9W2o2y9kZKZS0FCJEYuHsUu9KQYa7CipmzGiNnjZwzp9J3N7HHb32aXtgSCF6ykxAI18EH-DhzZAtNqpo83Pn6Kz0kqIvXAlAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
امباپه‌هم دیروز اکسپوزیتو رو برده یه جواهر فروشی معروف کف پاریس و براش هدیه گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101858" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101857">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wi50PFadBJggR4EMgt01HxvZ8RgZowzGwTTc8oM0mg83fB-66PfwvdPsgaC2Qz2RHgvtzZWwzH-SmULjmwb3TcQ7bkkA2R1QGw8rx3jy0latXHEbTdBWaCtLKsQN45U8dqfMQof6nuU7PLrwOxSuDGcE_GA5BDqs5cDu_ZrRVHVCKSVcg1xgIlyyY_pEAVMtxbXcxtaErYjyXUzwSxAQYxQpziZk5aIpYaUrkP6scZimpd3KyS5Y9FIv1EaWBa4CYZuIak6WCM7tr0kFWoacsW0twsP4dPEjlH99VzQIbFbMefn_ZblVBhxEIIAA2I6Og84PWdwt-DTRYgHdagcsfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
✔️
تمامی کاورهای بازی FC در یک‌نگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101857" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101856">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحامیان_جبهه_پایداری</strong></div>
<div class="tg-text">این یکی واقعا معرکس و حسابی زده توخال!
#من_نمیتونم
@hamiyanpaydari</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101856" target="_blank">📅 09:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101855">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❗️
▶️
کلیپ‌فوق‌العاده دیدنی از پایان برخی از اساطیر معروف تاریخ فوتبال در جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101855" target="_blank">📅 09:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101854">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2e5fe7985.mp4?token=UYQVT5hdgRbCD9OrdyxDtIvl_Gi5UmiHOWgCqIttrkAzfKLgPOI7UMKIEV6JIRFOkGqhZIXqX8lt1AmEWjDNbTQvIK2-gt2wujGwJHO5cLfLTLutWRD43HKpAbreh-1EzYBWI0LrEsseqAlR2aQUwvjxgjR4IJCgU0aKP_1gc_IFUIGExM23nDgzL5Qq78H0pIsC8s4HEmq-STD7lnHqk4aQhlahX5bl_oxtNbUxzYeMcJtSzdA0kTCMxBvNVtKYFnmlEmdb9tc4xnrjtUhDGDi4y9mvMtqzvdrQ7dcSrTt9jBuuzNkrrCz61bIpoac-hheb8-Cp0jd5yxV2oP4cYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2e5fe7985.mp4?token=UYQVT5hdgRbCD9OrdyxDtIvl_Gi5UmiHOWgCqIttrkAzfKLgPOI7UMKIEV6JIRFOkGqhZIXqX8lt1AmEWjDNbTQvIK2-gt2wujGwJHO5cLfLTLutWRD43HKpAbreh-1EzYBWI0LrEsseqAlR2aQUwvjxgjR4IJCgU0aKP_1gc_IFUIGExM23nDgzL5Qq78H0pIsC8s4HEmq-STD7lnHqk4aQhlahX5bl_oxtNbUxzYeMcJtSzdA0kTCMxBvNVtKYFnmlEmdb9tc4xnrjtUhDGDi4y9mvMtqzvdrQ7dcSrTt9jBuuzNkrrCz61bIpoac-hheb8-Cp0jd5yxV2oP4cYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
✅
علیرضا فغانی: هميشه خود را كنار مردم ايران مي دانم و از حقوقشان دفاع مي كنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101854" target="_blank">📅 09:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101853">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmpFbXdl-ZMBhfy4bPPv69YKgEyA-8JVof7NXANzmUJ0dUwWokbRS7CXuHbOGMyJGNAqhh6_7G4Rk7mSvPtgXQSzLt31MIccadEcoy-0Z12Ff1A-bOdd8OPvBogjZr_EdEgsIVjAwDaePIyJUS340U0-pMkXiJ72bTkWkIO_JAbq_vKv0goTPAMdSbUZnBUzSo2SjC-I2fwD5q5HpSVgaDDzQLNX3bjJ8SfRMw0dia7T5dmVVUgMgVLElzlkVDjTGNssQ1qOgh9FMP2nkBab8aiPhjdvQjFYtlzwwtaXzUeE-OSxXkTxnKwbfTZZXBiiPS1geJW4y2Yp55mgOk7P6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رسانه ESPN: رئال‌مادرید تصمیم گرفته که به سبک بارسلونا، شاکله اصلی تیمش رو حول محور بازیکنان اسپانیایی بنا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/101853" target="_blank">📅 02:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101852">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7211acfa.mp4?token=sKFXjLsSc2NyYjcprM0oF4k9gNJsPM2MAucueDhrHgOSnZH4Gk8I8XlcUldfKpSsKsXp8wA79YA5pZ592dGpMdFfT46_uS0MglqegBVbj4-7Ii7LFU32FOKSaaqC87Sx63bxZe8n1o6EiiawBWqTeaBxIwYRslDlnywAJyPG0JB7k_36Y6GV4sBXA5a_ttjozqOOagGBVLh20edxdK5RlC7DFjPxqdIG1PhHt64X9TzTU45V2J7Mv2O9DVMUz2JF0Auat9y6O6TPfViK2u_zvQjL4kVbelKk3J-fZJoolk0m04zFqku0mqraJPf2RKtGBDd6fvjWJj1ol1R-sEmphg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7211acfa.mp4?token=sKFXjLsSc2NyYjcprM0oF4k9gNJsPM2MAucueDhrHgOSnZH4Gk8I8XlcUldfKpSsKsXp8wA79YA5pZ592dGpMdFfT46_uS0MglqegBVbj4-7Ii7LFU32FOKSaaqC87Sx63bxZe8n1o6EiiawBWqTeaBxIwYRslDlnywAJyPG0JB7k_36Y6GV4sBXA5a_ttjozqOOagGBVLh20edxdK5RlC7DFjPxqdIG1PhHt64X9TzTU45V2J7Mv2O9DVMUz2JF0Auat9y6O6TPfViK2u_zvQjL4kVbelKk3J-fZJoolk0m04zFqku0mqraJPf2RKtGBDd6fvjWJj1ol1R-sEmphg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
‼️
🇪🇸
شروع‌قدرتمند آردا گولر در ترکیب رئال‌مادرید برای فصل‌جدید با خراب کردن‌پنالتی امروزش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101852" target="_blank">📅 02:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101851">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INJ9FsGrZ09Hh5Weylq_ibGVL6s8jjhWqk6ZzvUvKjoRkyld8-UFxup07Q9YsU094PyciItQL6i-HFUNJgw3avzkMN4pZrHug2vxEhVaRifdfPQpP9sJgJ1a2ADwT_g6WPbAry6De9FOqD3Hqh39vcfpa-5PcMPbm2UCTFZTWeIMGHEJgQccRAFyF-xPbk5K4EquPWJrx8I_8WtwGSZOADxlrL_bYZlDqPACplHxFT82peqImiMmLCx-h_r03PulihHbjuZQ88El2YZeSHGfBUUxKTgd1-4US2vO40RcMitSH9utKx9d-D5eKLgOp2AmzkOw3LOAVPZdVfrRWiSW6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇻
بر اساس شایعات منتشر شده از منابع خبری آمریکای جنوبی، ووزینیا گلر شگفتی‌ساز کیپ‌ورد فصل‌آینده به لیگ‌شیلی خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/101851" target="_blank">📅 02:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101850">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BtYSK_DpUHue38D0BGDeFfDkCP7oph6oCuOI12rC3QVnYOAR6PHzugbi7vabsaeKtRLeYFSfW051Vj7kW2wClRy_2wKoY1AePdSg147YPNNPeqEOUgSPORp3bUxHT3zRBrt77DjfCq9d-_xGMS1ESjWmZswrjzMaH97ZTsxIZSSiw7XsDM99lXfsZPoZA7zMzUFHnbgf4CB9bJJYMALHrVXCqKkoiIZKu_xpzVNsAzomO2vlCeWTYsyzmHOl832pIRHFINJdi02ewKvUXezTPG5fY15RFGma7ELAJlyCmuvIWsxqy9sJXAi9ezG5C1KXdG4Ajfzx5cNt6gNIPikxdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101850" target="_blank">📅 01:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101849">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqyBiU2m4LvtlOztqgKSMu5kPOgUq91HhYDvti8ANnJcnxma0StXWAZbXkgr6Eoq5oeIp9FErniKwegOyR4sl7isHRGj_SK1oFreq71YRyvXpmmcqkjURafkezoAL0rwnG62s8xC9zBah7tHBdsXqT84mGIq7F-XIAVYwyHJUWqmsBHCz6212fYGwm1zGya3udcjU5To5HfvhAWzsivm0j5UqGsaT-cxYZBNg1tUVL5_jWU8padsT_az8AMFnHDjxgVz1EXLjbCPHpfbRQpby2ukGPDF--SfeX7x6Qq5gm0Ci8ZR5fxxN2KGF9vJyNnqxJ7Fo1W5BX3JXlQySgZc1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🔥
🔥
🔥
مارکا: دیومانده تایید نهایی برای حضور در مادرید رو داده. این بازیکن به پیشنهاد نجومی پاری‌سن‌ژرمن دست رد زده و گفته که فقط به مادرید میره. مذاکرات فشرده برای توافق نهایی با لایپزیگ درحال انجامه و بزودی خبر رسمی میاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101849" target="_blank">📅 01:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101848">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGLewYQxiVie6Y1mtNvfYzN4owB2bLNnRVXy97YG506QSbPnIb3qQ70yHQzrHGf2zEpu3pgsX3KjD7RAftrQWiqXzixWH9FtDgHLcQgVodfce4yKXa_eZRpL38Sw2xr20A6gHdouySjHQML1IR32zIJqVFgKTXelGy-XHytcFllx4PpVBrM4MBPVWSyios55tT0WVly3gUtAEK2fialBD-slEM5SUx29Fgep9FkdikKkmzBIr-Fv2l7zLeYGhRO5fTi_JfjSVu8eywAwxabv1TivTZJMyT81gBGaEggzhRf9K_CjtYojMjtxzRLHB4LDn35zAjwc7EQKpeZqnbSlhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز: رئال‌مادرید و ژوزه‌مورینیو دیوانه‌وار عاشق دیوماند شده‌اند. این تلاش پس از ناامیدی از جذب اولیسه صورت گرفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/101848" target="_blank">📅 01:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101845">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6nn1-QPX3mcqeJU_VYYM6PB3DfHMBgn-TrOmuIEVbuq403I7OqDV6hLU_Jr7vS_sxiwIfIg1c5pfCzpHzP4wnHtqVwuDme8bP2j7ddMM4LuxC9-xoC4LHg3zZ1nBnJc5Df_K741MuUwH74a2edO1_0ADDk0k6hK8vzs0n-ZbivY--ByRfjAG7MjLWZRODfCJ5ViPLVi_sveWfmbgq0xB44Ok9KDSeLFxJPV5o72dKifW78tBqKAQ8UcoAzR5xdFA1Q16G2eIXhMGkIrcUaeB-fkmEm-0nfgqLUgzoMbNuU7tqSfbAbZ11fQ_LreH6iEhugql_TYUeX42DdDjDE09g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QiGCxtcCywiv6GPYBhf7iJYK7UZe6CVAXiS6N2ddCm9MwsgpOn_-dp3370fBdsGjeIHvnrP2ozG-hq5n3cAvJMFzHO6Zp4LX2cRIj3JiuYLIiASZyE7v6f8VWEaUvXYHI_o0D7szO35VJjwO96GH5yBcOzgjorDi5FuSFUHTRTPD-WgUTIf7Oi93pIxP6afpKRLihvAkhsJUn7can_3p2ZQzsB-9Q2olrGjqHrg1xkHazYt0-oO4dNp3uZZLmFNZ8Gr6lD16eNR8Of0ICWadUQzYj_lO5xhSa29GjHSouCG58crwOD2OIONJwnBfhHYQ6a3gflCp0h8N3r68Bjrfnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
په‌په‌آلوارز: رئال‌مادرید و ژوزه‌مورینیو دیوانه‌وار عاشق دیوماند شده‌اند. این تلاش پس از ناامیدی از جذب اولیسه صورت گرفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101845" target="_blank">📅 01:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101844">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0JCkD4lJ541GKa05JKdUI22j25EQRgRN1sI8CUp0C75P8aN3bc7PqdKN-bF8oa7B-ZNk-0zPSkeND7tlhE0Ll2Nlt86SKAhxkmiJgxTg8hkluffsftnLQqN3N3AvT9zR4svKOkmy66n437PP7cRsEITL_pkcSfsz7ekqDb4BZID_U4YN315cJHV-egxya3qIWjAlO75FjTVFbZcESTvrJZTWT1n4vodvJjH84i49R1agCe-zHIWF6YEWQs9mjZihMyH2NcMWH3u3LK-sliBmW5qCaOUpQ3hepqccsEDZgiYc-MeDbU0UHA5YOa6RqzBapLY8daOoEY_ZqULdZwWow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
په‌په‌آلوارز خبرنگار مطرح مادریدی: در رئال‌مادرید برای یک‌فروش دردناک و غیرمنتظره آماده میشن. بزودی نام این بازیکن فاش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101844" target="_blank">📅 01:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101843">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH_iWbw4MhP9Gbm724c5RZsL82_qNQ520PKpk1pGpFOyZA56vsgGr45TqI7AD_e8mNH4sPQH382ewgYlRaSkWcn3h8WW8inb4_zz5n_YtVJ2kwPOBEGJYFCeKltJUps3sCKzSuc2yzdzAhkB4aUZZVOWrTQ-E-JrzTMb2fnNzF4qQn2_5yGxu9JPx94fxb2OGcD3ej2Dq-Y2DdWmyUwd9YlWrKCRjqZV5mF77wcTZZ7hlGL413-cdFCM_4tDd21jh6RN0wKpNBheqzvWr1YVnElaY2Dz1Frwj-vnj3rkzBEQQ7TmGAZ8UTf7EN_27O4io2Bp41nFPmIUXb6U7aQkmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
په‌په‌آلوارز خبرنگار مطرح مادریدی: در رئال‌مادرید برای یک‌فروش دردناک و غیرمنتظره آماده میشن. بزودی نام این بازیکن فاش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101843" target="_blank">📅 01:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101842">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
⚪️
رومانو: رئال مادرید پیشنهاد اولیه ای را برای جذب دیوماند به لایپزیگ ارسال کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101842" target="_blank">📅 01:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101841">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVwkqevbxBp5O0NU-1BMzWCapJkOGqbRmBRsZWkx35su1EygN06vDDl_HijBhtn7JFzatZoemh37dNQ3Y4EGZOUMVkk8VA3oyja4yy_H1-N9QHeUhYIntOBUZ050Fmgxx1u4Bqndk2Y-Ot-XrTILN7efXBZ_-FStOVa8UfS9tGgHqTjTkKkovym_ZDQjjKEGsLCmyuXZU-tkKBRH9rW84knxjTC6tXHLQxYq9dMKVnRRR3i2B3U522kKcxTBEhGhhOrisgNCWWxAsy37zX8bVDeq4ry6pyZdkG83h6N0WBlW_UjUABjsK6OUYzHGTJ0LdJY3Gb5X7CYRiTW2V6Ry4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیژن مرتضوی و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101841" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101840">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5SqU63z-RAJRWWECAeg3PAHefXQEnO1YKZJale7ubJ-hHyRGfKdhp_MKonz3Wqj4Xp_I-oD2AA6UwHqD4-i8OFt4dgmInYJClb6tSuFBoI81YvJQI9zqSMeazYMrL-rJY-_f_BM7amjIVDllz6mgDmEvAqUQA8xP819CsbkYykVa71_hXaC-Gcic8EfiT5UZRIgbzPSbqIx0DbE86bGLqcsINe7RiYmQgiA3Dj2llB_0mB-btIHGaUTXZ4YzW2zBaJy_dF9i1SrgBgCyPzuu5I-AQEbgOGzZJZtSzoBngGB4qt21b3ipUzmK9B3ZaLh-OM08PZ2PZ2OC-g1D-8VWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
رقابت دو اسطوره برای رسیدن به ۱۰۰۰ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101840" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101839">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQqr0E7LFgMThno9vvKw-LnOajec_nv_cC8UuSOqrtloNDvRL9FNXtobw4G66FVmg_GMn9bh4kD9u7yAvOWSeN_KX82r79g5CXkO8iT8ABlrFjBhT_5ebbJvgQzwKqHa0L7V3gJ4WD_OhGgWarihBF2ClvneRT2bAtKJGyI7NatOhTlAEbVp2lstnbDfqB2nFByviJqJi8oZXky_28IyzBlfMDSDv0wVlOshOh1gOPRDXA-3yo4A08QUAn1irqEA5Q3xDVGVyH9WCUFT1zXlnpN_oXIU5xmKTn3ja2SS67Ni1uYFoEExX7u0s7sxoqjVMAqIgStIcuZP9w3_e7RDMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رومانو:
رئال مادرید پیشنهاد اولیه ای را برای جذب دیوماند به لایپزیگ ارسال کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101839" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101838">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7brRQqvI9nkUCWAMs0KUxSb_q5Py7ik83m6vD08qCzXH-9qLvwaBwce_cp5mpY4bGgFBEjqU2GdikZL0oY5wBG4rv6CuXa27NCMlxUm1aojyd6tjtXEDzRbiyGt5M0RxKoZcTql9WrzmLGgoS1IiS40NAyjOI_OGSxV-3v5EA6qwwTzmFhtjcSZObs2XX5EIm-lxaNqY_TQXPxlKBbfRTMF3rLKEhwjxEQe11XHyU-N20HFgCKYm9DDIRA2lkanGBLhzpwkuQZja2jO40kZVBnej9r-76SUxl-AkI-O9Ej9u5rGsRw1Of6n4jiGeIn8czlruYs0oyjiswBJP-Emeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
بهترین بازیکن جام جهانی ۲۰۲۶ از نگاه فیفا و برخی رسانه های فوتبالی جهان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101838" target="_blank">📅 00:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101836">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4oDnyfnAtldugEgXWxGvp41DsFoxwuPvqZFlqxGMT7uUKNhnU3iJtGo4m8SWGzm5EqOfeIIGwkh23LtZ2AyA_fuCA7skubyo8iDxSpn_R6iThu49wodSTAXpvDj_eoAvUMMq856QDZn82tsBBexWsKYlnrlbsU5DXMRPCpRUOIBaph919G1-bfiyQhVob64y0aV8yQFV7nPHykljzEtB743AX8zxiaGp8tkTyfBeIul2-nvInE1Lus1G8uLE07m52lo_2aefT_kwn9XkJSE7y57CYbJ8ivrbo8x6uGmdQRD8we7i8kUgF5BCUXTpfRsy9i44or7svf4f62VnZVFFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تیم ملی آرژانتین اعلام کرد که لیونل اسکالونی به عنوان سرمربی این تیم به کار خود ادامه خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101836" target="_blank">📅 23:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101835">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlSMSoX1Nawkw8ZOdanAi28Aj0FXbDgotsvxAhQ1KjGuR-iAIzSYp-bajXsbqupLKIfDM40ZP8ZbpmQfV9COGqAjJ1FUEylTMH5f8uN39H-hgb1iillqh9-mm__71FJccZa0VU7_pWOPuNp12dwZ_Pd-COzJ8RzBBZe-N_dQtDnQ_B1fz5faH71DgrH00qE8pt6NzCpR93R4dPvKWjDQXOLz96xe6s_GrvuVqVzqzicHWm8hqSSirwrtQcl06MRxb-MqFC56AhicV0rOXL53RJa-LzOTcNvdU9C90-Lwrb6T2QBbCQTiwWQZZByrUhTdsxqicbtA1o7W5_0a_NKVVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
فهرست بازیکنان سانتوس برای بازی بعدیشون مشخص شد و نیمار به لیست برگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101835" target="_blank">📅 23:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101834">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhLoPX-LhR1R-eMdP9o6h5vXiWWzHAl6M5rG-_rJTldypHyZDOybDGUY04eATLL-juWmI7_adWtHNfFqvMPvKBgj9SToBCN6Wc4BLoQJSPxalaLEfZ9iT3Va2LJwAjBFf42PzD1MZ3FpEO8Zv6zQMiCJMbNuav6ElM2Yb716QBIXvpWTNYZSy_6zwY2tHmhBdaCco84RwXv5k-aQ_i96gtivz04aEFVQRWRygFFaKNkc7ZuuGqqqycVyGmWIwMaMET9Cl0L2oeQeiZSaG0egASnFkLigYBixfmRgQBQY6D7Qg8NGA4GYs2KKgnMgPkZjau-XwFjCDwoIPiKqIV4uqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لبرون جیمز ۴۱ ساله با فیلادلفیا سونی‌سیکسرز، یکی از مدعیان قهرمانی NBA در فصل آینده، قرارداد امضا کرده. این انتقال مثل این میمونه که لیونل مسی ۳۹ ساله برای فصل آینده با آرسنال قرارداد امضا کنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/101834" target="_blank">📅 23:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101833">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
دونالد ترامپ: با وجود اینکه درحال گفتگو با ایران هستیم اما باید بگویم که مهمات ما برای یک حمله وحشتناک به ایران تکمیل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101833" target="_blank">📅 23:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101831">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gcTqpqYNqFdk-EPwJ-pBovk9HKL2LYc62_LETYboKiHLRRfKrPh6P7_QcfVLenPLbC28Pyan3T_C-m32EgOEoh-XUJNNUnQRFvuCwt35A3wPdn6h5xV84B4FFziiwj92NCyowzxDTTrVOb60Qgsumw8lyqjThTlVDgPCoBxyoxJ2bOGOfxy23DjnmuRMrYI57XkyjXvYlAZWa2zk_LzzD1liZNnGhoFo3zY15rTS5aXGjmCHHRxttQYfXZFBiWreShvAeWlQMhYlpRRKgATjfh5mzR6xnYRFnkEHAbbA67gQKgpHFoG_XjJRy6vkKuIpCunHf0VQR0fmE-iatJXlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HQ4MrTKJWunmegLkib-w8OQmfQ7Sqg81lJ-MNmvfTgcohavtq-VARG9nFXCWC4bQ66mWdIEKJ0TEBXn_GKv7_OFwrYNLlKORNzyYwIVnRtNvFwLvUcMpkiYPnjXSnQaOJbT6l02c97YXZovGVB7yZF6qr7zSTN1QAgByihYxej6J110-LXC9sruhjkMVBGHl3t5a0NEfg4ElRZHS1IgQ9zxXCSwOAD6vfIwKJRGOJJ4lEOlAZypNiNm8FKT9SD8dj9jp64N7UiUy1GCJdtcEC6dpSoPbMI5DiAhoVGf4AKWj0mzvjH4OxyC27KrFmwTzQR7HYfl_PXz99_-YSEFqlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
نیکی نیکول گفته دلیل جداییش از لامین یامال، دخالت‌های زیاد مادر یامال بوده؛ از تماس‌های روزانه گرفته تا کنجکاوی درباره جزئیات رابطه و کلا مادر یامال علاقه خاصی داشته بدونه یامال تو رابطه با دوست دخترش چیکار میکنه! او مدعی شده این دخالت‌ها باعث خراب شدن رابطه شده و همین رفتارو در رابطه فعلی یامال با اینس گارسیا هم میبینه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101831" target="_blank">📅 23:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101829">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kLYCoUxM4CZl1PekRONdvbHT7S9yC2ZBp3Lc5_kFupxFmz0Geez6YbMRl488Y-VBxmduMOUOpUUBB3CNTFv2y9cMsbM1CLx6LJNsCPWKPkH-Yo074H1dTmKqYfkrnhcX8bPhWF0mCoItVi0WNBwn4taBbtgcAqk2KeTq1f02lfz3gT5g2KGnZjKlOQXahoD7ksW36wK8pVYKTS6di0aWxka2OJG5Rh_UzHz-0fSDZ_uhGMecXO7lTDHS6w4BKRc4FGItoYheXtb-HO8c6HnGZS1tOJWwDstMbTaVVK2mnUXFYLhCJEB31rTKmWj5AR6xhY9otH6Ar1RV_9up__1Gnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yz3UWgd2FqXshZKiOhNMvGEmCkTSFSVP5nDrYJ_N_oRqBdG1DigRS4b4pzJ0z0yAgzV_cVe3OBx1dniURjwWmD_3kj46GveZeZ52nfH3spg3e6GHeX4zAi_Vw3Q3Vt8hYtoiO-ajEVGJGq7rNYmCyb4gB9Vike5wAOCnAY4pg5cQq-u31s3YYDMubaQxcvqtMoQ-4u5sPaVBoz97RjT5AuvUaYQ9M7Nl_B2PAhOMiQA6Kko90uzP-pPDtRqrpMH9S4a0lwvKCeo72n1F-FspAv2UlGaLGHLxBk_ai_338sGDCIhmzd7u3QrR_qEMQWMnxBWs7yksK6FbsHJZSB4a_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔴
زمانی که رافائل لیائو تو میلان بود دوست‌دختر سابقش با استفاده از مدارک جعلی تلاش کرد ۲ میلیون دلار از حساب‌هاش منتقل کنه، اما ایجنت لیائو این اقدام رو کشف کرد. تحقیقات پلیس میلان جعل اسناد رو تأیید کرد و در نهایت دادگاه این دختره تیغ زن رو به پرداخت ۵ میلیون دلار غرامت محکوم کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101829" target="_blank">📅 22:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101828">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUq1lIDKGWvfho9JIN2Uui3xA2RiZdtiLfqhifOuFa_6YLSUI4fujCvcLLGqe9BRxS6p8bx68C-DIoc-Id00YMEtJqZNJKgO_SZNOoih5aTR0HkGIlpzxW1am-C3y_LsXejj6uMzEP35knjG5DdoK0as-EIVnPFek1B9Rfa7lUI4NxarJ6ivxNvpgrW55E0aeEmc-cCzbuEvJyUF3L0jtcq9h3W_espH9qNNUnzJMM5h3G8C1ewHv74fr7V8B7_RbyYxA8bB_fmmDY_JOOESTwjFYjc3uP_j_6F4oVNHc20AoqrT9dyWjToqUYjgoRAk-MrboSL9g6iCXluXlpYWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
توماس مولر در مورد ادعاهایی مبنی بر اینکه داوران به لیونل مسی در زمین امتیاز می‌دهند:
🔺
"در مرحله یک‌چهارم نهایی جام جهانی 2010، ما مقابل آرژانتین پیش بودیم و مسی دقیقاً کنار من ایستاده بود.
🔺
توپ به سمت بالا پرتاب شد و به دست من برخورد کرد. داور بلافاصله…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101828" target="_blank">📅 22:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101827">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlVeBk9OoShHV9dpJTR8nIrOXKMck690KfdGrRdVylGCN_15QJ9fOHbCiw3viiGs26dyvYbUILL76O4QzM4GQv_FI0XsTT9z9WtSxhKhMyMdTwKbqU8UpV0cr9nKwQgkHW8rVORm_A02Lpw6KJlgXW6kOyGhbVv40w8ZO7oYzea6uLJLNoP-YYZP7X1l0QEOgjbSsi9vD0C44LvjBZaBBxekJh2Hk08kOn9vC3jVBTyi7hrOyNolHrZWJGddc6vGapfl565pRDwMngOjCtvdH7h2X1fAcjJSxlFdwEoKbrnoSzey2zGukwDsnVo_jj0tHhPf-NRwCT_GvHQoI23sWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇸🇦
•
الهلال رسماً سامرویل رو با مبلغ 70 میلیون یورو از وستهام جذب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101827" target="_blank">📅 22:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101826">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jb5Z_b5mZQXbIkywL9ySKICXQlMjLfrOyNBIQ6VFMkha4xRoqGnGLqWLb3PceibBE1k3qD2NWDoDel8R4LlN6wizbMRtbf7KkXNDVL-YgKMgi0iI1wd8PuXREzDV791o-95kOvrHRUd4YeLiY9SbGPQZ9tCb6MyBFGbclpKARMd3CQpDwyeyFhPT0EK1v7Sg8rIsQr0oIMzO3aBVn85OJcTR7dSjatu32uWc9aEAKgPJxG-0LXmrfhZ7szXuJmYD2agxtkSQ0O1exZUCZmNiixXHnaU-_lnYi0pZHoAkG_XMLpka676JiSXEINdmNYJ7fhCwNpYaK_3JiZNI2LhQ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
دیوید اورنشتین: رئال مادرید قصد داره که رودری رو حتما این تابستون به خدمت بگیره.عملکرد رودری در جام جهانی یکی از عواملی بود که باعث شد باشگاه رئال مادرید تصمیم به تلاش برای جذب او بگیرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101826" target="_blank">📅 22:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101823">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeuuyrEeDaLXZl0MxGxIkkUabb8h1KtEv2cqD-7jWkfjE2vP8WUwsx53svVtya2xICXH9zu7utNRRMv4H4fZlWpSdxNaT8DNMsRNqfD4y1WYWsqxTmSvkVYUvwg1qLaasFdidvY0AKFj7LRYeG4VhUx1oHjK5FwAgDvjP6CIbc8iN1EFVC0W0W08HA4sSXhwQCosxCotNIpHcvLx-V2-NCrqicgkPYw5oGxd-KFsZlTOgcuHhrm9uYwaGgBZ5ufOAICQA1z6b8qvt3eWM3ThdrCk3s_J_CcYHX_ZdtQHfCgQZ3RdskCbHTNGEdviDD0NC5grpQnYLrqytpA8lTST5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
🎙
ووزينيا درباره شایعات پیوستن به اینتر میامی و بازی کنار لیونل مسی:
من عاشق فوتبال هستم. اینکه در ۴۰ سالگی هنوز اینجا هستم، به خاطر علاقه واقعی‌ام به این ورزش است. میخواهم حداقل یک یا دو سال دیگر بازی کنم. امیدوارم باشگاهی را پیدا کنم که واقعا من را به‌عنوان یک فوتبالیست بخواهد، نه فقط برای اهداف تبلیغاتی.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101823" target="_blank">📅 22:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101822">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXKIgc-n8LqSpoFT8-U9AM4KFZdrixnWyAZWjki4dAYKeyKXucWH2QU62FKo7GjcvEaEDf708WlpEzE8_WOT1RpohbzefKySf8ZRLoPGYK-y0o1deHDWmEs30dWIQypkIs6hvJl4feoRSF7XfdOGUib7Pl3BI2K_2cqTd0UAgR1Mnev-P0XLLlAp4UFjU67S7ZtfjdNkvO0sBVvWzrpZhBKl8VDGZlotIJziPT4n9j40HmrBAJFX8083TQ86Ycy5U8YLphKgUe8C7vIOQ48PuZeiSl6Uo94e8f83Bpt72oaGDmzGcMxOK9MDLXjxSaHts5aA7fAmvLAdSCVjzDgsPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
دیوید اورنشتین:
رئال مادرید قصد داره که رودری رو حتما این تابستون به خدمت بگیره.عملکرد رودری در جام جهانی یکی از عواملی بود که باعث شد باشگاه رئال مادرید تصمیم به تلاش برای جذب او بگیرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101822" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101821">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qrt5qbkic1KWUkQFvUZ50a5hyI9qgwdFUkxNynU35ghacRKK47OrN_kfgTCTWiNIcQJ_F_zaTfG7n11grAW9FTFHwQGWZPabyXDTPJHkhTbboIfYWM_TbtnUQ3s_FE59IAQtlZSdF2iFwMDOxjyafPLzW_CbXm6urSR4eqpgji9NMmxWsknSPmzzdBc6PQm1v5sj72L1sZyXSEFDICuV0IDA9z80FRE-66un8jsxCrbB1lv1fCNAprtd4rKpz-gSqIGbOQ8PACCy8BDlXM-dPAbwReflMJ138RbWsqcP09ZfqaEOYvJaJ5EF0Hzsg8J8zEQxkki94Sr1cXG-cBSYXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
رده بندی ۱۰ بازیکن برتر جام جهانی از نگاه اسکای اسپورت:
🥇
🇦🇷
لیونل مسی
🥈
🇫🇷
کیلیان امباپه
🥉
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگام
4️⃣
🇫🇷
عثمان دمبله
5️⃣
🇪🇸
اونای سیمون
6️⃣
🇳🇴
ارلینگ هالند
7️⃣
🇪🇸
پدرو پورو
8️⃣
🇪🇸
میکل اویارزابال
9️⃣
🇪🇸
آیمریک لاپورته
🔟
🇪🇸
پائو کوبارسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101821" target="_blank">📅 22:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101816">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C96X3Bv-8IDsDHuvYIfjzl4BMLUvFG27kGfjUpwgNatSdPSDsTkKXHiOzfKsIG-Sks4Yghmy1A8aD0Reo3ijAUNeRWIUSkFbHkN0QhwHFu_iMQ1liFIkwdL1USpor_ghfeOJD72ikfz4FwFunBRlj2btvKvLRwo5aOQ64aJMfVxHuLahwkoU4CeE4hnbCEL12n_dhcC4xlN4zdbeUlTtBsC2le5TlMJgP91sZTZp4719NidB4Pwk4PSLQJsRX0LFJh0-vcyxXm3dseaOkqHD6xbbDBOPWM3oreTKylpTxVGvGPQ3nuzh-miKXN7myuRsiuvVQHPuI8tV3JK_g_hqmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cP9W-ADuwPDCqEugHQe2LC_pb4b1MlV_eBcLLNVU8xANhcm1Bo7whYClmZ2bB138RJ_FsA-riAk6_L1RvYygDMqQYZ3otdj1gCnmBgEbV1o-flveI1KZ9Kr4rE0w70GXgA-7jGFNf2xH0l1BS43O3MJIUYXAzUu6RkZcfmrg4JqYbGOCrq8XTv-jM8l5cRQwZ7zYBCaj5AR51jw2sgD9sy9_24kK53xlSQpPpDxPXAc9A4x3lmZM_qkhjuvoDlSXd-WM8LjVunzM62bTyDfV0H1rK-ag_Kgq02qOcVvU_Q7zg0Fnb00_WRs7wiYwkH3xtGRkP2LkteBiFHWBnzvK6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QFa6aVzQrNetoYSz-iK80CeuhAfp5ViXI5ZIOXXRoLfp1R8OiBhLx7LFDCoXNVaCvcOQdEO1nkTaOYS-cpBaYXELUYKukOt4vxJMoWaWOVMGdqIqbSjs0Zr09MQpVphwV6gNoMGPpENVee6QIMTRycKxsOjgqF3jUbAc1EAvODXDigQUtkVEQWCu9mYruwX7fKp-WYKio46rYNkTmpV9uPEVVR6GC2IEoszVGUdPAgkUNfXr22iiVN7_zDPdQ1_yCTsBTzkHdLv25OdurrbyUjbq7Z5XBKwhh14NbbYGjux_39JXzzZB0cx_dd7Eiv7i3RL0KEC3VnOWFt6kpprarQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cvb9siU2_8VGXT1uDP7z2zBvdyJgfccfcQnQWfiasFO53N9wthB7lMguYmxkV7SL-a1n_nYl9nU2WfWralkrZUSYc1ARcz6JjG1mjjFE0Ql9L0s67u7G01YMJl3e0wVnxGdREHyIulfX7rPVQiibIVhTN3D0e2WfpKAP7FrLo4L9Wb-nLEvigM4jAyiZN03DDH2nfzQkzMdk_StJ_xPgrB04QW-3jqCQni_ItWqP7OImkINVBGPP3r-xEzcy-J1quizTyjxVv4ZQUDGCJeKnRz1IdZjf8FvGncZhhv7EcWVPs5swUakpsOwS7S3yZE6cs-PjH712Av7eTNnqx1XShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TbwFDzRHLvJo8HMIZ6nkrqxL9gXc-DeFX1Nf2XEeGM2AFcVOcfip5-xNujhBFvI8C5SoCGE1RDb1KPtsCvrGcrUfL2la9GuJ6zJiJ_96K4aZqxVKlgSiXcFkGZM_oILOVDf9nWQFSXnxUIC3bbumTrn4BGT7Qx3_Ut4AaYw853_i2J1lzaGiAI7ILfbK0F0wq-_XHfwvGvSrKjIjz56oxrk2VxfrL7ySBgSODXUPtHE1pYTOKx9S6pT6qyq8umDl0CnTJohXsgTjobtqwDzU-Ga14ec3K1OjUDaK_DmSokfdnwryIpaUIsJrGwKAkjfT4zQXWBv7VRBP6cbco4bT4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌈
🏳️‍🌈
فران تورس با مارکوس یورنته رفته تعطیلات
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101816" target="_blank">📅 21:54 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
