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
<img src="https://cdn4.telesco.pe/file/NaYoYDcsHZBrbwZvF_zML-F2Rh2bSDSk0egR5SWZ_orfqIl0yISySiD_zx0POliqOsvB4lHGSnCSW6_V9mcKa_G9lnYrRVy35oHzS5Z7WoERH_eEjf543qkFFygV8RAEL_Tkx5c57TKwadLX56Z5PjT_1qo1E4trpvpQPddPw13Ki0eCDwYSxXrJz3QalIMCK10JQe082LLGPRO3gWkuZjZ3RNVlRriyal-VpqsiZ_RAeYjqtnqONvpGbhq-g-GTAX2iZsYNWeEYFbSVQ1D_xKVvCCoOo9PDL4wv8gnBpU8uqHmZZTxZNEdAuHwIMCA-hNqElbR9b2DFh1ulErgZrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 254K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 17:07:54</div>
<hr>

<div class="tg-post" id="msg-84277">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzU3qmmh6WpCE36F4brIVwTBWiO6U9YYnS11t3mN_B4yBHV1YdOv4ojbUW-ZNRvVdWCaMsdwmpL06rEvgd7iuO85ma6dz3DBh-cmGM1XIVETbtPwlxeblQ_u0Kt6r1PTa5r02SnxXerByOfb8BvPPyVnntyzhMO6BbVGmQ0a1vSyo9O1CRamfLBeyZp2Kn5K-ZrGa8hn9qUSv1ie-9hHor2M_Qr_l0dspvTkBe0hoNWVNXmu4QO4mJkqoEgS5b-CxE0ohrlvQJZlEalpzWNlQjPzkgjISoMVb1iTz-UFoAltLljvld7jUbjIvFMOZSNtrCu3DpgTvm68OFvBWEfe8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f25717c9e4.mp4?token=MWpItvlKN0cdHmbdQ9aLp8qWAycWUuUHaVASi2IDOzjngR_O6AQ-QFAkgHKu7yOThhnNSxVzKpfS2qdV9P0kIx2HrrMG3_tboO4W_Q6hy_MBm-5akq583EwNjpbLHtmYGqVNdPXtGWeg9LX5HN8v5xVBMnwDkVDZ8fliArVHIyD4f5c4efIIQm1Xc91DTP5KEk_dXmdfIeldMd03jyF0TjZw1PEGy_fK7r53b03n5Xs5GwBluNt_RW1xquuL-rYuSbEoRodzH0GbUGRrrH6PZZzLqP_Fy328y2dguO9g7C0RGaK3gYc5hAem5LwOQwgjGdltlc8gjTszudig39H5qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f25717c9e4.mp4?token=MWpItvlKN0cdHmbdQ9aLp8qWAycWUuUHaVASi2IDOzjngR_O6AQ-QFAkgHKu7yOThhnNSxVzKpfS2qdV9P0kIx2HrrMG3_tboO4W_Q6hy_MBm-5akq583EwNjpbLHtmYGqVNdPXtGWeg9LX5HN8v5xVBMnwDkVDZ8fliArVHIyD4f5c4efIIQm1Xc91DTP5KEk_dXmdfIeldMd03jyF0TjZw1PEGy_fK7r53b03n5Xs5GwBluNt_RW1xquuL-rYuSbEoRodzH0GbUGRrrH6PZZzLqP_Fy328y2dguO9g7C0RGaK3gYc5hAem5LwOQwgjGdltlc8gjTszudig39H5qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید جان ناموسا تو یکی دیگه بیا برو کونتو بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/funhiphop/84277" target="_blank">📅 16:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84276">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مارکو روبیو، دیشب هیئت ایرانی که احتمالا برای مذاکره مونده بودن تو آمریکا رو از خاک این کشور اخراج کرد  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/funhiphop/84276" target="_blank">📅 16:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84275">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">واقعا فید کردن موها یه کلک مارکتینگی بود که آرایشگرا پیاده کردن، مجبوری هر هفته بری پول بدی بهشون وگرنه شبیه جنگلیا میشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/funhiphop/84275" target="_blank">📅 15:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84274">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کصکشا انقد به پر و پای بلو بانک نپیچید و نگید بزودی اونم پول مردم رو میدزده، یهو عصبی میشن فیلمای ثبت ناممون رو پخش میکنن بدبخت میشیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/84274" target="_blank">📅 14:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84273">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4XmltXoFCCQ6pi3wY1eVQQuGLE2kZdnE98auO9eVeYeK9EwmzgCycjTKlRYddX4gYWMBrgyi3FpP7zxaEbSGzcyqfmr-jbW5qwrGg0nfGGlsxA6nq0IjuuqG18QNjtTBFnXSAmozohEGFNLeZMgwAI-5yYhnqNXpyRT4w_8tPIkDaixsFJZBodBOS_O_oGkEQSiphEuK1DIu2Am3JJLZwPjNGLp9cpoRkC_KUmn3IoXcLpoQCT7-8Qj5xMxUKKBS_wI3SaAseBGufG8I8DHtlEAwRJ7is_9v2C-2YFUtS7GBCUf5TXKeUSJ0UOAMRjo0wRc_pMyqAUHUZ_SmCD6BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو بازی دوستانه دیروز کونیا اسپور و تیم ملی فلسطین بازی رو دقیقه 89:59 متوقف کردن و گفتن ادامه بازی زمانی برگزار میشه که فلسطین آزاد بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/84273" target="_blank">📅 13:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84272">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e053e973a0.mp4?token=eb5_OuvDdDKVYZ3pKNaYgVRgp610TIOP_Lnx7_8MPh5KVWqRuYKhnCA64YvLhQb0Y3SBEx0y3qpcj5d6Z91pm_2xgdgEdzRSQjZ_7qzI4W0YnshLvCwGcP9wSK7iMN37YamQioz4NyPsxDx2P062tbKwQiFMSqgQUpQc9Xq9SensS3K4EW4ZmCEVi0BY3Z2sxZEKNmVJ1TizhAY9fMb2RNvBbdKpl97d9A9WAgbFnv01IE-Trq7O2xy5yYAjPYqOQEzIjRYLm3G-vFzyUkyU4pCrFzAYB1HydOmHJu0PgqccTTJ4w5TBsHNnFmGXF5ZrJgSq-hQ0mgqaWHqJNoJ4SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e053e973a0.mp4?token=eb5_OuvDdDKVYZ3pKNaYgVRgp610TIOP_Lnx7_8MPh5KVWqRuYKhnCA64YvLhQb0Y3SBEx0y3qpcj5d6Z91pm_2xgdgEdzRSQjZ_7qzI4W0YnshLvCwGcP9wSK7iMN37YamQioz4NyPsxDx2P062tbKwQiFMSqgQUpQc9Xq9SensS3K4EW4ZmCEVi0BY3Z2sxZEKNmVJ1TizhAY9fMb2RNvBbdKpl97d9A9WAgbFnv01IE-Trq7O2xy5yYAjPYqOQEzIjRYLm3G-vFzyUkyU4pCrFzAYB1HydOmHJu0PgqccTTJ4w5TBsHNnFmGXF5ZrJgSq-hQ0mgqaWHqJNoJ4SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آ
مریکای جنایتکار با انتشار این کلیپ و نحوه شناسایی و منفجر کردن آدما با پهپاد، ایران رو به جنگ زمینی تهدید کرد
.
تو این کلیپ سربازای آمریکایی وارد خاک ایران میشن، و دو نفرو با پهپاد میکشن!
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/84272" target="_blank">📅 12:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84271">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مارکو روبیو، دیشب هیئت ایرانی که احتمالا برای مذاکره مونده بودن تو آمریکا رو از خاک این کشور اخراج کرد
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/84271" target="_blank">📅 12:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84270">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">محسن رضایی: قبل از اینکه انتقام آقا را بگیرم شهید نمیشوم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/84270" target="_blank">📅 11:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84269">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
خبرنگار حوادث : دیشب تو تهران یه مرد جوون بخاطر اینکه زنش قصد داشته ازش طلاق بگیره با یه گالن بنزین وارد پاگرد طبقه اول شده و آتیش بپا کرده
تو این اتیش سوزی، خودش و خانمش و مادر زنش کشته شدن.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/84269" target="_blank">📅 11:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84268">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUAciDp5feGZPrWJSNNdqrpG6aMLO-aS2WsXMBS0JdO4TRbW10sI27CR0l3xqfboXkMVYxWfcYUwrxFWKv55CkVjmIdUDjODqp_1GMeNW4nTR4S49BH9jT1VehRj89EDdS1hvr5MMH98i5ZQl38BSLJeUNW4maGNessrJbi1ZXhJ0B5jh3AUdYdOMc42zZpaGhHIEbUPqmWL4-h02K9OdbBnPtLdSTAlUCzVQzyjxoyZOaqBn1hWzIl2cYRhgTw8uth79A4J23qqjsNOyL6dkBR80nQl9jiECWKkEE2PDI65xG8J-HCTNe6f8-Gs1shNKupHzbTSW4vDlPRMR58SRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط بوراک میتونه نجاتش بده
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/84268" target="_blank">📅 10:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84264">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGSP-jZ4ohTXyQ88RFBD6ETNQD_mpkmzlnTadBiPgz9LMyAwjVDyY0xGAZ9dNIViU7tS5aFeiv6tw9c-Q2FppfiDfMUggrvC906cSZPxkiwBpweR5oTMmR4YbJwVBTQW-H1RqNuFYJ7G4JNNNKyP-mTk9d0tuN2i0T5__W8PmzxRPgAQcgxSV09nmX8hoKHeQ_VTesT_j7i62kgRhg95W9ClKUseXISKIO-8S6xptGvmzDw5MJt-Ije5zDJ6QpPkxFjKvKHdFK4c77rnKvkzrhclHbtRyX-83E5hLsOF5IuE5n9vlKLNGaWmklb5NAwMOu1L7-XBTw3YFxiZ2tQPYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEJ4Y2ytRHKikfG9bdUejlHTuCBNlpol-38uPKiGg8pYB9SUNeTyA6ftBznFIsNMNJUsWoX9k-5CQCFivOkwVg0-DSyS3PbRp_ZtoW1mZtoSEnKpXNP-HezoPfPyjQex8jco_jFKjpHkHFBDmV4PANe56O9MHrvUH9-1ahJjCYB1idQ1xz7JGJxrjFpdDhRcaByJXmOyAIM9SysqfCvOGGzIc8PJ9NtkXAn6qsD4XZd3OnTaI_EeFA6w4zO9cAj1ds3I4Hjv6_GulsHrHl-YkNjVn8BTPC3ZPZidv6z0wQT9od6mnaFpEyrwfD9goNZEN2uxj8aiXXT0Q1KJZmj8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kzIQ9F65nYF2OS7bCF5lWJcA-LMB_Fs_h69QQPZevBb-0xchGcWP-1cXADnnEzHCVwji2jDU0CNB4uxUxCZLbJrCsSG64B5m51s-Ww6lPW4tKsU6n-V3HvMWi63emF3ABHY8u2BoREHUoymOh2jKI-lr1rWD7zPdHEIBUULNjkk8x9q_ygqwIjx0gHaLyRPJaqJvaobjqvr8EjRKEkA9h4q8IWLKPKbRZoqzR_DD0ufMKL53wwvHhEguiEVQ-12cAvqLT6Z7fvCnZw4oJNnR7RljEWHhBGpOwiavQiYjSWvOcFe1QejF3CVMh0W-4vPwlfyJnC_p-tdHwPQqoJOFcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zkuk6ccth-FLyjV5hH90WzRNwqiz3we4tZFrew1g6mfS8jKkLpQ-sg8kYjOBbc37oNxtnlBWUPHGU63PWeWQ3-XyS6hwu3qaBmbLu-Ebf_X3LWQ8vDWOZm5HGGhftIz-k2mTM_0NSOAhHt24JiqLfh09PMIHgaPDowPVl6eCFVLczgNyIS7yqzKpqNneJiBXtplU_Pg7vT_-oWa041NLsuH2aBkUXjBw4Augx1LIZQbTXY32CfyspV-rQayRNmaNwohsC_VgM7-IuC3bIYX7dIX-20gACewZblh3am0Tb1QJH1nd3FB19a497WOA-2ZAait-B2EFSPLJHp7l6CaL6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های جدید بوراک
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/84264" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84263">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84263" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/84263" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84262">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4obcY16zwjZUg3-kJSDhSM0ULa9sRcycxojdwmAQ05csBG0e-uHXThnXhkupXtpA480DPS1-4sCP60D4UHd0rqPbTlxijPpRF_tixSv-nYi_U-2fB-P4EMSVcr3l1bTAU-s-XM_B9Z9eX5ItdD0Whg1_DbUdexm049azxtZqyseykYYsd1O_TSfMTpfK12vy6cWveiG3I_umTyn5Sn8gn4EqCUT1V8cExb-tW9NbbKxo2a1a5BJNInpiiHtnZ0MuTDZWMeXYrzvqirBiKSzTRix3dKj5wqlbK8C_7pampyPoLXLstYrgXtVt5A22-h4da6QagE74qVNwcLZSdGbZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👏
یک بار شارژ کن ، دوبار شارژشو‌ این طرح اختصاصی ریتزوبت برای کاربرای فارسی زبان خودش رو از دست نده
🔵
اولین پلتفرم جهانی و اسپانسر لیگ هلند محیط امن و حرفه ای برای عاشقان شرط بندی فوتبال
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
r9
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/84262" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84261">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">در بازگشایی مدارس امسال جای خالی یک نفر شدیداً حس میشد، شهید رییسی اگر زنده بود امروز بعد از انتخاب رشته مشغول به تحصیل در دبیرستان میشد
💔
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/84261" target="_blank">📅 08:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84260">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49c29e72a9.mp4?token=DFprKXiUgaEEWWDXkv08DKvqVNDfF1KKdwgKtoVjJRKdysRZTq_kOGGDA9BuM7PtOM2dBrK4PmMm5l5C6_RsGfYmyS8QA-Q2fnluaeoriNxJDPOjTmobbT0LDPIYN4LF-8p0FhSFmpXNwYjpiHAX26MRgPYAQuw5zCp1XIXobgsrgw9Or1zDiYgvsMqBRvlCAxrAdWrntBYWt1Q5rErNK0cGc_oAoATtH4Q0YBbL8byQ22xeGlaemH2IxphdQVdzqsS39kSMVg9T-vlEU0kieQk9bvQwCl2T0w7I0o4LOkfi75ZvGH8HFjcrQ6jjt5A0_7ehriIuLYd42od34gSyMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49c29e72a9.mp4?token=DFprKXiUgaEEWWDXkv08DKvqVNDfF1KKdwgKtoVjJRKdysRZTq_kOGGDA9BuM7PtOM2dBrK4PmMm5l5C6_RsGfYmyS8QA-Q2fnluaeoriNxJDPOjTmobbT0LDPIYN4LF-8p0FhSFmpXNwYjpiHAX26MRgPYAQuw5zCp1XIXobgsrgw9Or1zDiYgvsMqBRvlCAxrAdWrntBYWt1Q5rErNK0cGc_oAoATtH4Q0YBbL8byQ22xeGlaemH2IxphdQVdzqsS39kSMVg9T-vlEU0kieQk9bvQwCl2T0w7I0o4LOkfi75ZvGH8HFjcrQ6jjt5A0_7ehriIuLYd42od34gSyMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده امارات در سازمان ملل: «تنب بزرگ، تنب کوچک و ابوموسی، جزایری هستند که بخشی از امارات محسوب می‌شوند و تحت اشغال ایران قرار دارند»
پ‌ن: بیا برو کونتو بده ناموسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84260" target="_blank">📅 01:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84259">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ: میخایم بزنیم ،بزودی تصمیم میگیریم
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84259" target="_blank">📅 00:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84257">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85208a1d9e.mp4?token=R4VRBxQVo0HFfU-jSFYu4xI1mrmmcMCFOoY9G5xMRawm3T_0ZWAmS7hFrWqLgzrk_0GPTTqbj71LW0Uc3Hq6Q3-D-73FfXklRRZ48Z62e658D5MIFHAYlYBJd0bWBvVJtSfyIs5zq-c5uv-0wAsknf3TWHnOKiXoGUcGdaWaEPMnJcaOLZrRWdfEgk5v-LUr10mYt8gBKEpuBmMpGWn7RXZAd25n-56D15gd8biKNR_ooKIgQk1eeTLssr5fa65x2UUP2FmHYzztFN2KrWVQeMwuUfjCBECXl8eDXaRucKAZC6v-D65NLlDPVtGzxtq3uXMuFoSzt0A_E2JR_aQUog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85208a1d9e.mp4?token=R4VRBxQVo0HFfU-jSFYu4xI1mrmmcMCFOoY9G5xMRawm3T_0ZWAmS7hFrWqLgzrk_0GPTTqbj71LW0Uc3Hq6Q3-D-73FfXklRRZ48Z62e658D5MIFHAYlYBJd0bWBvVJtSfyIs5zq-c5uv-0wAsknf3TWHnOKiXoGUcGdaWaEPMnJcaOLZrRWdfEgk5v-LUr10mYt8gBKEpuBmMpGWn7RXZAd25n-56D15gd8biKNR_ooKIgQk1eeTLssr5fa65x2UUP2FmHYzztFN2KrWVQeMwuUfjCBECXl8eDXaRucKAZC6v-D65NLlDPVtGzxtq3uXMuFoSzt0A_E2JR_aQUog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یجور هرکی که فکرشو بکنی خایمال داره فک کنم اگه استالین هم زنده بود خایمال داشت، یسری بودن که میگفتن قضاوتش نکنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84257" target="_blank">📅 00:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84256">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وقتی از زندگی خسته شدید به این فکر کنید یسری هستن که بصورت جدی موزیکی که توش میگه "بِچه ارچره من بربر" گوش میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84256" target="_blank">📅 23:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84255">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9caab26da7.mp4?token=CIGvmvJRSD0dq7n8PIVP5L1UrIA6dCvRinmUiDpU4k4gtTGQCSLXWRqTM7ZIxEbpvKugEuFv0vhFWvBcdjoTR52TYGfSwOXXJdkvZwkACACxcod8mvCybq1LC5UevXkq8JcNbDci1SagFFLg4D2WBiSc9DdIzAyNabHNlUtFvXhAjdhQvkUCpmYa-cJptoGlmp7pfPcT-e1AfEqKUz1LEvHgNXBhsH3vQ-YdaENi5cYp9Km_iqMUms6XWoef3QhbvA32mFms7NqEtKyUnMwtHzJZ35TRsCh-7okgBN3hIZXRkX9dmxq8vnbPeHKkAwGSw7QV2DAeL33a8eKGh70wRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9caab26da7.mp4?token=CIGvmvJRSD0dq7n8PIVP5L1UrIA6dCvRinmUiDpU4k4gtTGQCSLXWRqTM7ZIxEbpvKugEuFv0vhFWvBcdjoTR52TYGfSwOXXJdkvZwkACACxcod8mvCybq1LC5UevXkq8JcNbDci1SagFFLg4D2WBiSc9DdIzAyNabHNlUtFvXhAjdhQvkUCpmYa-cJptoGlmp7pfPcT-e1AfEqKUz1LEvHgNXBhsH3vQ-YdaENi5cYp9Km_iqMUms6XWoef3QhbvA32mFms7NqEtKyUnMwtHzJZ35TRsCh-7okgBN3hIZXRkX9dmxq8vnbPeHKkAwGSw7QV2DAeL33a8eKGh70wRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این رفتار ها در شان مردمی که چهارم جهان هستن نیست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84255" target="_blank">📅 23:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84254">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کاش شرکتی جز دلپذیر سس فرانسوی تولید نکنه، خر میشم میخرم بعد پشیمون میشم</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84254" target="_blank">📅 22:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84253">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4fUfzk-NFUwmE1Y-SdZ1-h3U3mDF7X9Fcvj2UusZSZ9HFvkmWTL-USUvS-4Vz33Ih-YJR1tFyhXhM2gCDQ5sVeg-iq7rgN1lQXnv5z90WorQecpA8QMN1Flg4wJ4eYsPXTFGygVBpwOsNCI7Jb734qp1Hg_2A9huwyBQnvXFSaZdXGzXtuH76X2cM3e7hbDjHfpfneFTOsrlqKItcu3On4Y7DWKBYabA475a5P3FDxEOrFfj2l-pyAJ37ZlBtS5dTGtWnuC6ZRObVGABR5RyHtI0NQVJI9tdVMwDmK-zKJYRLFXROksZRRfh6Q7_iZxtMQ3NH-VXdxR9CYFh-sEiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین موسوی مگه مجبورت کردن آخه؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84253" target="_blank">📅 22:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84252">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شاید همه اینا امتحانه خدا داره رونالدو رو میکنه</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84252" target="_blank">📅 22:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84251">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رونالدو رسما خودش اعلام کرد که کمپ تیم ملی پرتغالو ترک کرده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84251" target="_blank">📅 22:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84250">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رونالدو رسما خودش اعلام کرد که کمپ تیم ملی پرتغالو ترک کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84250" target="_blank">📅 22:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84249">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtgYi81dykvCWRpAe65ZyVy7lYq_DOhgqF1ESQHiRlsUbQ-fCKlbGdqKBoTxeRIHC7IFALKXCiVqVjSnu9ECATHilT_8GuCI-9tfbHhVYI1IzEHxFdRCAJg-msB-4QYC8hvmKVSbm79qrhU_cXLDQnf2AKeSCL52ewxF9OToLG7ooCq5VPNgbOKFZzocYgSCiYPPTAASPGqYJVyWmJac69m-c-w8NggJThQvA2b4Ga2AU2bMme3Hqxcm1P_9iE19hRbHZFDpurm-0qjHbJ0gfh21i7ETvIIvXVshDdW69UL8rbMqXZhOY73-EUEyiBC-6LZr6m-sMg6VsN0JbA5T9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣
🤣
🤣
🤣
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84249" target="_blank">📅 22:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84248">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KY1OflW6DgluCdL86tZpNB2cXbDFzrm7ZxQy4vl3WwLHlYvGgXtUbj8ZdXLti1XAUqV886X91bALxpy3C3vJAV_XuMaRHnKeiGGVSP2iBF9Cuvyp46KZgnLX1t8BYUd4WlimXz4BtfMDtfTOYypPEGpNRhj_ITCjhJwzw_qmKFntKxqGah-m5zzlId_C-cxPuct6o91uSz3SZ-DVu8TirOWdjhXRFkh4ctWRhf7YAcnzA5WVSvrysJ9fm-sO3vWwOuNPKia3WmGYcrsH9lwVXAFsHcp_4MHsIwcYs1uBSxH1tMDkb8h5xQ-yY5iKAEIEkeONveXHRrcGawS6sx2bIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعی که من پذیرش گرفتم با دلار اون موقع شد ۳۰۰ تومن که رفیقمم میخواست بیاد نیومد الان بخواد پذیرش بگیره باید ۲ میلیارد بده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84248" target="_blank">📅 21:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84247">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQ3bkjGtXIoVxcLNtp8dCZye7kwJElKA7PgMTsCcFy8C7n8lEqwEZz2Xzjq181ANiFHDedyHobbTMSBreQhmD5fK41wifE50uJaD6ytP-KuvSA8LZkfluhcjc-LvJXqRF8g7WkwRB-M65KVKCGCvojrwAps4fuVGRRtDp03aU71kkK9-TCNRzzTRFU_IeZNosEu-sN7GSmqOiDuRuwOp1Hd_ioHTdoWnJ1CbPW88C69YxSrBpvmsXmmvFm6jQR-sN7CqB2Faf4pMLCFVhGfgWmw-sBGDI52b0-86UZKpVaQcQYW8_mAhI7KxpC7orLQTJEtQBU0JpiM6GsQ6ZtH8XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار میخواد بشه 420000 حالا اپلای کن ببینم چاقال.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84247" target="_blank">📅 21:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84246">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚀
فروش کانفیگ پرسرعت | آی‌پی ثابت
⚡
سرعت بالا و پایدار
🌐
دارای آی‌پی ثابت
🔒
اتصال امن و مطمئن
📶
مناسب استفاده روزمره، سایت‌ها و اپلیکیشن‌ها
❌
بدون قطعی و نوسان
💰
حجم‌های متنوع از ۱۰ تا ۲۰۰ گیگ
📩
برای ثبت سفارش و دریافت اطلاعات بیشتر:
👉
@HolaAdmin
⚡
کیفیت…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84246" target="_blank">📅 21:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84244">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHola Vpn</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rw1XHuyutd3CX5_h890m_GUKmcgpBv66RqQaBINDTxbKy01rQcstvSKjehrSd_jiTaL5INfv1MNscFGNVc4m3td7rau1mlqS4BJ3CRZNLRV43jASvyg5bN4izYlk-hPqtH15Pyo5ZvfWr28dhjo5ssSqaH8ywk7mv5Yshn-Ipvic1oQtuqkmyieYH71iO_s6QHQMy5SIt69eMXBF6sQydcLXMbWO2nMGMJ2M5auHfWqU5y_jB-bWpEzUpyUyPw44ptVKmFHGj3dDFBuQew9suysaNrQfLePpxneBiv9oSZPKSvQ82cHLzXznl-9jf5arI08H1fAudxsKQEj3QjRB0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
فروش کانفیگ پرسرعت | آی‌پی ثابت
⚡
سرعت بالا و پایدار
🌐
دارای آی‌پی ثابت
🔒
اتصال امن و مطمئن
📶
مناسب استفاده روزمره، سایت‌ها و اپلیکیشن‌ها
❌
بدون قطعی و نوسان
💰
حجم‌های متنوع از ۱۰ تا ۲۰۰ گیگ
📩
برای ثبت سفارش و دریافت اطلاعات بیشتر:
👉
@HolaAdmin
⚡
کیفیت و سرعت رو با یک‌بار خرید تجربه کنید.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84244" target="_blank">📅 21:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84243">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رونالدو چون تو بازی قبلی بازیش ندادن قهر کرد و از کمپ تیم ملی پرتغال زد بیرون  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84243" target="_blank">📅 21:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84242">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رونالدو چون تو بازی قبلی بازیش ندادن قهر کرد و از کمپ تیم ملی پرتغال زد بیرون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84242" target="_blank">📅 21:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84241">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BArHAe1QKi-uzBzG0xqfB3SIbif7pkcOy6sA2GaUx-rqzjoz40C-LbKk3Rnyfx8SyEMNg_ZXpiLjwBZtJOyx0UdeHRtSq2vf5KroVLvJ30k4R3BIpNl5kS8CMyqGjJcyt7LtJh51Hu-AHbS3PEiWwJDKLsKUDgd5gjKoe40vsu5BeVYO770VU2Saqzn4rE6QIMOFemKsld3GlUxyNZ-SlAVhbgaA7JIaKU5jFbw_bMTxd5Ou1w0M1oS00TH1JhM7v-7uhhm6nbcG4KrJM28jtTlsaQ0KUv0YyJX-Ga6EoMLEsSq4luYFei3umSgPGsjlSJqQUGaxKnLQhFqkTj7LSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش تا حالا شده تو آینه نگاه کنی و از خودت خجالت بکشی؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84241" target="_blank">📅 20:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84240">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بادوم زمینی کیلو یتومن کجای دلم بزارم</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84240" target="_blank">📅 20:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84238">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FK2Ty8Qu5DdU92bA26_Qp8Cs8oSArXcwBjuvJsCnq6Ve9Ha4qTwP-cHzx334MKrhk8q1ss86RSvdIGqXtilIms-8ghOyiV11GQGPSVg1J1VPZqD4_GIde1sZ418BnPQRkhu_ooRXQPyiK4CWd46QADLLpE5I1Los3-a18SUglzMHOxzGU3nuj1wfMi5z01n2kIduguvzsW5u43jjaEELTGKz8K1s2G9thwGTkzZgkWMWQH2sAd5XonHDD2YYDzN-9_w6YTfoT94kyCCjySYNMs1SGkRV6buKJj_LWnLWqLjv-QJapxaOpFOCwCdi9ASp7lBdbscZF6So2-TLjckcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونم اتفاقی عادی تو خاورمیانه اس ولی خب تعداد بیشماری پهپاد جاسوسی تو آسمون تهران مشاهده شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84238" target="_blank">📅 19:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84236">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9XjZI2PRiSUf3colBjVORS7fESYy1QNvdR3w6S0XVxCYcdUgOhSNglLgVuFBmpNXkq0tXRD8uBySrvH2PqKd9T1JFw8MoaGN1xY_1XlvNhmuNwnCr3oR0IWJ_fSN4JbuzEBsRYYGvbWxNt2sCHDw-fsTjMVt7Lq7H2roPLzzyr1WMtlxw4gbG2m2L11AIymChahi_9ccL7HLNXVyAvLbfGH8NBQtYf5m7ia7RpGKHwegCRIJhXYevaHNR6fY-lEJp88_o8SQGnTOI42Uc3vDcjSYvalkFhGuwqeQJ33m5hgGTxtwf39rTJTeT5pI2xJCH4F5ohgTd3AgEXOA9PuJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی خیلی بیشعورید
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84236" target="_blank">📅 19:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84235">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نورا،دختری که کتونی پسرونه میفروشه
😁
چرا از من کتونی بخری؟
چون
👇
1⃣
تمام کتونی هام بالاترین کوالیتی و شبیه ترین کیفیت به اورجینال هست
2⃣
خرید اقساطی ۴ماهه دارم
3⃣
تعویض و مرجوع بدون قید و شرط دارم
4⃣
ارسال رایگان هم دارم
5⃣
به عنوان هدیه جوراب و استیکر پک برای هر سفارش میدم
6⃣
۲۰۰هزار تومان تخفیف برای اولین خرید میدم
@iransneak</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84235" target="_blank">📅 19:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84234">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1nRKasW9GGWejBgCzhS-nrfO9tcIXSG0wzV4tv_BkFY2C0vz7TWhiJgB150nntC0B_COCmMJZc6QOmDd4qeRU6Yc8LM3SFfVb72-79piIz7JcasRBkD7NJRqkYtJFXQEefmifV8IBtFzC31lqh1wEn5lbd0XDAjvkkdqSRtr9d2V3uUO6ewEDW7dt3up-OlYDk15KF5ZLPpcjHiJiBQ9swTCjSs9kJxABB68oBBH0JT4CoULVV_KnASB6gqsDrnN98FsEyWQOChWh1L3j9sDblg3m3NXDbTU9gZvbIVaMFNhWyDWXR4OR4DnMbasqbCo2z-Ho3MWhAyf97WAjuVlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدای همه دلقک بازیا واقعا دلم برا این بچه میسوزه، شده بازیچه دست چهارتا حرومزاده منفعت طلب.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84234" target="_blank">📅 18:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84233">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/142f9f8326.mp4?token=ldJlHToWqCmCFugnMoqItHHSLAIkIeLfDzz8E5W_uqS4UrtiH-4DNxGYKFTtsIvju61qBpb1wvBM_4wgc-6oOOXavmJcVDFKcbTeoTNnu3dfoqcOGw6LVp1y4Eiy9PVSoODFU_WCxQg5EidqFw8hx2t8nA3sq-mkV28ydN24FVsgfWaU8_R3SjjacsjaaXlifcQEOKXdXZf2-TfINe77mhjensVQPHd3nK_vo0QGZetPk6u4Jg5BLrL0wcA03bbRBln0G8RpLSUeQwL1EpgWgDZXQcPauq4M5-F2HpaJo1-f_SWQNQi4H5wH1K66IDzmYlPbw81BJI0aGJwtAe7-MCN2VAkGRbfWhTdq7AaziuRtnJnQUHyZxqO0AgCIkX2mIyVmzumFVkpOyXayW44_OQ6IG8AshRukhZCpZweT7OggEhBTTW6XoqphLMisFsHSgdHY3MzdJUMzlcfp_5_qylv6BEAgWYOIn4UZvYXTVxd9fRrtbUsNPTrOi-9BY5zBbj7G7zT3wtbRLrDmx1A24-Oxi_ZFcUQL5mDGiYW30rqeGXZNiKDUgPVPtlMom9HPAT1hYDrI4LLSzywXeWNUmKSCJkMELDBx7PDrJYVPKIDA1V5w0Ys0raz7SJKUY2we6OZrsNzvnY0FZuSRsJBr6FiX0_ZfHxB3e3_7UzGhHMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/142f9f8326.mp4?token=ldJlHToWqCmCFugnMoqItHHSLAIkIeLfDzz8E5W_uqS4UrtiH-4DNxGYKFTtsIvju61qBpb1wvBM_4wgc-6oOOXavmJcVDFKcbTeoTNnu3dfoqcOGw6LVp1y4Eiy9PVSoODFU_WCxQg5EidqFw8hx2t8nA3sq-mkV28ydN24FVsgfWaU8_R3SjjacsjaaXlifcQEOKXdXZf2-TfINe77mhjensVQPHd3nK_vo0QGZetPk6u4Jg5BLrL0wcA03bbRBln0G8RpLSUeQwL1EpgWgDZXQcPauq4M5-F2HpaJo1-f_SWQNQi4H5wH1K66IDzmYlPbw81BJI0aGJwtAe7-MCN2VAkGRbfWhTdq7AaziuRtnJnQUHyZxqO0AgCIkX2mIyVmzumFVkpOyXayW44_OQ6IG8AshRukhZCpZweT7OggEhBTTW6XoqphLMisFsHSgdHY3MzdJUMzlcfp_5_qylv6BEAgWYOIn4UZvYXTVxd9fRrtbUsNPTrOi-9BY5zBbj7G7zT3wtbRLrDmx1A24-Oxi_ZFcUQL5mDGiYW30rqeGXZNiKDUgPVPtlMom9HPAT1hYDrI4LLSzywXeWNUmKSCJkMELDBx7PDrJYVPKIDA1V5w0Ys0raz7SJKUY2we6OZrsNzvnY0FZuSRsJBr6FiX0_ZfHxB3e3_7UzGhHMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جانی دپ
❌
محمود احمدی‌نژاد
✅
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84233" target="_blank">📅 18:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84232">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84232" target="_blank">📅 18:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84231">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncgXCVmcPq3XepK7PgkXb7k2_7OBcMpXuduV4vxHqtoRaqNWdWg3HNx6qWQPf4_b_lGLmZTefQ6SwO7jvKlGK9ePtEtucR3lkqN0KaKFw4ER3ZaJ2UI4ohD2u4n1LFMJcogdViP89iNG6782DAfYnl1rbl4AcxhCGlPweMuFXizNWjuIw7yRrj5NFaQ1Jt1fIqsqVu6v7roMaUb3Rz5Ki0pjQbcsVKKN7NC6fzbfNzo5HEZ8hxmHAKlvEbepOe4zQkbxBnbzcDAQrouALNQD7E7CMuxfZoEClDN1bkEECaLO_SxZdABR8LGie81KXqkf2L79PnKEQ5uHAMynVmtTuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👏
یک بار شارژ کن ، دوبار شارژشو‌ این طرح اختصاصی ریتزوبت برای کاربرای فارسی زبان خودش رو از دست نده
🔵
اولین پلتفرم جهانی و اسپانسر لیگ هلند محیط امن و حرفه ای برای عاشقان شرط بندی فوتبال
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
g8
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84231" target="_blank">📅 18:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84229">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">میگن میرحسین موسوی مرد.
@Funhiphop
| Mehrdad</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84229" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84228">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بابا حداقل یه خبر از رشید مظاهری بدید بدونیم زندس این بدبخت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84228" target="_blank">📅 17:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84227">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8jG_5Cj8ysxW4l0fCVOJ8-ChG85OYGrugo2XLtkKL4faw_JfdKBjDsERlvilmVh4SOsj7z6vhBv8uDZpwDJqMnMts1OFRZUMh1xtBdnFEO6hXW8X8Cz1nYApEo7pOERyfrHw-6fCYeLckjMUB4_9Q9rYoWqLvKgvbvwX55f_wesONrWooBh9RXbm4yjApbrqt13jsVlnrNbpL9aiEBnN__N1TwheCTIxOf0Hy-TvHO48V6hpFL1Kn5et0JFIzDC_ZukDtPwb-Fs_BDTxK1QLaA4XT3uuZcFbqWiblQQ5kzoCJL8t3Se2CXwBthGC_pKIOGfB8_l-AvCxe6HOYl-ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبریک به پسر بچه های عشق گوز
برای سریال ترکی "اشرف رویا" یه اسپین اف ساختن که اتفاقات قبل از سریال اصلی رو نشون میده و بزودی منتشر میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84227" target="_blank">📅 17:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84226">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">زن بیژن مرتضوی: بیژن برگشت ایران تو این شرایط سخت جنگی کنار مردمش باشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84226" target="_blank">📅 17:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84225">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvDFJcqzIbTO7WS-OjyTCkCqAvvSqHJWpUmfSZI4Qk7usSvJ0BRjLW7pZLigr5hD4PQuyXx9KutPIf8skrcswT4SgkxSKR--OCrifS1WwOr-QwRSe_xvnLtRkLEN8bIJN1TgSohiKdA6H-4CkyMFKNSQtRDr2N3t7OwKLhN3pNQdZ2xfACVJEop8OuYlRND2RrIBjWqhJhU1YZlaviYkUZBL7lOhmsGsseOAHFefCMrzTNK_oyrAclS16nK9yYDLEGP8DJpVdX5qfnDSI9w_s0zh1O51Yevo1a7SaZ6ofgpigIwwFYF7dtykaG2blowA-rWA3uDtdLkNr25_1ABHOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84225" target="_blank">📅 17:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84224">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بیژن مرتضوی که چند روز پیش می‌گفت میخوان منو بدنام کنن و برام شایعه درست کردن که ایرانم و با شرایط فعلی ایران نمیام امروز برای اثبات حرفش اومد فرودگاه امام و لایو گرفت.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84224" target="_blank">📅 16:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84223">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بیژن مرتضوی که چند روز پیش می‌گفت میخوان منو بدنام کنن و برام شایعه درست کردن که ایرانم و با شرایط فعلی ایران نمیام امروز برای اثبات حرفش اومد فرودگاه امام و لایو گرفت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84223" target="_blank">📅 16:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84222">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آتش‌نشانا دیگه شغل دومشون آتش نشانیه، شغل اولشون بلاگریه
از در و دیوار داره بلاگر آتش‌نشان می‌ریزه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84222" target="_blank">📅 14:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84221">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یک فروند هواپیمای مسافربری که از دبی به مقصد تلاویو درحال پرواز بود. اول از مسیر تل آویو دور شد بعد از کد اضطراری ۷۵۰۰ که نشون دهنده دزدیده شدن هواپیما هست استفاده کرد  @Funhiphop  | Mehrdad</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84221" target="_blank">📅 13:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84218">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2003caf7.mp4?token=fOQde5F_8N7C8xCiJHf8A3WVYzhq3lC9-e-B8-far4BjnGFLK5cjWhMTWU2DD6V-XhDGQmWrPbfHzMC0z3L4LiVuA6lORDoF1OYhwsP0GTxhekMwl5wnGPjxjdSzhfJgkOAfX58KWKr7ArCxd5TI5q-AnIQKa8hyFuLUZ97_kinsd3i__mqLA-iscxEojmBuG0isdEzsBO0F5CzLBjGw5dpeRqYqW4Qhg8qL4UK8VurJGaPFKaXwpXEtFDohk91IZwDYUhSWmV9TXVvJECyr--YE4krBiNF38cDk_lpYoDFZe0NWmAicH5JK4f7Ed0Dp78a4wg_1ZrSpmi1faLACOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2003caf7.mp4?token=fOQde5F_8N7C8xCiJHf8A3WVYzhq3lC9-e-B8-far4BjnGFLK5cjWhMTWU2DD6V-XhDGQmWrPbfHzMC0z3L4LiVuA6lORDoF1OYhwsP0GTxhekMwl5wnGPjxjdSzhfJgkOAfX58KWKr7ArCxd5TI5q-AnIQKa8hyFuLUZ97_kinsd3i__mqLA-iscxEojmBuG0isdEzsBO0F5CzLBjGw5dpeRqYqW4Qhg8qL4UK8VurJGaPFKaXwpXEtFDohk91IZwDYUhSWmV9TXVvJECyr--YE4krBiNF38cDk_lpYoDFZe0NWmAicH5JK4f7Ed0Dp78a4wg_1ZrSpmi1faLACOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میخوام برم استانبول کنسرت.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84218" target="_blank">📅 11:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84217">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1244f53d60.mp4?token=SfxBTM7LhMUVBuMdZXHhQ8H1QFAP65R0kNvmEsctPOisa4VbM6UCA03yoq-9C7D0GsYsM6i1ooLgBGeUD_0hkhilPE6KQA2sEP9POZbAVtFlkNBJSuUcvLkqJnPoHrQ9dbo7s2bG5T56sZF17R7K9ezsCM4Bj-oo1Au2rLkpiKcHdWZRqdPDegKyQwrirYDX5V30Q190dtSMecYz24uZqzM8U1YqGDeRttmM6mTn1Sk9AkJADc6hfENd9gqXOp9NQpI-Rke1NjxLKSQ5Z5me-cRAwpVTBKi6MuVj6rda4PBfiGKDpF5b8SXNgGs024W6luSbOfwMKwRR9hASY8SvJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1244f53d60.mp4?token=SfxBTM7LhMUVBuMdZXHhQ8H1QFAP65R0kNvmEsctPOisa4VbM6UCA03yoq-9C7D0GsYsM6i1ooLgBGeUD_0hkhilPE6KQA2sEP9POZbAVtFlkNBJSuUcvLkqJnPoHrQ9dbo7s2bG5T56sZF17R7K9ezsCM4Bj-oo1Au2rLkpiKcHdWZRqdPDegKyQwrirYDX5V30Q190dtSMecYz24uZqzM8U1YqGDeRttmM6mTn1Sk9AkJADc6hfENd9gqXOp9NQpI-Rke1NjxLKSQ5Z5me-cRAwpVTBKi6MuVj6rda4PBfiGKDpF5b8SXNgGs024W6luSbOfwMKwRR9hASY8SvJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پسره برای اینکه علاقشو به دوس دخترش ثابت کنه، رو گردنش تتو زده و نوشته: من سگ دوست دخترمم.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84217" target="_blank">📅 10:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84216">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84216" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84216" target="_blank">📅 10:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84215">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRbJKf48XCeHSClYru6JgvI2UuOk5-tFm0qg6Epi0Zmte03piHOn-3L5XqrIRpOjsHjJ82dnGWMjx-YsdsC-LVY-Cr3SIcGJb4sUZTpREpnvIOdUZ6AE45Qv3riNQIQZuqmxKSo0Wj6CJU-CvomRdgHJKnhofnjl7se1IJeFZ_qEnfyQKRntThwOTjhqzwlnumOsAPJ8ca9X05ulcoA32lKl4i3qGp9YyP4LTTLSKpPzsZyztvlcImsOM-nUiEkJ8Ox8ijHpRB1tbl65vM8e3JNHRF8hcaf8sTfFTb64BQfJfdJS69eAGrFcdIbc8Mf2dkrs8PVahGHka7JAyFDZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👏
یک بار شارژ کن ، دوبار شارژشو‌ این طرح اختصاصی ریتزوبت برای کاربرای فارسی زبان خودش رو از دست نده
🔵
اولین پلتفرم جهانی و اسپانسر لیگ هلند محیط امن و حرفه ای برای عاشقان شرط بندی فوتبال
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
r8
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84215" target="_blank">📅 10:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84214">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یک فروند هواپیمای مسافربری که از دبی به مقصد تلاویو درحال پرواز بود. اول از مسیر تل آویو دور شد بعد از کد اضطراری ۷۵۰۰ که نشون دهنده دزدیده شدن هواپیما هست استفاده کرد  @Funhiphop  | Mehrdad</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84214" target="_blank">📅 10:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84213">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یک فروند هواپیمای مسافربری که از دبی به مقصد تلاویو درحال پرواز بود. اول از مسیر تل آویو دور شد بعد از کد اضطراری ۷۵۰۰ که نشون دهنده دزدیده شدن هواپیما هست استفاده کرد
@Funhiphop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84213" target="_blank">📅 10:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84211">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZ1dD7blyIJiFvMGuZWJd1T4Oq4vUltKY_jI3irf6RdiupNsu4KYnj6UIOvqShvg17Ib6EroTHvNoV9pAAAu6hwG3tBQor402VWui3J6JG7mfqb6pyF32z58-sQQw8u4jIvSrJwu8ctHR06EKM8GppsG-UUq9V0wb71JwQqZa1Sci859XI6vX2Zg_aJpgN3iiHB6xFz6CikcQw5_yB4bxVxTZVu2mw3KalH_ZsgVw7zAScrlF3y7cVD8XgVeXNiT0QJM5QyFqCfisW48YJOpj9o8GIDPd1-R77XqKR4ACZgYRG8brIL2S9y0-7Hez15d1W5CdnXpEQ5I8ZGRfKhAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dacdc1485a.mp4?token=SqaTRTNOig1wd_W4qsyyVo-2PhjtFMa-VzY2UA4xuAw-b3buAy6hGPNO4lxaZ-3-EC5U-hHcbDvwIC6oHI2zqzt_3MBBWH8kdhjW1PwCktOTxBTpLQSE7FUwIWqRZCXF5cEd7wqBWzoyrnuOWj1A4kg6ArdBouJYCUBUtdZY2JVaQidN-vnLiy9OtHaLiddAurMUrM4hb5SmdKLVvzSpqtCrRdvdtm3IGcDlbj00h8ht4rsr2fLN3H1itIQnsX-HVTsiRhPFCSa3ps4mC8ATuncm8msGytV5uSYk0qxXunKscgeGsf8BbiXZJLEPG1rhgHXSf2xho96iXoXsvGLNsmNtt15NUqsjd0YNSocCHmqlHe6bX-EwA6zTVJS2wzzbMKU0nk-zQ9f0pBfcE9MZ_ir9E6IAcJJNuFO5fNqP8ZH7UZtSXWucQ7uaanmKkztKpto8UyBhdR4BGxdxtxFZMNtYdaPSWBH2_FnXnbPC0V71EgtRtq20DTm1ESpeqxNhhNYx8DcEYDiOW-qPGAglFIpcZ90c3h2ZpSiOp1UV6GeU-77t-QKp7vEJVjWY5k6XVSVBiWdad1unduNxHNaWxaa0r2zPk_LwWXZt5uvW_tgsoTVsEOakgXahmYlL4DjkXQA6yAViCmXpB3trV19hWXq7Lx3vindgHeg1k-DJSXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dacdc1485a.mp4?token=SqaTRTNOig1wd_W4qsyyVo-2PhjtFMa-VzY2UA4xuAw-b3buAy6hGPNO4lxaZ-3-EC5U-hHcbDvwIC6oHI2zqzt_3MBBWH8kdhjW1PwCktOTxBTpLQSE7FUwIWqRZCXF5cEd7wqBWzoyrnuOWj1A4kg6ArdBouJYCUBUtdZY2JVaQidN-vnLiy9OtHaLiddAurMUrM4hb5SmdKLVvzSpqtCrRdvdtm3IGcDlbj00h8ht4rsr2fLN3H1itIQnsX-HVTsiRhPFCSa3ps4mC8ATuncm8msGytV5uSYk0qxXunKscgeGsf8BbiXZJLEPG1rhgHXSf2xho96iXoXsvGLNsmNtt15NUqsjd0YNSocCHmqlHe6bX-EwA6zTVJS2wzzbMKU0nk-zQ9f0pBfcE9MZ_ir9E6IAcJJNuFO5fNqP8ZH7UZtSXWucQ7uaanmKkztKpto8UyBhdR4BGxdxtxFZMNtYdaPSWBH2_FnXnbPC0V71EgtRtq20DTm1ESpeqxNhhNYx8DcEYDiOW-qPGAglFIpcZ90c3h2ZpSiOp1UV6GeU-77t-QKp7vEJVjWY5k6XVSVBiWdad1unduNxHNaWxaa0r2zPk_LwWXZt5uvW_tgsoTVsEOakgXahmYlL4DjkXQA6yAViCmXpB3trV19hWXq7Lx3vindgHeg1k-DJSXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی اومده یه سکانس از برنامه فان ۳۶۰ که ژوله اجرا میکنه گذاشته و گفته خیلی خفنه و اینا کاش قیاسی و ابوطالب اینا جای جلف بازی ازش یاد بگیرن و همچین شوخیایی بکنن
حالا قیاسی اومده کامنت گذاشته کصخل چی میگی این شوخی رو خود من نوشتم برا ژوله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84211" target="_blank">📅 10:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84210">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64cf794cfa.mp4?token=aJ7SZGC2sWBv4qQLv_xgBFPyKCRzsfrqkBeWjjArvQmIAbkWpzXi4CIZEgQ915kHq5t27O1oWKG5eNCXvPAyiJxy9kdah0y135HoRJl6_wICg-6Ng96ZQuNr9WC0bl4WJ4uroWtj2XkFUD14AHucmwdn4BqYsqaGr6ogZWAB48etQlv5_pIbEPFdkYBcEUklYxP7w2Zhw3fvYwTbQ6aeZUQypcAmYFgIhtMNyQESnVsfSmKEJCutiEF9xkw1_YyDpvBzViSEcMDctsDNH5wUBL9UFo3WSpl7ay3FrsUhxEJbzWA-FnQ7i7P-nBmf-cXSrgvoJ5NJ4iDUunPt_4htgA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64cf794cfa.mp4?token=aJ7SZGC2sWBv4qQLv_xgBFPyKCRzsfrqkBeWjjArvQmIAbkWpzXi4CIZEgQ915kHq5t27O1oWKG5eNCXvPAyiJxy9kdah0y135HoRJl6_wICg-6Ng96ZQuNr9WC0bl4WJ4uroWtj2XkFUD14AHucmwdn4BqYsqaGr6ogZWAB48etQlv5_pIbEPFdkYBcEUklYxP7w2Zhw3fvYwTbQ6aeZUQypcAmYFgIhtMNyQESnVsfSmKEJCutiEF9xkw1_YyDpvBzViSEcMDctsDNH5wUBL9UFo3WSpl7ay3FrsUhxEJbzWA-FnQ7i7P-nBmf-cXSrgvoJ5NJ4iDUunPt_4htgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بلاگر ایرانی تو خارج که اتفاقا فن کوروش وانتونز هم بوده، می‌ره یه ویدیو می‌سازه که توش نظر خارجی‌ها رو درمورد ظاهر سلبریتی‌های ایرانی می‌پرسه و عکس پارتنر کوروش وانتونز هم اون لابه‌لا بوده که کوروش برمی‌گرده به این بلاگره فحاشی خیلی سنگینی می‌کنه.
بلاگره هم برمی‌گرده می‌گه زنت ۹۰۰ کا فالوور داره هر روز از خودش عکس می‌ذاره بعد حالا من عکسشو به چهار نفر نشون دادم اینجوری فحاشی می‌کنی؟
به نظرتون بلاگره مقصره یا کوروش زیاده‌روی کرده؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84210" target="_blank">📅 03:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84209">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBaIu8ChcxJHuqFZQ0AFczmaTrtv1b49s2ED2yRrTjlza6YQKc3r9RqWTGkoD6bAKmGm9efyMH9gQX50CeVAsAOqczqF1zOdGT_bDFVAl_vS1naVdjZwnJpx-IEzamhQJp-pTWU8qJEmtBg1gIbDNxoTNCfHhQWSwWAAjH9CSPsGTtGSKa4SRfvdlhrmpeQR_EkmCfFUyj6oD_hJt3U4DinJhsya43FW6KeBHpKpwBHr_OH0ufCgNEKW-SYLugAwHm38-Q-xRDbLNIP8qocj4eaONCtze20n0za78iq2MR4uRYaeE-jQOYj90kKEfmvNAInmoKihUttxBHhc0hihfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواب از کلم پرید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84209" target="_blank">📅 00:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84208">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHQCn8qwvg6t-4J21E40vihzaBGD1GyiMDeMCJ7VPpvbI0fe9xVziXzGUL5BiXwHhVTPXvW8HB23GJX7_rS0ENJUhwpny7PhOJ4DCyMg_HdvJuKfS_6LdZvG0TuvZ0E-Q6NAZ7z_BVUJWggNckZ3QzxCVCuh9NDiDEKdF9JeKprCDkRa6XN8fv6q8XvoiCCY0gu5_A1MUEK31XHr2t3kSCoGangsKriDMKEue7p8YtMzSPDQj7yC_IfhEJxUJ10Ho1zIKcW0izaQvFOo_rkpRCGAADfit4fF8dXy7T9esdQjdmVznjvFQCfbAGrppQ6TNbyxTJyEZ_8bJ3dWuHooow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بیانیه میلی‌گلد: بعد از پیگیری‌های میلی دستور آزادسازی طلاهای میلی از بانک کارگشایی صادر شد
خدمت تسویه و تحویل که به علت مسدودی دارایی‌های میلی در بانک کارگشایی مختل شده بود، فردا عصر پس از دریافت طلا از بانک کارگشایی به روال طبیعی بازخواهد گشت.
همچنین طبق دستور دادستان، محدودیت‌های اعمال شده بر درگاه میلی رفع خواهد شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84208" target="_blank">📅 00:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84207">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رسام سهرابی جان مادرت وقتایی که جیحونی پنجره کیریو ببند بعد داد و بیداد کن سری بعد زنگ میزنم 110 میگم پرونده هم داری
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84207" target="_blank">📅 00:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84205">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">به وقت سم های عشق ابدی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84205" target="_blank">📅 23:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84204">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فرمین لوپز تو کیر شانسی میتونه با ما ایرانیا رقابت پایاپایی داشته باشه واقعا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84204" target="_blank">📅 23:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84203">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پشمام از یامال</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84203" target="_blank">📅 22:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84202">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geggxkrFv1VeEywq3zNqiJwxg1Syhjs9DtJNMd8-m56UUzJYgiFOzm8zTZegZtzY9foU1oZiMoPng13u1uAhmLHeu9h7oIShR2YRJNfoUnddb9MLnxyB_sHltBdSbulyZVZdnDTvqH2kd05u95rHBQEcPALd6UZmRecOHPDYGedv_xYGizvvVjzER4JaajA4n4yy0lFStaUfckSW6wyW-m_s5ZeH9fku9nHHaG10lFXBwxLnJds1hj1B3jBDP9vItsaJ1HatYrIkaSKkqRSFw-8SpnfUPUxwMHD4OIxtQCvV4afNG9Zz348PLWyHCY8A8erapU3JAM46KWujbUA5-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز همزمان با پلمپ شدن مغازه های ربکا عکس دوس پسر جدیدشم لیک شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84202" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84198">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یاسر بختیاری در یک لایو ۴ نفره اعلام کرد فیت سه نفره او با رضا پیشرو و tech 9 قطعا در کمتر از ۱۲ سال آینده منتشر خواهد شد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84198" target="_blank">📅 20:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84196">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بر جرعت میتونم بگم رضا پیشرو درحال حاضر رپر هایپ تریه تا تک ناین
و رضا پیشرو انقد هایپه سه روز آلبوم داده و بعنوان یه ادمین رسانه رپی هنوز گوشش نکردم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84196" target="_blank">📅 20:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84195">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یاسر بختیاری در یک لایو ۴ نفره اعلام کرد فیت سه نفره او با رضا پیشرو و tech 9 قطعا در کمتر از ۱۲ سال آینده منتشر خواهد شد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84195" target="_blank">📅 20:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84193">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iz25pjZujt7LJOQ6Ue7_mWR0mRVyuso0g4tB_6maBvi-3lzvvNCRyv6r1NxDSzjK_hUYBwenYnEMeUggwRL-6NJktEdBuN60NPxo6yargitTF4RS_v8vEkvLxAgiOWu5hInv_hVi6cM0hK0ESGMlNtnolkAzTY41DB0sm8OVJj4rpxCTQcqdp0KBam_hZ9QMGODM_iIPEfkOzYy82X2KiDp0IwXcRVjviVD0H0tFDztZRUTRC6VJXCdvQxYyFPCaYsnGiYF-ilyKrlymevl71u-8FpEIVca-TI_zU9T_NGroZ1tVEfUFhMz_yKgq-3vjwJ3_hehqlIvNPkeN8v2oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا باید صبح بیدار شیم از شیک زدن زنمون فیلم بگیریم بزاریم توییتر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84193" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84190">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سیتی محکوم شد و بزودی حکمش میاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84190" target="_blank">📅 19:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84189">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtFcfD4nWEH5zFSJzasLCtrAaYP0mu5Rp9uXBm_aLLiELnKM7FW6-nuUl8GRVNCs0aDGJNkUWfHlM3QXGjOcUWUTXhMZsTkj9LoIVU4rsDgnv3RpJvddZhzQYJX55glHpkmtcP9Yvqonise4_Ap_UeowHdDSQaxsNhB7f7VIVHLBD-RG8_c72l4QS4T0abNRDzgWv9afo4k3XqQ-DSe8Klahg-p3V1_v54DuTh6qM-nyPouZNNC2LH5kXYnf6cRadSCMMkn9uy7jIO94Km6TQZbkjwq9j9VEuZuSovJLKbc2JxAaE8k5M0O2_qMpYpafxzV9_b9OsQpLUCeiC1vbPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید آرون و کاگان به نام "انکار" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84189" target="_blank">📅 18:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84188">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترک جدید بهزاد لیتو و بیگ شگی به نام "1.6" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84188" target="_blank">📅 18:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84187">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeOVTkvxM2nVfbbozSbn25Z8XCuUPTRGyvxi1Fl8KI6tA6VeyrFiXrJsDuraRaKjsUHB7wmQVELSUdQiAsDq0kiq-HNMs89vQosUPPu3XuF0qbsK9qOF59RvbJpf-mdb9b7t4f4peDcQFP8orng4CV1vCewLR4_csgYTUF0ZKaJXx7Z38HuZnhb31hprjCIDh8zGHPABTm5qNQ3iQIBpfrFbjqpICYlz-asb4J9FYlc8ljt2bi_LoP-x3ndX2h68cXKYpjd6gVimj9EMojG4aFf6huxj0hPOz67MPCkirLEb6rqN1YenhYsvbS81C7oBHsnLHmvfJSj6SSjCKvUaUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید بهزاد لیتو و بیگ شگی به نام "1.6" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84187" target="_blank">📅 18:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84186">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uv_0Cld3vKDn3Sio4Xeyw3RkwskwpNzgNPQ0kVoWPUMm_4o6XQNmQ_07uAXFACIttsuXCVEvggj4QlbGcnggAV-lJb_Nt9ZZvM4UObzuspR6Sr4hSk_T9QO8auw3I2fDzIflyS73VQF-MEdk3tMVX5lIYy3gM_CU2HsauO4XxTAxIbSzn7LNC1uYhFrwTDkwUrGLp8lTltjwZpz37pMf8Z7H-ILVt2StYlLnz3cw1WxGm9x2yRSo3XojI5boD65hKK-ZXHP7ZhowTGWZhSZOodKXkfGFKB6y7CwcrU5hRhafjYWiCpHZ-lKCXZqX58z_SFQShmEG1tXXyViMW-HOUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاره شدم این چرا اینجوریهههه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84186" target="_blank">📅 18:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84185">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862ec698b.mp4?token=GX61koqIDD4irOuD-uKJ7S8aDQXbdflp8BarGMW5c97D868XpTJR_KHhixc5QjllbAGZzdNFpeatg4ooJOntSd6Hzd72gXJ3Bq4L0lLJAav8HaN32oux6Nbt-YtX5dJwVGSABloAutfQjV8CqGPauy8yx2fA50wZgI7pjN5sNDGmFWDdB4biJcSckP-66YyCJJAQPztvHkaH5GpCwh08yZQN7M5_KQHofJDoiKKUej84NEu71j0CCQS_q2uR7a0lG_M0q6oMZCLWTmmougcIm-Bz2MFU_FScoAmkT7ThfTbh_NcLRk8pXQkazlpJmVi2kOKRRoTP5DbpPt-FTi8RTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862ec698b.mp4?token=GX61koqIDD4irOuD-uKJ7S8aDQXbdflp8BarGMW5c97D868XpTJR_KHhixc5QjllbAGZzdNFpeatg4ooJOntSd6Hzd72gXJ3Bq4L0lLJAav8HaN32oux6Nbt-YtX5dJwVGSABloAutfQjV8CqGPauy8yx2fA50wZgI7pjN5sNDGmFWDdB4biJcSckP-66YyCJJAQPztvHkaH5GpCwh08yZQN7M5_KQHofJDoiKKUej84NEu71j0CCQS_q2uR7a0lG_M0q6oMZCLWTmmougcIm-Bz2MFU_FScoAmkT7ThfTbh_NcLRk8pXQkazlpJmVi2kOKRRoTP5DbpPt-FTi8RTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هادی چوپان: یه ساله دارم کابوس میبینم؛ باورم نمیشه دیگه محبوبیت قبلو ندارم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84185" target="_blank">📅 18:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84182">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ادم اخه طلا رو مجازی میخره</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84182" target="_blank">📅 17:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84181">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">معلوم نیست کی خورده ولی نزدیک ۲۰۰ میلیون دلار اموال مردم تو میلی گلد بگا رفته و هیشکی پاسخگو نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84181" target="_blank">📅 17:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84179">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf73bf24d.mp4?token=pzGsU4bxNiaQGfFk10ZiucIEOeIhP00XlLHZOlOJ02FcYQC6HBdNgW_k-GvGfzzZQjW6ZZm8kWmBXYk-8Z3Ri472pVzAKLD_IS77pZOQ_GRz-mvZMBwDoydU5PVU53JuTUGDyx-8zgsm6diKE48Y_QXh0MJkvC2_pLN3ONUwU6VdEEu2ZPkxFNH9udc0YgvXPtZCu2GSCnfrGRJr9HXsiRr8CuhXexCeWGIDAyh5IIvLhVM_p72SvZZeIbf0_Ga6gTt8V_S3N7iyKqBQy4rs1xZYVhBlHHkVLdxW8lf54OX0NGnq4BakZ_REjcyZvU5liHMZTYnHWhUHbg-dMm3G0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf73bf24d.mp4?token=pzGsU4bxNiaQGfFk10ZiucIEOeIhP00XlLHZOlOJ02FcYQC6HBdNgW_k-GvGfzzZQjW6ZZm8kWmBXYk-8Z3Ri472pVzAKLD_IS77pZOQ_GRz-mvZMBwDoydU5PVU53JuTUGDyx-8zgsm6diKE48Y_QXh0MJkvC2_pLN3ONUwU6VdEEu2ZPkxFNH9udc0YgvXPtZCu2GSCnfrGRJr9HXsiRr8CuhXexCeWGIDAyh5IIvLhVM_p72SvZZeIbf0_Ga6gTt8V_S3N7iyKqBQy4rs1xZYVhBlHHkVLdxW8lf54OX0NGnq4BakZ_REjcyZvU5liHMZTYnHWhUHbg-dMm3G0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خارکسه حداقل بدون لهجه فارسی حرف بزن بعد بحث وطن و وطن پرستی بکن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84179" target="_blank">📅 16:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84178">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یه زمانی خارجی ها مسخرمون  میکردن بخاطر کالا برگ ۷ دلاری الان چطوری بگیم  شده ۱.۱۷ دلار
سخنگوی دولت: خبر خوش دارم اونم اینه که الحمدالله بحث کالابرگ حل شد و از نیمه دوم مهر کالابرگ رقمش میره بالاتر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84178" target="_blank">📅 16:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84177">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">در همین حینی که قالیباف گفته اگه ما نفت نفروشیم هیچ کشوری نمیتونه بفروشه تو ۴۸ ساعت گذشته ۲۲ میلیون بشکه نفت از تنگه هرمز خارج شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84177" target="_blank">📅 16:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84176">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKudwMFOPCgo-_zwG4CwBwlCOwyTyL0MquthX4nf4PM75zWiS8BMYzq5ChklQY5FpPdp8K9t5UuOGjsN09FeOCcj4itZBJkRb5RIDgmtt4CIziqs5xv7QF5PYgvynwwdixiFFPeDmwtUhxiaA4CfaNvXp4sDoWi-FDYmtDuydgb6ruMGzp7uryBKal1eRpC1BB8tiVdlC2u9kjdyhCR3JGvuFvr5rgYYMNafLmZYzoniC5SrqCiE8pyCLRrBJ_PYh2vUZlQaOojoIGp6mtsI2NNhN7alSLW7t9M3tNrQhlOyiU6xKBOpNKfXVqNv7kM6xxz_aAMrQr1dt0WtdI1eyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار دیگ ترکراری شده لیر رفته بالا ۵ هزار تومن انشالا تا اخر ماه دیگ ۱۰ هزارتایی شدنش رو جشن میگیریم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84176" target="_blank">📅 15:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84175">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تو این دوسال آنچلوتی که سرمربی تیم ملی برزیله بیشتر از سرمربی های رئال به رئال خدمت کرده با مصدوم کردن رافینیا   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84175" target="_blank">📅 15:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84174">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آمریکا بعد از تحریم کل خطوط هواپیمایی ایران، الان فقط یه مجوز یک ماهه برا پروازای ایران و عراق با کلی شرط صادر کرده که توش فقط می‌تونه مسافر زیر نظارت کامل آمریکا بره نجف برا زیارت و باید از همون نجف هم برگرده ایران.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84174" target="_blank">📅 14:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84173">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">به کسی که حمایت نمیکنه ازتون فحش میدید به کسیم که حمایت میکنه ازتون و بگا میره میخندید
واقعا آدمای کصخلی هستید</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84173" target="_blank">📅 13:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84172">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هردو فروشگاه لوازم آرایشی بهداشتی ربکا قادری داخل ایران پلمپ شد و تمام اموالش داخل ایران مصادره شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84172" target="_blank">📅 13:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84171">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOoR6SSgr68qX81LyUVFGbyIzAMeAAgaYBz3mvZtchd82A0VB2mnZ4OULMoJLM6wmhIbMpz76Q_2UT0L-q8rT7lTgV1kceYcpBCVW4QfBYUd_qp6Cerbw_moYMpaqDBxtqGY7gDk3VtImXydjknmwMpbANyoTz48BrHYux5aMhhoSKg_Ak_OdWiBcdmzw44ZwbZ523N9ZbC5oGCV1mjlJ0xjHCbfjeQkFa3Ml3_9s2x2pHCtPQ8XyljdSLbPfiNq0BUypSMrNNrYJ01KkgdeVn84BIYCIeqAPiXnfTnC1VeHTEEpDIG_YElUUqGh5crF0eFVtppKD_8ikhiTrOeANg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هردو فروشگاه لوازم آرایشی بهداشتی ربکا قادری داخل ایران پلمپ شد و تمام اموالش داخل ایران مصادره شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84171" target="_blank">📅 13:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84170">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
مردم آمریکا تحمل کنید کمک در راه است
سپاه یه نامه زده خطاب به مردم آمریکا: حساب خودتان را از اشغالگران فلسطین که خواه ناخواه باید آنجا را ترک کنند و به کشورهایشان برگردند، جدا کنید، ما می‌توانیم همزیستی مسالمت‌آمیزی با هم داشته باشیم.
دولت یاغی، کودک‌کش، شهوتران و بی‌خرد را کنار بگذارید، امور خود را به‌جای اراذل به اندیشمندان بسپارید و به آنها یادآوری کنید که دنیا عوض شده است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84170" target="_blank">📅 13:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84169">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7e6ffd31df.mp4?token=AbHXYu2Zt97qAT2GK_rrhep4JXsmF9trp5wXts7fvPn7wfYfHPMy-4xhiQ4GI5RLtVeqM4LNG9aZSbQNRezZoGd3vEvnKUH2Zo41Md3uLVj-1dfDSfjVjgjOVZ6dxrwfT8nQgoOgRyM0fzaMA_1HydszAcFF-JoV22fqCtetexP8BX8q_VvhsdbNhsGvhsf6hqAncLV6aFtk3JaneLFvECjtq-JE2AyQXcRW5_uW8so11rMEYt-aRCweKFp6ypZ6NrbuFDaSgOw6arWefZusqSSLYUbgfqroXQYEa7nn8sO91pJC6dAJJviEgJufnv_qVL7ZjULd38ztYYDyWdxgPg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7e6ffd31df.mp4?token=AbHXYu2Zt97qAT2GK_rrhep4JXsmF9trp5wXts7fvPn7wfYfHPMy-4xhiQ4GI5RLtVeqM4LNG9aZSbQNRezZoGd3vEvnKUH2Zo41Md3uLVj-1dfDSfjVjgjOVZ6dxrwfT8nQgoOgRyM0fzaMA_1HydszAcFF-JoV22fqCtetexP8BX8q_VvhsdbNhsGvhsf6hqAncLV6aFtk3JaneLFvECjtq-JE2AyQXcRW5_uW8so11rMEYt-aRCweKFp6ypZ6NrbuFDaSgOw6arWefZusqSSLYUbgfqroXQYEa7nn8sO91pJC6dAJJviEgJufnv_qVL7ZjULd38ztYYDyWdxgPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#شرمنده_بابت_پست_رپی
به نظرتون ویناک به داریوش چی داده که داریوش حاضر شده چنین شاهکاری رو خلق کنه؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84169" target="_blank">📅 13:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84168">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تو این دوسال آنچلوتی که سرمربی تیم ملی برزیله بیشتر از سرمربی های رئال به رئال خدمت کرده با مصدوم کردن رافینیا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84168" target="_blank">📅 13:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84167">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTmUxeEmQPJ9e580vuuLY2ASfpIAD8Zp7OaRpfomxCVYMH8S0zV0cb5mWBkLdEfxDPOBlK7_EN2dbs5gVfiJCx7SCctplTodIrg4-t40W0ZGEKG3NbAAhSsUSmd_wkqIEh1IBaZp0SDiinQ8GIZv9QrB5G6ulWouX45xPceInwMVZu1qEIO8W-UzyQyERebHHXYHRIyUIdmj8sBycjWgZbIfLlsXIgGK8GLc81vJuCbfmp0nx_wUEzlUUx0TxEoGBppAsXlKNxil3Z0Zrf8fYRgtCks8vEHhsYWq241X3RLEilNsM-AWmTxkK008WP1zcGlKag7PzhQtpNDrKGm_fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو دین یهودیت چیزی به نام تغییر دین از دین دیگری به یهودی وجود نداره، هرکی یهودیه باید تو خونش باشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84167" target="_blank">📅 12:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84164">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سخنگوی قوه قضاییه:پرونده حقوقی ترور سردار سلیمانی در دادگستری تهران تشکیل شد که سه هزار و ۳۱۷ نفر شاکی داشت
رأی این پرونده دو سال و نیم پیش صادر شد و بر اساس آن، سردمداران دولت آمریکا به پرداخت ۴۸ میلیارد دلار محکوم شدند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84164" target="_blank">📅 12:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84163">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ما میگیم اعدام فوری بیرانوند دور میدون آزادی شما میگید بره سربازی؟</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84163" target="_blank">📅 11:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84162">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/398fe520da.mp4?token=G7zM2doXyfNHxc43z-VGsAtgnU2O8d5pJVA_nd7-xokgDCDQ2jLH9gfiV_R1pJ-jA2KJ6u1yJIoiSdCaAxjCGuMWIi7Uj_XemwMUKoFczblasaztqCVB6q9HqlP689y95es0CUCTTCXe4op5pdBc7j9RdtFuIVqYeBg8H5km_mqhSwOjJldMRPqrhoGUASQGvzfJvNdvSKj4KmnwFjRKRFwj692qWR9xbbz-7NjXJzT13U7YrXNKuCqf4iM8zKo6sr4s5U7ChqKC4ks1T5UrE9Yh7kOZYt8XGzH0Fvwvbtd1PieWTp3jCPUo8eYkFljLqfgWSQ34vd2SBDMwhI3m1m0TfzWn-FYXjP9mIwa9RGHrZNGEF0wGfIj8kX40SqS8hyGTwFkwSlwgP7ZBaLfPLdP7dI2OUX_w20r9T5XQ8YIsXlBg5qRIbAYeOcqvxTIOMEvrylfrKTs-7ATF6WceQNp3WHDHDv7T6MRDDrPY07g6A-ncOd448hKtGV-C5-UMTBidzeqgtaEC9GlwZdj9_KDfR_jElqII7SFwgylRIJJnn3KQWBNsg6a9sf43jCymElCRALtklZQvJp41LdJfxnJetGUIh4UxbHwGXI7FxsR0yC5XhX9Hu1unp_rne79pQrxwP-eW2af0nthSaND7QwZFoo7UFH027bpq0Hn7GrY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/398fe520da.mp4?token=G7zM2doXyfNHxc43z-VGsAtgnU2O8d5pJVA_nd7-xokgDCDQ2jLH9gfiV_R1pJ-jA2KJ6u1yJIoiSdCaAxjCGuMWIi7Uj_XemwMUKoFczblasaztqCVB6q9HqlP689y95es0CUCTTCXe4op5pdBc7j9RdtFuIVqYeBg8H5km_mqhSwOjJldMRPqrhoGUASQGvzfJvNdvSKj4KmnwFjRKRFwj692qWR9xbbz-7NjXJzT13U7YrXNKuCqf4iM8zKo6sr4s5U7ChqKC4ks1T5UrE9Yh7kOZYt8XGzH0Fvwvbtd1PieWTp3jCPUo8eYkFljLqfgWSQ34vd2SBDMwhI3m1m0TfzWn-FYXjP9mIwa9RGHrZNGEF0wGfIj8kX40SqS8hyGTwFkwSlwgP7ZBaLfPLdP7dI2OUX_w20r9T5XQ8YIsXlBg5qRIbAYeOcqvxTIOMEvrylfrKTs-7ATF6WceQNp3WHDHDv7T6MRDDrPY07g6A-ncOd448hKtGV-C5-UMTBidzeqgtaEC9GlwZdj9_KDfR_jElqII7SFwgylRIJJnn3KQWBNsg6a9sf43jCymElCRALtklZQvJp41LdJfxnJetGUIh4UxbHwGXI7FxsR0yC5XhX9Hu1unp_rne79pQrxwP-eW2af0nthSaND7QwZFoo7UFH027bpq0Hn7GrY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با یه پست رپی ناب روزمون رو شروع کنیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84162" target="_blank">📅 09:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84161">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">صبح دلار ۲۵۰ تومنیتون بخیر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84161" target="_blank">📅 09:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84160">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یسری رسانه میگن عراقچی قبول کرده تسلیم بشن و اورانیوم هارو بدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/84160" target="_blank">📅 00:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84159">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مادر ترکیه گاییده شد که</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/84159" target="_blank">📅 22:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84158">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">قوه قضاییه: حمید رسایی به بند ویژه روحانیت زندان اوین منتقل و رسما زندانی شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/84158" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84157">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmDxJFOEU8L4Vxxj45ADkAKdQJya9kU6B4EZgikHK6XMRozbwYBZ5xOI7crCBMkkMA1t1lb2lpOvu7vRYJpK4VFoKJVskrIp-PQV_iGqbBFtB11LsUN8W0lDZYfj2kKhiK3mWNYy-ibmmm28w5BVvG5zDTLl6Im-c4xNi6Kojrju_I7t_itoe3MIhqElktOlOM5bJ7EHjHa3gcI-n8eelK292u8-zDibi6E5OmPUzBSJBRG8_6kscgC3mlzATaVvGYbzyt0a4XkS5dmqqdPzby57lK0k-BWwej6QJatVAedm1XYJQUYXIKy5gqu6iED0qB5rHASFFyC0_u9wv-_rIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه:
حمید رسایی به بند ویژه روحانیت زندان اوین منتقل و رسما زندانی شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/84157" target="_blank">📅 21:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84156">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJgSwPoUhAYn6EJ7Qhf7BaK8LczXd_dqrqlfhq28HYQBYqVn3GzeVhauvS0Slbr7V1OidOvOU5Xk31GWb-AMjsyqTSgtV7P6XOfMDQjn7H4JlpkBwjGY6LmVC67pFSMT62-UNCvzIljvTazUrvZcdyduYB1e5UQQZnfjY8g1c-g72Mw3bYDQSqGF-L4SoEHghHsgBSsOz-qdkl7k_MG_YU02PLYSVVRV6tQFAYJVrWFsz9CmwdpCSE7uKoI9LjPHjwQqENbpMF2gJW_f8MPvmJXNePbJ2CyXJn4xZjDGWnZDtO4O2YrTF4HBxFSXyhQAmyqzH6iJKJoeMeLB3OzVJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من وقتی یبار تصمیم میگیرن رو فرانسه بزنم بعد عمری
واکنش زیدان:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84156" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84155">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bF0QIHPopLYmREAcRF9UxXV_FoCrNOW8yIyOBNan6WOKup38xO0lh1opXWpwsHWz2jnYsRzmpa8jCoymyZPl1HBKI2NKyQFm1pyrjYkiZRcjZVwwMXdLh20C-Al8kETs3109eTYhWpxobBfnPgwOuXZtqxbKwYRRdf69tuQOp_JtLXB9nI4oiAdmY2Yxbd6oOXOg4vAOrLfX_lhcSulMjZ6BDat9TiR4GhbLtH1MSV8trhhItjgBjckltXIpV01F0QPXWsd5pXoaDELiyY10KSAKe5fNzhUvqZghMEmFlesCAKRsrufyE4qiFhqnVQQ49SPlBEFKV2gCArXPvb4yhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلیت به دخترا
ایسم عکسش با زیدشو استوری کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84155" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84152">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff9d6bc22.mp4?token=RRg8j3HpmzZ6mgesOAzWQW5qRYqGkLGP_POWK1Wjdt_i1uR4QVAcE_ChuI9wNT-WysjlYggPH7cwMUoMTemAcGVn_AbEWMGalTqxQaib9y7HiitPNyvo76VVuxMCav98Y-JX9EL7UK3rR_UdmrEISmcUDZa9AyadpBkXSP6HxKjYcq4RHmTI1W6-mc2Kpx-akv47t-7yfj6MBjSmYTnas5lX-o7ksb4QxNoR5QAfik-OEfTl3eHMEs4Uv81vanQzpOiqGJt9KwBHgR3S9X0PeCj6UiOhQN7Uih43gpbKEk-pKDWsJ_dwdvaxJLHhcjG5fl2Qu7fR2GSaTN-4Dm1YaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff9d6bc22.mp4?token=RRg8j3HpmzZ6mgesOAzWQW5qRYqGkLGP_POWK1Wjdt_i1uR4QVAcE_ChuI9wNT-WysjlYggPH7cwMUoMTemAcGVn_AbEWMGalTqxQaib9y7HiitPNyvo76VVuxMCav98Y-JX9EL7UK3rR_UdmrEISmcUDZa9AyadpBkXSP6HxKjYcq4RHmTI1W6-mc2Kpx-akv47t-7yfj6MBjSmYTnas5lX-o7ksb4QxNoR5QAfik-OEfTl3eHMEs4Uv81vanQzpOiqGJt9KwBHgR3S9X0PeCj6UiOhQN7Uih43gpbKEk-pKDWsJ_dwdvaxJLHhcjG5fl2Qu7fR2GSaTN-4Dm1YaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حلال ترین استفاده از هوش مصنوعی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84152" target="_blank">📅 20:09 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
