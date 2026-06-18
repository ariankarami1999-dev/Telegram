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
<img src="https://cdn4.telesco.pe/file/QaoBuVEt99TBzrx6dV-H0yO5HdA8xW7baC-_WwLhwodXWBpHTCyZILZFrbxYwmldB2jwWKjTmOgGXLovN5UzrxMqPG5oJbWwMjRgXnnVy6D8WzIWyRZyIG6z87rNv5Bu2SmxxhctnfZhvdLdEEh-jr_Ob95MdO-lgCPHE-V1f822Bl6A0liuAbiA7RaaWhfIMRhZf1PnEKULEYxLtT6fkLjhMZ6OIREXOkalBAZ6Hbrr7wQcdgpgxuA-fYmxqNvXtWIQbTSi9dwwMRG1hFWuDYa4DkrptynwXXUZrGZ0rjV9_boP5GJzjyiTVmeQ9HPmignyS6-veLKQ7WMeERPCoA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 170K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 21:11:13</div>
<hr>

<div class="tg-post" id="msg-78217">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پی دی اف جدید مقام معظم رهبری در کمتر از یک ساعت دیگه منتشر خواهد شد  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/funhiphop/78217" target="_blank">📅 21:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78216">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a862002bab.mp4?token=HMa-hmv33eHIqF1AeewIieO8JSzcjNPTV37-Qud1Pg9aegWab25s55QxQl11AnXDWKNoIyFGLTeTa0Tj3WqVS4wne1zYjnLRgs6RDzqFtgY-w73MI9d_ANepqFnTGzgeayvq9_IoOIQcQceWqEUDaGpT_3PI2a1P2dXQkwTjnyZX9_jZXsyPAz_VebuJwb1iOzepQTRlYWy268l8vKJXS4IB9rrJV8pnr-mdXD2FeKyqRSSJdHicCI3mCgTKM3oOB4stpBisr4cwSYxRxB4plOHtVJYaUJGL2y2TzHIh2_wvq4aJDHL9ylXv1xwyWZualOJfIy5FbPaBmEzeUXRtcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a862002bab.mp4?token=HMa-hmv33eHIqF1AeewIieO8JSzcjNPTV37-Qud1Pg9aegWab25s55QxQl11AnXDWKNoIyFGLTeTa0Tj3WqVS4wne1zYjnLRgs6RDzqFtgY-w73MI9d_ANepqFnTGzgeayvq9_IoOIQcQceWqEUDaGpT_3PI2a1P2dXQkwTjnyZX9_jZXsyPAz_VebuJwb1iOzepQTRlYWy268l8vKJXS4IB9rrJV8pnr-mdXD2FeKyqRSSJdHicCI3mCgTKM3oOB4stpBisr4cwSYxRxB4plOHtVJYaUJGL2y2TzHIh2_wvq4aJDHL9ylXv1xwyWZualOJfIy5FbPaBmEzeUXRtcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظریه داروین درمورد تکامل انسان
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/funhiphop/78216" target="_blank">📅 20:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78215">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">محاصره دریایی تموم شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/funhiphop/78215" target="_blank">📅 20:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78214">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پی دی اف جدید مقام معظم رهبری در کمتر از یک ساعت دیگه منتشر خواهد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/funhiphop/78214" target="_blank">📅 20:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78213">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYji21JbIu5BQbdj27Gy1USRQGyFQyr_f2wIJ6mRo0y1xFfhQI6R23M1F0JDUm5PYuYpSaEhBeIqUPtzkNYEzX1nn5Yvgw5g_7ox8h1sQsIlX8PqxvLHE_M19CiLlhDRjyEaQZd9-gvYuniSqqjXKxN1PJra20ehCinwBhF7JCueBFnBrZIgEmLjm3xVQdDOo5_99iABcsRfpt4vOIgwFXUJj0dcVjPZb7tdc-PzOoBXkZxNnR6KdOYJiMoJREpJnKppQBR_BkqLn9Dm7jgi5G19jS2nNEGr5HPqMZQ9NyVMzsmNMTGDRp7RI_WJBnvhrq1mC_m1nYPfnLmkZd-UJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتو جدید ممد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/funhiphop/78213" target="_blank">📅 19:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78212">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7_FEa52T75--2v6nyTSTu2MeEPNNwF8VjUrb2LCEIFYz9XMYF6nktQ1di6V4sDgpwDFRm5BfwWTv4BhyxamqR7Yy6XRe6tdjX-yjo4cUh3KAPC3yi1PTPGLtjswQm9fPpIi7uUgTt52qZpEWIDRKijBYRZ1QnsFaE-MaWBFhS4pxOYs_i8YZu-6Db2K7AKtL2F96Z2rBUGmg8I2tbtiFwzdPH0XpzISoVaskgKUZjSfLIHnO8pcyZ75J1r-yWzr4hjPJIpfBaGYN0JmPTfd0rolXnagQf5PYYZsg9tUmp3gaTYako6h_8BWeHTl4XVkEvaoapES7P8H-5IBs4AdNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری عماد قویدل برای پوری
@FunHipHop
| Behi</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/funhiphop/78212" target="_blank">📅 19:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78211">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klkcTpO8l-FGJNXt2YJXScF4aBKKfrMohhc1e7IErt2UwmkOUsXpD-PVToVIUgexfJjMC6n_53UxjA7zWeBCEPO-Tu3Jgh9NxgK4vO5Q7XlFwPMq59wHLIEWMX-IqX8oTR-7gRY1-59Ea2ugzdVk_48LL6VwPEu7NE5Wtu_ZaCm9t55DigK0bROjsQz3aZtdtGrcn4ST2EfjU6864dJjmVfoFG1_bqFIh7ZdcTNz5YrYipkZ8BOad3ANG0qt3RzUvS3PorBI9CfAYuLLuEHinXIwjDFFfY2zl6kYrFVJ4Xjr7xBqx0qcxSfb0Xy5MqoFm_lZDa0ZdW3veEeRfwBvCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4 کامیون ایموجی خنده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/funhiphop/78211" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78210">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تیم منتخب هفته اول جام جهانی 2026  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/funhiphop/78210" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78209">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/es8r1x5eQ7Yf7FeeDWYmYYEBR1eN3gfpAQTca0g0WXVeEPynVj6ZT-1t0iJORTbEy7eOJQucK_iwOFyCzp4J45h2BvhjX7ktyhcbOPwWlul83CdDckRsNl7pcKvjJJ3gLhE8MJss4L_Lo17jfL6ssoCl4-DMksEzpky4yIX2STqeQqqM73A7HB6ZAIYwqfSnsqSbg5s65fjRyFYmkuYPCRxS3sRZktuIN1IexwKH5osImKPZY7kGXJn4WL1KOQ_ERibT4qCEF66ljB4Ehv0z2crO1q0_Zxy0Vr4fRE4706CD1cUFcxIQgz_bfTlesH7JBnH0Kay_Wktiw83wWgQghQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم منتخب هفته اول جام جهانی 2026
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/funhiphop/78209" target="_blank">📅 19:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78208">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTGFztXsyUYrrMCOdpCQOphlUbIsIvPW6TOTiAawqgSA89D4XHbWRBnHwml4LDwmN7IcwFPcHP115Dd589BGNOjhVpHVj5tBxBBSIW-sFQNtlgCj_xphUeL11n4znqcrQVI5-jK-Fata6zU4GnQDXTYP79DB3ou1W1nUbobXM6rk8fq3SUS5bsSFSLMqwBd24uspCtGazwT8ExallQF-fQGLucD3Owv_hi1GUkyWDHpKJlUTD85KzXWnQY97rX90tDd_0COAGo_x0T9KeVX0-vq_nct-R3HyygkmHT-PMIS9efhfRuR6gMTxBomGTsStCC5E6HOHZBIfqwVuQcRSUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند ساله ترجیح دادم پول سیگار
بشه غذا واسه حیوونای تو خیابون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/funhiphop/78208" target="_blank">📅 18:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78207">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گویا پوری و تیمش این مدت توسط موساد تحت تعقیب بودن
🙏
@Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/funhiphop/78207" target="_blank">📅 18:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78206">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5ce_3WofajfCIBtKLLtcEIWkwHz_WT9BQ93cfJRebhhPpGCTxNtahHt_1tvNCc_Zb-lJP4s4DOv5Kg_9ZU91PScRHBIWmx7BrRBu62s3552i72HFTTOAe4FzIbIrUs5HSeciQUxfdNYTo29SvvAPXXSaj5Ec4uqiHc-CDwYcF5sxr6KUiKUd2KTpqAseJuQ4L6VzR4tiV6zmsfJpINKPGVcd0tHEb_bGc5KDllh4Vp3VuEglwhEIn7biVin56PTOkxxSvUygfQVFWnqF7Ts6MLzn-cbLktlwSzc7cLP7NmwfbqnKf5RGl2urWExjFKz4GdeqOQz2NvMb04P662Y4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از عجایب جام‌جهانی
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/funhiphop/78206" target="_blank">📅 18:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78205">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLk</strong></div>
<div class="tg-text">بچه بودم دوست داشتم مثل رونالدو بازی کنم،
الان رونالدو مثل من بازی می‌کنه</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/funhiphop/78205" target="_blank">📅 17:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78204">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLfAR7p287HmiiGGT_nZ5mMBX3AcEIweRufz8vD7rMOYfajn4NjBXyWq1jIZodcE909PCINcHf_vvXJO0n2-21FKJsncOkGnfOHvaQ6TLbPpxM0z7JMJ3zOBzLgYmuJ1_1CY9qu7bDLkXE5DqmfH21iY-ZdZ6K9LVINbcJ3Q1ZPln9cp2-reZc9kZhzUQl1C9zr0zLU4P07NbIADHemGsRcwxNoyT_F2pYVh6PvS_WZqx-4Wmoo6qlmKBbme6h4FRnrHwJkSGa9uF9rq-axVTU0fqXenaUrBYMVcq0dKUWtPt0cOGBdhZ2jAe0pFW9CQFQMpdJiXYq_S2nN-GGGsrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای تاپ دنیا توی اولین بازیشون درخشیدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/funhiphop/78204" target="_blank">📅 17:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78203">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/funhiphop/78203" target="_blank">📅 17:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78202">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUBkEKmuup2RSOaeLyJb0203MmQ_rTB7xbTFNM2orHSfmOc0niOm8dmdTYs9kIGh9x3nA3uHAHyj29C1ID4h1Y4trGdMwKwFmkDRj68mruULvZb3TN_4OZeDMgU7vK01oGF_C1Ngs_FIUf2qsR3CPRUna6nJBQYWzUv-YFB-OBvAsvtZ1ZpVOVTrQ1gImHogP8tSOqr2fTT-bhPGcV_jideR8CXm7YbUnr8Pj7_Gzelpy73jopglXyOumI1yzofNJemPpy8fRtGViH8NpDUkCHkroHMPvU-eerhGhKvQtFRNzyhSNvWb66VtK9Wml0OaZ6D6Q9pqi8X8EVy0wrjrtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g28
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/funhiphop/78202" target="_blank">📅 17:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78201">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گویا پوری و تیمش این مدت توسط موساد تحت تعقیب بودن
🙏
@Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/funhiphop/78201" target="_blank">📅 17:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78200">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcWHF6U2d33jU7hx6_so7SX0xaOsS_vVe0KNJgrmQdVWf3xV08K8KmSx381ZTmljzQ4CcIh0VAyZ6Gzj93nwg0WoJhRqLE9IqMQObdtXq7hJA6qla5UmaXR32A8nShdcwr2BgharRPIGXnsMeiHQxb0Y3Y290JwAIkzk2DAjQwh6FrG91dsaeo1OJuupwBdMWKnWiXgtTifIHhiddlcqI6iPVG_SlSb7XJ0GDoPE0YnDQ2rH4WKLtWTcShHPjZ6mqy8Cmc4jzI563stsRSTMxLo89K7-BdlwHMH-4dN16UW9EHBImdKBPw_q36WOZs6kU8peCd95AdJeYTAmKsWHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید پوری به اسم سرپا ریلیز شد   YouTube  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/funhiphop/78200" target="_blank">📅 17:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78199">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9sP33XgGu-mO2KPuwJT3gu_b0_tGiOzr9EfXS1-8jhtk_2THc8ovhfXTfeezDi8zLUsYPt2fCwXT-hHwgktwWFzouuLDtt9leEg-1pD-d2Ik2hjkx7eUoPxx9upb7B7ssWma6MGNNMyhN22WbkbOD-_XiABM2Z9y5aHf71I1sTimqSaaTLKpeFKM65pEbU76FS-op3-c2BjUeo7eRK8FCOSl7qY3S4R_1FnXNVGSpVu7SZHjeV4Uixb_PqobjlYeAu6fnoh0pPmTJlAIzithSwCJpz6BwCJTwbx8zNT4bq7g7xU2wNguaGJBSRM41X3bNSKXsyDBvdzO1U1iM31wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید پوری به اسم
سرپا
ریلیز شد
YouTube
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/funhiphop/78199" target="_blank">📅 17:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78198">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وقتی مردم ایران صدای بمب‌ها را نمی‌شنوند، ناراحت می‌شوند؛ آن‌ها می‌خواهند همچنان صدای بمب‌ها را بشنوند. چون آن‌ها می‌خواهند آزاد شوند.</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/funhiphop/78198" target="_blank">📅 17:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78197">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ: فقط مردمان دیوانه میگویند کشورم را بمباران کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78197" target="_blank">📅 16:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78196">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkL1vzH7L2uoN3Stf9u4dr8SKvRDJ5ys0jo6SkFhqD2_HXGc41sd7VfPemHYBbSpcji9cnSc3HGf3v9RBT_y1XQiEFJ0I6JyEOn1rPNlCmkitizQtT4H4uKfxXnLLug71B-t3H3AIlbcyW-GdkOpNtcdtit1Xlz6s2eHa9BjLuaEQMqRBqFd40a4rIzvt7LV4TTtn4fnwoFPQkXo127DkIXTSFSSsdA_erCI6tDv5nMZtgvSonTuJvNotIcTsbC5tEFtPw4PcT2IHPhHs1fHTgTKi9U7pQxN73YArv567T0ynP3l-BU3ifuByoUIWW8P_O1HhdGO0lg8w5_wK0gAOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/78196" target="_blank">📅 16:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78195">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoouhXvwCpLgT_QXJLwXBDEUoZLXwqTtlGAk9RHwW3Q-Z7oJ9S5Rj-Sp1YIAtTwu9nQ3whPgKxzhoeWQ-csK486M8To6FswHjDT6PZV5DsBI_fPBd2CTW1ORpNbNRBTpLkufEwc2Wx9NXK5NT60Y1EgdPXHlYRLniLXKqLbeNiYHWjKbpeT_kjZbBUdZT4kTWLTf0FV9wG_TMe7_lycVtC5fvBgleyQkCxaHgKz7LubogtiPa7WMo-X-L46Z5zfItnrLwyqC5i-bjZt2f7rdsIofW1qxbZdFbOV4LLEbTTgFe6RVdlb8399Wzt1Fg5v0DlQIlENehGevm7jIIreQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سنت خجالت بکش کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78195" target="_blank">📅 16:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78194">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پوری میخوام برم بیرون، سریع تر ترکو ریلیز کن یکم بخندم برم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78194" target="_blank">📅 15:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78193">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromuıǝssoɥ pɐɯɯɐɥoW</strong></div>
<div class="tg-text">مهدی واقعا افغانیه؟ آگه آره که کیرم دهن صاحب کانال که یه سگ افغان و ادمین کرده</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78193" target="_blank">📅 15:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78192">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06ef661660.mp4?token=Ajfl6hcaEriHaSgMYasqSXao2_dycloRda1toKaTi64bpJxiJjrXbuRXLK0ukqWJWWz7OhEBxB3uk8jAwWDMyA42tP17DndMyiiNNVz4iSLU_mb1rNSNwcUxBi6IQpJH0en8dWtQBQkX07mSkSO_DESPnKzZEt6ftJl9Uc3TcgeevTiavIGAKLJU7f3Y1NjLM1MSAmh5kmHfl7r6zy1BEkqtCixjg1NwL6ipq4HN4pFEYOPBO2ysUgSJGXbpRJwwPpqn3yZdpDbdrkgP2u8VT6a_nd8LYfca2G9PexKaZsDhGAyPTU0-2pwTwVo3Ej2qbp-BI5wj1MCY6fdeMS-nIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06ef661660.mp4?token=Ajfl6hcaEriHaSgMYasqSXao2_dycloRda1toKaTi64bpJxiJjrXbuRXLK0ukqWJWWz7OhEBxB3uk8jAwWDMyA42tP17DndMyiiNNVz4iSLU_mb1rNSNwcUxBi6IQpJH0en8dWtQBQkX07mSkSO_DESPnKzZEt6ftJl9Uc3TcgeevTiavIGAKLJU7f3Y1NjLM1MSAmh5kmHfl7r6zy1BEkqtCixjg1NwL6ipq4HN4pFEYOPBO2ysUgSJGXbpRJwwPpqn3yZdpDbdrkgP2u8VT6a_nd8LYfca2G9PexKaZsDhGAyPTU0-2pwTwVo3Ej2qbp-BI5wj1MCY6fdeMS-nIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریچ یک کانادا و حومه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78192" target="_blank">📅 15:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78191">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">راستی محرمه، پرچم عوض شد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78191" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78190">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">انقد همه پرچم گذاشتن جلو اسمشون منم تصمیم گرفتم بزارم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78190" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78189">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzWx0ASdcNHKPRUsBJdzrv-JbU8GVCY5mKgfngcJq-jD-icQ4mlR8AiwtrerV3vBc-DcfLJnpuMlpQPXqPwXfiO2CuZwbQInLRu2wc8ettzWS3hxclhx_VNzP1oxJjMkjmcyM0Jfsbz7K2lu8jgrhtAJ2MqspmDhtkkopwo8UCDIn3zOfXtRE85AiI3nhDzAcQC1dkcKtERNl3fnm2PRR-VYkm7W4E-t7M8wp4zaOIbtFiVmoOzeEMuOPpKoalTfLVaYGtD8dplZlp0fV8j_SQx487XsTMLeHo1JwRBBixttSFri24HmD6XW0zaCdQAgM7OjzDelMygIoC7LfWpV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت اوردم براتون که توش میتونید خودتونو درحالت امضای توافق با آمریکا قرار بدید
پرامپتش:
A tight close-up mirror selfie, black and white, grainy backstage aesthetic.
Subject 1 (Foreground): A young man with messy, sweaty wavy hair. He is wearing a tight superhero suit with a web texture. His face has realistic battle-damage makeup (cuts, dirt, bruises) and he looks exhausted but calm.
Subject 2 (Right): A girl leaning her chin heavily on the man's shoulder, snuggling in very close. She is holding a small retro silver camera directly to her eye, covering half her face, smiling.
The lighting is harsh and direct (flash photography style), creating strong shadows. The background is cluttered with a hanging white t-shirt and messy towels. High noise, raw, candid snapshot.
‌
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78189" target="_blank">📅 14:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78186">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کصخلا فریب و فرید دو تا انسان متفاوتن  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78186" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78185">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کصخلا فریب و فرید دو تا انسان متفاوتن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78185" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78184">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRrrLIu_t9V0ipYxgZWzOgYKqknhNdBrFBDC3cXiprx7L8iVpS8uoXCPHS9IXAEy2_8ZFrqJKmjvWItdcq2NaMEMyDZ9oF0HIBuCZEmFIaxkARx8u4T-r23BmhqT8vH7u8XJ90W0znaKRFljYqi3vSfFslNuy-uaCtpkme_--IhOjubyYPc-Al6L074xVYrtj1hkbQVKMI2WvwNfxhr2ZwjO6e_p4zsHsH7PN7xqoBRx6s83C5n3VIjDtflh5vePvDyfl7edKgfPiILon0iz1dSOlIk6KxjHBNw6YbDlegujJwdxYNMMC5QKjVpJuxcTcM1C7k-DLUztMoNqUKpHQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78184" target="_blank">📅 13:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78182">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خب دیگه توافق هم امضا شد و مانعی برای سخنرانی مقام معظم رهبری در ملا عام وجود ندارد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78182" target="_blank">📅 13:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78181">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78181" target="_blank">📅 12:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78180">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTP-r8sCFQOWFLlrvGy987yHhuIO4Yty8gMIlLQJLQ8JLAJl9sZSrIntvH1fSJUm8O4PXjcV2p_u19r9FoQIvscrpTd2MK1nt6orlv9Lm2aCWgOOVOzeXMKik7m5tkquN-mdpM3bPFYQxYSgYgg7OOwmppwYkAdUmIQ_OGLTrrcnQ5uhJ5RDrMSQA-SGt7JLITOKl6zVfFbSnm6n65BvQ8AGmtfMwars_R5FocTL08sjmotWCUUfrG9H-YCTpeM4pfN7wTqKTPY4CoPVo_88yEPyveONIk8-Y1CiVacycvFwjH4Z1zj52Ohvhi3OHTSD0xOd1P8lduDtZzyASoC_bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78180" target="_blank">📅 12:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78179">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">عرفان چطوری میتونی انقد کصشر باشی داداش</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78179" target="_blank">📅 12:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78178">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آرتا:‌ کصه بشینه نمیره عین جمهوری اسلامی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78178" target="_blank">📅 12:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78177">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.  Download Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78177" target="_blank">📅 12:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78176">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.  Download Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78176" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78174">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1Zn4L-ynMzwYeXNF906DNMPNOQCDe3i1n-vIOB0c_KTUQFQ9dnu-og1kA8gIghCenW4TEws9n7pUc1izypt-izxYIl82KhqAxZv0ePqvtao1MlJZ8PnXPgRccNq030D8QsuIPQQ8eBJK9SCtNf5G5e-r0iMVd_IWdy6F-AFEVLpjo7BOQSvGjrremhtqfxpJqX4-8UNude0uRwL5RocedAtjv193MCauP-6SwxApqR8EQWhfzr9gyzCyP289OZ7qMQqZsg8NRjW4_dgGB02gW3kPl00RWZKAVyN48RBLV5z_c6spG6pKq8rENEqcB1Qo5r8DX1-0xGk2FY-Yoxf1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.
Download
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78174" target="_blank">📅 12:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78173">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آرتا، ویناک، عرفان پایدار، کوروش و کچی فیت دادن</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78173" target="_blank">📅 12:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78172">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QR2UyC3oC-WfLjc66jQKT3lXsToqmTsQDh6TRmWOteJvBn-YW7cMbn3wDdgMxZzVt6YADo81SK9zx1_PZtz6wn6K3p_KQ1liuIhPjMNNw9zsz6-Mqt1kQg85CHIhQPFZwZLdxv-RPi5irj5MiLY4o9EXhwdqkBtJgSK1eW1fOVpbXDbFB1FG6u9eDTKUHdhhs2vyKScUmPLaO7HI98SChbIxsfLFiswYbaIkNvXyVwoOGDxIvgYLJw7EYSBMGOxPacWpVL2ELriowSBC63jvEhVbGukQalLM8c0uBgyiDkQolaljCURFtgHnyeEX0F8dqiK0p8dlS16bMTKQk6gkCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرانی بدون خایه نمیمونه، بالاخره یه جفت خایه پیدا میکنه برا مالیدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78172" target="_blank">📅 12:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78171">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">آیت الله سید دونالد الدین ترامپ(دالگخیز): عادلانه نیست تمام کشورها موشک داشته باشند اما ایران نداشته باشد
آنها باید بتوانند دفاع کنند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78171" target="_blank">📅 12:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78170">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رائفی پور: اگر میخواستین توافق کنید قبل از ۹ اسفند میکردین حداقل رهبرمون زنده بمونه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78170" target="_blank">📅 11:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78169">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رائفی پور: اگر میخواستین توافق کنید قبل از ۹ اسفند میکردین حداقل رهبرمون زنده بمونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78169" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78168">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شاهین نجفی نوستراداموس   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78168" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78167">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40ff98049.mp4?token=VyZQRhuZTcemndxh_93uJc4Qx1OFkSrHs8vWdB-Q4I9o1LJrzj7szzJPV2VeOs9hSq-XJn4BBVY0Cky5YVpLevEG2h1tjYCcrV3mv-XqtLZW5q-AllRicalg8BjROg-qS-P9NmJ2UezZQJioUF5PgfW7H8uGp4pwb1terfhzRSBp2SAqXALzE9i6RibSc2704_C-_dcS3SA9mhnvu7hiGc8ns3oVf9xNFQQrC-rjy592TLS3wmWuqD1nRqaLZ6hVCTBveqZXOYaero0PCFHhpd14PXMNCFh_mtBCXuJGWt8mNckPgdvhqjG08Cbvh8-sN13Y8cninWdBwSLaGK3HmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40ff98049.mp4?token=VyZQRhuZTcemndxh_93uJc4Qx1OFkSrHs8vWdB-Q4I9o1LJrzj7szzJPV2VeOs9hSq-XJn4BBVY0Cky5YVpLevEG2h1tjYCcrV3mv-XqtLZW5q-AllRicalg8BjROg-qS-P9NmJ2UezZQJioUF5PgfW7H8uGp4pwb1terfhzRSBp2SAqXALzE9i6RibSc2704_C-_dcS3SA9mhnvu7hiGc8ns3oVf9xNFQQrC-rjy592TLS3wmWuqD1nRqaLZ6hVCTBveqZXOYaero0PCFHhpd14PXMNCFh_mtBCXuJGWt8mNckPgdvhqjG08Cbvh8-sN13Y8cninWdBwSLaGK3HmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهین نجفی نوستراداموس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78167" target="_blank">📅 11:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78166">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9ksiEsuKYAqoWEicxPk8q_wdOCPIJsZ-8DVHODUW8Vj_UR8K4lpfsjaGKcoCsHKK0vlKFJLBdvXONARR1rjIl6YhIg9h0UeJjY-737DQsQlupiAsHNqp3qjf_owHkH0xK4oOXaQZPeNeB6HnxSq38RSz8xF6cFwRs2L4xC6Z9EPWia_S8Lb6OfRZ4onJSMCNfmgdrqYJfAl-1wk9F8ubiWuEIGA6IdlKYVoc-DslAR7OT-NSpnakaxxtEPxcXSPIKEsHIDmlgxdmSffK8uoP5X9WyiSKEexaf3vHfcZB4KXFlkICCsO0g68nxhM7y-Aoe5Tt7f4pwIFCaD_1iHeoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین ها درحال درخشیدن....
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78166" target="_blank">📅 11:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78165">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/funhiphop/78165" target="_blank">📅 11:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78164">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNxV3p2CIA-XYfMtPiB074iYdmAoXvoeZ_EmrCTyHPDctCdNMn__RjyV4am0zBBMIe0bTJzou2xK9mFX578Yh1UH9EEjpzLHrT4XOF047WFQHhamwfhQXUHs5y0UFePle3iHeLCOgdVRXsGTqY8h98_q-kELvVE6jpUd0zTWoaZAN5q_2ZD6X-7DT34LbQQ49hHe41jDWuH7gfyg9LP6C8PAQmHMCzt4JshLzjbjuOLJK-IdURFoGKxaoTYKNhM5e1ZNHh9vRBVqnST0heKnQ3kXBOmaYaqWOIA5qlDFKe2ZqphcImK3ODXYpU8qjo3QQvBx6yEGONyLKXsb9dZggA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r28
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78164" target="_blank">📅 11:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78163">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be730c80f1.mp4?token=erwvDhcrU1mbT_WLxCwZITn-jLEwKC76aQcWeNoVxY-3kaZTi9gVwf-AAt1z9M7zFNuctLtBUq9rLB_nhA80xVaw3Z9rrUPnxvELkVzvErOQqWMWrRT5l0ZrDZbp9tVAGM8huWhezFQXcCqC3lBQkG2ENuTyfkQtKlLDBNbOCIazmfHTzv4YRodACtBT3fkOqite9dnT_vps5zSGhWf_jh_bWmKe6wqPiT4JCjhQHa-2I_QKZ64HvtF53bRfvjhVZSFiPPFGaENJvjkTvR5-GqcJErsomZw9XKX1w3j4dJMzl6NcpYhJHdT1X6l5pw4IQpNYorOKXDH3Mu9X64A-cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be730c80f1.mp4?token=erwvDhcrU1mbT_WLxCwZITn-jLEwKC76aQcWeNoVxY-3kaZTi9gVwf-AAt1z9M7zFNuctLtBUq9rLB_nhA80xVaw3Z9rrUPnxvELkVzvErOQqWMWrRT5l0ZrDZbp9tVAGM8huWhezFQXcCqC3lBQkG2ENuTyfkQtKlLDBNbOCIazmfHTzv4YRodACtBT3fkOqite9dnT_vps5zSGhWf_jh_bWmKe6wqPiT4JCjhQHa-2I_QKZ64HvtF53bRfvjhVZSFiPPFGaENJvjkTvR5-GqcJErsomZw9XKX1w3j4dJMzl6NcpYhJHdT1X6l5pw4IQpNYorOKXDH3Mu9X64A-cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
یک انسان خردمند در ژانویه ۲۰۲۰ گفت: «ایران هرگز در هیچ جنگی پیروز نشده، اما هرگز در هیچ مذاکره‌ای هم شکست نخورده است».
ترامپ:
این را چه کسی گفته است؟
خبرنگار:
دونالد ترامپ
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78163" target="_blank">📅 08:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78162">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpwqPSlS0qXxZ4v_ywIDB_ZYo_lJXzdbn8dCj2Cbpte4fVBe1BF6opsdXkumSHtqzX-mejff9LiZbL4Nx3YwZv_37ACAymdD5u5JQaDkpMGE9aXejmiLnoWkReohDWJ9QDdQ_JspZYrnTM4JGMKKCwJyxURSYO2C9TVG8Q2-MIZsXcWFndfYPigOEeAcoPMK7DKu0eQ_LEFxmspxsbXij9Tax2TnJ8wPpYkylzL8ajIhqZ9Gs1QC8YSDRdZBF_fYhSSY-JqSZB6rf3-OfYXtNCnvdv9wSvkkqijqvnrPzY8C4Wrt5c-d1U6icqWzi2Av9OgGAvyYxysDvtOr9GtV_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78162" target="_blank">📅 06:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78160">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfFVpHJnEJUZMxXNyjFK2Fk2A_owHIwYm-0KYfp7dUrSX6GRSOiKdcqCHM9O6zkPncImPvcX_6xm889CeptQPPiTolQrMc7o61VWI1DgiR2YdDOtDwJilFs-DYHx--OH7MvwmGTN27MqUSXbFGqaVLsV5lqlUcqCVuwTTippzHuaN68C7dBJ0dCx-G3d7ERQhsckeU3DWVTAPOl26ZuRdbNKheEjOOJ7_8XvdYJSj8lshFsIDtPeGmNcqPTXjFKkCL4VfhoSO80H29PfwqChoG-iWUoqmCKd3rnBiPYyTuNoLSkq7pqXD165A8DcfhndIW4_3z4CC2Fzz4T57z1tCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gGjYPphY-4K7TX_LF9xnyLYimaURs_qniLMwZFBeipR2GoLgWhn0kIJzPwmIV5CWMF_HiKDYN1yiWL2qA9Lzs3QwC8o1kQ9DOMn2zw_G8QLXa-4Vx55K4XYbyqzB-SQ9lDEwmPukE2xGkCizYnRl5qBb9lW1KBDSNnZRfX1UyaMMcUC6bL-DtqOjuObpGvrWfAPKRKTw34WyNCIsUzUep_4_ttFZgVhbDgZIGJhlcISF-5gYyQt3IrwQi74lCEkFbiNGGVYKSoK_MlLaA_6GSRAWXdQ2VWJWsQkt4TQ0f2A3jfla5WfCrakgF8wgHdP7_97lVJtQk5MdjmxD61NnAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78160" target="_blank">📅 06:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78159">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">جی‌دی ونس دو سه روز پیش اومد گفت تمام بندهایی که از توافق تو رسانه‌های مختلف پخش میشه پروپاگاندای سپاه پاسدارانه.
امشب خودش از رو تک تک همون بندها خوند و تاییدشون کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78159" target="_blank">📅 02:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78158">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سخنگوی وزارت خارجه:
ایران دو قدرت هسته‌ای را که توسط برخی کشورهای دیگر نیز حمایت می‌شدند را شکست داد.
ما شعار نمی‌دهیم؛ ما واقعاً یک ابرقدرت هستیم.
روند تعلیق تحریم‌های نفتی از امشب آغاز می‌شود.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78158" target="_blank">📅 02:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78156">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کاخ سفید جدی جدی حسینیه شد؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78156" target="_blank">📅 01:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78154">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رشفورد چهارمی رو زد و تمام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78154" target="_blank">📅 01:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78153">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خب طبق بررسی های میدانی و حضوری تیم من در ژنو، تفاهم نامه به صورت دیجیتالی توسط پزشکیان و ترامپ امضا شده؛ ارزش قرارداد سیصد میلیارد دلار با بند فسخی که بعد شصت روز فعال میشه.
Here We Go.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78153" target="_blank">📅 01:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78152">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">میگن که تفاهم نامه رو امضا کردن ولی فعلا بچسبید به بازی انگلیس کرواسی این مهم تره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78152" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78150">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عجب سیو پشم ریزونی کرد گلر کرواسی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78150" target="_blank">📅 00:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78149">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بلینگهام گل سوم رو زد برای انگلیس
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78149" target="_blank">📅 00:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78148">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kc2oQDv6Hmhc05dC0W1DgUYFIYqaSD6umYcY5V9ivGDJoVeDtizXmrNIqURyDBKVPYgsIpKqQ1UXcDkQ3v4gCCTTl2vdujOYq0j8gSwMH7rAZqZbeJnRoRs0wRE4spZGjsPeCVVwmj5vmlPpNPoC4_fSCwE-j_gYx6rjNI5KAIABLFLNSSCrTwSLzrvNy8GBw6BiJ0gFfb6xtn7uLJCUCzQM8eT41BGIeKSdzUxOwWKTKk5KwGxbu0XYUSuAUIwUeL_1CdylSYH-w_j-Eo9tDPf68JcURtYPYCPYhxAa0hOrxRvadIhQOoqB_w15mGe3yQ4Y5h4s7ULLPKR9OMdgcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمتر از یک هفته تا منتشر شدن فصل سوم سریال خاندان اژدها مونده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78148" target="_blank">📅 00:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78146">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALizD4PsrMu66TXYmDx-AjpCzrGX9elsS1sGA7mFJtvq303ZSFR3PlT2vyqJJS9yMLRhdQaKWVLG0rSfcsRrg1lYHeZKfZuXFALZpYsGMDr9FKz1wAKj7cvN8RuLaBoKYDmwopsgefm1RTCzOLkDAJuNxSiTvr9FwZmoTqzMtk1hdPB4aTSvQqafVGtWiN8uMLbakAdPcRQpDtWZacn90Pg5IreW2l-jb8J-n3zbO3HQlBI_cE-DxBdgzsJGCJlNVeht91i1dYbd3H1ovGtjc6SsKfkie2q52PfnuBKjsHaCseAm7UHyrFHWHZa_HeJvwqFudmyufvB7aMclZqtcbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری مامان پوری از مهدی طارمی.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78146" target="_blank">📅 00:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78145">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کرواسی زد
۲ ۲ شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78145" target="_blank">📅 00:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78144">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مثکه متن تفاهم نامه منتشر شده ترامپ قمبل سیاسی کرده برا جمهوری اسلامی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78144" target="_blank">📅 00:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78142">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">این بازی داره قشنگ افتضاح بازی قبل رو میشوره میبره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78142" target="_blank">📅 00:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78141">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7dd58a539d.mp4?token=HhukWp4ywWsPjlQeTcpeE-uxhCwKraroZJaFxgvjLJt57ut979W4r9pTWi6tDUjtoj_0s9YtTPTiDLdq50OewetxHvTWbl8HJPbvLRVe9QdQd51NqvlbW2Sf4Ydz8b0PiI-KI-cMiymKyH-Q-F9JXg6UhDkYmTWCSL-vt-rhCEx4EU6uQ0Nn86zCAhOh3PJ6JpjF8KnsH04C2XsOSA_LXRGc8Rl3XoNQdF5ef6Q3DKjw6-A3DGRlt-XPYCFHGy6x3lFYvItZgdHgPfgOYZtMQ-_cKp-7eUWgYioUyGgVGpWjEq-497cLu8t-gj4QR2TaN_YcMs30uRyGs_Wlw0zQxw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7dd58a539d.mp4?token=HhukWp4ywWsPjlQeTcpeE-uxhCwKraroZJaFxgvjLJt57ut979W4r9pTWi6tDUjtoj_0s9YtTPTiDLdq50OewetxHvTWbl8HJPbvLRVe9QdQd51NqvlbW2Sf4Ydz8b0PiI-KI-cMiymKyH-Q-F9JXg6UhDkYmTWCSL-vt-rhCEx4EU6uQ0Nn86zCAhOh3PJ6JpjF8KnsH04C2XsOSA_LXRGc8Rl3XoNQdF5ef6Q3DKjw6-A3DGRlt-XPYCFHGy6x3lFYvItZgdHgPfgOYZtMQ-_cKp-7eUWgYioUyGgVGpWjEq-497cLu8t-gj4QR2TaN_YcMs30uRyGs_Wlw0zQxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خخخ:
وقتی همه‌ی کشورهای همسایه ایران غنی‌سازی دارند، منطقی نیست که به ایران بگوییم به طور کامل غنی‌سازی خود را برچیند به گونه‌ای که برای تولید برق اتمی هم غنی سازی نداشته باشد؛
درمورد موشک‌ها هم همین است، وقتی همه‌ی کشورهای خاورمیانه موشک دارند، خب عقلانی نیست فقط به سپاه پاسداران بگوییم موشک نداشته باشد.
بیایید کمی عاقلانه‌تر با آتها مذاکره کنیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78141" target="_blank">📅 00:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78140">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شما یادتون نیست ولی دالیچ یزمان کنار شفر گزینه سرمربی استقلال بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78140" target="_blank">📅 00:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78139">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کرواسی لاشی همیشه جام جهانی غول میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78139" target="_blank">📅 00:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78137">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انگلیس چه خوشگل بازی میکنه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78137" target="_blank">📅 23:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78135">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ: ما حتی ۱۰ سنت هم در ایران سرمایه‌گذاری نمی‌کنیم /از یادداشت تفاهم، بد برداشت شده است
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78135" target="_blank">📅 23:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78134">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fADEWqjjOjt_4S46WYly68cvbrRHvVXyd-yoEb0GYFZ6o_ET3eWPJH0dA5r0SoeryB34oHjfqe2f9JI-C4vnX35_D6t_yuAkY5P08RRJnI_O9ErxMNQcumE3rcrsdr6jFawCPvJ7cspEm6XkGEeoCwzS0l-49L-4ZRvPycn918Z4PBm3SVaWkBqt3_1IL5KSTt3KGSMLBkD-Y6pUYwWeh-XpGh1jhzHwPcNFxG-3qQPzDCAEhKfU0sYjLpoPkfTb6fNK1J2JI7VmsiXY00PDj_Zv2cLCVFnPoWy3NRsHxMIGWeFTmr_2O_bKtae3v8W-eCcN_Pu7R70bPUxDmxJ3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکوادو
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78134" target="_blank">📅 22:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78133">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">☁️
✨
HappyCloud
✨
☁️
🔥
تخفیف‌های فوق خفن
🔥
⚠️
فقط برای مدت محدود
⚠️
+
⚡
قوی • سریع • پایدار  +
🌍
مولتی لوکیشن واقعی در ۶ کشور:
🇩🇪
آلمان
🇳🇱
هلند
🇦🇹
اتریش
🇫🇷
فرانسه
🇫🇮
فنلاند
🇺🇸
آمریکا  +
🛜
تمامی سرویس‌ها آیپی ثابت هستند.  +
🎛️
پنل کاربری اختصاصی و حرفه‌ای…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78133" target="_blank">📅 22:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78132">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">☁️
✨
HappyCloud
✨
☁️
🔥
تخفیف‌های فوق خفن
🔥
⚠️
فقط برای مدت محدود
⚠️
+
⚡
قوی • سریع • پایدار
+
🌍
مولتی لوکیشن واقعی در ۶ کشور:
🇩🇪
آلمان
🇳🇱
هلند
🇦🇹
اتریش
🇫🇷
فرانسه
🇫🇮
فنلاند
🇺🇸
آمریکا
+
🛜
تمامی سرویس‌ها آیپی ثابت هستند.
+
🎛️
پنل کاربری اختصاصی و حرفه‌ای
📦
20 گیگ --->
❗
فقط ۴۹ تومن
📦
30 گیگ --->
❗
فقط ۷۲ تومن
📦
50 گیگ --->
❗
فقط ۹۹ تومن
💎
100 گیگ --->
❗
فقط ۱۶۹ تومن
💎
150 گیگ --->
❗
فقط ۲۳۹ تومن
💎
200 گیگ  --->
❗
فقط ۲۹۹ تومن
💢
تمامی سرویس ها
۳۰ روزه
و
بدون محدودیت کاربر
هستند.
✅
خرید فوری از طریق بات
👇🏻
🤖
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78132" target="_blank">📅 22:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78131">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یه صحنه گلر پرتغال هم اومد پاس به عقب بده به خودش اومد دید خودش آخرین نفره
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78131" target="_blank">📅 22:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78130">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تخمی ترین بازی جام با اختلاف
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78130" target="_blank">📅 22:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78129">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">همون بهتر ک توپ نرسه به رونالدو
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78129" target="_blank">📅 22:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78128">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فقط یه رونالدو فن میتونه بگه ترکیب منتخب بهترین هافبکای جهان نمیتونن تغذیه اش کنن</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78128" target="_blank">📅 22:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78124">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بعد دیشب گفتم شانس ایتالیا از پرتغال بیشتره یسریا به کونشون برخورده بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78124" target="_blank">📅 21:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78123">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تقصیر رونالدو نیست
گذاشتنش نوک بعد یه پاس نمیتونن بهش بدن</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78123" target="_blank">📅 21:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78122">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رونالدو مادرتو گاییدم پول منو کی میده</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78122" target="_blank">📅 21:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78118">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نوس با قد اندازه کاگان چطوری با سر گل میزنه هی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78118" target="_blank">📅 20:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78117">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6aO-L_2EbH2xOx5xKLTrHN0R1TCvQSC1Mp9OqLa_XFSVyAzRz_FNZSHmbiFxlui24f3qwFOC_EVJj2Chgf7hzbb8I0LZ3A0d6OZO3u8Rr_zRFL6517rTLZDpvRY7hiq6HJrFVQ0mbmALKluULjw5jzKjGRd4RBGSYwsoo-t58jCeZPH0RhBASdPf6c1d5iTimJsasyJubOzuiECpcpAW28MhQI87MBQaxnVy_B4XvmL7GfI-W81_frtdBJbb1CdwPYeTelDAoszbNAu1qdAx_jtftebAv2uFD-wNA9tUiPj19fVH6KUUZXERRy-EbbTBf0I5azdT_eFXjuAMytldQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا عارف
تولدت مبارک مرد بزرگ
❤️
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78117" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78116">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ایت الله جی دی ونس میگه چهارشنبه متن تفاهم نامه منتشر میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78116" target="_blank">📅 19:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78115">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نه داداش پوری خایمال نیست اینطوری میکنه فدایی باهاش بیف کنه و کیرخر
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78115" target="_blank">📅 19:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78114">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مسئولین جمهوری اسلامی حاضرن هر کاری بکنن ولی نرن حضوری قرارداد رو امضا کنن چون اینطوری مجبور میشن با قاتلین آقاشون دست بدن و روبوسی کنن
فک کنید همچین عکسی پخش شه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78114" target="_blank">📅 19:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78113">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f63df8bb0.mp4?token=ZHtbOtaTSa052pgzkezzd6Fg1ZL8z-RUC-51B9mgJM1N-RXFmmIQrbKB3LVfpOdCLjGU8FoC0MmnZzdpbWZH3Ph1WfeK-iMhmBT-Zc5yN16akLEpZUa6OYxfJteDPpSrzzij4LPvzO9-dOwACakbXJLSBSslar5-QW2owz9sN-3jBGxEox_Oud8xl5eC3MPIbPXZlPnpfI79AxkI-JxlHWv4vO-NsNttcEFwzBDf-PHEYEr7767jSe0MuUP5P306Eg2OibOYrPCz9_ZpBPTWQ1QNJB7JOEFGJ0XFia35neQUB9w_sd0Jnb0LoRZI_wOqOjpg8uMUwOb0p-aBWZpDCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f63df8bb0.mp4?token=ZHtbOtaTSa052pgzkezzd6Fg1ZL8z-RUC-51B9mgJM1N-RXFmmIQrbKB3LVfpOdCLjGU8FoC0MmnZzdpbWZH3Ph1WfeK-iMhmBT-Zc5yN16akLEpZUa6OYxfJteDPpSrzzij4LPvzO9-dOwACakbXJLSBSslar5-QW2owz9sN-3jBGxEox_Oud8xl5eC3MPIbPXZlPnpfI79AxkI-JxlHWv4vO-NsNttcEFwzBDf-PHEYEr7767jSe0MuUP5P306Eg2OibOYrPCz9_ZpBPTWQ1QNJB7JOEFGJ0XFia35neQUB9w_sd0Jnb0LoRZI_wOqOjpg8uMUwOb0p-aBWZpDCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78113" target="_blank">📅 18:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78112">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">از دیشب هرچی بازیکن و باشگاهه افتادن به مالیدن تخمای مسی بابت هتریکی که کرد  @Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78112" target="_blank">📅 18:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78110">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c2c1uKahJFVWOxZDFsbTfDMkJjj1NaSMFeTK1wtdrAyco8NgCrmZbQV8TF3ZKIuXmJ4_QsZGvn7HRG6tGF88SlwHaE5F7f6ChluW4L5MHN36JmQSgDJ5noQjvVrLQceOVsTT1_bCpTUhcW9PSb9_VEWgw1UW9TqCzzppy0peAJtEQcvc24EYv64VqS59VlJYwd4mVRHLuylqAQkRyY7ku8xqr96Sk7EauDcvlnpnL64lel5YSCDbw6eMxO3ZwYjyb3-HefoQ9ypAx8qfM4QuUKxiMhLJ331VX-0FTWH9udkH0ItFVUGacqNzlyWbRAHIBkEjy67fn96zUn0RDQs54A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxpyMpmEKkbEpxgADD-c61x3NMo4YSgIyAx_wr-iRMeqUBvM4MoLAmD2aJ1TU5uUfhe2yvtMnVjUueFzc3EySipFkZ1moRvNFqu9G3baRxt-c4KjdN-SCCJjT1K2qol--3OHwZld0TovmcwOfuClXdyUtZKku501ygGZo8zstf1zUXIvaqUhy5CUchcAgfqDzLjwYzUwd3p3NgVhxXPpkrrFUAbQEvVxBkWEhL_Sktrwd1vFoNDQkG3QUqi6XkArdYEZ2C4JC7u4QHiRqz2jzRPT0whX370r9KQElZO6qojf9Tt0-bpWpa_An9vgU7n4OFnTZZ-nXGLogqNXFFtIkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از دیشب هرچی بازیکن و باشگاهه افتادن به مالیدن تخمای مسی بابت هتریکی که کرد
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78110" target="_blank">📅 18:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78109">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78109" target="_blank">📅 18:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78108">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9ExCjJXAApbLzwnTchUtA5n_VCK8GieNqwb6OhItEL8kx3d3CfOO_ga1c8Wmo1hoiDuhne9qsl86YVjFwaU6QCY_Y5tLj4Lo8Wx7BTFRyk1nrYM2GHuTW3Lavw4PsthsQYKSjC-1VWSd0dgl2QxlinJXlYz0uX5E8pVaMZveNLhY5W_MQ0hSiTfTGdjEETW2m2ZxBJj7oiOedu3YziOBWuiYjFaw0kzvAEXlEg4cpfaEvorrUHTEf2MhgGOruWfYevMqv9goVhJWRCavklYok8Wrhvf-wV5auKCiZt1i7-IQAOb8HDUOLtJ7jf_qZQKCn2GUD0Fg0sesrssm2m4iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g27
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78108" target="_blank">📅 18:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78105">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">جدی برا این لگن هایی که تولید میکنید خجالت نمیکشید بالای ۱.۵ میلیارد پول میگیرید؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78105" target="_blank">📅 18:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78104">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDh7zh2D-TWk_wZxczTFbt1vVY9jSUUJlTAOJdu2VhlpoqrYIP4UrBXjcPPuj1Jgh36RhkWKlN_GJqtbw2nDiVH9rPWHswn1oZxuTktSz5hwEmdsnCCv9Lyac3-9yzltD7HLaF7msgfDEiMFVQGV0Zm6qM3MoB_0Jy_JVVIYi6H4y-ngqsLXNAxvlCg4wzVPfXjuwnJS5asbhr7MEF_fl9LFDJ2zyDsS7Kebg_QudhbR0V7piXy9y5CMQYsQsqGPDnKDEJWjuMKcqv8eFRm_wwDkMDV4k0okqyB0fzPu-IGDtipV72RaHrlm-ZPwM6q2D-foFdUQHpxs4NnU_nJH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی برا این لگن هایی که تولید میکنید خجالت نمیکشید بالای ۱.۵ میلیارد پول میگیرید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78104" target="_blank">📅 18:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78103">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/912473cfa2.mp4?token=jxd-p5pJc3AjV9gAYvut_GWmX9s4CpNMfOjXmepGVZxKoDPYskMqwiZfyx9IVkjm74rGJDdqQejYLdlDzjTZXA5gWm_Fjn_WWeis17ghMNw8LnyIfZxl_X7aZQz1afuth8rfGGgGLH1RcjGN2KuBNY0GI_3nXl8VCE8M_mHQEZrenyiv8_sO630rD-YVDTYUYWJ2L3o9WwEQAi6wAN6dx5eb-kgEBxsXWFIXtd3nYFUseANvTcp2qi8GZJBwCTP3G9SpWEyahDyBpGjg-yX6panoiclX7b0r1vFzhBrhjQJtGkpMiJU4iJz3zuNJzWRwahX5OGYKWe6PJycuH7krITzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/912473cfa2.mp4?token=jxd-p5pJc3AjV9gAYvut_GWmX9s4CpNMfOjXmepGVZxKoDPYskMqwiZfyx9IVkjm74rGJDdqQejYLdlDzjTZXA5gWm_Fjn_WWeis17ghMNw8LnyIfZxl_X7aZQz1afuth8rfGGgGLH1RcjGN2KuBNY0GI_3nXl8VCE8M_mHQEZrenyiv8_sO630rD-YVDTYUYWJ2L3o9WwEQAi6wAN6dx5eb-kgEBxsXWFIXtd3nYFUseANvTcp2qi8GZJBwCTP3G9SpWEyahDyBpGjg-yX6panoiclX7b0r1vFzhBrhjQJtGkpMiJU4iJz3zuNJzWRwahX5OGYKWe6PJycuH7krITzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دسخوش
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78103" target="_blank">📅 16:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78102">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مثل برج میلاد بعد ترور سران نظام هنوز سرپام
😂</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78102" target="_blank">📅 16:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78101">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ابوطالبو بخاطر این که گفته بود تیم ملیو دوس نداره چوب تو آستینش کردن و مجبور شد بیاد معذرت خواهی بکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78101" target="_blank">📅 15:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78100">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترام: توافق قطعی نشده اگه هم قطعی نشه دوباره بمباران میکنیم ایرانو
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78100" target="_blank">📅 14:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78099">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ: بخشی از تنگه هرمز باز شده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78099" target="_blank">📅 14:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78098">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ: گزارش صندوق سیصد میلیارد دلاری کذبه و آمریکا چنین کاری نمیکنه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78098" target="_blank">📅 14:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78097">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ: ایرانی ها به ریش اوباما خندیدن گفتن اون یه حرومزاده احمقه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78097" target="_blank">📅 14:29 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
