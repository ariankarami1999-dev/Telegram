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
<img src="https://cdn4.telesco.pe/file/KSisxuQEB-UYgrSishDZdc30S7ysmSCzbss_C6hvjfeykzK2pJxtp5cScts1_z82RtaXAyeceNCD89Bg29rdjCh6fhb86Q8qZCIoGkKVOJVhfCg4DdQug0va-uw2hYi3P07AY6sGY6R-9y3O-hylduHPI9K5pRj0RFu10hmB9jKoAKDd2t310QrE0CLvE8WLBDm66-7bfTeM7ASYlAcL-OqNE4nwwiQYs1hY6y6bzxQs3bAgmK-XuashUbH6Bl55Jitv84yhHvdOdgE_Zh7HPu7dPkMkzKmUwDAO_W3eFmifuknKopYhNa7-Mlcnz-q6zNvxwado6TTuItgJMV4vKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 20:42:49</div>
<hr>

<div class="tg-post" id="msg-448793">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73925989f.mp4?token=ojmQthLZO8cUMruAUtTFkdSe5I2OZAhB-3cy_LtegAo8zbX9QLT00fhbiUcwdA-I1S3r4IbgyAvmahmzSL84wS9CDI8iZbldZyJPYk3u_HZVBmhz2qL58zPdGsrt4UKxzcnabRAvDy4Dxk7-QbXINBf8BHxt8gGQqhtowvC9j-AneHMsgQlPpjfveq349YWupPdFmnI0p3kbsvhNg2eiH0Wsqo1jvMFgj7wTjHnZtuT8JUsoOQAv6h9iyAPdwdY4rAAzBsEMppbjne2Qw5Pg3qQfIaXwriRQ-N-S_7CnmlO8XQbSqB0xyaRVxjocWHyOq6zZtq4tv4odKIqb5HQFUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73925989f.mp4?token=ojmQthLZO8cUMruAUtTFkdSe5I2OZAhB-3cy_LtegAo8zbX9QLT00fhbiUcwdA-I1S3r4IbgyAvmahmzSL84wS9CDI8iZbldZyJPYk3u_HZVBmhz2qL58zPdGsrt4UKxzcnabRAvDy4Dxk7-QbXINBf8BHxt8gGQqhtowvC9j-AneHMsgQlPpjfveq349YWupPdFmnI0p3kbsvhNg2eiH0Wsqo1jvMFgj7wTjHnZtuT8JUsoOQAv6h9iyAPdwdY4rAAzBsEMppbjne2Qw5Pg3qQfIaXwriRQ-N-S_7CnmlO8XQbSqB0xyaRVxjocWHyOq6zZtq4tv4odKIqb5HQFUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خداحافظ آقاجان
@Farsna</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/448793" target="_blank">📅 20:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448792">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHv7QRe971gWVcJaR6Y8rLKSK_USUVWbKfKB5BwTKSUEUgbe0OFiv_frOUw4KKXIugfU3h4NyOiyVldzcdB65A8kfazNczBahc4FN68wLULh3D-5Axxt_2TprS7j05RA0kNeydCRy3yfgfCAVYsk-hvMWd2mguJh5HV_Bs6Dq5EFHQpKm9WjZerCflwjyWCVDGHE4R7oiKUyHW47u9kf_5qt9H5GgSwCssP67iw7FMMsV6De9-oDyqGZy9Xu1cjKt6cB_hOUP2TEMVtTnIG8NxQw3KkUD_UtOF5XTrYvveT648EM4mHnbz-FtUW5fxm1Nncqh_UYS29ukPgrTIcM7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
خادم حضرت خورشید به آغوش حرم باز آمد…
@Farsna</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/farsna/448792" target="_blank">📅 20:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448791">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8329395b4.mp4?token=MowG9tV_FyOaca9h6T_nxIqf1N5QNwvIOz2VYFodkR5kHbBOuR54MheJI2DXqS9LtEKBHMpGuJXOAGcHO7k_25WTVW1ZOvcN_xkvKdP-Imx-0tPlBLRRSbdBO97dyqzML6P62eQ2XIfyb_kLcA-jNtIUwTb_R_D5obyBTBM-kB2clx86OpezYczTLJqhggJmMh4yIlAYf-JcvBH0aBgTq_i4516hZCiNg0Qf84AaBH1J05J_lOz2-RsOOEsfH23LsvgfAS6u7E_W4iDSq-gVaam3hkXhoRJs5fA51cLikdGkEGZVl-CgoiZmdZlSwPNhd3AzG8wZzs0PTHVb86q5Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8329395b4.mp4?token=MowG9tV_FyOaca9h6T_nxIqf1N5QNwvIOz2VYFodkR5kHbBOuR54MheJI2DXqS9LtEKBHMpGuJXOAGcHO7k_25WTVW1ZOvcN_xkvKdP-Imx-0tPlBLRRSbdBO97dyqzML6P62eQ2XIfyb_kLcA-jNtIUwTb_R_D5obyBTBM-kB2clx86OpezYczTLJqhggJmMh4yIlAYf-JcvBH0aBgTq_i4516hZCiNg0Qf84AaBH1J05J_lOz2-RsOOEsfH23LsvgfAS6u7E_W4iDSq-gVaam3hkXhoRJs5fA51cLikdGkEGZVl-CgoiZmdZlSwPNhd3AzG8wZzs0PTHVb86q5Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوای «یا حسین(ع)» در حرم امام رضا(ع) طنین‌انداز شد
@Farsna</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/farsna/448791" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448785">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s-X8ylgJaaxfO2KWsAzW6dF1H8gm4WT7pd3YQlUEg6LIOWYFCIpUrGG94YKy3G-LkPxn0cwpH70_x5u7LUFz7F1LHw0z9uZXow2rKL4yCwUtMh47aWB1Pan6J-1TQ1YmupRmnB-kq8owyg-V72vv2ZA5QhLmXbH0X9oeljaIhCNFglIgxBobxJeMgm_3raHBg0u2X64WJyJ-K3xgd2UDDWYYXOIibIslMlDREkDFKNqA5JBQBfX2RK4taU3p1zN9NpId0XGgJKjX_glK7TpUxOc1OVPZ34IWwbnhITdVvwGrw2p1k8Kd9uQ51N8TXVY21S9mqDFuWoHOezv8aMvWMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hYaZ4TPzXcsUBVRmNfSuDB3sxnNHqK2h5-06vyPmsK8nLC8cTB-X5j4V0kzGizXx6E1y0LDcGdXlF81oRFkN0szboz4HdxgCz8aVzNXE4AYjtpaMF3W6AMeTxfIJVO6IEueVdH-pcZ-KTmwGb1lfG2cezm6G8GvRuu3pZvLUzjsHRxK1RkuLgpn2Tc6BeYvl8F-SxzbbMAt2xlK85fzFfbWjkz-BIIbo2MLFRMTa128KUxBrBgoqBHj4wsgnoV33AD6QSzh1LIwfbXRSD6aulgfuSgkx_GaH7LE2Rol0dclVlxzd_GFzeFY3fdMGP2rtG8Z6G1a45Nwf8GZLyg7svg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qf-YQ4V339KCyf9ji8FQmL--SAtQXlipwT5OmZVxUOhEN8joEHb64fdtAiNKPd0mZA2E0008OVJd9acoLmwySupF_edKhoeYxNyPMtPKP7dvVtC6Y9266h-v8Gymt_SYIqihOH295pmaDpC6HWVll6fnyrAgOu9fjn63Mj-q5elrfLLQRm6CL2ymgKwlqLjhSM6ScLeCOAiALiFvZHBB7-pJlF21MUw4LkfXwUI_SrSF83bTlhGUpa4ur8CGNzdPGTrWfraFeFnOv0EEG9l6c_d28PCyXcyVUsu5kOQXsgfLvF078t2AvLW5dczK5f2HVAoF50Onjz65L9-zm91G8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgEaHVvYOFbLb_uRxSi8ZHwW2ezDWMf8VAZhub92j9UxcmeVxrKIwiXX_r-equf-LRs4duU8U9ErmWGAkb-vef9BazggV3O7zaG6jCpqZER5uVMyKmZcFSegKJ9nPKTFcZF_wFQ_E_qhE23bqEnqFBs2472OOqpbHUlGVsQEzD4yLxL5-qSujmUuDsQj7bo3TMx-ySGe9iKpcjSRgMJqW5BYykIGWC-2uaeGkyyhV28nGDzD1lWwWSsqTIue1TNxDSzDTKvEg20aQ7F1lhSVCvOAksmqjwG9Y1iOaZYOS8bQSD4POa8WP55bSlG7HUxjUzTmrWu5S1EYReswmljWnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_jnDpGqiZkUc9aFpVXlQkZ9tcO1w8Wqbg0Ecqw1eoHblGaneJRPu43Q5q8I9EeQkzcUocVSQdVJI-FCs447ks1zvJ7_l6zzaYYwUfhNACN7_njHVyP6jfdurp2RJXjIU7wTzK93zYJmTYZkxupfo4SkUzfFZYOYmn1YGdDsIJSC8OzTjv3QYrE8UHKNhJfK_NthY4Bd23WsMdoTEk6BcKL82tIaJW4Eh6im-IYLNedGv4OJn5diVbwG4QIElzPBNi2i29ZJ5icjepqYANIQIUxHYJXEnbdiot-_c8xJK-kmYJ0IQSNdixqvkmwdc1DzWhC-n08FEWWvWOqVOu7Gew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R8anTp9_IQQzXI-HgRCOH1M3M2ADcZvjXPT4GfN5VfGLX8qArfP7qc5b1fd45cUb9-bE9AzCK877ZKe7htHg997wPSh9AvWanSeMAewspoaTFj2y-8VPvTtAW3-Zhr7oi97ZvFq1mJ59oCQClw-gyFOx4AdOB0tCU9dSOTLq56_8KNPkVwHasDwmjOVsPk_PvXJFPgKYEdakuaHCLu9ZiiIKQen_OV2N9tr-5FXooJaFPcz37nN9RsaBr2k_unS87VTuvNftyMkZMk9aR0GELkhHUj4YlYjZuA3u1ciwaBoRhBWl_p6wH3eXmSO0yo_HPUSrX7aX5UfAbNHoPjK8Cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر هوایی حوزه هنری انقلاب اسلامی از تشییع باشکوه پیکر مطهر رهبر شهید در مشهد.
@Farsna</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/448785" target="_blank">📅 20:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448784">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqjSFpMqyOBsAevkKyD2Zs9wRH_qSDwY4lb_OjYjN9dfvbiGQPBoLhLo9t1EvvVBXemGb33TLZrpWISShlY45S9C-h49HuVEk3IbOW4JiLEH4uLApFhWaGXRtNRbJ6dQgXO30agtrR0bIC-gq8sREP_6UCUmtuaERvfCuGNl58LumJNZ2jlQNzcUFEQIUfmOo4DZ0InJrC1bgd0rx8GjzXtwMkgPnfYadnvuB-W64o9A1Gro8hSMAuHVmQcjcQAaLuuQ765TZhRVrCQwYoxqAoV6l3yb_z8xHzBvakYNBILyEaScwwCFzs06rlh8iuzBP2d7GvQwn1f1fzec7cdJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔖
واریز سود سپرده‌های بلندمدت، فعال‌سازی خدمات چک و امکان مشاهده مانده حساب در بام؛ تداوم بازگشت خدمات بانک ملی ایران
آخرین خدمات فعال‌شده را در ادامه مشاهده کنید
⬇️
✅
واریز سود سپرده‌های بلندمدت
✅
مشاهده مانده حساب در بام
✅
سامانه چکاوک
✅
رفع محدودیت مبلغ استفاده از رمز دوم ثابت
✅
صدور کارت جدید برای حساب‌های واجد شرایط
✅
انتقال وجه از حساب‌های فاقد کارت در بام
✅
مشاهده صورت‌حساب در بام و شعب
(از ۱۱ تیر)
✅
وصول چک‌های صادره بانک ملی ایران
(در صورت وجود موجودی کافی)
روند بازگشت خدمات بانک ملی ایران ادامه دارد
🔹
🔗
مشروح خبر...
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/farsna/448784" target="_blank">📅 20:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448783">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/farsna/448783" target="_blank">📅 20:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448782">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ef055869d.mp4?token=NEruy2NVF3o-Ym9-nctzleapVbOMMAvKieDzAcoGZRVazuCifHg9TveuTZxxFdGv3jWt04aqetshKWbmYuajpEkZWJ73ASwIWDwQJBczN-d3MPbZzX0C1zhq8ju5-bEYr31YGVHHoCUFRh42Lk8EHjKi4UjAijpE-iVZBiD4O_oPxK9c9utLQ-K7BUeM77O_f0_N3_ZKH2JGOC1Ffd1we4MLawNw1mbzL09oShzUFw5BP5gDcBecdcZusVaJCvU-T5vm3ao9lU2RhMSXMR5mNws_x0NQ5GfmPnHFowflxD7SQ9HXxPSKFUm3dGxWUeaT6iEUOv6eiZ5TUhD52Hx9hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ef055869d.mp4?token=NEruy2NVF3o-Ym9-nctzleapVbOMMAvKieDzAcoGZRVazuCifHg9TveuTZxxFdGv3jWt04aqetshKWbmYuajpEkZWJ73ASwIWDwQJBczN-d3MPbZzX0C1zhq8ju5-bEYr31YGVHHoCUFRh42Lk8EHjKi4UjAijpE-iVZBiD4O_oPxK9c9utLQ-K7BUeM77O_f0_N3_ZKH2JGOC1Ffd1we4MLawNw1mbzL09oShzUFw5BP5gDcBecdcZusVaJCvU-T5vm3ao9lU2RhMSXMR5mNws_x0NQ5GfmPnHFowflxD7SQ9HXxPSKFUm3dGxWUeaT6iEUOv6eiZ5TUhD52Hx9hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مردم در حرم امام رضا(ع): این همه لشکر آمده به عشق رهبر آمده.
@Farsna</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/farsna/448782" target="_blank">📅 20:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448781">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تردد قطارهای مسیر تهران-مشهد متوقف شد
🔹
راه‌آهن: به‌دنبال حملۀ جنایتکارانه دشمن صهیونیستی آمریکایی بامداد امروز به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.
🔹
تیم‌های فنی و عملیاتی راه‌آهن بلافاصله به محل اعزام…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/448781" target="_blank">📅 20:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448780">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">امشب برای آقای شهیدمان نماز لیلةالدفن بخوانیم
🔹
روش خواندن نماز لیلة‌الدفن به این صورت است که در رکعت اول سوره حمد و آية‌الکرسی و در رکعت دوم سوره حمد و ده مرتبه سوره قدر می‌خواند و بعد از نماز می‌گويد:
🔹
«اَللّهُمَّ صَلِّ عَلی مُحَمَّدٍ وَ آلِ مُحَمَّدٍ وَ…</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/448780" target="_blank">📅 20:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448779">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3XvhU5LoPzHXsXmcyW4sZqf74a94RJC-Et7dh1eDhxJ2AwNoMj5wFzXkoeKpEYMKAF7Onoaxocp9gkN84o7BjAGz10CgWXqv5kDsKpuy0NuvXDcHJQBhYReDQNInj1J4PnOREuhaaeYZvw5cE8F7K8pY2q7okip7yLXxVoYhtvWs5r3OJRklKlsILcqt0bFByjSIp7TXNH7jMRnoJpWJs6tVRcCAeH2flz6AJE5SYjcXXikdpMgkz_z2RPlYBh5se3Msu5VncQNwgd_hmDabBD9pAUSbRW0Almkd02AERf0oCsm2atOfee0ywdgLSbq26B8AnfWUmBcAflYueaiww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
رهبر شهید انقلاب اینجا دفن می‌شوند؛ رواق دارالذکر حرم امام رضا(ع)  @Farsna</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/farsna/448779" target="_blank">📅 20:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448778">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d99ff886c9.mp4?token=r_H3Dpt0flV-MRTDLkQ3xiIvtkEotgOZeA0sz8YoPPChNnJ2y82whpZeEjxzdj_3Yo9u2-FUU2SGqtAB7ax61SdAJaPovRAEclYZP7AIxU9nFnMH-WycrV0l8KXNaG_UaQtRI54etjTbr0rmF-e4hOjj18WIQvOiGVcyjHlRpXUABWHhhGdwNOckZafjjcy2mGZVWU0FecqfNXi0O1W03vlinss_qpQk3LxGxwB42pLeueYpdqPueXxu8sPrOgxP70ZXARofHrgtsaivSori-VefxYCgHFfEnfuDXEMiAXw1seFe4DBrpLPR5oswj1SUfFqfF10wR047yMxiP5pHbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d99ff886c9.mp4?token=r_H3Dpt0flV-MRTDLkQ3xiIvtkEotgOZeA0sz8YoPPChNnJ2y82whpZeEjxzdj_3Yo9u2-FUU2SGqtAB7ax61SdAJaPovRAEclYZP7AIxU9nFnMH-WycrV0l8KXNaG_UaQtRI54etjTbr0rmF-e4hOjj18WIQvOiGVcyjHlRpXUABWHhhGdwNOckZafjjcy2mGZVWU0FecqfNXi0O1W03vlinss_qpQk3LxGxwB42pLeueYpdqPueXxu8sPrOgxP70ZXARofHrgtsaivSori-VefxYCgHFfEnfuDXEMiAXw1seFe4DBrpLPR5oswj1SUfFqfF10wR047yMxiP5pHbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زیارت امین‌الله توسط بنی‌فاطمه قبل از شروع نماز بر پیکر امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/448778" target="_blank">📅 20:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448777">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcc86d82c8.mp4?token=ZDr-CRa8LxVdqE8jUjNz1GUonIbKlBgfkw1weBdMajJPS5tCIUZ2j0mxebMK6VTgxu47TFZY50B_LxFyGMZj6389bvOKUQ10jewje2l6z4kvce1yHBDBrQZEBt8_iFgZ8xaVfeZByxFkx6C6mlyy_rKCjF2uh4NX-aie5jzIgNeut3BJyBlBFwmIWFRs8kt95MdT_I4-LFVH1p0e2WKGtVMkwVW-NQcNXZW0OqjC-CL36EcCewGq4XhaH9Em2N9l7wkhEdlVEOCJ6ClGed_EhTS1dgDJWb8Djzg6rPTV7I0PTR0ijYUOLxkbH-bYAxKNPdAUZJr9V8ZYgJCUqNNbUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcc86d82c8.mp4?token=ZDr-CRa8LxVdqE8jUjNz1GUonIbKlBgfkw1weBdMajJPS5tCIUZ2j0mxebMK6VTgxu47TFZY50B_LxFyGMZj6389bvOKUQ10jewje2l6z4kvce1yHBDBrQZEBt8_iFgZ8xaVfeZByxFkx6C6mlyy_rKCjF2uh4NX-aie5jzIgNeut3BJyBlBFwmIWFRs8kt95MdT_I4-LFVH1p0e2WKGtVMkwVW-NQcNXZW0OqjC-CL36EcCewGq4XhaH9Em2N9l7wkhEdlVEOCJ6ClGed_EhTS1dgDJWb8Djzg6rPTV7I0PTR0ijYUOLxkbH-bYAxKNPdAUZJr9V8ZYgJCUqNNbUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دختری که آقا را با بغض تعریف کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/448777" target="_blank">📅 20:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448776">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnLby3c_pG4ysfqZBxZqib__RGsMOC7-LNQijR2zaXrUFfLdg-U0rOJJHS_Cqg8P-GGWT_BqnBog_yWTrNL8JQTdy37jL--pFFbxNSWDwPA8z38mOKlaULYqg_EklRWtEpK-bfA5h1nl23MAUHFYlQfKvE7gnTs6Htp-oSjow1j6GTfEtAgEB9g3tA1NGQKhYt3w36QW6DpsLmtsFge20yDGSETTuMQSVKPp5th9NiR8R-4konVL4_xS0-myAAW5KPj5eEKhRhE56y7PnaZgk2aX6Exa-w_qMK7qSghcggpgoqkC_vpd38J0dJa-L3Oley90mni9c_DMWfI2kPL-wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ما همه خون‌خواه توییم خامنه‌ای...
@Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/448776" target="_blank">📅 19:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448775">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1280170218.mp4?token=r1QK8v2n1QJVNey6e67h9c_ux40Bd2iGdW41pAdEBe9_RhZepJznfVizV_CuPoPJghcfQP4BWuGokC98RfOJI94ZD_bIFaHIaYo1OxvCPHWVsMYeWENE60vuUnnEACaMI0CkyWgTqkS3_yKxryj0tMQXgx6-WkWQ85Tny-ufksfLnhqxUIzTalbOJ-m1vO-8TnnFHHfq8YsnaW1AFE9zSjceKTOiIzAVr5jnm_mT7RIifaIXTei5IO0PRmgOJOKCa0xJk1LgpiMZDYrLyLeUxabZBJo89bE5YAYgHSR2cONecPJJEUK2DBRG70cyFjnORuPek3ddnbesDXQZe7AwVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1280170218.mp4?token=r1QK8v2n1QJVNey6e67h9c_ux40Bd2iGdW41pAdEBe9_RhZepJznfVizV_CuPoPJghcfQP4BWuGokC98RfOJI94ZD_bIFaHIaYo1OxvCPHWVsMYeWENE60vuUnnEACaMI0CkyWgTqkS3_yKxryj0tMQXgx6-WkWQ85Tny-ufksfLnhqxUIzTalbOJ-m1vO-8TnnFHHfq8YsnaW1AFE9zSjceKTOiIzAVr5jnm_mT7RIifaIXTei5IO0PRmgOJOKCa0xJk1LgpiMZDYrLyLeUxabZBJo89bE5YAYgHSR2cONecPJJEUK2DBRG70cyFjnORuPek3ddnbesDXQZe7AwVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب اینجا دفن می‌شوند؛ رواق دارالذکر حرم امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/448775" target="_blank">📅 19:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448774">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe69692a2.mp4?token=hGfpaVPssdSn4wq8cYyI_MDj8I4SiPnfNtiJkRHYr6njy3e5V9XA6bk3Ay3_7j1bb1IAwpB4nyOd_pNsbfDrYEvwEiW8pY4PosTt8lyTBESQq_HoKo1RmBnoIhCmjwia7HHGoR3ct0bY5hvtEJl4bL4w0LlBFrjKzwgoOfn6IzEaTrm9r-iPJsClyoX24NgqeDQ4RmD3D9k9dJYNy78eq0zXSyJvwNrQHkURP1II3Z_l4ocZssVZ-UkvFJ6viLwP0Is5VSK4n_jZoud6PByengBmFMEUoSqEIk91Yr9WJx1PpTiHSfOmjpqW6LL2yRaMJvUoQCYVyNMDVgdVv6qofZGh9YOx35HHLUYhbrJhIIfDAYgNs2aGZtQpVvj9R5xGwjJ_HCh_H9G72TleFU_Ne9L14XOnh09ZMeo81BOaBNq3D4TZY-6XziEbmzzrLx_KzMzjkRuDPU2kYSt7BpmVFtp802ANql0Ku-fPY4Jalj6QkttuAiBDmPMxvdkxaca2QWh-7w8-6t2FmuilDJGuLKfiESFkEFUA-UUYdsWt8pMRDSSjCXxhm1FWLKrUBDCWE-KBjgB27pJOA63LK4JtZ0wkAuTyypOVhKy6JauF2PCVxLNGaGH9w_j-wFh5YsI7enc--W9Jat69L7UNEnsH1OzQFASxyousLE_Bf8URSdY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe69692a2.mp4?token=hGfpaVPssdSn4wq8cYyI_MDj8I4SiPnfNtiJkRHYr6njy3e5V9XA6bk3Ay3_7j1bb1IAwpB4nyOd_pNsbfDrYEvwEiW8pY4PosTt8lyTBESQq_HoKo1RmBnoIhCmjwia7HHGoR3ct0bY5hvtEJl4bL4w0LlBFrjKzwgoOfn6IzEaTrm9r-iPJsClyoX24NgqeDQ4RmD3D9k9dJYNy78eq0zXSyJvwNrQHkURP1II3Z_l4ocZssVZ-UkvFJ6viLwP0Is5VSK4n_jZoud6PByengBmFMEUoSqEIk91Yr9WJx1PpTiHSfOmjpqW6LL2yRaMJvUoQCYVyNMDVgdVv6qofZGh9YOx35HHLUYhbrJhIIfDAYgNs2aGZtQpVvj9R5xGwjJ_HCh_H9G72TleFU_Ne9L14XOnh09ZMeo81BOaBNq3D4TZY-6XziEbmzzrLx_KzMzjkRuDPU2kYSt7BpmVFtp802ANql0Ku-fPY4Jalj6QkttuAiBDmPMxvdkxaca2QWh-7w8-6t2FmuilDJGuLKfiESFkEFUA-UUYdsWt8pMRDSSjCXxhm1FWLKrUBDCWE-KBjgB27pJOA63LK4JtZ0wkAuTyypOVhKy6JauF2PCVxLNGaGH9w_j-wFh5YsI7enc--W9Jat69L7UNEnsH1OzQFASxyousLE_Bf8URSdY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این پرچم‌ها نماد خون‌خواهی است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/448774" target="_blank">📅 19:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448772">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ردپای عربستان، امارات و قطر در حملات اخیر به زیرساخت‌های ایران
🔹
داده‌های وبسایت‌های اوسینت و مراکز هوانوردی از حمایت‌های متعدد جنگنده‌های آمریکایی توسط پایگاه‌هایی در کشورهای امارات، قطر و عربستان خبر می‌دهند.
🔹
برخی منابع خبری  مدعی شدند سوخت‌رسان‌های اماراتی در حملات بامداد چهارشنبه آمریکا به بنادر ایرانی کمک کرده‌اند؛ داده‌های رصد ناوبری هوایی حضور دو هواپیمای تانکر حمل‌ونقل چندمنظوره (MRTT) در عملیات هوایی علیه ایران را تأیید کردند.
🔹
این هواپیماها توسط امارات متحده عربی اداره می‌شوند اما تا این لحظه امارات این اقدام خصمانه را رد یا تأیید نکرده است.
🔹
ایران در جنگ رمضان چندین فروند سوخت‌رسان و یک فروند آواکس آمریکایی مستقر در پایگاه الخرج عربستان سعودی را منهدم کرد.
🔹
مرکز ناوبری فلایت‌رادار، فعالیت هواپیماهای سوخت‌رسان از مبدأ پایگاه العدید قطر در حمله بامداد پنجشنبه آمریکا به ایران را تأیید کرد.
🔹
پیگیری خبرنگار دفاعی و امنیتی فارس از منابع نظامی نیز حمایت لجستیکی قطر، امارات، اردن و عربستان از پروازهای متعدد جنگنده‌های آمریکایی را تأیید می‌کند.
🔹
پایگاه‌های آمریکا در این کشورها در حملات ۴۸ ساعت اخیر مورد استفاده قرار گرفتند.
🔹
آمریکا بامداد پنجشنبه حداقل سه زیرساخت مرتبط با راه‌آهن و صنایع نفت ایران در شمال شرق و جنوب کشور را مورد حمله قرار داد. حملات به زیرساخت‌های فرودگاهی در چابهار و قایق‌های صیادی در عسلویه از دیگر اقدامات تنش‌زای آمریکا در نقض فاحش تفاهمنامه اسلام‌آباد است.
🔹
عبدالرضا صدیق، کارشناس حوزه امنیتی می‌گوید آمریکا با هدف قرار دادن زیرساخت مهم تجاری با چین، خط قرمز بزرگی را رد کرده است.
🔹
قرارگاه مرکزی خاتم‌الانبیا چهارشنبه شب اعلام کرد مبدأ هرگونه پشتیبانی از ارتش متجاوز آمریکا برای تجاوز به حاکمیت و سرزمین ایران اسلامی، هدف مشروع نیروهای مسلح ایران خواهد بود.
🔹
ایران پیش از جنگ رمضان نیز به‌طور مکتوب به سران کشورهای حاشیه خلیج فارس اعلام کرد مبدأ حملات به کشور خود را هدف قرار خواهد داد و این وعده را عملی کرد.
🔹
رضایی، سخنگوی کمیسیون امنیت ملی مجلس معتقد است با توجه به اعلام قبلی ستاد کل نیروهای مسلح، زیرساخت‌های ترابری دریایی، ریلی، فرودگاهی و زیرساخت‌های حوزه نفت و گاز در کشورهای عربستان، کویت، امارات، قطر، اردن و بحرین به عنوان ایالت پنجاه‌ویکم ایالات‌متحده هدف مشروع ایران برای پاسخ به حملات ۴۸ ساعت گذشته آمریکا به زیرساخت‌های کشور خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/448772" target="_blank">📅 19:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448771">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E95pPLGVa5orc_UKIwwj_KUjHtxgcQ3g9UYGdAAtqJQkN768CdquIYY2a_oPK-u4UtY6Vevyo9Xa6JiP2mIwSl_8SLPq7QLNnGAv0iyAnxCJe8drnxHCFzxy7M3SbYQaS_z5vtPSPXWkhIOKgBo8aIq8brsy72oWmBV1Se3J4Y15xh4Wcm-OPzLFhfUL5_CzkKUGJ1WUVRjMCb3S2rbNfKrsWgU5fbhJjSAak6GZZounR_FrUBsq0bKGzfp7c2hkY7jpjO2tcNgT-1jWiIpBUwvxrWfIe-3zN2KpF4aOx-O3F-QDakoaspuVei8T0cN9UGNrofG_nLAdfpofP_RtfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
یاد آن مشت‌ گره کرده...
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/448771" target="_blank">📅 19:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448770">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01cfcf412d.mp4?token=Wm10ema39au6t8aSa5C7R49C38p_PE-nXZI-hGTx3NjsFHu0CElau_f_2gLnL7jdVBjRpXWLQJnrqoFdRvDGPm_KQvx4hXz9D-4oA9NRTNfqTmehqd3hV8p8Fm4zI1zrslOZbw4YUfGbFHTNXlbZ1mgOwmadrRjCP7iL-Z-ggS3RpRDnhFLk4wI0XDow4MVz7QND91QUThfFBlksaatTxmTnBnU6XrBRTkP0Ke1MCLm5gKVMD4dQn96hMr5q9hQeUvtH9ePO7URX7a-aLMqQDX6nfMUoMevU-1x-U-NIi_p8LWHHirnBzSsd5aEeShcwg41jvRBy6wJESAxbvJGaWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01cfcf412d.mp4?token=Wm10ema39au6t8aSa5C7R49C38p_PE-nXZI-hGTx3NjsFHu0CElau_f_2gLnL7jdVBjRpXWLQJnrqoFdRvDGPm_KQvx4hXz9D-4oA9NRTNfqTmehqd3hV8p8Fm4zI1zrslOZbw4YUfGbFHTNXlbZ1mgOwmadrRjCP7iL-Z-ggS3RpRDnhFLk4wI0XDow4MVz7QND91QUThfFBlksaatTxmTnBnU6XrBRTkP0Ke1MCLm5gKVMD4dQn96hMr5q9hQeUvtH9ePO7URX7a-aLMqQDX6nfMUoMevU-1x-U-NIi_p8LWHHirnBzSsd5aEeShcwg41jvRBy6wJESAxbvJGaWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ای جهان از دادِ «حیدر حیدر» شیعه بترس
@Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/448770" target="_blank">📅 19:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448769">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02f558405c.mp4?token=nUOd-rW9qfh7rfnhmMvKi4aNxRCo4-q5lhpK-s_WM2-N79Z6HkBPmC64xzS14eVuWuZ014RfKRzUkzvk_3xEl39nXBAz_kiS8DdFgOMPhHepGovVaEQE_rTBlWzVV4P4_qni7WI5E3qM_DFzsXFkRwQUTzZ017Qvj8xSNUEGl3Iblj_BLEdaAmdczvWMhitZVUErs7dmdFbjgdaYZfBq3Di_THcVpZefr0sRdeZ12ierW3h2rlS-prcK0Cfj6EtnQ_-wqZst45oJaX1cEbLvaHfh45n429PNksgfHo29wKXGtUChFC9kWaUB-hoGrlgJrFRCcQ7a-UrJt7rqn6Dw9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02f558405c.mp4?token=nUOd-rW9qfh7rfnhmMvKi4aNxRCo4-q5lhpK-s_WM2-N79Z6HkBPmC64xzS14eVuWuZ014RfKRzUkzvk_3xEl39nXBAz_kiS8DdFgOMPhHepGovVaEQE_rTBlWzVV4P4_qni7WI5E3qM_DFzsXFkRwQUTzZ017Qvj8xSNUEGl3Iblj_BLEdaAmdczvWMhitZVUErs7dmdFbjgdaYZfBq3Di_THcVpZefr0sRdeZ12ierW3h2rlS-prcK0Cfj6EtnQ_-wqZst45oJaX1cEbLvaHfh45n429PNksgfHo29wKXGtUChFC9kWaUB-hoGrlgJrFRCcQ7a-UrJt7rqn6Dw9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غم‌انگیزترین اذان مغرب در فضای حرم مطهر رضوی طنین‌انداز شد
@Farsna</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/448769" target="_blank">📅 19:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448768">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51aa105312.mp4?token=TDrzYROODFOQbD1JDHFoXFY9BQBVVhmCxsfo9ZWaUlqRjct7FsA9Ds9JSMwKsd-FLqziJYU1vQmkzg-CBU-zL5GTThUxD4IUXpIpbW0Hl1cm6iUyDQlPEHrqovN2NlLb-GikYb0WE1CFpuYoG9Twp467jJJMzCPlHkdBmF_TU_BOnVAMzDrrs6NVnO4nuTOjQZhuUhcLDluXktHM6x2_CNjXVSHOc8KeIsRg0Qdf9SikVNtdvVcqC7XADLJy5D0ZvGOGB7GYP2A4qUxLhurOq1ZXZCDpp-zukj8joCry4qdHJuhi1HaOh8nnW7k8xCsTx8TPS8-wb6Od-0oH_eG9XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51aa105312.mp4?token=TDrzYROODFOQbD1JDHFoXFY9BQBVVhmCxsfo9ZWaUlqRjct7FsA9Ds9JSMwKsd-FLqziJYU1vQmkzg-CBU-zL5GTThUxD4IUXpIpbW0Hl1cm6iUyDQlPEHrqovN2NlLb-GikYb0WE1CFpuYoG9Twp467jJJMzCPlHkdBmF_TU_BOnVAMzDrrs6NVnO4nuTOjQZhuUhcLDluXktHM6x2_CNjXVSHOc8KeIsRg0Qdf9SikVNtdvVcqC7XADLJy5D0ZvGOGB7GYP2A4qUxLhurOq1ZXZCDpp-zukj8joCry4qdHJuhi1HaOh8nnW7k8xCsTx8TPS8-wb6Od-0oH_eG9XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این غروب حرم امام رضا(ع) فرق می‌کند
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/448768" target="_blank">📅 19:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448767">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a61f3dd23.mp4?token=EmyIeTI_b8WhTeTO48iEGqT_PSvbyc9hdqzF_wkEkJ_F696UCN0hJrW0aLvRgTCiC6rAJCnu1l6QnNt6ni5houORhgrDjhtUViGoCdEbzSvv-heV1XtkUWgzF0jD_do7d0ijMb54wShoUUbc0FA7dgLXWRdSNW-S_ql_hOu6S-JNkXTl_nWZa2LDTnOUmjiC8oyD4Rr_egAjZRZIYchI808ZeeCxauO7nd3zLQskk9a-F_ApBbxKBo3XW3UJ7caFXgGBXnOEcZmTkCrncudW89VL8Nvu6-XPeSHyR0y9RdzpMXwj6u1S0ma206WXgsBdKJF_h1hXcLg5KX9zpEuKVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a61f3dd23.mp4?token=EmyIeTI_b8WhTeTO48iEGqT_PSvbyc9hdqzF_wkEkJ_F696UCN0hJrW0aLvRgTCiC6rAJCnu1l6QnNt6ni5houORhgrDjhtUViGoCdEbzSvv-heV1XtkUWgzF0jD_do7d0ijMb54wShoUUbc0FA7dgLXWRdSNW-S_ql_hOu6S-JNkXTl_nWZa2LDTnOUmjiC8oyD4Rr_egAjZRZIYchI808ZeeCxauO7nd3zLQskk9a-F_ApBbxKBo3XW3UJ7caFXgGBXnOEcZmTkCrncudW89VL8Nvu6-XPeSHyR0y9RdzpMXwj6u1S0ma206WXgsBdKJF_h1hXcLg5KX9zpEuKVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انبوه جمعیت در کوچه‌ای که به خیابان امام رضا(ع) می‌رسد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/448767" target="_blank">📅 19:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448766">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0388f0078.mp4?token=SxgZqEACS5pLwoMofOxuG14dsOgjl8ZeK2spdo0QDbJFxzcRPGMTKaX9-pb2po7FBGQLuBFP4hLUBEanjf5NepGs8QLpTj5L1b9vlgZCXg82hG_jx8rMFCYViEFFiG3g8LrrbFX331Q7KFk1LusN3LG3RdNHH93PbEABD-SR9wkqFzNhL7Xw3xAf9KBIBDuxaOLC74A2EB2wJh9rXmviNP3p3q3frXZsRdUn5cyxmQpEOioDwz4b7XGVlsMm6pUapLp_jiho_3F8dm_MycEfV2F2tWQF095i2VX-Ayp2e9M2SK-_-N0TIG2I12ZFfg0DM0iszgWh1_f_1SMYZWRg_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0388f0078.mp4?token=SxgZqEACS5pLwoMofOxuG14dsOgjl8ZeK2spdo0QDbJFxzcRPGMTKaX9-pb2po7FBGQLuBFP4hLUBEanjf5NepGs8QLpTj5L1b9vlgZCXg82hG_jx8rMFCYViEFFiG3g8LrrbFX331Q7KFk1LusN3LG3RdNHH93PbEABD-SR9wkqFzNhL7Xw3xAf9KBIBDuxaOLC74A2EB2wJh9rXmviNP3p3q3frXZsRdUn5cyxmQpEOioDwz4b7XGVlsMm6pUapLp_jiho_3F8dm_MycEfV2F2tWQF095i2VX-Ayp2e9M2SK-_-N0TIG2I12ZFfg0DM0iszgWh1_f_1SMYZWRg_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سلام ای زائر شهید، مشهد به این‌گونه آمدنت عادت ندارد
🔹
حال‌وهوای خاصِ کنترلر مراقبت پرواز فرودگاه مشهد هنگام ورود هواپیمای حامل پیکر مطهر آقای شهید ایران.
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/448766" target="_blank">📅 19:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448765">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73a592d33.mp4?token=XtR1lJffqgdD-wTCWrgHD_SpXddKiQrAIbP1wuPxT-4kcCvzf2uk6pVb7-qZgo6wWXeDU0HwhXeSN2_QtfALfVgyIuHC7igSiwLXqueLiWwwuxDcwYgnKCBZmUAxkCl3VNfUl7TWuFtcROcggyFWn9jGrs3yCHSmzJIbK93g1lNi7ISa64XE4lZQXbQMlWyScs8pH-1NcdmBIXOYwxOCJ3Ox7-6CxZ4U7SdG5bTn4ZuuFWkyowpdgi306Y8MjMwTZQ08hIYq_KtZattCJVI4qUfHMkls-K0nQubML-diY6D1lz3ndvY9XdSv9AQjocuHqBeNrADOQ57R7Rm_XnQkeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73a592d33.mp4?token=XtR1lJffqgdD-wTCWrgHD_SpXddKiQrAIbP1wuPxT-4kcCvzf2uk6pVb7-qZgo6wWXeDU0HwhXeSN2_QtfALfVgyIuHC7igSiwLXqueLiWwwuxDcwYgnKCBZmUAxkCl3VNfUl7TWuFtcROcggyFWn9jGrs3yCHSmzJIbK93g1lNi7ISa64XE4lZQXbQMlWyScs8pH-1NcdmBIXOYwxOCJ3Ox7-6CxZ4U7SdG5bTn4ZuuFWkyowpdgi306Y8MjMwTZQ08hIYq_KtZattCJVI4qUfHMkls-K0nQubML-diY6D1lz3ndvY9XdSv9AQjocuHqBeNrADOQ57R7Rm_XnQkeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مردم در حرم امام رضا(ع): نه سازش، نه تسلیم، انتقام انتقام
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/448765" target="_blank">📅 19:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448764">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a14e34a0.mp4?token=u3BLRbykJwNTHPeegnS6YKSPFrqfQAp0eTQN043JQDY7gWXPuiCMgP4ZVeiIWdIkbJLlN0_ihKQn5VD3TOYnqtklTz0-1FY4T0aDBuIBU7O5ak5-X6dE_OtxnIAXjJm55csFAzieCzYBGpXWu-c-J8b23CsvQty82UHuA7agrVRg52pyWN1k2is_8rELNP0Zn-3qY1BuUe160BXWvUbm5a7uVfHyupspVdza47MiYftUy_hyOWUnqN6sTVFonrzd3xy2gx9ypUhD1TOmaNB9g6TvetVHaMmDqeDmx_WguAglusX06z7XJEer-RPq67iDTNvGaa3VrAZo31sEDCfbQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a14e34a0.mp4?token=u3BLRbykJwNTHPeegnS6YKSPFrqfQAp0eTQN043JQDY7gWXPuiCMgP4ZVeiIWdIkbJLlN0_ihKQn5VD3TOYnqtklTz0-1FY4T0aDBuIBU7O5ak5-X6dE_OtxnIAXjJm55csFAzieCzYBGpXWu-c-J8b23CsvQty82UHuA7agrVRg52pyWN1k2is_8rELNP0Zn-3qY1BuUe160BXWvUbm5a7uVfHyupspVdza47MiYftUy_hyOWUnqN6sTVFonrzd3xy2gx9ypUhD1TOmaNB9g6TvetVHaMmDqeDmx_WguAglusX06z7XJEer-RPq67iDTNvGaa3VrAZo31sEDCfbQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ای اهل حرم میر و علمدار نیامد
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/448764" target="_blank">📅 19:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448763">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">چه زمانی امکان زیارت مزار رهبر شهید انقلاب فراهم می‌شود؟
🔹
استاندار خراسان‌رضوی: امیدواریم از فردا حوالی ساعت ۱۰ تا ۱۱ صبح محدودیت‌های حرم برداشته شود و زائران بتوانند به زیارت مشرف شوند.
🔹
به نظر می‌رسد از ظهر جمعه، مقدمات زیارت مردم از محل تدفین فراهم شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/448763" target="_blank">📅 19:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448762">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvcaIJ4bsQuF_DVUmofOtOrXDTlGX9tnEoaDz815YbJmtSuQtUi-7e9ndUMILfC8l6RLzk-dCFYRSc3Jc3v4o1NzmLJmd09KriSvFLQ8qeWItJDaYjaH3tYZtLjjneGllKhbn4QTJPy1pwl5ossJavbNYs33ONdD-JxRZJp_287VNweoXccCV8XhNB2TPWlYfaMGajzXA9Dg-SM2wngVCquphmbBn9gibejjO0Xbfj9B5OwFKQp90V8-JWIiYOArl_ENgsQjb_J1boMAI0l8ifqnmlTc7O_xw2mv7sBtOGdB8Mo_Dyw0mwkyoUblqBeyGL6PPo8wNeXLEgocpxMUOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قابِ ماندگار در تشییع امروز
@Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/448762" target="_blank">📅 19:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448761">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3886daf0c.mp4?token=VGshjsRouk4bw0rGFlF9dkeUtZSWSBtQ-LbYKxKpoPa0whRLdBbXTUxLwBaVWr86_rg4EPRoLKwqpfej764ejripqr3Eean261xhzCd6VtlSkHSM9Yb5f1CRLudM8j4R_NzsRsJPyuoMvMaiAIDCMZdtSKB9O_1G12HbyArlcVeXrsXVXpHHzO2bhlEeWuKkX_xRppgzowUVytr1uOaaa_QRfprEIvfFTHEOyblNd26BjPqrifQsI9F3DEhRrGnZIP1ZaE-a_x4yIDE0WQPhjxHc8ZhdEiULA7Qey7n6F5JlgEap7H8U-YvuXEIeS4nshaEBsZv3qvwQ_-rzqG1Ahw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3886daf0c.mp4?token=VGshjsRouk4bw0rGFlF9dkeUtZSWSBtQ-LbYKxKpoPa0whRLdBbXTUxLwBaVWr86_rg4EPRoLKwqpfej764ejripqr3Eean261xhzCd6VtlSkHSM9Yb5f1CRLudM8j4R_NzsRsJPyuoMvMaiAIDCMZdtSKB9O_1G12HbyArlcVeXrsXVXpHHzO2bhlEeWuKkX_xRppgzowUVytr1uOaaa_QRfprEIvfFTHEOyblNd26BjPqrifQsI9F3DEhRrGnZIP1ZaE-a_x4yIDE0WQPhjxHc8ZhdEiULA7Qey7n6F5JlgEap7H8U-YvuXEIeS4nshaEBsZv3qvwQ_-rzqG1Ahw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ جان‌سوز وداع آمد ولی جدایی از تو ممکن نیست
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/448761" target="_blank">📅 19:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448760">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
با توجه به ازدحام جمعیت در حدفاصل چهارراه دانش تا حرم مطهر رضوی، ادامهٔ انتقال پیکر به صورت هوایی به حرم مطهر انجام خواهد شد و نماز در حرم مطهر و خیابان‌های طبرسی، شیرازی و نواب‌صفوی اقامه خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/448760" target="_blank">📅 18:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448759">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fR32wUw9rRnpklIk07aB9Ctovw_g8KX1VCfVUFxRrC0hAoQ1H1jQ6bTTYPdxuSXinX1VfRdA1rSaVwjH5zeyf5BZnD5yuYJw5ypH6KnwD4LMvxSxnuuRcgkGOLf32QcxRRWwFG6hkiwQ8uAfMdniEMizIuiCfgy5bwkqwnkHZgwVUlPuaZkY3uBlLvHH4hxq7hnlwpPQoaUBEZNj3RZya0GGwPot-AoAxQ1UQMwmTMxnTjV8N6R1A1B6qNkXqeILm1_URr8IwzNZzwr973hCITD6Am-wRJ5udmE6Xc0r0B8-zM9hwt0zHQi_2CBF6FHMSY804DH05SBi3mE9risuRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور وزیر اقتصاد در تشییع رهبر شهید در مشهد مقدس
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/448759" target="_blank">📅 18:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448758">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d68f0b36.mp4?token=e8PajLC2FrIKjFOiZMFuWmkwFIioPnS6iWy6zP_6dKFaBLRLloPjvYiduPedSt3_GvDJHEsiNlCffu-M-Bj1_-qXMQm0KuiRMjOogBROh2KTElr8jRYPOiDUsNVlTfAWFANcJLE21q3Lq7OIg21U2ozozbkzL7WMeoCGsuuRzlFwGQacNV_yndlV4611aHJ8bhtk0oSMzkgggL5kwuz_eSP36MaVcpmV8ByfHmZM10f_fB9zmW2DZltuvmI-OsNR0zNx3Zmnw-ojM-W_l70IyJ_U55q4ZznidaT1IKaTQ6YhitW9JdeDIdoX4_42-Twg8AVjC_qsOlAdRrzm1J6ikQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d68f0b36.mp4?token=e8PajLC2FrIKjFOiZMFuWmkwFIioPnS6iWy6zP_6dKFaBLRLloPjvYiduPedSt3_GvDJHEsiNlCffu-M-Bj1_-qXMQm0KuiRMjOogBROh2KTElr8jRYPOiDUsNVlTfAWFANcJLE21q3Lq7OIg21U2ozozbkzL7WMeoCGsuuRzlFwGQacNV_yndlV4611aHJ8bhtk0oSMzkgggL5kwuz_eSP36MaVcpmV8ByfHmZM10f_fB9zmW2DZltuvmI-OsNR0zNx3Zmnw-ojM-W_l70IyJ_U55q4ZznidaT1IKaTQ6YhitW9JdeDIdoX4_42-Twg8AVjC_qsOlAdRrzm1J6ikQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرواز تهران-قشم-تهران امروز انجام شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/448758" target="_blank">📅 18:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448757">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">عراقچی در گفت‌وگو با فرمانده ارتش پاکستان: لفاظی‌ها و اذعان مقامات آمریکایی به عدم پایبندی به یادداشت تفاهم نشانه‌ای آشکار از پیمان‌شکنی است
🔹
عراقچی همچنین با هشدار نسبت به هرگونه ماجراجویی ارتش آمریکا، بر عزم و اراده راسخ ملت ایران و نیروهای مسلح غیور جمهوری اسلامی ایران برای دفاع از حاکمیت، تمامیت سرزمینی و امنیت ملی کشور تأکید کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/448757" target="_blank">📅 18:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448756">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSWtne6n7wh4QLuL8bthsLMTL5rWPZ4YJqPKaRQ97BOA5pvmbwd5_aLaRLSbfNrrIg1gbXwQJ5Osn4ceKxu10Pqcgplna97P2aS1r8x82ItpuEDzUOkYlNyy45cW4DhGh-TbJmWlS9xDewMeuWGA3QrD-92i7qMffYov005CmvNFO0JGnd7bS4oNoAW46dNkf1P5y2WYtBQV0lBJp4uXrtf6xCMcdJLp6iMNnhEWe8cpkk8yNNXpt8i0ZAu0F5kyfXkRf4hI6NSQYAXg7sGeVHfPFydJTcI279Mp98svzONqnF4xSjHVly_ySFRu-NGrFCcmNFQxXog3CxKr-e8txg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ باز هم بنزین را در آمریکا گران کرد
🔹
انجمن خودروسازان آمریکا می‌گوید که متوسط قیمت بنزین در این کشور به بالاترین رقم در ۲ ماه گذشته رسیده است.
🔹
تنش‌هایی که آمریکا در تنگهٔ هرمز ایجاد کرده، قیمت نفت را هم دیروز تا ۸۰ دلار در هر بشکه بالا برد و تردد کشتی‌ها در هرمز را باز هم متوقف کرد.
🔹
حالا درحالی‌که ذخایر راهبردی نفت آمریکا هم هر هفته رکورد کاهشی جدیدی می‌زند، قیمت هر گالن بنزین در آمریکا ۳.۸۵ دلار شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/448756" target="_blank">📅 18:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448755">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205fd5823d.mp4?token=FzWFsr7goQrBtKGvdDLhBPbCMDUKKNfaY_RgpkH36QvQnwPjQZvo4yEYdQrFBivHKLOVX8qvLuTFw82vpAtfgrI439Q8xZLeniGOTlr7EP1VC14aj6jQmwuu6t7w86bTJXzsIzBl2uQaur3St8SMxWHH0-1k44Du2IqPLqQn9BMtLo0N4A0F4bJ0tpFUhs2u-Bj_5Y7XF_8pUEGRnHBEXotJ7CPpRpzxqqbVt2hY2T74tFBxwwY_Pev-kQyp3m5YEXiHEn1aCEvZpKJO_ok31FVZEL6jmKqJ8AHM4LPIeAxUlQKuk1f3HVxrNYeem1ayi489aSxz5f7cV5JZoN_oNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205fd5823d.mp4?token=FzWFsr7goQrBtKGvdDLhBPbCMDUKKNfaY_RgpkH36QvQnwPjQZvo4yEYdQrFBivHKLOVX8qvLuTFw82vpAtfgrI439Q8xZLeniGOTlr7EP1VC14aj6jQmwuu6t7w86bTJXzsIzBl2uQaur3St8SMxWHH0-1k44Du2IqPLqQn9BMtLo0N4A0F4bJ0tpFUhs2u-Bj_5Y7XF_8pUEGRnHBEXotJ7CPpRpzxqqbVt2hY2T74tFBxwwY_Pev-kQyp3m5YEXiHEn1aCEvZpKJO_ok31FVZEL6jmKqJ8AHM4LPIeAxUlQKuk1f3HVxrNYeem1ayi489aSxz5f7cV5JZoN_oNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور جلیلی در مراسم تشییع رهبر شهید در مشهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/448755" target="_blank">📅 18:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448754">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1322afad.mp4?token=D9b2rE0IWZHfD2K11hUPg9laXbiCiL7myZDs3MCoARwK8A5tMYcNpHmvj-ZoWMbvJnys3_msjWle2D3BobMUBM8hLHCqdWk6kJCg4RZxtGty17DEX3WKgvN8iondDP1NfFLWkNHv01vSrbped46q8fjdmrVcotf-ib8l4-Icx-EBdU99yxvOB7yBolNjsfthSUYJs8ehoV5qhGJdeLFCuXoDk7rLncZOLt-rFaokSne4AUSFo0CJWaDVO8Ebffkx1MegO1d_IYnybSt3J8vOKJI1n7lB59iHZ-3Om7Q2G6kaU8c5-W-qFeknpde76qYuTkAUFtZ7DgSD9T154FoIpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1322afad.mp4?token=D9b2rE0IWZHfD2K11hUPg9laXbiCiL7myZDs3MCoARwK8A5tMYcNpHmvj-ZoWMbvJnys3_msjWle2D3BobMUBM8hLHCqdWk6kJCg4RZxtGty17DEX3WKgvN8iondDP1NfFLWkNHv01vSrbped46q8fjdmrVcotf-ib8l4-Icx-EBdU99yxvOB7yBolNjsfthSUYJs8ehoV5qhGJdeLFCuXoDk7rLncZOLt-rFaokSne4AUSFo0CJWaDVO8Ebffkx1MegO1d_IYnybSt3J8vOKJI1n7lB59iHZ-3Om7Q2G6kaU8c5-W-qFeknpde76qYuTkAUFtZ7DgSD9T154FoIpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگو با مردم عراق در تشییع پیکر رهبر شهید در شهر نجف
🔹
امروز قسمت کوچکی از جبران ما برای جمهوری اسلامی است.
🔹
مردم عراق، شیعیان عراق و شیعیان تمام دنیا از سید علی خامنه‌ای ممنون هستند.
@Farspolitics</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/448754" target="_blank">📅 18:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448752">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bm3T4Znmq9nszcXWT-vagjttB_pVzpAW_qOche-ghQopgvC73Yk3D0g5rlzyVpcZd1quM3FRA5QiAYPbU2sm26hYc9IpxyyZZ37YSXY03myJHjHmxuP62IkOeMcqROhvZcPFm9zk0A_V5lcr_wa8EqwcHqw63bJHjC3IAolLKyM0CAcf4tfqF2C0cQOcgYykEn2_lLNuNLexLy1VJ55P4FDU0JvtQF0i4699h3WHvlsuaPjyaZjvc2YrI7oM0L0YIxwHlgzLgwVYfqzD5GljqqDD8JH4xUYuGzKvAUnNZJeqVjpO4SY8vHtCNV9QwDta1l9zsoW671i0UZChjM0NmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب برای آقای شهیدمان نماز لیلةالدفن بخوانیم
🔹
روش خواندن نماز لیلة‌الدفن به این صورت است که در رکعت اول سوره حمد و آية‌الکرسی و در رکعت دوم سوره حمد و ده مرتبه سوره قدر می‌خواند و بعد از نماز می‌گويد:
🔹
«اَللّهُمَّ صَلِّ عَلی مُحَمَّدٍ وَ آلِ مُحَمَّدٍ وَ ابْعَثْ ثَوابَها إلی قَبرِ فُلانِ بنِ فُلانْ»
🔸
(به‌جای «فلان بن فلان» اسم هر شهید و پدر ایشان گفته شود)
اسامی شهدا به همراه نام پدر:
◾️
حضرت آیت‌الله العظمی شهید سید علی حسینی خامنه‌ای، نام پدر: سید جواد
◾️
شهید مصباح الهدی باقری کنی، نام پدر: محمدباقر
◾️
شهید زهرا حداد عادل، نام پدر: غلامعلی
◾️
شهید سیده بشری حسینی خامنه‌ای، نام پدر: سید علی
◾️
شهید زهرا محمدی گلپایگانی، نام پدر: محمدجواد
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/448752" target="_blank">📅 18:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448751">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95b70af5b3.mp4?token=cvE-Zbi2wdRcji22wiGmlEKEPXGW5cANYWECrFnIxOg7iQ7JQHdQ_zeBw1DB4Q0LyvDUwQjvzugztU14sHJyB__8FVRQiLaDqeuS-PYzORpAcMVe1u7EowpooPUOUyx9sFE1TCVAZa43xRD8wXAMitDaGS8M1tRSI7Vam2nezthapXTK8fpc-M1p_9tWmOBv9PDnSArY55yhqi1DmPFu7HGrqsk298gtD9hgK0fSwEtMAPzFBAR3BjSuhUxdxJ4ZesfIoD0h2923pgS3ssvufZ9cFukulEPADl81B5g-2BYwV36yHfU_F4CiixprPSddaFTxZjdBvI8vV9wL96_IdVo3eVjp6SCGfLb0jTRB_yqJ2aczZ6ksCv1zvHeG1tZL9amXELzCVZ_m8PW8V8tn5qNFv7EQ2f7hRguI_iSArIDQWQe6mm1Bn-vWMNYwMcaLPIqu5SZB1NzNEia8hCrLP44tXNVGNN4OHhnzGCkJw-HsMZ_y31zrlJ-tDXCctN9Ddi0z8lVeNogEX_emJ5M-SBhhHvy-sapIrvuZTweiC3EedPou4_uuX5OqdxtDze9SgAS-MGwO-NXHUOC6ZjYxxORZOnRpqACHpyKg5GiTZAyyLHUJTxIomYAwg9ypK5yCel-FIj8wSJO9gZsHpvY5xv9wPaaVm-cr2YKQCN_wEA4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95b70af5b3.mp4?token=cvE-Zbi2wdRcji22wiGmlEKEPXGW5cANYWECrFnIxOg7iQ7JQHdQ_zeBw1DB4Q0LyvDUwQjvzugztU14sHJyB__8FVRQiLaDqeuS-PYzORpAcMVe1u7EowpooPUOUyx9sFE1TCVAZa43xRD8wXAMitDaGS8M1tRSI7Vam2nezthapXTK8fpc-M1p_9tWmOBv9PDnSArY55yhqi1DmPFu7HGrqsk298gtD9hgK0fSwEtMAPzFBAR3BjSuhUxdxJ4ZesfIoD0h2923pgS3ssvufZ9cFukulEPADl81B5g-2BYwV36yHfU_F4CiixprPSddaFTxZjdBvI8vV9wL96_IdVo3eVjp6SCGfLb0jTRB_yqJ2aczZ6ksCv1zvHeG1tZL9amXELzCVZ_m8PW8V8tn5qNFv7EQ2f7hRguI_iSArIDQWQe6mm1Bn-vWMNYwMcaLPIqu5SZB1NzNEia8hCrLP44tXNVGNN4OHhnzGCkJw-HsMZ_y31zrlJ-tDXCctN9Ddi0z8lVeNogEX_emJ5M-SBhhHvy-sapIrvuZTweiC3EedPou4_uuX5OqdxtDze9SgAS-MGwO-NXHUOC6ZjYxxORZOnRpqACHpyKg5GiTZAyyLHUJTxIomYAwg9ypK5yCel-FIj8wSJO9gZsHpvY5xv9wPaaVm-cr2YKQCN_wEA4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب متفاوت هوایی از تشییع پیکر مطهر رهبر شهید انقلاب در مشهد مقدس.
@Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/448751" target="_blank">📅 18:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448750">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🎥
پیامی که از دل این جمعیت به کاخ سفید می‌رسد
@Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/448750" target="_blank">📅 18:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448749">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید انقلاب اسلامی در سیل جمعیت عزاداران درحال حرکت به سمت حرم مطهر رضوی است  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/448749" target="_blank">📅 18:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448748">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9dc2333dd.mp4?token=OUG2g_Oar_iR89i38knXWr8g_osvAUhro6_QyFMgIeNDrvnp3eX0w9yKjfJjOutOi7jNO35u5bijh-0_3p6v-j1Vf97gYsNYdH841HJcaMxHjaMfIMp-TL3QLcvYFG-vAtaG7Ojy_OV4HmA9QbaGoCx9J6XN0Eq8BbSpZTDKst_3pM57CGeem-jtGJc6oX_ilrdekVBZwNuNkaGWHbdG_qo_XokfP29HY2IS8CJV4Ov46IZSlTVXLieOC20Z8gUQW0UDD2x5xBX89Z23DGlK2RJVFpZOZ3187WJMXipD33f5mOBAbsN-jZAgVyOXN9JkRlU_BBJJtpCBbUaiMS_FIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9dc2333dd.mp4?token=OUG2g_Oar_iR89i38knXWr8g_osvAUhro6_QyFMgIeNDrvnp3eX0w9yKjfJjOutOi7jNO35u5bijh-0_3p6v-j1Vf97gYsNYdH841HJcaMxHjaMfIMp-TL3QLcvYFG-vAtaG7Ojy_OV4HmA9QbaGoCx9J6XN0Eq8BbSpZTDKst_3pM57CGeem-jtGJc6oX_ilrdekVBZwNuNkaGWHbdG_qo_XokfP29HY2IS8CJV4Ov46IZSlTVXLieOC20Z8gUQW0UDD2x5xBX89Z23DGlK2RJVFpZOZ3187WJMXipD33f5mOBAbsN-jZAgVyOXN9JkRlU_BBJJtpCBbUaiMS_FIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این‌پرچم‌ زمین نمی‌مونه
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/448748" target="_blank">📅 18:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448747">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bccb2ff9c4.mp4?token=O5BPvxGb_WZMxK67oJHGa9-5EhTdy_x6FV6flpDkLJvSi0lE_tB7_1DbcShPXU9zqalJdgyYWdwqyFRXdsGTUIi-9HFnAgTgk1xiF0F-FU4apu0w_BMFhmFgyX_GXWsP01VXRLyA0RT_PFQlmRjNWhNAMjAw_5S5y-gXterySSqVlFibTFwKzgtrJUhm02iHJOIYAiGTRaBViG6ApihwnCN2okK73qFLNBbY0vNltOULVIspe7wkMljdS75_rox_egEL2vQDmbe2uPb66RxLJVxdKV84H7O_8WwFWZXIp4h3m6fsqpZDeQp4DH7phuKgGCy2KkHqrvul8eJlv9b8Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bccb2ff9c4.mp4?token=O5BPvxGb_WZMxK67oJHGa9-5EhTdy_x6FV6flpDkLJvSi0lE_tB7_1DbcShPXU9zqalJdgyYWdwqyFRXdsGTUIi-9HFnAgTgk1xiF0F-FU4apu0w_BMFhmFgyX_GXWsP01VXRLyA0RT_PFQlmRjNWhNAMjAw_5S5y-gXterySSqVlFibTFwKzgtrJUhm02iHJOIYAiGTRaBViG6ApihwnCN2okK73qFLNBbY0vNltOULVIspe7wkMljdS75_rox_egEL2vQDmbe2uPb66RxLJVxdKV84H7O_8WwFWZXIp4h3m6fsqpZDeQp4DH7phuKgGCy2KkHqrvul8eJlv9b8Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید انقلاب اسلامی در سیل جمعیت عزاداران درحال حرکت به سمت حرم مطهر رضوی است
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/448747" target="_blank">📅 18:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448745">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f803a62c9c.mp4?token=GZct1cN1xUCZAMJWI948rH9B8q5BoAdJL-fUtFJNpR0CSjmiu_bjtHHfGYBhbnyqtBBCefENiNpCmr-bdkx-YwmGfBRjOQkVNqATf_8d_l4OruVT908R2GJoglk4-XOTMBh4wKtcvitQ4lHl8MX1yUgTSWxSTbqjiZq9Gcu0cyMi6iZjp-j1rTRtV9Ap9uPjeS6w-CA9xckCEcPZI-CHagg09ZvuzMCWXPlWlbhsEOv5j3V66zThrHk7XQq9AaeDBcTRoxzkDl2W5UrfE4Ebeug1y-MQR6iGZk1sUiaGyioERPImFiy39J005frjqGmgZ-1ooO3Z-kwY0O2_HkcP1ga8vqUQuDzcZnhyljYgb5F6Io_h_afAFK8uVpGo5ivcrLqUy6LmqhIET3tQwt4ezuBY0gNXDGCWmVeIhKVpdE1n2h0VldAloY_kbNDfU5i-Vsu2cH1Euc11SuG4Jvr7wR5t--V1adL7O7RhPw3MtQp_BUpn_2PxvRDqJi8v8_1FtCD9LPo2g04AN9z5YW63efFy-q75zV7ZGf6br9d3wtWoRq8XVXEWsvOnEC56cfQerjbe9_q31I6j6sC4P1tauFim8t5L-BwVJSqhhuj6Of8KGMHiB86ZQ30pcQiRex8V9vFFQxUmWML1qbrIGJBIVkIgHdZCYf788wsD0zCtkS8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f803a62c9c.mp4?token=GZct1cN1xUCZAMJWI948rH9B8q5BoAdJL-fUtFJNpR0CSjmiu_bjtHHfGYBhbnyqtBBCefENiNpCmr-bdkx-YwmGfBRjOQkVNqATf_8d_l4OruVT908R2GJoglk4-XOTMBh4wKtcvitQ4lHl8MX1yUgTSWxSTbqjiZq9Gcu0cyMi6iZjp-j1rTRtV9Ap9uPjeS6w-CA9xckCEcPZI-CHagg09ZvuzMCWXPlWlbhsEOv5j3V66zThrHk7XQq9AaeDBcTRoxzkDl2W5UrfE4Ebeug1y-MQR6iGZk1sUiaGyioERPImFiy39J005frjqGmgZ-1ooO3Z-kwY0O2_HkcP1ga8vqUQuDzcZnhyljYgb5F6Io_h_afAFK8uVpGo5ivcrLqUy6LmqhIET3tQwt4ezuBY0gNXDGCWmVeIhKVpdE1n2h0VldAloY_kbNDfU5i-Vsu2cH1Euc11SuG4Jvr7wR5t--V1adL7O7RhPw3MtQp_BUpn_2PxvRDqJi8v8_1FtCD9LPo2g04AN9z5YW63efFy-q75zV7ZGf6br9d3wtWoRq8XVXEWsvOnEC56cfQerjbe9_q31I6j6sC4P1tauFim8t5L-BwVJSqhhuj6Of8KGMHiB86ZQ30pcQiRex8V9vFFQxUmWML1qbrIGJBIVkIgHdZCYf788wsD0zCtkS8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حالا حال حلما را درک می‌کنیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/448745" target="_blank">📅 18:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448744">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af6c4a87bd.mp4?token=ndM9wC7SKgdthyOKupIVKyvzT9rF0LwGIOwUzG5SANU9UxWRMa0tigReqVmDR33sEib2eUAE94XukspCRZLmF3WtW2BX9r4QeuZDQnfZomzEMrYfFfGX2M7yRr5JTV2FyLVUyFxCJ3jtSKfexbQ-JmUQ4_N9umoANEfHTwDBId4bvcR1uVWebgu4va7PekfVxUzWC2yPH73yPhMV449--Y9x8XGjI5r8w-uEjM8r29q-dBvU7LupBi-cMEcoY-rPcDm78UfWxoUq16Ir9vfHeyLj_dWk_clG4RdEBWvSRdix3Eo8CtKO6cCudBXQwawpQ-DDXuMbSLD7Q_eOuZUFFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af6c4a87bd.mp4?token=ndM9wC7SKgdthyOKupIVKyvzT9rF0LwGIOwUzG5SANU9UxWRMa0tigReqVmDR33sEib2eUAE94XukspCRZLmF3WtW2BX9r4QeuZDQnfZomzEMrYfFfGX2M7yRr5JTV2FyLVUyFxCJ3jtSKfexbQ-JmUQ4_N9umoANEfHTwDBId4bvcR1uVWebgu4va7PekfVxUzWC2yPH73yPhMV449--Y9x8XGjI5r8w-uEjM8r29q-dBvU7LupBi-cMEcoY-rPcDm78UfWxoUq16Ir9vfHeyLj_dWk_clG4RdEBWvSRdix3Eo8CtKO6cCudBXQwawpQ-DDXuMbSLD7Q_eOuZUFFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خون‌خواهی رهبر باید این‌شکلی باشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/448744" target="_blank">📅 18:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448743">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0756d602ce.mp4?token=XQ3M8Ms9vRX2ghMrtXnOFnJ_EguUTue7_4PuZQ6Q1kasjFYqyNPYbMCZwiOHciDLCzrqiFXqWKneMOwOSoz2EtFi4pl7arcz91-29yBKwdlnwRoJLhHRVS9nUS5iP8iAunywidJL_D_8vm1G_vAUr5jb7U5Q_xCAGWUbBIP6v9JjPWyRlUrSgk7b-pmQ4uWOC4RacVqwJdF5yrShI9mYTE15oHz8a1CzFVQL-3AuR-UXy3mFsEWAtTggZBFseA5_CQqDdjjAkFY6EtL8Kf4OLxnVqz-iinpm2NeUV_vfVYrHtaBMg1oW7XyT7SbcNY605W30z1LcgQwBxZEUarFAkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0756d602ce.mp4?token=XQ3M8Ms9vRX2ghMrtXnOFnJ_EguUTue7_4PuZQ6Q1kasjFYqyNPYbMCZwiOHciDLCzrqiFXqWKneMOwOSoz2EtFi4pl7arcz91-29yBKwdlnwRoJLhHRVS9nUS5iP8iAunywidJL_D_8vm1G_vAUr5jb7U5Q_xCAGWUbBIP6v9JjPWyRlUrSgk7b-pmQ4uWOC4RacVqwJdF5yrShI9mYTE15oHz8a1CzFVQL-3AuR-UXy3mFsEWAtTggZBFseA5_CQqDdjjAkFY6EtL8Kf4OLxnVqz-iinpm2NeUV_vfVYrHtaBMg1oW7XyT7SbcNY605W30z1LcgQwBxZEUarFAkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریایی خروشان، به رنگ انتقام
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/448743" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448742">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ab73420a.mp4?token=k4-plwqq2cWTePPCIYkmTwaJzdSccIiCBPrSMCEa6F1lmcElZYv9Y-FwCQzwrp0m5GZNteiil3O0ClZ2IcyKFpWbjivJqVtc8c49ONarVO9MblZaP_sJON6i3F2e2nNTV0JrdqWy5qrz_KcieSaN_2jPaUhzHSVWU9oWKpL1x4g62kl-p9Vi3Nv5iEbtrSLa_qK2FHjo-KKv6WZFMDa8lTYEoXh2NJGVxAzLe2YiDFihUvr3MsoJTVbyM7zHkYT9K_jwNyMavKk5g6n96keIzYZWakOHr_mragXkFL8lFBZaRpRmK3eAMZ3zTdEGHUlvJ9wqmWX2uAh0Q7A48gKM7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ab73420a.mp4?token=k4-plwqq2cWTePPCIYkmTwaJzdSccIiCBPrSMCEa6F1lmcElZYv9Y-FwCQzwrp0m5GZNteiil3O0ClZ2IcyKFpWbjivJqVtc8c49ONarVO9MblZaP_sJON6i3F2e2nNTV0JrdqWy5qrz_KcieSaN_2jPaUhzHSVWU9oWKpL1x4g62kl-p9Vi3Nv5iEbtrSLa_qK2FHjo-KKv6WZFMDa8lTYEoXh2NJGVxAzLe2YiDFihUvr3MsoJTVbyM7zHkYT9K_jwNyMavKk5g6n96keIzYZWakOHr_mragXkFL8lFBZaRpRmK3eAMZ3zTdEGHUlvJ9wqmWX2uAh0Q7A48gKM7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وعده دختر دهه هشتادی به «آقای شهید ایران»
#حاشیه‌های_بدرقه_در_تهران
@Farspolitics
_
link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/448742" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448741">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c53b5ed1ea.mp4?token=V8H9eQ8zjZI87ivo6cN57813d8USoshAI3FKcX9c1ccrYLZaEv1TN_nKpMGaJ94fkdG2ZVs7cgpcvRGqOXifo5sfsdSQfsqS_qo3VrxrSCcIWJfsDnvEgcsR-t3X60C4JYW28G7SZJ3KffdLQDa3BaqapUADBcElubdI_wOWsnvDp1bV4v07Wd0Ui0gmlPZSbZS8uxJ2S-y8kaC6aPk024W_sj-ViCPSt-42Q9CbotZi4OoVikeDVc8JqwxUVeLPO8Bl9uAXyO7OyYh4J4EBMGBblFwosw23QLlTUE2cOuWGqYz_V47cuy08ctrsjWEl3htH1mS-llSPWUPAj8NmzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c53b5ed1ea.mp4?token=V8H9eQ8zjZI87ivo6cN57813d8USoshAI3FKcX9c1ccrYLZaEv1TN_nKpMGaJ94fkdG2ZVs7cgpcvRGqOXifo5sfsdSQfsqS_qo3VrxrSCcIWJfsDnvEgcsR-t3X60C4JYW28G7SZJ3KffdLQDa3BaqapUADBcElubdI_wOWsnvDp1bV4v07Wd0Ui0gmlPZSbZS8uxJ2S-y8kaC6aPk024W_sj-ViCPSt-42Q9CbotZi4OoVikeDVc8JqwxUVeLPO8Bl9uAXyO7OyYh4J4EBMGBblFwosw23QLlTUE2cOuWGqYz_V47cuy08ctrsjWEl3htH1mS-llSPWUPAj8NmzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماهنگ در آغوش ابدی خورشید
🔸
برخی تصاویر رهبر شهید در این نماهنگ برای اولین‌بار منتشر شده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/448741" target="_blank">📅 17:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448740">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/792f81a5b6.mp4?token=nN7bvW6WiD0zo_uNS2K_AgMkQWd22lWf-nkRaKorOy48aYhk8vHbszVp0o9tSpXZkF8N2Z76dYpaYt3Djh8cU6YlwdRFdfKCUFI7J85tYUGULAp_B534CZjrPXCczSIjHgp7b4Fiwwxw9s4JgWdFEzg7VbSDMfWj01__i4kjKCuetJEVMxLmOMXcT4MUwmnpfogrz2f214PpLBD3t1bBLNfhKhM4Y7D_RWFi8ywvd33p8BV2nKRMtERjr6D_ka6MhS4Iym7ilexLZ49CdDXyKRA_HJq3TYnzQShAOCt9LfKuKtMhg9ZJJC7d_6rvogd0ce0Ur_qlFYJw6Ou4ivpKRwII6HCWHvmhhR2dE95sDH2K3eHrKO2MQ8hvM6xNZdD1LQTb89z28q5AQ9p0uGkNdeW6zD4z82RIqnufXk6yDUTjsXpoZ9BpA7DtQF_gSwoXo6RH2_koFReJTIZl23Fg_GwlDnQhyS-0jMLVXB2-7N5TdfwPWnqqOYUHwE995LaCfNtwzaYO5GCPHBXlI_oVzhjoY-gz6wB3seeCcqQDUL53-E3ykZH0qlGu6PuTlL8LPsLdELrkPaNofu-wSnfVkfpNXJ5fiIbpUoob3BVPZ-DpjZLG91oEji3hfblIXJ9NgHtZVDqxPe8ypCHAW1ivjJgjJ6R4WtdsHMDGiFhKVso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/792f81a5b6.mp4?token=nN7bvW6WiD0zo_uNS2K_AgMkQWd22lWf-nkRaKorOy48aYhk8vHbszVp0o9tSpXZkF8N2Z76dYpaYt3Djh8cU6YlwdRFdfKCUFI7J85tYUGULAp_B534CZjrPXCczSIjHgp7b4Fiwwxw9s4JgWdFEzg7VbSDMfWj01__i4kjKCuetJEVMxLmOMXcT4MUwmnpfogrz2f214PpLBD3t1bBLNfhKhM4Y7D_RWFi8ywvd33p8BV2nKRMtERjr6D_ka6MhS4Iym7ilexLZ49CdDXyKRA_HJq3TYnzQShAOCt9LfKuKtMhg9ZJJC7d_6rvogd0ce0Ur_qlFYJw6Ou4ivpKRwII6HCWHvmhhR2dE95sDH2K3eHrKO2MQ8hvM6xNZdD1LQTb89z28q5AQ9p0uGkNdeW6zD4z82RIqnufXk6yDUTjsXpoZ9BpA7DtQF_gSwoXo6RH2_koFReJTIZl23Fg_GwlDnQhyS-0jMLVXB2-7N5TdfwPWnqqOYUHwE995LaCfNtwzaYO5GCPHBXlI_oVzhjoY-gz6wB3seeCcqQDUL53-E3ykZH0qlGu6PuTlL8LPsLdELrkPaNofu-wSnfVkfpNXJ5fiIbpUoob3BVPZ-DpjZLG91oEji3hfblIXJ9NgHtZVDqxPe8ypCHAW1ivjJgjJ6R4WtdsHMDGiFhKVso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک ملت، یک داغ و آخرین وداع
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/448740" target="_blank">📅 17:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448739">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dca6861c19.mp4?token=vLdpNd1SKqXnC7R0Mu_iakp6kmoM1i7NlyiIdVGB0746S0LYWVsA9MDvsIB969RaL02TkePw_okrR-pWM8hg1OUxAFpJ5RJ4ya2pfU5q43URauWu_cIQZ70Z3EOVCEQg_aG7FXzvkTZW-kIoRg2P4LOYcWawNsHbDRt-OnRavoyrSUgeTAfri_oumb5PeJFKMkdxfNpih66caRc7tI5jG8hgkHT3Th9Tutt5sIIUB3YGSpvSAIx8KMsnJjUhJcOSg8d5zJACexpWbHWqxDgNBsX_ZfEOZOKudPJYuvogpDAQkGWcAaukrYwnJD8BOG9UrFKTPqVjehbJCJEJSLxHBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dca6861c19.mp4?token=vLdpNd1SKqXnC7R0Mu_iakp6kmoM1i7NlyiIdVGB0746S0LYWVsA9MDvsIB969RaL02TkePw_okrR-pWM8hg1OUxAFpJ5RJ4ya2pfU5q43URauWu_cIQZ70Z3EOVCEQg_aG7FXzvkTZW-kIoRg2P4LOYcWawNsHbDRt-OnRavoyrSUgeTAfri_oumb5PeJFKMkdxfNpih66caRc7tI5jG8hgkHT3Th9Tutt5sIIUB3YGSpvSAIx8KMsnJjUhJcOSg8d5zJACexpWbHWqxDgNBsX_ZfEOZOKudPJYuvogpDAQkGWcAaukrYwnJD8BOG9UrFKTPqVjehbJCJEJSLxHBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برافراشته شدن پرچم‌های انتقام در تشییع امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/448739" target="_blank">📅 17:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448738">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61f80416c9.mp4?token=olrhyRu_jopi5-5-rTTSiNvtap8uQ4VqSPy4hEWLN99mqmeY6uSDPvQwvUD3n5BT4-88rOS6pHhwUvNTwcpXDTY7jLcmdBuLTqFKZR6lQYjaXQunvbo80I55WyHFQ4CeGujeUAXWzphPi7Qgja5a5Npe5RvyKkD45Z_nxSEDnRuvgMa6uo1Erdgej9S6GbhgtTLQVTO3v4uatczZELjoHY3WADS1bIdbT30UMGf3DjaroOjO595sSLLW_R1mo9ublTl_GsVSQngOHfmVM8xJiGxZBDAzYqlNlAW4fmamGi3QHflJhji7MzZ2xCDl6jZ2_gc5zOY-HkrO3RD3WZGDjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61f80416c9.mp4?token=olrhyRu_jopi5-5-rTTSiNvtap8uQ4VqSPy4hEWLN99mqmeY6uSDPvQwvUD3n5BT4-88rOS6pHhwUvNTwcpXDTY7jLcmdBuLTqFKZR6lQYjaXQunvbo80I55WyHFQ4CeGujeUAXWzphPi7Qgja5a5Npe5RvyKkD45Z_nxSEDnRuvgMa6uo1Erdgej9S6GbhgtTLQVTO3v4uatczZELjoHY3WADS1bIdbT30UMGf3DjaroOjO595sSLLW_R1mo9ublTl_GsVSQngOHfmVM8xJiGxZBDAzYqlNlAW4fmamGi3QHflJhji7MzZ2xCDl6jZ2_gc5zOY-HkrO3RD3WZGDjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از سیل جمعیت مردم مشهد در بدرقهٔ آقای شهید
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/448738" target="_blank">📅 17:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448731">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XALCM6-K8nVpjLlICQ0pMByq6YOM-C8dZxpDvUvdJSmGaqDUgew47ljkkn1bn1wTnBjzYBK-AnuhbX011kxDcTtGr_9APaW6qarlpIAAd6HOFeLH3ZJE1SPmumWk45B6S1KCSxBpnGlr-BHej33fKDQzPl7C-qQqJXgmJJmC2dKpcUHfuA9XZL147yyADGxQSWohbRBGQdsOaE6jLGkzC8a9RAZchFCt9p28w0erDTZ3EhXvEsmp4elY6zHNl-nLkaCzij-1bNrLUvLkf55orQju8y-8a88nC0UZyFvHqjs7jsSPm4jBi9l2EVKRWUUeHU2TDkx9LZpOIKSRCp3zDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbnJ-8ICq9ami7vAndpDudAuk3sXaOaeD7qtB8lte38lgH8IqCVKmVLvuUVTOzZyg8n8hS-YvPo5QlW39uKhME0Q4d8RXElMBEQPnreJESQ-FYk2olIhDdppDQQexoZ9MPDdxmVAC5uJZhScdL2BoEWGRc_EaZGg3VLzpiVHWuPOuhM_5RN41EbsWOJq95RVspK4fdrjECYOdAwMRL6EiPX8jRm4to6t6Ji066OXYocaw6V5vFD4_82slPzvfyhNBifEPj9Y53ubtv2SbGEK_CqpK4R87_ojrrblNn0RfOlczS3y9y6uD-ipdGmODTiK24NxcpHrPIky4Px3MdTmYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TAPnRvinTI18_8DaWplvY2qnD5EBuBDPzYUpK4Pak9oHVOvoiSx-oGan14O_BK-OPFpeIELnQ9tIZl6okxjbhTqht28HyyLcoIKGTJ_SdAu01RZmEk2nXvcQLfDJEnqEwJ61YL2_sc9jnrOt2kXSD_IKNSfKc6bu-rsqyxHMZ4piyM3n9yt-QvNILy8YFQNRivh_TjXfYm-7oYT7SI84R1FOjklXTdscp6J2uQ-uHlp16GYDc2GFbElJACyLEKb6wOyp9C4EMD4mjiyhar7XKaPLFUL-tulcQ7s2611lmWD8NyB3_AlmQEHOM0p5PGe_EsdtGgLKAU5MVyvNm20vfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pM-yng1BHxw93VLtbGP0lZU9reqdJp_49bjl5gE8QnA5ncVJPAS3ptt8cfPMFcJLXj8AR_y9w4CWbFjzjT4nYeXHCWhSLii2KU0Ur6aQ0-wEn7Cxn5GDygtkavz2lPWhdrBp3myHgff6FfG26KY3MG5b5E7_4x6uMrzB3QJFpmAkXn6_-BTe-CP6JwqPJUR2gIc_vLILRHGokAhu4aBiRvnk6O2x07KLER_-ydio9do4H3XUYGs4JBQlVSMjMPz6BeDrzkDMUhsdbtBmeYtfpQq557K5m2wFqAPt1X4cbUxaKN9AnVlS1BJ7Ord9XXW_8lJI7ZH5kysp6ugdkz_jiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nbNs7NzSK2_1xO6b_Dd3f_tQi_aVRI5UB54ERBtKAVYZKaZ-CshaNaIKNi53dmaHF70g-UxxC--C8AeenPfa0bsFqZCyxzTyqv9tydPxNvAeTuX2XV14I8hRcEamEDvb6DORBACExcJg81nTReNFnYRkulEN3lqjW99UiOHdNVrCoFCMvNhinznfrScEN8J9XKabs7lGIU7g-ppXtdJFSXJ91WOrKsyyRqEgZDn57JXAshejpvlyC7-jKbCXNrGGT0_egz6x6domVxZ_baDrrkJ-XHgzuIV8vH-BfrjF6U1JwjBRD0aZXgxG0NzhR2_qNBJQ3yXvJLIgoZGzJkJPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VB6GMfthSCWnYnYegJft1Nt1Ckv7rOfZtoD8a0OKAiN_Du6lWL8RUXGKbgpnFXfqsm51-QNwyXJBciZboswgJrF-VK2XX_8eM7_ZITsA7YCksWl8FAFnUPK_lojrRqJT710lsIpVHQyoVOZ76yZVdfUIEl9PLOlCPsqjVKNkQQVUU5bBZC61k6VOQOLIapPAUmYdi1LVId0JW5OAidgsvy_R1HgYnIEtnAeOKG6DcYw5NVvH5s9ubQORdMI6BNu4poK7je6eXIvxyO998AqwRnL5z9b_KIC40HDD0pQuh569mtizTueC-VMqCst7tz2NjXi2VG4ZTnyUWk0tb34YfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ej5nn33btIiaWw7pzfOjil1UwC8JYfjlPufyEd5JUlnMXymR6ZDAhJQLJpvP4JGiRS-s4gnMCySr9y6M83mCLr35vc7amVegBAax9taPVOSzxy06QUYDvPay3atA3Kx4YJdwB8IvHivBuBdfGPECzyErpFX9-JPg-sPhIX_3YdkZw32t099eBe0C0nwCi-o0fhQQE8wu4jL4ZR3RYGctzJln8rYtBRuhyiduVpBoDcp8CvWNVeW5QB_IjD7JpNJJ0oDtpt-C_rhjRkRXvc3QfU8MbkgQU0BM1CTMgsmqZ0DsuxION0K9EOMbc7WOzyuGAo2PDOAV-AqvkTER_j5SMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پرچم ما ترامپ را خواهیم کشت در دست مردم عزادار مشهد
عکس:
حسین توحیدی فرد
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/448731" target="_blank">📅 17:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448730">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ظرفیت حرم مطهر رضوی تکمیل شد
🔹
ستاد برگزاری تشییع رهبر شهید در مشهد: ظرفیت تمامی صحن‌ها و رواق‌های حرم رضوی تکمیل شده است. از  از زائران و عزاداران درخواست می‌شود از مراجعه به محدوده‌های پرتراکم و ورودی‌های باب‌الرضا(ع) و باب‌الجواد(ع) خودداری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/448730" target="_blank">📅 17:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448729">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79d29c8884.mp4?token=Xz3owxuc9WeMKptTCtcPrQmd8segbStUUMz7Wt_vxcb3EacTkmYeijdQRdxWIO1WTIwxN1jW70QqcKv0YBwvpjKY6QSUA0T5EkuyQScAyxnCMo7NGVTc5Azq4vLqdXIJ62UAMn8LlW2yWepJyzgS8BhhGD_fw0sYlOC1bcGrQhav-gsyLq-yin8jKBHmxB-rr7weswuYoGVdtk3g6O8fEdK9KK_pplXCXFXU_WTr8l0t2FF8N5b_A6X3GQgCZFvWeerBJ-75CbGlcdyDODGgd_2f43UF9mdp2uEh4dWqg6vea1Lq32zQtDIAIuMf30gslswbPiGsLw2xWH9px4Eo4GqL2vjHZdtzM8tUIN_xmVKTrdqRKyBNO9_NpYQDFhBFjSA-D1NoTmrVEY7uDBf82R24nJRMnGlH-Gu9mkdfDQW07G0tt5OGnRW7Cfrr0GlKQfQFezWXa7kCfGzV7wVmV47rXt2cyXoYW9r5dsysDzlmabAt6Pv3hoWP1ZpCr9BZUrV-VAIpTkw8r8x7CnxsljzqEgBqmLSLg-l11tMl1YYwpWCaiQ37_FxJprQKOkRayzpWcYcbMJzOhU68pIJnPF4xp-rJCCzETnW9xyjcCJqjXsgNZcMrEG1X7aUA_pNeconiyrvVOzD9yD5N_r5hsLp1koDPLeuakAy3s969Xas" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79d29c8884.mp4?token=Xz3owxuc9WeMKptTCtcPrQmd8segbStUUMz7Wt_vxcb3EacTkmYeijdQRdxWIO1WTIwxN1jW70QqcKv0YBwvpjKY6QSUA0T5EkuyQScAyxnCMo7NGVTc5Azq4vLqdXIJ62UAMn8LlW2yWepJyzgS8BhhGD_fw0sYlOC1bcGrQhav-gsyLq-yin8jKBHmxB-rr7weswuYoGVdtk3g6O8fEdK9KK_pplXCXFXU_WTr8l0t2FF8N5b_A6X3GQgCZFvWeerBJ-75CbGlcdyDODGgd_2f43UF9mdp2uEh4dWqg6vea1Lq32zQtDIAIuMf30gslswbPiGsLw2xWH9px4Eo4GqL2vjHZdtzM8tUIN_xmVKTrdqRKyBNO9_NpYQDFhBFjSA-D1NoTmrVEY7uDBf82R24nJRMnGlH-Gu9mkdfDQW07G0tt5OGnRW7Cfrr0GlKQfQFezWXa7kCfGzV7wVmV47rXt2cyXoYW9r5dsysDzlmabAt6Pv3hoWP1ZpCr9BZUrV-VAIpTkw8r8x7CnxsljzqEgBqmLSLg-l11tMl1YYwpWCaiQ37_FxJprQKOkRayzpWcYcbMJzOhU68pIJnPF4xp-rJCCzETnW9xyjcCJqjXsgNZcMrEG1X7aUA_pNeconiyrvVOzD9yD5N_r5hsLp1koDPLeuakAy3s969Xas" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت‌هایی از میزبانی مردم عزیز مشهد از مراسم بدرقهٔ آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/448729" target="_blank">📅 17:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448728">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7a7390bb.mp4?token=UGcpyrPxMIBhDL1uqJpfORbQFUdIjD2VhvbsQVu7LW7uzBmonj0AQrCQnsrEgE0Hg_hAHoO8VqtOQQ6liomO_DE6h7g2F6EBC6Fcv0F5uW4aNQ42XbM45liUEGuqcKK87mqQ0b05Wf1CIQNhEa5lDUkUVSpwd8_67ncNqc1xf5krEYgpsuOc7vqSXCQ3UeqpK-eJQGsf9Ydn8tHRURq6X4JaBEf2bTvWBLwVbcfoMDt1IZTLm8_Vnt1lLcYUs0W-o4ZRUhApQ3TtmOrp_SUnxCuIgP0_Eq2kO8bIsIgng3fWJvDkM08wUpqFmkgKEzLlB7Tbynk7k1bkV6NWfAPBuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7a7390bb.mp4?token=UGcpyrPxMIBhDL1uqJpfORbQFUdIjD2VhvbsQVu7LW7uzBmonj0AQrCQnsrEgE0Hg_hAHoO8VqtOQQ6liomO_DE6h7g2F6EBC6Fcv0F5uW4aNQ42XbM45liUEGuqcKK87mqQ0b05Wf1CIQNhEa5lDUkUVSpwd8_67ncNqc1xf5krEYgpsuOc7vqSXCQ3UeqpK-eJQGsf9Ydn8tHRURq6X4JaBEf2bTvWBLwVbcfoMDt1IZTLm8_Vnt1lLcYUs0W-o4ZRUhApQ3TtmOrp_SUnxCuIgP0_Eq2kO8bIsIgng3fWJvDkM08wUpqFmkgKEzLlB7Tbynk7k1bkV6NWfAPBuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحن پیامبر اعظم(ص) پیش‌از رسیدن پیکر رهبر شهید مملو از جمعیت شد
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/448728" target="_blank">📅 17:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448727">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/099b8d9b4a.mp4?token=eMj3wn_2ureTNBXVbx7lJKmdGsaysXPm7a1ZLBrZ4iFOWFsawnm803IJzDqxO-FACxpNVFOs3A_OFmyit33l-WlWv_zHYVIu31xpl36q_nL3R4Sfr7uNNA2T0e6ZzxvMiciydx1CQxhBfYo5sTUkAhccrSE1bzgk4X6qbScDLgk_9d5WYEdotUbeiGzuaOxChhGb_NYtxfVlqwl-8eD-77DISs4TgHZLbOrWOR7ze71k25vF_q14FHfwyg2AuHbjo2ah5c9AWQkinWZfqNL338q2bMGTstz8f5rJ7UfwglcovJDu3EcMbfD_elrMlWbN448UkdQmJNvfoKRJiMNBqjN1kV5EDs5_yCIyb9CF-bTDZn_i9iKtoGNrSdr8x9YlQQE5rndLtegNXcdMteKTGGiluyuYmwjRp3UnM-7cSxLEYBv0MnhIiRYUK_Ca6pWqfSnwpR5KL12Du7PzOfisjQrWaOsHnIzwJcnLv2-tFZtDYS_bzQ3umhaS53zhwtgj_U3ZBD1BkRsvkXgQNyiUFR5yZo7nyBSXWw42tBLOokHZOUhdeLSp8gxCiF68aXU2SMv_Rw4RHf2KKPvt6lxvCQDCXGfSVzKQYkt5cOAvIJ5z0XAfqDxwKVPyB1cKo_Bi3N3MQ4b4nzbt_DgQmi4Gp3fLKkoLsuL_2YLTiOdwmkE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/099b8d9b4a.mp4?token=eMj3wn_2ureTNBXVbx7lJKmdGsaysXPm7a1ZLBrZ4iFOWFsawnm803IJzDqxO-FACxpNVFOs3A_OFmyit33l-WlWv_zHYVIu31xpl36q_nL3R4Sfr7uNNA2T0e6ZzxvMiciydx1CQxhBfYo5sTUkAhccrSE1bzgk4X6qbScDLgk_9d5WYEdotUbeiGzuaOxChhGb_NYtxfVlqwl-8eD-77DISs4TgHZLbOrWOR7ze71k25vF_q14FHfwyg2AuHbjo2ah5c9AWQkinWZfqNL338q2bMGTstz8f5rJ7UfwglcovJDu3EcMbfD_elrMlWbN448UkdQmJNvfoKRJiMNBqjN1kV5EDs5_yCIyb9CF-bTDZn_i9iKtoGNrSdr8x9YlQQE5rndLtegNXcdMteKTGGiluyuYmwjRp3UnM-7cSxLEYBv0MnhIiRYUK_Ca6pWqfSnwpR5KL12Du7PzOfisjQrWaOsHnIzwJcnLv2-tFZtDYS_bzQ3umhaS53zhwtgj_U3ZBD1BkRsvkXgQNyiUFR5yZo7nyBSXWw42tBLOokHZOUhdeLSp8gxCiF68aXU2SMv_Rw4RHf2KKPvt6lxvCQDCXGfSVzKQYkt5cOAvIJ5z0XAfqDxwKVPyB1cKo_Bi3N3MQ4b4nzbt_DgQmi4Gp3fLKkoLsuL_2YLTiOdwmkE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هر پرچم سرخ؛ فریاد بلند خون‌خواهی
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/448727" target="_blank">📅 17:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448726">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/606cfad7a9.mp4?token=pm9b2XfTlpqsx8cIalgr_3TyFVni8bTLZRKU0-7_oejeeJnObLmcUZ0xeesAFe5vFKI_nOS-6CkgCEVZxLaaqqjZigDSuLvtU-rkFDwJ-ajPIxKsL61XmA9va6YdA2Jp-hzpOPt3SZRDK1VBEstQvch8t-JVj8LJ4TFWISVmpa27Sfp-G5lAv-TREyg5KJeZz2Yz7rH5JpMUjUA6Zi21lluH65A14JUv5VxRbBpqcmnIEjkep8BUOIjVAU1mue7zqQuMnGyCg5zTOFCZxVTPLdC5hy0GugEh_O00IRaK3Gpor4AittmmgXzAbh9Tl2UJh6Saf5utmB0dFQzoXCk9fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/606cfad7a9.mp4?token=pm9b2XfTlpqsx8cIalgr_3TyFVni8bTLZRKU0-7_oejeeJnObLmcUZ0xeesAFe5vFKI_nOS-6CkgCEVZxLaaqqjZigDSuLvtU-rkFDwJ-ajPIxKsL61XmA9va6YdA2Jp-hzpOPt3SZRDK1VBEstQvch8t-JVj8LJ4TFWISVmpa27Sfp-G5lAv-TREyg5KJeZz2Yz7rH5JpMUjUA6Zi21lluH65A14JUv5VxRbBpqcmnIEjkep8BUOIjVAU1mue7zqQuMnGyCg5zTOFCZxVTPLdC5hy0GugEh_O00IRaK3Gpor4AittmmgXzAbh9Tl2UJh6Saf5utmB0dFQzoXCk9fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بغل واکن در آغوشت بگیر این‌ میهمان، سلطان
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/448726" target="_blank">📅 17:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448725">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fed5a5f4c.mp4?token=V4N_H67DKo5Kao49p6M9YGtjMYe6GROrWdDpZTQ1VLA3JhMfx67AEkFh0btoCAbMclLoN7fZcspw1BL-MZbS9OkQre5_4xeiDxst5x93KCzpbheGG_jUTYCuhMOwFzz85Srj8quy7y6f9xi4NPBTROzanEY9Y7FRXGMJA_tCHHED8Y9fbaRNK_oL0gp1dzfG4hBM_i9vCqHdeTFQtf03xsuGOAaJ0_Ax5hixcU-NDkn2QCxd2zeK6e7vZOVyPYWKTKbve2kg_9aURY_KQ54KOASuifpEzMZYVCCp3n_jJnW2Al9FzZb8UmTG2W6ZbrFr-75R0qWxDvGg_P3K8JJ-3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fed5a5f4c.mp4?token=V4N_H67DKo5Kao49p6M9YGtjMYe6GROrWdDpZTQ1VLA3JhMfx67AEkFh0btoCAbMclLoN7fZcspw1BL-MZbS9OkQre5_4xeiDxst5x93KCzpbheGG_jUTYCuhMOwFzz85Srj8quy7y6f9xi4NPBTROzanEY9Y7FRXGMJA_tCHHED8Y9fbaRNK_oL0gp1dzfG4hBM_i9vCqHdeTFQtf03xsuGOAaJ0_Ax5hixcU-NDkn2QCxd2zeK6e7vZOVyPYWKTKbve2kg_9aURY_KQ54KOASuifpEzMZYVCCp3n_jJnW2Al9FzZb8UmTG2W6ZbrFr-75R0qWxDvGg_P3K8JJ-3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با پرچم یالثارات برخاستیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/448725" target="_blank">📅 17:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448724">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b681ec30f.mp4?token=joHhCpgoSZQWKxSXz6zQwt9t9aVOOTMSfpFH9IQHFScqrhKu10CUsoeUzE8aDsIPCiknnwsoWJ547mv9NnwsBLc5sOM32l5Xky7oM1TkpTzK5C3tm6EnnEmBFWJfPSTqaTXld6oAuig5G6ys8J51rONktp5M_ceupETBeCfmM4sGgpERwybK9LhleWHsPUW5p2HwvktMUpkVw_lH1OrZ2vcGrQfC-41rdSZZY8MD3Dr4uc-cQsCGEoz7KpsbZjuPdIFBG7BkkaKSAcZZCP2VtH9i1Bq795OadwTNHnUra9mu6I2fyKHu84wiMXJMEP2uGJuQqSrafOv8Xy9FplPs_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b681ec30f.mp4?token=joHhCpgoSZQWKxSXz6zQwt9t9aVOOTMSfpFH9IQHFScqrhKu10CUsoeUzE8aDsIPCiknnwsoWJ547mv9NnwsBLc5sOM32l5Xky7oM1TkpTzK5C3tm6EnnEmBFWJfPSTqaTXld6oAuig5G6ys8J51rONktp5M_ceupETBeCfmM4sGgpERwybK9LhleWHsPUW5p2HwvktMUpkVw_lH1OrZ2vcGrQfC-41rdSZZY8MD3Dr4uc-cQsCGEoz7KpsbZjuPdIFBG7BkkaKSAcZZCP2VtH9i1Bq795OadwTNHnUra9mu6I2fyKHu84wiMXJMEP2uGJuQqSrafOv8Xy9FplPs_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مردم مشهد: حرف ما یک کلام؛ «انتقام، انتقام»
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/448724" target="_blank">📅 17:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448723">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14efea4cb7.mp4?token=JBtJmqN_n9sPc0hOoY1kgiJKY7UY_mwKrK97xlsgESuFy2NTc-iY8vyGv4oYg5mBJivJtAZfvq89UK7uFwcFWT2hccCpj63qyMT1wVnPPYC5C5DF3jXH9rX2_RJxJavUdUWXrj6WP2EhIc7PFjF31SP90ZDf35kiwZ8v4Rjus2RusTKWcaQbvzVNVKWc7W1lIr5lK_SpEz1pACHr8Jgkxz5cM3aVT35WMSTwG2pYNBj_8_YyLOiSgwWlbhkcVTtBy0tnqujaTdHi-2vbUWbBNW5MYzgYFsOZWZZ0dpLtnuzQL-WaW-rOhaYLK_QC9JXnrJMLm-LcfEdop9R_E_GRyW61wyKJ7dGGdGjKFc38X4rMOSB1JW8A3NANrBXBNOf-s8Y8O98Eab3qThLQIXvo2fBRypixue0ywnisfnDg0XaVdwYxOoW7FypO-9Enfm1IP580DhDsrGHYTfu-_Ye7DGf0fphhiz5ZEDTqMtD7XKbo6M9TUpZBgZ2eliGM7qPHDE9Lx1IPqlqQI0a-OZn2zmlPZgnmUQ1Ryv7WbLsjy_M9ejxpZFz9W3M2RZaJi-IA-MEHWtxatvywV9coRk5C_F9D7ZhAqk_dktfWK5t-Eubbz9-Q8-KGusELUM5w-q0ArgT7VKRD_-OM5PS6ANiwolix4O-Nuu7RZdFc8Hfg8m8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14efea4cb7.mp4?token=JBtJmqN_n9sPc0hOoY1kgiJKY7UY_mwKrK97xlsgESuFy2NTc-iY8vyGv4oYg5mBJivJtAZfvq89UK7uFwcFWT2hccCpj63qyMT1wVnPPYC5C5DF3jXH9rX2_RJxJavUdUWXrj6WP2EhIc7PFjF31SP90ZDf35kiwZ8v4Rjus2RusTKWcaQbvzVNVKWc7W1lIr5lK_SpEz1pACHr8Jgkxz5cM3aVT35WMSTwG2pYNBj_8_YyLOiSgwWlbhkcVTtBy0tnqujaTdHi-2vbUWbBNW5MYzgYFsOZWZZ0dpLtnuzQL-WaW-rOhaYLK_QC9JXnrJMLm-LcfEdop9R_E_GRyW61wyKJ7dGGdGjKFc38X4rMOSB1JW8A3NANrBXBNOf-s8Y8O98Eab3qThLQIXvo2fBRypixue0ywnisfnDg0XaVdwYxOoW7FypO-9Enfm1IP580DhDsrGHYTfu-_Ye7DGf0fphhiz5ZEDTqMtD7XKbo6M9TUpZBgZ2eliGM7qPHDE9Lx1IPqlqQI0a-OZn2zmlPZgnmUQ1Ryv7WbLsjy_M9ejxpZFz9W3M2RZaJi-IA-MEHWtxatvywV9coRk5C_F9D7ZhAqk_dktfWK5t-Eubbz9-Q8-KGusELUM5w-q0ArgT7VKRD_-OM5PS6ANiwolix4O-Nuu7RZdFc8Hfg8m8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اثر فاخر پرواز همای در رثای قائد شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/448723" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448722">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3134345d79.mp4?token=cNTJ2QwlDwhwAcDABLGXdA5KlRnvmU1Hx36ueVekGJe2mWRVyuX9ZoyOk0u3tsMFULwawcD4OeMwrsW9YUlZwuee-aWKKpePAU1yykJ1mEcH0Okh1JIDGbEB99FG3GiGaHwTRiTk2gIis2SJw5jYrgUJ6xlyaTKHAaYOMo8AhdAX9OC7evO3DNw8uBwM2ux9TIxB4v40HS-DF5e8cAVN5-5QCMNFxov2UtuMlvR16qKGty2kndFH2yGnxRQ79JFPRyt5d49UFrgX9jqxtw59NPWE2keRVKYDTRBfKXeIvsseHFFiZYu4IYYKI7T2-GuAOWVpVYTOZlpotVI7lH-cxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3134345d79.mp4?token=cNTJ2QwlDwhwAcDABLGXdA5KlRnvmU1Hx36ueVekGJe2mWRVyuX9ZoyOk0u3tsMFULwawcD4OeMwrsW9YUlZwuee-aWKKpePAU1yykJ1mEcH0Okh1JIDGbEB99FG3GiGaHwTRiTk2gIis2SJw5jYrgUJ6xlyaTKHAaYOMo8AhdAX9OC7evO3DNw8uBwM2ux9TIxB4v40HS-DF5e8cAVN5-5QCMNFxov2UtuMlvR16qKGty2kndFH2yGnxRQ79JFPRyt5d49UFrgX9jqxtw59NPWE2keRVKYDTRBfKXeIvsseHFFiZYu4IYYKI7T2-GuAOWVpVYTOZlpotVI7lH-cxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم متفاوت خون‌خواهی مردم: ترامپ را خواهیم کشت
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/448722" target="_blank">📅 16:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448721">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c874506631.mp4?token=jIbgJACqAVFy8DucqNbtpZkqbIybW62MJnG953A5P0eNE8YNy_IoBWraDnQOt3_rfCWaNvIxjD0GPD1DBOrA12uawvFbZAGNpzH31PtyOOqOXNOJdZJo05kL5Xp37PQpXkaT0_4Sn4ZbJIjCLppm38nFrht9SAtM_R3SIEtOrlh5QxaRG7aeyxkCbsUcP_HwBYhrXRe7eQyKlFQFByH_NigIdoOqVJ-sjXWbVIJB1-GQBfOJtv_w6Yh2d7tkkumORC8VN20EnjaS4175-EU6wi3Cm2pRqnyDAvnvgmFFno427rWn6gpgCp73PdzQz6pILNnSr1icojTnUN3QIKMkfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c874506631.mp4?token=jIbgJACqAVFy8DucqNbtpZkqbIybW62MJnG953A5P0eNE8YNy_IoBWraDnQOt3_rfCWaNvIxjD0GPD1DBOrA12uawvFbZAGNpzH31PtyOOqOXNOJdZJo05kL5Xp37PQpXkaT0_4Sn4ZbJIjCLppm38nFrht9SAtM_R3SIEtOrlh5QxaRG7aeyxkCbsUcP_HwBYhrXRe7eQyKlFQFByH_NigIdoOqVJ-sjXWbVIJB1-GQBfOJtv_w6Yh2d7tkkumORC8VN20EnjaS4175-EU6wi3Cm2pRqnyDAvnvgmFFno427rWn6gpgCp73PdzQz6pILNnSr1icojTnUN3QIKMkfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی تصویری از شکوه و عظمت ملت در تشییع رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/448721" target="_blank">📅 16:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448720">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55b592dae.mp4?token=LK9FHxGjRloTrNMSMfKgpXltOKw5wA-55tN5GloyBC6NtjU2bf8zfVIrLh80Z5MKPOHSQyPJMtLMsybjMkhxr54UnRgwZ14gxJC0BaPnqXaJWK8n_U_Fd8mM3hi_IYrpXC3t2PoZ4k4QJSumJ4EeW63i6RZddKYrPEATyBBnWFgRzDof9A8WajVolP0IvD4W0JA0ZMMsiyO0zn1oYxhK8U3-_zwaIU4GTBKFv20ue5l4XK18w8nwwEVyCCNNp1LquYuOpfUPzF20p8sYrJPlxoFddAAeHigUYBiWkKZoaJE3eTYnorZNEC_C_Fhzv0LVkvsCScttk73jh4X2LRwaJr6SmuMP1eTVlK3dUrkS8LK90XLcbod5Icw4I3K_JdrBxjRfepCNzAc1u2S_YdmzWpLE-tiaFIXWBh9Ra4FqElMUAgS7Jo9lMU2MzoD3rD6tXIUR5cWJI3uL_StHmSgCCcZ5HnMt8omrJgoCB0sBSh2pkXuCUMewQ2rGyWd7zMtxFwEaP8b0HxXjgt_zzg-d0Jqox0nV4tUB3wQAAvhQEpJxi-ndA-5LlaLsvk_JSxlTARzpAA25GYCPhtS4hsZS-e8FlM5t7MAsBfuBdD2t5yhfJecnQQ3_DCG_VEn6Us0Sa6G_IgwUnUFXs85OTL8Q8k652eee3jS7RFEKvri-jr4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55b592dae.mp4?token=LK9FHxGjRloTrNMSMfKgpXltOKw5wA-55tN5GloyBC6NtjU2bf8zfVIrLh80Z5MKPOHSQyPJMtLMsybjMkhxr54UnRgwZ14gxJC0BaPnqXaJWK8n_U_Fd8mM3hi_IYrpXC3t2PoZ4k4QJSumJ4EeW63i6RZddKYrPEATyBBnWFgRzDof9A8WajVolP0IvD4W0JA0ZMMsiyO0zn1oYxhK8U3-_zwaIU4GTBKFv20ue5l4XK18w8nwwEVyCCNNp1LquYuOpfUPzF20p8sYrJPlxoFddAAeHigUYBiWkKZoaJE3eTYnorZNEC_C_Fhzv0LVkvsCScttk73jh4X2LRwaJr6SmuMP1eTVlK3dUrkS8LK90XLcbod5Icw4I3K_JdrBxjRfepCNzAc1u2S_YdmzWpLE-tiaFIXWBh9Ra4FqElMUAgS7Jo9lMU2MzoD3rD6tXIUR5cWJI3uL_StHmSgCCcZ5HnMt8omrJgoCB0sBSh2pkXuCUMewQ2rGyWd7zMtxFwEaP8b0HxXjgt_zzg-d0Jqox0nV4tUB3wQAAvhQEpJxi-ndA-5LlaLsvk_JSxlTARzpAA25GYCPhtS4hsZS-e8FlM5t7MAsBfuBdD2t5yhfJecnQQ3_DCG_VEn6Us0Sa6G_IgwUnUFXs85OTL8Q8k652eee3jS7RFEKvri-jr4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
سیل عظیم جمعیت مردم عزادار و خون‌خواه در مشهد مقدس  عکس: محمدعلی حسینی @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/448720" target="_blank">📅 16:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448719">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6551db78e9.mp4?token=XU7IY3WuSey5DcwHMgQqnDjUd8xRvhgst9KEAFosTVakH6iTL_9ZibjewGU575jL1HvYwEL643s53gJ_3Yb512Cr-ctoqxao-6wybA898yuY16Qum4EMfo8S0XKXyd5qfNAUJk3kW6VfaZdgmRfn6Cn-c7SoXnDlw51aHb_FJqoaVJvM75yyt-pIoelw7oMb2gVtd6kkZIIWs1JKzvMX6rwciy8K6dYRG-9AoxfE7ACQ6iv613Di6i8gs2yd1qYB9nqe_cHv99y8dvyREKMWRWrwC7rl0cEXZI6ITrsxbjT7zJ_G1rWZYhXsIrYMg_S_r0Ttver9E7i7k1C55UAE0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6551db78e9.mp4?token=XU7IY3WuSey5DcwHMgQqnDjUd8xRvhgst9KEAFosTVakH6iTL_9ZibjewGU575jL1HvYwEL643s53gJ_3Yb512Cr-ctoqxao-6wybA898yuY16Qum4EMfo8S0XKXyd5qfNAUJk3kW6VfaZdgmRfn6Cn-c7SoXnDlw51aHb_FJqoaVJvM75yyt-pIoelw7oMb2gVtd6kkZIIWs1JKzvMX6rwciy8K6dYRG-9AoxfE7ACQ6iv613Di6i8gs2yd1qYB9nqe_cHv99y8dvyREKMWRWrwC7rl0cEXZI6ITrsxbjT7zJ_G1rWZYhXsIrYMg_S_r0Ttver9E7i7k1C55UAE0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید انقلاب در آغوش ملت عزادار ایران، وارد میدان ۱۵ خرداد مشهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/448719" target="_blank">📅 16:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448718">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025348386b.mp4?token=mRuwV_8T1tOhrBfzmGDMLBP9KLWuiSns6FfX1pesOf6vG4qbegpj3m0RR15l1zbEoOZJM_oOByI5-lTur2v1F2aSzjRWOoHL2Kl1f5WmwF9qbOiGmPzFEDMxRoTWVMV_8ZTxKaKLPJyObGZKqesvH6MB4Yh3ce2Ste9ubyu84DBQ-fNQDeNgezhcukIBSWEH6GtSNA3GQFRmC-I3GWXq4b1f9PunrouV-cspAVGLXqLa-nVx4FuzFI1S0YyRwFgk1emDzZexdI49edn4aMmIqf9jeS46DoQBX7kBIDq9m0ScXz3vV5EGJVer52EF6vgFRF6gu15v9kfC9iJYboPFxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025348386b.mp4?token=mRuwV_8T1tOhrBfzmGDMLBP9KLWuiSns6FfX1pesOf6vG4qbegpj3m0RR15l1zbEoOZJM_oOByI5-lTur2v1F2aSzjRWOoHL2Kl1f5WmwF9qbOiGmPzFEDMxRoTWVMV_8ZTxKaKLPJyObGZKqesvH6MB4Yh3ce2Ste9ubyu84DBQ-fNQDeNgezhcukIBSWEH6GtSNA3GQFRmC-I3GWXq4b1f9PunrouV-cspAVGLXqLa-nVx4FuzFI1S0YyRwFgk1emDzZexdI49edn4aMmIqf9jeS46DoQBX7kBIDq9m0ScXz3vV5EGJVer52EF6vgFRF6gu15v9kfC9iJYboPFxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب‌های انتظار و دلتنگی و حسرت
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/448718" target="_blank">📅 16:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448717">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81e61f7f3c.mp4?token=dYPTyOlk02uc5u4VksMEUfCgiUXVqVbxfQzzOPSGTAykFtsYcrNJZYbGEiJOQvcO7h5wucCMUQ4AF01jfuUlUZe9uxbIM_5256aFtXdtW3LiFXlVBf9_I2mPTk_ffie_KOrk2w08VjkowpS324eKiUOSmiD-ZtHkvcwkxzyFdO0GWJpjaK_HfYbYx8WgEO5fK6QjDooyYIlCx60nYOQ9o0TvxhE1NJhKvmBQXyftBzCRD6ELgoBKr-YF2Zz9Im-6p3kU07KiI3fkQWDkwtxCD3NBj1jePUmz0JSMl80VXlIKziaiDe5ygQFF0BZmCrauDsJDnHDrl62BzAPx4xWPiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81e61f7f3c.mp4?token=dYPTyOlk02uc5u4VksMEUfCgiUXVqVbxfQzzOPSGTAykFtsYcrNJZYbGEiJOQvcO7h5wucCMUQ4AF01jfuUlUZe9uxbIM_5256aFtXdtW3LiFXlVBf9_I2mPTk_ffie_KOrk2w08VjkowpS324eKiUOSmiD-ZtHkvcwkxzyFdO0GWJpjaK_HfYbYx8WgEO5fK6QjDooyYIlCx60nYOQ9o0TvxhE1NJhKvmBQXyftBzCRD6ELgoBKr-YF2Zz9Im-6p3kU07KiI3fkQWDkwtxCD3NBj1jePUmz0JSMl80VXlIKziaiDe5ygQFF0BZmCrauDsJDnHDrl62BzAPx4xWPiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلدادگان رهبر شهید انقلاب در نزدیکی حرم مطهر رضوی، چشم‌انتظار رسیدن پیکر امام مجاهد شهیدند
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/448717" target="_blank">📅 16:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448716">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‌
🔴
سفارت آمریکا در اردن: گزارش‌ها حاکی از آن است که چندین موشک‌، پهپاد یا راکت‌ در حریم هوایی اردن هستند.  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/448716" target="_blank">📅 16:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448715">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🎥
رهبر ما از سفر کربلا آمده
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/448715" target="_blank">📅 16:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448714">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d3a346e64.mp4?token=f122LVo99JpYbHh2WGbpnZ5Yr0Vt5qm6BW6oncDYyn-YIfEO-QZbO685Th6tCFxCnoaHuq8cDBY91skmjlvuHmYT-F5JmnF1L1LXQ2QElyEM3x0zRq-XYB0wT348sGragTgwKi5x84QfV45wwKNeCre_3CJSH3y98PmpkcQZdDmCTXSqzuiKNHpLJt1NZcPLQlWsg4_X7IMkczZvP_9NmlnWl1eyZmxg7W2B3WBpoMqAon0J8SYSzRfiqlIPi_yvQse_5gVo4b0K1y4FFcqK4yUhb_uY6M78bhPLcRfWFp2Shsy-y9MOsfmpEXYtcIHCCMa8LG6ghaxBvFrmDuiWMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d3a346e64.mp4?token=f122LVo99JpYbHh2WGbpnZ5Yr0Vt5qm6BW6oncDYyn-YIfEO-QZbO685Th6tCFxCnoaHuq8cDBY91skmjlvuHmYT-F5JmnF1L1LXQ2QElyEM3x0zRq-XYB0wT348sGragTgwKi5x84QfV45wwKNeCre_3CJSH3y98PmpkcQZdDmCTXSqzuiKNHpLJt1NZcPLQlWsg4_X7IMkczZvP_9NmlnWl1eyZmxg7W2B3WBpoMqAon0J8SYSzRfiqlIPi_yvQse_5gVo4b0K1y4FFcqK4yUhb_uY6M78bhPLcRfWFp2Shsy-y9MOsfmpEXYtcIHCCMa8LG6ghaxBvFrmDuiWMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر حملات امروز سپاه در پاسخ به تجاوز و عهدشکنی آمریکا  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/448714" target="_blank">📅 16:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448712">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmUe6UaISCvyEeqYF_h2leZKgwp7mshWxWPoNQbR2D-4L9Av6do2r-GlltniG7UJZJxZ8Yg3pyPhNLCgg-Bg5eKLILRdOMWEf_Sv0U6Wa8bc-yVNySnGQXDzR7JkAHwq69H8Fl086v_lN4eVoeI53HEgm79afhOEwjPR22fM7a0Ryv5rrfJgozQl1Nq3rbo3KzffdWFQNHvr4W-M0hwrunE-5-U-up57OdLR0IrH4X5rMsPo25GvbJVMtoN3vIQANKQGX1aLRYluiYGkPd6mx9bUOQaKSmBbd63vcDZWxDPj2vEXa1yVa5uQQHbmqggXQjtPX_aHzQwOE06kl74wKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعطای نمایندگی فروش
شرکت فنی و مهندسی شهدآوران، تولید کننده محصولات:
پودر عسل، کرک و ماسالا، پودر شربت، گلاب، عسل و فراورده های آن (عسل ارده، عسل بادام رمینی)
با افتخار 30 سال سابقه تولید
متقاضیان و علاقه مندان محترم جهت کسب اطلاعات بیشتر تماس حاصل فرمایند.
01132347085
01132347084
09116336557</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/448712" target="_blank">📅 16:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448711">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/448711" target="_blank">📅 16:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448710">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بغداد: بیش از ۱۰ میلیون نفر رهبر شهید را در عراق بدرقه کردند
🔹
کمیتهٔ عالی مسئول سازماندهی و برگزاری مراسم تشییع، امروز از مشارکت بیش از ۱۰ میلیون نفر در تشییع پیکر مطهر رهبر شهید ایران در عراق خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/448710" target="_blank">📅 16:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448708">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f14782d82.mp4?token=ZilxrFMonn8Jhty07q-jTiQkGCdjdcsZHs3rpj4iSfvRCUJD0fknqFUAREAFnR0j1aiMR8bGWHksTEDReh-97ezuLRh0rKtQyRNjVD54N0ondX1KVl_Z65ZQGHfmP8wvP_vra0YLSs3uZhishHktm7Qi5B6ikYKtSn1oy4QTKBt7lmnpcIdFvFFOqzHYEiVvLeQfOsZbW02VsLxmV-UcTLfVQzi-97udRLoDbGnVhQjdSL3C0DxyxGJgUwTEodOeveLRHTq2P9WiTcK8jQMHjJjdra2CAAJwEjqmK81lX6Lw07kYma009tupMMhNXy3JSIF4JMf1DsfDrA2csjdfBFM-A2vOOgRzRGXW8djWQ6daXQmjfclw3M2u8AbKS_DqNFpjtVhTqvvHz8S1XBQq3rl-06XLQ_X26lawmzyu90ee3yjazK-7IW4b4fzvqMfWbeDKdojRIHngnI_rQp8qvhQiuH7Km4J8IJcYCFuIhzeMG84QIQZbcePuEdZJAyY5xl9GKwcvmRWOPKEbWuL1YI1KVf3ug1xq1XGJJA1KzJxTo9sCW_mw1K_fggqH8q81KPyxuRt0b10xMkVvHhMtNFZ3Ggq4Ev295jcJhZFQ6e5dcBpSfN-KNLV92TQwU39q-zsVeiB8X8GAJKujnizQyRnhx8ZVwExy14UxDrCHn0c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f14782d82.mp4?token=ZilxrFMonn8Jhty07q-jTiQkGCdjdcsZHs3rpj4iSfvRCUJD0fknqFUAREAFnR0j1aiMR8bGWHksTEDReh-97ezuLRh0rKtQyRNjVD54N0ondX1KVl_Z65ZQGHfmP8wvP_vra0YLSs3uZhishHktm7Qi5B6ikYKtSn1oy4QTKBt7lmnpcIdFvFFOqzHYEiVvLeQfOsZbW02VsLxmV-UcTLfVQzi-97udRLoDbGnVhQjdSL3C0DxyxGJgUwTEodOeveLRHTq2P9WiTcK8jQMHjJjdra2CAAJwEjqmK81lX6Lw07kYma009tupMMhNXy3JSIF4JMf1DsfDrA2csjdfBFM-A2vOOgRzRGXW8djWQ6daXQmjfclw3M2u8AbKS_DqNFpjtVhTqvvHz8S1XBQq3rl-06XLQ_X26lawmzyu90ee3yjazK-7IW4b4fzvqMfWbeDKdojRIHngnI_rQp8qvhQiuH7Km4J8IJcYCFuIhzeMG84QIQZbcePuEdZJAyY5xl9GKwcvmRWOPKEbWuL1YI1KVf3ug1xq1XGJJA1KzJxTo9sCW_mw1K_fggqH8q81KPyxuRt0b10xMkVvHhMtNFZ3Ggq4Ev295jcJhZFQ6e5dcBpSfN-KNLV92TQwU39q-zsVeiB8X8GAJKujnizQyRnhx8ZVwExy14UxDrCHn0c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه: زیرساخت‌ها و تاسیسات مهم پایگاه‌های آمریکایی در کویت و بحرین مورد اصابت قرار گرفتند
🔹
سپاه پاسداران: ملت شریف ایران، ملت کریم و مجاهد عراق؛ آفرین بر شما مردمان مومن و بصیر و وفادار که با موقع شناسی و تشییع بی‌نظیر در تاریخ جهان قدر و منزلت ولایت الهی…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/448708" target="_blank">📅 16:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448707">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae2a9a6e61.mp4?token=Ve39XS7a-m9lkwvuXpAfjrMivW2apuT2A1ATwxVVsMuTpHIJ3mIvnUkdMTDGPHH7GKfqLqvge9KO2Wge6wFsY21PpkjVyN0JlpIgr2ZnjfXM-mirendMlYJ_0vwfFWhPAJQiaFhvxYmHVh8HaK3w2i_1_uzoAxvmBCODRh0Vkd96QyNNdYhWtWtn00XghY69QAXV58ZMkJGb0ZGMlOgi-Ro-fEu8mq7ZulDSOWZhH33W0Xuw7J6ERvCS1SydVr3AtKkRH0sx4DQLP3CBfltoE-XntfFlkoonwtQBhNBu1Sjr7vH0E4XcAAGtStfX3r_-Ok_1xCjh2kV_GQdphm67ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae2a9a6e61.mp4?token=Ve39XS7a-m9lkwvuXpAfjrMivW2apuT2A1ATwxVVsMuTpHIJ3mIvnUkdMTDGPHH7GKfqLqvge9KO2Wge6wFsY21PpkjVyN0JlpIgr2ZnjfXM-mirendMlYJ_0vwfFWhPAJQiaFhvxYmHVh8HaK3w2i_1_uzoAxvmBCODRh0Vkd96QyNNdYhWtWtn00XghY69QAXV58ZMkJGb0ZGMlOgi-Ro-fEu8mq7ZulDSOWZhH33W0Xuw7J6ERvCS1SydVr3AtKkRH0sx4DQLP3CBfltoE-XntfFlkoonwtQBhNBu1Sjr7vH0E4XcAAGtStfX3r_-Ok_1xCjh2kV_GQdphm67ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید در آغوش مردم مشهد
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/448707" target="_blank">📅 16:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448706">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11318f247d.mp4?token=PuZmvt3KKINmzuygLYaFcrVFm9httVSD4-IhexI6tGjsH_M4vvbbed9PeM-421BYdHK-UQdT7go87G6uf_fyKJ__eq9M6jqls74DLixdDU3zWeThrMsuO1IkOrY-ki1KaDbZcAa9HW5uhvuGgBDgqNhHVPiULH8tHGOk86DDSpgHZm-HY6Rh8wuue4Wr3DRpCGi10dyIIDg0vuKVqcvzptYk_3OicH-wTYyj5G-37vXuG_cTI4s92zeKuuNEylv5Uez35fcdKjKy0RvF3MQCDUXLi4Vhq2f1JyuXONxx4Fv2uaLtxPKfdB5rC5YG7bLZgLMN6Pml-GXt5fjJOTZm6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11318f247d.mp4?token=PuZmvt3KKINmzuygLYaFcrVFm9httVSD4-IhexI6tGjsH_M4vvbbed9PeM-421BYdHK-UQdT7go87G6uf_fyKJ__eq9M6jqls74DLixdDU3zWeThrMsuO1IkOrY-ki1KaDbZcAa9HW5uhvuGgBDgqNhHVPiULH8tHGOk86DDSpgHZm-HY6Rh8wuue4Wr3DRpCGi10dyIIDg0vuKVqcvzptYk_3OicH-wTYyj5G-37vXuG_cTI4s92zeKuuNEylv5Uez35fcdKjKy0RvF3MQCDUXLi4Vhq2f1JyuXONxx4Fv2uaLtxPKfdB5rC5YG7bLZgLMN6Pml-GXt5fjJOTZm6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ پرواز جنگنده‌های ارتش برای تامین امنیت آسمان مراسم تشییع
🔹
پیگیری‌ خبرنگار فارس در مشهد نشان می‌دهد پرواز جنگنده‌های ارتش در استقبال از پیکر مطهر رهبر شهید و برای تامین امنیت هوایی آسمان مراسم تشییع بر فراز خیابان‌های منتهی به حرم مطهر رضوی انجام شده‌ است.…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/448706" target="_blank">📅 16:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448699">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xws1Lf93-iT1K7GmI0j5jDvCfY3KO99xRpUmyjHZjWpLNLUM97icuWyp4n8-X55AZl1YyLVw8Mh55N5fc9NN4H90XM-82mURmAIh9mgnyT8zVyzLb9INTZjG1Tl87wNqZzIMN3QHjxT1eVZlHnhds-m2bceUpds8id14v_oXuvxJYM1sSYCub-Qj3ucdp-5CwaPvvGvrqiCd0UpuqKw-d5fTp1n1LFSccsue458Jf5v2eMgjx6T6AzfmydtsuxHKnfkvbOiuFX8EHtaY4jhssl_rfNrzdx8O4jQvr6kxSQdRgIt4WkLgFxkuQYKvHtkWF92nCRy5NeJoLx5WBW20xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UqrC9zYfqsXvpuRoAEz7R4ouzEv5BG3WWeEH0bxLBqPDP6s8aZ3PLXvJ6h8g0j6avwbz2FV_g2cjVt2dATIkLhUz87brpmlfOFgmcSSQHrRWYv6XLNvk0WEbrOE-PlBCOhOpAxt2LU-sS7gPN-UNVJXIu7f2RvED0X7_yz0jZ3jAlWqjpzEBUKUSokNgy537Y3tGqovhFVOAh_AYjWmCbHo3vJcRK1EDQW87ZOUTVcR4UyOj-2tR08PNwKtcxo8fgNsQxbDmfE3midNxkVYSwfvzOT1lVsgIYqvHXLh2qRF1bAqS1LHWGIAtVBd1DOYnNzYj5PH36kTM_6F9SMxcsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rXCbOQkj7pBdOViHEfoK0mKaiWNUqy1_AXVR0-4qocRvEhd4XyVO6-zCxfhlnOeFE4RHYfWvCbAbqjQNFvtbcj2LbyjcidyX3YFHzS0n55_0Wxa_nYsOfB4lIKpH7BpHASRZ0yqXiZS6L5NQgko55ruh-7_CmwdF31LUUZbiaUJ1IsP4_BbkXEdB7B9cgi-rq6gC_p4pF5tz_H9oaPQ4YVOxHrVoRYlwVAwcY9gX1ZpWU7a-iYsNN5egpu-YWUUAY5VjyVF2UmuaNl-lG7CIZVa4V2eB74Cz_a5bxySny2u7cIxjz2-XpPE-hjByDWjkEb-1_iF_e5VpdFHn_qc42Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VfwNN0GgCXngXqx2sC00YZK9TFdMk--ZeY_Sgc0JSuueI3EA-_h1V-1jeuQS1jgCrmWxsmhY_tdh9sVvN7E3--8Vjmrm0h5Z69w2M1TyPAsoOMtnpPYa-jXq7Sc_7_se8hKdYXfAKw5b9vHhr1DDy7N2vw1S9nPqrzG1-jzDd4iWz-oENPym8GjuWEFqqRC1j9aV3ZTVfgpoC8ZeEBTTYVePHcizM8bjBDVvN58eS-j0Ox2aDQLMu-3ilsVcC5EwyN5tjT1ZuO71fsCTIldZ8IevwKVinIbDZcTR5n1WLEFdyX6fCMIF1wLAppL7HQlYBOOyWKkGOSjXaoK50bNt8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rILOs5cRQyy2ZK1C3VcQ9Y7i69Ji5FOjkRoDTZbLeB4baTnck4gji6xdEPDPUI7w34GkkEcgvVbWLKvhhv3kVon-kZJmpggZAJ2Vvc73GnNfrWP_W5MhbO77ZFR-x8zD785CBf44r3C8rjOwsb8Q0kxDu0FMwiH9mlR4oFR_o2wxF_JDzi5AzOJz5rpYWrYaHl8EAQOWTwM8TempoiBFHEBCqfvx9hh-E3jzmG4i1Fvkyiq70UFHqxJW_seEu9eR5tTjCO92txGicx5_Qzyt_Mdphm2LuI69vsEpXblMxCBnSJ-FoS8l3TO-U3w25PzsIOu6lbyFUfNNBkh5gqfvOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YICI4BBatjLtoXmUb626ihGWmhTjjlThwIcR1hvcSUYkBgh5YEJogqSj_wKgOsmlDAXEbEd-wM8uQL7uKLB33efoSOViFjsQ0YzFx2I4tq7SpYKQBVFo5pLoyjztf0iwc6wzb9HEQ6JcOzbWHNg3WYm2NOQChPjqFPbYXOfxUA5t5UHWGGjkQIxIkDqcpWBNVtOF0bwAVgbmCzMqL3dFshZX0-dZUNuPCJxSSYKK8XXvQML2Ga8AKcm1y1WIv1YkYRPfeHK56lw9TgN699fvcw7HZuzJ96qqXKkeRIpy7Pyxi5scy9I60PVcRbhVxRT7bs4bmQEcnQyuUg-WeSMfeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m7Z4NOtJQduyMZXZp_L_MrUnsALbTO5DbTM4Idr7RuXF58cVn5nLTiq-yQ-8kV-pXTRDKTM79PJJT71LgwfdWE-g3EeI77TmvCn3edwYpDt_-hEFNNmiMJSmnLBp5Xw8bHlK-vxw60_W8cmkrxJNwf1JRRV4sL4Sjh4sdKUu7948_m2FhQJ5-W5iVsu7e7KLzkWZtYAax25XFCWDuhD5FTE64tibDr9q90_DuRYdBuQ3J66_hqZQ8qlI7lhkFrNMkabVpGF0uzyLTIs89f0wPbEpLj3THsHCSkaCkHO-LQDHL5NHY4xVwieflMHjIOEPT9bE107dWjrpOPZWZVQXqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خیابان امام رضا(ع) مشهد جای سوزن انداختن نیست
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/448699" target="_blank">📅 16:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448697">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سرلشکر عبداللهی: قاتلان قائدِ شهید را قصاص خواهیم کرد
🔹
با عرض تسلیت و تعزیت به مناسبت شهادت پیشوای مسلمانان و آزادگان جهان، حضرت آیت‌الله‌العظمی امام خامنه‌ای (قدس‌الله نفسه الزکیه)، به محضر حضرت بقیه‌الله الاعظم (روحی و ارواحنا فداه)، رهبر فرزانه انقلاب، حضرت آیت‌الله العظمی امام سید مجتبی حسینی خامنه‌ای (مدظله‌العالی) و امت اسلامی؛ در روزهای گذشته، جهان شاهد خلق حماسه‌ای کم‌نظیر و ماندگار در تاریخ بود.
🔹
آیین تشییع و بدرقه امامِ شهیدِ امت، به عنوان نماد و جلوه‌ای از شکوه، بصیرت، ایمان، جهاد و مقاومت در حافظه بشریت به ثبت خواهد رسید.
🔹
اینجانب‌ ضمن ادای احترام به مقام شامخ آن قائد شهیدِ عظیم‌الشأن، بر خود فرض می‌دانم مراتب سپاس و قدردانی عمیق خویش را از ملت بی‌نظیر، شرافتمند و بزرگ ایران و مردم سلحشور، مسئولان و نیروهای مسلحِ کشور برادر و دوست، عراق، رزمندگان اسلام و تمامی مسلمانان و آزادگان جهان که با حضور بی نظیر و معنادار خود در آیین‌های وداع و بدرقه سیدِ شهیدانِ انقلاب اسلامی و جبهه مقاومت، حماسه‌ای بزرگ آفریدند، ابراز نمایم.
🔹
حضور بی‌سابقه امت اسلامی، فراتر از یک مراسم وداع، فریاد رسای حق‌طلبی و خط بطلانی بر نقشه‌های مستکبران عالم بود که حق و باطل را به‌وضوح از یکدیگر متمایز ساخت. این خیزشِ انسانی، تجلی‌گاهِ پیوند عمیق میان اراده ملت‌های بیدار با مسیر متعالی شهادت است.
🔹
دنیا و سردمداران کفر و استکبار جهانی، به‌ویژه آمریکای جنایتکار و رژیم خبیث صهیونیستی، مبادا حزنِ جاری در چشمان ملت و خروشِ برخاسته از این اندوه را به حساب ضعف بگذارند.
🔹
این سوگ و خشمِ مقدس، در مسیر خون‌خواهیِ قاتلان قائدِ شهید و رهبرِ مسلمانان و آزادگان جهان و شهدای مظلومِ جنگ‌های تحمیلی دوم و سوم، استمرار خواهد یافت و آنان را به سزای اعمالشان خواهد رساند.
🔹
فرزندان برومند و دلاور ملت در نیروهای مسلح، با توکل و یاری خداوند متعال و همراهی ملت‌های مسلمان و آزادی‌خواه، با اقدامی انقلابی، خواب را از چشمان دشمن خواهند ربود و عاملان این جنایات تروریستی را دیر یا زود قصاص خواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/448697" target="_blank">📅 16:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448696">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5479d3f368.mp4?token=lQ7UVfcxHfJQX_lRxPW4rEeQwkNbnKfV72Cbotuh882GOPPRAyfqLjhE3mD0AAbsJufLRTj199-1iG-zIVRZ5bpwWdOBOu7JrtnEdEvW-As31Cn2TTtpEnKxkrrdDrzcPYaHz0V9cKIMXAodjTS89S3dJ0Js0Q8234qyLXMSLGlvgKqDxkv6ohR_A91K59iFmRT1KnWPlCHgxO_bjTbjZ1rYBvl0DJdkRRZ_dr0X5oZNrnhbsI85OsPk1t-6AaWiD7L3gVyeDt0XewSq4yHFGAJGYOhledF7If0jGMne4M8zts50EcwSj7nkoCLseydsXCreYR7ff-ui_oJwnMcbzzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5479d3f368.mp4?token=lQ7UVfcxHfJQX_lRxPW4rEeQwkNbnKfV72Cbotuh882GOPPRAyfqLjhE3mD0AAbsJufLRTj199-1iG-zIVRZ5bpwWdOBOu7JrtnEdEvW-As31Cn2TTtpEnKxkrrdDrzcPYaHz0V9cKIMXAodjTS89S3dJ0Js0Q8234qyLXMSLGlvgKqDxkv6ohR_A91K59iFmRT1KnWPlCHgxO_bjTbjZ1rYBvl0DJdkRRZ_dr0X5oZNrnhbsI85OsPk1t-6AaWiD7L3gVyeDt0XewSq4yHFGAJGYOhledF7If0jGMne4M8zts50EcwSj7nkoCLseydsXCreYR7ff-ui_oJwnMcbzzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از حضور جمعیت عزادار در خیابان‌های مشهد
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/448696" target="_blank">📅 16:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448695">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfae7ebd2a.mp4?token=OIwZwE1Sb7nELE-ivBIEr_272xkeO-ldZ-rUfIPxXr5jXGALIxYY4FchpfvjikOUHCLPTbR4S05TSNZq7y8t8uafwYrMnz_fUs-MsWDPZrdlMbpbjdgEfnBtY88OIsa01aYlQVRON9QIw6sDCz1F5HYjsMRNTSkkhj-wlfrsRMs9COiIOhUBQOSQGC0HbgcSN28PHCtcy7m61E7w5Tr-WWc6rvUXLva8OzdPyWzs4CvEv74bFWuoNOJBGFjDd44EO2Fx_v4KkZJmHc45gnrmAP66MC3sj7UtemO6NcLeIEZY86i8-PwquxMLD9HOZYeOftAuPkGTvvb3rOqVmFIKOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfae7ebd2a.mp4?token=OIwZwE1Sb7nELE-ivBIEr_272xkeO-ldZ-rUfIPxXr5jXGALIxYY4FchpfvjikOUHCLPTbR4S05TSNZq7y8t8uafwYrMnz_fUs-MsWDPZrdlMbpbjdgEfnBtY88OIsa01aYlQVRON9QIw6sDCz1F5HYjsMRNTSkkhj-wlfrsRMs9COiIOhUBQOSQGC0HbgcSN28PHCtcy7m61E7w5Tr-WWc6rvUXLva8OzdPyWzs4CvEv74bFWuoNOJBGFjDd44EO2Fx_v4KkZJmHc45gnrmAP66MC3sj7UtemO6NcLeIEZY86i8-PwquxMLD9HOZYeOftAuPkGTvvb3rOqVmFIKOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج خروشان منتقمان رهبر شهید در چهارراه دانش مشهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/448695" target="_blank">📅 16:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448694">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3326c346ff.mp4?token=iWpIX6vkQ-D4OmViF8c8kRvnC4NiXeWQsEnlHOZ_imV89V6uXb_D5ztLDh23ccb90OpA0g8YnAh1FQt7i-Tf98tIPjavRI00KRKtR4cgzDUWVdIv75zQx8-LxGsckhB2tSv-dYaeHTTMVTuWeqOTAQxkgToQ3FxM4tmm6NTTSh9DSOPOsxjfsFRvGmqZSvmtqJYd2uFT--zsotzk1VtyrUgDAkZnuR4WpvMqGgR1_shmVxrSJ-HDs1o7y8153I-cFJemL-37QZXdDf3B9rjjBMVAY7-Bd734VSyMRsA4iFGc2LNl28mFp22O2yYnCL0Ru7BpjXZ-lbYnzSM3A-ZsZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3326c346ff.mp4?token=iWpIX6vkQ-D4OmViF8c8kRvnC4NiXeWQsEnlHOZ_imV89V6uXb_D5ztLDh23ccb90OpA0g8YnAh1FQt7i-Tf98tIPjavRI00KRKtR4cgzDUWVdIv75zQx8-LxGsckhB2tSv-dYaeHTTMVTuWeqOTAQxkgToQ3FxM4tmm6NTTSh9DSOPOsxjfsFRvGmqZSvmtqJYd2uFT--zsotzk1VtyrUgDAkZnuR4WpvMqGgR1_shmVxrSJ-HDs1o7y8153I-cFJemL-37QZXdDf3B9rjjBMVAY7-Bd734VSyMRsA4iFGc2LNl28mFp22O2yYnCL0Ru7BpjXZ-lbYnzSM3A-ZsZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکوه یک عهد، از بلندای آسمان
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/448694" target="_blank">📅 16:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448693">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeUT8LXmGo6JyrnKUwJivtOhCc5YkgAmMv0mkeoiV3HKP9t0bgdZjXGf2U2-iBCKRVEJz08HUcsalnlHbKHi4eBXzfnddWNjcV1kGWwaQH_XM_dzLlH-ehAdq7wOknNlQcSSWthLrfHHu66b3lLy4qwvjJfeOWy-PORJUWJPL2OkFEvjYZ1GGxN7jRc6nTzLQgLPQMKmcAhBJZlF7cy5ngNCwioZhv_wRrIqcoMsGJDCyeTj4WImkguKd1gUJjj8a7tNMTyfmpM63OZNyUxXZMDUy0R-OYznadF3snYEQqWazMMKGPkXxkpUhI8MOLmLmuiWgHI506XRCtjDiRmKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
شاه پناهم بده...
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/448693" target="_blank">📅 16:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448692">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bb03071a.mp4?token=QmJJBOch42D7RRSUQtI_65MXNJ3v50Z3KZBAWJR2BiAMRnhRHyUXct0u0w-okDuJQe4uHWdfqeJajEiwtoeZ4GmhAer0Z_rihg1ZlorMaierafeil0P4NER-_5jbbNxr_FatH6aybwAZNNHLgm334w4D-z0Ca38w7ZDLHHx5_-GTXZA7wylIjFCBAGdmwPsunOITmn2LbB99sxxp6WwHpFF5pQGR33JIg1ivqpN6FHHZdtIxUWQlXIUq9lmbygDRLT2St4qVendB6AVZfwldsGCxTKhYZ6E6yXb-zblfzyRxJoeucL2CKgbJwPTu6MTE5Og7J3r9_Dll_ol_LQvmHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bb03071a.mp4?token=QmJJBOch42D7RRSUQtI_65MXNJ3v50Z3KZBAWJR2BiAMRnhRHyUXct0u0w-okDuJQe4uHWdfqeJajEiwtoeZ4GmhAer0Z_rihg1ZlorMaierafeil0P4NER-_5jbbNxr_FatH6aybwAZNNHLgm334w4D-z0Ca38w7ZDLHHx5_-GTXZA7wylIjFCBAGdmwPsunOITmn2LbB99sxxp6WwHpFF5pQGR33JIg1ivqpN6FHHZdtIxUWQlXIUq9lmbygDRLT2St4qVendB6AVZfwldsGCxTKhYZ6E6yXb-zblfzyRxJoeucL2CKgbJwPTu6MTE5Og7J3r9_Dll_ol_LQvmHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائر پاکستانی: آقا را خیلی دوست دارم چون رهبر آزادگان عالم است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/448692" target="_blank">📅 16:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448691">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03205958f1.mp4?token=MflrulSSXJsWqLiBMUj2M-qVNLcYQ9KUnX4j_YhA5YHS7yWIWkuEEAlcdEXc1T_EMzbkzLqRnbMio4N-3oBpTN4LkDi4W_wnKnys7s3u64J2DAysxfWBpw6xPIALRvDmFcGrmTyNdp4CN_Flb7DBBoAtfDhx52V5ERjgzva_r4apSH1RQTRsjqFoCsxkdhpZXfvKG4HbqNPqXsBcAsoSmi1NxaRYkOYduXNZtVgQ1klPOV-_DhaWgM2jVE0aZzLmEelMzw0vfJbBjh2uiGm_Je5snZVl_1ac3OZmgWHyslbQtl0KAeFeO6AhIsueguTIBxUHe2hq4PC2mVYApzDiSoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03205958f1.mp4?token=MflrulSSXJsWqLiBMUj2M-qVNLcYQ9KUnX4j_YhA5YHS7yWIWkuEEAlcdEXc1T_EMzbkzLqRnbMio4N-3oBpTN4LkDi4W_wnKnys7s3u64J2DAysxfWBpw6xPIALRvDmFcGrmTyNdp4CN_Flb7DBBoAtfDhx52V5ERjgzva_r4apSH1RQTRsjqFoCsxkdhpZXfvKG4HbqNPqXsBcAsoSmi1NxaRYkOYduXNZtVgQ1klPOV-_DhaWgM2jVE0aZzLmEelMzw0vfJbBjh2uiGm_Je5snZVl_1ac3OZmgWHyslbQtl0KAeFeO6AhIsueguTIBxUHe2hq4PC2mVYApzDiSoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج خروشان آخرین بدرقۀ رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/448691" target="_blank">📅 15:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448690">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tl82yo_IwGVqcWu8rgHjlbsdG5pD0zAfanLn-0VkKvPOZjf8tFQHd4hqkGTtgAPQJJLHVqhk3-gSyV6xGw-oUJ_zYbtpavQ3rcfRyCKDQhSJMKJCkpvPxUxTzuDLX3eL6_lnvbc1sfBh_BYfeHaX1itHfQZ2b2kL3XEPZUaP033rpm5YIGVrRL-AkMNWXdsiLrswc7USDkeuIjYEZgasGxqVPEKXJe8NcpSoBhErx5ujxZN9zU2uNidfiSwYQaB3JJ7L_xzeNYhgPA0cqQDzazJg7jNDJBfYB5I1YLWRJswAKAPfbOLLiGFIOCbkORkx4ueDIVE1MKuKHBFuBeeBBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پیام مهمی که امروز از مشهد مخابره شد
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/448690" target="_blank">📅 15:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448689">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a27e5555.mp4?token=MI1jXUUGelEdBae3Fo7uNSrS4P774XWRivCNzwOMzG6YxccJ2utFd6uPcIkexJ4BYxQXZ54m0RFmytdK1SRvUPo-u8ixMl14JcjjYKhej4yUAV8ZdwHIeAP7RSIS0z1Y97RMm1WjMRpaURlT1elBiJTDd27gnAndmUyCzd148xdVmIeYZtcIGBFV5WusUn9WOaY1vh0r0h6eXPu5AaNDAfqSKSW5cj8TicTVYkZW6RGVtDp8oHrE61y5ughcavGqfbwXBdeVOpEZviNqUz-PG1V_RtWce1Q7XD5Tox2blZiIF9sP7oevkP-FZbweYKnQ7_Mi0Ly_--B9hadBctPlEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a27e5555.mp4?token=MI1jXUUGelEdBae3Fo7uNSrS4P774XWRivCNzwOMzG6YxccJ2utFd6uPcIkexJ4BYxQXZ54m0RFmytdK1SRvUPo-u8ixMl14JcjjYKhej4yUAV8ZdwHIeAP7RSIS0z1Y97RMm1WjMRpaURlT1elBiJTDd27gnAndmUyCzd148xdVmIeYZtcIGBFV5WusUn9WOaY1vh0r0h6eXPu5AaNDAfqSKSW5cj8TicTVYkZW6RGVtDp8oHrE61y5ughcavGqfbwXBdeVOpEZviNqUz-PG1V_RtWce1Q7XD5Tox2blZiIF9sP7oevkP-FZbweYKnQ7_Mi0Ly_--B9hadBctPlEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشک و حماسه، زیر سایۀ خورشید
نوای روضه حضرت رقیه(س) در تشییع رهبر شهید در مشهد طنین‌انداز شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/448689" target="_blank">📅 15:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448688">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U67bB6klBHWCR38uwakG9ubWHMqep-GfAKsAQrbsguXvSn3h7M7KJEVrToeEkGzz0OLwM8OgPo3Kwto5N69owy9Tum3keuXaEAVu7NJlmDJikAwxrm706JmJwJhDO569HrrHzDHfVE8M3NOUcTWzYjWLRlFLwDVOxXn6s2mEybJ9no529CXZuVeHTzYUDZbz9hRah2Gjt5WycJcO4Pheo1_FT81vNbGsPkDYG-o8kbWJdidJvHRIYzCMmjso_B1hZHu3VczenRL4rZaK40PMxq0A7OVfujRZfHo7yWH6C13zUDidpE7BXTER3_2LmzExmrSQeYhVXbC7YK7o1FVunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
قاب ماندگار از تشییع رهبر شهید در مشهد  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/448688" target="_blank">📅 15:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448687">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7626a8268.mp4?token=ThHhso-VM2210D2IhVfr-Vevfp2wufnF3WQ7wf9RMHmeYM6q_rlT6YQrTpqG0VODAcrcuox6gFhLVAyiGJZird62n2RlPRFjKAl3xu7Yu5ZxOfzckp6A7XBHIW2SQHHk-h6XKyihQuv3rDZqd3Yg1_Kw2g86ovzwqag10VM_EphARZcqlWNmB9-jTpq4Yb4sIgO3PyqpYNETFeZZVbpzvIV6jPffi1T4WpS6qt4ZF6DTZ3HAG2wV0XcLFN3w7LE1Et1Vt37-DKwSPXIMP7dgP1UZv2Wvlot27CIPBVjV-9J3wNIU9P69x6zvbnudn9WcKvHmXlMMRDZ15cwpun2ozQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7626a8268.mp4?token=ThHhso-VM2210D2IhVfr-Vevfp2wufnF3WQ7wf9RMHmeYM6q_rlT6YQrTpqG0VODAcrcuox6gFhLVAyiGJZird62n2RlPRFjKAl3xu7Yu5ZxOfzckp6A7XBHIW2SQHHk-h6XKyihQuv3rDZqd3Yg1_Kw2g86ovzwqag10VM_EphARZcqlWNmB9-jTpq4Yb4sIgO3PyqpYNETFeZZVbpzvIV6jPffi1T4WpS6qt4ZF6DTZ3HAG2wV0XcLFN3w7LE1Et1Vt37-DKwSPXIMP7dgP1UZv2Wvlot27CIPBVjV-9J3wNIU9P69x6zvbnudn9WcKvHmXlMMRDZ15cwpun2ozQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار یک‌صدای مشهدی‌ها: ارتشی، سپاهی، انتقام انتقام
🙍‍♂️
ارسالی مخاطبان به
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/448687" target="_blank">📅 15:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448686">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fa16352e1.mp4?token=cIO2_tD6HWcXiP9lzMRzJN7Txe1WxqAbYrIUuOvARzvhsq6U20RVUxysV36rjsrijdxQtymR7BWGK_lFnPjLbwZ15Pq7u5p6N3K2Ptes9Yts9d5r18BOZNgr5I96DYXHD9Lug3UyNoAvpCmneAdThO3zDXf13Rf2Z55b0M0P1xfU02lVNUCcBKzLyM_mkUiEIu69jJhSaeOn0G0QPa9gOgFG_8zQVb_ZekyaPRyjKhKAVgcJ2IazDq_1qtj0eFTNOTfepRCPeCSOc7H0ypnRSY7uflOU8jtRixLmHzN3dzZ9LovMoCHKPztK5d1NehAOHhdNWPwtxZgHMjbS8YEyAoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fa16352e1.mp4?token=cIO2_tD6HWcXiP9lzMRzJN7Txe1WxqAbYrIUuOvARzvhsq6U20RVUxysV36rjsrijdxQtymR7BWGK_lFnPjLbwZ15Pq7u5p6N3K2Ptes9Yts9d5r18BOZNgr5I96DYXHD9Lug3UyNoAvpCmneAdThO3zDXf13Rf2Z55b0M0P1xfU02lVNUCcBKzLyM_mkUiEIu69jJhSaeOn0G0QPa9gOgFG_8zQVb_ZekyaPRyjKhKAVgcJ2IazDq_1qtj0eFTNOTfepRCPeCSOc7H0ypnRSY7uflOU8jtRixLmHzN3dzZ9LovMoCHKPztK5d1NehAOHhdNWPwtxZgHMjbS8YEyAoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب ماندگار از تشییع رهبر شهید در مشهد
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/448686" target="_blank">📅 15:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448685">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3cb84d9de.mp4?token=LvqZGgI6tlKtsW5aWaftDHNIaM838CzmrROUJZP_rqGp6p_rHXLLHmyL9I1VsnS7n5xCv0LHyx5Ekb9WQKNYYWhLf9BlvPs9rhr4cKxUXjhRB1px-S57XCMnKYIwK-G2R-yW04aI27yJfNE1DptlixTFA9TXcjElpLM3R4f-p7ZR1SLb_pKzg0wQltvaB1P0C1yX05QlICU-7CjZxj2EFB98necgkl_YpPDOJ10eBNc107bGyrCYtqwv3g8JvDBNKtJV8jr8-fh7wnLfsuirjkoNxhNz0_P51z5J_AbBQDUKKwVVaAmidRFVhePeITCs9U32KE8hglcgOtrPSc7d9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3cb84d9de.mp4?token=LvqZGgI6tlKtsW5aWaftDHNIaM838CzmrROUJZP_rqGp6p_rHXLLHmyL9I1VsnS7n5xCv0LHyx5Ekb9WQKNYYWhLf9BlvPs9rhr4cKxUXjhRB1px-S57XCMnKYIwK-G2R-yW04aI27yJfNE1DptlixTFA9TXcjElpLM3R4f-p7ZR1SLb_pKzg0wQltvaB1P0C1yX05QlICU-7CjZxj2EFB98necgkl_YpPDOJ10eBNc107bGyrCYtqwv3g8JvDBNKtJV8jr8-fh7wnLfsuirjkoNxhNz0_P51z5J_AbBQDUKKwVVaAmidRFVhePeITCs9U32KE8hglcgOtrPSc7d9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شبی که شهادت رهبر انقلاب عراقی‌ها را تکان داد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/448685" target="_blank">📅 15:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448684">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b17be43a7.mp4?token=tlXUzqMOixo06XrSkiVnMHF2PSWJDYbYN_c_9vUTUggzxc2Y4DXujv97AoUP6pqWitZ-gW_U5elWr3FiJA5CqFLm6vr-1KHOxxtEX9HagSuF3E1h_A72hLd6dBw-BbkatBTb5D9tVxJG6gN9ANOC28womvpAQinvQnh1RcqDOBcAn0DymXYnzym51yRXhxxsMnZ0eWqN85VDM_I6mURr0VC7bE3keLGr4AxdXABtxDEuIpD2DQh8ppPglGld2wbiu9eNQTG98K-9J9BUpIN0cek4dmR2KBKxLVue9xMbMTorhuxokIzNkweYMnBxCTxXFAZHs94lG56kwnEGYZpL5wqnh4pyDXio5JIfuJtMc-WzDAIRKpe64KrO1JZbZmfDM4Iqax3b2iyRvyWAhVdOEvDFJJoK0UohIC0h_2Pk1vtnFRUzpPQxuX9tYkDc5pFbU2v4-C0ObNI0ThDujUVfLuM8tOZyYPqgcnqV-iLB2js5Glv9kbMfYEWeJC9Kjl5DEVnVUvZzANje8zC7h1KWXoqwbtH19RA9hBj7ZFPwU4G8VM8pjFU5qbuve3GESGeQ3vIFGhlw1MrANMXyRlvmPmWo_kGRgoJ2qfaYxkAT6RkvR0KxVC-7YOMjcHvdj6M0_eBfH_1QxXQj4aHbyXH--K28lQRmDlff2vBTA_PvKw8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b17be43a7.mp4?token=tlXUzqMOixo06XrSkiVnMHF2PSWJDYbYN_c_9vUTUggzxc2Y4DXujv97AoUP6pqWitZ-gW_U5elWr3FiJA5CqFLm6vr-1KHOxxtEX9HagSuF3E1h_A72hLd6dBw-BbkatBTb5D9tVxJG6gN9ANOC28womvpAQinvQnh1RcqDOBcAn0DymXYnzym51yRXhxxsMnZ0eWqN85VDM_I6mURr0VC7bE3keLGr4AxdXABtxDEuIpD2DQh8ppPglGld2wbiu9eNQTG98K-9J9BUpIN0cek4dmR2KBKxLVue9xMbMTorhuxokIzNkweYMnBxCTxXFAZHs94lG56kwnEGYZpL5wqnh4pyDXio5JIfuJtMc-WzDAIRKpe64KrO1JZbZmfDM4Iqax3b2iyRvyWAhVdOEvDFJJoK0UohIC0h_2Pk1vtnFRUzpPQxuX9tYkDc5pFbU2v4-C0ObNI0ThDujUVfLuM8tOZyYPqgcnqV-iLB2js5Glv9kbMfYEWeJC9Kjl5DEVnVUvZzANje8zC7h1KWXoqwbtH19RA9hBj7ZFPwU4G8VM8pjFU5qbuve3GESGeQ3vIFGhlw1MrANMXyRlvmPmWo_kGRgoJ2qfaYxkAT6RkvR0KxVC-7YOMjcHvdj6M0_eBfH_1QxXQj4aHbyXH--K28lQRmDlff2vBTA_PvKw8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرد مینابی ۲۵ شهید داده، اما خود را برای خون‌خواهی رهبرش به مشهد رساند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/448684" target="_blank">📅 15:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448683">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">محل خاک‌سپاری رهبر شهید در نزدیکی روضۀ منوره است
🔹
رئیس اداره اطلاع‌رسانی و رسانۀ حرم رضوی: پیکر مطهر رهبر شهید و خانوادۀ ایشان پس از آیین تشییع و اقامه نماز به یکی از رواق‌های نزدیک به روضه منوره منتقل خواهد شد و مراسم تدفین در آن مکان با حضور خانواده و بیت رهبر شهید انقلاب انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/448683" target="_blank">📅 15:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448682">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a81c3bb0a.mp4?token=d21_OzxmnBU5nUKhgPHJkDhUe9LCVR_b8sUJtKgiYHZRaVCs30efVm7JZlPtSt-8Il6gbSjVP16dieo9_jb6Ra84-QS8LnBlSXUlWn1DV42uuKPqOZMfR_RNxEQFCca6pVwFBH4NgmNtxLtBFsTDwc4OtFfn0-GFYgWfDWgBmcPyQ_XEw6XJAmi_-X8rEgT_3xINVeS0ePW82qMHFPRP5o-hXwTqLZZePI_CuvIzKxTWiQvrY30AZTLdS1nvnsLFhSJsd_HYVpC9TxLpDiQEc3cOhzMUW9KLW1XCbFUR--V7pjh9FcEFwvrha4vffeOwQhbM9uJIQjnql9dMMRPYqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a81c3bb0a.mp4?token=d21_OzxmnBU5nUKhgPHJkDhUe9LCVR_b8sUJtKgiYHZRaVCs30efVm7JZlPtSt-8Il6gbSjVP16dieo9_jb6Ra84-QS8LnBlSXUlWn1DV42uuKPqOZMfR_RNxEQFCca6pVwFBH4NgmNtxLtBFsTDwc4OtFfn0-GFYgWfDWgBmcPyQ_XEw6XJAmi_-X8rEgT_3xINVeS0ePW82qMHFPRP5o-hXwTqLZZePI_CuvIzKxTWiQvrY30AZTLdS1nvnsLFhSJsd_HYVpC9TxLpDiQEc3cOhzMUW9KLW1XCbFUR--V7pjh9FcEFwvrha4vffeOwQhbM9uJIQjnql9dMMRPYqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار «یالثارات الحسین علیه‌السلام» ملت غیور ایران در لحظات ابتدایی تشییع پیکر مطهر «آقای شهید ایران» در مشهد مقدس
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/448682" target="_blank">📅 15:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448679">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd499f35e.mp4?token=JykKbxkhXPdHgAehuUPHn2T2mXurO2HwJc0xXJOB079Yhly1f2hD0cBHyslUdF9VhEVVhFM4--azrg1MUndDaqiDOC9KqzdJGUShivrAvwGhwzYgU20Dw9hb59PtCCOsdHglY2fYCSY6b3y6NwlIJio7Wewc41X6ShMw9ceiZFF8HSLyolrUcUJ_xlG2S6stXmoETSeVV6XQg_ykkQ7zpkziZgy29w6kdd8W0Au7bb08dAxwz0IH9fWUG35wKAizVzYd7GHFt0gJJtR-Drdvc5IM1pMe7oHeIr-EOsAuAl0tS9jsl-EOeerOJ1fctBdEWpvN4fSr2EnJCSiVSn0mgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd499f35e.mp4?token=JykKbxkhXPdHgAehuUPHn2T2mXurO2HwJc0xXJOB079Yhly1f2hD0cBHyslUdF9VhEVVhFM4--azrg1MUndDaqiDOC9KqzdJGUShivrAvwGhwzYgU20Dw9hb59PtCCOsdHglY2fYCSY6b3y6NwlIJio7Wewc41X6ShMw9ceiZFF8HSLyolrUcUJ_xlG2S6stXmoETSeVV6XQg_ykkQ7zpkziZgy29w6kdd8W0Au7bb08dAxwz0IH9fWUG35wKAizVzYd7GHFt0gJJtR-Drdvc5IM1pMe7oHeIr-EOsAuAl0tS9jsl-EOeerOJ1fctBdEWpvN4fSr2EnJCSiVSn0mgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی محمود کریمی و میثم مطیعی در کنار پیکر مطهر رهبر شهید در پرواز تهران به نجف
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/448679" target="_blank">📅 15:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448678">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpstmxf_33KnIGM2zN5B3101zzjcMOSKdexMwMKbFFgY2PY74D8I9xiTVd7AWlRxFV0y2Tp9Q8As-I9-IxywbMGhwdxsvdwFzpyWs1QAGN2oJl3YzrytiRmsW84j6H0wbbBLCeO44-E47bmpQVzgn4IhIpvKl72pgbfq0XI-KTyWvNgbjogOQBxbGdufXyP8oK3xHCyg5OiHy-mCO4Vl4MUz2BM-2AgOfuFSu0y0GXHnyq7oOMnqVo6sJX2ERGGfSfmPD0MZPNYtLqZ0GPgitvnpu6eJoUO5-zsaedtrAh1dMnINFls-6k_G9r31tY0bA9jiPtxw9y2XAPG5oSnc6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروی دریایی سپاه: ماجراجویی‌های ارتش تروریستی آمریکا پاسخ کوبنده ما را به دنبال خواهد داشت و روند بازگشایی تنگه هرمز را با اختلال مواجه می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/448678" target="_blank">📅 15:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448677">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNbaWJ2OlaB7PpCuADTNZqFskKBXz6SofW5kagqEiAU6-wjXrqQ0cGcAk4qboAdWyUtleqnhvpFeyQHShubdT3zYymajTq8Y9DNQ-JveV3g5Y2OzB_W9Y9HRjDXiaiGfIN35XhyVq9XgQY6fkvAiTszXuv_N2MgNB6v6UL_NNhCMKdW80S2BJH5r7DMpmvL08CRE748Gjx7x-8G2lu1g8sNiXnxkCn-pBf1qhiX1Zyj0Eq7oOj6Y8GL0F38CQH4KiTNFXX7BpfMN6g71bEJKIPWtYEdiZQngd5LROzy-cxa0_l3z_6fmdosovyxDazoWHVdgtsLkIp6UMtoc3zTpMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یکی از نیروهای مرزبانی هرمزگان در حملۀ آمریکا
🔹
ستوان‌سوم حمید زارعی حاجی‌آبادی، از نیروهای مرزبانی استان هرمزگان، ساعت ۰۱:۳۰ بامداد روز هفدهم تیرماه، در جریان حملات هوایی رژیم صهیونیستی و آمریکا در محدوده بندرکوهستک، هنگام انجام مأموریت به شهادت رسید.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/448677" target="_blank">📅 15:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448676">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgILGxcQIOeH75eAe97sNdSx7OLEgwg5F0hovV61Z0DlyB0ffNA0lmkumY7HXFr04e1nSiQxaEf57a35_GM5L-FNj9WTBUihUcasTXGd-v-q3F8j8_EJeaoIORsiDGvjLfDNb5OvVGxc1OT3QS1Ow7AZQqL-VvzZ2K_I0cX3WLbvti6EUC6VUQGEu45LMVnM71thHwIAGBJGtx3sqPPbfGdIF24psDh-qWv2bImN3KTIC3UbjQGwS4RrFWHZb5OW36Gb7PYfEpRSJvYGAu-zu0U377RH-OnA_yxVSXGJKNEBERkv2iFT56BbQMCFRkOIZMPD-cfHds3-Iqlbz2tZbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
شنیده‌شدن صدای چند انفجار در چغادک بوشهر
🔹
دقایقی پیش مردم شهر چغادک استان بوشهر صدای چند انفجار شنیدند. هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است.
🔸
ساعتی پیش هم مردم بخش‌هایی از بوشهر از شنیدن صدای انفجار خبر داده بودند. همچنین صبح امروز…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/448676" target="_blank">📅 15:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448675">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6394a96b6.mp4?token=el3a5Xxyk2FVhxUltGC0kv4NR1WSNcl0OWM321NzTCzjM_ripTzzJ8J5TbikN9HNylLCx-1aMtYlfeWtf-vPTvmbpDCigq6w2KpO9hWe3yS5E44Ja5seI4KE9vXX1NiiakdVsDC0oBwQ4QSEUQB56uUu5Jcqc0L7sC1G5f4lwNkKsLhynTYAPexXfllSGWqqFtybi9IPCCrgFHH0A1gI5TDhFaAC8xYZujBtwmH7tnC8CVqhIJxZ2XIWtzolRLHJzd9R1VJCPQRCDSt7S9pysnMGJn73XP6D-0XWoect2ZTdWVwM6h-zyQmmkEFWaA3QVQn4uF2eIeDy_lpbIavXpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6394a96b6.mp4?token=el3a5Xxyk2FVhxUltGC0kv4NR1WSNcl0OWM321NzTCzjM_ripTzzJ8J5TbikN9HNylLCx-1aMtYlfeWtf-vPTvmbpDCigq6w2KpO9hWe3yS5E44Ja5seI4KE9vXX1NiiakdVsDC0oBwQ4QSEUQB56uUu5Jcqc0L7sC1G5f4lwNkKsLhynTYAPexXfllSGWqqFtybi9IPCCrgFHH0A1gI5TDhFaAC8xYZujBtwmH7tnC8CVqhIJxZ2XIWtzolRLHJzd9R1VJCPQRCDSt7S9pysnMGJn73XP6D-0XWoect2ZTdWVwM6h-zyQmmkEFWaA3QVQn4uF2eIeDy_lpbIavXpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی یک جنگنده F-16 نیروی هوایی یونان پس از فرود اضطراری در فرودگاه زاکینتوس
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/448675" target="_blank">📅 15:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448674">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6648536b.mp4?token=kFjuwURnje4oFitCe4xUA8fmI9uB4fHYFt5yQnhvOLmy_Y0ddzBNxS-t1xdv0xKmvixnWSCehQCQmD9kD7ueZtAvz8XvLFL4fyKSxI4yE0pT6b1r7XS6yppnTbU5_iaF97DHsfyIjxyoIpT94mucC2L8e17SwmuVWDOGPQHYBu1F2Zc2fUlNzYjJ1CWt7muRnzz4OhS5EzfyR74poTKqnkfHet0Q35iLQqyzgROdpvcic6ZSHtDZqKUHm6JeQkZB85bh7qNpOMGID1gXgUu6CzImgELb_f8dkVArfPQnxV91g1AKAKMH-myCl5JTKycle83YHYoac6kqM5l5_D0ONQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6648536b.mp4?token=kFjuwURnje4oFitCe4xUA8fmI9uB4fHYFt5yQnhvOLmy_Y0ddzBNxS-t1xdv0xKmvixnWSCehQCQmD9kD7ueZtAvz8XvLFL4fyKSxI4yE0pT6b1r7XS6yppnTbU5_iaF97DHsfyIjxyoIpT94mucC2L8e17SwmuVWDOGPQHYBu1F2Zc2fUlNzYjJ1CWt7muRnzz4OhS5EzfyR74poTKqnkfHet0Q35iLQqyzgROdpvcic6ZSHtDZqKUHm6JeQkZB85bh7qNpOMGID1gXgUu6CzImgELb_f8dkVArfPQnxV91g1AKAKMH-myCl5JTKycle83YHYoac6kqM5l5_D0ONQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نظم ایرانی در تنگۀ هرمز همچنان برقرار است.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/448674" target="_blank">📅 15:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448673">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/788f652c2a.mp4?token=TDbXgnqqyg9qmRLpjjcTEDAhPziFF6dCDMyuCOKdEKskkIMzGK6txa6aB8ogv0gbsqycHmlbpBUGtoVi5KCqEr6tdGWsAw7JyokWnshQ__mqo8Syye-CywKJ7__dmBcwzfT69ZTy7w5S75P303tqA15E2vNzzGw2E_6hCXqPgThMVCw3Yhl0Ud0dfLgy78nAJghYbjG9RNr964ua60txEQKx3x0jCZGU5W0tFmLJEycprhQsagpsY2s-pQ3-ch37Fu7y5ZRJckXucIn7yAH5WgGPL5Q_nfot80x6ewKiBXRt1N0lDr5HIfeuPe5gwnC-HQzly8BQOAhbjGABn37ATw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/788f652c2a.mp4?token=TDbXgnqqyg9qmRLpjjcTEDAhPziFF6dCDMyuCOKdEKskkIMzGK6txa6aB8ogv0gbsqycHmlbpBUGtoVi5KCqEr6tdGWsAw7JyokWnshQ__mqo8Syye-CywKJ7__dmBcwzfT69ZTy7w5S75P303tqA15E2vNzzGw2E_6hCXqPgThMVCw3Yhl0Ud0dfLgy78nAJghYbjG9RNr964ua60txEQKx3x0jCZGU5W0tFmLJEycprhQsagpsY2s-pQ3-ch37Fu7y5ZRJckXucIn7yAH5WgGPL5Q_nfot80x6ewKiBXRt1N0lDr5HIfeuPe5gwnC-HQzly8BQOAhbjGABn37ATw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد خون‌خواهی مردم عزادار با مشت‌های گره‌کرده در مسیر تشییع پیکر مطهر رهبر شهید انقلاب در مشهد مقدس
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/448673" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448672">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
الجزیره: آژیرهای خطر در چندین منطقه اردن فعال شد.  @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/448672" target="_blank">📅 15:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448671">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
منابع عراقی: آژیرهای خطر در پایگاه آمریکایی «حریر» در استان اربیل در شمال عراق به صدا درآمد
.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/448671" target="_blank">📅 14:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448670">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🎥
همراهی جنگنده‌های ارتش با هواپیمای حامل پیکر رهبر شهید انقلاب و شهدای خانواده ایشان، لحظاتی قبل از ورود به فرودگاه شهید هاشمی‌نژاد مشهد.  @Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/448670" target="_blank">📅 14:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448668">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7258b3fb74.mp4?token=R64H0qE6i5rCmcIjKuxfAJwYTjWrRmZjG1fqzinEZBzzhLZ86wcwqu66EMmVEwaqGgZUFmFmxZh4h8k7_pKURf_uVN4V8scB6NJlOKGVpYvDxIo78WrN-Pk0Zf2n2xe36Jn0J11PPiPLMXZnrnIjHwwweEs7_kZAt7GCcZKh9kIP0AjzQ1HJCSA6w0X1f10MuZR64x11B1_MnzxOo56183I7FJvMgPMulQOI3PY2OdVsbQTgmdYQpdEQAmQq6Jg0NTd5Qfb8T1AI0o12O77GbqKiU4nnAJ60ejpXsfhuEHagchi0SJSq-U4p8LrXBsP2uCokwuJKZXCwLjUcAp8KRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7258b3fb74.mp4?token=R64H0qE6i5rCmcIjKuxfAJwYTjWrRmZjG1fqzinEZBzzhLZ86wcwqu66EMmVEwaqGgZUFmFmxZh4h8k7_pKURf_uVN4V8scB6NJlOKGVpYvDxIo78WrN-Pk0Zf2n2xe36Jn0J11PPiPLMXZnrnIjHwwweEs7_kZAt7GCcZKh9kIP0AjzQ1HJCSA6w0X1f10MuZR64x11B1_MnzxOo56183I7FJvMgPMulQOI3PY2OdVsbQTgmdYQpdEQAmQq6Jg0NTd5Qfb8T1AI0o12O77GbqKiU4nnAJ60ejpXsfhuEHagchi0SJSq-U4p8LrXBsP2uCokwuJKZXCwLjUcAp8KRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج خون‌خواهی در مشهد؛ خیابان‌های امام‌رضا (ع) سرخ‌پوش شد
🔹
خیابان‌های منتهی به حرم مطهر رضوی مملو از جمعیتی است که از ساعات پیش برای تشییع پیکرهای مطهر شهیدان حضور یافته‌اند.
🔹
مردم با سر دادن شعار «لبیک یا حسین» و برافراشتن پرچم‌های سرخ خون‌خواهی، خیابان…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/448668" target="_blank">📅 14:35 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
