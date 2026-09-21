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
<img src="https://cdn4.telesco.pe/file/JSP0A1E8GkF8kgJUtifiL_10rbXFLkpqqGxrcC1NsshkjwlhXt5CsdIWcvhA2qnSUknBVgSIdcHB_cx78QF9ZAoV-SRLtMSc0w1ttdlyT9Qi92n_QJinReWIIx3MU2YW7IxlVAE8A0IfE47RRlsfYbuE1b5AfYdHvZ4H1LmcsO1pagbRp6ueJDIwfFHLgkGgqyW751GDWeGzYBaCHkyQDhjq_clVQ2MJb_42hmqO8D6kwMGMDVPvQBBqdDJ9gnSgA2Ro9cnOsHZE07jMFFiiei03pYHF-yW6J_VmzxodrngQXnQmGTKFPV9OAhnTrq-DkVud8bmH60ZuO6zvtHPnBQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 15:01:28</div>
<hr>

<div class="tg-post" id="msg-463393">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5df56c00e.mp4?token=qQWbedA7jGaZEOWuwub2-COqrjTaMscaFlDxN-Sef5f20dK_MgnNx5WsFUvSCPWxnyEbfhsLOuRGYSbNcfOShkCZrkjLSHaIb8QrsgyJrCJk1sxUXy7Jc-e7M78ib9imvHgOE0t0ojZuPNrzbIyGvqMINWSR4VL1SR9rPpbk3au-H1_WCCAnBaLbbGF8XqyylOCp8NLOIU6vNEM-f1BoxFKqmjwgnx_tcu-DUTURK6MK2a6o1A5XjHPFydYQuYCxoekyA58-ckxVfLk0J2TP5IegEYSZUL2DleVP8ASijTM1pZ1AneTvwgsz6XYVaJ-f0pzcJu_jnMAjQnCkbQ_0yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5df56c00e.mp4?token=qQWbedA7jGaZEOWuwub2-COqrjTaMscaFlDxN-Sef5f20dK_MgnNx5WsFUvSCPWxnyEbfhsLOuRGYSbNcfOShkCZrkjLSHaIb8QrsgyJrCJk1sxUXy7Jc-e7M78ib9imvHgOE0t0ojZuPNrzbIyGvqMINWSR4VL1SR9rPpbk3au-H1_WCCAnBaLbbGF8XqyylOCp8NLOIU6vNEM-f1BoxFKqmjwgnx_tcu-DUTURK6MK2a6o1A5XjHPFydYQuYCxoekyA58-ckxVfLk0J2TP5IegEYSZUL2DleVP8ASijTM1pZ1AneTvwgsz6XYVaJ-f0pzcJu_jnMAjQnCkbQ_0yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم آمریکا پای صندوق رأی از گرانی و وضعیت بد اقتصادی می‌گویند
@Farsna</div>
<div class="tg-footer">👁️ 373 · <a href="https://t.me/farsna/463393" target="_blank">📅 15:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463392">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36ab28dc44.mp4?token=ScezvvAkeL77yWfPMkPZWBF6vicBcva6VbIyg1-aYc8KS4MZg5YwaYM5HinoJPbxQwGq38pokVBLz_c8D-lBybA3X0n6_JW6991H1nPr0AklG02Kn7G0JKk7xlZg-fb9jFX-BvHekbSmSh9Wka86oN6XXcJV04UEQx30I118iWMtgU87z8CXzMVBwFplHcylmjCKSMikU2e9f1wr2wB-4OqX9JZnOdDQOjQoSspriPMAdvGOk56PbTyzGrXgDbsAvTDRmoe3z4XANd1AL-QUQKfuRtvhYRxVr62-c-_-4FSTMiOyzdb6GpClNBbheCrShmsIRrSYK97seF3yUOMLQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36ab28dc44.mp4?token=ScezvvAkeL77yWfPMkPZWBF6vicBcva6VbIyg1-aYc8KS4MZg5YwaYM5HinoJPbxQwGq38pokVBLz_c8D-lBybA3X0n6_JW6991H1nPr0AklG02Kn7G0JKk7xlZg-fb9jFX-BvHekbSmSh9Wka86oN6XXcJV04UEQx30I118iWMtgU87z8CXzMVBwFplHcylmjCKSMikU2e9f1wr2wB-4OqX9JZnOdDQOjQoSspriPMAdvGOk56PbTyzGrXgDbsAvTDRmoe3z4XANd1AL-QUQKfuRtvhYRxVr62-c-_-4FSTMiOyzdb6GpClNBbheCrShmsIRrSYK97seF3yUOMLQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ارتحال آیت‌الله شبیری‌زنجانی را تسلیت گفت
🔹
رئیس‌جمهور در پیامی رحلت عالم ربانی و فقیه صمدانی حضرت آیت‌الله شبیری‌زنجانی را به محضر بقیه الله الاعظم(عج)، مقام معظم رهبری، مراجع عظام تقلید، بیت شریف آن عزیز، حوزه‌های علمیه، شاگردان، مقلدان و ملت…</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/farsna/463392" target="_blank">📅 14:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463385">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TaqY9wGJqsO9fj67VLxvCV77yasjNaPUeGGlikYLGCARF1UvKDnmKF2ZnNXrTIEWqQ1TYL4Fggl6oAZyyweTiPlNllTqa4fKEv372TWCG-wisRjU1gT82MY4fHtplx1w6NuVXR10oFRFzTIMFKhhW5XopgnJg9juhsYxdcu5tjebpgcMzk-VODvVx3SLcjXq5WyqtFbM_7_ej7YV02cRBxyvPtKmpCRBloo7h5b8U6RpjJMrFk2X67gu1WzzoIyKn5-luDGqCcx8Y3spphAQSy4ynSpudQWSZQYNV_1riGm-d2o3CqpUKzSZOsQFxPdki9mq8FGMSYKYil_XYHVNEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F9a2VEBdrIFouBsKcTBuJmYLMvMAebjgQG4GT0bPEmeyFOrF2EWXanKEONkaluCSFXa0VAl_6QCvLRQ9E8di90wzKc7T7Ga74VtWED0gVBJEC6UJZHy3sInIh4LoIo3oq61qslrVdblxi1qLDEmJSDIeR8rEDaipJmqtml2osw2zsn9V5xn_d5Y_FFllwMCULbg8sC3PVFAGyMvON2z2NwDeGbVqENJILwGdgVFNDBTy4NNF_hzq7_90GT5lIj3SKCIpA-b-SC5ZlhIvgj_v8hkkodX593X83x8jNQlMC-MZFaO0Z7Ui664u_K2nF0F1HKfCQycKgF4t_qfP2YFhxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tl6-MVFZRniMup4PQv9DlR64W0dDvN99O-95P_g4PFUMmnYHmFYvMWFm6umyrvZ3QtV1HX5jJDkuboUlLdwt9pTBsNh50IUrJ_SI76ofNExPruaP4lwHDaPPeB8Oq4N7X_vkDDJbTPyi0nmrSriXXVslbrB0uTMNKtLzyma20pFramhfbz1M0U6Sd_8F6P1WZ3JRnJTZDrzqnZQE7O6LGnHrZZB8OTgRhHqJWFFRZqghOGD_uuvP1ZZZUwtfbsFQEb0SHcbxNrcRDwRyX5K7Ejm4CrQoZI4WyHfUbZwIymlSrmlKQ_DoXWyZ_-jjANmZ6G_ZVkL48-wXZ5WEXCeX6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HNIEV6k7S-o9kEXflKgUzGvpccd44CGQFAM7HWqslfeXLxsnnZ2fzEM7fPFMYMcCJgATqEj-ItIddo33Iiosa4CtqMeN2d3L09vh07CIjbP_KoBOgyB_v9P-eciBA3a85TBbauaY4XAFJI_eqtawT6xxYWQk-Hq_PRCY2oKiJN2vG00NdQwFjI3OAwfZE-zI1dMUYF6OjBTDM2p3cpdoO67B_Y1ObCO0Qtp8Stv0TX17mFX7-raE3r5OCnW56Yjao8qJxLjjVDVt6YvSAoXKaDK7PAby2vWZL2UGMkBgDqjCs0O46hDxUZvGpa0-joZoIZBhNbyBh9tGg4H0iwYeQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KEbDYmNuRZFHzD4nxXiWCxvwCafnugUWR0E5PzObZ8dL_BhW2QoieBwE3azxZzv95rDL6ivqt39a9JIYHf94zPmI_Koqxmfzr82nx1XackbRxPJtqSD7u2zIuKbfBiAd872nJnrQEsFRU_LCapB241pk_mu-4KsnLf6aPKjLgtvdWqmvlUCWv9Yd4hZdsUByVaxKPhZNiXoCyBAX4bcaQJRlzvc_Zw9TPqLuael0UtOm1RsVDZ-a-FEmNHexxY44M0sx5mUuaVv4p0fKNt7rTjZKLMc4pYmLJspgksZWyym974KbS752zGuZcp1jcqW14j4TNoMGkGomofXupjFMSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q3juuWVVq3VPG2k8i0eDP761dHdlFbOcbXyJ-uIQ_bdXr1lpIg8EwrPDdtayrkjB8cjCBZkc8t60dYuDU0CiyeNTzWkqcFFnys8WcuIxSmehkNbdyDtNAYJ5epmMfRKP4r1v78G_nKFq7XP8IZIImKW_5Ab1VKSh9R3NLeagtZ6uwdhShtp5gsPa9iGBQUU8fi94gZnFHxT2dad6fX-uMb4PGtSCNsuoGI4ro27tPNWb-tWRAHL3_vamqIFksGwUSIMNvOfsK-Xe8tNjkFH9e2dt4NWtcMv9QbxrHSxVbgWVEHjkyQPUe2_T6UFhzC-rYfW56HAWzvcPVg_PbLJ9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TaFYzUx54zr1Bbq1es545m0AyOoKwHyCQH5f_v08LJZ7XuYHgD3abF24GQMu6fKTNZ5NpK85A_CoSOXAA3k4ZQZbzlCBAX3Kl2pwNrD-n9GkwAy8eqKadYsAguULoyoNYjLOooz2FzawQeAQCzQynaB3Qvj_h64kOY1sUwUUa8-dyiDTaT4jWWnowEaFPmvKnSR8b49rFXcBmsqqMOJ2vnFCaJsrUNHfcG39meEnFUglpgSvW3j0f_wj6ggQ0nREJhBusQbMD3JYBrmLxo4UNKf39ZHa81KIQp9vJ6OMgFo4-Vg_Q1VJG_k9w56aRBQcepdid4g1d7Pwk1wFP43nMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن جوانه‌های ۱۴۰۵
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/farsna/463385" target="_blank">📅 14:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463384">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b04b9187.mp4?token=vnNIxCXnN8aNCp8iQkxDRj8Z3Rxz0D8u7EtWCf4teUmJT-iEvvy80_if1XatXbW5MjQII207rTxulLQbgpTy0u6TM-x5SJjY_hjbXT1ETCj0jgOAbv3f1o5dwejaZkdZwjyRegbg72dUaQkU6KkDP715nH6P1c2Nq3_y8M4WITiJe9p7FhCcCO05Z6swl-S-N2zXoPOW3q2TZFRDGW-sFq2Jt7figcf3PUotNxYB462cKserdV9dwTO3rIBOMYsosvlkvUH1wLN4tbuP6zm_u5xCEySMBODLIiWcbFCDXRvVK7dsV12Ds0UV83y9M3E8d72E46T4hAg8UtizoP3h0bquQn1XUttqqukGD-NZhjb1ZsZOyehvf-FHRR87db2O9D9ffyfpTl2ouv-IE_HYT_qrhD6DXeaQo2W18DJ73BRPce-jGANStpmra02Oh0E0E7GCv1WfokWqoP4VaxOrzkn7oYAgx36kR0cicqz8o7NSPzmAaOts-1qMAWH1i8Dzdrzqqmpe9je8xyjWYKLV3nwCGrer_7QcULiFtT7tQzwtbyJ4NOkDZsqvoudg2xm6ES3hgXhlBfRz4XbVRFDA8vXe-lIOqwW3xgztkG301Xg3NhJiijmSV2cqsqBg9GqIEo41PoLXW6pZxzqICRAkrUdyJavC11m1Rfi9YUPhmfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b04b9187.mp4?token=vnNIxCXnN8aNCp8iQkxDRj8Z3Rxz0D8u7EtWCf4teUmJT-iEvvy80_if1XatXbW5MjQII207rTxulLQbgpTy0u6TM-x5SJjY_hjbXT1ETCj0jgOAbv3f1o5dwejaZkdZwjyRegbg72dUaQkU6KkDP715nH6P1c2Nq3_y8M4WITiJe9p7FhCcCO05Z6swl-S-N2zXoPOW3q2TZFRDGW-sFq2Jt7figcf3PUotNxYB462cKserdV9dwTO3rIBOMYsosvlkvUH1wLN4tbuP6zm_u5xCEySMBODLIiWcbFCDXRvVK7dsV12Ds0UV83y9M3E8d72E46T4hAg8UtizoP3h0bquQn1XUttqqukGD-NZhjb1ZsZOyehvf-FHRR87db2O9D9ffyfpTl2ouv-IE_HYT_qrhD6DXeaQo2W18DJ73BRPce-jGANStpmra02Oh0E0E7GCv1WfokWqoP4VaxOrzkn7oYAgx36kR0cicqz8o7NSPzmAaOts-1qMAWH1i8Dzdrzqqmpe9je8xyjWYKLV3nwCGrer_7QcULiFtT7tQzwtbyJ4NOkDZsqvoudg2xm6ES3hgXhlBfRz4XbVRFDA8vXe-lIOqwW3xgztkG301Xg3NhJiijmSV2cqsqBg9GqIEo41PoLXW6pZxzqICRAkrUdyJavC11m1Rfi9YUPhmfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب‌هایی از دانش‌آموزانی که دیگر به کلاس برنگشتند
🔹
پزشکیان با حضور در کلاس درس، به تصاویر دانش‌آموزان شهید مدرسۀ میناب ادای احترام کرد.  @Farsna</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/farsna/463384" target="_blank">📅 14:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463383">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lijoKQu54jtr0UCkpLb3-4BFuBvOWwG2OeLn6wozLE3y_gCo8X4B-2luHkND0e6A4wxkrt3rS_MTTMGPVIszYLHc1ER9YkhwMaFJBKpxpF0mcljL0Q5w4jEKg5EnGS43hHJBjUAa0ZfDYq7UdJKHjNsyPEcpunUyHXM0_UIb34ExCHgDYnQL4yh9QEK6WyoeQx0NWo8pbplYwOMF-KN8QgiQ7Z0I6glB4x4IKwax5wmG3ilwdfDOTrlb3dk-3OukvA7aMMo1QVjtp_S9-d7yio9hSH8j8dyxjd5qmeEIDDlKzbo7cf5h62XG4r-GlZm2QoB7MxB0GoydfYMPFgz8cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ ورود ۳ رسانهٔ بزرگ آمریکایی به کاخ سفید را ممنوع کرد!
🔹
با اعلام ترامپ، دسترسی «سی‌ان‌ان، ام‌اس‌ناو و پولیتیکو» به کاخ سفید به‌دلیل آنچه «انتشار مداوم اخبار دروغین و سفارشی» خوانده شده، به‌طور کامل لغو شد. @Farsna</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/farsna/463383" target="_blank">📅 14:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463382">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b390ee69.mp4?token=LqWyk-19KYh-RrDopnWRV3R2Xjzn46pNjDsckwhb4x1H2Kuvc9OpQ09G3BfxmpNN1iPCOh142aCdutbUjtoPruENK9sFFN5GuYhtKjfEanpL6ExTz6if5lQ2qjm1qmdvWMR7Y2M16sOL4cBqnZdIuF8g3aDv8ix-YQnd1rlLtYbOsuk_rNufQttBkKhdzhMECupObiBNBfVpqR8CVd67Ms_8xFEajfLFvqTcvqN2bh3zz6rXiAVNlJIiPolLPfugBNE9sajkZurfJVs7JJ0MGYMJ-BjCq9X2ETbLqElMpuVVXVRqUEgIbrV_twwqrqTw247fUBtTqHuP_jyURR7_Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b390ee69.mp4?token=LqWyk-19KYh-RrDopnWRV3R2Xjzn46pNjDsckwhb4x1H2Kuvc9OpQ09G3BfxmpNN1iPCOh142aCdutbUjtoPruENK9sFFN5GuYhtKjfEanpL6ExTz6if5lQ2qjm1qmdvWMR7Y2M16sOL4cBqnZdIuF8g3aDv8ix-YQnd1rlLtYbOsuk_rNufQttBkKhdzhMECupObiBNBfVpqR8CVd67Ms_8xFEajfLFvqTcvqN2bh3zz6rXiAVNlJIiPolLPfugBNE9sajkZurfJVs7JJ0MGYMJ-BjCq9X2ETbLqElMpuVVXVRqUEgIbrV_twwqrqTw247fUBtTqHuP_jyURR7_Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرخ نژاد:
پيشينه بانك ملت در ايفاى به موقع تعهدات، زمينه ساز اطمينان سرمايه گذاران به اولين صندوق ارزى كشور است
▫️
مديرعامل بانك ملت در آيين آغاز پذيره نويسى نخستین صندوق سرمايه گذارى ارزى کشور (مانا ملت):
🔹
در نخستين صندوق سرمایه گذاری ارزى كشور، بانك ملت مدير ثبت و مدير عمليات ارزى و همچنين ضامن نقدشوندگى است.
🔹
ارز منتخب صندوق دلار است كه واحدهاى آن به گونه اى در نظر گرفته شده تا با مقادير حداقلى نيز امكان سرمايه گذارى براى مردم وجود داشته باشد.
🔹
ساختار صندوق صدور و ابطالى است و سرمايه گذاران براى خريد و فروش نيازى به بازار ثانويه ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/farsna/463382" target="_blank">📅 14:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463381">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه معلم | Moallem.ins</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWgCjJ5VwNgED4fjoQ0lgqSiRy1Fo2dBXQafdPVkD3Jodtxz7AT69shPcyEV65HNrGhy4zmXVuEplgqKrX5WmxEvxtnGY8fSbjGKZ7EtayOJ8SNOaJ_W6ycNrE3cTR2NFo-UIAXr_Ns4GbW7Md8vItI__lqrgfU0vkM9wQU68IQQ60a-ZtyVxWSylQOhhSSmHWtihpkt6xN1Y7XbIPAaeOwpFsN3uAqJAnpVM79nVwdvpG8dNUFkUvk84VJybXwI41sUTOe1i7-GoLMS6l6lZps43qe5KIs_oeEV-PUSvESi30onsajHOF0BSiO39kHaT3psfNu9PiFs8ijwrvXUEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز جشنواره «مهر معلم» با تخفیف‌های ویژه بیمه معلم برای فرهنگیان
🔹
بیمه معلم در آستانه آغاز سال تحصیلی، طرح ویژه «مهر معلم» را با ارائه تخفیف‌های ویژه در رشته‌های بیمه بدنه خودرو، حوادث انفرادی و آتش‌سوزی منازل مسکونی برای فرهنگیان و خانواده بزرگ آموزش‌وپرورش اجرا می‌کند.
🔹
به گزارش روابط‌عمومی بیمه معلم، طرح «مهر معلم» از ۲۵ شهریور تا ۱۵ مهرماه ۱۴۰۵ اجرا می‌شود و فرهنگیان و مشمولان این طرح می‌توانند در این بازه زمانی از شرایط ویژه و تخفیف‌های در نظر گرفته‌شده در رشته‌های مختلف بیمه‌ای بهره‌مند شوند.
🔹
بر اساس این طرح، ۷۰ درصد تخفیف در بیمه بدنه خودرو، ۷۰ درصد تخفیف در بیمه حوادث انفرادی و ۵۰ درصد تخفیف در بیمه آتش‌سوزی منازل مسکونی به مشمولان ارائه می‌شود.
🔹
طرح «مهر معلم» با هدف توسعه خدمات بیمه‌ای ویژه فرهنگیان، افزایش دسترسی این قشر به پوشش‌های موردنیاز و ارائه خدمات با شرایط ویژه طراحی شده است؛ خدمتی که تلاش دارد بخشی از نیازهای بیمه‌ای فرهنگیان و خانواده‌های آنان را در قالب یک طرح اختصاصی پاسخ دهد.
🔹
در این طرح، اعضای خانواده بزرگ آموزش‌وپرورش نیز می‌توانند از مزایای در نظر گرفته‌شده بهره‌مند شوند. متقاضیان برای اطلاع از شرایط و ضوابط طرح، مدارک موردنیاز، افراد مشمول و نحوه اعمال تخفیف‌ها می‌توانند به شعب و نمایندگی‌های شرکت بیمه معلم در سراسر کشور مراجعه کنند.
#بیمه_معلم
#آموزش_و_پرورش
#جشنواره_مهر_معلم
سایت
|
بله
|
اینستاگرام
|
تلگرام</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/farsna/463381" target="_blank">📅 14:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463380">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/farsna/463380" target="_blank">📅 14:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463379">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSfyEP3mR5EUi3IPGqLe7hlsu4gz8Mh1TNXXEOoSFPTK8QkjRDwOF0IDXP0szNzXdANp62bclTG2LxMvRE1t6-Ln4iG06NiAw6rRhGgDaw1jGEoZts6TD4uboYmrPDlDcMoQp1lDptiLEXeC4_JdH5QWpHXLcbOMZoRYzd6tEoF0hXyYMUJ7g0RiMfbqACF34aUk2MgW8ykQ1z3BOaTqXeJcprzGgR5nJky5a0m-r6RG29iZ0FUEzCNszhCBfgQAqDD4i9Ak6MWE7g9SLaeuI-_1jGF-8f4eYxZADkxd5_xKJNNMfFMshbNrV2ZxjUwiRtvYCx2VkX59LW-JoAM4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: سفر وزیر کشور پاکستان به تهران دربارۀ روابط دوجانبۀ ایران و پاکستان خواهد بود و قرار بر تبادل پیام خاصی دربارۀ میانجی‌گری نیست. @Farsna</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/farsna/463379" target="_blank">📅 14:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463378">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsMqM1-c-WgogWt4exYUMRrP0v_oFLyJbst94ihoIcNCfV_opavi51wQHx_CdGpQU36JhP5kMp4Au8n-DMKruJD4lshmGjePFRMWP9t6jqsd0QMVbAFD_aHCSF0hcTRXu7HYQTNmnNnbX3jdldwmeRu7M5uX1iGwYSYNdebDdH3iIqEqm79HoZPD0ZlA5xy-UvLXF2iSyZ1Q2-mv8iCh0zF4jcdxYPPPX9hVJaXTAkUH22Mywqv2y_OWhQNuqOAlgURsI4Dy7mr8psikh25_ksASI_waowq6Xl1-xaRWEJgjMmHyY-tVvJcX7c88hAKIG4SQH8KsG7LFFgoN9_hltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز زبان فرانسه یا محل اجرای پروژه‌های ضدایرانی!
🔹
مرکز زبان فرانسه تهران موسوم به CLF که امروز با دستور قضایی دادستانی تهران پلمب شده، مرکزی وابسته به ساختار فرهنگی فرانسه است که مدعی‌ست در تهران در حوزه آموزش زبان فرانسه، برگزاری آزمون‌های رسمی TCF و DELF/DALF، تربیت مدرس و ارائه خدمات مرتبط با تحصیل در فرانسه فعالیت می‌کند.
🔹
این مرکز در مرکز تهران و در محدوده‌ای نزدیک به دانشگاه‌های مهم کشور مانند دانشگاه تهران و امیرکبیر مستقر است و سالانه تعداد زیادی زبان‌آموز را پذیرش کرده است.
🔹
دادستانی تهران در اطلاعیه پلمب، CLF اعلام کرده که این مرکز از پوشش آموزش زبان برای «شناسایی، شبکه‌سازی و تسهیل خروج نخبگان از کشور» استفاده کرده است.
🔹
دادستانی تهران همچنین تاکید کرده که این مرکز از عنوان زبان‌آموزی برای اجرای پروژه‌های ضد فرهنگ ایرانی – اسلامی و بر خلاف امنیت ملی سوءاستفاده نموده و اقدام به شناسایی، شبکه‌سازی و تسهیل خروج نخبگان از کشور می‌کرده است.
🔹
فرانسه در سال‌های اخیر در چارچوب سیاست فشار غرب علیه جمهوری اسلامی ایران، مجموعه‌ای از اقدامات خصمانه علیه ایران را دنبال کرده است.
@Farspolitics
_
link</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/farsna/463378" target="_blank">📅 14:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463377">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCghkIO3VospfVII-ynp0ao3h6QBdzu3uXrpWoY-SBzy7l-RQOwjHsjHkxvAWEifpWrXqPBw4F6ZWGIooRSerju1DNB9nAoNLBKqQqsVk3c4vHiEA6x6vIZHJAuxLY2gp57c2Gx5Un30ZCAn7ZSxcOnk_vLclBFKrPWJEB9bOnH21lYqlUvuocPitKPWM56wMNXdePSoeMHTdvvydJoS5kSJFHTZ8-_DaXFqMqfwKcLvOYm8YL-8_A-jEPVdVVMXKKcH2Q5PS1sYlsghvVgKNAip4ZV8DYEUhwQgUke2AOBxelaxpD4pe548CTBP0B-dz635AKziY_254QdjVcxvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده‌کل سپاه رحلت آیت‌الله سیدموسی شبیری‌زنجانی را تسلیت گفت
🔹
سرلشکر وحیدی در پیامی به‌مناسبت ارتحال آیت‌الله شبیری‌زنجانی نوشت: رحلت جانسوز مرجع عالی‌قدر جهان تشیع، فقیه اهل‌بیت عصمت و طهارت، حضرت آیت‌الله‌العظمی آقای حاج سیدموسی شبیری‌زنجانی(قدس سره…</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/farsna/463377" target="_blank">📅 14:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463376">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_l3uHug3JyxytvJi2RbZC914TpFCqNge8ciwsySubQ7R8EnMXPlmt99bukdGH5mSwkmU64XATUIc7_FliRyiYmbPZYVXwCpQpZPm7z7KHo0MHtQFqqGcJ9Lhzr5zDnA2qUissWfjwrnUwmH4ywURTvuTo7LEuW8AfrYZNAlcSK1KT7kLl_BBX96jtRkVT_lz7XX4fSnsZXAKzuoXSITSZa4XtQtB3oKG5ZQsDZYO3769yoCVodLR3_2Xa0Sqtp3DjJQyxydR5GJ3-NA3CqrUxsYn34-PurPYBR9QdWy6T6mnpfrB5rJ17N2LrLr0YoK_xYURah5XEd4lEh-UPwTrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر اقتصاد: ارائهٔ کالابرگ با مبالغ جدید به دهک‌های پایین از ۱۵ مهر آغاز می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/farsna/463376" target="_blank">📅 14:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463375">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqT1Z988ZQeDp40pC-jCs86SUAcTlgGM4O0Nd3qufgqej5BLACJdDm3RfbH8u8bjIe8zhgns7Yx01lT7RNTW0bf3K6kfq-0dNBjVmnYF41TX_PFnBVtf3r9RcrRJq-97f66asze6JP_pfMvdKJwamHbWNec8i-f3KV1OAG_fXxfaJLhWg97Lve-5S9DmxDXdKC24akAi8j6POZaR0Y19dUzOhUbLsKFCerqKgXw1UXe_yoMHem0gTaHvgXbia2IvSq87tGcRCteXJ46GCJGSE2QYrMQYdHBHgg3fmwPLPqj2-02zlOm5Uf_ahVUVODAt6VS0uCKP7PMzodoGO_F4IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر ارشاد: ممکن است در صورت آماده‌شدن مقدمات، نمایشگاه کتاب به‌صورت حضوری در آبان برگزار شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/farsna/463375" target="_blank">📅 14:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463374">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وطن‌فروشی جدید سردار آزمون
🔹
در بحبوحۀ تنش‌های منطقه‌ای و همزمان با حملات نظامی آمریکا و رژیم صهیونیستی با همکاری امارات، سردار آزمون، مهاجم تیم ملی فوتبال ایران، با انتشار استوری‌هایی در صفحۀ شخصی خود جنجال‌آفرین شد.
🔹
این بازیکن که از ابتدای جنگ تاکنون…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/463374" target="_blank">📅 13:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463373">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09914fb83.mp4?token=HtU0yj9eys0w_-Q-1UqmkUp1fkUm8-8x6_OZQ_t2nyepCaeykuMAw28MdgqD5rAE6jHff4f0naH5NlMyVPBcLcWIwCcLXohX7II3ETQvwcaykDJm_lW0wVAQ4cT9FCS1WUIwPSLT3MNhf7XgXV8bAARnwiNpHNw820EMyuhXTNTzzMb0SxmafJk61BK6U5ESAmFNTPc9yKGsZ-e5CfHoJVtioPAbg4lbZY7K1biYAuis69-yrPLECwcGwRdL6lyA_0V-3hxeoxOPrPuuPYKSL1Q0xY76LR9WBGwVcgKftCAhM8j-_uzp9UdG4ooPrtkItx-EiYBN2AKbpwPyoZ_1FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09914fb83.mp4?token=HtU0yj9eys0w_-Q-1UqmkUp1fkUm8-8x6_OZQ_t2nyepCaeykuMAw28MdgqD5rAE6jHff4f0naH5NlMyVPBcLcWIwCcLXohX7II3ETQvwcaykDJm_lW0wVAQ4cT9FCS1WUIwPSLT3MNhf7XgXV8bAARnwiNpHNw820EMyuhXTNTzzMb0SxmafJk61BK6U5ESAmFNTPc9yKGsZ-e5CfHoJVtioPAbg4lbZY7K1biYAuis69-yrPLECwcGwRdL6lyA_0V-3hxeoxOPrPuuPYKSL1Q0xY76LR9WBGwVcgKftCAhM8j-_uzp9UdG4ooPrtkItx-EiYBN2AKbpwPyoZ_1FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهریۀ مدارس غیردولتی از ۲۸ تا ۲۲۳ میلیون
🔹
رئیس سازمان مدارس و مراکز غیردولتی آموزش‌وپرورش: شهریۀ مدارس غیردولتی در مقاطع مختلف تحصیلی از حدود ۲۸.۵ میلیون تومان آغاز می‌شود و در برخی مدارس شهر تهران به حداکثر ۲۲۳ میلیون تومان می‌رسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/463373" target="_blank">📅 13:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463372">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh9NXqsSDdePOxYWJqTkPMrWjdGPNLi2tC5yZeS-39XK-Qkrfcyx4GdkfE0UzjWPRjgHuTkLC_APIM45EcNQV-pDKqSL95M4Q3ku5sPX_SQuKJYnLHUuei9wvV5UW6rh3HUSyor8Wx4RoWVbWgF4tiTrIqPNrquZZdD7n9nTPLq7tawvCO6w901vckjfzJrvF8fGTrCthctKIX8FgYMIDQqpYMj2-wk6fyppCn8Q226Y-9ZpPeP0vhmU24gSjhysLtN_0c77LlFGFbRFcpyuMtCu1ieC3ZEGr_CAHzWdqMiSXPuvudeDYOsBUXFdQhq03L5oq1o1gPORfOopa6XIaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله سبحانی: آیت‌‌الله شبیری‌زنجانی در علوم اسلامی صاحب‌نظر و دارای مبانی استوار بود
🔹
آیت‌الله سبحانی در پیامی رحلت آیت‌الله سیدموسی شبیری‌زنجانی را تسلیت گفت و نوشت: آن عالم بزرگوار از ارکان حوزه‌های علمیه و در بسیاری از علوم اسلامی صاحب‌نظر و دارای…</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/463372" target="_blank">📅 13:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463371">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjMgFFr2c8tKfc9wHStbVgT064ujbu3PzWqYuDAmX7ogVxLnIMv17r75mWX9h0ba-29PJB8N11t-1RInKCzjDptjTNYyv7lNrxN1WT5O5b6Q2C1IsFX5Mce0FkgqZAg5FOeJ4j7nHWyYclM-iu3oJtZIjhuxWVtXrAcaeUD70dxKB-KMOJjOWb09zr4BU7DqnzEDONL4KYlQznd2n3Ntgkf-R8QA07ej7hHuAv17nLfovpDG06hjsW94IiKRRFKq0hILLMDCzNS3VQ4bDDTbr7L_vFzAGTjiwRI1nMz85HXvAqJJEqdo_96xwuzdmlYyvbG1kHr8F6bWCKMs3HKrfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثه برای یک نفتکش در تنگهٔ هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس به‌نقل از مقامات نظامی گزارش کرد: یک تانکر در حال عبور از تنگهٔ هرمز توسط یک پرتابهٔ ناشناخته هدف قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/463371" target="_blank">📅 13:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463370">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s30SatuJY5c_gopbhr9sioowIcIR2IyBvsBO_D-MpDWxaGuRXbSlwMW38G1UK37dTC8zcLuX-sgCY5T0lezgIZHdM-4b4lOJ2cy7G03e7ICkhGineLRjh8uFEoduIRuC8uoITG1zc6ZjAJ3sD9xczWFvP7svtD0mpYaEaYLkj7yiNvgHNKYH4hhV6ZorV8F6l6smP6hPVkx7143K2pLl5sCbTzUHvvcO0UFlaM1zDTmE_n9htcAf0O6oweYXqwITuPdLQYZelqYVc2cZ6luGKL-SR_Uys23gx32uoDo_SR7Hc0vaY8JJglM0k-7sSoc6eIoQhbo9qilTVT9bWQqWlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
آیت‌الله سیستانی در پیامی رحلت آیت‌الله شبیری‌زنجانی را تسلیت گفت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/463370" target="_blank">📅 12:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463369">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1aWo1SnSQYnsTEL8CWQfH0Te_PsR6aRxx9ysSan1JsK4wzDuTYRkscLPpSaqK4c7vJj4S3dwgeDwQ6rXq1VDhD6l-IQAxwdIYTslMeG_ONlTYfi9vojCeTFunqucwIxe3GZLWcuZl--Col6n3RR1NJsx4aKR4E0FGVLirgkmeSLlTh2fohsouY0t9_wZ32cJFbtZNjwH85DZm1GkO-W9lJh1oqmIiefzVzT6f4ezTyIu6BDw0qz3h_6eGoV2rhqTVH4qGanqHNNxy_eozFRM71U30GyrrQXNJ0kwqjONBUJkO4fRcU8Fup3RVGnWPnf2C_OWdfFkPK_OSvcLfGQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با کاهش ۱۲ هزار واحدی به ۷ میلیون و ۲۸۰ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/463369" target="_blank">📅 12:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463368">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zgo2bg4DsluGxBldg2s42hdctgmcdgBCPn151Rv-w_psPRdJTkt42bniin7ayAyPHZs9Gtt7CtTLCWEWrnCoVMZq_KOANknnbf8G9i5EoQutO8RtHLyBM8Xz7koYbZiCmKq9eTWd_OdYg8wq5v2fyEH5lYCyrM9hKgdwEKU3xa6t_TX7KT1UYuzv5ajdyaLX8g24BbS2MwzFYaAaIpWClwOmYaNSrfd0b87Hb4BbNLuJqnOeMZJ0-vqKQsdQJCaZlomtuVYf76TBmYiZb-5GuHvEygTD1ukt0uTmKOYkBORsk4RO0JPbSnnJScC8dGN3qog1H8zRDAckjdqpsvwhFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«به وقت ایران» ۱۷ میلیونی شد
🔹
برنامه تلویزیونی «به وقت ایران» حدود ۱۷ میلیون بازدید به خود اختصاص داده؛ این آمار با بررسی تلوبیون به‌دست آمده است.
🔹
«به وقت ایران» با اجرای سرباز روح‌الله رضوی و حضور وحید خضاب و نیما اکبرخانی به عنوان کارشناس، از جمله تولیداتی است که از آغاز جنگ تحمیلی سوم روی آنتن رفت.
🔹
این برنامه که به بررسی آخرین تحولات ایران و منطقه می‌پردازد،‌ پیش‌تر هم از جمله پربیننده‌ترین تولیدات صداوسیما بوده است. بر طبق نظرسنجی مرکز متا در تیر ۱۴۰۵، «به وقت ایران» در رتبه نخست پرمخاطب‌ترین تولیدات رسانه‌ای قرار داشت.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/463368" target="_blank">📅 12:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463366">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzNiSJ660ZvDsMt4SONw-Xm0SUqZsbnwSASy6wQL6V_-8Yt2zPkSziJeTMvdoU7LFsrq-Mqmx7h6RTr6k-mJJqbp2MvDX8ymo7_Y0Qqxpr2iro_UWMyLQl8Eflv3IvY83L_rmSLsXmsvlT9wI53o0vbZOUuzp_dm7D0euW50EBZK9D6EFDRepc9PzMmgl6xCNciqzPDQjpjMCZhPSNVD5KizztJ9vFlJiKHnZhPBkvZITyjx5SO6AyPWDBGTTd7sIVA_3qEw0GoRFDMV7otAa6-emj-_6OIfl45USCim0MOXvSIWu_TM5vxjPto8aNGYWqhInJne5DMGX2N44itVcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس قوه‌قضاییه ارتحال آیت‌الله شبیری‌زنجانی را تسلیت گفت
🔹
اژه‌ای در پیام خود برای تسلیت ارتحال آیت‌الله شبیری‌زنجانی نوشت: ایشان از نگهبانان امانت‌دار میراث اصیل و عَریق تشیع و از استوانه‌های حوزه‌های علمیه و از برجستگان علمی و عملی مکتب نورانی فقه جعفری…</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/463366" target="_blank">📅 12:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463365">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">انهدام مهمات عمل نکردۀ دشمن در ملارد
🔹
سپاه سیدالشهدا تهران: انهدام مهمات عمل‌نکردۀ تجاوز آمریکایی‌صهیونی در شهرستان ملارد امروز از ساعت ۱۲ الی ۱۷ صورت می‌گیرد.
🔹
احتمال شنیده شدن صدای انفجار، ناشی از عملیات فنی وجود دارد و جای نگرانی برای شهروندان نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/463365" target="_blank">📅 11:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463364">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oE2u1Xtua2HkHyNVw5NJ77PBJ6rZvQZLcmjXrHRHqd9G4tOrE9lbjamXr01Q-6Exd6EDeYr0PpWb2_SyXxmxC6cX21j7I_aq8pdD3cqJbF4o-CeiaZN8XJhE2p0Jc64HXHoLJpZN60RHwyMKFXOjefmoJDmhUkyhhskkZ_9e19bgGz3VrWm2kqFQjn-Ch97DXoj9qUrwhP5HwSEZT8mVYboaoYAcix2YgSy5x-1UfotKwD0qWXKr2qvh-Zy2vJ8D2fvJGhB6yW7KrO2ZmeRRviv-ejw_butat0lKBH8YeiJo7qHCeVFb9gQub5l_Iwvki9OfgWFUYrjFbRkuZurTMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداداد عزیزی ۴ ماه و عالیشاه ۴ جلسه محروم شد
⚽️
کمیتۀ انضباطی فدراسیون آرای مربوط به حواشی دیدار تراکتور-گل‌کهر را به شرح زیر اعلام کرد:
🔹
خداداد عزیزی ۴ ماه محرومیت از ورود به ورزشگاه‌ها و ۲ میلیارد تومان جریمه
🔹
امید عالیشاه ۴ جلسه محرومیت از مسابقات و ۵۰۰…</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/463364" target="_blank">📅 11:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463363">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZ2dRWbUFlJ5jO203uYImFlhARoqNwv0Iam3s5ZUkN2_aZqkvJTN2qDblhV099tynBqs9-6oSaOe1TBciT-aN34S3f2SNQLxly-DGQMyZFn1kfvyc1F9261IykgIlDGAhGZ87IvOAPen62btOxkWuwqgsrZQJEuSJqcFry4gYpFIGxPeG-tXAduxNX5K9KTFkq8qvsoceDblM8qRh_vgtDlap40jr4Syx4ntR3_ZMMD-hSyds17SZLH3IhkwY0XCL8MVjLKgtFnO8MRrAWnALU26a-Brlh5O__KTykhimVNeZoWdLmXKN39q3G74tYxleAN47RpOyOouYvLhXTHjvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای مسلح: طعم تلخ شکست‌های بیشتر را به دشمن می چشانیم
🔹
بیانیۀ ستادکل نیروهای مسلح و قرارگاه خاتم‌الانبیا به‌مناسبت هفتۀ دفاع مقدس: کشور با استفاده از تجارب ارزشمند هشت سال دفاع مقدس به‌سمت «ایران قوی» سوق داده شد و آمریکا و رژیم صهیونیستی، در جنگ دوازده…</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/463363" target="_blank">📅 11:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463362">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پزشکیان به نیویورک می‌رود
🔹
رئیس‌جمهور در روزهای آتی به‌منظور شرکت در مجمع عمومی سازمان ملل عازم آمریکا می‌شود.
🔹
رئیس‌جمهور ضمن سخنرانی در مجمع ‌عمومی و اعلام مواضع کشورمان در خصوص مسائل جهانی و خصوصاً جنگ آمریکا و اسرائیل علیه ایران، با سران برخی کشورها…</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/463362" target="_blank">📅 11:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463361">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAtNwqoS9XdIsC_15eeNNMrHzPFNJ5KAXHii6sMWdCtR_VDv8FUQHPQTpzE3VDwLrKSPqpTC4XT6KcroItrYePM6Rjnmn5JwMo6MJ3dTGkQUe7WHeNapGQJ479r7nHzitwaJ7ra2TaumChKAHx5UN-uFJ3gN_-ggd_MR7JY-Ldb3yNaNAF6DpkJ81L9izr2A53mc7Vm0AIH6eHdljxKdKQ7M3Z1WiD8ZziN7lgJlfKe1Ed3--fmiMBBozskC41VywghkrmbimUZ2Y8zztyBLoeNN8IDAihQNv6qi0D4JlPv7j6tKkkhN1DLhdiW8vLVS-DRvLXKeR83ol_NLSm2nZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت فقط نباید صدای مردم را بشنود؛ باید واقعاً به مردم گوش بدهد
🔹
«دولت شنوا» نگاهی متفاوت به رابطۀ دولت و جامعه و راه‌های ساختن حکمرانی بهتر در دنیای امروز است.
🔹
شنیدن، شروع فهمیدن است. اگر می‌خواهید نگاه متفاوتی به حکمرانی و رابطۀ دولت و جامعه داشته باشید،
دولت شنوا
را تهیه کنید.
راه‌های تهیۀ کتاب:
🔹
خریدآنلاین
اینجا
کلیک کنید
🔸
ارسال پیامک عنوان کتاب به ۵۰۰۰۱۶۷۶
🔹
تماس با ۶۶۹۷۳۹۹۶ یا ۶۶۹۷۳۷۹۴
🔸
فروشگاه حضوری: خیابان انقلاب، روبه‌روی دانشگاه تهران، مجتمع پارسا، انتشارات فارس
🖼
انتشارات فارس مرکز جامع کتب رسانه
@Farsna</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/463361" target="_blank">📅 11:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463360">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دروس حوزۀ علمیۀ قم تعطیل شد
🔹
مرکز مدیریت حوزۀ علمیۀ قم: به‌مناسبت ارتحال ‌آیت‌الله شبیری‌زنجانی، دروس حوزۀ علمیه تا پایان هفته تعطیل است. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/463360" target="_blank">📅 10:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463357">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VG1ZYPO4MSKRrGumEbBnVXHhxY89ZkQnCerFJlchUANP3RgxcCVQ18mVQy-gkg2XWGAMXYB6uOpXzMOoCDJDZl3K_RRuTQUjnraY-p80NbrRh3rPaeyNeb6cBgc3T-GbmtDWsGMNTsF8GUiM-Qc_-pY9V9TRS2T7QBXIEj52zX-IyISo0WbnjglVe93O0AYzJYZWm7iOgl5dnrMPIaUZaRIrY2lV7z6HbQpjV4OUoHtAxx13k97FETMquFxFAEMyyonFgjr_FbtOoRPv51wT6Snbn1Pmc232E5ADxEXYz2J3LmVbH5ZWoFBJ0ePPCzXEAlQh9wiu3ekjDqpYOC2KyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mp7df8SmixqLvwQU21pCrhTSpsEXPIvz7fZ__rD8C9I8k2mFcSUmEpHAwFEL5UK9VU549o-s6CzaL4XvQOvHUCZ45b7lYAUsRM-6261vfWWTYsT4ZZEJstfDz6tKfCEF2KmdAnxltKisV-9K6VL5wZlpJ6rTZLJmT6OKhb53Dur3rM6n6Vo0_NYRRFv9e2SLJDJmXCUgBHdKcItgT9IfFKze8j0nVdFkUz-_IxHO2iIIXG_EPRg4yPTMBxR5uFePn5txS8i4HAu39jh85IhyiqC7BkYYZlWteiF1vkTqNTXEMZ3JbqDz6HZ2XZSV62-1LS07fGpYukKlHNm_-wNUfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qFHW8qZJ91W3eQ12iBAibsaeeGcKG1Do8VXfJT55Us1GxebypietvalijPNYhlDlm0vfIU5pkB3tFuyPj2O3vRkg1Kt2CMIy1_8OaidGCeYFsHl94OAPPlCdlAFxNsl3f8QsgTYZ4DzFNT4sqLvt3xwyb8ghSnK4nUHgbELpq7Ezk6UJBA2vsTdF44qezRf8Jg36xY9kl9wdIzFrJdCG5hoD7ZLDN7rox2QjmH4IiqeF1aEwNL6hl6XboDJgU44SoCpCAGCro4ISbXTRZW7aYxGsh0Pot0FyOSq-FK2RM_KyjdTd1Beh2QuIkj3nNUCTT449NBPbaGVSIZFSPtlklg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر پژوپارس قاچاقچی که با شلیک پلیس هم متوقف نشده بود!
🔹
رئیس پلیس پایتخت در محل نمایش کشفیات موادمخدر پلیس تهران به پژوپارسی اشاره کرد که با شلیک پلیس هم متوقف نشده بود.
🔹
سردار محمدیان دربارهٔ این خودروی حمل موادمخدر گفت: این خودرو که حامل موادمخدر بود حتی با شلیک پلیس به لاستیک‌ها هم متوقف نشد و راننده با رانندگی روی رینگ به حرکت خود ادامه داد تا وقتی که با شلیک پلیس به خود راننده متوقف و ۳ کیلو شیشه از این خودرو کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/463357" target="_blank">📅 10:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463356">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نیروهای مسلح: طعم تلخ شکست‌های بیشتر را به دشمن می چشانیم
🔹
بیانیۀ ستادکل نیروهای مسلح و قرارگاه خاتم‌الانبیا به‌مناسبت هفتۀ دفاع مقدس: کشور با استفاده از تجارب ارزشمند هشت سال دفاع مقدس به‌سمت «ایران قوی» سوق داده شد و آمریکا و رژیم صهیونیستی، در جنگ دوازده ‌روزۀ تحمیلی و جنگ رمضان، در برابر ملت مبعوث و فرزندان دلاور و شجاع آنان در نیروهای مسلح، زانو بزنند و سر تعظیم فرود آورند.
🔹
نیروهای مسلح، معادلات امنیتی را به نفع امت اسلامی و ملت شریف ایران تغییر داده‌اند که نمونۀ بارز آن، به‌دست گرفتن مدیریت تنگه هرمز با ترتیبات ایرانی، فروریختن هیمنۀ پوشالی ارتش روبه زوال، هالیوودی و تروریستی آمریکای جنایتکار، و ذلیل کردن ارتش کودک‌کش صهیونیستی است.
🔹
نیروهای مسلح در برابر دشمن کوتاه نخواهند آمد و طعم تلخ شکست‌های بیشتر را بر متجاوزان و بدخواهان ملت ایران، به‌ویژه دشمنان آمریکایی، صهیونیستی و هم‌پیمانان آن‌ها، خواهند چشاند.
@Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/463356" target="_blank">📅 10:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463355">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14286db87.mp4?token=K-kbigXmRq44m_wcmR-7ienmG0Rl8cB5CwSQWSNNEFaCXPFeVhA2gPyCu8-W8-Y2onLxHQvkqD7ysHpUO96mhJoMsVoMXlePGZmr3-w-gAcpD3smq8xR7rCmLb9VN_jaFU9ulXaDG4iFR-4XnZILCPCPmHjQdY05iOiAg67ioapftR1UnZoGoAmn3xhVmR21zDMC1OzUtYAAYbH2batX3sjoSzIDrHbnlEMnwc8wJqF-AH2Kh821cw7N9hq1CSpTbQXcmANWw9GUUYkV2hXTeSyh9YuVmLZ5FINjYRoN43psC9j9hwbZSvo2cai2Xxk_ysA63rQskv9Qerhn5dv7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14286db87.mp4?token=K-kbigXmRq44m_wcmR-7ienmG0Rl8cB5CwSQWSNNEFaCXPFeVhA2gPyCu8-W8-Y2onLxHQvkqD7ysHpUO96mhJoMsVoMXlePGZmr3-w-gAcpD3smq8xR7rCmLb9VN_jaFU9ulXaDG4iFR-4XnZILCPCPmHjQdY05iOiAg67ioapftR1UnZoGoAmn3xhVmR21zDMC1OzUtYAAYbH2batX3sjoSzIDrHbnlEMnwc8wJqF-AH2Kh821cw7N9hq1CSpTbQXcmANWw9GUUYkV2hXTeSyh9YuVmLZ5FINjYRoN43psC9j9hwbZSvo2cai2Xxk_ysA63rQskv9Qerhn5dv7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زن ایرانی کافه‌نشین است یا میدان‌دار؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/463355" target="_blank">📅 10:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463354">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f510c530a0.mp4?token=e3oWytjq7S1HmR0BvBoDSEyKRvdKSccpY3XSr1SsKcNtVJg_D0TSSZOiX_sfrn1AKwLRrDX7_DBarOKdGcbJPEPmaUbfoHBnZDx_gVX4bQBoNVND1EE07b7NLLvbu1Pw7uOxZHH0H1lhDhmQj_XNiTbAlCHVoVvGQfVMlZeB1T27EQipAAHH471IIvJRHQezs6jrb_uKT3TtBZ1hgklWZNqSrtbpzKvSHvi5vueUUqj4Q2iQZ3Lo0l1ecFo2A4MMX4LaZAkbi8pAfTMPZE4s25ZcMX7u2KiBHChcBZwJUmP_IUDbrwYGrmFYgT1NvLVKfo1v_dv87ZhzskCF4jXLMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f510c530a0.mp4?token=e3oWytjq7S1HmR0BvBoDSEyKRvdKSccpY3XSr1SsKcNtVJg_D0TSSZOiX_sfrn1AKwLRrDX7_DBarOKdGcbJPEPmaUbfoHBnZDx_gVX4bQBoNVND1EE07b7NLLvbu1Pw7uOxZHH0H1lhDhmQj_XNiTbAlCHVoVvGQfVMlZeB1T27EQipAAHH471IIvJRHQezs6jrb_uKT3TtBZ1hgklWZNqSrtbpzKvSHvi5vueUUqj4Q2iQZ3Lo0l1ecFo2A4MMX4LaZAkbi8pAfTMPZE4s25ZcMX7u2KiBHChcBZwJUmP_IUDbrwYGrmFYgT1NvLVKfo1v_dv87ZhzskCF4jXLMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدیۀ ۱۰۰ هزار دلاری به مادر با مشت سنگین
🔹
شون شرف، فایتر فلسطینی‌تبار بعداز پیروزی بزرگ خود در مسابقات MMA گفت: تمام هدیۀ ۱۰۰ هزار دلاری را به مادرم هدیه می‌دهم.
🔹
این فایتر حریف آمریکایی خود را در ۱۲ ثانیه ناک‌اوت کرد تا سومین ناک‌اوت سریع تاریخ MMA را به نامش ثبت کند.
🔹
شرف متولد آمریکاست اما از حامیان مردم فلسطین و غزه به‌شمار می‌آید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/463354" target="_blank">📅 10:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463353">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qazeIJcZ0JpQwoVs4taNYsHDxOtvUI11as06Ht68WvlFck4nt3LopuyIfp4LjDYwFHszP7LeGoIvbSO1d_ZCEHEEjvCdrwBFV4WGtKM8yUoPFsk1rQjaUOgzrj1_bs4aKHvVRaEpCxSYrQG8TjdjPby60XJJWc6N4thaMw_BjD-IVH2ZHnvfrAas-8gAE0-tL_Eg98-ZZfUBGANHDWz5IxGw7hVTVyt-pwsO0zVh-5YoVfDxZakGy9gTchcCPSm62ghy6ZMI3WWQrlFHKe5oLnSazW13PkkOLakY5CHOVlTTJjds3YaGU-gLbzBUzXXJgvk-WVWKI3YTFV0hLKq9qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
برنز بسکتبال ایران با عبور از دیوار چین در ناگویا  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/463353" target="_blank">📅 10:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463352">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgsETQj2DWhwhR8c-k12h7XXAwdGf8DISsfbOFO1A57DxQBuzqruY9zzySg-uqEMHcZs8d8bWU9FhWQkQoPIDucDM4qpKoyl_ohMvBHZwbtB97dsX5NJZdEIOcabLVe5BmsaUT-tXB4Vo3aZ1fth2kB55KfEYRxq-7CtcJty2iS55h_DaugYJ0sxsIGvY2jA30yYwp3IG4da-P-Beo5-VvqsSq-xgnGpJbdz3znuC48v-eIa96fN5McPxB-Swh043jskWI0ml_n50rEkK7kubjMbsJC32xzJ5bsGpHuPaIByOVwUsmZDoXVXGRpCu9VY-SuGaKAole7s2dsoqMpUQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقدیر از همراه اول برای حمایت از پویش «فرشته‌های میناب»
🔹
آیین «روایت ایستادگی؛ مدارس ایران» امروز ۲۹ شهریورماه با هدف بهره‌برداری همزمان از مدارس آسیب‌دیده در جنگ تحمیلی سوم (رمضان) و تجلیل از مدافعان دانایی، با حضور وزیر آموزش و پرورش، رئیس سازمان نوسازی، توسعه و تجهیز مدارس و جمعی از مسئولان، خیرین و جهادگران در مدرسه علامه حلی برگزار شد.
🔹
در این رویداد، از همراه اول به‌پاس حمایت از پویش «فرشته‌های میناب» و مشارکت در بازسازی و حمایت از مدارس آسیب‌دیده، با اهدای لوح تقدیر و تندیس به‌صورت ویژه قدردانی شد.
🔹
همراه اول با اختصاص کد دستوری #۲۴* ، اجرای پویش در باشگاه مشتریان، ارسال پیامک هدفمند و اطلاع‌رسانی و تبلیغات در روبیکا، بخشی از ظرفیت‌های ارتباطی و رسانه‌ای خود را در اختیار این حرکت قرار داد.
🔹
این مشارکت، بخشی از اقدامات مستمر همراه اول در حوزه آموزش و مدرسه‌سازی برای ارتقای زیرساخت‌های آموزشی و حمایت از دانش‌آموزان مناطق مختلف کشور است.
http://mci.ir/-XK6OB6
@mcinews</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/463352" target="_blank">📅 10:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463351">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePZgriLSOLmPEkf7k_2Z_5uLnaP0htr2mHNySPjfIzckkzN-F39chHjzMNb-pQBFiVdEkvCcm4umk9qtbN4S0O2Y8-f4B-HQkm30ikpHGMPzP7PKz5_txlH8AGOUwuSz0yQ8YJiL1y1JhpBKOtWyRKsFrxASF6bu3hildw1mC56PNrWmueQKn6lznnziP3CWamnnNAsFtHJCeA6Ce7k1tCluxX-QzlYcdadgs8yeGaM1f9YKm5dm3iHF77Joa0MF2E5_b8MJ_SKIWSF4BAMtx4XjPJr3xdgBun2PMGVf_xCsMbd1PO6gNtcKxpl1uQj9zhTqVHo381c31kSx18sYkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنگ‌تمام صندوق سرمایه گذاری زیست فناوری برای دانش‌بنیان‌ها/ روایتی از همراهی تا اوج
صندوق حمایت از سرمایه گذاری زیست فناوری
، وابسته به معاونت علمی، فناوری و اقتصاد دانش‌بنیان ریاست‌جمهوری، با ارائه کامل‌ترین زنجیره خدمات مالی و اعتباری از سرمایه‌گذاری خطرپذیر و اعطای تسهیلات تا صدور ضمانت‌نامه به پناهگاهی مطمئن برای شرکت‌های فناور تبدیل شده است.
رسالت بی‌بدیل این صندوق در ایثار مالی و حمایت خالصانه تجلی یافته است؛ مجموعه‌ای که با پذیرش ریسک طرح‌های نوآورانه، شرکت‌ها را به مرحله سوددهی و تجاری‌سازی می‌رساند و سپس بدون چشم‌داشت، سهم‌خواهی یا طلب سود، کنار می‌کشد تا تمامی دستاوردها و منافع تجاری در اختیار خود فناوران قرار گیرد.
🌐
درگاه ارتباطی:
www.biotechfund.ir</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/463351" target="_blank">📅 10:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463350">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/463350" target="_blank">📅 10:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463349">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6e999557.mp4?token=KnVfQEebjOHNQiaF4HDqHmx8DKZQDjZL6z5MaYteW62v_IMIdn_uzgCPCPik7HjNOgyDgFdVj3rMD1fKCT66yeUcJ9RBRdYLiwLvbn97CsOmxVyvzmvaU4lu-PwiloK7PQvr24tSC0tKOk7MW9qvZOLCH2qloxceBM4pJewMSaABObtHBaDt-Fqsa3GH-K9q2PQm3H0grhW15wqTZEs6cuVOJaerNcU4lxwbQlBfthQlLQgDZ1NwEdAo0s9Qk4B7D3ti6NJHeRSW6UfQefbOa_Vo7CmxKE0Q5kbM0pXiw1GpzYuT8C5jJJxh6j0iuA38s8gsiJFSEopsd6wxr6l3WYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6e999557.mp4?token=KnVfQEebjOHNQiaF4HDqHmx8DKZQDjZL6z5MaYteW62v_IMIdn_uzgCPCPik7HjNOgyDgFdVj3rMD1fKCT66yeUcJ9RBRdYLiwLvbn97CsOmxVyvzmvaU4lu-PwiloK7PQvr24tSC0tKOk7MW9qvZOLCH2qloxceBM4pJewMSaABObtHBaDt-Fqsa3GH-K9q2PQm3H0grhW15wqTZEs6cuVOJaerNcU4lxwbQlBfthQlLQgDZ1NwEdAo0s9Qk4B7D3ti6NJHeRSW6UfQefbOa_Vo7CmxKE0Q5kbM0pXiw1GpzYuT8C5jJJxh6j0iuA38s8gsiJFSEopsd6wxr6l3WYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ صدور کیفرخواست در پروندهٔ شهادت رهبر انقلاب و اعضای خانوادهٔ ایشان و اقدام تروریستی منتهی به شهادت دانش‌آموزان مدرسهٔ میناب
🔹
دادستان تهران: کیفرخواست پروندهٔ اقدام تروریستی منتهی به شهادت رهبر انقلاب و ۴ نفر از اعضای خانوادهٔ ایشان با تکمیل تحقیقات مقدماتی…</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/463349" target="_blank">📅 09:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463348">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPvfgtdWVqJIlmrng4D_Wd0eY7uEAE-qp6rAeM_Tlf6J9ZvumuRwtdXWMKmHcwk53pFijSmjTXj-iJ_lG3KQhzJ5MwkbXJrWxYqSWcs3VhXdIQO2p5WQ-fRSk5h6cPq4NC5hMlhwZ1VRu__Szagr9nBPFiuvZruQ1LiVs0ItHf2CZjFkF55ZocsNw_DnjSg9BSSPOTDmyZ3a6CTjFW7C_1BBCcAQ81oc3FTCaZvphVn_RsVgX5BYERUyHLPeBTjupyDg3m9XC6L2dt-1hLWHT8c0ks7luYqyjgfKtnBe_j24DFAMAF3-Pg00N5G2dHcTLBEgbYPy1jA3c9-RxA286Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/463348" target="_blank">📅 09:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463347">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebef596c4.mp4?token=m2eU71_JNAbZrgIOtPYLLJdtE7hqRbRmBm1haEjqJOu-bf550csH-v6bo9_10QtkdvRIB14uZ9c7fiSPAytqUGZHYwjVvcK5L9o3p4DHcNat76EVoTQdBaRWnCbft_WOKMjglRp4KlUOmVvIqHFSusJDzCkbAi6Fg27UGBMe7Z2YdxsB-YNigSmNPftg92abilYEvSpshMMpZTPhx0-xk_RvEazHhbIgKw_EfVrorRRhjuSXQ2nXbFNwR2-pqixl_7MhoNns3V4E0WdzOubSHuB4RqqFf0oRFyYZbg6RSNUMMaxUzOujA06BrhJ8lQ-N3RQyl7CHkXmmUFVBy8IT4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebef596c4.mp4?token=m2eU71_JNAbZrgIOtPYLLJdtE7hqRbRmBm1haEjqJOu-bf550csH-v6bo9_10QtkdvRIB14uZ9c7fiSPAytqUGZHYwjVvcK5L9o3p4DHcNat76EVoTQdBaRWnCbft_WOKMjglRp4KlUOmVvIqHFSusJDzCkbAi6Fg27UGBMe7Z2YdxsB-YNigSmNPftg92abilYEvSpshMMpZTPhx0-xk_RvEazHhbIgKw_EfVrorRRhjuSXQ2nXbFNwR2-pqixl_7MhoNns3V4E0WdzOubSHuB4RqqFf0oRFyYZbg6RSNUMMaxUzOujA06BrhJ8lQ-N3RQyl7CHkXmmUFVBy8IT4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: آدم، مفت به جایی نمی‌رسد؛ باید تلاش کرد
🔹
من که اینجا ایستاده‌ام دلم می‌خواهد به همۀ مردم کشورم کمک کنم.
🔹
ما می‌توانیم علم و مهارت پیدا کنیم و مشکلات مردم، خانواده، شهر و کشور و حتی مشکلات دنیا را حل کنیم.
🔹
ما به شما دانش‌آموزان اعتماد داریم و…</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/463347" target="_blank">📅 09:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463346">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2379983810.mp4?token=A-cUxhu43FQqran_T0r_-hCRVsbC4F8DrobnpvuyFK-eR16rUCd_ef9WEe8rxIcNqyMQq45zX_XqB-l2IZQJ9odCVROFzisCFbYs3OxKCBjOMIKsB6DUkfZLbhMff2Ihba0BALfX1t3af5TxV-_pemnktb8AXE0ju1RhZmpPbtxbyRIwlqzv4cvfO9z0hxRKFtBMuk4dowaifHN2YZ5lRPgAbZBJy6LfXNZC4L9gl7Ixzhj_10CB6Fb8R1HKoF-3hHK1n6huqLJbvd3qKyRjzDNR1ml6wPPKSc6OA95lSUxLQmBXhAKwYgxv2U1fU4izBbymnUb_FBchDIMTijanuhxkfK8mPrFujQudKQTrrP_fGUbPTZXvPX3X7q_lffQKKposduOK2_y4ZipGZLeVrCWljy-WGSjcDNg1rvlRh6WxnunGDk2UlwlNZ1sCFN4oM8uwaQ7Csa5QIrvDaugSPEYW7LCaewcYUMitmuei7DiA-7Yo0kw73eqKJD0IMJjtLyBITWZ56T4U0WbNibS76zCHGYqSZiWJEZd_Jp0iz9GBUERL6TTDBmwE-ZCHSMRnMPbSlkLhbgUf5HNUK-Ln_lTxXnmYcv4EpZOQrgQyzw0XejxcPSo6tZjiwKlfZwWbPL3xzzP9e1XqbEDwiiPD7mYsYOiJ1Anh4Cehy4BswwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2379983810.mp4?token=A-cUxhu43FQqran_T0r_-hCRVsbC4F8DrobnpvuyFK-eR16rUCd_ef9WEe8rxIcNqyMQq45zX_XqB-l2IZQJ9odCVROFzisCFbYs3OxKCBjOMIKsB6DUkfZLbhMff2Ihba0BALfX1t3af5TxV-_pemnktb8AXE0ju1RhZmpPbtxbyRIwlqzv4cvfO9z0hxRKFtBMuk4dowaifHN2YZ5lRPgAbZBJy6LfXNZC4L9gl7Ixzhj_10CB6Fb8R1HKoF-3hHK1n6huqLJbvd3qKyRjzDNR1ml6wPPKSc6OA95lSUxLQmBXhAKwYgxv2U1fU4izBbymnUb_FBchDIMTijanuhxkfK8mPrFujQudKQTrrP_fGUbPTZXvPX3X7q_lffQKKposduOK2_y4ZipGZLeVrCWljy-WGSjcDNg1rvlRh6WxnunGDk2UlwlNZ1sCFN4oM8uwaQ7Csa5QIrvDaugSPEYW7LCaewcYUMitmuei7DiA-7Yo0kw73eqKJD0IMJjtLyBITWZ56T4U0WbNibS76zCHGYqSZiWJEZd_Jp0iz9GBUERL6TTDBmwE-ZCHSMRnMPbSlkLhbgUf5HNUK-Ln_lTxXnmYcv4EpZOQrgQyzw0XejxcPSo6tZjiwKlfZwWbPL3xzzP9e1XqbEDwiiPD7mYsYOiJ1Anh4Cehy4BswwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصادف کشتی فله‌بر پانامایی با قایق چینی در تنگه سنگاپور
🔹
یک کشتی فله‌بر با پرچم پاناما در نزدیکی تنگهٔ سنگاپور با یک قایق ماهیگیری چینی برخورد کرد. داده‌های ردیابی نشان می‌دهد که کشتی ماهیگیری شناور مانده و به‌نظر می‌رسد که به اسکله‌ای در همان نزدیکی رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/463346" target="_blank">📅 09:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463345">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0ffc79845.mp4?token=FXIVxjd_r_d5nV06aQ7_3-Pe5p9xLUiZUJJ_fQotadvFq12Pu0Wy1HPIZtXHlzjw5BSMktHDjcp4y5UMcF15T20BBaPQLiQIvrYZti21Q4nyfSFqd0SuivR2kY6Mo5VdUIG6wK5QeQYxaGtTBBGJU3PtYVVMugfZul1iLcPwKQ2ET6JKkdr0ES0UNdR56NPEr8SR9rnb9IHWYNanl6GAmbU0-hAfGsRuxwDhReCS08ilCqoXvdhu9uNkQzBZ56qU_S9MA45PjhwzPs7h-yiCB3jkoG6Scap-felWObpXfdw_3p6iFtPyOVXD56FrUDPt5Ol-uo3-Ts00m_ZXFCirkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0ffc79845.mp4?token=FXIVxjd_r_d5nV06aQ7_3-Pe5p9xLUiZUJJ_fQotadvFq12Pu0Wy1HPIZtXHlzjw5BSMktHDjcp4y5UMcF15T20BBaPQLiQIvrYZti21Q4nyfSFqd0SuivR2kY6Mo5VdUIG6wK5QeQYxaGtTBBGJU3PtYVVMugfZul1iLcPwKQ2ET6JKkdr0ES0UNdR56NPEr8SR9rnb9IHWYNanl6GAmbU0-hAfGsRuxwDhReCS08ilCqoXvdhu9uNkQzBZ56qU_S9MA45PjhwzPs7h-yiCB3jkoG6Scap-felWObpXfdw_3p6iFtPyOVXD56FrUDPt5Ol-uo3-Ts00m_ZXFCirkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان خطاب به دانش‌آموزان: بچه‌ها سلام! می‌دانید که شما گوهر هستید!
🔹
می‌دانید من از یک خانوادۀ معمولی به اینجا رسیدم.
🔹
شما اگر ذهن‌‎ و فکرتان این باشد که بهترین شوید حتما می‌شوید. ما تلاش خواهیم کرد که شما بهترین شوید.  @Farsna</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/463345" target="_blank">📅 09:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463344">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cf94be4a9.mp4?token=ctnie4fkPuj5uxhpMJQHmk72GoH2KMQHR0etXrJVeyke0dhxOcwzsGQ2S2kWVhlqPTbjJxeg4RfXTIybUbstz7yq1Q5X1wLxQCqd1h8vErV9Koo-BAEam-pZGoSwexp8REs00UQfuZQ7PCClSC4WD7-PtclAJDQrAX0G2u6JE1bDTjcbZUbD86Vhv5-CNjTyvPngB3hWEyjgZvDL_7Rxg2w1u-FTIVvONirJXE01JJt663QfOuc-9G5mXVb8HL3nQyzdux56P1qH6WgFB4vEsa6eqrmxxwjCMCM5iB6ssvbvd6Z0Z5ibq1iDNSb5IWD_2S0q_1aR7lct51QtR4qBxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cf94be4a9.mp4?token=ctnie4fkPuj5uxhpMJQHmk72GoH2KMQHR0etXrJVeyke0dhxOcwzsGQ2S2kWVhlqPTbjJxeg4RfXTIybUbstz7yq1Q5X1wLxQCqd1h8vErV9Koo-BAEam-pZGoSwexp8REs00UQfuZQ7PCClSC4WD7-PtclAJDQrAX0G2u6JE1bDTjcbZUbD86Vhv5-CNjTyvPngB3hWEyjgZvDL_7Rxg2w1u-FTIVvONirJXE01JJt663QfOuc-9G5mXVb8HL3nQyzdux56P1qH6WgFB4vEsa6eqrmxxwjCMCM5iB6ssvbvd6Z0Z5ibq1iDNSb5IWD_2S0q_1aR7lct51QtR4qBxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ نواخته‌شدن زنگ آغاز سال تحصیلی جدید توسط رئیس‌جمهور  @Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/463344" target="_blank">📅 09:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463342">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGLnoCYalMGP11VIAxReKFZ9b9-DgbASiS9lFzIOZUZP0dnxNrkU3n5FiAf2b6UWNSGk5uQGXkOpI47a2ZQzvC7WqAOvh2DKR59sLeAi_TQ9-kDHSUrAmNONI6nKTLD61ugW8-MubBycI2gh54VDv05FNwjr9Zhg9iNwbvxUyX2rubnxRQxPBL7mMkT-0oO98KQ67A9guvyRuP8IXijSHM1hDgjAc8DKl-64MFMz8OxpENgTDT7Y9aF5Y9WZ0FsVDxoJ5szEIfoAWYjNRGb58KmDVT0VpM_HEX6HPw9bKAInK3CdRqqEJSeEFfjUMGhX_HgL7AcfxladfWNFgclzEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف ارتحال آیت‌الله شبیری‌زنجانی را تسلیت گفت
🔹
رحلت عالم ربانی، فقیه ژرف‌اندیش و مرجع عالی‌قدر جهان تشیع، حضرت آیت‌الله العظمی حاج سیدموسی شبیری زنجانی، ضایعه‌ای سنگین و جبران‌ناپذیر برای حوزه‌های علمیه، جامعه روحانیت و عموم ارادتمندان مکتب اهل‌بیت عصمت…</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/463342" target="_blank">📅 08:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463341">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌ سخنگوی سپاه: یمن، لبنان و حزب‌الله نیروی نیابتی ایران نیستند
🔹
برخی تصور می‌کنند مثلاً یمن، لبنان، و... نیروهای نیابتی ما هستند.
🔹
آن‌ها خودشان نسبت به تمامیت ارضی کشور خودشان عِرق دارند، خودشان سیاست دارند، خودشان تشخیص دارند، خودشان تصمیم می‌گیرند. گروه‌های…</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/463341" target="_blank">📅 08:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463340">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d69d1407c5.mp4?token=ILDFsn0Id-KRIefvlszg3g7GNtZu5d_o7B4B71CRspZ7dupAcr6sG9iN5Seb-MJ2N4hWqrwX8G5Gq7gGw-D5mFu8Q2QGtVR96-3Lxmsq1PIKus7rtf0duL5djEMw6hzFSPApKz5SCAgWnDbjT1U17dSmwvLCv9zO0epZpupmCRl3GvpPBBn0DMplKaJKZHBrrZHeJPloGTui604RrANyEWJgQ0iGFoXGnC3VIxoA7JjwDBpKcGaTDMr6avfd0G-IWcipHwTViZPFt_AuDdpD50GX3zGQDUyXP3ugn5wvGqOH10QjenluKlIZtYmqXQ-NLvh7nECr48ZlsQ9MrW9QhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d69d1407c5.mp4?token=ILDFsn0Id-KRIefvlszg3g7GNtZu5d_o7B4B71CRspZ7dupAcr6sG9iN5Seb-MJ2N4hWqrwX8G5Gq7gGw-D5mFu8Q2QGtVR96-3Lxmsq1PIKus7rtf0duL5djEMw6hzFSPApKz5SCAgWnDbjT1U17dSmwvLCv9zO0epZpupmCRl3GvpPBBn0DMplKaJKZHBrrZHeJPloGTui604RrANyEWJgQ0iGFoXGnC3VIxoA7JjwDBpKcGaTDMr6avfd0G-IWcipHwTViZPFt_AuDdpD50GX3zGQDUyXP3ugn5wvGqOH10QjenluKlIZtYmqXQ-NLvh7nECr48ZlsQ9MrW9QhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پزشکیان در آیین آغاز سال تحصیلی جدید   @Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/463340" target="_blank">📅 08:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463339">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkeL9DsA_JzR4TXlwNkgkKkXxQxyrmJYCNuVdLlragI5n18uvCRLnzMsqp5K1-Urq8mX6AaEqTZd2jxS06VuN0nWXz1481F8ClXC1SyiJEp2TdsexDd6FipCrG8wQ66MVwrnHX45elTP62Zl2RkpFMtW-WOnx2EecOq3QG1w1B8Cb0z1f823NbMGVv6cuJAoj2KnrKMA4C0h7wp6YiFxhd6oRoeYGsvpP5s23D4IFKdqrwrUiD52jhhCECtvQO-koYwCeGI1i3cSEk_02_Z0Yy1u0ujdm9ri8zwk33Z8BP5Ma41JF9fI6qhR7Li0gWSig8aZkzAAUnweBxgmUSz_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌آیت‌الله شبیری زنجانی دار فانی را وداع گفت
🔹
دفتر آیت‌الله شبیری زنجانی اعلام کرد: روح مطهر فقیه اهل‌بیت عصمت و طهارت(ع) ومرجع عالی‌قدر جهان تشیع، آیت‌الله العظمی شبیری زنجانی به لقاءالله پیوست.
🔹
جزئیات مراسم تشییع و تدفین پیکر ایشان، متعاقبا اعلام می‌شود.…</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/463339" target="_blank">📅 08:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463338">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌ سخنگوی سپاه: اگر تهاجم جدیدی صورت بگیرد، قطعاً سلاح و جغرافیای جنگ را تغییر خواهیم داد
🔹
اگر تهاجم جدیدی صورت بگیرد قطعاً تغییرات قابل‌توجهی در دفاع ما و هجوم متقابل ما وجود خواهد داشت.
🔹
آن تغییرات، تغییر در جغرافیای جنگ، تغییر در سلاح‌ها و تجهیزات جنگی…</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/463338" target="_blank">📅 08:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463336">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b04ff241.mp4?token=QnJT91xQCowlxHCD2MQapL7yWVqX5VRIWEFhBbwFwvBtDyv8wXyNCXZzNt32QizC_u-qnFfoSNfpPVuSZ7Dn3Q2Ndu5bjCbnfX-K8CboIV__uKwKde2IquOFcDb9ehG7yS-4w6Qqh0BS4hafshwokr53gE6PU9oIaMRfoxZGcUce-gOXYnDieveMMbj--2_Aenu-XB-dvd_vVmTuGlz15thefbU_TlijQ8ZfYLVgrzunuXhJkzwU1UFHDlLJxL1Hzzg4_NYarS-OboZJkD0_UFaz2Kbo_x_5igklYuytRbX2EZSHPEPAItosb3MlO2ddjhkaeedUb_Zycf8s9r3s6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b04ff241.mp4?token=QnJT91xQCowlxHCD2MQapL7yWVqX5VRIWEFhBbwFwvBtDyv8wXyNCXZzNt32QizC_u-qnFfoSNfpPVuSZ7Dn3Q2Ndu5bjCbnfX-K8CboIV__uKwKde2IquOFcDb9ehG7yS-4w6Qqh0BS4hafshwokr53gE6PU9oIaMRfoxZGcUce-gOXYnDieveMMbj--2_Aenu-XB-dvd_vVmTuGlz15thefbU_TlijQ8ZfYLVgrzunuXhJkzwU1UFHDlLJxL1Hzzg4_NYarS-OboZJkD0_UFaz2Kbo_x_5igklYuytRbX2EZSHPEPAItosb3MlO2ddjhkaeedUb_Zycf8s9r3s6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پزشکیان در آیین آغاز سال تحصیلی جدید
@Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/463336" target="_blank">📅 08:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463335">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‌ سخنگوی سپاه: سپاه وارد عرصۀ دیپلماسی نمی‌شود
🔹
سپاه پاسداران نه حالا و نه هیچ‌وقت دیگر هیچ ارتباط رسمی و غیررسمی با ایالات متحده نداشته و اصلاً ورود به دیپلماسی هم پیدا نمی‌کند.
🔹
سپاه بازوی دفاعی و نظامی ایران و اسلام است، و در وظیفۀ خودش کاملاً مجهز، مجرب…</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/463335" target="_blank">📅 08:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463334">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b690fb886e.mp4?token=iF--4tWJlbuzF30oufxMJtHCrCty-iDuCCMIvtEgdkbXRmqDEigVUY3eMT-IolPrPdUbxe9c7nkiNeC9Gt3SI8OsaX3Ec5XKWImSiyAqWslT04zHxL6XzE8FzFdjwoXnE_NDU2PkF6jlRk8byKCQODqmvkR9aS79y__z3-E4SpDNLQZ4XkaPUtKbK-EfUO9hS04j4CWO6SwtVkp94EkLk8hLminVmRnb3Rgt3f5OuVuGUsQEFSFQ4iCu__u1c04uEWd90JxO-v0N37i_A1D6b-HERrW6QmtNaQDcQ-N1qR4bZHXvu977KgnZrWc4p_NQCkrrnv4qx53zswIIv5a5Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b690fb886e.mp4?token=iF--4tWJlbuzF30oufxMJtHCrCty-iDuCCMIvtEgdkbXRmqDEigVUY3eMT-IolPrPdUbxe9c7nkiNeC9Gt3SI8OsaX3Ec5XKWImSiyAqWslT04zHxL6XzE8FzFdjwoXnE_NDU2PkF6jlRk8byKCQODqmvkR9aS79y__z3-E4SpDNLQZ4XkaPUtKbK-EfUO9hS04j4CWO6SwtVkp94EkLk8hLminVmRnb3Rgt3f5OuVuGUsQEFSFQ4iCu__u1c04uEWd90JxO-v0N37i_A1D6b-HERrW6QmtNaQDcQ-N1qR4bZHXvu977KgnZrWc4p_NQCkrrnv4qx53zswIIv5a5Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نشستن، سیگار جدید است!
@Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/463334" target="_blank">📅 08:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463333">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‌ سخنگوی سپاه: برای یک جنگ طولانی آماده‌ایم
🔹
از نظر ما جنگ همان جنگ است، مقاطع مختلفی دارد، ولی جنگ همان جنگ است و جنگ هم تمام نشده و ادامه دارد.
🔹
سپاه پاسداران از قبل آماده بوده و الان آماده‌تر شده برای یک جنگ طولانی‌مدت.  @Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/463333" target="_blank">📅 08:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463332">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌ سخنگوی سپاه: امروز ما هستیم که نظام جدید منطقه را مشخص می‌کنیم، نه آمریکا
🔹
آمریکا به خاطر بمباران مدرسۀ  میناب تمام حیثیت خودش را باخت؛ به خاطر بمباران و آزمایش سلاح جدید در لامرد، دنیا را از دست داد. به خاطر بمباران مراسم عروسی، کاپ اخلاقش را نابود کرد.…</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/463332" target="_blank">📅 08:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463331">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌‌ سخنگوی سپاه: تکنولوژی‌های آمریکا قادر به دفاع از خودش هم نیست، چه برسد به دفاع از هم‌پیمانانش
🔹
برخی تصور می‌کردند آمریکا از یک تکنولوژی بسیار بالا در حوزۀ جنگ‌افزارهای تهاجمی و دفاعی برخوردار است که این تکنولوژی غیرقابل‌دستیابی است.
🔹
اما در این جنگ همۀ…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/463331" target="_blank">📅 08:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463330">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjW2WHEGAaV9JgmzKmMV8I6XE1WEJsWEjMZO8KZ7l0r-nct23GaCEWKgwcC6i2470IuoFnPUlCyIAFlDKog9ZerEGKsgVcY5Oer6yfb3VBjuUeBtDQLaYVSrvLtJpX6bCm4v3GmtwiiZbjguG2hDjI0YuML3LKoYiyZzszo2ojINp8Tg0t8ZonVM281BxPAJQrKhQjb8eyPwUT-Z-qvbtggnJLqg2cSUmTJyNY7ggadZ5AACz9VLze6j-aRvN_HcTEOnCfLWN0zqDDFHhpd3Kwt_hepsmItH2Bo_0gY8k-6G32sIkSlABOR1biVQl04abX1PlSaPRyKfP6zwAH8S5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌آیت‌الله شبیری زنجانی دار فانی را وداع گفت
🔹
دفتر آیت‌الله شبیری زنجانی اعلام کرد: روح مطهر فقیه اهل‌بیت عصمت و طهارت(ع) ومرجع عالی‌قدر جهان تشیع، آیت‌الله العظمی شبیری زنجانی به لقاءالله پیوست.
🔹
جزئیات مراسم تشییع و تدفین پیکر ایشان، متعاقبا اعلام می‌شود.…</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/463330" target="_blank">📅 08:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463329">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌ سخنگوی سپاه: برخلاف تصویرسازی‌ها مراکز اطلاعاتی واشنگتن قابل‌دسترسی بود و مورد حملۀ ایران قرار گرفت
🔹
این‌گونه تصویرسازی شده بود که آمریکا یک نظام اطلاعاتی غیرقابل‌دسترس دارد.
🔹
اما وقتی این مراکز در حاشیۀ خلیج‌فارس و در شمال عراق مورد اصابت موشک‌های ایران…</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/463329" target="_blank">📅 08:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463328">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دیشب که خواب بودید چه گذشت؟
🔸
آیت‌الله شبیری زنجانی، مرجع عالی‌قدر جهان تشیع دار فانی را وداع گفت.
🔹
سازمان هواپیمایی کشور، شایعۀ توقف پروازهای ایران و عراق را تکذیب کرد.
🔸
قیمت نفت در آغاز معاملات هفتۀ جدید میلادی صعودی شد، و به بالای ۱۰۴ دلار رسید.
🔹
ایران طلسم ۱۶سالۀ فینال شنای آسیا را شکست و هومر عباسی به فینال بازی‌های آسیایی ناگویا صعود کرد. امیر مطاعی نیز در مرحلۀ مقدماتی ۱۰۰ متر قورباغۀ مردان، به فینال صعود کرد.
🔸
یک پهپاد MQ-1 دیگر ارتش تروریست آمریکا در آسمان تنگۀ هرمز منهدم شد.
🔹
تیم ملی کبدی بانوان در اولین دیدار خود مقابل ژاپن، با نتیجۀ ۶۳ - ۲۰ به پیروزی رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/463328" target="_blank">📅 08:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463327">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‌ سخنگوی سپاه: امروز پایگاه‌های آمریکا دیگر حتی توان محافظت از خودشان را هم ندارند
🔹
آمریکا طی ده‌ها سال، در منطقه، در کشورهای حاشیۀ خلیج‌فارس، کشورهای شرق و غرب ایران، پایگاه‌های متعددی ایجاد کرد تا بتواند در این منطقه سلطه‌گری کند.
🔹
اما تمام این پایگاه‌ها…</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/463327" target="_blank">📅 08:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463326">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سخنگوی سپاه: آمریکا شجاعت اعتراف به شکست در جنگ را ندارد
🔹
سردار محبی: آمریکا در این جنگ شکست خورده و شکستش هم یک شکست تاریخی و مفتضحانه است، اما شجاعت اعتراف این شکست و پذیرش این شکست را ندارد.
🔹
شکست ایالات متحده و رژیم صهیونیستی شکستی است که همۀ آگاهان…</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/463326" target="_blank">📅 08:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463325">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سخنگوی سپاه: آمریکا شجاعت اعتراف به شکست در جنگ را ندارد
🔹
سردار محبی: آمریکا در این جنگ شکست خورده و شکستش هم یک شکست تاریخی و مفتضحانه است، اما شجاعت اعتراف این شکست و پذیرش این شکست را ندارد.
🔹
شکست ایالات متحده و رژیم صهیونیستی شکستی است که همۀ آگاهان نظامی و سیاسی، حتی در خود آمریکا، هم به این اعتراف دارند و می‌توانند با کمترین توجه این شکست را خوب ببینند، لمس کنند و حس کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/463325" target="_blank">📅 07:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463324">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">بازی‌های آسیایی ناگویا | برتری کبدی بانوان مقابل میزبان
🔹
تیم ملی کبدی بانوان در اولین دیدار خود مقابل ژاپن با نتیجه قاطع ۶۳ - ۲۰ به پیروزی رسید.
🔹
ملی‌پوشان کشورمان روزهای سه‌شنبه و چهارشنبه به ترتیب رو در روی بنگلادش و هند قرار می‌گیرند.
@Sportfars</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/463324" target="_blank">📅 07:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463323">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
انهدام یک پهپاد MQ-1 در آسمان تنگۀ هرمز
🔹
سپاه: لحظاتی قبل یک پهپاد MQ-1 دیگر ارتش تروریستی آمریکا توسط آتش پدافند پیشرفتۀ هوافضای سپاه در آسمان تنگۀ هرمز رهگیری و منهدم شد.
🔸
این مدل از پهپاد آمریکایی، چندسالی است از نیروی دریایی و هوایی ارتش تروریست این کشور کنار گذاشته شده و جای خود را به MQ-9 داده، اما حالا با توجه به انهدام بخش اعظمی از MQ-9ها، آمریکا دوباره مجبور به استفاده از این پهپاد شده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/463323" target="_blank">📅 07:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463321">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YB-i5WWd91XWjkmO_m8jADJj6BYI1hLxoqJw7uckE0qYFOyM0XBSpML8Dx8BYpfaCYNjAGvWfJLmiXb01HStNZGL7SOZzj6tkoQEQjn4kyXAR14YFNyRzF7m6Mw0hhWxQMBrTa9b0-LweGRF1dCPnG5vJtDP2dRA3APlFPTFv7Jj2U1EGBJLSTSKKKqryhnTasAiSVcItmR_54x8wTFqxvRm5CPpEkg74zqJZ99kCXoSm3BHtYO82CfLJqKcdcCT4oeCX6oVjW6tGA-StDjvxi3vPMVD2wORq1uzE8ZY0VrtMBIzEo8pme1TD4uiNQsFWYWBiWxXOP9wND3xHKrkQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFxMfcSloa28VmqR-1lDXTV_aMHBtDJSg-yfh_Nm2J7dXxXhq2dUdlrKHhb-fj9pUdyuE-gfhERC2Pr2jsDMDB0T8C4t0qkrhj0OwINTG-Ydb6VFReO01GIS2kpDmNHzjLjDRQqt6kgfQCE2wyn_yFNj9bpMFBbZGaiT2_-dI7CXfTiWrLgrWyQqLR0mH66Jh8D1h1AjiTMwJdzxjJUHmMjzW8H-fH5dDnF_sG9DlciVbcgmLDkWQjLQ6UXxHwLlZkDpKbcEo8PnaY7Hf1aqBDxQ627P4Cw8otHpMweyXxT5jEjbeZu4IA0h-DdYDsNy5TEepUh5HFJ68TdkFTGibw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت امور خارجه جنایات ضد بشری رژیم صهیونیستی علیه فلسطینیان را محکوم کرد
🔹
رژیم اشغالگر صهیونیستی که طی ۳ سال گذشته با برخورداری از حمایت همه‌جانبۀ تسلیحاتی مالی و سیاسی-تبلیغاتی آمریکا و برخی از کشورهای مدعی حقوق انسان، مرتکب یکی از بزرگترین نسل‌کشی‌های تاریخ جهان در غزه شده است، همزمان به شنیع‌ترین شیوه‌ها از جمله ترور و شکنجه نظام‌مند و گستردۀ فلسطینیان در کرانۀ باختری و غزه برای پیشبرد طرح اهریمنی «محو استعماری فلسطین» متوسل شده است.
🔹
گروگانگیری زنان و کودکان فلسطینی که تعداد آن‌ها به بیش از ده‌هزار نفر رسیده است و شکنجۀ آن‌ها در زندانهای مخوف که منجر به شهادت ده‌ها نفر از آن‌ها و قطع عضو و معلولیت صدها نفر دیگر شده است، بدون تردید مصداق جنایت جنگی و جنایت علیه بشریت است.
🔸
جنایات بی‌سابقۀ رژیم صهیونیستی بدون تردید شدیدترین ضربات را به اعتبار و جایگاه سازمان ملل متحد و حقوق بین‌الملل وارد کرده است.
🔸
این واقعیت که رژیم صهیونیستی در صدر ناقضان قطعنامه‌های سازمان ملل متحد است و بیشترین تعداد وتوی قطعنامه‌های شورای امنیت، با هدف ممانعت از مقابله با قانون‌شکنی و جنایات اسرائیل صورت گرفته، به‌تنهایی گویای نقش این رژیم در فرسایش اعتبار و جایگاه سازمان ملل است.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/463321" target="_blank">📅 07:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463320">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPPSp3OpJDgjW4zR8mCoSyNmIa-dtf7PNIkKKMy1Sbf_C3ezX9rsSlRwKuDZcJO2b3WUfR6GMJ6tsqS3DTnOo-A79jusmQW-QSVoGi_iAeqa7sr-UXG1P8Tk8wf2l9lL72VbZW5ZaWSZVOoiO5TNP5N5qZa5z6QYg5aFM1Cqto9RfWYfHu7lOXOBh6IWudj32p7dZxblioCf0Im0Pkr84lmj_7OmWrEeobAzUXeKRamO1yjSYSUxK1qNKr7nR0-pqNuEFw7W0rS7KKu0yo0tPHty5bf4bj1C49cpyNBede-Wwl3rnoBmZZhx5EqqmwtzTjiYYjzpyIqBEutNaSFJOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درآمد نفتی ایران به ۱۶ میلیارد دلار رسید؛ دست دولت برای حمایت‌های معیشتی بازتر شد
🔹
اطلاعات کسب شده نشان می‌دهد درآمد نفتی ایران در ۶ ماهۀ نخست امسال به حدود ۱۶ میلیارد دلار رسیده است.
🔹
در ۵ ماه ابتدایی سال بیش از ۱۳ میلیارد دلار از محل فروش نفت وارد کشور شده بود. حالا با احتساب درآمد وصولی شهریورماه، مجموع درآمد نفتی کشور در نیمۀ نخست سال از ۱۶ میلیارد دلار عبور کرده است.
🔸
درواقع این درآمد دست دولت را برای تقویت حمایت‌های معیشتی از جمله افزایش مبلغ کالابرگ بازتر کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/463320" target="_blank">📅 07:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463319">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">عامل حمله با قمه به مأمور پلیس‌راهور در شهرکرد دستگیر شد
🔹
دادستانی چهارمحال‌وبختیاری: عامل حمله به مأمور پلیس راهور در شهرکرد، پس از صدور دستور قضایی و با اقدام مأموران انتظامی شناسایی و دستگیر شد.
🔹
برای فرد مهاجم پروندۀ کیفری تشکیل شده و به‌صورت ویژه مورد رسیدگی قرار خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/463319" target="_blank">📅 06:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463317">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4024a404b.mp4?token=a3-qQyfesQV5ZfuAGGKAzq9RIbhMcqO-oqUjSJnS4o38_WEBDWUMqTKrrPmS3in7nZp90ninHh9SDCob5yzNkyyHC3gUjDzUWFvaOb4WWjLComXm0BSLs7w6TLcenjejHXTITHLKs6tY0zGVF3CvxtEojwXp5brA6O052WnEQa_0SCH37n4AmT6MITzbihBdDgUei6GC6Oysm3EDgWTzZWrXkQWVylHGneVe3cra9G_k_V-XoBFyDAMUQEkcdiKbfgn8zoxPzmFQ0uWKtv1Vj76JbHqH4cYOSLlYa8kNl7X2o4rcKS5IvDSHkdUid9-RGfrWSpEzBs5ENZACEUcukQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4024a404b.mp4?token=a3-qQyfesQV5ZfuAGGKAzq9RIbhMcqO-oqUjSJnS4o38_WEBDWUMqTKrrPmS3in7nZp90ninHh9SDCob5yzNkyyHC3gUjDzUWFvaOb4WWjLComXm0BSLs7w6TLcenjejHXTITHLKs6tY0zGVF3CvxtEojwXp5brA6O052WnEQa_0SCH37n4AmT6MITzbihBdDgUei6GC6Oysm3EDgWTzZWrXkQWVylHGneVe3cra9G_k_V-XoBFyDAMUQEkcdiKbfgn8zoxPzmFQ0uWKtv1Vj76JbHqH4cYOSLlYa8kNl7X2o4rcKS5IvDSHkdUid9-RGfrWSpEzBs5ENZACEUcukQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در آستانۀ رحلت حضرت معصومه(س)، صحن‌وسرای حرم مطهر بانوی کرامت سیاه‌پوش شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/463317" target="_blank">📅 06:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463316">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">قانون جدید کالیفرنیا برای اینفلوئنسرها
🔹
کالیفرنیا با قانون جدید، اینفلوئنسرهایی را که در ازای دریافت پول محتوای سیاسی منتشر می‌کنند اما منافع مالی خود را اعلام نمی‌کنند، هدف گرفته است.
🔹
بر اساس این قانون، برای چنین تخلفاتی جریمه‌هایی تا ۵ هزار دلار در نظر گرفته شده و نهاد ناظر انتخاباتی ایالت اختیار بیشتری برای برخورد با متخلفان پیدا کرده است.
🔹
این قانون در شرایطی تصویب شده که کمپین‌های سیاسی بیش از گذشته از اینفلوئنسرها برای دسترسی به مخاطبان شبکه‌های اجتماعی استفاده می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/463316" target="_blank">📅 06:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463314">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd7d64ac1c.mp4?token=MMQNAWWLh-EnDRp5lUQV6wpi4qYtYb0hahHtgdXvxd-PTJrfaDM1qHaoCNuQalxPpH207YsfAclMM5HU_hlHMsnF6_Lm_GSGTgM0mHCZm6XYYPaFGC16nNlV_EzYVst5PlHM4fhvNRtbZ9gMxQX07erM7KXot9fEeWkzXdxnKFRxq4-O2Buyas2FEmOKDVwOXBB9QSKsD3-KhbJvTLJAclaIVJDq_8xS_Mn0iu8y5hSSpsQlO3Ka4E543Sz98gnOzCeLbIad1Ux2IJyn_BrFT_PuWoMurbgQl8tY0CJ0-JhZ8rT1BsfjATxKC7IXRGHbN_CpboF3ZIqedxl4rIuUqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd7d64ac1c.mp4?token=MMQNAWWLh-EnDRp5lUQV6wpi4qYtYb0hahHtgdXvxd-PTJrfaDM1qHaoCNuQalxPpH207YsfAclMM5HU_hlHMsnF6_Lm_GSGTgM0mHCZm6XYYPaFGC16nNlV_EzYVst5PlHM4fhvNRtbZ9gMxQX07erM7KXot9fEeWkzXdxnKFRxq4-O2Buyas2FEmOKDVwOXBB9QSKsD3-KhbJvTLJAclaIVJDq_8xS_Mn0iu8y5hSSpsQlO3Ka4E543Sz98gnOzCeLbIad1Ux2IJyn_BrFT_PuWoMurbgQl8tY0CJ0-JhZ8rT1BsfjATxKC7IXRGHbN_CpboF3ZIqedxl4rIuUqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌آیت‌الله شبیری زنجانی دار فانی را وداع گفت
🔹
دفتر آیت‌الله شبیری زنجانی اعلام کرد: روح مطهر فقیه اهل‌بیت عصمت و طهارت(ع) ومرجع عالی‌قدر جهان تشیع، آیت‌الله العظمی شبیری زنجانی به لقاءالله پیوست.
🔹
جزئیات مراسم تشییع و تدفین پیکر ایشان، متعاقبا اعلام می‌شود.…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/463314" target="_blank">📅 05:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463312">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yo4ooykwyZQIVqNOd2CcCRrjz5hiCyPV52ujQbyaFs2OsA5Daho1XyYHKo8TYMtloy2Dy8_K9e5QSju4n66T0dXjo4w35lx_0yGw3VPsZRuFDP_XMwa52ZvNjRBXfb0g3V9qgluN3192YtairjBi0N5XWNgowXIWfPfJhl8ev7DubHFIsUzy5UUb437jGVZgT8l6GxQ8AgBiKTow5bmD_EJoSBI8buzwczFFwz208w3t68qXDnaE3mVK0Bx_gqk31lpHsBv9WOmIMeMokUrdpJHnN-aA8Q6X-Q2nWsNZY7BomF42xQbhxeq23xRVSQWzvptNaeHoiodlllml3xSQ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران طلسم ۱۶سالۀ فینال شنای آسیا را شکست
🔹
هومر عباسی در شنای پنجاه متر کرال پشت با ثبت رکورد ۲۵.۳۷ثانیه در رتبه ۹ قرار گرفت و به فینال صعود کرد.
🔸
امیر مطاعی نیز در مرحلۀ مقدماتی ۱۰۰ متر قورباغه مردان با ثبت زمان ۱ دقیقه و ۶۶ صدم‌ثانیه در جایگاه هشتم قرار گرفت و جواز حضور در فینال را به‌دست آورد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/463312" target="_blank">📅 05:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463311">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">حملۀ هوایی پاکستان به افغانستان
🔹
الجزیره: حملات هوایی جنگنده‌های پاکستانی به ولایت کونار در شرق افغانستان چند کشته و زخمی برجای گذاشت.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/463311" target="_blank">📅 05:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463310">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtCYkxZidSayBI-AiGJQgJRJtAFgciGAUZXUXcbAbReL_nEpC4To1410pc6y4Rr5bOdGjjw85OgfIDBAyaPCYeuCtTcDKSjFP-9vUSH-5QYdu3CZWOBq8umfaq8ZYdlp523WHTOjtYBKtHckr-klrLcw1oqKTzPmUVa67wPJRgxkytvcZZaXoEUS0a7MDUynshRC9GEoB-FinsZd8Vf94DPTM7qdp4SoreliEIAMm0feCd7As-kJdue9bYUs8MixizNc3AotfiwvqAJ88rngpGEUewpuxnD_nbA1vvZge3yILIRg2l5VotQ8RchaU87yric7-9lupQ3aWBR99Rj_gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرهای خوبی که شاید امروز نشنیده باشید  آغاز پرداخت وام قرض‌الحسنه مسکن بهزیستی، و اختصاص ۱۵۰ میلیون کمک بلاعوض
🔸
سازمان بهزیستی کشور از اجرای بستۀ جدید حمایت مسکن مددجویان خبر داد که بر اساس آن خانوارهای واجد شرایط می‌توانند تا سقف ۴۰۰ میلیون تومان تسهیلات…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/463310" target="_blank">📅 05:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463309">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نفت برنت هفته را بالای ۱۰۴ دلار آغاز کرد
🔹
قیمت نفت در آغاز معاملات هفتۀ جدید میلادی صعودی شد و نفت برنت با رشد حدود ۸۰ سنتی به محدودۀ ۱۰۴.۷ دلار در هر بشکه رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/463309" target="_blank">📅 04:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463308">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287bdc0a73.mp4?token=nRC-G8dqdQ0cZJ8DJZ_69vSuaT1Gx8zyAsMcUiYA-k3BKsnMlJn_-Mzlg27T_BFtzJzWD5-k-OYt1uJHFFVEtstTPYo1HR3RjO9DKXd7CPao0h8ipz4yieEGX4hNuaLmaT_7UJw1ouD_ZEdwhadRY-D_RHYYtRL0uZW6IslQL_jcQvUE_pDiDPuUT8XGDyJ3TpQ3Q3rRj4PxELiVCB3rzdZagyedJ4RGqhtAHyrjjdBrQmQcXjxSUJcM-MR-h3OIA5lIbqcAzh2000d_xszEfr7SfQaq_oTHHAO4_KmYqIv2QSLQOFAB6C89qOwc8a1SvLmrQf2ZbFw7JQR5dkKHaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287bdc0a73.mp4?token=nRC-G8dqdQ0cZJ8DJZ_69vSuaT1Gx8zyAsMcUiYA-k3BKsnMlJn_-Mzlg27T_BFtzJzWD5-k-OYt1uJHFFVEtstTPYo1HR3RjO9DKXd7CPao0h8ipz4yieEGX4hNuaLmaT_7UJw1ouD_ZEdwhadRY-D_RHYYtRL0uZW6IslQL_jcQvUE_pDiDPuUT8XGDyJ3TpQ3Q3rRj4PxELiVCB3rzdZagyedJ4RGqhtAHyrjjdBrQmQcXjxSUJcM-MR-h3OIA5lIbqcAzh2000d_xszEfr7SfQaq_oTHHAO4_KmYqIv2QSLQOFAB6C89qOwc8a1SvLmrQf2ZbFw7JQR5dkKHaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رسانه‌های عراقی از به هلاکت رسیدن تعدادی از عناصر داعش در منطقۀ دریاچۀ ثرثار، و کشف مقداری سلاح از یک قایق توسط نیروهای حشد شعبی خبر دادند.
🔹
تعدادی از عناصر باقی‌مانده نیز پس از تحمل تلفات، پا به فرار گذاشتند.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/463308" target="_blank">📅 04:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463307">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/463307" target="_blank">📅 04:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463306">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57624d7066.mp4?token=DbvoCdIxmbeEH7ZIR5Z1W5EsVOMrcSWSG712BmMv2KpeagvNXpA8ZURNaJ8nsfeUUCo5NlgpH8hDqaMPRhgxVf4DyM1DA0pJuQVcd178eB6pxnc7mVnD9Y1YYyFRbL0oCfB05TuHmVoruJ8xKe0HaGKX5OU3oW7uAgOEtEUgPttMELVULclRRxlxg1pICpunA6-FDhvVYhQTVDXqM7dFr5yeh3WSn10cnsxHddi1oBrZarQ94Q6N93sKm2jon8vPBBNmr_pVp_rQd6larwhFW-q_DhJgZHF33dp5GZVFdAa4ljqS4dP_Q8kOYs-EQdyuvyk91V3PiVsxtqONwaEVCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57624d7066.mp4?token=DbvoCdIxmbeEH7ZIR5Z1W5EsVOMrcSWSG712BmMv2KpeagvNXpA8ZURNaJ8nsfeUUCo5NlgpH8hDqaMPRhgxVf4DyM1DA0pJuQVcd178eB6pxnc7mVnD9Y1YYyFRbL0oCfB05TuHmVoruJ8xKe0HaGKX5OU3oW7uAgOEtEUgPttMELVULclRRxlxg1pICpunA6-FDhvVYhQTVDXqM7dFr5yeh3WSn10cnsxHddi1oBrZarQ94Q6N93sKm2jon8vPBBNmr_pVp_rQd6larwhFW-q_DhJgZHF33dp5GZVFdAa4ljqS4dP_Q8kOYs-EQdyuvyk91V3PiVsxtqONwaEVCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیرالمومنین(ع): اگر غصّهٔ گذشته را بخوری غافل از حال می‌شوی
🎙
حجت‌الاسلام رمضانی
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/463306" target="_blank">📅 02:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463305">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">خانبان و لوسادا، ۲ دستیار جدید قلعه‌نویی در تیم ملی
🔹
پس از جدایی آندرانیک تیموریان و علی اصغر قربانعلی‌پور، به‌نظر می‌رسد نام ۲ دستیار جدید قلعه‌نویی قطعی شده است.
🔹
خانبان ۴۴ ساله که سابقه کار با کی‌روش و اسکوچیچ در تیم ملی را دارد؛ و لوسادای ۵۰ ساله که دارای مدرک پیشرفتۀ یوفا است، و از دانشگاه مادرید فارغ‌التحصیل شده؛ او در نساجی و پرسپولیس فعالیت کرده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/463305" target="_blank">📅 02:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463303">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8838cd1132.mp4?token=KiPki1uRoZaCPySPd81Rs2a1PSgL5BaHTmvGAkmSi6CtNghU_wRICzWz-xAH3gsPSy8vQDyOMuLXbb5OobWoQkC59o1lOD4-898llFjbU4Z0p3TkN04nPINyAAD26QxknYOmAUa041NFXtkwAtIl0zUHKAfAbxU1fIBI9FdeJNlFDB_Ai3JKmHvgOR8a3hh00PoXoRxyTBq4acruzyEONiLDo9DzPAZbDBDn9iTTArWhEoMTmYwcyViBk-yk8MPsHZ9DCYca7gu3bsJ85A8FXhZ6ONLXDjeTOvb9YNw5FVEoM0J-dGaqV4ulVt0D09o8cISnbyjnp5p6ByOaTL4iaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8838cd1132.mp4?token=KiPki1uRoZaCPySPd81Rs2a1PSgL5BaHTmvGAkmSi6CtNghU_wRICzWz-xAH3gsPSy8vQDyOMuLXbb5OobWoQkC59o1lOD4-898llFjbU4Z0p3TkN04nPINyAAD26QxknYOmAUa041NFXtkwAtIl0zUHKAfAbxU1fIBI9FdeJNlFDB_Ai3JKmHvgOR8a3hh00PoXoRxyTBq4acruzyEONiLDo9DzPAZbDBDn9iTTArWhEoMTmYwcyViBk-yk8MPsHZ9DCYca7gu3bsJ85A8FXhZ6ONLXDjeTOvb9YNw5FVEoM0J-dGaqV4ulVt0D09o8cISnbyjnp5p6ByOaTL4iaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع خبری از وقوع انفجار مهیب در یک انبار مهمات در استان حلب سوریه گزارش می‌دهند
.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/463303" target="_blank">📅 02:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463302">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBRvERaKTfbqj0V5omMio2mSRQPK6La0xBgZtiZYBIu8btp1aYaDVZ7F3E3PBNzHkKvleXfv6Nc-8Cgttuw1-iahzQgjr9N7uqPUL9YuW-4ltCHBYaScnQKct9nRsFbjbURMFqlIn5zAXGK5iH0w-q-d1MLltD_mtaK7C6isfBVqtAGdV_2chNRP2Uy1HRrSXtmqQq0U-kCqBI32W8jbQrsGPMyHZYEGIgYZoiUtcpO720d4oP5-A-lKdZ-1OpnGP20jUFdw8cq3VYn02sZTVc0W86yatO0cNcvsm0YILVK1oX0aR6mcAN5Rrxv94j-eXNwbSaG29sNOtYmLEaVCLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقال سهمیۀ بنزین به کارت بانکی از مهر در ۵ استان اجرا می‌شود
🔹
سخنگوی کمیسیون انرژی مجلس: این طرح تاکنون ۲ مرتبه در چند جایگاه به اجرا درآمده و قرار است از ابتدای مهرماه، در پنج استان کشور به‌صورت آزمایشی آغاز شود.
🔹
طرح انتقال سهمیۀ بنزین به کارت بانکی به‌تدریج تا پایان سال در سراسر کشور اجرایی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/463302" target="_blank">📅 01:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463299">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWcnYKmxgcx-wcNE26rocWbU6bN23XZuhz2x3kFrkZ8Lw3xBz_xBl2_DRM0FOGNuVoz9Ufp3wlk_y14egJRdkt5hK08E-Qqq0-IAygZe8pPy0Mp_21_yr625KNkQlvd9KFw97_SGxQdefIx6KNnfDBNYimLwEVFjYJisL-uAUm69KIZtTblpDBwKw6bmXvZ_C8aH_DKZ16LkF9xz76n03SYPVzF7yBmD4qxwWpSKs6MPWVgWRcpMRSfljaXWdeOLqJUU4rxUgzPlDZSENDrK5cBppOay-Ic_epyGqxYlV_EdaxslLpKu9nbJoUx8g6iTP7EvVNjNJBbs353yXqnwuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AGCAsqU1ZC9QBZMzmTPv7Hmb_6guM1kXsfP8BcbuUOpIOmURiQPzt3p7EcI2UXsJmlct9IH8cNty905VmQynP3eFn5Mc-VNWNffAqFE7AJxvbiwUIDQXHsPgN3XCjWbJLo4tF_GBXXgPgaKqAMYW6mrZWnQe-bBfVR2R7dXoqmw1Ojp4YRI66J8jQtjFXA5pkjAwkCQKcbMwpXjy8Zqx_922nPICdgd5BHB2lc_w3XG2Bh4SSizawnS-urCLDqHfc99irCFwiy7psF6YveMkj22DHQjoj9idSxmkREXbhB4xvGewa7K4vVegbjsGunK6hQrB3ANQEg8PIPI-B6LLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gKljkSTS6PkEkqmCvnE29ymWhIx3LuJckmi7eBeH-0Ne7YsDmrzSGqEldip9NXrxoSAr6jcVykagqEU0XAwbg3-Vpxq5QUiIYyPAHh_fy6HHNoi0uAgYPywf7KMqmS-y1oY6uV0TV7F-SuB0zfT0Spt_w4G8pfYHzwB31CRfihpP_Vtp4v5da4Ieo8yBLCFlZYCX1_JOMOiWIMFNg8ZOZNPYcXfvx8XJ4KdYAHdTZc8kd1Kwygeb2ommCUc-fYaCGIH1dVi5kKhPLpGOa35uTDW3395nxdMUwCqc1zyGnGdSzSEDdsTtwJ2d8H-FUU73JnTmsH5hFHAaWhNxgxmXQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتایج اولیۀ انتخابات پارلمانی روسیه؛ حزب «روسیۀ متحد» پیشتاز است
🔹
بر اساس نتایج اولیۀ اعلام‌شده از سوی کمیسیون مرکزی انتخابات روسیه، حزب حاکم «روسیۀ متحد» با کسب ۵۷.۲۶ درصد آرا پیشتاز انتخابات پارلمانی این کشور است و پس از آن حزب کمونیست با ۱۳.۸۴ درصد در جایگاه دوم قرار دارد.
@FarsNewsInt
-
link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/463299" target="_blank">📅 01:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463298">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4cH-yfbbIf-raQqb70N8DyKSLlXPX00O2plZqGxofsKE9bjHx19KMD0Y20FO1UiQmo-HpKHgCjH-gxfYzRnuW3Pqo8-wSCR4a11-Fi37p1DnNb6C5cCKvgfBR40F6YePJd-PNmtKfuLT-g3t2zG1tIKUMv51ClFpZ1StPuGbCUpbWhbORGcN9qeyWhqoOI1Rpne-OlMBBud3cZbcYNT1HNOJjvOxIkoFk4tp8FbOYrrskzpRgQ11VXcNdegasOicsfELIfkLpPfNGAVb8wJ3kA0RIF_k1bTV2yKwcQP-f3z10MfyqpBLemX5ek5fvLQnkVA_MxQCMYJCUlFx_tFZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات هوایی عربستان به استان الجوف یمن با ۷ شهید و زخمی
🔹
رسانه‌های یمنی از حملات هوایی عربستان سعودی به مناطقی در استان الجوف در شمال شرق یمن خبر دادند که در پی آن دست‌کم ۷ نفر شهید یا زخمی شده‌اند.
🔹
به گفتۀ سخنگوی نیروهای مسلح یمن، جنگنده‌های متجاوز سعودی از زمان آغاز تشدید تنش ۷۶۰ حملۀ هوایی علیه یمن و مردم این کشور انجام داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/463298" target="_blank">📅 01:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463292">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rwfq00TBKXANVSMyp2JqhIS-sZMugy2HKi7MLhS8j0jOVdjbtqpzM7bTvoSrGNuv5f76_muTk3kVebNHUt6EriBLlZ5DRmTjwnwTOge_79AxRfYnFmXhq6qUnj5CJ9md3i1WyzutYRnQFtKYN0C4K_S8hH8ixh9cUosnpOdkg0kYRKn0ZQ1wMY8Alcdl2uz7zXEGHVDcJEcCAi9N1oE-wP9R0GlksaFeUN9OnnCaSyiduHkcNbgoj2dDy7GDaYwOM8uADaeRtnBgKLE9s-VkOzGC5yf2PIkidDmu6cYA8SWwOrL4pvLoYEJZiZemkt7O9l7kA4Bg01QnGN6p50gcTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fViNsiDqa7pfkcSMlu5f72kzZK40K37BqXBJBgaT0911VFW4wb6aheO4_hbNw8cEamurfI52KJrEDnpCB3rH2cpRuuszJhXl4h5vs1YC4Fhg-sDt9emioV14Vn8f4Txjax0-aeTK1yARHh0MzhyG_hjBhc7clMkFbD0g49PT3Y3qOY4SgHVJrrUraueKaoolopi7GZY6Mi9l9Ky_vEzqThRldp3dCAOQmJU4lYsRcxgzUC-LdwTB644f_eVc4EiRu-VxIz95O7LWib20TPC-rytznYjtj5d5hL-3w7ydoAMjdgGQrXp-WPQazi57gr_n8YZXRC50Uy0nf7jMoFDEcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXo8VIWxh_rufnURtaFCjoKKbirEJNYJuCVoMZMWH-x9bFvVFJBKxVn3QrXlhJ2qa_04zAtdiPlh8d9lU1kkMSQ5zA8AZ_iAwvLgUmRpsnJ8C_ljb32hbhpe9t4XEo2SjmlNBG5DWp3rkVZ2C2mISSP6Hlfl9ljp_HyB2raH8YxFtpTqnNu54E8C17dUMzOqeCmGSXa-qUgU1qGE4XMmzf4czZcqYUCPiYeeYS7jyIXlqMqPZeYrVqASIOct0Jiq8VJOHoJFiIUed7IOZIuOnMi2NYLeyaaN9ozoI6EnpY2UEe05FwzmD08nOIbWc2HpRDjTrTcBIuTYHo0GObYKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNe5dFLoNQHLPRXsulMM-A0sFymiq5nZHueRbb6pp2WH6eWG0cja4cYrWi4yXXEWXjTCpGYtJuRE9Zb7gR0sAFmnDGBKg12J9lhsUsqRUunEi1Eq2siWyBwXSvVd-zNnd3Yhh4Wq7ZHNYwo-u0aIpZhO0EyxqPybCcemO4GqDOGi0MKiMzMrVtC17iBsLXl7ZerAe_Dmou-k5ccwl6vXOfIKXQ3C9NDkpteU1KWUQw4jUGv1SUcOKxy5BGGUmbajQP5vEUtqmrp0jzO4m8BMUIled2FvdF-b0NHucnGkJuk9GXB95ZBQESyiXcnYLPqyJJomAs6fNmZizC37riaWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aeV4HnfYa4On1dstWhG4zkjhhHXkQCEhDQdWyhW1UcUYKn8MmdNCgWxVqjuSJ9uxbwxWZIdqHq4MIkSr0qlslrSyPDvO4U7pXT6glPtsY7T69dxqogTsJG5rTGjTHEtvER7JHg-SE9vnkBfP6dY_Meo_9qSohaU-DA6XrsoiM1H7HgR41mNhA7zoCCESqjWPkItKvGdUjElQ31AnxnxwOqPJix8VojtwXsXqvOTRDTZ2XzPFnF8wvpv6w6w_hkIL1gxlk3X1vZHJEQ-uAuZ0yQ5sIvMnS8yXBYdyHt8rYIhwEjVS3D_I4Xr2jFQfxbzy50y_Ha0ugHktDXVPzZOEkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IxYlwmNSIUxVhJESlj_eXsMqxoztVBcdbmGaRPLDPh6kJoiNnosgbqvyD1dhSy7OwlbBepth8n4BqbWmLr3iS2KZ-U9qjMLITDaUT45lV6m18r10GNEeu9fOuusBJIhT_4bjaAEdFMbImvGfDyjr_1zcja1phoS7JP7aZum4NsoxgVzbxCa9Vb4ojk2755AjEYSOssRADjfhrQuGOBZ4D1dOFKsEahQgPZ4F0BFcXwNewuOavCsxbifUO6wOsu1r1l-mMFUMFz-rO5e6-S-2VdmhiGDyCQlOmOGzgjteqEp1e8MZcoBt9rP9-3I5-NfzItM0QViNcV4G7lsN5akiOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ارتش ایران پهپاد اوربیتر دشمن را بر فراز تنگۀ هرمز منهدم کرد
🔹
روابط‌عمومی ارتش: ساعت ۱۸:۳۰ امروز، یک فروند پهپاد شناسایی پیشرفتهٔ اوربیتر با آتش سامانه‌های بومی نیروی پدافند هوایی ارتش بر فراز تنگهٔ هرمز هدف اصابت قرار گرفت و منهدم شد. @Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/463292" target="_blank">📅 01:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463291">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y80Qvh-zAwSd5FAFDxWPfCgHUsKFCZNphISJ-QRPPSzSUm7N-IYJMu2sfq29lZMBE21xaNl01_K8e58BPeypHFb2Hsq3VoIMWvH64MwLsA3BGcUbSLXpfRuXiRHxEHPs77REdFCXk8h23cqZsPRgRvNoeHVtllLIIbIezuRHTcNkPFRD3AnwDxppXb6Yj18KFWA-EiAUpvNJgbS_dReze7vI-6MWfHhMtGDBj6IEt_7l_jwUPu4x_aTA4TvBRgJCfYz0KS3yJrH6ldzFscDfBwREhACD3JQdkfLeRm1I5ksAt5zjTuCmMVJKWzrrtnebiGqCMCo3J7jDlp4PVSNodw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله سیدموسی شبیری زنجانی به‌دلیل عارضۀ خونریزی معده در بخش مراقبت‌های ویژۀ بیمارستان بستری شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farsna/463291" target="_blank">📅 00:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463290">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FB9Ujzatf_IjMcT-g0ZaI9d5Ce1r8hOQKKodJMUu3Lz1Clcj6gT_Y4rF_6QB0f14Oh7W8vJZRVrAopDSkQRzleE00m63Se5QlH9kqAixRJWCZcvKv1bTA3vQuXDwfO19oC0Juu5WIh1UqMaStcsEONBkyXRd9lQ8NPbJLpqIs0U7F94_1TH1GiAPvYjrkGiSfqFCwi9761eQrhC6Uvp7DD4Ba9qWTvY63GetjgaTHg0eWqopX1BU2xFsNgv6mI9zw-Daw5VvhaSeyUy7Zr96Opc_dqAU4vB_AQ2-1xIJe0NAiqo6oNCBRZo8hVODCW9H26OVsF9jwLLeFt9WmAgsnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای شایعهٔ حکم اعدام یک متهم در مشهد چیست؟
🔹
رسانه‌های ضد انقلاب با انتشار یک فایل صوتی منتسب به فردی به نام نجمه امینی مدعی شدند این صوت از داخل زندان مشهد از سوی این متهم منتشر شده و در این صوت، فرد مدعی است برای او حکم اعدام صادر شده است.
🔹
پیگیری‌های خبرنگار فارس از منابع آگاه حاکی است فردی به نام نجمه امینی به اتهام توهین به مقدسات و سب النبی در فضای مجازی و فعالیت علیه امنیت ملی در ایام اغتشاشات دی‌ماه مشهد بازداشت و به زندان مشهد منتقل شده است.
🔹
این منبع آگاه در پاسخ به سوالی درخصوص صحت ادعای صدور حکم اعدام برای این فرد تصریح کرد: هنوز هیچ حکم قطعی برای این متهم صادر نشده و هنوز دیوان درباره این پرونده اعلام نظر نکرده است. او هدف از انتشار این محتوا را تهییج دانشجویان در آستانه شروع سال تحصیلی جدید عنوان کرد.
🔹
این منبع آگاه دربارهٔ اصالت صوت منتشر شده نیز گفت:‌ هنوز اصالت صوت منتشر شده از سوی نهادهای ذی‌ربط تأیید نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/463290" target="_blank">📅 00:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463289">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">توقف پروازهای ایران و عراق تکذیب شد
🔹
ساعاتی پیش خبری در فضای مجازی منتشر شد که دولت عراق تصمیم گرفته تمامی پروازهای ایران و عراق را از سه‌شنبۀ آینده متوقف کند.
🔸
حالا سخنگوی سازمان هواپیمایی کشور ضمن تکذیب این خبر گفت منابع داخلی و عراقی این موضوع را به‌طور کامل رد کرده، و پروازها میان دو کشور همسایه،‌ همچون گذشته برقرار است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/463289" target="_blank">📅 00:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463288">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ep6IEq6bGkNHmUma4kFUOxJfsCpJOYNOLJhfxADD7MQUhg-KkfNmbdGR2hVKhM-v6blzI6ApedF_qDpZWnImj6DOtpa6E5y4o8TqpeTwZdzZDsDqpjNVqQVi4chqNbREIR7dTZdr-DhODkud6AQ-tWygV_J9IkV0TclTOjLbfOdx7-mv773_j27cBcLHwMp0smI7NAE_352aZ2-M4OOC_4Kj0DYcZy6Egx8eUIS57ZtFZSsKKayaO0X4nl0_11hiNWThpUzPJ0XHy31AxZpcwmKn-vLx4QxrH0j8s0zn_f92ZmrRusq0g_jeXqDa3pvvtgDdT7OwRixSANFLOAmRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود دادستانی به حواشی آراز کاپ نوشهر
🔹
دادستان عمومی نوشهر: پس از اطلاع ضابطان قضایی از بروز برخی رفتارهای خارج از شئونات اخلاقی و شرعی در ساحل مجاور ساختمان هتل بین المللی آراز نوشهر، موضوع با قید فوریت مورد بررسی قرار گرفت.
🔹
با اخذ اظهارات شاهدان و بازبینی چندین ساعت از تصاویر دوربین‌های مداربسته مجموعه هتل آراز، مشخص شد این اتفاق پس از پایان مسابقات در رشته‌های بسکتبال سه‌نفره و تنیس ساحلی و در ساحل مجاور این مجموعه رخ داده است.
🔹
بررسی‌های اولیه نشان می‌دهد نحوه نظارت و هماهنگی دستگاه‌های مسئول و برگزارکنندگان مسابقات نیازمند بررسی دقیق است.
🔹
در صورت احراز قصور یا تخلف، با افراد حقیقی و حقوقی مسئول مطابق موازین قانونی برخورد خواهد شد و در اجرای قانون اغماضی صورت نمی‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/463288" target="_blank">📅 23:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463287">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkQLtNBkY9n8ePu_vJdlQKWeVCGcqqBefOF4MnMJCyfPokperWhS3Oqj_GReESScQUIhaXhFflpxwqbcfFQXLxMPBDl5sb7Xhnl3V6hUxyb9ICv04jX0XD688n-4z5cHJP4i1NMY84bNGOsy49-JTdu-JJ90Kla4_iynkQTdcT9A9gDJzxeTe1soRri-12xnslwZjwq1r6442ResqawJFYj4RWBZa_qV6IzaG3WmoFFma4Mq_UQiIY697TfVeSPcg6amzINW2OpxbuPzGDckf4GnOy4tw0p2STZcYo4kYYEtO1WIzbAx0p7-LQHirfPxkqcPz6jLj6iZ5R3rRVVpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبل از فروش لپ‌تاپ، این چند قدم را فراموش نکنید
🔹
انگجت: لپ‌تاپ قدیمی فقط یک وسیله الکترونیکی بلااستفاده نیست؛ ممکن است هنوز حجم زیادی از اطلاعات شخصی، حساب‌های کاربری و فایل‌های خصوصی صاحب قبلی را در خود نگه داشته باشد.
🔹
به همین دلیل، فروش، اهدا یا بازیافت آن بدون پاک‌سازی کامل می‌تواند اطلاعات کاربر را در اختیار فرد دیگری قرار دهد.
🔹
اگر لپ‌تاپ همچنان قابل استفاده است، فروش یا واگذاری آن به فرد دیگر یکی از گزینه‌هاست و در صورت خرابی یا فرسودگی نیز باید برای بازیافت ایمن تحویل مراکز مربوط شود.
🔹
اما پیش از هر تصمیمی، نخستین مرحله تهیه نسخه پشتیبان از اطلاعات است. در رایانه‌های ویندوزی می‌توان از ابزار «ویندوز بک‌آپ» برای پشتیبان‌گیری استفاده کرد و در کنار آن، فایل‌های مهم را روی یک حافظه خارجی مانند هارد یا حافظه اس‌اس‌دی قابل حمل ذخیره کرد.
🔗
اما قبل از اینکه لپ‌تاپ قدیمی‌تان را بفروشید، آیا مطمئنید هیچ اطلاعاتی از شما روی آن باقی نمی‌ماند؟
راه درست پاک‌سازی لپ‌تاپ را در
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/463287" target="_blank">📅 23:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463286">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6XR5ylsNf4sb45iPx4CgWJLz2yImq8hxL5eQ1fMXVJP-nPllyvKbbMR7ftodox7qfvTT8KjCs9Ca2kjfxEJDEC7RY2Yr-eocwEVdt4WqTWhO4WwdLfgib0myHynkFX4h3eZQP4gYizkotWrkUcwI-yaNMk0groG2Af5kRBLv2LButfV2Lsw-saQnlErKMVxeWpwe6_7g4LBfQQ6MlmU0exwz5JezJX5Oxg59HUGa6nTmnDTuJc5IExHQHN5a9kTWskG0L4FmQgoQOT1h1lZ4n7FbgExNNTuVBcvk-gR6ZuP2tfv2ZlOz1Tru5tSUHNkNOGNEfwfcit_TcctTpQX0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن به نابودی اقتصاد عربستان تهدید کرد
🔹
وزیر دفاع و رئیس ستاد مشترک ارتش یمن در بیانیه‌ای مشترک نوشتند: حکومت عربستان سعودی و مزدورانش باید از این شکست‌ها درس بگیرند.
🔹
هرگونه حماقتی که مرتکب شوید، هزینه‌ای گزاف برایتان خواهد داشت.
🔹
موشک‌ها و پهپادهای ما می‌تواند به عمق خاک عربستان ضربه بزند، اقتصاد این کشور را نابود ‌کند و به هر مکانی که در آن مسئولان سعودی پناه گرفته‌ باشند برسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/463286" target="_blank">📅 23:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463285">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ecdb9dd0d.mp4?token=tw0PPQtZo7RN2DX7WEi-It4wgvFNj2m6W8JstEt9NVUg5ZS1VuOF7KiLb0QjyirCR63fmddH0XBgOV3PuIDRGUF1DzYi94oDSxT39bcJ6fadtWH3FD0QLUET4rtHXJGfJpdsQsivhCV0A7CCLrkIU9zFKbouVeT9DlBBfmcDPEhUL6Z76sYfdsUnz8zWBdtFXyuiomU8r1f2Is4wIcYDGIusPiDYljmU7GCfq5S9fG7DTWck0_jbgOd9Llzh6O8AG-jm0SfevikWBETYpz5MXMUmWLO8dYPj0DP1nWwaiLprBZw6kTKndRSZUedA9yzXVPVEDvUDmlj4RUZHk6Kykg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ecdb9dd0d.mp4?token=tw0PPQtZo7RN2DX7WEi-It4wgvFNj2m6W8JstEt9NVUg5ZS1VuOF7KiLb0QjyirCR63fmddH0XBgOV3PuIDRGUF1DzYi94oDSxT39bcJ6fadtWH3FD0QLUET4rtHXJGfJpdsQsivhCV0A7CCLrkIU9zFKbouVeT9DlBBfmcDPEhUL6Z76sYfdsUnz8zWBdtFXyuiomU8r1f2Is4wIcYDGIusPiDYljmU7GCfq5S9fG7DTWck0_jbgOd9Llzh6O8AG-jm0SfevikWBETYpz5MXMUmWLO8dYPj0DP1nWwaiLprBZw6kTKndRSZUedA9yzXVPVEDvUDmlj4RUZHk6Kykg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۲۰۴ حماسهٔ خیابان بروجردی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/463285" target="_blank">📅 23:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463284">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXCsDAaXcu1M2ney__J9lPYm0L_maVYba8LTNfpTJF-eBjUSr7H0IwFswIEm_gmB0ek-Ujk-AFXGpozNe4zC0SkTj1HmRW3jaI1DMQQLZeeI1vmHvLBZ3GVmdd_1vS_-jBp1MSWzaL-Zz4gUT7NBzB9PgnpNKsvDgqPKVww42PbbYhIzaVEPHup3IbTujXvbgkP0sPE3pIXmRceqzfEuDgPQT4U5YvtLph1-VYDPpo1GaRx4WY8ROHiBWvbhqIAG3SQzF1UcARLtmI-Gw49Pz8wT02Z5mp-6bFlbEug4ig1g1nYBGgTqG7x5PzpHf7dGZnnvFGH4M62__0VmQTvNoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مغز ما چگونه تمیز می‌شود؟
🔹
شاید تصور کنیم تمیزکاری فقط مربوط به خانه، لباس یا وسایلی است که در طول روز استفاده می‌کنیم اما مغز ما هم به نوعی نیاز به پاک‌سازی دارد.
🔹
در طول روز فعالیت سلول‌های مغزی باعث تولید مواد زائدی می‌شود که باید از محیط مغز خارج شوند. بخش مهمی از این فرایند پاکسازی در زمان خواب، به‌ویژه در خواب عمیق، انجام می‌شود.
🔹
پروفسور ندرگارد کشف کرد که یک سری سلول به اسم گلیا در مغز وجود دارد که کار پاکسازی و تمیزکاری را در مغز انجام می‌دهند دقیقا شبیه کاری که سیستم لنف در بقیه قسمت‌های بدن انجام می‌دهد.
🔹
او اسم این سیستم تمیزکاری را گلیمفاتیک گذاشت بر وزن لنفاتیک. این کشف باعث شد به یافته‌های بسیار مهمی در مورد آلزایمر دست پیدا شود.
🔗
مغز دقیقاً چه زمانی و چگونه خودش را تمیز می‌کند؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/463284" target="_blank">📅 23:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463283">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11908925a5.mp4?token=g3o5VzL26IqRLfFcyYyGnCSmWuRIYH_yJcdVwQTkpHhExzAWRINwo1Nx63QZe0Uz0ehnER1dhpgyX0i9Pl8RECL3O3FM6YTRkR6LXQP3vPuSCGkhEd15bmh1O05Qg-En7N3sQwTg78GJtx7XkZ7UacvbuRUYE5yfyquM9Zzs07N8CGUKh6uI1pWMkt6HWtbi0hjd9my7VlHFDHJTKw0W55ODQ8Wb8O8BYr64_-BsgTzq4ub6IvHEf6Y69hsG6klVfhYUz9Xi0xvXH085qZ0UznzuTHdl0hE2Kqi3g3qXUgzSjsEFrivOFLEyUj5fBizOR2d6RjXPb6I_YBVOX1xuB3I1Et4g_1FnD5IWZPp-vCCBO7q01qZO3xqYzMc66tMXzfWB_OYcXsBuHq9x4aHMF-o6f2FtQJUG6xJwJkF5mPtxy78oIELd_ZhmAD8-W9GNl7B9LUrw8Kmst_Ct98iIt4ageACcjOaSP5vWzHbRoIGICCd5siFe-79wMgiBVNxD4PP5YiPudlSokBktpbAPprH-DoZR29HVPmYOVsGVFf05yLt6MdS-iKqkyZIZ-DpL8d9rQ44Wj6OprPYHpEUyncudtqPPCRsk7fsTynFSlXVLvX9uI0gJ-VxG7Ha8WGxIw5uzif3x38VOSJh-uHpqVwPTaa-w64SIRiHhk0hxqH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11908925a5.mp4?token=g3o5VzL26IqRLfFcyYyGnCSmWuRIYH_yJcdVwQTkpHhExzAWRINwo1Nx63QZe0Uz0ehnER1dhpgyX0i9Pl8RECL3O3FM6YTRkR6LXQP3vPuSCGkhEd15bmh1O05Qg-En7N3sQwTg78GJtx7XkZ7UacvbuRUYE5yfyquM9Zzs07N8CGUKh6uI1pWMkt6HWtbi0hjd9my7VlHFDHJTKw0W55ODQ8Wb8O8BYr64_-BsgTzq4ub6IvHEf6Y69hsG6klVfhYUz9Xi0xvXH085qZ0UznzuTHdl0hE2Kqi3g3qXUgzSjsEFrivOFLEyUj5fBizOR2d6RjXPb6I_YBVOX1xuB3I1Et4g_1FnD5IWZPp-vCCBO7q01qZO3xqYzMc66tMXzfWB_OYcXsBuHq9x4aHMF-o6f2FtQJUG6xJwJkF5mPtxy78oIELd_ZhmAD8-W9GNl7B9LUrw8Kmst_Ct98iIt4ageACcjOaSP5vWzHbRoIGICCd5siFe-79wMgiBVNxD4PP5YiPudlSokBktpbAPprH-DoZR29HVPmYOVsGVFf05yLt6MdS-iKqkyZIZ-DpL8d9rQ44Wj6OprPYHpEUyncudtqPPCRsk7fsTynFSlXVLvX9uI0gJ-VxG7Ha8WGxIw5uzif3x38VOSJh-uHpqVwPTaa-w64SIRiHhk0hxqH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع ۲۰۴ مردم کرمان برای دفاع از وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/463283" target="_blank">📅 23:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463282">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23196aff17.mp4?token=m-Fj9IOz87zrXw5ySkv3A1S5VWU50KWZLodo7qXzloznbMvZFOgLReVJzIYx3C4TyGNHg6gbPt6xHLgbMHZ0qq61TzUxyQl8-HCB32118n4CZS-fiKSjOwKGk3VKzCF6A_MPXI4dA38mkLL_0qmZCYu6eQa9D8eX-Y45pfYcY9Jobj7voKoqnJFWNfpTPGld-rRoImC33FZ7_t_4ST8Df00CbchWx5QxzXZ1sstcva_JiXTi4pgrNBScf6cchEXM9x4G91DudzzV6-qbxYCDzvZLvmf8zoOyQMCYndF6BHV8NQ26Q7sTupN6DRZXESBUpIsTl6iwnI3xedmZYjLKBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23196aff17.mp4?token=m-Fj9IOz87zrXw5ySkv3A1S5VWU50KWZLodo7qXzloznbMvZFOgLReVJzIYx3C4TyGNHg6gbPt6xHLgbMHZ0qq61TzUxyQl8-HCB32118n4CZS-fiKSjOwKGk3VKzCF6A_MPXI4dA38mkLL_0qmZCYu6eQa9D8eX-Y45pfYcY9Jobj7voKoqnJFWNfpTPGld-rRoImC33FZ7_t_4ST8Df00CbchWx5QxzXZ1sstcva_JiXTi4pgrNBScf6cchEXM9x4G91DudzzV6-qbxYCDzvZLvmf8zoOyQMCYndF6BHV8NQ26Q7sTupN6DRZXESBUpIsTl6iwnI3xedmZYjLKBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همدانی‌ها در شب ۲۰۴ همچنان پای قرار ایستادند
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/463282" target="_blank">📅 22:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463281">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f8bfd542c.mp4?token=s79fI_YMltCIyM-DNqUUsToh_UtJWw3bAyk4OsPynqlWzJaFUnRGxCjInjCsimUkIisiUziqWFVmKPS4L9pBbVi22iD78GyxoM4u90cosrxS1iMx-pyCrsn3ewymM9vcoKXstYOeVufMdgu3bczSBBeO-qzmFjPcdbNM2Lc23TTY6oTE5ouaWYK6_PLjNcEI5PhFIOSQo9WqDcMA7X_nnfFF7dKfWqVzibp9MPjArOpial959uoOADKfVcvSnT7T9ZwYZ0dgqNLY6S2DEReSe0l63noZZv5uZYzD9-EoDj1vAY6w9pw8pkq8x0fnxwsaj_een6ReVS4M3HnXAwgIZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f8bfd542c.mp4?token=s79fI_YMltCIyM-DNqUUsToh_UtJWw3bAyk4OsPynqlWzJaFUnRGxCjInjCsimUkIisiUziqWFVmKPS4L9pBbVi22iD78GyxoM4u90cosrxS1iMx-pyCrsn3ewymM9vcoKXstYOeVufMdgu3bczSBBeO-qzmFjPcdbNM2Lc23TTY6oTE5ouaWYK6_PLjNcEI5PhFIOSQo9WqDcMA7X_nnfFF7dKfWqVzibp9MPjArOpial959uoOADKfVcvSnT7T9ZwYZ0dgqNLY6S2DEReSe0l63noZZv5uZYzD9-EoDj1vAY6w9pw8pkq8x0fnxwsaj_een6ReVS4M3HnXAwgIZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله عاملی: همهٔ محاسبات می‌گفت شکست قطعی است، اما تاریخ نشان داده وقتی خدا با کسی باشد، معادلات تغییر می‌کند
🔹
روایتی از روزهای پیروزی انقلاب اسلامی؛ «همه چیز با ما بود، فقط خدا با خمینی بود»
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/463281" target="_blank">📅 22:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463280">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f823bb53f.mp4?token=UIuGC28rNlelG0JtA3s8mbgot9fQ0KHAwsQAa4VZOrl9GiBqxQDqC7MLRYuDKkyhCj6gmAOOqcUbguDnhb2Dx-GRDr0m2N9xKIQoBT_6LWpLLhZ_pFf55_7Ha-OoFY1LSWozfYR_zRRRUq-izNddI6PC_uYuZmT2Vgil-P2X32Ix8_5aksKVzb-nGkmzD-EKj3Z5-W9b4j0FwyoTClmtNYgvL9qt8PRzT7gVR6ObzC1b1CITr9eoHr1P6fzXwGzryVrD9OnZFg_5fQSRo4glYCRsqFD3mHQow8qflekCpNJ70qdacpcGSWf8d5ilWL0Fsxr_Py_4giYRhbcfkBW_5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f823bb53f.mp4?token=UIuGC28rNlelG0JtA3s8mbgot9fQ0KHAwsQAa4VZOrl9GiBqxQDqC7MLRYuDKkyhCj6gmAOOqcUbguDnhb2Dx-GRDr0m2N9xKIQoBT_6LWpLLhZ_pFf55_7Ha-OoFY1LSWozfYR_zRRRUq-izNddI6PC_uYuZmT2Vgil-P2X32Ix8_5aksKVzb-nGkmzD-EKj3Z5-W9b4j0FwyoTClmtNYgvL9qt8PRzT7gVR6ObzC1b1CITr9eoHr1P6fzXwGzryVrD9OnZFg_5fQSRo4glYCRsqFD3mHQow8qflekCpNJ70qdacpcGSWf8d5ilWL0Fsxr_Py_4giYRhbcfkBW_5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: قطعاً مدارس حضوری خواهد بود
🔹
ما تمام برنامه‌ریزی‌های لازم را برای حضوری‌شدن کامل مدارس انجام داده‌ایم.
🔹
اگر اتفاقی در نقاطی از کشور رخ بدهد، اختیاراتی به استانداران می‌دهیم و استانداران متناسب با آن شرایط، به‌صورت نقطه‌ای تصمیم‌گیری می‌کنند.…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/463280" target="_blank">📅 22:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463279">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYh4c63TzIMs5T8wKJRNkkjb9DCAY-q-rEWKTi6gm_kRfpOZbcZOf5nu_OaRBMLA3-RFmfNrDmUEdpX1V0kyJc00Bk8gB5Wgf7gX_X2oeqXSk2kMSxLqE5f_w-a4am0VbHznUr455EieE3nM6npEcHWOmho3QWZx7RsD4sjU2rjiVCQlTM-WZwzF33GtQXqizcID1Pvrc5ILaDqy8gvFOyXmrfUqIH8jxBBEMOn7El8ReQBrLQJEhoQGE0rFo3gVbhe3Uu62ouyN139931n3KIG4f6oYiuf2T2YEJc6MH6ez7-VSw6dZOJaLUYowOjBtRbO6CkVncwJVyKj2MFmwSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشاورزی به ازبکستان رفت
🔹
نوری، وزیر کشاورزی در راس هیئتی از تجار و بازرگانان با هدف افزایش روابط اقتصادی به تاشکند سفر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/463279" target="_blank">📅 22:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463278">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e283b14cd.mp4?token=abyfcxUljSXgbibntyjIZCf72iieixdvSx8FmtOSPKbl84ySmzQ2GKPJ7gmlAfmMr9o1jwF-s_VK9MpsXSb8zjP8dFEySMZ9SAb7F6W-xm-dV6fl6iou5YKImz001P4iRbhM63VWvbz31P3oIOBsRvpuW_RS-RsbmJNPZTtMF7ZIUcSNrRzFeTyb1j5_297Tj74P9iXKYs1LnKItrWBaPyqDf9pdn0jpLWdltUCyZdWPrv4vZy2fXe0gwm_FKaelt3jBNPTG8MZmSJs7W2rL5ymrTLKI8kKmCEqKShV26g42x_db0tqaxFYPEVvUozwrVp6G1zhZKUF7pKKqe_QUxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e283b14cd.mp4?token=abyfcxUljSXgbibntyjIZCf72iieixdvSx8FmtOSPKbl84ySmzQ2GKPJ7gmlAfmMr9o1jwF-s_VK9MpsXSb8zjP8dFEySMZ9SAb7F6W-xm-dV6fl6iou5YKImz001P4iRbhM63VWvbz31P3oIOBsRvpuW_RS-RsbmJNPZTtMF7ZIUcSNrRzFeTyb1j5_297Tj74P9iXKYs1LnKItrWBaPyqDf9pdn0jpLWdltUCyZdWPrv4vZy2fXe0gwm_FKaelt3jBNPTG8MZmSJs7W2rL5ymrTLKI8kKmCEqKShV26g42x_db0tqaxFYPEVvUozwrVp6G1zhZKUF7pKKqe_QUxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احساسی شدن شرکت‌کنندهٔ برنامهٔ سرآشپز شبکه ۳ به یاد مادرش
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/463278" target="_blank">📅 22:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463277">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b95879771.mp4?token=cVPSka-g2MGpVIRgf36ulKgKKq2LO4jF_fCcs0GGgxAB1ivSVOn2HD2DbQ1GoZfLIwTB1yha2py_7NU1PeXx22bcDw_Vrl1AfnnkVhoEmdol_yJsQCPxmTKC8cEp2k9DvIODHP94wlCFH4tJ00msNPlKAOwS8VZNINsiIGnHJU5wZNg6Cc4ILZGVaYKS2SQsJudCIsEUtlZ07jXGRmLl09dStk2SBz4EtgspMEpFdiKqxTRzcHWt6OujNSa_GEqFUrgg8yTDa_HrD-T2LJCCk-vUjB5A6ugf6nsgI28FjnSEBWHAqPBCtL8j5Ts3vSY0MYw5SA4BMJog4_QKt4rDlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b95879771.mp4?token=cVPSka-g2MGpVIRgf36ulKgKKq2LO4jF_fCcs0GGgxAB1ivSVOn2HD2DbQ1GoZfLIwTB1yha2py_7NU1PeXx22bcDw_Vrl1AfnnkVhoEmdol_yJsQCPxmTKC8cEp2k9DvIODHP94wlCFH4tJ00msNPlKAOwS8VZNINsiIGnHJU5wZNg6Cc4ILZGVaYKS2SQsJudCIsEUtlZ07jXGRmLl09dStk2SBz4EtgspMEpFdiKqxTRzcHWt6OujNSa_GEqFUrgg8yTDa_HrD-T2LJCCk-vUjB5A6ugf6nsgI28FjnSEBWHAqPBCtL8j5Ts3vSY0MYw5SA4BMJog4_QKt4rDlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: قطعاً مدارس حضوری خواهد بود
🔹
ما تمام برنامه‌ریزی‌های لازم را برای حضوری‌شدن کامل مدارس انجام داده‌ایم.
🔹
اگر اتفاقی در نقاطی از کشور رخ بدهد، اختیاراتی به استانداران می‌دهیم و استانداران متناسب با آن شرایط، به‌صورت نقطه‌ای تصمیم‌گیری می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/463277" target="_blank">📅 22:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463276">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60af7456ed.mp4?token=c7un2vRaswGH0JKKhqhrHJe20N4LVDWEdmOQJq0xAl8Pm07BtpNPOnm3UZjJtJpCAFr-5MOiGYXkzcFpu5XPEsBzYLUdPGhpYkIaj4T9NyrIJXHset8LExmP7V7EOwM5xOkItVd7XEcQbEZQZy4lRCabdQnT9HCy0SybOD08CWvVvAozBB_yWs7i4TVKXLsFiXieTqup43tl9qbM3Uqazz-HYosj46MI6UD9zGnvYWiWdbT-n1PtqQ8Q_fZ0QMBrOzdenNc6pdNfyXS8pfIWgQbP9-Nf3ZbXt-nFaxx1NJ7u4BlwyvMS8f3eMjRfwki3pfqXI5xitQVZFnNIdbb5AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60af7456ed.mp4?token=c7un2vRaswGH0JKKhqhrHJe20N4LVDWEdmOQJq0xAl8Pm07BtpNPOnm3UZjJtJpCAFr-5MOiGYXkzcFpu5XPEsBzYLUdPGhpYkIaj4T9NyrIJXHset8LExmP7V7EOwM5xOkItVd7XEcQbEZQZy4lRCabdQnT9HCy0SybOD08CWvVvAozBB_yWs7i4TVKXLsFiXieTqup43tl9qbM3Uqazz-HYosj46MI6UD9zGnvYWiWdbT-n1PtqQ8Q_fZ0QMBrOzdenNc6pdNfyXS8pfIWgQbP9-Nf3ZbXt-nFaxx1NJ7u4BlwyvMS8f3eMjRfwki3pfqXI5xitQVZFnNIdbb5AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۴ شب قرار عاشقانه؛ گنابادی‌ها همچنان پای وطن ایستادند
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/463276" target="_blank">📅 22:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463275">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBD4Luc5MXiZi0qSaL8IDbX5AuXlRf3YOoMumC8xUoEHGIDnI1biYHttdoc-EuDjXSIjCI3lzcSzChBmMQ5KnzI6hmAFsmEbb6whlZouQvGCkWGweUK8AcQ8YgriQWCUrH7qX1e2RKngX76DFua9pS6fLxvSocDodwkGbYcz0bpTiU35K_JcQ8AwFSftwxdJ_Nr0cBuwwGvmojFPX89qSXBVpwBU6C0wOe--uSB-T18ys1nm8AIXU72S-Qmenj95OCBoyU8A6FlneWO6tfzXAVY1cgBojmMY1MZKi3xkLOhwxRAJKcVVhYGgVSQiqqUN06oG_XfxvWpQZxyYa0Kt7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی برای شرکت در اجلاس سازمان ملل عازم نیویورک شد
🔹
وزیر خارجه در مسیر سفر به نیویورک توقف کوتاهی در دوحه دارد و دربارۀ آخرین تحولات منطقه رایزنی می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/463275" target="_blank">📅 22:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463274">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
برای درمان دندان به دندانپزشکی مراجعه کردم؛ هزینه یک عکس ۳۵۰ هزار تومان، کشیدن دندان ۳ میلیون تومان و کشیدن با جراحی ۵ میلیون تومان اعلام شد. با این هزینه‌های سنگین،
بسیاری از مردم توان پرداخت هزینه‌های درمان دندان را ندارند
.
🔹
پس از بیش از سه دهه خدمت، بازنشستگی برای ما به‌جای آرامش، به دغدغه‌ای دائمی برای تأمین ابتدایی‌ترین نیازهای زندگی تبدیل شده است. با وجود سال‌ها خدمت صادقانه، امروز پرداخت اجاره مسکن، هزینه تحصیل فرزندان، مخارج روزمره و هزینه‌های درمان به دغدغه‌ای سنگین تبدیل شده است. ما انتظار زندگی تجملاتی نداریم؛ تنها می‌خواهیم حاصل سال‌ها خدمت، کفاف یک زندگی آبرومندانه را بدهد. از
مسئولان محترم صندوق بازنشستگی کشوری
، سازمان تعاون روستایی و سایر مسئولان مربوطه تقاضا داریم
صدای بازنشستگان را بشنوند
و برای رفع مشکلات معیشتی آنان اقدامی جدی و فوری انجام دهند.
🔹
لطفاً پیگیری کنید چرا
به برخی خودروهای نو شماره
، از جمله خودرویی که با زحمت و حقوق کارمندی خریداری کرده‌ایم،
بنزین یارانه‌ای تعلق نمی‌گیرد و مجبوریم
بنزین با نرخ ۱۰ هزار تومان
تهیه کنیم؟
🔹
لطفا پیگیر
دهک‌بندی‌های غیر عادلانه
باشید. من مستأجرم با یک ماشین ساینا با درآمد کم چرا باید دهک نه باشم؟
🔹
عوارض برخی آزادراه‌های کشور
به‌صورت دوربینی و با ثبت پلاک دریافت می‌شود و راننده باید ظرف هفت روز آن را پرداخت کند؛ در غیر این صورت به‌دلیل تأخیر چندین بار جریمه می‌شود. اولاً همه مردم از این قانون و مهلت پرداخت اطلاع ندارند چرا اطلاع‌رسانی درست و کافی انجام نمی‌شود؟ ثانیاً همه مردم سواد یا امکان پرداخت آنلاین ندارند، اما بدهی آن‌ها روزبه‌روز بیشتر می‌شود. ثالثاً بسیاری از افرادی که نحوه پرداخت را می‌دانند، پیامک‌های تبلیغاتی را در تلفن همراه خود مسدود کرده‌اند و در نتیجه
پیامک‌های هشدار پرداخت عوارض نیز به دستشان نمی‌رسد و مرتب جریمه می‌شوند
. حقیقتاً این شیوه درآمدزایی منصفانه نیست. فردی ممکن است هنگام فروش خودرو تازه متوجه شود مبلغ عجیب‌وغریبی بابت عوارض جاده‌ای بدهکار است.
🔹
در ارتباط با
سهمیۀ سوم سوخت در استان‌های کرمان و سیستان‌وبلوچستان
سؤال و مطالبه‌ای داریم. مسئولان آیا متوجه نیستند که مردم این استان‌ها به ‌دلیل مسافت‌های طولانی بین شهرهای مختلف و مرکز استان یا سایر استان‌ها، برای مراجعه به پزشک و انجام امور ضروری به مشقت می‌افتیم؟
با این مقدار سهمیه بنزین، نیاز مردم برطرف نمی‌شود
. مشهد که رفتیم در هیچ‌کدام از جایگاه‌ها به ما بنزین ندادند و با مشکل جدی مواجه شدیم. این سؤال هم برای مردم مطرح است که چرا باید با وجود چنین شرایطی، سهمیه سوخت این استان‌ها محدود باشد؟ آیا استاندار و مسئولان استانی واقعاً از مشکلات مردم در این زمینه اطلاع دارند؟
🔹
بنده نیروی رسمی آموزش‌وپرورش با ۱۳ سال سابقه خدمت هستم. یک سرباز معلم پس از دو سال حضور در آموزش و پرورش، کارت پایان خدمت خود را دریافت می‌کند، اما ما
نیروهای رسمی آموزش و پرورش
با وجود ۱۳ سال سابقه خدمت، هنوز
کارت پایان خدمت
‌مان صادر نشده است.
🔹
چطور واسطه‌ها خرمای کشاورزان را نمی‌خرند و بهانه می‌آورند که خریدار نیست، اما همین خرما وقتی به دست مصرف‌کننده می‌رسد با قیمت بالایی عرضه می‌شود؟ منِ مصرف‌کننده به‌دلیل گرانی خرما توان خرید ندارم. اگر واسطه‌ها خرما را از کشاورز با قیمت پایین خریداری می‌کنند، چرا محصول را با قیمت مناسب به مصرف‌کننده عرضه نمی‌کنند تا فروش بیشتری داشته باشد؟ آیا این انصاف است که زیاده‌خواهی واسطه‌ها هم کشاورز و هم مصرف‌کننده ضرر کنند به خاطر!
🔹
در شهرستان ورزقان استان آذربایجان‌شرقی و در مجموعه
معدن مس سونگون
، متأسفانه در شرکت‌های تابعه،
جذب و به‌کارگیری نیروی انسانی
بر اساس سفارش و روابط انجام می‌شود و این موضوع موجب ایجاد تبعیض و احساس بی‌عدالتی در میان بخشی از مردم منطقه شده است.
مردم بومی این منطقه
انتظار دارند فرصت‌های شغلی مجموعه سونگون به‌صورت شفاف و عادلانه در اختیار نیروهای واجد شرایط قرار گیرد.
🔹
من
راننده تاکسی
هستم. سهمیه بنزین ۳ هزار تومانی ما ابتدا ۴۵۰ لیتر بود بعد به ۲۲۸ لیتر کاهش پیدا کرد و پس از گرانی بنزین، سهمیه را به ۱۰۰ لیتر رساندند که همین امروز تمام شد. با توجه به اینکه تاکسی وسیله امرار معاش ماست،
این میزان سهمیه پاسخگوی نیاز رانندگان نیست
و هزینه سوخت فشار زیادی به ما وارد می‌کند.
شهرداری و تاکسیرانی
نیز تاکنون اقدامی برای حل این مشکل انجام نداده‌اند.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/463274" target="_blank">📅 22:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463273">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b65d69a311.mp4?token=ElPz2BmJwSW8T2tRBMgxUUlqpZ-EmhAP32k8PTXP4Mdk0v2pv2m1MDqNgqpQU87igPiDZ-iN-9l2L0cx1YA18RZgGg3nNWu-Da-GBb-u3M-LM6-wg0rfd3ROqGwd1kb8AvIdvSmbTlnt52uo2KMV7GX_vWQxzb-RQfC5uFXT6Kml_SuHpQHTjIkkQ8hFZ-cJh_XmplYH-CPhdkRGoa48NPoxaknU0R_YbP56UQ-lAVWNxAzUJflYuMVAa7HUYtP_MIi9cw9aFdeTa7iQbRYyRvQT0nGZDObLVm2FA7EOVEg_hKIpyaEdpozwQ9cIzXFeN-QkRkEt0bKYGESg6k63zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b65d69a311.mp4?token=ElPz2BmJwSW8T2tRBMgxUUlqpZ-EmhAP32k8PTXP4Mdk0v2pv2m1MDqNgqpQU87igPiDZ-iN-9l2L0cx1YA18RZgGg3nNWu-Da-GBb-u3M-LM6-wg0rfd3ROqGwd1kb8AvIdvSmbTlnt52uo2KMV7GX_vWQxzb-RQfC5uFXT6Kml_SuHpQHTjIkkQ8hFZ-cJh_XmplYH-CPhdkRGoa48NPoxaknU0R_YbP56UQ-lAVWNxAzUJflYuMVAa7HUYtP_MIi9cw9aFdeTa7iQbRYyRvQT0nGZDObLVm2FA7EOVEg_hKIpyaEdpozwQ9cIzXFeN-QkRkEt0bKYGESg6k63zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از شب اول تا شب ۲۰۴؛ مردم هنوز در میدان‌اند
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/463273" target="_blank">📅 21:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463272">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/320d035b7f.mp4?token=hM2HsAEYff2WWSnxdK47JwZjCZsQRUbmxZFoHjCP1omekzrMl5kda5TYUCe-XfBJoCdr82YsjrM9-hoz6pCsvrV8vqWsn7YBikVpKZpZscS1ok_oNl2nFUjVMxpedBlG-JgfI9UWZXp9t4jhofYyI-rIMdTkVum3h1mg-Snh2vs6N-FSyn1nQhXkSxjz2KzRmLQ_q0SBZleGnHblk-hmcf13Byj8HB0W9_Psfie4P7T3hjVu2F9yisg8NdzV02uz74mLziI4RIHyo-GU_ePr5Iqlr-N9SNPEt80w-X0JUr40Ve3S0sHCOoUsiUVW-gwUmsJFHLsFhMJykSzGn_CuuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/320d035b7f.mp4?token=hM2HsAEYff2WWSnxdK47JwZjCZsQRUbmxZFoHjCP1omekzrMl5kda5TYUCe-XfBJoCdr82YsjrM9-hoz6pCsvrV8vqWsn7YBikVpKZpZscS1ok_oNl2nFUjVMxpedBlG-JgfI9UWZXp9t4jhofYyI-rIMdTkVum3h1mg-Snh2vs6N-FSyn1nQhXkSxjz2KzRmLQ_q0SBZleGnHblk-hmcf13Byj8HB0W9_Psfie4P7T3hjVu2F9yisg8NdzV02uz74mLziI4RIHyo-GU_ePr5Iqlr-N9SNPEt80w-X0JUr40Ve3S0sHCOoUsiUVW-gwUmsJFHLsFhMJykSzGn_CuuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ا
گر قرائی اسرائیلی بود بعد از ونیز سلب تابعیت می‌شد!
@Farsnart</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/463272" target="_blank">📅 21:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463269">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ti-wxrY5NfdVY_3QiQ45Glnq-b36CEeTYAcGwt6aeelKGEr9a-7hRgL14b-__-YBomRv946d29JxHsCPEMgYyzwJZtDEtNrV4uzVo1AMpdFgfwumC6PbeElrxBOjxTN_VS8XgU7TKBx8ZSODcZJRbUyS0NbkOEpJZ8dKYvJ9DUj9chJBrvl2ldE6QibaCutvADkNnBxge5aVrQRDEgQiZNee4NfEhAJzt1xFxYIaD6yvSfUEajtjXFXE8Ff6WIqh-V_SN5xifcD_op64IK2B36ma05rWABxU2jy3P2qFAO6anY0NmiHjfQpT-MREPjJQKj2D4aG_wT-is8RYxe9PGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nPXj0EtnEGziS4mxJCU5RzQWb2dGsFyLk9bAOtAuexA0zteeRczXEPGPZvfnMcnq668Nw6Icb-gGLWl_y0ir21dbLhSCHz9DX1FYOixLw-1CE1vrEM6KUbKOdBJZw-wvnmIQFRZCpCK1gXCTRkc_rVr0uFWjqND3iZrjDUVsEF7v0Wvl2Mr3HyBc_YkaJX2yne3IaPYmuUFokbeUbQaw1waQlc_F48DpxyBLcBe5xzJ4cCm5qMTT7tzxpZhzNmN2J2o0zRbPI3COXPsudDwxohhWG2tjYIew01I4Xaj5EN8UykVWpOc2X6nO8zREYp_IqawmkoGHI3KSn63O7yEgEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jhMqk-7EYhaE_5RQFS935E0y_CcFGqMBaMr_HL5WdZrskk5axr82cNP2cHNA-NUD-nTF5BTyhh9mxKo8CGb0UgOVTx4AoqgwYvAjshtPnPfgFFPEjPCcKEKF1K9By66-OjreJtsE4c3D6ELhMQIpy7Hcj7nnLpC3i42jszllBZf39UsRRbI8JlapWL8WaZPQ2ObMwud12cHZo_zftT-Z6MvvLNgyXxvbF48konDucNL0T9kz5oTABvP2_FRn0MIIPJyDAK7lTJifHRpEOczgqGA6fSQc0gPQiVFMlqMNhON_-FV35EmYaPSQKeaUR-TyupQgVKIBXZ53MRnE6VGlPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نخستین تصاویر از ۱۷ اتوبوس آسیب دیده از حمله آمریکایی‌ها
🔹
سخنگوی شهرداری تهران: آمریکا با تعرض به کشتی حامل اتوبوس‌های دوکابین شهرداری تهران، به ۱۷ دستگاه آسیب جدی زد؛ اتوبوس‌هایی که برای خدمت به مردم در ناوگان حمل‌ونقل عمومی پایتخت عازم ایران بودند.
🔹
۳۱ دستگاه دیگر از محاصره عبور کرده و در گمرک منتظر ترخیص و انتقال به تهران‌اند.
🔹
جنایتکاران آمریکایی با زندگی روزمره مردم ایران در جنگند؛ این خباثت‌ها عزم ما را برای خدمت بیشتر، راسخ‌تر می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/463269" target="_blank">📅 21:29 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
