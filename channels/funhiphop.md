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
<img src="https://cdn4.telesco.pe/file/AM-IJkPaQRqobKmehRXEN4iTCP55gzYoEh4wK1hSDS3pzFLDxTx4WB2kfkcKocNlMNIgsiF5DSp9gE13v9HEKGPB0LrWpI1B95zo_vkCdkweH85xgD9TLizAtkMSEiAkJ6_eDPsGPNzUCyntQm1qrfM9nvG119Sq_-iVon33vFEPYfjBmfhwh_0aN5MnLav_3xBoNyCRsTiofp_zUlxMm20J5swIoiy4_Nd-lKbUz0YU-kV6ypcra7oOv5ZclwePk_HD9BERdIVOPnh8K0O0igGG9vrqPJaUA92g033Qm0sL1Z3aDWUl3KvlERz39dDf1WsgiDMJTGg3OpXMJEw15w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 22:23:04</div>
<hr>

<div class="tg-post" id="msg-83285">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1473c0f40f.mp4?token=STOAfo2ZtSpiCMG3sKgdCdkPpFMd5ESNvau3Go8upzF_SnaTckuBbDpFP1StRHI3tutpXtjKA8RQ6RmLMEr8wqCryn37hEU6gYuNbS98mvAAfKZiJqEuEIjhDpxUNtN1P3Anf8d3yMuFc0q7MN_2XTZXTv-vjY8IosrmwaVc961mPAKlG90xodKCQzz3wZItmxW4ow4veJLmC3qFMdrphCW_7xRDUd1foZYAGYp-P7BpRNNPa2070QAH48VUsHwGjw7lHY7zIHtcC4s6RlKuVJtw8GkeIcIEbrhwtfjUZ85rexLOoPqHKc71V6H3brvSEFGEqjBglL_WcTC4yuQCRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1473c0f40f.mp4?token=STOAfo2ZtSpiCMG3sKgdCdkPpFMd5ESNvau3Go8upzF_SnaTckuBbDpFP1StRHI3tutpXtjKA8RQ6RmLMEr8wqCryn37hEU6gYuNbS98mvAAfKZiJqEuEIjhDpxUNtN1P3Anf8d3yMuFc0q7MN_2XTZXTv-vjY8IosrmwaVc961mPAKlG90xodKCQzz3wZItmxW4ow4veJLmC3qFMdrphCW_7xRDUd1foZYAGYp-P7BpRNNPa2070QAH48VUsHwGjw7lHY7zIHtcC4s6RlKuVJtw8GkeIcIEbrhwtfjUZ85rexLOoPqHKc71V6H3brvSEFGEqjBglL_WcTC4yuQCRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید سروش هیچکس.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/funhiphop/83285" target="_blank">📅 22:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83284">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8742f867a0.mp4?token=PiVUQG3Qx7I06t81sJYpuYPUvCWXGjk6IrY6iRGjNIdiMaUCmqEI5gRX6QXtf59cDssZCAZg4co7pLWvPZnq9JJH7FeaRc9bvz2TFKXOC5AYZtZhyaRyR5jnB3DWd1dX3aWu7vgPe6ki9tFHQHaU1PpPWtoboz22SVAjQk_wZQxmyrpRvFXWhhs7sv3LocXEDJ86b1QzT8ipM3hggF4oschh35PugOdR0GJiImvHV1x7xFsRhxWvT4nzk_2wI9aIOgb3lPwH9BeEtTJMols-Fpxe9sV8uq1lqUl83VNLw4VpMiakwPjkNfjr6rKeOjtNbSy4EgLKRdjANieuhxkkcZg5p89QD9xkGt64WKYgZ-ns4mycq39uWwOcJSSt_W1-jJeZXLlE_m9Fz96KJ9ROmuNpNeJ_sfvirD9Z2KTOuPq9nxIHQc515t6TG_QqFTVfsBN6YqoIVCX74hCJxTUugJUDOj19sFwQmGmQdGrRRb1KqFw6Pq-M6VpKvST-Y1g3cUZNfLL7WL2GuTNxDLLZG6AWWyEzybuF1qZN6rLKePznpZs3zcmc3ywGH_s0HTpJkBVi80vsCLKjUrK2gUbDAXmn4gKfCaEWia_edvYutoHYLVA1JsOQeDu-FII_hs95oFugwrYTk3YJeIQU8zanL9wqNZ2QmRAuemVoeWRN0hE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8742f867a0.mp4?token=PiVUQG3Qx7I06t81sJYpuYPUvCWXGjk6IrY6iRGjNIdiMaUCmqEI5gRX6QXtf59cDssZCAZg4co7pLWvPZnq9JJH7FeaRc9bvz2TFKXOC5AYZtZhyaRyR5jnB3DWd1dX3aWu7vgPe6ki9tFHQHaU1PpPWtoboz22SVAjQk_wZQxmyrpRvFXWhhs7sv3LocXEDJ86b1QzT8ipM3hggF4oschh35PugOdR0GJiImvHV1x7xFsRhxWvT4nzk_2wI9aIOgb3lPwH9BeEtTJMols-Fpxe9sV8uq1lqUl83VNLw4VpMiakwPjkNfjr6rKeOjtNbSy4EgLKRdjANieuhxkkcZg5p89QD9xkGt64WKYgZ-ns4mycq39uWwOcJSSt_W1-jJeZXLlE_m9Fz96KJ9ROmuNpNeJ_sfvirD9Z2KTOuPq9nxIHQc515t6TG_QqFTVfsBN6YqoIVCX74hCJxTUugJUDOj19sFwQmGmQdGrRRb1KqFw6Pq-M6VpKvST-Y1g3cUZNfLL7WL2GuTNxDLLZG6AWWyEzybuF1qZN6rLKePznpZs3zcmc3ywGH_s0HTpJkBVi80vsCLKjUrK2gUbDAXmn4gKfCaEWia_edvYutoHYLVA1JsOQeDu-FII_hs95oFugwrYTk3YJeIQU8zanL9wqNZ2QmRAuemVoeWRN0hE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید سروش هیچکس.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/funhiphop/83284" target="_blank">📅 22:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83283">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d69a6fe9b0.mp4?token=YtxyK5Xgflb_rYdOwLtUjHpfy1CdXdqxCgMz8eRoyNIm7oLHX-oiNJj9fREF3_QiQ0iHXpdkfA3oXOuyJFvPqgH7FXnlzGe-E95eZOP2m-EGvJGrX5b3D1ksZaAjyQljs_q-H_9yovnSxVhbyEzE4rNeq1clCidaM0tTvSc_xpDQvp2MVDKYqbqHBccj9m5TwXOhDRTsi4XMbiKwLzH3nWLUHEjooXJRABLRAX1VXgGONSYljOVQnyUBcoEp3Dba-J02OH_xpRiG2fyOsT7v5QhpLkZ77s6ORZ7ARAVPb2cgyMsRy3VjvabcHrshTVSdk6b63i-9FSaqLTWQmc-Z3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d69a6fe9b0.mp4?token=YtxyK5Xgflb_rYdOwLtUjHpfy1CdXdqxCgMz8eRoyNIm7oLHX-oiNJj9fREF3_QiQ0iHXpdkfA3oXOuyJFvPqgH7FXnlzGe-E95eZOP2m-EGvJGrX5b3D1ksZaAjyQljs_q-H_9yovnSxVhbyEzE4rNeq1clCidaM0tTvSc_xpDQvp2MVDKYqbqHBccj9m5TwXOhDRTsi4XMbiKwLzH3nWLUHEjooXJRABLRAX1VXgGONSYljOVQnyUBcoEp3Dba-J02OH_xpRiG2fyOsT7v5QhpLkZ77s6ORZ7ARAVPb2cgyMsRy3VjvabcHrshTVSdk6b63i-9FSaqLTWQmc-Z3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هادی چوپان: هانی رامبد رو من گنده کردم، قبل من هیچکس نمیشناختش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/funhiphop/83283" target="_blank">📅 21:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83282">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">شاهین نجفی عجب موزیک ویدیو خفنی ریلیز کرده
🔥
@FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/funhiphop/83282" target="_blank">📅 21:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83281">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8Zrty-P4Xu2EdQ1ntZBh_UxWEKkS2KvqhSV_LCe6xGbrTWxR5QWhHKkQMDO89wMMQ4yl3KO6Hvz3EhXpo-HADL0eyGzeMK4cGUdKR5CMIS0Kmscy5Sw059jCq5UIIOSA_cyh7TeyWmqpmF2TBNx8oZXKdTEhIFuMFW2teas_AKQFqh69I1iN9eqy0PR3G5OTb-LQ5_8u60ULyYM02p-rkhJ2ZDMhTFzAg99b22h8vwhaDDIvyn2NMAw0XgoeR0q6uAwyp-BW8OrtnW9bjRSsfUreoSDhR411qRTa2A8yBgDHQa3w3qU1bLItyWTuL7ejMlzCHP-hrB6jKNoxDH4wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهین نجفی عجب موزیک ویدیو خفنی ریلیز کرده
🔥
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/funhiphop/83281" target="_blank">📅 21:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83280">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جدی این وضعیت دیگه داره تکراری و حوصله سربر می‌شه، به نظرتون سیزن بعد از کی شروع میشه یکم پشت کامیونای سازمان ملل بدویم یه ذره هیجان زندگی بالا بره؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/funhiphop/83280" target="_blank">📅 20:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83279">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سعی کنید تو این دوره زمونه درامد دلاری داشته باشید
من خودم درامدم دلاریه، دلاری بت میزنم و میبازم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/funhiphop/83279" target="_blank">📅 19:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83278">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یه سریالی هم هست Special Lioness یجوری توش ایرانو گنده کردن منم کم کم داره باورم میشه ایران ابرقدرته.
- مثلا ایرانیا رفتن افسر ارشد اطلاعاتی CIA رو تو خاک خود آمریکا دزدیدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/funhiphop/83278" target="_blank">📅 19:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83277">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9a6977e47.mp4?token=bDck3Dmk5Ar6mxKlSxCj7K0uNCqOkzxuYgR2dmJIVTdgg9yMAg-LLXMvVVUltI83Teaf7m81yt6YXt4JkH5zs3E8sBklkjspHbovO7dDWmPqcvJas-wbRDeLZ4umBrhNfkO3gySvPgEQyQshh_SWZTtmjV-7AE7qg4dxzM51OujZtBoFU3utfCGr5H3B0zAs9jqSzAu4-7w7AjTKSTIpR7tIoPGm1BoI-ksynf9Bjj1F7jYkdawuFi7cAjN9IIlh3qVywMpwye9_FC4TuSQxjBiXH7hAmJhQj0pwxduFBv_n-iZlvKjC3mu4tcjTnJF-SFIy6RGHkBTxZmkPN0YXYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9a6977e47.mp4?token=bDck3Dmk5Ar6mxKlSxCj7K0uNCqOkzxuYgR2dmJIVTdgg9yMAg-LLXMvVVUltI83Teaf7m81yt6YXt4JkH5zs3E8sBklkjspHbovO7dDWmPqcvJas-wbRDeLZ4umBrhNfkO3gySvPgEQyQshh_SWZTtmjV-7AE7qg4dxzM51OujZtBoFU3utfCGr5H3B0zAs9jqSzAu4-7w7AjTKSTIpR7tIoPGm1BoI-ksynf9Bjj1F7jYkdawuFi7cAjN9IIlh3qVywMpwye9_FC4TuSQxjBiXH7hAmJhQj0pwxduFBv_n-iZlvKjC3mu4tcjTnJF-SFIy6RGHkBTxZmkPN0YXYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق تجربه شخصی ۹۰ درصد فیلم هایی که تو اینستاگرام معرفی میکنن کصشره و بعد دیدنشون پشیمون میشید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/funhiphop/83277" target="_blank">📅 19:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83276">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_1eLnDfOn42wbptqrnO5eDNd_LXfSw8bYNi-jf4UammOHI68IeS1v0i4Vi0AWUI6w9Ul486nJj_ey83azSenpzOoYFo7pOddSskh5EZokIYQdvCviI91F6T_FbBKPHfGbhUD2waxvFe8JfFltm2jHufN8eZihCDdunBCtP2Dlg0e52tx1qArNqvQzL4YT1CN6ZOHxlroWi3QzkrBKSf5rGbPalDbayYrZbdE62pweEfUuo6-QgRbuBCPf4d0vLglu1MfPEOs_EAvqV9ZfE18laXnk-UfjF4uTJKMXjJEmcJ_IXGjWK9H3zUXrRqivev9wX7vlz1KPfhyAKpR6H5gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی هفته چهارم سری آ ایتالیا
🇮🇹
⚽️
تا دوشنبه بیست‌وسوم شهریور ماه، با ثبت حداقل ۶ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های هفته چهارم سری آ ایتالیا، در صورت ناموفق شدن نتیجه پیش‌بینی، بتفوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/SEA4
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g20
💻
@BetForward</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/funhiphop/83276" target="_blank">📅 19:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83275">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhXQQ8kmvqFtzHcIdepl4sngOjAwA0ivfnO2jxX7JNzH90PRVmDPbhFT9mDYks7V1NUUq3hDJx4wo9BwC7Krc4CazVaVQH4eaCBdZ5tVdMB428EeLqHf--1W5UOSXETroN84lLrbRThHQZmcGZo-Xbl4fIDB5zhfYSEosOl_WG6DFp0aHcajCPP0s2ZViklihlWMCRBmA0HtlIvnNIKnZktjPS_RPsGBdk4J7zchRJE-609otn3Jn5-Tmd2r7XGbS_JTzucsBNEOawO2G86ibRMG4ttlJswwbK-8ZwBsBLN5QLkNPlR3hIWmRGZbvink-gvf-b84XwNmzaWEOO3jVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیکس چند هفته از تمام دنیا جلوایم
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/83275" target="_blank">📅 18:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83274">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edd900df7.mp4?token=D2MDG-v5bho6XWuzy-G7sHJkbqNFHU-vGpupDCAdOubh4211s3VyxthfU4XYbzE0he5MrIyTTL8v5KyCYaglePRmtS0fgVPLhsCwsYiW7aRfLhRJY-kVnt6nHtPv2eaybo57B0j89oRkPNe23JaS1rM5bHXvM5xsLXel5BWswO-l3epP3CTbbP-x362RPWV4pJcak-w765HbGgCOOZ245rgf_TDs6To2cPAZOBwWygagvhhKeKp7mUYFBCbf8T_AywEEBPnHGaJE7XLCE0l3b7FYoBjItD6_z-XrPUIugO8hi1IJtWY9MRwvRSt19uu7Iy3XJubP8jZHTRZU-kQdTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edd900df7.mp4?token=D2MDG-v5bho6XWuzy-G7sHJkbqNFHU-vGpupDCAdOubh4211s3VyxthfU4XYbzE0he5MrIyTTL8v5KyCYaglePRmtS0fgVPLhsCwsYiW7aRfLhRJY-kVnt6nHtPv2eaybo57B0j89oRkPNe23JaS1rM5bHXvM5xsLXel5BWswO-l3epP3CTbbP-x362RPWV4pJcak-w765HbGgCOOZ245rgf_TDs6To2cPAZOBwWygagvhhKeKp7mUYFBCbf8T_AywEEBPnHGaJE7XLCE0l3b7FYoBjItD6_z-XrPUIugO8hi1IJtWY9MRwvRSt19uu7Iy3XJubP8jZHTRZU-kQdTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدی این بچه چه گناهی داشت که پوتک باباشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/83274" target="_blank">📅 17:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83273">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ و‌ آمریکاییا بفهمن با ۱۱ سپتامبر همچین شوخیایی میکنیم همین امشب با اتم ایرانو نابود میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/83273" target="_blank">📅 17:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83272">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تصویری از فاجعه ۱۱ سپتامبر:
🛬
🏢
🏢
🏢
🏢
🏢
🏢
🛫
🏢
🏢
🏢
🏢
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/83272" target="_blank">📅 17:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83271">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دوستان رئالی شما برا اولیسه بمالید مالک بایرن نمیگه اینا خوب مالیدن پس اولیسه رو بدیم بهشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/83271" target="_blank">📅 16:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83270">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دلار ۲۳۵
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/83270" target="_blank">📅 16:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83269">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">@FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/83269" target="_blank">📅 15:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83267">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQ7UiFh36MVV9udLs2W_cFYgWo2cutNU6CbkH4jG_DngYx1azMhauHl0l9Vsrt-hd7XUvnRqysUbHUfBL2s0ISYMTuigBFzmrOsuprlTCECryuzPdtNB72lv_cm6SfLA6PZ99YOzdwp39rHch1XSmaUU4aW0vJhiQRdgC45vkFJWkVBJa2P22dJhK0Sa6DEzEE0qwYwUf38ZHAa_7NYmV7zoMmqGBhUz9fGIDmZfM82TIg9K5tvjqezYbkAbsYSNng5XLjXJeRq9hua9Qs18Yo7I3ps1vUULEp5wzcHTDpCSoRr-5j4hYBL0hn-RygKtSCmU7lg485aExIg36xVSOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rblCe3wowVCjZaaM7ez_7JmqWqb56kxB6Eyc53SHmOlVpEu8MF-TIfojtmF68OB_i-zlzYbZ7CS38ZiExwbBK6-Lh9-o5XQR8PMS4Z1p9qCD9cCX378T49GOtQ-SdDpQ-wd3ogrzCeeT-nKJjY9azSH_XiLKGl3smhGTk1z8nVb0eE-aArT0tY3t1meI4sY4lHKHUfMW_w8nDpy8jczhRXC_YqNOJuqJBASTpBvewqay-vcmEEXglfzaGE3RXKWMIdYN4rBxnuwwYtEGXeNaIsYIHa6SiVG7xiDDAnKgIWaFMXIB2Ltkd8BKP3wBn7_ACZFFbdeHclc9YBtSK-w90g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همدردی مردم ایران با مردم آمریکا همزمان با حمله تروریستی القاعده به آمریکا 20 شهریور 1380
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/83267" target="_blank">📅 14:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83266">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56d26230e.mp4?token=WRn8_iWSNo64o6wReQVjVA08k_MHgZYz95UbSnMLuz4viNc9RSqZo3CAqwf3cHzhCwRjYrr6ya74F1-_aFcy5ERacMp6yuI6K4W1tTwFgQ1Nc8QgPDsyi-FqRZD0cF43aaq8TRqgkGdT6KtbEvt902Tk4tngWECqQBereXeKVGUdJRkAwpzuAkztSYYolEDak36-JHYVqigfF70rntlwxg6Yj9dWwjByO7DOxDS5ZguZLH6ZIkiwAxrL-Gd_3gX4Seb9K9sYCbb6xRcnGABdL6DhcwWtMukdRVYfEZXIdt7RXu7w1ZnoPr8l8C9zTxfNjIVcBI25AeO53MClV_ujGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56d26230e.mp4?token=WRn8_iWSNo64o6wReQVjVA08k_MHgZYz95UbSnMLuz4viNc9RSqZo3CAqwf3cHzhCwRjYrr6ya74F1-_aFcy5ERacMp6yuI6K4W1tTwFgQ1Nc8QgPDsyi-FqRZD0cF43aaq8TRqgkGdT6KtbEvt902Tk4tngWECqQBereXeKVGUdJRkAwpzuAkztSYYolEDak36-JHYVqigfF70rntlwxg6Yj9dWwjByO7DOxDS5ZguZLH6ZIkiwAxrL-Gd_3gX4Seb9K9sYCbb6xRcnGABdL6DhcwWtMukdRVYfEZXIdt7RXu7w1ZnoPr8l8C9zTxfNjIVcBI25AeO53MClV_ujGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت ۱۰۶دلار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/83266" target="_blank">📅 12:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83265">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دیشب نه در آمریکا، بلکه در یک کافه در قم از آیفون ۱۸ رونمایی شده، تو این ایونت همه حضور داشتن الا خود آیفون ۱۸</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83265" target="_blank">📅 11:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83264">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8758825884.mp4?token=dr166vbRmfIKfPzz38hPulYw7vk0JaR3EdVhzuEG1Xv_KU9FYY5P4SjLLJP_e08JFaTgQBD3v4GyKgTyWoIUYgwtgBWbfN9qckWp4JelxjjVQOTlCY_pYUVHUivAZDLkUx8KeDmljD30Hf73fMEL4wztR08M-R_ClB4J1-5JO_-bLOEdbbKeKKqHGdC0uHYEOk2ozD_qwGFeukTQpVJ1xBuPvsc4Lfet_uFsum-4G-KVtGZ3JPWZLXiZLhlUVrs9ySDn-RnzsjTRtPDO9TCNviXJhb3NeymIMVf5lkajylUK5Ej4UGb0MC1W2xdgsr5eabMpcKdTCiKPdxh8AysHIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8758825884.mp4?token=dr166vbRmfIKfPzz38hPulYw7vk0JaR3EdVhzuEG1Xv_KU9FYY5P4SjLLJP_e08JFaTgQBD3v4GyKgTyWoIUYgwtgBWbfN9qckWp4JelxjjVQOTlCY_pYUVHUivAZDLkUx8KeDmljD30Hf73fMEL4wztR08M-R_ClB4J1-5JO_-bLOEdbbKeKKqHGdC0uHYEOk2ozD_qwGFeukTQpVJ1xBuPvsc4Lfet_uFsum-4G-KVtGZ3JPWZLXiZLhlUVrs9ySDn-RnzsjTRtPDO9TCNviXJhb3NeymIMVf5lkajylUK5Ej4UGb0MC1W2xdgsr5eabMpcKdTCiKPdxh8AysHIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو منهدم کردن تونل های در علی‌الطاهر که اسرائیل منتشر کرده
انفجار این تونل باعث شده یک زلزله ۴‌.۱ ریشتری بیاد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83264" target="_blank">📅 11:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83263">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe621a2e8.mp4?token=MVEVTpboA1SMaHNRKSgdPD2iCSxYIOdQPu7ASpCwkYdmHhY4dt1aFgMNbokrp0LeWR62PF6yQGq4Egw25_g0EDBQ96RgIChelGXEx_M-JaQvm3_WIKiEVeUds3HvHHcgFi0a06BqlZQfb_yOXld-Y7IWXP0NHI3dKNf_VbD3kxqLJeHuhz3a3et8JVnX3Vq4cjKhQHSuVC3o6TOCaVki5dRctkfGt0GibNGd4QpgmrVVbvKWJIiqNkrPR1vdj9H6sRZY7qMQLt5VQuIQUkeneDtYhdCArDh8baV6WHSDFtUi7EuG9QDUEaaftKRiR6hCp-yOeZ5dkhr-6Ye4gePFpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe621a2e8.mp4?token=MVEVTpboA1SMaHNRKSgdPD2iCSxYIOdQPu7ASpCwkYdmHhY4dt1aFgMNbokrp0LeWR62PF6yQGq4Egw25_g0EDBQ96RgIChelGXEx_M-JaQvm3_WIKiEVeUds3HvHHcgFi0a06BqlZQfb_yOXld-Y7IWXP0NHI3dKNf_VbD3kxqLJeHuhz3a3et8JVnX3Vq4cjKhQHSuVC3o6TOCaVki5dRctkfGt0GibNGd4QpgmrVVbvKWJIiqNkrPR1vdj9H6sRZY7qMQLt5VQuIQUkeneDtYhdCArDh8baV6WHSDFtUi7EuG9QDUEaaftKRiR6hCp-yOeZ5dkhr-6Ye4gePFpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی پایدار کی منحل میشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/83263" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83262">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/funhiphop/83262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
اپلیکیشن حرفه ای اندروید کمپانی بین المللی وی پاری
🔥
💖
امکان شارژ از طریق کارت بانکی
💖
تسویه حساب سریع بدون احراز
💖
دارای مجوز رسمی Anjuan وcuracao
🫣
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا، ترکیه و...
✅
کانال تلگرام:
👇
💖
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/83262" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83261">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJxe16V6KDQM4WAv8SJC85YZzuLduw1hyHSDL6ala0mXBu6N-9zBJdyaeSZ44yKPgplGeDjyI0QU1RiLkZED0C1QkY9zYEQVIpGKsDaraItQL2KlUnmh3aOeSV2a_N-pM-Iw_0UaV4OerrhG0tdO4QAmWj02FPJqkKOaR_Vv85koLfnabX0hAl9d99vKSK1T1zM7XivQD_fj7phcTPxsxBWOpWcer0B_DK8SwYKc9u_wjGTXp7Al3fqciJs-NbcxZkzcyVhW3OGInUGX657wn5zRmOwH9iRW2VqTxo7VV50l6_NhxH4dmzH3Xn56kCvweO4t1rndY5dcIabOsrqw6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرط بندی با سایت بین المللی تجربه کنید
🔥
🥇
سایت شماره یک اروپا حالا در ایران
🥇
😀
😃
😄
😁
🎁
واریز اول
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز دوم
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز سوم
💖
75% بونوس هدیه
🎁
واریز چهارم
💖
50% بونوس هدیه
💌
کد هدیه ثبت نام: GG007
ادرس سایت:
🤔
http://til.ac/z5jcpGT
💎
کانال اطلاع رسانی ایران:r20
🅰
✉️
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/83261" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83260">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">امروز سالگرد حادثه ۱۱ سپتامبره، یه دژاوومون نشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/83260" target="_blank">📅 09:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83259">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83259" target="_blank">📅 02:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83258">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0wkq0gyohSCK8HZx7A1msULhzOkWyprHVXT6yTLXecWuVyoHDZvnD3EQoMRO5FY-8JkuDx_cJt8XfMti03S4Hl9voVC1UWyOQzTw17ZDWj9RfYH7SWU7pXgFxMnLvZw8w6xjExZ1mr4-_LT3KplpobRZ-rOh5qn8BXuxqYTUtFja0Vg0iOVoAK3LCdEKZl8Oas-oYYzjFnXsko3xxX2qeF6_E3LcJDdOJdNxUbNkLlBO3H6l_OX2lKrKCBtGuTHbmGJo0Lt5CFDKwZghnuRKaPGqp_xMLS7jxTqg8jlJ8kqZlgMzFPnDb3bDCqfHfAo_QCq3Fjz2jmYd4q9VehPoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا اعلام کرد به دو نفتکش در ۷ کیلومتری عمان حمله شده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83258" target="_blank">📅 00:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83257">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شاهین نجفی الان برا زید جدیدش آهنگ عاشقانه هاشو میفرسته میگه لیلی بهونه بود اینارو برا تو خوندم، درحالی که اون موقع این اصلا بدنیا نیومده بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83257" target="_blank">📅 23:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83256">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmhKPpiwoo9_F-5Dn7YEvCdzqQRepx49KwXVvEIjSBLPXj65RIjWTWGaC5olDquj_c_LJBOFXbC0_5L6qKlzqBrVvIJRHGtWmiAI3Cv5ALbCCssqV3CyZf-h9cp5BpTV-ZWTOCsDqIAmwe29af0PebP-esp3uyooNEX3YW2ZSaPiU_W5Lt89IsAKCumGHf6JoKDK5KOq8kaHuG8SoVNoixAcA55fan75n5IP1NDKsxzdGdKPSiFVYBu9KyTJjXIVjaf0zYnMvgMtIhakPtpmISOMJ33vDOzwXx1svFImujjuhoDXVmGTY23ddoagDbVigeXCCtgezcaUphMcFZnQ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافینیا یه باند میپیچه دور دستاش، با اون ۶۶ میلیون تهش اونو بدن بهتون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83256" target="_blank">📅 22:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83255">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/774541b7ea.mp4?token=XJjC3wI7cq3wO8YxT67rqzSKe-_gSFbo0rrI3AWiWiXJ-dF8RSUuWB9mWxFU9_8jXdv2xUKwDW6O3Ys-LNc_nil1shGQT2-STOUSDfYyzSp9CDy0aNUpVnIBelSZcCHrdt2caW7bpMJwR561rb0KouoL2f_ahschCvjDeLBbAN10NWnUPlc6PR4KcZWnpWPe8ymlAJHk1ft_H8jfTp79JxVMUBdgryjLrlN5t8_G3wGz5XeMHsyFTUxh7W79hkkoMwTbOiFsdXzMDxlj8JaLkbTHfTLRGdtW9jgJ1NqwqbULH6GOQtKMX_V7DJ5AsjbnHjLbdTwSn_5eBhhk7s7zkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/774541b7ea.mp4?token=XJjC3wI7cq3wO8YxT67rqzSKe-_gSFbo0rrI3AWiWiXJ-dF8RSUuWB9mWxFU9_8jXdv2xUKwDW6O3Ys-LNc_nil1shGQT2-STOUSDfYyzSp9CDy0aNUpVnIBelSZcCHrdt2caW7bpMJwR561rb0KouoL2f_ahschCvjDeLBbAN10NWnUPlc6PR4KcZWnpWPe8ymlAJHk1ft_H8jfTp79JxVMUBdgryjLrlN5t8_G3wGz5XeMHsyFTUxh7W79hkkoMwTbOiFsdXzMDxlj8JaLkbTHfTLRGdtW9jgJ1NqwqbULH6GOQtKMX_V7DJ5AsjbnHjLbdTwSn_5eBhhk7s7zkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو انهدام پایگاه عماد ۴ حزب الله در تپه علی الطاهر توسط ارتش اسرائیل
پایگاه عماد ۴ بزرگ ترین پایگاه گروه حزب الله بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83255" target="_blank">📅 22:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83254">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تاشو بودیم وقتی تاشو مود نبود  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83254" target="_blank">📅 22:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83253">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d72d98371.mp4?token=r8RRPncaWXPkfHi-eQWPs1qSl1YHX4pbRolPO74YPMUZ1vS8T9JFi0GIhOtVgQxGDhjF9kYL_wRLacUh5oDFps4rWilM3gB9yvsETy7AjeCItOGrSHorVo-hSH7lgzyl4C_HaxCsWVJ4xUnQnnNMqthYZIVKEGiNwqJ624asSb8X9-ZpyIMeo7DB672zrLvR5HxwhOf-TFoveRPj9VbWh-hpdTpaoPFk9NWuwAt-HUgErR75vr1D48vhfMQSN_sWLBFruMmkdLa7OTy9mafDlWMTk2-WVB7XJEo9o-HJFloENKYqZVMPJ2nZNUZWS_GPpgKYHU_9iNM_uXkfNUdiSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d72d98371.mp4?token=r8RRPncaWXPkfHi-eQWPs1qSl1YHX4pbRolPO74YPMUZ1vS8T9JFi0GIhOtVgQxGDhjF9kYL_wRLacUh5oDFps4rWilM3gB9yvsETy7AjeCItOGrSHorVo-hSH7lgzyl4C_HaxCsWVJ4xUnQnnNMqthYZIVKEGiNwqJ624asSb8X9-ZpyIMeo7DB672zrLvR5HxwhOf-TFoveRPj9VbWh-hpdTpaoPFk9NWuwAt-HUgErR75vr1D48vhfMQSN_sWLBFruMmkdLa7OTy9mafDlWMTk2-WVB7XJEo9o-HJFloENKYqZVMPJ2nZNUZWS_GPpgKYHU_9iNM_uXkfNUdiSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاشو بودیم وقتی تاشو مود نبود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83253" target="_blank">📅 21:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83252">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLCMJ5cGh3sCoJLwPz8VKN_u4m9O31OJDTcn2538AuDtekF68YLcjaTUYQIQ_Lsbnjb7Y4qfTuFusodCvnxO7dicSGL0YFVDCrDPpgO50KWZPTN3ay27R-jmwNrAmcXenFma-AnUFjxAwD7YJXHfFVtT_Kqmye2Ognw5yI24GmGouV59URqSCt5l57L-bkmnIfHa52RogQyCszC7NjbxjSj3p8gMgSh1F_fFelLICh7racYaL_rUOVOaySUtnEnidR3VkYsDM7cwvbi9FywTYseL1amZRZ0AOur7T1jikKWhk7u6ldkShlT2L0VZaLNpWGDYEo0GRGaUm0edKqxlCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا این کصخل که اشتباه جمع و تفریق کرده ولی جدای این ۲۶ تا میمونه، یه تورکم بوده گیشنیزارو خورده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83252" target="_blank">📅 21:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83251">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4r3YMaqJpG2Tu9LjTTtdFxTY07TrFeNcBWD9nZ0YCdLlDPa_TS6-FSHV9HjOWhdpU77R0d5tgWQZDibG-CRluS1KnSmnvDNgYOos51eoNpQj1kW_BqCvE73aRxNbAZNSX7IsPjqcoQmyBGpkGUhKxGS7eKAwv7lOor8VxIWoqRDKPO_Bi8O8zIoHnlawvnG1aLUR_bLbJvCU-tFOpw4878zoXLrVLhdg0h4gHQ1YJpQtVC-83uKx_28CIdhru19yUpVUvUaq7z9MhHOhV83J4da48EQH6yd0URWx7vgfDEGHvHAJSei2NhMk5BBYh-HwM8-KhLoqcROKJj2cOwS5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقا مهراد هیدن که با اعضای گروهش فرق داره و بحثش جداست اومده ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83251" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83249">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hv_iBz-UU2JI5L7i5kIPnZ7v8Yp2FE-5EQGcmfDn9YzZkNUA1nKfusGpHcTXteK0jrDT3ESi4I-_1JjWujDEpqvqab7Y6Fy1XnYB2zMc7dKyld1-1Q-uEd58m_Px-7u3xe6nnUGKO0IX33NvVjcW7KM7yV6CBjOS3Jy-QjSrewc48fEOezsUs_uV1HH4CnlxiBRDqiSCqnutHBOrgs8S2fh6UJBfSk-JzKabxbpE_NI3xRR0zHEtZbRE3jvuQ19FEAjcpJo3dzaX7GL_710g4ybHPOyNpOL_Fedilr2CDXqUic7OoCvQ8IWw_Zlnx835uWA6-vFJ-okldKAZEyCLFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qPuTcFtE2FxadY6M_i42-2ZD7BuxBwmgM18ny-ODrT4ZFSBzV-2zPZFkEk5ZMjSGz_p9bylg6BuCF2Fuatt5XVTqRZMWqRh_aE4WTFMow_lEyglwbudH5KZ20GsYdU3qmkixs2A1b0metD6wNGqYvbthtKfFzhKYBCgWSK0j_RMCPaxnxMSa6iFG906tYYWpoe5QZLza5X0K7XTktwAaj1kfT9rx1JAHqh5mEdkO9AZw_DFjvUxyoqLwn2_3ve-Wt-lWkGhD2YZG6iNG0Q4oXxThX1uMWjfgN-IlpJLF7LnfV4zUFGPVD2wzKcVdhuAOvHaOLJ___f2nwzHK8z_hEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آدیداس با انیمیشن ماشین ها همکاری کرده و کفش با طرح مک کویین و ماتر داده بیرون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83249" target="_blank">📅 19:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83248">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHHrlo5u96V5oFqmkFHJK3PQ6ZW-X0O2fNeoZJMicyLVddX5jeRIEV7hRyd57J0tRqHm9FaP4yDICv66D1Ur4emdTiqePdbobqH0bWtDmC5P_t7bBwz4o0m3GSHMNJk78TOAhEiFEQjfVNGNqXdzgz-LyNDn8hXsKZALWa5To1GL66e_mjpSiZamJh9OeQECagjJj4HfDJ4PhSDgHICMmwFB6ZZ7QXqqv_kVnvM659o-nfUBDeVaBClcplJ1iYkPm6RmybVdJ929-Zn2SswT82hm8YsR8ruKSX8GEV8Ftsq6dlsiMBfPy8DNDBkmOoJ-Z0I4TwaHq-iSouBJEtHuPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکم دیگه بگذره عکس کیر مهدیارم لیک میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83248" target="_blank">📅 19:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83247">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEinyenldGSvQQcjm6fx1O3R71rdgYzNU1adang8XM8jQWebFKBkwqm5leUYFYzIs5RdsGUGGnTfoo7LCDcOMzSFXGyISsspJQi0jSVsQQmC51zXethdFAkPTCEVXNzsAX5BzpWao-ks3ktupxpFsBKXM7Zzypih3q2x2k0MMG6uEIVBhlY6mi1DbtlEb7dogxeHz8_mxyOt-FP-pAFTcr8BTwNgw10EfTTiUYIAeI_zKUwXgz0mkGz-eXWbl0b-I53uYYXdXdnwTJwmAnEdNYmeW_dYNi2b2R3Hi0wOotTJM31C-7tlfDuJWZckgrM2kDXyFzCxA_H5vcbBs548kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۰٪ بونوس ورزشی برای هر واریز فقط در بتگو
🤩
🙄
🤗
🎁
۲۰۰٪ بونوس خوش آمدگویی
🤑
-
✔️
تا ۸۰۰ میلیون تومان پاداش وفاداری
✔️
-تا ۳۰٪
بونوس
شارژ اضافی برای هر بار شارژ با روش حساب به حساب بانکی
✔️
-اپلیکیشن اندروئید
-
✔️
شارژ حساب بانکی و درگاه اتوماتیک بتگو پی و اتوپی
👽
بات راهنمای بتگو و آدرس بدون فیلتر:
@betgoir1_bot
📌
لینک دائمی سایت بتگو
🔝
:
g19
🅰
🪩
betgoir.com
@betgoir
Let's Go To Betgo
🚶‍♂️
🚶‍♂️
🚶‍♂️</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83247" target="_blank">📅 19:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83246">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqGtMw1BAUAbz_aPk0m3isS9utk7ad0QPCvNue9JR2qGnhPB9xZcjnaI_1Xd9XVbT7BCbKDynH5Kdb5__Aun7Hcp5EJTgGh-NoUGa-2z9bQmqkH32G-_ecXJQeNLT1bD12m24wL1fSvS6hpjFGfrhlvbHWTSJwCTET-pkTN8kIWzSataEkRJPMPOsAoYLRJzC5Jxy-WtnErGbOvF7R-fSGXj09ajmHMml01Lwx4tuazEL3qZd7dL63_eQajWk5ZUYxtG1se4fCgXQQ3c4vO6H1wNeszwj_Y1WWMZOf_YmtkhOVGMDJhHSOKsUB1E-VCQ8NugFXj-5dcOy1sbe2HWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین مهاجم نوکای تاریخو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83246" target="_blank">📅 17:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83245">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خلوت کنید آقای خمسه اومده</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83245" target="_blank">📅 17:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83244">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TturWT44KvwDYI7n7iK6ZX8FXOQxPH7L5mqJ0C6CEwyNGmv0jFvDClfGzixnCAYgL2gLGRlwt-7fHGuv44YYK0Ue3KVka8TIyj1KcPzecVg_gD1ZfMzdpnn5ugzTjU9UOD7cYmUK_6XYoCnpyFy8jOOxR3iS8vP4iQQ54j4NlBYQPlZDPynUcQ1gK_QTkMrH2H2k_RNkwB-9CWAyUEkzqAPI--7lqXuXNhkwxKFZyvebBcGOJrwtBr2tG878aM2dJsxiDekYiyeeuOXL_LoFLx1F3ztRAHhbcwohUB8tR09IpHrmCiaepMxbn94YD0lRf0a6UlmDsRCZCTuOCCyW9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از عجایب رپفارسی اینه که کسی که به داداش حسین تی ام میشناسنش به سجاد شاهی میگه فید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83244" target="_blank">📅 16:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83240">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/483fabad8c.mp4?token=VGhU9Y0XmteUBZwgPWdRZJAlnK5DDMcgqCsbJunvxzgdM2b42DT49DQg4DOTXX-tLH16b_gf5uZigbdLZgVPzAwRH9T7kQ1QaVmSSqcLQUotmdWSh05tlAO6NhS0imsqgF4WpjmAdkcBpGzejJ81cHEnO-QivEFGTsqAKYgXHre73-gS3lsbHa8-vl1OV77gN1mvsCY6aPQmbCboHrrtV5qpbfZL9LEiQ0SAqLSr9qb2QIeYBvxdIl6byEoxuDhzQTtK8_aGonNpTtEHpEEIFdri2SrBvKvjl2gRCnLmojRYItdTdm92yXNmslZEFboEVIGXBCcfs5sDlWLZVZb-9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/483fabad8c.mp4?token=VGhU9Y0XmteUBZwgPWdRZJAlnK5DDMcgqCsbJunvxzgdM2b42DT49DQg4DOTXX-tLH16b_gf5uZigbdLZgVPzAwRH9T7kQ1QaVmSSqcLQUotmdWSh05tlAO6NhS0imsqgF4WpjmAdkcBpGzejJ81cHEnO-QivEFGTsqAKYgXHre73-gS3lsbHa8-vl1OV77gN1mvsCY6aPQmbCboHrrtV5qpbfZL9LEiQ0SAqLSr9qb2QIeYBvxdIl6byEoxuDhzQTtK8_aGonNpTtEHpEEIFdri2SrBvKvjl2gRCnLmojRYItdTdm92yXNmslZEFboEVIGXBCcfs5sDlWLZVZb-9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: پاکستان و ترکیه تصمیم گرفتند نیروهای خود را به یمن نفرستند</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83240" target="_blank">📅 14:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83239">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ولی خب طبیعتاً هیچوقت کسی که برا پول میجنگه نمیتونه حریف کسی برا اعتقاد میجنگه بشه، اسرائیلم سر همین جلو اینا دووم اورده و خیلیاشونو نابود کرده، چون اونام اعتقاد خودشونو دارن</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83239" target="_blank">📅 14:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83238">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مگه نمیگقتید حوثی ها دارن بگا میرن</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83238" target="_blank">📅 14:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83237">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انصار الله و حوثی های یمن به نیروهای تحت حمایت عربستان و امارات کیر زدن و درحال پیشروی ان.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83237" target="_blank">📅 14:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83236">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RB-apvuN0GhypUAR4M3trpmaxhhzrEsQZdMjIy0ZcPyvmHhiIWSWJd65Hym2Q96rKgv0fNJCsVFXgQBfVmWr4PRlUZAJRDzqWcrR3y41MYUG0-vfhqgTuJ8x8vG7B5VBvvW74fmSwQ8XnIcdPKW3rLIM1G3eXUavgOn1Zy3f7tvJcm7K9wVc2hf6elHprXCCQ9_X-oVhcBUn9CIxzoAjziFza7WoGHt84DSFc95NunmnUsnWXVUBDai1ks5Q_a6vfCYDwf6vnhkobz9lB56H5ozbg6IHsHy6fAfSWWNikaaVAIXYLPJYn36iK1Z--Rj2KYP5CNakR2tc1gop7OoF6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکم نظرم عوض شد ولی همچنان لیلی بهتره.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83236" target="_blank">📅 14:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83234">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJDAfuUmu02YLRCpLaeGpAwN9lw3Y99jsl9kaUqt9ttC_NDE6KuBcxc5njJaW0wUnGCJ5SdfF3lBC-DSyxhL46FMGvZMyuJGVaday0JbcDcmPAIgmhcHM1gWBQIcatheFwJ7MNZe1XJGVObBnZ9nn1V42IrQC1sPewV30EGj_-3nxR9bZUR_bktneU3mgw4SQvf5az1G1wHwWdxvIZoM40fRPOVCfS7g1H6wLFTdoLp2vJOAOLZtiW3bSbHKHVGJk3dZ5SX9jv13UBAuLnNoNwJ1jUm32J5A0cTB4Z6momEb7GKsuXn8AsEXCJaR0K6oyUgYRG1Kj22NX2EjLTl2_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kScCGGLjnnzwsMdmtWYvc4cP4N9QK-5WnV3yo3YSqjo1rcMP8zXZi7J_4fKevUoxSkB6MdYDHj7a9ts7TRAtGQG9kXA8m7LeqEg0PAUlEww0REVoE170elxlRNvnJINx-cRQscOw_80F4lRb1SzkOqPR4ycWWllF0PCge9y-xwzPPqv8y2zGnEtHGvu_QNAp2jKjwhipzMEH7M4gIbRy2AdoBoi98uaviDaN46CkhzC0ZwBGBaEfTVC_l2FpBmk-8dNuPxdL9feshDNEmBO85WkoH50UG63QuD9uW3Yj8_o66-Vxa8h7YbtjkyGze-m3sGrm5HOwlG2QpYn-PVlFOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لیلی بازرگان بدون دست و پا اینو میزنه</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83234" target="_blank">📅 14:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83233">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">الان لیلی بازرگان میاد توییت میزنه این کار شاهین نجفی رو به شاهزاده اطلاع دادم و منتظرم باهاش برخورد کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83233" target="_blank">📅 13:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83232">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شاهین نجفی هم شوگر ددی شد و با یه دختر نهایتا ۲۰ ساله رفته تو رابطه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83232" target="_blank">📅 13:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83228">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GmmX9_XYZYpGxKr6RBoccQEGEhCEnwL_avDNVBvjEZjSCKOjqf9VTd0mFmoNZQcLca9Cl450mqoWEfqY6ldic7A_mE9Ui21pmDr5hWpOulmFQETU6Ll2BiohrdbqH1wss5V1leGqAyUuH_xeHLOW6_cahCIrpUHbIdzRlGjbab8OSJGt4pTMgtH558YEA3fuVsfY4v3wvJ5UBxdQrlJo_yzwpdDFQ-E3D0mhbHSYpj_51hu2By4WsiuR0WQkdJkz-_7dWmBDDK7GQQzKB3ufDUIlrkJSGN_fUnHHVczO6faqKZxm4GnsUTYZRcNVLa_-xx7MVyZWcHtIiobk0Ex0kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uAO0lD-3ows6sqtVodJjSGc8av_Wa0glNYMYINjQuhFAV9GQMxLzKX2nwbexVqixVxD2KI_SZ1imQwfdiIvfwjfg1A5me_6nOjWahhBacChsUYgT6doYahLswvb8oZehfmlZEGOe6YHNik7elLgDQrzO8MU6WkcFNGeoCSJ9yJxCYMXPNwvbK4MhfBtF6QPPxNuBupbiBhzT5m8H-i5Jd3U05j5dKdogeRc5VAmSaL2cpfFgEMu5jV1eNOpaU8F-QOsEbx-O5M9mXcMTHOm6XEZaYRJW58bSqLR32al595fBV_3ruImTKUizW2UiSgeb3QehMJeYxbZrpC6mS9fcJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N1CxswJ9YhMFvy6jpHDNR3ypcTeHqgMgZHUfWsHMlXPcDxUjhF0piP0gCzouox1wRxHZiAeaWFwMfCYpiPBn9w8d5bfjknUK0sYH9IxraIHN5h5aVaddgye6c6IHdhW26X6sekFOO7E5G87le918SdEntqBdePtkwmiOZwzSlI-hw5I2QTWZwZXyvW2SpPtDp9B0zpGMPr3WD1pYJqbnQu7ncdbVQxYBwq2ypkJxrFOe5mkL3uzVgmwhySugfC7lmxdUQ6DHek-EZy-flCpT0w9lyxqlyUiv401iDl764XL5SSlNC8nel2NqrkX4LL3vTmW8gO8zSUONk4Sg__pDRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/scVT4C9tdyh3_0OM0lEA67UW37GZa4AIBBWiOB6VdL6EWKlJivw2pUgKvEzt9FH0FSnR-lPHvS1fBSFbgjk4tTWo9SPpXbMuYBEq3rSgVqnydhNqyqVf3V3PD22tZEcjZpzF7NtynRec0CirZwQ7rGpznSIql5MPkX7vdJb1wTTtvXcgsN2UoH3YNJpsQxsw9mZ02nJGf7qmQb3WPpo0MPbX1LCzO5dGlJCuSSF532Qz005C9lFTgDq1LSQooYY8xONlNhLZpTPTalqy5iTHe40tZt9-bBP9Ago91JzifrsD4DSU3V80p6GXIzG6fFb077IzOTCR6jOojZ4rbcSLgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاهین نجفی هم شوگر ددی شد و با یه دختر نهایتا ۲۰ ساله رفته تو رابطه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83228" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83227">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تو مشهد ۱۰۰تن مرغ فاسد شده بوده، گفتن حیف نشه بردن سوسیسشون کردن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83227" target="_blank">📅 13:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83226">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تو مشهد ۱۰۰تن مرغ فاسد شده بوده، گفتن حیف نشه بردن سوسیسشون کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83226" target="_blank">📅 12:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83225">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الان دیگه هرکی عقل داره از قبل داشته</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83225" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83224">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeCy-W19aD9xGMvco5fQNxiSbUe2O7XR3D8z1QFJp7T7Y3BFzU7FxZArr2xPHSoQc6AeQi1OEvIt_oULI2tP1kZoVB4AB6Q0vGnNUbjeKH7WrBQyptXd938NKl9KIcaghjikCHOCUFG5-WlU1bhiJraD3dLIDmj6HO3oVXqJ05GltMVVB782WY2uu3UPt8t96sxzlLqrRoGymaJ99Y9cT2pM_Y1zgv6KPezKI6qmjGnZ9vYGt1TVQryHWztsWld-M2Ul7Gn3THRlrFPBNU0OzJ2sqWGI_AuuEALS076ChMR_JM3_XXXLwyQBUp_Nf1QMbPSri5ZDO2bQKaq1b7XG7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سعید جوانمرد، افسر معترض ارتش، به ۸ سال حبس محکوم شد
جوانمرد، اهل الشتر در استان لرستان، پس از حضور در اعتراضات سراسری ۱۴۰۱ از ارتش اخراج شد و در پرونده‌ای مرتبط با فعالیت‌ها و مواضعش به سه سال زندان محکوم شد.
بر اساس این گزارش، جوانمرد که در مرخصی زندان به سر می‌برد، ۱۹ دی ۱۴۰۴ در منزلش بازداشت شد و در پرونده‌ای جدید با اتهام‌های «همکاری با دول متخاصم»، «اخلال در نظم» و «اقدام علیه امنیت ملی» به پنج سال  دیگر حبس محکوم شده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83224" target="_blank">📅 11:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83223">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1ZlHoXNIOqdUcSoLih0NDNqayYIszDdRkYsNiurlYkb87_segOuPInwFo21aS-CuuHe8Bcyzr0JvHRYeZ806Qkhm5YTmKnDiFckWrVwB03Mumt54OaxsQeiK_2ouViu_Lnxh5f3_at1AZxgGO01MPqWLU0jluMmMRv3GPrOLihzr8jadmftDvNP525tv8KxhEJtXnZylYuVVP0iWguFbOdvGtGQIgwZbLiuPAoKhFunIwi25EABK1Xyl0_nNwFRTe02alcfI05RrzhHFPyq16YhfZzoCQSVOhNQ8Kx9X66Pf9VLan96L4u4Us_dTxjsZWfnGSbesfmgK1di34od4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا به خدا این کار همه جای دنیا رای خریدن حساب میشه، این آمریکا دیگه زیادی دموکراسی داره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83223" target="_blank">📅 10:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83222">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZhjjQXdc3-7J5S5TjB68_9tAjsn-YJWhP4ZyzT25QsTGakXZQ03HeW5wE_BmDdRLBjEn0J7KT38cIGUzsgtSrIqC-suGmx3eiLiD7LySntl5N8XGuByyJMKckDUFDi81WN3lIMwKbAohmWD_zpZNFzrseNBdPIQCz0s2dtNE8EsEVzPHVkjZ2JrNC5bDSiRU_pqItAmAAgxCai3IONADpXCUfUoc42kuemC0DbwoXnsnIFaUtIguKlwCB9ivh-AN2tnGSS7eDvQEpoOX3nDvBAYIkNIXE5ZmlugZsKKbDMESMDhWMGU4IdHaxogiW_8HRIG8JCKlYk-sAwMd1NU5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بونوس ورزشی ویژه برای لیگ قهرمانان اروپا در بتگو
🤩
🙄
🤗
🎁
۲۰۰٪ بونوس خوش آمدگویی
🤑
-
✔️
تا ۸۰۰ میلیون تومان پاداش وفاداری
✔️
-تا ۳۰٪
بونوس
شارژ اضافی برای هر بار شارژ با روش حساب به حساب بانکی
✔️
-اپلیکیشن اندروئید
-
✔️
شارژ حساب بانکی و درگاه اتوماتیک بتگو پی و اتوپی
👽
بات راهنمای بتگو و آدرس بدون فیلتر:
@betgoir1_bot
📌
لینک دائمی سایت بتگو
🔝
:
🅰
19r
🪩
betgoir.com
@betgoir
Let's Go To Betgo
🚶‍♂️
🚶‍♂️
🚶‍♂️</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83222" target="_blank">📅 10:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83221">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ:
ما شاهد فعالیت‌های مشکوک در کوه کلنگ هستیم، به آنها هشدار می‌دهم دست بردارند وگرنه مجبور به اقدام خواهیم شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83221" target="_blank">📅 10:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83220">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDfnRTthWov6Pdg6aLEH3l9Tihec0N9xCw8cDWplneR7g1wx2mwqvR3zqo4WPq9y4mLWTCtqcYqrPy-PYNXrhc-xI3S5gp9r9P6p7k4I8rh3_1Hp2AsSV9oZHKwrxxq3NYyNkD7tEFdXdyZgZoL9HtQ7wmclU_0vvNILNBWlLg5BIxfRYk0aiQf-tHELCHmrvCCu0KhMr5EfwSA30Z2eQS7bT9RNnMhmSvXx9WcrqATh9y5xwoHcStwAmGnxy05llwDunlTMQLqtoanQuIRTAwIhNKS-UlR2W-WDKEzSwoT_rTuYYi3wipdBDS9VXzdfn9l8udXFR3s9d3s1tk6m_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون متن ریز اون وسط رو من اضافه نکردم، خود عقب مونده‌ش فکر کرده خیلی خنده داره.
ولی به هرحال اینچیزا مهم نیست که، دوباره صبح زیباتون بخیر
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83220" target="_blank">📅 10:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83219">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cfeb7c626.mp4?token=FdNEgi1hC63s8Yu1Bt8H585YwCG7b2Sjw-CEBus5L1fUYzQ4uSCUxKU1iTVTeWEc181r1PBlHsPrNPhtO2uEBrmBtAZhX1IA8xKQBRIEhZiRkDrBgG_icQA-TxSYHdm-RQ_cvZR0pKOyVTKDIqyqtP3UcMnUvr7PCJSc6plyeXNC3OT8H9DDC9Stm-1RCoAfdHTjlWohkGBtq1zx4vpZKoEWgr07NSL2uRA8RGjTJvl5tMtuoo4ZByJ5o96GKfFEth4m0YYbRctRQzqvSFL5wOk0b5lpytM8ZZXLLAKwx1w76eFI-BdS64L4TQ41tRNwuNJFFX6qTJiCaoOV-MRCVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cfeb7c626.mp4?token=FdNEgi1hC63s8Yu1Bt8H585YwCG7b2Sjw-CEBus5L1fUYzQ4uSCUxKU1iTVTeWEc181r1PBlHsPrNPhtO2uEBrmBtAZhX1IA8xKQBRIEhZiRkDrBgG_icQA-TxSYHdm-RQ_cvZR0pKOyVTKDIqyqtP3UcMnUvr7PCJSc6plyeXNC3OT8H9DDC9Stm-1RCoAfdHTjlWohkGBtq1zx4vpZKoEWgr07NSL2uRA8RGjTJvl5tMtuoo4ZByJ5o96GKfFEth4m0YYbRctRQzqvSFL5wOk0b5lpytM8ZZXLLAKwx1w76eFI-BdS64L4TQ41tRNwuNJFFX6qTJiCaoOV-MRCVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکا اعلام کرده فیلم سینمایی نجات خلبان آمریکایی در خاک ایران هم دستور ساختشو صادر کردن و بزودی وارد پرده سینما میشه.
بزودی مردم آمریکا تو سینما:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83219" target="_blank">📅 09:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83218">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d4fcf7c48.mp4?token=cwHISR7hY1f_EDccUIJ60dc7jTKeYBki7EggwARhPj_l8pJrG8ENLOX-qI9uPcmPrpEsJ9IThEErs1kqy-DxFo_o_8uJXkg5rXjEDwKSVSD3xYu-nIxXdbjRBDGF6cewhNjxgevI2P4zgs1sOotwosZQXZa_tCvcgjbAaZxvlNJN1RlY_F6DwDmtQo8X6955PKz4rMpvLPtn2UUpK2wp8yJEf5FsUlDA_C_Mqox_u4uXmUvrpi8tFvbCmIKLubqjpTZM5HuLPeKo1ArjRNnGegHi2-6ny_5n4zSqzIrWlERf_lfR9hhJqDnZuuoYJ41EN5g-PT7Qb8SAc5NCbNbTXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d4fcf7c48.mp4?token=cwHISR7hY1f_EDccUIJ60dc7jTKeYBki7EggwARhPj_l8pJrG8ENLOX-qI9uPcmPrpEsJ9IThEErs1kqy-DxFo_o_8uJXkg5rXjEDwKSVSD3xYu-nIxXdbjRBDGF6cewhNjxgevI2P4zgs1sOotwosZQXZa_tCvcgjbAaZxvlNJN1RlY_F6DwDmtQo8X6955PKz4rMpvLPtn2UUpK2wp8yJEf5FsUlDA_C_Mqox_u4uXmUvrpi8tFvbCmIKLubqjpTZM5HuLPeKo1ArjRNnGegHi2-6ny_5n4zSqzIrWlERf_lfR9hhJqDnZuuoYJ41EN5g-PT7Qb8SAc5NCbNbTXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون با تیک‌تاک فارسی بخیر.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83218" target="_blank">📅 08:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83217">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">قرمه سبزی جا افتاده از نظر پسرا و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83217" target="_blank">📅 02:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83216">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">۸ ماه گذشت.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83216" target="_blank">📅 00:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83214">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vasUost0gOVrZeRRiqh29Kdxlh3E_mvRsiz4igJOcfvoV-JSRQ2C4tqDBJsQZGC2SPb8HFXqT9gjvBkEtZT-juL5gB32HHTE7kdQiuIOFOtX2S04ZwcEK-L-TA9KquhHcaJAAJ1hJ_RbfepUZPH0bdPAA9DormDFCRI7Jlx3icz8FRHh3Vkciy_h6Tl_cQ4UqkIYxV_p_lzqEGYqDI691KbozW1EZO7qwWQBxIOtzdqKTN8l3LJ045xHxX2RxNvQ-agDduvDlIBZyLQpPbUqr4TUYHYh5dXkjaOPAn4qVm5obpAncUS8yD5FDyboBmfpNFvmKIA3JNgtm295Y9nTZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfvoAZns9v2m7JcQp-dHjfaNlRrAd-zS1KXaIxhWbhxW_lkBG9RppHwSZFk1WbIq28j9lJoRTzyqCkVmzW3S3ekU24F1JzCLtdjybNS9054DAJgdEl13kpo6uBBHkL8vfmlTdiu-ODMrG6XmivTEu9dMid_RZEy9QO58qB6R-BrTduHlopt3Q4o-SntrMafY7SQxNE3SuBH7QgzcSjScd0frWitz6qs13eSHcJASvL9XXfRVetc3dowgk5wrfpCli1EyofhLTS574PaBdj3_aBNcMMqp1aopba6C9p-Y82QwnRxkGL0X4sNlWLrdKJAiyjoIaOniqRsPV9VX_7XOGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عاقبت بت زدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83214" target="_blank">📅 22:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83213">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQarMlS1i_Dhiaz0QW0dJ8TdXa5BgoyGsmm5fbBPBdadUeSgGNwtfUFY8BHRXWx2DAfhQ7DjZLh56AWFHK5H9w0dlaPwR3Sv9Cype5e0ndk1WAUtHll_SPlMd-dXu7183WOtCmAfe_BUl89di_9UDVml-pauHNFLHfNkHJYFVrqSLQ4Bve-aUAsbpjkq3gBhwbpBjqVmvSUP2Dkbz89KUTK8kis7g-FkA0fQfYKnH_Agl2FMSU0ADDQwSD_i13V6kEfpnsdRo1HwBEztbg6P39zFwwdXPKhJFDKY1YpTBJmvPbKPdp5YXzzPCLsjHSaBkHShaA2rQ9VMw1gMB4TSAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احساس میکنم بارسا منظوری داره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83213" target="_blank">📅 22:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83212">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rr1ji5inhjCRaX3AkOQ2ZbwC1rixbFxXcGu97lcECIj1jgs6x1zAnJQn0wQl9SuW9hCnm8H2gPIv9o9Vex77OKDO-ftlxhKTFPVJW_5gCCHXkZ0xDECmQf5IakjO1_tOxC2ZVEOsxtVVFhtTBW786G3RHhAL25OmXhu2Qos4i_HS4BuuA3a8ojJos8UwB40gPG10pJSQdjIbpHIWpuZpBzffAbYzy8iQF7kOCWdCJpcGZNAv3Ac-kZZ8bCioJgU1Kj519Hut6gP81t2RJ9r2jmba8gT1qAdkmuQWmIQ78h2eaCrz-SRGrLzfntw6F1j_mujTYQdRq8BXm3KhJ5K0dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظ
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83212" target="_blank">📅 20:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83211">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کریم سوسکه چی موشکی ول داد</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83211" target="_blank">📅 20:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83210">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">میثاقی وقتی خداداد تو پخش زنده از کلمه های "کصخل و کصکش" استفاده میکرد میخندید، الان اومده میگه کار خداداد زشت بود نباید فحش میداد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83210" target="_blank">📅 19:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83209">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1a52ccfb.mp4?token=NM8b0eRwUn_brzlJxcwZ3vzESjzwq7mzHB3DTrmjZzlJzs_zHUthhUMsGuyIXSBgoxeDN7y_6cvCaK1aU_zQ4xrABP4md64b1xK3w481YAkSW61bBOg2YVhRi0au1wxJ9lnlIHb318I31q6hx-wI_MlFjzArg-j-rNW7wbAwehg03FgYcBlFfH1nJVUXr-MAfMIUwuSg0h44iirGTF7j_2FbCEPl65kweLVI2Cjc3fopGrnheXdKlUuGHGBtO-5ZChnGeAoOz65QYmH7bQ_SgCf6TLmbgeQpEKdnxFAK9S7KxBp66J8NJrBsTlVlEZy6NTri3UJCNR_tKWBA6RTl7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1a52ccfb.mp4?token=NM8b0eRwUn_brzlJxcwZ3vzESjzwq7mzHB3DTrmjZzlJzs_zHUthhUMsGuyIXSBgoxeDN7y_6cvCaK1aU_zQ4xrABP4md64b1xK3w481YAkSW61bBOg2YVhRi0au1wxJ9lnlIHb318I31q6hx-wI_MlFjzArg-j-rNW7wbAwehg03FgYcBlFfH1nJVUXr-MAfMIUwuSg0h44iirGTF7j_2FbCEPl65kweLVI2Cjc3fopGrnheXdKlUuGHGBtO-5ZChnGeAoOz65QYmH7bQ_SgCf6TLmbgeQpEKdnxFAK9S7KxBp66J8NJrBsTlVlEZy6NTri3UJCNR_tKWBA6RTl7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبلیغ سیدنی سوئینی برا یه سایت شرط‌بندی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83209" target="_blank">📅 19:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83208">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc63a398d.mp4?token=O8caA0eWpYBb_jLE_4L-R71jm4fvtyPa_D-IfJcuTwXAgct4iYsERjpx68JX6GsD5sU_PgTI1aGgCS3Rv4Gp-MvQRRgc-0Ofon0K7AZjtL3Z1DizRcY77ld5cUWWkzFbGvXcqc_eiTI9EUzBpqoHkRBaYccqPrxHilRYUkw8qvq7jBk6yTC2flshkTSrwU-Rg_jLZmDJnojfuDSaz-of7Z8o5uibla15VOLwb6zI26zRVvwJJerE4q2h_WWwfvRfx2AD5mWM4cmNSwB1t_NXUp0fP8kzgkKGyhvWlFXC1x4eLziRdP1W0Zh27JkWH6ve3MWrTJvgVTt9G2h6gyyVYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc63a398d.mp4?token=O8caA0eWpYBb_jLE_4L-R71jm4fvtyPa_D-IfJcuTwXAgct4iYsERjpx68JX6GsD5sU_PgTI1aGgCS3Rv4Gp-MvQRRgc-0Ofon0K7AZjtL3Z1DizRcY77ld5cUWWkzFbGvXcqc_eiTI9EUzBpqoHkRBaYccqPrxHilRYUkw8qvq7jBk6yTC2flshkTSrwU-Rg_jLZmDJnojfuDSaz-of7Z8o5uibla15VOLwb6zI26zRVvwJJerE4q2h_WWwfvRfx2AD5mWM4cmNSwB1t_NXUp0fP8kzgkKGyhvWlFXC1x4eLziRdP1W0Zh27JkWH6ve3MWrTJvgVTt9G2h6gyyVYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83208" target="_blank">📅 19:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83206">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgpXQSL2dX38DX9C9gTyg2-8kjBcHv2all3dideyxKis7anwMxNMmLIJDHWIpGiUPFxJQu96BWosX0DnPjIF8lCaBm5Ma5NF6qiK2uSjU--ns3NcMJoiHRYJ4Oldx_g_BvLMspapq4QWQdT9Vj1pQEfqQsd9nMZLxqFQMbxWLYHF8sl3qEBGTDpKiAUgZ2ba0bzaG0g1TMDtvaNtmF7sZYpbyAjWu8uzo2jV3jMdwqifXgBQXmVWFoqqOoeI_i6vGSMTV9IESPdIxKPzkVIXpf-MBCUb7PQphKIOgsUMFpZCahm6eNUTtGpc72DTyYU0a3ienRFUStNzv22alv6UlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درصورت هرگونه تحقیق، بنده‌ی حقیر به هیچ عنوان هیچگونه ارتباطی با عوامل این کانال و به خصوص این محتوا نداشته و ندارم و به صورت اجباری و تصادفی و به دلیل کمبود محتوا، در این کانال ادمین شده و دست به انتشار غیرعمدی و ناگهانی این توییت زده‌ام.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83206" target="_blank">📅 18:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83205">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مثکه پاکستان میخواد پیمان مکه رو فعال کنه و حوثیا رو بزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83205" target="_blank">📅 18:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83204">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_Nhhc9mLm5Ln51f-IsItENjiJUONH7rae_grOxENRRK2SVWaYMBKMwboLw6443FJdFflSnBszv_tZOkyJRnkRRIbs6UZ9f5iGX_pmxSR6o8EkwTG6dcLhepjAuIpNNX31alMiWuS54TnvNh37XkAr5ba1Gx3phHNwI6HhmtYxHLbpSdzZZtWMH5zKgEM0t9Ni3AV3fyA6OHM3wFWv7Trvy8hh7JN4N5mvG0pQuz1XvH2K-5JUwPqs3-oIseNnmJizrfz1mMhG-vP0x7xzHBxie2RKEd5cD8NsrzFAYbENBSJDzNHs8fSJEoVo_CImfk7CYNObXx5EF2O6SVEhckkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به این حرکتا، همینکه تاحالا اتم نخوردیم یعنی هر جور حساب کنی خیلی تو سودیم پسر.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83204" target="_blank">📅 17:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83203">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/565302292d.mp4?token=iBI_KOk1yNSodOTA64Ve7M0d_G3pTaEiBKLoPxhN66IEAEToFAsoHizLMlIir18KFDJ6IgwnSdpRO-WGel_Cud7YZuazhSTvJsGYlaLUu_nY2M2voCnypiCCCwm7xp1G_4fJTkAfRrAXmFh6HWkbwu2EBaloAAF0sCFfhGShTM1vc7cqM12apA45wfkdNxd_vsuEWXtD1wKI1XbM4mJRQS2NT8GCzC_SPpXx1Qf2RoJuXfIjKBpMZkEU1OgcOsmJf2xjFaJ13z3nsd12ItxCisM1YxRXrQk6uMV5sHCIdA_b-KF6msDtzjQc0-7YCwDkiFTupXVemDNFr4aIeDoU3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/565302292d.mp4?token=iBI_KOk1yNSodOTA64Ve7M0d_G3pTaEiBKLoPxhN66IEAEToFAsoHizLMlIir18KFDJ6IgwnSdpRO-WGel_Cud7YZuazhSTvJsGYlaLUu_nY2M2voCnypiCCCwm7xp1G_4fJTkAfRrAXmFh6HWkbwu2EBaloAAF0sCFfhGShTM1vc7cqM12apA45wfkdNxd_vsuEWXtD1wKI1XbM4mJRQS2NT8GCzC_SPpXx1Qf2RoJuXfIjKBpMZkEU1OgcOsmJf2xjFaJ13z3nsd12ItxCisM1YxRXrQk6uMV5sHCIdA_b-KF6msDtzjQc0-7YCwDkiFTupXVemDNFr4aIeDoU3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فان‌هیپ‌هاپ در گذر زمان:
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83203" target="_blank">📅 17:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83202">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ارم نیوز: آمریکا در حال بررسی حضور تفنگداران دریایی خود در برخی جزایر خالی از سکنه ایران در اطراف تنگه هرمز است
در صورت اجرای این طرح، جنگنده‌های اف‌ـ۳۵بی مستقر در ناو تریپولی وظیفه پشتیبانی هوایی از تفنگداران را بر عهده خواهند داشت.
هدف این طرح، ایجاد نقاط دیده‌بانی و پایگاه‌های لجستیکی برای نظارت بر تنگه و حفاظت از کشتی‌های تجاری عنوان شده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83202" target="_blank">📅 17:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83201">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f275b2369.mp4?token=GvzGteh7A34vrioavGBgif09syBADH3e5hN6f1HLrgXDgL6vbTjJk5uN-SQ-Jc6jSTVoKzY-gDp5wcDaEXYmFcPYgNafY7b7i7t9Jl1PpwlpdA8fTli6N4ngpQcHix8MOALUqrKgOpfdYE_2nKjUGsmzo0YWyjcA5dSYDWSgALyScL4HVMSLeIHOjEP0Unq44fsKgre7JcYhzqsgLs7lAwe6MoVw3-zRUzSz8-LKJsKnZPetiDLN_okFN355kQjq17ueQS3MqWktJUaml99i6NUbWAKsY4M8lM8AhAQymZRPKZgMO3kzg1acbdkc9cxCmB9lGdZQN4bwBq_yMmTYbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f275b2369.mp4?token=GvzGteh7A34vrioavGBgif09syBADH3e5hN6f1HLrgXDgL6vbTjJk5uN-SQ-Jc6jSTVoKzY-gDp5wcDaEXYmFcPYgNafY7b7i7t9Jl1PpwlpdA8fTli6N4ngpQcHix8MOALUqrKgOpfdYE_2nKjUGsmzo0YWyjcA5dSYDWSgALyScL4HVMSLeIHOjEP0Unq44fsKgre7JcYhzqsgLs7lAwe6MoVw3-zRUzSz8-LKJsKnZPetiDLN_okFN355kQjq17ueQS3MqWktJUaml99i6NUbWAKsY4M8lM8AhAQymZRPKZgMO3kzg1acbdkc9cxCmB9lGdZQN4bwBq_yMmTYbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه ویدیو دیگه از عملکرد قوی سامانه پدافندی پاتریوت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83201" target="_blank">📅 17:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83200">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBUzsSzoq89YZYSwulV68RBZ9eZSGizzE5Cb55erTUakv41XuvZfCClMwTGSpp5bJLeJ_fWaPc7J0PHciBbAKCqoAmRzV_JwkkHTstbGDAp4esjy2Sff2XFZPq9OfgcFsIc7wN5up_IYL4-CBE0MP5aSw5L89ACqnV_8j2aeuXllhnVLF2oOl5GWAFgRcD03k5-dA2Qi_b1YcYFTL2WyKR6Tk-bIhP-4dZ9-Oy2MjMA6N2HelXYYtFpRzOQswBAIiFJBlHdrpnlMCc08ADnGeF3kTqh0uJ5wMHyd6xO8EStj1h-LcgJ9Ui5mQPsuaKHD3A_lhISkMFsNkTmUT1r6Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد محجوب ۲۵ مهر ماه قراره با لویی سادرلند فایت کنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/83200" target="_blank">📅 16:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83199">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترک جدید ممد به اسم Sweet one منتشر شد SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/83199" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83197">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuvGsJu4gCWNVXbJ6dSBZbAt1eKm5OlW05DdG4OyggeKMcF1wLIJn_Y7mpz4ZtMS5NSmGWJLQoCtExXu0gQCpo34JSg9oCy4xS1Vf_qWwFtn40-CfCheVZ-ibWQb5Gsb9XYMh4-DorGtFaMWsyAZmhTdQVQCsh5QjCV8UJyDyz0RA9Vv5FuRqauUGjSZcz03PqvfkKXAjrXU1wenHn_LNH4O9FEMvUwfU_c_0h1I_wftluQJFTWU_nehup64IV_izKbfSexnpIbFa26iuB7C4blYzpvbKPYmJs4COh_cjgwNv6GmLCb5pJHbBMOYg7neoVCXSmmICXejaNcESz58LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ممد به اسم Sweet one منتشر شد
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83197" target="_blank">📅 16:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83196">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZYqOHlMIthDIjalRXNl2tsqCsswAQAFTlziCDoVoAWZHwP7b8kntOmGuQj3AOAQHjtCuypF9r6EgSiOo8PXI1_T4cNiKBPXK-mmFI4hzsMgpvies_Kczh-kRdfzviAKauhaWWQYpcvtHUAfija3Ki9jrJwo97tcKMnt2IZwkcNwFXAH0moehxo3sfd1MU9EsbAMqadvIF2_QthWB4Yunr07RPzPC6Kv85VgIL8LT4KC_zIfy5KMfuHioVnVHUNUO4BC7nVSEC6aCjiPxVN7Ygnuh2nUsK9HFXiXsmFikU3QSTADwGXwxqdeHS88iawf4KpvqZvNHCVJN_BhfyDf0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83196" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83195">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jW8HcesWNE3lFyHzE3QxmLk4magjPJnUp4DnzfabOyQQfCRv3QNSE6FGliuQvMdIJ-zrMd76b33nKTQEBF5UhH83z0MCZUF0pQn1dUF6nH2uqQVzuU89zqYm-o43H3Zgnz1Y7D6ftSh2_uFQVWw5KW1aDD-y1OEhsDNV3vlBW35EUbMwte9PKEE_ckuT-idwt7_USPzMsFZVMCYd1sGhYhzyTcGEABT-VTHiFqWd8GVxgRCeVoy7R_uzBexb1nGXyKltWJ1vgJv68Qoi-LzXt-O6PqxtTiUm15-lTW07ED-tIONmax_jTKjlnxM826UfFJM5f42Lzo1pbwEeVQpxiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رنگ های احتمالی آیفون ۱۸ که میتونید با حقوق ۳ روزتون بخرید اگه قاچاقچی اعضای بدن باشید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83195" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83194">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/peBh48CS7MgOlE2lxUFlaNHDzsqa-lq1_eQougax2Vf5TLP1-Jj_f5rY6M5jAb72mLQzCYSz0_X-5BRHURYVAq8Tx8jtWsFzN_3ieYYuFMUCnzQxLKIv8ILZSonYN2J73m6EqAmQi3K4eslfd_e9DuhhjjOUage8AeZRmQMFcIxFR3g7D74O_NPG4swiJhzQHfYTIOuc234b2WLaAb-ncqykYHcXjpgBNf8AOKKYroGM-3u_wUMb7YsmRLr91JIU-KNcq6PONKq_CCYSLrx5Z5BkhvLX-Slp11Dv2jwxg80tn5y3efGhBObDX6NFg356mK06ihWeMggYnD-2ZdMGNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندگی وقتی دلار ی میلیارد و هفتصد و بیست میلیون تومن بود.
(اینو چند سال بعد بخونید)
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83194" target="_blank">📅 15:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83193">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1bc2eba11.mp4?token=jKIqTdeRvq3j1AgD9PDftMWb2-UF-Xg6fhGYrIr1EeFu9tgQmCvOXyD-UUkGOYNYB0b-mpIxYujeh73HDOTmrn6EeQbIOF3cDhvfYJT1Jzlr3ZgJgsytHMfEJtSfOjKZfgBKrHJg0SM6HcwyD4CB2feZeHlijeQXFnKHZjqgZEh4vb-TDpNU8gVMokOpc8KfK1-QaFdwbNtbWH_eNTKptIgW9ztr3Vs-wTcwbLQpAnNXILF6tvG77gcThcw8SCBW7FvayDexvfhNsPg363daHVVvP1SA03o7uzczSpPILXGNLb0wLyKq17IzJ5k0aQsgpMsQOqF8D2kE1dtO0w_XVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1bc2eba11.mp4?token=jKIqTdeRvq3j1AgD9PDftMWb2-UF-Xg6fhGYrIr1EeFu9tgQmCvOXyD-UUkGOYNYB0b-mpIxYujeh73HDOTmrn6EeQbIOF3cDhvfYJT1Jzlr3ZgJgsytHMfEJtSfOjKZfgBKrHJg0SM6HcwyD4CB2feZeHlijeQXFnKHZjqgZEh4vb-TDpNU8gVMokOpc8KfK1-QaFdwbNtbWH_eNTKptIgW9ztr3Vs-wTcwbLQpAnNXILF6tvG77gcThcw8SCBW7FvayDexvfhNsPg363daHVVvP1SA03o7uzczSpPILXGNLb0wLyKq17IzJ5k0aQsgpMsQOqF8D2kE1dtO0w_XVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس دانشگاه سمنان درمورد اتفاقات چند روز پیش و تعرض به یه دختر ایرانی توسط دانشجویان عراقی:
از همه دانشجویان عراقی‌ای که هیچ کار بدی نکرده بودن و یه دروغ بزرگ براشون بافتن عذر می‌خوام که چند تا دانشجو ایرانی که حالت طبیعی نداشتن سمت خوابگاهشون هجوم بردن، ما دستگیرشون کردیم و کاری کردیم که اعتراف کنن به کار بدی که کردن شما خیالتون راحت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83193" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83192">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ما تو خیابون کسی با استایل دهه هشتاد میلادی ببینیم مسخره اش میکنیم، بعد شما میرید عکساتونو میدید هوش مصنوعی اون شکلی بکنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83192" target="_blank">📅 14:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83191">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کیا مثل من نمی‌تونن تا شب صبر کنن تا مشخصات و قیمت گوشی آینده‌شون رو ببینن و پیش خرید کنن.
😍
بیاید بهتون قیمت و مشخصات احتمالی رو بدم تا از همین الان آماده باشید.
😉
این رو برای سیسی‌های ارزون هم که دنبال آیفون ۱۸ معمولی هستن بگم که آیفون ۱۸ عادی فعلا تا بهمن…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83191" target="_blank">📅 14:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83190">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDw5l0TsRHYs2DncfZJbjX6ozyzv6f-_M8H_rE4vZGuX7XihjwRMCjBwugFkg5BlQo16vorPkwoS9Xg9ybp1nPw2dDCzKAeOY60eHS5m-KKNUWU9s0av5mbps621I4PdwS71vY67N2fTSSWWkHXQ2mJOBW4UT1AH18gcYNXhxndZ6GomMyjct8UjroqXmh_oJ7AX1ksqHLWhBvSzSWm1ue2FKhqdRl7r57kpcL43jBRWORH0tpZgQYw7nBYwCpAEqq8q8ttfWmvbWRvEANQVPqtgfjM9Xui9r63UxZR2vQCHkZeDavDYekqw4xQOfbHUbkDJnMVZTpFNR_Okgj9sag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاگرای ایرانی آماده باشید که عقب نمونید امشب از آیفون ۱۸ رونمایی میشه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83190" target="_blank">📅 13:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83189">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حاجی من از آیفون ۱۳ به بعد دیگه باورم نشد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83189" target="_blank">📅 12:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83188">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دلار ۲۳۱
درهم ۶۳
طلا گرمی ۲۴
خدایی این وضعیت برای کشوری که میانگین آیکیو جهانیش تو رتبه چهارمه اصلا قابل قبول نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83188" target="_blank">📅 12:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83187">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">روبیو وزیر امورخارجه آمریکا:
از این پس هربار ایران تلاش کند به ناوگان امریکایی آسیب برساند چه موفق باشد چه ناموفق، تعدادی از ناوگان نفتکش‌های خود را از دست می‌دهد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83187" target="_blank">📅 11:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83186">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f64e8a43.mp4?token=gNJrr5-WLmnlXGbIsiBLvZMXrPRN55-nsrJUAwCt1S6omiuY8a3XP2tm6YpXDSpecSSbfOke9YwG6dCCiEW2f5fXX1WlL0psUxC27B4KemumefBvnq6O27-vCdcnEXOi4Cbyt6Cq0bCxyGs1UE2Td2hpAcP01e0_ZfWFwj1n2pLQPC_34jwRqPUwKlfrTBxsokKfAHTZeAthhqg6QyGW4jiVakOiVJStEjt4KWRbojLbYj76EHbLqr2qbRGbJk1V0fO1MRkYVJoPugyOiL6NKRLKRmUGa5ZXak7rl_BHjhuq4rYis_9f2J_QZ4Lm7BAfCYydZUdt8RG_SdwpIys04g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f64e8a43.mp4?token=gNJrr5-WLmnlXGbIsiBLvZMXrPRN55-nsrJUAwCt1S6omiuY8a3XP2tm6YpXDSpecSSbfOke9YwG6dCCiEW2f5fXX1WlL0psUxC27B4KemumefBvnq6O27-vCdcnEXOi4Cbyt6Cq0bCxyGs1UE2Td2hpAcP01e0_ZfWFwj1n2pLQPC_34jwRqPUwKlfrTBxsokKfAHTZeAthhqg6QyGW4jiVakOiVJStEjt4KWRbojLbYj76EHbLqr2qbRGbJk1V0fO1MRkYVJoPugyOiL6NKRLKRmUGa5ZXak7rl_BHjhuq4rYis_9f2J_QZ4Lm7BAfCYydZUdt8RG_SdwpIys04g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83186" target="_blank">📅 11:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83185">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دالر ۲۳۰
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83185" target="_blank">📅 10:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83184">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lX1nI23ouj9WZuCyJyRvjRONSsB1b_Tm34uXGF-TdyPIVGBKlcX0ffD8wS4X2sjrsAMEqteVkMDCCKmlWmYmdXuqYOUVcGsk3mKrZv5pGbLRRIxNn3E0AWbLP-mwC3KBvoivMtgXkgV6PrmyPHPFq8BTrNuEI5VMSmNTPDC_saFG2bpAQWGXY5VWyoSof0xFMFd0H54YD4nrU4Uh0R2_MpbIIeZbiYrV5jHhXj2SWFwrxZKEYzlWtfwi4LiIiT-5DL_G657N2Sk7yP1a_4xLCbGGhhBP0GYOxUXutpPiOurXw-W5jIe6TtN44EYV6ohlLwf_BL_IB8T0YjCmuoXNEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاگرای ایرانی آماده باشید که عقب نمونید امشب از آیفون ۱۸ رونمایی میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83184" target="_blank">📅 10:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83183">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b7d8831e3.mp4?token=ZxT7BxIrLf4T6RVw8XKEcqDXsFXlT4m2fq3Wxj4CRxc5awfHA8t51bfC9qvxO-b9UM7xb06i66nSu8Yc6BBvXtPqCpJMgZx-HMVYkqhyUclmYZtl-VAzzNgrIykBUpLBOTof3xGlTFUeI5OarabfLbNlpJv6lYzmwXWnEpQ0tpiCmrzqp78jtVN818orULv9GDyGt1rIuSln201e5vcoKyHcM042URMuqN4LqO6xJFmazc64ULZeIBV-46vaBTR6C0exnhePqdte3IjdHcivQVPH-i6YIrgtPvqulg0VlJ4LZoBBA65T1sVI2hYdrn8iCC7h62QC7ikzFXGXZbSHAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b7d8831e3.mp4?token=ZxT7BxIrLf4T6RVw8XKEcqDXsFXlT4m2fq3Wxj4CRxc5awfHA8t51bfC9qvxO-b9UM7xb06i66nSu8Yc6BBvXtPqCpJMgZx-HMVYkqhyUclmYZtl-VAzzNgrIykBUpLBOTof3xGlTFUeI5OarabfLbNlpJv6lYzmwXWnEpQ0tpiCmrzqp78jtVN818orULv9GDyGt1rIuSln201e5vcoKyHcM042URMuqN4LqO6xJFmazc64ULZeIBV-46vaBTR6C0exnhePqdte3IjdHcivQVPH-i6YIrgtPvqulg0VlJ4LZoBBA65T1sVI2hYdrn8iCC7h62QC7ikzFXGXZbSHAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب سپاه بزرگترین حمله موشکی اش بعد از ۱۷ فروردین انجام داده، این وسط هم پدافند پاتریوت آمریکایی اینجوری داشته موشک رهگیری میکرده در صورتی که اوکراین بدبخت بخاطر جنگ آمریکا با ایران دیگه ازش بی نصیبه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83183" target="_blank">📅 09:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83182">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/funhiphop/83182" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
اپلیکیشن حرفه ای اندروید کمپانی بین المللی وی پاری
🔥
💖
امکان شارژ از طریق کارت بانکی
💖
تسویه حساب سریع بدون احراز
💖
دارای مجوز رسمی Anjuan وcuracao
🫣
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا، ترکیه و...
✅
کانال تلگرام:
👇
💖
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83182" target="_blank">📅 09:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83178">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdnlRQ2z8bY9RPp0xHNx_-dmrT_4VMdYdZe5BSx73bbDUxiTo0J-OYlvc0yHicOCfoh0RY5GwvKfeBdGn2MaDkRxLCBx6IUf7Jocaet_HUAVmMrO1yM7lp5XSM00p7SCrlbrFDZZHPEtUn1ExJ15fdNdsTBeAL0lbOAkKTGHsAEFDUZJNL5iz2Q9mmBA0oXtA-cWWw7RRPddv-8luri-h_htwhtjvl_7ogFycuAOxeyNCqMgLfFEJX8xOALcUUaq8UolcVjOoMIpeHZK-eid64egZcdirteBqMFela9gAZObNNGK5tipCaT-k7cyhk7rL1vFXJ2iFq8-PlGjd1vmyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیر تو جنگ بابا جنیفرلوپز ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83178" target="_blank">📅 02:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83177">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یکی از این موشکایی که میزنن اردن کسخل شه بره بخوره اسرائیل بخندیم</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83177" target="_blank">📅 01:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83176">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آمریکایی‌ها مثل نقل و نبات دارن پاتریوت شلیک می‌کنن
به زلنسکی که میرسه میگن نداریم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83176" target="_blank">📅 01:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83175">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">من حقیقتا دیگه بکیرمم نیست چی میشه، ما که بگا رفتیم چه کمتر چه بیشتر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83175" target="_blank">📅 01:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83174">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">۵ تا نفتکش ایران رو تو جزیره خارگ و جاسک زده آمریکا.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83174" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83173">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">۵ تا نفتکش ایران رو تو جزیره خارگ و جاسک زده آمریکا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83173" target="_blank">📅 01:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83172">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">جمهوری اسلامی هرچی داره تلاششو میکنه قبل انتخابات آمریکا جنگ شروع بشه و هی حمله میکنه آمریکا هیچ اهمیتی به حملات نمیده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83172" target="_blank">📅 01:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83171">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILs9TH2AxtG2DKymSq1hyW7V7mZWNoCIbdlHur7AZT1GaBa33rqeqwPbxrnu3SHe7Bpz-uHX6i8EWW0VRzY4py5Ph8Su9umZgYHOs6q6cjemC5YpRAmqEu-_qNRzrVKXKJqFUVaS9qpUCRq3MRkRs6aMdcfXPSdCrveFCcmFE6-xB_qLTtf019upxJb2EfUETUpi6c89tUgon03fspipLvZPJK3DpJcfcmTkKMC4ZAzUEKdKQpYNWvyUY31dok2dqFYTkvx0ois98uPQNPG9ttLAhbb4dpdk_GRuAUa0le6lj0gH7PheDAOUL14OYd0Kh5Wo54unStLagnurpi6t8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منیره جان افتاده دنبال کون مردم از کل تهران فیلم گرفته، اگه قوانین کشور درست بود الان باید دادگاهی میشد بخاطر همین فیلما.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/83171" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
